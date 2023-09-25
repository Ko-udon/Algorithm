# -*- coding: utf-8 -*-
"""pyalgo_알고리즘 베스트10 문제풀이.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14o94nJAKCvZvWIADJCofgjEmXGick0Mt
"""

# 1. 자격증명

def solution(data):
    result = ''
    for d in data:
        result += chr(int(d.replace(" ","").replace("+", "1").replace("-", "0"),2))
    return result

# 2. 암호문
import re
def solution(data):
    days = re.findall('([r,e,v])(10|[0-9])',data)
    day = 0
    print(days)
    for i, j in days:
        day += int(j)
    print(day)
    return f'{day//10}월 {day%10}일'
solution('a10b9r1ce33uab8wc918v2cv11v9')

# 3. 출정인원 선발
data = [['A',25, 25, 25,25],
        ['B',10,12,13,11],
        ['C',24,22,23,21],
        ['D',13,22,16,14]
        ]

def solution(data):
    size = len(data)
    choose = int((size * 3) / 10)
    if choose == 0:
        return
    choosed_count = 0
    score = {}
    choosed = []
    for i in data:
        total = sum(i[1:])
        if total in score:
            score[total] = score[total] + i[0]
        else:
            score[total] = i[0]

    for i in sorted(list(score.items()),reverse = True):
        if choosed_count <= choose and len(i[1]) <= choose and choosed_count != choose:
            choosed.extend(i[1])
            choosed_count += len(i[1])
        elif len(i[1]) > choose:
            return choosed

    return sorted(choosed, reverse = True)

solution(data)

# 4. 꿈의 설계
import re

data = ['10 - A. 20 - B. 30 - A.', '1 - A. 1 - A. 1 - A. 1 - A. 2 - B. 1 - A. 1 - B']

def solution(data):
    training_value = {}
    gomin_value = {}
    future = 0
    change_future = 0

    #훈련 수치
    for i in data[0].split('.')[:-1]:
        key = re.findall(r'[a-zA-Z]', i)[0]
        value = re.findall(r'\d+', i)[0]
        if key in training_value:
            training_value[key] += int(value)
        else:
            training_value[key] = int(value)

    # 고민 수치
    for i in data[1].split('.')[:-1]:
        key = re.findall(r'[a-zA-Z]', i)[0]
        value = re.findall(r'\d+', i)[0]
        if key in gomin_value:
            gomin_value[key] += int(value)
        else:
            gomin_value[key] = int(value)

    #원래 미래
    for i in training_value.keys():
        if i in gomin_value:
            future += training_value[i] * gomin_value[i]
    if future == 0:
        return '미래가 보이지 않습니다.'

    # 가장 큰 값에 100을 더해주기
    most_training_value = max(training_value.values())
    most_gomin_value = max(gomin_value.values())

    for i in training_value:
        if training_value[i] == most_training_value:
            training_value[i] += 100
    for i in gomin_value:
        if gomin_value[i] == most_gomin_value:
            gomin_value[i] += 100
    for i in training_value.keys():
        if i in gomin_value:
            change_future += training_value[i] * gomin_value[i]

    return f'최종 꿈의 설계는 원래 미래 {future}, 바뀐 미래 {change_future}입니다. 이 수치대로 Vision을 만듭니다.'

solution(data)

# 5. 상한 당근 찾기

data = [[0, 0, '#', '#'], ['#', '#', 0, '#'], [0, '#', '#', 0]]

def solution(data):
    for i in range(len(data)):
        for j in range(len(data[1])):
            if data[i][j] == '#':
                #상
                if i != 0:
                    if data[i-1][j] != '#':
                        data[i-1][j] +=1
                #하
                if i != len(data) - 1:
                    if data[i+1][j] != '#':
                        data[i+1][j] +=1

                #좌
                if j != 0:
                    if data[i][j-1] != '#':
                        data[i][j-1] +=1

                #우
                if j != len(data[0]) - 1:
                    if data[i][j+1] != '#':
                        data[i][j+1] +=1

                #(좌 대각선 상)
                if j != 0 and i != 0:
                    if data[i-1][j-1] != '#':
                        data[i-1][j-1] +=1

                #(우 대각선 하)
                if j != len(data[0]) - 1 and i != len(data) - 1:
                    if data[i+1][j+1] != '#':
                        data[i+1][j+1] +=1

                # 우 대각선 상
                if j != len(data[0]) - 1 and i != 0:
                    if data[i-1][j+1] != '#':
                        data[i-1][j+1] +=1


                # 좌 대각선 하
                if j != 0 and i != len(data) - 1:
                    if data[i+1][j-1] != '#':
                        data[i+1][j-1] +=1

    return [sum(data, []).count('#'), sum(list(filter(lambda x:type(x) == int, sum(data, []))))]

solution(data)

# 6. 샌드위치

# 문제: https://pyalgo.co.kr/?page=6
#  1, 2, 3, 4, 1
# [1, 1, 1, 2, 3, 4, 1, 2, 3, 4, 1] -> 2개
# 1, 2, 3, 4, 1, 2, 3, 4, 1


# 스택으로 풀기
# data = [1, 1, 1, 2, 3, 4, 1, 2, 3, 4, 1]
data = [1, 2, 3, 4, 1, 2, 3, 4, 1]
def solution(data):
    sandwitch = [1, 2, 3, 4, 1]
    count = 0
    stack = []

    for i in data:
        stack.append(i)
        if len(stack) >= 5 and stack[-5:] == sandwitch: # 뒤에서 5번째 부터 끝까지 값이 샌드위치와 일치하는지 확인
            stack = stack[0:-5] # 샌드위치 pop()
            count+=1
    return count


# string으로 풀기
data = [1, 1, 1, 2, 3, 4, 1, 2, 3, 4, 1]
data = [1, 2, 3, 4, 1, 2, 3, 4, 1]
def solution(data):
    sandwitch = '12341'

    data_str = ''.join(map(str,data)) # 문자열로 바꾸기
    count = 0
    while sandwitch in data_str:
        count+=1
        data_str = data_str.replace(sandwitch, '', 1) # 샌드위치 패턴 제거, 한번만!
    return count
solution(data)

# 7. 두 수의 합 찾기
# 문제: https://pyalgo.co.kr/?page=7#
from itertools import combinations

data = [[1, 5, 10, 20, 93], 103]	# 오름차순
def solution(data):
    result = list(combinations(data[0], 2))
    answer_list = list(filter(lambda x : x[0]+x[1] == data[1], result))
    first = data[0].index(answer_list[0][0])
    second = data[0].index(answer_list[0][1], first+1)
    return [first, second]

solution(data)