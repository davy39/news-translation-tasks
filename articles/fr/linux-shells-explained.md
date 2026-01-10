---
title: Les shells Linux pour débutants – Bash, Zsh et Fish expliqués
subtitle: ''
author: Anthony Behery
co_authors: []
series: null
date: '2022-12-13T21:55:05.000Z'
originalURL: https://freecodecamp.org/news/linux-shells-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-oleksandr-pidvalnyi-320260.jpg
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
- name: zsh
  slug: zsh
seo_title: Les shells Linux pour débutants – Bash, Zsh et Fish expliqués
seo_desc: 'When you open up your terminal, chances are that it uses Bash as its UNIX
  shell environment. But other "shell" environments exist.

  There are other environments such as the C Shell, Korn Shell, Z Shell, and even
  the Fish Shell. All of these different ...'
---

Lorsque vous ouvrez votre terminal, il est probable qu'il utilise Bash comme environnement de shell UNIX. Mais d'autres environnements "shell" existent.

Il existe d'autres environnements tels que le C Shell, le Korn Shell, le Z Shell et même le Fish Shell. Tous ces environnements de shell différents ont leurs propres avantages et inconvénients, et vous devriez les considérer avant de choisir celui que vous allez utiliser sur votre propre système.

Dans cet article, je vais passer en revue quelques shells populaires ainsi que leurs principales caractéristiques pour vous aider à en choisir un.

## Le shell Bash

Le shell Bash (ou Bourne Again Shell) est un shell UNIX et un langage de commande. Il a été écrit par Brain Fox pour le projet GNU en tant que remplacement logiciel libre pour le Bourne Shell (sh).

Bash a été publié pour la première fois en 1989, et pour la plupart des distributions Linux, c'est l'environnement de shell par défaut. D'autres distributions, comme Kali Linux, utilisent le Z Shell comme shell par défaut.

Bash est l'un des premiers programmes que Linus Torvalds (le créateur de Linux) a porté sur Linux.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/cli_example.png)
_[Source de l'image](https://www.geeksforgeeks.org/introduction-linux-shell-shell-scripting/)_

Une chose que vous ne devriez pas confondre est que Bash est également un langage de programmation. Donc c'est un "shell", mais vous pouvez également programmer des comportements en Bash. Par exemple :

``` bash
#!/bin/bash
echo "Hello World"
```

### Points clés sur Bash

* La plupart des utilisateurs utilisent Bash, puisque c'est l'environnement de shell par défaut sur la plupart des systèmes
* Bash ne dispose pas d'une expression générique en ligne. Une expression générique est lorsque vous souhaitez rechercher des motifs dans votre shell, similaire à Regex. Les trois principaux caractères génériques sont `*`, `?`, et `[]`.
* Vous ne pouvez pas changer automatiquement le nom du répertoire
* `#` est traité comme un commentaire dans les scripts
* Il dispose de paramètres `shopt`
* L'invite de commande dispose d'échappements de barres obliques inverses
* Les paramètres de configuration de l'utilisateur se trouvent dans `.bashrc`

## Le shell Z

Le Z Shell, ou Zsh, est également un shell UNIX très similaire à Bash. Vous pouvez également scripter et utiliser le shell comme interpréteur de commandes.

Zsh est une extension du shell Bourne avec de nombreuses améliorations. Zsh a été publié en 1990 par Paul Falstad, et il partage certaines caractéristiques avec Bash, le Korn Shell et le C Shell.

macOS utilise par défaut le shell Zsh.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/nebirhos.jpg)
_[Source de l'image](https://ohmyz.sh/)_

### Points clés sur Zsh

* Dispose de l'autocomplétion lors de l'utilisation du terminal. Ainsi, lorsque vous appuyez sur `Tab ↹` pour autocompléter la commande que vous souhaitez exécuter, non seulement il autocomplète pour vous, mais il affiche également une liste déroulante de tous les autres fichiers et répertoires possibles :

![Zsh Toggle](https://i.ibb.co/bswYkn0/0f8c8e1a6016.gif)

* Prend en charge les expressions génériques en ligne
* Beaucoup plus configurable que Bash
* Prend en charge les plugins et les thèmes. Voici une [liste de plugins](https://github.com/unixorn/awesome-zsh-plugins) disponibles pour Zsh.

Il existe également des frameworks construits autour du Z Shell. L'un des plus populaires est [Oh My Zsh](https://ohmyz.sh/), qui est un framework open-source piloté par la communauté pour gérer la configuration de Zsh. (J'utilise Oh My Zsh 😄)

![Image](https://www.freecodecamp.org/news/content/images/2022/12/oh-my-zsh-mac.jpg)
_[Source de l'image](https://osxdaily.com/2021/11/15/how-install-oh-my-zsh-mac/)_

Zsh et Oh My Zsh sont similaires mais pas exactement les mêmes. Pour réitérer, Oh My Zsh est un moyen de gérer vos configurations Zsh, ce n'est pas le shell lui-même.

## Le shell Fish

Fish est un environnement de shell UNIX avec un accent sur l'interactivité et la convivialité. Contrairement à Zsh, Fish vise à offrir à l'utilisateur une interactivité par défaut au lieu de faire confiance à l'utilisateur pour implémenter sa propre configuration.

Il a été créé par Axel Liljencrantz en 2005. Fish est considéré comme un "shell exotique" en raison du fait qu'il ne respecte pas les normes POSIX des shells. [[Source](https://en.wikipedia.org/wiki/Fish_(Unix_shell)]

![Image](https://www.freecodecamp.org/news/content/images/2022/12/fish-shell-screenshot.png)
_[Source de l'image](https://blog.sudobits.com/2015/06/05/fish-a-user-friendly-command-line-shell-for-ubuntulinux/)_

### Points clés sur Fish

* Fish dispose de suggestions automatiques "recherche au fur et à mesure de la frappe" basées sur votre historique de commandes et le répertoire dans lequel vous vous trouvez. Similaire à la recherche d'historique de Bash, la recherche d'historique de Fish Shell est **toujours** activée. Ainsi, l'utilisateur pourra obtenir un retour interactif lors de l'utilisation de son terminal.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/fish.gif)
_[Source de l'image](https://taskwarrior.org/news/news.20140906/)_

* Fish préfère également les fonctionnalités en tant que commandes plutôt qu'en tant que syntaxe. Cela rend les fonctionnalités visibles en termes de commandes avec des options et des textes d'aide
* Puisque Fish vient par défaut avec de nombreuses configurations déjà définies, il est considéré comme plus convivial pour les débutants que d'autres options `sh` comme Zsh.
* Le langage de script de Fish est différent de celui de Zsh et Bash. Zsh utilise plus d'alias alors que Fish évite d'utiliser des alias dans le langage de script.

Si vous deviez simplement créer des scripts en utilisant des commandes de base telles que `cd`, `cp`, `vim`, `ssh`, et ainsi de suite, vous ne remarqueriez aucune différence dans la façon dont les langages de script de Fish et Bash fonctionnent.

L'une des plus grandes différences est lorsque vous essayez de capturer la sortie d'une commande. Dans Bash, vous pourriez être habitué à ceci :

```bash
todays_date=$(date)
echo "Todays date is $todays_date"
```

![Output](https://i.ibb.co/0hrF0Y3/fa71b0032fba.gif)

```
Todays Date is Tue Dec 13 15:29:28 CST 2022

```

Alors que dans Fish, la capture de sortie fonctionne différemment. L'équivalent pour Fish en scripting ressemblerait à ceci :

```bash
set date (date)
echo "Todays Date $date"
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/ezgif.com-gif-maker.gif)

```bash
todays date is Tue Dec 13 21:35:03 UTC 2022                                   

```

## Conclusion

Bash, Z Shell et Fish Shell ont tous leurs mérites, ainsi que certaines similitudes. Vous pouvez utiliser chacun d'eux efficacement dans votre environnement de travail maintenant que vous en savez un peu plus à leur sujet.

Si vous voulez quelque chose de plus configurable, vous pourriez utiliser Zsh (ou même installer Oh My Zsh). Si vous voulez une expérience de terminal plus interactive sans beaucoup de configuration, vous pourriez utiliser Fish Shell. Si vous voulez l'expérience classique, vous pouvez simplement garder Bash.

Tout dépend vraiment de vos préférences en tant que développeur - alors choisissez simplement le shell qui fonctionne le mieux pour vous.

_J'espère que cela vous a aidé ! Merci d'avoir lu_ 🐆🐆🐆