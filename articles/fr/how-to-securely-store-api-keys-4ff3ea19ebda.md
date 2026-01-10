---
title: Meilleures pratiques pour stocker en toute sécurité les clés API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-25T15:27:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-securely-store-api-keys-4ff3ea19ebda
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xw9gprMTI6h3U3NkKV0vUg.jpeg
tags:
- name: api
  slug: api
- name: Docker
  slug: docker
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: Security
  slug: security
seo_title: Meilleures pratiques pour stocker en toute sécurité les clés API
seo_desc: 'By Bruno Pedro

  In the past, I’ve seen many people use Git repositories to store sensitive information
  related to their projects.

  Lately, I’ve been seeing some people announce that they’re storing API keys on their
  private GitHub repositories. I’m wri...'
---

Par Bruno Pedro

Par le passé, j'ai vu beaucoup de gens utiliser des dépôts Git pour stocker des informations sensibles liées à leurs projets.

Récemment, j'ai vu certaines personnes annoncer qu'elles stockent des clés API dans leurs dépôts GitHub privés. J'écris cet article parce que les gens doivent comprendre les risques de stocker des clés API avec leur code.

Cet article n'est pas destiné à être une solution permanente aux problèmes que vous pourriez avoir avec le stockage des clés API. Au lieu de cela, il s'agit de ma propre analyse du problème et de mes suggestions sur la façon de le résoudre.

Alors, quel est exactement le problème de stocker des informations sensibles près de votre code dans un dépôt Git ?

### Pourquoi vous ne devriez pas stocker les clés API dans les dépôts Git

Stocker des clés API, ou toute autre information sensible, dans un dépôt `git` est quelque chose à éviter à tout prix. Même si le dépôt est privé, vous ne devriez pas le considérer comme un endroit sûr pour stocker des informations sensibles.

Commençons par examiner pourquoi il est mauvais de stocker des clés API dans des dépôts `git` **publics**.

Par nature, un dépôt `git` public peut être accessible par n'importe qui.

En d'autres termes, toute personne ayant une connexion Internet peut accéder au contenu d'un dépôt `git` public. Non seulement cela, mais ils peuvent également parcourir tout le code à l'intérieur du dépôt et éventuellement même l'exécuter. Si vous stockez une clé API dans un dépôt public, vous la publiez en clair pour que tout le monde puisse la voir.

Une recherche récente pour **client_secret** sur GitHub a révélé qu'il y a plus de 30 000 commits qui exposent potentiellement une clé API et un secret. Dans certains cas, vous n'avez qu'à copier et coller le code pour accéder immédiatement à l'API.

Ce problème devient si important que certaines entreprises investissent des ressources pour s'assurer qu'il n'y a pas de clés API et de secrets divulgués.

L'année dernière, Slack a commencé à rechercher des jetons API exposés et à les invalider de manière proactive. Cette action empêche l'accès malveillant aux comptes Slack mais ne peut pas trouver tous les jetons divulgués.

Donc, cela se passe sur les dépôts Git publics. Qu'en est-il des dépôts **privés** ? Pourquoi est-ce un problème ?

Les dépôts Git privés hébergés sur des services tels que GitHub, GitLab et Bitbucket sont exposés à un type de risque différent. Lorsque vous intégrez une application tierce avec l'un des services mentionnés, vous pouvez ouvrir vos dépôts privés à ces tiers. Ces applications pourront accéder à vos dépôts privés et lire les informations qu'ils contiennent.

Bien que cela seul ne crée pas de risque, imaginez si l'une de ces applications devient vulnérable aux attaquants. En obtenant un accès non autorisé à l'une de ces applications tierces, les attaquants pourraient accéder à vos données sensibles, y compris les clés API et les secrets.

### Alors, où les clés API doivent-elles être stockées ?

Il existe de nombreuses alternatives pour stocker en toute sécurité les clés API et les secrets. Certaines d'entre elles vous permettent d'utiliser votre dépôt Git et de chiffrer les données sensibles. D'autres outils sont plus sophistiqués et déchiffrent les informations sensibles dans le cadre d'un workflow de déploiement. Examinons quelques-unes des solutions disponibles.

#### `git-remote-gcrypt`

La première solution vous permet de chiffrer un dépôt Git entier. [git-remote-gcrypt](https://github.com/spwhitton/git-remote-gcrypt) le fait en ajoutant des fonctionnalités aux assistants distants Git afin qu'une nouvelle couche de transport chiffrée devienne disponible. Les utilisateurs n'ont qu'à configurer un nouveau distant chiffré et y pousser le code.

Continuez à lire si vous cherchez une solution plus fine qui vous permet de chiffrer des fichiers individuels.

#### `git-secret`

`[git-secret](http://git-secret.io/)` est un outil qui fonctionne sur votre machine locale et chiffre des fichiers spécifiques avant de les pousser vers votre dépôt. En arrière-plan, `git-secret` est un script shell qui utilise GNU Privacy Guard ([GPG](https://www.gnupg.org/)) pour chiffrer et déchiffrer les fichiers qui pourraient contenir des informations sensibles.

#### `git-crypt`

Une autre solution est `[git-crypt](https://www.agwa.name/projects/git-crypt/)`. Il est très similaire à git-secret dans son fonctionnement, mais il présente quelques différences intéressantes.

La première chose à noter à propos de `git-crypt` est qu'il s'agit d'un exécutable binaire et non d'un script shell, comme git-secret. Étant un exécutable binaire signifie que pour l'utiliser, vous devez d'abord le compiler, ou vous devez trouver une distribution binaire pour votre machine.

Si vous utilisez un Mac, vous avez de la chance car [HomeBrew](https://brew.sh/) propose un package `git-crypt` prêt à installer. Tout ce que vous avez à faire est d'exécuter `brew install git-crypt` dans un terminal.

#### BlackBox

[BlackBox](https://github.com/StackExchange/blackbox) est un outil créé par [Stack Overflow](https://stackoverflow.com/). Il s'agit de l'entreprise derrière les communautés populaires de questions et réponses telles que Stack Overflow lui-même, Server Fault et Super User. BlackBox est un outil robuste car il fonctionne avec Git ainsi qu'avec d'autres systèmes de contrôle de version comme Mercurial et Subversion.

Il prend également en charge le chiffrement de petites chaînes de caractères et pas seulement de fichiers entiers. Il le fait lorsqu'il travaille avec [Puppet](https://puppet.com/) et utilise [Hiera](https://docs.puppet.com/hiera/) de Puppet, un outil de recherche de paires clé-valeur pour les données de configuration.

Avoir la capacité de chiffrer et de déchiffrer des chaînes individuelles fait de BlackBox une excellente solution pour sécuriser les clés API et les secrets.

#### Configuration Heroku et Config Vars

Si vous travaillez avec [Heroku](https://www.heroku.com/), vous ne devriez pas stocker d'informations sensibles telles que des clés API et des secrets dans vos dépôts Git. Heroku offre une solution qui vous permet de [définir des variables de configuration](https://devcenter.heroku.com/articles/config-vars).

Votre application peut ensuite accéder au contenu de ces variables de configuration pendant l'exécution en accédant aux variables d'environnement correspondantes. Même si les valeurs ne sont pas chiffrées, cette solution vous permet d'éviter d'utiliser votre dépôt Git pour stocker les clés API.

[Dokku](http://dokku.viewdocs.io/dokku/), une solution Open Source comme Heroku, offre les mêmes capacités.

#### Secrets Docker

À la fin du spectre des solutions possibles se trouvent les [secrets Docker](https://docs.docker.com/engine/swarm/secrets/). Cette solution [a été introduite par Docker](https://blog.docker.com/2017/02/docker-secrets-management/) en février 2017. Elle a gagné en popularité depuis.

Docker secrets vous permet de définir des variables chiffrées et les rend disponibles pour des services spécifiques pendant l'exécution. Les secrets sont chiffrés à la fois pendant le transit et au repos.

Cette approche fait des secrets Docker la solution parfaite pour stocker et utiliser des clés API et des secrets de manière sécurisée et chiffrée.

### Résumé

À ce stade, vous devriez être conscient des dangers de stocker des informations sensibles telles que des clés API et des secrets dans des dépôts Git publics et privés.

Comprendre les moyens potentiels par lesquels vos dépôts pourraient être exposés est essentiel pour évaluer et atténuer les risques associés aux fuites d'informations.

Cet article propose également quelques solutions différentes qui vous permettent de chiffrer les clés API et les secrets afin que vous puissiez utiliser vos dépôts de code en toute sécurité.

Je suis sûr qu'il existe d'autres solutions qui peuvent vous aider à obtenir les mêmes résultats.