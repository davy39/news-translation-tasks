---
title: CSS Overflow – Visible, Scroll, Auto, ou Hidden ? La Propriété Overflow Expliquée
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-02-17T20:37:54.000Z'
originalURL: https://freecodecamp.org/news/css-overflow-visible-scroll-auto-hidden
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/css-overflow.png
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: CSS Overflow – Visible, Scroll, Auto, ou Hidden ? La Propriété Overflow
  Expliquée
seo_desc: "In this tutorial, we will talk about an important CSS property – the overflow\
  \ property. \nIt helps us control what happens when an element's content is too\
  \ big to fit into an area. When this happens, it makes the content \"overflow\"\
  \ into another area, ..."
---

Dans ce tutoriel, nous allons parler d'une propriété CSS importante – la propriété `overflow`.

Elle nous aide à contrôler ce qui se passe lorsque le contenu d'un élément est trop grand pour tenir dans une zone. Lorsque cela se produit, cela fait "déborder" le contenu dans une autre zone, soit horizontalement (axe X), soit verticalement (axe Y).

Nous allons passer en revue les valeurs suivantes de la propriété overflow et voir comment elles fonctionnent :

* `visible`
* `hidden`
* `scroll`
* `auto`

## Comment utiliser la valeur `visible`

Il s'agit de la valeur par défaut que prend la propriété `overflow` si aucune n'est spécifiée. Avec cette propriété, nous pouvons voir clairement notre contenu lorsqu'il déborde dans une autre zone.

Considérons les exemples suivants :

```html
<div>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Error quas
        repellendus reprehenderit libero labore dolor omnis! Obcaecati ipsam est
        accusantium quis quos minus veniam eaque? Modi expedita mollitia et qui!
      </p>
</div>
```

```css
body{
    background: black;
}

div{
    height: 200px;
    width: 200px;
    background: white;
}

p{
    color: green;
}
```

C'est assez basique. Nous avons donné à notre page une couleur de fond noire. Nous avons défini la couleur de fond de notre élément `div`, qui agit comme un conteneur, en blanc. Il a une hauteur et une largeur de 200px chacune. Ensuite, nous avons rendu la couleur du texte de notre paragraphe verte.

Voici à quoi cela ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--238-.png)

Le texte s'insère confortablement dans le conteneur blanc sans franchir la bordure du conteneur sur les deux axes. Mais ce n'est pas toujours le cas.

Vous pourriez travailler sur un projet et réaliser qu'un morceau de texte franchit la bordure. Quelque chose comme ceci :

```html
<div>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Error quas
        repellendus reprehenderit libero labore dolor omnis! Obcaecati ipsam est
        accusantium quis quos minus veniam eaque? Modi expedita mollitia et qui!
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Error quas
        repellendus reprehenderit libero labore dolor omnis! Obcaecati ipsam est
        accusantium quis quos minus veniam eaque? Modi expedita mollitia et qui!
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Error quas
        repellendus reprehenderit libero labore dolor omnis! Obcaecati ipsam est
        accusantium quis quos minus veniam eaque? Modi expedita mollitia et qui!
      </p>
</div>
```

Les styles CSS restent les mêmes. Maintenant, regardez ce qui se passe avec le conteneur et le texte :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--241-.png)

Le texte ne peut pas tenir dans le conteneur blanc, donc il déborde et franchit la bordure du conteneur. Dans un projet réel, cela serait encore plus gênant car vous auriez ce texte qui chevauche d'autres éléments sur la page.

Nous sommes en mesure de voir le texte déborder dans une autre zone car la valeur par défaut ici est `visible`, même si nous ne l'avons pas spécifiée.

Continuons et ajoutons cela à notre CSS pour que vous puissiez voir la propriété `overflow` appliquée :

```css
body{
    background: black;
}

div{
    height: 200px;
    width: 200px;
    background: white;
    overflow: visible;
}

p{
    color: green;
}
```

Nous avons ajouté `overflow: visible;` au `div`. Le résultat reste le même – nous verrions notre texte déborder dans une autre zone.

Dans la section suivante, nous verrons les différentes valeurs qui peuvent nous aider à contrôler ce qui se passe lorsque le contenu déborde.

## Comment utiliser la valeur `hidden`

Avec la valeur `hidden`, la partie du texte qui a débordé sera coupée – elle sera "invisible". Vous n'avez pas à vous soucier de l'espace que le débordement occupait. Une fois le contenu coupé, il ne sera plus dans la zone où il débordait.

Nous allons examiner un exemple avant de parler de pourquoi ce n'est pas la meilleure solution. Ajoutons la valeur `hidden` :

```css
body{
    background: black;
}

div{
    height: 200px;
    width: 200px;
    background: white;
    overflow: hidden;
}

p{
    color: green;
}
```

Voici ce qui arrive au texte dans le conteneur :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--243-.png)

Comme vous pouvez le voir, nous ne pouvons plus voir cette partie du texte qui franchit la bordure du conteneur.

Cela résout le problème d'avoir du contenu dans une zone où il n'est pas censé être, mais cela ne fournit pas de moyen d'accéder au contenu qui a été coupé. Nous allons donc aborder cela dans la section suivante.

## Comment utiliser la valeur `scroll`

Nous savons déjà que la valeur `hidden` coupe le texte et le cache. Mais la valeur `scroll` coupe également le texte et fournit une barre de défilement afin que nous puissions faire défiler et voir la partie du texte qui a été coupée.

Regardons cela :

```css
body{
    background: black;
}

div{
    height: 200px;
    width: 200px;
    background: white;
    overflow: scroll;
}

p{
    color: green;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--244-.png)

Maintenant, nous avons des barres de défilement sur les deux axes. La barre de défilement horizontale n'est pas pertinente pour nous car nous n'avons pas de contenu débordant dans cette direction. Nous allons corriger cela dans la section suivante.

## Comment utiliser la valeur `auto`

```css
body{
    background: black;
}

div{
    height: 200px;
    width: 200px;
    background: white;
    overflow: auto;
}

p{
    color: green;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--245-.png)

Maintenant, la barre de défilement n'apparaît que verticalement. La valeur `auto` détecte où le débordement se produit et ajoute une barre de défilement dans cette direction.

Aucune barre de défilement n'a été ajoutée horizontalement car nous n'avons pas de débordement de contenu sur cet axe. De même, si nous n'avons pas de débordement sur les deux axes, aucune barre de défilement ne sera ajoutée.

## Propriétés `overflow-x` et `overflow-y`

Dans les exemples que nous avons utilisés dans les sections précédentes, nous avons utilisé la propriété `overflow`. Cela s'applique à la fois à l'axe horizontal et vertical. Si vous préférez vérifier le débordement séparément, vous pouvez utiliser celles-ci :

* `overflow-x` spécifie ce qui se passe lorsque le contenu déborde horizontalement (de gauche à droite).  
* `overflow-y` spécifie ce qui se passe lorsque le contenu déborde verticalement (de haut en bas).  

Les mêmes valeurs – `visible`, `hidden`, `scroll` et `auto` – peuvent être utilisées ici également.

Un exemple rapide :

```css
div {
  overflow-x: hidden; /* le débordement est visible sur l'axe x */
  overflow-y: scroll; /* une barre de défilement est ajoutée lorsqu'il y a un débordement sur l'axe y */
}
```

## Conclusion

Dans ce tutoriel, nous avons appris à contrôler le débordement de contenu sur nos pages. Nous avons vu les différentes valeurs que nous pouvons attribuer à la propriété `overflow` et les différents résultats que ces valeurs produisent.

Enfin, nous avons appris à appliquer les valeurs de la propriété `overflow` soit sur la direction horizontale, soit sur la direction verticale uniquement.

Bon codage !