import logging
from worker import app

# LOG = logging.getLogger('app')

@app.task
def add(x, y):
    LOG.debug('this is task add')
    return x + y
