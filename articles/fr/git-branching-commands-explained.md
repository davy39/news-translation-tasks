---
title: Commandes de branchement Git expliquées avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-02T21:49:02.000Z'
originalURL: https://freecodecamp.org/news/git-branching-commands-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/git-commands-thumbnail.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Commandes de branchement Git expliquées avec des exemples
seo_desc: 'By Deborah Kurata

  Knowing the right Git command for the task at hand can often be challenging. Especially
  when you''re adding complexity to your task, like with Git branching.

  Git is a powerful version control system that enables you to track changes ...'
---

Par Deborah Kurata

Connaître la bonne commande Git pour la tâche à accomplir peut souvent être un défi. Surtout lorsque vous ajoutez de la complexité à votre tâche, comme avec le branchement Git.

Git est un système de contrôle de version puissant qui vous permet de suivre les changements apportés à votre base de code. L'une des fonctionnalités clés de Git est sa capacité à gérer les branches.

Les branches permettent aux développeurs de travailler sur différentes fonctionnalités, problèmes ou corrections de bugs sans affecter la base de code principale du projet.

Ce tutoriel vous guide à travers un ensemble de commandes Git pour créer, commiter, fusionner et supprimer des branches.

Le tutoriel suppose que vous avez une compréhension conceptuelle de base du branchement Git [comme je l'ai couvert dans mon article précédent](https://www.freecodecamp.org/news/how-to-work-with-branches-in-git/).

Vous pouvez également regarder la vidéo associée ici qui inclut des démonstrations de branchement en utilisant l'intégration Git de VS Code.

%[https://www.youtube.com/watch?v=_-SjD_k7uIY]

Ce tutoriel est conçu pour que vous puissiez essayer les commandes au fur et à mesure. Nous commencerons donc par créer notre dépôt local.

## Comment créer un dépôt local

Nous voulons créer un site web de recettes, ou peut-être une application pour collecter et gérer des recettes. Et nous voulons créer un dépôt afin de pouvoir suivre facilement les changements apportés aux fichiers du projet.

Pour créer un dépôt local, suivez ces étapes :

Tout d'abord, ouvrez votre terminal ou invite de commande et naviguez jusqu'au répertoire où vous souhaitez créer votre projet.

Ensuite, initialisez un nouveau dépôt Git en utilisant la commande suivante.

```git
git init recipes
```

Cette commande crée un nouveau dossier pour le projet appelé `recipes` et initialise un nouveau dépôt Git dans ce dossier.

Le processus d'initialisation crée un dossier `.git` dans le dossier du projet qui stocke les fichiers et les données du dépôt.

Ce fichier peut être caché par défaut. Dans le Finder de Mac, utilisez `Command + Shift + . (point)` pour faire apparaître les fichiers cachés. Sur Windows, utilisez l'onglet Affichage de l'Explorateur de fichiers et cochez `Éléments cachés` pour afficher les fichiers cachés.

Lorsqu'un nouveau dépôt est initialisé, Git crée automatiquement une nouvelle branche principale. Selon vos paramètres Git, cette branche principale est créée avec le nom "main", "master", ou quelque chose de similaire.

Naviguez jusqu'au dossier du projet :

```git
cd recipes
```

Le dossier du projet est notre dossier de travail. Tous les fichiers de notre projet doivent être créés, mis à jour et modifiés à partir de ce dossier ou de ses sous-dossiers.

Ce dossier de travail est le dossier que Git surveille pour suivre nos changements.

Facultativement, vérifiez l'état du dépôt Git :

```git
git status
```

Le résultat des étapes ci-dessus est montré ci-dessous :

![Résultat des commandes ci-dessus.](https://www.freecodecamp.org/news/content/images/2023/02/image-193.png)
_Figure 1. Création d'un dépôt local_

La commande `init` nous indique qu'elle a initialisé un dépôt Git vide nommé `.git` dans le dossier que nous lui avons indiqué d'utiliser.

La commande `status` fournit l'état de notre dépôt. À ce stade, nous sommes sur la branche `main`, nous n'avons aucun commit, et nous n'avons rien à commiter.

Nous avons maintenant un dépôt local ! Ajoutons quelques fichiers au dépôt pour avoir quelque chose avec quoi travailler.

## Comment créer des fichiers

Le but principal d'un dépôt est de stocker une capture instantanée des fichiers de notre dossier de travail à un moment donné. Nous n'avons actuellement aucun fichier dans notre dossier de travail.

Ajoutons deux fichiers texte simples. Mais notez que le processus de branchement couvert dans cet article est le même avec tout type de fichiers de code.

Utilisez un éditeur de texte pour créer les deux fichiers : file1.txt et file2.txt. Ajoutez une ligne de contenu à chaque fichier pour identifier le fichier.

Si vous préférez créer les deux fichiers en utilisant la console, tapez ces commandes, une à la fois :

```git
echo file1 > file1.txt
echo file2 > file2.txt
```

Chacune de ces commandes "echo", ou "écrit" le texte de gauche dans le fichier de droite. Si le fichier n'existe pas, il le crée.

Utilisez un seul signe supérieur à `>` avec `echo` pour remplacer le contenu du fichier par le texte spécifié. Utilisez un double signe supérieur à `>>` pour ajouter le texte à la fin du fichier. Nous verrons le double signe supérieur à plus tard dans ce tutoriel.

Maintenant que nous avons un dépôt local et deux fichiers modifiés, committons ces fichiers dans le dépôt.

## Comment commiter des fichiers dans le dépôt local

Le commit de fichiers dans un dépôt local nécessite les étapes suivantes :

Tout d'abord, ajoutez les fichiers à la zone de staging de Git.

```git
git add .
```

Avant de commiter des fichiers dans le dépôt local, nous indiquons à Git quels fichiers nous voulons inclure dans ce commit en les ajoutant à une zone de staging. Basiquement, le staging nous permet de choisir sélectivement quels changements inclure dans un commit.

L'utilisation du `.` (point) ajoute tous les fichiers du dossier de travail (et ses sous-dossiers) à la zone de staging. Si vous ne voulez ajouter que des fichiers spécifiques, vous pouvez les lister à la place.

Pensez au staging comme à un panier d'achat. Vous pouvez mettre des articles dans votre panier d'achat ou en retirer sans vous engager à les acheter. Lorsque vous êtes prêt, vous vous engagez à acheter les articles qui sont dans votre panier.

Vous êtes maintenant prêt à commiter les fichiers stagés dans le dépôt local.

```git
git commit -m "Initial commit"
```

Ici, nous committons les fichiers de la zone de staging de Git dans le dépôt local.

L'option `-m` est pour un message de commit. Suivez le `-m` avec le message, entre guillemets. Assurez-vous de définir un message clair décrivant les changements que vous commitez. Plus d'informations sur les messages de commit dans la section suivante ci-dessous.

Ensuite, vous pouvez facultativement vérifier le commit en utilisant la commande `log` :

```git
git log
```

La commande `log` affiche l'historique des commits pour le dépôt avec le commit le plus récent en premier. Utilisez-la chaque fois que vous voulez voir ce qui s'est passé dans ce dépôt.

NOTE : Si votre fenêtre de terminal est trop petite pour afficher le log entier, cette commande ouvre automatiquement un écran de pagination pour paginer l'affichage. Utilisez les touches `PgUp`, `PgDn` ou les flèches pour paginer la sortie. Appuyez sur la touche `Q` pour quitter le paginateur.

Il existe un ensemble complet d'options disponibles pour la commande `log` pour filtrer ou limiter le log à des commits spécifiques. Il existe également des options pour rendre le log plus joli. [Voir la documentation](https://git-scm.com/docs/git-log) pour plus d'informations.

Le terminal après ces étapes est montré ci-dessous :

![Résultat du commit de fichiers dans le dépôt local](https://www.freecodecamp.org/news/content/images/2023/03/image-1.png)
_Figure 2. Commit de fichiers dans le dépôt local_

La commande `add` n'affiche pas de message.

La commande `commit` affiche la branche sur laquelle nous nous trouvons (`main`), les premiers caractères de l'id du commit (plus d'informations à ce sujet dans un instant), et le message de commit. Elle liste ensuite les fichiers modifiés. Dans cet exemple, il y avait 2 fichiers modifiés et les deux étaient des insertions (nouveaux fichiers).

Le nombre après `create mode` indique le type de fichier et les permissions. `100644` signifie que ce sont des fichiers réguliers, pas des dossiers, avec des permissions de lecture et d'écriture pour le propriétaire.

La commande `log` fournit l'historique des commits de la branche actuelle. Elle inclut une longue chaîne de nombres et de lettres appelée Secure Hash Algorithm ou SHA. Le SHA est un identifiant attribué à chaque commit. Techniquement, c'est une somme de contrôle basée sur les fichiers du commit plus le message de log, les informations de l'auteur et la date. Le log affiche également la personne qui a fait le commit (nom et email), la date du commit et le message de commit.

Nous avons maintenant notre branche `main` avec un seul commit. Nous sommes prêts à commencer à travailler sur notre projet.

Avant de continuer, couvrons un peu plus les messages de commit.

## Comment créer des messages de commit utiles

Un message de commit détaille ce que vous avez fait et pourquoi. Cela est particulièrement important lorsque vous travaillez en équipe car cela indique aux autres membres de l'équipe ce qu'il y a dans le commit. Mais c'est aussi utile lorsque vous travaillez seul car cela vous rappelle ce que vous avez fait.

Définir de bons messages de commit peut faciliter la recherche et la comparaison des commits précédents. Et comprendre le but d'un commit nous aide à nous sentir confiants lors de la fusion de ce commit.

Les messages de commit pourraient également être utilisés pour les notes de version lors de la travail sur des changements pour une application de production.

Voici quelques conseils pour créer de bons messages de commit :

* Décrivez le changement de manière concise. Essayez de le limiter à pas plus de 50 caractères. Si vous ne pouvez pas décrire le commit en 50 caractères, cela peut signifier que vous incluez trop de choses dans un commit. Et si vous vous surprenez à ajouter un "et", c'est un bon indicateur que vous avez plusieurs changements dans un seul commit.
* Décrivez ce qui a été fait, pas comment. Par exemple, au lieu de "Modifier 5 fichiers", utilisez "Ajouter un avis de copyright au pied de page".
* Utilisez la casse de la phrase avec seulement la première lettre en majuscule.
* Ne terminez pas par un point.
* Utilisez le mode impératif. C'est-à-dire, écrivez le message sous la forme d'une commande au présent.

Ce dernier point est un peu difficile pour moi car ma première pensée est d'utiliser le passé, décrivant ce que j'ai fait. Mais cela devrait être ce que le commit fera.

Pour m'aider à m'en souvenir, je pense à compléter la phrase "Ce commit va : " Par exemple : "Ce commit va améliorer le contraste des couleurs". Pas "amélioré" ou "amélioration".

Pour plus d'informations sur les messages de commit, voir cette vidéo :

%[https://youtu.be/9UlmPCMZ4tc]

Pour mieux démontrer le branchement, sautons un peu dans le temps et supposons que nous avons maintenant une version bêta de notre projet sortie pour plusieurs utilisateurs. Et nous avons une liste de tâches de fonctionnalités à terminer et de bugs/problèmes à corriger.

## Comment créer une branche

Créez une branche pour chaque tâche ou problème sur lequel vous travaillez. Cela garantit que votre travail sur la tâche ou le problème est isolé de votre base de code existante. Cela facilite le travail sur plusieurs parties du projet simultanément, ou l'essai d'idées sans affecter négativement votre base de code principale.

En suivant notre exemple, nous commençons par une tâche pour mettre à jour le style des recettes afin de rendre la liste des ingrédients plus claire et les étapes des recettes plus faciles à suivre.

Nous créons une branche pour la tâche en suivant ces étapes.

Tout d'abord, basculez vers la branche principale du projet :

```git
git checkout main
```

Pour notre exemple particulier, nous n'avons que notre branche `main` à ce stade, donc cette commande n'est pas nécessaire. Mais en général, il est important de s'assurer que vous êtes sur la branche `main` avant de créer une nouvelle branche.

Ensuite, créez une branche à partir de la branche actuelle :

```git
git branch style_change
```

Cette commande `branch` crée une branche avec le nom spécifié à partir de la branche actuelle. Dans ce cas, la branche est nommée `style_change`.

Mais cette commande ne bascule pas notre dossier de travail vers la nouvelle branche.

Ensuite, basculez vers la nouvelle branche :

```git
git checkout style_change
```

La commande `checkout` extrait la branche afin que vous puissiez travailler avec elle. Pensez-y comme à extraire un livre de la bibliothèque pour pouvoir le lire. Ou sélectionner un film d'un service de streaming pour pouvoir le regarder.

Dans le cadre du processus de checkout, Git copie les fichiers du commit le plus récent sur la branche spécifiée dans le dossier de travail afin que nous puissions travailler dessus. Lorsque nous insérons, éditons ou supprimons des fichiers dans notre dossier de travail, nous impactons la branche extraite.

Alternativement, vous pouvez utiliser une seule commande pour créer et basculer vers la nouvelle branche.

```git
git checkout -b style_change
```

L'option `-b` crée une nouvelle branche avec le nom fourni et extrait cette branche.

Facultativement, affichez la liste de toutes les branches pour confirmer la création de la branche :

```git
git branch
```

La commande `branch` liste toutes les branches existantes dans le dépôt.

En suivant ces étapes en utilisant la commande unique pour créer et basculer vers la nouvelle branche, le terminal apparaît comme montré ci-dessous :

![Résultat de la création d'une branche](https://www.freecodecamp.org/news/content/images/2023/02/image-266.png)
_Figure 3. Création d'une branche_

La première commande `checkout` nous indique que nous sommes déjà sur la branche `main`.

La deuxième commande `checkout` crée une nouvelle branche appelée `style_change` et bascule vers cette branche.

Dans le cadre du processus de checkout, les fichiers du dossier de travail sont modifiés pour correspondre aux fichiers du dernier commit de la branche `style_change`. Puisque c'est une nouvelle branche créée à partir de la branche `main`, le dernier commit de la nouvelle branche pointe vers le dernier commit de la branche à partir de laquelle elle a été créée, qui est `main`. Donc les fichiers du dossier de travail sont les fichiers du dernier commit de la branche `main`.

La commande `branch` liste les deux branches. La branche actuelle est indiquée par un astérisque (*).

Maintenant que nous avons extrait la nouvelle branche, nous pouvons apporter des modifications à notre dossier de travail et ces modifications n'impactent que cette branche. Notre base de code principale reste inchangée.

Pour simuler une modification de notre branche, ajoutons une ligne de texte à l'un de nos fichiers :

```git
echo Style changes >> file1.txt
```

Confirmez la modification en tapant le contenu du fichier :

```git
type file1.txt		// Sur windows
OU
cat file1.txt		// Sur un mac
```

Le résultat de ces deux commandes ressemble à ceci :

![Le résultat de la modification d'un fichier.](https://www.freecodecamp.org/news/content/images/2023/02/image-267.png)
_Figure 4. Modification d'un fichier_

À ce stade, nous avons deux fichiers dans notre dossier de travail, dont l'un a été modifié. Après avoir apporté un ensemble de modifications, nous voulons commiter ces modifications dans la branche.

## Comment commiter des modifications dans une branche

Alors que nous travaillons sur une tâche ou un problème, comme notre tâche de modifications de style, nous committons nos modifications. Le commit stocke une capture instantanée de notre dossier de travail ainsi que toutes les modifications stagées. Le commit stocke essentiellement notre progression sur la branche pour cette tâche ou ce problème.

Voici les étapes :

Tout d'abord, stockez les modifications à inclure dans le commit :

```git
git add .
```

Nous avons déjà utilisé cette commande. Elle indique à Git quels fichiers nous voulons inclure dans le commit en les ajoutant à une zone de staging.

Le `.` (point) ajoute tous les fichiers du dossier de travail (et ses sous-dossiers) à la zone de staging.

Ensuite, commitez les fichiers qui sont dans le staging :

```git
git commit -m "Restyle recipe ingredients"
```

Cette commande `commit` crée un nouveau commit. Comme nous l'avons utilisé précédemment, l'option `-m` signifie que nous fournissons un message de commit. Suivez le `-m` avec le message, entre guillemets.

Ou, si vous avez seulement modifié ou supprimé des fichiers, sans créer de nouveaux fichiers, vous pouvez stager et commiter les modifications de la branche en utilisant une seule commande :

`git commit -a -m "Restyle recipe ingredients"`

L'option `-a` stocke tous les fichiers modifiés et supprimés dans le dossier de travail, mais n'inclut pas les nouveaux fichiers. Cette commande `commit` crée ensuite une nouvelle capture instantanée de notre dossier de travail (à l'exception des nouveaux fichiers) et les commite.

Facultativement, vérifiez le commit en utilisant la commande `log` :

```git
git log
```

Nous avons utilisé cette commande précédemment pour afficher l'historique des commits du dépôt.

Le résultat est montré ci-dessous :

![Le résultat du commit des modifications dans une branche.](https://www.freecodecamp.org/news/content/images/2023/03/image-2.png)
_Figure 5. Commit des modifications dans une branche_

La commande `log` liste nos deux commits avec le plus récent en premier.

Continuez à apporter des modifications à la branche, en committant ces modifications si nécessaire. Envisagez de commiter chaque fois que vous avez terminé une partie logique de la tâche ou lorsque vous devez mettre la tâche de côté pour un autre travail ou lorsque vous partez pour la journée.

## Comment créer et commiter sur une autre branche

En tant que développeurs, nous sommes souvent détournés de notre tâche actuelle pour travailler sur une autre tâche ou un autre problème.

Pour notre exemple, disons que nous travaillons toujours sur la tâche de modifications de style, et nous recevons un problème urgent de nos utilisateurs que notre page de connexion ne fonctionne plus. Nous committons nos modifications actuelles dans la branche `style_changes` comme montré ci-dessus afin de pouvoir commencer à travailler sur le problème de connexion.

Nous voulons une nouvelle branche pour le problème de connexion afin de pouvoir garder notre travail sur ce problème séparé de notre base de code principale et de notre travail en cours sur la tâche de modifications de style.

Nous créons la nouvelle branche de problème de connexion à partir de notre branche `main` qui contient notre base de code actuellement déployée. De cette façon, nous pouvons déployer la correction sans inclure de code de nos tâches en cours.

Commencez par basculer vers la branche `main`.

```git
git checkout main
```

Cette commande extrait la branche `main`, remplaçant le code dans notre dossier de travail par le code du dernier commit de notre branche `main`.

Facultativement, confirmez le code dans le dossier de travail :

```git
type file1.txt		// Sur windows
OU
cat file1.txt		// Sur un mac
```

En tapant notre fichier `file1.txt`, nous voyons que nous n'avons pas notre modification de style. Notre dossier de travail contient maintenant le code original de notre branche `main`.

Ensuite, créez et basculez vers une nouvelle branche `login_issue` :

```git
git checkout -b login_issue
```

L'option `-b` signifie que nous créons une nouvelle branche avec le nom fourni et que nous extrayons cette branche.

Facultativement, confirmez la nouvelle branche :

```git
git branch
```

Le résultat de ces commandes est montré ci-dessous :

![Résultat de la création d'une autre branche](https://www.freecodecamp.org/news/content/images/2023/02/image-269.png)
_Figure 6. Création d'une autre branche_

La commande `branch` liste nos trois branches. L'astérisque (*) indique que nous avons extrait la branche `login_issue`.

Dans le cadre du processus de checkout, les fichiers du dossier de travail sont modifiés pour correspondre aux fichiers du dernier commit de la branche `login_issue`.

Puisque c'est une nouvelle branche créée à partir de la branche `main`, le dernier commit de la nouvelle branche pointe vers le dernier commit de la branche à partir de laquelle elle a été créée, qui est `main`. Donc les fichiers du dossier de travail sont les fichiers du dernier commit de la branche `main`.

Ensuite, nous apportons nos modifications pour corriger le problème de connexion. Nous allons simuler la modification en ajoutant une ligne de texte à notre autre fichier :

```git
echo Login changes >> file2.txt
```

Confirmez la modification en tapant le contenu du fichier :

```git
type file2.txt		// Sur windows
OU
cat file2.txt		// Sur un mac
```

Le contenu du fichier est montré ci-dessous :

![Résultat de la modification d'un fichier.](https://www.freecodecamp.org/news/content/images/2023/02/image-270.png)
_Figure 7. Modification d'un fichier_

Comme pour notre branche `style_change`, lorsque nous terminons nos modifications, nous committons ces modifications.

Stockez les modifications pour le commit :

```git
git add .
```

Comme nous l'avons vu précédemment, cette commande indique à Git quels fichiers nous voulons inclure dans le commit en les ajoutant à une zone de staging.

Ensuite, commitez les fichiers du staging vers la branche extraite :

```git
git commit -m "Fix login issue"
```

Cela crée un nouveau commit à partir de notre zone de staging.

Facultativement, vérifiez le commit en utilisant la commande `log` :

```git
git log
```

Voici le résultat de ces commandes.

![Résultat du commit des modifications.](https://www.freecodecamp.org/news/content/images/2023/03/image-3.png)
_Figure 8. Commit des modifications_

Remarquez dans le journal ci-dessus que nous ne voyons pas le commit de modification de style. C'est parce qu'il est dans la branche `style_change` et non dans cette branche `login_issue`.

Nous continuons à apporter des modifications jusqu'à ce que le problème de connexion soit résolu.

Pendant que vous travaillez sur le problème de connexion, si vous devez revenir à la tâche de modification de style :

* Vérifiez toutes les modifications actuelles du problème de connexion.
* Utilisez la commande `checkout` pour basculer vers la branche `style_change`.
* Travaillez sur la tâche, en vérifiant toutes les modifications.
* Lorsque vous êtes prêt, revenez à la branche `login_issue`.

Utilisez la commande `branch` à tout moment pour afficher votre liste de branches et confirmer quelle branche vous avez extraite.

## Comment fusionner une branche

Lorsque nous avons terminé la tâche ou le problème, nous voulons fusionner le code de cette tâche ou de ce problème dans notre base de code principale. Nous pouvons ensuite optionnellement déployer le changement pour les utilisateurs.

Confirmons d'abord le contenu de nos fichiers en tapant les deux commandes, une à la fois :

```git
type file1.txt		// Sur windows
type file2.txt
OU
cat file1.txt		// Sur un mac
cat file2.txt
```

Le résultat est montré ci-dessous :

![Affiche le contenu actuel de la branche login_issue](https://www.freecodecamp.org/news/content/images/2023/02/image-272.png)
_Figure 9. Contenu actuel de la branche login_issue_

Notre `file1.txt` contient notre texte original, pas nos modifications de style. Notre `file2.txt` contient notre nouveau texte de connexion.

Maintenant, nous sommes prêts à fusionner notre branche `login_issue` dans notre branche `main`.

Tout d'abord, basculez vers la branche `main` :

```git
git checkout main
```

Pour être clair sur ce qui se passe, vérifions à nouveau le contenu de nos fichiers :

```git
type file1.txt		// Sur windows
type file2.txt
OU
cat file1.txt		// Sur un mac
cat file2.txt
```

Voici le résultat :

![Contenu de la branche main avant la fusion.](https://www.freecodecamp.org/news/content/images/2023/02/image-273.png)
_Figure 10. Contenu de la branche main avant la fusion_

Remarquez que les deux fichiers contiennent uniquement notre texte original. Lorsque nous basculons vers la branche `main`, le contenu de notre dossier de travail a été modifié pour correspondre aux fichiers du dernier commit de la branche `main`. Il n'inclut aucune des modifications que nous avons apportées dans nos autres branches.

Ensuite, fusionnez la branche de tâche ou de problème dans la branche `main`.

`git merge login_issue`

Cette commande fusionne les modifications de la branche spécifiée dans la branche actuelle. Si des conflits surviennent, Git vous invite à les résoudre avant que la fusion ne puisse être terminée.

Nous allons à nouveau vérifier le contenu de nos fichiers :

```git
type file1.txt		// Sur windows
type file2.txt
OU
cat file1.txt		// Sur un mac
cat file2.txt
```

Voici le résultat de ces commandes :

![Contenu de la branche main après la fusion.](https://www.freecodecamp.org/news/content/images/2023/03/image-4.png)
_Figure 11. Contenu de la branche main après la fusion_

La commande `merge` affiche des informations sur le type de fusion ainsi que les fichiers qui ont été fusionnés.

Dans ce cas, Git a utilisé un type de fusion rapide. Il s'agit d'une fusion simple que Git peut utiliser lorsqu'il n'y a pas de nouvelles modifications sur la branche actuelle depuis la création de la branche fusionnée.

Les commits de la branche fusionnée sont effectivement incorporés dans la branche actuelle. Pas besoin d'un nouveau commit de fusion et il n'y a aucune possibilité de conflit de fusion.

Pour notre exemple, nous n'avons apporté aucune modification sur la branche actuelle (`main`) depuis le point où nous avons créé la branche `login_issue`. Ainsi, les commits de la branche `login_issue` ont pu être incorporés directement dans la branche `main`.

Nous pouvons voir à partir du contenu de `file2.txt` que notre branche `main` contient maintenant les modifications de notre branche `login_issue` ! Nous avons fusionné avec succès la branche dans `main`.

Une fois qu'une branche a été fusionnée dans la base de code principale, il est sûr de la supprimer.

## Comment supprimer une branche

Supprimez toute branche dont vous n'avez plus besoin pour garder votre dépôt propre et plus facile à gérer.

Commençons par confirmer notre liste actuelle de branches :

```git
git branch
```

Si vous n'êtes pas sur la branche `main`, basculez vers la branche `main` :

```git
git checkout main
```

Vous ne pouvez pas supprimer la branche sur laquelle vous vous trouvez. En basculant vers la branche `main`, vous pouvez supprimer n'importe quelle autre branche.

Supprimez la branche de tâche ou de problème souhaitée :

```git
git branch -d login_issue
```

L'option `-d` supprime la branche spécifiée du dépôt local.

Facultativement, confirmez la liste résultante de branches :

```git
git branch
```

Le résultat de ces commandes est montré ci-dessous :

![Résultat de la suppression d'une branche.](https://www.freecodecamp.org/news/content/images/2023/03/image-5.png)
_Figure 12. Suppression d'une branche_

La première commande `branch` liste les trois branches.

La commande `branch -d` supprime la branche définie et journalise l'action.

La dernière commande `branch` liste nos deux branches restantes. Notre branche de problème a été supprimée avec succès !

Maintenant, qu'en est-il de notre branche originale ? Notre branche `main` a nos modifications de problème de connexion fusionnées, mais notre branche `style_change` originale ne les a pas.

## Comment fusionner "main" vers les branches

Pour minimiser les conflits de fusion plus étendus plus tard, il est souvent judicieux de garder toutes les branches de tâches et de problèmes à jour avec `main`. Cela signifie qu'après avoir fusionné les modifications d'une branche dans la branche `main`, nous voulons fusionner ces modifications de la branche `main` vers toutes les branches de tâches ou de problèmes restantes.

Tout d'abord, basculez vers l'une des branches de tâches ou de problèmes :

```git
git checkout style_change
```

Ici, nous basculons vers la branche `style_change` car c'est notre seule autre branche.

Facultativement, affichez les commits de cette branche :

```git
git log
```

Voici le résultat de ces commandes :

![Résultat du journal de la branche style_change avant la fusion de main](https://www.freecodecamp.org/news/content/images/2023/03/image-6.png)
_Figure 13. Journal de la branche style_change avant la fusion de main_

Remarquez que la commande `log` liste le commit initial et le changement de style. Elle n'a pas notre correction de connexion.

Maintenant, fusionnez la branche `main` dans la branche actuelle :

```git
git merge main
```

Cette commande `merge` fusionne l'historique des modifications de la branche `main` dans la branche actuelle, qui dans ce cas est la branche `style_change`.

Facultativement, affichez à nouveau les commits de la branche :

```git
git log
```

Le résultat est montré ci-dessous :

![Résultat du journal de la branche style_change après la fusion de main](https://www.freecodecamp.org/news/content/images/2023/03/image-9.png)
_Figure 14. Journal de la branche style_change après la fusion de main_

Remarquez que dans ce cas, Git n'a pas pu utiliser le type de fusion rapide. C'est parce que les branches `style_change` et `main` ont divergé, ce qui signifie qu'elles ont toutes deux changé depuis le moment où nous avons créé la branche `style_change`.

Git a plutôt utilisé une stratégie `ort` pour fusionner les modifications. [Voir la documentation](https://git-scm.com/docs/merge-strategies#Documentation/merge-strategies.txt-ort) pour plus d'informations sur cette stratégie de fusion.

Parce que Git n'a pas pu utiliser le type de fusion rapide, le processus de fusion a créé un nouveau commit, appelé un _commit de fusion_. Un commit de fusion représente une combinaison des modifications apportées sur les branches séparées.

La commande `log` dans la Figure 14 inclut nos commits de style et les commits fusionnés de `main`. En commençant par le haut :

* Le commit de fusion créé par le processus de fusion.
* Le commit de notre correction de problème de connexion fusionné de `main`.
* Le commit de notre première modification de style.
* Notre commit initial à `main` avant de créer la branche.

À ce stade, nous pouvons continuer à travailler sur notre tâche de style. Ou utiliser les étapes que nous avons couvertes pour ajouter des branches pour d'autres tâches ou problèmes.

## Comment terminer notre projet

Terminons notre projet, en apportant une dernière modification à notre branche, puis en fusionnant nos modifications dans `main`. Ces étapes ont une explication minimale puisque nous les avons couvertes en détail plus tôt dans ce tutoriel.

Basculez vers la branche `style_change` :

```git
git checkout style_change
```

Si vous étiez déjà sur cette branche, elle affichera un message.

Ensuite, apportez les modifications finales. Nous allons simuler les modifications en ajoutant une autre ligne au fichier `file2.txt` :

```git
echo More style changes >> file2.txt
```

Ajoutez les fichiers au staging :

```git
git add .
```

Et commitez les modifications :

```git
git commit -m "Restyle recipe steps"
```

Le résultat de ces étapes est ci-dessous :

![Résultat d'une modification supplémentaire.](https://www.freecodecamp.org/news/content/images/2023/03/image-10.png)
_Figure 15. Une modification supplémentaire_

Maintenant, nous avons terminé la tâche et sommes prêts à la fusionner dans la branche `main`.

Basculez vers la branche `main` :

```git
git checkout main
```

Fusionnez la branche `style_change` dans `main` :

```git
git merge style_change
```

Supprimez la branche `style_change` :

```git
git branch -d style_change
```

Facultativement, confirmez que la branche a été supprimée :

```git
git branch
```

Cela donne le résultat montré ci-dessous :

![Résultat de la fusion dans main](https://www.freecodecamp.org/news/content/images/2023/03/image-11.png)
_Figure 16. Fusion dans main_

Remarquez que la fusion a pu utiliser la stratégie de fusion rapide.

À ce stade, nous n'avons plus que notre branche `main`.

Facultativement, confirmez l'état de la branche `main` :

```git
git log
```

Voici le résultat :

![Journal de l'historique final des commits.](https://www.freecodecamp.org/news/content/images/2023/03/image-13.png)
_Figure 17. Historique final des commits_

La commande `log` affiche :

* La dernière modification de style fusionnée de la branche `style_change`.
* Le commit de fusion créé par le processus de fusion précédent.
* Le commit de notre correction de problème de connexion fusionné de `main`.
* Le commit de notre première modification de style.
* Notre commit initial à `main`.

Nous avons maintenant notre base de code principale à jour !

Si vous voulez supprimer complètement tout le travail que vous avez fait, supprimez le dossier `recipes`. Cela supprime les fichiers et le dépôt Git.

## Conclusion

Les étapes de base pour travailler avec des branches sont :

* Basculer vers la branche `main`.
* Créer la nouvelle branche de tâche ou de problème à partir de la branche `main` et l'extraire.
* Apporter des modifications aux fichiers dans le dossier de travail.
* Stager et commiter les modifications dans la branche de tâche ou de problème.
* Lorsque la tâche ou le problème est terminé, basculer vers la branche `main` et fusionner les modifications de la branche de tâche ou de problème dans `main`.
* Supprimer la branche de tâche ou de problème.

Notez que ces étapes sont un peu plus complexes lorsque vous travaillez avec un dépôt distant. Dans ce cas, vérifiez avec votre équipe ou communauté open source les étapes supplémentaires appropriées pour utiliser des branches avec un dépôt distant.

La gestion des branches est une partie essentielle du travail avec Git. En suivant les commandes décrites dans cet article, vous pouvez créer, commiter, fusionner et supprimer des branches avec facilité.

Avec ces compétences, vous pouvez travailler sur plusieurs fonctionnalités ou corrections de bugs en même temps sans affecter la base de code principale, et fusionner vos modifications une fois qu'elles sont terminées.