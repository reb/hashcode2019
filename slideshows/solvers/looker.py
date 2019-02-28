import logging
from collections import defaultdict
from solvers.general import value


logger = logging.getLogger('solvers/looker.py')


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def solve(problem):
    slides = []
    verticals = []
    for photo in problem['photos']:
        if photo['orientation'] == 'H':
            slides.append({
                'photos': [photo['index']],
                'tags': sorted(photo['tags'])
            })
        else:
            verticals.append(photo)
    for photo_a, photo_b in pairwise(verticals):
        slides.append({
            'photos': [photo_a['index'], photo_b['index']],
            'tags': sorted(photo_a['tags'] + photo_b['tags'])
        })

    tags = defaultdict(list)

    for slide in slides:
        for tag in slide['tags']:
            tags[tag].append(slide)

    first_slide = slides.pop()
    tags = remove_from_tags(first_slide, tags)
    slideshow = [first_slide]

    while slides:
        logger.debug('slideshow length: %s', len(slideshow))
        current_slide = slideshow[-1]
        next_slide = find_next_slide(current_slide, tags)
        if next_slide:
            slides.remove(next_slide)
            tags = remove_from_tags(next_slide, tags)
            slideshow.append(next_slide)
            continue
        break

    return [slide['photos'] for slide in slideshow]

def find_next_slide(slide, tags):
    for tag in slide['tags']:
        if tags[tag]:
            return tags[tag][0]
    return False

def remove_from_tags(slide, tags):
    for tag in slide['tags']:
        tags[tag].remove(slide)
    return tags