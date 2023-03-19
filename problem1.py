'''


Date: Mar 19, 2023.


Author :  Name: Sejin Yoon
          uID: u1311019


Source code File name: problem1.py


'''


word = input('Write the word: ')

palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:
        palindrome = False
        break

print(palindrome)