---
title: Comment exploiter la puissance de l'Inspecteur Web moderne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-14T22:15:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-leverage-the-power-of-the-modern-web-inspector-b94dd85e1917
coverImage: https://cdn-media-1.freecodecamp.org/images/1*llEGsvQxvCsOvzSvxkdHNg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment exploiter la puissance de l'Inspecteur Web moderne
seo_desc: 'By Craig Fitzpatrick

  The little, handy beast (aka the Web Inspector) has certainly come a long way since
  the days of “view source”!

  For those of you who are too young to remember — back in the prehistoric days of
  website development, the “view source...'
---

Par Craig Fitzpatrick

La petite bête pratique (alias l'Inspecteur Web) a certainement parcouru un long chemin depuis les jours de « view source » !

Pour ceux d'entre vous qui sont trop jeunes pour se souvenir — à l'époque préhistorique du développement web, la commande « view source » ouvrait simplement le HTML d'une page dans le Bloc-notes de Windows. Ce n'était pas génial.

![Image](https://cdn-media-1.freecodecamp.org/images/Z315UwxriuUc1bIFJZBKuOL9GMrnnVNsA3NG)

![Image](https://cdn-media-1.freecodecamp.org/images/9HzsRSz98dsHAIyxljAA7MEmuPG81wOlLaLq)

Aujourd'hui, nous avons...

...des règles CSS modifiables avec des sélecteurs de couleurs intégrés...

![Image](https://cdn-media-1.freecodecamp.org/images/huO9Eg2fuA3IfS1hnziYbgTJpBjzAL2nbbHZ)

...la possibilité de modifier les valeurs de pixels avec votre clavier, provoquant un mouvement en temps réel de votre contenu...

![Image](https://cdn-media-1.freecodecamp.org/images/vtVRPpwtF0GAW6ROWFWHAPDgRm9V4d0nfiMA)

...et la plus grande invention de toutes : le « look-ahead », qui complète automatiquement les noms et valeurs CSS au fur et à mesure que vous tapez. Cela vous fait économiser des heures de temps de débogage causé par votre propre orthographe horrible :

![Image](https://cdn-media-1.freecodecamp.org/images/7WQBILjFGLGLxGqSFU-vATjY8yRs5dffoGJW)

De nombreux développeurs n'ont même pas découvert tous les petits éléments d'émerveillement intégrés dans la plupart des Inspecteurs Web.

Par exemple, **saviez-vous** que vous pouvez construire une page HTML entière dans l'Inspecteur ?

Ouvrez simplement un nouvel onglet et l'Inspecteur (vous verrez probablement une page de recherche Google ou autre chose comme page par défaut) et commencez à supprimer des nœuds directement depuis l'inspecteur de DOM. Une fois que vous êtes réduit au nœud HTML, faites un clic droit et choisissez MODIFIER EN TANT QUE HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/GSt70yFCJfH3HgGtGNNf4i1NM63KCaOu1hep)

Construisez votre page à partir de zéro avec un aperçu automatique et en temps réel de votre travail dans le cadre du navigateur ci-dessus ! Vous pouvez même glisser-déposer des nœuds HTML à l'intérieur de l'Inspecteur pour déplacer les éléments.

Ne me lancez même pas sur la façon dont la console JavaScript est incroyable pour inspecter la mémoire, parcourir la pile, et plus encore.

C'est une belle journée pour être un développeur web !

### Mais

Mais il y a un petit hic. L'enregistrement de votre travail n'a été rendu disponible que [récemmement, et c'est un peu compliqué](https://youtu.be/wz1Sy5C039M?t=6m17s)... Vous devez :

* ouvrir le navigateur et sélectionner les remplacements
* activer les remplacements locaux
* faire un clic droit sur le fichier CSS et enregistrer pour les remplacements

Bien sûr... Il y a ici une technologie assez puissante, mais comment obtenez-vous rapidement vos modifications sur votre site de production ? Ugh. Si proche de la perfection !

### PageCloud

Lorsque j'écrivais la première version de [PageCloud](https://www.pagecloud.com), c'était l'une des choses qui me préoccupaient.

Même si PageCloud est un constructeur de sites web visuel qui aide les non-techniciens à construire des pages web, je me suis dit : l'inspecteur de DOM est un outil si puissant, ne serait-ce pas génial si vous pouviez simplement faire quelques modifications et les envoyer immédiatement dans le cloud ?

Et ainsi, je me suis lancé dans une mission pour donner aux développeurs la possibilité d'utiliser l'Inspecteur Web pour modifier un site de production.

Cependant, la seule façon d'y parvenir était de faire un pas en arrière et de repenser la façon dont les pages web sont construites, gérées et servies.

![Image](https://cdn-media-1.freecodecamp.org/images/fJOKYJXQW7npJiN5Mlux5ngsBWH2QQGf27x5)

Il y avait tout un tas de défis techniques en cours de route, comme les serveurs d'applications, les modèles, l'imbrication, les bases de données, les caches...

J'ai donc décidé de prendre une page du livre de la publication assistée par ordinateur. L'idée était simple : vous lancez une application pour pouvoir lire, modifier et créer des documents. Une fois que vous cliquez sur Enregistrer, toutes vos modifications sont conservées.

Je me suis donc demandé :

> Et si nous considérions simplement les pages web comme des documents ?

Je ne vous ennuyerai pas avec les luttes pour faire fonctionner cela (et les plusieurs bouteilles de vin qui ont aidé à apaiser la douleur), mais cette idée initiale a été la fondation de tout ce que PageCloud est aujourd'hui. Et, jusqu'à présent, nous sommes les seuls à l'avoir fait.

En développant ce concept, nous avons pu permettre aux utilisateurs d'interagir avec le web de la même manière que vous le feriez avec vos applications de bureau : comme copier/coller depuis le presse-papiers, superposer, redimensionner et déplacer librement des objets sur la page.

Cette même idée nous a permis de nous intégrer avec l'Inspecteur Web, permettant aux utilisateurs de modifier n'importe quoi, de cliquer sur Enregistrer, et d'avoir terminé.

Voici un exemple rapide :

![Image](https://cdn-media-1.freecodecamp.org/images/tCpOmzM9SMCBJfPnTlZKBo7ZewNNZ7uFvF6r)

En exploitant toute la beauté de l'Inspecteur Web moderne, vous pouvez : modifier le HTML, le CSS, et créer des liens vers des CSS et JS externes. Vous pouvez même exécuter des commandes dans la console JavaScript pour modifier le DOM !

Tous les moyens par lesquels vous pouvez modifier ce DOM sont acceptables. Lorsque vous cliquez sur « ENREGISTRER », toutes vos modifications sont conservées et renvoyées dans le cloud — car votre page est un document, après tout !

![Image](https://cdn-media-1.freecodecamp.org/images/9Zwy1AALskP8H9q8hJnGROEAPL5FVaTwpjzO)

Grâce à la magie de l'inspecteur web, vous pouvez même copier des nœuds d'une fenêtre de navigateur et les coller dans le DOM d'une autre page.

Oui, nous sommes ambitieux. Mais nous croyons que cette nouvelle façon de penser permettra à PageCloud de devenir le premier outil à répondre aux besoins du designer visuel, tout en maintenant un accès sans restriction pour les développeurs.

Peut-être qu'un jour dans un avenir pas si lointain, « Inspecter » sera remplacé par une interface conviviale, et rejoindra « view source » dans les rangs des outils obsolètes. C'est-à-dire, si PageCloud a quelque chose à voir avec cela !