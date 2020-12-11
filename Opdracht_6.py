import keyword


def contains_keyword(*args):
    final_result = False
    for s in args:
        if keyword.iskeyword(s):
            final_result = True
    return final_result


print (contains_keyword('hello', 'goodbye'))
print(contains_keyword('def', 'haha', 'lol', 'chikens', 42))
print(contains_keyword('four', 'for', 'if'))
print(contains_keyword('blabla', 'crab', 'anchor', 'doggo'))
print(contains_keyword('grizzly', 'ignore', 'return'))
