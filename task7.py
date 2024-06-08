import random

def monte_carlo_simulation(num_trials):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums_count[total] += 1

    probabilities = {sum_: count / num_trials * 100 for sum_, count in sums_count.items()}

    return probabilities

def display_results(probabilities):
    print("Сума\tЙмовірність")
    for sum_, probability in probabilities.items():
        print(f"{sum_}\t{probability:.2f}%")

num_trials = 1000000

probabilities = monte_carlo_simulation(num_trials)

display_results(probabilities)
