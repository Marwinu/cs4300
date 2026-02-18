import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

def calculate_mean(arr):
    return np.mean(arr)

def calculate_max(arr):
    return np.max(arr)

def calculate_sum(arr):
    return np.sum(arr)


if __name__ == "__main__":
    print(f"Array: {numbers}")
    print(f"Mean: {calculate_mean(numbers)}")
    print(f"Max: {calculate_max(numbers)}")
    print(f"Sum: {calculate_sum(numbers)}")