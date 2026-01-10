---
title: Qu'est-ce que le HTML – Définition et signification du langage de balisage
  hypertexte
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-24T16:38:12.000Z'
originalURL: https://freecodecamp.org/news/what-is-html-definition-and-meaning
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/html.png
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: markup
  slug: markup
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que le HTML – Définition et signification du langage de balisage
  hypertexte
seo_desc: "HTML, or Hypertext Markup Language, is a markup language for the web that\
  \ defines the structure of web pages. \nIt is one of the most basic building blocks\
  \ of every website, so it's crucial to learn if you want to have a career in web\
  \ development. \nIn..."
---

HTML, ou Hypertext Markup Language, est un langage de balisage pour le web qui définit la structure des pages web. 

C'est l'un des éléments de base les plus fondamentaux de chaque site web, il est donc crucial de l'apprendre si vous souhaitez faire carrière dans le développement web. 

Dans cet article, je vais vous expliquer en détail ce qu'est le HTML, comment il fonctionne sur les pages web, et nous aborderons également une partie vraiment intéressante du HTML – le HTML sémantique.

## Qu'est-ce que le HTML ?

Pour comprendre le "HTML" de A à Z, examinons chaque mot qui compose l'abréviation : 

**Hypertexte** : texte (souvent avec des éléments intégrés tels que des images) organisé de manière à connecter des éléments liés.

**Balise** : un guide de style pour la composition de tout ce qui doit être imprimé en format papier ou numérique.

**Langage** : un langage qu'un système informatique comprend et utilise pour interpréter des commandes.

Le HTML détermine la structure des pages web. Cette structure seule ne suffit pas pour rendre une page web attrayante et interactive. Vous devrez donc utiliser des technologies complémentaires telles que CSS et JavaScript pour rendre votre HTML beau et ajouter de l'interactivité, respectivement. 

Dans ce cas, j'aime décomposer les trois technologies – HTML, CSS et JavaScript – de cette manière : elles sont comme un corps humain. 

* Le HTML est le squelette, 
* Le CSS est la peau, 
* Et le JavaScript est le système circulatoire, digestif et respiratoire qui donne vie à la structure et à la peau.

Vous pouvez également voir le HTML, le CSS et le JavaScript de cette manière : le HTML est la structure d'une maison, le CSS est la décoration intérieure et extérieure, et le JavaScript est l'électricité, le système d'eau et de nombreuses autres fonctionnalités qui rendent la maison habitable.

## Balises HTML

Puisque le HTML définit le balisage pour une page web particulière, vous souhaiterez que le texte, les images ou d'autres éléments intégrés apparaissent de certaines manières. 

Par exemple, vous pourriez vouloir que certains textes soient grands, d'autres petits, et certains en gras, en italique ou sous forme de liste à puces. 

Le HTML dispose de "balises" qui vous permettent de faire cela. Il existe donc des balises pour créer des titres, des paragraphes, des mots en gras, des mots en italique, et bien plus encore.

L'image ci-dessous décrit l'anatomie d'une balise HTML :

![anatomy-of-an-html-tag](https://www.freecodecamp.org/news/content/images/2021/08/anatomy-of-an-html-tag.png)


## Éléments HTML

Un élément se compose de la balise d'ouverture, d'un caractère, du contenu et d'une balise de fermeture. Certains éléments sont vides – c'est-à-dire qu'ils n'ont pas de balise de fermeture mais ont plutôt une source ou un lien vers le contenu que vous souhaitez intégrer sur la page web. 

Un exemple d'élément vide est `<img>`, que vous utilisez pour intégrer des images sur une page web.

Les éléments HTML sont souvent utilisés de manière interchangeable avec les balises, mais il existe une petite différence entre les deux. Un élément est une combinaison de la balise d'ouverture et de la balise de fermeture, ainsi que du contenu entre elles.

J'ai créé une autre image pour vous aider à visualiser l'anatomie d'un élément HTML :

![anatomy-of-an-html-element](https://www.freecodecamp.org/news/content/images/2021/08/anatomy-of-an-html-element.png)

## Attributs HTML
 
Les balises HTML prennent également ce que l'on appelle des attributs. Ces attributs sont placés dans la balise d'ouverture et vont des styles et identifiants aux classes. Ils prennent des valeurs, qui transmettent plus d'informations sur l'élément et vous aident à faire des choses comme le style et la manipulation avec JavaScript.

Dans l'infographie ci-dessous, la balise d'ouverture contient un attribut `class` avec une valeur de `text`. Cela peut être utilisé pour styliser l'élément ou le sélectionner avec JavaScript pour l'interactivité.

![attribute-1](https://www.freecodecamp.org/news/content/images/2021/08/attribute-1.png)

Voici l'anatomie d'une page HTML de base :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Définition du HTML</title>
  </head>
  <body>
    <!--Le contenu de la page tel que le texte et les images va ici-->
  </body>
</html>
```

Examinons les parties importantes du code ici :

`<!Doctype html>` : Spécifie que nous utilisons HTML5 dans ce code. Avant l'introduction de HTML5, vous deviez explicitement indiquer quelle version de HTML vous utilisiez avec la balise `<!Doctype>`. Par exemple, HTML4.0, 3.2, et ainsi de suite. Mais maintenant, nous n'en avons plus besoin. Lorsque "html" est écrit dans le code, le navigateur suppose automatiquement que vous codez en HTML5.

`<html></html>` : la racine, ou l'élément de niveau supérieur de chaque document HTML. Tous les autres éléments doivent être enveloppés dedans.

`<head></head>` : l'une des parties les plus cruciales du document HTML. Les robots d'indexation recherchent à l'intérieur des balises head pour obtenir des informations importantes sur la page. Il contient des informations telles que le titre de la page, les feuilles de style, les méta-informations pour le SEO, et bien plus encore.

`<meta />` : il s'agit d'un élément vide qui transmet des méta-informations sur la page. Ces informations peuvent inclure l'auteur, le type d'encodage utilisé (presque toujours UTF-8), la réactivité, la compatibilité, et bien plus encore. Les robots d'indexation regardent toujours la balise meta pour obtenir des informations sur la page web, ce qui jouera un rôle crucial dans le SEO.

`<title></title>` : cela définit le titre de la page web. Il est toujours affiché dans l'onglet du navigateur.

`<body></body>` : tout le contenu du document HTML est situé à l'intérieur de la balise body. Il ne peut y avoir qu'une seule balise `<body>` sur toute la page.
  
## Qu'est-ce que le HTML sémantique ?

Le HTML sémantique signifie que vos balises HTML transmettent le sens réel de ce pour quoi elles sont utilisées. 

La sémantique a toujours été une partie intégrante du HTML depuis sa création au début des années 90. Mais elle n'a jamais gagné une pertinence particulière jusqu'à la fin des années 90, lorsque CSS a commencé à fonctionner dans la plupart des navigateurs. 

Avec le HTML sémantique, les balises sémantiquement neutres telles que `<div>` et `<span>` sont déconseillées puisque des balises sémantiquement plus descriptives telles que `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>` et `<article>` peuvent faire la même chose qu'elles.

Un avantage notable de l'utilisation des balises sémantiques est que les robots d'indexation peuvent indexer la page web ou le site web facilement, améliorant ainsi le SEO en retour. 

De plus, un site web qui utilise la sémantique devient plus informatif, adaptable et accessible à ceux qui utilisent des lecteurs d'écran pour accéder aux sites web. 

### Balises sémantiques importantes et ce qu'elles font 

Examinons certaines des balises HTML sémantiques les plus couramment utilisées :

`<header>` : L'élément `<header>` définit la section introductive d'une page web. Il contient des éléments tels que le logo, la navigation, le sélecteur de thème et la barre de recherche.

`<nav>` : L'élément `<nav>` spécifie les éléments de navigation de la page tels que l'accueil, le contact, à propos, les FAQ, et ainsi de suite.

`<main>` : L'élément `<main>` est conventionnellement traité comme le descendant immédiat de la balise <body>. Il contient les sections principales du document HTML à part `<header>` et `<footer>`. Idéalement, il devrait n'y en avoir qu'un seul dans tout le document HTML.
    
`<section>` : L'élément `<section>` définit une section particulière de la page web. Cela peut être la section de présentation, la section à propos, la section de contact, ou d'autres. Vous pouvez utiliser de nombreuses sections dans un seul document HTML.
 
`<article>` : L'élément `<article>` représente une certaine partie d'une page web qui transmet une information particulière. Une telle information pourrait être une combinaison de texte, d'images, de vidéos et d'éléments intégrés. Considérez cet élément comme un article de blog autonome sur une page contenant des extraits d'autres articles de blog.

`<aside>` : Comme le nom l'indique, cela représente une barre latérale sur une page web. Il s'agit généralement d'une partie de la page web qui n'est pas directement liée au contenu principal.

`<footer>` : L'élément `<footer>` accueille des éléments tels que des liens rapides, des informations de copyright, ou toute autre donnée liée à l'ensemble du site web ou de la page web.

Notez que, puisque les éléments sémantiques transmettent un sens réel et ce que fait un contenu particulier (comme `nav` pour la navigation, `aside` pour une barre latérale, etc.), ces éléments ne sont pas automatiquement positionnés là où ils sont censés être. Vous devez toujours le faire avec CSS. 

Un document HTML sémantique super simple ressemble à ceci :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Définition du HTML</title>
  </head>

  <body>
    <header>
      <h1 class="logo">LOGO</h1>
      <nav>
        <ul>
          <li>Accueil</li>
          <li>À propos</li>
          <li>Contact</li>
          <li>FAQ</li>
        </ul>
      </nav>
    </header>
    <main>
      <section class="about-me">
        <article>
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Optio magni
          est asperiores nemo, adipisci minus itaque quam, rem libero aliquam
          nesciunt, nisi inventore assumenda earum repellat labore ratione
          architecto eos quis. Soluta mollitia cupiditate dolorem. Consequatur a
          soluta laudantium nihil. Molestias, officiis ut! Nobis adipisci
          voluptatem quam at officia beatae!
        </article>
      </section>
      <section class="contact-me">
        Vous pouvez me trouver sur
        <a href="https://twitter.com/koladechris">Twitter</a> Vous pouvez me trouver sur
        <a href="https://Instagram.com/koladechris">Instagram</a>
      </section>
      <aside class="address">Mon Adresse</aside>
    </main>
    <footer>
9 2020 Tous droits réservés</footer>
  </body>
</html>
```
Voici à quoi cela ressemble dans le navigateur :

![semanticHTML-4](https://www.freecodecamp.org/news/content/images/2021/08/semanticHTML-4.png)

Vous pouvez voir que le contenu à l'intérieur de la balise `<aside>` n'est pas dans la barre latérale et que le contenu à l'intérieur de la balise `<nav>` n'est pas automatiquement disponible en tant que barre de navigation. C'est pourquoi vous devez toujours les faire ressembler à ce qu'ils sont censés être avec CSS.

## Conclusion 

J'espère que cet article vous a aidé à apprendre les bases du HTML et ce qu'il fait. Maintenant, vous pouvez commencer à apprendre des technologies plus avancées telles que CSS et JavaScript, puis commencer à former une carrière solide dans le développement web. 

Merci beaucoup d'avoir lu et passez un bon moment.