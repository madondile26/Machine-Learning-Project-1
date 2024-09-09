# Iris Dataset Feature Pair Plotting

## Overview

This project visualizes the relationships between the various features of the Iris dataset by creating scatter plots for all possible pairs of features. The Iris dataset is a famous dataset used in pattern recognition and machine learning, containing 150 samples from three species of iris flowers: setosa, versicolor, and virginica.

## Features
The Iris dataset consists of the following four features:
1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

Each sample in the dataset is labeled as one of three species of iris flowers:
- **Setosa**
- **Versicolor**
- **Virginica**

## Functionality
The script performs the following tasks:
- **Loads the Dataset**: Utilizes `scikit-learn` to load the Iris dataset.
- **Color Coding**: Assigns a unique color to each species for easy differentiation.
- **Scatter Plot Matrix**: Generates a 4x3 grid of scatter plots, where each plot shows the relationship between two features. Each plot visualizes the data points belonging to the three species using different colors.

## Requirements
- Python 3.x
- `matplotlib` for plotting
- `scikit-learn` for loading the dataset
- `numpy` for numerical operations

You can install the required packages using pip:
```bash
pip install matplotlib scikit-learn numpy
