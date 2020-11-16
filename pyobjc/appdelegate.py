# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#    PageBot application.
#    Copyright (c) 2016+ Type Network
#
#
# -----------------------------------------------------------------------------
#
#    appdelegate.py
#

import objc
from AppKit import NSObject
from PyObjCTools import AppHelper

class AppDelegate(NSObject):
    u"""Delegate for the application."""

    @objc.IBAction
    def applicationDidFinishLaunching_(self, notification):
        u"""
        """
        print('starting')

    def applicationShouldTerminate_(self, sender):
        print('closing')

AppHelper.runEventLoop()
