---
title: Apprenez CSS Flexbox dans ce tutoriel GRATUIT et interactif
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-25T05:34:06.000Z'
originalURL: https://freecodecamp.org/news/i-just-launched-a-free-full-length-flexbox-course-where-you-can-build-projects-interactively-1860e3d3c4af
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lTZoPTPzuKifD2wr3rUETw.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: startup
  slug: startup
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Apprenez CSS Flexbox dans ce tutoriel GRATUIT et interactif
seo_desc: 'By Per Harald Borgen

  After the success of the CSS Grid course I launched with freeCodeCamp in December
  (over 14,000 students so far!), I decided to launch a second free course.

  This time you can learn Flexbox, which has become a must-have skill for f...'
---

Par Per Harald Borgen

Après le succès du [cours CSS Grid que j'ai lancé](https://medium.freecodecamp.org/heres-my-free-css-grid-course-merry-christmas-3826dd24f098) avec freeCodeCamp en décembre (plus de 14 000 étudiants à ce jour !), j'ai décidé de lancer un deuxième cours gratuit.

Cette fois, vous pouvez apprendre Flexbox, qui est devenu une compétence indispensable pour les développeurs front-end.

Flexbox était également l'une des demandes les plus fréquentes que j'ai reçues des étudiants qui ont suivi le cours CSS Grid.

Dans cet article, je vais expliquer comment le cours Flexbox est structuré afin que vous puissiez décider s'il vous convient.

Mais si vous voulez vous lancer directement dans le cours, vous pouvez [y aller directement et commencer](https://scrimba.com/g/gflexbox?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_launch_article).

Mise à jour : J'ai également lancé un cours gratuit sur les [variables CSS ici.](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_launch_article)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/gflexbox-1.png)
_[Cliquez ici pour accéder au cours.](https://scrimba.com/g/gflexbox?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gflexbox_launch_article)_

### Ce que couvre mon cours Flexbox

Le cours se compose de douze screencasts interactifs, qui vous mènent de débutant à avancé. Il est axé sur l'acquisition de compétences pertinentes dès que possible, ce qui signifie que j'ai priorisé les propriétés en fonction de leur utilité dans un contexte réel.

Ainsi, si vous ne travaillez que sur les cinq premiers, vous apprendrez tout de même de nouveaux concepts que vous pourrez commencer à utiliser dans vos projets. Cela dit, je recommande tout de même de suivre l'ensemble du cours.

Tout au long du cours, vous construirez et expérimenterez avec une barre de navigation, car c'est un cas d'utilisation très typique pour Flexbox.

Examinons chacun des screencasts :

#### Leçon #1 : Votre premier Flexbox

![Image](https://cdn-media-1.freecodecamp.org/images/1*rPzIll98F0gHToNeKZE3RQ.png)

Vous commencerez par créer une mise en page simple. Cela vous enseignera le concept de conteneur flex et d'éléments flex, les deux ingrédients de base d'une mise en page Flexbox.

#### Leçon #2 : Axe principal et axe transversal

![Image](https://cdn-media-1.freecodecamp.org/images/1*1z53nj8_eUtwkdyr6UEAfg.png)

Dans le deuxième screencast, j'explique un concept fondamental de Flexbox qu'il est crucial de comprendre dès le début : les axes. Une mise en page Flexbox a deux axes : l'axe principal et l'axe transversal. Par défaut, l'axe principal est horizontal et l'axe transversal vertical, mais ils peuvent également échanger leurs rôles.

#### Leçon #3 : Comment justifier le contenu

![Image](https://cdn-media-1.freecodecamp.org/images/1*oX0mCKg4caqQE7X04CvIiw.png)

La propriété `justify-content` contrôle le contenu le long de l'axe principal. Tout au long du cours, votre axe principal sera principalement horizontal, par opposition à vertical. J'ai choisi de faire ainsi car j'ai constaté que les mises en page Flexbox horizontales sont plus courantes que les verticales dans la vie réelle.

#### Leçon #4 : Comment positionner des éléments individuels

![Image](https://cdn-media-1.freecodecamp.org/images/1*TK1nvZSGCbi3EfQBwMQbgQ.png)

Dans cette leçon, vous apprendrez à positionner des éléments individuels en utilisant la bonne vieille technique consistant à définir la `margin` sur auto.

#### Leçon #5 : La propriété flex

![Image](https://cdn-media-1.freecodecamp.org/images/1*gnO8ugL8stVg0ytPlTJNEQ.png)

La propriété `flex` vous permet de donner à vos éléments des largeurs réactives. C'est en fait une abréviation pour trois autres propriétés : `flex-grow`, `flex-shrink` et `flex-basis`. Mais nous les garderons pour la fin du cours, car elles sont plus avancées.

#### Leçon #6 : Comment aligner les éléments

![Image](https://cdn-media-1.freecodecamp.org/images/1*bpDqaWA3uSwUtdXDKAwg6w.png)

La propriété `align-items` contrôle les éléments le long de l'axe transversal, qui dans notre cas est vertical. Dans l'image ci-dessus, nous avons centré les éléments le long de cet axe.

#### Leçon #7 : Direction de la colonne Flex

![Image](https://cdn-media-1.freecodecamp.org/images/1*U9_BLWNTbc91G8zGb9kXFQ.png)

Définir la `flex-direction` sur colonne inversera l'axe principal et l'axe transversal, de sorte que les éléments soient disposés vers le bas plutôt que sur le côté.

#### Leçon #8 : Retour à la ligne

![Image](https://cdn-media-1.freecodecamp.org/images/1*NVE8i0fzYR_lkztjmhgN5w.png)

Par défaut, Flexbox ne vous permettra pas de retourner à la ligne vos éléments, ce qui signifie qu'ils resteront sur une seule ligne ou une seule rangée. Si vous définissez `flex-wrap` sur wrap, vous pourrez le faire. Je vais montrer comment cela se passe.

#### Leçon #9 : Flex grow, shrink et basis

![Image](https://cdn-media-1.freecodecamp.org/images/1*Xbb_jKfJ9rbXTeWqs89MRw.gif)

Flex grow, shrink et basis sont un peu complexes à comprendre, c'est donc le screencast le plus long du cours. En bref, `flex-basis` définit la largeur de base de l'élément, `flex-grow` contrôle comment il va croître au-dessus de sa largeur de base, et `flex-shrink` contrôle comment il va rétrécir lorsque l'élément est plus étroit que sa largeur de base.

#### Leçon #10 : Ordre

![Image](https://cdn-media-1.freecodecamp.org/images/1*hyzXwySi5-ep_j8rfCEi9A.png)

Nous terminerons le cours par une leçon sur la propriété `order`. Cela vous introduira à l'indépendance de l'ordre source, qui vous permet de définir l'ordre des éléments indépendamment de leur disposition dans le HTML.

#### Section bonus

Dans la section bonus, vous créerez deux mises en page réelles de début à fin.

Dans la première, vous utiliserez tout ce que vous avez appris dans le cours pour créer une barre de navigation qui s'adapte à diverses tailles d'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CZikqoB4iZIIrV_rAW_qdg.gif)

Dans la deuxième leçon bonus, vous expérimenterez la création d'une grille d'images avec Flexbox. Si vous avez suivi mon cours CSS Grid, vous reconnaîtrez la configuration :

![Image](https://cdn-media-1.freecodecamp.org/images/1*e7EoeCwxU6RCPKsj72KkUg.png)

Et c'est tout.

### Le format Scrimba

Examinons enfin la technologie derrière le cours. Il est construit en utilisant Scrimba, un outil de screencast de codage interactif qui a été développé par mes deux cofondateurs géniaux [Sindre](https://medium.com/u/c825b7f99be3) et [Magnus](https://medium.com/u/1a7998d688dd).

Les screencasts Scrimba ressemblent à des vidéos normales, mais ils sont entièrement interactifs. Vous pouvez modifier le code à l'intérieur des casts.

Voici un gif qui explique le concept :

![Pausez le screencast → Modifiez le code → Exécutez-le ! → Voyez vos modifications](https://cdn-media-1.freecodecamp.org/images/1*4PWxbgV--7ZHlB-YVqavJg.gif)

Pausez le screencast → Modifiez le code → Exécutez-le ! → Voyez vos modifications

C'est idéal lorsque vous sentez que vous devez expérimenter avec le code pour bien le comprendre, ou lorsque vous souhaitez simplement copier un morceau de code.

De plus, comme les screencasts Scrimba se déroulent dans un éditeur de code, ils n'utilisent qu'environ 1 % de la bande passante qu'une vidéo normale utiliserait. Cela signifie que les screencasts Scrimba sont beaucoup plus faciles à diffuser, même lorsque votre connexion Internet est lente.

J'espère que vous apprécierez le cours. Si vous avez des commentaires ou des demandes pour ajouter d'autres screencasts, n'hésitez pas à [me le faire savoir sur Twitter](https://twitter.com/perborgen) et je serais ravi de les considérer.

Bon codage !

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le cofondateur de [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_launch_article) – la manière la plus simple d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web réactif](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gflexbox_launch_article) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gflexbox_launch_article)_