# 描述
# 众所周知，北京大学的燕南食堂和农园食堂是离教学楼区最近的食堂。热爱学习的艾雪西同学为了不把学习时间浪费在吃饭上面（这是不正确的！一定要好好吃饭！），总会选择在这两个食堂吃饭。现在是中午十二点半，小艾结束了在二教的自习准备去食堂吃饭。他分别知道这两个食堂还有哪些菜品以及有多少份，现在他希望你帮助他把两个食堂的信息合并起来，统计出两个食堂总共还有哪些菜品以及总共有多少份。希望帮助他好好吃饭的你一定能完成这个任务吧！

# 题目要求：输入两个食堂分别拥有的菜品和份数，输出总共拥有的菜品及份数，按照份数从多到少排序。当两个食堂都有某菜品时，总共拥有该菜品的份数为两个食堂该菜品份数总和；如果仅有一个食堂有该菜品，则总共拥有该菜品的份数为该食堂拥有该菜品的份数。

# 输入数据保证不会有剩余总份数相同的菜品，菜品名称中保证不含有空格，菜品份数均为整数。对于同一个食堂的输入，每个菜品仅会出现一次（但两个食堂可能会有一样的菜品）

# 输入
# 第一行两个整数n和m，分别表示燕南食堂和农园食堂拥有的菜品种类数
# 接下来n行表示燕南食堂信息，每行为空格分隔的一个菜品名称和它的份数；
# 再接下来m行表示农园食堂信息，每行为空格分隔的一个菜品名称和它的份数；
# 输出
# 第一行一个整数k，表示两个食堂总共还有多少种菜品
# 接下来k行，每行为空格分隔的一个菜品名称和它的总份数；按照份数从大到小的顺序输出
# 样例输入
# 3 5
# chaobaicai 78
# tudousi 56
# paigutang 34
# banmian 13
# paigutang 18
# tudousi 5
# shouzhuabing 108
# mutongfan 72
# 样例输出
# 6
# shouzhuabing 108
# chaobaicai 78
# mutongfan 72
# tudousi 61
# paigutang 52
# banmian 13

n,m=input().split()
n=int(n)
m=int(m)
dishes={}
for i in range(n+m):
    name,num=input().split()
    num=int(num)
    if name in dishes:
        dishes[name]+=num
    else:
        dishes[name]=num

sorted_dishes = sorted(dishes.items(), key=lambda x: (-x[1], x[0]))

print(len(sorted_dishes))
for name, num in sorted_dishes:
    print(f"{name} {num}")

