---
title: Cours accéléré sur Unreal Engine 5 avec Blueprint
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-02-03T18:38:19.000Z'
originalURL: https://freecodecamp.org/news/unreal-engine-5-crash-course-with-blueprint
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/unrealengine.png
tags:
- name: unreal-engine
  slug: unreal-engine
- name: youtube
  slug: youtube
seo_title: Cours accéléré sur Unreal Engine 5 avec Blueprint
seo_desc: 'Unreal Engine is one of the most popular game engines in use today. It
  can be helpful to learn if you are interested in 3D or 2D game development.

  We just published an Unreal Engine 5 crash course on the freeCodeCamp.org YouTube
  channel. Varnos Games...'
---

Unreal Engine est l'un des moteurs de jeu les plus populaires utilisés aujourd'hui. Il peut être utile de l'apprendre si vous êtes intéressé par le développement de jeux 3D ou 2D.

Nous venons de publier un cours accéléré sur Unreal Engine 5 sur la chaîne YouTube freeCodeCamp.org. Varnos Games a créé ce cours.

Vous apprendrez à créer un jeu en utilisant le système de script visuel Blueprint. Blueprint est un système de script de gameplay complet basé sur le concept d'utilisation d'une interface basée sur des nœuds pour créer des éléments de gameplay depuis l'éditeur Unreal.

Ce cours est destiné aux débutants absolus. Vous allez créer un jeu 3D où les joueurs contrôlent un robot qui doit collecter des batteries dispersées dans le niveau.

Voici toutes les sections couvertes dans ce cours :

* Blueprints dans Unreal Engine
* Bases d'Unreal Engine 5
* UI/UX
* Événements de victoire/défaite
* Conception de niveau de base

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=xl5fqr-CpTY) (2 heures de visionnage).

%[https://www.youtube.com/watch?v=xl5fqr-CpTY]

### Transcription

(autogénérée)

Dans ce cours de développement de jeux, Varnos Games vous apprendra à construire des jeux avec Unreal Engine 5, vous apprendrez également à utiliser le système de script visuel Blueprint qui simplifie la création d'éléments de gameplay.

Hey, les gars, merci beaucoup de vérifier ce cours.

Ce sera un cours très, très débutant sur Unreal Engine 5, uniquement sur les blueprints, nous allons faire un jeu simple appelé Battery Man.

Donc, si je joue à ce jeu, ce qui va se passer, c'est que j'ai quelques batteries présentes partout dans la scène, je dois collecter ces batteries ici.

Et une fois que c'est fait, je vais soit au nouveau niveau, soit je gagne le jeu.

Donc ici, c'est mon deuxième niveau.

Et si je collecte ces batteries, j'ai mon événement condition.

Et j'ai toujours une condition de défaite aussi.

Donc si j'attends, si je ne collecte aucune de ces batteries ici, et que j'attends cinq secondes, je perds le jeu, je peux quitter si je veux.

Et si je peux réessayer, nous avons évidemment encore beaucoup à faire.

Donc nous allons passer en revue tout dans ce jeu, y compris la validation de l'UI, en regardant les conditions et les émissions.

Nous codons tout à partir de zéro, nous utilisons le modèle Third Person, mais nous n'utilisons aucun de leurs mouvements intégrés, nous allons créer notre propre personnage, ajouter nos propres fonctionnalités à ce personnage.

Donc ce sera un jeu que vous aurez.

Hey, les gars, et bienvenue.

Maintenant, nous allons jeter un coup d'œil à Unreal Engine 5 et essayer de créer notre propre projet.

Donc ce que vous devez faire est d'ouvrir votre lanceur Epic Games.

Et le lanceur Epic Games est essentiellement un portail vers Unreal Engine et son marketplace.

Donc si je regarde le marketplace ici.

Donc le marketplace a essentiellement tous ces différents actifs de haute qualité que je peux utiliser.

Et une chose que j'aime dans le marketplace, c'est qu'il a quelque chose appelé le "free for the month", où il choisit cinq actifs payants du magasin d'actifs du marketplace.

Et il fournit ces actifs aux utilisateurs d'Unreal Engine absolument gratuitement.

Donc c'est une fonctionnalité incroyable.

Et c'est pourquoi j'aime le marketplace d'Unreal Engine.

Il a beaucoup de différents actifs de haute qualité, et même Epic Games, la plupart de son contenu est complètement gratuit et vous pouvez l'utiliser dans votre jeu.

Donc essayez de consulter le marketplace et utilisez-le dans votre jeu.

Ce n'est pas de la triche, c'est en fait une chose incroyable que de savoir comment utiliser les actifs des autres dans votre jeu, car c'est ainsi que fonctionne réellement le développement de jeux.

Essayons de voir comment installer Unreal Engine 5.

Maintenant, si j'ouvre le lanceur de jeux et que j'ouvre cette partie cinq ici, il a mon early access, il dit Unreal Engine 5 early access.

Maintenant, Unreal Engine 5 n'est pas complet, c'est pourquoi il dit toujours qu'il est en early access.

Mais je peux télécharger mon early access à partir d'ici.

Et je peux aussi obtenir le projet d'exemple qu'ils ont montré dans la vidéo de présentation d'Unreal Engine 5, ce qui est incroyable.

Mais une fois que vous avez terminé l'installation du fichier Unreal Engine, si vous allez dans votre bibliothèque, vous verrez votre éditeur Unreal Engine 5 ici et je peux l'ouvrir.

Et ici.

Si vous faites défiler jusqu'en bas, si vous allez à Wall, vous avez tous les actifs que vous avez achetés ou revendiqués, j'ai tous ces actifs, tous ces actifs sont gratuits et ils sont incroyables.

Donc essayez de consulter les actifs, peut-être que vous aimerez quelque chose et que vous les utiliserez.

En tout cas, je peux aller ici et appuyer sur lancer.

Et si cela prend un certain temps, ne vous inquiétez pas, j'ai ma version Android 5 installée sur mon HDD juste à cause de sa taille.

Habituellement, j'ai le moteur sur mon HDD et ensuite sur mon SSD, c'est là que j'ai tous mes projets sauvegardés.

Donc vous pouvez faire cela, vous pouvez avoir la même approche ou vous pouvez faire quelque chose de différent, c'est complètement à vous.

Mais c'est généralement ce que je fais.

Cela prend un certain temps pour ouvrir Unreal Engine pour moi, essentiellement parce que je veux dire, premièrement, je suis en train d'enregistrer et deuxièmement, parce que pour Unreal Engine, vous avez besoin de spécifications assez décentes, j'ai des spécifications moyennes par exemple, vous pouvez voir que j'ai un CPU à six cœurs et de la mémoire, en ce qui concerne la mémoire.

Si vous essayez de faire un jeu en utilisant Unreal Engine, assurez-vous d'avoir au moins 16 Go de RAM.

N'essayez pas de créer un jeu avec huit Go, cela ne va pas bien fonctionner pour vous, surtout si c'est un jeu à grande échelle.

Et assurez-vous d'avoir une bonne carte graphique.

J'ai deux Go de RAM, donc je peux à peine passer à travers cela.

Mais si vous essayez d'acheter un nouvel ordinateur portable ou un nouvel ordinateur juste pour le développement de jeux, assurez-vous d'avoir un bon CPU, qui est au moins six cœurs ou plus de six cœurs.

Il utilise beaucoup de puissance CPU.

Donc si je vais aux processus ici, vous pouvez voir qu'Unreal Engine utilise mon CPU comme un fou.

Et si je vais à mes performances à nouveau, mémoire, assurez-vous d'avoir au moins 16 Go de RAM, surtout sur le moteur cinq, vous ne pourrez pas obtenir quand je le jure.

Mais en tout cas, allons aux jeux.

Mais nous avons beaucoup de ces modèles ici.

Donc si vous voulez créer un prototype vraiment rapide, le meilleur aspect d'Unreal Engine est que vous pouvez créer des prototypes vraiment facilement.

Donc si je veux créer un prototype à la première personne, je peux, au lieu de créer le mouvement, le mouvement de projectile, tout à partir de zéro, je peux juste utiliser le modèle ici, et il va le créer automatiquement pour moi.

Donc j'ai ma partie tir, mon clavier, mon joystick, tous intégrés, donc je n'ai pas à les créer à partir de zéro.

Maintenant, cela est très, très utile lorsqu'il s'agit de game jams, nécessairement des game jams ou des compétitions, où vous avez un jour ou deux jours pour créer un jeu.

Et pour ceux-ci, c'est très, très utile.

Donc vous pouvez voir que j'ai beaucoup de ces différents projets, je vais utiliser le troisième personnage, sauf que nous allons créer les animations, le jeu, la logique de mouvement, tout à partir de zéro.

Donc c'est ce que je vais utiliser le troisième personnage et la raison pour laquelle j'utilise le troisième personnage.

Le projet Third Person et non un projet vide est parce que j'ai beaucoup d'animations fournies par Unreal Engine.

Et j'ai besoin de ces animations dans mon jeu, je ne veux pas faire mes animations à partir de zéro, ce qui est bien, je vais utiliser le projet Third Person.

Maintenant, sous le patient de qualité, je vais utiliser le mien pour le mettre à l'échelle, je vais activer le contenu statique, le contenu statique est essentiellement un ensemble d'actifs qu'Unreal Engine donne gratuitement comme des textures, des matériaux, des particules, etc.

Sous le nom du projet, assurez-vous qu'il n'y a pas de blueprint, pas de C++, il n'y a pas de cours C++, le prochain cours que je vais publier, ce sera un cours C++ du même jeu.

En tout cas, je vais nommer cela Batman et créer le projet, cela peut prendre un certain temps, surtout si c'est votre première fois, cela peut prendre un certain temps pour moi, pas beaucoup.

Mais lorsqu'il compile les shaders, c'est là que cela prend très longtemps.

Donc si vous avez un projet qui a beaucoup de logique de gameplay et d'actifs intégrés, alors cela va prendre très, très longtemps, surtout parce qu'il doit compiler les shaders.

D'accord, maintenant que c'est ouvert, vous pouvez voir que nous avons cette scène et tout le monde ouvre la scène du troisième personnage.

C'est la scène par défaut ici, j'ai les sols, il y a beaucoup de cubes, le personnage, blah, blah, blah.

Commençons à passer en revue tous ceux-ci un par un.

Maintenant, j'ai l'onglet placer des acteurs où j'ai différentes confidences ou acteurs que je peux ajouter à ma scène, qu'est-ce qu'un acteur, un acteur est un objet qui peut être placé dans le monde.

C'est un acteur vide.

Et je peux ensuite ajouter de la logique à cet acteur ici.

Maintenant, comment cela fonctionne est que tout ce qui peut être placé sur la scène est un acteur.

Donc la boîte de déclenchement est essentiellement un acteur.

Regardez cela de cette façon.

Une Tesla Model S, par exemple, est une voiture.

C'est une voiture électrique, mais toujours une voiture, elle dérive d'une voiture.

C'est ainsi que cela fonctionne ici.

L'acteur vide est universel, tout ce qui peut être placé ici est un acteur.

Donc c'est un acteur, c'est un acteur, mais nous avons différents types d'acteurs.

Donc à partir d'un acteur, quelque chose appelé upon est créé, upon est un acteur qui peut être traité, traité, ce qui signifie que vous pouvez ajouter un acteur d'entrée à ce point ici, par exemple, vous pouvez déplacer le point comme un véhicule, etc.

Ou le personnage est essentiellement un upon qui se déplace.

Donc c'est ainsi que la hiérarchie fonctionne.

Vous avez une force active, sous cet acteur, nous avons un point donc le point hérite d'un acteur, et le personnage hérite d'un point et a essentiellement comme un maillage de collision, etc.

Parlons de la collision Shelby, sélectionnez ce personnage à la troisième personne et dans le World Outliner, vous pouvez voir que ce personnage à la troisième personne a été sélectionné.

Et sous les paramètres du monde, j'ai mon mode de jeu override.

Nous allons examiner tout cela plus tard.

Mais allons au panneau Détails.

Sous ce panneau, j'ai mon composant capsule, qui est essentiellement une collision.

La façon dont la collision fonctionne dans les jeux est que vous avez une capsule, vous n'avez pas toutes ces collisions complexes, comme vous connaissez la forme exacte du personnage, cela ne va pas se produire.

C'est très, très gourmand en ressources.

Nous utilisons des collisions simples dans nos jeux.

Et ce que les permissions font, c'est qu'elles s'assurent qu'il ne traverse pas les escaliers ici, sauf si vous voulez créer un fantôme.

Je peux monter les escaliers, je peux sauter, la collision solide dit essentiellement d'accord, cet objet est solide, mais cela ne peut pas être, vous savez, la collision ne peut pas traverser le mur, elle peut définitivement le faire, vous avez différents préréglages.

Par exemple, je peux sauvegarder, je peux définir ma collision de telle manière que je puisse me déplacer à travers les escaliers, mais je ne peux pas me déplacer à travers un plancher, je peux faire cela, je peux définitivement le faire, tout ce que vous avez à faire est de sélectionner le composant capsule.

Et une fois que vous avez sélectionné le composant capsule, et dans cette partie ici, nous avons différents autres, nous avons différents attributs, essentiellement comme la transformation, la forme, la navigation, tout cela.

Maintenant, la transformation est universelle pour chaque moteur de jeu, nous avons l'emplacement, la rotation et l'échelle.

Le rouge est pour l'axe x, y est pour eux dans le vert est pour l'axe Y et le bleu pour l'axe Zed.

Vous pouvez également voir ces flèches ici.

Si je change cette flèche rouge, si je tiens cette flèche rouge et que je bouge ma souris, vous pouvez voir que mon axe x est en train de changer, de même pour mon Y et mon Zed, je peux également déplacer deux axes en même temps.

Par exemple, mon Zed, oops, d'accord, c'est assez bien.

Je peux déplacer mon Zed et mes axes bi en même temps.

Vraiment, d'accord, je sais ce que je vais déplacer mon x et mon y, juste parce que c'est simple, vous pouvez voir que mes valeurs, les valeurs correspondantes changent également.

Donc je suis que lorsque vous essayez de placer des objets, c'est-à-dire que vous devrez comprendre comment changer toutes ces valeurs.

Maintenant, je peux également changer la rotation, si j'appuie sur E, je peux changer ma rotation.

Donc vous pouvez voir que je peux monter et descendre, je peux changer, par exemple.

D'accord, revenons.

Si je change la partie verte ici, vous pouvez les voir changer en rotation par rapport à mon axe y, de même pour le bleu et le rouge ne perd pas de temps.

Et l'échelle est évidemment la taille du personnage, je vais la remettre à zéro, je ne veux pas d'un personnage énorme.

D'accord, maintenant le mien est censé être un non zéro, s'il est zéro, il ne va pas avoir la dimension x du tout, il va être un deux, il va être un objet à deux dimensions, composant capsule si j'ai quelque chose appelé mobilité, et cela est présent pour chaque objet.

Donc par exemple, si je sélectionne mon réseau, le Mac, l'étoile de jeu, cela définit essentiellement où mon joueur devrait commencer, cela est pour le réseau SS joueur commence.

Donc c'est pour le multijoueur.

Donc cette capsule, probablement sous la compagnie capsule, si j'ai si j'ai quelque chose sur la mobilité, je peux essentiellement dire si mon personnage devrait être statique, mobile ou stationnaire.

Si je suis si ma personne obtient une entrée et doit se déplacer dans l'un de ces accès, ou même tourner, je dois m'assurer que cela est mobile.

Ici, j'ai mes animations, nous allons passer en revue tout cela plus tard, en recréant cela à partir de zéro, j'ai mon maillage, je peux sélectionner si je veux simuler la physique ou non.

Et cela donne une physique réaliste, je peux activer la gravité ou désactiver la gravité.

En fait, vous savez quoi, essayez de changer toutes ces valeurs et essayez de voir ce que cela fait.

C'est la meilleure façon d'apprendre, explorez et essayez de changer toutes ces valeurs.

Espérons que vous ne casserez pas le moteur.

J'ai ma compétence capsule.

Donc j'ai essentiellement différentes compétences attachées à mon personnage.

Et ces compétences ont différents attributs comme, par exemple, mes cheveux ont différents attributs, mes jambes ont différents attributs, mais en tant que personne entière.

Donc c'est essentiellement ainsi que cela fonctionne.

En tant que tout, c'est un personnage à la troisième personne et a différents composants attachés à celui-ci, un marteau, une caméra, etc.

Maintenant, vous pouvez voir qu'il est indiqué qu'il est hérité ici, cela signifie que si je survole cela, il est indiqué que mes classes parentales sont des personnages, que veux-je dire par héritage, cela signifie qu'il s'agit en fait d'un concept de programmation.

Et ce que cela signifie, c'est que la classe parente a un ensemble d'attributs que j'hérite sur mon enfant, c'est ce personnage à la troisième personne, ce n'est pas cela, cela hérite de la classe de personnage.

Donc vous pouvez voir la classe de stylo, il est indiqué la classe de personnage et la classe de personnage a le composant capsule, le maillage, etc.

Donc je n'ai pas à, si je crée un enfant de ce personnage à la troisième personne, je veux dire l'enfant de cette classe de personnage et avoir tous les attributs de ce personnage.

Pensez à cela comme vous pensez à vos parents.

Si vous avez, si vos parents ont, disons, des yeux bruns, les chances que vous ayez des yeux bleus sont assez faibles.

Donc vous héritez en quelque sorte des gènes de vos parents, et cela se transmet à l'enfant.

C'est ainsi que fonctionne la programmation aussi.

Et c'est pourquoi c'est si beau.

Maintenant, en ce qui concerne le navigateur de contenu, j'ai mes blueprints et avec les boîtes de contenu utilisées pour naviguer à travers vos fichiers de jeu, et c'est à peu près à quoi cela sert.

Et j'ai différents dossiers.

Cela a été créé automatiquement par Unreal Engine en raison du modèle que j'ai choisi.

Donc si je vais aux blueprints, j'ai un personnage à la troisième personne.

Avant cela, familiarisons-nous d'abord avec la partie Place Actors Part Two, si je vais à, j'ai différents onglets ici sous Place Actors, j'ai ma lumière directionnelle, ma lumière ponctuelle ici, lumière sportive, tout cela comme dans la vraie vie, je peux, je peux faire glisser cette valeur dans la scène, et elle a automatiquement sélectionné quel que soit l'objet que j'ai ajouté, je peux changer toutes ces valeurs, par exemple, je peux changer la couleur de la lumière en bleu, rouge, etc., je peux changer mon intensité, je peux la rendre absolument brillante ou très, très sombre.

Donc le C D signifie CAD, CAD, faites ce que vous voulez, d'accord, je ne sais pas, j'ai commencé la physique.

Mais en tout cas, c'est à quoi sert l'intensité pour ma lumière d'atténuation, ce sont tous des concepts de lumière physique.

Donc si vous aimez vraiment la physique, vous pourriez probablement être capable de reconnaître toutes ces différentes variables ici.

Malheureusement, si vous voulez devenir vraiment bon en développement de jeux, un peu de physique, un peu de mathématiques, c'est important, parce que, vous savez, la programmation est essentiellement juste des mathématiques et de la physique, mais dans une facture très, très pratique.

Donc vous n'avez pas besoin de connaître les mathématiques, la physique et tout cela.

Mais cela aide beaucoup.

Vous pouvez comprendre les concepts beaucoup mieux, surtout lorsque vous devez déboguer quelque chose ou ajouter une fonctionnalité complètement nouvelle.

En tout cas, ne perdons plus de temps.

Et cela crée un nouveau niveau afin que nous puissions ajouter nos propres personnages, je veux dire, nos propres objets à la scène.

Le fait est que si je clique sur mon fichier, je peux aller au nouveau niveau, je vais créer un niveau par défaut ici, et il va automatiquement me demander de sauvegarder ce modèle ici.

Maintenant, si j'appuie sur Ctrl S, je peux sauvegarder cela dans mon dossier, je vais créer comme cliquer ici créer un nouveau dossier appelé scènes.

Et je vais appeler ce niveau un.

En fait, cela devrait s'appeler niveaux, je faisais cela dans Unity.

C'est censé être des niveaux dans Unity deux, trois politiques.

Nous y voilà.

D'accord, je vais supprimer le sol et le Player Start qu'ils ont effectivement mis, nous allons ajouter tout cela.

J'ai, évidemment, quelque chose appelé brouillard atmosphérique, qui a beaucoup d'influence sur la lumière.

Mais je peux aussi ajouter quelque chose appelé le brouillard exponentiel de hauteur avec, qui ajoute beaucoup de profondeur à la carte.

En fait, essayez d'explorer ici, essayez d'ajouter différents objets à votre scène, comme je l'ai dit, mais nous allons créer quelque chose appelé un paysage ici.

Donc j'ai quelque chose appelé l'onglet paysage.

Si je clique sur cela, vous avez quelque chose, d'accord.

Tous ces clients que vous voyez ici, cela s'appelle généralement des gizmos dans le développement de jeux.

Cela s'applique à tous les moteurs de jeu, ces lignes, l'appel de base gizmos, et ils sont essentiellement des contours de tout objet que vous avez sélectionné.

La raison pour laquelle je peins le paysage et n'ajoute pas simplement un cube ici et le met à l'échelle est parce qu'il est très, très bien optimisé, les paysages sont optimisés pour des niveaux énormes.

Et je vais en fait vous montrer pourquoi.

Ici, si je vais à mon onglet paysage, je peux changer beaucoup de valeurs différentes.

Mais tout ce qui m'inquiète, c'est la taille de ma section, je vais faire sept à sept cordes.

Donc vous pouvez voir qu'il est sept ici et sept ici, je suppose 1234 Oui, nous y voilà.

Et je vais créer cela.

Maintenant, la raison pour laquelle je dis que cela est très bien optimisé est, premièrement, je peux changer la profondeur de ce paysage et vous verrez dans un instant.

Oh, j'ai oublié d'ajouter le matériau, mais non, probablement nous pouvons l'ajouter plus tard.

Cela peut prendre un certain temps, surtout si c'est la première fois que vous configurez tout.

Mais une fois que vous avez créé cela, attendez un peu, d'accord, vous pouvez maintenant voir ce grand curseur blanc ici.

Changeons la taille du pinceau pour quelque chose de petit.

Vous pouvez voir que je l'ai sélectionné, il a automatiquement sélectionné la partie sculpture et je peux essentiellement ajouter de la profondeur à cette carte.

Par exemple, je peux créer des montagnes ici et si je veux l'aplatir, je peux sélectionner la partie aplatie et ensuite lisser complètement cela et l'aplatir pour faire l'inverse de En fait non.

Maintenant, cela sélectionne automatiquement la partie sculpture ici.

Je peux essentiellement créer des montagnes, etc.

Lisseur où il est une surface assez montante est plus que assis.

Et vous pouvez voir que les ombres commencent à disparaître.

Et c'est un peu l'inverse du mode sculpture.

Aplatir rend le terrain aussi plat que possible.

Donc si je veux, par exemple, ajouter une rivière ici, je ne sais pas si vous êtes au courant, mais Unreal Engine a ce système d'eau incroyable.

Donc si je veux ajouter un composant, pas une rivière, cela n'a pas de sens, si je veux ajouter un point ici, je peux facilement le faire.

Mais la raison pour laquelle j'utilise le paysage est parce que laissez-moi vous montrer quelque chose.

Allons-y jusqu'au bout.

Découpons cette partie ici.

Et laissez-moi changer la force de l'outil à, par exemple, 0,4.

Donc c'est plus rapide, vous pouvez voir qu'il ne rend pas les graphiques ici, parce qu'il n'a pas à, je veux dire, pourquoi voudrais-je rendre tous mes graphiques, la profondeur, la hauteur complète de ces graphiques ici, quand le joueur ne va pas les voir ? Exact ? Tout est une question d'optimisation.

Maintenant, c'est aussi l'une des raisons pour lesquelles vous avez vu dans de nombreux jeux, si vous avez des problèmes de collision, par exemple, si je n'ai pas de collision ici, et que le joueur tombe à travers la carte, si vous continuez à tomber, vous pouvez en fait remarquer que vous ne pourrez pas voir le haut du niveau.

C'est à cause de la partie optimisation de ce paysage ou de ce qu'ils utilisent.

Cela s'applique à beaucoup de moteurs de jeu différents.

C'était très, très courant dans Grand Theft Auto, San Andreas, et aussi Cyberpunk.

Mais en tout cas, c'est à peu près pourquoi j'utilise le paysage.

Donc ici et aussi parce que je peux utiliser la fonction de sculpture ici, laissez-moi juste, je vais ajouter un peu de profondeur, je vais faire en sorte que cela ressemble à un vrai sol pour qu'il ne soit pas complètement plat, je trouve cela vraiment ennuyeux, je déteste quand les objets sont complètement plats.

Donc je vais juste faire cela.

Et donc, vous pouvez voir qu'il édite quelque chose appelé la carte de hauteur, la carte de hauteur ajoute essentiellement de la profondeur, dit à la carte où et comment elle est haute.

Le niveau est, par exemple, cette coordonnée, j'ai comme une montagne de quelque sorte.

Et nous ici, je n'ai pas.

Donc c'est à peu près ce qu'il fait, nous sommes ici.

Maintenant, si je veux revenir à mon mode SELECT, je peux simplement cliquer sur mon mode select ici.

Et c'est à peu près tout.

Donc si je sélectionne mon paysage, je peux changer beaucoup de ces valeurs, ce que je vais faire, c'est que je vais en fait recréer cela, parce que je ne vous ai pas montré comment ajouter un matériau.

Donc quand vous allez dans votre mode paysage, vous pouvez voir cette partie matériau ici, essayez de sélectionner le matériau du sol.

Et recréons-le.

Et ce sera 77.

Donc c'est ainsi que vous ajoutez du matériau.

Et encore une fois, je vais ajouter un peu de profondeur ici, juste frotter le son et assurez-vous que vous avez cliqué sur votre souris et juste pour envelopper cela.

D'accord, c'est génial.

Maintenant, ils ont créé le paysage.

Et aussi une autre bonne partie de ce mode paysage est qu'il met à l'échelle la texture automatiquement pour vous afin qu'elle ne soit pas juste, vous savez, une partie de la texture, elle met à l'échelle beaucoup.

Donc j'aime vraiment, vraiment cela à propos du paysage.

Donc essayez d'ajouter quelques lumières sur votre paysage, essayez d'expérimenter par vous-même pour changer la lumière, la couleur de la lumière ou l'intensité, ce que vous voulez.

Et cela de moins en moins, je pense autour du brouillard exponentiel de hauteur.

Si je vais tout en haut, je pourrais changer la densité du brouillard pour rendre cela vraiment brumeux.

Je veux donner à cela une sorte d'apparence martienne, je vais la rendre rouge.

Et oui, cela a l'air vraiment bien.

D'accord, maintenant, passons à la partie codage.

Mais ce n'est pas exactement du codage.

C'est ce qu'on appelle le blueprinting.

Et c'est le langage de script visuel d'Unreal Engine et je l'adore absolument.

Si vous allez dans le dossier Blueprints, vous pouvez voir le personnage à la troisième personne qui dit W tech.

Maintenant, rappelez-vous, cela ne signifie pas que vous pouvez complètement vous en sortir avec juste des blueprints.

Vous aurez besoin de C++ si vous faites un jeu complet et que vous le publiez.

Pourquoi, parce que les blueprints sont principalement destinés au prototypage et aux petites fonctionnalités.

Si vous essayez de faire un jeu multijoueur, par exemple, vous ne pouvez pas vous en sortir avec des blueprints parce que les blueprints ne sont pas exactement le langage de programmation le plus rapide.

C'est aussi un langage de programmation, mais il n'est pas rapide.

C++ est beaucoup plus rapide, c'est pourquoi nous allons créer le même jeu en C++ plus tard.

Mais c'est un cours différent.

Celui-ci ne sera que des blueprints comme je l'ai expliqué avant.

Cela peut sembler un peu confus pour vous, mais en fait, ce sont deux fenêtres différentes, et si je vais à mon viewport ici, je peux voir mon personnage à la troisième personne en action.

Et je peux voir ma collision, je peux voir toutes mes confidences ensemble, comme la caméra, le composant d'erreur, tout cela, essayons de jeter un coup d'œil à tous ceux-ci un par un, ils ont toujours jeté un coup d'œil au composant capsule, jetons un coup d'œil à la confiance de la flèche, cela pointe essentiellement vers les points vers l'avant de moi vers le vecteur avant, ou il pointe vers l'avant tout le temps.

Ils regardent le maillage, le maillage.

D'accord, donc maintenant nous avons deux types de maillage différents dans Unreal Engine, alors que le maillage statique, et l'un est dans le maillage squelettique, le maillage statique est utilisé pour des choses comme, par exemple, un cube, si je fais glisser ce cube ici, vous pouvez voir que j'ai un maillage statique.

C'est surtout parce que ce cube ne va probablement pas bouger et qu'il n'a pas d'animations supplémentaires.

Comme, je veux dire, quoi, je vais animer un cube, peut-être que je peux faire tomber cela, c'est un champion, je n'ai pas besoin d'un squelette, je n'ai pas besoin de quelque chose appelé un squelette pour cela.

Mais j'ai quelque chose appelé le maillage squelettique.

Et c'est le homologue complexe du maillage statique.

Un maillage squelettique est essentiellement un maillage avec quelque chose appelé un squelette, comment les animations sont créées est que vous avez quelque chose appelé un squelette et il est assigné à un maillage particulier.

Et vous avez le squelette est un os et un riddlin.

C'est presque comme le squelette humain ici.

Maintenant, comment les animations sont créées est que je prends un os spécifique, et je change les valeurs.

Par exemple, si je fais tourner cet os ici, active une animation, je veux dire cela pendant une seconde en giflant quelqu'un, mais c'est à peu près comment les animations sont créées.

Je manipule les valeurs de transformation de ces points ici, comme, d'accord, pas le majeur, peut-être l'index.

Et oui, nous y voilà, je peux faire cela.

Donc c'est à peu près ce que les animations, comment les animations sont créées.

Maintenant, vous pouvez créer des animations dans Unreal Engine, mais je vous suggère de, si vous voulez apprendre à faire des animations, il y a beaucoup de cours Blender en ligne, par Game Dev TV, ou en tout cas, il y a beaucoup de cours Blender différents en ligne, s'il vous plaît, jetez un coup d'œil.

C'est incroyable.

Mais c'est le squelette qu'Unreal nous fournit, j'ai quelque chose pour la caméra, boom.

Maintenant, si je survole, c'est le composant bras de ressort.

Et le composant bras de ressort.

Essentiellement, la raison pour laquelle nous n'ajoutons pas la caméra directement est que si j'ai un mur derrière, et si mon personnage se déplace derrière lui, si le personnage se déplace en arrière comme cela, d'accord, n'a pas déplacé la capsule, j'ai en fait déplacé le maillage, si je continue à reculer et que la caméra bouge avec lui, la caméra pourrait traverser le mur, je ne veux pas cela, je veux que ma caméra se déplace vers le haut comme le mur lorsque je m'approche du mur, ce à quoi Sprayground est utilisé, il s'assure que la caméra ne bouge pas à travers le vide.

Maintenant, la caméra de suivi est la caméra elle-même et si vous voulez changer la position, ajoutez plutôt changer les valeurs du décalage de la cible ici.

Donc cinq, Jésus comme peut-être 30, je veux dire 300, vous pouvez voir les déplacements par rapport à l'axe y.

Donc je fais cela, à tout moment.

Donc je vais, si je veux cela, je peux changer le décalage de la prise, et appuyer sur E pour changer la rotation comme cela.

Donc c'est la voie à suivre en ce qui concerne la création d'un système de caméra.

Et ils ont le mouvement du personnage.

C'est un composant intégré créé par et créé par Epic Games.

Et cela a essentiellement différents menus que vous pouvez manipuler, par exemple, les valeurs de mouvement, essayons de changer celles-ci si je cherche ma vitesse de marche ici, c'est en fait de chercher la vitesse de marche maximale.

Si je change cela en, disons, 350 ici.

Et si vous voulez que vos changements soient enregistrés, vous devez vous assurer d'appuyer sur le bouton compiler.

Et si j'appuie sur Alt P, vous pouvez voir que je marche plus lentement que d'habitude.

Donc je peux essentiellement manipuler toutes ces valeurs.

Et cela est encore, vous pouvez voir que c'est hérité.

Donc cela appartient à la classe de personnage.

Et cette classe de personnage a tous ces hérités, donc je peux lire n'importe lequel de ceux-ci.

Essayons de respecter les 600.

Mais en tout cas, cela n'a pas d'importance car nous créons notre propre personnage.

Le graphique d'événements est l'endroit où vous créez votre logique.

Donc tous ceux-ci sont appelés nœuds.

Et vous pouvez essentiellement glisser-déposer ces nœuds ici pour créer votre flux de code.

Ne vous inquiétez pas, cela est très confus.

Nous allons créer tout cela à partir de zéro.

D'accord, et oui, c'est à peu près tout pour le graphique d'événements.

Et si je vais à mon script de construction, cela se produit même avant le début du jeu.

Donc si je veux ajouter une fonctionnalité à mon moteur de jeu, je peux le faire dans le script de construction.

Dans mon graphique d'événements, j'ai mon bouton variables.

Jetons un coup d'œil aux graphiques, je peux obtenir différents graphiques.

Par exemple, je peux créer un nouveau graphique, juste un moment, si je veux garder cela très, très ordonné.

Mais nous ne allons pas faire cela, nous avons un script très simple, donc c'est bien.

Et nous avons quelque chose appelé variables, une variable est d'accord, je vais faire une variable, une variable est essentiellement quelque chose qui peut contenir une valeur.

Les variables peuvent être de différents types, flottants, entiers, entier 64, par double, jetons un coup d'œil à tous ceux-ci.

Un booléen contient une valeur vraie ou fausse, par le bit de serpent, l'entier est un nombre plus grand que le byte, entier 6464.

Le nombre de bits flottant est un nombre décimal.

Donc c'est comme 3,14 10,6 6,9.

Et double est un grand nombre à virgule flottante de 64 bits, comme 6,999.

Et essayez de continuer jusqu'à six bits de mémoire.

Un nom est un morceau de texte, ou une chaîne est essentiellement n'importe quelle valeur unique qui est entre guillemets.

Par exemple, cela pourrait être mon nom, ou le mot, le mot bonjour, ou la phrase Bonjour le monde, cela pourrait être une chaîne.

Un texte aussi, c'est un type différent de chaîne utilisé pour l'UI, etc.

Le nom est principalement utilisé pour les noms de scène, les noms de niveau, tout cela, le vecteur, un vecteur en physique est essentiellement une valeur qui a une magnitude et une direction.

Donc je peux dire, x se déplace à 10 à 10 mètres carré par seconde dans ma direction x.

Donc c'est un vecteur.

Et un vecteur se compose des valeurs X, Y et Zed, theta est pour la rotation, et il a également les valeurs X, Y et Zed qui sont transformées.

Nous l'avons déjà vu, c'est la rotation, l'emplacement de la rotation et l'échelle.

C'est universel pour chaque moteur de jeu.

Donc oui, ce sont les bases pour les blueprints.

Maintenant, passons à la création de notre propre personnage.

Donc je vais d'abord créer un nouveau dossier.

Et je vais appeler cela des blueprints personnalisés, car je vais différencier ceux créés par Epic Games et ceux que j'ai créés.

Et il est très important d'être organisé.

Maintenant.

Faites-moi confiance sur ce point, chaque développeur de jeux vous demandera d'être organisé et ils ne seront pas organisés eux-mêmes.

Cela arrive tout le temps.

Mais ce sont les meilleures pratiques, vous commencez tout juste à apprendre.

Essayez de garder votre projet aussi organisé que possible.

Maintenant, ici, j'ai mes icônes de bureau cachées, mais si je vous montrais votre politique, comment l'ancien prochain temps, assurez-vous de ne pas faire cette erreur, essayez d'organiser vos dossiers autant que possible.

Et les blueprints personnalisés, je vais créer une classe Blueprint, et cela va hériter de mon personnage.

Donc je vais avoir toutes les fonctionnalités que ce personnage fournit.

Par exemple, je peux me déplacer, je peux ajouter une entrée de code, j'ai la capacité de le faire.

Mais je dois m'assurer que je dis à mon personnage de bouger, c'est comme vous, vous avez l'intelligence pour faire un jeu.

Mais vous devez apprendre à faire un jeu, c'est à peu près ce que nous faisons ici.

Donc avoir un personnage, je peux le sélectionner.

Et la convention de nommage est généralement DT underscore le nom de quelqu'un appelle cela battery man.

Et si je l'ouvre, je n'ai pas le maillage.

Donc si je vais à mon personnage à la troisième personne et que j'essaie de le comparer à toutes ces parties héritées, je les ai sur mon VPN disco Batchi.

Homme, je n'ai pas le maillage parce que le maillage n'est pas, je veux dire, je n'ai pas la caméra et le composant de ressort parce que cela n'est pas hérité.

Donc copions cela et ajoutons-les à notre personnage ici.

Oh, en fait, il semble que oui, nous pouvons probablement les copier et les coller ici.

Donc j'ai déjà ma caméra ajoutée ou vous pouvez simplement dire Ajouter une caméra et ajouter un composant de ressort, etc.

D'accord, j'ai ma caméra, Compiler et Sauvegarder et assignons notre maillage.

Donc si je vais à mon maillage, je peux aller à mon maillage squelettique.

J'en ai seulement deux.

J'ai la femme et l'homme.

Je vais utiliser le mannequin masculin.

Ils vont amener cela tout en bas de 80 unités.

En fait, faisons 90, en fait non, je pense que je pense que cela serait bien ici et appuyer sur E et déplacer cela de 90 degrés.

Et encore, c'est l'axe Zed, compagnon sauvegarder ce style.

Pour exécuter le jeu, vous remarquerez que j'ai toujours mon personnage à la troisième personne.

Et si vous êtes toujours confus quant au personnage que j'utilise, vous pouvez injecter à partir de ce personnage.

Qu'est-ce que cela signifie ? fonction, appuyez simplement sur f8 dans votre clavier.

Et puis vous pouvez, le jeu est toujours en cours d'exécution, mais je peux essentiellement déboguer la scène ici.

Maintenant, si vous sélectionnez votre personnage à la troisième personne, vous pouvez voir que j'utilise toujours le premier personnage en métal, mon joueur depuis le pion.

Et cela soulève une question.

Comment le moteur de jeu sait-il, sans ajouter de fonctionnalité, comment sait-il que j'ajoute, je veux que mon personnage à la troisième personne apparaisse ? Cela n'a même pas de sens, n'est-ce pas ? La raison est que j'ai quelque chose appelé les modes de jeu.

Si vous allez dans Modifier les paramètres du projet, jetons un coup d'œil à la partie cartes et modes.

Ici, j'ai quelque chose appelé Game Mode, le jeu définirait essentiellement des valeurs par défaut pour chaque scène.

Donc je peux dire, peu importe quelle scène je crée, je veux toujours que mon personnage à la troisième personne apparaisse.

Et dans cette scène, je peux dire par exemple, si c'est le menu principal, je peux avoir un mode de jeu override, qui dit, d'accord, pour le menu principal, ne faites pas apparaître le personnage, car c'est bizarre.

Donc je vais juste avoir mon UI, etc., je ne veux pas que mon personnage réponde.

Donc c'est ainsi qu'Unreal Engine fonctionne.

Donc ici, sur mon mode de jeu par défaut, je vais changer cette valeur en BP underscore Batman.

Et maintenant, si j'appuie sur Alt P, je peux voir ici, mais évidemment, je n'ai aucune fonctionnalité.

La raison est que j'ai la capacité de prendre une entrée, mais je n'ai encore rien fait avec cette entrée.

Donc c'est ce que nous allons ajouter ici.

Si je vais à mon graphique d'événements, jetons un coup d'œil à tous ces événements ici, que nous n'avons pas vus auparavant.

Je vais supprimer ceux-ci.

D'accord, maintenant, l'événement claim, voyons ce que cela fait, l'événement play event, il exécute tout code qui y est attaché au début du jeu, donc un seul va être exécuté une fois et c'est lorsque vous commencez à jouer au jeu.

Même prendre, il est exécuté chaque seconde.

Et jetons un coup d'œil à un exemple.

Si je fais glisser cela ici, c'est ce qu'on appelle le nœud exec.

Et je peux le relâcher pour jouer pour placer un nouveau nœud.

Et je peux simplement sauvegarder la chaîne de caractères ici.

La façon dont cela fonctionne est que lorsque j'appelle begin play lorsque l'implémentation est appelée automatiquement et que le temps va imprimer la chaîne de caractères ici.

Et je vais simplement dire que cela peut jouer compiler, et jouer au jeu, Alt P.

Et vous pouvez voir que cela dit que cela est en train d'être joué.

Maintenant, je vais ajouter Player Start au style de jeu, ce qui définit essentiellement où mon joueur s'est arrêté, ma ventilation a arrêté le jeu.

Donc maintenant, je ne tombe pas de la carte.

Donc remarquez que cela est grand et joué.

Je vais maintenant appuyer sur Alt et cliquer sur ce bouton ici.

Et puis déplacer, déplacer cela en bas, et puis faire glisser le nœud de l'événement prendre ici.

Maintenant, cela peut être n'importe où.

Mais je viens de vous demander de l'amener en bas parce que je veux que cela soit net.

Donc Compiler et Sauvegarder sur dpi.

Et maintenant, vous pouvez voir que cela est imprimé chaque frame.

Maintenant, rappelez-vous, cela peut être différent pour chaque ordinateur.

Si mon jeu tourne à 60 images par seconde, cette fonction sera appelée 60 images par seconde.

Mais sur un autre ordinateur, disons que vous avez une RTX 13 3080.

Et votre jeu tourne à 160 images par seconde, 120 images par seconde, alors cette fonction sera appelée à 100 120 images par seconde.

C'est ainsi que la fonction tick fonctionne.

Pour les utilisateurs d'Unity.

C'est comme les fonctions start et update.

Très, très similaire.

Donc nous n'allons pas utiliser l'une de celles-ci car ce que nous allons faire, c'est dire si j'appuie sur ma touche W ou mon s ou mon A ou mon D, déplacez-moi, déplacez le personnage et si j'appuie, disons, sur mon bouton de la souris, imprimez quelque chose, c'est ce que nous allons dire ici.

Donc si je minimise cette fenêtre, allez dans Modifier les paramètres du projet.

J'ai ma partie d'entrée ici.

J'ai deux types de liaisons ici.

L'une est la liaison d'action, le mappage d'action et l'autre est le mappage d'axe, les mappages d'action sont assez explicites, j'ai juste ma barre d'espace ici.

Je ne vais pas me donner la peine d'ajouter une banque, notre jeu n'a pas de mécanismes de saut ici, donc nous n'allons pas ajouter de saut, mais je vais en fait vous montrer comment faire sauter votre joueur.

Donc cela signifie essentiellement que si je vais, si je vais essentiellement, si je retourne à mon blueprint, comme et à l'événement de saut.

Vous pouvez voir sous les événements d'action d'entrée, j'ai ce saut, et ce bouton, mon bouton de pression, mon bouton de saut, faites quelque chose, pressez.

Si je relâche mon sauteur, faites quelque chose, j'ai appuyé sur le bouton de saut.

Le bouton de saut est ma barre d'espace.

Et pour ma manette de jeu, c'est mon bouton face, pop, pop bottom.

Mais en tout cas, je vais nommer tous ceux-ci Unreal Engine, évidemment, il semble qu'il supporte beaucoup de consoles différentes, ce qui est génial.

Et mes mappages d'axes, cela devient un peu confus, je vais tout supprimer, je ne vais pas les utiliser à nouveau, parce que cela devient très confus pour les nouveaux développeurs.

Donc je vais faire plus de ceux-ci.

Maintenant, si j'appuie sur W, je veux retourner une valeur de un, ce qui signifie essentiellement aller de l'avant.

Si j'appuie sur S, je veux retourner une valeur de moins un.

Et si j'appuie sur A, je veux retourner une valeur de moins un, si j'appuie sur D, modérer la valeur plus un, pourquoi ? Parce que regardez l'axe.

Si vous allez de l'avant, c'est généralement positif.

Si je vais en arrière, c'est négatif.

Donc pour mon entrée de mouvement, je vais essentiellement dire ajouter un, deux, tant que j'appuie sur mon bouton W, ajouter un à mon entrée de mouvement.

Et si j'appuie sur A, cela va ajouter une valeur de, disons, moins un à cette direction particulière.

Donc pourquoi est-ce que c'est moins un, eh bien, regardez l'axe X.

Si vous regardez l'axe X, la partie gauche est moins un, la partie droite est censée être un.

Donc c'est essentiellement ainsi que fonctionne le système de coordonnées ici.

Taux de rotation, ce que nous allons faire ici, c'est que je vais en fait supprimer notre taux de rotation et notre taux de recherche ici.

Et ce que nous allons faire, c'est, au lieu de cela, nous allons appeler cela look tight, et puis nous appellerons cela look up, look up est votre direction de souris, il retourne une valeur allant de moins un à quatre look right, si je déplace ma souris dans ma direction x, il retourne une valeur allant de bots à un, voyons en fait ce que cela fait.

Maintenant, dans mon action d'entrée, si j'appuie sur cela, je veux imprimer que je saute.

Donc je peux simplement dire contrôle-moi, compile, sauvegarde cela, retourne en arrière, je peux supprimer cela maintenant, et tout a échoué.

Si j'appuie sur espace, il dit que j'ai abri et si je relâche cela, si je vais à ma partie de libération ici, il ne va imprimer cela que lorsque je relâche mon important.

D'accord, maintenant, essayons de lier tous les Les que j'ai couru et dit, ajoutez une fonctionnalité.

Si je clique avec le bouton droit et que je cherche le X de la souris, assurez-vous d'obtenir l'événement, les événements et non les valeurs de la souris.

Donc je vais obtenir le X de la souris et le vi de la souris, les événements.

Donc voyons en fait ce que je veux dire lorsque je dis qu'il retourne une valeur allant de moins un.

Donc ce que je peux faire, c'est à partir de ce nœud, je peux imprimer une chaîne.

Et c'est un flottant, la partie verte est pour le flottant, ce que cela fait, c'est qu'il donne une sortie ou retourne une valeur d'un flottant, qui est la valeur de l'axe.

Et si je fais glisser cette fin, cela va convertir un flottant en une chaîne.

Si je compile et sauvegarde, retourne en arrière, Alt P, si je déplace ma souris, à gauche et à droite, en fait, c'était plus de sexe, oui, donc cela va être à gauche et à droite, vous pouvez voir mes valeurs vont de un à moins un.

Je veux dire, cela commence à un, si je vais à droite, cela va être positif, cela va aller si je vais à gauche, cela va être négatif, cela continue d'ajouter cette valeur ici.

Et il en va de même, vous pouvez essayer cela pour la plupart des pilotes, je ne vais pas perdre le temps de tout le monde en essayant de faire la même chose pour la plupart des pilotes, cela fera la même chose.

D'accord, essayons donc d'ajouter notre mouvement de souris ici.

Si je vais à mon bras de ressort, je dois m'assurer qu'il utilise toujours la rotation de contrôle du pion.

Pourquoi ? Parce que lorsque je change, lorsque je vais faire, c'est que je vais changer la rotation de contrôle du téléphone.

Et c'est ainsi que je vais changer la rotation du bras de ressort, ce qui change la rotation de la caméra.

Pourquoi ? Parce que la caméra est l'enfant d'un bras de ressort.

Ce que cela signifie, c'est que si je déplace mon ressort, la caméra va changer avec lui, tout comme un enfant suit sa mère tout le temps.

C'est essentiellement ainsi que fonctionne la partie de peinture du ressort ici.

De la même manière, la flèche est un enfant du composant capsule, le maillage est l'enfant de la capsule, etc.

Ce qui signifie que lorsque le moment de la capsule est permanent, le maillage bouge avec lui.

D'accord, donc nous allons changer quelque chose appelé le lacet et le tangage, le tangage est l'axe y, le lacet est l'axe Zed.

Donc avec cette valeur d'axe, ajoutez essentiellement cette valeur à l'axe Y ou Zed.

Voyons comment faire cela.

C'est dragonoid.

Et nous allons le rechercher.

Si c'est l'axe x, nous allons ajouter le votre.

Pourquoi ? Parce que l'axe x, si je vais tourner par rapport à mon axe x ici, cela signifie que je vais le faire tourner, vous savez, sur le côté, je ne veux pas cela, n'est-ce pas.

Donc je tourne essentiellement par rapport aux axes définis, qui est essentiellement gauche et droite.

Donc je peux brancher cette valeur ici, copier, je veux dire, je ne vais pas copier cela, je vais juste faire la même chose, mais pour le tangage ici, donc ajouter l'entrée de tangage du contrôleur.

Maintenant, gardez à l'esprit, si j'ai cela désactivé, donc tous les 10 comme cela, si je n'ai pas de nœud exec connecté, cela signifie que cette fonction ne sera pas exécutée, quelle est la fonction de la fonction, c'est un morceau de code, qui peut ou non prendre une entrée, et il fournit une sortie basée sur cela en le traitant.

Donc vous avez une entrée, il traite cette entrée, calcule cela, fait quelque chose et puis fournit une sortie, la sortie ici étant la caméra, la caméra tournant sur la scène.

Donc si je retourne en arrière, Alt P, vous pouvez maintenant voir que j'ai un mouvement de caméra correct ici.

Maintenant, si votre axe est inversé, par exemple, si je vais en haut, je veux aller en bas.

Et si je déplace vers le bas, je veux aller en haut, si je veux faire cela, tout ce que j'ai à faire est d'aller dans mes paramètres de projet à nouveau, aller dans ma partie d'entrée, et je peux simplement changer ma souris vide positive un.

Et si je fais alt v, maintenant, si je déplace, si je déplace vers le haut, je veux dire, cela fait simplement l'inverse, essentiellement.

D'accord.

Ouvrons les blueprints à nouveau, où nous avons fait cela pour notre souris, mais nous devons ajouter un mouvement, évidemment, à cela.

Donc faisons cela.

Maintenant, obtenons les événements.

Donc notre événement de déplacement vers l'avant était essentiellement lié aux touches W et a, je veux dire, W et S.

Donc cherchons l'événement d'accès ici.

Et faisons de même pour le déplacement vers la droite, l'événement X.

Donc j'ai la valeur x ici, pour le déplacement vers l'avant, je vais ajouter cette valeur d'axe à quelque chose appelé le vecteur avant du personnage, le vecteur avant est essentiellement un vecteur qui définit la direction avant.

Et ici, nous allons ajouter cela au vecteur droit.

Le vecteur droit est essentiellement le vecteur qui définit la direction droite.

Donc si je clique avec le bouton droit et ajoute un mouvement, ou si je cherche cela, j'ai besoin de la direction du monde ici.

La direction du monde est que nous obtenons essentiellement l'acteur.

Obtenons en fait la rotation ici.

Donc si je fais glisser cela ici, obtenir la rotation, d'accord, obtenir l'emplacement, obtenir le vecteur avant.

Donc cela va obtenir cette direction va être le vecteur avant, parce que nous allons, nous allons soit avancer soit reculer.

Et cela prend une entrée de rotation d'actif.

Maintenant, c'est une variable, le vecteur avant est une variable.

Et c'est, si je veux dire, il y a une fonction, le vecteur avant lui-même est disponible, ce get forward vector est une fonction.

Et cela n'a pas de mode exec, ce qui signifie que c'est une fonction pure, elle retourne un vecteur, et je peux l'ajouter à la direction du monde, la valeur scalaire va être l'intensité, ce qui signifie essentiellement si j'appuie sur W, cela va retourner une valeur positive, appuyer sur S, cela va retourner une valeur négative.

Et N rot est essentiellement la rotation, je vais obtenir la rotation de l'acteur ici.

Et donc, essentiellement, ce qu'il fait, c'est qu'il fait des mathématiques complexes, et puis dit, d'accord, je sais ce qu'est le vecteur avant.

Donc déplacez-vous, selon cette direction.

Maintenant, la même chose ici, et le mouvement et le pied, mais cela va être pour le vecteur droit.

Donc obtenir le vecteur droit.

Et nous allons à nouveau utiliser la rotation de l'acteur ici.

Donc c'est cela pour notre mouvement.

Et c'est à peu près tout.

Nous avons terminé avec le mouvement.

Donc si je le fais maintenant, je peux me déplacer à gauche, à droite, en avant, en arrière, etc.

Et cela fonctionne parfaitement bien.

Mais mon personnage est toujours dans cette pose V, ou cette pose T.

La raison en est que je n'ai aucune animation assignée.

Avant cela, voyons comment rendre cela net.

Maintenant, d'accord, la longueur de ce nœud ou de cette ligne, la longueur de cette ligne n'a pas d'importance.

Ce n'est pas, ce n'est pas du tout affecter la vitesse.

Juste, juste en ajoutant cela, j'étais assez stupide pour croire que la vitesse était affectée.

Parce que cela.

Ne soyez pas comme moi, ce n'est pas le cas.

Mais assurez-vous toujours que c'est net.

Assurez-vous de pouvoir voir quelle ligne, quel axe, je veux dire, quelle voie était connectée à quoi, etc.

C'est très important.

Donc Compiler et Sauvegarder.

Maintenant, commençons, envoyons un document de notre code ici.

Si je sélectionne tout cela, et que j'appuie sur C, je peux ajouter quelque chose appelé un commentaire.

Cela ne fait rien, mais c'est juste pour nous, pour notre compréhension.

Donc je vais juste dire Ajouter l'entrée de mouvement ici, et ici sur l'écran pour voir ajouter l'entrée de la souris ici.

Maintenant, nous n'allons pas avoir, nous n'allons pas faire sauter un personnage, mais au cas où vous voudriez ajouter la fonctionnalité, je vais vous montrer comment faire cela.

Si je clique avec le bouton droit et que je cherche l'événement de saut.

Donc rappelez-vous, nous avons un événement d'action appelé Jump.

Très impressionné, je veux commencer, je veux juste sauter et sauter est une fonction intégrée de cette classe de personnage.

Donc le personnage commence automatiquement à sauter.

Et ici, je peux dire Arrêter de sauter, parce que je ne veux pas continuer à monter de plus en plus haut.

Donc tous les trois, j'ai mon saut ici à la deuxième personne.

Mais je ne vais pas me donner la peine d'ajouter cela parce que je ne veux pas cela dans mon jeu.

Mais oui, c'est cela pour le mouvement.

Maintenant qu'ils ont ajouté le mouvement, la partie suivante est d'ajouter des animations.

Beaucoup de gens n'aiment pas les animations.

Personnellement, je n'aime pas ajouter des animations.

Mais malheureusement, c'est une partie du développement de jeux.

Donc plongeons dans la façon de faire cela.

Pour les animations, j'ai un blueprint différent que je peux ajouter.

Donc je vais faire une partie de contenu et un nouveau dossier.

Je vais appeler cela animations.

Et créons quelque chose appelé un blueprint d'animation.

Maintenant, la raison pour laquelle nous utilisons un blueprint d'animation, et non le blueprint normal, est que le blueprint d'animation est optimisé spécialement pour les blueprints et les animations, et il a beaucoup de fonctions intégrées.

Maintenant, pour créer un blueprint d'animation, je dois attacher ou assigner un squelette à ce que nous avons déjà vu ce qu'est un squelette.

Donc différentes animations sont faites pour différents squelettes.

Donc assurez-vous de sélectionner le YUI pour mannequin, qui est le squelette intégré, appuyez sur OK, la convention de nommage est AVP.

Oups, encore une fois, cliquez avec le bouton droit, renommez un BP underscore, je vais simplement nommer cela battery man ici.

Double-cliquez.

Et maintenant, j'ai ma pose de sortie, j'ai deux graphiques différents.

Donc ici, j'ai quelque chose appelé le graphique Adam, qui décide essentiellement de la pose de sortie, et dans le graphique d'événements, je peux, par exemple, obtenir la vitesse du personnage et ensuite changer les animations en fonction de cela.

C'est ce que font ces deux graphiques, le graphique d'événements est pour toute la fonctionnalité comme obtenir les variables, ajouter des valeurs aux variables, etc.

Le graphique enum est pour décider de la pose de sortie.

Si je fais glisser un nœud d'ici et que je cherche l'animation de course ou la personne qui court et que je compile.

Maintenant, cela prend une entrée si votre variable est du côté gauche, cela signifie qu'elle prend une entrée.

Si elle est du côté droit, cela signifie que le nœud donne une sortie.

Donc la troisième personne va obtenir l'animation, utiliser la pose d'animation comme sortie.

Et cette sortie est envoyée comme entrée à cette sortie.

Donc ici, composant sauvegarder, je dois aller à Batman et assigner mon blueprint d'animation.

Donc je peux soit sélectionner mon blueprint d'animation et ensuite appuyer sur cette flèche ici.

Ou je peux simplement rechercher par un BP underscore batch command.

Maintenant Compiler et Sauvegarder.

Si je lance cela maintenant, vous pouvez voir que mon animation est jouée en continu.

Je ne veux pas cela, je veux que les animations de repos, tout cela.

Je veux une animation différente pour le strafing, cela semble vraiment bizarre.

Donc nous allons créer quelque chose appelé un espace de mélange pour cela.

Jetons un coup d'œil à ce que sont les espaces de mélange.

Donc bonne animation.

Et c'est pour l'espace de mélange.

Et encore une fois, vous devez assigner le squelette.

Donc ce sera BS underscore battery man.

D'accord, maintenant, ouvrons cela.

Et cela peut sembler un peu confus, mais essentiellement, le Blendspace a l'axe x et l'axe Y.

Et selon les valeurs de celui-ci, une certaine animation sera jouée.

Par exemple, jetons un coup d'œil à la verticale et à l'horizontale, la verticale.

Je pense que la verticale est celle-ci ici.

Oui, c'est la vitesse.

Donc c'est l'axe vertical, nous allons nommer cela la vitesse et en bas sur l'axe horizontal, la direction.

Donc en fonction de ma direction et de ma vitesse, je peux jouer une animation particulière.

Donc ma vitesse minimale ici va être zéro, ma valeur maximale de l'axe ici, mon maximum trois, le 600.

Comme nous l'avons défini dans notre composant de mouvement, une valeur minimale de l'axe ici va être 180.

Par Paul, le maximum va être d'abord 180.

Donc Y, d'abord 180.

Et ensuite 181 80 est généralement vers l'avant, négatif 180 est la direction complètement opposée.

Donc c'est ce que nous faisons ici.

D'accord, donc essentiellement, ce que je dis, c'est, en fait, faisons cela avec un exemple, cherchons sous ce navigateur d'actifs, source pour votre animation d'inactivité, et faites glisser et déposez cela en bas.

Ce que je dis ici, c'est que si ma vitesse est zéro, quelle que soit ma direction, assurez-vous de jouer l'animation d'inactivité, je suis assez sûr que vous pouvez maintenant comprendre ce que cela fait.

Donc si ma vitesse est zéro, alors je vais jouer mon animation d'inactivité.

Maintenant, vous pouvez comprendre où mettre votre animation de course, elle va être tout en haut.

Maintenant, si vous maintenez Maj enfoncée et que vous vous déplacez, vous pouvez en fait prévisualiser l'animation.

Donc si ma vitesse est définie, si ma direction est à zéro, qui est vers l'avant, et ma vitesse est à 600, alors je vais jouer cette animation.

Et elle se transmet lentement, elle ajoute lentement la valeur.

Donc mon animation ralentit à mesure que je descends.

Et ma valeur de prévisualisation, si ma vitesse est à zéro, quelle que soit ma direction, je vais rester inactif.

Donc c'est ce qu'il fait.

Si ma direction est à 90, je veux m'assurer que je me déplace vers la gauche.

Donc cherchons cela, cherchons, experts, jetons un coup d'œil à toutes les familles ici.

D'accord, donc ce qui se passe habituellement, c'est que nous avons différentes animations lorsque le personnage tourne à gauche et lorsque le personnage est à droite.

Mais l'animation, les animations qui sont intégrées, nous n'avons malheureusement pas ces animations.

Donc ce que nous allons faire, c'est que nous allons simplement ajouter run ici.

Et rappelez-vous, lorsque ma direction est à, habituellement, vous aurez aussi une animation de course en arrière.

Donc lorsque la direction est à moins d'argent à MIT, vous voulez généralement que votre personnage se déplace en arrière, donc vous avez une animation différente pour cela, et vous l'ajouterez, respectivement.

Donc c'est juste ajouter cette animation, je ne veux vraiment pas faire cela.

Mais dans notre cours C++, je m'assurerai que nous avons des animations pour nous déplacer à droite, à gauche, en fait, essayons de supprimer toutes les autres valeurs, ayons-en une pour avancer.

Si je sauvegarde cela, et que tout est correct, évidemment, je dois assigner cet espace de mélange dans le jeton d'animation, car nous ne l'avons pas encore assigné.

Donc si je vais à mon blueprint d'animation, je peux faire glisser un nœud et chercher Blendspace.

Donc maintenant je peux voir mon Blendspace vs underscore Batman.

Et cela prend deux entrées, l'une va être la direction, l'autre va être la vitesse, et en fonction de cela, il choisira une animation, ce que nous avons défini.

Donc à partir d'ici, je vais faire glisser et charger et promouvoir cela à une variable.

Donc il crée automatiquement une variable appelée direction et c'est un flottant.

Et je vais promouvoir cela à une variable et cela va être la vitesse, compiler, aller à mon graphique d'événements.

Maintenant dans mon graphique d'événements, je peux obtenir la vitesse et la direction.

Donc voyons comment faire cela.

Maintenant, à partir de lier, obtenir le propriétaire du pion, ce que cela fait, c'est qu'il essaie d'obtenir le propriétaire de ce blueprint d'animation.

Donc je peux maintenant le convertir en mon BP battery man, pourquoi je fais cela, mais en fait, c'est principalement parce que j'ai mon point sur la classe, mais je dois convertir ma classe en mon battery man.

La façon dont cela fonctionne est que si je vais à mon BP underscore battery man et que j'ajoute une variable, je vais simplement l'appeler cette variable de test.

Et je veux obtenir cette variable.

Je ne peux pas l'obtenir à partir de porn, je peux simplement dire obtenir la variable de test, elle n'existe pas.

Mais si je convertis cela en Batman, et ensuite en tant que Batman, si j'essaie d'obtenir la variable de test, maintenant je peux obtenir la variable.

Donc nous essayons de localiser notre localisé ce pion à ma portée VPN, en fait, homme.

Donc à partir d'ici, nous allons en fait d'abord ce que nous allons faire, c'est que nous allons vérifier pour voir si nous avons obtenu notre propriétaire de porn ou non, et cela est fait en utilisant le nœud S valide.

Donc si j'obtiens mon point d'honneur, si je ne suis pas capable d'obtenir mon point ou je peux simplement dire, je peux simplement imprimer une chaîne disant que je suis porn sur ne sont pas valides.

Maintenant, la raison pour laquelle nous faisons cela est à cause de l'avocat, obtenir quelques variables à partir du point d'honneur, le pour s'assurer que nous avons ce propriétaire de pion, sinon votre jeu est et votre jeu va planter, c'est la façon la plus sûre de le faire.

Si c'est valide, ce que nous allons faire, c'est que nous allons convertir en troisième conversion en PP underscore Batman.

Et cela a un nœud exec.

Donc évidemment, cela va à valide.

En tant que Batman, ce que je vais faire, c'est que nous allons obtenir une variable appelée obtenir la vitesse.

Donc la vitesse est évidemment la vitesse.

Mais rappelez-vous, la vitesse a une direction et une magnitude.

Donc à partir de la vitesse, nous allons obtenir, nous allons calculer que vous allez obtenir la longueur du vecteur, la valeur de retour va être votre vitesse.

Donc nous avons déjà promu cela à une variable.

Donc nous allons définir cette variable ici.

Donc faites glisser cette variable sur votre graphique d'événements et appuyez sur Alt, puis vous pouvez simplement faire glisser la valeur de retour sur la vitesse, ce qui signifie que maintenant la valeur de la vitesse va être la vitesse, le vecteur de vitesse de battery man, nous avons évidemment défini la direction à, nous n'avons pas encore terminé.

Donc à partir d'ici, nous allons obtenir la rotation de l'acteur.

Et à partir de la rotation, nous allons calculer la direction.

Donc, évident pour la direction, vous devez calculer ce que vous devez calculer la vitesse.

Donc à partir de la vitesse, vous obtenez quelque chose appelé la direction, c'est ainsi que fonctionnent les vecteurs.

Et encore une fois, je vais dans la même direction.

Et je peux définir la valeur.

Après avoir défini la vitesse, je vais définir la direction.

Donc le flux de contrôle est essentiellement la mise à jour de l'animation.

Cela va essentiellement se produire chaque frame.

À partir d'ici, cela va aller à S valide, cela va vérifier si les propriétaires de pions sont valides, si c'est le cas, le coût pour pvns, allez battery man.

Donc convertir porn en Batman, à partir d'ici, obtenir la vitesse, obtenir la rotation de l'acteur, calculer la longueur du vecteur, calculer la direction, définir la vitesse et puis définir la direction, nous pouvons en fait alors garder cela ici.

Maintenant, nous avons les valeurs pour la vitesse et la direction, tout ce que vous avez à faire est d'aller à Anam graph, et vous pouvez voir qu'il a déjà défini la direction et la vitesse.

Donc maintenant Compiler et Sauvegarder, retourner en arrière.

Et si vous appuyez sur ALT T, j'ai maintenant mes animations.

Évidemment, cela semble un peu bizarre si je vais à gauche et à droite, je n'ai pas d'animations appropriées.

Mais cela va en fait essayer de le faire vous-même, recherchez vos animations gauche et droite.

Allez dans votre espace de noms.

Lorsque votre direction est à moins de 180, vous voulez vous assurer que le personnage va en arrière.

Et pour les animations gauche et droite ici, vous allez placer votre animation droite ici, vous allez appuyer sur votre animation gauche et vérifier si cela fonctionne.

Et si c'est le cas, alors vous avez compris comment fonctionnent les espaces de mélange.

Mais nous allons passer au jeu.

Comme vous l'avez vu au début, la façon dont le jeu fonctionne est que vous avez beaucoup de batteries différentes partout sur la carte.

Et la santé du joueur continue de diminuer.

Et vous devez vous assurer de collecter toutes ces batteries.

Et si vous le faites, alors vous passez au niveau suivant ou vous gagnez le jeu.

Donc voyons comment faire cela.

C'est là que nous allons apprendre sur l'UI, etc.

Donc cela va être la deuxième partie du cours.

Si je vais à mes blueprints, méthode person, en fait pas méthode freschetta.

Évidemment, cela doit être mon AVP underscore Batman, je veux dire, mon btn school Batman ici, nous allons créer une nouvelle variable appelée Health.

Enlevons cela.

Et créons une variable de santé.

Ici, je vais chercher maintenant, je vais en faire un flottant et compiler la valeur par défaut comme valeur par défaut.

Et qu'est-ce qui se passe avec moi, la valeur par défaut va être 100.

Compiler et Sauvegarder.

Maintenant, ce que nous allons faire, c'est que nous allons obtenir notre événement tech et toutes les cinq secondes, nous allons réduire la santé.

Comment faire cela, faire glisser le nœud et puis ajouter un délai ici.

Ce que cela fait, c'est qu'il va essentiellement attendre X montant, ils vont attendre toutes les cinq secondes et obtenir cette valeur.

Donc si vous Jacqueline's funny sur l'écran et puis appuyez sur Ctrl, puis placez-le, vous pourrez obtenir, vous serez en mesure d'obtenir la valeur de votre santé.

Et nous allons soustraire.

Donc si je suis juste, comme vous pouvez le voir, si je cherche moins, je peux soustraire une valeur, et je vais soustraire une valeur de cinq peut-être.

Donc une fois que j'ai soustrait la valeur, donc disons que ma santé est de 100.

Si je la soustrais, la sortie va être 95.

Et j'ai défini ici, encore une fois, défini la valeur que j'ai retournée.

Et puis une fois que j'ai terminé, je peux simplement faire cela.

Maintenant, essentiellement, toutes les cinq secondes, je vais réduire ma santé, imprimons ma santé.

En fait, pour simplifier, je veux dire, assurez-vous que c'est plus rapide, je vais le faire toutes les deux secondes, et faites glisser et déposez la santé, encore une fois, convertie en une chaîne et branchée dans mon fichier de force d'impression et sauvegardez-le.

Maintenant, vous pouvez voir qu'il est à 100, après deux secondes, 95.

Et puis c'est 9085, etc.

Donc cela continue de descendre.

Ce que je vais faire, c'est que je vais ajouter une UI, je vais ajouter une barre de santé pour que cela soit connecté à cela, je vais réduire ma santé toutes les deux secondes, mais je vais réduire ma santé de 10, Compiler et Sauvegarder.

Maintenant, je dois faire quelque chose appelé binding, je vais lier cette maison à mon UI.

Donc voyons comment créer une UI.

Sous les blueprints, je vais créer un nouveau dossier et l'appeler UI.

Et sous UI, vous pouvez aller à FX, je ne fais pas d'effets.

Ce n'est pas une interface utilisateur.

Et je vais créer un Widget Blueprint, les conventions de nommage W BP underscore quel que soit le nom que je vais donner à cela, l'UI du joueur.

Donc dans celui-ci, nous avons quelque chose appelé le designer et le designer, c'est à quoi l'UI va ressembler, vous pouvez me concevoir, vous pouvez essentiellement placer tous ces objets, et vous pouvez en faire une UI correcte, nous allons ajouter quelque chose appelé une barre de progression ici.

Faisons en sorte que cela soit à peu près 500.

Et je vais faire quelque chose appelé l'ancrage.

Ce que cela signifie, c'est que lorsque je redimensionne mon écran, par exemple, si je minimise mon écran, je veux que mon, je veux que cela reste dans le coin supérieur gauche.

Et si je le mets en plein écran, il devrait se déplacer avec l'écran.

C'est ce que signifie l'ancrage.

Donc je vais m'assurer que c'est là.

Et si je fais défiler jusqu'en bas, sous style, j'ai quelque chose appelé l'image de remplissage.

Si je, si je suis, si je fais glisser cela vers le bas, j'ai quelque chose appelé le 10ème.

La première image va être la santé réelle ici.

Donc je vais m'assurer que mon, je veux dire, ma batterie, ma batterie va être verte, cela me rappelle en fait comment changer cela en batterie ici.

D'accord, et assurez-vous de sauvegarder cela ici et de compiler.

Et ici, notre image de fond, faisons en sorte que cela soit en fait, faisons cela en noir, c'est bien.

Et nous devons, nous avons quelque chose appelé le pourcentage.

Maintenant, le pourcentage varie de zéro à un, s'il est un, il va être complètement rempli.

S'il est zéro, il va être vide.

Faisons en sorte que le défaut soit plein.

Et nous allons faire quelque chose appelé le binding.

Donc vous voyez ce bouton bind, et vous pouvez sélectionner Créer un Binding.

Et ce que nous allons faire, c'est que nous allons obtenir la santé et nous allons définir cette santé à ce pourcentage, nous allons convertir la santé en pourcentage, et ensuite nous allons la définir ici.

Donc la valeur de retour va être le pourcentage qui est affiché.

Donc maintenant, nous pouvons dire Obtenir le Personnage du Joueur.

Et cela va retourner quel que soit le personnage que j'ai possédé, le bon RBC convertir cela en mon Batman.

Donc une fois que nous avons fait cela, en tant que Batman, nous pouvons simplement obtenir notre santé et obtenir la batterie.

Et puis nous pouvons définir cela ici.

Mais rappelez-vous, nous devons convertir cela en pourcentage parce que ce pourcentage va être entre zéro et un.

Donc ce que nous allons faire, c'est que nous allons diviser cela par 100.

Rappelez-vous, par définition, le pourcentage signifie par cent, cent est 100.

Donc, nous allons diviser cela par 100.

Et puis le retourner ici, Compiler et Sauvegarder.

Maintenant, nous devons ajouter cette UI sur l'écran.

Pour ce faire, allons au lit, ayons notre début de jeu, toute l'UI sera instanciée en étant en jeu.

Ici, nous allons créer un widget.

Donc nous allons créer un objet de cette UI de joueur.

Donc je dois sélectionner quelle classe, ce sera mon WP player UI.

Et la valeur de retour, je vais ajouter cela à Viewport.

Donc c'est essentiellement pour ajouter cette UI de joueur sur le viewport et quelle que soit la fonction de binding, elle va s'assurer qu'elle exécute tout ce code.

Donc maintenant, si je joue, vous pouvez voir que ma barre de pourcentage diminue lentement, ce qui est incroyable.

Et elle a aussi des décals incroyables.

Donc elle a des graphiques animés.

C'est très cool.

De plus, Unreal Engine, il fait tout pour vous.

Et nous pouvons maintenant supprimer cette chaîne de cadre.

Maintenant, encore une fois, nous devons nous assurer qu'elle ne réduit la valeur que jusqu'à ce qu'elle coûte zéro.

Et une fois qu'elle atteint zéro, je veux tuer mon joueur.

Donc pour ce faire, premièrement, nous allons diminuer la valeur uniquement si ma batterie est supérieure à zéro.

Donc si je fais glisser le contrôle, nous pouvons maintenant chercher le symbole supérieur à.

Et si c'est supérieur à zéro, exécutez uniquement cela.

Mais comment faisons-nous cela ? Comment ajoutons-nous des conditions, nous le faisons par quelque chose appelé une branche.

Donc vous pouvez voir cette couleur rouge ici.

Donc si c'est plus que zéro, cela va retourner vrai.

Si c'est moins que zéro, cela va retourner faux.

Donc à partir d'ici, je peux créer quelque chose appelé une branche.

Et je peux maintenant ajouter cela à cette branche.

Maintenant, si ma santé est supérieure à zéro, alors je vais exécuter cela.

Donc je vais déplacer cela en haut.

Si ma santé est inférieure à zéro, alors je vais dire que mon joueur est mort.

Donc à ce moment-là, je vais ajouter un écran de réessai, etc.

Et je vais m'assurer que je ne possède plus ce personnage.

Mais nous verrons cela plus tard.

Mais créons une variable.

Maintenant.

Disons B est le joueur, c'est une convention de nommage pour les valeurs booléennes, vous vous assurez que c'est B est clair ou autre chose.

Et nous allons nous assurer que ce booléen compile, et la valeur par défaut sera fausse.

Et si je maintiens Alt et que je fais glisser cela sur la scène, nous pouvons définir cela comme vrai ici.

Génial.

Maintenant, si le joueur est mort, alors évidemment, j'ai perdu, donc j'utiliserai un menu d'écran de menu.

Et je peux soit réessayer le jeu, soit jouer au jeu à nouveau.

Donc c'est la fonctionnalité de base que nous allons utiliser ici.

Une fois que le joueur est mort, ce que nous allons faire, c'est que nous avons cette fonction appelée detach from controller pending destroy.

Ce que cela fait, c'est qu'il s'assure que vos contrôles n'affectent pas le joueur une fois que vous avez détaché, une fois que vous êtes mort.

Donc si j'attends et que j'attends, c'est en fait, faisons cela plus vite, je n'ai pas de patience, je vais faire cela à 20 pour que dès que je spawn, comme en quatre secondes, je finis par mourir.

Donc c'est là.

Et maintenant, vous pouvez voir que vous pouvez essayer de contrôler, mais vous remarquerez que vos contrôles ne fonctionnent pas.

Et c'est parce que nous avons détaché de ce contrôleur.

Et nous avons besoin que l'animation s'arrête.

Donc nous pouvons, nous pouvons aussi avoir un autre, donc nous pouvons, nous pouvons soit arrêter notre animation comme cela, mais cela pourrait ne pas fonctionner.

Essayons cela.

Laissez-moi rendre cela amusant parce que je ne veux pas attendre quatre secondes, Compiler et Sauvegarder.

Tous les paiements.

Maintenant, les animations jouent toujours.

Donc nous devons nous en occuper par le montage Adam.

Je veux dire le blueprint d'animation, nous avons cette variable ici, le joueur est mort.

Donc nous allons obtenir cette variable de notre BP battery man.

Et si c'est vrai, ils vont arrêter l'animation.

Donc voyons comment faire cela.

Nous allons apprendre une nouvelle chose appelée le mélange par bleu.

Oui, le Blendspace par bleu.

D'accord.

Ici, dans ce graphique enum, nous avons vu avant que nous avons quelque chose appelé une branche.

Donc si la condition est vraie, faites cela, la condition est fausse pour cela.

Au lieu de cela, ce que nous allons faire, c'est que nous allons dire, cherchez simplement des réponses de mélange par bool.

Puis posez cela par bleu.

D'accord, en tout cas, si nous pouvons passer une valeur booléenne ici.

Et si c'est vrai, il fera cela.

Si c'est faux, nous ferons autre chose.

Maintenant, si un joueur n'est pas mort, nous voulons cet espace de mélange.

Si le joueur est là, alors nous pouvons, peut-être que je sais, nous pouvons jouer l'animation d'inactivité ici.

Et comment obtenons-nous cette valeur ? De la même manière, nous avons BP battery man, ils peuvent aussi dire obtenir le S est le joueur que et nous pouvons promouvoir cela à une variable.

Donc promouvoir la variable et amener cela tout en haut et compiler.

Maintenant, je pense que vous pouvez comprendre le reste, nous pouvons simplement glisser-déposer cela ici.

Et maintenant, cela va s'assurer que si c'est mort, alors il veut juste jouer l'animation d'inactivité et ne rien faire parce que nous n'avons pas de carburant pour courir.

Nous y voilà.

Cela fonctionne parfaitement bien.

Et après cela, nous devons nous assurer que nous affichons notre écran de joueur Lua.

Maintenant, essayez de faire cela par vous-même, cela peut être un peu difficile, mais donnez simplement un coup de feu.

Si vous ne pouvez pas, aucun problème, nous allons le faire de toute façon, nous allons créer une nouvelle interface utilisateur, nous allons en fait en créer deux.

L'une est pour le joueur quand l'autre est pour le joueur deux.

Donc nous WP underscore.

En fait, nous n'avons pas besoin d'un blueprint de Widget Blueprint pour quand parce que nous allons automatiquement passer au niveau suivant.

Ou nous allons simplement l'avoir, cela va passer au niveau suivant.

Et ici, nous pouvons simplement nommer cela l'écran BV WPP Lu et la partie designer.

Je vais ajouter une image d'abord, faisons en sorte que cela s'adapte complètement à cette poignée.

Et assurez-vous que nous avons cela correctement aligné.

D'accord, en tout cas, même si c'est surdimensionné, aucun problème, nous allons ancrer cela pour qu'il soit en plein écran.

Nous y voilà.

Donc cela va s'assurer qu'il est toujours en plein écran.

Et je vais changer l'opacité à, je vais changer la couleur en noir et le F deux comme cela.

Cela a l'air bien.

Nous allons avoir deux boutons maintenant.

Le premier bouton est essentiellement pour une seconde.

Donnez-moi une seconde, d'accord, le premier bouton, ce qu'il va faire, c'est quand il y a, quand la partie de réessai, donc réessayer le jeu, et avoir besoin d'ajouter du texte.

Le même bouton, je peux faire le cater.

Et ils vont ajouter cela ici.

Je sais que ce n'est pas exactement aligné, mais c'est bien.

Cela va être la couleur de sortie et l'opacité semble juste bien pour moi.

Oui, cela semble juste bien.

Aucun problème.

D'accord, maintenant, voyons comment ajouter du texte à cela, tout ce que vous avez à faire est de chercher du texte et de le faire glisser et de le déposer, il va automatiquement l'apparier, faire de ce texte un enfant.

Et soit le bloc de texte ici vont sauvegarder le jeu de réessai.

Ou en fait, habituellement, nous réessayons simplement.

Et sur le téléphone, je vais changer la taille à peut-être 34.

Cela semble bien.

Et pour le jeu rapide à nouveau, un autre bloc de texte, ils vont le faire 3042.

Et nous pouvons simplement dire quitter.

Game nation, je vais nommer ce bloc de texte pour quitter le texte.

Et celui-ci va être réessayer.

Et nous allons avoir un gros bloc de texte ici.

Et celui-ci, nous allons le nommer.

Nous allons simplement dire que vous faites cela, c'est à peu près tout.

Laissez-moi faire cela 80 en fait vivant et manuel, je dis simplement que je vais dire que vous Louis.

D'accord, génial.

Dans mon graphique, je dois m'assurer d'ajouter une fonctionnalité à cela, à ces boutons.

Donc si vous faites défiler jusqu'en bas après avoir sélectionné le bouton, nous avons on click et on press, nous allons utiliser le on pressed parce que cela fonctionne mieux, par exemple, si vous appuyez sur entrer par erreur, cela pourrait simplement finir par réessayer à nouveau, nous ne voulons pas cela, nous devons nous assurer que nous cliquons sur le bouton.

Donc c'est pourquoi nous utilisons on pressed, faites de même pour le jeu de réessai, je veux dire pour le jeu de sortie.

Pas sur le clic, sur le pressed ici.

Et pour le réessai, ils vont ouvrir, nous allons charger le niveau, nous allons charger exactement le même niveau.

Donc ce niveau va être obtenir le niveau, obtenir le nom du niveau actuel.

Parce que si c'est un niveau différent, si c'est le niveau deux, alors il doit s'assurer qu'il a, il ouvre ce niveau.

Donc obtenir le nom actuel garantit qu'il obtient le niveau approprié, le niveau que vous exécutez en ce moment.

Et nous allons ouvrir ce niveau.

Donc c'est essentiellement pour ouvrir le même niveau, encore une fois, tous les paramètres par défaut pour le jeu de sortie, c'est littéralement un seul nœud, le jeu de sortie.

C'est tout, Compiler et Sauvegarder.

Maintenant, si je minimise mon écran appelé P, encore une fois, nous devons nous assurer que nous l'ajoutons à Viewport.

Donc si je vais à mes blueprints, si mon joueur est que détaché du contrôleur en attente de destruction, c'est bien.

Et ce que nous avons fait ici, nous faisons exactement la même chose ici.

Mais le problème est, rappelez-vous, cela est sur tick.

Et lorsque nous créons, lorsque nous mettons cela sur tick, cela signifie qu'il va créer le widget du joueur chaque frame et l'ajouter à Viewport chaque frame, ce qui signifie que votre jeu pourrait finir par planter.

Donc nous allons ajouter un nœud qui dit faire une fois.

Cela signifie qu'il va faire ce qui vient après seulement une fois.

Ils vont brûler pour s'assurer que nous recréons le widget de l'écran de défaite, et puis nous allons ajouter à Viewport.

Maintenant, si nous compilons et sauvegardons, jouons au jeu.

Et maintenant, il dit qu'il a perdu.

Mais le problème est que nous ne pouvons pas utiliser notre souris, nous pouvons seulement, vous savez, nous devons appuyer sur windows, etc.

Donc si vous voulez montrer le curseur de la souris, obtenez votre contrôleur de joueur, tout ce qui est lié aux contrôles est présent dans le contrôleur de joueur, et ici, cherchez le curseur.

Voyons ce que nous avons ici.

Nous avons obtenir le curseur de la souris, définir le curseur de la souris.

Donc nous pouvons définir cela par cette valeur est présente dans le contrôleur de joueur, nous pouvons définir cela à vrai après Compiler et Sauvegarder cela et minimiser.

Et nous courons.

Et maintenant, je peux voir mon curseur.

Si j'appuie sur réessayer.

Il charge le même niveau à nouveau, et je perds et blah, blah, blah.

Donc cela redémarre essentiellement le niveau.

D'accord, génial.

Nous avons fait tout cela.

Maintenant, voyons comment convertir ceux-ci en fonctions.

Les fonctions sont essentiellement des blocs de code transformés en un seul morceau d'objet, que vous pouvez appeler plus tard.

Par exemple, si je clique avec le bouton droit sur tout cela, réduire en fonction, réduire la fonction fail, voyons pourquoi est-ce que c'est d'accord ? Le délai ne peut pas être d'accord, certains.

D'accord, créons simplement une fonction de test ici, une fonction de test.

Donc cette fonction peut avoir beaucoup de fonctionnalités différentes.

Par exemple, imaginez que j'ai 1000 nœuds dans ce graphique ici, j'ai oublié même le graphique si je suis, si je veux appeler cette fonction à nouveau, comme dans 10 positions différentes.

Qu'est-ce que cela fait mieux pour moi d'appeler cette fonction plutôt que de créer ces 1000 nœuds encore et encore, cela va avoir l'air très, très sale, c'est pourquoi je préfère mettre ces 1000 nœuds dans une fonction, et ensuite je peux appeler cette fonction, et les délais ne peuvent pas être ajoutés dans une fonction.

Donc si je clique avec le bouton droit ici, je peux simplement réduire cela à une fonction.

Et je peux dire que j'utilise la santé.

Et cette fonction, nous savons qu'elle réduit la santé.

Si je double-clique dessus, cela fait exactement la même chose ici.

Maintenant, si vous voulez, vous pouvez convertir cela en une fonction, je vais le laisser, ils ont fait cela pour moi, ils ont fait une fonction pour cela, mais je vais laisser la partie de la mort du joueur telle quelle.

Mais je peux peut-être ajouter cette partie à une fonction.

Mais cela dépend de vous.

Ou je peux simplement réduire cela à un nœud pour réduire à un nœud player deck.

Donc cela installe essentiellement un graphique 11ème.

Ce n'est pas, ce n'est pas une fonction ou autre chose, mais nous rendons simplement cette partie du code plus rapide.

Je veux dire, plus courte afin que nous puissions découvrir ce qui se passe.

D'accord, donc maintenant, créons une variable appelée batteries collectées, il devrait y avoir un entier par, ce que nous allons faire, c'est que nous allons avoir un nombre maximum de batteries par niveau.

Par exemple, ce niveau aura probablement huit batteries différentes.

Et une fois que nous les avons toutes collectées, nous allons vérifier si le nombre de batteries que nous avons collectées est égal au nombre de patties qui doivent être collectées.

Et si c'est égal, alors nous pouvons dire que le joueur a gagné le jeu et passer au niveau suivant.

Ou ils peuvent simplement afficher l'écran de victoire, mais dans ce cas, nous allons simplement passer à un nouveau niveau, et vous pouvez ajouter toutes les autres fonctionnalités.

Donc une fois que nous avons réduit la santé, cette partie signifie que le joueur n'est pas encore mort, comme vous pouvez le voir ici.

Donc ce que nous allons faire, c'est qu'après avoir relâché la tête, nous allons vérifier pour voir si le nombre de batteries que nous avons collectées est égal.

Mais en fait, nous ne allons pas faire cela dans le joueur, nous allons le faire dans quelque chose appelé le Blueprint de Niveau.

Donc si je vais à mes effets de niveau ici sur le blueprint, et si je clique sur Ouvrir le Blueprint de Niveau, c'est un type différent de blueprint, il est pour le niveau lui-même, et il peut accéder à chaque objet présent dans le niveau.

Et je peux ajouter des fonctionnalités en fonction de cela, par exemple, je peux obtenir, je peux obtenir le personnage qui est présent dans ce niveau, et ensuite vérifier pour voir combien de batteries il a collectées.

Et vérifier pour voir si le nombre de batteries que j'ai collectées est, vous savez, égal au nombre de batteries qu'elles doivent être collectées, et ensuite changer pour le niveau suivant.

Donc commençons par cela.

Tout d'abord, dans le début du jeu, nous allons obtenir notre BP underscore Batman.

Donc Obtenir le Personnage du Joueur, nous allons le convertir en fi underscore Batman.

Donc nous allons convertir notre personnage en Batman.

Et ensuite, en tant que Batman, nous allons promouvoir cela à une variable, afin que nous ayons une référence à notre joueur à tout moment.

Et dans le tech.

Donc maintenant, nous allons introduire autre chose.

Mais avant de commencer à faire nos conditions de Venn, implémentons en fait nos batteries elles-mêmes.

Donc cliquez avec le bouton droit, créez un nouveau blueprint.

Et cela va être un acteur, TV underscore battery.

Si je l'ouvre, je vais ajouter quelque chose appelé box.

Et je vais juste ajouter, en fait, laissez-moi juste ajouter un cube ici.

Si je fais défiler jusqu'en bas, d'accord, j'ajoute un cube, cela va être ma batterie, votre titre, essayez de changer le maillage statique en autre chose, peut-être essayez de trouver un acide de batterie et changez le maillage en une batterie.

Mais je vais le laisser tel quel, nous allons le mettre à l'échelle.

Donc si vous voulez mettre à l'échelle et appuyer sur r, je vais rendre cela plat.

Quelque chose comme cela.

D'accord, génial.

Maintenant, ce que nous allons faire, c'est que je vais changer le matériau en peut-être, j'ai vu ce matériau vraiment cool qu'Unreal Engine a, il a cette texture de type cyberpunk, nous y voilà.

J'adore cette texture.

Je vais en faire cela.

D'accord.

Maintenant, si nous faisons défiler jusqu'en bas, nous avons beaucoup d'événements différents.

Ce que sont ces événements, c'est que lorsque le composant est touché, faites quelque chose, lorsque quelqu'un chevauche le composant, faites quelque chose lorsque qu'un objet a terminé de chevaucher, faites quelque chose.

C'est essentiellement tout ce que font ces événements.

C'est ce que font ces événements, essayons de jeter un coup d'œil à l'événement on component head appelé lorsque qu'un composant frappe quelque chose de solide.

Donc si ce composant frappe, peut-être quelque chose de solide, comme un autre cube ou un joueur, qu'est-ce qu'il est censé faire, c'est ainsi que fonctionnent les balles de projectile dans le développement de jeux, essayons de jeter un coup d'œil à on competent head, appuyez sur si je clique sur le symbole plus, j'ai quelque chose appelé le head component.

Et l'autre acteur, l'autre acteur va être quel que soit l'acteur qui a collisionné ou frappé ce cube ici.

Et nous allons le convertir en notre battery man.

Non, pas la batterie, le battery man.

Donc cherchez battery man.

Maintenant, si c'est vrai, donc si j'ai converti, si j'ai frappé le battery man, alors nous allons obtenir la santé.

Obtenez la batterie.

Et puis nous allons ajouter, peut-être voyons, nous allons ajouter un montant qui est en fait, faisons de cela une valeur aléatoire, soustrayons un nœud de cela et puis il devrait y avoir un nœud qui dit random float in range, nous allons ajouter une valeur entre cinq et 10.

Donc cela va retourner une valeur de cinq et avoir un nombre, un nombre aléatoire entre cinq et 10.

Et à partir de la batterie, nous allons définir la batterie à nouveau.

Et puis nous pouvons faire glisser cela pour Compiler et Sauvegarder.

Voyons si cela fonctionne.

Et je dois évidemment détruire cet objet parce que je ne veux pas tricher, donc je peux détruire l'acteur, ce qui signifie qu'il va être supprimé de la scène.

Si j'ai placé cet objet ici, et que je le déplace en haut, peut-être que nous pouvons ajouter des lignes, quoi ? Oups, d'accord, je dois m'assurer que je, le jeu n'est pas si difficile pour moi.

Donc je vais changer ma valeur de batterie à 100, Compiler et Sauvegarder, alt faith, fam, me déplacer vers cette batterie, vous pouvez voir que ma tête a augmenté ici, laissez-moi vous montrer à nouveau ma batterie.

Donc vous pouvez voir qu'elle augmente lentement, ce que nous allons faire ici.

Maintenant, nous allons nous assurer que nous continuons à augmenter notre batterie pour notre joueur ici.

Laissez-moi retourner à mon BP underscore battery, laissez-moi ajouter une lumière ici, une lumière ponctuelle.

Et assurez-vous de la soulever en haut parce que si elle est à l'intérieur de l'objet, vous ne pourrez pas la voir.

Et nous pouvons la rendre rouge.

D'accord, Compiler et Sauvegarder.

Maintenant, voici la partie intéressante.

C'est là que nous faisons nos conditions de victoire.

Donc ici, une fois que nous avons ajouté la santé, ajouté, d'accord, mon adversaire a été ajouté à la batterie de notre battery man, nous pouvons ajouter une variable aux batteries que le joueur a collectées.

Donc encore une fois, obtenez les batteries collectées ici.

Et nous avons évidemment le set de doses, set that is collected, j'espère que cela ne devient pas trop confus.

Si vous le faites, alors essayez de faire un peu de maths dans un projet différent par vous-même en obtenant des valeurs d'un joueur et en les convertissant.

Et vous serez en mesure de les comprendre en un rien de temps, je vais ajouter un aux batteries collectées.

Donc si je dis, par exemple, que j'ai trois batteries déjà collectées, je vais en ajouter une.

Donc cela va devenir quatre, je vais définir les batteries collectées.

Et puis je vais détruire le cube, Compiler et Sauvegarder.

Maintenant, dans mon Level Blueprint, je dois m'assurer que je définis ce qu'est le nombre maximum de batteries, n'est-ce pas.

Donc essayons de faire cela.

Maintenant, cliquez avec le bouton droit, nous allons jeter un coup d'œil à quelque chose appelé le Game Instance.

Donc jetons un coup d'œil à Game Instance ici.

Maintenant, gi underscore battery, man instance citizen tout cela.

Donc dans cette instance, ce qu'est une Game Instance, c'est qu'il s'agit d'un objet qui persiste à travers chaque niveau.

Donc cet objet sera là dans le niveau principal.

Et puis le niveau un, le niveau deux, le niveau trois, cela va persister dans chaque niveau.

Donc nous pouvons ajouter quelques variables qui disent d'accord, si c'est le niveau un, alors assurez-vous que le nombre de batteries est, disons, huit.

Et cela doit être 10, etc.

Maintenant, ce n'est pas la meilleure façon de le faire.

Mais puisque c'est un tutoriel de niveau très débutant, nous ne allons pas passer en revue le gameplay, comme les mécaniques de gameplay appropriées.

Donc je vais simplement ajouter une variable ici.

Donc le niveau un, puis les batteries, en fait non, les batteries max.

Un.

Cela indique pour le niveau un, c'est le nombre maximum de batteries que nous allons faire, c'est un flottant.

Et cela, cette valeur va être huit.

Maintenant, si vous voulez un autre niveau, disons le niveau deux, vous pouvez dire Max batteries, deux, etc.

Maintenant, allez au Level Blueprint.

Et vous devrez faire cela pour chaque niveau.

Mais dans le tech, ce que nous pouvons faire, c'est que nous pouvons cliquer avec le bouton droit sur Get Game Instance, nous devons convertir cela en notre batterie man instance cost vi batterie man instance.

Et encore une fois, nous pouvons faire cela dans le big and play parce que nous ne voulons pas parler, nous ne voulons pas convertir cela chaque frame.

Et puis nous pouvons promouvoir cela à une variable gi batterie math.

D'accord, maintenant, à partir de l'instance batterie man, ce que nous pouvons faire, c'est que nous pouvons obtenir le max batteries pour un.

Et puis à partir de notre batterie man, le joueur lui-même, nous pouvons obtenir les batteries connectées.

Nous allons vérifier si elles sont égales.

Maintenant, j'ai oublié de faire de cela un entier.

Donc assurons-nous que cela est un entier pour Compiler et Sauvegarder le niveau un qui est vérifié pour voir si elles sont égales.

Donc je peux, si elles sont égales, alors je peux essentiellement dire, donc encore une fois, nous devons créer une branche, donc nous créons une condition ici.

Donc si nous créons une branche Event Tick, si ces deux sont égaux, alors j'ai gagné le jeu.

Donc je peux simplement finir par ouvrir le niveau suivant ou encore une fois, je peux avoir un écran de victoire ou autre chose, un autre écran pour cela.

Et appelons cela niveau, le niveau suivant, peu importe.

Par exemple, celui-ci va être le niveau deux, vous devrez faire cela pour chaque niveau de jeu.

Mais rappelez-vous, dans le cours C++, puisque ce sera un cours plus avancé, nous allons voir comment rendre cela beaucoup plus évolutif, dans le sens de comment s'assurer que nous ajoutons la logique une fois et que nous n'avons pas à continuer à copier-coller notre code encore et encore.

Maintenant qu'ils ont créé le Game Instance, nous devons nous assurer de le définir dans nos paramètres de projet.

Donc allez dans les cartes et les modes.

Et si vous faites défiler jusqu'en bas, notre Game Instance par défaut doit être gi underscore batterie instance, laissez-nous créer un autre niveau ici.

Donc encore une fois, nouveau niveau, il y aura un niveau par défaut et sauvegardez-le.

Nous allons appeler cela niveau deux.

Et c'est à peu près tout.

Je parie que nous avons terminé avec toute notre mécanique de code.

Maintenant, si je joue au jeu, et disons que notre maximum va être un.

Donc si j'ouvre mon Game Instance, ici, mon nombre maximum d'entrées va être un, par exemple, sauvegardez le jeu.

Et si je joue maintenant, nous passons maintenant au niveau suivant.

Donc c'est ainsi que nous faisons nos conditions de victoire.

Maintenant, tout ce que vous avez à faire est de décorer votre niveau, peut-être ajouter quelques obstacles, et peut-être comme quelques cubes qui distraient le joueur, peut-être essayer de faire de cela un labyrinthe, obtenir quelques actifs du marketplace et essayer de le faire de telle sorte que peut-être c'est comme dans un vaisseau spatial, et le joueur doit trouver toutes les batteries du vaisseau spatial, ce qui aurait probablement l'air vraiment cool.

Mais maintenant, j'ai cinq batteries différentes ici.

Donc je vais aller à mon Game Instance, le maximum de batteries va être cinq ici.

Compiler et Sauvegarder, et sauvegardez-le.

D'accord.

Maintenant, voyons si cela fonctionne toujours.

Donc tous les fiefs, je vais collecter, oops, il semble que je dois m'assurer que cela est tout en bas.

Donc tout en bas, tout en bas.

D'accord, tous les fiefs.

Maintenant, voyons.

Donc d'abord, ma batterie continue d'augmenter.

Donc c'est assez cool.

Mais d'accord, je pourrais, je pourrais en fait perdre cela.

Je ne suis pas vraiment bon aux jeux.

D'accord.

D'accord, nous semblons, nous semblons gagner le jeu.

C'est génial.

Et oui, c'est à peu près tout pour nos événements de victoire.

Maintenant, disons que votre niveau deux est votre dernier événement, ce que vous faites, c'est dans votre Level Blueprint de niveau deux.

Donc si vous ouvrez le blueprint, il suffit d'avoir la même condition que celle que vous aviez dans le niveau un, sauf si c'est égal, vous créez un nouveau widget, votre écran de victoire, par exemple.

Et puis vous affichez cet écran de victoire sur la scène.

Par exemple, si je vais au niveau deux, maintenant, laissez-moi en fait vous montrer comment faire cela rapidement.

Donc si je vais au niveau deux, ouvre mon Level Blueprint, maintenant je peux essayer de le faire par moi-même, s'il vous plaît, n'essayez pas de copier ce que je fais.

C'est bien, je veux tout montrer parce que je veux m'assurer que vous, les gars, le comprenez par vous-mêmes.

Ce que vous faites, c'est que vous allez obtenir votre Game Instance à nouveau, vous allez la convertir en deux instances de batterie.

Et nous faisons à peu près la même chose que nous avons fait avant.

Et rappelez-vous, si vous avez le niveau deux, votre Level Blueprint de niveau deux ouvert, vous pouvez ouvrir votre Level Blueprint de niveau un, il va se fermer automatiquement.

Donc nous allons promouvoir cela à une variable.

Et la même chose se produit sauf qu'elle va être pour notre Personnage du Joueur.

Donc Obtenir le Personnage du Joueur, convertir en battery man.

Donc essentiellement, le convertir en battery man et puis promouvoir la variable.

Et puis nous pouvons obtenir le max, je veux dire, obtenir les batteries collectées.

Et nous pouvons utiliser cela pour comparer.

Donc dans notre Event deck, ce que nous allons faire, c'est que nous pouvons obtenir ces deux obtenir les batteries man, donc il va y avoir, donc nous devons créer une nouvelle condition pour le niveau deux.

Donc tout ce que vous avez à faire est Ctrl C Ctrl V, renommez cela en max batteries deux, je vais juste m'assurer que la batterie max est juste quelque chose comme un pour mon niveau deux.

Donc cela est égal au nombre de batteries que nous avons collectées, pas le nombre de batteries, le nombre de batteries collectées, si cela est vrai, ce qui va se passer, c'est que je peux simplement imprimer, je peux créer un nouveau widget, il va y avoir mon écran de victoire ici, qui va essentiellement avoir un texte qui dit que vous gagnez le jeu, et puis il peut avoir un jeu rapide.

Et puis ici, nous pouvons dire convertir en, je veux dire, et à Viewport pour le temps de compiler, il a une flèche ici, parce que la classe Create Widget doit être spécifiée.

Donc créons un nouvel élément UI ici.

Donc UI.

En fait, laissez-moi simplement, laissez-moi faire des patineurs W, BP underscore wind screen.

Maintenant, dans le stuff lose, ils peuvent simplement dire, vous quand.

Et nous allons charger pour réessayer, nous allons charger le premier niveau.

Et en fait, ayons la partie de retour au menu principal dans cette veine de menu principal, et quittez le jeu.

Oui, le cinquième jeu va être le même.

Maintenant, dans le graphique, ouvrez le niveau quatre, parce que nous devons nous assurer de renommer tout parce que nous venons de le dupliquer.

Donc pour le jeu de réessai ici, nous devons nous assurer que cela dit menu principal maintenant.

C'est juste pour simplifier.

Maintenant, lorsque vous appuyez sur le menu principal, nous voulons ouvrir le menu principal.

Donc nous allons créer un nouveau niveau appelé Menu Principal, évidemment, Compiler et Sauvegarder.

Parce que si je vais au niveau deux, je peux simplement créer l'écran principal et m'assurer que vous obtenez le contrôleur du joueur.

Donc Obtenez le contrôleur du joueur.

Montrez le curseur de la souris, nous allons le définir, ne l'obtenez pas.

Donc Montrez le curseur de la souris, définissez-le, nous allons le définir à vrai, Compiler et Sauvegarder.

Maintenant, nous avons le menu principal, nous avons la partie du menu principal.

Et c'est à peu près tout.

Donc ma condition pour mon deuxième niveau va être deux ensembles, il faut collecter deux batteries et j'ai dans le jeu.

Donc ici, nous allons finir par ajouter des batteries à nouveau, nous allons ajouter deux batteries.

Si je jouais au jeu maintenant, j'ai collecté une, j'ai collecté deux, et cela ne semble pas fonctionner, jetons un coup d'œil à ce qui se passe.

D'accord, la raison pour laquelle cela ne fonctionnait pas, c'est que j'ai obtenu la variable pour le premier niveau.

Donc nous allons obtenir les batteries ici et nous assurer de définir cela maintenant, cela va fonctionner.

Donc si je compile et sauvegarde, et encore une fois, rappelez-vous que nous devons nous assurer de nous détacher de, d'accord, si je retourne à mon battery man, vous voyez que nous avons détaché de la destruction en attente ici, nous allons faire la même chose ici.

C'est parce que lorsque je déplace ma souris, je ne veux pas que ma caméra bouge dans mon écran de victoire.

Donc voyons, voyons en fait si nous pouvons obtenir cela par nous-mêmes.

Donc détacher de non, je ne suis pas capable d'obtenir ce nœud particulier.

Donc voyons si cela est présent dans notre contrôleur de joueur.

Non, ce n'est pas présent dans notre contrôleur de joueur, ce qui signifie qu'il devrait être présent dans notre personnage lui-même.

detach from controller pending destroyed, nous y voilà.

Nous pouvons faire cela Compiler et Sauvegarder.

Donc cela signifie que nous ne pouvons plus contrôler notre joueur.

Donc une fois que j'ai collecté ces deux batteries, il dit que vous avez gagné et encore un problème.

Cela se passe dans le tech.

Donc nous devons nous assurer que nous faisons cela seulement une fois.

Nous ne voulons pas que cela se fasse chaque frame, cela va planter votre jeu, ce qui était sur le point de planter mon jeu.

Donc nous devons nous assurer que cela est fait seulement une fois.

Si vous voulez, vous pouvez mettre tout cela dans une fonction.

Et encore, nous allons sauvegarder cela, revenir, OLOFI, collecter le premier, le second, nous avons gagné, quitter le jeu et nous avons terminé avec le jeu.

Génial.

Maintenant, évidemment, ce n'est pas la meilleure façon de faire une condition de victoire, mais si vous voulez le faire, ne vous inquiétez pas de le faire de la meilleure façon possible la première fois que vous essayez.

Le point principal est de comprendre comment fonctionnent les blueprints en premier, et ensuite dans le prochain cours, c'est bien.

Le prochain cours sera un cours plus avancé où nous apprendrons les conditions de victoire appropriées, tous les principes de gameplay, etc.

Maintenant, il nous reste une chose.

Et puis nous avons enfin terminé ce cours, ce qui va être notre menu principal.

Donc, en fait, j'ai dû créer un autre Widget Blueprint, W BP underscore main menu ici.

Et je vais ajouter une image à nouveau.

Faisons en sorte que cela soit en plein écran et ancré, assurez-vous que cela soit en plein écran.

Et maintenant, ce que nous allons faire, c'est, eh bien, laissez-moi d'abord changer cela en noir, cela va avoir deux boutons, l'un va être jouer au jeu, l'autre va être quitter le jeu.

C'est à peu près tout.

Et je suis assez sûr que c'est explicite.

Je suis assez sûr que la plupart d'entre vous, les gars, pourront le faire par vous-mêmes maintenant.

Mais si ce n'est pas le cas, aucun problème, ne vous sentez pas démotivé, c'est complètement normal.

C'est normal.

Donc nous allons sauvegarder jouer au jeu ici.

Dupliquer ce contrôle, en fait, oui, Ctrl W, c'est dupliquer.

Et ils vont, ils vont faire cela, je vais appeler cela quitter le jeu.

Et évidemment, vous pouvez avoir un autre, vous pouvez avoir un autre bouton qui montre les contrôles, etc.

Ici, c'est ajouter du texte, du texte aux deux jouer au jeu et le faire à nouveau, je l'ai ajouté à l'image par erreur.

Donc je vais supprimer cela, cela va s'appeler jouer au jeu.

Cela va s'appeler charger le jeu.

Et évidemment, nous voulons changer la taille à, disons, peut-être 34.

Ce n'est pas du fake.

Je vais simplement rapidement ici.

Et ici, encore une fois, retournez à la police, faites-en 34 Compiler et Sauvegarder.

Comment disons-nous à l'éditeur que chaque fois que nous ouvrons un projet ou le jeu, nous devons nous assurer qu'il ouvre ce menu principal.

Pour ce faire, allez dans les cartes et les modes.

Et vous pouvez voir votre carte de démarrage de l'éditeur et votre carte par défaut du jeu, ce que je vais faire, c'est que je vais créer un nouveau niveau et m'assurer qu'il ouvre le menu principal.

Maintenant, ouvrez un nouveau niveau.

En fait, nous n'avons pas besoin d'en faire un niveau par défaut, nous pouvons simplement créer un niveau vide ici.

Et Ctrl S, vous pouvez voir qu'il est complètement sombre parce qu'il n'y a rien dans ce niveau, nous allons appeler cela le Menu Principal.

Ici, ce que nous allons faire, c'est ouvrir votre Level Blueprint.

Avant cela, nous devons ajouter un override de mode de jeu parce que, comme je l'ai dit, il n'a pas à ajouter.

Donc si je lance ce jeu maintenant, il va, d'accord, tout en haut.

Si vous voyez qu'il spawn, il spawn le BP underscore Batchi.

Homme, nous ne voulons pas cela, évidemment.

Donc ce que nous allons faire, c'est que nous allons ajouter un override de mode de jeu ici, ce qui signifie que pour ce niveau seul, il va créer un mode de jeu différent et il va l'utiliser, donc sous les blueprints personnalisés, je vais créer GM underscore main menu.

Et ici, sous le point par défaut, ce sera aucun, sous dur, je vais avoir tout cela normal.

Maintenant.

Sous les blueprints, ouvrez le Level Blueprint, encore une fois, nous allons faire la même chose sauf que cela pourrait être en vegan play.

Donc créez un widget.

Et ce que nous allons créer, c'est le menu principal et ajoutez à Viewport Compiler et Sauvegarder.

Maintenant, si je retourne à mes paramètres de projet, faites défiler, faites défiler ici, j'ai ma carte de démarrage de l'éditeur.

Je vais garder mon niveau sélectionné ici, donc le contenu des niveaux, le menu principal, je vais appuyer sur cette flèche et il va automatiquement assigner mon menu principal maintenant, jouons au jeu.

Donc appuyez sur Jouer au jeu, rien ne se passe, c'est parce que nous n'avons pas encore ajouté de fonctionnalité.

Donc si je vais au menu principal, sélectionnez ce bouton à nouveau, faites défiler jusqu'en bas, appuyez sur, vous savez quoi faire, ouvrez le niveau, cela va être le niveau un.

Et si je vais à quitter le jeu, appuyez à nouveau, vous pouvez simplement quitter le jeu.

Maintenant, assurez-vous que dans le niveau deux, le niveau bleu dans notre écran de victoire, le Level Blueprint.

Le niveau est nommé correctement.

Donc c'est le menu principal sans espace, Compiler et Sauvegarder.

Et cela est pour avoir un aperçu maintenant.

Donc si je fais alt V trois jeu, j'ai mon HUD, et vous pouvez avoir VLC à cause de cela, d'accord, nous y voilà.

Nous allons essayer de collecter toutes celles-ci à temps.

Et c'est le niveau deux.

Et le niveau deux, nous allons, nous allons obtenir celles-ci.

Et maintenant nous gagnons le jeu.

Et nous pouvons quitter le jeu.

C'est à peu près tout.

Maintenant, nous avons une toute petite partie ici, l'animation continue de jouer pour l'animation continue de jouer pour notre bien dans notre niveau deux après avoir gagné le jeu, parce que nous n'avons pas ajouté une condition de victoire dans notre Animation Blueprint.

Donc ce que nous allons faire, c'est que nous allons aussi ajouter une autre variable, et cette variable va s'appeler B a layer one.

Maintenant, dans le début du jeu, je vais m'assurer de définir cette valeur à faux et m'assurer que c'est un bool.

Donc nous allons changer le type de variable.

Fermer Compiler et Sauvegarder, et m'assurer de définir cela à faux chaque fois que nous commençons à jouer au jeu.

Ici, dans mon Level Blueprint, encore une fois, ce que je vais faire, c'est dans le niveau un, à Sauvegarder les blueprints sélectionnés, Ouvrir le Level Blueprint.

Et nous devons nous assurer d'obtenir ce personnage à partir du personnage ici, définir.

Clear one a player one ici.

Si c'est vrai, alors nous pouvons définir, nous pouvons en fait, nous devons définir cela uniquement dans le niveau deux, pas notre niveau un, parce que notre joueur n'a pas techniquement gagné le jeu complètement encore.

Donc si je vais au niveau deux, ouvre mon Level Blueprint, j'ai la même chose ici aussi.

Maintenant, si je, si je, à partir du battery man, je dois définir un, cherchez simplement has player one, je vais double-cliquer sur ce nœud pour que je puisse rediriger ce nœud ici comme cela.

Déplacez-le tout au bout.

Et puis connectez cela, nous allons le définir à vrai, je vais encore ajouter un autre nœud ici pour que nous puissions le détecter correctement, cela semble un peu net.

Compiler et Sauvegarder.

Maintenant, ouvrons notre blueprint d'animation.

Et ouvrons cela.

D'accord, ici maintenant, nous mélangeons les espaces où que nous mélangeons les poses par bool ici.

Maintenant, si le joueur est mort, ils vont jouer l'animation d'inactivité.

Mais si le joueur est mort, ou si le joueur a gagné le jeu, nous allons toujours jouer l'animation d'inactivité.

Donc ici, nous allons avoir un booléen, ce que cela fait, c'est qu'il vérifie si l'une de ces valeurs est vraie, donc il prend deux valeurs booléennes.

Et si cela peut être collé beaucoup plus, cela peut prendre cinq, six, etc.

Mais nous devons simplement avoir ceux-ci.

Donc nous allons supprimer, puis supprimer la poêle ici si le joueur est mort, ou si le joueur a gagné, jouez l'animation du joueur mort.

Donc pour obtenir cela, convertissez en Batman, nous l'avons déjà fait.

À partir d'ici, nous allons obtenir un a clear one.

Déplacez cela tout en bas.

Et encore une fois, nous allons promouvoir cela à une variable, le nom est bien.

Et tout en bas.

Nous y voilà.

Cela semble un peu net.

AnimGraph placez cela ici.

Donc si l'une de ces conditions est vraie, nous allons jouer l'animation d'inactivité.

Donc si je joue maintenant le deuxième niveau un pour voir maintenant mes animations ne jouent pas en continu.

Donc je peux maintenant quitter le jeu.

Et cela fonctionne parfaitement bien.

Génial.

Maintenant, c'est à peu près tout pour ce jeu.

Votre défi est d'ajouter votre propre carte, essayez d'ajouter votre propre niveau, allez sur le marché, obtenez-y beaucoup d'actifs gratuits que vous pouvez utiliser.

Peut-être faites-en un vaisseau spatial et essayez cela.

Le seul problème maintenant est que, malheureusement, puisque Unreal Engine 5 est encore en développement, la plupart des actifs ne sont pas compatibles avec le moteur.

Donc si je retourne à mon lanceur Epic Games et que j'essaie d'ajouter cet actif gratuit que j'ai obtenu de la chose du mois gratuit, si je clique sur montrer tous les projets et que j'essaie de sélectionner Unreal Engine 5, vous pouvez voir qu'il dit que l'actif n'est pas compatible.

Donc ce que vous devrez faire, c'est que vous devrez rétrograder ce projet à Unreal Engine 5.

Et puis vous aurez Unreal Engine 4 et ensuite ajouter les actifs.

Mais le problème est que vous pourriez avoir beaucoup de problèmes après l'avoir mis à niveau à Unreal Engine 5, c'est pourquoi il est encore en accès anticipé.

Pas beaucoup d'actifs sont encore disponibles pour Unreal Engine 5, ce qui est dommage.

Oui, c'est un peu décevant, mais en même temps, ils ont spécifiquement mentionné que ce moteur est en accès anticipé.

Donc ne vous inquiétez pas trop, vous pouvez suivre le tutoriel exact que j'ai montré ici dans Unreal Engine 4, c'est la même fonctionnalité, les mêmes blueprints, tous fonctionnent parfaitement bien, c'est juste que l'UI peut sembler un peu différente.

Cela semble beaucoup plus moderne que Unreal Engine 4.

C'est la seule différence, c'est assez bien pour l'instant en ce qui concerne au moins les parties de base.

Donc ce tutoriel peut être suivi dans Unreal Engine 4, 2, donc ne vous inquiétez pas de cela.

Mais merci beaucoup d'avoir regardé.

J'espère vraiment que vous avez appris quelque chose et j'espère que vous avez pu vous familiariser avec Unreal Engine 5 et le développement de jeux.

Si vous avez terminé ce cours, c'est incroyable, essayez d'ajouter vos propres fonctionnalités.

Si vous voulez apprendre le C++, restez à l'écoute car j'ai un cours C++ qui arrive très, très bientôt, nous allons créer exactement le même jeu mais en C++, donc cela va être très, très amusant.

Mais merci beaucoup d'avoir regardé et je vous verrai très bientôt.

Au revoir et bonne chance.