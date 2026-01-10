---
title: Comment garder votre pied de page où il doit être ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-06T17:13:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gUfDwoSlbdxjXv10Pxnxtw.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment garder votre pied de page où il doit être ?
seo_desc: 'By Dominic Fraser

  A footer is the last element on the page. At a minimum it is at the bottom of the
  viewport, or lower if the page content is taller than the viewport. Simple, right?
  ?

  When working with dynamic content that includes a footer, a probl...'
---

Par Dominic Fraser

Un pied de page est le dernier élément de la page. Au minimum, il se trouve en bas de la fenêtre d'affichage, ou plus bas si le contenu de la page est plus grand que la fenêtre d'affichage. Simple, non ? 💡

Lorsqu'on travaille avec du contenu dynamique qui inclut un pied de page, un problème survient parfois lorsque le contenu d'une page n'est pas suffisant pour la remplir. Le pied de page, au lieu de rester en bas de la page où nous aimerions qu'il soit, remonte et laisse un espace vide en dessous.

Pour une solution rapide, vous pouvez positionner absolument le pied de page en bas de la page. Mais cela comporte son propre inconvénient. Si le contenu devient plus grand que la fenêtre d'affichage, le pied de page restera « collé » en bas de la fenêtre d'affichage, que nous le voulions ou non.

Cela montre le comportement que nous ne voulons pas et celui que nous voulons :

![Image](https://cdn-media-1.freecodecamp.org/images/CmSel82bidnUEBQ5fnl1aWwQlwmj4h2eO0WI)

Examinons une approche pour y parvenir.

#### Garder le contrôle de votre pied de page

`index.html` :

```
<!DOCTYPE html>

<html>
 <head>
   <link rel="stylesheet" type="text/css" href="main.css" />
 </head>

<body>
 <div id="page-container">
   <div id="content-wrap">
     <!-- tout le reste du contenu de la page -->
   </div>
   <footer id="footer"></footer>
 </div>
</body>

</html>
```

`main.css` :

```css
#page-container {
  position: relative;
  min-height: 100vh;
}

#content-wrap {
  padding-bottom: 2.5rem;    /* Hauteur du pied de page */
}

#footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 2.5rem;            /* Hauteur du pied de page */
}
```

Alors, que fait ce code ?

* Le `page-container` englobe tout sur la page et définit sa hauteur minimale à 100 % de la hauteur de la fenêtre d'affichage (`vh`). Comme il est `relative`, ses éléments enfants peuvent être positionnés avec `absolute` par rapport à lui plus tard.
* Le `content-wrap` a un padding inférieur qui correspond à la hauteur du pied de page, garantissant qu'exactement assez d'espace est laissé pour le pied de page à l'intérieur du conteneur dans lequel ils se trouvent tous les deux. Une `div` enveloppante est utilisée ici et contiendrait tout le reste du contenu de la page.
* Le `footer` est défini sur `absolute`, collé au `bottom: 0` du `page-container` dans lequel il se trouve. Cela est important, car il n'est pas `absolute` par rapport à la fenêtre d'affichage, mais descendra si le `page-container` est plus grand que la fenêtre d'affichage. Comme indiqué, sa hauteur, arbitrairement définie à `2.5rem` ici, est utilisée dans le `content-wrap` au-dessus.

Et voilà. Votre pied de page reste maintenant où vous l'attendez !

#### Dernières touches

Bien sûr, c'est du CSS, donc il ne serait pas complet sans quelques [considérations UX spécifiques aux mobiles](https://nicolas-hoizey.com/2015/02/viewport-height-is-taller-than-the-visible-part-of-the-document-in-some-mobile-browsers.html), et [une approche alternative](https://matthewjamestaylor.com/blog/keeping-footers-at-the-bottom-of-the-page) utilisant `min-height: 100%` plutôt que `100vh`. Mais cela a ses propres [inconvénients](https://stackoverflow.com/questions/6654958/make-body-have-100-of-the-browser-height/38908284#38908284).

Flexbox (avec flex-grow) ou Grid peuvent également être utilisés, et sont tous deux très puissants.

La méthode que vous choisissez dépend entièrement de vous et des spécificités de votre design. Espérons que l'exemple ci-dessus et les liens vous aideront à gagner du temps dans votre décision et sa mise en œuvre.

Merci pour votre lecture. Voici quelques autres articles que j'ai écrits récemment :

* [Un guide pour débutants sur le service de conteneurs élastiques d'Amazon](https://medium.freecodecamp.org/amazon-ecs-terms-and-architecture-807d8c4960fd)
* [Tester React avec Jest et Enzyme](https://medium.com/@dfrase/testing-react-with-jest-and-enzyme-20505fec4675)