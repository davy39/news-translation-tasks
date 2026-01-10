---
title: Comment convertir un tableau HTML statique en une grille de données JavaScript
  dynamique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-18T22:40:00.000Z'
originalURL: https://freecodecamp.org/news/convert-html-table-to-dynamic-javascript-data-grid
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/freecodecamp-html-table-migrate.png
tags:
- name: Datatables
  slug: datatables
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Comment convertir un tableau HTML statique en une grille de données JavaScript
  dynamique
seo_desc: "By Alan Richardson\nHTML Tables are simple to use for rendering small amounts\
  \ of data. But they can be hard for users to work with when they display a lot of\
  \ data. \nFeatures like sorting, filtering, and pagination make it easier to work\
  \ with many rows..."
---

Par Alan Richardson

Les tableaux HTML sont simples à utiliser pour afficher de petites quantités de données. Mais ils peuvent être difficiles à utiliser pour les utilisateurs lorsqu'ils affichent beaucoup de données. 

Des fonctionnalités comme le tri, le filtrage et la pagination facilitent le travail avec de nombreuses lignes de données. Nous pouvons facilement implémenter ces fonctionnalités en migrant d'un tableau HTML vers un composant de grille de données JavaScript.

Dans cet article, nous utiliserons l'édition communautaire gratuite de [AG Grid JavaScript Data Grid](https://www.ag-grid.com/) pour convertir un long tableau HTML statique en une grille de données interactive facile à utiliser. La quantité de JavaScript dont nous avons besoin pour cela est minimale et très simple.

Nous construirons le code d'exemple en trois étapes :

* Afficher une liste statique de données d'éléments Todo dans un tableau HTML.
* Charger une liste d'éléments Todo à partir d'une API REST et les afficher dans le tableau.
* Convertir le tableau HTML en une grille de données pour permettre le tri, le filtrage et la pagination.

## Comment afficher des données avec des tableaux HTML

La première version de notre application nous permettra de créer la structure de base de la page et de nous assurer que nous affichons les bonnes données pour l'utilisateur.

Je crée un simple fichier `index.html` comme montré ci-dessous :

```html
<!DOCTYPE html>
<html>

<head>
    <title>Exemple de tableau</title>
</head>

<body>

    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }

        td,
        th {
            border: 1px solid #000000;
            text-align: left;
            padding: 8px;
        }
    </style>

    <h1>Liste de TODO</h1>

    <div id="data-table">
        <table id="html-data-table">
            <tr>
                <th>userId</th>
                <th>id</th>
                <th>title</th>
                <th>completed</th>
            </tr>
            <tr>
                <td>1</td>
                <td>1</td>
                <td>Mon todo 1</td>
                <td>false</td>
            </tr>
        </table>    
    </div>

</body>

</html>

```

Cela affichera un seul élément Todo dans un tableau.

![Un seul élément Todo affiché dans un tableau HTML](https://www.freecodecamp.org/news/content/images/2022/01/single-todo-item-html-table.png)
_Un seul élément Todo affiché dans un tableau HTML_

Voici l'exemple de [Page de tableau HTML statique](https://eviltester.github.io/freecodecampexamples/html-table-to-data-grid/static-html-table.html).

Le `table` est stylisé pour avoir une largeur de 100 % de la page en utilisant `width:100%` et les lignes de bordure entre les cellules du tableau ont été stylisées pour être affichées comme une seule ligne avec `border-collapse: collapse`.

Sans la valeur `border-collapse`, le tableau ressemblerait à l'image ci-dessous :

![Tableau stylisé sans border-collapse](https://www.freecodecamp.org/news/content/images/2022/01/single-todo-item-html-table-no-border-collapse.png)
_Tableau stylisé sans border-collapse_

## Avantages des tableaux HTML courts

Les tableaux HTML sont un moyen très rapide d'afficher de petites quantités de données sous forme tabulaire sur une page.

Les tableaux nécessitent un stylisme car le style par défaut d'un `table` varie selon les navigateurs et est souvent affiché sans bordures, ce qui rend les données difficiles à lire.

Pour l'instant, notre liste d'éléments Todo est codée statiquement dans la page. Pour l'étape suivante, nous allons `fetch` la liste à partir d'une API REST en utilisant JavaScript.

## Comment lire du JSON à partir d'une API pour l'afficher dans un tableau HTML

Puisque nous allons charger les données à partir d'une API, je ne vais pas coder en dur les données dans le tableau. Pour supporter le chargement dynamique, je supprime simplement la ligne de données du `table` car je vais créer les lignes de données en utilisant JavaScript :

```html
    <div id="data-table">
        <table id="html-data-table">
            <tr>
                <th>userId</th>
                <th>id</th>
                <th>title</th>
                <th>completed</th>
            </tr>
        </table>    
    </div>

```

J'ajouterai le JavaScript dans la page `index.html` immédiatement avant la balise de fermeture `body`.

```html
    <script type="text/javascript" charset="utf-8">
    </script>
</body>

```

Pour commencer, j'écrirai le code qui lit les données.

Je vais utiliser l'application REST API "{JSON} Placeholder" pour cette démonstration. En faisant une requête `GET` sur l'URL [https://jsonplaceholder.typicode.com/todos](https://jsonplaceholder.typicode.com/todos), nous recevrons une réponse JSON qui est une liste d'éléments Todo.

Vous pouvez l'essayer vous-même sans JavaScript en cliquant sur le lien ci-dessus.

Le moyen le plus simple de faire une requête `GET` sur l'API est d'utiliser la fonction `fetch` intégrée à JavaScript.

```html
    <script type="text/javascript" charset="utf-8">

        fetch('https://jsonplaceholder.typicode.com/todos')
            .then(function (response) {
                return response.json();
            }).then(function (apiJsonData) {
                console.log(apiJsonData);
            })

    </script>
</body>

```

Pour expliquer le code ci-dessus, je vais le décrire en sections ci-dessous :

* Émettre une requête GET à `https://jsonplaceholder.typicode.com/todos`

```javascript
fetch('https://jsonplaceholder.typicode.com/todos')

```

* Ensuite, lorsque la requête est terminée, convertir la réponse en un objet JavaScript – dans notre cas, ce sera un tableau contenant tous les éléments Todo.

```javascript
.then(function (response) {
	return response.json();
})

```

* Ensuite, écrire l'objet JavaScript dans la console

```javascript
.then(function (apiJsonData) {
	console.log(apiJsonData);
})

```

Avec ce code dans notre application, nous ne verrons rien dans le tableau, mais nous verrons le tableau rendu dans la console des outils de développement du navigateur où nous pourrons voir les données.

![Données affichées lorsque console.log est utilisé](https://www.freecodecamp.org/news/content/images/2022/01/console-log.png)
_Données affichées lorsque console.log est utilisé_

L'appel à l'API retourne 200 éléments, et chaque élément est un objet Todo :

```json
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  }

```

Notre prochaine étape est d'afficher les données dans le tableau :

```html
    <script type="text/javascript" charset="utf-8">

        fetch('https://jsonplaceholder.typicode.com/todos')
            .then(function (response) {
                return response.json();
            }).then(function (apiJsonData) {
                console.log(apiJsonData);
                renderDataInTheTable(apiJsonData);
            })

        function renderDataInTheTable(todos) {
            const mytable = document.getElementById("html-data-table");
            todos.forEach(todo => {
                let newRow = document.createElement("tr");
                Object.values(todo).forEach((value) => {
                    let cell = document.createElement("td");
                    cell.innerText = value;
                    newRow.appendChild(cell);
                })
                mytable.appendChild(newRow);
            });
        }
    </script>
</body>

```

La fonction `renderDataInTheTable` trouve le tableau dans le DOM afin que nous puissions y ajouter de nouvelles lignes, puis parcourt tous les éléments Todo retournés par l'appel à l'API.

Pour chaque élément Todo, le code crée un nouvel élément `tr`, puis ajoute chaque valeur de l'élément Todo au tableau en tant qu'élément `td`.

```javascript
let newRow = document.createElement("tr");
Object.values(todo).forEach((value) => {
    let cell = document.createElement("td");
    cell.innerText = value;
    newRow.appendChild(cell);
})
```

Lorsque le code `fetch` et `renderDataInTheTable` est ajouté à notre application, et que la page se charge, nous verrons que le tableau HTML contient maintenant tous les 200 éléments Todo rendus dans le tableau.

![Liste de todos chargée dynamiquement](https://www.freecodecamp.org/news/content/images/2022/01/todo-list-200-rows-ez.gif)
_Liste de todos chargée dynamiquement_

Voici l'exemple de [Page de tableau HTML dynamique](https://eviltester.github.io/freecodecampexamples/html-table-to-data-grid/table-index.html).

## Avantages et inconvénients des longs tableaux HTML

Les tableaux HTML sont un moyen facile d'afficher des données sur une page, mais ne sont pas très utilisables pour les longues listes de données.

Les éléments de données peuvent être difficiles à trouver, bien que l'utilisateur puisse rechercher les données en utilisant la fonctionnalité intégrée "trouver dans la page" du navigateur.

En affichant dans un tableau HTML, nos utilisateurs n'ont aucun moyen de trier les données, ou de les filtrer pour n'afficher que les éléments Todo complétés. Nous devrions ajouter du code supplémentaire à notre application pour implémenter les fonctionnalités de tri et de filtrage.

Les tableaux HTML s'agrandiront automatiquement à mesure que des lignes sont ajoutées au tableau. Cela peut les rendre plus difficiles à utiliser dans une application lorsqu'une grande quantité de données a été ajoutée.

Lorsque nous ajoutons beaucoup de données, nous voulons probablement avoir une pagination pour limiter le tableau de données à n'afficher qu'un certain nombre de lignes et permettre à l'utilisateur de cliquer pour passer à la page suivante afin de voir plus d'éléments. Cela, encore une fois, est une fonctionnalité pour laquelle nous devrions écrire du code supplémentaire.

Lorsque notre application atteint le point où nous avons besoin de plus d'interaction utilisateur, nous devrions envisager d'utiliser un composant de grille de données.

Nous pouvons l'utiliser pour ajouter des fonctionnalités supplémentaires comme :

* le tri
* le filtrage
* le redimensionnement des colonnes
* la pagination

## Composants et bibliothèques de grilles de données

Il existe de nombreux composants de grilles de données gratuits, mais la plupart d'entre eux sont spécifiques à un framework, nécessitant donc un codage utilisant soit React, Angular, ou Vue.

J'utilise [AG Grid](https://www.ag-grid.com/) pour cet exemple car la version gratuite peut être utilisée avec JavaScript, TypeScript, React, Angular ou Vue. Le "AG" signifie Agnostic, ce qui signifie qu'il peut être utilisé avec n'importe quel framework.

Lorsque vous apprenez à utiliser AG Grid dans un framework, la même API est disponible pour d'autres frameworks, rendant vos connaissances transférables à d'autres projets.

La version gratuite de AG Grid peut être utilisée dans des applications commerciales, donc si vous parvenez à développer l'application de démonstration montrée ici en une application commerciale de gestion de liste de tâches, vous pourrez toujours utiliser AG Grid gratuitement. De nombreuses applications commerciales ont été construites en utilisant la version gratuite de AG Grid.

De plus, AG Grid est souvent recherché comme compétence dans les offres d'emploi, il vaut donc la peine de l'expérimenter.

La version commerciale de AG Grid dispose de fonctionnalités supplémentaires comme l'exportation vers Excel et la création de graphiques, mais nous n'avons pas besoin de ces fonctionnalités dans cette démonstration.

L'utilisation d'une grille de données signifie que nous configurons la grille de données, lui donnons les données à afficher, et la grille gère toutes les autres fonctionnalités comme le tri, le filtrage et la pagination.

Nous pouvons convertir notre code existant pour utiliser AG Grid avec seulement quelques changements.

## Comment ajouter AG Grid JavaScript et CSS

AG Grid est une bibliothèque, nous allons donc inclure le JavaScript requis.

Si vous utilisez des outils de construction comme `npm`, alors diverses commandes `npm install` sont listées dans la [documentation Getting Started with AG Grid](https://file+.vscode-resource.vscode-webview.net/Users/alan/Documents/GitHub/alan/freecodecampexamples/docs/html-table-to-data-grid/readme.md).

Nous utilisons du JavaScript simple, nous pouvons donc inclure le `script` dans notre section `head`.

```html
<head>
    <title>Exemple de grille de données</title>
    <script src="https://unpkg.com/ag-grid-community/dist/ag-grid-community.min.noStyle.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/ag-grid-community/dist/styles/ag-grid.css">
    <link rel="stylesheet" href="https://unpkg.com/ag-grid-community/dist/styles/ag-theme-balham.css">
</head>

```

Cela inclut l'édition communautaire de AG Grid et le CSS requis pour afficher correctement la grille.

Notre `div` `data-table` n'a plus besoin d'avoir d'élément `table` :

```html
    <div id="data-table" class="ag-theme-balham">
    </div>

```

AG Grid créera le HTML pour la grille de données lorsque nous la configurerons. Nous ajoutons la `class` pour utiliser un [thème AG Grid](https://www.ag-grid.com/javascript-data-grid/themes/). Dans cet exemple, nous utilisons le thème `ag-theme-balham`.

AG Grid nécessite de définir une largeur et une hauteur pour le `div`. J'ai choisi d'ajouter cela dans la section `style` du code :

```html
    <style>
        #data-table {
            height: 500px;
            width: 100%;
        }
    </style>

```

La grille sera affichée avec une hauteur de 500 pixels et remplira `100%` de la largeur de l'écran. Cela reproduit le style de base que nous avions avec le tableau HTML. Mais cela montre également l'un des avantages de l'utilisation d'une grille de données. La taille du tableau rendu peut être facilement contrôlée et des barres de défilement seront ajoutées automatiquement si nécessaire par la grille elle-même.

## Comment configurer AG Grid et afficher des données

La section `script` du code change car nous devons :

* Configurer la grille de données.
* Créer une nouvelle grille de données en utilisant la configuration.
* Récupérer les données et les ajouter à la grille.

Je vais montrer la section `script` initiale modifiée ci-dessous et l'expliquer dans les paragraphes suivants.

```html
    <script type="text/javascript" charset="utf-8">

        const columnDefs = [
            { field: 'userId' },
            { field: 'id' },
            { field: 'title' },
            { field: 'completed' },
        ];

        const gridOptions = {
            columnDefs: columnDefs,
            onGridReady: (event) =>{renderDataInTheTable(event.api)}
        };

        const eGridDiv = document.getElementById('data-table');
        new agGrid.Grid(eGridDiv, gridOptions);

        function renderDataInTheTable(api) {
            fetch('https://jsonplaceholder.typicode.com/todos')
                .then(function (response) {
                    return response.json();
                }).then(function (data) {
                    api.setRowData(data);
                    api.sizeColumnsToFit();
                })
        }
    </script>

```

Une grille de données est pilotée par les données et la configuration – nous n'avons pas besoin d'écrire beaucoup de code pour créer une grille de données fonctionnelle.

Tout d'abord, nous créons un tableau d'objets de colonnes qui définissent les colonnes dans la grille de données. Ces colonnes correspondent aux données.

Les données que nous recevons de l'appel à l'API ont quatre propriétés : "userId", "id", "title" et "completed" :

```json
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  }

```

Pour les afficher dans la grille de données en tant que colonnes, nous créons un objet avec une propriété `field` où la valeur est le nom de la propriété dans l'objet de données.

```javascript
        const columnDefs = [
            { field: 'userId' },
            { field: 'id' },
            { field: 'title' },
            { field: 'completed' },
        ];

```

Ensuite, nous créons l'objet `gridOptions`. Cela configure la grille de données :

```javascript
        const gridOptions = {
            columnDefs: columnDefs,
            onGridReady: (event) =>{renderDataInTheTable(event.api)}
        };

```

La propriété `columnDefs` est assignée au tableau d'objets de colonnes que nous avons définis précédemment.

La propriété `onGridReady` est assignée à une fonction qui appellera la fonction `renderDataInTheTable` lorsque la grille aura été créée et rendue dans le DOM (c'est-à-dire lorsque la grille est prête).

Pour ajouter la grille à la page, nous trouvons l'élément `div` qui contiendra la grille, puis nous instancions un nouvel objet AG Grid pour cet élément et avec les options que nous avons configurées :

```javascript
        const eGridDiv = document.getElementById('data-table');
        new agGrid.Grid(eGridDiv, gridOptions);

```

La fonction pour récupérer les données et les afficher dans la grille est presque la même que le code `fetch` que nous avons utilisé pour le tableau HTML dynamique. La différence est que la fonction `renderDataInTheTable` reçoit un objet Api AG Grid en tant que paramètre, ce qui nous permet d'appeler la fonctionnalité AG Grid pour définir les données de ligne et ajuster la taille des colonnes à la grille :

```javascript
        function renderDataInTheTable(api) {
            fetch('https://jsonplaceholder.typicode.com/todos')
                .then(function (response) {
                    return response.json();
                }).then(function (data) {
                    api.setRowData(data);
                    api.sizeColumnsToFit();
                })
        }

```

Lorsque ce code s'exécute, nous aurons essentiellement répliqué la même fonctionnalité du tableau HTML dynamique, mais maintenant toutes les données sont affichées dans une grille de données avec une barre de défilement.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/initial-data-grid.png)

Pour bénéficier de l'utilisation d'une grille de données et permettre à l'utilisateur de trier, filtrer et naviguer dans les données, nous devons simplement modifier la configuration.

## Comment implémenter le tri, le filtrage et la pagination

Voici ce que nous avons configuré dans la grille de données jusqu'à présent :

* quels champs des données afficher
* quelles données utiliser

Pour ajouter le tri, le filtrage, le redimensionnement des colonnes et la pagination, nous modifions la configuration `gridOptions` :

```javascript
        const gridOptions = {

            defaultColDef: {
                sortable: true,
                filter: 'agTextColumnFilter',
                resizable: true
            },

            pagination: true,

            columnDefs: columnDefs,
            onGridReady: (event) =>{renderDataInTheTable(event.api)}
        };

```

Nous pouvons configurer les colonnes dans AG Grid individuellement en ajoutant des propriétés supplémentaires aux objets `columnDefs`. Ou si la même fonctionnalité est requise par défaut dans toutes les colonnes, nous pouvons configurer le `defaultColDef`.

Ici, nous le configurons pour qu'il soit triable, filtrable et redimensionnable :

```javascript
            defaultColDef: {
                sortable: true,
                filter: 'agTextColumnFilter',
                resizable: true
            },

```

Le filtre par défaut que nous avons défini pour toutes les colonnes est le filtre de texte.

Pour ajouter une pagination automatique à la grille, nous ajoutons la propriété `pagination: true` et AG Grid paginera automatiquement les données pour nous.

![Grille de données avec tri, filtrage et pagination](https://www.freecodecamp.org/news/content/images/2022/01/sorting-pagination-ez.gif)
_Grille de données avec tri, filtrage et pagination_

## Grille de données conviviale

Avec le code ci-dessus, nous avons créé une grille de données conviviale qui récupère dynamiquement les données et les ajoute à une grille de données qui supporte le tri, le filtrage et la pagination.

Voici l'exemple de [Page HTML de grille de données](https://eviltester.github.io/freecodecampexamples/html-table-to-data-grid/datagrid-index.html) :

```html
<!DOCTYPE html>
<html>

<head>
    <title>Exemple de grille de données</title>
    <script src="https://unpkg.com/ag-grid-community/dist/ag-grid-community.min.noStyle.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/ag-grid-community/dist/styles/ag-grid.css">
    <link rel="stylesheet" href="https://unpkg.com/ag-grid-community/dist/styles/ag-theme-balham.css">
</head>

<body>
    <style>
        #data-table {
            height: 500px;
            width: 100%;
        }
    </style>

    <h1>Liste de TODO</h1>

    <div id="data-table" class="ag-theme-balham">
    </div>

    <script type="text/javascript" charset="utf-8">

        const columnDefs = [
            { field: 'userId' },
            { field: 'id' },
            { field: 'title' },
            { field: 'completed' },
        ];

        const gridOptions = {

            defaultColDef: {
                sortable: true,
                filter: 'agTextColumnFilter',
                resizable: true
            },

            pagination: true,
            
            columnDefs: columnDefs,
            onGridReady: (event) =>{renderDataInTheTable(event.api)}
        };

        const eGridDiv = document.getElementById('data-table');

        new agGrid.Grid(eGridDiv, gridOptions);

        function renderDataInTheTable(api) {
            fetch('https://jsonplaceholder.typicode.com/todos')
                .then(function (response) {
                    return response.json();
                }).then(function (data) {
                    api.setRowData(data);
                    api.sizeColumnsToFit();
                })
        }
    </script>
</body>
</html>

```

## Filtres numériques

Puisque les colonnes `userId` et `id` sont numériques, nous pourrions les faire utiliser un filtre numérique en modifiant les `columnDefs` :

```javascript
        const columnDefs = [
            { field: 'userId', filter: 'agNumberColumnFilter'},
            { field: 'id', filter: 'agNumberColumnFilter'},
            { field: 'title' },
            { field: 'completed' },
        ];

```

Voici l'exemple de [Page HTML de grille de données avec filtres numériques](https://eviltester.github.io/freecodecampexamples/html-table-to-data-grid/datagrid-number-filters-index.html).

Il existe de nombreuses [options de configuration pour les colonnes](https://www.ag-grid.com/javascript-data-grid/column-properties/) listées dans la documentation AG Grid, par exemple la configuration de la largeur, du style et la possibilité de rendre les cellules éditables.

## Avantages d'une grille de données

Pour de nombreux sites web, un simple tableau HTML sera un moyen parfaitement sensé d'afficher des données tabulaires. C'est rapide et facile à comprendre, et avec un peu de CSS, le tableau peut avoir une belle apparence pour vos utilisateurs.

Lorsque vos pages deviennent plus complexes, affichent plus de données ou nécessitent plus d'interactivité pour l'utilisateur, il commence à être plus judicieux d'utiliser un composant ou une bibliothèque de grille de données.

Les grilles de données fournissent une grande partie de la fonctionnalité dont vos utilisateurs ont besoin, sans avoir à écrire beaucoup de code. Dans l'exemple présenté dans cet article, nous sommes passés d'un tableau dynamique qui lisait les données à partir d'une API, à une grille de données lisant à partir d'une API avec tri, filtrage, pagination et redimensionnement des colonnes. 

C'est beaucoup de fonctionnalités supplémentaires, mais notre code HTML était de la même longueur et le JavaScript que nous avons ajouté était moins compliqué car la grille de données a fait tout le travail de rendu des données.

Les grilles de données peuvent gérer des centaines de milliers de lignes et se mettre à jour rapidement, elles sont donc souvent utilisées dans les systèmes de trading financier en temps réel avec des prix dans les cellules se mettant à jour toutes les quelques millisecondes.

Si vous utilisez React, alors en plus de [AG Grid](https://www.ag-grid.com/react-data-grid/), vous pourriez regarder [Material UI](https://mui.com/components/data-grid/) ou [React Table](https://react-table.tanstack.com/). React Table est un 'tableau' plutôt qu'une grille de données, il nécessite donc un peu plus de code initialement pour rendre le tableau.

Material UI et React Table sont uniquement disponibles pour React. AG Grid est agnostique et fonctionnera avec JavaScript, TypeScript, React, Angular et Vue.

Le code source de cet article peut être [trouvé dans ce dépôt Github](https://github.com/eviltester/freecodecampexamples) dans le dossier [docs/html-table-to-data-grid](https://github.com/eviltester/freecodecampexamples/tree/main/docs/html-table-to-data-grid).