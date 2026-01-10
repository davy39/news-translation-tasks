---
title: Comment créer des objets 3D réalistes dans Figma
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-07T14:00:31.000Z'
originalURL: https://freecodecamp.org/news/creating-realistic-3d-objects-in-figma-carton-box-example-f674c21c3452
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LMmouy5qiEmwew9mmFrIbg.png
tags:
- name: Design
  slug: design
- name: figma
  slug: figma
- name: Nigeria
  slug: nigeria
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment créer des objets 3D réalistes dans Figma
seo_desc: 'By Gbolahan Taoheed Fawale

  Prior to using Figma, I used Adobe Illustrator for most of my designs (like logos,
  mockups, illustrations, and so on). But since I joined the “Figma gang” , I’ve dropped
  illustrator so I can focus on Figma and learn as much...'
---

Par Gbolahan Taoheed Fawale

Avant d'utiliser Figma, j'utilisais Adobe Illustrator pour la plupart de mes designs (comme les logos, les maquettes, les illustrations, etc.). Mais depuis que j'ai rejoint le "Figma gang", j'ai abandonné Illustrator pour me concentrer sur Figma et apprendre autant que possible à son sujet.

Je voulais découvrir plus de trucs avec le logiciel, pour arriver à des résultats finaux qui ne sont pas "typiques de Figma". Cela vient du fait que les designs que j'espère créer ne sont pas nécessairement ce pour quoi le logiciel a été développé.

Figma est plus un outil de design UI/UX qu'un outil de design visuel ou d'illustration comme Adobe Illustrator.

Cet article parle de mon exploration de Figma au-delà de l'UI/UX pour découvrir de nouvelles façons de l'utiliser et de nouvelles choses que je pourrais découvrir en l'utilisant comme mon outil de design complet. Au final, peu importait le type de design que je pourrais vouloir faire ou explorer.

Je vais donc vous guider à travers le processus de création de l'image ci-dessus.

### **Étape 1 : Créer une boîte similaire**

La première chose que j'ai créée est une boîte qui ressemble à celle en marron sur l'image ci-dessus. Cela a été créé en utilisant des formes (uniquement des rectangles). Je sais que certaines personnes sont fans de l'outil plume. Mais dans l'exemple ci-dessus, l'outil plume ne nous offre pas la flexibilité de créer des ombres, d'ajouter des dégradés, ou de faire toute sorte de manipulation d'objet sur des formes individuelles ou des parties de la boîte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z00lKKJqwukXunl84Opinw.png)
_étape une ?_

Dans l'illustration ci-dessus, j'ai utilisé l'outil d'édition d'objet pour redimensionner et manipuler les rectangles afin de faire une forme similaire à un rhombe. La chose suivante que j'ai faite a été de recréer les mêmes rectangles et de les retourner pour former les troisième et quatrième côtés de la boîte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jmv3ZmYhU31lFOq8dIbY6g.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*flcE2QrMjONEyC85lZqd1w.png)
_outil d'édition d'objet_

### **Étape 2 : Ajout des ombres**

J'ai ajouté de la couleur pour différencier chaque côté de la boîte, et aussi pour donner une idée de comment les ombres, les contrastes et les dégradés seraient appliqués. Cela a posé une base pour que les côtés de la boîte puissent être travaillés indépendamment. J'ai également créé les pièces du couvercle de la boîte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Am7RNhHO6VGF-hOupNcVqg.png)
_création des couvercles_

### **Étape 3 : Rendre cela plus réaliste**

J'ai ajouté un dégradé aux couvercles visibles de la boîte (f1 & f2) pour leur donner un aspect plus réaliste et plat. Remarquez la façon dont le dégradé est superposé sur f2 ? J'ai fait de même pour f1, puis j'ai ajusté le degré du dégradé pour correspondre à la direction de la lumière sur la boîte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Rf23OEHaAvNHFa6c95BTRg.png)

Après avoir ajouté le dégradé, j'ai ajouté les ombres. Lorsque des rayons de lumière tombent sur un objet, une ombre se forme automatiquement en fonction de la direction de la lumière et de l'objet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G8uX_CbCCNk1oKGQPmBN_w.png)
_création de la couche d'ombre en copiant la couche existante et en l'éditant_

_Note : La couche surlignée ci-dessus est en fait sous celle visible. C'est ce qui sera redimensionné pour former l'ombre._

### **Étape 4 : Ajuster le couvercle**

Pour ajouter une ombre, j'ai simplement copié f1 et je l'ai collé sur la même couche. J'ai ensuite choisi la copie originale/initiale de f1 (qui est sous le nouvellement copié 'f1'), j'ai cliqué sur l'outil d'édition d'objet, et je l'ai redimensionné pour qu'il dépasse un peu sous le 'f1 copie'. Cela a été fait juste pour créer parfaitement l'effet d'ombre. La fonction d'ombre par défaut de Figma ne m'aurait pas donné la flexibilité de créer la boîte marron de l'image.

J'ai donc ajouté une couleur foncée et je l'ai floutée avec une valeur de 20. Vous pourriez aussi remarquer que le f1 original n'est pas aussi net que les autres couches. Le flouter lui donne cet effet d'ombre réaliste et réduit la saturation de la couleur noire. J'ai ensuite répliqué le même processus pour f2.

Dans Figma, vous pouvez facilement copier et coller un style/effet d'une couche à une autre en utilisant ctrl + alt + c pour copier et ctrl + alt + v sur la couche à laquelle vous voulez appliquer un effet ou un style similaire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*weTcM5eJwXqNTh1hNL5kSA.png)

### **Étape 5 : Travailler sur le corps**

Maintenant que nous avons terminé avec le couvercle de la boîte en carton, travaillons sur le corps de la boîte. Nous voulons refléter le rayon de lumière qui rebondit dessus ainsi que les ombres qui donnent à la boîte une apparence contrastée et réaliste.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CQhAsTiCwk3LCa8zAye_pQ.png)
_Première image : B1 avec dégradé appliqué. Deuxième image : B1 et B2 avec dégradé appliqué_

Tout ce dont nous avons besoin pour b1 et b2 est un remplissage dégradé, comme on peut le voir dans l'illustration ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tC9U9RJipP1mmrY3dNLLzA.png)
_b1 et b2_

Avez-vous remarqué que la boîte commence à paraître plus réelle ? Pouvez-vous voir la différence lorsque le dégradé est ajouté à b1 mais pas encore à b2 ? Ou lorsque le remplissage dégradé est appliqué aux deux côtés ?

Continuons.

### **Étape 6 : Le défi de l'intérieur**

Travailler sur la partie intérieure de la boîte (b3 et b4) a été un peu plus difficile. J'ai dû faire une pause de quelques minutes pour étudier les ombres et le niveau de saturation à différents coins des parties intérieures avant de penser à une façon de les reproduire — tout en utilisant encore des ombres et des dégradés.

De la même manière que précédemment, j'ai appliqué une couche de remplissage dégradé sur b4 avec des couleurs plus sombres — puisque c'est la partie la plus sombre de la boîte — pour atteindre le niveau de saturation que je voulais. Voyez l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*xps_zitJODTxsbZ1INf3XA.png)

Remarquez la façon dont les dégradés sont disposés verticalement avec une des boîtes de couleur sur la ligne de dégradé proche de l'autre ? L'idée est de faire apparaître l'ombre comme si elle venait de l'intérieur de la boîte. Bien que nous ne puissions pas voir à l'intérieur de la boîte, nous savons que plus c'est profond, moins les rayons de lumière pénètrent, ce qui rend les parties les plus intérieures automatiquement plus sombres.

### Partie finale : Les ombres sous la boîte

Ici, nous allons prendre la même idée que j'ai utilisée ci-dessus pour créer les ombres pour les couvercles de la boîte (copier les couches, redimensionner et appliquer des couleurs sombres et des effets) et la répéter. Bien que je l'aie déjà appliquée dans l'image ci-dessus, celle ci-dessous est la solution de contournement ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*YuQ5gNYsFZh43QslCvu6bQ.png)
_redimensionnement de la couche b1 originale, extension de la hauteur vers la base et ajout d'un dégradé plus sombre_

J'ai fait des copies supplémentaires de b1 et b2 et j'ai choisi la couche originale. Je l'ai ensuite tirée vers le bas, j'ai ajouté une couleur plus sombre, je l'ai légèrement floutée et je l'ai également redimensionnée pour avoir cette vue en perspective. Créer des images réalistes en art et en architecture est une question de perspective.

Nous avons maintenant créé une boîte 3D réaliste — elle n'est pas parfaite, mais elle est suffisamment réaliste. ☺️

![Image](https://cdn-media-1.freecodecamp.org/images/1*tC9U9RJipP1mmrY3dNLLzA.png)
_notre boîte en carton 3D réaliste_

### Dernières retouches

À ce stade, je me suis arrêté pour comparer ce que j'avais fait avec la boîte marron originale que j'avais trouvée sur internet. Je n'étais pas satisfait, alors j'ai décidé d'aller plus loin pour voir ce que je pouvais accomplir en essayant de faire en sorte que la boîte paraisse très réelle avec un fort contraste.

Alors, comment ai-je réalisé cela ?

J'ai créé des copies supplémentaires de b3 et b4, et j'ai appliqué une couche de dégradé à leurs copies originales (qui sont les parties sombres faisant face à nous dans l'image ci-dessous).

![Image](https://cdn-media-1.freecodecamp.org/images/1*__4V1Or93Bzur9qvXgzQTA.png)
_application de dégradé à b4 pour augmenter le contraste_

![Image](https://cdn-media-1.freecodecamp.org/images/1*zA-1ZEpHV8IYS3jjPlZFvQ.png)

En observant de plus près, vous remarquerez que cela ressemble aux bords de b1 et b2 qui ont leur propre ombre vers b4 et b3, respectivement. Cela est dû au fait que les rayons de lumière sont tombés sur eux depuis les côtés, projetant leurs ombres sur la couche ou l'objet disponible le plus proche.

Vous vous souvenez des copies supplémentaires de b1 et b2 que j'ai faites plus tôt pour former l'ombre sous la boîte ? Eh bien, j'ai d'abord redimensionné ces deux couches (b1 et b2 originaux) pour qu'elles dépassent au-dessus des versions copiées de (b1 et b2). Vous pouvez les voir comme les côtés extérieurs actuels de la boîte sur lesquels le rayon de lumière tombe. Ensuite, j'ai ajouté une autre couche de dégradé plus sombre.

Voici à quoi ressemble la boîte maintenant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WQGPpKjovMxOaDb6Fxyu8w.png)
_version finale_

_Note : L'image ci-dessus est un peu différente de celle de la partie introductive de cet article, car j'ai dû en créer une autre pour pouvoir expliquer certaines des choses que j'ai faites dans le premier design. C'était vraiment rapide_ ?

Pour obtenir plus de détails et comprendre tout ce que j'ai fait, [**voici**](https://www.figma.com/file/KZPqES7QooFN0qsA20yX4I8o/3d-box) le lien vers la version originale et la version exemple que j'ai créée.

Merci d'avoir lu !

N'hésitez pas à me contacter sur Twitter [@GbMillz](https://twitter.com/GbMillz)