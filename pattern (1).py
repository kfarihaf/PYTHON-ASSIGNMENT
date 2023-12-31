# -*- coding: utf-8 -*-
"""Pattern

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bmNJ6uYG2e0eq_88_-VOViNkLvLs2DXJ

#PATTERN ASSESMENT
"""

1.
#    *
#   **
#  ***
# ****
#*****
a=1
b=4
while(b>=0):
  print(' '*b+'*'*a)
  a+=1
  b-=1

n=4
for i in range(1,6):
  for j in range(i+1):
    if(j==1):
      print(' '*n,'*'*i)
      n-=1

2.
#    *
#   ***
#  *****
# *******
#*********

a=1
b=4
while(b>=0):
  print(' '*b+'*'*a)
  a+=2
  b-=1

n=4
for i in range(1,10,2):
  for j in range(i+1):
    if(j==i):
      print(' '*n,'*'*i)
      n-=1

3.
#  *********
#   *******
#    *****
#     ***
#      *
n=0
for i in range(9,0,-2):
  for j in range(i+1):
    if(j==i):
      print(' '*n,'*'*i,end='')
      n+=1
  print()

a=9
b=0
while(b<=4):
  print(' '*b+'*'*a)
  a-=2
  b+=1

4.
#    *
#   ***
#  *****
# *******
#*********
# *******
#  *****
#   ***
#    *
a=1
b=4
while(b>=0):
  print(' '*b+'*'*a)
  a+=2
  b-=1
a=9
b=0
while(b<=4):
  print(' '*b+'*'*a)
  a-=2
  b+=1

n=4
for i in range(1,10,2):
  for j in range(i+1):
    if(j==i):
      print(' '*n,'*'*i,end='')
      n-=1
  print()
n=1
for i in range(7,0,-2):
  for j in range(i+1):
    if(j==i):
      print(' '*n,'*'*i,end='')
      n+=1
  print()

5.
# 2 9
# 3 8
# 4 7
# 5 6
# 6 5
# 7 4
# 8 3
# 9 2
# 10 1
a=2
b=9
while(a<=10):
  print(a,b)
  a+=1
  b-=1

for i in range(2,11):
  print(i,11-i)

6.
# 1
# 22
# 333
# 4444
# 55555
for i in range(1,6):
  for j in range(i):
    print(i,end='')
  print()

a=1
while(a<=5):
  j=1
  while(j<=a):
     print(a,end='')
     j+=1
  a+=1
  print()

7.
# 54321
# 4321
# 321
# 21
# 1
for i in range(5,0,-1):
  for j in range(i,0,-1):
    print(j,end='')
  print()

a=5
b=5
while(a>=0):
  b=a
  while(b>=1):
    print(b,end='')
    b-=1
  a-=1
  print()

8.
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
i=1
j=1
a=1
while(i<=5):
  while(j<=i):
    print(a,end='')
    a+=1
    j+=1
  print()
  i+=1
  j=1

a=1
for i in range(1,6):
  for j in range(i):
    print(a,end=' ')
    a+=1
  print()

9.
# 1 2 3 4 5
# 6 7 8 9
# 10 11 12
# 13 14
# 15
a=1
for i in range(5,0,-1):
  for j in range(i):
    print(a,end=' ')
    a+=1
  print()

i=5
j=5
a=1
while(i>=1):
  j=i
  while(j>=1):
    print(a,end=' ')
    a+=1
    j-=1
  i-=1
  print()

10.
# 0 x 9 + 8 = 8
# 9 x 9 + 7 = 88
# 98 x 9 + 6 = 888
# 987 x 9 + 5 = 8888
# 9876 x 9 + 4 = 88888
# 98765 x 9 + 3 = 888888
# 987654 x 9 + 2 = 8888888
# 9876543 x 9 + 1 = 88888888
# 98765432 x 9 + 0 = 888888888
for i in range(10,1,-1):
    if(i==10):
      b="0"
      a=8
    else:
      b+=str(i)
      a-=1
    print(f"{(int(b))}x9+{a}={((int(b))*9)+a}")

11.
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25
# 6 12 18 24 30 36
# 7 14 21 28 35 42 49
# 8 16 24 32 40 48 56 64
# 9 18 27 36 45 54 63 72 81
# 10 20 30 40 50 60 70 80 90 100
a=1
for i in range(1,11):
  for j in range(i):
    print(i*(j+1),end=' ')
  print()

12.
#            1
#          2 3
#        4 5 6
#      7 8 9 10
#11 12 13 14 15
b=11
a=1
for i in range(1,6):
   print(' '*b,end='')
   for j in range(1,i+1):
    print(a,end=' ')
    a+=1
    b-=1
   print()

13.
# A
# A A
# A A A
# A A A A
# A A A A A
a=1
b=0
for i in range(1,6):
  print(' '*b,'A '*a)
  a+=1

14.
# A
# AB
# ABC
# ABCD
# ABCDE
a=1
while(a<=5):
  b=1
  while(b<=a):
   c=chr(ord('A')+b-1)
   print(c,end='')
   b+=1
  print()
  a+=1

for i in range(1,6):
  for j in range(1,i+1):
     a=chr(ord('A')+j-1)
     print(a,end='')
  print()

15.
#   A
#  ABC
# ABCDE
n=2
for i in range(1,6,2):
  print(' '*n,end='')
  for j in range(1,i+1):
    c=chr(ord('A')+j-1)
    print(c,end='')
  print()
  n-=1

16.
# A
# BC
# DEF
# IJKL
# MNOPQ
# RSTUVW
a='ABCDEFIJKLMNOPQRSTUVWXYZ'
b=0
for i in range(0,6):
  for j in range(i+1):
    print(a[b],end='')
    b+=1
  print()

17.
#   A
#  BCD
# EFGHI
n=2
a=1
for i in range(1,6,2):
  print(' '*n,end='')
  for j in range(1,i+1):
    c=chr(ord('A')+a-1)
    print(c,end='')
    a+=1
  print()
  n-=1