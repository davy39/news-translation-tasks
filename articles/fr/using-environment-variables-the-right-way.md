---
title: Comment utiliser les variables d'environnement de la bonne manière
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-02T18:27:57.000Z'
originalURL: https://freecodecamp.org/news/using-environment-variables-the-right-way
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/cover.jpg
tags:
- name: Application Security
  slug: application-security
- name: clean code
  slug: clean-code
- name: Code Quality
  slug: code-quality
seo_title: Comment utiliser les variables d'environnement de la bonne manière
seo_desc: "By Stanley Nguyen\nEnvironment variables are one of the foundational concepts\
  \ for application developers. And they're something we use on a daily basis. \n\
  Environment variables have even claimed a part in the de-facto twelve-factor app.\
  \ They have a lon..."
---

Par Stanley Nguyen

Les variables d'environnement sont l'un des concepts fondamentaux pour les développeurs d'applications. Et c'est quelque chose que nous utilisons au quotidien. 

Les variables d'environnement ont même une place dans [l'application douze facteurs de facto](https://12factor.net/config). Elles ont une longue liste d'avantages qui inclut la configurabilité et la sécurité des applications, comme le montrent de nombreuses ressources telles que [celle-ci](https://hyperlane.co/blog/the-benefits-of-environment-variables-and-how-to-use-them), ou même [celle-ci de StackOverflow](https://serverfault.com/questions/892481/what-are-the-advantages-of-putting-secret-values-of-a-website-as-environment-var).

Les variables d'environnement sont géniales et je suis complètement derrière cette idée. Cependant, tout a un coût – et les variables d'environnement, si elles sont utilisées sans précaution, peuvent avoir des effets néfastes sur nos bases de code et nos applications.

## La malédiction des variables d'environnement

Comment les variables d'environnement pourraient-elles être une mauvaise chose si elles nous aident à écrire un code plus sécurisé et à configurer plus facilement nos applications pour différents environnements ? 

Ironiquement, les inconvénients des variables d'environnement proviennent précisément de leur nature qui les rend si utiles : elles sont globales et externes, ce qui permet aux développeurs d'applications d'injecter des configurations et de gérer ces secrets dans un endroit plus difficile à compromettre.

En tant que développeurs, nous savons tous à quel point les états globaux sont mauvais pour nos applications. Et ne prenez pas seulement ma parole pour cela, ces problèmes ont été discutés dans de nombreux endroits comme [ici](https://softwareengineering.stackexchange.com/questions/148108/why-is-global-state-so-evil), [ici](https://thevaluable.dev/global-variable-explained/), et [ici](https://stackoverflow.com/questions/19209468/why-is-global-state-bad).

Pour cet article, je vais me concentrer sur les 2 principaux défauts que je rencontre le plus souvent lorsque je travaille avec des variables d'environnement :

* Inflexibilité / Mauvaise testabilité
* Compréhension du code / Lisibilité

## Comment utiliser correctement les variables d'environnement

De la même manière que je traite les variables globales ou les motifs globaux (comme le singleton) appliqués à de mauvais endroits, mon arme préférée est [l'injection de dépendances](https://en.wikipedia.org/wiki/Dependency_injection).

Ce ne sera pas exactement la même chose que ce que nous faisons pour les dépendances de code, mais les principes sont les mêmes. Au lieu d'utiliser directement les variables d'environnement (dépendances), nous les injectons aux points d'appel (c'est-à-dire, l'endroit où elles sont réellement utilisées). Cela inverse la relation de "points d'appel dépendants" à "points d'appel exigeants". 

L'injection de dépendances résout ces problèmes en :

* permettant aux développeurs d'injecter des configurations plus facilement au moment des tests
* réduisant la portée mentale pour les lecteurs de code au package uniquement, éliminant ainsi toutes les externalités

## Alors, comment appliquer ces principes ?

Je vais utiliser un exemple Node.js pour démontrer comment nous pouvons refactoriser une base de code et éliminer les variables d'environnement dispersées.

### Situation hypothétique

Imaginons que nous avons une application simple avec un seul endpoint qui interrogera toutes les TODOs dans une base de données PostGres. Voici notre module de base de données avec des variables d'environnement dispersées :

```js
const { Client } = require("pg");

function Postgres() {
  const c = new Client({
    connectionString: process.env.POSTGRES_CONNECTION_URL,
  });
  this.client = c;
  return this;
}

Postgres.prototype.init = async function () {
  await c.connect();
  return this;
};

Postgres.prototype.getTodos = async function () {
  return this.client.query("SELECT * FROM todos");
};

module.exports = Postgres;

```

et ce module sera injecté dans notre contrôleur HTTP via le point d'entrée de l'application :

```js
const express = require("express");
const TodoController = require("./controller/todo");
const Postgres = require("./pg");

const app = express();

(async function () {
  const db = new Postgres();
  await db.init();
  const controller = new TodoController(db);
  controller.install(app);

  app.listen(process.env.PORT, (err) => {
    if (err) console.error(err);
    console.log(`UP AND RUNNING @ ${process.env.PORT}`);
  });
})();

```

En jetant un coup d'œil au fichier de point d'entrée ci-dessus, nous n'avons aucun moyen de savoir quelles sont les exigences de l'application en matière de variables d'environnement (ou de configuration d'environnement en général) (moins un point pour la lisibilité du code 👎 ).

### Refactorisation du code

La première étape pour améliorer le code précédemment présenté est d'identifier tous les endroits où les variables d'environnement sont utilisées directement. 

Pour notre cas spécifique ci-dessus, c'est assez simple car la base de code est petite. Mais pour des bases de code plus grandes, vous pouvez utiliser des outils de linting comme [eslint](https://github.com/eslint/eslint) pour scanner tous les endroits qui utilisent des variables d'environnement directement. Il suffit de configurer une règle, par exemple, interdisant les variables d'environnement (comme `node/no-process-env` de [eslint-plugin-node](https://github.com/mysticatea/eslint-plugin-node#readme)).

Il est maintenant temps de supprimer les utilisations directes des variables d'environnement de nos modules d'application et d'inclure ces configurations dans les exigences du module :

```js
...
function Postgres(opts) {
  const { connectionString } = opts;
  const c = new Client({
    connectionString,
  });
  this.client = c;
  return this;
}
...

```

Ces configurations seront ensuite fournies uniquement à partir du point d'entrée de notre application :

```js
...
const db = new Postgres({
  connectionString: process.env.POSTGRES_CONNECTION_URL,
});
...

```

Il est beaucoup plus clair quelles sont les exigences environnementales pour notre application maintenant, en regardant le point d'entrée. Cela évite les problèmes potentiels avec les variables d'environnement oubliées à ajouter.

Le code source complet pour la démonstration ci-dessus peut être trouvé [ici](https://github.com/stanleynguyen/dispelling-environment-variable-curse-demo).

## Bonus : Questions fréquemment posées

Ce sont quelques-unes des questions que **je pense** pourraient être posées par ceux qui lisent cet article. Peut-être ne sont-elles pas des questions réellement fréquemment posées, mais après tout, quel est le mal à aborder des opinions alternatives possibles ?

### Pourquoi ne pas utiliser un fichier/module de configuration central ?

J'ai vu plusieurs tentatives pour résoudre ce problème en utilisant un emplacement central pour extraire ces valeurs (comme un fichier/module `config.js` pour les projets Node). 

Mais cette approche n'est pas meilleure que l'utilisation directe des variables d'environnement fournies par le runtime de l'application (comme `process.env`) car tout est toujours consolidé dans un état quelque peu global (un seul objet de configuration utilisé dans toute l'application). 

En fait, cela pourrait être encore pire, car nous introduisons maintenant un autre endroit où le code peut pourrir.

### Que faire si je veux une configuration zéro-config pour mon module ?

Oui, qui n'aime pas les modules zéro-config, prêts à l'emploi. Encore une fois, je tiens à réitérer que la construction de logiciels consiste à faire des compromis, et cela se fait au détriment de la lisibilité, comme cet article l'a discuté. 

Si vous souhaitez toujours une configuration zéro-config possible, je suggère d'avoir des objets de configuration (c'est-à-dire, l'argument `opts` du constructeur dans l'exemple de code précédent) et l'utilisation directe des variables d'environnement uniquement comme solution de repli, quelque chose comme ceci :

```js
function Postgres(opts) {
  const connectionString =
    opts.connectionString || process.env.POSTGRES_CONNECTION_URL;
  const c = new Client({
    connectionString,
  });
  this.client = c;
  return this;
}

```

De cette manière, les lecteurs de notre code pourront toujours reconnaître (bien que avec moins de lisibilité, car cela a été échangé contre une configurabilité zéro-config) les exigences du module.

### Merci d'avoir lu !

Enfin, si vous aimez mes écrits, rendez-vous sur [mon blog](https://blog.stanleynguyen.me/) pour des commentaires similaires et suivez [moi sur Twitter](https://twitter.com/stanley_ngn). 🎉