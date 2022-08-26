"""
default Json Logger Iso8601 Date Time Config 
"""

import os 

defaultJLIDTConfig = {
    "version": 1,
    ## "incremental": False,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "%(levelname)s -- %(message)s -- from logger: %(name)s "
        },
        "jsonFile": {
            "()": "jsonloggeriso8601datetime.CustomJsonFormatter",
            "format": "%(timestamp)s %(module)s %(name)s %(levelname)s %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            ## "level": "DEBUG",
            "level": os.getenv('JLIDT_CONSOLE_LEVEL', 'INFO'),
            "formatter": "console",
            "stream": "ext://sys.stdout"
        },
        "jsonFile": {
            ## "class": "logging.FileHandler",
            "()": "jsonloggeriso8601datetime.MakedirFileHandler",
            ## "level": "DEBUG",
            "level": os.getenv('JLIDT_JSONFILE_LEVEL', 'INFO'),
            "formatter": "jsonFile",
            "filename": "./logs/jsonLogs.log",
            "encoding": "utf8"
        }
    },
    "loggers": {
        "gunicorn": {
            "level": "INFO",
            "propagate": False,
            "handlers": ["console", "jsonFile"],
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "jsonFile"]
    }
}

## end of file 