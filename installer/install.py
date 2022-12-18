import os
import stat
import sys
import winreg

import admin

ON_WINDOWS = os.name == "nt"

HOME_DIR = os.path.expanduser("~")
BIN_DIR = os.path.abspath("/Program Files/molt") if ON_WINDOWS else os.path.join(HOME_DIR, "bin")
EXECUTABLE_FILE = os.path.join(BIN_DIR, "molt")

def install(bundled_system):
    ensure_windows_admin()
    add_bin_to_PATH()
        
    
    write_executable(EXECUTABLE_FILE, bundled_system)
    
    if ON_WINDOWS:
        write_executable(os.path.join(BIN_DIR, "molt.cmd"), make_bat_for(sys.executable, EXECUTABLE_FILE))


def make_bat_for(interpreter, file):
    return ("@echo off\n" +
            f'"{interpreter}" "{file}" %*')

def write_executable(file, content):
    make_folder_if_not_exist(os.path.dirname(file))
    with open(file, 'w') as install_handle:
        install_handle.write(content)
        make_executable(file)
        
def make_folder_if_not_exist(folder):
    os.makedirs(folder, exist_ok=True)

def ensure_windows_admin():
    if not admin.isUserAdmin():
        admin.runAsAdmin()

def make_executable(file):
    os.chmod(file, os.stat(file).st_mode | stat.S_IEXEC)

def add_bin_to_PATH():
    if ON_WINDOWS:
        add_windows_bin_to_PATH()
    else:
        for prof in ".profile", ".bashrc", ".zshrc":
            prof_file = os.path.join(HOME_DIR, prof)
            cmd = f"export PATH=$PATH:f{BIN_DIR}"
            os.system(cmd)
            with open(prof_file, 'a') as prof_handle:
                prof_handle.write("\n" + cmd)
        
def add_windows_bin_to_PATH():
    with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Control\Session Manager\Environment", access=winreg.KEY_ALL_ACCESS) as key:
        path = winreg.QueryValueEx(key, "Path")[0]
        bindir_term = BIN_DIR + ";"
        
        if bindir_term not in path:
            winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, bindir_term + path)