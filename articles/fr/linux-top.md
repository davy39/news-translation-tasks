---
title: Comment voir vos processus Linux
subtitle: ''
author: Anthony Behery
co_authors: []
series: null
date: '2022-12-06T21:09:33.000Z'
originalURL: https://freecodecamp.org/news/linux-top
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/Screenshot-2022-12-05-235534.png
tags:
- name: Linux
  slug: linux
seo_title: Comment voir vos processus Linux
seo_desc: "You may be used to using the Activity Monitor in MacOS or the Task Manager\
  \ for Windows to see the current processes running on your system. \nBut for those\
  \ running Linux, if that includes a dual boot, virtual box, or even WSL2, you could\
  \ use a useful ..."
---

Vous êtes peut-être habitué à utiliser l'`Activity Monitor` dans MacOS ou le `Task Manager` pour Windows afin de voir les processus en cours d'exécution sur votre système. 

Mais pour ceux qui utilisent Linux, que ce soit en dual boot, dans une machine virtuelle ou même avec WSL2, vous pouvez utiliser une commande Linux utile pour inspecter et voir tous les processus en cours dans votre système d'exploitation.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-8.png)
_Moniteur d'activité MacOS_

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-7.png)
_Gestionnaire des tâches Windows_

## Quel est l'équivalent sous Linux ?

La commande `top` (tableau des processus) sous Linux affichera tous les processus du système. Si vous essayez cette commande dans votre terminal, vous verrez ceci : 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/30fps.gif)

C'est assez pratique – le programme `top` montre une liste dynamique de tous les processus en cours d'exécution sur votre système Linux. 

Généralement, cette commande affiche un résumé des informations sur votre système qui sont actuellement exécutées/gérées par le noyau Linux. 

Pour quitter `top`, appuyez sur `q` sur votre clavier pour sortir de l'interface interactive.

### Que signifient les colonnes ?

* **PID :** Affiche les identifiants de processus uniques de la tâche.
* **USER :** Affiche quel utilisateur exécute quelle tâche

Par exemple, vous voyez "root" et "brandgrim". Root est, eh bien, la racine du système exécutant ce processus, tandis que "brandgrim" (moi !) est l'utilisateur exécutant ce processus. 

* **PR :** Ce nombre montre la priorité du processus – plus le nombre est bas, plus la priorité est élevée. (Cela a du sens intuitivement, n'est-ce pas ?) 
* **VIRT :** La mémoire virtuelle totale utilisée par la tâche
* **RES :** La quantité de RAM que le processus utilise réellement, mesurée en KB
* **SHR :** Ce nombre représente la taille de la mémoire partagée utilisée par une tâche spécifique
* **%CPU :** Représente l'utilisation du CPU
* **%MEM :** Représente l'utilisation de la mémoire
* **+TIME :** Représente le temps total de CPU que la tâche a utilisé depuis le début de la tâche
* **COMMAND :** Le nom de la commande qui a réellement démarré le processus

Lorsque vous êtes dans l'interface interactive de `top`, vous pouvez appuyer sur `h` pour afficher le `Résumé des commandes` qui est une liste de toutes les commandes que `top` a à offrir.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-9.png)
_Affichage du "Résumé des commandes" dans `top`_

## Drapeaux et commandes utiles

`top` dispose de tant de drapeaux et commandes uniques qu'il peut sembler accablant de savoir lequel utiliser, bien qu'il y ait certains drapeaux qui sont utiles dès le départ.

### Comment filtrer par utilisateur

Le drapeau `-u` spécifie quels processus doivent être listés en fonction de l'utilisateur que vous spécifiez. 

Par exemple, nous avons vu que sous la colonne **USER** il y avait "root" et "brandgrim", donc si nous essayions ceci :

```bash
top -u root
```

nous verrions ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-10.png)

Ce qui liste les processus qui sont exécutés sous l'utilisateur "root". Si nous essayions cette commande, d'autre part :

```bash
top -u brandgrim
```

Nous obtiendrions ce qui suit (qui montre les processus exécutés sous l'utilisateur "brandgrim") :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-11.png)

### Comment changer l'intervalle de rafraîchissement

Par défaut, l'intervalle de rafraîchissement de l'écran pour top est défini à 3,0 secondes. Si vous souhaitez augmenter l'intervalle ou le diminuer, vous pouvez appuyer sur `d` pendant que vous êtes dans l'interface interactive `top` afin de définir un temps souhaité.

![Image](https://i.ibb.co/d0PYmJ3/281f04fc75ba.gif)
_Montrant comment changer l'intervalle de rafraîchissement_

### Comment trier les processus par utilisation du CPU

Pour trier tous vos processus Linux par la quantité de CPU qu'ils utilisent, vous devez appuyer sur les touches `SHIFT + P` afin de les trier dans `top`. Maintenant, vous savez ce qui accaparait votre CPU – cette petite boucle while qui continuait à s'exécuter indéfiniment ! 

Par exemple, lorsque je filtre mes processus lorsque j'ouvre VSCode, voici ce que je vois :

![Processus](https://i.ibb.co/3YwQhbf/88368a8fe195.gif)

Vous pouvez voir que l'utilisation du CPU est initialement très élevée, bien qu'elle commence à diminuer à mesure que VSCode charge toutes mes extensions et l'Intellisense.

### Comment sauvegarder les processus Top dans un fichier

Pour sauvegarder tous les résultats de la commande top en cours d'exécution dans un fichier, vous pouvez utiliser ces commandes :

```bash
top -n 1 -b > top-processes.txt
```

## Alternatives à `top`

Il existe de nombreuses alternatives à `top`, telles que `Htop`, `Vtop`, `Gtop`, `Gotop`, et bien d'autres – bien que je ne couvrirai pas toutes ces alternatives dans cet article.

`Htop` est actuellement l'alternative la plus populaire à `top` grâce à son menu interactif et à la possibilité de faire défiler verticalement et horizontalement. Sans oublier que `Htop` permet également de visualiser vos processus sous forme de structure arborescente, ce qui est plus facile à visualiser.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-12.png)
_Htop (ça a l'air cool !)_

# Conclusion

`top` est une interface interactive qui vous permet de visualiser tous vos processus Linux en temps réel. Elle affiche les informations système ainsi que les listes de processus ou de threads actuellement utilisés par le noyau Linux. 

`top` dispose de ses propres commandes utiles telles que le drapeau `-u` et la commande `d`. Il existe des alternatives plus modernes à `top` comme `Htop` qui permet une interface plus colorée et interactive. 

%[https://tenor.com/view/how-linux-users-install-a-web-browser-linux-linux-users-gif-20223386]

J'espère que cela vous a aidé ! Merci d'avoir lu :)