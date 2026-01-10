---
title: Guide de personnalisation de Bashrc – Comment ajouter des alias, utiliser des
  fonctions et plus
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
seo_title: Guide de personnalisation de Bashrc – Comment ajouter des alias, utiliser
  des fonctions et plus
seo_desc: "By Brandon Wallace\nCustomizing your .bashrc file can greatly improve your\
  \ workflow and increase your productivity. \nThe .bashrc is a standard file located\
  \ in your Linux home directory. In this article I will show you useful .bashrc options,\
  \ aliases, ..."
---

Par Brandon Wallace

Personnaliser votre fichier .bashrc peut grandement améliorer votre flux de travail et augmenter votre productivité. 

Le .bashrc est un fichier standard situé dans votre répertoire personnel Linux. Dans cet article, je vais vous montrer des options utiles pour .bashrc, des alias, des fonctions et plus.

Les principaux avantages de la configuration du fichier .bashrc sont :

* L'ajout d'alias vous permet de taper des commandes plus rapidement, vous faisant gagner du temps.
* L'ajout de fonctions vous permet de sauvegarder et de réexécuter du code complexe.
* Il affiche des informations système utiles.
* Il personnalise l'invite de commande Bash.

## Comment commencer à éditer .bashrc

Voici comment vous pouvez éditer le fichier .bashrc avec un éditeur de texte :

```bash
$ vim ~/.bashrc
```

Vous pouvez ajouter un formatage de date et d'heure à l'historique bash.

```bash
HISTTIMEFORMAT="%F %T "
```

```bash
# Sortie

$ history
 1017  20210228 10:51:28  uptime
 1019  20210228 10:52:42  free -m
 1020  20210228 10:52:49  tree --dirsfirst -F
 1018  20210228 10:51:38  xrandr | awk '/\*/{print $1}'
```

Ajoutez cette ligne pour ignorer les commandes en double dans l'historique.

```bash
HISTCONTROL=ignoredups
```

Pour définir le nombre de lignes dans l'historique actif et pour définir le nombre de lignes sauvegardées dans l'historique Bash, ajoutez ces deux lignes.

```bash
HISTSIZE=2000
HISTFILESIZE=2000
```

Vous pouvez configurer votre historique pour qu'il ajoute au lieu d'écraser l'historique Bash. **`shopt`** signifie "options de shell". 

```bash
shopt -s histappend
```

Pour voir toutes les options de shell par défaut, exécutez `shopt -p`.

```bash
# Sortie

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

Créez quelques variables pour ajouter de la couleur à l'invite de commande Bash comme ceci :

```bash
blk='\[\033[01;30m\]'   # Noir
red='\[\033[01;31m\]'   # Rouge
grn='\[\033[01;32m\]'   # Vert
ylw='\[\033[01;33m\]'   # Jaune
blu='\[\033[01;34m\]'   # Bleu
pur='\[\033[01;35m\]'   # Violet
cyn='\[\033[01;36m\]'   # Cyan
wht='\[\033[01;37m\]'   # Blanc
clr='\[\033[00m\]'      # Réinitialiser
```

Ceci est pour les amateurs de Vim. Cela vous permettra d'utiliser des commandes vim sur la ligne de commande. C'est toujours la première ligne que j'ajoute à mon .bashrc.

```bash
set -o vi
```

## Comment créer des alias dans .bashrc

Vous pouvez utiliser des alias pour les commandes que vous exécutez souvent. Créer des alias vous permettra de taper plus vite, en gagnant du temps et en augmentant la productivité. 

La syntaxe pour créer un alias est `alias <mon_alias>='commande plus longue'`. Pour savoir quelles commandes feraient de bons alias, exécutez cette commande pour voir une liste des 10 commandes que vous exécutez le plus.

```bash
$ history | awk '{cmd[$2]++} END {for(elem in cmd) {print cmd[elem] " " elem}}' | sort -n -r | head -10

```

```
# Sortie

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

Puisque j'utilise beaucoup Git, ce serait une excellente commande pour créer un alias.

```bash
# Voir le statut Git.
alias gs='git status'

# Ajouter un fichier à Git.
alias ga='git add'

# Ajouter tous les fichiers à Git.
alias gaa='git add --all'

# Valider les modifications du code.
alias gc='git commit'

# Voir le journal Git.
alias gl='git log --oneline'

# Créer une nouvelle branche Git et se déplacer vers la nouvelle branche en même temps. 
alias gb='git checkout -b'

# Voir la différence.
alias gd='git diff'
```

Voici quelques autres alias utiles :

```bash
# Se déplacer vers le dossier parent.
alias ..='cd ..;pwd'

# Monter de deux dossiers parents.
alias ...='cd ../..;pwd'

# Monter de trois dossiers parents.
alias ....='cd ../../..;pwd'
```

```bash
# Appuyez sur c pour effacer l'écran du terminal.
alias c='clear'

# Appuyez sur h pour voir l'historique bash.
alias h='history'

# Afficher la structure des répertoires de manière plus lisible.
alias tree='tree --dirsfirst -F'

# Créer un répertoire et tous les répertoires parents avec verbosité.
alias mkdir='mkdir -p -v'
```

```bash
# Afficher le calendrier en tapant les trois premières lettres du mois.

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
# Sortie

$ mar

     March 2021      
Su Mo Tu We Th Fr Sa 
    1  2  3  4  5  6 
 7  8  9 10 11 12 13 
14 15 16 17 18 19 20 
21 22 23 24 25 26 27 
28 29 30 31          

```

## Comment utiliser des fonctions dans .bashrc

Les fonctions sont idéales pour du code plus complexe lorsqu'un alias ne suffit pas.

Voici la syntaxe de base des fonctions :

```bash
function nom_fonction() {
	# code;
}
```

Voici comment vous pouvez trouver les plus gros fichiers dans un répertoire :

```bash
function trouver_fichiers_plus_gros() {
    du -h -x -s -- * | sort -r -h | head -20;
}

```

```bash
# Sortie

Downloads $ trouver_fichiers_plus_gros

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

Vous pouvez également ajouter des couleurs à l'invite de commande Bash et afficher la branche Git actuelle comme ceci :

```bash
# Afficher la branche Git actuelle dans l'invite de commande Bash.

function branche_git() {
    if [ -d .git ] ; then
        printf "%s" "($(git branch 2> /dev/null | awk '/\*/{print $2}'))";
    fi
}

# Définir l'invite.

function invite_bash(){
    PS1='${debian_chroot:+($debian_chroot)}'${blu}'$(branche_git)'${pur}' \W'${grn}' \$ '${clr}
}

invite_bash

```

![bash-prompt.png](https://i.postimg.cc/mgg56Zjp/bash-prompt.png)
_Invite Bash personnalisée_

Recherchez dans votre historique les commandes exécutées précédemment :

```bash
function hg() {
    history | grep "$1";
}
```

```bash
# Sortie

$ hg vim

305  2021-03-02 16:47:33 vim .bashrc
307  2021-03-02 17:17:09 vim .tmux.conf
```

Voici comment vous commencez un nouveau projet avec Git :

```bash
function git_init() {
    if [ -z "$1" ]; then
        printf "%s\n" "Veuillez fournir un nom de répertoire.";
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
# Sortie

$ git_init mon_projet

/home/brandon/mon_projet
Initialized empty Git repository in /home/brandon/mon_projet/.git/
```

Vous pouvez également obtenir un rapport météo sur la ligne de commande. Cela nécessite le paquet **curl**, **jq**, et une [**clé API**](https://openweathermap.org/api) de [Openweathermap.](https://openweathermap.org/) Lisez la [documentation de l'API Openweathermap](https://openweathermap.org/api) afin de configurer correctement l'URL pour obtenir la météo dans votre région.

Installez curl et jq avec ces commandes :

```bash
$ sudo apt install curl jq

# OU

$ sudo dnf install curl jq
```

```bash
function rapport_meteo() {

    local response=$(curl --silent 'https://api.openweathermap.org/data/2.5/weather?id=5128581&units=imperial&appid=<VOTRE_CLE_API>') 

    local status=$(echo $response | jq -r '.cod')

	# Vérifier la réponse 200 indiquant une requête API réussie.
    case $status in
		
        200) printf "Emplacement: %s %s\n" "$(echo $response | jq '.name') $(echo $response | jq '.sys.country')"  
             printf "Prévisions: %s\n" "$(echo $response | jq '.weather[].description')" 
             printf "Température: %.1f b0F\n" "$(echo $response | jq '.main.temp')" 
             printf "Temp Min: %.1f b0F\n" "$(echo $response | jq '.main.temp_min')" 
             printf "Temp Max: %.1f b0F\n" "$(echo $response | jq '.main.temp_max')" 
            ;;
        401) echo "erreur 401"
            ;;
        *) echo "erreur"
            ;;

    esac

}
```

```bash
# Sortie

$ rapport_meteo

Emplacement: "New York" "US"
Prévisions: "ciel dégagé"
Température: 58.0 b0F
Temp Min: 56.0 b0F
Temp Max: 60.8 b0F
```

## Comment afficher les informations système dans .bashrc

Vous pouvez afficher des informations système utiles lorsque vous ouvrez le terminal comme ceci :

```bash
clear

printf "\n"
printf "   %s\n" "ADRESSE IP: $(curl ifconfig.me)"
printf "   %s\n" "UTILISATEUR: $(echo $USER)"
printf "   %s\n" "DATE: $(date)"
printf "   %s\n" "TEMPS D'ACTIVITÉ: $(uptime -p)"
printf "   %s\n" "NOM D'HÔTE: $(hostname -f)"
printf "   %s\n" "CPU: $(awk -F: '/model name/{print $2}' | head -1)"
printf "   %s\n" "NOYAU: $(uname -rms)"
printf "   %s\n" "PAQUETS: $(dpkg --get-selections | wc -l)"
printf "   %s\n" "RÉSOLUTION: $(xrandr | awk '/\*/{printf $1" "}')"
printf "   %s\n" "MÉMOIRE: $(free -m -h | awk '/Mem/{print $3"/"$2}')"
printf "\n"
```

Sortie :

![Screenshot-2021-03-15-23-39-29.png](https://i.postimg.cc/8k6pNN39/Screenshot-2021-03-15-23-39-29.png)

Sourcez le fichier .bashrc pour que les modifications prennent effet :

```bash
$ source ~/.bashrc
```

Voici toutes ces personnalisations de .bashrc ensemble. Sur un nouveau système, je colle toute personnalisation sous le code par défaut dans le fichier .bashrc.

```bash
######################################################################
#
#
#            e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 94 97   e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 94 97  e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 94 97   e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 94 97   e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 94 97
#            e2 96 88 e2 96 88 e2 94 93 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 94 93 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 94 93 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97     
#            e2 96 88 e2 96 88 e2 94 93 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 95 9a e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 94 93 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 95 9a e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 94 97
#            e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 94 93 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 94 93 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97     
#            e2 96 88 e2 96 88 e2 94 93 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 95 9a e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 94 93 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 94 93 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97     
#            e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 94 93 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 94 93 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97     
#            e2 96 88 e2 96 88 e2 94 93 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 96 88 e2 94 97 e2 96 88 e2 96 88 e2 94 93 e2 94 80 e2 94 80 e2 96 88 e2 96 88 e2 94 97     
#            e2 95 9a e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 94 80  e2 95 9a e2 94 80 e2 94 80   e2 95 9a e2 94 80 e2 95 9a e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 95 9a e2 95 9a e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 95 9a e2 95 9a e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 95 9a e2 95 9a e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 94 80 e2 95 9a
#
#
######################################################################

set -o vi

HISTTIMEFORMAT="%F %T "

HISTCONTROL=ignoredups

HISTSIZE=2000

HISTFILESIZE=2000

shopt -s histappend

blk='\[\033[01;30m\]'   # Noir
red='\[\033[01;31m\]'   # Rouge
grn='\[\033[01;32m\]'   # Vert
ylw='\[\033[01;33m\]'   # Jaune
blu='\[\033[01;34m\]'   # Bleu
pur='\[\033[01;35m\]'   # Violet
cyn='\[\033[01;36m\]'   # Cyan
wht='\[\033[01;37m\]'   # Blanc
clr='\[\033[00m\]'      # Réinitialiser

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

function trouver_fichiers_plus_gros() {
    du -h -x -s -- * | sort -r -h | head -20;
}

function branche_git() {
    if [ -d .git ] ; then
        printf "%s" "($(git branch 2> /dev/null | awk '/\*/{print $2}'))";
    fi
}

# Définir l'invite.
function invite_bash(){
    PS1='${debian_chroot:+($debian_chroot)}'${blu}'$(branche_git)'${pur}' \W'${grn}' \$ '${clr}
}

invite_bash

function git_init() {
    if [ -z "$1" ]; then
        printf "%s\n" "Veuillez fournir un nom de répertoire.";
    else
        mkdir "$1";
        builtin cd "$1";
        pwd;
        git init;
        touch readme.md .gitignore LICENSE;
        echo "# $(basename $PWD)" >> readme.md
    fi
}

function rapport_meteo() {

    local response=$(curl --silent 'https://api.openweathermap.org/data/2.5/weather?id=5128581&units=imperial&appid=<VOTRE_CLE_API>') 

    local status=$(echo $response | jq -r '.cod')

    case $status in
		
        200) printf "Emplacement: %s %s\n" "$(echo $response | jq '.name') $(echo $response | jq '.sys.country')"  
             printf "Prévisions: %s\n" "$(echo $response | jq '.weather[].description')" 
             printf "Température: %.1f b0F\n" "$(echo $response | jq '.main.temp')" 
             printf "Temp Min: %.1f b0F\n" "$(echo $response | jq '.main.temp_min')" 
             printf "Temp Max: %.1f b0F\n" "$(echo $response | jq '.main.temp_max')" 
            ;;
        401) echo "erreur 401"
            ;;
        *) echo "erreur"
            ;;

    esac

}

clear

printf "\n"
printf "   %s\n" "ADRESSE IP: $(curl ifconfig.me)"
printf "   %s\n" "UTILISATEUR: $(echo $USER)"
printf "   %s\n" "DATE: $(date)"
printf "   %s\n" "TEMPS D'ACTIVITÉ: $(uptime -p)"
printf "   %s\n" "NOM D'HÔTE: $(hostname -f)"
printf "   %s\n" "CPU: $(awk -F: '/model name/{print $2}' | head -1)"
printf "   %s\n" "NOYAU: $(uname -rms)"
printf "   %s\n" "PAQUETS: $(dpkg --get-selections | wc -l)"
printf "   %s\n" "RÉSOLUTION: $(xrandr | awk '/\*/{printf $1" "}')"
printf "   %s\n" "MÉMOIRE: $(free -m -h | awk '/Mem/{print $3"/"$2}')"
printf "\n"


```

## Conclusion

Dans cet article, vous avez appris comment configurer diverses options .bashrc, alias, fonctions et plus pour grandement améliorer votre flux de travail et augmenter votre productivité.

Suivez-moi sur [Github](https://github.com/brandon-wallace) | [Dev.to](https://dev.to/brandonwallace).