def remove_mark(s):
    return ''.join([t for t in s if t.isalpha()])

def begin_duplicate(tokens):
    for f in range(1, len(tokens)):
        if tokens[:f] == tokens[f:2*f]: return f
    return None

def distinct(tokens):
    if not tokens: return ''
    
    duplicate = begin_duplicate(tokens)
    
    if duplicate:
        return distinct(tokens[duplicate:])
    else:
        return tokens[0]+ distinct(tokens[1:])



sentence1 = '这个橘子真的真的好好吃哦'
sentence2 = '你到底知不知道,到底知不知道？'
sentence3 = '这个饭馆是我吃过最好吃的饭馆，最好吃的饭馆！'
sentence4 = '你是真的不知道，真的不知道？还是假的不知道'
sentence5 = '你你你你要气死我了，你真是不可理喻'

assert distinct(remove_mark(sentence1)) == '这个橘子真的好吃哦'
assert distinct(remove_mark(sentence2)) == '你到底知不知道'
assert distinct(remove_mark(sentence3)) == '这个饭馆是我吃过最好吃的饭馆'
assert distinct(remove_mark(sentence4)) == '你是真的不知道还是假的不知道'
assert distinct(remove_mark(sentence5)) == '你要气死我了你真是不可理喻'
