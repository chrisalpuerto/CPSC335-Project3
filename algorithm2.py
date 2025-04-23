# Name: Jonathan Quiroz
# Email: jquiroz44@csu.fullerton.edu
# Project 3 - Algorithm 2: Wine Aged to Perfection

# This program finds the maximum value appreciation for wine aged over several days.
# It takes a list of daily values and computes the best possible profit from bottling
# on one day and selling on a later day.

def max_value_appreciation(values):
    if not values:
        return 0

    min_value = values[0]
    max_profit = 0

    for value in values[1:]:
        profit = value - min_value
        if profit > max_profit:
            max_profit = profit
        if value < min_value:
            min_value = value

    return max_profit

# Example usage:
if __name__ == "__main__":
    # Sample input
    values = [7, 1, 5, 3, 6, 4]
    print("Maximum Appreciation:", max_value_appreciation(values)) 