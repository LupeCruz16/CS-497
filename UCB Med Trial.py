import random
import math
import matplotlib.pyplot as plt

# Data for different treatments
Green = [4.77317728, 5.99791051, 5.76776377, 4.47913849, 6.21411927,
         6.84915318, 8.44082357, 6.15266159, 6.97135381, 7.43452167]

Blue = [6.00449072, 3.34005839, 6.71096916, 4.11113061, 5.68416528,
        3.88539945, 3.51181469, 3.67426432, 4.98069804, 4.41366311]

Red = [6.36086896, 5.65584783, 7.62912922, 13.29826146, 5.99876216,
       8.14484021, 9.74488991, 6.616229, 14.26793535, 0.98932393]
 
# Initial values
QG = [0]  # Estimated value for Green
QB = [0]  # Estimated value for Blue
QR = [0]  # Estimated value for Red

# Number of times each choice has been selected
N_counts = [0, 0, 0]  # NG, NB, NR

# Confidence level parameter
C = 2

# Lists to track the evolution of estimated values
QG_evolution = [0]
QB_evolution = [0]
QR_evolution = [0]

# Lists to track the evolution of average rewards
average_rewards = []

# Choose action function using Upper Confidence Bound (UCB)
def choose_action_ucb(QG, QB, QR, N_counts, C, t):
    Q_values = [QG[-1], QB[-1], QR[-1]]
    ucb_values = [q + C * math.sqrt(math.log(t) / (n + 1)) for q, n in zip(Q_values, N_counts)]
    return ucb_values.index(max(ucb_values))

# Reward function
def get_reward(action):
    if action == 0:
        return random.choice(Green)
    elif action == 1:
        return random.choice(Blue)
    else:
        return random.choice(Red)

# Main loop
for t in range(1, 101):  # Loop 100 times
    action = choose_action_ucb(QG, QB, QR, N_counts, C, t)
    reward = get_reward(action)

    # Update Q values based on the incremental update rule
    if action == 0:
        N_counts[0] += 1
        QG.append(QG[-1] + (1 / N_counts[0]) * (reward - QG[-1]))
    elif action == 1:
        N_counts[1] += 1
        QB.append(QB[-1] + (1 / N_counts[1]) * (reward - QB[-1]))
    else:
        N_counts[2] += 1
        QR.append(QR[-1] + (1 / N_counts[2]) * (reward - QR[-1]))

    # Track the evolution of estimated values
    QG_evolution.append(QG[-1])
    QB_evolution.append(QB[-1])
    QR_evolution.append(QR[-1])

    # Calculate the average reward at each time step
    average_reward = sum([QG[-1], QB[-1], QR[-1]]) / 3
    average_rewards.append(average_reward)

# Generate the plot for estimated values
plt.figure(figsize=(12, 6))
plt.plot(range(len(QG_evolution)), QG_evolution, label='Green', color='green')
plt.plot(range(len(QB_evolution)), QB_evolution, label='Blue', color='blue')
plt.plot(range(len(QR_evolution)), QR_evolution, label='Red', color='red')

plt.xlabel('Number of iterations')
plt.ylabel('Estimated Value (Average Q Value)')
plt.title('Estimated Value vs. Number of Iterations')
plt.legend()
plt.savefig('estimated_values_plot.png')
plt.show()  # Display the figure

# Generate the plot for average rewards
plt.figure(figsize=(12, 6))
plt.plot(range(len(average_rewards)), average_rewards, label='Average Reward', color='black')

plt.xlabel('Number of iterations')
plt.ylabel('Average Reward')
plt.title('Average Reward vs. Number of Iterations')
plt.legend()
plt.savefig('avg_rewards.png')
plt.show()  # Display the figure
