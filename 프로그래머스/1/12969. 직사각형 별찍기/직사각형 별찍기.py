a, b = map(int, input().strip().split(' ')) # 별 그리기 n, m값 가져오기

for i in range(b):
    string = '*' * a
    print(string)
