---
title: Comment utiliser Nodemailer pour envoyer des emails depuis votre serveur Node.js
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2021-01-25T22:36:15.000Z'
originalURL: https://freecodecamp.org/news/use-nodemailer-to-send-emails-from-your-node-js-server
coverImage: https://cdn-media-2.freecodecamp.org/w1280/600efb510a2838549dcb7595.jpg
tags:
- name: email
  slug: email
- name: Express
  slug: express
- name: gmail
  slug: gmail
- name: node js
  slug: node-js
seo_title: Comment utiliser Nodemailer pour envoyer des emails depuis votre serveur
  Node.js
seo_desc: 'Nodemailer is a Node.js module that allows you to send emails from your
  server with ease. Whether you want to communicate with your users or just notify
  yourself when something has gone wrong, one of the options for doing so is through
  mail.

  There ar...'
---

[Nodemailer](https://nodemailer.com/about/) est un module Node.js qui vous permet d'envoyer des emails depuis votre serveur avec facilité. Que vous souhaitiez communiquer avec vos utilisateurs ou simplement vous notifier lorsque quelque chose ne va pas, l'une des options pour le faire est par email.

Il existe de nombreux articles expliquant comment utiliser Nodemailer dans sa forme la plus basique, mais cet article n'en est pas un. Ici, je vais montrer la pratique la plus courante pour envoyer un email depuis votre backend Node.js en utilisant Nodemailer et Gmail.

## Comment commencer avec Nodemailer

Tout d'abord, nous devons configurer notre modèle Node.js en utilisant Express. Pour vous assurer que vous avez Node et npm installés, vous pouvez exécuter les commandes suivantes :

```bash
node -v 
npm -v
```

Si ces deux commandes affichent une version, vous êtes prêt à commencer. Sinon, installez ce qui manque.

Créez un répertoire pour votre projet. Nous utiliserons **nodemailerProject**.

```bash
mkdir nodemailerProject
```

Allez dans le répertoire nouvellement créé et exécutez

```bash
npm init
```

Cela initialisera notre projet avec un fichier **package.json**.

Ensuite, nous devrons installer Express en utilisant :

```
npm install express
```

Selon le fichier que vous avez indiqué comme point d'entrée (par défaut index.js), ouvrez-le et collez le code suivant :

```node.js
const express = require('express')
const app = express()
const port = 3000


app.listen(port, () => {
  console.log(`nodemailerProject écoute sur http://localhost:${port}`)
})
```

Ci-dessus se trouve ce qui est nécessaire pour démarrer un serveur simple en utilisant Express. Vous pouvez voir qu'il fonctionne correctement en exécutant :

```bash
node index.js
```

### Comment installer Nodemailer

Installez nodemailer en utilisant la commande suivante :

```bash
npm install nodemailer
```

L'API de Nodemailer est assez simple et nécessite que nous fassions ce qui suit :

1. Créer un objet **Transporter**
2. Créer un objet **MailOptions**
3. Utiliser la méthode **Transporter.sendMail**

Pour créer un objet transporter, nous faisons ce qui suit :

```node.js
let transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        type: 'OAuth2',
        user: process.env.MAIL_USERNAME,
        pass: process.env.MAIL_PASSWORD,
        clientId: process.env.OAUTH_CLIENTID,
        clientSecret: process.env.OAUTH_CLIENT_SECRET,
        refreshToken: process.env.OAUTH_REFRESH_TOKEN
      }
    });
```

> ❤️ Faites attention, car en plus des clés user et pass, qui sont vos propres identifiants pour votre compte Gmail, les trois autres clés doivent être récupérées après avoir configuré OAuth.

Comme nous l'avons mentionné au début de cet article, nous utiliserons Gmail pour nos besoins d'envoi de courrier. Comme vous l'avez peut-être deviné, Gmail a un niveau de sécurité élevé en ce qui concerne les emails envoyés par/un compte utilisateur.

Il existe plusieurs moyens de surmonter cet obstacle (certains meilleurs que d'autres), et nous choisirons celui qui nécessite de configurer un projet dans la **Google Cloud Platform**. Nous devons faire cela afin d'avoir des identifiants pour la sécurité OAuth activée par Gmail.

> Si vous souhaitez en savoir plus sur les complexités de l'utilisation de Gmail avec nodemailer, allez [ici](https://nodemailer.com/usage/using-gmail/).

Les prochaines étapes nécessiteront quelques configurations au lieu de codage, alors préparez-vous.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-297.png)
_Photo par [Unsplash](https://unsplash.com/@d_mccullough?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Daniel McCullough</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## Configurations de la Google Cloud Platform

Si vous n'avez pas de compte [Google Cloud Platform](https://console.cloud.google.com/home), assurez-vous d'en créer un en tant que prérequis. Une fois que vous avez cela configuré, créez un nouveau projet en cliquant sur le menu déroulant dans le coin supérieur gauche.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_a4fnFLNMoTtLJuqsKilVnA.png)

Sélectionnez l'option Nouveau Projet :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_HNwUG3wPdbrwc3JB5D7_tg.png)

Dans la fenêtre suivante, nous devrons donner un nom à notre projet. Choisissez ce que vous voulez, mais nous continuerons avec notre nom **NodemailerProject**. Pour la propriété de localisation, vous pouvez la laisser comme Aucune organisation.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_TRlA6RBLCCCSMQ5R4di27A.png)

Cela peut prendre quelques secondes pour que le projet soit configuré, mais après cela, vous pourrez voir cet écran :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_FT9MhBZyU4cZd4Qg6zeFag.png)

Ouvrez le menu de navigation en cliquant sur les trois lignes en pointillés dans le coin supérieur gauche et sélectionnez **APIs et Services** :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_qPaPpPadHQLdKCQbhjND7Q.png)

Afin de pouvoir utiliser Nodemailer et Gmail, nous devrons utiliser OAuth2. Si vous n'êtes pas familier avec OAuth, c'est un protocole d'authentification. Je ne vais pas entrer dans les détails ici car ce n'est pas nécessaire, mais si vous voulez comprendre plus à ce sujet, allez [ici](https://oauth.net/2/).

Tout d'abord, nous devrons configurer notre écran de consentement OAuth :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_W2oeT1KmJXpwSQlIMIVo5w.png)

Si vous n'êtes pas membre de G-Suite, la seule option disponible sera Externe pour le type d'utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_l_GrPVtXODPS0GXKLMdWYA.png)

Après avoir cliqué sur créer, l'écran suivant nous demande de remplir les informations de l'application (notre serveur) :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_reZ04hUX4jh1IzLGh7vCFA.png)

Remplissez votre email dans le champ Email de support utilisateur et également dans le champ Informations de contact du développeur. Cliquer sur Enregistrer et Continuer nous amènera à la phase des Portées de cette configuration. Passez cette phase, car elle n'est pas pertinente pour nous, et passez à la phase des Utilisateurs de Test.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_Jms50wZ5mVmUyOaiVF7b4w.png)

Ici, ajoutez-vous en tant qu'utilisateur et cliquez sur Enregistrer et Continuer.

## Comment configurer vos paramètres OAuth

Dans cette phase, nous créerons des identifiants OAuth à utiliser avec Nodemailer. Rendez-vous dans l'onglet Identifiants au-dessus de l'écran de consentement OAuth. Cliquez sur le signe plus (➕) qui a le texte **Créer des identifiants** et choisissez ID client OAuth.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_h0nME2ccR7HPjKmz_DMZRw.png)

Dans le menu déroulant Type d'application, choisissez **Application Web** :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_72Em-VS-fdM2WCwOA6zcfg.png)

Dans la section **URIs de redirection autorisés**, assurez-vous d'ajouter OAuth2 Playground ([https://developers.google.com/oauthplayground](https://developers.google.com/oauthplayground/)) car nous l'utiliserons pour obtenir l'une des clés mentionnées au début de cet article.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_ywIcOlqA5DHdsPaSNnjJ9Q.png)

Après avoir cliqué sur créer, vous verrez votre ID client et votre secret client. **Gardez ces informations pour vous et ne les exposez jamais de quelque manière que ce soit.**

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-298.png)
_Photo par [Unsplash](https://unsplash.com/@welipower?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Power Lai</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

### Obtenez votre jeton de rafraîchissement OAuth

Pour obtenir le jeton de rafraîchissement, que nous utiliserons dans l'objet transporter dans Nodemailer, nous devons nous rendre sur le terrain de jeu OAuth2. Nous avons approuvé cette URI à cette fin spécifique à une étape précédente.

1. Cliquez sur l'icône d'engrenage à droite (qui est la configuration OAuth2) et cochez la case pour utiliser vos propres identifiants OAuth2 :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_Kbg3RnTBNkDd_RQ0zn59mQ.png)

2. Regardez du côté gauche du site et vous verrez une liste de services. Faites défiler jusqu'à ce que vous voyiez Gmail API v1.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_BppvkU1r4JzZ6j6FvC2qNw.png)

3. Cliquez sur **Autoriser les APIs**

Vous verrez un écran pour vous connecter à l'un de vos comptes Gmail. Choisissez celui que vous avez listé comme utilisateur de test.

4. L'écran suivant vous informera que Google n'a pas encore vérifié cette application, mais ce n'est pas grave puisque nous ne l'avons pas soumise pour vérification. Cliquez sur continuer.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_rL0tNdaZqOyIg6aCp4IR3g.png)

5. Dans l'écran suivant, vous serez invité à accorder la permission à votre projet d'interagir avec votre compte Gmail. Faites-le.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_y0TUXbtC_oUaB6KoGlURbQ.png)

6. Une fois cela fait, vous serez redirigé vers le terrain de jeu OAuth et vous pourrez voir qu'il y a un code d'autorisation dans le menu de gauche. Cliquez sur le bouton bleu étiqueté **Échanger le code d'autorisation contre des jetons**.

Les champs pour le jeton de rafraîchissement et le jeton d'accès seront maintenant remplis.

## Retour au serveur

Après avoir fait toutes ces configurations, nous pouvons retourner à notre application et entrer toutes ces données dans la création du transporter. Afin de garder toutes vos informations d'identification privées, vous pouvez utiliser le [package dotenv](https://www.npmjs.com/package/dotenv). N'oubliez pas d'ajouter également le fichier .env que vous créerez à .gitignore.

Donc, maintenant nous avons ceci :

```node.js
let transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        type: 'OAuth2',
        user: process.env.MAIL_USERNAME,
        pass: process.env.MAIL_PASSWORD,
        clientId: process.env.OAUTH_CLIENTID,
        clientSecret: process.env.OAUTH_CLIENT_SECRET,
        refreshToken: process.env.OAUTH_REFRESH_TOKEN
      }
    });
```

Ensuite, nous créerons l'objet mailOptions, qui contient les détails de l'endroit où envoyer l'email et avec quelles données.

```node.js
let mailOptions = {
      from: tomerpacific@gmail.com,
      to: tomerpacific@gmail.com,
      subject: 'Projet Nodemailer',
      text: 'Bonjour de la part de votre projet nodemailer'
    };
```

Cet objet peut avoir beaucoup plus de champs et même plusieurs destinataires, mais nous n'entrerons pas dans les détails ici.

Enfin, nous utiliserons la méthode sendMail :

```node.js
transporter.sendMail(mailOptions, function(err, data) {
      if (err) {
        console.log("Erreur " + err);
      } else {
        console.log("Email envoyé avec succès");
      }
    });
```

Exécutez votre application et vous verrez votre boîte de réception se remplir avec un nouvel email.

Cet article a été inspiré par un projet que j'ai créé et qui utilise Nodemailer. Si vous souhaitez le consulter, allez [ici](https://github.com/TomerPacific/ProjectChecker).