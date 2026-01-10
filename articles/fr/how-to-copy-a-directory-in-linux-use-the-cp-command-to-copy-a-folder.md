---
title: Comment copier un répertoire sous Linux – Utiliser la commande cp pour copier
  un dossier
date: '2023-05-03T13:30:33.000Z'
author: freeCodeCamp
authorURL: https://www.freecodecamp.org/news/author/shittuolumide/
originalURL: https://freecodecamp.org/news/how-to-copy-a-directory-in-linux-use-the-cp-command-to-copy-a-folder
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Shittu-Olumide-How-to-Copy-a-Directory-in-Linux---Use-the-cp-Command-to-Copy-a-Folder.png
tags: []
seo_desc: "By Shittu Olumide\nOften times you'll want to copy a folder in Linux to\
  \ perform specific tasks – maybe for backup, sharing, editing, an so on. This is\
  \ a frequent task that you can perform using the cp command. \nThe cp command is\
  \ a simple yet powerful ..."
---


Souvent, vous voudrez copier un dossier sous Linux pour effectuer des tâches spécifiques – peut-être pour une sauvegarde, un partage, une modification, etc. C'est une tâche fréquente que vous pouvez réaliser à l'aide de la commande `cp`.

<!-- more -->

La commande `cp` est une commande simple mais puissante que vous pouvez utiliser pour copier des fichiers et des répertoires sous Linux. Dans ce tutoriel, nous allons voir comment utiliser la commande `cp` pour copier un dossier sous Linux.

Les étapes à suivre pour copier un répertoire sous Linux à l'aide de la commande `cp` sont les suivantes :

## Étape 1 : Ouvrir le terminal

Pour copier un dossier sous Linux, vous devez ouvrir le terminal. Vous pouvez ouvrir le terminal en utilisant le raccourci clavier `Ctrl+Alt+T` ou en recherchant l'application Terminal dans le menu des applications.

## Étape 2 : Naviguer vers le répertoire source

Avant de copier le dossier, vous devez vous rendre dans le répertoire source. Vous pouvez utiliser la commande `cd` pour changer le répertoire de travail actuel vers le répertoire source.

Par exemple, si le dossier que vous souhaitez copier se trouve dans le répertoire personnel (home), vous pouvez utiliser la commande suivante :

```bash
cd /home/user/source_folder
```

## Étape 3 : Copier le dossier

Une fois que vous avez navigué vers le répertoire source, vous pouvez utiliser la commande `cp` pour copier le dossier. La syntaxe de base de la commande `cp` est la suivante :

```bash
cp [options] source destination
```

Pour copier un dossier, vous devez spécifier l'option `-r`, qui signifie récursif (recursive), afin de copier toute l'arborescence du répertoire. Vous devez également spécifier les chemins source et destination.

Par exemple, pour copier un dossier nommé `source_folder` vers un répertoire de destination nommé `destination_folder`, vous pouvez utiliser la commande suivante :

```bash
cp -r source_folder /path/to/destination_folder/
```

Notez que vous devez remplacer `/path/to/destination_folder/` par le chemin réel du répertoire de destination.

## Étape 4 : Vérifier le dossier copié

Après avoir copié le dossier, vous pouvez vérifier les fichiers et répertoires copiés dans le répertoire de destination. Vous pouvez utiliser la commande `ls` pour lister le contenu du répertoire de destination.

Par exemple, vous pouvez utiliser la commande suivante pour lister le contenu du répertoire `destination_folder` :

```bash
ls /path/to/destination_folder/
```

Cela affichera la liste des fichiers et des répertoires présents dans le dossier de destination.

## Avantages de la commande `cp` sous Linux

Vous vous demandez peut-être quels sont les avantages d'utiliser le terminal et la commande `cp` pour copier un dossier.

L'utilisation du terminal Linux pour copier un dossier présente plusieurs avantages, notamment :

1.  **Flexibilité** : Le terminal Linux offre une plus grande flexibilité et un meilleur contrôle lors de la copie de dossiers que l'utilisation d'une interface graphique. Avec le terminal, vous pouvez utiliser des options en ligne de commande pour personnaliser le processus de copie et gérer les erreurs qui pourraient survenir.
2.  **Vitesse** : La copie de dossiers volumineux contenant de nombreux fichiers peut être plus rapide dans le terminal qu'avec une interface graphique. En effet, le terminal consomme moins de ressources système et peut exécuter les actions plus rapidement qu'une interface visuelle.
3.  **Efficacité** : Le terminal vous permet d'effectuer plusieurs tâches simultanément et d'exécuter plusieurs commandes à la fois. Cela peut faire gagner du temps et rendre le processus de copie plus efficace.
4.  **Automatisation** : La copie de dossiers dans le terminal peut être automatisée à l'aide de scripts. Cela signifie que vous pouvez gagner du temps en créant un script pour copier les dossiers que vous utilisez fréquemment, et exécuter ce script avec une seule commande.
5.  **Fiabilité** : Le terminal est un moyen fiable de copier des dossiers car il fournit un retour d'information sur le processus de copie, y compris les erreurs ou les avertissements éventuels. Cela vous permet de prendre des mesures correctives et garantit que le processus de copie se termine avec succès.

## Conclusion

Copier un dossier sous Linux est une tâche simple qui peut être accomplie à l'aide de la commande `cp`. En suivant les étapes décrites dans cet article, vous pouvez facilement copier un dossier sous Linux via la commande `cp`.

N'oubliez pas d'utiliser l'option `-r` pour copier l'intégralité de l'arborescence du répertoire, et vérifiez le dossier copié en listant son contenu dans le répertoire de destination.

Connectons-nous sur [Twitter][1] et sur [LinkedIn][2]. Vous pouvez également vous abonner à ma chaîne [YouTube][3].

Bon code !

[1]: https://www.twitter.com/Shittu_Olumide_
[2]: https://www.linkedin.com/in/olumide-shittu
[3]: https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A