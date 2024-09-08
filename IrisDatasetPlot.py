import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# Load the Iris dataset
iris = load_iris()
data = np.array(iris.data)
targets = np.array(iris.target)

cd = {0: 'r', 1: 'b', 2: 'g'}
cols = np.array([cd[target] for target in targets])

# Define all possible combinations of 2 features out of 4
feature_combinations = [(0, 1), (0, 2), (0, 3),
                        (1, 0), (1, 2), (1, 3),
                        (2, 0), (2, 1), (2, 3),
                        (3, 0), (3, 1), (3, 2)]

# Create a 4x3 grid of subplots (12 in total)
fig, axes = plt.subplots(4, 3, figsize=(15, 15))

for i, (feat1, feat2) in enumerate(feature_combinations):
    row = i // 3  # Determine the row index
    col = i % 3   # Determine the column index

    ax = axes[row, col]  # Select the current subplot

    for target_name, target_value in zip(iris.target_names, range(3)):
        ax.scatter(data[targets == target_value, feat1], data[targets == target_value, feat2],
                   label=target_name, c=cd[target_value])

    ax.set_xlabel(iris.feature_names[feat1])
    ax.set_ylabel(iris.feature_names[feat2])
    ax.legend()

plt.tight_layout()
plt.show()