
import codecs
import collections


fd = codecs.open("heptral.txt", 'r','utf-16')
sqlFile = str(fd.read())

# print (sqlFile)

from pymystem3 import Mystem
import re

RU = Mystem()
lemmas = RU.lemmatize(sqlFile)
analysis = RU.analyze(sqlFile)
type_pattern = re.compile("^([A-Z]+)*")
# print (lemmas)
# for i in range(lemmas):

# ROS_dict = {i.get('analysis')[0].get('lex'): \
#                 type_pattern.findall(i.get('analysis')[0].get('gr'))[0] \
#             for i in analysis if 'analysis' in i.keys()}


wordcount = {}
for word in lemmas:
    if len(word)>5:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)
lst = word_counter.most_common(n_print)
# df = pd.DataFrame(lst, columns = ['Word', 'Count'])
# df.plot.bar(x='Word',y='Count')
