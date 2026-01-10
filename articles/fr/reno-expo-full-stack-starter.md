---
title: Comment construire des applications Full Stack avec un kit de démarrage simple
  appelé Reno Expo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-17T23:10:42.000Z'
originalURL: https://freecodecamp.org/news/reno-expo-full-stack-starter
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a34740569d1a4ca2431.jpg
tags:
- name: Apps
  slug: apps-tag
- name: Express
  slug: express
- name: full stack
  slug: full-stack
- name: node
  slug: node
- name: React
  slug: react
seo_title: Comment construire des applications Full Stack avec un kit de démarrage
  simple appelé Reno Expo
seo_desc: 'By Jackson Bates

  Building any new project from scratch can be intimidating. There''s a lot to decide
  before you can even start coding to test out your idea.

  How are you building the front end? Plain CSS, or a framework? Vanilla HTML and
  JS, or a frame...'
---

Par Jackson Bates

Construire un nouveau projet à partir de zéro peut être intimidant. Il y a beaucoup de décisions à prendre avant même de pouvoir commencer à coder pour tester votre idée.

Comment allez-vous construire le front end ? CSS simple, ou un framework ? HTML et JS vanilla, ou un framework ou une bibliothèque comme Vue, React, Angular ou Svelte ?

Quel langage back end allez-vous utiliser ? JavaScript, Ruby, PHP, Python ou autre chose ? Peut-être "serverless" ?

Et la base de données ? Relationnelle ? MySQL, Postgresql ? NoSQL ? Mongo ? Peut-être quelque chose de "simple" comme Firebase ?

Comment allez-vous gérer l'authentification ? Peut-être une intégration Passport qui inclut simplement un écran de connexion Facebook, Google, Github et LinkedIn ?

Chaque fois que j'ai une idée cool pour une petite application que je veux construire moi-même, je suis toujours épuisé par la gamme d'options et de décisions à prendre.

J'ai donc pris le temps de réfléchir à ma pile idéale, y compris les considérations d'authentification et de déploiement, et j'ai regroupé le tout dans un package raisonnablement facile à configurer : Reno Expo.

# Qu'est-ce que Reno Expo ?

Reno Expo signifie React, NodeJS, Express et Postgresql. Il utilise également Sequelize comme ORM pour la base de données.

Au cœur, c'est une application Express très simple qui inclut une application Create React App pour le front end. Elle est conçue pour être déployée sur Heroku et dispose d'une interface très simple pour enregistrer de nouveaux utilisateurs et se connecter, en utilisant JWT pour l'authentification.

À part cela, c'est une ardoise complètement vierge. Je l'ai intentionnellement laissée assez vide en termes de style CSS, afin de pouvoir intégrer les bibliothèques de style que je souhaite ou écrire mon propre CSS selon les besoins.

Outre la version complètement brute de Reno Expo, j'ai également réalisé un projet freeCodeCamp, la Bibliothèque Personnelle, en utilisant cette pile. Il sert d'exemple sur la façon d'intégrer un framework CSS, Ant Design dans ce cas, et fournit également des exemples d'extension de la base de données avec des migrations Sequelize.

## Où puis-je l'obtenir ?

Le code des deux applications peut être trouvé ici :

* [Kit de démarrage Reno Expo](https://github.com/JacksonBates/reno-expo)
* [Bibliothèque Personnelle, construite avec Reno Expo](https://github.com/JacksonBates/reno-expo-books)

Chacun dispose d'un fichier README.md détaillé, mais j'expliquerai également comment commencer avec les deux, et comment la deuxième application s'appuie sur le kit de démarrage dans cet article.

## À quoi ressemblent les applications ?

Des exemples pour les deux applications peuvent être trouvés ici :

* [Reno Expo, exemple hébergé sur Heroku](http://renoexpo.herokuapp.com/)
* [Bibliothèque Personnelle, hébergée sur Heroku](https://reno-expo-books.herokuapp.com/)

Le kit de démarrage est hideux, franchement. Comme je l'ai mentionné précédemment, il a un style minimal - et je ne plaisantais pas. La Bibliothèque Personnelle montre comment on pourrait intégrer un framework CSS pour obtenir quelques victoires de style faciles avec un effort minimal.

## Commencer avec Reno Expo

Pour travailler avec Reno Expo, vous aurez besoin des éléments suivants installés sur votre ordinateur local : [git](https://git-scm.com/), [Node](https://nodejs.org/en/download/), npm (inclus avec votre téléchargement de Node), et [Postgresql](https://www.postgresql.org/).

Utilisez les dernières versions de chacun si vous commencez à partir de zéro, mais si vous avez déjà d'autres versions de ceux-ci sur votre système, ils peuvent très bien fonctionner. 

Pour information, j'ai développé avec ces versions : Node 8.16, npm 6.14 et Postgres 10, et mes déploiements Heroku ont été les dernières versions stables de tous ceux-ci. 

Si vous rencontrez des problèmes en utilisant différentes versions, essayez d'utiliser ces versions ou cherchez les différences dans les journaux de modifications appropriés pour vous aider à vous débloquer.

Votre installation Postgres nécessitera également un utilisateur valide avec des privilèges de création de base de données. La configuration de cela dépasse le cadre de cet article, mais vous pouvez trouver les guides pertinents pour votre environnement avec une recherche en ligne pour "getting started with postgres windows/mac/ubuntu" etc.

### Installation du Kit de démarrage

Pour initialiser le kit de démarrage, nous utiliserons deux terminaux. Plus tard, je partagerai un truc pour lancer votre environnement de développement à partir d'un seul terminal, mais pour l'instant, nous garderons le front end et le back end séparés.

Dans le premier terminal, à partir du répertoire dans lequel vous souhaitez créer votre nouvelle application :

`git clone git@github.com:JacksonBates/reno-expo.git`

Ensuite, naviguez vers ce nouveau dossier : `cd reno-expo`

Faites une copie du fichier .env : `cp .env.example .env`

Vous devrez ajuster les variables de développement dans le nouveau fichier .env :

```sh
DEVELOPMENT_DATABASE=database_development
DEVELOPMENT_DATABASE_USERNAME=sequelize
DEVELOPMENT_DATABASE_PASSWORD=password
```

La base de données de développement peut être ce que vous voulez, mais le nom d'utilisateur et le mot de passe devront correspondre à ce que vous avez configuré pour votre installation locale de Postgres.

Maintenant, installez les packages npm pour le back end : `npm i`

Ensuite, nous allons créer la base de données en utilisant Sequelize. Notez que si votre installation Postgres n'est pas configurée correctement, c'est la première partie qui va échouer...

`npx sequelize-cli db:create`

Cela créera la base de données avec le nom que vous avez défini dans votre fichier .env.

Maintenant, nous pouvons créer la table pour nos utilisateurs :

`npx sequelize-cli db:migrate`

Si cela fonctionne, vous devriez voir une sortie de terminal comme celle-ci :

```sh
== 20200606113054-create-user: migrating =======
== 20200606113054-create-user: migrated (0.074s)
```

Si tout cela a fonctionné, vous pouvez maintenant démarrer le serveur back end avec `npm start`.

La configuration du front end devrait être plus simple. Dans votre deuxième terminal, naviguez vers le dossier client : `reno-expo/client`

Installez les modules node : `npm i`

Maintenant, exécutez l'application React avec `npm start`.

### Lancement en un seul terminal

Si tout s'initialise correctement, à l'avenir, vous pourrez facilement lancer à la fois l'application React et le serveur Express avec une seule commande à partir d'un seul terminal :

`npm run dev`

### Vérifiez que cela fonctionne

Dans votre navigateur de choix, visitez localhost:3000 et vous devriez voir une page 'Home' très basique et quelques liens vers une page Admin et une page de connexion.

Admin devrait être verrouillée jusqu'à ce que vous vous connectiez.

La connexion nécessitera que vous créiez d'abord un compte utilisateur. Cliquez sur 'Je n'ai pas de compte' et créez-en un via le formulaire d'inscription. Vous pouvez maintenant vous connecter et tester votre accès à la page Admin.

Si tout fonctionne, vous pouvez commencer à développer votre application !

## Construire quelque chose de plus substantiel avec Reno Expo

Pour créer la Bibliothèque Personnelle, il y avait 3 choses principales à faire : 

1. installer et implémenter le framework CSS Ant Design
2. créer les nouvelles routes / vues front end
3. étendre l'API avec de nouveaux modèles de base de données et contrôleurs

Après avoir installé Ant Design avec `npm i antd`, j'ai ajouté la ligne suivante au fichier App.css existant dans le dossier `client/styles` : `@import"~antd/dist/antd.css";`

Cela garantit que le style Ant Design sera disponible dans toute l'application.

Le dépôt pour la Bibliothèque Personnelle contient toutes les modifications, mais voici quelques exemples de modèles que vous pourriez utiliser. Bien sûr, vous pourriez créer votre propre CSS, ou utiliser d'autres frameworks comme Material-UI, Bootstrap ou autres, ce qui suit est juste illustratif.

### Implémentation d'une mise en page

```js
import React from "react";
import { Layout, Menu } from "antd";
import { Link } from "react-router-dom";
import { useAuth } from "../../context/auth";

const { Content, Sider, Footer } = Layout;

export default function AppLayout(props) {
  const { setAuthTokens } = useAuth();

  const logout = (e) => {
    e.preventDefault();
    setAuthTokens();
    localStorage.removeItem("tokens");
  };

  return (
    <Layout>
      <Sider breakpoint="md" collapsedWidth="0">
        <Menu theme="dark" mode="inline">
          <Menu.Item key="1">
            <Link to={"/"}>
              <span className="nav-text">Accueil</span>
            </Link>
          </Menu.Item>
          <Menu.Item key="2">
            <Link to={"/personal"}>
              <span className="nav-text">Bibliothèque Personnelle</span>
            </Link>
          </Menu.Item>
          <Menu.Item key="3">
            <Link to={"/public"}>
              <span className="nav-text">Bibliothèque Publique</span>
            </Link>
          </Menu.Item>
          <Menu.Item key="4">
            <Link to={"/login"} onClick={logout}>
              <span className="nav-text">Se déconnecter</span>
            </Link>
          </Menu.Item>
        </Menu>
      </Sider>
      <Layout style={{ minHeight: "100vh" }}>
        <Content style={{ margin: "24px 16px 0" }}>
          <div style={{ padding: 24, background: "#fff", minHeight: "80vh" }}>
            {props.children}
          </div>
        </Content>
        <Footer>Reno Expo Books</Footer>
      </Layout>
    </Layout>
  );
}

```

Outre une petite fonction gérant le jeton d'authentification, le reste de cela utilise les composants fournis par Ant Design pour créer une application avec une barre latérale persistante pour la navigation, et un contenu rendu dynamiquement en fonction du composant actif.

Où le composant actif est-il chargé ?

```js
import React from "react";
import { Route } from "react-router-dom";
import { AppLayout } from "../layouts";

export default function PublicRoute({ children, ...rest }) {
  return (
    <Route {...rest}>
      <AppLayout>{children}</AppLayout>
    </Route>
  );
}
```

Ci-dessus, nous avons un exemple du composant PublicRoute. Il y a quelques autres composants de route que j'utilise, mais les comprendre devrait être assez simple sur la base de celui-ci.

Notre PublicRoute est une route React-Router `<Route>` enveloppant la mise en page ci-dessus. 

App.js montre des exemples de ces routes publiques étant utilisées, par exemple :

```js
<PublicRoute exact path="/">
  <Home />
</PublicRoute>
      
```

Dans les deux premiers fichiers, nous pouvons voir une référence à `children`.

`children` est une prop intégrée dans React qui fait référence aux composants enfants qui sont imbriqués dans les composants parents.

Dans les exemples ci-dessus, nous voyons le composant `<Home>` comme un enfant de `PublicRoute`. Dans le fichier PublicRoute.js, nous voyons la référence à children, à la fois dans les props et étant passée directement au composant `<AppLayout>`. Et enfin, dans AppLayout.js, le composant `<Content>` contient également les enfants. Dans tous ces cas, children fait référence au composant `<Home>` passé depuis App.js.

En pratique, cela signifie que l'un des composants passés depuis App.js sur des routes publiques ou privées sera rendu dans la zone de contenu de notre mise en page, laissant la barre latérale de navigation intacte.

D'autres fichiers dans le dossier client devraient donner de nombreux exemples de la façon dont des éléments comme le formulaire de connexion peuvent être remplacés par le framework Ant Design après quelques modifications mineures.

### Apporter des modifications au back end

L'autre chose principale à développer lors de l'utilisation de Reno Expo est l'API elle-même - après tout, il est utile de pouvoir enregistrer un utilisateur et de le faire se connecter, mais la plupart des applications nécessitent plus que cela pour être vraiment utiles.

Pour les besoins de ma version de la Bibliothèque Personnelle, nous devions implémenter un certain nombre de nouveaux points de terminaison API, et créer de nouvelles tables de base de données pour stocker les données des livres et des commentaires.

Il est utile de souligner ici que dans ces exemples, je travaille à l'envers. Normalement, je créerais d'abord les migrations de base de données et les modèles, puis je construirais les méthodes de contrôleur et les routes API ensuite. Je les présente 'à l'envers' ici afin que nous puissions suivre la logique de notre objectif à travers la façon dont il a été implémenté pièce par pièce.

Le fichier `reno-expo-books/app/router/router.js` contient toutes les routes du projet, mais je vais partager deux exemples ici à titre d'illustration.

```js
// Route publique
app.get("/api/books", booksController.getBooks);


// Route privée
app.get(
    "/api/user/books",
    [authJwt.verifyToken],
    booksController.getUserBooks
  );
  
```

L'ajout de routes publiques est assez simple, nous devons simplement définir la méthode http, le point de terminaison API et la méthode de contrôleur qui gérera la requête, par exemple une requête GET, vers `api/books` gérée par la méthode `getBooks` du contrôleur booksController.

L'authentification JWT que nous avons déjà disponible à partir du kit de démarrage Reno Expo rend les routes privées également assez simples. Tout ce que nous devons faire est d'inclure le middleware pour vérifier le jeton, `[authJwt.verifyToken]` dans l'exemple ci-dessus.

Les contrôleurs pour ces points de terminaison, c'est-à-dire le code qui traite les requêtes, sont également raisonnablement simples, bien que l'utilisation de Sequelize pour la première fois puisse avoir une courbe d'apprentissage.

Voici un exemple de la méthode publique 'getBooks' référencée ci-dessus :

```js
const db = require("../../models/index");
const Sequelize = require("sequelize");
const Book = db.Book;
const BookComment = db.BookComment;

// Routes publiques

exports.getBooks = (req, res) => {
  Book.findAll({
    where: { userId: null },
    attributes: {
      include: [
        [
          Sequelize.fn("COUNT", Sequelize.col("BookComments.id")),
          "commentcount",
        ],
      ],
      exclude: ["createdAt", "updatedAt"],
    },
    include: {
      model: BookComment,
      attributes: [],
    },
    group: ["Book.id"],
  })
    .then((data) => res.status(200).json(data))
    .catch((error) => res.send(error));
};

```

Les imports en haut du fichier fournissent les modèles de base de données et la bibliothèque Sequelize.

La méthode `getBooks` semble compliquée, mais elle est composée de quelques parties relativement simples.

Tout d'abord, nous appelons le modèle `Book`. Le modèle est une représentation ORM de la table des livres - nous verrons comment nous créons cette table bientôt.

Sequelize, comme la plupart des ORM, fournit non seulement un schéma ou une description de la table, mais aussi des méthodes qui peuvent être appelées sur le modèle. Dans ce cas, nous appelons `Book.findAll({...})`, qui retournera tous les livres qu'il peut trouver qui correspondent à des paramètres particuliers que nous lui passons.

Dans ce cas particulier, je voulais recevoir quelque chose comme ceci :

```json
[
  {
    "id": 1,
    "title": "The Hobbit",
    "commentcount": 3
  },
  {
    "id": 2,
    "title": "The Lord of the Rings",
    "commentcount": 2
  }
]
```

Dans la méthode findAll, nous passons d'abord les paramètres `where`. Si vous êtes familier avec SQL, il devrait être assez clair ce que cela fait. Dans l'exemple ci-dessus, nous voulons tous les livres où l'userId est null. Cela est dû au fait que nous ne voulons retourner que les livres publics à partir de ce contrôleur, donc seulement ceux qui n'ont pas d'utilisateur attaché.

Ensuite, les `attributes` décrivent la forme de la réponse, ou les données que nous attendons en retour. La section exclude est plus facile à comprendre, donc je vais l'expliquer en premier. La table des livres a des colonnes pour les timestamps created_at et updated_at pour chaque enregistrement. Puisque nous ne voulons pas de ceux-ci dans notre réponse json, nous pouvons les omettre explicitement dans la section exclude.

Notre partie include des attributs est plus compliquée. En SQL brut, nous compterions le nombre de commentaires associés comme ceci :

```sql
SELECT "Books"."id", "Books"."title", COUNT("BookComments"."id") AS "commentcount"
FROM "Books"
JOIN "BookComments" ON "BookComments"."bookId" = "Books"."id"
GROUP BY "Books"."id";
```

La fonction SQL COUNT compte tous les enregistrements dans la colonne BookComments.id, et la fonction GROUP BY limite les commentaires comptés à chaque livre, par ID.

Il est utile de noter que commentcount n'est pas une colonne de la table des livres, mais plutôt une colonne calculée dérivée de la chose que nous demandons à la base de données de compter pour nous.

Sequelize nous donne accès à la fonction count via sa bibliothèque.

La fonction pertinente est incluse dans les attributs ci-dessus comme ceci :

```js
[Sequelize.fn("COUNT", Sequelize.col("BookComments.id")),"commentcount"]

```

C'est-à-dire "Appeler la fonction Sequelize 'COUNT', compter les colonnes pour BookComments.id, et nommer la colonne générée 'commentcount'

Cela fournit notre fonction de comptage tout comme dans la version SQL. Il ne reste plus qu'à inclure le `group: ['Book.id']` comme paramètre supplémentaire de la méthode findAll sur le modèle Book.

L'autre partie que vous avez peut-être remarquée dans les paramètres de la méthode findAll est celle-ci :

```js
include: {
  model: BookComment,
  attributes: [],
},
```

C'est exact, _un autre_ include. Remarquez que celui-ci n'est pas imbriqué dans les attributs, mais est son pair. Cet include agit de la même manière que l'instruction JOIN dans le SQL ci-dessus. Cela signifie que nous voulons inclure le modèle BookComment, mais nous n'avons pas besoin d'ajouter d'attributs puisque nous ne voulons pas référencer directement l'une des colonnes qu'il possède - nous l'utilisons simplement dans la fonction de comptage.

### Apporter des modifications à la base de données

La dernière chose que nous devons comprendre pour être productif avec Sequelize est les migrations pour apporter des modifications à la base de données.

Les migrations peuvent être considérées comme un contrôle de source pour votre base de données.

Bien que vous puissiez modifier une base de données directement en créant de nouvelles tables, en ajoutant des colonnes, en introduisant des contraintes, en changeant les types de données ou autre chose, l'utilisation de migrations vous permet de faire des changements expérimentaux avec la possibilité de les annuler facilement, et de pouvoir partager votre développement sur une base de données avec d'autres personnes qui n'ont pas à lutter pour garder leurs bases de données locales et de production synchronisées.

Les migrations sont essentiellement du code qui indique à votre base de données comment changer, et comment annuler le changement qui a été introduit, si cela est nécessaire.

Voici la migration pour créer la table des livres :

```js
'use strict';
module.exports = {
  up: (queryInterface, Sequelize) => {
    return queryInterface.createTable('Books', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      title: {
        type: Sequelize.STRING
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE
      }
    });
  },
  down: (queryInterface, Sequelize) => {
    return queryInterface.dropTable('Books');
  }
};
```

Cette migration est un module qui exporte deux fonctions : `up` et `down`

La fonction `up` effectue les changements, tandis que la fonction `down` annule tous les changements qui ont été introduits.

Ainsi, nous voyons que up crée une table appelée 'Books' avec les colonnes id, title, created_at et updated_at. Chaque colonne a également certaines qualités associées, telles que le type de données, et si elle peut contenir une valeur nulle, par exemple.

La fonction down supprime simplement la table.

Je ne vais pas partager toute la migration suivante, c'est-à-dire celle pour créer la table Book Comment, mais je vais montrer un extrait de sa fonction up qui définit la colonne bookId :

```js
bookId: {
  type: Sequelize.INTEGER,
  onDelete: "CASCADE",
  references: {
    model: { tableName: "Books" },
    key: "id",
  },
  allowNull: false,
},
 
```

Les choses intéressantes à noter ici sont la propriété `onDelete`, qui est définie sur "CASCADE" et la propriété `references` qui lie la table des livres via la colonne id. Cela établit la relation entre un livre et ses commentaires. La propriété onDelete indique à la base de données ce qu'il faut faire si un livre est supprimé : cette action de suppression doit se propager à tous les commentaires associés. C'est-à-dire que si je supprime 'The Hobbit', tous les commentaires relatifs à 'The Hobbit' sont également supprimés.

La dernière chose à savoir est que ces migrations sont également soutenues par des modèles. Le modèle BookComment ressemble à ceci :

```js
"use strict";
module.exports = (sequelize, DataTypes) => {
  const BookComment = sequelize.define(
    "BookComment",
    {
      comment: DataTypes.TEXT,
      bookId: {
        type: DataTypes.INTEGER,
        references: {
          model: "Books",
          key: "id",
        },
      },
    },
    {}
  );
  BookComment.associate = function (models) {
    // associations can be defined here
    BookComment.belongsTo(models.Book, {
      foreignKey: "bookId",
    });
  };
  return BookComment;
};

```

Vous remarquerez quelques similitudes entre ceci et la migration. Il a deux parties, la définition du modèle et les associations du modèle. Celles-ci aident à renforcer la relation entre les différentes tables selon les besoins.

Pour créer des tables à partir de zéro, vous pouvez utiliser une commande comme celle-ci :

`npx sequelize-cli model:generate --name Post --attributes post:text`

Cela générera automatiquement un squelette de modèle et un squelette de migration pour une table `posts` avec la colonne 'post'. Vous pouvez ensuite remplir la migration et le modèle avec les détails des autres colonnes ou associations pertinentes.

Si vous souhaitez simplement modifier une table existante, par exemple, pour changer un type de données ou ajouter une colonne, vous pouvez utiliser une commande pour générer uniquement une migration :

`npx sequelize-cli migration:generate --name add-userId-to-posts`

Vous pouvez ensuite apporter les modifications au modèle existant et au nouveau fichier de migration selon les besoins.

### Appliquer les modifications de la base de données

Écrire simplement le code pour mettre à jour la base de données ne suffit pas, vous devez également exécuter les migrations pour chaque base de données sur laquelle votre code fonctionne - c'est-à-dire votre machine de développement locale, peut-être votre serveur de staging si vous en avez un, et également votre serveur de production.

La commande pour exécuter celles-ci est :

`npx sequelize-cli db:migrate`

Vous pouvez également annuler les migrations : 

`npx sequelize-cli db:migrate:undo`

## Bon codage !

C'est tout ! Comme je l'ai mentionné ci-dessus, je déploie personnellement tout ce que je fais avec ceux-ci sur Heroku, et il y a des instructions détaillées pour les particularités de leur déploiement sur Heroku dans le README.md de Reno Expo. Cela inclut également les commandes pour exécuter les migrations sur le serveur de Heroku.

Il y a beaucoup à assimiler ici. Mais si vous comprenez fondamentalement Express et React, et que vous êtes prêt à plonger dans la documentation de Sequelize lorsque cela est nécessaire, vous pouvez construire à peu près tout ce que vous pouvez imaginer qui bénéficie d'une base de données relationnelle en utilisant ce kit de démarrage.

Ce n'est pas tout à fait aussi complet qu'un framework MVC complet comme Rails, Laravel, Sails ou Nest, mais il se trouve que j'aime qu'il y ait moins de superflu et moins de `magie` cachée dans les internes de celui-ci. Après tout, ce n'est qu'une application Create React App regroupée avec un serveur léger et un package ORM. Le reste dépend de vous.

---

Si vous êtes arrivé à la fin de cet article, et surtout si vous construisez quelque chose avec Reno Expo, j'adorerais avoir de vos nouvelles. Vous pouvez me contacter sur Twitter : [@JacksonBates](https://twitter.com/JacksonBates)