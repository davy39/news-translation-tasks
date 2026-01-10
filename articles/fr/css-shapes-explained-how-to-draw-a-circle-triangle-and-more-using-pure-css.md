---
title: 'Explication des formes CSS : comment dessiner un cercle, un triangle et plus
  encore en utilisant du CSS pur'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-05T10:22:12.000Z'
originalURL: https://freecodecamp.org/news/css-shapes-explained-how-to-draw-a-circle-triangle-and-more-using-pure-css
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/delila-ziebart-b0GSCFJ-Gzg-unsplash.jpg
tags:
- name: CSS
  slug: css
seo_title: 'Explication des formes CSS : comment dessiner un cercle, un triangle et
  plus encore en utilisant du CSS pur'
seo_desc: "By Thomas Weibenfalk\nBefore we start. If you want more free content but\
  \ in video format. Don't miss out on my Youtube channel where I publish weekly videos\
  \ on FrontEnd coding.   \nhttps://www.youtube.com/user/Weibenfalk  \n\nAre you new\
  \ to web developme..."
---

Par Thomas Weibenfalk

Avant de commencer. Si vous voulez plus de contenu gratuit mais en format vidéo. Ne manquez pas ma chaîne YouTube où je publie des vidéos hebdomadaires sur le codage FrontEnd.   
  
[https://www.youtube.com/user/Weibenfalk](https://www.youtube.com/user/Weibenfalk)  
  
----------  
  
Êtes-vous nouveau dans le développement web et CSS ? Vous êtes-vous déjà demandé comment ces belles formes que vous voyez partout sur Internet sont réalisées ? Ne vous demandez plus. Vous êtes au bon endroit.

Ci-dessous, je vais expliquer les bases de la création de formes avec CSS. Il y a **beaucoup** de choses à vous dire sur ce sujet ! Par conséquent, je ne couvrirai pas tous les outils et formes (loin de là), mais cela devrait vous donner une idée de base de la manière dont les formes sont créées avec CSS.

Certaines formes nécessitent plus de "fix et astuces" que d'autres. La création de formes avec CSS est généralement une combinaison d'utilisation de **width, height, top, right, left, border, bottom, transform** et de pseudo-éléments comme **:before** et **:after**. Nous avons également des propriétés CSS plus modernes pour créer des formes comme **shape-outside** et **clip-path**. J'écrirai à leur sujet ci-dessous également.

## **Formes CSS - La méthode de base**

En utilisant quelques astuces en CSS, nous avons toujours été capables de créer des formes de base comme des carrés, des cercles et des triangles avec des propriétés CSS régulières. Regardons quelques-unes d'entre elles maintenant.

### Carrés et rectangles

Les carrés et les rectangles sont probablement les formes les plus faciles à réaliser. Par défaut, une div est toujours un carré ou un rectangle. 

Vous définissez la largeur et la hauteur comme montré dans le code ci-dessous. Ensuite, il suffit de donner à l'élément une couleur de fond. Vous pouvez avoir toutes les autres propriétés que vous voulez sur l'élément.  


```css
#square {
    background: lightblue;
    width: 100px;
    height: 100px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/square.png)
_Un carré CSS_

###   
Cercles

Créer un cercle est presque aussi facile. Pour créer un cercle, nous pouvons définir le border-radius sur l'élément. Cela créera des coins courbés sur l'élément. 

Si nous le définissons à 50%, cela créera un cercle. Si vous définissez une largeur et une hauteur différentes, nous obtiendrons un ovale à la place.

```css
#circle {
    background: lightblue;
    border-radius: 50%;
    width: 100px;
    height: 100px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/circle.png)
_Un cercle CSS_

### Triangles

Les triangles sont un peu plus délicats. Nous devons définir les bordures de l'élément pour correspondre à un triangle. En définissant la largeur et la hauteur à zéro sur l'élément, la largeur réelle de l'élément sera la largeur de la bordure. 

Gardez à l'esprit que les bords de la bordure sur un élément sont des diagonales à 45 degrés les unes par rapport aux autres. C'est pourquoi cette méthode fonctionne pour créer un triangle. En définissant une des bordures à une couleur solide et les autres bordures à transparentes, cela prendra la forme d'un triangle. 

![Image](https://www.freecodecamp.org/news/content/images/2020/01/borders.png)
_Les bordures CSS ont des bords anguleux_

```css
#triangle {
    width: 0;
    height: 0;
    border-left: 40px solid transparent;
    border-right: 40px solid transparent;
    border-bottom: 80px solid lightblue;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/triangle.png)
_Un triangle CSS_

Si vous voulez avoir un triangle/flèche pointant dans une autre direction, vous pouvez changer les valeurs de bordure correspondant au côté que vous voulez rendre visible. Ou vous pouvez faire pivoter l'élément avec la propriété _transform_ si vous voulez être vraiment élégant.

```css
 #triangle {
     width: 0;
     height: 0;
     border-top: 40px solid transparent;
     border-right: 80px solid lightblue;
     border-bottom: 40px solid transparent;
 }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/triangle2.png)
_Un autre triangle CSS_

D'accord – c'est une introduction aux formes de base avec CSS. Il y a probablement une infinité de formes que vous pouvez imaginer créer. Ce ne sont que les bases, mais avec un peu de créativité et de détermination, vous pouvez réaliser beaucoup avec juste les propriétés CSS de base. 

Dans certains cas, avec des formes plus avancées, il est également bon d'utiliser les sélecteurs pseudo :after et :before. Cela dépasse le cadre de cet article, car mon intention est de couvrir les bases pour vous lancer.

### Inconvénient

**Il y a un grand inconvénient avec l'approche ci-dessus.** Par exemple, si vous voulez que votre texte s'écoule autour de votre forme. Une div HTML régulière avec un fond et des bordures pour constituer la forme ne permettra pas cela. Le texte ne s'adaptera pas et ne s'écoulera pas autour de votre forme. Au lieu de cela, il s'écoulera autour de la div elle-même (qui est un carré ou un rectangle).

Ci-dessous se trouve une illustration montrant le triangle et comment le texte s'écoulera. 

![Image](https://www.freecodecamp.org/news/content/images/2020/01/textflow-bad.png)

Heureusement, nous avons quelques propriétés CSS modernes à utiliser à la place. 

## Formes CSS - L'autre méthode

De nos jours, nous avons une propriété appelée **shape-outside** à utiliser en CSS. Cette propriété vous permet de définir une forme autour de laquelle le texte s'enroulera/s'écoulera. 

Avec cette propriété, nous avons quelques formes de base :   
  
**inset()**  
**circle()  
ellipse()  
polygon()**

**Voici un conseil** : Vous pouvez également utiliser la propriété **clip-path**. Vous pouvez créer votre forme avec cela de la même manière, mais cela ne permettra pas au texte de s'enrouler autour de votre forme comme le fait shape-outside.

L'élément auquel nous allons appliquer la forme avec la propriété shape-outside doit être flottant. Il doit également avoir une largeur et une hauteur définies. **C'est vraiment important à savoir !**

Vous pouvez lire plus sur pourquoi [ici](https://developer.mozilla.org/en-US/docs/Web/CSS/shape-outside). Ci-dessous se trouve également un texte que j'ai tiré du lien fourni vers developer.mozilla.org.

> La propriété `shape-outside` est spécifiée en utilisant les valeurs de la liste ci-dessous, qui définissent la zone de flottement pour les éléments flottants. La zone de flottement détermine la forme autour de laquelle le contenu en ligne (éléments flottants) s'enroule.

### inset()

Le type inset() peut être utilisé pour créer un rectangle/carré avec un décalage optionnel pour le texte d'enroulement. Il vous permet de fournir des valeurs sur la quantité de chevauchement que vous voulez que votre texte d'enroulement ait avec la forme. 

Vous pouvez spécifier le décalage pour qu'il soit le même pour les quatre directions comme ceci : **inset(20px).** Ou il peut être défini individuellement pour chaque direction : **inset(20px 5px 30px 10px)**. 

Vous pouvez utiliser d'autres unités également pour définir le décalage, par exemple, le pourcentage. Les valeurs correspondent comme ceci : **inset(haut droite bas gauche)**_**.**_

Consultez l'exemple de code ci-dessous. J'ai spécifié les valeurs inset à 20px en haut, 5px à droite, 30px en bas et 10px à gauche. Si vous voulez que votre texte contourne votre carré, vous pouvez simplement sauter l'utilisation de inset(). Au lieu de cela, définissez le fond de votre div et spécifiez la taille comme d'habitude.

```css
 #square {
     float: left;
     width: 100px;
     height: 100px;
     shape-outside: inset(20px 5px 30px 10px);
     background: lightblue;
 }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/inset.png)
_Le texte est décalé par les valeurs spécifiées. Dans ce cas, 20px en haut, 5px à droite, 30px en bas et 10 px à gauche_

Il est également possible de donner à inset() une deuxième valeur qui spécifie le border-radius de l'inset. Comme ci-dessous :

```css
 #square {
     float: left;
     width: 100px;
     height: 100px;
     shape-outside: inset(20px 5px 30px 10px round 50px);
     background: lightblue;
 }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/inset2.png)
_border-radius défini à 50px sur l'inset_

### circle()

Dans cet exemple, un cercle est créé en utilisant la propriété **shape-outside**. Vous devez également appliquer un **clip-path** avec la propriété correspondante pour que le cercle apparaisse. 

La propriété **clip-path** peut prendre la même valeur que la propriété shape-outside, donc nous pouvons lui donner la forme standard **circle()** que nous avons utilisée pour **shape-outside**. Notez également que j'ai appliqué une marge de 20px sur l'élément ici pour donner de l'espace au texte.

```css
#circle {
    float: left;
    width: 300px;
    height: 300px;
    margin: 20px;
    shape-outside: circle();
    clip-path: circle();
    background: lightblue;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/circle-shape-margin-1.png)
_Le texte s'écoule autour de la forme !_

Dans l'exemple ci-dessus, je ne spécifie pas le rayon du cercle. Cela est dû au fait que je veux qu'il soit aussi grand que la div (300px). Si vous voulez spécifier une taille différente pour le cercle, vous pouvez le faire. 

Le circle() prend deux valeurs. La première valeur est le rayon et la deuxième valeur est la position. Ces valeurs spécifieront le centre du cercle. 

Dans l'exemple ci-dessous, j'ai défini le rayon à 50%. Ensuite, j'ai décalé le centre du cercle de 30%. Notez que le mot "at" doit être utilisé entre les valeurs de rayon et de position. 

J'ai également spécifié une autre valeur de position sur le clip-path. Cela coupera le cercle en deux lorsque je déplace la position à zéro.

```css
 #circle {
      float: left;
      width: 150px;
      height: 150px;
      margin: 20px;
      shape-outside: circle(50% at 30%);
      clip-path: circle(50% at 0%);
      background: lightblue;
    }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/circle2.png)

### ellipse()

Les ellipses fonctionnent de la même manière que les cercles, sauf qu'elles créent un ovale. Vous pouvez définir à la fois la valeur X et la valeur Y, comme ceci : **ellipse(25px  50px).**

Comme pour un cercle, il prend également une valeur de position comme dernière valeur.

```css
   #ellipse {
      float: left;
      width: 150px;
      height: 150px;
      margin: 20px;
      shape-outside: ellipse(20% 50%);
      clip-path: ellipse(20% 50%);
      background: lightblue;
    }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/ellipse.png)

### polygon()

Un polygone est une forme avec différents sommets/coordonnées définis. Ci-dessous, je crée une forme "T" qui est la première lettre de mon nom. Je commence par les coordonnées 0,0 et je me déplace de gauche à droite pour créer la forme "T".

```css
#polygon {
      float: left;
      width: 150px;
      height: 150px;
      margin: 0 20px;
      shape-outside: polygon(
        0 0,
        100% 0,
        100% 20%,
        60% 20%,
        60% 100%,
        40% 100%,
        40% 20%,
        0 20%
      );
      clip-path: polygon(
        0 0,
        100% 0,
        100% 20%,
        60% 20%,
        60% 100%,
        40% 100%,
        40% 20%,
        0 20%
      );
      background: lightblue;
    }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/polygon_t.png)

### Images

Vous pouvez également utiliser des images avec des fonds transparents pour créer votre forme. Comme cette belle lune ronde ci-dessous.

Il s'agit d'une image .png avec un fond transparent.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/moon.png)

```html
<img src="src/moon.png" id="moon" />
```

```css
#moon {
      float: left;
      width: 150px;
      height: 150px;
      shape-outside: url("./src/moon.png");
    }
```



![Image](https://www.freecodecamp.org/news/content/images/2020/01/moon2.png)

Et c'est tout ! Merci d'avoir lu.

## À propos de l'auteur de cet article

Je m'appelle Thomas Weibenfalk et je suis un développeur de Suède. Je crée régulièrement des tutoriels gratuits sur ma chaîne YouTube. Il y a également quelques cours premium sur React et Gatsby. N'hésitez pas à me rendre visite sur ces liens :

Twitter — [@weibenfalk](https://twitter.com/weibenfalk),  
Weibenfalk sur [YouTube](https://www.youtube.com/c/weibenfalk),  
Weibenfalk [Site Web des Cours](https://www.weibenfalk.com).