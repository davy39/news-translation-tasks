---
title: Qu'est-ce que le Glassmorphism ? Créez cet effet de design nouveau en utilisant
  uniquement HTML et CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-29T18:21:22.000Z'
originalURL: https://freecodecamp.org/news/glassmorphism-design-effect-with-html-css
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/freecodecamp-glass.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
seo_title: Qu'est-ce que le Glassmorphism ? Créez cet effet de design nouveau en utilisant
  uniquement HTML et CSS
seo_desc: 'By Zoltán Szőgyényi

  Glassmorphism is a new design trend that is currently very popular. You''ll see
  it all over websites such as Dribbble, and even big companies like Apple and Microsoft
  are using it.

  Let me introduce you to this new design trend of g...'
---

Par Zoltán Szőgyényi

Le glassmorphism est une nouvelle tendance de design actuellement très populaire. Vous la verrez partout sur des sites comme Dribbble, et même de grandes entreprises comme Apple et Microsoft l'utilisent.

Permettez-moi de vous présenter cette nouvelle tendance de design qu'est le **glassmorphism**. Après la tendance du [design neumorphisme](https://demo.themesberg.com/neumorphism-ui/) de l'année dernière, qui était un style controversé et manquait d'accessibilité, cette tendance semble beaucoup plus prometteuse.

## Qu'est-ce que le glassmorphism ?

Essentiellement, l'aspect principal de cette tendance est un arrière-plan semi-transparent, avec une ombre sublime et une bordure. 

Mais vous avez également un flou ajouté à l'arrière-plan lui-même afin que tout ce qui se trouve derrière l'arrière-plan soit magnifiquement "morphé" dans l'élément lui-même. Est-ce que cela a du sens ? 

Voici un exemple :

[![Glassmorphism](https://www.freecodecamp.org/news/content/images/2021/03/glassmorphism-ui.png)](https://ui.glass/)

Il s'agit d'un exemple réel de glassmorphism en action, que vous pouvez également consulter sur le site [ui.glass](https://ui.glass/) (il s'agit d'une bibliothèque CSS UI à venir). 

L'effet de flou dont je parle est ce que vous pouvez voir derrière le code sur le côté droit de l'image ci-dessus. Voyez comme il se morphé magnifiquement dans l'arrière-plan, tout en restant lisible et agréable à l'œil ?

C'est l'effet que je veux vous montrer comment créer dans ce tutoriel. Nous verrons comment l'appliquer en utilisant uniquement HTML et CSS.

## Mise en route

Tout ce dont vous aurez besoin pour ce tutoriel est un navigateur et un éditeur de code, car nous n'allons utiliser que le bon vieux HTML et CSS. 

L'élément final que nous allons construire ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-24-at-17.35.18.png)
_Exemple de Glassmorphism_

Commençons par créer un fichier HTML de base avec le balisage suivant :

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Effet Glassmorphism</title>
</head>
<body>
    <!-- le code va ici -->
</body>
</html>
```

Je n'aime pas vraiment la famille de polices par défaut, alors utilisons quelque chose de plus joli de Google Fonts. J'aime vraiment la police Inter, alors incluons-la dans notre projet à l'intérieur de la balise `head` :

```html
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

Maintenant, ajoutons quelques styles de base à notre balise `body` et créons également un arrière-plan en utilisant des couleurs vives et des dégradés :

```css
body {
  padding: 4.5rem;
  margin: 0;
  background: #edc0bf;
  background: linear-gradient(90deg, #edc0bf 0,#c4caef 58%);
  font-family: 'Inter', sans-serif;
}
```

Super ! Maintenant que nous avons configuré certains des balisages et styles de base, créons un élément de carte à l'intérieur de la balise `body` :

```html
<div class="card">
    <h3 class="card-title">Le Glassmorphism est génial</h3>
    <p>Une bibliothèque CSS UI moderne basée sur les principes de design du glassmorphism qui vous aidera à concevoir et construire rapidement de beaux sites web et applications.</p>
    <a href="https://ui.glass">Lire la suite</a>
</div>
```

Le contenu à l'intérieur de la carte n'a pas vraiment d'importance – vous pouvez ajouter des boutons supplémentaires, des icônes et d'autres éléments. 

Avant d'appliquer l'effet **glassmorphism** à la carte, appliquons d'abord un espacement et des styles à la typographie en ajoutant le CSS suivant :

```css
.card {
  width: 400px;
  height: auto;
  padding: 2rem;
  border-radius: 1rem;
}

.card-title {
  margin-top: 0;
  margin-bottom: .5rem;
  font-size: 1.2rem;
}

p, a {
  font-size: 1rem;
}

a {
  color: #4d4ae8;
  text-decoration: none;
}
```

Bon travail jusqu'à présent ! Ensuite, je vais vous montrer comment appliquer l'effet spécial.

## Comment appliquer l'effet glassmorphism en utilisant CSS

Tout ce que vous avez à faire est d'appliquer une couleur d'arrière-plan semi-transparente et d'appliquer un flou en utilisant la propriété `backdrop-filter`. Ajoutez les styles suivants à l'élément `.card` en utilisant CSS :

```css
.card {
	/* autres styles */
	background: rgba(255, 255, 255, .7);
	-webkit-backdrop-filter: blur(10px);
	backdrop-filter: blur(10px);
}
```

Nous avons donc maintenant appliqué avec succès le style glassmorphism à la carte – mais où est l'effet ? 

Nous devons encore avoir quelque chose derrière la carte, comme une forme ou une image, afin de le voir en action.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-24-at-12.57.00.png)
_Exemple sans la forme_

Ajoutons une forme en utilisant un élément de balise `img` juste après l'ouverture de la balise `body` :

```html
<img class="shape" src="https://s3.us-east-2.amazonaws.com/ui.glass/shape.svg" alt="">
```

Et appliquons les styles CSS suivants à l'élément `.shape` pour le positionner correctement dans la page :

```css
.shape {
  position: absolute;
  width: 150px;
  top: .5rem;
  left: .5rem;
}
```

Vous devriez maintenant voir l'effet complet de la nouvelle tendance de design glassmorphism. Félicitations !

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-24-at-17.35.18.png)
_Exemple de Glassmorphism_

Vous pouvez consulter ce [codepen](https://codepen.io/themesberg/pen/RwKNMeY) pour obtenir le code et les styles directement à partir de ce guide.

## Support des navigateurs

L'un des principaux inconvénients du glassmorphism est que la propriété `backdrop-filter` n'est pas supportée par Internet Explorer 11, et elle est également désactivée par défaut par Firefox.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/glassmorphism-browser-support.png)
_Support des navigateurs pour backdrop-filter_

Cependant, selon le site [caniuse.com](https://caniuse.com/css-backdrop-filter), plus de 88,2 % des navigateurs dans le monde supporteront le style. Si Firefox décide d'activer cette propriété par défaut, et à mesure que l'utilisation des anciens navigateurs (comme IE 11) diminue, je crois que dans les années à venir, le glassmorphism pourra être utilisé à une échelle beaucoup plus grande.

En attendant, n'hésitez pas à l'utiliser pour vos projets personnels, ou amusez-vous simplement à créer des pages avec cette nouvelle tendance de design géniale.

## Conclusion

J'espère que ce tutoriel vous a aidé à en apprendre davantage sur cette nouvelle tendance de design. 

Si vous souhaitez l'explorer davantage, je voudrais vous présenter un projet sur lequel j'ai travaillé avec mon ami. 

Il s'appelle [Glassmorphism UI](https://ui.glass/), et ce sera une bibliothèque CSS UI gratuite et open source basée sur la nouvelle tendance de design. N'hésitez pas à vous inscrire avec votre email pour recevoir des mises à jour sur les progrès et être parmi les premiers à savoir quand elle sera lancée.

La bibliothèque sera disponible via NPM, mais elle sera également publiée sur GitHub sous la licence MIT.