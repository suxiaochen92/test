# a=input('请输入需要计算的数字：')
# print('共计：',len(a))

# 字符统计--不包括空格
a=input('请输入需要计算的内容：')
# b=a.count(' ')
# print('字数合计：',{m},'字。').format(m=len(a)-b)
b=0
for i in a:
    if i==' ':
        b+=1
print(len(a)-b)

# a=(1,2,3,'qwe','你好')
# b=a.count(1)
# c=a.index('qwe')
# print(b,c)

# q=[1,2,55,11,66,33,22,14,21]
# q[1]=93
# print(q)
# print(93 in q)
# q.append('append插入')
# print(q)
# q.insert(0,'insert插入')
# print(q)
# q.extend(['55','11','22'])
# print(q)
# w=q.pop(3)
# print(w)
# q.reverse()
# q.sort()
# q.sort(reverse=True)
# print(q)

# 冒泡排序
q=[1,2,55,11,66,33,22,14,21]
print(len(q))
for i in range(len(q)-1):  # 这个循环负责设置冒泡排序进行的次数（比如说n个数，则只要进行n-1次冒泡，就可以把这个n个数排序好，对吧）
    # 9-1=8
    # 0,1,2,3,4,5,6,7
    for j in range(len(q)-i-1): # 9-0-1=8,9-1-1=7,9-2-1=6,9-3-1=5,9-4-1=4,9-5-1=3,9-6-1=2,9-7-1=1
        if q[j]>q[j+1]:
            q[j],q[j+1]=q[j+1],q[j]
print(q)

# p={
#     'name':'张三',
#     'age':17,
#     'high':'175cm'
# }
# print(p['name'])

# a=p.get("list")
# print(a)

# 发送红包
m=input('请输入金额：')
a=m.count('.')
for i in m:
    if i not in '0123456789.':
        print('输入的内容不合法，请输入数字！')
        exit()
if a>=2:
    print('输入金额不合法，请重新输入！')
    quit()
elif '.' in m:    
    b=m.split('.')
    if len(b[1])>2:
        print('只允许保留两位小数，请重新输入！')
        exit()
if float(m)>0.01 and float(m)<200.00:
    print('红包发送成功，金额：{}'.format(float(m)))
else:
    print('金额不在发送范围，请重新输入!')

# 跳过和结束循环
for i in range(1,21):
    if i == 11:
        continue
    elif i==12:
        break
    else:
        print('a={e}'.format(e=i))

# 格式化美化打印
name=input('请输入你的姓名：')
age=input('请输入你的年龄：')
high=input('请输入你的身高(cm)：')
color=input('你的肤色是黑的吗？(y/n)：')

res='''
==========Personal Info==========
    姓名    :   {n}
    年龄    :   {a}
    身高    :   {h}
    肤色    :   {c}
===============END===============
'''.format(n=name,a=age,h=high,c=color)
print(res)

# 成绩匹配
fen=int(input('请输入需要查询的分数：'))
if fen>=90 and fen<=100:
    print('A')
elif fen>=80 and fen<=89:
    print('B')
elif fen>=60 and fen<=79:
    print('C')
elif fen>=40 and fen<=59:
    print('D')
else:
    print('E')

# 猜数字
import random
a=input('请输入数字(仅限整数):')
b=random.randint(1,50)
print(b)
for i in a:
    if i not in '0123456789':
        print('输入不合法，请重新输入！')
        exit()
c=int(a)
if c>b:
    print('猜大了')
elif c<b:
    print('猜小了')
else:
    print('恭喜您，猜对了！')

# 猜数字进阶--允许三次错误机会
import random
b=random.randint(1,20)
a=0
while a < 3:
    c=input('请输入猜的数字(只允许输入整数)：')
    for i in c:
        if i not in '0123456789':
            print('输入不合法，请重新输入!')
    d=int(c)
    if d > b:
        print('大了')
    elif d<b:
        print('小了')
    else:
        print('恭喜，猜对了')
        break
    a+=1
    if a==3:
        e=input('继续输入y，结束输入n：')
        if e=='y' or e=='Y':
            a=0
        elif e=='n' or e=='N':
            print('游戏结束，欢迎下次再来')
            break

# 双色球彩票
red=[]
blue=[]
while True:
    while True:
        red_one=input('[1]请选择第一个红色号码：')
        if int(red_one)>16 or int(red_one)<1:
            print('只能选择1-16之间的号码，请重新选择！')
            continue
        else:
            red.append(red_one)
            break
    while True:
        red_two=input('[2]请选择第二个红色号码：')
        if red_two in red:
            print('该号码已存在，请重新选择！')
            continue
        elif int(red_two)>16 or int(red_two)<1:
            print('只能选择1-16之间的号码，请重新选择！')
            continue
        else:
            red.append(red_two)
            break
    while True:
        red_three=input('[3]请选择第三个红色号码：')  
        if red_three in red:
            print('该号码已存在，请重新选择！')
            continue
        elif int(red_three)>16 or int(red_three)<1:
            print('只能选择1-16之间的号码，请重新选择！')
            continue
        else:
            red.append(red_three)
            break
    while True:
        red_four=input('[4]请选择第四个红色号码：')  
        if red_four in red:
            print('该号码已存在，请重新选择！')
            continue
        elif int(red_four)>16 or int(red_four)<1:
            print('只能选择1-16之间的号码，请重新选择！')
            continue
        else:
            red.append(red_four)
            break
    while True:
        red_five=input('[5]请选择第四个红色号码：')  
        if red_five in red:
            print('该号码已存在，请重新选择！')
            continue
        elif int(red_five)>16 or int(red_five)<1:
            print('只能选择1-16之间的号码，请重新选择！')
            continue
        else:
            red.append(red_five)
            break
    while True:
        red_six=input('[6]请选择第四个红色号码：')  
        if red_six in red:
            print('该号码已存在，请重新选择！')
            continue
        elif int(red_six)>16 or int(red_six)<1:
                print('只能选择1-16之间的号码，请重新选择！')
                continue
        else:
            red.append(red_six)
            break
    while True:
        blue_one=input('[1]请选择第一个蓝色号码：')  
        if blue_one in red:
            print('该号码已存在，请重新选择！')
            continue
        elif int(blue_one)>16 or int(blue_one)<1:
            print('只能选择1-16之间的号码，请重新选择！')
            continue
        else:
            blue.append(blue_one)
            break
    while True:
        blue_two=input('[2]请选择第二个蓝色号码：')  
        if blue_two==blue_one or blue_two in red:
            print('该号码已存在，请重新选择！')
            continue
        elif int(blue_two)>16 or int(blue_two)<1:
                print('只能选择1-16之间的号码，请重新选择！')
        else:
            blue.append(blue_two)
            break
    if len(blue)==2:
        break
print('====================================================')
print('红色号码为：    |',red)
print('蓝色号码为：    |',blue)
print('====================================================')
print('{res}个号码已选择完毕，请耐心等待开奖!'.format(res=len(red)+len(blue)))
print('====================================================')