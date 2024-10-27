# Function to determine the number of problems solved
def count_problems_solved(P):
    for x in range(11):  # x is the number of 100-point problems, max 10 problems
        y = P - 100 * x  # y is the rest of the score
        if 0 <= y <= 10 and x + y <= 10:
            return x + y  # valid solution, return total problems solved
    return -1  # no valid solution

# Read number of test cases
t = int(input())
results = []

# Process each test case
for i in range(t):
    p = int(input())
    results.append(count_problems_solved(p))

# Print results for all test cases
print("\n".join(map(str, results)))
