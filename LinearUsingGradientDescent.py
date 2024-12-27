import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
	m = len(y)
	theta = np.zeros(X.shape[1])
	for _ in range(iterations):
		h = X @ theta
		gradients = (1/m) * X.T @ (h - y)
		theta = theta - alpha * gradients
	return np.round(theta, 4)
