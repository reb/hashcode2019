from itertools import product


def value(tags_a, tags_b):
    same = set()
    only_in_a = set()
    only_in_b = set()
    for tag_a, tag_b in product(tags_a, tags_b):
        if tag_a == tag_b:
            same.add(tag_a)
        only_in_a.add(tag_a)
        only_in_b.add(tag_b)
    return min(len(same), len(only_in_a), len(only_in_b))
