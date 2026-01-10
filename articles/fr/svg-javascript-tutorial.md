---
title: Tutoriel SVG + JavaScript – Comment coder une montre animée
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2021-12-23T17:19:15.000Z'
originalURL: https://freecodecamp.org/news/svg-javascript-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/SVG-Watch.001.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: SVG
  slug: svg
seo_title: Tutoriel SVG + JavaScript – Comment coder une montre animée
seo_desc: 'Since SVG images can be inlined in HTML, we can manipulate them with JavaScript.
  This means that we can animate parts of an image from code, make it interactive,
  or turn things around and generate graphics from data.

  In this example, we are going to ...'
---

Puisque les images SVG peuvent être intégrées en ligne dans le HTML, nous pouvons les manipuler avec JavaScript. Cela signifie que nous pouvons animer des parties d'une image à partir du code, la rendre interactive ou inverser les choses et générer des graphiques à partir de données.

Dans cet exemple, nous allons créer une montre. Nous utiliserons SVG pour dessiner la montre et JavaScript pour animer les aiguilles.

Ce tutoriel est un peu plus avancé, approfondissant certaines des propriétés SVG moins évidentes et se concentrant sur l'animation avec JavaScript. Si vous souhaitez obtenir un aperçu plus général des SVG, consultez mon [article précédent](https://www.freecodecamp.org/news/svg-tutorial-learn-to-code-images/) où nous passons en revue le code de 7 images SVG simples.

Vous pouvez également [regarder cet article sous forme de vidéo](https://www.youtube.com/watch?v=ULomsOSk4JA) avec un peu plus de contenu. Dans la vidéo, nous couvrons également l'interaction.

## **SVG dans HTML**

Dans l'article précédent, nous avons appris que les images SVG peuvent être intégrées en ligne dans un document HTML. Nous avons parlé de la balise SVG elle-même, qui définit la taille de l'image et le placement des éléments de l'image.

Les éléments de l'image sont placés dans l'image par leur position. La `viewBox` définit comment ces positions doivent être interprétées.

Les deux premiers nombres de la propriété définissent la position dans le coin supérieur gauche. Avec la taille définie par les deux derniers nombres, ils forment un système de coordonnées.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/SVG-Watch.001-1.jpeg)

```html
<html>
  <head>
    <title>Montre</title>
    <link rel="stylesheet" href="./index.css" />
  </head>

  <body>
    <svg width="200" height="200" viewBox="-100 -100 200 200">
      <circle
        cx="0"
        cy="0"
        r="90"
        fill="transparent"
        stroke="#f0f0c9"
        stroke-width="7"
      />
    </svg>

    <script src="./index.js"></script>
  </body>
</html>
```

Dans cet exemple, nous centrons le système de coordonnées. La coordonnée `0,0` est au milieu de l'image. Nous définissons avec la `viewBox` que le coin supérieur gauche doit être la coordonnée `-100,-100` et que la largeur et la hauteur doivent être de 200 unités.

Dans cet exemple, la taille définie par `width` et `height` et la taille définie par `viewBox` sont les mêmes. Cela signifie qu'une unité dans l'image sera un pixel dans le navigateur. Ce n'est pas toujours vrai. Si les deux ne correspondent pas, l'image est mise à l'échelle vers le haut ou vers le bas.

## **Comment créer les aiguilles des minutes et des heures de la montre**

Maintenant que nous avons établi nos bases, commençons à coder la montre elle-même. Nous commençons par les aiguilles des minutes et des heures.

Il existe de nombreuses façons de dessiner ces petites lignes. Nous pourrions dessiner chaque ligne une par une, mais probablement la manière la plus efficace de les dessiner est de dessiner un cercle avec une propriété de tiret spéciale.

La balise `circle` dans notre exemple initial a une position centrale, un rayon pour la taille, une couleur de remplissage et de bordure, et une largeur de bordure.

Les éléments SVG ont souvent des options de style similaires à celles des éléments HTML avec CSS. Mais ces options ont des noms de propriétés différents. Vous pouvez considérer la propriété `fill` comme la `background-color` en CSS. Et les propriétés `stroke` et `stroke-width` sont également similaires aux propriétés `border-color` et `border-width`. Gardez simplement à l'esprit qu'elles ne sont pas exactement les mêmes.

Nous utiliserons également la propriété `fill` pour définir la couleur du texte, et nous utiliserons la propriété `stroke` pour définir la couleur d'une ligne.

Maintenant, comment transformer un cercle continu en marqueurs de minutes ? Vous êtes peut-être familier avec la propriété `border-style` en CSS. Principalement, vous utiliseriez une bordure solide, mais vous pouvez également avoir une bordure pointillée ou en tirets. Ces styles de bordure ne sont pas très courants, car vous n'avez pas autant d'options pour les ajuster finement en CSS.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/SVG-Watch.001-2.jpeg)
_La propriété `border-style` en CSS pour les éléments HTML_

En SVG, nous avons des possibilités similaires avec beaucoup plus d'options de personnalisation. Nous pouvons utiliser les propriétés `stroke-dasharray`, `stroke-dashoffset` et `pathLength`.

Prenons quelques exemples. Dans le premier exemple, nous définissons un seul nombre comme `stroke-dasharray`. Cela résultera en une bordure en tirets où le segment de ligne et l'écart ont tous deux la même longueur.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/SVG-Watch.002.jpeg)
_La propriété `stroke-dasharray` pour SVG_

Cette propriété est un tableau. Si nous définissons deux nombres, le premier sera la longueur du segment de ligne, et le second sera la longueur de l'écart. Vous pouvez même définir plus de deux nombres, et la longueur de la ligne et de l'écart prendra toujours le nombre suivant. Jusqu'à ce qu'il arrive à la fin du tableau, puis il recommence au début.

Nous allons définir deux nombres. Un pour la longueur du marqueur de minute, et un pour l'écart entre eux. La somme de ces deux doit être exactement la longueur d'une minute sur le cercle. Nous savons qu'une heure est de 60 minutes. Nous pouvons donc calculer la circonférence du cercle, puis la diviser par 60 pour obtenir la longueur d'une minute.

Mais il y a une meilleure façon. Au lieu de calculer la circonférence du cercle, nous pouvons faire l'inverse. Nous pouvons définir la propriété `pathLength`.

Cette propriété est un peu délicate. Elle ne redimensionne pas le cercle mais affecte la manière dont la propriété dasharray est interprétée. Les tirets seront dessinés comme si le cercle avait une circonférence définie par `pathLength`.

Alors définissons `pathLength` à `60`, représentant 60 minutes. Maintenant, la somme du segment de ligne et de l'écart doit être de 1 au total. Je l'ai définie à `0.2` et `0.8` dans cet exemple.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/SVG-Watch.001-3.jpeg)
_Utilisation de la propriété `pathLength`. Notez que la somme des deux nombres dans la propriété `stroke-dasharray` est de un, correspondant à la longueur d'une minute._

Maintenant, nous avons presque terminé, mais un petit morceau manque encore. Le tiretage commence à la mauvaise position. Pour le corriger, nous devons le décaler de la moitié de la longueur du segment de ligne en utilisant la propriété `stroke-dashoffset`.

La propriété de décalage des tirets peut être un peu contre-intuitive, car une valeur positive ici décale le tiretage vers l'arrière. Vous pouvez également la définir à un nombre positif pour la décaler vers l'avant.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/SVG-Watch.002-1.jpeg)
_Exemple avec et sans `stroke-dashoffset`_

De la même manière, nous pouvons définir un marqueur d'heure. Nous ajoutons une nouvelle balise circle avec presque les mêmes propriétés. La seule chose qui est différente est la couleur et nous avons des écarts plus longs dans le tableau de tirets.

```html
. . .

    <svg width="200" height="200" viewBox="-100 -100 200 200">
      <circle
        cx="0"
        cy="0"
        r="90"
        fill="transparent"
        stroke="#0f0e0e"
        stroke-width="7"
        stroke-dasharray="0.2 0.8"
        stroke-dashoffset="0.1"
        pathLength="60"
      />

      <circle
        cx="0"
        cy="0"
        r="90"
        fill="transparent"
        stroke="#f0f0c9"
        stroke-width="7"
        stroke-dasharray="0.2 4.8"
        stroke-dashoffset="0.1"
        pathLength="60"
      />
    </svg>
    
. . .
```

Il est important de noter ici que la superposition dans SVG compte. Les balises ajoutées plus tard dans le document seront au-dessus des précédentes. Si nous ajoutons ces deux cercles dans l'ordre inverse, alors les minutes couvriraient complètement les marqueurs d'heure.

Puisque SVG vit maintenant dans HTML, nous pouvons déplacer certaines de ces propriétés vers CSS. Nous ne pouvons pas déplacer toutes les propriétés cependant. Il y a une différence entre les propriétés définissant le style et celles définissant la forme d'un élément.

Le rayon, par exemple, définit la forme du cercle, donc il doit rester avec le code SVG. Les propriétés de remplissage et de contour, en revanche, nous pouvons les déplacer.

```html
. . .
    
    <svg width="200" height="200" viewBox="-100 -100 200 200">
      <circle class="minute_marker" r="90" pathLength="60" />
      <circle class="hour_marker" r="90" pathLength="60" />
    </svg>
    
. . .
```

```css
.hour_marker {
  fill: transparent;
  stroke: #f0f0c9;
  stroke-width: 7;
  stroke-dasharray: 0.2, 4.8;
  stroke-dashoffset: 0.1;
}

.minute_marker {
  fill: transparent;
  stroke: #0f0e0e;
  stroke-width: 7;
  stroke-dasharray: 0.2, 0.8;
  stroke-dashoffset: 0.1;
}
```

## **Comment dessiner les aiguilles de la montre**

Ajoutons les aiguilles qui indiquent l'heure. Initialement, nous les dessinons pour qu'elles pointent vers le haut, puis nous les tournons en position avec JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/SVG-Watch.001-4.jpeg)

Nous utilisons l'élément `line` pour dessiner les aiguilles. Pour définir un élément de ligne, nous devons définir les coordonnées de départ et de fin, ainsi qu'une couleur `stroke` et la propriété `stroke-width`.

Pour rendre les choses un peu plus belles, nous pouvons également ajouter la propriété `stroke-linecap` pour avoir des extrémités de ligne arrondies. Ces propriétés de style, nous les ajoutons avec CSS.

```html
. . . 

    <svg width="200" height="200" viewBox="-100 -100 200 200">
      <circle class="minute_marker" r="90" pathLength="60" />
      <circle class="hour_marker" r="90" pathLength="60" />

      <line class="hand" x1="0" y1="0" x2="0" y2="-50" />
      <line class="hand hand--thick" x1="0" y1="-12" x2="0" y2="-50" />

      <line class="hand" x1="0" y1="0" x2="0" y2="-80" />
      <line class="hand hand--thick" x1="0" y1="-12" x2="0" y2="-80" />

      <line class="hand hand--second" x1="0" y1="12" x2="0" y2="-80" />
    </svg>

. . .    
```

```css
. . .

.hand {
  stroke: #ffffff;
  stroke-width: 2;
  stroke-linecap: round;
}

.hand--thick {
  stroke-width: 7;
}

.hand--second {
  stroke: yellow;
}
```

## Comment orienter les aiguilles de la montre dans la bonne direction

Maintenant, comment faire pour tourner ces lignes en position ? Si nous attribuons un ID à un élément, nous pouvons y accéder et le manipuler depuis JavaScript.

Quel élément devons-nous attribuer un ID, cependant ? Nous avons deux éléments pour une aiguille. Pour résoudre ce problème, nous pouvons regrouper ces deux éléments de ligne dans une balise de groupe. Vous pouvez considérer une balise de groupe comme l'élément `div` en HTML.

Nous pouvons attribuer un ID à ce groupe, puis nous pouvons faire tourner tout le groupe en position depuis JavaScript.

```html
. . .

    <svg width="800" height="800" viewBox="-100 -100 200 200">
      <circle class="minute_marker" r="90" pathLength="60" />
      <circle class="hour_marker" r="90" pathLength="60" />

      <g id="hour_hand">
        <line class="hand" x1="0" y1="0" x2="0" y2="-50" />
        <line class="hand hand--thick" x1="0" y1="-12" x2="0" y2="-50" />
      </g>

      <g id="minute_hand">
        <line class="hand" x1="0" y1="0" x2="0" y2="-80" />
        <line class="hand hand--thick" x1="0" y1="-12" x2="0" y2="-80" />
      </g>

      <g id="second_hand">
        <line class="hand hand--second" x1="0" y1="12" x2="0" y2="-80" />
      </g>
    </svg>

. . .
```

Dans le fichier JavaScript, nous obtenons d'abord les éléments des aiguilles par leur ID. Ensuite, nous créons un objet Date et nous obtenons l'heure, la minute et la seconde actuelles. Enfin, nous définissons l'attribut `transform` des éléments en fonction de ces valeurs.

```javascript
const hoursElement = document.getElementById("hour_hand");
const minutesElement = document.getElementById("minute_hand");
const secondsElement = document.getElementById("second_hand");

const date = new Date();

const hour = date.getHours();
const minute = date.getMinutes();
const second = date.getSeconds();

hoursElement.setAttribute("transform", `rotate(${(360 / 12) * hour})`);
minutesElement.setAttribute("transform", `rotate(${(360 / 60) * minute})`);
secondsElement.setAttribute("transform", `rotate(${(360 / 60) * second})`);
```

L'attribut transform peut inclure plusieurs transformations comme la mise à l'échelle, la translation ou l'inclinaison.

Nous définissons la transformation `rotate`, qui nécessite un nombre. Ce nombre est une rotation entre 0 et 360 degrés. Pour l'aiguille des heures, nous divisons 360 par 12 pour obtenir la rotation nécessaire par heure et nous la multiplions par l'heure actuelle. Cela devrait tourner l'aiguille des heures vers l'heure actuelle.

Pour l'aiguille des minutes et des secondes, nous faisons la même chose, sauf que nous divisons 360 par 60, car une heure est composée de 60 minutes et une minute est de 60 secondes.

Heureusement pour nous, le centre de transformation par défaut est l'origine, la coordonnée `0,0`. Si ce n'était pas le cas, nous pourrions définir une autre origine de transformation, mais grâce à nos paramètres de `viewBox`, nous n'en avons pas besoin.

## **Comment animer les aiguilles de la montre**

Maintenant, cela devrait déjà montrer l'heure actuelle, mais notre image est statique. Pour suivre l'heure, nous pouvons utiliser la fonction `requestAnimationFrame` pour déplacer les aiguilles.

```javascript
const hoursElement = document.getElementById("hour_hand");
const minutesElement = document.getElementById("minute_hand");
const secondsElement = document.getElementById("second_hand");

function animate() {
  const date = new Date();

  const hour = date.getHours() % 12;
  const minute = date.getMinutes();
  const second = date.getSeconds();

  hoursElement.setAttribute("transform", `rotate(${(360 / 12) * hour})`);
  minutesElement.setAttribute("transform", `rotate(${(360 / 60) * minute})`);
  secondsElement.setAttribute("transform", `rotate(${(360 / 60) * second})`);

  requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
```

Nous déplaçons la logique de rotation dans une fonction animate et utilisons la fonction requestAnimationFrame.

Tout d'abord, nous la déclenchons en appelant requestAnimationFrame en dehors de la fonction animate. Ensuite, pour continuer avec l'animation, nous demandons également une autre image à la fin de chaque cycle d'animation.

Si vous voulez une animation plus fluide, vous pouvez affiner le positionnement. Au lieu d'avoir des positions discrètes pour les aiguilles, nous pouvons les définir de manière à ce qu'elles puissent pointer vers des secondes, minutes et heures divisées.

```javascript
const hoursElement = document.getElementById("hour_hand");
const minutesElement = document.getElementById("minute_hand");
const secondsElement = document.getElementById("second_hand");

function animate() {
  const date = new Date();

  const hour = date.getHours() + date.getMinutes() / 60;
  const minute = date.getMinutes() + date.getSeconds() / 60;
  const second = date.getSeconds() + date.getMilliseconds() / 1000;

  hoursElement.setAttribute("transform", `rotate(${(360 / 12) * hour})`);
  minutesElement.setAttribute("transform", `rotate(${(360 / 60) * minute})`);
  secondsElement.setAttribute("transform", `rotate(${(360 / 60) * second})`);

  requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
```

L'aiguille des heures ne recevra pas sa position uniquement en fonction de l'heure, mais elle effectuera également une légère rotation en fonction des minutes actuelles.

L'aiguille des minutes tiendra compte de la seconde actuelle dans sa rotation. Et l'aiguille des secondes tiendra également compte des millisecondes. Ainsi, nos aiguilles auront un mouvement continu. Elles ne sauteront pas de seconde en seconde, mais elles s'animeront.

## **Prochaines étapes – Comment rendre la montre interactive**

Maintenant, si nous vérifions le résultat, nous devrions avoir une montre animée de manière fluide.

Pour aller plus loin, vous pouvez également ajouter une fenêtre de calendrier affichant la date actuelle, avec l'élément `text`. Et pour passer au niveau supérieur, vous pouvez même ajouter un gestionnaire d'événements pour cet élément, qui bascule son contenu entre la date actuelle et l'indicateur AM/PM.

Si vous êtes bloqué, consultez la vidéo ci-dessous, où nous couvrons également cette partie.

Mélanger SVG avec JavaScript ouvre de nombreuses options intéressantes. Vous pouvez animer des choses, ajouter des interactions et générer des graphiques. J'ai hâte de voir ce que vous allez créer.

%[https://www.youtube.com/watch?v=ULomsOSk4JA]

## **Abonnez-vous pour plus de tutoriels sur le développement Web :**

%[https://www.youtube.com/channel/UCxhgW0Q5XLvIoXHAfQXg9oQ]