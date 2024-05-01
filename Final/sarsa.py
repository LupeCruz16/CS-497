from parking_lot import ParkingLot
import matplotlib.pyplot as plt
from car import Car
import numpy as np
import random

class SARSA_ParkingLot(ParkingLot):
    def __init__(self, num_spots=10):
        super().__init__(num_spots)
        self.q_table = np.zeros(num_spots)  # Initialize Q-values for each spot

    def choose_action(self, epsilon=0.9):
        """Choose an action using an epsilon-greedy policy based on Q-values."""
        available_spots = [i for i in range(self.num_spots) if self.spots[i] is None]
        if random.random() < epsilon:  # Explore: choose a random available spot
            return random.choice(available_spots) if available_spots else None
        else:  # Exploit: choose the best available spot according to Q-values
            if available_spots:
                return max(available_spots, key=lambda x: self.q_table[x])
            return None

    def update_q_value(self, state, action, reward, next_state, next_action, alpha=0.5, gamma=0.9):
        """Update the Q-value for the state-action pair using the SARSA update rule."""
        if action is not None:
            current_q = self.q_table[action]
            next_q = self.q_table[next_action] if next_action is not None else 0
            self.q_table[action] = current_q + alpha * (reward + gamma * next_q - current_q)

def simulate_sarsa(episodes=100, alpha=0.5, gamma=0.9, epsilon_decay=0.99):
    lot = SARSA_ParkingLot(10)
    q_values_over_time = np.zeros((episodes, 10))
    epsilon = 0.9  # Start with higher epsilon for more initial exploration

    for e in range(episodes):
        print(f"\nEpisode {e+1}")
        epsilon *= epsilon_decay  # Decrease epsilon over time for less exploration
        if random.random() < 0.75:
            car = Car(e)
            action = lot.choose_action(epsilon)
            if action is not None:
                reward = 10 - car.parking_time  # Change reward structure
                lot.park_car(car, action)
                next_action = lot.choose_action(epsilon)
                lot.update_q_value(None, action, reward, None, next_action, alpha, gamma)
            else:
                print("No available action found.")
        else:
            print("No car arrived this step.")
        lot.update_time(1)
        q_values_over_time[e, :] = lot.q_table
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

simulate_sarsa()
