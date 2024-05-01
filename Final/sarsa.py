from parking_lot import ParkingLot
from car import Car
import numpy as np
import random

class SARSA_ParkingLot(ParkingLot):
    def __init__(self, num_spots=10):
        super().__init__(num_spots)
        self.q_table = np.zeros(num_spots)  # Initialize Q-values for each spot

    def choose_action(self, epsilon=0.1):
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

def simulate_sarsa(episodes=100, alpha=0.5, gamma=0.9, epsilon=0.1, arrival_probability=0.75):
    lot = SARSA_ParkingLot(10)
    for e in range(episodes):
        print(f"\nEpisode {e+1}")
        if random.random() < arrival_probability:  # Car arrives with a certain probability
            car = Car(e)  # Create a new car for each potential parking event
            action = lot.choose_action(epsilon)
            if action is not None:
                lot.park_car(car, action)
                reward = -car.parking_time  # Define reward: negative of parking time
                next_action = lot.choose_action(epsilon)
                next_state = lot.get_parking_status()
                lot.update_q_value(None, action, reward, None, next_action, alpha, gamma)
            else:
                print("No available action was found.")
        else:
            print("No car arrived this step.")
        lot.update_time(1)  # Simulate time passing
        print()
        print(lot)
        print(f"Q-Table: {lot.q_table}")

simulate_sarsa()
