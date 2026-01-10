---
title: Comment générer des badges ReadMe avec Express
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-30T17:36:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-generate-readme-badges-with-express-and-squirrelly-77310125dca0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BqQhKwkKqIBn_lL-pmYHNg.png
tags:
- name: Express.js
  slug: expressjs
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment générer des badges ReadMe avec Express
seo_desc: 'By Ben Gubler

  I first came across this idea on this website. Since the tutorial there is a few
  years old, I wrote a new tutorial with updated code.

  If you’re in a hurry, you can find the completed code here.

  We all know about them or use them — the s...'
---

Par Ben Gubler

J'ai découvert cette idée pour la première fois sur [ce](https://odino.org/generating-badges-slash-shields-with-nodejs/) site web. Comme le tutoriel là-bas date de quelques années, j'ai écrit un nouveau tutoriel avec un code mis à jour.

*Si vous êtes pressé, vous pouvez trouver le code complet [ici](https://github.com/nebrelbug/badge-generator).*

Nous les connaissons tous ou les utilisons — les badges brillants en haut de presque tous les ReadMe qui disent des choses comme « **build: passing** » ou « **size: 10KB** ». Ce guide vous apprendra à générer vos propres badges, avec rien d'autre que Node.js, ExpressJS et Squirrelly.

### Passons au tutoriel

#### Prérequis

Ce tutoriel suppose que vous avez déjà installé Node.js et npm (ou yarn). Si ce n'est pas le cas, rendez-vous sur le site de Node [ici](https://nodejs.org/en/) (npm est installé par défaut).

#### Installation

Tout d'abord, créez un nouveau répertoire et accédez-y :

```
mkdir badge-generator && cd badge-generator
```

Ensuite, installez les dépendances nécessaires, [Express](https://expressjs.com/) et [Squirrelly](https://squirrelly.js.org/).

Avec npm :

```
npm install express squirrelly
```

Ou pour ceux qui utilisent yarn :

```
yarn add express squirrelly
```

#### Création du serveur

Nous n'aurons besoin que de deux fichiers pour notre programme, **index.js** et **template.svg** (que nous créerons ensuite).

Créez un fichier nommé **index.js** et collez le code suivant :

Cela ouvre un serveur sur le port 8080 et écoute les requêtes. À la fin de ce tutoriel, vous pourrez faire une requête à [**http://localhost:8080/texte-gauche/texte-droite/couleur**](http://localhost:8080/texte-gauche/texte-droite/couleur) et obtenir un badge SVG superbe ! Hourra ! Mais quelle est la partie du code avec `Sqrl` ?

```
var badge = Sqrl.renderFile(path.join(__dirname, 'template.svg'), req.params)
```

C'est là que Squirrelly intervient. Nous voulons servir un fichier image SVG, mais le contenu (largeur, longueur et texte) de l'image sera différent à chaque fois. Squirrelly est un **moteur de template**, un programme qui prend un fichier ou une chaîne appelée template et insère les données. Il fait aussi d'autres choses sympas, comme gérer le cache, mais nous n'aurons pas besoin de nous en soucier.

Le code ci-dessus lit le fichier nommé `template.svg`, puis utilise `req.params` (un objet qui contient les chemins) pour remplir le template. Dans ce cas, `req.params` ressemblera à :

```
{  left: "première-partie-du-chemin-url",  right: "deuxième-partie-du-chemin-url",  color: "troisième-partie"}
```

#### Création d'un template

Créez un nouveau fichier appelé `template.svg`, et collez le code suivant :

Vous pouvez lire la documentation complète de Squirrelly [ici](https://squirrelly.js.org/), mais essentiellement, tout ce qui se trouve entre doubles crochets : `{{` et `}}` sera remplacé par sa valeur réelle.

Mais attendez : nous n'avons passé que `left`, `right` et `color` — d'où viennent `leftWidth` et `rightWidth` ? C'est ce que fait le code ci-dessous (en haut du template) ; en utilisant l'aide `js` (qui vous permet d'écrire du JS à l'intérieur d'un template), il définit une nouvelle variable, appelée `leftWidth`.

```
{{js(options.leftWidth = options.left.length * 10)/}}
```

Il reste une chose à faire. Remarquez que la ligne 18 ressemble à ceci :

```
<rect ...stuff... fill="{{returnColor(options.color)/}}"/>
```

Avec les images SVG, l'attribut fill doit soit contenir l'une des quelques couleurs prédéfinies qui ne sont pas très belles, soit un code [RGB](https://en.wikipedia.org/wiki/RGB_color_model) ou hexadécimal. Nous voulons utiliser des codes hexadécimaux, mais il y a un piège : vous remarquerez que si vous entrez [**http://localhost:8080/du/texte/#fff**](http://localhost:8080/du/texte/#fff) dans un navigateur, il pense que le code hexadécimal à la fin est le hash à la fin de l'URL, et Express ne le reconnaît pas.

Ce que nous allons faire, c'est créer un helper (appelé `returnColor`) qui traduira les mots de couleur, comme 'brightgreen', 'green' et 'red', en codes hexadécimaux. Collez ce qui suit n'importe où dans index.js :

#### Vérifiez si cela fonctionne

Tapez `node index.js` dans votre terminal, puis allez sur [http://localhost:8080/test/badge/brightgreen](http://localhost:8080/test/badge/brightgreen). Si tout s'est bien passé, vous devriez voir un badge !

![Image](https://cdn-media-1.freecodecamp.org/images/1*s3-kyFWQZL_v7s8xDWn1vw.png)

Si quelque chose génère une erreur, comparez votre code avec le code fonctionnel [ici](https://github.com/nebrelbug/badge-generator).

Vous pouvez trouver plus d'informations sur Squirrelly ci-dessous.

[**Documentation de Squirrelly**](https://squirrelly.js.org/)  
[_Squirrelly ne fait que 2KB compressé, n'a 0 dépendances et est ultra-rapide._squirrelly.js.org](https://squirrelly.js.org/)

Merci d'avoir lu ce guide. J'espère qu'il a été utile !