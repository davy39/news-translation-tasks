---
title: Comment télécharger des fichiers vers Amazon S3 avec Node.js
subtitle: ''
author: Fiyin Akinsiku
co_authors: []
series: null
date: '2023-04-25T16:31:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-upload-files-to-aws-s3-with-node
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-cottonbro-studio-3584994.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: node js
  slug: node-js
seo_title: Comment télécharger des fichiers vers Amazon S3 avec Node.js
seo_desc: "File upload is a common feature in a lot of modern applications. These\
  \ platforms accept different file formats, including jpeg, png, gif, pdf, txt, zip,\
  \ and mp3. \nSome applications will also restrict uploads to a specific file type.\
  \ For example, when..."
---

Le téléchargement de fichiers est une fonctionnalité courante dans de nombreuses applications modernes. Ces plateformes acceptent différents formats de fichiers, notamment jpeg, png, gif, pdf, txt, zip et mp3. 

Certaines applications restreignent également les téléchargements à un type de fichier spécifique. Par exemple, lors du téléchargement de votre CV sur LinkedIn, vous verrez un sous-texte spécifiant DOC, DOCX et PDF.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screen-Shot-2023-03-27-at-10.08.32-AM.png)
_Page de téléchargement de CV sur LinkedIn_

D'autres cas d'utilisation du téléchargement de fichiers sont :

* Ajouter une photo de profil sur Instagram.
* Ajouter une image de produit à une boutique Shopify.
* Ajouter une capture d'écran à un tutoriel freeCodeCamp.
* Vendre des produits numériques tels que des fichiers PDF sur Selar.

Où vont les fichiers téléchargés ? Il est conseillé d'enregistrer vos fichiers en utilisant des fournisseurs de services de stockage cloud. Ils permettent aux utilisateurs d'accéder au fichier depuis n'importe où. Ils offrent également un stockage sécurisé pour les fichiers. Par exemple, Amazon Simple Storage Service (S3) dispose de paramètres de politique d'accès qui vous permettent de déterminer qui a accès à votre bucket S3.

Vous pouvez en savoir plus sur la sécurité et la gestion des accès Amazon S3 sur le [site officiel](https://aws.amazon.com/s3/security/).

Dans ce tutoriel, je vais vous montrer comment télécharger des fichiers vers un bucket S3 avec une application Node.js.

## Prérequis

Pour suivre ce tutoriel, vous devez comprendre les éléments suivants :

* HTML de base.
* Le serveur Node.js.
* Le framework Express.js.

Vous devez également disposer d'un compte AWS avec un bucket S3 actif. Il existe des étapes claires pour [configurer votre compte AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-up-s3.html#sign-up-for-aws) et [créer un bucket S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) dans la documentation AWS.

Maintenant, commençons.

## Comment créer le serveur Node.js

Cette application utilisera plusieurs packages :

* `express` : Il s'agit d'un framework [Node.js](https://www.freecodecamp.org/news/p/994c216e-e3df-47b3-8e00-2a899a78aa45/Node.js) pour les API.
* `dotenv` : Cela permet d'accéder aux variables d'environnement dans le fichier `.env`.
* `formidable` : Il s'agit d'un analyseur de données qui prend en charge les téléchargements de fichiers.
* `@aws-sdk/lib-storage` : Il s'agit d'une bibliothèque AWS SDK pour télécharger des fichiers volumineux.
* `@aws-sdk/client-s3` : Il s'agit d'un client S3 AWS SDK pour Node.js.

Installez-les en exécutant cette commande :

```js
npm install express dotenv formidable @aws-sdk/lib-storage @aws-sdk/client-s3
```

Ensuite, créez un fichier `index.js` pour configurer le serveur. Comme cette application est à des fins de tutoriel, je vais configurer le formulaire HTML dans le même fichier. Vous pouvez opter pour une configuration différente.

```javascript
const express = require('express');
const app = express();
require('dotenv').config();

app.set('json spaces', 5); // pour formater la réponse JSON

const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send(`
    <h2>Téléchargement de fichiers avec <code>"Node.js"</code></h2>
    <form action="/api/upload" enctype="multipart/form-data" method="post">
      <div>Sélectionnez un fichier : 
        <input type="file" name="file" multiple="multiple" />
      </div>
      <input type="submit" value="Télécharger" />
    </form>

  `);
});

app.listen(PORT, () => {
  console.log(`Serveur en cours d'exécution sur le port ${PORT}.`)
})
```

Démarrez le serveur avec la commande `node index.js`.

Pour confirmer que tout fonctionne comme prévu, vérifiez le message `Serveur en cours d'exécution sur le port 3000.` sur votre terminal.

Avec le serveur en cours d'exécution, ouvrez ce lien [http://127.0.0.1:3000/](http://127.0.0.1:3000) (remplacez `3000` par votre numéro de port) sur votre navigateur. Il devrait afficher un formulaire sur la page web.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screen-Shot-2023-03-24-at-12.29.33-PM.png)
_Page de formulaire pour le téléchargement de fichiers_

## Comment configurer l'analyseur de fichiers

Nous allons servir les fichiers du client vers le bucket S3 en utilisant le package Node.js `formidable`.

Le module `formidable` accepte un objet `options` qui contient une série de propriétés de fichiers. Ces propriétés ont des valeurs par défaut que vous pouvez remplacer pour configurer l'analyseur selon vos besoins. Certaines des clés sont :

* `allowEmptyFiles` : Cette clé est assignée à une valeur booléenne. Elle détermine si les fichiers vides doivent être autorisés et sa valeur est `true` par défaut.
* `minFileSize` : Cette clé accepte une valeur numérique représentant la taille de fichier la plus petite autorisée. La valeur par défaut est 1 octet.
* `maxFileSize` : Cette clé accepte également une valeur numérique. Elle représente la taille de fichier la plus grande autorisée. La valeur par défaut est 200 mégaoctets (Mo).

Je veux que mon application accepte des fichiers de taille inférieure ou égale à 100 Mo, donc je dois le définir comme option `maxFileSize` dans l'objet options.

Ouvrez un fichier `fileparser.js` et ajoutez le code ci-dessous :

```javascript
const formidable = require('formidable');

const parsefile = async (req) => {
    return new Promise((resolve, reject) => {
        let options = {
            maxFileSize: 100 * 1024 * 1024, //100 Mo convertis en octets,
            allowEmptyFiles: false
        }

        const form = formidable(options);
        
        form.parse(req, (err, fields, files) => {});
    })
}

module.exports = parsefile;

```

Ce service retourne une promesse qui se résout avec les détails du téléchargement si tout se passe bien. Sinon, elle rejette avec les détails de l'erreur pertinente. Il génère une instance de `form` qui n'accepte pas les téléchargements vides et ne traitera que les fichiers de 100 Mo ou moins. Il appelle également la méthode `form.parse()` pour traiter la requête entrante.

La méthode parse accepte deux arguments – la charge utile de la requête et une fonction de rappel. Vous pouvez accéder aux champs, aux fichiers et à toute erreur `parse()` (en tant que `err`) ici.

> Vous pouvez remplacer cette méthode si vous souhaitez accéder directement au flux multipart. Cela désactivera tout traitement des événements `'field'` / `'file'` qui se produirait sinon, vous rendant entièrement responsable de la gestion du traitement. ([Formidable](https://www.npmjs.com/package/formidable))

Nous ne remplacerons pas cette partie puisque nous avons besoin de l'instance de formulaire pour diffuser le fichier vers le bucket S3. Nous explorerons cela plus tard dans ce tutoriel.

### Comment gérer les événements de formulaire

Si vous n'êtes pas familier avec les événements en programmation, consultez cette définition avant de continuer : 

> Les événements sont des choses qui se produisent dans le système que vous programmez, et que le système vous signale afin que votre code puisse réagir à eux. ([Source : MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events))

L'instance `form` émet différents événements lors du traitement d'un fichier, notamment :

* Un événement `error` pour les erreurs dans le processus d'analyse.
* Un événement `file` lorsqu'il reçoit une paire fichier/champ.
* Un événement `progress` après l'analyse de chaque bloc de données.

Vous pouvez spécifier comment vous souhaitez gérer ces événements en utilisant la méthode `form.on()`.

La méthode `on()` accepte un nom d'événement et une fonction d'écoute, qui est déclenchée chaque fois que le formulaire émet l'événement. La requête peut parfois expirer, comme dans un événement `error`, si l'événement n'est pas géré. Vous pouvez contrôler ce qui se passe lorsque le programme émet un événement particulier dans la fonction d'écoute.

Mettez à jour le fichier `fileparser.js` avec la méthode `on()` :

```javascript
const formidable = require('formidable');

const parsefile = async (req) => {
    return new Promise((resolve, reject) => {
        let options = {
            maxFileSize: 100 * 1024 * 1024, //100 Mo convertis en octets,
            allowEmptyFiles: false
        }

        const form = formidable(options);
        
        form.parse(req, (err, fields, files) => {});

        form.on('error', error => {
            reject(error.message)
        })
        
        form.on('data', data => {
            if (data.name === "successUpload") {
                resolve(data.value);
            }
        })

        
    })
}

module.exports = parsefile;

```

L'écouteur `data` retournera une réponse réussie lorsque le téléchargement S3 sera réussi. Cependant, l'écouteur `error` écoutera les événements d'erreur et enverra la réponse d'erreur au client. 

Par exemple, j'obtiens ce message d'erreur lorsque j'essaie de télécharger un fichier vide.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screen-Shot-2023-04-24-at-10.43.29-AM.png)
_Réponse d'erreur pour un téléchargement de fichier vide_

Un autre événement que vous écouterez est l'événement `fileBegin`.

Avertissement : Je suis tombé sur cette [solution](https://github.com/node-formidable/formidable/issues/227#issuecomment-289223225) sur GitHub. Je l'ai modifiée pour l'adapter à mon cas d'utilisation, et elle a parfaitement fonctionné.

> Il est émis chaque fois qu'un nouveau fichier est détecté dans le flux de téléchargement. Utilisez cet événement si vous souhaitez diffuser le fichier ailleurs tout en mettant en mémoire tampon le téléchargement sur le système de fichiers. ([Formidable](https://www.npmjs.com/package/formidable))

### Comment créer le flux de fichiers

Un avantage du streaming est que nous n'avons pas besoin d'attendre de recevoir le fichier entier avant de le traiter. Chaque bloc de données est traité dès sa réception.

Importez la classe `Transform` du module `stream` de Node.js dans le fichier `fileparser.js`. Cette classe créera un flux de transformation qui passera en tant que corps de l'objet téléchargé.

> Le flux de transformation est un type de flux duplex qui lit les données, transforme les données, puis écrit les données transformées dans un format spécifié. ([Blog LogRocket](https://blog.logrocket.com/working-node-js-streams/#transform-streams))

Ensuite, appelez la méthode `form.on` avec un nom d'événement `fileBegin` et la fonction d'écoute.

Que fait la fonction d'écoute ici ? 

La fonction a deux paramètres – `formName` et `file`. Ils représentent respectivement le nom du formulaire contenant le fichier et l'objet fichier contenant les détails du fichier. L'accent dans cette section est mis sur l'objet `file`.

`file` est une instance de la classe `PersistentFile` de Formidable [classe](https://github.com/node-formidable/formidable/blob/master/src/PersistentFile.js) créée à partir de la classe `EventEmitter` de Node.js. La classe `PersistentFile` possède certaines méthodes, notamment `open()` et `end()`. Vous pouvez les remplacer pour déterminer ce qui se passe lorsqu'elles sont déclenchées.

Créez une fonction asynchrone pour gérer le téléchargement du flux et attribuez-la à la méthode `file.open`.

Mettez à jour le fichier `fileParser.js` comme indiqué :

```javascript
const formidable = require('formidable');
const Transform = require('stream').Transform;

const parsefile = async (req) => {
    return new Promise((resolve, reject) => {
        let options = {
            maxFileSize: 100 * 1024 * 1024, //100 Mo convertis en octets,
            allowEmptyFiles: false
        }

        const form = formidable(options);
        
        form.parse(req, (err, fields, files) => {});

        form.on('error', error => {
            reject(error.message)
        })
        
        form.on('data', data => {
            if (data.name === "successUpload") {
                resolve(data.value)
            }
        })
        
        form.on('fileBegin', (formName, file) => {

            file.open = async function () {
                this._writeStream = new Transform({
                    transform(chunk, encoding, callback) {
                        callback(null, chunk)
                    }
                })

                this._writeStream.on('error', e => {
                    form.emit('error', e)
                });
            }

        })

        
    })
}

module.exports = parsefile;

```

Cette fonction crée une instance de la classe `Transform` qui traite les blocs de données avec une méthode interne `transform`. Le flux résultant est ensuite défini comme flux d'écriture pour l'objet `file` en utilisant `this._writeStream`.

Ensuite, nous ajoutons l'écouteur `on` à `this._writeStream` pour gérer les erreurs dans le processus de streaming.

### Comment télécharger vers le bucket S3

C'est ici que le stockage des fichiers se produit.

Importez le module `Upload` du package `@aws-sdk/lib-storage` dans le fichier `fileparser.js`. Le module nous permet de télécharger le fichier en parties. Nous importerons également le `S3Client` de `@aws-sdk/client-s3`. 

```
const { Upload } = require("@aws-sdk/lib-storage");
const { S3Client, S3 } = require("@aws-sdk/client-s3");
```

Vous aurez besoin de vos identifiants AWS pour configurer le téléchargement.

* Suivez les [instructions](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html) sur le site AWS pour récupérer les clés d'accès.
* Consultez la [console S3](https://s3.console.aws.amazon.com/s3/buckets?) pour confirmer le nom et la région de votre bucket.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screen-Shot-2023-04-23-at-3.50.38-PM.png)

* Ajoutez-les à votre fichier `.env` et attribuez-les au fichier `fileparser.js`.

```
PORT=3000
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
S3_REGION=eu-central-1
S3_BUCKET=prac-s3
```

Ensuite, vous créerez une nouvelle instance du module `Upload` importé de `@aws-sdk/lib-storage` dans la méthode `file.open`. Nous configurerons cette instance avec plusieurs options, notamment :

* `client` : Il s'agit de la destination du fichier. Comme nous téléchargeons vers un bucket S3, nous utiliserons le `S3Client` fourni par AWS. Créez une nouvelle instance de `S3Client` et ajoutez vos identifiants AWS – clé d'accès secrète AWS et ID de clé d'accès AWS – pour le configurer. Vous devez également spécifier la région du bucket dans le client.
* `params` : Cet objet contient le nom du bucket S3 (Bucket), la `Key` (c'est-à-dire le nom du fichier), la liste de contrôle d'accès (ACL) qui définit l'accès aux données, et le `Body` (c'est-à-dire le flux de transformation généré).
* `queueSize` : Cela définit le nombre de parties à traiter simultanément. La valeur par défaut est 4.
* `partSize` : Cela définit la taille de chaque partie traitée. La taille minimale possible est de 5 Mo.

Voici le fichier `fileparser.js` mis à jour :

```javascript
const { Upload } = require("@aws-sdk/lib-storage");
const { S3Client } = require("@aws-sdk/client-s3");
const Transform = require('stream').Transform;

const accessKeyId = process.env.AWS_ACCESS_KEY_ID;
const secretAccessKey = process.env.AWS_SECRET_ACCESS_KEY;
const region = process.env.S3_REGION;
const Bucket = process.env.S3_BUCKET;

const parsefile = async (req) => {
    return new Promise((resolve, reject) => {
        let options = {
            maxFileSize: 100 * 1024 * 1024, //100 Mo convertis en octets,
            allowEmptyFiles: false
        }

        const form = formidable(options);
        
        form.parse(req, (err, fields, files) => {});

        form.on('error', error => {
            reject(error.message)
        })
        
        form.on('data', data => {
            if (data.name === "successUpload") {
                resolve(data.value);
            }
        })
        
        form.on('fileBegin', (formName, file) => {

            file.open = async function () {
                this._writeStream = new Transform({
                    transform(chunk, encoding, callback) {
                        callback(null, chunk)
                    }
                })

                this._writeStream.on('error', e => {
                    form.emit('error', e)
                });
                
                // télécharger vers S3
                new Upload({
                    client: new S3Client({
                        credentials: {
                            accessKeyId,
                            secretAccessKey
                        },
                        region
                    }),
                    params: {
                        ACL: 'public-read',
                        Bucket,
                        Key: `${Date.now().toString()}-${this.originalFilename}`,
                        Body: this._writeStream
                    },
                    tags: [], // balises optionnelles
                    queueSize: 4, // configuration de concurence optionnelle
                    partSize: 1024 * 1024 * 5, // taille optionnelle de chaque partie, en octets, au moins 5 Mo
                    leavePartsOnError: false, // gestion manuelle optionnelle des parties abandonnées
                })
                    .done()
                    .then(data => {
                        form.emit('data', { name: "complete", value: data });
                    }).catch((err) => {
                        form.emit('error', err);
                    })
            }

        })

        
    })
}

module.exports = parsefile;

```

La méthode `done` enchaînée à l'instance `Upload` retourne une promesse lorsque le processus de téléchargement est terminé. 

Si le téléchargement est réussi, la promesse se résout avec un objet contenant des informations sur le fichier téléchargé. L'instance `form` émet un événement `data` avec le nom `complete` et les données retournées. L'événement émis envoie une réponse réussie au client. 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screen-Shot-2023-04-24-at-10.42.23-AM.png)
_Réponse de téléchargement réussie_

Les données de réponse contiennent des détails pertinents concernant le téléchargement, notamment :

* `$metadata` : Un objet contenant le code de statut, le nombre de tentatives de téléchargement, etc.
* `Key` : Le nom du fichier.
* `Location` : Une URL pointant vers l'emplacement du fichier. Elle permet également de le télécharger.

Si le téléchargement échoue, il rejette la promesse avec un message d'erreur et l'instance `form` déclenche un événement `error`.

Vous souhaitez également vous assurer que chaque bloc de données est écrit dans le flux avant sa fermeture. Modifiez la méthode `file.end()` pour vous assurer que le flux d'écriture émet un événement `finish` avant d'appeler sa méthode `end`. L'événement `finish` signifie que le programme a écrit toutes les données dans le flux et que le flux est fermé. Et l'événement `end` sur l'objet flux indique que le flux est terminé.

Le fichier `fileparser.js` mis à jour :

```
const { Upload } = require("@aws-sdk/lib-storage");
const { S3Client } = require("@aws-sdk/client-s3");
const Transform = require('stream').Transform;

const accessKeyId = process.env.AWS_ACCESS_KEY_ID;
const secretAccessKey = process.env.AWS_SECRET_ACCESS_KEY;
const region = process.env.S3_REGION;
const Bucket = process.env.S3_BUCKET;

const parsefile = async (req) => {
    return new Promise((resolve, reject) => {
        let options = {
            maxFileSize: 100 * 1024 * 1024, //100 Mo convertis en octets,
            allowEmptyFiles: false
        }

        const form = formidable(options);
        
        form.parse(req, (err, fields, files) => {});

        form.on('error', error => {
            reject(error.message)
        })
        
        form.on('data', data => {
            if (data.name === "successUpload") {
                resolve(data.value);
            }
        })
        
        form.on('fileBegin', (formName, file) => {

            file.open = async function () {
                this._writeStream = new Transform({
                    transform(chunk, encoding, callback) {
                        callback(null, chunk)
                    }
                })

                this._writeStream.on('error', e => {
                    form.emit('error', e)
                });
                
                // télécharger vers S3
                new Upload({
                    client: new S3Client({
                        credentials: {
                            accessKeyId,
                            secretAccessKey
                        },
                        region
                    }),
                    params: {
                        ACL: 'public-read',
                        Bucket,
                        Key: `${Date.now().toString()}-${this.originalFilename}`,
                        Body: this._writeStream
                    },
                    tags: [], // balises optionnelles
                    queueSize: 4, // configuration de concurence optionnelle
                    partSize: 1024 * 1024 * 5, // taille optionnelle de chaque partie, en octets, au moins 5 Mo
                    leavePartsOnError: false, // gestion manuelle optionnelle des parties abandonnées
                })
                    .done()
                    .then(data => {
                        form.emit('data', { name: "complete", value: data });
                    }).catch((err) => {
                        form.emit('error', err);
                    })
            }
            
            file.end = function (cb) {
                this._writeStream.on('finish', () => {
                    this.emit('end')
                    cb()
                })
                this._writeStream.end()
            }

        })

        
    })
}

module.exports = parsefile;

```

Une mise à jour plus facile à lire pourrait impliquer l'abstraction du processus de téléchargement S3 et son appel dans le fichier `fileparser.js`.

Enfin, mettez à jour le fichier `index.js` avec la route de téléchargement. Importez le module `fileparser` et créez une route `POST`. Le module est une promesse, ce qui signifie que vous pouvez gérer la réponse avec `.then()` et les erreurs en utilisant `.catch()`.

Le fichier `index.js` mis à jour :

```javascript
const express = require('express');
const app = express();
require('dotenv').config();

app.set('json spaces', 5); // pour formater la réponse JSON

const PORT = process.env.PORT;
const fileparser = require('./fileparser');

app.get('/', (req, res) => {
  res.send(`
    <h2>Téléchargement de fichiers avec <code>"Node.js"</code></h2>
    <form action="/api/upload" enctype="multipart/form-data" method="post">
      <div>Sélectionnez un fichier : 
        <input name="file" type="file" />
      </div>
      <input type="submit" value="Télécharger" />
    </form>

  `);
});

app.post('/api/upload', async (req, res) => {
  await fileparser(req)
  .then(data => {
    res.status(200).json({
      message: "Succès",
      data
    })
  })
  .catch(error => {
    res.status(400).json({
      message: "Une erreur s'est produite.",
      error
    })
  })
});

app.listen(PORT, () => {
  console.log(`Serveur en cours d'exécution sur le port ${PORT}.`);
})

```

Et voilà ! 

## Conclusion

Dans cet article, vous avez vu comment configurer votre application Node.js pour gérer le téléchargement de fichiers. Vous avez également vu comment le package `formidable` facilite le processus en utilisant des événements et comment configurer le module `Upload` d'AWS-SDK.

Ce [dépôt](https://github.com/Fiyin-Anne/node-s3-upload) contient le code. Au moment de la rédaction, la logique du code dans les exemples ici est la même que le contenu du dépôt.