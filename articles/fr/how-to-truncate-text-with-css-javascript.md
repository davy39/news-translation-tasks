---
title: Comment tronquer du texte avec CSS et JavaScript
subtitle: ''
author: David Fagbuyiro
co_authors: []
series: null
date: '2023-04-04T18:06:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-truncate-text-with-css-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-pixabay-261763.jpg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment tronquer du texte avec CSS et JavaScript
seo_desc: "CSS is a powerful tool to have in your programming toolkit. It offers numerous\
  \ features that allow you to create responsive and attractive websites. \nSometimes\
  \ you might see an ellipsis (...) that appears to indicate that some content or\
  \ text is hidd..."
---

[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) est un outil puissant à avoir dans votre boîte à outils de programmation. Il offre de nombreuses fonctionnalités qui vous permettent de créer des sites web réactifs et attrayants. 

Parfois, vous pouvez voir une ellipsis (...) qui apparaît pour indiquer que certains contenus ou textes sont cachés. Vous êtes-vous déjà demandé comment vous pouvez coder cette fonctionnalité ?

Dans ce tutoriel, nous allons voir comment faire des tronçages multi-lignes en `CSS` en utilisant [JavaScript](https://developer.mozilla.org/en-US/docs/Web/javascript). Commençons !

## Qu'est-ce que la tronçage de texte ?

En CSS, la tronçage de texte est utilisée pour tronquer le texte qui dépasse de son conteneur en cachant le contenu supplémentaire et en le remplaçant par des ellipses. Cette technique est utile pour créer des mises en page plus compactes et visuellement attrayantes dans des situations où la longueur du texte peut varier, comme dans les menus de navigation, les cellules de tableau ou les en-têtes.

La propriété CSS que vous utilisez pour la tronçage de texte est `text-overflow`. Pour activer la tronçage de texte, vous devez définir la propriété `text-overflow` sur "ellipsis" et la propriété `white-space` sur `nowrap` pour empêcher le texte de `wrapping` à la ligne suivante. Vous devrez peut-être également définir la propriété `overflow` sur "hidden" pour cacher tout texte qui `overflows` le conteneur.

Discutons maintenant de ces propriétés plus en détail.

## Propriétés CSS pour tronquer le texte

Différentes propriétés en CSS peuvent être utilisées pour tronquer le texte. Voici quelques-unes des propriétés CSS les plus courantes :

`text-overflow` : Cette propriété spécifie comment le contenu textuel doit être affiché lorsqu'il dépasse la zone de contenu de l'élément. La propriété `text-overflow` peut prendre l'une des valeurs suivantes :

* `clip` : Si le texte dépasse la zone de contenu de l'élément, il est rogné et non affiché.
* `ellipsis` : Si le texte dépasse la zone de contenu de l'élément, il est tronqué et une ellipsis (...) est insérée à la fin.
* `fade` : Si le texte dépasse la zone de contenu de l'élément, il est tronqué et un effet de fondu est ajouté à la fin.

`white-space` : Cette propriété contrôle comment les caractères d'espace blanc dans le texte sont traités. L'attribut white-space a les qualités possibles suivantes :

* `normal` : Le navigateur cassera les lignes de texte pour s'adapter à l'espace disponible.
* `nowrap` : Le navigateur ne cassera pas les lignes de texte, ce qui peut faire déborder le texte de la zone de contenu de l'élément.
* `pre` : Le navigateur préservera les caractères d'espace blanc, ce qui peut faire déborder le texte de la zone de contenu de l'élément.

`overflow` : Cette propriété spécifie comment le contenu débordant doit être géré. La propriété overflow peut prendre l'une des valeurs suivantes :

* `visible` : Le contenu débordant est visible et non rogné.
* `hidden` : Le contenu débordant est caché et non visible.
* `scroll` : Le contenu débordant est visible et des barres de défilement sont ajoutées pour permettre le défilement.
* `auto` : Le contenu débordant est visible et des barres de défilement sont ajoutées à l'élément uniquement si le contenu déborde.

Pour tronquer le texte, vous pouvez utiliser la propriété `text-overflow` en combinaison avec les propriétés `white-space` et `overflow`.

## Tronçage dynamique

Vous pouvez également implémenter une tronçage dynamique en utilisant CSS pour afficher le contenu textuel sur une page web. Un cas d'utilisation courant pour la tronçage dynamique avec CSS est de limiter la quantité de texte affichée dans un conteneur tout en fournissant un lien ou un bouton "lire la suite" pour permettre aux utilisateurs d'étendre le contenu.

Voici un exemple de code HTML et CSS qui implémente le CSS dynamique dans la tronçage de texte, avec une bordure autour du texte pour indiquer sa largeur :

Le code HTML :

```html
<html>
  <body>
    <div class="list">
      <div class="card">
        <h3>Premier Exemple</h3>
        <p class="text single-line">
          mollis, ante non euismod ornare, orci diam ornare orci, eu mattis
          tortor lectus at erat. Nam rutrum erat nec euismod lacinia. Curabitur
          et velit ut mauris euismod tempus. Fusce pharetra augue lectus, quis
          maximus quam auctor pellentesque.  
        </p>
      </div>
      <div class="card">
        <h3>Deuxième Exemple</h3>
        <p class="text single-line">
          Curabitur pharetra, erat a gravida malesuada, augue mi tincidunt odio,
          quis rhoncus tortor metus ut purus. Nunc lectus quam, tempus sed
          mollis id, feugiat a quam. Donec posuere nulla a lacus interdum
          faucibus ut tincidunt nisi. 
        </p>
      </div>
    </div>
  </body>
</html> <body>
    <div class="list">
        <div class="card">
          <h3>Premier Exemple</h3>
          <p class="text single-line">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam augue nulla, elementum non erat id, cursus feugiat sem. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nullam velit neque, tincidunt in ipsum vel, accumsan mattis nisi. 
          </p>
        </div>
            <div class="card">
          <h3>Deuxième Exemple</h3>
          <p class="text single-line">
            Curabitur pharetra, erat a gravida malesuada, augue mi tincidunt odio, quis rhoncus tortor metus ut purus. Nunc lectus quam, tempus sed mollis id, feugiat a quam. Donec posuere nulla a lacus interdum faucibus ut tincidunt nisi. Curabitur consequat vitae turpis quis lobortis. 
          </p>
        </div>
      </div>
      
</body>
</html>

```

Voici le rendu du code HTML sans ajouter le CSS :

![Image](https://i.imgur.com/MKWdlrN.png)

Voici le code CSS pour tronquer le texte débordant :

```css
.list {
  display: flex;
  flex-direction: column;
}

.card {
  border: 1px solid #1948e3;
  border-radius: 8px;
  height: 100px;
  margin: 0 auto;
  padding: 15px 25px;
  width: 890px;
}

.card:not(:last-of-type) {
  margin-bottom: 20px;
}

.text.single-line {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

```

Voici le rendu de l'image du paragraphe après avoir lié le code CSS ci-dessus avec celui-ci :

![Image](https://i.imgur.com/BQJZJeN.png)

Voici un GIF montrant le comportement du texte après l'avoir lié avec CSS pour tronquer le texte dynamiquement :

![Image](https://i.imgur.com/wQysyoe.gif)

## Comment créer un texte tronqué multi-lignes

Les propriétés CSS tronquent efficacement une seule ligne de texte ou un texte multi-lignes s'étendant sur deux lignes ou moins. Mais il est également possible de réaliser une tronçage de texte pour un texte multi-lignes en utilisant JavaScript.

Dans les sections suivantes, nous explorerons deux techniques pour la tronçage de texte multi-lignes, l'une utilisant CSS et l'autre utilisant JavaScript. En examinant les deux approches, vous pouvez décider quelle technique est la mieux adaptée à vos besoins.

### Comment utiliser CSS pour tronquer le texte multi-lignes

Les propriétés CSS fonctionnent bien pour une seule ligne de texte et un texte multi-lignes qui s'étend sur plus de deux lignes.

La première étape consiste à spécifier la hauteur de la `boîte ou de l'élément`. Ensuite, nous multiplions la `line-height` par le nombre de lignes que nous souhaitons ignorer avant la tronçage pour obtenir la `max-height`.

Voici comment cela se fait :

```html
<body>
  <h3>Débordement de tronçage de texte multi-lignes !</h3>

  <p class="truncate-overflow">
    Lorem ipsum dolor sit, amet consectetur adipisicing elit. In sint facilis
    explicabo voluptatum exercitationem earum. Quibusdam vitae, iusto temporibus
    corrupti tempore distinctio soluta reiciendis. Ab aspernatur facilis autem
    temporibus veniam.
  </p>

  <p class="truncate-overflow">
    La tronçage de texte multi-lignes est un modèle de conception courant qui permet aux concepteurs de montrer une quantité limitée de texte sur une page web ou une application, tout en donnant aux utilisateurs la possibilité de voir plus s'ils le souhaitent.
  </p>

  <p class="truncate-overflow">
    En CSS, il existe plusieurs façons de tronquer le texte multi-lignes, y compris l'utilisation de la propriété text-overflow en combinaison avec display, white-space et overflow.
  </p>
</body>

```

Voici le rendu de l'image du code HTML ci-dessus :

![Image](https://i.imgur.com/EDkUWHB.png)

Maintenant, définissons le `Overflow` sur `hidden` et le `max-height` sur notre hauteur préférée, la même que la `line-height`.

Ensuite, nous avons `-webkit-box-orient` défini sur `vertical`, `-webkit-line-clamp` et `text-overflow` défini sur `ellipsis`. Nous allons également changer le `display` en `box` :

```css
:root {
  --lh: 1.4rem;
}

html {
  max-width: 22rem;
  margin: 2rem auto;
  line-height: var(--lh);
}

.truncate-overflow {
  --max-lines: 3;
  position: relative;
  max-height: calc(var(--lh) * var(--max-lines));
  overflow: hidden;
  padding-right: 1rem;
}
.truncate-overflow::before {
  position: absolute;
  content: "...";
  bottom: 0;
  right: 0;
}
.truncate-overflow::after {
  content: "";
  position: absolute;
  right: 0;
  width: 1rem;
  height: 1rem;
  background: white;
}

```

Voici une image montrant la tronçage de texte multi-lignes avec du CSS pur :

![Image](https://i.imgur.com/vYBjwVF.png)

### Comment utiliser JavaScript pour tronquer le texte multi-lignes

JavaScript a également la capacité de tronquer le texte. Voici un exemple de la façon d'implémenter JavaScript pour tronquer le texte en fonction d'un certain nombre de caractères.

Voyons comment nous pouvons faire cela avec JavaScript. Pour commencer, définissons une fonction nommée `truncate` et passons les mots à tronquer en tant que paramètres. Nous fournirons également un `paramètre de longueur maximale`.

Voici un exemple de code HTML pour tronquer le texte avec JavaScript :

```html
<script src="Truncate.js"></script>
<body>
  <div>
    <h1>En-tête d'exemple de tronçage de texte</h1>
    <p id="text">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi in sapien
      eu velit eleifend ullamcorper eget vitae nulla. Aenean euismod purus sed
      neque dictum, nec lobortis ante faucibus.
    </p>
    <button onclick="truncateText()">Tronquer le texte</button>
  </div>
</body>

```

Voici le rendu de l'image du code HTML pur avant d'ajouter la fonction JavaScript et la fonction de bordure CSS :

![Image](https://i.imgur.com/KK4868S.png)

Voici le code JavaScript :

```javascript
function truncateText() {
  var text = document.getElementById("text").innerHTML;
  var truncated = text.substring(0, 50) + "...";
  document.getElementById("text").innerHTML = truncated;
}

```

Et voici le code CSS :

```css
#text {
  border: 1px solid black;
  padding: 10px;
}

```

Le code HTML de l'exemple contient un paragraphe `element` avec l'`ID` "text" qui contient un exemple de texte. La fonction `truncateText` dans le code JavaScript récupère le texte de l'élément de paragraphe. 

Avec ces modifications, lorsque le bouton "Tronquer le texte" est cliqué, le texte sera tronqué à 50 caractères et une bordure sera ajoutée au texte tronqué. Il insère également une `ellipsis` à la fin. 

La fonction est appelée lorsque l'utilisateur clique sur le bouton "Tronquer le texte", et le texte dans l'élément de paragraphe est remplacé par le contenu tronqué.

Voici le rendu de l'image après avoir ajouté à la fois le CSS et le JavaScript au code HTML ci-dessus :

![Image](https://i.imgur.com/xwijXlB.png)

Voici un GIF illustrant le rendu :

![Image](https://i.imgur.com/tkF6DQi.gif)

Cet exemple démontre une approche fondamentale pour tronquer le texte en utilisant JavaScript.

## Comment ajouter un élément après l'ellipsis

L'`Ellipsis` (...) est utilisé pour représenter une tronçage de texte, indiquant que certains contenus ont été omis de l'affichage. La propriété text-overflow est utilisée pour spécifier ce qui se passe avec le texte qui déborde du conteneur.

Voici un exemple avec le code HTML ci-dessous :

```html
<div class="parent-box box">
  <div class="child-box">
    Vous apprenez la tronçage de texte avec javascript, qui se fait avec ces
    trois étapes
  </div>
</div>

```

Voici le rendu de l'image du code HTML avant d'introduire l'ellipsis :

![Image](https://i.imgur.com/HD5eTPz.png)

Nous avons ajouté le `:after pseudo-element` à l'élément parent `element.box` pour accomplir cela. Le `nest div` est ensuite donné la `class.child-box` et un affichage `inline-block`. Cela permet à l'élément `.parent-box pseudo-element` d'apparaître après la largeur du `.child-box`.

Le `hidden overflow` est déclenché si la `max-width` définie est dépassée. Si il y a un `text-overflow`, nous pouvons avoir l'`ellipsis` et l'élément du `.parent-box`.  
Voici le code CSS pour ajouter un `Element` après l'`Ellipsis` :

```css
.box {
  margin: 10px;
  padding: 10px;
  border: 1px solid rgb(0, 0, 0);
  width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  position: relative; /* Ajoutez ceci pour vous assurer que l'élément ::after est positionné par rapport au parent */
}

.child-box::after {
  content: "+"; /* Changez le contenu pour l'élément souhaité */
  position: absolute;
  right: 0;
  bottom: 0;
}

.no-max-width {
  max-width: none;
}

```

Voici le rendu après avoir introduit le code ci-dessus :

![Image](https://i.imgur.com/gfYrZP4.png)

## Conclusion

Nous avons vu comment tronquer du texte en CSS en utilisant diverses approches CSS et JavaScript dans ce tutoriel. 

Nous avons également vu comment ajouter un `element` après l'`ellipsis`, ce qui peut être délicat dans certaines circonstances.