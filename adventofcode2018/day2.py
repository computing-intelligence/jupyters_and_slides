# Created by mqgao at 2018/12/11

from collections import Counter


def contains_counts(string, n):
    return n in Counter(string).values()


def get_checksum(strings):
    two_times = sum(1 for s in strings if contains_counts(s, 2))
    three_times = sum(1 for s in strings if contains_counts(s, 3))

    return two_times * three_times


def is_differ_one(string1, string2):
    contains_two_num = sum(1 for i in range(len(string1)) if contains_counts(string1[i]+string2[i], 2))

    return contains_two_num == len(string1) - 1


def get_only_one_differ(strings):

    string1, string2 = None, None

    for i, s1 in enumerate(strings):
        for j, s2 in enumerate(strings):
            if is_differ_one(s1, s2):
                string1, string2 = s1, s2
                break

    return ''.join(c for i, c in enumerate(string1) if string1[i] == string2[i])


assert contains_counts('abcdef', 2) == False
assert contains_counts('bababc', 2) == True
assert contains_counts('bababc', 3) == True

strings_original = """
abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.
"""

strings = [s.split()[0] for s in strings_original.split('\n') if s]

assert get_checksum(strings) == 12

strings = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz""".split('\n')

assert is_differ_one('abcde', 'axcye') is False
assert is_differ_one('fghij', 'fguij') is True

assert get_only_one_differ(strings) == 'fgij'


if __name__ == '__main__':
    strings = [line.strip() for line in open('data/input-day2.txt')]
    print(get_checksum(strings))
    print(get_only_one_differ(strings))
