---
title: La commande Linux LS – Comment lister les fichiers dans un répertoire + Options
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2020-09-03T07:59:30.000Z'
originalURL: https://freecodecamp.org/news/the-linux-ls-command-how-to-list-files-in-a-directory-with-options
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/article-banner-7.png
tags:
- name: command
  slug: command
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: La commande Linux LS – Comment lister les fichiers dans un répertoire +
  Options
seo_desc: 'Since the creation of Unix in the 1970s, a lot of operating systems have
  used it as their foundation. Many of these operating systems failed, while others
  succeeded.

  Linux is one of the most popular Unix based operating systems. It''s open source,
  and...'
---

Depuis la création d'Unix dans les années 1970, de nombreux systèmes d'exploitation l'ont utilisé comme base. Beaucoup de ces systèmes d'exploitation ont échoué, tandis que d'autres ont réussi.

Linux est l'un des systèmes d'exploitation basés sur Unix les plus populaires. Il est open source et est utilisé dans le monde entier dans de nombreuses industries.

Une fonctionnalité incroyable du système d'exploitation Linux est l'interface en ligne de commande (CLI) qui permet aux utilisateurs d'interagir avec leur ordinateur à partir d'un shell. Le shell Linux est un environnement REPL (**R**ead, **E**valuate, **P**rint, **L**oop) où les utilisateurs peuvent entrer une commande et le shell l'exécute et retourne un résultat.

La commande `ls` est l'une des nombreuses commandes Linux qui permettent à un utilisateur de lister des fichiers ou des répertoires à partir de la CLI.

Dans cet article, nous allons approfondir la commande `ls` et certaines des options les plus importantes dont vous aurez besoin au quotidien.

## Prérequis

* Un ordinateur avec des répertoires et des fichiers

* Avoir l'une des distributions Linux installées

* Connaissance de base de la navigation dans la CLI

* Un sourire sur le visage :)

## La commande Linux ls

La commande `ls` est utilisée pour lister les fichiers ou les répertoires dans Linux et d'autres systèmes d'exploitation basés sur Unix.

Tout comme vous naviguez dans votre *Explorateur de fichiers* ou *Finder* avec une interface graphique, la commande `ls` vous permet de lister tous les fichiers ou répertoires dans le répertoire courant par défaut, et d'interagir davantage avec eux via la ligne de commande.

Lancez votre terminal et tapez `ls` pour voir cela en action :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-20-at-9.40.29-PM.png align="left")

## Comment lister les fichiers dans un répertoire avec des options

La commande `ls` accepte également certains flags (également appelés options) qui sont des informations supplémentaires modifiant la façon dont les fichiers ou répertoires sont listés dans votre terminal.

En d'autres termes, les flags modifient le fonctionnement de la commande `ls` :

```python
 ls [flags] [directory]
```

> PS : Le mot **contenu** utilisé dans tout l'article fait référence aux **fichiers et répertoires** listés, et non au contenu réel des fichiers/répertoires ?

### Lister les fichiers dans le répertoire de travail actuel

Tapez la commande `ls` pour lister le contenu du répertoire de travail actuel :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-20-at-9.40.29-PM.png align="left")

### Lister les fichiers dans un autre répertoire

Tapez la commande `ls [chemin du répertoire ici]` pour lister le contenu d'un autre répertoire :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-20-at-10.32.52-PM.png align="left")

### Lister les fichiers dans le répertoire racine

Tapez la commande `ls /` pour lister le contenu du répertoire racine :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-20-at-10.46.10-PM.png align="left")

### Lister les fichiers dans le répertoire parent

Tapez la commande `ls ..` pour lister le contenu du répertoire parent un niveau au-dessus. Utilisez `ls ../..` pour le contenu deux niveaux au-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-20-at-10.48.22-PM.png align="left")

### Lister les fichiers dans le répertoire personnel de l'utilisateur (/home/user)

Tapez la commande `ls ~` pour lister le contenu dans le répertoire personnel de l'utilisateur :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-20-at-10.51.19-PM.png align="left")

### Lister uniquement les répertoires

Tapez la commande `ls -d */` pour lister uniquement les répertoires :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-21-at-12.53.05-PM.png align="left")

### Lister les fichiers avec les sous-répertoires

Tapez la commande `ls *` pour lister le contenu du répertoire avec ses sous-répertoires :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-21-at-1.07.54-PM.png align="left")

### Lister les fichiers de manière récursive

Tapez la commande `ls -R` pour lister tous les fichiers et répertoires avec leurs sous-répertoires correspondants jusqu'au dernier fichier :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-9.04.56-AM.png align="left")

> Si vous avez beaucoup de fichiers, cela peut prendre très longtemps à compléter car chaque fichier dans chaque répertoire sera imprimé. Vous pouvez plutôt spécifier un répertoire pour exécuter cette commande, comme ceci : `ls Downloads -R`

### Lister les fichiers avec leurs tailles

Tapez la commande `ls -s` (le **s** est en minuscule) pour lister les fichiers ou répertoires avec leurs tailles :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-21-at-12.30.19-PM.png align="left")

### Lister les fichiers en format long

Tapez la commande `ls -l` pour lister le contenu du répertoire dans un format de tableau avec des colonnes incluant :

* permissions du contenu

* nombre de liens vers le contenu

* propriétaire du contenu

* groupe propriétaire du contenu

* taille du contenu en octets

* dernière date/heure de modification du contenu

* nom du fichier ou du répertoire

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-20-at-10.52.37-PM.png align="left")

### Lister les fichiers en format long avec des tailles de fichiers lisibles

Tapez la commande `ls -lh` pour lister les fichiers ou répertoires dans le même format de tableau ci-dessus, mais avec une autre colonne représentant la taille de chaque fichier/répertoire :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-21-at-12.14.33-PM.png align="left")

Notez que les tailles sont listées en octets (B), mégaoctets (MB), gigaoctets (GB) ou téraoctets (TB) lorsque la taille du fichier ou du répertoire est supérieure à 1024 octets.

### Lister les fichiers y compris les fichiers cachés

Tapez la commande `ls -a` pour lister les fichiers ou répertoires y compris les fichiers ou répertoires cachés. Dans Linux, tout ce qui commence par un `.` est considéré comme un fichier caché :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-21-at-11.12.26-AM.png align="left")

### Lister les fichiers en format long y compris les fichiers cachés

Tapez la commande `ls -l -a` ou `ls -a -l` ou `ls -la` ou `ls -al` pour lister les fichiers ou répertoires dans un format de tableau avec des informations supplémentaires y compris les fichiers ou répertoires cachés :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-21-at-12.17.01-PM.png align="left")

### Lister les fichiers et trier par date et heure

Tapez la commande `ls -t` pour lister les fichiers ou répertoires et trier par date de dernière modification en ordre décroissant (du plus grand au plus petit).

Vous pouvez également ajouter un flag `-r` pour inverser l'ordre de tri comme ceci : `ls -tr` :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-21-at-12.20.09-PM.png align="left")

### Lister les fichiers et trier par taille de fichier

Tapez la commande `ls -S` (le **S** est en majuscule) pour lister les fichiers ou répertoires et trier par taille en ordre décroissant (du plus grand au plus petit).

Vous pouvez également ajouter un flag `-r` pour inverser l'ordre de tri comme ceci : `ls -Sr` :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-21-at-12.20.38-PM.png align="left")

### Lister les fichiers et sortir le résultat dans un fichier

Tapez la commande `ls > output.txt` pour imprimer la sortie de la commande précédente dans un fichier `output.txt`. Vous pouvez utiliser l'un des flags discutés précédemment comme `-la` — le point clé ici est que le résultat sera sorti dans un fichier et non journalisé dans la ligne de commande.

Ensuite, vous pouvez utiliser le fichier comme vous le souhaitez, ou journaliser le contenu du fichier avec `cat output.txt` :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-9.12.59-AM.png align="left")

*.*

# Conclusion

Il existe de nombreuses autres commandes et combinaisons que vous pouvez explorer pour lister des fichiers et des répertoires en fonction de vos besoins. Une chose à retenir est la capacité à combiner plusieurs commandes ensemble en une seule fois.

Imaginez que vous souhaitez lister un fichier en format long, y compris les fichiers cachés, et trier par taille de fichier. La commande serait `ls -alS`, qui est une combinaison de `ls -l`, `ls -a` et `ls -S`.

Si vous oubliez une commande ou si vous n'êtes pas sûr de ce qu'il faut faire, vous pouvez exécuter `ls --help` ou `man ls` qui affichera un manuel avec toutes les options possibles pour la commande `ls` :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-9.57.37-AM.png align="left")

Merci d'avoir lu !