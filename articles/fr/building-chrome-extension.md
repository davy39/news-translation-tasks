---
title: Comment créer votre propre extension Google Chrome
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-03T19:42:43.000Z'
originalURL: https://freecodecamp.org/news/building-chrome-extension
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/World-Wildlife-Day--1-.png
tags:
- name: chrome extension
  slug: chrome-extension
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment créer votre propre extension Google Chrome
seo_desc: "By Sampurna Chapagain\nIf you are a Google Chrome user, you've probably\
  \ used some extensions in the browser. \nHave you ever wondered how to build one\
  \ yourself? In this article, I will show you how you can create a Chrome extension\
  \ from scratch.\nTable ..."
---

Par Sampurna Chapagain

Si vous êtes un utilisateur de Google Chrome, vous avez probablement utilisé certaines extensions dans le navigateur. 

Vous êtes-vous déjà demandé comment en créer une vous-même ? Dans cet article, je vais vous montrer comment vous pouvez créer une extension Chrome à partir de zéro.

## Table des matières

* [Qu'est-ce qu'une extension Chrome](#heading-qu-est-ce-qu-une-extension-chrome) ?
* [À quoi ressemblera notre extension Chrome](#heading-a-quoi-ressemblera-notre-extension-chrome) ?
* [Comment créer une extension Chrome](#heading-comment-creer-une-extension-chrome)
* [Création d'un fichier manifest.json](#heading-fichier-manifestjson)
* [Conclusion](#heading-conclusion)

## Qu'est-ce qu'une extension Chrome ?

Une extension Chrome est un programme installé dans le navigateur Chrome qui améliore les fonctionnalités du navigateur. Vous pouvez en créer une facilement en utilisant des technologies web comme HTML, CSS et JavaScript.

Créer une extension Chrome est similaire à la création d'une application web, mais cela nécessite un fichier `manifest.json` dont nous parlerons dans la dernière section de cet article.

## À quoi ressemblera notre extension Chrome ?  


![Image](https://www.freecodecamp.org/news/content/images/2022/01/covid_report.gif)
_Dernier rapport Covid du Royaume-Uni - Extension Chrome_

Comme vous pouvez le voir, l'extension Chrome ci-dessus affiche les dernières données sur le Coronavirus (COVID-19) au Royaume-Uni. Nous allons voir comment créer cette extension dans cet article de blog.

Ici, nous utiliserons l'API [https://api.coronavirus.data.gov.uk/v1/data](https://api.coronavirus.data.gov.uk/v1/data) afin de récupérer les données. Nous n'afficherons que le dernier enregistrement pour la simplicité de cet article.

Le code source complet de ce projet peut être trouvé sur [GitHub](https://github.com/SampurnaC/chrome_extension_fcc).

## Comment créer une extension Chrome

Tout d'abord, nous devons créer un dossier vide où nous ajouterons nos fichiers HTML, CSS et JavaScript.

À l'intérieur du dossier, créons un fichier index.html avec ce code de base HTML :

```html
<!DOCTYPE html>
<html>
<head>
    <title>Statistiques Covid-19 - Royaume-Uni</title>
    <meta charset="utf-8">
</head>
<body>
</body>
</html>
```

Maintenant, ajoutons un lien vers le CDN Bootstrap dans la balise head. Nous utiliserons le [Framework Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) ici pour ne pas avoir à écrire du CSS supplémentaire dans cet exemple.

```html
<head>
    <title>Statistiques Covid-19 - Royaume-Uni</title>
    <meta charset="utf-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
```

Dans la démonstration, nous avons vu que les enregistrements sont affichés sous forme de tableau. Nous devons donc maintenant travailler à la création d'un tableau.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Statistiques Covid-19 - Royaume-Uni</title>
    <meta charset="utf-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-3" style="width: 450px;">
        <h2 class="text-center">Dernier rapport Covid - Royaume-Uni</h2>
        <table class="table table-bordered">
            <thead>
            <tr>
                <th>Date</th>
                <th>Pays</th>
                <th>Confirmés</th>
                <th>Décès</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td id="date"></td>
                <td id="areaName"></td>
                <td id="latestBy"></td>
                <td id="deathNew"></td>
            </tr>
            </tbody>
        </table>
    </div>
</body>
<script src="script.js"></script>
</html>



```

Le code ci-dessus crée un tableau avec une largeur de `450px`. Il y a quatre en-têtes différents dans un tableau : `Date`, `Pays`, `Confirmés` et `Décès`. 

Ici, vous pouvez voir que chaque donnée de tableau `td` s'est vu attribuer différents identifiants. Nous utiliserons la valeur de ces identifiants en JavaScript pour mettre à jour les données du tableau. De plus, ici nous avons chargé le JavaScript à la fin après avoir chargé tout le contenu HTML.

Maintenant, puisque le tableau a été affiché, nous devons travailler à l'écriture de JavaScript afin de récupérer les données de l'API.

Créons un fichier `script.js` et ajoutons le code suivant :

```javascript
async function fetchData() {
    const res = await fetch("https://api.coronavirus.data.gov.uk/v1/data");
    const record = await res.json();
    document.getElementById("date").innerHTML = record.data[0].date;
    document.getElementById("areaName").innerHTML = record.data[0].areaName;
    document.getElementById("latestBy").innerHTML = record.data[0].latestBy;
    document.getElementById("deathNew").innerHTML = record.data[0].deathNew;
}
fetchData();
```

Maintenant, décomposons le code ci-dessus :

* Ici, nous utilisons la fonction asynchrone appelée `fetchData`.
* Les données sont récupérées depuis l'API https://api.coronavirus.data.gov.uk/v1/data.
* Les données JSON sont stockées dans une variable appelée `record`.
* Le contenu HTML de td avec les identifiants `date`, `areaName`, `latestBy` et `deathNew` est mis à jour par les valeurs correspondantes de l'API.

Si nous vérifions le navigateur, nous pourrons voir le résultat suivant.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/covid_browser.gif)
_Dernier rapport Covid du Royaume-Uni - Aperçu du navigateur_

Les données sont récupérées depuis l'API et elles continuent de se mettre à jour dès que les données dans l'API changent.

## Fichier Manifest.json

Comme nous l'avons discuté précédemment, créer une extension Chrome est similaire à la création de n'importe quelle application web. La seule différence est que l'extension Chrome nécessite un fichier `manifest.json` où nous gardons toutes les configurations.

Le fichier manifest.json contient toutes les informations nécessaires pour créer l'extension Chrome. C'est le premier fichier que l'extension vérifie et tout est chargé à partir de ce seul fichier.

Maintenant, créons un fichier `manifest.json` dans le dossier racine et ajoutons le code suivant :

```json
{
    "name": "Statistiques Covid-19 Royaume-Uni",
    "version": "1.0.0",
    "description": "dernières données covid du Royaume-Uni",
    "manifest_version": 3,
    "author": "Sampurna Chapagain",
    "action": {
        "default_popup": "index.html",
        "default_title": "Dernier rapport Covid"
    }
}
```

Notre fichier `manifest.json` contient les valeurs de `name`, `version`, `description`, `manifest_version` (3 dans ce cas, qui est la dernière version du manifest), `author`, et les champs `action`. Dans le champ action, il y a la valeur pour `default_popup` qui contient le chemin vers le fichier HTML qui est `index.html` dans cet exemple. 

Vous pouvez consulter [ici](https://developer.chrome.com/docs/extensions/mv3/manifest/) pour voir toutes les configurations d'un fichier `manifest.json`.

Maintenant, puisque nous avons également ajouté le fichier manifest.json, nous sommes prêts à ajouter ce projet en tant qu'extension dans notre navigateur Chrome.

Pour cela, nous devons aller dans `Sélectionner plus d'outils` puis choisir `Extensions` dans le menu du navigateur comme montré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Untitled-design--1-.png)
_Navigation vers les extensions dans Chrome_

Après avoir choisi Extensions, cela redirige vers la page des extensions dans Chrome. Assurez-vous d'activer le `Mode développeur` ici.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Untitled-design--1--1.png)

Une fois cela fait, vous devez cliquer sur le bouton `Charger l'extension non empaquetée` qui nous permettra de charger notre projet dans le magasin d'extensions Chrome.

Maintenant, l'extension est disponible dans notre magasin d'extensions Chrome. Vous pouvez également épingler l'extension dans le navigateur comme montré dans le gif ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/pin_extension.gif)
_Épingler l'extension au navigateur_



Cette extension fonctionne uniquement dans votre navigateur. Si vous souhaitez la publier sur le Chrome Web Store, vous pouvez suivre ce [lien](https://developer.chrome.com/docs/webstore/register/).

## Conclusion

Si vous avez des connaissances en HTML, CSS et JavaScript, vous pouvez facilement créer des extensions Chrome. J'espère qu'après avoir lu cet article de blog, vous créerez des extensions cool.

Bon codage !

Vous pouvez me trouver sur [Twitter](https://twitter.com/saam_codes) pour du contenu quotidien lié au développement web.