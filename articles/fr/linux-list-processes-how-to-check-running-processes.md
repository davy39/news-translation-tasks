---
title: Linux Lister les Processus – Comment Vérifier les Processus en Cours
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2021-06-29T19:47:13.000Z'
originalURL: https://freecodecamp.org/news/linux-list-processes-how-to-check-running-processes
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/article-banner.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: Linux Lister les Processus – Comment Vérifier les Processus en Cours
seo_desc: 'Every day, developers use various applications and run commands in the
  terminal. These applications can include a browser, code editor, terminal, video
  conferencing app, or music player.

  For each of these software applications that you open or comman...'
---

Chaque jour, les développeurs utilisent diverses applications et exécutent des commandes dans le terminal. Ces applications peuvent inclure un navigateur, un éditeur de code, un terminal, une application de visioconférence ou un lecteur de musique.

Pour chacune de ces applications logicielles que vous ouvrez ou des commandes que vous exécutez, cela crée un *processus* ou une *tâche*.

Une belle caractéristique du système d'exploitation Linux et des ordinateurs modernes en général est qu'ils offrent un support pour le multitâche. Ainsi, plusieurs programmes peuvent s'exécuter en même temps.

Vous êtes-vous déjà demandé comment vous pouvez vérifier tous les programmes en cours d'exécution sur votre machine ? Alors cet article est fait pour vous, car je vais vous montrer comment lister, gérer et tuer tous les processus en cours d'exécution sur votre machine Linux.

## Prérequis

* Une distribution Linux installée.

* Une connaissance de base de la navigation dans la ligne de commande.

* Un sourire sur votre visage :)

## Une Brève Introduction aux Processus Linux

Un processus est une instance d'un programme informatique en cours d'exécution que vous pouvez trouver dans une application logicielle ou une commande.

Par exemple, si vous ouvrez votre éditeur Visual Studio Code, cela crée un processus qui ne s'arrêtera (ou ne mourra) que lorsque vous terminerez ou fermerez l'application Visual Studio Code.

De même, lorsque vous exécutez une commande dans le terminal (comme `curl ifconfig.me`), cela crée un processus qui ne s'arrêtera que lorsque la commande aura fini de s'exécuter ou sera terminée.

## Comment Lister les Processus en Cours d'Exécution sous Linux en Utilisant la Commande `ps`

Vous pouvez lister les processus en cours d'exécution en utilisant la commande `ps` (ps signifie *process status*). La commande `ps` affiche vos processus en cours d'exécution en temps réel.

Pour tester cela, ouvrez simplement votre terminal et exécutez la commande `ps` comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-28-at-3.25.33-PM.png align="left")

Cela affichera le processus pour le shell actuel avec quatre colonnes :

* **PID** retourne l'ID de processus unique

* **TTY** retourne le type de terminal auquel vous êtes connecté

* **TIME** retourne le temps total d'utilisation du CPU

* **CMD** retourne le nom de la commande qui a lancé le processus.

Vous pouvez choisir d'afficher un certain ensemble de processus en utilisant n'importe quelle combinaison d'options (comme `-A`, `-a`, `-C`, `-c`, `-d`, `-E`, `-e`, `-u`, `-X`, `-x`, et autres).

Si vous spécifiez plus d'une de ces options, alors tous les processus qui correspondent à au moins une des options données seront affichés.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-28-at-3.55.10-PM.png align="left")

*La* page de manuel de la commande `ps`.

> Tapez `man ps` dans votre terminal pour lire le manuel de la commande `ps`, qui contient une référence complète pour toutes les options et leurs utilisations.

Pour afficher tous les processus en cours d'exécution pour tous les utilisateurs sur votre machine, y compris leurs noms d'utilisateur, et pour montrer les processus non attachés à votre terminal, vous pouvez utiliser la commande suivante :

```python
ps aux
```

Voici une explication de la commande :

* `ps` : est la commande de statut de processus.

* `a` : affiche les informations sur les processus des autres utilisateurs ainsi que les vôtres.

* `u` : affiche les processus appartenant aux noms d'utilisateur spécifiés.

* `x` : inclut les processus qui n'ont pas de terminal de contrôle.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-28-at-4.39.05-PM.png align="left")

Cela affichera le processus pour le shell actuel avec onze colonnes :

* **USER** retourne le nom d'utilisateur de l'utilisateur exécutant le processus

* **PID** retourne l'ID de processus unique

* **%CPU** retourne le pourcentage d'utilisation du CPU

* **%MEM** retourne le pourcentage d'utilisation de la mémoire

* **VSV** retourne la taille virtuelle en Kbytes

* **RSS** retourne la taille du jeu résident

* **TT** retourne le nom du terminal de contrôle

* **STAT** retourne l'état symbolique du processus

* **STARTED** retourne l'heure de démarrage

* **CMD** retourne la commande qui a lancé le processus.

## Comment Lister les Processus en Cours d'Exécution sous Linux en Utilisant les Commandes `top` et `htop`

Vous pouvez également utiliser la commande de gestion des tâches `top` sous Linux pour voir une liste triée en temps réel des principaux processus qui utilisent le plus de mémoire ou de CPU.

Tapez `top` dans votre terminal et vous obtiendrez un résultat comme celui que vous voyez dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-28-at-4.27.28-PM.png align="left")

> Vous pouvez taper `q` pour quitter la session.

Une alternative à `top` est `htop` qui fournit un moniteur système interactif pour visualiser et gérer les processus. Il affiche également une liste triée en temps réel des processus en fonction de leur utilisation du CPU, et vous pouvez facilement rechercher, filtrer et tuer les processus en cours d'exécution.

`htop` n'est pas installé par défaut sur Linux, vous devez donc l'installer en utilisant la commande ci-dessous ou [télécharger les binaires](https://htop.dev/downloads.html#binaries) pour votre distribution Linux préférée.

```python
sudo apt update && sudo apt install htop
```

Tapez simplement `htop` dans votre terminal et vous obtiendrez un résultat comme celui que vous voyez dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-29-at-4.49.09-AM.png align="left")

## Comment Tuer les Processus en Cours d'Exécution sous Linux

Tuer un processus signifie que vous terminez une application ou une commande en cours d'exécution. Vous pouvez tuer un processus en exécutant la commande `kill` avec l'ID du processus ou la commande `pkill` avec le nom du processus comme suit :

```python
kill [PID]
```

ou

```python
pkill [COMMAND]
```

Pour trouver l'ID du processus d'un processus en cours d'exécution, vous pouvez utiliser la commande `pgrep` suivie du nom du processus comme suit :

```python
pgrep iTerm2
```

Pour tuer le processus iTerm2 dans la capture d'écran ci-dessus, nous utiliserons l'une des commandes suivantes. Cela terminera et fermera automatiquement le processus (application) iTerm2.

```python
kill 25781
```

ou

```python
kill iTerm2
```

## Conclusion

Lorsque vous listez les processus en cours d'exécution, il s'agit généralement d'une liste longue et dense. Vous pouvez la transmettre via `less` pour afficher la sortie de la commande une page à la fois dans votre terminal comme suit :

```python
ps aux | less
```

ou afficher uniquement un processus spécifique qui correspond à un nom particulier comme suit :

```python
ps aux | grep Chrome
```

J'espère que vous comprenez maintenant ce que sont les processus Linux et comment les gérer en utilisant les commandes `ps`, `top` et `htop`.

Assurez-vous de consulter le manuel de chaque commande en exécutant `man ps`, `man top` ou `man htop` respectivement. Le manuel inclut une référence complète que vous pouvez consulter si vous avez besoin d'aide à un moment donné.

Merci d'avoir lu – à votre santé ! 💙