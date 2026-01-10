---
title: Guide du débutant pour Git — Qu'est-ce qu'un journal des modifications et comment
  le générer
subtitle: ''
author: Gaël Thomas
co_authors: []
series: null
date: '2020-04-01T09:36:56.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-git-what-is-a-changelog-and-how-to-generate-it
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/what-is-a-changelog-and-how-to-generate-it.png
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Guide du débutant pour Git — Qu'est-ce qu'un journal des modifications
  et comment le générer
seo_desc: 'Say you are a developer, and you use Git for one of your projects. You
  want to share the changes you made with your users, but you don’t know how. Well,
  then this article is for you.

  In the last part of this series, I shared with you how to write a g...'
---

Disons que vous êtes un développeur et que vous utilisez Git pour l'un de vos projets. Vous souhaitez partager les modifications que vous avez apportées avec vos utilisateurs, mais vous ne savez pas comment. Eh bien, cet article est fait pour vous.

Dans la dernière partie de cette série, je vous ai partagé [comment écrire un bon message de commit](https://herewecode.io/blog/a-beginners-guide-to-git-how-to-write-a-good-commit-message/).

Je vous ai donné un aperçu des avantages d'écrire un bon commit, et j'ai mentionné la possibilité de générer un journal des modifications.

Dans cet article, vous apprendrez ce qu'est un journal des modifications ainsi que deux façons de le générer — une simple et une sophistiquée.  


## Qu'est-ce qu'un journal des modifications ?

Un journal des modifications est un fichier qui partage une liste chronologiquement ordonnée des modifications que vous avez apportées à votre projet. Il est souvent organisé par version avec la date suivie d'une liste de fonctionnalités ajoutées, améliorées et supprimées.

Globalement, il existe deux façons d'écrire un journal des modifications :

* la manière habituelle : créer un fichier texte et commencer à énumérer toutes vos modifications avec une date spécifique
* le choix du développeur (alias l'option paresseuse) : auto-générer votre journal des modifications à partir de vos messages de commit. J'ai une bonne nouvelle pour vous — c'est ce que vous allez apprendre dans cet article !

> « Un journal des modifications est un journal ou un enregistrement de toutes les modifications notables apportées à un projet. Le projet est souvent un site web ou un projet logiciel, et le journal des modifications inclut généralement des enregistrements de modifications telles que des corrections de bugs, de nouvelles fonctionnalités, etc. » — [Wikipedia](https://en.wikipedia.org/wiki/Changelog)

### Pourquoi est-ce essentiel ?

Je pense que, même maintenant, vous vous demandez pourquoi c'est essentiel et pourquoi vous devriez prendre le temps de le créer.

Un journal des modifications est une sorte de résumé de toutes vos modifications. Il devrait être facile à comprendre à la fois par les utilisateurs utilisant votre projet et les développeurs travaillant dessus.

Dans un monde où tout évolue rapidement, un utilisateur a besoin de savoir si le site web/logiciel qu'il utilise est en train de changer. Vous pourriez être surpris, mais les gens aiment lire des articles de blog ou une page de mise à jour sur votre site web.

Pour un développeur, par exemple, si le projet est grand, il peut être intéressant de savoir comment le logiciel sur lequel il travaille évolue.

Ou si vous travaillez sur un projet open-source, vous pouvez trouver un fichier « CHANGELOG.md » dans le dépôt GitHub. Ce fichier vise à informer les contributeurs des dernières mises à jour du projet. 

![Image](https://www.freecodecamp.org/news/content/images/2020/07/angularjs-changelog.png)
_CHANGELOG.md du [dépôt GitHub Angular.js](https://github.com/angular/angular/blob/master/CHANGELOG.md)_

### Où les trouve-t-on ?

Les journaux des modifications sont partout ! D'accord, ils ont souvent différents styles et emplacements, mais ils sont littéralement sur chaque projet.

J'ai créé une courte liste avec quelques endroits où vous pouvez trouver un journal des modifications.

* Un article de blog. Un journal des modifications peut être livré sous forme d'article partageant les dernières fonctionnalités point par point.
* Un fichier « CHANGELOG.md » dans un dépôt GitHub.
* Une section Journal des modifications sur votre site web/logiciel préféré. Voici [un exemple avec l'outil de gestion des tâches TickTick](https://ticktick.com/public/changelog/en.html).
* Dans « Quoi de neuf » sur le store Android et iOS.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ticktick-android-changelog.png)
_Section « Quoi de neuf » de TickTick sur Android_

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ticktick-ios-changelog.png)
_Section « Quoi de neuf » de TickTick sur iOS_

## Génération automatique du journal des modifications 

Dans cette partie, nous allons générer notre premier journal des modifications ensemble.

En effectuant cette tâche, vous comprendrez pourquoi il peut être utile de commiter en suivant certaines règles.

Un commit excellent et explicite n'a pas besoin d'être modifié et peut être directement ajouté au journal des modifications.

Si vous êtes intéressé par la génération d'un fichier nécessaire sans aucune personnalisation ou embellissement, je recommande la première méthode ; sinon, la deuxième est meilleure.

**Note** : Certains sites web comme [Keep A Changelog](https://keepachangelog.com/) expliquent que vous ne devriez pas faire un journal des modifications uniquement en copiant et collant vos commits git (référez-vous à la méthode simple). En effet, je recommande d'essayer d'éviter cette méthode si vous travaillez sur un produit professionnel. 

Cependant, de nos jours, il existe des générateurs avancés qui vous permettent de transformer vos logs git en journaux des modifications (référez-vous à la méthode sophistiquée).

### Comment générer un journal des modifications (la méthode simple)

En utilisant cette première méthode, vous n'avez besoin d'aucun prérequis. Tout ce dont vous avez besoin est de taper quelques commandes à l'intérieur de votre dépôt Git.

Pour rappel, lorsque vous tapez « git log », une liste de tous vos commits est affichée.

```
$ git log

// Sortie
commit f6986f8e52c1f889c8649ec75c5abac003102999 (HEAD -> master, origin/master, origin/HEAD)
Author: Sam Katakouzinos <sam.katakouzinos@gmail.com>
Date:   Tue Mar 10 11:41:18 2020 +1100

    docs(developers): commit message format typo
    
    Any line of the commit message cannot be longer *than* 100 characters!
    
    Closes #17006

commit ff963de73ab8913bce27a1e75ac01f53e8ece1d9
Author: Chives <chivesrs@gmail.com>
Date:   Thu Feb 6 19:05:57 2020 -0500

    docs($aria): get the docs working for the service
    
    Closes #16945

commit 2b28c540ad7ebf4a9c3a6f108a9cb5b673d3712d
Author: comet <hjung524@gmail.com>
Date:   Mon Jan 27 19:49:55 2020 -0600

    docs(*): fix spelling errors
    
    Closes #16942
```

Cette commande peut prendre quelques paramètres. Nous allons les utiliser pour changer la sortie et obtenir une sortie améliorée pour générer notre journal des modifications.

En tapant la commande suivante, vous aurez une sortie avec un commit par ligne.

```
$ git log --oneline --decorate

// Sortie
f6986f8e5 (HEAD -> master, origin/master, origin/HEAD) docs(developers): commit message format typo
ff963de73 docs($aria): get the docs working for the service
2b28c540a docs(*): fix spelling errors
68701efb9 chore(*): fix serving of URI-encoded files on code.angularjs.org
c8a6e8450 chore(package): fix scripts for latest Node 10.x on Windows
0cd592f49 docs(angular.errorHandlingConfig): fix typo (wether --> whether)
a4daf1f76 docs(angular.copy): fix `getter`/`setter` formatting
be6a6d80e chore(*): update copyright year to 2020
36f17c926 docs: add mention to changelog
ff5f782b2 docs: add mention to changelog
27460db1d docs: release notes for 1.7.9
add78e620 fix(angular.merge): do not merge __proto__ property
```

C'est mieux, mais voyons ce que nous pouvons faire avec la suivante.

```
$ git log --pretty="%s"

// Sortie
docs(developers): commit message format typo
docs($aria): get the docs working for the service
docs(*): fix spelling errors
chore(*): fix serving of URI-encoded files on code.angularjs.org
chore(package): fix scripts for latest Node 10.x on Windows
docs(angular.errorHandlingConfig): fix typo (wether --> whether)
docs(angular.copy): fix `getter`/`setter` formatting
chore(*): update copyright year to 2020
docs: add mention to changelog
docs: add mention to changelog
docs: release notes for 1.7.9
fix(angular.merge): do not merge __proto__ property
```

Avec celle-ci, vous pouvez imprimer la liste des commits avec le style que vous voulez.

Le « %s » correspond au titre du commit lui-même. Vous pouvez modifier la chaîne pour styliser votre commit comme vous le souhaitez.

Dans notre cas, nous voulons créer une liste.

```
$ git log --pretty="- %s"

// Sortie
- docs(developers): commit message format typo
- docs($aria): get the docs working for the service
- docs(*): fix spelling errors
- chore(*): fix serving of URI-encoded files on code.angularjs.org
- chore(package): fix scripts for latest Node 10.x on Windows
- docs(angular.errorHandlingConfig): fix typo (wether --> whether)
- docs(angular.copy): fix `getter`/`setter` formatting
- chore(*): update copyright year to 2020
- docs: add mention to changelog
- docs: add mention to changelog
- docs: release notes for 1.7.9
- fix(angular.merge): do not merge __proto__ property
```

Vous l'avez fait ! Vous avez créé un journal des modifications simple.

**Note** : Si vous voulez aller plus loin et sauvegarder votre journal des modifications plus rapidement : au lieu de copier et coller le résultat dans un fichier, redirigez-le vers votre terminal en tapant « git log --pretty="- %s" > CHANGELOG.md »

### Comment générer un journal des modifications (la méthode sophistiquée)

**Prérequis**

Nous allons maintenant explorer une méthode sophistiquée pour générer un journal des modifications. L'idée derrière le processus reste la même, mais cette fois nous allons utiliser d'autres outils pour nous aider.

Vous vous souvenez lorsque [dans la dernière partie de cette série](https://herewecode.io/blog/a-beginners-guide-to-git-how-to-write-a-good-commit-message/) j'ai écrit sur les directives Git ?

**Note** : Les directives Git sont un ensemble de règles pour écrire vos commits de manière plus efficace. Ces directives vous aident à ajouter une certaine structure à vos commits.

Lorsque vous utilisez une directive pour votre projet, vous pouvez utiliser des outils pour générer un journal des modifications. La plupart du temps, ces outils sont meilleurs car ils vous permettent de créer un journal des modifications formaté en markdown.

Dans cet exemple, nous allons utiliser un générateur simple qui fonctionne avec la plupart des directives. Son nom est « [generate-changelog](https://github.com/lob/generate-changelog) », et il est disponible sur NPM (le gestionnaire de paquets Node).

Cet outil va créer un journal des modifications stylisé, mais ce n'est pas celui avec le plus de fonctionnalités. J'ai décidé de l'utiliser car c'est un excellent exemple pour un débutant. Si vous voulez aller plus loin, veuillez vous référer à la liste des outils de journal des modifications ci-dessous :

Voici quelques outils que vous pouvez utiliser :

* [Github Changelog Generator](https://github.com/github-changelog-generator/github-changelog-generator)
* [Git Chglog](https://github.com/git-chglog/git-chglog)
* [Auto Changelog](https://github.com/CookPete/auto-changelog)
* [Conventional Changelog](https://github.com/conventional-changelog/conventional-changelog)

> Note : Avant d'installer l'outil, vous devez avoir NPM installé sur votre ordinateur. Si vous ne l'avez pas, je vous invite à [suivre le site officiel](https://www.npmjs.com/get-npm) (il vous aidera à installer Node et NPM).

Pour installer le package sur votre ordinateur, tapez la commande suivante dans votre terminal.

```
$ npm install generate-changelog -g 
```

Une fois que vous avez fait cela, c'est installé !

**Comment l'utiliser**

Pour faire fonctionner ce package, vous devez suivre les directives pour utiliser ce modèle — « type(catégorie) : description [flags] ». Dans cet exemple, j'utiliserai le dépôt GitHub Angular.js.

Maintenant, vous pouvez taper la commande generate dans votre terminal à l'intérieur de votre dépôt GitHub.

```
$ changelog generate
```

Un fichier « CHANGELOG.md » sera automatiquement créé et rempli avec vos logs dans un format markdown.

Vous pouvez trouver un exemple de la sortie (avec un lecteur markdown tel que GitHub) ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/generate-changelog-example.png)
_Journal des modifications auto-généré avec l'outil generate-changelog_

## Conclusion

J'espère que vous avez aimé ce guide et que vous comprenez maintenant comment créer un journal des modifications pour votre projet. Je pense que c'est une bonne façon de démontrer pourquoi vous devriez écrire de bons messages de commit.

N'hésitez pas à essayer d'autres générateurs de journal des modifications et envoyez-moi le résultat !

Si vous avez des questions ou des commentaires, n'hésitez pas à me le faire savoir. 

Si vous voulez plus de contenu comme celui-ci, vous pouvez [me suivre sur Twitter](https://twitter.com/gaelgthomas/), où je tweete sur le développement web, l'amélioration de soi et mon parcours en tant que développeur full stack !