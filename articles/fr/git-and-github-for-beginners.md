---
title: Tutoriel Git et GitHub – Contrôle de version pour débutants
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2021-11-05T18:25:06.000Z'
originalURL: https://freecodecamp.org/news/git-and-github-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/g1117.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Tutoriel Git et GitHub – Contrôle de version pour débutants
seo_desc: "Git and GitHub are two technologies that every developer should learn,\
  \ irrespective of their field. \nIf you're a beginner developer, you might think\
  \ that these two terms mean the same thing – but they're different. \nThis tutorial\
  \ will help you unders..."
---

Git et GitHub sont deux technologies que chaque développeur devrait apprendre, quel que soit son domaine. 

Si vous êtes un développeur débutant, vous pourriez penser que ces deux termes signifient la même chose – mais ils sont différents. 

Ce tutoriel vous aidera à comprendre ce que sont Git et le contrôle de version, les commandes Git de base que vous devez connaître, comment vous pouvez utiliser ses fonctionnalités pour améliorer votre efficacité au travail, et comment étendre ces fonctionnalités en utilisant GitHub.

Ce guide est adapté aux débutants, car les exemples seront très faciles à comprendre. Il s'agira également d'un tutoriel généralisé afin que chacun puisse suivre, peu importe votre langage de programmation préféré. 

Pour notre projet, nous créerons une liste de tâches écrite dans un fichier texte (txt). Vous verrez comment nous pouvons utiliser les fonctionnalités de Git pour travailler et créer une version finale de la liste.

### Prérequis

Pour compléter ce tutoriel, vous aurez besoin des éléments suivants :

* Une interface de ligne de commande.
* Un éditeur de texte de votre choix (j'utiliserai VS Code).
* Un compte GitHub.

## Qu'est-ce que Git ?

Git est un système de contrôle de version qui vous permet de suivre les modifications que vous apportez à vos fichiers au fil du temps. Avec Git, vous pouvez revenir à divers états de vos fichiers (comme une machine à voyager dans le temps). Vous pouvez également créer une copie de votre fichier, apporter des modifications à cette copie, puis fusionner ces modifications avec la copie originale.

Par exemple, vous pourriez travailler sur la page d'accueil d'un site web et découvrir que vous n'aimez pas la barre de navigation. Mais en même temps, vous ne voulez peut-être pas commencer à modifier ses composants car cela pourrait empirer. 

Avec Git, vous pouvez créer une copie identique de ce fichier et jouer avec la barre de navigation. Ensuite, lorsque vous êtes satisfait de vos modifications, vous pouvez fusionner la copie avec le fichier original.

Vous n'êtes pas limité à utiliser Git uniquement pour les fichiers de code source – vous pouvez également l'utiliser pour suivre les fichiers texte ou même les images. Cela signifie que Git n'est pas seulement pour les développeurs – tout le monde peut le trouver utile.

### Comment installer Git

Pour utiliser Git, vous devez l'installer sur votre ordinateur. Pour ce faire, vous pouvez télécharger la dernière version sur le [site officiel](https://git-scm.com/downloads). Vous pouvez télécharger pour votre système d'exploitation parmi les options données. 

Vous pouvez également installer Git en utilisant la ligne de commande, mais comme les commandes varient selon chaque système d'exploitation, nous nous concentrerons sur l'approche plus générale.

### Comment configurer Git

Je vais supposer qu'à ce stade, vous avez installé Git. Pour vérifier cela, vous pouvez exécuter cette commande sur la ligne de commande : `git --version`. Cela vous montre la version actuelle installée sur votre PC. 

La prochaine chose que vous devrez faire est de définir votre nom d'utilisateur et votre adresse e-mail. Git utilisera ces informations pour identifier qui a apporté des modifications spécifiques aux fichiers. 

Pour définir votre nom d'utilisateur, tapez et exécutez ces commandes : `git config --global user.name "VOTRE_NOM_D_UTILISATEUR"` et `git config --global user.email "VOTRE_EMAIL"`. Assurez-vous simplement de remplacer `"VOTRE_NOM_D_UTILISATEUR"` et `"VOTRE_EMAIL"` par les valeurs que vous choisissez.

## Comment créer et initialiser un projet dans Git

Nous avons enfin terminé l'installation et la configuration de Git. Il est maintenant temps de créer notre projet. 

J'ai créé un dossier sur mon bureau appelé `Git and GitHub tutorial`. En utilisant la ligne de commande, naviguez jusqu'à l'emplacement de votre nouveau projet. Pour moi, j'exécuterais les commandes suivantes :

`cd desktop`

`cd Git and GitHub tutorial`

Si vous êtes nouveau dans la ligne de commande et que vous apprenez encore à l'utiliser pour naviguer sur votre PC, alors je vous suggérerais d'utiliser Microsoft's Visual Studio Code. Il s'agit d'un éditeur de code qui dispose d'un terminal intégré pour exécuter des commandes. Vous pouvez le télécharger [ici](https://code.visualstudio.com/download). 

Après avoir installé VS Code, ouvrez votre projet dans l'éditeur et ouvrez un nouveau terminal pour votre projet. Cela pointe automatiquement le terminal/la ligne de commande vers le chemin de votre projet.

Pour initialiser votre projet, exécutez simplement `git init`. Cela indiquera à Git de se préparer à commencer à surveiller vos fichiers pour chaque changement qui se produit. Cela ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot--95-.png)
_git init_

La première ligne contient des informations sur mon PC et le chemin où se trouve le dossier. La deuxième ligne est la commande `git init`, et la troisième ligne est la réponse envoyée me disant que mon dépôt (repo) a été initialisé. Il est considéré comme vide car nous n'avons pas encore dit à Git quels fichiers suivre. 

Un dépôt est simplement une autre façon de définir un projet surveillé/suivi par Git.

### Fichiers du projet Git

J'ai créé un seul fichier appelé `todo.txt`. Voici à quoi ressemble le fichier :

```txt
MA LISTE DE TÂCHES

1. Écrire un article.
2. Coder.
3. Étudier les livres.
4. Assister aux cours à l'heure.
5. Rendre visite à ma tante.
6. Postuler pour des emplois à distance. 
```

Avant de continuer avec l'apprentissage d'autres commandes Git, parlons de GitHub.

## Qu'est-ce que GitHub ?

GitHub est un service d'hébergement en ligne pour les dépôts Git. Imaginez travailler sur un projet à la maison et, alors que vous êtes absent, peut-être chez un ami, vous vous souvenez soudainement de la solution à une erreur de code qui vous a rendu inquiet pendant des jours. 

Vous ne pouvez pas apporter ces modifications car votre PC n'est pas avec vous. Mais si vous avez votre projet hébergé sur GitHub, vous pouvez accéder et télécharger ce projet avec une commande sur n'importe quel ordinateur auquel vous avez accès. Ensuite, vous pouvez apporter vos modifications et pousser la dernière version vers GitHub.

En résumé, GitHub vous permet de stocker votre dépôt sur leur plateforme. Une autre fonctionnalité géniale qui vient avec GitHub est la capacité de collaborer avec d'autres développeurs depuis n'importe quel endroit.

Maintenant que nous avons créé et initialisé notre projet localement, poussons-le vers GitHub. 

Si vous êtes débutant, vous rencontrerez certains nouveaux termes comme push, commit, add, et ainsi de suite – mais ne soyez pas submergé par eux. Avec un peu de pratique, vous serez en mesure de vous souvenir de ces termes et de ce qu'ils font.

## Comment pousser un dépôt vers GitHub

Je vais diviser cette section en étapes pour vous aider à comprendre le processus plus clairement.

### Étape 1 – Créer un compte GitHub

Pour pouvoir utiliser GitHub, vous devrez d'abord créer un compte. Vous pouvez le faire sur leur [site web](https://github.com/).

### Étape 2 – Créer un dépôt

Vous pouvez cliquer sur le symbole `+` dans le coin supérieur droit de la page, puis choisir "New repository". Donnez un nom à votre dépôt, puis faites défiler vers le bas et cliquez sur "Create repository".

### Étape 3 – Ajouter et commiter des fichier(s)

Avant d'"ajouter" et de "commiter" nos fichiers, vous devez comprendre les étapes d'un fichier suivi par Git. 

#### État commité

Un fichier est dans l'état **commité** lorsque toutes les modifications apportées au fichier ont été sauvegardées dans le dépôt local. Les fichiers dans l'étape commité sont des fichiers prêts à être poussés vers le dépôt distant (sur GitHub).

#### État modifié

Un fichier dans l'état **modifié** a subi certaines modifications mais il n'est pas encore sauvegardé. Cela signifie que l'état du fichier a été altéré par rapport à son état précédent dans l'état commité. 

#### État indexé

Un fichier dans l'état **indexé** signifie qu'il est prêt à être commité. Dans cet état, toutes les modifications nécessaires ont été apportées, donc la prochaine étape est de déplacer le fichier vers l'état commité. 

Vous pouvez mieux comprendre cela en imaginant Git comme un appareil photo. L'appareil photo ne prendra une photo que lorsque le fichier atteint l'état commité. Après cet état, l'appareil photo commence à comparer les modifications apportées au même fichier avec la dernière photo (c'est l'état modifié). Et lorsque les modifications requises ont été apportées, le fichier est indexé et déplacé vers l'état commité pour une nouvelle photo.

Cela peut être beaucoup d'informations à assimiler pour le moment, mais ne vous découragez pas – cela devient plus facile avec la pratique.

### Comment ajouter des fichiers dans Git

Lorsque nous avons initialisé notre projet pour la première fois, le fichier n'était pas suivi par Git. Pour ce faire, nous utilisons cette commande `git add .` Le point ou le point qui suit `add` signifie tous les fichiers qui existent dans le dépôt. Si vous souhaitez ajouter un fichier spécifique, peut-être un nommé `about.txt`, vous utilisez `git add about.txt`. 

Maintenant, notre fichier est dans l'état indexé. Vous n'obtiendrez pas de réponse après cette commande, mais pour savoir dans quel état se trouve votre fichier, vous pouvez exécuter la commande `git status`. 

### Comment commiter des fichiers dans Git

L'état suivant pour un fichier après l'état indexé est l'état commité. Pour commiter notre fichier, nous utilisons la commande `git commit -m "first commit"`. 

La première partie de la commande `git commit` indique à Git que tous les fichiers indexés sont prêts à être commités, il est donc temps de prendre une photo. La deuxième partie `-m "first commit"` est le message de commit. `-m` est l'abréviation de message tandis que le texte à l'intérieur des parenthèses est le message de commit. 

Après avoir exécuté cette commande, vous devriez obtenir une réponse similaire à celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot--97-.png)
_git commit_

Maintenant, notre fichier est dans l'état commité.

### Étape 4 – Pousser le dépôt vers GitHub

Après avoir créé le dépôt, vous devriez être redirigé vers une page qui vous indique comment créer un dépôt localement ou pousser un dépôt existant. 

Dans notre cas, le projet existe déjà localement, nous allons donc utiliser les commandes dans la section "…or push an existing repository from the command line". Voici les commandes :

```
git remote add origin https://github.com/ihechikara/git-and-github-tutorial.git
git branch -M main
git push -u origin main
```

La première commande `git remote add origin [https://github.com/ihechikara/git-and-github-tutorial.git](https://github.com/ihechikara/git-and-github-tutorial.git)` crée une connexion entre votre dépôt local et le dépôt distant sur GitHub. 

L'URL de votre projet distant devrait être entièrement différente de celle ci-dessus. Donc, pour suivre, assurez-vous de suivre les étapes et de travailler avec votre propre dépôt distant. Vous n'obtiendrez généralement pas de réponse après avoir exécuté cette commande, mais assurez-vous d'avoir une connexion Internet.

La deuxième commande `git branch -M main` change le nom de votre branche principale en "main". La branche par défaut pourrait être créée en tant que "master", mais "main" est le nom standard pour ce dépôt maintenant. Il n'y a généralement pas de réponse ici.

La dernière commande `git push -u origin main` pousse votre dépôt de votre appareil local vers GitHub. Vous devriez obtenir une réponse similaire à celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot--102-.png)
_git push_

Pour vous aider à approfondir votre compréhension des étapes des fichiers, je vais apporter des modifications au fichier puis pousser la nouvelle version vers GitHub.

Rappelons que notre fichier est maintenant dans l'état commité. Apportons des modifications au fichier et notons les états.

Je vais ajouter une nouvelle tâche à la liste de tâches :

```
MA LISTE DE TÂCHES

1. Écrire un article.
2. Coder.
3. Étudier les livres.
4. Assister aux cours à l'heure.
5. Rendre visite à ma tante.
6. Postuler pour des emplois à distance. 
7. Pratiquer le code
```

Après avoir ajouté la nouvelle tâche, exécutez la commande `git status`. Voici ce que vous devriez voir :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot--98-.png)
_git status_

Après avoir apporté des modifications au fichier, il est passé à l'état modifié – mais il n'est pas encore indexé pour le commit, donc vous ne pouvez pas encore le pousser vers GitHub. Git n'a pas encore pris de photo finale de cet état actuel, car il compare uniquement les modifications que nous avons apportées maintenant avec la dernière photo.

Maintenant, nous allons ajouter (indexer) ce fichier, puis le commiter et le pousser. C'est la même chose que dans la dernière section.

Nous ajoutons d'abord le fichier en utilisant `git add .` qui ajoute tous les fichiers dans le dossier (un fichier dans notre cas). Ensuite, nous committons le fichier en exécutant `git commit -m "added new task"` suivi de `git push -u origin main`. 

Ce sont les trois étapes pour pousser vos fichiers modifiés vers GitHub. Vous ajoutez, commitez, puis poussez. J'espère que vous comprenez maintenant les étapes des fichiers et les commandes qui leur sont associées.

## Comment utiliser les branches dans Git

Avec les branches, vous pouvez créer une copie d'un fichier sur lequel vous souhaitez travailler sans altérer la copie originale. Vous pouvez soit fusionner ces modifications avec la copie originale, soit laisser la branche rester indépendante. 

Avant de nous lancer dans l'utilisation des branches, je veux vous montrer une représentation visuelle de notre dépôt qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/g638.png)
_main banch_

L'image ci-dessus montre notre branche principale avec les deux derniers commits (le premier commit et le commit de la nouvelle tâche ajoutée). 

À ce stade, je veux ajouter plus de tâches à la liste, mais je ne suis pas encore sûr de vouloir les inclure dans ma liste principale. Je vais donc créer une nouvelle branche appelée `test` pour voir à quoi ressemblerait ma liste avec plus de tâches incluses.

Pour créer une nouvelle branche, exécutez cette commande : `git checkout -b test`. Je vais la décomposer. 

`checkout` indique à Git qu'il doit basculer vers une nouvelle branche. `-b` indique à Git de créer une nouvelle branche. `test` est le nom de la branche à créer et à basculer. Voici la réponse que vous devriez obtenir :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot--99-.png)
_git checkout -b_

Maintenant que nous avons créé une nouvelle branche, voici à quoi ressemblera notre dépôt :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/g664.png)
_git branch_

Nous avons créé la nouvelle branche à partir de l'état de notre dernier commit. Ajoutons maintenant plus de tâches à cette nouvelle branche.

```
MA LISTE DE TÂCHES

1. Écrire un article.
2. Coder.
3. Étudier les livres.
4. Assister aux cours à l'heure.
5. Rendre visite à ma tante.
6. Postuler pour des emplois à distance. 
7. Pratiquer le code
8. Terminer la tâche de stage.
9. Pratiquer les ouvertures aux échecs.
10. Résoudre des puzzles d'échecs.
11. Vérifier l'emploi du temps des examens. 
```

J'ai ajouté quatre nouvelles tâches. Pour fusionner le nouvel état avec la branche principale, vous devez d'abord indexer et commiter cette branche. Je ne vais pas entrer dans les détails sur la façon de le faire, car nous l'avons fait deux fois dans la dernière section. 

Vous devriez essayer de le faire vous-même pour comprendre comment cela fonctionne. En tant qu'indice, ajoutez le fichier, puis commitez avec un message (reportage à la section précédente pour les détails vous montrant comment faire cela).

Après avoir commité votre branche de test, revenez à la branche principale en exécutant cette commande : `git checkout main`.

Avez-vous remarqué que nous n'avons pas ajouté `-b` ? C'est parce que nous ne créons pas une nouvelle branche, mais que nous basculons vers une branche existante. Vous pouvez vérifier toutes les branches qui existent dans votre dépôt en exécutant la commande `git branch`.

Maintenant, nous pouvons fusionner les modifications que nous avons apportées dans la branche de test avec la branche principale en exécutant `git merge test`. À ce stade, vous verrez toutes les modifications apportées dans la branche de test reflétées sur la branche principale. Vous devriez également recevoir une réponse similaire à celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot--100-.png)
_git merge_

Voici une représentation visuelle de notre dépôt :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/g816.png)
_git merge_

Si vous continuez à pousser votre dépôt vers GitHub, vous verrez que la branche de test ne sera pas poussée. Elle ne restera que dans votre dépôt local. Si vous souhaitez pousser votre branche de test, basculez vers la branche en utilisant `git checkout test`, puis exécutez `git push -u origin test`.

## Comment tirer un dépôt dans Git

Tirer dans Git signifie cloner l'état actuel d'un dépôt distant dans votre ordinateur/dépôt. Cela s'avère utile lorsque vous souhaitez travailler sur votre dépôt à partir d'un autre ordinateur ou lorsque vous contribuez à un projet open source en ligne. 

Pour tester cela, ne vous inquiétez pas de basculer vers un nouvel ordinateur. Exécutez simplement `cd ..` pour quitter le répertoire actuel et revenir en arrière d'un pas. Dans mon cas, j'ai navigué jusqu'à mon bureau. 

Allez sur GitHub, et sur la page principale de votre dépôt, vous devriez voir un bouton vert qui dit "Code". Lorsque vous cliquez sur le bouton, vous devriez voir certaines options dans un menu déroulant. Allez-y et copiez l'URL HTTPS. 

Après cela, exécutez `git clone VOTRE_URL_HTTPS`. Cette commande tire le dépôt distant dans votre ordinateur local dans un dossier appelé git-and-git-tutorial. C'est-à-dire :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot--101-.png)
_git clone_

## Conclusion

Cet article a couvert les commandes de base qui vous aideront à commencer à utiliser Git. Nous avons également commencé à apprendre à utiliser GitHub. 

Si vous avez suivi jusqu'à ce point, alors félicitations, vous êtes prêt à partir. Vous pouvez maintenant utiliser Git dans vos projets, quel que soit le langage de programmation que vous utilisez. 

Vous devez savoir que ce ne sont pas toutes les commandes qui existent dans Git – alors n'hésitez pas à faire plus de recherches pour apprendre plus de commandes et leurs utilisations. [Cet article](https://www.freecodecamp.org/news/what-is-git-learn-git-version-control/) et [cette feuille de triche](https://www.freecodecamp.org/news/git-cheat-sheet/) sont d'excellents points de départ. [Ceci](https://gist.github.com/brandon1024/14b5f9fcfd982658d01811ee3045ff1e) est un excellent endroit pour voir une liste détaillée de plus de commandes Git.

Retrouvez-moi sur Twitter [@ihechikara2](https://twitter.com/Ihechikara2). Bon codage !