{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "source": [
    "input_string = input(\"Введите строку: \") \n",
    "\n",
    "words = input_string.split() \n",
    "\n",
    "longest_word = max(words, key=len) \n",
    "\n",
    "print(\"Самое длинное слово:\", longest_word) "
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Самое длинное слово: прекрасный\n"
     ]
    }
   ],
   "metadata": {}
  }
 ],
 "nbformat": 4,
 "nbformat_minor": 2,
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": 3
  },
  "orig_nbformat": 4
 }
}