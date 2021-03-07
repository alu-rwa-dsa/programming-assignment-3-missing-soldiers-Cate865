'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

# Number of barriers
total_stoppers = int(input())

# hold the barriers points
stoppers = []

for i in range(total_stoppers):  # get the points
    x, y, d = map(int, input().strip().split())
    stoppers.append((x, x + d))

stoppers.sort()

# initialize blocked ants counter
ants_blocked = block_point = 0

for stopper in stoppers:  # gets the number of ants at each block point
    if stopper[0] >= block_point:
        block_point = stopper[0]
        if block_point < stopper[1]:
            ants_blocked += (stopper[1] - block_point) + 1
            block_point = stopper[1] + 1
    elif block_point <= stopper[1]:
        ants_blocked += (stopper[1] - block_point) + 1
        block_point = stopper[1] + 1

print(ants_blocked)
