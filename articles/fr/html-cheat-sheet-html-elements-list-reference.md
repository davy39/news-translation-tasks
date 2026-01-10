---
title: Feuille de triche HTML – Référence de la liste des éléments HTML
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-02-03T17:00:24.000Z'
originalURL: https://freecodecamp.org/news/html-cheat-sheet-html-elements-list-reference
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/html-cheat-sheet.png
tags:
- name: cheatsheet
  slug: cheatsheet
- name: HTML
  slug: html
- name: reference
  slug: reference
- name: Web Development
  slug: web-development
seo_title: Feuille de triche HTML – Référence de la liste des éléments HTML
seo_desc: 'In this tutorial, we will go over commonly used HTML tags, elements, and
  attributes. We''ll also see examples of how these tags, elements, and attributes
  work.

  You can use this article as a reference guide whether you''re a beginner or experienced
  deve...'
---

Dans ce tutoriel, nous passerons en revue les balises, éléments et attributs HTML couramment utilisés. Nous verrons également des exemples de fonctionnement de ces balises, éléments et attributs.

Vous pouvez utiliser cet article comme guide de référence, que vous soyez débutant ou développeur expérimenté.

## Qu'est-ce qui constitue un document HTML ?

Les balises suivantes définissent la structure de base d'un document HTML :

* Balise `<html>` – Cette balise sert de conteneur pour tous les autres éléments du document, à l'exception de la balise `<!DOCTYPE html>`.
* Balise `<head>` – Inclut toutes les métadonnées du document.
* Balise `<title>` – Définit le titre du document qui s'affiche dans la barre de titre du navigateur.
* Balise `<body>` – Sert de conteneur pour le contenu du document qui s'affiche dans le navigateur.

Voici à quoi cela ressemble :

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <title> Ma feuille de triche HTML </title>
  </head>
  <body></body>
</html>
```

`<!DOCTYPE html>` spécifie que nous travaillons avec un document HTML5.

Les balises suivantes fournissent des informations supplémentaires au document HTML :

* Balise `<meta>` – Cette balise peut être utilisée pour définir des informations supplémentaires sur la page web.
* Balise `<link>` – Utilisée pour lier le document à une ressource externe.
* Balise `<style>` – Utilisée pour définir les styles du document.
* Balise `<script>` – Utilisée pour écrire des extraits de code (généralement en JavaScript) ou pour lier le document à un script externe.

```html
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Ma feuille de triche HTML</title>

    <style>
      * {
        font-size: 100px;
      }
    </style>

    <script>
      alert('Ceci est une alerte');
    </script>
 </head>
```

## Structure d'un document HTML

Lorsque vous développez votre document HTML, vous utiliserez certaines balises pour créer la structure.

Les balises `<h1>` à `<h6>` montrent différents niveaux de titres dans un document, `<h1>` étant le plus grand et `<h6>` le plus petit.

```html
<h1> Titre 1 </h1>
<h2> Titre 2 </h2>
<h3> Titre 3 </h3>
<h4> Titre 4 </h4>
<h5> Titre 5 </h5>
<h6> Titre 6 </h6>
```

Vous utilisez la balise `<p>` pour créer un paragraphe.

```html
<p> Ceci est un paragraphe </p>
```

La balise `<div>` peut être utilisée pour diviser et styliser des sections séparées du document. Elle sert également de conteneur parent pour d'autres éléments. Voici comment cela fonctionne :

```html
<div class="sectionActualites">
  <h1> Ceci est la section des actualités </h1>
  <p> Bienvenue dans la section des actualités ! </p>
</div>

<div class="sectionContact">
  <h1> Ceci est la section contactez-nous </h1>
  <p> Bonjour le monde ! </p>
</div>
```

Nous avons également la balise `<span>`. Celle-ci est similaire à `<div>`, mais vous l'utilisez comme un conteneur en ligne.

```html
<p> J'adore <span class="motcle"> coder ! </span></p>
```

Il y a la balise `<br/>`, que nous utilisons pour créer des sauts de ligne. Celle-ci n'a pas de balise de fermeture.

```html
<p> J'adore <br/> freeCodeCamp </p>
```

La balise `<hr/>` est utilisée pour créer une ligne horizontale. Elle n'a pas non plus de balise de fermeture.

## Images en HTML

En HTML, nous utilisons la balise `<img/>` pour afficher des images.

Voici quelques attributs de la balise `<img/>` :

* `src` est utilisé pour spécifier le chemin vers l'emplacement de l'image sur votre ordinateur ou sur le web.
* `alt` définit un texte alternatif qui s'affiche si l'image ne peut pas être rendue. Le texte alternatif est également utile pour les lecteurs d'écran.
* `height` spécifie la hauteur de l'image.
* `width` spécifie la largeur de l'image.
* `border` spécifie l'épaisseur des bordures, qui est définie à 0 si aucune bordure n'est ajoutée.

```html
<img src="ihechikara.png" alt="une photo de Ihechikara" width="300" height="300">
```

## Mise en forme du texte en HTML

Nous avons de nombreuses façons de formater le texte en HTML. Passons-les rapidement en revue.

* `<i>` affiche le texte en italique.
* `<b>` affiche le texte en gras.
* `<strong>` affiche le texte en gras. Utilisé pour mettre l'accent sur l'importance.
* `<em>` une autre balise d'emphase qui affiche le texte en italique.
* `<sub>` définit le texte en indice, comme les deux atomes d'oxygène dans CO₂.
* `<sup>` définit un exposant comme la puissance d'un nombre, 10².
* `<small>` réduit la taille du texte.
* `<del>` définit le texte supprimé en barrant le texte.
* `<ins>` définit le texte inséré qui est généralement souligné.
* `<blockquote>` est utilisé pour enfermer une section de texte citée d'une autre source.
* `<q>` est utilisé pour des citations en ligne plus courtes.
* `<cite>` est utilisé pour citer l'auteur d'une citation.
* `<address>` est utilisé pour afficher les informations de contact de l'auteur.
* `<abbr>` désigne une abréviation.
* `<code>` affiche des extraits de code.
* `<mark>` met en surbrillance le texte.

```html
<p><i> texte en italique </i></p>
<p><b> texte en gras </b></p>
<p><strong> texte important </strong></p>
<p><em> texte important </em></p>
<p><sub> texte en indice </sub></p>
<p><sup> texte en exposant </sup></p>
<p><small> petit texte </small></p>
<p><del> texte supprimé </del></p>
<p><ins> texte inséré </ins></p>
<p><blockquote> texte cité </blockquote></p>
<p><q> texte cité court </q></p>
<p><cite> texte cité </cite></p>
<p><address> adresse </address></p>
<p><abbr> texte inséré </abbr></p>
<p><code> extrait de code </code></p>
<p><mark> texte marqué </mark></p>
```

## Liens

La balise `<a>`, également connue sous le nom de balise d'ancrage, est utilisée pour définir des hyperliens qui pointent vers d'autres pages (y compris des pages web externes) ou vers une section de la même page.

Voici quelques attributs de la balise `<a>` :

* `href` spécifie l'URL vers laquelle le lien emmène l'utilisateur lorsqu'il est cliqué.
* `download` spécifie que la cible ou la ressource cliquée est téléchargeable.
* `target` spécifie où le lien doit être ouvert. Cela peut être dans la même fenêtre ou dans une fenêtre séparée.

```html
<a href="https://www.freecodecamp.org/" target="_blank"> Apprendre à coder </a>
```

## Listes

La balise `<ol>` définit une liste ordonnée tandis que la balise `<ul>` définit une liste non ordonnée.

La balise `<li>` est utilisée pour créer des éléments dans la liste.

```html
<!-- Liste non ordonnée -->
<ul>
  <li> HTML </li>
  <li> CSS </li>
  <li> JavaScript </li>
</ul>

<!-- Liste ordonnée -->
<ol>
  <li> HTML </li>
  <li> CSS </li>
  <li> JavaScript </li>
</ol>
```

## Formulaires

La balise `<form>` est utilisée pour créer un formulaire en HTML. Les formulaires sont utilisés pour obtenir des entrées utilisateur. Voici quelques attributs associés à l'élément `<form>` :

* `action` spécifie où les informations du formulaire sont envoyées lors de la soumission.
* `target` spécifie où afficher la réponse du formulaire.
* `autocomplete` peut avoir une valeur de on ou off.
* `novalidate` spécifie que le formulaire ne doit pas être validé.
* `method` spécifie la méthode HTTP utilisée lors de l'envoi des données du formulaire.
* `name` spécifie le nom du formulaire.
* `required` spécifie qu'un élément d'entrée ne peut pas être laissé vide.
* `autofocus` donne le focus aux éléments d'entrée lorsque la page se charge.
* `disabled` désactive un élément d'entrée afin que l'utilisateur ne puisse plus interagir avec lui.
* `placeholder` est utilisé pour donner aux utilisateurs un indice sur les informations requises pour un élément d'entrée.

Voici d'autres éléments d'entrée associés aux formulaires :

* `<textarea>` pour obtenir une entrée de texte utilisateur avec plusieurs lignes.
* `<select>` spécifie une liste d'options parmi lesquelles l'utilisateur peut choisir.
* `<option>` crée une option sous l'élément select.
* `<input>` spécifie un champ d'entrée où l'utilisateur peut saisir des données. Celui-ci a un attribut `type` qui spécifie quel type de données l'utilisateur peut saisir.
* `<button>` crée un bouton.

```html
<form action="/info_url/" method="post">

    <label for="prenom"> Prénom : </label>
    <input type="text" 
           name="prenom" 
           placeholder="prénom" 
           required
    >
    
    <label for="nom"> Nom : </label>
    <input type="text" 
           name="nom" 
           placeholder="nom" 
           required
    >

    <label for="bio"> Bio : </label>
    <textarea name="bio"></textarea>

    <select id="age">
      <option value="15-18">15-18</option>
      <option value="19-25">19-25</option>
      <option value="26-30">26-30</option>
      <option value="31-36">31-36</option>
    </select>

    <input type="submit" value="Soumettre">
    
  </form>
```

## Tableaux

* La balise `<table>` définit un tableau HTML.
* `<thead>` spécifie les informations pour chaque colonne dans un tableau.
* `<tbody>` spécifie le corps ou le contenu du tableau.
* `<tfoot>` spécifie les informations de pied de page du tableau.
* `<tr>` désigne une ligne dans le tableau.
* `<td>` désigne une cellule unique dans le tableau.
* `<th>` désigne l'en-tête de la colonne de valeur.

```html
<table>
    
  <thead>
    <tr>
      <th> Cours </th>
      <th> Progression </th>
    </tr>
  </thead>
    
  <tbody>
    <tr>
      <td> HTML </td>
      <td> 90% </td>
    </tr>
    <tr>
      <td> CSS </td>
      <td> 80% </td>
    </tr>
  </tbody>
    
  <tfoot>
    <tr>
      <td> JavaScript </td>
      <td> 95% </td>
    </tr>
  </tfoot>
    
</table>
```

## Balises introduites dans HTML5

Voici quelques balises introduites dans HTML5 :

* `<header>` spécifie l'en-tête de la page web.
* `<footer>` spécifie le pied de page de la page web.
* `<main>` spécifie une section de contenu principal.
* `<article>` spécifie une section d'article, généralement pour du contenu qui peut se suffire à lui-même sur la page web.
* `<section>` est utilisé pour créer des sections séparées.
* `<aside>` est généralement utilisé pour placer des éléments dans une barre latérale.
* `<time>` est utilisé pour formater la date et l'heure.
* `<figure>` est utilisé pour des figures comme des graphiques.
* `<figcaption>` désigne une description d'une figure.
* `<nav>` est utilisé pour imbriquer des liens de navigation.
* `<meter>` est utilisé pour mesurer des données dans une plage.
* `<progress>` est utilisé comme une barre de progression.
* `<dialog>` est utilisé pour créer une boîte de dialogue.
* `<audio>` est utilisé pour intégrer un fichier audio dans la page web.
* `<video>` est utilisé pour intégrer une vidéo.

```html
  <header>
    <h1> Bienvenue </h1>
    <h3> Bonjour le monde ! </h3>
  </header>

  <nav>
    <ul>
        <li><a href="#">Accueil</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">À propos</a></li>
    </ul>
  </nav>

  <article>
      
    <h1> Un article sur nous </h1> 
    <p> Contenu de l'article </p>

    <aside>
      <p> Il fait beau aujourd'hui </p>
    </aside>
      
  </article>

  Progression : <progress min="0" max="100" value="50"> </progress>

  <footer> Copyright 2022-2099. Tous droits réservés. </footer>
```

## Conclusion

Dans cet article, nous avons vu de nombreuses balises, éléments et attributs HTML couramment utilisés par les développeurs. Ce n'est pas tout ce qui existe, mais cela devrait servir de bonne ressource de référence.

J'espère que vous avez trouvé cela utile. Merci d'avoir lu.