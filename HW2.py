P = "My name is Min Byounghee"

# 1. 문자열의 문자수 출력
print("1. 문자 수:", len(P))

# 2. 문자열을 10번 반복한 문자열 출력
print("2. 10번 반복:", P * 10)

# 3. 문자열의 첫 번째 문자 출력
print("3. 첫 번째 문자:", P[0])

# 4. 처음 4문자 출력
print("4. 처음 4문자:", P[:4])

# 5. 마지막 4문자 출력
print("5. 마지막 4문자:", P[-4:])

# 6. 문자열 거꾸로 출력
print("6. 거꾸로 출력:", P[::-1])

# 7. 첫 번째 문자와 마지막 문자 제거한 문자열 출력
print("7. 첫/마지막 문자 제거:", P[1:-1])

# 8. 모두 대문자로 변경
print("8. 대문자:", P.upper())

# 9. 모두 소문자로 변경
print("9. 소문자:", P.lower())

# 10. 'a'를 'e'로 대체
print("10. 'a' → 'e' 대체:", P.replace('a', 'e'))
