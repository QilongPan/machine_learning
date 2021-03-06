
# -*- coding: utf-8 -*-
# @Date    : 2019-08-01 14:41:44
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
import gym
import time
env = gym.make('CartPole-v0')
for i_episode in range(200):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
time.sleep(5)
env.close()