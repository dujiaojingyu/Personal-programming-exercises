# _*_ coding: utf-8 _*_
# 程序 6-3.py (Python 3.x version)
# 计算单词在文章中出现的频率
# 只列出出现超过一次以上的单词
import re

fp = open("sample.txt", "r")
article = fp.read()
new_article = re.sub("[^a-zA-Z\s]", "", article)
words = new_article.split()
word_counts = {}
for word in words:
    if word.upper() in word_counts:
        word_counts[word.upper()] = word_counts[word.upper()] + 1
    else:
        word_counts[word.upper()] = 1

key_list = list(word_counts.keys())
key_list.sort()
for key in key_list:
    if word_counts[key] > 1:
        print("{}:{}".format(key, word_counts[key]))
