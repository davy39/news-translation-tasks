---
title: Comment recevoir des emails depuis le formulaire "Contactez-nous" de votre
  site en utilisant AWS SES, Lambda & API Gateway
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-24T19:26:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-receive-emails-via-your-sites-contact-us-form-with-aws-ses-lambda-api-gateway
coverImage: https://cdn-media-2.freecodecamp.org/w1280/605b0cfb687d62084bf6bd50.jpg
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: email
  slug: email
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Comment recevoir des emails depuis le formulaire "Contactez-nous" de votre
  site en utilisant AWS SES, Lambda & API Gateway
seo_desc: "By Adham El Banhawy\nI was recently building a simple landing page website\
  \ for a client who wanted to receive emails through their website without sharing\
  \ their email. \nHonestly, I had never tried to implement that functionality myself\
  \ before. I was a..."
---

Par Adham El Banhawy

Je construisais récemment une page de destination simple pour un client qui souhaitait recevoir des emails via son site sans partager son adresse email. 

Honnetement, je n'avais jamais essayé d'implémenter cette fonctionnalité moi-même auparavant. J'avais toujours l'habitude d'avoir un simple bouton "Contactez-nous" avec une balise d'ancrage et un `mailto` dans l'attribut _href_ comme ceci :

```html
<button>
	<a href="mailto:myemail@example.com">Contactez-moi</a>
</button>

```

Mais cette approche présente deux inconvénients :

1. Elle oblige les deux parties, l'utilisateur qui veut envoyer le message et le propriétaire du site qui le reçoit, à partager leurs emails l'un avec l'autre. Bien que cela soit acceptable pour certains, ce n'est pas idéal pour les personnes soucieuses de leur vie privée.
2. Pour le visiteur du site, cliquer sur le lien l'oblige à ouvrir son programme de messagerie par défaut sur son appareil, et cela peut être frustrant. Et s'il utilise un ordinateur public ? Et s'il n'est pas connecté ? Et s'il ne veut tout simplement pas utiliser son programme de messagerie ?   
Oui, techniquement, il peut simplement copier l'adresse email du destinataire et envoyer le message via son navigateur ou là où il est connecté. Mais ce sont toutes des étapes supplémentaires et des obstacles qui peuvent décourager les utilisateurs d'envoyer leurs messages et l'entreprise pourrait perdre des retours potentiels ou des opportunités.

Pour cette raison, nous avons choisi d'opter pour un formulaire d'email à partir duquel l'utilisateur peut simplement écrire son message et cliquer sur envoyer, envoyant un email au propriétaire du site sans jamais quitter le site web.

Une rapide recherche Google montre qu'il existe des outils/widgets tiers que vous pourriez intégrer dans un site web, mais la plupart sont marqués et nécessitent un abonnement payant pour une personnalisation complète. 

Et à moins que vous n'utilisiez un CMS comme WordPress qui dispose d'un plugin intégré capable de le faire, c'est un coût récurrent inconvenant. 

J'ai plutôt choisi de coder cette fonctionnalité moi-même pour avoir un contrôle total.

Pour les besoins de ce guide, je vais recréer les étapes que j'ai suivies pour implémenter cette fonctionnalité en utilisant HTML et les services AWS.

## Le formulaire HTML

Je vais le garder super simple ici et opter pour un formulaire HTML de base sans CSS, juste pour tester notre fonctionnalité souhaitée.

```html
<h2>Contactez-nous</h2>
<form>
  <label for="name">Nom :</label>
  <input name="name" type="text"/><br/><br/>
  <label for="email">Email :</label>
  <input name="email" type="email"/><br/><br/>
  <label for="name">Message :</label>
  <textarea name="message"></textarea><br/><br/>
  <input type="submit"/>
  <div>
    <p id="result-text"></p>
  </div>
</form>

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-61.png)
_Rien de fantastique à voir ici..._

Maintenant, nous voulons gérer la fonctionnalité de soumission avec JavaScript.

```js
const form = document.querySelector('form')
form.addEventListener('submit', event => {
  // empêcher la soumission du formulaire de rafraîchir la page
  event.preventDefault()
 
  const { name, email, message } = event.target
  console.log('Nom : ', name.value)
  console.log('email : ', email.value)
  console.log('Message : ', message.value)
  
})

```

À ce stade, nous avons un formulaire qui reçoit les entrées de l'utilisateur et un code JavaScript qui affiche simplement les résultats dans la console. 

Nous pouvons en rester là pour l'instant et commencer à travailler sur les services backend qui recevront les données du formulaire et enverront un email avec ces données.

## Aperçu du Backend

Plongeons dans AWS et voyons quels services nous allons utiliser et comment. 

Comme mentionné dans le titre, nous allons utiliser **AWS Lambda** et **Simple Email Service** (SES). SES est un service de messagerie serverless qui vous permet d'envoyer des messages email lorsqu'il est invoqué. AWS Lambda vous permet d'écrire du code côté serveur pour exécuter en réponse à des événements. 

Nous allons également utiliser **API Gateway** qui nous permet d'invoquer des fonctions Lambda via HTTP.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-62.png)

Dans ce cas, lorsque notre formulaire est soumis, le flux de travail suivant se produira :

1. Notre navigateur (JavaScript) effectuera une requête POST, avec les données du formulaire dans le corps de la requête, à une URL de point de terminaison spécifiée par AWS API Gateway
2. L'API Gateway validera cette requête. Ensuite, elle déclenchera la fonction Lambda qui accepte un paramètre d'événement. L'API Gateway placera les données du formulaire dans la propriété body du paramètre d'événement.
3. Notre fonction Lambda extraira les données du corps de l'événement et nous utiliserons ces données pour construire le corps de l'email que nous voulons envoyer ainsi que ses destinataires. Notre fonction utilisera ensuite le SDK AWS pour invoquer SES avec les données de l'email.
4. Une fois que SES reçoit la requête _sendMail_, il transforme les données de l'email en un email texte réel et l'envoie au destinataire via les propres serveurs de messagerie d'AWS.

Une fois l'email envoyé, notre navigateur recevra une réponse avec le code de statut 200 et un message de succès. Si une étape dans le cloud AWS échoue, la réponse aura un code de statut 500.

## Étape 1 : Comment configurer SES

Nous allons en fait configurer chacune de ces étapes dans l'ordre inverse, en commençant par SES, ce qui sera plus facile.

Tout d'abord, dans votre console AWS, allez au service SES —> puis cliquez sur Adresses email dans le menu latéral —> puis cliquez sur le bouton "Vérifier une nouvelle adresse email".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-63.png)

Dans la boîte de dialogue qui s'ouvre, entrez l'adresse email que vous souhaitez que le service SES utilise comme _expéditeur_ lorsqu'il envoie l'email.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-64.png)

Cela enverra un email à l'adresse email que vous avez entrée avec un lien à cliquer pour vérifier. C'est ainsi qu'AWS sait que le propriétaire de l'email consent à ce que son adresse email soit utilisée comme adresse d'expéditeur.

Jusqu'à ce que vous vérifiiez l'email, le tableau de bord des emails SES maintiendra le statut de vérification comme en attente.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-65.png)

Une fois que le propriétaire de l'email ouvre l'email qu'il a reçu d'AWS et clique sur le lien de vérification, le statut de vérification devrait passer à vérifié (rafraîchissez la page pour voir le changement).

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-66.png)

Et c'est tout ce que vous avez à faire pour SES. Vous pouvez éventuellement tester le service en sélectionnant votre email vérifié dans la liste et en cliquant sur le bouton "Envoyer un email de test". Cela vous permettra de saisir une adresse email de destinataire, un sujet et un message et de l'envoyer.

L'email envoyé sera signé par les serveurs AWS et votre adresse vérifiée devrait être l'expéditeur. Il devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-67.png)

## Étape 2 : Comment configurer Lambda

Maintenant, c'est la partie la plus amusante. Nous allons créer une fonction qui recevra les données du formulaire et appellera SES. 

La beauté des fonctions Lambda est que vous n'avez pas à vous soucier de l'exécution de votre code backend sur un serveur 24/7 et de la maintenance de ce serveur. C'est _serverless_. 

Mais cela ne signifie pas qu'il n'y a pas de serveurs impliqués. AWS va s'en occuper sous le capot afin que vous puissiez vous concentrer uniquement sur l'écriture de code, et non sur la maintenance des serveurs. De plus, vous n'êtes facturé que pour le nombre de fois où votre fonction est appelée et le temps qu'il faut pour l'exécuter, et c'est [incroyablement bon marché](https://aws.amazon.com/lambda/pricing/) !

### Créer un rôle IAM et le configurer

Avant de commencer à écrire notre fonction lambda, nous devons créer un rôle IAM à attacher à la fonction et lui accorder des permissions (appelées politiques dans AWS) pour invoquer le service SES.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-68.png)

Depuis votre console AWS, allez au service IAM —> cliquez sur Politiques dans le menu latéral —> puis cliquez sur le bouton "Créer une politique".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-69.png)

Dans la page de création de politique, allez dans l'onglet JSON et collez les permissions suivantes, puis cliquez sur Suivant.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ses:SendEmail",
                "ses:SendRawEmail"
            ],
            "Resource": "*"
        }
    ]
}

```

Dans le troisième écran, nommez la politique et cliquez sur le bouton "Créer une politique".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-70.png)

Maintenant, nous créons un rôle IAM qui sera attaché à la lambda et le lierons à la politique de permissions que nous venons de créer.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-71.png)

Depuis le menu latéral IAM, cliquez sur Rôles puis cliquez sur le bouton "Créer un rôle".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-72.png)

Dans l'écran de création de rôle, assurez-vous que le type sélectionné est "Service AWS" et sélectionnez le cas Lambda puis cliquez sur le bouton "Suivant:Permissions".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-73.png)

Dans l'écran suivant, recherchez la politique que nous avons créée précédemment par son nom et sélectionnez-la, puis cliquez sur suivant.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-74.png)

Dans l'écran de révision, donnez un nom au rôle que vous pouvez retenir puis cliquez sur "Créer un rôle".

Maintenant, nous pouvons créer une nouvelle fonction lambda. Allez au tableau de bord du service Lambda et cliquez sur le bouton "Créer une fonction".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-75.png)

Dans l'écran de création de fonction, nommez votre fonction, sélectionnez l'option "Créer à partir de zéro", et choisissez Node.js comme runtime. 

Sous "Changer le rôle d'exécution par défaut" choisissez l'option "Utiliser un rôle existant" puis choisissez le nom du rôle que vous avez créé dans l'étape précédente dans le menu déroulant "Rôle existant". 

Enfin, cliquez sur le bouton "Créer une fonction" pour créer la fonction.

### Écrire le code et le tester

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-76.png)

Dans l'éditeur, ouvrez le fichier index.js (c'est le fichier qui sera exécuté lorsque votre lambda sera appelée), et remplacez son contenu par le code suivant :

```js
const aws = require("aws-sdk");
const ses = new aws.SES({ region: "us-east-1" });
exports.handler = async function (event) {
  console.log('EVENT: ', event)
  const params = {
    Destination: {
      ToAddresses: ["your@email.com"],
    },
    Message: {
      Body: {
        Text: { 
            Data: `Hello from Lambda!` 
        },
      },
      Subject: { Data: `Message from AWS Lambda` },
    },
    Source: "your@email.com",
  };

  return ses.sendEmail(params).promise()
};

```

Remarquez qu'à la ligne 2 nous utilisons le SDK AWS et créons une instance SES. La raison pour laquelle j'ai choisi **us-east-1** comme région est que c'est _où j'ai enregistré & vérifié mon email_. Assurez-vous de remplacer l'email et d'utiliser la région AWS où vous avez enregistré votre email.

Pour tester cette fonction, cliquez sur le bouton "Déployer". Ensuite, cliquez sur le bouton Test —> Configurer l'événement de test, ce qui devrait ouvrir une boîte de dialogue de configuration de test où vous pouvez créer un nouvel événement de test.  

Dans l'éditeur de corps d'événement de test, entrez le JSON suivant qui imite ce qui viendra éventuellement de notre requête du navigateur. Ensuite, cliquez sur créer.

```json
{
  "body": {
        "senderName": "Namo",
        "senderEmail": "namo@trains.com",
        "message": "I love trains!"
    }
}

```

Maintenant, cliquer sur le bouton de test exécutera le test que nous venons de créer. Il devrait ouvrir un nouvel onglet dans l'éditeur pour nous montrer les logs créés à partir de l'exécution de la fonction, ce qui devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-77.png)

Remarquez que l'objet événement que nous avons journalisé s'affiche ici sous les logs de la fonction avec les données du corps que nous avons utilisées dans l'événement de test.

Ce test devrait avoir envoyé un email à ma boîte de réception également – voyons si cela s'est produit.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-78.png)

Oui, comme prévu. Et cela s'est produit presque immédiatement après l'exécution du test.

Maintenant, modifions notre code de fonction pour obtenir un message plus significatif à partir des données de test.

```js
const aws = require("aws-sdk");
const ses = new aws.SES({ region: "us-east-1" });
exports.handler = async function (event) {
  console.log('EVENT: ', event)
	// Extraire les propriétés du corps de l'événement
  const { senderEmail, senderName, message } = JSON.parse(event.body)
  const params = {
    Destination: {
      ToAddresses: ["the.benhawy@gmail.com"],
    },
		// Interpoler les données dans les chaînes à envoyer
    Message: {
      Body: {
        Text: { 
            Data: `You just got a message from ${senderName} - ${senderEmail}:
            ${message}` 
        },
      },
      Subject: { Data: `Message from ${senderName}` },
    },
    Source: "the.benhawy@gmail.com",
  };

  return ses.sendEmail(params).promise();
};

```

Il est important de noter que lorsque API Gateway appelle notre fonction, elle passera une chaîne au corps de l'événement. C'est pourquoi j'utilise `JSON.parse` sur event.body, pour le transformer en JSON et extraire l'email, le nom et le message de l'expéditeur. Ensuite, j'utilise ces variables dans le texte du corps de l'email et le sujet en utilisant l'interpolation de chaînes.

Si vous essayez le test, le code retournera une erreur. Cela est dû au fait que le test passe un objet JSON à event.body et que nous utilisons JSON.parse sur JSON, ce qui provoque une erreur en JavaScript. 

Malheureusement, l'éditeur de test ne nous permet pas de passer des chaînes à l'événement, nous devrons donc tester cela plus tard depuis un autre endroit.

## Étape 3 : Comment configurer API Gateway

Ensuite, le dernier service AWS que nous allons utiliser est API Gateway, qui permettra à notre navigateur d'envoyer des requêtes HTTP à la fonction Lambda que nous avons créée.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-79.png)

Sans quitter la page de votre fonction lambda, développez la section "Aperçu de la fonction" et cliquez sur "Ajouter un déclencheur".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-80.png)

Ensuite, choisissez API Gateway dans le menu déroulant, HTTP API comme type d'API, "Open" comme mécanisme de sécurité, et cochez l'option de case à cocher CORS. Ensuite, cliquez sur "Ajouter".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-81.png)

Vous devriez être redirigé vers l'onglet "Configuration" de votre fonction, vous montrant le nouveau déclencheur API Gateway que vous venez de créer. À partir de là, notez le **point de terminaison de l'API**. C'est l'URL que nous allons appeler depuis notre navigateur avec les données du formulaire.

## Retour au HTML

Nous pouvons enfin tester le formulaire pour voir s'il envoie des emails ou non.

Modifions notre JavaScript pour gérer l'envoi de la requête lorsque le formulaire est soumis.

```js
const form = document.querySelector("form");
form.addEventListener("submit", (event) => {
  // empêcher la soumission du formulaire de rafraîchir la page
  event.preventDefault();

  const { name, email, message } = event.target;

	// Utilisez votre URL de point de terminaison de l'API que vous avez copiée de l'étape précédente
  const endpoint =
    "<https://5ntvcwwmec.execute-api.us-east-1.amazonaws.com/default/sendContactEmail>";
  // Nous utilisons JSON.stringify ici pour que les données puissent être envoyées sous forme de chaîne via HTTP
	const body = JSON.stringify({
    senderName: name.value,
    senderEmail: email.value,
    message: message.value
  });
  const requestOptions = {
    method: "POST",
    body
  };

  fetch(endpoint, requestOptions)
    .then((response) => {
      if (!response.ok) throw new Error("Error in fetch");
      return response.json();
    })
    .then((response) => {
      document.getElementById("result-text").innerText =
        "Email envoyé avec succès !";
    })
    .catch((error) => {
      document.getElementById("result-text").innerText =
        "Une erreur inconnue s'est produite.";
    });
});

```

Maintenant, le moment de vérité : remplissez le formulaire et cliquez sur envoyer. Si vous voyez le message de succès, cela signifie que l'email a été envoyé.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-82.png)

Puisque je possède l'email auquel le message a été envoyé, je jette un coup d'œil rapide à ma boîte de réception pour voir que j'ai reçu un email de moi-même avec les détails que j'ai utilisés dans le formulaire !

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-83.png)

Si vous avez suivi, vous avez maintenant un formulaire "Contactez-nous" fonctionnel que vous pouvez intégrer à n'importe quel site web. Et vous ne serez facturé que lorsqu'il est réellement utilisé. 

Je ne sais pas pour vous, mais je trouve cela assez génial et presque magique ! Et c'est une belle façon pratique d'utiliser le cloud computing/services dans votre flux de travail. 

Bien sûr, vous pouvez personnaliser ce flux en termes d'utilisation d'un framework frontend comme React ou Vue ou un langage de programmation différent pour Lambda comme Python ou Go.

## Avant de partir...

Merci d'avoir lu jusqu'ici ! J'écris des articles sur JavaScript, le développement cloud, et mes expériences éducatives et professionnelles personnelles en tant que développeur autodidacte. N'hésitez donc pas à me suivre sur Twitter [@adham_benhawy](https://twitter.com/adham_benhawy) où je tweete également à leur sujet !

### Ressources

* [https://aws.amazon.com/premiumsupport/knowledge-center/lambda-send-email-ses/](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-send-email-ses/)
* [https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html](https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html)
* [https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html?icmpid=docs_lambda_console](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html?icmpid=docs_lambda_console)