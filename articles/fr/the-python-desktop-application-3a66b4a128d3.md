---
title: Comment transformer une application Web en application de bureau, en utilisant
  Chromium et PyInstaller
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-27T23:23:18.000Z'
originalURL: https://freecodecamp.org/news/the-python-desktop-application-3a66b4a128d3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lmD7FIkUL4t5P-swMEPH7Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment transformer une application Web en application de bureau, en utilisant
  Chromium et PyInstaller
seo_desc: 'By Cristian Medina

  Packaging and distributing your app sounds simple in principle. It’s just software.
  But in practice, it’s quite challenging.

  I’ve been working on a Python module called Sofi that generates user interfaces.
  It can deliver a desktop ...'
---

Par Cristian Medina

L'emballage et la distribution de votre application semblent simples en principe. Ce n'est que du logiciel. Mais en pratique, c'est assez difficile.

J'ai travaillé sur un module Python appelé [Sofi](https://github.com/tryexceptpass/sofi) qui génère des interfaces utilisateur. Il peut offrir une expérience de bureau tout en utilisant des technologies web standard à page unique. Pour plus de flexibilité, je l'ai conçu pour fonctionner avec deux méthodes de distribution : dans le navigateur et exécutable.

En s'exécutant dans le navigateur, il fonctionne comme une page web normale. Vous pouvez le charger en ouvrant un fichier ou le lancer depuis votre terminal. J'ai également construit un exécutable qui s'exécute comme une application emballée, indépendante et sans dépendances externes.

Avec le temps, alors que je codais dans Atom — mon éditeur de choix ces jours-ci — je me suis souvenu qu'Atom est en fait un navigateur. Il utilise Node.js comme backend et le framework Electron pour son interface utilisateur. Cela m'a inspiré à commencer à explorer les internes d'Electron, espérant trouver des exemples et des meilleures pratiques sur la manière dont ils ont résolu l'emballage pour le bureau.

Il n'a pas fallu longtemps pour découvrir que tout est construit sur des technologies libres et open source : le navigateur Chromium et le [Chromium Embedded Framework](https://bitbucket.org/chromiumembedded/cef). Cela présentait des personnalisations faciles à intégrer, capables de répondre à mes exigences.

Avec tout cela en main, je me suis mis au travail.

#### Le Chromium Embedded Framework

Chromium est le code de base qui alimente le navigateur Chrome de Google. Il rassemble tous les éléments qui rendent une interface, traitent les entrées utilisateur et scriptent ses fonctions.

Le Chromium Embedded Framework (CEF) est un ensemble de fonctions C qui peuvent contrôler ce navigateur. Il fournit également des scripts qui aident à simplifier le processus de construction et de compilation.

Visual Studio Code, Slack, Mattermost, Curse, Postman et Kitematic sont tous des exemples d'applications de bureau qui utilisent Electron. Ces systèmes sont tous qualifiés de sites web qui exploitent le navigateur sous-jacent avec CEF.

Si vous pensez que Python peut se lier avec C et tirer parti de ces fonctionnalités également, alors vous avez raison. Ne cherchez pas plus loin que le projet [pycef](https://github.com/cztomczak/pycef) pour appeler directement les fonctions d'enveloppement de CEF. Cependant, il inclut le binaire Chromium comme dépendance supplémentaire. Donc, si vous êtes préoccupé par la gestion de déclarations de support compliquées, réfléchissez avant de vous lancer.

Dans ma situation particulière, le projet Sofi gère toutes les interactions via une websocket, offrant une interface cohérente sur différents types de plateformes (web, bureau, mobile, etc.). Cela signifie que je n'ai pas besoin de commander ou de piloter manuellement le navigateur. Je souhaite uniquement interagir avec le DOM que le navigateur affiche via des technologies web standard.

Mon objectif est de personnaliser les éléments de l'interface utilisateur qui font qu'un navigateur ressemble à un navigateur. Je dois supprimer les menus, les barres d'outils et les barres d'état. En faisant cela, je donnerai l'impression que nous sommes en mode plein écran — mais à l'intérieur d'une fenêtre d'application.

Étant donné mes exigences simples, j'ai estimé que pycef — ou toute autre liaison de bas niveau — était trop complexe. Au lieu de cela, j'ai tiré parti d'un exemple pré-construit du projet CEF : _cefsimple_. Ce navigateur masque tous les éléments visuels que je souhaite, donc si j'utilise son CLI pour ouvrir une page web, l'utilisateur n'a aucune idée qu'il se trouve réellement à l'intérieur d'un navigateur. Cela ressemble à une fenêtre normale de n'importe quelle application.

La construction de _cefsimple_ n'était pas trop compliquée une fois que j'ai parcouru la documentation. Mais cela prend un temps énorme si vous construisez également Chromium avec. Pour éviter cela, le projet lui-même fournit des binaires pré-construits que vous pouvez personnaliser et compiler dans cefsimple. J'ai trouvé qu'il était préférable de tirer parti de ceux-ci.

Les étapes sont les suivantes :

1. Jetez un coup d'œil rapide à [comment construire](https://bitbucket.org/chromiumembedded/cef/wiki/GeneralUsage#markdown-header-using-a-binary-distribution) avec CEF à partir de binaires.
2. Prenez l'une des [distributions binaires](http://opensource.spotify.com/cefbuilds/index.html) du dépôt. Assurez-vous de lire les infobulles avant d'en sélectionner une, car tous les paquets ne contiennent pas les mêmes fichiers. Je cherchais spécifiquement une avec `cefsimple`.
3. Parcourez le fichier `CMakeLists.txt` et assurez-vous d'installer les outils de construction nécessaires. Cela est spécifique à la plateforme.
4. Effectuez la construction. Cela est expliqué dans le même fichier que l'étape précédente et est également spécifique à la plateforme, mais cela tend à suivre le processus : créez et accédez au répertoire de construction, exécutez cmake pour vos outils de compilation et votre architecture tout en pointant vers le répertoire parent. Comme j'ai utilisé les outils OSX Ninja sur une plateforme 64 bits, la commande ressemblait à `cmake -G "Ninja" -DPROJECT_ARCH="x86_64" ..`
5. Le répertoire de construction contiendra maintenant les fichiers de sortie. La structure peut être un peu déroutante, mais elle est décrite dans le `README` principal. À titre de référence, l'étape précédente a abouti à un bundle d'application sous `build/tests/cefsimple/Release/cefsimple.app`.
6. N'oubliez pas que vous devrez faire cela pour créer les binaires dont vous avez besoin pour chaque plateforme et architecture de système d'exploitation que vous supportez.

Maintenant que vous avez un exécutable, exécutez-le depuis la ligne de commande avec `--url` défini sur la page web que vous souhaitez ouvrir. Cela signifie que l'incorporer dans un script Python est facilement fait via le module `subprocess`.

Bien que ce ne soit pas obligatoire, si vous êtes intéressé par la compilation de Chromium lui-même, consultez la documentation de CEF. Elle vous indiquera la bonne direction. Mais attention, cela prend beaucoup de temps à télécharger, construire et compiler. Une bonne puissance de traitement à l'ancienne aidera définitivement à obtenir des résultats plus rapides.

#### Emballage

Maintenant que nous pouvons offrir une expérience de bureau, nous devons considérer comment la distribuer à nos utilisateurs. La distribution traditionnelle des packages Python est réalisée via le Python Package Index (PyPI). Cependant, elle nécessite que nos utilisateurs installent l'interpréteur Python et une forme d'outil de packaging comme `easy_install` ou `pip`.

Bien que cela ne soit pas particulièrement difficile, vous devriez considérer une gamme plus large d'utilisateurs. La gestion d'un processus d'installation avec des étapes manuelles séparées devient assez compliquée. Surtout avec des publics non techniques — dont certains ne savent pas que Python est autre chose qu'un grand serpent. Alors que d'autres peuvent au moins connaître la vitesse de vol d'une hirondelle européenne non chargée.

S'ils connaissent le langage, la plupart ont déjà leur propre version installée. C'est là que les dépendances de packages, les différents systèmes d'exploitation, les navigateurs dont vous n'avez jamais entendu parler (ou que vous pensiez morts à l'heure actuelle) entrent en jeu, ainsi que les compétences variées des utilisateurs à configurer des environnements virtuels. Cela tend à se traduire par une grande quantité de temps passé à supporter des logiciels incompatibles.

Pour éviter un tel désordre, il existe des outils qui peuvent intégrer toutes vos dépendances dans des fichiers exécutables spécifiques au système d'exploitation. Après une réflexion approfondie, celui que j'ai choisi pour mes entreprises est [PyInstaller](https://github.com/pyinstaller/pyinstaller). Il semble offrir la plus grande flexibilité en termes de plateformes et de formats supportés.

Un bref extrait de leur dépôt GitHub résume bien les choses :

> PyInstaller lit un script Python écrit par vous. Il analyse votre code pour découvrir chaque autre module et bibliothèque dont votre script a besoin pour s'exécuter. Ensuite, il collecte des copies de tous ces fichiers — y compris l'interpréteur Python actif ! — et les place avec votre script dans un seul dossier, ou éventuellement dans un seul fichier exécutable.

L'outil a tenu sa promesse. Je l'ai pointé vers le fichier Python de mon application d'exemple et il le regroupe dans un répertoire assez facilement avec : `pyinstaller sample.py`. Lorsque je veux un exécutable à la place, il suffit d'ajouter le paramètre `--onefile`.

Cela devient un peu plus délicat lorsque vous devez ajouter des données non-Python à votre bundle. C'est le cas avec les fichiers html et js qui forment la base de Sofi, et le navigateur _cefsimple_ qui présente l'interface de l'application depuis plus tôt. L'utilitaire PyInstaller fournit `--add-data` pour faire exactement cela, permettant une cartographie vers le chemin dans votre bundle où le fichier de données (ou répertoire) résidera. Cependant, il m'a fallu un certain temps pour comprendre comment accéder correctement à ces répertoires depuis mon code. Heureusement, la documentation m'a indiqué la bonne direction.

Il s'avère que, lors de l'exécution d'une application regroupée par PyInstaller, vous ne pouvez pas vous fier à `__file__` et à des mécanismes similaires pour déterminer les chemins. Au lieu de cela, le chargeur de démarrage de PyInstaller stocke le chemin absolu vers le bundle dans `sys._MEIPASS` et ajoute un attribut `frozen` pour vous faire savoir que vous exécutez à l'intérieur d'un bundle. Si `sys.frozen` est `True`, chargez vos fichiers en fonction de `sys._MEIPASS`, sinon utilisez des fonctions de chemin normales pour déterminer où se trouvent les choses.

J'ai réussi à créer à la fois une application regroupée OSX et un binaire exécutable Linux du même script Python. J'ai vérifié que je pouvais faire de même avec un exécutable Windows, mais je n'ai pas encore eu le temps de mettre ensemble une version Windows du navigateur _cefsimple_ pour tester le chemin du bundle.

#### Le Produit Final

Pour un exemple de l'interface utilisateur basée sur un navigateur emballée avec le système décrit ici, consultez ma présentation à PyCaribbean 2017.

La démonstration pertinente pour CEF et l'emballage est celle d'une galerie d'images et elle apparaît vers 18:15.

Pour des lectures supplémentaires sur la façon dont j'ai créé Sofi, consultez la série [A Python Ate My GUI](http://tryexceptpass.org/article/a-python-ate-my-gui/).

---

Si vous avez aimé l'article et souhaitez en lire plus sur Python et les pratiques logicielles, veuillez visiter [tryexceptpass.org](https://tryexceptpass.org). Restez informé avec leur dernier contenu en vous abonnant à [la liste de diffusion](https://tinyurl.com/tryexceptpass-signup).