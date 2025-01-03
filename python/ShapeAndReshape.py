import numpy as np
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
rows = 3
columns = 4
def reshape_array_pad(data, rows, columns):
    total_elements = rows * columns
    if data.size < total_elements:
        padded_data = np.pad(data, (0, total_elements - data.size), 'constant')
        print(f"Data padded with {total_elements - data.size} zeros.")
        return padded_data.reshape(rows, columns)
    else:
        return data[:total_elements].reshape(rows, columns)
reshaped_array = reshape_array_pad(data, rows, columns)
print("Reshaped 2D array:")
print(reshaped_array)
