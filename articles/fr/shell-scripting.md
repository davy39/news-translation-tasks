---
title: Scripting Shell
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-07T18:16:00.000Z'
originalURL: https://freecodecamp.org/news/shell-scripting
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e14740569d1a4ca3b3b.jpg
tags:
- name: command line
  slug: command-line
- name: shell script
  slug: shell-script
- name: toothbrush
  slug: toothbrush
seo_title: Scripting Shell
seo_desc: In the command line, a shell script is an executable file that contains
  a set of instructions that the shell will execute. Its main purpose is to reduce
  a set of instructions (or commands) in just one file. Also it can handle some logic
  because it’s ...
---

Dans la ligne de commande, un script shell est un fichier exécutable qui contient un ensemble d'instructions que le shell exécutera. Son principal objectif est de réduire un ensemble d'instructions (ou commandes) en un seul fichier. De plus, il peut gérer une certaine logique car c'est un langage de programmation.

## **Comment le créer**

Créez le fichier :

```bash
$ touch myscript.sh
```

Ajoutez un [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) au début du fichier. La ligne Shebang est responsable de l'indication à l'interpréteur de commandes quel interpréteur sera utilisé pour exécuter le script shell :

```bash
$ echo "#!/bin/bash" > myscript.sh
# ou
$ votre-editeur-souhaite myscript.sh
# écrire à la première ligne #!/bin/bash
```

Ajoutez quelques commandes :

```bash
$ echo "echo Bonjour le monde !" >> myscript.sh
```

Donnez au fichier le mode _exécution_ :

```bash
$ chmod +x myscript.sh
```

Exécutez-le !

```bash
$ ./myscript.sh
Bonjour le monde !
```

Plus d'informations sur le scripting shell peuvent être trouvées [ici](https://www.shellscript.sh/)

## Plus d'informations sur le scripting shell et Linux :

* [Un guide du débutant pour survivre dans le shell Linux](https://www.freecodecamp.org/news/a-beginners-guide-to-surviving-in-the-linux-shell-cda0f5a0698c/)
* [Commandes Linux de base à connaître](https://guide.freecodecamp.org/linux/basic-linux-commands)
* [Astuces de scripting shell](https://www.freecodecamp.org/news/functional-and-flexible-shell-scripting-tricks-a2d693be2dd4/)