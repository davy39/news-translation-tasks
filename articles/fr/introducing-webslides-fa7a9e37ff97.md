---
title: Présentation de WebSlides
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-09T10:28:22.000Z'
originalURL: https://freecodecamp.org/news/introducing-webslides-fa7a9e37ff97
coverImage: https://cdn-media-1.freecodecamp.org/images/1*v1zc80z1gh6n9eKrDNZF9A.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: open source
  slug: open-source
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: Présentation de WebSlides
seo_desc: 'By José Luis Antúnez

  Everyone loves stories. People share content that makes them feel inspired. We need
  stories to know we’re not alone.

  Slide decks are an excellent way to tell these stories. And there are already plenty
  of great tools out there fo...'
---

Par José Luis Antúnez

Tout le monde aime les histoires. Les gens partagent du contenu qui les inspire. Nous avons besoin d'histoires pour savoir que nous ne sommes pas seuls.

Les diapositives sont un excellent moyen de raconter ces histoires. Et il existe déjà de nombreux outils pour cela, comme Powerpoint et Keynote.

Mais personne n'aime les présentations HTML. Littéralement, personne. « J'adore les présentations HTML » retourne [zéro résultat](https://www.google.es/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#newwindow=1&q=%22I+love+HTML+presentations%22&search_plus_one=form) dans la recherche Google. ?

Je suis designer et développeur, et je travaille toute la journée sur la plateforme géante qu'est le web. Il m'a toujours semblé étrange et dépassé de devoir lancer un programme séparé sur mon ordinateur et utiliser Powerpoint et Keynote — avec leurs formats propriétaires étranges — puis de devoir l'envoyer par email à quelqu'un.

J'ai donc créé [WebSlides](https://webslides.tv).

WebSlides est tout au sujet de **raconter une histoire, puis de la partager de manière belle** : hypertexte, balisage propre et CSS élégant comme éléments narratifs.

![Image](https://cdn-media-1.freecodecamp.org/images/WNgHPuzDIzudaRmfUGlM-7M8p9LWZQkFuCN7)

Concevoir dans WebSlides peut être aussi rapide qu'avec Powerpoint. Vous pouvez vous en sortir avec une compréhension de base de HTML et CSS. Il suffit de choisir une [démo](https://webslides.tv/demos) et de la personnaliser en quelques minutes.

Les designers, développeurs, marketeurs et journalistes disposent désormais d'un outil de présentation natif pour le web avec :

* Raccourcis clavier de navigation rapide (et glissement horizontal et vertical).
* Permaliens qui vous emmènent directement à une diapositive spécifique.
* Un compteur de diapositives.
* [+40 composants](https://webslides.tv/demos/components) incluant des couvertures, cartes, citations et formulaires.
* Une grande variété d'arrières-plans : couleurs, dégradés, images et vidéos.
* Blocs flexibles avec remplissage automatique et hauteur égale.
* 500+ icônes SVG grâce à Font Awesome.

![Image](https://cdn-media-1.freecodecamp.org/images/XwUc3TQQQPPG6xrkIbG9pIiQP-R0i2n2yI4m)
_Démos : [Keynote](https://webslides.tv/demos/landings" rel="noopener" target="_blank" title="">Landings</a> · <a href="https://webslides.tv/demos/portfolios" rel="noopener" target="_blank" title="">Portfolios</a> · <a href="https://webslides.tv/demos/keynote" rel="noopener" target="_blank" title=")._

### Poésie du code

Voici un exemple de [code source HTML](https://webslides.tv) qui montre comment cela fonctionne. Ce code est propre, évolutif et bien documenté. Il utilise un balisage intuitif avec des [conventions de nommage populaires](https://webslides.tv/demos/classes). **Il n'est pas nécessaire de surutiliser les classes ou les imbrications.**

Chaque parent `_<section>` dans l'élément #webslides est une diapositive individuelle :

```
<article id="webslides">  <!-- Diapositive 1 -->  <section>    <h1>Design pour la confiance</h1>  </section>  <!-- Diapositive 2 -->  <section class="bg-primary aligncenter">    <div class="wrap">      <h2>.wrap = conteneur 1200px</h2>    </div>  </section></article>
```

### **Concevoir avec intention**

WebSlides est gratuit et [open source](https://github.com/jlantunez/webslides). Je l'ai créé parce que nous avons besoin d'une plateforme pour un storytelling beau et élégant. Voyons ce qui se passe :

* [Medium](https://medium.com) = Beaux articles.
* [Typeform](http://typeform.com) = Beaux formulaires.
* [WebSlides](https://webslides.tv) = Belles présentations et longs formats.

![Image](https://cdn-media-1.freecodecamp.org/images/RYGMgnNiCJN8U5ScGXqiPzFuzncQHH10Paww)
_Démo : [Pourquoi WebSlides ?](https://webslides.tv/demos/why-webslides" rel="noopener" target="_blank" title=") — Bon karma._

Je suis ouvert aux [pull requests pour WebSlides](https://github.com/jlantunez/webslides/issues) afin que nous puissions continuer à améliorer et à développer cet outil.

Veuillez partager cet article avec toute personne susceptible d'être intéressée par cet outil. J'attends avec impatience de lire vos commentaires. N'hésitez pas à [m'envoyer un email](mailto:jlantunez@gmail.com) si vous avez des questions.

_Merci tout particulier à [Luis Sacristán](https://twitter.com/luissacristan) et [Jenn Schiffer](http://twitter.com/jennschiffer) ([SimpleSlides](https://github.com/jennschiffer/SimpleSlides) a été une révélation)._ ? _Vous pouvez également suivre les mises à jour sur [Twitter](https://twitter.com/webslides), [Dribbble](http://dribbble.com/tags/webslides) et [GitHub](https://github.com/jlantunez/webslides)._