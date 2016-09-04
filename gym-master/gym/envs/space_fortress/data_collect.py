import gym
import sys
import numpy as np
import cv2 # remove at one point

env = gym.make('SFS-v0')
# setting the render mode does not actually	work
#env.configure(mode='human_sleep')
env.configure(mode='human', record_path="./test_images")

#env.render()
#observation, reward, done, info = env.step(action)
for i_episode in range(103):
		observation = env.reset()
		for t in range(5100):
				env.render()
				action = env.action_space.sample()
				observation, reward, done, info = env.step(action)			
				if reward:
					print("👍: ", reward)
				if done:
						print("Episode finished after {} timesteps".format(t+1))
						break
env.write_out_stats("test")
env.close()
