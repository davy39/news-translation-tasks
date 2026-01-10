---
title: 'Une introduction à Git : qu''est-ce que c''est et comment l''utiliser'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-12T18:02:47.000Z'
originalURL: https://freecodecamp.org/news/what-is-git-and-how-to-use-it-c341b049ae61
coverImage: https://cdn-media-1.freecodecamp.org/images/0*LU7AdfUTUviVY8DP
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: 'Une introduction à Git : qu''est-ce que c''est et comment l''utiliser'
seo_desc: 'By Aditya Sridhar

  Git is an Open Source Distributed Version Control System. Now that’s a lot of words
  to define Git.

  Let me break it down and explain the wording:


  Control System: This basically means that Git is a content tracker. So Git can be
  used...'
---

Par Aditya Sridhar

Git est un **Système de Contrôle de Version Distribué Open Source**. Voici beaucoup de mots pour définir Git.

Permettez-moi de le décomposer et d'expliquer la terminologie :

* **Système de Contrôle** : Cela signifie essentiellement que Git est un suiveur de contenu. Ainsi, Git peut être utilisé pour stocker du contenu — il est principalement utilisé pour stocker du code grâce aux autres fonctionnalités qu'il offre.
* **Système de Contrôle de Version** : Le code qui est stocké dans Git continue de changer à mesure que du code est ajouté. De plus, de nombreux développeurs peuvent ajouter du code en parallèle. Ainsi, le Système de Contrôle de Version aide à gérer cela en maintenant un historique des changements qui ont eu lieu. De plus, Git offre des fonctionnalités comme les branches et les fusions, que je couvrirai plus tard.
* **Système de Contrôle de Version Distribué** : Git dispose d'un dépôt distant qui est stocké sur un serveur et d'un dépôt local qui est stocké sur l'ordinateur de chaque développeur. Cela signifie que le code n'est pas seulement stocké sur un serveur central, mais qu'une copie complète du code est présente sur tous les ordinateurs des développeurs. Git est un Système de Contrôle de Version Distribué puisque le code est présent sur l'ordinateur de chaque développeur. J'expliquerai le concept de dépôts distants et locaux plus tard dans cet article.

### Pourquoi un Système de Contrôle de Version comme Git est nécessaire

Les projets réels ont généralement plusieurs développeurs travaillant en parallèle. Ainsi, un système de contrôle de version comme Git est nécessaire pour garantir qu'il n'y a pas de conflits de code entre les développeurs.

De plus, les exigences dans de tels projets changent souvent. Ainsi, un système de contrôle de version permet aux développeurs de revenir à une version antérieure du code.

Enfin, parfois plusieurs projets qui sont menés en parallèle impliquent la même base de code. Dans un tel cas, le concept de branchement dans Git est très important.

### Commençons à utiliser Git maintenant

Plutôt que de mentionner tous les concepts à la fois, je vais expliquer les concepts de Git à travers un exemple pour que ce soit plus facile à suivre.

#### Télécharger git

Ce lien contient des détails sur la façon d'installer Git sur plusieurs systèmes d'exploitation :
[https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Vérifiez si Git est installé en utilisant la commande suivante dans l'invite de commande :

```bash
git --version
```

#### Créez votre dépôt Git local

Sur votre ordinateur, créez un dossier pour votre projet. Appelons le dossier du projet `simple-git-demo`.

Allez dans votre dossier de projet et ajoutez un dépôt Git local au projet en utilisant les commandes suivantes :

```bash
cd simple-git-demo
git init
```

La commande `git init` ajoute un dépôt Git local au projet.

#### Ajoutons un peu de code maintenant

Créez un fichier appelé `demo.txt` dans le dossier du projet et ajoutez le texte suivant :

```
Contenu Initial
```

Ici, nous allons faire une démonstration avec du texte brut au lieu de code réel, puisque le principal sujet de cet article est Git et non un langage de programmation spécifique.

### Mise en scène et validation du code

La validation est le processus dans lequel le code est ajouté au **dépôt local**. Avant de valider le code, il doit être dans la **zone de mise en scène**. La zone de mise en scène est là pour suivre tous les fichiers qui doivent être validés.

Tout fichier qui n'est pas ajouté à la zone de mise en scène ne sera pas validé. Cela donne au développeur le contrôle sur les fichiers qui doivent être validés.

#### Mise en scène

Utilisez la commande suivante pour mettre en scène le fichier :

```bash
git add demo.txt
```

Si vous souhaitez ajouter plusieurs fichiers, vous pouvez utiliser :

`git add file1 file2 file3`

Si vous souhaitez ajouter tous les fichiers à l'intérieur de votre dossier de projet à la zone de mise en scène, utilisez la commande suivante :

```bash
git add .
```

Utilisez cela avec précaution car il ajoute tous les fichiers et dossiers de votre projet à la zone de mise en scène.

#### Validation

Utilisez la commande suivante pour valider le fichier :

```bash
git commit -m "Premier Commit"
```

"Premier Commit" est le message de validation ici. Entrez un message de validation pertinent pour indiquer quels changements de code ont été effectués dans cette validation particulière.

### État de Git et Journal de Git

Modifiez maintenant le fichier `demo.txt` et ajoutez le snippet suivant :

```
Contenu Initial Ajout de plus de Contenu
```

#### État

Utilisez `git status` pour obtenir des informations sur les fichiers modifiés et les fichiers présents dans la zone de mise en scène — il montre également d'autres informations, que nous pouvons ignorer pour l'instant.

Utilisez la commande suivante pour voir l'état :

```bash
git status
```

L'état montre que `demo.txt` est modifié et n'est pas encore dans la zone de mise en scène.

Maintenant, ajoutons `demo.txt` à la zone de mise en scène et validons-le en utilisant les commandes suivantes :

```bash
git add demo.txt git commit -m "Le fichier demo.txt est modifié"
```

### Journal

Utilisez `git log` pour imprimer tous les commits qui ont été effectués jusqu'à présent.

La commande utilisée pour cela est :
`git log`

Le journal montre l'auteur de chaque commit, la date du commit et le message du commit.

### Branches

Jusqu'à présent, nous n'avons créé aucune branche dans Git. Par défaut, les commits Git vont dans la branche **master**.

#### Qu'est-ce qu'une branche ?

Une branche n'est rien d'autre qu'un pointeur vers le dernier commit dans le dépôt Git. Ainsi, actuellement, notre branche master est un pointeur vers le deuxième commit « Le fichier demo.txt est modifié ».

#### Pourquoi plusieurs branches sont-elles nécessaires ?

Plusieurs branches sont nécessaires pour supporter plusieurs développements parallèles. Référez-vous à l'image ci-dessous pour voir comment les branches fonctionnent.

![Image](https://cdn-media-1.freecodecamp.org/images/sww3mboJ61C4kpLWlQYHnHWvrjX8p--VMui2)

Initialement, le commit 1 et le commit 2 ont été effectués dans la branche master. Après le commit 2, une nouvelle branche appelée « Test » est créée, et le commit 3 et le commit 4 sont ajoutés à la branche de test.

En même temps, un commit 3 et un commit 4 différents sont ajoutés à la branche master. Ici, nous pouvons voir qu'après le Commit 2, deux développements parallèles sont effectués dans 2 branches séparées.

La branche de test et la branche master ont divergé ici et ont un code différent — le code de la branche de test peut être fusionné avec la branche master en utilisant `git merge`. Cela sera couvert plus tard.

#### Créer une nouvelle branche en local

Créez une nouvelle branche appelée **test** en utilisant la commande suivante :

```bash
git branch test
```

Cette commande crée la branche `test`.

Nous sommes toujours dans le contexte de la branche master. Pour passer à la branche `test`, utilisez la commande suivante :

```bash
git checkout test
```

Maintenant, nous sommes dans la branche `test`.

Vous pouvez lister toutes les branches en local en utilisant la commande suivante :

```bash
git branch
```

#### Faire quelques commits dans la nouvelle branche

Modifiez `demo.txt` en ajoutant le snippet suivant :

```
Contenu Initial Ajout de plus de Contenu Ajout de contenu depuis la branche test
```

Maintenant, mettez en scène et validez en utilisant les commandes suivantes :

```bash
git add demo.txt git commit -m "Commit de la branche test"
```

Ce commit a été effectué dans la branche de test, et maintenant la branche de test est en avance sur la branche master d'un commit — car la branche de test inclut également les 2 commits de la branche master.

Vous pouvez vérifier l'historique des commits dans la branche de test en utilisant :

```bash
git log
```

### Fusion

Actuellement, la branche de test est en avance sur la branche master d'un commit. Supposons maintenant que nous voulons que tout le code de la branche de test soit ramené dans la branche master. C'est là que `git merge` est très utile.

Pour fusionner le code de la branche de test dans la branche master, suivez ces étapes :

D'abord, retournez à la branche master :

```bash
git checkout master
```

Ensuite, exécutez la commande `merge` :

```bash
git merge test
```

Après avoir exécuté ces 2 commandes, la fusion devrait être réussie. Dans cet exemple, il n'y a pas de conflits.

Mais dans les projets réels, il y aura des conflits lors d'une fusion. La résolution des conflits est quelque chose qui vient avec l'expérience, donc à mesure que vous travaillerez plus avec Git, vous pourrez vous habituer à résoudre les conflits.

Exécutez `git log` maintenant et vous remarquerez que la branche master a également 3 commits.

### Le dépôt Git distant

Jusqu'à présent, nous avons travaillé uniquement dans le dépôt local. Chaque développeur travaillera dans son dépôt local, mais finalement, ils pousseront le code dans un dépôt distant. Une fois le code dans le dépôt distant, d'autres développeurs peuvent voir et modifier ce code.

![Image](https://cdn-media-1.freecodecamp.org/images/O-6UdGYVsEjM-oJmtJ5KQpQnXIBOCZoB22X1)
_Montrant les dépôts distants et locaux_

#### GitHub

Ici, nous utiliserons GitHub pour le dépôt distant.

Allez sur [https://github.com/](https://github.com/) et créez un compte.

Après vous être inscrit sur la page d'accueil de GitHub, cliquez sur **Démarrer un projet** pour créer un nouveau dépôt Git. Donnez un nom au dépôt et cliquez sur « Créer un dépôt »

Donnez le nom `git-blog-demo`.

Cela créera un dépôt distant dans GitHub, et lorsque vous ouvrirez le dépôt, une page comme l'image ci-dessous s'ouvrira :

![Image](https://cdn-media-1.freecodecamp.org/images/LWpWCg5LTo7m-IkZW1io-194VWZ61di5CIGY)

L'URL du dépôt est la partie surlignée `**https://github.com/aditya-sridhar/git-blog-demo.git**`

Pour pointer votre dépôt local vers le dépôt distant, utilisez la commande suivante :

```bash
git remote add origin [url du dépôt]
```

#### **Git Push**

Pour pousser tout le code du dépôt local vers le dépôt distant, utilisez la commande suivante :

```bash
git push -u origin master
```

Cela pousse le code de la branche master dans le dépôt local vers la branche master dans le dépôt distant.

### Commandes supplémentaires

#### Git Pull

`git pull` est utilisé pour tirer les derniers changements du dépôt distant vers le dépôt local. Le code du dépôt distant est mis à jour en continu par divers développeurs, d'où la nécessité de `git pull` :

```bash
git pull origin master
```

#### Git Clone

`git clone` est utilisé pour cloner un dépôt distant existant sur votre ordinateur. La commande pour cela est :

```bash
git clone [url du dépôt]
```

### Félicitations

Maintenant, vous connaissez les bases de l'utilisation de Git, alors allez-y et explorez davantage !

Je publierai bientôt un autre article sur des concepts légèrement plus avancés de Git. Restez à l'écoute !

### À propos de l'auteur

J'aime la technologie et je suis les avancées technologiques. J'aime aussi aider les autres avec les connaissances que j'ai dans le domaine de la technologie.

N'hésitez pas à me contacter sur mon compte LinkedIn [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

Vous pouvez aussi me suivre sur Twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

Mon site web : [https://adityasridhar.com/](https://adityasridhar.com/)

### Autres articles de moi

[Comment utiliser Git efficacement](https://www.freecodecamp.org/news/how-to-use-git-efficiently-54320a236369/)