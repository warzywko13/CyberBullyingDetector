import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from app.models import Comments

def admin(request: HttpRequest) -> HttpResponse:
    """
    Show admin page.

    Args:
        request: request: Request from django inlude data

    Returns:
        HttpResponse: rendered page
    """
    comments = Comments.objects.filter(is_toxic=True, deleted_at=None)

    return render(request, "comments/admin.html", {
        "comments": comments,
    })

def approve_comment(request: JsonResponse) -> JsonResponse:
    """
    Untoxic comment.
    """
    try:
        data = json.loads(request.body)

        comment = Comments.objects.get(id=data["id"])
        comment.is_toxic = False
        comment.save()

        return JsonResponse({
            "success": True,
            "message": f"Komentarz {data["id"]} został odznaczony jako toksyczny",
        }, status=201)
    except (json.JSONDecodeError, KeyError) as e:
        return JsonResponse({
            "error": str(e)
        }, status=400)

def deny_comment(request: JsonResponse) -> JsonResponse:
    """
    Delete comment.
    """
    try:
        data = json.loads(request.body)

        comment = Comments.objects.get(id=data["id"])
        comment.delete()
        
        return JsonResponse({
            "success": True,
            "message": f"Komentarz {data['id']} został usunięty",
        })
    except (json.JSONDecodeError, KeyError) as e:
        return JsonResponse({
            "error": str(e)
        }, status=400)