---
title: 'Modèle HTML5 de base : utilisez ce code boilerplate comme point de départ
  pour tout projet de développement web'
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-07-30T22:41:08.000Z'
originalURL: https://freecodecamp.org/news/basic-html5-template-boilerplate-code-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/jackson-so-_t-l5FFH8VA-unsplash.jpg
tags:
- name: boilerplate
  slug: boilerplate
- name: HTML
  slug: html
- name: HTML5
  slug: html5
seo_title: 'Modèle HTML5 de base : utilisez ce code boilerplate comme point de départ
  pour tout projet de développement web'
seo_desc: "When you are building a new website, it is important to have a good starting\
  \ foundation. In this article, I will explain what an HTML 5 boilerplate is and\
  \ how to create a basic template to use in your projects. \nWhat is an HTML 5 boilerplate?\n\
  Accordi..."
---

Lorsque vous construisez un nouveau site web, il est important d'avoir une bonne fondation de départ. Dans cet article, je vais expliquer ce qu'est un boilerplate HTML 5 et comment créer un modèle de base à utiliser dans vos projets. 

## Qu'est-ce qu'un boilerplate HTML 5 ?

Selon [Wikipedia](https://en.wikipedia.org/wiki/Boilerplate_code#HTML),

> **boilerplate code** ou simplement **boilerplate** sont des sections de code qui sont répétées à plusieurs endroits avec peu ou pas de variation.

Un boilerplate en HTML est un modèle que vous ajouterez au début de votre projet. Vous devriez ajouter ce boilerplate à toutes vos pages HTML. 

## Exemple de boilerplate HTML 5

Examinons un exemple de base.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 5 Boilerplate</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
	<script src="index.js"></script>
  </body>
</html>
```

### Qu'est-ce qu'un doctype en HTML ?

La première ligne de votre code HTML doit être la déclaration du doctype. Un doctype indique au navigateur quelle version de HTML la page utilise. 

```html
<!DOCTYPE html>
```

Si vous oubliez d'inclure cette ligne de code dans votre fichier, certaines des balises HTML 5 comme `<article>`, `<footer>` et `<header>` peuvent ne pas être supportées par le navigateur.

### Qu'est-ce que l'élément racine HTML ?

La balise `<html>` est l'élément de niveau supérieur du fichier HTML. Vous y imbriquerez les balises `<head>` et `<body>`.

```html
<!DOCTYPE html>
<html lang="en">
  <head></head>
  <body></body>
</html>
```

L'attribut `lang` à l'intérieur de la balise `<html>` définit la langue de la page. Il est également bon de l'inclure pour des raisons d'accessibilité, car les lecteurs d'écran sauront comment prononcer correctement le texte. 

### Que sont les balises head en HTML ?

Les balises `<head>` contiennent des informations qui sont traitées par les machines. À l'intérieur des balises `<head>`, vous imbriquerez des métadonnées qui décrivent le document à la machine. 

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 5 Boilerplate</title>
    <link rel="stylesheet" href="style.css">
</head>
```

### Qu'est-ce que l'encodage de caractères UTF-8 ?

UTF-8 est l'encodage de caractères standard que vous devriez utiliser dans vos pages web. Cela sera généralement la première balise `<meta>` affichée dans l'élément `<head>`.

```html
 <meta charset="UTF-8">
```

Selon le [World Wide Web Consortium](https://www.w3.org/International/questions/qa-choosing-encodings),

> Un encodage basé sur Unicode tel que UTF-8 peut supporter de nombreuses langues et peut accommoder des pages et des formulaires dans n'importe quel mélange de ces langues. Son utilisation élimine également le besoin de logique côté serveur pour déterminer individuellement l'encodage des caractères pour chaque page servie ou chaque soumission de formulaire entrant.

### Qu'est-ce que la balise meta viewport en HTML ?

Cette balise rend la largeur de la page égale à la largeur de l'écran de l'appareil. Si vous avez un appareil mobile qui fait 600px de large, alors la fenêtre du navigateur fera également 600px de large.

L'initial-scale contrôle le niveau de zoom. La valeur de 1 pour l'initial-scale empêche le zoom par défaut des navigateurs. 

```html
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

```

### Que signifie X-UA-Compatible ?

Cette balise `<meta>` spécifie le mode de document pour Internet Explorer. `IE=edge` est le mode le plus élevé supporté. 

```html
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

```

### Que sont les balises title en HTML ?

La balise `<title>` est le titre de la page web. Ce texte est affiché dans la barre de titre du navigateur.

```html
    <title>HTML 5 Boilerplate</title>

```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-30-at-4.15.25-AM.png)

### Feuille de style CSS

Ce code liera votre CSS personnalisé à la page HTML. `rel="stylesheet"` définit la relation entre le fichier HTML et la feuille de style externe. 

```html
    <link rel="stylesheet" href="style.css">

```

### Balises script en HTML

Les balises de script externes seront placées juste avant la balise de fermeture du body. C'est ici que vous pouvez lier votre code JavaScript externe. 

```html
	<script src="index.js"></script>

```

## Conclusion

Vous devriez ajouter un boilerplate HTML 5 à chacune de vos pages HTML. Ce code de départ contient des informations importantes comme le doctype, les métadonnées, les feuilles de style externes et les balises de script.