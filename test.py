import mujoco_py
import gym
import time
env = gym.make('InvertedDoublePendulum-v2').unwrapped
#env = gym.make('CartPole-v0').unwrapped
env.reset()
# #import
# import pyvirtualdisplay
# _display = pyvirtualdisplay.Display(visible=0,  # remember to use visible=0 and not False
#                                     size=(1400, 900))
# _ = _display.start()
# import matplotlib.pyplot as plt
# from IPython import display
#%matplotlib inline

# env = gym.make('CartPole-v0')
# env.reset()

for i in range(25):
   #plt.imshow(env.render(mode='rgb_array'))
   env.render()
   time.sleep(0.5)
#    display.display(plt.gcf())    
#    display.clear_output(wait=True)
   print(env.step(env.action_space.sample())) # take a random action

env.close()