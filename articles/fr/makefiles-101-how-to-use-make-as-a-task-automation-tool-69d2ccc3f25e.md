---
title: 'Makefiles 101 : comment utiliser make comme outil d''automatisation des tâches'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-21T18:23:11.000Z'
originalURL: https://freecodecamp.org/news/makefiles-101-how-to-use-make-as-a-task-automation-tool-69d2ccc3f25e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aOVtsK7VBpDnR71WlBuHOg.jpeg
tags:
- name: automation
  slug: automation
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Makefiles 101 : comment utiliser make comme outil d''automatisation des
  tâches'
seo_desc: 'By Alex Nadalin

  It seems like developers are afraid of using make as they associate it with the
  painful experience of compiling things from scratch — the dreaded ./configure &&
  make && make install.

  Part of this fear is due to the description of what...'
---

Par Alex Nadalin

Il semble que les développeurs aient peur d'utiliser `make` car ils l'associent à l'expérience douloureuse de compiler des choses à partir de zéro — le redouté `./configure && make && make install`.

Une partie de cette peur est due à la description de ce que fait [make(1)](https://linux.die.net/man/1/make) :

> _Le but de l'utilitaire make est de déterminer automatiquement quelles parties d'un grand programme doivent être recompilées, et d'émettre les commandes pour les recompiler._

> **_Free Software Foundation_** [The Linux Man Pages](https://linux.die.net/man/1/make)

Tout le monde ne sait pas que make peut facilement être utilisé pour gérer des tâches dans vos projets. Dans cet article, je souhaite partager une brève introduction sur la façon dont [les Makefiles m'aident à automatiser certaines tâches](https://github.com/odino/mssqldump/blob/master/Makefile) dans mes activités quotidiennes. Ce guide se concentrera sur l'utilisation de make comme outil d'automatisation des tâches plutôt que comme outil de compilation de code.

### Exécution des tâches

Commençons simplement par créer un `Makefile` et définir une tâche à exécuter :

```
task:
	date
```

Si vous exécutez `make task`, vous rencontrerez l'erreur suivante :

```
/tmp \u1405 make task
Makefile:2: *** missing separator.  Stop.
```

Et cela est dû au fait que les Makefiles utilisent des tabulations pour indenter le code. Mettons à jour notre exemple en utilisant des tabulations plutôt que des espaces et... Voilà.

```
/tmp \u1405 make task
Fri Jun 15 08:34:15 +04 2018
```

Quel genre de sorcellerie est-ce ? Eh bien, `make` a compris que vous vouliez exécuter la section `task` de votre makefile, et a exécuté le code (`date`) dans cette section dans un shell, en affichant à la fois la commande et sa sortie. Si vous souhaitez sauter l'affichage de la commande qui est exécutée, vous pouvez simplement la préfixer avec un signe `@` :

```
task:
	@date
```

Exécuter la commande make à nouveau :

```
/tmp \u1405 make task
Fri Jun 15 08:34:15 +04 2018
```

La première tâche dans un `Makefile` est celle par **défaut**, ce qui signifie que nous pouvons exécuter `make` sans aucun argument :

```
/tmp \u1405 make       
Fri Jun 15 08:37:11 +04 2018
```

### Exécution de tâches supplémentaires

Vous pouvez ajouter des tâches supplémentaires dans votre `Makefile` et les appeler avec `make $TASK` :

```
task:
	@date
some:
	sleep 1
	echo "Slept"
thing:
	cal
```

Exécuter la commande make à nouveau :

```
/tmp \u1405 make thing
cal
     June 2018        
Su Mo Tu We Th Fr Sa  
                1  2  
 3  4  5  6  7  8  9  
10 11 12 13 14 15 16  
17 18 19 20 21 22 23  
24 25 26 27 28 29 30
```

### Exécution de tâches dans un ordre spécifique

Souvent, vous voudrez exécuter une tâche avant la tâche actuelle. Pensez à cela comme des hooks `before` ou `after` dans vos tests automatisés. Cela peut être fait en spécifiant une liste de tâches juste après le nom de votre tâche :

```
task: thing some
	@date
...
```

Exécuter la commande make à nouveau :

```
/tmp \u1405 make task
cal
     June 2018        
Su Mo Tu We Th Fr Sa  
                1  2  
 3  4  5  6  7  8  9  
10 11 12 13 14 15 16  
17 18 19 20 21 22 23  
24 25 26 27 28 29 30

sleep 1
echo "Slept"
Slept
Fri Jun 15 08:40:23 +04 2018
```

### Utilisation de variables avec make

Définir et utiliser des variables est assez simple :

```
VAR=123

print_var:
	echo ${VAR}
...
```

Exécuter la commande make à nouveau :

```
/tmp \u1405 make print_var    
echo 123
123
```

Mais attention, car vos variables shell ne fonctionneront pas directement :

```
print_user:
	echo $USER
```

Exécuter la commande make à nouveau :

```
/tmp \u1405 make print_user   
echo SER
SER
```

Vous devrez les échapper avec soit `${VAR}` soit `$$VAR`.

Passer des flags est également un peu différent de ce à quoi vous pourriez être habitué. Ils sont positionnés comme des flags mais utilisent la même syntaxe que les variables d'environnement :

```
print_foo:
  echo $$FOO
```

Exécuter la commande make à nouveau :

```
/tmp \u1405 make print_foo
echo $FOO

/tmp \u1405 make print_foo FOO=bar
echo $FOO
bar
```

### Make et le shell

```
5.3.1 Choosing the Shell
------------------------

The program used as the shell is taken from the variable `SHELL'.  If this variable is not set in your makefile, the program `/bin/sh' is used as the shell.
```

Make utilisera `sh` pour exécuter le code dans une tâche. Cela signifie que certaines choses pourraient ne pas fonctionner, car vous utilisez probablement une syntaxe spécifique à bash. Pour changer, vous pouvez simplement spécifier la variable `SHELL`. Dans notre cas, nous voudrions utiliser `SHELL:=/bin/bash`.

Comme vu précédemment, parfois vous devrez utiliser une syntaxe personnalisée pour faire fonctionner une commande shell régulière dans `make`. Tout comme les variables doivent être échappées avec un `$$` ou `${...}`, vous devrez utiliser `shell` lors de l'utilisation de la [substitution de commande](http://tldp.org/LDP/abs/html/commandsub.html) :

```
subshell:
  echo $(shell echo ${USER})
```

Exécuter la commande make à nouveau :

```
/tmp \u1405 make subshell
echo alex
alex
```

Vous ne me croyez pas ? Essayez de supprimer l'instruction `shell`. Voici ce que vous allez obtenir :

```
/tmp \u1405 make subshell
echo
```

### Conclusion

Il y a tellement plus de choses que `make` peut faire, et tellement plus de choses particulières que vous pourriez avoir besoin de découvrir pour diminuer le WPS (WTF par seconde) lors de son utilisation. 😄

Cela n'invalide pas le fait que `make` est un outil extrêmement utile qui nous permet d'automatiser les flux de travail avec facilité (sans avoir à configurer des pipelines très compliqués) en écrivant des lignes séparées par des tabulations avec un ensemble de commandes shell.

_Publié à l'origine sur [odino.org](https://odino.org/makefile-101/) (15 juin 2018)._
_Vous pouvez me suivre sur [Twitter](https://twitter.com/_odino_) - les rants sont les bienvenus !_ 😉