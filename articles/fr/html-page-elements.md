---
title: Éléments de page HTML – Expliqué pour les débutants
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-06-13T21:01:13.000Z'
originalURL: https://freecodecamp.org/news/html-page-elements
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/pexels-joshua-135018.jpg
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Éléments de page HTML – Expliqué pour les débutants
seo_desc: "HTML, which stands for Hypertext Markup Language, is the standard markup\
  \ language used for creating web pages and structuring their content on the World\
  \ Wide Web. \nHTML serves as the backbone of web development and acts as a fundamental\
  \ building bloc..."
---

HTML, qui signifie **Hypertext Markup Language**, est le langage de balisage standard utilisé pour créer des pages web et structurer leur contenu sur le World Wide Web. 

HTML sert de colonne vertébrale au développement web et agit comme un bloc de construction fondamental pour créer des documents basés sur le web. Jetons un coup d'œil rapide à son fonctionnement.

## Que fait HTML ?

Le rôle principal de HTML est de définir la structure et la mise en page d'une page web en utilisant un ensemble de balises ou d'éléments. Ces balises représentent différents types de contenu tels que les titres, les paragraphes, les images, les liens, les formulaires et les tableaux. 

Les balises HTML sont enfermées dans des chevrons (<>) et sont composées d'une balise d'ouverture, de contenu et d'une balise de fermeture (qui est identifiée par sa barre oblique - "/").

Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). Si vous le souhaitez, vous pouvez suivre la version vidéo ici :

%[https://youtu.be/jWOVD6MtjyI]

En utilisant HTML, les développeurs web peuvent définir la structure sémantique d'une page web, en spécifiant des éléments comme les titres, les paragraphes, les listes et les sections. Voici un exemple typique d'une page HTML avec les sections `<head>`, `<body>`, `<header>`, et `<footer>` clairement identifiées :

```
<!DOCTYPE html>
<html>
<head>
	<title>Ma Démo</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<header>
	<h3>Ma Démo</h3>
</header>
<div class="container2">
	<!--Et un commentaire !
	-->
	Voici quelques points importants à considérer :<br>
	<ul>
	<li>Point Un
	<li>Point Deux
	<li>Point Trois
	</ul>
<footer>
  <p>&copy; 2023 Ma Démo. Tous droits réservés.</p>
  <nav>
    <ul>
      <li><a href="/about">À propos</a></li>
      <li><a href="/contact">Contact</a></li>
      <li><a href="/privacy">Politique de confidentialité</a></li>
    </ul>
  </nav>
</footer>
</div>
</body>
</html>
```

De plus, HTML permet l'inclusion de contenu multimédia comme des images et des vidéos. Il permet également d'intégrer d'autres technologies web telles que CSS (Cascading Style Sheets) pour le style, et JavaScript pour l'interactivité.

Voici un exemple de code montrant une image et une vidéo incorporées dans une page web.

```
<img src="test_image.png" width="800" alt="Une image de test">
<hr>

<div class="video-container">
  <video controls>
    <source src="sample_video.mkv" type="video/mp4">
    Votre navigateur ne supporte pas la balise vidéo.
  </video>
</div>
```

Les documents HTML sont interprétés par les navigateurs web, qui rendent le contenu structuré et le présentent aux utilisateurs. Il permet aux navigateurs de comprendre la hiérarchie, les relations et la présentation des éléments sur une page web. Il garantit que tout s'affiche comme prévu et qu'il y a une interactivité appropriée.

Dans ce guide, nous allons explorer les éléments principaux de HTML, y compris la structure du document, les liens externes, les médias intégrés et les formulaires simples. Et nous allons faire tout cela en créant réellement des choses. Plus de diapositives ennuyeuses.

## Comprendre la structure d'une page HTML

D'accord. La structure de base d'un document HTML, parfois décrite comme le squelette HTML, fournit une base pour la création de pages web. Elle se compose de plusieurs éléments essentiels qui établissent la structure et définissent le contenu de la page. 

Lorsque je fais un clic droit sur une page, je peux sélectionner l'option Afficher la source de la page et je me retrouverai à regarder le code source HTML.

Nous commencerons par le haut. La déclaration du type de document (<!DOCTYPE>) est placée au tout début d'un document HTML pour spécifier la version HTML utilisée. Elle garantit que le navigateur interprète correctement la page.

La balise HTML est l'élément racine d'un document HTML. Elle enferme tout le contenu de la page et sert de conteneur pour tous les autres éléments HTML. 

Si vous faites défiler jusqu'en bas d'une page, vous verrez une balise de _fermeture_ comme celle-ci : `</html>`.

### Que contient la section <head> de votre code HTML ?

La balise head contient des métadonnées et d'autres informations non visibles sur la page web. Elle peut inclure des éléments tels que le titre de la page, l'encodage des caractères, les feuilles de style liées et les fichiers JavaScript. Le contenu de la balise head n'est pas directement visible pour les utilisateurs qui chargent la page.

La balise _charset_ dans ce cas utilise **UTF-8**. De quoi s'agit-il ? L'encodage des caractères HTML fait référence à la méthode utilisée pour représenter et afficher les caractères, les symboles et les caractères spéciaux dans un document HTML. 

Voici à quoi tout cela pourrait ressembler :

```
<!DOCTYPE html>
<html>
<head>
	<title>Ma Démo</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
```

Puisque HTML est un langage de balisage basé sur du texte, il a besoin d'une manière standardisée de représenter les caractères au-delà de l'ensemble alphanumérique de base des majuscules A-Z, des minuscules a-z et des chiffres 0-9. 

Lorsque vous utilisez l'encodage UTF-8, les caractères [en dehors de la plage ASCII](https://www.freecodecamp.org/news/get-the-ascii-value-of-any-character-with-one-line-of-code/) sont représentés en utilisant plusieurs octets. Par exemple, un caractère latin de base comme "A" est représenté par un seul octet (0x41), tandis que certains caractères non latins peuvent nécessiter deux octets ou plus.

La section `<head>` peut également contenir des informations de style qui auraient tout aussi bien pu être placées dans un fichier CSS accompagnant. Voici à quoi cela pourrait ressembler :

```
<style>
  .video-container {
    width: 500px; /* Définir la largeur souhaitée */
  }
</style>
```

La balise body représente le contenu _visible_ de la page web. Elle contient tous les éléments qui seront affichés à l'écran, tels que le texte, les images, les titres, les paragraphes et les liens. Le contenu de la balise body est ce que les utilisateurs voient lorsqu'ils visitent la page.

Les balises de titre, comme h1, h2, et ainsi de suite, sont utilisées pour définir les titres ou les titres des sections dans le corps de la page. La balise h1 représente le titre principal, suivie de h2 pour les sous-titres, h3 pour les sous-sous-titres, et ainsi de suite.

Les balises de paragraphe, `<p>`, définissent des blocs de texte ou de contenu dans le corps de la page. Elles créent des paragraphes séparés et sont couramment utilisées pour structurer le contenu textuel.

```
<p>Voici un nouveau texte :</p>
```

## Comprendre les balises sémantiques

Enfin, **HTML5** a introduit un ensemble de balises sémantiques qui fournissent une structure plus significative et descriptive au contenu. Ces balises incluent header, nav, section, article, aside, et footer. 

Même s'ils n'ont pas toujours d'impact direct sur la façon dont une page s'affichera dans votre navigateur, les balises sémantiques aident à l'organisation et facilitent la compréhension de la finalité des différentes sections de la page.

Une balise qui commence par un point d'exclamation est en fait utilisée pour les commentaires qui ne seront pas visibles par vos utilisateurs et qui n'ont aucun impact sur la façon dont les navigateurs lisent la page. Voici un exemple :

```
<!-- Voici un commentaire qui est juste pour les yeux des développeurs. -->
```

Le but des balises de commentaire est de nous aider à nous souvenir de la finalité et de la fonction des diverses sections de code. Il s'agit de documenter votre code.

En fait, la "lisibilité" est une caractéristique importante de _tout_ code HTML bien écrit. Chacun des éléments que nous avons vus ici – qu'ils contrôlent les métadonnées, les styles, les scripts, la navigation ou le texte brut – peut, lorsqu'il est présenté intelligemment, contribuer à la valeur à la fois de la page vue par vos utilisateurs et du code lui-même.

_Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257)._ _Et il y a beaucoup plus de bonnes choses technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)_