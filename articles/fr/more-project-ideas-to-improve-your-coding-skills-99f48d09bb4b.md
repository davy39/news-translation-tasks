---
title: Plus d'idées de projets pour améliorer vos compétences en codage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-18T18:42:43.000Z'
originalURL: https://freecodecamp.org/news/more-project-ideas-to-improve-your-coding-skills-99f48d09bb4b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*hL2XRi5uD_N7Pr8T.png
tags:
- name: application
  slug: application
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Plus d'idées de projets pour améliorer vos compétences en codage
seo_desc: 'By Florin Pop

  https://www.youtube.com/watch?v=TNzCfgwIDCY

  Two weeks ago I published an article containing 15 project ideas that you can build
  to level up your coding skills, and people were very excited about that resource.

  Also, the app-ideas reposi...'
---

Par Florin Pop

%[https://www.youtube.com/watch?v=TNzCfgwIDCY]

Il y a deux semaines, j'ai publié un article contenant [15 idées de projets](https://medium.freecodecamp.org/here-are-some-app-ideas-you-can-build-to-level-up-your-coding-skills-39618291f672) que vous pouvez réaliser pour améliorer vos compétences en codage, et les gens étaient très enthousiastes à propos de cette ressource.

De plus, le dépôt [app-ideas](https://github.com/florinpop17/app-ideas) a obtenu près de 3000 étoiles depuis que j'ai publié cet article. C'est incroyable ! ?

Merci à tous pour cela ! ?

Dans cet article, nous allons passer en revue quelques **nouveaux** projets qui ont été ajoutés au dépôt depuis.

Pour rappel, tous les projets sont divisés en trois _niveaux_ en fonction des connaissances et de l'expérience requises pour les compléter. Consultez la description des _niveaux_ dans le dépôt.

Vous trouverez ci-dessous 2 idées de projets **Débutant**, 4 **Intermédiaire** et 3 **Avancé**.

### 1. CALCULATRICE

**Niveau :** 1 — Débutant

Les calculatrices ne sont pas seulement l'un des outils les plus utiles disponibles, mais elles sont également un excellent moyen de comprendre l'interface utilisateur et le traitement des événements dans une application. Dans ce problème, vous allez créer une calculatrice qui prend en charge les calculs arithmétiques de base sur des entiers.

Le style est à votre discrétion, alors utilisez votre imagination et soyez créatif ! Vous pourriez également trouver utile d'expérimenter avec l'application calculatrice sur votre appareil mobile pour mieux comprendre la fonctionnalité de base et les cas particuliers.

#### Contraintes

* Vous ne pouvez pas utiliser la fonction `eval()` pour exécuter les calculs

#### Histoires utilisateur

* L'utilisateur peut voir un affichage montrant le nombre actuel entré ou le résultat de la dernière opération.
* L'utilisateur peut voir un pavé de saisie contenant des boutons pour les chiffres 0–9, les opérations — '+', '-', '/', et '=', un bouton 'C' (pour effacer), et un bouton 'AC' (pour tout effacer).
* L'utilisateur peut entrer des nombres comme des séquences jusqu'à 8 chiffres en cliquant sur les chiffres du pavé de saisie. La saisie de plus de 8 chiffres sera ignorée.
* L'utilisateur peut cliquer sur un bouton d'opération pour afficher le résultat de cette opération sur : _ le résultat de l'opération précédente et le dernier nombre entré OU _ les deux derniers nombres entrés OU * le dernier nombre entré
* L'utilisateur peut cliquer sur le bouton 'C' pour effacer le dernier nombre ou la dernière opération. Si la dernière entrée de l'utilisateur était une opération, l'affichage sera mis à jour avec la valeur qui la précédait.
* L'utilisateur peut cliquer sur le bouton 'AC' pour effacer toutes les zones de travail internes et pour réinitialiser l'affichage à 0.
* L'utilisateur peut voir 'ERR' affiché si une opération dépasse le maximum de 8 chiffres.

#### Fonctionnalités bonus

* L'utilisateur peut cliquer sur un bouton '+/-' pour changer le signe du nombre actuellement affiché.
* L'utilisateur peut voir un bouton de point décimal (.) sur le pavé de saisie qui permet d'entrer des nombres à virgule flottante jusqu'à 3 décimales et d'effectuer des opérations jusqu'au nombre maximum de décimales entrées pour un nombre.

#### Liens et ressources utiles

* [Calculatrice (Wikipédia)](https://en.wikipedia.org/wiki/Calculator)
* [MDN](https://developer.mozilla.org/en-US/)

#### Exemples de projets

%[https://codepen.io/giana/pen/GJMBEv]

%[https://codepen.io/mjijackson/pen/xOzyGX]

### 2. APPLICATION DE RECETTES

**Niveau :** 1 — Débutant

Vous ne vous en êtes peut-être pas rendu compte, mais les recettes ne sont rien de plus que des algorithmes culinaires. Comme les programmes, les recettes sont une série d'étapes impératives qui, si elles sont suivies correctement, aboutissent à un plat savoureux.

L'objectif de l'application de recettes est d'aider l'utilisateur à gérer les recettes de manière à ce qu'elles soient faciles à suivre.

#### Contraintes

* Pour la version initiale de cette application, les données de recettes peuvent être encodées sous forme de fichier JSON. Après avoir implémenté la version initiale de cette application, vous pouvez l'étendre pour maintenir les recettes dans un fichier ou une base de données.

#### Histoires utilisateur

* L'utilisateur peut voir une liste de titres de recettes
* L'utilisateur peut cliquer sur un titre de recette pour afficher une carte de recette contenant le titre de la recette, le type de repas (petit-déjeuner, déjeuner, dîner ou collation), le nombre de personnes qu'elle sert, son niveau de difficulté (débutant, intermédiaire, avancé), la liste des ingrédients (y compris leurs quantités), et les étapes de préparation.
* L'utilisateur clique sur un nouveau titre de recette pour remplacer la carte actuelle par une nouvelle recette.

#### Fonctionnalités bonus

* L'utilisateur peut voir une photo montrant à quoi ressemble l'article après qu'il a été préparé.
* L'utilisateur peut rechercher une recette qui n'est pas dans la liste des titres de recettes en entrant le nom du repas dans une boîte de recherche et en cliquant sur un bouton 'Rechercher'. Toute API de recettes open source peut être utilisée comme source pour les recettes (voir The MealDB ci-dessous).
* L'utilisateur peut voir une liste de recettes correspondant aux termes de recherche
* L'utilisateur peut cliquer sur le nom de la recette pour afficher sa carte de recette.
* L'utilisateur peut voir un message d'avertissement si aucune recette correspondante n'a été trouvée.
* L'utilisateur peut cliquer sur un bouton 'Enregistrer' sur les cartes des recettes trouvées via l'API pour enregistrer une copie dans le fichier ou la base de données de recettes de cette application.

#### Liens et ressources utiles

* [Utilisation de Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
* [Axios](https://www.npmjs.com/package/axios)
* [The MealDB API](https://www.themealdb.com/api.php)

#### Exemples de projets

%[https://codepen.io/eddyerburgh/pen/xVeJvB]

%[https://codepen.io/inkblotty/pen/oxWRme]

### 3. APPLICATION DE DESSIN

**Niveau :** 2 — Intermédiaire

Créez des œuvres d'art numériques sur une toile sur le web pour les partager en ligne et les exporter sous forme d'images.

#### Histoires utilisateur

* L'utilisateur peut dessiner dans un `canvas` en utilisant la souris
* L'utilisateur peut changer la couleur
* L'utilisateur peut changer la taille de l'outil
* L'utilisateur peut appuyer sur un bouton pour effacer le `canvas`

#### Fonctionnalités bonus

* L'utilisateur peut enregistrer l'œuvre d'art en tant qu'image (format `.png`, `.jpg`, etc)
* L'utilisateur peut dessiner différentes formes (`rectangle`, `cercle`, `étoile`, etc)
* L'utilisateur peut partager l'œuvre d'art sur les réseaux sociaux

#### Liens et ressources utiles

* [Apprenez à créer une application de dessin en utilisant p5js](https://www.florin-pop.com/blog/2019/04/drawing-app-built-with-p5js/)

#### Exemples de projets

%[https://codepen.io/FlorinPop17/pen/VNYyZQ]

%[https://codepen.io/t0mm4rx/pen/dLowvZ]

### 4. TRADUCTEUR D'EMOJI

**Niveau :** 2 — Intermédiaire

Les emojis sont devenus la _lingua franca_ de la société moderne. Ils sont un moyen amusant et rapide de communiquer, mais aussi un mécanisme extrêmement expressif pour communiquer des émotions et des réactions.

L'objectif de l'application Traducteur d'Emoji est de traduire le texte saisi par l'utilisateur en une chaîne équivalente d'emojis, traduite à partir d'un ou plusieurs mots dans le texte original, et des mots pour lesquels il n'y a pas d'emoji correspondant.

#### Histoires utilisateur

* L'utilisateur peut entrer une chaîne de mots, de nombres et de ponctuation dans une boîte de texte
* L'utilisateur peut cliquer sur un bouton 'Traduire' pour traduire les mots dans le texte saisi en leurs emojis correspondants.
* L'utilisateur peut voir un message d'avertissement si 'Traduire' a été cliqué, mais que la boîte de texte d'entrée était vide ou inchangée depuis la dernière traduction.
* L'utilisateur peut voir les éléments de texte dans le texte saisi traduits en leurs emojis équivalents dans une boîte de texte de sortie. Les éléments de texte pour lesquels il n'y a pas d'emoji resteront inchangés.
* L'utilisateur peut cliquer sur un bouton 'Effacer' pour effacer les boîtes de texte d'entrée et de sortie.

#### Fonctionnalités bonus

* Le développeur implémentera une fonctionnalité de synonyme d'emoji pour permettre à l'application de traduire une plus grande variété de mots en emoji.
* L'utilisateur peut sélectionner la langue dans laquelle le texte d'entrée est saisi à partir d'une liste déroulante de langues.

#### Liens et ressources utiles

[Liste complète des emojis v12.0](https://unicode.org/emoji/charts/full-emoji-list.html)

#### Exemples de projets

[Emoji Translate](https://emojitranslate.com/)

### 5. APPLICATION DE GÉNÉRATION DE MÈMES

**Niveau :** 2 — Intermédiaire

Permettre aux utilisateurs de générer des mèmes personnalisés en ajoutant du texte sur une image.

#### Histoires utilisateur

* L'utilisateur peut télécharger une image qui apparaîtra dans un canvas
* L'utilisateur peut ajouter du texte dans la partie supérieure de l'image
* L'utilisateur peut ajouter du texte dans la partie inférieure de l'image
* L'utilisateur peut sélectionner la couleur du texte
* L'utilisateur peut sélectionner la taille du texte
* L'utilisateur peut enregistrer le mème résultant

#### Fonctionnalités bonus

* L'utilisateur peut sélectionner la famille de polices pour le texte
* L'utilisateur peut partager le mème sur les réseaux sociaux (twitter, reddit, facebook, etc)
* L'utilisateur peut faire glisser le texte et le placer où il le souhaite sur l'image
* L'utilisateur peut dessiner des formes sur l'image (cercles, rectangles, ou dessin libre avec la souris)

#### Liens et ressources utiles

Travailler avec canvas est rendu très facile par la bibliothèque [p5js](http://p5js.org/).

#### Exemples de projets

[Générateur de Mèmes par imgflip](https://imgflip.com/memegenerator)

%[https://codepen.io/ninivert/pen/BpLKRx]

### 6. PRATIQUE DE LA FRAPPE

**Niveau :** 2 — Intermédiaire

Certaines choses sont si évidentes qu'elles peuvent être facilement négligées. En tant que développeur, votre capacité à taper rapidement et avec précision est un facteur qui influence votre productivité de développement. L'objectif de l'application Pratique de la frappe est de vous fournir une pratique de la frappe ainsi que des métriques pour vous permettre de mesurer vos progrès.

La pratique de la frappe affiche un mot que vous devez ensuite taper dans un intervalle de temps spécifique. Si le mot est mal tapé, il reste à l'écran et l'intervalle de temps reste le même. Mais lorsque le mot est correctement tapé, un nouveau mot est affiché et l'intervalle de temps est légèrement réduit.

Espérons que cette pratique répétitive vous aidera à améliorer à la fois votre vitesse et votre précision de frappe.

#### Histoires utilisateur

* L'utilisateur peut voir l'intervalle de temps dans lequel les mots doivent être tapés affiché dans la fenêtre de l'application.
* L'utilisateur peut voir le nombre de tentatives réussies et le nombre total de tentatives dans une boîte de score.
* L'utilisateur peut cliquer sur un bouton 'Démarrer la pratique' pour commencer la session de pratique.
* L'utilisateur peut voir le mot de rappel affiché dans une boîte de texte.
* L'utilisateur peut commencer à taper le mot dans une boîte de saisie de texte.
* L'utilisateur peut voir les lettres qui ont été tapées clignoter si une lettre incorrecte est entrée et la boîte de saisie de texte sera effacée.
* L'utilisateur peut voir un message adjacent à la boîte de saisie de texte indiquant que l'utilisateur doit réessayer si une lettre incorrecte est entrée.
* L'utilisateur peut voir le nombre total de tentatives incrémenté dans la boîte de score.
* L'utilisateur peut voir un message de félicitations si le mot est correctement tapé.
* L'utilisateur peut voir l'intervalle de temps dans lequel les mots doivent être tapés diminué d'une petite quantité si le mot est correctement tapé.
* L'utilisateur peut voir le nombre de tentatives réussies incrémenté dans la boîte de score si le mot a été correctement tapé.
* L'utilisateur peut cliquer sur un bouton 'Arrêter la pratique' pour arrêter la session de pratique.

#### Fonctionnalités bonus

* L'utilisateur peut entendre un ton audible unique signalant lorsqu'un nouveau mot est affiché, qu'un mot est correctement entré, ou qu'une lettre incorrecte est tapée dans le mot.
* L'utilisateur peut se connecter à l'application
* L'utilisateur peut voir les statistiques de performance cumulatives sur toutes ses sessions de pratique.

#### Liens et ressources utiles

* [keydown](https://developer.mozilla.org/en-US/docs/Web/Events/keydown)
* [setInterval](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)

#### Exemples de projets

[Tuteur de frappe Twiddler](http://twiddler.tekgear.com/tutor/twiddler.html)

### 7. ASCENSEUR

**Niveau :** 3 — Avancé

Il est difficile d'imaginer un monde sans ascenseurs. Surtout si vous devez monter et descendre 20 étages chaque jour. Mais, si vous y réfléchissez, les ascenseurs étaient l'une des premières implémentations d'événements et de gestionnaires d'événements bien avant que les applications web n'apparaissent.

L'objectif de l'application Ascenseur est de simuler le fonctionnement d'un ascenseur et, plus important encore, comment gérer les événements générés lorsque les occupants du bâtiment l'utilisent. Cette application simule les occupants appelant un ascenseur depuis n'importe quel étage et appuyant sur les boutons à l'intérieur de l'ascenseur pour indiquer l'étage qu'ils souhaitent visiter.

#### Contraintes

* Vous devez implémenter un seul gestionnaire d'événements pour les boutons haut et bas à chaque étage. Par exemple, s'il y a 4 étages, un seul gestionnaire d'événements doit être implémenté plutôt que 8 (deux boutons par étage).
* De même, un seul gestionnaire d'événements doit être implémenté pour tous les boutons du panneau de contrôle dans l'ascenseur plutôt qu'un gestionnaire d'événements unique pour chaque bouton.

#### Histoires utilisateur

* L'utilisateur peut voir un diagramme en coupe d'un bâtiment avec quatre étages, une cage d'ascenseur, l'ascenseur, et un bouton haut au premier étage, des boutons haut et bas aux deuxième et troisième étages, et un bouton bas au quatrième étage.
* L'utilisateur peut voir le panneau de contrôle de l'ascenseur avec un bouton pour chacun des étages à côté du diagramme.
* L'utilisateur peut cliquer sur les boutons haut et bas à n'importe quel étage pour appeler l'ascenseur.
* L'utilisateur peut s'attendre à ce que le fait de cliquer sur les boutons haut et bas à n'importe quel étage pour demander l'ascenseur soit mis en file d'attente et traité dans la séquence où ils ont été cliqués.
* L'utilisateur peut voir l'ascenseur monter et descendre dans la cage jusqu'à l'étage où il a été appelé.
* L'utilisateur peut cliquer sur le panneau de contrôle de l'ascenseur pour sélectionner l'étage où il doit se rendre.
* L'utilisateur peut s'attendre à ce que l'ascenseur s'arrête pendant 5 secondes en attendant qu'un bouton d'étage sur le panneau de contrôle soit cliqué. Si un bouton d'étage n'est pas cliqué dans ce délai, l'ascenseur traitera la prochaine demande d'appel.
* L'utilisateur peut s'attendre à ce que l'ascenseur retourne au premier étage lorsqu'il n'y a plus de demandes à traiter.

#### Fonctionnalités bonus

* L'utilisateur peut voir une notification d'avertissement si le nombre de demandes d'ascenseur dépasse le nombre maximum autorisé. Cette limite est laissée au développeur.
* L'utilisateur peut entendre un son lorsque l'ascenseur arrive à un étage.
* L'utilisateur peut voir un occupant arriver aléatoirement à un étage pour indiquer quand l'utilisateur doit cliquer sur le bouton d'appel haut ou bas de l'ascenseur à cet étage.
* L'utilisateur peut spécifier l'intervalle de temps entre l'arrivée de nouveaux occupants pour appeler un ascenseur.

#### Liens et ressources utiles

[File d'attente premier entré, premier sorti (Wikipédia)](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics))

#### Exemples de projets

%[https://codepen.io/nibalAn/pen/prWdjq]

### 8. APPLICATION DE SIMULATION DE RESTAURATION RAPIDE

**Niveau :** 3 — Avancé

L'application de restauration rapide simule le fonctionnement d'un simple restaurant à emporter et est conçue pour aider le développeur à mettre en pratique ses connaissances des promesses et des principes de conception SOLID.

Cette application simule les clients d'un restaurant à emporter passant des commandes et attendant qu'elles soient préparées et livrées à un comptoir de retrait. Après avoir passé la commande, le client attend que la commande soit annoncée avant de la récupérer et de se rendre dans la zone de restauration.

Les histoires utilisateur qui composent cette application tournent autour de quatre rôles distincts :

* Utilisateur — l'utilisateur final utilisant l'application
* Client — le client simulé
* Preneur de commande — le preneur de commande simulé
* Cuisinier — le cuisinier simulé
* Serveur — le serveur simulé

Cette application a assez d'histoires utilisateur. Ne soyez pas submergé cependant. Prenez le temps de dessiner non seulement l'interface utilisateur, mais aussi comment les différents acteurs (rôles) interagissent et construisez l'application de manière incrémentielle en suivant les principes Agile.

#### Contraintes

* Les tickets de commande peuvent être représentés sous forme de deux types différents de promesses — une que le serveur attend pendant que le cuisinier prépare la commande et une autre que le client attend pendant qu'il est dans la file d'attente.
* Utilisez l'équivalent natif des promesses JS dans le langage que vous choisissez de développer. Les développeurs JS doivent utiliser des promesses natives et non `async/await`.
* Créez cette application en utilisant les fonctionnalités natives du langage. Vous ne pouvez PAS utiliser un package ou une bibliothèque de simulation.
* De nouveaux clients arrivent dans la file d'attente à un intervalle de temps fixe. En d'autres termes, de nouveaux clients arrivent à un rythme constant.
* Les tickets de commande sont remplis à un intervalle de temps fixe également. Ils sont complétés à un rythme constant.

#### Histoires utilisateur

**Fonctionnement de l'application**

* L'utilisateur peut voir une zone de saisie qui permet l'entrée de l'intervalle de temps pour l'arrivée des clients et un intervalle de temps pour l'exécution d'un _ticket de commande_ par le cuisinier.
* L'utilisateur peut voir un message d'avertissement personnalisé si l'intervalle d'arrivée des clients ou l'intervalle d'exécution de la commande est incorrectement entré.
* L'utilisateur peut démarrer la simulation en cliquant sur un bouton Démarrer.
* L'utilisateur peut voir une zone de file d'attente contenant une boîte de texte montrant le nombre de clients attendant pour passer des commandes.
* L'utilisateur peut voir une zone de commande contenant des boîtes de texte montrant le _numéro de commande_ actuellement pris.
* L'utilisateur peut voir une zone de cuisine contenant une boîte de texte montrant le _numéro de commande_ qui est en cours de préparation et une boîte de texte listant les commandes en attente dans l'ordre, ainsi qu'un compte du nombre de commandes en attente.
* L'utilisateur peut voir une zone de retrait contenant une boîte de texte montrant le _numéro de commande_ qui est actuellement disponible pour le retrait par le client et une boîte de texte montrant le nombre de clients attendant dans la file d'attente.
* L'utilisateur peut arrêter la simulation à tout moment en cliquant sur un bouton Arrêter.

#### Fonctionnalités bonus

* L'utilisateur peut spécifier combien de temps il faut à un preneur de commande pour créer un _ticket de commande_.
* L'utilisateur peut spécifier combien de temps il faut au serveur pour livrer une commande au client.
* L'utilisateur peut spécifier la durée totale de la simulation une fois le bouton Démarrer cliqué.
* L'utilisateur peut voir une vue animée des clients et des commandes alors qu'ils se déplacent dans le flux de travail.

#### Liens et ressources utiles

* [Simulateur de restauration rapide — Flux de travail logique](https://drive.google.com/file/d/1Thfm5cFDm1OjTg_0LsIt2j1uPL5fv-Dh/view?usp=sharing)
* [Manifeste Agile et 12 principes du logiciel Agile](http://agilemanifesto.org/)
* [Principes SOLID que chaque développeur devrait connaître](https://blog.bitsrc.io/solid-principles-every-developer-should-know-b3bfa96bb688)
* [Utilisation des promesses](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
* [Promesse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

### 9. JEU DE COQUILLAGES

**Niveau :** 3 — Avancé

Un jeu de coquillages est un jeu de hasard classique qui remonte à la Grèce antique. Pour y jouer, il faut trois coquillages, un pois, de la dextérité manuelle de l'opérateur et des compétences d'observation aiguisées de la part du joueur. C'est aussi un jeu de dupe classique puisque l'opérateur peut facilement escroquer le joueur. Heureusement, ce n'est pas notre intention avec cette application.

Ce jeu de coquillages est destiné à fournir une interface graphique au jeu de coquillages classique et à offrir au joueur un jeu honnête à jouer. Notre jeu dessine trois coquillages sur le canevas avec le pois, déplace le pois sous l'un des coquillages et mélange les coquillages pendant un intervalle de temps spécifique. L'utilisateur doit ensuite cliquer sur le coquillage sous lequel il pense que le pois est caché. L'utilisateur est autorisé à continuer à deviner jusqu'à ce que le pois soit localisé.

#### Histoires utilisateur

* L'utilisateur peut voir le canevas avec trois coquillages et le pois.
* L'utilisateur peut cliquer sur le coquillage sous lequel le pois doit être caché.
* L'utilisateur peut voir le pois se déplacer sous le coquillage qui a été cliqué.
* L'utilisateur peut cliquer sur un bouton 'Mélanger' pour démarrer un mélange animé des coquillages pendant 5 secondes.
* L'utilisateur peut cliquer sur le coquillage sous lequel il pense que le pois est caché lorsque l'animation s'arrête.
* L'utilisateur peut voir le coquillage qui a été cliqué s'élever pour révéler si le pois est caché dessous.
* L'utilisateur peut continuer à cliquer sur les coquillages jusqu'à ce que le pois soit trouvé.
* L'utilisateur peut voir un message de félicitations lorsque le pois est localisé
* L'utilisateur peut commencer une nouvelle partie en cliquant sur un coquillage sous lequel le pois doit être caché (étape #2 ci-dessus). Les étapes ci-dessus sont ensuite répétées.

#### Fonctionnalités bonus

* L'utilisateur peut voir un panneau de score contenant le nombre de victoires et le nombre de parties jouées.
* L'utilisateur peut voir le nombre de parties jouées augmenter lorsque le pois est caché sous un coquillage
* L'utilisateur peut voir le nombre de victoires incrémenté lorsque le pois est trouvé à la première tentative.
* L'utilisateur peut voir le coquillage cachant le pois s'animer (couleur, taille, ou un autre effet) lorsqu'il est cliqué (une bonne supposition).

#### Liens et ressources utiles

* [Jeu de coquillages (Wikipédia)](https://en.wikipedia.org/wiki/Shell_game)
* [Animation HTML DOM JavaScript](https://www.w3schools.com/js/js_htmldom_animate.asp)
* [Bibliothèque d'animation p5js](https://p5js.org/)

#### Exemples de projets

%[https://codepen.io/RedCactus/pen/dwEjXy]

### Conclusion

N'oubliez pas de consulter l'[article précédent](https://www.freecodecamp.org/news/here-are-some-app-ideas-you-can-build-to-level-up-your-coding-skills-39618291f672/) et le [dépôt](https://github.com/florinpop17/app-ideas) si vous souhaitez trouver plus d'idées d'applications/projets.

De plus, si les informations de cet article et du dépôt vous ont été utiles d'une manière ou d'une autre, assurez-vous de lui donner une étoile ? ; ainsi, d'autres pourront le trouver et en bénéficier également ! Merci !

Avez-vous des suggestions sur la manière dont nous pourrions améliorer ce projet dans son ensemble ? Faites-le nous savoir ! Nous serions ravis d'avoir votre retour !

Vous êtes invité à contribuer avec vos propres idées ! Nous pouvons faire de ce dépôt la ressource incontournable en matière d'idées d'applications.

_Publié à l'origine sur [www.florin-pop.com](https://www.florin-pop.com/blog/2019/04/more-project-ideas-to-improve-your-coding-skills/)._