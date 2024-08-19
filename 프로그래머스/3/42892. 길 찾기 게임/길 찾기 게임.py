# 풀의 참고
from sys import setrecursionlimit
setrecursionlimit(10000)

def REC(nodeinfo, result):
    if nodeinfo:
        highest = (0,-1,0) ### 루트 노드 정보: (nodeinfo 에서 index, y, 노드번호)
        for idx, (x,y,n) in enumerate(nodeinfo): ### 루트 노드 idx 찾기 (3분할 과정)
            if y > highest[1]:
                highest = (idx, y, n)

        result[0].append(highest[-1]) ### 좌,우 재귀함수 실행전 루트노드 탐색 --> 전위 순회
        left, right = nodeinfo[:highest[0]], nodeinfo[highest[0]+1:]
        REC(left, result), REC(right, result)
        result[1].append(highest[-1]) ### 좌,우 재귀함수 실행후 루트노드 탐색 --> 후위 순회
    return result

def solution(nodeinfo): ### ↓ n:노드번호 추가하여 (x,y,n) 형태로 x좌표 기준 정렬
    nodeinfo = sorted([(x,y,i+1) for i,(x,y) in enumerate(nodeinfo)], key=lambda x:x[0])
    result = [[], []]
    ans = REC(nodeinfo, result)
    return ans