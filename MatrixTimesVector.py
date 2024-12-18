def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	if len(a[0]) != len(b):
		return -1
	c = []
	for row in a:
		dot_product = sum(row[i] * b[i] for i in range(len(b)))
		c.append(dot_product)
	return c
