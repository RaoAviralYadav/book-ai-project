

from textstat import flesch_reading_ease

def review_text(original, spun):
    original_score = flesch_reading_ease(original)
    spun_score = flesch_reading_ease(spun)
    improvement = spun_score - original_score
    feedback = (
        "✅ Clearer and easier to read!" if improvement > 0 else "⚠️ Consider making the text more concise or clearer."
    )
    return {
        'original_score': original_score,
        'spun_score': spun_score,
        'improvement': improvement,
        'feedback': feedback
    }
