---
title: Ne ruinez pas votre <img>
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-09T12:40:54.000Z'
originalURL: https://freecodecamp.org/news/you-need-to-stop-making-these-6-mistakes-with-your-img-s-e242c02d14be
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fXZTuZFmYlUNbu1OLfHm3w.jpeg
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Ne ruinez pas votre <img>
seo_desc: 'By Anthony Ng

  As developers and designers, it’s our duty to ensure the best user experience possible.
  And you know what one huge part of that experience is? Images.

  But many of us are too busy to give images much thought beyond adding a src property
  ...'
---

Par Anthony Ng

En tant que développeurs et designers, il est de notre devoir d'assurer la meilleure expérience utilisateur possible. Et vous savez quelle est une énorme partie de cette expérience ? Les images.

Mais beaucoup d'entre nous sont trop occupés pour accorder beaucoup d'attention aux images au-delà de l'ajout d'une propriété **src** et de quelques dimensions en pixels.

Ce guide vous montrera quelques problèmes courants liés à l'utilisation des images, et comment les résoudre.

J'ai également créé un [site web](https://newyork-anthonyng.github.io/Responsible_Responsive_Images/) avec des exemples en direct pour illustrer tous ces problèmes. Faites quelques rafraîchissements forcés, redimensionnez votre navigateur, et vous verrez rapidement ce que je veux dire. ?

Oh, et vous pouvez trouver tout le code source ici sur [Github](https://github.com/newyork-anthonyng/tutorials/tree/master/Responsive_Responsible_Images).

Commençons.

### Réduisez les images à la bonne taille

Lorsque vous visitez un site web, une page HTML est envoyée à votre navigateur. Le navigateur doit ensuite télécharger tous les actifs que la page HTML inclut. Votre navigateur doit charger tous les fichiers JavaScript, les feuilles de style — et bien sûr, les images — que la page utilise. Chacun de ces actifs prend du temps à charger. Plus le fichier est grand, plus il faudra de temps.

Nous minifions nos fichiers JavaScript pour supprimer le superflu et obtenir une taille de fichier plus petite. Nous devrions faire de même avec nos images.

Une façon de se débarrasser du "superflu" des images est de s'assurer que les dimensions sont raisonnables. Il n'y a aucune raison de laisser les images plus grandes qu'elles n'en ont besoin.

Si la largeur maximale d'une image sur votre site web va être de 960px, alors il n'y a pas besoin d'utiliser un fichier image qui fait 1800px de large. Le temps de chargement de votre site web en souffrira. Surtout sur des connexions plus lentes. Et vous forcez votre utilisateur à télécharger plus d'octets que nécessaire.

Lorsque vous connaissez les dimensions de vos images, utilisez un programme qui peut redimensionner les photos à la taille dont vous avez besoin. J'utilise généralement [Sketch](https://www.sketchapp.com/) ou [Affinity Designer](https://affinity.serif.com/en-us/).

Dans notre exemple [ici](https://newyork-anthonyng.github.io/Responsible_Responsive_Images/image_dimension.html), les images ont toutes deux une largeur de 960px. Cependant, la photo originale a une largeur de 5183px. Il n'y a aucun intérêt à avoir une image avec des dimensions aussi grandes si nous n'allons pas l'utiliser.

Après avoir réduit les dimensions de la photo pour qu'elle ait une largeur de 960px, nous voyons une réduction de 90 % de la taille du fichier, avec une amélioration de 6 secondes du temps de chargement sur une connexion wifi.

![Image](https://cdn-media-1.freecodecamp.org/images/M-ZjRnIZizP4GvCJCfNPc1fLEhb8kLhOU6wM)
_Image originale vs. Image redimensionnée_

Et, bien sûr, les temps de chargement varient en fonction de la vitesse de votre réseau.

Si nous utilisons l'outil Chrome Developer pour limiter la connexion à une connexion 4G régulière, nous voyons une amélioration impressionnante de 16 secondes du temps de chargement.

![Image](https://cdn-media-1.freecodecamp.org/images/BUX-ZX0BHIz92mI78q4PfQrJvHD3wMdrzYAU)
_Image originale vs. Image redimensionnée sur 4G_

### Utilisez la compression

Réduire les dimensions de notre image est un excellent début pour réduire la taille globale du fichier, mais nous pouvons faire plus. Nous pouvons compresser notre image pour réduire davantage la taille du fichier image, avec peu (voire aucune) réduction de la qualité de l'image.

La compression supprime les éléments inutiles de notre image, tels que les métadonnées, les miniatures intégrées, les commentaires et les profils de couleur inutiles.

J'utilise une application appelée ImageOptim pour compresser mes images. Pour l'utiliser, il vous suffit de glisser vos images dans l'application et... c'est tout. La nouvelle image compressée remplacera l'ancienne. Si vous souhaitez automatiser la compression des images, vous pouvez utiliser un exécuteur de tâches, tel que Grunt, pour minifier vos images lors de la construction de votre projet.

Dans notre exemple [ici](https://newyork-anthonyng.github.io/Responsible_Responsive_Images/image_compression.html), nous voyons une réduction de 13 % de la taille du fichier après compression, avec une amélioration de 100 millisecondes (12 %) du temps de chargement sur une connexion wifi.

100 millisecondes peuvent sembler peu, mais ces économies font une différence lorsque vous avez plusieurs images sur la même page qui tentent de passer à travers un réseau 3G faible sur un iPhone.

![Image](https://cdn-media-1.freecodecamp.org/images/oq50cJJ2RND9ObD59o4tA7Wlu8MNnEUT1183)
_Image non compressée vs. Image compressée_

### Utilisez les media queries pour rendre les images responsives

Maintenant, nous avons un fichier image allégé qui se chargera rapidement sur votre page HTML. L'expérience utilisateur est définitivement meilleure, mais notre travail n'est pas encore terminé. Nous devons nous assurer que l'image a fière allure sur tous les types d'écrans. Elle doit être responsive.

Il existe des sites web où l'image ne s'adapte pas complètement à l'écran. Vous devez faire défiler de gauche à droite — ou même zoomer — afin de voir la photo entière. Ce n'est pas la meilleure expérience utilisateur.

Utilisons les media queries pour styliser nos images lorsque l'écran est d'une certaine taille. Sur les écrans plus petits, nous utiliserons "max-width: 100%" pour styliser nos images.

Dans notre exemple [ici](https://newyork-anthonyng.github.io/Responsible_Responsive_Images/responsive.html), chaque fois que nous redimensionnons la page, nous pouvons voir que notre image responsive s'adaptera toujours entièrement à l'écran. L'utilisateur n'a pas besoin de faire défiler ou de zoomer pour voir l'image complète.

### Demandez à un directeur artistique

Notre expérience utilisateur s'améliore définitivement. Notre image est légère et responsive. Cependant, cette image redimensionnée n'est peut-être pas exactement ce que nous voulons sur notre site web.

Par exemple, notre site web pourrait parler de l'Empire State Building. Lorsque l'image fait 960px, l'Empire State Building se dresse majestueusement au centre de la ligne d'horizon, reconnaissable au premier coup d'œil. Mais une fois que nous redimensionnons notre navigateur pour qu'il fasse 360px de large, il perd un peu de son panache. Dans ce cas, une image redimensionnée n'est pas ce que nous voulons.

En rendant notre image responsive, nous évitons le problème des utilisateurs qui doivent faire défiler et zoomer pour voir notre image. Mais nous remplaçons ce problème par un nouveau. Les utilisateurs doivent maintenant zoomer sur l'image, pour voir un Empire State Building pixelisé. Ce n'est pas la meilleure expérience utilisateur.

Dans des situations comme celle-ci, notre image doit être changée de manière plus drastique. Vous pourriez vouloir recadrer l'image ou changer complètement l'image. Faire cela est appelé "art direction".

Pour utiliser différentes images, nous pouvons utiliser les balises HTML <picture> et <source>. Cela indique au navigateur quelle image demander et utiliser en fonction d'une media query.

Dans notre [exemple](https://newyork-anthonyng.github.io/Responsible_Responsive_Images/art_direction.html), nous utiliserons différentes images en fonction de la taille de notre écran. Maintenant, lorsque vous redimensionnez le site web, vous devriez pouvoir voir l'Empire State Building dans toute sa gloire.

### Utilisez les service workers pour profiter de la mise en cache

Le Responsive Web Design est un concept relativement nouveau. Nous devrions concevoir nos sites web pour qu'ils aient fière allure, peu importe l'écran sur lequel ils sont affichés. Maintenant, il y a une nouvelle tendance pour que les sites web ressemblent davantage à des applications natives. Parmi d'autres choses, cela signifie que nos sites web doivent fonctionner même sans connexion internet.

Qu'est-ce que cela signifie pour nos images ? Pour les images qui sont statiques et ne seront pas souvent mises à jour (comme les logos), nous devrions les mettre en cache. Lorsque nous mettons en cache des actifs, ceux-ci sont sauvegardés dans le navigateur client.

Lorsque nous mettons en cache des actifs, ceux-ci sont sauvegardés dans le navigateur client. L'avantage de cela est que lorsque l'utilisateur visite nos sites web à l'avenir, il cherchera d'abord tout actif dans notre cache avant de faire une demande au serveur. Notre image se chargera encore plus rapidement, car la récupération depuis le cache est généralement plus rapide que de faire une requête HTTP. Un autre avantage est que nous pouvons même accéder à notre image sans connexion internet !

Utilisons les service workers pour mettre en cache nos actifs. Les service workers sont une nouvelle technologie puissante qui agit comme un middleware entre votre navigateur et internet. Cela nous permet d'avoir des pages web entièrement fonctionnelles hors ligne !

Dans notre [exemple](https://newyork-anthonyng.github.io/Responsible_Responsive_Images/offline.html), si vous éteignez votre internet et rafraîchissez la page, vous verrez que notre site web fonctionne toujours comme avant.

![Image](https://cdn-media-1.freecodecamp.org/images/JewcFUneXtwOMRa6i-9zUdAef4-w1MJYhtW8)
_Remarquez que notre jpeg est récupéré depuis le ServiceWorker_

### Une image accessible est une image conviviale

Lorsque vous utilisez la balise HTML <img>, gardez à l'esprit la propriété alt.

De nombreuses personnes atteintes de déficiences visuelles utilisent des outils appelés lecteurs d'écran qui lisent tout le contenu d'une page web à voix haute. Ils liront la propriété alt de toute image qu'ils rencontrent, et ignoreront toute image qui n'a pas de propriété alt. Ainsi, les propriétés alt sont cruciales pour que ces personnes comprennent les images.

Au fait, chaque image devrait avoir une propriété alt, mais si l'image est purement décorative (ou clairement expliquée ci-dessus), vous pouvez la laisser vide.

De cette façon, nos images peuvent être comprises par tout le monde — même par les personnes qui ne peuvent pas les voir.

C'est tout ! Avez-vous des conseils pour mieux utiliser les images ? Laissez un commentaire ci-dessous !

Vous voulez en savoir plus sur les Service Workers ? Consultez cette [introduction](https://developers.google.com/web/fundamentals/primers/service-worker/) sur la page des développeurs de Google.

Vous voulez en savoir plus sur la création de meilleures expériences utilisateur grâce à des sites web plus rapides ? Consultez ce [livre](http://designingforperformance.com/).