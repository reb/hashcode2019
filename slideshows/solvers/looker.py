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
                'tags': set(photo['tags'])
            })
        else:
            verticals.append(photo)
    for photo_a, photo_b in pairwise(verticals):
        slides.append({
            'photos': [photo_a['index'], photo_b['index']],
            'tags': set(photo_a['tags'] + photo_b['tags'])
        })

    tags = defaultdict(set)

    for index, slide in enumerate(slides):
        slide['index'] = index
        for tag in slide['tags']:
            tags[tag].add(index)

    available_slides = [slide['index'] for slide in slides]

    first_slide = slides.pop()
    tags = remove_from_tags(first_slide, tags)
    available_slides.remove(first_slide['index'])
    slideshow = [first_slide]
    logger.debug(first_slide)

    while available_slides:
        logger.info('slideshow length: %s', len(slideshow))
        current_slide = slideshow[-1]
        next_slide_index = find_next_slide(current_slide, tags)
        if next_slide_index is not None:
            available_slides.remove(next_slide_index)
            next_slide = slides[next_slide_index]
            logger.debug(next_slide)
            tags = remove_from_tags(next_slide, tags)
            slideshow.append(next_slide)
            continue
        break

    return [slide['photos'] for slide in slideshow]

def find_next_slide(slide, tags):
    for tag in slide['tags']:
        if tags[tag]:
            logger.debug('matching on %s', tag)
            return next(iter(tags[tag]))
    return None

def remove_from_tags(slide, tags):
    for tag in slide['tags']:
        tags[tag].remove(slide['index'])
    return tags