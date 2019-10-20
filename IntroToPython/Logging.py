#python logging modules
# CAPS are constants
#First letter with CAPS are classes
# lowercase are methods
#pylint: disable = E1101 
import logging
import math

# print(dir(logging))
#Create and configure logger
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename='C:\\Users\\DASA004\\Documents\\KnowHow\\Python\\IntroToPython\\Lumberjack.log',
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()

#Test
logger.info('our SECOND message')
print(logger.level) #print the level of log

logger.debug('This is a harmless debug message.')
logger.info('Just some useful info.')
logger.warning('I am sorry, but i cant do that, Dave.')
logger.error('divide by zero.')
logger.critical('Internet is down!!!.')


def quadratic_formula(a, b, c):
    """Return the solutions to the equation axpower2+bx+c =0. """
    logger.info('quadratic_formula({0}, {1}, {2})'.format(a,b,c))
    # Compute the discriminant
    logger.debug('# Compute the discriminant')
    disc = b ** 2 - 4 * a * c

    #Compute the two roots
    logger.debug('#Compute the two roots')
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)

    #Return the roots
    logger.debug('#Return the roots')
    return (root1, root2)

roots = quadratic_formula(1, 0, 1)
print(roots)
