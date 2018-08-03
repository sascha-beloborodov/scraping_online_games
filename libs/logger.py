
import os
from datetime import datetime
import logging
logging.basicConfig(filename=os.getcwd()+'/logs/'+datetime.today().strftime('%Y%m%d')+'.log',level=logging.DEBUG)

def log_error(e):
    logging.warning(e)