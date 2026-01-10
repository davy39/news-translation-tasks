---
title: Créer un jeu VR multijoueur basé sur navigateur avec A-Frame, PubNub et WebVR
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T20:50:01.000Z'
originalURL: https://freecodecamp.org/news/build-a-multiplayer-browser-based-vr-game-with-a-frame-pubnub-and-webvr-b7de33ba088
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Iu7_DRv1Pr_9dHfkr22ZVw.png
tags:
- name: coding
  slug: coding
- name: 'tech '
  slug: tech
- name: Virtual Reality
  slug: virtual-reality
- name: vr
  slug: vr
- name: webvr
  slug: webvr
seo_title: Créer un jeu VR multijoueur basé sur navigateur avec A-Frame, PubNub et
  WebVR
seo_desc: 'By Namratha Subramanya

  Advancements in technology have made Virtual Reality (VR) more immersive and affordable
  than ever. This immersive environment can be similar to the real world. Or it can
  be fantastical, creating an experience that is not possib...'
---

Par Namratha Subramanya

Les avancées technologiques ont rendu la réalité virtuelle (VR) plus immersive et abordable que jamais. Cet environnement immersif peut être similaire au monde réel. Ou il peut être fantastique, créant une expérience impossible dans la réalité ordinaire.

Mieux encore, des dispositifs VR de haute qualité sont disponibles à bas prix ces jours-ci. Avec un certain nombre de casques VR compatibles avec les smartphones tels que Google Cardboard, Samsung Gear VR, Oculus Rift et HTC Vive, la VR s'impose comme la prochaine grande révolution.

Dans ce tutoriel, nous allons exploiter cela et construire un jeu VR multijoueur en temps réel en utilisant A-Frame, PubNub, Glitch et WebVR.

Le [dépôt de code GitHub complet peut être trouvé ici](https://github.com/namrathasubramanya/VR-Bowling-game).

### WebVR

[WebVR](https://webvr.info/) est une spécification ouverte qui permet de vivre la VR dans votre navigateur. Il s'agit d'une API JavaScript pour navigateur qui sert d'interface pour le matériel VR. WebVR est multiplateforme et peut être utilisé pour développer, visualiser et partager du contenu VR sur n'importe quel navigateur prenant en charge la VR. Avec WebVR, vous pouvez ouvrir un navigateur et entrer dans la VR simplement en cliquant sur un lien. Travailler directement avec WebVR nécessite des connaissances en JavaScript et WebGL.

### A-Frame

[A-Frame](https://aframe.io/) est un framework de réalité virtuelle construit sur l'API WebVR. Il utilise l'API WebVR pour accéder aux données des capteurs du casque VR (position, orientation) afin de transformer la caméra et de rendre le contenu directement sur les casques VR. A-Frame est un projet communautaire ouvert qui utilise l'API WebVR ainsi que HTML, CSS, JavaScript et Three.js. A-Frame vise un contenu VR hautement immersif et interactif avec des performances natives. En même temps, A-Frame souhaite que tout le monde puisse participer à la création de contenu VR. A-Frame prend en charge tous les principaux casques avec leurs contrôleurs.

### Glitch

[Glitch](https://glitch.com/~aframe) fournit un éditeur de code en ligne avec déploiement et hébergement instantanés de sites web. L'éditeur prend en charge le code front-end et back-end ainsi que plusieurs fichiers et répertoires. Glitch vous permet de remixer (c'est-à-dire copier) des projets existants et de les rendre vôtres, puis d'héberger et de déployer instantanément les modifications pour que tout le monde puisse les voir. Firefox Nightly vous permet de déboguer le contenu VR à l'aide de la console de débogage.

### Environnement de jeu

#### Système de physique A-Frame

`aframe-physics-system` est un middleware qui initialise le moteur physique et expose des composants A-Frame que nous pouvons appliquer aux entités. Lorsque nous utilisons ses composants `static-body` ou `dynamic-body`, `aframe-physics-system` crée une instance `Cannon.Body` et l'attache à nos entités A-Frame, de sorte que, à chaque frame, il ajuste la position, la rotation, etc. de l'entité pour correspondre au corps.

#### Balle

L'élément primitif `<a-sphere>` crée une forme sphérique. Vous pouvez définir son rayon, sa couleur et sa position. Grâce à `aframe-physics-system`, la balle peut être convertie en un corps dynamique avec une certaine masse.

#### Piste de bowling

`<a-box>` crée des formes telles que des boîtes, des cubes ou des murs. Vous pouvez créer une boîte rectangulaire et en faire une piste de bowling en plaçant des quilles et une balle dessus.

#### Quilles

L'élément primitif `<a-cylinder>` est utilisé pour créer des tubes et des surfaces courbes. Ces cylindres peuvent être utilisés comme quilles dans le jeu. Assurez-vous de définir le rayon, la hauteur, la position et la masse du cylindre.

#### Pistes

La balle ne peut pas rouler dans la même direction à chaque fois que vous la lancez. Vous pouvez définir un nombre quelconque de pistes pour que la balle roule, et cette piste peut, à son tour, définir la direction. Ce jeu a 5 pistes, et le mouvement de la balle sur ces pistes est contrôlé par 5 triangles ou, disons, des pointeurs sur la piste de bowling.

#### Environnement

Une scène est représentée par l'élément `<a-scene>`. La scène est l'objet racine global, et toutes les entités sont contenues dans la scène. Les frottements, la restitution et les itérations des objets sont définis à des valeurs de 0,001, 0,3 et 30 respectivement.

A-Frame dispose d'un système de gestion des actifs qui nous permet de placer nos actifs à un seul endroit et de précharger et mettre en cache les actifs pour de meilleures performances. Nous plaçons de tels actifs dans `<a-assets>`.

Le composant scale définit une transformation de rétrécissement, d'étirement ou de cisaillement d'une entité. Vous pouvez utiliser le composant scale pour transformer une boîte en un mur derrière la piste de bowling.

Sur des lignes similaires, une boîte peut être convertie en un bouton attaché au mur en utilisant le composant scale. `<a-text>` peut ajouter du texte dans votre environnement virtuel.

`<a-box>` peut également être utilisé pour construire des bordures à côté de la piste de bowling.

### Le Jeu

#### Lancer la balle

Comme discuté précédemment, la balle peut rouler sur 5 pistes imaginaires sur la piste de bowling. Cela peut être réalisé en utilisant `<a-animation>`. Les animations peuvent être attachées dans A-Frame via l'élément `<a-animation>` en le faisant enfant de l'entité à animer.

Maintenant, vous pouvez lier ces animations de la balle avec les 5 pointeurs de sorte que l'animation commence chaque fois qu'un des triangles est cliqué. Cela peut être réalisé en écrivant un composant. Nous pouvons enregistrer le composant en JavaScript et l'utiliser de manière déclarative depuis le DOM. Les composants sont configurables, réutilisables et partageables.

#### Chute des quilles

Lorsque un corps dynamique de masse 17,5 roule vers 10 corps dynamiques de masse 1,25, certains d'entre eux tendent à tomber. Après chaque chute, on peut compter le nombre de quilles qui sont tombées. Nous pouvons vérifier la position des quilles à la fin de l'animation. Si la rotation de l'une des quilles a une valeur x différente de 0 ou -0, cela signifie que la quille n'est pas debout. En comptant le nombre de quilles qui sont couchées, vous pouvez calculer le score du joueur.

La ligne ci-dessus capture la valeur x de l'attribut de rotation d'une quille. De cette manière, vous pouvez récupérer la valeur x de l'attribut de rotation de toutes les quilles et la sauvegarder dans un tableau. Maintenant, vous pouvez parcourir le tableau et vérifier chaque valeur et incrémenter le compteur `strike`.

#### Nouvelle partie

Le joueur peut commencer une nouvelle partie à tout moment en cliquant sur le bouton Nouvelle Partie sur le mur. Cela rafraîchit automatiquement le jeu.

#### Déplacement de la caméra

Vous pouvez déplacer la caméra à tout moment pendant le jeu. Ici, j'ai choisi de déplacer la caméra chaque fois que le joueur lance la balle pour une meilleure vue des quilles qui tombent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kZFpH7Qepl0i1OtR7jwmrg.png)

### PubNub

Avec une latence inférieure à 1/4 de seconde, PubNub peut publier et recevoir des messages en douceur entre plusieurs dispositifs VR. Convertissons ce jeu solo en un jeu à 2 joueurs.

Vous devrez maintenant initialiser vos clés PubNub. [Inscrivez-vous pour un compte PubNub](https://admin.pubnub.com/#/register/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q3-Medium-Aug-17) et créez un projet dans le [Tableau de bord Admin](https://admin.pubnub.com/#/register?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q3-Medium-Aug-17).

#### Décider des tours

Chaque joueur a deux tours. Le joueur change de tour après chaque deux lancers. Ainsi, après chaque deux lancers, PubNub peut notifier l'autre utilisateur qu'il peut prendre le contrôle. Dans ce jeu, chaque fois que le joueur a son tour, les 5 pointeurs triangulaires apparaissent sur la piste de bowling. Et quand ce n'est pas leur tour, les 5 pointeurs triangulaires sont cachés.

Cachez les pointeurs quand ce n'est pas votre tour. Ici, au lieu de cacher, je définis la position à 0.

Faites réapparaître les pointeurs sur la piste de bowling quand c'est votre tour. En faisant cela, vous reprenez le contrôle des pistes.

#### Répliquer l'état des quilles après la chute

Après chaque chute, vous pouvez capturer la position des quilles qui sont tombées et l'envoyer à l'autre utilisateur en utilisant PubNub. En faisant cela, vous pouvez répliquer l'écran d'un joueur sur les écrans des autres joueurs. Dans le code ci-dessous, vous pouvez voir que les valeurs de position et de rotation de la quille 1 sont transmises aux autres joueurs via PubNub. De la même manière, vous pouvez envoyer les valeurs de rotation et de position de toutes les quilles via PubNub.

#### Basculer entre les corps statiques et dynamiques

Auparavant, nous avons utilisé `aframe-physics-system` pour convertir les objets A-Frame en corps dynamiques. Lorsque le joueur ne lance pas la balle et se contente de répliquer l'écran d'un autre joueur, la balle ne doit pas être un corps dynamique afin d'éviter la chute de quilles supplémentaires.

Lorsque c'est le tour du joueur actuel, les dynamiques sont définies sur vrai, et les propriétés `dynamic-body` sont ajoutées.

Lorsque ce n'est pas le tour du joueur, les dynamiques sont définies sur faux, et les propriétés `dynamic-body` sont supprimées.

#### Joueur 2

Une fois que vous avez terminé la publication des données via PubNub depuis l'écran du Joueur 1, vous pouvez lire les données en vous abonnant au canal de PubNub.

Lorsque PubNub reçoit des données liées à la position et à la rotation des quilles tombées, vous pouvez définir les attributs des quilles sur l'écran du joueur 2 aux mêmes valeurs que celles du Joueur 1 et ainsi rendre les deux écrans identiques.

### Conclusion

Félicitations ! Chaque fois que vous lancez la balle sur l'écran du Joueur 1, vous pouvez voir l'écran du Joueur 2 répliquer tous les mouvements. Maintenant, vous pouvez inverser cela en publiant les données du Joueur 2 vers le Joueur 1 et convertir votre jeu en un jeu à deux joueurs entièrement fonctionnel. Il peut également être converti en un jeu multijoueur. Bon jeu VR !

**Le [dépôt de code GitHub complet peut être trouvé ici](https://github.com/namrathasubramanya/VR-Bowling-game).**

_Publié à l'origine sur [www.pubnub.com](https://www.pubnub.com/blog/build-multiplayer-browser-based-vr-game-aframe-webvr/?utm_source=Syndication&utm_medium=Medium&utm_campaign=SYN-CY18-Q3-Medium-Aug-17)._