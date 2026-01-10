---
title: Style Inline en HTML – Styles CSS Inline
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-08T21:24:31.000Z'
originalURL: https://freecodecamp.org/news/inline-style-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template-1.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: style
  slug: style
seo_title: Style Inline en HTML – Styles CSS Inline
seo_desc: 'Cascading Style Sheets (CSS) is a markup language that determines how your
  web pages will appear. It manages the colors, fonts, and layouts of your website
  elements, as well as allowing you to add effects or animations to your pages.

  We can style an ...'
---

Les feuilles de style en cascade (CSS) sont un langage de balisage qui détermine l'apparence de vos pages web. Il gère les couleurs, les polices et les mises en page des éléments de votre site web, ainsi que vous permettant d'ajouter des effets ou des animations à vos pages.

Nous pouvons styliser un fichier/page HTML de trois manières : le style externe, le style interne et le style inline. Dans cet article, nous nous concentrerons sur le style inline.

## Comment Utiliser le Style Inline en HTML

En utilisant l'attribut style, nous pouvons appliquer un style à notre HTML à l'intérieur des balises HTML individuelles avec le style inline.

```html
<h1 style="...">...</h1>
```

L'attribut style fonctionne de la même manière que tout autre attribut HTML. Nous utilisons `style`, suivi du signe égal (=), puis d'une guillemet où toutes les valeurs de style seront stockées en utilisant les paires propriété-valeur CSS standard - `"propriété: valeur;"`.

**Note :** Nous pouvons avoir autant de paires propriété-valeur que nous le souhaitons, tant que nous les séparons par un point-virgule (;).

Il est à noter que l'attribut `style` est généralement utilisé dans la balise HTML d'ouverture car c'est la partie de l'élément HTML qui peut contenir du texte, des données, une image, ou rien du tout. Un exemple de style inline est le suivant :

```html
<h1 style="color: red; font-size: 40px;">Bonjour le Monde</h1>
```

Cela est similaire à ceci :

```css
h1 {
  color: red;
  font-size: 40px;
}
```

La seule différence est que le style inline ne s'applique qu'à la balise à laquelle il est appliqué, alors que cet exemple de code affecte toutes les balises `p` de votre page HTML.

### Quand Utiliser les Styles Inline

L'utilisation des styles inline n'est pas considérée comme une bonne pratique, car elle entraîne beaucoup de répétitions – car les styles ne peuvent pas être réutilisés ailleurs.

Mais il y a des moments où les styles inline sont la meilleure (ou la seule) option, comme lors du stylage des e-mails HTML, du contenu CMS comme WordPress, Drupal, etc. Vous pouvez également les utiliser lors du stylage de contenu dynamique, qui est créé ou modifié par JavaScript.

À l'exception de la déclaration `!important`, les styles inline ont une [haute spécificité/priorité élevée](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance#Understanding_the_cascade), ce qui signifie qu'ils remplaceront la plupart des autres règles dans les feuilles de style internes et externes.

Supposons que nous avons deux textes de paragraphe avec un style inline défini sur `red` et un style interne défini sur `green` :

```html
<html>
  <head>
      <title>Bonjour le Monde</title>
      <style>
       p {
           color: green;
       }
   </style>
  </head>
 
  <body>
     <p style="color: red;">Le premier paragraphe est rouge.</p>
     <p style="color: red;">Le deuxième paragraphe est également rouge.</p>
  </body>
</html>
```

Le CSS de nos styles inline remplacera le CSS du style interne, donc les deux paragraphes seront `red`.

## Avantages et Inconvénients des Styles Inline

Jusqu'à présent, nous avons appris ce qu'est le style inline et comment l'utiliser dans les balises HTML. Maintenant, examinons les avantages et les inconvénients pour voir quand nous devons utiliser les styles inline et quand nous ne devons pas.

### Avantages du CSS Inline :

* Le style inline prime sur tous les autres styles. Tout style défini dans les feuilles de style internes et externes est remplacé par les styles inline.

* Vous pouvez rapidement et facilement insérer des règles CSS dans une page HTML, ce qui est utile pour tester ou prévisualiser les modifications et effectuer des corrections rapides sur votre site web.

* Il n'est pas nécessaire de créer un fichier supplémentaire.

* Pour appliquer un style en JavaScript, utilisez l'attribut `style`.

### Inconvénients du CSS Inline :

* L'ajout de règles CSS à chaque élément HTML prend du temps et rend votre structure HTML désorganisée. Il est difficile de maintenir, de réutiliser et de mettre à l'échelle.

* La taille et le temps de téléchargement de votre page peuvent être affectés par le stylage de plusieurs éléments.

* Les styles inline ne peuvent pas être utilisés pour styliser les pseudo-éléments et les pseudo-classes. Par exemple, vous pouvez styliser les couleurs visitées, survolées, actives et de lien d'une balise d'ancrage en utilisant des feuilles de style externes et internes.

## Conclusion

Dans cet article, nous avons appris comment utiliser le style inline en HTML, quand l'utiliser, et certains des avantages et inconvénients de le faire.

Étant donné que le style inline prime sur tous les autres styles, l'un des meilleurs moments pour l'utiliser est lors du test ou de la prévisualisation des modifications et de l'exécution de corrections rapides sur votre site web.