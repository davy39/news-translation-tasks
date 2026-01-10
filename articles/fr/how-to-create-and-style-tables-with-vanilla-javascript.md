---
title: Comment créer et styliser des tableaux avec Vanilla JavaScript
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2025-10-21T19:03:29.487Z'
originalURL: https://freecodecamp.org/news/how-to-create-and-style-tables-with-vanilla-javascript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761066375438/ad2ff6f1-336c-4d32-89f7-3294a4bfebbd.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
- name: Web Design
  slug: web-design
seo_title: Comment créer et styliser des tableaux avec Vanilla JavaScript
seo_desc: 'Tables are one of the most useful ways to display structured data, whether
  you’re showing a list of users, sales figures, or project reports.

  In this tutorial, you will learn how to:


  Build tables using plain HTML


  Style them using CSS


  Create and ma...'
---

Les tableaux sont l'un des moyens les plus utiles pour afficher des données structurées, que vous présentiez une liste d'utilisateurs, des chiffres de vente ou des rapports de projet.

Dans ce tutoriel, vous apprendrez comment :

* Construire des tableaux en utilisant du HTML pur
    
* Les styliser à l'aide de CSS
    
* Créer et manipuler des tableaux dynamiquement en utilisant **vanilla JavaScript**
    

À la fin, vous comprendrez non seulement comment faire cela, mais aussi pourquoi c'est important. Vous apprendrez également à séparer les données de la présentation, ce qui est au cœur du développement web moderne.

## Table des matières

1. [Créer un tableau simple avec HTML](#heading-creer-un-tableau-simple-avec-html)
    
2. [Comprendre et styliser les bordures](#heading-comprendre-et-styliser-les-bordures)
    
3. [Quand utiliser HTML vs JavaScript pour les tableaux](#heading-quand-utiliser-html-vs-javascript-pour-les-tableaux)
    
4. [Comment construire un tableau dynamiquement avec JavaScript](#heading-comment-construire-un-tableau-dynamiquement-avec-javascript)
    
5. [Explication étape par étape](#heading-explication-etape-par-etape)
    
6. [Comment ajouter des classes CSS pour le stylisage](#heading-comment-ajouter-des-classes-css-pour-le-stylisage)
    
7. [Comment le transformer en une fonction réutilisable](#heading-comment-le-transformer-en-une-fonction-reutilisable)
    
8. [Dernières réflexions et conclusion](#heading-dernieres-reflexions-et-conclusion)
    

## Créer un tableau simple avec HTML

Avant d'impliquer JavaScript, comprenons d'abord comment fonctionne un tableau HTML standard.

Un tableau en HTML est construit à partir de quelques balises clés :

| **Balise** | **Description** |
| --- | --- |
| `<table>` | Définit le conteneur principal du tableau |
| `<thead>` | Groupe les lignes d'en-tête |
| `<tbody>` | Contient les lignes de données du tableau |
| `<tr>` | Définit une ligne |
| `<th>` | Définit une cellule d'en-tête (en gras et centrée par défaut) |
| `<td>` | Définit une cellule de données |

Voici un exemple minimal :

```html
<table border="1">
  <thead>
    <tr>
      <th>Name</th>
      <th>Age</th>
      <th>Occupation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Fahim</td>
      <td>25</td>
      <td>Software Engineer</td>
    </tr>
  </tbody>
</table>
```

![Rendu du code](https://cdn.hashnode.com/res/hashnode/image/upload/v1760798670028/487aa67e-67db-4d78-b37e-6824ea7cb366.png align="center")

Laissez-moi décomposer ce fragment de code correctement :

* `<table>` commence le tableau.
    
* `<thead>` définit la section d'en-tête du tableau.
    
* À l'intérieur de `<thead>`, nous avons un `<tr>` (ligne de tableau), qui contient des éléments `<th>` (ce sont les en-têtes de colonnes).
    
* `<tbody>` contient les données réelles. Chaque `<tr>` à l'intérieur représente un enregistrement, et chaque `<td>` à l'intérieur de cette ligne est une cellule.
    

L'attribut `border="1"` donne un contour fin autour des cellules. C'est utile pour la visualisation lorsque vous apprenez à manipuler les tableaux.

## Comprendre et styliser les bordures

Vous avez peut-être remarqué l'attribut `border` dans la balise `<table>` :

```html
<table border="1">
```

C'est un moyen rapide d'ajouter des contours visibles. Vous pouvez même les rendre plus épais, comme ceci :

```html
<table border="5">
```

Le code ci-dessus rendra des bordures plus épaisses, comme ceci :

![Rendu avec border=5](https://cdn.hashnode.com/res/hashnode/image/upload/v1760798709116/7225688d-1a13-4199-a527-2001df5705c2.png align="center")

Mais il y a un bémol...

### Pourquoi utiliser `border` n'est pas une bonne pratique

L'attribut `border` est une ancienne technique de stylisage en ligne. Le développement web moderne sépare la structure (HTML) de la présentation (CSS). Cela signifie que nous utilisons désormais le CSS pour tout le stylisage visuel.

Voici l'équivalent moderne :

```css
table {
  border-collapse: collapse; /* empêche les doubles bordures */
  border: 2px solid #444;
}

th, td {
  border: 1px solid #666;
  padding: 8px;
  text-align: left;
}
```

## Quand utiliser HTML vs JavaScript pour les tableaux

Vous pouvez tout à fait créer des tableaux entièrement en HTML, mais seulement si les données sont statiques.

Utilisez **HTML** uniquement lorsque :

* Les données ne changent pas souvent (comme une liste de prix statique).
    
* Vous connaissez le nombre exact de lignes et de colonnes.
    
* Vous ne récupérez pas de données d'une source externe.
    

Utilisez **JavaScript** lorsque :

* Les données sont dynamiques (par exemple, récupérées via une API).
    
* Vous souhaitez mettre à jour le tableau en fonction des entrées de l'utilisateur.
    
* Vous voulez trier, filtrer ou paginer votre tableau de manière interactive.
    

JavaScript vous permet de construire des tableaux par programmation en définissant les données dans un tableau ou un objet et en laissant le code gérer le rendu.

## **Comment construire un tableau dynamiquement avec JavaScript**

Nous allons maintenant créer un tableau dynamique en utilisant JavaScript. D'abord, je vais vous montrer le code complet, puis nous le décomposerons étape par étape pour que vous puissiez comprendre exactement ce qui se passe.

### Exemple de code :

```html
<!DOCTYPE html>
<html>
<head>
  <title>JS Table Example</title>
</head>
<body>

<div id="table-container"></div>

<script>
  // Étape 1 : Définir vos données
  const data = [
    { name: "Fahim", age: 25, job: "Software Engineer" },
    { name: "Sara", age: 29, job: "Designer" },
    { name: "David", age: 31, job: "Manager" }
  ];

  // Étape 2 : Créer un élément table
  const table = document.createElement("table");
  table.border = "1"; // pour la visibilité uniquement

  // Étape 3 : Ajouter les en-têtes
  const headers = ["Name", "Age", "Job"];
  const headerRow = document.createElement("tr");

  headers.forEach(text => {
    const th = document.createElement("th");
    th.textContent = text;
    headerRow.appendChild(th);
  });
  table.appendChild(headerRow);

  // Étape 4 : Ajouter les lignes de données
  data.forEach(item => {
    const row = document.createElement("tr");
    Object.values(item).forEach(value => {
      const cell = document.createElement("td");
      cell.textContent = value;
      row.appendChild(cell);
    });
    table.appendChild(row);
  });

  // Étape 5 : Insérer le tableau dans le DOM
  document.getElementById("table-container").appendChild(table);
</script>

</body>
</html>
```

![Rendu du tableau](https://cdn.hashnode.com/res/hashnode/image/upload/v1760798906301/10a7abdf-364a-4b9d-9691-17113ef4229a.png align="center")

### Explication étape par étape

#### Étape 1 : Définir les données – Séparer les données de la présentation

Dans le développement web, les données et la présentation doivent être maintenues séparées. Dans ce contexte, les données sont le contenu (comme les noms, les âges, les emplois) et la présentation est l'apparence de ces données (mise en page du tableau HTML, couleurs, etc.).

Nous définissons nos données comme un tableau d'objets :

```js
const data = [
  { name: "Fahim", age: 25, job: "Software Engineer" },
  { name: "Sara", age: 29, job: "Designer" },
  { name: "David", age: 31, job: "Manager" }
];
```

Cette structure rend nos données flexibles. Si vous les récupérez plus tard d'une API ou d'une base de données, votre logique de rendu de tableau reste la même.

Cela reflète également le fonctionnement des Framework modernes (comme React ou Vue) : votre interface utilisateur rend simplement ce qui se trouve dans vos données.

#### Étape 2 : Créer l'élément de tableau

```js
const table = document.createElement("table");
table.border = "1";
```

Ici, nous utilisons `document.createElement()`, une méthode de l'API DOM qui crée des éléments par programmation. Nous ne l'avons pas encore ajouté à la page. Il est juste stocké en mémoire.

Pourquoi le construire d'abord en mémoire ? Eh bien, c'est plus rapide. Ajouter de nombreux éléments au DOM un par un provoque des reflows (le navigateur recalcule la mise en page). Construire la structure d'abord et l'ajouter une seule fois à la fin réduit les recalculs de mise en page et améliore les performances.

#### Étape 3 : Ajouter la ligne d'en-tête

```js
const headers = ["Name", "Age", "Job"];
const headerRow = document.createElement("tr");

headers.forEach(text => {
  const th = document.createElement("th");
  th.textContent = text;
  headerRow.appendChild(th);
});
table.appendChild(headerRow);
```

Ici, nous bouclons à travers les étiquettes d'en-tête et créons dynamiquement des cellules `<th>`.

Nous générons les en-têtes automatiquement car si vous chargez plus tard des données à partir d'un fichier JSON, vous pouvez extraire automatiquement les noms de colonnes en utilisant `Object.keys(data[0])`. Cela évite le codage en dur et rend la génération de votre tableau plus flexible.

#### Étape 4 : Remplir les lignes de données

```js
data.forEach(item => {
  const row = document.createElement("tr");
  Object.values(item).forEach(value => {
    const cell = document.createElement("td");
    cell.textContent = value;
    row.appendChild(cell);
  });
  table.appendChild(row);
});
```

Nous bouclons sur chaque objet de données, créons un `<tr>` pour chacun, puis remplissons les cellules `<td>` pour chaque valeur. `textContent` garantit que nous insérons le texte en toute sécurité (pas d'injection HTML).

#### Étape 5 : Insérer le tableau dans le DOM

```js
document.getElementById("table-container").appendChild(table);
```

C'est ici que notre tableau apparaît enfin sur la page. Nous sélectionnons le `<div>` vide (notre emplacement réservé) et lui ajoutons le tableau construit.

JavaScript n'ajoute pas automatiquement de tableaux. Il ne les crée que parce que nous lui avons dit de le faire. L'appel à `appendChild()` est ce qui l'ajoute réellement au DOM actif.

### Pourquoi cette approche est meilleure

L'utilisation de JavaScript pour générer des tableaux présente plusieurs avantages :

1. **Réutilisabilité :** Vous pouvez réutiliser le même code pour n'importe quel ensemble de données – il suffit de changer le tableau.
    
2. **Séparation des préoccupations :** Les données (JS), la structure (HTML) et le design (CSS) sont tous gérés indépendamment.
    
3. **Performance :** Construire des tableaux en mémoire avant de les ajouter évite les reflows coûteux du DOM.
    
4. **Interactivité :** Vous pouvez facilement ajouter des fonctionnalités telles que le tri, le filtrage ou la mise en évidence des lignes.
    
5. **Données dynamiques :** C'est l'approche naturelle lors de la récupération de données JSON à partir d'API.
    

## Comment ajouter des classes CSS pour le stylisage

Au lieu du stylisage en ligne, nous utiliserons des classes pour une meilleure organisation :

```js
table.classList.add("data-table");
```

Ensuite, nous définirons nos styles en CSS :

```css
.data-table {
  border-collapse: collapse;
  border: 2px solid #333;
  width: 100%;
}

.data-table th, .data-table td {
  border: 1px solid #888;
  padding: 10px;
}
```

Lorsque nous disons « utilisez-les », nous faisons référence aux noms de classes CSS – des identifiants réutilisables qui vous permettent de styliser vos éléments séparément de votre logique JavaScript.

## Comment le transformer en une fonction réutilisable

Enfin, rendons ce processus réutilisable. Nous pouvons tout envelopper dans une fonction qui génère n'importe quel tableau à partir de données et d'en-têtes fournis.

```js
function createTable(data, headers, containerId) {
  const table = document.createElement("table");

  const headerRow = document.createElement("tr");
  headers.forEach(text => {
    const th = document.createElement("th");
    th.textContent = text;
    headerRow.appendChild(th);
  });
  table.appendChild(headerRow);

  data.forEach(item => {
    const row = document.createElement("tr");
    Object.values(item).forEach(value => {
      const td = document.createElement("td");
      td.textContent = value;
      row.appendChild(td);
    });
    table.appendChild(row);
  });

  document.getElementById(containerId).appendChild(table);
}
```

Ensuite, utilisez-la comme ceci :

```js
createTable(data, ["Name", "Age", "Job"], "table-container");
```

### Quand et pourquoi utiliser une fonction

Ce modèle est idéal lorsque vous devez générer plusieurs tableaux sur une seule page, que vous voulez un code plus propre, modulaire et testable, ou que vous prévoyez de l'intégrer à des sources de données dynamiques (comme des API).

## Dernières réflexions et conclusion

Nous avons couvert beaucoup de choses ! Dans cet article, récapitulons ce que vous avez appris :

* Comment créer un tableau avec HTML
    
* Comment le styliser correctement avec CSS
    
* Quand utiliser HTML vs JavaScript
    
* Comment séparer les données de la présentation
    
* Comment générer des tableaux dynamiquement avec JavaScript
    
* Comment rendre votre code réutilisable et efficace
    

Avec ces bases, vous pouvez maintenant construire des tableaux dynamiques, stylisés et pilotés par les données – en utilisant uniquement vanilla JavaScript.

Merci d'avoir lu l'intégralité de cet article. J'espère que vous avez acquis un aperçu de la manière de faire une transition subtile des tableaux HTML typiques vers des tableaux dynamiques basés sur JavaScript. Pour obtenir plus de contenu comme celui-ci, vous pouvez me suivre sur [LinkedIn](https://www.linkedin.com/in/fahimfba/) et [X](https://x.com/Fahim_FBA). Vous pouvez également consulter [mon site web](https://www.fahimbinamin.com/) et me suivre sur [GitHub](https://github.com/FahimFBA) si vous vous intéressez à l'open source et au développement.