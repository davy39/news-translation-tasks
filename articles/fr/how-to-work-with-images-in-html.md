---
title: Comment travailler avec des images en HTML – Un guide pour débutants
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-10-09T15:33:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-images-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Beige-and-Blue-Minimal-Modern-Thesis-Defense-Presentation.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Comment travailler avec des images en HTML – Un guide pour débutants
seo_desc: "Images are an essential part of web development, adding visual appeal and\
  \ context to your web pages. \nIn HTML, you can easily incorporate images to enhance\
  \ the user experience. This article will guide you through the basics of working\
  \ with images in ..."
---

Les images sont un élément essentiel du développement web, ajoutant un attrait visuel et un contexte à vos pages web. 

En HTML, vous pouvez facilement incorporer des images pour améliorer l'expérience utilisateur. Cet article vous guidera à travers les bases du travail avec des images en HTML et vous aidera à mieux comprendre les images en HTML.

## Comment insérer une image dans une page web

Pour afficher une image sur votre page web, vous utiliserez l'élément `<img>`. C'est une balise auto-fermante, ce qui signifie que vous n'avez pas besoin d'une balise de fermeture `</img>`. Au lieu de cela, vous placez la source de l'image et d'autres attributs dans la balise d'ouverture. 

Voici la syntaxe de base :

```html
<img src="image.jpg" alt="Description de l'image">

```

* L'attribut `src` spécifie l'emplacement du fichier image.
* L'attribut `alt` fournit un texte alternatif pour les lecteurs d'écran et est affiché si l'image ne parvient pas à se charger.

### Exemple :

```html
<img src="cat.jpg" alt="Un chat mignon">

```

Résultat :

<img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg">

## Types de fichiers image

HTML prend en charge divers formats de fichiers image, notamment JPEG, PNG, GIF, et plus encore. Le choix du format dépend de vos besoins. 

Voici des explications de certains formats d'image couramment utilisés en HTML :

### JPEG (Joint Photographic Experts Group) :

* **Meilleur pour :** Les photographies, les images avec des dégradés et les scènes complexes.
* **Avantages :** Haute compression, petites tailles de fichier et bonne qualité d'image pour les photographies.
* **Considérations :** Compression avec perte, non adapté aux images avec transparence.

### PNG (Portable Network Graphics) :

* **Meilleur pour :** Les images avec transparence, les icônes, les logos et les graphiques avec des bords nets.
* **Avantages :** Prend en charge la compression sans perte et avec perte, excellente qualité d'image et transparence.
* **Considérations :** Taille de fichier plus grande pour les images complexes par rapport au JPEG.

### GIF (Graphics Interchange Format) :

* **Meilleur pour :** Les animations simples, les images avec une palette de couleurs limitée et les icônes.
* **Avantages :** Prend en charge les animations, la transparence et les petites tailles de fichier pour les graphiques simples.
* **Considérations :** Support de couleur limité (256 couleurs), non adapté aux photographies ou aux images complexes.

### SVG (Scalable Vector Graphics) :

* **Meilleur pour :** Les graphiques vectoriels, les logos, les icônes et les images qui doivent être redimensionnées sans perte de qualité.
* **Avantages :** Indépendant de la résolution, petites tailles de fichier et rendu net à toute taille.
* **Considérations :** Non adapté aux images photographiques complexes.

### WebP :

* **Meilleur pour :** Les navigateurs web modernes et la livraison efficace d'images.
* **Avantages :** Fournit une compression avec et sans perte, des tailles de fichier plus petites et une bonne qualité d'image.
* **Considérations :** Support limité dans les anciens navigateurs.

### BMP (Bitmap Image) :

* **Meilleur pour :** Rarement utilisé sur le web en raison des grandes tailles de fichier et du manque de compression.
* **Avantages :** Aucune perte de qualité, adapté à certaines applications spécialisées.
* **Considérations :** Grandes tailles de fichier et non recommandé pour une utilisation web générale.

Lors du choix d'un format d'image pour votre page web, tenez compte de facteurs tels que le type de contenu, la complexité de l'image, la transparence requise et le support des navigateurs de votre public cible. 

Il est courant d'utiliser une combinaison de formats au sein d'un site web pour optimiser la livraison des images. L'utilisation de techniques et d'outils de compression d'image appropriés peut également aider à réduire les tailles de fichier tout en maintenant la qualité de l'image, ce qui est crucial pour les performances web.

## Taille et mise à l'échelle des images

Vous pouvez contrôler la taille de vos images en utilisant les attributs `width` et `height`. Ces attributs vous permettent de spécifier les dimensions d'une image sur votre page web.

```html
<img src="cat.jpg" alt="Un chat mignon" width="300" height="200">

```

Résultat :

<img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg" alt="Photo d'un chat" width="300" height="200">


Il est important de définir des dimensions appropriées pour maintenir les ratios d'aspect et assurer un design réactif.

## Alignement des images

L'alignement d'une image dans le texte en utilisant l'attribut `align` était une approche autrefois utilisée dans les anciennes versions de HTML. Mais l'attribut `align` est obsolète dans le HTML moderne (HTML5). 

Au lieu de cela, l'alignement est généralement réalisé via CSS. Voici une explication détaillée des deux approches :

### Comment utiliser l'attribut obsolète `align` (non recommandé) :

Dans les anciennes versions de HTML, vous pouviez utiliser l'attribut `align` avec l'élément `<img>` pour contrôler l'alignement d'une image dans le texte. L'attribut `align` avait des valeurs comme "left", "right", "top", "middle", et "bottom". Voici un exemple :

```html
<img src="cat.jpg" alt="Un chat mignon" align="left">
<p>Ceci est un texte qui entoure l'image.</p>

```

Résultat :

<img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg" alt="Une image" align="left">
<p>Ceci est un texte qui entoure l'image.</p>


Bien que cette méthode ait fonctionné par le passé, elle est considérée comme obsolète et n'est pas recommandée pour le développement web moderne. Il est préférable de séparer le contenu de la présentation en utilisant CSS pour l'alignement.

### Comment utiliser CSS pour l'alignement des images (recommandé) :

Dans le développement web moderne, CSS (Cascading Style Sheets) est la méthode préférée pour contrôler l'alignement des images dans le texte. Vous pouvez appliquer des règles CSS directement dans votre fichier HTML en utilisant des styles en ligne ou, de préférence, utiliser un fichier CSS externe pour une meilleure maintenabilité.

Voici un exemple de la façon dont vous pouvez utiliser CSS pour aligner une image à gauche dans un paragraphe :

```html
<style>
  .image-align-left {
    float: left;
    margin-right: 10px; /* Ajoute un espace entre l'image et le texte */
  }
</style>

<p><img src="cat.jpg" alt="Un chat mignon" class="image-align-left">Ceci est un texte qui entoure l'image.</p>

```

<style>
  .image-align-left {
    float: left;
    margin-right: 10px; /* Ajoute un espace entre l'image et le texte */
  }
</style>

<p><img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg" alt="Une image" class="image-align-left">Ceci est un texte qui entoure l'image.</p>


Dans cet exemple, nous définissons une classe CSS appelée `image-align-left` qui utilise la propriété `float` pour faire flotter l'image à gauche du texte. La propriété `margin-right` ajoute un espace entre l'image et le texte pour améliorer la lisibilité.

L'utilisation de CSS pour l'alignement offre plus de flexibilité et de contrôle sur le positionnement des images dans le texte, et c'est l'approche recommandée pour le design web moderne. Cela sépare également le style du contenu, rendant votre HTML plus propre et plus maintenable.

## Liens d'images

Vous pouvez rendre les images cliquables en les enveloppant dans un élément `<a>` (ancre). Vous pouvez personnaliser davantage le comportement de l'hyperlien en utilisant des attributs HTML supplémentaires, tels que `target="_blank"` pour ouvrir la page liée dans un nouvel onglet ou une nouvelle fenêtre du navigateur. 

```html
<a href="link-to-page.html" target="_blank">
  <img src="cat.jpg" alt="Image de chat cliquable">
</a>

```

Résultat :

<a href="link-to-page.html" target="_blank">
  <img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg" alt="Image de chat cliquable">
</a>


Maintenant, lorsque l'utilisateur clique sur l'image, il sera redirigé vers le lien spécifié. 

## Images réactives

Les sites web modernes doivent être réactifs, s'adaptant à diverses tailles d'écran. Pour rendre vos images réactives, utilisez la propriété de style `max-width` :

```html
<img src="image.jpg" alt="Description" style="max-width: 100%;">

```

Cette propriété garantit que les images seront automatiquement redimensionnées proportionnellement pour s'adapter à la largeur de leurs conteneurs parents lorsque la taille de l'écran ou la largeur de la fenêtre d'affichage diminue. 

Cela est particulièrement important pour s'assurer que les images ne débordent pas ou ne cassent pas la mise en page sur les petits écrans, comme ceux des appareils mobiles.

## Comment charger des images à partir de sources externes

Vous pouvez également afficher des images hébergées sur des sites web externes en spécifiant l'URL complète dans l'attribut `src` :

```html
<img src="https://example.com/image.jpg" alt="Image externe">

```

Assurez-vous simplement d'avoir la permission d'utiliser des images externes et qu'elles sont publiquement accessibles.

## Accessibilité des images

L'accessibilité web est cruciale. Incluez toujours un texte descriptif dans l'attribut `alt` pour aider les utilisateurs handicapés. Un texte alternatif significatif aide les lecteurs d'écran à fournir un contexte pour l'image. 

Le texte alternatif, ou "alt text", est une description textuelle d'une image qui peut être lue à voix haute par les lecteurs d'écran ou affichée à la place de l'image si elle ne peut pas être chargée.

### Objectif du texte alternatif :

* **Lecteurs d'écran :** Les personnes malvoyantes utilisent souvent des lecteurs d'écran pour naviguer sur les sites web. Lorsqu'un lecteur d'écran rencontre une image, il lit le texte alternatif à voix haute pour fournir un contexte et transmettre le sens de l'image.
* **Problèmes de chargement d'image :** Le texte alternatif est également affiché lorsqu'une image ne parvient pas à se charger correctement dans un navigateur web, permettant aux utilisateurs de comprendre le contenu de l'image même s'ils ne peuvent pas la voir.

### Comment créer un texte alternatif significatif :

* Le texte alternatif doit être concis mais descriptif, transmettant les informations essentielles ou le but de l'image.
* Il doit être exempt de détails inutiles ou de descriptions de conception visuelle (par exemple, "Un bouton bleu" n'est pas aussi utile que "Soumettre le formulaire").
* Évitez d'utiliser des phrases comme "image de" ou "photo de" puisque les lecteurs d'écran annoncent déjà qu'il s'agit d'une image.
* Pour les images décoratives ou purement esthétiques qui ne transmettent pas d'informations, utilisez un attribut alt vide (alt="") ou indiquez qu'il s'agit d'une image décorative (alt="Image décorative").

### Exemples de texte alternatif :

**Exemple 1 (Image informative) :**

<img src="" alt="Un chien guide aidant une personne à traverser un passage piéton.">

**Exemple 2 (Image décorative) :**

<img src="" alt="Bordure décorative">

**Exemple 3 (Image complexe avec description) :**

<img src="" alt="Diagramme du système solaire montrant les positions et les orbites des planètes, avec le soleil au centre.">

N'oubliez pas que l'objectif du texte alternatif est de fournir une description significative et informative de l'image afin que les utilisateurs handicapés puissent comprendre son contenu et son contexte. 

En suivant ces directives et en créant un texte alternatif approprié, vous contribuez à une expérience web plus accessible et inclusive pour tous les utilisateurs.

## Conseils supplémentaires pour l'utilisation des images

### 1. Optimisation des images

[L'optimisation des images](https://www.freecodecamp.org/news/image-optimization/) est cruciale pour les performances web. Compressez les images, utilisez des dimensions appropriées et sélectionnez le bon format de fichier pour équilibrer la qualité de l'image et la vitesse de chargement.

### 2. Chargement paresseux

Vous pouvez améliorer les performances du site web en implémentant le chargement paresseux. L'attribut "loading" défini sur "lazy" est une fonctionnalité en HTML qui indique au navigateur de charger l'image de manière paresseuse. Cela signifie qu'il ne chargera l'image que lorsqu'elle est dans ou près de la fenêtre d'affichage (zone visible) de la page web. 

Le chargement paresseux peut aider à améliorer les performances de chargement de la page en réduisant le temps de chargement initial pour les images qui ne sont pas immédiatement visibles pour l'utilisateur. 

Voici le code pour faire cela :

```html
<img src="cat.jpg" alt="Un chat mignon" loading="lazy">

```

<img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg" alt="Description" loading="lazy">


### 3. Légendes des images

En plus du texte alternatif pour l'accessibilité, envisagez d'utiliser des légendes d'image pour un meilleur contexte. Vous pouvez inclure un élément `<figcaption>` dans un élément `<figure>` :

```html
<figure>
  <img src="cat.jpg" alt="Un chat mignon">
  <figcaption>Ceci est la photo d'un chat avec des yeux mignons</figcaption>
</figure>

```

Résultat :

<figure>
  <img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg" alt="Description">
  <figcaption>Ceci est une photo d'un chat avec des yeux mignons</figcaption>
</figure>


### 4. Écrans Retina et haute résolution

Pour les écrans haute résolution comme les écrans Retina, servez des images de résolution plus élevée en utilisant l'attribut `srcset` :

```html
<img src="cat.jpg" alt="Un chat mignon" srcset="image.jpg 1x, image@2x.jpg 2x">

```

<img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg" alt="Description" srcset="image.jpg 1x, image@2x.jpg 2x">


## Conclusion

Incorporer des images dans des documents HTML est une compétence fondamentale pour les développeurs web. Avec l'élément `<img>` et ses attributs, vous pouvez facilement contrôler l'affichage, la taille et l'alignement des images. 

En suivant les meilleures pratiques pour l'optimisation des images, l'accessibilité et le design réactif, vous créerez un contenu web visuellement attrayant et convivial.

Alors que vous continuez votre parcours en développement web, pratiquez l'intégration d'images dans vos projets et explorez ces conseils supplémentaires pour améliorer les performances et l'accessibilité de vos sites web.