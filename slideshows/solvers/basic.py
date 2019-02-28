import logging

logger = logging.getLogger('solver/basic.py')

def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

def solve(problem):
    slideshow = []
    verticals = []
    for photo in problem['photos']:
        if photo['orientation'] == 'H':
            slideshow.append([photo['index']])
        else:
            verticals.append(photo['index'])
    for photo_a, photo_b in pairwise(verticals):
        slideshow.append([photo_a, photo_b])
    return slideshow
