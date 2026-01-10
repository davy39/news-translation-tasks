---
title: Comment implémenter 3DS2 avec Stripe pour la conformité SCA sous PSD2 en Europe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-18T20:27:18.000Z'
originalURL: https://freecodecamp.org/news/implement-3ds2-for-your-saas-using-stripe-billing-and-be-sca-compliant-for-pds2
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/BLOG_002_Implement-3DS2-for-your-SaaS-using-Stripe-Billing-and-be-SCA-compliant-for-PDS2.png
tags:
- name: 3DS2
  slug: 3ds2
- name: psd2
  slug: psd2
- name: 3ds
  slug: 3ds
- name: node
  slug: node
- name: Node.js
  slug: nodejs
- name: React
  slug: react
- name: React
  slug: reactjs
- name: SCA
  slug: sca
- name: stripe
  slug: stripe
seo_title: Comment implémenter 3DS2 avec Stripe pour la conformité SCA sous PSD2 en
  Europe
seo_desc: 'By Ben Sears

  What are PSD2, SCA, and 3DS?

  PSD2

  The second Payment Services Directive (PSD2) is an EU directive announced in 2015.
  The goal of PSD2 is to protect people when they pay online, promote open banking,
  and make cross-border European payment...'
---

Par Ben Sears

# **Qu'est-ce que PSD2, SCA et 3DS ?**

## **PSD2**

La deuxième directive sur les services de paiement (PSD2) est une directive de l'UE annoncée en 2015. L'objectif de la PSD2 est de protéger les personnes lorsqu'elles paient en ligne, de promouvoir la [banque ouverte](https://en.wikipedia.org/wiki/Open_banking) et de rendre les services de paiement européens transfrontaliers plus sûrs. Elle est entrée en vigueur en septembre 2019.

## **SCA**

L'authentification forte du client (SCA) est une [exigence de la PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2018.069.01.0023.01.ENG&toc=OJ:L:2018:069:TOC) qui garantit que les paiements en ligne sont effectués avec une authentification multifactorielle pour augmenter la sécurité des paiements en ligne. Bien que la PSD2 ait été promulguée en septembre 2019, la SCA a été reportée de 18 mois pour permettre aux commerçants et aux banques plus de temps pour mettre en œuvre des solutions.

## **3DS2**

3-D Secure 2.0 (3DS2) est la deuxième itération du 3DS, utilisé pour alimenter des systèmes de marque tels que [Visa Secure](https://usa.visa.com/visa-everywhere/security.html), [Mastercard Identity Check](https://www.mastercard.us/en-us/merchants/safety-security/identity-check.html) et [American Express SafeKey](https://network.americanexpress.com/globalnetwork/safekey/us/en/). Il a été conçu pour réduire la fraude et fournir une sécurité supplémentaire aux paiements en ligne et est soutenu par de nombreuses grandes banques.

3DS2 est considéré comme une solution conforme à la SCA. Si votre entreprise implémente 3DS2, vous ne risquez plus de voir vos paiements refusés par les banques.

# **La SCA affecte-t-elle votre entreprise SaaS ?**

![Image](https://blog.servicebot.io/content/images/2019/10/image-21.png)

La SCA est considérée comme en vigueur pour tous les paiements de commerce électronique lorsque :

* L'entreprise est dans l'UE
* La banque du client est dans l'UE

Si la SCA s'applique à vous et que vous n'authentifiez pas les transactions de vos clients, vous risquez **de voir vos paiements refusés par les banques**. 

Il existe des exemptions pour plusieurs types de transactions définies dans les [articles 12-18 de la PSD2](https://eba.europa.eu/documents/10180/1761863/Final+draft+RTS+on+SCA+and+CSC+under+PSD2+%28EBA-RTS-2017-02%29.pdf). En tant qu'entreprise SaaS, l'exception la plus critique à noter est **l'article 13**. Cet article stipule que les transactions récurrentes ne doivent pas être soumises à la SCA. Cela signifie que vous n'avez besoin d'une implémentation SCA que pour gérer la création initiale d'un abonnement et non les paiements récurrents ultérieurs.

Si vous êtes intéressé par une analyse des autres exemptions et comment elles peuvent s'appliquer à vous, [Stripe approfondit chacune d'entre elles ici](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication).

# **Devriez-vous être prêt pour la SCA même si vous n'êtes pas en Europe ?**

Il y a des avantages à implémenter une solution telle que 3DS2, même si vous n'êtes pas affecté par la PSD2 ou la SCA. En implémentant 3DS2, vous traiterez les informations des clients de manière beaucoup plus sécurisée, tout en transférant la responsabilité de vous à l'émetteur de la carte, réduisant ainsi le risque de rétrofacturation.

# **Comment devenir conforme à la SCA ?**

Être conforme à la SCA en tant que SaaS signifie que tous les paiements en ligne sont autorisés en utilisant deux des trois éléments,

![Image](https://blog.servicebot.io/content/images/2019/10/image-19.png)

Comme je l'ai mentionné précédemment, 3DS2 est une solution conforme à la SCA. Les solutions clés en main telles que [Servicebot](https://servicebot.io), PayPal et [Stripe Checkout](https://stripe.com/payments/checkout) utilisent déjà 3DS2 et sont donc conformes à la SCA. Si vous utilisez une solution personnalisée utilisant quelque chose comme Stripe Billing ou Braintree pour gérer vos abonnements, vous devrez développer une implémentation 3DS2.

# **Comment implémenter 3DS2 en utilisant Stripe Billing ?**

![Image](https://blog.servicebot.io/content/images/2019/10/image-22.png)

Stripe a créé deux nouveaux objets dans le cadre de l'offre d'une solution conforme à la SCA, PaymentIntent et SetupIntent, pour faciliter l'utilisation de 3DS2. Un PaymentIntent représente l'intention de facturer quelqu'un et est utilisé dans le cadre d'un flux d'authentification de paiement. Les SetupIntents sont similaires aux PaymentIntents, mais ils représentent l'intention de facturer éventuellement la carte de quelqu'un. Vous utiliserez les SetupIntents si votre SaaS propose un essai gratuit ou une offre gratuite, essentiellement partout où une carte de crédit sera facturée à une date ultérieure.

## **Utilisation des PaymentIntents**

Si vous utilisez Stripe Billing pour créer des abonnements, vous utilisez déjà des PaymentIntents par défaut. Ils sont créés et attachés à chaque facture pour chaque nouvel abonnement. Si vous souhaitez savoir si un nouvel abonnement nécessite une SCA, vous pouvez vérifier le statut du `payment_intent` sur le `latest_invoice` de l'abonnement. L'objet contiendra un `status` de `requires_action` - Exécutez le code NodeJS suivant pour le voir en action.

## Ce code crée un abonnement qui nécessite une SCA
<pre class="runkit-element">
const STRIPE_TEST_SECRET_KEY = "rk_test_3U9s3aPLquPOczvc4FVRQKdo00AhMZlMIE";
let stripe = require("stripe")(STRIPE_TEST_SECRET_KEY);
const sub = await stripe.subscriptions.create({ //crée un abonnement nécessitant une SCA
    items: [{plan : "plan_FvnU01xoIPrg9l"}], //$300 par mois sans essai gratuit
    customer: "cus_G0juGVZSLskx57",
    default_payment_method: "pm_1FUiR8CISNxwKLmI8uIQDdnv", //Cette méthode de paiement nécessite toujours une SCA
    expand: ["latest_invoice.payment_intent"] //nous développons la charge utile pour afficher l'intention de paiement
});
const paymentIntent = sub.latest_invoice.payment_intent;
console.log(`Statut de l'abonnement : ${sub.status}`);
console.log(`Statut du PaymentIntent : ${paymentIntent.status}`)
console.log(paymentIntent.status === "requires_action" ? "SCA Requise" : "Aucune SCA Requise");
console.log(sub);
</pre>

Une fois que vous savez que vous avez un abonnement qui nécessite une authentification, vous pouvez utiliser le client_secret du PaymentIntent sur le navigateur pour démarrer un processus d'authentification 3DS2 en utilisant Stripe.js

## **Utilisation de Stripe.js handleCardPayment avec le PaymentIntent**

Stripe.js dispose d'une fonction pratique appelée [handleCardPayment](https://stripe.com/docs/stripe-js/reference#stripe-handle-card-payment), qui prend un secret client d'une intention de paiement et démarre le processus 3DS2 pour authentifier le paiement.

```javascript
await stripe.handleCardPayment('PAYMENTINTENT_SECRET');
```

Vous pouvez voir cela en action ici

%[https://codepen.io/bsears/pen/PooGOLg?editors=1111]

Une fois que le client s'est authentifié, l'abonnement passera d'un état `incomplete` à un état `active`, et le client sera facturé avec succès.

## **SetupIntents**

En tant qu'entreprise SaaS, vous interagirez principalement avec les SetupIntents si vous utilisez un niveau gratuit ou offrez un essai gratuit. Lorsqu'une personne entre une carte de crédit pour l'un de ces abonnements, vous verrez un `pending_setup_intent` sur l'[objet d'abonnement](https://stripe.com/docs/api/subscriptions/object#subscription_object-pending_setup_intent). Le `client_secret` du SetupIntent doit être transmis au front-end afin que Stripe.js puisse démarrer le flux d'authentification 3DS2.

## **Utilisation de Stripe.js handleCardSetup avec le SetupIntent**

Cela est essentiellement identique à la manière dont nous avons traité le PaymentIntent, sauf que nous appelons handleCardSetup à la place

```javascript
await stripe.handleCardSetup('{SETUP_INTENT_CLIENT_SECRET}')
```

Vous pouvez voir un flux SCA SetupIntent en action ci-dessous.

%[https://codepen.io/bsears/pen/RwwGyYw?editors=1111]

Une fois l'authentification terminée, le client peut être transféré vers un plan payant plus tard ou voir sa carte débitée après la fin d'un essai gratuit.

# **Alternative sans code**

Si vous cherchez une solution conforme à la SCA pour Stripe Billing sans avoir à gérer le développement de l'intégration 3DS2, consultez [Servicebot](https://servicebot.io). Nous fournissons une interface utilisateur clé en main pour les entreprises SaaS utilisant Stripe, qui est conforme à la SCA dès la sortie de la boîte ! Vous voulez voir cela en action ? Consultez [cette démonstration](https://dashboard.servicebot.io/examples/signup-embed/0) et utilisez la carte de test `4000002760003184` (toute date d'expiration et CVC).

<a href="https://servicebot.io"><img src="https://i.imgur.com/QJkpyHN.png"/></a>