"""
N명의 이름과 국어 영어 수학 점수가 주어진다 
학생 성적 정렬 

국어 점수 reverse true
국어 점수 다음 영어 점수 reverse false
수학 점수 reverse true 
모든 점수가 같으면 이름이 사전순으로  
아스키 코드에서 대문자는 소문자 앞에 온다 
"""
import sys


n = int(input())
student = []
for i in range(n):
    name, ko, en, ma = sys.stdin.readline().rstrip().split()
    student.append((name, ko, en, ma))

student.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))


for i in student:
    print(i[0])
