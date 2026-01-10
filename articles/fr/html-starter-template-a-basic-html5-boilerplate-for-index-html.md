---
title: Modèle de départ HTML – Une structure de base HTML5 pour index.html
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-25T23:18:46.000Z'
originalURL: https://freecodecamp.org/news/html-starter-template-a-basic-html5-boilerplate-for-index-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-pixabay-270404.jpg
tags:
- name: boilerplate
  slug: boilerplate
- name: HTML
  slug: html
- name: HTML5
  slug: html5
seo_title: Modèle de départ HTML – Une structure de base HTML5 pour index.html
seo_desc: "By Dillion Megida\nHTML has different tags, some of which have semantic\
  \ meanings. A basic boilerplate for an HTML file looks like this:\n<!DOCTYPE html>\n\
  <html lang=\"en\">\n  <head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\"\
  \ content=\"width=devic..."
---

Par Dillion Megida

L'HTML possède différentes balises, dont certaines ont des significations sémantiques. Une structure de base (Boilerplate) pour un fichier HTML ressemble à ceci :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>My Website</title>
    <link rel="stylesheet" href="./style.css">
    <link rel="icon" href="./favicon.ico" type="image/x-icon">
  </head>
  <body>
    <main>
        <h1>Welcome to My Website</h1>  
    </main>
	<script src="index.js"></script>
  </body>
</html>
```

Dans la suite de cet article, j'expliquerai ce que signifie chaque partie de ce Boilerplate.

# Syntaxe du Boilerplate HTML
## DOCTYPE

```html
<!DOCTYPE html>
```

Cet élément est la déclaration du doctype du fichier HTML. `<!DOCTYPE html>` indique au navigateur de rendre les codes HTML en tant qu'HTML5 (par opposition à une autre version d'HTML). 

C'est important car, sans cette déclaration, les éléments HTML5 comme `section`, `article`, etc., pourraient ne pas être rendus correctement.

## La balise html

```html
<html lang="en">
    ...
</html>
```

La balise `html` est la racine du document HTML. Elle contient la balise `head`, la balise `body` et tout autre élément HTML (à l'exception du DOCTYPE) utilisé dans votre site web.

Elle possède également l'attribut `lang`, que vous pouvez utiliser pour spécifier la langue du contenu textuel d'un site web. La valeur par défaut est "unknown", il est donc recommandé de toujours spécifier une langue. 

Définir une langue aide les lecteurs d'écran à lire les mots correctement et aide les moteurs de recherche à renvoyer des résultats de recherche spécifiques à la langue.

## La balise head

```html
<head>
    ...
</head>
```

La balise `head` contient les métadonnées de votre site web. Ce sont des données invisibles visuellement pour l'utilisateur, mais elles fournissent des informations sur le contenu de votre site. Les moteurs de recherche utilisent particulièrement ces données pour classer votre site.

Les métadonnées dans la balise head incluent les balises meta, les balises title, les balises link, les scripts, les feuilles de style, et plus encore.

## Les balises meta

```html
<meta ... />
```

La balise `meta` est un élément de métadonnées utilisé pour ajouter plus de métadonnées à votre site web que celles fournies par des balises non-meta comme title.

Vous pouvez utiliser ces balises à diverses fins :
- ajouter des métadonnées pour les plateformes de réseaux sociaux afin de créer des aperçus de liens
- ajouter une description pour votre site web
- ajouter un encodage de caractères pour votre site web
- et bien d'autres encore.

Les moteurs de recherche, les plateformes de réseaux sociaux et les services web utilisent ces métadonnées pour comprendre le contenu de votre site et déterminer comment le présenter aux utilisateurs.

## La balise title

```html
<title>My Website</title>
```

La balise `title` est utilisée pour spécifier un titre pour votre site web. Votre navigateur l'utilise pour afficher un titre dans la barre de titre :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-25-at-07.38.56.png)

Cette balise aide également les moteurs de recherche à afficher les titres de votre site web sur leurs résultats de recherche :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-25-at-07.44.11.png)

## La balise link
Vous utilisez la balise `link`, comme son nom l'indique, pour lier vers un autre document. Généralement, cela établit différents types de relations entre le document actuel et un document séparé.

```html
<link rel="stylesheet" href="./style.css">
```

Par exemple, comme on le voit dans le bloc de code ci-dessus, nous avons établi une relation de document "stylesheet" avec le fichier styles.css.

L'utilisation la plus courante de cette balise est d'ajouter des feuilles de style à un document et d'ajouter également des favicons à un site web :

```html
<link rel="icon" href="./favicon.ico" type="image/x-icon">
```

Un favicon est une petite image proche du titre de la page web, comme illustré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-25-at-07.38.56-1.png)

## La balise body

```html
<body>
    ...
</body>
```

La balise `body` contient le contenu principal d'un site web, qui est visible par les utilisateurs. Bien que des éléments non visibles comme `style` et `script` puissent également être ajoutés ici, la plupart des balises body sont généralement visibles.

Des titres aux paragraphes, en passant par les médias et bien plus encore, ces éléments sont ajoutés ici. Tout élément ne se trouvant pas ici (qui pourrait être inclus dans la balise head) ne sera pas affiché à l'écran.

## La balise main

```html
<main>
    ...
</main>
```

La balise `main` spécifie le contenu essentiel d'un site web. Il s'agirait du contenu lié au titre du site web.

Par exemple, sur une page d'article de blog, le partage sur les réseaux sociaux à gauche, les publicités à droite, l'en-tête et le pied de page sont des parties mineures de la page web. L'article lui-même affichant l'image de couverture, le titre et le contenu textuel est la partie centrale, qui se trouverait dans l'élément `main`.

## La balise h1
L'HTML possède différents éléments d'en-tête qui sont `h1`, `h2`, `h3`, `h4`, `h5` et `h6`. Les éléments d'en-tête sont utilisés pour décrire les différentes sections d'une page web. Et ces éléments ont un ordre, le `h1` étant le plus élevé.

Vous ne devriez avoir qu'un seul élément `h1` sur une page web car il commence la section principale. Ensuite, vous avez d'autres sections et sous-sections pour lesquelles vous pouvez utiliser les autres éléments d'en-tête.

Notez également que vous ne devriez pas sauter de niveaux de titre. Par exemple, vous ne devriez pas utiliser un élément `h4` après un élément `h2`. Une bonne structure pourrait ressembler à ceci :

```html
<h1>Welcome to my website</h1>

<h2>What do I have to offer</h2>

<h3>1. Financial Benefits</h3>

<h3>2. Society improves</h3>

<h4>a. Improving the tax system</h4>

<h4>b. Providing more refuse dumps</h4>

<h2>Who am I</h2>

<h2>Conclusion</h2>
```

À partir de ce code, vous pouvez voir comment les niveaux de titre spécifient leur position dans les sections et les sous-sections.

# Conclusion
Dans cet article, nous avons vu un Boilerplate de départ HTML et ce que signifie chaque balise utilisée dans ce modèle.

Cette liste d'éléments n'est pas exhaustive car de nombreux autres éléments peuvent être trouvés dans la balise head et la balise body, avec de nombreux attributs également.