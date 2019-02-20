__author__ = 'mqgao'
__date__  = '2019.Feb.17'

import random


human = """
human = 自己 寻找 活动
自己 = 我 | 俺 | 我们 
寻找 = 看看 | 找找 | 想找点
活动 = 乐子 | 玩的
"""


host = """
host = 寒暄 报数 询问 业务相关 结尾 
报数 = 我是 数字 号 ,
数字 = 单个数字 | 数字 单个数字 
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ,
人称 = 先生 | 女士 | 小朋友
打招呼 = 你好 | 您好 
询问 = 请问你要 | 您需要
业务相关 = 玩玩 具体业务
玩玩 = 耍一耍 | 玩一玩
具体业务 = 喝酒 | 打牌 | 打猎 | 赌博
结尾 = 吗？"""


ROOT = 'root'


def generate_grammer(grammer_define):

    grammer_pattern = {}
    default = None

    for line in grammer_define.split('\n'):
        if not line: continue
        key, rules = line.split('=')
        key = key.strip()
        default = default or key
        rules = rules.split('|')
        grammer_pattern[key] = rules
        grammer_pattern[key] = [r.split() for r in rules]

    grammer_pattern[ROOT] = grammer_pattern[default]

    return grammer_pattern


def generate(p, target=ROOT):
    if target not in p: return target
    
    sub_target = random.choice(p[target])
    return ''.join(generate(p, r) for r in sub_target)



if __name__ == '__main__':
    sample_num = 10
    
    while sample_num > 0:
        print(generate(generate_grammer(human)))
        print(generate(generate_grammer(host)))
        sample_num -= 1
