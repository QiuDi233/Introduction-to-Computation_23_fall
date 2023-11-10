# 04:推免工作

# 总时间限制: 1000ms 内存限制: 65535kB
# 描述
# 一年一度的保研时间又到了，XX大学XX学院即将准备推免工作。为简化问题，我们假设该学院仅按照平均绩点来进行排名，不考虑挂科，综测排名等各种因素。

# 推免优先级按照学生的平均绩点来决定，平均绩点更高的同学比平均绩点更低的同学更优先获得推免资格。(输入数据保证同学绩点均不相同，无需考虑绩点相同的情况）

# 当某门课的得分低于60分时，该门课程绩点为0，当得分score满足60<=score<=100时，分数和绩点的转换公式如下：

# gpa=4-3*(100-score)**2/1600

# 每门课程的绩点按照  该课程的学分/总学分  的权重进行加权平均，得到平均绩点。

# 例如，一个同学修过三门课，三门课绩点分别是2.0,3.0,4.0 ； 三门课学分分别是2，3，3 ; 则该学生所修总学分为2+3+3=8，则三门课对应的权重分别为2/8, 3/8, 3/8
# 该同学平均绩点为：2.0*(2/8)+3.0*(3/8)+4.0*(3/8)=3.125

# 输入
# 第一行输入两个整数N和M，并用空格隔开，表示总共有N个同学，M个推免资格
# 下面是N行，每行表示一个学生的信息（保证一个同学的信息仅出现1次，不会重复出现）：
# 第1个数据表示该学生的学号，后面的数据两两一组，表示该学生所修某门课程的得分和该课程的学分，学分一定是整数，得分可能带有小数。数据间用空格隔开。
# 例如"2201111002 78 5 80 2"表示学号为2201111002的同学选修过2门课，第一门5学分得分78，第二门2学分得分80
# 输出
# 输出共一行，输出所有获得推免同学的学号，中间用空格隔开（按照平均绩点高的在前的顺序输出，输入数据保证不存在绩点相同的同学）
# 样例输入
# 5 3
# 2201111000 80 5 78 3 95 2
# 2201111001 59 2 67 3 60 4 57 2
# 2201111002 78 5 80 2
# 2201111003 60 2 100 5
# 2201111004 78 4 84 2
# 样例输出
# 2201111000 2201111004 2201111003

def score_to_gpa(score):
  if score < 60:
    return 0
  else:
    return 4 - 3 * (100 - score) ** 2 / 1600

def average_gpa(scores, credits):
  total_gpa = 0
  total_credit = 0
  for i in range(len(scores)):
    total_gpa += score_to_gpa(scores[i]) * credits[i]
    total_credit += credits[i]
  return total_gpa / total_credit

N, M = map(int, input().split())
students = []
for i in range(N):
  data = input().split()
  student_id = data[0]
  scores = list(map(float, data[1::2]))
  credits = list(map(int, data[2::2]))
  gpa = average_gpa(scores, credits)
  students.append((student_id, gpa))

students.sort(key=lambda x: x[1], reverse=True)

for i in range(M):
  print(students[i][0], end=" ")
print()