import os
import sys
import platform
import urllib.request

def find_program_files_directory():
    program_files_dir = os.path.join(os.environ.get('SystemDrive', 'C:'), 'Program Files')
    return program_files_dir

def is_admin():
    system_platform = platform.system()
    if system_platform == "Windows":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

def add_path_to_system_path(new_path):
    key_path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
    path_variable_name = 'Path'
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ) as reg_key:
        current_path, _ = winreg.QueryValueEx(reg_key, path_variable_name)
    if new_path not in current_path:
        new_path_variable = f'{new_path};{current_path}'
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE) as reg_key:
            winreg.SetValueEx(reg_key, path_variable_name, 0, winreg.REG_EXPAND_SZ, new_path_variable)

def creator(path):
   ffname = path+"\\"+"IHA089"+"\\"+"ihagarud.bat"
   ff = open(ffname, 'a')
   ff.write("@echo off\n") 
   ff.write("setlocal enabledelayedexpansion\n")
   ff.write("set \"PFP="+path+"\\ihagarud.py\"\n")
   ff.write("if \"%1\" == \"about\" (\n") 
   ff.write("python \"!PFP!\" about\n") 
   ff.write(") else if \"%1\" == \"help\" (\n") 
   ff.write("python \"!PFP!\" help\n") 
   ff.write(") else if \"%1\" == \"install\" (\n") 
   ff.write("python \"!PFP!\" install \"%2\"\n") 
   ff.write(") else if \"%1\" == \"tools\" (\n") 
   ff.write("python \"!PFP!\" tools\n") 
   ff.write(") else if \"%1\" == \"toollist\" (") 
   ff.write("python \"!PFP!\" toollist") 
   ff.write(") else if \"%1\" == \"update\" (\n") 
   ff.write("python \"!PFP!\" update \"%2\"\n") 
   ff.write(") else if \"%1\" == \"uninstall\" (\n") 
   ff.write("python \"!PFP!\" uninstall \"%2\"\n") 
   ff.write(") else if \"%1\" == \"version\" (\n") 
   ff.write("python \"!PFP!\" version \"%2\"\n") 
   ff.write(") else (\n")
   ff.write("python \"!PFP!\"\n") 
   ff.write(")\n") 
   ff.write("endlocal\n")
   ff.close()

def cloner(path):
    try:
        make_req = urllib.request.urlopen("https://raw.githubusercontent.com/IHA089/ihagarud/main/ihagarud.py")
        if make_req.status == 200:
            data = make_req.read()
            data = str(data, 'utf-8')
            ffname = path+"\\"+"ihagarud.py"
            ff = open(ffname, 'w')
            ff.write(data)
            ff.close()
        else:
            print("IHA089:::Server Down")
    except:
        print("No Internet Connection")
        exit()



if __name__ == "__main__":
    if is_admin():
        program_files_dir = find_program_files_directory()
        program_files_dir = program_files_dir.replace("Program Files","")
        iha_dir = program_files_dir+"\\"+"ihaahi"
        os.mkdir(iha_dir)
        iha_dir_home = iha_dir+"\\"+"IHA089"
        os.mkdir(iha_dir_home)
        add_path_to_system_path(iha_dir)
        creator(iha_dir)
        cloner(iha_dir)
        iha_dir_help = iha_dir+"\\"+"helper"
        os.mkdir(iha_dir_help)
    else:
        print("This script is NOT running without administrator privileges. Please run it as an administrator.")
        sys.exit()
    
