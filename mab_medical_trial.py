import random
import matplotlib.pyplot as plt

Green = [4.77317728, 5.99791051, 5.76776377, 4.47913849, 6.21411927,
         6.84915318, 8.44082357, 6.15266159, 6.97135381, 7.43452167]

Blue = [6.00449072, 3.34005839, 6.71096916, 4.11113061, 5.68416528,
        3.88539945, 3.51181469, 3.67426432, 4.98069804, 4.41366311]

Red = [6.36086896, 5.65584783, 7.62912922, 13.29826146, 5.99876216,
       8.14484021, 9.74488991, 6.616229, 14.26793535, 0.98932393]

# Initial Q values for each action
QG = [0]
QB = [0]
QR = [0]

# Number of times an action has been selected
N_counts = [0, 0, 0]

# Epsilon for exploration
EPSILON = 0.1  # Slightly increased for more exploration

# Learning rate (alpha)
ALPHA = 0.1

def choose_action(QG, QB, QR, EPSILON):
    if random.random() < EPSILON:
        return random.randint(0, 2)
    else:
        Q_values = [QG[-1], QB[-1], QR[-1]]
        return Q_values.index(max(Q_values))

def get_reward(action):
    if action == 0:
        return random.choice(Green)
    elif action == 1:
        return random.choice(Blue)
    else:
        return random.choice(Red)

def update_Q(Q, reward, alpha):
    return Q + alpha * (reward - Q)

for _ in range(100):
    action = choose_action(QG, QB, QR, EPSILON)
    reward = get_reward(action)

    if action == 0:
        QG.append(update_Q(QG[-1], reward, ALPHA))
    elif action == 1:
        QB.append(update_Q(QB[-1], reward, ALPHA))
    else:
        QR.append(update_Q(QR[-1], reward, ALPHA))

    N_counts[action] += 1

print(f"Final Counts: Green selected {N_counts[0]} times, Blue selected {N_counts[1]} times, Red selected {N_counts[2]} times")

plt.figure(figsize=(12, 6))
plt.plot(range(len(QG)), QG, label='Green', color='green')
plt.plot(range(len(QB)), QB, label='Blue', color='blue')
plt.plot(range(len(QR)), QR, label='Red', color='red')

plt.xlabel('Number of times the choice has been taken')
plt.ylabel('Q Value')
plt.title('Q Value vs. Number of Actions Taken')
plt.legend()
plt.xlim([0, 100])

plt.show()
