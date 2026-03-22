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