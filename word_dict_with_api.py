"""
This word ditionary is built using PyDictionary
"""

from PyDictionary import PyDictionary

PyDictionary = PyDictionary()


while True:
    word = input("Enter your word: ")
    if word == "":
        break
    print(PyDictionary.meaning(word))


""""
You can also get the meaning of a list of words and PyDictionary will return a meaning of all of them
# dictionary = PyDictionary("eyes, head, tail")
print(dictionary.printMeaning())
"""