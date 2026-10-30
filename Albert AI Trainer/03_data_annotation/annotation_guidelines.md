# Sentiment Annotation Guidelines

## Labels
- Positive: the text expresses satisfaction, praise, or a favorable opinion.
- Negative: the text expresses dissatisfaction, criticism, or an unfavorable opinion.
- Neutral: the text mainly states facts and does not clearly express a favorable or unfavorable opinion.
- Mixed: the text contains meaningful positive and negative sentiment.

## Rules
1. Label the sentiment expressed in the text, not what you assume the writer feels.
2. Do not treat every factual statement as positive or negative.
3. Use Mixed when both positive and negative opinions are present and neither can be ignored.
4. If a sentence is ambiguous, flag it for review rather than inventing context.
5. Apply the same rules consistently across the dataset.

## Quality checks
- Review a sample of labels after annotation.
- Check for class imbalance and repeated templates.
- Keep the text and label together so each decision can be audited.
- The included dataset is synthetic and contains repeated sentence patterns for practice; it is not a representative real-world corpus.
