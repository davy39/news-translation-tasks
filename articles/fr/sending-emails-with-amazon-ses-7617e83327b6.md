---
title: Envoyer des emails avec Amazon SES
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-20T02:49:59.000Z'
originalURL: https://freecodecamp.org/news/sending-emails-with-amazon-ses-7617e83327b6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6qHAynt7vd0MQr7Yut0LVA.png
tags:
- name: AWS
  slug: aws
- name: email marketing
  slug: email-marketing
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Startups
  slug: startups
seo_title: Envoyer des emails avec Amazon SES
seo_desc: 'By Kangze Huang

  The Complete AWS Web Boilerplate — Tutorial 3


  Table of Contents


  Part 0: Introduction to the Complete AWS Web Boilerplate

  Part 1: User Authentication with AWS Cognito (3 parts)

  Part 2: Saving File Storage Costs with Amazon S3 (1 part...'
---

Par Kangze Huang

#### Le Modèle Complet AWS Web — Tutoriel 3

![Image](https://cdn-media-1.freecodecamp.org/images/APBEF5hr2WpoHLy0DEuLKJV2GzmYTubut78Q)

### Table des Matières

> **Partie 0 :** [Introduction au Modèle Complet AWS Web](https://medium.com/@kangzeroo/the-complete-aws-web-boilerplate-d0ca89d1691f#.3eqpvcjsy)

> **Partie 1 :** [Authentification des Utilisateurs avec AWS Cognito](https://medium.com/@kangzeroo/user-management-with-aws-cognito-1-3-initial-setup-a1a692a657b3#.cbkz7b2jp) (3 parties)

> **Partie 2 :** [Économiser les Coûts de Stockage de Fichiers avec Amazon S3](https://medium.com/@kangzeroo/amazon-s3-cloud-file-storage-for-performance-and-cost-savings-8f38d7769619#.l9so2hk00) (1 partie)

> **Partie 3 :** [Envoyer des Emails avec Amazon SES](https://medium.com/@kangzeroo/sending-emails-with-amazon-ses-7617e83327b6#.5nhcrr609) (1 partie)

> Partie 4 : Gérer les Utilisateurs et les Permissions avec AWS IAM **[Bientôt Disponible]**

> Partie 5 : Hébergement de Serveur Cloud avec AWS EC2 et ELB **[Bientôt Disponible]**

> Partie 6 : Le Tueur de MongoDB : AWS DynamoDB **[Bientôt Disponible]**

> Partie 7 : Mise à l'Échelle SQL Sans Douleur en utilisant AWS RDS **[Bientôt Disponible]**

> Partie 8 : Architecture Serverless avec Amazon Lambda **[Bientôt Disponible]**

Téléchargez le projet Github [ici](https://github.com/kangzeroo/Kangzeroos-Complete-AWS-Web-Boilerplate/tree/SES).

### Installation

Envoyer des emails avec Amazon SES est vraiment simple. Commençons par l'installation. Allez sur Amazon SES et cliquez sur **Adresses Email** dans la barre latérale. Ensuite, cliquez sur **Vérifier une Nouvelle Adresse Email** et entrez une adresse email que vous souhaitez utiliser pour les messages dans l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/-Mx1fdq0M7OF63l3-3Jmc0fQHrLl8jR56nbh)

Maintenant, allez sur votre fournisseur d'email et cliquez sur le lien de vérification. Après vérification, retournez à l'onglet **Adresses Email** d'Amazon SES. Vous devriez maintenant voir votre email vérifié.

![Image](https://cdn-media-1.freecodecamp.org/images/KgdxVyP4QlP-XpKRFG-aUpjn2Wuj5VH1-gSC)

Cela était nécessaire pour 2 raisons. La première est que nous avons besoin d'une adresse email pour envoyer un message, et la seconde est parce que nous sommes dans un environnement de bac à sable. Un environnement de bac à sable signifie que vous ne pouvez envoyer et recevoir des emails que depuis des adresses vérifiées, et vous empêche d'envoyer des spams. C'est tout ce dont nous avons besoin pour cette installation.

![Image](https://cdn-media-1.freecodecamp.org/images/wRQoOk9N4QQSCM6Slimww-YrZhMrWzi2-KWR)

Si vous souhaitez pouvoir envoyer des emails à n'importe quelle adresse email, vous devez faire une demande écrite à Amazon pour sortir de l'environnement de bac à sable. Pour ce faire, naviguez vers le coin supérieur droit à **Support** &**gt; Centre de Support**.

![Image](https://cdn-media-1.freecodecamp.org/images/ErZNvtZKAWPsUVrhSHje-JmjlseahbCJhi1V)

À cet écran suivant, cliquez sur `Créer un cas`.

C'est un formulaire simple, mais nous allons l'expliquer brièvement. Sélectionnez **Augmentation de la Limite de Service** et définissez le **Type de Limite** sur **Limites d'Envoi SES**. Maintenant, créez 2 demandes, une où **Limite** est **Quota d'Envoi Quotidien Souhaité** (combien d'emails peuvent être envoyés en une journée), et l'autre où **Limite** est **Taux d'Envoi Maximum Souhaité**. Définissez la **Nouvelle valeur de limite** sur le montant dont vous avez besoin. Enfin, définissez optionnellement le Type de Courrier car cela augmente vos chances d'approbation. Utilisez transactionnel si vos emails sont générés à la suite d'une activité de l'utilisateur. Il existe d'autres options disponibles pour d'autres cas d'utilisation.

![Image](https://cdn-media-1.freecodecamp.org/images/FqkYQdVUxsfCm232bHtQlCbCNltKdDoh57p8)

Le reste de la demande est facile. Assurez-vous d'accepter de vous conformer aux Conditions d'Utilisation, et que vous avez un processus pour gérer les [rebonds et plaintes](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/best-practices-bounces-complaints.html) (pour lorsque les utilisateurs marquent votre email comme spam). Enfin, donnez une brève explication de votre cas d'utilisation.

![Image](https://cdn-media-1.freecodecamp.org/images/in92mh4YL5eNVCjDz6Iy96b7jhWP3xZ222Fv)

Soumettez votre demande et vous devriez recevoir un email d'Amazon avec les résultats de votre demande d'augmentation de service. Une fois approuvé, votre application peut envoyer des messages à n'importe quelle adresse email.

### Le Code

Nous sommes prêts à plonger dans le code ! Allez dans `App/src/api/aws/aws_ses.js` où se trouve la majeure partie du code. Jetons un coup d'œil à la fonction principale `sendAWSEmail()` :

```
export function sendAWSEmail(email, message){ const ses = new AWS.SES({  region: 'us-east-1' }) const p = new Promise((res, rej)=>{  if(!email|| message){   rej('Missing user email or message content')  }else{   const params = createInquiryParamsConfig(email, message)   // console.log('Sending email with attached params!')   AWS.config.credentials.refresh(function(){    // console.log(AWS.config.credentials)    ses.sendEmail(params, function(err, data) {      if(err){        // console.log(err, err.stack); // an error occurred        rej(err)      }else{       // console.log(data);           // successful response     res('Success! Email sent')      }    })   })  } }) return p}
```

C'est extrêmement simple. Nous recevons deux arguments, une adresse email à laquelle envoyer, et un message à envoyer. La première chose que nous faisons dans cette fonction est d'instancier l'objet AWS SES pour interagir avec AWS en passant simplement la région. Ensuite, nous vérifions s'il y a une adresse email de destinataire et un message. Si les deux sont fournis, alors nous pouvons réellement envoyer l'email.

En supposant que nous avons à la fois une adresse email de destinataire et un message, nous allons créer un objet `params` pour que AWS SES lise toutes les informations et options nécessaires. Cet objet `params` est créé avec `createInquiryParamsConfig()`. Avant de plonger dans ce terrier, terminons rapidement l'explication du reste de `sendAWSEmail()`. Nous actualisons les informations d'identification de l'utilisateur AWS Cognito (que nous avons définies avec AWS Cognito, expliqué dans mon [autre tutoriel](https://medium.com/@kangzeroo/user-management-with-aws-cognito-1-3-initial-setup-a1a692a657b3#.ykdx6xqx2)) et appelons `ses.sendEmail` avec `params` et un callback de réponse passé en argument. Rejetez la promesse s'il y a une erreur, et résolvez avec un message de succès s'il n'y a pas d'erreur. `ses.sendEmail` est la seule fonction AWS que nous utiliserons, et tout le reste dont nous avons besoin est déterminé dans `params`.

Maintenant, voyons comment créer `params` avec `createInquiryParamsConfig()`.

```
function createInquiryParamsConfig(email, message){ const params = {   Destination: {      BccAddresses: [],     CcAddresses: [],     ToAddresses: [ email ]   },   Message: {      Body: {        Html: {         Data: generateHTMLInquiryEmail(landlordEmail, message),         Charset: 'UTF-8'       }     },     Subject: {        Data: 'Kangzeroos Boilerplate says hi ' + email,       Charset: 'UTF-8'     }   },   Source: 'yourApp@gmail.com',    ReplyToAddresses: [ 'yourApp@gmail.com' ],   ReturnPath: 'yourApp@gmail.com' } return params}
```

Assez simple, nous passons `email` et `message`, et retournons un grand objet JavaScript. Toutes les valeurs que vous voyez ici sont nécessaires, mais vous pouvez ajouter une tonne d'autres configurations optionnelles. La fonction à laquelle nous devons prêter attention est `generateHTMLInquiryEmail()`. Jetons un coup d'œil à cela.

```
function generateHTMLInquiryEmail(email, message){ return `  <!DOCTYPE html>  <html>    <head>      <meta charset='UTF-8' />      <title>title</title>    </head>    <body>     <table border='0' cellpadding='0' cellspacing='0' height='100%' width='100%' id='bodyTable'>      <tr>          <td align='center' valign='top'>              <table border='0' cellpadding='20' cellspacing='0' width='600' id='emailContainer'>                  <tr style='background-color:#99ccff;'>                      <td align='center' valign='top'>                          <table border='0' cellpadding='20' cellspacing='0' width='100%' id='emailBody'>                              <tr>                                  <td align='center' valign='top' style='color:#337ab7;'>                                      <h3>${message}</h3>                                  </td>                              </tr>                          </table>                      </td>                  </tr>                  <tr style='background-color:#74a9d8;'>                      <td align='center' valign='top'>                          <table border='0' cellpadding='20' cellspacing='0' width='100%' id='emailReply'>                              <tr style='font-size: 1.2rem'>                                  <td align='center' valign='top'>                                      <span style='color:#286090; font-weight:bold;'>Send From:</span> <br/> ${email}                                  </td>                              </tr>                          </table>                      </td>                  </tr>              </table>          </td>      </tr>      </table>    </body>  </html> `}
```

Tout ce que nous faisons ici est de créer un fichier HTML et de passer `email` et `message` pour créer un email personnalisé. Nous utilisons les littéraux de chaîne ES6 pour ajouter des variables de chaîne avec `${ }` comme ceci : `<h3>${message}</h3>.

Et c'est tout ! Vous pouvez utiliser n'importe quel code front-end que vous souhaitez, il suffit de passer un `email` et un `message` à `sendAWSEmail()`. N'oubliez pas que `sendAWSEmail()` retourne une promesse, vous devrez donc la gérer en conséquence. Si vous ne savez pas comment gérer les promesses, consultez mon [autre tutoriel ici](https://medium.com/@kangzeroo/quick-story-about-javascript-promises-31b4e76ed0cd#.sty9l0ncx).

À la prochaine !

### Table des Matières

> **Partie 0 :** [Introduction au Modèle Complet AWS Web](https://medium.com/@kangzeroo/the-complete-aws-web-boilerplate-d0ca89d1691f#.3eqpvcjsy)

> **Partie 1 :** [Authentification des Utilisateurs avec AWS Cognito](https://medium.com/@kangzeroo/user-management-with-aws-cognito-1-3-initial-setup-a1a692a657b3#.cbkz7b2jp) (3 parties)

> **Partie 2 :** [Économiser les Coûts de Stockage de Fichiers avec Amazon S3](https://medium.com/@kangzeroo/amazon-s3-cloud-file-storage-for-performance-and-cost-savings-8f38d7769619#.l9so2hk00) (1 partie)

> **Partie 3 :** [Envoyer des Emails avec Amazon SES](https://medium.com/@kangzeroo/sending-emails-with-amazon-ses-7617e83327b6#.5nhcrr609) (1 partie)

> Partie 4 : Gérer les Utilisateurs et les Permissions avec AWS IAM **[Bientôt Disponible]**

> Partie 5 : Hébergement de Serveur Cloud avec AWS EC2 et ELB **[Bientôt Disponible]**

> Partie 6 : Le Tueur de MongoDB : AWS DynamoDB **[Bientôt Disponible]**

> Partie 7 : Mise à l'Échelle SQL Sans Douleur en utilisant AWS RDS **[Bientôt Disponible]**

> Partie 8 : Architecture Serverless avec Amazon Lambda **[Bientôt Disponible]**

Cette méthode a été partiellement utilisée dans le déploiement de [renthero.ca](http://renthero.ca)