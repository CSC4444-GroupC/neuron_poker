"""PPO RL agent"""

import numpy as np
from gym_env.enums import Action
from icecream import ic
from stable_baselines3 import PPO


class Player:
    """Mandatory class with the player methods"""

    def __init__(self, model: PPO, name="PPO_RL"):
        """Initiaization of an agent"""
        self.equity_alive = 0
        self.actions = []
        self.last_action_in_stage = ""
        self.temp_stack = []
        self.name = name
        self.autoplay = True
        self.model = model

    def action(self, action_space, observation, info):
        """Mandatory method that calculates the move based on the observation array and the action space."""
        _ = info  # not using info for decision
        action_mask = info["action_mask"]
        observation = np.nan_to_num(observation, nan=0.0, posinf=0.0, neginf=0.0)
        action, _ = self.model.predict(observation)
        return action
