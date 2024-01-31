#Possible rewards for each selection
import random

Green = [4.77317728, 5.99791051, 5.76776377, 4.47913849, 6.21411927,
6.84915318, 8.44082357, 6.15266159, 6.97135381, 7.43452167]

Blue = [6.00449072, 3.34005839, 6.71096916, 4.11113061, 5.68416528,
3.88539945, 3.51181469, 3.67426432, 4.98069804, 4.41366311]

Red = [6.36086896, 5.65584783, 7.62912922, 13.29826146, 5.99876216,
8.14484021, 9.74488991, 6.616229, 14.26793535, 0.98932393]

# Initial values 
QG = []
QB = []
QR = []

# Number of times a choice has been selected
N_counts = [0, 0, 0]  # NG, NB, NR

#Epsilon 
EPSILON = 0.01

'''
    Steps

    1. Find the greedy action => find the action to take
    2. Generate the random reward
    --> from the list
    -- follow a distribution
    3. Update the Q from the action

    All three steps are functions 
'''

# Choose action function
def choose_action(QG, QB, QR, EPSILON):
    Q_values = [sum(QG)/len(QG) if QG else 0,
                sum(QB)/len(QB) if QB else 0,
                sum(QR)/len(QR) if QR else 0]
    if random.random() < EPSILON:
        # Exploration: choose a random action
        return random.randint(0, 2)
    else:
        # Exploitation: choose the greedy action (max Q value)
        max_value = max(Q_values)
        greedy_actions = [i for i, q in enumerate(Q_values) if q == max_value]
        return random.choice(greedy_actions)

# Reward function
def get_reward(action):
    if action == 0:
        return random.choice(Green)
    elif action == 1:
        return random.choice(Blue)
    else:
        return random.choice(Red)

# Main loop
for _ in range(100):  # Loop 100 times or however many iterations you want
    action = choose_action(QG, QB, QR, EPSILON)
    reward = get_reward(action)
    # Store the reward
    if action == 0:
        QG.append(reward)
    elif action == 1:
        QB.append(reward)
    else:
        QR.append(reward)
    # Increment the count for the chosen action
    N_counts[action] += 1

# Calculate the average of the Q values
average_QG = sum(QG)/len(QG) if QG else 0
average_QB = sum(QB)/len(QB) if QB else 0
average_QR = sum(QR)/len(QR) if QR else 0

# Print the average Q values and the lists
print("Average Q-values:")
print("Green:", average_QG)
print("Blue:", average_QB)
print("Red:", average_QR)
print("\nQ-values arrays:")
print("QG:", QG)
print("QB:", QB)
print("QR:", QR)
print("\nN-counts:", N_counts)