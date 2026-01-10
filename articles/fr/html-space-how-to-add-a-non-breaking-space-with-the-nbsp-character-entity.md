---
title: Espace HTML – Comment ajouter une espace insécable avec l'entité de caractère
  &nbsp;
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-19T17:29:46.000Z'
originalURL: https://freecodecamp.org/news/html-space-how-to-add-a-non-breaking-space-with-the-nbsp-character-entity
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/space.png
tags:
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Espace HTML – Comment ajouter une espace insécable avec l'entité de caractère
  &nbsp;
seo_desc: "In HTML, you can't create an extra blank space after the space ( ) character\
  \ with the spacebar. If you want 10 blank spaces in your HTML code and you try to\
  \ add them with the spacebar, you'll only see one space in the browser. \nAlso,\
  \ one or more of t..."
---

En HTML, vous ne pouvez pas créer d'espace vide supplémentaire après le caractère espace (` `) avec la barre d'espace. Si vous voulez 10 espaces vides dans votre code HTML et que vous essayez de les ajouter avec la barre d'espace, vous ne verrez qu'un seul espace dans le navigateur. 

De plus, un ou plusieurs des mots qui sont censés être ensemble peuvent se séparer en une nouvelle ligne.

Ainsi, dans cet article, je vais vous montrer comment créer autant d'espaces vides que vous le souhaitez dans votre code, et comment ajouter une espace insécable avec l'entité de caractère `&nbsp;`.

## D'abord, que sont les entités de caractères ?

Les entités de caractères sont réservées pour afficher divers caractères dans le navigateur. 

Par exemple, le symbole inférieur à (`<`) et le symbole supérieur à (`>`) sont réservés pour les balises en HTML. Si vous voulez les utiliser dans votre code, HTML pourrait les confondre avec des balises d'ouverture et de fermeture.

Si vous voulez les utiliser comme "supérieur à" et "inférieur à", vous devez utiliser leurs entités de caractères respectives (`&lt;` et `&gt;`). Ensuite, vous pouvez les afficher en toute sécurité dans le navigateur. 

## Comment ajouter des espaces insécables en HTML avec `&nbsp;`

Puisque le navigateur n'affichera qu'un seul espace vide même si vous en mettez des millions dans votre code, HTML dispose de l'entité de caractère `&nbsp;`. Elle permet d'afficher plusieurs espaces vides.

Sans l'entité de caractère `&nbsp;`, voici à quoi ressemblerait votre code :

```html
<div>
    <p>
      Les lémuriens sont des primates que l'on trouve exclusivement dans l'île isolée de
      Madagascar. Les lémuriens sont des primates tout comme les singes et les singes, mais ils
      ont évolué indépendamment et sont uniques. Le nombre de lémuriens
      diminue en raison du braconnage et d'autres activités humaines destructrices. Les lémuriens
      valent plus de 2 billions de dollars. En fait, aucune somme d'argent ne peut jamais
      en acheter un. Alors, protégez les lémuriens !
    </p>
</div>
```

J'ai ajouté un peu de CSS pour rendre le HTML plus clair et pour faciliter la visualisation de ce que j'essaie de montrer :

```css
body {
     display: flex;
     align-items: center;
     justify-content: center;
     height: 100vh;
     max-width: 800px;
     margin: 0 auto;
     font-size: 2rem;
}

span {
     background-color: #2ecc71;
}
```

![sans-nbsp](https://www.freecodecamp.org/news/content/images/2021/08/without-nbsp.png)

Dans le code HTML ci-dessous, j'ai inséré quelques entités de caractères `&nbsp;` pour créer plusieurs espaces vides :

```html
<div>
   <p>
     Les lémuriens &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; sont des primates que l'on trouve exclusivement
     dans l'île isolée de Madagascar. Les lémuriens sont des primates tout comme les singes
     et les singes, mais ils ont évolué indépendamment et sont uniques. Le nombre
     de lémuriens diminue en raison du braconnage et d'autres activités humaines
     destructrices. Les lémuriens valent plus de 2 billions de dollars. En fait, aucune somme
     d'argent ne peut jamais en acheter un. Alors, &nbsp; &nbsp; &nbsp; &nbsp; protégez
     les lémuriens !
   </p>
</div>
```
![un-espace-avec-nbsp](https://www.freecodecamp.org/news/content/images/2021/08/one-space-with-nbsp.png)

Vous pouvez voir qu'il y a 5 espaces vides entre les deux premiers mots, et 4 entre les mots antépénultièmes et pénultièmes. C'est parce que j'ai inséré 5 et 4 caractères `&nbsp;`, respectivement. 

Sans l'entité de caractère `&nbsp;`, cela ne serait pas possible.

## Que faire si vous voulez un tas d'espaces dans votre code ?

Que faire, par exemple, si vous voulez 10 espaces vides dans votre code ? Écrire `&nbsp;` 10 fois serait redondant et ennuyeux. 

Au lieu de cela, HTML fournit l'entité de caractère `&ensp;` pour 2 espaces insécables, et `&emsp;` pour 4 espaces insécables.

```html
<div>
   <p>
     Les lémuriens &emsp; &nbsp; sont des primates que l'on trouve exclusivement dans l'île isolée
     de Madagascar. Les lémuriens sont des primates tout comme les singes et les singes,
     mais ils ont évolué indépendamment et sont uniques. Le nombre de lémuriens
     diminue en raison du braconnage et d'autres activités humaines destructrices. Les lémuriens
     valent plus de 2 billions de dollars. En fait, aucune somme d'argent ne peut jamais
     en acheter un. Alors, &ensp; &ensp; protégez les lémuriens !
   </p>
</div>
```

Dans le code ci-dessus, j'ai inséré 5 espaces vides entre les deux premiers mots en utilisant `&emsp;` une fois (4 espaces) et `&nbsp;` une fois (1 espace). Ensuite, j'ai utilisé 2 entités `&ensp` entre les mots antépénultièmes et pénultièmes. Ainsi, le nombre d'espaces vides reste le même que dans le premier exemple :

![espaces-vides-multiples](https://www.freecodecamp.org/news/content/images/2021/08/mutiple-blanks-pace.png)

### Pourquoi auriez-vous besoin d'une espace insécable dans votre code ?

Parfois, HTML peut séparer des mots qui sont censés être ensemble en une autre ligne – par exemple, des initiales, des unités, des dates, des montants d'argent, et plus encore. 

L'entité de caractère `&nbsp;` empêche cela de se produire. Lorsque vous insérez le caractère `&nbsp;` entre de tels mots, il rendra un espace et ne permettra jamais à aucun des mots de se séparer en une nouvelle ligne.

Dans le code HTML ci-dessous, j'ai quelques informations sur les lémuriens – les beaux primates que l'on trouve à Madagascar :

```html
 <div>
    <p>
      Les lémuriens sont des primates que l'on trouve exclusivement dans l'île isolée de
      Madagascar. Les lémuriens sont des primates tout comme les singes et les singes, mais ils
      ont évolué indépendamment et sont uniques. Le nombre de lémuriens
      diminue en raison du braconnage et d'autres activités humaines destructrices. Les lémuriens
      valent plus de <span>2 billions de dollars.</span> En fait, aucune somme d'argent ne peut jamais
      en acheter un. Alors, protégez les lémuriens !
    </p>
</div>
```

J'ai un peu de CSS pour le rendre plus clair et montrer ce que j'essaie de montrer :

```css
body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    max-width: 800px;
    margin: 0 auto;
    font-size: 2rem;
}

span {
    background-color: #2ecc71;
}
```

Le résultat ressemble à ceci : 
![espace-de-rupture](https://www.freecodecamp.org/news/content/images/2021/08/breaking-space.png)

Vous pouvez voir que les 2 billions de dollars se séparent, ce qui ne semble pas bien car cela pourrait confondre le lecteur. 

L'entité de caractère `&nbsp;` force les deux mots à rester ensemble :

```html
<div>
    <p>
      Les lémuriens sont des primates que l'on trouve exclusivement dans l'île isolée de
      Madagascar. Les lémuriens sont des primates tout comme les singes et les singes, mais ils
      ont évolué indépendamment et sont uniques. Le nombre de lémuriens
      diminue en raison du braconnage et d'autres activités humaines destructrices. Les lémuriens
      valent plus de <span>2&nbsp;billions de dollars.</span> En fait, aucune somme d'argent ne peut
      jamais en acheter un. Alors, protégez les lémuriens !
    </p>
</div>
```

![espace-insécable](https://www.freecodecamp.org/news/content/images/2021/08/non-breaking-space.png)

N'est-ce pas génial ?

## Conclusion

Vous avez vu qu'avec les entités de caractères `&nbsp;`, `&ensp;` et `&emsp;`, vous pouvez afficher des espaces vides dans le navigateur. Cela n'est pas possible en utilisant simplement la touche de la barre d'espace. 

Vous pouvez également utiliser l'entité de caractère `&nbsp;` à des endroits spécifiques pour empêcher les mots qui doivent rester ensemble de se séparer à la ligne suivante.

Merci d'avoir lu, et continuez à coder.