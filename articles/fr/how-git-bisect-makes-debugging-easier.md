---
title: Comment Git Bisect facilite le débogage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-23T00:06:25.000Z'
originalURL: https://freecodecamp.org/news/how-git-bisect-makes-debugging-easier
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c998e740569d1a4ca2065.jpg
tags:
- name: debugging
  slug: debugging
- name: Git
  slug: git
- name: Productivity
  slug: productivity
seo_title: Comment Git Bisect facilite le débogage
seo_desc: 'By Periklis Gkolias

  Git bisect is a fantastic tool that can help make debugging a breeze. But very few
  people use it actively.

  In this quick article, I will showcase how git bisect can easily point out the where
  your bugs lie.

  But first, lets talk ab...'
---

Par Periklis Gkolias

_Git bisect_ est un outil fantastique qui peut rendre le débogage très facile. Mais très peu de gens l'utilisent activement.

Dans cet article rapide, je vais montrer comment _git bisect_ peut facilement pointer où se trouvent vos bugs.

Mais d'abord, parlons de...

### Le débogage delta

Le débogage delta est le processus qui consiste à effectuer de nombreuses étapes de débogage et, à chaque étape, votre objectif est d'éliminer la moitié du "problème". Vous pouvez y penser comme la recherche binaire du débogage. Ou, comme l'a dit [Andreas Zeller](https://andreas-zeller.info/) (qui a inventé le terme) :

> Le débogage delta automatise la méthode scientifique du débogage. L'idée de base de la méthode scientifique est d'établir une hypothèse sur la raison pour laquelle quelque chose ne fonctionne pas. Vous testez cette hypothèse, et vous l'affinez ou la rejetez en fonction du résultat du test. Lors du débogage, les gens font cela tout le temps. Manuellement. Le débogage delta automatise ce processus.

_Git bisect_ est la manière dont nous appliquons le débogage delta avec Git.

Supposons que nous avons un bug et que nous essayons de trouver la cause racine. À chaque étape de notre investigation pour une solution, nous éliminons la moitié de l'espace de solution. Configuration, code, entrée... n'importe quoi. Voici un exemple pour clarifier.

### Exemple de git bisect

Tout d'abord, nous devons initialiser un dépôt pour suivre notre travail.

```
mkdir test_git_bisect && cd test_git_bisect && git init

```

Disons que nous allons créer un script qui prend une époque et la convertit en

```
datetime

```

Nous faisons cela en utilisant un fichier d'entrée (nommé epochs.txt) qui _devrait_ contenir uniquement des époques.

Veuillez noter que pour exécuter _git bisect_ en douceur, nous devons avoir un nombre suffisant de commits.

Le script Python `parse_epochs.py` que nous allons utiliser ici n'a rien de spécial.

```

from time import localtime, strftime

with open('epochs.txt', 'r') as handler:
    epochs = handler.readlines()
    for epoch in epochs:
        current_datetime = strftime('%Y-%m-%d %H:%M:%S', localtime(int(epoch)))
        print(current_datetime)


```

Faisons le premier commit :

`git add . && git commit -m "Created epoch parser"`

puis créons l'entrée :

`for i in {1..100}; do   sleep 3;   date +%s >> epochs.txt; done`

Cela représente essentiellement toutes les époques depuis le moment où nous avons démarré le script (plus 3 secondes) jusqu'à cinq minutes plus tard, avec un pas de 3 secondes.

Nous faisons à nouveau un commit de la modification :

`git add . && git commit -m "Generated the first version of input"`

Si nous exécutons maintenant le script initial, nous obtenons toutes les entrées analysées en dates :

```
$ python3 parse_epochs.py
2020-07-21 16:08:39
2020-07-21 16:10:40
2020-07-21 16:10:43
2020-07-21 16:10:46
2020-07-21 16:10:49
2020-07-21 16:10:52
...

```

Modifions maintenant l'entrée pour la rendre défectueuse :

```
echo "random string" >> epochs.txt

```

et faisons un commit à nouveau :

```
git add . && git commit -m "Added faulty input"

```

Pour le bien de l'entropie, pour rendre l'exemple plus complexe, ajoutons plus d'entrées défectueuses - commits.

```
echo "This is not an epoch" >> epochs.txt 
&& git add . && git commit -m "Added faulty input v2"

```

```
echo "Stop this, the script will break" >> epochs.txt
&& git add . && git commit -m "Added faulty input v3"

```

Voici le journal des commits que nous avons créé :

```
$ git log --pretty=format:"%h - %an, %ar : %s"
b811d35 - Periklis Gkolias, 2 minutes ago: Added faulty input v3
dbf75cd - Periklis Gkolias, 2 minutes ago: Added faulty input v2
cbfa2f5 - Periklis Gkolias, 8 minutes ago: Added faulty input
d02eae8 - Periklis Gkolias, 20 minutes ago: Generated first version of input
a969f3d - Periklis Gkolias, 26 minutes ago: Created epoch parser

```

Si nous exécutons à nouveau le script, il échouera évidemment avec l'erreur suivante :

```
Traceback (most recent call last):
  File "parse_epochs.py", line 6, in <module>
    current_datetime = strftime('%Y-%m-%d %H:%M:%S', localtime(int(epoch)))
ValueError: invalid literal for int() with base 10: 'random string\n'


```

Il semble que nous ayons besoin de _git bisect_ pour corriger cela. Pour ce faire, nous devons commencer l'investigation :

`git bisect start`

et marquer un commit comme mauvais (généralement le dernier) et un commit comme bon. Ce serait le deuxième commit lorsque nous avons généré l'entrée :

```
git bisect bad b811d35 && git bisect good d02eae8

```

Après cela, git bisect divise l'historique entre le bon et le mauvais commit en deux. Vous pouvez le voir en faisant `git bisect visualize` pour voir les commits qui sont considérés comme les coupables, et

```
git show

```

pour imprimer celui qui est actuellement extrait, dans notre cas celui-ci :

```
dbf75cd

```

Si nous exécutons le script, il échouera toujours. Nous marquons donc le commit actuel comme mauvais :

`git bisect bad dbf75cd`

Il est intéressant de noter la sortie de Git dans ce cas :

```
git bisect bad dbf75cd
Bisecting: 0 revisions left to test after this (roughly 0 steps)
[cbfa2f5f52b7e8a0c3a510a151ac7653377cfae1] Added faulty input

```

Git sait que nous y sommes presque. Hourra !

Si nous exécutons à nouveau le script, il échoue bien sûr. Et si nous le marquons comme mauvais, Git dit :

```
git bisect bad cbfa2f5
cbfa2f5f52b7e8a0c3a510a151ac7653377cfae1 is the first bad commit

```

À ce moment-là, vous pouvez soit corriger le bug, soit contacter la personne qui a commis le mauvais code/entrée/configuration. Voici comment obtenir les détails :

```
$ git show -s --format='%an, %ae' cbfa2f5
Periklis Gkolias, myemail@domain.com

```

## Conclusion

Merci d'avoir lu cet article. N'hésitez pas à partager vos réflexions sur cet outil formidable.