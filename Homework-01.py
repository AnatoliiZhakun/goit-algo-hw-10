# Набір монет
coins = [50, 25, 10, 5, 2, 1]

# 1. Жадібний алгоритм
def find_coins_greedy(amount):
    remaining = amount
    result = {}
    for coin in coins:
        count = remaining // coin
        if count > 0:
            result[coin] = count
            remaining -= coin * count
    return result

# 2. Алгоритм динамічного програмування
def find_min_coins(amount):
    # Мінімальна кількість монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Для суми 0 потрібно 0 монет

    # Відстежуємо, яку монету використали для досягнення суми
    coin_used = [0] * (amount + 1)

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
                coin_used[a] = coin

    # Відновлення складу монет
    result = {}
    a = amount
    while a > 0:
        coin = coin_used[a]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        a -= coin

    return result

# Приклад використання
amount = 113
print("Жадібний алгоритм:", find_coins_greedy(amount))
print("Динамічне програмування:", find_min_coins(amount))
