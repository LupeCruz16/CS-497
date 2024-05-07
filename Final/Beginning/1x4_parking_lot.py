import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Parameters
num_spots = 4  # Number of parking spots in the lot (1x4 grid)
epsilon = 0.1  # Exploration rate
alpha = 0.5  # Learning rate
gamma = 0.9  # Discount factor
episodes = 50  # Reduced number of episodes for simplicity

# Q-values table, initialized randomly for demonstration
Q = np.random.rand(num_spots)  

# Parking lot state, 0 for empty, 1 for occupied, -1 for entrance
parking_lot = np.zeros(num_spots)
parking_lot[0] = -1  # First spot is always the entrance

# Estimated parking times for cars (e.g., in hours)
estimated_times = [2, 4]  # Two cars with their respective estimated parking times

def choose_action():
    """Choose the best available parking spot based on the lowest Q-value, excluding the entrance."""
    available_spots = np.where((parking_lot == 0))[0]  # Exclude the entrance from available spots
    if available_spots.size > 0:
        return available_spots[np.argmin(Q[available_spots])]
    return None

def update_environment(action, time_estimate):
    """Update parking spot to occupied and modify Q-value based on estimated time."""
    if action is not None:
        parking_lot[action] = 1  # Mark the spot as occupied
        # Reward inversely proportional to the estimated time (simulate cost for longer stays)
        Q[action] += -time_estimate  
        return Q[action]
    return 0

def simulate_and_visualize():
    """Simulate parking of two cars and visualize the lot state."""
    plt.figure(figsize=(12, 3))
    car_count = 0

    for car_time in estimated_times:
        action = choose_action()
        if action is not None:
            reward = update_environment(action, car_time)
            print(f"Car {car_count + 1} parks at spot {chr(64 + action)} with estimated time {car_time} hours, Reward: {reward:.2f}")
            car_count += 1
        else:
            print("No available spots!")

        # Display parking lot state
        plt.subplot(1, 3, car_count if car_count > 0 else 1)
        lot_display = np.array(['Entrance', 'A', 'B', 'C'])
        color_mapping = ['grey' if x == -1 else 'black' if x == 1 else 'white' for x in parking_lot]
        plt.imshow(parking_lot.reshape(1, 4), cmap=mcolors.ListedColormap(color_mapping), aspect='auto')
        plt.title(f'Parking Lot State after Car {car_count}')
        plt.xticks(ticks=np.arange(4), labels=lot_display)
        plt.yticks([])

    plt.show()

print("The first spot is designated as the entrance and is not available for parking.")
simulate_and_visualize()