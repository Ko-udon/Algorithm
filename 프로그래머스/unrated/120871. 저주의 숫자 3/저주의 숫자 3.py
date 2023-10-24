def solution(n):
    mura = []
    for i in range(1,200):
        if '3' not in str(i) and i%3 != 0:
            mura.append(i)
    return mura[n - 1]