import os
import sys
import ctypes
import shutil
import platform
import urllib.request

def is_admin():
    system_platform = platform.system()
    if system_platform == "Linux":
        user = os.getenv("SUDO_USER")
        if user is None:
            return False
        else:
            return True
    if system_platform == "Windows":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

def _d_controler(typ):
    cont=""
    if typ == "raw":
        cont="6J8b7x4O7O4i7c0V7J3i3GaU2OfU2yfD7F2w6G1g7N7I2Aey6m7D6l9G7d4u6I8b7q5X6E2a7H5f7m3j6T5J7Z2j6s3U6hfa6xeR7r4Y6x5R6EeR7r4G2Yef6y3Q6rfq6Cdd2hfE4v9R4w8p4k1x3i0W3K8h3x9k2nfC"
    else:
        cont="6g8T7E4Y7B4l7z0K7O3j3bad2Xfz2ifY6P7S6E9p7S4R6v8Y7J5W6F2Z2Nec6C3x6ofa6sdp2sfR4G9F4U8E4G1U3w0x3t8I3f9E2nfi"
    return cont


def manage_file(filepath, aim):
    if aim=="dirrem":
        if os.path.exists(filepath):
            shutil.rmtree(filepath)
    elif aim=="filrem":
        if os.path.exists(filepath):
            os.remove(filepath)

def _header(osci, red):
    if osci == "linux":
        print("{}IHA089: https://iha089.org.in".format(red))
        print("{}IHA089: Navigating the Digital Realm with Code and Security – Where Programming Insights Meet Cyber Vigilance.".format(red))
    elif osci == "window":
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0004)
        print("IHA089: https://iha089.org.in")
        print("IHA089: Navigating the Digital Realm with Code and Security – Where Programming Insights Meet Cyber Vigilance.")
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)


def _usage(osci, blue, white, red):
    _header(osci, red)
    if osci == "linux":
        print("{} Usage: `{}ihagarud help{}` for more information.".format(blue, white, blue))
    elif osci == "window":
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0004)
        print("Usage: `ihagarud help` for more information")
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)


def _real_getter(ENSTR):
    DESTR = ""
    for i in range(0, len(ENSTR), 2):
        DESTR += ENSTR[i]
    return bytes.fromhex(DESTR).decode()

def _networkconnection(red):
    try:
        urllib.request.urlopen("https://iha089.org.in")
    except:
        if osci == "linux":
            print("{}No Internet Connection".format(red))
        elif osci == "window":
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0004)
            print("No Internet Connection")
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)

def _about(osci, blue, red, white):
    if osci == "linux":
        print("{}IHA089: Navigating the Digital Realm with Code and Security – Where Programming Insights Meet Cyber Vigilance.".format(red))
        print("{}Create By            {}:::     {}IHA089".format(blue, red, white))
        print("{}Official Website     {}:::     {}https://iha089.org.in".format(blue, red, white))
        print("{}Telegram channel     {}:::     {}https://t.me/IHATron".format(blue, red, white))
        print("{}Telegram Group       {}:::     {}https://t.me/IHA089".format(blue, red, white))
    elif osci == "window":
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0004)
        print("IHA089: Navigating the Digital Realm with Code and Security – Where Programming Insights Meet Cyber Vigilance.")
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)

        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001)
        print("Create By            :::     IHA089")
        print("Official Website     :::     https://iha089.org.in")
        print("Telegram channel     :::     https://t.me/IHATron")
        print("Telegram Group       :::     https://t.me/IHA089")
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)




def _help(osci, red, blue, white):
        _header(osci, red)
        if osci == "linux":
            print("{}ihagarud about                    {}:>         {}About IHA089".format(blue,red,white))
            print("{}ihagarud help                     {}:>         {}Help".format(blue,red,white))
            print("{}ihagarud install <tool name>      {}:>         {}Installing new tool".format(blue,red,white))
            print("{}ihagarud tools                    {}:>         {}Print the list of all installed tool with version".format(blue,red,white))
            print("{}ihagarud toollist                 {}:>         {}Print the list of all tools that design by IHA089".format(blue,red,white))
            print("{}ihagarud update <tool name>       {}:>         {}Update tool in leatest version".format(blue,red,white))
            print("{}ihagarud uninstall <tool name>    {}:>         {}uninstalling a tool".format(blue,red,white))
            print("{}ihagarud version <tool name>      {}:>         {}Print the version of the tool".format(blue,red,white))
        elif osci == "window":
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001)
            print("ihagarud about                    :>         About IHA089")
            print("ihagarud help                     :>         Help")
            print("ihagarud install <tool name>      :>         Installing new tool")
            print("ihagarud tools                    :>         Print the list of all installed tool with version")
            print("ihagarud toollist                 :>         Print the list of all tools that design by IHA089")
            print("ihagarud update <tool name>       :>         Update tool in leatest version")
            print("ihagarud uninstall <tool name>    :>         uninstalling a tool")
            print("ihagarud version <tool name>      :>         Print the version of the tool")
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)

def _check_main_dict(main_path, dir_path, runner_path, osci):
    if os.path.exists(main_path):
        pass
    else:
        os.mkdir(main_path)
    
    helper_path = dir_path+"helper"
    if os.path.exists(helper_path):
        pass
    else:
        os.mkdir(helper_path)

    if osci == "window":
        if os.path.exists(runner_path):
            pass
        else:
            os.mkdir(runner_path)


def _toollist(red):
    _networkconnection(red)
    tool_list = "6pcH7H3N6XbM6Y4G6Eac6Z6V6gfL7u7o6N5I6Xar6m1E7p3b6Bck6Rbi6N6T6QaJ6cfq6y1u7L7O6w5T6A9Z6a6Z6Kav6Q1S6efi6e8u6v9T6t7J6A1D6Xfu6U9r7t7s6o5o6i6S6sao6afg6N1S6m9O7H7B6fae6r5B6P6u6ufX6C1e6K9n6Y8q6F5o6Qfs6v1k6d9h7l7Z6v5I6Dav6JfW6X6N6w1m6p9X6B8m6M7b6ofA6i1h6Z9X6H6F6pfq6g1r7a7o6j5Z6c9c6KaB6s6N6Bfv6j1Y6i9S6R8Y7r7I6a7R6GfX6q1g7r7g6v5R6w9c6vaN6c6C6I1H6KfH6g8x6z5x6j7g7Z7K2ifp6LdN6M1V6a9S6Cev2JfW6T3s6ofd6oei7p4c7R2q6Xfq6xcb6X5O7u2c2Tev7u4D7A8k7d4h"
    list_ul = _real_getter(_d_controler("raw"))+_real_getter(tool_list)
    

    
    try:
        make_req = urllib.request.urlopen(list_ul)
        if make_req.status == 200:
            text = make_req.read()
            text = str(text, 'utf-8')
            krk = text.split("\n")
            for lines in krk:
                if lines == "":
                    pass
                else:
                    gtkst = _real_getter(lines)
                    gtkst = gtkst.replace("window","")
                    gtkst = gtkst.replace("linux","")
                    gtkst = gtkst.replace("-","")
                    print(gtkst)
        else:
            print("IHA089 ::: Server Down")
    except urllib.error.URLError:
        if osci == "linux":
            print("{} No Internet Connection".format(red))
        elif osci == "window":
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001)
            print("No Internet Connection")
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)

def _check_support(toolname, red, osci):
    _networkconnection(red)
    tool_list = "6pcH7H3N6XbM6Y4G6Eac6Z6V6gfL7u7o6N5I6Xar6m1E7p3b6Bck6Rbi6N6T6QaJ6cfq6y1u7L7O6w5T6A9Z6a6Z6Kav6Q1S6efi6e8u6v9T6t7J6A1D6Xfu6U9r7t7s6o5o6i6S6sao6afg6N1S6m9O7H7B6fae6r5B6P6u6ufX6C1e6K9n6Y8q6F5o6Qfs6v1k6d9h7l7Z6v5I6Dav6JfW6X6N6w1m6p9X6B8m6M7b6ofA6i1h6Z9X6H6F6pfq6g1r7a7o6j5Z6c9c6KaB6s6N6Bfv6j1Y6i9S6R8Y7r7I6a7R6GfX6q1g7r7g6v5R6w9c6vaN6c6C6I1H6KfH6g8x6z5x6j7g7Z7K2ifp6LdN6M1V6a9S6Cev2JfW6T3s6ofd6oei7p4c7R2q6Xfq6xcb6X5O7u2c2Tev7u4D7A8k7d4h"
    list_ul = _real_getter(_d_controler("raw"))+_real_getter(tool_list)
    try:
        make_req = urllib.request.urlopen(list_ul)
        if make_req.status == 200:
            text = make_req.read()
            text = str(text, 'utf-8')
            krk = text.split("\n")
            epic=0
            for lines in krk:
                if lines == "":
                    pass
                else:
                    gtkst = _real_getter(lines)
                    if toolname in gtkst:
                        epic=1
                        if osci in gtkst:
                            pass
                        else:
                            print(toolname+" is not avilable for "+osci)
                            sys.exit(0)
                    else:
                        epic=0

            if epic==0:
                print("No tool found : "+toolname)
                sys.exit(0)
        else:
            print("IHA089 ::: Server Down")
    except urllib.error.URLError:
        if osci == "linux":
            print("{} No Internet Connection".format(red))
        elif osci == "window":
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001)
            print("No Internet Connection")
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)
        sys.exit(0)

def _all_tool(main_path, dir_path):
    entries = os.listdir(main_path)
    if len(entries) == 0:
        print("No installed tool")
    else:
        for dire in entries:
            dire_path = os.path.join(main_path, dire)
            if os.path.isdir(dire_path):
                if dire == "helper":
                    pass
                elif dire == "IHA089":
                    pass
                else:
                    print(dire, end="")
                    print("\t\t\t", end="")
                    npt = dir_path+dire+"/"+dire+"-main/.version"
                    version = ""
                    try:
                        f_open = open(npt, 'r')
                        cont = f_open.readline()
                        f_open.close()
                        version = cont.replace("\n","")
                    except:
                        version="not found"
                    print(version)

def _version(toolname, dir_path):
    npt = dir_path+toolname+"/"+toolname+"-main/.version"
    version = ""
    if os.path.exists(npt):
        try:
            f_open = open(npt, 'r')
            cont = f_open.readline()
            version = cont.replace("\n","")
        except:
            version="null"
        f_open.close()
        print(toolname+": "+version)
    else:
        print("No tool found: "+toolname)

def _convert_size(byte):
    KB = 1024
    MB = KB ** 2
    GB = KB ** 3

    if byte < KB:
        return f"{byte} bytes"
    elif byte < MB:
        return f"{byte/KB:.2f} KB"
    elif byte < GB:
        return f"{byte/MB:.2f} MB"
    else:
        return f"{byte/GB:.2f} GB"

def _unpack_file(tool_name, dir_path):
    f_path = "{}{}.zip".format(dir_path, tool_name)
    e_path = "{}{}".format(dir_path, tool_name)
    shutil.unpack_archive(f_path, e_path)
    os.remove(f_path)

#need update
def _tool_cloner(tool_data, red, rem, osci, dir_path, blue, file_path, main_path):
    _check_support(tool_data, red, osci)
    tool_path = dir_path+tool_data
    if os.path.exists(tool_path):
        if osci == "linux":
            print(red+tool_data+rem+" already installed")
        elif osci == "window":
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0004)
            print(tool_data+" already installed")
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)
        sys.exit()
    cloner1 = "6g8r7j4I7t4N7L0V7l3t3nav2dfN2Xfm6j7P6Z9C7L4x6P8Z7k5w6Z2a2JeW6P3J6PfV6Tdg2wfB4Z9X4j8z4b1U3R0x3Q8Y3T9m2Ifs"
    cloner2 = "2cfT6C1G7p2n6Z3k6S8B6X9F7L6T6j5D2hfv6UdM6h1h7D3B7z4H6x5r7I2d2neY7raa6K9z7f0J"
    archive_ui = _real_getter(cloner1)+tool_data+_real_getter(cloner2)
    try:
        print("Getting file size...",end='\r')
        make_req = urllib.request.urlopen(archive_ui)
    except KeyboardInterrupt:
        print("Exit...")
    
    if make_req.status == 200:
        try:
            file_size = int(make_req.getheader('Content-Length'))
        except TypeError:
            make_req = urllib.request.urlopen(archive_ui)
            file_size = int(make_req.getheader('Content-Length'))
        except:
            print("Please try again!!!")
            exit()
        sise = _convert_size(file_size)
        if osci == "linux":
            print("Size : {}{}{}                               ".format(red,str(sise),rem))
        elif osci == "window":
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0004)
            print("Size : {}                               ".format(str(sise)))
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)

        block_size = 1024  
        save_path = f"{dir_path}{tool_data}.zip"
        try:
            progress = 0
            with open(save_path, 'wb') as file:
                while True:
                    data = make_req.read(block_size)
                    if not data:
                        break
                    file.write(data)
                    progress += len(data)
                    percent = (progress/file_size)*100
                    if osci == "linux":
                        print(f"Downloaded: {progress}/{file_size} bytes ({percent:.2f}%)", end='\r')
                        print("`{}{}{}` downloaded successfully!            ".format(blue,tool_data,rem))
                    elif osci == "window":
                        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0004)
                        print("`{}` downloaded successfully!".format(tool_data))
                        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)
        except KeyboardInterrupt:
            filepath = main_path+tool_data+".zip"
            manage_file(file_path, "filrem")
            print("Exit...") 
        
        try:
            _unpack_file(tool_data, dir_path)
            system_platform = platform.system()
            if system_platform == "Linux":
                cmd = "cp {}{}/{}-main/{} {}{}".format(dir_path, tool_data, tool_data, tool_data, file_path, tool_data)
                os.system(cmd)
                cmd = "chmod +x "+file_path+tool_data
                os.system(cmd)
                print("Installation Success")
                print("Type `{}{}{}` in terminal to active this tool".format(red,tool_data,rem))
            elif system_platform == "Windows":
                ffpath = dir_path+tool_data+"\\"+tool_data+"-main\\start.py"
                fspath = runner_path+"\\"+tool_data+".bat"
                fopen = open(fspath, 'w')
                fopen.write("@echo off\n")
                fopen.write("python \""+ffpath+"\"")
                fopen.close()
                print("Installation Success")
                dkji = dir_path+tool_data+"\\"+tool_data+"-main\\"+tool_data
                manage_file(dkji, "filrem")
                ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0004)
                print("Open a new command prompt(cmd) and type `{}` to active this tool".format(tool_data))
                ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)
        except Exception as e1:
            print("Error111 when extracting file")
            print(e1)
    else:
        if response.text == "Not Found":
            print(response.text+" "+tool_data+", please check tool name then try again")
        else:
            print(f"Failed to download {tool_data}")
        exit()
        

def _uninstaller(toolname, osci, dir_path, runner_path, file_path):
    print("Uninstalling {} ....".format(toolname))
    if osci == "linux":
        filepath = file_path+toolname
        manage_file(filepath, "filrem")
    elif osci == "window":
        filepath = runner_path+"\\"+toolname+".bat"
        manage_file(filepath, "filrem")
    filepath = dir_path+toolname
    manage_file(filepath, "dirrem")
    print("Successfully uninstalled!")

def _tool_updater(tool_data, dir_path, osci):
    cloner1 = "6g8r7j4I7t4N7L0V7l3t3nav2dfN2Xfm6j7P6Z9C7L4x6P8Z7k5w6Z2a2JeW6P3J6PfV6Tdg2wfB4Z9X4j8z4b1U3R0x3Q8Y3T9m2Ifs"
    cloner2 = "2cfT6C1G7p2n6Z3k6S8B6X9F7L6T6j5D2hfv6UdM6h1h7D3B7z4H6x5r7I2d2neY7raa6K9z7f0J"
    archive_ui = _real_getter(cloner1)+tool_data+_real_getter(cloner2)
    try:
        print("Getting update file size...",end='\r')
        make_req = urllib.request.urlopen(archive_ui)
    except KeyboardInterrupt:
        print("Exit...")
    
    if make_req.status == 200:
        file_size = int(make_req.getheader('Content-Length'))
        sise = _convert_size(file_size)
        if osci == "linux":
            print("Size : {}{}{}                               ".format(red,str(sise),rem))
        elif osci == "window":
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0004)
            print("Size : {}                               ".format(str(sise)))
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)
        block_size = 1024  

        save_path = f"{dir_path}{tool_data}.zip"
        try:
            with open(save_path, 'wb') as file:
                progress = 0
                for data in response.iter_content(block_size):
                    file.write(data)
                    progress += len(data)
                    percent = (progress / file_size) * 100
                    print(f"Downloaded: {progress}/{file_size} bytes ({percent:.2f}%)", end='\r')
                    print("`{}{}{}` downloaded successfully!            ".format(blue,tool_data,rem))
        except KeyboardInterrupt:
            filepath = main_path+tool_data+".zip"
            manage_file(filepath, "filrem")
            print("Exit...")
        
        try:
            _unpack_file(tool_data, dir_path)
            print("Update Success")
        except Exception as e:
            print("Error222 when extracting file")
            print(e)
    else:
        print("Failed to update [{tool_data}]")
        exit()

def _update_check(toolname, dir_path):
    path = "{}{}/{}-main/.version".format(dir_path, toolname, toolname)
    ff = open(path, 'r')
    kd = ff.readline()
    kd = kd.replace("\n","")
    cks1 = "6i8n7U4t7n4Z7q0R7l3N3MaD2XfK2Kfe7X2S6t1W7w7j2beQ6v7U6Q9b7j4p6L8C7G5m6y2G7V5w7x3P6e5h7b2H6d3o6zfC6Tet7C4M6f5H6Pel7w4W2MeH6e3i6Efq6JdY2mfz4z9S4j8z4k1K3t0s3m8A3Q9E2hfQ"
    cks2 = "2Wfq6fdo6J1b6i9e6teM2qfb2meW7c6j6u5X7W2K7X3J6X9V6ffB6OeT"
    ul = _real_getter(cks1)+toolname+_real_getter(cks2)
    try:
        gkg = urllib.request.urlopen(ul)
        kd1 = gkg.read()
        kd1 = str(kd1,'utf-8')
        kd1 = kd1.replace("\n","")
        if kd1 == kd:
            print("{} : No Update Found".format(toolname))
        else:
            _tool_updater(toolname)
    except:
        print("Error: error when getting update")


def _Handler():
    if is_admin():
        pass
    else:
        print("This script is NOT running without administrator privileges. Please run it as an administrator.")
        sys.exit()
    
    system_platform = platform.system()
    if system_platform == "Linux":
        red="\033[1;31;48m"
        white="\033[1;37;48m"
        blue="\033[1;36;48m"
        rem="\033[0m"
        osci="linux"
        file_path="/usr/local/bin/"
        dir_path="/usr/share/ihaahi/"
        main_path="/usr/share/ihaahi"
        runner_path=""
        _check_main_dict(main_path, dir_path, runner_path, osci)
    elif system_platform == "Windows":
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        osci="window"
        program_files_path = os.path.join(os.environ['ProgramFiles'], 'ihaahi')
        dir_path=program_files_path+"\\"
        runner_path = dir_path+"IHA089"
        main_path=program_files_path
        _check_main_dict(main_path, dir_path, runner_path, osci)
    elif system_platform == "Darwin":
        print("Operating System: macOS")
        print("comming soon...")
        sys.exit()
    else:
        print("Operating System: Unknown")
        sys.exit()

    
    leng = len(sys.argv)
    if leng > 1 and leng < 4 :
        if sys.argv[1] == "toollist" or sys.argv[1] == "Toollist":
            _toollist(red)
        elif sys.argv[1] == "about" or sys.argv[1] == "About":
            _about(osci, blue, red, white)
        elif sys.argv[1] == "help" or sys.argv[1] == "Help":
            _help(osci, red, blue, white)
        elif sys.argv[1] == "tools" or sys.argv[1] == "Tools":
            _all_tool(main_path, dir_path)
        elif sys.argv[1] == "install" or sys.argv[1] == "Install":
            try:
                _tool_cloner(sys.argv[2], red, rem, osci, dir_path, blue, file_path, main_path)
            except IndexError:
                print("Error: provide tool name which u want to install")
                if osci == "linux":
                    print("Ex. {}ihagarud install pchecker{}".format(red, rem))
                elif osci == "window":
                    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0004)
                    print("EX. ihagarud install pchecker")
                    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)
                exit()
        elif sys.argv[1] == "update" or sys.argv[1] == "Update":
            try:
                _update_check(sys.argv[2], dir_path)
            except IndexError:
                print("Error: provide tool name which u want to install")
                if osci == "linux":
                    print("Ex. {}ihagarud update pchecker{}".format(red, rem))
                elif osci == "window":
                    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0004)
                    print("EX. ihagarud update pchecker")
                    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)

                exit()
        elif sys.argv[1] == "uninstall" or sys.argv[1] == "Uninstall":
            try:
                _uninstaller(sys.argv[2], osci, dir_path, runner_path, file_path)
            except IndexError:
                print("Error: provide tool name which u want to install")
                if osci == "linux":
                    print("Ex. {}ihagarud uninstall pchecker{}".format(red, rem))
                elif osci == "window":
                    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0004)
                    print("EX. ihagarud uninstall pchecker")
                    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)
                exit()
        elif sys.argv[1] == "version" or sys.argv[1] == "Version":
            try:
                _version(sys.argv[2], dir_path)
            except IndexError:
                print("Error: provide tool name which u want to install")
                if osci == "linux":
                    print("Ex. {}ihagarud version pchecker{}".format(red, rem))
                elif osci == "window":
                    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0004)
                    print("EX. ihagarud version pchecker")
                    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)
                exit()
        else:
            print("command not found")
    elif leng == 1:
        _usage(osci, blue, white, red)
    else:
        error = ""
        for i in range(1, leng):
            error = error+sys.argv[i]
        if osci == "linux":
            print("{} command `{}` not found".format(red, error))
        elif osci == "window":
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0004)
            print("command `{}` not found".format(error))
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 0x0001 | 0x0002 | 0x0004 | 0x0008)

if __name__ == "__main__":
    _Handler()
