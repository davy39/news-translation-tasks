---
title: Comment construire et déployer une application backend avec Express, Postgres,
  Github et Heroku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-03T20:46:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-backend-application
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-pixabay-417273.jpg
tags:
- name: 'Back end development '
  slug: back-end-development
- name: deployment
  slug: deployment
- name: Express
  slug: express
- name: GitHub
  slug: github
- name: Heroku
  slug: heroku
- name: postgres
  slug: postgres
seo_title: Comment construire et déployer une application backend avec Express, Postgres,
  Github et Heroku
seo_desc: "By Njoku Samson Ebere\nIn this tutorial, we will be learning how to build\
  \ and deploy an image management application backend. \nIt will be able to store\
  \ a record of an image in the database, get the image's record back from the database,\
  \ update the rec..."
---

Par Njoku Samson Ebere

Dans ce tutoriel, nous allons apprendre à construire et déployer le backend d'une application de gestion d'images.

Il sera capable de stocker un enregistrement d'une image dans la base de données, de récupérer l'enregistrement de l'image depuis la base de données, de mettre à jour l'enregistrement, et même de supprimer complètement l'enregistrement si nécessaire.

Pour réaliser tout cela, nous allons utiliser Express (un framework Node.js), Postgres (une base de données), Cloudinary (un stockage d'images basé sur le cloud), GitHub (pour le contrôle de version/stockage) et Heroku (une plateforme d'hébergement).

Ces outils sont tous gratuits. Vous n'avez donc pas à vous soucier de la manière de les payer. Merci à ces grands innovateurs.

### Prérequis

Si vous êtes nouveau dans la plupart de ces technologies, je vous conseille de suivre mon autre tutoriel sur la manière de [créer un serveur et télécharger des images vers Cloudinary](https://www.freecodecamp.org/news/build-a-secure-server-with-node-and-express/).

Si vous êtes totalement nouveau dans Postgres, alors consultez ce [tutoriel](https://dev.to/ogwurujohnson/-persisting-a-node-api-with-postgresql-without-the-help-of-orms-like-sequelize-5dc5).

Quand vous serez prêt, commençons le travail !

## Comment stocker et récupérer un enregistrement d'image

### Créer une base de données et une table

Vous allez donc vouloir commencer par cloner ce [projet](https://github.com/EBEREGIT/server-tutorial/tree/cloudinary-upload) si vous ne l'avez pas déjà.

Dans votre **pgAdmin** :

* Créez une base de données et nommez-la `tutorial`
* Créez une table et nommez-la `tutorial`
* Créez un rôle de connexion/groupe et nommez-le `tutorial`. **(N'oubliez pas de lui donner tous les privilèges.)**

De retour dans votre répertoire de projet, installez les packages [node-postgres](https://node-postgres.com/) (`npm i pg`) et [make-runnnable](https://www.npmjs.com/package/make-runnable) (`npm i make-runnable`).

Dans votre fichier `package.json`, remplacez le contenu de `"scripts"` par `"create": "node ./services/dbConnect createTables"`. Nous allons utiliser cela pour exécuter le fichier `dbConnect` que nous allons créer.

Créez un fichier `services/dbConnect` pour contenir le code suivant :

```javascript

const pg = require("pg");

const config = {
  user: "tutorial",
  database: "tutorial",
  password: "tutorial",
  port: 5432,
  max: 10, // nombre maximum de clients dans le pool
  idleTimeoutMillis: 30000,
};

const pool = new pg.Pool(config);

pool.on("connect", () => {
  console.log("connecté à la base de données");
});

const createTables = () => {
  const imageTable = `CREATE TABLE IF NOT EXISTS
    images(
      id SERIAL PRIMARY KEY,
      title VARCHAR(128) NOT NULL,
      cloudinary_id VARCHAR(128) NOT NULL,
      image_url VARCHAR(128) NOT NULL
    )`;
  pool
    .query(imageTable)
    .then((res) => {
      console.log(res);
      pool.end();
    })
    .catch((err) => {
      console.log(err);
      pool.end();
    });
};

pool.on("remove", () => {
  console.log("client supprimé");
  process.exit(0);
});

// exporter pool et createTables pour être accessibles depuis n'importe où dans l'application
module.exports = {
  createTables,
  pool,
};

require("make-runnable");


```

Maintenant, nous sommes prêts à créer la table dans notre base de données. Si vous êtes prêt, c'est parti !

Exécutez le code suivant dans votre terminal :

```javascript

  npm run create


```

Si l'image ci-dessous est votre résultat, alors vous êtes prêt à continuer :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/fjk5ty113j5p7kaxveqc.JPG)

Vérifiez votre **pgAdmin**, et vous devriez avoir votre table correctement installée dans votre base de données comme dans l'image ci-dessous :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/sj7gy6d86vm7ay3d8a74.JPG)

D'accord, c'a été un long chemin. Il est temps d'unir Node, Postgres et Cloudinary.

## Comment créer des endpoints pour stocker et récupérer des enregistrements d'images

### Endpoint 1 : Persister une image

Tout d'abord, requérez le fichier `dbConnect.js` en haut du fichier `app.js` comme suit :

```javascript
  const db = require('services/dbConnect.js');

```

Ensuite, dans le fichier `app.js`, créez un nouvel endpoint _(persist-image)_ avec le code suivant :

```javascript

// persister une image
app.post("/persist-image", (request, response) => {
  // image collectée depuis un utilisateur
  const data = {
    title: request.body.title,
    image: request.body.image,
  }

  // télécharger l'image ici
  cloudinary.uploader.upload(data.image)
  .then().catch((error) => {
    response.status(500).send({
      message: "échec",
      error,
    });
  });
})


```

Remplacez le bloc `then` par le code suivant :

```javascript

.then((image) => {
    db.pool.connect((err, client) => {
      // requête d'insertion à exécuter si le téléchargement vers cloudinary est réussi
      const insertQuery = 'INSERT INTO images (title, cloudinary_id, image_url) 
         VALUES($1,$2,$3) RETURNING *';
      const values = [data.title, image.public_id, image.secure_url];
    })
  })


```

Les `image.public_id` et `image.secure_url` sont obtenus comme partie des détails retournés pour une image après que l'image a été téléchargée avec succès vers Cloudinary.

Nous gardons maintenant une trace de `image.public_id` et `image.secure_url` (comme vous pouvez le voir dans le code ci-dessus) afin de l'utiliser pour récupérer, mettre à jour ou supprimer l'enregistrement de l'image lorsque nous le souhaitons.

D'accord, continuons !

Toujours dans le bloc `then`, ajoutez le code suivant sous la requête que nous avons créée :

```javascript

// exécuter la requête
client.query(insertQuery, values)
      .then((result) => {
        result = result.rows[0];

        // envoyer une réponse de succès
        response.status(201).send({
          status: "success",
          data: {
            message: "Image téléchargée avec succès",
            title: result.title,
            cloudinary_id: result.cloudinary_id,
            image_url: result.image_url,
          },
        })
      }).catch((e) => {
        response.status(500).send({
          message: "échec",
          e,
        });
      })


```

Ainsi, notre endpoint `persist-image` ressemble maintenant à ceci :

```javascript

// persister une image
app.post("/persist-image", (request, response) => {
  // image collectée depuis un utilisateur
  const data = {
    title: request.body.title,
    image: request.body.image
  }

  // télécharger l'image ici
  cloudinary.uploader.upload(data.image)
  .then((image) => {
    db.pool.connect((err, client) => {
      // requête d'insertion à exécuter si le téléchargement vers cloudinary est réussi
      const insertQuery = 'INSERT INTO images (title, cloudinary_id, image_url) 
         VALUES($1,$2,$3) RETURNING *';
      const values = [data.title, image.public_id, image.secure_url];

      // exécuter la requête
      client.query(insertQuery, values)
      .then((result) => {
        result = result.rows[0];

        // envoyer une réponse de succès
        response.status(201).send({
          status: "success",
          data: {
            message: "Image téléchargée avec succès",
            title: result.title,
            cloudinary_id: result.cloudinary_id,
            image_url: result.image_url,
          },
        })
      }).catch((e) => {
        response.status(500).send({
          message: "échec",
          e,
        });
      })
    })  
  }).catch((error) => {
    response.status(500).send({
      message: "échec",
      error,
    });
  });
});


```

**Testons maintenant tout notre travail acharné :**

Ouvrez votre _postman_ et testez votre endpoint comme dans l'image ci-dessous. Le mien a réussi. J'espère que le vôtre n'a pas d'erreurs non plus ?

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/euxsoyb821v85uv5rhml.JPG)

Ouvrez votre console/tableau de bord Cloudinary et vérifiez votre `media Library`. Votre nouvelle image devrait être là confortablement comme la mienne ci-dessous :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/dxy5fl8fodqpn89oltzh.JPG)

Et maintenant, la principale raison pour laquelle nous sommes ici : vérifiez la table `images` dans votre **pgAdmin**. La mienne est ce que vous voyez ci-dessous :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ypv6vcrocsgp13owq5dv.JPG)

Oohlala ! Nous sommes arrivés aussi loin. Prenez une pause si vous en avez besoin. Je serai ici à votre retour. :)

Si vous êtes prêt, alors récupérons l'image que nous avons persistée il y a un moment.

### Endpoint 2 : Récupérer une image

Commencez avec ce code :

```javascript

app.get("/retrieve-image/:cloudinary_id", (request, response) => {

});


```

Ensuite, nous devons collecter un ID unique de l'utilisateur pour récupérer une image particulière. Ajoutez donc `const { id } = request.params;` au code ci-dessus comme suit :

```javascript

app.get("/retrieve-image/:cloudinary_id", (request, response) => {
  // données de l'utilisateur
  const { cloudinary_id } = request.params;

});


```

Ajoutez le code suivant juste en dessous du code ci-dessus :

```javascript

db.pool.connect((err, client) => {
      // requête pour trouver l'image
    const query = "SELECT * FROM images WHERE cloudinary_id = $1";
    const value = [cloudinary_id];
    });


```

Sous la requête, exécutez la requête avec le code suivant :

```javascript

// exécuter la requête
    client
      .query(query, value)
      .then((output) => {
        response.status(200).send({
          status: "success",
          data: {
            id: output.rows[0].cloudinary_id,
            title: output.rows[0].title,
            url: output.rows[0].image_url,
          },
        });
      })
      .catch((error) => {
        response.status(401).send({
          status: "failure",
          data: {
            message: "impossible de récupérer l'enregistrement !",
            error,
          },
        });
      });


```

Maintenant, notre API `retrieve-image` ressemble à ceci :

```javascript

app.get("/retrieve-image/:cloudinary_id", (request, response) => {
  // données de l'utilisateur
  const { cloudinary_id } = request.params;
  
  db.pool.connect((err, client) => {
    // requête pour trouver l'image
    const query = "SELECT * FROM images WHERE cloudinary_id = $1";
    const value = [cloudinary_id];

    // exécuter la requête
    client
      .query(query, value)
      .then((output) => {
        response.status(200).send({
          status: "success",
          data: {
            id: output.rows[0].cloudinary_id,
            title: output.rows[0].title,
            url: output.rows[0].image_url,
          },
        });
      })
      .catch((error) => {
        response.status(401).send({
          status: "failure",
          data: {
            message: "impossible de récupérer l'enregistrement !",
            error,
          },
        });
      });
  });
});


```

**Voyons comment nous nous en sommes sortis :**

Dans votre postman, copiez le `cloudinary_id` et ajoutez-le à l'URL comme dans l'image ci-dessous :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/9bmutxbmitgznqnnwmny.JPG)

YEEESSS ! Nous pouvons également récupérer notre image.

Si vous êtes ici, alors vous méritez une salve d'applaudissements et une ovation debout pour votre assiduité.

Félicitations ! Vous venez d'atteindre un grand jalon.

Le code pour stocker et récupérer les enregistrements d'images est [ici](https://github.com/EBEREGIT/server-tutorial/tree/create-APIs).

## Comment mettre à jour et supprimer un enregistrement d'image

Nous allons maintenant voir comment supprimer et mettre à jour un enregistrement d'image si nécessaire. Commençons par l'endpoint de suppression.

### Endpoint de suppression

Dans le fichier app.js, commencez avec le code suivant :

```javascript

// supprimer une image
app.delete("delete-image/:cloudinary_id", (request, response) => {

});


```

Ensuite, nous voulons obtenir l'ID unique de l'image que nous voulons supprimer de l'URL, c'est-à-dire `cloudinary_id`. Donc à l'intérieur du code ci-dessus, ajoutez :

```javascript

const { cloudinary_id } = request.params;


```

Nous commençons maintenant le processus de suppression.

Tout d'abord, nous supprimons de Cloudinary. Ajoutez le code suivant pour supprimer l'image de Cloudinary :

```javascript

cloudinary.uploader
    .destroy(cloudinary_id)
    .then((result) => {
      response.status(200).send({
        message: "success",
        result,
      });
    })
    .catch((error) => {
      response.status(500).send({
        message: "Failure",
        error,
      });
    });


```

À ce stade, notre API peut supprimer l'image de Cloudinary uniquement (vous pouvez le vérifier dans postman). Mais nous voulons également nous débarrasser de l'enregistrement que nous avons dans notre base de données Postgres.

Deuxièmement, nous supprimons de notre base de données Postgres. Pour ce faire, remplacez le code dans le bloc `then` par la requête suivante :

```javascript

db.pool.connect((err, client) => {
     
      // requête de suppression
      const deleteQuery = "DELETE FROM images WHERE cloudinary_id = $1";
      const deleteValue = [cloudinary_id];

})

```

Exécutez la requête avec le code suivant en dessous :

```javascript

// exécuter la requête de suppression
      client.query(deleteQuery, deleteValue)
      .then((deleteResult) => {
        response.status(200).send({
          message: "Image supprimée avec succès !",
          deleteResult
        });
      }).catch((e) => {
        response.status(500).send({
          message: "L'image n'a pas pu être supprimée !",
          e
        });
      });


```

Ainsi, notre endpoint devrait ressembler à ceci :

```javascript

// supprimer une image
app.delete("/delete-image/:cloudinary_id", (request, response) => {
  // ID unique
  const { cloudinary_id } = request.params;

  // supprimer l'image de cloudinary d'abord
  cloudinary.uploader
    .destroy(cloudinary_id)

    // supprimer l'enregistrement de l'image de postgres également
    .then(() => {
      db.pool.connect((err, client) => {
     
      // requête de suppression
      const deleteQuery = "DELETE FROM images WHERE cloudinary_id = $1";
      const deleteValue = [cloudinary_id];

      // exécuter la requête de suppression
      client
        .query(deleteQuery, deleteValue)
        .then((deleteResult) => {
          response.status(200).send({
            message: "Image supprimée avec succès !",
            deleteResult,
          });
        })
        .catch((e) => {
          response.status(500).send({
            message: "L'image n'a pas pu être supprimée !",
            e,
          });
        });
      })
    })
    .catch((error) => {
      response.status(500).send({
        message: "Failure",
        error,
      });
    });
});


```

Le moment est venu pour nous de mettre notre endpoint à l'épreuve.

Voici ma bibliothèque de médias Cloudinary avec deux images que j'ai déjà téléchargées. Notez leur ID unique (`public_id`).

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/sjir185on5pqrlzrc1hl.JPG)

Si vous n'avez pas déjà cela, veuillez utiliser l'endpoint persist-image pour télécharger quelques images.

Maintenant, procédons à postman :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/beu5lleymnffa5vyzj97.JPG)

Remarquez l'ID unique tel qu'il correspond à l'une des images de ma bibliothèque de médias Cloudinary.

D'après le résultat, nous avons exécuté la commande DELETE et cela a supprimé une ROW de notre TABLE d'images dans notre base de données.

Maintenant, voici ma bibliothèque de médias avec l'une des images restantes :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/8d7rs33580c4ewpcipbr.JPG)

Walahhhh... Nous sommes maintenant capables de nous débarrasser d'une image.

Prenez une pause si vous en avez besoin. 

Si vous êtes prêt, je suis prêt à mettre à jour les images.

### API de mise à jour d'image

En dessous de l'API `delete-image`, commençons à créer l'API `update-image` avec le code suivant :

```javascript

// mettre à jour une image
app.put("/update-image/:cloudinary_id", (request, response) => {

});

Tous les codes seront là.


```

Collectez l'ID unique de Cloudinary et les nouveaux détails de l'image de l'utilisateur avec le code suivant :

```javascript

// ID unique
  const { cloudinary_id } = request.params;

// image collectée depuis un utilisateur
  const data = {
    title: request.body.title,
    image: request.body.image,
  };


```

Supprimez l'image de Cloudinary avec le code suivant :

```javascript

// supprimer l'image de cloudinary d'abord
  cloudinary.uploader
    .destroy(cloudinary_id)
      // télécharger l'image ici
    .then()
    .catch((error) => {
      response.status(500).send({
        message: "échec",
        error,
      });
    });


```

Ensuite, téléchargez une autre image vers Cloudinary. Pour ce faire, entrez le code suivant dans le bloc `then` :

```javascript

() => {
      cloudinary.uploader
        .upload(data.image)
        .then()
        .catch((err) => {
          response.status(500).send({
            message: "échec",
            err,
          });
        });
    }


```

Maintenant, remplaçons notre enregistrement initial par les nouveaux détails de l'image. Remplacez le contenu du bloc `then` par ce qui suit :

```javascript

(result) => {
          db.pool.connect((err, client) => {
            
            // requête de mise à jour
            const updateQuery =
              "UPDATE images SET title = $1, cloudinary_id = $2, image_url = $3 WHERE cloudinary_id = $4";
            const value = [
              data.title,
              result.public_id,
              result.secure_url,
              cloudinary_id,
            ];
          });
        }


```

Nous exécutons la requête en utilisant le code suivant juste en dessous de la déclaration de la requête :

```javascript

// exécuter la requête
            client
              .query(updateQuery, value)
              .then(() => {

                // envoyer une réponse de succès
                response.status(201).send({
                  status: "success",
                  data: {
                    message: "Image mise à jour avec succès"
                  },
                });
              })
              .catch((e) => {
                response.status(500).send({
                  message: "Mise à jour échouée",
                  e,
                });
              });


```

À ce stade, voici ce que j'ai :

```javascript

// mettre à jour une image
app.put("/update-image/:cloudinary_id", (request, response) => {
  // ID unique
  const { cloudinary_id } = request.params;

  // image collectée depuis un utilisateur
  const data = {
    title: request.body.title,
    image: request.body.image,
  };

    // supprimer l'image de cloudinary d'abord
    cloudinary.uploader
      .destroy(cloudinary_id)

      // télécharger l'image ici
      .then(() => {
        cloudinary.uploader
          .upload(data.image)

          // mettre à jour la base de données ici
          .then((result) => {
            db.pool.connect((err, client) => {
            // requête de mise à jour
            const updateQuery =
              "UPDATE images SET title = $1, cloudinary_id = $2, image_url = $3 WHERE cloudinary_id = $4";
            const value = [
              data.title,
              result.public_id,
              result.secure_url,
              cloudinary_id,
            ];

            // exécuter la requête
            client
              .query(updateQuery, value)
              .then(() => {

                // envoyer une réponse de succès
                response.status(201).send({
                  status: "success",
                  data: {
                    message: "Image mise à jour avec succès"
                  },
                });
              })
              .catch((e) => {
                response.status(500).send({
                  message: "Mise à jour échouée",
                  e,
                });
              });
            });
          })
          .catch((err) => {
            response.status(500).send({
              message: "échec",
              err,
            });
          });
      })
      .catch((error) => {
        response.status(500).send({
          message: "échec",
          error,
        });
      });
  
});


```

C'est l'heure du test !

Voici mon postman dans l'image ci-dessous :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/jowr0guiazmqkhx1mmls.JPG)

Notez l'ID unique de cloudinary qui correspond à l'image restante dans ma bibliothèque de médias Cloudinary.

Maintenant, jetez un coup d'œil à ma bibliothèque de médias Cloudinary dans l'image qui suit :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/td9rpqovhh2kl6ytc2u4.JPG)

Notez la nouvelle image remplaçant l'initiale dans ma bibliothèque de médias ci-dessus.

Aussi, voyez que l'ID unique de Cloudinary correspond à celui dans ma base de données avec le nouveau titre. Voir l'image ci-dessous :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/wu3mydrn71x3azyd75ee.JPG)

Yayeh ! Vous avez fait un travail formidable ! 

Nous venons de compléter une application de gestion d'images avec Node.js, Cloudinary et Postgres.

## Optimisation du code avec le routage Express

Le routage Express nous permet de rendre notre code Node.js plus optimisé ou de lui donner une structure plus modulaire en séparant la logique métier des contrôleurs. Nous allons utiliser cela pour nettoyer notre code jusqu'à présent.

Nous allons commencer par créer un nouveau dossier avec le nom `routes` dans le répertoire racine :

```javascript

mk dir routes


```

Dans le dossier routes, créez un fichier avec le nom : `routes.js`.

Pour Windows :

```javascript

echo . > routes.js


```

Pour Mac :

```javascript

touch routes.js


```

Videz le fichier `routes.js` s'il y a quelque chose et entrez le code suivant :

```javascript

const express = require('express');

const router = express.Router();



module.exports = router;


```

Ajoutez le code suivant au-dessus de la dernière ligne :

```javascript

const cloudinary = require("cloudinary").v2;
require("dotenv").config();
const db = require("../services/dbConnect.js");

// configuration cloudinary
cloudinary.config({
  cloud_name: process.env.CLOUD_NAME,
  api_key: process.env.API_KEY,
  api_secret: process.env.API_SECRET,
});


```

De retour dans le fichier App.js, supprimez le code suivant :

```javascript

const cloudinary = require("cloudinary").v2;
require("dotenv").config();
const db = require("./services/dbConnect.js");

// configuration cloudinary
cloudinary.config({
  cloud_name: process.env.CLOUD_NAME,
  api_key: process.env.API_KEY,
  api_secret: process.env.API_SECRET,
});


```

Déplacez toutes les API vers `routes.js`.

Changez toutes les occurrences de `app` en `router` soigneusement.

Mon fichier `routes.js` ressemble maintenant à [ceci](https://github.com/EBEREGIT/server-tutorial/blob/routing/routes/routes.js).

De retour dans le fichier `app.js`, importez le fichier `routes.js` comme suit :

```javascript

// importer le fichier des routes
const routes = require("./routes/routes")


```

Maintenant, enregistrez les routes comme suit :

```javascript

// enregistrer les routes 
app.use('/', routes);


```

Voici à quoi ressemble mon fichier `app.js` pour le moment :

```javascript

const express = require("express");
const app = express();

// importer le fichier des routes
const routes = require("./routes/routes")

// configuration du body parser
const bodyParser = require("body-parser");
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// enregistrer les routes 
app.use('/', routes);

module.exports = app;


```

Il est temps de tester et de voir si nos routes fonctionnent toujours comme avant.

Assurez-vous que les vôtres fonctionnent comme les miennes ci-dessous :

#### persist-image

![persist image](https://dev-to-uploads.s3.amazonaws.com/i/r2uz54xix054li4lgw6i.JPG)

#### retrieve-image

![retrieve image](https://dev-to-uploads.s3.amazonaws.com/i/o44a1dnfgvz3r9sv3a1j.JPG)

#### update-image

![update image](https://dev-to-uploads.s3.amazonaws.com/i/6t9k5m079rwx4p6ouax3.JPG)

#### delete-image

![delete image](https://dev-to-uploads.s3.amazonaws.com/i/nkkydplioi68la4eynhp.JPG)

Wow ! Nous avons réussi à séparer nos routes de notre fichier `app.js`.

Le code pour cela est [ici](https://github.com/EBEREGIT/server-tutorial/tree/routing).

Même si notre fichier `routes.js` est encore long, nous avons une bonne base pour séparer notre logique métier de nos contrôleurs. Le moment est venu de faire exactement cela.

## Comment déplacer chaque endpoint vers un fichier différent

Commencez par créer un nouveau dossier dans le dossier `routes` et nommez-le `controllers`.

Dans le dossier controllers, créez 5 fichiers et nommez-les d'après les 5 endpoints.

Notre dossier et nos fichiers doivent être structurés comme suit :

![folder and files structure](https://dev-to-uploads.s3.amazonaws.com/i/dmren2r2w2801lf28wjy.JPG)

De retour dans le fichier routes.js, travaillons sur l'API `image-upload`. Coupez le code suivant :

```javascript

(request, response) => {
  // image collectée depuis un utilisateur
  const data = {
    image: request.body.image,
  };

  // télécharger l'image ici
  cloudinary.uploader
    .upload(data.image)
    .then((result) => {
      response.status(200).send({
        message: "success",
        result,
      });
    })
    .catch((error) => {
      response.status(500).send({
        message: "failure",
        error,
      });
    });
}


```

Dans le fichier `imageUpload`, égalisez le code que vous avez déjà coupé de l'endpoint `image-upload` à `exports.imageUpload` comme suit :

```javascript

exports.imageUpload = (request, response) => {
    // image collectée depuis un utilisateur
    const data = {
      image: request.body.image,
    };
  
    // télécharger l'image ici
    cloudinary.uploader
      .upload(data.image)
      .then((result) => {
        response.status(200).send({
          message: "success",
          result,
        });
      })
      .catch((error) => {
        response.status(500).send({
          message: "failure",
          error,
        });
      });
  }


```

Maintenant, importons ce qui est nécessaire pour que ce code fonctionne. Voici à quoi ressemble mon fichier `imageUpload` pour le moment :

```javascript

const cloudinary = require("cloudinary").v2;
require("dotenv").config();

// configuration cloudinary
cloudinary.config({
  cloud_name: process.env.CLOUD_NAME,
  api_key: process.env.API_KEY,
  api_secret: process.env.API_SECRET,
});

exports.imageUpload = (request, response) => {
    // image collectée depuis un utilisateur
    const data = {
      image: request.body.image,
    };
  
    // télécharger l'image ici
    cloudinary.uploader
      .upload(data.image)
      .then((result) => {
        response.status(200).send({
          message: "success",
          result,
        });
      })
      .catch((error) => {
        response.status(500).send({
          message: "failure",
          error,
        });
      });
  }


```

Importons et enregistrons l'API `imageUpload` dans le fichier `routes.js` comme suit :

```javascript

const imageUpload = require("./controllers/imageUpload");

// API de téléchargement d'image
router.post("image-upload", imageUpload.imageUpload);


```

Maintenant, nous avons cette ligne de code pointant vers l'API `imageUpload` dans le fichier `imageUpload.js` depuis le fichier `routes.js`.

C'est génial ! Notre code est plus lisible.

Assurez-vous de tester l'API pour être sûr qu'elle fonctionne correctement. La mienne fonctionne parfaitement. Voir l'image ci-dessous :

![image upload test result](https://dev-to-uploads.s3.amazonaws.com/i/t456z1fz1537nja0huyr.JPG)

Maintenant, c'est à vous !

Appliquez ce que vous avez appris aux autres API. Voyons ce que vous avez.

Je vous attendrai de l'autre côté...

Si vous êtes ici, alors je crois que vous avez fait les vôtres et qu'ils fonctionnent parfaitement – ou du moins, vous avez déjà donné le meilleur de vous-même. Félicitations !

Consultez les miens [ici](https://github.com/EBEREGIT/server-tutorial/tree/controller-setup/routes).

Félicitations. Vous êtes génial :)

Le code d'optimisation du code est [ici](https://github.com/EBEREGIT/server-tutorial/tree/controller-setup).

D'accord, passons à l'étape suivante.

## Comment déployer sur GitHub et Heroku

Maintenant que nous avons terminé notre application, déployons-la sur Heroku afin de pouvoir y accéder même sans être sur notre ordinateur portable où le code a été écrit.

Je vais vous guider à travers le téléchargement de notre application sur [GitHub](https://github.com/) et son déploiement sur [Heroku](https://heroku.com/).

Sans plus tarder, mettons-nous au travail.

## Comment télécharger le code sur GitHub

Télécharger ou pousser sur GitHub est aussi facile que de manger votre repas préféré. Consultez [cette ressource](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-an-existing-project-to-github-using-the-command-line) pour apprendre comment pousser votre projet de votre machine locale vers GitHub.

## Comment déployer sur Heroku

Commençons par créer un compte sur [Heroku](https://heroku.com/).

Si vous avez créé un compte, il se peut que vous ayez été invité à créer une application (c'est-à-dire un dossier où votre application sera hébergée). Vous pouvez le faire, mais je vais le faire en utilisant mon terminal puisque le terminal vient avec quelques fonctionnalités supplémentaires dont nous aurons besoin plus tard.

Ouvrez votre projet dans un terminal si vous ne l'avez pas déjà fait. Je vais utiliser le terminal intégré de VS Code.

Installez Heroku CLI :

```javascript
npm install heroku

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/716g1v0nnea93rdrhmk5.JPG)

Connectez-vous à Heroku CLI. Cela ouvrira une fenêtre de navigateur, que vous pouvez utiliser pour vous connecter.

```javascript
heroku login

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/bky4mywipzua8cj6d0kf.JPG)

Créez une application. Elle peut avoir n'importe quel nom. J'utilise `node-postgres-cloudinary`.

```javascript
heroku create node-postgres-cloudinary

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ibofc7xcyqgi165f5dz1.JPG)

Allez sur votre [tableau de bord Heroku](https://dashboard.heroku.com/apps) et vous trouverez la nouvelle application créée.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/d84emoge8pi9qt0a2qrb.JPG)

Waalaah !

Voici à quoi ressemble le mien dans l'image ci-dessus. J'ai déjà quelques applications là-bas, mais vous pouvez voir celle que je viens de créer.

Ajoutons maintenant la base de données PostgreSQL à l'application.

### Comment ajouter Heroku Postgres

Cliquez sur l'application que vous venez de créer. Cela vous amènera au tableau de bord de l'application.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/g48iadulci1evt6j8ftf.JPG)

Cliquez sur l'onglet/menu `Resources`.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/e6bvzsv7cn6ebgwi0y65.JPG)

Dans la section `Add-ons`, recherchez et sélectionnez `Heroku Postgres`.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/91nwppclfdkvitp56rrj.JPG)

Assurez-vous de sélectionner le plan `Hobby Dev - Free` dans la fenêtre contextuelle qui suit :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/hd7zj1qa2t4e051zn654.JPG)

Cliquez sur le bouton `provision` pour l'ajouter à l'application comme suit :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/8w2z6tok8plmp154ovuj.JPG)

Cliquez sur `Heroku Postgres` pour accéder au tableau de bord `Heroku Postgres`.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/nvrdf902ypuz2frqiu1q.JPG)

Cliquez sur l'onglet `settings` :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/6k81alizfc5yzgtbzlcv.JPG)

Cliquez sur `View Credentials` :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/33p2ceyfkbmr590s1r6b.JPG)

Dans les identifiants, nous nous intéressons à l'Heroku CLI. Nous allons l'utiliser dans un instant.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/xzmtjtqrg8a5vqrfjkg3.JPG)

Retour au terminal.

Confirmons si `Heroku Postgres` a été ajouté avec succès. Entrez ce qui suit dans le terminal :

```javascript
heroku addons

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/7hhl70mw99b2mrji9i35.JPG)

Yeeeeaaaah ! Il a été ajouté avec succès.

Avant de continuer, **assurez-vous que votre chemin `PostgreSQL` est correctement défini si vous êtes sur Windows**. Suivez ce [lien](https://www.computerhope.com/issues/ch000549.htm) pour apprendre comment définir un `chemin`. Le chemin doit être comme ceci : `C:\Program Files\PostgreSQL\<VERSION>\bin`.

La version dépendra de celle installée sur votre machine. La mienne est : `C:\Program Files\PostgreSQL\12\bin` puisque j'utilise la `version 12`.

L'image suivante pourrait être utile :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/dl3wv0z1dtvyjvvusx26.JPG)

Vous devrez peut-être naviguer jusqu'au dossier où PostgreSQL est installé sur votre machine pour trouver votre propre chemin.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/bzf04c5827d4tri3ngrg.JPG)

Connectez-vous à `Heroku Postgres` en utilisant le [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) à partir de nos [identifiants](https://devcenter.heroku.com/articles/heroku-postgresql-credentials) Heroku Postgres. Voici le mien – le vôtre sera différent :

```javascript
heroku pg:psql postgresql-slippery-19135 --app node-postgres-cloudinary

```

Si vous avez obtenu une erreur, c'est probablement parce que votre chemin n'est pas correctement défini.

### Comment préparer notre connexion à la base de données pour correspondre à celle de Heroku

Pour le moment, ma base de données ressemble à ceci :

```javascript

const pg = require("pg");

const config = {
  user: "tutorial",
  database: "tutorial",
  password: "tutorial",
  port: 5432,
  max: 10, // nombre maximum de clients dans le pool
  idleTimeoutMillis: 30000,
};

const pool = new pg.Pool(config);

pool.on("connect", () => {
  console.log("connecté à la base de données");
});


```

Si vous essayez de connecter Heroku à cela, vous allez obtenir une erreur. Cela est dû au fait que Heroku a déjà une `chaîne de connexion` configurée. Nous devons donc configurer notre connexion de manière à ce que Heroku puisse facilement se connecter.

Je vais refactoriser mon fichier de connexion à la base de données (`dbConnect.js`) et le fichier `.env` pour que cela se produise.

* dbConnect.js

```javascript

const pg = require('pg');
require('dotenv').config();

// définir la variable de production. Cela sera appelé lorsque déployé sur un hôte live
const isProduction = process.env.NODE_ENV === 'production';

// détails de configuration
const connectionString = `postgresql://${process.env.DB_USER}:${process.env.DB_PASSWORD}@${process.env.DB_HOST}:${process.env.DB_PORT}/${process.env.DB_DATABASE}`;

// si le projet a été déployé, connectez-vous avec l'URL de la base de données de l'hôte
// sinon connectez-vous avec l'URL de la base de données locale
const pool = new pg.Pool({
  connectionString: isProduction ? process.env.DATABASE_URL : connectionString,
  ssl: isProduction,
});

// afficher un message de succès si réussi
pool.on('connect', () => {
  console.log('Base de données Teamwork connectée avec succès !');
});


```

* fichier .env

```javascript

DB_USER="tutorial"
DB_PASSWORD="tutorial"
DB_HOST="localhost"
DB_PORT="5432"
DB_DATABASE="tutorial"


```

Avec la configuration du fichier `dbconnect` et `.env`, nous sommes prêts à exporter notre base de données et nos tables de notre machine locale vers `heroku postgres`.

### Comment exporter la base de données et les tables

Allez dans votre `pgAdmin` et localisez la base de données pour ce tutoriel. La mienne est tutorial.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/m454dij54j7dghsxqa25.JPG)

Faites un clic droit dessus et sélectionnez `Backup`. Cela ouvrira une nouvelle fenêtre.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/u57h6kpw5gtbhublc1la.JPG)

Entrez un nom pour le fichier SQL comme je l'ai fait. Sélectionnez le format `plain`. Ensuite, cliquez sur Backup. Cela enregistrera le fichier dans votre dossier de documents.

Localisez le fichier et déplacez-le dans le répertoire du projet. Il peut être n'importe où dans le répertoire, mais je choisis de déplacer le mien dans le répertoire `services` car il contient les fichiers liés à la base de données.

De retour dans le terminal, naviguez jusqu'au dossier contenant le fichier SQL et exécutez le code suivant pour ajouter les tables que nous venons d'exporter à la base de données `heroku postgres` :

```html
cat <votre-fichier-SQL> | <heroku-CLI-depuis-les-identifiants-heroku-posgres>

```

Voici à quoi ressemble le mien :

```javascript
cat tutorial.sql | heroku pg:psql postgresql-slippery-19135 --app node-postgres-cloudinary

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/67x0f9521g5savkrafpc.JPG)

Avez-vous remarqué que j'ai changé de répertoire pour services (`cd services`) ? C'est là que se trouve mon fichier `sql`.

Wow ! Nous venons de réussir à exporter notre base de données et nos tables vers Heroku.

C'est presque terminé...

### Comment dire à GitHub que nous avons fait des changements

Ajoutez les fichiers que nous avons modifiés :

```javascript
$ git add .

```

Le point (`.`) ajoute tous les fichiers.

Validez vos derniers changements :

```javascript
$ git commit -m "refactored the dbConnect and .env file to fit in to heroku; Added the database SQL file"

```

Poussez les fichiers validés :

```javascript
$ git push origin -u master

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/u8kogsya1gt3uxnujz35.JPG)

### Enfin, déployer notre application

Allez sur le tableau de bord de votre application :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4j4bi64n0f0bp65j7pb7.JPG)

Sélectionnez la méthode de déploiement GitHub :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/5edwt90cpy75b3uyqgvy.JPG)

Recherchez et sélectionnez un dépôt, puis cliquez sur `connect` :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ifg4zh7jzab3edpaxvnf.JPG)

Sélectionnez la branche que vous souhaitez déployer (dans mon cas, c'est la branche `master`) :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4ka9c6781vft1gio7p0k.JPG)

Activez le déploiement automatique en cliquant sur le bouton `Enable automatic deployment` comme dans l'image ci-dessus.

Cliquez sur le bouton `Deploy` dans le déploiement manuel

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/7ksrclnfyjzzvn2nr4gc.JPG)

Nous n'aurons pas à faire tout cela pour les déploiements ultérieurs.

Maintenant, vous avez un bouton qui vous dit de "view site" après la fin de la construction. Cliquez dessus. Cela ouvrira votre application dans un nouvel onglet.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/9xi5vx6lx99z49uscre6.JPG)

**Oh non ! Un bug ? Erreur d'application ??**

Ne vous inquiétez pas, ce n'est qu'un petit problème. Quelque chose que vous ne devriez jamais oublier de faire lors des déploiements. La plupart des services d'hébergement l'exigeront.

### Comment corriger l'erreur d'application Heroku

Retournez au répertoire racine de votre projet.

Créez un fichier et nommez-le `Procfile` (il n'a pas d'extension).

Dans le fichier, entrez le code suivant :

```javascript
web: node index.js

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/k3jb0rof1g6bs1zs2eh6.JPG)

Cela dirige Heroku vers le fichier serveur (`index.js`) qui est le point d'entrée de l'application. Si votre serveur est dans un fichier différent, veuillez modifier comme requis.

Enregistrez le fichier et poussez les nouveaux changements vers GitHub.

Attendez 2 à 5 minutes pour que Heroku détecte automatiquement les changements dans votre dépôt GitHub et rende les changements sur l'application.

Vous pouvez maintenant actualiser cette page d'erreur et voir votre travail acharné porter ses fruits :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/n4t9yp4598wc5i7v8p82.JPG)

Vous pouvez également tester la route `retrieve image` et voir qu'elle fonctionne.

Félicitations ! Quel exploit vous avez accompli.

Les autres routes **(persist-image, update-image, et delete-image)** ne fonctionneront pas car nous n'avons pas provisionné ou ajouté l'add-on `cloudinary`. C'est aussi simple que celui de `PostgreSQL` que nous venons de faire. Vous pouvez donc essayer.

## Conclusion

Nous avons commencé ce tutoriel avec l'objectif d'apprendre à construire une application backend en utilisant Express, Postgres, Cloudinary, Github et Heroku.

Nous avons appris à stocker, récupérer, supprimer et mettre à jour un enregistrement d'image. Nous avons ensuite organisé notre code avec le routage Express, l'avons poussé vers GitHub et l'avons déployé sur Heroku. C'était beaucoup.

J'espère que vous serez d'accord pour dire que cela en valait la peine car nous avons appris beaucoup. Vous devriez essayer d'ajouter l'add-on Cloudinary vous-même pour affiner encore plus vos connaissances.

Merci d'avoir lu !