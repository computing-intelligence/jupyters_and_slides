# Created by mqgao at 2018/9/30

import jieba; jieba.load_userdict('dict.txt')
from itertools import product


def need_closure(index, tokens, split):
    """if index is the last one or meets 2 continuous chars, need close the parenthesis"""
    return (index == len(tokens) - 1) or is_continuous_2_char(index, tokens, split)


def is_continuous_2_char(index, tokens, split):
    return not (tokens[index] == split or tokens[index+1] == split)


def group(tokens, split='/'):
    """split the tokens with parenthesis, which make closures of same group candidates"""

    with_parenthesis, tmp = [], []

    for i, t in enumerate(tokens):
        if t == split: continue
        tmp.append(t)
        if need_closure(i, tokens, split):
            with_parenthesis.append(tmp); tmp = []

    return with_parenthesis


if __name__ == '__main__':
    sentences = """
    如何办理贵宾卡/金卡/特惠卡?
    如何办理贵宾卡/金卡/特惠卡
    网银/信用卡如何/怎样注销/开户啊/呀!
    网银/信用卡如何/怎样注销/开户
    """.split('\n')

    for s in sentences:
        s = s.strip()

        if not s: continue

        print('*'*8 + s)
        combinations = list(group(list(jieba.cut(s))))
        print('combination result is : {}'.format(combinations))

        for words in product(*combinations):
            print(''.join(words))
