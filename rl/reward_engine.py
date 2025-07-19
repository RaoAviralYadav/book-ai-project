

import language_tool_python
from textstat import flesch_reading_ease, sentence_count

# Initialize grammar tool
tool = language_tool_python.LanguageTool('en-US')

def grammar_score(text):
    """Score grammar: fewer errors yields higher score (0-100)."""
    matches = tool.check(text)
    num_errors = len(matches)
    num_sentences = max(sentence_count(text), 1)
    score = 100 - (num_errors / num_sentences) * 10
    return max(0, min(score, 100))


def readability_score(text):
    """Normalize Flesch reading ease to 0-100."""
    score = flesch_reading_ease(text)
    return max(0, min(score, 100))


def improvement_score(original, edited):
    """Reward positive delta in readability."""
    delta = flesch_reading_ease(edited) - flesch_reading_ease(original)
    return max(0, delta)


def compute_reward(original, edited):
    """Combine grammar, readability, and improvement into a final reward."""
    g_score = grammar_score(edited)
    r_score = readability_score(edited)
    i_score = improvement_score(original, edited)

    # Weighted average
    total = (0.4 * g_score) + (0.4 * r_score) + (0.2 * i_score)
    return round(max(0, min(total, 100)), 2)

