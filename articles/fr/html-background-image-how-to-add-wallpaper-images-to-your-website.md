---
title: Image d'arrière-plan HTML – Comment ajouter des images de fond à votre site
  web
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-09-23T19:18:19.000Z'
originalURL: https://freecodecamp.org/news/html-background-image-how-to-add-wallpaper-images-to-your-website
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/jonatan-pie-3l3RwQdHRHg-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: image
  slug: image
seo_title: Image d'arrière-plan HTML – Comment ajouter des images de fond à votre
  site web
seo_desc: "Background images can help beautify websites and make them more attractive\
  \ to users. \nIn this article, you'll learn: \n\nHow to add a background image to\
  \ your website using the CSS background-image property. \nOther CSS background properties\
  \ for images...."
---

Les images d'arrière-plan peuvent aider à embellir les sites web et à les rendre plus attrayants pour les utilisateurs.

Dans cet article, vous apprendrez :

* Comment ajouter une image d'arrière-plan à votre site web en utilisant la propriété CSS `background-image`.
* D'autres propriétés CSS d'arrière-plan pour les images.

## Comment ajouter des images de fond à votre site web

Lors du codage d'un site web, l'utilisation d'une image comme image d'arrière-plan du site est différente de l'insertion d'une image en HTML à l'aide de l'élément `img`.

Pour utiliser une image comme arrière-plan de votre site web, vous utiliserez le CSS.

Voici un exemple :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <link rel="stylesheet" href="style.css">
    <title>Image d'arrière-plan</title>
</head>

<body>
    <h1>Image d'arrière-plan</h1>
</body>
</html>
```

```css
h1{
    text-align: center;
}
```

Nous avons deux blocs de code ci-dessus — le code HTML affiche le texte « Image d'arrière-plan » sur la page web tandis que le code CSS centre le texte sur la page.

Pour ajouter une image de fond au site web — une image qui couvre toute la page — vous devez écrire quelques règles CSS pour l'élément `body`. Voici comment :

```css
body{
    background-image: url('bg-image.jpg');
}
```

Dans le code ci-dessus, nous utilisons la propriété `background-image` pour ajouter une image au corps de la page web. Le chemin/l'emplacement de l'image est passé en paramètre à la fonction `url()` : `url('bg-image.jpg')`.

Voici à quoi ressemble la page web maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/full-bg-image.PNG)

## Que faire si l'image d'arrière-plan est plus petite que la fenêtre du navigateur ?

Dans les situations où l'image est plus petite que le navigateur, l'image est répétée plusieurs fois pour combler les espaces restants.

Cette répétition ne rend pas bien pour toutes les images. Voici à quoi ressemble une version plus petite de l'image utilisée dans la section précédente dans le navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/repeat.PNG)

L'image a été divisée en quatre parties inégales. À moins que ce ne soit l'effet recherché, vous pouvez y remédier en utilisant la propriété `background-repeat`.

Voici comment résoudre le problème de répétition d'image :

```css
body{
    background-image: url('bg-image-small.jpg');
    background-repeat: no-repeat;
}

```

Dans le code ci-dessus, nous avons attribué la valeur `no-repeat` à la propriété `background-repeat`.

Voici à quoi ressemble la page web maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/small-image.PNG)

L'image n'est plus répétée sur la page, mais nous avons un nouveau problème — l'image ne couvre plus toute la page.

Pour corriger cela, nous utilisons les propriétés `background-size` et `background-attachment` :

```css
body{
    background-image: url('bg-image-small.jpg');
    background-repeat: no-repeat;
    background-size: cover;
    background-attachment: fixed;
}
```

Définir la valeur de la propriété `background-size` sur `cover` permet à l'image de couvrir l'ensemble de l'élément (le `body`/toute la page dans notre cas).

Avec la valeur `fixed` de la propriété `background-attachment`, la position de l'image est fixe. De cette façon, elle reste à la même position même lorsque vous faites défiler la page.

Voici l'image maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/cover-image.PNG)

L'inconvénient d'étirer une petite image pour couvrir toute la page est que l'image perd en qualité et devient floue à mesure qu'elle est étirée. Dans ce cas, vous devriez y réfléchir avant d'utiliser une petite image comme image d'arrière-plan pour votre site web.

## Résumé

Dans cet article, nous avons parlé de l'ajout d'images de fond à un site web.

Vous pouvez ajouter une image d'arrière-plan à votre site web en utilisant la propriété CSS `background-image`.

Nous avons également appris à utiliser d'autres propriétés CSS d'arrière-plan comme `background-repeat`, `background-size` et `background-attachment`.

Bon codage !