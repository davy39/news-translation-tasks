---
title: Meilleurs outils de débogage à distance en 2020
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-17T08:01:19.000Z'
originalURL: https://freecodecamp.org/news/remote-debugging-tools
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Remote-Debugginng-Tools-3.png
tags:
- name: debugging
  slug: debugging
- name: remote work
  slug: remote-work
- name: remote-working
  slug: remote-working
seo_title: Meilleurs outils de débogage à distance en 2020
seo_desc: "By Anton Lawrence\nWhen it comes to debugging, the tool you use is extremely\
  \ important and can determine how easy is is to fix problems within your code. \n\
  In the early days, the debugging process was quite a challenge. With the distinct\
  \ lack of reliab..."
---

Par Anton Lawrence

En matière de débogage, l'outil que vous utilisez est extrêmement important et peut déterminer la facilité avec laquelle vous pouvez corriger les problèmes dans votre code. 

Dans les premiers temps, le processus de débogage était assez difficile. Avec le manque distinct d'outils de débogage fiables, les développeurs se tournaient vers plusieurs astuces. 

Par exemple, lors du débogage d'une application mobile ou d'un site web, vous deviez recréer les problèmes sur votre bureau et utiliser les outils de développement Chrome et des kits d'outils similaires.   
  
Malheureusement, ces astuces n'étaient pas aussi efficaces — vous deviez constamment passer de votre navigateur de bureau à votre appareil mobile.

Aujourd'hui, nous disposons d'une puissante suite d'outils qui permettent de déboguer du code défectueux s'exécutant sur un autre appareil comme s'il s'agissait de code local. Mieux encore, ces outils de débogage à distance non seulement répondent aux défis du débogage, mais améliorent également la collaboration au sein des équipes de développement. 

Dans cet article, j'ai rassemblé les dix meilleurs outils de débogage à distance qui peuvent être utilisés de manière fiable pour déboguer votre code à distance.

## Rookout

![Image](https://www.freecodecamp.org/news/content/images/2020/04/rookout-remote-debugging.jpeg)

Rookout est un outil qui apporte de l'agilité au processus de débogage. Il peut être utilisé pour déboguer du code JVM, Node.JS et Python dans des applications serverless et conteneurisées.   
  
La beauté de Rookout réside dans sa capacité à permettre aux utilisateurs de déboguer rapidement et en toute sécurité les applications de staging et de production. Il élimine les processus de débogage longs et compliqués en fournissant toutes les données nécessaires en quelques secondes.   
  
Les données à la demande fournies par Rookout garantissent que les développeurs peuvent comprendre et déboguer les problèmes présents dans leur code sans coder, redéployer ou redémarrer leurs applications.

Avec Rookout, vous pouvez déboguer à distance des applications Electron en direct. L'interface partageable de Rookout permet aux développeurs de définir des points d'arrêt non bloquants dans les applications Electron problématiques.   
  
L'outil vous donne une visibilité complète sur les performances de votre application, afin que vous puissiez tracer les problèmes et développer des correctifs appropriés. Rookout rend tout cela possible sans avoir besoin d'installer un autre logiciel sur l'utilisateur final.

### Points forts

* Facile à démarrer
* Intégration transparente avec Git
* S'intègre avec une gamme d'outils incluant Slack, Datadog, Sentry, Sumologic, et plus
* Capacités de suivi des interactions et de partage d'écran
* Fournit des données de débogage complètes en temps réel

## Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) est toujours un choix de premier ordre pour chaque développeur travaillant avec .NET. Il dispose d'une tonne de fonctionnalités pour faciliter le débogage local et à distance. Avec cet outil, vous pouvez définir des points d'arrêt conditionnels et des points de journalisation.  
  
Il permet également d'inspecter les variables. Pour le débogage à distance, vous devrez installer le [pack d'extension de développement à distance de VS Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). Ce pack contient trois extensions qui fournissent tout ce dont vous avez besoin pour lancer, surveiller et accélérer votre boucle de débogage à distance.

### Points forts

* Gratuit à utiliser, opérations multiplateformes
* Communauté de développement très active avec le soutien de Microsoft
* Contrôle Git intégré
* Prend en charge une large gamme d'extensions et d'options de personnalisation pour l'amélioration du flux de travail
* Vérification automatique des erreurs et coloration syntaxique excellente

## RubyMine

[RubyMine](https://www.jetbrains.com/ruby/) est un IDE intelligent et puissant multiplateforme qui permet de déboguer Ruby on Rails, CoffeeScript, JavaScript, CSS, ERB et HAML, et plus encore. Son débogueur intégré avancé permet de définir des points d'arrêt et de définir des conditions de déclenchement avec facilité.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/qhHcGFYO.png)

RubyMine de JetBrains offre deux façons de déboguer des applications qui s'exécutent sur des appareils distants. Tout d'abord, vous pouvez ajouter l'[interpréteur Ruby distant](https://www.jetbrains.com/help/ruby/configuring-language-interpreter.html#add_remote_ruby_interpreter) et configurer les mappages entre les fichiers de projet locaux et distants, puis lancer votre session de débogage.   
  
Alternativement, vous pouvez exécuter des applications sur l'appareil distant puis ajouter l'interpréteur Ruby.   
  
Une fois terminé, configurez les mappages entre les fichiers et liez à un processus en cours d'exécution. Ce dernier est particulièrement utile lors du débogage d'une application que vous ne pouvez pas lancer directement depuis votre IDE. 

Une autre grande chose à propos de cet outil est qu'il permet de lancer plusieurs processus de débogage simultanément.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/KzzzZclD.png)

### Points forts

* RubyMine est basé sur la plateforme solide intelliJ IDEA
* Bon support pour les frameworks et technologies liés à Ruby
* La fonction d'autocomplétion est assez bonne
* Bonne intégration avec Git.
* Prend en charge plusieurs plugins
* S'intègre parfaitement avec Rails

## PyCharm

![Image](https://www.freecodecamp.org/news/content/images/2020/04/fiYc7Lxc.png)

[PyCharm](https://www.jetbrains.com/pycharm/) est un autre IDE robuste développé par JetBrains pour Python. Cet éditeur de code intelligent est équipé de capacités de développement à distance, y compris l'exécution, les tests, le débogage, le déploiement et les applications sur des machines virtuelles et des hôtes distants. 

Le débogueur offre plusieurs points d'arrêt, une vue des cadres, des moniteurs, des modes de pas à pas, des interpréteurs distants et une console de débogage.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/pCiayilm.png)

Parmi les fonctionnalités incroyables de PyCharm, on trouve une autocomplétion sophistiquée, un excellent support de refactorisation et une intégration transparente avec des outils tels que Django, IPython, Docker, Vagrant et Pytest.   
  
De plus, PyCharm est un outil de développement multiplateforme merveilleux. En plus de Python, il prend en charge JavaScript, Cython, CoffeeScript, TypeScript SQL, HTML/CSS, Node.js, AngularJS, et plus encore.

### Points forts

* Connectivité impressionnante avec plusieurs bases de données pour les requêtes dans l'IDE
* Recherche et installation de packages faciles
* Complétion automatique du code
* Visualisation Git
* Affiche les erreurs de code à la volée et facilite leur correction

## GDB

GDB peut être utilisé efficacement pour déboguer des programmes sur un autre ordinateur. Pour effectuer un débogage à distance, vous devrez exécuter l'utilitaire GDB dans le système hôte. De plus, vous devez exécuter gdbserver sur le système cible afin que les deux utilitaires communiquent via un réseau ou une ligne série en utilisant le protocole série distant GDB.

Il existe deux options de configuration pour le débogage à distance avec GDB/gdbserver. La première consiste à utiliser le serveur GDB distant pour construire et télécharger automatiquement le code de l'application sur la machine distante.   
  
La deuxième option consiste à utiliser le débogage distant GDB où vous devez avoir les fichiers exécutables.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/P02ETVPk.png)

### Points forts 

* Facile à utiliser et à tracer les fautes dans le code
* Multiplateforme et support de nombreux langages
* Efficace pour l'analyse des vidages de mémoire

## Eclipse

Eclipse est un IDE renommé pour le développement Java qui prend également en charge des langages comme Python, Ruby, C# et PHP. L'IDE Eclipse est équipé de fonctionnalités avancées pour le développement et le débogage, ce qui en fait un outil polyvalent.   
  
L'une des fonctionnalités les plus impressionnantes d'Eclipse est la perspective de débogage de la plateforme qui affiche des informations de débogage détaillées telles que les points d'arrêt, les variables, les piles d'appels et les threads côte à côte.   
  
En utilisant Eclipse, vous pouvez parcourir l'exécution du programme, suspendre et reprendre les threads, évaluer les expressions et inspecter les valeurs. La gestion des [configurations de débogage à distance sur Eclipse](https://www.eclipse.org/jetty/documentation/current/debugging-with-eclipse.html) est assez facile et directe, ce qui rend l'outil plus populaire parmi les développeurs.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/CMTsLiXY.png)

### Points forts

* Complétion automatique du code
* Bon support de refactorisation
* Excellente capacité de navigation
* Aide à la vérification de la syntaxe pour un code propre et efficace
* Intégration Git

## Zend Studio Debugger

![Image](https://www.freecodecamp.org/news/content/images/2020/04/pM6wj0kR.png)

[Zend Studio](https://www.zend.com/downloads/zend-studio-web-debugger) est un IDE professionnel qui prend en charge l'édition, les tests, le débogage de code PHP, et plus encore.   
  
Il est étroitement intégré avec le [Zend Server](https://en.wikipedia.org/wiki/Zend_Server), créant ainsi un environnement PHP complet qui facilite l'analyse des problèmes détectés dans les environnements de staging et de production.   
  
Zend fournit également une extension PHP que les utilisateurs peuvent installer sur les serveurs web pour déboguer les scripts PHP. L'utilisation de Zend pour le débogage est relativement facile — vous n'avez besoin que d'ouvrir le code source, de définir des points d'arrêt dans le projet et d'exécuter une session de débogage.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/rHmFIozA.png)

Le débogage à distance sur Zend peut être effectué de trois manières. La première option consiste à utiliser la fonctionnalité Debug URL sur Zend Studio.   
  
Deuxièmement, vous pouvez utiliser la fonctionnalité Debug as Web Page dans Zend Studio. Et enfin, en utilisant la barre d'outils du navigateur Zend sur Firefox ou Chrome.

### Points forts

* Capacité à parcourir les fichiers du projet en quelques touches
* Plateforme très efficace et rapide
* Grand soutien de la communauté
* Excellent pour la construction et le débogage d'applications PHP
* Le framework est exceptionnellement flexible

## WinPdb

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Bl1p7hZs.png)

[WinPdb](http://winpdb.org/) est un excellent débogueur Python qui fonctionne bien sur les systèmes Windows, Mac OS et Linux. Il est compatible avec Python 2.x et Python 3.x.  
  
Cet outil de débogage prend en charge les points d'arrêt intelligents, la modification de l'espace de noms, les threads multiples, le débogage intégré et la communication chiffrée. Pour le débogage à distance, vous devrez copier rpdb2.py (le débogueur en ligne de commande de Winpdb) sur la machine distante.   
  
Une fois terminé, démarrez le script Python avec le débogueur sur la machine distante. Depuis votre appareil local, lancez l'interface graphique et attachez le script pour le débogage. À ce stade, vous pouvez utiliser le nom de base ou le chemin complet du script tel qu'il est sur l'appareil distant. Vous pouvez en savoir plus sur le débogage des scripts Python avec Win PDB [ici](http://winpdb.org/tutorial/WinpdbTutorial.html).

### Points forts

* Prend en charge le débogage multithread
* Communication chiffrée pour le débogage à distance
* Plus rapide que PDB
* Interface graphique facile à utiliser avec des points d'arrêt, une inspection de la pile/des variables, et plus encore

**Utilisez les outils ci-dessus pour améliorer votre expérience de débogage à distance. Bon codage !**