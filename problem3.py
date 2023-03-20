'''


Date: Mar 19, 2023.


Author :  Name: Sejin Yoon
          uID: u1311019


Source code File name: problem3.py


'''



n = int(input("Enter a positive integer: "))
sum = 0
for i in range(1, n+1):
    sum += 1/i
print("The sum of the series is:", round(sum, 2))


n = int(input("Enter a positive integer: "))
sum = 0
for i in range(1, n+1):
    sum += pow(n, n)/n
print("The sum of the series is:", round(sum, 2))