import numpy as np

print(np.sqrt(17))

print(np.log(np.e))

print(np.mean([20, 13, 20, 30, 40, 23, 40, 1000]))

print(np.median([20, 13, 20, 30, 40, 23, 40, 1000]))

test_list = [20, 13, 20, 30, 40, 23, 40, 1000]

test_array = np.array(test_list)

test_array_family_size = np.array([2, 3, 4])

test_array_persons_raiting = np.array([[5, 2, 3.5], [1, 9, 6.5]])

print('{}\n{}\n{}'.format(test_array, test_array_family_size, test_array_persons_raiting))