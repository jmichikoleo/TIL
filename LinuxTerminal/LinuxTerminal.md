# Basic Command Line For Linux Terminal 

--- 

- 'pwd' or print working directory (to check the current directory)
- 'cd' or change directory (to move between directories)
- 'ls' or list (give a list of everything in the home directory)
    - ls -a (shows everything including hidden files)
    - ls -al (shows everything including hidden files and shows it in a long format)
    - ls -lah (shows everything, in a long format and give it in a human readable format)
- 'man' or manual
- 'touch <filename.txt>' (used to make a txt file)
- 'nano' which is a text editor (to open a file using a text editor)
- 'cat <filename.txt>' (to check the contents of the file)
- 'mkdir' (make a new directory)
- 'mv' (move file to a different directory)
- 'cp' (copy file to other directory)
- 'rm' (remove file)
    - 'rmdir' (removes an empty directory)
    - 'rm -rf' (remove recursively and forcefully)
- 'which' (search only the directories specified in the user's path env variable)
- 'whereis' (searches a  set of standard system directories for the binary, source file, and manual pages)
- 'locate' (search for files and directories on the system)
    - it's the same with 'sudo find / -iname'
- 'echo' (to print a text)
- 'printf' (to print a text with special format)
  > printf "1\n2\n3" 

  > 1
  > 2
  > 3
- 'cat .bashrc' (display the contents of .bashrc which is an automatic file in linux terminal) 
- 'less' (view file contents page by page)
- 'head filename' (view 10 first lines on the file)
    - 'head -n 15 filename' (the -n is used to specify the numbers add (if you don't use the -n it will automatically show 10), meanwhile the number beside of the n is the number of the lines that you want to show)
- 'tail filename' (view 10 last lines on the file, the -n command also works here)
- 'chmod' or change mode for permissions 
  - u for user 
  - g for group 
  - o for others 
  - a for all 
  - r for read 
  - w for write 
  - x for execute
- './filename'  (a way to run the file)
- 'history' (to show all of the command history)
  - '!number' after using the history command will run the command from that exact number on the history list.
- 'kill' (used to kill a program)
  - 'killall' (kill all running program)
  - 'xkill' (use a mouse to specifically kill a program if you click it)
- 'htop' is a real time system monitor to see the cpu, memory, swap usage. 
- 'ping web/ip address' (to check ping stats)
  > ping google.com 
- 'wget' (to download)
- 'date' (shows the date)
- 'cal' (shows the calendar)
- 'bc' or base calculator (to use the terminal as a calculator)
- 'sudo apt update' (to update all software into the latest version)
- 'grep "<text>" filename' (to search for a specific string within a file)
- whoami (to check the username of the user)

---
