# Project 2 Report: AI Response Preference Ranking

## 1. Overview
This project demonstrates a structured method for comparing two AI-generated responses to the same prompt and choosing the response that better satisfies the user's needs.

## 2. Objective
To practise evaluating candidate responses for factual accuracy, instruction following, relevance, clarity, completeness, safety, and appropriate uncertainty.

## 3. Method
Twenty synthetic prompt-response pairs were created across beginner explanations, instruction following, arithmetic, summarization, general knowledge, reasoning, writing, coding, safety, and uncertainty. Each pair includes a preferred response, a short justification, the relevant criteria, and a note explaining the judgment.

## 4. Decision procedure
The evaluator identifies the user's constraints, checks factual and logical claims, compares both responses using the same criteria, selects the stronger response, and documents the decisive reason. Safety-critical errors are treated as high-severity issues rather than being offset by good writing.

## 5. What the dataset demonstrates
- A concise answer can outperform a longer answer when the prompt requests brevity.
- Correctness and safety matter more than confident tone.
- A response can be factually correct but still fail the user's formatting or audience requirements.
- Some comparisons are close; a responsible evaluator should describe the preference as modest when appropriate.
- The reasoning for a preference is as important as the A/B selection.

## 6. Limitations
The examples are synthetic and were designed for practice. The reference judgments are illustrative and may be debated in context. This dataset does not establish professional experience, production-level annotation quality, or inter-rater reliability. A stronger follow-up study would ask multiple independent reviewers to rank the same responses and compare agreement.

## 7. Next steps
1. Complete the blind-ranking worksheet before viewing the reference labels.
2. Review disagreements and update the guidelines if needed.
3. Add original examples and cite reliable sources for factual checks where appropriate.
4. Publish the reviewed dataset and methodology on GitHub, clearly labelled as an independent practice project.
