import datetime
import time
import random
import math

print("1:import txt | 2:random")
mode = int(input("select mode:"))
if mode ==1:
 with open("poly.txt","r") as file:
  contents = file.readlines()
 file.close()
 print(contents)
 p=0
 print(contents[p][0:])
 p=p+1




elif mode ==2:
 pass

 print("error")

 print("|satart-------------------end|")
 for i in range(0,10,1):
  print("== ",end='')
 time.sleep(1)
 num = int(input("answer:"))

else:
 pass



def randompoly():
 pass

def solution(data,A,B,C,answer1,answer2):
 classify = data.find('^2')

 if classify > 1: #2�?
  num_list = data.split('x^2') #문자?��->계수 분리?�� int?��?���? �?�?
  A = int(num_list[0]) #x^2 계수
  num_list = num_list[1].split('x')
  B = int(num_list[0]) #x 계수
  C = int(num_list[1]) #?��?��
  answer1= -((B+math.sqrt(B*B-4*A*C))/2*A)
  answer2= -((B-math.sqrt(B*B-4*A*C))/2*A)
  print(answer1,answer2)
  return(answer1, answer2)
 else: #1�?
  num_list = data.split('x')
  B = int(num_list[0]) #x 계수
  C = int(num_list[1]) #?��?��
  answer1r=(-C/B)
  print(answer1)
  print(answer1)






