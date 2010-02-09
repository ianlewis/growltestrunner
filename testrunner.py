#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
import unittest
from datetime import datetime

APP_NAME = "Growl Text Test Runner"

class BaseTestRunner(unittest.TextTestRunner):
    """Text test runner with growl
    Need to installed growlnotiry.

    USAGE: pyautotest -r growltestrunner.GrowlTestRunner
    """
    def __init__(self, *args, **kwargs):
        self.stikey = False
        super(BaseTestRunner, self).__init__(*args, **kwargs)
        
    def run(self, test):
        "Run the given test case or test suite."
        result = self._makeResult()
        startTime = time.time()
        test(result)
        stopTime = time.time()
        timeTaken = stopTime - startTime
        result.printErrors()
        self.stream.writeln(result.separator2)
        run = result.testsRun
        result_line = "Ran %d test%s in %.3fs" %\
            (run, run != 1 and "s" or "", timeTaken)
        self.stream.writeln(result_line)
        self.stream.writeln()

        message = ""
        sticky = False
        if not result.wasSuccessful():
            title = "Tests Failed"
            icon = "icon_fail.png"
            priority = 2
            sticky = True
            o = ["FAILED ("]
            failed, errored = map(len, (result.failures, result.errors))
            if failed:
                o.append("failures=%d" % failed)
            if errored:
                if failed: o.append(", ")
                o.append("errors=%d" % errored)
            o.append(")")
            self.stream.writeln("".join(o))
            message = "".join(o) + "\n"
        else:
            title = "Tests Passed"
            icon = "icon_ok.png"
            priority = -2
            self.stream.writeln("OK")
        self.notify(title, message + result_line, priority, icon, sticky)
        return result

    def notify(self, title, message, priority, icon, sticky=False):
        pass
try:
    import pynotify
    pynotify.init(APP_NAME)
    
    class NotifyTestRunner(BaseTestRunner):
        """
        Notifications using pynotify
        """
        def notify(self, title, message, priority, icon, sticky=False):
            base_dir = os.path.abspath(os.path.dirname(__file__))
            n = pynotify.Notification(
                summary=title,
                message=message,
                icon=os.path.join(base_dir, icon),
            )

except ImportError:

    class NotifyTestRunner(BaseTestRunner):
        def notify(self, title, message, priority, icon, sticky=False):
            """
            Growl message via growlnotify
            """
            base_dir = os.path.abspath(os.path.dirname(__file__))
            fmt = 'growlnotify -n "%(app_name)s" -p %(priority)s '\
                '--image="%(icon_path)s" -m "%(message)s" "%(title)s" %(sticky)s'
            dic = {"app_name": APP_NAME,
                   "title": title,
                   "message": "%s\n%s" % (message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                   "priority": priority,
                   "icon_path": os.path.join(base_dir, icon),
                   "sticky": "-s" if sticky else ""
                   }
            os.system(fmt % dic)
