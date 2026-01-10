---
title: Un Modèle Spatial pour une Navigation Web Sans Perte
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-29T20:07:23.000Z'
originalURL: https://freecodecamp.org/news/lossless-web-navigation-spatial-model-37f83438201d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*o68S8d3Ui0YaNEftvhqGcg.png
tags:
- name: Design
  slug: design
- name: interaction design
  slug: interaction-design
- name: Product Design
  slug: product-design
- name: UX
  slug: ux
- name: Web Design
  slug: web-design
seo_title: Un Modèle Spatial pour une Navigation Web Sans Perte
seo_desc: 'By Patryk Adaś

  In my last post I described the concept of navigation trails as an evolution of
  the standard tabbed browsing model.

  As a part of the Browser.html project, I’m working on a spatial model through various
  user interactions and animations....'
---

Par Patryk Adaś

Dans [mon dernier article](https://medium.freecodecamp.com/lossless-web-navigation-with-trails-9cd48c0abb56), j'ai décrit le concept de trails de navigation comme une évolution du modèle standard de navigation par onglets.

Dans le cadre du projet [Browser.html](https://github.com/browserhtml), je travaille sur un modèle spatial à travers diverses interactions utilisateur et animations. Cela devrait aider les utilisateurs à mieux comprendre ce qui se passe et comment naviguer sur le web de manière plus efficace.

**Les utilisateurs ont développé certains comportements et attentes sur lesquels nous voulons construire. Au lieu de remplacer les flux de travail existants, nous voulons les améliorer.**

### Mouvement horizontal — revenir en arrière / avancer

![Image](https://cdn-media-1.freecodecamp.org/images/3ESNwAoCmMrfM0qpFBakdOXbVguqT1EcZT9Z)

Lorsque vous rembobinez une cassette ou utilisez un outil de montage vidéo, un modèle d'interaction courant est le mouvement horizontal le long d'une timeline. Les navigateurs utilisent cette approche pour permettre aux utilisateurs de revenir en arrière dans leur historique de navigation. Mais cela ne permet de revenir en arrière qu'à une seule entrée de l'historique à la fois. Des raccourcis existent, mais ils ne permettent pas de _prévisualiser_ les pages passées.

Même avec un historique de navigation conventionnellement perteux, il est courant d'avoir plusieurs entrées pour revenir en arrière ou avancer. L'introduction des trails ne fera qu'augmenter le nombre d'entrées.

**Nous voulons que les utilisateurs puissent sélectionner un point arbitraire dans la timeline en utilisant des interactions familières.**

![Image](https://cdn-media-1.freecodecamp.org/images/AZ6wT4exYyrD-Q2hHnj3va1k7MybmOEjIgpW)
_[Youtube](https://youtu.be/reMbtUWeias" rel="noopener" target="_blank" title=")_

Dans notre conception, un léger tirage (glissement) depuis la gauche permet à l'utilisateur de jeter un coup d'œil à la dernière entrée de l'historique. Tirer plus loin déploie le trail complet et révèle tout l'historique, permettant à l'utilisateur de revenir à un point arbitraire en relâchant sur un site.

![Image](https://cdn-media-1.freecodecamp.org/images/BCVBeORK3UEPK6dA4jGaublELpGNagsjmzZt)
_[Youtube](https://youtu.be/6e0cGYHJoDQ" rel="noopener" target="_blank" title=")_

Tirer au-delà de toutes les entrées passe à une vue d'ensemble des trails, car nous supposons que l'utilisateur voulait passer à un site web différent.

![Image](https://cdn-media-1.freecodecamp.org/images/QfsKjte08TArlZjzpYnPNvCBH87cHwRJH3IL)
_[Youtube](https://youtu.be/uVRWfjceDDg" rel="noopener" target="_blank" title=")_

**Nous voulons fournir des indices visuels dès les premières étapes de la création d'un trail.** Un nouveau site web poussera la page actuelle vers la gauche, devenant le premier de la ligne.

### Mouvement vertical — changer de trail

![Image](https://cdn-media-1.freecodecamp.org/images/2Puh8Ovp-yFr8PjmeRIy1-U25sZ41VpMNfZ4)

Les navigateurs de bureau grand public finissent par surcharger l'axe horizontal comme moyen de changer d'onglets. En revanche, les navigateurs mobiles utilisent l'espace vertical à cette fin.

Cela s'aligne avec l'utilisation de longue date de l'ordre vertical dans les catalogues et comme moyen naturel d'organiser les éléments à faire.

La personne moyenne a tendance à avoir soit moins de huit onglets ouverts, soit à ajouter des onglets sans organisation jusqu'à déclarer une "banqueroute d'onglets" et à recommencer à zéro.

![Image](https://cdn-media-1.freecodecamp.org/images/LxH8tZ2WpsdMwp8LdJU3mBvEuO35KEE0CurF)
_[Youtube](https://youtu.be/QH1sOQXvH-k" rel="noopener" target="_blank" title=")_

Ouvrir un lien en arrière-plan crée un trail qui glisse sous la page actuellement mise en avant, fournissant à nouveau un indice de l'endroit où les nouveaux trails se retrouvent spatialement.

![Image](https://cdn-media-1.freecodecamp.org/images/ZAHOVFdw3s-FdRczvRoFtCFEIg1OtTtO1AQz)
_[Youtube](https://youtu.be/3NxlriMTNnY" rel="noopener" target="_blank" title=")_

Le bas d'une page est un endroit naturel pour fournir un accès facile au trail suivant, qui est commodément accessible en faisant défiler la page jusqu'à la fin.

![Image](https://cdn-media-1.freecodecamp.org/images/Cq-Xk3IPFrRl9WMjB-IIAmBxXRXKt3jZwYqt)
_[Youtube](https://youtu.be/AWpbnV41zUE" rel="noopener" target="_blank" title=")_

Pour que le modèle mental fonctionne, il doit être appliqué à toutes les vues. La vue d'ensemble des trails permet de naviguer dans les trails en utilisant les mêmes gestes horizontaux montrés précédemment et de changer de trails en utilisant des gestes verticaux. Elle fournit une carte de navigation avec accès à tous les trails pris lors de la poursuite d'un sujet spécifique.

### Rejoignez-nous !

Nous travaillons actuellement à la construction de notre premier prototype fonctionnel. Si cela vous semble amusant, consultez le projet [Browser.html](https://github.com/browserhtml/browserhtml) ! Vous pouvez trouver notre liste de [problèmes ouverts](https://github.com/browserhtml/browserhtml/issues) sur GitHub, ou venir discuter avec nous sur notre [Slack](https://browserhtml-slackin.herokuapp.com/).