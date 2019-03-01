import logging
from collections import defaultdict
from tqdm import tqdm
from solvers.general import value
from solvers import iterative


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

    logger.info("Creating tags dictionary")
    tags = create_tags(slides)

    available_slides = [slide['index'] for slide in slides]
    slideshow = []
    progress = tqdm(total=len(available_slides))

    while available_slides:
        try:
            current_slide = slideshow[-1]
            next_slide_index = find_next_slide(current_slide, tags, slides)
        except IndexError:
            next_slide_index = 0

        if next_slide_index is not None:
            available_slides.remove(next_slide_index)
            next_slide = slides[next_slide_index]
            logger.debug(next_slide)
            tags = remove_from_tags(next_slide, tags)
            slideshow.append(next_slide)
            progress.update(1)
            continue
        break
    progress.close()

    logger.info("Optimizing slideshow")
    iterative.optimize(slideshow)
    return [slide['photos'] for slide in slideshow]

def find_next_slide(slide, tags):
    for tag in slide['tags']:
        if tags[tag]:
            logger.debug('matching on %s', tag)
            return next(iter(tags[tag]))
    return None


def create_tags(slides):
    tags = defaultdict(set)
    for index, slide in enumerate(slides):
        slide['index'] = index
        for tag in slide['tags']:
            tags[tag].add(index)
    return tags


def remove_from_tags(slide, tags):
    for tag in slide['tags']:
        tags[tag].remove(slide['index'])
    return tags