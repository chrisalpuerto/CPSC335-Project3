# Name: Christopher Alpuerto
# Email: chrisalpuerto@csufullerton.edu
# Project 3
# Algorithm 1: Crafting the Infinite-Charm Bracelet

'''
Description: This algorithm is designed to solve the problem of crafting an infinite-charm bracelet
using dynamic programming and unbounded knapsack. The goal is to maximize the total value of charms that can be added to the bracelet
while adhering to a weight limit. The algorithm takes into account the number of charms, their respective weights,
and values, and uses a dynamic programming approach to find the optimal solution.
The algorithm uses a 2D array to store the maximum value that can be achieved for each weight limit
and each charm type. It iterates through the charms and updates the array based on the current weight limit
and the value of the charm. The final result is the maximum value that can be achieved for the given weight limit.


'''

def infiniteCharm(n, weight, w, v):
    dp = [0] * (weight + 1)
    for i in range(n):
        for j in range(w[i], weight + 1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])
    res = dp[weight]
    return f"{res:.1f}"

# Example usage
if __name__ == "__main__":
    print("Let's demonstrate the infinite charm bracelet algorithm.")

    n = 3  # Number of charms
    weight = 10  # Weight limit of the bracelet
    w = [2,3,5]  # Mass of each bead type
    v = [3.0,3.0,7.5]  # Charm value of each bead type

    result = infiniteCharm(n, weight, w, v)
    print("Maximum value that can be achieved:", result)

    print("Let's try another example.")

    weight = 7
    w = [2,3,4]
    v = [3.0,4.0,5.0]

    res = infiniteCharm(n, weight, w, v)
    print("Maximum value that can be achieved:", res)

