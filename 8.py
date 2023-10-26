# 描述
# 现在有一些英语单词需要做拼写检查，你的工具是一本词典。需要检查的单词，有的是词典中的单词，有的与词典中的单词相似，你的任务是发现这两种情况。单词A与单词B相似的情况有三种：
# 1、删除单词A的一个字母后得到单词B；
# 2、用任意一个字母替换单词A的一个字母后得到单词B；
# 3、在单词A的任意位置增加一个字母后得到单词B。
# 你的任务是发现词典中与给定单词相同或相似的单词。


# 输入
# 第一部分是词典中的单词，从第一行开始每行一个单词，以"#"结束。词典中的单词保证不重复，最多有10000个。
# 第二部分是需要查询的单词，每行一个，以"#"结束。最多有50个需要查询的单词。
# 词典中的单词和需要查询的单词均由小写字母组成，最多包含15个字符。
# 输出
# 按照输入的顺序，为每个需要检查的单词输出一行。如果需要检查的单词出现在词典中，输出“?x is correct"，?x代表需要检查的单词。如果需要检查的单词没有出现在词典中，则输出"?x: ?x1 ?x2 ...?xn"，其中?x代表需要检查的单词，?x1...?xn代表词典中与需要检查的单词相似的单词，这些单词中间以空格隔开。如果没有相似的单词，输出"?x:"即可。
# 样例输入

# i
# is
# has
# have
# be
# my
# more
# contest
# me
# too
# if
# award
# #
# me
# aware
# m
# contest
# hav
# oo
# or
# i
# fi
# mre
# #
# 样例输出
# me is correct
# aware: award
# m: i my me
# contest is correct
# hav: has have
# oo: too
# or:
# i is correct
# fi: i
# mre: more me

dictionary = []
while True:
    word = input()
    if word == "#":
        break
    dictionary.append(word)
queries = []
while True:
    word = input()
    if word == "#":
        break
    queries.append(word)
for query in queries:
    if query in dictionary:
        print(query + " is correct")
    else:
        similar_words = []
        for word in dictionary:
            if abs(len(query) - len(word)) > 1:
                continue
            if len(query) == len(word) - 1:
                deleted_word = ""
                for i in range(len(word)-1):
                    if word[i] != query[i]:
                        deleted_word = word[:i] + word[i+1:]
                        break
                if deleted_word=="":
                    deleted_word=word[0:len(word)-1]
                if deleted_word == query:
                    similar_words.append(word)
            elif len(query) == len(word):
                replaced_word = ""
                for i in range(len(word)):
                    if word[i] != query[i]:
                        replaced_word = word[:i] + query[i] + word[i+1:]
                        break
                if replaced_word == query:
                    similar_words.append(word)
            elif len(query) == len(word) + 1:
                inserted_word = ""
                for i in range(len(query)):
                    if i == len(query) - 1 or query[i] != word[i]:
                        inserted_word = word[:i] + query[i] + word[i:]
                        break
                if inserted_word == query:
                    similar_words.append(word)
        if len(similar_words) > 0:
            print(query + ": " + " ".join(similar_words))
        else:
            print(query + ":")