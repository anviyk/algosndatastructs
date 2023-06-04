from time import sleep
print ("-----Welcome to the Fibonacci series game-----")
sleep(2)
length = 0
while length < 1:
	length = int(input("Enter how long you want the fibonacci series to go on for (greater than or equal to 1): "))

n = length + 1
while n > length and n > 0:
	n = int(input("Enter a position in the list: "))
n = n - 1

m = n + 1
while m > n and m > 0:
	m = int(input("Enter a position in the list less than " + str(n) + ": "))
m = m - 1

fibonacci = [0] * length
fibonacci
fibonacci[1] = 1

if length > 1:
	for l in range(2,length):
		fibonacci[l] = fibonacci[l-2] + fibonacci[l-1]

print(fibonacci)

num_diff = fibonacci[n] - fibonacci[m]
 
print(f"The difference between the Fibonnaci numbers {fibonacci[n]} and {fibonacci[m]} is: {num_diff}")
