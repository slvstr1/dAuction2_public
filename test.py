import os.path
import logging
log = logging.getLogger(__name__)
pname = "instructions/templates/instructions/pages"
for name in os.listdir(pname):
    # print("test-name", name)
    log_string = "test-name" + str( name)
    log.info(log_string)