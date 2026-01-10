---
title: Renommer un fichier sous Linux – Commande du terminal Bash
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-09-30T15:06:08.000Z'
originalURL: https://freecodecamp.org/news/rename-file-linux-bash-command
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Copy-of-read-write-files-python--3-.png
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
seo_title: Renommer un fichier sous Linux – Commande du terminal Bash
seo_desc: "Renaming files is a very common operation whether you are using the command\
  \ line or the GUI. \nCompared to the GUI (or Graphical User Interface), the CLI\
  \ is especially powerful. This is in part because you can rename files in bulk or\
  \ even schedule the..."
---

Renommer des fichiers est une opération très courante, que vous utilisiez la ligne de commande ou l'interface graphique (GUI).

Comparé à l'interface graphique (ou Graphical User Interface), le CLI est particulièrement puissant. C'est en partie parce que vous pouvez renommer des fichiers en masse ou même programmer des scripts pour renommer des fichiers à un moment précis.

Dans ce tutoriel, vous verrez comment renommer des fichiers dans la ligne de commande Linux en utilisant la commande intégrée `mv`.

## Comment utiliser la commande Linux `mv` 

Vous pouvez utiliser la commande Linux intégrée `mv` pour renommer des fichiers. 

La commande `mv` suit cette syntaxe :

```bash
mv [options] source_file destination_file
```

Voici quelques-unes des options qui peuvent s'avérer utiles avec la commande `mv` :

* `-v` , `--verbose`: Explique ce qui est fait.
* `-i`, `--interactive`: Demande confirmation avant de renommer le fichier.

Supposons que vous vouliez renommer `index.html` en `web_page.html`. Vous utilisez la commande `mv` comme suit :

```bash
zaira@Zaira:~/rename-files$ mv index.html web_page.html

```

Listons les fichiers pour voir si le fichier a été renommé :

```bash
zaira@Zaira:~/rename-files$ ls
web_page.html
```

## Comment renommer des fichiers en masse avec `mv` 

Voyons un script où vous pouvez renommer des fichiers en masse en utilisant une boucle et la commande `mv`.

Ici, nous avons une liste de fichiers avec l'extension `.js`. 

```bash
zaira@Zaira:~/rename-files$ ls -lrt
total 0
-rw-r--r-- 1 zaira zaira 0 Sep 30 00:24 index.js
-rw-r--r-- 1 zaira zaira 0 Sep 30 00:24 config.js
-rw-r--r-- 1 zaira zaira 0 Sep 30 00:24 blog.js
```

Ensuite, vous voulez les convertir en `.html`.

Vous pouvez utiliser la commande ci-dessous pour renommer tous les fichiers du dossier :

```bash
for f in *.js; do mv -- "$f" "${f%.js}.html"; done
```

Analysons cette longue chaîne pour voir ce qui se passe en coulisses :

* La première partie [`for f in *.js`] indique à la boucle `for` de traiter chaque fichier « .js » du répertoire.
* La partie suivante [`do mv -- "$f" "${f%.js}.html`] spécifie ce que fera le traitement. Elle utilise `mv` pour renommer chaque fichier. Le nouveau fichier sera nommé avec le nom du fichier d'origine en excluant la partie `.js`. Une nouvelle extension `.html` sera ajoutée à la place.
* La dernière partie [`done`] termine simplement la boucle une fois que tous les fichiers ont été traités.

```bash
zaira@Zaira:~/rename-files$ ls -lrt
total 0
-rw-r--r-- 1 zaira zaira 0 Sep 30 00:24 index.html
-rw-r--r-- 1 zaira zaira 0 Sep 30 00:24 config.html
-rw-r--r-- 1 zaira zaira 0 Sep 30 00:24 blog.html
```

## Conclusion

Comme vous pouvez le voir, renommer des fichiers est assez facile en utilisant le CLI. Cela peut être vraiment puissant lorsqu'il est déployé dans un script.

Quelle est la chose préférée que vous avez apprise ici ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).

[Image par storyset](https://www.freepik.com/free-vector/college-project-concept-illustration_29659818.htm) sur Freepik