#!/usr/bin/env python

while True:
    sentence = input("Enter your text: ")
    spoiledSentence = ""
    for letter in sentence:
        spoiledSentence = spoiledSentence + "||" + letter + "||"
        print(spoiledSentence)
