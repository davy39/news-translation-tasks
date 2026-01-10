---
title: Comment commencer avec la réalité augmentée en Swift en décorant votre maison
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T19:03:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-augmented-reality-in-swift-by-decorating-your-home-85671482df3c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ycF6WrJkcT0SUg45pM-reg.jpeg
tags:
- name: Augmented Reality
  slug: augmented-reality
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: Comment commencer avec la réalité augmentée en Swift en décorant votre
  maison
seo_desc: 'By Ranadhir Dey

  If you’ve read my previous post, you already have a beautiful AR floor in your dining
  room. That was the first thing we built while learning the basics of AR. And now,
  it’s time to decorate the room with some cool virtual furniture. A...'
---

Par Ranadhir Dey

Si vous avez lu mon précédent article, vous avez déjà un beau sol AR dans votre salle à manger. C'était la première chose que nous avons construite en apprenant les [bases de la RA](https://medium.freecodecamp.org/how-to-get-started-with-ar-in-swift-the-easy-way-7399fe1c82f5). Et maintenant, il est temps de décorer la pièce avec quelques meubles virtuels sympas. À la fin de ce tutoriel, vous aurez une salle à manger comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ANkvfr-d7BmwxS_AxGD6zw.gif)

### Nommer les SCNNodes

Mettons-nous au travail. Lancez Xcode et ouvrez le [dernier projet](https://github.com/ranadhirdey/Home-Decor) où nous avons décoré notre sol. Avant viewDidLoad, créez une constante floorNodeName.

```
let floorNodeName = "FloorNode"
```

Nous allons maintenant définir le nom du nœud de sol avec cette constante afin de ne pas confondre ce nœud avec d'autres nœuds de meubles. Allez à la méthode createFloorNode et nommez le nœud de sol.

À la ligne 7, nous avons simplement nommé le nœud de sol — tout le reste reste le même.

Le plan est que, une fois lancé, l'application reconnaîtra d'abord le sol, puis l'utilisateur verra à travers l'écran pour déterminer où il veut placer les meubles. Il tapera sur l'emplacement et un meuble sera placé juste là. Pour y parvenir, nous avons besoin d'une corrélation entre les points à l'écran et les emplacements réels. Heureusement, Apple a rendu ce processus assez simple.

### Gestes et HitTests

Une session AR active continue de trouver des objets/plans à proximité. Une fois qu'un nouvel objet/plan est trouvé, il place des ancres AR dessus. Pour trouver exactement sur quelles ancres l'utilisateur a tapé, nous avons besoin de l'aide de [HitTest](https://developer.apple.com/documentation/arkit/arframe/2875718-hittest). HitTest fonctionne comme suit :

* un rayon logique est tiré du point de contact vers les ancres sur le plan
* toutes les ancres que le rayon traverse sont stockées dans un tableau au format [HitTestResult](https://developer.apple.com/documentation/arkit/arhittestresult).

Chaque HitTestResult contient les informations de la surface réelle d'une ancre AR. Nous utiliserons ces informations HitTestResult pour placer nos meubles.

Créons une méthode qui ajoute le geste de tapotement à notre sceneView pour interagir avec l'utilisateur. Nous appellerons cette méthode depuis viewDidLoad.

Maintenant, définissez la méthode "tapped" pour obtenir l'emplacement du tapotement et y placer un meuble. Pour l'instant, nous imprimons pour tester si le HitTest fonctionne correctement.

Dans la première ligne, nous castons la vue du geste de tapotement en ARSCNView. Comme nous savons que le tapotement viendra de notre sceneView elle-même, nous le déballons de force. Ensuite, nous obtenons l'emplacement sur sceneView où l'utilisateur a tapé. Ensuite, un HitTest est effectué pour obtenir tous les HitTestResults de l'emplacement tapé aux ancres réelles. "existingPlaneUsingExtent" donne la taille estimée des plans détectés. Maintenant, nous vérifions si l'utilisateur a réellement tapé sur un plan détecté ou ailleurs, et nous imprimons en conséquence.

Maintenant, exécutez l'application, attendez que l'origine du monde se charge et que le sol soit détecté. Ensuite, tapez sur l'écran pour vérifier si nous touchons les plans correctement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hPQSMPreK6Nv3bypYaaR_Q.png)

Si vous tapez sur les endroits où se trouvent les carreaux, il imprimera "Touched on the plane." Touchez ailleurs, et ce sera "Not a plane." S'il n'y a pas de sortie dans la console, vous n'avez pas appelé la méthode addTapGesture depuis viewDidLoad (cela m'est arrivé !). Maintenant que nous avons détecté avec succès la position cliquée, il est temps de ramener quelques meubles à la maison.

### Importer des modèles 3D dans le projet

Nous avons besoin de quelques modèles de meubles 3D. J'utilise [turbosquid](https://www.turbosquid.com/), qui est un excellent dépôt de modèles 3D. Vous devez créer un compte gratuit pour accéder à leurs modèles gratuits. J'ai téléchargé une [table](https://www.turbosquid.com/3d-models/3d-small-dining-table-1161153) en 3D pour l'instant (dans le dépôt GitHub — j'ajouterai d'autres meubles également).

[Apple conseille](https://developer.apple.com/documentation/scenekit/scnscenesource?changes=_4) d'utiliser des modèles au format collada (.dae) dans SceneKit. J'ai utilisé d'autres types de modèles par le passé, et j'ai rencontré des problèmes dans de nombreux cas. Principalement, s'il y a du verre, SceneKit tend à le rendre solide. Alors, trouvons des modèles 3D avec une extension .dae.

Maintenant, ajoutez un dossier d'actifs sous le groupe "Home Decor".

![Image](https://cdn-media-1.freecodecamp.org/images/1*uZdqGuSoLDUxBwrXlOYxUQ.png)

Appuyez sur suivant, et dans la boîte de dialogue d'enregistrement, enregistrez-le sous furnitures.**scnassets** et non xcassets.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xtrw-mhR3k5NKcfRtOUoZw.png)

### Travailler avec l'éditeur SceneKit de Xcode

Tous les fichiers de scène ou modèles qui seront utilisés par SceneKit doivent résider dans un dossier scnassets. Maintenant, faites glisser et déposez la table que nous venons de télécharger dans le dossier scnassets et renommez-la en "Table". Cliquez sur le fichier Table.dae (s'il n'est pas déjà ouvert) pour l'ouvrir dans l'éditeur SceneKit. Dans le coin inférieur gauche, il y a un bouton (marqué d'une ellipse rouge ci-dessous) pour ouvrir la vue du graphe de scène. Cliquez dessus et l'éditeur devrait apparaître comme ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qffmqaKYDb8vMjRCiqB-8g.png)

Dans le graphe de scène, il y a 3 nœuds : une caméra, une source de lumière (Lampe) et la table (Small_table). ARKit a sa caméra par défaut, donc nous n'avons plus besoin de cette caméra. Comme nous utiliserons l'éclairage par défaut de sceneView, nous n'avons pas besoin de la lampe non plus. Supprimez les deux.

Renommons "Small_table" en "Table", comme le nom du fichier. Maintenant, le graphe de scène ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FSabN1vH7ZexHcv6Wmscdw.png)

Il y a quelque chose appelé point de vue (marqué d'une ellipse rouge ci-dessus) dans l'éditeur qui détermine comment l'objet apparaîtra d'un certain point de vue. Par défaut, il est réglé sur Perspective, mais nous verrons la table de face. Changez donc le point de vue en Front.

Oups — il semble que nous ne puissions voir que la vue de dessus. Clairement, ce n'est pas comme cela que nous aimerions la voir. Nous voulons voir la table comme elle était montrée dans la vue en perspective. Corrigons cela.

Sélectionnez le nœud Table, ouvrez l'onglet Utilities (bouton en haut à droite dans Xcode) et cliquez sur l'inspecteur de nœud (l'icône du cube). Vous devriez voir la fenêtre ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vt6XWmh6fsRBmBIbe1Qgaw.png)

J'ai numéroté les étapes pour votre référence. Pour voir la table complète de face, nous devons faire tourner la table sur son axe X. Si vous pouvez vous en souvenir, nous avons fait le même genre de chose dans le [premier article](https://medium.freecodecamp.org/how-to-get-started-with-ar-in-swift-the-easy-way-7399fe1c82f5) où nous avons fait tourner la capsule sur son axe Z en changeant son angle d'Euler.

Si vous regardez la matrice de transformation, l'angle d'Euler pour X est déjà spécifié à 90 degrés radians, ce qui fait que la table est tournée incorrectement. Mettez-le à zéro et la rotation sera corrigée. Mais le positionnement a un vecteur de (-0.35, 0.348, 0). Nous allons le mettre à (0, 0, 0) pour placer la table exactement là où l'utilisateur tapera. Maintenant, la transformation ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZnK7C1ACHG-roVzMnNCWsg.png)

L'édition de la matrice de transformation est une tâche un peu par essais et erreurs. Vous devrez peut-être passer par un certain nombre d'itérations avant d'atteindre la position exacte.

Maintenant, nous changeons le modèle .dae en un fichier de scène SceneKit (.scn) qui le rendra beaucoup plus efficace pour que SceneKit le gère. Allez dans Editor>Convert to SceneKit scene file(.scn).

Et… nous avons terminé avec l'édition de l'objet 3D. Retournez au fichier ViewController. Tout d'abord, puisque nous avons supprimé la source de lumière de la table, nous devons activer l'éclairage par défaut de la vue de scène dans viewDidLoad.

sceneView.autoenablesDefaultLighting = true

### Positionner des objets 3D

Ensuite, nous créons une méthode pour ajouter la table à la scène. Elle acceptera un HitResult comme paramètre et placera la table en fonction de la position du HitResult.

Soyez patient avec moi — c'est la dernière méthode qui nécessite quelques explications !

1. Une constante est déclarée pour savoir quel meuble de scène doit être ajouté. Nous la changerons en variable et la déclarerons en haut du viewcontroller lorsque nous aurons plus de meubles.
2. Ensuite, nous créons une scène à partir du fichier de meuble sélectionné.
3. Un nœud de meuble est créé à partir du nœud enfant du nœud racine de la scène de meuble avec le nom du meuble. Comme nous avons nommé le premier nœud de la même manière que le nom du meuble, il n'a pas besoin de parcourir plus loin. Par conséquent, l'option récursive est définie sur false.
4. La propriété [worldTransform](https://developer.apple.com/documentation/arkit/arhittestresult/2867907-worldtransform) de HitResult contient la matrice de transformation de corrélation entre la position réelle et la position de l'ancre/nœud de la scène. Et la 3ème colonne de la matrice de transformation contient les informations de position.
5. Maintenant que nous avons extrait avec succès la coordonnée mondiale de l'emplacement tapé, notre travail consiste simplement à placer le nœud de meuble sur cette même coordonnée exacte.
6. Ensuite, nous ajoutons le nœud au nœud racine de la scène. Et c'est tout !

Maintenant, nous devons simplement appeler la méthode chaque fois que l'utilisateur tape sur l'écran. Modifions la méthode tapped pour accommoder ce changement.

Ici, si nous trouvons un plan, nous appelons simplement la méthode pour ajouter le meuble. Comme HitTest contient toutes les positions que le rayon traverse, nous considérons le résultat le plus élevé. Exécutons l'application, attendons que le sol ait des carreaux, puis tapons sur l'écran pour placer une table. Et voilà ! Vous avez une nouvelle table sur votre sol. Faites attention à votre pas :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*HMeqtcy7IoAzqkiwRoPBkg.png)

J'ai téléchargé quelques autres meubles et les ai ajoutés au dépôt. J'ai également ajouté des gestes de pincement et de rotation pour redimensionner et faire tourner les objets. Le code source complet vous donnera une apparence comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ycF6WrJkcT0SUg45pM-reg.jpeg)

Vous pouvez télécharger le code source complet depuis [GitHub](https://github.com/ranadhirdey/Home-Decor-With-Furniture).

J'espère que vous avez apprécié la lecture de cet article autant que j'ai apprécié l'écrire :)

À la prochaine. Bonne lecture !!