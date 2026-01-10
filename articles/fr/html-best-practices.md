---
title: Meilleures pratiques HTML – Comment construire un meilleur site web basé sur
  HTML
subtitle: ''
author: Cess
co_authors: []
series: null
date: '2022-01-03T23:42:00.000Z'
originalURL: https://freecodecamp.org/news/html-best-practices
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/HTML-Best-Practices
seo_title: Meilleures pratiques HTML – Comment construire un meilleur site web basé
  sur HTML
---

How-to-Build-a-Better-HTML-Based-Website--1-.png
tags:
- name: meilleures pratiques
  slug: meilleures-pratiques
- name: codage
  slug: codage
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Développement Web
  slug: developpement-web
seo_title: null
seo_desc: "HTML est l'épine dorsale de tout site web. C'est la première chose que les gens voient. Sans lui, il n'y aurait pas de site web. \nPar conséquent, il est important de respecter les bonnes pratiques de codage. Si vous ne suivez pas les meilleures pratiques, vous créerez une mauvaise expérience utilisateur pour l'internaute."
---

**HTML** est l'épine dorsale de tout site web. C'est la première chose que les gens voient. Sans lui, il n'y aurait pas de site web. 

Par conséquent, il est important de respecter les bonnes pratiques de codage. Si vous ne suivez pas les meilleures pratiques, vous créerez une mauvaise expérience utilisateur pour l'internaute.

Il y a toujours quelque chose de nouveau à apprendre en HTML, que vous soyez un débutant en codage ou un professionnel expérimenté.

Dans cet article, nous parlerons des meilleures pratiques de base de HTML.

Commençons. 💃

## Meilleures pratiques HTML

Les **meilleures pratiques HTML** sont des règles qui vous aident à créer des sites web faciles à maintenir et à lire.

Voici quelques directives à garder à l'esprit lors de la construction d'un site web basé sur HTML :

### Utilisez un seul élément <h1> pour une feuille de code

Il existe six balises d'en-tête différentes en HTML, de `<h1>` à `<h6>`. La balise `<h1>` est l'en-tête principal (sujet de la page web) tandis que la balise `<h6>` est l'en-tête le moins important.

La balise `<h1>` est plus grande que la balise `<h2>`, la balise `<h2>` est plus grande que la balise `<h3>`, et ainsi de suite jusqu'à la balise `<h6>`. Chacun des en-têtes diminue en taille selon son importance.

Il est important d'éviter d'utiliser plus d'un élément `<h1>` pour une feuille de code.

Ne faites pas cela 🔹🏿 :

```
<main>
<div>
<h1>Le codage peut-il être amusant ?</h1>
<p>Plus vous codez, meilleur vous devenez</p>
</div>

<div>
<h1>Le codage est amusant</h1>
<p>C'est toujours mieux quand on s'amuse en codant</p>
</div>
</main>
```

Dans l'exemple ci-dessus, nous avons utilisé la balise `<h1>` sur le premier et le deuxième `<div>`. Coder de cette manière fonctionnera, mais bien que vous atteindrez le même objectif, ce n'est pas la meilleure pratique.

Faites plutôt cela 🔹🏿 :

```
<main>

<div>
<h1>Le codage peut-il être amusant ?</h1>
<p>Plus vous codez, meilleur vous devenez</p>
</div>

<div>
<h2>Le codage est amusant</h2>
<p>C'est toujours mieux quand on s'amuse en codant</p>
</div>

</main>

```

Avoir un seul élément `<h1>` sur une page web est vital pour l'optimisation des moteurs de recherche (SEO). Cela aide les moteurs de recherche à comprendre de quoi parle une page web (l'idée principale d'une page web).  

### Ne sautez pas les niveaux d'en-tête en HTML

Lorsque vous utilisez les balises d'en-tête, il est vital de procéder de `<h1>` à `<h2>` à `<h3>` à `<h4>` et ainsi de suite...

N'utilisez pas `<h1>` puis passez à `<h3>` lorsque vous utilisez des balises d'en-tête. Il est difficile pour les visiteurs du web utilisant un lecteur d'écran de comprendre le contenu de votre page web lorsque vous sautez des niveaux d'en-tête.

Un lecteur d'écran est une technologie qui aide les personnes ayant des difficultés à voir à accéder et à interagir avec le contenu numérique, comme les sites web ou les applications via l'audio ou le toucher. Les principaux utilisateurs des lecteurs d'écran sont les personnes aveugles ou ayant une vision très limitée.  

Vous pouvez lire une petite [introduction aux lecteurs d'écran ici](https://abilitynet.org.uk/factsheets/introduction-screen-readers).

Ne faites pas cela 🔹🏿 :

```
<h1>Le codage est amusant</h1>
<h3>C'est toujours mieux quand on s'amuse en codant</h3>
<h5>La cohérence est la clé</h5>
```

Faites plutôt cela 🔹🏿 :

```
<h1>Le codage peut-il être amusant ?</h1>
<h2>Plus vous codez, meilleur vous devenez</h2>
<h3>Le codage est amusant</h3>
```

### Utilisez l'élément figure pour ajouter des légendes à vos images en HTML

Il est conseillé d'utiliser l'élément `<figure>` lorsque vous ajoutez des légendes à vos images. Il est important d'utiliser l'élément `<figcaption>` avec l'élément `<figure>` pour que cela fonctionne.

Ne faites pas cela 🔹🏿 :

```
<div>
<img src="a-man-coding.jpg" alt="Un homme travaillant sur son ordinateur">
<p>Ceci est une image d'un homme travaillant sur son ordinateur</p>
</div>
```

L'exemple ci-dessus fonctionnera comme prévu, mais ce n'est pas la meilleure façon de procéder. Dans une situation où l'image ne parvient pas à se charger, vous aurez le texte `alt` et le texte sur l'élément `<p>` qui s'affichent à l'écran. Il sera difficile pour un visiteur du web utilisant un lecteur d'écran de faire la différence entre le `<p>` et le texte `alt`.

Gardez toujours à l'esprit que le fait que votre code fonctionne ne signifie pas que vous suivez les meilleures pratiques.

Faites plutôt cela 🔹🏿 :

```
<figure>
<img src="a-man-coding.jpg" alt="Un homme travaillant sur son ordinateur">
<figcaption> Ceci est une image d'un homme travaillant sur son ordinateur</figcaption>
</figure>
```

L'exemple ci-dessus est la meilleure façon d'ajouter des légendes à vos images.

Il est important d'ajouter des légendes à vos images de cette manière pour :

* L'optimisation des moteurs de recherche : Il est plus facile de trouver vos images sur les moteurs de recherche.
* Il sera plus facile pour les visiteurs du web qui utilisent des lecteurs d'écran de comprendre le contenu de votre page web.

### N'utilisez pas de divs pour créer des en-têtes et des pieds de page – utilisez des éléments sémantiques à la place

Les éléments sémantiques HTML marquent la structure d'un document de manière plus significative sur une page web. Il est préférable d'utiliser des éléments sémantiques HTML pour l'assemblage correct de votre page web.

Évitez d'utiliser des `<divs>` à la place des sémantiques HTML. N'utilisez pas d'éléments `<div>` pour afficher les en-têtes et les pieds de page sur votre page web. Utilisez plutôt des éléments sémantiques `<header>` et `<footer>`.

L'élément `<header>` montre la navigation ou la partie d'ouverture de la page web.

L'élément `<footer>` montre les informations de copyright ou les liens de navigation concernant la page web.

Ne faites pas cela 🔹🏿 :

```
<div class="header">
<a href="index.html">Accueil</a>
<a href="#">À propos</a>
<a href="#">Contact</a>
</div>

<div class="footer">
<a href="index.html">Accueil</a>
<a href="#">À propos</a>
<a href="#">Contact</a>
</div>
```

Dans l'exemple ci-dessus, nous avons utilisé la balise `<div>` comme conteneur pour le `<header>` et le `<footer>`. Coder de cette manière fonctionnera, mais bien que vous atteindrez le même objectif, ce n'est pas la meilleure pratique.

Faites plutôt cela 🔹🏿 :

```
<header>
<h1></h1>
</header>

<footer>
<a href="index.html">Accueil</a>
<a href="#">À propos</a>
<a href="#">Contact</a>
</footer>
```

L'exemple ci-dessus est la meilleure façon d'ajouter des `<footers>` et des `<headers>` à votre page web.

Il est important d'ajouter des `<footer>` et des `<header>` en utilisant des éléments sémantiques HTML parce que :

* L'utilisation d'éléments sémantiques pour votre `header` et `footer` rend votre code plus facile à lire.

* Cela offre une meilleure expérience utilisateur pour les visiteurs du web. Il sera plus facile pour les visiteurs du web qui utilisent des lecteurs d'écran de comprendre le contenu de votre page web.


Consultez cet article pour en savoir plus sur les [éléments sémantiques HTML](<https://www.freecodecamp.org/news/semantic-html5-elements/#:~:text=Semantic%20HTML%20elements%20are%20those,content%20that%20is%20inside%20them>).

### Évitez d'utiliser `<b>` et `<i>` pour mettre en gras et en italique des textes sur une page web

Les balises `<b>` et `<i>` sont également connues sous le nom de balises de gras et d'italique. Elles sont toutes deux utilisées pour mettre en évidence des mots dans un texte sur une page web.

Vous ne devriez pas utiliser `<b>` et `<i>` pour le gras et l'italique car ils n'ont aucune signification sémantique. Utilisez la propriété CSS `font-weight` ou utilisez les balises `<strong>` et `<em>` à la place.

Vous utilisez la balise `<strong>` pour rendre un texte important sur une page web. Elle met en évidence ou en gras un texte sur une page web. La balise `<em>` met l'accent sur le texte dans une page web. Elle affiche également le texte en italique comme la balise `<i>`.

Ne faites pas cela 🔹🏿 :

```
<p><i>Codez à votre propre rythme</i><p>

<p><b>codez à votre propre rythme</b><p>
```

Les textes affichés seront en gras et en italique dans l'exemple ci-dessus. Cela n'aura aucune importance pour l'utilisateur web utilisant un lecteur d'écran. Cela n'a aucune signification sémantique.

**La** spécification **HTML5** indique que les balises `<b>` et `<i>` ne doivent être utilisées qu'en dernier recours si aucune autre balise n'est disponible.

Faites plutôt cela 🔹🏿 :

```
 <p><strong>Codez à votre propre rythme</strong><p>

<p><em>codez à votre propre rythme</em><p>
```

### Ne placez pas d'élément de niveau bloc à l'intérieur d'éléments en ligne

Les éléments de niveau bloc commencent sur une nouvelle ligne sur une page web. Par défaut, ils s'étirent du début de la ligne à la fin sur une page web. Vous ne pourrez pas ajouter plus de contenu en ligne à un élément de bloc sans utiliser CSS.

Les éléments `<p>`, `<h1>-<h6>`, et `<div>` sont quelques exemples d'éléments de niveau bloc.

L'élément en ligne couvre la plus petite zone sur une page web. Ils ne commencent pas sur une nouvelle ligne sur une page web.

Les éléments `<span>`, `<em>`, et `<a>` sont quelques exemples d'éléments en ligne.

Vous ne pouvez pas placer d'éléments de bloc à l'intérieur d'éléments en ligne.

Ne faites pas cela 🔹🏿 :

```
<a href="#" >
    
    <p> Visitez freecodecamp </p>
    
</a>
```

Vous ne pouvez pas envelopper `<p>` à l'intérieur d'un élément `<a>` car `<p>` est un élément de niveau bloc et `<a>` est un élément en ligne.

Faites plutôt cela 🔹🏿 :

```
<p>
Visitez <a href="www.freecodecamp.org" target="_blank">FreecodeCamp</a> 
pour apprendre Javascript
</p>
```


L'exemple ci-dessus est la meilleure façon d'imbriquer des éléments en ligne à l'intérieur d'un élément de niveau bloc.

Il est important de noter que :

* L'élément de niveau bloc ne peut pas être imbriqué à l'intérieur d'un élément en ligne.
* L'élément en ligne peut être imbriqué à l'intérieur d'un élément de niveau bloc.
* L'élément en ligne et l'élément de niveau bloc peuvent être imbriqués à l'intérieur de l'élément de niveau bloc.

Juste une note rapide : imbriqué, dans l'exemple ci-dessus, signifie placer à l'intérieur. Donc lorsque je dis qu'il ne peut pas être imbriqué, je fais référence au fait qu'il ne peut pas être placé à l'intérieur.

J'espère que vous comprenez ces trois règles simples utilisées pour imbriquer des éléments.

Il est également possible de convertir des éléments de niveau bloc en éléments en ligne et vice versa en utilisant CSS. Utilisez `display: inline-block` et `display: inline` pour convertir de bloc à élément en ligne.

Il est important de se rappeler que le fait que votre code fonctionne ne signifie pas que vous suivez les meilleures pratiques.

C'est pourquoi je recommande toujours d'utiliser le [service de validation de balisage W3C](https://validator.w3.org/) pour vérifier vos codes.

Ce validateur vérifie la validité du balisage des documents web en HTML, XHTML, SMIL, MathML, etc. : [Service de validation de balisage W3C](https://validator.w3.org/).

Vous pouvez vérifier votre code en copiant son URL et en le collant sur le site ou en téléchargeant votre fichier HTML.

## Conclusion
J'espère que cet article vous a aidé à apprendre une ou deux choses sur les meilleures pratiques HTML. J'ai essayé d'inclure uniquement les conseils les plus utiles afin que vous puissiez commencer à les utiliser immédiatement ! 
 
Si vous avez d'autres questions ou commentaires, n'hésitez pas à me contacter à tout moment sur Twitter : [@cessss_](http://www.twitter.com/cessss_) et LinkedIn : [Success](https://www.linkedin.com/in/success-eriamiantoe/) 
 
J'essaierai de répondre dès que possible ! Merci pour votre lecture 💙.