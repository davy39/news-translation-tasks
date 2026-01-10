---
title: Apprendre le HTML – Guide d'étude sur la conception Web réactive
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-06-27T16:41:05.000Z'
originalURL: https://freecodecamp.org/news/freecodecamp-responsive-web-design-study-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/jackson-sophat-wUbNvDTsOIc-unsplash.jpg
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: HTML
  slug: html
- name: responsive design
  slug: responsive-design
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Apprendre le HTML – Guide d'étude sur la conception Web réactive
seo_desc: 'HTML (HyperText Markup Language) is an important markup language for building
  websites. HTML represents the content of the web page.

  But when you are learning this information for the first time, it can be hard to
  keep track of all of the different H...'
---

HTML (HyperText Markup Language) est un langage de balisage important pour la création de sites Web. HTML représente le contenu de la page Web.

Mais lorsque vous apprenez ces informations pour la première fois, il peut être difficile de garder une trace de tous les différents éléments HTML.

Dans cet article, j'ai créé un guide d'étude pour l'ensemble du [projet pratique Apprendre le HTML en construisant une application photo de chat](https://www.freecodecamp.org/learn/2022/responsive-web-design/#learn-html-by-building-a-cat-photo-app). Ce guide d'étude est rempli d'informations supplémentaires, de liens et de vidéos pour vous aider à mieux comprendre les concepts.

N'hésitez pas à vous référer à ce guide tout au long de la certification. Si vous êtes intéressé par une introduction détaillée au HTML, veuillez lire [cet article freeCodeCamp sur le HTML](https://www.freecodecamp.org/news/what-is-html-what-does-html-stand-for-solved/).

Voici la liste complète des sujets abordés. Cliquez sur l'un des liens ci-dessous pour en savoir plus sur le sujet.

## Table des matières

* [Éléments de titre - Étapes 1-2, 17, 18, 25, 33](#heading-elements-de-titre)
* [Éléments de paragraphe - Étape 3](#heading-elements-de-paragraphe)
* [Commentaires HTML - Étape 4](#heading-commentaires-html)
* [Élément principal - Étape 5](#heading-element-principal)
* [Indentation HTML - Étape 6](#heading-indentation-html)
* [Éléments d'image - Étapes 7-9, 21, 28, 29](#heading-elements-dimage)
* [Éléments d'ancrage - Étapes 10-11, 63](#heading-elements-dancrage)
* [Intégration d'éléments d'ancrage dans des paragraphes - Étape 12](#heading-integration-delements-dancrage-dans-des-paragraphes)
* [Attributs de cible - Étape 13](#heading-attributs-de-cible)
* [Intégration d'images dans des balises d'ancrage - Étape 14](#heading-integration-dimages-dans-des-balises-dancrage)
* [Éléments de section - Étapes 15-16, 32](#heading-elements-de-section)
* [Éléments de liste non ordonnée - Étapes 19-20](#heading-elements-de-liste-non-ordonnee)
* [Éléments Figure et Figcaption - Étapes 22-23, 27, 30](#heading-elements-figure-et-figcaption)
* [Éléments d'emphase - Étape 24](#heading-elements-demphase)
* [Éléments de liste ordonnée - Étape 26](#heading-elements-de-liste-ordonnee)
* [Éléments Strong - Étape 31](#heading-elements-strong)
* [Éléments de formulaire - Étapes 34-35](#heading-elements-de-formulaire)
* [Champs de texte de formulaire et boutons de soumission - Étapes 36-42](#heading-champs-de-texte-de-formulaire-et-boutons-de-soumission)
* [Boutons radio de formulaire - Étapes 43, 47, 48](#heading-boutons-radio-de-formulaire)
* [Éléments de label - Étapes 44-46, 55](#heading-elements-de-label)
* [Éléments Fieldset et Legend - Étapes 49-52](#heading-elements-fieldset-et-legend)
* [Éléments de case à cocher de formulaire - Étapes 53-54, 56-58](#heading-elements-de-case-a-cocher-de-formulaire)
* [Attributs de valeur et vérifiés - Étapes 59-60](#heading-attributs-de-valeur-et-verifies)
* [Éléments de pied de page - Étapes 61-62](#heading-elements-de-pied-de-page)
* [Éléments Head et title - Étapes 64-65](#heading-elements-head-et-title)
* [Attribut lang - Étape 66](#heading-attribut-lang)
* [DOCTYPE - Étape 67](#heading-doctype)

## Ressources HTML supplémentaires

* [Apprendre le HTML – Tutoriel complet pour débutants (2022)](https://www.youtube.com/watch?v=kUMe1FH4CHE)
* [Cours complet HTML - Tutoriel pour créer un site Web](https://www.youtube.com/watch?v=pQN-pnXPaVg)
* [Tutoriel HTML - Comment créer un site Web super simple](https://www.youtube.com/watch?v=PlxWf493en4)

## Éléments de titre

Les éléments de titre HTML représentent le titre principal et les sous-titres d'une page Web.

L'élément `h1` représente le titre le plus important et ne doit être utilisé qu'une seule fois par page Web.

```html
<h1>Je représente le titre principal d'une page Web</h1>
```

L'élément `h2` représente le deuxième titre le plus important sur la page.

```html
<h2>Je suis le deuxième élément de titre le plus important</h2>
```

Il y a un total de six éléments de titre de section.

```html
<h1>Je suis l'élément de titre le plus important</h1>
<h2>Je suis le deuxième élément de titre le plus important</h2>
<h3>Je suis le troisième élément de titre le plus important</h3>
<h4>Je suis le quatrième élément de titre le plus important</h4>
<h5>Je suis le cinquième élément de titre le plus important</h5>
<h6>Je suis l'élément de titre le moins important</h6>
```

Voici à quoi cela ressemble rendu sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-18-at-9.19.27-PM.png)

Pour en savoir plus sur les éléments de titre, veuillez lire [cette explication détaillée des éléments de titre DevDocs](https://devdocs.io/html/element/heading_elements).

## Éléments de paragraphe

Les éléments de paragraphe représentent les paragraphes sur une page Web.

```html
<p>J'adore apprendre avec freeCodeCamp. Ils ont des milliers d'articles et de vidéos gratuits pour m'aider à apprendre à coder.</p>
```

Voici à quoi cela ressemble rendu sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-18-at-9.55.21-PM.png)

Pour en savoir plus sur les éléments de paragraphe, veuillez lire [cette explication détaillée de l'élément `p` DevDocs](https://devdocs.io/html/element/p).

## Commentaires HTML

Les commentaires HTML peuvent être utiles dans le code lorsque vous devez laisser des messages pour vous-même ou pour d'autres développeurs lisant votre code. Les commentaires ne seront pas rendus sur la page Web.

```html
<!--Je suis un commentaire. Je ne suis pas affiché sur la page Web.-->
<p>Je suis un élément de paragraphe.</p>
```

Voici à quoi ressemble le résultat rendu sur la page Web.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-18-at-10.10.32-PM.png)

Pour en savoir plus sur les commentaires HTML, je suggère de lire ces articles utiles.

* [Commenter le HTML – Exemple de code](https://www.freecodecamp.org/news/comment-out-html-code-example/)
* [Commentaire HTML – Comment commenter une ligne ou une balise en HTML](https://www.freecodecamp.org/news/html-comment-how-to-comment-out-a-line-or-tag-in-html/)

## Élément principal

L'élément `main` est utilisé pour regrouper tout le contenu principal de la page Web.

```html
<h1>Ce que freeCodeCamp a à offrir</h1>
<main>
  <p>Le programme principal de freeCodeCamp enseigne le développement full stack JavaScript et Python. Il y a des centaines de leçons à parcourir pour vous préparer à un emploi de développeur de niveau débutant.</p>

  <p>freeCodeCamp a des milliers d'articles gratuits sur leur publication d'actualités. Ils ont également des centaines de vidéos sur leur chaîne YouTube.</p>
</main>
```

Voici à quoi ressemble le code rendu sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-18-at-10.34.18-PM.png)

Pour en savoir plus sur l'élément `main`, veuillez lire [cette explication détaillée de l'élément `main` DevDocs](https://devdocs.io/html/element/main).

## Indentation HTML

Lorsque vous avez des éléments HTML imbriqués dans d'autres éléments HTML, il est préférable d'utiliser l'indentation. Les éléments imbriqués sont connus comme les enfants de leur élément parent.

L'indentation est utilisée pour rendre votre code plus lisible par d'autres développeurs. Pour indenter votre code, vous déplacerez l'élément de deux espaces vers la droite.

Voici un exemple **sans** indentation.

```html
<main>
<h2>Apprenons l'indentation</h2>
<p>Il n'y a pas d'indentation ici</p>
</main>
```

Mais si j'édite le code en déplaçant les éléments `h2` et `p` de deux espaces vers la droite, nous avons maintenant une indentation correcte.

```html
<main>
  <h2>Apprenons l'indentation</h2>
  <p>Voici l'indentation</p>
</main>
```

Maintenant, nous pouvons voir que les éléments `h2` et `p` sont des enfants de l'élément `main`.

Pour en savoir plus sur l'indentation HTML et pourquoi elle est importante, veuillez lire [cet article utile sur l'indentation](https://www.freecodecamp.org/news/how-to-indent-in-html-and-why-it-is-important/).

## Éléments d'image

Les éléments `img` sont utilisés pour ajouter des images à la page Web.

L'attribut `src` représente l'emplacement de l'image et l'attribut `alt` est le texte descriptif pour l'image.

```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg" alt="assiette de lasagnes">
```

Voici à quoi ressemble le code rendu sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-18-at-11.41.23-PM.png)

Pour en savoir plus sur l'élément `img`, veuillez lire [ce tutoriel utile sur l'élément `img`](https://www.freecodecamp.org/news/img-html-image-tag-tutorial/).

## Éléments d'ancrage

Un élément d'ancrage représente un lien sur la page Web.

Voici la syntaxe de base :

```html
<a href="lien-ou-vous-voulez-aller">le texte d'ancrage va ici</a>
```

Voici à quoi cela ressemble rendu sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-5.10.07-PM.png)

Vous utilisez l'attribut `href` pour indiquer à l'hyperlien où aller.

```html
href="lien-ou-vous-voulez-aller"
```

Le texte d'ancrage est ce qui est affiché à l'écran pour les utilisateurs.

Voici un exemple de balise d'ancrage qui mène à freeCodeCamp.

```html
<a href="https://www.freecodecamp.org/">freeCodeCamp</a>
```

Voici à quoi cela ressemble rendu sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-5.41.36-PM.png)

Pour en savoir plus sur les éléments d'ancrage HTML, je suggère de lire ces articles utiles.

* [La balise HTML <a> – Exemple de code de balise d'ancrage](https://www.freecodecamp.org/news/the-html-a-tag-anchor-tag-example-code/)
* [Balise HTML <a> – Exemple de lien d'ancrage HREF](https://www.freecodecamp.org/news/html-a-tag-anchor-link-href-example/)

## Intégration d'éléments d'ancrage dans des paragraphes

Si vous souhaitez inclure des liens dans vos paragraphes, vous pouvez imbriquer des balises d'ancrage dans les balises de paragraphe.

Dans cet exemple, nous avons le texte "J'adore freeCodeCamp".

```html
<p>J'adore freeCodeCamp</p>
```

Si je voulais transformer le mot freeCodeCamp en un lien, je l'envelopperais dans un ensemble de balises d'ancrage.

```html
<p>J'adore <a href="https://www.freecodecamp.org/">freeCodeCamp</a></p>
```

Voici à quoi ressemble le résultat rendu à l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-8.53.45-PM.png)

L'imbrication de liens dans des balises de paragraphe est utile lorsque vous souhaitez diriger vos utilisateurs vers des informations supplémentaires concernant le contenu principal de la page.

Pour en savoir plus sur l'imbrication de balises d'ancrage dans des paragraphes, je suggère de lire cet article utile.

* [Lien HTML – Comment transformer une image en lien et imbriquer des liens dans des paragraphes](https://www.freecodecamp.org/news/how-to-turn-text-and-images-into-links-using-html/)

## Attributs de cible

Vous utilisez l'attribut `target="_blank"` dans la balise d'ancrage d'ouverture comme ceci :

```html
<a href="lien-du-site-web" target="_blank">
```

Lorsque l'utilisateur clique sur le lien, un nouvel onglet du navigateur s'ouvre automatiquement sur cette page.

Dans cet exemple, j'ai imbriqué un lien dans un ensemble de balises de paragraphe pour diriger les gens vers freeCodeCamp.

```html
<p>Pour apprendre à coder gratuitement, veuillez visiter <a href="https://www.freecodecamp.org/learn" target="_blank">freeCodeCamp.org</a></p>
```

Lorsque vous cliquez sur le lien freeCodeCamp, un nouvel onglet du navigateur s'ouvre pour vous.

%[https://codepen.io/jessica-wilkins/pen/zYRRdmQ]

Pour en savoir plus sur l'attribut de cible, je suggère de lire cet article utile.

* [Comment ouvrir un lien dans un nouvel onglet – Attribut HTML target blank expliqué](https://www.freecodecamp.org/news/how-to-open-a-link-in-a-new-tab/)

## Intégration d'images dans des balises d'ancrage

En HTML, nous pouvons utiliser l'élément `<img>` pour ajouter des images sur la page. Dans cet exemple, nous ajoutons une image de cinq chats.

```html
<img  src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"  alt="Cinq chats regardant autour d'un champ."/>
```

![Screen-Shot-2022-06-02-at-10.39.02-PM](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-02-at-10.39.02-PM.png)

Si nous voulions faire de cette image un lien cliquable, nous pourrions la placer à l'intérieur d'un ensemble de balises d'ancrage.

```html
<a href="https://en.wikipedia.org/wiki/Cat"><img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Cinq chats regardant autour d'un champ."/></a>
```

Nous pouvons également ajouter l'attribut `target="_blank"` pour que ce lien s'ouvre dans un nouvel onglet.

```html
<a target="_blank" href="https://en.wikipedia.org/wiki/Cat"><img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Cinq chats regardant autour d'un champ." /></a>
```

Lorsque vous passez votre souris sur l'image, vous verrez le pointeur du curseur indiquant qu'il s'agit d'un lien vous dirigeant vers un article sur les chats.

%[https://codepen.io/jessica-wilkins/pen/XWZYRgy]

## Éléments de section

L'élément `section` est utilisé pour regrouper des sections de contenu dans le document HTML.

Voici un exemple de l'élément `section`.

```html
<h1>Apprenons les éléments de section</h1>
<section>
  <h2>Définition</h2>
  <p>L'élément de section est utilisé pour regrouper des sections de contenu dans le document HTML.</p>
</section>
```

Voici à quoi ressemble le résultat rendu sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-9.34.22-PM.png)

Pour en savoir plus sur les éléments `section`, veuillez lire [cette explication détaillée de l'élément `section` DevDocs](https://devdocs.io/html/element/section).

## Éléments de liste non ordonnée

L'élément de liste `ul` est utilisé pour afficher une liste d'éléments dans aucun ordre particulier. L'élément `li` représente l'élément de liste individuel.

Voici un exemple de liste d'éléments alimentaires.

```html
<h2>Aliments préférés</h2>
<ul>
  <li>Salade</li>
  <li>Pizza</li>
  <li>Hamburger</li>
  <li>Carottes</li>
</ul>
```

Voici à quoi cela ressemble rendu à l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-10.07.42-PM.png)

Pour en savoir plus sur l'élément de liste non ordonnée, veuillez lire cet article utile.

* [Puces HTML – Comment créer une liste non ordonnée avec l'exemple de balise <ul>](https://www.freecodecamp.org/news/html-bullet-points-how-to-create-an-unordered-list-with-the-ul-tag-example/)

## Éléments Figure et Figcaption

L'élément `figure` représente un contenu autonome qui est souvent utilisé avec des images et des légendes. La légende `figcaption` est un texte descriptif court pour l'image.

Dans cet exemple, nous avons une image de cinq chatons dans l'herbe avec une petite légende en dessous.

```html
<figure>
  <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Cinq chats regardant autour d'un champ." />
  <figcaption>Cinq chatons regardant autour dans l'herbe</figcaption>
</figure>
```

Voici à quoi cela ressemble rendu sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-10.24.35-PM.png)

Pour en savoir plus sur les éléments `figure` et `figcaption`, veuillez lire [cette explication utile de DevDocs](https://devdocs.io/html/element/figure).

## Éléments d'emphase

L'élément `em` est utilisé pour placer un accent supplémentaire sur une section de texte.

Dans cet exemple, nous avons la phrase : "Nous devons sortir du bâtiment maintenant !"

```html
<p>Nous devons sortir du bâtiment maintenant !</p>
```

Si je voulais mettre l'accent sur le mot maintenant, je pourrais l'envelopper dans des balises `<em>`.

```html
<p>Nous devons sortir du bâtiment <em>maintenant</em> !</p>
```

Voici à quoi ressemble le résultat rendu sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-10.38.35-PM.png)

Pour en savoir plus sur les éléments d'emphase, veuillez lire cette explication utile de DevDocs.

* [L'élément Emphasis](https://devdocs.io/html/element/em)

## Éléments de liste ordonnée

L'élément `ol` est utilisé pour afficher une liste d'éléments dans un ordre particulier. L'élément `li` représente l'élément de liste individuel.

Voici un exemple d'un ensemble d'étapes pour une recette.

```html
<h1>Comment faire un gâteau</h1>
<h2>Instructions pour la recette</h2>
<ol>
  <li>Préchauffer le four</li>
  <li>Fouetter la farine, le sucre et le cacao dans un bol</li>
  <li>Mélanger le lait, l'huile végétale, les œufs et la vanille</li>
  <li>Cuire au four pendant 30 minutes</li>
  <li>Sortir du four, laisser refroidir pendant 10 minutes et glacer le gâteau</li>
</ol>
```

Voici à quoi ressemble le résultat rendu sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-25-at-10.53.18-PM.png)

Pour en savoir plus sur les éléments de liste ordonnée, veuillez lire cet article utile.

* [Liste ordonnée en HTML – Exemple de balise OL](https://www.freecodecamp.org/news/ordered-list-in-html-ol-tag-example/)

## Éléments Strong

Les éléments Strong sont des sections de texte qui représentent un sentiment d'urgence ou de sérieux.

Dans cet exemple, nous avons la phrase suivante :

```html
<p>Danger ! Zone non sécurisée devant</p>
```

Nous pouvons utiliser les balises `strong` pour souligner le fort sentiment de sérieux du mot "Danger".

```html
<p><strong>Danger !</strong> Zone non sécurisée devant</p>
```

Voici à quoi ressemble le résultat rendu sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-26-at-8.41.09-AM.png)

## Éléments de formulaire

Les éléments de formulaire sont utilisés pour collecter des données d'un utilisateur comme des noms et des adresses e-mail. Des exemples de formulaires pourraient être des formulaires d'enquête ou des formulaires pour rejoindre une liste de diffusion.

Voici la syntaxe de base pour un formulaire :

```html
<form action="url-ou-les-donnees-doivent-etre-envoyees">
  <!--les entrées vont ici-->
</form>
```

L'attribut `action` est l'URL où les données de l'utilisateur seront envoyées. À l'intérieur des balises `form`, il y aura des entrées où l'utilisateur fournit ses informations.

Les entrées seront couvertes plus en détail dans la section suivante.

## Champs de texte de formulaire et boutons de soumission

L'entrée de texte `input` est un champ de texte où les utilisateurs peuvent entrer leurs informations. Ces entrées vont à l'intérieur de l'élément `form`.

Voici la syntaxe de base :

```html
<form action="url-ou-les-donnees-doivent-etre-envoyees">
  <input type="text">
</form>
```

`type="text"` indique à l'ordinateur qu'il s'agit d'une entrée de texte.

Voici à quoi ressemble le résultat rendu sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-26-at-9.44.59-AM.png)

L'attribut `name` est utilisé pour représenter la valeur des données soumises.

```html
<input type="text" name="username">
```

Le texte `placeholder` est utilisé pour fournir aux utilisateurs des informations sur ce qui doit aller dans les entrées de texte.

Dans cet exemple, le texte de l'espace réservé montre aux utilisateurs un exemple de nom d'utilisateur. Une fois que vous commencez à taper dans l'entrée, le texte de l'espace réservé disparaît.

```html
  <input type="text" name="username" placeholder="Ex.codergirlrules">
```

%[https://codepen.io/jessica-wilkins/pen/oNqvBmb]

Le bouton de soumission est utilisé pour soumettre les informations du formulaire au serveur. `type="submit"` indique à l'ordinateur de quel type de bouton il s'agit.

```html
<button type="submit">Soumettre le formulaire</button>
```

L'attribut `required` est utilisé pour s'assurer qu'un utilisateur doit remplir les entrées requises avant de soumettre le formulaire. Si vous essayez de soumettre un formulaire sans avoir complété les entrées requises, un message s'affichera vous dirigeant pour remplir ces informations.

```html
  <input required type="text" name="username" placeholder="Ex.codergirlrules">
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-26-at-10.00.04-AM.png)

Pour en savoir plus sur les entrées de formulaire, veuillez lire cet article.

* [Formulaire HTML – Exemple de type d'entrée et de bouton de soumission](https://www.freecodecamp.org/news/html-form-input-type-and-submit-button-example/)

## Boutons radio de formulaire

Les boutons radio représentent un groupe d'options parmi lesquelles un utilisateur peut choisir. Une seule option dans ce groupe peut être sélectionnée à la fois.

Voici la syntaxe de base :

```html
<input type="radio">
```

Voici à quoi cela ressemble rendu à l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-26-at-10.20.33-PM.png)

Dans cet exemple, nous utilisons un groupe de boutons radio où l'utilisateur peut choisir entre bœuf, poulet, poisson ou autre. Lorsque vous utilisez un groupe de boutons radio, tous les boutons du groupe doivent avoir la même valeur pour l'attribut `name`.

```html
<input type="radio" id="beef" name="food">Bœuf
<input type="radio" id="chicken" name="food">Poulet
<input type="radio" id="fish" name="food">Poisson
<input type="radio" id="other" name="food">Autre
```

Essayez l'exemple ci-dessous et remarquez comment vous ne pouvez sélectionner qu'une seule option à la fois. Remarquez comment toutes les entrées ont la même valeur `name="food"`.

%[https://codepen.io/jessica-wilkins/pen/yLKBPzE?editors=1000]

Vous pouvez en savoir plus sur les boutons radio en lisant [cette documentation sur les boutons radio de DevDocs](https://devdocs.io/html/element/input/radio).

## Éléments de label

L'élément `label` associe le texte de l'étiquette à l'entrée.

Voici un exemple d'utilisation de l'élément `label` pour associer le texte "Bœuf" à l'entrée.

```html
  <label for="beef">Bœuf</label>
  <input type="radio" id="beef" name="food">
```

L'attribut `for` est utilisé pour connecter l'étiquette à l'entrée afin que lorsque l'utilisateur clique sur le texte de l'étiquette, il sélectionne l'entrée. La valeur de l'attribut `for` est la même que l'`id` de l'entrée.

Essayez l'exemple ci-dessous en cliquant sur le texte de l'étiquette. Vous verrez que l'entrée radio est sélectionnée.

%[https://codepen.io/jessica-wilkins/pen/vYRBWdG?editors=1000]

Vous pouvez également imbriquer l'entrée à l'intérieur de l'élément `label`. Dans ce cas, vous n'avez pas besoin d'utiliser l'attribut `for` car l'association entre les deux éléments est implicite.

```html
  <label>Bœuf
    <input type="radio" id="beef" name="food">
  </label>
```

Pour en savoir plus sur l'élément `label`, veuillez lire cet article utile.

* [Label HTML – Exemple de balise Label](https://www.freecodecamp.org/news/html-label-label-tag-example/)

## Éléments Fieldset et Legend

L'élément `fieldset` est utilisé pour regrouper les contrôles de formulaire qui sont des entrées et des étiquettes. L'élément `legend` est utilisé pour fournir une légende pour l'élément `fieldset`.

Voici un exemple de l'élément `fieldset` :

```html
<form action="">
  <fieldset>

  </fieldset>
</form>
```

Voici à quoi cela ressemble rendu à l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-26-at-11.42.04-PM.png)

Voici un exemple de l'élément `legend` :

```html
<form action="">
  <fieldset>
    <legend>Choisissez votre langage de programmation préféré</legend>
  </fieldset>
</form>
```

Voici à quoi cela ressemble rendu à l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-26-at-11.43.51-PM.png)

Voici l'exemple complet de la façon dont les éléments `fieldset` et `legend` fonctionnent avec les entrées et les étiquettes de formulaire.

```html
<form action="">
  <fieldset>
    <legend>Choisissez votre langage de programmation préféré</legend>
      
    <input type="radio" id="JavaScript" name="programming">
    <label for="JavaScript">JavaScript</label>

    <input type="radio" id="Python" name="programming">
    <label for="Python">Python</label>

    <input type="radio" id="Rust" name="programming">
    <label for="Rust">Rust</label>
  </fieldset>
</form>
```

%[https://codepen.io/jessica-wilkins/pen/GRxKypM?editors=1000]

## Éléments de case à cocher de formulaire

Les éléments `checkbox` sont des cases où un utilisateur peut sélectionner plusieurs options dans un formulaire.

Voici un exemple de case à cocher :

```html
    <input type="checkbox" id="London" name="London">
    <label for="London">Londres</label>
```

Voici à quoi cela ressemble rendu sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-27-at-12.14.29-AM.png)

Voici un exemple complet utilisant plusieurs cases à cocher pour différentes villes.

```html
<form action="">
  <fieldset>
    <legend>Villes que vous aimeriez visiter</legend>

    <input type="checkbox" id="London" name="London">
    <label for="London">Londres</label>

    <input type="checkbox" id="Barcelona" name="Barcelona">
    <label for="Barcelona">Barcelone</label>

    <input type="checkbox" id="Venice" name="Venice">
    <label for="Venice">Venise</label>

    <input type="checkbox" id="Tokyo" name="Tokyo">
    <label for="Tokyo">Tokyo</label>
  </fieldset>
</form>
```

Essayez l'exemple ci-dessous et vous pourrez sélectionner plusieurs options.

%[https://codepen.io/jessica-wilkins/pen/wvmwpeE?editors=1000]

Pour en savoir plus sur les éléments de case à cocher, veuillez lire [la documentation sur les cases à cocher de DevDocs](https://devdocs.io/html/element/input/checkbox).

## Attributs de valeur et vérifiés

L'attribut `value` représente la valeur de l'entrée.

Voici un exemple.

```html
<input type="checkbox" id="London" name="London" value="London">
```

L'attribut `checked` est utilisé pour indiquer quelles entrées doivent être cochées par défaut au chargement de la page.

Voici un exemple.

```html
    <input type="checkbox" id="London" name="London" value="London" checked>
    <label for="London">Londres</label>
```

Voici à quoi ressemble le résultat rendu sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-27-at-12.42.20-AM.png)

## Éléments de pied de page

L'élément `footer` est situé en bas du document HTML et contient des informations comme les droits d'auteur, ou des liens vers d'autres informations liées à la page.

Voici un exemple de base :

```html
<footer>
  <p>
9 2022 Jessica Wilkins</p>
</footer>
```

Pour en savoir plus sur l'élément `footer`, veuillez lire [cette explication de l'élément `footer` par DevDocs](https://devdocs.io/html/element/footer).

## Éléments Head et title

Les balises `<head>` contiennent des informations qui sont traitées par les machines. À l'intérieur des balises `<head>`, vous imbriquerez des métadonnées qui sont des données décrivant le document à la machine.

```html
<head>
  <!--les métadonnées importantes vont ici-->
  <!--l'élément title va également ici-->
</head>
```

La balise `<title>` est le titre de la page Web. Ce texte est affiché dans la barre de titre du navigateur.

```html
    <title>Modèle HTML 5</title>

```

![Screen-Shot-2021-07-30-at-4.15.25-AM](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-30-at-4.15.25-AM.png)

Voici un exemple de ce à quoi un `head` pourrait ressembler sur une vraie page Web. Aucune de ces informations n'est affichée sur la page Web elle-même.

```html
 <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Modèle HTML 5</title>
    <link rel="stylesheet" href="style.css">
  </head>
```

Pour une description détaillée de chaque balise meta listée, veuillez lire [cet article sur un modèle HTML5](https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/).

## Attribut `lang`

L'attribut `lang` à l'intérieur de la balise `<html>` d'ouverture définit la langue de la page. Il est également bon de l'inclure pour des raisons d'accessibilité, car les lecteurs d'écran sauront comment prononcer correctement le texte.

```html
<html lang="en">
```

## DOCTYPE

La première ligne de votre code HTML doit être la déclaration de type de document. Un doctype indique au navigateur quelle version de HTML la page est écrite.

```html
<!DOCTYPE html>
```

Si vous oubliez d'inclure cette ligne de code dans votre fichier, alors certaines des balises HTML 5 comme `<article>`, `<footer>`, et `<header>` peuvent ne pas être supportées par le navigateur.