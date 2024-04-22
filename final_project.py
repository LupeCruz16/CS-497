import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle

# Parameters
num_spots = 10  # Number of parking spots in the lot
num_entrances = 2  # Number of entrances
epsilon = 0.1  # Exploration rate
alpha = 0.5  # Learning rate
gamma = 0.9  # Discount factor
episodes = 1000  # Total number of episodes for training
display_step = 100  # Display the grid every 100 iterations

# Q-values table
Q = np.zeros(num_spots)  # One-dimensional array, one Q-value per spot

# Parking lot state
parking_lot = np.zeros(num_spots)  # 0 for empty, 1 for occupied

# Entrances
entrances = random.sample(range(num_spots), num_entrances)

def choose_action(state, epsilon):
    """Choose an action based on the epsilon-greedy policy."""
    if random.uniform(0, 1) < epsilon:
        # Randomly choose from available spots only
        available_spots = np.where((parking_lot == 0) & (~np.isin(range(num_spots), entrances)))[0]
        return random.choice(available_spots) if available_spots.size > 0 else None
    else:
        # Exploit: choose the best available spot
        available_spots = np.where((parking_lot == 0) & (~np.isin(range(num_spots), entrances)))[0]
        if available_spots.size > 0:
            return available_spots[np.argmin(Q[available_spots])]
        else:
            return None

def update_environment(action):
    """Simulate parking a car."""
    if action is not None:
        parking_lot[action] = 1  # Park the car
        reward = -action  # Closer to the entrance has less negative, hence more desirable
        return reward
    return 0  # No change if no action

def update_q_value(old_state, action, reward, new_state, new_action):
    """Update Q-values using the Sarsa update rule."""
    if action is not None and new_action is not None:
        Q[action] = Q[action] + alpha * (reward + gamma * Q[new_action] - Q[action])

def simulate_and_visualize():
    """Run the simulation and visualize each step."""
    for episode in range(episodes):
        action = choose_action(0, epsilon)
        reward = update_environment(action)
        new_action = choose_action(0, epsilon)
        update_q_value(0, action, reward, 0, new_action)
        
        # Visualize the parking lot state every 100 iterations
        if (episode + 1) % display_step == 0 or episode == episodes - 1:
            # Display desirability heatmap
            normalized_values = 1 / (1 + np.exp(-Q))  # Sigmoid normalization of Q-values
            plt.figure(figsize=(10, 4))
            plt.subplot(1, 2, 1)
            img = plt.imshow(normalized_values.reshape(2, 5), cmap='coolwarm', aspect='equal')
            plt.title('Desirability Heatmap')
            cbar = plt.colorbar(img, orientation='horizontal')
            cbar.set_label('Desirability of Parking Spot')

            # Display occupancy
            plt.subplot(1, 2, 2)
            occupancy_img = plt.imshow(parking_lot.reshape(2, 5), cmap='gray', aspect='equal')
            plt.title('Parking Lot Occupancy')
            plt.colorbar(occupancy_img, orientation='horizontal', ticks=[0, 1], label='Spot Status')

            plt.xticks([])
            plt.yticks([])
            plt.show()

        # Randomly empty spots to simulate cars leaving
        if random.random() < 0.1:  # 10% chance to empty a spot
            empty_indices = np.where(parking_lot == 1)[0]
            if empty_indices.size > 0:
                parking_lot[random.choice(empty_indices)] = 0

simulate_and_visualize()