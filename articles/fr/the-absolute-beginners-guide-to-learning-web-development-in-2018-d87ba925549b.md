---
title: Le guide absolu du débutant pour apprendre le développement web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-02T01:44:40.000Z'
originalURL: https://freecodecamp.org/news/the-absolute-beginners-guide-to-learning-web-development-in-2018-d87ba925549b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*48Svhyucz8U4vEbhK8swpg.png
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Le guide absolu du débutant pour apprendre le développement web
seo_desc: 'By Jessica Chan

  This post was originally published on Coder-Coder.com.

  If you’re a beginner coder, this guide is for you!

  Here is what this guide covers:


  An explanation of the basic areas in web development,


  An overview of programming languages and...'
---

Par Jessica Chan

*Cet article a été initialement publié sur* [*Coder-Coder.com*](https://coder-coder.com/learn-web-development/)*.*

Si vous êtes un codeur débutant, ce guide est pour vous !

Voici ce que couvre ce guide :

* Une explication des **domaines de base** du développement web,
  
* Un aperçu des **langages de programmation et des frameworks**,
  
* Et des **ressources recommandées** pour vous aider à apprendre.
  

Il est conçu pour les débutants, avec des liens utiles et des informations pour vous donner un coup d'avance dans vos propres recherches.

Voici ce que nous allons aborder.

### Table des matières

*Des liens de saut sont inclus, afin que vous puissiez sauter d'une section à l'autre si vous le souhaitez !

### [Partie 1 : Commençons par les bases](#partie1)

* **Qu'est-ce que le développement web** : explication de ce qui se passe réellement lorsque vous chargez un site web dans votre navigateur.
  
* **HTML, CSS et JavaScript** : la base de chaque site web.
  
* Outils utiles : utilisation des **éditeurs de code et de Git**
  
* Qu'est-ce que le **front-end** et le **back-end** ?
  

### [Partie 2 : Ensuite, nous aborderons des compétences front-end plus intermédiaires](#partie2)

* **Design responsive** : faire en sorte que votre site web ait une belle apparence sur les ordinateurs, les tablettes et les téléphones.
  
* **Grunt, Gulp et WebPack** : utilisation d'outils de build pour faire une partie du travail à votre place !
  
* Une introduction aux **frameworks front-end JavaScript** : React, Vue et Angular
  

### [Partie 3 : Suivi des compétences back-end](#partie3)

* Un aperçu des **langages back-end** les plus couramment utilisés et de leur comparaison.
  
* Une rapide introduction aux **bases de données** et aux langages de bases de données que vous devriez apprendre.
  
* Les bases de la configuration d'un site web sur un **serveur**.
  

### [Épilogue : Ressources d'apprentissage](#epilogue)

* Une courte liste de cours en ligne, tutoriels et livres recommandés.
  

Maintenant, avant de passer en revue tout ce qui concerne les sites web... commençons par vous !

### Quel est votre objectif ultime en apprenant à coder ?

Dans son livre *Les 7 habitudes des gens efficaces*, Stephen R. Covey affirme que pour réussir, vous devez "commencer avec la fin en tête".

Considérez vos propres raisons de vous lancer dans le codage... Quelle fin visez-vous ?

Quel est votre objectif ultime ?

Cherchez-vous un passe-temps amusant, un changement de carrière, un emploi flexible qui vous permet d'être plus proche de votre famille ?

**Toute votre approche du développement web devrait être centrée sur la réalisation de ce rêve.**

Vous pouvez même essayer d'écrire votre objectif et de le placer quelque part où vous le verrez tous les jours, comme sur votre miroir de salle de bain ou à côté de votre ordinateur.

En parcourant cet article, gardez votre objectif à l'esprit et laissez-le déterminer les décisions que vous prenez : quelles langues apprendre, même comment vous choisissez d'apprendre.

Cela dit, commençons par les bases !

![Image](https://cdn-media-1.freecodecamp.org/images/1*wCBlcgi36bFR_JfU1pcp8Q.png align="left")

### Partie 1 : Les bases

Cela peut sembler évident, mais je vais le dire quand même :

**Au cœur du développement web, il s'agit de construire des sites web.**

Un site web peut être un simple site d'une page, ou il peut s'agir d'une application web incroyablement complexe.

Si vous pouvez le visualiser sur le web dans un navigateur, cela a à voir avec le développement web.

Voici une explication simple de la façon dont les sites web fonctionnent sur Internet :

1. **Les sites web** sont essentiellement un ensemble de fichiers stockés sur des ordinateurs appelés serveurs.
  
2. **Les serveurs** sont des ordinateurs utilisés pour héberger des sites web, ce qui signifie qu'ils stockent les fichiers du site web. Ces serveurs sont connectés au réseau géant appelé World Wide Web (pour utiliser le jargon des années 90), ou Internet.
  
3. **Les navigateurs** sont des programmes que vous exécutez sur votre ordinateur. Ils chargent les fichiers du site web via votre connexion Internet. Votre ordinateur est également connu sous le nom de **client**, qui se connecte au **serveur**.
  

**Pour aller plus loin**

* [Comment fonctionne Internet ?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/How_does_the_Internet_work) — Mozilla Developer Network
  
* [Quelle est la différence entre une page web, un site web, un serveur web et un moteur de recherche ?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Pages_sites_servers_and_search_engines) — Mozilla Developer Network
  

### Les 3 composants qui constituent chaque site web

Comme mentionné précédemment, les sites web sont constitués de fichiers, principalement des fichiers HTML, CSS et JavaScript.

Examinons chacun d'eux de plus près :

#### **HTML ou HyperText Markup Language**

HTML est la base de tous les sites web. C'est le principal type de fichier qui est chargé dans votre navigateur lorsque vous regardez un site web.

Vous pouvez en fait créer un site web très basique en utilisant uniquement HTML et aucun autre type de fichier.

Il n'aura pas l'air très intéressant, mais c'est le minimum dont vous avez besoin pour qu'un site web soit un site web.

*(Si vous êtes intéressé par les bases de HTML, vous pouvez consulter un* [*tutoriel vidéo/blog*](https://coder-coder.com/how-to-make-simple-website-html/) *que j'ai à ce sujet.)*

#### **CSS ou Cascading Style Sheets**

Sans CSS, un site web aura l'air aussi esthétiquement plaisant qu'un document Word.

Avec CSS, vous pouvez ajouter des couleurs de toutes sortes, des polices attrayantes, et disposer le site web de presque n'importe quelle manière qui vous plaît.

Vous pouvez même ajouter des animations et dessiner des formes en utilisant un CSS plus avancé.

#### **JavaScript**

JavaScript est un langage de programmation qui vous permet d'interagir avec les éléments du site web et de les manipuler.

Alors que CSS ajoute du style au HTML, JavaScript ajoute de l'interactivité et rend un site web plus dynamique.

Par exemple, vous pouvez utiliser JavaScript pour faire défiler jusqu'en haut de la page lorsque vous cliquez sur un bouton, ou pour créer un diaporama avec des boutons pour naviguer à travers les images.

Pour travailler avec des fichiers HTML, CSS et JavaScript, vous devrez utiliser un programme sur votre ordinateur appelé éditeur de code.

Ce qui nous amène au point suivant :

### Quel éditeur de code devriez-vous utiliser ?

C'est une question très courante, surtout si vous commencez tout juste.

Le meilleur éditeur de code pour vous dépendra fortement du type de code que vous écrivez.

Si vous faites principalement du HTML, du CSS et du JavaScript, vous pourriez coder dans le Bloc-notes de Windows ou TextEdit pour les Mac si vous le souhaitez.

Mais quel serait l'intérêt ?

Les programmes d'édition de code comme Sublime ou VS Code viennent avec beaucoup de fonctionnalités qui rendent simplement le codage plus facile.

Ils vous permettent d'indenter plusieurs lignes de texte à droite ou à gauche, et peuvent mettre en évidence le texte de différentes manières selon le langage du fichier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JCnyi8HTMhlUNX3Ym16S8A.jpeg align="left")

*Exemple de mise en évidence de la syntaxe dans VS Code*

Pour les langages back-end (nous aborderons ceux-ci dans une section ultérieure), vous aurez besoin d'un éditeur de code plus puissant appelé IDE (Integrated Development Environment). Les IDE ont des fonctionnalités qui vous permettent de déboguer et de compiler (traiter) votre code.

Voici quelques éditeurs de code populaires :

![Image](https://cdn-media-1.freecodecamp.org/images/0*z4FzNLD6u884XHFT.png align="left")

[**VS Code**](https://code.visualstudio.com/) : Cette version légère de Visual Studio, l'IDE principal de Microsoft, n'a que quelques années mais elle est devenue incroyablement populaire, grâce à sa rapidité, sa facilité d'utilisation et ses fonctionnalités puissantes. VS Code est mon éditeur personnel de choix, donc je peux être plutôt partial ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*XNya7s0zovmrqiRJ.png align="left")

[**Atom**](https://atom.io/)**:** Créé par GitHub et présenté comme un "éditeur de texte hackable", Atom est un éditeur très apprécié. L'un de ses principaux atouts est sa personnalisation. Vous pouvez installer des packages et des thèmes qui ajouteront des fonctionnalités au programme.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Qb5K88ZRZ2d9JP-m.png align="left")

[**Sublime**](https://www.sublimetext.com/) : Un programme extrêmement populaire qui existe depuis un certain temps. Comme Atom, vous pouvez installer des packages et des thèmes, et il offre également des performances rapides. Contrairement aux deux autres éditeurs, une licence Sublime coûte 70 $ (mais il est gratuit à essayer).

Je recommanderais d'essayer certains ou tous ces éditeurs, à des fins de comparaison. Ensuite, choisissez-en un et restez-y, en apprenant ses fonctionnalités et ses raccourcis clavier.

### Contrôle de version

Maintenant que vous avez votre éditeur de code et que vous commencez à écrire du code.

Cependant, que se passe-t-il si vous faites une erreur dans votre code et que l'appui sur Ctrl-Z pour annuler un million de fois ne fonctionne pas pour vous ? Que faites-vous ?

La réponse est le contrôle de version !

**Le contrôle de version est comme avoir des points de sauvegarde pour vos fichiers de code.**

Si vous pensez que vous pourriez être sur le point de faire des changements de code qui pourraient tout casser, vous pouvez créer un nouveau point de sauvegarde (appelé un commit).

Ensuite, si vous cassez votre site web, vous pouvez revenir à l'état où il était avant.

Cela peut être un sauveur si vous faites une erreur que vous devez désespérément annuler.

**Le contrôle de version semble génial ! Comment cela fonctionne-t-il ?**

L'utilisation d'un [système de contrôle de version](https://www.atlassian.com/git/tutorials/what-is-version-control) (VCS) implique de stocker vos fichiers de code et l'historique complet des modifications dans ce qu'on appelle un dépôt.

Généralement, vous utiliserez un dépôt par site web ou projet.

Ensuite, vous stockez votre dépôt en ligne dans ce qu'on appelle un **dépôt central**, et vous gardez également une version sur votre ordinateur dans un **dépôt local**.

Au fur et à mesure que vous apportez des modifications sur votre ordinateur, vous pouvez créer des commits et ensuite les pousser vers le dépôt central.

Ce processus permet à plusieurs personnes de travailler sur le même ensemble de code, même en modifiant les mêmes fichiers.

**Git est le VCS le plus populaire en ce moment**

Le principal système de contrôle de version de nos jours est [Git](https://git-scm.com/). Son principal concurrent est [Subversion](https://subversion.apache.org/) (SVN), un système plus ancien.

Mais la grande majorité des bootcamps de codage et des tutoriels utilisent Git, c'est donc ce que je recommanderais d'apprendre.

**Pour aller plus loin**

* [Tutoriel rapide sur les bases de l'utilisation de Git](https://try.github.io/levels/1/challenges/1)
  
* [Guide approfondi sur l'utilisation de GitHub](https://guides.github.com/activities/hello-world/)
  

Maintenant, alors que nous passons à l'explication des langages et frameworks réellement utilisés, nous utiliserons des termes que vous avez probablement déjà rencontrés : **front end et back end**.

### Le front end concerne l'apparence visuelle du site web.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1ZgqE7dZv3rSaRT2.gif align="left")

\_*[Sarah Maes via GIPHY](https://giphy.com/sarahmaes/" rel="noopener" target="*blank" title=")*

Le front end (ou côté client) fait référence à ce qui est chargé par le navigateur de l'utilisateur, également appelé le client.

Cela inclut le HTML et le CSS dont nous avons parlé au début. JavaScript était à l'origine simplement un langage front-end, mais de nos jours, vous pouvez utiliser JavaScript comme langage côté serveur, ou back-end.

**Le travail front-end consiste principalement à rendre le site web esthétiquement agréable.**

De plus, il implique également de faire en sorte que le site se comporte de manière à avoir du sens pour l'utilisateur (également appelé UX ou expérience utilisateur).

Si vous aimez ajuster votre CSS pour vous assurer que le site est pixel parfait, et ajouter des animations JavaScript subtiles qui aident l'utilisateur, alors vous aimerez probablement le développement front-end.

### Le back end concerne la fonctionnalité et le bon fonctionnement de tout.

Alors que le front end concerne l'apparence et le comportement visuel du site web, le back end concerne le bon fonctionnement de tout en coulisses.

Si vous travaillez dans le développement back-end, vous effectuerez des tâches comme la gestion des requêtes vers le serveur et la base de données.

Quelques exemples de travail back-end seraient l'enregistrement des données lorsqu'une personne remplit un formulaire sur la page de contact, ou la récupération de données pour afficher des articles de blog dans une catégorie spécifique que l'utilisateur a demandée.

Le travail back-end peut également impliquer la configuration du site web sur un serveur, la gestion du déploiement et la configuration de bases de données SQL.

Si l'idée de configurer toutes les parties fonctionnelles d'un site web vous semble amusante, vous pourriez aimer le travail back-end !

### Assembler les deux côtés

Les noms front-end et back-end sont apparus parce que le front-end est ce que vous pouvez voir dans votre navigateur.

Et le back-end est la partie que vous ne pouvez pas voir, mais il gère beaucoup de travail lourd et de fonctionnalités qui aident le front-end.

Vous pouvez penser au front-end comme à la vitrine d'une entreprise, la seule partie que la plupart des clients verront. Le back-end est comme les centres de fabrication, de distribution et d'exploitation qui aident le magasin à fonctionner.

Les deux servent des fonctions séparées qui sont tout aussi importantes.

### Front end, back end ou full stack ?

Dans le développement web, vous pouvez vous concentrer uniquement sur le front end, ou uniquement sur le back end. Ou vous pouvez traiter les deux, ce qui est appelé le développement full stack.

Ce que vous choisissez de vous concentrer dépend principalement de deux choses :

* **Votre préférence personnelle** : Tout le monde n'aime pas à la fois le front end et le back end.
  
* **Disponibilité des emplois** : Parcourez les offres d'emploi locales et participez à des rencontres locales de codage pour vous faire une idée des types d'emplois disponibles.
  

Il est intéressant de noter que si vous aimez à la fois le front end et le back end, être un développeur full stack vous rendra plus commercialisable.

Cela a du sens — plus vous pouvez travailler avec de technologies, plus vous pourrez effectuer de tâches.

Stack Overflow a rapporté dans leur [enquête 2017 des utilisateurs](https://insights.stackoverflow.com/survey/2017#developer-profile-specific-developer-types) que 63,7 % s'identifiaient comme full-stack, 24,4 % comme back-end et 11,9 % comme développeurs front-end :

![Image](https://cdn-media-1.freecodecamp.org/images/1*UYtHdEZA9xAiq_ys3Z9ArQ.png align="left")

\_Source : [Enquête Stack Overflow 2017](https://insights.stackoverflow.com/survey/2017#developer-profile-specific-developer-types" rel="noopener" target="*blank" title=")*

Cependant, cela dépendra encore beaucoup de l'entreprise. Certaines entreprises peuvent utiliser des développeurs full stack, tandis que d'autres séparent le back end et le front end.

Certaines font également en sorte que leurs développeurs front-end empiètent sur le design, où les développeurs concevront et construiront le front-end de l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y3XK4wTNDRfVtdBhVD0nlw.png align="left")

### Partie 2 : Faire briller vos compétences front-end

Une fois que vous avez maîtrisé les bases du HTML, du CSS et du JavaScript, vous pouvez commencer à acquérir des compétences plus avancées en front-end.

Cette section abordera les pratiques et outils qui vous aideront à développer des compétences plus commercialisables en tant que développeur web.

### Le design responsive est un must dans ce monde mobile

Lorsque les sites web sont apparus pour la première fois, il n'y avait qu'une seule façon de les visualiser : sur votre ordinateur.

Les smartphones et les données mobiles n'existaient pas vraiment encore. En créant un site web, vous n'aviez à vous soucier que de son apparence sur votre ordinateur.

Maintenant, selon [Statcounter.com](http://gs.statcounter.com/press/mobile-and-tablet-internet-usage-exceeds-desktop-for-first-time-worldwide), plus de personnes utilisent leurs téléphones que leurs ordinateurs de bureau pour naviguer sur Internet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LJTR6eQvxIwaQZj4yN4MDQ.png align="left")

Nous devons donc nous assurer que tous nos sites web fonctionnent et ont une belle apparence sur tout, du plus grand moniteur au plus petit téléphone.

Cette pratique est ce qu'on appelle le **design responsive**. Il est appelé ainsi parce que le design peut "répondre" à n'importe quel appareil qui le visualise.

Vous pouvez tester la réactivité d'un site web en modifiant manuellement la largeur de votre fenêtre de navigateur et en voyant comment le design apparaît aux largeurs grandes et petites.

La construction d'un site web vraiment responsive implique beaucoup de planification dans la phase de design pour considérer comment tout apparaîtra sur tous les appareils. Et dans la phase de développement web, cela implique l'utilisation de requêtes média pour contrôler quelles propriétés CSS sont utilisées à des largeurs spécifiques.

### Les frameworks peuvent vous aider à construire un site web responsive rapidement

Comme vous pouvez l'imaginer, coder tout le CSS d'un site web responsive prend beaucoup de travail.

Si vous ne pouvez pas vous permettre beaucoup de temps supplémentaire, vous pourriez essayer d'utiliser un framework responsive comme [Bootstrap](https://getbootstrap.com/) ou [Zurb Foundation](https://foundation.zurb.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*q2QUM3sANJz1ez4o0-SVew.png align="left")

\_Exemple de page que vous pouvez créer avec [Bootstrap](https://getbootstrap.com/docs/4.0/examples/" rel="noopener" target="*blank" title=")*

La beauté de ces frameworks est qu'ils sont pré-emballés avec du CSS et du JavaScript personnalisés. Ils ont fait beaucoup de travail pour vous en pré-stylisant des éléments comme les titres et les boutons.

Ils viennent également avec des composants JavaScript (essentiellement de petits plugins) comme des fenêtres pop-up modales et des barres de navigation.

Puisque vous utilisez quelque chose qui a déjà été testé, cela rendra la construction de votre site web beaucoup plus facile. Le seul bémol est que vous ne devriez pas devenir trop dépendant des frameworks.

**Rien ne remplace le fait de savoir construire un site web responsive à partir de zéro.**

**Pour aller plus loin**

* [Exemples de design responsive de Designmodo.com](https://designmodo.com/responsive-design-examples/)
  
* [Les bases du design web responsive de Google](https://developers.google.com/web/fundamentals/design-and-ux/responsive/)
  
* [Tutoriel Bootstrap 4 de W3Schools](https://www.w3schools.com/bootstrap4/bootstrap_get_started.asp)
  
* [Tutoriels Zurb Foundation](https://foundation.zurb.com/learn/tutorials.html)
  

### Sass vous fera gagner du temps et des maux de tête lors de l'écriture de CSS

Une fois que vous avez maîtrisé les bases de CSS, je commencerais à apprendre [Sass](http://sass-lang.com/), car il est tout simplement génial.

C'est même dans le nom ! Sass signifie "Syntactically Awesome Style Sheets". Et il est décrit sur son site web comme ["une extension de CSS"](http://sass-lang.com/documentation/file.SASS_REFERENCE.html).

**Il rend l'écriture de vos styles CSS beaucoup plus facile, plus intuitive et plus rapide.**

Ne vous méprenez pas, CSS est génial. Mais à mesure que vous vous y plongez, vous réaliserez que le CSS vanilla régulier peut devenir assez fastidieux. Et, si vous n'êtes pas super organisé dans la façon dont vous écrivez vos styles, vos styles CSS peuvent rapidement devenir frustrants et emmêlés.

**Ce que Sass fait, c'est vous donner plus de puissance et de contrôle.**

Voici quelques exemples de la façon dont Sass facilitera votre vie :

* **Mixins** : Au lieu de copier et coller le code CSS pour certains éléments un million de fois, vous pouvez utiliser des mixins. Ils vous permettent d'écrire un ensemble de styles pour un élément une seule fois, et de les réutiliser autant de fois que vous le souhaitez.
  
* **Nesting** : Au lieu d'écrire toutes les classes parent d'un style spécifique, vous pouvez imbriquer tous les enfants à l'intérieur des styles du parent. Cela réduit également beaucoup de travail en double.
  

![Image](https://cdn-media-1.freecodecamp.org/images/1*QeU_j0ZkguS_Sqyzc5hJcg.png align="left")

*Voici un exemple d'utilisation de l'imbrication dans Sass.*

En bref, l'utilisation de Sass vous fera gagner du temps et des tracas. Cela vaut bien l'effort qu'il faut pour l'apprendre !

**Pour aller plus loin**

* [Commencer avec Sass](http://thesassway.com/beginner/getting-started-with-sass-and-compass)
  
* [Les bases de Sass](http://sass-lang.com/guide)
  

Une note : comme le navigateur ne peut pas lire les fichiers Sass lui-même, vous devez compiler vos fichiers Sass en CSS.

Pour ce faire, vous devrez utiliser quelque chose appelé un outil de build et l'exécuter sur votre ordinateur.

Ce qui nous amène à la section suivante...

### À quoi servent tous ces outils de build, de toute façon ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*f5D9s0KsC4sIauxLEz9oUg.png align="left")

Vous avez probablement entendu un ou plusieurs des termes suivants : npm, Webpack, Grunt, Gulp, Bower, Yarn... la liste est assez longue !

Ces outils sont souvent décrits comme des outils de build, des exécuteurs de tâches, des gestionnaires de tâches, ou *"Maintenant, que dois-je installer ?!"*

### Certains outils font votre travail ingrat (jeu de mots intentionnel !) pour vous

Les outils de build comme [Grunt](https://gruntjs.com/), [Gulp](https://gulpjs.com/), et [Webpack](https://webpack.js.org/) sont couramment utilisés pour effectuer certaines des tâches suivantes :

* **Traitement** des fichiers Sass en CSS
  
* **Concaténation** (combinaison) de plusieurs fichiers CSS ou de plusieurs fichiers JavaScript en un seul grand fichier CSS ou JavaScript.
  
* **Minification** (compression) des fichiers CSS, JavaScript, et même des fichiers image
  
* **Actualisation automatique** de votre navigateur avec le code CSS ou JavaScript mis à jour
  

Bien sûr, beaucoup de ces tâches, vous pourriez les faire vous-même à la main.

Mais devoir le faire encore et encore chaque fois que vous apportez une petite modification CSS ou JavaScript devient fatigant.

### Quel outil de build devriez-vous utiliser ?

En ce moment, Webpack domine le domaine, mais Grunt et Gulp sont encore utilisés.

Je recommanderais définitivement d'apprendre Webpack, mais cela ne ferait pas de mal d'apprendre soit Grunt soit Gulp (Gulp est plus rapide et semble un peu plus facile à démarrer).

### D'autres outils installent des packages (plugins) pour vous

![Image](https://cdn-media-1.freecodecamp.org/images/1*g_5-PNq-uB6f1ooeD-7gNA.png align="left")

De plus, afin d'accomplir toutes ces tâches, vous devez généralement télécharger et installer des plugins ou des packages.

C'est là qu'un outil comme [npm](https://www.npmjs.com/) (Node Package Manager), [Bower](https://bower.io/), ou [Yarn](https://yarnpkg.com/en/) devient utile. Ces outils vous permettent d'installer rapidement des packages sur votre ordinateur en tapant des commandes dans la ligne de commande de votre ordinateur.

Ce sont des outils pour obtenir plus d'outils, en gros !

Comme **npm** est le gestionnaire de packages dominant en ce moment, vous devriez définitivement apprendre à l'utiliser.

**Bower** était l'un des premiers outils de gestion de packages, mais il est officiellement obsolète — les créateurs de Bower.io recommandent maintenant d'utiliser Yarn.

**Yarn** est un outil très similaire à npm créé par Google, Facebook et d'autres qui [promet de corriger](https://scotch.io/tutorials/yarn-package-manager-an-improvement-over-npm) certains des problèmes que npm a.

Bien que Yarn soit minoritaire, je recommanderais quand même de le vérifier, car il semble gagner en popularité.

**Pour aller plus loin**

* [Comment configurer Webpack +2.0 à partir de zéro](https://codeburst.io/easy-guide-for-webpack-2-0-from-scratch-fe508a3ce44e)
  
* [Outillage JavaScript — L'évolution et l'avenir de JS et des outils de build front-end](https://blog.qmo.io/javascript-tooling-the-evolution-and-future-of-js-front-end-build-tools/)
  
* [Feuille de triche NPM vs Yarn](https://shift.infinite.red/npm-vs-yarn-cheat-sheet-8755b092e5cc)
  

### Tout le monde aime les frameworks JavaScript

Vous avez probablement remarqué beaucoup de frameworks, bibliothèques, boîtes à outils JavaScript, etc., qui sont lancés... vous savez, ces noms qui se terminent tous par ".JS ?"

Commençons par faire un pas en arrière et définir ce qu'est un framework JavaScript.

Selon à qui vous parlez, les termes framework, bibliothèque et/ou boîte à outils peuvent ou non être interchangeables. ([C'est encore en débat.](https://stackoverflow.com/questions/148747/what-is-the-difference-between-a-framework-and-a-library))

Mais ils sont tous essentiellement des outils qui, surprise, surprise, font une partie du travail pour vous.

#### Un framework est une structure pré-construite sur laquelle vous construisez.

En général, un framework est un système de pièces fonctionnelles créé par quelqu'un d'autre.

Pour utiliser le framework, vous l'installez dans vos propres fichiers de site web. Ensuite, vous travaillez à partir de cette structure existante, en ajoutant ce que vous voulez accomplir.

Utiliser un framework, c'est comme acheter une maison à l'ossature nue qui vient avec tous les composants structurels (fondation, cadre, toit), mais qui n'est pas totalement complète.

Vous devez encore aller à l'intérieur et attacher l'eau et l'électricité, ainsi qu'installer des armoires, peindre les murs et décorer.

Quelques exemples de frameworks front-end JavaScript sont [React](https://reactjs.org/), [Vue](https://vuejs.org/), et [Angular](https://angular.io/).

#### Une bibliothèque est un ensemble d'outils pré-faits que vous ajoutez à votre propre structure.

En comparaison, une bibliothèque est une collection de composants individuels que vous pouvez prendre et brancher dans votre propre système.

> **C'est la principale différence entre les frameworks et les bibliothèques :**

> Alors que les frameworks sont des structures pré-faites, les bibliothèques ne sont pas une structure en elles-mêmes. Elles fournissent une fonctionnalité supplémentaire pour les systèmes existants.

Pour continuer l'analogie de la construction de maison, vous pouvez penser aux bibliothèques comme des appareils que vous choisissez d'ajouter à votre maison.

Des machines comme les fours, les douches et les climatiseurs remplissent toutes une fonction distincte, mais vous devez les installer dans une maison existante pour qu'elles soient utiles.

Un exemple de bibliothèque, en utilisant la catégorisation ci-dessus, est jQuery.

[jQuery](http://jquery.com/) est une bibliothèque JavaScript qui n'a aucun type de structure en elle-même, mais qui a plus de [300 fonctions différentes](http://api.jquery.com/) que vous pouvez utiliser.

**Encore une fois, ces définitions ne sont pas acceptées par tout le monde.**

React et jQuery se catégorisent eux-mêmes comme des bibliothèques, et Angular et Vue s'appellent des frameworks.

Cependant, pour ma propre compréhension personnelle, il est utile de séparer les outils en ces deux catégories générales de frameworks (systèmes) et de bibliothèques (outils).

Ce qui nous amène à notre prochain point...

### Les trois grands frameworks JavaScript : Angular, React et Vue

![Image](https://cdn-media-1.freecodecamp.org/images/1*8lqOL3IOvK879eu64unZCA.png align="left")

Au début des années 2010, il y a eu une explosion de frameworks se terminant par ".js", presque un nouveau chaque mois.

Cependant, alors que nous approchons de 2020, le champ s'est éclairci et il nous reste les trois grands gagnants : Angular, React et Vue.

**Les frameworks JavaScript ont peut-être commencé comme une tendance, mais ils sont définitivement là pour rester.**

Angular, React et Vue sont tous en croissance, et JavaScript lui-même est extrêmement populaire en ce moment — [c'est la technologie la plus utilisée](https://insights.stackoverflow.com/survey/2017#most-popular-technologies) pour la cinquième année consécutive dans l'enquête annuelle de Stack Overflow.

De plus, Stack Overflow publie des tendances de technologies basées sur le nombre de questions posées par mois.

Vous pouvez voir qu'Angular a le plus grand volume, et que Angular et React ont connu une croissance assez forte au cours de l'année dernière.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z2fsSGzW1zz8BZwaku8CCg.png align="left")

\_Source : Stack Overflow — [Tendances des frameworks JavaScript](https://insights.stackoverflow.com/trends?utm\_source=so-owned&utm\_medium=blog&utm\_campaign=trends&utm\_content=blog-link&tags=angularjs%2Cangular%2Creactjs%2Cvue.js" rel="noopener" target="*blank" title=")*

[L'enquête The State of JavaScript](https://stateofjs.com/2017/front-end/results) montre que React est en tête du nombre de développeurs qui l'ont utilisé et aimé, tandis qu'Angular ne semble pas être aussi intéressant ou suscite autant de désir de réutilisation.

Vue a un taux d'utilisation réel plus faible, mais est en tête du peloton en termes de technologie que les développeurs veulent essayer à l'avenir. Il est donc envisageable que Vue devienne un acteur plus important dans les prochaines années.

Cependant, je pense que les trois sont là pour rester, au moins pour les prochaines années.

### TL,DR : Quel framework devrais-je apprendre maintenant ?

Cela dépend — si vous cherchez à décrocher un emploi de développeur web à temps plein, je vous recommande de parcourir les offres d'emploi locales pour voir quel framework semble être le plus mentionné.

Si vous apprenez simplement pour le moment sans cet objectif spécifique en tête, Vue est un bon point de départ pour les débutants. Il est léger et bien documenté.

Cependant, je ne recommanderais pas personnellement d'apprendre uniquement Vue. Il serait bon d'ajouter éventuellement React ou Angular à votre boîte à outils, selon vos préférences.

**Pour aller plus loin**

* [Meilleurs frameworks, bibliothèques et outils JavaScript à utiliser en 2017](https://www.sitepoint.com/top-javascript-frameworks-libraries-tools-use/)
  
* [Le guide du débutant pour choisir un framework JavaScript](https://webdesign.tutsplus.com/tutorials/the-noobs-guide-to-choosing-a-javascript-framework--cms-28538)
  

![Image](https://cdn-media-1.freecodecamp.org/images/1*QXYhx3P_IUMHLyZQniVbVA.png align="left")

### Partie 3 : Plongeons dans le back-end

#### Quel langage devriez-vous apprendre en premier ?

Il existe une multitude de langages back-end. Beaucoup d'entre eux existent depuis un certain temps, certains même avant l'existence d'Internet !

Cela peut rendre difficile le choix du langage avec lequel commencer. Pour réduire vos choix, je recommande d'appliquer les principes suivants à votre décision :

* Choisissez un langage qui est **apprenable** : il a une courbe d'apprentissage raisonnable, est bien documenté et/ou dispose d'un bon système de support en ligne.
  
* Choisissez un langage qui est **pertinent** pour vos objectifs de carrière éventuels.
  
* Choisissez un langage qui est **agréable**. Apprendre le développement web est suffisamment difficile — il n'y a aucun intérêt à vous forcer à apprendre un langage que vous n'aimez vraiment pas.
  

> **Une chose importante à garder à l'esprit est que vous n'avez pas à apprendre tous les langages.**

> En fait, si vous êtes débutant, je vous recommande fortement de vous concentrer sur un langage d'abord.

**Tous les langages de programmation partagent certains principes communs.**

Par exemple, vous pouvez écrire une boucle "for" en JavaScript, PHP, C# et Python.

Une fois que vous avez acquis les principes fondamentaux de la programmation dans votre premier langage, il sera plus facile de transférer ces concepts dans d'autres langages.

J'espère que cela enlève un peu de pression pour choisir votre premier langage back-end à apprendre ?

### Examinons certains des langages back-end les plus populaires.

**Java**

[Java](https://www.oracle.com/java/index.html) est un langage stable qui est très largement utilisé et existe depuis longtemps. Il occupe la première place de l'[index TIOBE](https://www.tiobe.com/tiobe-index/) depuis 2001. (TIOBE est un classement des langages de programmation par nombre de recherches.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*HqJzc1ZlB4pBPQgBfXPYWg.png align="left")

\_Source : [Stackify.com](https://twitter.com/benjaminputano" rel="noopener" target="\_blank" title=""&gt;Ben Putano sur &lt;a href="https://stackify.com/popular-programming-languages-2018/" rel="noopener" target="*blank" title=")*

De plus, Java s'est classé troisième dans les classements de Stack Overflow des [langages les plus couramment utilisés](https://insights.stackoverflow.com/survey/2017#technology-programming-languages) et a le deuxième plus grand nombre de [questions taguées](https://stackoverflow.com/tags) sur Stack Overflow.

![Image](https://cdn-media-1.freecodecamp.org/images/1*68BlQUD0zRq2YGf__-O2Vg.png align="left")

\_Source : [Langages de programmation les plus courants](https://insights.stackoverflow.com/survey/2017#technology-programming-languages" rel="noopener" target="*blank" title="), Enquête auprès des développeurs Stack Overflow 2017*

De nombreuses grandes entreprises technologiques [utilisent Java](https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites) dans leurs sites web : Google, YouTube, Facebook, Amazon et Twitter, entre autres.

Une raison à cela est que Java est rapide et peut être mis à l'échelle pour gérer de grands sites web. C'est également un langage cohérent qui permet une maintenance plus facile pour les [projets à long terme](https://www.upwork.com/hiring/development/the-java-platform/).

Twitter a été initialement construit avec Ruby on Rails. Mais en 2015, ils avaient besoin de pouvoir supporter leur énorme croissance, alors ils [sont passés à Scala](https://www.quora.com/Why-did-Twitter-switch-to-a-Java-based-front-end-after-successfully-using-Ruby-on-Rails-with-200-million-users), un langage qui s'exécute sur la machine virtuelle Java.

**C# (C Sharp)**

[C#](https://docs.microsoft.com/en-us/dotnet/csharp/getting-started/introduction-to-the-csharp-language-and-the-net-framework) a été créé par Microsoft pour être un concurrent de Java. Vous pouvez voir que C# a atteint son pic sur les tendances de Stack Overflow en 2009 et est en déclin depuis.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ddhjNfjMedPiY8QK_6Z6Cw.png align="left")

\_Source : Stack Overflow [tendances pour les langages back-end](https://insights.stackoverflow.com/trends?utm\_source=so-owned&utm\_medium=blog&utm\_campaign=trends&utm\_content=blog-link&tags=java%2Cpython%2Cc%23%2Cjavascript%2Cphp%2Cruby%2Cc%2B%2B%2Cnode.js" rel="noopener" target="*blank" title=")*

Mais je ne compterais pas encore C#.

C'est un langage puissant, orienté objet, qui a le troisième plus grand nombre de [tags Stack Overflow](https://stackoverflow.com/tags). Il s'est également classé troisième dans les [recherches](https://stackify.com/popular-programming-languages-2018/) de Stackify sur les langages les plus demandés dans les offres d'emploi Indeed en décembre 2017.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uop6ItxTX3wFkTQnuFZOvA.png align="left")

\_Source : [Stackify.com](https://twitter.com/benjaminputano" rel="noopener" target="\_blank" title=""&gt;Ben Putano sur &lt;a href="https://stackify.com/popular-programming-languages-2018/" rel="noopener" target="*blank" title=")*

C# est utilisé dans une grande variété d'applications, telles que les applications de bureau Windows et la programmation Android.

Il est également beaucoup utilisé dans le développement de jeux, via le [moteur de jeu Unity](https://www.quora.com/What-is-unity-game-engine/answer/Harshal-B-Kolambe). Donc, si vous êtes intéressé par le développement Android ou de jeux, C# serait une excellente option à apprendre.

**Node.js**

Comme mentionné précédemment, JavaScript a été le langage le plus couramment utilisé rapporté par les utilisateurs de Stack Overflow au cours des cinq dernières années.

Une grande partie de cela est due à [Node.js](https://nodejs.org/en/), qui a occupé la première place de leur [liste](https://insights.stackoverflow.com/survey/2017#technology-frameworks-libraries-and-other-technologies) des frameworks et bibliothèques les plus utilisés en 2017.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VOHEKe0YQunX-g6USjpMVg.png align="left")

\_Source : [Frameworks et bibliothèques les plus courants](https://insights.stackoverflow.com/survey/2017#technology-frameworks-libraries-and-other-technologies" rel="noopener" target="*blank" title="), Enquête auprès des développeurs Stack Overflow 2017*

Node.js, décrit comme un "runtime JavaScript", est essentiellement du JavaScript qui s'exécute sur le back-end.

Il était à l'origine destiné à servir d'alternative plus efficace au serveur HTTP Apache. Depuis sa sortie en 2009, Node.js a régulièrement augmenté en utilisation, grâce à sa nature rapide et légère.

Les développeurs Node utilisent souvent le framework [Express](https://expressjs.com/) lors de la construction d'applications web. Express.js est un "framework web minimaliste" pour Node.js.

En utilisant Node et Express sur le back-end, et Angular ou React sur le front-end, cela signifie que vous pouvez être un développeur full stack JavaScript.

Cette stack, ou combinaison de technologies, est très populaire en ce moment, [surtout avec les startups](https://codingvc.com/which-technologies-do-startups-use-an-exploration-of-angellist-data).

**Python**

[Python](https://www.python.org/) est apparu pour la première fois en 1991 et est souvent le "premier langage" pour de nombreux étudiants en programmation.

Grâce à sa [lisibilité](https://en.wikipedia.org/wiki/Python_\(programming_language\)) et à l'utilisation de mots-clés en anglais, il est généralement considéré comme un langage facile à apprendre.

Il existe quelques frameworks Python que vous pouvez utiliser :

* [Django](https://www.djangoproject.com/) (fonctionnalités pré-construites, plus de clochettes et de sifflets), et
  
* [Flask](http://flask.pocoo.org/) (plus minimaliste et flexible).
  

La popularité de Python a explosé ces dernières années. À l'heure où j'écris ces lignes, il est [classé n°4](https://www.tiobe.com/tiobe-index/) sur l'index TIOBE.

Et en 2017, il a été classé deuxième en nombre de pull requests sur GitHub, selon leur [rapport 2017 Year in Review](https://octoverse.github.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*FK5xi-zleQCUafgucPamlw.png align="left")

\_Source : [Stackify.com](https://twitter.com/benjaminputano" rel="noopener" target="\_blank" title=""&gt;Ben Putano sur &lt;a href="https://stackify.com/popular-programming-languages-2018/" rel="noopener" target="*blank" title=")*

Stack Overflow a [rapporté](https://stackoverflow.blog/2017/09/14/python-growing-quickly/) en septembre dernier que la science des données, l'apprentissage automatique et la recherche académique sont largement responsables de cette croissance rapide.

Même si vous n'êtes pas un scientifique des données, être capable de travailler avec et de manipuler des données devient une compétence utile.

Comme l'écrit Alexus Strong de Code Academy :

> "Python est attrayant pour ceux d'entre nous dans des domaines non techniques car il met l'analyse de données [...] à portée de main."

Si vous êtes curieux de la science des données ou de l'apprentissage automatique, Python pourrait être un très bon choix pour vous, car ces domaines devraient probablement s'étendre dans les années à venir.

**Ruby**

[Ruby](https://en.wikipedia.org/wiki/Ruby_\(programming_language\)) a été publié pour la première fois en 1995. Il a commencé à attirer beaucoup d'attention au début des années 2000 lorsque la startup [Basecamp](https://basecamp.com/about) a inventé le framework [Ruby on Rails](http://rubyonrails.org/).

Combiné avec la syntaxe conviviale pour les débutants et la lisibilité de Ruby, Rails a rendu la construction d'applications web très rapide et facile.

Ruby on Rails a gagné en popularité et est devenu le framework de choix pour les startups. (Codepen.io, GitHub et [Shopify](https://basecamp.com/about) [utilisent tous](https://w3techs.com/technologies/details/pl-ruby/all/all) Ruby on Rails.)

Cependant, Ruby n'a jamais été l'un des grands acteurs. L'année dernière, il s'est classé à la dixième place à la fois dans les classements des langages les plus couramment utilisés de Stack Overflow et dans l'[index TIOBE](https://www.tiobe.com/tiobe-index/).

De plus, Ruby on Rails ne s'adapte pas très bien, ce qui a conduit ces startups à finalement passer à d'autres langages lorsqu'elles deviennent vraiment grandes (comme Twitter passant à Java, comme nous l'avons mentionné ci-dessus).

Il ne domine peut-être pas les classements, mais Ruby pourrait encore être un bon choix pour votre premier langage à apprendre.

Si vous êtes intéressé par le monde des startups ou si votre région géographique compte de nombreux emplois Ruby, je vous recommande d'apprendre Ruby et Ruby on Rails.

**PHP**

[PHP](http://php.net/manual/en/intro-whatis.php) est un langage que beaucoup de gens aiment détester.

Cependant, malgré le nombre de questions Quora [demandant si PHP est mort](https://www.quora.com/Is-PHP-dead-What-is-the-job-outlook-and-future-of-PHP-in-the-next-five-years), le fait reste que PHP est le langage back-end le plus largement utilisé aujourd'hui.

Les recherches effectuées par [W3Techs.com](https://w3techs.com/technologies/overview/programming_language/all) montrent que 83 % de tous les sites web utilisent PHP. (Le langage suivant, ASP.NET, ne représente que 14 %.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wsn6WoqlDCLANKqny2TzIw.png align="left")

\_Source : [W3Techs.com](https://w3techs.com/technologies/overview/programming\_language/all" rel="noopener" target="*blank" title=")*

Les systèmes de gestion de contenu (CMS) sont une raison majeure de la grande part de marché de PHP. Les [trois principaux CMS](https://w3techs.com/technologies/overview/content_management/all) — WordPress, Joomla et Drupal — sont tous construits avec PHP.

WordPress lui-même détient la part du lion du marché des CMS, représentant [29,5 % de tous les sites web](https://w3techs.com/technologies/overview/content_management/all).

Si vous aimez travailler avec, le développement WordPress peut être un bon domaine de concentration pour personnaliser des sites web et construire des plugins ou des thèmes.

En plus des systèmes de gestion de contenu, PHP dispose de certains frameworks qui rendent le développement plus facile et plus rapide. [Laravel](https://laravel.com/), un framework sorti en 2011, est actuellement le plus populaire.

**Pour aller plus loin**

* [Un guide du débutant pour le développement back-end (Upwork.com)](https://www.upwork.com/hiring/development/a-beginners-guide-to-back-end-development/)
  
* [Frameworks web côté serveur (Mozilla Developer Network)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Web_frameworks)
  
* [Quel est le meilleur langage de programmation pour moi ?](http://www.bestprogramminglanguagefor.me/)
  

### Travailler avec les données et les bases de données

![Image](https://cdn-media-1.freecodecamp.org/images/0*tMc9X0KyVDJNRf2Q.gif align="left")

\_Source : [Sherchle](https://giphy.com/gifs/art-design-illustration-l0HlN5Y28D9MzzcRy" rel="noopener" target="*blank" title=") via GIPHY*

Les bases de données peuvent sembler intimidantes si vous n'êtes pas familier avec elles.

Cependant, si vous y réfléchissez, vous avez probablement travaillé avec des données et les avez utilisées dans votre propre vie à un moment donné.

Si vous avez déjà utilisé Excel pour organiser des données, ou créé un graphique pour suivre vos objectifs, alors vous avez fait une fonction similaire (bien que beaucoup plus simple) à celle des bases de données.

### Que dois-je apprendre pour utiliser les bases de données ?

Heureusement, vous n'avez pas besoin d'apprendre une tonne de langages différents. Le principal langage de base de données est [SQL](https://en.wikipedia.org/wiki/SQL) (prononcé *sequel*).

SQL (Structured Query Language) a été [créé](https://www.thebalance.com/what-is-sql-and-uses-2071909) dans les années 1970 par IBM, et est utilisé dans les [bases de données relationnelles](https://en.wikipedia.org/wiki/Relational_database).

Le modèle relationnel est une façon de structurer les données en lignes et colonnes (pensez à une feuille de calcul Excel).

Chaque colonne est désignée pour un certain type de données, et elle peut exiger que les données soient formatées correctement. Et chaque ligne, ou enregistrement, contient un identifiant ou une clé unique en plus des valeurs de colonne, ou de champ.

Vous pouvez voir cela ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*axy8IyyF8aiv3NKDQk5QBw.png align="left")

*Une simple feuille de calcul similaire à la façon dont les données sont stockées dans une table. La colonne Loyer nécessiterait des valeurs numériques.*

Les enregistrements sont ensuite stockés dans plusieurs collections appelées tables. Et une collection de tables (entre autres choses) constitue l'ensemble du schéma de la base de données, ou structure.

Les principaux types de systèmes de bases de données SQL sont :

* [MySQL](https://www.mysql.com/) (utilisé pour PHP et les applications open source)
  
* [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-2017) (généralement utilisé pour les applications .NET)
  
* [PostgreSQL](https://www.postgresql.org/) (open source)
  

**NoSQL**

Même si SQL est le type de base de données dominant, il en existe un autre : NoSQL (c'est-à-dire non-SQL). Comme le nom l'indique, les bases de données NoSQL sont en quelque sorte opposées aux bases de données SQL traditionnelles.

[NoSQL](https://en.wikipedia.org/wiki/NoSQL) n'est pas relationnel et [n'impose pas](https://www.infoworld.com/article/3240644/nosql/what-is-nosql-nosql-databases-explained.html) la même structure que SQL. Au lieu de cela, vous pouvez stocker n'importe quel type de données dans un système plus libre et plus flexible.

Cela crée des processus beaucoup plus rapides et est beaucoup mieux pour évoluer vers des applications grandes et complexes. L'inconvénient est que vous sacrifiez la cohérence des données.

Comme l'écrit Craig Buckler de Sitepoint :

> NoSQL est plus flexible et indulgent, mais pouvoir stocker n'importe quelle donnée n'importe où peut entraîner des problèmes de cohérence.

NoSQL a gagné en popularité dans les années 2000 en raison des grandes entreprises technologiques comme Facebook et Amazon ayant besoin d'une manière rapide de manipuler et de stocker des données.

[MongoDB](https://www.mongodb.com/) est le système NoSQL le plus couramment utilisé. Les autres principaux types sont Cassandra, Elasticsearch et Couchbase, selon [Hackernoon](https://hackernoon.com/top-4-nosql-databases-infographic-b6acc389befc).

**SQL vs NoSQL ?**

Vous pouvez rencontrer des discussions sur le fait de savoir si NoSQL remplace SQL, ou lequel est le meilleur. La vérité est que les deux types de bases de données ont leurs forces et leurs faiblesses.

Comme pour tout le reste, le bon choix changera en fonction du projet et du travail. Personnellement, je recommande d'apprendre les bases de SQL et de NoSQL.

**Pour aller plus loin**

* [Histoire de SQL](https://www.thebalance.com/what-is-sql-and-uses-2071909) — TheBalance.com
  
* [SQLCourse.com](http://www.sqlcourse.com/intro.html) — tutoriel en ligne gratuit sur SQL
  
* [Différence entre SQL et NoSQL](https://medium.com/xplenty-blog/the-sql-vs-nosql-difference-mysql-vs-mongodb-32c9980e67b2) — XplentyBlog
  
* [NoSQL expliqué](https://www.mongodb.com/nosql-explained) — MongoDB
  

### Créer des sites web sur des serveurs

![Image](https://cdn-media-1.freecodecamp.org/images/0*zZFtoXHQdZd2pZCC.gif align="left")

Comme nous l'avons mentionné au début, les serveurs sont simplement des ordinateurs qui stockent des fichiers de sites web et d'autres ressources comme des bases de données.

Pour qu'un site web soit accessible publiquement sur Internet, il doit être installé sur un serveur.

Voici quelques-unes des choses avec lesquelles vous devrez travailler pour créer un site web en direct :

#### **Nom de domaine et certificat SSL**

Les noms de domaine sont l'adresse du site web, comme Google.com, Wikipedia.org ou Dartmouth.edu.

Pour en obtenir un, vous devrez en choisir un qui est disponible, puis l'acheter auprès d'un registraire de noms de domaine comme [Namecheap.com](https://www.namecheap.com/) ou [Google Domains](https://domains.google/#/).

Ces entreprises enregistrent les domaines auprès de l'[ICANN](https://en.wikipedia.org/wiki/ICANN) (Internet Corporation for Assigned Names and Numbers).

L'ICANN est une organisation centralisée qui supervise et gère le DNS (système de noms de domaine) et les zones IP (protocole Internet) de l'Internet mondial.

En plus du nom de domaine, vous devriez également obtenir un certificat SSL (Secure Sockets Layer) pour votre domaine. SSL [chiffrera le trafic](https://www.digicert.com/ssl/) sur votre site web, ce qui aidera à le protéger contre les cyberattaques.

#### **Espace serveur d'hébergement web**

![Image](https://cdn-media-1.freecodecamp.org/images/1*XgwG8TIIqH_6RHDMiOO6ew.jpeg align="left")

Une fois que vous avez votre nom de domaine pour *AwesomeStupendousAmazingSite.com*, vous devrez acheter de l'espace serveur.

Il existe quelques niveaux différents de plans d'hébergement web :

* **Serveurs partagés** : L'option la moins chère, peut varier de quelques dollars à 12–20 $ par mois. Comme son nom l'indique, vous partagez votre espace serveur avec d'autres sites web "voisins". L'avantage est l'abordabilité, et l'inconvénient est des vitesses plus lentes et un possible temps d'arrêt si vous dépassez votre utilisation pour le mois. Les hébergeurs populaires sont [SiteGround](https://www.siteground.com/), [Bluehost](https://www.bluehost.com/), et [WP Engine](https://wpengine.com/).
  
* **Serveurs cloud** : [L'hébergement cloud](https://www.interoute.com/what-cloud-hosting) est une option relativement nouvelle. Il consiste en un système d'un grand nombre de serveurs physiques dont les ressources sont toutes partagées. Chaque "locataire" individuel se voit ensuite attribuer un serveur virtuel qui tire des ressources du pool collectif. Cette configuration permet une plus grande flexibilité pour la bande passante et peut être mise à l'échelle très rapidement. Une entreprise, [Digital Ocean](https://www.digitalocean.com/), ne traite que des serveurs cloud. Le prix dépend des spécifications de votre serveur et peut varier de quelques dollars par mois à près de 1000 $.
  
* **VPS (Virtual Private Servers)** : Les VPS sont similaires à l'hébergement cloud en ce sens que chaque locataire a son propre serveur virtuel, et tous les locataires partagent un serveur physique. C'est mieux que l'hébergement partagé car vous avez votre propre part des ressources du serveur. Cette option est un peu plus chère, entre 20 et 60 $ par mois (selon [BlueHost](https://www.bluehost.com/products/vps)).
  
* **Serveurs dédiés** : Ces serveurs vous donnent un serveur physique complet rien que pour vous. Comme vous pouvez l'imaginer, cette option est la plus puissante mais aussi la plus chère. Ils sont souvent également des serveurs gérés, ce qui signifie que l'entreprise effectuera la maintenance et d'autres tâches pour vous. L'hébergement dédié vous coûtera généralement quelques centaines de dollars par mois, selon les prix de SiteGround.
  

#### **Configuration et maintenance du serveur**

Une fois que vous avez votre nom de domaine et votre espace serveur, vous devrez configurer votre site sur le serveur.

Cela implique de diriger votre nom de domaine vers l'adresse IP unique de votre serveur, de configurer vos fichiers de site web et votre base de données (si nécessaire), et d'autres configurations.

La quantité de travail que vous devrez faire dépendra du type de plan serveur que vous avez acheté auprès de votre hébergeur web. Les plans partagés les plus simples viennent souvent avec des fonctionnalités en un clic qui installeront automatiquement WordPress, Drupal ou d'autres sites pour vous.

D'autres serveurs, comme Digital Ocean, sont très minimaux et nécessitent que vous configuriez tout manuellement.

#### **Déploiement de fichiers sur votre serveur**

Vous vous demandez peut-être comment transférer des fichiers de votre propre ordinateur vers votre serveur. Vous pouvez y parvenir en utilisant un [protocole](https://en.wikipedia.org/wiki/Communication_protocol), qui est essentiellement une méthode de transport de fichiers ou d'autres données vers et depuis un serveur.

> **Note de côté :**  
> HTTP, la manière dont votre navigateur charge les sites web, est également un protocole — HTTP signifie Hypertext Transfer Protocol.

La manière la plus simple est d'utiliser un protocole appelé [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol) (File Transfer Protocol). Cependant, il n'est plus recommandé d'utiliser FTP, car il n'est pas sécurisé (chiffré).

De nos jours, la plupart des gens utilisent des protocoles plus sécurisés comme FTPS (FTP sur SSL) ou SFTP (Secure SHell FTP).

Pour faire fonctionner FTP/SFTP, vous devez créer un compte sur votre serveur. Vous vous connecterez ensuite au serveur en utilisant l'adresse IP du serveur, ainsi qu'un nom d'utilisateur et un mot de passe pour l'authentification.

Pour transférer des fichiers via FTP/SFTP, vous pouvez utiliser des programmes comme [Filezilla](https://filezilla-project.org/) ou [CyberDuck](https://cyberduck.io/). Ces programmes disposent d'une interface graphique (GUI) qui facilite le téléchargement et le téléchargement de fichiers entre votre ordinateur et votre serveur.

#### **Outils de déploiement**

![Image](https://cdn-media-1.freecodecamp.org/images/1*1jvILZIbneS98ISyxfynXQ.jpeg align="left")

Comme vous pouvez l'imaginer, devoir télécharger manuellement des fichiers sur votre serveur chaque fois que vous apportez une petite modification de code peut devenir fastidieux. De plus, les choses peuvent devenir confuses si plusieurs personnes travaillent sur le même fichier et téléchargent simultanément.

Heureusement, vous pouvez configurer des déploiements qui se lient à votre dépôt Git.

L'outil de déploiement stocke vos paramètres FTP/SFTP, et lorsque vous poussez une modification dans Git vers votre branche principale, par exemple, l'outil transférera les fichiers pour vous. Ainsi, vous n'avez pas besoin de vous souvenir des fichiers que vous avez modifiés, réduisant le nombre d'erreurs que vous commettez.

Pour les sites web plus complexes qui ont une équipe de plusieurs personnes, il existe des outils et systèmes de déploiement plus avancés que vous pouvez utiliser pour rendre vos déploiements plus structurés.

Ces systèmes dépassent le cadre de cet article, mais ils incluent des pratiques telles que [l'intégration continue](https://aws.amazon.com/devops/continuous-integration/).

**Pour aller plus loin**

* [Processus d'enregistrement de nom de domaine](https://whois.icann.org/en/domain-name-registration-process) — WHOIS
  
* [8 types populaires de services d'hébergement web](https://www.thebalance.com/types-of-web-hosting-services-2532072) — TheBalance.com
  
* [6 meilleurs clients FTP](http://www.wpbeginner.com/showcase/6-best-ftp-clients-for-wordpress-users/) — WP Beginner
  
* [Intégration continue vs livraison continue vs déploiement continu](https://www.atlassian.com/continuous-delivery/ci-vs-ci-vs-cd) — Atlassian
  

### Félicitations !!

![Image](https://cdn-media-1.freecodecamp.org/images/0*hDquyfV9gO45z7Vf.gif align="left")

Vous avez réussi !

Avant de continuer vers la liste des ressources, veuillez noter que la section suivante contient certains liens d'affiliation. Cela signifie que je recevrai une petite commission de la part de l'entreprise si vous achetez via le lien.

C'est une manière facile pour vous de soutenir l'écriture de ce type d'articles, sans frais supplémentaires pour vous. (J'ai également inclus des liens non affiliés, si vous préférez les utiliser.)

### Épilogue : Ressources d'apprentissage recommandées

Comme je suis sûre que vous le savez, il existe une multitude de ressources que vous pouvez utiliser pour apprendre à coder.

J'ai inclus ici certaines des ressources en ligne, des livres et autres ressources les plus populaires et recommandés.

### Cours complets de développement web

Il existe quelques cours en ligne qui couvrent tous ou presque tous les domaines du développement web.

Si vous ne voulez pas sauter d'un endroit à l'autre et que vous voulez simplement vous concentrer sur un seul endroit pour tout apprendre, je recommande l'un ou plusieurs des éléments suivants :

![Image](https://cdn-media-1.freecodecamp.org/images/1*YPpb4B_k1FehpeRNxDApzw.png align="left")

[**freeCodeCamp**](https://www.freecodecamp.org/) est une organisation à but non lucratif qui offre une éducation complètement gratuite pour les développeurs web en herbe.

Leur programme est un ensemble complet de cours allant du front au back end (en utilisant Node et Express) et plus encore !

Beaucoup de gens ont obtenu des emplois à temps plein après avoir suivi freeCodeCamp. Vous pouvez également contribuer à des [projets open source](https://www.freecodecamp.org/nonprofits/) via GitHub.

L'un des principaux avantages de freeCodeCamp est qu'il est très centré sur la communauté, avec des forums et des groupes Facebook, afin que vous puissiez obtenir beaucoup de soutien pendant que vous apprenez.

Vous pouvez lire quelques avis sur freeCodeCamp sur [Quora](https://www.quora.com/How-did-Free-Code-Camp-change-your-life) et [Reddit](https://www.reddit.com/r/learnprogramming/comments/4cen3v/a_review_of_freecodecamp_the_first_25_hours_from/).

![Image](https://cdn-media-1.freecodecamp.org/images/0*4nEbzCm3SWCGX_jJ.png align="left")

**Le Bootcamp de Développeur Web de Colt Steele** *(*[*lien d'affiliation*](https://www.udemy.com/the-web-developer-bootcamp/?siteID=T4jMTDexBoM-4eq5n6HlbL7PAfBCL8SWqw&LSNPUBID=T4jMTDexBoM) */* [*lien non affilié*](https://www.udemy.com/the-web-developer-bootcamp/)*)*

Colt est un ancien instructeur de bootcamp de codage qui voulait offrir un bootcamp complet pour une fraction du prix.

Il a fini par créer l'un des cours de développeur web les plus populaires et les mieux notés sur Udemy, et pour de bonnes raisons.

Son cours vous emmène des bases au développement full-stack (en utilisant Node et Express comme back-end), avec beaucoup de contenu et est mis à jour fréquemment.

Vous pouvez lire les [avis](https://www.udemy.com/the-web-developer-bootcamp/#reviews) de son cours sur la page Udemy, ainsi que sur un [post du forum](https://forum.freecodecamp.org/t/the-web-developer-bootcamp-udemy-review/61595/4) de freeCodeCamp.

![Image](https://cdn-media-1.freecodecamp.org/images/0*8mRX8qP022AC1ygz.png align="left")

**Udacity** propose à la fois des [cours gratuits](https://www.udacity.com/courses/web-development) et des programmes payants appelés [Nanodegrees](https://www.udacity.com/nanodegree).

Les Nanodegrees s'appuient sur les cours gratuits — ce sont des programmes intensifs (12 heures/semaine) où vous construisez des projets de portfolio et avez plus d'interaction et de soutien communautaire.

Ils ne sont pas bon marché, actuellement 199 $/mois et il peut vous falloir entre 6 à 10 heures pour en compléter un.

Si vous êtes intéressé, voici quelques avis sur les programmes Nanodegree d'Udacity sur [Quora](https://www.quora.com/Are-Udacity-Nanodegrees-worth-it-for-finding-a-job) et [Hacker News](https://news.ycombinator.com/item?id=9313088), et des [réponses Quora](https://www.quora.com/What-is-the-difference-between-a-Udacity-nanodegree-degree-program-and-free-courses) sur la différence entre les cours gratuits d'Udacity et les Nanodegrees.

### Autres ressources

![Image](https://cdn-media-1.freecodecamp.org/images/0*4v3jYDpiexq_tDvo.png align="left")

[**Team Treehouse**](https://teamtreehouse.com/tracks) est un site web très populaire pour apprendre le codage. Ils n'ont pas de contenu gratuit, mais ils utilisent un modèle d'abonnement.

Treehouse propose des plans mensuels échelonnés (25 $ ou 55 $/mois actuellement) et vous pouvez suivre des cours illimités.

Vous pouvez même mettre en pause votre abonnement si vous souhaitez faire une pause de quelques mois, et le reprendre plus tard lorsque vous serez prêt.

En plus des cours individuels, ils proposent également des parcours structurés comme le développement web Java ou le développement web front-end qui vous guident à travers une série de cours sélectionnés.

![Image](https://cdn-media-1.freecodecamp.org/images/0*eEoOMNC5kTo9Eoas.png align="left")

**Udemy** *(*[*lien d'affiliation*](https://www.udemy.com/courses/development/web-development/?siteID=T4jMTDexBoM-BdAzoxv_nMbWPIUjULEsSg&LSNPUBID=T4jMTDexBoM) */* [*lien non affilié*](https://www.udemy.com/courses/development/web-development)*)*

Udemy est l'une des plus grandes plateformes d'apprentissage en ligne et propose des cours non seulement en codage, mais aussi dans d'autres domaines professionnels et de loisirs.

Vous payez pour chaque cours individuellement, et ils ont des ventes fréquentes où les cours coûtent entre 10 et 20 $ chacun.

Bien sûr, en raison du grand nombre de cours et d'instructeurs, ils varient en qualité, donc vous devriez faire des recherches avant d'acheter.

Je recommande de vérifier les notes et les avis à la fois sur la page du cours Udemy et ailleurs en ligne.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ExV7N_TGY8rzoH5B.png align="left")

[**Wes Bos**](http://wesbos.com/courses/) est un instructeur en développement web qui a créé plusieurs cours très populaires.

Un cours que je recommande définitivement est **JavaScript30** *(*[*lien d'affiliation*](https://javascript30.com/friend/CODERCODER) */* [*lien non affilié*](https://javascript30.com/)*)*. Il s'agit de son défi de codage JavaScript vanilla (c'est-à-dire sans frameworks ni bibliothèques) gratuit de 30 jours.

Il propose également des cours premium sur React, Node et JavaScript plus avancé sur son site web.

Si vous êtes curieux, voici quelques avis sur ses cours sur [Reddit](https://www.reddit.com/r/webdev/comments/69yd1g/wes_bos_learn_node_course_officially_launched/) et le [forum freeCodeCamp](https://forum.freecodecamp.org/t/want-to-learn-node-wes-bos-review/113286/13).

![Image](https://cdn-media-1.freecodecamp.org/images/1*a9ES6TeAXN-VtU7CjVB1MQ.png align="left")

[**Microsoft Virtual Academy**](https://mva.microsoft.com/) **(MVA)** propose une collection de cours en ligne gratuits allant de C# et Python à SQL Server et d'autres domaines comme le développement de jeux.

Certains de leurs cours populaires sont [Introduction à la programmation avec Python](https://mva.microsoft.com/en-us/training-courses/introduction-to-programming-with-python-8360), [Fondamentaux de C#](https://mva.microsoft.com/en-US/training-courses/c-fundamentals-for-absolute-beginners-16169) et [Fondamentaux des bases de données SQL](https://mva.microsoft.com/en-US/training-courses/sql-database-fundamentals-16944).

Voici quelques avis sur les cours MVA sur [Reddit](https://www.reddit.com/r/learnprogramming/comments/7kum1x/c_course_on_microsoft_virtual_academy_looks_to_be/) et [LinkedIn](https://www.linkedin.com/pulse/review-microsoft-virtual-academy-database-course-michelle-hoque).

![Image](https://cdn-media-1.freecodecamp.org/images/0*GkbtxAeIvIIUTz0q.png align="left")

[**SoloLearn**](https://www.sololearn.com/) a une approche unique de l'apprentissage du codage : vous pouvez apprendre non seulement à partir de leur site web, mais aussi sur leurs applications mobiles gratuites.

Certains de leurs cours les plus populaires sont Python, C++ et Java.

Ils ont également un tableau de messages de type StackOverflow qui est assez actif avec des questions et des discussions.

Si vous êtes curieux, vous pouvez consulter quelques avis sur SoloLearn sur [Reddit](https://www.reddit.com/r/learnprogramming/comments/7tks7h/is_sololearn_a_good_app_for_learning_code/) et [Quora](https://www.quora.com/How-good-are-SoloLearn-courses-for-learning-programming-Do-their-certificates-have-any-credibility-if-mentioned-in-a-resume).

### Livres

Si vous aimez apprendre à partir de livres, ou si vous voulez en avoir sous la main comme références, voici une courte liste de livres que je pense être bons pour les débutants.

Certains d'entre eux sont gratuits et disponibles en ligne pour que vous puissiez les lire, d'autres sont des livres papier traditionnels.

![Image](https://cdn-media-1.freecodecamp.org/images/0*O7xUZsT9qn-TGvvu.jpg align="left")

**HTML et CSS par Jon Duckett**  
*(*[*lien d'affiliation*](http://amzn.to/2GNgyFt) */* [*lien non affilié*](https://www.amazon.com/gp/product/1118008189)*)*

**JavaScript et JQuery par Jon Duckett**  
*(*[*lien d'affiliation*](http://amzn.to/2EZOq1m) */* [*lien non affilié*](https://www.amazon.com/gp/product/1118531647)*)*

Les livres de Jon Duckett sont probablement les livres les plus populaires pour les développeurs web débutants.

Ce ne sont pas simplement des manuels scolaires, mais des livres magnifiquement conçus qui utilisent des photos et des illustrations pour enseigner les concepts de codage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Kk8_Xc9hFSRWZoYqHX1DVQ.jpeg align="left")

[**Le manuel du développeur front-end**](https://www.gitbook.com/book/frontendmasters/front-end-developer-handbook-2018/details) est un livre en ligne gratuit de [Frontend Masters](https://frontendmasters.com/) et écrit par [Cody Lindley](http://codylindley.com/).

Il est mis à jour chaque année et vous pouvez le considérer comme un guide "état du développement web front-end" avec de nouvelles informations, ressources, tendances et outils liés au domaine.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FIStnBRnDyvqAyayjQzF6A.jpeg align="left")

[**Eloquent JavaScript**](http://eloquentjavascript.net/) est un livre pour débutants sur la programmation qui se concentre sur JavaScript.

Vous pouvez le lire gratuitement en ligne sur le site web, qui dispose d'un outil de console pratique où vous pouvez écrire et tester le code au fur et à mesure que vous lisez.

Si vous voulez une copie physique, le livre est également disponible sur Amazon *(*[*lien d'affiliation*](http://amzn.to/2EVJYof) */* [*lien non affilié*](https://www.amazon.com/Eloquent-JavaScript-2nd-Ed-Introduction/dp/1593275846)*)*.

### Réflexions finales

Est-il possible de s'enseigner le développement web avec des ressources en ligne ? Je crois que la réponse est oui.

Cependant, cela ne sera pas facile du tout. Apprendre et maîtriser quoi que ce soit est difficile, et apprendre à coder ne fait pas exception.

Avec cela à l'esprit, si vous voulez vraiment emprunter ce chemin, voici quelques conseils :

#### **Restez concentré.**

Lorsque vous apprenez par vous-même, il peut être très tentant de sauter d'un tutoriel à l'autre. Surtout lorsque vous commencez à rencontrer des obstacles.

Mais cela peut entraîner un apprentissage très superficiel, alors que vous avez en fait besoin de développer une connaissance plus approfondie des compétences.

Essayez de rester avec le cours/livre sur lequel vous travaillez, sauf si vous ne l'aimez vraiment pas. Surmonter les obstacles vous aidera à développer une compréhension plus complète du matériel.

Et plus vous aborderez de problèmes apparemment impossibles, plus vous vous habituerez à relever des défis.

#### **Tout cours n'est que la première étape de votre parcours d'apprentissage.**

Suivre simplement un tutoriel ou un cours ne signifie pas que vous serez un expert à la fin. Vous devrez apprendre et pratiquer de nombreuses fois avant de vraiment "comprendre".

Essayez de suivre un tutoriel une deuxième fois, ou même d'apprendre le même matériel avec un cours ou un livre différent.

Vous verrez comment différentes personnes expliquent le même concept, et cela peut aider à ancrer les connaissances dans votre cerveau.

**Et, bien sûr, rien ne remplace l'expérience pratique.**

Au fur et à mesure que vous apprenez, essayez de pratiquer les compétences que vous apprenez par vous-même. Construisez des projets aléatoires, créez un site web gratuitement pour un ami ou une organisation à but non lucratif. Plus vous résolvez de problèmes, plus vous les comprendrez.

### Merci d'avoir lu !

![Image](https://cdn-media-1.freecodecamp.org/images/0*wDiab2yE-XocbLtC.gif align="left")

J'espère vraiment que vous avez trouvé cet article utile !

N'hésitez pas à laisser un commentaire ci-dessous avec vos pensées ou vos retours.

#### Vous voulez plus ?

J'écris des tutoriels de développement web sur mon blog, [Coder-Coder.com](https://coder-coder.com) !

D'autres articles de blog que vous pourriez apprécier :

* [Construire une mise en page de site web responsive avec flexbox](https://coder-coder.com/build-flexbox-website-layout/)
  
* [Les meilleurs livres pour apprendre le développement web](https://coder-coder.com/best-web-development-books/)
  
* [Les meilleurs cours pour apprendre le développement web](https://coder-coder.com/best-web-development-courses/)
  

Je publie également des mini-conseils sur [Instagram](https://www.instagram.com/thecodercoder/) et des tutoriels de codage sur [YouTube](https://www.youtube.com/c/codercodertv).