---
title: Guide du HTML sémantique – 10 alternatives à l'utilisation de divs
subtitle: ''
author: Edan Ben-Atar
co_authors: []
series: null
date: '2021-09-28T16:00:39.000Z'
originalURL: https://freecodecamp.org/news/semantic-html-alternatives-to-using-divs
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/How-To-Start-Freelancing-1.png
tags:
- name: Accessibility
  slug: accessibility
- name: HTML
  slug: html
seo_title: Guide du HTML sémantique – 10 alternatives à l'utilisation de divs
seo_desc: "Raise your hand if your typical HTML layout looks like this:\n<body>\n\
  \  <div class=\"header\" id=\"site-header\">\n    <div class=\"site-nav\">\n   \
  \   <ul>\n        <li><a href=\"/\">Home</a></li>\n        <li><a href=\"/\">About</a></li>\n\
  \        <li><a href=\"/\">Con..."
---

Levez la main si votre mise en page HTML typique ressemble à ceci :

```html
<body>
  <div class="header" id="site-header">
    <div class="site-nav">
      <ul>
        <li><a href="/">Accueil</a></li>
        <li><a href="/">À propos</a></li>
        <li><a href="/">Contact</a></li>
      </ul>
    </div>
  </div>
  <div class="content-wrap">
    <div class="intro">
      Ceci est l'introduction du site, qui est rempli de divs.
    </div>
  </div>
  <div class="container"></div>
</body>
```

Beaucoup d'entre nous utilisent l'élément `<div>` par défaut car c'est le moyen le plus rapide de construire une mise en page HTML. Il peut être tentant de simplement se débarrasser du balisage pour se concentrer sur les aspects plus intéressants comme le CSS ou le JavaScript.

Bien que la construction d'une mise en page complète dans un document en utilisant des éléments `<div>` puisse être la solution la plus évidente, cela peut créer des problèmes à long terme.

## Les problèmes liés à l'utilisation exclusive de `div`

Utiliser l'élément `<div>` en soi n'est pas un problème. Il sert un but et il n'y a aucune raison de ne pas l'utiliser.

Mais utiliser exclusivement des DIV dans votre HTML peut causer des problèmes pour vous et toute autre personne travaillant sur votre projet.

### Problèmes de lisibilité

Si vous avez déjà regardé le code de quelqu'un d'autre, ou même votre propre code des mois après l'avoir écrit, il peut être difficile de le parcourir s'il est peuplé uniquement d'éléments `<div>`.

Déchiffrer la mise en page peut prendre beaucoup plus de temps que nécessaire, ce qui est comme de la Kryptonite pour votre productivité. Essayer de trouver où se trouve la balise de fermeture `</div>` pour un bloc de code spécifique peut être fastidieux.

### Problèmes d'accessibilité

Respecter les considérations d'accessibilité ne concerne pas seulement la couleur, le contraste et les sous-titres. L'Organisation mondiale de la santé estime que 285 millions de personnes sont malvoyantes dans le monde : 39 millions sont aveugles et 246 millions ont une vision réduite.

C'est une autre raison pour laquelle il est important d'écrire votre HTML pour qu'il soit aussi accessible que possible, ce qui signifie écrire du code sémantique.

Les lecteurs d'écran ont besoin de contexte pour lire avec précision une page web à voix haute. Pour un lecteur d'écran, des éléments comme `<div>` et `<span>` ne signifient rien. Les divs sémantiques comme `<form>` et `<button>` sont plus faciles à analyser.

### Problèmes de cohérence

Si vous savez à quoi vous attendre lorsque vous travaillez sur un projet avec une équipe, vous serez beaucoup plus efficace. Vous aurez également tendance à avoir moins de bugs dans votre code.

Établir une norme pour l'utilisation du HTML sémantique a du sens car toute personne reprenant le projet comprendra plus facilement la mise en page.

De plus, lorsque vous commencez à appliquer ou à ajuster le CSS pour un document HTML, vous trouverez beaucoup plus rapide et facile de trouver des éléments spécifiques lorsque le HTML sémantique a été utilisé dans la mise en page.

### Problèmes de SEO

Lors de l'utilisation de balises sémantiques, les moteurs de recherche considéreront leur contenu comme des mots-clés importants pour influencer le classement de recherche de la page. [(MDN Web Docs)](https://developer.mozilla.org/en-US/docs/Glossary/Semantics)

Qu'est-ce que le HTML sémantique ?

La [définition la plus claire](https://www.w3schools.com/html/html5_semantic_elements.asp) du HTML sémantique que j'ai trouvée indique que :

> Un élément sémantique décrit clairement sa signification à la fois pour le navigateur et le développeur.

Utiliser le HTML sémantique, c'est comme la différence entre pointer un objet dans le ciel et dire : « Regarde, un objet ! » ou « Regarde, un avion ! »

Tout comme décrire des objets du monde réel facilite la communication quotidienne, le HTML sémantique facilite la lecture du code.

En fait, l'utilisation du HTML sémantique est notée comme faisant partie de la [norme HTML5](https://html.spec.whatwg.org/multipage/grouping-content.html#the-div-element) :

> Les auteurs sont fortement encouragés à considérer l'élément [div](https://html.spec.whatwg.org/multipage/grouping-content.html#the-div-element) comme un élément de dernier recours, pour lorsque aucun autre élément n'est approprié. L'utilisation d'éléments plus appropriés au lieu de l'élément `div` conduit à une meilleure accessibilité pour les lecteurs et à une maintenance plus facile pour les auteurs.

Par exemple, lequel est le plus facile à parcourir :

```html
<div class="quote" id="twain-quote">
  "Obtenez d'abord vos faits, puis vous pouvez les déformer comme vous le souhaitez." – Mark Twain
</div>
```

Ou

```html
<blockquote>
  "Obtenez d'abord vos faits, puis vous pouvez les déformer comme vous le souhaitez." – Mark Twain
</blockquote>
```

Dans le deuxième exemple, vous pouvez voir l'élément `<blockquote>`, qui est immédiatement compréhensible comme du texte qui doit être affiché dans un format de citation.

L'utilisation d'alternatives à `div` peut nécessiter un peu plus de réflexion, mais ce peu de planification supplémentaire avec le HTML sémantique en vaudra la peine à la fin.

## Alternatives à `div` en HTML

Parlons de certaines des alternatives les plus courantes à `div`. Il est probable que vous ayez déjà vu ces éléments, mais ici nous couvrirons exactement à quoi ils servent et comment les utiliser.

### L'élément `<nav>`

```html
<nav>
  <ul>
    <li><a href="/">Accueil</a></li>
    <li><a href="/">À propos</a></li>
    <li><a href="/">Contact</a></li>
  </ul>
</nav>
```

L'élément nav est exactement ce à quoi il ressemble. Vous utilisez cet élément pour délimiter un ensemble de liens de navigation.

Comme mentionné précédemment, cela permet également aux lecteurs d'écran de décider s'ils doivent afficher ou non ce type de contenu initialement. L'élément `nav` est mieux utilisé pour un bloc principal de liens de navigation dans le document.

### L'élément `<main>`

```html
<main>
  <h1>Le Parrain de tout le contenu</h1>
  <h2>Le Mariage</h2>
  <p>
    Pourquoi es-tu allé à la police ? Pourquoi n'es-tu pas venu me voir en premier ? Vito, comment trouves-tu mon petit ange ? N'est-elle pas belle ? Ne me dis pas que tu es innocent. Parce que cela insulte mon intelligence et me met très en colère. Je vois que tu as pris le nom de la ville. Quel était le nom de ton père ? L'hôtel, le casino. La famille Corleone veut te racheter.
  </p>
</main>
```

Similaire à `<nav>`, l'élément main est utilisé exactement comme il le suggère (la sémantique à l'œuvre encore une fois). Cet élément enveloppe les blocs de code qui spécifient le contenu principal de la page, ou du document. L'élément main vivra entre les balises d'ouverture et de fermeture `<body>`.

### L'élément `<section>`

```html
<section>
  <h1>Le Meilleur Sandwich de Tous les Temps</h1>
  <p>
    Le meilleur sandwich est un sandwich au mouton, à la laitue et à la tomate, où le mouton est tendre et maigre. Il est si savoureux, j'adore ça.
  </p>
</section>
```

L'élément `<section>` est un excellent exemple d'utilisation d'une alternative à `div` pour séparer le contenu.

Dans l'exemple ci-dessus, nous séparons une introduction et un paragraphe d'ouverture en deux sections. Trouver et styliser ces sections dans notre document CSS sera beaucoup plus rapide que de chercher une classe `<div>`.

### L'élément `<header>`

```html
<header>
  <img src="/" id="logo">
</header>
```

L'élément `<header>` est différent de l'élément `<head>` en ce sens que vous pouvez l'utiliser plusieurs fois tout au long du document.

Par exemple, vous pourriez utiliser un ensemble d'éléments `<header>` pour placer un logo et un autre ensemble pour décrire un en-tête pour un contenu spécifique, comme un article (plus sur cela plus tard).

### L'élément `<footer>`

```html
<footer>
  <p>© 2021 Tous droits réservés. Ne vole pas.</p>
  <p>Contact : <a href="mailto:jiffy@jiffysites.com">Email Jiffy !</a></p>
</footer>
```

Tout comme avec l'élément `<header>`, vous pouvez utiliser des éléments `<footer>` n'importe où dans votre document HTML.

Une utilisation typique de `<footer>` est pour les informations de copyright ou d'auteur. Vous pouvez également utiliser un élément footer comme une fermeture dans un élément `<section>`.

### Alternatives moins courantes à `div`

Il existe également des éléments que vous n'avez peut-être jamais vus ou que vous avez rarement vus. Mais ils sont utiles et les apprendre vous aidera à rendre votre code beaucoup plus lisible.

### L'élément `<aside>`

```html
<p>
  Mon émission de télévision préférée de tous les temps est The Muppet Show. C'est doux, drôle et brillant.
</p>
<aside>
  <h3>The Muppet Show</h3>
  <p>The Muppet Show a été créé par Jim Henson et diffusé de 1976 à 1981.</p>
</aside>
```

Au cinéma ou au théâtre, une aside est connue comme un procédé dramatique dans lequel un personnage parle au public, séparément du dialogue principal.

C'est exactement comment nous pouvons utiliser l'élément `<aside>` dans notre HTML. Nous faisons une notation qui est liée au contenu, mais que nous voulons garder séparée. Nous pouvons également l'utiliser dans une barre latérale.

### L'élément `<article>`

```html
<article>
  <h2>Les Grenouilles Muppets</h2>
  <p>
    Les grenouilles Muppets sont un groupe de grenouilles anthropomorphes qui apparaissent dans The Muppet Show. Elles sont connues pour leur humour et leur talent musical.
  </p>
</article>
```

L'élément `<article>` est utilisé pour encapsuler du contenu qui peut être distribué ou réutilisé de manière indépendante. Cela peut être un article de blog, un article de journal, un commentaire, etc.

### L'élément `<figure>` et `<figcaption>`

```html
<figure>
  <img src="muppet-frog.jpg" alt="Une grenouille Muppet">
  <figcaption>Une grenouille Muppet de The Muppet Show.</figcaption>
</figure>
```

L'élément `<figure>` est utilisé pour encapsuler du contenu multimédia, comme des images, des diagrammes, des illustrations, etc. L'élément `<figcaption>` est utilisé pour fournir une légende pour le contenu multimédia.

### L'élément `<time>`

```html
<p>La première diffusion de The Muppet Show était le <time datetime="1976-09-13">13 septembre 1976</time>.</p>
```

L'élément `<time>` est utilisé pour représenter une date ou une heure. Cela peut être utile pour les moteurs de recherche et les lecteurs d'écran pour comprendre le contexte temporel du contenu.

### L'élément `<mark>`

```html
<p>Les Muppets sont <mark>incroyablement populaires</mark> depuis des décennies.</p>
```

L'élément `<mark>` est utilisé pour mettre en évidence du texte qui est pertinent dans un contexte particulier. Cela peut être utile pour attirer l'attention sur des parties importantes du contenu.

## Conclusion

Utiliser des alternatives à `div` dans votre HTML peut sembler nécessiter un peu plus de réflexion au début, mais les avantages en termes de lisibilité, d'accessibilité, de cohérence et de SEO en valent largement la peine. En utilisant des éléments sémantiques, vous rendez votre code plus facile à comprendre et à maintenir, tout en améliorant l'expérience utilisateur pour tous les visiteurs de votre site.

Alors, la prochaine fois que vous serez tenté d'utiliser un `<div>`, demandez-vous si l'un de ces éléments sémantiques pourrait mieux convenir. Votre futur vous et vos collègues vous en remercieront ! 🚀

Pour en savoir plus sur le HTML sémantique, consultez les ressources suivantes :

- [MDN Web Docs sur les éléments sémantiques](https://developer.mozilla.org/fr/docs/Web/HTML/Element)
- [W3Schools sur les éléments sémantiques HTML5](https://www.w3schools.com/html/html5_semantic_elements.asp)
- [Spécification HTML5 sur les éléments de regroupement de contenu](https://html.spec.whatwg.org/multipage/grouping-content.html)

Bon codage ! 💻💡