---
title: Comment utiliser votre fichier .bashrc pour faire deux fois plus avec la moitié
  des frappes
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-08-22T13:20:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-do-twice-as-much-with-half-the-keystrokes-using-bashrc
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/cover-1.png
tags:
- name: Bash
  slug: bash
- name: Devops
  slug: devops
- name: Linux
  slug: linux
- name: Productivity
  slug: productivity
- name: terminal
  slug: terminal
- name: tips
  slug: tips
seo_title: Comment utiliser votre fichier .bashrc pour faire deux fois plus avec la
  moitié des frappes
seo_desc: 'In my recent post about setting up Ubuntu with Bash scripts, I briefly
  alluded to the magic of .bashrc. This didn’t really do it justice, so here’s a quick
  post that offers a bit more detail about what the Bash configuration file can do.

  My current c...'
---

Dans mon [article récent sur la configuration d'Ubuntu avec des scripts Bash](https://victoria.dev/verbose/how-to-set-up-a-fresh-ubuntu-desktop-using-only-dotfiles-and-bash-scripts/), j'ai brièvement évoqué la magie du `.bashrc`. Cela ne lui rendait pas vraiment justice, alors voici un rapide article qui offre un peu plus de détails sur ce que le fichier de configuration Bash peut faire.

Ma configuration actuelle améliore considérablement mon flux de travail et me fait économiser bien plus de 50 % des frappes que je devrais utiliser sans elle ! Examinons quelques exemples d'alias, de fonctions et de configurations d'invite qui peuvent améliorer notre flux de travail en nous rendant plus efficaces avec moins de frappes.

# Alias Bash

Un fichier `.bashrc` bien écrit peut économiser beaucoup de frappes. Nous pouvons en tirer parti au sens littéral en utilisant des [alias bash](https://www.gnu.org/software/bash/manual/html_node/Aliases.html), ou des chaînes qui s'étendent à des commandes plus grandes. Pour un exemple indicatif, voici un alias Bash pour copier des fichiers dans le terminal :

```bash
# Toujours copier le contenu des répertoires (r)écursivement et expliquer (v) ce qui a été fait
alias cp='cp -rv'
```

La commande `alias` définit la chaîne que nous taperons, suivie de ce que cette chaîne développera. Nous pouvons remplacer des commandes existantes comme `cp` ci-dessus. Seul, la commande `cp` ne copiera que les fichiers, pas les répertoires, et réussira silencieusement. Avec cet alias, nous n'avons pas besoin de nous souvenir de passer ces deux drapeaux, ni de `cd` ou `ls` l'emplacement de notre fichier copié pour confirmer qu'il est là ! Maintenant, juste ces deux frappes (pour `c` et `d`) feront tout cela pour nous.

Voici quelques autres alias `.bashrc` pour passer des drapeaux avec des fonctions courantes.

```bash
# Lister le contenu avec des couleurs pour les types de fichiers, (A)presque tous les fichiers cachés (sans . et ..), en (C)olonnes, avec des indicateurs de classe (F)
alias ls='ls --color=auto -ACF'
# Lister le contenu avec des couleurs pour les types de fichiers, (a)ll hidden entries (including . and ..), use (l)ong listing format, with class indicators (F)
alias ll='ls --color=auto -alF'

# Expliquer (v) ce qui a été fait lors du déplacement d'un fichier
alias mv='mv -v'
# Créer tous les répertoires (p)arents non existants et expliquer (v) ce qui a été fait
alias mkdir='mkdir -pv'
# Toujours essayer de (c)ontinuer à obtenir un fichier partiellement téléchargé
alias wget='wget -c'
```

Les alias sont pratiques lorsque nous voulons éviter de taper de longues commandes. En voici quelques-uns que j'utilise lorsque je travaille avec des environnements Python :

```bash
alias pym='python3 manage.py'
alias mkenv='python3 -m venv env'
alias startenv='source env/bin/activate && which python3'
alias stopenv='deactivate'
```

Pour plus d'inspiration sur la façon dont les alias Bash peuvent faire gagner du temps, je recommande vivement [les exemples de cet article](https://www.digitalocean.com/community/tutorials/an-introduction-to-useful-bash-aliases-and-functions).

# Fonctions Bash

Un inconvénient des alias ci-dessus est qu'ils sont plutôt statiques - ils s'étendront toujours exactement au texte déclaré. Pour un alias Bash qui prend des arguments, nous devrons créer une fonction. Nous pouvons le faire comme suit :

```bash
# Afficher le contenu du répertoire après y être passé
function cd () {
    builtin cd "$1"
    ls -ACF
}
```

Je ne peux pas commencer à compter combien de fois j'ai tapé `cd` puis `ls` immédiatement après pour voir le contenu du répertoire dans lequel je me trouve maintenant. Avec cette fonction configurée, tout se passe avec juste ces deux lettres ! La fonction prend le premier argument, `$1`, comme l'emplacement pour changer de répertoire, puis imprime le contenu de ce répertoire en colonnes bien formatées avec des indicateurs de type de fichier. La partie `builtin` est nécessaire pour que Bash nous permette de remplacer cette commande par défaut.

Les fonctions Bash sont très utiles lorsqu'il s'agit de télécharger ou de mettre à niveau des logiciels. Je passais auparavant au moins quelques minutes toutes les deux semaines à télécharger la nouvelle version étendue du [générateur de site statique Hugo](https://gohugo.io/categories/releases), grâce à leur excellente fréquence de livraison. Avec une fonction, je n'ai besoin que de passer la version, et la mise à niveau se fait en quelques secondes.

```bash
# Installation ou mise à niveau de Hugo
function gethugo () {
    wget -q -P tmp/ https://github.com/gohugoio/hugo/releases/download/v"$@"/hugo_extended_"$@"_Linux-64bit.tar.gz
    tar xf tmp/hugo_extended_"$@"_Linux-64bit.tar.gz -C tmp/
    sudo mv -f tmp/hugo /usr/local/bin/
    rm -rf tmp/
    hugo version
}
```

La notation `$@` prend simplement tous les arguments donnés, remplaçant sa place dans la fonction. Pour exécuter la fonction ci-dessus et télécharger la version 0.57.2 de Hugo, nous utilisons la commande `gethugo 0.57.2`.

J'en ai aussi une pour [Golang](https://golang.org/) :

```bash
function getgolang () {
    sudo rm -rf /usr/local/go
    wget -q -P tmp/ https://dl.google.com/go/go"$@".linux-amd64.tar.gz
    sudo tar -C /usr/local -xzf tmp/go"$@".linux-amd64.tar.gz
    rm -rf tmp/
    go version
}
```

Ou comment une fonction qui ajoute une URL d'origine distante pour GitLab au dépôt actuel ?

```bash
function glab () {
    git remote set-url origin --add git@gitlab.com:"$@"/"${PWD##*/}".git
    git remote -v
}
```

Avec `glab username`, nous pouvons créer une nouvelle URL `origin` pour le dépôt Git actuel avec notre `username` sur GitLab.com. Pousser vers une nouvelle URL distante [crée automatiquement un nouveau dépôt privé GitLab](https://victoria.dev/verbose/how-to-write-bash-one-liners-for-cloning-and-managing-github-and-gitlab-repositories/#a-bash-one-liner-to-create-and-push-many-repositories-on-gitlab), donc c'est un raccourci utile pour créer des sauvegardes !

Les fonctions Bash sont vraiment limitées uniquement par les possibilités de scripting, dont il y a, pratiquement, peu de limites. Si nous faisons quelque chose fréquemment qui nécessite de taper quelques lignes dans un terminal, nous pouvons probablement créer une fonction Bash pour cela !

# Invite Bash

Outre le contenu des répertoires, il est également utile de voir le chemin complet du répertoire dans lequel nous nous trouvons. L'invite Bash peut nous montrer ce chemin, ainsi que d'autres informations utiles comme notre branche Git actuelle. Pour la rendre plus lisible, nous pouvons définir des couleurs pour chaque partie de l'invite. Voici comment nous pouvons configurer notre invite dans `.bashrc` pour y parvenir :

```bash
# Les codes de couleur sont encombrants, alors nommons-les
txtcyn='\[\e[0;96m\]' # Cyan
txtpur='\[\e[0;35m\]' # Violet
txtwht='\[\e[0;37m\]' # Blanc
txtrst='\[\e[0m\]'    # Réinitialisation du texte

# Quelle (C)ouleur pour quelle partie de l'invite ?
pathC="${txtcyn}"
gitC="${txtpur}"
pointerC="${txtwht}"
normalC="${txtrst}"

# Obtenir le nom de notre branche et mettre des parenthèses autour
gitBranch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

# Construire l'invite
export PS1="${pathC}\w ${gitC}\$(gitBranch) ${pointerC}\$${normalC} "
```

Résultat :

```bash
~/github/myrepo (master) $
```

Nommer les couleurs aide à identifier facilement où une couleur commence et s'arrête, et où la suivante commence. L'invite que nous voyons dans notre terminal est définie par la chaîne suivant `export PS1`, chaque composant de l'invite étant défini avec une [séquence d'échappement](https://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/bash-prompt-escape-sequences.html). Décomposons cela :

* `\w` affiche le répertoire de travail actuel,
* `\$(gitBranch)` appelle la fonction `gitBranch` définie ci-dessus, qui affiche la branche Git actuelle,
* `\$` affichera un "$" si vous êtes un utilisateur normal ou en mode utilisateur normal, et un "#" si vous êtes root.

La [liste complète des séquences d'échappement Bash](https://www.gnu.org/software/bash/manual/html_node/Controlling-the-Prompt.html) peut nous aider à afficher beaucoup plus d'informations, y compris même l'heure et la date ! Les invites Bash sont hautement personnalisables et individuelles, alors n'hésitez pas à les configurer comme vous le souhaitez.

Voici quelques options qui mettent les informations au premier plan et peuvent nous aider à travailler plus efficacement.

## Pour les anti-procrastination

Nom d'utilisateur et heure actuelle avec les secondes, au format 24 heures HH:MM:SS :

```bash
export PS1="${userC}\u ${normalC}at \t >"
```

```
user at 09:35:55 >

```

## Pour ceux qui aiment toujours savoir où ils en sont

Chemin complet du fichier sur une ligne séparée, et nom d'utilisateur :

```bash
export PS1="${pathC}\w${normalC}\n\u:"
```

```
~/github/myrepo
user:

```

## Pour les minimalistes

```bash
export PS1=">"
```

```
>

```

Nous pouvons construire de nombreuses invites pratiques avec juste les séquences d'échappement de base ; une fois que nous commençons à intégrer des fonctions avec des invites, comme dans l'exemple de la branche Git, les choses peuvent devenir vraiment compliquées. Si cette quantité de complication est un ajout ou un inconvénient pour votre productivité, seul vous pouvez le savoir avec certitude !

De nombreuses invites Bash sophistiquées sont possibles avec des programmes facilement disponibles avec une recherche rapide. Je n'ai intentionnellement pas fourni d'exemples ici parce que, eh bien, si vous pouvez vous enthousiasmer autant pour ce genre de choses que je peux le faire, il pourrait s'écouler quelques heures avant que vous ne reveniez à ce que vous faisiez avant de commencer à lire cet article, et je ne peux tout simplement pas avoir cela sur ma conscience. ?

Nous avons, espérons-le, trouvé un bon équilibre entre le temps investi et l'utilité acquise de notre fichier de configuration Bash ! J'espère que vous utiliserez votre capacité de frappe nouvellement récupérée pour de bonnes choses.