import logging
from solvers.general import value


logger = logging.getLogger('solvers/iterative.py')


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def solve(problem):
    slideshow = []
    verticals = []
    for photo in problem['photos']:
        if photo['orientation'] == 'H':
            slideshow.append({
                'photos': [photo['index']],
                'tags': sorted(photo['tags'])
            })
        else:
            verticals.append(photo)
    for photo_a, photo_b in pairwise(verticals):
        slideshow.append({
            'photos': [photo_a['index'], photo_b['index']],
            'tags': sorted(photo_a['tags'] + photo_b['tags'])
        })

    optimize(slideshow)
    return [slide['photos'] for slide in slideshow]


def optimize(slideshow):
    changes = True
    while changes:
        changes = False
        for i in range(1, len(slideshow)):
            if should_swap(slideshow, i):
                slideshow[i-1], slideshow[i] = slideshow[i], slideshow[i-1]
                changes = True


def should_swap(slideshow, i):
    start = i - 2
    if start < 0:
        start = 0
    end = i + 2
    if end >= len(slideshow):
        end = len(slideshow)

    frame = slideshow[start:end]
    unswapped = frame_value(frame)

    frame[i-1 - start], frame[i - start] = frame[i - start], frame[i-1 - start]

    swapped = frame_value(frame)

    logger.debug('Unswapped value: %s, swapped value: %s', unswapped, swapped)
    return swapped > unswapped


def frame_value(frame):
    total = 0
    for i in range(len(frame) - 1):
        total += value(frame[i]['tags'], frame[i+1]['tags'])
    return total








