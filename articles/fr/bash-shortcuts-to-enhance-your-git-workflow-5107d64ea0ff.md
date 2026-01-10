---
title: Raccourcis Bash pour améliorer votre flux de travail Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-18T22:15:54.000Z'
originalURL: https://freecodecamp.org/news/bash-shortcuts-to-enhance-your-git-workflow-5107d64ea0ff
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5RNo772LhsWxTO5LYqbTYw.jpeg
tags:
- name: Bash
  slug: bash
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Raccourcis Bash pour améliorer votre flux de travail Git
seo_desc: 'By Buddy Reno

  The more you work with Git, the faster you’ll learn its workflows.

  Here are some of the tasks that me and my team do daily:


  Create and name branches

  Count commits for squashing

  Update master to the latest version, then rebase it onto a...'
---

Par Buddy Reno

Plus vous travaillez avec Git, plus vous apprendrez rapidement ses flux de travail.

Voici quelques-unes des tâches que mon équipe et moi effectuons quotidiennement :

1. Créer et nommer des branches
2. Compter les commits pour les squasher
3. Mettre à jour la branche master vers la dernière version, puis la rebase sur une branche

Mais chacune de ces tâches nécessite plusieurs étapes. Cela m'a fait réfléchir : _il doit y avoir une meilleure façon de faire cela_.

Heureusement, il existe une meilleure façon ! En apprenant un peu de Bash, vous pouvez créer des alias Git qui vous feront gagner beaucoup de temps.

#### D'abord : le drapeau ! de Git

Avez-vous déjà vu un alias Git qui commence par un point d'exclamation ? Par exemple :

```
somealias = "!......some code"
```

Selon la [documentation](https://git-scm.com/docs/git-config#git-config-alias) de Git, _Si l'expansion de l'alias est précédée d'un point d'exclamation, elle sera traitée comme une commande shell_.

Hé, c'est génial ! Nous pouvons utiliser cela à notre avantage et ajouter un peu d'intelligence à nos alias. Essayons d'abord un exemple simple, puis augmentons la complexité.

Ouvrez votre fichier `~/.gitconfig` dans votre éditeur de texte préféré et ajoutez l'alias suivant :

```
hello = "!echo \"Hello World\""# (les barres obliques inverses servent à échapper les guillemets.)
```

Maintenant, lorsque vous exécutez `$ git hello` dans votre terminal, vous obtiendrez `Hello World` comme sortie. Super ! Armé de cette connaissance, parcourons les 3 exemples décrits ci-dessus et les alias que j'ai utilisés pour les accomplir.

#### Noms de branches cohérents

Alias :

```
newb = "!f() { ticketnum=$1; branchName=$2; git checkout -b \"POD-${ticketnum}/${branchName}\"; }; f"
```

Utilisation :

```
# Crée une nouvelle branche nommée POD-573/my-new-feature$ git newb 573 my-new-feature
```

Commandes clés :

* Fonction : `f(){}; f`
* Paramètres : `$1`, `$2`
* Interpolation de chaîne : `${ticketnum}`, `${branchName}`

Dans mon équipe, nous préfixons nos noms de branches pour correspondre au numéro de la carte dans notre système de ticketing. Par exemple : « POD-573/my-new-feature ». Cela fonctionne avec un hook de commit dans le système de ticketing pour lier les choses ensemble, il est donc important que nous respections ce système.

#### Fonction

En bash, vous pouvez écrire une fonction comme ceci : `FunctionName(){}; FunctionName`. Écrire le nom de la fonction après la déclaration de la fonction est ce qui exécute la fonction. Dans mes alias, j'ai raccourci le nom de la fonction à simplement `f` pour plus de brièveté.

Lorsque bash exécute `f`, il exécutera tout le code saisi entre les accolades `{}`. Dans ce cas, la fonction exécute `git checkout -b "MESSAGE"`.

#### Paramètres

Les paramètres sont ce qui suit immédiatement la commande. Par exemple, la commande de déplacement en bash :

```
$ mv ./file.txt ./folder/file.txt
```

Le premier paramètre que la commande de déplacement reçoit est `./file.txt`. Ce paramètre est automatiquement assigné à `$1` en bash.

De même, `./folder/file.txt` est assigné à `$2`. Dans la fonction d'alias, vous pouvez utiliser cette connaissance pour assigner des noms de variables plus significatifs pour ces paramètres.

```
# développé pour une meilleure lisibilité!f() { # beaucoup plus significatif! ticketnum=$1;  branchName=$2; git checkout -b \"POD-${ticketnum}/${branchName}\";};f
```

#### Interpolation de chaîne

Pour utiliser des variables en bash, vous placez simplement un signe dollar `$` devant le nom de la variable, comme : `$ticketnum`. Dans ce cas, la fonction interpole la variable dans une chaîne.

Bien que bash permette aux utilisateurs d'interpoler en utilisant directement la variable, je préfère utiliser la même syntaxe que de nombreux autres langages de programmation utilisent pour faire l'interpolation de chaîne `${variable}`.

En utilisant l'exemple d'utilisation ci-dessus, lorsque bash évalue `POD-${ticketnum}/${branchName}`, il se développera en `POD-573/my-new-feature`.

#### Compter les commits

Alias :

```
count = "!f() { compareBranch=${1-master}; git rev-list --count HEAD ^$compareBranch; }; f"
```

Utilisation :

```
# La branche a fait 5 commits depuis la branche master.$ git count # retourne 5# Passez un nom de branche pour vérifier au lieu de master$ git count dev
```

Commandes clés :

* Expansion de paramètre : `${1-DEFAULT}`
* Compter les révisions : `rev-list --count`

#### Expansion de paramètre

Similaire à l'interpolation de chaîne, remarquez que la variable `compareBranch` est maintenant assignée en utilisant la syntaxe `${}`. Cela vous permet de définir une valeur par défaut si aucun paramètre n'est passé à la commande. Dans l'alias, `compareBranch=${1-master}` utilisera master comme `compareBranch` si rien n'a été passé à la commande.

```
# suppose master$ git count# compareBranch est défini sur dev$ git count dev
```

Vous pouvez consulter la [documentation](http://www.gnu.org/software/bash/manual/bashref.html#Shell-Parameter-Expansion) de bash pour plus d'informations sur l'expansion de paramètre.

#### Compter les révisions

Par défaut, la commande `rev-list` de Git retournera les SHAs associés au nom de branche donné. En utilisant le drapeau `--count`, elle retournera plutôt le nombre total de commits pour cette branche particulière. Puisque le but est d'obtenir le nombre de _nouveaux_ commits depuis la branche à partir de master (ou une autre branche), vous devez passer un autre nom de branche avec l'opérateur `^`.

```
$ git rev-list --count HEAD ^master
```

Cette commande indique à git _Je veux le nombre de commits qui sont accessibles depuis HEAD (la branche actuelle) mais NON ACCESSIBLES depuis master._

Si vous avez fait 5 commits après avoir créé une branche à partir de master, la commande retournerait 5.

#### Squasher X Commits

Alias :

```
squashbase = "!f() { branchName=${1-master}; commitCount=$(git count $branchName); git rebase -i HEAD~$commitCount; }; f"
```

Utilisation :

```
# Obtenez le nombre de commits à squasher# et commencez un rebase interactif.$ git squashbase# passez un nom de branche optionnel.$ git squashbase dev
```

Commandes clés :

* Substitution de commande : `$(COMMAND)`

#### Substitution de commande

Celle-ci est amusante. Le script utilise à nouveau le `branchName` optionnel pour substituer une branche à master, mais le deuxième paramètre utilise une nouvelle syntaxe `$()`. Cela s'appelle la « substitution de commande ». Lorsque Bash voit une commande entre parenthèses, il évaluera cette instruction et utilisera la sortie comme valeur de la variable. Par exemple, `x=$(echo "Hello")` évaluera à `x` recevant la valeur de `Hello`.

Dans ce cas, l'alias rappelle l'alias `count` précédent pour obtenir le nombre de commits effectués depuis master. En supposant que la branche actuelle a fait 5 commits depuis la branche à partir de master, l'exécution de `$ git squashbase` évaluera à `$ git rebase -i HEAD~5`. Cette commande commence un rebase interactif avec les 5 derniers commits, vous donnant l'opportunité de nettoyer vos commits.

#### Mettre à jour Master et Rebase de la Branche

Alias :

```
pullbase = "!f() { branchName=${1-master}; git checkout $branchName && git pull && git checkout - && git rebase -i $branchName; }; f"
```

Utilisation :

```
# Vérifiez la branche, tirez-la, vérifiez la branche précédente et rebasez.$ git pullbase$ git pullbase dev
```

Commandes clés :

* Raccourci de tiret de Git : `-`
* Commande de contrôle : `&&`

#### Raccourci de tiret

Il n'y a pas grand-chose à expliquer ici. Basiquement, cela vous fera économiser _beaucoup de frappe_. Le tiret est une référence à la dernière branche que vous avez vérifiée — un peu comme le bouton de rappel sur une télécommande de télévision.

Considérez l'exemple suivant :

```
# actuellement sur la branche dev$ git checkout master # maintenant sur la branche master$ git checkout - # retour sur la branche dev.$ git checkout - # retour sur la branche master.
```

#### Commande de contrôle

Il existe de nombreuses façons d'enchaîner des opérations dans bash. Utiliser le double esperluette `&&` est l'une de mes préférées.

L'avantage de cette commande est qu'elle arrêtera le traitement si la commande précédente a échoué. Si git vérifie master mais échoue à tirer les dernières modifications, il s'arrêtera au lieu de continuer et de rebase des modifications potentiellement obsolètes dans votre branche.

L'alias ci-dessus exécutera alors les étapes suivantes, en s'arrêtant si l'une d'elles échoue :

1. Vérifiez la branche master (ou la branche donnée).
2. Mettez à jour vers la dernière version.
3. Vérifiez la branche sur laquelle vous étiez précédemment.
4. Rebasez la branche master dans votre branche actuelle.

Mon équipe exige que toutes nos demandes de tirage soient un seul commit avant de pouvoir être fusionnées dans master. Je exécute donc cette commande plusieurs fois par jour, et elle m'a fait gagner beaucoup de temps depuis que j'ai commencé à l'utiliser.

Vous pouvez lire à propos d'autres commandes de contrôle dans la [documentation](http://www.gnu.org/software/bash/manual/bashref.html#Lists-of-Commands) de Bash.

### Attendez, pourquoi utiliser un alias ?

Vous pourriez vous demander, « Ne devrais-je pas simplement écrire des scripts de profil bash ? »

Techniquement, vous pourriez faire cela. L'avantage ici est le _contexte_. Toutes ces commandes sont composées de diverses commandes Git. Une fonction dans votre profil bash s'exécutera partout où vous la tapez.

En créant ces scripts comme des alias Git, vous vous assurez que les commandes ne seront exécutées que dans un dépôt git. De plus, vous n'avez pas à préfixer vos noms de fonction avec `git-Function` ou `gitFunction` juste pour les « namespacer ». Si vous alliez faire cela, un alias Git est plus adapté.

J'espère que vous avez trouvé de l'inspiration dans mes raccourcis et appris comment vous pouvez créer les vôtres.

Si vous avez créé des alias préférés ou d'autres améliorations à votre propre flux de travail git, partagez-les dans la section des commentaires afin que nous puissions tous les explorer et potentiellement nous faire gagner beaucoup de temps et de frappe.