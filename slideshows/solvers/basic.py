import logging

logger = logging.getLogger('solver/basic.py')


def solve(problem):
    logger.debug('%s', problem)
    logger.info('Not actually solving anything')
    logger.debug('Or debugging')
    return problem
