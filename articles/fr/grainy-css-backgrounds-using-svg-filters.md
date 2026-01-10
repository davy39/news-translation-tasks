---
title: Comment créer des arrière-plans CSS granulaires à l'aide de filtres SVG
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-02-16T16:00:47.000Z'
originalURL: https://freecodecamp.org/news/grainy-css-backgrounds-using-svg-filters
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/fCC-thumbp.jpg
tags:
- name: CSS
  slug: css
- name: SVG
  slug: svg
- name: Web Development
  slug: web-development
seo_title: Comment créer des arrière-plans CSS granulaires à l'aide de filtres SVG
seo_desc: "In this article we're going to create more interesting website backgrounds\
  \ by using grainy effects. \nThere's a full video walkthrough at the bottom of the\
  \ article \U0001F447, as well as a 15 second video in the middle for those of you\
  \ who just want a quick s..."
---

Dans cet article, nous allons créer des arrière-plans de site web plus intéressants en utilisant des effets granulaires. 

Il y a une vidéo complète à la fin de l'article 👇, ainsi qu'une vidéo de 15 secondes au milieu pour ceux qui veulent un résumé rapide.

Nous allons couvrir cela de deux manières :

1. En utilisant une image PNG avec transparence comme sur le site ci-dessous.
2. En utilisant notre propre image SVG et code

## Comment créer un arrière-plan granulaire en utilisant une image PNG granulaire

Tout d'abord, l'approche PNG.

Je suis tombé sur cet arrière-plan l'autre jour sur le [site d'Arc](https://arc.net/), et j'étais intrigué. J'avais déjà vu des [illustrations de type granulaire](https://dribbble.com/tags/grainy) et des couleurs auparavant, et j'en avais même fait quelques-unes dans Illustrator. Mais cela m'a fait me demander comment produire le même effet en tant qu'arrière-plan sur un site web.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-15-at-10.20.48-AM.png)
_Capture d'écran de l'arrière-plan granulaire de https://arc.net/_

L'inspection de cela m'a montré qu'ils utilisaient deux choses : un `background: var(--colors-primary3)` et un `background-image: url(noise.png);` :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-15-at-10.28.24-AM.png)

Le fichier `.noise.png` était simplement une image granulaire avec transparence pour que la couleur unie de l'arrière-plan CSS puisse apparaître :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-15-at-10.33.09-AM.png)
_Capture d'écran de l'image noise.png_

## Comment recréer le bruit PNG

Téléchargeons le [fichier noise.png](https://arc.net/noise.png). Ensuite, créons un document HTML. Nous allons ajouter une section pour l'afficher :

```html
<section class="container noise">
	<h1>Bruit avec PNG</h1>
</section>
```

Dans notre CSS, nous allons ajouter un style de base pour le conteneur :

```css
.container{
    margin: 0 auto;
    display: flex;
    width: 100%;
    min-height: 33vh;
    justify-content: center;
    align-items: center;
}
```

Puis, pour notre classe `.noise` :

```css
.noise{
    background: rgb(182, 34, 58);
    background-image: url(/assets/noise.png);
}
```

Et voilà ! Nous avons le même effet :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-15-at-11.05.15-AM.png)

Assez astucieux, mais j'ai creusé plus loin et j'ai trouvé comment créer la texture bruyante elle-même ainsi que la générer en ligne dans notre code.

## Qu'est-ce que les SVGs ? Avec un aperçu vidéo

Tout d'abord, un résumé vidéo de 15 secondes de la partie en ligne (la vidéo complète de 10 minutes est à la fin de l'article) :

%[https://youtube.com/shorts/P4ByGInNhqI]

Les SVGs sont des graphiques vectoriels scalables.

Ils sont pratiques car ils peuvent être redimensionnés sans perdre en qualité. Et ils sont polyvalents car vous pouvez les marquer avec du code tout comme vous pouvez utiliser CSS pour apporter des changements stylistiques à votre HTML.

En fait, vous pouvez même coder en dur un SVG directement dans votre HTML ou CSS.

Ci-dessous, je vais vous montrer trois choses :

1. Comment créer un fichier SVG à référencer de manière similaire au PNG ci-dessus.
2. Comment utiliser un fichier SVG pour créer un arrière-plan granulaire
3. Comment coder le SVG granulaire directement dans CSS pour appliquer l'effet granulaire aux éléments de notre HTML.

## Comment créer un SVG

Le [Grainy Gradient Playground](https://grainy-gradients.vercel.app/) a été très utile lors de cette recherche. Il permet la création rapide de ces SVGs.

Examinons le code du SVG qu'ils utilisent :

```html
<!-- svg: première couche -->
<svg viewBox='0 0 250 250' xmlns='http://www.w3.org/2000/svg'>
  <filter id='noiseFilter'>
    <feTurbulence 
      type='fractalNoise' 
      baseFrequency='1' 
      numOctaves='3' 
      stitchTiles='stitch'/>
  </filter>
  
  <rect width='100%' height='100%' filter='url(#noiseFilter)'/>
</svg>
```

La première ligne configure le SVG avec une viewBox initiale.

```html
<svg viewBox='0 0 250 250' xmlns='http://www.w3.org/2000/svg'>
```

Ensuite, le filtre est configuré et reçoit un identifiant. Nous utilisons le filtre `feTurbulence` pour créer l'effet granulaire. MDN, comme toujours, a plus d'informations sur les détails de [feTurbulence](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feTurbulence).

```
<feTurbulence 
      type='fractalNoise' 
      baseFrequency='1' 
      numOctaves='3' 
      stitchTiles='stitch'/>
  </filter>
```

Ensuite, nous définissons la forme (un rectangle), la taille (100 %) et appliquons le filtre `feTurbulence` :

```
<rect width='100%' height='100%' filter='url(#noiseFilter)'/>
```

Si nous ajoutons cela dans notre HTML maintenant, cela s'affichera comme un simple bruit :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-15-at-11.17.46-AM.png)
_Image de bruit SVG feTurbulence_

## Comment utiliser un SVG comme image d'arrière-plan

Parce que les SVGs sont essentiellement du code, nous pouvons créer un fichier `noise.svg` dans notre projet, et copier le contenu de l'exemple SVG.

Nous allons créer une autre `div` pour cette méthode dans notre HTML :

```html
<section class="container noise2">
	<h1>Bruit utilisant un fichier SVG</h1>
</section>
```

J'ai changé `baseFrequency='1'` dans le fichier SVG pour des raisons d'apparence, puis j'ai ajouté ce qui suit à notre CSS :

```css
.noise2{
    background: rgb(219, 255, 219);
    background-image: url(/assets/noise.svg);
}
```

Cela nous donne un résultat similaire pour notre section d'arrière-plan verte :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-15-at-11.38.04-AM.png)

## Filtre SVG en ligne CSS

Enfin, nous avons la possibilité de nous passer du fichier de bruit séparé en mettant le SVG en ligne.

Dans le Gradient Playground, vous verrez l'option pour cela dans la troisième boîte CSS+Gradient+CSSFilter, et il y a un interrupteur pour produire le CSS en ligne directement :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-15-at-11.40.37-AM.png)
_Capture d'écran du Grainy Gradient Playground_

Il utilise des dégradés allant de l'opaque au transparent pour permettre au bruit de apparaître. Vous pouvez obtenir le même effet sur un arrière-plan de couleur unie en répétant une partie de notre code ci-dessus.

Nous allons créer une troisième `div` pour cet exemple :

```html
<section class="container noise3">
	<h1>Bruit avec SVG en ligne</h1>
</section>
```

Ensuite, nous pouvons convertir le SVG en un format utilisable dans notre CSS en utilisant un encodeur URL [comme celui-ci](https://yoksel.github.io/url-encoder/). (Vous pouvez également copier à partir de la boîte Grainy Gradient Playground où le même code est généré).

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-15-at-11.23.35-AM.png)
_Capture d'écran de l'encodeur URL pour le code SVG_

Et juste comme cela, nous avons dans les parenthèses de l'URL le code que nous pouvons utiliser pour notre `background-image`. Ainsi, le CSS pour notre `div` ressemble à ceci (j'ai modifié la baseFrequency pour obtenir un aspect plus fin) :

```css
.noise3{
    background:rgb(68,0,255);
	background-image: url("data:image/svg+xml,%3C!-- svg: first layer --%3E%3Csvg viewBox='0 0 250 250' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='4' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-15-at-11.35.14-AM.png)

Les paramètres sont facilement modifiables sur tous ces SVGs et filtres pour produire différents effets granulaires. J'espère que ce tutoriel vous a été utile pour pimenter facilement vos arrière-plans !

## Vidéo de démonstration

Voici la vidéo de démonstration de tout ce qui précède :

%[https://youtu.be/vi-vi4_UpqM]

Envisagerez-vous de vous abonner à ma [chaîne YouTube](https://www.youtube.com/@eamonncottrell) ? Je crée plus de contenu comme celui-ci, et je m'amuse beaucoup !

Vous pouvez également me trouver sur [LinkedIn](https://www.linkedin.com/in/eamonncottrell/) 👋.

Vous êtes génial ; passez une excellente journée !