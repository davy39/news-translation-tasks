---
title: Mes astuces préférées pour les outils de développement Chrome
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-10T16:56:03.000Z'
originalURL: https://freecodecamp.org/news/awesome-chrome-dev-tools-tips-and-tricks
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/cover_image.png
tags:
- name: Google Chrome
  slug: chrome
- name: Developer Tools
  slug: developer-tools
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Mes astuces préférées pour les outils de développement Chrome
seo_desc: 'By Dor Shinar

  Chrome Developer Tools are a super powerful suite of tools for developing web applications.
  They can do so much, from very basic operations like traversing the DOM, to checking
  out network requests or even profiling your application''s p...'
---

Par Dor Shinar

Les outils de développement Chrome sont une suite d'outils extrêmement puissante pour le développement d'applications web. Ils permettent de faire tant de choses, des opérations très basiques comme la navigation dans le DOM, à l'inspection des requêtes réseau ou même au profilage des performances de votre application.

Parmi les grandes fonctionnalités qu'ils offrent au quotidien, il y a pas mal de pépites à découvrir si l'on creuse suffisamment. Des fonctionnalités qui peuvent vous faire économiser un clic ou deux – et n'est-ce pas ce que nous recherchons tous ici ?

## Requêtes DOM style jQuery dans la console

jQuery est génial. Il a régné sur le web pendant plus d'une décennie, et certaines statistiques indiquent que [plus de 70 % des pages web les plus populaires au monde](https://en.wikipedia.org/wiki/JQuery#Popularity) exécutent une version de jQuery. C'est fou pour une bibliothèque qui remonte à 2006.

L'API la plus populaire fournie par jQuery est le `$`, utilisé pour sélectionner des éléments DOM. La console des outils de développement Chrome vous permet d'utiliser ce sélecteur `$`, et plus encore. Sous le capot, `$` est un alias pour `document.querySelector()`.

Par exemple, si vous souhaitez simuler un clic sur un élément, vous pouvez faire :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/--selector.png)
_Utilisation du sélecteur $ pour cliquer sur un bouton_

De même, `$$` est un alias pour `document.querySelectorAll()` :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/---selector.png)
_Utilisation du sélecteur $$ pour imprimer les noms de classe_

Il y a encore quelques astuces dans la manche du `$`. Parfois, un sélecteur peut être trop compliqué à écrire de mémoire, ou vous ne connaissez tout simplement pas un sélecteur suffisamment spécifique. Si vous sélectionnez un élément dans l'onglet Éléments, vous pouvez le récupérer avec la variable `$0` dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/-0-selector.gif)
_Un gif montrant l'utilisation du sélecteur $0 dans la console_

La console va encore plus loin, en nous permettant d'accéder non seulement à la dernière sélection, mais aux cinq dernières, dans l'ordre. Les sélections sont exposées via les variables `$0` - `$4` :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/-0-4-selector.gif)
_Un gif montrant l'utilisation du sélecteur $0 - $4 dans la console_

## Copier les propriétés d'un élément

L'onglet Éléments est vraiment utile. Il stocke l'arborescence DOM de notre site web, il nous permet de voir le CSS appliqué à chaque élément, et nous pouvons apporter des modifications aux éléments à la volée depuis celui-ci.

Une astuce vraiment cool que j'ai découverte est la possibilité de copier les propriétés d'un élément (et pas seulement les propriétés) depuis le menu contextuel.

Par exemple, vous pouvez copier le sélecteur d'un élément :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/copy-selector.gif)
_Un gif montrant comment copier le sélecteur d'un élément_

Ce sélecteur peut ne pas être suffisamment spécifique, ou trop spécifique pour la production, mais il devrait faciliter un peu votre vie lors du débogage.

Comme vous pouvez le voir dans le gif précédent, le menu contextuel de copie cache quelques autres choses utiles que vous pouvez copier. Vous pouvez copier les styles de l'élément, le chemin JS (`document.querySelector(SELECTOR)`) ou le XPath.

## Filtrer les requêtes réseau

Parfois, vous travaillez sur une page qui a beaucoup de requêtes. Je veux dire, BEAUCOUP.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/lots-of-requests.gif)
_Faire défiler une très longue liste de requêtes réseau_

Travailler à travers toutes ces requêtes peut être difficile lorsque vous cherchez quelque chose de spécifique. Heureusement, vous pouvez très facilement filtrer les requêtes.

La barre de filtres dispose de bascules rapides pour divers types de requêtes, telles que XHR/Fetch, feuilles de style, scripts JS, images et plus encore :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/toolbar-filters.gif)
_Utilisation des filtres de la barre d'outils pour filtrer les requêtes réseau_

Si vous devez être encore plus spécifique, ou pour que vous puissiez trouver plus rapidement, vous pouvez simplement écrire un critère de filtre dans l'entrée `filter` juste au-dessus de la barre d'outils pour rechercher dans les noms des requêtes :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/filter-by-name.gif)
_Filtrer les requêtes réseau par nom_

## Émuler différentes vitesses de réseau

En utilisant à nouveau l'onglet `Network`, nous pouvons tester notre site avec différentes vitesses d'internet. Le préréglage par défaut est `online`, et vous profiterez de la pleine bande passante de votre connexion internet.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/network-speed-menu.png)
_Un menu permettant la sélection de diverses vitesses d'internet_

Outre `online`, il y a quelques autres préréglages disponibles : `Fast 3G`, `Slow 3G` et `offline`, qui varient en vitesse de téléchargement, vitesse de téléversement et latence. Si vous devez émuler une vitesse différente, plus exotique, vous pouvez ajouter votre propre profil via le bouton `Add...` :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/custom-throttling-profile.png)
_Ajout d'un profil de limitation personnalisé_

## Utiliser les expressions en direct dans la console

Qu'est-ce que les `Live Expressions` ?

Les `Live Expressions` sont des expressions qui s'évaluent constamment en haut de votre console. Supposons que vous souhaitiez suivre la valeur d'une variable au fil du temps. Vous pouvez la journaliser encore et encore :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/print-over-and-over.png)
_Impimer une variable encore et encore_

Avec les `Live Expressions`, vous pouvez vous concentrer sur votre code et laisser Chrome faire le suivi :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/live-expression.gif)
_Stocker une variable dans une expression en direct_

Cela s'applique aux variables définies à la fois dans la console et dans un script.

## Émuler différents appareils

Ceux d'entre nous qui travaillent sur des applications réactives connaissent le sentiment où vous travaillez très dur pour créer une belle mise en page, seulement pour la voir mal se comporter sur des appareils avec différentes résolutions.

Je ne suis pas ici pour vous parler des media queries, mais plutôt d'une manière pratique de tester qu'elles fonctionnent.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/dev-tools-topbar.png)
_Un bouton pour basculer vers la vue appareil_

Lorsque vous cliquez sur le bouton qui ressemble à une tablette et un téléphone, vous verrez que la fenêtre d'affichage de votre navigateur change pour refléter les dimensions d'un autre appareil.

Vous pouvez choisir un appareil parmi une liste de préréglages contenant divers appareils populaires, tels que l'iPhone X, l'iPad Pro, le Pixel 2, le Pixel 2 XL et plus encore. La liste est admettons un peu obsolète, mais je pense qu'elle est suffisamment bonne pour la plupart des cas.

Si vous ne trouvez pas d'appareil qui correspond à vos besoins, vous pouvez définir une résolution personnalisée. Comme vous pouvez le voir, j'ai défini une résolution personnalisée pour émuler un OnePlus 6 (qui est mon appareil quotidien).

![Image](https://www.freecodecamp.org/news/content/images/2020/02/oneplus-6.png)
_Appareil simulé OnePlus 6_

## Forcer l'état d'un élément

Avez-vous déjà été confronté à une situation où vous vouliez jouer avec le CSS spécifique à `:hover` d'un élément, mais chaque fois que vous déplaciez votre souris vers la section des styles dans les outils de développement, l'élément n'était plus survolé ?

Eh bien, les outils de développement Chrome exposent une manière agréable de verrouiller l'état d'un élément, afin que vous puissiez manipuler ses propriétés en paix. De cette manière, vous pouvez rapidement basculer les propriétés `:active`, `:hover`, `:focus`, `:focus-within` et `:visited` d'un élément :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/toggle-state.png)
_Un menu pour basculer l'état d'un élément_

Ce sont mes astuces et conseils que je pense que tout le monde peut utiliser. Merci d'avoir lu !

Cet article a été précédemment publié sur mon blog : [dorshinar.me](https://dorshinar.me/themes-using-css-variables-and-react-context). Si vous souhaitez lire plus de contenu, vous pouvez consulter mon blog, cela me ferait très plaisir.

Si vous souhaitez me soutenir, vous pouvez <a href='https://ko-fi.com/L3L116P44' target='_blank'><img height='36' style='left:0;border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi4.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>