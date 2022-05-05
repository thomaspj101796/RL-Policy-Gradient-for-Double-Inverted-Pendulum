# RL-Policy-Gradient-for-Double-Inverted-Pendulum

Author: Patrick Thomas

Implementation of a Policy Gradient to train a vanilla neural network to complete the task of holding a double inverted pendulum upright.

Code writtem based on: https://towardsdatascience.com/understanding-actor-critic-methods-931b97b6df3f

## Known Dependencies
- Python 3.6
- Pytorch 11.1
- gym 0.23
- mujoco_py 2.12

## How to run:

### Clone Repository
```bash
git clone https://github.com/thomaspj101796/RL-Policy-Gradient-for-Double-Inverted-Pendulum.git
cd RL-Policy-Gradient-for-Double-Inverted-Pendulum
pip install .
```

### Install MuJoCo dependency:
- Install MuJoCo (only works on Linux or Mac) from https://github.com/deepmind/mujoco/releases
- Install and build mujoco_py using the script available here: https://gist.github.com/BuildingAtom/3119ac9c595324c8001a7454f23bf8c8

### Running program:
- Run Jupyter notebook to create, train, and evaluate performance of net. Tunable hyperparameters are before the training function call in the last Jupyter block.