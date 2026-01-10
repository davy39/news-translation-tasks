---
title: Comment utiliser des données de fichier plat dans une application Nuxt statique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-19T18:33:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-flat-file-data-in-a-static-nuxt-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/flat_file_db.jpg
tags:
- name: database
  slug: database
- name: JavaScript
  slug: javascript
- name: Nuxt.js
  slug: nuxtjs
seo_title: Comment utiliser des données de fichier plat dans une application Nuxt
  statique
seo_desc: 'By Anthony Gore

  Making your Nuxt web app static can potentially save you the time and money of setting
  up a server-rendered app. It may also offer superior performance.

  But what if your app needs dynamic data? The most popular solution is to set up
  a...'
---

Par Anthony Gore

Rendre votre application web Nuxt statique peut potentiellement vous faire économiser du temps et de l'argent en évitant de configurer une application rendue côté serveur. Cela peut également offrir des performances supérieures.

Mais que faire si votre application a besoin de données dynamiques ? La solution la plus populaire consiste à configurer une API aux côtés de votre application statique qui peut fournir des données dynamiques via AJAX.

Dans cet article, je vais vous montrer une autre architecture possible - l'utilisation d'une base de données de fichier plat. Cette architecture pourrait vous éviter la difficulté de configurer une API et offre des performances supérieures.

## Qu'est-ce qu'une base de données de fichier plat ?

Une "base de données de fichier plat" est une architecture de base de données où les données sont stockées dans un simple fichier texte plutôt que dans un logiciel de base de données comme MySQL ou MongoDB.

Dans une application Nuxt, ce fichier peut être un fichier JSON qui se trouve dans votre répertoire de fichiers statiques et est déployé aux côtés des fichiers de balisage.

À l'exécution, le fichier JSON est chargé par l'application Nuxt. Une fois les données analysées en tant que données JavaScript, elles peuvent être utilisées pour alimenter l'application.

## Pourquoi utiliser une base de données de fichier plat ?

Les bases de données de fichier plat sont avantageuses en raison de leur simplicité et de leur faible surcharge. Mais elles sont également non sécurisées et n'offrent pas les avantages de performance des logiciels de base de données conventionnels, c'est pourquoi elles sont rarement utilisées.

Dans le contexte des applications Nuxt, cependant, elles ont un autre grand avantage - elles peuvent être stockées et accessibles à partir d'un hébergement statique.

L'utilisation d'une base de données de fichier plat peut également avoir un avantage de performance par rapport à un service API qui aura une petite surcharge de latence encourue lorsque les requêtes sont traitées par le serveur.

Cependant, les bases de données de fichier plat ne seront pas toujours appropriées à utiliser, car elles n'offrent aucune sécurité et sont en lecture seule en production. Cela signifie que vous devrez reconstruire le site chaque fois que vous souhaitez écrire de nouvelles données.

Un type de données qui est un bon candidat pour le stockage et la récupération de fichiers plats est les métadonnées. Par exemple, sur le [blog Vue.js Developers](https://vuejsdevelopers.com/), que j'ai construit avec Nuxt, j'utilise une base de données de fichier plat pour stocker les métadonnées sur les articles publiés.

Cela me permet d'accéder facilement à ces données à travers le site, par exemple sur la page d'accueil où les derniers articles de blog sont affichés, et sur la page des sujets qui indexe les articles en fonction des balises de sujet appliquées (les deux sont montrés ci-dessous).

![Vue.js Developers Blog](https://s3.us-east-2.amazonaws.com/downloads.vuejsdevelopers.com/flat_file_db_image_1.png)

## Mise en œuvre de l'architecture de base de données de fichier plat dans Nuxt

Maintenant, voyons comment implémenter l'architecture de base de données de fichier plat dans votre propre site Nuxt.

Disons que nous voulons créer une page d'accueil de blog qui montre le dernier article publié comme celui sur le blog Vue.js Developers.

Nous commencerons par voir comment les données provenant de fichiers plats sont utilisées dans la page, puis nous travaillerons à rebours jusqu'à ce que nous puissions voir comment l'architecture complète fonctionne.

### Utilisation des données de fichier plat dans une page

Dans notre composant de page d'accueil, _pages/index.vue_, nous importerons `getArticleSummaries` d'un module JavaScript bientôt créé `flatFileDb`.

Cette méthode retournera une promesse contenant les données de résumé d'article prêtes à être utilisées sur la page.

Vous pouvez, bien sûr, utiliser ces données au moment de la construction via `asyncData`, et au moment de l'exécution via le hook `created`.

_pages/index.vue_:

```js
const { getArticleSummaries } from "@/assets/js/flatFileDb";

export default {
    data: () => ({
        articleSummaries: []
    }),
    async asyncData () {
        const articleSummaries = await getArticleSummaries();
        return { articleSummaries }
    },
    async created () {
        this.articleSummaries = await getArticleSummaries();
    }
}

```

Notez que la structure de données que nous obtiendrons de `getArticleSummaries` sera un tableau d'objets comme ceci :

```js
[
    {
        title: "...",
        description: "...",
        published: "...",
        ...
    },
    ...
]

```

Remarque : Si vous avez plusieurs entités (par exemple, en plus des articles, vous stockez également des informations sur les vidéos), chacune aura son propre fichier plat et sa propre méthode de récupération dans l'application, comme `getVideoSummaries`.

### Module de base de données de fichier plat

Nous avons vu ci-dessus qu'une méthode `getArticleSummary` était importée du module `flatFileDb`. Voyons comment nous pouvons l'implémenter.

Notre base de données de fichier plat sera incluse dans nos fichiers statiques et devrait être un fichier JSON puisque ceux-ci sont simples à analyser en tant que données JavaScript valides.

Nous inclurons ce fichier JSON en utilisant une importation dynamique. Cette fonctionnalité est conçue pour importer des modules JavaScript, mais elle fonctionne avec les fichiers JSON directement avec Webpack. De manière pratique, vous obtenez le fichier JSON déjà analysé en tant que JavaScript.

Il est important d'appeler l'importation dynamique dans un bloc `try/catch` pour éviter que l'application ne plante si le fichier est manquant ou si l'analyse JSON échoue.

Avant de retourner les données au composant consommateur, nous devons les "décoder" avec une autre méthode personnalisée `decodeArticleSummaries`. Je vais expliquer cela dans un instant.

Enfin, notez qu'un fichier JSON n'a pas d'exportation par défaut, vous devrez donc accéder à la propriété `default` du module de base de données pour accéder aux données.

_assets/js/flatFileDb.js_:

```js
import { decodeArticleSummaries } from "dbDecoders";

const getArticleSummaries = async () => {
    try {
    const db = await import(`@/static/article-summaries.json`);
    return decodeArticleSummaries(db.default);
  } catch (err) {
    console.log(err);
    return [];
  }
};

export { getArticleSummaries };

```

### Décodage de la base de données

Plus haut, j'ai dit que les données fournies au composant ressembleraient à ceci :

```
{
    title: "...",
    description: "...",
    published: "...",
    // etc
}

```

Cependant, elles ne devraient pas être stockées dans la base de données comme ceci car les noms de propriété sont inutilement longs.

Afin de garder le fichier plat aussi léger que possible, nous devrions "encoder" chaque clé lorsque la base de données est créée. Ensuite, nous devrions les décoder avant qu'elles ne soient consommées par les composants afin qu'elles aient leurs noms complets disponibles pour le développeur.

Donc, disons que nous faisons "title" => "t", "description" => "d", et "published" => "p". Dans une grande base de données, cette transformation pourrait réduire la taille du fichier de nombreux octets.

_assets/js/dbDecode.js_:

```js
const decodeArticleSummaries = db => {
    return db.map(article => ({
        title: article.t,
        description: article.d,
        published: article.p
        // etc
    }));
}

```

## Génération de la base de données de fichier plat

Maintenant que nous avons vu comment la base de données de fichier plat est consommée à l'exécution. Comment est-elle créée ?

Vous pourriez créer une base de données de fichier plat manuellement à la main, mais généralement vous voudrez la générer au moment de la construction avec un script Node.js.

Dans notre exemple, nous voudrons faire un script qui extrait les métadonnées de chaque article et les stocke sous _static/article-summaries.json_. Supposons que les articles sont stockés sous forme de markdown et se trouvent dans un répertoire "articles" à la racine du projet.

Les détails du script seront spécifiques à votre implémentation, donc je vais juste vous donner un pseudo-code pour communiquer l'idée de base.

_scripts/generateDb.js_:

```js
const fs = require("fs");
const frontmatterExtractor = require("./frontmatterExtractor");
const encodeArticleSummaries = require("./encodeArticleSummaries");

module.exports = async () => {
    // Charger les fichiers d'articles
    const articles = await fs.readdir("/articles", (err, filePaths) => {
        // Créer la base de données en lisant chaque fichier
        const db = filePaths.map(async path => {
            const file = await fs.readFile(path);
            // Extraire les métadonnées
            return frontmatterExtractor(file);
        });
        // Encoder les données
        const encoded = encodeArticleSummaries(db);
        // Écrire l'objet de base de données dans un fichier JSON
        await fs.writeFile(
            "/static/article-summaries.json", 
            JSON.stringify(encoded)
        );
    });
}

```

## Exécution du script de génération de la base de données avant la construction du site

Maintenant que nous avons un script de génération de base de données, déclenchons-le pour qu'il s'exécute juste avant les processus de construction (ou de génération) qui voudront le consommer.

Pour ce faire, nous allons l'intégrer dans les commandes NPM dans _package.json_. Notez qu'en utilisant l'opérateur `&&` nous pouvons nous assurer que le processus Nuxt ne commence pas avant que le script de génération ne soit terminé.

_package.json_:

```json
{
    ...
    "scripts": {
        ...
        "build": "node scripts/generateDb && nuxt build",
        "generate": "node scripts/generateDb && nuxt generate",
        ...
    }
    ...
}

```

En développement, cependant, je trouve plus facile de générer manuellement la base de données sur la ligne de commande chaque fois que je dois la mettre à jour :

```
$ node scripts/generateDb

```

## Lectures complémentaires

C'est l'architecture de base expliquée. Voici quelques autres articles pour en apprendre plus :

* [Going JAMstack with Netlify and Nuxt](https://blog.lichter.io/posts/jamstack-nuxt-netlify/)
* [Multiple Ways of API Integration in your JAMStack](https://www.raymondcamden.com/2019/07/25/multiple-ways-of-api-integration-in-your-jamstack)
* [Including Markdown Content in a Vue or Nuxt SPA](https://vuejsdevelopers.com/2018/12/31/vue-nuxt-spa-markdown/)