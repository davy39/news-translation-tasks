---
title: Comment inciter vos utilisateurs à mettre à jour votre application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-29T17:24:49.000Z'
originalURL: https://freecodecamp.org/news/the-architecture-of-an-intelligent-application-update-system-3fc2f27a4a2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*94NdJI6DWSeplX9gibc2hA.png
tags:
- name: software
  slug: software
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment inciter vos utilisateurs à mettre à jour votre application
seo_desc: 'By Jake Soenneker

  The software development cycle is accelerating, and the web supports it beautifully.
  There’s no need to send new binaries to your users. They just visit your site and
  presto — they instantly have the latest and greatest version of y...'
---

Par Jake Soenneker

Le cycle de développement logiciel s'accélère, et le web le supporte magnifiquement. Il n'est pas nécessaire d'envoyer de nouveaux binaires à vos utilisateurs. Ils visitent simplement votre site et presto — ils ont instantanément la dernière et meilleure version de votre code.

Mais il existe des situations où votre application ne peut pas être servie via le web. Et parfois vos utilisateurs ont besoin que votre application fonctionne même lorsqu'ils n'ont pas accès à Internet. Et soyons réalistes — en 2017, il y a encore beaucoup d'applications trop gourmandes en ressources pour fonctionner dans un navigateur. Les applications de bureau ne vont donc pas disparaître.

Cela dit, les utilisateurs d'applications de bureau veulent toujours être "à la pointe" avec votre dernière version. Ils veulent utiliser cette nouvelle fonctionnalité géniale dont ils ont lu sur votre blog de développement.

"Pas de problème," dit le développeur. "Je vais compiler le code, insérer les binaires dans l'installeur, et publier une nouvelle version sur mon site. Ensuite, les utilisateurs pourront télécharger ma dernière version. Je vais simplement tweeter un lien, ou l'inclure dans le prochain email d'information pour les en informer."

C'est la manière traditionnelle de procéder pour mettre à jour un client. Et c'est acceptable pour 98% des applications de bureau natives. C'est la routine pour vos utilisateurs. C'est résistant aux erreurs, et ne nécessite pas beaucoup de travail de la part des développeurs. Les développeurs peuvent même ajouter un élément "vérifier les mises à jour" dans leurs menus contextuels. Votre application peut interroger votre site web pour obtenir le numéro de la dernière version, puis rediriger vos utilisateurs vers le fichier.

Eh bien, il est devenu clair que cette manière traditionnelle n'est pas suffisante. Voici pourquoi:

* Les annonces sont cruciales pour amener les utilisateurs à utiliser votre prochaine version.
* Si votre application accède à des services réseau, les développeurs doivent les rendre rétrocompatibles.
* Les utilisateurs doivent mettre à jour le logiciel manuellement. Cela signifie du temps, de l'énergie et de la concentration perdus.
* Le support client ne veut pas traiter les problèmes liés aux versions obsolètes.
* Les utilisateurs récupèrent souvent leur logiciel ailleurs que depuis la source. Il faut du temps pour qu'une nouvelle version se propage, et elle ne sera jamais à jour partout.
* Pour certaines applications et jeux, il est crucial que chaque utilisateur exécute exactement la même version.

La mise à jour automatique est difficile. Les entreprises en subissent les conséquences chaque fois que quelque chose ne va pas.

Par exemple, en tant qu'utilisateur, je ne sais pas ce que Slack fait lorsqu'il se met à jour. Tout ce que je sais, c'est qu'à la fin, il me dit souvent qu'il n'est _toujours_ pas à jour. Chrome échoue tout le temps et ne me dit même pas pourquoi. Windows Update s'améliore.

Eh bien, en tant que développeur, j'ai de la sympathie pour les produits et les équipes qui les maintiennent, car il y a de nombreuses raisons pour lesquelles les mises à jour sont si difficiles.

![Image](https://cdn-media-1.freecodecamp.org/images/y9aenzfNJZC1VdUvukjFCuPHIVDijGkdg0vm)
_Crédit image : [XKCD](https://xkcd.com/1328/" rel="noopener" target="_blank" title=")_

* Les utilisateurs exécutent une multitude de systèmes d'exploitation et de combinaisons d'environnements de nos jours.
* Les frameworks sous-jacents peuvent également avoir besoin d'être mis à jour d'une version à l'autre.
* Les utilisateurs continuent de modifier les paramètres de sécurité et les permissions.
* Les utilisateurs peuvent négliger d'installer les mises à jour de leur système d'exploitation ou de votre application elle-même.
* Et si le système de mise à jour lui-même a besoin d'une mise à jour ?
* Avec les déploiements de plus en plus automatisés, et les équipes livrant du code plus rapidement, les bugs et les problèmes de sécurité évoluent également plus vite.

#### **Plus d'applications ont besoin de meilleurs systèmes de mise à jour.**

Ces systèmes de mise à jour ajoutent une énorme valeur en offrant aux utilisateurs la meilleure expérience que votre organisation a à offrir.

Il existe de nombreux frameworks de mise à jour disponibles. Un framework populaire est [Squirrel](https://github.com/Squirrel/Squirrel.Windows).

Si vous êtes aux prises avec des problèmes de mise à jour, je vous exhorterais à faire vos recherches avant de recommander quoi que ce soit à votre équipe. Il est intéressant de noter qu'un grand pourcentage des systèmes existants en production aujourd'hui sont sur mesure. Cela est dû au fait que ces systèmes donnent aux développeurs le plus de contrôle sur leur code.

#### Il existe plusieurs fonctionnalités pour un système de mise à jour intelligent et flexible :

* La capacité de télécharger des "deltas" — les différences entre l'installation actuelle et la nouvelle. Il n'est pas nécessaire de télécharger un fichier si l'utilisateur l'a déjà.
* Le système peut se mettre à jour et se réparer lui-même, et il peut se rétablir en cas de problèmes.
* Le système peut détecter les frameworks existants sur le système d'exploitation. Il peut télécharger et installer de nouveaux frameworks sans que l'utilisateur ait à les récupérer lui-même.

Certaines architectures dépendent de services. Je pense à vous, Google et Adobe. Eh bien, les développeurs ne devraient pas dépendre de ces processus en arrière-plan toujours en cours et gourmands en ressources s'ils peuvent les éviter.

L'architecture que je vais décrire n'est qu'un type, mais la plupart d'entre elles sont une variation et suivent les mêmes principes généraux. Par la suite, je vais être plus spécifique à Windows, mais ces fondamentaux s'appliquent également à d'autres systèmes d'exploitation. Je vais couvrir les concepts de base derrière les composants du système de mise à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/Hz8eZG5phsWHQvOeisTMYnJqXbhcZElj40K1)
_Les composants du système de mise à jour_

### L'Installeur

C'est le point d'entrée initial pour l'utilisateur, et c'est là que tout le processus commence. Ce n'est pas un installeur ClickOnce ou Wix typique. C'est un seul exécutable. Il fait plusieurs choses importantes, et il peut être surprenant qu'il ne contienne pas l'application principale. Que fait-il alors ?

1. Tout d'abord, il vérifie la compatibilité du système d'exploitation. Ce ordinateur pourra-t-il exécuter l'application ?
2. Il a une exigence de framework très basse. Par exemple, sur Windows, ce serait .NET 2.0 ou 3.0. Cela signifie que les utilisateurs peuvent ouvrir l'installeur facilement s'ils sont en retard sur les mises à jour.
3. L'exécutable de l'Installeur a le Metteur à jour intégré à l'intérieur. Ne pas inclure l'application cible rend l'exécutable petit en taille de fichier. C'est idéal pour la distribution. Moins il y a de temps entre le moment où l'utilisateur clique sur le bouton de téléchargement et le moment où il ouvre l'installeur, mieux c'est.
4. L'Installeur télécharge et installe tous les frameworks nécessaires pour le Metteur à jour. Cela signifie aller sur le site de Microsoft, récupérer l'installeur .NET, et utiliser des paramètres silencieux pour l'installer.
5. Il crée les répertoires initiaux où l'ensemble de l'environnement de l'application résidera. Où exactement ? Sur Windows, c'est :

```
C:\Users\<Username>\AppData\Local\ 
```

Pourquoi ? Vous n'avez pas besoin de privilèges d'administrateur pour installer là. Cela améliore à son tour l'expérience utilisateur, et permet aux utilisateurs qui n'ont pas de privilèges d'utiliser tout de même votre logiciel. **Sauf s'il y a une excellente raison de le faire, ne demandez pas l'UAC et ne nécessitez pas l'élévation de privilèges.**

6. Le Metteur à jour est extrait dans AppData et si des raccourcis doivent être créés, ils pointeront vers le Metteur à jour.

7. Une fois cela fait, il démarre le Metteur à jour.

### Le Metteur à jour

Le Metteur à jour est la partie la plus importante de l'ensemble du système, d'où le nom. Il sert de hub pour le reste du système de mise à jour.

1. Tout d'abord, le Metteur à jour fait l'inventaire des fichiers résidant dans le dossier où il se trouve. Il hache (MD5, SHA, etc.) chacun des fichiers, et stocke les valeurs dans un dictionnaire.
2. Le Metteur à jour enverra la version actuelle du framework dont il dépend au Serveur de Mise à jour. Cela permet au Serveur de Mise à jour d'instruire le Metteur à jour de récupérer une nouvelle version du framework si nécessaire.
3. Le Metteur à jour enverra le dictionnaire des fichiers/hachages, et le Serveur de Mise à jour déterminera si l'utilisateur a besoin d'une mise à jour. Si ce n'est pas le cas, le client peut passer à l'Application.
4. Si une mise à jour est disponible, le Metteur à jour téléchargera un fichier compressé depuis le Serveur de Mise à jour. Il extraira le contenu dans un nouveau dossier. Si c'est la première fois que l'utilisateur ouvre le Metteur à jour, il recevra un package contenant l'Application. **Si l'utilisateur a téléchargé un installeur plus ancien, cette méthode garantit qu'il n'est pas nécessaire de télécharger l'application deux fois.**
5. Le Metteur à jour démarre l'Extracteur.

### L'Extracteur

Le but de l'Extracteur est que le Metteur à jour lui-même puisse se mettre à jour. L'Extracteur n'a même pas besoin d'une interface.

1. L'Extracteur effectue tout nettoyage nécessaire.
2. Il déplace les fichiers du dossier de contenu extrait vers l'endroit où l'Application réside.
3. L'Extracteur démarre le Metteur à jour.

### Le Serveur de Mise à jour

Pourquoi ne pas héberger les binaires sur un serveur web au lieu de construire une application de serveur de mise à jour dédiée ? Eh bien, il n'est pas possible de faire des choses comme la vérification du framework client avec un serveur web, et il ne pourra pas construire de packages de mise à jour delta. Cela aide également pour des choses comme déterminer si une réparation est nécessaire ou non. Il peut également y avoir des situations de migration de version uniques qui peuvent nécessiter une gestion.

1. Sur le serveur, tous les composants du système de mise à jour résident dans un dossier auquel il a accès. Lorsqu'il démarre, il construit son propre dictionnaire de hachage de chacun de ces fichiers.
2. La version nécessaire du framework dépendant est définie comme un paramètre de configuration sur le Serveur de Mise à jour. Si le message envoyé par le Metteur à jour est inférieur à la version, il instruira le Metteur à jour de télécharger et d'installer le nouveau framework.
3. Lorsque l'équipe de développement est prête à déployer une nouvelle version, elle remplace les fichiers que le Serveur de Mise à jour a inventoriés. Ils actualisent le dictionnaire de hachage.
4. Vous vous souvenez lorsque le Metteur à jour a envoyé ce dictionnaire de hachage ? Eh bien, le Serveur de Mise à jour compare les deux dictionnaires et détermine les fichiers obsolètes du client. C'est ainsi qu'il construit les packages delta.
5. Il compresse le package, et le Serveur de Mise à jour enverra un message pour que le Metteur à jour commence son téléchargement.

Le schéma suivant illustre le processus de mise à jour :

![Image](https://cdn-media-1.freecodecamp.org/images/g2nfdHXCh9PRVphA3yBr0LZMVQ6BYqMOVyKG)

### Derniers mots

Dans cette conception, le Metteur à jour est le point d'entrée de l'application. Cela n'a pas besoin d'être le cas cependant. Voici quelques questions à poser lors de la construction d'un système de mise à jour :

* Demandez-vous si l'utilisateur veut mettre à jour, rendez-vous cela obligatoire, ou cachez-vous le processus ?
* Le Metteur à jour doit-il être un composant séparé ? Il peut être intégré dans l'application elle-même.
* La mise à jour est-elle nécessaire avant que l'application ne commence ? Peut-être peut-elle se mettre à jour pendant que l'application est en cours d'exécution.

Ce sont des types de questions que le développeur devrait considérer avant de se lancer dans une conception. La mise à jour automatique des applications devient de plus en plus populaire, et pour de bonnes raisons. C'est plus facile pour l'utilisateur, et cela permet au code du développeur d'arriver plus rapidement entre leurs mains. **En tant qu'ingénieur, efforcez-vous de rendre votre processus de mise à jour meilleur pour vous et vos utilisateurs.**

Merci d'avoir lu !