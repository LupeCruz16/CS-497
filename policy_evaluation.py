import numpy as np

# Constants for the gridworld
gamma = 1  # discount factor as 1
reward = -1  # reward for all transitions
threshold = 0.01  # convergence threshold
actions = ["up", "down", "left", "right"]

# Initialize value function to zero for all states
value_function = np.zeros((4, 4))

# Function to get the next state and reward
def next_state_reward(state, action):
    i, j = state
    if action == "up":
        return (max(i - 1, 0), j), reward
    elif action == "down":
        return (min(i + 1, 3), j), reward
    elif action == "left":
        return (i, max(j - 1, 0)), reward
    elif action == "right":
        return (i, min(j + 1, 3)), reward

# Value iteration algorithm
def value_iteration(v_function, gamma, threshold):
    iteration = 0
    while True:
        delta = 0
        new_v_function = v_function.copy()  # Create a copy of the value function
        for i in range(4):
            for j in range(4):
                # Skip the terminal states
                if (i == 0 and j == 0) or (i == 3 and j == 3):
                    continue
                old_value = v_function[i, j]
                new_values = []
                for action in actions:
                    (next_i, next_j), _ = next_state_reward((i, j), action)
                    new_values.append(reward + gamma * v_function[next_i, next_j])
                new_v_function[i, j] = max(new_values)
                delta = max(delta, abs(old_value - new_v_function[i, j]))
        print(f"\n\nIteration {iteration}:")
        print("Value Function:")
        print(new_v_function)
        if delta < threshold:
            # Once converged, find the optimal policy
            optimal_policy = calculate_optimal_policy(new_v_function)
            print(f"\n\nIteration {iteration}:\nValue function converged.")
            print(new_v_function)
            print("\nOptimal Policy: ")
            print(optimal_policy)
            break
        v_function = new_v_function  # Update the value function
        iteration += 1
    return new_v_function

# Function to calculate the optimal policy for each state based on the value function
def calculate_optimal_policy(v_function):
    policy = np.empty_like(v_function, dtype=object)
    for i in range(4):
        for j in range(4):
            # Skip the terminal states
            if (i == 0 and j == 0) or (i == 3 and j == 3):
                policy[i, j] = "None".ljust(12)
                continue
            best_actions = []
            best_action_value = float('-inf')
            # Find the best action(s) for the current state
            for action in actions:
                (next_i, next_j), _ = next_state_reward((i, j), action)
                action_value = v_function[next_i, next_j]
                if action_value == best_action_value:
                    best_actions.append(action)
                elif action_value > best_action_value:
                    best_action_value = action_value
                    best_actions = [action]
            # Format the best actions
            if len(best_actions) == len(actions):
                policy[i, j] = "all".ljust(12)
            else:
                best_actions_str = ', '.join(best_actions)
                policy[i, j] = best_actions_str.ljust(12)
    return policy

# Run value iteration
value_function = value_iteration(value_function, gamma, threshold)
