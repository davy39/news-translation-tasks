---
title: Comment utiliser l'API Payment Request en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-24T22:40:51.000Z'
originalURL: https://freecodecamp.org/news/payment-request-api-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/js-payment-request.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: payments
  slug: payments
seo_title: Comment utiliser l'API Payment Request en JavaScript
seo_desc: "By  Atta ✨\nThe Payment Request API provides a cross-browser standard that\
  \ lets you collect payments, addresses, and contact information from your customers.\
  \ You can then use this info to process their order. \nIt also facilitates the exchange\
  \ of this ..."
---

Par Atta ✨

L'API Payment Request fournit une norme multi-navigateurs qui vous permet de collecter des paiements, des adresses et des informations de contact auprès de vos clients. Vous pouvez ensuite utiliser ces informations pour traiter leur commande.

Elle facilite également l'échange de ces informations entre le navigateur et le site web. L'idée fondamentale derrière cela est d'améliorer l'expérience d'achat en ligne de l'utilisateur en facilitant le stockage des informations de paiement et de contact dans le navigateur.

## Prise en charge de l'API Payment Request par les navigateurs

L'API Payment Request est encore en développement actif et n'est prise en charge que par [les dernières versions](https://caniuse.com/#feat=payment-request) des navigateurs modernes.

Avant de commencer à faire une demande de paiement, vous devez détecter la fonctionnalité pour vous assurer que l'API est prise en charge par le navigateur :

```javascript
if (window.PaymentRequest) {
  // Oui, nous pouvons utiliser l'API
} else {
  // Non, basculer vers la page de paiement
  window.location.href = '/checkout'
}
```

Notez que vous ne pouvez utiliser l'API Payment Request que sur les sites servis via `https`.

Maintenant, voyons comment cette API utile fonctionne.

## Comment créer l'objet PaymentRequest

Une demande de paiement commence toujours par la création d'un nouvel objet `PaymentRequest` en utilisant le constructeur `PaymentRequest()`. Le constructeur prend deux paramètres obligatoires et un paramètre facultatif :

* `paymentMethods` définit quelles formes de paiement sont acceptées. Par exemple, vous pouvez n'accepter que les cartes de crédit Visa et MasterCard.
* `paymentDetails` contient le montant total du paiement dû, les taxes, les frais de livraison, les articles affichés, etc.
* `options` est un argument facultatif utilisé pour demander des détails supplémentaires à l'utilisateur, tels que le nom, l'e-mail, le téléphone, etc.

Ensuite, nous allons créer une nouvelle demande de paiement avec uniquement les paramètres requis.

### Comment utiliser le paramètre `paymentMethods`

```javascript
const paymentMethods = [
  {
    supportedMethods: ['basic-card']
  }
]

const paymentDetails = {
  total: {
    label: 'Montant total',
    amount: {
      currency: 'USD',
      value: 8.49
    }
  }
}

const paymentRequest = new PaymentRequest(paymentMethods, paymentDetails)
```

Remarquez le paramètre `supportedMethods` dans l'objet `paymentMethods`. Lorsqu'il est défini sur `basic-card`, les cartes de débit et de crédit de tous les réseaux seront acceptées.

Mais vous pouvez limiter les réseaux pris en charge et les types de cartes. Par exemple, avec ce qui suit, seules les cartes de crédit Visa, MasterCard et Discover sont acceptées :

```javascript
const paymentMethods = [
  {
    supportedMethods: ['basic-card'],
    data: {
      supportedNetworks: ['visa', 'mastercard', 'discover'],
      supportedTypes: ['credit']
    }
  }
]
// ...
```

### Comment utiliser l'objet `paymentDetails`

Le deuxième paramètre passé au constructeur `PaymentRequest` est l'objet des détails de paiement. Il contient le total de la commande et un tableau facultatif d'articles affichés. Le paramètre `total` doit inclure un paramètre `label` et un paramètre `amount` avec `currency` et `value`.

Vous pouvez également ajouter des articles affichés supplémentaires pour fournir une ventilation de haut niveau du total :

```javascript
const paymentDetails = {
  total: {
    label: 'Montant total',
    amount: {
      currency: 'USD',
      value: 8.49
    }
  },
  displayItems: [
    {
      label: 'Remise de 15%',
      amount: {
        currency: 'USD',
        value: -1.49
      }
    },
    {
      label: 'Taxe',
      amount: {
        currency: 'USD',
        value: 0.79
      }
    }
  ]
}
```

Le paramètre `displayItems` n'est pas destiné à afficher une longue liste d'articles. Comme l'espace est limité pour l'interface de paiement du navigateur sur les appareils mobiles, vous devez utiliser ce paramètre pour afficher uniquement les champs de haut niveau tels que le sous-total, la remise, la taxe, les frais de livraison, etc.

Gardez à l'esprit que l'API `PaymentRequest` ne effectue aucun calcul. Ainsi, votre application web est responsable de fournir le montant `total` pré-calculé.

### Comment utiliser l'argument `options` pour demander des détails supplémentaires

Vous pouvez utiliser le troisième paramètre facultatif pour demander des informations supplémentaires à l'utilisateur, telles que le nom, l'adresse e-mail et le numéro de téléphone :

```javascript
// ...
const options = {
  requestPayerName: true,
  requestPayerPhone: true,
  requestPayerEmail: true
}

const paymentRequest = new PaymentRequest(paymentMethods, paymentDetails, options)
```

Par défaut, toutes ces valeurs sont `false`, mais l'ajout de l'une d'entre elles à l'objet `options` avec une valeur `true` entraînera une étape supplémentaire dans l'interface de paiement. Si l'utilisateur a déjà stocké ces détails dans le navigateur, ils seront pré-remplis.

## Comment afficher l'interface de paiement

Après avoir créé un objet `PaymentRequest`, vous devez appeler la méthode `show()` pour afficher l'interface de demande de paiement à l'utilisateur.

La méthode `show()` retourne une [promesse](https://www.freecodecamp.org/news/javascript-promises-for-beginners/) qui se résout avec un objet `PaymentResponse` si l'utilisateur a correctement rempli les détails. Si une erreur se produit ou si l'utilisateur ferme l'interface, la promesse est rejetée.

```javascript
// ...
const paymentRequest = new PaymentRequest(paymentMethods, paymentDetails, options)

paymentRequest
  .show()
  .then(paymentResponse => {
    // fermer l'interface de paiement
    paymentResponse.complete().then(() => {
      // TODO: appeler l'API REST pour traiter le paiement sur le serveur backend
      // avec les données de `paymentResponse`.
    })
  })
  .catch(err => {
    // l'utilisateur a fermé l'interface ou l'API a généré une erreur
    console.log('Erreur :', err)
  })
```

Avec le code ci-dessus, le navigateur affichera l'interface de paiement à l'utilisateur. Une fois que l'utilisateur a rempli les détails et cliqué sur le bouton 'Payer', vous recevrez un objet `PaymentResponse` dans la promesse `show()`.

L'interface de demande de paiement est fermée immédiatement lorsque vous appelez la méthode `PaymentResponse.complete()`. Cette méthode retourne une nouvelle promesse afin que vous puissiez appeler le serveur backend avec les informations collectées et traiter le paiement.

![Interface de demande de paiement](https://cdn.attacomsian.com/gims/da91575d-9de1-448e-92dc-9c255083f271.jpg)

Si vous souhaitez appeler le serveur backend pour traiter le paiement pendant que l'interface de paiement affiche une animation de chargement, vous pouvez retarder l'appel à `complete()`.

Créons une fonction fictive pour le traitement du paiement avec le serveur backend. Elle prend `paymentResponse` comme paramètre et retourne une promesse après 1,5 seconde qui se résout en un [objet JSON](https://www.freecodecamp.org/news/what-is-json-a-json-file-example/) :

```javascript
const processPaymentWithServer = paymentResponse => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({ status: true })
    }, 1500)
  })
}

//...
paymentRequest
  .show()
  .then(paymentResponse => {
    processPaymentWithServer(paymentResponse).then(data => {
      if (data.status) {
        paymentResponse.complete('success')
      } else {
        paymentResponse.complete('fail')
      }
    })
  })
  .catch(err => {
    console.log('Erreur :', err)
  })
```

Dans l'exemple ci-dessus, l'interface de paiement du navigateur affichera un écran de traitement jusqu'à ce que la promesse retournée par la méthode `processPaymentWithServer()` soit résolue. Nous avons également utilisé les chaînes 'success' et 'fail' pour informer le navigateur du résultat de la transaction. Le navigateur affichera un message d'erreur à l'utilisateur si vous appelez `complete('fail')`.

## Comment annuler une demande de paiement

Si vous souhaitez annuler la demande de paiement en raison d'une inactivité ou pour toute autre raison, vous pouvez utiliser la méthode `PaymentRequest.abort()`. Elle ferme immédiatement l'interface de demande de paiement et rejette la promesse `show()`.

```javascript
// ...
setTimeout(() => {
  paymentRequest
    .abort()
    .then(() => {
      // demande de paiement annulée
      console.log('Demande de paiement annulée en raison d'une inactivité.')
    })
    .catch(err => {
      // erreur lors de l'annulation
      console.log('Erreur abort() : ', err)
    })
}, 5000)
```

## Conclusion

C'est la fin d'une rapide introduction à l'API Payment Request en JavaScript. Elle fournit une méthode basée sur le navigateur pour collecter les informations de paiement et de contact du client qui peuvent être envoyées au serveur backend pour traiter le paiement.

L'objectif est de réduire le nombre d'étapes pour effectuer un paiement en ligne. Cela rend l'ensemble du processus de paiement plus fluide en mémorisant la méthode de paiement préférée de l'utilisateur pour les biens et services.

Si vous souhaitez en savoir plus sur l'API Payment Request, voici une [bonne ressource](https://developer.mozilla.org/en-US/docs/Web/API/Payment_Request_API) qui discute des principaux concepts et de l'utilisation de l'API.


## Merci d'avoir lu !

Si vous souhaitez en savoir plus sur JavaScript, vous pouvez consulter mon [blog personnel](https://attacomsian.com/), où j'ai publié plus de 235 tutoriels sur les objets JavaScript, les tableaux, les chaînes, les API Web, et plus encore.

Je suis également le fondateur de [AcquireBase](https://acquirebase.com). Vous pouvez me suivre sur [Twitter](https://twitter.com/attacomsian) pour recevoir des mises à jour lorsque je publie de nouveaux tutoriels ou partage des projets parallèles.