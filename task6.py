def greedy_algorithm(items, budget):
    selected_items = []

    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    for item, details in sorted_items:
        if details['cost'] <= budget:
            selected_items.append(item)
            budget -= details['cost']

    return selected_items


def dynamic_programming(items, budget):
    dp_table = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    for i, (item, details) in enumerate(items.items(), start=1):
        for j in range(1, budget + 1):
            if details['cost'] <= j:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i - 1][j - details['cost']] + details['calories'])
            else:
                dp_table[i][j] = dp_table[i - 1][j]

    selected_items = []
    i, j = len(items), budget
    while i > 0 and j > 0:
        if dp_table[i][j] != dp_table[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]['cost']
        i -= 1

    return selected_items


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_result = greedy_algorithm(items, budget)
print("Greedy Algorithm Result:", greedy_result)

dp_result = dynamic_programming(items, budget)
print("Dynamic Programming Result:", dp_result)
