import sys
input = sys.stdin.readline

def dfs(pre_word, picked):
    # 문자열과 picked(지금까지 선택한 문자열 수)가 같을 경우 return 1
    if picked == len(S):
        return 1
    
    answer = 0
    for key in counter.keys():
        # 이전의 문자와 같은 문자일 경우
        if pre_word == key:
            continue
        
        # 해당 key의 남은 value가 0일 경우
        if counter[key] == 0:
            continue
       
        # 해당 key를 사용했기 때문에 -1
        counter[key] -= 1
        # 당 key로 시작하는 모든 문자를 재귀로 생성
        answer += dfs(key, picked + 1)
        # 해당 key로 시작하는 모든 문자를 만들었기 때문에 +1로 되돌려줌 -> 새로운 문자열 시작
        counter[key] += 1

    return answer

S = list(input().strip())

# 입력받은 문자열에서 각 문자의 횟수를 counter에 저장
counter = dict()
for s in S:
    if s in counter:
        counter[s] += 1
    else:
        counter[s] = 1

answer = dfs('', 0)
print(answer)