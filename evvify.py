#!/usr/bin/env python
# coding: utf-8

import time
from os import listdir
from os.path import *
from pync import Notifier


def watchFile(logg):
    logg.seek(0, 2)
    while True:
        line = logg.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == "__main__":
    home = expanduser("~")
    #eveLogPathPost = join('Documents', 'EVE', 'logs', 'Gamelogs')
    eveLogPathPost = join('Library', 'Preferences', 'EVE Online Preferences', 'p_drive', 'My Documents', 'EVE')
    eveLogs = join(home, eveLogPathPost)
    files = sorted([f for f in listdir(eveLogs)])
    newest = files[-1]
    rdyLog = join(eveLogs, newest)
    logfile = open(rdyLog)
    loglines = watchFile(logfile)
    for line in loglines:
        try:
            message = line
            Notifier.notify(message)
        except (KeyboardInterrupt, SystemExit):
            logfile.close()
            Notifier.remove(os.getpid())
            exit()
            raise
        except:
            logfile.close()
            Notifier.remove(os.getpid())
            exit()
        else:
            pass
logfile.close()
Notifier.remove(os.getpid())
