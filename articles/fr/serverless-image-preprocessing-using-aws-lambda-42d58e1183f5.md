---
title: Comment améliorer vos performances avec les architectures serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-27T18:18:34.000Z'
originalURL: https://freecodecamp.org/news/serverless-image-preprocessing-using-aws-lambda-42d58e1183f5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7qRL-fNyFh7eNe4KbIPn3Q.png
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment améliorer vos performances avec les architectures serverless
seo_desc: 'By Domenico Angilletta

  In this article, I am going to describe how I moved a heavy task like image pre-processing
  from my application server to a completely serverless architecture on AWS in charge
  of storing, processing and serving images.

  The Probl...'
---

Par Domenico Angilletta

Dans cet article, je vais décrire comment j'ai déplacé une tâche lourde comme le prétraitement d'images de mon serveur d'application vers une architecture complètement **serverless** sur AWS, chargée de stocker, traiter et servir les images.

#### Le Problème

Le prétraitement d'images est une tâche requise par de nombreuses applications web. Chaque fois qu'une application permet à un utilisateur de télécharger une image, il est très probable que cette image doive être prétraitée avant d'être servie à une application front-end.

Dans cet article, je vais décrire une architecture serverless basée sur AWS, qui est extrêmement scalable et rentable.

Mais commençons par le début. Dans l'un de mes derniers projets, une application web de marketplace où les utilisateurs doivent télécharger une image d'un produit qu'ils veulent vendre, l'image originale est d'abord recadrée au bon ratio (4:3). Elle est ensuite transformée en trois formats différents utilisés à différents endroits de l'application front-end : 800x600px, 400x300px et 200x150px.

En tant que développeur Ruby on Rails, ma première approche a été d'utiliser une RubyGem — en particulier [Paperclip](https://github.com/thoughtbot/paperclip) ou [Dragonfly](https://github.com/markevans/dragonfly), qui utilisent toutes deux [ImageMagick](https://www.imagemagick.org/script/index.php) pour le traitement d'images.

Bien que cette implémentation soit assez simple (puisqu'il s'agit principalement de configuration), il peut y avoir différents inconvénients :

1. Les images sont traitées sur le serveur d'application. Cela pourrait augmenter le temps de réponse général en raison de la charge de travail plus importante sur le CPU.
2. Le serveur d'application a une puissance de calcul limitée, qui est définie à l'avance, et n'est pas bien adapté pour gérer les requêtes en rafale. Si de nombreuses images doivent être traitées en même temps, la capacité du serveur pourrait être épuisée pendant une longue période. Augmenter la puissance de calcul, d'un autre côté, entraînerait des coûts plus élevés.
3. Les images sont traitées en séquence. Encore une fois, si de nombreuses images doivent être traitées en même temps, la vitesse pourrait être très mauvaise.
4. Si elles ne sont pas correctement configurées, ces gems sauvegardent les images traitées sur le disque, ce qui pourrait rapidement faire saturer l'espace de votre serveur.

En général, en fonction de la quantité de traitement d'images que votre application effectue, cette solution n'est pas scalable.

#### La Solution

En examinant de plus près la tâche de prétraitement d'images, vous remarquerez qu'il n'est probablement pas nécessaire de l'exécuter directement sur votre serveur d'application. En particulier, c'est le cas si vos transformations d'images sont toujours les mêmes et ne dépendent pas d'autres informations que l'image elle-même. C'était mon cas, où je générais toujours différentes tailles d'images ainsi qu'une optimisation de la qualité/poids de l'image.

Une fois que vous réalisez que cette tâche peut être facilement isolée du reste de la logique de l'application, penser à une solution serverless qui prend simplement une image originale en entrée et génère toutes les transformations nécessaires est simple.

AWS Lambda s'avère être une solution parfaite pour ce type de problème. D'une part, il peut gérer des milliers de requêtes par seconde, et d'autre part, vous ne payez que pour le temps de calcul que vous consommez. Il n'y a pas de frais lorsque votre code n'est pas en cours d'exécution.

AWS S3 offre un stockage illimité à un prix très bas, tandis qu'AWS SNS fournit un moyen facile de messagerie Pub/Sub pour les microservices, les systèmes distribués et les applications serverless. Enfin, AWS Cloudfront est utilisé comme réseau de diffusion de contenu (CDN) pour les images stockées sur S3.

La combinaison de ces quatre services AWS donne une solution de traitement d'images très puissante à un coût très bas.

### Architecture de Haut Niveau

Le processus de génération de différentes versions d'images à partir d'une image originale commence par le téléchargement de l'image originale sur AWS S3. Cela déclenche, via AWS SNS, l'exécution d'une fonction AWS Lambda chargée de générer les nouvelles versions d'images et de les télécharger à nouveau sur AWS S3. Voici la séquence en détail :

1. Les images sont téléchargées dans un dossier spécifique à l'intérieur d'un bucket AWS S3.
2. Chaque fois qu'une nouvelle image est téléchargée dans ce dossier, S3 publie un message contenant la clé S3 de l'objet créé sur un sujet AWS SNS.
3. AWS Lambda, qui est configuré comme consommateur sur le même sujet SNS, lit le nouveau message et utilise la clé de l'objet S3 pour récupérer la nouvelle image.
4. AWS Lambda traite la nouvelle image, applique les transformations nécessaires et télécharge l'image traitée sur S3.
5. Les images traitées sont maintenant servies aux utilisateurs finaux via le CDN AWS Cloudfront, afin d'optimiser la vitesse de téléchargement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7qRL-fNyFh7eNe4KbIPn3Q.png)

Cette architecture est très scalable, car chaque image téléchargée déclenchera une nouvelle exécution de code Lambda pour traiter cette requête, de sorte que des milliers d'images peuvent être traitées en parallèle par autant d'exécutions de code.

Aucun espace disque ou puissance de calcul n'est utilisé sur le serveur d'application, car tout est stocké sur S3 et traité par Lambda.

Enfin, configurer un CDN devant S3 est très facile et vous permet d'avoir des vitesses de téléchargement élevées depuis n'importe où dans le monde.

### Tutoriel Pas à Pas

La mise en œuvre de cette solution est relativement facile, car il s'agit principalement de configuration, à l'exception du code Lambda qui effectue le prétraitement des images. Le reste de cet article décrira en détail comment configurer l'architecture AWS et fournira le code exécuté par AWS Lambda pour redimensionner l'image téléchargée afin d'avoir un exemple complet fonctionnel.

Pour l'essayer vous-même, vous aurez besoin d'un compte AWS. Si vous n'en avez pas, vous pouvez en créer un gratuitement et profiter de l'offre gratuite AWS [ici](https://aws.amazon.com/free/).

#### Étape 1 : Créer un Sujet sur AWS SNS

Tout d'abord, nous devons configurer un nouveau sujet SNS (Simple Notification Service) sur lequel AWS publiera un message chaque fois qu'une nouvelle image est téléchargée sur S3. Ce message contient la clé de l'objet S3 utilisée plus tard par la fonction Lambda pour récupérer l'image téléchargée et la traiter.

Depuis votre console AWS, visitez la [page SNS](https://console.aws.amazon.com/sns/v2/home), cliquez sur « Créer un sujet » et entrez un nom de sujet, par exemple « image-preprocessing ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*b5URVdeHEjEh9Upi08tIqQ.png)

Ensuite, nous devons modifier la politique du sujet pour permettre à notre bucket S3 de publier des messages sur celui-ci.

Depuis la page du sujet, cliquez sur Actions -> Modifier la politique du sujet, choisissez la vue avancée, ajoutez le bloc JSON suivant (avec vos propres arns pour Resource et SourceArn) au tableau de déclaration et mettez à jour la politique :

```
{      "Sid": "ALLOW_S3_BUCKET_AS_PUBLISHER",      "Effect": "Allow",      "Principal": {        "AWS": "*"      },      "Action": [        "SNS:Publish",      ],      "Resource": "arn:aws:sns:us-east-1:AWS-OWNER-ID:image-preprocessing",      "Condition": {          "StringLike": {              "aws:SourceArn": "arn:aws:s3:*:*:YOUR-BUCKET-NAME"          }      }}
```

Vous pouvez trouver un exemple de politique JSON complète [ici](https://github.com/domangi/image-preprocessing-lambda/blob/master/sns-policy-example.json).

#### Étape 2 : Créer la Structure de Dossiers AWS S3

Maintenant, nous devons préparer la structure de dossiers sur S3 qui contiendra les images originales et traitées. Dans cet exemple, nous allons générer deux versions d'images redimensionnées, 800x600 et 400x300.

Depuis votre console AWS, ouvrez la [page S3](https://s3.console.aws.amazon.com/s3/home) et créez un nouveau bucket. Je vais appeler le mien « image-preprocessing-example ». Ensuite, à l'intérieur du bucket, nous devons créer un dossier nommé « originals », un dossier nommé « 800x600 » et un autre nommé « 400x300 ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*H8zhYpEEHofH67mjPI01lA.png)

#### Étape 3 : Configurer les Événements AWS S3

Chaque fois qu'une nouvelle image est téléchargée dans le dossier originals, nous voulons que S3 publie un message sur notre sujet SNS « image-preprocessing » afin que l'image puisse être traitée.

Pour ce faire, ouvrez votre bucket S3 depuis la console AWS, cliquez sur Propriétés -> Événements -> + Ajouter une notification et remplissez les champs suivants :

![Image](https://cdn-media-1.freecodecamp.org/images/1*O3q00njD2ruHfX1zldXnSg.png)

Ici, nous disons à S3 de générer un événement chaque fois qu'un nouvel objet est créé (ObjectCreate) à l'intérieur du dossier originals (préfixe), et de publier cet événement sur notre sujet SNS « image-preprocessing ».

#### Étape 4 : Configurer le Rôle IAM pour permettre à Lambda d'accéder au Dossier S3

Nous voulons créer une fonction Lambda qui récupère les objets image de S3, les traite et télécharge à nouveau les versions traitées sur S3. Pour ce faire, nous devons d'abord configurer un rôle IAM qui permettra à notre fonction Lambda d'accéder au dossier S3 nécessaire.

Depuis la [page IAM de la console AWS](https://console.aws.amazon.com/iam/home) :

1. Cliquez sur [Créer une politique](https://console.aws.amazon.com/iam/home?region=us-east-1#/policies$new?step=edit)
2. Cliquez sur JSON et tapez (remplacez YOUR-BUCKET-NAME)

```
{      "Version": "2012-10-17",      "Statement": [          {              "Sid": "Stmt1495470082000",              "Effect": "Allow",              "Action": [                  "s3:*"              ],              "Resource": [                  "arn:aws:s3:::YOUR-BUCKET-NAME/*"              ]          }      ]}
```

où la ressource est notre bucket sur S3. Cliquez sur révision, entrez le nom de la politique, par exemple AllowAccessOnYourBucketName, et créez la politique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gZcfUJozRyZMTLZPSd8TPw.png)

3. Cliquez sur Rôles -> Créer un rôle
4. Choisissez Aws Service -> Lambda (qui utilisera la politique)
5. Sélectionnez la politique précédemment créée (AllowAccessOnYourBucketName)
6. Enfin, cliquez sur révision, tapez un nom (LambdaS3YourBucketName), et cliquez sur créer un rôle

![Image](https://cdn-media-1.freecodecamp.org/images/1*tCw83JM8xraEa0P2ZXhIaQ.png)
_Créer un rôle Lambda_

![Image](https://cdn-media-1.freecodecamp.org/images/1*0RL2XQ5xaayD5wwB3eVonw.png)
_Attacher une politique au rôle Lambda_

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jtm_1s64mpvRoRO7NlNkdQ.png)
_Enregistrer le rôle_

#### Étape 5 : Créer la Fonction AWS Lambda

Maintenant, nous devons configurer notre fonction Lambda pour consommer les messages du sujet SNS « image-preprocessing » et générer nos versions d'images redimensionnées.

Commençons par créer une nouvelle fonction Lambda.

Depuis votre console AWS, visitez la [page Lambda](https://console.aws.amazon.com/sns/v2/home), cliquez sur « Créer une fonction », et tapez le nom de votre fonction, par exemple ImageResize, choisissez votre runtime, dans ce cas Node.js 6.10, et le rôle IAM précédemment créé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mmWNnZa-eWH-hs9oJ6LhLg.png)

Ensuite, nous devons ajouter SNS aux déclencheurs de la fonction, afin que la fonction Lambda soit appelée chaque fois qu'un nouveau message est publié sur le sujet « image-preprocessing ».

Pour ce faire, cliquez sur « SNS » dans la liste des déclencheurs, sélectionnez « image-preprocessing » dans la liste des sujets SNS, et cliquez sur « ajouter ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*0aZu0bxIsYjyiEdHGPT3og.png)

Enfin, nous devons télécharger notre code qui gérera l'événement S3 ObjectCreated. Cela signifie récupérer l'image téléchargée depuis le dossier originals de S3, la traiter et la télécharger à nouveau dans les dossiers d'images redimensionnées.

Vous pouvez télécharger le code [ici](https://github.com/domangi/image-preprocessing-lambda). Le seul fichier que vous devez télécharger vers votre fonction Lambda est [version1.1.zip](https://github.com/domangi/image-preprocessing-lambda/blob/master/version1.1.zip), qui contient index.js et le dossier node_modules.

![Image](https://cdn-media-1.freecodecamp.org/images/1*F4um-2CraoefdiLYcZ0ofg.png)

Afin de donner à la fonction Lambda suffisamment de temps et de mémoire pour traiter l'image, nous pouvons augmenter la mémoire à 256 Mo et le délai d'attente à 10 secondes. Les ressources nécessaires dépendent de la taille de l'image et de la complexité de la transformation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*a8x2lFcEgOxXwug-AGY-_A.png)

Le code lui-même est assez simple et a pour seul but de démontrer l'intégration AWS.

Tout d'abord, une fonction de gestionnaire est définie (exports.handler). Cette fonction est appelée par le déclencheur externe, dans ce cas le message publié sur SNS qui contient la clé de l'objet S3 de l'image téléchargée.

Elle analyse d'abord le message JSON de l'événement pour extraire le nom du bucket S3, la clé de l'objet S3 de l'image téléchargée et le nom de fichier qui est simplement la partie finale de la clé.

Une fois qu'elle a le bucket et la clé de l'objet, l'image téléchargée est récupérée à l'aide de _s3.getObject_ puis transmise à la fonction de redimensionnement. La variable _SIZE_ contient les tailles d'images que nous voulons générer, qui correspondent également aux noms des dossiers S3 où les images transformées seront téléchargées.

```
var async = require('async');var AWS = require('aws-sdk');var gm = require('gm').subClass({ imageMagick: true });var s3 = new AWS.S3();
```

```
var SIZES = ["800x600", "400x300"];
```

```
exports.handler = function(event, context) {    var message, srcKey, dstKey, srcBucket, dstBucket, filename;    message = JSON.parse(event.Records[0].Sns.Message).Records[0];
```

```
srcBucket = message.s3.bucket.name;    dstBucket = srcBucket;    srcKey    =  message.s3.object.key.replace(/\+/g, " ");     filename = srcKey.split("/")[1];    dstKey = "";     ...    ...    // Télécharger l'image depuis S3    s3.getObject({            Bucket: srcBucket,            Key: srcKey    }, function(err, response){        if (err){            var err_message = 'Impossible de télécharger l\'image : ' + srcKey;            return console.error(err_message);        }        var contentType = response.ContentType;
```

```
        // Passer notre image à ImageMagick        var original = gm(response.Body);
```

```
        // Obtenir la taille de l'image        original.size(function(err, size){            if(err){                return console.error(err);            }
```

```
            // Pour chaque taille dans SIZES, appeler la fonction de redimensionnement            async.each(SIZES, function (width_height,  callback) {                var filename = srcKey.split("/")[1];                var thumbDstKey = width_height +"/" + filename;                resize(size, width_height, imageType, original,                          srcKey, dstBucket, thumbDstKey, contentType,                        callback);            },            function (err) {                if (err) {                    var err_message = 'Impossible de redimensionner ' + srcKey;                    console.error(err_message);                }                context.done();            });        });    });
```

```
}
```

La fonction de redimensionnement applique certaines transformations sur l'image originale en utilisant la bibliothèque « gm », en particulier elle redimensionne l'image, la recadre si nécessaire et réduit la qualité à 80 %. Elle télécharge ensuite l'image modifiée sur S3 en utilisant « _s3.putObject_ », en spécifiant « _ACL: public-read_ » pour rendre la nouvelle image publique.

```
var resize = function(size, width_height, imageType,                       original, srcKey, dstBucket, dstKey,                       contentType, done) {
```

```
    async.waterfall([        function transform(next) {            var width_height_values = width_height.split("x");            var width  = width_height_values[0];            var height = width_height_values[1];
```

```
            // Transformer le buffer de l'image en mémoire            original.interlace("Plane")                .quality(80)                .resize(width, height, '^')                .gravity('Center')                .crop(width, height)                .toBuffer(imageType, function(err, buffer) {                if (err) {                    next(err);                } else {                    next(null, buffer);                }            });        },        function upload(data, next) {            console.log("Téléchargement des données vers " + dstKey);            s3.putObject({                    Bucket: dstBucket,                    Key: dstKey,                    Body: data,                    ContentType: contentType,                    ACL: 'public-read'                },                next);            }        ], function (err) {            if (err) {                console.error(err);            }            done(err);        }    );};
```

#### Étape 6 : Test

Maintenant, nous pouvons tester que tout fonctionne comme prévu en téléchargeant une image dans le dossier originals. Si tout a été implémenté correctement, nous devrions trouver une version redimensionnée de l'image téléchargée dans le dossier 800x600 et une autre dans le dossier 400x300.

Dans la vidéo ci-dessous, vous pouvez voir trois fenêtres : à gauche le dossier originals, au milieu le dossier 800x600, et à droite le dossier 400x300. Après avoir téléchargé un fichier dans le dossier original, les deux autres fenêtres sont actualisées pour vérifier si les images ont été créées.

Et voilà, les voici ;)

#### (Facultatif) Étape 6 : Ajouter le CDN Cloudfront

Maintenant que les images sont générées et téléchargées sur S3, nous pouvons ajouter le CDN Cloudfront pour livrer les images à nos utilisateurs finaux, afin d'améliorer la vitesse de téléchargement.

1. Ouvrez la [page Cloudfront](https://console.aws.amazon.com/cloudfront/home)
2. Cliquez sur « Créer une distribution »
3. Lorsque vous êtes invité à choisir la méthode de livraison, sélectionnez « Distribution Web »
4. Choisissez votre bucket S3 comme « Nom de domaine d'origine » et cliquez sur « Créer une distribution »

Le processus de création du réseau de distribution n'est pas immédiat, vous devrez donc attendre que le statut de votre CDN passe de « _En cours_ » à « _Déployé_ ».

Une fois déployé, vous pouvez utiliser le nom de domaine au lieu de l'URL de votre bucket S3. Par exemple, si votre nom de domaine Cloudfront est « _1234-cloudfront-id.cloudfront.net_ », vous pouvez accéder à votre dossier d'images redimensionnées par « _https://1234-cloudfront-id.cloudfront.net_/400x300/FILENAME » et « _https://1234-cloudfront-id.cloudfront.net_/800x600/FILENAME ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*nsIx2cOXyOLkyKEJGRE9lQ.png)

Cloudfront a de nombreuses autres options qui doivent être configurées, mais celles-ci sont hors du cadre de cet article. Pour un guide plus détaillé sur la configuration de votre CDN, consultez le [guide de démarrage d'Amazon](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.html).

Et c'est tout ! J'espère que vous avez apprécié cet article. N'hésitez pas à laisser un commentaire ci-dessous et faites-moi savoir ce que vous en pensez !