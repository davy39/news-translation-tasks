---
title: Comment utiliser CSS Flexbox pour faire sortir des éléments de leurs conteneurs
subtitle: ''
author: kyw
co_authors: []
series: null
date: '2024-01-08T18:15:47.000Z'
originalURL: https://freecodecamp.org/news/break-out-elements-from-containers-using-flexbox
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/pexels-dagmara-dombrovska-19707371.jpg
tags:
- name: css flex
  slug: css-flex
- name: Web Development
  slug: web-development
seo_title: Comment utiliser CSS Flexbox pour faire sortir des éléments de leurs conteneurs
seo_desc: 'When you''re building a webpage, sometimes you might want images or other
  elements to go beyond the boundaries of a container. So in this tutorial, I''ll
  show you a couple ways you can accomplish this.

  To illustrate a situation when you might find this...'
---

Lorsque vous construisez une page web, il arrive parfois que vous souhaitiez que des images ou d'autres éléments dépassent les limites d'un conteneur. Dans ce tutoriel, je vais vous montrer quelques méthodes pour y parvenir.

Pour illustrer une situation où cela pourrait être utile, imaginons que nous avons une page web qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/847shots_so.png)
_Une page web dont le contenu s'étend sur 100 % de la largeur de la fenêtre_

Comme vous en conviendrez probablement, ce n'est pas très agréable à lire. L'une des choses que vous pouvez faire est de définir une `max-width` sur le conteneur – dans ce cas, il s'agit de l'élément `article` afin qu'il soit "contenu" de manière plus agréable :

```css
article {
  max-width: 60ch; /* pas plus de 60 caractères par ligne dans ce conteneur */
}

```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/645shots_so-1.png)
_Utiliser la propriété max-width pour contraindre la largeur d'un conteneur_

C'est mieux, mais c'est décalé à gauche. Maintenant, plaçons notre texte d'article et notre image au centre de la page en définissant `margin: 0 auto` sur le conteneur :

```css
article {
  max-width: 60ch;
  margin: 0 auto; /* centrer ce conteneur */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/945shots_so.png)
_Centrer notre article avec margin: 0 auto_

Beaucoup mieux maintenant, n'est-ce pas ? Pour optimiser davantage la lisibilité, nous pouvons ajuster la taille de la police et la hauteur de ligne comme je l'ai fait dans le bac à sable ci-dessous :

%[https://codepen.io/kilgarenone/pen/NWJPePO]

Maintenant, remarquez la largeur de l'image : elle a été contrainte par la largeur du conteneur. Et si vous souhaitez que l'image (ou tout autre élément) s'étend sur toute la page (c'est-à-dire en pleine largeur), comme ceci ?

![Image](https://www.freecodecamp.org/news/content/images/2024/01/868shots_so.png)
_Exemple de mise en page en pleine largeur_

Ou si vous souhaitez simplement que l'image "dépasse" pour avoir une largeur supérieure à celle de son conteneur, comme ceci ?

![Image](https://www.freecodecamp.org/news/content/images/2024/01/539shots_so.png)
_Un élément dépassant pour avoir une largeur supérieure à celle du conteneur_

Actuellement, autant que je sache, il existe deux méthodes principales pour y parvenir :

1. Vous pouvez soit faire un décalage horizontal manuel via un `margin-left` négatif et `translateX` pour déplacer l'image vers la gauche, soit
2. Vous pouvez utiliser [CSS Grid](https://www.bram.us/2017/06/20/breaking-elements-out-of-their-containers-in-css/).

Mais à mon avis, la première solution est bricolée, et la seconde est lourde.

Dans cet article, je vais couvrir des méthodes plus simples pour faire cela.

## Préparation du terrain

Tout d'abord, libérons tous les éléments enfants à l'intérieur du conteneur. Au lieu de définir une largeur sur le conteneur, nous la définissons sur ses éléments enfants :

```css
/* Au lieu de faire ceci
article {
  max-width: 60ch;
  margin: 0 auto;
}
*/

/* nous définissons la largeur sur ses éléments enfants directs */
article > * {
  max-width: 60ch; /* la largeur des enfants ne peut pas dépasser 60ch */
  margin: 0 auto; /* les centrer */
}

```

**Avant :**

![Image](https://www.freecodecamp.org/news/content/images/2024/01/504shots_so.png)
_Tous les enfants ne peuvent pas dépasser les limites de leur conteneur_

**Après :**

![Image](https://www.freecodecamp.org/news/content/images/2024/01/409shots_so.png)
_Maintenant, chaque enfant a suffisamment d'espace pour s'étendre horizontalement s'il le souhaite_

Le conteneur `article` n'est plus limité à une largeur spécifique. Il s'étend maintenant sur toute la largeur de la fenêtre. Cela permet à tout élément enfant de s'étendre latéralement jusqu'à la limite de la fenêtre.

Par exemple, nous pouvons choisir de laisser spécifiquement l'image s'étendre à notre guise :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/4shots_so.png)
_L'élément `img` s'étendant plus largement que les éléments `p`_

C'est exactement ce que nous allons apprendre à faire ensuite.

## Comment faire sortir des éléments sans enfants

Faire sortir des éléments sous leur forme la plus simple, c'est lorsque les éléments que nous voulons faire sortir n'ont pas d'enfants. Par exemple, disons que nous voulons faire sortir l'élément `img` ci-dessous :

```html
<article>
  <p>Textes</p>
  <img />
  <p>Textes</p>
</article>

```

Et faisons-en une image en _pleine largeur_. Pour cela, nous allons appliquer 3 propriétés sur l'`img` :

1. `**display: block**` – Parce que a) `img` est en ligne par défaut, et b) `margin: 0 auto` ne fonctionne que sur les éléments [block](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-left#auto). 
2. `**width: 100%**` – Pour qu'il remplisse entièrement la largeur de son conteneur qui est `article` et qui remplit déjà la fenêtre.
3. `**max-width: 100%**` – Pour remplacer le `max-width: 60ch` et aussi pour l'empêcher de s'étendre au-delà de l'espace horizontal disponible de son conteneur. 

```css
img {
  display: block;
  width: 100%;
  max-width: 100%; 
}

```

Et cela fonctionne :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/914shots_so.png)
_Mise en page en pleine largeur_

Suite au bac à sable précédent :

%[https://codepen.io/kilgarenone/pen/QWowRME]

Jusqu'à présent, tout va bien.

## Comment faire sortir des éléments qui ont des enfants

Maintenant, que se passe-t-il si votre image est enveloppée dans une balise `figure`, comme ceci :

```html
<figure>
  <img width="900px" src="" alt="" />
  <figcaption></figcaption>
</figure>

```

Et l'image a sa largeur définie ou utilise simplement sa largeur intrinsèque ? Comment allons-nous la faire sortir tout en la centrant ? 

Sans utiliser CSS Flexbox, pour rendre l'image en pleine largeur comme avant, nous devons d'abord définir la `figure` à `max-width: 100%` afin qu'elle puisse remplir tout l'espace horizontal de `article`. Ensuite, nous devons nous assurer que notre `img` est appliquée avec `display: block` et `margin: 0 auto` afin de rester centrée.

Comparez cela à l'utilisation de **CSS Flexbox**. Appliquez une classe CSS qui contient 3 propriétés Flexbox à `figure` seule et c'est terminé :

```css
.break-out {
  display: flex;
  flex-direction: column;
  align-items: center;
}

```

1. `**display: flex**` – Définir `figure` comme un conteneur Flex à partir duquel nous pouvons choisir d'organiser son contenu – dans ce cas, il s'agirait de `img` et `figcaption` – soit horizontalement (ligne) soit verticalement (colonne) le long de l'[axe principal](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox#the_main_axis). 
2. `**flex-direction: column**` – Pour notre cas d'utilisation, nous choisissons d'organiser le contenu verticalement.
3. `**align-items: center**` – Enfin, nous choisissons de toujours centrer le contenu le long de l'axe transversal. Si l'axe principal va verticalement dans `flex-direction: column`, son axe transversal irait horizontalement. Cette propriété permet donc à `img` et `figcaption` d'être toujours centrées horizontalement par rapport à `figure` qui s'étend maintenant sur 100 % de l'écran. 

Enfin, nous appliquons simplement la classe à l'élément `figure` :

```html
<figure class="break-out">
  <img width="900px" src="" alt="" />
  <figcaption></figcaption>
</figure>

```

Maintenant, quelle que soit la largeur de l'`img`, elle sera centrée même jusqu'à ce qu'elle soit en pleine largeur :

%[https://codepen.io/kilgarenone/pen/eYXNyjp]

## Avantages de ces méthodes

Les méthodes que j'ai démontrées ici présentent les avantages suivants :

1. [Principe du moindre pouvoir](https://www.w3.org/2001/tag/doc/leastPower.html) : CSS Flexbox est une solution moins puissante que CSS Grid.
2. Pas de calcul compliqué : nous laissons le navigateur centrer notre image dans l'espace disponible.
3. Réactif : aucun recalcul nécessaire de notre part lorsque le navigateur redimensionne.

Les avantages de second ordre sont :

1. Pour les utilisateurs : performance optimale – moins de code à exécuter et un code moins coûteux. Navigateur heureux, utilisateurs heureux.
2. Pour les développeurs : code plus simple et moins de code à maintenir, ce qui signifie moins de ressources cognitives précieuses dépensées.

## Contexte

J'ai trouvé cette méthode lorsque je construisais Zuunote. C'est une [application web de prise de notes basée sur Markdown](https://zuunote.com/) dans laquelle les images peuvent être redimensionnées. 

Le point délicat est que, dans Markdown, la syntaxe des images est analysée comme un élément en ligne. Ainsi, lorsque les utilisateurs créent des images en ligne lors de la rédaction d'un paragraphe, cette méthode leur permet de redimensionner entre en ligne et en pleine largeur.

Voici comment j'ai réalisé cela. Similaire à ce que nous venons de discuter, j'ai enveloppé l'élément `img` dans une balise `span` pour conserver les caractères en ligne :

```html
<span>
  <img src="" alt="" />
</span>

```

Ensuite, j'ai appliqué nos propriétés Flexbox sur le `span` lorsque l'utilisateur a redimensionné au-delà de la limite des paragraphes :

```html
<span class="break-out">
  <img src="" alt="" />
</span>

```

Et le navigateur gardera l'image centrée sans aucune assistance coûteuse de ma part.

Voici le résultat :

%[https://codepen.io/kilgarenone/pen/bGZdEQJ]

Un geste couvre un spectre d'intentions de redimensionnement – je trouve cela assez ingénieux :)

Merci d'avoir lu !