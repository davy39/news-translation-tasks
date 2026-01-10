---
title: Une introduction au HTML pour les débutants
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-09-24T11:57:44.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-html
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/White-Playful-English-Class-Education-Presentation-43.png
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: Web Development
  slug: web-development
seo_title: Une introduction au HTML pour les débutants
seo_desc: "HTML, which stands for HyperText Markup Language, serves as the foundation\
  \ of web development. It enables you to create interactive web pages, structure\
  \ content, and effectively communicate your message. \nIn this guide, we'll explore\
  \ HTML comprehensi..."
---

HTML, qui signifie HyperText Markup Language, sert de fondation au développement web. Il vous permet de créer des pages web interactives, de structurer le contenu et de communiquer efficacement votre message. 

Dans ce guide, nous explorerons le HTML de manière exhaustive, en abordant des questions essentielles pour fournir une base solide aux développeurs web en herbe.

## Le rôle crucial du HTML dans le développement web

Le HTML joue un rôle essentiel dans le développement web, car il définit la structure et le contenu des pages web. Il sert de colonne vertébrale sur laquelle les sites web sont construits.

Le HTML y parvient en utilisant un système de balises et d'éléments, chacun servant un objectif unique.

```html
<!-- Exemple de balise HTML -->
<h1>Ceci est une balise HTML</h1>

```

## Comment écrire du code HTML ?

Écrire du code HTML consiste à comprendre les balises HTML. 

Les balises sont enfermées dans des chevrons, chacune comprenant une partie d'ouverture et de fermeture. Elles fonctionnent comme des blocs de construction qui définissent la structure de votre page web. 

Considérez-les comme les briques et le mortier du développement web. Comprendre leurs rôles est essentiel pour le développement web.

```html
<!-- Structure HTML de base -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Ma première page web</title>
</head>
<body>
    <h1>Bonjour, le monde !</h1>
    <p>Ceci est un paragraphe de texte.</p>
</body>
</html>

```

## Comment créer un site web en utilisant le HTML ?

Créer un site web en utilisant le HTML implique plusieurs étapes clés. Passons-les en revue dans les sections suivantes.

### Planification du site web

Avant de commencer à coder, prenez le temps de planifier soigneusement votre site web. 

Identifiez votre public cible, esquissez le contenu et la structure de votre site et concevez une mise en page qui correspond à vos objectifs. 

Gardez à l'esprit que la conception visuelle peut être améliorée avec CSS (Cascading Style Sheets), un sujet que nous explorerons plus tard dans votre parcours de développement web.

### Écriture du code HTML

Ouvrez un éditeur de texte, tel que Visual Studio Code ou Sublime Text, et commencez à écrire du code HTML. 

Commencez par la structure de base, y compris `<!DOCTYPE html>`, `<html> </html>`, `<head> </head>`, et `<body> </body>`. 

Ensuite, remplissez le corps avec votre contenu.

```html
<!-- Exemple de structure de document HTML -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Mon premier site web</title>
</head>
<body>
    <!-- Votre contenu va ici -->
</body>
</html>

```

### Enregistrement en tant que `.html`

Enregistrez vos fichiers HTML avec une extension `.html` pour indiquer qu'ils sont des pages web. Une bonne nomenclature des fichiers est essentielle pour organiser votre projet.

### Test local

Pour voir à quoi ressemble votre site web et comment il fonctionne, ouvrez vos fichiers HTML dans un navigateur web. Cette phase de test local vous permet d'affiner votre design et votre mise en page.

### Hébergement et publication

Pour que votre site web soit accessible sur Internet, vous aurez besoin de services d'hébergement web. Divers fournisseurs offrent de l'hébergement, et vous obtiendrez généralement un nom de domaine (par exemple, www.votresite.com) pour pointer vers votre site hébergé.

## Comment commencer le code HTML ?

Commencer le code HTML est simple. Passons en revue chaque étape dans les sections suivantes.

### Sélection de l'éditeur de texte

Choisissez un éditeur de texte qui répond à vos besoins. Les options populaires incluent Visual Studio Code, Sublime Text et Atom. Ces éditeurs offrent des fonctionnalités comme la coloration syntaxique et l'autocomplétion adaptées au développement web.

### Déclaration HTML5

Commencez votre document HTML avec `<!DOCTYPE html>`. Cette déclaration indique l'utilisation de HTML5, la dernière norme HTML.

```html
<!DOCTYPE html>

```

### Construction de la structure

À l'intérieur des balises `<html> </html>`, créez votre structure HTML. 

La section `<head> </head>` contient les métadonnées, y compris le titre de la page, et la section `<body> </body>` abrite le contenu visible de votre page web.

```html
<html>
<head>
    <meta charset="UTF-8">
    <title>Ma page web</title>
</head>
<body>
    <!-- Votre contenu va ici -->
</body>
</html>

```

### Ajout de métadonnées

Dans la section `<head> </head>`, utilisez la balise `<meta>` pour spécifier l'encodage des caractères, assurant un rendu correct.

```html
<meta charset="UTF-8">

```

## Comment exécuter du code HTML étape par étape ?

Exécuter du code HTML est simple, grâce aux navigateurs web modernes. Voici un guide étape par étape :

### Enregistrez votre fichier HTML

Assurez-vous que votre fichier HTML est enregistré avec une extension `.html`. Cela indique à votre ordinateur qu'il s'agit d'un document HTML.

### Double-cliquez pour ouvrir

Double-cliquez sur le fichier HTML, et votre navigateur web par défaut l'ouvrira automatiquement. Votre navigateur interprète le HTML, affichant votre page web.

### Navigateurs alternatifs

Si vous préférez un navigateur web spécifique, vous pouvez faire un clic droit sur le fichier HTML et choisir "Ouvrir avec" pour sélectionner votre navigateur préféré.

### Inspecter et déboguer

Les navigateurs web modernes sont équipés d'outils de développement intégrés qui vous permettent d'inspecter et de déboguer votre HTML, CSS et JavaScript. 

Accédez à ces outils en faisant un clic droit sur votre page web et en sélectionnant "Inspecter" ou en appuyant sur `F12` ou `Ctrl+Maj+I` (Windows) ou `Cmd+Option+I` (Mac).

## Comment écrire "Bonjour" en HTML ?

Afficher "Bonjour" sur une page web est simple. Vous pouvez utiliser la balise `<h1>` pour créer un titre de premier niveau, comme démontré précédemment. 

Le HTML offre plusieurs façons de présenter "Bonjour". Par exemple :

```html
<!-- Utilisation d'une balise <h1> -->
<h1>Bonjour !</h1>

```

Ou vous pouvez utiliser une balise de paragraphe :

```html
<!-- Utilisation d'une balise <p> -->
<p>Bonjour !</p>

```

Les deux options résultent en "Bonjour !" affiché sur votre page web. Le choix dépend du contexte et de vos préférences de style.

Il est intéressant de noter que le HTML dispose de six niveaux de titres, allant de `<h1>` (le plus élevé) à `<h6>` (le plus bas). Les titres sont utilisés pour structurer le contenu de manière hiérarchique, avec `<h1>` représentant le titre principal et `<h6>` représentant les sous-titres.

## Comment créer un fichier HTML avec un exemple ?

Créer un fichier HTML est votre porte d'entrée vers le développement web. Voici un guide étape par étape détaillé :

### Choisir un éditeur de texte

Sélectionnez un éditeur de texte qui correspond à votre flux de travail et à vos préférences. Les éditeurs modernes offrent des fonctionnalités comme la coloration syntaxique et l'autocomplétion, améliorant votre expérience de codage.

### Structurer votre HTML

Commencez votre document HTML avec `<!DOCTYPE html>`, suivi des balises `<html> </html>` pour enfermer votre contenu. Dans la section `<head> </head>`, définissez les métadonnées, telles que le titre de la page et l'encodage des caractères, en utilisant la balise `<meta>`.

```html
<!-- Exemple de structure HTML -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Mon premier site web</title>
</head>
<body>
    <!-- Votre contenu va ici -->
</body>
</html>

```

### Ajouter du contenu

Dans la section `<body> </body>`, insérez votre contenu. Expérimentez avec diverses balises HTML pour formater votre contenu, y compris les titres, les paragraphes, les listes, les liens et les images.

```html
<!-- Exemple de contenu -->
<h1>Bienvenue sur mon site web</h1>
<p>Ceci est un paragraphe d'exemple.</p>
<ul>
    <li>Élément 1</li>
    <li>Élément 2</li>
    <li>Élément 3</li>
</ul>

```

### Enregistrer avec l'extension `.html`

Enregistrez votre fichier avec une extension `.html`. Cette convention de nommage garantit que votre ordinateur le reconnaît comme un document HTML.

### Prévisualisation locale

Double-cliquez sur le fichier HTML pour l'ouvrir dans votre navigateur web. Cela fournit un aperçu instantané de votre page web, vous permettant de voir comment elle apparaît à votre audience.

### Introduction au CSS pour le style

Alors que le HTML définit la structure de votre page web, le CSS (Cascading Style Sheets) est utilisé pour le style. Vous pouvez lier un fichier CSS externe à votre HTML pour contrôler le design et la mise en page de votre page web. Par exemple :

```html
<!-- Lier un fichier CSS externe -->
<link rel="stylesheet" type="text/css" href="styles.css">

```

Cette séparation du contenu (HTML) et de la présentation (CSS) est une pratique fondamentale dans le développement web.

## Comment écrire une phrase en HTML ?

Pour créer une phrase en HTML, vous pouvez utiliser la balise `<p>` (paragraphe), comme mentionné précédemment. Cependant, le HTML offre de la flexibilité, vous permettant d'utiliser d'autres balises en ligne pour des extraits de texte plus courts. Voici un exemple :

```html
<!-- Utilisation d'une balise <p> -->
<p>Ceci est une phrase d'exemple en HTML.</p>

```

Alternativement, pour un texte plus court, vous pouvez utiliser la balise `<span>` :

```html
<!-- Utilisation d'une balise <span> -->
<span>Ceci est une phrase.</span>

```

La balise `<p>` est généralement utilisée pour les paragraphes, tandis que la balise `<span>` est plus polyvalente et est souvent utilisée pour les éléments en ligne dans une phrase ou un paragraphe. Choisissez la balise qui convient au contexte de votre contenu.

## Éléments HTML supplémentaires à explorer

Bien que nous ayons couvert les bases, le HTML offre une pléthore d'éléments et d'attributs pour créer des expériences web riches et interactives. Voici quelques éléments HTML supplémentaires que vous pouvez explorer :

### Formulaires

Le HTML fournit des éléments comme `<form>`, `<input>` et `<button>` pour créer des formulaires conviviaux pour collecter des données.

### Tableaux

Vous pouvez utiliser `<table>`, `<tr>`, `<td>` et d'autres balises connexes pour structurer des données tabulaires.

### Multimédia

Intégrez des images, de l'audio et de la vidéo en utilisant les balises `<img>`, `<audio>` et `<video>`.

### Liens et ancres

Créez des hyperliens en utilisant la balise `<a>` pour connecter des pages web et des ressources externes.

### Listes

Utilisez `<ul>` pour les listes non ordonnées, `<ol>` pour les listes ordonnées et `<li>` pour les éléments de liste.

### Balises sémantiques

Le HTML5 a introduit des éléments sémantiques comme `<header>`, `<nav>`, `<section>`, `<article>` et `<footer>` pour améliorer la structure et l'accessibilité des pages web.

### Balises méta

Affinez davantage votre document avec des balises méta, y compris celles pour spécifier l'encodage des caractères, les paramètres de la fenêtre d'affichage et les informations sur l'auteur.

## Conclusion

En conclusion, le HTML est votre porte d'entrée vers le développement web. Il fournit la fondation sur laquelle vous pouvez construire des expériences web époustouflantes et communiquer efficacement avec votre audience. 

Que vous vous lanciez dans la création d'un blog personnel, que vous lanciez un site de commerce électronique ou que vous présentiez votre portfolio, le HTML constitue la base de votre présence en ligne.

Alors que vous progressez dans le développement web, rappelez-vous que le HTML n'est que le début de votre voyage. Complétez vos compétences en HTML avec le CSS pour le style et le JavaScript pour l'interactivité. Cette approche vous permet de créer des sites web dynamiques et engageants qui captivent l'attention de votre audience.

Dans votre quête de l'excellence en développement web, embrassez les défis et les possibilités infinies présentées par le HTML et le domaine en constante évolution des technologies web. Restez curieux, ne cessez jamais d'apprendre et restez à jour avec les dernières normes et meilleures pratiques. Connectez-vous avec moi sur [Twitter](https://twitter.com/codesbyjojo).