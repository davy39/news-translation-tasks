---
title: Coder un jeu de course sans fin en utilisant Unreal Engine et C++
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-10-21T19:02:44.000Z'
originalURL: https://freecodecamp.org/news/code-an-endless-runner-game-using-unreal-engine-and-c
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/endless.png
tags:
- name: C++
  slug: c-2
- name: unreal-engine
  slug: unreal-engine
- name: youtube
  slug: youtube
seo_title: Coder un jeu de course sans fin en utilisant Unreal Engine et C++
seo_desc: 'Endless runner games can be fun and addicting. Also, an endless runner
  game is a great game development project for a beginner.

  We just released a course on the freeCodeCamp.org YouTube channel that will teach
  you how to create an endless runner game...'
---

Les jeux de course sans fin peuvent être amusants et addictifs. De plus, un jeu de course sans fin est un excellent projet de développement de jeu pour un débutant.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à créer un jeu de course sans fin en utilisant Unreal Engine et C++.

Fahir d'Awesome Tuts a créé ce cours. Farhir a créé une série de grands cours de développement de jeux et a un don pour enseigner aux débutants.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/giphy--3-.gif)
_J'espère qu'elle fera une pause bientôt._

Ce cours vous apprendra les bases d'Unreal Engine et vous préparera à créer des jeux encore plus compliqués.

Voici les sections de ce cours :

* Aperçu du jeu
* Création de la classe du joueur
* Création des obstacles
* Création du niveau
* Génération des niveaux
* Destruction du joueur et redémarrage du niveau

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/SOjZTmOMGcY) (2 heures de visionnage).

%[https://youtu.be/SOjZTmOMGcY]

## Transcription

(générée automatiquement)

Dans ce cours de développement de jeux, vous apprendrez à créer un jeu de course sans fin en utilisant Unreal Engine et le fichier c++ Fahir enseigne ce cours.

Il a créé une tonne de tutoriels de développement de jeux et il est un excellent enseignant.

Qu'est-ce qui se passe les gars, Fahir ici et de retour avec un autre tutoriel Unreal Engine, cette fois en c++ Oui, parce que beaucoup de vos doozy blows blows.

D'accord, je vais faire un tutoriel c++.

Bref, jetons un coup d'œil au jeu que nous allons créer.

Donc ici, j'ai mon éditeur, si je clique sur le bouton lecture, c'est un simple jeu de défilement latéral.

Donc si je, vous savez, saute et tout ça, vous voyez, nous pouvons sauter, nous pouvons bouger, le but est d'éviter ce mur qui nous poursuit car s'il nous touche, nous allons mourir.

Et bien sûr, nous allons avoir des obstacles le long du chemin, comme ces plateformes, comme les piques que nous espérons voir très bientôt, car ils ne se génèrent pas tout le temps.

Les voici, nous avons les piques.

Si nous touchons les piques, bam, nous sommes morts, le niveau va redémarrer.

Si le mur nous touche, bam, nous sommes morts, le niveau va redémarrer.

Comme vous pouvez le voir, cela ressemble à un jeu basique.

Mais nous allons apprendre beaucoup de choses cool, surtout en c++, car nous allons tout faire en c++ à partir de zéro, en codant tout, et vous allez me voir coder et, vous savez, vous allez apprécier cela et apprendre beaucoup et bla bla bla.

Bref, que puis-je dire d'autre ? Plongeons-nous dans cela.

Cours.

Oui, c'est un mini-cours.

Qu'y a-t-il d'autre ? Non, c'est un mini-cours.

D'accord, c'est un tutoriel mini-cours, peu importe, plongeons-nous dedans et créons le jeu scolaire.

D'accord, alors mon jeu se développe.

Maintenant que nous avons vu le jeu que nous allons créer, créons le jeu.

Donc ici, j'ai le navigateur de projets Unreal Engine, nous allons cliquer ici sur jeux.

Et au fait, ceci est la version quatre point 25 d'Unreal Engine.

Et nous allons sélectionner notre projet en troisième personne.

Donc pas celui vide, mais le troisième personne car nous avons besoin de certains éléments de ce package en troisième personne.

Et ici, nous allons cliquer sur Suivant.

Et à partir du blueprint, je vais cliquer sur la liste déroulante et sélectionner c++ car Yay, ceci est un cours c++.

Et ici, je vais nommer mon projet, je vais l'appeler side rather CPP.

Bien sûr, vous pouvez penser à quelque chose de plus créatif que cela, je vais cliquer ici Créer le projet et attendre que le projet soit créé.

Et puis je vais revenir.

Et nous y voilà enfin.

Donc maintenant, ce que nous allons faire, c'est créer le joueur et spécifiquement la classe du joueur ici, au fait, j'ai ce contenu du moteur, nous allons l'utiliser aussi.

Si vous ne l'avez pas, vous allez cliquer ici où il est écrit Options de vue.

Donc ceci que je dessine ici, cliquez dessus, et à partir de là, vous allez cliquer sur cette case à cocher montrer le contenu du moteur.

Donc assurez-vous que cela est coché.

Et alors vous pourrez voir ce que je vois dans mon projet.

Aussi une astuce sympa, si vous trouvez que tous ces éléments à l'intérieur de l'éditeur sont trop petits, surtout si vous avez un grand moniteur, vous pouvez aller ici sous fenêtre et puis outils de développement.

Et puis vous pouvez aller ici widget ou réflecteur.

Et laissez-moi simplement amener ce mauvais garçon ici.

Et ceci est l'échelle pour l'application.

Habituellement, je la règle à 1.16 et elle va redimensionner mon application, la rendre un peu plus grande et tout ça pour que je puisse voir mieux.

C'est tout ce qu'il y a à faire.

Bref, en allant ici dans le contenu, je vais faire un clic droit et créer un nouveau dossier que je vais appeler maps car ici nous allons créer une nouvelle carte et cela va se passer sous Fichier et le nouveau niveau, c'est-à-dire un nouveau niveau, j'ai dit map mais c'est la même chose Ctrl S pour l'enregistrer, je vais l'enregistrer ici et je vais l'appeler celui-ci gameplay et le voilà.

Donc la première chose que je vais faire avec ce gameplay, c'est que je vais supprimer le sol que nous avons ici, donc simplement le supprimer et le voilà.

Et ensuite, je vais aller ici dans géométrie et maillages et je vais prendre ce modèle et s'il vous plaît allez ici et le voilà.

Laissez-moi simplement positionner ce mauvais garçon, donc pour x, ce sera zéro, pour Y, ce sera zéro, z sera 20 et je vais aussi le redimensionner, donc je vais cliquer ici sur cette icône de cadenas pour verrouiller l'échelle et je vais dire point 25 et le voilà.

Redimensionnez-le et Wallah.

Aussi en ce qui concerne la position de départ du joueur, laissez-moi simplement cliquer dessus, oui, ce sera là où il est.

Et c'est ici que nous allons faire apparaître notre joueur.

Maintenant, avant de procéder à la création de la classe du joueur ici, à l'intérieur des paramètres du projet et dans l'entrée, nous allons avoir quelques mappages et axes.

Donc, en gros, nous n'avons besoin que des sauts, je vais supprimer cette réinitialisation, nous cliquons simplement ici sur cette x et la supprimons.

Ici, nous allons avoir déplacer à droite, nous n'allons pas avoir déplacer vers l'avant et toutes ces choses.

Donc, regarder vers le haut, taux de regard, tourner, taux de rotation et déplacer vers l'avant.

Nous allons supprimer tout cela et laisser seulement tout cela.

Bien sûr, vous pouvez aussi filtrer ceux-ci, donc nous n'avons pas besoin du GamePad, j'ai besoin en gros seulement de la barre d'espace.

Mais encore une fois, cela dépend de vous, selon si vous voulez créer, peut-être que vous voulez pratiquer ou autre chose, je ne sais pas, je ne suis pas vous, je ne sais pas, je ne vous contrôle pas et tout ça.

Donc, voilà.

Donc nous devrions avoir sauter et déplacer à droite pour le travail, nous avons la barre d'espace pour le déplacement, à droite A et D, vous pouvez aussi ajouter, vous pouvez aussi ajouter la gauche et la droite, c'est totalement à vous, je ne vais pas entrer là-dedans, vous savez, ne me jugez pas.

Donc maintenant nous pouvons aller ici à l'intérieur de notre c++ ou classes c++.

Et à partir de là, voilà.

Ici nous avons notre side runner CPP character, je ne vais pas utiliser celui-là, je vais simplement faire un clic droit et aller ici Nouvelle classe c++, elle va hériter du character, je vais cliquer sur Suivant.

Et je vais appeler celui-ci runner character et cliquer sur Créer la classe.

Bien sûr, vous savez que cela prend un certain temps pour qu'Unreal Engine compile et charge tout cela, je vais obtenir un m deux SSD juste à cause de cela, comme je ne l'obtiens pas juste à cause de cela, j'obtiens un es m deux, excusez-moi SSD qui peut lire pour je crois, trois 3500 mégaoctets par seconde.

Donc c'est ce que je vais obtenir.

D'accord, c'est ce que je vais obtenir.

Et enfin, voici ma classe.

Donc nous avons le fichier runner.h et le fichier runner.cpp.

Si vous ne connaissez pas la différence entre les deux, je vais expliquer rapidement, donc dans le fichier .h, nous déclarons tout ce dont nous avons besoin et à l'intérieur de notre fichier .cpp, nous codons ensuite tout ce que nous avons déclaré, c'est simple.

Oui, c'est le cas.

Donc, qu'avons-nous besoin ici, juste en dessous de l'endroit où il est écrit notre corps généré, je vais déclarer une propriété u.

Donc c'est prah per T, voilà.

Parfois, je ne peux pas épeler et je vais l'appeler visible partout, voilà.

Et celui-ci va être notre classe.

Cela s'appelle une déclaration anticipée lorsque vous tapez une classe afin de ne pas avoir à inclure le fichier ici.

Et je vais dire composant de caméra, et c'est un pointeur.

Donc nous devons le noter avec l'étoile.

Et je vais appeler celui-ci caméra de vue latérale.

Maintenant, comme je l'ai dit, cela s'appelle une déclaration anticipée ou une déclaration anticipée, je crois, je ne suis pas sûr à 100%, parce que je ne suis pas bon avec ces noms, je m'en fiche.

Mais essentiellement, quel est le but de cela, c'est que nous le déclarons avec une classe ici afin de ne pas avoir à utiliser l'inclusion ici, vous voyez, parce que chaque chose que nous utilisons, par exemple, si nous voulons utiliser des fonctions du personnage, nous devons inclure le personnage du cadre de jeu.

Mais je ne veux pas faire cela pour le composant de caméra parce que chaque fois que vous incluez le fichier runner.h n'importe où dans votre classe ou dans n'importe quelle autre classe, il inclura toutes les inclusions qui viennent avec lui, mais lorsque vous l'utilisez comme cela, alors il ne les inclura pas.

Mais à l'intérieur de ici runner.or runner character.cpp, alors nous allons l'inclure et c'est la meilleure façon de procéder.

Donc ici, c'est vous savez, le constructeur pour notre personnage au Begin Play et tout le bon truc tick et set up player input components, donc nous ne allons pas toucher à aucun de ceux-ci.

Au lieu de cela, ce que je vais faire, c'est ici protégé.

Et ici, je vais déclarer mes propres fonctions et variables.

Premièrement, je vais déclarer ici void move right et celui-ci va prendre une valeur float comme paramètre.

Et bien sûr, à un moment donné, cela va commencer à se plaindre avec une ligne verte sous ce move right parce que nous le déclarons ensuite à l'intérieur du fichier .cpp.

Ne vous inquiétez pas pour cela, nous le ferons dans quelques instants.

Donc ici, nous allons également créer un public et celui-ci va retourner notre composant de caméra et encore une fois, c'est un pointeur et je vais appeler celui-ci get side view.

Donc get side view camera component.

Et celui-ci va prendre une constante ou en fait c'est une constante et il va retourner les caméras de vue latérale, simple comme cela.

Ensuite, nous allons avoir une autre fonction publique que je vais appeler void re start level, cela va se produire à la fin lorsque notre joueur se fait tuer, ce que nous avons vu également.

Aussi ce que je vais créer et c'est ce que j'ai dit va se plaindre avec cela, ne vous inquiétez pas, nous allons l'implémenter dans une vue.

Ici, je vais créer une fonction u.

Et celle-ci va être notre void on over lap begin, elle va prendre un u primitive.

Donc, la composante primitive, qui est un pointeur et je vais appeler celle-ci composante chevauchée, virgule.

Elle prend également un acteur A, simplement un acteur, mais il est orthographié a acteur.

C'est un pointeur et je vais appeler celui-ci autre acteur.

Voilà, nous allons également prendre une autre composante primitive.

Donc, je vais copier cela ici et le coller et c'est un pointeur.

Donc, encore une fois, nous devons utiliser cette étoile ici.

Et autre comp ou autre composante, cela je vais l'appeler prend un int 32.

Autre index de corps, un booléen B de balayage.

Et enfin, une constante de F hit result.

Et ici, le résultat du balayage, voilà.

Et enfin, quelques variables privées supplémentaires, l'une sera la position Z.

Donc, float z, la position, voilà, c'est la position comme cela, nous allons également prendre un F vector, qui sera notre position temporaire que je vais noter est égal à f vector comme cela.

Et enfin, un booléen pour noter si nous pouvons bouger ou si nous ne pouvons pas bouger.

Maintenant, bien sûr, ici, comme vous pouvez le voir, il se plaint pour le move right et le restart level, il ne se plaint pas pour le on overlap again, mais il va commencer à se plaindre parce que j'attends toujours que ce SSD arrive.

Donc ce que nous devons faire, c'est déclarer cette fonction ici à l'intérieur de notre fichier runner character dot cpp.

Donc nous devons, comme je l'ai dit, la déclarer et cela peut se faire en allant ici et en déclarant et en tapant yet vous savez, void a runner character call on call on et ainsi de suite.

Mais il y a un moyen plus rapide de faire cela, ce que nous pouvons faire, c'est cliquer sur ce move right, puis je peux faire un clic droit, et ensuite je peux aller ici actions rapides et refactorisation.

Et ici, je peux dire créer une déclaration de définition.

Et voilà.

Lorsque je clique sur cela, cela va le créer, bien sûr, vous savez, ce disque dur HDD, il me rend fou.

Et je devrai probablement couper cette vidéo parce que, vous savez, si je chante pour vous, cela vous coûtera extra.

Je veux dire, cela est sur YouTube, vous ne payez rien pour cela.

Mais voilà, enfin, d'accord, donc maintenant si je vais ici dans le runner, le voilà.

Donc nous avons le void runner move, right, nous pouvons faire la même chose pour cela ici.

Donc nous pouvons, vous savez, faire la même chose pour le restart level en tapant void a runner character call on call on will ride.

Mais au lieu de cela, je vais simplement faire un clic droit à nouveau, actions rapides et refactorisation.

Et je vais créer une définition pour cela.

Et enfin, nous devons faire cela pour on overlap begin.

Donc actions rapides refactorisation créer une déclaration, voilà, enregistrer cela ici, enregistrer cela ici, et voilà, voici les fonctions dont nous avons besoin.

Donc à partir d'ici, voilà.

Donc que allons-nous faire en ce qui concerne notre runner character ? Eh bien, pour notre runner character, voici où j'ai dit que nous allons ajouter ces inclusions.

Donc la première que je vais inclure, et celle-ci va être components, voilà, c'est come ponents et puis une barre oblique inverse et celle-ci va être capsule component dot age, et je vais inclure tout ce que nous allons utiliser donc ici nous allons également inclure entre guillemets, game frame work, et puis une barre oblique inverse spring, en fait nous n'avons pas besoin du composant spring, nous avons besoin de la caméra donc je me suis emporté habituellement quand on utilise la caméra on utilise le bras spring mais je vais simplement utiliser la caméra sans lui.

Donc camera dash ou barre oblique inverse camera component dot h, voilà.

Et aussi inclure et ici game frame work.

Donc game frame work, en fait, oui, c'est Capital Framework comme cela.

Et barre oblique inverse character, movement component.

Et voilà, en fait, j'ai pensé Ah, et maintenant voilà.

Donc c'est ou ce sont les inclusions dont je parlais quand j'ai déclaré à l'avance le composant de la caméra.

Donc au lieu d'utiliser cette inclusion de composant de caméra ici, je vais simplement la déclarer à l'avance comme ceci.

Et puis ici, je vais utiliser l'inclusion parce que si nous devons utiliser le runner character dans une autre classe et que nous devons inclure le fichier runner character dot h, quand nous incluons cela, il n'inclura pas cette importation parce que cette importation est à l'intérieur du fichier dot cpp.

Donc ici, à l'intérieur de notre runner character, qui est le constructeur en gros, ce que nous allons faire en premier, c'est définir le composant capital, donc je vais dire get capsule component.

Et à partir de là, je vais dire in it capsule size et la taille va être 42 sur l'axe X et 96 sur l'axe Y, voilà.

Je vais aussi définir le canal pour répondre à la collision avec chevauchement, en définissant les paramètres de collision pour répondre avec chevauchement.

Donc ici, je vais dire get capsule components ou get the capsule, capsule component, voilà.

Et ici, je vais dire set collision response to channel.

Et à partir d'ici, en descendant, je vais dire ECC underscore game trays channel, et il va être traced channel one.

Et je vais dire a CR, over lap, voilà.

Et en avançant, nous allons noter que nous n'allons pas permettre au contrôleur de nous faire tourner, au lieu de cela, nous allons utiliser notre propre ou en gros nous allons contrôler cette classe à partir de celle-ci.

Donc je vais dire ici be use control rotation pitch, qui va être égal à false.

Je vais aussi simplement copier cela et le coller, coller, coller et celui-ci va être pitch puis nous aurons le rôle.

Et enfin, nous aurons le yard, en gros, comme je l'ai dit, cela ne permettra pas au contrôleur de tourner, le contrôleur ne va pas faire tourner ce personnage, au lieu de cela, nous allons le faire à partir de cette classe.

Et puisque c'est un défilement latéral, nous n'allons pas tourner du tout.

Ensuite, je vais créer la caméra, donc notre caméra de vue latérale va être égale à create default sub object et elle va être de type view camera component comme cela.

Et je vais lui donner un nom en passant ici un texte.

Et ce nom va être side view camera, simple comme cela, voilà.

Rien de compliqué, je vais aussi ou je ne veux pas que le contrôleur fasse tourner la caméra non plus.

Donc je vais dire side view camera.

Et ici, je vais dire be use pan control rotation qui va être false.

Donc cela ne permettra pas au contrôleur de faire tourner la caméra.

Ensuite, je vais définir le mouvement du personnage pour faire face à la direction dans laquelle nous nous déplaçons, donc nous nous déplaçons vers ou dans ce cas, parce que le jeu est un défilement latéral, nous pouvons avancer ou reculer.

Donc c'est pourquoi je vais dire ici, get character movement.

Et à partir de là, je vais dire be orient rotation.

Donc orienter la rotation vers le mouvement, ce qui va être égal à true, ce qui va nous permettre, comme je l'ai dit, de tourner vers la direction où nous allons.

Maintenant, cela va être les taux de rotation, je vais dire get character movement, mais je vais le copier parce que nous allons l'utiliser quelques fois ici.

Et je vais voir ici un taux de rotation.

Et cela va être égal à App rotate or, et ici je vais dire zéro pour l'axe X, 720 pour l'axe Y et 0.0 F pour l'axe Z. Maintenant, si quelqu'un est confus, si c'est la première fois que vous voyez du code Unreal Engine en C++, premièrement, je vous conseille de suivre ma série de tutoriels C++ ici sur YouTube.

Vous aurez cela dans mon Académie aussi.

Mais ce que je voulais dire, c'est que si vous êtes confus pourquoi j'utilise ici 0.0.

Mais ici 720 point et je n'ajoute pas zéro, quelle est la différence ? Eh bien, il y a vous, il n'y en a pas en fait, donc vous pouvez ajouter zéro, vous pouvez émettre zéro, c'est exactement la même chose.

Donc c'est pour le taux de rotation que je vais pointer zéro ici et déplacer cela en arrière, et voilà.

Donc ensuite, nous allons définir l'échelle de gravité pour nos personnages.

Donc je vais dire gravity scale qui va être égal à deux.

Je vais aussi définir le contrôle aérien, donc le contrôle aérien va être égal à zéro point f, le contrôle aérien est essentiellement comment ou combien de contrôle avons-nous sur notre personnage pendant qu'il est dans les airs, plus le nombre est élevé, plus le contrôle est élevé.

Ensuite, nous allons aussi dire ici, notre jump z velocity va être égal à 1000.

Cela va être essentiellement, vous savez, à quelle distance ou à quelle hauteur nous pouvons sauter.

Ensuite, ici, je vais dire ground reaction va être égal à trois.

Et ground friction est essentiellement, vous savez, la collision avec le joueur et le sol.

Aussi ici, je vais définir la vitesse de marche maximale qui va être égale à 600.

Et enfin, la vitesse de vol maximale qui va être égale à 600.

Et voilà.

Et maintenant, nous allons obtenir nos positions temporaires et nous dirons temp pose qui va être égal à get actor location, qui est l'emplacement actuel de notre acteur ou essentiellement le personnage du jeu et j'ai besoin de cette position temporaire parce que je vais dire que notre variable de position z va être égale à temp, position z plus 300.0.

Voilà.

Et maintenant, que devons-nous faire, nous devons lier, nous devons lier nos contrôles si nous voulons déplacer le personnage.

Donc ici, nous avons notre set up player input.

Et c'est ici que nous allons lier les axes et le saut et tout le bon truc.

Donc maintenant nous avons ce composant player input qui est passé ici dans le setup input component.

Donc je peux simplement l'utiliser.

Et je peux dire, player input component, qui est, vous savez, appelé comme vous pouvez le voir, pour lier la fonctionnalité à l'entrée.

Donc je vais dire ici, bind action.

Donc bind action, et je vais lier l'action de saut et où ou quoi, où ai-je cette action de saut ? Eh bien, l'action de saut est ici, si je vais dans le projet, la voici, action mappings.

Et c'est l'action de saut.

Donc ce nom doit correspondre au nom que nous spécifions ici.

Donc liez cela à.

Et bien sûr, parce que c'est une action, nous pouvons l'appuyer et la relâcher.

Donc je vais dire IE pressed, en gros, que voulons-nous faire lorsque nous appuyons sur le bouton de saut ? Eh bien, ici, nous allons le lier en passant cela aussi.

Et ici, un personnage appelle on appelle on jump, voilà.

Donc essentiellement, lorsque nous appuyons sur le bouton de saut, ou dans notre cas, le bouton de saut est désigné par la barre d'espace.

Donc lorsque nous appuyons sur la barre d'espace, nous allons appeler la fonctionnalité de saut du personnage que nous avons hérité.

Parce que cette classe hérite du personnage, voyez ici public a character.

Et le personnage a certaines fonctionnalités intégrées comme le saut.

Donc je vais aussi copier cela parce que lorsque nous le relâchons, nous allons donc c'est I II pressed et ici, ie released.

Donc lorsque nous relâchons le bouton de saut, au lieu de sauter, nous allons arrêter de sauter, cela va arrêter le saut du joueur et il va commencer à tomber, simple comme cela.

Ensuite, je vais prendre le composant player input, et maintenant je vais lier les axes au lieu de lier l'action et je vais lier le move right.

Et je vais le lier à ceci en faisant référence à cette classe et en faisant référence à l'appel a runner character call on call on move right ? Voici.

Donc ceci ici va se lier au move right, qui est encore, en revenant ici, c'est ce move right, il va se lier à notre fonction move write, qui est cette fonction ici.

Donc essentiellement maintenant, ici dans notre move right, nous allons ajouter le code qui va déplacer le joueur.

Donc ici, nous allons tester si can move et nous allons utiliser ceci pour noter si le joueur peut bouger quand il est mort, nous verrons cela plus tard.

Mais si le joueur peut bouger, nous allons dire add movement input.

Et à partir de là, je vais dire f vector.

Donc c'est f vector, et ici, zéro mouvement sur l'axe X, sur l'axe Y, ce sera un et sur l'axe Y ou en fait sur l'axe Z, ce sera aussi zéro, ici, je vais passer la valeur que nous avons.

Maintenant, pour que cela fonctionne, nous devons noter à l'intérieur de notre Begin Play que can move.

Donc can move va être égal à true.

C'est lorsque nous commençons notre jeu, ce qui est, vous savez, normal et tout le bon truc, sinon cela ne fonctionnera pas.

Donc je vais maintenir Ctrl Shift et appuyer sur B, cela va compiler mon code.

Et bien sûr, nous allons attendre quelques instants.

Je ne sais pas, peut-être que je vais couper cette vidéo en fonction du temps que cela prendra.

Parce que encore une fois, mon SSD est le lot ici, je peux aussi essayer de synchroniser avec vous, non, et puis et puis et puis voilà.

Cela a fonctionné.

Vous voyez ici, build succeeded, ce qui signifie que maintenant nous pouvons aller à l'intérieur de notre éditeur.

Et si je devais aller dans le gameplay et appuyer sur le bouton lecture, nous voyons un personnage et nous pouvons déplacer le personnage, mais ce n'est pas le personnage her.

C'est celui intégré que nous avons créé avec le projet.

Donc pour créer notre propre personnage, je vais faire un clic droit ici et aller dans le nouveau dossier.

Je vais l'appeler do some blueprints.

Et à partir d'ici, je vais cliquer et entrer dans ce dossier et je vais créer une classe de blueprint et je vais hériter du runner character.

Donc voici mon runner character et je vais cliquer sur celui-ci et je vais dire BB runner character.

Donc c'est maintenant notre personnage.

Cela va créer notre personnage à partir de la classe que nous venons de créer.

Bien sûr, comme vous pouvez le voir, nous n'avons rien.

Nous avons la caméra de vue latérale, vous voyez, nous l'avons créée ici, mais ce que nous devons faire, c'est cliquer sur le maillage et ici, nous devons ajouter le Skeletal Mesh, qui sera essentiellement notre mannequin, qui est ce mauvais garçon ici, je vais aussi définir sa position z à moins 97 pour le descendre un peu comme vous pouvez le voir, et je vais le faire tourner de 90 ou moins 90 degrés comme cela.

Et en gros, ce serait tout.

Je peux compiler, enregistrer cela, bien une chose de plus que nous devons attacher ici, une classe de blueprint pour son animation, qui à nouveau, cliquez sur la liste déroulante et nous avons le third person an MVP, qui automatiquement le fera ou il sera animé.

Maintenant, pour ajouter notre personnage dans le jeu, nous devons créer notre propre mode de jeu car si vous vous souvenez du tutoriel précédent, de la série de tutoriels Unreal Engine précédente, ici, à l'intérieur des maps et modes, vous voyez, nous devons créer notre propre mode de jeu.

Parce que actuellement, encore une fois, si je clique sur le bouton lecture, ce n'est pas notre personnage.

Voyez, ce n'est pas le personnage que nous voulons.

Au lieu de cela, ici, je vais faire un clic droit et blueprint class, et je vais filtrer à partir du mode de jeu ou filtrer pour le mode de jeu et cliquer ici et hériter du mode de jeu, ce sera notre BP runner ou side runners, excusez-moi, side runner underscore game mode.

Et allons ici dans les paramètres du projet et sélectionnons le BP side runner game mode.

Et ici, au lieu du pawn par défaut, je vais sélectionner le BP runner care Rector.

Et enfin, cela va nous permettre d'avoir notre propre personnage dans le jeu.

Donc si je clique sur le bouton lecture, le voilà, si je l'incarne, nous avons un problème.

Vous voyez, nous ne voyons pas le personnage, nous ne voyons rien.

Et la raison en est que nous pouvons le déplacer, je ne sais pas si vous remarquez, faites attention à l'endroit où il se trouve actuellement, si je l'incarne, et si je bouge comme cela, je bouge.

Et essayons de voir où il se trouve maintenant.

Vous voyez, il est presque tombé.

Donc le voilà.

D'accord, donc que devons-nous faire pour que cela fonctionne ? Eh bien, nous devons revenir dans notre classe c++, et ici où il est écrit le tick.

Donc à l'intérieur de la fonctionnalité arctique, nous devons dire notre temp position.

Donc temp p o S va être égal à get actor location, encore une fois, nous obtenons l'emplacement de l'acteur, notre temp position que x va être égal à ou nous allons soustraire de lui 850 comme ceci, et sur la position Z, donc temp position que z va être égal à z position.

Donc z position.

Et enfin, notre caméra de vue latérale set world location ici, nous allons passer la temp position, et voilà.

Donc ce que cela va faire, c'est encore une fois obtenir l'emplacement actuel de l'acteur, l'emplacement actuel de l'acteur est essentiellement, eh bien, l'emplacement de l'acteur, juste en l'obtenant, mais l'emplacement actuel est l'emplacement de notre propre acteur, du personnage, nous allons ensuite changer l'exposition, donc soustraire de lui 850, et la position Z va rester celle que nous avons ici, et ensuite nous allons définir cette position à la position du monde de la caméra.

Donc Ctrl Shift B afin de compiler cela.

Et au fait, je ne vais pas le faire, mais vous allez le faire si vous voulez voir le résultat, par exemple, si vous changez ce nombre à moins 1000, moins 100, la position Z ici, je ne sais pas, plus 500.

Essayez-le, voyez le résultat, ce sera, vous savez, ce sera notre pratique, vous comprendrez mieux, donc si je clique sur le bouton lecture maintenant, le voilà.

Vous voyez ici notre personnage, il tombe, regardez cela, nous mais s'il tombe comme cela, nous ne pouvons plus le voir.

Donc c'est tout ce qu'il y a à faire.

Bref, encore une fois, cliquez sur le bouton lecture, nous pouvons incarner le personnage, regardez cela, nous pouvons bouger ici, nous pouvons bouger ici.

C'est le point, vous voyez, et il tourne vers la direction où nous nous déplaçons.

Si nous nous déplaçons en arrière, vous voyez, il tourne pour se déplacer en arrière.

Si nous nous déplaçons en avant, il tourne pour se déplacer en avant.

Le voilà, nous pouvons appuyer sur base pour sauter comme cela.

Le voilà.

Mais le problème est que nous n'avons que cette seule plateforme.

Comment sommes-nous, ce que nous devons faire, eh bien, nous devons créer plus de plateformes, c'est logique.

Donc à partir de la vidéo suivante, nous allons préparer tout pour commencer à créer nos parties de niveau et puis nous allons bien sûr commencer à encoder tout cela afin que nous puissions avoir notre niveau pour jouer au jeu.

Si quelque chose n'était pas clair en ce qui concerne cette vidéo, assurez-vous de demander dans les commentaires ci-dessous et je vous aiderai et je vous verrai dans la prochaine vidéo.

D'accord, alors mon jeu dev ELS avant de pouvoir créer notre niveau, nous devons également créer les obstacles car ils vont faire partie du niveau.

Donc ici, dans notre classe c++, je vais créer une nouvelle classe c++ et elle va hériter de l'acteur.

Donc l'une d'entre elles va s'appeler obstacle.

Donc ici, je vais voir l'appel.

Et bien sûr, attendre qu'Unreal Engine l'ajoute au projet à nouveau, ce SSD va arriver lundi ou jeudi, mardi, car maintenant c'est samedi pour moi qui enregistre cela.

Je vais chanter pour vous en attendant, puis et puis et puis et puis et puis et puis et puis et puis et puis et puis et puis et puis merci beaucoup, cela sera 5 $ supplémentaires.

Maintenant, la mauvaise nouvelle est que nous devons en créer un autre.

Donc je fais un clic droit ici, Nouvelle classe c++, et cette fois un acteur à nouveau et celui-ci va être spikes.

Donc spikes, voilà, appuyez sur entrée, bien sûr et attendez qu'il nous torture.

Que puis-je dire d'autre ? La bonne chose est que nous n'allons pas coder quoi que ce soit.

Au lieu de cela, nous allons simplement utiliser ces classes afin de pouvoir, vous savez, faire un cast plus tard lorsque nous entrerons en collision avec ces objets, bien sûr, à partir des blueprints que nous créerons.

Donc ici, si je l'ouvre, laissez-moi simplement recharger tout, recharger à nouveau.

Voilà.

Donc nous avons les spikes, nous avons l'obstacle.

Mais comme je l'ai dit, nous n'allons pas coder quoi que ce soit ici.

Au lieu de cela, nous allons simplement utiliser ceux-ci comme références pour créer des blueprints.

Donc retournons dans notre Unreal Engine, et ici dans les blueprints, je vais faire un clic droit, un nouveau dossier, et je vais appeler celui-ci obstacles.

Et à l'intérieur des obstacles, je vais créer une classe de blueprint, l'une va hériter de l'obstacle, qui est ce mauvais garçon.

Et je vais l'appeler BB obstacle.

Simple, très simple, clic droit à nouveau, classe de blueprint.

Et ici, l'une va hériter des spikes.

Et je vais l'appeler BP underscore spikes.

Simple.

Double-cliquez dessus, ouvrez-le dans notre éditeur ici, j'ai presque dit Visual Studio, mais c'est en fait l'éditeur à nouveau.

Donc que allons-nous faire ? Eh bien, premièrement, pour les spikes, je vais cliquer sur ce BP spikes et ajouter un composant de maillage statique que je vais simplement appeler spike, très simple.

Maintenant, pour le maillage statique de spike ici, je vais cliquer sur la liste déroulante et filtrer pour nos quad pyramids.

Je vais dire quad pyramids, voilà, c'est celui que nous voulons.

Et ici pour les matériaux, je vais filtrer pour le clay new, et c'est celui que nous voulons.

Voilà.

C'est à peu près tout sauf ici, je vais le définir à moins 50 sur la position Z, aussi simple que cela.

Et aussi en ce qui concerne la collision, nous allons faire une chose intéressante.

Premièrement, je vais compiler et enregistrer cela et je vais aller ici dans les paramètres du projet.

Et je vais aller ici dans la collision pour les paramètres du projet.

Donc c'est essentiellement ceci ici sous moteur lorsque vous allez dans les paramètres du projet.

Ici, nous pouvons créer nos propres canaux d'objets.

Qu'est-ce que cela signifie ? Cela signifie essentiellement que nous pouvons créer nos propres couches pour différencier la collision entre les acteurs.

Donc ici, je vais cliquer sur nouveau canal d'objet, et le nom pour celui-ci sera obstacle et l'obstacle va bloquer.

Donc l'obstacle va simplement bloquer le joueur, c'est essentiellement un corps solide ne permettant pas au joueur de passer à travers.

Et c'est ce qu'est un bloc.

Et je vais cliquer ici sauf suivant ici, je vais dire nouveau canal d'objet et celui-ci sera notre spike, mais le spike va chevaucher, le spike va chevaucher afin que nous puissions chevaucher dans la détection de collision entre le spike et le joueur.

Je vais cliquer ici sauf donc maintenant nous avons les canaux de bloc et de chevauchement ici.

Qu'est-ce que cela signifie ? Cela signifie maintenant que je peux aller à l'intérieur des spikes ici et faire défiler vers le bas ici où il est dit la collision, voilà, ce mauvais garçon ici, je peux zoomer pour que vous puissiez voir, voilà.

Donc ici le préréglage de collision.

Je vais le définir sur personnalisé, donc cliquez sur la liste déroulante et cliquez ici sur personnalisé dans la liste.

Ici, nous allons avoir la collision de retour à query only.

Donc nous allons avoir query only, pas de collision physique, car nous ne voulons pas de la physique, nous ne voulons pas entrer en collision en tant qu'objet physique avec notre pyramide ou essentiellement le spike, et ici pour le type d'objet.

Maintenant, nous allons avoir, donc laissez-moi simplement compiler et enregistrer cela.

Donc maintenant, nous devrions voir le spike et l'obstacle que nous venons de créer ici.

Si vous ne le voyez pas tout de suite, compilez et enregistrez simplement votre blueprint.

Et puis ici, à partir du type d'objet où il est dit world dynamic, vous pouvez sélectionner celui-ci pour être spike, et voilà.

Donc ici, je vais définir notre spike pour chevaucher tout sauf ici l'obstacle, je ne veux pas qu'il chevauche l'obstacle et nous pouvons aussi définir ici pour ne pas chevaucher ou simplement ignorer la caméra car nous n'avons pas besoin de la caméra, compilez et enregistrez cela.

Donc il va chevaucher tous ces autres.

Réponses telles que le pawn physics body, qui est essentiellement notre joueur, nous allons le définir pour être un pawn.

Donc ceci ici pourra chevaucher avec le joueur.

Et bien sûr, nous détecterons alors la collision entre eux et nous détruirons le joueur et tout ce bon truc.

Donc maintenant nous pouvons passer à notre cube ou à l'obstacle qui est celui-ci et encore une fois, à partir d'ici, le composant statique, nous allons filtrer pour notre maillage statique, et je vais appeler celui-ci cube ou simplement l'appeler block obstacle, voilà.

Ici, pour le maillage statique, je vais filtrer pour le cube.

Donc tapez simplement cube et voilà, où est le QB QB.

Le voilà, voici le QB QB.

Et ici, pour le matériau, je vais dire basic shape material.

C'est ce que je veux, compilez et enregistrez cela.

Maintenant, je vais le laisser à 000 pour X, Y et Z et je ne vais pas toucher la rotation, je veux dire qu'il n'y a aucun intérêt à toucher la rotation car ce sera toujours la même chose, c'est un cube.

Et en revenant ici, encore une fois pour le préréglage de collision au lieu de block all dynamic, nous allons le définir sur personnalisé ici, la collision activée sera query et physics car encore une fois, cet obstacle, cet obstacle de bloc, il va être un corps solide et il va bloquer le joueur lorsque le joueur entre en collision avec lui, le joueur ne pourra pas le traverser.

Et ici, pour le type d'objet, nous allons le définir pour être un obstacle et nous allons le définir pour bloquer tout sauf ici pour spike, nous n'avons pas besoin qu'il bloque le spike, vous pouvez simplement chevaucher ce spike, mais il va bloquer tout, ce qui signifie qu'il est un corps solide, je vais simplement compiler et enregistrer cela et voilà.

Donc c'est à peu près tout en préparation pour la création de nos parties de niveau.

Maintenant, bien sûr, si quelque chose n'était pas clair, assurez-vous de demander dans les commentaires ci-dessous et à partir de la vidéo suivante, nous allons construire nos pirates de niveau et le niveau et tout le bon truc, puis nous allons commencer à les faire apparaître et bla bla bla.

Donc je vous verrai dans la prochaine vidéo, ce serait le début du jeu ici EDA qui avance maintenant, nous allons créer nos niveaux et pour cela, nous allons aller à l'intérieur de nos classes c++ et faire un clic droit et construire une classe de niveau de base qui va hériter de l'acteur et je vais appeler celle-ci ici, base level et appuyer sur entrée pour créer la classe et bien sûr, nous devrons attendre un moment ou deux ou un gazillion de moments pour qu'Unreal Engine fasse preuve de pitié envers nos âmes mortelles.

Jusqu'à ce que nous oublions l'homme SSD, plus vous regardez ces vidéos, plus je reçois de revenus publicitaires, je suppose, et plus je peux acheter ce SSD rapidement.

Je plaisante, mais allons-y et rechargeons tout, voilà.

Ici, nous avons notre base level dot age et ici nous avons notre base level dot cpp, donc à l'intérieur de notre dot h, la première chose ici en haut à droite en dessous des inclusions, je vais déclarer la classe you box bone et comme je l'ai dit, cela s'appelle la déclaration anticipée afin de ne pas avoir à utiliser l'importation ou l'inclusion, excusez-moi.

Maintenant, en revenant ici en bas à droite en dessous du public virtuel void, je vais créer protégé et je vais créer une nouvelle propriété.

Et cette propriété u va être blueprint read and write, elle sera également editable anywhere.

Donc edit anywhere.

Et enfin, je vais la définir sous une catégorie qui sera égale à triggers comme cela.

Qu'est-ce que c'est que ce professeur, je ne sais pas, je suis confus, je veux vous gifler, écoutez, écoutez et ne me giflez pas.

D'accord, donc ce que nous avons ici, c'est blueprint read and write, ce qui signifie essentiellement que le composant que nous déclarons maintenant, qui va être un composant you box, qui est un pointeur, donc j'ai besoin d'ajouter une étoile ici.

Et je dois l'appeler un trigger, ce qui signifie que ce composant trigger peut être lu et écrit, nous pouvons l'éditer et nous pouvons obtenir une valeur de celui-ci à l'intérieur du blueprint, edit anywhere signifie que nous pouvons l'éditer à l'intérieur de l'éditeur de blueprint sur le côté dans l'onglet détails.

Et la catégorie triggers signifie essentiellement que lorsque nous recherchons ce composant dans le code du blueprint, nous le trouverons sous la catégorie triggers.

Donc nous pouvons aussi l'appeler my triggers, vous pouvez l'appeler comme cela et nous le verrons lorsque nous le recherchons.

Donc ce que je vais faire, c'est copier cela et le coller en dessous parce que nous allons avoir la même signature, mais cette fois nous n'allons pas appeler celui-ci trigger mais je vais l'appeler spawn location comme cela.

Et enfin, nous allons avoir deux fonctions publiques, donc public comme cela.

Et ce qui va se passer ici, ces fonctions vont retourner un composant u box qui est un pointeur, donc celui-ci va être get trigger qui va obtenir notre trigger, pas Teague.

C'est un trigger, et un autre pour le composant u box.

Et c'est un pointeur.

Donc ici, je vais dire get spawn location comme cela.

Et voilà.

Maintenant, ne vous inquiétez pas si cela est encore du texte blanc, vous savez, cela prend du temps pour que le moteur Unreal compile cela.

Pendant que nous attendons ce SSD, vous comprenez ce que je veux dire, je vais faire un clic droit sur ce mauvais garçon, actions rapides et refactorisation, je vais créer une déclaration pour cela ici, faire la même chose, actions rapides, refactorisation, créer une déclaration pour cela.

Et bien sûr, je ne sais pas quoi dire, je veux dire, vous voyez, vous voyez les problèmes que nous avons tous.

Donc à l'intérieur de notre CPP, c'est là que nous allons inclure la même chose que ce que nous faisons avec nos joueurs.

Donc inclure, et je vais inclure components, barre oblique inverse box component dot h, c'est cet âge, voilà.

Et à l'intérieur de notre Begin Play, je vais d'abord tester si le trigger, s'il n'est pas égal à null PTR, ce qui signifie un pointeur nul, alors je vais dire trigger.

Et à partir de là, je vais dire be hidden in game qui va être égal à true et ne pas permettre à ce trigger d'être, vous savez, visible dans le jeu en direct, compilez simplement tout cela, afin que nous soyons sûrs que rien ne va mal, et que tout devrait fonctionner parce qu'il ne me donne pas à compléter l'argument, quoi que ce soit, vous voyez, build succeeded, nous sommes bons à partir.

Mais vous savez, cela prend du temps à Unreal Engine, je devrai probablement redémarrer ou fermer mon Visual Studio et l'ouvrir pour que cela fonctionne.

Je ne sais pas, ne me demandez pas ici maintenant, allez retourner un pointeur nul, au lieu de cela, je vais retourner un trigger.

Et ici, je ne vais pas retourner un ancien pointeur, au lieu de cela, je vais retourner un spawn location.

C'est tout ce qu'il y a à faire.

Et encore une fois, assurez-vous de compiler ou de construire cela.

Donc c'est Ctrl, Shift B pour construire ce code.

Et voilà.

Bien sûr, une autre façon de construire ce code est d'aller ici et de simplement cliquer sur Compile, cela fait exactement la même chose.

Mais je ne vais pas le faire.

Sinon, nous allons attendre beaucoup.

Donc allons ici à l'intérieur de nos blueprints, et faites un clic droit et créez un nouveau dossier, et celui-ci va être nos niveaux à l'intérieur du dossier niveaux, je vais faire un clic droit et créer une classe de blueprint et hériter de la base level, voilà et sélectionner je vais appeler celui-ci BP level one, bien sûr, nous allons avoir level two jusqu'à level 10.

Et ce qui va se passer dans celui-ci, je vais l'ouvrir et je vais créer quelques niveaux.

Et puis je vais vous laisser créer les autres niveaux car vous savez, ce processus peut être un peu fastidieux, cela prend un peu de temps et tout le bon truc, la première chose que je vais faire ici, à l'intérieur du VP level, je vais ajouter quelques composants, les premiers vont être un maillage statique, l'un va être un sol.

Et un autre, je vais dupliquer ce mauvais garçon, donc copier et coller puis au lieu de sol, je vais appeler celui-ci cube, voilà.

Et aussi je vais avoir une boîte de déclenchement.

Donc boîte de collision, c'est une que je vais appeler et ce n'est pas un enfant du cube.

Donc je vais appeler celui-ci trigger box, copier et coller et celui-ci, je vais l'appeler spawn location box.

Laissez-moi simplement compiler et enregistrer cela.

Et laissez-moi simplement ajouter tout ce dont j'ai besoin.

Et nous allons coder ou en fait avant cela dans le Event Graph.

Ce que je vais faire, c'est supprimer tout cela.

Et ici nous avons dans le Event Begin Play, je vais définir le spawn location.

Donc je vais faire un clic droit ici et je vais dire set spawn location.

Et remarquez qu'il est sous my triggers.

Regardez cela, vous voyez cela ici.

Regardez mes triggers.

C'est essentiellement ce que nous avons fait dans notre code.

Donc si je retourne ici, où nous avons déclaré ces triggers, regardez cela.

Donc mes triggers, c'est cette catégorie.

Donc maintenant nous pouvons les trouver sous cette catégorie à l'intérieur de nos blueprints lorsque nous voulons coder.

Donc je vais faire un clic droit et je vais dire set spawn location et le spawn location encore, assurez-vous qu'il est sous my trigger.

Donc set spawn location, le voilà sous mes triggers, et le flux d'exécution va aller ici et je vais définir cela ou la boîte de spawn location va être le spawn location.

Ensuite, à partir de là, je vais dire set trigger, et c'est celui-ci ici sous mes triggers.

Donc le flux d'exécution va continuer ici et ensuite je vais prendre la boîte de déclenchement et la brancher ici et laissez-moi simplement compiler et enregistrer cela.

Ce que cela va faire, c'est définir le spawn location à partir de notre code vers celui-ci ici.

Donc nous avons, vous savez, connecté ces deux, ce qui signifie que maintenant c'est une référence à celui-ci ici, même chose que nous avons fait ici, assurez-vous de compiler et enregistrer cela.

Donc maintenant, à l'intérieur de notre viewport, et voici mon sol, que vais-je faire au sol ? Eh bien, je ne vais rien faire au sol, parce que vous savez, je suis un bon garçon, je ne vais rien faire.

Au lieu de cela, ce que je vais faire, c'est aller ici pour le maillage statique et filtrer pour le cube.

Et voilà, voici notre cube pour le matériau, nous allons dire basic shape material, voilà, c'est tout ce qu'il y a à faire.

Et je vais changer l'échelle de celui-ci.

Donc l'échelle x va être 10.

L'échelle y va être un et R, laissez-moi simplement aller ici, j'ai verrouillé l'icône.

Donc je ne veux pas verrouiller quoi que ce soit.

Mais ici, l'échelle, x va être 10, y est un et 0.5.

Donc cela va être, cela va être notre sol.

Ensuite, nous allons avoir un cube.

Donc ici, en prenant le cube.

Et encore, en ajoutant un cube à celui-ci.

Et ici, basic shape, basic shape material, voilà.

Maintenant, pour ce cube, je vais le définir à 90 pour la position Z et le laisser comme cela, c'est tout ce qu'il y a à faire, la boîte de déclenchement, je vais la prendre et pour la boîte de déclenchement, je vais définir cette position à 380, la position était de rester ou de rester à zéro et la position z à 250.

Et je vais aussi définir l'échelle Z à 10.

Ici, pour la boîte de déclenchement, la boîte de déclenchement va être le déclencheur qui, lorsque nous le traversons, nous allons détecter la collision et ensuite nous allons faire apparaître un nouveau niveau.

Donc c'est ce que nous allons faire avec la boîte de déclenchement.

Donc lorsque le joueur passe ici et qu'il touche cette collision, alors nous allons détecter cela et nous allons faire apparaître un nouveau niveau et ici, assurez-vous simplement qu'il chevauche tout le dynamique.

Donc le préréglage de collision est défini sur cela.

Ensuite, nous avons l'emplacement de spawn et l'emplacement de spawn.

Ce que je vais faire avec lui, c'est simplement le repositionner.

Donc je vais le positionner à 1000.

Et c'est tout ce qu'il y a à faire.

Donc l'emplacement de spawn, nous allons utiliser sa position pour positionner le niveau suivant.

Donc lorsque nous faisons apparaître un nouveau niveau, il va commencer à se positionner à partir d'ici.

Et essentiellement, il va former un nouveau niveau comme cela.

Simple, c'est tout ce que nous allons faire avec le spawn ou avec l'emplacement de spawn.

Donc c'est notre niveau un et assurez-vous simplement de compiler et d'enregistrer cela.

Si je vais ici à l'intérieur du gameplay, je vais faire un clic droit et créer une nouvelle classe de blueprint.

Et maintenant, vous allez supposer que, encore une fois, je vais utiliser la base level, mais cette fois, non, au lieu de cela, je vais utiliser level one.

Et chaque niveau suivant que je crée sera un enfant de level one.

Donc BP level one, je vais sélectionner cela, et celui-ci sera BP level two, voilà.

Et je vais simplement l'ouvrir, il a déjà tous ces composants configurés dans le Event Graph, il va appeler le Begin Play des parents, ce qui va faire tout cela, il va préparer tout, nous n'avons pas à le refaire pour ce blueprint.

Très malin, je sais.

Et c'est tout ce qu'il y a à faire.

Bien sûr, maintenant, nous ajoutons simplement de nouvelles choses.

Et ce serait tout, par exemple, le cube que nous avons ici, je vais le repositionner et donc l'exposition sera moins 330, le Y restera le même et le Z restera le même.

Mais je vais aussi ajouter de nouvelles boîtes.

Donc je vais copier ce cube et le coller et je vais appeler celui-ci cube deux.

Et pour ce cube deux, je vais le repositionner.

Donc x sera 190, y zéro, z 130.

Et je vais définir l'échelle Z à trois pour l'échelle Z.

Simple comme cela et copier celui-ci, copier et coller maintenant nous avons le cube trois, et pour le cube trois, la position x est moins 70, la position y 01 180 pour le Z et définir l'échelle Z 2.3 et Wallah, compiler et enregistrer cela.

Donc c'est notre blueprint de niveau deux.

Simple, très, très simple, en revenant ici, clic droit, et encore une fois, classe de blueprint.

Encore une fois, en héritant de level one, voilà.

Pas level two, mais level one, et celui-ci sera BP level three.

Encore une fois, nous avons tout préparé, nous avons notre base queue, nous avons tout ici préparé dans le Event Graph.

Nous n'avons rien à faire, mais nous allons changer ou repositionner ce cube.

Donc encore une fois, moins 330 pour le x, y, je ne vais pas toucher, z, je ne vais pas toucher, donc il va rester tel quel.

Mais maintenant, je vais copier ce cube et le renommer en cube deux.

Et ce cube deux va être repositionné à 70 pour le x, y 04 20 sur l'axe z, et ici, je vais dire trois échelles pour le Z, compiler et enregistrer cela.

En avançant, nous allons avoir un autre niveau.

Donc classe de blueprint ici, hériter du niveau.

Donc hériter de notre niveau un, sélectionner BB, niveau quatre, double-cliquez dessus et ouvrez-le ici dans Visual Studio.

Et encore une fois, simplement repositionner les choses, donc le cube ici va être repositionné, x est moins 303 30, excusez-moi, 174 l'axe z, puis je vais copier ce cube et le renommer en cube deux.

Pour notre cube deux, je vais définir la position à 160 sur le x, y zéro, 2020, ou deux à zéro pour le Z et redimensionner l'échelle Z à quatre.

Enfin, nous avons un autre cube, donc copier et coller, et celui-ci sera à 10 pour le X, 370 sur le Z et l'échelle, Z restera un, mais l'échelle x sera deux et compiler et enregistrer cela, c'est notre niveau pour avancer, je vais faire un clic droit, et encore une fois hériter du niveau un.

Le voilà.

Et celui-ci sera notre BP level five.

Et maintenant nous allons ajouter quelques spikes ici.

Et c'est le dernier niveau que je vais créer, les niveaux suivants sont à vous.

Donc ici pour le cube, je vais définir le x à moins 30 et le Z à 390.

Et je vais définir l'échelle x à trois, l'échelle Z à 2.3, voilà.

Et enfin, nous allons attacher quelque chose ou nous allons attacher un spike.

Et je vais faire ce qui suit.

Donc ici, je vais cliquer sur Ajouter un composant, sélectionner le BP level et je vais filtrer pour child actor.

Et celui-ci sera notre spike.

Voilà.

Je vais l'appeler spike deux.

Mais bien sûr, nous allons aussi avoir spike un.

Donc copiez celui-ci.

Et donc ce que nous allons faire pour notre spike deux, ici vous voyez le composant child actor.

À partir de là, nous pouvons sélectionner le blueprint, nous pouvons cliquer ici, et je peux filtrer pour spikes.

Voilà.

Et laissez-moi simplement supprimer celui-ci, je vais dupliquer celui-ci après.

Donc pour celui-ci, je vais définir le X à deux à zéro et le Z à 40, voilà.

Mais je vais le déplacer un peu vers le haut, quelque chose comme cela.

Voilà, ici sur cette grille de position, snap Val et nous avons décidé de un, donc je peux le snap un peu mieux, while odd, voilà.

Et je vais simplement copier cela et le coller et celui-ci sera notre spike un et simplement le déplacer ici.

Essentiellement, la position x est moins 260 et voilà, compiler et enregistrer cela, donc c'est le dernier niveau que je vais créer, je vais couper la vidéo maintenant et créer les autres niveaux et revenir et vous montrer les niveaux que j'ai créés, mais vous avez beaucoup d'informations pour créer vos propres niveaux.

Une note rapide, vous n'avez pas à créer les mêmes niveaux que moi, vous pouvez créer, vous pouvez créer des niveaux par vous-même, ce qui est une bonne pratique et je l'encourage à chaque fois.

Donc encore une fois, pour ces spikes, lorsque vous savez, vous les touchez, nous allons mourir, mais nous verrons cela plus tard.

Ne vous inquiétez pas pour cela maintenant.

Et essentiellement, c'est tout, chaque niveau que vous créez va hériter de level one.

Je vais couper la vidéo maintenant et je vais continuer, rappelez-vous simplement lorsque vous ajoutez des spikes, vous allez les ajouter en tant que composants child actor.

Donc à partir d'ici, vous allez filtrer pour le child actor lorsque vous sélectionnez le child actor ici, nous allons sélectionner les spikes pour ce child actor.

Et ce serait tout.

Ce serait essentiellement tout.

Donc je n'ai rien d'autre de nx, je n'ai rien d'autre de malin à dire, je ne sais pas comment parler, je vous verrai dans quelques jours lorsque j'aurai créé les autres parties de niveau et je serai de retour, m'avez-vous manqué car cela m'a pris un certain temps pour créer tout cela, bien sûr pour vous, cela a été quelques moments, mais vous savez, si vous ne m'avez pas manqué, alors vous pouvez regarder cette vidéo encore.

Je ne fais que des commentaires, en tout cas, voici les niveaux 6, 7, 8, 9 et 10, donc voici mon niveau six comme vous pouvez le voir, vous pouvez également télécharger le projet complet que j'ai fourni sous la vidéo, vous savez, importer ou créer le projet, vous pouvez, vous savez, télécharger les actifs ou essentiellement le projet complet et le voir par vous-même ou vous pouvez créer vos propres niveaux, ce que je vous encourage fortement à faire, mais en gros, c'est ma vie.

Six comme vous pouvez le voir, donc nous avons un cube ici et deux spikes, ensuite nous avons le niveau sept qui est très simple comme vous pouvez le voir, je ne déplace même pas la boîte de collision ou la boîte de déclenchement et la position de spawn, ils restent au même endroit où ils sont dans le niveau un et je déplace simplement le cube, je le redimensionne, j'ajoute ici des acteurs enfants qui sont les spikes, ici j'ai le niveau huit comme vous pouvez le voir, c'est mon niveau 8123, voilà jusqu'à trois boîtes ou T trois cubes, c'est le niveau neuf, voilà.

Nous avons un spike dans cette chose bizarre ici, la forme en L, si votre nom est Lauren, alors vous savez que c'est pour vous, Lauren, et ici nous avons le niveau 10, voilà.

Et c'est tout ce qu'il y a à faire, compiler et enregistrer.

Je ne peux rien dire d'autre ou je n'ai rien d'autre de malin à dire.

Sauf si quelque chose n'est pas clair.

Assurez-vous de demander dans les commentaires ci-dessous.

Et oui, je vous verrai dans la prochaine vidéo, vous savez, où ailleurs puis-je vous voir, vous savez, je ne vis pas où vous vivez, je ne vous connais pas en personne.

Donc je ne peux pas vous voir, vous savez, chez vous.

Je peux vous voir dans la prochaine vidéo.

Donc encore une fois, si quelque chose n'est pas clair, comme ci-dessous, je vous verrai dans la prochaine vidéo.

D'accord, alors mon elfe de jeu dev.

Donc allons ici dans la classe c++, je vais faire un clic droit et créer une nouvelle classe c++ qui va hériter de la spike, donc je vais cliquer ici sur show all classes et filtrer pour nos spikes, ce n'est pas spike spike, juste spikes, voilà, et celui-ci sera notre wall spike, voilà.

Et ce qui va se passer à l'intérieur de cette classe, c'est que je ne vais rien faire dans le fichier .h, mais bien sûr, nous devons, vous savez, passer par le processus douloureux de tout cela, envoyez-moi ce SSD.

Que puis-je dire d'autre ? Je l'attends, je plaisante, dans quelques jours, il arrivera, dans le prochain tutoriel, nous serons prêts et cela sera rapide comme quelque chose de rapide, je ne sais pas, un écureuil.

Donc dans le wall, allons ici et rechargeons tout d'abord, wall spike dot age, je ne vais rien faire dans le fichier .h, mais dans le fichier .cpp, nous allons faire quelque chose.

Donc ici, en gros, dans le fichier .h, nous allons avoir tout ce dont vous avez besoin, donc nous avons le corps généré, nous allons avoir un public ici, nous allons avoir un wall spike qui est notre constructeur, dans le protégé, donc protégez cela.

Nous allons avoir notre void virtuel.

Donc virtual void Begin Play car nous voulons le remplacer.

Donc override dans notre public, nous allons avoir notre.

Donc à partir d'ici, ce sera virtual, void, tick, et il prendra float Delta time.

Et ici, override, voilà.

Parce que maintenant dans le fichier .cpp, nous allons implémenter tout cela.

Donc ici, nous allons dire a wool spike colon colon, et ce sera notre a will spike, en gros le constructeur.

Et ici, nous allons avoir notre primary actor tick que B can ever tick est égal à true.

Donc nous allons activer cela, aussi ici dans notre void, a wall spike call on call on sera notre begin.

Donc c'est begin blay.

Ce qui va se passer ici, d'abord, vous allez appeler le super, qui est la superclasse et appeler le Begin Play à partir de là.

Donc begin, play.

Voilà, en fait begin play comme ceci.

Et puis à partir de là, ce que je vais faire, ce n'est pas être, c'est begin play comme cela Begin Play, je vais dire this, et je vais obtenir le composant root de notre blueprint, et je vais dire component, donc component velocity, et nous avons dit que F vector, zéro pour le X 25 pour le y et zéro pour le Z.

Donc c'est la vitesse, ou en gros la vitesse de notre acteur.

Ensuite, je vais dire Boyd, a wall spike avec double ou capital W spike, call on call on tick.

Et ici, nous allons avoir le Delta time, comme cela.

Donc ce qui va se passer ici, encore une fois, d'abord, je vais appeler le super dick.

Donc super dick, qui va prendre le Delta time et je sais que vous attendez de moi que je fasse des blagues, oh, vous êtes tick.

Regardez, je ne suis pas Danny, je n'essaie pas d'être Danny, je m'en fiche, vous savez, je ne vais pas faire la blague du tick et tout ça, a dit actor location.

Et à partir de là, je vais obtenir l'emplacement de l'acteur, qui est l'emplacement actuel de cet acteur, et je vais ajouter à celui-ci un F vector.

Et à l'intérieur de ce F vector, je vais dire zéro pour les x, 350 pour le Y, multiplié par Delta time, delta time.

Donc c'est Delta time, voilà, et zéro pour le Z.

Et ici, je vais dire true.

Et c'est tout ce qu'il y a à faire.

Donc laissez-moi simplement compiler cela et nous pouvons nous assurer que tout est correct, nous n'avons aucun problème.

Essentiellement, ce que nous avons fait ici, c'est à l'intérieur de notre Begin Play, voilà, build succeeded, nous sommes bons.

Dans on Begin Play, nous avons défini la vitesse du composant de la racine à 25 sur l'axe y et ensuite ici, à l'intérieur du tick, nous déplaçons l'acteur en utilisant son emplacement actuel et en ajoutant à celui-ci seulement le Y ici parce que x et z sont à zéro, ce qui signifie qu'ils ne bougeront pas et nous ajoutons à celui-ci 350 multiplié par Delta time, bien sûr, vous pouvez définir une variable publique speed ou quelque chose comme cela.

Cela dépend de vous si vous voulez le faire.

Je ne vais pas le faire.

Mais oui, voilà.

Donc allons à l'intérieur de l'éditeur.

Et à l'intérieur des blueprints, je vais aller dans les obstacles et faire un clic droit et créer un obstacle de mur.

Donc je vais dire well spike, parce que cela va hériter du wall spike BP will spike et nous devons éditer cela, nous devons éditer cela pour qu'il ressemble à un mur.

Donc ici, je vais filtrer pour le maillage statique que je vais appeler walls simplement ici pour le maillage statique qui va être notre cube, je vais dire cube comme cela.

Voilà.

Et ici, basic shape material, Wallah.

Je vais changer, vous savez, l'échelle, donc l'échelle y et l'échelle Z vont être 10.

C'est tout.

Ici, pour nos préréglages, vous voyez, il est défini pour bloquer tout le dynamique, au lieu de cela, nous allons dire no collision.

Maintenant, la raison en est que je vais détecter la collision avec une boîte de collision.

Donc je vais ici, aller ici et dire bar collision.

Et simplement l'appeler box, vous pouvez l'appeler box ou autre chose, et pour celle-ci, je vais définir l'échelle x à trois, l'échelle y va être 20 et l'échelle Z va être 20.

Et avec celle-ci, je veux détecter la collision avec notre joueur.

Et pour que je puisse faire cela, je vais faire défiler vers le bas ici où il est dit pour les préréglages de collision et je vais définir celui-ci sur la collision personnalisée, ici, je vais dire query only no physics collision.

Donc essentiellement, pas de collision physique ici pour le world dynamic, je vais en fait définir celui-ci sur spike, car le spike pourra entrer en collision avec le joueur, compilez et enregistrez cela maintenant afin que nous ou pour que cela fonctionne, nous allons aller dans notre joueur, qui est celui-ci, laissez-moi simplement fermer ces niveaux.

Donc en fermant, tous les niveaux, allez, voilà.

Pour le joueur, je vais sélectionner son composant de capsule et faire défiler vers le bas ici pour le préréglage de collision, il est défini pour être un personnalisé et il est dit être un pawn.

Donc c'est ce dont nous avons besoin, nous allons le définir pour être un personnalisé, le définir pour être un pawn, assurez-vous qu'il chevauche le spike, car c'est ce dont nous avons besoin.

Donc nous en avons besoin pour chevaucher le spike.

Maintenant, ce que nous devons faire, c'est aller ici à l'intérieur de notre jeu, et nous allons ajouter notre wolf spike, le voilà, et laissez-moi simplement le repositionner.

Donc l'exposition va être moins 30, le Y va être moins 830 et le Z à 455.

Et bien sûr, je vais aussi le faire tourner de 90 degrés sur le z, donc 90 degrés sur l'axe z.

Si je clique sur le bouton lecture maintenant, voilà, vous voyez, il avance, il essaie de nous chercher ou en fait, il essaie de nous attraper, s'il nous attrape, regardez maintenant, il passe simplement à travers nous, nous ne détectons pas de collision dans le code.

C'est pourquoi nous ne voyons rien.

Donc nous devons détecter la collision avec le joueur dans le code, je ne veux pas laisser cela dans la prochaine vidéo.

Au lieu de cela, je vais le faire maintenant, je peux le laisser dans la prochaine vidéo, mais je vais le faire maintenant.

Donc en revenant ici à l'intérieur de notre runner character CPP en haut ici, donc à l'intérieur de Begin Play après ou avant de définir can move à true, nous devons obtenir le composant de capsule, donc nous devons dire get capsule component qui est un composant, le composant de capsule du joueur que nous avons juste édité.

Vous savez, celui que j'ai dit, il doit être un pawn.

Donc à partir de là, je vais voir on component begin overlap dot et je dirais add dynamic.

Et ici, nous allons ajouter cela et je vais simplement descendre et copier le nom ici afin de ne pas avoir à, vous savez, le taper.

Donc et et cela, voilà.

Donc cela va prendre ce composant de capsule du joueur, qui est, vous savez, dans les blueprints, donc en prenant ce composant de capsule, puis il va y attacher notre on begin overlap ou on overlap begin.

Donc essentiellement, ce qui va se passer à l'intérieur de celui-ci, c'est que nous allons détecter si nous avons heurté un spike ou un wall spike.

Donc ici, je vais dire si l'autre acteur n'est pas égal à no PTR.

Donc c'est PTR, pas TPR.

C'est PTR, l'autre acteur est essentiellement l'acteur, l'autre que nous avons heurté à l'intérieur de notre jeu.

Donc s'il n'est pas égal à nul, nous avons heurté l'un des acteurs, alors nous allons dire un spike comme cela, ou spikes qui est un pointeur.

Et je vais dire ici walls spikes, voilà, ou wall spike et cela va être égal à je vais caster cela en un wall spike comme cela et je caste l'autre acteur.

Maintenant, nous n'avons pas la complétion ou quoi que ce soit parce que nous devons aller ici en haut et à droite ici, nous devons inclure quelques choses, donc nous devons dire inclure notre fichier spikes dot h, nous devons aussi inclure notre fichier wall spike dot h et enfin, nous devons inclure le moteur.

Donc c'est engine dot h parce que nous allons redémarrer le jeu lorsque le joueur meurt, afin de pouvoir le faire.

Ensuite, nous devons utiliser le moteur et voilà, ici nos spikes wall spike, nous allons faire cela ou essayer de caster cela ensuite, je vais dire a spikes et ici parce que c'est un pointeur spike et je vais le caster en un spike comme cela, puis je caste à nouveau l'autre acteur, comme je l'ai fait naturellement ici, c'est spikes, pas spike.

Donc essentiellement, si nous entrons en collision avec le mur, donc si wall spike ou nous avons le spike.

Donc si nous entrons en collision avec l'un de ceux-ci, ce qui signifie qu'ils ne sont pas égaux à nul, cela signifie que nous avons heurté l'un des deux, cela signifie game over.

Donc maintenant, je vais dire get mash, qui va obtenir le maillage de notre personnage, et ensuite je vais désactiver ce maillage, je vais aussi dire get mesh.

Et à partir de là, je vais dire set visibility pour ce maillage à false afin que nous ne le voyions plus dans le jeu, can move est maintenant égal à false, nous ne pouvons plus bouger.

Et ensuite, nous allons recharger le niveau après deux secondes.

Et pour cela, nous devons créer f timer handle, je vais dire on used donc on used handle comme cela.

Et je vais dire get world timer manager.

Et à partir de là, je vais dire set timer.

Et je vais passer le handle on use donc on use le handle dans celui-ci et ensuite je vais passer cette fonction qui est notre runner re start level.

Donc ici et en passant le restart level en passant ici deux, car après deux secondes, je veux que cela redémarre et ici je vais dire false car je ne veux pas que cela boucle et soit une boucle infinie et apparaisse encore et encore.

La dernière étape ici est à l'intérieur de notre restart level, nous devons simplement appeler you gameplay statics.

Donc vérifiez les statics et ici, open level.

Et simplement, nous pouvons passer le nom du niveau ou nous pouvons faire cela, je peux passer cela et je peux dire le nom du niveau au lieu de passer le nom.

Je peux dire ici avec une étoile get world comme cela.

Et ici, get the name, voilà.

Et voilà, ce monde va obtenir le nom du niveau actuel dans lequel nous nous trouvons et il va le coller ici, je vais compiler cela et pendant que je compile, je vais expliquer ce qui se passe ici.

Je ne pense pas qu'il y ait quelque chose à expliquer car nous avons déjà expliqué que à l'intérieur de notre runner character, nous avons attaché ici le on begin overlap pour le collider de capsule.

C'est tout ce que nous avons fait.

Et ici, nous testons si nous avons l'autre acteur, ce qui signifie que nous avons heurté quelque chose, donc l'autre acteur n'est pas égal à nul et voilà, le build a réussi.

Donc notre jeu est terminé.

Et ici, nous avons l'autre acteur et nous avons heurté quelque chose.

Donc essayez de caster cet autre acteur en un wall spike ou un spike, en gros, ce qui signifie essayer de tester si l'autre acteur est le wall spike ou si l'autre acteur est le spike.

Est-ce vrai, est-ce le cas, en gros, c'est ce que nous demandons.

Et si nous avons l'un ou l'autre, donc si nous avons un wall spike ou un spike, ce qui signifie qu'ils ne sont pas égaux à non, nous allons obtenir le maillage et le désactiver, nous allons aussi définir la visibilité du maillage à false afin de ne plus le voir, nous ne pouvons pas bouger à l'intérieur de notre jeu afin que lorsque nous appuyons sur les boutons, nous ne pourrons pas bouger parce qu'ici, si vous vous souvenez, seulement si nous pouvons bouger maintenant, nous allons avoir le mouvement ajouter le mouvement au joueur et ensuite ici, nous allons redémarrer le niveau, c'est la signature pour redémarrer le niveau, donc nous devons passer ce handle de timer même si nous ne l'utilisons pas, en passant cela en faisant référence à cette classe, c'est la fonction que je veux être appelée après deux secondes et non, je ne veux pas qu'elle boucle, je ne veux pas qu'elle se répète encore et encore et ici, simplement en appelant gameplay statics open level en passant le nom du niveau pour recharger le niveau et c'est à peu près tout, nous avons terminé, donc si je clique sur le bouton lecture maintenant, lorsque nous, vous savez, entrons en collision avec les spikes ou ce mur, donc maintenant lorsque le mur me touche, voilà, le personnage a disparu, maintenant nous avons redémarré le niveau et si je entre en collision avec l'un des spikes, alors, allez, en voici un des spikes, voilà, bam.

Je suis aussi mort et voilà.

C'est notre jeu, essayons-le à nouveau, encore une fois, essayons de courir, essayons de courir, en tout cas, vous comprenez.

Félicitations pour être arrivé jusqu'à la fin de ce jeu.

Si vous avez aimé cette vidéo, cliquez sur le bouton like et abonnez-vous à la chaîne, tout le bon truc parce que cela m'aidera, vous savez, j'essaie de répandre la parole sur ma sagesse et je plaisante, mais en tout cas, vous comprenez.

Donc je n'ai rien d'autre à dire.

Si vous aimez cela, vous avez plus de tutoriels dans mon Académie de développement de jeux.

Merci d'avoir regardé encore et je vous verrai dans la prochaine vidéo.