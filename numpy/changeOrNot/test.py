import numpy as np 

# Generate the array to save the random car possition. 
# Size is the number of the testing sample. 
def init_array(size = 100):
	array = np.random.randint(0, 3, size)
	return array

# Random check if we pick a car. 
def random_pick(car_pos):
	pick = np.random.randint(0, 3)

	if pick == car_pos:
		return 1
	else:
		return 0

def change_mind_pick(car_pos):
	pick = np.random.randint(0, 3)
	doors = [0, 1, 2]

	doors.remove(car_pos)
	if pick in doors:
		doors.remove(pick)

	if len(doors) == 2: 
		return 0
	else:
		return 1 

def keep_mind_pick(car_pos):
	pick = np.random.randint(0, 3)
	doors = [0, 1, 2]

	doors.remove(car_pos)
	if pick in doors:
		doors.remove(pick)

	if len(doors) == 2: 
		return 1
	else:
		return 0 

# Test the possibility of keep mind after we remove one wrong option. 
def KeepMindTest(size = 1000):
	test_array = init_array(size = size)
	test_result = []

	for item in test_array:
		result = change_mind_pick(item)
		test_result.append(result)

	result = np.mean(test_result)
	print('Keep mind after remove one door, the possibility of getting a car is: {}.'.format(result))

	return result

# Test the possibility of changing mind after we remove one wrong option. 
def ChangeMindTest(size = 1000):
	test_array = init_array(size = size)
	test_result = []

	for item in test_array:
		result = change_mind_pick(item)
		test_result.append(result)

	result = np.mean(test_result)
	print('Change mind after remove one door, the possibility of getting a car is: {}.'.format(result))

	return result


# Test the possibility of random open a door to get car.  
def SimpleOpenDoorTest(size = 1000):
	test_array = init_array(size = size)
	test_result = []

	for item in test_array:
		result = random_pick(item)
		test_result.append(result)

	result = np.mean(test_result)
	print('Random open a door, the possibility of getting a car is: {}.'.format(result))

	return result

if __name__ == '__main__':
	number_of_test = 1000000

	SimpleOpenDoorTest(size = number_of_test)
	ChangeMindTest(size = number_of_test)
	KeepMindTest(size = number_of_test)