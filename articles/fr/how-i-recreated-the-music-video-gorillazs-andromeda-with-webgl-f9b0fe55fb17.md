---
title: Comment j'ai recréé le clip Andromeda de Gorillaz en utilisant WebGL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-04T19:35:26.000Z'
originalURL: https://freecodecamp.org/news/how-i-recreated-the-music-video-gorillazs-andromeda-with-webgl-f9b0fe55fb17
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9jbUlPQ5H5C49rpKI7NOhQ.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: music
  slug: music
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai recréé le clip Andromeda de Gorillaz en utilisant WebGL
seo_desc: 'By Yağız Gürgül

  I was 14 years old when I first saw Gorillaz — Feel Good Inc music video. I fell
  in love with it saying “Whaatt? A cartoony music video? How awesome!”. The next
  thing I knew I was buying the Demon Days album.

  Years later… About 4 mont...'
---

Par Yağız Gürgül

J'avais 14 ans lorsque j'ai vu pour la première fois le clip de Gorillaz - Feel Good Inc. J'en suis tombé amoureux en disant « Whaatt ? Un clip de dessin animé ? Trop cool ! ». La prochaine chose que je savais, c'est que j'achetais l'album Demon Days.

Des années plus tard... Il y a environ 4 mois, YouTube m'a montré le nouveau clip de Gorillaz, Andromeda. Lorsque la lecture a commencé, j'ai immédiatement pensé que cette vidéo pouvait être rendue sur les navigateurs.

C'est alors que j'ai commencé à recréer le clip Andromeda avec WebGL. N'hésitez pas à le vérifier [Gorillaz — Andromeda en WebGL.](http://yagiz.me/andromeda/)

Lorsque j'ai commencé à recréer, la première chose que j'ai faite a été de télécharger [three.js](https://threejs.org/), qui est une solide bibliothèque JavaScript 3D. J'ai téléchargé la source et j'ai commencé avec une simple scène « Hello World ». Ensuite, j'ai commencé à planifier les objets, les textures et les animations.

J'ai divisé mon projet en quatre parties principales. Il s'agit de la scène de fond, de la scène des météorites, de la scène de Saturne et des animations.

### Analyser le clip musical

Le clip Andromeda a en fait une scène simple. Une image de galaxie de fond se déplaçant de gauche à droite. Une sphère avec une texture fluide que j'appellerai Saturne. Et des météorites dansant à l'avant. De temps en temps, lorsque la musique monte, une météorite vient du coin supérieur gauche et s'écrase sur Saturne, la faisant briller plus fort.

J'allais imiter quelque chose de similaire. J'ai donc esquissé la scène ci-dessous avec des composants comme le fond, Saturne et les météorites.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oDEEsoBguL1JcBr3gF_e5Q.png)

### Scène de fond

Cela semble être la partie la plus simple de la scène et c'est en partie vrai. Techniquement, c'est facile. D'abord, créez un plan. Animez-le de gauche à droite. Créez-en un autre et placez-le derrière le premier. Réglez leurs modes de fusion sur additif pour qu'ils semblent fusionnés. Enfin, ajoutez quelques textures.

Mais comment trouver une texture de galaxie appropriée, réelle, en 4K, belle et colorée ?

Eh bien, c'était difficile.

J'ai consulté environ mille sites pour des images libres de droits ou gratuites. Mais tout ce que j'ai pu trouver, c'est quelques beaux fonds d'écran en 4K, pas de vraies textures.

C'était mauvais. J'ai dû les acheter et les télécharger un par un. Ensuite, essayer de les convertir en textures continues. Et modifier leurs paramètres de luminosité et de contraste. Après toutes ces étapes, je les ai testées dans la scène, en essayant de voir s'ils avaient l'air bien ou non.

Cela a pris un certain temps, mais j'ai réussi à trouver l'image parfaite. Ce qui en valait totalement la peine et j'étais vraiment heureux de voir les résultats :

![Image](https://cdn-media-1.freecodecamp.org/images/1*p5-J7LfHecsnzdoYkXJyKA.gif)

J'avais besoin d'ajouter quelques effets de post-traitement tels que changer la teinte à mon projet. J'ai utilisé EffectComposer (Vous pouvez trouver un tutoriel détaillé [ici.](http://blog.cjgammon.com/threejs-post-processing)), qui ne fait pas partie de three.js mais qui est fourni avec les exemples. En utilisant EffectComposer, j'ai facilement réussi à ajouter des effets de teinte à ma scène de fond.

### Scène des météorites

Les météorites étaient la partie la plus simple du projet. En même temps, elles étaient les ennemies de la performance. Il y en a 500 qui bougent et tournent dans la scène ! J'avais besoin de trouver un modèle de météorite de la manière la plus simple pour avoir des animations fluides.

C'est incroyable ce que vous pouvez faire avec les géométries de stock dans three.js. Avec [OctahedronGeometry](https://threejs.org/docs/index.html#api/geometries/OctahedronGeometry), j'ai déformé chaque sommet. Cela ressemble essentiellement à un rocher :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3LvuOXIAblsJpq8iAGtgvw.gif)

Comme je l'ai dit avant, ce projet compte 500 météorites. Chacune a une vitesse de mouvement différente, une vitesse de rotation et une taille aléatoire. Elles se déplacent de droite à gauche. Lorsqu'elles sortent de la vue, elles se téléportent du côté droit de la vue.

![Image](https://cdn-media-1.freecodecamp.org/images/1*M4NXejdznwpNd5KKC_AN5g.gif)

Les météorites derrière Saturne sont en fait une seule image statique. Au début, j'ai essayé de créer cette image statique à partir de zéro. J'ai dessiné quelques cercles aléatoires avec un effet de lueur, mais ensuite je n'ai pas aimé leur apparence dans la scène. Ensuite, j'ai trouvé une texture d'étoiles. Je l'ai teintée en jaune et j'ai réglé son mode de fusion sur additif.

### Scène de Saturne

Sans aucun doute, c'était la partie la plus difficile de la scène. Pour comprendre pourquoi, vous devez inspecter ses caractéristiques dans le clip musical :

* La texture s'anime de manière à ce que la partie supérieure se déplace plus rapidement que la partie inférieure.
* Saturne ne tourne pas, mais la texture donne l'impression qu'elle oscille.
* Saturne a une lueur intérieure. Les bords et les parties centrales sont plus brillants.
* Saturne a également une lueur extérieure. En fait, il y a deux lueurs extérieures. L'une d'elles est plus brillante et proche des bords, l'autre est plus grande et plus sombre.

#### Texture

Trouver une belle texture appropriée... Vous savez déjà que c'est difficile. Mais l'un de mes collègues m'a donné l'idée la plus simple, de rechercher **"saturn texture"** sur Google Images. J'ai été choqué par ce que j'ai trouvé.

La première image qui est apparue était exactement la même que celle utilisée dans le clip Andromeda. L'artiste/designer a-t-il recherché "saturn texture" sur Google Images et choisi la première dans la production ? Est-ce courant ?

En tout cas, puisque j'ai trouvé ma texture de Saturne, la partie suivante était de l'animer. C'était le plus grand défi. Après avoir fait quelques recherches, j'ai compris que je devais utiliser quelque chose appelé **fragment shader**. Mais qu'est-ce que c'était que ça ? Autant que je comprenne, c'est un code qui vit dans .js/.html mais qui s'exécute dans le GPU.

Lorsque qu'un modèle 3D est rendu, chaque pixel de ce modèle doit savoir quelle couleur de texture il doit utiliser. Une façon de faire cela est d'utiliser [UV mapping](https://en.wikipedia.org/wiki/UV_mapping). J'anime les coordonnées de la carte UV de manière exponentielle. Ainsi, la partie supérieure est devenue plus rapide que la partie inférieure. C'était un peu par essais et erreurs, mais je pense que j'ai réussi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pWqB6m1TaqtWJdAIgvpuew.gif)

Dans la vidéo, Saturne oscille également. Pour obtenir ce mouvement, j'ai utilisé une fonction sin. L'une des entrées de cette fonction sin est le temps de l'image, qui augmente avec le temps. Ainsi, la sphère semble osciller.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aodD5NHKnDyYE1JpWGC1uA.gif)

#### Lueurs

Il y a trois types de lueurs dans le projet, la lueur intérieure, la grande lueur extérieure et la petite lueur extérieure.

Pour la lueur intérieure, j'ai créé une texture de dégradé simple en noir et blanc. Ensuite, j'ai ajouté ses couleurs de pixels à la couleur de la texture originale de Saturne dans le fragment shader :

![Image](https://cdn-media-1.freecodecamp.org/images/1*nKxnVsPHR1feNKSzo3IjMw.gif)

Au début, j'ai pensé que je pourrais créer les lueurs extérieures en utilisant le fragment shader. Mais j'ai décidé que ce serait excessif, car la caméra et Saturne ne tournent pas.

J'ai donc créé des textures de dégradé circulaire en noir et blanc. Je les ai placées derrière Saturne et j'ai réglé leurs modes de fusion sur additif. Cela m'a fait économiser une énorme quantité de temps de développement.

Vous pouvez voir la plus grande lueur en action. N'oubliez pas qu'il s'agit en fait d'un plan derrière Saturne :

![Image](https://cdn-media-1.freecodecamp.org/images/1*jGZmX4KwtFk-QGgqhJvpNg.gif)

Voici la lueur plus petite mais plus brillante créée avec la même technique :

![Image](https://cdn-media-1.freecodecamp.org/images/1*q1UWZqzb0BN0KzzGc7OAag.gif)

Voici le résultat final de Saturne avec toutes les lueurs activées :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tXAtxUHYYM78lNmAMhhmEw.gif)

### Animation

La dernière partie du projet était de créer des animations synchronisées avec la chanson.

Dans la vidéo, une météorite vient du coin supérieur gauche et s'écrase sur Saturne à trois reprises. Lors du premier crash, la texture réelle de Saturne, les effets de lueur et le fond deviennent visibles. Lors des deuxième et troisième crashes, la texture de Saturne et les lueurs deviennent plus brillantes.

J'ai choisi [tween.js](https://github.com/tweenjs/tween.js), une bibliothèque d'animation JavaScript, qui est super facile à utiliser. Toute la scène est dynamiquement contrôlée par des paramètres comme l'opacité du fond, la vitesse d'écoulement de la texture, et la luminosité des lueurs intérieures et extérieures. Ensuite, j'ai suivi le temps actuel du lecteur YouTube et j'ai commencé à animer ces paramètres aux bons moments.

Vous pouvez voir la deuxième explosion en action ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FCPA5ZMBD1ZgrqkLWrdU3Q.gif)

### Les rassembler tous ensemble

![Image](https://cdn-media-1.freecodecamp.org/images/1*007tX6vx8VO0yrChR-S_iQ.gif)

En rassemblant tous mes composants, j'ai constamment comparé mon projet avec le clip musical réel. J'ai écouté la même chanson et regardé la même vidéo encore et encore pour m'assurer que mes animations correspondaient au clip réel. Plusieurs fois, j'ai complètement changé les valeurs des effets pour les rendre attrayants pour l'œil des spectateurs.

Après de nombreuses modifications et allers-retours entre les scènes, j'étais très satisfait du résultat final, mon produit final. Même si je ne m'attendais pas à voir quelque chose d'aussi beau lorsque j'ai commencé.

Tester le projet sur des appareils mobiles était également satisfaisant. Voir les animations fonctionner aussi bien que sur ordinateur était génial. Je n'ai pas eu à faire de trucs de performance pour le mobile.

Je dois dire que l'expérimentation en 3D a été une expérience incroyable. Si vous êtes bon en JavaScript et en mathématiques, mais que vous n'avez pas beaucoup d'expérience en 3D, je vous suggère fortement de jouer avec. C'est gratifiant de voir ce que vous pouvez faire avec quelques plans et sphères.

* Développeur : [Yagiz Gurgul](http://yagiz.me)
* Lien du projet : [http://yagiz.me/andromeda/](http://yagiz.me/andromeda/)
* Source du projet : [https://github.com/yagiz/andromeda](https://github.com/yagiz/andromeda)