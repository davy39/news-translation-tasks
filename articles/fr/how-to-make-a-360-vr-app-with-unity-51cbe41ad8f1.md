---
title: Voici comment créer une application VR 360 en 10 minutes avec Unity
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-23T03:54:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-360-vr-app-with-unity-51cbe41ad8f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*US4qmns1r1F0BKMxBpeYcg.png
tags:
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: unity
  slug: unity
- name: Virtual Reality
  slug: virtual-reality
seo_title: Voici comment créer une application VR 360 en 10 minutes avec Unity
seo_desc: 'By Adriana Vecchioli

  Virtual Reality (VR) is exciting. It’s also the New Frontier of app development.

  VR is poised to give birth to new forms of storytelling and emotionally powerful
  experiences. Yet making VR is perceived as intimidating: it’s expen...'
---

Par Adriana Vecchioli

La réalité virtuelle (VR) est passionnante. C'est aussi la nouvelle frontière du développement d'applications.

La VR est sur le point de donner naissance à de nouvelles formes de narration et à des expériences émotionnellement puissantes. Pourtant, la création de VR est perçue comme intimidante : elle est coûteuse et nécessite à la fois du matériel spécial et des compétences.

Mais cela change, car des outils intuitifs et du matériel abordable rendent le développement VR accessible. Ce tutoriel vous montrera comment créer une application vidéo 360 sur Android et Google Cardboard en quelques minutes seulement. Et presque aucun codage requis ;)

Le développement VR ne devrait pas être un obstacle pour donner vie à vos idées. Commençons :

### **Ce dont vous avez besoin**

Voici notre liste de courses :

? Un téléphone Android avec un gyroscope pour détecter les mouvements de la tête, fonctionnant sous KitKat ou une version plus récente.

? Un casque Cardboard. Si vous n'en possédez pas, vous pouvez en trouver beaucoup sur Amazon pour moins de 10 dollars. Celui-ci est mon préféré.

? Unity3D, un moteur de jeu multiplateforme, que vous devez installer sur votre ordinateur, version 5.6 ou plus récente. Nous utiliserons ce logiciel pour construire notre projet entier.

? Le SDK GoogleVR pour Unity, que vous pouvez télécharger au préalable.

? Une vidéo 360. Tournez-en une avec une caméra 360 (en voici une que vous pouvez brancher sur votre téléphone) ou trouvez-en une en ligne.

### **Comment construisons-nous cette application ?**

Contrairement à la vidéo régulière qui a un cadre rectangulaire, la vidéo 360 a la forme d'une sphère. Nous devons donc d'abord créer un écran sphérique pour projeter notre vidéo 360. Le joueur (ou spectateur) sera situé à l'intérieur de cette sphère et pourra regarder la vidéo dans n'importe quelle direction.

Les étapes ci-dessous devraient vous donner les moyens d'apporter vos propres modifications, en expliquant comment tout cela fonctionne sous le capot. Pour des instructions pas à pas, reportez-vous à la vidéo.

### **Étape 1 : Construire une sphère ?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*jvbDMcNGQU9l9lnNSFij5w.png)

Tout d'abord, ouvrons un nouveau projet Unity si vous commencez à partir de zéro (ou une nouvelle scène si vous souhaitez intégrer le lecteur vidéo 360 dans un projet existant). Pensez à une scène comme à un niveau d'un jeu vidéo, et à un projet comme à un jeu complet.

Ensuite, ajoutez un objet sphère dans la scène, placé à son centre (Position = 0, 0, 0), avec un rayon de 50 (Échelle = 50, 50, 50). La position de la caméra doit également être définie à 0, 0, 0. La caméra est les yeux du joueur/spectateur, nous la voulons donc au centre de la sphère. La placer ailleurs rendrait la vidéo déformée.

Une fois la caméra placée à l'intérieur de la sphère, cette dernière n'est plus visible dans la scène. Ne vous inquiétez pas, il y a une explication à cela ! En effet, la plupart des moteurs de jeu ne rendent pas, par défaut, le côté intérieur des objets 3D. Cela est dû au fait que nous avons rarement besoin de les voir, ce serait une perte de ressources de les rendre. Nous allons corriger cela ensuite.

### **Étape 2 : Inverser les normales de la sphère ?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*NXKLWLDirFigK2Zx9L8IoQ.png)

Dans notre cas, nous devons voir notre sphère de l'intérieur. C'est tout l'intérêt de l'application, nous allons donc la retourner à l'envers.

Dans Unity, les sphères ne sont pas réellement des sphères (quoi ? On nous a menti tout du long !), ce sont des polygones composés de milliers de petites facettes. Les côtés externes des facettes sont visibles, mais pas les côtés internes. Pour cette raison, nous allons créer un programme pour retourner ces petites facettes comme des crêpes.

En géométrie 3D, nous appelons cette transformation « inverser les normales » ou « retourner les normales ».

Nous allons utiliser un programme appelé un Shader, que nous appliquerons au Matériau de la Sphère. Les matériaux contrôlent l'apparence des objets dans Unity. Les shaders sont de petits scripts qui calculent la couleur de chaque pixel rendu, en fonction de l'éclairage et des informations tirées de leurs Matériaux.

Créez donc un nouveau Matériau pour la Sphère, puis un nouveau Shader appliqué à ce Matériau. Nous devons écrire du code personnalisé pour le Shader... mais n'ayez pas peur, vous pouvez copier-coller le code ci-dessous :

Ce petit Shader va retourner chaque pixel de la sphère à l'envers. Maintenant, notre Sphère apparaît comme une grande boule blanche, vue de l'intérieur, dans notre Scène. L'étape suivante consiste à transformer cette sphère blanche en un lecteur vidéo.

### **Étape 3 : Projeter votre vidéo 360 à l'intérieur de la Sphère ?**

Ici, vous devez avoir une vidéo 360 mp4 à portée de main. Importez-la dans le projet, puis faites-la glisser sur la Sphère. Et c'est là que la magie opère : un composant 'Video Player' apparaît et boom, la vidéo est prête à être lue.

Vous pouvez jouer avec les paramètres comme les boucles et l'audio. Il supporte également le streaming !

### **Étape 4 : Configurer Google Cardboard ?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*nLFO9-K8swJjfRYTByT15g.png)

Dans cette étape, nous allons rendre l'expérience vraiment immersive. C'est pourquoi nous voulons la visualiser dans un casque VR, ici un Google Cardboard.

Nous allons créer une vue « stéréoscopique » (l'écran sera divisé en deux, avec quelques effets de fisheye des deux côtés — un côté pour chaque œil), en utilisant le SDK GoogleVR. L'effet fisheye sur chaque œil, combiné avec la distorsion des lentilles en plastique du Cardboard, est ce qui vous donne l'illusion de profondeur et d'immersion.

Pour ajouter le SDK GoogleVR à notre projet, téléchargez et importez le plugin, puis nous ajusterons un ensemble de paramètres Android :

* Allez dans le menu de la barre supérieure > Fichier > Paramètres de construction. Ajoutez votre scène ouverte si elle n'est pas déjà ajoutée, puis sélectionnez Android dans la liste des plateformes supportées.
* Cliquez sur Basculer la plateforme. Cela devrait prendre un peu de temps la première fois que vous effectuez le basculement.
* Cliquez sur Paramètres du joueur. Les composants apparaissent dans le panneau de l'inspecteur.

Dans l'inspecteur des paramètres du joueur, sous la section 'Autres paramètres' :

* Cochez Réalité virtuelle supportée. Sous SDK de réalité virtuelle, sélectionnez l'icône +, puis sélectionnez Cardboard pour l'ajouter à la liste.
* Entrez un nom de package dans le champ Identifiant du bundle (par exemple, com.votredomaine.demo360). Il doit être unique et est utilisé pour distinguer notre application des autres dans le Google Play Store.
* Définissez le menu déroulant Niveau d'API minimum sur « Android 4.4 'Kit Kat' (niveau d'API 19) ».

Ensuite, prenez l'élément 'GvrViewerMain' du dossier GoogleVR\Prefabs dans le navigateur de projet, et faites-le glisser dans la scène. Dans l'inspecteur, donnez-lui la même Position que le centre de la Sphère — (0, 0, 0).

Le prefab GvrViewerMain contrôle tous les paramètres du mode VR, tels que l'adaptation de l'écran aux lentilles du Cardboard. Il communique également avec le gyroscope de votre téléphone pour suivre les mouvements de votre tête. Lorsque vous tournez la tête, la caméra et ce que vous voyez tournent également à l'intérieur du lecteur vidéo 360.

Maintenant, vous pouvez regarder dans toutes les directions lorsque la vidéo est en marche et que l'écran est divisé en deux, pour accommoder les deux lentilles du Cardboard.

### **Étape 5 : Exécuter l'application sur Android ?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*6ZeCWw1dEKNNT7iLtXfndQ.png)

Pour notre dernière étape, nous allons exécuter l'application sur un téléphone Android et la partager avec des amis !

Il y a deux façons de faire cela :

* Retournez à Fichier > Paramètres de construction. Vous pouvez brancher un téléphone Android avec un câble USB à votre ordinateur et cliquer sur Construire et exécuter. Cela installe l'application directement sur votre téléphone.
* L'autre option est de cliquer sur Construire uniquement. Cela ne l'installe pas sur un téléphone, mais génère plutôt un fichier APK. Vous pouvez partager l'APK par e-mail avec quiconque souhaite essayer le chef-d'œuvre que vous venez de créer. Ils doivent double-cliquer sur la pièce jointe APK pour l'installer sur leurs téléphones.

Pendant le processus de construction, il peut vous être demandé de sélectionner le dossier racine du SDK Android. Si c'est le cas, téléchargez le SDK Android puis sélectionnez son emplacement de dossier.

Lancez l'application, placez votre téléphone dans un casque Cardboard, et vous êtes prêt à partir ! Vous pouvez remplacer la vidéo par n'importe quoi au format 360 et vivre l'immersion VR 360 chez vous.

### **Aller plus loin**

Félicitations, vous avez créé une application vidéo 360, et vous n'êtes qu'à un pas de créer une application vidéo VR ! Bien que les termes soient souvent utilisés de manière similaire, 360 et VR définissent deux expériences différentes :

* La vidéo 360 est enregistrée sous tous les angles, avec une caméra spéciale ou un assemblage de plusieurs caméras. L'utilisateur peut regarder dans n'importe quelle direction souhaitée, mais il n'y a pas d'interactivité dans l'expérience.
* La VR fait généralement référence à un environnement généré par ordinateur dans lequel l'utilisateur est immergé. C'est une expérience interactive : le joueur peut se déplacer et contrôler des objets, en plus de regarder dans toutes les directions.

Votre nouvelle application peut servir de point de départ pour construire une expérience VR plus riche. Unity dispose de nombreuses fonctionnalités que vous pouvez exploiter, comme l'ajout d'éléments 3D ou de cool effets de particules ✨ pour superposer et améliorer votre vidéo, ou l'ajout de quelques éléments interactifs.

Vous pouvez également placer un environnement 3D complet à l'intérieur du lecteur vidéo 360 et utiliser ce dernier comme une skybox. L'utilisateur peut naviguer dans le décor, en utilisant ce script de marche pratique.

Laissez libre cours à votre imagination et montrez-moi vos créations : tweetez-moi @AdrianaVecc ou laissez un commentaire.

Créer de belles histoires VR est difficile. Les construire ne devrait pas l'être.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9iyrdtDJfikdkJBKpmWzPQ.png)

**Si vous avez aimé cet article, appuyez sur le ? ci-dessous pour que d'autres personnes puissent le voir.**

Adriana est une artiste et designer de produits qui crée des expériences VR pour développer l'empathie. Si vous souhaitez donner vie à vos idées VR, envoyez-nous un e-mail : hello@vrtiginous.com ?