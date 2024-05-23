import time

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
            if amount == 0:
                break
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    min_coins = [0] + [float('inf')] * amount
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = last_coin[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin

    return result

def form_result(result, title):
    formatted_output = f"{title}:\n"
    for coin, count in sorted(result.items(), reverse=True):
        formatted_output += f"Номінал {coin} копійок: {count} монет(и)\n"
    return formatted_output

def form_execution_time(function, *args):
    start_time = time.time()
    function(*args)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    return execution_time_ms

small_sum = 217

greedy_result_small = find_coins_greedy(small_sum)
dp_result_small = find_min_coins(small_sum)

print(form_result(greedy_result_small, "#Розрахунок Жадібного Алгоритму для малої суми"))
print(form_result(dp_result_small, "#Розрахунок Динамічного Програмування для малої суми"))

greedy_time_small = form_execution_time(find_coins_greedy, small_sum)
dp_time_small = form_execution_time(find_min_coins, small_sum)

print(f"Час  Жадібного Алгоритму для малої суми: {greedy_time_small:.5f} мс")
print(f"Час виконання Динамічного Програмування для малої суми: {dp_time_small:.5f} мс")

print("*" * 90)

large_sum = 121343

greedy_result_large = find_coins_greedy(large_sum)
dp_result_large = find_min_coins(large_sum)

print(form_result(greedy_result_large, "#Розрахунок Жадібного Алгоритму для великої суми"))
print(form_result(dp_result_large, "#Розрахунок Динамічного Програмування для великої суми"))

greedy_time_large = form_execution_time(find_coins_greedy, large_sum)
dp_time_large = form_execution_time(find_min_coins, large_sum)

print(f"Час Жадібного Алгоритму для визначення великої суми: {greedy_time_large:.5f} мс")
print(f"Час Динамічного Програмування для визначення великої суми: {dp_time_large:.5f} мс")