def knapsack_dp(values, weights, capacity):
    n = len(values)  # Number of items available
    
    # Create a 2D array to store the maximum value for each subproblem
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the dp array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Include the item and check if it's more beneficial
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])# i-1 means current item
            else:
                # Exclude the item
                dp[i][w] = dp[i - 1][w]
    
    # The maximum value for the entire capacity will be stored in dp[n][capacity]
    return dp[n][capacity]

# Get user input
if __name__ == "__main__":# script run directecly

    num_items = int(input("Enter the number of items: "))
    
    values = []
    weights = []
    
    for i in range(num_items):
        value = int(input(f"Enter the value for item {i + 1}: "))
        weight = int(input(f"Enter the weight for item {i + 1}: "))
        values.append(value)
        weights.append(weight)
    
    capacity = int(input("Enter the knapsack capacity: "))
    
    max_value = knapsack_dp(values, weights, capacity)
    print(f"Maximum value in the knapsack: {max_value}")
