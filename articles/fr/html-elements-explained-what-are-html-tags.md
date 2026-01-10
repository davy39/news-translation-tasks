---
title: 'Éléments HTML expliqués : Que sont les balises HTML et comment les utiliser
  ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/html-elements-explained-what-are-html-tags
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ce7740569d1a4ca34cb.jpg
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: toothbrush
  slug: toothbrush
seo_title: 'Éléments HTML expliqués : Que sont les balises HTML et comment les utiliser
  ?'
seo_desc: 'What are HTML Elements?

  Elements are the building blocks of HTML that describe the structure and content
  of a web page. They are the “Markup” part of HyperText Markup Language (HTML).

  HTML syntax uses the angle brackets (”<” and ”>”) to hold the name...'
---

## Qu'est-ce que les éléments HTML ?

Les éléments sont les blocs de construction du HTML qui décrivent la structure et le contenu d'une page web. Ils constituent la partie "Markup" du langage HyperText Markup Language (HTML).

La syntaxe HTML utilise les chevrons ("<") pour contenir le nom d'un élément HTML. Les éléments ont généralement une balise d'ouverture et une balise de fermeture, et donnent des informations sur le contenu qu'ils contiennent. La différence entre les deux est que la balise de fermeture a une barre oblique.

Examinons quelques exemples spécifiques de balises HTML.

## Élément p

La balise `<p>` signifie paragraphe, qui est la balise la plus courante utilisée pour créer des lignes de texte à l'intérieur d'un document HTML.

L'utilisation de la balise `<p>` est compatible avec d'autres balises, permettant d'ajouter des hyperliens (`<a>`) et du texte en gras (`<strong>`), entre autres.

### Exemple

```html
<html>
  <head>
    <title>Exemple de paragraphe</title>
  </head>
  <body>
    <p>
      Ceci est un paragraphe. C'est le premier de nombreux.
    </p>
    <p>
      Ceci est un autre paragraphe. Il apparaîtra sur une ligne séparée.
    </p>
  </body>
</html>

```

Vous pouvez également imbriquer un élément d'ancrage `<a>` dans un paragraphe.

### Exemple

```html
<p>Voici un <a href="https://freecodecamp.org">lien vers freeCodeCamp</a>.</p>
```

## Éléments de titre

Il existe six éléments de titre — `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`.

Les éléments de titre sont utilisés pour signifier l'importance du contenu en dessous d'eux. Plus le nombre du titre est bas, plus l'importance est élevée.

Par exemple, l'élément `<h1>` représente le titre principal de la page, et il ne devrait y en avoir qu'un par page. Cela aide les moteurs de recherche à comprendre le sujet principal de la page. Les éléments `<h2>` ont moins d'importance et doivent être placés sous l'élément de niveau supérieur `<h1>`.

### Exemple

```
<h1>Ceci est le titre principal.</h1>
<h2>Ceci est un sous-titre h2.</h2>
<h3>Ceci est un sous-titre h3.</h3>
<h4>Ceci est un sous-titre h4.</h4>
<h5>Ceci est un sous-titre h5.</h5>
<h6>Ceci est un sous-titre h6.</h6>

```

## Élément a

L'élément d'ancrage (`<a>`) crée un hyperlien vers une autre page ou un autre fichier. Pour lier à une page ou un fichier différent, la balise `<a>` doit également contenir un attribut `href`, qui indique la destination du lien.

Le texte entre les balises d'ouverture et de fermeture `<a>` devient le lien. Ce texte doit être une description significative de la destination du lien, et non une phrase générique telle que "Cliquez ici". Cela permet aux utilisateurs de lecteurs d'écran de naviguer parmi les différents liens d'une page et de comprendre quel contenu chaque lien va ouvrir.

Par défaut, une page liée est affichée dans la fenêtre actuelle du navigateur, sauf si une autre cible est spécifiée. Les styles de lien par défaut sont les suivants :

* Un lien non visité est souligné et bleu
* Un lien visité est souligné et violet
* Un lien actif est souligné et rouge

### Exemples

```html
  <a href="https://guide.freecodecamp.org/">freeCodeCamp</a>

```

Vous pouvez également créer un lien vers une autre section de la même page :

```html
  <h1 id="haut"></h1>
  <a href="#haut">Aller en haut</a>

```

Une image peut également être transformée en lien en enfermant la balise `<img>` dans une balise `<a>` :

```html
  <a href="https://guide.freecodecamp.org/"><img src="logo.svg"></a>

```

## Éléments de liste

Il existe deux principaux types de listes en HTML : ordonnées (`<ol>`) et non ordonnées (`<ul>`). Toutes les listes doivent contenir un ou plusieurs éléments de liste (`<li>`).

### Liste non ordonnée

La liste non ordonnée commence par la balise `<ul>` et les éléments de liste commencent par la balise `<li>`. Dans les listes non ordonnées, tous les éléments de liste sont marqués par des puces par défaut.

```
<ul>
  <li>Élément</li>
  <li>Élément</li>
  <li>Élément</li>
</ul>

```

Sortie :

* Élément
* Élément
* Élément

### Liste ordonnée

La liste ordonnée commence par la balise `<ol>` et les éléments de liste commencent par la balise `<li>`. Dans les listes ordonnées, tous les éléments de liste sont marqués par des nombres.

```
<ol>
  <li>Premier Élément</li>
  <li>Deuxième Élément</li>
  <li>Troisième Élément</li>
</ol>

```

Sortie :

1. Premier Élément
2. Deuxième Élément
3. Troisième Élément

## Élément em

L'élément `<em>` est utilisé pour _mettre en emphase_ du texte dans un document HTML. Cela peut être fait en enveloppant le texte que vous souhaitez mettre en emphase dans une balise `<em>` et une balise `</em>` respectivement. La plupart des navigateurs afficheront le texte enveloppé dans une balise `<em>` en italique.

Note : La balise `<em>` ne doit pas être utilisée pour mettre stylistiquement du texte en italique. La balise `<em>` est utilisée pour mettre l'accent sur le texte. Typiquement, la mise en forme CSS est utilisée pour mettre stylistiquement du texte en italique.

### Exemple

```
<body>
  <p>
    Le texte qui nécessite une emphase doit aller <em>ici</em>.
  </p>
</body>

```

## Élément i

L'élément `<i>` est utilisé pour désigner du texte qui est mis à part de son texte environnant d'une certaine manière. Par défaut, le texte entouré de balises `<i>` sera affiché en italique.

Dans les spécifications HTML précédentes, la balise `<i>` était uniquement utilisée pour désigner du texte à mettre en italique. Dans le HTML sémantique moderne, cependant, des balises telles que `<em>` et `<strong>` doivent être utilisées lorsque cela est approprié.

Vous pouvez utiliser l'attribut `class` de l'élément `<i>` pour indiquer pourquoi le texte dans les balises est différent du texte environnant. Vous pouvez vouloir montrer que le texte ou la phrase est d'une autre langue :

```html
<p>La phrase française <i class="francais">esprit de corps</i> est souvent
utilisée pour décrire un sentiment de cohésion et de camaraderie de groupe.</p>

```

## Élément strong

L'élément `<strong>` est utilisé pour désigner du texte qui est d'une grande importance ou urgence. La plupart des navigateurs afficheront le texte enveloppé dans une balise `<strong>` en gras.

Note : La balise `<strong>` ne doit pas être utilisée pour styliser le texte en gras. Utilisez CSS pour cela.

### Exemple :

```
<body>
  <p>
    <strong>Ceci</strong> est vraiment important.
  </p>
</body>

```

## Élément img

Un simple élément HTML `<img>` peut être inclus dans un document HTML comme ceci :

```html
<img src="chemin/vers/fichier/image" alt="ceci est une image cool" title="Un texte descriptif va ici">

```

Notez que les éléments `<img>` sont auto-fermants et ne nécessitent pas de balise de fermeture.

Les balises `alt` fournissent un texte alternatif pour une image. Une utilisation de la balise `alt` est pour les personnes malvoyantes utilisant un lecteur d'écran ; elles peuvent lire la balise `alt` de l'image afin de comprendre le sens de l'image.

L'attribut `title` est optionnel et fournira des informations supplémentaires sur l'image. La plupart des navigateurs affichent ces informations dans une info-bulle lorsque l'utilisateur survole l'image.

Notez que le chemin vers le fichier image peut être relatif ou absolu. De plus, rappelez-vous que l'élément `img` est auto-fermant, ce qui signifie qu'il ne se ferme pas avec la balise `</img>` mais se ferme avec un seul `>`.

### Exemples

```html
<img src="https://example.com/image.png" alt="ma photo" title="Ceci est une image d'exemple">

```

(Ceci suppose que le fichier HTML est à l'adresse [https://example.com/index.html](https://example.com/index.html), donc il est dans le même dossier que le fichier image)

est la même chose que :

```html
<img src="image.png" alt="ma photo" title="Ceci est une image d'exemple">

```

Parfois, un élément `<img>` utilisera également deux autres attributs pour spécifier sa taille, `height` et `width`, comme montré ci-dessous :

```html
<img src="image.png" alt="ma photo" width="650" height="400" />

```

Les valeurs sont spécifiées en pixels, mais la taille est généralement spécifiée en CSS plutôt qu'en HTML.

## **Élément nav**

L'élément `<nav>` est destiné à un bloc principal de liens de navigation. TOUS les liens d'un document ne doivent pas être à l'intérieur d'un élément `<nav>`.

Les navigateurs, tels que les lecteurs d'écran pour les utilisateurs handicapés, peuvent utiliser cet élément pour déterminer s'il faut omettre le rendu initial de ce contenu.

### Exemple

```html
<nav class="menu">
  <ul>
    <li><a href="#">Accueil</a></li>
    <li><a href="#">À propos</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

## **Élément header**

La balise `<header>` est un conteneur utilisé pour les liens de navigation ou le contenu introductif. Elle peut typiquement inclure des éléments de titre, tels que `<h1>`, `<h2>`, mais peut également inclure d'autres éléments tels qu'un formulaire de recherche, un logo, des informations sur l'auteur, etc.

Bien que ce ne soit pas obligatoire, la balise `<header>` est destinée à contenir le titre des sections environnantes. Elle peut également être utilisée plus d'une fois dans un document HTML. Il est important de noter que la balise `<header>` n'introduit pas une nouvelle section, mais est simplement l'en-tête d'une section.

### Exemple

```html
<article>
  <header>
    <h1>Titre de la Page</h1>
  </header>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
</article>
```

## **Élément textarea**

La balise textarea HTML vous permet de créer une zone qui contiendra du texte pour les commentaires ou les interactions des utilisateurs. Dans la plupart des cas, il est courant de voir la textarea utilisée comme partie d'un formulaire.

Les programmeurs utilisent la balise textarea pour créer un champ multilingue pour la saisie de l'utilisateur (utile surtout lorsque l'utilisateur doit pouvoir mettre sur le formulaire un texte plus long). Les programmeurs peuvent spécifier différents attributs pour les balises textarea.

### Exemple

```html
    <form>
      <textarea name="commentaire" rows="8" cols="80" maxlength="500" placeholder="Entrez votre commentaire ici..." required></textarea>
    </form>
```

Attributs les plus courants : les attributs `row` et `cols` déterminent la hauteur et la largeur de la textarea. L'attribut `placeholder` spécifie le texte visible pour l'utilisateur, il aide l'utilisateur à comprendre quelles données doivent être tapées. L'attribut `maxlength` détermine la longueur maximale du texte qui peut être tapé dans la textarea, l'utilisateur ne peut pas soumettre plus de caractères. L'attribut `required` signifie que ce champ doit être rempli avant la soumission du formulaire.

## Élément label

La balise `<label>` définit une étiquette pour un élément `<input>`.

Une étiquette peut être liée à un élément soit en utilisant l'attribut "for", soit en plaçant l'élément à l'intérieur de l'élément **label**.

### Exemple

```text
<label for="id">Étiquette</label>
<input type="text" name="text" id="id" value="votrevaleur"><br>
```

Comme vous pouvez le voir, l'attribut _for_ de la balise **label** doit être égal à l'attribut id de l'élément associé pour les lier ensemble.

### Support de la plateforme

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-18-at-4.01.48-PM.png)

### Attributs

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-18-at-4.02.13-PM.png)

### **Attribut Global**

La balise `<label>` supporte les Attributs Globaux en HTML.

### **Attribut d'Événement**

La balise `<label>` supporte les Attributs d'Événement en HTML.

L'élément `<label>` ne se rend pas comme quelque chose de spécial pour l'utilisateur. Cependant, il fournit une amélioration de l'utilisabilité pour les utilisateurs de souris, car si l'utilisateur clique sur le texte à l'intérieur de l'élément **label**, il bascule le contrôle.

## **Balise Meta**

La balise `<meta>` fournit les métadonnées sur le document HTML.

Ces métadonnées sont utilisées pour spécifier le jeu de caractères d'une page, sa description, ses mots-clés, l'auteur et la fenêtre d'affichage de la page.

Ces métadonnées n'apparaîtront pas sur le site web lui-même, mais elles seront utilisées par les navigateurs et les moteurs de recherche pour déterminer comment la page affichera le contenu et évaluer l'optimisation pour les moteurs de recherche (SEO).

### Exemple

```html
<head>
  <meta charset="UTF-8">
  <meta name="description" content="Brève description du contenu du site web ici">
  <meta name="keywords" content="HTML,CSS,XML,JavaScript">
  <meta name="author" content="Jane Smith">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- HTML5 a introduit une méthode pour permettre aux concepteurs web de prendre le contrôle de la fenêtre d'affichage, via la balise <meta>. La fenêtre d'affichage est la zone visible de l'utilisateur d'une page web. Un élément <meta> de fenêtre d'affichage donne au navigateur des instructions sur la façon de contrôler les dimensions et la mise à l'échelle de la page. -->  
</head>
```

## **Élément div**

La balise `<div>` est un conteneur générique qui définit une section dans votre document HTML. Un élément `<div>` est utilisé pour regrouper des sections d'éléments HTML ensemble et les formater avec CSS.

Un `<div>` est un élément de niveau bloc. Cela signifie qu'il prend sa propre ligne à l'écran. Les éléments juste après le `<div>` seront poussés vers la ligne du dessous. Pour un regroupement et un style similaires qui ne sont pas de niveau bloc, mais en ligne, vous utiliseriez plutôt la balise `<span>`. La balise est utilisée pour regrouper les éléments en ligne dans un document.

### **Exemple**

Voici un exemple de la façon d'afficher une section dans la même couleur :

```html
<div style="color:#ff0000">
  <h3>mon titre</h3>
  <p>mon paragraphe</p>
</div>
```

## Élément section

L'élément `<section>` définit une section où il n'y a pas d'élément HTML sémantique plus spécifique pour la représenter. Typiquement, un élément `<section>` inclura un élément de titre (`<h1>` - `<h6>`) comme élément enfant.

Par exemple, une page web pourrait être divisée en diverses sections telles que les sections d'accueil, de contenu et de contact.

Un élément `<section>` ne doit pas être utilisé à la place d'un élément `<div>` si un conteneur générique est nécessaire. Il doit être utilisé pour définir des sections dans une page HTML.

```html
<html>
<head>
  <title>Exemple de Section</title>
</head>
<body>
  <section>
    <h1>Titre</h1>
    <p>Un tas de contenu génial</p>
  </section>
</body>
</html>

```

## **Élément footer**

La balise `<footer>` désigne le pied de page d'un document HTML ou d'une section. Typiquement, le pied de page contient des informations sur l'auteur, des informations de copyright, des informations de contact et un plan du site. Toute information de contact à l'intérieur d'une balise `<footer>` doit être placée dans une balise `<address>`.

### **Exemple**

```html
<html>
<head>
  <title>Exemple de paragraphe</title>
</head>
<body>
  <footer>
    <p>&copy; 2017 Joe Smith</p>
  </footer>
</body>
</html>
```

## **Élément audio**

La balise `<audio>` définit un élément audio, qui peut être utilisé pour ajouter une ressource multimédia audio à un document HTML qui sera lu par le support natif de lecture audio intégré dans le navigateur plutôt que par un plugin de navigateur.

La balise audio prend actuellement en charge trois formats de fichiers OGG, MP3 et WAV qui peuvent être ajoutés à votre html comme suit.

### Ajout d'un OGG

```text
<audio controls>
  <source src="fichier.ogg" type="audio/ogg">
</audio>
```

### Ajout d'un MP3

```text
<audio controls>
  <source src="fichier.mp3" type="audio/mpeg">
</audio>
```

### Ajout d'un WAV

```text
<audio controls>
  <source src="fichier.wav" type="audio/wav">
</audio>
```

Il peut contenir une ou plusieurs sources audio, représentées en utilisant l'attribut src ou l'élément source.

### Ajout de plusieurs fichiers audio

```text
<audio controls>
  <source src="fichier-1.wav" type="audio/wav">
  <source src="fichier-2.ogg" type="audio/ogg">
  <source src="fichier-3.mp3" type="audio/mpeg">
</audio>
```

### Support des navigateurs pour différents types de fichiers

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-18-at-4.06.46-PM.png)

### **Attributs supportés**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-18-at-4.07.17-PM.png)

## **Élément iframe**

L'élément HTML `<iframe>` représente un cadre en ligne, qui vous permet d'inclure un document HTML indépendant dans le document HTML actuel. Le `<iframe>` est typiquement utilisé pour intégrer des médias tiers, vos propres médias, des widgets, des extraits de code, ou pour intégrer des applets tiers tels que des formulaires de paiement.

### **Attributs**

Voici quelques-uns des attributs de l'`<iframe>` :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-31-at-2.02.44-PM.png)

Les balises iframe sont utilisées pour ajouter une page web ou une application existante à votre site web dans un espace défini.

Lors de l'utilisation des balises iframe, l'attribut src doit être utilisé pour indiquer l'emplacement de la page web ou de l'application à utiliser dans le cadre.

```html
<iframe src="framesite/index.html"></iframe>
```

Vous pouvez définir les attributs de largeur et de hauteur pour limiter la taille du cadre.

```html
<iframe src="framesite/index.html" height="500" width="200"></iframe>
```

Les iframes ont une bordure par défaut, si vous souhaitez la supprimer, vous pouvez le faire en utilisant l'attribut style et en définissant les propriétés de bordure CSS sur none.

```html
<iframe src="framesite/index.html" height="500" width="200" style="border:none;"></iframe>
```

### **Exemples**

Intégration d'une vidéo YouTube avec un `<iframe>` :

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/v8kFT4I31es" 
frameborder="0" allowfullscreen></iframe>
```

Intégration de Google Maps avec un `<iframe>` :

```html
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d774386.2436462595!2d-74.53874786161381!3d40.69718109704434!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew+York%2C+NY%2C+USA!5e0!3m2!1sen!2sau!4v1508405930424" 
width="600" height="450" frameborder="0" style="border:0" allowfullscreen></iframe>
```

### **Texte alternatif**

Le contenu entre les balises d'ouverture et de fermeture `<iframe>` est utilisé comme texte alternatif, à afficher si le navigateur de l'utilisateur ne supporte pas les iframes.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/v8kFT4I31es" frameborder="0">
  <p>Votre navigateur ne supporte pas les iframes.</p>
</iframe>
```

### **Cibler un iframe dans un lien**

Tout élément d'ancrage peut cibler le contenu d'un élément `<iframe>`. Plutôt que de rediriger la fenêtre du navigateur vers la page web liée, il redirigera l'`<iframe>`. Pour que cela fonctionne, l'attribut `target` de l'élément `<a>` doit correspondre à l'attribut `name` de l'`<iframe>`.

```html
<iframe width="560" height="315" src="about:blank" frameborder="0" name="iframe-redir"></iframe>

<p><a href="https://www.youtube.com/embed/v8kFT4I31es" target="iframe-redir">Rediriger l'Iframe</a></p>
```

Cet exemple affichera un `<iframe>` vide initialement, mais lorsque vous cliquerez sur le lien ci-dessus, il redirigera l'`<iframe>` pour afficher une vidéo YouTube.

### **JavaScript et iframes**

Les documents intégrés dans un `<iframe>` peuvent exécuter JavaScript dans leur propre contexte (sans affecter la page web parente) comme d'habitude.

Toute interaction de script entre la page web parente et le contenu de l'`<iframe>` intégré est soumise à la politique de même origine. Cela signifie que si vous chargez le contenu de l'`<iframe>` depuis un domaine différent, le navigateur bloquera toute tentative d'accès à ce contenu avec JavaScript.