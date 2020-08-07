upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter_and_space = upper_alphabet + upper_alphabet.lower() + ' \t\n'

import os, sys

#dictionary 읽어들이기
def loadDictionary():
    #os.chdir('시저암호')
    dictionary_file = open('시저암호/dictionary.txt')
    EnglishWords = {}
    for word in dictionary_file.read().split('\n'):
        EnglishWords[word] = None
    dictionary_file.close()
    return EnglishWords

# 전역변수
EnglishWordS = loadDictionary()

# --- letter, space만 추가하는 함수
def removeNonLetters(message):
    letters_only = [] #list
    for ch in message:
        if ch in letter_and_space:
            letters_only.append(ch)
    return ''.join(letters_only)

#----- 올바른 영어단어의 비율
def percentEnglishWords(message):
    message = message.lower()
    message = removeNonLetters(message)
    possible_words = message.split()

    if possible_words == []:
        return 0.0
    count_words = 0
    for word in possible_words:
        if word in EnglishWordS:
            count_words += 1
    return float(count_words)/len(possible_words)

#----- 영어인지 판정하기
def isEnglish(message, wordPercentage = 20, letterPercentage = 80):
    wordsMatch = percentEnglishWords(message)*100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    
    return wordsMatch and lettersMatch
