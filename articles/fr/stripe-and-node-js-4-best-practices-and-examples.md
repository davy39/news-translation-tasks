---
title: 'Comment créer une excellente intégration Stripe avec Node.js : 4 bonnes pratiques
  et exemples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-28T17:23:26.000Z'
originalURL: https://freecodecamp.org/news/stripe-and-node-js-4-best-practices-and-examples
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/BLOG_003_Stripe-and-Node.js_-4-Best-Practices-and-Examples.jpg
tags:
- name: node
  slug: node
- name: Node.js
  slug: nodejs
- name: stripe
  slug: stripe
seo_title: 'Comment créer une excellente intégration Stripe avec Node.js : 4 bonnes
  pratiques et exemples'
seo_desc: 'By Ben Sears

  Have you ever woken up in the middle of the night, worried that you are not using
  the Stripe npm module properly? Probably not, but this article will help put your
  troubled soul at ease anyway with some interactive Node.js examples that ...'
---

Par Ben Sears

Vous êtes-vous déjà réveillé en pleine nuit, inquiet de ne pas utiliser correctement le module npm Stripe ? Probablement pas, mais cet article vous aidera tout de même à apaiser votre âme tourmentée avec des exemples interactifs Node.js qui expliquent comment construire une excellente intégration Stripe.

## 1. Utilisez l'auto-pagination pour éviter un code gonflé

La pagination est un mal nécessaire qui nous évite de charger trop de données, mais la gérer dans le code peut être fastidieux. Avant la version `v6.11.0`, votre code Stripe ressemblait à quelque chose comme ceci pour gérer la pagination :

#### Cet exemple montre l'ancienne méthode de gestion de la pagination dans Stripe
<pre class="runkit-element">
//require Stripe's Node bindings
const stripe = require("stripe")("rk_test_72wdhn7pifTOWbrtrSNFxhsQ00NrdzPvaC")

//get first 100 invoices
let invoices = await stripe.invoices.list({limit: 100});
let numberProcessed = 0;

//loop through these invoices
for(let invoice of invoices.data){
    numberProcessed++;
}

//has_more indicates if we need to deal with pagination
while(invoices.has_more){

    //starting_after will be the the id of the last result
    invoices = await stripe.invoices.list({limit: 100, starting_after: invoices.data[invoices.data.length -1].id});
    
    //loop through the next 100
    for(let invoice of invoices.data){
        numberProcessed++;
    }
    console.log("Number processed so far: " + numberProcessed);
}
console.log("Total Number Processed: " + numberProcessed);
</pre>

Avec l'introduction de l'auto-pagination dans `v6.11.0`, nous avons maintenant une méthode beaucoup plus efficace pour paginer :

#### Cet exemple montre comment utiliser l'auto-pagination dans Stripe
<pre class="runkit-element">
//require Stripe's Node bindings
const stripe = require("stripe")("rk_test_72wdhn7pifTOWbrtrSNFxhsQ00NrdzPvaC")

//get all invoices
const allInvoices = await stripe.invoices.list({limit: 100}).autoPagingToArray({limit: 10000});
console.log("Invoices - " + allInvoices.length);
</pre>

> Note : Vous devez utiliser Node.js v10 ou supérieur pour cela.

## 2. Utilisez expand pour réduire le nombre d'appels API

Dans Stripe, il existe de nombreux objets différents. Souvent, lorsque vous traitez un type d'objet, par exemple un abonnement, vous souhaitez obtenir le produit auquel cet abonnement appartient. Pour obtenir le produit, vous devez effectuer un appel supplémentaire à Stripe comme montré ici :

#### Cet exemple montre comment obtenir le produit d'un abonnement dans Stripe sans utiliser expand
<pre class="runkit-element">
//require Stripe's Node bindings
const stripe = require("stripe")("rk_test_3U9s3aPLquPOczvc4FVRQKdo00AhMZlMIE")

const subscription = await stripe.subscriptions.retrieve("sub_G0zK9485afDl6O");
const product = await stripe.products.retrieve(subscription.plan.product);
console.log(product.name);
</pre>

Nous pouvons éviter cela efficacement en utilisant l'attribut ["expand" dans l'API de Stripe](https://stripe.com/docs/api/expanding_objects) :

#### Cet exemple montre comment obtenir le produit en utilisant expand
<pre class="runkit-element">
//require Stripe's Node bindings
const stripe = require("stripe")("rk_test_3U9s3aPLquPOczvc4FVRQKdo00AhMZlMIE")

//expand the product inside the plan
const subscription = await stripe.subscriptions.retrieve("sub_G0zK9485afDl6O", {expand: "plan.product"});
console.log(subscription.plan.product.name);
</pre>

Réduire le nombre d'appels API améliorera les performances de votre application et réduira le risque d'atteindre les limites de l'API Stripe.

## 3. Configurez votre connexion Stripe pour une expérience plus stable

La plupart des personnes avec une intégration Stripe simple définiront une nouvelle connexion Stripe à la volée sans la configurer au préalable comme ceci :

`const stripe = require("stripe")("STRIPE_SECRET_KEY");`

Lorsque vous scalez votre système de facturation, envisagez de faire ce qui suit pour améliorer la qualité de votre intégration :

* **Verrouillez votre version d'API pour éviter d'être affecté par les changements d'API**
* **Configurez pour réessayer automatiquement en cas de défaillance réseau**
* **Définissez les informations de votre application pour aider l'équipe Stripe**

#### Voici un exemple de fonction qui retourne une connexion Stripe configurée
<pre class="runkit-element">
function createStripeConnection(stripe_api_key){
    const Stripe = require("stripe");
    const stripe = Stripe(stripe_api_key);
    stripe.setApiVersion('2019-03-14');//lock API version down to avoid code breaking
    stripe.setAppInfo({
        name: 'Servicebot',
        version: "1.1.3", //Optional
        url: 'https://servicebot.io' // Optional
    });
    stripe.setMaxNetworkRetries(3); //retry on network failure
    return stripe;
}

const stripe = createStripeConnection("rk_test_72wdhn7pifTOWbrtrSNFxhsQ00NrdzPvaC");
console.log(await stripe.invoices.list());
</pre>


## 4. Utilisez les Webhooks pour traiter les événements qui se produisent dans Stripe

Les Webhooks jouent un rôle essentiel dans la plupart des intégrations Stripe. Il existe [de nombreux événements différents](https://stripe.com/docs/api/events/types) qui peuvent se produire, alors lesquels devriez-vous surveiller ?

Le webhook le plus important pour une application SaaS à surveiller est [customer.subscription.deleted](https://stripe.com/docs/api/events/types#event_types-customer.subscription.deleted) - lorsqu'un abonnement passe à l'état annulé. Vous écoutez cet événement afin de décider quoi faire avec le compte de quelqu'un lorsqu'il annule, que son essai gratuit expire ou que sa carte échoue.

Une fois que vous commencez à écouter les événements Stripe, il est bon de sécuriser votre récepteur de webhook pour éviter de recevoir de faux webhooks d'un acteur malveillant. Vous faites cela en utilisant la fonctionnalité de signature des webhooks de Stripe :

### Cet exemple montre comment valider qu'un webhook provient de Stripe

```javascript
// Définissez votre clé secrète : n'oubliez pas de la changer pour votre clé secrète en production
// Voir vos clés ici : https://dashboard.stripe.com/account/apikeys
const stripe = require('stripe')('sk_test_bkoS59kZFWBR3XZgkiHwozoX00lD4ttSs1');

// Trouvez le secret de votre endpoint dans les paramètres de webhook de votre Dashboard
const endpointSecret = 'whsec_...';

// Cet exemple utilise Express pour recevoir les webhooks
const app = require('express')();

// Utilisez body-parser pour récupérer le corps brut sous forme de buffer
const bodyParser = require('body-parser');

// Faites correspondre le corps brut au type de contenu application/json
app.post('/webhook', bodyParser.raw({type: 'application/json'}), (request, response) => {
  const sig = request.headers['stripe-signature'];

  let event;

  try {
    event = stripe.webhooks.constructEvent(request.body, sig, endpointSecret);
  }
  catch (err) {
    response.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Traitez l'événement
  switch (event.type) {
    case 'payment_intent.succeeded':
      const paymentIntent = event.data.object;
      handlePaymentIntentSucceeded(paymentIntent);
      break;
    case 'payment_method.attached':
      const paymentMethod = event.data.object;
      handlePaymentMethodAttached(paymentMethod);
      break;
    // ... traitez d'autres types d'événements
    default:
      // Type d'événement inattendu
      return response.status(400).end();
  }

  // Retournez une réponse pour accuser réception de l'événement
  response.json({received: true});
});

app.listen(8000, () => console.log('Running on port 8000'));

```



---

## Évitez l'effort de construire et de maintenir une intégration Stripe complexe

Votre code de facturation peut devenir assez compliqué lorsqu'il s'agit d'avoir une solution complète qui inclut des coupons, des essais gratuits, une facturation mesurée, et plus encore.

Construire une interface utilisateur pour votre intégration Stripe pourrait prendre des mois à développer. [Servicebot](https://servicebot.io) fournit une interface utilisateur clé en main pour la facturation Stripe. Cela prend moins d'une heure à configurer et ne nécessite aucun effort de développement.

<a href="https://servicebot.io"><img src="https://i.imgur.com/QJkpyHN.png"/></a>