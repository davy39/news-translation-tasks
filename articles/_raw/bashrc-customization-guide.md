---
title: Bashrc Customization Guide – How to Add Aliases, Use Functions, and More
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-17T22:40:57.000Z'
originalURL: https://freecodecamp.org/news/bashrc-customization-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/bashrc_cover_image2-1.png
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
- name: Productivity
  slug: productivity
- name: shell script
  slug: shell-script
- name: unix
  slug: unix
seo_title: null
seo_desc: "By Brandon Wallace\nCustomizing your .bashrc file can greatly improve your\
  \ workflow and increase your productivity. \nThe .bashrc is a standard file located\
  \ in your Linux home directory. In this article I will show you useful .bashrc options,\
  \ aliases, ..."
---

By Brandon Wallace

Customizing your .bashrc file can greatly improve your workflow and increase your productivity. 

The .bashrc is a standard file located in your Linux home directory. In this article I will show you useful .bashrc options, aliases, functions, and more.

The main benefits of configuring the .bashrc file are:

* Adding aliases allows you to type commands faster, saving you time.
* Adding functions allows you to save and rerun complex code.
* It displays useful system information.
* It customizes the Bash prompt.

## How to Get Started with Editing .bashrc

Here's how you can edit the .bashrc file with a text editor:

```bash
$ vim ~/.bashrc
```

You can add date and time formatting to bash history.

```bash
HISTTIMEFORMAT="%F %T "
```

```bash
# Output

$ history
 1017  20210228 10:51:28  uptime
 1019  20210228 10:52:42  free -m
 1020  20210228 10:52:49  tree --dirsfirst -F
 1018  20210228 10:51:38  xrandr | awk '/\*/{print $1}'
```

Add this line to ignore duplicate commands in the history.

```bash
HISTCONTROL=ignoredups
```

To set the number of lines in active history and to set the number of lines saved in Bash history, add these two lines.

```bash
HISTSIZE=2000
HISTFILESIZE=2000
```

You can set your history to append instead of overwriting Bash history. **`shopt`** stands for "shell options". 

```bash
shopt -s histappend
```

To see all the default shell options, run `shopt -p`.

```bash
# Output

$ shopt -p

shopt -u autocd                   
shopt -u assoc_expand_once        
shopt -u cdable_vars              
shopt -u cdspell                  
shopt -u checkhash                
shopt -u checkjobs                
shopt -s checkwinsize             
[...]
```

Create some variables to add color to the Bash prompt like this:

```bash
blk='\[\033[01;30m\]'   # Black
red='\[\033[01;31m\]'   # Red
grn='\[\033[01;32m\]'   # Green
ylw='\[\033[01;33m\]'   # Yellow
blu='\[\033[01;34m\]'   # Blue
pur='\[\033[01;35m\]'   # Purple
cyn='\[\033[01;36m\]'   # Cyan
wht='\[\033[01;37m\]'   # White
clr='\[\033[00m\]'      # Reset
```

This is for the Vim lovers. This will allow you to use vim commands on the command line. This is always the first line I add to my .bashrc.

```bash
set -o vi
```

## How to Create Aliases in .bashrc

You can use aliases for commands you run a lot. Creating aliases will allow you to type faster, saving time and increasing productivity. 

The syntax for creating an alias is `alias <my_alias>='longer command'`. To find out which commands would make good aliases, run this command to see a list of the top 10 commands you run most.

```bash
$ history | awk '{cmd[$2]++} END {for(elem in cmd) {print cmd[elem] " " elem}}' | sort -n -r | head -10

```

```
# Output

171 git
108 cd
62 vim
51 python3
38 history
32 exit
30 clear
28 tmux
28 tree
27 ls
```

Since I use Git a lot, that would be a great command to create an alias for.

```bash
# View Git status.
alias gs='git status'

# Add a file to Git.
alias ga='git add'

# Add all files to Git.
alias gaa='git add --all'

# Commit changes to the code.
alias gc='git commit'

# View the Git log.
alias gl='git log --oneline'

# Create a new Git branch and move to the new branch at the same time. 
alias gb='git checkout -b'

# View the difference.
alias gd='git diff'
```

Here are some other useful aliases:

```bash
# Move to the parent folder.
alias ..='cd ..;pwd'

# Move up two parent folders.
alias ...='cd ../..;pwd'

# Move up three parent folders.
alias ....='cd ../../..;pwd'
```

```bash
# Press c to clear the terminal screen.
alias c='clear'

# Press h to view the bash history.
alias h='history'

# Display the directory structure better.
alias tree='tree --dirsfirst -F'

# Make a directory and all parent directories with verbosity.
alias mkdir='mkdir -p -v'
```

```bash
# View the calender by typing the first three letters of the month.

alias jan='cal -m 01'
alias feb='cal -m 02'
alias mar='cal -m 03'
alias apr='cal -m 04'
alias may='cal -m 05'
alias jun='cal -m 06'
alias jul='cal -m 07'
alias aug='cal -m 08'
alias sep='cal -m 09'
alias oct='cal -m 10'
alias nov='cal -m 11'
alias dec='cal -m 12'
```

```bash
# Output

$ mar

     March 2021      
Su Mo Tu We Th Fr Sa 
    1  2  3  4  5  6 
 7  8  9 10 11 12 13 
14 15 16 17 18 19 20 
21 22 23 24 25 26 27 
28 29 30 31          

```

## How to Use Functions in .bashrc

Functions are great for more complicated code when an alias won't work.

Here's the basic function syntax:

```bash
function funct_name() {
	# code;
}
```

This is how you can find the largest files in a directory:

```bash
function find_largest_files() {
    du -h -x -s -- * | sort -r -h | head -20;
}

```

```bash
# Output

Downloads $ find_largest_files

709M	systemrescue-8.00-amd64.iso
337M	debian-10.8.0-amd64-netinst.iso
9.1M	weather-icons-master.zip
6.3M	Hack-font.zip
3.9M	city.list.json.gz
2.8M	dvdrental.tar
708K	IMG_2600.JPG
100K	sql_cheat_sheet_pgsql.pdf
4.0K	repeating-a-string.txt
4.0K	heart.svg
4.0K	Fedora-Workstation-33-1.2-x86_64-CHECKSUM
[...]
```

You can also add colors to the Bash prompt and display the current Git branch like this:

```bash
# Display the current Git branch in the Bash prompt.

function git_branch() {
    if [ -d .git ] ; then
        printf "%s" "($(git branch 2> /dev/null | awk '/\*/{print $2}'))";
    fi
}

# Set the prompt.

function bash_prompt(){
    PS1='${debian_chroot:+($debian_chroot)}'${blu}'$(git_branch)'${pur}' \W'${grn}' \$ '${clr}
}

bash_prompt

```

![bash-prompt.png](https://i.postimg.cc/mgg56Zjp/bash-prompt.png)
_Custom Bash prompt_

Grep (search) through your history for previous run commands:

```bash
function hg() {
    history | grep "$1";
}
```

```bash
# Output

$ hg vim

305  2021-03-02 16:47:33 vim .bashrc
307  2021-03-02 17:17:09 vim .tmux.conf
```

This is how you start a new project with Git:

```bash
function git_init() {
    if [ -z "$1" ]; then
        printf "%s\n" "Please provide a directory name.";
    else
        mkdir "$1";
        builtin cd "$1";
        pwd;
        git init;
        touch readme.md .gitignore LICENSE;
        echo "# $(basename $PWD)" >> readme.md
    fi
}
```

```bash
# Output

$ git_init my_project

/home/brandon/my_project
Initialized empty Git repository in /home/brandon/my_project/.git/
```

You can also get the weather report on the command line. This requires the package **curl**, **jq**, and an [**API key**](https://openweathermap.org/api) from [Openweathermap.](https://openweathermap.org/) Read the [Openweathermap API documentation](https://openweathermap.org/api) in order to configure the URL correctly to get the weather in your location.

Install curl and jq with these commands:

```bash
$ sudo apt install curl jq

# OR

$ sudo dnf install curl jq
```

```bash
function weather_report() {

    local response=$(curl --silent 'https://api.openweathermap.org/data/2.5/weather?id=5128581&units=imperial&appid=<YOUR_API_KEY>') 

    local status=$(echo $response | jq -r '.cod')

	# Check for the 200 response indicating a successful API query.
    case $status in
		
        200) printf "Location: %s %s\n" "$(echo $response | jq '.name') $(echo $response | jq '.sys.country')"  
             printf "Forecast: %s\n" "$(echo $response | jq '.weather[].description')" 
             printf "Temperature: %.1f°F\n" "$(echo $response | jq '.main.temp')" 
             printf "Temp Min: %.1f°F\n" "$(echo $response | jq '.main.temp_min')" 
             printf "Temp Max: %.1f°F\n" "$(echo $response | jq '.main.temp_max')" 
            ;;
        401) echo "401 error"
            ;;
        *) echo "error"
            ;;

    esac

}
```

```bash
# Output

$ weather_report

Location: "New York" "US"
Forecast: "clear sky"
Temperature: 58.0°F
Temp Min: 56.0°F
Temp Max: 60.8°F
```

## How to Print System Information in .bashrc

You can display useful system information when you open the terminal like this:

```bash
clear

printf "\n"
printf "   %s\n" "IP ADDR: $(curl ifconfig.me)"
printf "   %s\n" "USER: $(echo $USER)"
printf "   %s\n" "DATE: $(date)"
printf "   %s\n" "UPTIME: $(uptime -p)"
printf "   %s\n" "HOSTNAME: $(hostname -f)"
printf "   %s\n" "CPU: $(awk -F: '/model name/{print $2}' | head -1)"
printf "   %s\n" "KERNEL: $(uname -rms)"
printf "   %s\n" "PACKAGES: $(dpkg --get-selections | wc -l)"
printf "   %s\n" "RESOLUTION: $(xrandr | awk '/\*/{printf $1" "}')"
printf "   %s\n" "MEMORY: $(free -m -h | awk '/Mem/{print $3"/"$2}')"
printf "\n"
```

Output:

![Screenshot-2021-03-15-23-39-29.png](https://i.postimg.cc/8k6pNN39/Screenshot-2021-03-15-23-39-29.png)

Source the .bashrc file to make the changes take effect:

```bash
$ source ~/.bashrc
```

Here are all these custom .bashrc settings together. On a new system I paste any customization below the default code in the .bashrc file.

```bash
######################################################################
#
#
#           ██████╗  █████╗ ███████╗██╗  ██╗██████╗  ██████╗
#           ██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗██╔════╝
#           ██████╔╝███████║███████╗███████║██████╔╝██║     
#           ██╔══██╗██╔══██║╚════██║██╔══██║██╔══██╗██║     
#           ██████╔╝██║  ██║███████║██║  ██║██║  ██║╚██████╗
#           ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝
#
#
######################################################################

set -o vi

HISTTIMEFORMAT="%F %T "

HISTCONTROL=ignoredups

HISTSIZE=2000

HISTFILESIZE=2000

shopt -s histappend

blk='\[\033[01;30m\]'   # Black
red='\[\033[01;31m\]'   # Red
grn='\[\033[01;32m\]'   # Green
ylw='\[\033[01;33m\]'   # Yellow
blu='\[\033[01;34m\]'   # Blue
pur='\[\033[01;35m\]'   # Purple
cyn='\[\033[01;36m\]'   # Cyan
wht='\[\033[01;37m\]'   # White
clr='\[\033[00m\]'      # Reset

alias gs='git status'

alias ga='git add'

alias gaa='git add --all'

alias gc='git commit'

alias gl='git log --oneline'

alias gb='git checkout -b'

alias gd='git diff'

alias ..='cd ..;pwd'

alias ...='cd ../..;pwd'

alias ....='cd ../../..;pwd'

alias c='clear'

alias h='history'

alias tree='tree --dirsfirst -F'

alias mkdir='mkdir -p -v'

alias jan='cal -m 01'
alias feb='cal -m 02'
alias mar='cal -m 03'
alias apr='cal -m 04'
alias may='cal -m 05'
alias jun='cal -m 06'
alias jul='cal -m 07'
alias aug='cal -m 08'
alias sep='cal -m 09'
alias oct='cal -m 10'
alias nov='cal -m 11'
alias dec='cal -m 12'

function hg() {
    history | grep "$1";
}

function find_largest_files() {
    du -h -x -s -- * | sort -r -h | head -20;
}

function git_branch() {
    if [ -d .git ] ; then
        printf "%s" "($(git branch 2> /dev/null | awk '/\*/{print $2}'))";
    fi
}

# Set the prompt.
function bash_prompt(){
    PS1='${debian_chroot:+($debian_chroot)}'${blu}'$(git_branch)'${pur}' \W'${grn}' \$ '${clr}
}

bash_prompt

function git_init() {
    if [ -z "$1" ]; then
        printf "%s\n" "Please provide a directory name.";
    else
        mkdir "$1";
        builtin cd "$1";
        pwd;
        git init;
        touch readme.md .gitignore LICENSE;
        echo "# $(basename $PWD)" >> readme.md
    fi
}

function weather_report() {

    local response=$(curl --silent 'https://api.openweathermap.org/data/2.5/weather?id=5128581&units=imperial&appid=<YOUR_API_KEY>') 

    local status=$(echo $response | jq -r '.cod')

    case $status in
		
        200) printf "Location: %s %s\n" "$(echo $response | jq '.name') $(echo $response | jq '.sys.country')"  
             printf "Forecast: %s\n" "$(echo $response | jq '.weather[].description')" 
             printf "Temperature: %.1f°F\n" "$(echo $response | jq '.main.temp')" 
             printf "Temp Min: %.1f°F\n" "$(echo $response | jq '.main.temp_min')" 
             printf "Temp Max: %.1f°F\n" "$(echo $response | jq '.main.temp_max')" 
            ;;
        401) echo "401 error"
            ;;
        *) echo "error"
            ;;

    esac

}

clear

printf "\n"
printf "   %s\n" "IP ADDR: $(curl ifconfig.me)"
printf "   %s\n" "USER: $(echo $USER)"
printf "   %s\n" "DATE: $(date)"
printf "   %s\n" "UPTIME: $(uptime -p)"
printf "   %s\n" "HOSTNAME: $(hostname -f)"
printf "   %s\n" "CPU: $(awk -F: '/model name/{print $2}' | head -1)"
printf "   %s\n" "KERNEL: $(uname -rms)"
printf "   %s\n" "PACKAGES: $(dpkg --get-selections | wc -l)"
printf "   %s\n" "RESOLUTION: $(xrandr | awk '/\*/{printf $1" "}')"
printf "   %s\n" "MEMORY: $(free -m -h | awk '/Mem/{print $3"/"$2}')"
printf "\n"


```

## Conclusion

In this article you learned how to configure various .bashrc options, aliases, functions, and more to greatly improve your workflow and increase your productivity.

Follow me on [Github](https://github.com/brandon-wallace) | [Dev.to](https://dev.to/brandonwallace).

