---
title: 'Full Stack React : Comment construire votre propre blog en utilisant Express,
  Hooks et Postgres.'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-03T20:16:00.000Z'
originalURL: https://freecodecamp.org/news/fullstack-react-blog-app-with-express-and-psql
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/photo-1568127558771-dad1b9d93a08.jpg
tags:
- name: Express
  slug: express
- name: postgres
  slug: postgres
- name: React
  slug: react
seo_title: 'Full Stack React : Comment construire votre propre blog en utilisant Express,
  Hooks et Postgres.'
seo_desc: "By Mohammad Iqbal\nIn this tutorial we're going to build out a full stack\
  \ React blog along with a blog admin back end. \nI will walk you through all the\
  \ steps in detail.\nBy the end of this tutorial, you will have enough knowledge\
  \ to build fairly comple..."
---

Par Mohammad Iqbal

Dans ce tutoriel, nous allons construire un blog full stack React ainsi qu'un backend d'administration de blog. 

Je vais vous guider à travers toutes les étapes en détail.

À la fin de ce tutoriel, vous aurez suffisamment de connaissances pour construire des applications full stack assez complexes en utilisant des outils modernes : React, Express et une base de données PostgreSQL. 

Pour garder les choses concises, je vais faire le minimum de style/mise en page et laisser cela à l'appréciation du lecteur. 

**Projet terminé :**  
[https://github.com/iqbal125/react-hooks-complete-fullstack](https://github.com/iqbal125/react-hooks-complete-fullstack)

**Application Admin :**  
[https://github.com/iqbal125/react-hooks-admin-app-fullstack](https://github.com/iqbal125/react-hooks-admin-app-fullstack)

**Projet de démarrage :**  
[https://github.com/iqbal125/react-hooks-routing-auth-starter](https://github.com/iqbal125/react-hooks-routing-auth-starter)

**Comment construire le projet de démarrage :**  
[https://www.freecodecamp.org/news/build-a-react-hooks-front-end-app-with-routing-and-authentication/](https://www.freecodecamp.org/news/build-a-react-hooks-front-end-app-with-routing-and-authentication/)

**Comment ajouter un moteur de recherche fullstack à ce projet :**  
[https://www.freecodecamp.org/news/react-express-fullstack-search-engine-with-psql/](https://www.freecodecamp.org/news/react-express-fullstack-search-engine-with-psql/)

Vous pouvez regarder une version vidéo de ce tutoriel ici  
[https://www.youtube.com/playlist?list=PLMc67XEAt-yzxRboCFHza4SBOxNr7hDD5](https://www.youtube.com/playlist?list=PLMc67XEAt-yzxRboCFHza4SBOxNr7hDD5)

> Connectez-vous avec moi sur Twitter pour plus de mises à jour sur les futurs tutoriels : [https://twitter.com/iqbal125sf](https://twitter.com/iqbal125sf)

## Section 1 : Configuration du serveur Express et de la base de données PSQL

1. **Structure du projet**
2. **Configuration de base d'Express**
3. **Connexion au côté client**  
axios vs react-router vs express router  
pourquoi ne pas utiliser un ORM comme Sequelize ?
4. **Configuration de la base de données**  
Clés étrangères PSQL  
Shell PSQL
5. **Configuration des routes Express et des requêtes PSQL**

## Section 2 : Configuration du front-end React

1. **Configuration de l'état global avec des réducteurs, des actions et un contexte.**   
Enregistrement des données de profil utilisateur dans notre base de données  
Configuration des actions et des réducteurs
2. **Application React côté client**  
addpost.js  
editpost.js   
posts.js  
showpost.js  
profile.js  
showuser.js

## Section 3 : Application Admin

1. **Authentification de l'application Admin**
2. **Privilèges globaux d'édition et de suppression** 
3. **Tableau de bord Admin**
4. **Suppression des utilisateurs ainsi que de leurs publications et commentaires**

## Structure du projet

Nous commencerons par discuter de la structure des répertoires. Nous aurons 2 répertoires, le répertoire **Client** et le répertoire **Server**. Le répertoire **Client** contiendra le contenu de notre application React que nous avons configurée dans le dernier tutoriel et le **Server** contiendra le contenu de notre serveur `express` et la logique de nos appels API à notre base de données. Le répertoire **Server** contiendra également notre schéma de notre base de données **SQL**. 

La structure finale des répertoires ressemblera à ceci.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-158.png)

## Configuration de base d'Express

Si vous ne l'avez pas déjà fait, vous pouvez installer `express-generator` avec la commande :

`npm install -g express-generator`

C'est un outil simple qui générera un projet express de base avec une seule commande simple, similaire à `create-react-app`. Cela nous fera gagner un peu de temps pour ne pas avoir à tout configurer à partir de zéro. 

Nous pouvons commencer par exécuter la commande `express` dans le répertoire **Server**. Cela nous donnera une application express par défaut, mais nous n'utiliserons pas la configuration par défaut, nous devrons la modifier. 

Tout d'abord, supprimons le dossier **routes**, le dossier **views** et le dossier **public**. Nous n'en aurons pas besoin. Vous devriez avoir seulement 3 fichiers restants. Le fichier **www** dans le dossier **bin**, le fichier `app.js` et le fichier `package.json`. Si vous avez accidentellement supprimé l'un de ces fichiers, générez simplement un autre projet express. Puisque nous avons supprimé ces dossiers, nous devrons également modifier un peu le code. Refactorez votre fichier `app.js` comme suit :

```javascript

var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');



var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));


module.exports = app;


```

Nous pouvons également placer `app.js` dans un dossier appelé **main**. 

Ensuite, nous devons changer le port par défaut dans le fichier **www** pour autre chose que le port 3000 puisque c'est le port par défaut sur lequel notre application front-end React sera exécutée. 

```javascript
/**
 * Obtenir le port de l'environnement et le stocker dans Express.
 */

var port = normalizePort(process.env.PORT || '5000');
app.set('port', port);

```

En plus des dépendances que nous avons obtenues en générant l'application express, nous allons également ajouter 3 autres bibliothèques pour nous aider :

`cors`**:** c'est la bibliothèque que nous utiliserons pour aider la communication entre l'application React et le serveur Express. Nous le ferons via un proxy dans l'application React. Sans cela, nous recevrions une erreur de ressource d'origine croisée dans le navigateur.

`helmet`**:** Une bibliothèque de sécurité qui met à jour les en-têtes http. Cette bibliothèque rendra nos requêtes http plus sécurisées.

`pg`**:** C'est la bibliothèque principale que nous utiliserons pour communiquer avec notre base de données psql. Sans cette bibliothèque, la communication avec la base de données ne sera pas possible.

nous pouvons procéder à l'installation de ces bibliothèques

`npm install pg helmet cors`

Nous avons terminé la configuration de notre serveur minimal et devrions avoir une structure de projet qui ressemble à ceci. 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-159.png)

Maintenant, nous pouvons tester pour voir si notre serveur fonctionne. Vous pouvez exécuter le serveur sans une **application côté client**. **Express** est une application entièrement fonctionnelle et s'exécutera indépendamment d'une **application côté client**. Si cela est fait correctement, vous devriez voir ceci dans votre terminal.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-160.png)

Nous pouvons garder le serveur en cours d'exécution car nous allons l'utiliser bientôt.

## Connexion au côté client 

Connecter notre **application côté client** à notre serveur est très facile et nous n'avons besoin que d'une seule ligne de code. Allez dans votre fichier `package.json` dans votre **répertoire Client** et entrez ce qui suit :

`"proxy": "http://localhost:5000"`

Et c'est tout ! Notre client peut maintenant communiquer avec notre serveur via un proxy.

**Note : N'oubliez pas que si vous définissez un autre port que le port:5000 dans le fichier `www`, utilisez ce port dans le proxy à la place.

Voici un diagramme pour décomposer et expliquer ce qui se passe et comment cela fonctionne.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-161.png)

Notre **localhost:3000** fait essentiellement des requêtes comme s'il s'agissait de **localhost:5000** via un intermédiaire proxy, ce qui permet à notre **Serveur** de communiquer avec notre **Client**.

Notre côté client est maintenant connecté à notre serveur et nous voulons maintenant tester notre application.

Nous devons maintenant revenir au côté serveur et configurer le routage `express`. Dans votre dossier **main** dans le répertoire **Server**, créez un nouveau fichier appelé `routes.js`. Ce fichier contiendra toutes les routes `express`, qui nous permettent d'envoyer des données à notre **application côté client**. Nous pouvons définir une route très simple pour l'instant :

```javascript
var express = require('express')
var router = express.Router()

router.get('/api/hello', (req, res) => {
	res.json('hello world')
})

module.exports = router
```

Essentiellement, si un appel API est fait à la route `/hello`, notre **serveur Express** répondra avec une chaîne de caractères "hello world" au format json.

Nous devons également refactoriser notre fichier `app.js` pour utiliser les routes express.

```javascript
var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes')

var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));


app.use('/', indexRouter)

module.exports = app;
```

Maintenant, pour notre code côté client dans notre composant `home.js` :

```jsx
import React, { useState, useEffect } from 'react'
import axios from 'axios';

const Home = props => {
    useEffect(() => {
      axios.get('/api/hello')
        .then(res => setState(res.data))
    }, [])

    const [state, setState] = useState('')

  return(
    <div>
      Home
      <p>{state}</p>
    </div>
 )
};

export default Home;
```

Nous faisons une requête `axios` get basique à notre serveur `express` en cours d'exécution, si cela fonctionne, nous devrions voir "hello world" rendu à l'écran. 

Et oui, cela fonctionne, nous avons réussi à configurer une application Fullstack React Node ! 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-162.png)

Avant de continuer, j'aimerais aborder quelques questions que vous pourriez avoir, à savoir quelle est la différence entre `axios`, `react router` et `express router` et pourquoi je n'utilise pas un **ORM** comme **Sequelize**.

### Axios vs Express Router vs React Router

**TLDR;** Nous utilisons `react router` pour naviguer dans notre application, nous utilisons `axios` pour communiquer avec notre serveur `express` et nous utilisons notre serveur `express` pour communiquer avec notre base de données.

Vous vous demandez peut-être à ce stade comment ces 3 bibliothèques fonctionnent ensemble. Nous utilisons `axios` pour communiquer avec notre serveur backend `express`, nous signifierons un appel à notre serveur `express` en incluant "api/" dans l'URI. `axios` peut également être utilisé pour faire des requêtes http directes à n'importe quel point de terminaison backend. Cependant, pour des raisons de sécurité, il n'est pas conseillé de faire des requêtes du client à la base de données. 

`express router` est principalement utilisé pour communiquer avec notre base de données, puisque nous pouvons passer des requêtes SQL dans le corps de la fonction `express router`. `express` ainsi que Node est utilisé pour exécuter du code en dehors du navigateur, ce qui est ce qui rend les requêtes SQL possibles. `express` est également un moyen plus sécurisé de faire des requêtes http plutôt qu'axios.

Cependant, nous avons besoin d'`axios` du côté client React pour gérer les requêtes http asynchrones, nous ne pouvons évidemment pas utiliser `express router` du côté client React. `axios` est basé sur **Promise**, donc il peut automatiquement gérer les actions asynchrones également.

Nous utilisons `react-router` pour naviguer dans notre application, puisque React est une application à page unique, le navigateur ne se recharge pas lors d'un changement de page. Notre application dispose d'une technologie en coulisses qui saura automatiquement si nous demandons une route via `express` ou `react-router`.

### Pourquoi ne pas utiliser une bibliothèque ORM comme Sequelize ?

**TLDR;** Préférence pour travailler directement avec SQL, ce qui permet un meilleur contrôle que l'ORM. Plus de ressources d'apprentissage pour SQL que pour un ORM. Les compétences ORM ne sont pas transférables, les compétences SQL sont très transférables.

Il existe de nombreux tutoriels qui montrent comment implémenter une bibliothèque ORM en utilisant une base de données SQL. Rien de mal à cela, mais je préfère personnellement interagir directement avec SQL. Travailler directement avec SQL vous donne un contrôle plus fin sur le code et je crois que cela vaut la légère augmentation de difficulté lorsque vous travaillez directement avec SQL.

Il y a beaucoup plus de ressources sur SQL que sur n'importe quelle bibliothèque ORM donnée, donc si vous avez une question ou une erreur, il est beaucoup plus facile de trouver une solution.

De plus, vous ajoutez une autre dépendance et un niveau d'abstraction avec une bibliothèque ORM qui pourrait causer des erreurs à l'avenir. Si vous utilisez un ORM, vous devrez suivre les mises à jour et les changements de rupture lorsque la bibliothèque est modifiée. SQL, en revanche, est extrêmement mature et existe depuis des décennies, ce qui signifie qu'il est peu probable qu'il y ait beaucoup de changements de rupture. SQL a également eu le temps d'être affiné et perfectionné, ce qui n'est généralement pas le cas pour les bibliothèques ORM. 

Enfin, une bibliothèque ORM prend du temps à apprendre et les connaissances ne sont généralement pas transférables à autre chose. SQL est le langage de base de données le plus utilisé, et de loin (la dernière fois que j'ai vérifié, environ 90 % des bases de données commerciales utilisaient SQL). Apprendre un système SQL tel que PSQL vous permettra de transférer directement ces compétences et connaissances à un autre système SQL tel que MySQL.

Ce sont mes raisons de ne pas utiliser une bibliothèque ORM.

## Configuration de la base de données

Commençons par configurer le schéma SQL en créant un fichier dans le dossier principal du répertoire Server appelé `schema.sql.` 

Cela contiendra la forme et la structure de la base de données. Pour configurer réellement la base de données, vous devrez bien sûr entrer ces commandes dans le shell PSQL. **Simplement avoir un fichier SQL ici dans notre projet ne fait rien**, c'est simplement un moyen pour nous de référencer à quoi ressemble la structure de notre base de données et permettre à d'autres ingénieurs d'avoir accès à nos commandes SQL s'ils veulent utiliser notre code. 

**Mais pour avoir une base de données fonctionnelle, nous entrerons ces mêmes commandes dans le terminal PSQL.**

```sql

CREATE TABLE users (
  uid SERIAL PRIMARY KEY,
  username VARCHAR(255) UNIQUE,
  email VARCHAR(255),
  email_verified BOOLEAN,
  date_created DATE,
  last_login DATE
);


CREATE TABLE posts (
  pid SERIAL PRIMARY KEY,
  title VARCHAR(255),
  body VARCHAR,
  user_id INT REFERENCES users(uid),
  author VARCHAR REFERENCES users(username),
  date_created TIMESTAMP
  like_user_id INT[] DEFAULT ARRAY[]::INT[],
  likes INT DEFAULT 0
);

CREATE TABLE comments (
  cid SERIAL PRIMARY KEY,
  comment VARCHAR(255),
  author VARCHAR REFERENCES users(username),
  user_id INT REFERENCES users(uid),
  post_id INT REFERENCES posts(pid),
  date_created TIMESTAMP
);

```

Nous avons donc 3 tables ici qui contiendront les données de nos utilisateurs, publications et commentaires. Conformément à la convention SQL, tout le texte en minuscules est le nom de colonne ou de table défini par l'utilisateur, et tout le texte en majuscules est des commandes SQL.

**PRIMARY KEY** : Numéro unique généré par psql pour une colonne donnée

**VARCHAR(255)** : caractère variable, ou texte et nombres. 255 définit la longueur de la ligne. 

**BOOLEAN** : Vrai ou faux 

**REFERENCES** : comment définir la clé étrangère. La clé étrangère est une clé primaire dans une autre table. Je l'explique plus en détail ci-dessous.

**UNIQUE** : Empêche les entrées en double dans une colonne. 

**DEFAULT** : définir une valeur par défaut

**INT[] DEFAULT ARRAY[]::INT[]** : cette commande a l'air assez complexe mais elle est assez simple. Nous avons d'abord un tableau d'entiers, puis nous définissons ce tableau d'entiers à une valeur par défaut d'un tableau vide de type tableau d'entiers. 

**Table des utilisateurs**  
Nous avons une table très basique pour les **utilisateurs**, la plupart de ces données proviendront d'auth0, que nous verrons plus en détail dans la section **authcheck**.  

**Table des publications**  
Ensuite, nous avons la table des publications. Nous obtiendrons notre titre et notre corps à partir du front-end React et nous associerons également chaque publication à un `user_id` et à un `username`. Nous associons chaque publication à un utilisateur avec la clé étrangère de SQL. 

Nous avons également notre tableau de `like_user_id`, qui contiendra tous les identifiants des utilisateurs qui ont aimé une publication, empêchant ainsi les multiples likes d'un même utilisateur. 

**Table des commentaires**  
Enfin, nous avons notre table de commentaires. Nous obtiendrons notre commentaire à partir du front-end react et nous associerons également chaque **utilisateur** à un **commentaire**, nous utilisons donc le champ `user id` et `username` de notre **table des utilisateurs**. Et nous avons également besoin du `post id` de notre **table des publications** puisque un commentaire est fait pour une publication, un commentaire n'existe pas isolément. Chaque commentaire doit donc être associé à la fois à un **utilisateur** et à une **publication**.

### Clés étrangères PSQL

**Une clé étrangère** est essentiellement un champ ou une colonne dans une autre table qui est référencée par la table d'origine. Une clé étrangère fait généralement référence à une **clé primaire** dans une autre table, mais comme vous pouvez le voir dans notre **table des publications**, elle a également un lien de **clé étrangère** vers le `username` dont nous avons besoin pour des raisons évidentes. Pour garantir l'intégrité des données, vous pouvez utiliser la contrainte `UNIQUE` sur le champ `username`, ce qui lui permet de fonctionner comme une clé étrangère.

L'utilisation d'une colonne dans une table qui référence une colonne dans une table différente est ce qui nous permet d'avoir des relations entre les tables de notre base de données, d'où le nom de "bases de données relationnelles" pour les bases de données SQL.

La syntaxe que nous utilisons est :

```sql

column_name data_type REFERENCES other_table(column_name_in_other_table)

```

Ainsi, une seule ligne dans la colonne `user_id` de notre table des publications devra correspondre à une seule ligne dans la colonne `uid` de la **table des utilisateurs**. Cela nous permettra de faire des choses comme rechercher toutes les publications qu'un certain utilisateur a faites ou rechercher tous les commentaires associés à une publication.

**Contrainte de clé étrangère**  
De plus, vous devrez être attentif aux **contraintes de clé étrangère de PSQL**. Ce sont des restrictions qui vous empêchent de supprimer des lignes qui sont référencées par une autre table. 

Un exemple simple est **supprimer des publications sans supprimer les commentaires associés à cette publication**. Le **post id** de la **table des publications** est une **clé étrangère** dans la **table des commentaires** et est **utilisé pour établir une relation entre les tables**.

Vous ne pouvez pas simplement **supprimer la publication sans d'abord supprimer les commentaires** car vous aurez alors un tas de commentaires dans votre base de données avec une **clé étrangère post id** inexistante. 

Voici un exemple montrant comment supprimer un utilisateur et ses publications et commentaires. 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-167.png)

### Shell PSQL

Ouvrons le **shell PSQL** et entrons ces commandes que nous venons de créer ici dans notre fichier `schema.sql`. Ce **shell PSQL** aurait dû être installé automatiquement lorsque vous avez installé **PSQL**. Si ce n'est pas le cas, allez simplement sur le site **PSQL** pour le télécharger et l'installer à nouveau.

Si vous vous connectez pour la première fois au **shell PSQL**, vous serez invité à définir le serveur, le nom de la base de données, le port, le nom d'utilisateur et le mot de passe. Laissez le port au **port 5432 par défaut** et configurez le reste des identifiants comme vous le souhaitez.

Vous devriez maintenant voir `postgres#` dans le terminal ou ce que vous avez défini comme nom de la base de données. Cela signifie que nous sommes prêts à commencer à entrer des commandes **SQL**. Au lieu d'utiliser la base de données par défaut, créons-en une nouvelle avec la commande `CREATE DATABASE database1` puis connectons-nous à celle-ci avec `\c database1`. Si cela est fait correctement, vous devriez voir `database#`.

Si vous voulez une liste de toutes les commandes, vous pouvez taper `help` ou `\?` dans le **shell PSQL**. N'oubliez jamais de terminer vos requêtes SQL par un `;` qui est l'une des erreurs les plus courantes lorsque vous travaillez avec SQL.

À partir de là, nous pouvons simplement copier et coller nos commandes à partir du fichier `schema.sql`.

Pour voir une liste de nos tables, nous utilisons la commande `\dt` et vous devriez voir ceci dans le terminal.

Et nous avons réussi à configurer la base de données !

Maintenant, nous devons réellement connecter cette **base de données** à notre **serveur**. Faire cela est extrêmement simple. Nous pouvons le faire en utilisant la bibliothèque `pg`. Installez la bibliothèque `pg` si vous ne l'avez pas déjà fait et assurez-vous d'être dans le répertoire Server, nous ne voulons pas installer cette bibliothèque dans notre application React.

Créez un fichier séparé appelé `db.js` dans le **répertoire principal** et configurez-le comme suit :

```javascript
const { Pool } = require('pg')

const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'postgres',
  password: '',
  post: 5432
})

module.exports = pool

```

Ce seront les mêmes identifiants que vous avez définis lors de la configuration du **shell PSQL**.

Et c'est tout, nous avons configuré notre base de données pour une utilisation avec notre serveur. Nous pouvons maintenant commencer à faire des requêtes depuis notre serveur express.

### Configuration des routes Express et des requêtes PSQL

Voici la configuration des routes et des requêtes. Nous avons besoin de nos opérations CRUD de base pour les publications et les commentaires. Toutes ces valeurs proviendront de notre frontend React que nous configurerons ensuite. 

```javascript
var express = require('express')
var router = express.Router()
var pool = require('./db')


/*
    SECTION DES ROUTES DES PUBLICATIONS
*/

router.get('/api/get/allposts', (req, res, next ) => {
  pool.query(`SELECT * FROM posts 
              ORDER BY date_created DESC`, 
            (q_err, q_res) => {
                  res.json(q_res.rows)
  })
})

router.get('/api/get/post', (req, res, next) => {
  const post_id = req.query.post_id

  pool.query(`SELECT * FROM posts
              WHERE pid=$1`,
            [ post_id ], (q_err, q_res) => {
                res.json(q_res.rows)
      })
} )


router.post('/api/post/posttodb', (req, res, next) => {
  const values = [ req.body.title, 
                   req.body.body,
                   req.body.uid, 
                   req.body.username]
  pool.query(`INSERT INTO posts(title, body, user_id, author, date_created)
              VALUES($1, $2, $3, $4, NOW() )`,
           values, (q_err, q_res) => {
          if(q_err) return next(q_err);
          res.json(q_res.rows)
    })
})

router.put('/api/put/post', (req, res, next) => {
  const values = [ req.body.title,
                   req.body.body, 
                   req.body.uid, 
                   req.body.pid, 
                   req.body.username]
  pool.query(`UPDATE posts SET title= $1, body=$2, user_id=$3, author=$5, date_created=NOW()
              WHERE pid = $4`, values,
              (q_err, q_res) => {
                console.log(q_res)
                console.log(q_err)
        })
})

router.delete('/api/delete/postcomments', (req, res, next) => {
  const post_id = req.body.post_id
  pool.query(`DELETE FROM comments
              WHERE post_id = $1`, [post_id],
              (q_err, q_res) => {
                  res.json(q_res.rows)
                  console.log(q_err)
        })
})

router.delete('/api/delete/post', (req, res, next) => {
  const post_id = req.body.post_id
  pool.query(`DELETE FROM posts WHERE pid = $1`, [ post_id ],
              (q_err, q_res) => {
                res.json(q_res.rows)
                console.log(q_err)
       })
})

router.put('/api/put/likes', (req, res, next) => {
  const uid = [req.body.uid]
  const post_id = String(req.body.post_id)

  const values = [ uid, post_id ]
  console.log(values)
  pool.query(`UPDATE posts
              SET like_user_id = like_user_id || $1, likes = likes + 1
              WHERE NOT (like_user_id @> $1)
              AND pid = ($2)`,
     values, (q_err, q_res) => {
    if (q_err) return next(q_err);
    console.log(q_res)
    res.json(q_res.rows);
  });
});

/*
    SECTION DES ROUTES DES COMMENTAIRES
*/


router.post('/api/post/commenttodb', (req, res, next) => {
  const values = [ req.body.comment, 
    req.body.user_id, 
    req.body.username, 
    req.body.post_id]

  pool.query(`INSERT INTO comments(comment, user_id, author, post_id, date_created)
              VALUES($1, $2, $3, $4, NOW())`, values,
              (q_err, q_res ) => {
                  res.json(q_res.rows)
                  console.log(q_err)
      })
})

router.put('/api/put/commenttodb', (req, res, next) => {
  const values = [ req.body.comment,
                   req.body.user_id, 
                   req.body.post_id, 
                   req.body.username, 
                   req.body.cid]

  pool.query(`UPDATE comments SET comment = $1, user_id = $2, post_id = $3, author = $4, date_created=NOW()
              WHERE cid=$5`, values,
              (q_err, q_res ) => {
                  res.json(q_res.rows)
                  console.log(q_err)
      })
})


router.delete('/api/delete/comment', (req, res, next) => {
  const cid = req.body.comment_id
  console.log(cid)
  pool.query(`DELETE FROM comments
              WHERE cid=$1`, [ cid ],
              (q_err, q_res ) => {
                  res.json(q_res)
                  console.log(q_err)
      })
})


router.get('/api/get/allpostcomments', (req, res, next) => {
  const post_id = String(req.query.post_id)
  pool.query(`SELECT * FROM comments
              WHERE post_id=$1`, [ post_id ],
              (q_err, q_res ) => {
                  res.json(q_res.rows)
      })
})

/*
  SECTION DU PROFIL UTILISATEUR
*/

router.post('/api/posts/userprofiletodb', (req, res, next) => {
  const values = [req.body.profile.nickname, 
                  req.body.profile.email, 
                  req.body.profile.email_verified]
  pool.query(`INSERT INTO users(username, email, email_verified, date_created)
              VALUES($1, $2, $3, NOW())
              ON CONFLICT DO NOTHING`, values,
              (q_err, q_res) => {
                res.json(q_res.rows)
      })
} )

router.get('/api/get/userprofilefromdb', (req, res, next) => {
  const email = req.query.email
  console.log(email)
  pool.query(`SELECT * FROM users
              WHERE email=$1`, [ email ],
              (q_err, q_res) => {
                res.json(q_res.rows)
      })
} )


router.get('/api/get/userposts', (req, res, next) => {
  const user_id = req.query.user_id
  console.log(user_id)
  pool.query(`SELECT * FROM posts
              WHERE user_id=$1`, [ user_id ],
              (q_err, q_res) => {
                res.json(q_res.rows)
      })
} )

// Récupérer le profil d'un autre utilisateur de la base de données en fonction du nom d'utilisateur 
router.get('/api/get/otheruserprofilefromdb', (req, res, next) => {
  // const email = [ "%" + req.query.email + "%"]
  const username = String(req.query.username)
  pool.query(`SELECT * FROM users
              WHERE username = $1`,
    [ username ], (q_err, q_res) => {
    res.json(q_res.rows)
  });
});

// Obtenir les publications d'un autre utilisateur en fonction du nom d'utilisateur
router.get('/api/get/otheruserposts', (req, res, next) => {
  const username = String(req.query.username)
  pool.query(`SELECT * FROM posts
              WHERE author = $1`,
    [ username ], (q_err, q_res) => {
    res.json(q_res.rows)
  });
});

module.exports = router
```

**Commandes SQL**

`SELECT * FROM table` : Comment nous obtenons des données de la base de données. Retourne toutes les lignes d'une table.

`INSERT INTO table(column1, column2)` : Comment nous sauvegardons des données et ajoutons des lignes à la base de données.  

`UPDATE table SET column1 =$1, column2 = $2` : comment mettre à jour ou modifier des lignes existantes dans une base de données. La clause `WHERE` spécifie quelles lignes mettre à jour. 

`DELETE FROM table` : supprime des lignes en fonction des conditions de la clause `WHERE`. **ATTENTION** : ne pas inclure une clause `WHERE` supprime toute la table. 

`WHERE` clause : Une instruction conditionnelle optionnelle à ajouter aux requêtes. Cela fonctionne de manière similaire à une instruction `if` en javascript.

`WHERE (array @> value)` : Si la valeur est contenue dans le tableau. 

### Routes Express

Pour configurer les **routes express**, nous utilisons d'abord l'objet `router` que nous avons défini en haut avec `express.Router()`. Ensuite, la **méthode http** que nous voulons, qui peut être les méthodes standard telles que **GET, POST, PUT**, etc. 

Ensuite, entre parenthèses, nous passons d'abord la chaîne de la **route** que nous voulons et le deuxième argument est une fonction à exécuter lorsque la **route** est appelée depuis le **client**. **Express** écoute automatiquement ces appels de route depuis le **client**. Lorsque les **routes** correspondent, la fonction dans le corps est appelée, ce qui dans notre cas se trouve être des **requêtes PSQL**.

Nous pouvons également passer des paramètres à l'intérieur de notre appel de fonction. Nous utilisons **req, res** et **next**. 

**req** : est l'abréviation de request et contient les données de la requête de notre client. C'est essentiellement ainsi que nous obtenons les données de notre front-end vers notre serveur. **Les données de notre front-end React sont contenues dans cet objet req** et nous l'utilisons ici dans nos **routes** de manière extensive pour accéder aux valeurs. Les données seront fournies à axios en tant que paramètre sous forme d'objet javascript.  
Pour les requêtes **GET** avec un paramètre optionnel, les données seront disponibles avec **req.query**. Pour les requêtes **PUT, POST et DELETE**, les données seront disponibles directement dans le corps de la requête avec **req.body**. Les données seront un objet javascript et chaque propriété peut être accessible avec la notation par points régulière. 

**res** : est l'abréviation de response et contient la **réponse du serveur express**. Nous voulons envoyer la réponse que nous obtenons de notre **base de données** au **client**, donc nous passons la réponse de la base de données à cette fonction res qui l'envoie ensuite à notre client. 

**next** : est un middleware qui vous permet de passer des rappels à la fonction suivante.

Remarquez à l'intérieur de notre **route express** que nous faisons `pool.query` et que cet objet `pool` est le même que celui qui contient nos **identifiants de connexion à la base de données** que nous avons configurés précédemment et importés en haut. La **fonction query** nous permet de faire des **requêtes SQL** à notre base de données au format chaîne. Remarquez également que j'utilise `` et non des guillemets, ce qui me permet d'avoir ma requête sur plusieurs lignes. 

Ensuite, nous avons une virgule après notre **requête SQL** et le paramètre suivant qui est une fonction fléchée à exécuter après l'exécution de la **requête**. Nous passons d'abord 2 paramètres à notre fonction fléchée, `q_err` et `q_res` signifiant l'**erreur de requête** et la **réponse de requête**. Pour envoyer des données au **frontend**, nous passons `q_res.rows` à la fonction `res.json`. `q_res.rows` est la réponse de la base de données puisque c'est SQL et la base de données nous renverra des lignes correspondantes en fonction de notre requête. Nous convertissons ensuite ces **lignes** en **format json** et les envoyons à notre **frontend** avec le paramètre `res`.

Nous pouvons également passer des valeurs optionnelles à nos **requêtes SQL** en passant un **tableau** après la **requête** séparé par une virgule. Ensuite, nous pouvons accéder aux éléments individuels de ce **tableau** dans la **requête SQL** avec la syntaxe `$1` où `$1` est le **premier élément** du tableau. `$2` accéderait au **deuxième élément** du tableau et ainsi de suite. Notez que ce n'est pas un système basé sur 0 comme en javascript, il n'y a pas de `$0`

Décomposons chacune de ces routes et donnons une brève description de chacune. 

**Routes des publications** 

* **/api/get/allposts** : récupère toutes nos publications de la base de données. `ORDER BY date_created DESC` nous permet d'avoir les nouvelles publications affichées en premier.
* **/api/post/posttodb** : Enregistre une publication d'utilisateur dans la base de données. Nous enregistrons les 4 valeurs dont nous avons besoin : titre, corps, identifiant utilisateur, nom d'utilisateur dans un tableau de valeurs. 
* **/api/put/post** : Modifie une publication existante dans la base de données. Nous utilisons la commande SQL `UPDATE` et passons toutes les valeurs de la publication à nouveau. Nous recherchons la publication avec l'identifiant de la publication que nous obtenons de notre front-end.
* **/api/delete/postcomments** : Supprime tous les commentaires associés à une publication. En raison de la **contrainte de clé étrangère de PSQL**, nous devons supprimer tous les commentaires associés à la publication avant de pouvoir supprimer la publication elle-même. 
* **/api/delete/post** : Supprime une publication avec l'identifiant de la publication.
* **/api/put/likes** : Nous faisons une requête put pour ajouter l'identifiant utilisateur de l'utilisateur qui a aimé la publication au tableau `like_user_id`, puis nous augmentons le compteur de `likes` de 1. 

**Routes des commentaires** 

* **/api/post/commenttodb** : Enregistre un commentaire dans la base de données
* **/api/put/commenttodb** : modifie un commentaire existant dans la base de données
* **/api/delete/comment** : Supprime un seul commentaire, cela est différent de la suppression de tous les commentaires associés à une publication.
* **/api/get/allpostcomments** : Récupère tous les commentaires associés à une seule publication

**Routes des utilisateurs** 

* **/api/posts/userprofiletodb** : Enregistre les données de profil utilisateur d'auth0 dans notre propre base de données. Si l'utilisateur existe déjà, PostgreSQL ne fait rien.
* **/api/get/userprofilefromdb** : Récupère un utilisateur en recherchant son email
* **/api/get/userposts** : récupère les publications faites par un utilisateur en recherchant toutes les publications qui correspondent à son identifiant utilisateur.
* **/api/get/otheruserprofilefromdb** : obtenir les données de profil d'un autre utilisateur à partir de la base de données et les afficher sur leur page de profil. 
* **/api/get/otheruserposts** : Obtenir les publications d'un autre utilisateur lorsque vous consultez sa page de profil   


## Configuration de l'état global avec les réducteurs, les actions et le contexte. 

###   
Enregistrement des données de profil utilisateur dans notre base de données

Avant de pouvoir commencer à configurer l'état global, nous avons besoin d'un moyen d'enregistrer les données de profil utilisateur dans notre propre base de données, actuellement nous obtenons simplement nos données d'auth0. Nous allons faire cela dans notre composant `authcheck.js`. 

```jsx
import React, { useEffect, useContext } from 'react';
import history from './history';
import Context from './context';

import axios from 'axios';

const AuthCheck = () => {
  const context = useContext(Context)

  useEffect(() => {
    if(context.authObj.isAuthenticated()) {
      const profile = context.authObj.userProfile
      context.handleUserLogin()
      context.handleUserAddProfile(profile)
       axios.post('/api/posts/userprofiletodb', profile )
        .then(axios.get('/api/get/userprofilefromdb',
        		{params: {email: profile.profile.email}})
          .then(res => context.handleAddDBProfile(res.data)) )
        .then(history.replace('/') )
    }
    else {
      context.handleUserLogout()
      context.handleUserRemoveProfile()
      context.handleUserRemoveProfile()
      history.replace('/')
      }
    }, [context.authObj.userProfile, context])

    return(
        <div>
        </div>
)}

export default AuthCheck;
```

Nous avons configuré la plupart de ce composant dans le dernier tutoriel, je recommande donc de consulter ce tutoriel pour une explication détaillée, mais ici nous faisons une **requête post axios** suivie immédiatement d'une autre **requête get axios** pour obtenir immédiatement les données de profil utilisateur que nous venons d'enregistrer dans la base de données. 

Nous faisons cela parce que nous avons besoin de l'identifiant unique de la clé primaire généré par notre base de données et cela **nous permet d'associer cet utilisateur à ses commentaires et publications**. Et nous utilisons l'email de l'utilisateur pour le rechercher puisque nous ne savons pas quel est son identifiant unique lorsqu'il s'inscrit pour la première fois. Enfin, nous enregistrons ces données de profil utilisateur de la base de données dans notre état global. 

*Notez que cela s'applique également aux connexions OAuth telles que les connexions Google et Facebook. 

### Actions et réducteurs

Nous pouvons maintenant commencer à configurer les actions et les réducteurs ainsi que le contexte pour configurer l'état global de cette application. 

Pour configurer le contexte à partir de zéro, voir mon tutoriel précédent. Ici, nous n'aurons besoin d'état que pour le profil de la base de données et tous les messages.

Tout d'abord, nos types d'actions

```javascript
export const SET_DB_PROFILE = "SET_DB_PROFILE"

export const REMOVE_DB_PROFILE = "REMOVE_DB_PROFILE"

export const FETCH_DB_POSTS = "FETCH_DB_POSTS"

export const REMOVE_DB_POSTS = "REMOVE_DB_POSTS"
```

Maintenant, nos actions

```javascript

export const set_db_profile = (profile) => {
  return {
    type: ACTION_TYPES.SET_DB_PROFILE,
    payload: profile
  }
}

export const remove_db_profile = () => {
  return {
    type: ACTION_TYPES.REMOVE_DB_PROFILE
  }
}

export const set_db_posts = (posts) => {
  return {
    type: ACTION_TYPES.FETCH_DB_POSTS,
    payload: posts
  }
}

export const remove_db_posts = () => {
  return {
    type: ACTION_TYPES.REMOVE_DB_POSTS
  }
}

```

Enfin, notre réducteur de messages et notre réducteur d'authentification

```javascript
import * as ACTION_TYPES from '../actions/action_types'

export const initialState = {
  posts: null,
}

export const PostsReducer = (state = initialState, action) => {
    switch(action.type) {
      case ACTION_TYPES.FETCH_DB_POSTS:
        return {
          ...state,
          posts: action.payload
        }
      case ACTION_TYPES.REMOVE_DB_POSTS:
        return {
          ...state,
          posts: []
        }

      default:
        return state
    }
}
```



```javascript
import * as ACTION_TYPES from '../actions/action_types'

export const initialState = {
  is_authenticated: false,
  db_profile: null,
  profile: null,
}

export const AuthReducer = (state = initialState, action) => {
    switch(action.type) {
      case ACTION_TYPES.LOGIN_SUCCESS:
        return {
          ...state,
          is_authenticated: true
        }
      case ACTION_TYPES.LOGIN_FAILURE:
        return {
          ...state,
          is_authenticated: false
        }
        case ACTION_TYPES.ADD_PROFILE:
          return {
            ...state,
            profile: action.payload
          }
        case ACTION_TYPES.REMOVE_PROFILE:
          return {
            ...state,
            profile: null
          }
        case ACTION_TYPES.SET_DB_PROFILE:
          return {
            ...state,
            db_profile: action.payload
          }
        case ACTION_TYPES.REMOVE_DB_PROFILE:
          return {
            ...state,
            db_profile: null
          }
      default:
        return state
    }
}
```

Maintenant, nous devons ajouter ceux-ci au `<Context.Provider />`  

```jsx


...

    /*
      Réducteur de messages
    */

    const [statePosts, dispatchPosts] =  useReducer(PostsReducer.PostsReducer,                                                         PostsReducer.initialState)


    const handleSetPosts = (posts) => {
      dispatchPosts(ACTIONS.set_db_posts(posts) )
    }

    const handleRemovePosts = () => {
      dispatchPosts(ACTIONS.remove_db_posts() )
    }
  ...
  
  
      /*
      Réducteur d'authentification
    */
    const [stateAuth, dispatchAuth] = useReducer(AuthReducer.AuthReducer,
                                                               AuthReducer.initialState)



    const handleDBProfile = (profile) => {
      dispatchAuth(ACTIONS.set_db_profile(profile))
    }

    const handleRemoveDBProfile = () => {
      dispatchAuth(ACTIONS.remove_db_profile())
    }
    
  ...
  
  <Context.Provider
          value={{
          	...
          
            dbProfileState: stateAuthReducer.db_profile,

            handleAddDBProfile: (profile) => handleDBProfile(profile),
            handleRemoveDBProfile: () => handleRemoveDBProfile(),
                     
            // État des messages
            postsState: statePostsReducer.posts,
            handleAddPosts: (posts) => handleSetPosts(posts),
            handleRemovePosts: () => handleRemovePosts(),

            ...
          }}>
   ...
```

C'est tout, nous sommes maintenant prêts à utiliser cet état global dans nos composants. 

## Application React côté client

Ensuite, nous allons configurer le blog React côté client. Tous les appels API de cette section ont été configurés dans la section précédente sur les routes Express.

Il sera configuré en 6 composants comme suit.

**addpost.js** : Un composant avec un formulaire pour soumettre des publications.

**editpost.js** : Un composant pour modifier des publications avec un formulaire qui a des champs déjà remplis.

**posts.js** : Un composant pour rendre toutes les publications, comme dans un forum typique.

**showpost.js** : Un composant pour rendre une publication individuelle après qu'un utilisateur a cliqué sur une publication.

**profile.js** : Un composant qui rend les publications associées à un utilisateur. Le tableau de bord de l'utilisateur.

**showuser.js** : Un composant qui montre les données de profil et les publications d'un autre utilisateur. 

### **Pourquoi ne pas utiliser Redux Form ?**

**TDLR;** Redux Form est excessif pour la plupart des cas d'utilisation.

Redux Form est une bibliothèque populaire couramment utilisée dans les applications React. Alors pourquoi ne pas l'utiliser ici ? J'ai essayé Redux Form, mais je n'ai simplement pas trouvé de cas d'utilisation pour cela ici. Nous devons toujours garder à l'esprit l'utilisation finale, et je n'ai pas pu imaginer un scénario pour cette application où nous aurions besoin d'enregistrer les données du formulaire dans l'état global de redux. 

Dans cette application, nous prenons simplement les données d'un formulaire régulier et les passons à Axios qui les passe ensuite au serveur express qui les enregistre enfin dans la base de données. L'autre cas d'utilisation possible est pour un composant editpost, que je gère en passant les données de la publication à une propriété de l'élément Link. 

Essayez Redux Form et voyez si vous pouvez trouver une utilisation astucieuse pour cela, mais nous n'en aurons pas besoin dans cette application. De plus, toute fonctionnalité offerte par Redux Form peut être accomplie relativement plus facilement sans celui-ci.

Redux form est simplement excessif pour la plupart des cas d'utilisation.

Comme avec un ORM, il n'y a aucune raison d'ajouter une autre couche de complexité inutile à notre application.

Il est simplement plus facile de configurer des formulaires avec React régulier.

### addpost.js

```jsx
import React, { useContext} from 'react';
import axios from 'axios';

import history from '../utils/history';
import Context from '../utils/context';
import TextField from '@material-ui/core/TextField';



const AddPost = () => {
  const context = useContext(Context)

  const handleSubmit = (event) => {
    event.preventDefault()
    const user_id = context.dbProfileState[0].uid
    const username = context.dbProfileState[0].username
    const data = {title: event.target.title.value,
                  body: event.target.body.value,
                  username: username,
                  uid: user_id}

    axios.post('/api/post/posttodb', data)
      .then(response => console.log(response))
      .catch((err) => console.log(err))
      .then(setTimeout(() => history.replace('/'), 700) )
  }


    return(
      <div>
        <form onSubmit={handleSubmit}>
          <TextField
            id='title'
            label='Title'
            margin='normal'
            />
          <br />
          <TextField
            id='body'
            label='Body'
            multiline
            rowsMax='4'
            margin="normal"
            />
           <br />
           <button type='submit'> Submit </button>
           </form>
        <br />
        <button onClick={() => history.replace('/posts')}> Cancel </button>
      </div>
  )}



export default AddPost;
```

Dans le composant addpost, nous avons un formulaire simple à 2 champs où un utilisateur peut entrer un titre et un corps. Le formulaire est soumis en utilisant la fonction `handlesubmit()` que nous avons créée. La fonction `handleSubmit()` prend un paramètre de mot-clé d'événement qui contient les données de formulaire soumises par l'utilisateur. 

Nous utiliserons `event.preventDefault()` pour empêcher la page de se recharger puisque React est une application à page unique et que cela serait inutile. 

La méthode **axios post** prend un paramètre de "data" qui sera utilisé pour contenir les données qui seront stockées dans la base de données. Nous obtenons le **username** et le **user_id** de l'état global dont nous avons parlé dans la dernière section. 

L'envoi réel des données à la base de données est géré dans la fonction **express routes** avec des requêtes SQL que nous avons vues auparavant. Notre **appel API axios** transmet ensuite les données à notre serveur express qui enregistrera les informations dans la base de données.

### editpost.js

Ensuite, nous avons notre composant `editpost.js`. Cela sera un composant de base pour modifier les publications des utilisateurs. Il ne sera accessible que via la page de profil de l'utilisateur. 

```jsx
import React, { useContext, useState } from 'react';
import axios from 'axios';
import history from '../utils/history';
import Context from '../utils/context';

import TextField from '@material-ui/core/TextField';
import Button from "@material-ui/core/Button";




const EditPost = (props) => {
  const context = useContext(Context)

  const [stateLocal, setState] = useState({ title: props.location.state.post.post.title,
                                            body: props.location.state.post.post.body
                                          })


  const handleTitleChange = (event) => {
    setState({...stateLocal, title: event.target.value })
  }

  const handleBodyChange = (event) => {
    setState({...stateLocal, body: event.target.value })
  }

  const handleSubmit = (event) => {
    event.preventDefault()

    const user_id = context.dbProfileState[0].uid
    const username = context.dbProfileState[0].username
    const pid = props.location.state.post.post.pid
    const title = event.target.title.value
    const body = event.target.body.value

    const data = {title: title,
                  body: body,
                  pid: pid,
                  uid: user_id,
                  username: username
                 }
    axios.put("/api/put/post", data)
      .then(res => console.log(res))
      .catch(err => console.log(err))
      .then(setTimeout(() => history.replace('/profile'), 700 ))
  }


    return(
        <div>
          <form onSubmit={handleSubmit}>
            <TextField
              id='title'
              label='title'
              margin="normal"
              value={stateLocal.title}
              onChange={handleTitleChange}
            />
            <br />
            <TextField
              id='body'
              label='body'
              multiline
              rows="4"
              margin='normal'
              value={stateLocal.body}
              onChange={handleBodyChange}
              />
          <br />
          <button type="submit"> Submit </button>
          </form>
          <br />
          <Button onClick={() => history.goBack()}> Cancel </Button>
        </div>
    )}



export default EditPost;
```

`props.location.state.posts.posts.title` : est une fonctionnalité offerte par **react-router**. Lorsqu'un utilisateur clique sur une publication depuis sa page de profil, les données de la publication sur laquelle il a cliqué sont enregistrées dans une propriété d'état dans l'élément de lien et cela est **différent de l'état local du composant** dans React provenant du hook `useState`. 

Cette approche nous offre un moyen plus facile d'enregistrer les données par rapport au contexte et nous évite également une requête API. Nous verrons comment cela fonctionne dans le composant `profile.js`. 

Après cela, nous avons un formulaire de composant contrôlé de base et nous enregistrons les données à chaque frappe dans l'état React. 

Dans notre fonction `handleSubmit()`, nous combinons toutes nos données avant de les envoyer à notre serveur dans une requête put axios.  

### posts.js

```jsx
import React, { useContext, useEffect, useState } from 'react';

import { Link } from 'react-router-dom';

import axios from 'axios';
import moment from 'moment';
import Context from '../utils/context';

import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';

import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CardHeader from "@material-ui/core/CardHeader";

import '../App.css';
import '../styles/pagination.css';




const Posts = (props) => {
  const context = useContext(Context)


  const [stateLocal, setState] = useState({ posts: [],
                                            fetched: false,
                                            first_page_load: false,
                                            pages_slice: [1, 2, 3, 4, 5],
                                            max_page: null,
                                            items_per_page: 3,

                                            currentPage: 1,
                                            num_posts: null,
                                            posts_slice: null,
                                            posts_search: [],
                                            posts_per_page: 3
                                        })


    useEffect(() => {
     if(!context.postsState) {
        axios.get('/api/get/allposts')
          .then(res => context.handleAddPosts(res.data) )
          .catch((err) => console.log(err))
        }
      if (context.postsState && !stateLocal.fetched) {
        const indexOfLastPost = 1 * stateLocal.posts_per_page
        const indexOfFirstPost = indexOfLastPost - stateLocal.posts_per_page
        const last_page = Math.ceil(context.postsState.length/stateLocal.posts_per_page)

        setState({...stateLocal,
                  fetched: true,
                  posts: [...context.postsState],
                  num_posts: context.postsState.length,
                  max_page: last_page,
                  posts_slice: context.postsState.slice(indexOfFirstPost,
                                                        indexOfLastPost)
                  })
        }
      }, [context, stateLocal])


    useEffect(() => {
      let page = stateLocal.currentPage
      let indexOfLastPost = page * 3;
      let indexOfFirstPost = indexOfLastPost - 3;

      setState({...stateLocal,
                posts_slice: stateLocal.posts.slice(indexOfFirstPost,
                                                    indexOfLastPost) })
    }, [stateLocal.currentPage]) //eslint-disable-line




   const add_search_posts_to_state = (posts) => {
      setState({...stateLocal, posts_search: []});
      setState({...stateLocal, posts_search: [...posts]});
   }


  const handleSearch = (event) => {
     setState({...stateLocal, posts_search: []});
     const search_query = event.target.value
     axios.get('/api/get/searchpost', {params: {search_query: search_query} })
       .then(res => res.data.length !== 0
                      ? add_search_posts_to_state(res.data)
                      : null )
       .catch(function (error) {
         console.log(error);
         })
     }



  const RenderPosts = post => (
    <div >
    <Card >
      <CardHeader
        title={<Link to={{pathname:'/post/' + post.post.pid, state: {post}}}>
                  {post.post.title}
                </Link> }
        subheader={
            <div className="FlexColumn">
              <div className="FlexRow">
              {  moment(post.post.date_created).format('MMMM Do, YYYY | h:mm a') }
              </div>
              <div className="FlexRow">
                By:
                <Link style={{paddingLeft: '5px', textDecoration: 'none'}}
                      to={{pathname:"/user/" + post.post.author, state:{post} }}>
                 { post.post.author }
                 </Link>
               </div>
               <div className="FlexRow">
                <i className="material-icons">thumb_up</i>
                <div className="notification-num-allposts"> {post.post.likes} </div>
              </div>
            </div>
            }
          />
      <br />
      <CardContent>
        <span style={{overflow: 'hidden' }}> {post.post.body} </span>
      </CardContent>
    </Card>
    </div>
  )

  const page_change = (page) => {
    window.scrollTo({top:0, left: 0, behavior: 'smooth'})

    //variables pour le changement de page
    let next_page = page + 1
    let prev_page = page - 1

    //gère le changement de page général
    //if(state.max_page < 5 return null)
    if(page > 2 && page < stateLocal.max_page - 1) {
      setState({...stateLocal,
                currentPage: page,
                pages_slice: [prev_page - 1,
                              prev_page,
                              page,
                              next_page,
                              next_page + 1],
              })
     }
     if(page === 2 ) {
       setState({...stateLocal,
                currentPage: page,
                 pages_slice: [prev_page,
                               page,
                               next_page,
                               next_page + 1,
                               next_page + 2],
               })
      }
     //gère le cas d'utilisation pour que l'utilisateur revienne à la première page depuis une autre page
     if(page === 1) {
       setState({...stateLocal,
                currentPage: page,
                 pages_slice: [page,
                               next_page,
                               next_page + 1,
                               next_page + 2,
                               next_page + 3],
            })
     }
     //gère le changement de dernière page
     if(page === stateLocal.max_page) {
       setState({...stateLocal,
                 currentPage: page,
                 pages_slice: [prev_page - 3,
                               prev_page - 2,
                               prev_page - 1,
                               prev_page,
                               page],
               })
     }
     if(page === stateLocal.max_page - 1) {
       setState({...stateLocal,
                 currentPage: page,
                 pages_slice: [prev_page - 2,
                               prev_page - 1,
                               prev_page,
                               page,
                               next_page],
               })
     }
   }



  return(
      <div>
      <div style={{opacity: stateLocal.opacity, transition: 'opacity 2s ease'}}>
      <br />
      { context.authState
        ?  <Link to="/addpost">
              <Button variant="contained" color="primary">
                Add Post
              </Button>
            </Link>
        : <Link to="/signup">
              <Button variant="contained" color="primary">
                Sign Up to Add Post
              </Button>
            </Link>
          }
      </div>
      <br />
      <TextField
        id="search"
        label="Search"
        margin="normal"
        onChange={handleSearch}
      />
      <hr />
       
       <br />
       <div>
         {stateLocal.posts_search
           ? stateLocal.posts_search.map(post =>
             <RenderPosts key={post.pid + 1000} post={post} />
            )
            : null
          }
        </div>

      <h1>Posts</h1>
        <div>
          {stateLocal.posts_slice
            ? stateLocal.posts_slice.map(post =>
              <RenderPosts key={post.pid} post={post} />
             )
            : null
           }
        </div>
        <div>
            <div className="FlexRow">
                <button onClick={() => page_change(1) }> First </button>
                <button onClick={() => page_change(stateLocal.currentPage - 1) }> Prev </button>
                   {stateLocal.pages_slice.map((page) =>
                       <div
                         onClick={() => page_change(page)}
                         className={stateLocal.currentPage === page
                                       ? "pagination-active"
                                       : "pagination-item" }
                         key={page}>
                           {page}
                        </div>
                   )}
                 <button onClick={() => page_change(stateLocal.currentPage + 1)}> Next </button>
                 <button onClick={() => page_change(stateLocal.max_page)}> Last </button>
               </div>
         </div>
      </div>
  )}


export default Posts;
```

Vous remarquerez que nous avons un appel `useEffect()` assez complexe pour obtenir nos publications de notre base de données. Cela est dû au fait que nous sauvegardons nos publications de notre base de données dans l'état global, afin que les publications soient toujours là même si un utilisateur navigue vers une autre page. 

Faire cela évite des appels API inutiles à notre serveur. C'est pourquoi nous utilisons une condition pour vérifier si les publications sont déjà sauvegardées dans l'état du contexte.

Si les publications sont déjà sauvegardées dans l'état global, nous définissons simplement les publications dans l'état global à notre état local, ce qui nous permet d'initialiser la pagination.   

**Pagination**   
Nous avons une implémentation de pagination de base ici dans la fonction `page_change()`. Nous avons essentiellement nos 5 blocs de pagination configurés sous forme de tableau. Lorsque la page change, le tableau est mis à jour avec les nouvelles valeurs. Cela est visible dans la première instruction `if` de la fonction `page_change()`, les 4 autres instructions `if` ne servent qu'à gérer les changements de page des 2 premières et des 2 dernières pages. 

Nous devons également appeler `window.scrollTo()` pour faire défiler vers le haut à chaque changement de page. 

Lancez-vous le défi de voir si vous pouvez construire une implémentation de pagination plus complexe, mais pour nos besoins, cette seule fonction ici pour la pagination est suffisante. 

Nous avons besoin de 4 valeurs d'état pour notre pagination. Nous avons besoin de : 

* `num_posts` : nombre de publications
* `posts_slice` : une partie des publications totales 
* `currentPage` : la page actuelle
* `posts_per_page` : Le nombre de publications sur chaque page. 

Nous devons également passer la valeur d'état `currentPage` au hook `useEffect()`, cela nous permet de déclencher une fonction à chaque changement de page. Nous obtenons `indexOfLastPost` en multipliant 3 par `currentPage` et obtenons le premier message que nous voulons afficher en soustrayant 3. Nous pouvons ensuite définir ce nouveau tableau découpé comme le nouveau tableau dans notre état local. 

Maintenant pour notre JSX. Nous utilisons **flexbox** pour structurer et disposer nos blocs de pagination au lieu des listes horizontales habituelles qui sont traditionnellement utilisées. 

Nous avons 4 boutons qui vous permettent d'aller à la toute première page ou de revenir en arrière d'une page et vice-versa. Ensuite, nous utilisons une instruction map sur notre tableau `pages_slice` qui nous donne les valeurs pour nos blocs de pagination. Un utilisateur peut également cliquer sur un bloc de pagination qui passera la page en argument à la fonction `page_change()`. 

Nous avons également des classes **CSS** qui nous permettent de définir le style de notre pagination.  

* `.pagination-active` : il s'agit d'une classe CSS régulière au lieu d'un sélecteur pseudo que vous voyez généralement avec des listes horizontales telles que `.item:active`. Nous basculons la classe active dans le JSX React en comparant `currentPage` avec la page dans le tableau `pages_slice`. 
* `.pagination-item` : style pour tous les blocs de pagination 
* `.pagination-item:hover` : style à appliquer lorsque l'utilisateur survole un bloc de pagination

```jsx
          <div className="FlexRow">
                <button onClick={() => page_change(1) }> First </button>
                <button onClick={() => page_change(stateLocal.currentPage - 1)  }>
                	Prev 
                </button>
                   {stateLocal.pages_slice.map((page) =>
                       <div
                         onClick={() => page_change(page)}
                         className={stateLocal.currentPage === page
                                       ? "pagination-active"
                                       : "pagination-item" }
                         key={page}>
                           {page}
                        </div>
                   )}
                 <button onClick={() => page_change(stateLocal.currentPage + 1)}> Next </button>
                 <button onClick={() => page_change(stateLocal.max_page)}> Last </button>
               </div>
```

```css

.pagination-active {
  background-color: blue;
  cursor: pointer;
  color: white;
  padding: 10px 15px;
  border: 1px solid #ddd; /* Gray */
}

.pagination-item {
  cursor: pointer;
  border: 1px solid #ddd; /* Gray */
  padding: 10px 15px;
}

.pagination-item:hover {
  background-color: #ddd
}
```

**RenderPosts**  
`<RenderPosts />` est le composant fonctionnel que nous utilisons pour rendre chaque publication individuelle. Le titre des publications est un `Link` qui, lorsqu'il est cliqué, amènera un utilisateur à chaque publication individuelle avec des commentaires. De plus, vous remarquerez que nous passons toute la publication à la propriété `state` de l'élément `Link`. Cette propriété `state` est différente de notre état local, il s'agit en fait d'une propriété de `react-router` et nous verrons cela plus en détail dans le composant `showpost.js`. Nous faisons de même avec l'auteur de la publication également. 

Vous remarquerez également quelques autres choses liées à la recherche de publications que je discuterai dans les sections suivantes.  

Je discuterai également de la fonctionnalité "likes" dans le composant `showpost.js`. 

### showpost.js

Maintenant, voici de loin le composant le plus complexe de cette application. Ne vous inquiétez pas, je vais le décomposer complètement étape par étape, ce n'est pas aussi intimidant que cela en a l'air.  

```jsx
import React, { useContext, useState, useEffect } from 'react';


import { Link } from 'react-router-dom';
import axios from 'axios';
import history from '../utils/history';
import Context from '../utils/context';

import TextField from '@material-ui/core/TextField';

import Button from '@material-ui/core/Button';




const ShowPost = (props) => {
  const context = useContext(Context)

  const [stateLocal, setState] = useState({ comment: '',
                                            fetched: false,
                                            cid: 0,
                                            delete_comment_id: 0,
                                            edit_comment_id: 0,
                                            edit_comment: '',
                                            comments_arr: null,
                                            cur_user_id: null,
                                            like_post: true,
                                            likes: 0,
                                            like_user_ids: [],
                                            post_title: null,
                                            post_body: null,
                                            post_author: null,
                                            post_id: null
                                           })



    useEffect(() => {
      if(props.location.state && !stateLocal.fetched) {
        
        setState({...stateLocal,
                  fetched: true,
                  likes: props.location.state.post.post.likes,
                  like_user_ids: props.location.state.post.post.like_user_id,
                  post_title: props.location.state.post.post.title,
                  post_body: props.location.state.post.post.body,
                  post_author: props.location.state.post.post.author,
                  post_id: props.location.state.post.post.pid})
        }
      }, [stateLocal,
          props.location])

  useEffect( () => {
    if(!props.location.state && !stateLocal.fetched) {
      
      const post_id = props.location.pathname.substring(6)

      axios.get('/api/get/post',
                  {params: {post_id: post_id}} )
        .then(res => res.data.length !== 0
                ?   setState({...stateLocal,
                        fetched: true,
                        likes: res.data[0].likes,
                        like_user_ids: res.data[0].like_user_id,
                        post_title: res.data[0].title,
                        post_body: res.data[0].body,
                        post_author: res.data[0].author,
                        post_id: res.data[0].pid
                      })
                 : null
              )
        .catch((err) => console.log(err) )
    }
  }, [stateLocal,
      props.location])

   useEffect(() => {
     if(!stateLocal.comments_arr) {
       if(props.location.state) {
         const post_id = props.location.pathname.substring(6)
         axios.get('/api/get/allpostcomments',
                     {params: {post_id: post_id}} )
           .then(res => res.data.length !== 0
                          ? setState({...stateLocal, comments_arr: [...res.data]})
                          : null )
           .catch((err) => console.log(err))
       } 
     }
   }, [props.location, stateLocal])


    const handleCommentSubmit = (submitted_comment) => {
        if(stateLocal.comments_arr) {
            setState({...stateLocal, comments_arr: [submitted_comment,
                                                  ...stateLocal.comments_arr]})
         } else {
           setState({...stateLocal, comments_arr: [submitted_comment]})
         }
     };

     const handleCommentUpdate = (comment) => {
       const commentIndex = stateLocal.comments_arr.findIndex(com => com.cid === comment.cid)
       var newArr = [...stateLocal.comments_arr ]
       newArr[commentIndex] = comment

       setTimeout(() => setState({...stateLocal, comments_arr: [...newArr], edit_comment_id: 0 }), 100)
     };


     const handleCommentDelete = (cid) => {
       setState({...stateLocal, delete_comment_id: cid})
       const newArr = stateLocal.comments_arr.filter(com => com.cid !== cid)
       setState({...stateLocal, comments_arr: newArr})
     };

     const handleEditFormClose = () => {
       setState({...stateLocal, edit_comment_id: 0})
     }


    const RenderComments = (props) => {
      return(
      <div className={stateLocal.delete_comment_id === props.comment.cid
                        ? "FadeOutComment"
                        : "CommentStyles"}>
        <div>
        <p>{props.comment.comment} </p>
        <small>
          { props.comment.date_created === 'Just Now'
            ?  <div> {props.comment.isEdited
                  ? <span> Edited </span>
                  : <span> Just Now </span> }</div>
            :  props.comment.date_created
          }
        </small>
        <p> By: { props.comment.author} </p>
        </div>
        <div>
        {props.cur_user_id === props.comment.user_id
          ? !props.isEditing
            ?  <div>
                  <Button onClick={() => setState({...stateLocal,
                                                  edit_comment_id: props.comment.cid,
                                                  edit_comment: props.comment.comment
                                                  })
                                     }>
                     Edit
                   </Button>
                </div>
            :   <form onSubmit={(event, cid) => handleUpdate(event, props.comment.cid) }>
                  <input
                    autoFocus={true}
                    name="edit_comment"
                    id="editted_comment"
                    label="Comment"
                    value={stateLocal.edit_comment}
                    onChange={handleEditCommentChange}
                  />
                    <br />
                    <Button type='submit'>
                       Agree
                    </Button>
                    <Button type="button" onClick={handleEditFormClose}>
                     Cancel
                    </Button>
                    <button onClick={() => handleDeleteComment(props.comment.cid)}>
                      Delete
                    </button>
                  </form>
            : null }
          </div>
      </div>
    );
   }



    const handleEditCommentChange = (event) => (
      setState({...stateLocal,
                edit_comment: event.target.value})
    );


    const handleSubmit = (event) => {
      event.preventDefault()
      setState({...stateLocal, comment: ''})

      const comment = event.target.comment.value
      const user_id = context.dbProfileState[0].uid
      const username = context.dbProfileState[0].username
      const post_id = stateLocal.post_id
      const current_time = "Just Now"
      const temp_cid = Math.floor(Math.random() * 1000);

      const submitted_comment = {cid: temp_cid,
                                 comment: comment,
                                 user_id: user_id,
                                 author: username,
                                 date_created: current_time }

      const data = {comment: event.target.comment.value,
                    post_id: post_id,
                    user_id: user_id,
                    username: username}

      axios.post('/api/post/commenttodb', data)
        .then(res => console.log(res))
        .catch((err) => console.log(err))
      window.scroll({top: 0, left: 0, behavior: 'smooth'})
      handleCommentSubmit(submitted_comment)
    }

    const handleUpdate = (event, cid) => {
      event.preventDefault()
      console.log(event)
      console.log(cid)
      const comment = event.target.editted_comment.value
      const comment_id = cid
      const post_id = stateLocal.post_id
      const user_id = context.dbProfileState[0].uid
      const username = context.dbProfileState[0].username
      const isEdited = true
      const current_time = "Just Now"

      const edited_comment = {cid: comment_id,
                              comment: comment,
                              user_id: user_id,
                              author: username,
                              date_created: current_time,
                              isEdited: isEdited }

      const data = {cid: comment_id,
                    comment: comment,
                    post_id: post_id,
                    user_id: user_id,
                    username: username}

      axios.put('/api/put/commenttodb', data)
        .then(res => console.log(res))
        .catch((err) => console.log(err))
      handleCommentUpdate(edited_comment);
    }

    const handleDeleteComment = (cid) => {
      const comment_id = cid
      console.log(cid)
      axios.delete('/api/delete/comment', {data: {comment_id: comment_id}} )
        .then(res => console.log(res))
        .catch((err) => console.log(err))
      handleCommentDelete(cid)
    }

    const handleLikes = () => {
        const user_id = context.dbProfileState[0].uid
        const post_id = stateLocal.post_id

        const data = { uid: user_id, post_id: post_id }
        console.log(data)
        axios.put('/api/put/likes', data)
          .then( !stateLocal.like_user_ids.includes(user_id) && stateLocal.like_post
                    ? setState({...stateLocal,
                                likes: stateLocal.likes + 1,
                                like_post: false})
                    : null )
          .catch(err => console.log(err))
      };


    return(
        <div>
          <div>
            <h2>Post</h2>
            {stateLocal.comments_arr || props.location.state
              ? <div>
                  <p>{stateLocal.post_title}</p>
                  <p>{stateLocal.post_body}</p>
                  <p>{stateLocal.post_author}</p>
                </div>
            : null
           }

              <div style={{cursor: 'pointer'}} onClick={context.authState
                                                        ? () => handleLikes()
                                                        : () => history.replace('/signup')}>
                  <i className="material-icons">thumb_up</i>
                  <small className="notification-num-showpost">
                    {stateLocal.likes}
                  </small>
                </div>
          </div>
          <div>

            <h2> Comments:</h2>
            {stateLocal.comments_arr
              ? stateLocal.comments_arr.map((comment) =>
                 <RenderComments comment={comment}
                                 cur_user_id={context.dbProfileState
                                                ? context.dbProfileState[0].uid
                                                : null  }
                                 key={comment.cid}
                                 isEditing={comment.cid === stateLocal.edit_comment_id
                                              ? true
                                              : false }
                       />)
              : null
            }
          </div>
          <div>
            <form onSubmit={handleSubmit}>
              <TextField
                id="comment"
                label="Comment"
                margin="normal"
              />
              <br />
             
              {context.authState
                ? <Button variant="contained" color="primary" type="submit">
                    Submit
                  </Button>
                : <Link to="/signup">
                     <Button  variant="contained" color="primary">
                         Signup to Comment
                      </Button>
                   </Link>
               }
            </form>
          </div>
          <div>
          </div>
        </div>
    )}




export default ShowPost;
```

Vous remarquerez d'abord un appel `useState` gigantesque. Je vais expliquer comment chaque propriété fonctionne au fur et à mesure que nous explorerons notre composant au lieu de tout expliquer ici d'un coup. 

**useEffect() et requêtes API**  
La première chose à laquelle nous devons être attentifs est qu'un utilisateur peut accéder à une publication de 2 manières différentes. **En y accédant depuis le forum** ou **en y naviguant en utilisant l'URL directe**.  

```jsx
useEffect(() => {
      if(props.location.state && !stateLocal.fetched) {
        setState({...stateLocal,
                  fetched: true,
                  likes: props.location.state.post.post.likes,
                  like_user_ids: props.location.state.post.post.like_user_id,
                  post_title: props.location.state.post.post.title,
                  post_body: props.location.state.post.post.body,
                  post_author: props.location.state.post.post.author,
                  post_id: props.location.state.post.post.pid})
        }
      }, [stateLocal,
          props.location])

  useEffect( () => {
    if(!props.location.state && !stateLocal.fetched) {
     
      const post_id = props.location.pathname.substring(6)

      axios.get('/api/get/post',
                  {params: {post_id: post_id}} )
        .then(res => res.data.length !== 0
                ?   setState({...stateLocal,
                        fetched: true,
                        likes: res.data[0].likes,
                        like_user_ids: res.data[0].like_user_id,
                        post_title: res.data[0].title,
                        post_body: res.data[0].body,
                        post_author: res.data[0].author,
                        post_id: res.data[0].pid
                      })
                 : null
              )
        .catch((err) => console.log(err) )
    }
  }, [stateLocal,
      props.location])

   useEffect(() => {
     if(!stateLocal.comments_arr) {
       if(props.location.state) {
         const post_id = props.location.pathname.substring(6)
         axios.get('/api/get/allpostcomments',
                     {params: {post_id: post_id}} )
           .then(res => res.data.length !== 0
                          ? setState({...stateLocal, 
                                      comments_arr: [...res.data]})
                          : null )
           .catch((err) => console.log(err))
       }
     }
   }, [props.location, stateLocal])
```

S'ils **y accèdent depuis le forum**, nous vérifions cela dans notre appel `useEffect()` puis définissons notre état local sur la publication. Puisque nous utilisons la propriété `state` de **react router** dans l'élément `<Link />`, nous avons accès à l'ensemble des données de la publication déjà disponibles pour nous via les props, ce qui nous évite un appel API inutile. 

Si l'utilisateur **entre l'URL directe** d'une publication dans le navigateur, nous n'avons alors pas d'autre choix que de faire une requête API pour obtenir la publication, car un utilisateur doit cliquer sur une publication depuis le forum `posts.js` pour enregistrer les données de la publication dans la propriété `state` de react-router.

Nous extrayons d'abord l'**identifiant de la publication** de l'URL avec la propriété `pathname` de react-router, que nous utilisons ensuite comme paramètre dans notre **requête axios**. Après la requête API, nous enregistrons simplement la réponse dans notre état local. 

Après cela, nous devons **obtenir les commentaires avec une requête API** également. Nous pouvons utiliser la même méthode d'extraction d'URL de l'identifiant de la publication pour rechercher les commentaires associés à une publication. 

**RenderComments et Animations**  
Ici, nous avons notre composant fonctionnel `<RenderComments />` que nous utilisons pour afficher un commentaire individuel. 

```jsx
....

const RenderComments = (props) => {
      return(
      <div className={stateLocal.delete_comment_id === props.comment.cid
                        ? "FadeOutComment"
                        : "CommentStyles"}>
        <div>
        <p>{props.comment.comment} </p>
        <small>
          { props.comment.date_created === 'Just Now'
            ?  <div> {props.comment.isEdited
                  ? <span> Edited </span>
                  : <span> Just Now </span> }</div>
            :  props.comment.date_created
          }
        </small>
        <p> By: { props.comment.author} </p>
        </div>
        <div>
        {props.cur_user_id === props.comment.user_id
          ? !props.isEditing
            ?  <div>
                  <Button onClick={() => setState({...stateLocal,
                                                  edit_comment_id: props.comment.cid,
                                                  edit_comment: props.comment.comment
                                                  })
                                     }>
                     Edit
                   </Button>
                </div>
            :   <form onSubmit={(event, cid) => handleUpdate(event, props.comment.cid) }>
                  <input
                    autoFocus={true}
                    name="edit_comment"
                    id="editted_comment"
                    label="Comment"
                    value={stateLocal.edit_comment}
                    onChange={handleEditCommentChange}
                  />
                    <br />
                    <Button type='submit'>
                       Agree
                    </Button>
                    <Button type="button" onClick={handleEditFormClose}>
                     Cancel
                    </Button>
                    <button onClick={() => handleDeleteComment(props.comment.cid)}>
                      Delete
                    </button>
                  </form>
            : null }
          </div>
      </div>
    );
   }
   
 ....
 
   <h2> Comments:</h2>
   {stateLocal.comments_arr
     ? stateLocal.comments_arr.map((comment) =>
         <RenderComments comment={comment}
                         cur_user_id={context.dbProfileState
                                        ? context.dbProfileState[0].uid
                                        : null  }
                          key={comment.cid}
                          isEditing={comment.cid === stateLocal.edit_comment_id
                                         ? true
                                         : false }
                       />)
              : null
            }
          </div>

....
```

```css

.CommentStyles {
  opacity: 1;
}

.FadeInComment {
  animation-name: fadeIn;
  animation-timing-function: ease;
  animation-duration: 2s
}


.FadeOutComment {
  animation-name: fadeOut;
  animation-timing-function: linear;
  animation-duration: 2s
}


@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes fadeOut {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    width: 0;
    height: 0;
  }
}
```

Nous commençons par utiliser une expression ternaire à l'intérieur de la propriété `className` de la div pour basculer les classes de style. Si l'`delete_comment_id` dans notre état local correspond à l'identifiant du commentaire actuel, il est supprimé et une **animation de fondu** est appliquée au commentaire. 

Nous utilisons `@keyframe` pour faire les animations. Je trouve les animations CSS `@keyframe` beaucoup plus simples que les approches basées sur JavaScript avec des bibliothèques telles que `react-spring` et `react-transition-group`.

Ensuite, nous affichons le commentaire réel

Suivi d'une expression ternaire qui définit soit la **date de création du commentaire**, "Edited" ou "Just Now" en fonction des actions de l'utilisateur.  

Ensuite, nous avons une expression ternaire imbriquée assez complexe. Nous comparons d'abord l'`cur_user_id` (que nous obtenons de notre état `context.dbProfileState` et définissons dans notre JSX) à l'**identifiant de l'utilisateur du commentaire**. S'il y a une correspondance, nous affichons un **bouton d'édition**. 

Si l'utilisateur clique sur le **bouton d'édition**, nous définissons le commentaire sur l'état `edit_comment` et définissons l'état `edit_comment_id` sur l'**identifiant du commentaire**. Et cela rend également la propriété **isEditing** vraie, ce qui fait apparaître le formulaire et permet à l'utilisateur de modifier le commentaire. Lorsque l'utilisateur clique sur Agree, la fonction `handleUpdate()` est appelée, que nous verrons ensuite. 

**Opérations CRUD des commentaires**  
Ici, nous avons nos fonctions pour gérer les opérations CRUD des commentaires. Vous verrez que nous avons **2 ensembles de fonctions**, un ensemble pour **gérer les opérations CRUD côté client** et un autre pour **gérer les requêtes API**. Je vais expliquer pourquoi ci-dessous. 

```jsx
....
//Gestion des opérations CRUD côté client

const handleCommentSubmit = (submitted_comment) => {
        if(stateLocal.comments_arr) {
            setState({...stateLocal,
                      comments_arr: [submitted_comment,                                                  ...stateLocal.comments_arr]})
         } else {
           setState({...stateLocal,
                     comments_arr: [submitted_comment]})
         }
     };

     const handleCommentUpdate = (comment) => {
       const commentIndex = stateLocal.comments_arr.findIndex(com => com.cid === comment.cid)
       var newArr = [...stateLocal.comments_arr ]
       newArr[commentIndex] = comment

       setTimeout(() => setState({...stateLocal,
                                  comments_arr: [...newArr],
                                  edit_comment_id: 0 }), 100)
     };


     const handleCommentDelete = (cid) => {
       setState({...stateLocal, delete_comment_id: cid})
       const newArr = stateLocal.comments_arr.filter(com => com.cid !== cid)
       setState({...stateLocal, comments_arr: newArr})
     };

     
     

.... 

//Requêtes API

    const handleSubmit = (event) => {
      event.preventDefault()
      setState({...stateLocal, comment: ''})

      const comment = event.target.comment.value
      const user_id = context.dbProfileState[0].uid
      const username = context.dbProfileState[0].username
      const post_id = stateLocal.post_id
      const current_time = "Just Now"
      const temp_cid = Math.floor(Math.random() * 1000);

      const submitted_comment = {cid: temp_cid,
                                 comment: comment,
                                 user_id: user_id,
                                 author: username,
                                 date_created: current_time }

      const data = {comment: event.target.comment.value,
                    post_id: post_id,
                    user_id: user_id,
                    username: username}

      axios.post('/api/post/commenttodb', data)
        .then(res => console.log(res))
        .catch((err) => console.log(err))
      window.scroll({top: 0, left: 0, behavior: 'smooth'})
      handleCommentSubmit(submitted_comment)
    }

    const handleUpdate = (event, cid) => {
      event.preventDefault()
      console.log(event)
      console.log(cid)
      const comment = event.target.editted_comment.value
      const comment_id = cid
      const post_id = stateLocal.post_id
      const user_id = context.dbProfileState[0].uid
      const username = context.dbProfileState[0].username
      const isEdited = true
      const current_time = "Just Now"

      const edited_comment = {cid: comment_id,
                              comment: comment,
                              user_id: user_id,
                              author: username,
                              date_created: current_time,
                              isEdited: isEdited }

      const data = {cid: comment_id,
                    comment: comment,
                    post_id: post_id,
                    user_id: user_id,
                    username: username}

      axios.put('/api/put/commenttodb', data)
        .then(res => console.log(res))
        .catch((err) => console.log(err))
      handleCommentUpdate(edited_comment);
    }

    const handleDeleteComment = (cid) => {
      const comment_id = cid
      console.log(cid)
      axios.delete('/api/delete/comment', {data: {comment_id: comment_id}} )
        .then(res => console.log(res))
        .catch((err) => console.log(err))
      handleCommentDelete(cid)
    }
```

C'est parce que si un utilisateur soumet, modifie ou supprime un commentaire, **l'interface utilisateur ne sera pas mise à jour** sans recharger la page. Vous pouvez résoudre ce problème en faisant une autre requête API ou en ayant une configuration de socket web qui écoute les changements dans la base de données, mais une solution beaucoup plus simple est simplement de le gérer côté client de manière programmatique.  

Toutes les fonctions CRUD côté client sont appelées à l'intérieur de leurs appels API respectifs. 

**CRUD côté client :** 

* `handleCommentSubmit()` : met à jour le `comments_arr` en ajoutant simplement le commentaire au début du tableau.  
* `handleCommentUpdate()` : Trouve et remplace le commentaire dans le tableau avec l'index, puis met à jour et définit le nouveau tableau dans le `comments_arr`
* `handleCommentDelete()` : Trouve le commentaire dans le tableau avec l'**identifiant du commentaire**, puis le `.filter()` et enregistre le nouveau tableau dans `comments_arr`. 

**Requêtes API :** 

* `handleSubmit()` : nous obtenons nos données de notre formulaire, puis nous combinons les différentes propriétés dont nous avons besoin, et nous envoyons ces données à notre serveur. Les variables `data` et `submitted_comment` sont différentes car nos opérations CRUD côté client ont besoin de valeurs légèrement différentes de celles de notre base de données. 
* `handleUpdate()` : cette fonction est presque identique à notre fonction `handleSubmit()`. La principale différence étant que nous faisons une requête **put** au lieu d'un **post**. 
* `handleDeleteComment()` : simple requête **delete** utilisant l'**identifiant du commentaire**.  

**Gestion des likes**  
Maintenant, nous pouvons discuter de la manière de gérer lorsque l'utilisateur aime une publication. 

```jsx
 ....
 
     const handleLikes = () => {
        const user_id = context.dbProfileState[0].uid
        const post_id = stateLocal.post_id

        const data = { uid: user_id, post_id: post_id }
        console.log(data)
        if(!stateLocal.like_user_ids.includes(user_id)) {
        	axios.put('/api/put/likes', data)
          		.then( !stateLocal.like_user_ids.includes(user_id)
          					&& stateLocal.like_post
                    ? setState({...stateLocal,
                                likes: stateLocal.likes + 1,
                                like_post: false})
                    : null )
          		.catch(err => console.log(err))
      };
     }      
 
 .... 
 
 <div style={{cursor: 'pointer'}}
 	  onClick={context.authState
                 ? () => handleLikes()
                 : () => history.replace('/signup')}>
   <i className="material-icons">thumb_up</i>
     <small className="notification-num-showpost">
        {stateLocal.likes}
     </small>
 ....
```

```css
.notification-num-showpost {
  position:relative;
  padding:5px 9px;
  background-color: red;
  color: #941e1e;
  bottom: 23px;
  right: 5px;
  z-index: -1;
  border-radius: 50%;
}
```

Dans la fonction `handleLikes()`, nous définissons d'abord l'**identifiant de la publication** et l'**identifiant de l'utilisateur**. Ensuite, nous utilisons une condition pour vérifier si l'**identifiant de l'utilisateur actuel** n'est pas dans le tableau `like_user_id`, qui, rappelons-le, contient tous les **identifiants des utilisateurs** des utilisateurs qui ont déjà aimé cette publication. 

Si ce n'est pas le cas, nous faisons une requête **put** à notre serveur et après, nous utilisons une autre condition et vérifions si l'utilisateur n'a pas déjà aimé cette publication côté client avec la propriété d'état `like_post`, puis nous mettons à jour les likes.  

Dans le JSX, nous utilisons un événement `onClick` dans notre div pour soit appeler la fonction `handleLikes()`, soit rediriger vers la page d'inscription. Ensuite, nous utilisons une icône material pour afficher l'icône du pouce levé et la styliser avec un peu de CSS. 

Ce n'est pas trop mal, n'est-ce pas ? 

### profile.js

Maintenant, nous avons notre composant `profile.js` qui sera essentiellement notre tableau de bord utilisateur. Il contiendra les données de profil de l'utilisateur d'un côté et leurs publications de l'autre. 

Les données de profil que nous affichons ici sont différentes du `dbProfile` qui est utilisé pour les opérations de base de données. Nous utilisons l'autre profil ici que nous obtenons d'auth0 (ou d'autres connexions oauth) car il contient des données que nous n'avons pas dans notre `dbProfile`. Par exemple, peut-être leur photo de profil Facebook ou leur surnom. 

```jsx
import React, { useContext, useState, useEffect } from 'react';
import Context from '../utils/context';

import { Link } from 'react-router-dom';
import history from '../utils/history';
import axios from 'axios';

import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardHeader from '@material-ui/core/CardHeader';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Button from '@material-ui/core/Button';



const Profile = () => {
  const context = useContext(Context)

  const [stateLocal, setState] = useState({ open: false,
                                            post_id: null,
                                            posts: []
                                          })

  useEffect(() => {
    const user_id = context.dbProfileState[0].uid
    axios.get('/api/get/userposts', {params: { user_id: user_id}})
      .then((res) => setState({...stateLocal, posts: [...res.data] }))
      .catch((err) => console.log(err))
  })

  const handleClickOpen = (pid) => {
    setState({open: true, post_id: pid })
  }

  const handleClickClose = () => {
    setState({open: false, post_id: null })
  }

  const DeletePost = () => {
    const post_id = stateLocal.post_id
    axios.delete('api/delete/postcomments', {data: { post_id: post_id }} )
      .then(() => axios.delete('/api/delete/post', {data: { post_id: post_id }} )
          .then(res => console.log(res) ) )
      .catch(err => console.log(err))
      .then(() => handleClickClose())
      .then(() => setTimeout(() => history.replace('/'), 700 ) )
  }

  const RenderProfile = (props) => {
    return(
      <div>
        <h1>{props.profile.profile.nickname}</h1>
        <br />
        <img src={props.profile.profile.picture} alt="" />
        <br />
        <h4> {props.profile.profile.email}</h4>
        <br />
        <h5> {props.profile.profile.name} </h5>
        <br />
        <h6> Email Verified: </h6>
        {props.profile.profile.email_verified ? <p>Yes</p> : <p>No</p> }
        <br />
      </div>

     )
   }

  const RenderPosts = post => (
    <Card style={{width: '500px', height: '200px', marginBottom: '10px', paddingBottom: '80px' }}>
      <CardHeader
        title={<Link to={{pathname:'/post/' + post.post.pid, state: {post}}}>
                  {post.post.title}
                </Link> }
        subheader={
            <div className="FlexColumn">
              <div className="FlexRow">
                {post.post.date_created}
              </div>
              <div className="FlexRow">
                <Link to={{pathname:'/editpost/' + post.post.pid, state:{post} }}>
                  <button>
                   Edit
                  </button>
                </Link>
                <button onClick={() => handleClickOpen(post.post.pid) }>
                 Delete
                </button>
              </div>
            </div>
            }
          />
      <br />
      <CardContent>
        <span style={{overflow: 'hidden' }}> {post.post.body} </span>
      </CardContent>

    </Card>
  );


      return(
          <div>
            <div>
            <RenderProfile profile={context.profileState} />
            </div>
            <div>
              {stateLocal.posts
                ? stateLocal.posts.map(post =>
                  <RenderPosts post={post} key={post.pid} /> )
                : null }
            </div>
            <Dialog
              open={stateLocal.open}
              onClose={handleClickClose}
              aria-labelledby="alert-dialog-title"
              aria-describedby="alert-dialog-description"
            >
              <DialogTitle id="alert-dialog-title"> Confirm Delete? </DialogTitle>
                <DialogContent>
                  <DialogContentText
                    id="alert-dialog-description"
                    >
                      Deleteing Post
                    </DialogContentText>
                    <DialogActions>
                      <Button onClick={() => DeletePost() }>
                        Agree
                      </Button>
                      <Button onClick={() => handleClickClose()}>
                        Cancel
                      </Button>
                  </DialogActions>
                </DialogContent>
            </Dialog>

          </div>
  )}



export default (Profile);

```



```css


.FlexProfileDrawer {
  display: flex;
  flex-direction: row;
  margin-top: 20px;
  margin-left: -90px;
  margin-right: 25px;
}

.FlexColumnProfile > h1 {
  text-align: center;
}

FlexProfileDrawerRow {
  display: flex;
  flex-direction: row;
  margin: 10px;
  padding-left: 15px;
  padding-right: 15px;
}


.FlexColumn {
  display: flex;
  flex-direction: column;
}

.FlexRow {
  display: flex;
  flex-direction: row;
}
```

La grande majorité de cette fonctionnalité dans ce composant, nous l'avons déjà vue. Nous commençons par faire une requête API dans notre hook `useEffect()` pour obtenir nos publications de la base de données en utilisant l'**identifiant utilisateur**, puis nous enregistrons les publications dans notre état local. 

Ensuite, nous avons notre composant fonctionnel `<RenderProfile />`. Nous obtenons les **données de profil pendant l'authentification** et les enregistrons dans l'état global afin de pouvoir simplement y accéder ici sans faire de requête API.  

Ensuite, nous avons `<RenderPosts />` qui affiche une publication et permet à un utilisateur d'aller à, modifier ou supprimer une publication. Ils peuvent accéder à la page de la publication en cliquant sur le titre. Cliquer sur le **bouton de modification** les emmènera au composant `editpost.js` et cliquer sur le **bouton de suppression** ouvrira la boîte de dialogue. 

Dans la fonction `DeletePost()`, nous supprimons d'abord tous les commentaires associés à cette publication en utilisant l'identifiant de la publication. Parce que si nous supprimions simplement la publication sans supprimer les commentaires, nous aurions simplement **un tas de commentaires dans notre base de données sans publication**. Après cela, nous supprimons simplement la publication. 

### showuser.js

Maintenant, nous avons notre composant qui affiche les publications et les commentaires d'un autre utilisateur lorsqu'un utilisateur clique sur son nom dans le forum.

```jsx
import React, { useState, useEffect } from 'react';

import { Link } from 'react-router-dom';

import axios from 'axios';
import moment from 'moment';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardHeader from '@material-ui/core/CardHeader';

import Button from '@material-ui/core/Button';


const ShowUser = (props) => {

  const [profile, setProfile ] = useState({})
  const [userPosts, setPosts ] = useState([])

  useEffect(() => {
    const username = props.location.state.post.post.author
    axios.get('/api/get/otheruserprofilefromdb',
              {params: {username: username}} )
      .then(res =>  setProfile({...res.data} ))
      .catch(function (error) {
          console.log(error);
        })
     axios.get('/api/get/otheruserposts',
               {params: {username: username}} )
       .then(res =>  setPosts([...res.data]))
       .catch(function (error) {
           console.log(error);
         })
      window.scrollTo({top: 0, left: 0})
    }, [props.location.state.post.post.author] )


  const RenderProfile = (props) => (
    <div>
      <div className="FlexRow">
         <h1>
            {props.profile.username}
         </h1>
         </div>
         <div className="FlexRow">
         <Link to={{pathname:"/sendmessage/", 
                   state:{props} }}>
             <Button variant="contained" color="primary" type="submit">
                Send Message
             </Button>
          </Link>
        </div>
    </div>
    );


  const RenderPosts = (post) => (
    <div>
     <Card className="CardStyles">
        <CardHeader
          title={<Link to={{pathname:"/post/" + post.post.pid,
      						state: {post} }}>
                { post.post.title }
                </Link>}
          subheader={
                    <div>
                      <div >
                      {  moment(post.post.date_created).format('MMMM Do, YYYY | h:mm a') }
                      </div>
                      <div >{post.post.author}</div>
                    </div> }
        />
        <CardContent>
            <span style={{ overflow: 'hidden'}}>{ post.post.body } </span>
        </CardContent>
      </Card>
    </div>
  );


   return (
     <div>
     <div className="FlexRow">
        {profile
          ? <RenderProfile profile={profile} />
          : null
         }
     </div>

    <br />
    <hr className="style-two" />

     <h3> Latest Activity: </h3>
       <div className="FlexColumn">
       { userPosts ?
          userPosts.map(post =>
          <div key={ post.pid }>
             <RenderPosts  post={post} />
             <br />
          </div>
           )
       : null
       }
       </div>
     </div>
  )
}


export default (ShowUser);
```

Nous commençons par 2 requêtes API dans notre hook `useEffect()` puisque nous aurons besoin à la fois des données de profil de l'autre utilisateur et de ses publications, puis nous les enregistrons dans l'état local. 

Nous obtenons l'identifiant de l'utilisateur avec la propriété `state` de **react-routers** que nous avons vue dans le composant `showpost.js`. 

Nous avons nos composants fonctionnels habituels `<RenderProfile />` et `<RenderPosts />` qui affichent les données de profil et les publications. Et ensuite, nous les affichons simplement dans notre JSX. 

C'est tout pour ce composant, il n'y avait rien de nouveau ou d'ambigu ici, donc je l'ai gardé bref. 

## Application Admin 

Aucun blog full stack n'est complet sans une application admin, c'est donc ce que nous allons configurer ensuite. 

Ci-dessous se trouve un diagramme qui montrera essentiellement comment une application admin fonctionnera. Il est possible de simplement avoir votre application admin sur différentes routes au sein de votre application régulière, mais le fait de l'avoir complètement séparée dans sa propre application rend vos deux applications beaucoup plus compartimentées et sécurisées. 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-168.png)



Ainsi, l'application admin sera sa propre application avec sa propre authentification, mais elle se connectera à la même base de données que notre application régulière. 

### Authentification de l'application Admin

L'authentification pour l'application admin sera un peu différente de notre application régulière. La principale différence étant qu'il n'y aura **aucune option d'inscription** sur l'application admin, les administrateurs devront être ajoutés manuellement. Puisque nous ne voulons pas que des personnes aléatoires s'inscrivent à notre application admin.

Similaire à l'application régulière, j'utiliserai Auth0 pour l'authentification.

Tout d'abord, nous commencerons par le tableau de bord admin. 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-169.png)

Ensuite, cliquez sur le bouton **créer une application**. 

![Image](https://lh3.googleusercontent.com/VgClY93X2X04CU49SHaHG4zh9kZvl4QiLCZUsLM2cVu2tfMpaLLy7Oootsb1SHB8_dbC0q-aHp575FtpWb0mtD545RZSh_X7cn7v3vuw-vyYqCDOV3_UWkdZjV_2zZA7dLGb2Ypa)

Ensuite, nous devrons créer une connexion de base de données. Allez dans la section **connexions** et cliquez sur **créer une connexion DB**.

![Image](https://lh5.googleusercontent.com/PBWEyx9KOGXyEtptGPJNQwZ-L93gaeveqN_fNh4xOJ1ih90h4JAHq_6is6yZyPbCCR4g6Ck_isGfyweJWyBty6Ol5uotMc0nS29iP4-Il9ig4AK42aLGsZElSCXDTPTYRB_KIhCU)

Nous appellerons notre nouvelle connexion "adminapp2db".   
****Important :** Vérifiez le bouton coulissant étiqueté "Disable Sign Ups". Nous ne voulons pas que des personnes aléatoires s'inscrivent à notre application admin.

![Image](https://lh3.googleusercontent.com/-gGWutAmysLlbKEiNq_7hdPzAr-vLTu4q17gN0_jisCquTyJvVcVUsrJgHyhq9eu7Aww8wSA7i-7ygNV13jTgTRa-17aEZ4rU3xJL3OqgVDhcM7veyMjHqTSQVvURj142vCI3387)

Cliquez sur **Créer** et allez à l'onglet **Applications**. Cliquez sur le bouton coulissant pour **adminapp2** que nous avons créé à l'étape précédente.

![Image](https://lh6.googleusercontent.com/b_pGjEqPPmqdlyUpsFIiqIMdEAimsV0QG_4FcWKF-o49zjXOVbAe5JUwkfhbcWTG2vc1iXZpBF2YWaL83j8OcOGOm7AxcR3oPDRVdWCJJlMnCFNe6ovhEJWoLX4CYuDNf_A5Uw_-)

Ensuite, nous voulons ajouter manuellement des utilisateurs pour qu'ils puissent se connecter à notre application admin. Allez dans la section **utilisateurs** et cliquez sur **Créer un utilisateur**.

![Image](https://lh6.googleusercontent.com/HkSPFibFEKfr1nSbc9vIuONHNBhVf2qsnbH83sGdzYEhf6a45orXu0xKK201-PERiH6UDrTarUy5j6tBHkiRrjrAmCzsJFFrJpJyu_GNhLstzwcGyNmXUZwnHigeOV4KRbZo8DGu)

Remplissez les champs email et mot de passe avec vos informations de connexion souhaitées et définissez la **connexion** sur la connexion **adminapp2db** que nous avons créée à l'étape précédente. Ensuite, cliquez sur **enregistrer**.

![Image](https://lh4.googleusercontent.com/394iX1K9e90HoWRjJ03yAK73ZqH9IHvZJ-BunjdX1ORzCdBiynIuZs4JdujELDbLfCOR856SVkmkOM5LoWN9FDRkUpC2MkBzAO6bpxvoSQnlnJYDk2_I3a6jM2Vb-nK13ueOCZvF)

  
Et c'est tout. Nous pouvons maintenant tester si notre connexion fonctionne. Retournez à la section **connexions** et cliquez sur la connexion **adminapp2db**. Cliquez sur l'onglet **essayer la connexion**. Entrez vos détails de connexion de l'étape **Créer un utilisateur**. Vous ne devriez pas non plus voir d'onglet pour vous inscrire.

![Image](https://lh5.googleusercontent.com/W3p4YMqQRRQ1Wt-V_M_qt4afMNpx5H8uPeGg6o13SxWSEo9aH3zgUflgWGpifhWuhrdi9oyq0dQ2M5mA_1HID_l5MdxD4a3aLiqePDpK3qIKG4bNTxfZBJ6UaqdE1J-8gmq9oIVt)

  
Si cela réussit, vous devriez voir ceci :

![Image](https://lh3.googleusercontent.com/Uf6JN9Jflq1PBeOchgQLD4h9sKHXQPavRhOby6UvgqLUX6h_FxIQwg-nQegIk-OWedkb99LVh4N58_IDB5qvO6pVKR1KT6XpaP8DngUa9692dvY2-wV5D-is4i_wXodiKcpMoD2R)

Ce qui signifie que notre authentification est configurée et que seuls les administrateurs que nous avons ajoutés manuellement peuvent se connecter. Super ! 

### Privilèges globaux d'édition et de suppression

L'une des principales fonctionnalités d'une application admin sera d'avoir des privilèges globaux d'édition et de suppression, ce qui permettra à un administrateur ou à un modérateur d'apporter des modifications aux publications et aux commentaires des utilisateurs ou de supprimer du spam. C'est ce que nous allons construire ici. 

**L'idée de base de la manière dont nous allons procéder est de supprimer la vérification d'authentification pour éditer et supprimer des publications et des commentaires**, tout en veillant à ce que la publication et le commentaire appartiennent toujours à leur auteur d'origine. 

Nous n'avons pas à commencer à partir de zéro, nous pouvons utiliser la même application que nous avons construite dans les sections précédentes et ajouter du code spécifique à l'admin. 

La toute première chose que nous pouvons faire est de nous débarrasser des boutons "s'inscrire pour ajouter une publication/commentaires" dans notre composant `addpost.js` et `showpost.js` puisque un administrateur ne peut pas s'inscrire à cette application par lui-même.  

  

ensuite, dans notre composant `editpost.js`, dans la fonction `handleSubmit()`, nous pouvons accéder à `user_id` et `username` avec les **props react-router** que nous avons vus auparavant. 

Cela garantira que même si nous modifions la publication en tant qu'admin, elle appartient toujours à l'utilisateur d'origine. 

```javascript
const handleSubmit = (event) => {
    event.preventDefault()

    const user_id = props.location.state.post.post.user_id
    const username = props.location.state.post.post.author
    const pid = props.location.state.post.post.pid
    const title = event.target.title.value
    const body = event.target.body.value

    const data = {title: title,
                  body: body,
                  pid: pid,
                  uid: user_id,
                  username: username
                 }
    axios.put("/api/put/post", data)
      .then(res => console.log(res))
      .catch(err => console.log(err))
      .then(setTimeout(() => history.replace('/'), 700 ))
  }
```

Le composant `addpost.js` peut être laissé tel quel, puisque un administrateur doit pouvoir faire des publications normalement.

De retour dans notre composant `posts.js`, nous pouvons ajouter des boutons **edit** et **delete** à notre fonction `<RenderPosts />`. 

```jsx
....

const RenderPosts = post => (
  <div >
  <Card >
 ...   
    <button>
      <Link to={{pathname:"/editpost/" + post.post.pid, state:{post} }}>
        Edit
      </Link>
    </button>
    <button onClick={() => deletePost(post.post.pid)}>
      Delete
    </button>
  </Card>
  </div>
)

....
```

Cette fonctionnalité n'était disponible que sur le tableau de bord de l'utilisateur dans notre application régulière, mais nous pouvons l'implémenter directement dans le forum principal pour notre application admin, ce qui nous donne des privilèges globaux d'édition et de suppression sur toutes les publications. 

Le reste du composant `posts.js` peut être laissé tel quel.

Maintenant, dans notre composant `showpost.js`, la première chose que nous pouvons faire est de supprimer la comparaison de l'identifiant de l'utilisateur actuel avec l'identifiant de l'utilisateur du commentaire qui permet les modifications. 

```jsx
....    
	// props.cur_user_id === props.comment.user_id
    const RenderComments = (props) => {
      return(
      <div className={stateLocal.delete_comment_id === props.comment.cid
                        ? "FadeOutComment"
                        : "CommentStyles"}>
        <div>
        {true
          ? !props.isEditing
            ?  <div>
  ....
```

Ensuite, dans la fonction `handleUpdate()`, nous pouvons définir le nom d'utilisateur et l'identifiant de l'utilisateur à l'auteur original du commentaire.  

```jsx
....

    const handleUpdate = (event, cid, commentprops) => {
      event.preventDefault()
      
       ....
      const user_id = commentprops.userid
      const username = commentprops.author
  
  ....
```

Notre serveur et notre base de données peuvent être laissés tels quels.

C'est tout ! nous avons implémenté la fonctionnalité d'édition et de suppression globale dans notre application. 

### Tableau de bord Admin

Une autre fonctionnalité très courante dans les applications admin est d'avoir un calendrier avec des heures et des dates de rendez-vous, ce que nous allons devoir implémenter ici. 

Nous commencerons par le **serveur** et **SQL**. 

```sql

CREATE TABLE appointments (
  aid SERIAL PRIMARY KEY,
  title VARCHAR(10),
  start_time TIMESTAMP WITH TIME ZONE UNIQUE,
  end_time TIMESTAMP WITH TIME ZONE UNIQUE
);
```

Nous avons une configuration simple ici. Nous avons la `PRIMARY KEY`. Ensuite, le titre du rendez-vous. Après cela, nous avons `start_time` et `end_time`. `TIMESTAMP WITH TIME ZONE` nous donne la date et l'heure, et nous utilisons le mot-clé `UNIQUE` pour nous assurer qu'il ne peut pas y avoir de rendez-vous en double. 

```javascript
/*
      DATE APPOINTMENTS
*/

router.post('/api/post/appointment', (req, res, next) => {
  const values = [req.body.title, req.body.start_time, req.body.end_time]
  pool.query('INSERT INTO appointments(title, start_time, end_time)
             VALUES($1, $2, $3 )', 
    	values, (q_err, q_res) => {
    		if (q_err) return next(q_err);
    		console.log(q_res)
    		res.json(q_res.rows);
  });
});


router.get('/api/get/allappointments', (req, res, next) => {
  pool.query("SELECT * FROM appointments", (q_err, q_res) => {
    res.json(q_res.rows)
  });
});
```

Ici, nous avons nos **routes** et **requêtes** pour les rendez-vous. Pour des raisons de concision, j'ai omis les routes d'édition et de suppression puisque nous avons vu ces requêtes de nombreuses fois auparavant. Lancez-vous le défi de voir si vous pouvez créer ces requêtes. Ce sont des instructions `INSERT` et `SELECT` basiques, rien d'extraordinaire ici.

 Nous pouvons maintenant passer à notre **côté client.**

Au moment de la rédaction de cet article, je n'ai pas trouvé de bonne bibliothèque de calendrier qui fonctionnerait à l'intérieur d'un composant React Hooks, j'ai donc décidé de simplement implémenter un composant de classe avec la bibliothèque `react-big-calendar`. 

Ce sera toujours facile à suivre, nous n'utiliserons pas Redux ou toute fonctionnalité de classe complexe qui n'est pas disponible pour les hooks React. 

`componentDidMount()` est équivalent à `useEffect(() => {}, [] )` . Le reste de la syntaxe est essentiellement le même, sauf que vous ajoutez le mot-clé `this` au début lorsque vous accédez aux valeurs des propriétés. 

Je vais remplacer le composant `profile.js` régulier par le tableau de bord admin ici, et nous pouvons le configurer comme suit. 

```jsx
//profile.js

import React, { Component } from 'react'

import { Calendar, momentLocalizer, Views } from 'react-big-calendar';
import moment from 'moment';
import 'react-big-calendar/lib/css/react-big-calendar.css';

import history from '../utils/history';

import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

import axios from 'axios';



const localizer = momentLocalizer(moment)

const bus_open_time = new Date('07/17/2018 9:00 am')
const bus_close_time = new Date('07/17/2018 5:00 pm')


let allViews = Object.keys(Views).map(k => Views[k])





class Profile extends Component {
  constructor(props) {
  super(props)
    this.state = {
      events: [],
      format_events: [],
      open: false,
      start_display: null,
      start_slot: null,
      end_slot: null
     }
  }

  componentDidMount() {
    axios.get('api/get/allappointments')
    .then((res) => this.setState({events: res.data}))
    .catch(err => console.log(err))
    .then(() => this.dateStringtoObject())
   }

   handleClickOpen = () => {
      this.setState({ open: true });
    };

    handleClose = () => {
      this.setState({ open: false });
    };


 dateStringtoObject = () => {
    this.state.events.map(appointment => {
      this.setState({
        format_events: [...this.state.format_events,
          { id: appointment.aid,
            title: appointment.title,
            start: new Date(appointment.start_time),
            end: new Date(appointment.end_time)
       }]})
     })
   }


   handleAppointmentConfirm = () => {
     const time_start = this.state.start_slot
     const time_end = this.state.end_slot
     const data = {title: 'booked', start_time: time_start, end_time: time_end }
     axios.post('api/post/appointment', data)
       .then(response => console.log(response))
       .catch(function (error) {
         console.log(error);
       })
       .then(setTimeout( function() { history.replace('/') }, 700))
       .then(alert('Booking Confirmed'))
    }

    showTodos = (props) => (
      <div className="FlexRow">
        <p> { props.appointment.start.toLocaleString() }</p>
      </div>
    )


   BigCalendar = () => (
     <div style={{height: '500px'}} >
       <Calendar
         selectable
         localizer={localizer}
         events={this.state.format_events}
         min={bus_open_time}
         max={bus_close_time}
         views={allViews}
         defaultDate={new Date('07/12/2018')}
         onSelectEvent={event => alert(event.start)}
         onSelectSlot={slotInfo =>
           {
             this.setState({start_slot: slotInfo.start,
                            end_slot: slotInfo.end,
                            start_display: slotInfo.start.toLocaleString()
              });
             this.handleClickOpen();
          }}
       />
     </div>
   )

 render() {
    return (
    <div className="FlexRow">
      <div className="FlexColumn">
        <div className="FlexRow">
         <h1> Admin Dashboard </h1>
        </div>


        <h4>Appointments: </h4>
          <div className="FlexRow">
           <Paper>
            <div className="FlexDashAppointCol">
            { this.state.format_events ?
              this.state.format_events.map(appointment =>
                <this.showTodos key={appointment.id} appointment={appointment} />)
             : null
            }
            </div>
         </Paper>
        </div>
        <br />
        <br />
        <div className="FlexRow">
        { this.state.format_events ?
          <this.BigCalendar />
         : null
        }
        </div>
        <hr />
      </div>

      <Dialog
          open={this.state.open}
          onClose={this.handleClose}
          aria-labelledby="alert-dialog-title"
          aria-describedby="alert-dialog-description"
        >
          <DialogTitle id="alert-dialog-title"> Confirm Appointment? </DialogTitle>
          <DialogContent>
            <DialogContentText id="alert-dialog-description">
              Confirm Appointment:  {this.state.start_display}
            </DialogContentText>
          </DialogContent>
          <DialogActions>
            <Button color="primary" onClick={() => this.handleAppointmentConfirm() }>
            Confirm
            </Button>
            <Button color="primary" onClick={() => this.handleClose() }>
              Cancel
            </Button>
          </DialogActions>
        </Dialog>
    </div>
    )}
}

export default (Profile);

```

Nous commencerons par nos importations habituelles. Ensuite, nous initialiserons le localisateur de calendrier avec la bibliothèque `moment.js`. 

Ensuite, nous définirons l'heure d'ouverture et de fermeture de l'entreprise, que j'ai fixée de 9h00 à 17h00 dans les variables `bus_open_time` et `bus_close_time`. 

Ensuite, nous définissons la variable `allViews` qui permettra au calendrier d'avoir les vues des mois, des semaines et des jours. 

Ensuite, nous avons notre variable d'état local dans le constructeur, qui est équivalente au hook `useState`. 

Il n'est pas nécessaire de comprendre les `constructeurs` et la méthode `super()` pour nos besoins, car ce sont des sujets assez vastes. 

Ensuite, nous avons notre méthode `componentDidMount()` que nous utilisons pour faire une requête `axios` à notre serveur afin d'obtenir nos rendez-vous et de les sauvegarder dans notre propriété d'état local `events`.  

`handleClickOpen()` et `handleClose()` sont des fonctions d'assistance qui ouvrent et ferment notre boîte de dialogue lorsqu'un utilisateur confirme un rendez-vous. 

Ensuite, nous avons la fonction `dateStringToObject()` qui prend nos données brutes de notre requête et les transforme en un format utilisable par notre calendrier. `format_events` est la propriété d'état pour contenir les événements formatés. 

Après cela, nous avons la fonction `handleAppointmentConfirm()`. Nous utiliserons cette fonction pour faire notre requête API à notre serveur. Ces valeurs, nous les obtiendrons de notre composant `<Calendar />` que nous verrons dans un instant. 

Notre `<showTodos />` est la manière dont nous affichons chaque rendez-vous. 

Ensuite, nous avons notre calendrier réel. La plupart des props devraient être auto-explicatives, mais 2 sur lesquelles nous pouvons nous concentrer sont `onSelectEvent` et `onSelectSlot`.

`onSelectEvent` est une fonction qui est appelée chaque fois qu'un utilisateur clique sur un événement existant dans le calendrier, et nous l'avertissons simplement de l'heure de début de l'événement. 

`onSelectSlot` est une fonction qui est appelée chaque fois qu'un utilisateur clique sur un créneau vide dans le calendrier, et c'est ainsi que nous obtenons les valeurs de temps du calendrier. Lorsque l'utilisateur clique sur un créneau, **nous sauvegardons les valeurs de temps contenues dans le paramètre slotInfo dans notre état local**, puis nous ouvrons une boîte de dialogue pour confirmer le rendez-vous. 

Notre méthode de rendu est assez standard. Nous affichons nos événements dans un élément `<Paper />` et avons le calendrier en dessous. Nous avons également une boîte de dialogue standard qui permet à un utilisateur de confirmer ou d'annuler la demande. 

Et c'est tout pour le tableau de bord admin. Vous devriez avoir quelque chose qui ressemble à ceci : 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-170.png)



### Suppression des utilisateurs ainsi que de leurs publications et commentaires

Maintenant, pour la dernière partie de ce tutoriel, nous pouvons supprimer les utilisateurs et leurs commentaires et publications associés. 

Nous commencerons par nos requêtes API. Nous avons ici des instructions `DELETE` assez simples, je vais expliquer davantage avec le code front-end. 

```javascript

/*
    Section des utilisateurs
*/

router.get('/api/get/allusers', (req, res, next) => {
  pool.query("SELECT * FROM users", (q_err, q_res) => {
    res.json(q_res.rows)
  });
});


/*
 Supprimer les utilisateurs et toutes les publications et commentaires associés
*/

router.delete('/api/delete/usercomments', (req, res, next) => {
  uid = req.body.uid

  pool.query('DELETE FROM comments 
             WHERE user_id = $1', [ uid ], (q_err, q_res) => {
    res.json(q_res);
  });
});

router.get('/api/get/user_postids', (req, res, next) => {
  const user_id = req.query.uid

  pool.query("SELECT pid FROM posts 
             WHERE user_id = $1", [ user_id ], (q_err, q_res) => {
    res.json(q_res.rows)
  });
});

router.delete('/api/delete/userpostcomments', (req, res, next) => {
  post_id = req.body.post_id

  pool.query('DELETE FROM comments 
             WHERE post_id = $1', [ post_id ], (q_err, q_res) => {
    res.json(q_res);
  });
});

router.delete('/api/delete/userposts', (req, res, next) => {
  uid = req.body.uid
  pool.query('DELETE FROM posts
             WHERE user_id = $1', [ uid ], (q_err, q_res) => {
    res.json(q_res);
  });
});

router.delete('/api/delete/user', (req, res, next) => {
  uid = req.body.uid
  console.log(uid)
  pool.query('DELETE FROM users 
             WHERE uid = $1', [ uid ], (q_err, q_res) => {
    res.json(q_res);
    console.log(q_err)
  });
});


module.exports = router
```



Et maintenant pour notre composant, vous remarquerez que nous utilisons toutes nos requêtes API dans la fonction `handleDeleteUser()`.

```jsx
import React, { useState, useEffect } from 'react'

import axios from 'axios';
import history from '../utils/history';

import Button from '@material-ui/core/Button';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';



const Users = () => {
  const [state, setState] = useState({ users: [],
                                       open: false,
                                       uid: null
                                     })

  useEffect(() => {
    axios.get('api/get/allusers')
      .then(res => setState({users: res.data}))
      .catch(err => console.log(err))
  }, [])


  const handleClickOpen = (user_id) => {
      setState({ open: true, uid: user_id });
    };

  const handleClose = () => {
      setState({ open: false });
    };

  const handleDeleteUser = () => {
      const user_id = state.uid
      axios.delete('api/delete/usercomments',
      					{ data: { uid: user_id }})
        .then(() => axios.get('api/get/user_postids',
        					{ params: { uid: user_id }})
          .then(res => res.data.map(post => 
          		axios.delete('/api/delete/userpostcomments', 
          				{ data: { post_id: post.pid }})) )
        )
        .then(() => axios.delete('api/delete/userposts',
        					{ data: { uid: user_id }})
          .then(() => axios.delete('api/delete/user',
          							{ data: { uid: user_id }} )
      ))
        .catch(err => console.log(err) )
        .then(setTimeout(history.replace('/'), 700))
    }

  const RenderUsers = (user) => (
    <TableRow>
      <TableCell>
      <br/>
      <p> { user.user.username } </p>
      <p> { user.user.email } </p>
      <br />
      <button onClick={() => handleClickOpen(user.user.uid)}>
        Delete User
      </button>
      </TableCell>
    </TableRow>
  );


    return (
    <div>
      <h1>Users</h1>
      <div className="FlexRow">
      <Paper>
      <div className="FlexUsersTable">
      <Table>
        <TableHead>
          <TableRow>
            <TableCell> User</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
             {state.users ?
                state.users.map(user =>
                  <RenderUsers key={ user.uid } user={user} />)
             : null
             }
          </TableBody>
        </Table>
      </div>
    </Paper>
    </div>

    <Dialog
        open={state.open}
        onClose={handleClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title"> Delete User </DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
          Deleteing User will delete all posts and comments made by user
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => {handleDeleteUser(); handleClose()} }>
            Delete
          </Button>
          <Button onClick={handleClose} color="primary">
            Cancel
          </Button>
        </DialogActions>
      </Dialog>
     </div>
    )
}

export default (Users);

```

**handleDeleteUser()**   
Je vais commencer par la fonction `handleDeleteUser()`. La première chose que nous faisons est de définir l'**identifiant de l'utilisateur** de l'utilisateur que nous voulons supprimer, que nous obtenons de l'état local. L'identifiant de l'utilisateur est enregistré dans l'état local lorsqu'un administrateur clique sur le nom d'un utilisateur et que la boîte de dialogue s'ouvre. 

La raison de cette configuration est due à la **contrainte de clé étrangère de PSQL**, où nous ne pouvons pas supprimer une ligne dans une table qui est référencée par une autre table avant de supprimer cette autre ligne. Voir la section **contrainte de clé étrangère de PSQL** pour un rappel. 

C'est pourquoi nous devons travailler à l'envers et supprimer tous les commentaires et publications associés à un utilisateur avant de pouvoir supprimer l'utilisateur lui-même.    

La **première requête de suppression axios** est de supprimer tous les commentaires où il y a un identifiant d'utilisateur correspondant que nous venons de définir. Nous faisons cela parce que nous ne pouvons pas supprimer les commentaires associés aux publications avant de supprimer les publications elles-mêmes. 

Dans notre **première** instruction `.then()`, nous recherchons toutes les publications que cet utilisateur a faites et récupérons ces **identifiants de publication**. Vous remarquerez que notre deuxième instruction `.then()` est en fait _à l'intérieur_ de notre première instruction `.then()`. Cela est dû au fait que nous voulons la réponse de la requête `axios.get('api/get/user_postids')` plutôt que la réponse de la **première requête de suppression axios**.

**Dans notre deuxième instruction `.then()`**, nous obtenons un tableau des identifiants de publication des publications associées à l'utilisateur que nous voulons supprimer, puis nous appelons `.map()` sur le tableau. Nous supprimons ensuite tous les commentaires associés à cette publication, quel que soit l'utilisateur qui l'a faite. Cela ferait de `axios.delete('/api/delete/userpostcomments')` **une requête axios triplement imbriquée** ! 

Notre **troisième** instruction `**.then()**` supprime les publications réelles faites par l'utilisateur. 

Notre **quatrième** instruction `.then()` supprime enfin l'utilisateur de la base de données. Notre **cinquième** instruction `.then()` redirige ensuite l'administrateur vers la page d'accueil. Notre **quatrième** instruction `.then()` est à l'intérieur de notre **troisième** instruction `**.then()**` pour la même raison que notre **deuxième** instruction **`.then()`** est à l'intérieur de notre **première**.   


Tout le reste est une fonctionnalité que nous avons vue plusieurs fois auparavant, ce qui conclura notre tutoriel ! 

Merci d'avoir lu !