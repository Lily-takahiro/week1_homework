rows = int(input("行数を入力してください:"))
cols = int(input("列数を入力してください:"))


for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(f"{i}X{j}={i * j:2}", end=" ")
print()  # 改行
