---
title: Comment utiliser l'IA, la RA et les shaders WebGL pour aider les malvoyants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T21:25:37.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-use-ai-ar-and-webgl-shaders-to-assist-the-visually-impaired-3df5bdf3b3e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1Vg0Gku4F-8K6sFtQiOZFQ.png
tags:
- name: Accessibility
  slug: accessibility
- name: Augmented Reality
  slug: augmented-reality
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: Web Development
  slug: web-development
seo_title: Comment utiliser l'IA, la RA et les shaders WebGL pour aider les malvoyants
seo_desc: 'By Dan Ruta

  Today, about 4% of the world’s population is visually impaired. Tasks like simple
  navigation across a room, or walking down a street pose real dangers they have to
  face every day. Current technology based solutions are too inaccessible, o...'
---

Par Dan Ruta

Aujourd'hui, environ 4 % de la population mondiale est malvoyante. Des tâches comme la simple navigation dans une pièce ou la marche dans une rue posent de réels dangers qu'ils doivent affronter chaque jour. Les solutions technologiques actuelles sont trop inaccessibles ou difficiles à utiliser.

Dans le cadre d'un projet universitaire, nous ([moi-même](https://twitter.com/Dan_Ruta), [Louis](https://twitter.com/LouisJordan) et [Tom](https://www.instagram.com/thomas.j.fox96/)) avons conçu et mis en œuvre une nouvelle solution. Nous avons utilisé des shaders WebGL configurables pour augmenter un flux vidéo des environs d'un utilisateur en temps réel. Nous avons rendu la sortie dans un format AR/VR, avec des effets tels que la détection de contours et les ajustements de couleur. Plus tard, nous avons également ajouté une simulation de daltonisme, pour les designers. Nous avons également ajouté quelques expériences d'IA.

Nous avons fait une revue de littérature plus approfondie dans notre article de recherche original. ACM a publié une version plus courte, de deux pages, [ici](https://dl.acm.org/citation.cfm?id=3196319&dl=ACM&coll=DL&preflayout=flat). Cet article se concentre davantage sur les technologies utilisées, ainsi que sur certaines des utilisations ultérieures et des expériences telles que l'intégration de l'IA.

Une approche populaire que nous avons trouvée dans nos études de solutions existantes était l'utilisation de la détection de contours pour détecter les obstacles dans l'environnement. La plupart des solutions étaient insuffisantes en termes d'utilisabilité, ou d'accessibilité et de portabilité du matériel.

L'approche la plus intuitive à laquelle nous avons pensé pour donner un retour à l'utilisateur était l'utilisation d'un casque VR. Bien que cela signifie que le système ne serait pas d'une grande aide pour les personnes très sévèrement malvoyantes, ce serait un système beaucoup plus intuitif pour ceux qui ont une vue partielle, surtout pour ceux qui ont une vision floue.

#### Détection de contours

La détection de caractéristiques, telles que les contours, est mieux réalisée en utilisant des convolutions 2D, et est même utilisée dans l'apprentissage profond ([réseaux de neurones convolutifs](http://cs231n.github.io/convolutional-networks/)). Simplement dit, ce sont des produits scalaires d'une grille de données d'image (pixels) contre des poids dans un noyau/filtre. Dans la détection de contours, la sortie est plus élevée (plus blanche) lorsque les valeurs des pixels s'alignent avec les valeurs du filtre, représentant un contour.

![Image](https://cdn-media-1.freecodecamp.org/images/mSstLIsZsNZK2vz-UaV3bLTnpiyQpoKTzNmk)
_Ceci est fait pour chaque pixel. - [Crédit image](http://jeanvitor.com/convolution-parallel-algorithm-python/" rel="noopener" target="_blank" title=")_

Il existe quelques options disponibles pour les filtres de détection de contours. Ceux que nous avons inclus comme configurations sont Frei-chen, et les variantes 3x3 et 5x5 de [Sobel](https://en.wikipedia.org/wiki/Sobel_operator). Ils atteignent tous le même objectif, mais avec de légères différences. Par exemple, le filtre Sobel 3x3 était plus net que le filtre 5x5, mais incluait plus de bruit, provenant de textures telles que le tissu :

![Image](https://cdn-media-1.freecodecamp.org/images/St0sndi1cpWo4e9GcpCu9p6yRITP8PVv1pTR)
_Gauche : 3x3, Droite : 5x5_

#### La plateforme web

La raison principale pour laquelle nous avons choisi le web comme plateforme était sa large disponibilité et sa compatibilité avec presque tous les appareils mobiles. Il bénéficie également d'un accès plus facile, par rapport aux applications natives. Cependant, ce compromis est venu avec quelques problèmes, principalement en termes d'étapes de configuration nécessaires qu'un utilisateur devrait suivre :

1. Assurer la connectivité réseau
2. Naviguer vers la page web
3. Tourner l'appareil en mode paysage
4. Configurer l'effet
5. Activer le mode VR
6. Activer le mode plein écran (en tapant sur l'écran)
7. Insérer le téléphone dans un casque VR

Pour éviter de confondre un utilisateur non technique, nous avons créé le site web comme une PWA ([progressive web app](https://developers.google.com/web/progressive-web-apps/)), permettant à l'utilisateur de l'enregistrer sur l'écran d'accueil de son Android. Cela garantit qu'il démarre toujours sur la bonne page, le mode paysage est forcé, l'application est toujours en plein écran et ne dépend pas d'une connexion réseau.

#### Performance

Les premiers prototypes JavaScript fonctionnaient bien en dessous de notre objectif de 60fps, en raison des opérations de convolution très coûteuses. Nous avons soupçonné que le goulot d'étranglement était JavaScript lui-même. Nous avons tenté une version WebAssembly. Le prototype résultant fonctionnait encore plus lentement. Cela était probablement dû à la surcharge de passage des données de la trame vidéo au code WebAssembly, et vice versa.

Nous nous sommes donc tournés vers les shaders WebGL. Les shaders sont géniaux grâce à leur parallélisation extrême d'un peu de code (le shader) sur les pixels de la texture (flux vidéo). Pour maintenir des performances élevées, tout en gardant un niveau élevé de personnalisation, le code du shader devait être assemblé et recompilé à l'exécution, à mesure que les configurations changeaient, mais avec cela, nous avons réussi à rester dans le budget de 16,7 ms par trame nécessaire pour 60fps.

#### Retour d'information

Nous avons effectué quelques tests utilisateurs. Nous avons testé quelques tâches de base comme la navigation, et recueilli quelques retours qualitatifs. Cela incluait des ajustements à l'UI, une suggestion d'ajouter une option pour configurer les couleurs des contours et des surfaces, et une remarque que le champ de vision (FoV) était trop bas.

Les deux suggestions d'amélioration logicielle ont été appliquées. Le FoV n'était pas quelque chose qui aurait pu être corrigé par le logiciel, en raison des limitations matérielles de la caméra. Cependant, nous avons réussi à trouver une solution pour cela sous la forme de lentilles fish-eye pour téléphone-caméra, disponibles à bas prix. Les lentilles ont élargi le FoV optiquement, au lieu de numériquement.

![Image](https://cdn-media-1.freecodecamp.org/images/4jBuDXQcVSRCIW10boRa-Tl5rtdoEYHqerGM)
_Lentille fish-eye_

![Image](https://cdn-media-1.freecodecamp.org/images/SDASEK6w5TFLXm7eXYzjYRQD1Ld7uWWTzofn)
_Gauche : sans lentille, Droite : avec lentille_

Autrement, le système a dépassé les attentes initiales, mais a été insuffisant pour la lecture de texte. Cela était dû au fait qu'il y avait deux ensembles de contours pour chaque caractère. La performance en basse lumière était également utilisable, malgré l'introduction de plus de bruit.

![Image](https://cdn-media-1.freecodecamp.org/images/XUnEmgZYZn2cj5iSAEQvnXLHE0JlclqFWhXm)
_Quelques exemples de configuration d'effets de shader_

D'autres configurations que nous avons incluses étaient le rayon de l'effet, son intensité et l'inversion des couleurs.

![Image](https://cdn-media-1.freecodecamp.org/images/5jvE831AtBsKj7eFSXr0hzCwmJTkfsmdzPsA)
_Le menu des options_

#### Autres cas d'utilisation

Une idée que nous avons eue était d'ajouter des effets de shader pour simuler divers types de daltonisme, offrant un moyen facile pour les designers de détecter les problèmes d'accessibilité liés au daltonisme dans leurs produits, qu'ils soient logiciels ou autres.

En utilisant les valeurs de ratio RVB trouvées [ici](http://web.archive.org/web/20081014161121/http://www.colorjack.com/labs/colormatrix/), et en désactivant la détection de contours, nous avons pu ajouter des simulations de base de tous les principaux types de daltonisme grâce à des composants supplémentaires, activables dans les shaders.

![Image](https://cdn-media-1.freecodecamp.org/images/YflPhnWBrDuIrMI2w-WeOjQ122D-Vhz9E60J)
_Test d'Ishihara - [Crédit image](http://www.colour-blindness.com/colour-blindness-tests/ishihara-colour-test-plates/" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/BGBmXtHVuvC7WeWoFPubBOMCRZjevjccC3VP)
_**(Gauche)** Normal **(Droite)** Filtre Deutéranopie_

![Image](https://cdn-media-1.freecodecamp.org/images/b4ZsxdfjfGFJAL2WxJ7EpBIaighVoALhJqOp)
_**(Gauche)** Normal **(Droite)** Filtre Protanopie_

#### IA et travaux futurs

Bien que ce soit une expérience, encore à ses tout débuts, la détection d'objets de niveau supérieur peut être réalisée en utilisant [tensorflowjs](https://js.tensorflow.org/) et [tfjs-yolo-tiny](https://github.com/ModelDepot/tfjs-yolo-tiny), un port tensorflowjs de [tiny-yolo](https://pjreddie.com/darknet/yolo/), une version plus petite et plus rapide du modèle de détection d'objets YOLO.

![Image](https://cdn-media-1.freecodecamp.org/images/J6bwH0h0HQXONQaDapoimg6aUDcAr5jjJ2c6)
_Les catégories actuelles_

![Image](https://cdn-media-1.freecodecamp.org/images/YGBVsqdO0WC9HizjlwNVoWOfh2I-XRHuqeMK)
_Exemple d'inférence, utilisant un ordinateur portable. Nécessite un GPU décent pour fonctionner._

La prochaine étape est de faire fonctionner la segmentation d'instances dans un navigateur, avec quelque chose de similaire à [mask rcnn](https://github.com/matterport/Mask_RCNN) (bien qu'il doive peut-être être plus petit, comme tiny-yolo), et de l'ajouter à WebSight, pour mettre en évidence les éléments avec un masque de couleur, au lieu de boîtes avec des étiquettes.

![Image](https://cdn-media-1.freecodecamp.org/images/fs-OeTSPqBXdyLhBL8oU7gqIAQknnb3tDyr5)
_Objectifs — [Source](https://github.com/matterport/Mask_RCNN#4k-video-demo-by-karol-majek" rel="noopener" target="_blank" title=")_

Le dépôt GitHub est [ici](https://github.com/DanRuta/WebSight), et une démo en direct peut être trouvée à [https://websight.danruta.co.uk](https://websight.danruta.co.uk). Notez bien que jusqu'à ce qu'Apple fournisse un support pour l'API de la caméra dans les navigateurs, cela pourrait ne pas fonctionner sur les téléphones Apple.

Bien sûr, je me suis aussi bien amusé avec cela. Pouvoir éditer ce que vous pouvez voir autour de vous en temps réel ouvre un monde d'opportunités.

Par exemple, en utilisant un [shader Matrix](https://websight.danruta.co.uk/#matrix), vous pouvez vous sentir comme The One.

![Image](https://cdn-media-1.freecodecamp.org/images/PGMyqHkLVWBECPfmIxvEqpAGD7uz8e6pcPWf)
_Tout est dessiné en utilisant des chiffres verts, pas des lignes_

Ou peut-être que vous aimez simplement regarder le monde [brûler](https://websight.danruta.co.uk/#fire).

![Image](https://cdn-media-1.freecodecamp.org/images/3rZoIwLMDtceBYESlehqZWPecrbUdCjN8lLu)
_Jouant : [Billy Joel — We Didn't Start the Fire](https://www.youtube.com/watch?v=eFTLKWw542g" rel="noopener" target="_blank" title=")_

Vous pouvez tweeter plus d'idées de shaders ici : @DanRuta