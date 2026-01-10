---
title: Apprendre le HTML et le CSS en espagnol – Cours pour débutants
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2021-10-28T15:32:02.000Z'
originalURL: https://freecodecamp.org/news/learn-html-and-css-in-spanish-course-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/html-css-thumbnail.png
tags:
- name: CSS
  slug: css
- name: Español
  slug: espanol-2
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Apprendre le HTML et le CSS en espagnol – Cours pour débutants
seo_desc: 'Hi! If you speak Spanish and you want you learn HTML and CSS, you''re in
  the right place.

  In this article, you will find a brief introduction to the basics of HTML and CSS.
  Then you will find a free 5-hour course on HTML and CSS on our Spanish YouTube...'
---

Salut ! Si tu parles espagnol et que tu veux apprendre le HTML et le CSS, tu es au bon endroit.

Dans cet article, tu trouveras une brève introduction aux bases du HTML et du CSS. Ensuite, tu trouveras un [cours gratuit de 5 heures sur le HTML et le CSS sur notre chaîne YouTube en espagnol](https://www.youtube.com/watch?v=XqFR2lqBYPs&feature=youtu.be) où tu pourras apprendre le contenu plus en profondeur avec des exemples pratiques.

Cet article utilisera l'anglais pour résumer tout ce que tu apprendras à travers ce cours. Si tu connais des amis hispanophones, tu peux partager [cette version espagnole de cet article](https://www.freecodecamp.org/espanol/news/aprende-html-y-css-curso-desde-cero/).

Commençons ! ✨

## 📝 HTML et CSS : Description et objectif

Voyons ce que sont le HTML et le CSS et à quoi ils servent :

* **HTML** (HyperText Markup Language) est essentiel pour le développement web car nous l'utilisons pour définir la **structure** d'une page web, le contenu qui sera affiché sur le navigateur.
* **CSS** (Cascading Style Sheets) est un langage basé sur des règles que nous utilisons pour définir et assigner des styles aux éléments de notre page web.

Le HTML fonctionne avec le CSS pour créer les pages web que nous utilisons tous les jours sur nos navigateurs. Certaines pages web utilisent également JavaScript.

**💡 Astuce :** Les fichiers HTML ont une extension `**.html**` et les fichiers CSS ont une extension `**.css**`.

Réfléchis à cela un instant. Le site web que tu regardes en ce moment est fait de HTML et de CSS. Génial, non ?

Maintenant, parlons un peu des Chrome Developer Tools.

## 📸 Chrome Developer Tools

Tu peux voir le code HTML et CSS de n'importe quelle page web sur Google Chrome simplement en faisant un clic droit sur la page et en sélectionnant "Inspecter".

Cela ouvrira les Chrome Developer Tools, où tu verras deux sections principales :

* La section supérieure montre le code HTML de la page web. Cette partie est entourée par un rectangle orange dans l'image suivante.
* La section inférieure montre les styles CSS qui sont appliqués à l'élément actuellement sélectionné dans la section HTML. Cette partie est entourée par un rectangle vert dans l'image suivante.

![Image](https://www.freecodecamp.org/espanol/news/content/images/2021/10/chrome-dev-tools.png)
_Chrome Developer Tools_

## 📝 Introduction au HTML

Maintenant, commençons à plonger dans les fondamentaux du HTML. Voici un exemple de page web très simple :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>freeCodeCamp</title>
  </head>
  <body>
    <h1>freeCodeCamp</h1>
    <p>J'apprends le HTML et le CSS.</p>
  </body>
</html>
```

💡 **Astuce :** En HTML, l'indentation (l'espace que tu peux voir avant les lignes) n'est pas obligatoire car elle n'a pas d'impact sur le résultat final. Néanmoins, elle est fortement recommandée car elle nous aide à écrire des fichiers HTML faciles à lire, maintenir et comprendre. Nous utilisons généralement 2 espaces par niveau d'indentation en HTML.

Voyons les principaux composants du HTML.

### Éléments HTML

Un fichier HTML est composé d'éléments HTML. Ces éléments sont les composants individuels que nous utilisons pour créer la structure de la page web.

Voici un exemple d'élément :

```html
<h1>freeCodeCamp</h1>
```

💡 **Astuce :** Certains éléments peuvent agir comme des conteneurs pour d'autres éléments afin de nous aider à créer des structures plus complexes. Tu devrais indenter ces éléments imbriqués pour refléter la structure du site web, comme dans notre exemple précédent.

### **Balises HTML**

Chaque élément a une balise associée. Nous pouvons créer un élément en incluant sa balise dans notre fichier HTML.

Voici des exemples des balises les plus couramment utilisées :

* `**<html>**` – Tout le contenu du site web doit être contenu dans ces balises.
* `**<head>**` – Cet élément contient le titre de la page web que tu peux voir dans l'onglet de ton navigateur et il contient les métadonnées de la page web.
* `**<body>**` – Cet élément contient tous les éléments visibles de la page web. La structure de la page web doit être à l'intérieur de ces balises.
* **`<h1>`**, `<h2>`, **`<h3>`**, **`<h4>`**, `<h5>`, **`<h6>`** – Ces éléments créent des titres dans l'ordre d'importance de 1 à 6.
* `**<p>**` – Un paragraphe.
* `**<a>**` – Un lien vers un autre site web, une autre page web, ou vers des sections internes de la page web actuelle.
* `**<strong>**` – Cette balise nous permet de mettre en évidence un texte important. Il est affiché en texte gras.
* `**<em>**` – Cette balise nous permet de mettre en évidence un texte important. Il est affiché en texte italique.
* `**<form>**` – Cet élément représente un formulaire.
* `**<hr>**` – Une règle horizontale qui peut être utilisée pour séparer des paragraphes ou des sections de la page web.
* `**<input>**` – Un élément qui nous permet de créer les composants d'un formulaire. Il peut s'agir d'un champ de saisie de texte ou devenir un bouton radio ou une case à cocher.
* `**<footer>**` – Un pied de page.

💡 **Astuce :** le premier élément de notre page web doit être `**<!DOCTYPE html>**`. Il indique au navigateur que le fichier est un fichier HTML et quelle version de HTML utiliser.

La plupart des éléments HTML ont besoin d'une balise d'ouverture et d'une balise de fermeture. Nous écrivons le contenu de l'élément entre les balises.

Dans l'exemple précédent, nous avons créé un élément de type `**<h1>**` :

```html
<h1>freeCodeCamp</h1>
```

Cet élément a une balise d'ouverture et une balise de fermeture pour entourer son contenu.

* La balise d'ouverture est `**<h1>**`.
* La balise de fermeture est `**</h1>**`.

Tu peux voir cela dans le diagramme suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-90.png)

💡 **Astuce :** la différence entre la balise d'ouverture et la balise de fermeture est que la balise de fermeture a une barre oblique (`**/**`) avant le type d'élément.

Cependant, certains éléments n'ont **pas** besoin de balise de fermeture car ils n'agissent pas comme des conteneurs. Un exemple de ce type d'élément est l'élément `**<img>**` (image) :

`**<img src="freeCodeCamp.jpg">**`

### **Attributs HTML**

Les éléments HTML peuvent avoir des attributs. Ces attributs nous permettent de définir des informations supplémentaires sur l'élément. Ils incluent `**class**`, `**id**`, `**style**`, `**lang**`, `**src**`, et `**href**`.

Voici un exemple d'un élément HTML avec l'attribut `**class**` :

```
<h1 class="main-title">freeCodeCamp</h1>
```

Comme tu peux le voir dans cet exemple :

* Les attributs doivent être écrits dans la balise d'ouverture, avant le crochet de fermeture `**>**`.
* Les attributs et leurs valeurs sont séparés par un signe égal. À gauche, nous écrivons le nom de l'attribut et à droite nous écrivons sa valeur. Dans cet exemple, la valeur est `**main-title**`.
* La valeur de l'attribut doit être entourée de guillemets.

💡 **Astuce :** chaque type d'élément a un ensemble spécifique d'attributs que nous pouvons leur assigner et chaque attribut a un ensemble de valeurs possibles. Tu peux vérifier cela dans la documentation web [MDN Web Docs](https://developer.mozilla.org/es/).

### **Langue HTML**

Tu peux spécifier la langue de la page web et la langue de n'importe quel élément dans la structure HTML avec l'attribut `**lang**` et le code de la langue :

```html
<html lang="en">
```

Dans cet exemple, nous spécifions que la langue de la page web est l'anglais.

### Liens HTML

En HTML, tu peux créer des liens vers d'autres pages web et des liens vers des sections internes de la page web actuelle avec l'élément `**<a>**` (ancre) et l'attribut `**href**`.

Par exemple, cet élément te mènerait au site web de freeCodeCamp en espagnol :

```html
<a href="https://www.freecodecamp.org/espanol/">freeCodeCamp</a>
```

* Avec l'attribut `**href**`, nous spécifions où le lien mènera l'utilisateur.
* Le texte que nous écrivons entre les balises `**<a></a>**` est le texte que les utilisateurs verront. Dans ce cas, le texte est `**freeCodeCamp**`.

Nous pouvons également emmener les utilisateurs vers une autre page du même site web en sélectionnant un fichier HTML comme destination :

```html
<a href="about.html">À propos de moi</a>
```

Si nous assignons l'attribut `**id**` à un élément HTML, nous pouvons également créer un lien pour emmener l'utilisateur à cet élément sur la même page. Nous devons simplement écrire un hashtag suivi du nom de l'`**id**` comme valeur de l'attribut `**href**` :

```
<a href="#main-title">freeCodeCamp</a>

```

Dans cet exemple, le lien emmènerait l'utilisateur à l'élément avec l'`**id**` `main-title`.

💡 **Astuce :** l'élément `**<a>**` est différent de l'élément `**<link>**`. L'élément `**<link>**` est utilisé pour spécifier la relation entre le fichier HTML et une source externe comme un fichier CSS. Nous verrons un exemple de cela dans un instant.

### **Commentaires HTML**

Nous pouvons également écrire des commentaires en HTML. Les commentaires sont très utiles pour ajouter des notes que nous et d'autres développeurs pouvons lire lorsque nous ouvrons le fichier. Ils nous aident à expliquer et à comprendre la structure de la page web :

```
<!-- Ajouter un lien vers freeCodeCamp -->
```

**💡 Astuce :** Les commentaires ne font pas partie du résultat final. Ils ne peuvent être lus que lorsque tu ouvres le fichier HTML et ils sont utiles pour les développeurs qui travaillent avec le fichier.

### Listes HTML

En HTML, tu peux créer des listes ordonnées et des listes non ordonnées avec les balises `**<ol>**` et `**<ul>**`, respectivement.

Voici un exemple de chaque type de liste :

* Liste ordonnée

```html
<ol>
  <li>Bleu</li>
  <li>Vert</li>
  <li>Noir</li>
</ol>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-94.png)

* Liste non ordonnée

```html
<ul>
  <li>Bleu</li>
  <li>Vert</li>
  <li>Noir</li>
</ul>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-91.png)

**💡 Astuce :** la différence entre les deux types de listes est que les éléments des listes ordonnées sont numérotés tandis que les éléments des listes non ordonnées ne le sont pas.

### Images HTML

Pour créer une image en HTML, nous utilisons la balise `**<img>**`. Cet élément n'a pas besoin de balise de fermeture, seulement d'une balise d'ouverture.

Par exemple :

```html
<img src="https://bit.ly/fcc-relaxing-cat">
```

* Nous spécifions l'emplacement de l'image avec l'attribut `**src**` dans la balise `**<img>**`.

Tu devrais également assigner l'attribut `**alt**` à toutes les images de ta page web pour avoir un texte alternatif au cas où l'image ne serait pas téléchargée correctement ou si l'utilisateur doit utiliser un lecteur d'écran.

Par exemple :

```html
<img src="https://bit.ly/fcc-relaxing-cat" alt="Un chat orange mignon.">
```

Super ! Maintenant, tu connais les bases du HTML.

Commençons avec le CSS.

## **📸 Introduction au CSS**

Une fois que nous avons la structure HTML de notre page web, nous pouvons commencer à appliquer des styles aux éléments HTML avec le CSS.

Le CSS est un langage basé sur des règles. Ces règles nous permettent de spécifier comment les éléments seront présentés sur la page web en fonction des sélecteurs CSS, des propriétés et des valeurs.

### Comment appliquer des styles à tes éléments HTML

Il y a trois options pour appliquer des styles CSS à tes éléments HTML :

#### Styles en ligne :

Tu peux spécifier un style directement dans la balise d'ouverture de l'élément que tu veux personnaliser. Tu dois simplement assigner l'attribut style.

Par exemple :

```html
<h1 style="color: blue">freeCodeCamp</h1>
```

Dans cet exemple, la valeur de l'attribut **`style`** est la propriété **`color`** et sa valeur correspondante (`**blue**`). Ils sont entourés de guillemets.

**💡** Astuce :** la propriété et sa valeur doivent être séparées par un deux-points et un espace.

#### Élément <style> :

Si tu veux appliquer le même style à plusieurs éléments, tu peux le faire dans l'élément `**<style>**`, où tu peux écrire tes règles CSS en utilisant des sélecteurs CSS.

Par exemple :

```html
<head>
  <title>freeCodeCamp</title>
  <style>
    h1 {
      color: blue;
    }
  </style>
</head>
```

**💡 Astuce :** l'élément `**<style>**` doit être à l'intérieur de l'élément `**<head>**`.

#### Fichier CSS :

Cependant, ce que nous faisons généralement, c'est que nous écrivons les règles CSS dans un fichier CSS et ensuite nous lions ce fichier au fichier HTML.

Pour ce faire, nous incluons un élément `**<link>**` dans l'élément `**<head>**` et nous assignons l'emplacement du fichier comme valeur de l'attribut `**href**`.

```html
<link href="style.css" rel="stylesheet">
```

De cette manière, les styles que nous définissons dans le fichier CSS seront appliqués aux éléments HTML correspondants.

💡 **Astuce :** si le fichier CSS est dans le même dossier que le fichier HTML, nous écrivons simplement le nom du fichier CSS. Mais s'il est à l'intérieur d'un dossier, nous devons spécifier son emplacement relatif au fichier HTML.

### Règles CSS

Voici un exemple de règle CSS :

```
h1 {
  color: blue;
  font-size: 15px;
  font-weight: bold;
}
```

Analysons sa syntaxe :

* Tout d'abord, nous écrivons un sélecteur (dans ce cas, `**h1**`). Les sélecteurs nous permettent de sélectionner les éléments auxquels nous appliquerons les styles.
* Ensuite, à l'intérieur des accolades, nous écrivons les propriétés que nous voulons assigner aux éléments qui ont été sélectionnés.
* Les propriétés doivent être séparées de leurs valeurs par un deux-points et un espace après le deux-points.
* Et... nous terminons chaque ligne par un point-virgule.

💡 **Astuce :** il est recommandé d'indenter le contenu de la règle CSS en utilisant 2 espaces.

### Sélecteurs CSS

Il existe divers types de sélecteurs CSS qui nous permettent de sélectionner différents types d'éléments en fonction de critères spécifiques.

Les sélecteurs les plus couramment utilisés sont :

* **Sélecteurs de type :** Ils nous permettent de sélectionner tous les éléments d'un type spécifique.

Exemple :

```
h1 {
  color: blue;
  font-size: 15px;
  font-weight: bold;
}
```

Avec ce sélecteur, nous sélectionnons tous les éléments de type `**h1**`.

* **Sélecteurs de classe :** Ils nous permettent de sélectionner tous les éléments avec une classe particulière. Nous pouvons assigner la même classe à plusieurs éléments. Dans ce cas, nous écrivons un point avant le nom de la classe dans la règle CSS.

```
.green-text {
  color: green;
}
```

Avec ce sélecteur, nous sélectionnons tous les éléments avec la classe **`green-text`**.

* **Sélecteurs d'ID :** Ils nous permettent de sélectionner l'élément avec un ID spécifique. Chaque ID doit être unique et ne doit être appliqué qu'à un seul élément par page. Dans ce cas, nous écrivons un hashtag `**#**` avant le nom de l'`**id**` dans la règle CSS.

```
#main-title {
  color: red;
  font-size: 20px;
  font-weight: bold;
}
```

Avec ce sélecteur, nous sélectionnons tous les éléments avec l'`**id**` `**main-title**`.

## **📼 Cours YouTube**

Super. Maintenant que tu connais les bases du HTML et du CSS, regarde ce cours gratuit de 5 heures **en espagnol** avec plus de contenu, de détails, d'astuces et d'exemples étape par étape :

%[https://www.youtube.com/watch?v=XqFR2lqBYPs&feature=youtu.be]

✍️ Cours créé par Estefania Cassingena Navone ([@EstefaniaCassN](https://twitter.com/EstefaniaCassN)).

### **Contenu du cours**

Les sujets du cours sont divisés en concepts spécifiques, mais pour la liste suivante, je les ai divisés en leurs catégories principales pour te donner une idée générale du contenu :

### **HTML**

* Introduction au HTML et au CSS.
* Chrome Developer Tools.
* Éditeurs de code.
* Créer un fichier HTML et déclarer DOCTYPE.
* Éléments et balises.
* Titres et paragraphes.
* Documentation web.
* Indentation.
* Images.
* Liens.
* Listes ordonnées et listes non ordonnées.
* Format de texte.
* Formulaires.
* Boutons radio et cases à cocher.
* Éléments `**<div>**`.
* Pied de page.
* Élément `**<head>**`.

### **CSS**

* Introduction au CSS.
* Styles en ligne, le bloc `**<style>**`, et les fichiers CSS.
* Classes et IDs.
* Format de texte (taille, taille de police, familles de polices, et polices de secours).
* Google Fonts.
* Images.
* Remplissage et marges.
* Sélecteurs d'attributs.
* Unités absolues et relatives.
* Priorité des sélecteurs de type, des classes, des IDs, et des styles en ligne.
* Codes de couleur HEX et RGB en CSS.
* Variables CSS.

J'espère vraiment que tu aimeras le cours et que tu le trouveras utile pour faire tes premiers pas dans le monde du développement web.

Tu es également le bienvenu pour continuer à apprendre avec nos cours **en espagnol** :

%[https://www.youtube.com/watch?v=ivdTnPl1ND0]

%[https://www.youtube.com/watch?v=DLikpfc64cA]

%[https://www.youtube.com/watch?v=tWnyBD2src0]

###