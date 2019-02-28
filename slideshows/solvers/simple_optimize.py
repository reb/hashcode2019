import logging
from solvers.general import value


logger = logging.getLogger('solvers/simple_optimize.py')


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

    slideshow = [slides.pop()]



    while slides:
        logger.debug(len(slides))
        best_next = {
            'value': 0,
            'slide': None
        }
        current_slide = slideshow[-1]
        for slide in slides:
            slide_value = value(slide['tags'], current_slide['tags'])
            if slide_value >= best_next['value']:
                best_next = {
                    'value': slide_value,
                    'slide': slide
                }

        slideshow.append(best_next['slide'])
        slides.remove(best_next['slide'])

    return [slide['photos'] for slide in slideshow]

