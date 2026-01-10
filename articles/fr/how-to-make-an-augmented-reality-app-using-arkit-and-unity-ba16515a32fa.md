---
title: Bonjour, Kitty ! Comment créer une application de réalité augmentée avec ARKit
  et Unity.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-07T16:57:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-an-augmented-reality-app-using-arkit-and-unity-ba16515a32fa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sybYCmTLY_r_rmRrim2AgA.jpeg
tags:
- name: Apple
  slug: apple
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Virtual Reality
  slug: virtual-reality
seo_title: Bonjour, Kitty ! Comment créer une application de réalité augmentée avec
  ARKit et Unity.
seo_desc: 'By Francesco Pallotta

  We’ve all heard of Augmented Reality (AR), but at this point there are few opportunities
  to see this technology in action. We know that AR allows us to see virtual elements
  fused with the real world around us. For example, with ...'
---

Par Francesco Pallotta

Nous avons tous entendu parler de la réalité augmentée (AR), mais à ce jour, il y a peu d'opportunités de voir cette technologie en action. Nous savons que l'AR nous permet de voir des éléments virtuels fusionnés avec le monde réel qui nous entoure. Par exemple, avec l'AR, nous pouvons voir un canapé virtuel dans notre salon. Apple nous permet désormais de voir de nouveaux objets ajoutés au monde réel en utilisant les caméras de nos téléphones.

Apple a introduit ARKit, le framework pour créer des expériences en réalité augmentée, dans iOS 11. ARKit utilise l'odométrie visuelle inertielle (VIO) pour cartographier l'environnement environnant. Le VIO combine les données fournies par le capteur de la caméra avec les données de Core Motion. Les données de Core Motion sont collectées via l'accéléromètre, le gyroscope, le podomètre, le magnétomètre et le baromètre.

Toutes ces entrées permettent à l'appareil de comprendre son mouvement dans une pièce. Avec ARKit, l'iPhone et l'iPad peuvent analyser une scène et trouver les plans horizontaux d'une pièce. ARKit peut localiser les tables et les sols, et peut tracer et positionner des objets à des points précis.

ARKit utilise également le capteur de la pièce pour mesurer la lumière ambiante et appliquer la quantité correcte de lumière aux objets virtuels. ARKit est compatible avec les processeurs A9, A10 et A11 d'Apple. Pour développer avec ARKit, vous pouvez utiliser Metal, Scenekit et des outils tiers tels que Unity et Unreal Engine.

Voyons maintenant comment créer une application AR en utilisant ARKit.

### Environnement de développement

Pour commencer, nous avons besoin de :

* La version stable de [Unity 2017.1.0](https://unity3d.com/get-unity/download?thank-you=update&download_nid=47505&os=Mac) ou ultérieure. ARKit est également compatible avec la [version expérimentale VR](http://beta.unity3d.com/download/c92f68c59a22/public_download.html) utilisée pour la création de contenu VR macOS et les versions Unity 5.x de [Unity 5.6.2](https://unity3d.com/get-unity/download?thank-you=update&download_nid=47271&os=Mac) ou ultérieures.
* iOS 11 ou ultérieur
* XCode 9 bêta ou ultérieur, avec le SDK iOS qui inclut le framework ARKit
* Un appareil iOS compatible avec ARKit (iPhone 6S ou ultérieur, iPad 2017 ou ultérieur)

### Procédure

Démarrez Unity. La fenêtre du projet s'ouvrira.

À ce stade, nous devons créer un nouveau projet vide :

1. Dans la fenêtre, cliquez sur **New** pour un nouveau projet.
2. Écrivez « ARKitty » dans la zone de texte **Nom du projet**.
3. Dans la même fenêtre, appuyez sur le bouton **Créer le projet**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bA4I0lnMGQeNJOJB3l3sMQ.png)

Nous avons créé notre projet AR !

Ouvrez l'**Asset Store** en cliquant sur cet onglet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*M27Cvn-q9LT5ihs3Ue4tDA.png)

Ensuite, recherchez dans le magasin : écrivez « ARKit » dans la zone de texte et cliquez sur l'icône de la loupe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Tx44H1h35r166e552nzLKw.png)

Faites défiler la fenêtre de l'Asset Store jusqu'à trouver « Unity ARKit Plugin ». C'est le plugin qui intègre ARKit dans Unity.

![Image](https://cdn-media-1.freecodecamp.org/images/0*uk87mkA8rHUP_Lcq.png)

Cliquez sur Unity ARKit Plugin et faites défiler jusqu'au bouton **Import** et appuyez dessus. Appuyez à nouveau sur import pour importer le même projet, puis importez une fois de plus dans la fenêtre de l'élément du plugin.

Retournez à l'Asset Store, appuyez sur le symbole **Accueil**, et écrivez « Cute Kitten » dans le champ de recherche. Appuyez sur le symbole de recherche et importez le modèle Cute Kitten comme vous l'avez fait avec le plugin ARKit.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ghwgXn4-isL8Eqd8.png)

Faites défiler avec le curseur jusqu'au bouton d'importation et appuyez dessus. Appuyez à nouveau sur import dans la fenêtre de l'élément du plugin.

Recherchez la scène « UnityARKitScene » dans le dossier UnityARKitScene sous « Asset/Examples ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZMRD69z37L17Kk7inyHEdQ.png)

Glissez la scène « UnityARKitScene » sous Hierarchy.

Allez dans les assets et trouvez Kitten.

Allez sous **Model** et glissez « kitten » sous « Hierarchy-> HitCubeParent ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*_4Zd0hg2Zun7zyoN.png)

Supprimez HitCube et RandomCube de la scène en cliquant avec le bouton droit de la souris, puis en cliquant sur **Delete**. Sélectionnez GeneratePlanes, ARKitControl, et cliquez sur l'inspecteur et décochez **Tag**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*9h5UqsdDgKxbRFKJ.png)

Allez à **Main Camera** sous CameraParent et, dans l'inspecteur, définissez **Near** à 0.01.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Ms5CohAnYnk_b5Ce.png)

Cliquez sur l'onglet **Scene**. Cliquez sur le chaton dans **Hierarchy** pour le sélectionner. Maintenant, nous voyons notre chaton dans la vue de la scène en trois dimensions. Allez dans l'asset « UnityARKitPlugin-> Plugins-> Helpers » et prenez le script UnityARHitTestExample.cs. Glissez le script dans l'inspecteur du chaton.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3ZKr9R10-rGC8vTe.png)

Glissez le chaton dans le champ **Hit transform** du script « UnityARHitTestExample.cs ».

Enregistrez la scène en sélectionnant « File-> Save Scenes » et appelez-la « ARKittyTest ».

Terminé ! Il est temps d'essayer la nouvelle application en réalité augmentée.

Allez dans le menu **File** et choisissez **Build Settings**. Dans la fenêtre qui s'ouvre, sous **Platform**, choisissez iOS.

Appuyez sur le bouton **Player Settings** et faites défiler jusqu'à trouver **Bundle Identifier**. Ici, écrivez un identifiant du type : « com.<VotreNom>.arkittytest ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*FslQzB0A7GIYuC9G.png)

Cliquez sur le bouton Build dans la fenêtre Build Settings et enregistrez le projet pour iOS sous « ARKittyTest ».

À la fin du processus, trouvez le projet XCode dans le Finder nommé « Unity-iPhone.xcodeproj ». Double-cliquez pour ouvrir le projet avec XCode. Dans XCode, cliquez sur Unity-iPhone et allez dans **General**. Dans le champ identité, écrivez le même Bundle Identifier inséré dans les paramètres de construction de Unity.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eA4vOjDQ05994iL9pWHceA.png)

Sous **Signing** dans le menu déroulant **Team**, sélectionnez le nom de l'équipe enregistrée.

Sélectionnez l'appareil (iPhone / iPad) avant de le connecter au Mac en tant qu'appareil cible.

Appuyez sur la touche fléchée de XCode pour « Build and Run the Current Scheme ».

Enfin, lorsque nous cadrons une surface près de nous et que nous tapons sur l'écran du téléphone, nous pouvons voir notre chaton en direct devant nous.

![Image](https://cdn-media-1.freecodecamp.org/images/0*g9WcAK0FTjQiM1F0.png)

Mission accomplie ! La vidéo suivante montre la procédure complète.

**Francesco Pallotta** est un ingénieur logiciel senior expert en conception et développement de logiciels. Il travaille dans le domaine de l'espace et de la défense et s'occupe des techniques de développement d'applications pour la réalité virtuelle et la réalité augmentée.

Vous voulez en savoir plus sur la réalité virtuelle, la réalité augmentée et la réalité mixte ? **Suivez-moi** sur [Medium](https://medium.com/@pallotta.francesco) et [Twitter](https://twitter.com/FranPallotta).

Avez-vous aimé cet article ? **Recommandez-le** en lui donnant quelques applaudissements. Merci !