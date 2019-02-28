import logging

logger = logging.getLogger('solver/basic.py')


def solve(problem):
    for photo in problem['photos']:
        if photo['orientation'] == 'H':
            return [[photo['index']]]
