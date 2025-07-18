

from textstat import flesch_reading_ease

def compute_reward(original, edited):
    orig_score = flesch_reading_ease(original)
    edit_score = flesch_reading_ease(edited)
    reward = max(0, edit_score - orig_score)
    return reward