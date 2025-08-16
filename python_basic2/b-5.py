# 合計値を計算する関数
def calc_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# 最大値を計算する関数
def calc_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


# 最小値を計算する関数
def calc_min(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value


# 平均値を計算する関数
def calc_mean(numbers):
    total = calc_sum(numbers)
    count = 0
    for _ in numbers:
        count += 1
    return total / count


# メイン処理
input_str = input("スペース区切りの整数を入力してください: ")
input_list = input_str.split()
numbers = []
for item in input_list:
    numbers.append(int(item))

# 結果表示
print("合計値:", calc_sum(numbers))
print("最大値:", calc_max(numbers))
print("最小値:", calc_min(numbers))
print("平均値:", format(calc_mean(numbers), ".1f"))

