import logging
# logging.basicConfig(filename='ejemplo.log', encoding='utf-8', filemode='w', level=logging.INFO)
logging.root.setLevel(logging.ERROR)
logging.debug('Texto debug')
logging.info('Texto info')
logging.warning('Texto warning')
logging.error('Texto error')
logging.critical('Texto critical')



# [(print(level), print(getattr(logging, level))) for level in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']]
#
# logging.root.getEffectiveLevel() == logging.WARNING
# logging.root.setLevel(logging.INFO)
# logging.root.getEffectiveLevel() == logging.INFO
# logging.info('Now this should get logged.')
# logging.log(21, 'This will also get logged at a numbered custom level')
# logging.basicConfig(level=logging.DEBUG)
# logging.root.getEffectiveLevel() == logging.DEBUG
# exit()
#
# import logging
# logging.basicConfig(level=logging.INFO)
# logging.info('This is some information')
# logging.root.getEffectiveLevel() == logging.INFO
