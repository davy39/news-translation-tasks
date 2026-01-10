---
title: Un aperçu de Visual Studio Code pour les développeurs front-end
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-05T17:27:55.000Z'
originalURL: https://freecodecamp.org/news/an-overview-of-visual-studio-code-for-front-end-developers-49a4aa0771fb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fEUJfqoKCP2YsEHBfXUVBw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Un aperçu de Visual Studio Code pour les développeurs front-end
seo_desc: 'By Vinh Le

  No matter whether you are a code newbie or a seasoned developer, code editor is
  an imperative part of your work. The problem, especially if you are a beginner,
  is that there are tons of choices for IDEs. And many of them share similar feat...'
---

Par Vinh Le

Que vous soyez un novice en programmation ou un développeur expérimenté, l'éditeur de code est une partie essentielle de votre travail. Le problème, surtout si vous êtes débutant, est qu'il existe une multitude de choix pour les IDE. Et beaucoup d'entre eux partagent des fonctionnalités, des fonctionnalités et même une interface utilisateur similaires. Par conséquent, choisir le bon IDE peut en réalité prendre plus de temps et d'efforts que vous ne le pensiez.

Si votre question est : « Quel éditeur de code devrais-je utiliser ? », alors je répondrais : « Cela dépend, mon ami. » Le choix d'un IDE particulier dépend de plusieurs facteurs : le type de développeur que vous êtes, les types d'environnements avec lesquels vous travaillez principalement, ou si vous avez une fonctionnalité intégrée exclusive dont vous avez absolument besoin pour accomplir vos tâches.

Je dirais que la façon de choisir un IDE est de les essayer et de les explorer tous, puis de choisir celui qui vous convient le mieux.

# Choisir le bon éditeur de code pour vous

Comme la plupart des débutants, j'ai commencé avec Notepad++ comme premier éditeur de code. C'est probablement l'un des IDE les plus simples que j'ai essayés. Plus tard, lorsque mes besoins ont commencé à nécessiter des fonctionnalités plus avancées de l'éditeur, j'ai essayé Brackets, Atom, puis Visual Studio Code.

Après une quantité décente d'expérimentation, VSCode est devenu mon préféré. Il m'a impressionné avec son interface utilisateur moderne, une large disponibilité d'extensions, ainsi que de grandes fonctionnalités telles que Git intégré et le terminal.

Le but principal de ce blog n'est pas de comparer différents IDE, mais de discuter de mon expérience avec VSCode. Donc dans cet article, je vais :

* présenter une brève introduction à VSCode
* présenter le thème particulier que j'ai installé
* discuter des extensions utiles que j'utilise
* vous montrer comment je tire parti des fonctionnalités de VSCode pour améliorer mon flux de travail.

Commençons !

# Mais d'abord, qu'est-ce que VSCode ?

Visual Studio Code (VSCode) est un éditeur de code source développé par Microsoft qui peut être exécuté sur Windows, macOS et Linux. Il est gratuit, open-source et offre un support pour le débogage ainsi que le contrôle de version Git intégré, la coloration syntaxique, les extraits de code, et bien plus encore. L'interface utilisateur de VSCode est hautement personnalisable, car les utilisateurs peuvent basculer entre différents thèmes, raccourcis clavier et préférences.

VSCode a été initialement annoncé en 2015 en tant que projet open-source hébergé sur GitHub avant d'être publié sur le web un an plus tard. Depuis lors, l'éditeur de code de Microsoft a gagné en popularité parmi les développeurs.

Dans l'enquête [Stack Overflow 2018 Developer Survey](https://insights.stackoverflow.com/survey/2018/), VSCode a été classé comme l'environnement de développement le plus populaire avec environ 35 % des plus de 100 000 répondants disant qu'ils l'utilisent. Plus impressionnant encore, ce chiffre est d'environ 39 % dans le domaine du développement web.

Et avec des mises à jour mensuelles, les utilisateurs peuvent s'attendre à une expérience encore meilleure - des corrections de bugs, une stabilité et des améliorations de performance sont fréquemment poussées.

# Thème : Couleur et Police

Si vous êtes comme moi, et que vous vous souciez du thème de votre IDE, trouver une police et une couleur de thème appropriées est très important. Je préfère personnellement un thème sombre et je déteste la police Consolas par défaut de VSCode sur Windows.

Donc, le thème de couleur **Monokai** et la police **FiraCode** sont mes choix actuels. Cette combinaison offre un contraste élevé que je trouve très agréable pour travailler.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_3Hbizu5ONhDrQSzw.png)

* Pour installer un thème, cliquez sur l'icône des paramètres => Thème de couleur => Choisissez le thème que vous aimez
* Trouvez le guide d'installation de FiraCode [ici](https://github.com/tonsky/FiraCode).
* Vous pouvez également consulter **OneDarkPro**, un autre excellent thème sombre : dans les Extensions (Ctrl + Shift + X sur Windows), recherchez OneDarkPro, cliquez sur Installer, et sélectionnez-le dans le Thème de couleur.

# Extensions utiles (Extensions => Recherche => Installation)

Voici quelques-unes de mes extensions préférées :

* [**Beautify**](https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify) : Embelli le code en place et rend votre code plus lisible
* **Bracket Pair Colorizer** : permet d'identifier les parenthèses correspondantes avec des couleurs

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_vD9MA7SB6_wysUbt.png)
_Les couleurs de ( et { sont séparées, n'est-ce pas ?_

* [**ESLint**](https://eslint.org/) : une extension indispensable pour les développeurs React ou JavaScript en général. ESLint est utilisé pour trouver des problèmes et des fautes de frappe dans votre code, et vous permet de marquer cette faute de frappe. Il suggère également des solutions.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_XhWMwqhcdl4k3L5M.png)

* **HTML Snippets** : ajoute un support de langage riche pour le balisage HTML tel que la fermeture automatique des balises.
* **JavaScript (ES6) code snippets** : assez explicite
* **Live Server** : lance un serveur local avec des fonctionnalités de rechargement en direct pour votre site HTML ou PHP
* **Markdown Preview Enhanced** : lance un serveur en direct pour votre fichier markdown.
* **Material Icon Theme** : fournit des icônes basées sur le Material Design de Google. Pour l'activer, cliquez sur _Paramètres => Thème des icônes de fichier => Sélectionnez Material Icon Theme_
* **Prettier** : formate magnifiquement votre code JavaScript/TypeScript/CSS.

# Personnalisez votre interface utilisateur

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_IrMw_PwCRvt0ub5x.png)

Vous pouvez personnaliser presque tout, de la famille de polices et de la taille de la police de votre code à la hauteur de ligne, en :

* Allant dans **Paramètres utilisateur (Ctrl + ,)**
* Recherchant des mots-clés liés à votre personnalisation souhaitée
* Cliquant sur le bouton Modifier sur le côté gauche des paramètres et choisissant Remplacer dans les paramètres
* Changeant la valeur du paramètre que vous venez de choisir.

Dans ma configuration actuelle, j'ai défini la taille de la police à 14, la hauteur de ligne à 22 et la taille de la tabulation à 3 pour ma préférence personnelle (et pour une bonne lisibilité).

# Choses que j'aurais aimé savoir depuis le début

En plus de ces thèmes et extensions, je voudrais partager avec vous comment j'utilise les grandes fonctionnalités de VSCode pour améliorer la productivité. Ce sont toutes des choses que je ne savais pas en tant que débutant, et qui auraient été très utiles pour tirer parti et faciliter mon flux de travail.

## Terminaux intégrés

Il est inévitable que plus vous passez de temps dans le développement logiciel, plus le Terminal devient important. En tant que développeur JavaScript, j'utilise le Terminal pour installer des packages, exécuter le serveur de développement, ou même pousser des changements dans mon dépôt actuel vers GitHub.

Au début, je m'occupais principalement de ces tâches avec l'invite de commande Windows ou Git Bash plus tard. Si vous utilisez Windows, alors vous savez à quel point CMD peut être stupide et ennuyeux. Git Bash est un bon outil, mais basculer entre les applications lorsque vous travaillez n'est pas vraiment une expérience agréable.

VSCode résout vraiment ce problème pour moi avec son terminal fantastique. Et le plus cool, c'est que vous pouvez facilement le configurer pour qu'il fonctionne de la même manière que Git Bash, mais directement dans VSCode ! Vous avez alors une combinaison géniale.

Pour accéder au terminal VSCode, utilisez **Ctrl + ` (à gauche de votre touche 1)**. Ensuite, le Terminal apparaîtra.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_f7fzEsGoAAWe3bpq.png)

À partir de là, vous pouvez faire des tonnes de choses cool comme créer un nouveau terminal ou tuer celui existant. Vous pouvez également les diviser en vue divisée ainsi qu'en vue latérale.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_rKqG80RkVDPiiu0Z.png)
_C'est cool d'avoir plusieurs terminaux intégrés directement dans votre éditeur de code, n'est-ce pas ?_

## Contrôle de source (Git)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_wuw9PVTrCZAvURR6.png)

Lorsque vous travaillez sur un dépôt et que vous devez constamment apporter des modifications, vous trouveriez normalement le terminal pour valider les modifications récentes, n'est-ce pas ? Eh bien, VSCode vous offre un outil intégré génial pour contrôler vos versions.

En cliquant sur l'icône Git située dans le panneau de gauche ou en utilisant Ctrl + Shift + G (Windows), vous avez un accès facile au Contrôle de source. Ici, vous pouvez faire toutes les choses Git. Si pratique, n'est-ce pas ?

# Comment toutes ces choses améliorent-elles mon flux de travail - et comment peuvent-elles améliorer le vôtre aussi ?

Après une quantité décente de temps à travailler avec VSCode, je crois fermement que sa valeur clé réside dans son environnement tout-en-un. Tous mes besoins et tâches dans mon flux de travail en tant que développeur front-end sont bien et sans faille gérés.

Pour rendre ces avantages plus clairs, laissez-moi vous guider à travers mon flux de travail normal.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_z6IPS9tRac4GW_vc.png)

Disons que j'ai quelques idées pour travailler sur une nouvelle application musicale créée avec React. Je commence normalement un projet en créant un dossier vide - donc je vais créer un nouveau dossier nommé **music_react**. Après cela, je peux immédiatement ouvrir le projet dans VSCode en choisissant une option de clic droit.

Une fois que je suis dans mon projet de travail, je peux rapidement créer le fichier et les dossiers avec des raccourcis dans le panneau de gauche.

Dans ce projet, je veux utiliser l'initialisation **create-react-app**. Par conséquent, je devrais peut-être installer ce package - ce n'est pas un gros problème. J'ouvre mon terminal en tapant Ctrl + `. Incroyablement, le terminal navigue automatiquement vers mon répertoire exact. Il n'est plus nécessaire de changer de répertoires.

Après avoir entré dans la ligne de commande pour installer le package npm, tout ce que je dois faire est d'attendre que toutes les dépendances soient installées.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_lNgIoaLH8JzJAkL1.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_0TqpJnj1afgKVW18.png)

Je veux également publier mon projet sur GitHub, donc je devrais probablement initialiser un dépôt Git au préalable. Après l'installation des packages, je tape une commande d'initialisation Git directement dans mon terminal également.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/0_MmZy6cvYDSU76GMf.png)

Une fois Git installé avec succès, je peux valider toutes les modifications en attente directement dans le Contrôle de source du panneau de gauche.

Ensuite, je peux continuer à travailler sur mon projet comme d'habitude. De plus, je peux pousser toutes les modifications vers GitHub depuis mon terminal si je le souhaite.

# Conclusion

Voilà donc mon flux de travail normal dans l'environnement VSCode. Je comprends que cela varie considérablement en fonction du type de développeur que vous êtes. Un développeur back-end pourrait avoir un flux de travail complètement différent du mien.

Cependant, si vous êtes un développeur front-end qui commence à connaître VSCode, et que vous souhaitez l'essayer avant de vous y mettre, j'espère que cet article vous donne un aperçu et vous aide à améliorer votre productivité. Après tout, ma plus grande inspiration pour écrire ce petit guide est que je n'ai pas vraiment trouvé de critique approfondie de VSCode pour les nouveaux venus. Par conséquent, ce blog espère vous apporter une certaine valeur.

Enfin, si votre configuration est différente de la mienne ou s'il existe de grandes extensions que vous pensez être bien d'avoir, n'hésitez pas à les partager dans les commentaires. Je suis ravi d'avoir de vos nouvelles !