import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from app.models import Comments
from app.views.helpers.view import View
from src.filemanager import FileManager
from src.evaluation import Evaluation

def index(request: HttpRequest) -> HttpResponse:
    """
    Show index page.

    Args:
        request: request: Request from django inlude data

    Returns:
        HttpResponse: rendered page
    """
    comments = Comments.objects.filter(is_toxic=False, deleted_at=None)

    return render(request, "index.html", {
        "comments": comments,
    })

def add_comment(request: JsonResponse) -> JsonResponse:
    """
    Add comment to the database.
    """
    try:
        data = json.loads(request.body)

        # Predict toxicity
        toxic = predict_comment(data["comment"])

        comment = Comments.objects.create(
            comment=data["comment"],
            is_toxic=toxic,
        )

        if toxic:
            message = "Twój komentarz został oznaczony jako toksyczny! Komentarz zostanie poddany ocenie przez moderatora."
        else:
            message = "Twój komentarz został dodany pomyślnie!"

        comment_view = View(
            view_name="comments/comment.html",
            params={"comment": comment}
        ).render()

        return JsonResponse({
            "view": comment_view,
            "is_toxic": toxic,
            "message": message
        }, status=201)
    except (json.JSONDecodeError, KeyError) as e:
        return JsonResponse({ 
            "error": str(e)
        }, status=400)
    
def predict_comment(comment):
    """
    Predict toxicity of a comment.
    """
    file_manager = FileManager()
    evaluation = Evaluation(file_manager.results)
    toxic = evaluation.predict(comment)
    return toxic