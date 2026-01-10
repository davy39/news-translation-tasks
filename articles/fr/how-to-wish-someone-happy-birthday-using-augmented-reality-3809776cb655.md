---
title: Comment souhaiter un joyeux anniversaire à quelqu'un en utilisant la réalité
  augmentée
subtitle: ''
author: Pratik Parmar
co_authors: []
series: null
date: '2018-06-29T17:43:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-wish-someone-happy-birthday-using-augmented-reality-3809776cb655
coverImage: https://cdn-media-1.freecodecamp.org/images/1*R6c3P43LzQgB6d3khSNnRQ.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: Augmented Reality
  slug: augmented-reality
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Virtual Reality
  slug: virtual-reality
seo_title: Comment souhaiter un joyeux anniversaire à quelqu'un en utilisant la réalité
  augmentée
seo_desc: I have a friend who’s birthday was coming up, so I wanted to do something
  special for her. As she is a TechGeek just like me, so I couldn’t just get her a
  simple birthday present like a teddy bear or chocolates. So, I started looking for
  unique ways ...
---

J'ai une amie dont l'anniversaire approchait, alors je voulais faire quelque chose de spécial pour elle. Comme elle est une TechGeek tout comme moi, je ne pouvais pas simplement lui offrir un cadeau d'anniversaire simple comme un ours en peluche ou des chocolats. Alors, j'ai commencé à chercher des moyens uniques de lui souhaiter un joyeux anniversaire sur le Web.

J'ai fini par regarder une [vidéo](https://youtu.be/O_EUnGMJtLA) où un homme faisait sa demande en mariage à une femme en utilisant la VR. Alors, j'ai décidé — c'était ça ! C'est comme ça que j'allais faire. Pas la partie demande en mariage, bien sûr.

Alors que je contribuais à Mozilla, j'avais créé quelques petits projets VR en utilisant [**A-Frame**](https://aframe.io/) **—** le framework web de Mozilla pour construire des expériences de réalité virtuelle. Et croyez-moi, même si vous ne connaissez pas beaucoup la VR ou la RA, vous pouvez facilement créer une scène VR en utilisant A-Frame. Le seul prérequis est HTML, que vous pouvez apprendre facilement [ici](https://www.w3schools.com/Html/). Pour une meilleure compréhension, cependant, je vous recommande de parcourir [A-Frame School](https://aframe.io/aframe-school/#/), qui est une grande collection de tutoriels destinés aux débutants.

J'avais donc décidé que j'allais utiliser A-Frame, mais je voulais plus qu'une simple scène VR affichant « Joyeux Anniversaire ». À la fin, j'ai choisi de créer une scène AR. J'ai trouvé un excellent projet appelé [AR.js](https://github.com/jeromeetienne/AR.js/blob/master/README.md)**.** Si vous voulez commencer avec AR.js, voici un [excellent article pour débutants](https://medium.com/arjs/augmented-reality-in-10-lines-of-html-4e193ea9fdbf)**.**

### Construire une application Web AR de base

![Image](https://cdn-media-1.freecodecamp.org/images/1*R6c3P43LzQgB6d3khSNnRQ.jpeg)
_Scène AR, créée en utilisant AR.js_

Pour regarder la scène AR, vous devez :

* Ouvrir cette [image de marqueur HIRO](https://jeromeetienne.github.io/AR.js/data/images/HIRO.jpg) dans votre navigateur de bureau.
* Ouvrir cette application Web AR dans votre navigateur de téléphone, et la pointer vers votre écran.

Lorsque vous scannez un marqueur (ici, un marqueur HIRO), il affichera une scène AR sur votre téléphone, comme l'image ci-dessus. J'ai utilisé un marqueur HIRO simple, mais vous pouvez [créer votre propre marqueur également](https://medium.com/arjs/how-to-create-your-own-marker-44becbec1105).

Donc, après avoir ajouté toutes ces bibliothèques, mon code ressemblait à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*VpWtY3jmzmc5ftAM23SRPA.png)
_Application Web AR de base [ [Démo](https://hackyroot.github.io/A-Frame-Examples/Happy_Birthday/Basic.html" rel="noopener" target="_blank" title=") ]_

Veuillez noter que lors de l'accès à une application Web AR, si vous obtenez une invite demandant la permission d'accéder à la webcam, veuillez l'autoriser. Sinon, l'application ne fonctionnera pas.

### Ajouter des modèles 3D et des polices

Donc, maintenant nous avons une application Web AR simple fonctionnant sur notre appareil. Mais qu'est-ce qu'un anniversaire sans **gâteau** ?! Heureusement, A-Frame supporte trois types de modèles 3D : [glTF](https://aframe.io/docs/0.8.0/components/gltf-model.html), [OBJ](https://aframe.io/docs/0.8.0/components/obj-model.html), et [COLLADA](https://aframe.io/docs/0.8.0/components/collada-model.html). En savoir plus sur les modèles 3D dans A-Frame [ici](https://aframe.io/docs/0.8.0/introduction/models.html).

J'ai téléchargé quelques fichiers de modèles 3D de gâteau depuis [Google Poly](https://poly.google.com/)**.** Vous pouvez importer n'importe quel fichier d'actif dans A-Frame en utilisant la balise _<a-assets>_. Vous pouvez également importer des polices séparées, au cas où vous souhaitez utiliser une police différente.

J'étais assez convaincu qu'A-Frame ne pouvait pas être plus génial. Mais, attendez...

### Ajouter de l'audio

Les anniversaires ne sont pas complets sans la chanson d'anniversaire, n'est-ce pas ? Et A-Frame supporte également les fichiers audio. Vous pouvez utiliser la balise _<audio>_ pour importer vos fichiers, sous la balise <a-assets>.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z7Bj8EeI8PA_MfGnUzdv5w.png)
_Importer des fichiers d'actifs_

### Ajouter des particules

Quelle est la chose qui vous vient à l'esprit lorsque vous entendez parler d'un anniversaire — après le gâteau, bien sûr ? Une **fête**, n'est-ce pas ? Alors, ajoutons des confettis à notre scène AR, en utilisant [le composant Particle System d'A-Frame](https://github.com/IdeaSpaceVR/aframe-particle-system-component).

![Image](https://cdn-media-1.freecodecamp.org/images/1*WRq3LqBLvxy8aQIuH3J2zA.png)
_Ajouter des bibliothèques pour les confettis et le texte 3D_

### Mettons tout cela ensemble

#### Modèles 3D

Ce code affichera le modèle 3D du gâteau. Mais comme vous pouvez le voir, j'ai ajouté quelques valeurs dans les champs _rotation_ et _scale_. Alors, discutons de cela. Selon la [page GitHub](https://github.com/aframevr/aframe/blob/master/docs/components/rotation.md) d'A-Frame :

* **Rotation** : le composant de rotation définit l'orientation d'une entité en degrés. Il prend le tangage (`x`), le lacet (`y`), et le roulis (`z`) comme trois nombres séparés par des espaces indiquant les degrés de rotation.
* **Scale** : le composant d'échelle définit une transformation de rétrécissement, d'étirement ou de cisaillement d'une entité. Il prend trois facteurs d'échelle pour les axes X, Y et Z.
* **MTL** : signifie Material Library File (.**mtl**) Les fichiers de bibliothèque de matériaux contiennent une ou plusieurs définitions de matériaux, chacune incluant la couleur, la texture et la carte de réflexion des matériaux individuels. Ceux-ci sont appliqués aux surfaces et aux sommets des objets. Les fichiers de matériaux sont stockés au format ASCII et ont l'extension .**mtl**.
* **OBJ** : un format de fichier qui a été créé comme un moyen simple d'importer et d'exporter la géométrie depuis différentes applications 3D. Il s'agit d'un type de fichier courant utilisé par de nombreuses solutions de conception 3D.
* **Suggestion** : Si vous ne voyez pas votre modèle, essayez de le réduire. Les modèles OBJ ont généralement des échelles extrêmement grandes par rapport à l'échelle d'A-Frame.

Si vous vous demandez comment je connaissais les valeurs exactes pour la rotation, eh bien je ne les connaissais pas. J'ai utilisé un outil incroyable créé par l'équipe Mozilla appelé [A-Frame Inspector](https://github.com/aframevr/aframe-inspector), construit à cette fin seulement.

Pour en savoir plus sur _<a-obj-model>_, visitez [ce](https://aframe.io/docs/0.8.0/primitives/a-obj-model.html) lien.

![Image](https://cdn-media-1.freecodecamp.org/images/1*588pLp64QgtSVHgXeq-4rg.png)
_Afficher le modèle 3D du gâteau_

#### Particules

Eh bien, ce code peut sembler écrasant à première vue, mais croyez-moi, ce n'est pas le cas. Nous avons discuté de la Rotation plus tôt, mais parlons des autres champs également :

* **Position** : place les entités à certains endroits dans l'espace 3D. La Position prend une valeur de coordonnée sous forme de trois nombres séparés par des espaces.
* **Preset** : configuration prédéfinie. Les valeurs possibles sont : `default`, `dust`, `snow`, `rain`. Ici, nous avons choisi default afin d'afficher des étoiles.
* **Color** : décrit la couleur d'une particule. Cette propriété est une propriété « valeur-sur-la-durée-de-vie », ce qui signifie qu'un tableau de valeurs peut être donné pour décrire des changements de valeur spécifiques sur la durée de vie d'une particule.
* **Acceleration Value** : décrit l'accélération de base de cet émetteur.
* **Particle Count** : le nombre total de particules que cet émetteur contiendra.
* **Direction** : la direction de l'émetteur. Si la valeur est `1`, l'émetteur démarrera au début du cycle de vie de la particule. Si la valeur est `-1`, l'émetteur démarrera à la fin du cycle de vie de la particule et travaillera à rebours.
* **Rotation Axis** : décrit l'axe de rotation de cet émetteur. Les valeurs possibles sont `x`, `y` et `z`.

Pour en savoir plus sur le système de composants de particules d'A-Frame, visitez ce [lien](https://www.npmjs.com/package/aframe-particle-system-component).

![Image](https://cdn-media-1.freecodecamp.org/images/1*lryKm0DHjxWdXL2on4uiig.png)

#### Texte et Audio

Eh bien, vous pouvez utiliser _<a-text>_ également, mais j'ai décidé d'utiliser le [composant Text Geometry](https://www.npmjs.com/package/aframe-text-geometry-component) pour plus d'options. Il est utilisé pour générer du texte sous forme de géométrie unique.

* **Material** : Le composant de géométrie de texte définit uniquement la géométrie. Nous pouvons appliquer n'importe quel matériau three.js à la géométrie.

```html
<a-entity text="value: HELLO" material="color: red; src: #texture"></a-entity>
```

Pour plus de détails, visitez la [documentation](https://threejs.org/docs/) de three.js.

* **Text Geometry** : valeur de la chaîne et de la police. (vous devriez modifier le texte dans cette partie, sinon vous finirez par souhaiter un joyeux anniversaire à mon amie ??)
* **Sound** : définit l'entité comme une source de son ou d'audio.
* **Autoplay** : décrit si le son doit être joué automatiquement une fois défini.
* **Loop** : décrit si le son doit être joué en boucle une fois que le son a fini de jouer.
* **On** : un événement pour l'entité à écouter avant de jouer le son.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YVFBn6QETdSUvbtRwLS5zw.png)

### Ressources :

* [Code source](https://github.com/HackyRoot/A-Frame-Examples/tree/master/Happy_Birthday)
* [Démo](https://hackyroot.github.io/A-Frame-Examples/Happy_Birthday/demo.html)

Oui, vous l'avez fait ? ? ?. Vous avez créé votre **première** application AR. Si vous avez tout fait correctement, vous devriez maintenant voir quelque chose comme l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zZc5N-LaMQm9iXPFOG6I5g.jpeg)
_Finalement, Joyeux Anniversaire Krupa !_

Si vous aimez mon travail, veuillez me suivre sur Medium @[Pratik Parmar](https://www.freecodecamp.org/news/how-to-wish-someone-happy-birthday-using-augmented-reality-3809776cb655/undefined) ou m'ajouter sur [LinkedIn](https://www.linkedin.com/in/pratik-parmar-8853597a/). N'hésitez pas à me contacter sur Twitter : [Pratik Parmar](https://www.freecodecamp.org/news/how-to-wish-someone-happy-birthday-using-augmented-reality-3809776cb655/undefined) ou commentez ci-dessous, au cas où vous auriez besoin d'aide.

En plus des contributions open-source chez Mozilla, je suis un Microsoft Student Partner et membre de la communauté chez GDG Baroda. Je tiens à remercier [Mozilla](https://www.freecodecamp.org/news/how-to-wish-someone-happy-birthday-using-augmented-reality-3809776cb655/undefined) et la communauté [MozillaIN](https://twitter.com/MozillaIN) pour m'avoir donné une chance et les ressources pour apprendre sur la VR/AR et l'Open Source.

C'est moi, **Pratik Parmar**, qui signe jusqu'à la prochaine aventure technologique. Fin de transmission...

[ Modification : Merci à [Vikranth Kanumuru](https://www.freecodecamp.org/news/how-to-wish-someone-happy-birthday-using-augmented-reality-3809776cb655/undefined) d'avoir attiré mon attention sur le fait que l'URL du code source était cassée. Elle a été mise à jour maintenant, veuillez essayer maintenant. Continuez à coder, continuez à assurer ]