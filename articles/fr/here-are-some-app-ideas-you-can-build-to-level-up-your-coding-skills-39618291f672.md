---
title: Voici quelques idées d'applications que vous pouvez construire pour améliorer
  vos compétences en codage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-04T16:21:05.000Z'
originalURL: https://freecodecamp.org/news/here-are-some-app-ideas-you-can-build-to-level-up-your-coding-skills-39618291f672
coverImage: https://cdn-media-1.freecodecamp.org/images/0*v3qXmKe1LTiiW_3H.png
tags:
- name: coding
  slug: coding
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Voici quelques idées d'applications que vous pouvez construire pour améliorer
  vos compétences en codage
seo_desc: 'By Florin Pop

  Have you ever wanted to build something but you had no idea what to do? Just as
  authors sometimes have “writer''s block” it’s also true for developers.

  Together with my friend Jim we created a collection of application ideas which is
  int...'
---

Par Florin Pop

Avez-vous déjà voulu construire quelque chose mais vous ne saviez pas quoi faire ? Tout comme les auteurs ont parfois un "blocage de l'écrivain", c'est aussi vrai pour les développeurs.

Avec mon ami [Jim](https://twitter.com/jd_medlock), nous avons créé une [collection d'idées d'applications](https://github.com/florinpop17/app-ideas) qui est destinée à résoudre ce problème une fois pour toutes !

Ces applications sont :

* excellentes pour améliorer vos compétences en codage
* excellentes pour expérimenter avec de nouvelles technologies
* excellentes à ajouter à votre portfolio pour impressionner votre prochain employeur/client
* excellentes à utiliser comme exemples dans des tutoriels (articles ou vidéos)
* faciles à compléter et également facilement extensibles avec de nouvelles fonctionnalités

Ce n'est pas juste une simple liste de projets, mais une collection qui décrit chaque projet en détail afin que vous puissiez le développer à partir de zéro !

Chaque spécification de projet contient les éléments suivants :

1. Un objectif clair et descriptif
2. Une liste d'_User Stories_ qui doivent être implémentées (ces histoires servent plus de guide que de liste forcée de _To-Do's_. N'hésitez pas à ajouter vos propres fonctionnalités si vous le souhaitez)
3. Une liste de _fonctionnalités bonus_ qui améliorent non seulement le projet de base mais aussi vos compétences en même temps
4. Toutes les ressources et liens pour vous aider à trouver ce dont vous avez besoin pour compléter le projet

%[https://www.youtube.com/watch?v=TNzCfgwIDCY]

### Projets

Tous les projets sont divisés en trois niveaux en fonction des connaissances et de l'expérience requises pour les compléter. Ces niveaux sont :

1. **Débutant** — Développeurs aux premiers stades de leur parcours d'apprentissage. Ceux qui se concentrent généralement sur la création d'applications orientées utilisateur.
2. **Intermédiaire** — Développeurs à un stade intermédiaire d'apprentissage et d'expérience. Ils sont à l'aise avec l'UI/UX, l'utilisation d'outils de développement et la construction d'applications qui utilisent des services API.
3. **Avancé** — Développeurs qui ont tout ce qui précède et apprennent des techniques plus avancées comme l'implémentation d'applications BackEnd et de services de base de données.

Ci-dessous vous trouverez **5 projets** pour chacun des niveaux (**15 au total**), mais il y a plus de **30 projets** (à l'heure actuelle) dans [ce dépôt GitHub](https://github.com/florinpop17/app-ideas). Assurez-vous de le consulter car nous prévoyons d'ajouter plus de projets à l'avenir. Vous êtes les bienvenus pour aider ! (Plus d'informations à ce sujet dans la section _Contribution_ ci-dessous ?)

### 1. Application de Notes

**Niveau** : 1 — Débutant

**Description** : Créez et stockez vos notes pour une utilisation ultérieure !

#### User Stories

* L'utilisateur peut créer une note
* L'utilisateur peut éditer une note
* L'utilisateur peut supprimer une note
* Lorsque la fenêtre du navigateur est fermée, les notes seront stockées et lorsque l'utilisateur revient, les données seront récupérées

#### Fonctionnalités bonus

* L'utilisateur peut créer et éditer une note au format Markdown. À l'enregistrement, elle sera convertie de Markdown en HTML
* L'utilisateur peut voir la date à laquelle il a créé la note

#### Liens et ressources utiles

* [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
* [Guide Markdown](https://www.markdownguide.org/basic-syntax/)
* [Marked — Un parseur markdown](https://github.com/markedjs/marked)

#### Exemple de projet

%[https://codepen.io/nickmoreton/pen/gbyygq]

### 2. Lumières de Noël

**Niveau** : 1 — Débutant

**Description** : L'application Lumières de Noël repose sur vos talents de développement pour créer un affichage lumineux fascinant. Votre tâche consiste à dessiner sept cercles colorés en ligne et, en fonction d'un minuteur, à changer l'intensité de chaque cercle. Lorsqu'un cercle s'illumine, son prédécesseur revient à son intensité normale.

Cela simule l'effet d'une guirlande de lumières ondulantes, similaire à celles affichées pendant les vacances de Noël.

#### User Stories

* L'utilisateur peut appuyer sur un bouton pour démarrer et arrêter l'affichage
* L'utilisateur peut changer l'intervalle de temps contrôlant le changement d'intensité

#### Fonctionnalités bonus

* L'utilisateur peut sélectionner la couleur utilisée pour remplir chaque cercle
* L'utilisateur peut spécifier la valeur d'intensité
* L'utilisateur peut changer la taille de n'importe quel cercle dans la ligne
* L'utilisateur peut spécifier le nombre de lignes à inclure dans l'affichage. De une à sept lignes peuvent être choisies

#### Liens et ressources utiles

* [Image d'exemple](https://previews.123rf.com/images/whiterabbit/whiterabbit1003/whiterabbit100300020/6582600-seven-color-balls-red-orange-yellow-green-cyan-blue-and-magenta-in-a-row-on-a-white-background.jpg)
* [Matrice LED Adafruit](https://cdn-shop.adafruit.com/970x728/1487-02.jpg)

#### Exemple de projet

%[https://codepen.io/tobyj/pen/QjvEex]

### 3. FlipImage

**Niveau** : 1 — Débutant

**Description** : Il est important pour les développeurs web de comprendre les bases de la manipulation d'images, car les applications web riches reposent sur des images pour ajouter de la valeur à l'interface utilisateur et à l'expérience utilisateur (UI/UX).

FlipImage explore un aspect de la manipulation d'images — la rotation d'images. Cette application affiche un panneau carré contenant une seule image présentée dans une matrice 2x2. En utilisant un ensemble de flèches haut, bas, gauche et droite adjacentes à chacune des images, l'utilisateur peut les retourner verticalement ou horizontalement.

Vous ne devez utiliser que du HTML, CSS et JavaScript natifs pour implémenter cette application. Les bibliothèques et packages d'images ne sont pas autorisés.

#### User Stories

* L'utilisateur peut voir un panneau contenant une seule image répétée dans une matrice 2x2
* L'utilisateur peut retourner n'importe laquelle des images verticalement ou horizontalement en utilisant un ensemble de flèches haut, bas, gauche et droite à côté de l'image

#### Fonctionnalités bonus

* L'utilisateur peut changer l'image par défaut en entrant l'URL d'une autre image dans un champ de saisie
* L'utilisateur peut afficher la nouvelle image en cliquant sur un bouton "Afficher" à côté du champ de saisie
* L'utilisateur peut voir un message d'erreur si l'URL de la nouvelle image n'est pas trouvée

#### Liens et ressources utiles

* [Comment retourner une image](https://www.w3schools.com/howto/howto_css_flip_image.asp)
* [Créer une animation de retournement CSS](https://davidwalsh.name/css-flip)

#### Exemple de projet

%[https://codepen.io/seyedi/pen/gvqYQv]

### 4. Application de Quiz

**Niveau** : 1 — Débutant

**Description** : Pratiquez et testez vos connaissances en répondant à des questions dans une application de quiz.

En tant que développeur, vous pouvez créer une application de quiz pour tester les compétences en codage d'autres développeurs. (HTML, CSS, JavaScript, Python, PHP, etc.)

#### User Stories

* L'utilisateur peut démarrer le quiz en appuyant sur un `bouton`
* L'utilisateur peut voir une question avec 4 réponses possibles
* Après avoir sélectionné une réponse, affichez la question suivante à l'utilisateur. Faites cela jusqu'à la fin du quiz
* À la fin, l'utilisateur peut voir les statistiques suivantes :

1. Temps nécessaire pour terminer le quiz
2. Nombre de réponses correctes obtenues
3. Un message indiquant s'il a `réussi` ou `échoué` le quiz

#### Fonctionnalités bonus

* L'utilisateur peut partager le résultat d'un quiz sur les réseaux sociaux
* Ajoutez plusieurs quiz à l'application. L'utilisateur peut choisir celui à faire
* L'utilisateur peut créer un compte et avoir tous les scores sauvegardés dans son tableau de bord. L'utilisateur peut compléter un quiz plusieurs fois

#### Liens et ressources utiles

* [Base de données de quiz ouverte](https://opentdb.com/api_config.php)

#### Exemples de projets

%[https://codepen.io/FlorinPop17/pen/qqYNgW]

[Quiz app built with React](http://tranquil-beyond-43849.herokuapp.com/) (attendez qu'il se charge car il est hébergé sur Heroku)

### 5. Convertisseur de chiffres romains en nombres décimaux

**Niveau** : 1 — Débutant

**Description** : Le système numérique représenté par les chiffres romains a pris naissance dans la Rome antique et est resté la manière habituelle d'écrire les nombres à travers l'Europe jusqu'à la fin du Moyen Âge. Les chiffres romains, tels qu'utilisés aujourd'hui, emploient sept symboles, chacun ayant une valeur entière fixe.

Voir le tableau ci-dessous des paires _Symbole — Valeur_ :

* I — 1
* V — 5
* X — 10
* L — 50
* C — 100
* D — 500
* M — 1000

#### User Stories

* L'utilisateur doit pouvoir entrer un chiffre romain dans un champ de saisie
* L'utilisateur peut voir les résultats dans un seul champ de sortie contenant l'équivalent décimal (base 10) du chiffre romain qui a été entré en appuyant sur un bouton
* Si un symbole incorrect est entré, l'utilisateur doit voir une erreur

#### Fonctionnalités bonus

* L'utilisateur peut voir la conversion se faire automatiquement au fur et à mesure qu'il tape
* L'utilisateur doit pouvoir convertir de décimal en romain (vice-versa)

#### Liens et ressources utiles

* [Une explication des chiffres romains](https://en.wikipedia.org/wiki/Roman_numerals)

#### Exemple de projet

[Convertisseur de chiffres romains](https://www.calculatorsoup.com/calculators/conversions/roman-numeral-converter.php)

### 6. Application de recherche de livres

**Niveau** : 2 — Intermédiaire

**Description** : Créez une application qui permettra aux utilisateurs de rechercher des livres en entrant une requête (Titre, Auteur, etc). Affichez les livres résultants dans une liste sur la page avec toutes les données correspondantes.

#### User Stories

* L'utilisateur peut entrer une requête de recherche dans un champ `input`
* L'utilisateur peut soumettre la requête. Cela appellera une API qui retournera un tableau de livres avec les données correspondantes (**Titre**, **Auteur**, **Date de publication**, **Image**, etc)
* L'utilisateur peut voir la liste des livres apparaître sur la page

#### Fonctionnalités bonus

* Pour chaque élément de la liste, ajoutez un lien qui enverra l'utilisateur vers un site externe qui contient plus d'informations sur le livre
* Implémentez un design réactif
* Ajoutez des animations de chargement

#### Liens et ressources utiles

Vous pouvez utiliser l'[API Google Books](https://developers.google.com/books/docs/overview)

#### Exemple de projet

%[https://codepen.io/chasebank/pen/wpQBKV]

[BookSearch-React](https://fethica.github.io/BookSearch-React/)

### 7. Jeu de mémoire de cartes

**Niveau** : 2 — Intermédiaire

**Description** : Le jeu de mémoire de cartes est un jeu où vous devez cliquer sur une carte pour voir quelle image se trouve en dessous et essayer de trouver l'image correspondante sous les autres cartes.

#### User Stories

* L'utilisateur peut voir une grille avec n x n cartes (`n` est un entier). Toutes les cartes sont face cachée initialement (`état caché`)
* L'utilisateur peut cliquer sur un bouton pour démarrer le jeu. Lorsque ce bouton est cliqué, un minuteur démarrera
* L'utilisateur peut cliquer sur n'importe quelle carte pour révéler l'image qui se trouve en dessous (changer en `état visible`). L'image sera affichée jusqu'à ce que l'utilisateur clique sur une 2ème carte

Lorsque l'utilisateur clique sur la 2ème carte :

* S'il y a une correspondance, les 2 cartes seront éliminées du jeu (soit les cacher/supprimer ou les laisser dans l'`état visible`)
* S'il n'y a pas de correspondance, les 2 cartes retourneront à leur état initial (`état caché`)
* Lorsque toutes les correspondances ont été trouvées, l'utilisateur peut voir une boîte de dialogue affichant un message de félicitations avec un compteur affichant le temps qu'il a fallu pour terminer le jeu

#### Fonctionnalités bonus

* L'utilisateur peut choisir entre plusieurs niveaux de difficulté (Facile, Moyen, Difficile). Une difficulté accrue signifie : diminuer le temps disponible pour compléter et/ou augmenter le nombre de cartes
* L'utilisateur peut voir les statistiques du jeu (nombre de fois où il a gagné/perdu, le meilleur temps pour chaque niveau)

#### Liens et ressources utiles

* [Wikipedia](https://en.wikipedia.org/wiki/Concentration_(game))

#### Exemples de projets

[Flip — jeu de mémoire de cartes](https://codepen.io/zerospree/full/bNWbvW)

[SMB3 Memory Card Game](https://codepen.io/hexagoncircle/full/OXBJxV)

### 8. Générateur de tableaux Markdown

**Niveau** : 2 — Intermédiaire

**Description** : Créez une application qui convertira un tableau régulier avec des données fournies par l'utilisateur (optionnellement) en un tableau formaté en Markdown.

#### User Stories

* L'utilisateur peut créer un `tableau HTML` avec un nombre donné de **lignes** et de **colonnes**
* L'utilisateur peut insérer du texte dans chaque cellule du `tableau HTML`
* L'utilisateur peut générer un `tableau formaté en Markdown` qui contiendra les données du `tableau HTML`
* L'utilisateur peut prévisualiser le `tableau formaté en Markdown`

#### Fonctionnalités bonus

* L'utilisateur peut copier le `tableau formaté en Markdown` dans le presse-papiers en appuyant sur un bouton
* L'utilisateur peut insérer une nouvelle **ligne** ou **colonne** à un emplacement spécifié
* L'utilisateur peut supprimer une **ligne** ou une **colonne** entièrement
* L'utilisateur peut aligner (à _gauche_, _droite_ ou _centre_) une **cellule**, une **colonne**, une **ligne**, ou le **tableau** entier

#### Liens et ressources utiles

* [Guide Markdown](https://www.markdownguide.org/)
* [Marked — Un parseur markdown](https://github.com/markedjs/marked)
* [Comment copier dans le presse-papiers](https://www.w3schools.com/howto/howto_js_copy_clipboard.asp)

#### Exemple de projet

[Générateur de tableaux / Tableaux Markdown](https://www.tablesgenerator.com/markdown_tables)

### 9. Art de ficelle

**Niveau** : 2 — Intermédiaire

**Description** : Le but de l'Art de ficelle est de fournir au développeur une pratique pour créer un graphique animé simple, en utilisant la géométrie dans l'algorithme d'animation, et en créant quelque chose qui est visuellement agréable à regarder.

L'Art de ficelle dessine une seule ligne multicolore qui se déplace en douceur jusqu'à ce qu'une extrémité touche un côté de la fenêtre englobante. À ce moment, un effet de "rebond" est appliqué pour changer sa direction.

Un effet d'ondulation est créé en ne retenant que 10 à 20 images de la ligne lorsqu'elle se déplace. Les images plus anciennes s'estompent progressivement jusqu'à disparaître.

Les bibliothèques d'animation ne sont pas autorisées. Utilisez uniquement du HTML/CSS/JavaScript Vanilla.

#### User Stories

* Commencez par dessiner une ligne multicolore à une position aléatoire dans les limites de sa fenêtre englobante
* Toutes les 20 ms, dessinez une nouvelle copie de la ligne à une nouvelle position basée sur une trajectoire — la distance incrémentielle par rapport à la ligne précédente basée sur les points d'extrémité
* Lorsque l'une ou l'autre des extrémités de la ligne touche la limite de la fenêtre englobante, changez sa direction et modifiez aléatoirement son angle
* Estompez progressivement l'intensité des anciennes lignes afin que seules les 10 à 20 lignes les plus récentes soient visibles pour créer le sens du mouvement ou de "l'ondulation"

#### Fonctionnalités bonus

* L'utilisateur peut spécifier la longueur de la ligne et sa vitesse
* L'utilisateur peut spécifier plusieurs lignes dans la fenêtre, toutes se déplaçant le long de différentes trajectoires et vitesses

#### Liens et ressources utiles

* [Utilisation des animations et transitions multi-étapes](https://css-tricks.com/using-multi-step-animations-transitions/)
* [Bases de l'animation](https://www.khanacademy.org/computing/computer-programming/programming/animation-basics/a/what-are-animations)

#### Exemple de projet

Ce projet est très proche, mais a une petite fenêtre englobante et est monochromatique. [Daniel Cortes](https://codepen.io/dgca/pen/dpxreO)

### 10. Application de To-Do

**Niveau** : 2 — Intermédiaire

**Description** : L'application classique To-Do où un utilisateur peut écrire toutes les choses qu'il veut accomplir.

#### User Stories

* L'utilisateur peut voir un champ `input` où il peut taper un élément de to-do
* En appuyant sur entrer (ou un bouton), l'utilisateur peut soumettre l'élément de to-do et peut voir qu'il est ajouté à une liste de to-do
* L'utilisateur peut marquer un to-do comme `complété`
* L'utilisateur peut supprimer un élément de to-do en appuyant sur un bouton (ou sur l'élément de to-do lui-même)

#### Fonctionnalités bonus

* L'utilisateur peut éditer un to-do
* L'utilisateur peut voir une liste avec tous les to-do `complétés`
* L'utilisateur peut voir une liste avec tous les to-do `actifs`
* L'utilisateur peut voir la date à laquelle il a créé le to-do
* Lorsque la fenêtre du navigateur est fermée, les to-do seront stockés et lorsque l'utilisateur revient, les données seront récupérées

#### Liens et ressources utiles

* [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

#### Exemples de projets

%[https://codepen.io/yesilfasulye/pen/eJIuF]

[Todo App built with React](http://todomvc.com/examples/react/#/)

### 11. Moteur de jeu de Bataille navale

**Niveau** : 3 — Avancé

**Description** : Le moteur de jeu de Bataille navale (BGE) implémente le classique jeu de plateau à tours comme un package qui est séparé de toute couche de présentation. Il s'agit d'un type de modèle architectural utile dans de nombreuses applications, car il permet à un nombre quelconque d'applications d'utiliser le même service.

Le BGE lui-même est invoqué par une série d'appels de fonctions plutôt que par des actions directes de l'utilisateur final. À cet égard, l'utilisation du BGE est similaire à l'utilisation d'une API ou d'une série de routes exposées par un serveur web.

Ce défi nécessite que vous développiez le BGE et une couche de présentation très fine, basée sur du texte, pour les tests, qui est séparée du moteur lui-même. En raison de cela, les User Stories ci-dessous sont divisées en deux ensembles — un pour le BGE et un pour la couche de présentation basée sur du texte.

Le BGE est responsable du maintien de l'état du jeu.

#### User Stories

#### BGE

* L'appelant peut invoquer une fonction `startGame()` pour commencer un jeu à 1 joueur. Cette fonction générera un plateau de jeu 8x8 composé de 3 navires ayant une largeur d'un carré et une longueur de :

1. Destroyer : 2 carrés
2. Croiseur : 3 carrés
3. Cuirassé : 4 carrés

`startGame()` placera aléatoirement ces navires sur le plateau dans n'importe quelle direction et retournera un tableau représentant le placement des navires.

* L'appelant peut invoquer une fonction `shoot()` en passant les coordonnées de ligne et de colonne cibles de la cellule ciblée sur le plateau de jeu. `shoot()` retournera des indicateurs représentant si le tir a résulté en un coup ou un raté, le nombre de navires restants (c'est-à-dire non encore coulés), le tableau de placement des navires, et les tableaux de coups et de ratés mis à jour.

Les cellules dans les tableaux de coups et de ratés contiendront un espace si elles n'ont pas encore été ciblées, `O` si elles ont été ciblées mais qu'aucune partie d'un navire n'était à cet endroit, ou `X` si la cellule était occupée par une partie d'un navire.

#### Couche de présentation basée sur du texte

* L'utilisateur peut voir les tableaux de coups et de ratés affichés sous forme de représentation de caractères en deux dimensions du plateau de jeu retourné par la fonction `startGame()`.
* L'utilisateur peut être invité à entrer les coordonnées d'une case cible sur le plateau de jeu.
* L'utilisateur peut voir une mise à jour de l'affichage des tableaux de coups et de ratés après avoir tiré.
* L'utilisateur peut voir un message après chaque tir indiquant si le tir a résulté en un coup ou un raté.
* L'utilisateur peut voir un message de félicitations après le tir qui coule le dernier navire restant.
* L'utilisateur peut être invité à rejouer à la fin de chaque jeu. Refuser de rejouer arrête le jeu.

#### Fonctionnalités bonus

#### BGE

* L'appelant peut spécifier le nombre de lignes et de colonnes dans le plateau de jeu comme paramètre de la fonction `startGame()`.
* L'appelant peut invoquer une fonction `gameStats()` qui retourne un objet JavaScript contenant des métriques pour le jeu actuel. Par exemple, le nombre de tours joués, le nombre actuel de coups et de ratés, etc.
* L'appelant peut spécifier le nombre de joueurs (1 ou 2) lors de l'appel de `startGame()` qui générera un plateau pour chaque joueur, peuplé aléatoirement de navires.

`shoot()` acceptera le numéro du joueur pour lequel le tir est effectué, ainsi que les coordonnées du tir. Les données qu'il retourne seront pour ce joueur.

#### Couche de présentation basée sur du texte

* L'utilisateur peut voir les statistiques du jeu actuel à tout moment en entrant le mot `stats` à la place des coordonnées cibles. (Notez que cela nécessite la fonction `gameStats()` dans le BGE)
* L'utilisateur peut spécifier qu'un jeu à deux joueurs doit être joué, chaque joueur alternant les tours dans la même session de terminal (Notez que cela nécessite les fonctionnalités bonus correspondantes dans le BGE)
* L'utilisateur peut voir le numéro du joueur dans les invites associées aux entrées de chaque tour.
* L'utilisateur peut voir les plateaux des deux joueurs à la fin de chaque tour.

#### Liens et ressources utiles

* [Jeu de Bataille navale (Wikipedia)](https://en.wikipedia.org/wiki/Battleship_(game))
* [Règles du jeu de Bataille navale (Hasbro)](https://www.hasbro.com/common/instruct/battleship.pdf)

#### Exemples de projets

Cette vidéo YouTube montre comment un jeu de [Bataille navale basé sur du texte](https://www.youtube.com/watch?v=TKksu3JXTTM) est joué.

L'exemple suivant est fourni comme démonstration du jeu de Bataille navale s'il vous est inconnu. N'oubliez pas que vous devez implémenter une couche de présentation basée sur du texte pour les tests. [Jeu de Bataille navale par Chris Brody](https://codepen.io/CodifyAcademy/pen/ByBEOz)

### 12. Application de Chat

**Niveau** : 3 — Avancé

**Description** : Interface de chat en temps réel où plusieurs utilisateurs peuvent interagir les uns avec les autres en envoyant des messages.

En tant que MVP (Produit Minimum Viable), vous pouvez vous concentrer sur la construction de l'interface de chat. La fonctionnalité en temps réel peut être ajoutée plus tard (les fonctionnalités bonus).

#### User Stories

* L'utilisateur est invité à entrer un nom d'utilisateur lorsqu'il visite l'application de chat. Le nom d'utilisateur sera stocké dans l'application
* L'utilisateur peut voir un champ `input` où il peut taper un nouveau message
* En appuyant sur la touche `enter` ou en cliquant sur le bouton `envoyer`, le texte sera affiché dans la `boîte de chat` avec son nom d'utilisateur (par exemple, `John Doe : Hello World !`)

#### Fonctionnalités bonus

* Les messages seront visibles pour tous les utilisateurs qui sont dans l'application de chat (en utilisant WebSockets)
* Lorsqu'un nouvel utilisateur rejoint le chat, un message est affiché à tous les utilisateurs existants
* Les messages sont sauvegardés dans une base de données
* L'utilisateur peut envoyer des images, des vidéos et des liens qui seront affichés correctement
* L'utilisateur peut sélectionner et envoyer un emoji
* Les utilisateurs peuvent chatter en privé
* Les utilisateurs peuvent rejoindre des `canaux` sur des sujets spécifiques

#### Liens et ressources utiles

* [Socket.io](https://socket.io/)
* [Comment construire une application de chat React.js en 10 minutes — article](https://medium.freecodecamp.org/how-to-build-a-react-js-chat-app-in-10-minutes-c9233794642b)

%[https://www.youtube.com/watch?v=tHbCkikFfDE]

#### Exemple de projet

%[https://codepen.io/iremlopsum/pen/ZWEdZj]

[Chatty2](https://web-chatty.herokuapp.com/)

### 13. Chronologie GitHub

**Niveau** : 3 — Avancé

**Description** : Les API et la représentation graphique des informations sont des caractéristiques des applications web modernes. GitHub Timeline combine les deux pour créer un historique visuel de l'activité GitHub d'un utilisateur.

Le but de GitHub Timeline est d'accepter un nom d'utilisateur GitHub et de produire une chronologie contenant chaque dépôt et annotée avec les noms des dépôts, les dates de leur création et leurs descriptions. La chronologie doit être celle qui pourrait être partagée avec un employeur potentiel. Elle doit être facile à lire et faire un usage efficace de la couleur et de la typographie.

Seuls les dépôts GitHub publics doivent être affichés.

#### User Stories

* L'utilisateur peut entrer un nom d'utilisateur GitHub
* L'utilisateur peut cliquer sur un bouton "Générer" pour créer et afficher la chronologie des dépôts de l'utilisateur nommé
* L'utilisateur peut voir un message d'avertissement si le nom d'utilisateur GitHub n'est pas un nom d'utilisateur GitHub valide.

#### Fonctionnalités bonus

* L'utilisateur peut voir un résumé du nombre de dépôts comptabilisés par l'année de leur création

#### Liens et ressources utiles

GitHub propose deux API que vous pouvez utiliser pour accéder aux données des dépôts. Vous pouvez également choisir d'utiliser un package NPM pour accéder à l'API GitHub.

La documentation de l'API GitHub peut être trouvée à :

* [API REST GitHub V3](https://developer.github.com/v3/)
* [API GraphQL GitHub V4](https://developer.github.com/v4/)

Exemple de code montrant comment utiliser les API GitHub :

Vous pouvez utiliser cette commande CURL pour voir le JSON retourné par l'API REST V3 pour vos dépôts :

```bash
curl -u "user-id" https://api.github.com/users/user-id/repos
```

#### Exemples de projets

%[https://codepen.io/NilsWe/pen/FemfK]

%[https://codepen.io/tutsplus/pen/QNeJgR]

### 14. Spell-It

**Niveau** : 3 — Avancé

**Description** : Savoir épeler est une partie fondamentale de la maîtrise de toute langue. Que vous soyez un jeune apprenant à épeler ou un individu apprenant une nouvelle langue, pouvoir pratiquer aide à solidifier vos compétences linguistiques.

L'application Spell-It aide les utilisateurs à pratiquer leur orthographe en jouant l'enregistrement audio d'un mot que l'utilisateur doit ensuite épeler en utilisant le clavier de l'ordinateur.

#### User Stories

* L'utilisateur peut cliquer sur le bouton "Jouer" pour entendre le mot qui doit être entré
* L'utilisateur peut voir les lettres affichées dans la boîte de texte d'entrée du mot au fur et à mesure qu'elles sont entrées sur le clavier
* L'utilisateur peut cliquer sur le bouton "Entrer" pour soumettre le mot qui a été tapé dans la boîte de texte d'entrée du mot
* L'utilisateur peut voir un message de confirmation lorsque le mot correct est tapé
* L'utilisateur peut voir un message demandant de taper à nouveau le mot lorsqu'il est mal orthographié
* L'utilisateur peut voir un décompte du nombre d'orthographes correctes, du nombre total de mots tentés et un pourcentage d'entrées réussies.

#### Fonctionnalités bonus

* L'utilisateur peut entendre un son de confirmation lorsque le mot est correctement orthographié
* L'utilisateur peut entendre un son d'avertissement lorsque le mot est mal orthographié
* L'utilisateur peut cliquer sur le bouton "Indice" pour mettre en évidence les lettres incorrectes dans la boîte de texte d'entrée du mot
* L'utilisateur peut appuyer sur la touche "Entrer" du clavier pour soumettre un mot tapé ou cliquer sur le bouton "Entrer" dans la fenêtre de l'application

#### Liens et ressources utiles

* [Texas Instruments Speak and Spell](https://en.wikipedia.org/wiki/Speak_%26_Spell_(toy))
* [Web Audio API](https://codepen.io/2kool2/full/RgKeyp)
* [Click and Speak](https://codepen.io/shangle/full/Wvqqzq)

#### Exemples de projets

[Word Wizard pour iOS](https://itunes.apple.com/app/id447312716)

[Speak N Spell sur Google Play](https://play.google.com/store/apps/details?id=au.id.weston.scott.SpeakAndSpell&hl=en_US)

### 15. Application de sondage

**Niveau** : 3 — Avancé

**Description** : Les sondages sont une partie précieuse de la boîte à outils de tout développeur. Ils sont utiles pour obtenir des commentaires de vos utilisateurs sur une variété de sujets, y compris la satisfaction de l'application, les exigences, les besoins futurs, les problèmes, les priorités, et simplement les frustrations pour n'en nommer que quelques-unes.

L'application de sondage vous donne l'opportunité d'apprendre en développant une application complète que vous pouvez ajouter à votre boîte à outils. Elle offre la possibilité de définir un sondage, de permettre aux utilisateurs de répondre dans un délai prédéterminé, et de tabuler et de présenter les résultats.

Les utilisateurs de cette application sont divisés en deux rôles distincts, chacun ayant des exigences différentes :

* Les _Coordinateurs de sondage_ définissent et mènent des sondages. Il s'agit d'une fonction administrative non disponible pour les utilisateurs normaux.
* Les _Répondants au sondage_ complètent les sondages et consultent les résultats. Ils n'ont aucun privilège administratif dans l'application.

Les outils de sondage commerciaux incluent une fonctionnalité de distribution qui envoie des sondages par e-mail en masse aux répondants. Pour simplifier, cette application suppose que les sondages ouverts pour les réponses seront accessibles à partir de la page web de l'application.

#### User Stories

#### Général

* Les coordinateurs de sondage et les répondants peuvent définir, mener et consulter des sondages et les résultats des sondages à partir d'un site web commun
* Les coordinateurs de sondage peuvent se connecter à l'application pour accéder aux fonctions administratives, comme la définition d'un sondage.

#### Définition d'un sondage

* Le coordinateur de sondage peut définir un sondage contenant 1 à 10 questions à choix multiples.
* Le coordinateur de sondage peut définir 1 à 5 sélections mutuellement exclusives pour chaque question.
* Le coordinateur de sondage peut entrer un titre pour le sondage.
* Le coordinateur de sondage peut cliquer sur un bouton "Annuler" pour revenir à la page d'accueil sans sauvegarder le sondage.
* Le coordinateur de sondage peut cliquer sur un bouton "Sauvegarder" pour sauvegarder un sondage.

#### Conduite d'un sondage

* Le coordinateur de sondage peut ouvrir un sondage en sélectionnant un sondage dans une liste de sondages précédemment définis
* Les coordinateurs de sondage peuvent fermer un sondage en le sélectionnant dans une liste de sondages ouverts
* Le répondant au sondage peut compléter un sondage en le sélectionnant dans une liste de sondages ouverts
* Le répondant au sondage peut sélectionner des réponses aux questions du sondage en cliquant sur une case à cocher
* Les répondants au sondage peuvent voir qu'une réponse précédemment sélectionnée sera automatiquement décochée si une réponse différente est cliquée.
* Les répondants au sondage peuvent cliquer sur un bouton "Annuler" pour revenir à la page d'accueil sans soumettre le sondage.
* Les répondants au sondage peuvent cliquer sur un bouton "Soumettre" pour soumettre leurs réponses au sondage.
* Les répondants au sondage peuvent voir un message d'erreur si "Soumettre" est cliqué, mais que toutes les questions n'ont pas reçu de réponse.

#### Visualisation des résultats du sondage

* Les coordinateurs de sondage et les répondants peuvent sélectionner le sondage à afficher dans une liste de sondages fermés
* Les coordinateurs de sondage et les répondants peuvent consulter les résultats du sondage sous forme de tableau montrant le nombre de réponses pour chacune des sélections possibles aux questions.

#### Fonctionnalités bonus

* Les répondants au sondage peuvent créer un compte unique dans l'application
* Les répondants au sondage peuvent se connecter à l'application
* Les répondants au sondage ne peuvent pas compléter le même sondage plus d'une fois
* Les coordinateurs de sondage et les répondants peuvent consulter des représentations graphiques des résultats du sondage (par exemple, des graphiques en camembert, en barres, en colonnes, etc.)

#### Liens et ressources utiles

Bibliothèques pour créer des sondages : [SurveyJS](https://surveyjs.io/Overview/Library/)

Certains services de sondage commerciaux incluent : [Survey Monkey](https://www.surveymonkey.com/) et [Typeform](https://www.typeform.com/)

#### Exemple de projet

%[https://codepen.io/amyfu/pen/oLChg]

### _Contribution_

Vous êtes les bienvenus pour contribuer au projet dans le [dépôt GitHub](https://github.com/florinpop17/app-ideas) ! Toute contribution est grandement appréciée.

Vous pouvez contribuer de deux manières :

1. créez un problème et dites-nous votre idée. Assurez-vous d'utiliser l'étiquette **nouvelle idée** dans ce cas ;
2. forkez le projet et soumettez une PR. Avant de le faire, assurez-vous de lire et de suivre le Guide de Contribution (vous pouvez le trouver dans le dépôt) ;

#### Ajoutez vos propres exemples

Vous pouvez également ajouter vos propres exemples aux projets après les avoir complétés. Je vous encourage vivement à le faire car cela montrera aux autres les choses incroyables que vous avez construites ! ?

### Faites passer le mot !

Si les informations de cet article et du dépôt vous ont été utiles de quelque manière que ce soit, assurez-vous de lui donner une étoile ?, afin que d'autres puissent le trouver et en bénéficier également ! Ensemble, nous pouvons grandir et rendre notre communauté meilleure !

Avez-vous des suggestions sur la manière dont nous pourrions améliorer ce projet dans son ensemble ? Faites-le nous savoir ! Nous serions ravis d'avoir votre retour !

#### Principaux contributeurs ??

**Florin Pop** : [Twitter](https://twitter.com/florinpop1705) et [site web](https://florin-pop.com).

**Jim Medlock** : [Twitter](https://twitter.com/jd_medlock) et [Medium](https://medium.com/@jdmedlock)

### **Défi de codage hebdomadaire ?**

En bonus, il y a un Défi de Codage Hebdomadaire où vous pouvez en apprendre davantage en pratiquant vos compétences sur des projets du monde réel. Lisez [Le Guide Complet](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/) pour découvrir comment vous pouvez participer ! ?

_Publié à l'origine sur [www.florin-pop.com](https://www.florin-pop.com/blog/2019/03/15-plus-app-ideas-to-build-to-level-up-your-coding-skills/).