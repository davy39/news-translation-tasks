---
title: Comment créer un flux d'intégration de facturation Stripe pour votre SaaS en
  utilisant NodeJS et React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-16T14:59:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-stripe-billing-onboarding-flow-for-your-saas-using-nodejs-and-react
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/BLOG_001_How-to-build-a-Stripe-Billing-onboarding-flow-for-your-SaaS-using-NodeJS-and-React.jpg
tags:
- name: Node.js
  slug: nodejs
- name: React
  slug: react
seo_title: Comment créer un flux d'intégration de facturation Stripe pour votre SaaS
  en utilisant NodeJS et React
seo_desc: 'By Ben Sears

  What will you learn?

  In this article we will be going over the steps needed to integrate Stripe Billing
  with an onboarding flow using NodeJS and React. In the guide we will be:


  Configuring a Stripe account with a pricing strategy we wil...'
---

Par Ben Sears

# Qu'allez-vous apprendre ?

Dans cet article, nous allons passer en revue les étapes nécessaires pour intégrer Stripe Billing avec un flux d'intégration en utilisant NodeJS et React. Dans ce guide, nous allons :

* Configurer un compte Stripe avec une stratégie de tarification que nous utiliserons dans cet exemple
* Configurer une route dans ExpressJS qui exposera la stratégie de tarification au front-end
* Configurer un front-end React qui gérera le flux d'intégration, en utilisant [Stripe Elements](https://stripe.com/payments/elements) pour le checkout

Dans cet article, nous supposons que vous avez déjà une connaissance pratique de Node et ExpressJS ainsi que des étapes nécessaires pour créer une application React. Pour quelques bonnes ressources sur la façon d'apprendre ces technologies, consultez :

* [ExpressJS sur FreeCodeCamp](https://guide.freecodecamp.org/nodejs/express/)
* [React sur FreeCodeCamp](https://learn.freecodecamp.org/front-end-libraries/react/)

# Définir vos produits et plans dans Stripe

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-64.png)

La première étape consiste à créer des produits et des plans dans votre compte Stripe. Si vous n'êtes pas encore inscrit à Stripe, vous pouvez le faire [ici](https://dashboard.stripe.com/register).

Pour cet exemple, nous allons créer une stratégie de tarification à deux niveaux, avec un niveau Basic à 50 $/mois et un niveau Premium à 300 $/mois, définis comme des produits distincts dans Stripe.

![Image](https://blog.servicebot.io/content/images/2019/10/image-10.png)
_Les produits que nous créons avec les plans associés_

Si vous souhaitez automatiser cela pour votre compte Stripe spécifique, n'hésitez pas à modifier la clé secrète dans ce RunKit avec votre clé de test Stripe.

### Ce code créera des produits et des plans dans Stripe
<pre class="runkit-element">
const STRIPE_TEST_SECRET_KEY = "sk_test_6pewDqcB8xcSPKbV1NJxsew800veCmG5zJ"//votre clé Stripe ici
const stripe = require('stripe')(STRIPE_TEST_SECRET_KEY);

const basicPlan = await stripe.plans.create({
    amount: 5000, 
    interval: "month", 
    product: {
        name : "AcmeBot Basic"
    },
    currency: "USD"
})
const premiumPlan = await stripe.plans.create({
    amount: 30000, 
    interval: "month", 
    product: {
        name : "AcmeBot Premium"
    },
    currency: "USD"
})
console.log(`Stripe Plans that were Created:`);
console.log(`AcmeBot Basic, Plan ID: ${basicPlan.id}, Amount: $${basicPlan.amount/100}/${basicPlan.interval}, Product ID: ${basicPlan.product}`)
console.log(`AcmeBot Premium, Plan ID: ${premiumPlan.id}, Amount: $${premiumPlan.amount/100}/${premiumPlan.interval}, Product ID: ${premiumPlan.product}`)
</pre>

# Créer un endpoint REST pour obtenir les plans

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-62.png)

Après avoir configuré votre Stripe, nous pouvons définir un nouvel endpoint REST dans Express que notre React peut consommer afin de rendre un flux d'intégration en utilisant des données Stripe en direct.

Pour rendre une page de tarification, le front-end devra connaître les plans de votre compte Stripe, donc notre code effectuera un appel API à Stripe en utilisant le module `stripe`. Voici à quoi pourrait ressembler un exemple de middleware ExpressJS qui fait cela.

### Middleware ExpressJS pour obtenir tous les plans Stripe          
<pre class="runkit-element">
const STRIPE_TEST_SECRET_KEY = "rk_test_3U9s3aPLquPOczvc4FVRQKdo00AhMZlMIE"; //votre clé Stripe ici
const stripe = require('stripe')(STRIPE_TEST_SECRET_KEY);


//middleware express
async function getAllPlans(req, res, next){

    //obtenir tous les plans, le mot-clé expand retournera également le contenu du produit auquel ce plan est attaché
    const plans = await stripe.plans.list({expand: ["data.product"]});
    res.json(plans);
}


//voir cela en action
const req = {}; // req non utilisé
const res = {
    json : function(payload){
        console.log("Tous les plans Stripe :")
        for(let plan of payload.data){
            console.log(`Plan ${plan.id}, Nom : ${plan.product.name}, Montant : ${plan.amount/100}/${plan.interval}`)
        }
        console.log("payload :", payload);
}
};
const next = function(){};
await getAllPlans(req, res, next)
</pre>

Après cette étape, nous pouvons faire notre front-end en React afin d'afficher une page de tarification et un flux de checkout.

# Créer un composant pour afficher les tarifs

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-63.png)

Pour créer une page de tarification, nous devons définir un composant qui rend les données de plan obtenues à partir de l'API REST que nous avons définie ci-dessus.

Le composant ressemblera à quelque chose comme ceci. Il parcourra tous les plans et rendra les informations pertinentes telles que le prix, le nom et l'intervalle. Il affichera également une page de checkout (que nous définirons à l'étape suivante) lorsque l'utilisateur appuiera sur "Commencer".

```javascript
function Pricing({pricingPlans, onPlanSelect}){
  return <div>{pricingPlans.data.map(({id, interval, amount, product: {name}})=>{
      return <div>
        <h1>{name}</h1>
        <h4>${amount/100}/{interval}</h4>
        <button onClick={onPlanSelect(id)}>Commencer</button>
      </div>
    })}</div>
}
```

Vous pouvez voir ce code en action ci-dessous dans le CodePen. Notez que, pour ce CodePen, nous ne faisons pas d'appel API et définissons simplement le payload de manière statique. Dans votre propre implémentation, vous devriez obtenir le payload directement de votre API.

%[https://codepen.io/bsears/pen/jOOEaap]

# Créer un flux de checkout

Pour la dernière étape, nous allons créer un processus de checkout en utilisant [Stripe Elements](https://stripe.com/payments/elements) et le lier à la page de tarification que nous venons de configurer.

Dans l'exemple précédent, nous avons créé une fonction de rappel qui serait déclenchée lorsque quelqu'un choisit un plan. Nous devons maintenant la lier à Stripe afin que, lorsqu'ils choisissent un plan, ils soient invités avec une page de checkout. Nous le faisons en utilisant [React Stripe Elements](https://github.com/stripe/react-stripe-elements), le wrapper React autour de la bibliothèque Stripe Elements.

Vous pouvez voir cela en action ci-dessous :

%[https://codepen.io/bsears/pen/BaayXME]

Maintenant que nous avons un flux de checkout de base, nous devons [traiter le token](https://stripe.com/docs/sources/cards) généré par le formulaire et [créer un abonnement](https://stripe.com/docs/api/subscriptions/create) pour le nouveau client, ce qui nous donne un nouvel abonnement. Alternativement, vous pourriez, au lieu d'utiliser Stripe Elements, utiliser [Stripe Checkout](https://stripe.com/payments/checkout) qui crée automatiquement des abonnements (mais est moins flexible).

Cela conclut le tutoriel sur la création d'un flux de checkout avec Stripe, React et Node.

## Qu'est-ce qui vient ensuite ?

Merci d'avoir lu ! Cela vous permettra de commencer avec la facturation, mais nous n'avons fait qu'effleurer la surface de la construction d'un système de facturation avec Stripe avec cet article. Des sujets plus avancés tels que les coupons, les stratégies de tarification avancées et les différents intervalles de tarification (mensuel/annuel par exemple) nécessitent beaucoup plus de développement pour être supportés.

Si vous cherchez à obtenir des pages de tarification, des formulaires de checkout et plus encore, à la fois esthétiques et adaptés aux mobiles, sans avoir à tout construire vous-même, consultez [Servicebot](https://servicebot.io) - Un kit d'outils UI prêt à l'emploi construit sur Stripe, vous collez simplement un extrait de code et obtenez un front-end entièrement fonctionnel alimenté par Stripe.

<a href="https://servicebot.io"><img src="https://i.imgur.com/QJkpyHN.png"/></a>