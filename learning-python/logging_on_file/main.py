import logging

# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logging.getLogger().setLevel(logging.INFO)

# logging.info('Hello World')
# logging.debug('Hello World debug')
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)

fh = logging.FileHandler(filename='../example.log', encoding='utf-8')
fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(fh)
logger.info('Hello')

