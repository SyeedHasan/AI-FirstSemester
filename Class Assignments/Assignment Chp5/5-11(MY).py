
a = [1,2,3,4,5,6,6]

def F(inputArray):
	return max([inputArray[i]*inputArray[i+1] for i in range(0, int(len(inputArray)-1))])

print(F(a))