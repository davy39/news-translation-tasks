---
title: Comment activer le mode sombre avec CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-09T22:04:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-dark-mode-working-with-css-740ad31e22e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Y2utWiZeebjS3t5ofXLZPA.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: CSS
  slug: css
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment activer le mode sombre avec CSS
seo_desc: 'By Frank Lämmer

  I have been playing around with MacOS Mojave’s dark mode lately. It’s not 100% pleasing
  to my eyes, yet. But it’s especially useful when nerding out at night time with
  little ambient light.

  Dark mode is a design trend. Many reading ap...'
---

Par Frank Lämmer

J'ai récemment exploré le mode sombre de MacOS Mojave. Il n'est pas encore parfait pour mes yeux, mais il est particulièrement utile pour travailler la nuit avec peu de lumière ambiante.

**Le mode sombre est une tendance en design.** De nombreuses applications de lecture (Medium App, Twitter, etc.) l'ont déjà adopté. Il ne s'agit pas seulement d'inverser toutes les couleurs, mais aussi de direction artistique.

![Image](https://cdn-media-1.freecodecamp.org/images/7MXofS94AfNVI-oYG-rNDkZ9WH8i-PvyNcUB)
_Sous macOS Mojave, vous pouvez passer votre interface en mode sombre. Safari et Firefox le supportent déjà._

#### Tout n'est pas sombre (encore)

Une chose qui peut être un peu choquante lorsque l'on travaille en mode sombre est l'éclat de lumière lors de l'ouverture d'un document avec un grand fond blanc. Cet article explore comment gérer le mode sombre sur le web et le styliser avec CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/6vFnrxWHWhxykOVOCl6-jcsMpypqSQpbeNAf)
_L'auteur ouvrant cet article Medium en mode sombre avec peu de lumière ambiante._

### Gérer les paramètres utilisateur du mode sombre

Ne serait-il pas agréable que les documents et les sites web respectent le thème environnemental actuel ?

#### Conversion automatique des couleurs ?

Au moins Safari et Firefox ont déjà un « mode lecteur » avec support pour du texte clair sur fond sombre. Ici, le contexte <article> est rendu en utilisant des styles personnalisés pour une meilleure lisibilité et en supprimant le désordre, et il y a un paramètre pour inverser les couleurs. En s'appuyant sur cela, les navigateurs pourraient inverser automatiquement les sites web avec des styles intelligents. Cela semble effrayant ! Mais au moins Apple Mail le fait déjà. Il inverse même les couleurs pour certains emails HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/kSO148kZlhL9q5FvYT-08ooWX2eZXys6f4jI)
_OMG toutes les couleurs inversées dans un email HTML dans Apple Mail, macOS Mojave_

L'inversion intelligente des couleurs peut être une solution, ou non. Que faire d'autre ?

#### La requête média à la rescousse !

Je ne suis pas seul. Le mode sombre pour CSS est actuellement (août 2018) [**en discussion** dans les « CSS Working Group Editor Drafts »](https://github.com/w3c/csswg-drafts/issues/2735). L'idée est de rendre cela disponible sous forme de requête média. [Quelque chose](https://bugs.webkit.org/show_bug.cgi?id=186606) a déjà été implémenté dans Safari ([privé](https://twitter.com/rmondello/status/1007400236514504706)), voir aussi [ici](https://github.com/WebKit/webkit/commit/46198bd7636f0d1f85e36d830fd3108707d4c169).

En théorie, vous pouvez faire ceci :

```
@media (prefers-color-scheme: dark) {   color: white;   background: black}
```

Attendons que tous les navigateurs soient prêts. Je pense qu'il reste du chemin à parcourir pour la standardisation. Les fabricants de systèmes d'exploitation doivent peut-être aussi se mettre d'accord sur quelque chose.

### Inversé n'est pas le mode sombre

![Image](https://cdn-media-1.freecodecamp.org/images/K33cTogRj84FtU2LvVq19-VIXMpLli8sEFEs)
_Fait amusant : Vous pouvez aussi inverser les couleurs en mode sombre._

Le saviez-vous : Il existe déjà une [fonctionnalité média pour les "couleurs inversées"](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/inverted-colors) dans les Media Queries Level 4. Ce n'est pas la même chose que le mode sombre. Une sorte de "mode sombre" existe depuis un certain temps. Windows a aussi un mode **Contraste élevé**. Il existe de nombreuses variantes.

Néanmoins, ce serait vraiment cool si les auteurs de sites web pouvaient décider comment gérer cela lorsqu'un utilisateur avec le mode "sombre" activé visite leur site. Ainsi, en tant que designer, vous avez un contrôle total sur l'apparence de votre site web en "mode éteint". Beaucoup plus de travail pour vous ? Non, c'est facile. Continuez votre lecture.

### Le mode incognito n'est pas le mode sombre

![Image](https://cdn-media-1.freecodecamp.org/images/C6PA7T3Uj9e0HnFtBfltKMnXvOwLfhS-kVar)
_Ce n'est PAS le mode sombre !_

Lors de l'ouverture d'une fenêtre de navigation privée, de nombreux navigateurs présentent une interface sombre pour souligner la différence. Ce n'est pas non plus le mode sombre, mais c'est sombre.

### Utiliser les variables CSS pour le thème du mode sombre

Grâce aux "propriétés personnalisées CSS" (également connues sous le nom de "variables CSS"), nous pouvons maintenant créer des thèmes plus facilement que jamais avec très peu de CSS. Le thème d'inversion le plus simple :

```
:root {  --text-color: DarkBlue;  --back-color: Azure;}
```

```
body { color: var(--text-color); background: var(--back-color)}
```

```
@media (prefers-dark-interface) {  :root {   --text-color: Azure;   --back-color: DarkBlue;  } }
```

Plug sans vergogne : Mon (nouveau et génial) framework CSS Teutonic CSS utilise déjà cette simple inversion :

![Image](https://cdn-media-1.freecodecamp.org/images/2oe6YHeKR513YrwBo3gSPRqppu46nE27OEFj)
_Ajoutez "inverted" sur le conteneur extérieur pour inverser toutes les couleurs via les variables CSS. Voir en action [ici](https://teutonic.co/examples/colors#inverted" rel="noopener" target="_blank" title=")._

### Sites web changeant l'interface du navigateur

Cet article parle de la façon dont un paramètre utilisateur peut changer l'apparence d'un site web. Cela fonctionne aussi dans l'autre sens : un site web peut changer l'apparence du navigateur. Il existe quelques balises meta propriétaires, disponibles pour l'instant uniquement pour les navigateurs mobiles :

```
<meta name="theme-color" content="black"><meta name="msapplication-navbutton-color" content="black"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black">
```

_ARGH !_

### Lectures complémentaires

L'article « [**OS : High Contrast versus Inverted Colors**](http://adrianroselli.com/2017/11/os-high-contrast-versus-inverted-colors.html) » d'Adrian Roselli discute des différences entre « inversé » et « contraste élevé » dans Windows et macOS.

L'article « [**How “invert brightness” can improve accessibility and help us use our devices**](https://developer.paciellogroup.com/blog/2017/12/how-invert-brightness-can-improve-accessibility-and-help-us-use-our-devices/) » de Matthew Atkinson discute de la façon dont l'inversion des couleurs aide à l'expérience utilisateur. Vous pouvez également y trouver le concept d'inversion « intelligente » des couleurs.

### Résumé

![Image](https://cdn-media-1.freecodecamp.org/images/hNpXvSYGCgpEBw1FoDrNj0bKDeNCiEAQ1umU)
_Un commutateur jour/nuit sur les pages des développeurs Microsoft. Joli détail : ce paramètre est persistant (localstorage ou cookie)._

Le bon côté des standards, c'est qu'il y en a tant à choisir.

Alors que le « mode nuit » est définitivement une tendance, différentes implémentations circulent. Faites entendre votre voix pour en faire UN standard web. Rendez votre CSS compatible pour pouvoir le supporter sans trop de tracas.