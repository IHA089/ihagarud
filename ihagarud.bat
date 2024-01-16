@echo off
setlocal enabledelayedexpansion

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo This Command Prompt is running without administrator privileges. Please run with administrator privileges.
    exit /b 1
)

for /f "tokens=*" %%a in ('echo %systemdrive%\^| %SystemRoot%\System32\find.exe /i "C:"') do set "systemDrive=%%a"
set "PFP=!systemDrive!\Program Files"

set "NDN=ihaahi"
set "NDP=!PFP!\!NDN!"
if not exist "!NDP!" (
    mkdir "!NDP!"
)

set "NDN=ihaahi/helper"
set "NDP=!PFP!\!NDN!"
if not exist "!NDP!" (
    mkdir "!NDP!"
)

set "NDN=ihaahi/IHA089"
set "NDP=!PFP!\!NDN!"
if not exist "!NDP!" (
    mkdir "!NDP!"
)

set "inputString=!path!"
set "token="
set "j=0"
for /l %%i in (0,1,999) do (
    set "char=!inputString:~%%i,1!"
    if "!char!"==";" (
        if defined token (
            if "!token!"=="!NDP!" (
                set "j=1"
            )
            set "token="
        )
    ) else (
        set "token=!token!!char!"
    )
)

if !j! equ 1 (
    echo Alread in PATH Environment
) else (
    echo Adding in PATH Environment...
    set "NKN=ihaahi\IHA089"
    set "NDP=!PFP!\!NKN!"
    setx PATH "%PATH%;!NDP!" /M
) 

title IHA089:: WE ARE FEW BUT POWERFUL

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Downloading and installing Python...
    call :PYTHON_GET
)


set "kpath=ihaahi/run.py"
set "cpath=ihaahi/runner.py"
set "ppth=ihagarud.bat"
set "gpath=ihaahi/IHA089/ihagarud.bat"
echo import urllib.request > !PFP!\!kpath!
::change this link. set the runner.py link here
echo req=urllib.request.urlopen("https://raw.githubusercontent.com/IHA089/ihagarud/main/ihagarud.py") >> !PFP!\!kpath!
echo jt=open("!PFP!\!cpath!","w") >> !PFP!\!kpath!
echo jt.write(req.read()) >> !PFP!\!kpath!
echo jt.close() >> !PFP!\!kpath!
echo @echo off > !PFP!\!gpath!
echo setlocal enabledelayedexpansion >> !PFP!\!gpath!
echo for /f "tokens=*" %%%%a in ('echo %%systemdrive%%\^^^| %%SystemRoot%%\System32\find.exe /i "C:"') do set "systemDrive=%%%%a" >> !PFP!\!gpath!
echo set "PFP=^!systemDrive^!\Program Files\ihaahi\runner.py" >> !PFP!\!gpath!
echo if "%%1" == "about" ( >> !PFP!\!gpath!
echo     python "^!PFP^!" about >> !PFP!\!gpath!
echo ) else if "%%1" == "help" ( >> !PFP!\!gpath!
echo    python "^!PFP^!" help >> !PFP!\!gpath!
echo ) else if "%%1" == "install" ( >> !PFP!\!gpath!
echo    python "^!PFP^!" install "%%2" >> !PFP!\!gpath!
echo ) else if "%%1" == "tools" ( >> !PFP!\!gpath!
echo    python "^!PFP^!" tools >> !PFP!\!gpath!
echo ) else if "%%1" == "toollist" ( >> !PFP!\!gpath!
echo    python "^!PFP^!" toollist >> !PFP!\!gpath!
echo ) else if "%%1" == "update" ( >> !PFP!\!gpath!
echo    python "^!PFP^!" update "%%2" >> !PFP!\!gpath!
echo ) else if "%%1" == "uninstall" ( >> !PFP!\!gpath!
echo    python "^!PFP^!" uninstall "%%2" >> !PFP!\!gpath!
echo ) else if "%%1" == "version" ( >> !PFP!\!gpath!
echo    python "^!PFP^!" version "%%2" >> !PFP!\!gpath!
echo ) else ( >> !PFP!\!gpath!
echo    python "^!PFP^!" >> !PFP!\!gpath!
echo ) >> !PFP!\!gpath!
echo endlocal >> !PFP!\!gpath!

python "!PFP!\!kpath!"
refreshenv
echo "type `ihagarud` any where in command prompt."

goto :EOF

:PYTHON_GET
echo $url = "https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe" > download.ps1
echo $output = "python_installer.exe" >> download.ps1
echo Invoke-WebRequest -Uri $url -OutFile $output >> download.ps1
echo Downloading Python 3.9...
powershell -ExecutionPolicy Bypass -File download.ps1
echo Installing Python 3.9...
start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 AddToPath=1 Include_pip=1
del python_installer.exe
del download.ps1
echo Python 3.9 is installed successfully. Open a new cmd and type python --version
refreshenv
goto :EOF


endlocal
