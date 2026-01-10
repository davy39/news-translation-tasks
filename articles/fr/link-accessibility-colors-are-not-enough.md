---
title: 'Comment rendre les liens accessibles (Indice : les couleurs ne suffisent pas)'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-23T18:12:14.000Z'
originalURL: https://freecodecamp.org/news/link-accessibility-colors-are-not-enough
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9fd2740569d1a4ca44c9.jpg
tags:
- name: Accessibility
  slug: accessibility
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: usability
  slug: usability
seo_title: 'Comment rendre les liens accessibles (Indice : les couleurs ne suffisent
  pas)'
seo_desc: 'By Anna Monus

  Link accessibility is one of the most important aspects of usability. However, designers
  often don''t understand what it takes to make links accessible. Most frequently,
  they only distinguish links by color, which makes it hard for users...'
---

Par Anna Monus

L'accessibilité des liens est l'un des aspects les plus importants de l'utilisabilité. Cependant, les designers ne comprennent souvent pas ce qu'il faut pour rendre les liens accessibles. Le plus fréquemment, ils ne distinguent les liens que par la couleur, ce qui rend difficile pour les utilisateurs ayant des déficiences visuelles de les repérer dans les blocs de texte — même si un contraste de couleur élevé est utilisé.

En règle générale, les liens accessibles ne devraient pas dépendre uniquement des couleurs. Partiellement parce que les utilisateurs ayant une basse vision, une déficience chromatique et d'autres troubles visuels ne peuvent pas toujours reconnaître ce type de lien, mais aussi parce qu'il est plus facile pour les utilisateurs réguliers de parcourir le contenu si les liens sont mieux mis en évidence.

Cependant, il n'est pas toujours facile de découvrir comment créer des liens accessibles qui correspondent au design de votre site web. Il est également possible d'en faire trop en utilisant trop de signifiants visuels qui pourraient confondre l'utilisateur.

<h2>Types de liens</h2>

Lorsque nous parlons de liens, nous pensons généralement aux liens bleus classiques avec un soulignement, mais il existe en réalité différents types de liens, tels que :

<ul>
    <li>les liens dans le texte du corps,</li>
    <li>les liens dans les titres et sous-titres,</li>
    <li>les liens de menu,</li>
    <li>les boutons,</li>
    <li>les liens d'image,</li>
    <li>les liens vidéo,</li>
    <li>les liens audio,</li>
    <li>et plus encore.</li>
</ul>

Dans cet article, je ne parlerai que du premier groupe : les liens dans le texte du corps. Ne le lisez pas comme un guide, mais plutôt comme une expérience pour comprendre ce qui peut être fait pour des liens plus accessibles.

<h2>Liens accessibles selon WCAG 2.0</h2>

Selon les [directives de WebAIM sur les liens et l'hypertexte](https://webaim.org/techniques/hypertext/link_text), WCAG 2.0 a deux exigences supplémentaires pour les liens dans le texte du corps :

1. Le texte du lien doit avoir un ratio de contraste de 3:1 par rapport au texte non-lien environnant.
2. Le lien doit présenter un "désignateur non-coloré" (généralement l'introduction du soulignement) à la fois au survol de la souris et au focus du clavier.

Les navigateurs web viennent avec un style de lien par défaut qui répond à ces exigences. Vous pouvez le vérifier en désactivant tous les styles CSS supplémentaires en utilisant l'extension de navigateur [Web Developer](https://chrispederick.com/work/web-developer/) ou un autre outil de développement. Par exemple, voici à quoi ressemble la page d'accueil du Mozilla Developer Network dans Chrome :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/basic-chrome-styling.jpg)

C'est un style très basique, mais c'est toujours un style : les liens bleus soulignés sont bien connus et les utilisateurs d'internet peuvent facilement les reconnaître. Ce n'est pas une coïncidence si le groupe Nielsen-Norman nomme également le bleu comme le choix de couleur de lien le plus sûr dans son article [Beyond Blue Links: Making Clickable Elements Recognizable](https://www.nngroup.com/articles/clickable-elements/).

<h2>Exemples de liens accessibles</h2>

WebAIM ne recommande pas de supprimer le soulignement en utilisant CSS, car "les utilisateurs sont habitués à voir les liens soulignés". Pourtant, de nombreux grands sites web ne suivent pas ce principe d'accessibilité des liens. Souvent, ils ne suppriment pas seulement le soulignement de l'état de lien par défaut, mais aussi les styles `:hover`.

Mais pourquoi font-ils cela ? Principalement pour des raisons esthétiques, cependant, les liens soulignés n'ont pas nécessairement à être simples et ennuyeux.

<h3>1. Border-bottom</h3>

Par exemple, Bloomberg utilise la propriété `border-bottom` pour imiter un soulignement dans une couleur différente. Comme vous pouvez le voir ci-dessous, les textes des liens sont noirs tandis que les soulignements sont bleus, ce qui donne un design stylisé aux liens.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/bloomberg-link-signifier.jpg)

Peut-être que les liens de Bloomberg pourraient bénéficier davantage de lettres en gras, mais c'est un bon exemple que les soulignements peuvent être utilisés pour les liens de manière créative, pas seulement de la manière habituelle.

<h3>2. Soulignement inversé</h3>

The Verge utilise une approche différente pour créer des soulignements pour les liens dans le texte du corps. Ici, les soulignements sont présents par défaut, mais ils sont supprimés lorsque l'utilisateur survole le lien. Lorsque le soulignement disparaît, la couleur change également subtilement, du rose au magenta (bien que ce changement de couleur soit à peine reconnaissable).

![Image](https://www.freecodecamp.org/news/content/images/2019/10/the-verge-link-underline.jpg)

La présence de soulignements dans l'état par défaut aide les lecteurs à repérer facilement les liens, même dans de grands blocs de texte. Et, lorsqu'ils survolent le lien, le changement d'état est instantanément visualisé par la disparition du soulignement. Un choix inhabituel, c'est sûr, mais il suit toujours le principe d'utilisation de désignateurs non-colorés pour des liens accessibles.

<h3>3. Icônes</h3>

Vous pouvez également aider les utilisateurs à reconnaître les liens en ajoutant de petites icônes à côté d'eux. Par exemple, certains sites d'actualités ajoutent une icône vidéo à côté des liens qui pointent vers des vidéos (bien que l'intégration de vidéos soit une pratique plus largement utilisée ces jours-ci).

WebAIM a choisi une solution tout-en-un pour l'accessibilité des liens. En plus du soulignement, ils ajoutent également une petite icône après chaque lien externe. De cette manière, l'icône ne sert pas seulement de signifiant visuel supplémentaire, mais distingue également clairement les liens externes et internes.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/webaim-external-link-icon.jpg)

Vous n'avez pas nécessairement besoin de créer une icône de lien par vous-même. Par exemple, Font Awesome a une [icône de lien externe](https://fontawesome.com/icons/external-link-alt?style=solid&from=io) que vous pouvez rapidement ajouter à vos liens.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/font-awesome-external-link.jpg)

<h3>4. Texte du lien</h3>

Comme les lecteurs d'écran informent les utilisateurs lorsqu'ils rencontrent un lien, il n'est pas recommandé d'utiliser des phrases telles que "lien vers" ou "suivez ce lien" pour le texte du lien. Au lieu de cela, vous devriez fournir des textes de lien qui décrivent le contenu principal du lien. Cela facilite la décision des utilisateurs de cliquer sur le lien, ce qui est particulièrement important pour les utilisateurs ayant des [déficiences cognitives](https://webaim.org/articles/cognitive/).

WCAG 2.0 a même une recommandation sur la façon de [fournir des textes de lien appropriés](https://www.w3.org/TR/2008/WD-WCAG20-TECHS-20081103/H30.html), avec une poignée d'exemples utiles (principalement pour les liens d'image, cependant).

Si vous voulez voir un exemple de texte de lien approprié, je mentionnerais le site web Gov.uk qui publie des informations gouvernementales au Royaume-Uni. Par exemple, consultez leur page [Créer une entreprise](https://www.gov.uk/set-up-business).

![Image](https://www.freecodecamp.org/news/content/images/2019/10/gov.uk-link-texts.jpg)

Jetez un coup d'œil, par exemple, à la ligne _En savoir plus sur le fait d'être un travailleur indépendant et comment s'inscrire_ sur la capture d'écran ci-dessus. Notez qu'ils ont placé la balise d'ancrage sur la partie qui décrit le but du lien ("être un travailleur indépendant et comment s'inscrire") au lieu du verbe d'action ("en savoir plus").

<h2>Le rôle controversé de l'attribut <code>title</code></h2>

Le rôle de l'[attribut global `title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title) dans l'accessibilité des liens est une question intéressante. Si vous l'ajoutez à un lien, les informations supplémentaires apparaissent quelque part autour du lien lorsque les utilisateurs le survolent.

Par exemple, prenez la ligne de HTML suivante :

`<a href="#" title="Informations supplémentaires">Survolez ce lien mais ne cliquez pas dessus.</a>`

<p>Il est affiché comme ceci dans le navigateur : <a href="#" title="Informations supplémentaires">Survolez ce lien mais ne cliquez pas dessus.</a></p>

J'ai longtemps pensé que l'ajout de l'attribut `title` aux liens est une bonne pratique pour l'accessibilité, car les informations supplémentaires aident les utilisateurs à comprendre le but du lien. Cependant, WCAG 2.0 a une vision légèrement différente de la question.

Sur leur page "[Supplementing link text with the title attribute](https://www.w3.org/TR/2008/WD-WCAG20-TECHS-20081103/H33.html)", ils mentionnent plusieurs problèmes d'accessibilité. Par exemple, l'attribut `title` n'est pas disponible pour les technologies d'assistance et les utilisateurs uniquement au clavier. De plus, il disparaît après environ cinq secondes dans certains agents utilisateurs, ce qui ne laisse généralement pas assez de temps pour le lire.

Dans l'ensemble, WCAG 2.0 ne déconseille pas l'attribut `title` mais recommande une utilisation prudente. Une chose est sûre, n'utilisez jamais `title` pour des informations importantes qui ne sont pas disponibles sous une autre forme, comme des avertissements. Sur une autre note, si `title` ne peut être utilisé que pour des informations sans importance, vaut-il la peine de l'utiliser du tout ?

<h2>États des liens</h2>

Il existe cinq états de liens différents, représentés par des pseudo-classes CSS : [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/:hover), [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus), [`:active`](https://developer.mozilla.org/en-US/docs/Web/CSS/:active), [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/:visited), et [`:link`](https://developer.mozilla.org/en-US/docs/Web/CSS/:link).

Il est une question ouverte de savoir s'il est préférable pour l'accessibilité de styliser tous les états de liens différemment ou non. Si vous utilisez différentes règles de style pour chaque état, les utilisateurs sont informés de chaque changement, mais est-ce toujours une bonne chose ? Trop de changements d'état peuvent causer une surcharge d'informations et de la confusion à l'utilisateur.

Personnellement, j'ai tendance à créer un style pour l'état de lien par défaut, un deuxième pour les états `:hover`, `:active`, et `:focus`, et parfois un troisième pour les liens `:visited`. Cependant, je ne peux toujours pas dire si c'est la meilleure solution pour l'accessibilité. Si vous êtes intéressé par le sujet, voici une [discussion UX intéressante sur StackOverflow](https://ux.stackexchange.com/questions/73403/should-focus-and-hover-styles-be-the-same-or-distinct) sur le fait que le style des états `:focus` et `:hover` devrait être le même ou distinct.

Cependant, il y a une chose importante que vous devez garder à l'esprit. **Ne supprimez pas le contour pointillé que les navigateurs utilisent pour l'état `:focus`.** La navigation au clavier (tabulation) sera inutile si l'élément focalisé n'est pas visible à l'écran. Si vous supprimez le contour pointillé, les utilisateurs du clavier perdront littéralement le focus. Si vous êtes gêné par le style de contour par défaut [rendez-le moins intrusif avec un style supplémentaire](https://a11yproject.com/posts/never-remove-css-outlines/), mais ne le supprimez pas.

<h2>Lire plus</h2>

Dans mon blog, je traite de sujets liés à l'accessibilité qui sont moins largement discutés. Si vous voulez en lire plus, consultez également mon article sur pourquoi [la documentation logicielle fait partie de l'accessibilité](https://www.annalytic.com/documentation-part-of-accessibility.html).