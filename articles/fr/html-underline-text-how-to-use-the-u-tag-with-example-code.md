---
title: Texte souligné en HTML – Comment utiliser la balise <u> avec des exemples de
  code
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-07-20T22:48:13.000Z'
originalURL: https://freecodecamp.org/news/html-underline-text-how-to-use-the-u-tag-with-example-code
coverImage: https://cdn-media-2.freecodecamp.org/w1280/605301d528094f59be257c67.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: HTML5
  slug: html5
seo_title: Texte souligné en HTML – Comment utiliser la balise <u> avec des exemples
  de code
seo_desc: "In this article, we are going to learn about the <u> tag and when it is\
  \ appropriate to use it in HTML 5. \nIn older versions of HTML, you'd use this tag\
  \ as a way to underline text. We are going to learn about the new HTML 5 definition\
  \ and ways to unde..."
---

Dans cet article, nous allons apprendre à connaître la balise `<u>` et quand il est approprié de l'utiliser en HTML 5.

Dans les anciennes versions de HTML, vous utilisiez cette balise pour souligner du texte. Nous allons apprendre la nouvelle définition en HTML 5 et les moyens de souligner du texte en utilisant CSS.

## Qu'est-ce que la balise <u> ?

La balise `<u>` signifie « Unarticulated Annotation element » (élément d'annotation non articulée). Cet élément est une portion de texte en ligne qui semble stylistiquement différente du texte environnant mais qui possède une annotation non textuelle.

Le style par défaut pour cet élément est un soulignement simple.

Examinons quelques exemples de quand utiliser la balise `<u>`.

### Comment utiliser la balise <u> pour les mots mal orthographiés

Une utilisation courante de cette balise est de signaler les mots mal orthographiés.

```html
<p>J'étais assis en <u>orcestra</u> pratique et le chef d'orchestre était en colère parce que nous <u>didt</u> pas pratiquer nos parties.</p>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-20-at-2.45.43-PM.png)

Vous pouvez également utiliser la balise `<u>` si vous souhaitez marquer du texte chinois comme une marque de nom propre. Selon Wikipedia,

> une **marque de nom propre** ([Chinois simplifié](https://en.wikipedia.org/wiki/Simplified_Chinese): 专名号, zhuānmínghào; [Chinois traditionnel](https://en.wikipedia.org/wiki/Traditional_Chinese): 專名號) est un [soulignement](https://en.wikipedia.org/wiki/Underline) utilisé pour marquer les [noms propres](https://en.wikipedia.org/wiki/Proper_name), tels que les noms de [personnes](https://en.wikipedia.org/wiki/Chinese_name), de [lieux](https://en.wikipedia.org/wiki/Place_name), de [dynasties](https://en.wikipedia.org/wiki/Chinese_dynasties), d'organisations.

```html
<p>Voici un exemple de marque de nom propre : <u>书名号</u></p>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-20-at-1.28.22-AM.png)

## Comment utiliser CSS pour changer le style de la balise <u>

Si vous souhaitez signaler un texte mal orthographié, vous pouvez styliser la balise `<u>` avec une ligne rouge ondulée en dessous.

```html
<p>Cette phrase contient tellement de <u class="spelling">fautes</u> d'orthographe <u class="spelling">errrrors</u>.</p>
```

```css
body {
  font-family: Verdana, sans-serif;
}
u.spelling {
  text-decoration: red wavy underline;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-20-at-1.36.15-AM.png)

## Éviter d'utiliser la balise <u> à des fins de style

Dans les versions antérieures de HTML, il était approprié d'utiliser la balise `<u>` strictement pour styliser du texte avec un soulignement. Mais en HTML 5, la balise `<u>` a une signification sémantique et vous devriez utiliser CSS pour styliser votre texte avec un soulignement.

```html
<span class="underline">Ce texte a été stylisé avec CSS.</span>
```

```css
.underline {
  text-decoration: underline;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-20-at-1.50.19-AM.png)

## Ne pas utiliser la balise <u> pour les titres de livres

Si vous faites référence à un titre de livre, vous devriez utiliser la balise `<cite>`. Le style par défaut est en italique, mais vous pouvez remplacer ces styles en utilisant CSS.

```html
<p>J'ai aimé lire <cite>The Great Gatsby</cite> au lycée.</p>
```

```css
cite {
  font-style: normal;
  text-decoration: underline;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-20-at-2.11.30-AM.png)

## Conclusion

La balise `<u>` est un élément sémantique qui ne devrait être utilisé que dans des cas très spécifiques. Si vous souhaitez signaler des erreurs d'orthographe dans le texte, vous pouvez utiliser la balise `<u>`.

Un exemple moins courant serait d'utiliser la balise pour les marques de noms propres en chinois.

Vous ne devriez jamais utiliser la balise `<u>` à des fins de style. À la place, vous devriez utiliser `text-decoration:underline;` dans votre CSS.

Lorsque vous travaillez sur un projet, il est important d'apprendre l'utilisation correcte des éléments HTML 5 afin de les utiliser de la manière appropriée.