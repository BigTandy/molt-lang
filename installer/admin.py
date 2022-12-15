#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

# (C) COPYRIGHT © Preston Landers 2010
# Released under the same license as Python 2.6.5


import ctypes
from ctypes import c_char_p, c_wchar_p
import sys
import os
import traceback
import types


def isUserAdmin():

    if os.name == 'nt':
        # WARNING: requires Windows XP SP2 or higher!
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            print("Admin check failed, assuming not an admin.")
            return False
    elif os.name == 'posix':
        # Check for root on Posix
        return os.getuid() == 0
    else:
        raise RuntimeError("Unsupported operating system for this module: %s" % (os.name,))


def runAsAdmin():

    if os.name != 'nt':
        raise RuntimeError("This function is only implemented on Windows.")

    
    
    ShellExecuteA = ctypes.windll.shell32.ShellExecuteA
    
    args = " ".join(f'"{p}"' for p in sys.argv)

    # https://learn.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-findexecutablea
    procInfo = ShellExecuteA(
                            None,                                    #hwnd
                            c_char_p(bytes("runas"       , "utf8")), #lpOperation
                            c_char_p(bytes(sys.executable, "utf8")), #lpFile
                            c_char_p(bytes(args          , "utf8")), #lpParameters
                            c_char_p(bytes(os.getcwd()   , "utf8")), #lpDirectory
                            1                                        #nShowCmd
                        )
                        
    if procInfo < 32:
        print("Error requesting admin access. Please manually 'Run as Administrator'.")
        sys.exit(1)

    sys.exit(0)
