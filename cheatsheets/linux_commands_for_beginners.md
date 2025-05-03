# Useful Linux Commands for Beginners

## 1. System Information
- `uname -a` — Show system information  
  Example: `uname -a`
- `hostname` — Show or set system hostname  
  Example: `hostname`
- `uptime` — Show how long the system has been running  
  Example: `uptime`
- `top` — Real-time process and resource monitoring  
  Example: `top`
- `htop` — Enhanced version of `top` (needs to be installed)  
  Example: `htop`

## 2. File & Directory Navigation
- `ls` — List files and directories  
  Example: `ls -l` or `ls -a`
- `pwd` — Print current working directory  
  Example: `pwd`
- `cd` — Change directory  
  Example: `cd /home/user/Documents`
- `tree` — View directory structure (needs to be installed)  
  Example: `tree`

## 3. File Operations
- `cp` — Copy files or directories  
  Example: `cp file.txt /home/user/Documents/`
- `mv` — Move or rename files  
  Example: `mv oldname.txt newname.txt`
- `rm` — Remove files or directories  
  Example: `rm file.txt` or `rm -r folder/`
- `touch` — Create empty files  
  Example: `touch newfile.txt`
- `mkdir` — Create directories  
  Example: `mkdir new_folder`
- `rmdir` — Remove empty directories  
  Example: `rmdir old_folder`

## 4. Viewing File Contents
- `cat` — View file content  
  Example: `cat file.txt`
- `less` — Paginate through file content  
  Example: `less bigfile.log`
- `more` — Similar to `less`, but more basic  
  Example: `more file.txt`
- `head` — Show first lines of a file  
  Example: `head -n 10 file.txt`
- `tail` — Show last lines of a file  
  Example: `tail -n 10 file.txt`  
  `tail -f logfile.log` (real-time monitoring)

## 5. Searching
- `find` — Search for files and directories  
  Example: `find /home -name "file.txt"`
- `grep` — Search text in files  
  Example: `grep "hello" file.txt`
- `locate` — Find file paths quickly (uses a database)  
  Example: `locate file.txt`

## 6. File Permissions & Ownership
- `chmod` — Change file permissions  
  Example: `chmod 755 script.sh`
- `chown` — Change file owner  
  Example: `sudo chown user:user file.txt`
- `ls -l` — View file permissions and ownership

## 7. Disk Usage
- `df -h` — Show disk space usage (human readable)  
  Example: `df -h`
- `du -sh folder/` — Show folder size  
  Example: `du -sh /var/log/`

## 8. Package Management (Debian/Ubuntu)
- `sudo apt update` — Update package list  
- `sudo apt upgrade` — Upgrade all installed packages  
- `sudo apt install package` — Install a package  
  Example: `sudo apt install curl`
- `sudo apt remove package` — Remove a package  
  Example: `sudo apt remove nano`

## 9. User Management
- `whoami` — Show current username  
  Example: `whoami`
- `id` — Show user ID and groups  
  Example: `id`
- `adduser` — Add a new user  
  Example: `sudo adduser newuser`
- `passwd` — Change user password  
  Example: `passwd`

## 10. Networking
- `ping` — Check network connection  
  Example: `ping google.com`
- `ifconfig` or `ip a` — Show network interfaces  
  Example: `ip a`
- `curl` — Transfer data from URLs  
  Example: `curl https://example.com`
- `wget` — Download files  
  Example: `wget https://example.com/file.txt`
- `netstat -tuln` — Show open ports (deprecated, try `ss`)
- `ss -tuln` — Modern replacement for `netstat`

## 11. System Monitoring & Logs
- `ps aux` — View running processes  
- `kill PID` — Terminate a process  
  Example: `kill 1234`
- `dmesg` — Kernel ring buffer messages  
- `journalctl` — Systemd logs  
  Example: `journalctl -xe`

## 12. Archiving & Compression
- `tar -czvf file.tar.gz folder/` — Create a compressed archive  
- `tar -xzvf file.tar.gz` — Extract a tar.gz archive  
- `zip -r file.zip folder/` — Zip a folder  
- `unzip file.zip` — Extract a zip archive

## 13. Miscellaneous
- `alias` — Create command shortcuts  
  Example: `alias ll='ls -la'`
- `man` — Display manual pages  
  Example: `man ls`
- `history` — Show previously used commands  
  Example: `history`
- `clear` — Clear the terminal screen  
- `echo` — Print to terminal  
  Example: `echo "Hello World"`
- `date` — Show current date and time
