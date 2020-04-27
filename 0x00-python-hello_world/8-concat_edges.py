#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[(46-7):(74-7)] + str[(74-7+40):(74-7+45)] + str[:6]
print(str)
