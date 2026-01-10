---
title: Un guide visuel des internes de Git — Objets, Branches et Comment Créer un
  Dépôt à partir de Zéro
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2020-12-14T22:30:27.000Z'
originalURL: https://freecodecamp.org/news/git-internals-objects-branches-create-repo
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/A-Visual-Guide-to-Git-Internals-Book-Cover--1-.png
tags:
- name: Git
  slug: git
- name: handbook
  slug: handbook
- name: version control
  slug: version-control
seo_title: Un guide visuel des internes de Git — Objets, Branches et Comment Créer
  un Dépôt à partir de Zéro
seo_desc: "Many of us use git on a daily basis. But how many of us know what goes\
  \ on under the hood? \nFor example, what happens when we use git commit? What is\
  \ stored between commits? Is it just a diff between the current and previous commit?\
  \ If so, how is the ..."
---

Beaucoup d'entre nous utilisent `git` au quotidien. Mais combien d'entre nous savent ce qui se passe sous le capot ?

Par exemple, que se passe-t-il lorsque nous utilisons `git commit` ? Qu'est-ce qui est stocké entre les commits ? Est-ce simplement une diff entre le commit actuel et le précédent ? Si oui, comment cette diff est-elle encodée ? Ou est-ce qu'un instantané complet du dépôt est stocké à chaque fois ? Que se passe-t-il vraiment lorsque nous utilisons `git init` ?

Beaucoup de personnes qui utilisent `git` ne connaissent pas les réponses aux questions ci-dessus. Mais est-ce vraiment important ?

Tout d'abord, en tant que professionnels, nous devrions nous efforcer de comprendre les outils que nous utilisons, surtout si nous les utilisons tout le temps — comme `git`.

Mais encore plus important, j'ai constaté que comprendre comment git fonctionne réellement est utile dans de nombreux scénarios — qu'il s'agisse de résoudre des conflits de fusion, de chercher à effectuer un rebase intéressant, ou même simplement lorsque quelque chose ne va pas légèrement.

Vous bénéficierez de cet article si vous êtes suffisamment expérimenté avec `git` pour vous sentir à l'aise avec des commandes telles que `git pull`, `git push`, `git add` ou `git commit`.

Néanmoins, nous commencerons par un aperçu pour nous assurer que nous sommes sur la même longueur d'onde concernant les mécanismes de `git`, et spécifiquement, les termes utilisés tout au long de cet article.

J'ai également téléchargé une série YouTube couvrant cet article — vous êtes les bienvenus pour la regarder [ici](https://www.youtube.com/playlist?list=PL9lx0DXCC4BNUby5H58y6s2TQVLadV8v7).

# À quoi s'attendre de ce tutoriel

Nous allons obtenir une compréhension rare de ce qui se passe sous le capot de ce que nous faisons presque quotidiennement.

Nous commencerons par couvrir les objets — **blobs, arbres,** et **commits.** Nous discuterons brièvement des **branches** et de leur implémentation. Nous plongerons dans le **répertoire de travail, la zone de staging** et le **dépôt**.

Et nous nous assurerons de comprendre comment ces termes se rapportent aux commandes `git` que nous connaissons et utilisons pour créer un nouveau dépôt.

Ensuite, nous créerons un dépôt à partir de zéro — sans utiliser `git init`, `git add`, ou `git commit`. Cela nous permettra de **approfondir notre compréhension de ce qui se passe sous le capot** lorsque nous travaillons avec `git`.

Nous créerons également de nouvelles branches, changerons de branches, et créerons des commits supplémentaires — tout cela sans utiliser `git branch` ou `git checkout`.

À la fin de cet article, **vous aurez l'impression de _comprendre_** `**git**`. Êtes-vous prêt ? 😊

# Objets Git — blob, arbre et commit

Il est très utile de penser à `git` comme maintenant un système de fichiers, et spécifiquement — des instantanés de ce système dans le temps.

Un système de fichiers commence avec un _répertoire racine_ (dans les systèmes basés sur UNIX, `/`), qui contient généralement d'autres répertoires (par exemple, `/usr` ou `/bin`). Ces répertoires contiennent d'autres répertoires, et/ou des fichiers (par exemple, `/usr/1.txt`).

Dans `git`, les contenus des fichiers sont stockés dans des objets appelés **blobs**, des objets binaires volumineux.

La différence entre les **blobs** et les fichiers est que les fichiers contiennent également des métadonnées. Par exemple, un fichier "se souvient" quand il a été créé, donc si vous déplacez ce fichier dans un autre répertoire, son heure de création reste la même.

Les **blobs**, en revanche, sont simplement des contenus — des flux binaires de données. Un **blob** n'enregistre pas sa date de création, son nom, ou autre chose que son contenu.

Chaque **blob** dans `git` est identifié par son [hachage SHA-1](https://en.wikipedia.org/wiki/SHA-1). Les hachages SHA-1 consistent en 20 octets, généralement représentés par 40 caractères en forme hexadécimale. Tout au long de cet article, nous montrerons parfois seulement les premiers caractères de ce hachage.

![Les blobs ont des hachages SHA-1 associés](https://www.freecodecamp.org/news/content/images/2020/12/image-34.png)

Dans `git`, l'équivalent d'un répertoire est un **arbre**. Un **arbre** est essentiellement une liste de répertoires, faisant référence à des **blobs** ainsi qu'à d'autres **arbres**.

Les **arbres** sont identifiés par leurs hachages SHA-1 également. Faire référence à ces objets, soit des **blobs** ou d'autres **arbres**, se fait via le hachage SHA-1 des objets.

![Un arbre est une liste de répertoires](https://www.freecodecamp.org/news/content/images/2020/12/image-35.png)



Notez que l'**arbre** **CAFE7** fait référence au **blob F92A0** en tant que _pic.png._ Dans un autre **arbre**, ce même **blob** peut avoir un autre nom.

![Un arbre peut contenir des sous-arbres, ainsi que des blobs](https://www.freecodecamp.org/news/content/images/2020/12/image-36.png)



Le diagramme ci-dessus est équivalent à un système de fichiers avec un répertoire racine qui a un fichier à `/test.js`, et un répertoire nommé `/docs` avec deux fichiers : `/docs/pic.png` et `/docs/1.txt`.

Maintenant, il est temps de prendre un instantané de ce système de fichiers — et de stocker tous les fichiers qui existaient à ce moment-là, avec leurs contenus.

Dans `git`, un instantané est un **commit**. Un objet **commit** inclut un pointeur vers l'**arbre** principal (le répertoire racine), ainsi que d'autres métadonnées telles que le **committer**, un message de **commit** et l'heure du **commit**.

Dans la plupart des cas, un **commit** a également un ou plusieurs **commits** parents — le ou les instantanés précédents. Bien sûr, les objets **commit** sont également identifiés par leurs hachages SHA-1. Ce sont les hachages que nous avons l'habitude de voir lorsque nous utilisons `git log`.

![Un commit est un instantané dans le temps. Il fait référence à l'arbre racine. Comme il s'agit du premier commit, il n'a pas de parent(s).](https://www.freecodecamp.org/news/content/images/2020/12/image-37.png)

Chaque **commit** contient l'_instantané entier_, pas seulement les diffs des **commits** précédents.

Comment cela peut-il fonctionner ? Cela ne signifie-t-il pas que nous devons stocker beaucoup de données à chaque commit ?

Examinons ce qui se passe si nous changeons le contenu d'un fichier. Supposons que nous éditions `1.txt`, et ajoutions un point d'exclamation — c'est-à-dire que nous avons changé le contenu de `HELLO WORLD`, à `HELLO WORLD!`.

Eh bien, ce changement signifierait que nous avons un nouveau **blob**, avec un nouveau hachage SHA-1. Cela a du sens, car `sha1("HELLO WORLD")` est différent de `sha1("HELLO WORLD!")`.

![Changer le blob entraîne un nouveau SHA-1](https://www.freecodecamp.org/news/content/images/2020/12/image-38.png)

Puisque nous avons un nouveau hachage, alors la liste de l'**arbre** devrait également changer. Après tout, notre **arbre** ne pointe plus vers **blob 73D8A**, mais plutôt vers **blob 62E7A** à la place. En changeant le contenu de l'**arbre**, nous changeons également son hachage.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-39.png)
_L'arbre qui pointe vers le blob modifié doit également changer_

Et maintenant, puisque le hachage de cet **arbre** est différent, nous devons également changer l'**arbre** parent — puisque ce dernier ne pointe plus vers **arbre CAFE7**, mais plutôt vers **arbre 24601**. Par conséquent, l'**arbre** **parent** aura également un nouveau hachage.

![L'arbre racine change également, et donc son hachage.](https://www.freecodecamp.org/news/content/images/2020/12/image-40.png)

Presque prêt à créer un nouvel objet **commit**, et il semble que nous allons stocker beaucoup de données — l'ensemble du système de fichiers, une fois de plus ! Mais est-ce vraiment nécessaire ?

En fait, certains objets, spécifiquement les objets **blob**, n'ont pas changé depuis le commit précédent — **blob F92A0** est resté intact, et il en va de même pour **blob F00D1.**

Donc voici l'astuce — tant qu'un objet ne change pas, nous ne le stockons pas à nouveau. Dans ce cas, nous n'avons pas besoin de stocker **blob F92A0** et **blob F00D1** une fois de plus. Nous nous référons simplement à eux par leurs valeurs de hachage. Nous pouvons ensuite créer notre objet **commit**.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-41.png)
_Les blobs qui sont restés intacts sont référencés par leurs valeurs de hachage_

Puisque ce **commit** n'est pas le premier **commit**, il a un parent — **commit A1337**.

#### Donc pour résumer, nous avons introduit trois objets git :

* **blob** — contenus d'un fichier.
* **arbre** — une liste de répertoires (de **blobs** et **arbres**).
* **commit** — un instantané de l'arbre de travail.

Considérons les hachages de ces objets pendant un instant. Supposons que j'ai écrit la chaîne `git is awesome!` et créé un **blob** à partir de celle-ci. Vous avez fait de même sur votre système. Aurions-nous le même hachage ?

La réponse est — Oui. Puisque les **blobs** consistent en les mêmes données, ils auront les mêmes valeurs SHA-1.

Et si je créais un **arbre** qui référence le **blob** de `git is awesome!`, et que je lui donnais un nom spécifique et des métadonnées, et que vous faisiez exactement la même chose sur votre système. Aurions-nous le même hachage ?

Encore une fois, oui. Puisque les objets **arbres** sont les mêmes, ils auraient le même hachage.

Et si je créais un **commit** de cet **arbre** avec le message de commit `Hello`, et que vous faisiez de même sur votre système. Aurions-nous le même hachage ?

Dans ce cas, la réponse est — Non. Même si nos objets **commit** référencent le même **arbre**, ils ont des détails de **commit** différents — temps, committer, etc.

# Branches dans Git

**Une branche est simplement une référence nommée à un commit.**

Nous pourrions toujours référencer un **commit** par son hachage SHA-1, mais les humains préfèrent généralement d'autres formes pour nommer les objets. Une **branche** est une façon de référencer un **commit**, mais ce n'est vraiment que cela.

Dans la plupart des dépôts, la ligne principale de développement est faite dans une branche appelée `master`. Ce n'est qu'un nom, et il est créé lorsque nous utilisons `git init`, ce qui le rend largement utilisé. Cependant, il n'est en aucun cas spécial, et nous pourrions utiliser n'importe quel autre nom que nous aimerions.

Typiquement, la branche pointe vers le dernier **commit** dans la ligne de développement sur laquelle nous travaillons actuellement.

![Une branche est simplement une référence nommée à un commit](https://www.freecodecamp.org/news/content/images/2020/12/image-42.png)

Pour créer une autre branche, nous utilisons généralement la commande `git branch`. En faisant cela, nous créons en fait un autre pointeur. Donc si nous créons une branche appelée `test`, en utilisant `git branch test`, nous créons en fait un autre pointeur qui pointe vers le même **commit** que la branche sur laquelle nous nous trouvons actuellement.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-43.png)
_L'utilisation de `git branch` crée un autre pointeur_

Comment `git` sait-il sur quelle branche nous nous trouvons actuellement ? Il conserve un pointeur spécial appelé `HEAD`. Habituellement, `HEAD` pointe vers une branche, qui à son tour pointe vers un **commit**. Dans certains cas, `HEAD` peut également pointer directement vers un **commit**, mais nous ne nous concentrerons pas sur cela.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-44.png)
_HEAD pointe vers la branche sur laquelle nous nous trouvons actuellement._

Pour basculer la branche active vers `test`, nous pouvons utiliser la commande `git checkout test`. Maintenant, nous pouvons déjà deviner ce que cette commande fait réellement — elle change simplement `HEAD` pour pointer vers `test`.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-45.png)
_`git checkout test` change où `HEAD` pointe_

Nous pourrions également utiliser `git checkout -b test` avant de créer la branche `test`, ce qui est l'équivalent d'exécuter `git branch test` pour créer la branche, puis `git checkout test` pour déplacer `HEAD` pour pointer vers la nouvelle branche.

Que se passe-t-il si nous apportons quelques modifications et créons un nouveau **commit** en utilisant `git commit` ? À quelle branche le nouveau **commit** sera-t-il ajouté ?

La réponse est la branche `test`, car il s'agit de la branche active (puisque `HEAD` pointe vers elle). Ensuite, le pointeur `test` se déplacera vers le **commit** nouvellement ajouté. Notez que `HEAD` pointe toujours vers `test`.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-46.png)
_Chaque fois que nous utilisons `git commit`, le pointeur de branche se déplace vers le commit nouvellement créé._

Donc si nous revenons à master par `git checkout master`, nous déplaçons `HEAD` pour pointer à nouveau vers `master`.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-47.png)

Maintenant, si nous créons un autre **commit**, il sera ajouté à la branche `master` (et son parent serait **commit B2424**).

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-48.png)

# Comment Enregistrer les Changements dans Git

Habituellement, lorsque nous travaillons sur notre code source, nous travaillons à partir d'un **répertoire de travail**. Un **répertoire de travail** (ou **arbre de travail**) est n'importe quel répertoire sur notre système de fichiers qui a un **dépôt** associé. Il contient les dossiers et fichiers de notre projet, ainsi qu'un répertoire appelé `.git` dont nous parlerons plus tard.

Après avoir apporté quelques modifications, nous voulons les enregistrer dans notre **dépôt**. Un **dépôt** (en bref : **repo**) est une collection de **commits**, chacun d'eux étant une archive de ce à quoi ressemblait l'**arbre de travail** du projet à une date passée, que ce soit sur notre machine ou celle de quelqu'un d'autre.

Un **dépôt** inclut également d'autres choses que nos fichiers de code, comme `HEAD`, les branches, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-49.png)

Contrairement à d'autres outils similaires que vous avez peut-être utilisés, `git` ne commite pas les changements directement depuis l'**arbre de travail** vers le **dépôt**. Au lieu de cela, les changements sont d'abord enregistrés dans quelque chose appelé l'**index**, ou la **zone de staging**.

Ces deux termes font référence à la même chose, et ils sont souvent utilisés dans la documentation de `git`. Nous utiliserons ces termes de manière interchangeable tout au long de cet article.

Lorsque nous `checkout` une branche, `git` remplit l'**index** avec tous les contenus de fichiers qui ont été dernièrement extraits dans notre **répertoire de travail** et à quoi ils ressemblaient lorsqu'ils ont été initialement extraits. Lorsque nous utilisons `git commit`, le **commit** est créé en fonction de l'état de l'**index**.

L'utilisation de l'**index** nous permet de préparer soigneusement chaque **commit**. Par exemple, nous pouvons avoir deux fichiers avec des changements depuis notre dernier **commit** dans notre **répertoire de travail**. Nous pouvons n'ajouter qu'un seul d'entre eux à l'**index** (en utilisant `git add`), puis utiliser `git commit` pour enregistrer uniquement ce changement.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-50.png)

Les fichiers dans notre **répertoire de travail** peuvent être dans l'un des deux états : **suivis** ou **non suivis**.

Les **fichiers suivis** sont des fichiers que `git` connaît. Ils étaient soit dans le dernier instantané (**commit**), soit ils sont **staged** maintenant (c'est-à-dire qu'ils sont dans la **zone de staging**).

Les **fichiers non suivis** sont tout le reste — tout fichier dans notre **répertoire de travail** qui n'était pas dans notre dernier instantané (**commit**) et qui n'est pas dans notre **zone de staging**.

# Comment Créer un Dépôt — La Méthode Conventionnelle

Assurons-nous de comprendre comment les termes que nous avons introduits se rapportent au processus de création d'un **dépôt**. Ce n'est qu'un aperçu rapide, avant de plonger beaucoup plus profondément dans ce processus.

Note — la plupart des articles avec des commandes shell montrent des commandes UNIX. Je fournirai des commandes pour Windows et UNIX, avec des captures d'écran de Windows, pour le bien de la variance. Lorsque les commandes sont exactement les mêmes, je les fournirai une seule fois.

Nous allons initialiser un nouveau **dépôt** en utilisant `git init repo_1`, puis changer notre répertoire pour celui du dépôt en utilisant `cd repo_1`. En utilisant `tree /f .git`, nous pouvons voir que l'exécution de `git init` a résulté en plusieurs sous-répertoires à l'intérieur de `.git`. (Le drapeau `/f` inclut les fichiers dans la sortie de `tree`).

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-51.png)

Créons un fichier à l'intérieur du répertoire `repo_1` :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-52.png)

Sur un système Linux :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-53.png)

Ce fichier est dans notre **répertoire de travail**. Pourtant, puisque nous ne l'avons pas ajouté à la **zone de staging**, il est actuellement **non suivi**. Vérifions en utilisant `git status` :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-54.png)
_Le nouveau fichier est non suivi car nous ne l'avons pas ajouté à la zone de staging, et il n'a pas été inclus dans un commit précédent_

Nous pouvons maintenant ajouter ce fichier à la **zone de staging** en utilisant `git add new_file.txt`. Nous pouvons vérifier qu'il a été staged en exécutant `git status` :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-55.png)
_Ajout du nouveau fichier à la zone de staging_

Nous pouvons maintenant créer un **commit** en utilisant `git commit` :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-56.png)

Quelque chose a-t-il changé dans le répertoire `.git` ? Exécutons `tree /f .git` pour vérifier :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-57.png)
_Beaucoup de choses ont changé dans `.git`_

Apparemment, beaucoup de choses ont changé. Il est temps de plonger plus profondément dans la structure de `.git` et de comprendre ce qui se passe sous le capot lorsque nous exécutons `git init`, `git add` ou `git commit`.

# Temps de devenir hardcore

Jusqu'à présent, nous avons couvert quelques fondamentaux de Git, et maintenant nous sommes prêts à vraiment _Git going._

Afin de comprendre profondément comment `git` fonctionne, nous allons créer un **dépôt**, mais cette fois — nous allons le construire à partir de zéro.

Nous n'utiliserons pas `git init`, `git add` ou `git commit`, ce qui nous permettra d'obtenir une meilleure compréhension pratique du processus.

# Comment Configurer `.git`

Créons un nouveau répertoire, et exécutons `git status` à l'intérieur :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-106.png)

D'accord, donc `git` semble mécontent car nous n'avons pas de dossier `.git`. La chose naturelle à faire serait de simplement créer ce répertoire :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-107.png)

Apparemment, créer un répertoire `.git` n'est tout simplement pas suffisant. Nous devons ajouter du contenu à ce répertoire.

**Un** **dépôt git a deux** principaux **composants** :

1. Une collection d'objets — **blobs**, **arbres,** et **commits**.
2. Un système de nommage de ces objets — appelé **références**.

Un **dépôt** peut également contenir d'autres choses, comme des hooks git, mais au minimum — il doit inclure des objets et des références.

Créons un répertoire pour les objets à `.git\objects` et un répertoire pour les références (en bref : **refs**) à `.git\refs` (sur les systèmes basés sur UNIX — `.git/objects` et `.git/refs`, respectivement).

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-108.png)

Un type de référence est les **branches**. En interne, `git` appelle les **branches** par le nom **heads**. Donc nous allons créer un répertoire pour elles — `.git\refs\heads`.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-109.png)

Cela ne change toujours pas notre `git status` :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-110.png)

Comment `git` sait-il où commencer lorsqu'il cherche un **commit** dans le **dépôt** ? Comme je l'ai expliqué précédemment, il cherche `HEAD`, qui pointe vers la branche active actuelle (ou **commit**, dans certains cas).

Donc, nous devons créer le `HEAD`, qui est simplement un fichier résidant à `.git\HEAD`. Nous pouvons appliquer ce qui suit :

Sur Windows : `> echo ref: refs/heads/master > .git\HEAD`

Sur UNIX : `$ echo "ref: refs/heads/master" > .git/HEAD`

✨ Nous savons maintenant comment `HEAD` est implémenté — c'est simplement un fichier, et son contenu décrit ce qu'il pointe.

Suite à la commande ci-dessus, `git status` semble changer d'avis :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-111.png)
_HEAD est juste un fichier_

Remarquez que `git` croit que nous sommes sur une branche appelée `master`, même si nous n'avons pas créé cette branche. Comme mentionné précédemment, `master` est juste un nom. Nous pourrions également faire croire à `git` que nous sommes sur une branche appelée `banana` si nous le voulions :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-112.png)
_🍌_

Nous reviendrons à `master` pour le reste de cet article, juste pour adhérer à la convention normale.

Maintenant que nous avons notre répertoire `.git` prêt, pouvons-nous travailler pour faire un **commit** (encore une fois, sans utiliser `git add` ou `git commit`).

# Commandes Plumbing vs Porcelain dans Git

À ce stade, il serait utile de faire une distinction entre deux types de commandes `git` : **plumbing** et **porcelain**. L'application des termes vient étrangement des toilettes (oui, celles-ci — 🚽), traditionnellement faites de porcelaine, et de l'infrastructure de plomberie (tuyaux et drains).

Nous pouvons dire que la couche porcelaine fournit une interface conviviale à la plomberie. La plupart des gens ne traitent qu'avec la porcelaine. Pourtant, lorsque les choses tournent (terriblement) mal, et que quelqu'un veut comprendre pourquoi, il devrait retrousser ses manches pour vérifier la plomberie. (Note : ces termes ne sont pas les miens, ils sont très largement utilisés dans `git`).

`git` utilise cette terminologie comme une analogie pour séparer les commandes de bas niveau que les utilisateurs n'ont généralement pas besoin d'utiliser directement (commandes "plumbing") des commandes de haut niveau plus conviviales (commandes "porcelain").

Jusqu'à présent, nous avons traité avec des commandes porcelaine — `git init`, `git add` ou `git commit`. Ensuite, nous passons aux commandes plumbing.

# Comment Créer des Objets dans Git

Commençons par créer un objet et l'écrire dans la base de données des objets de `git`, résidant dans `.git\objects`. Nous trouverons la valeur de hachage SHA-1 d'un **blob** en utilisant notre première commande plumbing, `git hash-object`, de la manière suivante :

Sur Windows :

`> echo git is awesome | git hash-object --stdin`

Sur UNIX :

`$ echo "git is awesome" | git hash-object --stdin`

En utilisant `--stdin`, nous instruisons `git hash-object` de prendre son entrée depuis l'entrée standard. Cela nous fournira la valeur de hachage pertinente.

Afin d'écrire réellement ce **blob** dans la base de données d'objets de `git`, nous pouvons simplement ajouter l'option `-w` pour `git hash-object`. Ensuite, nous pouvons vérifier le contenu du dossier `.git`, et voir qu'ils ont changé.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-113.png)
_Écriture d'un blob dans la base de données des objets_

Nous pouvons maintenant voir que le hachage de notre **blob** est — `54f6...36`. Nous pouvons également voir qu'un répertoire a été créé sous `.git\objects`, un répertoire nommé `54`, et à l'intérieur, un fichier portant le nom de `f6...36`.

Donc `git` prend en fait les deux premiers caractères du hachage SHA-1 et les utilise comme nom d'un répertoire. Les caractères restants sont utilisés comme nom de fichier pour le fichier qui contient réellement le **blob**.

Pourquoi est-ce ainsi ? Considérons un dépôt assez grand, qui a 300 000 objets (**blobs**, **arbres**, et **commits**) dans sa base de données. Pour rechercher un hachage dans cette liste de 300 000 hachages peut prendre un certain temps. Ainsi, `git` divise simplement ce problème par 256.

Pour rechercher le hachage ci-dessus, `git` chercherait d'abord le répertoire nommé `54` à l'intérieur du répertoire `.git\objects`, qui peut avoir jusqu'à 256 répertoires (`00` à `FF`). Ensuite, il rechercherait ce répertoire, en réduisant la recherche au fur et à mesure.

De retour à notre processus de génération d'un **commit**. Nous avons maintenant créé un objet. Quel est le type de cet objet ? Nous pouvons utiliser une autre commande plumbing, `git cat-file -t` (`-t` signifie "type"), pour vérifier cela :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-114.png)

Sans surprise, cet objet est un **blob**. Nous pouvons également utiliser `git cat-file -p` (`-p` signifie "pretty-print") pour voir son contenu :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-115.png)

Ce processus de création d'un **blob** se produit généralement lorsque nous ajoutons quelque chose à la **zone de staging** — c'est-à-dire lorsque nous utilisons `git add`.

Rappelons que `git` crée un **blob** du _fichier entier_ qui est staged. Même si un seul caractère est modifié ou ajouté (comme nous avons ajouté `!` dans notre exemple précédent), le fichier a un nouveau **blob** avec un nouveau **hachage**.

Y aura-t-il un changement dans `git status` ?

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-116.png)

Apparemment, non. Ajouter un objet **blob** à la base de données interne de `git` ne change pas le statut, car `git` ne connaît aucun fichier suivi ou non suivi à ce stade.

Nous devons suivre ce fichier — l'ajouter à la **zone de staging**. Pour ce faire, nous pouvons utiliser la commande plumbing `git update-index`, comme suit : `git update-index --add --cacheinfo 100644 <blob-hash> <filename>`.

Note : (Le `cacheinfo` est un mode de fichier 16 bits [tel que stocké par git](https://github.com/git/git/blob/master/Documentation/technical/index-format.txt), suivant la disposition des [types et modes POSIX](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sys_stat.h.html). Cela n'est pas dans le cadre de cet article).

L'exécution de la commande ci-dessus entraînera un changement dans le contenu de `.git` :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-117.png)

Pouvez-vous repérer le changement ? Un nouveau fichier nommé `index` a été créé. C'est lui — le célèbre **index** (ou **zone de staging**), est essentiellement un fichier qui réside dans `.git\index`.

Maintenant que notre **blob** a été ajouté à l'**index**, nous nous attendons à ce que `git status` ait l'air différent, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-118.png)

C'est intéressant ! Deux choses se sont passées ici.

Tout d'abord, nous pouvons voir que `new_file.txt` apparaît en vert, dans la zone `Changes to be committed`. C'est parce que l'**index** contient maintenant `new_file.txt`, en attente d'être commit.

Deuxièmement, nous pouvons voir que `new_file.txt` apparaît en rouge — parce que `git` croit que le _fichier_ `my_file.txt` a été supprimé, et le fait que le fichier a été supprimé n'est pas staged.

Cela se produit car nous avons ajouté le **blob** avec le contenu `git is awesome` à la base de données des objets, et avons dit à l'**index** que le fichier `my_file.txt` a le contenu de ce **blob**, mais nous n'avons jamais réellement créé ce fichier.

Nous pouvons facilement résoudre cela en prenant le contenu du **blob**, et en l'écrivant dans notre système de fichiers, dans un fichier appelé `my_file.txt` :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-119.png)

En conséquence, il n'apparaîtra plus en rouge par `git status` :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-120.png)

Il est maintenant temps de créer un objet **commit** à partir de notre **zone de staging**. Comme expliqué ci-dessus, un objet **commit** a une référence à un **arbre**, donc nous devons créer un **arbre**.

Nous pouvons faire cela avec la commande `git write-tree`, qui enregistre le contenu de l'**index** dans un objet **arbre**. Bien sûr, nous pouvons utiliser `git cat-file -t` pour voir qu'il s'agit bien d'un **arbre** :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-121.png)
_Création d'un objet arbre de l'index_

Et nous pouvons utiliser `git cat-file -p` pour voir son contenu :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-122.png)

Super, nous avons créé un **arbre**, et maintenant nous devons créer un objet **commit** qui référence cet **arbre**. Pour ce faire, nous pouvons utiliser `git commit-tree <tree-hash> -m <commit message>` :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-123.png)

Vous devriez maintenant vous sentir à l'aise avec les commandes utilisées pour vérifier le type de l'objet créé, et imprimer son contenu :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-124.png)
_Création d'un objet commit_

Notez que ce **commit** n'a pas de **parent**, car c'est le premier **commit**. Lorsque nous ajouterons un autre **commit**, nous devrons déclarer son **parent** — nous le ferons plus tard.

Le dernier hachage que nous avons obtenu — `80e...8f` — est un hachage de **commit**. Nous sommes en fait très habitués à utiliser ces hachages — nous les regardons tout le temps. Notez que ce **commit** possède un objet **arbre**, avec son propre hachage, que nous spécifions rarement explicitement.

Quelque chose changera-t-il dans `git status` ?

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-125.png)

Non 🤔.

Pourquoi est-ce ainsi ? Eh bien, pour savoir que notre fichier a été commit, `git` doit connaître le dernier **commit**. Comment `git` fait-il cela ? Il va à `HEAD` :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-126.png)
_Regardant `HEAD` sur Windows_

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-127.png)
_Regardant `HEAD` sur UNIX_

`HEAD` pointe vers `master`, mais qu'est-ce que `master` ? Nous ne l'avons pas vraiment créé encore.

Comme nous l'avons expliqué plus tôt dans cet article, une branche est simplement une référence nommée à un **commit**. Et dans ce cas, nous aimerions que `master` fasse référence au **commit** avec le hachage `80e8ed4fb0bfc3e7ba88ec417ecf2f6e6324998f`.

Nous pouvons y parvenir en créant simplement un fichier à `\refs\heads\master`, avec le contenu de ce hachage, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-128.png)

✨ En résumé, une **branche** est simplement un fichier à l'intérieur de `.git\refs\heads`, contenant un hachage du **commit** auquel elle fait référence.

Maintenant, enfin, `git status` et `git log` semblent apprécier nos efforts :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-129.png)

Nous avons réussi à créer un **commit** sans utiliser de commandes porcelaine ! À quel point c'est cool ? 🎉

# Comment Travailler avec les Branches dans Git — Sous le Capot

Tout comme nous avons créé un **dépôt** et un **commit** sans utiliser `git init`, `git add` ou `git commit`, nous allons maintenant créer et basculer entre des **branches** sans utiliser de commandes porcelaine (`git branch` ou `git checkout`).

Il est parfaitement compréhensible que vous soyez excité, moi aussi 😊

**Commençons :**

Jusqu'à présent, nous n'avons qu'une seule **branche**, nommée `master`. Pour en créer une autre avec le nom `test` (comme l'équivalent de `git branch test`), nous devrions simplement créer un fichier nommé `test` dans `.git\refs\heads`, et le contenu de ce fichier serait le même hachage de **commit** que celui vers lequel `master` pointe.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-130.png)

Si nous utilisons `git log`, nous pouvons voir que c'est effectivement le cas — `master` et `test` pointent tous deux vers ce **commit** :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-131.png)

Passons également à notre branche nouvellement créée (l'équivalent de `git checkout test`). Pour cela, nous devrions changer `HEAD` pour pointer vers notre nouvelle branche :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-132.png)
_Passage à la branche `test` en changeant `HEAD`_

Comme nous pouvons le voir, `git status` et `git log` confirment que `HEAD` pointe maintenant vers `test`, qui est donc la branche active.

Nous pouvons maintenant utiliser les commandes que nous avons déjà utilisées pour créer un autre fichier et l'ajouter à l'index :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-133.png)

En utilisant les commandes ci-dessus, nous avons créé un fichier nommé `test.txt`, avec le contenu `Testing`, créé un **blob** correspondant, et l'avons ajouté à l'**index**. Nous avons également créé un **arbre** représentant l'**index**.

Il est maintenant temps de créer un **commit** référençant cet **arbre**. Cette fois, nous devons également spécifier le _parent_ de ce **commit** — qui serait le **commit** précédent. Nous spécifions le parent en utilisant l'option `-p` de `git commit-tree` :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-136.png)

Nous venons de créer un **commit**, avec un **arbre** ainsi qu'un parent, comme nous pouvons le voir :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-139.png)

`git log` nous montrera-t-il le nouveau **commit** ?

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-138.png)

Comme nous pouvons le voir, `git log` ne montre rien de nouveau. Pourquoi est-ce ainsi ? 🤔 Souvenez-vous que `git log` suit les **branches** pour trouver les commits pertinents à afficher. Il nous montre maintenant `test` et le **commit** vers lequel il pointe, et il montre également `master` qui pointe vers le même **commit**.

C'est exact — nous devons changer `test` pour qu'il pointe vers notre nouveau **commit**. Nous pouvons faire cela en changeant simplement le contenu de `.git\refs\heads\test` :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-140.png)

Ça a marché ! 🎉🍾

`git log` va à `HEAD`, qui lui dit d'aller à la branche `test`, qui pointe vers le **commit** `465...5e`, qui renvoie à son **commit** parent `80e...8f`.

N'hésitez pas à admirer la beauté, nous vous avons _git_. 😊

# Résumé

Cet article vous a introduit aux internes de `git`. Nous avons commencé par couvrir les objets de base — **blobs**, **arbres,** et **commits**.

Nous avons appris qu'un **blob** contient le contenu d'un fichier. Un **arbre** est une liste de répertoires, contenant des **blobs** et/ou des sous-**arbres**. Un **commit** est un instantané de notre répertoire de travail, avec certaines métadonnées telles que l'heure ou le message de commit.

Nous avons ensuite discuté des **branches** et expliqué qu'elles ne sont rien d'autre qu'une référence nommée à un **commit**.

Nous avons continué en décrivant le **répertoire de travail**, un répertoire qui a un dépôt associé, la **zone de staging (index)** qui contient l'**arbre** pour le prochain **commit**, et le **dépôt**, qui est une collection de **commits**.

Nous avons clarifié comment ces termes se rapportent aux commandes `git` que nous connaissons en créant un nouveau dépôt et en committant un fichier en utilisant les bien connues `git init`, `git add`, et `git commit`.

Ensuite, nous avons plongé sans crainte dans `git`. Nous avons arrêté d'utiliser les commandes porcelaine et sommes passés aux commandes plumbing.

En utilisant `echo` et des commandes de bas niveau telles que `git hash-object`, nous avons pu créer un **blob**, l'ajouter à l'**index**, créer un **arbre** de l'**index**, et créer un objet **commit** pointant vers cet **arbre**.

Nous avons également pu créer et basculer entre des **branches**. Félicitations à ceux d'entre vous qui ont essayé cela par eux-mêmes ! 👏

Espérons qu'après avoir suivi cet article, vous avez l'impression d'avoir approfondi votre compréhension de ce qui se passe sous le capot lorsque vous travaillez avec `git`.

**Merci d'avoir lu !** Si vous avez apprécié cet article, vous pouvez en lire plus sur ce sujet sur le blog de [swimm.io](http://swimm.io/).

_[Omer Rosenbaum](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/), Directeur Technique de [Swimm](https://swimm.io/). Expert en formation cybernétique et fondateur de Checkpoint Security Academy. Auteur de_ [_Computer Networks (en hébreu)_](https://data.cyber.org.il/networks/networks.pdf)_._

_Visitez ma_ [_Chaîne YouTube_](https://www.youtube.com/watch?v=79jlgESHzKQ&list=PL9lx0DXCC4BMS7dB7vsrKI5wzFyVIk2Kg)_._

---

# Références supplémentaires

Beaucoup de choses ont été écrites et dites sur `git`. Plus précisément, j'ai trouvé ces références utiles :

* [Liste de lecture YouTube Git Internals — par Brief](https://www.youtube.com/playlist?list=PL9lx0DXCC4BNUby5H58y6s2TQVLadV8v7)
* [Conférence de Tim Berglund — « Git From the Bits Up »](https://www.youtube.com/watch?v=MYP56QJpDr4)
* [Git from the Bottom Up — par John Wiegley](https://jwiegley.github.io/git-from-the-bottom-up/)
* [comme promis, docs : git pour les confus](http://www.gelato.unsw.edu.au/archives/git/0512/13748.html)
* [Git Internals — Git Objects — du livre Pro Git, par Scott Chacon et Ben Straub](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)