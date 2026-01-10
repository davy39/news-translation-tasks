---
title: Apprendre Git et GitHub en espagnol – Cours pour débutants
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2023-02-09T15:25:52.000Z'
originalURL: https://freecodecamp.org/news/learn-git-and-github-in-spanish-course-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/thumbnail-v4.png
tags:
- name: Español
  slug: espanol-2
- name: freeCodeCamp.org
  slug: freecodecamp
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: online courses
  slug: online-courses
seo_title: Apprendre Git et GitHub en espagnol – Cours pour débutants
seo_desc: 'Hi! If you speak Spanish and you want to learn Git and GitHub, you are
  in the right place.

  In this article, you will find a brief introduction to Git and GitHub. You will
  learn why they are very powerful tools and why you should learn them if your go...'
---

Salut ! Si vous parlez espagnol et que vous souhaitez apprendre Git et GitHub, vous êtes au bon endroit.

Dans cet article, vous trouverez une brève introduction à Git et GitHub. Vous découvrirez pourquoi ce sont des outils très puissants et pourquoi vous devriez les apprendre si votre objectif est de devenir développeur.

Ensuite, vous trouverez un cours de **5+ heures** sur Git et GitHub sur la chaîne YouTube espagnole de freeCodeCamp, où vous pourrez apprendre les bases en espagnol avec des exemples pratiques et des projets.

Si vous avez des amis hispanophones, vous êtes invité à partager la **[version espagnole de cet article](https://www.freecodecamp.org/espanol/news/aprende-git-y-github-curso-desde-cero)** avec eux.

Commençons ! ✨

## **🔸** Qu'est-ce que le contrôle de version ?

Tout d'abord, voyons ce qu'est le contrôle de version, car ce concept est essentiel pour Git et GitHub.

N'avez-vous jamais souhaité pouvoir suivre les modifications que vous avez apportées à un projet ou même revenir à une version précédente d'un fichier ?

Laissez-moi vous dire que cela est possible avec le contrôle de version.

Avec un système de contrôle de version, vous pouvez suivre les modifications que vous apportez à vos fichiers et conserver plusieurs versions de votre projet sur le même ordinateur simultanément. Ainsi, vous pouvez basculer entre différentes versions de votre projet au fur et à mesure que vous apportez des modifications et créez de nouvelles fonctionnalités.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-30-at-6.42.42-PM.png)

C'est la puissance du contrôle de version.

Vous pouvez conserver une version "expérimentale" de votre projet pour travailler sur une nouvelle fonctionnalité tout en ayant la version stable de votre projet en ligne pour vos utilisateurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-02-at-3.31.46-PM.png)

Deux des outils de contrôle de version les plus populaires dans la communauté mondiale des développeurs sont **Git et GitHub**. Commençons par un bref aperçu de Git.

## **🔹** Qu'est-ce que Git ?

Git est l'un des systèmes de contrôle de version les plus populaires parmi la communauté des développeurs. Je vous promets que l'apprentissage de Git en vaudra totalement la peine si votre objectif est de devenir développeur de logiciels.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-31-at-2.46.12-PM.png)
_Git (logo officiel)._

Avec Git, vous pouvez suivre les modifications que vous apportez à vos fichiers et travailler avec différentes versions de votre projet sur le même ordinateur.

En apprenant quelques commandes Git importantes, vous pouvez vous concentrer sur vos projets de développement de logiciels tandis que Git s'occupe des détails internes de toutes les tâches importantes de contrôle de version.

### ⬢ **Concepts de base de Git**

Maintenant que vous savez ce qu'est Git, voyons quelques concepts essentiels pour travailler avec Git :

#### Référentiel Git

Un référentiel est l'endroit où Git stocke nos fichiers de projet et suit leurs différentes versions. Un référentiel peut être local ou distant.

Un référentiel local est stocké localement sur votre ordinateur. Un référentiel distant est stocké à distance sur les serveurs du service d'hébergement de votre choix (comme, par exemple, GitHub).

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-02-at-10.57.53-AM.png)

#### Répertoire de travail

Le répertoire de travail est le répertoire du projet dans notre système de fichiers où les fichiers sont stockés. C'est, par exemple, le dossier que vous ouvrez dans votre éditeur de code ou IDE pour travailler avec vos fichiers.

#### Zone de préparation

La zone de préparation contient l'ensemble des fichiers et des modifications qui seront inclus dans le prochain commit (un enregistrement des modifications apportées au référentiel). Nous pouvons ajouter et supprimer des fichiers de cette zone si nécessaire.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-02-at-11.01.34-AM.png)

#### Commit

Un commit est comme un "instantané" de votre projet à un moment particulier. Un commit enregistre les modifications qui ont été apportées au projet. Vous choisissez quand créer un commit et ce qu'il doit inclure.

**💡 Conseil :** Pour décrire les modifications enregistrées dans un commit, nous écrivons un message de commit que nous pouvons vérifier plus tard en travaillant sur le projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/commits.png)

#### Branche

Une branche est une ligne de développement indépendante d'un projet suivie par Git. Chaque projet commence avec une branche par défaut que nous appelons généralement `**main**`. Nous pouvons créer une nouvelle branche pour travailler sur une nouvelle fonctionnalité sans affecter la version principale de notre projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/branch.png)

#### Fusion

Nous pouvons également combiner (fusionner) des branches lorsque nous devons incorporer les modifications apportées sur une branche dans une autre. C'est ce que nous faisons généralement lorsqu'une nouvelle fonctionnalité est prête à être ajoutée à la version en ligne de notre projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/merge.png)

Ce sont des concepts fondamentaux pour travailler avec Git. Maintenant, voyons l'outil en ligne de commande réel avec lequel nous allons travailler.

### ⬢ **Git Bash**

Pendant le cours, nous utiliserons Git Bash, un outil en ligne de commande pour Windows qui fournit un environnement où nous pouvons exécuter des commandes Git.

**💡 Conseil :** Bash signifie Bourne Again Shell. Un bash est une application utilisée pour interagir avec le système d'exploitation d'un ordinateur via des commandes.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-387.png)
_Capture d'écran de Git Bash (Windows)_

Super ! Maintenant que vous en savez plus sur Git, commençons à plonger dans les bases de GitHub. Git et GitHub fonctionnent ensemble pour créer le flux de travail que les développeurs de logiciels utilisent chaque jour.

## **🔸** Qu'est-ce que GitHub ?

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-02-at-11.02.14-AM.png)
_[Page d'accueil officielle de GitHub](https://github.com/)_

Lorsque vous travaillez avec Git, tout ce que vous stockez dans votre référentiel est uniquement stocké localement. Seuls vous pouvez avoir accès à votre référentiel et à vos modifications.

Cela peut être exactement ce dont vous avez besoin si vous travaillez sur un projet personnel.

Cependant, si vous faites partie d'une équipe, vous devrez collaborer avec d'autres développeurs pour modifier la même base de code, ce qui peut être très problématique s'il n'y a aucun moyen d'avoir un accès rapide aux modifications apportées par d'autres développeurs.

C'est là que GitHub vient à la rescousse !

Lorsque vous créez un référentiel GitHub, tous les membres de l'équipe ont accès à ce référentiel. Ils peuvent créer des copies locales (clones) du référentiel distant sur leurs ordinateurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-31-at-4.20.06-PM.png)

Ces clones sont super utiles car les développeurs peuvent travailler avec les fichiers localement, apporter des modifications et des commits, et les renvoyer à GitHub.

Lorsque le référentiel distant reçoit de nouvelles modifications, les membres de l'équipe peuvent également incorporer ces modifications dans leurs référentiels locaux pour s'assurer qu'il n'y a pas de conflits entre leurs modifications et les modifications apportées par leurs collègues.

C'est la puissance de Git et GitHub. Maintenant, voyons quelques données sur pourquoi vous devriez apprendre Git et GitHub si votre objectif est de devenir développeur.

## **🔹** Pourquoi devriez-vous apprendre Git et GitHub ?

Git et GitHub sont largement utilisés dans de nombreux domaines et organisations différents.

**💡 Conseil :** Chez [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp), nous utilisons Git et GitHub pour maintenir et mettre à jour la version en ligne de la plateforme d'apprentissage que vous pouvez voir et utiliser chaque jour.

Le [site officiel de Git](https://git-scm.com/) mentionne également que ces entreprises et projets utilisent Git :

* Google
* Microsoft
* Twitter
* LinkedIn
* Netflix
* PostgreSQL
* Android
* Linux
* Ruby on Rails
* Gnome
* Eclipse

Selon l'[Enquête des développeurs de Stack Overflow 2022](https://survey.stackoverflow.co/2022/#version-control-version-control-system-learn) :

> Aucune autre technologie n'est aussi largement utilisée que Git. Surtout parmi les développeurs professionnels.

Les résultats sont très cohérents. **93,87 %** des **71 379** développeurs qui ont répondu à cette question dans l'enquête utilisent Git comme système de contrôle de version.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-30-at-6.59.27-PM.png)
_Les résultats de l'[Enquête des développeurs de Stack Overflow 2022](https://survey.stackoverflow.co/2022/#version-control-systems) pour la catégorie Systèmes de contrôle de version. 93,87 % des répondants ont choisi Git comme système de contrôle de version._

En plus d'être un outil très précieux dans des scénarios réels, Git est également l'un des systèmes de contrôle de version les plus populaires dans la communauté des apprenants qui apprennent à coder.

Parmi les répondants qui apprennent à coder, **81,87 %** d'entre eux utilisent Git.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/learning-to-code.png)
_Les résultats de l'[Enquête des développeurs de Stack Overflow 2022](https://survey.stackoverflow.co/2022/#version-control-version-control-system-learn) pour la catégorie Systèmes de contrôle de version. 81,87 % des répondants qui apprennent à coder utilisent Git._

Sur la base de ces résultats, vous pouvez voir que Git est un outil très puissant pour les développeurs de logiciels de tous horizons et de tous niveaux d'expérience.

Lorsque vous combinez la puissance de Git avec la puissance de **GitHub**, vous déverrouillez la véritable puissance du contrôle de version.

Par exemple, le référentiel de freeCodeCamp est un projet open source hébergé sur GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/GitHub.png)
_[Référentiel GitHub de freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp)_

Le [site officiel de GitHub](https://github.com/) mentionne également que les organisations suivantes hébergent leurs référentiels sur GitHub :

* Stripe
* Pinterest
* KPMG
* Mercedes-Benz
* Procter & Gamble
* Telus

Selon l'[Enquête des développeurs de Stack Overflow 2022](https://survey.stackoverflow.co/2022/#version-control-platforms) :

> GitHub est le système de contrôle de version le plus populaire pour un usage personnel et professionnel.

Dans cette enquête, GitHub était la plateforme de contrôle de version la plus populaire parmi la communauté des développeurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-30-at-7.06.09-PM.png)
_Les résultats de l'[Enquête des développeurs de Stack Overflow 2022](https://survey.stackoverflow.co/2022/#version-control-platforms) pour la catégorie Plateformes de contrôle de version._

Une autre grande chose à propos de GitHub pour les apprenants qui apprennent à coder est que chaque profil dispose d'un calendrier pour suivre les contributions. Il s'agit d'un calendrier interactif avec un petit carré par jour.

Si vous avez apporté plus de contributions un jour particulier, vous verrez une nuance plus foncée de vert sur son carré correspondant.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-386.png)
_Calendrier des contributions de [cet article](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/viewing-contributions-on-your-profile) par GitHub._

Ce calendrier interactif est fréquemment utilisé par les recruteurs pour évaluer votre expérience, vos projets et vos contributions.

Lorsque vous contribuez activement à des projets hébergés sur GitHub, vous créez une chronologie de contributions que les recruteurs peuvent examiner pour voir comment vous communiquez avec d'autres développeurs et comment vous faites face aux défis.

En gros, lorsque vous contribuez sur GitHub, vous créez progressivement votre portfolio de développeur tout en acquérant de l'expérience avec des projets réels.

Super ! Maintenant que vous savez ce que sont Git et GitHub, et pourquoi vous devriez les apprendre, plongeons dans le contenu du cours.

## **🔸** Contenu du cours

Voici un bref aperçu des sujets que vous apprendrez pendant le cours. À la fin du cours, vous serez en mesure de travailler avec Git et GitHub sur vos projets personnels et professionnels.

Nous travaillerons avec des fichiers texte et des fichiers de code simples, donc vous pouvez suivre ce cours indépendamment du ou des langages de programmation que vous avez appris jusqu'à présent ou même si vous commencez tout juste à plonger dans le monde merveilleux de la programmation.

**💡 Conseil :** Mon objectif est de vous enseigner le flux de travail de Git et GitHub étape par étape de manière à ce qu'il soit complètement indépendant du contenu des fichiers. Ainsi, vous pourrez appliquer vos connaissances à tout projet de codage.

### **Introduction à Git**

* Qu'est-ce que Git ? Applications dans la vie réelle.
* Concept de référentiel.
* Comment installer Git et Git Bash.
* Commandes Git Bash.
* Configurer le nom d'utilisateur et l'email Git.

### **Référentiels Git**

* Comment créer un référentiel Git.
* Répertoire de travail.
* Zone de préparation.
* Répertoire `**.git**`.
* La commande `**git status**`.

### **Commits Git**

* Qu'est-ce qu'un commit ?
* Comment créer un commit.
* Afficher l'historique des commits avec `**git log**`.
* Configurer un éditeur Git (Visual Studio Code).
* Modifier le commit le plus récent.
* Annuler un commit.

### **Branches**

* Qu'est-ce qu'une branche ?
* Comment créer une branche.
* La branche `**main**`.
* Basculer vers une branche.
* Renommer une branche.
* Supprimer une branche.
* Créer des commits sur une branche.
* Voir l'historique des commits sur une branche.

### **Fusion de branches**

* Qu'est-ce que la fusion ?
* Comment fusionner deux branches.
* Conflits de fusion.
* Comment supprimer une branche après l'avoir fusionnée avec `**main**`.

### **Introduction à GitHub**

* Qu'est-ce que GitHub ?
* Créer votre compte et profil.
* Personnaliser les paramètres du référentiel.
* Renommer un référentiel.
* Supprimer un référentiel.

### **Flux de travail Git et GitHub**

* Cloner un référentiel.
* Envoyer (push) des modifications à GitHub.
* Recevoir (pull) des modifications de GitHub.
* Validation HTTPS pour pousser des modifications.
* `**git pull**` vs. `**git fetch**`
* Forker un référentiel.
* Cloner un référentiel forké.
* Qu'est-ce qu'une pull request ?
* Démarrer et soumettre une pull request.
* Mettre à jour un référentiel forké.
* Qu'est-ce qu'un issue ?
* Comment ouvrir un issue.
* Modèles d'issues.
* Étiquettes pour les issues et les pull requests.
* Cloner de nouvelles branches distantes vers un référentiel local.
* Supprimer des branches distantes et locales.

Nous verrons comment ces principes et éléments fonctionnent sur un projet réel : [référentiel GitHub de freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp).

![Image](https://www.freecodecamp.org/news/content/images/2023/01/GitHub.png)
_[Référentiel GitHub de freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp)_

Nous créerons également de petits projets au fur et à mesure que vous apprendrez ces sujets étape par étape.

## **📌 Cours Git et GitHub**

Super. Maintenant que vous en savez plus sur Git et GitHub et sur ce que vous apprendrez pendant le cours, vous êtes invité à commencer à suivre le cours en **espagnol** :

%[https://www.youtube.com/watch?v=mBYSUUnMt9M]

✍️ Cours créé par **Estefania Cassingena Navone**. Consultez ma chaîne YouTube ([Coding with Estefania](https://youtube.com/codingwithestefania)) et Twitter [@EstefaniaCassN](https://twitter.com/EstefaniaCassN).

J'espère vraiment que vous aimerez le cours et que vous le trouverez utile pour faire vos premiers pas dans le monde du contrôle de version.

Vous êtes également invité à continuer à apprendre avec nos autres cours en **espagnol** :

%[https://www.youtube.com/watch?v=XqFR2lqBYPs]

%[https://www.youtube.com/watch?v=ivdTnPl1ND0]

%[https://www.youtube.com/watch?v=DLikpfc64cA]

%[https://www.youtube.com/watch?v=6Jfk8ic3KVk]