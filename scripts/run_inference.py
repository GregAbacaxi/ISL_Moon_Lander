from stable_baselines3 import PPO
import gymnasium as gym
import os
import sys

MODEL_BASE = "ppo_lunarlander"
MODEL_FILE = MODEL_BASE + ".zip"

if os.path.exists(MODEL_FILE):
    model = PPO.load(MODEL_BASE)
else:
    print(f"Model file not found: {MODEL_FILE}")
    sys.exit(2)

env = gym.make("LunarLander-v3")
model.set_env(env)

N_EPISODES = 5

for ep in range(1, N_EPISODES + 1):
    obs, info = env.reset()
    total_reward = 0.0
    while True:
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        if terminated or truncated:
            print(f"Episode {ep}: reward={total_reward}")
            break

env.close()
