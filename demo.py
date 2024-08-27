'''
鸡兔同笼问题
头:35    脚:94

问:鸡和兔,各有多少只
'''


def func_1(head, foot):
    for i in range(head + 1):
        j = head - i
        if 4 * i + 2 * j == foot:
            print(f'兔子有{i}只,鸡{j}只')


'''
羊毛问题:
共有70头羊,共剪下了106kg羊毛
大羊每只能剪1.6kg
小羊每只能剪1.2kg
问:大羊和小羊各多少只
'''

'''
用 1 2 3 4 组成一个三位数
有多少种可能
列出所有的三位数
'''
def func_2():
    for i in range(1,5):
        for j in range(1,5):

