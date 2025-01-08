import sys
from datetime import datetime

task = sys.argv[1:]
def todo():
    pass

def keep_alive():
    pass

def pomodoro():
    pass

if "todo" in task:
    todo()

if "ka" in task:
    keep_alive()

if "study" in task:
    pomodoro()
