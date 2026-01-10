---
title: Tutoriel HTML sur les italiques – Comment mettre du texte en italique avec
  la balise <i>
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-03-22T23:21:42.000Z'
originalURL: https://freecodecamp.org/news/html-italics-tutorial-how-to-make-text-italic-with-the-i-tag
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6053020b28094f59be257c71.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: style
  slug: style
- name: Web Development
  slug: web-development
seo_title: Tutoriel HTML sur les italiques – Comment mettre du texte en italique avec
  la balise <i>
seo_desc: "In this article, we are going to learn about how to use the <i> tag and\
  \ how it differs from the <em> tag. \nIn previous versions of HTML, the <i> tag\
  \ was used to display text in italics. But in HTML 5, the definition has changed.\
  \ We are going to explo..."
---

Dans cet article, nous allons apprendre à utiliser la balise `<i>` et en quoi elle diffère de la balise `<em>`.

Dans les versions précédentes de HTML, la balise `<i>` était utilisée pour afficher du texte en italique. Mais dans HTML 5, la définition a changé. Nous allons explorer cette nouvelle définition et apprendre d'autres façons de styliser du texte en italique en utilisant CSS.  

## Qu'est-ce que la balise <i> ? 

La balise `<i>`, ou élément de texte idiomatique, est une portion de texte qui représente un changement d'humeur ou de qualité du texte. Ce texte est affiché en italique. 

Examinons quelques raisons pour lesquelles vous pourriez vouloir utiliser la balise `<i>`.  

### Utilisation de la balise <i> pour marquer des phrases dans une autre langue

Vous pouvez utiliser la balise `<i>` pour marquer une portion de texte dans une autre langue. Cet exemple met en italique une phrase latine.  

```html
<p>Stacy vient de se faire tatouer la phrase <i>Audentes fortuna iuvat</i> qui signifie "La fortune sourit aux audacieux".</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/latin-phrase-tattoo.png)

Vous pouvez également utiliser l'attribut `lang` dans la balise `<i>` pour représenter des phrases qui sont dans une langue différente de leur texte environnant. 

```html
<p>La première phrase que Matt a apprise en italien est <i lang="it">Vorrei una birra</i>, ce qui se traduit par "Je voudrais une bière".</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/lang-atrribute.png)

### Utilisation de la balise <i> pour montrer les pensées de quelqu'un

Vous pouvez également utiliser la balise `<i>` pour mettre en évidence les pensées intérieures d'une personne. 

```html
<p>Après que Ben ait rencontré les parents de sa petite amie, il se dit à lui-même, <i>J'espère vraiment qu'ils m'ont aimé</i>.</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/ben-story.png)

### Utilisation de la balise <i> pour le nom d'un navire

Si vous souhaitez utiliser le nom d'un navire, vous pouvez envelopper ce nom dans des balises `<i>`. 

```html
<p>Le <i>USS Arizona</i> était un cuirassé de la marine américaine construit dans les années 1910.</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/uss-arizona.png)

### Utilisation de la balise <i> pour les descriptions taxonomiques

Selon la [Convention sur la diversité biologique](https://www.cbd.int/gti/taxonomy.shtml),

> La taxonomie est la science de la nomenclature, de la description et de la classification des organismes et inclut toutes les plantes, animaux et micro-organismes du monde. 

Voici un exemple d'utilisation de la balise `<i>` pour le terme _Felis catus_. 

```html
<p>Un autre terme pour le chat domestique serait <i>Felis catus</i>.</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/cat-term.png)

## **Différences entre la balise <i> et la balise <em> en HTML**

Vous pourriez penser que les balises `<i>` et `<em>` ont la même signification parce qu'elles apparaissent de la même manière dans le navigateur. Mais les deux balises ont des significations différentes l'une de l'autre. 

La balise `<em>`, ou élément d'emphase, doit être utilisée lorsque vous souhaitez mettre l'accent sur un mot ou une portion de texte. 

Voici un exemple utilisant la balise `<em>`.

```html
 <p>Arrête de faire l'enfant et <em>fais</em>-le déjà !</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/em-example.png)

Les humains et les lecteurs d'écran placeraient un accent verbal sur le mot "fais". Cela diffère de la balise `<i>` où il n'y avait pas d'emphase supplémentaire placée sur le texte. 

## Devriez-vous utiliser la balise <i> pour le style ? 

Vous ne devriez pas utiliser la balise `<i>` à des fins de style. Si vous souhaitez styliser du texte en italique, vous devriez utiliser la propriété CSS `font-style`. 

```html
<p class="demo-para">J'utilise CSS pour styliser ce texte en italique.</p>

```

```css
.demo-para {
  font-style: italic;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/css-italics.png)

## Devriez-vous utiliser la balise <i> ou <span> pour les icônes ?

Au fil des ans, il y a eu un débat sur le fait de savoir s'il est "correct" d'utiliser des balises `<i>` ou `<span>` pour ajouter des icônes à votre site web. 

Certains soutiendront qu'il n'y a rien de mal à cela et que c'est une pratique assez courante, tandis que d'autres pensent que c'est un mauvais usage de la balise `<i>` et que vous devriez utiliser la balise `<span>` à la place. 

Voici une réponse de [Font Awesome](https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use) concernant l'utilisation de la balise `<i>` pour ses icônes :

> Nous aimons la balise `<i>` pour sa brièveté et parce que la plupart des gens utilisent `<em></em>` pour le texte sémantique mis en emphase/italique de nos jours. Si ce n'est pas votre tasse de thé, utiliser un `<span>` est plus sémantiquement correct.

Mon objectif n'est pas de vous faire choisir un côté plutôt qu'un autre dans ce débat, mais plutôt de vous faire prendre conscience de cette discussion en cours. 

## Conclusion

La balise `<i>` est une portion de texte qui représente un changement d'humeur ou de qualité du texte. Si vous souhaitez mettre l'accent sur du texte, la balise appropriée serait alors la balise `<em>`.

La balise `<i>` ne doit pas être utilisée à des fins de style. La bonne façon de styliser du texte en italique est d'utiliser la propriété CSS `font-style`.

J'espère que vous avez apprécié cet article et appris quand utiliser la balise `<i>`.