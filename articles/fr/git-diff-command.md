---
title: Commande Git diff – Comment comparer les changements dans votre code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-29T16:50:29.000Z'
originalURL: https://freecodecamp.org/news/git-diff-command
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/git-diff.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Commande Git diff – Comment comparer les changements dans votre code
seo_desc: "By Preethi⚡\nHey friends, have you ever been working in Git and found yourself\
  \ wondering if you're going to stage the correct changes? \nOr maybe you want to\
  \ see what changes you're going to commit compared to your last commit. Perhaps\
  \ you want to see ..."
---

Par Preethi⚡

Salut les amis, avez-vous déjà travaillé avec Git en vous demandant si vous alliez indexer (stage) les bons changements ?

Ou peut-être voulez-vous voir quels changements vous allez valider (commit) par rapport à votre dernier commit. Vous souhaitez peut-être voir les différences entre deux branches, commits ou fichiers.

Ce sont des problèmes et des tâches courants lors du travail avec un système de contrôle de version. Heureusement, vous pouvez vérifier tout cela en utilisant la commande Git diff.

Je sais que votre temps est précieux, alors mettons-nous en route.

Et ne vous inquiétez pas – je vais vous enseigner chaque commande avec un exemple amusant. Commencez simplement à lire l'article avec enthousiasme.

## `git diff` – la commande diff universelle

`git diff` liste **les changements entre votre répertoire de travail actuel et votre zone d'index (staging area)**.

Prenons un exemple : j'ai créé un dépôt Git nommé `cat_vs_dog`. Non, ce n'est pas un repo formel, mais c'est tout de même très sérieux 😉. Ensuite, j'ai créé `cat.txt` et `dog.txt`.

Ils se présentent avec leurs noms – comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/kitty-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/03/puppy-1.png)

Ensuite, nous déplaçons ce changement vers la zone d'index en utilisant `git add cat.txt dog.txt`. Vous voulez confirmer ? Utilisez alors `git status`, qui montre quels changements sont prêts à être commités comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/status.png)

Ensuite, disons que je veux apporter des modifications au nom du chien – par exemple, je souhaite l'appeler "pup" au lieu de "puppy".

Avant cela, si j'exécute la commande `git diff`, elle n'affiche **rien**. Pouvez-vous deviner pourquoi ? Si vous ne le pouvez pas, c'est tout à fait normal. Continuez simplement le voyage avec moi et faites une pause de quelques secondes sur ce point.

Maintenant, j'ai changé "puppy" en "pup". C'est cool de l'appeler pup.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/pup.png)

Avant de les indexer, je souhaite voir ce que j'ai modifié dans mon répertoire de travail actuel (c'est-à-dire le dossier de travail actuel) par rapport aux changements indexés.

Pour ce faire, j'exécute la commande `git diff`. Vous pouvez maintenant voir leurs différences ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/diff.png)

Cela a un certain sens, mais c'est aussi un peu bizarre, non ? N'ayez pas peur, je suis là pour vous expliquer chaque ligne du résultat du diff.

Plus tôt, nous avons exécuté la commande `git diff` qui n'affichait rien. Parce que `git diff` montre la différence entre les changements dans votre répertoire de travail et la zone d'index. Or, nous n'avions rien changé dans le répertoire de travail après avoir indexé les changements. Il n'y avait donc aucune différence par rapport à la zone d'index. J'espère que cela est clair.

## Comprendre les résultats de `git diff` – Ligne par ligne

![Image](https://www.freecodecamp.org/news/content/images/2022/03/1-1.png)

**Ligne 1** – Il s'agit de deux versions du même fichier. Git a nommé **A** la **1ère version** et **B** la **2ème version**.

* A – Ancienne version du fichier
* B – Nouvelle version du fichier

![Image](https://www.freecodecamp.org/news/content/images/2022/03/2-2.png)

**Ligne 2** – Métadonnées sur le fichier qui ne sont pas cruciales pour votre vie. Les deux premiers hachages concernent les deux fichiers comparés. **100644** est un identifiant interne du mode de fichier.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/3-1.png)

**Ligne 3** – Git a attribué un signe moins (-) à la version **A** du fichier et un signe plus (+) à la version **B** du fichier.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/4--.png)

**Ligne 4 –** Git affiche normalement un **bloc de lignes** (chunk) qui a été modifié, pas le fichier entier.

* La ligne commençant par le symbole (-) provient de la version A
* La ligne commençant par le symbole (+) provient de la version B

À l'exception des lignes modifiées, cela inclut également quelques lignes de code avant et après ce bloc pour montrer le contexte.

**Ligne 5** – Chaque bloc commence par un **En-tête de bloc** (Chunk header). L'en-tête du bloc est identifié par **@@** (au début et à la fin). Ensuite, il y a deux ensembles de nombres. Pouvez-vous voir le **-1** et le **+1** ?

* **-1** signifie qu'à partir du fichier de la **version A**, on extrait une ligne commençant à la ligne 1.
* **+1** signifie qu'à partir du fichier de la **version B**, on extrait une ligne commençant à la ligne 1.

Si les ensembles ressemblent à **-3,4** **+3,2**, alors :

* **-3,4** signifie qu'à partir du fichier de la **version A**, on extrait quatre lignes commençant à la ligne 3.
* **+3,2** signifie qu'à partir du fichier de la **version B**, on extrait deux lignes commençant à la ligne 3.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/endline.png)

**No newline at the end of the file** – Le texte indique qu'il n'y a pas de lignes après ces lignes modifiées. Cela signifie que, dans l'exemple ci-dessus, j'ai ajouté une seule ligne et j'ai modifié cette même ligne. Il n'y a donc plus de lignes après cela.

C'est pourquoi il affiche "_No newline at end of file_" dans le résultat du diff. J'espère que vous comprenez mon point.

## Temps de célébration

Prenez une petite seconde pour célébrer votre effort cognitif. Parce que vous avez déjà mis la main à la pâte avec les résultats du diff. Maintenant, vous avez une base solide pour commencer à apprendre plus de commandes avec le sourire....

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Tan-Round-Minimalist-Modern-Typography-Pretty-things-inside-Circle-Sticker--1-.png)

## Comment comparer les changements indexés (staged) dans Git

Avant de commiter vos changements, vous pouvez comparer les **changements indexés avec le dernier commit**. Vous pouvez le faire en ajoutant un seul drapeau `--staged` ou `--cached`. J'adore `--staged` parce que c'est explicite. Si vous préférez `--cached`, c'est bien aussi.

Laissez-moi vous expliquer cela par un exemple. Tout d'abord, nous commitons nos changements indexés dans notre repo `cat_vs_dog`. Si vous ne vous souvenez pas de ce que nous avons indexé, ils s'étaient présentés comme kitty et puppy.

Ensuite, nous voulions faire un changement – c'est-à-dire que nous souhaitions changer "puppy" en "pup", ce qui n'est pas indexé.

Très bien, d'abord nous commitons les changements indexés par `git commit -m "intro to cat and dog"` :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/stage.png)

Maintenant, indexez le changement de "puppy" en "pup". Ensuite, exécutez la commande `git diff --staged` qui liste les changements entre la **zone d'index** (staging area) et votre **dernier commit**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/pup-1.png)

* **Version A –** dernier commit contenant la ligne `my name is puppy` dans `dog.txt`
* **Version B** – zone d'index qui diffère du dernier commit. Comme "puppy" vers "pup" dans `dog.txt`.

D'après le résultat du diff, nous voyons clairement ce que nous avons modifié et indexé – "my name is puppy" de la version A et "my name is pup" de la version B.

J'espère que vous êtes maintenant capable de comparer les changements et de reconnaître ce que nous avons modifié en regardant le résultat du diff. `diff` est une commande extrêmement puissante qui vous permet de comparer les changements de multiples façons.

## 4 comparaisons diff que vous devez connaître

Vous pouvez exécuter la commande `git diff HEAD` pour comparer à la fois les changements indexés et non indexés avec votre dernier commit.

Vous pouvez également exécuter la commande `git diff <nom_branche1> <nom_branche2>` pour comparer les changements de la première branche avec les changements de la deuxième branche. L'ordre est important lors de la comparaison des branches. Ainsi, le résultat du diff changera selon l'ordre.

Conseil d'expert : La comparaison de branches ne prend en compte que les commits. Elle ne recherche pas les changements indexés ou non indexés.

Vous pouvez exécuter la commande `git diff <hash_commit> <hash_commit>` pour comparer les changements entre deux commits. Comme pour la comparaison de branches, l'ordre est important pour comparer les commits.

Vous pouvez exécuter les commandes ci-dessous pour comparer les changements pour un fichier spécifique :

* `git diff HEAD <nom_fichier>`
* `git diff <nom_fichier>`
* `git diff --staged <nom_fichier>` ou `git diff --cached <nom_fichier>`
* `git diff <nom_branche1> <nom_branche2> <nom_fichier>`
* `git diff <hash_commit> <hash_commit> <nom_fichier>`

## Conclusion

J'espère que cet article vous aidera à rendre votre prochain commit ou indexation plus précis. Votre état d'esprit est important lorsque vous travaillez avec les commandes Git. Gérez-les avec confiance et vous pourrez apprendre de chaque erreur.

Si vous trouvez quoi que ce soit qui doit être mis à jour dans ce tutoriel, n'hésitez pas à me contacter😜.