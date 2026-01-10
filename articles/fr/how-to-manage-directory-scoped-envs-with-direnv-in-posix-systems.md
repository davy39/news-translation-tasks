---
title: Comment gérer les variables à portée de répertoire avec direnv dans les systèmes
  POSIX
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-22T21:39:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-directory-scoped-envs-with-direnv-in-posix-systems
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/pexels-aleksejs-bergmanis-681335.jpg
tags:
- name: Productivity
  slug: productivity
- name: unix
  slug: unix
- name: variables
  slug: variables
seo_title: Comment gérer les variables à portée de répertoire avec direnv dans les
  systèmes POSIX
seo_desc: 'By Otavio Ehrenberger

  A common practice in software projects is to keep certain information separated
  but accessible from the codebase which uses it. Developers usually do this with
  secrets such as passwords or private keys, or with user or context-s...'
---

Par Otavio Ehrenberger

Une pratique courante dans les projets logiciels consiste à garder certaines informations séparées mais accessibles depuis la base de code qui les utilise. Les développeurs le font généralement avec des secrets tels que des mots de passe ou des clés privées, ou avec des informations spécifiques à l'utilisateur ou au contexte. 

Mais gérer les variables d'environnement peut être fastidieux. Il existe un certain nombre de solutions pour faciliter cette tâche, et il existe même des solutions intégrées telles que [bash_profile](https://www.baeldung.com/linux/bashrc-vs-bash-profile-vs-profile).

Une solution que j'ai découverte récemment et que j'ai trouvée particulièrement pratique est [direnv](https://github.com/direnv/direnv). Il s'agit d'une extension de shell qui vous permet de définir des variables d'environnement dont la portée est limitée à un répertoire. 

Après avoir installé et intégré l'extension à votre shell, `direnv` s'exécutera chaque fois que vous changerez de répertoire, à la recherche d'un fichier `.envrc` dans le même répertoire ou dans un niveau supérieur de l'arborescence des répertoires. Il chargera ensuite les variables définies dans l'environnement actuel et les déchargera s'il cesse de détecter le même `.envrc`.

Notez que `direnv` chargera le premier fichier `.envrc` détecté, ce qui signifie que _l'environnement_ **ne** _hérite pas des valeurs d'un_ `.envrc` _dans un répertoire parent_.

Il est également important de garder à l'esprit que les variables d'environnement _ne seront chargées dans votre session shell que lorsque vous vous déplacerez dans un répertoire affecté par un fichier_ `.envrc`. Donc, si vous essayez quelque chose comme exécuter un script qui charge un environnement défini dans un répertoire en dessous de votre niveau actuel, les variables ne seront pas accessibles.

## Comment installer `direnv`

Voici une [liste des systèmes pris en charge](https://direnv.net/docs/installation.html). Il est très probable que le gestionnaire de paquets open source principal de votre système basé sur UNIX l'ait disponible. 

Supposons que nous sommes sur Debian, nous pouvons installer `direnv` en exécutant la commande standard d'installation de paquets externes dans le terminal :

```bash
sudo apt-get install direnv
```

## Comment configurer `direnv`

Après l'avoir installé, vous devez intégrer `direnv` à votre shell. Si vous utilisez bash, vous pouvez le faire en ajoutant cette ligne à la fin de votre fichier de configuration de démarrage du shell :

```bash
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
```

C'est presque la même chose pour ZShell :

```bash
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
```

Direnv prend également en charge FISH, TCSH et Elvish. [Voici les instructions d'intégration pour chaque shell pris en charge](https://direnv.net/docs/hook.html).

## Comment utiliser `direnv`

Maintenant, nous devons créer un fichier `.envrc` pour le répertoire auquel nous souhaitons limiter la portée des variables d'environnement.

Supposons que nous le créons pour le répertoire `~/project`.

```bash
echo export FOO='J\'adore Linux !' >> ~/project/.envrc
```

Vous recevrez alors un avertissement indiquant que le `.envrc` actuel n'a pas été lu. `direnv` bloquera le chargement de `.envrc` chaque fois qu'il détectera des modifications qui n'ont pas été explicitement autorisées. Donc, exécutez maintenant :

```bash
direnv allow ~/project
```

et voilà !, vous avez maintenant un environnement à portée de répertoire.

Vous souvenez-vous quand je vous ai dit que '`direnv` bloquera le chargement de `.envrc` chaque fois qu'il détectera des modifications qui n'ont pas été explicitement autorisées' ? Cela ne se limite pas aux modifications nouvellement introduites – le fichier entier sera non autorisé. Donc, lorsque vous faites ceci :

```bash
echo export BAR='Il est en fait appelé GNU/Linux !' >> ~/project/.envrc
```

vous devrez exécuter `direnv allow ~/project` à nouveau, même pour accéder à `$FOO`. Un peu ennuyeux, mais orienté vers la sécurité.

Chaque fois qu'un `.envrc` est chargé, direnv affichera un message avec le chemin du fichier et également les noms des variables chargées, afin que vous n'ayez pas à vous soucier d'oublier votre configuration. Il vous indiquera également chaque fois qu'un environnement a été déchargé.

### Merci d'avoir lu !

C'est tout ! C'est assez simple, et j'espère que vous le trouverez aussi pratique que je l'ai trouvé.