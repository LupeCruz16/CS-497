import random
import matplotlib.pyplot as plt

'''
To view generated graph install library as command:

pip install matplotlib

'''

Green = [4.77317728, 5.99791051, 5.76776377, 4.47913849, 6.21411927,
6.84915318, 8.44082357, 6.15266159, 6.97135381, 7.43452167]

Blue = [6.00449072, 3.34005839, 6.71096916, 4.11113061, 5.68416528,
3.88539945, 3.51181469, 3.67426432, 4.98069804, 4.41366311]

Red = [6.36086896, 5.65584783, 7.62912922, 13.29826146, 5.99876216,
8.14484021, 9.74488991, 6.616229, 14.26793535, 0.98932393]

# Initial values 
QG = [0]
QB = [0]
QR = [0]

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
    Q_values = [QG[-1], QB[-1], QR[-1]]
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
for _ in range(100):  # Loop 100 times
    action = choose_action(QG, QB, QR, EPSILON)
    reward = get_reward(action)
    
    # Update Q values based on the average
    if action == 0:
        QG.append((QG[-1] * N_counts[0] + reward) / (N_counts[0] + 1))
        N_counts[0] += 1
    elif action == 1:
        QB.append((QB[-1] * N_counts[1] + reward) / (N_counts[1] + 1))
        N_counts[1] += 1
    else:
        QR.append((QR[-1] * N_counts[2] + reward) / (N_counts[2] + 1))
        N_counts[2] += 1

# Print the final counts
print(f"Final Counts: Green selected {N_counts[0]} times, Blue selected {N_counts[1]} times, Red selected {N_counts[2]} times")

# Generate the plot
plt.figure(figsize=(12, 6))
plt.plot(range(len(QG)), QG, label='Green')
plt.plot(range(len(QB)), QB, label='Blue')
plt.plot(range(len(QR)), QR, label='Red')

plt.xlabel('Number of times the choice has been taken')
plt.ylabel('Average Q Value')
plt.title('Average Q Value vs. Number of Actions Taken')
plt.legend()
plt.xlim([0, 100])

plt.savefig('reward_plot.png')
plt.show()