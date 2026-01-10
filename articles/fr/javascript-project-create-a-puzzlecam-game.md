---
title: 'Projet JavaScript : Créer un jeu PuzzleCam'
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-10-28T13:40:10.000Z'
originalURL: https://freecodecamp.org/news/javascript-project-create-a-puzzlecam-game
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/thumb.png
tags: []
seo_title: 'Projet JavaScript : Créer un jeu PuzzleCam'
seo_desc: 'Creating a game is a great way to improve your JavaScript skills.

  We just published a JavaScript tutorial on the freeCodeCamp.org YouTube channel
  that will teach you how to create a puzzle game that gets an image for the puzzle
  from your computer''s c...'
---

Créer un jeu est une excellente façon d'améliorer vos compétences en JavaScript.

Nous venons de publier un tutoriel JavaScript sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à créer un jeu de puzzle qui obtient une image pour le puzzle à partir de la caméra de votre ordinateur.

Radu Mariescu-Istodor a développé ce cours. Radu a un doctorat en informatique et crée des tutoriels de programmation vraiment créatifs.

C'est un tutoriel vraiment unique. Le projet est amusant à construire et amusant à jouer.

Le projet est principalement créé avec JavaScript mais il utilise PHP et SQL en backend.

Voici les sujets abordés dans ce cours :

* Accéder à la caméra
* Rogner l'image
* Glisser-déposer
* Éléments de gameplay
* Conception de logo
* Son
* Base de données MySQL
* Serveur web PHP
* Rognage avancé
* Détection de collision avancée

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=HS6KHYIYdXc) (2 heures de visionnage).

%[https://www.youtube.com/watch?v=HS6KHYIYdXc]

## Transcription

(générée automatiquement)

C'est un cours vraiment cool qui vous apprend à utiliser JavaScript et HTML.

Pour créer un jeu de puzzle qui utilise le flux vidéo d'une caméra, vous apprendrez également un peu de HTML et SQL.

Raju a un style unique et intéressant qui rend l'apprentissage des concepts vraiment amusant.

Salut, je suis Raju, et aujourd'hui je vais vous apprendre à faire un jeu de puzzle qui utilise la caméra.

Ce projet entier est réalisé en utilisant uniquement JavaScript vanilla et HTML canvas, et une petite partie de celui-ci.

Celui-ci est réalisé en utilisant PHP et MySQL pour sauvegarder et charger les scores de la base de données.

Le jeu fonctionne sur les ordinateurs de bureau, mais aussi sur les appareils mobiles comme les téléphones et les tablettes.

En regardant cela, vous apprendrez beaucoup de choses utiles que vous pourrez ensuite appliquer dans d'autres projets.

Même si certaines de ces choses sont assez avancées.

Je les enseignerai aussi simplement que possible.

Et je laisserai les deux choses les plus compliquées à la fin.

La bonne nouvelle est qu'elles sont également facultatives, ce qui signifie que vous pouvez obtenir un jeu entièrement fonctionnel sans elles.

Alors ne soyez pas effrayé.

Ce sera amusant, je vous le promets.

Aussi, un merci spécial à Beau de Free Code Camp pour m'avoir permis de partager cela avec vous.

J'espère que vous allez aimer ça.

Ensuite, si vous avez des questions, contactez-moi via ma chaîne YouTube.

Maintenant, commençons.

Nous commençons par écrire la page HTML.

Dans l'en-tête, nous donnons à la page un titre.

Cela changera ce que nous voyons ici dans l'onglet du navigateur.

Et nous lierons également les deux fichiers externes, un pour le JavaScript et un autre pour le CSS.

Ces fichiers sont juste vides pour l'instant.

Ensuite, la partie corps de notre document sera vraiment simple.

Pour l'instant, nous exécutons simplement une fonction appelée main lorsque la page se charge et ajoutons l'élément canvas ici, qui est ce que nous utiliserons principalement pour construire le jeu, ce sera une application Canvas.

Si nous actualisons la page, maintenant nous voyons que l'onglet affiche le titre correct.

Et nous obtenons également une erreur ici dans la console.

Si vous ne voyez pas la console dans votre navigateur, essayez d'appuyer sur F12.

C'est le raccourci pour les outils de développement dans la plupart des navigateurs.

J'utilise Google Chrome, je pense qu'il a les outils les plus utiles.

Mais c'est vraiment juste une préférence personnelle.

N'importe lequel d'entre eux fonctionnera très bien.

Maintenant, l'erreur dit que cette fonction main est manquante.

Alors passons à notre fichier JavaScript et implémentons-la.

Pour l'instant, je vais simplement faire en sorte qu'elle affiche la chaîne main dans la console pour tester si elle fonctionne.

Et c'est le cas.

C'est très bien de déboguer comme ça chaque fois que vous faites un changement.

Sinon, les erreurs s'accumulent, et il peut être très confus de traiter avec beaucoup d'entre elles à la fois.

Mais maintenant, voyons comment accéder à la caméra.

Nous utiliserons une promesse pour obtenir l'accès à nos appareils multimédias.

Nous ne sommes intéressés que par la vidéo provenant de la caméra, et nous le spécifions ici.

Ce qui se passe maintenant, c'est que le navigateur demandera au joueur la permission d'utiliser la caméra.

Lorsque le joueur l'accorde, le code ira ici, où nous définissons une fonction de rappel dans laquelle nous avons accès au signal de la caméra.

Si le joueur n'autorise pas la caméra ou s'il y a une autre erreur, nous la capturerons et l'afficherons à l'écran.

Lorsque tout fonctionne, nous initialisons l'objet vidéo.

Nous utiliserons une variable globale pour cela, et je les écrirai en lettres majuscules.

Pour rendre clair quand une variable est globale ou non dans le code, nous créons ensuite l'élément vidéo.

Nous l'initialisons au signal provenant de la caméra et le jouons lorsque les données vidéo sont disponibles, nous pouvons commencer à le mettre à jour sur le canvas.

Cette fonction updateCanvas est ce que nous allons implémenter ensuite.

Mais d'abord, définissons également le canvas ici globalement et ajoutons la référence à l'objet de contexte du canvas également.

Nous initialisons le canvas avec celui défini dans la page HTML précédemment.

Cela fournit toutes les méthodes de dessin dont nous aurons besoin pour construire le jeu.

Notre Canvas remplira toute la fenêtre maintenant, la fonction updateCanvas doit dessiner la vidéo sur le canvas.

Nous utiliserons donc la méthode drawImage pour faire exactement cela.

Nous devons également spécifier ici que nous voulons commencer à dessiner à partir du coin supérieur gauche, qui a les coordonnées 00.

Maintenant, lorsque je rafraîchis, quelque chose se passe, il montre l'image provenant de ma caméra.

Ma caméra est simplement pointée vers le mur ici pour le moment.

Mais elle ne détecte aucun mouvement pour l'instant.

Nous devons mettre à jour le canvas plusieurs fois par seconde pour voir cela se produire.

Et nous utiliserons les méthodes requestAnimationFrame pour le faire fonctionner.

Cette méthode appellera la fonction de manière récursive plusieurs fois par seconde, et elle essaiera de mettre à jour 60 fois par seconde si l'ordinateur est assez rapide.

Maintenant, nous obtenons l'image en direct.

Je vais simplement mettre Mr chibi son ici pour que ce soit moins ennuyeux.

Maintenant, vous remarquerez une bordure blanche ici.

C'est un peu étrange, car nous avons dit que nous voulions dessiner la vidéo à 00.

Mais l'élément body a une margede par défaut.

Et c'est ce que nous voyons réellement.

Nous allons l'enlever en allant dans notre fichier CSS, et en changeant le style de l'élément body en mettant la marge à zéro.

Mieux maintenant, mais nous avons toujours les barres de défilement ici, qui ne sont pas vraiment nécessaires.

Alors je vais les enlever en mettant overflow à hidden.

Maintenant, les barres de défilement ont disparu, mais la vidéo dépasse réellement de l'écran.

Nous ne voulons pas cela.

Et nous devons garder à l'esprit qu'en général, il existe de nombreuses webcams ou caméras de téléphone avec différentes résolutions, ratios d'aspect, etc.

Alors nous avons besoin d'un moyen de redimensionner la vidéo pour qu'elle s'adapte au milieu de l'écran, de préférence avec un peu d'espace autour pour que nous ayons assez de place pour déplacer les pièces plus tard.

Nous utiliserons ce scaler pour spécifier combien d'espace à l'écran sera utilisé par l'image.

Et ils garderont également une trace d'autres informations connexes dans cette variable de taille.

Nous mettons à jour ces valeurs ici lorsque les métadonnées sur la vidéo sont disponibles.

Tout d'abord, nous utilisons une variable auxiliaire pour trouver le ratio minimum entre la taille de l'écran et la taille de la vidéo.

Et ensuite, nous définissons les attributs de taille en conséquence.

Notez ici que l'une de ces choses se simplifiera.

Ainsi, nous préservons correctement le ratio d'aspect et rien n'est étiré.

Pour les coordonnées x et y, nous commençons au milieu de l'écran et allons simplement à mi-largeur vers la gauche et à mi-hauteur vers le haut.

Ensuite, pour affecter réellement l'image, nous devons mettre à jour la méthode drawImage ici.

Cette méthode peut être appelée avec un nombre différent d'arguments avant que nous n'ayons simplement spécifié le coin supérieur gauche.

Mais maintenant, nous ajoutons également la largeur et la hauteur.

D'accord, cela fonctionne, nous voyons maintenant toute l'image provenant de la caméra avant qu'elle ne soit légèrement rognée sur la droite.

Nous obtenons également cette marge de sécurité en pourcentage.

Et si nous changeons la valeur ici, nous obtenons une marge de taille différente à la place.

Nous pouvons également vérifier pour voir comment l'application apparaît sur différents écrans en appuyant sur ce bouton.

Nous pouvons même sélectionner un appareil spécifique dans cette liste.

Mais chaque fois que nous changeons quelque chose, nous devons rafraîchir la page pour voir cela se produire.

Cela a l'air bien.

Et en mode paysage, il faut rafraîchir à nouveau.

Nous pourrions en fait faire en sorte que ce redimensionnement se fasse automatiquement en utilisant un écouteur d'événements pour le redimensionnement de la fenêtre.

Nous devons ensuite déplacer ce code dans la fonction de rappel et également appeler cette fonction ici pour que le code s'exécute comme avant.

Et je devrais également déplacer ces lignes ici aussi.

De cette manière, le Canvas se redimensionnera également et pas seulement le flux de la caméra.

D'accord, voyons si nous changeons l'orientation.

Oui, cela fonctionne.

Quelle que soit la taille de l'écran, nous obtiendrons l'ajustement approprié cette fois-ci.

Mais encore plus important, cela fonctionnera indépendamment de la taille et du ratio d'aspect que votre caméra produit.

Je vais démontrer cela en forçant ma webcam à produire une taille spécifique.

Notez que toutes les webcams ne supportent pas le redimensionnement de cette manière, et cela peut ne pas fonctionner pour vous, mais vous pouvez essayer, vous pouvez voir que cela fonctionne très bien avec le ratio d'aspect carré.

Essayons un ratio d'aspect vertical ensuite.

D'accord, cela fonctionne très bien.

Je vais enlever ces paramètres supplémentaires.

Maintenant, parce que nous voulons voir toute la vidéo provenant de la caméra.

C'était juste une expérience.

Et je vais en fait commenter cet écouteur d'événements.

Parce que nous n'avons pas vraiment besoin de cette fonctionnalité à l'intérieur de l'application.

Les utilisateurs ne sont pas censés redimensionner l'écran comme cela.

Je l'ai fait pour mieux démontrer comment les choses fonctionnent et éviter de rafraîchir tout le temps.

De plus, vous pourriez en avoir besoin dans l'un de vos projets.

Nous définissons maintenant la classe piece et spécifions un index de ligne et de colonne dans le constructeur.

Nous aurons un tableau de ces pièces et le définirons globalement ici.

Nous devons également spécifier combien de lignes et de colonnes il y a.

Et je vais les stocker ici.

Maintenant, pour initialiser les pièces, nous commençons avec un tableau vide et itérons à travers les lignes en utilisant la variable I et à travers les colonnes en utilisant la variable j et ajoutons la nouvelle pièce définie en utilisant ces deux indices dans le tableau.

Pour pouvoir dessiner les pièces, nous allons implémenter la méthode draw qui prend le contexte comme paramètre.

Commençons par dessiner un simple rectangle ici pour voir si ce que nous avons fait jusqu'à présent fonctionne.

Maintenant, nous devons déterminer l'emplacement et la taille de ces pièces en fonction du nombre de lignes, de colonnes et de la taille de la vidéo à l'écran.

Je vais entrer ces espaces réservés ici et calculer les valeurs exactes dans le constructeur.

La largeur et la hauteur de chaque pièce est simplement la largeur et la hauteur de la zone divisée par le nombre de colonnes et de lignes respectivement.

Je définis ici x et y pour que chaque pièce soit définie à l'emplacement correct au début.

Même si c'est un jeu de puzzle où le joueur doit trouver les emplacements corrects, il est utile de commencer avec la configuration douce lors du développement du jeu.

Vous verrez.

Je me rends compte maintenant que x et y pourraient en fait être définis après avoir la largeur et la hauteur, puis les définir en utilisant la largeur et la hauteur comme ceci.

Le code est clair de cette manière.

Nous avons maintenant besoin d'un moyen de dessiner les pièces.

Nous faisons cela ici en itérant simplement à travers toutes et en appelant la méthode draw en utilisant le contexte global.

D'accord, je pense que nous sommes prêts à déboguer maintenant.

Oh, j'ai oublié d'appeler la méthode stroke ici.

Sans elle, rien ne sera dessiné.

Voyons, je vais rafraîchir et rien n'est différent pour l'instant.

C'est parce que le tableau des pièces est vide, nous devons appeler la fonction initialize pieces.

Et nous le ferons dans la console pour l'instant.

D'accord, maintenant quelque chose se passe et cela a l'air bien.

Trois lignes et trois colonnes.

Mais ce n'est pas encore prêt.

Ce sont juste des rectangles vides dessinés sur la vidéo.

Regardez, si je commente le dessin de l'image vidéo ici, vous pouvez juste voir la grille.

Chaque pièce doit rogner une partie spécifique de la vidéo et la montrer, nous faisons cela en ajoutant un appel à la méthode draw image ici.

Nous utilisons une autre version de la méthode draw image, une plus compliquée qui accepte neuf arguments.

Après avoir spécifié la vidéo, nous devons indiquer la partie gauche où le rognage se produit.

Ensuite, la partie supérieure, puis la largeur et la hauteur, ces valeurs sont relatives à la vidéo.

Et quelle que soit la résolution et le ratio d'aspect qu'elle a, maintenant, après avoir spécifié d'où prendre les données de l'image, nous devons dire où la dessiner.

C'est facile.

C'est simplement l'emplacement x et y de la pièce, et nous devons utiliser sa largeur et sa hauteur, d'accord, cela ressemble maintenant à avant, mais chaque pièce montre la partie de la vidéo dont elle est responsable, nous pouvons en fait paramétrer cette fonction ici pour supporter n'importe quel nombre de lignes et de colonnes et nous l'appelons simplement ici avec des valeurs par défaut au début, nous pouvons tester dans la console en utilisant différentes tailles de grilles, randomisons l'emplacement des pièces.

Ensuite, nous écrivons simplement une fonction où nous itérons à travers toutes et générons un emplacement aléatoire pour chaque pièce.

Nous définissons ici x et y respectivement, nous appelons cela dans la console.

Et ce n'est pas ce que nous attendons.

Les valeurs aléatoires sont comprises entre zéro et un, ce qui signifie qu'elles sont toutes plus ou moins dans le coin supérieur gauche ici.

Je ne vais pas entrer dans le fonctionnement des demi-pixels.

Alors passons et mettons ces valeurs à l'échelle par la largeur et la hauteur du canvas.

Mieux, beaucoup mieux.

Mais vous pouvez voir que certaines pièces sortent de l'écran ici.

Nous pouvons empêcher cela en soustrayant la largeur et la hauteur de la pièce ici lors de la mise à l'échelle.

D'accord, bien.

Maintenant, la raison pour laquelle nous voyons des pièces en double, une fois distribuées aléatoirement et d'autres qui sont derrière elles aux emplacements corrects, est que nous ne vidons pas le canvas avant de redessiner chaque image.

Si nous faisons cela ici et randomisons à nouveau les pièces, nous obtenons ce que nous attendons.

Testons également différentes tailles de grille.

Bien, j'aimerais en fait avoir une idée de l'endroit où les pièces doivent aller, cela rendra le débogage plus facile.

Et peut-être pouvons-nous le garder comme un mode facile ou quelque chose de similaire.

Alors je vais déplacer cet appel clearRect en haut, définir une transparence de 50 % et décommenter le dessin de la vidéo que nous avions précédemment.

Ensuite, je réinitialise la transparence afin que seule la vidéo soit semi-transparente, mais les pièces soient dessinées normalement après cela.

De cette manière, la vidéo en arrière-plan montre où je dois déplacer les pièces, mais elle est estompée pour ne pas être confondue avec les pièces réelles. Maintenant, pour implémenter la fonctionnalité de glisser-déposer pour les pièces, nous devons ajouter des écouteurs d'événements au canvas.

Nous implémentons la fonction pour cela ici et commençons par ajouter un écouteur d'événements pour le clic de souris avec une fonction de rappel que nous devrons définir.

Ensuite, deux autres écouteurs d'événements pour le mouvement de la souris et le relâchement de la souris seront également nécessaires.

Pour gérer l'événement de clic de la souris, nous marquons d'abord quelle est la pièce sélectionnée en obtenant celle que l'utilisateur presse dans l'interface.

Nous définirons cette fonction bientôt.

Mais obtenons d'abord la logique de haut niveau.

Nous stockerons la pièce sélectionnée à l'intérieur de la variable globale que nous avons initialisée avec normal au début ou si aucune pièce n'est pressée.

Ensuite, si une pièce est sélectionnée, nous calculons quel est le décalage par rapport au coin supérieur gauche de la pièce comme ceci, nous utiliserons ce décalage lors du glisser pour que la pièce ne se verrouille pas simplement à l'emplacement de la souris comme ceci.

Cela rendra une interaction fluide.

Ensuite, lors du mouvement de la souris, si une pièce est sélectionnée, nous mettons à jour l'emplacement vers le nouvel emplacement de la souris et considérons également le décalage.

L'événement de relâchement de la souris sera simplement laissé vide pour l'instant.

Alors, comment savons-nous si le joueur appuie sur une pièce ou non ? Eh bien, tout ce que nous devons faire est d'itérer à travers toutes les pièces et de vérifier si l'emplacement du clic est dans les limites de l'une d'entre elles.

Nous devons vérifier si x est supérieur à la pièce X et inférieur à celle-ci plus la largeur de la pièce.

Et si y est supérieur à la pièce Y et inférieur à celle-ci plus la hauteur de la pièce, si c'est le cas, nous retournons simplement cette pièce.

Si rien ne correspond à ces conditions, nous retournons simplement Non, ce qui signifie que rien n'a été pressé.

D'accord, testons. Je déplace la souris sur la pièce du coin inférieur gauche, je clique et je fais glisser.

Super, mais maintenant je suis coincé comme ça, je dois implémenter l'événement de relâchement de la souris pour pouvoir lâcher la pièce.

Maintenant, la chose évidente que nous devons faire est de définir la pièce sélectionnée à non.

Mais avant cela, nous devons faire une autre chose.

Nous vérifions si la pièce est proche de l'emplacement correct où elle est censée aller.

Et si c'est le cas, nous la verrouillons en place.

Nous devrons implémenter ces nouvelles méthodes.

Mais d'abord, discutons de pourquoi nous faisons cela.

La première raison est que cela donne un retour approprié.

Lorsque le joueur lâche la pièce, si elle saute en place, cela signifie que le mouvement était correct.

Et le joueur peut passer à la suivante.

La deuxième raison est que plus tard, nous devrons évaluer si les pièces sont dans la position correcte ou non.

Et il est très peu probable que le joueur puisse déposer toutes les pièces de manière pixel parfaite.

Donc ce verrouillage aidera également à cela.

La raison finale est que je pense que cela rend le jeu plus intéressant et amusant à jouer.

Alors, pour implémenter cette fonctionnalité, nous retournons à la classe pièce et ajoutons les deux nouvelles méthodes.

Tout d'abord, nous vérifions si la pièce est proche de l'emplacement correct.

Nous faisons cela en calculant simplement la distance par rapport à l'emplacement correct.

Et en vérifiant si elle est inférieure à un seuil.

Ou utilisez un seuil qui est proportionnel à la taille de la pièce ici, environ 33 %.

J'ai fait quelques essais et erreurs et je pense que cela semble bien comme ça.

Si la distance est inférieure, alors elle est considérée comme proche.

Sinon, ce ne sont pas les emplacements corrects qui doivent être stockés quelque part.

Et je le ferai ici dans le constructeur parce que nous avons déjà convenu que les pièces seront initialisées à l'emplacement correct.

Pour mesurer la distance, nous utilisons simplement une conséquence du théorème de Pythagore.

Je suis presque sûr que vous le connaissez déjà.

Mais si vous ne le connaissez pas ou voulez en apprendre davantage à ce sujet, consultez la vidéo récente que j'ai faite à ce sujet.

Je pense avoir fait un bon travail en l'expliquant, en le prouvant et en donnant toutes sortes d'applications.

Qu'en pensez-vous ? La méthode snap est vraiment facile.

Elle place simplement la pièce à l'emplacement correct et c'est tout.

Déboguons maintenant. Je peux aller et cliquer sur une pièce, la faire glisser et la relâcher.

Je peux la relâcher où je veux.

Et si je la dépose près de l'emplacement correct, elle se verrouillera en place.

Et cela fonctionne pour chaque pièce.

Mais un problème est que la pièce sélectionnée est parfois dessinée sous les autres.

Ce n'est pas bien.

Cela dépend de l'ordre dans lequel nous dessinons les pièces.

Puisque celle en haut à gauche est la première dans le tableau.

Toutes les autres seront dessinées par-dessus.

Mais celle en bas à droite n'a pas ce problème.

Elle est toujours au-dessus.

Nous devons corriger cela en déplaçant la pièce sélectionnée à la dernière position dans le tableau, nous trouvons d'abord l'index où elle se trouve actuellement.

Ensuite, même si cela ne devrait pas être possible pour qu'elle soit manquante, je vérifie ici juste pour être sûr, je la supprime ensuite en utilisant la méthode splice et je l'ajoute à nouveau à la fin du tableau en utilisant la méthode push.

Maintenant, peu importe quelle pièce je sélectionne, elle sera dessinée par-dessus tout comme prévu.

Mais il reste encore un problème.

Lorsque je clique ici où plusieurs pièces se chevauchent, cela sélectionne la pièce la plus basse.

Nous corrigeons cela en itérant le tableau des pièces dans l'ordre inverse.

De cette manière, nous nous arrêtons à la pièce la plus haute sur laquelle l'utilisateur clique.

Maintenant, tout fonctionne bien.

Mais une dernière chose que nous devons considérer est les appareils mobiles.

Ce que nous avons fait jusqu'à présent ne fonctionne pas encore sur ceux-ci.

Voyez, même si je débogue en utilisant ce mode, et que j'essaie de faire glisser des pièces, rien ne se passe.

C'est parce que les mobiles utilisent des événements tactiles au lieu d'événements de souris.

Alors nous devons supporter ceux-ci également.

Nous retournons à la fonction où nous ajoutons des écouteurs d'événements, copions les trois et réécrivons ce qui est nécessaire.

Les fonctions de rappel touchstart, touchmove et touchend devront être définies ensuite.

Mais elles sont faciles à faire car nous réutiliserons les fonctions de rappel des événements de souris de tout à l'heure, nous devons simplement obtenir l'emplacement ici d'une manière un peu différente.

Et ensuite nous pouvons appeler l'autre rappel comme ceci, nous copions cette fonction de rappel et implémentons les deux autres.

Maintenant, lorsque nous déboguons, cela fonctionne, mais une erreur se produit au toucher.

Et c'est parce qu'il n'y a pas d'emplacement disponible alors.

Je veux dire, si vous ne touchez pas, où ne touchez-vous pas.

Alors nous omettons en fait ces arguments ici.

Maintenant, tout fonctionne lorsque je débogue ici.

Mais certains appareils mobiles ont une fonction intégrée qui rafraîchit la page lorsque l'on fait glisser vers le bas.

Nous ne voulons pas que cela se produise chaque fois qu'un joueur fait glisser une pièce vers le bas.

Alors nous le désactivons dans le fichier CSS en définissant le comportement de défilement excessif à none.

C'est tout pour le glisser-déposer.

Vérifions simplement si cela fonctionne également avec des pièces de différentes tailles.

Ensuite, nous ajoutons des éléments de gameplay comme le menu et l'affichage du temps écoulé, nous devons définir plus de structure dans la page HTML, une div qui contiendra tous ces nouveaux éléments.

Une div pour le menu et la div pour afficher le temps.

Le menu contiendra un composant select pour définir la difficulté, il y aura quatre options différentes.

Et lorsque l'utilisateur change celles-ci, nous appellerons une fonction appelée SetDifficulty, que nous devrons définir en JavaScript.

Nous avons également besoin du bouton ici pour démarrer le jeu.

Appuyer dessus appellera une fonction appelée restart que nous devrons également définir en JavaScript.

Alors passons au fichier JavaScript.

Ensuite, nous ajoutons deux nouvelles variables globales pour suivre l'heure de début et de fin.

Nous implémentons ensuite la fonction setDifficulty, nous obtenons d'abord la valeur du composant select que nous avons défini en HTML.

Sur cette base, nous appelons la fonction initializedPieces avec un nombre différent de lignes et de colonnes.

J'utilise une structure switch case ici pour éviter de nombreuses instructions if else.

C'est une erreur courante que font mes étudiants.

Les valeurs que j'utilise ici ne sont que des suppositions.

Mais pour la variante insensée, je voulais avoir exactement 1000 pièces.

Alors j'utilise 40 et 25, qui ont le ratio d'aspect le plus carré, puis la fonction restart définira la variable startTime à l'horodatage actuel.

Et l'heure de fin est définie à No car nous venons de commencer à jouer, nous randomisons également les pièces à ce stade.

Si je rafraîchis, nous ne voyons le menu nulle part.

En fait, il clignote rapidement avant que la page ne se charge.

Mais où va-t-il, nous pouvons utiliser les outils de développement pour inspecter les éléments et voir qu'ils sont poussés sous le bas de la page par le canvas, nous pouvons en fait essayer différents styles ici pour que cela fonctionne.

Définir un positionnement absolu avec le zéro haut fera l'affaire pour l'instant.

Alors je vais ajouter cela à notre fichier CSS.

En rafraîchissant maintenant, cela fonctionne.

Je peux appuyer sur start et cela randomisera les pièces à chaque fois.

Et si je change le niveau de difficulté, nous voyons les différentes tailles de grilles apparaître.

Je pensais que le mode insensé serait trop intensif pour le processeur au début, mais cela fonctionne bien sur mon ordinateur au moins.

Je suis sûr que certains appareils auront du mal cependant.

Ensuite, nous affichons le temps, je vais définir une fonction appelée UpdateTime qui prend d'abord le temps actuel du système.

Ensuite, elle prend la div avec définie précédemment pour contenir cette valeur et définit le innerHTML à la différence entre maintenant et l'heure de début.

Nous devons appeler cette fonction quelque part.

Alors je vais aller à la fonction updateCanvas qui est appelée à chaque image et l'entrer ici.

Nous avons également remarqué que ce nom n'est plus approprié, car maintenant nous mettons à jour plus que juste le canvas ici.

Alors je vais le refactoriser un peu lorsque je rafraîchis maintenant, j'appuie sur start et cela montre le temps ici mais il est en millisecondes et nous devrions le formater correctement. Je vais d'abord le convertir en secondes en gardant la partie entière des millisecondes lors de la division par 1000, puis je veux considérer ce format.

Alors nous devons connaître la partie secondes entre zéro et 59 et nous l'obtiendrons comme ceci.

La partie minute également entre zéro et 59 peut être obtenue comme ceci.

Et la partie heure est entre zéro et 23.

Et nous l'obtenons comme ceci, je doute que quelqu'un passe plus d'une journée à jouer à cela.

Ensuite, pour les formater dans la chaîne finale.

Je prends chaque composant et je fais un remplissage à gauche avec zéro si nécessaire.

J'utilise une colonne entre chaque partie, puis nous retournons cette valeur finale et c'est tout.

Maintenant, nous pouvons l'utiliser ici pour formater la différence, cela commence à ressembler à un vrai jeu déjà, n'est-ce pas ? Mais rien ne se passe lorsque nous avons terminé.

Nous devons détecter d'une manière ou d'une autre que toutes les pièces sont à l'emplacement correct.

Nous faisons cela en ajoutant un attribut ici qui sauvegardera si l'emplacement est correct ou non.

Initialement, il devrait l'être car les pièces sont définies à l'emplacement correct.

Mais ensuite, lorsque nous les randomisons, nous le définissons immédiatement à false.

Ensuite, lorsqu'une pièce est verrouillée à l'emplacement correct, nous le définissons à nouveau à true.

Il est possible que quelqu'un prenne une pièce de l'emplacement correct.

Alors nous devons la définir à nouveau à false ici sur le clic de la souris.

Ensuite, pour vérifier si toutes les pièces sont correctes, nous écrivons la fonction comme ceci.

Elle parcourt toutes les pièces.

Et si même l'une d'entre elles n'est pas correcte, la fonction retourne false.

Sinon, nous retournons true.

Nous vérifions cela dans la fonction de rappel du clic de la souris.

Parce que le jeu ne peut être complété que lorsque le joueur relâche une pièce, la dernière pièce qui va à l'emplacement correct.

Ici, nous devons également vérifier si l'heure de fin est no car en principe, le joueur peut continuer à déplacer les pièces après la fin du jeu.

Et nous ne voulons plus mettre à jour le temps.

Après cela, nous définissons simplement l'heure de fin ici à l'heure actuelle.

Nous devons également changer l'affichage ici pour que l'heure de fin soit disponible, la différence par rapport à celle-ci est affichée et non la différence par rapport à l'heure actuelle.

D'accord, voyons maintenant, le chronomètre commence à compter comme avant, nous avons joué au jeu.

Et maintenant le chronomètre s'est arrêté.

Maintenant, nous allons rendre cette partie meilleure.

Tout d'abord, mettons le bouton en dessous comme ceci.

Maintenant, nous pouvons passer au fichier CSS et positionner ces éléments au centre de l'écran.

Nous disons que les éléments doivent être à 50 % de la gauche et à 50 % du haut.

Maintenant, si nous laissons cela comme ça, les éléments se déplaceront ici.

Donc leur coin supérieur gauche est au centre de l'écran.

Mais nous aimerions qu'ils soient ici.

Donc nous devons ajouter transform translate moins 50 % moins 50 %.

Et maintenant nous obtenons cela.

Maintenant, le texte n'est pas clairement lisible tel quel, ajoutons l'arrière-plan semi-transparent ici comme ceci.

Mieux maintenant, nous pouvons aligner les éléments au centre comme ceci, nous pouvons donner aux éléments un peu d'espacement en définissant une valeur pour le padding.

J'utilise une valeur de cinq min ici, ce qui signifie que l'espacement sera de 5 % du minimum entre la largeur et la hauteur de la fenêtre.

J'ai également défini la bordure semi-transparente noire ici aussi.

Maintenant, nous pouvons rendre le bouton plus beau.

Nous allons lui donner une taille de police plus grande et une couleur d'arrière-plan bleutée et un texte blanc.

Bien.

Nous pouvons rendre le bouton plus convivial en changeant ses propriétés lorsque la souris le survole.

Je vais lui donner un arrière-plan orange et un texte noir dans ce cas.

D'accord, maintenant lorsque je le survole, le style change.

Vous ne pouvez pas voir ma souris ici maintenant pour une raison quelconque, mais elle est là et elle ressemble à la flèche par défaut pour la faire ressembler à un curseur en forme de main.

Nous pouvons la changer ici en CSS.

De nos jours, il y a beaucoup de fonctionnalités fantaisistes que vous pouvez choisir lors du style des éléments, comme vous pouvez facilement ajouter des animations avec la propriété de transition.

En définissant cette durée de 0,3 seconde ici, nous obtiendrons une courte animation d'un style à l'autre au survol.

Je pense que c'est vraiment bien.

Je n'aime pas cette bordure ici.

Alors je vais l'enlever et cela rendra les coins du bouton arrondis en définissant un petit rayon, la taille de la police à part ce bouton est plutôt petite.

Alors nous allons travailler là-dessus ensuite.

Tout d'abord, je la change en Arial, je pense que la pierre Sarah a très bonne allure dans ce cas.

D'accord, maintenant je vais la rendre plus grande.

La même que la taille de la police sur le bouton.

Je pense que c'est bien maintenant, voyons à quoi cela ressemblerait sur les mobiles aussi.

C'est définitivement lisible, je pense que cela pourrait être un peu plus grand.

Mais cela fera aussi l'affaire pour l'instant, le texte sur le composant select n'est pas encore affecté.

Alors nous devons spécifiquement ajouter la taille de la police là aussi.

D'accord, en revenant à l'écran complet maintenant, je vais changer la souris pour qu'elle ressemble à un pointeur lorsque je survole ce composant select aussi, et styliser cet élément pour qu'il soit plus en ligne avec le bouton.

Alors pas de bordure, un petit rayon, et nous devons enlever le contour ici aussi.

D'accord, essayons de tester le jeu.

Maintenant.

J'appuie sur start, et ce n'est pas ce que nous voulons, vraiment, ce menu devrait disparaître à ce stade, et seul le chronomètre devrait rester visible.

Alors je vais retourner à l'HTML et sortir cet élément d'ici.

Ensuite, dans le fichier JavaScript, nous allons à la fonction restart et définissons l'affichage des éléments du menu à none.

Maintenant, je rafraîchis, appuie sur le bouton start et le menu a disparu.

Mais le chronomètre a également disparu.

Il devrait être là.

Déboguons.

Je passe au panneau Éléments.

Et il est là.

Il est juste en dessous du canvas.

Alors nous devons changer son style en CSS.

Je le veux en haut de l'écran.

Alors je vais changer le positionnement en absolu.

Définir le haut à zéro et avoir le centre de l'écran.

Alors je définis la gauche à 50 %.

Et j'utilise à nouveau la méthode Transform translate, mais seulement sur le côté gauche.

Maintenant, je rafraîchis, appuie sur start et le chronomètre est là.

Ensuite, je vais vous montrer comment dessiner un logo en utilisant PowerPoint.

Vous pouvez utiliser plusieurs logiciels différents pour cela.

J'utilise PowerPoint simplement parce qu'il est installé sur la plupart des ordinateurs des étudiants.

Alors, espérons que vous l'avez aussi.

J'utilise l'outil rectangle arrondi pour commencer à dessiner un appareil photo, je peux ajuster le rayon des coins comme ceci.

Maintenant, je fais une copie de l'élément en maintenant la touche Ctrl enfoncée et en le faisant glisser vers un nouvel emplacement, je vais faire une chose similaire avec des cercles maintenant.

Je vais changer les couleurs en simplement noir et blanc pour les cercles.

Et je vais utiliser les outils d'alignement pour m'assurer qu'ils sont exactement comme je les veux.

J'ai changé la couleur des rectangles dessinés précédemment en noir et j'ai déplacé les cercles par-dessus.

Les nouvelles fonctionnalités de PowerPoint ont ces lignes d'aide qui apparaissent et elles sont utiles, je pense, mais si vous ne les avez pas et que vous voulez avoir un alignement correct, utilisez simplement les outils d'alignement que nous avons utilisés précédemment.

Maintenant, je suis satisfait de l'apparence de cela.

Alors je vais le copier et le coller comme une image, nous en aurons besoin plus tard dans ce format.

Mais maintenant, je veux dessiner une petite pièce de puzzle.

Alors je commence par un rectangle d'environ cette taille.

Et je dessine un ovale ici aussi.

Je vais façonner cet ovale pour qu'il ressemble davantage à la partie de connexion des pièces de puzzle.

Et je fais cela en éditant les points de cette forme.

Clic droit Éditer les points.

C'est utile si vous comprenez comment fonctionnent les courbes de Bézier à ce stade.

D'accord, je suis satisfait de cela.

Je le copie, le fais tourner sur son côté et fusionne ces trois éléments en une seule forme en allant dans fusionner les formes et union.

Maintenant, je vais placer cela par-dessus la copie de l'image de notre caméra, l'aligner un peu mieux et dupliquer les deux objets à droite.

Pour la première copie, nous sélectionnons d'abord l'image de la caméra.

Ensuite, en maintenant la touche Maj enfoncée, appuyez également sur la pièce de puzzle, allez dans fusionner les formes et soustrayez.

Pour la deuxième copie.

Sélectionnez également d'abord l'image de la caméra.

Ensuite, en maintenant la touche Maj enfoncée, appuyez également sur la pièce de puzzle, allez dans fusionner les formes et intersectez.

Je déplace maintenant cette pièce en place pour qu'elle ait l'air de compléter le puzzle.

Maintenant, sélectionnez ces deux objets, copiez et collez son image.

À ce stade, nous n'avons plus besoin de tous les autres éléments.

Nous gardons simplement celui-ci comme icône, et nous l'utiliserons pour faire un titre.

Ensuite, je crée simplement une zone de texte et j'écris puzzle cam ici, en majuscules.

Je définis la police sur Arial Black pour qu'elle soit similaire à celle de la page HTML et j'augmente la taille de la police.

Je rend ensuite le P plus grand, et je veux qu'il soit de la même taille que la caméra.

Alors un peu d'essais et d'erreurs s'imposent ici.

Et lorsque nous en sommes satisfaits, appliquez la même taille à let her see et nous avons presque terminé.

Nous pouvons maintenant copier tout et coller comme une image une fois de plus.

Mais vous verrez que l'image a des marges transparentes étranges ici.

C'est ainsi que fonctionne PowerPoint lorsque des zones de texte sont impliquées, malheureusement, mais nous pouvons les recadrer en utilisant l'outil de recadrage.

Redimensionnez l'image à la taille souhaitée.

Clic droit et enregistrez sous image.

Ensuite, je la nomme this title dot png et je l'ajoute au même répertoire que notre code.

En parlant de cela, nous pouvons maintenant ajouter la nouvelle image au fichier HTML comme ceci.

Et je vais définir sa largeur à 90 % en ligne ici, car il n'y a pas d'autre style que je vais ajouter à cela, puis le rafraîchissement fait apparaître l'image.

Je pense que cela aura l'air mieux si nous apportons un petit changement en CSS, je vais rendre tout le menu plus large comme ceci.

De cette manière, l'image du titre est significativement plus grande que l'autre texte et la liste déroulante pour la difficulté se déplace sur la même ligne que l'étiquette.

Je pense que c'est mieux comme ça, ajoutons quelques sons ensuite.

Tout d'abord, je vais en définir un en utilisant un fichier mp3 que j'ai enregistré plus tôt comme ceci, je vais régler le volume assez bas.

Parce que cela jouera chaque fois que nous déposons une pièce à l'endroit correct.

Ce serait vraiment ennuyeux si cela joue à volume maximum, je pense.

Alors ajoutons-le ici dans la méthode snap et testons.

Je rafraîchis la page, appuie sur start et hourra, cela fonctionne.

Mais il n'y a pas de son lorsque le jeu est terminé.

Et il doit définitivement y avoir quelque chose là.

Au lieu de simplement ajouter un autre fichier mp3 ici, ce qui rendrait ce tutoriel vraiment court.

Je vous rappellerai qu'il est possible de synthétiser des sons en JavaScript.

Pour générer les sons, nous devrons définir un contexte audio et le faire comme ceci fonctionnera sur la plupart des navigateurs.

Ensuite, je veux créer une simple mélodie composée de trois notes jouées sur des touches de piano.

Ici, j'écris leurs fréquences, nous devons créer une fonction pour jouer une seule note, elle aura une clé spécifiée et une durée donnée, combien de temps la clé doit être pressée.

Nous définissons ensuite un oscillateur.

Celui-ci sera responsable de la génération du son avec une fréquence donnée.

Nous définissons la fréquence à la valeur venant comme paramètre ici.

Nous démarrons l'oscillateur comme ceci à l'heure actuelle.

Et nous pouvons également lui dire de s'arrêter après la durée spécifiée.

Il est bon de déconnecter également l'oscillateur en même temps.

Sinon, un bruit de fond à peine perceptible peut encore être entendu sur certains navigateurs.

J'utilise setTimeout pour cela.

Et j'ai spécifié la durée ici également.

Maintenant, il y a un problème car setTimeout attend la durée en millisecondes, mais la méthode stop l'attend en secondes.

Alors je l'ai décidé en millisecondes et je dois diviser ici par 1001.

Une autre chose que nous devons faire avant de tester est de connecter l'oscillateur à la destination, qui dans ce cas est les haut-parleurs par défaut de votre appareil.

D'accord, testons.

Je fais cela en appelant la note de jeu ici dans la console.

Et nous obtenons une erreur, il semble que je ne sache pas comment épeler oscillateur.

Laissez-moi simplement corriger cela rapidement.

Et vous pouvez entendre un simple son pendant une seconde.

Maintenant, nous commençons à façonner cela pour que cela ressemble davantage à un piano, je vais utiliser une enveloppe pour contrôler le jeu, vous pouvez la considérer comme le volume en essence, je connecte l'enveloppe maintenant à la destination.

Et j'ai changé l'oscillateur ici pour qu'il soit connecté à cette enveloppe à la place, formant une sorte de chaîne, puis le son du piano a une attaque puissante, ce qui signifie qu'il doit passer de zéro au gain maximum très rapidement.

Ici, cela se produit en 0,1 seconde, je définis le maximum ici à 0,5 au lieu de un pour qu'il ne soit pas trop fort, puis le gain diminuera progressivement pour revenir à zéro pendant la durée donnée, à nouveau spécifiée ici en secondes.

Maintenant, rafraîchissons et testons une autre erreur.

Je suis sûr d'en faire beaucoup aujourd'hui, il semble que le problème soit que je connecte l'oscillateur ici à l'enveloppe avant même de la définir.

Alors le déplacer vers le bas ici devrait fonctionner.

Vous pouvez maintenant entendre le son s'estomper progressivement au cours d'une seconde.

Et vous pouvez obtenir un son encore plus agréable en changeant le type d'onde du signe par défaut en triangle.

Si vous avez du mal à comprendre ces choses, consultez mon cours de développement web visuel.

Là, j'utilise un rythme beaucoup plus lent et j'explique toutes les différentes techniques dont j'avais besoin pour faire mon piano à réalité augmentée.

Maintenant, composons la mélodie elle-même.

Elle commencera par une simple note jouée d'abord pendant 300 millisecondes, puis je jouerai une note différente après 300 millisecondes.

Et une autre 300 millisecondes après cela, ou 600 millisecondes à partir du point de départ.

Et ce que nous obtenons est ceci.

Maintenant, cela pourrait fonctionner comme la mélodie, mais vous êtes libre de la faire sonner comme vous le souhaitez.

Par exemple, elle pourrait sonner comme ceci maintenant pour la jouer lorsque le puzzle est terminé, nous appelons simplement cette fonction ici.

Cela sonne un peu mal car cela se superpose au bruit final de clic lorsque la pièce se verrouille en place.

Je corrige cela en ajoutant un petit délai ici à l'appel de la fonction.

Pour stocker les scores, nous devrons utiliser une sorte de base de données. Je recommande d'aller au lien suivant et de télécharger XAMPP, il est livré avec MySQL et PHP myadmin, qui est une interface utilisateur agréable pour gérer le contenu de la base de données.

Sample inclut également le serveur Apache, dont nous aurons besoin pour écrire le code backend PHP.

Après avoir installé sample, nous allons au Panneau de contrôle et démarrons ces deux services.

Ensuite, nous nous dirigeons vers la page d'administration.

À partir de là, nous pouvons ouvrir PHP myadmin et commencer à construire notre base de données pour contenir les scores.

Nous créons la nouvelle base de données en appuyant sur le bouton Nouveau à gauche et nous donnons un nom à notre base de données. Maintenant, nous devons créer une table pour les colonnes, c'est très bien.

Et appelons-la scores.

Maintenant, chaque table MySQL devrait avoir un champ ID, nous le laissons comme type entier et le marquons comme clé primaire.

Et cocher cette case ici pour qu'il s'incrémente automatiquement.

Cela signifie que chaque fois que nous ajouterons un nouveau score, nous n'aurons pas à nous soucier de son ID, il sera automatiquement décidé par MySQL.

Ensuite, nous devrons stocker le nom du joueur ici, ce sera une chaîne, donc nous utiliserons var char comme type de données.

Et mettre la longueur maximale de 255 caractères ici pourrait être un peu trop, mais on ne sait jamais quels noms les gens inventent.

Ensuite, nous stockerons le temps, il peut être un entier car je prévois de stocker le nombre de secondes.

Je peux également ajouter le commentaire ici pour clarifier le format afin de ne pas avoir à m'en souvenir plus tard.

Et enfin, stockons le niveau de difficulté afin de pouvoir regrouper les scores en fonction de cela.

Maintenant, nous appuyons sur Enregistrer, et nous pouvons voir la structure de la table ici.

Ajoutons quelques données d'exemple pour travailler.

Ce seront des données fictives pour l'instant, nous allons à insérer et commençons à entrer des valeurs dans chaque champ.

Mais comme je l'ai dit plus tôt, nous n'avons pas à nous soucier de l'ID, il sera automatiquement généré par MySQL.

Je vais simplement ajouter mon nom ici.

Et disons qu'il m'a fallu 50 secondes pour compléter le puzzle en mode Facile.

Ensuite, j'ajouterai Rado à nouveau et 100 secondes en jouant en mode Moyen et à nouveau avec 200 secondes en mode Difficile.

Et enfin 4000 secondes en mode Insensé.

Alors maintenant, il semble que j'ai joué au jeu à tous les niveaux de difficulté.

Ajoutons quelques personnes ici comme John avec 20 secondes en mode Facile et 1000 secondes en mode Insensé, Diana avec 100 secondes en mode Difficile et 400 secondes également en mode Difficile.

Michael avec 400 secondes en mode Moyen, et Leo avec 10 secondes en mode Moyen.

Maintenant, nous appuyons sur Go et toutes ces 10 entrées ont été ajoutées dans la table, nous pouvons cliquer sur l'onglet Parcourir pour l'inspecter.

Maintenant, nous pouvons en fait voir ici la requête SQL qui affiche cette table entière.

Elle dit sélectionner tout de scores.

Nous devrons écrire des requêtes similaires en PHP pour communiquer entre notre jeu frontal et la base de données.

Cette requête ici pourrait être utile pour charger les scores par exemple, mais elle n'est pas très agréable en tant que telle, elle mélange tous les niveaux de difficulté et n'est pas triée de quelque manière que ce soit.

Difficile de voir qui sont les gagnants comme ça.

Alors dirigeons-nous vers la recherche et disons que nous voulons uniquement les entrées avec une difficulté facile.

Nous pouvons voir comment la requête SQL ici est également mise à jour.

Je pense que cet outil PHP myadmin est très utile pour apprendre la syntaxe SQL.

Vous pouvez également pratiquer l'écriture de la syntaxe par vous-même en appuyant sur modifier.

Ici, nous pourrions par exemple ajouter une clause ORDER BY pour que les résultats soient triés par temps.

Maintenant, il est vraiment facile de voir que John est le gagnant lorsqu'il joue en mode facile, nous pouvons obtenir de manière similaire les résultats pour les autres niveaux de difficulté.

Nous devons simplement changer la difficulté ici à chaque fois.

Nous utiliserons cette requête plus tard en PHP pour obtenir les meilleurs scores.

Maintenant, pour ajouter le nouveau résultat, nous utilisons le mot-clé Insert.

Nous spécifions le nom de la table et les colonnes qui recevront les données et ensuite les valeurs réelles qui y vont.

Notez ici que le nom et la difficulté sont des chaînes.

Donc ils doivent être spécifiés en utilisant des guillemets, sinon vous obtiendrez une erreur.

Ensuite, nous appuyons sur Go et obtenons un retour indiquant qu'une ligne a été insérée.

Si nous parcourons à nouveau la table, nous verrons une nouvelle entrée pour notre difficulté insensée.

Maintenant, nous allons pratiquer ces requêtes en utilisant PHP.

Et comme c'est la première fois que je l'enseigne, je vais y aller lentement.

J'ai déplacé tous les fichiers du projet du jeu construit jusqu'à présent dans le répertoire HT docs de SAP.

Maintenant, je vais créer un fichier vide appelé server.php.

Nous ouvrons ensuite ce fichier dans notre éditeur de texte et dans le navigateur.

Mais notez ici, l'adresse est localhost/puzzlecam/server.php, vous devez l'écrire comme cela, car alors le code PHP est exécuté par le serveur Apache, je vous rappelle que vous devez avoir samp installé et Apache et MySQL en cours d'exécution à ce stade.

Maintenant, le code PHP est assez différent de JavaScript, la syntaxe commence et se termine comme ceci, et tout le code va entre les deux.

Si vous voulez imprimer quelque chose ici, vous utilisez le mot-clé echo, suivi de ce que vous voulez imprimer.

Si vous actualisez la page, vous obtenez exactement cela.

Maintenant, je vais vous apprendre à connecter la base de données MySQL que nous avons créée précédemment.

Parce qu'elle est également en cours d'exécution localement sur notre ordinateur, nous utiliserons localhost comme hôte.

L'utilisateur par défaut est root et le mot de passe est vide.

Bien sûr, si vous allez mettre cela en ligne quelque part, vous voudrez ajouter une meilleure sécurité, mais je ne me concentrerai pas sur cela dans cette vidéo.

Ensuite, pour se connecter à la base de données, nous utilisons la fonction MySQL y connect et fournissons ces informations.

Si le lien n'a pas été établi, nous avons averti que la connexion a échoué.

La fonction DI termine également le script PHP.

Si le code passe l'instruction if, il ira ici où nous affichons simplement que la connexion a réussi.

Je vais actualiser et la connexion a réussi.

Mais si je spécifie un hôte différent, PHP produira des messages d'avertissement, et le programme se termine après cette instruction die.

Nous obtenons également un message d'erreur si nous utilisons le mauvais utilisateur ou mot de passe.

Maintenant, avec une connexion réussie, nous pouvons passer à la sélection de la base de données comme ceci.

Et nous pouvons utiliser le mot-clé or pour appeler la fonction DI en cas d'échec.

Si le code atteint ici, il affichera le message de succès, nous pouvons tester et voir que c'était un succès car la base de données puzzlecam existe vraiment.

Si nous faisons une erreur ici et utilisons un nom différent, par exemple, le code se terminera avec une erreur.

Définissons maintenant une requête SQL comme une simple chaîne.

J'utiliserai la requête que nous avons déterminée précédemment en utilisant PHP myadmin pour sélectionner les entrées de la table Scores avec une difficulté facile.

Nous pouvons exécuter cette requête en utilisant la fonction MySQL I query.

Maintenant, cette fonction ne retourne pas réellement le résultat.

Mais un objet que nous pouvons utiliser pour itérer à travers les résultats, je vais vous montrer, nous initialisons d'abord un tableau vide.

Ensuite, si le résultat contient des lignes, nous utiliserons une boucle while pour récupérer chaque ligne une par une en utilisant la fonction MySQL I fetch Asok sur l'objet RS.

Nous ajoutons chaque ligne au tableau des résultats en utilisant la fonction array push, et imprimons ensuite le tableau en utilisant la fonction print our comme ceci.

Et nous obtenons une erreur.

J'ai oublié un i ici, il devrait être my SQL I num rows.

Maintenant, nous avons le tableau imprimé ici, mais il n'est pas trié par rapport au score, ou dans ce cas, le temps de jeu.

Comme nous l'avons vu précédemment, nous pouvons faire cela en utilisant la clause ORDER BY.

Je vais également formater cette requête un peu mieux pour qu'elle ne dépasse pas de l'écran.

Notez qu'en PHP, le signe d'arrêt est utilisé pour la concaténation, et non le plus comme en JavaScript et de nombreux autres langages de programmation.

Maintenant, parce que nous allons réutiliser ce code pour obtenir des résultats pour d'autres niveaux de difficulté, il est logique d'écrire cela comme une fonction qui retourne le tableau des résultats.

Nous pouvons alors l'appeler avec facile comme paramètre et obtenir le même résultat.

Laissez-moi simplement remplacer ici la difficulté pour utiliser cet argument et j'ai presque oublié de spécifier le lien ici également.

Maintenant, nous rafraîchissons et obtenons le même résultat qu'auparavant.

Mais nous pouvons obtenir d'autres résultats également en appelant à nouveau la fonction.

Laissez-moi ajouter rapidement les autres niveaux de difficulté également.

Maintenant, enveloppons tout cela dans une fonction pour obtenir tous les scores.

Nous n'avons plus besoin de ces instructions d'impression, nous pouvons simplement retourner un tableau associatif avec chacun de ces résultats.

Les tableaux associatifs sont comme des objets JavaScript, où nous pouvons donner des noms aux clés.

Maintenant, nous appelons cette fonction et imprimons le résultat comme ceci.

Ou pour être plus familier, vous pouvez utiliser Echo et convertir ce tableau de résultats en une chaîne JSON comme ceci.

C'est génial que PHP prenne en charge tout cela sans avoir besoin d'installer de bibliothèques.

Je vais commenter cela et me concentrer sur la création de l'autre fonction, nous devrons ajouter le nouveau score à la base de données.

Je vais passer les informations comme premier argument.

Pour l'instant, j'écrirai la requête comme une simple chaîne avec des valeurs codées en dur ici, puis remplacer chaque valeur une par une avec les éléments de l'info.

Si vous écrivez votre requête comme ceci, il est moins probable de faire des erreurs.

Sinon, il est assez facile de se tromper et d'oublier la simple quote ou une double quote quelque part.

Maintenant, nous appelons à nouveau mySQL like query, si nous ne réussissons pas pour une raison quelconque, nous retournerons false.

Sinon, nous retournons true pour signifier le succès.

Maintenant, nous pouvons tester la fonction comme ceci en définissant une info et en appelant la fonction Add score en l'utilisant.

Nous pouvons l'envelopper dans une instruction if comme ceci, pour voir si l'insertion a réussi ou non.

Et elle prétend avoir fonctionné.

Laissez-moi maintenant ramener cet appel de fonction pour obtenir tous les scores et voir si cela a vraiment fonctionné.

Et c'est le cas.

Génial.

Maintenant, nous allons changer ce serveur PHP pour prendre en charge les deux fonctionnalités : ajouter le score et lire tous les scores.

Laissez-moi d'abord supprimer ce code de test.

Maintenant, j'utiliserai un paramètre get nommé info pour envoyer des informations supplémentaires à la page.

Lisons-le d'abord ici et voyons comment cela fonctionne.

Alors je dois définir ici info égal à quelque chose.

Essayons hello pour l'instant.

Et vous pouvez voir qu'il est effectivement imprimé ici.

Je vais changer info maintenant pour contenir les informations nécessaires à l'ajout du score.

Et je vais l'écrire comme une chaîne JSON.

Maintenant, pour analyser cette chaîne, j'appelle Jason decode et get info est un objet ici, que je peux passer à notre fonction ad score que nous avons écrite précédemment, et gérer le résultat comme avant.

Maintenant, nous pouvons insérer le score en visitant simplement cette adresse avec certains paramètres.

Je vais maintenant faire en sorte que si nous n'envoyons aucune info, il listera tous les scores à la place.

De cette manière, nous prenons en charge à la fois la lecture et l'écriture dans la base de données avec ce seul script.

Maintenant, laissez-moi aborder l'éléphant dans la pièce.

Oui, ce code n'est pas très sécurisé.

N'importe qui peut pirater ma base de données de scores en allant à ce lien et en envoyant des données là-bas.

Encore pire, ces données ne sont pas échappées de quelque manière que ce soit.

Alors ils peuvent même faire des dégâts par des injections SQL ici.

Tous ces problèmes ne sont pas faciles à résoudre.

Et si je passe du temps dessus maintenant, cela s'écartera trop du projet.

Nous construisons un jeu de puzzle, pas la chose la plus sécurisée au monde.

Mais parce que beaucoup d'entre vous sont intéressés par la sécurité, voici ce que vous devriez faire.

Tout d'abord, échappez les informations ici ou mieux encore utilisez un PreparedStatement, changez get ici en post, c'est plus sécurisé.

Je ne l'ai pas fait moi-même parce que j'aurais besoin de quelque chose comme postman pour tester.

Et je ne voulais pas installer plus d'outils ici.

Post est également la pratique courante lors de l'envoi de données, alors vous devriez définitivement l'utiliser ici.

Ensuite, vous voudrez ajouter une certaine authentification ici pour que tout le monde ne puisse pas faire une demande comme celle-ci, vous devrez demander aux gens de s'inscrire et de confirmer leur compte en leur envoyant un e-mail de confirmation.

Je ne le fais généralement pas pour mes petits projets, je sens que je demanderais trop à ceux qui visitent mon site web.

Et ils trouvent piraté.

Alors je n'ai pas d'informations sensibles ici, et j'aime bien l'attention.

Toutes ces étapes ne rendent pas le système à toute épreuve.

Mais chacune d'elles le rend un peu plus difficile à pirater.

Vous pourriez aller encore plus loin en ajoutant un CAPTCHA parce que quelqu'un pourrait automatiser l'authentification s'il le veut vraiment et inonder votre base de données avec un tas de faux comptes et de faux scores.

Les CAPTCHA rendent cela plus difficile à faire mais pas impossible.

Vous pourriez concevoir un système de vérification de validité ici, peut-être enregistrer l'heure de début et l'heure et les mouvements individuels.

Si le résultat ne contient pas de pièces se déplaçant une par une, à des intervalles de temps raisonnables, c'est un signe de jeu déloyal.

Bien sûr, on pourrait aussi pirater cela, en découvrant comment fonctionne le vérificateur de validité et en générant de fausses données qui semblent réelles.

Mais c'est tout ce que j'ai.

Alors faites-moi savoir si vous avez de meilleurs conseils sur la sécurité.

Je suis vraiment intéressé de savoir ce que vous pensez.

Mais maintenant, continuons avec la partie frontale.

Laissez-moi remettre Mr chibi son ici.

En HTML, je vais maintenant créer un écran de fin, il montrera le score et permettra à l'utilisateur d'entrer son nom dans ce champ de saisie.

Il y aura également un bouton pour sauvegarder le score, au clic, nous devrons implémenter cette fonction saveScore en JavaScript.

J'ajouterai également ici un bouton pour afficher les scores avec une autre fonction que nous devrons définir et un autre bouton pour revenir au menu.

Je vais également créer l'écran des scores.

Il contiendra une div vide, qui contiendra éventuellement les scores et un bouton pour revenir à l'écran de fin, nous devrons définir cette fonction JavaScript également.

Maintenant, je vais copier cette image de titre dans ces deux écrans pour qu'ils aient une apparence cohérente.

Et en parlant d'apparence, je vais définir une classe CSS appelée menu et l'appliquer à tous ces éléments.

Cette classe aura le même style que nous avons précédemment appliqué à la div avec l'ID menu items.

Alors nous changeons simplement cela ici en CSS.

Maintenant, nous rafraîchissons et nous pouvons voir les trois écrans se chevaucher, nous devons masquer l'écran de fin et l'écran des scores au début bien sûr.

Maintenant, commençons à définir les fonctions manquantes en JavaScript.

Tout d'abord, ils veulent afficher l'écran de fin, je vais simplement utiliser le temps de jeu comme score et je vais le placer à l'intérieur de l'élément avec l'ID score value.

Nous devons également calculer ce temps comme l'heure de fin moins l'heure de début, nous devons nous assurer que l'élément de l'écran de fin devient visible comme ceci.

Ensuite, la fonction pour afficher le menu commencera par fermer l'écran de fin et ensuite rendre le menu visible ici.

Maintenant, si je rafraîchis et appuie sur start, le menu disparaît comme avant.

Mais si j'appelle la fonction showEndScreen ici dans la console, l'écran de fin apparaît et il a l'air bien.

Mais le score est maintenant quelque chose d'étrange car nous n'avons pas réellement complété le puzzle pour obtenir la vraie valeur pour l'heure de fin.

Cela ira bien lorsque nous jouerons au jeu pour de vrai, nous n'avons pas à nous en soucier.

Maintenant, appuyer sur le menu ne fonctionne pas.

Oh, j'ai oublié la parenthèse ici.

Nous devons appeler cette fonction ici au clic.

Désolé pour cela.

Corrigeons cela et rafraîchissons, démarrons, appelons la fonction showEndScreen dans la console.

Appuyez sur menu et oui, cela fonctionne maintenant, passons à l'affichage des scores ensuite.

Je vais copier cette ligne pour que l'écran de fin s'en aille et faisons apparaître l'écran des scores à la place.

Maintenant, je vais faire en sorte que le conteneur des scores soit initialement affiché avec le texte de chargement car cela peut prendre un certain temps pour charger le score.

Et nous voulons faire savoir au joueur que quelque chose se passe.

Nous obtenons ensuite les scores avec la fonction que nous implémenterons ensuite.

Cette fonction getScores utilise fetch pour obtenir des données de server.php, qui, je le rappelle, se trouve dans le même répertoire ici, fetch retourne une promesse.

Lorsque la réponse est disponible, nous la convertissons en JSON.

Cela retourne une autre promesse.

Alors nous devons écrire then à nouveau.

Et ici nous avons accès aux données réelles.

Journalisons-les dans la console pour tester, je rafraîchis, appuie sur start, appelle showEndScreen dans la console, et appuie sur Show scores.

Et maintenant nos données sont ici.

Cela montre toujours le chargement, car maintenant nous devons formater les scores et les placer ici.

Au lieu de cela, la fonction formatScores générera le tableau en HTML.

Je ne vais pas expliquer cela trop, je sens que ce tutoriel devient trop long si je le fais.

Et si vous avez pu suivre jusqu'ici, je suis sûr que vous n'aurez aucun mal à comprendre ce que cela est.

Je dirai cependant que maintenant, lorsque j'ai les résultats formatés pour facile, je vais extraire cette fonctionnalité dans sa propre fonction.

C'est une très mauvaise habitude d'écrire un code similaire au lieu d'utiliser des fonctions.

Et beaucoup de mes étudiants ont ce problème.

Alors j'ai pensé à le signaler ici aussi.

J'appelle maintenant cette fonction pour chaque niveau de difficulté pour montrer tous les résultats les uns après les autres.

La liste finale est simplement trop longue.

Je vais définir une hauteur fixe ici et overflow à auto pour que la barre de défilement apparaisse.

C'est mieux, je pense.

Maintenant, j'appuie sur retour, et je suppose qu'il est temps de définir la fonction closeScores.

Cela est facile à faire, cela rendra l'écran N visible et masquera l'écran des scores.

Maintenant, je rafraîchis et tout semble fonctionner bien, sauf pour la fonction de sauvegarde qui n'est pas encore implémentée.

La fonction SaveScore va calculer le score comme le temps qu'il a fallu pour jouer au jeu et obtenir le nom du joueur à partir du champ de saisie.

Si aucun nom n'est saisi, nous donnons un avertissement et arrêtons la fonction ici.

Sinon, nous obtenons la difficulté à partir de l'élément select et faisons un fetch à server.php en utilisant le paramètre info où nous passons le nom, le temps de jeu et le niveau de difficulté.

Pour donner un retour à l'utilisateur, je vais changer le texte sur le bouton Save pour dire okay pendant le fetch, je désactive ce bouton pour que les joueurs ne puissent pas l'appuyer plusieurs fois par erreur.

Je réinitialise également le texte sur le bouton Save lors de l'ouverture de l'écran de fin à nouveau, au cas où le joueur jouerait une deuxième fois, et ils devraient réactiver le bouton également.

Ajoutons le style gris pour le bouton désactivé et faisons en sorte que le curseur soit une flèche par défaut indiquant qu'il peut être cliqué.

Maintenant, voyons une erreur.

Bien sûr, il semble que j'ai oublié la parenthèse fermante.

Avant de tester, appelons également la fonction showEndScreen ici lorsque le puzzle est terminé et testons pour de vrai cette fois.

D'accord, cela fonctionne assez bien.

Mais mon score ici est en millisecondes au lieu de secondes.

Mais en y réfléchissant, je pense qu'il est préférable de garder ceux-ci en millisecondes afin que nous puissions mieux distinguer les personnes jouant presque au même moment, je formate le score pour afficher le nombre de secondes, mais je garde les millisecondes dans la base de données afin que l'ordre de la liste classée provienne de cela.

D'accord, maintenant le score semble être le nombre de secondes.

Et le tableau des scores a l'air bien pour ceux qui ont zéro car nous considérons maintenant qu'ils ont joué en 20 et 50 millisecondes.

Mais lorsque nous effacerons la base de données et que les gens commenceront réellement à jouer à cela, ce problème disparaîtra.

Une chose qui me dérange encore est que le bouton de sauvegarde est sur la ligne suivante, mais ensuite il devient plus petit lorsqu'il dit okay, et il saute vers le haut.

Je vais corriger cela en rendant la saisie plus petite afin que le bouton tienne toujours sur la même ligne.

Je vais également le styliser pour qu'il soit plus cohérent avec les autres éléments.

D'accord, super.

Maintenant, nous allons faire quelques ajustements fins et travailler sur le style des pièces pour qu'elles ressemblent à de vraies pièces de puzzle.

Pour cela, nous allons à la fonction initializePieces et itérons à travers la grille de pièces comme ceci, les pièces sont stockées dans une liste dans cet ordre de haut en bas et de gauche à droite.

Alors nous pouvons obtenir l'index de chaque pièce en comptant simplement ici comme ceci.

Maintenant, nous prenons chaque pièce une par une, et i n j pointeront vers la ligne et la colonne où elle appartient.

Nous devons maintenant ajouter des informations sur ces choses à chaque pièce, appelons-les tabs.

Pour chaque tab, nous devons savoir si c'est un tab intérieur ou un tab extérieur, nous déciderons cela aléatoirement avec une probabilité égale comme ceci.

Alors le signe devient soit un moins un soit un plus un, indiquant s'il s'agira d'un tab intérieur ou extérieur.

La deuxième chose que nous devons décider est où le tab sera situé sur le bord.

Si nous considérons que cela commence à zéro et se termine à 100 %, permettons au tab d'être n'importe où entre 30 % et 70 %.

Se rapprocher trop des coins n'est pas une bonne idée.

Je vais maintenant définir cet attribut bottom pour encoder les informations pour le tab en bas.

Il s'agira d'un seul nombre entre 0,3 et 0,7.

S'il s'agit d'un tab extérieur, et entre moins 0,7 et moins 0,3.

S'il s'agit d'un tab intérieur, notez comment nous stockons les deux morceaux d'informations avec ce simple truc.

Si nous sommes sur la dernière ligne, nous n'avons aucun tab en bas ici.

Alors nous définissons cela à No.

Nous faisons maintenant la même chose pour le tab à droite et nous assurons que je n'ajoute pas de tabs sur la colonne la plus à droite.

Les tabs en haut ne seront plus aléatoires, car ils doivent se connecter avec les pièces du dessus, nous devons définir le haut pour qu'il soit moins la valeur du bas de la pièce directement au-dessus.

Si nous sommes sur la première ligne, nous n'avons pas de tab en haut, nous gérons maintenant le tab de gauche de manière similaire, nous utilisons la valeur de moins l'attribut droit de la pièce précédente.

Maintenant, rafraîchissons, agrandissons cette console et vérifions ici à quoi ressemble le tableau des pièces.

Alors la première pièce a une valeur positive ici, ce qui signifie qu'elle devrait être un tab extérieur.

La valeur de droite est négative, ce qui signifie qu'il s'agit d'un tab intérieur.

Nous n'avons pas de gauche et de haut.

Alors cela a l'air bien jusqu'à présent.

Pour la deuxième pièce, nous devons vérifier si la valeur de gauche est ce nombre mais inversé.

Alors voyons.

Oui, cela a l'air bien.

Vérifions à nouveau avec la pièce suivante.

Bien.

Et maintenant nous obtenons droite égal à non car nous sommes sur la colonne la plus à droite.

Maintenant, la pièce suivante est sur la ligne suivante.

Alors le haut n'est plus normal.

Et il devrait être l'opposé du bas de la première pièce.

Ce qui est bien.

Regardons la dernière pièce maintenant.

Elle n'a pas de valeurs pour le bas et la droite et les valeurs pour la gauche et le haut ont l'air correctes.

Oui, je pense que nous sommes bons.

Dessinons maintenant de nouvelles formes pour les pièces en utilisant ces informations supplémentaires.

Nous n'utiliserons plus la méthode rect ici, mais pour l'instant, je vais simplement la réimplémenter en utilisant les commandes moveTo et lineTo.

Laissez-moi simplement ajouter des commentaires ici pour expliquer où chacune de ces lignes va.

Maintenant, le rafraîchissement ne change rien.

Les pièces sont toujours de forme rectangulaire.

Mais maintenant, nous avons plus de contrôle sur ce dessin.

J'aurai besoin de connaître la longueur minimale de la pièce et de l'utiliser pour définir certaines caractéristiques visuelles du tab par rapport à celle-ci, comme le cou, la largeur et la hauteur du tab.

Maintenant, faisons d'abord un détour sur notre chemin vers le haut à droite comme ceci.

L'emplacement du tab est donné par la valeur absolue de l'argument du haut.

Nous nous déplaçons sur l'axe vertical de la hauteur du tab dans la direction donnée par le signe de la valeur du haut.

Rafraîchissons maintenant et voyons ce qui se passe.

Alors les bases ressemblent un peu à des maisons avec une sorte de toit.

Pour certaines, leur toit va vers l'intérieur comme ceci.

Laissez-moi désactiver le dessin de la vidéo pour l'instant.

C'est confus, je pense.

Alors maintenant vous voyez simplement la forme des pièces, mais vous pouvez en fait dire que celles avec le toit plat appartiennent en haut.

Alors nous commençons à voir que la forme des pièces aide vraiment lorsque l'on joue au jeu et rend l'expérience globale plus agréable.

Continuons.

J'ajouterai des détours similaires pour les autres côtés également.

Nous rafraîchissons et regardons cela.

Nous obtenons une division intéressante maintenant, je pense que cela pourrait en fait être une autre version du jeu si c'était voulu, c'est assez unique, je pense.

Quelle erreur, d'où vient-elle ? Ah, je vois.

Il semble que cela se produise lorsque je clique en dehors de la pièce.

Cela ici est considéré comme étant en dehors de la pièce parce que nous utilisons toujours la forme rectangulaire pour la détection des clics.

Mais l'erreur apparaît chaque fois que je clique ici également.

Je n'arrive pas à croire que j'ai manqué cela.

Nous devons nous assurer que la pièce sélectionnée n'est pas nulle avant de vérifier si elle est proche ou non.

D'accord, plus d'erreur.

Remarquez également que chaque fois que nous rafraîchissons, nous obtenons des pièces d'apparence différente.

C'est vraiment bien, je pense.

Mais maintenant, créons les onglets.

Je vais faire deux autres détours, un avant ce point et un après.

Et nous utilisons la valeur du cou que nous avons définie précédemment.

Laissez-moi maintenant écrire rapidement ceci pour les autres côtés également.

Je rafraîchis maintenant et cela a l'air bien.

Mais vous voyez que certaines pièces ont des lignes étranges qui dépassent.

Toutes les pièces ne l'ont pas.

Celle-ci est bien car elle a des onglets sur tous les côtés.

Le problème est que nous ajoutons ces nouveaux détours.

Même lorsqu'un bord n'a pas d'onglet, nous devons vérifier si nous devons dessiner l'onglet.

Sinon, nous nous contentons de dessiner jusqu'à la fin du bord.

Et c'est tout.

Je vais ajouter rapidement ceci aux autres côtés également.

Et maintenant les choses ont l'air assez bien.

Et remarquez que parce que nous travaillons avec des valeurs relatives à la taille des pièces, cela fonctionnera comme prévu à chaque niveau de difficulté lorsque cette taille change.

Pas besoin de faire quoi que ce soit de spécial ici du tout.

Maintenant, cette forme n'est toujours pas parfaite, nous devons ajouter quelques courbes, nous remplacerons cette ligne ici par la courbe de Bézier.

Au lieu de cela, je vais la définir avec l'aide de deux points de contrôle.

Et ce même point final d'avant, il semble que quelque chose ne va pas ici.

Je pense qu'il me manque cette parenthèse fermante.

Mais laissez-moi arranger ce code mieux de toute façon.

Rafraîchissement et maintenant vous pouvez voir ce qui s'est passé ici.

Cela fait une courbe au lieu d'une ligne droite.

Je vais faire la même chose du côté droit.

Je copie simplement ces lignes dans l'ordre inverse et je change ce moins en un plus ici.

Et ici.

Nous le rendons essentiellement symétrique.

Testons et cela a l'air bien.

Je pense que si vous voulez qu'il ait l'air différent, vous pouvez changer ces valeurs ici.

Comme vous pouvez rendre le cou plus étroit.

Ou vous pouvez rendre l'onglet plus large par exemple.

Vous pourriez en fait même avoir différentes propriétés pour chaque pièce si vous le souhaitez.

Ce n'est pas trop compliqué, mais je pense que c'est excessif et je suis satisfait de cela étant codé en dur ici.

Remarquez que cela a également affecté les autres onglets maintenant.

Ils sont plus minces et plus longs.

Je vais les rendre tous courbés ensuite en ajoutant un code similaire dans chacune de ces sections.

C'est ici que je dirais habituellement que nous devrions extraire la fonction comme Draw tab ou quelque chose, mais je n'ai pas pu penser à de bons noms de paramètres, et cela rendrait en fait certaines choses plus compliquées à l'intérieur de la fonction.

Alors j'ai décidé de le laisser comme ça.

Mais le conseil reste valable, juste parce que je ne peux pas trouver comment le faire proprement ne signifie pas que cela ne peut pas être fait.

D'accord, voyons ici.

Bien.

Et encore une fois, cela fonctionne sur n'importe quelle taille de pièces maintenant, tout ce que nous devons faire est de remettre la vidéo.

Je vais déplacer le code sec ici.

Et avant cela, j'appelle la méthode clip du contexte.

Et je sauvegarde l'état avant le clip et le restaure après l'appel à drawImage pour qu'il n'affecte pas les pièces suivantes de manière étrange.

Maintenant, certaines des pièces ont l'air super comme celle-ci, mais celles qui ont un onglet extérieur manquent de la vidéo à l'intérieur.

Nous corrigeons cela en prenant la vidéo avec un peu de remplissage sur chaque côté, un remplissage égal à la hauteur de l'onglet est suffisant.

Parce que la taille du puzzle et la taille de la vidéo ne correspondent pas, nous devons mettre à l'échelle cette hauteur de l'onglet pour les quatre premiers paramètres comme ceci, notez qu'ils divisent ici par la taille.

Alors essentiellement, je simplifie ici, il aurait été préférable de stocker uniquement les valeurs en pourcentage.

Mais je remarque cela seulement en éditant la vidéo, alors maintenant il est trop tard.

Quoi qu'il en soit, cela fonctionne ou non.

Il semble que j'ai une parenthèse supplémentaire ici.

Elle est censée se fermer après la méthode principale ici.

Maintenant, cela fonctionne et cela a l'air super.

La seule chose restante est de gérer lorsque l'utilisateur clique à l'intérieur des onglets.

Les onglets extérieurs ne sont pas cliquables, et l'onglet intérieur sélectionne la pièce même lorsqu'il ne devrait pas, vous pourriez penser que ce n'est pas un gros problème.

Mais si les pièces se chevauchent comme ceci, vous n'obtiendrez pas la pièce en dessous.

Et c'est très ennuyeux.

Vous ne voulez pas ennuyer vos joueurs maintenant, n'est-ce pas ? Pour corriger cela, nous allons réimplémenter la manière dont nous sélectionnons les pièces, je vais utiliser une stratégie différente pour cela.

Soyez patient avec moi pendant que j'implémente certaines choses qui peuvent sembler sans rapport.

Tout d'abord, faisons une fonction pour générer une couleur aléatoire, elle générera d'abord le composant rouge aléatoire entre zéro et 255.

Et nous en faisons un entier en utilisant floor.

Nous faisons de même pour les valeurs vertes et bleues et le retournons sous forme de chaîne en utilisant la syntaxe RGB comme ceci.

Maintenant, nous allons générer une couleur aléatoire pour chaque pièce.

Nous voulons vraiment que les couleurs soient uniques, et il est très peu probable que des doublons se produisent, surtout lorsque le jeu n'a que quelques pièces.

Mais un élément de mode insensé, mieux vaut prévenir que guérir et vérifier si une couleur a été utilisée auparavant et la régénérer dans ce cas.

Nous allons passer cette couleur à chaque pièce et maintenant dans la classe pièce, nous la stockons comme un attribut.

Ensuite, dans la méthode draw, nous allons spécifier un deuxième argument qui indique s'il faut utiliser la caméra ou non, par défaut défini sur true.

Si true, le code ici reste le même, mais si non, il dessinera les pièces en utilisant leur couleur à la place comme ceci.

J'utilise la méthode Fill rect ici et ajoute un padding de tab height pour que les onglets extérieurs soient également colorés.

Maintenant, testons en définissant use cam sur false, tout fonctionne toujours.

Mais maintenant les pièces sont plus colorées et l'entrée de la caméra n'est plus utilisée.

Vous pouvez en fait jouer au jeu comme ceci en vous basant uniquement sur la forme.

C'est assez facile en mode facile au moins.

Maintenant, nous avons fait ce changement parce que je veux utiliser la couleur de clic pour détecter si je clique sur une pièce ou non.

Comme ici, cela ne devrait pas détecter le clic car il n'y a rien là.

Et ici, cela devrait s'activer car j'appuie sur une couleur rose.

La pièce avec la couleur sur laquelle je clique devrait commencer à être traînée.

Nous implémentons cela en allant à la fonction de rappel onMouseDown.

Obtenir les informations de couleur de l'endroit où nous avons cliqué sur le canvas, nous obtenons les données de l'image à event.dot x et event.dot y est un tableau avec quatre éléments.

Le premier est pour le rouge, le deuxième pour le vert, le troisième pour le bleu.

Et le quatrième est la transparence, je vérifie si le quatrième élément est zéro, donc transparent, et je retourne dans ce cas, nous ne cliquons sur rien, puis ceci n'est pas blanc, en fait, c'est noir transparent.

Mais si nous passons cette partie, nous formatons la couleur au format de chaîne RGB, et vérifions pour voir où elle se trouve à l'intérieur de la pièce.

Nous devons implémenter une nouvelle fonction pour cela, mais c'est vraiment facile.

J'utiliserai cette autre fonction comme référence et passerai la couleur ici comme deuxième argument.

Maintenant, nous parcourons ces pièces comme avant.

Et si la couleur correspond, nous retournons cette pièce.

Simple comme cela.

Maintenant, si vous voulez rendre le code plus efficace, vous pourriez stocker les pièces dans un dictionnaire avec des clés égales aux valeurs de couleur, et ensuite faire cette recherche en temps constant au lieu de linéaire.

Mais cette méthode ici fonctionne très bien.

Nous n'avons pas tant de pièces même en mode insensé.

D'accord, rafraîchissons et testons.

Cela fonctionne.

Mais maintenant vous allez dire mais Rado.

Alors quoi si cela fonctionne, nous voulons voir l'image de la webcam ici et non des couleurs aléatoires.

Et à cela je dis plusieurs canvases.

Nous allons ajouter un autre canvas ici.

Je l'appellerai helper canvas.

Et maintenant en JavaScript, je vais y faire référence également de la même manière que nous l'avons fait pour l'autre.

Nous définissons ensuite sa largeur et sa hauteur pour qu'elles soient les mêmes également.

Maintenant dans Update game, je vais également effacer le helper canvas comme ceci, et ensuite dessiner les pièces normalement avec la caméra vers le bas du canvas principal, mais en utilisant les couleurs sur le helper canvas.

Et l'astuce est que maintenant sur le clic de la souris, nous ne prenons pas les données de couleur du canvas principal, nous les prenons du helper canvas à la place, laissez-moi simplement rafraîchir et vous comprendrez dans une seconde.

Ou quelques secondes.

Cela ne fonctionne pas.

J'ai oublié de changer l'ID ici en helper canvas.

D'accord, maintenant mes éléments ont montré le helper canvas quelque part ici en dessous.

Laissez-moi simplement le déplacer à l'écran comme ceci.

Je vais le rendre plus petit pour qu'il ne chevauche pas autant, et je vais le mettre dans le coin ici.

Maintenant, lorsque je clique quelque part sur le canvas principal, la valeur de couleur correspondante provient de ce helper canvas.

Alors la sélection de la pièce fonctionne maintenant comme prévu.

Et les deux canvases se mettent à jour en même temps, faisant du helper canvas un détecteur de clics fiable pour nos pièces.

Ce helper canvas n'a pas besoin d'être visible.

En fait, il n'a même pas besoin d'être ajouté au DOM.

Mais il peut être là aussi.

C'est utile pour le débogage, je pense que je vais simplement définir l'affichage ici en ligne à non et c'est tout.

Testons une dernière fois.

C'est tout, j'espère que cela en valait la peine et que vous avez appris quelque chose de cela.

Et si vous l'avez fait, s'il vous plaît, aimez et partagez cette vidéo avec quiconque vous pensez être intéressé.

Vous pouvez télécharger le code source depuis mon site web.

Il est divisé en parties pour que vous puissiez le prendre étape par étape si vous le souhaitez.

Aussi, faites-moi savoir si vous pouvez penser à une bonne stratégie pour jouer au jeu.

Il m'a fallu une heure et demie pour résoudre le mode insensé avec 1000 pièces.

Il doit y avoir une manière plus intelligente de faire cela.

Quoi qu'il en soit, merci d'avoir regardé et à bientôt.