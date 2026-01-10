---
title: Material Design et le problème de la navigation Mystery Meat
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-27T04:20:09.000Z'
originalURL: https://freecodecamp.org/news/material-design-and-the-mystery-meat-navigation-problem-65425fb5b52e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zWh3_7qHGS1sWYzzEnhaXw.png
tags:
- name: Design
  slug: design
- name: Material Design
  slug: material-design
- name: mobile
  slug: mobile
- name: UX
  slug: ux
- name: ux design
  slug: ux-design
seo_title: Material Design et le problème de la navigation Mystery Meat
seo_desc: 'By Teo Yu Siang

  In March 2016, Google updated Material Design to add bottom navigation bars to its
  UI library. This new bar is positioned at the bottom of an app, and contains 3 to
  5 icons that allow users to navigate between top-level views in an ap...'
---

Par Teo Yu Siang

En mars 2016, Google a [mis à jour](http://www.androidauthority.com/bottom-navigation-material-design-guidelines-680207/) Material Design pour ajouter des barres de navigation inférieures à sa bibliothèque d'interface utilisateur. Cette nouvelle barre est positionnée en bas d'une application et contient 3 à 5 icônes qui permettent aux utilisateurs de naviguer entre les vues de premier niveau d'une application.

Ça vous dit quelque chose ? C'est parce que les barres de navigation inférieures font partie de la [bibliothèque d'interface utilisateur d'iOS](https://developer.apple.com/ios/human-interface-guidelines/ui-bars/tab-bars/) depuis des années (elles sont appelées barres d'onglets dans iOS).

![Image](https://cdn-media-1.freecodecamp.org/images/7YItl6X12sekqS7gEvWob4GYqKgaeBZQHij9)
_Gauche : barre de navigation inférieure de Material Design | Droite : barre d'onglets d'iOS_

Les barres de navigation inférieures sont [une meilleure alternative](http://www.lukew.com/ff/entry.asp?1945) au menu hamburger, donc leur ajout dans Material Design devrait être une bonne nouvelle. Mais la version de Google des barres de navigation inférieures a un sérieux problème : **la navigation Mystery Meat**.

Que vous soyez un utilisateur, un designer ou un développeur Android, cela devrait vous préoccuper.

### Qu'est-ce que la navigation Mystery Meat et pourquoi est-elle si mauvaise ?

La navigation Mystery Meat est un terme inventé en 1998 par Vincent Flanders du célèbre site [Web Pages That Suck](http://www.webpagesthatsuck.com/). Il fait référence aux boutons ou liens qui n'expliquent pas ce qu'ils font. Au lieu de cela, vous devez cliquer dessus pour le découvrir.

(Le terme « mystery meat » provient de la viande servie dans les cafétérias des écoles publiques américaines qui était si transformée que le type d'animal dont elle provenait n'était plus discernable.)

![Image](https://cdn-media-1.freecodecamp.org/images/DCG0RcBAYpPo1PiWKyXvJ6udqLMKsAL4orlG)
_Un exemple de navigation Mystery Meat | [Source](http://gigi.nullneuron.net/gigilabs/on-mystery-meat-navigation-and-unusability/" rel="noopener" target="_blank" title=")_

**La navigation Mystery Meat est la marque des designs qui privilégient la forme à la fonction.** C'est un mauvais design UX, car il met l'accent sur l'esthétique au détriment de l'expérience utilisateur. Il ajoute une charge cognitive aux tâches de navigation, puisque les utilisateurs doivent deviner ce que fait le bouton. Et si vos utilisateurs doivent deviner, c'est que vous faites quelque chose de mal.

Vous ne voudriez pas manger de viande mystérieuse—de la même manière, les utilisateurs ne voudraient pas cliquer sur des boutons mystérieux.

### Strike 1 : La barre de navigation d'Android Lollipop

Le premier problème majeur de navigation Mystery Meat de Material Design est survenu en 2014 avec Android Lollipop.

Android Lollipop a été introduit lors de la même conférence qui a présenté Material Design, et arbore une interface utilisateur redessinée pour correspondre au nouveau langage de design de Google.

![Image](https://cdn-media-1.freecodecamp.org/images/Wdwchat-pQDuQX5nPu8I8w8ClC9iKK2wEA4T)
_Barre de navigation dans les versions antérieures d'Android_

L'un des éléments d'interface qui a été redessiné était la barre de navigation, la barre persistante en bas du système d'exploitation Android qui fournit des contrôles de navigation pour les téléphones sans boutons matériels pour Retour, Accueil et Menu.

Dans Android Lollipop, la barre de navigation a été redessinée comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/7nRsekkx7N76oZ0R2901z7FLPs0JUBefoSJs)
_Barre de navigation, Android Lollipop et versions ultérieures_

Voyez-vous le problème ?

Bien que le design précédent soit moins esthétique, il est plus ou moins direct. Les icônes Retour et Accueil peuvent être comprises sans besoin de libellés textuels. La 3ème icône est un peu un mystère, mais dans l'ensemble, l'UX de l'ancienne barre de navigation n'était pas trop mauvaise.

La nouvelle barre, en revanche, est _extrêmement_ belle. Le triangle équilatéral, le cercle et le carré sont des symboles de perfection géométrique. Mais elle est aussi _extrêmement_ peu conviviale. Elle est abstraite—et les contrôles de navigation ne devraient jamais être abstraits. C'est une navigation Mystery Meat à part entière.

L'icône du triangle peut ressembler à une flèche « Retour », mais que signifient un cercle et un carré en relation avec le contrôle de navigation ?

![Image](https://cdn-media-1.freecodecamp.org/images/nvOaaRnehcqssATkE4qJY7MzIiba7GoPVrlE)
_Comprendre les icônes de la barre de navigation_

### Strike 2 : Les boutons d'action flottants

Les boutons d'action flottants sont des boutons spéciaux qui apparaissent au-dessus des autres éléments d'interface utilisateur dans une application. Idéalement, ils sont utilisés pour promouvoir l'action principale de l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/MwpSqGbO5h9GLia5FMdnpsMVsxz0-SbU5BbM)
_Spécifications pour le bouton d'action flottant | [Source](https://material.io/guidelines/components/buttons-floating-action-button.html#buttons-floating-action-button-floating-action-button" rel="noopener" target="_blank" title=")_

Les boutons d'action flottants souffrent également du problème de navigation Mystery Meat. Par conception, le bouton d'action flottant est un cercle contenant une icône. C'est un bouton purement iconique, sans place pour des libellés textuels.

La vérité est que [**les icônes sont incroyablement difficiles à comprendre**](http://uxmyths.com/post/715009009/myth-icons-enhance-usability) car elles sont si ouvertes à l'interprétation. Notre culture et nos expériences passées influencent la manière dont nous interprétons les icônes. Malheureusement, les designers (en particulier, semble-t-il, les designers Material) ont du mal à faire face à cette vérité.

Besoin d'une preuve que les boutons avec uniquement des icônes sont une mauvaise idée ? Jouons à un jeu de devinettes.

Ci-dessous se trouve une liste de ce que—selon les [directives](https://material.io/guidelines/components/buttons-floating-action-button.html) de Material Design—sont des icônes acceptables pour les boutons d'action flottants. Pouvez-vous deviner ce que fait chaque bouton ?

![Image](https://cdn-media-1.freecodecamp.org/images/YvRDCuTrv7S8S76-ENqYBgS8GI8OjaIwXY-v)
_Bouton mystère 1_

D'accord, c'est un simple pour vous échauffer. Il représente « Directions ».

![Image](https://cdn-media-1.freecodecamp.org/images/2lqEudSZmyNmqGtpjrn4I2RtPYIZDbUnwwYL)
_Bouton mystère 2_

Et celui-ci ? Si vous êtes un utilisateur iOS ou Mac, vous pourriez dire « Safari ». Il représente en réalité « Explorer ».

![Image](https://cdn-media-1.freecodecamp.org/images/UUHgLVPW5MWGIx-1tiy2JAghliERwnjw6gDe)
_Bouton mystère 3_

Les choses deviennent amusantes (ou frustrantes) maintenant ! Cela pourrait-il être « Ouvrir dans les contacts » ? « Aide, quelqu'un me suit » ? Peut-être est-ce un bouton pour votre ligne de vie « Téléphoner à un ami ».

![Image](https://cdn-media-1.freecodecamp.org/images/QqiP6oceM0SVfMXfLxNPs4lajjSleb9kdb2g)
_Bouton mystère 4_

Attendez, _celui-ci_ est le bouton pour « Ouvrir dans les contacts ». N'est-ce pas ? Ou est-ce « Potiner sur un ami » puisque la personne est à l'intérieur d'une bulle de discours ?

Prêt pour la dernière manche ? Voici la pire (et la plus utilisée) icône :

![Image](https://cdn-media-1.freecodecamp.org/images/eYdflx0Iu5vUqPOt2QKCO0LR52ndHAPD9pCt)
_Bouton mystère 5_

Vous pourriez penser que le bouton « + » est plutôt simple à comprendre—il s'agit évidemment d'un bouton pour l'action « Ajouter ». Mais ajouter _quoi_ ?

_Ajouter quoi_ : voilà le problème. Si un utilisateur doit poser cette question, votre bouton est officiellement un mystère. Malheureusement, les développeurs et designers d'applications Material Design semblent être amoureux du bouton d'action flottant « + ».

Précisément parce que le bouton « + » _semble_ si facile à comprendre, il finit par être l'icône la plus abusée pour les boutons d'action flottants. Considérez comment l'application Inbox de Google affiche des boutons _supplémentaires_ lorsque vous appuyez sur le bouton flottant « + », ce qui n'est pas ce à quoi un utilisateur s'attendrait :

![Image](https://cdn-media-1.freecodecamp.org/images/f1EkSce5KKMIhKgbVxSkSisB5GnLbW6uly0y)

![Image](https://cdn-media-1.freecodecamp.org/images/CIE3zt1sLgpfCwGBs0ivSgBkQ8PJYtQ1l9ox)
_Le bouton « + » ouvre un menu de... plus de boutons ?_

Ce qui aggrave les choses, c'est la manière dont les mêmes icônes ont des significations différentes dans différentes applications. Google a utilisé l'icône du crayon pour représenter « Composer » dans Inbox et Gmail, mais l'a utilisée pour représenter « Modifier » dans son application photo Snapseed.

![Image](https://cdn-media-1.freecodecamp.org/images/31VNlRc307i36uGhWuNUC61Iib9ldA34nD7G)

![Image](https://cdn-media-1.freecodecamp.org/images/FdIG9drQMkrMFpYWlxHM4INmxjVtaM8tN53B)

![Image](https://cdn-media-1.freecodecamp.org/images/ezUJoa3dZv6IUhS-QKYc6jWGiBc6apr12efj)
_Même icône, significations différentes : « Composer » dans les applications Gmail et Inbox, « Modifier » dans l'application Snapseed_

Le bouton d'action flottant était censé être un excellent moyen pour les utilisateurs d'accéder à une action principale. Sauf que ce n'est pas le cas, car les boutons avec uniquement des icônes tendent à être des mystères.

Plus sur les boutons d'action flottants :

[**Material Design :**](https://medium.com/tech-in-asia/material-design-why-the-floating-action-button-is-bad-ux-design-acd5b32c5ef)
[**Pourquoi le bouton d'action flottant est un mauvais design UX**](https://medium.com/tech-in-asia/material-design-why-the-floating-action-button-is-bad-ux-design-acd5b32c5ef)
[_Material Design est un langage de design introduit par Google il y a un an, et représente la tentative audacieuse de l'entreprise de..._medium.com](https://medium.com/tech-in-asia/material-design-why-the-floating-action-button-is-bad-ux-design-acd5b32c5ef)

### Strike 3 : La nouvelle barre de navigation inférieure

Cela nous amène à la barre de navigation inférieure, introduite en mars 2016.

Pour les barres de navigation inférieures avec 3 vues, les directives de Google spécifient que les icônes et les libellés textuels doivent être affichés. Jusqu'à présent, tout va bien : pas de mystère ici.

![Image](https://cdn-media-1.freecodecamp.org/images/YGvSiyZjDEce7u2NuFDrRyW7qS77YeOLOuEx)
_Barre de navigation inférieure avec 3 vues : jusqu'à présent, tout va bien_

Mais pour les barres de navigation inférieures avec 4 ou 5 vues, Google spécifie que les vues inactives doivent être affichées sous forme d'_icônes uniquement_.

![Image](https://cdn-media-1.freecodecamp.org/images/D7CeYD631OThLgasrNa4NyDb5HpB60IeJWhF)
_Barre de navigation inférieure avec 4 vues : mystère_

Vous souvenez-vous à quel point il était difficile de deviner ce que signifient les icônes des boutons d'action flottants ? Essayez maintenant de deviner une rangée d'icônes utilisées pour naviguer dans une application.

C'est simplement un mauvais design UX. En fait, le groupe Nielsen Norman [soutient](https://www.nngroup.com/articles/icon-usability/) que les icônes _ont besoin_ d'un libellé textuel, surtout les icônes de navigation (emphase theirs) :

> « Pour aider à surmonter l'ambiguïté à laquelle presque toutes les icônes sont confrontées, un **libellé textuel doit être présent à côté d'une icône** pour clarifier sa signification dans ce contexte particulier. ... Pour les icônes de navigation, les libellés sont particulièrement critiques. »

Que le nouveau composant d'interface utilisateur de Material Design cautionne la navigation Mystery Meat n'est pas seulement frustrant, mais aussi étrange. Pourquoi les libellés textuels devraient-ils être affichés lorsqu'il y a 3 vues, mais être masqués lorsqu'il y a 4 à 5 vues ?

Une réponse évidente serait les contraintes d'espace.

Sauf que les barres d'onglets d'iOS parviennent à contenir 5 icônes et à afficher l'icône et le libellé textuel pour chacune d'entre elles. Donc, la contrainte d'espace n'est pas une raison valable.

![Image](https://cdn-media-1.freecodecamp.org/images/XuHqU7P7rXUzZjAawfbA89u2Gj12Ll6DBQSh)

![Image](https://cdn-media-1.freecodecamp.org/images/8U5exm475tOlJbYAJW8PJeWECTC-PLX93G00)

![Image](https://cdn-media-1.freecodecamp.org/images/Cv6H3piHbcpMiAYyD7h0Ro1CsMi4tuhXw7ed)
_Barre d'onglets iOS dans les applications App Store, Horloge et Musique : 5 icônes, toutes avec des libellés textuels_

Google a soit décidé que les icônes peuvent représenter suffisamment les actions de navigation (ce qui est mauvais), soit ils ont décidé que la propreté esthétique est plus importante que l'utilisabilité (ce qui est pire). Dans les deux cas, leur décision a aggravé l'UX de millions d'utilisateurs Android.

### Material Design et la forme sur la fonction

Lorsque Material Design a été lancé en 2014, il a été accueilli avec beaucoup d'enthousiasme. Il est audacieux et surfe sur (et surpasse) la tendance du design plat. L'association de couleurs vibrantes et d'animations le rend beau à regarder.

![Image](https://cdn-media-1.freecodecamp.org/images/OLb76CbG4u49bqTlU4WNfUXsIWhcmHQ397no)
« Rendez-le joli ! » — Designer de Material Design | [Source](https://www.youtube.com/watch?v=Q8TXgCzxEnw" rel="noopener" target="_blank" title=")_

Mais peut-être est-il un peu _trop_ joli. Peut-être que, tout en travaillant sur Material Design, les designers se sont un peu emportés.

À maintes reprises, les directives de Google pour les boutons et barres importants semblent privilégier la forme à la fonction. La beauté géométrique a été choisie au détriment de la reconnaissabilité dans la barre de navigation d'Android. La simplicité esthétique a été prônée dans les boutons d'action flottants, les transformant en énigmes au passage. Enfin, la propreté visuelle a été jugée plus importante que les libellés significatifs dans les barres de navigation inférieures.

Cela ne signifie pas que la navigation Mystery Meat est un problème exclusif à Google. Bien sûr, vous pouvez trouver des mystères dans les applications iOS aussi. Mais ils n'apparaissent généralement pas dans les contrôles de navigation critiques et les boutons promus. Ils ne sont pas non plus spécifiquement énoncés dans les directives de design pour être des mystères.

![Image](https://cdn-media-1.freecodecamp.org/images/If7hVf7dEE1YQkJoUeavMmsb0BbrZ0ttLGyV)
_Graphique de vitesse montrant la bonne (bleue) accélération pour les animations_

Si les designers de Google pouvaient consacrer du temps et des efforts à la création de graphiques de vitesse pour les animations, peut-être pourraient-ils passer un peu de temps à s'assurer que leurs designs ne sont pas des mystères.

Après tout, un bouton mystère animé est toujours moins agréable qu'un bouton statique mais clairement étiqueté.