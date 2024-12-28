def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a, b = matrix[0]
	c, d = matrix[1]
	trace = a + d
	det = a * d - b * c
	x = trace * trace - 4 * det
	guess = x / 2
	for _ in range(20):
		if guess == 0:
			break
		guess = (guess + x / guess) / 2
		
	eigenvalue1 = (trace + guess) / 2
	eigenvalue2 = (trace - guess) / 2
	if eigenvalue2 > eigenvalue1:
		eigenvalue1, eigenvalue2 = eigenvalue2, eigenvalue1
		
	return [round(eigenvalue1 * 10) / 10, round(eigenvalue2 * 10) / 10]
