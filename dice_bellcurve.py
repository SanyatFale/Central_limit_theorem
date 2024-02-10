import random
import numpy as np
import matplotlib.pyplot as plt

def simulate_dice_rolls(n, m):
    outcomes = []
    for _ in range(m):
        sum_outcome = 0
        for _ in range(n):
            dice_roll = random.randint(1, 6)
            sum_outcome += dice_roll
        outcomes.append(sum_outcome)
    return outcomes

# Number of simulations and dice rolls per simulation
m = 1000000 # Change this to the number of simulations you want to run
n = 10 # Change this to the number of dice rolls per simulation

outcomes = simulate_dice_rolls(n, m)

# Calculate the mean and standard deviation of the outcomes
mean = np.mean(outcomes)
std_dev = np.std(outcomes)

# Plot a histogram of the outcomes
plt.hist(outcomes, bins=range(n, 6 * n + 2), align='left', rwidth=0.8, density=True, alpha=0.5, label='Simulation')

# Generate and plot the bell curve
x = np.linspace(n, 6 * n, 100)
y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-(x - mean) ** 2 / (2 * std_dev ** 2))
plt.plot(x, y, 'r', label='Bell Curve')

plt.xlabel('Sum of Outcomes')
plt.ylabel('Probability Density')
plt.title(f'Distribution of {m} Simulations with {n} Dice Rolls Each')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.show()
