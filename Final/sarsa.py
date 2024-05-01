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
        if random.random() < epsilon:  # Explore: choose a random available spot
            available_spots = [i for i in range(self.num_spots) if self.spots[i] is None]
            return random.choice(available_spots) if available_spots else None
        else:  # Exploit: choose the best available spot according to Q-values
            q_values = np.where(self.spots == None, self.q_table, -np.inf)  # Mask occupied spots
            return np.argmax(q_values) if np.any(q_values > -np.inf) else None

    def update_q_value(self, state, action, reward, next_state, next_action, alpha=0.5, gamma=0.9):
        """Update the Q-value for the state-action pair using the SARSA update rule."""
        current_q = self.q_table[action]
        next_q = self.q_table[next_action] if next_action is not None else 0
        self.q_table[action] = current_q + alpha * (reward + gamma * next_q - current_q)

def simulate_sarsa(episodes=100, alpha=0.5, gamma=0.9, epsilon=0.1):
    lot = SARSA_ParkingLot(10)
    for e in range(episodes):
        state = lot.get_parking_status()  # Get current state
        action = lot.choose_action(epsilon)
        if action is not None:
            car = Car(e)  # Create a car with a new ID each episode
            lot.park_car(car, action)
            next_state = lot.get_parking_status()
            reward = -car.parking_time  # Simple reward: negative of parking time
            next_action = lot.choose_action(epsilon)
            lot.update_q_value(state, action, reward, next_state, next_action, alpha, gamma)
            lot.update_time(car.parking_time)  # Simulate time passing
        print()
        print(lot)
        print(f"Episode {e+1}: Q-Table {lot.q_table}")

simulate_sarsa()
