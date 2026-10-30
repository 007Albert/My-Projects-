# Preference Ranking Guidelines

## Project objective
Compare two candidate AI responses to the same prompt, select the better response for that user's request, and provide a concise evidence-based justification.

## Ranking principles
1. **Accuracy first:** prefer correct facts, calculations, and reasoning over confident but incorrect claims.
2. **Follow the prompt:** respect the requested format, length, number of items, tone, audience, and output constraints.
3. **Relevance:** answer the actual question rather than a related question.
4. **Clarity and audience fit:** use language appropriate for the intended reader.
5. **Completeness and fidelity:** include necessary details without adding unsupported information or changing source meaning.
6. **Safety:** do not prefer advice that creates avoidable harm. A serious safety failure can override stylistic strengths.
7. **Calibrated uncertainty:** when information is insufficient, acknowledge limits instead of inventing certainty.
8. **Conciseness:** longer is not automatically better. Prefer the shortest answer that adequately satisfies the prompt.

## Recommended workflow
1. Read the prompt and identify explicit constraints.
2. Read Response A and Response B independently.
3. Check important factual or mathematical claims.
4. Compare each response against the same criteria.
5. Choose A or B. If truly equivalent, use a tie/equivalent label if your platform supports it; otherwise explain that the preference is weak.
6. Write a short justification naming the decisive difference.
7. Mark any critical safety or factual failure.

## Suggested rating scale for confidence
- **High:** one response clearly wins on correctness, safety, or a direct instruction.
- **Medium:** a meaningful difference exists, but some judgment is involved.
- **Low:** responses are close or the preferred choice depends on context.

## What a good justification looks like
Weak: "B is better because it is good."
Strong: "B follows the exact-output instruction; A adds an explanation even though the prompt requested only 'Yes' or 'No'."

## Common mistakes to avoid
- Choosing the longer or more polished response by default.
- Rewarding confident wording without verifying claims.
- Ignoring exact formatting requirements.
- Treating every difference as equally important.
- Giving a preference without explaining the reason.
- Overstating certainty on ambiguous pairs.

## Dataset note
The included examples are synthetic training exercises. The reference preferences are illustrative judgments, not a claim that every pair has one universally correct answer. Review them independently and document reasonable disagreements.
