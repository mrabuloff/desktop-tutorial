# 1st program
print((9 * 5) ** 0, 5)

# 2st program
print(9.99 > 9.98 and 1000 != 1001)

# 3st program
print(((1234 % 1000) // 10) + ((5678 % 1000) // 10))

# 4st program

a, b = 13.42, 42.13

ai, bi = int(a), int(b)  # цели числа
af, bf = int((a - ai) * 100), int((b - bi) * 100)  # дрообные числа

print(ai == bf or bi == af)