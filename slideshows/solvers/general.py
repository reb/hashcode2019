def value(tags_a, tags_b):
    intersect_length = len(set(tags_a).intersection(tags_b))
    only_in_a = len(tags_a) - intersect_length
    only_in_b = len(tags_b) - intersect_length
    return min(intersect_length, only_in_a, only_in_b)
