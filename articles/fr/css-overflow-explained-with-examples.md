---
title: CSS Overflow Expliqué avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/css-overflow-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d29740569d1a4ca363e.jpg
tags:
- name: CSS
  slug: css
- name: CSS3
  slug: css3
- name: toothbrush
  slug: toothbrush
seo_title: CSS Overflow Expliqué avec des Exemples
seo_desc: 'The overflow property controls what happens if an element''s content overflows
  from its set width and height. It is shorthand for the overflow-x and overflow-y
  properties. Note that this property only works for block elements with a specified
  height.

  ...'
---

La propriété `overflow` contrôle ce qui se passe si le contenu d'un élément dépasse sa largeur et sa hauteur définies. Elle est une abréviation pour les propriétés `overflow-x` et `overflow-y`. Notez que cette propriété ne fonctionne que pour les éléments de bloc avec une hauteur spécifiée.

Avec `overflow`, vous pouvez contrôler si le contenu doit être rogné ou si des barres de défilement doivent être ajoutées lorsque le contenu d'un élément est trop grand pour tenir dans une zone spécifiée.

## **Valeurs**

* `visible` : Il s'agit de la valeur par défaut de la propriété. Aucun contenu n'est rogné lorsqu'il est plus grand que ses dimensions définies.
* `hidden` : Le contenu qui dépasse est masqué.
* `scroll` : Le contenu est masqué, mais les utilisateurs peuvent toujours faire défiler et voir le contenu masqué.
* `auto` : Si le contenu est plus grand que ses dimensions définies, le contenu sera automatiquement masqué et une barre de défilement apparaîtra.
* `initial` : Utilise la valeur par défaut pour cette propriété, `visible`.
* `inherit` : Utilise la valeur de débordement de l'élément parent.

## **Exemples**

Voici le HTML et le CSS que nous utiliserons pour tous les exemples suivants :

```html
<div class="box-element">
  <p>
    Qui sont les bébés chats sont gras j'aime les caresser ils aiment miauler en retour. Attaquer le chien puis faire comme si rien ne s'était passé kitty ipsum dolor sit amet, perdre ses poils partout perdre ses poils partout s'étirer attaquer vos chevilles courir après le point rouge, boule de poils courir herbe à chat manger l'herbe renifler, voir le propriétaire, courir en terreur. Frotter son visage sur tout les chats sont le monde. Miaou miaou, je dis à mon humain que je règne sur mon dos tu frottes mon ventre je te mords fort la meilleure chose dans l'univers est une boîte en carton si ça sent le poisson mange autant que tu veux et bois soigneusement de l'eau du verre puis renverse-la partout et procède à lécher la flaque. Patte sur le scarabée et mange-le avant qu'il ne s'échappe frotter son derrière sur la table pour mâcher sa patte, ou t'aimer, puis te mordre et bondir sur une personne sans méfiance. Quel trophée de chat ! gifle du chat sur le visage du chien laisse-moi entrer laisse-moi sortir laisse-moi entrer laisse-moi sortir laisse-moi entrer laisse-moi sortir qui a cassé cette porte de toute façon pour parader sur le dessus de la clôture du jardin, ennuyer le chien du voisin et le faire aboyer et mâcher le cordon d'alimentation de l'iPad ronronner.
  <p>
</div>
```

```css
.box-element {
  width: 400px;
  height: 200px;
  border: dashed;
}

.box-element {
  /* overflow sera défini ici */
}
```

### **Visible :**

```css
.box-element {
  overflow: visible;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-152.png)

### **Masqué :**

```css
.box-element { 
  overflow: hidden; 
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-153.png)

### **Défilement :**

```css
.box-element { 
  overflow: scroll; 
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-154.png)

### **Auto :**

```css
.box-element { 
  overflow: auto; 
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-155.png)

## **overflow-x et overflow-y**

* `overflow-x` : Permet à l'utilisateur de faire défiler le contenu qui s'étend au-delà de la hauteur de l'élément de boîte.
* `overflow-y` : Permet à l'utilisateur de faire défiler le contenu qui s'étend au-delà de la largeur de la boîte.

```css
.box-element {
  overflow-x: scroll;
  overflow-y: auto;
}
```

Et le `.box-element` ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-157.png)

Si le contenu dépasse l'axe Y, alors ce contenu sera masqué, tandis qu'une barre de défilement devrait être visible pour que les utilisateurs puissent lire le reste du contenu.