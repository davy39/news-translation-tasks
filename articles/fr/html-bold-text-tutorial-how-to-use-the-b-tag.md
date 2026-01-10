---
title: Tutoriel sur le texte en gras en HTML – Comment utiliser la balise <b>
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-03-18T23:16:44.000Z'
originalURL: https://freecodecamp.org/news/html-bold-text-tutorial-how-to-use-the-b-tag
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6051c3af28094f59be25734b.jpg
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Tutoriel sur le texte en gras en HTML – Comment utiliser la balise <b>
seo_desc: 'In this article, we are going to learn how to use the <b> tag and how it
  differs from the <strong> tag.

  What is the (bold) tag in HTML?

  The <b> tag is used to to make a portion of the text bold without carrying any special
  importance. Here is an exam...'
---

Dans cet article, nous allons apprendre à utiliser la balise `<b>` et en quoi elle diffère de la balise `<strong>`.

## Qu'est-ce que la balise **<b> (gras) en HTML ?**

**La** balise `<b>` est utilisée pour mettre en gras une portion de texte sans lui donner une importance particulière. Voici un exemple utilisant la balise `<b>`.

```html
<p>Ceci est un exemple de <b>texte en gras.</b></p>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/bold-text.png align="left")

**Selon la** [**norme HTML Living Standard**](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-b-element)**, la** balise `<b>` peut être utilisée dans les exemples suivants :

> **mots clés dans un résumé de document, noms de produits dans une critique, mots actionnables dans un logiciel interactif basé sur du texte, ou un chapô d'article.**

### **Voici un exemple d'utilisation pour un nom de produit dans une critique**

```html
<p>Les <b>écouteurs Sennheiser IE 300</b> s'adaptent bien à vos oreilles et offrent un son incroyable.</p>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/headphones-bold-text-1.png align="left")

**La** balise `<b>` est destinée à attirer l'attention de l'utilisateur sur une portion de texte. Elle n'est pas censée avoir une importance particulière ou transmettre un ton d'urgence ou de sérieux.

**Ce serait une utilisation incorrecte de la** balise `<b>`.

```html
<p><b>ATTENTION !!</b> Cette zone est dangereuse.</p>
```

**La balise appropriée pour cette situation serait la** balise `<strong>` car elle transmet un sentiment de sérieux.

## **Différences entre les balises <b> et <strong> en HTML**

**Lorsque j'ai commencé à apprendre le HTML, je pensais que les** balises `<b>` et `<strong>` étaient identiques. Une partie de la confusion vient du fait qu'elles ont toutes deux le même style en gras par défaut dans la plupart des navigateurs.

**Une différence clé est que les** balises `<strong>` doivent être utilisées lorsque le texte a une grande importance, ou un sentiment d'urgence ou de sérieux. Les balises `<b>`, en revanche, doivent être utilisées pour attirer l'attention sur une portion de texte sans importance accrue.

**Cet exemple de la** balise `<strong>` indique à l'utilisateur quel élément de la liste doit être lu en premier et qu'il est plus important que les deux autres éléments de la liste.

```html
<p>Liste de choses à faire pour lundi :</p>
<ul>
    <li><p><strong>Payer le loyer.</strong></p></li>
    <li><p>Commencer le mémoire.</p></li>
    <li><p>Faire les courses.</p></li>
</ul>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/to-do-list-.png align="left")

**Une autre différence clé est que les** balises `<b>` ne doivent pas être utilisées dans les titres et légendes, contrairement aux balises `<strong>`.

**Voici un exemple utilisant la** balise `<strong>` pour mettre l'accent sur le titre du chapitre.

```html
<h1>Chapitre 5 : <strong>La Bataille</strong></h1>
```

## **Comment utiliser l'attribut Class avec les balises en HTML**

**Il est courant d'ajouter un attribut de classe dans la** balise `<b>` pour ajouter plus de sens sémantique.

**Si vous avez une série de phrases, vous pouvez ajouter une classe comme ceci** `<b class="lead">` à la première balise `<p>` et cela la marquera comme la phrase d'accroche.

```html
<article>
    <h2>Un jeune garçon retrouve sa mère biologique</h2>
    <p><b class="lead">Un garçon de six ans rencontre inattendument sa mère biologique dans le magasin d'alimentation local.</b></p>
    <p>Un jeune garçon et son grand-père faisaient des courses dans le magasin d'alimentation, lorsqu'une jeune femme les a approchés par derrière.</p>
    [...]
</article>
```

## **Doit-on utiliser la balise <b> pour styliser du texte en HTML ?**

**En HTML 5, il n'est pas approprié d'utiliser la** balise `<b>` pour styliser du texte. La méthode de stylisation préférée est d'utiliser la propriété CSS `font-weight`.

### **Exemple utilisant le mot-clé bold**

```html
 <p class="demo-para">J'utilise CSS pour mettre le texte en gras.</p>
```

```css
.demo-para {
  font-weight: bold;
}
```

### **Exemple utilisant des valeurs numériques**

```css
.demo-para {
  font-weight: 700;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/using-font-weight.png align="left")

## **Conclusion**

**Bien que les** balises `<b>` et `<strong>` puissent sembler similaires dans le navigateur, elles ont des significations différentes. Il est important de connaître la différence entre les deux pour pouvoir les utiliser de manière appropriée.

Les balises `<b>` sont utilisées pour attirer l'attention sur une portion de texte mais n'ont pas d'importance particulière. Les balises `<strong>`, en revanche, doivent être utilisées si le texte transmet un sentiment d'importance, de sérieux ou d'urgence.

**J'espère que vous avez apprécié cet article et appris quand utiliser les** balises `<b>`.