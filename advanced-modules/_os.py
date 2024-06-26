import os
import datetime
result = dir(os)
# print(result)
'''
['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_TRAPPED', 'DirEntry', 'EX_CANTCREAT', 
'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 
'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 
'EX_UNAVAILABLE', 'EX_USAGE', 'F_LOCK', 'F_OK', 'F_TEST', 'F_TLOCK', 'F_ULOCK', 
'GRND_NONBLOCK', 'GRND_RANDOM', 'MFD_ALLOW_SEALING', 'MFD_CLOEXEC', 'MFD_HUGETLB', 
'MFD_HUGE_16GB', 'MFD_HUGE_16MB', 'MFD_HUGE_1GB', 'MFD_HUGE_1MB', 'MFD_HUGE_256MB', 
'MFD_HUGE_2GB', 'MFD_HUGE_2MB', 'MFD_HUGE_32MB', 'MFD_HUGE_512KB', 'MFD_HUGE_512MB', 
'MFD_HUGE_64KB', 'MFD_HUGE_8MB', 'MFD_HUGE_MASK', 'MFD_HUGE_SHIFT', 'MutableMapping', 
'NGROUPS_MAX', 'O_ACCMODE', 'O_APPEND', 'O_ASYNC', 'O_CLOEXEC', 'O_CREAT', 'O_DIRECT', 
'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_LARGEFILE', 'O_NDELAY', 'O_NOATIME', 'O_NOCTTY', 
'O_NOFOLLOW', 'O_NONBLOCK', 'O_PATH', 'O_RDONLY', 'O_RDWR', 'O_RSYNC', 'O_SYNC', 
'O_TMPFILE', 'O_TRUNC', 'O_WRONLY', 'POSIX_FADV_DONTNEED', 'POSIX_FADV_NOREUSE', 
'POSIX_FADV_NORMAL', 'POSIX_FADV_RANDOM', 'POSIX_FADV_SEQUENTIAL', 'POSIX_FADV_WILLNEED', 
'POSIX_SPAWN_CLOSE', 'POSIX_SPAWN_DUP2', 'POSIX_SPAWN_OPEN', 'PRIO_PGRP', 
'PRIO_PROCESS', 'PRIO_USER', 'P_ALL', 'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 
'P_WAIT', 'PathLike', 'RTLD_DEEPBIND', 'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 
'RTLD_NODELETE', 'RTLD_NOLOAD', 'RTLD_NOW', 'RWF_DSYNC', 'RWF_HIPRI', 'RWF_NOWAIT', 
'RWF_SYNC', 'R_OK', 'SCHED_BATCH', 'SCHED_FIFO', 'SCHED_IDLE', 'SCHED_OTHER', 
'SCHED_RESET_ON_FORK', 'SCHED_RR', 'SEEK_CUR', 'SEEK_DATA', 'SEEK_END', 'SEEK_HOLE', 
'SEEK_SET', 'ST_APPEND', 'ST_MANDLOCK', 'ST_NOATIME', 'ST_NODEV', 'ST_NODIRATIME',
 'ST_NOEXEC', 'ST_NOSUID', 'ST_RDONLY', 'ST_RELATIME', 'ST_SYNCHRONOUS', 'ST_WRITE', 
 'TMP_MAX', 'WCONTINUED', 'WCOREDUMP', 'WEXITED', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED',
  'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG', 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG', 
  'WUNTRACED', 'W_OK', 'XATTR_CREATE', 'XATTR_REPLACE', 'XATTR_SIZE_MAX', 'X_OK', 
  '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', 
  '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', 
  '_exists', '_exit', '_fspath', '_fwalk', '_get_exports_list', '_putenv', '_spawnvef', 
  '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 
  'chown', 'chroot', 'close', 'closerange', 'confstr', 'confstr_names', 
  'copy_file_range', 'cpu_count', 'ctermid', 'curdir', 'defpath', 'device_encoding',
   'devnull', 'dup', 'dup2', 'environ', 'environb', 'error', 'execl', 'execle', 
   'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir', 
   'fchmod', 'fchown', 'fdatasync', 'fdopen', 'fork', 'forkpty', 'fpathconf', 
   'fsdecode', 'fsencode', 'fspath', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 
   'fwalk', 'get_blocking', 'get_exec_path', 'get_inheritable', 'get_terminal_size', 
   'getcwd', 'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid', 
   'getgrouplist', 'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 
   'getpid', 'getppid', 'getpriority', 'getrandom', 'getresgid', 'getresuid', 'getsid',
    'getuid', 'getxattr', 'initgroups', 'isatty', 'kill', 'killpg', 'lchown', 
    'linesep', 'link', 'listdir', 'listxattr', 'lockf', 'lseek', 'lstat', 'major', 
    'makedev', 'makedirs', 'memfd_create', 'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 
    'nice', 'open', 'openpty', 'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep', 
    'pipe', 'pipe2', 'popen', 'posix_fadvise', 'posix_fallocate', 'posix_spawn', 
    'posix_spawnp', 'pread', 'preadv', 'putenv', 'pwrite', 'pwritev', 'read', 'readlink',
     'readv', 'register_at_fork', 'remove', 'removedirs', 'removexattr', 'rename',
      'renames', 'replace', 'rmdir', 'scandir', 'sched_get_priority_max', 
      'sched_get_priority_min', 'sched_getaffinity', 'sched_getparam', 
      'sched_getscheduler', 'sched_param', 'sched_rr_get_interval', 'sched_setaffinity', 
      'sched_setparam', 'sched_setscheduler', 'sched_yield', 'sendfile', 'sep', 
      'set_blocking', 'set_inheritable', 'setegid', 'seteuid', 'setgid', 'setgroups', 
      'setpgid', 'setpgrp', 'setpriority', 'setregid', 'setresgid', 'setresuid', 
      'setreuid', 'setsid', 'setuid', 'setxattr', 'spawnl', 'spawnle', 'spawnlp', 
      'spawnlpe', 'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'st', 'stat', 'stat_result',
       'statvfs', 'statvfs_result', 'strerror', 'supports_bytes_environ', 
       'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 
       'supports_follow_symlinks', 'symlink', 'sync', 'sys', 'sysconf', 'sysconf_names', 
       'system', 'tcgetpgrp', 'tcsetpgrp', 'terminal_size', 'times', 'times_result', '
       truncate', 'ttyname', 'umask', 'uname', 'uname_result', 'unlink', 'unsetenv',
        'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitid', 'waitid_result', 
        'waitpid', 'walk', 'write', 'writev']

Process finished with exit code 0

'''

r = os.name # operating systems, ex. nt is for microsoft, posix is for linux
print(r)

#dizin degistirme
# os.chdir('/home/user/Desktop')
# os.chdir('../../..')
# r = os.getcwd()
# print(r) # /home/user/Schreibtisch/python_basics/advanced-modules

#klasor olusturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasor")
# os.rename("newdirectory","yeniklasor")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasor/yeniklasor")

#listeleme
# print(os.listdir())
# print(os.listdir('/home/user'))
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)

#etkin dizin ogrenme
# r = os.getcwd()
# a = os.stat("date.py")
# print(a)
# size = a.st_size/1024
# print(f'size: {size}')
# time = datetime.datetime.fromtimestamp(a.st_ctime) # created date
# print(f'time: {time}')
# time = datetime.datetime.fromtimestamp(a.st_atime) # last access date
# print(f'time: {time}')
# time = datetime.datetime.fromtimestamp(a.st_mtime) # last modified date
# print(f'time: {time}')

# os.system("firefox --new-tab")

# path
result = os.path.abspath("_os.py")
print(result) # /home/user/Schreibtisch/python_basics/advanced-modules/_os.py
result = os.path.dirname("/home/user/Schreibtisch/python_basics/advanced-modules/_os.py")
print(result) # /home/user/Schreibtisch/python_basics/advanced-modules
result = os.path.dirname(os.path.abspath("_os.py"))
print(result) # /home/user/Schreibtisch/python_basics/advanced-modules
result = os.path.exists("/home/user/Schreibtisch/python_basics/advanced-modules/_os.py")
print(result) # True
result = os.path.exists("/home/user/Schreibtisch/python_basics/advanced-modules/_os1.py")
print(result) # False
result = os.path.isdir("/home/user/Schreibtisch/python_basics/advanced-modules/_os.py")
print(result) # False
result = os.path.isdir("/home/user/Schreibtisch/")
print(result) # True
result = os.path.isfile("/home/user/Schreibtisch/python_basics/advanced-modules/_os.py")
print(result) # True
result = os.path.join("/home","user","Schreibtisch")
print(result)
result = os.path.split("/home/user/Schreibtisch/python_basics") # ('/home/user/Schreibtisch', 'python_basics')
print(result)
result = os.path.splitext("_os.py")
print(result)
file = result[0]
print(file)
type = result[1]
print(type)














