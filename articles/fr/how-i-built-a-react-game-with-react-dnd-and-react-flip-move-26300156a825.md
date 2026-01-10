---
title: Comment j'ai construit un jeu React avec react-dnd et react-flip-move
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-14T00:41:38.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-react-game-with-react-dnd-and-react-flip-move-26300156a825
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d4ldJrlOxFf2SABu9HNteg.png
tags:
- name: Games
  slug: games
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment j'ai construit un jeu React avec react-dnd et react-flip-move
seo_desc: 'By Nicholas Vincent-Hill

  This is a high level overview of my implementation of a puzzle/word game built entirely
  in React. It’s not the prettiest code ever written, but I’m happy with my first
  browser-based game.

  Here’s what I built:

  Scrabblr — Impro...'
---

Par Nicholas Vincent-Hill

Voici un aperçu de haut niveau de mon implémentation d'un jeu de puzzle/mots entièrement construit en React. Ce n'est pas le code le plus joli jamais écrit, mais je suis satisfait de mon premier jeu basé sur un navigateur.

Voici ce que j'ai construit :

#### [Scrabblr](https://scrabblr.herokuapp.com/) — Améliorez vos compétences en Scrabble tout en vous amusant

![Image](https://cdn-media-1.freecodecamp.org/images/Yuy7Y3NjzTb45SAG5BmbqDhXrd9qzHj-vEw6)
_Cliquez sur moi pour jouer à Scrabblr !_

### **Contexte**

Je cherchais des solutions d'animation dans React.js et je suis tombé sur la [démo](http://joshwcomeau.github.io/react-flip-move/examples/#/scrabble?_k=8l9xbo) de [react-flip-move](https://github.com/joshwcomeau/react-flip-move) de Joshua Comeau. J'ai vu le potentiel de construire toutes sortes de jeux similaires au Scrabble avec son interface de glisser-déposer et de mouvement animé.

### Défis techniques

#### Décorateurs avec Babel

Le [react-flip-move](https://github.com/joshwcomeau/react-flip-move) de Joshua Comeau nécessite des décorateurs de fonction, une fonctionnalité du langage non supportée par le compilateur Babel de create-react-app.

![Image](https://cdn-media-1.freecodecamp.org/images/N1ViOUNEKcBwyVbNoGTuIgc0bQsaV3WREoVh)

Le package [react-app-rewired](https://github.com/timarney/react-app-rewired) résout ce problème en remplaçant les configurations Webpack de create-react-app sans éjection (quelque chose de super effrayant pour un débutant comme moi qui ne voulait pas gérer la complexité de Webpack sous le capot).

![Image](https://cdn-media-1.freecodecamp.org/images/DaNp9bCEpfrPwRdXOfuAz7utnMOXa4P9avjo)
_config-overrides.js_

Le code ci-dessus m'a permis d'injecter le plugin [transform-decorators-legacy](https://github.com/loganfsmyth/babel-plugin-transform-decorators-legacy) (sans éjection) pour gérer les décorateurs. Un problème résolu, mais il en reste beaucoup d'autres.

#### Création d'une boucle de jeu

Pour moi, ce qui distingue une chose cool d'un "jeu" est le concept de [boucle de jeu](https://gamedevelopment.tutsplus.com/articles/gamedev-glossary-what-is-the-game-loop--gamedev-2469).

La boucle de jeu principale commence avec une entrée utilisateur (un bouton cliqué pour démarrer une nouvelle partie). L'utilisateur mélange les tuiles et trouve des mots.

Chaque fois que l'utilisateur change l'emplacement d'une tuile, le jeu vérifie s'il y a des mots valides. Si le mot est valide, il marque ce mot et incrémente le score total du score du mot. Il ajoute également ce mot à un tableau "Mots trouvés" pour éviter de le compter deux fois s'il est retrouvé à l'avenir.

Lorsque l'utilisateur trouve tous les mots possibles (voir ci-dessous pour l'implémentation du problème de toutes les correspondances possibles) ou abandonne (clique sur le bouton d'abandon), la boucle de jeu se termine et une fenêtre modale de résultats apparaît.

Les données ou la source de vérité sont toutes contenues dans `state` et transmises à mes composants avec la nouvelle API React.context (pour éviter le [prop-drilling](https://itnext.io/compound-components-with-react-v16-3-6679c752bd56)). Lorsque une nouvelle boucle de jeu commence, ces valeurs sont toutes réinitialisées dans `state`.

![Image](https://cdn-media-1.freecodecamp.org/images/OMK5X0IhgiEZaZeOjdAYU6ew5pQJLVO6-sGi)
_Méthode pour initialiser la boucle de jeu à l'intérieur du composant App_

#### Accès à l'emplacement des tuiles pour trouver des caractères

Ce problème m'a pris un temps embarrassamment long à résoudre. La position (x, y) de la tuile dans la matrice de grille est contenue dans `state.tiles`.

![Image](https://cdn-media-1.freecodecamp.org/images/YESlxksNLL-Mu4pMWirwiv92D4qa-rixtxtM)
_Les tuiles sont créées avec des propriétés par défaut et conservées dans l'état_

J'avais besoin de pouvoir extraire des lettres des tuiles par leur position et assembler une chaîne à valider. Ma solution est un véritable bidouillage et je ne la montrerai pas ici — c'est la méthode `checkForWords()` dans App.js sur [mon Github](https://github.com/nvincenthill/scrabblr), qui a désespérément besoin d'être refactorisée.

#### Validation des mots

J'avais également besoin d'un moyen rapide de vérifier si une chaîne de caractères était un mot anglais valide. Les API de dictionnaires gratuits que j'ai envisagées avaient un nombre de requêtes autorisées par jour prohibitivement bas et une latence élevée. J'avais besoin d'une solution qui me permette de vérifier une liste locale exhaustive rapidement. La méthode `Object.hasOwnProperty()` invoquée sur un dictionnaire de 270 000+ paires clé-valeur fonctionne bien et rapidement.

![Image](https://cdn-media-1.freecodecamp.org/images/JYbcOMZuVG3ZalGkakc-mETO8t0p8KNJin6K)
_Vérifier un seul mot contre le dictionnaire Scrabble_

Le code ci-dessous est ma solution pour trouver tous les mots valides possibles étant donné un tableau de lettres. C'est ainsi que je calcule le nombre de mots restants à afficher à l'utilisateur et que je sais quand terminer la boucle de jeu.

Ma première tentative, sans utiliser la méthode `Object.hasOwnProperty()` et les optimisations de vitesse, a pris près de dix secondes pour calculer tous les mots valides possibles. Cette implémentation semble presque instantanée pour l'utilisateur et est appelée au début d'une nouvelle boucle de jeu.

![Image](https://cdn-media-1.freecodecamp.org/images/aDj0Di2Pw1a2mswM7RLXRuo67nIJ22fb4-tE)
_Trouver tous les mots anglais valides possibles étant donné un tableau de lettres_

### **Conclusion**

J'ai beaucoup appris en construisant ce projet et je suis fier du résultat : mon jeu fonctionne rapidement et a une belle apparence. Finalement, j'aimerais ajouter OAuth et la permanence des données, l'enregistrement des meilleurs scores et des niveaux conçus par les utilisateurs.

Je suis encore nouveau en programmation et en conception web — j'adorerais entendre vos commentaires/suggestions/critiques dans les commentaires.

Jouez à [Scrabblr ici !](https://scrabblr.herokuapp.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/YzhGBRF2K-Z9c8yUrtELsNILPMJlIa1NAu43)

![Image](https://cdn-media-1.freecodecamp.org/images/lesSwgRiwHVV0Y4WKx0M0hr6G84pnN9djrHU)
_Merci d'avoir lu !_

> _Lire ensuite :_

> [Introduction et un peu sur l'accès à l'API d'IEX avec JavaScript](https://medium.com/coding-overload/introduction-and-a-little-about-accessing-iexs-api-with-javascript-7ae4e8af79d6)