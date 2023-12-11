from itertools import combinations
# 혼자 해결 실패
# 코드 보고 공부하자

def solution(relation):
    li=[ [] for _ in range(len(relation[0])) ]

	# 튜플로 묶여있는 값을 컬럼으로 묶어줍니다
    for i in relation:
        for j in range(len(i)):
            li[j].append(i[j])

    count=0
    all_val=[]
    # 저는 컬럼을 묶을때 인덱스의 조합을 구하고 해당 인덱스에 맞는 컬럼을 넣는식으로 계산했기때문에 인덱스만 포함된 리스트를 만들었습니다.
    idx_li=[ i for i in range(len(li))]
    
    # n개의 후보키 선택
    for n in range(len(relation[0])+1):
    	# n개일때 선택할 수 있는 컬럼의 경우의수
        li_com = list(combinations(idx_li,n))
        
        # 각 경우의 수마다 후보키가 가능한지 판별
        for i in li_com:
        	# 문자열로 만들었을때 고유성을 만족하는지 판별하기위한 리스트
            idx_com=[ "" for _ in range(len(relation))]
            for j in i:
                for idx in range(len(li[j])):
                	# 문자열로 묶을때 "+"를 사용한 이유는 [[a,aa],[aa,a]]인 릴레이션은 고유성을 만족하기 때문에 후보키로 사용할 수 있지만 문자로 합치면 aaa,aaa가 되므로 잘못된 결과가 나올수 있습니다 때문에 +를 사용하여 a+aa,aa+a 가 되도록 하였습니다.
                    idx_com[idx]+=("+"+str(li[j][idx]))
            # 고유성을 가진다면 count+=1과 고유성만 만족한 후보키 리스트에 추가
            if len(idx_com)==len(set(idx_com)):
                count+=1
                all_val.append(list(i))

	# 최소성 확인
    for i in range(len(all_val)):
        for j in range(i+1,len(all_val)):
            if len(all_val[i])==0 or len(all_val[j])==0:
                continue
            t=True
            for a in all_val[i]:
                if a not in all_val[j]:
                    t=False
                    break
            if t:
                count-=1
                all_val[j]=[]
    return count