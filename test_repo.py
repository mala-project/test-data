import numpy as np

target_array = [1,2,3,4]
target_array = np.array(target_array)
saved_array = np.load("linking_tester.npy")
if np.abs(np.sum(target_array-saved_array)) > 0.0000000000001:
    raise Exception("Something is wrong with the repo.")
