---
title: Les meilleurs tutoriels Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-21T17:35:00.000Z'
originalURL: https://freecodecamp.org/news/best-git-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f26740569d1a4ca4107.jpg
tags:
- name: Git
  slug: git
seo_title: Les meilleurs tutoriels Git
seo_desc: 'Git is an open source distributed version control system created in 2005
  by Linus Torvalds and others from the Linux development community. Git can work
  with many types of projects, but it’s most commonly used for software source code.

  Version contro...'
---

Git est un système de contrôle de version distribué open source créé en 2005 par Linus Torvalds et d'autres membres de la communauté de développement Linux. Git peut fonctionner avec de nombreux types de projets, mais il est le plus couramment utilisé pour le code source des logiciels.

Le contrôle de version est un système qui suit les modifications apportées à un fichier ou à un groupe de fichiers au fil du temps. Lorsque vous avez un historique de ces modifications, il vous permet de trouver des versions spécifiques plus tard, de comparer les modifications entre les versions, de récupérer des fichiers que vous avez peut-être supprimés, ou de restaurer des fichiers à des versions précédentes.

Un système de contrôle de version _distribué_ signifie que différents utilisateurs maintiennent leurs propres dépôts d'un projet, au lieu de travailler à partir d'un dépôt central unique. Les utilisateurs ont automatiquement des capacités complètes de suivi des fichiers et l'historique complet des versions du projet sans avoir besoin d'accéder à un serveur central ou à un réseau.

Lorsque Git est initialisé dans un répertoire de projet, il commence à suivre les modifications des fichiers et les stocke sous forme de "jeux de modifications" ou de "correctifs". Les utilisateurs travaillant ensemble sur un projet soumettent leurs jeux de modifications qui sont ensuite inclus (ou rejetés) dans le projet.

freeCodeCamp a une [playlist YouTube avec de nombreux conseils pratiques sur Git et GitHub ici](https://www.youtube.com/watch?v=vR-y_2zWrIE&list=PLWKjhJtqVAbkFiqHnNaxpOPhh9tSWMXIF).

![Image](https://img.youtube.com/vi/vR-y_2zWrIE/maxresdefault.jpg)

### Autres tutoriels :

* Le livre [Pro Git](https://github.com/progit/progit2), écrit par Scott Chacon et Ben Straub et publié par Apress. Le livre est affiché en intégralité dans la [documentation Git](https://git-scm.com/book/en/v2).
* Pour les téléchargements, la documentation et un tutoriel basé sur le navigateur : [site officiel de Git](https://git-scm.com/)
* Commandes les plus utiles lorsque vous êtes dans une mauvaise situation avec GIT : [Oh s***, git !](http://ohshitgit.com/)

### **Comprendre les trois sections d'un projet Git**

Un projet Git aura les trois sections principales suivantes :

1. Répertoire Git
2. Répertoire de travail (ou arbre de travail)
3. Zone de préparation

Le **répertoire Git** (situé dans `YOUR-PROJECT-PATH/.git/`) est l'endroit où Git stocke tout ce dont il a besoin pour suivre précisément le projet. Cela inclut les métadonnées et une base de données d'objets qui inclut des versions compressées des fichiers du projet.

Le **répertoire de travail** est l'endroit où un utilisateur apporte des modifications locales à un projet. Le répertoire de travail extrait les fichiers du projet de la base de données d'objets du répertoire Git et les place sur la machine locale de l'utilisateur.

La **zone de préparation** est un fichier (également appelé "index", "stage" ou "cache") qui stocke des informations sur ce qui sera inclus dans votre prochain commit. Un commit est lorsque vous dites à Git d'enregistrer ces modifications préparées. Git prend un instantané des fichiers tels qu'ils sont et stocke définitivement cet instantané dans le répertoire Git.

Avec trois sections, il y a trois états principaux qu'un fichier peut avoir à tout moment : validé, modifié ou préparé. Vous _modifiez_ un fichier chaque fois que vous apportez des modifications dans votre répertoire de travail. Ensuite, il est _préparé_ lorsque vous le déplacez vers la zone de préparation. Enfin, il est _validé_ après un commit.

### **Installer Git**

* Ubuntu : `sudo apt-get install git`
* Windows : [Télécharger](https://git-scm.com/download/win)
* Mac : [Télécharger](https://git-scm.com/download/mac)

### **Configurer l'environnement Git**

Git dispose d'un outil `git config` qui vous permet de personnaliser votre environnement Git. Vous pouvez modifier l'apparence et le fonctionnement de Git en définissant certaines variables de configuration. Exécutez ces commandes à partir d'une interface de ligne de commande sur votre machine (Terminal sur Mac, Invite de commandes ou Powershell sur Windows).

Il existe trois niveaux où ces variables de configuration sont stockées :

1. Système : situé dans `/etc/gitconfig`, applique les paramètres par défaut à tous les utilisateurs de l'ordinateur. Pour apporter des modifications à ce fichier, utilisez l'option `--system` avec la commande `git config`.
2. Utilisateur : situé dans `~/.gitconfig` ou `~/.config/git/config`, applique les paramètres à un seul utilisateur. Pour apporter des modifications à ce fichier, utilisez l'option `--global` avec la commande `git config`.
3. Projet : situé dans `YOUR-PROJECT-PATH/.git/config`, applique les paramètres uniquement au projet. Pour apporter des modifications à ce fichier, utilisez la commande `git config`.

Si des paramètres entrent en conflit les uns avec les autres, les configurations au niveau du projet remplaceront celles au niveau de l'utilisateur, et les configurations au niveau de l'utilisateur remplaceront celles au niveau du système.

Note pour les utilisateurs de Windows : Git recherche le fichier de configuration au niveau de l'utilisateur (`.gitconfig`) dans votre répertoire `$HOME` (`C:\Users\$USER`). Git recherche également `/etc/gitconfig`, bien qu'il soit relatif à la racine MSys, qui est l'endroit où vous décidez d'installer Git sur votre système Windows lorsque vous exécutez l'installateur. Si vous utilisez la version 2.x ou ultérieure de Git pour Windows, il existe également un fichier de configuration au niveau du système dans `C:\Documents and Settings\All Users\Application Data\Git\config` sur Windows XP, et dans `C:\ProgramData\Git\config` sur Windows Vista et versions ultérieures. Ce fichier de configuration ne peut être modifié que par `git config -f FILE` en tant qu'administrateur.

#### **Ajoutez votre nom et votre email**

Git inclut le nom d'utilisateur et l'email dans les informations d'un commit. Vous voudrez configurer cela dans votre fichier de configuration au niveau de l'utilisateur avec ces commandes :

```shell
git config --global user.name "Mon Nom"
git config --global user.email "monemail@example.com"
```

#### **Changez votre éditeur de texte**

Git utilise automatiquement votre éditeur de texte par défaut, mais vous pouvez le changer. Voici un exemple pour utiliser l'éditeur Atom à la place (l'option `--wait` indique au shell d'attendre l'éditeur de texte pour que vous puissiez y faire votre travail avant que le programme ne continue) :

```shell
git config --global core.editor "atom --wait"
```

#### **Ajoutez de la couleur à la sortie Git**

Vous pouvez configurer votre shell pour ajouter de la couleur à la sortie Git avec cette commande :

```shell
git config --global color.ui true
```

Pour voir tous vos paramètres de configuration, utilisez la commande `git config --list`.

### **Initialiser Git dans un projet**

Une fois Git installé et configuré sur votre ordinateur, vous devez l'initialiser dans votre projet pour commencer à utiliser ses capacités de contrôle de version. Dans la ligne de commande, utilisez la commande `cd` pour naviguer vers le dossier de premier niveau (ou racine) de votre projet. Ensuite, exécutez la commande `git init`. Cela installe un dossier de répertoire Git avec tous les fichiers et objets dont Git a besoin pour suivre votre projet.

Il est important que le répertoire Git soit installé dans le dossier racine du projet. Git peut suivre les fichiers dans les sous-dossiers, mais il ne suivra pas les fichiers situés dans un dossier parent par rapport au répertoire Git.

### **Obtenir de l'aide dans Git**

Si vous oubliez comment fonctionne une commande dans Git, vous pouvez accéder à l'aide de Git depuis la ligne de commande de plusieurs manières :

```shell
git help COMMAND
git COMMAND --help
man git-COMMAND
```

Cela affiche la page de manuel de la commande dans votre fenêtre de shell. Pour naviguer, faites défiler avec les touches fléchées haut et bas ou utilisez les raccourcis clavier suivants :

* `f` ou `barre d'espace` pour avancer d'une page
* `b` pour reculer d'une page
* `q` pour quitter

## **Différence entre Git et GitHub**

Git et GitHub sont deux choses différentes. [Git](https://git-scm.com/) est le [système de contrôle de version](https://en.wikipedia.org/wiki/Version_control), tandis que [GitHub](https://github.com/) est un service d'hébergement de dépôts Git qui aide les gens à collaborer sur l'écriture de logiciels. Cependant, ils sont souvent confondus en raison de leur nom similaire, du fait que GitHub s'appuie sur Git, et parce que de nombreux sites web et articles ne font pas assez clairement la différence entre eux.

![Git n'est pas GitHub](https://i.imgur.com/EkjwJdr.png)

### **Git**

Git est le système de contrôle de version distribué. Git est responsable du suivi des modifications apportées au contenu - généralement des fichiers de code source.

Pour plus d'informations, il y a un [article complet sur Git lui-même](https://guide.freecodecamp.org/git).

### **GitHub**

GitHub est un service qui fournit l'hébergement de dépôts Git. Cela signifie qu'ils fournissent une solution clé en main pour héberger des dépôts Git sur leurs serveurs. Cela peut être utile pour garder une sauvegarde de votre dépôt (Git ne suit que les modifications apportées à vos fichiers au fil du temps ; le dépôt doit toujours être sauvegardé), et pour avoir un endroit centralisé pour garder et partager votre code avec d'autres.

Plus qu'un simple service d'hébergement de dépôts Git, GitHub est une [forge logicielle](https://en.wikipedia.org/wiki/Forge_(software)). Cela signifie qu'il fournit également un [suiveur de problèmes](https://en.wikipedia.org/wiki/Issue_tracking_system), des outils pour la [révision de code](https://en.wikipedia.org/wiki/Code_review), et d'autres outils pour collaborer avec d'autres personnes et créer des logiciels.

GitHub n'est pas le seul à fournir ce type de service. L'un de ses principaux concurrents est [GitLab](https://gitlab.com/). Pour plus d'informations à ce sujet, consultez la [section sur l'hébergement Git](https://www.freecodecamp.org/news/the-beginners-guide-to-git-github/#git-repositories).

# **Comment s'authentifier avec GitHub en utilisant SSH**

Vérifiez qu'il n'y a pas de fichiers `rsa` ici avant de continuer, utilisez :

```shell
ls -al ~/.ssh
```

S'il n'y a rien à lister (c'est-à-dire `: No such file or directory`) alors utilisez :

```shell
mkdir $HOME/.ssh
```

S'il n'y a rien là, générez une nouvelle clé avec :

```shell
ssh-keygen -t rsa -b 4096 -C your@email.com
```

Maintenant, en utilisant `ls -al ~/.ssh`, notre fichier `id_rsa.pub` sera affiché.

Ajoutez la clé SSH à l'agent SSH :

```shell
eval "$(ssh-agent -s)" # pour mac et Linux depuis bash
```

```shell
eval `ssh-agent -s`
ssh-agent -s # pour Windows
```

Ajoutez la clé RSA à SHH avec :

```shell
ssh-add ~/.ssh/id_rsa
```

Copiez votre clé dans le presse-papiers

```shell
clip < ~/.ssh/id_rsa.pub # Windows
```

```shell
cat ~/.ssh/id_rsa.pub # Linux
```

Allez sur votre page [paramètres](https://github.com/settings/keys) GitHub et cliquez sur le bouton 'New SSH key', collez votre clé générée.

Ensuite, authentifiez-vous avec :

```shell
ssh -T git@github.com
```