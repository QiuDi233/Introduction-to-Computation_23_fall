# 3:字符串加密
# 查看提交统计提问
# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 现要对一个由大写字母组成的字符串进行加密，有两种加密方法
# (1)替换法：把一个字母替换成它之后的第k个字母，比如AXZ，k取2，加密后得到CZB(Z之后第二个字符为B)
# (2)置换法：改变原来字符串中字母的顺序，比如将顺序<2 3 1>应用到ABC上得到的密文为BCA。(顺序<2 3 1>指将原字符串的第2个字符作为新字符串的第1个字符，将原字符串的第3个字符作为新字符串的第2个字符，以此类推)

# 这两种方法单独使用都很容易被人破解，所以我们将两种方法联合使用，对一个字符串进行两次加密，比如AXZ在k=2和顺序<2 3 1>下加密得到ZBC。
# 输入
# 包含若干组数据，每组数据一行。一组数据由三部分组成：待加密的字符串(长度不超过30)、k、顺序。
# 输出
# 对于每组数据输出一行，为加密后的字符串.
# 样例输入
# AXZ 2 2 3 1
# VICTORIOUS 1 2 1 5 4 3 7 6 10 9 8
# 样例输出
# ZBC
# JWPUDJSTVP

# 读取输入数据
while True:
    try:
        data = input().split()
        if len(data) == 0:
            break

        # 解析输入数据
        string = data[0]
        k = int(data[1])
        order = list(map(int, data[2:]))

        # 替换法加密
        encrypted_string = ""
        for char in string:
            encrypted_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            encrypted_string += encrypted_char

        # 置换法加密
        final_string = ""
        for index in order:
            final_string += encrypted_string[index - 1]

        # 输出加密后的字符串
        print(final_string)

    except EOFError:
        break