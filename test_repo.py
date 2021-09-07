import numpy as np

# This file is only for to check whether the linking to MALA worked.

target_array = [1,2,3,4]
target_array = np.array(target_array)
saved_array = np.load("linking_tester.npy")
if not np.isclose(target_array, saved_array, atol=1e-20).all():
    raise Exception("Something is wrong with the repo.")
