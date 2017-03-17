import numpy as np
import matplotlib.pyplot as plt

# eventually add functionality to pass function for criteria. Currenlty assume looking for circle
# monte_carlo() creates a random distribution of points within the predefined interval around 0
# inputs are: monte_carlo(int[], nominal[], trials[])
# all inputs must be integers
def monte_carlo(interval, nominal, trials):
    current_trial = 0
    dimensions = np.size(interval)
    points = np.zeros([dimensions, trials])
    while current_trial < trials:
        offset = np.zeros([dimensions])
        for i in range(0,dimensions):
            offset[i] = (np.random.random() * interval[i]) - 0.5*(interval[i])
            points[i, current_trial] = nominal[i] + offset[i]
        current_trial = current_trial + 1
    return points


def test_trial(points, criteria):
    passing_points = []
    failed_points = []
    shape = points.shape
    points = points - 1
    num = shape[1]
    for i in range(0,num):
        r = np.sqrt(points[0,i]**2 + points[1,i]**2)
        if r <= criteria:
            passing_points.append([points[0,i],points[1,i]])
        else:
            failed_points.append([points[0,i],points[1,i]])
    return passing_points, failed_points


trials = input('Enter the number of trials to run: ')

# *** Debugging ***
# define trial
interval = np.array([2,2])
nominal = np.array([1,1])

# run simulation
values = monte_carlo(interval,nominal,trials)

passed, failed = test_trial(values, 1)
passed = np.array(passed)
failed = np.array(failed)

pi_estimation = float(passed.shape[0])/(failed.shape[0]+passed.shape[0])*4.
print('pi_estimation:'),
print(pi_estimation)

plt.scatter(passed[:,0], passed[:,1], c='r')
plt.scatter(failed[:,0], failed[:,1], c='b')
plt.axis('equal')

plt.show()
