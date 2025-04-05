import argparse

def parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Application for data preprocessing, model fine-tuning, and prediction."
    )

    parser.add_argument(
        "--preprocessing",
        "-p",
        action="store_true",
        help="Perform data processing"
    )

    parser.add_argument(
        "--train",
        "-t",
        action="store_true",
        help="Train the model."
    )

    parser.add_argument(
        "--test",
        "-e",
        action="store_true",
        help="Test the model."
    )

    return parser.parse_args()