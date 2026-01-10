---
title: Comment importer JavaScript et CSS depuis un CDN public
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-09T00:38:48.000Z'
originalURL: https://freecodecamp.org/news/import-javascript-and-css-from-a-public-cdn
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/cdn-imports-for-javascript.png
tags:
- name: 'content delivery network '
  slug: content-delivery-network
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
seo_title: Comment importer JavaScript et CSS depuis un CDN public
seo_desc: "By Alan Richardson\nWhen you're writing a Vanilla JavaScript application,\
  \ you don't have to host all the code you use on your own site. \nMost popular JavaScript\
  \ libraries are available from a public Content Delivery Network (CDN). \nThis can\
  \ simplify d..."
---

Par Alan Richardson

Lorsque vous écrivez une application Vanilla JavaScript, vous n'avez pas besoin d'héberger tout le code que vous utilisez sur votre propre site.

La plupart des bibliothèques JavaScript populaires sont disponibles depuis un Content Delivery Network (CDN) public.

Cela peut simplifier le déploiement de l'application et maintenir les dépendances à jour. En fait, si vous avez suivi un tutoriel JavaScript pour une bibliothèque, alors vous avez probablement déjà utilisé un CDN public sans peut-être en être conscient.

## Qu'est-ce qu'un CDN ?

Un CDN est un Content Delivery Network. Ce sont des services d'hébergement de fichiers pour plusieurs versions de bibliothèques courantes. Ils sont généralement très performants et offrent des fichiers mis en cache par localisation, de sorte que, peu importe où se trouvent vos utilisateurs, ils reçoivent les fichiers depuis des emplacements géographiques proches d'eux. Cela peut rendre votre application plus rapide que l'hébergement des fichiers vous-même.

Les CDN ont également l'avantage que si vous utilisez des bibliothèques communes à plusieurs sites, vos utilisateurs peuvent déjà avoir le fichier en cache dans leur navigateur. Cela accélère votre site car le navigateur n'a pas besoin de télécharger à nouveau la bibliothèque.

Par exemple, JQuery dispose d'un [CDN officiel JQuery](https://releases.jquery.com/). Si la plupart des applications JQuery importent la bibliothèque JQuery depuis ce CDN, alors les utilisateurs sont plus susceptibles d'avoir JQuery dans leur cache déjà.

## CDN pilotés par `npm`

Toutes les bibliothèques n'ont pas leur propre CDN. La plupart des bibliothèques se déploient sur [npmjs.com](https://npmjs.com) et dépendent du programmeur ajoutant la bibliothèque à leur projet via `npm` au moment de la construction. `npm` télécharge la bibliothèque depuis un CDN et l'ajoute au projet localement.

Nous n'avons pas besoin d'utiliser `npm` et les processus de construction JavaScript pour profiter de l'écosystème `npm`. Nous pouvons utiliser un 'CDN piloté par npm' comme hôte pour les bibliothèques, sans avoir à utiliser `npm`.

Un 'CDN piloté par npm' est un CDN qui héberge le code de distribution pour les bibliothèques qui se déploient sur `npm`.

Par exemple, [AG Grid](https://ag-grid.com), que j'ai démontré dans mon article "[How to Convert a Static HTML Table to a Dynamic JavaScript Data Grid](https://www.freecodecamp.org/news/convert-html-table-to-dynamic-javascript-data-grid/)", se déploie sur `npm` mais ne dispose pas de son propre CDN. Au lieu de cela, les programmeurs peuvent ajouter une référence directe à AG Grid depuis un CDN comme [unpkg.com](https://unpkg.com/).

```html
<script src=
"https://unpkg.com/ag-grid-community/dist/ag-grid-community.min.nostyle.js">
</script>
```

Les CDN pilotés par `npm` surveillent les versions distribuées via `npm` et hébergent les versions sur leur propre site.

Dans le code source de mon précédent article sur freeCodeCamp, j'ai utilisé le CDN unpkg.com pour importer AG Grid dans mon code en utilisant un élément `script`.

Comme pour tout code que nous copions et collons, il est utile de comprendre ce qu'il fait afin de pouvoir gérer les éventuels problèmes.

## Quels CDN sont disponibles ?

Je n'ai jamais utilisé que trois CDN :

- [Unpkg.com](https://unpkg.com)
- [jsDelivr.com](https://www.jsdelivr.com)
- [cdnjs.com](https://cdnjs.com)

Ce sont tous des sites professionnels et bien gérés. Et la principale raison pour laquelle je choisis l'un plutôt que l'autre est que le tutoriel que j'ai suivi pour une bibliothèque utilisait ce CDN particulier dans le code.

Savoir que plusieurs CDN sont disponibles est utile car :

- une version particulière d'une bibliothèque que vous souhaitez utiliser peut ne pas être sur tous les CDN
- si un CDN commence à avoir des problèmes, vous pouvez modifier votre code pour utiliser un autre
- certaines bibliothèques peuvent être plus populaires sur un CDN que sur un autre et vous pouvez vouloir utiliser le CDN le plus populaire pour augmenter les chances que le code de la bibliothèque JavaScript soit mis en cache dans le navigateur de vos utilisateurs.


## Les CDN `npm` distribuent plus que du JavaScript

Les CDN délivrent plus que du JavaScript. Par exemple, AG Grid déploie des fichiers CSS ainsi que du JavaScript.

Ceux-ci seraient référencés depuis le CDN comme d'habitude en utilisant des éléments `link`.

Par exemple, AG Grid utilise deux feuilles de style.

La feuille de style structurelle fournit le CSS qui disposera les données sous forme de grille.

```
<link 
 rel="stylesheet"
 href="https://unpkg.com/ag-grid-community/dist/styles/ag-grid.css"
>
```    

La feuille de style de thème fournit l'esthétique visuelle pour la grille.

```
<link 
 rel="stylesheet" 
 href="https://unpkg.com/ag-grid-community/dist/styles/ag-theme-alpine.css"
>
```    

Ces deux fichiers CSS sont également déployés sur npmjs.com et peuvent être inclus dans notre projet depuis un CDN.


## Comment (et pourquoi) contrôler la version de la bibliothèque

Dans mon [outil open source d'édition de tableaux](https://eviltester.github.io/grid-table-editor/#), j'utilise trois bibliothèques : AG Grid, PapaParse et Faker.

Faker a récemment eu un problème où une version récente déployée sur npm avait des problèmes. Donc, si mon code avait utilisé la dernière version par défaut, mon application aurait échoué.

Heureusement, j'avais importé une version spécifique de faker depuis unpkg. Comme vous pouvez le voir dans l'URL `src` ci-dessous, j'ai inclus la version `5.5.3` :

```html
<script src=
    "https://unpkg.com/faker@5.5.3/dist/faker.min.js">
</script>
```

Il y a plusieurs avantages à contrôler la version :

- vous aurez testé votre application sur une version spécifique. Si vous déployez en production et permettez à la version de changer avec chaque nouvelle version, alors votre application peut progressivement présenter des bugs ou des incompatibilités au fil du temps car vous n'avez pas testé votre application contre la nouvelle version de la bibliothèque.
- lors de l'utilisation de plusieurs versions de bibliothèques, les versions futures peuvent entrer en conflit les unes avec les autres, provoquant à nouveau l'échec de votre application en production et éventuellement sans que vous le remarquiez.

J'importe les trois bibliothèques que j'utilise à des versions spécifiques :

```html
<script src="https://unpkg.com/ag-grid-community@26.2.1/dist/ag-grid-community.min.js"></script>
<script src="https://unpkg.com/papaparse@5.3.0/papaparse.min.js"></script>
<script src="https://unpkg.com/faker@5.5.3/dist/faker.min.js"></script>
```

Cela me permet de contrôler les tests et je suis plus confiant que tout bug dans l'application sera le résultat de mon codage, plutôt que d'une mise à jour d'une bibliothèque utilisée dans le projet.

Les différents CDN peuvent avoir une syntaxe différente pour contrôler les numéros de version. Mais vous pourrez voir le format à utiliser en recherchant la bibliothèque sur le CDN et en suivant la documentation fournie par chaque CDN.

Voici les listes pour AG Grid sur chacun des sites CDN :

- [Unpkg.com - AG Grid](https://unpkg.com/ag-grid-community/)
- [jsDelivr.com - AG Grid](https://www.jsdelivr.com/package/npm/ag-grid-community)
- [cdnjs.com - AG Grid](https://cdnjs.com/libraries/ag-grid)

Si vous suivez les liens pour les packages AG Grid, vous verrez que chaque site a une interface légèrement différente. Mais ils permettent tous de sélectionner une version spécifique de AG Grid et de copier et coller l'URL à ajouter à votre fichier HTML.

## CDN en pratique

Ci-dessous se trouve un simple fichier HTML qui affichera une grille de données à l'écran.

Je n'ai qu'à déployer le fichier HTML, car la bibliothèque AG Grid est chargée dans le navigateur depuis le CDN.

Dans l'exemple ci-dessous, je charge la version 26.2.1 de AG Grid et les fichiers CSS depuis le **CDN unpkg.com**.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Exemple AG Grid ajouté via CDN</title>
    <script src="https://unpkg.com/ag-grid-community@26.2.1/dist/ag-grid-community.min.nostyle.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/ag-grid-community@26.2.1/dist/styles/ag-grid.css">
    <link rel="stylesheet" href="https://unpkg.com/ag-grid-community@26.2.1/dist/styles/ag-theme-alpine.css">
</head>
<body>

    <div id="myGrid" style="height: 200px; width:500px;" class="ag-theme-alpine"></div>

<script>
document.addEventListener('DOMContentLoaded', () => {

    const columnDefs = [
        { field: "cdn" },
        { field: "url" },
    ];

    const rowData = [
        { cdn: "jsDelivr", url: "https://www.jsdelivr.com"},
        { cdn: "Unpkg", url: "https://Unpkg.com" },
        { cdn: "cdnJS", url: "https://cdnjs.com" }
    ];


    const gridOptions = {
        columnDefs: columnDefs,
        rowData: rowData,
        /* permettre la copie et le collage manuels */
        enableCellTextSelection:true,
        ensureDomOrder:true
    };


    const gridDiv = document.querySelector('#myGrid');
    new agGrid.Grid(gridDiv, gridOptions);
});
</script>
</body>
</html>
```

[Les imports Unpkg sont démontrés dans cette page html déployée.](https://eviltester.github.io/freecodecampexamples/javascript-cdns/adding-ag-grid-from-unpkg.html)

![cdns et leurs urls](https://www.freecodecamp.org/news/content/images/2022/02/cdn-urls.png)

Je pourrais facilement utiliser d'autres CDN en changeant les éléments `script` et `link` dans la section `head` de mon fichier `html`.

**JSDelivr** utilisant la version 26.2.1

- https://cdn.jsdelivr.net/npm/ag-grid-community@26.2.1/dist/ag-grid-community.min.noStyle.js
- https://cdn.jsdelivr.net/npm/ag-grid-community@26.2.1/dist/styles/ag-grid.css
- https://cdn.jsdelivr.net/npm/ag-grid-community@26.2.1/dist/styles/ag-theme-alpine.css

[Les imports JSDelivr sont démontrés dans cette page html déployée.](https://eviltester.github.io/freecodecampexamples/javascript-cdns/adding-ag-grid-from-jsdelivr.html)

**CdnJS** utilisant la version 26.2.1. CdnJS adopte une approche légèrement différente pour le nom des versions, il est donc utile de vérifier la liste déroulante des versions sur la [page CdnJS AG Grid](https://cdnjs.com/libraries/ag-grid)

- https://cdnjs.cloudflare.com/ajax/libs/ag-grid/Docs-26.2.0-20211117/ag-grid-community.min.noStyle.min.js
- https://cdnjs.cloudflare.com/ajax/libs/ag-grid/Docs-26.2.0-20211117/styles/ag-grid.min.css
- https://cdnjs.cloudflare.com/ajax/libs/ag-grid/Docs-26.2.0-20211117/styles/ag-theme-alpine.min.css

[Les imports CdnJS sont démontrés dans cette page html déployée.](https://eviltester.github.io/freecodecampexamples/javascript-cdns/adding-ag-grid-from-cdnjs.html)

## Résumé

Nous n'avons pas toujours besoin de déployer les bibliothèques JavaScript sur notre site avec nos fichiers HTML. Au lieu de cela, nous pouvons les inclure de manière à ce qu'elles soient livrées par un Content Delivery Network.

De nombreux tutoriels que nous suivons montreront des exemples de cela.

Si nous importons JavaScript ou CSS depuis un CDN, nous devons ajouter le numéro de version de la bibliothèque que nous utilisons pour protéger notre exemple déployé des futurs problèmes si la bibliothèque est mise à jour.

Une bonne habitude à prendre est d'ajouter la version même lorsque nous suivons un tutoriel. Si nous remarquons que les fichiers inclus depuis le CDN n'ont pas de version, il est utile de visiter le CDN pour découvrir quelle est la version actuelle de la bibliothèque. Ensuite, vous pouvez ajouter ce numéro de version à votre source.

Ce sont des ajustements comme celui-ci qui rendront les projets de portfolio que vous créez sur Github un peu plus professionnels.