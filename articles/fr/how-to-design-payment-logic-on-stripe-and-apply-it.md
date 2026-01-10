---
title: Comment concevoir la logique de paiement sur Stripe (et l'appliquer)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-25T07:24:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-design-payment-logic-on-stripe-and-apply-it
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/lee-campbell-DtDlVpy-vvQ-unsplash.jpg
tags:
- name: General Programming
  slug: programming
seo_title: Comment concevoir la logique de paiement sur Stripe (et l'appliquer)
seo_desc: 'By Vitaly Kuprenko

  Payment logic is central to any product that deals with money. After all, a well-designed
  payment architecture, if properly tested, saves tons of time in the future.

  But it may take too long to master the top level of working with ...'
---

Par Vitaly Kuprenko

La logique de paiement est centrale pour tout produit qui traite de l'argent. Après tout, une architecture de paiement bien conçue, si elle est correctement testée, fait gagner beaucoup de temps à l'avenir.

Mais il peut prendre trop de temps pour maîtriser le niveau supérieur de travail avec les passerelles de paiement populaires.

Pour vous aider, j'ai écrit ce guide sur la conception de la logique de paiement sur Stripe. Il inclut des cas d'utilisation, des exemples de projets, et un peu de théorie avec des exemples de code.

Ce guide est principalement destiné aux ingénieurs QA car il aide à comprendre comment tester la logique de paiement basée sur Stripe. Mais ne vous découragez pas, chefs de projet et développeurs. Nous avons beaucoup de détails intéressants pour vous aussi.

## Comment fonctionne Stripe

Commençons par les bases et examinons le schéma de paiement de Stripe.

![Image](https://lh4.googleusercontent.com/TbNvvj8SxuZifs9zYb_vDx3WutphLBQmmoLgOCiUUVofnM7ECswMY7FahTHHQEIEbzsseV7pOs6VhZUiV5q5rTjiFbwnmclwKaDpJwd9-xtkdOlKwusmg7EXyfJhXdGA0SE7yIfD)
_Schéma de paiement pour Stripe_

Ce schéma fonctionne pour les utilisateurs qui achètent du contenu sur des sites web ou via des applications mobiles. Les visiteurs n'ont pas besoin de s'inscrire et d'ajouter des cartes de crédit à leurs profils – Stripe permet de payer pour le contenu de manière transparente.

Tout ce qu'ils ont à faire est d'entrer les détails de la carte de crédit, et la magie opère :

1. Les informations d'identification sont envoyées à Stripe.
2. Stripe tokenise les données et retourne un token au back-end.
3. Le back-end crée une charge.
4. Les données sont envoyées à Stripe à nouveau, et celui-ci partage les détails avec les systèmes de paiement.
5. Les systèmes de paiement répondent à Stripe et indiquent si tout est en ordre. Ou signalent des problèmes.
6. Stripe répond au serveur sur l'état de la transaction.

Si tout se passe bien, l'utilisateur obtient le contenu. Sinon, un message d'erreur.

De plus, il y a deux conditions nécessaires pour utiliser Stripe :

* vous avez un compte bancaire
* vous êtes résident de l'un des 25 pays supportés

### Connecter une carte à Stripe

Lier l'utilisateur de votre produit avec le client Stripe se fait côté serveur. Et cela ressemble à ceci :

1. Les informations de la carte de crédit vont à Stripe (depuis l'application ou le site web) ;
2. Stripe retourne un token, puis il va au back-end ;
3. Le back-end l'envoie à Stripe ;
4. Stripe vérifie si le client existe (si oui, la carte est ajoutée, sinon – il crée un nouveau client et ajoute la carte).

La première carte ajoutée est la méthode de paiement par défaut. Stripe l'utilisera pour effectuer la transaction.

### Se connecter avec un compte Stripe

Si vous construisez une application à la demande comme Uber et que vous voulez que les utilisateurs soient payés (comme les chauffeurs Uber), demandez-leur de créer un compte d'abord.

Il existe trois types de comptes Stripe :

* **Standard**. Un compte déjà existant avec les informations d'identification requises. Enregistré par l'utilisateur, validé par Stripe et une banque.
* **Express**. Permet une intégration facile : vous créez un compte vous-même, et l'utilisateur le remplit avec des détails. Fonctionne aux États-Unis.
* **Custom**. Offre le plus haut niveau de flexibilité et permet de modifier de multiples paramètres. En retour, la plateforme est responsable de chaque interaction avec les utilisateurs.

## Fonctionnalités principales de Stripe

Toujours sur le sujet de comment Stripe fonctionne, je suggère de jeter un œil à ses fonctionnalités.

### Charges

Stripe effectue deux types de charges – **directes** et **de destination**.

**Charge directe**

Revenons au modèle Uber. La plateforme prélève un certain montant aux passagers, et cet argent va directement aux comptes liés, aux chauffeurs. La charge directe implique que les chauffeurs paient tous les frais. De plus, Uber prélève également un pourcentage fixe.

![Image](https://lh6.googleusercontent.com/tuM5RJt54RMYUyNGiJ-hRwNTDL1LrnR1jIoJXD6Sx_pq2QdHinsZDSu6QXhVNk9zYD9YeSVibie04bZUKYxVjxjXTsu8be8_0PcIVS45uVWzwDlwl0-siZCUc9lu0jbk5I34SdbN)

**Charge de destination**

Dans ce cas, la plateforme paie tous les frais, et vous obtenez la valeur nette. Tout d'abord, le montant va au compte Stripe de votre plateforme, puis il y a un transfert automatique vers le partenaire (chauffeurs).

### Autoriser et capturer

Stripe prend en charge les paiements en deux étapes qui permettent aux utilisateurs d'autoriser une charge d'abord et de la capturer plus tard. Les émetteurs de cartes garantissent que les paiements autorisés et le montant requis sont gelés sur la carte du client.

Si la charge n'est pas capturée pendant cette période, l'autorisation est annulée.

**Voici comment cela fonctionne dans Uber** : un passager voit un coût approximatif du trajet lors de la réservation. S'ils acceptent, ce montant est gelé sur leurs cartes jusqu'à ce qu'ils terminent leur trajet.

Lorsque ils terminent le trajet, Uber calcule le prix final et le prélève sur la carte.

C'est la raison pour laquelle les propriétaires de produits choisissent Stripe pour leur [développement d'application de paiement P2P](https://www.cleveroad.com/blog/p2p-payment-app-development). Car la confiance est ce qui compte le plus lorsqu'il s'agit de transactions de pair à pair.

Enfin, voici trois autres fonctionnalités de Stripe que je voudrais mentionner.

**Transfers**. Les transferts vont du compte de la plateforme aux fournisseurs. Par exemple, les chauffeurs Uber lient les comptes Stripe à leurs profils pour recevoir leur salaire.

**Subscriptions**. Cette fonctionnalité est assez flexible et permet aux utilisateurs de définir des intervalles, des périodes d'essai, et d'ajuster l'abonnement à leurs besoins.

**Refunds**. Si les acheteurs veulent récupérer leur argent, les utilisateurs de Stripe peuvent facilement émettre un remboursement sur la carte des clients.

## Gestion des objets Stripe

Ensuite, nous passons aux objets Stripe. Et voici les exemples de code que j'ai promis.

### Objet Source

Voici une checklist pour l'objet source.

<!DOCTYPE html>
    <html>
	<body>
	   <table>
	  <thead>
	    <tr>
	      <th>Clé</th>
	      <th>Valeur</th>
	    </tr>
	  </thead>
	  <tfoot>
	    <tr>
	      <td>customer</td>
	      <td>identifiant stripe du client</td>
	    </tr>
	  </tfoot>
	  <tbody>
	    <tr>
	      <td>id</td>
	      <td>stripe_id de la carte ajoutée</td>
	    </tr>
	    <tr>
	      <td>last4</td>
	      <td>les 4 derniers chiffres de la carte ajoutée</td>
	    </tr>
          <tr>
	      <td>brand</td>
	      <td>compagnie de carte de crédit (Visa, AE)</td>
	    </tr>
          <tr>
	      <td>exp_month, exp_year</td>
	      <td>date d'expiration de la carte</td>
	    </tr>
	  </tbody>
	</table>
	</body>
   </html>

L'objet conserve une méthode de paiement qui aide à compléter la charge. Il est également possible de lier l'objet source avec les utilisateurs. Cela leur permet de stocker toutes les méthodes de paiement là.

Lors des tests, il est crucial de s'assurer qu'une méthode de paiement correspond à la valeur retournée. Vérifiez **last4** et **exp_month/year** pour cela.

Si l'objet source est lié à un client et que vous voulez vous assurer qu'il appartient à la bonne personne, vérifiez l'**identifiant du client**.
Voici un JSON de l'objet :

```
{
        "id": "card_1CboP4CLud4t5fBlZMiVrzBq",
        "object": "card",
        "address_city": null,
        "address_country": null,
        "address_line1": null,
        "address_line1_check": null,
        "address_line2": null,
        "address_state": null,
        "address_zip": null,
        "address_zip_check": null,
        "brand": "Visa",
        "country": "US",
        "customer": "cus_D1s9PQgvr6U46j",
        "cvc_check": "pass",
        "dynamic_last4": null,
        "exp_month": 4,
        "exp_year": 2024,
        "fingerprint": "soMjdt25OvcMcObY",
        "funding": "credit",
        "last4": "4242",
        "metadata": {},
        "name": null,
        "tokenization_method": null
      }
```

### Objet Client

Commençons par la checklist à nouveau.

<!DOCTYPE html>
    <html>
	<body>
	   <table>
	  <thead>
	    <tr>
	      <th>Clé</th>
	      <th>Valeur</th>
	    </tr>
	  </thead>
	  <tfoot>
	    <tr>
	      <td>subscriptions</td>
	      <td>la liste des abonnements</td>
	    </tr>
	  </tfoot>
	  <tbody>
	    <tr>
	      <td>id</td>
	      <td>identifiant stripe du client</td>
	    </tr>
	    <tr>
	      <td>default_source</td>
	      <td>stripe_id de la carte par défaut</td>
	    </tr>
          <tr>
	      <td>sources</td>
	      <td>liste des sources</td>
	    </tr>
	  </tbody>
	</table>
	</body>
   </html>

L'objet client stocke les méthodes de paiement, y compris celle par défaut. Et contient des informations sur les utilisateurs et leurs abonnements.

Il rappelle également les cartes de crédit des utilisateurs et la méthode de paiement principale définie. Vous pouvez facturer les utilisateurs manuellement sur la base de ces données.

Même chose pour les abonnements – Stripe les gère et prélève les frais automatiquement.

```
{
  "id": "cus_D1s9PQgvr6U46j",
  "object": "customer",
  "account_balance": 0,
  "created": 1528717303,
  "currency": null,
  "default_source": "card_1CboP4CLud4t5fBlZMiVrzBq",
  "delinquent": false,
  "description": null,
  "discount": null,
  "email": null,
  "invoice_prefix": "4A178DE",
  "livemode": false,
  "metadata": {},
  "shipping": null,
  "sources": {
    "object": "list",
    "data": [
      {
        "id": "card_1CboP4CLud4t5fBlZMiVrzBq",
        "object": "card",
        "address_city": null,
        "address_country": null,
        "address_line1": null,
        "address_line1_check": null,
        "address_line2": null,
        "address_state": null,
        "address_zip": null,
        "address_zip_check": null,
        "brand": "Visa",
        "country": "US",
        "customer": "cus_D1s9PQgvr6U46j",
        "cvc_check": "pass",
        "dynamic_last4": null,
        "exp_month": 4,
        "exp_year": 2024,
        "fingerprint": "soMjdt25OvcMcObY",
        "funding": "credit",
        "last4": "4242",
        "metadata": {},
        "name": null,
        "tokenization_method": null
      },
      {
        "id": "card_1CcC3uCLud4t5fBlW2UMknUW",
        "object": "card",
        "address_city": null,
        "address_country": null,
        "address_line1": null,
        "address_line1_check": null,
        "address_line2": null,
        "address_state": null,
        "address_zip": null,
        "address_zip_check": null,
        "brand": "Visa",
        "country": "US",
        "customer": "cus_D1s9PQgvr6U46j",
        "cvc_check": "pass",
        "dynamic_last4": null,
        "exp_month": 4,
        "exp_year": 2024,
        "fingerprint": "soMjdt25OvcMcObY",
        "funding": "credit",
        "last4": "4242",
        "metadata": {},
        "name": null,
        "tokenization_method": null
      }
    ],
    "has_more": false,
    "total_count": 2,
    "url": "/v1/customers/cus_D1s9PQgvr6U46j/sources"
  },
  "subscriptions": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/customers/cus_D1s9PQgvr6U46j/subscriptions"
  }
}
```

### Objet Charge

Checklist pour l'objet charge :

<!DOCTYPE html>
    <html>
	<body>
	   <table>
	  <thead>
	    <tr>
	      <th>Clé</th>
	      <th>Valeur</th>
	    </tr>
	  </thead>
	  <tfoot>
	    <tr>
	      <td>destination</td>
	      <td>compte stripe du bénéficiaire</td>
	    </tr>
	  </tfoot>
	  <tbody>
	    <tr>
	      <td>id</td>
	      <td>stripe_id de la charge</td>
	    </tr>
	    <tr>
	      <td>amount</td>
	      <td>montant du paiement en cents</td>
	    </tr>
          <tr>
	      <td>amount_refunded</td>
	      <td>montant remboursé en cents</td>
	    </tr>
          <tr>
	      <td>customer</td>
	      <td>customer_id du payeur</td>
	    </tr>
          <tr>
	      <td>captured</td>
	      <td>true - paiement effectué, false - autorisé</td>
	    </tr>
	  </tbody>
	</table>
	</body>
   </html>

* **amount** – vous devez toujours vérifier quel montant a été facturé pendant le processus de test. Il peut être en cents, en euro cents, etc.
* **amount_refunded** – ce champ a une valeur différente de zéro si le montant total de la transaction (ou une partie de celle-ci) a été remboursé.
* **customer** – id de votre client
* **captured** – indique le statut de la transaction. L'argent peut être bloqué sur la carte de crédit de l'utilisateur ou peut être facturé.
* **destination** – la clé de destination stockera le compte Stripe de l'utilisateur auquel vous avez transféré l'argent.

```
"fingerprint": "soMjdt25OvcMcObY",
    "funding": "credit",
    "last4": "4242",
    "metadata": {},
    "name": null,
    "tokenization_method": null
  },
  "source_transfer": null,
  "statement_descriptor": null,
  "status": "succeeded",
  "transfer_group": null
}
```

**Objet Remboursement**

L'objet remboursement est intégré dans l'objet charge au cas où une partie du paiement (ou le paiement entier) est remboursé à l'acheteur.

<!DOCTYPE html>
    <html>
	<body>
	   <table>
	  <thead>
	    <tr>
	      <th>Clé</th>
	      <th>Valeur</th>
	    </tr>
	  </thead>
	  <tfoot>
	    <tr>
	      <td>status</td>
	      <td>success / pending / failed</td>
	    </tr>
	  </tfoot>
	  <tbody>
	    <tr>
	      <td>id</td>
	      <td>stripe_id du remboursement</td>
	    </tr>
	    <tr>
	      <td>amount</td>
	      <td>montant du paiement en cents</td>
	    </tr>
	  </tbody>
	</table>
	</body>
   </html>

```
{
  "id": "re_1CcY10CLud4t5fBlN23KtYq7",
  "object": "refund",
  "amount": 999,
  "balance_transaction": "txn_1CcY10CLud4t5fBlhlmzzJuK",
  "charge": "ch_1CcD7dCLud4t5fBlC1srZNIB",
  "created": 1528892634,
  "currency": "usd",
  "metadata": {},
  "reason": null,
  "receipt_number": null,
  "status": "succeeded"
}
```

**Objet Transfert**

<!DOCTYPE html>
    <html>
	<body>
	   <table>
	  <thead>
	    <tr>
	      <th>Clé</th>
	      <th>Valeur</th>
	    </tr>
	  </thead>
	  <tfoot>
	    <tr>
	      <td>reversals</td>
	      <td>liste des objets de transfert inversé</td>
	    </tr>
	  </tfoot>
	  <tbody>
	    <tr>
	      <td>id</td>
	      <td>transfer_id</td>
	    </tr>
	    <tr>
	      <td>amount</td>
	      <td>montant du paiement en cents</td>
	    </tr>
          <tr>
	      <td>destination</td>
	      <td>compte lié du bénéficiaire</td>
	    </tr>
          <tr>
	      <td>reversed</td>
	      <td>false - transaction monétaire, true - inversé</td>
	    </tr>
	  </tbody>
	</table>
	</body>
   </html>

L'objet transfert conserve les informations liées au transfert du solde de la plateforme vers d'autres comptes. Comme les paiements aux partenaires de la plateforme – les chauffeurs Uber.

Notez que toutes les transactions doivent être enregistrées dans la base de données. De cette façon, lors des tests, vous verrez l'identifiant de transfert. Allez sur Stripe et vérifiez les éléments suivants :

* **amount** – la somme payée à un bénéficiaire
* **destination** – compte Stripe de l'utilisateur qui reçoit le paiement
* **reversed** – si vous devez annuler une transaction, la clé agit comme un indicateur. Elle montre une valeur false si la transaction a réussi. True – si inversée
* **reversals** – stocke une liste d'objets au cas où une partie du transfert serait inversée

```
{
  "id": "tr_1CcApyCLud4t5fBlZyx5mEPI",
  "object": "transfer",
  "amount": 250,
  "amount_reversed": 0,
  "balance_transaction": "txn_1CcApyCLud4t5fBlfA5cgXBz",
  "created": 1528803538,
  "currency": "usd",
  "description": null,
  "destination": "acct_18bAS3KcT341ksb9",
  "destination_payment": "py_1CcApyKcT341ksb9VawxIJdS",
  "livemode": false,
  "metadata": {},
  "reversals": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/transfers/tr_1CcApyCLud4t5fBlZyx5mEPI/reversals"
  },
  "reversed": false,
  "source_transaction": null,
  "source_type": "card",
  "transfer_group": null
}
```

**Objet Transaction de Solde**

<!DOCTYPE html>
    <html>
	<body>
	   <table>
	  <thead>
	    <tr>
	      <th>Clé</th>
	      <th>Valeur</th>
	    </tr>
	  </thead>
	  <tfoot>
	    <tr>
	      <td>type</td>
	      <td>type de transaction (charge, remboursement, transfert)</td>
	    </tr>
	  </tfoot>
	  <tbody>
	    <tr>
	      <td>id</td>
	      <td>stripe_id du remboursement</td>
	    </tr>
	    <tr>
	      <td>amount</td>
	      <td>montant du paiement en cents (faites attention aux signes +/-)</td>
	    </tr>
          <tr>
	      <td>available_on</td>
	      <td>date à laquelle l'argent sera disponible pour un bénéficiaire</td>
	    </tr>
          <tr>
	      <td>fee</td>
	      <td>montant des frais de Stripe</td>
	    </tr>
          <tr>
	      <td>fee_details</td>
	      <td>liste des objets de frais</td>
	    </tr>
          <tr>
	      <td>net</td>
	      <td>montant du revenu/dépense net</td>
	    </tr>
          <tr>
	      <td>status</td>
	      <td>statut actuel de l'opération</td>
	    </tr>
	  </tbody>
	</table>
	</body>
   </html>

L'objet stocke les données sur tout changement du solde de l'application. Vous n'avez pas réellement besoin de tester cet objet. Il est plutôt pour comprendre d'où viennent les frais.

* **amount** – montant du paiement en cents
* **available_on** – l'argent envoyé aux partenaires sera disponible pour eux à temps, et cette clé indique quand exactement
* **fee** – montant des frais de Stripe
* **fee_details** – liste des objets de frais avec une description de pourquoi les frais ont été facturés
* **net** – montant du revenu net
* **status** – le statut de succès de l'opération
* **type** – type de l'objet (charge, remboursement, transfert)

Exemple de code de transaction de solde pour un transfert :

```
{
  "id": "txn_1CcApyCLud4t5fBlfA5cgXBz",
  "object": "balance_transaction",
  "amount": -250,
  "available_on": 1528803538,
  "created": 1528803538,
  "currency": "usd",
  "description": null,
  "exchange_rate": null,
  "fee": 0,
  "fee_details": [],
  "net": -250,
  "source": "tr_1CcApyCLud4t5fBlZyx5mEPI",
  "status": "available",
  "type": "transfer"
}
```

Exemple de code de transaction de solde pour une charge :

```
{
  "id": "txn_1CbrRTCLud4t5fBlhRfMLdq1",
  "object": "balance_transaction",
  "amount": 10000,
  "available_on": 1529280000,
  "created": 1528728983,
  "currency": "usd",
  "description": "Charge user asdf11@example.com for instructor sodom@example.com lesson id: 77",
  "exchange_rate": null,
  "fee": 320,
  "fee_details": [
    {
      "amount": 320,
      "application": null,
      "currency": "usd",
      "description": "Stripe processing fees",
      "type": "stripe_fee"
    }
  ],
  "net": 9680,
  "source": "ch_1CbrP3CLud4t5fBlztHMxVzv",
  "status": "pending",
  "type": "charge"
}
```

**Objet Abonnement**

<!DOCTYPE html>
    <html>
	<body>
	   <table>
	  <thead>
	    <tr>
	      <th>Clé</th>
	      <th>Valeur</th>
	    </tr>
	  </thead>
	  <tfoot>
	    <tr>
	      <td>plan</td>
	      <td>règles pour l'abonnement : montant, intervalle, jours d'essai</td>
	    </tr>
	  </tfoot>
	  <tbody>
	    <tr>
	      <td>id</td>
	      <td>stripe_id de l'abonnement</td>
	    </tr>
	    <tr>
	      <td>application_fee_percent</td>
	      <td>% facturé pour l'abonnement</td>
	    </tr>
          <tr>
	      <td>billing</td>
	      <td>charge automatique ou envoi de facture</td>
	    </tr>
          <tr>
	      <td>billing_cycle_anchor</td>
	      <td>heure du prochain cycle de l'abonnement</td>
	    </tr>
          <tr>
	      <td>current_period_start current_period_end</td>
	      <td>périodes de temps de la période d'abonnement actuelle</td>
	    </tr>
	  </tbody>
	</table>
	</body>
   </html>

* **application_fee_percent** – pourcentage du montant total que l'application facture, le reste est payé par le propriétaire du contenu
* **billing** – responsable de la manière dont le processus de facturation se déroule – automatiquement ou manuellement (via la facture)
* **billing_cycle_anchor** – contient la date d'échéance du prochain paiement pour le renouvellement de l'abonnement
* **current_period_start & current_period_end** – période de validité de l'abonnement du client
* **plan** – stocke l'objet d'un plan d'abonnement, inclut un ensemble de règles (montant à payer, intervalle, nombre de jours d'essai, et plus)

```
{
  "id": "sub_D2JskPBqcW24hu",
  "object": "subscription",
  "application_fee_percent": null,
  "billing": "charge_automatically",
  "billing_cycle_anchor": 1528820423,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "created": 1528820423,
  "current_period_end": 1531412423,
  "current_period_start": 1528820423,
  "customer": "cus_D2Jsi3JgT5zPh1",
  "days_until_due": null,
  "discount": null,
  "ended_at": null,
  "items": {
    "object": "list",
    "data": [
      {
        "id": "si_D2Js7N4mYxzAaY",
        "object": "subscription_item",
        "created": 1528820424,
        "metadata": {
        },
        "plan": {
          "id": "ivory-express-917",
          "object": "plan",
          "active": true,
          "aggregate_usage": null,
          "amount": 999,
          "billing_scheme": "per_unit",
          "created": 1528819224,
          "currency": "usd",
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {
          },
          "name": "Ivory Express",
          "nickname": null,
          "product": "prod_D2JYysdjdQ2gwT",
          "statement_descriptor": null,
          "tiers": null,
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "quantity": 1,
        "subscription": "sub_D2JskPBqcW24hu"
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/subscription_items?subscription=sub_D2JskPBqcW24hu"
  },
  "livemode": false,
  "metadata": {
  },
  "plan": {
    "id": "ivory-express-917",
    "object": "plan",
    "active": true,
    "aggregate_usage": null,
    "amount": 999,
    "billing_scheme": "per_unit",
    "created": 1528819224,
    "currency": "usd",
    "interval": "month",
    "interval_count": 1,
    "livemode": false,
    "metadata": {
    },
    "name": "Ivory Express",
    "nickname": null,
    "product": "prod_D2JYysdjdQ2gwT",
    "statement_descriptor": null,
    "tiers": null,
    "tiers_mode": null,
    "transform_usage": null,
    "trial_period_days": null,
    "usage_type": "licensed"
  },
  "quantity": 1,
  "start": 1528820423,
  "status": "active",
  "tax_percent": null,
  "trial_end": null,
  "trial_start": null
}
```

## Cas d'utilisation

Enfin, nous passons aux cas d'utilisation. Alors découvrons comment nous construisons la logique métier en utilisant Stripe.

### Abonnements

**Cas** : Les utilisateurs paient 5 $/mois pour obtenir l'accès au contenu. Son auteur gagne 80 % du coût total. Les clients ont cinq jours d'essai.

**Comment faire fonctionner** :

1. Créez le plan d'abonnement dans Stripe, spécifiez le coût, le % des frais de l'application, et l'intervalle.
2. Intégrez les webhooks pour que le serveur comprenne quand quelqu'un s'abonne et quand ils sont facturés.
3. Intégrez les emails pour envoyer aux utilisateurs des factures/reçus.
4. Lorsqu'un utilisateur achète l'abonnement, Stripe compte cinq jours à partir de ce moment et fait ensuite la charge.
5. L'auteur reçoit de l'argent, la plateforme reçoit ses frais.

**Frais** : 2,9 % + 30 cents

### Achat de contenu

**Cas** : Les utilisateurs achètent du contenu sur un site web ou une application mobile.

**Comment faire fonctionner** :

1. Le client tokenise une carte.
2. Le backend fait la Charge.
3. Si la Charge est réussie, la logique métier de la plateforme permet au client d'obtenir le contenu.

**Frais** : 2,9 % de la charge + 30 cents.

### Plateforme à la demande (Uber)

**Cas** : Le client paie pour le trajet, la plateforme prélève 20 %, le chauffeur reçoit 80 %.

**Préconditions** :

* Le chauffeur a lié un compte
* L'utilisateur a ajouté une carte

Dans ce cas, vous devez créer des transferts vous-même après que le passager a complété le paiement.

Tout d'abord, autorisez le paiement lorsqu'ils réservent le trajet et capturez-le lorsque le trajet est terminé.

Ensuite, créez un transfert pour le chauffeur – 80 % de la somme totale. Payez les frais de Stripe, et le reste sera le revenu net.

**Et les frais sont** : 2,9 % + 30 cents

### Plateforme à la demande #2

Les applications de type Uber sont parfaites pour montrer comment Stripe fonctionne. Alors voici un autre cas d'utilisation.

**Cas** : Le client paie pour le service, la plateforme prélève 20 %, le chauffeur reçoit 80 %. Plus, le chauffeur peut payer 5 $ pour le droit de réservation prioritaire.

Fonctionne si le chauffeur a lié son compte, et le passager a ajouté une carte de crédit.

* **Variante #1.** Vous prélevez 5 $ du chauffeur (en cas d'option prioritaire), autorisez le paiement pour le client, faites la capture lorsque le trajet se termine, faites un transfert pour le chauffeur. Et gardez le reste. Dans ce cas, vous payez 2,9 % de frais + 30 centimes pour chaque charge.
* **Variante #2.** Vous pouvez sauter les frais en créant la monétisation interne sur votre plateforme. Lorsque vous recevez de l'argent du client, vous calculez la part du chauffeur et transférez ces fonds au solde interne.

![Image](https://lh4.googleusercontent.com/PTXyrViF0NXh83Ej8kGdol0jENOP65cgCV3MBcodPJhr6KZ4vsoCOfa9CTQCCRwKdNYG5S9Wh-i3Jdq41SAs6JJxvPAiP-zs16dXNhdbVIsLwZMG6_VaNKt28_2VC_CY73Qku5jo)
_Flux de trésorerie_

## En conclusion

Comme vous le voyez, la mise en œuvre de la logique de paiement et son test ne sont pas aussi difficiles qu'ils en ont l'air. Tout ce que vous avez à faire est de gérer les objets Stripe de la bonne manière. Et de comprendre comment utiliser Stripe sur votre plateforme.

J'espère que ce guide vous sera utile lorsque vous commencerez à concevoir la logique de paiement basée sur Stripe et son test.