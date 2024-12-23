def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	if not a or not a[0]:
		return a
	original_rows=len(a)
	original_cols=len(a[0])
	target_rows, target_cols = new_shape
	if original_rows * original_cols != target_rows * target_cols:
		return a
	flat_list = []
	for row in a:
		flat_list.extend(row)
	reshaped_matrix = []
	for i in range(0, len(flat_list), target_cols):
		reshaped_matrix.append(flat_list[i:i + target_cols])
	return reshaped_matrix
