# DP, 

def solution(n, info_A):
    info_L = [0]*11
    arrow_L = [i+1 for i in info_A[:-1]]
    rate = [[10-index,(2-(hit==1))*(10-index),hit] for index,hit in enumerate(arrow_L)]
    rate.sort(key=lambda x:x[0])    
    dp = [[0,[],11] for _ in range(n+1)]
    for a,b,c in rate:
        for x in range(n,c-1,-1):
            if dp[x-c][0]+b > dp[x][0] or (dp[x-c][0]+b == dp[x][0] and dp[x-c][2] < dp[x][2]):
                dp[x][0] = dp[x-c][0]+b
                dp[x][1] = dp[x-c][1]+[a]
                dp[x][2] = min(dp[x][1])
    for i in dp[n][1]:
        info_L[10-i] = arrow_L[10-i]
    info_L[-1] = n-sum(info_L)        
    answer = sum(((l>a)-(a>l))*(10-index) for index,(a,l) in enumerate(zip(info_A,info_L)))
    return info_L if answer>0 else [-1] 


# dfs

# def solution(n, info):
#     global max_gap, answer
    
#     answer = [-1]
#     score = [0]*11
#     max_gap=0
    
#     def is_winner_with_gap(score):
#         a=0 # 어피치 점수
#         b=0 # 라이언 점수
        
#         for i in range(len(info)):
#             if info[i] > 0 or score[i] > 0:
#                 if info[i]>=score[i]:
#                     a += (10-i)
#                 else:
#                     b += (10-i)
#         return (b > a, abs(a-b))

#     def dfs(L, cnt):
#         global max_gap, answer
#         if L == 11 or cnt == 0:    
#             is_winner, gap = is_winner_with_gap(score)
#             if is_winner:
#                 if cnt >= 0: # 화살이 남은 경우
#                     score[10] = cnt # 0점에 쏴도 이김
                
#                 if gap > max_gap: # 갭이 더 큰 경우로 업데이트
#                     max_gap = gap
#                     answer = score.copy()
                    
#                 elif gap == max_gap: # 가장 낮은 점수를 많이 맞힌 경우로 업데이트
#                     for i in range(len(score)):
#                         if answer[i] > 0:
#                             max_i_1 = i
#                         if score[i] > 0:
#                             max_i_2 = i
#                     if max_i_2 > max_i_1:
#                         answer = score.copy()
                    
#             return
        
#         # k점을 어피치보다 많이 맞추거나 아예 안맞추거나
#         if cnt>info[L]:
#             score[L]=info[L]+1
#             dfs(L+1, cnt-(info[L]+1))
#             score[L]=0
            
#         dfs(L+1, cnt)
    
#     dfs(0,n)
    
#     return answer