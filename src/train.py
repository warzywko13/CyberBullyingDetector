from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, classification_report)

from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import numpy as np

class Train:

    @staticmethod
    def execute(df, file_manager):
        X_train, X_test, y_train, y_test = train_test_split(df['clean_message'], df['label'], test_size=0.2, random_state=42)

        tokenizer = BertTokenizer.from_pretrained("dkleczek/bert-base-polish-cased-v1")

        def tokenize(example):
            return tokenizer(example["text"], padding="max_length", truncation=True, max_length=128)

        train_dataset = Dataset.from_dict({"text": X_train.tolist(), "label": y_train.tolist()}).map(tokenize)
        test_dataset = Dataset.from_dict({"text": X_test.tolist(), "label": y_test.tolist()}).map(tokenize)

        model = BertForSequenceClassification.from_pretrained(
            "dkleczek/bert-base-polish-cased-v1", num_labels=2
        )

        training_args = TrainingArguments(
            output_dir="/tmp",
            num_train_epochs=3,
            per_device_train_batch_size=16,
            per_device_eval_batch_size=32,
            evaluation_strategy="epoch",
            save_strategy="no",
            logging_steps=10,
            report_to="none",
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            compute_metrics= Train.compute_metrics
        )

        trainer.train()

        preds = trainer.predict(test_dataset)
        y_pred = np.argmax(preds.predictions, axis=1)

        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy:", accuracy)

        report = classification_report(y_test, y_pred)
        print("\nClassification Report:\n", report)
        with open(file_manager.classyfication_report, "w", encoding="utf-8") as f:
            f.write(f"Accuracy: {accuracy}\n\n")
            f.write("Classification Report:\n")
            f.write(report)

        model.save_pretrained(file_manager.results)
        tokenizer.save_pretrained(file_manager.results)
    
    @staticmethod
    def compute_metrics(pred):
        preds = np.argmax(pred.predictions, axis=1)
        acc = accuracy_score(pred.label_ids, preds)
        return {"accuracy": acc}