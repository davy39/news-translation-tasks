---
title: HTML pour débutants – Les bases de HTML avec des exemples de code
subtitle: ''
author: Casmir Onyekani
co_authors: []
series: null
date: '2024-05-07T19:45:50.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-html-basics
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/cover-img.jpg
tags:
- name: HTML
  slug: html
seo_title: HTML pour débutants – Les bases de HTML avec des exemples de code
seo_desc: 'Welcome to the exciting world of web development! In this beginner''s guide,
  you will learn the fundamentals of HTML, the backbone of every web page.

  Imagine a tree: its roots anchor and nourish the entire plant. Similarly, HTML,
  the root of web devel...'
---

Bienvenue dans le monde passionnant du développement web ! Dans ce guide pour débutants, vous apprendrez les bases de HTML, l'épine dorsale de chaque page web.

Imaginez un arbre : ses racines ancrent et nourrissent toute la plante. De même, HTML, la racine du développement web, fournit la base de chaque page web.

Comprendre le rôle de HTML, c'est comme saisir les racines d'un arbre, cela forme la base fondamentale pour comprendre comment les pages web prennent vie.

À la fin de ce tutoriel, vous serez équipé des connaissances nécessaires pour démarrer votre voyage dans le codage.

## Table des matières

* [Qu'est-ce que HTML ?](#heading-quest-ce-que-html)
    
* [Structure de base d'un document HTML](#heading-structure-de-base-dun-document-html)
    
* [Commentaires](#heading-commentaires)
    
* [Balises et éléments](#heading-balises-et-elements)
    
* [Attributs HTML](#heading-attributs-html)
    
* [Multimédia HTML](#heading-multimedia-html)
    
* [Bonnes pratiques](#heading-bonnes-pratiques)
    

## Qu'est-ce que HTML ?

HTML, qui signifie Hypertext Markup Language, est le langage standard utilisé pour créer et concevoir la structure d'une page web. Il vous permet d'organiser le contenu de votre site web, de définir sa structure et d'établir les relations entre différents éléments.

## Structure de base d'un document HTML

Un document HTML suit une structure spécifique qui sert de base à votre page web :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link />
</head>
<body>
  <!-- le contenu de votre page web va ici -->
</body>
</html>
```

Décortiquons cela :

`<!DOCTYPE html>` : définit le type et la version du document HTML utilisé (HTML5 dans ce cas).

`<html lang="fr">` et `</html>` : balises d'ouverture et de fermeture de l'élément racine qui enveloppe tout le contenu HTML. L'attribut `lang="fr"` définit la langue (dans ce cas, le français).

`<head>` et `</head>` : balises d'ouverture et de fermeture de l'élément `head` contiennent des méta-informations `<meta >` sur le document HTML, le titre de la page `<title></title>` que vous voyez dans l'onglet du navigateur, et le lien `<link />` qui définit un lien entre votre document HTML et des ressources externes, comme une feuille de style, une favicon, une importation, etc.

`<body>` et `</body>` : balises d'ouverture et de fermeture `body` enferment tout le contenu visible d'une page web, y compris le texte, les images, les liens, les formulaires et d'autres éléments avec lesquels les utilisateurs interagissent.

**Note** : Tous les éléments HTML ont des balises d'ouverture (`**< >**`) et de fermeture (`**</ >**`), sauf pour les balises auto-fermantes (`**< >**` ou `**< />**`), que je vais expliquer plus en détail plus tard.

## Commentaires

Remarquez ceci `<!-- le contenu de votre page web va ici -->` dans la structure de base html ci-dessus, c'est ce qu'on appelle des commentaires. Les commentaires sont utilisés pour ajouter des notes explicatives qui ne sont pas affichées lorsque la page web est consultée dans un navigateur. Ils sont utiles pour documenter votre code, fournir des informations à d'autres développeurs, ou exclure temporairement des parties spécifiques du code. Vous pouvez créer un commentaire en utilisant cette balise `<!--` `votre commentaire va ici` `-->`.

Il en existe :

1. **Commentaire sur une seule ligne** : `<!-- Ceci est un commentaire sur une seule ligne -->`
    
2. **Commentaire sur plusieurs lignes** : `<!-- Ceci est un commentaire sur plusieurs lignes. Il peut s'étendre sur plusieurs lignes. Tout le contenu dans le bloc de commentaire sera ignoré par le navigateur. -->`
    

## Balises et éléments

HTML utilise des balises pour définir différents éléments sur une page web. Les balises sont enfermées dans des chevrons (`< >`). Il existe des balises d'ouverture (`< >`) et de fermeture (`</ >`), et des balises auto-fermantes (`< >` ou `< />`). Voici quelques exemples :

### Titres

```html
<h1>Ceci est un Titre 1</h1>
<h2>Ceci est un Titre 2</h2>
<!-- ... jusqu'à <h6> -->
```

Les balises de titre `<h1>` à `<h6>` sont utilisées pour définir des titres ou des sous-titres dans un document. Ces balises représentent une hiérarchie de titres, avec `<h1>` étant le niveau le plus élevé (titre principal) et `<h6>` étant le niveau le plus bas (niveau de sous-titre le plus bas).

Leur but est de structurer et d'organiser le contenu d'une page web, la rendant plus lisible et accessible.

### Paragraphe

La balise de paragraphe (`<p> votre texte va ici </p>`) est utilisée pour séparer des blocs de texte en paragraphes distincts. C'est un élément de niveau bloc qui représente une unité de texte ou un bloc de contenu, et il est couramment utilisé pour structurer et séparer le texte sur une page web.

La balise `<p>` fait partie du balisage structurel en HTML et aide à créer un contenu bien organisé et lisible.

### Sauts de ligne

Pour créer un saut de ligne sans commencer un nouveau paragraphe, utilisez la balise de saut (`<br>`).

Exemple 1 - Saut de ligne de base :

```html
<p>Ceci est la première ligne.<br>Ceci est la deuxième ligne.</p>
```

Cela se rendra comme :

Ceci est la première ligne.  
Ceci est la deuxième ligne.

Exemple 2 - Sauts de ligne dans le texte :

```html
<p>Ce texte contient un<br>saut de ligne.</p>
```

Cela se rendra comme :

Ce texte contient un  
saut de ligne.

Exemple 3 - Sauts de ligne dans une liste :

```html
<ul>
  <li>Élément 1</li>
  <li>Élément 2<br>avec un saut de ligne</li>
  <li>Élément 3</li>
</ul>
```

Cela se rendra comme :

* Élément 1
    
* Élément 2  
    avec un saut de ligne
    
* Élément 3
    

Exemple 4 - Sauts de ligne dans une adresse :

```html
<address>
  Nuel Cas<br>
  23 Musa Yar'Dua VI<br>
  Lagos, Nigeria
</address>
```

Cela se rendra comme :

Nuel Cas  
23 Musa Yar'Dua VI  
Lagos, Nigeria

Exemple 5 : Sauts de ligne avec plusieurs balises

```python
<p>Ceci est un paragraphe avec<br><br>plusieurs sauts de ligne.</p>
```

Cela se rendra comme :

Ceci est un paragraphe avec

plusieurs sauts de ligne.

Bien que la balise de saut (`<br>`) soit couramment utilisée pour des sauts de ligne simples, CSS et les éléments de niveau bloc comme les balises `<p>` et `<div>` sont souvent préférés pour des mises en page plus complexes.

L'utilisation excessive de balises `<br>` à des fins de mise en page est déconseillée. CSS est généralement plus adapté pour contrôler l'espacement et la mise en page des éléments sur une page web.

### Div

Une balise `<div>`, qui signifie "division", est l'un des éléments conteneurs les plus couramment utilisés en HTML. C'est un conteneur de niveau bloc qui est utilisé pour regrouper d'autres éléments HTML et appliquer des styles ou des scripts à ces éléments collectivement.

Voici un exemple :

```html
<div>
  <p>Ceci est un paragraphe à l'intérieur d'une div.</p>
  <ul>
    <li>Élément de liste 1</li>
    <li>Élément de liste 2</li>
  </ul>
</div>
```

Dans cet exemple, l'élément `<div>` enveloppe un paragraphe (`<p>`) et une liste non ordonnée (`<ul>`). Ce regroupement vous permet d'appliquer des styles ou de manipuler ces éléments ensemble en utilisant CSS ou JavaScript.

**Note** : La balise `<div>` est souvent utilisée à des fins de mise en page, aidant à structurer le contenu d'une page web. Pour des significations plus sémantiques et spécifiques, HTML5 a introduit de nouvelles balises sémantiques comme `<section>`, `<article>`, `<header>`, `<footer>`, etc., qui fournissent une meilleure clarté sur le but du contenu.

### Balises sémantiques

Elles sont comme des étiquettes spéciales qui indiquent aux navigateurs web et aux développeurs de quoi parlent les différentes parties d'une page web. Elles aident à rendre les sites web plus faciles à comprendre pour les personnes et les ordinateurs.

En utilisant ces balises, vous pouvez rendre vos sites web plus accessibles et plus faciles à trouver sur les moteurs de recherche. Voici quelques balises sémantiques HTML courantes avec des exemples :

1. `<header>` : La balise header représente le contenu introductif au début d'une section ou d'une page web. Elle contient généralement des logos, des menus de navigation et d'autres éléments introductifs.
    

Exemple :

```html
  <header>
  <h1>Titre du site web</h1>
  <nav>
    <ul>
      <li><a href="#">Accueil</a></li>
      <li><a href="#">À propos</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>
</header>
```

2. `<nav>` : Utilisez la balise nav pour définir les liens de navigation dans votre page web. Elle contient des liens vers d'autres pages ou sections du site web.
    

Exemple :

```html
<nav>
  <ul>
    <li><a href="#">Accueil</a></li>
    <li><a href="#">À propos</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

3. `<main>` : Utilisé pour définir le contenu principal d'une page web. Il aide à améliorer l'accessibilité et la structure de votre code HTML, car il identifie clairement la zone de contenu principal pour les lecteurs d'écran et autres technologies d'assistance. Il aide également les moteurs de recherche à comprendre la pertinence du contenu de votre page, ce qui peut améliorer l'optimisation pour les moteurs de recherche (SEO) de votre site web.
    

Exemple :

```html
<main>
  <article>
    <h2>Titre de la page</h2>
    <p>Le contenu de la page va ici...</p>
  </article>
</main>
```

4. `<section>` : Utilisez la balise `section` lorsque vous souhaitez définir des sections dans une page web. Également pour regrouper du contenu lié.
    

Exemple :

```html
<section>
  <h2>Titre de la section</h2>
  <p>Le contenu de la section va ici...</p>
</section>
```

5. `<article>` : Utilisez la balise `article` lorsque vous souhaitez définir un morceau de contenu indépendant qui peut se suffire à lui-même, comme un article de blog, un article de presse ou un message de forum.
    

Exemple :

```html
<article>
  <h2>Titre de l'article</h2>
  <p>Le contenu de l'article va ici...</p>
</article>
```

6. `<aside>` : Utilisez la balise `aside` lorsque vous souhaitez définir un contenu qui est lié au contenu principal mais qui n'en fait pas partie, comme des barres latérales, des publicités ou des liens connexes.
    

Exemple :

```html
<aside>
  <h3>Liens connexes</h3>
  <ul>
    <li><a href="#">Lien 1</a></li>
    <li><a href="#">Lien 2</a></li>
    <li><a href="#">Lien 3</a></li>
  </ul>
</aside>
```

7. `<footer>` : Utilisé pour définir le pied de page d'une page web, contenant généralement des informations de copyright, des détails de contact ou des liens vers des pages connexes.
    

Exemple :

```html
<footer>
  <p>&copy; Site web de Nuel Cas</p>
</footer>
```

### Balise de liste

Les listes `<li>` vous permettent d'organiser et de structurer le contenu de manière hiérarchique. Il existe deux types : les listes ordonnées `<ol>` (numérotées) et les listes non ordonnées (`<ul>`) (à puces).

Liste ordonnée : Utilisez `<ol>` pour les listes ordonnées, et `<li>` pour les éléments de liste.

Exemple :

```html
<ol>
  <li>Premier élément</li>
  <li>Deuxième élément</li>
  <li>Troisième élément</li>
</ol>
```

Cela se rendra comme :

1. Premier élément
    
2. Deuxième élément
    
3. Troisième élément
    

Liste non ordonnée : La balise `<ul>` est utilisée pour créer une liste non ordonnée, où l'ordre des éléments n'a pas d'importance, elle affiche des éléments à puces. Chaque élément de la liste est représenté par la balise `<li>` (élément de liste).

Exemple :

```html
<ul>
  <li>Élément 1</li>
  <li>Élément 2</li>
  <li>Élément 3</li>
</ul>
```

Cela se rendra comme :

* Élément 1
    
* Élément 2
    
* Élément 3
    

Les listes peuvent être imbriquées les unes dans les autres. Par exemple, vous pouvez avoir une liste ordonnée dans une liste non ordonnée ou vice versa.

Exemple :

```html
<ul>
  <li>Élément de liste non ordonnée 1</li>
  <li>Élément de liste non ordonnée 2
    <ol>
      <li>Élément de liste ordonnée 1</li>
      <li>Élément de liste ordonnée 2</li>
    </ol>
  </li>
  <li>Élément de liste non ordonnée 3</li>
</ul>
```

Cela se rendra comme :

* Élément de liste non ordonnée 1
    
* Élément de liste non ordonnée 2
    

1. Élément de liste ordonnée 1
    
2. Élément de liste ordonnée 2
    

* Élément de liste non ordonnée 3
    

Les éléments de liste peuvent également avoir des attributs. Par exemple, vous pourriez utiliser l'attribut `type` avec la balise `<ol>` pour changer le style de numérotation.

Exemple :

```html
<ol type="A">
  <li>Élément 1</li>
  <li>Élément 2</li>
  <li>Élément 3</li>
</ol>
```

Cela se rendra comme :

A. Élément 1  
B. Élément 2  
C. Élément 3

Les balises `<ul>`, `<ol>`, et `<li>` en HTML sont essentielles pour créer des listes organisées et structurer le contenu sur les pages web. Elles offrent de la flexibilité pour présenter des informations dans des formats ordonnés et non ordonnés.

### Balise Span

La balise `<span>` est un conteneur générique en ligne (elle ne crée pas de saut de ligne) utilisé pour regrouper et appliquer des styles aux éléments en ligne ou au texte. Elle est généralement utilisée lorsque vous souhaitez appliquer des styles ou utiliser JavaScript pour manipuler des portions spécifiques de texte au sein d'un bloc de contenu plus large sans affecter la structure globale.

Voici un exemple de la façon dont la balise `<span>` peut être utilisée en HTML :

```html
<p>Ceci est un <span style="color: red; font-weight: bold;">texte mis en évidence</span>.</p>
```

Dans cet exemple, le mot "mis en évidence" sera affiché en rouge et en gras, comme spécifié par les styles en ligne appliqués à l'élément `<span>`.

### Liens

La balise `<link>` est utilisée pour définir un lien entre un document et une ressource externe. Son but principal est d'inclure des ressources externes, telles que des feuilles de style, des icônes et d'autres documents. Examinons les cas d'utilisation courants de la balise `<link>` :

**Lien vers une feuille de style** : L'utilisation la plus courante de la balise `<link>` est de lier un fichier CSS (Cascading Style Sheets) externe à un document HTML. Cela vous permet de séparer le style de votre site web de sa structure, ce qui facilite la maintenance et la mise à jour.

Exemple :

```html
<link rel="stylesheet" type="text/css" href="styles.css">
```

Dans cet exemple, l'attribut `rel` spécifie la relation entre le document HTML et la ressource liée (feuille de style), l'attribut `type` indique le type de la ressource liée (`text/css` pour les feuilles de style), et l'attribut `href` spécifie le chemin vers le fichier CSS externe.

**Note** : Le lien vers un fichier CSS doit être fait à l'intérieur de l'élément `<head>`.

**Lien vers une icône** : La balise `<link>` est également couramment utilisée pour lier l'icône favicon d'une page web, qui est la petite icône qui apparaît dans l'onglet du navigateur ou à côté de l'URL dans la barre d'adresse.

```html
<link rel="icon" href="favicon.ico" type="image/x-icon">
```

Dans ce cas, l'attribut `rel` est défini sur "icon" pour indiquer qu'il s'agit d'un fichier d'icône, et l'attribut `href` spécifie le chemin vers le fichier d'icône. L'attribut `type` indique le type du fichier lié, dans ce cas, `image/x-icon` pour les icônes.

**Lien vers des documents externes** : La balise `<link>` peut être utilisée pour lier d'autres documents externes, tels que :

1. Feuille de style pour l'impression : Imaginez que vous avez un design spécial pour lorsque quelqu'un veut imprimer votre page web. La balise `<link>` peut connecter votre page web à une feuille de style séparée conçue uniquement pour l'impression. Ainsi, lorsque quelqu'un imprime votre page, elle a l'air propre et soignée.
    

Exemple :

```html
<!-- Lien vers la feuille de style pour l'impression -->
  <link rel="stylesheet" type="text/css" href="print-styles.css" media="print">
```

2. Versions alternatives d'un document (comme des traductions) : Parfois, vous pourriez avoir différentes versions de votre page web pour différentes langues ou objectifs. La balise `<link>` peut connecter votre page web à ces versions alternatives.
    

Exemple :

```html
<link rel="alternate" hreflang="es" href="spanish-version.html">
```

3. Flux pour la syndication de contenu : Supposons que vous avez un blog et que vous voulez que d'autres voient facilement vos derniers articles. La balise `<link>` peut aider en connectant votre page web à un flux, qui est comme un flux de votre dernier contenu.
    

Exemple :

```html
<link rel="alternate" type="application/rss+xml" title="Flux RSS" href="rss-feed.xml">
```

La balise `<link>` est comme un connecteur qui aide votre page web à interagir avec d'autres fichiers sur Internet.

### Balise d'ancrage

La balise d'ancrage, représentée par `<a>`, est utilisée pour créer des hyperliens ou des points d'ancrage dans une page web. Elle est principalement utilisée pour définir un hyperlien, permettant aux utilisateurs de naviguer vers une autre page web, une section différente de la même page, ou même une ressource externe.

La balise d'ancrage utilise l'attribut `href` pour spécifier l'URL de destination (Uniform Resource Locator).

Exemple :

```html
<a href="https://www.example.com">Visitez Example.com</a>
```

### Balise de formulaire

Les formulaires HTML sont essentiels pour l'interaction des utilisateurs sur les sites web. Ils permettent aux utilisateurs de saisir des données qui peuvent être envoyées à un serveur pour traitement. La structure de base d'un formulaire HTML implique plusieurs éléments clés :

```html
<form>
  <!-- Vos éléments de formulaire vont ici -->
</form>
```

La balise `<form>` marque le début et la fin de votre formulaire. Elle agit comme un conteneur pour divers éléments de formulaire. Elle abrite couramment des balises de libellé, des types d'entrée, des zones de texte et des boutons.

#### Libellé

La balise `<label>` est utilisée pour définir un libellé pour un élément d'entrée. Exemple :

```html
<label for="username">Nom d'utilisateur :</label>
```

#### Type d'entrée

Dans un formulaire, différents types d'entrée servent à diverses fins. La balise d'entrée (`<input>`) définit un élément interactif pour que les utilisateurs saisissent des données. Les plus couramment utilisés sont :

Entrée de texte :

```html
<input type="text" name="username" placeholder="Entrez votre nom d'utilisateur">
```

Entrée de mot de passe :

```html
<input type="password" name="password" placeholder="Entrez votre mot de passe">
```

Boutons radio :

```html
<input type="radio" name="gender" value="male"> Homme
<input type="radio" name="gender" value="female"> Femme
```

Cases à cocher :

```html
<input type="checkbox" name="subscribe" value="yes"> S'abonner à la newsletter
```

#### Zone de texte

La balise `<textarea>` définit un contrôle de saisie de texte multiligne, couramment utilisé dans les éléments de formulaire. Exemple :

```python
<textarea name="message" placeholder="Entrez votre message"></textarea>
```

#### Bouton (pour soumettre des formulaires)

La partie la plus cruciale d'un formulaire est de permettre aux utilisateurs de soumettre leurs entrées. Pour cela, vous pouvez utiliser une balise de bouton (`<button>`) pour soumettre :

Exemple :

```python
<button type="submit">Soumettre</button>
```

La balise `<button>` crée un bouton cliquable. L'attribut `type="submit"` indique que le clic sur ce bouton soumettra le formulaire.

### Conseils rapides

* Incluez toujours un attribut `name` dans vos éléments de formulaire. Il aide à identifier et à traiter les données sur le serveur.
    
* Utilisez l'attribut `placeholder` pour donner aux utilisateurs un indice sur l'entrée attendue.
    
* Pensez à l'expérience utilisateur lors du choix des types d'entrée. Par exemple, utilisez des boutons radio pour des options mutuellement exclusives.
    

Voici un extrait de code démontrant l'utilisation d'un élément de formulaire :

```html
<form>
  <label for="username">Nom d'utilisateur :</label>
  <input type="text" id="username" name="username" placeholder="Entrez votre nom d'utilisateur">

  <label for="password">Mot de passe :</label>
  <input type="password" id="password" name="password" placeholder="Entrez votre mot de passe">

  <label>Genre :</label>
  <input type="radio" name="gender" value="male"> Homme
  <input type="radio" name="gender" value="female"> Femme

  <label>S'abonner à la newsletter :</label>
  <input type="checkbox" name="subscribe" value="yes">

  <label for="message">Votre message :</label>
  <textarea id="message" name="message" placeholder="Entrez votre message"></textarea>

  <button type="submit">Soumettre</button>
</form>
```

### Balises auto-fermantes

L'élément `<input>` ou `<input />` ci-dessus est une balise auto-fermante, ce qui signifie qu'elle ne nécessite pas de balise de fermeture séparée.

Il existe d'autres balises auto-fermantes en HTML :

* Image (`<img>` ou `<img />`).
    
* Sauts de ligne (`<br>` ou `<br />`).
    
* Lien vers une ressource externe (`<link>` ou `<link />`).
    
* Règle horizontale (`<hr>` ou `<hr />`).
    
* Métadonnées (`<meta>` ou `<meta />`).
    
* Colonne de tableau (`<col>` ou `<col />`).
    
* URL de base pour les liens relatifs (`<base>` ou `<base />`).
    
* Opportunité de rupture de mot (`<wbr>` ou `<wbr />`).
    
* Zone (`<area>` ou `<area />`) qui définit une zone à l'intérieur d'une image map pour que l'image puisse avoir une région cliquable.
    

Note : HTML5 (dernière version de HTML) vous permet d'omettre la barre oblique (`/`) à la fin des balises auto-fermantes, mais l'inclure assure la compatibilité avec les anciennes normes comme XHTML et certains outils.

## Attributs HTML

Il s'agit d'informations ou de caractéristiques supplémentaires que vous pouvez appliquer aux éléments HTML pour modifier leur comportement, leur apparence ou définir certaines propriétés. Les attributs sont toujours inclus dans la balise d'ouverture d'un élément HTML et sont écrits sous forme de paires nom-valeur.

La syntaxe de base pour un attribut HTML est :

```html
<nomdelabalise attribut="valeur">Contenu</nomdelabalise>
```

Ici, `attribut` est le nom de l'attribut, et `"valeur"` est la valeur assignée à cet attribut.

Il existe de nombreux attributs disponibles pour divers éléments HTML, en voici quelques-uns :

### Attribut id

Il fournit un identifiant unique pour un élément HTML. Il doit être unique dans tout le document HTML.

L'attribut "id" vous aide à identifier et à contrôler des éléments spécifiques sur une page web, tout comme chaque numéro d'identification d'étudiant aide à les identifier de manière unique dans une école.

Exemple :

```html
<div id="header">Ceci est une div avec un attribut id.</div>
```

### Attribut class

Utilisé pour assigner un ou plusieurs noms de classe à un élément HTML. Il vous aide également à organiser et à styliser différentes parties d'une page web en les regroupant.

Voici la syntaxe pour l'attribut class :

```html
<nomdelabalise class="nomdeclasse1 nomdeclasse2 ...">Contenu</nomdelabalise>
```

Supposons que vous souhaitez styliser plusieurs paragraphes avec la même police et la même couleur. Au lieu d'écrire les mêmes styles CSS pour chaque paragraphe individuellement, vous pouvez assigner une classe commune à tous ces paragraphes et définir les styles pour cette classe dans votre fichier CSS. Exemple :

```html
<body>
  <p class="highlight">Ceci est le premier paragraphe.</p>
  <p class="highlight">Ceci est le deuxième paragraphe.</p>
  <p class="highlight">Ceci est le troisième paragraphe.</p>
</body>
```

**Note** : L'attribut "id" et l'attribut "class" en HTML servent des objectifs similaires en ce sens qu'ils permettent tous deux d'identifier de manière unique des éléments sur une page web. Cependant, il existe des différences clés entre les deux :

* Utilisez l'attribut "id" lorsque vous devez identifier de manière unique un seul élément.
    
* Utilisez l'attribut "class" lorsque vous souhaitez regrouper plusieurs éléments ensemble et appliquer un style ou une fonctionnalité à ces éléments collectivement.
    

Bien que les deux attributs puissent être utilisés pour le style, l'attribut "id" est plus adapté pour un style unique, tandis que l'attribut "class" est idéal pour appliquer des styles cohérents à plusieurs éléments.

### Attribut src (source)

Il spécifie l'URL source d'une image à afficher. Exemple :

```html
<img src="image.jpg" alt="Photo de Nuel Cas">
```

**Note** : L'attribut `alt` est utilisé pour fournir un texte alternatif pour une image si l'image échoue à se charger. Il sert de texte descriptif qui est affiché à la place de l'image, aidant les utilisateurs à comprendre le contenu ou le but de l'image même lorsqu'elle n'est pas visible.

### Attribut href (pour les liens)

Il spécifie l'URL vers laquelle le lien hypertexte pointe. Exemple :

```html
<a href="https://www.nuelcas.com">Visitez Nuel Cas</a>
```

### Attributs width et height (pour les images)

Ils déterminent la largeur et la hauteur d'une image en pixels. Exemple :

```html
<img src="image.jpg" alt="Photo de Nuel Cas" width="400" height="300">
```

### Attribut style

Permet d'appliquer des styles CSS en ligne à un élément HTML. Exemple :

```html
<p style="color: red; font-size: 18px;">Ceci est un texte rouge.</p>
```

### Attribut disabled (pour les éléments de formulaire)

Permet de désactiver l'interaction de l'utilisateur avec un élément de formulaire. Exemple :

```html
<input type="text" disabled>
```

### Attribut type (pour les éléments de formulaire et les éléments de liste)

Vous pouvez utiliser l'attribut `type` avec la balise `<ol>` pour changer le style de numérotation. Exemple :

```html
<ol type="A">
  <li>Élément A</li>
  <li>Élément B</li>
  <li>Élément C</li>
</ol>
```

Cela se rendra comme :

```text
A. Élément A
B. Élément B
C. Élément C
```

De plus, vous pouvez utiliser l'attribut `type` pour spécifier le type d'entrée de l'élément de formulaire. Par exemple, si vous voulez notifier le navigateur que cette entrée est pour un mot de passe, utilisez le code ci-dessous

```python
<input type="password" name="password" placeholder="Entrez votre mot de passe">
```

### Attribut name (pour les éléments de formulaire)

L'attribut `name` fournit un identifiant unique pour chaque champ de formulaire. Lorsque le formulaire est soumis au serveur, les données saisies dans chaque champ sont envoyées avec le nom correspondant sous forme de paire *clé-valeur*. L'extrait de code ci-dessous montre que vous voulez que le serveur identifie cette entrée comme un email.

```python
 <input type="email" id="email" name="email" placeholder="Entrez votre email">
```

**Note** : Comprendre et utiliser les attributs de manière efficace est essentiel pour contrôler l'apparence et le comportement des éléments dans vos documents HTML.

## Multimédia HTML

Vous pourriez avoir besoin d'intégrer divers types de contenu multimédia dans les pages web, tels que des images, de l'audio et de la vidéo. Ces éléments multimédias améliorent l'expérience utilisateur en rendant le contenu web plus engageant et dynamique.

Voici les différents types de multimédia que vous pouvez utiliser en HTML :

### Images

Les images sont le type de multimédia le plus courant en HTML. Vous pouvez ajouter des images à une page web en utilisant la balise `<img>`. Exemple :

```html
<img src="image.jpg" alt="Description de l'image" width="200" height="150">
```

Dans l'exemple ci-dessus, `src` spécifie l'URL source de l'image, `alt` fournit un texte alternatif pour l'accessibilité et le SEO, et `width` et `height` sont des attributs optionnels pour définir les dimensions de l'image.

### Audio

Vous pouvez intégrer des fichiers audio directement dans une page web en utilisant la balise `<audio>`. Cela vous permet de lire des clips audio, de la musique ou d'autres enregistrements sonores. Exemple :

```html
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
  Votre navigateur ne supporte peut-être pas l'élément audio.
</audio>
```

Dans l'exemple ci-dessus, `controls` fournit des contrôles de lecture, de pause et de volume pour l'utilisateur, `src` spécifie l'URL source du fichier audio, tandis que `type` spécifie le type [MIME](https://en.wikipedia.org/wiki/MIME) (Multipurpose Internet Mail Extensions) du fichier audio.

### Vidéo

La balise `<video>` est utilisée pour intégrer des fichiers vidéo dans une page web. Cela vous permet de lire des vidéos dans le contenu. Exemple :

```html
<video controls width="640" height="360">
  <source src="video.mp4" type="video/mp4">
  Votre navigateur ne supporte peut-être pas l'élément vidéo.
</video>
```

Dans l'exemple ci-dessus, `controls` fournit des contrôles de lecture, de pause et de volume pour l'utilisateur, `width` et `height` spécifient les dimensions de la vidéo, `src` spécifie l'URL source du fichier vidéo, tandis que `type` spécifie le type MIME du fichier vidéo.

### iframe

`<iframe>` vous permet d'afficher du contenu provenant d'une source ou d'une page différente à l'intérieur d'un cadre sur votre page web. Cela peut être utile pour intégrer des vidéos, des cartes, des pages web ou d'autres contenus externes. Exemple utilisant `<iframe>` pour intégrer une vidéo de YouTube :

```html
<iframe 
  src="https://www.youtube.com/embed/VIDEO_ID" 
  width="560" 
  height="315" 
  title="Vidéo YouTube" 
  frameborder="0" 
  allowfullscreen>
</iframe>
```

Dans l'extrait de code ci-dessus, l'attribut `src` spécifie l'URL de la page ou du contenu que vous souhaitez intégrer. Les tailles sont contrôlées à l'aide des attributs `width` et `height`. L'attribut `title` fournit une description pour le contenu, ce qui est important pour l'accessibilité.

L'attribut `frameborder` contrôle si l'iframe a une bordure (0 pour pas de bordure, 1 pour une bordure), tandis que l'attribut `allowfullscreen` permet à la vidéo d'être lue en mode plein écran.

**Note** : Remplacez `"VIDEO_ID"` par l'ID de la vidéo YouTube que vous souhaitez intégrer.

## Bonnes pratiques

1. Suivez une structure de document HTML appropriée :
    

* Commencez votre document HTML avec une déclaration `<!DOCTYPE html>` pour assurer la compatibilité avec les navigateurs et la conformité aux normes.
    
* Incluez toujours les balises `<html>`, `<head>` et `<body>` dans votre document.
    
* Utilisez la balise `<meta charset="UTF-8">` pour spécifier l'encodage des caractères de votre document.
    
* Définissez la langue de votre document en utilisant l'attribut de langue (`<html lang="fr">`).
    
* Incluez une balise de titre descriptive (`<title>`) dans la section head (`<head>`) pour fournir un contexte pour la page.
    

2. Utilisez des éléments HTML sémantiques :
    

* Utilisez des éléments HTML sémantiques comme `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>` et `<footer>` pour fournir de la clarté et de la structure à votre contenu. Les éléments sémantiques améliorent l'accessibilité, le SEO et la maintenabilité de votre code.
    

3. Commentez votre code :
    

* Utilisez des commentaires `<!-- -->` pour documenter votre code HTML, en expliquant son but et sa fonctionnalité. Les commentaires améliorent la lisibilité du code et facilitent la collaboration entre les développeurs.
    

4. Structurez votre contenu avec des balises appropriées :
    

* Utilisez les balises de titre `<h1>` à `<h6>` pour définir la hiérarchie de votre contenu.
    
* Utilisez les balises de paragraphe `<p>` pour séparer les blocs de texte en paragraphes distincts.
    
* Employez des listes (`<ul>`, `<ol>`, `<li>`) pour organiser et structurer le contenu de manière hiérarchique.
    

5. Regroupez les éléments avec `<div>` et `<span>` avec parcimonie :
    

* Utilisez les balises `<div>` et `<span>` selon les besoins pour regrouper et styliser les éléments, mais évitez les imbrications excessives et la dépendance excessive à ces éléments. Préférez des alternatives plus sémantiques lorsque cela est approprié.
    

6. Ne surutilisez pas les sauts de ligne (`<br>`) :
    

* Bien que les balises `<br>` puissent être utiles pour des sauts de ligne simples, évitez de les surutiliser à des fins de mise en page. Utilisez plutôt CSS et des éléments de niveau bloc pour des mises en page plus complexes afin de maintenir une meilleure lisibilité et maintenabilité du code.
    

7. Utilisez toujours un texte alternatif pour les images (attribut `alt`) :
    

* Incluez toujours un texte alternatif descriptif en utilisant l'attribut `alt` pour les images (balises `<img>`). Cela améliore l'accessibilité pour les utilisateurs ayant des déficiences visuelles et garantit que le contenu reste compréhensible même si les images ne se chargent pas.
    

8. Optimisez les formulaires pour l'expérience utilisateur (UX) :
    

* Incluez des attributs `name` significatifs pour les éléments de formulaire afin d'identifier et de traiter les données avec précision sur le serveur.
    
* Utilisez des types d'entrée appropriés (attribut `type`) pour les champs de formulaire afin d'améliorer l'expérience utilisateur et de garantir la validation des données.
    
* Utilisez l'attribut `placeholder` pour fournir des indices ou des entrées attendues pour les champs de formulaire.
    

9. Assurez la compatibilité avec les anciens navigateurs :
    

* Votre code doit subir des [tests de compatibilité](https://www.freecodecamp.org/news/cross-browser-compatibility-testing-best-practices-for-web-developers/) sur différents navigateurs et appareils pour garantir un rendu et une fonctionnalité cohérents.
    
* Incluez des solutions de repli appropriées pour les nouvelles fonctionnalités ou attributs HTML, cela aidera à maintenir la compatibilité avec les anciens navigateurs.
    

10. Restez à jour avec les normes HTML :
    

* Tenez-vous informé des dernières normes et bonnes pratiques HTML pour tirer parti des nouvelles fonctionnalités, améliorer les performances et renforcer l'expérience utilisateur de vos applications web.
    

En adhérant à ces bonnes pratiques, vous pouvez créer un code HTML bien structuré, accessible et maintenable qui contribue à la qualité globale et à l'utilisabilité de vos projets web.

#### Si vous avez lu, apprécié et souhaitez plus de ce contenu, n'hésitez pas à me contacter sur [X](https://twitter.com/casweb_dev) et [LinkedIn](https://www.linkedin.com/in/casmir-onyekani/) pour une collaboration supplémentaire.