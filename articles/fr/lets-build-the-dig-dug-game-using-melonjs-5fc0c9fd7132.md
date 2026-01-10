---
title: Créons le jeu Dig Dug en utilisant MelonJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-11T18:52:13.000Z'
originalURL: https://freecodecamp.org/news/lets-build-the-dig-dug-game-using-melonjs-5fc0c9fd7132
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BSr2KU-TRKONo4AkGOK1Rw.png
tags:
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Créons le jeu Dig Dug en utilisant MelonJS
seo_desc: 'By Yazed Jamal

  Recently I had the chance to watch Stranger Things Season 2. After watching it,
  I was very excited to see one of my favorite game during my childhood, “Dig Dug”,
  featured in the series. At the same time, I was searching for a game that...'
---

Par Yazed Jamal

Récemment, j'ai eu l'occasion de regarder la saison 2 de Stranger Things. Après l'avoir regardée, j'étais très excité de voir l'un de mes jeux préférés de mon enfance, « Dig Dug », présenté dans la série. En même temps, je cherchais un jeu que je pourrais créer pour pratiquer mes compétences en développement de jeux. Donc aujourd'hui, j'ai décidé que Dig Dug serait le jeu.

Cette version de Dig Dug n'est pas une version complète. Il s'agit uniquement du mécanisme de base du jeu, qui peut être étendu à une version complète de Dig Dug plus tard.

MelonJS est le framework choisi, non pas pour une raison particulière. Je l'ai simplement choisi au hasard parmi les nombreux frameworks disponibles.

Voici les étapes que je vais suivre pour ce développement de jeu :

1. Installation du framework
2. Création du terrain
3. Création du creuseur
4. Création du monstre
5. Création de la logique de collision
6. Ajout de l'affichage de l'unité de tête
7. Ajout des effets sonores et de la musique de fond
8. Ajout de l'écran d'introduction
9. Ajustement final
10. Prochaines étapes

#### **Étape 1 — Installation du framework**

MelonJS recommande d'utiliser le modèle fourni par eux pour commencer un développement de jeu. Tout d'abord, je dois télécharger le modèle depuis [GitHub](https://github.com/melonjs/boilerplate).

Je vais cloner le modèle dans mon répertoire local de choix :

```
#terminalgit clone https://github.com/melonjs/boilerplate.git mylocalfolder
```

Ensuite, je devrai configurer mon propre dépôt distant pour le jeu en utilisant ce [guide](https://help.github.com/articles/duplicating-a-repository/). Il est également conseillé de suivre leur tutoriel pour se familiariser avec l'utilisation du framework.

Ensuite, je devrai télécharger les ressources de jeu fournies par MelonJS sur leurs pages de tutoriel. Cela peut être utile si vous avez besoin de certaines images ou tuiles et que vous n'avez pas le temps de les concevoir et de les créer. Ces ressources peuvent être téléchargées sur l'une des pages de tutoriel de MelonJS [ici](http://melonjs.github.io/tutorial-space-invaders/) et [ici](http://melonjs.github.io/tutorial-platformer/).

Maintenant, je voudrais discuter un peu de certains fichiers squelettes importants fournis dans le modèle. MelonJS utilise la bibliothèque d'héritage [Jay Extend](https://github.com/parasyte/jay-extend). Je dois donc également me familiariser avec les fichiers.

`**js/game.js**` :

Voici l'espace de noms global de mon jeu qui se trouve être défini comme `game` (ce qui peut être n'importe quoi).

Des lignes 1 à 8, je peux définir toutes les informations dont j'ai besoin sous forme d'objet.

Ensuite, des lignes 12 à 25, c'est là que je peux configurer la résolution du jeu, le comportement de l'écran et charger toutes les ressources du jeu comme les images et les sons.

Je dois changer certains détails, comme la résolution de l'écran et la méthode de mise à l'échelle pour les performances du jeu à la ligne 14.

Enfin, les lignes 28 à 37 sont celles où le jeu exécutera tout.

`**js/screen/play.js**` :

Ce fichier sera chargé par `**game.js**` qui gère l'écran de jeu.

Des lignes 5 à 13, toute l'exécution se produit lorsque le jeu commence. C'est là que je spécifierai de rendre toutes les entités du jeu plus tard.

Mais, les lignes 18 à 21 sont celles où toutes les entités seront supprimées. Je vais modifier ces deux fichiers tout au long du processus.

Donc, avant de créer un autre objet, je dois installer toutes les bibliothèques npm requises en exécutant la commande suivante :

```
#terminalnpm install
```

et je dois installer `**grunt-cli**` qui est requis :

```
npm install -g grunt-cli
```

Enfin, pour exécuter le jeu, je peux exécuter la commande suivante et accéder au serveur local pour voir le jeu en cours d'exécution :

```
grunt serve
```

Pour l'instant, je ne peux voir qu'un écran noir vide lorsque le jeu est en cours d'exécution.

#### **Étape 2 — Création du terrain**

Après avoir un peu appris sur le modèle fourni, il est maintenant temps de créer ma première entité, le terrain. Il existe plusieurs types d'objets que je pourrais créer à partir de ce framework.

Donc, comme ce terrain entrera en collision avec le creuseur et le monstre dans le jeu, je dois créer un objet `Entity` pour le terrain. Le terrain est l'objet où le jeu se déroule et que le creuseur doit creuser pour que le creuseur puisse passer à travers.

À l'origine, le terrain est un petit carré de 15 x 15 pixels qui peut ensuite être rendu à plusieurs reprises sur l'écran pour faire une zone plus grande. Je pourrais utiliser un logiciel appelé [Tile Map Editor](http://www.mapeditor.org/) à cette fin, mais pour ce jeu, je vais le faire manuellement.

Voici comment je procède. Tout d'abord, créez un fichier dans le dossier `**js**` appelé `**ground.js**`. Ensuite, je vais créer une nouvelle entité d'objet comme suit :

À la ligne 2, je vais créer un nouvel objet appelé `game.Ground` qui étend l'objet Entity fourni par MelonJS.

À la ligne suivante, j'initialise l'objet via l'objet parent avec tous les arguments requis. Cet objet aura besoin des valeurs `x` et `y` comme emplacement de l'objet.

La largeur et la hauteur sont définies aux lignes 37 et 38.

Pour rendre quelque chose, je peux utiliser un sprite d'image à cette fin. Mais dans ce cas, je vais utiliser la fonction `draw` du HTML5 Canvas. Cela a été fait aux lignes 9 à 28. Ici, je vais programmer pour dessiner un rectangle avec des pois à l'intérieur. La couleur du carré et des pois sera définie par les variables déclarées aux lignes 5 et 6, respectivement.

Aux lignes 30 à 35 se trouve la fonction `update` de l'objet. Ici, je dois définir l'entité pour qu'elle se met à jour à la ligne 32 chaque fois que la fonction `update` est appelée. Et enfin, retourner une valeur vraie pour s'assurer que l'entité est redessinée chaque fois que le jeu est mis à jour.

À l'étape suivante, je devrai faire référence à ce fichier dans le fichier `**index.html**` à la ligne 40 et :

enregistrer l'entité dans le pool dans `**game.js**` à la ligne 33. Je n'aurai pas besoin du code précédemment dans `**game.js**` qui enregistrait `game.PlayerEntity` car je vais créer l'entité du joueur manuellement plus tard.

Puisque le terrain doit être dessiné plusieurs fois, il est bon pour moi de créer un conteneur pour tout le terrain qui gérera tout le travail. Pour créer un conteneur, je devrai créer un nouvel objet et étendre l'objet conteneur fourni par MelonJS.

Je nommerai ce conteneur `game.LevelManager`.

Comme avant, je devrai initialiser les arguments. Définir le nom de cet objet, et définir les données qui seront utilisées pour placer tous les carrés sur l'écran aux lignes 2 à 21.

Ensuite, je vais créer une fonction personnalisée qui exécute le travail de rendu basé sur les données aux lignes 24 à 37. À la ligne 30, c'est ainsi que j'ajoute le carré à ce conteneur, et après que tous les carrés soient rendus, je dois mettre à jour la zone de délimitation du conteneur à la ligne 36.

Enfin, je devrai rendre le conteneur sur l'écran de jeu, donc tout ce qui se trouve sous ce conteneur sera également rendu.

Avant de faire cela, je devrai créer une instance de l'objet `levelManager` aux lignes 9 à 11 ci-dessous :

Je dois également me rappeler de toujours faire référence au nouvel objet créé dans le fichier `**index.html**`.

Maintenant, si je lance le serveur, je devrais obtenir une vue comme celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*0ZbZbtDKdAnBqXTbjIA9aA.png)

#### **Étape 3 — Création du creuseur**

Tout d'abord, j'aurai besoin d'un sprite d'image pour mon creuseur. Au début, j'allais utiliser les ressources de jeu fournies par MelonJS, mais heureusement, mon fils a créé une image pixelisée pour que je l'utilise pour le creuseur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*_iy9MtYX5DdGxAWegVr2Ag.png)

Je dois ensuite placer cette image dans le dossier `**data/img**` du répertoire du modèle. Lorsque je lance le serveur maintenant, Grunt construira et ajoutera automatiquement le fichier de ressource dans le dossier `build/js` avec les données d'image ci-dessus.

Pour créer l'objet `Digger`, je devrai à nouveau étendre l'objet `Entity`.

Je vais créer un nouveau fichier appelé `**digger.js**` dans le dossier `**js**` et faire la référence dans `**index.html**`.

À la ligne 3, je charge l'image depuis le fichier de ressource que j'ai créé précédemment et je l'assigne à une variable. À la ligne 5, j'initialise l'objet avec les arguments et paramètres requis. Pour le creuseur, je vais assigner l'image avec l'image définie précédemment.

Ensuite, à la ligne 12, je retourne le sprite lorsqu'il est rendu pour la première fois.

Je vais également devoir mettre la `gravité` à `0` à la ligne 13 car ce n'est pas un jeu de plateforme qui nécessite une gravité pour que le personnage agisse correctement. Dans ce cas, le creuseur flottera.

À la ligne 14, la vitesse du creuseur est initialisée afin qu'il puisse être déplacé plus tard. Je définis le type de collision pour cette entité pour l'utilisation de la logique de collision plus tard.

Des lignes 17 à 22, je définis et gère l'animation du sprite. Les nombres dans le tableau de la fonction `addAnimation` sont destinés à déterminer quel cadre particulier de l'image doit être utilisé pour l'animation. Le nombre à côté est destiné à définir la vitesse. Enfin, je configure l'animation initiale à utiliser lorsque l'écran de jeu commence.

Maintenant, je vais devoir définir le mouvement du creuseur. Je remarque dans le jeu Dig Dug original que chaque fois que le creuseur tourne vers le haut ou vers le bas, il tourne toujours son personnage de manière appropriée en fonction du terrain. Je dois prendre note de cela pour l'implémenter correctement dans mon creuseur. Cela sera une section de code assez longue.

Je découvre que pour que le creuseur agisse correctement chaque fois que je tourne le sprite, je vais devoir ajuster la limite de l'entité et également la forme de la boîte de collision.

Initialement, le sprite du creuseur fait 48 x 24 pixels. Cela est dû à l'image du creuseur tirant son arme. Cependant, pendant le mouvement normal, je n'aurai besoin que du creuseur soit de 24 x 24 pixels.

Cela est géré en changeant la forme de collision initialement à 24 x 24 et en la transformant en 48 x 24 lorsque le creuseur tire son arme, aux lignes 17 à 19 ci-dessous :

Des lignes 28 à 33, je définis plusieurs indicateurs booléens que j'utiliserai dans la fonction de mouvement.

À partir de la ligne 36, c'est la fonction `update` du creuseur qui contient également la logique de mouvement du creuseur basée sur l'entrée du clavier des lignes 40 à 134.

Dans cette logique, je dois considérer beaucoup de choses comme ce qui se passe lorsque la touche de mouvement est pressée ou relâchée, la dernière position du creuseur avant qu'une touche de direction ou de tir soit pressée et relâchée, et l'état différent de l'animation requis. Ce n'est pas une fonction complexe, mais la logique est un peu longue (bien que fondamentalement simple).

Des lignes 143 à 283, c'est la fonction `movement` pour le haut, le bas, la gauche et la droite.

Pour rendre le creuseur à l'écran et rendre le mouvement possible, je dois ajouter l'objet creuseur au conteneur `game.world` à la ligne 12 et enregistrer la touche du clavier des lignes 19 à 23 pour le mouvement dans `**play.js**` ci-dessous. Je devrai également désactiver lorsque le jeu quitte l'écran de jeu pour d'autres utilisations si nécessaire aux lignes 30 à 34.

Si je lance le serveur maintenant, je peux voir le creuseur en action et le déplacer vers le haut, le bas, la gauche et la droite.

Cependant, je peux voir une image traînante lorsque le creuseur se déplace, ainsi que la ligne de l'image de démarrage de MelonJS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RssUgB7SFW-cX0hLGWGNMA.png)

L'image traînante est due au dessin exécuté chaque fois que la boucle de jeu se met à jour. Cela peut être résolu en ajoutant une couche de dessin avant chaque fois que le creuseur est redessiné à la ligne 12 ci-dessous :

#### **Étape 4 — Création du monstre**

Ayant terminé avec le creuseur pour l'instant, je vais créer les monstres ensuite. Ce sera essentiellement le même processus pour les monstres. Je vais devoir créer un objet `Entity` pour les monstres, ajouter les monstres au conteneur `levelManager`, et enfin les rendre à l'écran.

Voici l'objet `Entity` pour le monstre :

Je vais d'abord initialiser l'objet aux lignes 5 à 9. Cette fois, je vais simplement utiliser un sprite fourni par MelonJS depuis son tutoriel de jeu de plateforme que j'ai modifié pour ajouter plus de cadres ci-dessous.

Ce sprite doit être dans le même dossier que le sprite du creuseur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*aU3m-AZl2JSKPnN6GE-ycw.png)

Ensuite, je nomme l'objet à la ligne 11, je définis le type de collision à la ligne 12, je réinitialise le carré de collision et je le rends plus petit aux lignes 14 à 15, et je définis la vitesse et la gravité du monstre aux lignes 17 à 18. Je définis également le groupe d'animation à utiliser avant de configurer l'animation initiale à utiliser aux lignes 20 à 22.

Ensuite, je définis une fonction pour le mouvement du monstre. C'est un algorithme de mouvement très basique manipulant la valeur de vitesse `X` de l'objet pour le mouvement horizontal et `Y` pour le mouvement vertical aux lignes 26 à 43. Enfin, je crée la fonction `update` de l'objet qui ne contiendra que la mise à jour du corps pour l'instant aux lignes 45 à 52.

Avant de continuer, je dois toujours me rappeler de faire une référence dans `**index.html**` et un enregistrement dans `**game.js**` pour tout nouvel objet d'entité créé.

Après avoir créé l'objet, je devrai mettre à jour le conteneur `LevelManager` pour inclure les données du monstre et également la fonction `creation`.

Voici le code mis à jour :

Des lignes 21 à 28, ce sont les données pour l'emplacement du monstre. La fonction pour la création du monstre ou l'ajout à ce conteneur est ajoutée aux lignes 48 à 56. Enfin, pour le faire apparaître à l'écran, certaines lignes doivent être ajoutées dans `**play.js**`.

Voici l'ajout à la ligne 11 qui appelle la fonction pour créer tous les monstres :

Maintenant, si je lance le serveur, je peux voir deux petits monstres mignons apparaître à l'emplacement spécifique sur l'écran. Pour l'instant, ils ne bougeront pas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dH4wDQDkzszq52nEag0D9w.png)

#### **Partie 5 — Création de la logique de collision**

Je vais commencer par la logique de collision du creuseur avec le terrain et le monstre. Pour que le framework vérifie toute collision sur l'objet d'entité, je dois inclure la méthode **vérification de collision** dans la fonction `update`. Après cela, je peux maintenant inclure la fonction `onCollision` qui fournit des informations sur les objets spécifiques qui entrent en collision.

Voici les codes de l'objet creuseur mis à jour :

À la ligne 138, le code vérifie si une collision se produit pour cet objet.

Aux lignes 144 à 166, une fonction fournit une réponse lorsque les objets entrent en collision. Lorsque le creuseur entre en collision avec le terrain aux lignes 147 à 150, l'entité de terrain spécifique sera supprimée du conteneur `levelManager`.

Cependant, je ne veux pas que le terrain disparaisse lorsque le creuseur tire son arme, donc je mets une exception à la ligne 148.

Ensuite, c'est la logique pour la collision avec les monstres. Si le creuseur entre en collision avec un monstre tout en tirant son arme, le monstre clignotera et sera supprimé. Autrement, le creuseur clignotera, sera supprimé et le jeu sera réinitialisé des lignes 151 à 163. Retourner vrai dans la fonction `collision` rendra les autres objets qui entrent en collision avec le creuseur solides. En d'autres termes, le creuseur ne passera pas à travers un autre objet pendant la collision. Dans ce cas, je veux qu'il retourne faux.

Pour terminer cela, je vais ensuite créer la logique pour les limites. Actuellement, le creuseur est autorisé à sortir de l'écran. Pour ce faire, je vais définir la distance maximale que le creuseur est autorisé à parcourir sur les axes `x` et `y` dans la fonction d'initialisation de l'objet aux lignes 16 à 17 ci-dessous.

Ensuite, dans la fonction `update`, je vais définir les limites en utilisant la méthode intégrée `clamp` aux lignes 105-106.

Maintenant pour les monstres. Après avoir effectué la vérification de collision sur le monstre, je dois définir la logique de collision avec le terrain et aussi la limite. Cette logique doit également inclure une sorte d'intelligence artificielle (IA) pour que le monstre poursuive le creuseur.

Le monstre ne pourra pas creuser le terrain, donc il rebondira dans la direction où se trouve le creuseur lorsqu'il heurte le terrain ou la limite. Pour que la collision de la limite fonctionne, je dois définir la distance maximale de déplacement pour le monstre et la configurer. Je n'ai pas à définir la logique de collision avec le creuseur car elle est déjà gérée par l'objet `Digger`. J'ai également fait en sorte que le monstre se déplace vers la droite lorsque le jeu commence.

Voici le dernier objet `Monster` :

Des lignes 138 à 159, c'est une fonction que j'ai définie qui sera exécutée lorsque le monstre entre en collision avec le terrain dans la fonction `onCollision`. La logique est de faire en sorte que le monstre se déplace vers le creuseur lorsqu'il heurte le terrain.

Des lignes 76 à 136, j'ai défini une fonction qui représente la logique de collision du monstre avec la limite, qui est appelée dans la fonction `update` à la ligne 57.

Chaque fois que le monstre ne heurte pas la limite, il vérifiera toujours l'emplacement du creuseur et se déplacera vers lui. Ensuite, si le monstre heurte la limite, il se tournera vers le creuseur et continuera à le poursuivre. Je n'ai pas inventé l'algorithme d'IA moi-même — c'est une combinaison de scripts que j'ai trouvés sur Internet avec les miens. De plus, dans cette fonction, je suis tenu d'accéder aux propriétés de l'objet du creuseur comme les positions `X` et `Y`. Pour obtenir cet accès, je dois apporter quelques modifications à la façon dont le creuseur est rendu à l'écran de jeu.

À la ligne 13, je déclare une propriété `game` qui représente le creuseur enregistré depuis le pool avant de l'ajouter à l'écran de jeu. Cette propriété sera utilisée pour accéder aux propriétés du creuseur à l'intérieur de l'objet monstre.

Enfin, j'inclurai le code qui réinitialisera le jeu si tous les monstres sont entrés en collision avec le creuseur en mode tir. En d'autres termes, si le creuseur parvient à tuer tous les monstres. Cette vérification sera effectuée dans le conteneur `levelManager`.

Je vérifierai le tableau contenant tous les monstres des lignes 60 à 62. Si le tableau est vide, je réinitialiserai le jeu.

Mais avant cela, je dois également créer un indicateur booléen à la ligne 56 qui confirmera que le monstre est déjà créé lorsque je commence le jeu. Sinon, le jeu continuera à se réinitialiser avant que les monstres ne puissent être créés.

#### **Étape 6 — Ajout de l'affichage de l'unité de tête**

Tout d'abord, je dois créer un dossier de police dans le répertoire de données :

```
data/fnt
```

puis utiliser la police fournie par MelonJS dans les ressources de jeu téléchargées précédemment :

```
PressStart2P.pngPressStart2P.fnt
```

et les mettre dans le nouveau dossier.

Ensuite, je dois ajouter un script dans le `**gruntfile**` afin qu'il génère les données de ressource pour la police ci-dessous aux lignes 22 à 28 :

Lorsque je lance le serveur, la police sera dans les données de ressource :

Par défaut, l'objet d'affichage de l'unité de tête (HUD) est déjà créé dans le modèle. Je peux accéder au fichier dans `**js/entities/HUD.js**`. Je dois simplement définir la police ajoutée précédemment et créer une fonction `draw` pour celle-ci.

Voici le code mis à jour :

Je définis et initialise la police aux lignes 42 à 48, puis je crée la fonction `draw` qui rendra le score du jeu à l'emplacement spécifique tel que défini à la ligne 71.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XogFTGiBXcjroHyuUNksdQ.png)

Enfin, j'ajouterai un affichage du meilleur score et sa logique. La logique consiste simplement à sauvegarder et à additionner le score actuel à la propriété `highScore` chaque fois que le jeu se réinitialise. Soit le creuseur tue tous les monstres, soit le creuseur est tué.

Tout d'abord, j'ai créé la propriété `highScore` à la ligne 9 :

Ensuite, dans la fonction `onCollision` du `**digger**`, j'augmenterai le point chaque fois qu'un monstre est tué à la ligne 14 et j'additionnerai les points actuels au meilleur score si le creuseur est tué à la ligne 26.

Je vais également faire un petit ajustement à ce qui se passera lorsque le monstre heurtera le feu. Je vais faire en sorte que le monstre arrête de bouger, juste après avoir heurté le feu, pour éviter toute collision inutile par la suite à la ligne 11.

#### **Étape 7 — Ajout des effets sonores et de la musique de fond**

Configurer cela est un jeu d'enfant. Tout le code requis est déjà là dans le modèle. Ce que je dois faire, c'est mettre le fichier musical ou sonore requis dans le dossier pertinent et faire quelque chose avec la musique.

Basé sur le jeu original lorsque le creuseur se déplace, la musique de fond sera jouée. Une logique simple doit être implémentée pour que la musique de fond n'essaie pas de démarrer à plusieurs reprises lorsqu'une touche de direction est pressée.

Voici l'objet digger mis à jour :

À la ligne 37, je crée un indicateur booléen à utiliser dans la logique de mouvement et de musique de fond.

Aux lignes 45 à 47, c'est la logique pour que la musique de fond ne démarre pas à plusieurs reprises si une touche de direction est pressée en continu.

Respectivement aux lignes 114, 200, 224, 249 et 288, l'indicateur est défini pour que la logique fonctionne correctement.

La musique de fond a été faite pour s'arrêter lorsque le creuseur s'arrête à la ligne 115.

En ce qui concerne les autres sons, j'ajoute également un son pour le creuseur en mode tir et un son de pop lorsque le monstre meurt. À la ligne 69, j'active le son lorsque la touche de feu est pressée, et je l'arrête lorsque la touche de feu est relâchée à la ligne 140. Le son de pop sera activé lorsque le monstre entre en collision avec le creuseur pendant le mode tir juste après avoir été retiré de l'écran à la ligne 174.

#### **Étape 8 — Ajout de l'écran d'introduction**

Tout d'abord, j'ouvrirai `**game.js**` et je modifierai un morceau de code. Au lieu de changer l'état du jeu en PLAY, je changerai l'état en MENU à la ligne 40.

Cela chargera le fichier `**title.js**` lorsque le jeu sera chargé :

Ensuite, je modifierai le fichier `**title.js**` dans le dossier `**js/screens**` :

Ici, dans le `onResetEvent`, je joue la musique de fond lorsque l'écran apparaît à la ligne 8.

Ensuite, je couvre le viewport avec une couche de couleur marron à la ligne 10.

Puis, je crée un objet `Renderable` qui contient le titre et quelques mots des lignes 13 à 43.

Cet objet `Renderable` sera défilé vers le haut de l'extérieur vers le milieu de l'écran en utilisant `Tween` aux lignes 22 à 23.

Enfin, je devrai lier la touche ENTER pour déclencher un événement qui démarrera le jeu aux lignes 47 à 57.

#### **Étape 9 — Ajustement final**

Je ne ferai pas grand-chose pour l'ajustement final. Je vais simplement ajouter un autre son de fond au monstre et je vais positionner le creuseur de manière similaire au jeu original. Tout d'abord, je vais ajouter un autre `Tween` pour que le creuseur se déplace vers le centre de l'écran lorsque le jeu commence.

Je vais inclure le nouveau fichier sonore dans le bon dossier, puis je vais mettre à jour le fichier `**digger**`.

Je vais déclarer quelques indicateurs booléens supplémentaires à utiliser aux lignes 38 à 40, jouer la musique de fond au début du jeu à la ligne 30, et exécuter le mouvement initial du creuseur en appelant la fonction définie à la ligne 29.

Voici la nouvelle fonction :

À partir de la ligne 4, je vais définir l'animation `Tween` avec une fonction de rappel qui arrête la musique de fond, définit quelques indicateurs pour la logique, et déplace l'enregistrement de la touche de liaison ici depuis `**play.js**` pour éviter tout mouvement supplémentaire par une pression de touche pendant le tweening.

Enfin, voici la fonction pour créer le son du monstre toutes les 5 secondes. Cette fonction sera appelée dans la fonction `update` de l'objet `**digger**`.

#### **Étape 10 — Prochaines étapes**

Voici les éléments que je pourrais continuer à développer pour ce jeu :

1. Créer la version fantôme du monstre qui traverse le terrain.
2. Créer un deuxième niveau et les suivants pour le jeu.
3. Créer des éléments supplémentaires où le creuseur pourrait gagner plus de points.
4. Créer une base de données locale avec des cookies où le jeu se souviendra du meilleur score du joueur.
5. Refactoriser, refactoriser et refactoriser.
6. Améliorer les performances du jeu.

Merci d'avoir lu jusqu'à la fin. Si vous avez d'autres suggestions sur la liste ci-dessus, n'hésitez pas à commenter ce post ci-dessous.

Le code complet peut être téléchargé depuis [GitHub](https://github.com/muyaszed/dig-dug-clone).

N'hésitez pas à essayer la [démo](http://yazedjamal.com/myDigDug/) du jeu.

**Notes** : Il existe probablement de nombreuses façons d'implémenter cette fonctionnalité, mais celle-ci était la plus facile pour moi. Toute personne est libre de commenter toute erreur ou amélioration que je peux appliquer. Ce guide est initialement pour moi afin d'apprendre et de me souvenir de ce que j'ai fait. Néanmoins, tout le monde est le bienvenu pour suivre ce guide s'il le trouve utile.