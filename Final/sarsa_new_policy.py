# Import necessary libraries
from parking_lot import ParkingLot
import matplotlib.pyplot as plt
from car import Car
import numpy as np
import random

# Define SARSA_ParkingLot class, inheriting from ParkingLot
class SARSA_ParkingLot(ParkingLot):
    def __init__(self, num_spots=10):
        super().__init__(num_spots)  # Initialize superclass
        self.q_table = np.zeros(num_spots)  # Initialize Q-values for each spot

    def softmax_probabilities(self, q_values):
        """Compute softmax probabilities from Q-values. This method was added to support the new softmax policy."""
        exp_q = np.exp(q_values - np.max(q_values))  # Stabilize exp by subtracting max Q-value
        return exp_q / np.sum(exp_q)

    def choose_action(self, epsilon=0.1):
        """
        Choose an action using a softmax policy based on Q-values, replacing the original epsilon-greedy method.
        This method now uses softmax_probabilities to determine the action probabilities.
        """
        available_spots = [i for i in range(self.num_spots) if self.spots[i] is None]
        if available_spots:
            q_values = self.q_table[available_spots]
            probabilities = self.softmax_probabilities(q_values)
            return np.random.choice(available_spots, p=probabilities)
        return None

    def update_q_value(self, state, action, reward, next_state, next_action, alpha=0.5, gamma=0.9):
        """Update the Q-value for the state-action pair using the SARSA update rule."""
        if action is not None:
            current_q = self.q_table[action]
            next_q = self.q_table[next_action] if next_action is not None else 0
            self.q_table[action] = current_q + alpha * (reward + gamma * next_q - current_q)

# Simulation function for running SARSA algorithm
def simulate_sarsa(episodes=100, alpha=0.5, gamma=0.9):
    lot = SARSA_ParkingLot(10)  # Initialize parking lot
    q_values_over_time = np.zeros((episodes, 10))  # Store Q-values over time

    for e in range(episodes):
        print(f"\nEpisode {e+1}")
        if random.random() < 0.75:
            car = Car(e)  # Create a car instance
            action = lot.choose_action()  # Choose an action using the new softmax policy
            if action is not None:
                reward = 10 - car.parking_time  # Compute reward
                lot.park_car(car, action)  # Park the car
                next_action = lot.choose_action()  # Choose the next action using the softmax policy
                lot.update_q_value(None, action, reward, None, next_action, alpha, gamma)  # Update Q-value
            else:
                print("No available action found.")
        else:
            print("No car arrived this step.")
        lot.update_time(1)  # Update time
        q_values_over_time[e, :] = lot.q_table  # Record Q-values

        print()
        print(lot)
        print(f"Q-Table: {lot.q_table}")

    # Plotting the Q-values after all episodes
    plt.figure(figsize=(12, 8))
    for i in range(10):
        plt.plot(q_values_over_time[:, i], label=f'Spot {i}')
    plt.title('Q-values Over Episodes')
    plt.xlabel('Episode')
    plt.ylabel('Q-value')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig('Q_values_over_episodes.png')  # Save the plot as a PNG file
    plt.close()  # Close the plot to free up memory

simulate_sarsa()  # Start the simulation
