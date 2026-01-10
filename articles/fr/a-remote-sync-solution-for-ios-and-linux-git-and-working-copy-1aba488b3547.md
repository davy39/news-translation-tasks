---
title: 'Une solution de synchronisation à distance pour iOS et Linux : Git et Working
  Copy'
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-04-02T15:36:55.000Z'
originalURL: https://freecodecamp.org/news/a-remote-sync-solution-for-ios-and-linux-git-and-working-copy-1aba488b3547
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1fs_sMiHpsoYdX1uQMriYg.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Une solution de synchronisation à distance pour iOS et Linux : Git et
  Working Copy'
seo_desc: 'How to set up a cross-platform cloud sync solution for working anywhere
  using Git on iOS.

  I previously wrote about a (hackish) way to use a single Dropbox folder on a dual-boot
  Windows and Linux machine. I’ve since gained some sense gone full Linux w...'
---

#### Comment configurer une solution de synchronisation cloud multiplateforme pour travailler n'importe où en utilisant Git sur iOS.

J'ai précédemment écrit sur une méthode (un peu bricolée) pour utiliser un [seul dossier Dropbox sur un système dual-boot Windows et Linux](https://victoria.dev/verbose/how-i-set-up-a-single-dropbox-folder-on-my-dual-boot-windows-and-linux-system/). Depuis, j'ai adopté Linux avec Ubuntu 18.04 LTS, mais la configuration Dropbox semble ne plus être une option dans tous les cas. Heureusement, j'ai depuis trouvé une méthode bien meilleure (et beaucoup moins bricolée) pour synchroniser des fichiers à distance entre différents systèmes de fichiers. Reflétant ma configuration actuelle, je parle d'iOS (iPad et iPhone) et de ma machine Linux.

Le nouveau système de synchronisation est basé sur Git, très personnalisable et facilement extensible. Au-delà des fichiers texte, vous pouvez synchroniser tout ce que Git peut gérer (ce qui est presque tout – si vous souhaitez éditer vos fichiers `.gitignore` en déplacement, je ne suis pas sûr de pouvoir vous aider). Si vous êtes déjà familier avec Git, la configuration sera un jeu d'enfant. Si Git est nouveau pour vous, je pense que ces outils aident à rendre les concepts de clonage, de pull et de push Git faciles à comprendre.

### Composants

* [Application Working Copy](https://workingcopy.app) (15,99 $, achat unique pour le déverrouillage pro, bien worth it, iOS uniquement)
* [Application iA Writer](https://ia.net/writer) (8,99 $, achat unique pour iOS, également disponible sur Mac, Windows et Android)
* Dépôts GitHub ([privés](https://github.blog/2019-01-07-new-year-new-github/) ou publics, tous deux gratuits)

Je me suis inspiré de [cet article](https://www.macstories.net/ios/my-markdown-writing-and-collaboration-workflow-powered-by-working-copy-3-6-icloud-drive-and-github/) ainsi que de [celui-ci](http://blog.joncairns.com/2011/10/how-to-use-git-submodules/).

### Configuration

Voici les étapes de configuration que je vais vous expliquer dans cet article.

1. Créez votre dépôt distant
2. Clonez le dépôt sur iPad avec Working Copy
3. Ouvrez et éditez les fichiers avec iA Writer
4. Poussez les changements vers le dépôt distant
5. Récupérez les changements depuis le dépôt sur votre ordinateur

Ce système est simple à configurer, que vous soyez un expert de la ligne de commande ou que vous débutiez avec Git. Commençons !

#### Créez votre dépôt distant

GitHub propose désormais des [dépôts privés gratuits](https://github.blog/2019-01-07-new-year-new-github/) pour jusqu'à trois collaborateurs. Choisissez « Private » sur la page de création de dépôt de GitHub :

![Image](https://cdn-media-1.freecodecamp.org/images/ItFaqv-hTrHTAZBHmsGEffVasUsDH-RqlyqU)

Créez le dépôt. Si vous le souhaitez, vous pouvez suivre les instructions de GitHub pour pousser quelques fichiers depuis votre ordinateur, ou vous pouvez ajouter des fichiers plus tard depuis votre iPad.

#### Clonez le dépôt sur iPad avec Working Copy

Téléchargez [Working Copy](https://workingcopy.app) depuis l'App Store. C'est l'une des applications les plus chères que j'ai achetées, mais je pense qu'elle en vaut la peine. Le développeur [Anders Borum](https://twitter.com/palmin) a un historique solide de mises à jour fréquentes et d'intégration des dernières fonctionnalités pour les applications iOS, comme le [glisser-déposer](https://workingcopy.app/manual/dragdrop) sur iPad. Je pense qu'il a fixé un prix équitable pour son produit compte tenu du travail qu'il met dans sa maintenance et son amélioration.

Dans Working Copy, trouvez l'icône d'engrenage dans le coin supérieur gauche et touchez pour ouvrir les Paramètres.

![Image](https://cdn-media-1.freecodecamp.org/images/VuBXLHI2Tjs-mize4R-94tGwyJrdH4r43ajD)

Appuyez sur SSH Keys, et vous verrez cet écran :

![Image](https://cdn-media-1.freecodecamp.org/images/knqrfxBovulHFSbzBkwDamluhb4fBoacjSTT)

Les clés SSH, ou clés Secure Shell, sont des identifiants d'accès utilisés dans le [protocole SSH](https://en.wikipedia.org/wiki/Secure_Shell). Votre clé est un mot de passe que votre appareil utilisera pour se connecter de manière sécurisée à votre hôte de dépôt distant – GitHub, dans notre exemple. Comme toute personne ayant vos clés SSH peut potentiellement se faire passer pour vous et accéder à vos fichiers, il est important de ne pas les partager accidentellement, comme dans une capture d'écran sur un article de blog.

Appuyez sur la deuxième ligne qui ressemble à « WorkingCopy@iPad-xxxxxxxx » pour obtenir cet écran :

![Image](https://cdn-media-1.freecodecamp.org/images/qeX3GRpPhnr8oA3Em51b1nC6nd8t0897wyOy)

Working Copy prend en charge une connexion facile à la fois à BitBucket et GitHub. Appuyez sur « Connect With GitHub » ou BitBucket pour faire apparaître des écrans de connexion familiers qui autoriseront Working Copy à accéder à votre compte.

Une fois connecté, appuyez sur le symbole « + » dans le coin supérieur droit de la barre latérale pour ajouter un nouveau dépôt. Choisissez « Clone repository » pour faire apparaître cet écran :

![Image](https://cdn-media-1.freecodecamp.org/images/sf4D5NkNmRpjHzdccE3Vlgnzmg-ykFU5ToAO)

Ici, vous pouvez soit saisir manuellement l'URL distante, soit simplement choisir parmi la liste des dépôts que Working Copy récupère depuis votre compte connecté. Lorsque vous faites votre choix, l'application clone le dépôt sur votre iPad et il apparaîtra dans la barre latérale. Vous êtes connecté !

#### Ouvrez et éditez des fichiers avec iA Writer

L'une des (nombreuses) raisons pour lesquelles j'adore [iA Writer](https://ia.net/writer) est sa capacité à sélectionner votre dépôt distant nouvellement cloné comme emplacement de bibliothèque. Pour ce faire dans l'application iA Writer :

1. Depuis la liste principale de la bibliothèque, dans le coin supérieur droit de la barre latérale, appuyez sur « Edit »
2. Appuyez sur « Add Location… »
3. Une fenêtre contextuelle utile apparaît. Appuyez sur OK.
4. Depuis l'emplacement Working Copy, appuyez sur « Select » dans le coin supérieur droit, puis choisissez le dossier du dépôt.
5. Appuyez sur « Open », puis sur « Done »

Votre dépôt distant apparaît maintenant comme un emplacement dans la barre latérale. Appuyez dessus pour travailler dans ce répertoire.

Pendant que vous êtes dans cet emplacement, les nouveaux fichiers que vous créez (en appuyant sur l'icône de crayon et de papier dans le coin supérieur droit) seront enregistrés dans ce dossier localement. Au fur et à mesure que vous travaillez, iA Writer enregistre automatiquement votre progression. Ensuite, nous verrons comment pousser ces fichiers et modifications vers votre dépôt distant.

#### Poussez les changements vers le dépôt distant

Une fois que vous avez apporté des modifications à vos fichiers, rouvrez Working Copy. Vous devriez voir un point jaune sur votre dépôt modifié.

![Image](https://cdn-media-1.freecodecamp.org/images/cbUDJ3vGR0tbBfJVggpkEhKhXHJxzOVwmTrc)

Appuyez sur le nom de votre dépôt, puis sur « Repository Status and Configuration » en haut de la barre latérale. Vos fichiers modifiés seront indiqués par des points jaunes ou des symboles verts « + ». Cela signifie que vous avez modifié ou ajouté des fichiers, respectivement.

Working Copy est un client Git iOS génial, et vous pouvez appuyer sur vos fichiers pour voir des informations supplémentaires, y compris une comparaison des changements (« diff ») ainsi que l'état et l'historique Git. Vous pouvez même éditer des fichiers directement dans l'application, avec une [coloration syntaxique](https://workingcopyapp.com/manual/edit) pour ses nombreux langages pris en charge. Pour l'instant, nous allons voir comment pousser votre travail modifié vers votre dépôt distant.

![Image](https://cdn-media-1.freecodecamp.org/images/8Tpm89mGfCKzwYNQV6u6GOYqEyvcF2DrCDs-)

Sur la page « Repository Status and Configuration », vous verrez tout en haut qu'il y a des changements à valider. Si vous êtes nouveau dans Git, cela ressemble à « sauvegarder vos changements » dans votre historique Git, quelque chose généralement fait avec la commande terminal `[git commit](https://git-scm.com/docs/git-commit)`. Vous pouvez considérer cela comme la sauvegarde des fichiers que nous voudrons envoyer au dépôt GitHub. Appuyez sur « Commit changes ».

![Image](https://cdn-media-1.freecodecamp.org/images/HxVYK8VHBhl2bVQdnlt9sKmwYLBHKDwHDECl)

Entrez votre message de validation, et sélectionnez les fichiers que vous souhaitez ajouter. Activez l'interrupteur « Push » pour envoyer tout à votre dépôt distant lorsque vous validez les fichiers. Ensuite, appuyez sur « Commit ».

Vous verrez une barre de progression pendant que vos fichiers sont téléchargés, puis un message de confirmation sur l'écran d'état.

![Image](https://cdn-media-1.freecodecamp.org/images/CuKi9hmxEnUMgcSh3Qc2ZlcjlHCNXSLkd9cW)

Félicitations ! Vos changements sont maintenant présents dans votre dépôt distant sur GitHub. Vous avez réussi à synchroniser vos fichiers à distance !

#### Récupérez les changements depuis le dépôt sur votre ordinateur

Pour ramener vos fichiers mis à jour sur votre ordinateur, vous les récupérez depuis le dépôt GitHub. Je préfère utiliser le terminal pour cela car c'est rapide et facile, mais GitHub propose également un [client graphique](https://help.github.com/en/desktop/getting-started-with-github-desktop) si les commandes terminal semblent un peu étranges pour l'instant.

Si vous avez commencé avec le dépôt GitHub, vous pouvez le cloner dans un dossier sur votre ordinateur en suivant [ces instructions](https://help.github.com/en/articles/cloning-a-repository).

#### Restez synchronisé

Lorsque vous mettez à jour votre travail sur votre ordinateur, vous utiliserez Git pour pousser vos changements vers le dépôt distant. Pour ce faire, vous pouvez utiliser le [client graphique](https://help.github.com/en/desktop/getting-started-with-github-desktop) de GitHub, ou suivre [ces instructions](https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line).

Sur votre appareil iOS, Working Copy rend le pull et le push aussi simples qu'un seul clic. Sur la page Repository Status and Configuration, appuyez sur le nom du dépôt distant sous « Remotes ».

![Image](https://cdn-media-1.freecodecamp.org/images/u5dr0LkZTsYBvy2v4mk3me4RvEzdmtU9VUwA)

Ensuite, appuyez sur « Synchronize ». Working Copy se chargera des détails de la poussée de vos changements validés et/ou de la récupération de tout nouveau changement qu'il trouve depuis le dépôt distant.

### Pas mal, n'est-ce pas ?

Pour un développeur basé sur Git et accro au travail n'importe où comme moi, cette configuration ne pourrait pas être plus pratique. Working Copy rend vraiment la synchronisation avec mes dépôts distants sans effort, sans parler de la possibilité de travailler avec n'importe lequel de mes dépôts GitHub en déplacement.

Pour l'édition en déplacement, voici un conseil utile. Utilisez `.gitignore` dans votre dépôt de synchronisation si vous n'avez pas besoin de déplacer de gros fichiers, comme des images, avec vous. Cela empêchera les fichiers ignorés d'être poussés vers GitHub et récupérés sur votre appareil iOS - ils resteront uniquement sur le disque dur plus grand de votre ordinateur. Le fichier `.gitignore` de l'un de mes dépôts de synchronisation ressemble à ceci :

```
*.png
*.jpeg
*.jpg
*.mp4
*.gif
```

Cela signifie que tous les fichiers multimédias restent sur mon ordinateur, et je peux récupérer uniquement le contenu des fichiers texte sur mon iPad depuis GitHub pour travailler dessus lorsque je suis en déplacement.

J'ai récemment utilisé cette configuration pour faire un peu d'écriture tout en traînant dans l'atrium de la National Portrait Gallery de Washington DC, qui est agréablement photogénique.

![Image](https://cdn-media-1.freecodecamp.org/images/Ee1wX2GpB5ipu8cYJdMcrdyi2y2yWZltgeKR)

J'adorerais savoir comment cette configuration fonctionne pour vous et comment vous l'utilisez. En attendant, bon travail !