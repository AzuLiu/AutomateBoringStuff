import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)
logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s)' % n)
    total = 1
    for i in range(n):
        total *= i
        logging.debug('i is ' + str(i) + 'total is ' + str(total))
    logging.debug('End of factorial(%s)' % n)
    return total
print(factorial(5))
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error occurred.')
logging.critical('The program is unable to recover!')
l =[1,2,3]
logging.debug(l)

