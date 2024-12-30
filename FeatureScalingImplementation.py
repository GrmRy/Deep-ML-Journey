import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	rows = len(data)
	cols = len(data[0])
	standardized_data = [[0] * cols for _ in range(rows)]
	normalized_data = [[0] * cols for _ in range(rows)]
	for j in range(cols):
	    col = [data[i][j] for i in range(rows)]
	    mean = sum(col) / rows
	    variance = sum((x - mean) ** 2 for x in col) / rows
	    std = variance ** 0.5
	    min_val = min(col)
	    max_val = max(col)
	    range_val = max_val - min_val
	    for i in range(rows):
	        if std != 0:
	            standardized_data[i][j] = round((data[i][j] - mean) / std, 4)
	        else:
	            standardized_data[i][j] = 0
	        if range_val != 0:
	            normalized_data[i][j] = round((data[i][j] - min_val) / range_val, 4)
	        else:
	            normalized_data[i][j] = 0
	return standardized_data, normalized_data
