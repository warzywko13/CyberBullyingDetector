from transformers import BertTokenizer, BertForSequenceClassification
import torch

class Evaluation:
    def __init__(self, model_path):
        tokenizer = BertTokenizer.from_pretrained(model_path)
        model = BertForSequenceClassification.from_pretrained(model_path)
        self.model = model
        self.tokenizer = tokenizer
        self.model.eval()

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)

        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            predicted_class = torch.argmax(logits, dim=1).item()

        return predicted_class