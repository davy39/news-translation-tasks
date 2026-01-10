---
title: Apprendre les bases de Git – Un guide sur les tâches de développement quotidiennes
date: '2024-04-03T03:57:39.000Z'
author: Samyak Jain
authorURL: https://www.freecodecamp.org/news/author/samyak/
originalURL: https://freecodecamp.org/news/learn-git-basics
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Learn-Git-Basics-Cover-3--1-.png
tags:
- name: beginner
  slug: beginner
- name: Git
  slug: git
- name: handbook
  slug: handbook
- name: version control
  slug: version-control
seo_desc: "Welcome to my comprehensive guide on Git, the distributed version control\
  \ system that has revolutionized collaboration and code management in software development.\
  \ \nWhether you're a seasoned developer or just starting your journey in programming,\
  \ und..."
---


Bienvenue dans mon guide complet sur Git, le système de gestion de versions décentralisé qui a révolutionné la collaboration et la gestion du code dans le développement logiciel.

<!-- more -->

Que vous soyez un développeur chevronné ou que vous commenciez tout juste votre parcours en programmation, comprendre Git est essentiel pour garder un contrôle total sur votre code, gérer efficacement vos projets et collaborer avec d'autres personnes.

Dans ce tutoriel, je vous guiderai à travers les fondamentaux de Git, couvrant tout, de son flux de travail de base aux stratégies de branchement avancées et aux techniques de rebasage (rebasing).

À la fin de ce guide, vous aurez une compréhension solide des concepts clés de Git et vous serez confiant et bien équipé pour l'utiliser efficacement dans votre flux de travail de développement.

## Prérequis :

Tout ce dont vous avez besoin, c'est d'un esprit curieux et de l'envie d'apprendre. Ce guide est conçu pour les débutants, donc aucune connaissance préalable des systèmes de gestion de versions ou de la programmation n'est requise. Que vous soyez un novice complet ou que vous ayez une certaine expérience du code, vous trouverez ce tutoriel accessible et facile à suivre.

## **Table des matières :**

1.  [Qu'est-ce que Git ?][1]  
    – [Différence avec les autres systèmes de gestion de versions][2]  
    – [Les trois états et le flux de travail de base de Git][3]
2.  [Configuration initiale de Git][4]
3.  [Obtenir de l'aide dans Git][5]
4.  [Comment obtenir un dépôt Git][6]  
    – [Initialiser un dépôt dans un répertoire existant][7]  
    – [Cloner un dépôt existant dans Git][8]
5.  [Comment enregistrer des modifications dans le dépôt][9]
6.  [Visualiser l'historique des commits dans Git][10]
7.  [Annuler des actions dans Git][11]
8.  [Dépôts distants dans Git][12]
9.  [L'étiquetage (tagging) dans Git][13]
10.  [Les alias Git][14]
11.  [Les branches dans Git][15]  
    – [Créer une nouvelle branche dans Git][16]  
    – [Comprendre les branches][17]  
    – [Basculer vers une autre branche dans Git][18]  
    – [Visualiser les branches dans Git][19]
12.  [Comment gérer les branches dans Git][20]  
    – [Gérer les branches fusionnées][21]  
    – [Renommer des branches][22]  
    – [Changer le nom de la branche par défaut][23]
13.  [Flux de travail avec les branches][24]
14.  [Le rebasage (rebasing) dans Git][25]
15.  [Conclusion][26]

## Qu'est-ce que Git ?

Git est un système de gestion de versions décentralisé qui vous aide, vous et votre équipe, à collaborer efficacement tout en sécurisant l'historique de votre projet. C'est comme avoir une machine à remonter le temps pour votre code !

### Ce qui différencie Git des autres systèmes de gestion de versions

#### Différence conceptuelle :

L'élément majeur qui distingue Git des autres outils est sa façon de concevoir les données. Au lieu de stocker les modifications apportées aux fichiers, Git considère ses données comme une série d'instantanés (snapshots) de votre projet. Cela signifie qu'à chaque fois que vous effectuez une modification et que vous l'enregistrez (commit), Git prend une photo de tous vos fichiers à ce moment précis. Si un fichier n'a pas changé, Git conserve simplement un lien vers le fichier identique précédent.

#### Opérations locales :

Avec Git, la plupart des actions que vous effectuez ne nécessitent pas de connexion à un serveur. Comme vous possédez l'intégralité de l'historique du projet sur votre ordinateur, les opérations sont extrêmement rapides. Vous pouvez parcourir l'historique du projet ou voir les différences entre les versions sans attendre de réponse d'un serveur.

#### Intégrité des données :

Git s'assure que rien ne soit perdu ou corrompu. Chaque fichier et répertoire fait l'objet d'une somme de contrôle (checksum), et Git sait si quelque chose change.

Git utilise un hachage SHA-1, un code unique pour chaque version d'un fichier. Si une modification est apportée au contenu, même d'un seul caractère, cela entraînera un hachage SHA-1 différent.

#### Modèle d'ajout uniquement (Append-Only) :

Dans Git, presque toutes les actions ajoutent des données au projet, ce qui rend difficile la perte accidentelle d'informations. Une fois que vous avez validé (commit) vos modifications, elles sont stockées en toute sécurité. L'expérimentation est moins risquée avec Git.

### Les trois états et le flux de travail de base de Git

Comprendre les trois états de Git — modifié, indexé (staged) et validé (committed) — est essentiel pour une gestion de versions efficace :

-   **Modifié (Modified)** : Modifications apportées aux fichiers dans votre **Arbre de travail (Working tree)** qui ne sont pas encore validées.
-   **Indexé (Staged)** : Modifications marquées dans la **Zone de transit (Staging area)** pour être incluses dans le prochain commit.
-   **Validé (Committed)** : Modifications stockées de manière permanente dans le **Répertoire Git** local.

**Flux de travail de base de Git** :

1.  **Modifiez les fichiers** dans votre arbre de travail.
2.  **Indexez les modifications** que vous souhaitez inclure dans le prochain commit.
3.  **Validez les modifications (commit)**, ce qui enregistre de façon permanente les instantanés dans le répertoire Git.

## Configuration initiale de Git

Configurer Git pour la première fois implique de personnaliser votre environnement Git selon vos préférences. Mais d'abord, vous devrez télécharger Git depuis [Git - Downloads][27] ou utiliser le paquet Chocolatey. Suivez ensuite les instructions d'installation et vous devriez être prêt.

### Configuration de Git

Nous utilisons l'outil `git config` pour personnaliser notre environnement Git. Cet outil nous permet de récupérer et de définir des variables de configuration qui dictent le fonctionnement de Git. Ces variables peuvent être stockées à trois endroits différents :

1.  **Configuration au niveau du système :**  
    Stockés dans le fichier `/etc/gitconfig`, ces paramètres s'appliquent à tous les utilisateurs du système et à tous les dépôts. Nous pouvons interagir avec ce fichier en utilisant l'option `--system` avec `git config`.
2.  **Configuration spécifique à l'utilisateur :**  
    Stockées dans `~/.gitconfig` ou `~/.config/git/config`, ces valeurs sont spécifiques à vous en tant qu'utilisateur. Nous pouvons interagir avec ce fichier en utilisant l'option `--global` avec `git config`, ce qui affectera tous les dépôts sur lesquels vous travaillez sur votre système.
3.  **Configuration spécifique au dépôt :**  
    Stockés dans le fichier `.git/config` au sein d'un dépôt spécifique, ces paramètres remplacent les configurations globales et ne s'appliquent qu'à ce dépôt.

Chaque niveau de configuration remplace les valeurs du niveau précédent. Par exemple, les valeurs dans `.git/config` remplaceront celles de `~/.gitconfig`.

Pour afficher tous les paramètres de configuration et leurs sources/origines :

```bash
$ git config --list --show-origin
```

#### Comment configurer votre identité dans Git :

L'identité dans Git est utilisée pour attribuer correctement les commits. Configurons votre nom d'utilisateur et votre adresse e-mail.

```bash
$ git config --global user.name "Votre Nom"
$ git config --global user.email "votre.email@exemple.com"
```

Si vous avez besoin de remplacer cela pour des projets spécifiques, vous pouvez omettre l'option `--global` lors de la définition des valeurs, et elles ne s'appliqueront qu'à ce dépôt particulier.

#### Comment configurer votre éditeur de texte par défaut

Après avoir configuré votre identité, il est important de définir votre éditeur de texte par défaut dans Git. Cet éditeur sera utilisé lorsque Git aura besoin que vous saisissiez des messages, comme lors de la rédaction de messages de commit ou de la résolution de conflits de fusion.

Par défaut, Git utilise l'éditeur de texte par défaut de votre système. Cependant, si vous préférez utiliser un autre éditeur, comme Emacs, vous pouvez le configurer ainsi :

```bash
$ git config --global core.editor "emacs"
```

Sur les systèmes Windows, la configuration d'un éditeur de texte différent nécessite de spécifier le chemin complet de son fichier exécutable. Par exemple, si vous souhaitez utiliser Notepad++, vous pourriez utiliser une commande comme celle-ci :

```bash
$ git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"
```

Assurez-vous de fournir le chemin correct vers le fichier exécutable de votre éditeur de texte.

D'ailleurs, ces options – `"-multiInst -notabbar -nosession -noPlugin"` – sont utilisées pour personnaliser le comportement de Notepad++ lorsqu'il est lancé par Git.

#### Comment changer le nom de la branche par défaut dans Git (optionnel) :

Par défaut, lorsque vous initialisez un nouveau dépôt avec `git init`, Git crée une branche nommée `master`. Mais à partir de la version 2.28 de Git, vous avez la possibilité de définir un nom différent pour la branche initiale.

```bash
$ git config --global init.defaultBranch main
```

Ceci change globalement le nom de la branche par défaut en 'main'.

#### Comment vérifier la configuration/les paramètres dans Git :

Vous pouvez visualiser votre configuration Git en utilisant :

```bash
$ git config --list
$ git config user.name  # Pour vérifier un paramètre spécifique (ex: nom d'utilisateur) :
```

La commande `git config --list` liste tous les paramètres de configuration que Git peut trouver à ce moment-là.

## Comment obtenir de l'aide dans Git

Il existe trois façons équivalentes d'obtenir une aide détaillée pour n'importe quelle commande Git :

1.  Commande Git Help : `$ git help <verbe>`
2.  Utilisation de l'option `--help` : `$ git <verbe> --help`
3.  Pages de manuel (manpages) : `$ man git-<verbe>`

Remplacez `<verbe>` par la commande pour laquelle vous avez besoin d'aide. Par exemple, pour obtenir de l'aide sur la commande `config`, vous pouvez taper :

```bash
$ git help config
ou
$ man git-config
```

Ces commandes fonctionnent également hors ligne, ce qui est pratique.

Si vous avez besoin d'informations rapides et concises sur les options disponibles pour une commande Git, vous pouvez utiliser l'option `-h` :

```bash
$ git add -h    # Ceci affichera les options disponibles pour la commande add
```

## Comment obtenir un dépôt Git

Pour commencer à utiliser Git, vous devez généralement obtenir un dépôt Git. Il existe essentiellement deux façons principales de commencer :

### 1. Comment initialiser un dépôt dans un répertoire existant dans Git

Ouvrez un terminal ou une invite de commande. Utilisez la commande `cd` pour changer de répertoire vers l'emplacement de votre projet : `cd /chemin/vers/votre/projet`.

Une fois que vous êtes dans le répertoire de votre projet, initialisez un dépôt Git en exécutant :

```bash
$ git init
```

Cette commande crée un nouveau sous-répertoire nommé `.git` où Git stocke tous les fichiers nécessaires à votre dépôt Git. À ce stade, aucun de vos fichiers de projet n'est encore suivi.

Maintenant, supposons que vous ayez certains fichiers que vous voulez que Git commence à suivre :

```bash
$ git add *.py        # Ajouter tous les fichiers Python
$ git add README.md   # Ajouter le fichier README
$ git commit -m 'Initial commit'
```

`git add` ajoute les fichiers à la zone de transit, indiquant que vous souhaitez les inclure dans le prochain commit, puis valide les modifications. Le drapeau `-m` vous permet d'ajouter un message descriptif au commit.

### 2. Comment cloner un dépôt existant dans Git :

La deuxième façon d'obtenir un dépôt Git est d'en cloner un existant. C'est utile lorsque vous souhaitez travailler sur un projet qui existe déjà ailleurs (par exemple, un projet auquel vous aimeriez contribuer).

**Note :** Lorsque vous clonez un dépôt, Git récupère une copie complète de presque toutes les données présentes sur le serveur. Cela inclut chaque version de chaque fichier de l'historique du projet. Cela signifie que vous aurez une copie complète de l'historique du dépôt sur votre machine locale.

Pour cloner un dépôt, utilisez la commande `git clone` suivie de l'URL du dépôt que vous souhaitez cloner. Par exemple, pour cloner le dépôt grok-1, vous pouvez utiliser :

```bash
$ git clone https://github.com/xai-org/grok-1.git
```

Ceci crée un répertoire nommé grok-1, initialise un répertoire `.git` à l'intérieur, et télécharge toutes les données de ce dépôt.

Au fait, `.git` est juste une convention pour signifier que l'URL pointe vers un dépôt Git. Vous pouvez l'utiliser ou non, cela n'a pas d'importance.

Si vous souhaitez cloner dans un répertoire avec un nom différent, vous pouvez le spécifier. Pour cloner le dépôt grok-1 dans un répertoire nommé "chatgpt" au lieu de "grok-1", faites ceci :

```bash
$ git clone https://github.com/xai-org/grok-1.git chatgpt
```

Git propose différents protocoles de transfert pour cloner des dépôts. L'exemple ci-dessus utilise le protocole `https://`, mais vous pourriez aussi voir `git://` ou `user@server:path/to/repo.git`, qui utilise le protocole de transfert SSH.

## Comment enregistrer des modifications dans le dépôt

Maintenant que vous avez configuré un dépôt Git, vous devrez souvent apporter des modifications et les enregistrer dans votre dépôt. Le processus implique le suivi des fichiers, l'indexation des modifications et la validation des instantanés. Explorons les étapes impliquées :

![cycle de vie](https://www.freecodecamp.org/news/content/images/2024/03/lifecycle.png)

crédit image - https://git-scm.com/

### 1. Comment vérifier l'état de vos fichiers dans Git :

Lorsque vous travaillez avec un dépôt Git, il est crucial de comprendre l'état de vos fichiers.

Git classe les fichiers en deux types : suivis (tracked) et non suivis (untracked). Les fichiers suivis sont ceux que Git reconnaît, soit parce qu'ils faisaient partie du dernier instantané (commit), soit parce qu'ils ont été indexés. Les fichiers non suivis sont tout le reste — des fichiers que Git ne surveille pas actuellement. Pour vérifier l'état de votre dépôt :

```bash
$ git status
```

Cette commande fournit des informations complètes sur la branche actuelle, son état de synchronisation et l'état de vos fichiers.

`git status` suggère également des actions à entreprendre. Par exemple, lorsque des fichiers sont modifiés mais non indexés pour le commit, `git status` suggère d'utiliser `git add <file>` pour les indexer. Il suggère également d'utiliser `git checkout -- <file>` pour annuler les modifications dans le répertoire de travail. Ces suggestions simplifient votre flux de travail en offrant un accès rapide aux commandes Git pertinentes.

De plus, `git status` propose un mode court (`git status -s`), qui présente une vue plus concise de vos modifications en utilisant des symboles comme M (modifié), A (ajouté) et ?? (non suivi) pour représenter l'état des fichiers.

### 2. Comment suivre de nouveaux fichiers dans Git

Lorsque vous créez un nouveau fichier dans votre projet, Git le considère initialement comme non suivi. Pour commencer à suivre un nouveau fichier, vous devez l'ajouter à la zone de transit à l'aide de la commande `git add`.

Par exemple, créons un nouveau fichier appelé `index.html` pour notre projet et ajoutons-le à la zone de transit :

```bash
$ touch index.html
$ git add index.html
```

Après l'ajout, l'exécution de `git status` montrera que le fichier `index.html` est maintenant suivi et indexé pour le commit.

### 3. Comment indexer des fichiers modifiés dans Git

Si vous modifiez un fichier suivi existant, vous devez indexer les modifications avec `git add`. Supposons que nous modifions un fichier existant appelé `styles.css` :

```bash
$ vim styles.css
```

Après avoir apporté les modifications, indexez le fichier :

```bash
$ git add styles.css
```

Désormais, lorsque vous vérifierez l'état, vous verrez à la fois le fichier modifié et le nouveau fichier indexés pour le commit.

### 4. Comment ignorer des fichiers dans Git

Souvent, il y a des fichiers ou des répertoires au sein d'un projet qui ne sont pas destinés à être suivis par Git. Il peut s'agir de fichiers journaux (logs), de fichiers de build ou d'informations sensibles comme des paramètres d'environnement local (tels que \*.env ou config.json). Vous pouvez spécifier ces fichiers à ignorer à l'aide d'un fichier `.gitignore`.

Créez un fichier `.gitignore` :

```bash
$ nano .gitignore
```

Listez les modèles de fichiers ou de répertoires que vous souhaitez ignorer :

```bash
$ echo '*.log' >> .gitignore
$ echo 'build/' >> .gitignore
```

Ici, nous disons à Git d'ignorer tous les fichiers avec une extension `.log` et le répertoire `build/`.

****Note :**** Les fichiers déjà suivis par Git avant d'être ajoutés au fichier `.gitignore` resteront suivis. Pour les supprimer, vous devrez manuellement arrêter de les suivre à l'aide de commandes Git.

Voici quelques modèles que vous pouvez utiliser pour travailler plus efficacement avec Git :

-   ****Cibler précisément des fichiers individuels ou des extensions :**** Par exemple, `test.txt` ignore uniquement ce fichier spécifique, tandis que `*.log` ignore tous les fichiers se terminant par `.log`.
-   ****Caractères génériques pour des correspondances plus larges :**** L'astérisque (`*`) correspond à n'importe quel nombre de caractères. Par exemple, `*.doc` ignore tous les fichiers avec l'extension `.doc`, quel que soit leur nom.

### 5. Comment visualiser les modifications dans Git :

Si vous souhaitez voir les modifications exactes que vous avez apportées à vos fichiers avant de les valider, vous pouvez utiliser la commande `git diff`.

Pour voir les modifications non indexées :

```bash
$ git diff 
```

Et pour voir les modifications indexées :

```bash
$ git diff --cached README.md
```

`git diff` fournit une vue détaillée des modifications réelles. Utilisez `git diff <filename>` pour vous concentrer sur les changements au sein d'un fichier particulier.

### 6. Comment valider (commit) les modifications :

Lorsque vous êtes prêt à valider vos modifications, utilisez la commande `git commit`. Cela ouvre votre éditeur de texte pour que vous puissiez fournir un message de commit. Alternativement, vous pouvez utiliser le drapeau `-m` pour ajouter un message de commit directement :

Une fois que vous avez indexé les modifications que vous souhaitez inclure dans le commit, vous pouvez les valider avec `git commit` :

```bash
$ git commit -m "Votre message de commit ici"
```

### 7. Comment supprimer des fichiers dans Git :

Si vous devez supprimer un fichier du suivi de Git, vous pouvez utiliser `git rm`. Cela supprime le fichier à la fois du dépôt et du répertoire de travail. Supposons que vous vouliez supprimer un fichier nommé `temp.txt` :

```bash
$ git rm temp.txt
```

Si vous voulez seulement le supprimer du dépôt mais le conserver dans le répertoire de travail, utilisez l'option `--cached` :

```bash
$ git rm --cached temp.txt
```

### 8. Comment déplacer (ou renommer) des fichiers dans Git :

Git ne suit pas explicitement les déplacements de fichiers. Mais vous pouvez utiliser `git mv` pour renommer ou déplacer des fichiers au sein de votre dépôt. Par exemple, pour renommer `old_file.txt` en `new_file.txt` :

```bash
$ git mv old_file.txt new_file.txt
```

Cette commande indexera le renommage, et il sera reflété dans le prochain commit.

C'est l'équivalent de déplacer manuellement le fichier, puis d'utiliser `git rm` pour supprimer l'ancien fichier, et enfin `git add` pour ajouter le nouveau fichier. `git mv` regroupe essentiellement ces étapes en une seule commande.

Ces commandes constituent le flux de travail de base pour apporter des modifications, les indexer et les valider dans votre dépôt Git.

## Comment visualiser l'historique des commits dans Git

Après avoir créé plusieurs commits ou cloné un dépôt, la commande `git log` vous permet d'examiner l'historique des commits.

Par défaut, elle liste les commits dans l'ordre chronologique inverse, affichant chaque commit avec sa somme de contrôle SHA-1, le nom et l'e-mail de l'auteur, la date et le message du commit.  
Voyons maintenant comment nous pouvons améliorer cette sortie :

### Comment visualiser les différences entre les commits dans Git :

Pour voir la différence introduite dans chaque commit, vous pouvez utiliser l'option `-p` ou `--patch` :

```bash
$ git log -p -2    # -2 est utilisé pour voir les différences introduites dans chacun des deux derniers commits
```

### Comment afficher des statistiques dans Git :

L'option `--stat` fournit des statistiques résumées pour chaque commit, incluant les fichiers modifiés, les lignes ajoutées/supprimées et un résumé.

```bash
$ git log --stat
```

### Comment personnaliser le format de sortie de git log :

L'option `--pretty` vous permet de modifier le format de sortie des logs. Diverses options sont disponibles pour différents formats :

-   `oneline` : Résumé concis de chaque commit sur une seule ligne.
-   `short` : Format par défaut avec l'auteur, la date et le message.
-   `full` : Format détaillé avec le hash du commit, l'auteur, la date, le message et le diff.
-   `fuller` : Format encore plus détaillé, incluant les chemins complets des fichiers.
-   `format` : Personnalisez la sortie à l'aide de spécificateurs de format.

```bash
$ git log --pretty=oneline
```

**Spécificateurs de format utiles pour** `--pretty=format` :

-   `%h :` Hash de commit abrégé
-   `%an :` Nom de l'auteur
-   `%ae :` E-mail de l'auteur
-   `%ad :` Date de l'auteur
-   `%s :` Sujet (message du commit)

```bash
$ git log --pretty=format:"%h %an %ad %s"
```

**Graphique ASCII** :

En utilisant `--graph`, vous pouvez également visualiser l'historique des branches et des fusions.

```bash
$ git log --pretty=format:"%h %s" --graph
```

### Comment limiter la sortie de git log :

En plus des options de formatage, `git log` propose diverses options de limitation pour affiner l'historique des commits affiché.

-   `-<n> :` Affiche seulement les n derniers commits.
-   `--since, --until :` Limite les commits à ceux effectués après/avant la date spécifiée.
-   `--author :` Affiche uniquement les commits d'un auteur spécifique.
-   `--grep :` Filtre les commits par mot-clé dans les messages de commit.
-   `-S :` Affiche les commits changeant une chaîne spécifique.

****Exemple d'utilisation :**** Voir les 3 derniers commits de l'auteur Abbey depuis une certaine date, avec les détails du patch :

```bash
$ git log --author="Abbey" --since="2024-01-01" -p -3
```

## Comment annuler des actions dans Git

Annuler des modifications est un besoin courant dans Git, et plusieurs options sont disponibles à cet effet.

### Comment annuler un commit dans Git

Si vous avez validé trop tôt ou si vous devez apporter des modifications supplémentaires au dernier commit, utilisez cette commande :

```bash
$ git commit --amend
```

Cela ouvre l'éditeur de message de commit vous permettant de modifier le message. Si aucune modification n'a été apportée depuis le dernier commit, cela vous permet simplement de modifier le message de commit.

****Note**** : Ne modifiez (amend) que les commits qui sont encore locaux et qui n'ont pas encore été poussés (pushed) pour éviter des problèmes aux collaborateurs.

### Comment désindexer un fichier indexé avec `git reset`

Pour désindexer un fichier qui a été inclus par accident, vous pouvez utiliser la commande `git reset HEAD <file>`. Par exemple :

```bash
$ git reset HEAD CONTRIBUTING.md 
```

Le fichier est désindexé, ce qui vous permet d'apporter d'autres modifications sans valider celles qui n'étaient pas prévues.

### Comment annuler les modifications d'un fichier avec `git checkout`

Supposons que vous ayez apporté des modifications à des fichiers que vous réalisez plus tard ne pas vouloir conserver. Utilisez `git checkout -- <file>` pour rejeter les modifications apportées à un fichier et le ramener à son état précédent.

```bash
$ git checkout -- CONTRIBUTING.md
```

Ceci remplacera le fichier modifié par la dernière version indexée ou validée.

### Annuler des actions avec `git restore`

Explorons les alternatives introduites par la version 2.23.0 de Git, `git restore`, qui sert d'alternative à `git reset` pour de nombreuses opérations d'annulation.

#### Comment désindexer un fichier indexé avec `git restore`

Si vous indexez accidentellement un fichier que vous n'aviez pas l'intention de valider, vous pouvez utiliser `git restore --staged <file>` pour le désindexer.

```bash
$ git restore --staged CONTRIBUTING.md   
```

Le fichier est désindexé, de la même manière qu'avec `git reset HEAD <file>`, ce qui vous permet d'apporter d'autres modifications sans valider celles qui n'étaient pas prévues.

#### Comment annuler les modifications d'un fichier avec `git restore`

Pour rejeter les modifications apportées à un fichier dans le répertoire de travail, utilisez `git restore <file>` :

```bash
$ git restore CONTRIBUTING.md
```

Semblable à `git checkout -- <file>`, cette commande rejette les modifications apportées au fichier spécifié, le ramenant à l'état où il se trouvait lors du dernier commit.

****Note importante :**** Utilisez les commandes comme `git reset`, `git checkout --` et `git restore` avec prudence car elles peuvent rejeter définitivement des modifications locales. Utilisez ces commandes lorsque vous êtes certain que les modifications ne sont pas nécessaires et que vous n'avez pas de modifications locales non sauvegardées.

**Alternatives :** Le remisage (stashing) et le branchement (branching) sont des méthodes alternatives pour mettre temporairement de côté des modifications sans les rejeter entièrement. Ces méthodes sont plus sûres si vous n'êtes pas sûr de vouloir supprimer vos modifications.

## Comment travailler avec des dépôts distants (remotes) dans Git

Les dépôts distants sont des versions de votre projet hébergées sur Internet ou sur un réseau. Collaborer avec d'autres implique la gestion de ces dépôts distants, y compris leur ajout, leur suppression et leur inspection. Apprenons à les gérer efficacement.

### Comment afficher vos dépôts distants dans Git

Pour commencer, voyons quels serveurs distants sont configurés pour notre projet en utilisant :

```bash
$ git remote
```

Cette commande liste les noms courts (shortnames) de tous les dépôts distants que nous avons spécifiés. Par exemple, si nous avons cloné un dépôt, nous verrons généralement `origin`, le nom par défaut que Git attribue au serveur depuis lequel nous avons cloné.

L'ajout de l'option `-v` fournit des détails supplémentaires, tels que les URL associées à chaque dépôt distant.

```bash
$ git remote -v
```

Ceci affiche les URL de récupération (fetch) et de poussée (push) pour chaque dépôt distant, nous permettant de comprendre où notre projet est hébergé et comment nous interagissons avec lui.

### Comment ajouter des dépôts distants dans Git

Pour ajouter explicitement un nouveau dépôt distant, utilisez `git remote add <shortname> <url>` :

```bash
$ git remote add example https://github.com/example/example.git
```

Ici, nous avons ajouté un dépôt distant nommé `example` avec l'URL spécifiée. Cela nous permet de référencer ce dépôt distant en utilisant le nom court `example` dans nos commandes.

### Comment récupérer (fetch) et tirer (pull) depuis des dépôts distants

Pour récupérer des données d'un dépôt distant, nous utilisons la commande `git fetch` suivie du nom du dépôt distant :

```bash
$ git fetch origin // Ici, nous ne spécifions aucune branche particulière.
```

Cela télécharge toutes les nouvelles modifications du dépôt distant `origin` vers notre dépôt local, nous permettant de rester à jour avec les derniers développements.

Alternativement, si nous voulons récupérer et fusionner les modifications d'une branche distante dans notre branche actuelle en une seule étape, nous utilisons la commande `git pull` :

```bash
$ git pull origin master
```

Ici, nous tirons spécifiquement les modifications de la branche `master` du dépôt distant `origin` vers notre branche actuelle.

### Comment pousser (push) des modifications vers des dépôts distants

Pour partager notre travail avec d'autres, nous poussons nos modifications vers un dépôt distant en utilisant :

```bash
$ git push origin main
```

Dans cet exemple, nous poussons nos modifications locales vers la branche `main` du dépôt distant `origin`.

### Comment inspecter un dépôt distant dans Git

Enfin, nous pouvons inspecter un dépôt distant pour recueillir plus d'informations à son sujet en utilisant :

```bash
$ git remote show origin
```

Cette commande affiche des détails tels que les URL de fetch et de push, les branches suivies et les configurations des branches locales associées au dépôt distant `origin`.

### Comment renommer des dépôts distants dans Git

Supposons maintenant que nous voulions renommer le nom court d'un dépôt distant de `example` à `new-example` :

```bash
$ git remote rename example new-example
```

### Comment supprimer des dépôts distants dans Git

Si, pour une raison quelconque, nous n'avons plus besoin d'un dépôt distant et que nous voulons le supprimer de notre projet :

```bash
$ git remote remove new-example
ou
$ git remote rm new-example
```

Après la suppression, les branches de suivi à distance et les paramètres de configuration associés sont également supprimés.

## L'étiquetage (tagging) dans Git

L'étiquetage dans Git est une fonctionnalité fondamentale permettant aux développeurs de marquer des points spécifiques dans l'historique d'un dépôt comme étant significatifs. Généralement, les étiquettes (tags) sont utilisées pour désigner des points de version, tels que v1.0, v2.0, et ainsi de suite.

### Comment lister les étiquettes existantes dans Git

Imaginez que vous travaillez sur un projet avec plusieurs versions publiées. Pour lister les étiquettes existantes :

```bash
$ git tag
```

De plus, vous pouvez rechercher des étiquettes correspondant à un modèle spécifique en utilisant l'option `-l` ou `--list`. Par exemple :

```bash
$ git tag -l "v2.0*"
```

Cette commande listera les étiquettes comme `v2.0`, `v2.0-beta`, etc., correspondant au modèle spécifié.

### Comment créer des étiquettes dans Git

Git prend en charge deux types d'étiquettes : les étiquettes légères et les étiquettes annotées.

#### Étiquettes légères (Lightweight Tags)

Utilisez les étiquettes légères lorsque vous souhaitez marquer un commit spécifique sans ajouter d'informations supplémentaires. Exemple :

```bash
$ git tag v1.1-lw
```

Pour voir les informations de commit associées à cette étiquette, utilisez :

```bash
$ git show v1.1-lw
```

Les étiquettes légères n'affichent que la somme de contrôle du commit.

#### Étiquettes annotées (Annotated Tags)

Les étiquettes annotées, quant à elles, contiennent des informations supplémentaires telles que les informations sur l'auteur de l'étiquette, la date et un message d'étiquetage.

La création d'une étiquette annotée implique l'utilisation de l'option `-a` avec la commande `git tag`, ainsi qu'un message d'étiquetage. Par exemple :

```bash
$ git tag -a v2.0 -m "Version de sortie 2.0"
```

Pour afficher des informations détaillées sur cette étiquette, y compris le commit vers lequel elle pointe et le message d'étiquetage, utilisez :

```bash
$ git show v2.0
```

### Comment étiqueter un commit plus ancien dans Git

Parfois, vous pourriez oublier d'étiqueter un commit spécifique. Ne vous inquiétez pas, vous pouvez l'étiqueter plus tard en spécifiant la somme de contrôle du commit.

Exemple : supposons que vous ayez oublié d'étiqueter un commit avec l'ID `abcdefg`. Vous pouvez l'étiqueter comme suit :

```bash
$ git tag -a v1.2 abcdefg
```

Cette commande étiquette le commit spécifié comme `v1.2`.

#### Comment pousser une étiquette vers un dépôt distant dans Git

Pour pousser une étiquette spécifique vers un serveur distant, vous pouvez utiliser :

```bash
$ git push origin <tagname>
```

Si vous avez plusieurs étiquettes et que vous souhaitez les pousser toutes en même temps, vous pouvez utiliser l'option `--tags` :

```bash
$ git push origin --tags
```

#### Comment supprimer des étiquettes dans Git

Pour supprimer une étiquette localement (la retirer du dépôt local) :

```bash
$ git tag -d <tagname>
```

Par exemple, pour supprimer une étiquette légère nommée `v1.4-lw` :

```bash
$ git tag -d v1.4-lw
```

D'autre part, vous pouvez supprimer une étiquette d'un serveur distant de deux manières :

1.  Utilisation de la commande `git push` avec une spécification de référence (refspec) :

```bash
$ git push origin :refs/tags/v1.1-lw
```

Cette commande ne pousse rien (`:`) vers l'étiquette distante `v1.1-lw`, ce qui la supprime effectivement.

2.  Utilisation de l'option `--delete` avec `git push` :

```bash
$ git push origin --delete v1.1-lw
```

Celle-ci supprime directement l'étiquette `v1.1-lw` du serveur distant.

#### Comment extraire (checkout) des étiquettes dans Git

Pour visualiser l'état des fichiers à une étiquette spécifique, vous pouvez extraire cette étiquette :

```bash
$ git checkout v2.0
```

Cette commande place votre dépôt dans un état de "HEAD détachée", où vous pouvez voir les fichiers mais ne pouvez pas effectuer de modifications directement.

Si vous devez travailler sur les fichiers à cette étiquette, il est préférable de créer une nouvelle branche :

```bash
$ git checkout -b v2.0-branch v2.0
```

Vous pouvez maintenant effectuer des modifications et des commits sans altérer l'étiquette d'origine.

## Les alias Git

Les alias Git sont des raccourcis ou des commandes personnalisées que vous pouvez créer pour simplifier et rationaliser votre flux de travail Git.

Pour créer un alias Git, vous utilisez la commande `git config` avec le drapeau `--global` pour rendre l'alias disponible dans tous vos dépôts Git.

### Alias de base pour les commandes courantes

Vous pouvez créer des alias pour les commandes Git fréquemment utilisées afin de les rendre plus faciles à mémoriser et à taper. Par exemple :

```bash
$ git config --global alias.co checkout
$ git config --global alias.br branch
$ git config --global alias.ci commit
```

Désormais, au lieu de taper les commandes complètes, vous pouvez utiliser des alias plus courts comme `git co`, `git br` et `git ci` respectivement.

Vous pouvez également **créer des alias personnalisés pour des actions que vous effectuez fréquemment** ou pour améliorer la lisibilité des commandes. Exemple :

```bash
$ git config --global alias.unstage 'reset HEAD --'
```

Désormais, vous pouvez utiliser `git unstage <file>` au lieu de `git reset HEAD -- <file>` pour désindexer un fichier.

#### Comment combiner plusieurs commandes dans Git

Les alias peuvent également être utilisés pour combiner plusieurs commandes Git en un seul alias. Par exemple, créons un alias pour indexer toutes les modifications puis les valider avec une seule commande :

```bash
$ git config --global alias.commitall '!git add -A && git commit'
```

Maintenant, l'exécution de `git commitall` indexera toutes les modifications (`git add -A`) puis les validera, vous faisant gagner du temps et des frappes de touches.

## Les branches dans Git

Les branches dans Git offrent un moyen puissant de gérer le code de votre projet, permettant un développement parallèle et l'expérimentation sans affecter la base de code principale.

Le branchement Git vous permet de diverger de la ligne principale de développement, de travailler sur des fonctionnalités ou des correctifs, puis de fusionner vos modifications. Contrairement à de nombreux autres systèmes de gestion de versions, le modèle de branchement de Git est léger et efficace, rendant les opérations de branchement presque instantanées.

### Qu'est-ce qu'une branche dans Git ?

Une branche est un pointeur léger et mobile vers un commit. Le nom de la branche par défaut est souvent "master", mais elle n'a rien de spécial – elle est comme n'importe quelle autre branche.

La création et le basculement entre les branches vous permettent de travailler simultanément sur différentes fonctionnalités.

### Comment créer une nouvelle branche dans Git :

Lorsque vous voulez commencer à travailler sur une nouvelle fonctionnalité ou expérimenter une idée, vous pouvez créer une nouvelle branche dans Git. Cette nouvelle branche sert de ligne de développement distincte, vous permettant d'apporter des modifications sans affecter la branche principale.

```bash
$ git branch new_feature
```

Cette commande crée une nouvelle branche nommée 'new-feature' pointant vers le même commit que la branche actuelle. Les branches peuvent coexister, et Git conserve un pointeur spécial appelé `HEAD` pour indiquer la branche actuelle.

### Comprendre les branches

Tout d'abord, saisissons les bases des branches dans Git. Lorsque vous initialisez un dépôt Git, vous commencez avec une branche par défaut, généralement nommée 'master' ou 'main'. Les branches sont essentiellement des pointeurs vers des commits, vous permettant de travailler sur différentes fonctionnalités ou correctifs de manière indépendante.

Pour afficher toutes les branches de votre dépôt, utilisez la commande :

```bash
$ git branch
```

Ceci affichera une liste de branches avec un astérisque (\*) indiquant la branche actuellement extraite. Pour des informations supplémentaires comme le dernier commit sur chaque branche, utilisez :

```bash
$ git branch -v
```

### Comment basculer vers une autre branche dans Git :

Pour basculer vers une branche existante différente, utilisez `git checkout`.

```bash
$ git checkout new_feature
```

Cette commande déplace le pointeur 'HEAD' vers la branche 'new-feature', en faisant la branche active.

Pour créer et basculer vers une nouvelle branche en une seule opération :

```bash
$ git checkout -b <newbranchname>
```

À partir de la version 2.23 de Git, vous pouvez utiliser `git switch` au lieu de `git checkout`.

-   Basculer vers une branche existante : `git switch existing-branch`.
-   Créer et basculer vers une nouvelle branche : `git switch -c new-branch`.

### Comment visualiser les branches dans Git :

Après avoir créé et basculé entre les branches, vous pouvez visualiser la structure des branches en utilisant :

```bash
$ git log --oneline --decorate --graph --all
```

Cette commande affiche une représentation concise et graphique de l'historique des commits et des pointeurs de branches, vous permettant de voir comment les branches divergent et fusionnent au fil du temps.

## Comment gérer les branches dans Git

### Comment gérer les branches fusionnées

À mesure que votre projet évolue, vous fusionnerez les branches dans la branche principale une fois leurs modifications finalisées. Pour identifier les branches fusionnées, exécutez :

```bash
$ git branch --merged
```

Cette commande liste les branches qui ont été fusionnées avec succès dans la branche actuelle. Ces branches peuvent généralement être supprimées en toute sécurité avec :

```bash
$ git branch -d branch_name
```

Cependant, pour les branches contenant du travail non fusionné, utilisez :

```bash
$ git branch --no-merged
```

La suppression de telles branches nécessite le drapeau '-D' :

```bash
$ git branch -D branch_name
```

Cela garantit que vous ne perdez pas par inadvertance des modifications non fusionnées.

### Comment renommer des branches

Pour renommer une branche locale :

```bash
$ git branch --move old_branch_name new_branch_name
```

Cette commande met à jour le nom de la branche localement. Pour refléter le changement sur le dépôt distant, poussez la branche renommée :

```bash
$ git push --set-upstream origin new_branch_name
```

Vérifiez les modifications en utilisant :

```bash
$ git branch --all
```

Assurez-vous de supprimer l'ancienne branche sur le dépôt distant :

```bash
$ git push origin --delete old_branch_name
```

Cela garantit l'uniformité entre les dépôts locaux et distants.

### Comment changer le nom de la branche par défaut

Renommer la branche par défaut, souvent 'master', nécessite de la prudence et de la coordination, car cela impacte les intégrations du projet et les collaborateurs.

```bash
$ git branch --move master main
```

Une fois renommée, poussez la branche mise à jour vers le dépôt distant :

```bash
$ git push --set-upstream origin main
```

N'oubliez pas de mettre à jour les références et les configurations dans les dépendances, les tests, les scripts et les hébergeurs de dépôts. Une fois cela fait, supprimez l'ancienne branche master sur le distant :

```bash
$ git push origin --delete master
```

Ceci est **différent de `$ git config --global init.defaultBranch main`** dont nous avons discuté dans la partie configuration de la manière suivante :

-   `$ git branch --move master main` : Cette commande renomme la branche existante nommée "master" en "main" au sein du dépôt actuel. C'est une sorte d'opération locale qui n'affecte que ce dépôt.
-   `$ git config --global init.defaultBranch main` : Cette commande définit globalement le nom de la branche par défaut pour les nouveaux dépôts. Elle ne renomme pas les branches existantes mais garantit que tout nouveau dépôt créé par la suite utilisera "main" comme nom de branche par défaut au lieu de "master".

**Ressource supplémentaire** : Pensez à consulter cette [ressource][28] officielle de Git pour ses visuels et diagrammes informatifs qui peuvent vous apporter plus de clarté sur les branches distantes et les concepts de gestion de branches.

## Flux de travail avec les branches

Comprenons les branches plus en détail et examinons un flux de travail de branchement courant utilisé dans les grands projets.

### Branches à longue durée de vie :

Dans Git, les branches à longue durée de vie sont des branches qui restent ouvertes sur une période prolongée.

### Branches thématiques (Topic Branches) :

Les branches `Topic`/`Feature` sont des branches à courte durée de vie créées pour des fonctionnalités spécifiques ou des morceaux de travail. Contrairement aux branches à longue durée de vie, qui persistent dans le temps, les branches thématiques sont créées, utilisées et souvent supprimées une fois le travail terminé.

**Exemple :** Considérons un scénario où une équipe maintient deux branches à longue durée de vie : `master` et `develop`.

-   La branche `master` ne contient que du code stable, potentiellement ce qui a été publié ou sera publié.
-   La branche `develop` agit comme une zone de transit pour le développement en cours. Bien qu'elle ne soit pas toujours stable, elle sert de terrain d'essai pour les nouvelles fonctionnalités.

Les développeurs fusionnent les modifications des branches de fonctionnalités dans la branche `develop` pour les tests. Une fois que les fonctionnalités sont testées en profondeur et stables, elles sont fusionnées dans `master`.

Notez comment les modifications progressent à travers différents niveaux de stabilité, passant des moins stables (branches de fonctionnalités) aux plus stables (comme la branche develop), au fur et à mesure qu'elles subissent des tests et des affinements, pour être finalement fusionnées dans la branche principale/master la plus stable.

Cela maintient une séparation claire entre le code stable et le code de développement, garantissant que seules les fonctionnalités testées en profondeur parviennent à la version stable.

### Bonnes pratiques pour les branches

1.  **Créer des noms de branches descriptifs** : Utilisez des noms de branches significatifs qui reflètent l'objectif ou la fonctionnalité en cours de développement.
2.  **Supprimer les branches inutilisées** : Une fois qu'une branche a rempli son rôle et que ses modifications ont été fusionnées dans la branche principale, envisagez de la supprimer pour garder le dépôt propre et gérable.

## Le rebasage (rebasing) dans Git

Dans Git, lorsque vous travaillez avec des branches, il existe deux manières principales d'intégrer les modifications d'une branche dans une autre : la fusion (merging) et le rebasage (rebasing).

Contrairement à la fusion, qui peut créer un historique encombré avec de multiples commits de fusion, le rebasage produit un historique linéaire, ce qui facilite la compréhension de la séquence des modifications apportées au fil du temps.

### Exemple de rebasage de base :

Imaginez que vous travaillez sur un projet avec deux branches : "feature" et "master". Vous avez effectué quelques commits sur la branche "feature" et vous souhaitez maintenant intégrer ces modifications dans la branche "master" en utilisant le rebasage.

D'abord, vous basculez sur votre branche "feature" :

```bash
$ git checkout feature
```

Ensuite, vous rebasez votre branche feature sur la branche master :

```bash
$ git rebase master
```

Cette commande prend tous les commits/modifications que vous avez effectués sur votre branche "feature" et les applique par-dessus les derniers commits de la branche "master", en rejouant les commits un par un.

Pas seulement la branche master, vous pouvez également rebaser une branche thématique sur une autre branche thématique. Exemple :

Supposons que vous travailliez sur un projet avec deux branches de fonctionnalités : "frontend" et "backend". Vous avez fait quelques commits sur la branche "frontend" et vous voulez maintenant intégrer ces modifications dans la branche "backend".

Utilisons une approche différente cette fois —  
utilisez l'option `--onto` de `git rebase` pour rebaser la branche "frontend" sur la branche "backend" :

```bash
$ git rebase --onto backend frontend
```

Après le rebasage, revenez sur la branche "backend" et effectuez une fusion en avance rapide (fast-forward merge) :

```bash
$ git checkout backend
$ git merge frontend
```

Désormais, l'historique de votre projet apparaît linéaire, reflétant l'intégration séquentielle des modifications de la branche "frontend" dans la branche "backend".

### Rebasing vs Merging : lequel est le meilleur ?

#### Cas d'utilisation du rebasage (Rebasing) :

-   Convient aux branches de fonctionnalités qui nécessitent une intégration propre dans la branche principale.
-   Préféré pour les contributions open-source où un historique de commits propre est valorisé.

#### Cas d'utilisation de la fusion (Merging) :

-   Approprié pour les environnements collaboratifs où la transparence dans le processus de développement du projet est cruciale.
-   Utile pour les projets où le maintien d'un enregistrement historique précis est une priorité.

## Conclusion

Ce guide sert de manuel complet pour comprendre et utiliser Git, un puissant système de gestion de versions largement utilisé dans le développement logiciel.

Des flux de travail de base à la configuration d'un dépôt, en passant par l'étiquetage et le branchement de dépôts distants, nous avons appris un ensemble complet de fonctionnalités qui aideront à rationaliser le processus de développement.

---

![Samyak Jain](https://www.freecodecamp.org/news/content/images/size/w60/2024/02/profilepic.png)

Apprenant insatiable avec une boîte à outils de développeur web. Le monde de la science me fascine sans fin. Plus d'infos sur samyakinfo.tech

---

Si vous avez lu jusqu'ici, remerciez l'auteur pour lui montrer que vous appréciez son travail. Dites merci

Apprenez à coder gratuitement. Le programme open source de freeCodeCamp a aidé plus de 40 000 personnes à obtenir un emploi de développeur. [Commencer][29]

[1]: #heading-qu-est-ce-que-git
[2]: #heading-ce-qui-differencie-git-des-autres-systemes-de-gestion-de-versions
[3]: #heading-les-trois-etats-et-le-flux-de-travail-de-base-de-git
[4]: #heading-configuration-initiale-de-git
[5]: #heading-comment-obtenir-de-l-aide-dans-git
[6]: #heading-comment-obtenir-un-depot-git
[7]: #heading-1-comment-initialiser-un-depot-dans-un-repertoire-existant-dans-git
[8]: #heading-2-comment-cloner-un-depot-existant-dans-git
[9]: #heading-comment-enregistrer-des-modifications-dans-le-depot
[10]: #heading-comment-visualiser-l-historique-des-commits-dans-git
[11]: #heading-comment-annuler-des-actions-dans-git
[12]: #heading-comment-travailler-avec-des-depots-distants-dans-git
[13]: #heading-l-etiquetage-tagging-dans-git
[14]: #heading-les-alias-git
[15]: #heading-les-branches-dans-git
[16]: #heading-comment-creer-une-nouvelle-branche-dans-git
[17]: #heading-comprendre-les-branches
[18]: #heading-comment-basculer-vers-une-autre-branche-dans-git
[19]: #heading-comment-visualiser-les-branches-dans-git
[20]: #heading-comment-gerer-les-branches-dans-git
[21]: #heading-comment-gerer-les-branches-fusionnees
[22]: #heading-comment-renommer-des-branches
[23]: #heading-comment-changer-le-nom-de-la-branche-par-defaut
[24]: #heading-flux-de-travail-avec-les-branches
[25]: #heading-le-rebasage-rebasing-dans-git
[26]: #heading-conclusion
[27]: https://git-scm.com/download/win
[28]: https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches
[29]: https://www.freecodecamp.org/learn/