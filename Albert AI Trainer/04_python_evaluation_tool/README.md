# Python AI Response Evaluation Tool

A beginner-friendly command-line tool that reads a response-evaluation CSV, validates 1–5 scores, calculates average scores by criterion, and flags responses with low accuracy.

## Requirements
- Python 3.9 or newer
- No third-party packages required

## Run
From this folder, run:

```bash
python evaluate_responses.py ../01_ai_response_evaluation/evaluation_dataset.csv
```

If you copy the CSV into this folder, run:

```bash
python evaluate_responses.py evaluation_dataset.csv
```

## Limitations
This tool summarizes human-entered scores; it does not independently determine whether an AI response is correct. The quality of the report depends on the quality and consistency of the evaluator's judgments.
