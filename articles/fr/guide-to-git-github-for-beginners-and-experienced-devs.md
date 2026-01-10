---
title: Comment utiliser Git et GitHub – un guide pour les débutants et les développeurs
  expérimentés
subtitle: ''
author: Isaiah Clifford Opoku
co_authors: []
series: null
date: '2024-04-06T01:38:29.000Z'
originalURL: https://freecodecamp.org/news/guide-to-git-github-for-beginners-and-experienced-devs
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Attractive.png
tags:
- name: beginner
  slug: beginner
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Comment utiliser Git et GitHub – un guide pour les débutants et les développeurs
  expérimentés
seo_desc: "Welcome to Git and GitHub for Beginners! This comprehensive guide is tailored\
  \ to help you navigate the world of version control and collaboration. \nWhether\
  \ you're a newbie just starting out or an experienced developer looking to brush\
  \ up on your skil..."
---

Bienvenue dans Git et GitHub pour les débutants ! Ce guide complet est conçu pour vous aider à naviguer dans le monde du contrôle de version et de la collaboration. 

Que vous soyez un novice qui commence tout juste ou un développeur expérimenté cherchant à rafraîchir vos compétences, ce guide offre une approche étape par étape pour comprendre et utiliser efficacement Git et GitHub.

À la fin de ce parcours, vous aurez une base solide en Git et GitHub. Vous serez équipé de connaissances pratiques pour rationaliser votre flux de travail de codage, collaborer sans effort avec des équipes et contribuer à des projets open source. 

Alors, plongeons et commençons votre aventure avec Git et GitHub !

## Table des matières

  - [À qui s'adresse ce guide ?](#heading-a-qui-sadresse-ce-guide)
  - [Technologies](#heading-technologies)
  - [Termes](#heading-termes)
  - [Qu'est-ce que GitHub ?](#heading-quest-ce-que-github)
  - [À quoi sert GitHub ?](#heading-a-quoi-sert-github)
  - [Tâches courantes que vous effectuerez avec Git](#heading-taches-courantes-que-vous-effectuerez-avec-git)
  - [Comment installer Git](#heading-comment-installer-git)
  - [Comment configurer Git](#heading-comment-configurer-git)
  - [Comment définir l'éditeur par défaut](#heading-comment-definir-lediteur-par-defaut)
  - [Comment créer un dépôt en utilisant le site web de Github](#heading-comment-creer-un-depot-en-utilisant-le-site-web-de-github)
  - [Comment créer un dépôt en utilisant la ligne de commande Git](#heading-comment-creer-un-depot-en-utilisant-la-ligne-de-commande-git)
  - [Comment connecter un dépôt local à un dépôt distant sur GitHub](#heading-comment-connecter-un-depot-local-a-un-depot-distant-sur-github)
  - [Comment tirer les changements d'un dépôt distant vers un dépôt local](#heading-comment-tirer-les-changements-dun-depot-distant-vers-un-depot-local)
  - [Comment travailler avec les commandes Git](#heading-comment-travailler-avec-les-commandes-git)
  - [Comment apporter des modifications à un fichier](#heading-comment-apporter-des-modifications-a-un-fichier)
  - [Comment vérifier l'état de la branche actuelle](#heading-comment-verifier-letat-de-la-branche-actuelle)
  - [Comment préparer les changements](#heading-comment-preparer-les-changements)
  - [Comment valider les changements](#heading-comment-valider-les-changements)
  - [Comment pousser les changements vers un dépôt distant](#heading-comment-pousser-les-changements-vers-un-depot-distant)
  - [Comment créer une branche](#heading-comment-creer-une-branche)
  - [Comment créer une demande de tirage](#heading-comment-creer-une-demande-de-tirage)
  - [Comment fusionner une demande de tirage](#heading-comment-fusionner-une-demande-de-tirage)
  - [Conclusion](#heading-conclusion)

<h2 id="heading-a-qui-sadresse-ce-guide">À qui s'adresse ce guide ?</h2>

Ce guide est destiné à tous ceux qui veulent améliorer leurs compétences en codage et devenir compétents dans l'utilisation de Git et GitHub. 

Que vous soyez :
- en début de carrière technologique et que vous deviez apprendre les bases du contrôle de version.
- un développeur aspirant désireux d'intégrer `Git` dans votre flux de travail.
- un programmeur expérimenté cherchant à rafraîchir vos connaissances ou à découvrir de nouvelles fonctionnalités.
- un responsable d'équipe ou un manager intéressé à favoriser une culture de collaboration et de gestion efficace du code.

Quelle que soit votre expérience ou votre formation, ce guide est conçu pour vous donner les outils et les connaissances dont vous avez besoin pour exceller dans vos projets de codage.

<h2 id="heading-technologies">Technologies</h2>

Avant de commencer, assurez-vous :
- D'avoir un [compte GitHub](https://github.com/)
- Que [Git](https://git-scm.com/) est installé sur votre machine
- D'avoir un éditeur de texte, tel que [Visual Studio Code](https://code.visualstudio.com/) installé
- Que [Node.js](https://nodejs.org/en/) est installé sur votre machine

<h2 id="heading-termes">Termes</h2>

Il y a beaucoup de termes autour de Git et Github que vous pourriez rencontrer lorsque vous travaillez avec le contrôle de version. Laissez-moi vous les expliquer avant de commencer :

- **Branche** : Une version de la base de code qui diverge de la branche principale pour isoler les changements pour des fonctionnalités, des corrections ou des expériences spécifiques.
- **Commit** : Un instantané de vos changements, sauvegardé dans votre dépôt local. Chaque commit est identifié de manière unique par une somme de contrôle.
- **Stage** : La zone où Git suit les changements qui sont prêts à être inclus dans le prochain commit. Les fichiers dans la zone de staging sont préparés (staged) pour le prochain commit.
- **Merge** : Le processus d'intégration des changements d'une branche à une autre, généralement la branche principale.
- **Pull Request** : Une proposition de fusionner des changements d'une branche à une autre, souvent utilisée dans des environnements collaboratifs pour examiner et discuter des changements avant qu'ils ne soient fusionnés.
- **Fork** : Une copie personnelle du projet de quelqu'un d'autre qui vit sur votre compte GitHub.
- **Clone** : L'action de télécharger un dépôt depuis une source distante vers votre machine locale.
- **Remote** : Un dépôt commun que tous les membres de l'équipe utilisent pour échanger leurs changements.
- **Origin** : Le nom par défaut que Git donne au serveur à partir duquel vous avez cloné.
- **Upstream** : Le dépôt original qui a été cloné.
- **Master** : Le nom de branche par défaut donné à un dépôt lorsqu'il est créé. Dans la pratique moderne, il est souvent remplacé par `main`.
- **Repository** : Un emplacement de stockage où vit votre projet, contenant tous les fichiers et l'historique des révisions.
- **Working Directory** : Le répertoire sur votre ordinateur où vous apportez des modifications à votre projet.
- **Staging Area** : Également connue sous le nom d'"Index", c'est une zone où Git suit les changements qui sont prêts à être validés.
- **Index** : Un autre nom pour la zone de staging, où Git suit les changements qui sont prêts à être validés.
- **HEAD** : Une référence au dernier commit dans la branche actuellement extraite.
- **Checkout** : L'action de passer d'une branche à une autre ou à un commit spécifique.
- **Push** : L'action d'envoyer vos commits à un dépôt distant.
- **Pull** : L'action de récupérer les changements d'un dépôt distant et de les fusionner dans votre branche actuelle.
- **Fetch** : L'action de récupérer les mises à jour d'un dépôt distant sans les fusionner dans votre branche actuelle.

<h2 id="heading-quest-ce-que-github">Qu'est-ce que GitHub ?</h2>

![GitHub-1](https://www.freecodecamp.org/news/content/images/2024/04/GitHub-1.png)

GitHub est une plateforme qui héberge du code, fournissant des fonctionnalités de contrôle de version et de collaboration. Elle permet à vous et à d'autres de travailler ensemble sur des projets depuis n'importe où dans le monde. 

Ce guide vous introduira aux concepts essentiels de GitHub tels que les `dépôts`, les `branches`, les `commits`, et les `Pull Requests`. Vous apprendrez comment créer votre propre dépôt 'Hello World' et comprendre le flux de travail des Pull Requests de GitHub, une méthode largement utilisée pour créer et examiner du code. 

À la fin de ce guide, vous serez équipé des connaissances et des compétences pour collaborer efficacement sur GitHub.

<h2 id="heading-a-quoi-sert-github">À quoi sert GitHub ?</h2>

GitHub est plus qu'une simple plateforme d'hébergement de code. C'est un outil qui permet une collaboration et un contrôle de version sans faille. Voici quelques-unes de ses utilisations :

- Héberger et partager votre code avec d'autres.
- Suivre et assigner des problèmes pour maintenir un flux de travail organisé.
- Gérer les pull requests pour examiner et incorporer des changements dans votre projet.
- Créer votre propre site web en utilisant GitHub Pages, un service d'hébergement de sites statiques.
- Collaborer avec d'autres sur des projets, ce qui en fait un excellent outil pour les contributions open source.

<h2 id="heading-quest-ce-que-git">Qu'est-ce que Git ?</h2>

Git est un système de contrôle de version distribué gratuit et open source. Il est conçu pour gérer tout, des petits aux très grands projets avec rapidité et efficacité.

Git est facile à apprendre et a une empreinte minuscule avec des performances ultra-rapides. Il surpasse les outils SCM comme Subversion, CVS, Perforce et ClearCase avec des fonctionnalités comme le branchement local peu coûteux, des zones de staging pratiques et plusieurs flux de travail.

Git a été initialement conçu et développé par Linus Torvalds pour le développement du noyau Linux.

Quelques fonctionnalités/avantages de Git :

- Vous permet de suivre les changements apportés à votre code au fil du temps.
- Vous permet de collaborer avec d'autres sur la même base de code.
- Vous pouvez facilement revenir à une version précédente de votre code ou expérimenter de nouvelles fonctionnalités sans affecter la base de code principale.
- Fournit un enregistrement de tous les changements apportés à votre code, y compris qui les a faits et quand, ce qui peut être utile pour l'audit et le débogage.

<h2 id="heading-taches-courantes-que-vous-effectuerez-avec-git"> Tâches courantes que vous effectuerez avec Git </h2>

- Créer un dépôt
- Créer une branche
- Apporter des modifications à un fichier
- Préparer les changements
- Valider les changements
- Pousser les changements vers un dépôt distant
- Fusionner les changements
- Revenir en arrière sur les changements
- Supprimer une branche

<h2 id="heading-comment-installer-git">  Comment installer Git </h2>

Pour installer Git sur votre machine locale, vous devez suivre ces étapes :

1. Téléchargez Git depuis le site officiel : [Téléchargements Git](https://git-scm.com/downloads)

2. Installez Git sur votre machine locale en suivant les instructions fournies sur le site officiel : [Installation de Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

*Félicitations !* Vous avez installé Git avec succès sur votre machine locale. Vous êtes maintenant prêt à commencer à utiliser Git pour vos projets.

<h2 id="heading-comment-configurer-git">  Comment configurer Git </h2>

Git offre une variété de configurations qui peuvent rationaliser votre flux de travail. Dans cette section, je vais vous guider à travers le processus de configuration de Git sur votre machine locale. Commençons.

Configurer votre `nom` et votre `adresse email` sur votre machine locale est une étape essentielle dans la configuration de Git. Ces détails sont attachés à chaque commit que vous faites, fournissant un contexte et une propriété. Apprenons comment utiliser la commande `git config --global` pour définir votre nom et votre email globalement sur votre machine locale.

Pour configurer votre nom, vous devez taper la commande suivante dans votre terminal :

```bash

# Définir un nom identifiable pour le crédit lors de l'examen de l'historique des versions

$ git config --global user.name "Votre Nom"

```

![userNameEmail](https://www.freecodecamp.org/news/content/images/2024/04/userNameEmail.png)

Comme vous pouvez le voir sur l'image ci-dessus, j'ai entré mon nom.

Après avoir entré votre nom, appuyez sur `Entrée` pour l'enregistrer. Vous ne recevrez aucune réponse, mais soyez assuré, votre nom a été enregistré avec succès.

Tout comme nous avons configuré le nom d'utilisateur, nous devons également configurer l'email de l'utilisateur. Cet email sera associé à chaque commit que vous faites. Apprenons comment utiliser la commande `git config --global` pour définir votre email globalement sur votre machine locale.

```bash
# Définir une adresse email qui sera associée à chaque marqueur d'historique
$ git config --global user.email "votre-email@example.com"

```

![Email](https://www.freecodecamp.org/news/content/images/2024/04/Email.png)

Assurez-vous de remplacer cela par votre email réel utilisé dans votre compte GitHub.

Maintenant que nous avons terminé la configuration de votre nom d'utilisateur et de votre email pour Git et GitHub, vérifions que tout est configuré correctement.

Pour ce faire, utilisez la commande suivante :

```bash
git config --global --list 
```

Cette commande listera le nom d'utilisateur et l'email utilisés dans la console pour que vous puissiez les voir.

Vous devriez voir certaines informations affichées dans votre terminal.

<h2 id="heading-comment-definir-lediteur-par-defaut"> Comment définir l'éditeur par défaut</h2>

Dans le développement moderne, avoir un éditeur de code peut simplifier considérablement votre flux de travail, surtout lorsque vous êtes concentré sur le codage.

Maintenant, voyons comment configurer Git pour utiliser un éditeur par défaut en utilisant cette commande :

```bash
# Définir l'éditeur par défaut pour Git
$ git config --global core.editor "code --wait"
```

*Félicitations !* Vous avez configuré Git avec succès sur votre machine locale. Vous êtes maintenant prêt à commencer à utiliser Git pour vos projets.

<h2 id="heading-comment-creer-un-depot-en-utilisant-le-site-web-de-github">  Comment créer un dépôt en utilisant le site web de Github </h2>

Créer un dépôt est la première étape de l'utilisation de Git. Un dépôt est un emplacement de stockage où vivent vos projets, contenant tous les fichiers et l'historique des révisions. 

Dans cette section, je vais vous guider à travers le processus de création d'un dépôt sur GitHub. 

Il existe deux façons de créer un dépôt : en utilisant le `site web de GitHub` ou la ligne de commande. Commençons. Dans cette section, nous nous concentrerons sur la création d'un dépôt en utilisant le site web de GitHub et la ligne de commande.

Après vous être connecté à votre compte GitHub, vous pouvez créer un nouveau dépôt en suivant ces étapes :

1. Cliquez sur le signe `+` dans le coin supérieur droit de la page et sélectionnez `Nouveau dépôt` dans le menu déroulant.

![Github-create-repo](https://www.freecodecamp.org/news/content/images/2024/04/Github-create-repo.png)

Ci-dessus se trouve une image du bouton de nouveau dépôt sur GitHub.

2. Vous serez dirigé vers une nouvelle page où vous pourrez remplir les détails de votre nouveau dépôt. Vous devrez entrer les informations suivantes :

- `Nom du dépôt` : Il s'agit du nom de votre dépôt. Il doit être unique et descriptif.
- `Description` : Une brève description de votre dépôt.
- `Public ou Privé` : Vous pouvez choisir de rendre votre dépôt public ou privé. Les dépôts publics sont visibles par tous, tandis que les dépôts privés ne sont visibles que par vous et les personnes avec qui vous les partagez.
- `Initialiser` ce dépôt avec un README : Vous pouvez choisir d'initialiser votre dépôt avec un fichier README. Cela est utile si vous souhaitez fournir des informations sur votre projet ou des instructions sur son utilisation.

![github-repo-infor](https://www.freecodecamp.org/news/content/images/2024/04/github-repo-infor.png)

L'image ci-dessus montre le formulaire où vous remplirez les détails de votre nouveau dépôt.

3. Une fois que vous avez rempli les détails, cliquez sur le bouton `Créer un dépôt` pour créer votre nouveau dépôt.

![github-create-repo-button](https://www.freecodecamp.org/news/content/images/2024/04/github-create-repo-button.png)

L'image ci-dessus montre le bouton `Créer un dépôt`_.


*Félicitations !* Vous avez créé avec succès un nouveau dépôt sur GitHub. Vous pouvez maintenant commencer à ajouter des fichiers et à apporter des modifications à votre dépôt.

Vous devriez voir une page comme celle ci-dessous :

![github-new-repo](https://www.freecodecamp.org/news/content/images/2024/04/github-new-repo.png)

Maintenant, créons un dépôt en utilisant la ligne de commande.

<h2 id="heading-comment-creer-un-depot-en-utilisant-la-ligne-de-commande-git">  Comment créer un dépôt en utilisant la ligne de commande Git </h2>


Pour créer un nouveau `dépôt` en utilisant la ligne de commande, vous devez suivre ces étapes :

1. Ouvrez votre terminal et naviguez jusqu'au répertoire où vous souhaitez créer votre nouveau dépôt.

2. Utilisez la commande `git init` pour créer un nouveau dépôt. Cette commande créera un nouveau répertoire appelé `.git` dans votre répertoire actuel, qui contiendra tous les fichiers nécessaires pour votre dépôt.

```bash

# initialiser un nouveau dépôt appelé my-project

$ git init my-project

```

![terminal-init](https://www.freecodecamp.org/news/content/images/2024/04/terminal-init.png)

L'image ci-dessus montre la commande pour initialiser un nouveau dépôt appelé `my-project`.

3. Une fois que vous avez créé votre nouveau dépôt, vous pouvez commencer à ajouter des fichiers et à apporter des modifications. Vous pouvez également connecter votre dépôt local à un dépôt distant sur GitHub en suivant les instructions fournies sur le site web de GitHub.

*Félicitations !* Vous avez créé avec succès un nouveau dépôt en utilisant la ligne de commande. 

Nous avons maintenant créé avec succès un dépôt en utilisant le site web de GitHub et la ligne de commande – mais comment les connecter ? Maintenant, apprenons comment connecter un dépôt local à un dépôt distant sur GitHub.

<h2 id="heading-comment-connecter-un-depot-local-a-un-depot-distant-sur-github">  Comment connecter un dépôt local à un dépôt distant sur GitHub </h2>

Pour connecter votre dépôt local à un dépôt distant sur GitHub, vous devez suivre ces étapes :

1. Sur GitHub, naviguez jusqu'à la page principale du dépôt que vous avez créé précédemment.

2. Cliquez sur le bouton `Code` pour copier l'URL de votre dépôt.

![Github-code-url-cope](https://www.freecodecamp.org/news/content/images/2024/04/Github-code-url-cope.png)

L'image ci-dessus montre le bouton de code pour copier l'URL de votre dépôt.

3. Dans votre terminal, naviguez jusqu'au répertoire de votre dépôt local.

4. Utilisez la commande `git remote add origin` pour connecter votre dépôt local au dépôt distant sur GitHub. Remplacez repository-URL par l'URL de votre dépôt.

```bash
$ git remote add origin repository-url

```

![terminal-remote-add-origin](https://www.freecodecamp.org/news/content/images/2024/04/terminal-remote-add-origin.png)

L'image ci-dessus montre la commande pour connecter votre dépôt local au dépôt distant sur GitHub.

5. Une fois que vous avez connecté votre dépôt local au dépôt distant sur GitHub, vous pouvez commencer à pousser vos changements vers le dépôt distant en utilisant la commande `git push`.

*Félicitations !* Vous avez connecté avec succès votre dépôt local au dépôt distant sur GitHub.

<h2 id="heading-comment-tirer-les-changements-dun-depot-distant-vers-un-depot-local">   Comment tirer les changements d'un dépôt distant vers un dépôt local </h2>

Pour tirer les changements du dépôt distant vers le dépôt local, vous devez suivre ces étapes :

1. Dans votre terminal, naviguez jusqu'au répertoire de votre dépôt local.

2. Utilisez la commande `git pull` pour tirer les changements du dépôt distant vers le dépôt local.

```bash

$ git pull origin main

```

![terminal-git-pull](https://www.freecodecamp.org/news/content/images/2024/04/terminal-git-pull.png)

L'image ci-dessus montre la commande pour tirer les changements du dépôt distant vers le dépôt local.

Après cela, naviguez vers la branche principale en utilisant la commande suivante :

```bash

$ git checkout main

```

*Félicitations !* Vous avez tiré avec succès les changements d'un dépôt distant vers un dépôt local. Votre dépôt local est maintenant à jour avec le dépôt distant sur GitHub*.

<h2 id="heading-comment-travailler-avec-les-commandes-git"> Comment travailler avec les commandes Git </h2>

Dans cette section, nous allons couvrir certaines des commandes Git les plus couramment utilisées et leurs fonctions. Ces commandes vous aideront à naviguer dans le flux de travail Git dans votre dépôt GitHub. Commençons. 

Tout d'abord, je vais ajouter quelques fichiers afin que nous puissions commencer à utiliser les commandes Git.


<h2 id="heading-comment-apporter-des-modifications-a-un-fichier"> Comment apporter des modifications à un fichier </h2>

Pour apporter des modifications à un fichier dans Git, vous devez suivre ces étapes :

1. Ouvrez votre terminal et naviguez jusqu'au répertoire de votre dépôt local.

2. Utilisez un éditeur de texte pour apporter des modifications au fichier. Par exemple, vous pouvez utiliser la commande `code` pour ouvrir le fichier dans Visual Studio Code.

```bash

$ code file-name  # Par exemple, code index.html

```

3. Une fois que vous avez apporté vos modifications, enregistrez le fichier et fermez l'éditeur de texte.

*Félicitations !* Vous avez apporté avec succès des modifications à un fichier dans votre dépôt local. Ensuite, passons à l'étape suivante : préparer les changements.

<!-- montrer une image pour le nouveau fichier que j'ai ajouté qui est une application react et typescript  -->

![file-cahnge-added](https://www.freecodecamp.org/news/content/images/2024/04/file-cahnge-added.png)

L'image ci-dessus montre le nouveau fichier que j'ai ajouté qui est une application React et TypeScript.

Visual Studio Code (VS Code) inclut une fonctionnalité de contrôle de source qui vous permet d'interagir directement avec votre dépôt GitHub. Cette fonctionnalité prend en charge une variété d'opérations, y compris la préparation, la validation, le poussage et le tirage des changements. 

En plus de la fonctionnalité de contrôle de source, vous pouvez également utiliser le terminal intégré dans VS Code pour interagir avec votre dépôt GitHub. 

Actuellement, si vous regardez la section de contrôle de source dans VS Code, vous verrez le fichier que nous avons ajouté listé sous les changements. 

Ensuite, explorons comment utiliser le terminal pour interagir avec notre dépôt GitHub.

Ouvrez votre terminal et naviguez jusqu'au répertoire de votre dépôt local.

Maintenant, utilisons la commande `git status` pour vérifier l'état de la branche actuelle.

<h2 id="heading-comment-verifier-letat-de-la-branche-actuelle">  Comment vérifier l'état de la branche actuelle </h2>

La commande `git status` montre l'état de la branche actuelle, y compris les changements qui ont été apportés aux fichiers dans le dépôt. Elle fournit des informations sur les fichiers qui ont été modifiés, les fichiers qui ont été préparés et les fichiers qui ne sont pas suivis. 

Cette commande est utile pour comprendre l'état actuel de votre dépôt et déterminer quels fichiers doivent être préparés et validés.

```bash
#  Vérifier l'état de la branche actuelle

$ git status  # Sur la branche master

```

![terminal-git-status](https://www.freecodecamp.org/news/content/images/2024/04/terminal-git-status.png)

L'image ci-dessus montre la commande pour vérifier l'état de la branche actuelle.

Vous pouvez remarquer que des parties du fichier sont mises en évidence dans différentes couleurs. La couleur `rouge` indique que le fichier a été modifié, tandis que la couleur `verte` signifie que le fichier a été ajouté à la zone de staging. 

Actuellement, tous les fichiers doivent être mis en évidence en `rouge` car nous n'avons pas encore ajouté de fichiers à la zone de staging.

Ajoutons le fichier à la zone de staging en utilisant la commande `git add`.

<h2 id="heading-comment-preparer-les-changements">  Comment préparer les changements </h2>

La commande `git add` ajoute des fichiers à la zone de staging, les préparant pour le prochain commit. Vous pouvez ajouter tous les fichiers dans le répertoire actuel à la zone de staging en utilisant la commande `git add .`. 

Si vous souhaitez ajouter un fichier spécifique, utilisez la commande `git add <file-name>`, en remplaçant `<file-name>` par le nom de votre fichier. Ce processus est connu sous le nom de staging, qui prépare les fichiers pour le prochain commit.

```bash

# Ajouter des fichiers à la zone de staging

$ git add .  # Changements à valider :

ou 

$ git add file-name  # Changements à valider :

```

Pensez-y comme ceci : monter dans la voiture est comme ajouter des fichiers à la zone de staging, et conduire la voiture est comme faire un commit. 

Maintenant, utilisons la commande `git commit` pour valider les changements dans la branche actuelle.

<h2 id="heading-comment-valider-les-changements">  Comment valider les changements </h2>

La commande `git commit` valide les changements dans la branche actuelle. Vous pouvez utiliser le drapeau `-m` pour ajouter un message à votre commit. Ce message doit fournir un bref résumé des changements que vous avez apportés.

Par exemple, "Initial commit" pourrait être votre message de commit. Cette commande est utilisée pour sauvegarder les changements dans le dépôt local.

```bash


# Valider les changements dans la branche actuelle

$ git commit -m "Message de commit"   # Par exemple, git commit -m "Initial commit"

```

Nous avons validé avec succès les changements dans la branche actuelle. Ensuite, nous allons pousser ces changements vers le dépôt distant sur GitHub en utilisant la commande `git push`.

<h2 id="heading-comment-pousser-les-changements-vers-un-depot-distant">  Comment pousser les changements vers un dépôt distant </h2>

La commande `git push` pousse les changements de votre dépôt local vers un dépôt distant sur GitHub. Vous pouvez utiliser la commande `git push` pour pousser les changements de votre dépôt local vers le dépôt distant sur GitHub. Ce processus est essentiel pour mettre à jour le dépôt distant avec les changements que vous avez apportés localement.

```bash

# Pousser les changements vers un dépôt distant

$ git push origin main  # Par exemple, git push origin master

```

*Félicitations !* Vous avez poussé avec succès vos changements vers le dépôt distant sur GitHub. Vous pouvez maintenant voir vos changements sur le site web de GitHub.  

Maintenant que nous avons poussé avec succès nos changements vers le dépôt distant sur GitHub, passons à l'étape suivante : créer une branche. 

Selon l'environnement de votre PC, votre dépôt local peut avoir une branche par défaut nommée soit `main` soit `master`. Dans ce guide, nous utiliserons `main` comme nom de branche par défaut, en nous alignant sur le changement récent de GitHub de `master` à `main`.

Avant de commencer à ajouter des fichiers, assurons-nous que notre dépôt local est à jour avec le dépôt distant en tirant les changements. 

Si le terme `branche` vous semble inconnu, ne vous inquiétez pas. Dans la section suivante, nous couvrirons comment créer une branche et comment tirer les changements du dépôt distant vers le dépôt local.

<h2 id="heading-comment-creer-une-branche">  Comment créer une branche </h2>

Le branchement est un concept fondamental dans Git. Il vous permet de diverger de la ligne principale de développement et de continuer à travailler sans impacter la base de code principale. 

Dans cette section, je vais vous guider à travers le processus de création d'une nouvelle branche en utilisant la commande `git branch`. Cette commande crée une nouvelle branche mais ne bascule pas vers elle. Dans les étapes suivantes, nous couvrirons également comment basculer vers votre nouvelle branche en utilisant la commande `git checkout`. Commençons.

Pour créer une nouvelle branche, vous devez suivre ces étapes :

1. Ouvrez votre terminal et naviguez jusqu'au répertoire de votre dépôt local.

2. Utilisez la commande `git branch` pour créer une nouvelle branche. Remplacez `<branch-name>` par le nom de votre nouvelle branche.

```bash

# Créer une nouvelle branche

$ git branch <branch-name>  # Par exemple, git branch feature-branch

```

La commande `git branch` crée une nouvelle branche mais ne bascule pas vers elle. Pour basculer vers votre nouvelle branche, utilisez la commande `git checkout`.

```bash

# Basculer vers la nouvelle branche

$ git checkout <branch-name>  # Par exemple, git checkout feature-branch

```

La commande `git checkout` est utilisée pour basculer d'une branche à une autre. Remplacez `<branch-name>` par le nom de votre nouvelle branche. Dans ce cas, nous basculons vers la branche `feature-branch`. Mais si nous voulons supprimer la branche, nous pouvons utiliser la commande suivante :

```bash


# Supprimer une branche

$ git branch -d <branch-name>  # Par exemple, git branch -d feature-branch

```

La commande `git branch -d` est utilisée pour supprimer une branche. Remplacez `<branch-name>` par le nom de la branche que vous souhaitez supprimer. Dans ce cas, nous supprimons la branche `feature-branch`.

*Félicitations !* Vous avez créé avec succès une nouvelle branche et basculé vers elle. Vous pouvez maintenant commencer à ajouter des fichiers et à apporter des modifications à votre nouvelle branche.

Maintenant, vous savez comment créer un dépôt GitHub, connecter un dépôt local à un dépôt distant sur GitHub, tirer les changements d'un dépôt distant vers un dépôt local, travailler avec les commandes Git et créer une branche. 

Passons à la section suivante, où nous couvrirons comment créer une pull request. Il s'agit d'une étape cruciale dans le flux de travail collaboratif, car elle vous permet de proposer des changements et de demander une révision à d'autres collaborateurs.

 <h2 id="heading-comment-creer-une-demande-de-tirage"> Comment créer une demande de tirage  </h2>

Une pull request est une proposition de fusionner des changements d'une branche à une autre. C'est une méthode largement utilisée pour créer et examiner du code. Dans cette section, je vais vous guider à travers le processus de création d'une pull request en utilisant le site web de GitHub. 

Par exemple, disons que vous avez une branche nommée `feature-branch` et que vous souhaitez la fusionner dans la branche `main`. Nous allons vous guider à travers la création d'une pull request pour ce scénario. Commençons.

Tout d'abord, apportons une modification à notre branche de fonctionnalité en ajoutant un fichier :

```bash

$ git checkout feature-branch

```

Vous devriez voir quelque chose comme ceci dans votre terminal :

```bash

git checkout feature-branch
Switched to a new branch 'feature-branch'
branch 'feature-branch' set up to track 'origin/feature-branch'.

```

Maintenant, ajoutons un fichier à la branche de fonctionnalité. 

```bash

$ touch feature-branch-file.txt

```

Après avoir exécuté la commande, vous devriez voir un nouveau fichier appelé `feature-branch-file.txt` dans votre répertoire.

La commande `touch` est utilisée pour créer un nouveau fichier. Remplacez `feature-branch-file.txt` par le nom de votre fichier. Dans ce cas, nous créons un nouveau fichier appelé `feature-branch-file.txt`.

Maintenant, ajoutons du contenu au fichier.

```bash

$ echo "Ceci est un fichier dans la branche de fonctionnalité" >> feature-branch-file.txt

```

Cette commande ajoute le texte "Ceci est un fichier dans la branche de fonctionnalité" au fichier `feature-branch-file.txt`.

La commande `echo` est utilisée pour ajouter du contenu à un fichier. Dans ce cas, nous ajoutons le texte "Ceci est un fichier dans la branche de fonctionnalité" au fichier `feature-branch-file.txt`.

Maintenant que nous avons du texte dans le fichier, préparons et validons les changements dans la branche de fonctionnalité.

```bash

$ git add .

```

La commande `git add .` prépare tous les changements dans le répertoire actuel.

```bash


$ git commit -m "Ajouter un fichier à la branche de fonctionnalité"

```

La commande `git commit -m` valide les changements dans la branche actuelle. Remplacez `Ajouter un fichier à la branche de fonctionnalité` par votre propre message descriptif. Ce message doit fournir un bref résumé des changements que vous avez apportés. Dans ce cas, nous validons les changements dans la branche de fonctionnalité.

Maintenant, poussons les changements vers le dépôt distant sur GitHub.

```bash

$ git push origin feature-branch

```

La commande `git push` est utilisée pour pousser les changements de votre dépôt local vers le dépôt distant sur GitHub. Remplacez `feature-branch` par le nom de votre branche. Dans ce cas, nous poussons les changements vers la branche `feature-branch`.

*Félicitations !* Vous avez poussé avec succès vos changements vers le dépôt distant sur GitHub. Vous pouvez maintenant voir vos changements sur le site web de GitHub.

Maintenant, lorsque vous ouvrez votre dépôt GitHub, vous devriez voir un message indiquant que vous avez récemment poussé une nouvelle branche. Vous pouvez cliquer sur le bouton `Compare & pull request` pour créer une pull request pour la branche `feature-branch`. 

![github-compare-pull-request](https://www.freecodecamp.org/news/content/images/2024/04/github-compare-pull-request.png)

L'image ci-dessus montre le bouton `Compare & pull request` sur GitHub.

Après avoir cliqué sur le bouton `Compare & pull request`, vous serez dirigé vers une nouvelle page où vous pourrez remplir les détails de votre pull request. 

Vous devrez entrer les informations suivantes :

- Titre : un bref résumé de votre pull request.
- Description : une description détaillée de votre pull request, y compris des informations sur les changements que vous avez apportés et pourquoi vous les avez apportés.
- Relecteurs : vous pouvez choisir de demander une relecture à des collaborateurs spécifiques.
- Assignés : vous pouvez choisir d'assigner votre pull request à des collaborateurs spécifiques.
- Étiquettes : vous pouvez choisir d'ajouter des étiquettes à votre pull request pour la catégoriser.
- Projets : vous pouvez choisir d'ajouter votre pull request à un tableau de projet.
- Jalon : vous pouvez choisir d'ajouter votre pull request à un jalon.

![github-pull-request-form](https://www.freecodecamp.org/news/content/images/2024/04/github-pull-request-form.png)

L'image ci-dessus montre le formulaire pour remplir les détails de votre pull request.

Vous pouvez décider de remplir les détails de votre pull request ou de créer la pull request. Après avoir créé la pull request, vous pouvez la voir sur le site web de GitHub. Vous pouvez également demander une relecture à des collaborateurs spécifiques et apporter des modifications à votre pull request si nécessaire. 

Une fois que votre pull request a été relue et approuvée, vous pouvez la fusionner dans la branche `main`. Dans notre cas, nous n'allons pas remplir le formulaire mais nous allons créer la pull request.

<!-- image montrant après la création de la pull request  -->

![github-pull-request-created](https://www.freecodecamp.org/news/content/images/2024/04/github-pull-request-created.png)

L'image ci-dessus montre la pull request créée sur GitHub.

Maintenant que nous avons créé une pull request, passons à la section suivante, où nous couvrirons comment fusionner une pull request. Il s'agit de l'étape finale dans le flux de travail collaboratif, car elle vous permet d'incorporer des changements dans la base de code principale.

<h2 id="heading-comment-fusionner-une-demande-de-tirage">Comment fusionner une demande de tirage  </h2>

Fusionner une pull request signifie l'intégration des changements d'une branche à une autre, souvent la branche principale. Cette étape est cruciale dans les flux de travail collaboratifs, permettant l'assimilation des modifications dans la base de code principale. 

Dans cette section, nous allons naviguer dans le processus de fusion d'une pull request via le site web de GitHub. 

Après avoir créé une pull request, vous pouvez la fusionner dans la branche `main` en suivant ces étapes :

1. Sur GitHub, naviguez jusqu'à la page principale du dépôt où vous avez créé la pull request.

2. Cliquez sur l'onglet `Pull requests` pour voir la liste des pull requests.

<!--  image montrant la section des pull requests  -->

![github-pull-request-tab](https://www.freecodecamp.org/news/content/images/2024/04/github-pull-request-tab.png)

L'image ci-dessus montre l'onglet `Pull requests` sur GitHub.

3. Cliquez sur la pull request que vous souhaitez fusionner.

4. Cliquez sur le bouton `Merge pull request` pour fusionner la pull request dans la branche `main`.

5. Cliquez sur le bouton `Confirm merge` pour confirmer la fusion.

Après cela, vous devriez voir un message indiquant que la pull request a été fusionnée avec succès. Vous pouvez également supprimer la branche après avoir fusionné la pull request.

![github-pull-request-merged](https://www.freecodecamp.org/news/content/images/2024/04/github-pull-request-merged.png)

Maintenant, vous avez fusionné avec succès la pull request dans la branche `main`. Vous pouvez maintenant supprimer la branche `feature-branch`, car elle n'est plus nécessaire.  


 <h2 id="heading-conclusion"> Conclusion </h2>

Tout au long de ce guide, nous avons exploré les concepts fondamentaux de Git et GitHub, vous équipant d'une compréhension solide du contrôle de version et des pratiques collaboratives. 

Nous avons navigué à travers les opérations essentielles de Git, y compris la configuration d'un dépôt, la liaison du dépôt local à son homologue distant sur GitHub, la synchronisation des changements entre les dépôts locaux et distants, l'exécution des commandes Git, le branchement, l'initiation des pull requests et la fusion de ces demandes. 

La maîtrise de ces principes améliorera considérablement votre flux de travail de codage, facilitera la collaboration en équipe et permettra des contributions significatives aux projets open source. 

Je suis convaincu que ce guide vous a fourni les connaissances et la confiance nécessaires pour exceller dans votre parcours de programmation et commencer à contribuer à des projets open source. Bonne chance dans votre aventure de codage !

Vous pouvez me contacter sur [Twitter](https://twitter.com/Clifftech_Dev) ou [LinkedIn](https://www.linkedin.com/in/isaiah-clifford-opoku/) pour toute question ou feedback. J'adorerais avoir de vos nouvelles !