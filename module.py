'''
#로또 번호 뽑아보자
import random

numbers = range(1,46)

lotto = random.sample(numbers,6)
#random.sample(a,n) : a에서 랜덤한 n개의 데이터를 추출하는 함수

print(lotto)
'''
