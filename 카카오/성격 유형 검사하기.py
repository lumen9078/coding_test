''' 프로그래머스 레벨 1
- 성격 유형은 2 * 2 * 2 * 2 = 16가지
    1. 라이언형(R), 튜브형(T)
    2. 콘형(C), 프로도형(F)
    3. 제이지형(J), 무지형(M)
    4. 어피치형(A), 네오형(N)
- 총 N개의 질문
    - 매우 동의 or 매우 비동의 3점
    - 동의 or 비동의 2점
    - 약간 동의 or 약간 비동의 1점
    - 모르겠음 0점
- 하나의 지표에서 각 성격 유형 점수가 같으면, 사전 순으로 빠른 성격 유형
- 질문마다 판단하는 지표를 담은 1차원 배열 survey
    - survey의 원소: "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"
    - survey[i]의 첫번째 캐릭터는 i + 1번째 질문의 비동의 관련 선택지 성격 유형
    - survey[i]의 두번째 캐릭터는 i + 1번째 질문의 동의 관련 선택지 성격 유형
- 검사자가 각 질문마다 선택한 선택지를 담은 1차원 배열 choices
    - choices[i]: 검사자가 선택한 i + 1번째 질문의 선택지
    - 1: 매우 비동의, 2: 비동의, 3: 약간 비동의, 4: 모르겠음, 5: 약간 동의, 6: 동의, 7: 매우 동의
'''

survey_list = input().split()
# survey_dict = {["RT", "TR"]: {"R": 0, "T": 0}, ["CF", "FC"]: {"C": 0, "F": 0}, ["JM", "MJ"]: {"J": 0, "M": 0}, ["NA", "AN"]: {"A": 0, "N": 0}}
survey_dict = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
choices_list = list(map(int, input().split()))
choices_dict = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}

for num in range (0, len(survey_list)):
    survey = survey_list[num]
    choices = choices_list[num]
    
    if choices > 4:
        survey_dict[survey[1]] += choices_dict[choices]
    else:
        survey_dict[survey[0]] += choices_dict[choices]

print(survey_dict)
result = ''
for i in ["RT", "FC", "MJ", "AN"]:
    if survey_dict[i[0]] == survey_dict[i[1]]:
        result += sorted(list(i))[0]
    else:
        result += max((i[0], survey_dict[i[0]]), (i[1], survey_dict[i[1]]), key=lambda x:x[1])[0]
print(result)