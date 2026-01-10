---
title: J'ai découvert une API qui vous aide à expédier des produits e-commerce via
  plusieurs services de livraison.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-25T18:00:35.000Z'
originalURL: https://freecodecamp.org/news/check-out-this-api-that-helps-you-ship-ecommerce-products-through-multiple-mail-services-725bcd9ce6f8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZtB3bSD2qOkRT3xJ_5gDQg.jpeg
tags:
- name: api
  slug: api
- name: ecommerce
  slug: ecommerce
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
seo_title: J'ai découvert une API qui vous aide à expédier des produits e-commerce
  via plusieurs services de livraison.
seo_desc: 'By Igor Petrov

  The past few months have been super busy time: I’ve worked on development for different
  e-commerce projects, joined a startup, and co-organized another one — all while
  preparing for an ultra-marathon.

  It so happened that I was working ...'
---

Par Igor Petrov

Les derniers mois ont été une période très chargée : j'ai travaillé sur le développement de différents projets e-commerce, rejoint une startup et co-organisé une autre — tout en me préparant pour un ultra-marathon.

Il se trouve que je travaillais sur des projets e-commerce qui avaient besoin de fonctionnalités d'expédition. Ces projets avaient déjà été démarrés par quelqu'un d'autre (et non écrits par moi à partir de zéro) et ils avaient le service d'expédition **Shippo** intégré. C'est ainsi que j'ai rencontré Shippo et commencé à travailler avec.

Je ne sais pas si Shippo est la seule option pour les fonctionnalités d'expédition dans les applications web, mais il est assez populaire et dispose d'une API assez bonne et simple. Dans cet article, nous allons aborder plusieurs tâches courantes que vous pourriez avoir à résoudre avec ce service, ainsi qu'avec **Ruby**.

#### Commencer avec Shippo

Ce dont vous avez besoin en premier, c'est d'un compte Shippo et de la gemme `shippo` intégrée à votre projet :

```
gem 'shippo', git: 'https://github.com/goshippo/shippo-ruby-client'
```

Ensuite, vous devez le configurer avec le jeton API que vous devriez avoir (Shippo vous fournit des jetons `test` ou `live`). Il suffit de mettre ceci dans `config/initializers/shippo.rb` :

```
Shippo::api_token = ENV['shippo_api_token']
```

Pour travailler avec `ENV`, vous pourriez utiliser quelque chose comme `dotenv` ou `figaro` ou **Heroku**.

#### Validation des adresses

Une fonctionnalité intéressante de Shippo est de permettre la validation des adresses. Supposons que vous avez des champs d'adresse dans les profils des utilisateurs de votre application, et que vous devez valider lors de l'inscription si l'adresse de l'utilisateur est correcte. Je suis arrivé à une solution de validateur personnalisé :

```
class Profile < ApplicationRecord  validates_with ProfileAddressValidatorend
```

Et le code du validateur utilisant l'API `Shippo::Address` ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/QWMwFwVvJpJR8lyD1d1yf6tmIPidmnfQfqEd)

#### Création d'un envoi/récupération des tarifs

La prochaine tâche populaire est de créer un envoi en deux étapes. Tout d'abord, vous allez récupérer les tarifs d'expédition de différents transporteurs (que vous avez configurés dans Shippo) et les montrer à vos utilisateurs afin qu'ils puissent en choisir un. Ensuite, en fonction du choix de l'utilisateur, vous créerez une transaction (étiquette d'expédition).

Vous pouvez également offrir une interface utilisateur pour modifier les tailles des colis ou simplement permettre aux utilisateurs de choisir parmi des colis/boîtes prédéfinis.

Notre première étape pourrait ressembler à ceci :

```
Shippo::Shipment.create(  address_from: @address_from,  address_to: ADDRESS_TO,  parcels: parcels,  async: false)
```

Au cas où vous enveloppez ceci dans un objet de service, `@address_from` est quelque chose que vous voulez passer dedans. Cela devrait être comme ceci (le même _Hash_ pour `ADDRESS_TO` qui pourrait être une constante, au cas où vos utilisateurs n'envoient qu'à une seule adresse) :

```
{    :name => 'Apple',    :street1 => 'One Apple Park Way',    :city => 'Cupertino',    :state => 'CA',    :zip => '95014',    :country => 'US',    :phone => '+1 (408) 996–1010',    :email => 'tim@apple.com'  }
```

Et enfin, `parcels` est un tableau de telles structures :

```
{  length: 10, # ou quelque chose provenant des paramètres  width: 10,  height: 10,  distance_unit: :in,  weight: 3,  mass_unit: :lb,}
```

Après avoir passé toutes ces données et appelé `Shippo::Shipment.create`, vous devriez obtenir un objet d'expédition qui contient un attribut `rates` (`shipment.rates`).

#### Créer une étiquette d'expédition (transaction) basée sur le tarif sélectionné

Nous avons un tarif sélectionné par l'utilisateur, et nous l'avons instancié (disons dans un contrôleur) dans `@selected_shipping_rate`. Maintenant, il suffit de faire ceci :

```
transaction = Shippo::Transaction.create(  rate: @selected_shipping_rate['object_id'],  label_file_type: "PDF",  metadata: @ticket.token.to_s, # passez toute donnée supplémentaire si nécessaire  async: false)
```

Vous devez confirmer si cela a réussi ou non en vérifiant `transaction["status"]`. Cela devrait être `SUCCESS` ou quelque chose parmi les [statuts disponibles](https://goshippo.com/docs/reference/rb#transactions). Vous pourriez également être intéressé par `transaction["tracking_number"]` et `transaction["label_url"]` (l'URL du fichier PDF de l'étiquette d'expédition).

#### Création d'étiquette en un seul appel

Vous pourriez vouloir créer une étiquette d'expédition avec un seul appel à l'API Shippo. Eh bien, vous pouvez le faire ! Dans ce cas, vous utiliserez un transporteur d'expédition concret, comme **FedEx**.

Ainsi, cet appel à l'API ressemble à une combinaison des deux appels que nous avons faits précédemment : `carrier_account` est un identifiant d'objet de transporteur — vous pouvez l'obtenir avec [https://goshippo.com/docs/reference/rb#carrier-accounts-list](https://goshippo.com/docs/reference/rb#carrier-accounts-list) — et `servicelevel_token` est un jeton correspondant de cette [énumération des niveaux de service](https://goshippo.com/docs/reference/rb#servicelevels) :

![Image](https://cdn-media-1.freecodecamp.org/images/NlEl3YWnWQr6vHkj493AFNxoYxua6G5yShUW)

#### Paramètres des transporteurs

Pour les transporteurs fonctionnels, vous devez passer toutes les données requises. Cela dépend du fournisseur d'expédition concret. Shippo dispose d'une très bonne page de description [page](https://goshippo.com/docs/carriers) sur ce qui est nécessaire. Par exemple, pour configurer FedEx, vous devez obtenir d'eux au moins le `numéro de compteur` et le `numéro de compte`.

**Une chose délicate à propos de FedEx** : leur serveur de test n'est pas très stable (et ce fait a été confirmé par le support de Shippo). Ainsi, parfois vous pourrez créer des expéditions et demander des tarifs, mais parfois vous obtiendrez cette réponse : « L'API FedEx n'a pas répondu. Veuillez réessayer dans quelques minutes. »

#### Suivi des expéditions

Et enfin, vous pourriez vouloir être comme un « grand frère » qui surveille vos expéditions 😊 Alors vous devez commencer à suivre les expéditions afin de savoir quand elles ont réellement été envoyées et livrées.

Shippo dispose d'une API `Shippo::Track` à cet effet, ainsi que des webhooks que vous pouvez recevoir via HTTP. Tout d'abord, vous devez enregistrer que vous allez suivre une certaine expédition.

![Image](https://cdn-media-1.freecodecamp.org/images/MPyP80JfgdQENozndN6QBqAocfSS7YnAEiP7)

`@shipping_label` est notre propre objet que nous stockons dans la base de données : nous l'avons sauvegardé après la création réussie de la transaction Shippo (étiquette d'expédition).

Deuxièmement, vous devez avoir un gestionnaire de webhooks : en termes de Rails, vous devez ajouter une route et un contrôleur.

Shippo vous enverra alors des données sur les mises à jour de l'état de suivi, afin que vous puissiez mettre à jour les informations d'état dans la base de données et avoir tout en synchronisation.

```
# Webhook Shippo dans routes.rbpost '/shippo_webhook' => 'shippo#track_shipment'
```

![Image](https://cdn-media-1.freecodecamp.org/images/R0l88xDYcJoRXr8X4KHgU91DXPNEjaPLEsCU)

N'oubliez pas de tester cela en développement avec votre outil de tunnellisation de développement préféré comme `ngrok` ou `localtunnel`. Et bien sûr, vous devez vous connecter à votre compte Shippo et spécifier l'URL qui recevra les webhooks et quels types de webhooks ils sont.

### Conclusion

Shippo est une excellente solution pour presque tout ce dont vous avez besoin en matière de capacités d'expédition dans votre application. C'est pourquoi je le choisirais pour mon prochain projet.

S'il y a quelque chose de compétitif sur le marché, faites-le moi savoir dans les commentaires. J'adorerais entendre parler de quelque chose de vraiment cool pour les tâches d'expédition.

*Si vous avez aimé cet article, cliquez sur* 👋 *pour le partager.*