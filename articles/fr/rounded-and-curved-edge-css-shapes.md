---
title: Comment créer des formes à bords courbés et arrondis avec CSS
subtitle: ''
author: Temani Afif
co_authors: []
series: null
date: '2024-10-14T22:07:54.825Z'
originalURL: https://freecodecamp.org/news/rounded-and-curved-edge-css-shapes
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1728902609915/17a0da8c-143b-4160-8133-bc865c1b535b.jpeg
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: Comment créer des formes à bords courbés et arrondis avec CSS
seo_desc: In a previous article, I showed you how to create some fancy shapes that
  you can use as section dividers on your websites (a slanted divider, an arrow divider,
  and others). In this article, we will study and learn how to make more CSS shapes
  using th...
---

Dans [un article précédent](https://www.freecodecamp.org/news/section-divider-using-css/), je vous ai montré comment créer des formes élégantes que vous pouvez utiliser comme séparateurs de sections sur vos sites web (un séparateur incliné, un séparateur en forme de flèche, et d'autres). Dans cet article, nous allons étudier et apprendre à créer d'autres formes CSS en utilisant la même technique.

Voici un aperçu des formes que nous allons examiner ici, appliquées à l'en-tête de mon profil freeCodeCamp :

![Formes CSS : bords arrondis et courbés](https://cdn.hashnode.com/res/hashnode/image/upload/v1728811438184/24597334-f2be-4bb1-83f2-11045bc8cacc.png align="center")

Cool, n'est-ce pas ? Les deux designs sont couramment utilisés comme séparateurs de sections. Nous allons apprendre ensemble comment créer de telles formes avec un code simple.

Avant de commencer, vous pouvez trouver le code des formes que nous créons (et plus encore !) dans [ma collection en ligne](https://css-shape.com/). Vous pouvez facilement copier le code à partir de là – mais ne partez pas tout de suite ! Comprendre la logique derrière le code est également important et vous aidera à le personnaliser pour répondre à vos besoins.

## Comment créer un bord arrondi en utilisant `clip-path`

Commençons par la première forme : [le bord arrondi](https://css-shape.com/rounded-edge/). Cela peut sembler surprenant, mais le code pour créer une telle forme est aussi simple qu'une déclaration CSS :

```css
.rounded-edge {
  clip-path: ellipse(85% 100% at top);
}
```

Dessinons une figure pour comprendre comment une "ellipse" crée une forme de bord arrondi.

![Illustration de la valeur ellipse du clip-path](https://cdn.hashnode.com/res/hashnode/image/upload/v1728813578343/a4560ca7-c2db-41b6-a3ed-9661ab15ef0b.png align="center")

Nous commençons avec un élément rectangulaire sans `clip-path` appliqué. Ensuite, nous ajoutons `clip-path: ellipse(50% 100% at top)`. Comme vous pouvez le voir, nous avons la forme de l'ellipse. Son centre est au "centre haut" de l'élément et ses rayons sont égaux à `50%` horizontalement et `100%` verticalement. La forme dépasse les limites de l'élément, c'est pourquoi nous ne voyons que la partie inférieure de celle-ci. La partie supérieure ne masque rien.

Vous vous demandez peut-être : j'ai dit "centre haut", mais pourquoi dans le code n'avons-nous que "top" ?

Par défaut, si nous ne spécifions pas la position, elle sera au centre de l'élément. Cela équivaut à "`center`", "`center center`", "`50%`" ou "`50% 50%`". Notez comment nous pouvons définir une valeur ou deux valeurs. Si la deuxième valeur est omise, elle sera égale à "`center`" donc définir "`top`" est la même chose que "`top center`".

Vous n'avez pas besoin de vous souvenir de tous les cas. Utiliser des mots-clés tels que "`top`", "`left`", et ainsi de suite est, la plupart du temps, suffisant – sauf si vous avez besoin de créer une forme personnalisée (nous verrons cela plus tard).

Revenons à la figure précédente. Si nous augmentons le rayon horizontal et le rendons plus grand que 50% (85% par exemple), l'ellipse deviendra plus grande et couvrira logiquement une zone plus grande. Vous commencez à voir le truc, n'est-ce pas ? À la fin, ce n'est qu'une portion en bas de l'ellipse qui est visible – le bord arrondi que nous voulons !

En bonus, c'est responsive, puisque nous utilisons des valeurs en pourcentage. Le rayon horizontal est relatif à la largeur tandis que le vertical est relatif à la hauteur. Cela dit, vous pouvez également utiliser des valeurs en pixels si vous voulez une taille fixe pour votre ellipse. Dans certains cas, cela peut donner un meilleur résultat.

Voici une démonstration montrant les deux cas. Redimensionnez l'écran pour remarquer la différence :

<iframe height="500" style="width:100%;height:500px" src="https://codepen.io/t_afif/embed/preview/mdNRvEB/8d8fdd895914c59ab86257ed94f9f71a?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/mdNRvEB/8d8fdd895914c59ab86257ed94f9f71a">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Alors, qu'en est-il de l'autre variation ? Nous devons simplement changer "top" par "bottom", n'est-ce pas ?

Exactement ! En changeant le centre de l'ellipse, vous changez l'emplacement du bord arrondi et obtenez facilement les quatre directions.

![Quatre variations des bords arrondis](https://cdn.hashnode.com/res/hashnode/image/upload/v1728817085669/307215e8-f40a-4999-a36f-db6a70d3d1b7.png align="center")

Vous pouvez également obtenir une forme plus personnalisée si vous ajustez le centre de l'ellipse en utilisant des valeurs en pourcentage. Par exemple, utiliser `30% 0%` pour obtenir un bord arrondi décalé vers la gauche (notez que `top` est équivalent à `50% 0%`).

<iframe height="350" style="width:100%;height:350px" src="https://codepen.io/t_afif/embed/preview/vYogbZe/eee85304e8d8c22b625e81b0ee6e8a33?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/vYogbZe/eee85304e8d8c22b625e81b0ee6e8a33">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Beaucoup de possibilités avec une seule ligne de code !

Allez voir [la version en ligne](https://css-shape.com/rounded-edge/) où vous pouvez trouver plus d'exemples et personnaliser facilement la forme en ajustant le code existant.

## Comment créer un bord courbé en utilisant `mask`

Passons à la deuxième forme : [le bord courbé](https://css-shape.com/curved-edge/). Celui-ci est également assez facile à créer car il nécessite également une ligne de code.

```css
.curved-edge {
  mask: radial-gradient(60% 70px at bottom,#0000 100%,#000);
}
```

Cette fois, nous allons utiliser `mask` au lieu de `clip-path`, mais la logique est la même. Nous allons masquer certaines parties de l'élément et garder le reste visible. Lorsque vous utilisez mask, la partie masquée est la couleur transparente du dégradé (le `#0000`) tandis que la partie visible est la couleur opaque du dégradé (le `#000`).

Peu importe la couleur que vous utilisez, seule la transparence de la couleur compte. Vous êtes donc libre d'utiliser n'importe quelle syntaxe de couleur. Voici un exemple utilisant la syntaxe `rgb()` :

```css
.curved-edge {
  mask: radial-gradient(60% 70px at bottom,rgb(0 0 0/0%) 100%,rgb(0 0 0/100%));
}
```

Ou des noms de couleurs :

```css
.curved-edge {
  mask: radial-gradient(60% 70px at bottom,transparent 100%,black);
}
```

Et voici une figure pour illustrer comment cela fonctionne.

![Aperçu du radial-gradient](https://cdn.hashnode.com/res/hashnode/image/upload/v1728830604961/6468c949-d783-43b7-8d0a-81fb39ecf2c7.png align="center")

Similaire à la fonction ellipse de `clip-path`, `radial-gradient()` créera également une forme d'ellipse. La seule différence est que cette fois nous allons masquer la partie intérieure de l'ellipse et montrer la partie extérieure. Et grâce à la partie débordante, nous obtenons la forme courbée que nous voulons.

Je pense que vous connaissez la suite de l'histoire maintenant. En ajustant les rayons et la position du centre de l'ellipse, nous obtenons les différentes variations. Comme petit devoir, essayez de mettre à jour le code précédent pour obtenir les directions haut, gauche et droite. Vous pouvez comparer ce que vous avez trouvé avec [mon implémentation](https://css-shape.com/curved-edge/).

Lorsque vous utilisez cette méthode, assurez-vous d'avoir suffisamment d'espace en bas. Contrairement au bord arrondi, le bord courbé peut masquer une partie de votre contenu en bas, il est donc toujours bon d'inclure un padding égal au rayon vertical.

```css
.curved-edge {
  padding-bottom: 70px;
  mask: radial-gradient(60% 70px at bottom,#0000 100%,#000);
}
```

## Comment combiner ces deux formes CSS

Et si nous avions les deux courbes pour créer [une forme de rectangle courbé](https://css-shape.com/curved-rectangle/) ? C'est possible en combinant simplement les deux morceaux de code comme ceci :

```css
.curved-rectangle {
  /* bord courbé en bas */
  mask: radial-gradient(60% 70px at bottom,#0000 100%,#000);
  /* bord arrondi en haut */
  clip-path: ellipse(80% 100% at bottom);
}
```

Voyez-le en action :

<iframe height="400" style="width:100%;height:450px" src="https://codepen.io/t_afif/embed/preview/VwoPOwm/8f71a34ba272ac1cb7d96ff7d494239b?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/VwoPOwm/8f71a34ba272ac1cb7d96ff7d494239b">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Et l'effet opposé en changeant `bottom` par `top` :

```css
.curved-rectangle {
  /* bord courbé en haut */
  mask: radial-gradient(60% 70px at top,#0000 100%,#000);
  /* bord arrondi en bas */
  clip-path: ellipse(80% 100% at top);
}
```

<iframe height="450" style="width:100%;height:450px" src="https://codepen.io/t_afif/embed/preview/ZEgLNEZ/56d77b755720ce445225af72a32e7941?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/ZEgLNEZ/56d77b755720ce445225af72a32e7941">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Vous remarquerez que j'utilise soit `top` partout, soit `bottom` partout, ce qui rend les deux morceaux de code faciles à retenir.

Maintenant, vous vous demandez peut-être – comment pouvons-nous avoir les mêmes courbes en haut et en bas ?

Comme vous l'avez peut-être remarqué, les deux courbes ne correspondent pas, ce qui rend la forme globale un peu brisée. Mais nous pouvons corriger cela. Nous devons nous assurer que les deux parties du code créent la même forme d'ellipse en définissant les mêmes rayons.

```css
.curved-header {
  /* bord courbé en haut */
  mask: radial-gradient(80% 100% at top,#0000 100%,#000);
  /* bord arrondi en bas */
  clip-path: ellipse(80% 100% at top);
}
```

Notez le "`80% 100% at top`" qui est le même dans les deux déclarations – mais rien ne sera visible si nous utilisons ce code. N'oubliez pas que le `clip-path` masquera la partie extérieure de l'ellipse tandis que le dégradé masquera la partie intérieure. Donc si les deux ellipses sont les mêmes, tout sera masqué.

Pour corriger cela, nous devons décaler le dégradé et le déplacer vers le haut pour obtenir ce qui suit :

```css
.curved-rectangle {
  /* bord courbé en haut */
  mask: radial-gradient(80% 100% at 50% -78% /* au lieu de 50% 0% */,#0000 100%,#000);
  /* bord arrondi en bas */
  clip-path: ellipse(80% 100% at top);
}
```

La forme est maintenant parfaite et les deux courbes sont alignées.

<iframe height="450" style="width:100%;height:450px" src="https://codepen.io/t_afif/embed/preview/GRVWKZM/32ab225612d6ffade20cbef6c43100fa?default-tab=result">
  See the Pen <a href="https://codepen.io/t_afif/pen/GRVWKZM/32ab225612d6ffade20cbef6c43100fa">
  Untitled</a> by Temani Afif (<a href="https://codepen.io/t_afif">@t_afif</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Si vous n'aimez pas utiliser des nombres magiques comme "-78%", nous pouvons considérer quelques calculs pour obtenir des résultats précis :

```css
.curved-rectangle {
  --c: 80; /* contrôle la courbe */

  mask: 
    radial-gradient(calc(var(--c)*1%) 100% 
     at 50% calc(-100%*cos(asin(50/var(--c)))),
     #0000 100%,#000);
  clip-path: ellipse(calc(var(--c)*1%) 100% at top);
}
```

Le code semble plus complexe (je vais sauter l'explication géométrique ennuyeuse), mais vous pouvez facilement contrôler la courbe en ajustant une seule valeur.

Alors, qu'en est-il de la version du bas ? Nous mettons à jour le code comme suit :

```css
.curved-rectangle {
  --c: 80; /* contrôle la courbe */

  mask: 
    radial-gradient(calc(var(--c)*1%) 100% 
     at 50% calc(100% + 100%*cos(asin(50/var(--c)))),
     #0000 100%,#000);
  clip-path: ellipse(calc(var(--c)*1%) 100% at bottom);
}
```

Le `top` du `clip-path` devient `bottom` et dans le dégradé, nous utilisons `100% + X` au lieu de `-X` où `X` est le décalage. Vous pouvez toujours trouver tout le code dans [ma collection en ligne](https://css-shape.com/curved-rectangle/).

## Conclusion

Combien de lignes de code devez-vous retenir ? Seulement deux lignes de code – c'est tout ! Vous pouvez créer un bord arrondi en utilisant `clip-path` :

```css
.rounded-edge {
  clip-path: ellipse(85% 100% at top);
}
```

Et vous pouvez créer un bord courbé en utilisant `mask` :

```css
.curved-edge {
  mask: radial-gradient(60% 70px at top,#0000 100%,#000);
}
```

Et en combinant les deux, vous obtenez un rectangle courbé :

```css
.curved-rectangle {
  mask: radial-gradient(80% 100% at 50% -78%,#0000 100%,#000);
  clip-path: ellipse(80% 100% at top);
}
```

Vous n'avez pas besoin de retenir la version verbeuse où j'utilise des calculs. La plupart du temps, vous n'avez pas vraiment besoin de valeurs précises et vous pouvez ajuster manuellement la position jusqu'à ce que vous obteniez ce que vous voulez.

N'oubliez pas de marquer [ma collection en ligne de formes CSS](https://css-shape.com/) si vous voulez copier facilement le code de n'importe quelle forme. Je recommande également de lire mon "[Guide moderne pour créer des formes CSS](https://www.smashingmagazine.com/2024/05/modern-guide-making-css-shapes/)" pour connaître le secret derrière la création de plus de formes CSS.