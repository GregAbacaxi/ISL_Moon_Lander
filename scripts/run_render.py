#!/usr/bin/env python3
import argparse
import os
import sys
import time

import gymnasium as gym
from stable_baselines3 import PPO

parser = argparse.ArgumentParser(description="Run trained PPO on LunarLander with human rendering")
parser.add_argument("--model", default="ppo_lunarlander", help="Base name of the model file (without .zip)")
parser.add_argument("--episodes", type=int, default=10, help="Number of episodes to run")
args = parser.parse_args()

MODEL_FILE = args.model + ".zip"
if not os.path.exists(MODEL_FILE):
    print(f"Model file not found: {MODEL_FILE}")
    sys.exit(2)

try:
    model = PPO.load(args.model)
except Exception as e:
    print("Error loading model:", e)
    raise

# Create environment with human rendering
try:
    env = gym.make("LunarLander-v3", render_mode="human")
except Exception as e:
    print("Error creating env with render_mode='human':", e)
    raise

model.set_env(env)

for ep in range(1, args.episodes + 1):
    obs, info = env.reset()
    total_reward = 0.0
    done = False
    while True:
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        if terminated or truncated:
            print(f"Episode {ep}: reward={total_reward}")
            # small pause between episodes so rendering is visible
            time.sleep(1.0)
            break

env.close()
