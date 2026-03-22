#### 리스트 (list)

# mbti = ['INTJ', 'INTP', 'INFJ', 'INFP']

# print(mbti)
# print(mbti[0])

# mbti[0] = 'ENFP' # 리스트에 새로운 값 할당 
# print(mbti)
# print(mbti[0])
# # -> 첫번째 요소 변경이 됨 

# my_list = [123, 'apple'] # 파이썬은 데이터가 이렇게 일관성 없어도 가능 
# print(my_list)
# # 이렇게 하면 다른 for문이나 할때 문제가 될 수 있음
# # 리스트에 넣을 타입 고려는 해야함 

# -------------------------------------------------------------------

# colors = ['red', 'green', 'blue']

# # 수정 
# colors[2] = 'block' # 리스트의 요소 수정
# print(colors)

# # 추가 
# colors.append('yellow') # 리스트의 끝에 요소 추가
# print(colors)

# colors.insert(1, 'white') # 리스트의 특정 위치에 요소 추가
# print(colors)

# # 삭제  
# del colors[0] # 리스트에서 특정 위치의 요소 삭제
# # del : 리스트에서 특정 위치의 요소 삭제 (반환하지 않음)
# print(colors)

# color = colors.pop(0) # 리스트에서 특정 위치의 요소 제거
# # pop : 리스트에서 특정 위치의 요소 제거하고 반환
# print(colors)
# print(color) # pop은 제거한 요소를 반환하기 때문에, 제거된 요소를 변수에 저장할 수 있음

# colors.remove('green') # 리스트에서 특정 요소 제거
# print(colors)

# -------------------------------------------------------------------

# colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']

# 정렬

# colors.sort() # 리스트의 요소를 오름차순으로 정렬
# print(colors) # abc 순서로 정렬됨 , 원본 데이터를 변경 -> 이후 코드는 변경된 순서로 진행됨

# colors.sort(reverse=True) # 리스트의 요소를 내림차순으로 정렬
# print(colors)

# sorted(colors) # 리스트의 요소를 오름차순으로 정렬 (원본 유지)
# print(colors) # 원본 데이터는 변경되지 않음
# print(sorted(colors)) # 정렬된 리스트 반환

# 길이 - 요소의 갯수 
# print(len(colors)) # 리스트의 길이 (요소의 갯수) 반환

# print(colors[7]) # IndexError: list index out of range
# # 리스트의 인덱스 범위를 벗어난 접근 -> 오류 발생

# print(colors[-1]) # 리스트의 마지막 요소 반환

# -------------------------------------------------------------------

# colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']

# 리스트 슬라이싱 - 리스트의 일부분을 추출하여 새로운 리스트를 생성

# print(colors[1:4]) # 리스트의 인덱스 1부터 3까지의 요소 반환 (4는 포함되지 않음)
# print(colors[:3]) # 리스트의 처음부터 인덱스 2까지의 요소 반환 (3은 포함되지 않음)
# print(colors[3:]) # 리스트의 인덱스 3부터 끝까지의 요소 반환
# print(colors[:]) # 리스트의 모든 요소 반환 (원본 리스트와 동일한 새로운 리스트 생성)    
# print(colors[-5:]) # 리스트의 인덱스 -5부터 끝까지의 요소 반환 (음수 인덱스는 리스트의 끝에서부터 계산)

# colors_2 = colors[:] # 리스트의 모든 요소를 복사하여 새로운 리스트 생성
# print(colors_2) # colors_2는 colors의 복사본이므로, colors의 변경이 colors_2에 영향을 미치지 않음

# # colors_2 = colors 하면 되는거 아니냐? 
# # -> 이렇게 하면 colors_2는 colors의 참조가 되기 때문에, colors의 변경이 colors_2에 영향을 미침
# # 메모리 주소를 공유하게 됨

# colors_2 = colors[:]
# colors_2.pop()
# print(colors) 
# print(colors_2) 

# -------------------------------------------------------------------

# scores = [85, 90, 78, 92, 88, 100]

# scores.sort(reverse=True) 

# for score in scores:
#     # print(score) # 리스트의 각 요소를 순회하며 출력
    
#     if score >= 90:
#         print(score)
#     else:
#         print("fail")

# -------------------------------------------------------------------

# scores = [85, 90, 78, 92, 88, 100]

# max_val = max(scores) # 리스트의 최대값 반환
# min_val = min(scores) # 리스트의 최소값 반환
# sum_val = sum(scores) # 리스트의 요소들의 합 반환
# avg_val = sum_val / len(scores) # 리스트의 요소들의 평균 계산

# # sum 원시적으로 구하기 
# sum_values = 0

# for score in scores:
#     sum_values += score
# print(sum_values)

# # sum 함수를 사용하여 구하기
# print(sum_val)

# -------------------------------------------------------------------