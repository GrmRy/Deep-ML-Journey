def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if not matrix or not matrix[0]:
		return []
	if mode == 'row':
		return [sum(row) / len(row) for row in matrix]
	columns = list(zip(*matrix))
	means=[sum(col) / len(col) for col in columns]
	return means
