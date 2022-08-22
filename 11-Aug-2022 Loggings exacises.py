# 1).LoggingToPrompt 

##from logging import *
####debug("This is Debug")
####info("This is Info")
##warning("This is Warning")
##error("This is Error")
##critical("This is Critical")

#2). LogginToFile

##from logging import *
##basicConfig(filename='log1.log')
##warning("this is warning")
##error("this is error")
##critical("this is critical")


#3).3. ChangeLevel

##from logging import *
##basicConfig(filename='log2', level=DEBUG)
##debug("this is debug")
##warning("this is warning")
##error("this is error")
##critical("this is critical")

#4). ChangeFileMode

##from logging import *
##basicConfig(filename='log1.log',level=DEBUG,filemode='w')
##debug("this is debug")
##info("this is information")
##warning("this is warning")
##error("this is error")
##critical("this is critical")

#5). FormatLogData1

##from logging import *
##basicConfig(filename='log1.log',level=INFO,filemode='w',format='%(asctime)s ** %(message)s')
##debug("this is debug")
##info("this is info")
##warning("this is warning")
##error("this is error")
##critical("this is critical")


#6). FormatLogData2

##from logging import *
##log='%(asctime)s --//%(message)s //%(lineno)d'
##basicConfig(filename='log1.log',level=DEBUG,filemode='w',format=log)
##debug("tjis is debug")
##info("this is information")
##warning("this is warning")
##error("this is error")
##critical("this is critical ")


#7).ChangeFormatStyle

##from logging import*
##log='{message}@@{lineno}##{asctime}'
##basicConfig(filename='log1.log',level=INFO,filemode='w',style='{',format=log)
##debug("this is debug")
##info("this is info")
##warning("this is warning")
##error("this is error")
##critical("this is critical")


#8).getLogger

##from logging import *
##log='{lineno}--{name}--{asctime}--{message}'
##basicConfig(filename='log1.log',level=DEBUG,filemode='w',style='{',format=log)
##loge=getLogger('ojas')
##loge.debug("this is debug")
##loge.info("this is information")
##loge.warning("this is warning")
##loge.critical("this is critical")





##import logging
##logging.basicConfig(filename='employee.log',
##                     level=logging.INFO,
##                     format='%(lineno)s::%(asctime)s::%(levelname)s::%(message)s::%(name)s')
##logger = logging.getLogger('swetha')
##def validation(fun):
##    logger.info('Entered validation function')
##    def fun(user_input):
##        logger.info('Before Checking in Data')
##        data=['swetha']
##        if user_input in data:
##            logger.info('username present in database')
##            return 'welcome '+user_input
##        else:
##            logger.debug('username Not present in database')
##            return 'wrong user'
##    return fun
##@validation
##def login_user(user_input):
##    return user_input
##user_input=input("Enter UserName: ")
##logger.info('User Input given')
##print(login_user(user_input))


