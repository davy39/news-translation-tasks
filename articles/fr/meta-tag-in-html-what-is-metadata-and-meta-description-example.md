---
title: Balise Meta en HTML – Qu'est-ce que les métadonnées et exemple de méta description
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-01-04T18:52:11.000Z'
originalURL: https://freecodecamp.org/news/meta-tag-in-html-what-is-metadata-and-meta-description-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/nathan-da-silva-k-rKfqSm4L4-unsplash.jpg
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Balise Meta en HTML – Qu'est-ce que les métadonnées et exemple de méta
  description
seo_desc: 'In this article, you''ll learn what meta tags are in HTML and how to use
  them. Then we''ll go over some of the most important meta tags that you need to
  include in every new HTML project.

  Let''s get started!

  How to set up an HTML project

  When setting up...'
---

Dans cet article, vous apprendrez ce que sont les balises `meta` en HTML et comment les utiliser. Ensuite, nous passerons en revue certaines des balises `meta` les plus importantes que vous devez inclure dans chaque nouveau projet HTML.

Commençons !

## Comment installer un projet HTML

Lors de la configuration de nouveaux projets HTML, vous constaterez que vous devez inclure les mêmes balises à chaque fois.

Ces balises sont essentielles et vous en aurez besoin pour faire fonctionner correctement votre site HTML, en suivant les meilleures pratiques.

Certains éditeurs de code offrent des raccourcis pour remplir et entrer automatiquement les balises que vous utilisez dans chaque nouveau projet HTML. Cela peut vous faire gagner un temps considérable.

Dans l'[éditeur Visual Studio Code](https://code.visualstudio.com/download), vous pouvez faire cela de la manière suivante :

1) Assurez-vous d'avoir créé un fichier se terminant par `.html` - ici, vous écrirez tout votre code HTML.
2) À l'intérieur du fichier vide, tapez un point d'exclamation, `!`.

![Screenshot-2021-12-23-at-12.34.11-PM](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-23-at-12.34.11-PM.png)

3) Cliquez sur le point d'exclamation avec la mention que ce qui suit est une abréviation Emmet.

[Emmet](https://emmet.io/) est un plugin pour les éditeurs de code qui est intégré par défaut dans Visual Studio Code, et il vous aide à optimiser votre flux de travail HTML.

Vous verrez alors le code suivant rempli :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

Lors de la visualisation du fichier `.html` dans le navigateur de votre choix, vous verrez simplement une page vide.

Zoomons sur la section suivante du code qui a été créée :


```html
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
```

Que sont exactement ces balises `meta` ? Pourquoi sont-elles là et quel rôle jouent-elles lors de la création d'une page web ?

Cet article se concentrera sur l'explication des bases des balises `meta` et pourquoi elles sont utilisées dans les documents HTML.


## Que sont les balises `meta` en HTML ?

Les balises `meta` se trouvent dans la balise `head` du document HTML.

La balise `head` est utilisée pour configurer le fichier HTML.

Vous utilisez la balise `head` pour ajouter un titre à la page web, lier à une feuille de style CSS et définir plus d'informations sur le document HTML.

Les balises `meta` représentent des métadonnées. Elles sont essentiellement utilisées pour définir et décrire des données sur les données, et sont utilisées pour ajouter des informations supplémentaires aux données à l'intérieur de la page web.

Il existe de nombreuses balises `meta`. Certaines d'entre elles aident à améliorer le SEO (Search Engine Optimisation) de votre site web, en s'assurant que le contenu de votre site est pertinent par rapport à ce que les gens recherchent.

### Comment définir le jeu de caractères d'un site web

`<meta charset="UTF-8">` définit le jeu de caractères qui sera utilisé sur le site.

`UTF-8`, qui signifie 8-bit Unicode Transformation Format, est l'encodage de caractères standard utilisé avec la dernière version de HTML, qui est HTML5.

Cette ligne doit être incluse dans chaque page web créée, car elle garantit que chaque caractère de chaque langue du monde est affiché correctement dans chaque navigateur.

En utilisant le jeu de caractères universel `UTF-8`, les caractères des langues non latines ne seront pas déformés.

Le navigateur Google Chrome a automatiquement défini l'encodage sur `UTF-8`, donc vous n'aurez pas à vous en soucier lors de la conception pour ce navigateur. Mais vous devez toujours inclure `<meta charset="UTF-8">` dans chaque fichier HTML au cas où cette fonctionnalité ne serait pas supportée par d'autres navigateurs.

Par exemple, voyez ce qui se passe dans le navigateur Safari lorsque cette ligne n'est pas ajoutée et que j'écris un titre dans une langue non latine, comme le grec :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Γειά σου κόσμε!</h1> <!-- Hello world! -->
</body>
</html>
```

![Screenshot-2021-12-23-at-6.47.05-PM](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-23-at-6.47.05-PM.png)

Lorsque le document HTML est visualisé dans le navigateur, tous les caractères sont déformés.

### Comment indiquer à Microsoft's Internet Explorer quelle vue de rendu utiliser

Vous utilisez la balise meta `http-equiv="X-UA-Compatible" content="IE=edge"` pour choisir et définir la version d'Internet Explorer dans laquelle la page web sera rendue.

Choisissez toujours la dernière version, qui est `IE=edge`.

Il existe de nombreuses versions du navigateur de Microsoft. Dans le passé, les différentes avancées ont causé des maux de tête aux designers web et aux développeurs web, qui travaillaient à s'assurer que les sites web étaient utilisables sur les anciens navigateurs.

Cette balise garantira que le site web ne sera pas rendu comme une ancienne version d'Internet Explorer, qui tendent à être boguées.

### Comment ajuster les paramètres de la viewport

De nos jours, il est important que tous les sites aient une bonne apparence sur tous les appareils, en particulier sur les téléphones mobiles.

Vous devez donc inclure la balise `meta name="viewport" content="width=device-width, initial-scale=1.0"` dans chaque fichier HTML.

`viewport` fait référence à la manière dont le site est affiché sur différentes tailles d'écran, et à la quantité d'espace visuel dont un utilisateur dispose.

Chaque appareil a une viewport différente. Par exemple, les appareils mobiles en ont une plus petite et les ordinateurs de bureau en ont une plus grande.

`content="width=device-width` est la première étape pour s'assurer que les sites web ont une bonne apparence sur les appareils mobiles.

Cela empêche un site consulté depuis un appareil mobile d'avoir l'apparence qu'il aurait sur un ordinateur portable – c'est-à-dire petit et éloigné, zoomé.

Cela garantit que le HTML s'adaptera à la largeur de l'écran de l'appareil.

`initial-scale=1.0` définit la manière dont la page web est mise à l'échelle et définit le zoom initial lorsque la page est chargée pour la première fois par le navigateur.

## Balises `meta` supplémentaires à ajouter à votre projet HTML

### Comment ajouter une description de votre page web

L'utilisation d'une balise de description meta pour votre page aide les moteurs de recherche à comprendre et à classer votre site web par rapport à d'autres sites web. Elle est utilisée principalement à des fins de SEO (Search Engine Optimization).

La balise de description meta est utilisée pour expliquer de manière brève et concise de quoi traite votre site web.

Une balise de description meta pourrait ressembler à ceci :

```html
 <meta name="description" content="Notre mission : aider les gens à apprendre à coder gratuitement. Nous y parvenons en créant des milliers de vidéos, d'articles et de leçons de codage interactives - tout cela librement accessible au public.">
```

Vous utilisez les attributs `name` et `content`, avec la valeur de texte passée à `content` apparaissant dans les résultats de recherche :

![Screenshot-2021-12-26-at-3.23.14-PM](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-26-at-3.23.14-PM.jpeg)

#### Choses à considérer lors de la rédaction d'une description de votre site web

- Assurez-vous de garder la description de votre site web courte et de ne pas dépasser 160 caractères.
- Incluez des mots-clés et des phrases-clés utiles que les gens ont tendance à utiliser souvent lorsqu'ils recherchent les services que votre site web propose.
- Expliquez clairement ce que fait votre site web et la mission qui se cache derrière. Il est important de faire comprendre ce qui vous distingue et la valeur que vous apportez.
- Soyez cohérent avec la voix et le ton de votre marque.
- Plus important encore, tenez-vous-en à la description du contenu que votre site web fournit réellement. N'essayez pas de tromper vos lecteurs en visant uniquement à apparaître en haut des recherches et des classements.

### Comment ajouter le nom de l'auteur du site web

Un autre élément `meta` utile à inclure est le nom de l'auteur.

Cela pourrait ressembler à ce qui suit :

```html
<meta name="author" content="Quincy Larson">
```

Il peut être utile de savoir qui est l'auteur de la page.

Cette information partage qui a créé et construit le site web, qui a rédigé le contenu, ou à qui appartient le droit d'auteur.

## Conclusion

Pour résumer, tous les documents HTML doivent inclure au moins les trois balises `meta` suivantes :

- `<meta charset="UTF-8">`, pour spécifier le jeu de caractères.
- `<meta name="description">`, pour ajouter une description claire du site et des services que le site fournit aux lecteurs/clients.
- `<meta name="viewport">`, qui est la première étape que les sites doivent prendre pour être utilisables sur une variété d'appareils à écran.

Pour en savoir plus sur HTML et CSS, consultez la [Certification en Conception Web Réactive](https://www.freecodecamp.org/learn/2022/responsive-web-design/) de freeCodeCamp, où vous apprendrez de manière interactive tout en construisant des projets amusants en cours de route.

Merci d'avoir lu et bon codage !