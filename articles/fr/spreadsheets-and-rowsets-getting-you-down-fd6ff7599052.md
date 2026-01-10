---
title: Les tableaux vous dépriment ? Convertir les données de lignes en arbres JSON
  est un jeu d'enfant.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-30T05:41:28.000Z'
originalURL: https://freecodecamp.org/news/spreadsheets-and-rowsets-getting-you-down-fd6ff7599052
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5Yrv4yG9LUeSmYrvZ_ZUMQ.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: SQL
  slug: sql
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Les tableaux vous dépriment ? Convertir les données de lignes en arbres
  JSON est un jeu d'enfant.
seo_desc: 'By Jeff M Lowery

  Like many of you, I often have to take the result of SQL queries and convert the
  rowsets to JSON data objects. Sometimes I have to do the same with CSV files from
  spreadsheets. The transformation process can be a hassle, though anyon...'
---

Par Jeff M Lowery

Comme beaucoup d'entre vous, je dois souvent prendre le résultat de [requêtes SQL](http://www.sqlcourse.com/intro.html) et convertir les jeux de résultats en [objets de données JSON](http://www.json.org/). Parfois, je dois faire de même avec des fichiers CSV provenant de tableaux. Le processus de transformation peut être fastidieux, bien que tout le monde puisse le faire. Pourtant, cela peut être chronophage et sujet aux erreurs. Cet article vous montrera comment utiliser le package Node.js [**treeize**](https://www.npmjs.com/package/treeize) pour simplifier le processus en très peu de lignes de code.

Avant d'aller plus loin, j'aurai d'abord besoin d'un jeu de données pour baser quelques exemples. Le domaine sera **Les Livres**, qui se prêtent à toutes sortes de catégorisation. J'utiliserai un générateur de données fictives appelé [casual](https://github.com/boo1ean/casual), que j'ai précédemment utilisé pour des mocks dans mon article sur [les tests GraphQL](https://medium.freecodecamp.org/mocking-graphql-with-graphql-tools-42c2dd9d0364).

Les données des livres auront la structure suivante :

```js
casual.define('book', () => {
    const author = casual.random_element(authors);
    
const book = {
        first_name: author.first,
        last_name: author.last,
        title: casual.random_element(author.titles),
        category: casual.random_element(author.category)
    }

return book;
});
```

Chaque fois que je demande un `casual.book`, j'obtiens un livre avec un nouvel ensemble de valeurs. Ce n'est pas entièrement aléatoire. Le générateur utilise certaines [données prédéfinies](https://github.com/JeffML/rowsets2json/blob/master/src/mocks/index.js) pour des auteurs bien connus, et des données plus ou moins générées aléatoirement pour d'autres auteurs. Voici un exemple :

```json
{ dataset:
   [ { first_name: 'Barbara',
       last_name: 'Cartland',
       title: 'The Pirate and the Piano Teacher',
       category: 'thriller' },
     { first_name: 'Carlie',
       last_name: 'Haley',
       title: 'Digitized Global Orchestration',
       category: 'engineering' },
     { first_name: 'Arthur',
       last_name: 'Doyle',
       title: 'The Case of the Spotted Dick',
       category: 'mystery' },
     { first_name: 'Reinhold',
       last_name: 'Gutmann',
       title: 'Managed Directional Benchmark',
       category: 'management' },
     { first_name: 'Isaac',
       last_name: 'Asimov',
       title: 'Once in a Venusian Sun',
       category: 'science fiction' },
     { first_name: 'R. L.',
       last_name: 'Stein',
       title: 'Why are You Scared of Me?',
       category: 'childrens books' },
     { first_name: 'Alicia',
       last_name: 'Cruickshank',
       title: 'Balanced Local Database',
       category: 'engineering' },
     { first_name: 'Chase',
       last_name: 'Runte',
       title: 'Ergonomic Tertiary Solution',
       category: 'engineering' } ] }
```

Si vous êtes intéressé par la manière dont ces données ont été générées, le code source complet utilisé dans cet article peut être trouvé [ici](https://github.com/JeffML/rowsets2json). Pour un peu plus de réalisme, ces données générées seront insérées dans une [base de données SQL en mémoire](https://www.npmjs.com/package/alasql) pour une récupération ultérieure. Voici le format des résultats pour la requête SQL :

```sql
SELECT title, category, first_name, last_name
FROM book
JOIN author ON author.id = book.author
```

Ce format est, à toutes fins utiles, identique au format du **dataset** montré juste précédemment, par exemple :

```json
[ { title: 'Proactive Regional Forecast',
    category: 'mystery',
    first_name: 'Arthur',
    last_name: 'Doyle' },
  { title: 'More Scary Stuff',
    category: 'suspense',
    first_name: 'Steven',
    last_name: 'King' },
  { title: 'Scary Stuff',
    category: 'occult',
    first_name: 'Steven',
    last_name: 'King' },
  { title: 'Persistent Neutral Info Mediaries',
    category: 'management',
    first_name: 'Maegan',
    last_name: 'Frami' },
  { title: 'Enhanced Background Frame',
    category: 'engineering',
    first_name: 'Winifred',
    last_name: 'Turner' },...
```

La principale différence entre le dataset et le jeu de résultats est que lors du peuplement de la base de données à partir des données générées par casual, j'ai éliminé les auteurs en double (par nom) et les titres de livres en double (par catégorie) :

```js
const addEntities = (dataset) => {
    dataset.forEach(d => {
        d.title = d.title.replace(/'/, "''")

        const stmt =
            `
            IF NOT EXISTS (
                select * from author
                where first_name = '${d.first_name}'
                and last_name = '${d.last_name}')
            INSERT INTO author (first_name, last_name) VALUES('${d.first_name}', '${d.last_name}');
            IF NOT EXISTS (
                select * from book
                where title = '${d.title}'
                and category = '${d.category}')
            INSERT INTO book (title, category, author) VALUES('${d.title}', '${d.category}',
            (select id from author where first_name ='${d.first_name}' and last_name = '${d.last_name}'))
            `
        try {
            alasql(stmt)
        } catch (e) {
            console.error(stmt);
            throw (e);
        }

    })
};
```

### Conversion en JSON

![Image](https://cdn-media-1.freecodecamp.org/images/5eHzM7anyF1JlIGM11bcKtslW6D1MVQ2b66g)
_Image gratuite de chaton._

Vous pourriez remarquer que les résultats du dataset étaient déjà au format JSON. Ce que cet article vise, cependant, est de construire une hiérarchie de contenu qui montre les relations entre les auteurs, les livres et les catégories de manière concise. Ce n'est pas le cas avec les valeurs du jeu de résultats, où les résultats sont des paires clé-valeur glorifiées, où chaque paire est un nom de colonne et une valeur d'une ligne de tableau.

Donc, par exemple, disons que je veux lister les auteurs, les catégories dans lesquelles ils écrivent, et les titres des livres dans ces catégories qu'ils ont écrits. Je veux montrer chaque catégorie une seule fois, et chaque livre dans chaque catégorie doit également être listé une seule fois.

C'est un type de réduction assez courant qui est souvent appliqué aux données de jeux de résultats. Une façon de résoudre le problème est de déclarer un objet conteneur, puis de le remplir en parcourant les jeux de résultats. Une implémentation typique pourrait être :

```js
const handrolled = (rs) => {
    const authors = {}

    rs.forEach(r => {
        const authname = [r.last_name, r.first_name].join(',');
        if (!authors[authname]) {
            authors[authname] = {
                categories: {}
            }
        }
        var author = authors[authname];
        if (!author.categories[r.category]) {
            author.categories[r.category] = {
                titles: []
            }
        }
        var category = author.categories[r.category]
        if (!category.titles.includes(r.title)) {
            category.titles.push(r.title)
        }
    })

    return authors;
}
```

La méthode `handrolled()` devient un peu compliquée plus la hiérarchie est profonde. Des variables locales sont utilisées pour réduire les longueurs de chemin. Nous devons garder la méta-structure à l'esprit pour écrire les initialisations appropriées des propriétés dans l'objet JSON. Que pourrait-il y avoir de plus simple ?

Les résultats retournés sont :

```json
...
        "Doyle,Arthur": {
            "categories": {
                "thriller": {
                    "titles": [
                        "The Case of the Spotted Dick",
                        "The Case of the Mashed Potato"
                    ]
                },
                "mystery": {
                    "titles": [
                        "The Case of the Spotted Dick"
                    ]
                }
            }
        },
        "Asimov,Isaac": {
            "categories": {
                "science": {
                    "titles": [
                        "Once in a Venusian Sun",
                        "Total Multi Tasking Forecast"
                    ]
                },
                "general interest": {
                    "titles": [
                        "Total Multi Tasking Forecast",
                        "Once in a Venusian Sun",
                        "Fourth Foundation"
                    ]
                }
            }
        },
        "Kilback,Bradley": {
            "categories": {
                "management": {
                    "titles": [
                        "Mandatory Solution Oriented Leverage"
                    ]
                },
                "engineering": {
                    "titles": [
                        "Multi Layered Fresh Thinking Framework",
                        "Total Scalable Neural Net",
                        "Mandatory Solution Oriented Leverage"
                    ]
                },
                "reference": {
                    "titles": [
                        "Multi Layered Fresh Thinking Framework"
                    ]
                }
            }
        },...
```

### Construire un arbre avec Treeize

Le module npm treeize est conçu pour simplifier la conversion des jeux de résultats en données JSON structurées grâce à l'utilisation de clés descriptives. L'installation via npm est standard :

```bash
npm install --save treeize
```

#### Jeux de résultats JSON

Treeize est capable de reconnaître les motifs récurrents dans les jeux de résultats. Il les transforme selon la manière dont les noms de clés sont définis dans les métadonnées passées en tant que structure de base. Voici le code :

```js
import Treeize from 'treeize'

const treeized = rs => {
    var authors = new Treeize();

    const seed = rs.map(r => ({
        name: [r.last_name, r.first_name].join(', '),
        'categories:type': r.category,
        'categories:titles:name': r.title
    }))

    authors.grow(seed);
    return authors.getData();
}
```

Cela représente environ une douzaine de lignes de code contre le double pour la version manuelle. Remarquez les valeurs de clés utilisées dans l'opération de mappage. Treeize reconnaît les pluriels comme des collections, donc `categories` et `titles` seront des tableaux. Les deux-points (:) dans les noms indiquent une imbrication. `Type` sera une propriété d'un objet dans le tableau des catégories, et `name` sera une propriété dans tous les objets des titres.

L'arbre est construit lorsque `authors.grow(seed)` est appelé, et les résultats sont récupérés via `authors.getData()`. Cependant, cela ne donne pas tout à fait les mêmes résultats que ce que nous avions avec la méthode manuelle :

```json
...,
{
    "name": "Glover, Ashley",
    "categories": [
        {
            "type": "engineering",
            "titles": [
                {
                    "name": "Intuitive Full Range Capacity"
                },
                {
                    "name": "Organic Encompassing Core"
                }
            ]
        },
        {
            "type": "reference",
            "titles": [
                {
                    "name": "Distributed Client Server Service Desk"
                },
                {
                    "name": "Organic Encompassing Core"
                }
            ]
        },
        {
            "type": "management",
            "titles": [
                {
                    "name": "Organic Encompassing Core"
                }
            ]
        }
    ]
},...
```

Une différence notable est que les catégories ne sont pas des objets nommés (comme avant), mais des objets avec une propriété `name`. `Title` n'est également pas simplement un tableau de chaînes, mais un tableau d'objets avec `name` comme titre. Treeize interprète `categories` et `titles` comme des tableaux d'objets, et non comme des maps (ou des tableaux de primitives). Pour la plupart des cas d'utilisation, ce n'est pas un gros problème. Mais, si vous devez trouver une catégorie par nom rapidement (plutôt que de parcourir un tableau de catégories), alors vous pouvez vous en occuper [via un couple d'opérations de réduction](https://gist.github.com/JeffML/1bbe228f271765d3ee3a917196e8a81c) pour arriver à la même structure qu'avant :

```json
,...   
    "Doyle, Arthur": {
        "categories": {
            "mystery": {
                "titles": [
                    "The Case of the Spotted Dick",
                    "Pre Emptive Needs Based Approach",
                    "The Case of the Mashed Potato"
                ]
            },
            "thriller": {
                "titles": [
                    "The Case of the Mashed Potato",
                    "The Pound Puppies of the Baskervilles"
                ]
            }
        }
    },...
```

#### Tableurs

Parfois, les données proviennent de tableurs plutôt que de bases de données relationnelles. Treeize est également capable de gérer ce cas. Au lieu d'utiliser des clés descriptives comme nous l'avons fait avec les données de jeux de résultats au format JSON, le même format descriptif est utilisé comme valeurs de colonne dans une ligne d'en-tête :

```js
var seed = [
['name', 'categories:type', 'categories:titles:name'], 
['Doyle, Arthur', 'mystery', 'The Adventure of the Gyring Gerbils'],
['Schuppe, Katarina', 'engineering', 'Configurable Discrete Locks'],
['Doyle, Arthur', 'mystery', 'Holmes Alone 2'],
['Asimov, Isaac', 'science fiction', 'A Crack in the Foundation']
];

// même chose qu'avant...
var authors = new Treeize();
authors.grow(seed);
return authors.getData();
```

Il existe [de nombreuses options](https://www.npmjs.com/package/treeize#1-getset-options-optional) que treeize supporte, et je n'ai montré que les bases. C'est un outil puissant qui facilite la transformation des structures de données basées sur des lignes.

Le code source complet [peut être trouvé sur mon GitHub](https://github.com/JeffML/rowsets2json).