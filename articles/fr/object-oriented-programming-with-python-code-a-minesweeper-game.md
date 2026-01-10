---
title: Programmation Orientée Objet avec Python – Codez un Jeu Démineur
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-04-18T19:46:59.000Z'
originalURL: https://freecodecamp.org/news/object-oriented-programming-with-python-code-a-minesweeper-game
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/minsweeper.png
tags:
- name: Python
  slug: python
- name: youtube
  slug: youtube
seo_title: Programmation Orientée Objet avec Python – Codez un Jeu Démineur
seo_desc: 'Improve your Python programming skills by coding everyone''s favorite Windows
  3.1 game: Minesweeper.

  We just published a Python course on the freeCodeCamp.org YouTube channel that will
  teach you how to code Minesweeper using the tkinter library.

  Jim f...'
---

Améliorez vos compétences en programmation Python en codant le jeu préféré de Windows 3.1 : Démineur.

Nous venons de publier un cours Python sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à coder Démineur en utilisant la bibliothèque tkinter.

Jim de JimShapedCoding a développé ce cours. Il a publié de nombreux cours de programmation populaires à la fois sur la chaîne freeCodeCamp et sur sa propre chaîne.

Le jeu est entièrement implémenté en utilisant la Programmation Orientée Objet.

Voici les sections couvertes dans ce tutoriel :

* Commencer
* Créer des Cellules & des Mines
* Algorithmes de Démineur
* Afficher les données du jeu
* Touches finales et jouer au jeu

![Image](https://www.freecodecamp.org/news/content/images/2022/04/minesweeper-mine.gif)
_Démineur (mais pas la version que vous allez créer)_

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/OqbGRZx4xUc) (3 heures de visionnage).

%[https://youtu.be/OqbGRZx4xUc]

## Transcription

(générée automatiquement)

Dans ce cours, Jim vous aidera à améliorer vos compétences en Python en vous apprenant à construire un jeu de démineur.

Jim a créé de nombreux cours populaires sur notre chaîne et est un excellent enseignant.

Il vient de commencer à apprendre Python et vous voudrez développer un projet cool après avoir appris les bases.

Eh bien, cette série de vidéos est exactement pour vous, car dans cette série de vidéos, nous allons développer un jeu avec Python.

Maintenant, si vous connaissez les bases et que vous avez suivi un cours de base, peu importe la chaîne ou le cours, alors c'est la série que vous recherchez, car elle vous donnera les bases de la façon de commencer à structurer un projet Python.

Maintenant, dans cette série, nous allons développer un jeu qui s'appelle Démineur, qui est connu comme un jeu pour un seul joueur très amusant à jouer et aussi stimulant.

Voyons quel jeu vous allez apprendre à développer dans cette série.

D'accord, donc ce sera le jeu que nous allons développer tout au long de la série.

Maintenant, nous pouvons voir que nous avons une certaine quantité de cellules sur lesquelles nous pouvons cliquer et les ouvrir.

L'objectif principal dans Démineur est de ne pas cliquer sur une cellule qui a une mine derrière la cellule.

Donc, ce que cela signifie, c'est que si j'allais ouvrir cela, alors vous pouvez voir que je reçois un nombre en retour.

Cela signifie que dans les cellules environnantes de cette cellule, il y a une mine sur laquelle je ne devrais pas cliquer.

Donc, je vais deviner et dire que vous n'avez pas de mine ici.

Et vous n'avez pas non plus de mine là.

Et vous pouvez voir que j'ai tout à fait raison.

Donc, je vais cliquer avec le clic droit de la souris pour la marquer comme une mine, car si j'allais cliquer dessus avec le clic gauche de la souris, alors j'allais perdre le jeu, n'est-ce pas.

Donc, ce que je vais faire maintenant, c'est essayer d'obtenir le reste des emplacements qui sont des emplacements sans mine, donc je vais cliquer ici.

Et vous pouvez voir que j'ai reçu quelques nombres, vous pouvez voir que, par exemple, autour de la cellule, j'ai zéro mine, donc il est sûr de cliquer ici, ici et ainsi que là.

Et maintenant, essayons de cliquer gauche sur cet emplacement.

Et vous pouvez voir qu'il dit que vous avez cliqué sur une mine et j'ai perdu un jeu.

Et l'objectif principal est vraiment d'obtenir tous les emplacements qui n'ont pas de mine et alors vous gagnerez le jeu.

Donc, cela va être beaucoup de réflexion que nous devons faire afin de développer ce jeu.

Et ce sera cool de traiter tous les défis que ce jeu apporte avec lui.

Donc, avant de commencer, j'apprécierais si vous pouvez cliquer sur le bouton like de cette vidéo, cela aidera à diffuser la vidéo sur tout YouTube.

Et aussi, si vous connaissez des personnes qui commencent tout juste à apprendre Python et qu'elles veulent développer un projet cool, alors invitez-les à regarder ma série également, cela pourrait être très utile pour ces vidéos qui sont juste au niveau entre le début et devenir un expert.

Donc, cela dit, commençons.

Maintenant, avant de nous lancer dans l'écriture de ce projet, je m'attends à ce que vous ayez Python installé sur votre ordinateur.

Et ainsi qu'un IDE prêt à l'emploi qui reconnaît l'interpréteur Python sur votre ordinateur, je vais utiliser Python 3.8.

Mais tant que vous avez une version supérieure à celle-ci, alors vous devriez être en mesure d'écrire ce projet.

Maintenant, nous n'allons pas utiliser trop de bibliothèques externes, ou trop de code qui dépend de la version de Python.

Donc, ce n'est pas grave, si vous utilisez même Python trois point 10 ou Python trois point 11 qui sortira probablement dans le futur.

Très bien.

Donc, allons-y et commençons.

Maintenant, pour écrire un jeu de plateau en 2D, nous pouvons utiliser beaucoup de bibliothèques disponibles en Python.

Dans celui-ci, nous allons utiliser TK inter qui est très bien et une excellente bibliothèque à pratiquer car elle vient avec beaucoup de classes utiles que nous allons instancier pour créer notre fenêtre.

Donc, nous allons commencer par importer cela de la manière suivante.

Donc, je vais dire from tkinter, import everything.

Et cela sera un excellent début pour nous.

Donc, la ligne suivante que je vais écrire ici est d'instancier une instance de fenêtre.

Et nous voulons probablement faire cela parce que notre projet va être dans une fenêtre, et je vais nommer ma variable root et celle-ci va être égale à une instanciation de ce rôle clé le T K.

Et c'est juste les éléments les plus basiques que vous pouvez créer.

C'est juste une fenêtre régulière.

Maintenant, lorsque nous allons exécuter cela, rien ne va se passer car nous devons dire à ce TK qu'il devrait s'exécuter jusqu'à ce que nous le fermions avec le bouton X en haut à droite.

Donc, ce sera en disant route dot main loop comme cela, n'est-ce pas.

Donc, nous devons appeler cette méthode et tout le code va être entre ces deux lignes.

Donc, si nous devions exécuter cela, et vous pouvez voir que nous avons la fenêtre la plus basique qui soit possible.

Maintenant, juste une petite note, la raison pour laquelle j'ai utilisé la variable root est juste une convention dans les projets TK inter.

Donc, il sera plus facile pour vous de chercher des problèmes sur Stack Overflow.

Par exemple, si vous suivez ces conventions ou alors allons-y et voyons quelques-uns des attributs que nous pouvons changer ici pour rendre notre fenêtre plus belle.

Donc, le premier sera évidemment de changer la taille de la fenêtre.

Et nous pouvons faire cela en appelant la fonction geometry, je veux dire la méthode de cette route.

Et cela accepte une chaîne qui ressemble à ce qui suit : largeur, X, la hauteur.

Et ici, évidemment, vous pouvez mettre n'importe quels nombres que vous aimeriez maintenant, faites attention à ce qui va se passer si j'allais remplacer ceux-ci par des nombres réels comme les suivants, alors vous verrez la différence immédiatement.

Et si j'allais exécuter cela, alors vous pouvez voir comment cela change.

Maintenant, nous pouvons aussi faire attention qu'il utilise cette chaîne comme titre de notre fenêtre, nous pouvons changer cela en appelant une méthode qui s'appelle Title et lui donner n'importe quel titre que nous aimerions.

Donc, nous pouvons opter pour un jeu de démineur, et réexécuter notre programme.

Et vous pouvez voir les changements.

Maintenant, je n'ai pas parlé de cela.

Mais par défaut, toutes les fenêtres sont redimensionnables.

Et cela pourrait être quelque chose d'ennuyeux lorsque vous créez beaucoup d'éléments à l'intérieur de cette fenêtre comme des boutons ou des cadres.

Donc, c'est pourquoi nous cherchons probablement à éviter de redimensionner cette fenêtre, car cela nous donnera simplement une vie plus facile lorsque nous allons ajouter d'autres éléments dans cette fenêtre.

Donc, la manière dont cela est réalisable, est en appelant la méthode redimensionnable comme cela, et en spécifiant essentiellement que nous ne sommes pas autorisés à redimensionner la largeur et la hauteur de cette fenêtre.

Et cela est réalisable en passant essentiellement false deux fois, une pour le poids, et l'autre pour la hauteur.

Maintenant, si j'allais à nouveau, réexécuter notre programme, alors vous pouvez voir l'effet de cela, vous pouvez voir que ce maximiser ici est désactivé.

Et c'est juste quelque chose qui va nous faciliter la vie à l'avenir lorsque nous développerons ce jeu.

Maintenant, après avoir atteint ce stade, alors nous pourrions aussi être curieux de savoir comment changer la couleur de fond de notre fenêtre.

Maintenant, vous pourriez utiliser des valeurs hexadécimales si vous savez comment les utiliser.

Mais essentiellement, cela donne un support à beaucoup de mots-clés pour spécifier les couleurs.

Maintenant, nous ne voulons pas trop nous occuper du style, nous voulons surtout nous concentrer sur la logique et l'algorithme de la façon d'écrire un tel jeu.

Donc, à cette fin, je vais garder cela simple.

Mais encore, nous voulons évidemment avoir une fenêtre visualisée agréable ici.

Donc, je vais aller à cette cinquième ligne.

Et je vais dire router dot Configure.

Et nous allons devoir configurer la couleur de fond pour notre fenêtre.

Donc, nous devons aller de l'avant et appeler cette méthode et nous devons passer en BG égal à n'importe quelle couleur que nous aimerions.

Maintenant, dans la description, vous pouvez trouver une liste de couleurs qui sont disponibles en utilisant des mots-clés de couleurs.

Donc, dans la description, il y a un lien avec une grande liste de couleurs disponibles, je vais juste utiliser le noir pour cette fenêtre.

Et cela sera ajouté pour que vous puissiez voir l'effet immédiat du changement de la couleur de fond.

D'accord, donc maintenant que nous avons compris cela, alors allons-y et voyons comment nous pouvons créer quelques éléments à l'intérieur de notre fenêtre.

Maintenant, nous allons commencer avec les éléments les plus basiques que vous pouvez créer dans une fenêtre, qui s'appelle un cadre.

Maintenant, un cadre est juste comme un conteneur qui pourrait contenir plus d'éléments que nous créerons à l'avenir.

Maintenant, nous voulons utiliser ces cadres, car évidemment nous voulons diviser notre fenêtre en quelques sections.

Donc, il sera plus facile de comprendre où nous voulons localiser chacun de nos boutons ou textes à l'avenir.

Par exemple, nous pourrions dédier cette zone de notre fenêtre pour un titre, donc nous aurons le titre ici.

Et nous pourrions décider que nous aimerions avoir une barre latérale gauche.

Donc, nous pourrions dédier la zone gauche de notre fenêtre à être la barre latérale pour afficher le score, par exemple, quelque chose comme cela.

Et nous pourrions avoir un autre cadre ici.

Donc, nous appelons afficher le jeu ici.

Donc, c'est juste une excellente idée de diviser la fenêtre en plusieurs cadres, cela va être juste utile pour visualiser différents éléments plus tard.

Donc, ce que je vais faire maintenant, c'est écrire ici un commentaire qui dira override the settings of the window.

Et juste avant le root.me loop, je vais aussi commenter run the window et ensuite ici est l'emplacement exact où nous allons commencer à créer quelques cadres.

Donc, allons-y et commençons.

Donc, nous avons dit que nous aimerions avoir un cadre qui est situé en haut.

Donc, je vais nommer cette variable top frame et cela sera égal à une classe qui est nommée frame.

Et une fois que nous allons instancier à partir de cette classe de cadre, alors elle sera responsable d'instancier un cadre que nous déciderons plus tard où nous aimerions le localiser sur nos fenêtres.

Maintenant, le premier argument que ce cadre doit recevoir est l'élément dans lequel nous aimerions localiser le cadre.

Donc, il sera localisé dans la fenêtre.

Donc, nous allons passer root.

Et puis je vais séparer ceux-ci en plusieurs lignes.

Donc, il sera plus facile à lire.

Et comme vous pouvez le voir, les parenthèses sont ouvertes ici, fermées ici.

Maintenant, allons-y et donnons-lui plus d'attributs.

Donc, première chose, nous aimerions donner un fond différent.

Donc, nous pouvons vraiment différencier entre le cadre et la fenêtre car il sera difficile de comprendre où le cadre est localisé, si nous gardons la même couleur, donc juste pour des raisons de débogage, je garde ce rouge à changer plus tard en noir.

Et nous allons commenter cela ici.

Et puis ici, je vais décider du poids et de la hauteur.

Donc, je vais dire que le poids devrait être égal à la même taille de largeur que nous avons donnée à la fenêtre car nous aimerions couvrir toute la fenêtre.

Donc, cela devrait être le poids entier, comme la fenêtre, et la hauteur devrait probablement être de 180 pixels comme cela.

Donc, c'est juste sept sur 20 divisé en 20, cela a totalement du sens.

Et maintenant que nous avons cela, alors nous devons décider où nous aimerions commencer ce cadre.

Donc, afin de faire cela, alors je vais aller de l'avant et dire top underscore frame dot place.

Maintenant, cette place recevra deux arguments qui sont obligatoires.

Et avant d'aller de l'avant et de passer ceux-ci, laissez-moi vous montrer comment le placement fonctionne dans la fenêtre ici.

Donc, lorsque nous utilisons le placement, alors il doit recevoir la valeur des pixels.

Maintenant, nous savons que nous avons un cadre que nous aimerions commencer exactement à partir d'ici.

Et nous savons qu'il devrait probablement couvrir cette zone, n'est-ce pas.

Mais comment allons-nous lui dire de commencer à partir d'ici.

Eh bien, dans place, nous devons spécifier l'axe x et l'axe Y, ce qui signifie que si nous voulons commencer à partir du coin supérieur gauche, alors nous devons lui donner les valeurs de 0.0.

Parce que c'est là que tout commence en termes de pixels.

Maintenant, toute la zone ici est de 1400 pour le parce que c'est l'axe x et l'axe y est de 720 pixels.

Donc, toute la hauteur ici est de 720.

Maintenant, si par exemple, nous voulions avoir un bouton juste pour exemple, je ne vais pas faire cela à ce moment-là.

Mais disons que nous aimerions avoir un bouton que nous voulions commencer ici.

Donc, nous voulions le placer au milieu de notre page, n'est-ce pas, donc nous devons prendre cette valeur et la diviser par deux, donc l'axe x est de 720.

Et nous savons que nous aimerions l'avoir dans la position supérieure autant que possible.

Donc, ce devrait être la valeur de l'axe y qui sera zéro.

Donc, c'est ainsi que fonctionne la méthode place, nous devons spécifier la valeur des pixels pour l'axe x et l'axe y.

Et laissez-moi nettoyer tout ce que j'ai dessiné ici et revenir à Python et donner ici les valeurs de x égal à zéro et y égal à zéro.

Et maintenant, vérifiez comment ce cadre sera visualisé.

Si je stoppe et réexécute, alors vous pouvez voir que c'est le résultat attendu, exactement comme nous le voulions, il a commencé à partir d'ici et a pris toute la zone de poids, et il a pris 180 pixels de la hauteur.

Donc, c'est exactement ce que nous voulons maintenant, juste pour vraiment nous assurer que vous avez compris cela, je vais changer cela en x à 20.

Et vous allez deviner ce qui va se passer.

Donc, si nous devions lire cela, alors évidemment, cela va commencer à partir d'une position légèrement à gauche, vous pouvez voir où il est situé, il commence juste ici.

Et si nous devions sauter à y par 20 et arrêter et réexécuter cela, alors vous pouvez voir les résultats.

Donc, c'est ainsi que fonctionne la méthode place.

Évidemment, je vais changer ceux-ci en zéro et continuer à partir d'ici.

D'accord, donc maintenant que nous avons compris cela, alors allons-y et essayons de créer un autre cadre.

Cette fois, je veux faire un cadre que nous utiliserons comme une barre latérale gauche, où nous afficherons peut-être le score ou autre chose qui est utile.

Donc, je vais aller de l'avant et créer une variable left frame et cela va être égal au cadre.

Donc, nous allons instancier un autre à partir de cette classe.

Et nous voulons ce cadre dans le brut et puis nous allons dire quelque chose comme BG égal à une autre couleur.

Je vais juste copier cette ligne et la coller dans un et utiliser quelque chose comme bleu pour que nous puissions séparer entre différents cadres, et le poids sera de 360, j'utilise intentionnellement la valeur qui est juste un quart de cette valeur.

Donc, il sera plus facile pour moi de comprendre combien de pourcentage de la largeur totale j'ai couvert avec mes cadres.

Maintenant que j'ai spécifié la largeur, je vais spécifier la hauteur.

Donc, je vais dire que cela devrait couvrir toute la hauteur de notre fenêtre.

Maintenant, faites attention que nous avons déjà couvert 100 pixels pour le cadre supérieur.

Donc, nous ne pouvons pas simplement dire 700, je veux dire, sept et 20.

Comme cela, nous devons aller de l'avant et nous souvenir de la taille de hauteur de toute la fenêtre et soustraire ce nombre par ce nombre, n'est-ce pas.

Donc, nous devrions passer ici 500.

Pour l'instant, ne vous inquiétez pas si vous pensez que nous avons trop de valeurs codées en dur, je vais m'assurer que nous n'avons pas vraiment de valeurs codées en dur plus tard, lorsque nous restructurerons ce projet à l'avenir.

Donc, maintenant nous nous concentrons sur la compréhension de la façon dont TK inter fonctionne.

Donc, maintenant que nous avons compris cela, alors allons-y et disons que le cadre gauche devrait être placé en x égal à zéro, mais le y devrait être égal à 180, n'est-ce pas, parce que nous voulons le commencer juste après l'endroit où le cadre supérieur est situé.

Et si j'allais exécuter notre programme, alors vous pouvez voir que nous avons le résultat parfait.

Juste pour vraiment comprendre cela à nouveau, si nous devions prendre cet axe Y et sauter cela de 20, alors vous pouvez voir que cela commence juste à partir d'ici, parce qu'il a sauté 20 pixels dans l'axe Y.

Donc, c'est pourquoi je veux m'assurer que nous gardons la valeur de 100.

D'accord, donc maintenant que nous avons atteint ce stade, vous pouvez probablement remarquer que nous allons avoir trop de nombres codés en dur en termes d'utilisation de la largeur et de la hauteur et des pixels, etc.

Donc, c'est un bon moment pour avoir un fichier séparé pour toutes nos constantes, et avoir au moins quelques variables stockées quelque part.

Maintenant, je ne vais pas faire cela dans notre fichier main.py, car cela pourrait être trop d'informations qui doivent être stockées dans un seul fichier, à part cela, je vais créer un nouveau fichier Python, et je vais l'appeler settings.

Donc, à l'intérieur, je peux utiliser quelques constantes qui seront utiles.

Et pour vraiment vous montrer ces fenêtres côte à côte, laissez-moi utiliser le clic droit et l'option diviser verticalement.

Donc, nous pouvons commencer à penser à quelques bons candidats pour les variables que nous aimerions stocker ici.

Par exemple, nous pouvons commencer par la taille de la largeur de notre fenêtre, nous pouvons dire que la largeur est égale à 1440, nous pouvons dire que la hauteur est égale à 720.

Et nous pouvons immédiatement revenir à notre fichier main.py et dire quelque chose comme import settings.

Et puis nous pourrions aller ici et utiliser une chaîne formatée.

Et nous pourrions simplement convertir ceux-ci en cette chaîne, n'est-ce pas, nous pouvons dire ici, settings, dot width.

Et nous pouvons aller avec settings dot height, comme cela.

Et c'est juste un grand changement dans notre projet.

Maintenant, si j'allais exécuter notre fichier principal, alors vous pouvez voir que rien n'est vraiment changé.

Et nous sommes en bonne position pour continuer à faire ces manipulations pour stocker plus de variables.

Maintenant, si vous vous souvenez, j'ai dit dans le tutoriel que j'ai utilisé intentionnellement ces nombres, afin que nous puissions avoir un pourcentage précis de la taille du poids.

Par exemple, il y avait une bonne raison que j'utilise la valeur de 100 dans la hauteur des cadres supérieurs, car l'un des temps pour est similaire à 20.

Donc, je peux dire que j'aime consommer 25% de la hauteur totale de notre fenêtre.

Et ce sont des choses qui sont importantes car nous n'aurons pas trop de valeurs codées en dur.

Donc, ce que nous pouvons faire maintenant, c'est avoir un fichier pour certaines fonctions qui pourraient être utiles pour calculer ces choses.

Par exemple, nous pourrions avoir une fonction qui calculera combien font 20% de la hauteur totale de notre fenêtre, n'est-ce pas ? Donc, nous pouvons aller de l'avant et utiliser un autre fichier Python pour cela.

Nous pouvons l'appeler utilities ou utils.

Et nous pourrions avoir une fonction qui calculera le montant en pourcentage de notre hauteur.

Tout d'abord, nous pourrions aller de l'avant et utiliser import settings afin que nous importerons les paramètres de notre projet.

Et nous pourrions aller de l'avant et utiliser une fonction.

Donc, appelons cette fonction height underscore PRC T, juste une version abrégée de pourcentage, n'est-ce pas, donc nous pourrions aller de l'avant et recevoir ici, le montant en pourcentage comme paramètre, nous rendons cela un peu plus petit.

Et puis je peux juste aller de l'avant et à l'intérieur de cela, je peux retourner la valeur en fonction de l'argument reçu ici.

Donc, je peux aller de l'avant et utiliser return.

Et je peux dire, settings dot height, divisé par 100.

Et je peux couvrir cette chose avec des parenthèses.

Et je peux multiplier cela par le montant en pourcentage.

Maintenant, je veux valider que j'ai fait un excellent travail d'écriture de cette fonction, n'est-ce pas, je ne veux pas immédiatement appeler mes fonctions, et juste essayer de les utiliser car je pourrais avoir un bug lorsque j'écris une fonction.

Et c'est aussi un grand avantage de localiser différentes fonctions dans différents fichiers, car cela vous donnera un énorme avantage de déboguer vos trucs.

Par exemple, je pourrais temporairement exécuter uniquement le fichier utils.py et juste tester ma fonction, je pourrais aller de l'avant et essayer de l'appeler et passer il 25.

et valider que je vais vraiment recevoir 100 ad en retour.

Donc, je peux aller de l'avant et utiliser print, et exécuter utils.

Donc, je n'exécute pas mon projet original.

Et maintenant, si vous allez de l'avant et que vous voyez la valeur ici, vous pouvez voir que je reçois vraiment un ad.

Et c'est bien.

Cela signifie que nous avons fait un excellent travail d'écriture de cette fonction.

Et maintenant, je peux vraiment commencer à l'utiliser dans notre projet original, c'est-à-dire dans le fichier main.py, donc je peux aller de l'avant et importer également le fichier utils, je peux dire import utils.

Et je peux aller de l'avant et appeler la fonction de pourcentage de hauteur, je peux utiliser utils dot height, PRT CT et passer 25.

Et encore une fois, cela n'aura aucun effet.

Cela signifie que nous avons fait un excellent travail, seulement maintenant nous sommes plus dynamiques et nous ne codons pas en dur les valeurs.

Nous allons nous répéter avec le poids très rapidement.

Et puis nous passerons au sujet suivant, n'est-ce pas, donc je vais aller ici, et je vais utiliser cette hauteur, je veux dire le poids, PR city, nous allons recevoir à nouveau le pourcentage, et nous allons dire return open parenthèse juste pour que nous puissions avoir un look plus propre dans cette formule.

Et nous pouvons dire settings dot width divisé en 100 multiplié par le présent âge.

Donc maintenant, je peux aller de l'avant et faire à peu près la même chose dans les différentes valeurs codées en dur ici.

Donc, jetons un coup d'œil.

Donc, dans le cadre supérieur, nous utilisons toute la fenêtre.

Donc, il est logique de changer cela juste à la valeur de settings dot width, n'est-ce pas, car il est déjà 1440.

Allons à notre cadre gauche.

Donc, dans le cadre gauche, nous voyons que nous utilisons 25% de la largeur totale.

Donc, nous pouvons aller de l'avant et utiliser utils dot height PR CT, excusez-moi, avec brct je vais changer cela.

Et puis je vais passer 25.

Et vous pouvez aussi voir que dans la hauteur, nous utilisons 75% de notre hauteur totale.

Donc, cela signifie que je peux juste utiliser ici utils dot height Poct et passer 75.

Et je peux faire la même chose lorsque je veux localiser mon cadre gauche.

Et vous pouvez remarquer comment la valeur de l'axe y ici est à nouveau 25% de la hauteur totale.

Donc, je peux dire utils dot height brct et passer ici 25%.

Maintenant, voyons si nous avons fait un excellent travail, vous pouvez voir que le résultat est à nouveau parfait.

D'accord, donc maintenant que nous avons cela, alors laissez-moi changer ceux-ci aux valeurs originales et continuer à partir d'ici pour créer notre dernier cadre ici.

Donc, nous avons dit que nous aimerions avoir aussi un autre cadre qui va être au centre de notre page.

Donc, nous aurons un cadre qui sera dédié à notre jeu, n'est-ce pas.

Donc, je vais rapidement aller de l'avant et créer un cadre central qui sera à nouveau égal à un cadre et celui-ci devrait être à l'intérieur de la racine, le fond devrait être peut-être vert pour que nous puissions le séparer.

Je devrais changer tous ceux-ci en noir dans quelques minutes.

Et puis j'aimerais dire que le poids est égal à utils dot weight PR city et cette fois j'aimerais utiliser 75% de notre largeur totale et la hauteur va être à nouveau utils dot height ferocity et cela sera 75 pour cent également, maintenant la méthode place recevra les arguments suivants.

Donc, la valeur x devrait être utils dot with PRC at 25%.

Parce que nous voulons le commencer à partir d'ici, et la hauteur, c'est-à-dire l'axe y devrait être la même, n'est-ce pas, donc je vais dupliquer cela, et Y et changer cela en height periodicity.

Comme cela, parce que nous voulons que celui-ci commence à partir d'ici, n'est-ce pas, donc il va prendre 360 pixels de la gauche, et 180 pixels du haut.

Donc, maintenant, si nous devions tester notre code, alors vous allez voir que nous avons juste le résultat attendu.

Donc, maintenant, c'est un bon moment pour changer nos cadres en noir.

Parce que nous avons fait un excellent travail, nous pouvons aller de l'avant et changer ceux-ci en noir.

Maintenant, ce que vous allez voir, c'est juste une fenêtre qui ressemble à une fenêtre purement noire.

Mais en arrière-plan, dans le code Python réel, nous avons deux cadres qui sont divisés, exactement comme nous le voulions.

Donc, maintenant que j'ai changé tout l'arrière-plan en chose noire, nous allons juste voir la même chose.

Mais en arrière-plan, dans le code original, nous avons vraiment deux cadres, je veux dire trois cadres, d'accord, jusqu'à ce point, nous savons que nous avons un cadre ici.

Et nous avons aussi un cadre qui est ici.

Maintenant, nous avons dit qu'autour d'ici, nous allons écrire quelques informations sur le jeu.

Et ici, nous aurons le titre Démineur comme cela, n'est-ce pas.

Mais ce que nous voulons faire ici au centre, c'est en fait développer le tableau, n'est-ce pas, chaque cellule sur laquelle un joueur va cliquer devrait être ici.

Et ici, nous devrions localiser toutes nos cellules.

Maintenant, créer 36 cellules codées en dur ou 49 cellules, essentiellement juste une énorme quantité de ventes va être difficile.

Donc, voici l'emplacement exact où nous voulons rendre nos trucs un peu plus dynamiques, nous voulons pouvoir aller de l'avant et faire une boucle for qui ira de l'avant et créera ces types de cellules dynamiquement.

Maintenant, nous voulons aussi faire un comportement pour chaque vente, le genre de comportement de bouton appelé parce que nous voulons la capacité de cliquer sur quelque chose.

Et ensuite, la chose suivante est quelque chose qui se passera dans le jeu, n'est-ce pas, nous verrons quelques informations sur cette vente.

Donc, c'est le moment exact pour créer une classe que nous pouvons nommer cellule parce que nous savons que pour chaque cellule, nous aimerions aussi donner quelques attributs comme si la cellule est une mine ou non.

Ou si c'est une cellule qui est déjà ouverte ou qui est fermée.

Donc, c'est exactement le moment où c'est une excellente idée de penser à créer une classe que nous pourrions nommer Sal.

Et nous pourrions créer quelques instances de cela plus tard.

Maintenant, juste comme un exemple rapide, je vais supprimer cela après que je vais vous montrer l'exemple de base.

Mais voici comment vous pouvez créer un bouton sur une fenêtre en utilisant la bibliothèque TK Inter, n'est-ce pas, donc utilisons une variable aléatoire comme button one.

Et cela sera égal à button comme cela.

Maintenant, ce bouton va recevoir plusieurs arguments.

Disons que nous voulons que cela soit à l'intérieur de notre cadre central.

Et nous voulons donner la couleur de fond bleue.

Et donnons-lui un texte.

Désolé pour la virgule manquante ici.

Donnons-lui un texte comme premier bouton.

Et puis ce que je vais faire maintenant, c'est dire button one dot place, nous allons le placer dans le premier pixel de l'axe x et de l'axe y dans le cadre central.

Donc, il devrait être dans la position tout en haut à gauche de ce cadre central, n'est-ce pas.

Donc, si nous allions de l'avant et exécutions cela, alors vous pouvez voir que j'ai un bouton juste là et il est cliquable.

Maintenant, nous savons que nous voulons l'abstraire avec notre classe personnalisée car nous devons donner à cette cellule, appelée, quelques attributs comme je l'ai décrit plus tôt.

Donc, c'est pourquoi je veux créer une classe de cellule.

Et puis nous verrons aussi comment la classe de bouton va être impliquée dans cette classe de cellule que nous allons commencer à développer, mais allons-y et commençons à travailler sur cela maintenant.

Donc, je voulais juste vous montrer comment créer un bouton avant d'aller de l'avant et d'écrire un peu plus de code.

Donc, je vais aller ici et créer un fichier cell.py et je vais zoomer un peu pour que tout le monde puisse voir et je vais utiliser class.

Donc, maintenant temporairement, je ne veux pas hériter de la classe de bouton car ce n'est pas tout à fait correct de dire qu'une cellule est une sorte de bouton, nous savons que nous utilisons l'héritage pour décrire des types de choses comme un chien est une sorte d'animal.

Donc, la classe de chien devrait hériter d'une classe qui est une classe d'animal.

Mais ce n'est pas exactement le cas que vous allez.

Donc, je ne fais pas cela.

Et maintenant que j'ai créé cette classe, allons-y et écrivons le constructeur de notre classe.

Maintenant, comme nous le savons, le constructeur est une méthode qui va être appelée immédiatement une fois qu'une classe est instanciée.

Maintenant, je vais recevoir temporairement ici un paramètre, auquel je vais également fournir une valeur par défaut de false.

Et vous pouvez voir qu'il est appelé is mine, n'est-ce pas, et je vais dire self.is underscore mine est égal à is underscore mine, comme suit.

D'accord, donc maintenant que nous avons cela, voyons comment nous allons l'utiliser dans notre code.

Donc, je vais aller à mon fichier main.py.

Et nous allons faire défiler juste au-dessus de ce commentaire ici, exécuter la fenêtre.

Et j'aurai besoin d'importer la classe à coup sûr.

Donc, allons-y et utilisons from cell qui est le fichier, import the sale class comme cela, n'est-ce pas, et je vais juste le placer dans cette ligne.

Donc, nous aurons un look plus propre.

Et maintenant, je vais aller ici, et je vais juste dire c one est égal à sell.

Et puis je vais juste le laisser tel quel car il a une valeur par défaut de false.

Et maintenant que j'ai cela, alors je peux juste aller de l'avant et l'exécuter.

Et vous pouvez voir que la classe, l'instanciation est probablement bonne car nous ne recevons aucune flèche.

Maintenant, évidemment, nous ne voyons aucun bouton ici car nous avons juste créé une classe personnalisée sans la relier à la classe de bouton qui provient de cette bibliothèque TK inter.

Donc, maintenant, c'est exactement ce que nous allons faire.

Oui, nous allons aller à notre fichier cell, et nous allons créer une instance de bouton qui va appartenir à chaque objet de cellule.

Donc, ce que cela signifie, c'est que ce self va recevoir un attribut supplémentaire que nous pourrions nommer cell button object, quelque chose comme cela.

Et puis nous allons lui assigner un objet bouton.

Et c'est ainsi que la relation entre les objets de vente et l'objet bouton va être accomplie.

Donc, première chose, je vais fermer le jeu temporairement.

Et je vais aller ici et dire from T A inter import.

Vous savez quoi, importons juste la classe bouton.

N'utilisons pas une importation wildcard ici.

Et maintenant, je vais aller de l'avant et dire que cela devrait être égal à none au début.

Et puis ce que nous allons faire maintenant, c'est créer une méthode d'instance qui créera ce bouton pour nous et je l'assignerai à self dot sale button object.

Jetons un coup d'œil à la façon dont nous allons faire cela.

Donc, je vais dire Create button object.

Et nous allons recevoir self seulement pour l'instant.

Et nous allons dire ici button est égal à un bouton comme cela.

Et nous instancions simplement une instance de cette classe de bouton.

Maintenant, actuellement, nous ne recevons aucun paramètre supplémentaire autre que le self, qui est obligatoire dans les méthodes d'instance.

Donc, nous devons recevoir au moins un paramètre qui est assez important, que nous pouvons nommer location, car nous savons que pour chaque élément que nous aimerions créer dans notre fenêtre, nous devrions passer une pièce d'information qui fera comprendre à TK inter où il devrait localiser cet élément.

Donc, si nous recevons un paramètre qui est appelé location, alors je peux simplement passer la location directement.

Et puis chaque fois que j'appelle cette méthode, je ferai référence au capteur de cadre réel qui sera issu du main.py.

C'est pourquoi je reçois ici le paramètre location, n'est-ce pas.

Et juste pour un exemple temporaire, donnons-lui aussi un texte aléatoire comme text comme cela juste comme un débutant.

Et puis je vais dire que self dot sale btn object va être égal à l'objet du bouton que je viens de créer.

Et cela va être utile car cela m'aidera à personnaliser ce bouton une fois que j'aurai assigné ces attributs à un objet bouton, et vous allez voir juste dans une minute comment cela va être extrêmement utile.

Donc, allons-y et divisons maintenant verticalement pour que nous puissions comprendre ce que nous avons fait ici.

Donc, du côté gauche, nous avons le fichier cell et du côté gauche, je vais travailler sur mon fichier main.py.

Donc, ce que je vais faire maintenant ici, c'est aller de l'avant et dire c one dot Create button object car je peux me permettre d'appeler ce bouton et ensuite j'ai la capacité de passer la location car center frame est une variable qui est accessible à partir du fichier main.py, n'est-ce pas, donc je peux directement dire center frame comme paramètre.

Et puis je peux continuer à travailler avec mon objet bouton grâce à l'attribut avec une onde sinusoïdale que j'ai fait ici, n'est-ce pas, donc je peux descendre et je peux dire c one, dot cell btn object, dot place comme cela.

Et je peux dire que je voudrais le placer en x égal à zéro et y égal à zéro, exactement comme nous l'avons fait au début de cet épisode.

Et maintenant que j'ai fait cela, alors c'est un bon moment pour tester notre code.

Donc, je vais exécuter cette application et vous allez voir que nous avons ce bouton.

Donc, c'est un très bon début pour développer cette application et répartir le code dans différents fichiers.

Donc, ce sera plus maintenable et plus lisible.

D'accord, donc maintenant que nous avons fait cela, alors nous devons comprendre que nous allons avoir quelques problèmes à l'avenir, si nous continuons à utiliser ce placement ou pour placer nos éléments.

Maintenant, afin de vous montrer le problème dont je parle, je vais créer ici une autre instance de la même classe que nous avons créée.

Donc, je vais dire que c deux est égal à une cellule, comme suit.

Et puis je vais dire c deux dot Create button object, et ce sera à nouveau center frame.

Et puis je veux la cellule juste à côté de la première vente, n'est-ce pas.

Donc, je ne devrais pas dire quelque chose comme voir deux cette vente button object dot place.

Et puis nous devrions savoir dynamiquement combien de pixels nous devrions sauter, n'est-ce pas, afin de le placer exactement à l'endroit que nous voulons.

Mais cela va être beaucoup de maux de tête, et beaucoup de problèmes, toujours en connaissant l'emplacement exact que nous voulons passer.

Parce que, par exemple, disons que je vais passer en x égal à 20 et y égal à zéro et exécuter notre jeu.

Maintenant, vous pouvez voir ici que le bouton de droite semble être avant le bouton de gauche, car nous pouvons presque ne pas voir le texte sur le bouton de gauche ici.

Donc, nous pouvons essayer d'augmenter cette quantité de X à 40, quelque chose comme cela, et réexécuter notre jeu.

Et vous pouvez voir que maintenant c'est beaucoup mieux.

Mais lorsque nous voulons traiter la création de plusieurs éléments dynamiquement, alors peut-être que l'utilisation du placement ou n'est pas la meilleure option ici.

Donc, nous devons envisager de changer notre méthode de placement lorsque nous utilisons TK inter lorsqu'il s'agit de dizaines d'éléments que nous voulons créer dynamiquement.

Et nous pouvons faire cela en changeant notre méthode de place à grid.

Maintenant, ce que grid fait, c'est qu'il prend l'élément parent, qui est tout à fait correct là, et il transforme l'élément parent en colonnes et en lignes.

Maintenant, la beauté est qu'il compte à partir de zéro les colonnes et les lignes.

Donc, par exemple, si nous voulons placer un bouton juste là, alors nous pouvons dire que nous aimerions le saluer, et puis lui donner quelques valeurs qui seront considérées comme le numéro de colonne et le numéro de rouleau.

Voyons cela en action, n'est-ce pas.

Cela pourrait être un peu déroutant à comprendre en théorie.

Mais maintenant que nous allons de l'avant et codons cela, ce sera plus facile à comprendre.

Donc, je vais supprimer tout d'ici et revenir à pi charm.

Et en fait, aller de l'avant et changer la méthode de placement de grid sur les deux boutons ici.

Donc, je vais aller à mon C un et je vais dire grid, et puis je vais passer ici colonne égale à zéro et ligne égale à zéro comme cela.

Maintenant, je vais prendre ces arguments et passer les mêmes en changeant cette méthode en saluer également.

Et puis vous allez voir la différence lorsque je vais dire ici rho égale à un.

Et maintenant, si nous allions de l'avant et exécutions notre programme, alors vous pouvez voir qu'il y a une différence.

Ce texte ici était utilisé pour être à la colonne zéro, ligne zéro, mais celui-ci était utilisé pour être placé à la colonne zéro ligne un et c'est la raison pour laquelle vous voyez le deuxième bouton sous le premier bouton.

Et si j'allais changer cela en zéro, et faire celui-ci, ce qui signifie colonne égale à un, alors vous allez voir ces boutons l'un près de l'autre, ce qui est parfait.

Et cela sera utile lorsque nous voulons créer des tonnes de boutons afin de commencer à préparer le jeu de démineur.

D'accord, donc maintenant que nous avons compris comment fonctionne la méthode grid, alors nous allons commencer à créer ces cellules comme nous le voulons dans nos esprits, nous mettons le jeu maintenant, c'est quelque chose que nous pouvons réaliser avec une boucle for imbriquée.

Donc, laissez-moi vous montrer à quoi cela va ressembler afin que ce soit plus facile à maintenir à l'avenir.

Et effaçons cela d'abord.

Donc, je vais commencer ma première boucle for et je vais dire pour x dans la plage de cinq par exemple.

Maintenant, la plage est juste une fonction qui est responsable de générer tous les entiers dans la plage de nombres donnée.

Si j'ai seulement passé cinq, alors il générera 0123 et quatre comme cela.

D'accord.

Donc, je vais aller à l'intérieur et puis je vais dire pour y dans la plage de cinq.

Donc, je réalise essentiellement ici le comportement de créer 25 boutons car j'ai une boucle qui itère cinq fois à l'intérieur et une boucle qui itère également cinq fois.

Donc, maintenant je peux aller à l'intérieur de cela.

Et je peux dire que c est égal à sell.

Donc, j'instancie un objet de celui-ci.

Et puis je peux aller de l'avant et dire, créer btn object.

Et comme l'emplacement, je vais passer dans le cadre central à coup sûr.

Donc, maintenant que nous avons créé l'objet bouton, alors je peux y accéder avec la propriété que nous avons créée précédemment, qui était cell btn object et je peux utiliser l'option grid.

Et puis je peux passer dans colonne égale à y.

Et je peux dire que la ligne est égale à Wickes.

Comme cela.

Et maintenant, voyons le résultat de cela.

Donc, je vais exécuter cela.

Et vous pouvez voir à quel point c'est beau.

D'accord, donc nous commençons déjà à voir quelque chose de similaire à un jeu de démineur.

Et c'est parfait.

Maintenant, ce que nous pouvons faire, au lieu de coder en dur le cinq sur ces quatre boucles, nous pouvons en fait nous permettre d'aller dans le fichier des paramètres, et écrire ici un nouveau paramètre qui peut ressembler à grid size.

Et puis nous pouvons décider qu'il est égal à n'importe quel nombre que nous aimerions, je vais dire six, juste parce que c'est le nombre que j'ai montré au début de cette série entière comme exemple de jeu.

Et puis je vais aller ici et dire, settings, dot grid size.

Maintenant, rappelez-vous, j'importe tout le fichier des paramètres juste là, n'est-ce pas, donc je peux accéder à la variable grid size.

Et je peux aussi dire ici, la même chose.

Et puis je peux simplement exécuter notre programme à nouveau, et vous pouvez voir à quoi cela ressemble.

Donc, nous avons six colonnes et lignes comme cela.

Et c'est juste un excellent début.

Maintenant, avant d'aller de l'avant, désolé pour la confusion ici, je pense que ce serait mieux si nous disions colonne égale à x et ligne égale à y.

Parce que si nous devions, par exemple, changer cela en trois et non pas les paramètres dot grid size, alors il serait plus précis de dire que nous avons trois lignes, n'est-ce pas, une, deux, et trois.

Donc, c'est pourquoi je vais m'en tenir à ces colonnes égales à x et lignes égales à y, comme suit.

Et puis maintenant je peux simplement convertir cela en Settings dot grid size, et continuer à partir d'ici.

D'accord, donc maintenant que nous avons totalement compris cela, alors nous voulons probablement aussi comprendre comment nous pouvons assigner des événements à nos boutons.

Maintenant, un événement est essentiellement une liste d'actions que vous voulez prendre une fois que vous cliquez sur un bouton.

Maintenant, nous avons dit au début de cette série entière que nous aimerions différencier entre l'action que nous prenons lorsque nous cliquons gauche sur un bouton ou lorsque nous cliquons droit sur un bouton, n'est-ce pas, car ce sont deux actions différentes dans un jeu de démineur.

Donc, cela va être très cool de concevoir cette chose dans le jeu de démineur, donner les événements pour nos boutons est en fait une partie très amusante de notre jeu.

Donc, voyons comment nous pouvons faire cela.

Donc, je vais aller à mon fichier cell.py.

Et voici l'emplacement exact où nous pouvons commencer à assigner quelques événements aux boutons que nous créons.

Parce que c'est exactement l'emplacement où nous créons notre objet bouton, nous pouvons aussi aller de l'avant et lui assigner un événement.

Maintenant, allons-y et écrivons cela.

Donc, lorsque nous voulons assigner un événement à un bouton, alors nous voulons travailler avec une méthode spécifique qui est appelée bind.

Donc, avec bind, nous pouvons en fait aller de l'avant et dire que nous aimerions imprimer quelque chose lorsque nous cliquons gauche sur un bouton.

Et voyons comment nous allons faire cela.

Donc, nous allons devoir passer deux arguments, le premier argument étant la touche sur laquelle on clique sur le bouton.

Et ainsi que quelle est la fonction que vous voulez exécuter une fois que vous cliquez sur n'importe quel bouton que vous cliquez.

Donc, première chose, nous voulons dire que nous voulons faire quelque chose lorsque nous cliquons gauche sur un bouton.

Et la convention avec le TK enter pour passer le clic gauche va être quelque chose comme suit.

Donc, je vais utiliser le signe inférieur.

Et je vais dire button capitalisé dash one greater than sign.

Donc, button dash one est juste une convention pour dire le clic gauche, button dash three va être le clic droit et nous allons voir cela juste dans une seconde.

Et puis nous aimerions aussi dire que nous aimerions exécuter une fonction, n'est-ce pas ? Cela va être le deuxième argument de la méthode bind.

Donc, commençons par la fonction la plus minimaliste que nous pouvons imaginer.

Donc, je vais créer une méthode dans ma classe d'âme, que je vais appeler left click Actions comme cela et cela va aussi recevoir silver pour sûr, c'est un homme d'instance, et puis il va seulement dire, je suis cliqué à gauche, juste comme un exemple de base, je vais le laisser tel quel.

Et maintenant que nous avons fait cela, alors je peux facilement passer la référence pour cette méthode.

Donc, ce ne sera pas comme left click Actions.

Et je vais appeler cette méthode comme cela, en plus, je vais juste lui donner la référence, comme suit.

Donc, faites attention que vous n'appelez pas cette méthode, vous passez seulement la référence de cette méthode.

Donc, maintenant que nous avons cela, alors vérifions cela et voyons si cela va fonctionner pour nous.

Donc, je vais aller ici et agrandir un peu.

Et je vais essayer de cliquer sur l'une de ces cellules ici.

Et vous pouvez voir que nous avons une erreur.

Maintenant, vous pouvez voir qu'il dit ici, a left click Actions prend un argument positionnel, mais deux ont été donnés.

Maintenant, cela pourrait être une flèche familière que vous avez peut-être dans ma série op, mais essentiellement, cela signifie que ce self click Actions essaie de passer deux arguments, lorsqu'il essaie d'appeler la méthode left click Actions.

Maintenant, cela signifie que cette méthode doit recevoir un paramètre supplémentaire afin de rendre cette assignation d'événement réussie.

Et cela vient juste comme une convention de Kindle, elle doit recevoir un paramètre supplémentaire, lorsque vous assignez quelque chose à un événement, cela peut être un peu déroutant, mais c'est ainsi que les événements fonctionnent dans TK into.

Donc, par convention, je vais seulement recevoir dans un paramètre initial que je vais appeler event.

Maintenant, cela sera suffisant car tkinter essaie de passer deux arguments.

Donc, passer ici, un autre paramètre ne devrait pas être parfait.

Donc, je vais réexécuter le programme.

Et puis je vais essayer de cliquer sur quelques boutons.

Et vous pouvez voir que nous avons un excellent résultat ici.

Pour chaque bouton sur lequel je clique, je reçois ce texte de I am left clicked et c'est parfait.

Maintenant, j'aimerais aussi ajouter ici une ligne supplémentaire, qui sera responsable d'imprimer les informations qui viennent à ce paramètre d'événement.

Et vous allez voir qu'il est en fait rempli avec quelques informations que TK into passe en arrière-plan.

Donc, maintenant, relançons notre jeu.

Et si j'allais cliquer sur quelque chose, alors vous pouvez voir que j'ai reçu quelques infos sur l'événement qui a été tué.

Donc, vous pouvez voir que j'ai un événement de pression de bouton, état égal à mod un, juste quelques métadonnées sur l'événement qui s'est produit à ce moment-là.

Et vous pouvez aussi voir que j'ai reçu les valeurs de l'axe x et de l'axe y pour l'emplacement exact où il a été cliqué.

Donc, c'est juste une excellente information de fond que vous pouvez utiliser si vous le souhaitez.

Maintenant, vous pouvez clairement voir pourquoi cette méthode bind nécessite de nous de recevoir un paramètre supplémentaire, lorsque nous assignons une fonction comme un événement qui doit être appelé.

Maintenant, il pourrait être une excellente idée de préparer également la méthode bind pour nos clics droits.

Donc, je vais minimiser cette console.

Et je vais simplement dupliquer cette ligne.

Et je vais dire que nous devons également lier le button dash three.

Donc, cela représentera le clic droit, et cela représentera le clic gauche.

Maintenant, vous pourriez aussi vouloir essayer button dash deux si button dash three ne fonctionne pas pour vous.

Juste pour la sécurité.

Si trois ne fonctionne pas lorsque vous cliquez droit trois, aussi button dash deux.

Si vous avez d'autres problèmes, alors faites-le moi savoir dans la section des commentaires.

D'accord, donc je vais dire ici, right click Actions.

Et évidemment, je vais aller ici et dire this right click Actions.

Et encore une fois, je vais recevoir cet événement.

Et je vais faire la même chose.

Donc, d'abord, je vais imprimer l'événement.

Et je vais dire I am right click, pour que nous puissions différencier les deux.

Et je vais à nouveau exécuter notre jeu.

Et je sais que nous ne pouvons pas voir cela, mais je vais cliquer droit sur cela.

Et vous pouvez voir que maintenant nous avons le texte dans la console.

C'est exactement comme les actions de clic droit.

Donc, c'est génial.

Et nous avons pu assigner des événements à tous nos boutons dynamiquement.

D'accord, donc dans cet épisode, nous allons nous concentrer beaucoup sur notre classe de cellule, car nous allons devoir écrire une logique pour préparer le jeu de démineur.

Cela va être très amusant d'écrire toutes ces nouveaux attributs que nous aimerions recevoir dans cette classe de cellule.

Et ainsi que d'écrire toutes les méthodes qui seront responsables d'écrire la logique de notre jeu de démineur.

Donc, il y aura beaucoup de choses orientées objet que nous allons écrire dans cet épisode.

Et cela va être très cool de faire toutes ces choses.

D'accord, donc première chose, nous voulons peut-être commencer par augmenter la taille de nos boutons pour les rendre plus lisibles.

Et cela est réalisable en allant de l'avant vers l'instanciation de notre classe de bouton à l'intérieur de cette méthode Create button object, et en passant quelques arguments supplémentaires qui seront responsables d'augmenter réellement la taille de nos boutons.

Maintenant, avant de préparer le projet, j'ai découvert que passer en width equals to 12.

Et height equals two, four sont de grandes valeurs.

Lorsque vous jouez à Démineur, où il a 36 cellules, maintenant, vous pouvez en fait aller de l'avant et passer ici une formule qui sera responsable de rendre les boutons plus petits si la taille de la grille devient plus grande.

Mais afin de rendre cela simple, alors je vais juste le laisser tel quel.

Et je vais supposer tout au long du tutoriel, que nous allons seulement jouer au jeu de démineur avec 36 boutons, ce qui signifie que la taille de la grille est de six, ce qui est la valeur dont je parle.

Donc, maintenant, je vais exécuter mon fichier principal.

Et voici à quoi cela ressemble maintenant.

Et c'est juste plus grand et plus lisible et plus confortable pour jouer avec.

D'accord, donc maintenant que nous avons fait cela, alors nous allons devoir faire nos prochaines étapes afin d'avoir plus d'informations sur chacune de nos cellules.

Maintenant, par exemple, nous n'avons même pas un seul indicateur sur quelle cellule est quoi, jusqu'à présent, car la seule chose que nous savons sur chacune de nos cellules est le fait qu'elle écrit simplement un texte dans tous ces 36 boutons.

Mais cela aurait pu être génial si nous avions pu avoir quelques indicateurs sur chacune de nos cellules ici.

Donc, par exemple, jusqu'à ce point, nous savons que nous avons 36 boutons.

Donc, nous avons ceux-ci, et nous avons ceux-ci, n'est-ce pas, mais nous n'avons même pas un seul indicateur sur chaque cellule.

Donc, par exemple, cela aurait pu être bien si cette cellule, par exemple, pouvait avoir un attribut comme x égal à zéro et y égal à zéro, car c'est juste quelque chose qui représente cette cellule spécifiquement, cela signifie que nous pourrions recevoir quelques attributs supplémentaires dans cette cellule dans le même ordre, par exemple pour cela.

Donc, ici, n'est-ce pas, cela aurait pu être génial si nous avions pu dire que cette cellule avait un attribut comme x égal à cinq et y égal à cinq.

Et la raison pour laquelle j'utilise ces cinq et cinq ici, c'est parce que nous commençons à compter à partir de zéro, donc 012345 dans la même méthode de comptage, de haut en bas, comme cela.

Donc, allons-y et recevons quelques attributs supplémentaires dans cette classe.

Donc, je vais aller à ma méthode init, et je vais dire X et Y, comme cela et m'assurer que vous ajoutez ces commentaires.

Et puis je vais utiliser l'affectation self self dot x equals to x, puis je vais faire la même chose pour self dot y, self dot y is equal to y comme cela.

Et maintenant que j'ai cela, alors je peux en fait aller de l'avant et aller à mon fichier main.py et passer ces nombres, car je les itère lorsque je crée ces cellules.

Vous pouvez déjà voir que nous avons quelques problèmes à instancier la cellule, car nous devons passer quelques documents obligatoires.

Et une fois que nous le faisons, alors nous sommes totalement bien.

Et maintenant que nous avons quelques attributs dans chacune de nos cellules, nous pouvons en fait utiliser ceux-ci pour afficher temporairement différents textes sur nos cellules.

Donc, nous pouvons changer cela en une chaîne formatée, par exemple, et nous pouvons utiliser la référence à self dot x comma self dot y à l'intérieur des accolades.

Et maintenant, je peux exécuter notre jeu.

Et vous pouvez voir que maintenant nous avons quelques attributs où chaque attribut représente une vente unique, n'est-ce pas, donc nous savons que x égal à cinq y égal à cinq est cette vente ici.

Et nous savons que 2.2 est cette vente là-bas.

Donc, c'est un excellent début pour préparer l'algorithme que nous voulons écrire pour avoir le jeu de démineur.

D'accord, donc maintenant que nous avons fait cela, alors nous voulons préparer la conception, créer quelques mines entre toutes ces cellules.

Maintenant, nous savons que dans un jeu de démineur, lorsque nous commençons chaque jeu, le jeu choisit quelques cellules aléatoires et les convertit en cellules interdites à cliquer, c'est-à-dire des mines.

Donc, nous devons d'une manière ou d'une autre écrire un algorithme qui sera responsable de prendre quelques cellules et de les transformer en mines.

Maintenant, nous savons que nous avons déjà un attribut qui s'appelle ease mind.

Et par défaut, tous ceux-ci sont faux.

Donc, maintenant, nous allons devoir écrire une méthode qui choisira quelques objets de cellule.

Et nous convertirons ces attributs de Bing is mine equals to false à is mine equals to true, afin que nous ayons un excellent début du jeu de démineur en cours.

Maintenant, nous savons que temporairement, toutes les cellules sont mod mines, car nous assignons toujours false, mais c'est quelque chose que nous allons changer juste maintenant.

Donc, afin de commencer à concevoir cela, alors c'est une excellente idée d'avoir une méthode statique, que nous pouvons appeler à partir du fichier main.py, juste après avoir instancié les objets de vente.

Donc, c'est une excellente idée d'avoir simplement une méthode qui n'appartient pas à chaque instance, mais qui appartient globalement à la classe.

Et c'est la définition d'une méthode statique.

Donc, je vais utiliser ce décorateur ou méthode statique.

Et je vais dire def, randomize mines, comme cela.

Donc, cela signifie qu'il prend quelques cellules et les transforme en mines.

Donc, c'est exactement là où nous aimerions écrire une logique pour transformer certaines cellules en mines.

Donc, temporairement, je vais passer dans le passé, afin que nous n'ayons aucune flèche.

Et maintenant, voyons comment nous allons faire cela.

D'accord.

Donc, première chose, nous devons comprendre comment nous pouvons stocker toutes nos instances à l'intérieur de la liste.

Et il y a une excellente raison pour laquelle nous voulons faire cela à ce stade, car nous instancions 36 instances, mais nous n'avons aucun contrôle sur la façon dont nous pouvons prendre des mesures supplémentaires avec ces 36 instances que nous instancions à partir de cette classe de vente que nous avons ici.

Donc, afin d'avoir une collection de toutes nos instances en un seul endroit, alors c'est une excellente idée de créer un attribut de classe à l'intérieur de notre classe de cellule, que nous pouvons nommer quelque chose comme all.

Et cela va être une liste vide temporairement.

Maintenant, nous allons ajouter les objets de la classe de cellule à cette variable all.

Et c'est quelque chose que nous pouvons faire dynamiquement à l'intérieur de notre méthode init, car cette méthode est la méthode qui est appelée chaque fois que vous créez une instance.

Donc, il est tout à fait logique d'aller de l'avant et de faire ici quelque chose qui sera responsable d'ajouter l'objet à la liste cell dot all.

Donc, nous pouvons avoir toutes les instances de cette classe de cellule en un seul endroit.

Et cela signifie que nous allons devoir dire ici, cell dot all.

Maintenant, c'est la manière dont vous pouvez accéder aux attributs de classe à l'intérieur de votre classe, vous avez peut-être pensé à utiliser jest all.

Mais lorsque nous travaillons avec des classes, vous devez toujours spécifier le nom de la classe comme préfixe lorsque vous accédez à vos attributs de classe.

Donc, nous pouvons dire cell dot all dot append, et puis nous pourrions ajouter l'objet lui-même, qui est self.

Donc, maintenant que nous avons fait cela, alors nous aimerions probablement tester si cela va fonctionner.

Donc, nous pouvons aller à notre fichier main.py.

Et juste après avoir instancié tous ces objets dans ces lignes, nous pouvons dire print cell dot all.

Donc, nous devrions voir une liste avec 36 éléments à l'intérieur de celle-ci, aussi ici.

Donc, vous pouvez voir que c'est exactement le résultat, vous verrez que nous avons probablement dit les six éléments ici qui aussi nous pouvons tester.

Avec l'utilisation de la fonction len intégrée.

Avant cela, vous pouvez voir que nous avons 36.

Maintenant, vous allez probablement remarquer que les objets, la manière dont les objets étaient représentés dans la console n'était pas très conviviale, il aurait été génial si nous pouvions remplacer le paramètre, pour que nous puissions voir les objets plus jolis et plus conviviaux.

Et c'est quelque chose que nous pouvons faire en remplaçant certaines méthodes magiques.

Donc, nous pouvons aller à cette classe d'âme.

Et nous pouvons remplacer une méthode magique qui sera responsable de changer la manière dont l'objet est représenté.

Et je parle d'une méthode magique qui s'appelle our EPR.

Comme cela.

Donc, nous pouvons aller de l'avant et dire que cela devrait retourner une chaîne formatée qui pourrait ressembler à ce qui suit : cellule.

Et puis nous allons passer ici self dot x et self dot y.

Donc, c'est juste une chaîne plus conviviale qui représentera chaque objet de manière plus conviviale.

Donc, au lieu de voir des ID aléatoires, nous pouvons voir de vrais noms conviviaux pour chacun de nos objets.

Suivant.

Et si nous voulons tester que cela va fonctionner, je peux à nouveau me permettre d'exécuter ce fichier main.py et confirmer cela.

Et vous pouvez voir que maintenant j'ai des objets beaucoup plus conviviaux ici, vous pouvez voir que nous avons un résultat parfait.

Très bien, donc maintenant que nous avons compris cela, alors je veux travailler côte à côte, le côté gauche sera le fichier main.py, et le côté droit sera le fichier sale.py.

Maintenant, je veux vérifier chaque fois que je fais un excellent travail en écrivant une logique à l'intérieur de ce randomized mines.

Donc, je vais aller de l'avant et juste après avoir instancié ceux-ci, je vais appeler cette méthode randomize minds static.

Donc, je vais dire cell that randomize minds comme cela.

Et je vais le laisser tel quel, et chaque fois que j'ajoute un morceau de code à l'intérieur de cette méthode, alors je veux exécuter le jeu entier pour voir que je n'ai rien gâché.

Très bien, donc première chose, afin de randomiser les choses, afin de choisir certaines choses aléatoires dans une collection, nous devons travailler avec la bibliothèque qui s'appelle random.

Donc, je vais aller à la première ligne ici, je veux dire à la deuxième ligne, et je vais dire ici, import random.

Maintenant, random a une méthode très spécifique qui est responsable de choisir aléatoirement certains éléments dans la collection donnée.

Maintenant, je vais montrer un exemple plus simple d'abord.

Donc, je vais aller ici et dire que j'ai une liste.

Et encore une fois, cela va être juste un exemple simple, pour vous montrer comment fonctionne cette méthode dont je parle.

Donc, je vais avoir une liste avec trois noms.

Très bien, nous allons avoir Jim, Michael et Paul.

Et puis disons que je veux choisir aléatoirement deux noms chaque fois.

Donc, je vais aller de l'avant et dire random dot simple, simple est une méthode qui accepte d'abord la collection dont vous voulez choisir des éléments aléatoires, donc ce sera ma liste.

Et puis le deuxième argument est le nombre d'éléments que vous voulez choisir chaque fois.

Donc, puisque je veux choisir deux noms chaque fois, alors je vais passer ici, deux.

Donc, assignons aussi cette déclaration entière à une variable.

Donc, je vais appeler cela picked names, n'est-ce pas, et puis je vais juste l'imprimer.

Donc, print picked names.

Maintenant, faites attention que j'appelle cette méthode.

Donc, nous devrions voir les résultats lorsque j'exécute ce jeu.

Donc, lorsque je vais de l'avant et exécute notre programme, alors vous pouvez voir que je reçois Jim et Michael.

Et pour notre prochain, nous pouvons totalement recevoir différents noms, vous pouvez voir que cette fois j'ai reçu Jean et Paul.

Donc, c'est exactement ce que nous voulons faire avec nos mines, nous voulons choisir aléatoirement certaines cellules, certains objets d'argent, et puis simplement changer les attributs de ease mind à true parce que tous sont faux.

Donc, maintenant que nous avons compris cela, allons-y et écrivons la logique nécessaire à l'intérieur de randomized minds.

Donc, ma liste va être sale dot all parce que c'est la collection dont je veux choisir certains objets aléatoirement, n'est-ce pas.

Donc, je vais supprimer cette ligne une fois que nous avons compris comment fonctionne l'échantillon, je vais changer cette variable en picked cells.

Parce que c'est juste un nom de variable plus réaliste.

Et puis je vais supprimer cette ligne temporairement, nous allons sauter une ligne ici.

Donc, il sera plus facile de voir les arguments qui sont passés.

Et la collection que je vais passer ici sera remplie de all parce que le cell dot all inclut toutes les instances, n'est-ce pas, et puis nous devons décider d'un entier, qui sera responsable d'être le compte d'éléments qui devrait être choisi.

Maintenant, si nous avons environ 36 cellules, alors il pourrait être une excellente idée de choisir au moins un quart de sa valeur.

Donc, peut-être neuf cellules à convertir en mine ne rendront pas ce jeu trop difficile à gagner, n'est-ce pas.

Donc, je vais passer ici neuf temporairement juste pour voir comment cela va fonctionner.

Ensuite, je vais dire print picked cells et exécuter notre programme.

Et puis vous pouvez voir que nous avons aléatoirement neuf objets de cellule qui ont été choisis ici.

Donc, c'est une méthode extrêmement utile que nous pouvons utiliser pour choisir certaines cellules et les convertir en mines.

Donc, maintenant que nous avons une collection de cellules choisies, ce qui signifie une liste de cellules choisies, alors nous pouvons en fait itérer sur les objets de cellules choisies, et seulement changer l'attribut de is mine de false à true.

Donc, allons-y et en plus de print pixels, utilisons une boucle for qui ressemblera à ce qui suit.

Donc, je peux dire for pixel in pixels.

Et puis maintenant j'itère sur chaque objet.

Donc, je peux dire pixel.is.

Underscore mind equals to true.

Maintenant, le ease mine vient de ici, car nous savons déjà que nous avons un tel attribut.

Et nous voulons simplement changer cela en true.

Et maintenant que nous avons cela, alors allons-y et exécutons notre programme.

Et nous ne devrions pas voir quoi que ce soit mais en arrière-plan, l'attribut a été totalement remplacé par la valeur de true.

Maintenant, si vous voulez vraiment tester cela, vous pouvez aller de l'avant et après avoir appelé le randomize minds à gauche, vous pouvez aller de l'avant et utiliser quelque chose comme for C in cell dot all puis print le c.is mine.

Donc, nous devrions voir quelques vérités, quelques fausses.

Et cela va être le test final, qui nous montrera vraiment que nous avons pu changer certains attributs.

Et vous pouvez voir que c'est exactement le résultat.

Donc, nous avons fait un excellent travail en choisissant certains objets aléatoires, et en les transformant simplement en mines.

Et c'est juste une façon de faire cela.

D'accord, donc maintenant que nous avons fait cela, alors il est tout à fait logique de supprimer ces lignes de débogage.

Maintenant, nous devons déterminer comment nous allons décider dynamiquement de la valeur de ce nombre de mines choisies, n'est-ce pas, donc nous pouvons aller de l'avant et utiliser le fichier settings.py pour utiliser une formule pour calculer combien de mines nous voulons dans notre jeu.

Donc, nous pouvons aller de l'avant et utiliser ici un autre paramètre que nous pouvons nommer mines count qui pourrait être égal à quelque chose comme ce qui suit.

Donc, je vais ouvrir les parenthèses et je vais dire entre ces deux tailles de lecture au carré, et puis je peux le diviser par quatre.

Parce que dans ce jeu, actuellement, nous avons totalement six cellules car nous itérons sur la valeur de six, deux fois.

Donc, il est logique que nous écrivions une telle formule, n'est-ce pas, donc six au carré divisé par quatre est neuf.

Et c'est à peu près la valeur que nous cherchons à avoir, lorsque nous voulons avoir au moins un jeu de démineur équitable, nous ne voulons pas avoir la moitié de la valeur, nous ne voulons pas avoir comme 27 mines, car cela va être trop difficile à gagner ce jeu.

Donc, environ un quart de cette valeur est juste bien.

Maintenant, vous pourriez aussi vous demander, que va-t-il se passer si un jour je vais changer la taille de la grille à sept.

Donc, sept au carré est 49.

Et divisé par quatre est 12.

Point 25.

Et ce n'est pas bon, car le compte des mines sera un entier.

Donc, je vais juste ajouter ici une autre barre oblique.

Et lorsque vous utilisez une double barre oblique, cela force à être un entier, cela ignore totalement le reste.

Donc, nous pouvons juste ajouter ici une autre barre oblique, et cela sera correct.

Maintenant, je peux revenir à mon fichier cell.py, et je peux me référer à cette valeur settings that mines count.

Et je vois que nous n'avons aucune ligne d'entrée sur les paramètres.

Donc, je peux juste aller de l'avant et utiliser l'entrée des paramètres en haut, et nous devrions être bien.

Très bien, donc dans cet épisode, nous allons concevoir ce que nous devrions faire lorsque nous cliquons à gauche sur une cellule.

Donc, première chose, nous devrions supprimer le texte que nous avons écrit pour chacune des cellules ici, qui représente les valeurs des axes x et y.

Donc, allons-y et supprimons cela d'abord.

Donc, je vais enlever cette ligne car cela était le texte de la cellule.

Donc, je vais juste faire en sorte que cela soit égal à rien.

Et puis nous devons décider de ce que nous allons afficher ici.

Une fois que nous cliquons à gauche sur une cellule.

Donc, laissez-moi réexécuter le jeu comme cela.

Et maintenant nous pouvons voir que nous n'avons rien.

Donc, la réaction attendue ici est que chaque fois que nous cliquons à gauche, excusez-moi, sur leur cellule, alors nous devrions afficher un nombre, qui représentera combien de mines il y a autour de cette cellule.

Donc, ce que cela signifie, c'est que si c'est une mine, et que c'est une mine, et aussi celle-ci, alors nous devrions afficher ici trois, car cette cellule devrait déterminer combien de mines il y a autour de cette cellule.

Prenons un autre exemple ici.

Donc, supposons que nous avons cliqué ici, n'est-ce pas ? Alors cette cellule devrait commencer à réfléchir combien de mines il y a autour des cellules.

Donc, cela signifie que nous parlons de toutes ces cellules.

Et disons que nous avons une mine ici, n'est-ce pas ? Nous avons une mine là, et toutes celles-ci ne sont pas des mines.

Donc, nous devrions afficher ici.

Un, n'est-ce pas ? Donc, ce sera l'objectif principal dans cet épisode.

Et cela va prendre beaucoup d'algorithmes que nous allons écrire à l'intérieur des méthodes à l'intérieur de la classe de cellule.

Donc, ce sera extrêmement stimulant et aussi amusant de faire cela.

Et allons-y et commençons.

D'accord, donc je vais commencer par faire défiler vers le bas jusqu'à left click Actions.

Et puis je vais supprimer tout ici et commencer à écrire ici quelques actions que nous devons prendre.

Maintenant, l'une des premières choses que nous allons écrire ici est une conditionnelle if qui vérifiera si cette cellule est en fait une mine.

Et je peux faire cela en écrivant if self.is Mine.

Donc, la raison pour laquelle je peux faire cela est que je sais qu'au début du jeu, j'ai déjà appelé cette méthode qui s'appelle randomize mines, qui prend quelques objets d'âme, et puis elle définit is mine equals to true, donc je peux totalement faire cela.

Et puis si la cellule cliquée est une mine, alors je veux commencer à prendre plusieurs actions.

Donc, ces plusieurs actions seront également situées sous une méthode que nous pouvons écrire maintenant.

Donc, si self.is Mine, alors je peux aller de l'avant et dire self dot show underscore mind, quelque chose comme cela.

Et c'est juste une théorie.

Je sais que show mine n'est pas une méthode qui existe maintenant.

Mais c'est ce que nous allons faire juste maintenant, je vais sortir de cette méthode.

Et puis je vais dire def, show mine.

Et je recevrai self comme paramètre à coup sûr.

Très bien, donc dans cette méthode, je vais essentiellement écrire les actions qui seront responsables d'afficher cette cellule comme une mine.

Maintenant, nous savons que ici, nous devrions écrire une logique pour interrompre le jeu et afficher un message, un message, que le joueur a perdu, n'est-ce pas, quelque chose comme cela.

Mais je ne vais pas faire cela temporairement, car cela va être trop, je vais arrêter et terminer le jeu chaque fois que je clique sur une mine pendant que nous développons ce jeu.

Donc, convertir l'arrière-plan de cette cellule en couleur de fond rouge devrait être suffisant temporairement.

Donc, je vais simplement dire, ici quelque chose comme ce qui suit self dot cell, underscore bottom object, et puis je vais configurer la couleur de fond de celui-ci.

Donc, si vous vous souvenez, lorsque nous utilisons des objets TK inter, nous pouvons utiliser cette méthode configure qui sera responsable de configurer nos éléments.

Donc, comme exemple, je peux aller de l'avant et dire ici, Bg equals to red.

Maintenant, cela est équivalent à ce que nous avons fait avec le cadre.

Laissez-moi vous montrer cela en divisant verticalement, vous pouvez voir que nous avons pris notre fenêtre ici, et nous avons utilisé dot configure BG equals to black.

Donc, ce que nous faisons ici, nous faisons ici une action qui est assez équivalente.

Chaque fois que nous cliquons sur une cellule, nous vérifions si c'est une mine.

Et si c'est le cas, alors nous allons lancer cette méthode, qui sera responsable de configurer la couleur de fond de cela en rouge.

Et c'est juste un début parfait.

Donc, si nous exécutons notre jeu, et que nous cliquons sur quelques cellules, alors vous pouvez voir que c'est une mine.

Donc, c'est pourquoi elle a été colorée en rouge.

Donc, c'est un excellent début.

Et j'ai réalisé que j'avais une erreur de frappe ici.

Donc, ce sera la logique pour interrompre le jeu.

Et afficher le message d'affichage sera le dernier, d'accord.

Donc, maintenant que nous avons fait cela, alors nous devrions aussi concevoir ce que nous devons faire si la cellule n'est pas une mine.

Donc, voici l'emplacement exact où je devrais dire else.

Et puis je devrais lancer une méthode qui dira self dot show underscore, CIL right, et ici, il y aura des choses complexes car nous devons afficher un nombre qui représentera la quantité de mines qui entourent la cellule cliquée.

Donc, je vais aller ici, et je vais entrer et sortir de cette méthode left click Actions.

Et je vais dire ici, def show, underscore Sal et nous allons recevoir vous-même, disons pass ici et expliquer ce que nous allons faire ici juste dans une seconde.

Maintenant, j'ai zoomé un peu au début de notre classe, car afin d'expliquer ce que nous devons faire maintenant, je vais à nouveau ramener le texte que nous avions ici, qui était self dot x comma self dot y car je veux afficher les valeurs de l'axe x et x est y, car cela va être utile pour expliquer ce que je vais expliquer maintenant.

Donc, j'exécute le jeu ici, vous pouvez voir que nous avons à nouveau les x, x et y.

Maintenant, afin de commencer à calculer la quantité de mines dans les cellules environnantes, chaque fois que nous cliquons quelque part, alors nous devrions utiliser ces x, x et y pour sûr.

Parce que pensez à la situation où nous avons cliqué ici, n'est-ce pas ? Disons que nous avons cliqué ici maintenant.

Donc, nous devrions commencer à itérer sur les cellules qui entourent cette cellule et vérifier si chacune de celles-ci est une mine ou non.

Et puis d'une manière ou d'une autre, nous devrions collecter la quantité de mines et l'afficher ici, donc c'est beaucoup d'actions que nous devrions prendre.

Maintenant, nous pouvons comprendre qu'avoir une méthode qui recevra le x et y comme paramètre, et puis nous donnera l'objet d'une âme va être extrêmement utile, car je pense à une situation où vous cliquez sur cela.

Donc, vous voulez vérifier les attributs de cette cellule de cette cellule, et aussi cette cellule.

Donc, nous pouvons déjà commencer à comprendre que, si nous aurons une méthode qui retournera l'objet cellule, en fonction des valeurs x et y données, cela va être extrêmement, extrêmement utile.

Donc, ce sera la première étape que nous devons prendre maintenant, nous devons écrire une méthode que nous pouvons appeler get cell by exes.

Et puis cela nous rendra l'objet de la cellule.

Donc, allons-y et écrivons cela.

D'accord, donc je vais aller ici à cette ligne au-dessus du show cell.

Et je vais dire quelque chose comme ceci, get cell by Asus, et puis je vais recevoir ici, x et y, comme cela.

Et les actions que nous voulons faire ici sont essentiellement de retourner un seul objet basé sur les valeurs de x et y.

C'est tout, c'est tout ce que nous voulons faire ici dans cette méthode.

Donc, maintenant, nous savons que nous avons cette liste qui s'appelle all et nous pouvons essentiellement commencer à itérer sur cette liste d'objets pour trouver l'objet de vente que nous avons besoin basé sur ces valeurs x et y.

Donc, je vais aller de l'avant et commencer avec une filtration de base qui nous aidera à nous donner l'objet de cellule dont nous avons besoin.

Donc, je vais dire ici pour cell dans cell dot all et juste faire attention que j'utilise le nom de la classe, donc c devrait être en majuscules.

Et puis je vais dire quelque chose comme ce qui suit.

Si so dot x est égal à do donné ses arguments et sell dot y est égal à la valeur y donnée, alors nous devrions utiliser ici return cell comme cela.

Maintenant, la raison pour laquelle je peux faire cela est que chaque fois que j'aurai une correspondance dans ces attributs x et y, alors je peux immédiatement arrêter mon itération et simplement retourner cet objet.

Et cela va être utile, car chaque fois que nous voulons afficher la cellule, alors nous voulons immédiatement voir ce qui se passe à l'intérieur des cellules environnantes.

Donc, c'est une méthode qui va être vraiment utile encore une fois, et cela va être quelque chose que nous allons comprendre dans quelques minutes.

Très bien, donc la prochaine chose que je veux faire maintenant est d'appeler cette méthode et essentiellement imprimer le résultat de cela à l'intérieur du show cell.

Maintenant, juste un rappel, si nous prenons un coup d'œil dans les left click Actions, si la cellule cliquée n'est pas une mine, nous entrons ici dans l'instruction URL et nous appelons cette méthode show cell.

Donc, si nous allons ici et disons print, self dot get sale by xs, et nous passons juste des valeurs aléatoires, comme je ne sais pas zéro, virgule zéro, alors nous devrions voir l'objet spécifiquement, où l'attribut X est égal à zéro et l'attribut Y est égal à zéro.

Et cela n'aura pas d'importance quelle cellule je clique ici car je viens de ramener l'objet où x et y sont égaux à zéro tous les deux.

Très bien, donc laissez-moi lancer le jeu maintenant et voir ce qui se passe ici.

Donc, si la cellule cliquée n'est pas la mine, alors nous devrions voir l'objet à droite.

Donc, laissez-moi agrandir la console.

Et je vais juste cliquer sur 05.

Et c'était une mine.

Donc, nous n'avons rien vu sur la console.

Essayons de cliquer ici.

Et vous pouvez voir que je vois l'objet toujours zéro, virgule zéro, et c'était une mine qui va cliquer ici.

Ce n'est pas une mine.

Donc, c'est un résultat parfait.

Je vais aussi cliquer ici, vous pouvez voir que nous avons une méthode parfaite qui retourne l'objet basé sur les valeurs x et y données.

Donc, laissez-moi vous montrer dans une fenêtre séparée, pourquoi c'est utile d'avoir une telle méthode.

Donc, imaginez à nouveau, que nous allons cliquer sur 1.1 comme exemple, n'est-ce pas ? Donc, nous allons devoir collecter toutes ces huit cellules qui entourent la cellule cliquée.

Donc, cela signifie que maintenant nous avons le contrôle pour amener celle-ci, celle-ci et celle-ci et celle-là et celle-ci et celle-là et aussi celles-ci.

Donc, afin de montrer ce que nous devrions faire maintenant avec la méthode get cell by access.

Alors je vais travailler sur ce bloc-notes que j'ai ici.

Donc, imaginons une situation où nous avons vraiment cliqué sur 1.1.

Donc, si nous cliquons sur 1.1, alors nous devrions amener les cellules qui sont 0.0 0.1 0.2.

D'accord.

Donc, celles-ci vont être ces trois, n'est-ce pas.

Et puis continuons.

Donc, nous devrions aussi amener 1.0, et 2.0.

Et celles-ci vont être ces deux.

Et continuons encore une fois, en cliquant sur 1.1, nous devrions aussi amener la vente de 2.1 2.2.

Et celles-ci vont être ces deux.

Et puis nous avons aussi 1.2, que nous devrions amener.

Et cela va être aussi écrit ici.

Donc, vous pouvez voir que nous avons une formule que nous devons suivre.

Donc, maintenant, allons-y et implémentons cela dans notre code.

Donc, je vais supprimer tous les dessins ici.

Et je vais revenir à notre code réel.

Donc, première chose, je vais supprimer cela.

Et puis je vais juste faire quelque chose comme ce qui suit, je vais faire une liste qui va s'appeler surrounded cells.

Et cela va être égal à une liste.

Et cette liste va inclure ces huit objets.

Maintenant, ces huit objets pourraient être essentiellement tirés de cette méthode get cell by exes.

Donc, premièrement, cela va être served dot get cell by exes.

Et pour 1.1, nous devrions diminuer le x de un, et nous devrions aussi diminuer le Y de un.

Donc, le premier va être self dot x moins un, la deuxième valeur va être self dot y moins un comme cela.

Donc, nous pouvons nous permettre de vérifier la première cellule que nous devons tirer, n'est-ce pas.

Donc, allons à la deuxième.

Et n'oubliez pas d'ajouter ici une virgule, car nous avons une liste qui va inclure huit éléments et nous devons les séparer par des virgules.

Donc, la deuxième va être self dot get sale by axis.

Et maintenant la formule va être de diminuer le x de un.

Et la valeur y va être la même car comme vous pouvez le voir, la valeur y ici est la même.

Donc, je vais juste passer ici self dot y, et encore une fois, séparé par des virgules.

Et afin d'être organisé, je vais aussi dire ici, V pour marquer comme vérifié, donc la troisième va être sold out get sell by axis.

Et encore une fois, le self dot x va être diminué de un.

Mais cette fois, la valeur y va être augmentée de un car c'est vrai ici.

Donc, c'est maintenant aussi vérifié, j'ai mis une virgule.

Et maintenant, je vais dire self dot get sold by axis, je vais passer le même self dot x car la valeur suivante est un, et puis la valeur y est diminuée de un.

Donc, ce sera self dot y moins un comme cela.

Et c'est aussi vérifié.

Et maintenant, je vais sauter à la suivante, ce sera get sold by exes self dot x plus un car la suivante est 2.0.

Et puis je vais passer ici self dot y moins un, n'est-ce pas, et c'est la cinquième valeur, je vais vérifier cela, la sixième va être la précédente qui était la cinquième valeur.

Et c'est cette valeur.

Donc, self dot x plus un encore, et la valeur y devrait être la même.

Je vais fermer cela, ajouter la virgule, marquer comme vérifié.

Donc, je vais faire cela deux fois de plus self dot get sale by axis.

Maintenant, nous pouvons faire attention que les valeurs x et y sont augmentées de un.

Donc, je vais faire exactement comme cela.

Plus un pour les deux.

Et puis la dernière valeur va être self dot gets held by axis, nous allons passer la même valeur x, et puis le self dot y va être augmenté de un.

Et nous pouvons nous permettre de écrire essentiellement une vérification pour toutes les huit cellules.

Donc, maintenant que nous avons fait cela, alors nous pouvons nous permettre de d'abord l'imprimer pour voir si nous avons fait un excellent travail, n'est-ce pas.

Donc, je vais dire print surrounded cells pour voir que nous avons fait un travail merveilleux.

Et allons-y et vérifions-nous.

Donc, je vais exécuter le jeu Stop et relancer.

Donc, nous allons cliquer sur 1.1.

Et nous devrions voir une liste avec huit objets.

Suivons ce qui se passe ici.

Donc, 00 0.1 0.2 1.0 2.0 2.1 2.2, et 1.2.

Parfait, n'est-ce pas ? Parfait travail, nous avons apporté tout ce dont nous avons besoin.

Et si nous comptons cela 12345678, cela ressemble vraiment à ce que nous avons fait un travail merveilleux.

Maintenant, la chose problématique pourrait être si nous cliquons sur une vente comme 0.0, car cela a trois ventes environnantes.

Donc, cela pourrait ne pas fonctionner.

Mais voyons si cela va fonctionner, je crois que cela va fonctionner.

Et cela va tirer les trois objets comme prévu 1.0 0.1, et 1.1.

Donc, je vais cliquer sur 0.0.

Et vous pouvez voir que c'est exactement ce qui se passe.

Mais vous pouvez voir que nous recevons none pour tous les cinq, car ce qui se passe ici, si nous cliquons sur 0.0, alors à un moment donné, ce gate cell by axis va recevoir des valeurs négatives, car chaque fois que nous cliquons sur 0.0, alors une valeur moins un pourrait être passée.

Donc, nous devons éliminer ces nuns lorsque nous écrivons la liste des ventes environnantes.

Et c'est quelque chose dont nous allons nous occuper plus tard.

Mais jusqu'à présent, un travail parfait pour amener les objets de cellules environnantes.

Et continuons à partir d'ici.

D'accord, donc maintenant que nous avons fait cela, alors nous avons dit il y a une minute que nous allons nous occuper des valeurs non que nous avions à l'intérieur de notre liste.

Maintenant, c'est quelque chose qui pourrait être fait par la compréhension de liste.

Maintenant, une compréhension de liste signifie créer une liste par une ligne, qui va immédiatement s'occuper de quelque chose que vous voulez prendre en charge maintenant.

Donc, afin de prendre en charge les valeurs non à l'intérieur de la liste, alors vous pouvez utiliser une expression de compréhension de liste afin de gérer les valeurs non et de simplement les sortir de votre liste.

Donc, ce que nous allons faire maintenant, c'est que nous allons remplacer la liste des ventes environnantes.

Mais nous allons devoir utiliser une compréhension de liste en une ligne, vous savez, pour éliminer les nonces, donc cela va être quelque chose comme ce qui suit.

Donc, les cellules environnantes vont être égales à une nouvelle liste, qui va ressembler à ce qui suit.

Donc, ce que nous voulons vraiment faire, c'est avoir exactement la même liste, mais nous voulons éliminer les nonces.

Donc, cela est réalisable en faisant quelque chose comme cela.

Donc, vous pouvez utiliser une boucle for en une ligne à l'intérieur de votre liste afin de prendre en charge quelque chose immédiatement.

Par exemple, laissez-moi vous montrer comment nous pouvons faire une boucle for en une ligne.

Donc, vous pouvez dire cell for cell in surrounded cells.

Et maintenant que nous avons fait cela, voyons les résultats.

Oui, donc je vais imprimer surrounded cells et faire attention que je remplace la valeur de celui-ci en utilisant à nouveau la même valeur et en assignant quelque chose de nouveau à cela.

Donc, je vais à nouveau exécuter notre main.py.

Et essayons de voir ce qui va se passer si nous cliquons sur 1.1, vous pouvez voir que le résultat est à peu près le même.

Et si j'allais cliquer sur 0.0, alors à nouveau, les résultats sont les mêmes.

Mais lorsque vous utilisez une compréhension de liste, et que vous incluez à l'intérieur de celle-ci une boucle for en une ligne, alors vous pouvez utiliser une instruction if, qui prendra en charge quelque chose que vous ne voulez pas maintenant.

Donc, je peux aller de l'avant et utiliser une expression ici qui ressemblera à si la vente, ce qui signifie que la valeur de l'itérateur n'est pas connue.

Donc, cela va éliminer nos valeurs non.

Et c'est exactement ce que nous voulons.

Donc, à nouveau, je peux réexécuter notre programme, et voir si cela va fonctionner.

Donc, si nous devions cliquer sur 0.0, nous voyons le résultat parfait, n'est-ce pas, nous voyons trois éléments à l'intérieur de notre liste.

Et c'est aussi quelque chose que nous pourrions vouloir tester avec une cellule comme 0.1.

Parce que si nous comptons les cellules environnantes, alors nous avons ici 1234, et cinq.

Donc, si nous cliquons sur cela, alors vous pouvez voir que nous avons cinq éléments à l'intérieur de notre liste.

Donc, c'est une manière parfaite d'amener les ventes environnantes lorsque nous cliquons sur une vente.

D'accord, donc maintenant que nous avons compris cela, alors je vais déplacer toutes ces lignes de code dans une méthode séparée afin que nous puissions avoir une propriété qui va représenter l'objet des ventes environnantes.

Maintenant, une propriété est essentiellement comme un attribut qui est en lecture seule.

Et vous pouvez marquer ces attributs comme des attributs en lecture seule en utilisant un décorateur.

Donc, laissez-moi vous montrer comment cela va fonctionner.

Donc, je vais juste copier tout d'ici.

Et vous savez quoi, juste le couper comme CTRL X et non copier.

Et puis je vais dire ces cellules environnantes, et cela recevra lui-même.

Et je vais juste laisser ces extraits de code ici.

Et puis je vais dire quelque chose comme, return sales.

Et je vais changer ces noms de variables en sales, et aussi celui-ci.

Et ainsi que celui-là.

Maintenant, la raison pour laquelle je fais cela, c'est que je ne veux pas avoir le même nom de variable que le même que le nom de ma méthode, car cela pourrait entraîner beaucoup de problèmes.

Et j'ai dit que je vais convertir cela en un attribut en lecture seule.

Et cela est réalisable par la propriété, ils appellent cela.

Donc, au-dessus de cette méthode, je vais dire add property.

Et maintenant, vous pouvez l'utiliser comme un attribut exactement comme les attributs que nous avons ici dans l'init.

Donc, maintenant que nous avons fait cela, alors je peux me permettre d'aller à show cell, et valider que j'ai fait un excellent travail.

Et je peux utiliser ici self dot surrounded sales.

Et vous pouvez voir que j'ai une complétion automatique.

Et c'est juste parfait.

Maintenant, je peux accéder à mes cellules environnantes en accédant à cette propriété à partir d'ici.

Très bien, donc maintenant que nous avons une méthode qui apporte les objets de vente environnants, alors nous devons itérer sur les objets de vente environnants, et identifier lequel de ceux-ci sont des mines, et lequel de ceux-ci ne sont pas des mines.

Donc, cela va prendre une autre méthode qui sera responsable de cela.

Donc, je vais à nouveau créer une méthode ici qui va ressembler à surrounded sills mines linked, et vous pouvez comprendre ce que cette méthode va faire, elle va compter les mines qui sont dans les cellules environnantes chaque fois qu'une cellule est cliquée.

Donc, je vais rendre cette logique aussi facile que de dire d'abord counter equals to zero.

Et puis je vais itérer sur les objets de vente environnants.

Donc, ce sera pour cell dans self dot surrounded cells.

Et je vais vérifier si cell.is underscore mine, alors je vais augmenter le compteur de un.

Donc, ce sera counter, plus equals one.

Et à la fin de la journée, je veux retourner le compteur et juste l'utiliser.

Donc, ce sera sortir de ces quatre boucles.

Et si conditionnel, et puis juste utiliser return counter comme cela.

Maintenant, tout comme nous l'avons fait avec le self dot surrounded cells, je peux aussi me permettre d'utiliser le surrounded cells mines linked comme un attribut en lecture seule.

Donc, je vais à nouveau aller au-dessus de cette méthode.

Et je vais le marquer comme une propriété comme cela en utilisant ce décorateur.

Maintenant, je ne l'ai pas mentionné plus tôt.

Mais si vous ne savez pas ce qu'est le décorateur de propriété, alors j'ai une série de programmation orientée objet que vous pouvez aller voir.

Et je parie que ce sera une vidéo très informative si vous n'avez jamais entendu parler de ce décorateur de propriété, qui est une chose extrêmement utile lorsque nous écrivons des programmes orientés objet.

Très bien, donc maintenant que nous avons fait cela, alors je peux me permettre de faire quelque chose comme ce qui suit.

Donc, je veux aller à l'intérieur du show cell.

Et je veux juste voir la longueur des mines, ce qui signifie la quantité de mines que j'ai, chaque fois que je clique sur une cellule, donc cela va être un excellent test pour notre jeu.

Donc, si nous cliquons sur une cellule, alors nous pouvons nous permettre d'imprimer so de cette longueur de mines des cellules environnantes.

Et allons-y et voyons si cela va fonctionner.

Donc, je vais exécuter mon jeu.

Et par exemple, supposons que je vais cliquer sur 0.0.

Et c'est une mine et je suis d'accord avec cela.

Et c'est aussi une mine.

Et cliquons ici.

Donc, vous pouvez voir que je vois trois dans la console, n'est-ce pas, parce que j'ai cliqué sur le 1.1.

Et ce que cela signifie, c'est que par ici nous avons trois mines.

Donc, continuons et continuons à cliquer sur certaines cellules.

Donc, nous avons déjà deux mines ici et nous ne devrions pas en avoir une de plus à l'intérieur des cellules environnantes.

Donc, pas ici, pas ici.

Pas ici, pas ici.

Aussi pas ici.

D'accord, donc nous avons une mine ici.

Et si nous cliquons ici, donc ce n'est pas la mine non plus.

Donc, c'est parfait.

C'est vraiment parfait.

Parce qu'un tour autour de celui-ci autour de celui-ci.

Donc, ici nous avons trois mines.

Et cela signifie que nous avons terminé l'écriture de cette logique de la meilleure manière possible.

Très bien, donc il y a une chose de plus que nous voulons faire immédiatement lorsque nous allons de l'avant et cliquons sur une cellule et cela va être l'affichage du nombre de mines qui entourent cette cellule.

Donc, maintenant que nous avons le contrôle avec le surrounded sales mines linked, alors nous pouvons nous permettre de changer le comportement de cette méthode show sole.

Et nous pouvons aller de l'avant et simplement configurer le texte de notre cellule pour afficher la quantité de mines entourant cette cellule, donc cela va être quelque chose comme ce qui suit, ce sera en accédant à l'objet du bouton de la cellule et en configurant le texte.

Donc, je vais utiliser la méthode Configure à nouveau.

Et je vais simplement dire que le texte est égal à self dot surrounded cells mines length.

Et cela devrait être suffisant.

Et maintenant, je peux vraiment me permettre de supprimer le texte original que nous avions précédemment.

Donc, je vais faire défiler vers le haut, et je vais revenir à la méthode qui nous aide à créer l'objet bouton.

Et je vais enlever ce texte d'ici, juste supprimer cela.

Et puis je vais exécuter notre jeu, exécuter le programme.

Et cliquons sur quelques cellules.

Donc, vous pouvez voir que nous avons deux, et cela signifie que nous avons une cellule, peut-être ici, qui n'est pas la mine.

Donc, cela signifie que pour sûr, c'est une mine et c'est une mine aussi.

Donc, parfait.

Maintenant, nous commençons vraiment à avoir un vrai jeu en cours.

Dans ce tutoriel, nous voulons écrire la logique pour afficher la quantité de mines qui sont situées dans les cellules environnantes chaque fois que nous cliquons sur une cellule.

Donc, dans cet épisode, nous allons concevoir certaines fonctionnalités qui seront utiles pour afficher plus d'informations sur le jeu.

Par exemple, actuellement, nous savons qu'il y a 36 cellules sur lesquelles nous pouvons cliquer.

Mais maintenant, si je clique ici, nous savons que nous avons 35 cellules sur lesquelles nous pouvons cliquer, donc nous devons afficher de manière interactive ce type d'information dans notre fenêtre, ce qui sera intéressant de voir comment nous pouvons développer une telle fonctionnalité.

Et en plus, nous allons développer une fonctionnalité qui sera responsable de l'ouverture automatique de toutes les cellules environnantes.

Si la longueur de la cellule cliquée est zéro, exactement comme dans ce cas.

Parce que évidemment, si nous savons qu'il y a zéro mines entourant la cellule, alors il n'y a pas de raison de ne pas cliquer automatiquement sur celle-ci et celle-ci et celle-ci et celle-ci et celle-ci.

Donc, la raison pour cela est que ces cellules auront toujours zéro mines environnantes.

Donc, cliquer sur elles est sûr.

Donc, nous allons développer une fonctionnalité qui le fera automatiquement pour nous, et cela améliorera la vitesse de notre jeu.

Donc, allons-y et commençons par développer tout ce que nous venons de dire ici.

Très bien, donc commençons par le deuxième point que j'ai mentionné plus tôt.

Et cela va être comment ouvrir automatiquement les cellules environnantes au cas où nous voyons le nombre zéro lorsque nous cliquons sur une cellule.

Donc, si nous devions prendre un coup d'œil dans les left click Actions, alors vous pouvez voir qu'il y a une séparation entre une cellule qui est en fait une mine et une cellule qui n'est pas une mine.

Donc, ici, nous pouvons en fait vérifier si la cellule cliquée n'est pas une mine, bien sûr.

Donc, cela signifie que notre code va être ici.

Mais nous pouvons aussi vérifier si le nombre affiché est zéro ou non.

Et la manière dont nous pouvons faire cela est en utilisant la propriété de surrounded cells minds length, et nous pouvons vérifier si cela est égal à zéro ou non.

Donc, cela va ressembler à ce qui suit.

Donc, si self dot surrounded cells minds length est égal à zéro, alors nous devrions faire quelque chose.

Donc, si nous allons entrer ici, alors nous voulons lancer une boucle for qui sera responsable de l'affichage de la longueur des mines pour toutes les cellules environnantes.

Maintenant, nous savons déjà que nous avons une propriété qui nous rend toutes les cellules environnantes.

Et cela vient de ici.

Donc, nous allons utiliser cela dans ce cas à coup sûr.

Donc, cela va être comme ce qui suit.

Donc, nous pouvons dire pour sale underscore object dans self dot surrounded cells.

Et nous pouvons aller de l'avant et dire quelque chose comme cell object, dot show underscore cell.

Maintenant, si vous vous souvenez, nous avons aussi une méthode qui s'appelle Show cell que nous appelons ici.

Donc, il est logique d'essayer d'ouvrir toutes les cellules qui entourent la cellule cliquée, et aussi d'appeler la méthode show cell pour elles aussi.

Et cela va fonctionner dans le cas, bien sûr, si la longueur des mines est zéro, donc lançons le jeu et voyons si nous avons le comportement attendu ici.

Donc, le comportement attendu ici est si nous cliquons ici, et que cela affiche zéro, alors le jeu devrait automatiquement ouvrir cela et cela et cela et voyons si nous avons cela.

Donc, je vais relancer. Essayons de cliquer ici et vous pouvez voir que nous avons deux.

Donc, ce n'est pas un bon test pour nous.

Et c'est une mine.

Donc, nous cherchons zéro.

Et vous pouvez voir que cela fonctionne parfaitement, vous pouvez voir que lorsque j'ai cliqué sur zéro, alors nous avons obtenu tous les nombres qui entourent la cellule cliquée dans la première étape.

Donc, c'est quelque chose qui va accélérer le jeu et qui sera extrêmement utile.

Et continuons à partir d'ici.

Très bien, donc maintenant que nous avons fait cela, alors allons-y et voyons comment nous pouvons ajouter plus d'éléments à notre fenêtre.

Maintenant, nous avons dit que nous aimerions afficher plus d'informations sur le jeu auquel nous jouons, par exemple, des informations comme combien de cellules restent dans le jeu dans chaque situation, car chaque fois que vous cliquez sur une cellule, alors la quantité de cellules restantes diminue, donc allons-y et montrons un texte à ce sujet.

Parce que cela va être utile de voir dans quelle situation de jeu nous nous trouvons actuellement.

Donc, l'approche de cela va être assez équivalente à ce que nous avons fait avec Create button object.

Maintenant, si vous vous souvenez, nous avons utilisé une méthode d'instance qui va de l'avant et crée un bouton.

Et puis nous allons de l'avant et utilisons cette dernière ligne ici, qui ressemble à self dot sell button object equals to btn, qui sera la variable qui a cet objet bouton stocké.

Donc, nous allons faire à peu près la même chose.

Lorsque nous voulons afficher la quantité de ventes qui restent dans le jeu, nous allons créer une méthode qui créera un élément de texte dans la fenêtre.

Et puis nous allons appeler cette méthode à partir du fichier main.py.

Et allons-y et commençons par cela.

Donc, je vais aller de l'avant et dire def, create cell count, labeled.

Maintenant, la raison pour laquelle j'utilise label, c'est parce que le nom de la classe qui est responsable d'afficher juste du texte sans aucune fonctionnalité spéciale s'appelle label.

Et c'est la classe que nous allons initialiser.

Donc, c'est la raison pour laquelle je peux me permettre d'appeler cette fonction, je veux dire la méthode de cette manière.

Donc, nous allons aussi recevoir ici un autre paramètre que nous pouvons nommer location, et je vais aller à l'intérieur de celui-ci.

Et je vais dire label, ou LBL pour le rendre plus court est égal à un label.

Maintenant, nous savons que nous n'importons pas cela.

Donc, je vais faire défiler ici, et je vais dire from TK inter Import button et label aussi.

Et maintenant que nous avons fait cela, alors je vais passer l'argument de location.

Et puis je vais passer quelques arguments supplémentaires.

Donc, cet élément label accepte un paramètre qui s'appelle text, comme nous l'avons vu avec le bouton.

Et nous pouvons aller de l'avant et dire que son texte pourrait être une chaîne formatée, comme cells left, et utilisons un deux-points, et puis je peux aller de l'avant et utiliser quelque chose comme ce qui suit, je peux me référer à la quantité de cellules que nous connaissons déjà à partir des paramètres.

Donc, settings dot grid size, et si je me souviens bien, grid size stocke six ici, car nous venons de le définir à six.

Et donc cela signifie que nous avons six fois six cellules.

Donc, il est logique d'utiliser ici une autre variable que nous pouvons nommer cell count.

Et cela sera égal à read size power of two comme cela.

Donc, nous pouvons aller de l'avant et aussi remplacer cela par celui-ci.

Et cela a totalement du sens.

Et maintenant, je peux aller de l'avant vers mon fichier cell.py et remplacer cela par cell count.

Les choses ont l'air beaucoup mieux.

Donc, maintenant que nous avons fait cela, alors allons-y et retournons aussi l'objet label que nous avons ici.

Et maintenant, voyons comment nous allons appeler cela à partir du fichier main.py.

Maintenant, il y a quelque chose qui est assez délicat avec cette méthode.

Et c'est le fait que ce label n'est pas quelque chose qui doit appartenir à chacune de nos cellules, car c'est une information générale sur le jeu.

Donc, ce que cela signifie, c'est que cela ne peut pas être une méthode d'instance.

Parce que c'est juste une méthode à usage unique que nous voulons appeler tout au long du jeu, nous ne voulons pas appeler cette méthode pour chaque objet de cellule.

Donc, c'est pourquoi cela doit être une méthode statique.

Et une méthode statique est une méthode qui est juste pour le cas d'utilisation de la classe et non pour le cas d'utilisation de l'instance.

Donc, c'est pourquoi il est logique de la marquer comme une méthode statique.

Maintenant, cela signifie aussi que nous devons supprimer le self car nous n'avons pas besoin de recevoir le self si nous n'utilisons pas une méthode d'instance.

Donc, maintenant, il est sûr de supprimer cela d'ici et avoir une méthode comme ce qui suit.

Maintenant, si vous n'avez jamais entendu parler des méthodes statiques, alors il y a en fait un épisode sur les méthodes statiques dans la série Python op que j'ai publiée récemment sur ma chaîne.

Donc, assurez-vous de le regarder au moins pendant quelques minutes, afin d'avoir une meilleure compréhension des méthodes statiques.

Très bien, donc maintenant que nous avons fait cela, alors essayons de comprendre où nous allons appeler cette méthode.

Maintenant, si vous vous souvenez, pour l'objet bouton, nous avons essentiellement utilisé une instruction qui ressemblait à ce qui suit.

Donc, nous avons dit qu'au début, self dot sale button object est égal à none.

Et puis nous sommes allés de l'avant et nous avons assigné cela à un objet bouton qui provient de ici.

Donc, nous allons faire la même chose pour l'étiquette de compte de cellules, car cela va être utile lorsque nous devons utiliser l'étiquette de compte de cellules à partir du fichier main.py.

Donc, maintenant, je peux aller de l'avant et créer un attribut qui va appartenir au niveau de la classe, pas au niveau de l'instance.

Et la raison pour laquelle je fais cela, c'est que l'étiquette de compte de cellules devrait être quelque chose de global, quelque chose qui n'appartient pas au niveau de l'instance.

Donc, je vais aller de l'avant et dire cell count label est égal à none.

Et je peux en fait ajouter ici sur l'objet de score pour garder la même convention que l'objet de bouton de vente.

Et maintenant que j'ai fait cela, alors je peux changer cette chose ici en quelque chose comme cell, que l'objet d'étiquette de compte de cellules est égal à LBL, qui est le nom de variable que nous utilisons.

Donc, cela est en fait assez équivalent à ce que nous avons fait précédemment tout au long de la série avec l'objet de bouton de vente.

Et maintenant que nous avons cela, alors nous pouvons aller de l'avant et l'utiliser à partir du main.py, comme ce qui suit.

Donc, je peux aller de l'avant à ici.

Et je peux simplement appeler cela.

Donc, je vais aller de l'avant et dire comment, comme appeler l'étiquette de la classe de cellule.

Et cela devrait ressembler à ceci.

Donc, nous pouvons dire cell dot create.

Donc, count label, et l'emplacement pour cela sera le left frame.

Maintenant, left frame est le cadre qui était utilisé pour être installé dans la zone gauche de notre fenêtre.

Maintenant, si vous vous souvenez, laissez-moi vous montrer que cela va être juste ici dans cet emplacement.

Donc, si je dessine ici quelque chose, alors c'est le top frame.

C'est le left frame.

Et toute cette zone est le game frame, le center frame que nous utilisons pour jouer au jeu.

Donc, le widget dont je parle devrait être ici.

Très bien, donc laissez-moi nettoyer cela et fermer le jeu.

Oui.

Donc, maintenant nous appelons cette méthode.

Donc, cela signifie que je peux accéder à l'objet label en me référant à cell dot cell count label object.

Et je peux juste utiliser ici un place afin de placer cela quelque part dans le cadre.

Et commençons par placer cela en 0x égal à zéro et y égal à zéro.

Maintenant, si vous vous souvenez, les nombres sont relatifs au cadre lui-même.

Donc, cela sera dans le premier pixel de la cellule du left frame, excusez-moi.

Donc, si je lance le fichier main.py, alors vous pouvez voir que nous avons cela ici.

Maintenant, je sais que c'est assez petit, et il a besoin de quelques éditions pour le rendre plus grand et plus beau.

Donc, c'est exactement ce que nous allons faire maintenant.

Donc, si nous retournons au fichier cell.py, et que nous entrons dans notre méthode statique, qui crée le label, alors nous pouvons aller de l'avant et augmenter la largeur et la hauteur.

Donc, allons-y et utilisons width equals to 12.

Et height is equal to four, exactement comme les nombres de notre bouton.

Et donnons aussi à ces attributs comme BG, ce qui signifie que la couleur de fond est égale à blue black.

Et nous pouvons utiliser le paramètre de couleur de premier plan également.

Donc, nous pouvons utiliser f g is equal to white.

Et voyons ce qui va se passer maintenant.

Donc, si nous devions lancer le jeu, là, vous pouvez voir que cela ne change pas beaucoup.

Donc, cela signifie que peut-être devons-nous augmenter la taille de la police ici, donc nous pouvons aller de l'avant et utiliser font is equals to quelque chose comme ce qui suit.

Donc, formé par défaut accepte un tuple.

Donc, le premier argument de cela devrait être le type de police.

Et vous pouvez aller de l'avant et jouer avec vos polices préférées.

Et le second devrait être la taille de la police.

Donc, je vais commencer par une taille de peut-être 48, voir si cela va être trop et c'est, donc je vais changer le 2 en peut-être 30.

Et cela a l'air juste parfait maintenant.

Donc, je vais le laisser tel quel.

Cela signifie que nous pouvons supprimer ces attributs et continuer à partir d'ici.

Très bien, donc maintenant que nous avons compris cela, alors voyons comment nous allons changer le texte de manière interactive.

Chaque fois que nous cliquons sur une cellule dans la cellule cliquée était en fait une cellule et non une mine, cela termine le jeu.

Donc, cela signifie que nous devons changer la quantité de cellules restantes dans le texte que nous avons situé dans le cadre gauche.

Donc, cela signifie que nous devons faire cette action exacte dans la méthode que nous avons nommée show SIL.

Et la raison pour laquelle nous voulons faire cela ici est que c'est l'emplacement parfait qui utilise certaines actions lorsque nous cliquons sur une cellule, et que c'est en fait une cellule régulière, qui n'est pas une mine.

Donc, c'est l'emplacement exact où nous cherchons à prendre certaines actions lorsque nous voulons afficher des informations régulières sur une cellule ouverte.

Donc, je vais utiliser ici un commentaire qui dira, remplacer le texte de cell count label avec le mot-clé count, quelque chose comme cela.

Maintenant, afin de tester cela, alors je vais changer cela en quelque chose qui est codé en dur, juste pour voir que nous sommes capables de faire cela avec succès.

Donc, allons-y et testons cela.

Donc, premièrement, il est logique de vérifier si cell, que cell count label object est none ou non.

Et je peux juste le faire de la manière dont il est, si cell que cell count label object devrait être suffisant pour tester si cet objet est none, ou est rempli avec quelques informations, ce qui signifie un objet label.

Donc, si c'est le cas, alors nous voulons aller de l'avant et utiliser cell, que cell count label object, et nous voulons configurer son texte à un texte plus récent.

Donc, afin de tester cela, alors allons-y et utilisons changed comme cela, et voyons comment cela va se comporter.

Si je suis en train de lancer cela et de cliquer sur un emplacement aléatoire, alors vous pouvez voir que nous voyons un changement.

Et c'est parfait.

Donc, ce sera la manière dont cela va fonctionner.

D'accord, donc à ce stade, essayons de comprendre quelle sera la manière la plus efficace de stocker en continu les cellules qui restent dans le jeu.

Donc, première chose, nous pourrions nous permettre de stocker un autre attribut de classe que nous pouvons nommer cell count.

Maintenant, nous savons que le cell count change chaque fois que la méthode show cell est appelée.

Donc, ce que cela signifie, c'est que chaque fois que show sale est appelée, nous pourrions essentiellement diminuer la quantité de ventes de un.

Donc, laissez-moi vous montrer à quoi cela pourrait ressembler.

Donc, nous pourrions aller et faire défiler vers le haut et créer ici un attribut de classe que nous pouvons nommer cell count, que nous pouvons aussi nous permettre de définir cette valeur à Settings dot cell count.

Donc, il est logique d'avoir d'abord la valeur de 36, par exemple, pour cet attribut de classe.

Et nous pourrions diminuer en continu cette valeur chaque fois que la méthode show cell est appelée.

Donc, nous pourrions aller ici et utiliser comme première ligne quelque chose comme cell dot cell count, moins equals one, et cela sera responsable de diminuer le compteur de vente de un.

Et maintenant que nous faisons cela, alors nous allons aussi changer la méthodologie que nous stockons le texte dans le label que nous avons.

Maintenant, si vous vous souvenez, nous avons utilisé pour stocker à l'intérieur du label des informations sur les cellules restantes, ce qui signifie les paramètres, ce compte de cellules.

Mais maintenant, il est logique de changer la référence de cela à cell dot cell count comme cela, car c'est la variable que nous allons diminuer chaque fois que nous cliquons sur une cellule.

Donc, cela signifie que l'avoir comme cela est une meilleure idée.

Donc, maintenant, je peux me permettre de copier cela et de faire défiler vers le bas.

Et chaque fois que show cell est appelé, alors je peux configurer en continu ce texte avec les informations suivantes.

Donc, laissez-moi supprimer cela d'ici.

Et en fait, sauter la ligne.

Et entre ces parenthèses, je vais dire que le texte est égal à exactement la même chose.

Et cela doit être configuré chaque fois qu'une cellule est cliquée car nous devons rafraîchir les informations qui sont affichées dans ce label.

Donc, maintenant que nous avons fait cela, alors il est temps de tester si cela va fonctionner, n'est-ce pas.

Donc, si nous lançons notre fichier main.py, alors voyons ce qui va se passer.

Donc, si nous cliquons ici, alors vous pouvez voir que la quantité ici a été diminuée.

Maintenant, cela aurait été génial si nous avions cliqué sur une cellule qui a zéro de mines environnantes, pour voir si cela va fonctionner correctement aussi.

Donc, si nous cliquons ici, vous pouvez voir que cela fonctionne encore très bien.

Et c'est 34 à 3233, excusez-moi, et vous pouvez voir que ici nous avons une incompatibilité.

Et cela se produit, car il pense qu'il devrait aussi diminuer les quantités pour les mines qui sont ici aussi.

Maintenant, encore une fois, laissez-moi vous montrer ce qui s'est passé ici juste maintenant.

Donc, d'abord nous avons cliqué ici, ici, et puis ici, n'est-ce pas, et nous avons vu un comportement parfait de 33 là.

Mais maintenant nous essayons de cliquer ici, mais le jeu pense que ces cellules devraient être ouvertes aussi.

Et c'est pourquoi non seulement cela a diminué à 32.

Il a aussi diminué de cinq, car il a diminué les quantités pour cela et cela et cela et cela.

Et cela et cela, n'est-ce pas.

Donc, il est important de gérer cette situation avec quelque chose que nous pouvons faire juste maintenant, car c'est un bug dans notre jeu.

Donc, nettoyons ici et allons-y et voyons comment nous pouvons gérer cela.

Donc, la manière dont nous pouvons gérer cela est en mettant en place un attribut qui va appartenir à chaque vente, que nous pouvons nommer quelque chose comme ease underscore opened.

Maintenant, ease underscore open va être une variable de type booléen que nous pouvons définir par défaut à false.

Et chaque fois que la méthode show cell est appelée en fonction de cet objet de cellule, nous pouvons convertir cette variable booléenne en true, et cela marquera cette cellule comme étant ouverte.

Et dans ce cas, nous pouvons conditionner notre programme pour ne diminuer le compteur de vente que si la vente n'est pas encore ouverte.

Donc, allons-y et concevons cette fonctionnalité de recherche.

Donc, je vais faire défiler vers le haut.

Et je vais dire ici quelque chose comme ce qui suit.

Je vais dire self.is underscore opened.

Et je vais définir cela à false, car au début du jeu, il est logique de dire que chaque cellule n'est pas encore ouverte.

Et maintenant que nous avons fait cela, alors chaque fois que nous utilisons la méthode de show cell, alors juste après avoir terminé toutes nos fonctions, alors nous pouvons aller de l'avant et dire quelque chose comme self.is open, excusez-moi, est égal à true comme cela.

Et laissez-moi utiliser un commentaire ici qui dira Mark decyl, as opened, utilisez-le comme la dernière ligne de cette méthode, quelque chose comme ce qui suit devrait être suffisant pour expliquer pourquoi nous faisons cela ici.

Donc, maintenant, nous pouvons nous permettre de faire quelque chose comme ce qui suit, nous pouvons dire si self.is open, et nous voulons en fait tester si cela n'est pas ouvert.

Donc, cela signifie que je vais ajouter ici, not.

Donc, cela va vérifier si la vente n'est pas encore ouverte.

Et si c'est le cas, alors je veux tout indenter à l'intérieur de ce conditionnel, car le seul cas où je veux exécuter cela, et cela et aussi ces lignes est dans le cas où la cellule n'est pas encore ouverte.

Donc, cela a parfaitement du sens d'utiliser le code de la manière dont nous l'utilisons juste maintenant.

Donc, maintenant que nous avons fait tout cela, alors testons maintenant si notre jeu va se comporter comme prévu.

Donc, je vais exécuter ce fichier main.py à nouveau.

Et je vais essayer de cliquer sur celui-là.

Et c'est une mine.

Donc, il est logique que les ventes restantes ne diminuent pas, car nous devrions terminer le jeu dans ce cas, mais nous ne voulions pas le faire car cela interromprait notre processus de développement.

Donc, essayons en fait d'exécuter notre jeu une fois de plus.

Et essayons de jouer au jeu comme il doit être joué.

Donc, vous pouvez voir que maintenant nous voyons deux.

Donc, essayons de ne pas cliquer ici pour ne pas faire face à une mine.

Essayons de cliquer ici.

Donc, c'est 34, cela fonctionne toujours parfaitement, 33, et c'est une mine, donc essayons une fois de plus.

Si nous cliquons ici, d'accord, résultat parfait car vous pouvez voir que nous avons maintenant neuf cellules ouvertes et cela a diminué de neuf.

Donc, testons si cela va continuer à bien fonctionner.

Donc, si nous cliquons sur ces trois, alors ceux-ci sont assez sûrs car nous avons zéro ici.

Donc, 26, 25, 24, excusez-moi, et vous pouvez voir que cela fonctionne vraiment parfaitement, car lorsque nous cliquons ici, cela n'a diminué que de deux.

Et ces deux étaient pour celui-ci.

Et pour celui-là.

Donc, maintenant nous avons un excellent jeu en cours sans aucun bug.

Et nous avons géré beaucoup de choses qui auraient pu causer des problèmes à l'avenir.

D'accord, donc montrons un exemple de ce que nous voulons faire dans cet épisode.

Donc, si nous exécutons notre jeu, et que nous commençons à jouer un peu, et par exemple, nous cliquons ici, nous savons que nous avons trois mines autour de là.

Mais afin de commencer à déterminer quelles pourraient être les mines, je veux dire, les cellules sur lesquelles vous ne devriez pas cliquer, alors vous avez besoin d'une utilité qui vous dira à vous-même que vous ne devriez pas cliquer sur cela à l'avenir.

Donc, cela aurait été mieux si nous pouvions développer une fonctionnalité qui colorerait la cellule d'une couleur différente.

Donc, nous pouvons différencier entre les cellules que nous marquons comme candidates aux mines.

Et c'est exactement ce que nous allons concevoir dans cet épisode.

Donc, la manière dont cette fonctionnalité va fonctionner est en utilisant le clic droit de notre bouton de souris.

Donc, si nous allons cliquer avec le bouton droit de la souris sur une cellule, alors elle va la colorier avec une couleur comme orange, peut-être une couleur qui sera une bonne couleur pour différencier une candidate à la mine d'une vraie mine qui nous fait essentiellement perdre le jeu.

Donc, c'est essentiellement quelque chose qui sera responsable de colorier la cellule avec la couleur donnée.

Maintenant, disons que nous avons cliqué sur un emplacement que nous avons marqué comme candidat à la mine, nous aimerions aussi développer l'action opposée, qui sera de démarquer la cellule comme candidate à la mine.

Donc, ce sont les deux fonctionnalités que nous allons travailler juste maintenant.

Donc, allons-y et commençons.

D'accord, donc l'approche de faire quelque chose comme cela, va être assez similaire à ce que nous avons fait avec l'attribut EAS open, nous pourrions d'abord commencer par créer un nouvel attribut à chacun de nos objets de cellule qui ira quelque chose comme self thought is mine candidate, quelque chose comme cela.

Et cette valeur pourrait être false pour chacune de nos cellules au début, la raison pour laquelle cela pourrait arriver est que au début nous n'avons jamais marqué nous-mêmes comme candidats à la mine, nous commençons simplement avec un nouveau jeu vierge.

Donc, maintenant que nous avons un tel attribut, il est logique d'aller de l'avant et de prendre certaines actions lorsque nous cliquons à droite sur une cellule.

Et si vous vous souvenez, nous avons déjà une méthode qui s'appelle right click Actions.

Et nous pourrions trouver cela juste en faisant défiler un peu vers le bas, car cela devrait être juste ici.

D'accord, le voilà.

Donc, voici l'emplacement exact, où je pourrais me permettre de faire quelque chose lorsque nous cliquons à droite sur une cellule, et l'une des choses que je peux faire est de changer l'attribut de false à true.

Donc, je peux aller de l'avant et dire, si non self.is, mine candidate.

Donc, je vérifie si la cellule n'est déjà pas une candidate à la mine, alors je peux aller de l'avant et faire certaines choses.

Maintenant, l'une des premières choses que je veux faire est de changer la couleur de fond de la cellule.

Donc, cela va la marquer visuellement comme une candidate à la mine.

Donc, ce sera self dot cell btn object dot Configure.

Et nous allons appeler cette méthode et je vais simplement passer ici BG couleur de fond égale à orange.

Et maintenant que j'ai fait cela, je peux aussi me permettre de changer de false à true.

Donc, je peux dire self.is underscore mine candidate equals to true comme ce qui suit.

Donc, maintenant, allons-y et testons si cela va fonctionner pour nous.

Donc, je vais exécuter notre jeu.

Et je vais simplement cliquer à droite sur une cellule.

Et vous pouvez voir que cela fonctionne parfaitement.

Maintenant, nous avons dit que nous aimerions aussi concevoir l'action opposée, que nous allons faire maintenant.

Et avant de faire cela, je veux que vous remarquiez quelque chose d'important ici, vous verrez que les ventes restantes ne diminuent pas.

Et c'est bien car nous n'avons pas ouvert la vente, n'est-ce pas.

Donc, c'est un comportement important que nous voulons conserver.

Donc, peu importe combien de fois nous allons cliquer à droite, c'est bien que la valeur des ventes restantes ne diminue pas ici.

Donc, c'est quelque chose que je voulais montrer.

Très bien, donc maintenant que nous avons cela, alors nous devrions aussi concevoir l'action opposée en disant simplement ici else.

Donc, maintenant nous faisons quelque chose si la cellule est déjà une candidate à la mine.

Maintenant, la prochaine fois que nous allons cliquer à droite sur une cellule, et nous savons que la vente est une candidate à la mine, alors nous voulons simplement faire l'action opposée.

Donc, l'action opposée sera de configurer la couleur à la couleur originale.

Donc, ce sera self dot sale between object dot configure, nous allons appeler cette méthode.

Maintenant, cela pourrait être déroutant ici.

Mais il y a une valeur spécifique pour la couleur de fond que vous devez spécifier, qui est déjà la couleur par défaut pour chacun des éléments d'impression que vous créez.

Et cela s'appelle system button phase.

Et c'est juste la couleur que vous voyez au début, n'est-ce pas, la couleur grisâtre.

Donc, c'est la raison pour laquelle j'écris cette chose comme valeur du BG.

Et puis la prochaine chose que je vais faire est évidemment de changer cela en false.

Donc, je vais dire que la vente est ma candidate est égale à false comme cela.

Et cela va probablement fonctionner sans aucune surprise.

Donc, si je clique à droite une fois, deux fois, trois fois, alors maintenant essayons d'annuler nos actions.

Donc, je vais à nouveau cliquer à droite ici, et à nouveau ici, et ainsi que ici, vous pouvez voir que cela fonctionne.

Donc, c'est un excellent début pour avoir quelques candidats à la mine en cours.

Maintenant, essayons aussi de jouer au jeu avec cela, n'est-ce pas ? Voyons si nous avons fait quelque chose de mal au reste de notre jeu.

Donc, c'est un bon test pour nous.

Donc, je vais cliquer à gauche, ouvrir essentiellement quelques cellules.

Et vous pouvez voir que cela fonctionne, pouvons continuer à cliquer ici, ici et là.

Et cela fonctionne très bien.

Maintenant, disons que je pense que c'est une mine ici.

Donc, je vais simplement cliquer à droite, continuer à ouvrir cela.

Et ainsi que celui-là.

Maintenant, c'est en fait une mine car, par exemple, si nous regardons cette cellule, n'est-ce pas, vous pouvez voir qu'elle est censée avoir une mine, ici, ici, ici, ici ou là.

Donc, c'est la mine à coup sûr.

Donc, c'est une bonne fonctionnalité maintenant que nous pouvons marquer cela comme un candidat à la mine.

Donc, nous savons que nous ne devrions jamais cliquer dessus avec le clic gauche de la souris.

Maintenant, je voulais juste rappeler quelque chose qui pourrait vous causer des problèmes en utilisant cette fonctionnalité de candidat à la mine.

J'ai dit plus tôt dans cette série que si vous utilisez button dash three, comme je l'ai fait ici, alors vous pourriez avoir quelques problèmes, car dans certaines configurations de souris, il s'attend à button dash to, mais puisque j'ai la molette de la souris dans ma souris, alors cela devrait être button dash three pour moi-même.

Donc, si vous remarquez que les choses ne fonctionnent pas pour vous comme prévu, alors essayez d'utiliser d'autres combinaisons de nombres comme deux ou même quatre, essayez simplement d'utiliser quelque chose qui n'est pas trois.

Et j'espère que cela fonctionnera pour vous.

Très bien, donc maintenant que nous avons fait cela, alors allons-y et concevons quelques dernières choses que nous voulons afin d'avoir le jeu complet.

Maintenant, nous savons déjà que nous n'avons pas terminé le jeu, lorsque nous cliquons en fait sur notre mine.

Donc, je vais faire quelque chose qui va immédiatement avertir d'un message que nous avons perdu le jeu, si nous cliquons sur une mine.

Maintenant, afin de faire cela, je vais supposer que vous travaillez sur une machine Windows.

Mais la manière dont vous devriez quitter à nouveau, avec une exception est vraiment à vous.

Je vais juste montrer un exemple.

Mais il y a des dizaines d'autres options que vous pouvez aller de l'avant avec.

Et bien sûr, puisque j'utilise une machine Windows, alors cet exemple pourrait être plus adapté aux environnements Windows.

D'accord, donc la première chose que je vais faire ici est d'importer une bibliothèque qui sera responsable de lancer un message général sur la façon dont nous avons perdu le jeu ou quelque chose comme cela.

Donc, afin de faire cela, j'aime la bibliothèque qui s'appelle C types.

Et c'est juste la bibliothèque qui peut vous aider à lancer des messages, des avertissements, des erreurs, tout type de choses que vous voulez inventer.

Donc, maintenant que nous avons cela, alors je vais utiliser cette bibliothèque et essentiellement lancer un message si nous ouvrons la mine.

Maintenant, si vous vous souvenez, nous avons une méthode qui s'appelle Show mine.

Et vous verrez que nous avons déjà un commentaire qui dit une logique pour interrompre le jeu et afficher un message que le joueur a perdu.

Donc, voici l'emplacement exact où nous voulons écrire une telle fonctionnalité.

Et c'est ce que je vais faire maintenant.

Donc, si nous supprimons cela, maintenant je vais aller de l'avant et juste écrire un message générique.

Donc, nous allons utiliser cette bibliothèque C types, et puis je vais choisir la sous-bibliothèque win DLL, et puis je vais utiliser user 32 et puis je vais dire message box, W comme cela.

Maintenant, c'est juste une boîte de message générique que je vais lancer, d'accord, donc je vais passer ici plusieurs arguments.

Et une fois que nous verrons le résultat, alors je vais expliquer pourquoi j'ai fait cela.

D'accord, donc je vais commencer par dire zéro et puis je vais dire vous avez cliqué sur une mine et je vais passer une autre chaîne qui ressemblera à game over et puis je vais à nouveau passer l'argument de zéro.

Maintenant, avant de tester cela, je veux changer l'ordre ici.

Donc, premièrement, nous aimerions changer la configuration de cette couleur de fond en rouge.

Et puis nous aimerions lancer un message.

Très bien, donc maintenant, allons-y et jouons au jeu et cliquons intentionnellement sur une mine, n'est-ce pas, donc essayons de cliquer quelque part ici.

D'accord, donc nous pouvons voir que nous recevons une boîte de message générique.

Maintenant, vous pouvez voir si nous montrons cela côte à côte, comme ce qui suit, alors vous pouvez voir que d'abord, ce qui est le message box ici avec cela.

Donc, vous pouvez voir que le premier anneau était responsable du corps de notre boîte de message, car nous voyons le vous avez cliqué sur une mine dans son corps.

Et vous pouvez voir que le deuxième texte était responsable de montrer le titre.

Maintenant, ces nombres ici et ici sont responsables de vous livrer des types spécifiques de boîtes de message.

Maintenant, le fait que j'ai zéro ici est responsable de me donner seulement une option de bouton sur lequel cliquer, et cela sera d'accord.

Je pense que si j'allais changer cela en quelque chose comme deux, alors je recevrais les options de oui, non et annuler quelque chose de ce genre.

Donc, je vais relancer notre jeu.

Et encore une fois, je vais le perdre.

D'accord, donc vous pouvez voir que j'avais tout à fait raison, c'est abort, retry et ignore.

Et vous pouvez essayer de jouer avec différents nombres, et vous verrez différents résultats.

Mais pour moi-même, je veux seulement recevoir, d'accord, juste confirmez-le, et continuez avec le reste des actions que je veux faire.

Et je vais vous référer à un lien qui vous expliquera quel nombre est responsable de quoi.

Donc, si vous voulez prendre des mesures supplémentaires avec cette boîte de message, assurez-vous de vérifier le lien dans la description.

Très bien, donc je vais appuyer quelque part, juste le remettre à zéro, et maximiser notre PI charm et continuer à partir d'ici.

Très bien, donc juste après que nous avons cette boîte de message, et juste après avoir cliqué OK, alors nous devrions simplement terminer le jeu, nous devrions le quitter.

Maintenant, vous avez toutes les options, ce que vous aimeriez faire, chaque fois que vous cliquez OK, vous pouvez aussi décider que vous aimeriez développer une fonctionnalité pour redémarrer le jeu, je vais simplement le quitter.

Et la manière dont vous quittez un processus Python qui s'exécute est par Cys dot exit comme cela.

Maintenant, Cys est une bibliothèque que vous devez importer.

Donc, je vais faire défiler vers le haut et dire, import Cys.

Et voyons si tout cela ensemble va fonctionner parfaitement pour nous.

Donc, je vais lancer le jeu.

Et essayons à nouveau de le perdre intentionnellement.

D'accord, donc vous avez cliqué sur une mine, la seconde où j'appuie sur OK, il devrait être terminé.

Et c'est exactement ce qui se passe.

Donc, c'est une chose parfaite.

Et maintenant nous avons un jeu complet que nous pouvons essayer de jouer, nous pouvons essayer de le gagner.

Et nous pourrions aussi le perdre parfois.

Et nous devons simplement jouer à nouveau jusqu'à ce que nous gagnions le jeu de démineur.

Très bien, donc maintenant que nous avons fait cela, alors il y a plusieurs choses que nous devons aussi terminer avant d'avoir le jeu complet sans aucun bug et sans aucun problème.

Donc, maintenant, si nous essayons de jouer au jeu, et supposons que nous avons quelques mines qui sont des candidates pour une mine, donc cliquons simplement au hasard ici.

Et puis, supposons que je l'ai marqué comme un candidat à la mine, bien que cela n'ait pas de sens.

Et juste après cela, je clique à gauche sur cela, n'est-ce pas, comme ce qui suit, alors vous pouvez voir que maintenant nous avons un peu de problème, car nous pourrions aussi nous attendre à avoir la couleur de fond originale à nouveau.

Donc, ce que nous devons faire, nous devons aussi spécifier dans le cas où nous cliquons à gauche sur une cellule et que nous l'ouvrons, nous voulons aussi configurer la couleur de fond à la couleur originale du système plutôt que la face, n'est-ce pas.

Donc, c'est exactement ce que nous devons faire maintenant, afin de ne pas faire face à une situation comme celle-ci où nous avons une cellule ouverte, mais nous avons aussi la cellule qui est montrée comme un candidat à la mine, ce qui est assez drôle et nous devons gérer cela.

Donc, nous devons aller à notre méthode de cellule ouverte ou show cell ici, et nous devons faire exactement la même action de changer la couleur de fond à system button face ici.

Donc, nous pouvons aller de l'avant et dire ici quelque chose comme si c'était un candidat à la mine, alors pour la sécurité, nous devons configurer la couleur de fond à system button face quelque chose comme cela.

Donc, nous pouvons vraiment comprendre à l'avenir pourquoi nous avons fait cela ici aussi.

Et je vais faire la même chose que nous avons fait précédemment.

Donc, ce sera self dot cell btw et object dot configure, donc cela va être BG equals to system, button face, comme cela.

Et allons-y et vérifions si cela va corriger le bug pour nous.

Donc, je vais cliquer ici, candidat à la mine, et puis cliquer à gauche.

Donc, cela a l'air bien.

Cela a l'air comme si cela fonctionne.

Donc, nous pouvons continuer à faire les prochaines choses que nous voulons faire maintenant.

Très bien, donc maintenant, nous pourrions penser que nous avons le jeu parfait sans aucun bug.

Mais laissez-moi vous dire que nous avons encore quelques problèmes que nous pourrions résoudre afin d'avoir le jeu parfait et le code parfait pour le jeu.

Donc, si nous essayons de lancer notre jeu, alors essayons de cliquer sur quelques endroits ici, comme ici, et aussi là.

Très bien, donc Brock est génial.

Mais encore, laissez-moi vous dire que si nous cliquons avec notre clic gauche sur Sunsail, alors cela va toujours appeler la méthode left click Actions, ce qui pourrait être quelque chose que nous voulons éviter, car il n'y a aucune raison d'appeler une méthode, si nous avons déjà ouvert une cellule.

Et cela pourrait sembler que cela ne fait rien car la quantité de ventes restantes ne diminue pas.

Mais en fait, quelque chose se passe en arrière-plan.

D'accord, laissez-moi vous prouver en essayant aussi de cliquer avec mon clic droit de la souris.

Donc, si nous cliquons à droite maintenant, alors vous pouvez voir que je peux encore les marquer comme candidats à la mine, ce qui n'est pas bien.

Donc, la manière dont nous voulons gérer cela est en annulant les événements pour les boutons, je veux dire, les cellules qui ont déjà été ouvertes.

Donc, la manière dont nous pouvons faire cela est d'utiliser l'action opposée de la méthode qui était responsable d'assigner l'événement.

Donc, nous avons assigné certains événements au début de cette série entière.

Maintenant, si une cellule a été ouverte, nous voulons annuler ces événements.

Donc, allons-y et voyons comment nous pouvons faire cela.

Donc, nous pouvons voir que ici, nous assignons des événements pour le clic gauche, et pour le clic droit.

Donc, si nous ouvrons une vente, alors nous devons faire l'action opposée.

Et laissez-moi vous dire que TK inter a une méthode qui s'appelle unbind, ce qui signifie annuler tous les événements qui sont assignés à ce bouton spécifique, n'est-ce pas.

Donc, c'est exactement ce que nous allons faire maintenant.

Donc, je vais aller à nos left click Actions.

Et je vais exécuter ici quelques lignes qui seront responsables d'annuler tous les événements sur la cellule cliquée, donc je vais dire annuler les événements de clic gauche et droit, si la vente est déjà ouverte, et c'est sûr de faire cela, car dans le cas où nous cliquons à gauche sur une vente, alors nous ouvrons une vente.

Et si nous perdons le jeu, alors le jeu se termine.

Donc, il est logique d'écrire ici cette fonctionnalité.

Donc, cela va ressembler à self dot cell btn object.on Bind, et nous allons devoir appeler cela deux fois.

Donc, nous allons annuler les événements pour button dash one.

Donc, je vais simplement copier cette chaîne et la coller ici.

Et je vais faire la même chose pour button dash three.

Et cela devrait être responsable d'annuler tous les événements.

Maintenant, vérifions si cela va fonctionner.

Donc, je vais lancer le jeu et cliquer quelque part.

Et maintenant, je vais essayer de cliquer à droite sur cela, vous pouvez voir que rien ne se passe.

Et c'est exactement ce que nous voulons.

Essayons aussi avec quelques autres emplacements comme ici, ici et ici, peut-être, donc maintenant je vais essayer de cliquer à gauche, vous pouvez voir que rien ne se passe vraiment.

Si je clique à droite, et encore une fois, rien ne se passe vraiment.

Mais si je clique à droite ici, alors quelque chose est censé se passer.

Donc, c'est exactement ce que nous voulons.

Nous voulons annuler les événements pour les ventes qui sont déjà ouvertes.

Très bien, donc il y a une dernière chose que nous voulons faire avant de pouvoir jouer au jeu du début à la fin.

Maintenant, le cas où nous gagnons à nouveau, c'est si nous avons la quantité de ventes égale à la quantité de mines.

Laissez-moi répéter cela.

Maintenant, disons que dans ce cas, nous avons neuf mines dans notre jeu, n'est-ce pas ? Parce que si vous vous souvenez, de settings.py, nous savons que mines count est cell count divisé par quatre.

Maintenant, dans notre cas, c'est six puissance deux, ce qui est 36 divisé par quatre est neuf.

Donc, chaque fois que nous avons neuf ventes restantes dans le jeu, mais nous sommes toujours capables de jouer au jeu, alors voici le cas exact où nous pouvons lever le message que nous voulons le jeu, n'est-ce pas ? Félicitations, quelque chose de ce genre.

Donc, c'est exactement la dernière chose que nous voulons faire maintenant.

Très bien, donc allons-y et essayons de concevoir cela, je vais aller au fichier cell.py, et il est logique de lever un message comme félicitations.

Si on show sale, nous avons la correspondance attendue, n'est-ce pas, où sales count est égal au mines count.

Donc, je peux simplement aller sous le self dot show sale.

Et je peux dire quelque chose comme, si minus count est égal au sales, left count flayer one, quelque chose comme cela.

Et écrivons cela correctement.

Donc, je vais dire si cell dot cell count, si vous vous souvenez, c'était un attribut de classe est égal à settings that mines count, alors je vais simplement copier la ligne qui était responsable d'afficher un message.

Et je vais seulement changer le texte à l'intérieur de cela.

Donc, trouvons ce message.

Cela devrait être dans la méthode show mine.

Donc, je vais simplement Ctrl F cela, et vous pouvez voir que, le voilà.

Donc, je vais simplement copier cela et le coller ici.

Et je vais seulement changer les arguments.

Donc, je vais dire, game over.

Félicitations, vous avez gagné le jeu, quelque chose comme cela.

Très bien, donc maintenant que nous avons cela, jouons à notre jeu du début à la fin.

Très bien, donc avant d'aller de l'avant et d'essayer le jeu du début à la fin, nous avons dit que nous aimerions avoir un titre pour le jeu.

Et c'est quelque chose que nous devrions faire plus tôt.

Donc, laissez-moi faire cela rapidement.

Faisons cela ensemble en écrivant un jeu sur le titre du score est égal à un label, nous avons dit que pour créer un texte pur, c'est une excellente idée d'utiliser la classe label ou la bibliothèque TK inter.

Et nous voulons positionner cela dans le top frame, nous voulons que la couleur de fond soit noire, et la couleur du texte, ce qui signifie la couleur du texte, soit blanche.

Maintenant, nous aimerions aussi passer ici text equals to mine sweepable.

Minesweeper game, et la police devrait être un tuple.

Et le premier argument du tuple devrait être le type de police.

Donc, vous pouvez jouer avec n'importe quel type de police que vous aimez, je vais juste le laisser comme une chaîne vide.

Et je vais dire que la taille est égale à 48.

Comme cela.

Et maintenant que j'ai cela, alors je vais aussi dire game title dot place.

Et utilisons 25% de la taille de la largeur du top frame.

Nous avons cette utils dot weight brct, qui reçoit le montant en pourcentage à utiliser à partir de l'axe x.

Et maintenant que j'ai cela, alors je vais sortir de cette parenthèse et je vais dire y est égal à zéro.

Et je vais simplement lancer le jeu et vous pouvez voir que cela a l'air génial.

Très bien, donc en parlant de jouer au jeu, essayons de déterminer comment nous pouvons gagner ce jeu.

Donc, je vais simplement le jouer et deviner où se trouvent les mines.

Très bien, donc nous avons une mine autour d'ici.

Et nous avons cliqué sur une mine.

Cela pourrait prendre quelques fois jusqu'à ce que nous le gagnions.

Mais espérons le meilleur.

D'accord, donc c'est aussi une mine.

C'était une mine si nous cliquons ici au milieu, donc nous avons trois ici, donc c'est assez dangereux d'essayer de déterminer où se trouvent les mines.

D'accord, donc nous avons quelques zéros et c'est probablement la meilleure pratique à suivre.

D'accord, donc vous pouvez voir qu'autour de celui-ci, autour de celui-ci, ici nous avons une mine.

Donc, disons que nous supposons que nous avons une mine ici, alors nous sommes autorisés à cliquer là.

D'accord, donc nous avons deviné juste.

Et donc vous pouvez voir que ici nous avons un.

Et il y a déjà une mine ici, donc nous pouvons cliquer ici à coup sûr.

Très bien, donc maintenant nous devons déterminer où se trouvent le reste des mines.

Donc, ici nous avons trois mines environnantes et ainsi que ici.

Donc, je vais supposer que nous avons une mine ici à coup sûr.

Et ainsi que ici.

Donc, cela signifie que nous n'avons pas de mine ici, et nous avons perdu le jeu.

Donc, essayons une fois de plus.

Peut-être que vous pouvez le gagner, faites-le moi savoir dans la section des commentaires.

Si vous pouvez gagner ce jeu de démineur, c'est assez important.

Et essayons une dernière fois et promets de ne plus essayer car la vidéo va être trop longue.

Très bien, donc si nous cliquons ici, donc nous avons une mine autour d'ici, donc je ne vais pas prendre cela.

D'accord, donc certains zéros, les zéros sont géniaux pour nous.

Et allons prendre cela ici, nous avons une mine.

Donc, ici, nous n'avons pas de mine.

Très bien, belle supposition.

Donc, maintenant, cela signifie que je peux cliquer ici, ici, ici, ici et là.

Et aussi ici.

Donc, vous pouvez voir que maintenant, en regardant celui-ci, vous pouvez voir qu'il y a une mine ici, donc je suis aussi autorisé à cliquer là.

Aussi ici, et aussi ici.

Très bien, donc maintenant que nous avons cela, nous pouvons aussi essayer de cliquer ici parce que nous avons un ici.

D'accord, donc maintenant nous savons que nous avons une mine autour de celui-ci.

Donc, c'est une mine à coup sûr.

Et cela signifie que si nous regardons ce nombre, alors nous pouvons aussi cliquer ici, ici et ici.

Très bien, donc en regardant celui-ci, nous pouvons cliquer ici, parce que c'est une mine à coup sûr.

Donc, maintenant nous pouvons regarder celui-ci.

C'est une mine que nous avons marquée comme candidate à la mine, donc nous pouvons cliquer ici.

Très bien, donc maintenant cela devient compliqué.

Si nous prenons cela ici, nous avons une mine.

Alors nous pouvons cliquer à gauche ici.

Très bien, excellente supposition, nous pouvons continuer à jouer.

Donc, nous pouvons voir qu'en regardant ces trois, ceux-ci et cela sont des mines.

Absolument juste.

Donc, nous avons déjà trouvé six, trois de plus à trouver.

C'est assez excitant.

Très bien, donc je pense que je n'ai plus rien à deviner.

Donc, je dois aller ici en haut.

Et je vais penser que c'est une mine.

Donc, si je clique à gauche ici, oh mon dieu.

Très bien, je vous laisse tout le temps du monde pour essayer de comprendre et jouer au jeu et le gagner.

Et je pense que c'est à peu près tout pour cette série.

Maintenant, comme d'habitude, si vous avez apprécié ce cours entier, veuillez vous assurer de cliquer sur le bouton like.

Et c'est tout.

Donc, j'espère que vous avez tous apprécié, et à bientôt sur ma prochaine série.