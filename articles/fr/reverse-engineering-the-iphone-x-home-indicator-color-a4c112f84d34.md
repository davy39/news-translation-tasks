---
title: Ingénierie inverse de la couleur de l'indicateur d'accueil de l'iPhone X
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-29T16:28:10.000Z'
originalURL: https://freecodecamp.org/news/reverse-engineering-the-iphone-x-home-indicator-color-a4c112f84d34
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KdedwHiZuQFXgq1pDSKYtg.png
tags:
- name: Apple
  slug: apple
- name: Design
  slug: design
- name: iOS
  slug: ios
- name: iphone
  slug: iphone
- name: mobile app development
  slug: mobile-app-development
seo_title: Ingénierie inverse de la couleur de l'indicateur d'accueil de l'iPhone
  X
seo_desc: 'By Nathan Gitter

  I noticed an unusual behavior of the iPhone X home indicator while working on my
  most recent app. The app’s background near the home indicator is purple. When the
  app launches, the home indicator is very light gray.

  But something odd...'
---

Par Nathan Gitter

J'ai remarqué un comportement inhabituel de l'indicateur d'accueil de l'iPhone X en travaillant sur [ma dernière application](https://itunes.apple.com/app/id1312458558). Le fond de l'application près de l'indicateur d'accueil est violet. Lorsque l'application est lancée, l'indicateur d'accueil est de couleur gris très clair.

Mais quelque chose d'étrange s'est produit lorsque j'ai appuyé sur le bouton "partager" de l'application, qui a ouvert une vue d'activité iOS par défaut (aka "feuille de partage"). Lorsque j'ai appuyé sur le bouton "annuler" pour fermer la vue d'activité, l'indicateur d'accueil a animé vers une couleur gris foncé.

![Image](https://cdn-media-1.freecodecamp.org/images/PW1Sp7y3-Uyx8KotWbJmY3vLxeYbgTzQ1vnD)
_L'indicateur d'accueil commence en clair, puis une feuille de partage passant le rend sombre._

Même si la couleur de fond était exactement la même, la vue d'activité de couleur claire passant en dessous a provoqué le changement de couleur de l'indicateur d'accueil. La seule façon de ramener l'indicateur d'accueil à sa couleur d'origine était de quitter l'application et de revenir.

Je n'avais jamais vu cela auparavant, et cela a suscité ma curiosité.

Qu'est-ce qui détermine la couleur de l'indicateur d'accueil et pourquoi se comporte-t-il ainsi ? La réponse est surprenamment complexe. Plongeons-nous et voyons ce que nous pouvons apprendre !

![Image](https://cdn-media-1.freecodecamp.org/images/2BOISXO2zhsCXnfpgzLdSARUUYXPZ6xVW-i4)

### Les bases de l'indicateur d'accueil

En septembre 2017, Apple a introduit sa nouvelle itération de téléphone mobile : l'iPhone X. Le nouveau design a remplacé le bouton d'accueil emblématique par des gestes à l'écran. Pour revenir à l'écran d'accueil, l'utilisateur fait simplement glisser son doigt vers le haut depuis le bas de l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/HEVGYnljLUSkaodv3lCeOpTbrL2KjDG2xMd1)
_[https://www.apple.com/iphone-x/](https://www.apple.com/iphone-x/" rel="noopener" target="_blank" title=")_

### Le but de l'indicateur d'accueil

Pour créer l'affordance de pouvoir glisser vers le haut depuis le bas de l'écran, Apple a ajouté une petite barre horizontale connue sous le nom d'indicateur d'accueil. L'indicateur d'accueil est toujours présent sauf pour l'écran d'accueil et dans les applications qui demandent à ce qu'il soit temporairement masqué (vidéo en plein écran, jeux, etc.).

L'indicateur d'accueil sert un autre but : protéger le bord inférieur de l'écran des éléments d'interface utilisateur et des gestes conflictuels. Parce que l'utilisateur doit pouvoir glisser vers le haut depuis le bas de l'écran à tout moment, les meilleures pratiques dictent maintenant que les développeurs doivent éviter de placer des gestes ou des boutons conflictuels dans le bord inférieur de l'affichage.

En plaçant une barre en bas, les éléments d'interface utilisateur au même endroit _semblent incorrects_—il y a un conflit visuel entre la barre et les autres éléments. En ce sens, l'indicateur d'accueil "protège" cette région de l'écran des designers ou des ingénieurs qui ne sont pas conscients de la fonctionnalité de l'iPhone X.

![Image](https://cdn-media-1.freecodecamp.org/images/6agDeGHH86okGA0VTbuT0uz3kEETxOid-9wU)
_Il ne faut pas être un designer UI pour voir que quelque chose ne va pas ici._

Maintenant que nous sommes tous sur la même longueur d'onde, revenons à notre question initiale : "De quelle couleur est l'indicateur d'accueil ?"

### Partie 1 — Le début

Le 13 septembre 2017, j'ai répondu à une [question Stack Overflow](https://stackoverflow.com/a/46199029/6658553) demandant comment changer la couleur de l'indicateur d'accueil.

À l'époque, l'iPhone X n'avait pas encore été publié, mais la dernière version de Xcode incluait un simulateur iPhone X. L'exécution d'une simple application de test dans le simulateur a révélé que la couleur de l'indicateur d'accueil était basée sur la couleur du contenu en dessous.

Les nouvelles API pour l'iPhone X ont été publiées en même temps que cette version de Xcode, et il n'y avait pas d'API publique disponible pour modifier la couleur de l'indicateur d'accueil (ce qui est toujours le cas au moment de la rédaction de cet article, et le sera probablement toujours).

Cela a rendu ma réponse Stack Overflow simple et directe : il n'est pas possible de modifier la couleur, et vous ne devriez pas vous en soucier, car elle est hors de votre contrôle et garantie d'être visible.

Parce que je prévoyais que ce serait une question courante, j'ai inclus quelques captures d'écran de l'indicateur d'accueil sur différents fonds de couleur.

![Image](https://cdn-media-1.freecodecamp.org/images/yXawcigRDs6CVMWwxAd0IKe8x49OQF-QGkZf)
_Quelques exemples de couleurs d'indicateur d'accueil de ma réponse Stack Overflow._

Cela me suffisait. L'indicateur d'accueil maintient sa visibilité en échantillonnant la couleur de la vue en dessous et en choisissant une couleur grise qui offre un contraste suffisant.

### Partie 2 — L'intrigue s'épaissit

Il s'avère que la couleur de l'indicateur d'accueil n'est pas si simple. Certaines observations supplémentaires ont mis à mal ma théorie de la "fonction de couleur unie".

#### Observation #1 : Plusieurs couleurs

La première observation est que l'indicateur d'accueil peut avoir plusieurs couleurs, similaires à un dégradé. Dans l'exemple suivant, le côté gauche de l'écran est noir et le côté droit est blanc. L'indicateur d'accueil s'adapte à cela en adoptant une couleur plus claire sur le fond sombre et une couleur plus foncée sur le fond clair.

![Image](https://cdn-media-1.freecodecamp.org/images/ZPnZJOn4nQERqdYWY6VJgNpyWiyJFnYJlWpY)
_Si vous regardez de près, vous pouvez voir la transition du gris au noir. (simulateur iOS)_

L'indicateur d'accueil peut avoir plusieurs couleurs en même temps et passe en douceur de l'une à l'autre. Cette transition en douceur est mise à jour en temps réel si l'une des vues derrière l'indicateur d'accueil change.

![Image](https://cdn-media-1.freecodecamp.org/images/FYSsLMxrGG4qlvA8--O8VV9lrxLg2du9uIci)
_Regardez la couleur de l'indicateur d'accueil changer lorsque la vue blanche passe en dessous. (simulateur iOS)_

Dans l'exemple ci-dessus, une petite vue blanche se déplace d'avant en arrière derrière l'indicateur d'accueil. La section de l'indicateur d'accueil qui couvre la vue blanche devient noire pure et passe en douceur au gris.

Ce comportement est similaire à celui d'un `UIVisualEffectView`, qui applique un flou sur le contenu existant. L'indicateur d'accueil prend probablement un échantillon des couleurs voisines afin d'obtenir l'effet de mélange vu dans l'image ci-dessus.

(En plus de bien paraître, cette fonctionnalité pourrait aider à prévenir le burn-in sur l'écran OLED.)

#### Observation #2 : Même fond, couleur différente de l'indicateur d'accueil

Comme je l'ai mentionné au début de cet article, j'ai remarqué un comportement inhabituel lorsque la feuille de partage est passée sous l'indicateur d'accueil.

![Image](https://cdn-media-1.freecodecamp.org/images/GGyUjxfDNqAOskn7c6BGRxtesu7hqrmoFn6I)
_L'indicateur d'accueil commence en clair, la feuille de partage passant le rend sombre. (vrai iPhone X)_

C'était l'observation la plus surprenante — il n'y a pas de correspondance simple 1 à 1 entre les couleurs de fond et les couleurs de l'indicateur d'accueil. À ce stade, j'étais déterminé à en apprendre davantage par l'expérimentation.

### Partie 3 — L'enquête commence

Ma première tâche était de déterminer la formule de la couleur de l'indicateur d'accueil sur le simulateur iOS. D'après mes observations précédentes, le comportement du simulateur iOS était plus prévisible que celui d'un appareil réel.

J'ai créé une nouvelle application iOS comme laboratoire pour mes futures expériences. L'application était simple — tout ce dont j'avais besoin était un moyen facile de changer la couleur de fond derrière l'indicateur d'accueil. Un curseur et un contrôleur de pas contrôlent la valeur de gris de la couleur de fond, qui est affichée sous forme de grand nombre au centre de l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/nWzohviurK21h8OI5HAW1lK2j5-hZ2Y4Pxpc)
_L'application créée pour tester l'indicateur d'accueil._

Mon objectif était de déterminer la couleur de l'indicateur d'accueil pour chaque couleur de fond grise possible. Je pourrais tracer ces données et voir si une formule s'appliquait. Comme il n'y avait que 256 possibilités, j'ai pris l'approche manuelle, en utilisant l'application "Digital Color Meter" intégrée de macOS pour obtenir la couleur de l'indicateur d'accueil pour chaque valeur.

J'ai tracé les résultats. Ce n'était pas une fonction linéaire, une fonction exponentielle, ou tout autre type de fonction "agréable" que vous pourriez voir en cours de maths.

Le graphique était... étrange.

![Image](https://cdn-media-1.freecodecamp.org/images/EiCAcdHy9JjQ18UrUYZYFrxasQjZFldP1ocb)

Ce n'était pas ce à quoi je m'attendais.

C'était une fonction en escalier mais avec des marches inégales. Elle avait quelques sections distinctes : une période de gris (relativement) clair, deux grandes marches, une série de petites marches, des marches dans la direction inverse, et une période de noir pur.

La partie la plus inhabituelle était que la couleur de l'indicateur d'accueil n'était pas toujours décroissante. Il y avait une période (autour de rgb 170-190) où elle devenait plus claire à mesure que le fond devenait plus clair.

Pourquoi le graphique avait-il cette apparence ? Qu'est-ce que la même expérience aurait donné des résultats similaires sur un appareil réel ? J'avais besoin de savoir.

### Partie 4 — L'enquête continue

Ma prochaine tâche était de réaliser la même expérience sur un appareil réel. Il était immédiatement évident que les résultats allaient être radicalement différents.

Pour collecter des données sur un appareil réel, j'ai utilisé la même application que précédemment. J'ai diffusé un aperçu en direct de l'écran de l'iPhone sur mon ordinateur via QuickTime. Cela a éliminé toute décoloration de l'écran True Tone, ainsi que permis d'utiliser l'application Digital Color Meter pour inspecter facilement les couleurs.

Un autre facteur a ajouté à la complexité sur un appareil réel — les valeurs rouge, vert et bleu n'étaient pas toujours les mêmes. Sur le simulateur, les valeurs RVB étaient identiques, résultant en des couleurs comme RVB(54, 54, 54). Sur un appareil réel, elles étaient presque jamais les mêmes, mais étaient très proches, résultant en des couleurs comme RVB(211, 209, 212). Lors de l'enregistrement des résultats, j'ai pris la moyenne des valeurs RVB individuelles.

Voici les résultats, comparés aux données précédentes du simulateur.

![Image](https://cdn-media-1.freecodecamp.org/images/hPXJsKb9awbYEJ3YQTY0dbtRGmJ9EmFLhMk6)

Les couleurs sur un appareil réel (ligne rouge) suivent une tendance similaire à celles du simulateur (ligne bleue), sauf avec un décalage significatif. L'indicateur d'accueil du simulateur est toujours très sombre, tandis que l'indicateur d'accueil de l'appareil est soit très clair soit très sombre.

Le graphique pour l'appareil réel est bruyant. Globalement, il suit une tendance lisse, mais il monte et descend et semble rugueux. Cela est plus qu'un simple effet secondaire de ma moyenne, et le bruit est cohérent. Si l'expérience est répétée, le bruit suit le même motif exact.

Cependant, le graphique ci-dessus ne raconte pas toute l'histoire.

Les valeurs présentées ci-dessus ont été recueillies en commençant par un fond complètement noir et en incrémentant les valeurs RVB une à la fois (allant de 0 à 255). **Lorsque les valeurs sont recueillies dans la direction opposée, les résultats sont différents.**

À un certain moment, la couleur de l'indicateur d'accueil "tombe de la falaise" dans sa transition de clair à sombre ou de sombre à clair, et s'anime pendant une courte période, comme montré dans le gif précédent avec la couleur de fond violette. Selon que le fond commence clair ou sombre, la falaise se produit à un endroit différent.

Examinons un nouveau graphique comparant les résultats de "montée" (noir à blanc) et de "descente" (blanc à noir).

![Image](https://cdn-media-1.freecodecamp.org/images/adFEPIdfwqPFvZB4ShWxXVXbb3F2o4focA9E)

La ligne bleue ci-dessus est la même que la ligne rouge du graphique précédent. Ses points de données ont été collectés de gauche à droite (0 à 255, "montée"). La ligne orange est la même donnée, mais collectée dans la direction opposée (255 à 0, "descente"). La ligne rouge représente les points où l'indicateur d'accueil et le fond de la vue sont de la même couleur.

Les lignes "montée" et "descente" suivent un chemin similaire, mais ont un motif de bruit différent. Intéressamment, elles ont le même motif de bruit exact dans la plage la plus sombre (0-80).

À partir de ce graphique, nous pouvons dire que les "falaises" se produisent lorsque la couleur de l'indicateur d'accueil se rapproche trop de la couleur du fond. Il semble même que les lignes "montée" et "descente" soient repoussées par la ligne rouge, essayant activement de résister à devenir exactement de la même couleur que le fond. À un certain point, l'indicateur d'accueil bascule pour devenir très sombre ou très clair.

Cela explique le changement de couleur dans l'application avec le fond violet. La couleur violette doit être dans une région entre les deux falaises. Sur la base de la couleur précédente de l'indicateur d'accueil, il pourrait être clair ou sombre. Lorsque la vue d'activité blanche s'anime derrière l'indicateur d'accueil lors de sa fermeture, l'indicateur d'accueil passe de son état clair à son état sombre, et se réinstalle à la valeur sombre équivalente pour la couleur de fond violette.

### Partie 5 — L'enquête devient colorée

Tous les tests jusqu'à ce point ont utilisé des fonds en niveaux de gris. Comment les résultats différeraient-ils si nous utilisions des fonds colorés à la place ?

J'ai répété la même expérience, mais au lieu de modifier la couleur grise, j'ai modifié la teinte sur une échelle de couleur HSB. J'ai gardé la saturation (S) et la luminosité (B) à leurs valeurs maximales pour obtenir les couleurs les plus vibrantes et distinctes. Je n'ai testé ces couleurs qu'en "montée", ce qui dans ce cas signifie de la teinte 0 (rouge) à la teinte 255 (rouge) dans l'ordre de l'arc-en-ciel.

![Image](https://cdn-media-1.freecodecamp.org/images/mNmkHQrkvj5wMIK6Kp0EfYPBuo5zly9hjBik)

La première observation est qu'il y a deux falaises — une fois lorsque la couleur devient jaune, et à nouveau lorsque la couleur devient bleu foncé. Cela se produit en raison de la "luminosité" relative des couleurs.

L'observation suivante est la différence entre le simulateur et un appareil réel. Les couleurs suivent les mêmes tendances générales, mais la couleur de l'indicateur d'accueil de l'appareil réel est plus bruyante et peut atteindre des valeurs plus lumineuses.

Ce sont des découvertes fascinantes jusqu'à présent. En dehors de tester chaque couleur de fond possible, il n'y a pas grand-chose d'autre que nous pouvons découvrir par l'observation seule. Maintenant, j'étais curieux de savoir exactement comment l'indicateur d'accueil est implémenté — est-ce un `UIView` ? `CALayer` ? `UIVisualEffectView` ? Autre chose ? Qu'est-ce qui le fait se comporter de cette manière ?

Découvrons-le.

### Partie 6 — Il faut aller plus loin !

À ce stade, je me suis tourné vers mon ami et [expert iOS Ian McDowell](https://twitter.com/ian_mcdowell). Il a pu me pointer dans la bonne direction — utiliser le simulateur iPhone X et les outils de débogage de Xcode pour trouver l'indicateur d'accueil.

L'écran d'accueil iOS est en fait une application appelée SpringBoard. Nous pouvons attacher un débogueur à l'application SpringBoard en cours d'exécution dans le simulateur iPhone X et utiliser l'option "Debug View Hierarchy" afin d'inspecter les vues qui composent l'écran d'accueil, y compris l'indicateur d'accueil.

Si vous voulez suivre à la maison, voici le processus :

1. Lancez un simulateur iPhone X.
2. Dans Xcode, sélectionnez Debug > Attach to Process... > SpringBoard.
3. Lorsque SpringBoard est en cours d'exécution, sélectionnez le bouton Debug View Hierarchy.

Au fond de la hiérarchie des vues, nous trouvons un `MTLumaDodgePillView` qui est une sous-vue d'un `SBHomeGrabberView`. On dirait que nous avons trouvé l'indicateur d'accueil !

![Image](https://cdn-media-1.freecodecamp.org/images/dQxjnOKrUanJrQugTMg8Trr1QxSvDm9htka3)
_Nous avons trouvé l'indicateur d'accueil !_

Le nom `MTLumaDodgePillView` a du sens. Il confirme notre comportement observé de l'indicateur d'accueil, que sa couleur contraste avec le fond en fonction de sa luminosité actuelle.

Pouvons-nous aller plus loin ?

SpringBoard a une autre fonctionnalité intéressante : un menu de débogage caché. Il s'avère qu'il y a une section entière pour modifier les propriétés de l'indicateur d'accueil. Dans ce menu de débogage, l'indicateur d'accueil est appelé un "grabber".

![Image](https://cdn-media-1.freecodecamp.org/images/icEJTKHTlmST3Kg7FK8mPVHXTZGIkZBIvj8X)
_Tant de curseurs amusants avec lesquels jouer. ?_

Ce menu de débogage contient principalement des paramètres visuels et d'animation. Il est probablement utilisé pour collaborer entre le design et l'ingénierie au sein d'Apple. L'ingénierie construit l'indicateur d'accueil, fournit des crochets à tous les paramètres internes, laisse les designers les ajuster jusqu'à ce qu'ils soient satisfaits, puis les ingénieurs utilisent les paramètres pour le produit final.

Heureusement pour nous, nous pouvons accéder à ce menu et voir les résultats dans le simulateur.

J'ai d'abord joué avec l'apparence visuelle de l'indicateur d'accueil. Il y a des curseurs pour la largeur et la hauteur dans divers états.

![Image](https://cdn-media-1.freecodecamp.org/images/mC1yawDoCBeSgAN3nPmNfHtPpdXNIJf0JWfJ)
_Quelques tailles alternatives de l'indicateur d'accueil._

Les autres paramètres sont plus difficiles à tester, car ils ne semblent pas s'appliquer au simulateur. Il y a des paramètres pour un "seuil de luminosité" pour le clair et le foncé, ainsi que des paramètres pour l'animation entre les états. Cela confirme les "falaises" où la couleur s'animerait de manière dramatique entre le clair et le foncé — il y a des seuils prédéfinis basés sur la luminosité du fond.

Je n'ai pas pu déterminer pourquoi le simulateur se comporte si différemment d'un appareil réel. Mon hypothèse est que le simulateur utilise une combinaison différente de paramètres, ou que certains paramètres ne prennent effet que sur du matériel réel.

Vous voulez en savoir plus sur l'ingénierie inverse sur iOS ? Sash Zats a publié [un article approfondi incroyable sur l'indicateur d'accueil](http://blog.zats.io/2017/12/27/iPhone-X-home-button/). Consultez-le si vous voulez plonger dans plus de code !

Cela marque la fin de l'aventure de la découverte de l'indicateur d'accueil. J'espère que cela a été aussi éducatif pour vous que pour moi !

### Principaux enseignements

1. La couleur de l'indicateur d'accueil est déterminée par le système et ne peut pas être modifiée directement.
2. La couleur de l'indicateur d'accueil est déterminée par le contenu en dessous, et ce n'est pas toujours une couleur unie.
3. L'indicateur d'accueil sur le simulateur n'est **pas** une représentation précise de l'indicateur d'accueil sur un appareil réel.
4. L'indicateur d'accueil s'anime vers sa ou ses nouvelles couleurs lorsque le contenu en dessous change.
5. L'indicateur d'accueil est soit dans un état "clair" soit dans un état "sombre".

### Mais... Pourquoi ?

Pourquoi s'embêter à enquêter sur l'indicateur d'accueil si son apparence est hors de notre contrôle ?

Il y a une application pratique pour ces apprentissages : Si un écran dans votre application a une couleur de fond dans la plage moyenne où l'indicateur d'accueil pourrait être soit clair soit sombre, vous pouvez préférer un style à l'autre. Si la barre d'état est blanche, par exemple, il peut sembler plus équilibré visuellement si l'indicateur d'accueil est également blanc. Être conscient du comportement nuancé de l'indicateur d'accueil peut aider à s'assurer qu'il ne s'anime pas accidentellement entre clair et sombre lorsqu'il pourrait distraire l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/RA0vUMMWwxosnDxMxSGhLOsm3HXCD4OHckTZ)
_Préférez-vous l'un à l'autre ?_

Dans un exemple précédent, la feuille de partage blanche s'animant derrière l'indicateur d'accueil était suffisante pour changer le style de l'indicateur d'accueil.

Si je voulais empêcher cela, je pourrais épingler une vue derrière l'indicateur d'accueil entre la zone sécurisée et le bord inférieur de l'affichage. Lorsque la feuille de partage est fermée, je pourrais lui donner une couleur de fond plus foncée (peut-être noire avec 40 % d'opacité) et ajouter une animation de fondu pour qu'elle soit moins noticeable.

Cette même tactique pourrait être utilisée pour définir la couleur de l'indicateur d'accueil — le forçant à passer l'une des "falaises". Dans la grande majorité des cas, l'indicateur d'accueil devrait être laissé tranquille pour faire ce qu'il veut. La plupart des utilisateurs de l'iPhone X ont probablement déjà oublié qu'il est même là.

### La vraie leçon

Espérons que cette brève enquête sur la couleur de l'indicateur d'accueil nous aide à apprécier la complexité du design simple. "Ce n'est qu'une barre noire/blanche !" est loin de la vérité. La quantité de soin et d'attention aux détails qui a été mise dans l'indicateur d'accueil mérite d'être appréciée.

Prendre quelque chose de simple, enquêter sur ses complexités internes et réfléchir à son design nous aide à apprendre sur le processus créatif. En combinant le design et l'ingénierie, nous pouvons créer de meilleurs produits qui sont simples et agréables à utiliser.

Avez-vous apprécié l'histoire ? Laissez quelques applaudissements ? ici sur Medium et partagez-la avec vos amis designers/développeurs iOS. Vous voulez rester à jour sur les dernières tendances en matière de design/développement d'applications mobiles ? Suivez-moi sur Twitter ici : [https://twitter.com/nathangitter](https://twitter.com/nathangitter)

Merci à [Ian McDowell](https://twitter.com/ian_mcdowell) et [David Okun](https://twitter.com/dokun24) pour avoir aidé à réviser les versions précédentes de cet article.