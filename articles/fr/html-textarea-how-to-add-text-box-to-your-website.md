---
title: HTML textarea – Comment ajouter une balise de type zone de texte à votre site
  web
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-08-26T16:21:53.000Z'
originalURL: https://freecodecamp.org/news/html-textarea-how-to-add-text-box-to-your-website
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cover-template--3-.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: HTML textarea – Comment ajouter une balise de type zone de texte à votre
  site web
seo_desc: A text box is a section of your website where users can enter text. A blinking
  cursor appears when you click or tap on or inside the text box, indicating that
  you are ready to begin typing. And an on-screen keyboard will appear if you're using
  a tabl...
---

Une zone de texte est une section de votre site web où les utilisateurs peuvent saisir du texte. Un curseur clignotant apparaît lorsque vous cliquez ou tapez sur ou à l'intérieur de la zone de texte, indiquant que vous êtes prêt à commencer à taper. Et un clavier à l'écran apparaîtra si vous utilisez une tablette ou un smartphone.

Les zones de texte sont classées en deux types : les champs de texte et les zones de texte. Ces deux types de zones de texte servent à des fins différentes et aident l'utilisateur à comprendre ce qu'il doit taper dans la zone de texte.

Un champ de texte est une petite boîte, généralement rectangulaire, où vous pouvez saisir une seule ligne de texte, comme un nom, un numéro ou tout autre type de texte court.

Une zone de texte est une boîte plus grande où vous pouvez saisir plusieurs lignes de texte, comme des descriptions, des paragraphes, etc.

Lorsque vous appuyez sur le bouton Entrée dans un champ de texte, le curseur se déplacera soit vers le champ suivant, soit soumettra le formulaire. Dans une zone de texte, en revanche, le curseur se déplacera vers une nouvelle ligne, créant ainsi un saut de ligne.

![](https://paper-attachments.dropbox.com/s_64572030E8D25CA21F18BD5EC8523ECF39BB95CA9E14781CDD6E156EE366692C_1661531495728_Untitled.drawio+1.png align="left")

## Comment ajouter un champ de texte à votre site web

Chaque fois que vous souhaitez qu'un utilisateur saisisse quelque chose dans une page web, vous pouvez utiliser la balise `<input>`. Ensuite, pour vous assurer qu'il s'agit d'un champ de texte, vous pouvez ajouter l'attribut type avec la valeur `text` :

```html
<form>
  <input type='text' />
</form>
```

Cela affichera un champ de texte sur une seule ligne dans notre page web, qui peut accepter toutes les formes de valeurs textuelles. Nous pouvons également ajouter une balise label ou d'autres attributs comme l'attribut `placeholder` pour indiquer aux utilisateurs ce qu'ils doivent saisir dans le champ de texte.

```html
<form>
  <input type='text' placeholder='Entrez votre nom...' />
</form>

Ou

<form>
  <label>Nom :</label> </br>
  <input type='text' />
</form>
```

Il existe de nombreux autres attributs que nous pouvons définir sur un champ de texte, tels que `maxlength` et `minlength`, pour aider à définir la quantité maximale ou minimale de texte qu'un champ peut accepter.

```html
<form>
  <input type='text' maxlength="100" minlength="10" placeholder='Entrez votre nom' />
</form>
```

Nous pouvons également passer des valeurs par défaut à notre champ de texte avec l'attribut value :

```html
<form>
  <input type='text' value='John Doe' placeholder='Entrez votre nom...' />
</form>
```

![](https://paper-attachments.dropbox.com/s_64572030E8D25CA21F18BD5EC8523ECF39BB95CA9E14781CDD6E156EE366692C_1661546622536_image.png align="left")

## Comment ajouter une zone de texte à votre site web

Une zone de texte est définie par une balise `<textarea>`. Vous l'utilisez pour collecter du texte multilingue illimité comme des commentaires ou des avis.

Vous spécifiez la taille d'une zone de texte par les attributs `cols` et `rows` (ou avec CSS).

```html
<form>
  <textarea rows="5" cols="33"></textarea>
</form>
```

Le champ textarea n'utilise pas l'attribut value pour passer des valeurs par défaut, mais vous pouvez placer du contenu par défaut entre les balises d'ouverture et de fermeture.

```html
<form>
  <textarea rows="5" cols="33">
    Ceci est le commentaire par défaut...  
  </textarea>
</form>
```

![](https://paper-attachments.dropbox.com/s_64572030E8D25CA21F18BD5EC8523ECF39BB95CA9E14781CDD6E156EE366692C_1661546930588_image.png align="left")

Comme les balises input, nous pouvons ajouter les attributs `maxlength`, `minlength` et `placeholder` au champ textarea.

```html
<form>
  <textarea placeholder='Entrez un commentaire...' maxlength='1000' minlength='100'>
    Ceci est le commentaire par défaut...  
  </textarea>
</form>
```

## Conclusion

Dans cet article, vous avez appris comment ajouter une zone de texte à votre site web en utilisant les balises `<textarea/>` et `<input/>`, selon le `type` de `texte` que vous souhaitez ajouter.

Vous pouvez en apprendre davantage sur les balises HTML dans les ressources suivantes :

* [HTML pour débutants - freeCodeCamp](https://www.freecodecamp.org/news/html-crash-course/#:~:text=Common%20HTML%20Tags&text=html%20%3A%20After%20the%20doctype%2C%20all,the%20name%20of%20your%20page.)
    
* [Qu'est-ce que les balises HTML et comment les utiliser ?](https://www.freecodecamp.org/news/html-elements-explained-what-are-html-tags/)
    
* [Feuille de référence HTML – Liste des éléments HTML](https://www.freecodecamp.org/news/html-cheat-sheet-html-elements-list-reference/)
    

Amusez-vous bien en codant !