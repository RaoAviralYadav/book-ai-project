# I created this file just to test the reward_engie.py module in isolation.

from rl.reward_engine import compute_reward

original = "The boy go to school every day. He are smart."
edited = "The boy goes to school every day. He is smart."

reward = compute_reward(original, edited)
print(f"Reward Score: {reward}")
