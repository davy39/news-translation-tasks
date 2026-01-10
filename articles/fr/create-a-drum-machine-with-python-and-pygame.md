---
title: Créer une boîte à rythmes avec Python et Pygame
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-05-19T13:47:53.000Z'
originalURL: https://freecodecamp.org/news/create-a-drum-machine-with-python-and-pygame
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/drum.png
tags:
- name: Python
  slug: python
- name: youtube
  slug: youtube
seo_title: Créer une boîte à rythmes avec Python et Pygame
seo_desc: 'A drum machine is a fun project to create to practice your Python skills.

  We just published a full course on the freeCodeCamp.org YouTube channel that will
  teach you how to create a drum machine project using Python and Pygame.

  Pete LeMaster created ...'
---

Une boîte à rythmes est un projet amusant à créer pour pratiquer vos compétences en Python.

Nous venons de publier un cours complet sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à créer un projet de boîte à rythmes en utilisant Python et Pygame.

Pete LeMaster a créé ce cours. Pete a créé une série de tutoriels sur sa propre chaîne et a maintenant partagé ce cours avec la chaîne freeCodeCamp.

Tout d'abord, la vidéo présente le projet, puis elle passe à un tutoriel détaillé montrant comment ajouter une série de fonctionnalités ligne par ligne.

Ce cours est destiné aux débutants et aux développeurs expérimentés. Il couvre les concepts de Python et de programmation orientée objet, y compris les boucles for imbriquées, les fonctions, l'utilisation de fichiers audio pour générer du son, et la sauvegarde/lecture de données.

Voici les sections de ce cours :

* Présentation du projet
* Installation de l'application
* Dessin du tableau
* Activation et désactivation des notes
* Ajout d'un suivi de rythme mobile
* Ajout de sons et lecture !
* Ajout de la fonctionnalité Lecture/Pause
* Ajustement du nombre total de battements et de la vitesse
* Activation ou désactivation d'un instrument
* Contenu épique de la pause eau
* Dessin des boutons Sauvegarder et Charger
* Ajout de la fonctionnalité Effacer/Réinitialiser le tableau
* Dessin des menus Sauvegarder et Charger
* Sauvegarde des informations de rythme
* Chargement des rythmes sauvegardés
* Nettoyage et dépannage final

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/F3J3PZj0zi0) (3 heures de visionnage).

%[https://youtu.be/F3J3PZj0zi0]

## Transcription

(générée automatiquement)

Vous êtes sur le point d'apprendre à créer cette application de création de beats à partir de zéro en utilisant Python et Pygame.

C'est un excellent projet pour les débutants et les développeurs expérimentés.

Pete LeMaster a créé ce cours en premier, Pete va présenter le projet.

Et ensuite, il vous apprendra à coder le projet ligne par ligne, vérifiez la description pour un lien vers les ressources dont vous avez besoin, plus le code final.

Bonne chance avec ce projet.

Et n'hésitez pas à laisser un commentaire avec ce que vous apprenez dans ce tutoriel.

D'accord, je suis super excité de vous montrer ce projet.

C'est l'un des projets les plus cool que j'ai jamais construits.

Et je pense que vous pourriez vraiment apprécier construire quelque chose de similaire.

Donc, les principales caractéristiques de cette application incluent la capacité de créer et d'éditer rapidement de nouveaux beats ainsi que la capacité de modifier la vitesse à laquelle votre boucle se joue et le nombre total de beats dans ce motif.

Les boutons en bas vous donnent la capacité de mettre rapidement en pause ou de reprendre la lecture du beat ou d'effacer complètement le tableau lorsque vous êtes prêt à recommencer, vous pouvez éteindre des canaux entiers d'instruments afin de pouvoir éditer certaines parties de votre beat tout en gardant l'ensemble en lecture.

Ensuite, lorsque vous obtenez quelque chose que vous aimez vraiment, le menu Sauvegarder vous permet de l'enregistrer sous un nom de votre choix que vous pouvez recharger plus tard et revisiter certaines de vos créations préférées. Cet outil vous permet de créer des sons vraiment uniques et j'espère que vous apprécierez le projet.

Donc, suivez le tutoriel, prenez le code si vous voulez à partir du lien dans la description ci-dessous.

Laissez un commentaire pour me faire savoir quelles fonctionnalités supplémentaires vous aimeriez voir dans ce type de projet.

Ou ce que vous aimeriez voir sur la chaîne à l'avenir.

Si vous aimez la vidéo, n'oubliez pas de laisser un like sur la vidéo et de vous abonner à la chaîne pour beaucoup plus de contenu.

Maintenant, plongeons dans le tutoriel.

D'accord, je suis super excité de vous apporter ce tutoriel.

Mais il est long.

Alors, plongeons directement dedans.

Et je vais expliquer ce que nous faisons au fur et à mesure.

Donc, la première étape va être d'importer Pygame.

Si vous êtes familier avec le module PIP, alors vous pouvez utiliser PIP et faire pip install PI game.

Ou si vous avez un IDE, un bon comme pi charm, que j'utilise, alors vous pouvez généralement faire une instruction d'importation comme celle-ci.

Et tant qu'il reconnaît votre nom de module, il s'occupera de l'importation pour vous.

Et ensuite, je dirais que parce que cette application est fortement axée sur la musique, importer le mixer tout de suite.

Donc, Pygame dot mixer est une sorte d'outil associé à Pygame pour les effets sonores et la gestion de la musique.

Donc, nous allons simplement faire cela dès le début.

Et ensuite, nous allons faire pygame.in it pour l'initialiser, ce qui sera nécessaire pour les polices et l'utilisation de nombreuses fonctionnalités intégrées.

D'accord, donc c'est juste comment nous allons commencer.

Et ensuite, configurons notre écran.

Et puisque ce logiciel de création de beats, si vous y pensez, il est un peu comme vous voulez les mêmes dimensions que votre écran réel, donc plus large que haut, parce que nous anticipons les beats s'étendant sur l'écran.

Donc, j'utilise 1400 par 800.

Et j'aime bien ça, mais vous pouvez jouer avec cela stylistiquement si vous voulez.

Et j'ai défini quelques couleurs RVB tout de suite, parce que je sais que presque toutes les applications que je crée, je vais utiliser le noir, le blanc et une nuance de gris, peut-être 50 d'entre eux en cours de route.

Et donc je fais juste comme noir, blanc, gris.

Et ensuite, lorsque j'ajoute d'autres couleurs plus tard dans le projet, comme je vais sûrement utiliser un peu comme le rouge et peut-être un or dans ce projet.

Je les ajouterai ici.

Mais nous n'en avons pas besoin pour l'instant.

Donc, continuons.

Et ensuite, la chose suivante, nous allons nous concentrer sur la création de l'écran rapidement.

Donc, c'est Pygame dot display, dot set mode, set mode.

Et ensuite, entre crochets, faites simplement avec une virgule hauteur.

Nous y voilà.

Et vous pourriez taper ces nombres directement ici, vous n'avez pas besoin de les mettre dans une variable.

C'est une bien meilleure pratique.

Et si vous voulez le changer plus tard, c'est un peu plus facile à retrouver.

Une autre chose que j'aime faire techniquement, cela serait considéré comme une étape facultative.

Mais j'aime toujours définir la légende.

Et je l'appelle simplement beat maker.

Vous pouvez l'appeler autrement si vous voulez.

Et ensuite, je vais configurer une police ici, que j'appellerai label font parce qu'elle sera un peu plus grande.

Mais je crée toujours un texte dès le début parce qu'aussitôt que vous avez besoin de texte dans votre jeu, vous allez vraiment vouloir avoir cela initialisé déjà.

Sinon, vous allez simplement devoir revenir et faire cette étape plus tard.

Donc, je dis cela dans presque tous les projets, mais si vous ne voulez pas aller chercher un fichier ttf, presque tous les ordinateurs et installations de pi game vont venir avec celui que vous voyez ici, free sans bold, ce ttf.

C'est comme un intégré.

Donc, vous pouvez utiliser celui-ci, si vous voulez simplement suivre et que vous ne vous souciez pas trop du style, je suis allé chercher un gratuit sur internet, qui s'appelle simplement Roboto bold dot TTF.

Vous pouvez le voir ici dans ma structure de fichiers.

Donc, si vous voulez prendre une police pour votre projet et le personnaliser, déposez simplement ce fichier là et appelez-le comme ceci.

D'accord.

Et ensuite, la seule autre chose que vous devez lui donner ici est la taille de la police.

Donc, nous lui donnerons 32.

Et c'est, nous allons aussi faire FPS.

Donc, c'est notre fréquence d'images, et nous allons configurer un timer, qui va contrôler la vitesse de notre jeu, ce qui pour une application basée sur la musique est super important.

Donc, nous ferons timer égal à pi Game dot time dot clock, certaines personnes l'appelleront clock, certaines personnes l'appellent time, certaines personnes le feront directement dans la boucle de jeu.

Je n'aime pas faire cela.

Mais assurez-vous d'avoir quelque chose comme ceci.

Et allons-y et créons notre ce que j'appelle la boucle de jeu principale.

Donc, nous allons juste en dessous de ceci.

Et évidemment, il y aura beaucoup de choses qui se passeront entre notre bibliothèque de variables et notre boucle de jeu principale.

Mais juste pour commencer, nous allons faire ceci.

Donc, nous définirons cette variable run égale à true.

Et ensuite, nous allons configurer une boucle while qui est wall run.

Et les premières choses que vous faites toujours pendant run est timer dot TIG à votre fréquence d'images.

Donc, maintenant, cela dit tant que run est vrai, nous allons exécuter ce code 60 fois par seconde.

Donc, c'est le but de FPS.

Et puisque beaucoup de nos fonctionnalités vont se déplacer vers le beat suivant chaque seconde, chaque demi-seconde, peu importe.

Ce timer dot tick est super important pour cette application.

Donc, la fréquence d'images, vous voulez la garder à 60.

Si ce n'est pas le cas, si vous utilisez une fréquence d'images différente pour une raison quelconque, assurez-vous simplement que lorsque nous arrivons à la partie des mathématiques plus tard, où nous calculons combien de beats par minute, vous utilisez votre fréquence d'images dans ces mathématiques, d'accord, donc ensuite nous allons faire screen dot fill.

Et nous allons rendre le fond noir, je pense que cela a l'air assez bien.

Et allons-y et configurons ce que j'appelle toujours cette gestion d'événements, mais c'est essentiellement juste obtenir toutes les occurrences qui se produisent réellement sur votre ordinateur.

Donc, c'est pour event in PI Game dot event dot get.

Et cette petite application ici, chaque code que nous mettons, tout le code que nous mettons à l'intérieur de cette boucle for va vérifier toutes les touches du clavier, le mouvement de la souris, tout autre événement que l'ordinateur peut traiter sera à l'intérieur de for event in PI Game dot event dot get.

Et le premier que vous voulez configurer juste pour que votre jeu fonctionne est si event dot type est égal à et puis c'est pi Game dot quit juste comme ceci en majuscules.

Et si c'est le cas, alors nous voulons simplement que run soit égal à false.

Et c'est tout ce que nous allons faire pour l'instant.

Mais nous allons certainement mettre beaucoup de fonctionnalités là-dedans plus tard.

D'accord, et ensuite en dehors de ceci, nous voulons faire Pygame dot display display dot flip.

Et cela jette tout sur l'écran.

Et ensuite nous ferons ce dernier qui sera simplement Pygame dot quit comme cela.

Donc en dehors de tout autre code, juste au cas où il arriverait à ce point.

D'accord, donc reformater le format.

Donc maintenant nous devrions simplement obtenir la coquille de notre projet, et il s'est fermé immédiatement, parce que j'ai dit robot bold, et le fichier est Roboto bold.

Donc voilà.

D'accord, nous avons notre contour.

Et je pense que cela a l'air assez bien.

Mais allons-y.

Et maintenant, commençons à dessiner des choses sur le tableau.

Nous allons donc passer aux sons assez tôt dans ce projet.

Et je vais expliquer comment ceux-ci sont utilisés.

Parce que, évidemment, les sons sont super importants.

Mais d'abord, je vais configurer une fonction que je vais appeler draw grid, et elle va simplement dessiner toutes les choses statiques sur l'écran.

Donc je vais faire cela juste en dessous de mon screen dot fill, je vais l'appeler draw grid.

Et ensuite, nous allons venir entre, comme je l'ai dit, la bibliothèque de variables et la boucle de jeu principale.

Et je vais définir cette variable draw grid, et nous allons commencer à la construire ensemble.

Excusez-moi.

D'accord, donc commençons par draw grid et réfléchissons simplement à l'espace que nous allons avoir dans ce jeu.

Je vais commencer, je vais appeler la menu de gauche, left box.

Et c'est si vous avez déjà vu comme une disposition de beat, comme ce genre d'application.

C'est là que vous avez les instruments et parfois vous avez la possibilité de mettre des pistes en marche ou en pause ou d'ajuster le volume des instruments spécifiques.

Donc nous allons créer une sorte de menu de gauche que j'appellerai left box et nous allons le mettre sur l'écran, et nous allons le rendre gris.

Donc c'est pourquoi j'appelle cette couleur au début.

Et ensuite nous allons commencer dans le coin supérieur gauche.

Donc au tout début, il le rendra large de 200.

Et nous allons le rendre de la hauteur totale de l'écran.

Donc ce sont les quatre arguments, vous donnez des rectangles, x et y coordonnées de départ dans le coin supérieur gauche de votre boîte, et ensuite largeur, et ensuite hauteur.

Et ensuite après cela, ceux-ci sont maintenant facultatifs.

Donc cela vous donnerait juste assez ici, laissez-moi voir si je l'exécute, cela devrait fonctionner, nous obtenons cette boîte de gauche, qui a l'air bien.

Mais maintenant si nous ajoutons un argument de plus, nous allons dire à quel point nous voulons que les bords soient larges, ce qui va en faire un objet creux.

Donc il aura une largeur de cinq.

Et je pense que cela a l'air mieux comme un menu de gauche.

Préférence personnelle, vous pouvez le laisser totalement épais, si vous voulez.

Mais ensuite, ajoutons aussi un menu inférieur, que j'appellerai bottom box, et nous allons pi Game dot draw dot rec, c'est là que nous allons mettre comme nos contrôles de lecteur, comme démarrer et arrêter la boucle du jeu.

Donc comme play pause, je suppose que je dis game, vous comprenez que c'est une app.

Mais nous allons mettre comme play pause, et aussi comme save et load.

Donc les options pour sauvegarder votre B ou charger un beat précédemment sauvegardé, ou ajuster la vitesse, ou combien de beats il y a dans votre app au total, nous les mettrons dans cette boîte inférieure.

Donc nous allons l'appeler screen, gray.

Et ensuite pour ce rectangle, mettons-le en bas.

Et en fait, faisons-le juste 200 de haut.

Donc hauteur, moins 200.

Donc ce sera la position de départ.

Et ensuite nous le ferons pour la largeur totale de l'écran et 200 de haut.

Et faisons-le creux avec cinq aussi.

Et ce que vous verrez si je fais cela, maintenant nous allons avoir ce rectangle un peu étrange, peut-être que vous aimez ce look, peut-être que non, je vais prendre ma boîte de gauche, et je décide de l'arrêter à 200 de haut aussi.

Donc maintenant nous n'aurons pas ce chevauchement en croix en bas.

Je pense que cela a l'air assez bien.

Donc nous allons continuer.

La prochaine chose que je veux faire est de commencer à créer le beat.

Donc nous allons le faire de sorte qu'il soit ajustable, combien de cases il y a ici.

Mais juste pour commencer, nous allons simplement le configurer pour que nous puissions obtenir quelque chose à l'écran.

Donc ce que je vais dire, c'est que je vais créer une petite variable vide ici que j'appellerai boxes, comme ça.

Et je vais créer une petite bibliothèque de couleurs.

Donc colors est égal à gray, white, gray.

Et certaines de ces choses, nous ne les toucherons pas pendant un moment.

Donc si vous ne voulez pas suivre ligne par ligne, je suppose que vous pouvez sauter cela pour l'instant.

Mais nous allons y revenir.

Désolé, gray, white, gray.

Donc nous allons faire ceux-ci.

Mais maintenant, ce que nous voulons faire, c'est penser à une batterie, les trois instruments les plus importants sont la charleston, la caisse claire et la grosse caisse.

Donc ce que je vais commencer à faire, c'est créer de l'espace pour ceux-ci.

Donc la première chose que je vais faire, c'est l'appeler hi hat.

txt.

Et maintenant nous appelons cette label font que nous avons.

Et c'est label font dot font, ou désolé, label font dot render, nous l'avons déjà défini comme une police, et ensuite vous lui donnez le texte et pour le hi hat, nous allons simplement dire hi hat, cela devrait avoir du sens.

Et ensuite le deuxième est comme anti alias en tant que booléen.

C'est toujours vrai dans mon expérience, je ne sais pas réellement.

Je ne connais pas un scénario où ce ne serait pas le cas.

Et ensuite, lorsque nous aurons la possibilité d'activer ou de désactiver un canal.

Donc vous configurez un beat et vous voulez désactiver le hi hat, nous en ferons une variable.

Donc nous reviendrons à cela.

Mais pour l'instant, je vais simplement le mettre en blanc pour ne pas compliquer les premières étapes.

Et nous allons le dessiner sur l'écran.

Donc screen dot blit.

Et vous lui donnez le texte que vous voulez.

Donc nous voulons que le texte hi hat soit dessiné sur l'écran.

Et cela a besoin d'une coordonnée X et Y.

Et je vais le déplacer un peu vers le bas et un peu vers la droite à partir du coin supérieur, même si c'est notre premier.

Et donc cela devrait être tout ce que nous avons à faire pour voir le texte hi hat.

Donc je pense que cela a l'air assez bien.

Et maintenant, allons-y et faisons, prenons simplement ces mêmes éléments, C Ctrl V, et faisons snare et kick.

Donc, hi hat txt.

Nous allons faire snare Tex, ensuite, snare et snare text.

Et ensuite, ce que nous allons faire, c'est le déplacer vers le bas de 100, donc je crois que nous avons fait le jeu à 800 de haut, le menu inférieur est à 200 de haut et nous allons mettre un total de six instruments ici.

Donc nous allons faire un hi hat, une caisse claire, une grosse caisse, une cymbale crash et ensuite nous allons faire comme un floor time et nous allons faire une claque.

Ce sont les six beats les plus basiques.

Si vous voulez, vous pouvez prendre votre propre soundboard.

Et nous allons en parler un peu plus tard.

Et faire les sons que vous voulez, vous pouvez faire autant d'instruments que vous voulez.

Je vous donne un peu l'épine dorsale de la façon de le configurer, cependant.

Donc ce sera snare et hi hat.

Allons-y et faisons les deux prochains, que nous appellerons kick, parce que c'est une grosse caisse, mais vous pouvez l'appeler basse si vous voulez.

Et quoi de mal, nous allons dire basse drum sur le texte, c'est probablement ce que les gens connaissent le plus.

Et nous allons dire kick text.

D'accord.

Et faisons après kick, faisons la cymbale crash, et crash, et crash text.

Et nous les déplaçons de 100 pour chacun d'eux.

Donc 200 300.

Et nous allons en avoir deux de plus.

Donc nous avons la grosse caisse et le crash.

Et ensuite, nous allons vouloir faire le clap.

Et le floor tom.

Donc clap.

Et floor tom.

D'accord.

Et donc nous irons à 334 3530.

Maintenant, dessinons cela et voyons.

D'accord, cela a l'air assez bien.

Je pense que ce qui aurait du sens, c'est de mettre des lignes entre eux pour les délimiter.

Alors pourquoi ne pas les dessiner aussi, après ce texte, nous allons simplement faire pour i dans range.

Et je pense que nous voulons six parce qu'il y a six instruments.

Donc pour i dans range six.

Et nous allons faire ce Pygame dot draw dot line screen, nous allons le faire gris.

Donc il se fond avec les bords.

Et nous allons le commencer à zéro.

Et ensuite pour la hauteur, nous allons vouloir qu'il soit i fois 100.

Donc i fois 100.

Mais puisque nous ne voulons pas que le premier soit tout en haut, parce que la boîte commence déjà tout en haut, et pour les boucles for, elle va commencer à zéro, et cela va aller à cinq, c'est juste un peu comment les boucles for et Python fonctionnent.

Ils ne sont pas inclusifs de bord pour le nombre six, donc il va faire 012345.

Mais nous voulons que ces lignes soient dessinées à 100 200 300 400 500.

Et je suppose que nous n'avons pas techniquement besoin de 600, mais cela ne devrait pas affecter quoi que ce soit.

Donc la position de départ sera, je vais faire zéro, et i fois 100 plus 100, je pense que ce serait un peu mieux.

Ou vous pourriez simplement ajouter un à range, je suppose que cela n'a pas d'importance.

D'accord, et ensuite la position de fin, nous allons vouloir qu'elle aille.

Voyons, à 200.

Oui, c'est la largeur que nous avons faite pour ce menu.

Et ensuite nous voulons la même coordonnée y, donc c'est une ligne verticale.

Copions cela.

Et mettons cela ici.

D'accord.

Et puisque les bords du menu sont cinq, faisons ces lignes cinq aussi.

Et voyons si cela nous donne des lignes entre tous nos instruments.

J'ai fait quelque chose de stupide, je ne sais pas pourquoi j'ai ce crochet carré ici, vous n'avez pas besoin d'un crochet carré si vous dessinez une ligne.

Donc les arguments de la ligne sont l'écran, la couleur, la position de départ en tant que tuple de coordonnées X et Y, et la position de fin en tant que tuple de coordonnées.

Et ensuite l'épaisseur de la ligne.

Et voyons si cinq est un peu trop épais.

C'est bon, voyons si cela a l'air mieux en trois peut-être puisque ceux-ci ne sont pas les bords extérieurs de notre menu, peut-être que cela aurait l'air mieux.

Oui, j'aime trois de plus.

Vous pouvez faire ce que vous voulez, si vous voulez plus épais, faites-le plus épais.

Mais c'est bon pour moi pour l'instant.

Et maintenant, je pense que nous voulons commencer à considérer comment ce jeu va fonctionner, comment cette application va fonctionner en termes de beats.

Donc nous allons avoir une variable qui sera définie dès le début beats.

Et nous allons simplement la rendre égale à huit.

C'est une configuration de base très simple que nous pourrions faire.

Mais nous devons utiliser beats dans cette application, pour vérifier combien de cases nous devons dessiner pour chaque instrument.

Donc pour cela, nous faisons for i in range, et ensuite beats.

Et créons une variable que j'appellerai instruments.

Et nous l'utiliserons quelques fois tout au long pour vérifier combien de lignes il y a.

Donc je suppose que vous pourriez appeler cette variable rows si vous voulez.

Je vais dire instruments parce qu'il y a six sons différents que nous avons ici.

Et je vais aussi, au lieu de frire range six, je vais dire for i in range instruments.

Mais la raison pour laquelle je fais cela est que nous créons une grille de base pour ion range beats.

Et ensuite pour J in range.

Et c'est instruments.

Et donc c'est une autre façon, espérons-le, si vous avez l'intérêt de créer ce jeu, donc le ou l'application, peu importe, je dirai probablement jeu tout au long de ceci parce que le module s'appelle PI game et je fais tellement de jeux.

Mais donc si vous voulez ajouter plus d'instruments, nous le créons maintenant pour que tout ce que vous aurez vraiment à faire est d'ajuster l'épaisseur de chaque instrument.

Donc vous pourriez le faire de sorte qu'il soit une fonction de cet espace vertical de 600 que nous avons, vous pourriez me donner 50 au lieu de 100, et ensuite avoir 12 instruments totalement à vous.

Mais nous créons des boucles for imbriquées ici.

Donc pour Iron Range beats, et ensuite pour J in range instruments, ce que nous allons faire est de dire que, nous allons dessiner ce rectangle égal à pi Game dot draw dot rect.

Et nous allons le mettre sur l'écran.

Et pour l'instant, je vais simplement les rendre gris aussi.

Et nous allons faire, voyons, nous voulons faire l'épaisseur de ceux-ci.

J'essaie de réfléchir ici, je ne veux pas me tromper, nous voulons que l'épaisseur soit, nous voulons que la position de départ soit AI.

Donc ce sera notre b, ce qui va être pour le x la position de départ sera Ai fois, et ensuite nous voudrons la largeur totale que nous avons disponible pour les beats, qui est la largeur de l'écran moins 200.

Donc nous avons cette largeur de l'écran, moins 200, mettez-la à l'intérieur des parenthèses comme ceci, et ensuite nous allons utiliser quelque chose appelé division par le plancher.

Et nous allons diviser par le plancher par les beats.

Donc cette division par le plancher s'assure simplement qu'il s'agit d'un entier, car pour la position des pixels x&y, je suppose que ce n'est pas exactement la position des pixels, mais cela doit être un entier.

Donc, par exemple, cela serait maintenant 1200 divisé par huit, parce que c'est le nombre de beats que nous avons.

Cela va le commencer à 1200 divisé par huit, ce qui est comme 150.

Mais si pour une raison quelconque, c'était comme une division inégale, cela s'assurerait qu'il reste un entier.

D'accord.

Et ensuite, nous allons vouloir le déplacer un peu vers la droite, initialement.

Donc comme toujours, comme je l'ai dit, avec les boucles for, cela va commencer avec zéro, mais nous ne voulons pas qu'il commence à zéro, donc nous allons ajouter les premiers 200.

Et ensuite, je suppose que c'est un rectangle de cinq d'épaisseur, donc nous allons ajouter les premiers 205.

Et c'est juste notre position de départ x.

Donc ce rectangle va nécessiter quelques mathématiques, alors soyez patient avec moi.

Pour la position de départ whi, c'est un peu plus facile parce que nous n'avons pas de menu supérieur, donc ce sera j fois 100.

Et ici, il est en fait correct, cela commence à zéro, nous allons simplement faire plus cinq, parce que nous allons lui donner une largeur de cinq en tant que bordure, excusez-moi.

Donc en fait, nous n'avons pas besoin de bordure en haut, cela peut être juste contre le haut, et celui-ci sera également correct, juste contre ce menu.

Donc nous allons faire juste plus 200, et ensuite j fois 100.

Et ensuite pour le rectangle réel, nous allons dire, excusez-moi, pour la largeur réelle, nous allons vouloir qu'elle soit à nouveau avec moins 200.

Et cela peut être vraiment important pour la rendre ajustable afin qu'elle fonctionne pour n'importe quel nombre de beats, car une grande fonction de notre application sera qu'elle est ajustable à cet égard.

Donc encore une fois, faites simplement la largeur moins 200 divisée par le plancher des beats, cela vous donnera toujours la largeur possible la plus grande, mais rendra chaque case égale.

Et ensuite pour la hauteur.

Puisque nous avons six instruments, nous pourrions le faire de cette manière.

Nous pourrions faire la hauteur divisée par les instruments divisée par les instruments, mais ce n'est pas exactement la hauteur divisée par mes instruments parce que nous avons une largeur de 200, une hauteur de 200, un menu inférieur, donc ce serait la hauteur moins 200 divisée par les instruments.

Et vous devriez vraiment faire de cela une division par le plancher également.

Mais parce que cela fait 800, et nous savons que 800 moins 200 fait 600.

Et nous avons six instruments, cela revient effectivement à la même chose que de mettre un 100 ici.

Donc si vous voulez simplement faire une hauteur de 100.

Allez-y et faites cela.

Si vous comprenez ce qui se passe et que vous voulez faire ces mathématiques, parce que vous voulez être évolutif encore une fois, alors faites cela par tous les moyens.

D'accord, donc voyons ce que nous devons faire ici.

Parce que ce format ne semble pas tout à fait correct.

Je pense que je dois simplement fermer les parenthèses.

Et je vais zoomer un peu ici parce que cette ligne est longue.

Donc laissez-moi simplement copier cela dans une nouvelle ligne.

Nous y voilà.

Et faisons de cela une largeur de cinq et un rectangle arrondi.

Ces déclarations semblent bien.

Voyons pourquoi nous obtenons des erreurs ici.

J'ai probablement fait quelque chose de stupide sur le formatage.

Oh, j'ai trop de crochets fermants.

D'accord, je ne deviens pas fou.

Désolé pour un peu de dépannage.

C'est juste parfois que vous mettez une parenthèse de trop.

Donc vérifions rapidement pour ces rectangles parce que nous faisons quelques mathématiques avancées ici.

Mais une fois qu'il est configuré correctement, il va immédiatement être évolutif pour toute l'application.

Donc nous le commençons au beat.

Donc s'il y a huit beats, il va commencer à 200.

Et il va calculer combien de place il a sur l'écran.

Et il va se mettre à jour automatiquement pour prendre autant d'espace que possible.

Et ensuite, il fera la même chose en fonction du nombre d'instruments et nous allons en faire un rectangle arrondi, ce qui est ce que le deuxième cinq est pour.

Et nous allons le faire cinq d'épaisseur, donc il devrait être un rectangle creux.

Maintenant, voyons, parce que nous devrions obtenir huit beats, les doigts croisés, ce n'est pas mal, nous obtenons, nous obtenons huit beats par instrument, et ils remplissent tout l'écran.

Et cela a l'air assez bien.

Donc vous pouvez voir que nous obtenons une forme rudimentaire de cela, ce qui je pense a l'air assez bien.

Donc voyons, nous reviendrons et nous améliorerons ce style plus tard, je pense que ce qui va être important est que nous commençons à examiner comment rendre cela fonctionnel, car cela va être vraiment satisfaisant, si nous pouvons commencer à implémenter cela un peu plus tôt que plus tard.

Donc ce que je pense que nous voulons faire, parce que vous vous souvenez au début de cela, j'ai créé cette liste vide pour les cases.

Eh bien, au fur et à mesure que nous passons et créons toutes ces rectangles, ce que nous voulons faire est d'ajouter quelques informations à cette liste que j'ai faite appelée cases, parce que nous devons ramener ces informations de notre fonction, afin que nous puissions vérifier si ces choses sont cliquées.

Donc ce que nous allons faire est que chaque fois que nous appelons draw grid, nous allons vider la variable cases ici, nous allons la rendre vide.

Et ensuite nous allons dessiner tous ces rectangles sur l'écran.

Et ensuite nous allons retourner quelques informations dans cette liste.

Donc ce que je veux que ce soit, vous pouvez en quelque sorte le considérer comme un tuple.

Où à l'intérieur du tuple, l'un des deux arguments est un autre tuple.

Donc si cela est trop confus pour vous, pensez-y de cette manière, nous retournons quelques choses, nous retournons le rectangle de chaque beat, mais ensuite nous retournons également une coordonnée X et Y pour celui-ci.

Donc nous retournons ce qu'est b, qui est l'œil et ensuite nous retournons également quelle ligne il est, qui est le JE et ensuite nous retournons réellement le rectangle complet.

Et la raison pour laquelle nous faisons cela est que nous allons utiliser cela pour la détection de collision pour voir s'il a été cliqué.

Et ensuite ce que nous ferons ensuite est que nous retournerons simplement cette variable cases dont nous venons de parler.

Donc lorsque nous avons appelé Draw grid.

Laissez-moi reformater cela juste pour qu'il aime combien d'espaces.

Donc lorsque nous appelons draw grid ici, nous devons obtenir les cases de celui-ci.

Donc revenons à notre boucle de jeu.

Et où nous obtenons les cases est juste ici.

D'accord.

Et ce que nous devons faire est d'utiliser cette liste de cases pour vérifier et voir si nous avons cliqué sur l'une des cases.

Donc ce n'est pas trop mal, nous devons simplement ajouter une nouvelle détection de collision.

Donc ce que nous faisons est que nous descendons dans cet if event dot type equals pi Game dot quit.

Et nous faisons if event dot type equals, et ensuite celui-ci va être pi Game dot mouse button down, qui est ce qui se passe si vous cliquez sur le bouton et ne l'avez pas encore relâché, donc il y a mouse button up et mouse button down dans Pygame.

Et c'est ce que nous allons commencer.

Et nous allons créer une boucle qui va itérer à travers toute la liste.

Donc nous allons dire for i in range, et ensuite la longueur des cases.

Et la raison pour laquelle nous le faisons à la longueur des cases est que la liste, ce qui signifie également qu'en fait, au tout début, c'est une chose importante, chaque fois que vous créez une variable.

Même si c'est une variable que vous obtenez d'une fonction, si vous allez l'utiliser dans votre boucle principale, vous devez l'initialiser quelque part, ou elle va dire qu'elle a été référencée avant d'exister.

Donc pour i in range, et ensuite la longueur des cases, et la raison pour cela est que chaque fois que nous mettons à jour le beat total, le total des beats, qu'il passe de huit à 12, à 16 à 20, peu importe, cette liste va devenir significativement plus longue ou plus courte.

Et donc cela doit être évolutif pour vérifier cela.

Donc pour i in range longueur des cases, si les cases et voici où nous devons être très prudents quant à la manière dont nous adressons chaque élément.

Donc les cases, et je vais donc dire que nous passons en revue la liste des cases que nous avons définie, et nous vérifions chaque case à i qui va appeler le tuple complet, donc le rectangle et ensuite les coordonnées et ensuite nous vérifions zéro.

Donc cela fait référence au rectangle que nous avons stocké là.

Et c'est.

Donc la raison pour laquelle nous avons fait cela est que maintenant nous pouvons utiliser la fonction collide rect intégrée de PI games, qui est cet outil intégré super utile, qui vérifie si une coordonnée X et Y, qui dans ce cas sera la souris.

Et il vérifie pour voir si elle est entrée en collision avec un rectangle.

Donc dans ce cas, si collide rect avec event dot pause, donc event dot pause est la position à laquelle la souris était lorsque le mouse button down s'est produit.

Donc la position de notre souris lorsque nous cliquons, et si elle entre en collision avec, donc cela vérifie déjà ici si nous avons cliqué sur l'un des rectangles que nous venons de définir, donc nous créons une fonction vraiment puissante.

Et nous allons dire coords est égal à cases à i, et ensuite un.

Et la raison pour laquelle je fais cela est que c'est un peu plus facile que de référencer les coordonnées x&y comme cases, un, zéro, et ensuite cases un, un comme cela, cela va simplement me donner cette variable temporaire appelée coords, que nous allons utiliser juste en dessous pour suivre si quelque chose a été activement cliqué ou non.

D'accord, donc allons-y et faisons cela ce que nous allons faire.

Et voici où nous allons devoir créer une nouvelle liste.

Parce que nous allons prendre clicked at coords.

Et je suppose, en fait, nous devons être prudents à ce sujet, nous mettons le i et ensuite J, et J est la ligne dans laquelle il se trouve.

Donc en fait, nous allons vouloir coords un, et ensuite chords zéro.

Et je pense que j'ai manqué une case.

Nous y voilà.

D'accord, et nous allons vouloir définir cela égal à l'opposé de ce qu'il était.

Donc allons-y et créons la liste clicked.

Et la raison pour laquelle je dis liste est que c'est ce qui va garder une trace de quelles variables ont été de quels bits ont été sélectionnés ou non.

Donc au tout début, je vais créer cette liste.

Et nous allons le faire de telle sorte que nous définissons ce qui est essentiellement une liste complète de moins un.

Donc je choisis de faire moins un signifie qu'il n'est pas actuellement actif, et un signifie qu'il est actuellement actif.

Je pense que c'est la manière la plus facile de le faire.

Et je pense que vous verrez pourquoi dans juste une seconde.

Donc faisons-le de cette manière, disons clicked.

Et c'est notre liste de quels beats sont sélectionnés et lesquels ne le sont pas.

Et nous allons dire clicked pour underscore in parce que lorsque vous le faites ici, vous n'avez pas vraiment besoin d'une variable comme AI ou quelque chose à référencer.

Donc nous allons simplement faire pour underscore in range beats.

Donc cela va créer initialement une liste de cette taille, et donc pour underscore et range beats, et ensuite elle va être pour underscore in range instruments.

D'accord, donc cela va créer une liste dès que le jeu démarre, parce que beats est initialement huit et instruments est six, il y aura huit moins un dans une liste, et ensuite il y aura une liste de six lignes de huit moins un.

Donc cela crée ce tableau très utile, essentiellement une liste de listes, qui va initialement être tout moins un.

Et la raison pour laquelle je fais cela est que lorsque vous cliquez sur une case, nous pouvons la définir égale à moins un d'elle-même, donc nous allons la multiplier par moins un.

Donc si c'est un, il deviendra moins un, mais si c'est un moins un, il deviendra un.

Et la raison pour laquelle nous allons le faire est que nous pouvons utiliser cette liste pour dessiner tout l'écran actif, toutes les rectangles actifs.

Donc s'ils sont un, cela signifie qu'ils ont été sélectionnés, et ils seront verts.

Donc c'est une manière très polyvalente de le configurer.

Mais cela signifie que nous devons passer la liste clicked dans notre draw grid.

Donc nous allons simplement venir ici, draw a grid, et nous allons passer la liste clicked, ce qui est bien.

Ce n'est pas comme si c'était une gêne.

Et ce que nous allons faire, c'est que nous allons venir et nous allons dire, maintenant rappelez-vous, j'ai dit que nous allons vérifier chacun de ces rectangles, et nous allons ajuster la couleur en fonction de leur état actif ou non.

Donc je vais ajouter quelques couleurs ici.

Je vais dire que green est égal à R, G, B, Z.

C'est juste tous les verts 0255 zéros.

Et en fait, cela sera bien pour l'instant, car nous allons simplement le faire, s'il est actif, alors nous allons le faire dessiner en vert.

D'accord.

Et nous devons nous assurer que nous recevons l'argument clicked.

Et parfois à l'intérieur de votre fonction, ce n'est pas une mauvaise idée d'utiliser un nom de variable différent, comme je sais que j'ai utilisé boxes, mais parce que nous le réinitialisons complètement chaque fois, ce n'est pas vraiment un problème.

Mais nous ne remplaçons pas clicked dans la fonction draw, nous l'utilisons simplement.

Donc ce que nous allons faire ici, c'est que nous allons descendre et dire, doop, doop doop boxes est égal à colors.

D'accord, donc faisons ceci pour i dans range, beats.

Et ensuite pour J et range instruments, ajoutons quelque chose ici, qui va dire, si clicks à, et cela va être encore une fois, j, puis I, parce que le premier élément va être la ligne dans laquelle il se trouve, et ensuite AI va être la colonne dans laquelle il se trouve.

Et nous allons dire, si c'est égal à moins un, alors nous allons avoir notre couleur que nous utilisons actuellement être gris, parce qu'il n'est pas actif.

Mais ensuite, ce que nous allons dire, c'est else et vous pourriez dire l f.

Et vous pourriez vérifier si clicks est égal à moins un.

Mais ensuite, nous allons dire else color sera égal à green.

D'accord.

Et maintenant, je vais garder celui-ci parce que ce rectangle est essentiellement le contour du rectangle.

Et il n'y a aucune raison de toucher à cela exactement.

Autre que je veux simplement mettre quelques éléments stylistiques ici.

Donc nous n'avons pas besoin de celui-ci.

Eh bien, faisons celui-ci coloré, le rectangle que nous avons réellement référencé, donc nous allons laisser celui-ci tranquille ici.

Mais ensuite, ce que nous allons faire, c'est que nous allons dire, d'accord, sur l'écran, à notre couleur, et ensuite nous voulons que celui-ci soit solide.

Donc si vous voulez qu'il soit un rectangle arrondi, ce que je pense aurait l'air bien, mais vous voulez qu'il soit solide, alors faites simplement cet argument à zéro, et cela le rendra solide.

D'accord.

Maintenant, voyons ce que nous pouvons faire d'autre.

Puisque nous sommes ici, je pense que peut-être j'aime l'idée de faire comme un or, juste pour améliorer notre style un peu.

Donc puisque nous sommes ici, et que nous venons de faire un vert, je vais aussi faire un or et j'ai tiré ce RVB à l'avance à 12 175 55 à 12 175 55.

Si vous avez une couleur en tête que vous aimeriez utiliser, il suffit de rechercher la valeur RVB, puis le nom de votre couleur, et vous pourrez sélectionner tout sur internet.

Trouver des RVB n'est pas difficile.

D'accord, donc maintenant, allons-y et déplaçons essentiellement ce rectangle que nous venons de faire, qui est d'une couleur spécifique, déplaçons celui-ci à l'intérieur des paramètres de ce rectangle extérieur.

Donc voici où nous allons les déplacer, nous allons déplacer celui-ci de cinq vers le bas, et de cinq vers l'intérieur, et ensuite nous allons faire cette largeur, je pense moins 10.

Donc nous le mettons essentiellement à l'intérieur du cadre que nous avons construit avant.

Et nous allons le faire cette hauteur moins 10, aussi, puisque nous le mettons à l'intérieur d'un cadre de 10 par 10.

D'accord, et nous allons laisser celui-ci, peut-être noir.

Et nous allons mettre ce cadre doré à l'intérieur.

Donc je fais un effet à trois niveaux.

Et c'est purement pour le style.

Donc désolé, si vous n'avez pas aimé ce détour, mais je pense que cela ajoute vraiment à l'apparence du projet.

Et ce que nous allons faire, c'est que nous allons faire ce cadre doré, un cadre complet de cinq par cinq, et ensuite nous allons mettre un fil noir à l'intérieur.

Donc allons-y et chargeons cela avant d'en faire trop et de perdre de vue le projet.

Mais ce que vous voyez, c'est que aucun de ceux-ci n'a été cliqué.

Et donc ce que j'ai actuellement, c'est un bord doré de cinq avec un bord noir plus petit de seulement deux d'épaisseur autour de chacun d'eux, mais cela donne une profondeur vraiment cool.

Je pense.

Maintenant, essayons de cliquer.

D'accord, nous avons une erreur.

L'objet doit être un événement de style rect.

Je suis tout à fait d'accord.

Jetons un coup d'œil à ce que nous faisons ici.

Donc nous passons le rectangle Pygame dot draw dot rect Yep, cela devrait être correct.

Et ensuite nous retournons les cases à faire quatre cases dot append.

Cela a l'air bien.

Oh, erreur stupide parce que j'ai utilisé collide rect dans cette position mais il a besoin d'être collide point parce que ce que nous vérifions est si le rectangle à cases est zéro est en collision avec notre clic de souris qui est juste un point donc cela doit être collide point pas collide rekt.

Chargeons-le et essayons d'en cliquer quelques-uns maintenant.

D'accord, donc nous avons le hi hat en vert, ce qui est assez génial.

Et je peux en sélectionner plusieurs.

Et maintenant puis-je le désactiver ? Oui, je peux.

Voyons si je peux les sélectionner un peu partout.

Oui, donc c'est parfait.

C'est la fonctionnalité que nous voulons.

Et maintenant vous êtes probablement conscient que nous n'avons pas encore de mouvements à travers le tableau pour jouer les notes.

Si nous les avons sélectionnées, et je promets que nous nous rapprochons de l'avoir du son, ce qui est vraiment la partie amusante, d'accord.

Mais ce que nous devons faire, c'est que nous devons faire quelques mathématiques pour calculer essentiellement combien de temps chaque beat doit durer.

Et donc ce que je vais faire, c'est que je vais descendre ici, et je vais créer une variable.

Et je vais l'appeler beat length.

Et ce qui va être égal à, et c'est là que j'ai mentionné tout au début, si vous utilisez un taux de rafraîchissement différent, alors cela doit être ajusté un peu plus oops, bpm.

Donc nous n'avons pas encore créé de variable appelée BPM, mais cela va être une autre partie de ce jeu.

Donc nous allons dire que les beats par minute vont être 240, initialement, ce qui fait quatre beats par seconde, ce qui est assez rapide.

Mais c'est ce que nous allons utiliser dès le début.

Et donc cela signifie que la longueur de chaque beat individuel tel que notre jeu le voit va être 3600 divisé par BPM, si vous devez y penser de cette façon, vous pouvez y penser comme votre fréquence d'images par seconde fois 60, parce que dans chaque minute, il y a 60 secondes, n'est-ce pas ? Et ensuite, si vous utilisez une fréquence d'images de 60, c'est 60 fois 60, ce qui est 3600.

Et ensuite nous faisons une division par le plancher pour nous assurer que nous obtenons un entier de combien de beats par minute nous voulons.

Donc c'est combien de clics par minute, essentiellement, combien de boucles par minute, cette boucle while est en cours d'exécution.

Et donc chaque beat individuel va être ce nombre divisé par combien de beats par minute ils sont censés être.

Et donc ce que nous allons faire, c'est que nous allons dire, si playing, nous allons le faire de cette manière.

Donc nous allons créer une variable.

Et pour l'instant, nous allons toujours jouer.

Donc dès le début, nous allons définir playing égal à true, mais plus tard lorsque nous mettrons en place la fonctionnalité pause, et ce sera bien d'avoir une variable qui contrôle si nous jouons ou non.

Et donc nous allons dire si playing, alors ce que nous allons faire, c'est que nous allons créer une nouvelle variable, si active length, donc combien de temps le beat sur lequel nous sommes actuellement a été actif.

Et donc dès que le jeu démarre, nous allons initier initialiser celui-ci comme un zéro.

Et donc active length est égal à zéro dès que nous commençons, donc si playing while playing, si active length est inférieur à beat length, alors nous voulons simplement ajouter un à active length.

Donc nous avons cette variable active length, où nous suivons quel beat nous sommes actuellement.

Et nous allons simplement ajouter un à chaque fois que nous ne sommes pas à beat length.

Mais ensuite, ce que nous allons dire, c'est else.

Et donc cela signifie que le beat vient d'atteindre la durée qu'il doit avoir.

Donc juste pour des mathématiques faciles, si nous disions que nous voulions 60 beats par minute, une fois par seconde, nous devrions passer au beat suivant.

Donc nous allons dire else, et ensuite cela rendrait active length égal à zéro.

Et maintenant, nous devons vérifier si nous sommes à la toute fin d'un cycle, et nous devons revenir à zéro ou si nous pouvons continuer.

Donc ce que nous allons faire, c'est que nous allons créer une autre variable, et nous allons l'appeler active beat.

Et nous allons dire si active beat est inférieur à total beats moins un, donc cela signifie que nous ne sommes pas encore à la toute fin, alors nous allons ajouter un à active beat.

Et cela m'a donné oops, active beat, pas active length.

Et cela m'a donné un soulignement rouge parce que nous n'avons pas initialisé celui-ci non plus.

Donc dès le début, nous allons appeler active beat un.

Et vous ne voulez vraiment pas commencer avec zéro parce que même si dans la programmation de code, vous commencez presque toujours avec zéro, pour un beat, cela n'a pas vraiment de sens d'être à zéro à un moment donné, vous êtes toujours sur le beat 12341234.

D'accord, donc active beat, nous allons ajouter un à celui-ci.

Et ensuite, nous allons utiliser cette variable qui est juste une variable de changement, be changed.

Et nous allons la définir égale à true.

Et nous allons utiliser cela dans juste une seconde pour jouer réellement les notes sur ce beat.

Donc else, alors nous allons simplement ajouter, puis, whoops.

Else signifiant else contre cette instruction if si active b est inférieur ou égal à beats moins un.

Et donc nous allons dire else couvrant tout scénario, ce qui signifie que nous ne sommes pas à la fin de notre boucle.

Donc cela dit que nous sommes allés trop loin.

Définissez Active beat égal à zéro, mais beat changed va toujours être égal à true.

D'accord, et donc, allons-y et je pense que cela devrait être tout ce que nous devons faire pour le faire bouger.

Allons-y et même beat, changed equals true dès le début.

Parce que techniquement, dès que l'application se charge, vous voudriez que cela soit activé.

Et maintenant, nous devons faire quelque chose avec cette variable active beat, nous voulons réellement dessiner quelque chose sur l'écran montrant sur quel beat nous sommes.

D'accord, donc ce que nous allons faire maintenant, c'est que nous allons simplement dire que nous voulons passer en quoi beat nous sommes.

Donc nous utilisons déjà.

Voyons, oui, nous utilisons la variable Click de l'extérieur.

Donc nous allons simplement descendre à clicked.

Et nous allons dessiner active beat aussi.

D'accord, et je veux utiliser une nouvelle couleur pour celui-ci, afin qu'il se distingue.

Et je vais créer une sorte de bleu vibrant, pas exactement néon, je vais simplement l'appeler bleu, parce que ce sera la seule chose dans mon application, je vais faire du bleu.

Mais pour obtenir cette couleur que je fais, c'est assez comme un bleu turquoise ou un aqua, ce sera beaucoup de G et B.

Donc c'est comme un bleu néon, mais je vais simplement l'appeler bleu.

En tout cas, nous entrons dans notre fonction draw grid.

Et sous tout le reste que nous dessinons, dessinons cette nouvelle chose que je vais simplement appeler active, et cela n'a pas vraiment d'importance, c'est juste pour que je sache ce que je dessine, parce qu'à la fin de cette application, il y aura beaucoup de code partout.

Donc c'est juste pour moi, je vais le mettre sur l'écran, nous allons le faire bleu.

Et ensuite, nous devons commencer à réfléchir à ce rectangle.

Donc c'est essentiellement un rectangle mobile qui vous montre sur quel beat vous êtes.

Et, pour faire cela, nous allons utiliser la variable beat que nous passons fois, et ensuite avec divisée par 200 moins 200.

Désolé, ce bit devrait vous être familier maintenant.

Divisé par les beats.

Donc nous parlons de l'endroit où nous voulons commencer que la variable beat est 12345678.

Donc si vous y pensez, quand c'est un, nous voulons commencer à 200.

Donc ce sera une fois cela.

Et ensuite plus 200.

Donc nous devons le déplacer plus 200.

Et donc cela signifie, en fait, cela pourrait être 200.

Trop loin pour regarder avec mon stockage.

Nous verrons quand nous le chargerons.

Parce qu'il pourrait être conçu pour commencer à partir de zéro.

Je me demande si ce serait une meilleure façon de le faire.

Je ne m'inquiète pas pour l'instant.

C'est quelque chose que nous pouvons ajuster plus tard.

D'accord.

Et ensuite, voyons, la position de départ de why, commençons-la tout en haut de l'écran et ensuite allons tout en bas des instruments.

Donc alors pourquoi voulons-nous que ce soit bien, celui-ci est facile.

C'est juste avec moins 200, et ensuite divisé par le plancher des beats.

Donc cela dit simplement que nous voulons que ce rectangle soit exactement d'un beat de large.

Et ensuite nous allons le faire aussi haut que les instruments fois 100.

Donc il y a 600 Hi, c'est essentiellement un rectangle, qui va entourer tout le beat actif.

Et ce sont les quatre arguments dont le rectangle a besoin, sauf que j'ai mis le crochet au mauvais endroit.

Nous y voilà.

Et ensuite, faisons de cela, nous ne voulons certainement pas que ce soit un rectangle solide.

Faisons-en un rectangle arrondi avec une bordure de cinq et un rayon de coin de trois.

Et voyons si nous avons correctement un beat qui se déplace à travers l'écran.

Donc je pense que c'est assez génial.

Cela commence au bon endroit, cela va jusqu'à la fin et ensuite revient immédiatement au début.

Actuellement, cela ne fait rien avec différents sons, mais c'est l'étape suivante.

Donc allons-y et enfin, la chose que vous attendez tous.

Enfin, implémentons quelques sons.

D'accord.

Et pour cela, je vais dire que j'ai un dossier préparé appelé sounds.

Et j'ai ces six fichiers wav ici.

J'ai aussi un autre dossier là avec quelques fichiers wav supplémentaires dont je parlerai plus tard.

Je voulais juste montrer comment vous pouvez passer d'un kit à l'autre.

Mais nous y viendrons beaucoup plus tard pour l'instant.

Pour faire ce que je fais, vous aurez besoin d'obtenir six fichiers wav des sons.

J'utilise le téléchargement gratuit en ligne dont je mettrai un lien, j'espère qu'ils sont mis en miroir dans la vidéo ici.

Si ce n'est pas le cas, je m'assurerai qu'il y a un lien vers le site web dans les commentaires ci-dessous.

Et j'espère que j'en ai parlé dans l'introduction de cette vidéo aussi.

tons de kits de sons gratuits là-bas, donc vous pouvez en télécharger un qui fonctionne pour vous juste pour pouvoir suivre cela ou honnêtement vous pouvez faire les bruits avec votre bouche et les enregistrer, mais vous voudrez utiliser des fichiers wav, les mp3 ont quelques problèmes avec le mixer et ils ne fonctionnent pas aussi bien dans mon expérience, d'accord, donc assurez-vous d'avoir ce dossier sounds et clap, un crash, un hi hat, un kick, un snare et un Tom, si vous voulez suivre directement, et je vais simplement faire cette petite zone que tout dire charger dans les sons.

D'accord.

Maintenant, nous allons commencer par le hi hat.

Et nous allons le définir égal à mixer.

Donc rappelez-vous que nous avons appelé Pygame dot mixer dès le début, nous l'avons importé.

Maintenant nous allons l'utiliser et pour cela nous définissons ce mixer dot sound.

Et ensuite tout ce que nous avons à faire est de lui donner le fichier dans lequel il se trouve.

Donc sounds et ensuite backslash.

Et je l'appelle simplement hi hat dot wav.

D'accord, donc comme ceci, et nous allons copier cela.

Et nous allons en faire six ici.

Donc nous allons dire hi hat, et ensuite snare, snare.

Et ensuite nous allons l'appeler kick, et ensuite nous allons l'appeler crash, in then clap.

Et ensuite Tom.

D'accord.

Et ensuite dans les emplacements des sons, nous allons faire snare, hi hat do kick, assurez-vous que vos noms correspondent exactement à ce que les fichiers réels disent ici.

Je recommande toujours, s'ils ne téléchargent pas quelque chose de assez logique, envisagez de les renommer en quelque chose qui est un peu plus facile, un peu plus logique.

D'accord, mais comme ceci, et si vous avez un TTY, ou un caractère spécial qui ressemble à un caractère d'échappement, comme un backslash, N pour une raison quelconque, assurez-vous de faire ce double backslash, car c'est essentiellement ce que vous devez faire pour obtenir un backslash interprété comme un littéral dans votre chaîne.

Vous n'avez pas à vous soucier trop de cela.

Mais si vous obtenez quelque chose de bizarre, où il pense qu'il s'agit d'un caractère d'échappement, faites simplement ces doubles backslashes.

Et cela devrait fonctionner pour vous.

D'accord, donc maintenant nous allons descendre là où nous avons fait draw grid.

Et nous allons mettre quelque chose qui va utiliser cette fonctionnalité beat changed.

Et donc chaque fois que le beat change, nous voulons jouer les notes.

Donc avez-vous fait pour iron reigns, je veux juste m'assurer que je le mets dans un bon endroit.

screens for Iron Range instruments, draw a line down in here, boxes, draw the grid.

D'accord.

Donc ce que nous voulons faire, c'est dire si beat changed.

Et ensuite, donc si le beat a changé, nous allons appeler cette fonction play notes.

Et cela va simplement jouer les sons que nous venons de créer en fonction du changement de beat.

Et immédiatement, nous allons définir beat changed égal à false.

Donc c'est comment, même si ce code, le code extérieur, cette boucle while s'exécute 60 fois chaque seconde, cette boucle ne s'exécute qu'une fois par fois que le beat change.

Et c'est ainsi que nous contrôlons le nombre total de fois que le beat, que les sons sont joués.

Donc c'est ça.

Maintenant, allons dans, allons au-dessus de draw grid.

Et définissons la fonction play notes puisque les sons sont juste ici.

Donc nous allons dire définir play notes.

Et celle-ci est assez facile.

C'est juste pour i dans range, et ensuite la longueur de notre liste clicked.

Si clicked à i, et ensuite le active beat, donc c'est tout ce que nous devons vérifier si clicked à i, ce qui va vérifier chaque ligne.

Donc chaque instrument dans notre liste clicked à l'active beat.

Si elle est sélectionnée comme un, alors nous allons simplement vérifier à quoi i est égal, et ensuite jouer un son différent en fonction de cela.

Donc si elle est égale à zéro, nous voulons ce son que nous avons créé.

Faites simplement hi hat dot play comme cela.

C'est tout ce que vous devez faire.

Et ensuite nous allons faire Ctrl C Ctrl V.

Et même si celui-ci est un peu, vous savez, monotone, je dirais que ce n'est pas trop mal.

Et probablement en dehors de mettre ces sons dans une liste.

Et ensuite en faisant référence à un élément spécifique comme l'index de la liste.

Il n'y a probablement pas de moyen plus rapide de faire cela.

Autre que de simplement passer et de s'assurer que vous avez le bon ordre pour vos trucs.

Crash et ensuite clap.

Et ensuite Tom.

En fait, je ne suis pas sûr que ce soit ainsi que nous l'avons dessiné, c'est hi hat snare kick, crash clap et ensuite Tom, je pense, d'accord, c'est oui, si i est égal à cinq, alors nous allons faire Tom dot play.

Et cela, ce que nous venons de configurer super vite, super facile, est tout ce que vous devez faire pour obtenir les sons qui jouent ou cela devrait être.

D'accord.

Donc allons-y et chargeons simplement cela et voyons si nous pouvons obtenir quelques sons.

J'essaierai ce hi hat.

D'accord.

Et j'espère vraiment avoir laissé le son allumé lors de l'enregistrement de l'ordinateur ici.

Donc, espérons que vous pouvez entendre ce hi hat.

Si vous suivez, espérons que vous obtenez cela maintenant, jouons-le.

D'accord.

Peut-être que c'est juste moi.

Mais je pense que le fait que nous soyons ici déjà est super cool.

Et vous pouvez activer des trucs, vous pouvez désactiver des trucs.

Et essayez de jouer avec vos différents sons, une fois que vous arrivez à ce point.

D'accord, c'est si addictif, je pourrais rester là pour toujours.

Une fois que vous arrivez à ce point, c'est un bon moment pour vérifier que les sons que vous avez importés sont réellement les sons que vous espérez obtenir, car vous pouvez changer ces sons plus tard, bien sûr.

Mais c'est un peu votre première façon de savoir si vous avez des sons avec lesquels vous allez être heureux à l'avenir.

D'accord, donc il y a une chose que je voudrais faire sur le mixer.

Et c'est parce que le défaut de votre mixer, le défaut de cela, lorsque vous le chargez à partir de Pygame, c'est qu'il a un total de ce qu'on appelle huit canaux sur lesquels il peut jouer.

Donc huit sons techniques au total qui pourraient être en cours.

Mais certains de ces fichiers wav comme la cymbale crash, prennent en fait quelques boucles pour se terminer.

Donc en théorie, vous pourriez rencontrer ce problème où vous manquez de sons, et donc il doit choisir quel son il doit vous laisser jouer parce que son défaut est de n'avoir que huit.

La façon de contourner cela est super facile.

Vous faites simplement pi Game dot mixer dot set, num channels.

Et ensuite, je pense que la règle générale est que le nombre d'instruments, si vous leur donnez trois canaux chacun, il ne devrait y avoir aucun problème ici, quelle que soit la rapidité avec laquelle vous commencez à jouer.

Sauf si vous êtes à 600 beats par minute, alors peut-être que vous devez renforcer cela.

Mais la raison pour laquelle huit est le défaut est que, en général, si vous avez un jeu vidéo en cours et que vous avez plus de huit effets sonores à la fois, c'est juste le chaos.

Mais comme pour un soundboard, tant que vous choisissez des sons qui sonnent bien ensemble, avoir beaucoup plus de canaux est acceptable, donc vous pourriez faire des instruments fois quatre, si vous le voulez vraiment, des instruments fois trois a bien fonctionné pour moi dans le passé.

Donc nous allons opter pour cela.

D'accord.

Donc c'est assez cool.

Je pense que nous sommes un peu au point où nous devons commencer à ajouter une fonctionnalité de joueur à cela.

Donc comme, faisons play pause, parce que cela devrait être facile.

Et ensuite nous allons commencer à le faire de sorte que vous puissiez ajouter plus de beats, et vous pouvez ajouter plus de beats par minute, ou soustraire des beats par minute.

Et ensuite nous allons ajouter la fonctionnalité de pouvoir activer ou désactiver un canal spécifique.

Et ensuite nous allons commencer à examiner la capacité de sauvegarder et de charger des fichiers, ce qui est beaucoup que nous avons devant nous.

Donc continuons simplement.

Si vous appréciez cette vidéo, je pense que vous l'avez déjà regardée jusqu'au bout.

Laissez-moi simplement dire s'il vous plaît laissez un like sur la vidéo, abonnez-vous à la chaîne, cela signifierait beaucoup pour moi, j'espère que vous avez apprécié le contenu, j'essaie de sortir du contenu de haute qualité comme celui-ci tout le temps.

Et le soutien signifie beaucoup.

Si vous avez des questions sur ce que vous voyez ou si vous voulez voir quelque chose de spécifique à l'avenir, n'oubliez pas de laisser un commentaire pour me le faire savoir.

Sans plus tarder, continuons.

D'accord, donc faisons un bouton play pause.

Et nous allons simplement descendre en dessous de draw grid.

Et nous allons simplement ajouter un rectangle que nous allons dessiner ici.

Je pense que c'est plus facile que de le dessiner sur le, je pense que c'est plus facile que de le dessiner dans la grille.

Mais si vous n'êtes pas d'accord avec moi, ce n'est pas grave.

Dessinez-le où vous voulez.

Donc je vais dire lower menu buttons.

Et je vais créer une petite section dans mon code pour cela maintenant.

Et je vais simplement appeler ce bouton, le bouton play pause.

Et je vais dire Pygame dot draw dot rect.

Je vais le mettre sur l'écran et je vais le rendre gris.

Parce qu'il est sur un fond noir.

Donc le gris aura l'air assez bien.

Je vais le déplacer de 50 vers la gauche.

Et ensuite je vais le monter de 150 à partir du bas.

Donc il est toujours bien dans ce menu.

Et ils le feront 200 de large et 100 de haut.

Et cela devrait être un bon objet en forme de bouton.

Nous allons le rendre solide.

Et je vais en faire un rectangle arrondi, ce qui est assez normal pour les boutons.

Et je vais simplement oui, faisons un peu de texte pour faire savoir à tout le monde.

Donc je vais dire play text et nous allons le définir égal à la police label dot render.

Et nous allons simplement dire play slash pause et nous allons le rendre vrai.

Et nous allons rendre le texte blanc, et nous allons le mettre sur l'écran.

Donc screen dot blit, play text, et ensuite nous allons le mettre à l'intérieur de ce bouton par un peu.

Donc 70 et ensuite height moins 130.

Donc il devrait être assez proche du centre du bouton.

Et maintenant, ajoutons une petite vérification pour savoir si nous jouons ou non.

Donc si nous jouons, alors nous aurons play text to ici.

Donc faisons une nouvelle police, je l'appellerai medium font, parce que ce n'est pas exactement petit.

Mais nous avons ce bouton, qui va dire play slash pause dessus.

J'aimerais dire en dessous, si nous sommes en pause ou en lecture.

Donc je ne veux pas que ce soit petit, je veux que ce soit super facile à lire, mais ce ne devrait pas être la caractéristique du bouton.

Donc je vais simplement le faire à 24.

Nous verrons comment cela se présente.

Et peut-être que nous jouerons avec plus tard.

D'accord, mais oui, donc nous allons dire, d'accord, playing text est égal à medium font dot render.

Et ensuite, il va dire playing si nous jouons, playing true.

Et nous allons faire celui-ci, je suis toujours dans la chaîne, anti alias true.

Et obtenons une nouvelle nuance de gris.

Dans notre bibliothèque de couleurs en haut.

Et en général, plus votre gris est proche du noir, plus il s'assombrit.

Donc nous avons ce gris régulier, je vais dire dark gray, et il va être juste 50 5050.

Donc le noir est 000.

Ce gris clair normal que nous avons est 128 128 128.

Donc plus les nombres sur votre gris sont bas, plus ils sont proches du noir, plus les nombres sont élevés, plus ils sont clairs, juste un petit détail sur le gris pour vous.

D'accord, donc nous allons dire que play text est égal à playing si nous sommes actifs, et nous allons dire qu'il est égal à, donc nous n'avons pas besoin de if playing, c'est juste else maintenant.

Sinon, il sera égal à paused déjà.

Et voyons, mettons-le sur l'écran.

Et mettons-le en dessous.

Donc nous allons prendre cet écran en haut blit Ctrl, C.

Et juste là, et mettons-le à height moins un, trois, mettons 30 pixels plus bas sur l'écran.

Donc height moins 100.

Maintenant, il sera à 100 pixels du bas de l'écran.

Et il dira playing ou paused.

Mais pour l'instant, nous ne gérons pas vraiment si c'est cliqué ou non.

Donc découvrons cela ici, nous voulons faire à l'intérieur de notre code de clic de bouton de souris, ajoutons une deuxième section pour le clic vers le haut.

Donc en général, si vous voulez que quelque chose ne se produise qu'une seule fois, alors il est généralement préférable de faire Pygame dot mouse button up.

Parce que si vous maintenez le bouton enfoncé, alors il pourrait techniquement le faire plusieurs fois.

Et vous ne voulez vraiment pas vous embêter avec cela.

Donc nous allons aller à if event dot type equals pi Game dot mouse button up.

Et nous allons dire si play pause dot, et je ne vais pas me tromper cette fois collide point.

Nous y voilà.

collide point avec event dot pause, et playing.

Donc la raison pour laquelle nous avons besoin du and playing est que si c'est si c'est playing, alors nous devons définir playing égal à false.

Et en fait, ce qui est probablement une meilleure façon de faire cela est plutôt qu'un playing ici, il fera si playing dans ici, playing equals false.

Et ensuite nous allons dire L if not playing.

Et la raison pour laquelle vous ne voulez pas simplement faire else ici est que si c'était playing, vous viendriez et ensuite ce serait not playing et ensuite nous dirions else et ensuite il verrait que ce n'est pas playing et le définirait immédiatement égal à playing.

Donc vous devez faire un L F si vous le faites de cette manière.

L F playing equals true.

Et cela devrait le faire.

Donc nous avons déjà le vérificateur de type de beat actif qui arrête si nous jouons.

Donc voyons si notre bouton pause fonctionne.

Oh, mon garçon.

play pause.

Je ne pense pas avoir mis à jour le texte.

D'accord, attendez une seconde play text medium font dot random.

Juste ici.

C'est play text to, pas juste play text.

Nous y voilà.

D'accord, cela a l'air génial.

Nous avons playing ici.

Je le mets en pause, vous pouvez voir notre rectangle bleu s'arrête et ensuite il continue.

Je pense que c'est génial.

D'accord, donc voyons si je le mets en pause et je configure un beat.

Et je fais juste un beat rock générique qui se terminera par un crash.

posit, et ajoutons quelques floor times parce que c'est cool.

D'accord, génial.

Donc c'est, c'est génial.

Je pense que c'est un bon début, je pense que peut-être la prochaine chose que nous devrions faire est de le faire de sorte que vous puissiez ajouter plus de beats, plus de beats et plus de bpm.

Donc c'est un peu compliqué, mais soyez patient avec moi parce que je pense que nous avons créé une épine dorsale vraiment utile pour ce projet où en fait tout va s'adapter vraiment bien, nous devons simplement l'implémenter.

Et nous devons être prudents quant à obtenir tous les détails, corrects.

D'accord, donc allons-y ensuite.

Et je pense que nous allons ajouter le BPM.

Donc nous avons les boutons du menu inférieur, nous sommes dans cette section.

Nous sommes toujours dans cette section, pour sûr, les boutons du menu inférieur.

Et nous allons faire le BPM ici.

Et je trouve que cela aide à le séparer un peu avec ces commentaires.

Et donc la première chose que nous allons faire est de faire un rectangle BPM Pygame dot draw dot rect.

Et nous allons le mettre sur l'écran rect en espérant sur l'écran, nous allons le faire gris.

Et nous allons utiliser plus ou moins la même taille de rectangle.

Donc pour celui-ci, nous allons le faire 300 pour l'éloigner de 50 pixels du dernier, mais il sera toujours à height moins 150, nous allons toujours le faire 200 de large, et nous allons toujours le faire 100 de haut.

Et nous allons toujours le faire solide.

Non, vous savez quoi, parce que celui-ci n'est pas un bouton.

Faisons celui-ci creux.

Celui-ci affiche simplement combien de beats par minute, et ensuite les beats par minute, les boutons d'ajout et de soustraction seront à droite.

Donc faisons celui-ci creux.

Et ensuite ajoutons du texte, nous appellerons BPM text.

Et ce sera la police label maintenant.

Maintenant, il vaut mieux ne pas faire label font, car c'est beaucoup de texte en fait.

Donc medium font dot render, et ensuite nous allons épeler beats per per minute, nous y voilà.

D'accord, et mettons-le sur l'écran, inch true white, et ensuite mettons-le sur l'écran screen dot blit.

Et celui-ci, nous ne voulons pas le déplacer trop, car beats per minute est assez long.

Donc nous allons faire 308 juste pour l'intégrer un peu.

Mais nous allons toujours faire le height moins 130, comme ça.

Et ensuite, ce que nous allons faire, c'est que nous allons faire un deuxième texte qui va en fait montrer BPM text to, et ce sera la police label, car cela peut être grand, cela va montrer les beats par minute réels.

Donc pas seulement le texte qui vous dit ce que c'est.

Donc cela sera label font dot render.

Et ensuite, vous pourriez en faire une chaîne formatée si vous le vouliez.

Si pour une raison quelconque vous voulez ajouter autre chose que la variable beats par minute.

Je vais le faire de cette manière juste pour montrer que cela pourrait être fait.

Donc en théorie, vous pourriez dire comme, BPM, deux-points et ensuite BPM si vous voulez, mais je vais mettre cela en dessous du texte beats per minute.

Et encore une fois, vrai, et nous allons le faire blanc.

Et mettons cela sur l'écran screen dot blitt, le pm text to et mettons-le juste en dessous.

Donc ce qui aurait le plus de sens, probablement 373 70.

Et ensuite, je dirais que height moins 100.

Peut-être où nous avons mis la dernière deuxième ligne de texte.

Vérifions cela.

Donc beats per minutes 240, je suis un peu surpris parce que je pensais que j'essayais un rectangle là.

BPM RX vert gris 300 Oh, j'ai fait height moins 1500.

Nous voulons height moins 150.

Oui, cela a l'air un peu mieux.

D'accord, donc c'est cool, mais nous ne pouvons pas encore le faire, donc nous sommes capables de le faire, ajoutons deux rectangles de plus.

Et cela peut ne pas sembler la manière la plus facile de le faire.

Mais je pense que c'est une manière assez logique de le faire parce qu'en général, vous n'ajustez pas les beats par minute un par un.

Si vous voulez, par tous les moyens faites ces plus et moins un, je vais les faire plus et moins cinq parce que la plupart du temps vous voyez la vitesse des beats par minute ajustée par incréments de 10 ou occasionnellement cinq.

C'est vraiment bizarre de voir une chanson qui est à 137 beats par minute.

C'est beaucoup plus normal d'avoir 120 à 40.

Donc je vais simplement le faire en plus et moins cinq mais vous n'avez pas à.

Conduire une moto dans la rue effrayé.

D'accord, BPM add rec donc ce sera le rectangle qui vous permettra de faire plus cinq et nous allons dire Pygame dot draw dot rect, nous allons le mettre sur l'écran rect en espérant sur l'écran, nous allons le faire gris.

Et cette fois, allons un peu à droite.

Donc ce dernier rectangle que nous avons fait commence à 300.

Et à 500, celui-ci donnera simplement un rembourrage de 10.

Et ensuite nous le mettrons à height moins 150.

Donc la hauteur du haut du rectangle, et nous allons simplement faire celui-ci 148 48, presque 5050, de sorte que ces deux rectangles rempliront presque la hauteur totale.

Mais pas tout à fait, je pense que tout a l'air un peu mieux avec un peu de rembourrage autour.

Et ensuite nous allons dire BPM, sub rect.

Donc ce sera le bouton qui nous permettra de soustraire cinq de vos beats par minute, il fera Pygame dot rect, le mettra sur l'écran, le rendra gris.

Maintenant, celui-ci, toujours à 510, nous voulons qu'il soit à la même hauteur, ou nous voulons qu'il soit à la même exposition, mais ensuite nous allons simplement faire height moins 100.

Et maintenant, puisque ils sont 4848, nous avons un peu de rembourrage, ce qui sera bien, comme vous le verrez lorsque nous le chargerons.

Et je veux vraiment insister sur le style, vous pouvez faire ce que vous voulez avec le vôtre.

Donc si vous n'aimez pas la façon dont le mien a l'air, ou vous pensez qu'il aurait l'air mieux d'une autre manière, ajustez-le, changez la taille des polices, changez votre police, changez vos couleurs, faites ce que vous voulez, je vous donne simplement la fonctionnalité.

D'accord, donc ensuite, ce que nous allons faire, c'est que nous allons créer un texte d'ajout.

Et ce sera assez bien, car nous pouvons l'utiliser sur les boutons de beats par minute.

Et je suppose en théorie, nous allons vouloir faire juste plus et moins un pour les beats.

txt.

Donc oubliez ce que j'allais dire.

D'accord, add text est medium font, dot render, parce que ce sont des boutons plus petits, donc nous ne pouvons pas nous permettre de les faire énormes.

Et nous allons faire plus cinq pour add text, vrai et blanc.

Et ensuite sub text sub text Nice.

C'est la chose, medium font dot render.

Et ensuite dans la variable de chaîne moins cinq, vrai et blanc.

Et ensuite faisons screen dot blit pour add a text, et mettons cela un peu à l'intérieur.

Donc 520, parce que le bouton commence à 510, et ensuite height, moins 140.

Donc un peu vers le bas.

Donc nous lui donnons une sorte de crochet de 10 en haut et à gauche, et nous verrons comment cela se présente.

Cela fera à peu près la même chose pour le sub text.

Donc 520 et ensuite height moins 9090.

Nous y voilà.

D'accord, et nous n'avons pas eu de fonctionnalité.

Donc rien ne se passe si vous cliquez dessus pour l'instant, mais voyons si cela a l'air bien.

Oui.

D'accord, donc la prochaine chose que nous allons faire est de faire en sorte que lorsque vous cliquez sur ce bouton, il ajuste réellement votre BPM par plus ou moins cinq.

Et ce n'est pas difficile à faire.

Donc nous allons descendre dans notre code de bouton de souris où nous vérifions si le si le bouton play pause est Wow, c'était difficile pour moi de le sortir.

Si le bouton play pause est pressé, et nous allons faire si add BPM, add rect dot collide point, collide point, event dot pause, be Pm plus égal cinq, et ensuite nous allons faire un L if BPM sub rect dot collide point, event dot pause, be Pm moins égal cinq.

Et en fait, nous pouvons rendre notre code légèrement plus optimisé en faisant de tout cela des LFS parce qu'en théorie, nous savons que ces boutons ne sont pas au même endroit.

Donc nous pouvons économiser un peu de temps à notre code, en ne nous embêtant pas à vérifier si vous cliquez sur ces autres boutons si vous avez déjà cliqué sur ce bouton dans cette boucle, parce que vous ne ferez pas les deux.

Et c'est super simple.

Cela devrait être tout ce que nous avons à faire.

Donc allons-y et vérifions cela.

Voyons.

Je vais mettre un peu de son ici.

un tas au déjeuner, et voyons si nous pouvons le rendre plus rapide Oui, cela m'a donné de l'anxiété.

D'accord, mais espérons que si vous suivez, c'est vraiment cool.

Cela devrait être super encourageant.

Vous venez de faire cela.

Vous êtes un roi de la programmation.

Bon travail, continuez comme ça.

Peut-être que je me parle simplement, mais je pense que vous l'appréciez aussi.

D'accord, donc la prochaine chose que nous devons faire est d'ajouter des beats et cela va être un peu plus compliqué car nous devons évidemment mettre à jour notre clicked et mettre à jour notre grille totale.

Donc nous avons quelques listes qui doivent être mises à jour si nous changeons le nombre de beats dans la chanson, mais nous pouvons commencer essentiellement avec le BPM que nous venons de faire.

Donc nous allons dire beats stuff.

Donc, vous savez, oui, il y a un peu plus de programmation que nous devons faire en arrière-plan, mais au moins pour obtenir les rectangles dessinés, cela ne va pas être trop mal du tout.

Donc nous avons beats rekt beats, txt, beats.

txt, beats txt to même parce que c'est vraiment, c'est une seconde.

C'est une deuxième version du BPM, quelque chose que vous devriez avoir le contrôle, nous voulons qu'ils puissent ajouter et soustraire.

Donc nous allons dire add text to sub text to add text to sub text to et nous allons faire un beat à la fois.

Parce que techniquement, vous pourriez avoir n'importe quelle, vous pourriez avoir n'importe quelle signature de temps, vous pourriez faire neuf beats au total, si vous le voulez vraiment.

Donc nous allons dire beats in loop.

Et cette fois, nous sommes à, notre limite droite, je suppose, est 560.

N'est-ce pas ? Donc cela aurait-il le plus de sens de commencer cela à 600 ? Probablement.

Donc nous allons faire 600.

Et ensuite tout le reste, je pense que c'est bien, cela sera 608 670.

Et ensuite, cela devrait probablement maintenant être 810 810 828 20.

Et nous n'avons rien ajouté pour le code opérationnel.

Donc rien ne se passe lorsque nous cliquons sur ces boutons.

Mais cela a l'air bien.

Déplaçons le texte vers la droite.

Parce que cela n'est pas aussi long, donc beats in loop peut être comme 618.

Et cela peut être comme six ad, je pense que cela aura l'air bien.

Oui, cela a l'air mieux.

D'accord, continuons.

La fonctionnalité réelle dont nous avons besoin lorsque nous cliquons sur ces boutons est un peu plus compliquée.

Donc examinons ce que nous devons faire lorsque nous entrons en collision avec les points.

D'accord, donc nous allons descendre à ces deux beats BPM, add rect et soustraire.

Et nous devons faire un L F beats add rect collide point et LF beats.

Et initialement, nous pouvons plus ou moins utiliser le même code parce que nous allons prendre la variable beats qui existait déjà, et nous allons ajouter un et soustraire un.

Mais ce n'est pas assez là.

Parce que nous devons, nous devons ajouter une ligne complète, une ligne vide complète à notre grille.

Si c'était, assurez-vous que je dis bien, une ligne vide complète à notre grille.

Si nous ajoutons un B, et nous devons supprimer la dernière ligne de notre grille si nous soustrayons un B, donc ce que nous devons faire est de dire pour i dans la plage de longueur de clay clicked length have clicked, nous y voilà, nous devons supprimer un poids, c'est le plus un.

Donc je vais voler cela.

Nous y voilà.

Et donc cela signifie que nous avons simplement pressé beats moins un.

Et ce que nous devons faire, c'est que nous devons dire pour i dans la plage de longueur have clicked clicked at I donc cela passe par chaque ligne de notre liste clicked.

Et nous allons clicked I dot pop, qui est la fonction de liste Python pour la suppression.

Et nous allons pop le moins un qui signifie le dernier caractère à la fin, donc c'est ainsi que vous pouvez adresser cela, c'est l'index à l'intérieur de cette liste.

Et si vous faites un négatif, il compte à rebours à partir de la fin de votre liste.

Donc pop moins un, cela va passer et supprimer le dernier élément dans notre liste pour la liste Clicked.

Et ensuite pour les beats plus un, nous passons et faisons essentiellement la même chose do to do donc en fait, j'étais sur la bonne voie déjà.

Sauf qu'au lieu de pop moins un, c'est en fait assez amusant, c'est append et c'est toujours un moins un parce que moins un signifie non sélectionné.

Donc c'est maintenant tout, donc je pense que cela va faire, voyons, les doigts croisés.

Donc nous avons cliqué sur plus un et maintenant nous avons neuf à l'écran, c'est cool et tout l'écran se met à jour chaque fois que nous en ajoutons un, donc maintenant nous pouvons passer à 12 beats, je vais le mettre en pause pendant que je configure cela, donc basse caisse claire basse basse caisse claire, basse caisse claire crash.

Oui et cela, je veux dire que vous pouvez déjà jouer avec si vous voulez, mais cela peut continuer, vous pouvez faire cette chose 48 juste ici.

Vous remarquerez qu'il est un peu fastidieux de remplir 48 beats, mais nous l'avons configuré de manière très intelligente afin que cela soit complètement ajustable en fonction du nombre de beats que vous voulez dans votre boucle.

Donc je veux dire, super travail les gars.

Nous sommes juste en train de bien avancer ici.

Ajoutons quelques fonctionnalités supplémentaires.

Parce que cela se passe vraiment bien, ajoutons la possibilité de désactiver un canal afin de pouvoir l'éditer sans qu'il n'affecte votre boucle en direct et de l'activer et de le désactiver comme cela.

Pour ce faire, nous allons venir et nous allons créer quelques rectangles d'instruments.

Donc essentiellement, ils sont juste, allons-y en dessous de la section beats.

Et nous allons dire, instrument racks.

Et je fais cela simplement pour que nous puissions cliquer sur les canaux.

Et je vais dire, instrument, racks, égaux, et ensuite une liste vide.

Et ensuite pour i dans la plage des instruments, et j'essaie de faire en sorte que si vous copiez ce code, et ensuite plus tard, vous voulez ajouter quelques canaux supplémentaires, j'essaie de le rendre aussi évolutif que possible automatiquement.

Donc nous allons faire ce petit rect égal à pi Game dot rect dot rect.

Et vous remarquerez ce que je fais maintenant, c'est que je définis un rectangle, mais je ne le dessine pas sur l'écran parce que nous n'en avons pas besoin sur l'écran.

Et pour celui-ci, c'est un peu différent, nous définissons simplement un rectangle.

Et donc celui-ci a besoin de deux tuples au lieu d'une liste de quatre caractéristiques.

Il a besoin d'une position de départ x&y, et donc la position de départ x&y sera toujours zéro, et ensuite i fois 100.

Donc simplement au fur et à mesure que nous passons dans la liste, cela descend de 100 à la fois, mais cela reste tout à fait à gauche.

Et ensuite la largeur pour tous ceux-ci était de 200.

Et ils font tous 100 de haut.

Et ensuite nous allons faire instrument racks, dot append.

Et ce rectangle, d'accord, donc ce que nous faisons est que chaque boucle nous passons, et nous créons cette liste de rectangles pour ces boutons.

Mais nous faisons cela afin de pouvoir descendre dans notre détection de collision à l'intérieur de notre clic de bouton de souris.

Et nous pouvons vérifier si un rectangle d'instrument a été cliqué super facilement.

Pour ce faire, nous allons dire L à L f, nous allons dire pour i dans la plage, longueur des rectangles d'instruments, d'accord.

Donc cela va vérifier chaque rectangle d'instrument que nous définissons.

Et ce que nous allons dire, c'est si, à droite, si instrument rats, désolé, j'ai essayé de donner à mes noms de variables des noms longs et descriptifs, afin que lorsque vous suivez, il soit assez clair ce que tout est.

Mais ceux-ci sont peut-être plus longs que vous ne le souhaiteriez dans un projet optimal.

Mais donc nous allons vérifier si chaque rectangle a été cliqué, nous allons dire si instrument Rex dot collide point avec event, dot position, alors ce que nous allons faire maintenant est que nous allons créer une nouvelle liste, et je l'appellerai active list.

Et nous allons définir quel instrument a été cliqué.

Donc quel que soit ce active list, i fois égal à moins un.

Et donc nous allons utiliser la même logique que nous avions dans notre liste clicked pour notre liste active, mais cela va être un peu plus simple, car ce n'est pas vraiment un tableau, il n'a pas besoin d'être une liste de listes.

Donc nous allons descendre à clicked et lire seulement si clicked, je vais faire une autre liste appelée Active list, vous pourriez l'appeler active channels, active instruments, ce que vous voulez.

Et au début, je vais les définir tous égaux à true car je pense que notre défaut sera d'avoir tous vos instruments allumés.

Et ce sera juste un pour underscore in range of instruments.

D'accord, et cela va simplement nous donner une liste de six uns disant que tous les canaux seront initialement allumés.

Mais si vous cliquez sur un canal, il s'éteindra.

Et où nous allons le mettre à jour, c'est que nous allons entrer dans notre fonction draw grid.

Et nous allons passer cette liste active.

Donc nous allons dire actives, doo doo, doo doo ici, et nous allons leur donner la liste active.

Et maintenant doo doo actives.

Donc vous vous souvenez de cette couleur, gris, blanc, gris que j'ai faite avant, j'aimerais que le texte de chaque instrument soit de la couleur de sa position de liste active.

Donc essentiellement, si vous cliquez dessus, alors je veux qu'il soit un, ce qui signifie qu'il est actif, ou un moins un, ce qui est en fait génial parce que je me souviens, un moins un est le dernier élément dans une liste.

Donc je pense que c'est une manière intelligente de faire maintenant.

Hi Hat text va être colors zéro.

Attendez, attendez une seconde.

Colors, non actives.

00 D'accord, donc laissez-moi être super complet pour expliquer cet élément parce que maintenant c'est un peu confus, nous référençons un élément d'index d'une liste dans une liste.

Mais actives zéro nous dit si oui ou non nous voulons actuellement que hi hat soit actif, n'est-ce pas ? Donc c'est ce qui va être un ou un moins un, selon que hi hat est allumé ou non.

Et donc si c'est un, nous voulons qu'il soit blanc, si c'est un moins un, nous voulons qu'il soit gris.

Donc maintenant, nous faisons simplement cette logique de couleurs que nous avons faite ici, pour les six instruments, et nous nous assurons simplement de mettre à jour leur emplacement d'index.

Et dès que je fais cela, je vais le charger et vous montrer ce que nous faisons.

Donc si je clique sur hi hat, vous pouvez voir qu'il devient gris, ce qui est génial.

Si je clique sur snare, il devient gris, basse drum, je peux désactiver ces instruments.

Mais que signifie cela pour le code réel.

Et donc nous devons entrer dans notre fonction play notes car cela va l'impacter ici aussi.

Donc ce dont nous avons besoin, c'est que si clicked i est égal à active beat.

Et nous devons vérifier et active list à i est égal à positif un.

D'accord, donc c'est tout ce que nous devons faire maintenant.

Parce que lorsque nous vérifions et voyons oh, il est temps de jouer le hi hat, parce que dans mon beat que j'ai configuré, c'est un.

Eh bien, nous avons vérifié et vu que le hi hat est en fait éteint.

Donc ce n'est pas le moment de jouer le hi hat.

Et cela fonctionnera de cette manière pour tous.

Donc c'est tout ce que nous devons faire là.

Mais cela aura toujours l'air vert vif à l'écran.

Et donc cela pourrait être un peu déroutant pourquoi cela ne joue pas, peut-être que vous n'avez pas remarqué que le texte était gris foncé.

Donc ajoutons aussi dans la grille, je pense que j'aime cette idée.

Nous allons monter à ici où nous vérifions les couleurs.

Donc si ce n'est pas sélectionné, cela devrait être ce gris clair, ce gris de base déjà.

Mais ensuite, ce que nous allons faire, c'est à l'intérieur de cette instruction else, nous allons vérifier si actives à J maintenant, c'est en fait J est le beat pour cette boucle.

Donc espérons que ce n'est pas déroutant pour vous.

Mais peut-être que c'est le cas, cela vérifie quel instrument, donc si notre instrument actif est positif, alors la couleur devrait être verte.

Nous y voilà.

Nous y voilà.

D'accord, mais si actives, J en fait, nous pouvons simplement faire un else ici.

Donc nous avons vérifié pour voir si c'était un.

Si ce n'est pas le cas, alors nous allons vouloir que notre couleur soit égale à dark gray, dark gray.

Nous y voilà.

Donc maintenant, laissez-moi expliquer ce que nous venons de faire.

Mais assurez-vous de suivre.

Et espérons que je ne vous ai pas trop confus.

Donc disons que vous avez un hi hat qui joue à chaque beat dans votre boucle.

Et ensuite, vous voulez ajouter un peu de basse.

Mais ensuite, vous voulez voir à quoi cela ressemble sans le hi hat.

D'accord, vous pouvez éteindre ce canal.

Et vous voyez les carrés devenir gris foncé.

Mais ce qui est cool, c'est que cela vous donne toujours la possibilité de l'éditer.

Donc vous pourriez toujours travailler sur votre beat.

Et ensuite l'allumer.

Donc, par exemple, je veux ajouter un peu de crash et un peu de clap.

Je ne sais pas à quoi cela va ressembler, cela pourrait être bizarre.

Mais maintenant, je pourrais rallumer tout ce truc à tout moment.

Et ensuite, vous obtenez ce genre de beat funky, en fait, cela ne sonne pas trop mal.

Et je vais éteindre la basse et les floor toms.

Et nous avons un contrôle individuel des canaux.

Donc c'est vraiment cool.

C'est une autre fonctionnalité cool qu'une boîte à rythmes standard pourrait faire pour vous.

Donc d'accord, nous avons play pause, nous avons beats per minute, nous avons beats in a loop, nous avons toute la capacité d'ajouter des beats, d'ajouter de la vitesse, d'ajouter un hi hat, ou d'éteindre des canaux individuels, des choses comme ça, nous avons vu comment charger la musique.

Donc je pense que nous arrivons au point où nous devons travailler avec un fichier externe pour pouvoir charger et sauvegarder des beats spécifiques que nous avons créés.

Donc nous allons faire cela ensuite, mais j'ai besoin d'une pause rapide.

D'accord, donc la prochaine chose que je veux faire à notre application ici est que j'aimerais ajouter un menu Sauvegarder et un menu Charger.

Et je vais les mettre sur deux menus différents parce que je pense que cela aide un peu à séparer les fonctionnalités, mais vous pourriez probablement mettre tout cela sur un seul.

C'est juste à vous.

Mais commençons.

D'accord, donc commençons simplement par dessiner les rectangles parce qu'à partir de là, nous allons commencer à comprendre comment cela fonctionne réellement.

Donc nous allons descendre là où nous dessinons tout.

Et nous avons tant de rectangles et de beats et de rectangles d'instruments qui sont tous dessinés.

La prochaine chose que nous allons faire est le truc de sauvegarde et de chargement.

D'accord.

Et nous pouvons presque utiliser les mêmes rectangles que nous avons utilisés dans tout le menu, parce qu'il n'y a rien de mal avec eux, ils ont l'air très bien.

Donc nous allons dire Save button est égal à, et ce sera Pygame dot draw rect Skrein.

Gris.

Et maintenant, nous devons nous assurer de les déplacer vers la droite, donc celui-ci, nous allons le mettre à 900.

Et nous allons le mettre à height moins 150.

Et en fait, je pense que ce serait cool, peut-être, si ceux-ci étaient l'un au-dessus de l'autre.

Donc height est 150.

Et ensuite 200, large, et nous allons seulement le faire 48.

Haut, un peu comme les boutons plus et moins, parce que nous allons faire save au-dessus de load.

Et nous allons simplement voir à quoi cela ressemble.

Donc zéro, et cinq, et ensuite nous allons faire load button juste en dessous.

Donc mon copier le même button est égal à Control V et ensuite moins 100.

Et tout le reste est le même.

Oui, ces boutons ont l'air assez bien.

Mettons du texte dessus maintenant.

Donc je vais prendre en fait, je pense que ceux-ci peuvent peut-être être label font, je pense que cela ira bien.

Donc nous allons dire save text est égal à, et ce sera label font dot render devrait être pro à ce stade.

Et nous allons simplement dire save, beat.

Et nous allons le faire vrai.

Et nous allons le faire blanc.

Les gars, épeler les choses correctement, vrai et blanc.

Et je vais prendre tout cela, save text.

Et nous allons faire la même chose pour load, load text, load beat, vrai Drew et wait.

Et ensuite, nous devons les mettre sur l'écran.

Donc screen dot blit.

Screen dot that exit text, et nous voulons le mettre juste un peu à l'intérieur du bouton.

Donc 920 et height moins 140.

Donc il devrait être assez proche du centre du bouton.

Et ensuite, nous allons faire screen dot blitt load text.

Et ensuite, cela peut être 920 aussi.

Et ensuite moins 90.

Et voyons, encore une fois, nous ne pressons pas ces boutons pour l'instant.

Mais oui, le texte a l'air bien.

Vous pouvez jouer avec l'espacement si vous voulez.

Ils sont sur les boutons.

Donc que voulez-vous de plus de vous, les gars ? D'accord, save beat load beat.

Et la raison pour laquelle je les ai mis l'un au-dessus de l'autre est que je veux ajouter un autre bouton.

Une fois que nous avons terminé avec cela, c'est clear board.

Donc, par exemple, vous avez rempli ce tableau avec des carrés, et vous le regrettez totalement et vous voulez simplement tout effacer et recommencer, plutôt que de fermer le programme et ensuite de le rouvrir, nous allons simplement faire une fonctionnalité clear board.

Donc en fait, cela sera plus facile que le save et le load.

Donc faisons clear board, parce que clear est comme trois lignes de code.

Donc clear board, nous allons ajouter CLEAR button.

Et ce sera le même bouton.

En fait, je vais simplement copier tout cela parce que ce n'est que du texte aussi.

Pygame dot draw dot rect screen.

Et ensuite, nous allons vouloir que ce soit à 900, il est 200 de large.

Donc nous allons vouloir qu'il soit à 1150.

Est-ce que cela a du sens ? 1150 et height.

Et celui-ci peut être le 100 haut complet, je pense, et ensuite ce texte aura pour dire clear board.

D'accord, clear board.

Et ensuite, nous allons le mettre à 1160 et height moins 130.

Essayons cela 1160 height moins 130.

Et ce sera clear text et clear text.

D'accord, donc voyons si cela a l'air.

D'accord.

J'aimerais déplacer cela vers le bas, height moins 120.

Cela aura l'air mieux.

Oui.

D'accord, faisons le clear board rapidement, parce que clear est beaucoup plus facile que save et load.

Save et Load va être beaucoup de travail avec des fichiers externes.

Et je pense que cela va être un peu plus rapide.

Donc allons-y et vérifions si le bouton clear est en collision avec le point.

Donc nous allons descendre à notre LFS parce que cela s'intègre bien ici et nous allons dire LF CLEAR button dot collide point event dot pause.

Donc si vous avez cliqué sur le bouton clear, alors en fait ce que nous allons faire est de simplement définir la liste clicked égale à ce qu'elle est au tout début.

Donc, vous savez, nous vérifions combien d'instruments et combien de beats, et nous les définissons tous égaux à moins un.

Eh bien, nous pouvons simplement venir sous notre bouton clear et faire exactement la même chose.

Et donc c'est vraiment tout.

D'accord, vérifions cela rapidement.

Donc nous avons une tonne de hi hats et quelques, nous y voilà, juste un bouton aléatoire, terrible, vous êtes comme, Oh, qu'ai-je fait, clear the board, vous êtes vide, vous êtes libre.

Nous y voilà.

D'accord, donc nous avons la fonctionnalité clear.

C'est génial.

Bon travail.

Maintenant, faisons le save et le load.

Et je veux le faire, où save et load vont en fait arrêter de jouer la musique, et cela va faire en sorte que vous ne pouvez pas cliquer sur le reste de ces boutons.

Donc ce que je vais faire, c'est que je vais créer deux nouvelles variables appelées Save Menu et load menu.

Et nous allons utiliser celles-ci un peu comme playing pour voir, par exemple, si quelque chose est actuellement vrai, donc en haut de be changed, je vais dire Save Menu, et il sera égal à false lorsque le jeu commence.

Et donc nous allons load menu, ils seront tous les deux égaux à false dès le début.

Mais une chose que nous allons faire dès le début aussi, et vous allez vouloir faire cela, vous allez déposer un fichier texte vide dans votre projet Pygame.

Donc si vous devez en créer un dans le monde extérieur et le déposer, c'est bien.

Mais si vous avez un IDE décent, vous pouvez faire nouveau fichier, et ensuite simplement l'appeler comme, my beats ou autre chose dot txt.

J'en ai déjà un appelé Saved beats dot txt, et pour dire, Hé, nous allons utiliser cela à l'intérieur de ce programme, alors vous voulez commencer tôt dans votre fonction et simplement faire file equals open, et ensuite save beats ou autre chose le nom de votre fichier texte est dot txt, et ensuite virgule, et ensuite puisque dès le début, nous voulons lire les données.

Et donc disons que vous fermez votre session, puis deux jours plus tard, vous revenez et vous voulez faire une nouvelle session, vous voulez lire toutes les informations qui s'y trouvent actuellement.

Et nous allons le faire un peu comme un fichier CSV ou un fichier de valeurs séparées par des virgules, où chaque ligne du fichier sera toutes les informations dont nous avons besoin pour un beat.

Donc ce sera combien de beats il y a, combien de BPM, quel nom nous lui avons donné et ensuite la liste clicked de ce gars.

Donc nous allons faire pour line in file, le fichier que vous avez, et nous allons faire une liste appelée Saved beats dot append.

Et ensuite cette ligne, d'accord et saved beats n'existe pas encore.

Donc juste au-dessus de file, faisons simplement saved beats est une liste vide pour commencer.

D'accord, et puisque pour l'instant, nous n'avons aucun beat sauvegardé, ce sera simplement une variable vide jusqu'à ce que nous sauvegardions des trucs plus tard.

Mais c'est ainsi que vous ouvrez et stockez les données d'un fichier initialement déjà, donc allons-y et utilisons Save Menu et load menu.

Maintenant, si nous descendons à nos boutons, et la première chose que nous allons faire est de vérifier si vous avez cliqué sur un bouton.

Donc si vous cliquez sur save menu, ou vous cliquez sur Load menu, et une chose que nous allons ajouter à toute la logique du bouton de la souris jusqu'à présent, c'est que nous allons dire si mouse button up et not save menu et not load menu parce que techniquement tout va être là.

Même après avoir chargé un nouvel écran qui va le couvrir.

Donc nous voulons simplement faire en sorte que vous n'ayez pas à vous soucier de cliquer sur les boutons en dessous après avoir créé un nouveau menu.

Donc tout cela est génial.

Et ensuite, un peu le contre de cela est qu'une fois que nous avons le menu save menu ou load menu, nous devons nous assurer que les boutons qui s'y trouvent peuvent être pressés et nous allons faire cela en ajoutant une nouvelle ligne qui va être et donc Pi game mouse button up et save menu ou et et load menu et nous allons faire cela un peu plus tard.

D'accord, donc passons aux choses sérieuses et ne sauvegardons pas le menu et ne chargeons pas le menu, puis nous allons vouloir quelques LFS ici vérifiant si Save menu ou load menu sont cliqués donc LF Save Menu, save button, dot collide point avec event dot position.

Ensuite, nous voulons que save menu soit égal à true et ensuite nous allons dire L F load menu dot collide point To event dot pause, alors nous voulons que load menu soit égal à true.

Et nous ne voulons pas exécuter ce code pour l'instant, car il désactivera tous nos boutons.

Et nous ne pourrons rien faire d'autre que de le fermer.

Mais cela va faire en sorte que notre Save Menu et notre load menu s'ouvrent.

Et lorsque nous chargeons, je pense, oui, nous allons simplement le laisser comme ça pour l'instant.

Donc ce que je veux dire lorsque je dis que nous devons prendre ce code exact, mais que nous allons devoir faire quelques choses différentes avec, c'est que nous allons utiliser ce menu.

Donc nous allons dire l f.

Maintenant, parce que nous ne voulons pas exécuter cela si Save Menu et load menu sont faux, mais nous allons dire L F event dot type Pygame mouse button up.

Et nous allons simplement dire que nous allons créer des boutons de sortie.

Donc nous allons dire si exit button dot collide point, event dot position.

Et nous allons utiliser un bouton de sortie à la fois sur le Save menu et le load menu juste pour en sortir.

Donc même avant d'avoir réellement configuré la fonctionnalité de sauvegarde et de chargement, nous voulons simplement avoir la capacité d'entrer dans un menu et ensuite de sortir du menu.

D'accord.

Et nous allons simplement nous assurer que playing est égal à true, lorsque vous sortez du menu juste au cas où il se met en pause, il ne devrait pas, parce que nous ne l'avons pas configuré de cette manière.

Mais juste maintenant, nous l'avons.

D'accord.

Donc nous ne faisons rien avec Save menu ou load menu pour l'instant, mais nous voulons le faire, donc allons-y dans nos autres fonctions, où nous dessinons des trucs screen up fill boxes.

Oui, et donc nous voulons faire avant même que la boîte ne soit dessinée.

Donc screen dot fill est la seule chose qui s'est produite jusqu'à présent.

Et nous allons dire si Save Menu, alors nous allons faire une fonction appelée Draw Save menu.

Et ensuite nous allons dire la même chose, si load menu, alors nous allons dire draw load menu.

Et juste pour ne pas oublier, nous voulons nous assurer que nous obtenons le bouton de sortie des deux.

Exit button equals draw load menu, draw Save Menu, d'accord.

Et c'est vraiment ce que nous devons faire, nous devons penser à cela dans l'ordre de ce qui est le minimum que nous devons faire pour que ces menus fonctionnent.

Et ensuite nous pouvons commencer à ajouter la fonctionnalité réelle.

D'accord, donc regardons, cela n'a pas vraiment d'importance lequel nous commençons, ils seront plus ou moins similaires en format.

Donc nous allons descendre juste en dessous de notre draw grid.

Et nous allons faire draw Save menu en premier.

Donc draw def.

Bow, j'ai du mal à taper, def draw Save Menu.

D'accord.

Et nous devons simplement nous assurer que nous retournons un bouton de sortie avant toute autre chose.

Laissez-moi simplement m'assurer que nous n'oublions pas cela.

D'accord.

Et honnêtement, mettons-le simplement sur l'écran d'abord.

Donc nous allons faire exit button.

Et ne l'appelons pas exit button.

Parce que nous utilisons cet endroit si souvent.

Faisons exit btn, juste pour séparer, et nous allons dire exit btn est égal à ce Pygame dot draw dot rect.

Et nous allons le mettre sur l'écran, nous allons le faire gris parce que tous nos boutons sont gris.

Et pour la position x.

Mettons-le très loin à droite, donc avec moins 200.

Faisons avec moins 200 et height moins 100.

Et ensuite pour les inondations, faisons-en un, excusez-moi 180.

Donc il ne touche pas tout à fait le côté droit et 90 donc il ne touche pas tout à fait le bas.

Et ensuite nous allons le faire un rectangle solide avec des bords de rectangle arrondi de cinq comme nous le faisons toujours.

Et faisons un peu de texte exit ici qui va dire close menu en label font.

Donc label font dot render.

Et il va simplement dire close et faire to do true et white.

Faisons cela.

Et ensuite screen dot blit screen dot that exit text, et nous voulons quoi pour les coordonnées de ce gars ? Nous allons le mettre avec moins 160.

Donc nous voulons à l'intérieur de ce bouton avec moins 160 et height moins un oh huit moins 70, ils vont faire un peu de coussin là.

Et voyons, je vais essentiellement copier tout cela pour draw a load menu, juste pour pouvoir initialement tester l'ouverture de ces deux fenêtres.

Mais nous devons en fait, vous verrez, cela va être un peu bizarre.

Si nous ne faisons pas une autre étape, donc disons que nous sauvegardons le beat.

D'accord, nous sommes dans un menu maintenant.

Mais nous n'avons rien fait qui va donner l'impression d'un menu.

Donc boo pool n'a pas d'objet, load menu dot collide point oops, ce, qu'ai-je fait ? Exit button.

Oh, j'ai fait load menu au lieu de load button.

Vous êtes un peu bizarre.

Bizarre.

Pete.

Nous y voilà.

D'accord, déjà.

Donc une chose que je veux dire, nous voulons dessiner un rectangle qui est essentiellement l'écran complet.

Donc Pygame dot draw dot rect, mettez-le sur l'écran, faites-le noir.

Et faites-le de la taille du rectangle entier.

Donc commencez à 00 faites-le de la largeur et de la hauteur complètes, et pas d'arrondi, pas de bords, nous voulons qu'il soit solide, et faites-en la première chose que vous dessinez sur votre menu et faites-le pour les deux.

Donc ce que vous verrez maintenant si je clique sur Save beat, eh bien, vous ne verrez rien parce que j'ai fait quelque chose de mal.

Jetons un coup d'œil.

Oh, donc cela ne fonctionne pas.

Parce que je les ai mis beaucoup trop tôt.

Vous voulez que ces menus soient un peu la dernière chose que vous dessinez.

Donc après que tout le reste est dessiné.

Donc après le bouton clear après tout, nous voulons le dessin de ces menus si les menus sont sélectionnés.

Et la raison pour cela est que ce code dessine les choses dans cet ordre spécifique.

Donc la dernière chose qu'il fait est juste au bas, vérifier si vous avez un menu actif ou non.

Donc nous avons cette capacité maintenant d'aller dans le menu load et le menu Save comme cela.

D'accord.

Et pour illustrer, ce que nous pourrions faire, c'est de dire que pendant que nous sommes dans ces menus, nous pouvons mettre cela en pause.

Donc les boutons ne font rien mais la musique joue toujours.

Et si cela vous dérange, alors une chose super facile à faire serait de définir playing égal à false.

Pendant que les menus sont actifs, je pense que cela pourrait avoir du sens de le garder actif pendant que nous y sommes.

Parce que si vous sauvegardez un beat, peut-être que vous voulez l'entendre pour penser à un bon nom pour celui-ci.

Mais d'accord, c'est bien.

L'important était que nous obtenions ces menus à fonctionner parce que maintenant ces menus sont des ardoises vierges que nous pouvons ouvrir et faire notre travail.

Donc nous pouvons un peu arrêter de nous occuper de la boucle principale, qui est assez encombrée.

Donc nous allons commencer par simplement travailler dans ces menus.

Et donc pour commencer avec le menu draw saved, do to do, faisons draw, save, parce que c'est un peu plus simple de dessiner le menu de chargement, nous devons un peu trier tout ce qui a été sauvegardé.

Et cela peut prendre un peu de temps.

Donc commençons ici, nous avons le rectangle complet.

Appelons ce menu text.

Et nous allons simplement leur dire ce qu'ils font sur l'écran.

Donc nous allons dire render et nous allons dire Save menu.

Entrez un nom pour le beat actuel, d'accord.

Et nous allons le faire vrai comme toujours, blanc comme toujours, screen dot blit.

Comme toujours, et mettons le menu text menu text.

Et choisissons un bon endroit pour environ 440.

Et voyons à quoi cela ressemble.

Donc save menu, entrez les noms du beat actuel.

Cela a l'air assez bien.

Je suis content de cela.

Donc c'est cool, mais nous n'avons pas, nous n'avons pas vraiment fait quoi que ce soit encore.

Nous avons juste cela en cours.

Donc ensuite, mettons quelques, mettons un bouton avant de trop nous soucier de l'espace de frappe.

Mettons un bouton de sauvegarde sur l'écran.

Donc nous allons l'appeler saving button parce qu'il y a déjà un bouton de sauvegarde.

Donc c'est peut-être un peu déroutant, mais c'est ce que nous faisons.

D'accord, pi game, pi Game dot draw dot rect.

Et nous le mettons sur l'écran.

Et nous allons le rendre gris parce que c'est ce que nous faisons avec les boutons.

Et nous allons le mettre un peu au milieu de l'écran.

Donc nous allons faire avec cela, oui, la largeur divisée par deux, divisée par deux, et ensuite nous allons faire moins 200.

Donc celui-ci sera un vrai large, nous allons le mettre à hauteur fois 0,75.

Donc nous allons le mettre à trois quarts du chemin vers le bas de l'écran.

Mais nous allons le faire 400 de large et 100 de haut.

Parce que c'est un gros bouton, c'est un peu tout le but d'être sur l'écran.

Donc nous allons en faire un bouton plus grand.

Saving button, et ensuite nous allons faire saving, oops, gaming, saving text saving txt.

Et cela sera label font dot render, label font dot render.

Et le texte pour celui-ci sera save beat.

Et vrai et blanc.

Et screen dot blit saving text.

Et nous voulons le mettre à peu près au même endroit.

Donc autour de la largeur divisée par deux, peut-être moins 50.

Cette fois, parce que disons qu'il est 100 de large, peut-être, je suppose, et cela pourrait être un bon endroit pour cela.

Et ensuite nous allons faire hauteur fois 0,75.

Et ensuite nous allons faire plus 1020 30, nous allons le mettre au milieu du bouton 30.

Et cela devrait nous donner un gros bouton qui dit save sur l'écran de sauvegarde.

Save be Oui, nous voulons le déplacer un peu vers la gauche.

D'accord, mais nous avons le bouton de beat, ce qui est important.

Et déplaçons-le moins 70.

Je ne sais pas, je fais du wing ici.

Voyons si beat.

C'est assez bien.

D'accord, donc nous avons le beat de sauvegarde.

Et maintenant, une chose, nous retournons déjà le bouton de sortie.

Mais nous voulons également retourner le bouton de sauvegarde.

Parce que nous allons vérifier s'il entre en collision avec lui et le monde extérieur.

Donc allez en bas où vous dessinez votre menu de sauvegarde.

Et nous allons faire exit button et saving button.

Et nous allons utiliser cela plus tard pour vérifier si nous sauvegardons le beat déjà.

Et maintenant nous allons vouloir passer quelques choses dans cela, en fait, nous allons vouloir vérifier le nom du beat actuel, car nous allons taper pour sauvegarder un nom.

Et ensuite nous allons vouloir vérifier si nous tapons activement ou non.

Oui, ce n'est pas heureux, car ceux-ci ne sont pas encore des variables.

Mais nous allons venir ici.

Et nous allons créer ces nouvelles variables, nous allons créer beat name.

Et ce sera simplement une chaîne vide initialement.

Et nous allons créer une nouvelle variable typing, qui sera initialement false.

Et ensuite, si nous venons dans notre menu Draw Save, alors vous verrez que nous passons maintenant beat name.

Et nous passons la variable typing.

Et donc pour faire cela, nous allons créer une nouvelle boîte d'entrée au milieu de l'écran.

Et donc nous allons l'appeler, cela n'a pas vraiment d'importance où nous la mettons, nous allons l'appeler le rectangle d'entrée.

Donc entry rect.

Et cela sera égal à pi Game dot draw dot rect.

Et nous allons le mettre sur l'écran et nous allons le rendre dark gray.

Et nous allons, mettons simplement gray, parce que nous utilisons dark gray pour signifier si oui ou non il a été cliqué.

D'accord, donc screen gray.

Et ensuite, mettons-le à 400 200 600 200.

D'accord, donc il sera les 600 pixels du milieu de l'écran 200.

Nous allons descendre un peu du haut.

Et nous allons faire de ce truc un cinq par cinq.

Donc il y a juste un grand rectangle vide.

Et ensuite, nous allons avoir le texte d'entrée, qui va être essentiellement nous dire ce que nous avons actuellement tapé.

Donc label font dot render, F string de beat name.

Et nous y voilà, vrai, et blanc, et nous allons vouloir blit cela screen, dot blit the entry text et nous allons vouloir le mettre juste à l'intérieur de cette variable, de ce rectangle, d'accord.

Et nous devons retourner le rectangle d'entrée également parce que nous devons pouvoir cliquer dessus et déterminer si oui ou non nous tapons activement ou non.

Et je crois que c'est tout ce dont nous aurons besoin.

D'accord, donc maintenant, revenons à l'endroit où nous appelons cela et assurons-nous que nous retournons le rectangle d'entrée.

Donc non résolu, draw Save Menu a-t-il accidentellement changé le nom de draw Save Menu, beat name et typing, je suis sûr que j'ai mis un autre, oh oui, j'ai mis un point-virgule là, un goose si bête, d'accord.

Et tree rectangle.

D'accord, donc faisons quelque chose avec ces boutons, je vais vous montrer à quoi cela ressemble maintenant, vous devriez l'exécuter vous-même aussi.

Et vous voyez, nous avons ce joli rectangle au milieu où, pendant que nous tapons un nom de beat, il se chargera.

Donc allons-y et fermons.

Et faisons quelque chose avec tous ces boutons que nous avons.

Donc maintenant, nous devons descendre et vérifier quoi faire si toutes ces choses différentes sont cliquées.

D'accord, donc nous sommes dans cette section maintenant, ce L F, type pi game mouse button up, où nous avons les boutons de sortie.

Évidemment, pour réinitialiser tout, et nous allons vider le nom du beat.

Donc si vous étiez à moitié en train de taper un nom de beat, et ensuite vous fermez le menu, nous allons le définir égal à vide.

Et si vous tapiez, nous allons le remettre égal à false parce que maintenant vous n'êtes évidemment plus en train de taper.

D'accord.

Et donc, commençons à examiner les choses que nous venons de définir et dans le menu et ce que nous voulons qu'elles fassent.

Donc si vous cliquez sur le rectangle d'entrée, alors qu'est-ce que vous, si vous cliquez sur ce rectangle, alors ce que nous voulons faire est essentiellement changer l'état de frappe que vous avez.

Donc si entry rect collide, point event dot Pause, pause, alors nous allons dire si typing, alors typing equals false.

Et ensuite nous allons dire L if not typing.

Donc encore une fois, c'est là où si vous faites simplement un else, vous obtiendrez cette petite situation délicate où cela arrive et dit, Oh, si typing, typing equals false, else, mais ensuite l'else vérifie si ce n'est pas typing, et donc vous allez simplement obtenir cette sorte de situation collante.

Donc faites un lf not typing.

Définissez, typing égal à true.

Et nous allons simplement utiliser si typing pour gérer un nouveau type d'événement.

Donc nous allons descendre dans le niveau de ce comme lf.

Donc ce L F, et nous allons dire si event dot type, est égal à et maintenant nous allons utiliser un nouveau type, qui est Pygame dot text input.

Donc c'est que vous avez appuyé sur une touche qui a une valeur de texte, et la variable typing est true.

Et donc c'est ainsi que nous allons gérer la non-modification du nom du beat si vous ne tapez pas activement.

Et ensuite nous allons dire plus égal à event dot text, parce que lorsque vous appuyez sur une touche de texte, un P ou une apostrophe, ou un M, la valeur de la touche réelle que vous avez appuyée telle qu'elle apparaît dans une chaîne est event dot txt.

D'accord, et ensuite nous allons dire si event dot type est égal à pi Game dot key down, et nous allons vérifier si cette touche spécifique qui a été pressée si event dot key est égal à pi Game dot k underscore backspace, donc nous voulons vérifier si la touche backspace a été pressée, et la longueur de beat name est supérieure à zéro.

Et c'est une étape importante parce que si le nom du beat est déjà vide, nous ne voulons pas essayer de supprimer du texte de la variable qui garde la trace du nom du beat, il est déjà à zéro caractère.

Mais ce que nous devons faire ici, parce qu'il n'y a pas vraiment de moyen facile de simplement supprimer un caractère d'une chaîne, vous devez le redéfinir.

Et donc ce que nous allons faire, c'est que nous allons dire que beat name est maintenant égal au beat name actuel.

Et nous utilisons cette plage de caractères.

Et donc, en laissant, en laissant cela comme aucun caractère avant, ce deux-points signifie commencer à partir du tout début.

Et ensuite un moins un signifie aller au caractère qui est juste avant la fin du caractère.

Donc c'est simplement une manière de récupérer toute la chaîne jusqu'au caractère le plus récent.

Et donc juste avec ceux-ci, nous avons ajouté une fonctionnalité qui va nous permettre de supprimer et en fait nous voulons une autre condition de typing là.

Donc maintenant le rectangle d'entrée devrait déterminer si oui ou non nous sommes activement en train de taper ou non.

Et ensuite les caractères de texte d'entrée et de clé vers le bas ici devraient changer si oui ou non nous sommes capables de faire quoi que ce soit, donc nous n'avons pas encore géré le bouton Save réel.

Nous allons le faire ensuite.

Mais maintenant, allons-y et voyons comment fonctionne notre menu.

Donc sauvegarder.

Je vais cliquer ici et maintenant je devrais pouvoir taper Pete, Backspace, Backspace, Backspace.

Je vais taper Pete est cool.

Maintenant, si je clique à nouveau sur ce rectangle, et que je continue à taper.

Oui, il ne fait rien, ce qui est bien.

C'est ce que je veux.

Mais nous n'avons pas visuellement montré cela de toute façon.

Donc revenons dans le menu Save, do Save menu.

Et ajoutons comme un rectangle d'insertion gris foncé qui dit quand il est temps de taper.

Ou peut-être qu'un gris clair aurait plus de sens.

Mais je vais faire avec le gris foncé parce que c'est mon tutoriel.

D'accord.

Et donc ce que je vais faire, c'est que je vais dire avant le rectangle d'entrée, donc où était ce rectangle d'entrée ici ? Oui, Ctrl C, je vais dire si typing.

Et ensuite je vais mettre ce rectangle ici, et il n'a pas besoin de nom, parce que je l'utilise simplement pour signifier si oui ou non nous tapons, et je vais dire dark gray.

Et je vais simplement le faire solide, dans la même empreinte, et c'est bon, parce que nous le dessinons en premier.

Donc votre bordure sera toujours visible.

Et cela devrait maintenant être un bon moyen de signifier donc save beat.

Nous y voilà.

Nous tapons.

Pete, est cool, d'accord.

Et si je clique en dehors, d'accord, maintenant je ne tape plus.

Et maintenant je le suis.

Et je peux faire backspace, et autre chose.

Et si je le ferme, il sort, et c'est génial.

Donc allons-y et gérons le bouton Save.

Et je l'ai un peu repoussé parce que travailler avec des fichiers externes et sauvegarder des données dans un fichier texte est juste quelques étapes supplémentaires.

Et, et nous devons un peu choisir quelles données stocker et dans le bon format.

Et c'est un processus.

Donc plongeons dedans.

Parce que c'est très important pour la fonctionnalité de cela, évidemment, être capable de sauvegarder vos beats préférés et revenir et les utiliser plus tard est un énorme avantage pour ce genre de chose.

Donc nous allons descendre ici où nous avons notre rectangle d'entrée, et nous allons en ajouter un nouveau.

Et nous pouvons vraiment faire ceux-ci comme des LFS aussi.

Et donc nous allons dire l f.

Saving button, soyez très prudent parce que maintenant nous avons un bouton save et un bouton saving.

Et nous allons dire collide point avec event dot pause.

Et si c'est le cas, alors ce que nous voulons faire est un peu comme avant, file equals open, et notre fichier saved beats dot txt.

Mais cette fois, rappelez-vous, au tout début, nous l'avons lu pour stocker des données dans cette variable.

Maintenant, nous allons faire un W et cela signifie que nous allons écrire dedans.

Et ce que nous allons faire, c'est que nous allons prendre cette liste saved beats, save beats que nous avons faite au tout début.

Et nous allons ajouter quelques données.

Et si vous vous souvenez, je sais que c'était il y a un moment, nous avons dit ce que nous allons ajouter, nous voulons toujours commencer cela par une nouvelle ligne.

Parce que si vous ne le faites pas, alors chaque fois que vous sauvegardez, alors vous pourriez potentiellement sauvegarder sur le même fichier.

Et ensuite, la manière dont nous analysons les données avec comme par ligne, en les stockant comme une entrée dans notre liste serait fausse.

Donc nous allons le faire de cette manière.

Nous allons faire name, deux-points, et ensuite espace.

Et ensuite nous allons faire des crochets de chaîne, beat name.

Donc c'est ce que vous avez entré sera underscore name, d'accord.

Et ensuite nous allons faire une virgule, et ensuite nous allons faire beats deux-points espace, accolades, beats, et faites attention au format avec lequel vous l'enregistrez.

Parce que plus tard, nous allons un peu devoir inverser cela pour notre menu de chargement.

Donc nous enregistrons tout ce dont nous aurions besoin.

Nous enregistrons tout ce dont nous aurions besoin pour pouvoir rappeler cela plus tard, nous enregistrons la liste clicked, nous enregistrons combien de beats et de beats par minute, et ensuite un nom que nous lui avons donné pour pouvoir le sauvegarder.

Et donc nous allons ajouter cela comme un élément à notre liste saved beats, ce qui signifie qu'il va être au format d'un beat sauvegardé.

Et ensuite ce que nous allons faire, c'est que nous allons dire pour i dans la plage, longueur de saved beats, nous y voilà.

Nous voulons faire file dot write une chaîne de saved beats.

Et c'est ce que vous devez faire parce que pour écrire dans un fichier txt, cela doit être une chaîne.

Donc vous devez faire une conversion de chaîne de chaque entrée de votre liste saved beats.

Et ensuite pour le sauvegarder en dehors de cette boucle for, nous allons faire file dot close.

Et cela fermera le fichier texte, file les nouvelles données, et ensuite nous allons fermer le menu.

Donc maintenant Save Menu est égal à false, capital F false, parce que si vous venez de sauvegarder votre beat, il n'y a vraiment aucune raison de rester là.

Et ensuite nous allons définir typing égal à false parce que c'est un peu notre défaut et nous allons vider la variable beat name.

Donc c'est un peu comme dire que vous avez accompli ce pour quoi vous êtes ici.

Et maintenant, même si nous n'avons pas de moyen de le recharger, vous pouvez voir que nous avons un fichier M Do you save beats txt en ce moment, allons-y et en créons un.

Donc faisons un beat.

Je vais simplement en faire un comme un beat rock générique, que j'ai fait.

Génial, j'ai fait un beat de sauvegarde ama l'appeler generic rock beat.

Et je vais cliquer sur Save beet.

Et voyons.

C'est bon signe, cela n'a rien fermé.

Allons-y maintenant et regardons notre fichier texte, afin que vous puissiez avoir une idée de la manière dont nous le sauvegardons.

D'accord, c'est assez cool.

Son nom est generic rock beat, beats huit BPM, 240.

Et ensuite sélectionné et c'est la liste, vous pouvez voir qu'elle a tous les hi hat.

Donc c'est ce que ce premier est.

Et ils sont tous allumés, c'est pourquoi ils sont tous des uns.

Et ensuite c'est la caisse claire, je crois.

Et vous pouvez voir que ce sont juste les trois.

Donc comme, 12341234 pour la caisse claire, la grosse caisse est un et ensuite un, un.

Donc vous pouvez voir que c'est une liste de tout ce dont nous aurions besoin pour recréer ce beat.

Donc une fois que nous l'avons sauvegardé, nous pourrions l'effacer, nous pourrions le fermer et passer à autre chose.

Et, et c'est vraiment cool.

Mais nous n'avons aucun moyen de le recharger pour l'instant.

Cela nous amène au menu de chargement.

Et je l'ai repoussé parce que c'est probablement le plus délicat, nous devons prendre toutes ces informations que nous avons mises dans un fichier texte, et nous devons les inverser à partir d'un fichier texte.

Donc commençons, je prends une gorgée d'eau ici.

D'accord, donc dans le menu draw load menu, nous avons le rectangle de retour, et nous avons le bouton de sortie, ce qui est une bonne façon de commencer.

Je vais un peu empiéter sur le menu text d'ici et le texte de sauvegarde et les voler un peu parce que nous allons simplement les réutiliser pour un menu text, qui maintenant dira load menu et select a bit to load in, nous allons simplement dire load, c'est bien.

Ils savent ce qu'ils font.

Et au lieu de saving button, nous allons dire loading button.

Et au lieu de saving text loading text, et cela dira load beat, et cela dira loading text, mais les positions sont probablement bonnes.

Et évidemment, en plus du bouton de sortie et de tout, nous allons vouloir faire le bouton de chargement aussi.

Et je pense que nous allons aussi vouloir un bouton de suppression probablement parce que peut-être que vous en avez mis trop là maintenant.

Donc faisons simplement aussi un delete BTN.

Ce sera bien.

Et donc nous avons un bouton de chargement.

Allons-y et ajoutons le texte de chargement.

Allons-y et faisons un bouton de suppression, delete BTN.

Et où devrions-nous mettre ce bouton de suppression Pygame dot draw dot rect rect et screen et gray vous savez comment il est.

Et mettons celui-ci sur l'écran à peu près.

Donc nous allons faire la largeur divisée par deux pour obtenir le point milieu.

Et nous allons faire moins 400.

Donc un peu décalé à gauche de là avec moins deux moins 400, ce sera la position de départ.

Nous allons le mettre un peu plus bas.

Donc la hauteur fois ce que devrions-nous faire point neuf.

Je ne sais pas, je deviens un peu délirant, c'est un long tutoriel.

D'accord, nous allons le faire solide.

Nous allons en faire un rectangle arrondi.

Et nous allons simplement voir où cela se trouve, comment cela a l'air et partir de là.

Je ne sais pas pourquoi je mettrais cela à point neuf, cela devrait être à la même hauteur que le bouton de chargement.

Mais voyons.

Donc si cela commence à avec moins 200 et celui-ci commence à moins 400.

C'est 200.

Cela va toucher notre bouton de chargement.

Essayons de faire cela 500, je ne sais pas, je joue maintenant, je suis en eaux inconnues.

D'accord, nous devons ajouter du texte, nous devons faire delete text et le mettre sur notre bouton de suppression.

Et cela sera label font dot render.

Et cette fois, nous allons faire delete beat pour le texte.

Delete, beat.

D'accord, et ensuite il devrait être blanc.

Et d'abord, nous devons faire vrai pour l'anti alias blanc.

Allons Pete, vous le savez et ensuite screen dot blitt et ensuite delete text.

delete text.

D'accord et pour l'emplacement sur celui-ci, nous voulions simplement voler la position de départ x&y d'ici CTRL C vers le texte et le déplacer un peu à l'intérieur.

Donc voyons avec maintenant moins 500 au lieu de 500.

Faisons comme 485 et ensuite height fois oh, point sept cinq mon ami.

D'accord.

Et ensuite plus 10.

Vérifions cela, load beat.

Soyons honnête, ce n'est pas la pire chose au monde, n'est-ce pas ? D'accord ? Cela a l'air bien, allons-y et déplaçons delete beat un peu vers le bas.

Qu'avons-nous fait pour l'autre plus 30.

Nous allons faire plus 30 à nouveau.

D'accord, et maintenant nous devons si exit button tuple n'a pas d'attribut do collide point bien, qui est un tuple ? Ici ? Exit button Pygame dot draw dot rect.

Je ne comprends pas tout à fait pourquoi j'ai eu cet air.

Load beat.

Close.

Oh.

Donc l'objet tuple n'a pas d'attribut collide point, je comprends ce que cela signifie.

Mais exit button est juste ici.

Draw load menu, exit button loading button, delete button.

Oh, peut-être que c'est parce que nous n'avons pas encore dit au bouton de chargement.

Il reçoit quelques choses.

Donc attendez, nous retournons exit button loading button, delete button, descendez à l'endroit où vous appelez ces menus.

Et c'est exit loading button et delete button.

Et maintenant le bouton Close devrait fonctionner à moins que je ne sois fou.

Et je ne le suis pas.

D'accord, bon travail.

Eh bien, je le suis peut-être, mais continuons.

D'accord, donc dans le menu de chargement, nous devons un peu configurer une zone qui va être là où nous affichons les infos de nos beats chargés.

Donc load menu, select a beat to load, nous disons que nous mettons le texte sur l'écran.

Mais nous ne montrons pas actuellement, comme la zone où les beats pourraient être.

Donc dessinons, je pense, comme une sorte de parc d'attente, comme un rectangle extérieur où toutes les données vont être affichées.

Donc faisons simplement Pygame dot draw dot rect.

pour cela.

Laissez-moi réfléchir, quelle est la bonne façon de faire cela ? Oui, dessinons un parc d'attente, si vous voulez.

Et disons pi Game dot draw dot rect.

Et mettons-le sur l'écran.

Et faisons-le gris.

Et donnons-lui 190 100 Plus, qui commençons à 190 200.

Voyons simplement à quoi cela ressemble.

Et faisons-le, je ne sais pas, 1000 de haut et 600 de large.

Je ne sais pas, je suis un peu en conflit ici.

Parce que je veux que ce soit, je pense, comme un contour.

Mais je ne sais pas si cela a plus de sens de l'avoir comme un rectangle solide pour afficher les beats chargés.

Donc peu importe ce que j'ai fait, c'est hideux, corrigeons cela.

D'accord, corrigeons ce rectangle, je pense que 190 90, nous pouvons le faire 1000 de hauteur, ce sera bien.

600 devrait être bien.

Cinq et cinq est probablement correct, je pense que ce que nous allons faire, load beat, je pense que ce que nous allons faire est simplement descendre load et delete, nous avons mis load et delete plus bas parce que je veux vraiment montrer plusieurs beats différents.

Donc peut-être au lieu de point sept, cinq sur ceux-ci, nous faisons essayer comme point neuf ou proche de celui-ci.

Déplaçons ceux-ci vers le bas et faisons comme point.

Je ne sais pas, huit, sept.

Essayons cela point huit 7.8 7.87 plus 30.

Jetons un coup d'œil à cela load beat.

Nous y voilà.

Ce n'est pas mal, en fait.

Un peu comme ce rectangle d'entrée.

Et donc, allons-y et appelons cela quelque chose.

Je ne sais pas.

Beats rectangle.

Loaded rectangle.

Nous allons l'appeler loaded.

Rectangle.

rec angle.

Oui.

Et je pense que nous voulons le retourner aussi.

Parce que si vous cliquez quelque part là-dedans, vous sélectionneriez probablement un beat.

D'accord.

Donc, descendons à notre fonction où nous récupérons des trucs, le bouton de sortie, et nous allons dire loaded rectangle en bas.

D'accord.

Ou loaded, cela n'a pas vraiment d'importance.

D'accord, et voyons comment analyser les données dans ce menu draw load.

Donc nous devons un peu vérifier sur quel index a été sélectionné.

Donc d'abord, vous savez, nous devrions faire, nous avons un fichier texte avec un beat sauvegardé.

Allons-y et en créons un deuxième.

D'accord, donc faisons cela stupide.

Ce n'est pas le pire, pas la pire chose au monde.

Mais je vais simplement l'appeler Tom et clap.

Sauvegardez le beat.

Et allons-y et fermons cela et regardons notre fichier texte.

Donc maintenant vous voyez, nous avons ces deux.

Et disons que nous avons le menu de chargement.

Et nous voulons analyser les données de ces deux et les montrer à l'écran, nous voulons montrer combien de beats ils ont.

Nous voulons montrer leur nom, et tout.

Donc ce que nous devons faire, c'est que nous devons commencer à vérifier, comme, comment obtenons-nous les trucs spécifiques à l'intérieur de ceux-ci.

Et donc nous allons simplement plonger dedans.

Il n'y a pas de moyen facile de faire cela.

Donc voici ce que nous faisons, nous commençons et nous disons pour beat, dans la plage, longueur de saved beats.

Donc rappelez-vous, save beats est une liste, où chaque élément de la liste est une longue chaîne qui contient l'un de ces beats sauvegardés.

Donc pour beat dans la plage longueur de save beats, et mettons simplement en place notre rectangle, l'affichage 10.

Donc si b est inférieur à 10, ce qui signifie que nous allons commencer à zéro.

D'accord, beat clicked, va être égal à une liste vide.

Et nous devons simplement mettre en place quelques trucs pour analyser cela, c'est une chaîne vraiment longue.

Donc row text va être égal à medium font dot render, et nous allons simplement montrer quelle ligne c'est.

Donc ce sera F, et ensuite c'est une chaîne de format, et il y aura bt plus un, parce que cela va commencer à zéro.

Mais encore une fois, je ne pense pas vraiment que nous devrions dire quoi que ce soit est le zéro avec beat, ce sera le premier beat.

Et nous allons dire vrai et blanc.

Et nous allons le mettre sur l'écran.

Donc screen dot blit.

Et nous allons lui donner le row text.

Et nous allons le mettre à 200 100 plus le beat 200 100 plus le beat fois 50.

Donc c'est ainsi que nous allons faire cela pour chaque 10.

Parce que le rectangle fait comme 600 de haut.

D'accord, donc cela devrait être tout ce que nous devons faire pour mettre le row text dessus.

Mais nous devons commencer à obtenir quelques index.

Donc c'est là que si vous êtes familier avec la manipulation de chaînes en Python, vous serez un peu en avance sur la courbe, car beaucoup de ce que vous êtes sur le point de voir pourrait ne pas avoir beaucoup de sens, à moins que vous ne soyez familier avec les chaînes.

Donc nous devons déterminer où commencer le nom.

Et donc nous allons dire saved beats.

Donc c'est la liste de tous les beats que nous avons sauvegardés, et ensuite beat donc nous appelons notre chaîne spécifique.

Et ensuite nous devons trouver la valeur d'index.

Donc c'est là où dans cette chaîne, nous voyons pour la première fois cette sous-chaîne spécifique.

Donc l'index de name colon space, et vous verrez pourquoi j'ai été si particulier lorsque nous avons configuré cette instruction write que nous avons faite, parce que nous devons la répliquer à l'envers pour la déchirer.

D'accord, et ensuite parce qu'il y a six caractères dans cette chaîne, et un m, e, deux-points et espace, nous allons ajouter un six juste là.

Et ensuite l'index de fin du nom, doo doo doo doo, et sera égal à saved beats à beat dot index.

Et ensuite ce sera donc où la prochaine chose dans notre chaîne est ajoutée.

Et donc si vous y pensez, je vais en fait ouvrir le fichier texte ici.

Le nom se termine lorsque nous arrivons à deux-points espace beats.

Donc nous devons faire cette chose où nous vérifions où chaque morceau commence et se termine en faisant cela.

Donc beats juste comme cela sera où nous voulons le terminer.

Et ensuite name text.

Le texte réel pour chacun de ceux-ci sera égal à et nous allons faire ce medium font afin de pouvoir le mettre sur screen dot render.

Et ensuite le texte pour cela sera saved beats de apt beat donc cela vous dit quel élément utiliser.

Et ensuite nous devons faire ce qui va être de name index start et ensuite colon name index end.

Et donc cela peut sembler un peu déroutant, mais nous venons de faire ce qui est de dire d'accord, prenez la liste de tous les safe beats, choisissez celui pour celui spécifique que nous regardons et ensuite de là où ce texte de nom s'arrête.

Donc essentiellement, le caractère suivant, après que ce name, deux-points espace apparaît jusqu'à ce que ce deux-points espace beats apparaît.

C'est le texte réel qui est le nom sauvegardé pour ce beat.

Et ensuite nous voulons qu'il soit vrai, et ensuite blanc, et ensuite nous le mettons sur l'écran.

Donc screen dot blit.

Et ce sera le name text.

Et ce sera virgule, et ensuite 240.

Et ensuite 100 plus bT fois 50.

Ce n'est pas les fois là nous y voilà.

Beat fois 50.

Et donc c'est juste où nous mettons le Rotex aussi.

Et allons-y et commençons simplement par là.

Parce que je pense que si vous êtes familier avec la manière dont cela fonctionne, lorsque nous allons dans le menu de chargement, vous pouvez voir que nous avons generic crack, beat, Tom et clap.

Et ce sont les premier et deuxième noms.

C'est vraiment génial.

Donc c'est génial.

Ce que nous devons faire maintenant, c'est que nous devons déterminer comment analyser le reste des données car ce n'est qu'un des éléments.

Et c'est génial pour les montrer à l'écran.

Mais nous devons aussi déterminer comment obtenir les beats par minute et la liste sélectionnée.

Donc cela va être un peu délicat.

Soyez patient avec moi.

Et encore, si vous vous perdez dans les détails, n'hésitez pas à ralentir la vidéo, à regarder à nouveau les parties qui vous confusent et à poser vos questions dans les commentaires ci-dessous.

D'accord, donc maintenant ce que nous allons faire, c'est que nous allons dire si zéro est inférieur ou égal à l'index, et nous allons en venir à cette variable d'index que nous allons créer dans juste une seconde.

Donc si c'est supérieur à zéro et inférieur à la longueur de saved beats, je tape partout, Shift Tab, sortez de là, nous y voilà.

Et inférieur à la longueur de notre fichier saved beats, donc cela signifie que vous avez actuellement un beat sélectionné, nous allons utiliser l'index comme un moyen de sélectionner un beat spécifique.

Donc cela, je vais le mettre ici, afin de ne pas oublier de le passer.

Mais nous allons sélectionner en cliquant sur l'un de ces noms de beat, nous allons sélectionner celui que nous voulons charger.

Et cela va être la variable d'index.

Et ensuite, en fonction de ce qui a été sélectionné, nous allons devoir faire un travail supplémentaire.

Donc nous allons devoir déterminer où l'index et pour les beats est.

Et cela va être égal à saved beats à notre beat spécifique.

Donc c'est pourquoi nous voulons toujours qu'il soit do attendez une seconde, vérifions saved beats.

Et nous voulons ajouter une deuxième condition ici, et B est égal à index.

Donc c'est pourquoi nous mettons cela à l'intérieur de nos boucles for, parce que cela va vérifier et voir si, pendant que nous obtenons les noms de chaque beat, cela va vérifier et voir si nous avons également activement sélectionné un beat.

Et donc et b est égal à index.

D'accord, ensuite ce que nous allons faire, c'est que nous allons dire à ce point d'index, donc comme avant, et maintenant le suivant commence à deux-points espace, assurez-vous que votre chaîne dans une variable de chaîne deux-points espace BPM, parce que c'est là que la variable beats par minute commence.

Et donc cela rend les beats chargés, loaded beats, qui est une nouvelle variable égale à l'entier de saved beats dot beat, essayez d'être très prudent ici parce que nous devons faire cette sorte de double indexation encore, donc ce n'est pas safe beats que be it save beats at beat.

Et ensuite nous devons faire de name index end plus huit à beat index.

Et donc la raison pour laquelle cela commence à name index end est parce que ou name index n plus huit caractères est parce que cela va commencer avec le deux-points.

Et cela se termine huit caractères plus tard, ce qui est lorsque la valeur beats réelle commence.

Et c'est pourquoi nous mettons un i n t ici pour le convertir en un nombre.

Donc ce qu'il fait, c'est que nous indexons de ce caractère à ce caractère, et nous le transformons en un nombre, donc même si cela ressemble à huit comme un nombre, cela est en fait à l'intérieur d'une chaîne.

Donc ce n'est qu'un autre caractère de chaîne jusqu'à ce que nous fassions ce i n t.

Mais maintenant, nous obtenons les beats chargés, ce qui est génial.

Et nous devons faire essentiellement la même chose pour le BPM, donc l'index de fin du BPM, do index end, qui est une nouvelle variable aussi, sera égal à saved beats at beat.

Et ensuite il sera dot index.

Et celui-ci sera maintenant quand deux-points espace selected, je ne l'ai pas mis entre guillemets à nouveau.

Nous y voilà.

Quand cela apparaît, cela sera l'index qui dira, d'accord, c'est la fin de la section BPM selected, et cela rendra le loaded be PMS égal à peu près la même chose que ce loaded beats juste avec une valeur d'index différente.

Donc je vais prendre cela.

Donc celui-ci va aller de non pas de name index, et mais de beats index et et ce ne sera pas plus huit, ce sera plus six.

Je pense que j'ai tapé huit à nouveau, et ensuite celui-ci va aller jusqu'à BPM index et beats index et interest, dang, oh, c'est juste beat index.

Et nous y voilà.

D'accord, et donc maintenant nous avons le BPM, les beats et le nom.

Et ce que nous n'avons pas, c'est juste la partie la plus délicate, qui va être la liste sélectionnée.

Donc nous avons maintenant loaded clicks, oui, parce que nous l'appelons clicked dans le monde extérieur.

Donc loaded clicks, et je vais le différencier à loaded clicks en tant que chaîne sera égal à saved beats, à beat.

Et ensuite nous avons en fait toutes les infos dont nous avons besoin pour le reste de celui-ci, ce sera BPM index, et, mais ensuite celui-ci sera plus 14, d'accord, et je vais expliquer pourquoi c'est plus 14.

Et cela va aller essentiellement à la fin moins trois caractères.

Et la raison pour cela est que nous devons faire ce qu'on appelle la séparation des chaînes.

Donc si vous dites, c'est là que cela a commencé, donc 1-234-567-8910 1112 1314 caractères avant d'arriver au premier un, ou moins un dans notre liste, et ensuite si vous allez à la toute fin, nous avons un espace et ensuite deux crochets fermants à la toute fin, c'est pourquoi cela va à moins trois, cela va nous donner une chaîne de toutes nos valeurs.

Maintenant, nous devons diviser cette chaîne en une liste.

Et pour cela, nous allons utiliser la fonction intégrée Split, mais nous devons leur dire sur quoi séparer chaque élément de la liste.

Donc nous allons le diviser, nous descendons à loaded, clicks, et nous allons appeler cela maintenant une ligne, des lignes, parce que nous devons le diviser deux fois, oui, c'est actuellement juste une longue chaîne, nous devons le diviser en une liste de chaînes, et ensuite nous devons diviser chaque chaîne en uns et moins uns réels.

Donc pour cela, nous créons cette liste intermédiaire, qui sera loaded clicks rows, et définissons-la égale à la liste.

Et ensuite à l'intérieur de cela, nous faisons loaded, clicks string.

Et ensuite dot split est la fonction intégrée pour diviser une longue chaîne en une liste.

Et ce sera un crochet ouvert comme cela, et ensuite une virgule, et ensuite un espace, et ensuite un crochet fermé ou en arrière, un crochet fermé, une virgule, un espace, un crochet ouvert.

Et la raison pour cela est encore une fois, si nous regardons le fichier texte, ce qui sépare entre chaque entrée, chaque élément dans cette liste sélectionnée est un crochet fermé et ensuite une virgule, et ensuite un espace et ensuite un crochet ouvert.

Et donc c'est ce qui va diviser chaque élément en son propre élément de liste ici.

D'accord, donc maintenant, nous devons faire des choses plus compliquées.

Donc soyez patient avec moi.

Et une fois que nous aurons terminé, prenez simplement un bon coup d'œil à ce que chaque ligne fait et réfléchissez à ce qu'elle fait.

Et essayez vraiment de comprendre et ensuite demandez-moi si vous avez encore des questions après cela.

Mais donc pour row dans la plage, la longueur de la liste loaded clicks rows que nous venons de faire.

Donc nous configurons une boucle for pour passer par là.

Et nous allons dire, si loaded.

Clicks do to do ici nous y allons.

Si loaded clicks row, item.

Donc item est juste en train de vérifier.

Nous ne voulons pas que cela soit row, nous voulons que cela soit item.

Je m'avance, nous voulons que cela soit row et nous voulons dire loaded.

Clicks row Okay, est égal à, et je vais simplement créer une autre variable intermédiaire juste pour me clarifier l'esprit, parce qu'il y a beaucoup de mots en cours.

Donc nous allons dire load clicks row est égal à loaded, clicks, rows pluriel à cette row spécifique.

Et ensuite ce que nous allons faire, c'est que nous allons diviser cet élément de row split out.

Et nous allons le faire en fonction d'une virgule, et ensuite d'un espace.

Et la raison pour laquelle j'ajoute l'espace est que lorsque vous faites une division, cela va donner à chaque chose entre ceux-ci son propre élément dans la liste, mais cela va se débarrasser de ce texte qui était dans la chaîne.

Donc nous le faisons de cette manière.

Et ensuite cela va le diviser et faire une nouvelle liste et cela que nous allons stocker et loaded clicks row.

Et ensuite ce que nous allons faire, c'est que nous allons passer et dire pour item, parce qu'ils ne sont pas encore des entiers dans la plage, et ce sera la longueur de loaded clicks row que nous venons de faire.

D'accord.

Et ce que nous allons faire, c'est que nous allons vérifier si loaded clicks row singulier, à item, est égal à, et nous allons vérifier s'il est égal à la chaîne de un, ou à la chaîne de moins un.

Et la raison pour laquelle nous faisons cette vérification est que, une fois que cela a été trié une fois, nous ne voulons plus l'exécuter.

Donc nous allons dire ou si loaded clicks item est égal à moins un, parce qu'en théorie, ce sont les deux seules choses que les éléments devraient jamais être égaux.

Et nous n'avons pas besoin d'un autre si, nous avons juste besoin d'un ou.

Donc s'il est égal à une valeur de chaîne de un ou à une valeur de chaîne de moins un, alors ce que nous faisons, c'est que nous disons que loaded clicks row item est égal à la valeur entière de loaded clicks row, à item.

Et la raison pour laquelle nous faisons cette vérification est que, une fois que cela est devenu un entier, cela ne s'exécutera plus.

Donc nous n'avons pas à l'exécuter à nouveau, parce que tout est déjà un entier.

D'accord.

Donc c'est pourquoi nous faisons cela.

Et ensuite nous sortons du if et nous disons que nous voulons suivre quel beat était, quel beat chargé était, laissez-moi dire cela correctement, nous voulons faire une liste des valeurs clicked de ce qui a été chargé.

Donc si nous avons cette liste loaded, collect list qui reflète essentiellement le monde clicked extérieur, alors nous voulons nous assurer que nous ajoutons au bon moment.

Donc nous allons revenir ici où nous avons fait cette liste beat clicked.

Et nous allons append chaque liste ici.

Donc nous allons dire, laissez-moi m'assurer que j'ai mon indentation, beat clicked dot append.

Et nous allons ajouter loaded clicks row, chaque fois que nous faisons une autre row.

Et ensuite nous allons dire loaded click est égal à beat clicked, nous y voilà.

Et nous allons vouloir, ainsi que le loaded rectangle, nous allons vouloir retourner le loaded clicked.

Mais en fait, nous devons retourner le loaded clicked, et nous devons retourner les beats et le BPM.

Donc faisons une autre variable ici.

Et appelons-la loaded info.

Et faisons-en une liste.

Et donc elle aura loaded beats dedans.

Elle aura loaded BPM dedans, et elle aura loaded click dedans.

D'accord, mais ce que nous devons faire, parce que maintenant il y a un scénario raisonnable où rien n'a encore été sélectionné.

Et donc ceux-ci pourraient ne pas exister, parce que pour l'instant la seule place où nous les définissons est si quelque chose a été sélectionné, si nous avons défini cette valeur d'index, donc ce que nous voulons faire au tout début, c'est simplement les initialiser comme vous le feriez au début de votre programme, mais nous allons le faire à l'intérieur de la fonction.

Donc loaded clicked equals zéro, loaded beats equals zéro.

Load collect est une liste vide, pas zéro, mais vous voyez l'idée.

Et loaded BPM est égal à zéro.

D'accord, donc nous devons faire ces trois choses.

Et ensuite nous le passons tout en arrière dans loaded info.

Et donc nous allons passer cela à la place.

Cela a été, je le sais, l'une des choses les plus compliquées que nous ayons faites, manipuler des chaînes comme cela est un peu délicat, mais nous avons en fait fait des choses assez avancées ici.

Donc si vous êtes un débutant, vous devriez vous féliciter si vous avez simplement réussi à suivre et à comprendre la plupart de ce que nous venons de faire, car c'est un travail de chaîne assez délicat.

Maintenant, nous devons un peu descendre à la gestion des événements et configurer ce que nous voulons que chacune de ces choses fasse.

Donc nous descendons ici dans la zone qui est en dehors de la vérification qu'il ne s'agit pas du menu Save et du menu load.

Donc c'est la deuxième partie.

Et nous allons descendre, doo doo doo doo si saving button client point longueur file.

D'accord, donc le bouton de la souris est en haut, le rectangle d'entrée.

Ce que nous voulons faire maintenant, c'est de dire, do L F, et que disons-nous loaded rectangle.

Donc si loaded rectangle a été cliqué, alors nous voulons que l'index soit égal à, et nous allons utiliser cette position d'événement à un, qui est la position y, moins 100.

Et ensuite nous allons diviser cela par le plancher par 50.

Et cela nous donnera une valeur de un à 10, nous disant comme où sur le fil sur l'axe y nous venons de cliquer.

Et nous allons utiliser cet index pour ce que le beat actif devrait être.

Donc revenons en haut et loaded menu et utilisons cet index pour dessiner quelque chose qui va indiquer le beat activement sélectionné.

D'accord, donc dans notre menu loaded, nous passons l'index, laissez-moi m'assurer que nous le passons vraiment.

Load menu drop down menu, nous y voilà.

Nous voulons nous assurer que nous le passons.

Et en fait, nous ne l'initialisons pas au début, n'est-ce pas, donc appelons-le ici, nous allons simplement dire, index est initialement égal à 100.

De cette façon, il n'est pas sélectionné.

D'accord, et draw load menu dira, d'accord, si load menus est là, mais nous voulons utiliser l'index pour dessiner un rectangle sur l'écran, s'il est dans notre plage, donc sous load rectangle, je vais dire si l'index si zéro est inférieur ou égal à l'index, et il est inférieur à la longueur de notre liste saved beats, donc cela vérifie que nous avons un est inférieur à la longueur de notre liste, alors nous allons Pygame dot draw dot rect l'écran, nous allons le faire, faisons un gris clair.

Donc ce sera le dernier gris que j'ajoute, je le jure.

Et nous allons le faire 190.

Et ensuite nous allons le commencer à 100 Plus index fois 50.

Et nous allons le faire 1000 de large et 50 de haut.

Donc gris clair.

Allons-y et définissons cela en haut.

Et encore une fois, il s'est déplacé dans la direction opposée de notre gris de base.

Donc gris clair, et ce sera comme oh, comme un 171 7170 D'accord, et maintenant j'espère que lorsque nous faisons le menu de chargement, load beat a cassé quelque chose trop de valeurs à déballer attendu quatre, parce que je ne pense pas que je lui ai dit de s'attendre à ce que loaded info revienne encore.

Donc voyons.

Law load menu loaded info, et load rectangle loaded info.

Correct.

Nous y voilà.

Load info.

D'accord, donc maintenant, ouvrons loaded beat.

Generic rock beat.

Oh, la chaîne n'a pas.

Oui, sûr que j'ai voulu dire index, j'ai sûr que j'ai fait.

Donc allons vérifier cela.

Et lequel d'entre eux ai-je mis index pour ? index, index index.

Nous y voilà.

D'accord.

Essayons cela à nouveau.

Load beat, hey, nous avons un rectangle gris clair.

Si je clique sur le premier, si je clique sur le deuxième, si je clique sur le troisième, il disparaît, super, parce qu'il n'y a pas de beat là.

Et je clique sur ceux-ci.

C'est génial.

Mais nous ne sommes pas encore capables de supprimer des choses.

Et nous ne sommes pas encore capables de charger des choses.

Donc continuons à travailler sur les boutons.

D'accord, retour à notre gestion des événements ici.

Et il y a peut-être des moyens dont j'aurais pu configurer cela différemment.

Mais je les ai un peu faits comme nous sommes arrivés à chaque événement.

Donc descendons ici et disons, d'accord, nous avons tous ces LFS LFS loaded rectangle.

Faisons l if delete button dot collide point avec event dot position.

Et ensuite si nous avons supprimé quelque chose, alors ce que nous devons faire n'est pas trop mal.

C'est si index.

Donc à peu près la même chose.

Si index est entre zéro.

Donc index doit être supérieur ou égal à zéro.

Et index doit être inférieur à la longueur de saved beats.

Et je peux dire inférieur parce que la longueur de save beats sera toujours un de plus que la plus grande valeur d'index.

Donc s'il y a trois valeurs là-dedans, leurs index sont 01, et deux.

Donc ce que nous allons faire, c'est que nous allons simplement sauvegarder beats dot pop, ce qui était à l'index, et cela nous permettra de supprimer une entrée.

Celui-là est assez facile.

Nous allons mettre en évidence la fonctionnalité de quelques-uns de ceux-ci en même temps.

Une fois que nous les aurons en marche, d'accord, donc ensuite, faisons le bouton de chargement parce que celui-là est un peu délicat.

Et nous allons faire LF loading button dot collide, point, event dot pause, cette partie est facile.

La partie suivante est familière.

Si zéro est inférieur ou égal à index inférieur à la longueur de saved beats.

Ensuite, nous allons définir quelques-unes de nos variables égales aux informations que nous extrayons.

Donc beats va être égal à loaded info que nous passons en arrière, que je crois que nous venons d'appeler loaded info.

Oui.

Loaded info.

À zéro, donc la première chose était beats, loaded info zéro.

Et ensuite la deuxième chose était bpm.

Et donc ce sera loaded info à un.

Et ensuite le troisième était clicked, qui sera loaded info à deux.

Et nous allons définir l'index égal à 100.

Donc c'est comme un nombre irrélevant.

Et ensuite nous allons définir load menu égal à false juste comme nous l'avons fait lorsque le bouton de sauvegarde a été pressé, parce que votre travail est un peu terminé maintenant.

Et nous allons, cela devrait être tout ce que nous devons faire, je crois.

Donc allons-y et vérifions cela.

Maintenant, si nous avons toutes les fonctionnalités sur ce bouton de chargement, je pense que le bouton Fermer fonctionnait, je pense que nous sommes capables de cliquer là-dedans.

Donc en ce moment, en regardant notre écran, nous n'avons rien qui se passe.

Il n'y a rien de chargé si je charge ce generic rock beat in bien, je l'ai frappé Load beaten rien ne s'est passé.

Cela a fermé load beat.

Essayons Tom et clap.

D'accord, close, je peux le sentir mais pas de cigare.

Donc qu'est-ce qui se passe ? D'accord, je pense que la raison pour laquelle le bouton de chargement ne fonctionne pas est que nous devons, nous venons de faire LF loaded rectangle plus tôt, il doit être LF loaded rectangle dot collide point où avec event dot position.

Donc je suis vraiment surpris que l'indexation et la mise en surbrillance des rectangles fonctionnaient sans cela.

Mais cela devrait nous permettre de le charger.

Donc allons-y et vérifions load beat generic rock beat load beat.

Nous y voilà.

Et c'est vraiment génial.

Maintenant, essayons d'effacer le tableau.

C'est aussi génial.

Voyons si la suppression de l'un fonctionne.

Donc débarrassons-nous de Tom et clap parce que c'est un peu stupide de toute façon.

Donc allons-y et voyons si nous pouvons le supprimer.

Et il semble que nous nous en soyons débarrassés.

Maintenant, faisons quelque chose qui utilise plus de beats, et plus de beats par minute.

Donc faisons 24, est-ce une chose logique et faisons de ce nombre un nombre plus élevé comme 480 et voyons si cela fonctionne.

D'accord, donc nous sommes à beaucoup plus maintenant.

Et mettons simplement, je vais l'éteindre juste pour qu'il n'y ait pas trop de bruit pour vous, les gars.

Donc c'est huit.

C'est 1216 20.

Et ensuite pour ces quatre derniers, nous allons faire des crashes.

D'accord, et ensuite nous allons faire basse caisse claire.

En fait, nous allons vouloir les espacer un peu, parce que c'est un peu deux fois plus rapide qu'un beat rock normal.

Donc nous allons faire basse basse caisse claire.

Prenez une pause et ensuite nous allons faire basse basse, caisse claire tech pause, basse, basse caisse claire, et ensuite nous allons faire Clap, clap, clap à la fin.

Et nous allons le faire quatre fois à la fin.

Voyons à quoi ressemble le son quatre fois parce que nous sommes hardcore.

D'accord, donc je vais sauvegarder ce beef.

Je vais simplement l'appeler out.

Vous êtes ennuyé CBT donc cela ne fonctionne pas.

Maintenant.

Nous devons déterminer pourquoi nos boutons CBT ne fonctionnent pas.

Qu'avons-nous fait pour gâcher le reste de ce collide point ? Pause.

Je pense que nous ne voulons pas que tout cela soit des LFS parce que techniquement ils sont aux mêmes endroits.

Voyons si cela le résout.

Je pense que c'est ça.

causant des ennuis.

Vérifions cela.

Load beat entry rectangles ne trouve pas quelque chose d'étrange qui se passe.

Load beat nous devons vérifier pourquoi entry rectangle n'est pas défini.

Il vient de Save Menu.

Oh, eh bien, oui, entry rectangle ne va pas être défini.

Parce que si Save menu n'est pas vrai, alors il n'y a pas de rect.

Donc descendons aux rectangles comme celui-ci.

Et mettons simplement quelque chose ici.

C'est si Save menu.

Et ensuite nous allons mettre tout cela à l'intérieur.

Et je pense que nous allons vouloir la même chose pour ces trois, parce qu'ils sont seulement en chargement.

Donc nous allons dire si load menu.

Donc nous devons distinguer que nous ne voulons pas vérifier quoi que ce soit avec ces trois boutons, si ce n'est pas vrai, et ensuite espérons que cela le résoudra.

Donc si nous chargeons dans saving button n'est pas défini.

Mais pourquoi vous en souciez-vous ? Je pensais que je vous avais vérifié pour que vous ne vous en souciez pas.

Oh, nous voulons que tout cela soit à l'intérieur du même si Save menu.

Nous y voilà.

Essayons cela load beat Tom et clap.

Le voici.

Le Beat load in generic rock beat chargeons-le.

Oui, c'est hardcore.

D'accord, faisons-le simplement 12.

Et faisons quelque chose de stupide.

Je ne sais pas, cela n'a pas d'importance.

Essayons de sauvegarder cela comme un beat plus long.

Sauvegardons-le.

Voyons si nous pouvons charger dans le beat plus long.

Oui, je vais l'effacer.

Je vais charger le generic rock beat, charger le generic rock beat.

D'accord.

Je vais l'effacer.

Et je vais voir si je peux charger le beat plus long.

Et il le fait à 12.

D'accord.

Donc nous avons la capacité de désactiver des canaux individuels, nous avons la capacité de jouer et de mettre en pause, nous avons la capacité d'éditer pendant qu'un beat est actif ou inactif.

Nous avons la capacité de changer le nombre de beats dans la boucle, nous avons la capacité de sauvegarder des beats, nous avons la capacité de charger des beats, nous avons la capacité d'effacer le tableau.

C'est une application vraiment cool.

J'ai eu beaucoup de plaisir à la construire.

Évidemment, c'est un tutoriel difficile.

Je sais que cela a pris beaucoup de temps.

Donc si vous avez tenu jusqu'au bout.

J'espère que vous l'appréciez.

Si vous avez des questions sur des choses que nous n'avons pas couvertes ou que vous aimeriez voir approfondies, ou que vous avez essayé cela vous-même et que vous rencontrez des problèmes, faites-le moi savoir dans les commentaires ci-dessous.

Je vous répondrai dès que possible.

J'espère que vous l'avez apprécié.

Si c'est le cas, laissez un like sur la vidéo, abonnez-vous à ma chaîne.

Cela m'aide beaucoup.

Et je poste beaucoup de contenu génial comme celui-ci chaque semaine.

Donc sans plus tarder, bonne chance avec vos projets et merci d'avoir regardé.

Prenez soin de vous jusqu'à la prochaine fois, au revoir.