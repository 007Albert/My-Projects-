import csv
import argparse
from pathlib import Path
from statistics import mean

SCORE_FIELDS = [
    "accuracy_score",
    "relevance_score",
    "instruction_following_score",
    "clarity_score",
    "completeness_score",
]

def load_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def validate_scores(rows):
    for line_no, row in enumerate(rows, start=2):
        for field in SCORE_FIELDS:
            try:
                value = int(row[field])
            except (KeyError, TypeError, ValueError):
                raise ValueError(f"Line {line_no}: {field} must be an integer from 1 to 5.")
            if not 1 <= value <= 5:
                raise ValueError(f"Line {line_no}: {field} must be between 1 and 5.")

def summarize(rows):
    if not rows:
        raise ValueError("The input CSV has no data rows.")
    validate_scores(rows)
    print(f"Responses evaluated: {len(rows)}")
    print("\nAverage score by criterion:")
    for field in SCORE_FIELDS:
        avg = mean(int(row[field]) for row in rows)
        print(f"- {field.replace('_score', '').replace('_', ' ').title()}: {avg:.2f}/5")
    row_averages = [
        mean(int(row[field]) for field in SCORE_FIELDS)
        for row in rows
    ]
    print(f"\nOverall mean across all criteria: {mean(row_averages):.2f}/5")
    low_accuracy = [
        row for row in rows
        if int(row["accuracy_score"]) <= 2
    ]
    print(f"Responses with accuracy score <= 2: {len(low_accuracy)}")
    if low_accuracy:
        print("IDs needing accuracy review: " + ", ".join(row.get("id", "unknown") for row in low_accuracy))

def main():
    parser = argparse.ArgumentParser(description="Summarize an AI response evaluation CSV.")
    parser.add_argument("csv_path", help="Path to evaluation_dataset.csv")
    args = parser.parse_args()
    path = Path(args.csv_path)
    if not path.exists():
        raise SystemExit(f"File not found: {path}")
    rows = load_rows(path)
    summarize(rows)

if __name__ == "__main__":
    main()
