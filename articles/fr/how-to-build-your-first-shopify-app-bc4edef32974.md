---
title: Comment créer votre première application Shopify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-01T19:25:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-first-shopify-app-bc4edef32974
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5rTl2RMivof-SHDDYPsN6A.jpeg
tags:
- name: ecommerce
  slug: ecommerce
- name: React
  slug: react
- name: Ruby on Rails
  slug: ruby-on-rails
- name: shopify
  slug: shopify
- name: technology
  slug: technology
seo_title: Comment créer votre première application Shopify
seo_desc: 'By Igor Petrov

  Why build a Shopify App?

  I have always been excited about how the e-commerce market is growing, and have
  made various attempts to dive into this world. About five years ago, a partner and
  I built an e-commerce website selling and deliv...'
---

Par Igor Petrov

### Pourquoi créer une application Shopify ?

J'ai toujours été passionné par la croissance du marché du e-commerce et j'ai fait diverses tentatives pour plonger dans ce monde. Il y a environ cinq ans, un partenaire et moi avons créé un site de e-commerce vendant et livrant des fleurs, une peluche et une carte de vœux emballées ensemble en cadeau. C'était une tentative de validation d'idée, et nous ne l'avons pas pris au sérieux. Donc, cela s'est terminé rapidement.

Plus tard, nous avons essayé de vendre des carrelages (en partenariat avec un homme qui avait travaillé dans ce domaine pendant plusieurs années), et cela n'a pas bien fonctionné non plus. Principalement, la raison était la même : c'était un projet secondaire pour nous, et nous ne connaissions rien du marché des carrelages.

Mais, pendant cette période, nous avons développé de nombreux sites de e-commerce pour les clients de notre agence. La plupart de ces sites ont été construits en utilisant **Ruby on Rails** et spécifiquement **Spree**. Et cette direction a été réussie — nous avons appris beaucoup sur le développement de sites de e-commerce et les problèmes de développement typiques (ainsi que le marketing, la livraison et différents problèmes commerciaux).

Cette année, je travaille avec un nouveau partenaire qui avait une bonne expérience avec la plateforme **Shopify**. Nous avons beaucoup parlé et avons eu l'idée de développer une [application **Shopify**](https://apps.shopify.com/influencify). Cette plateforme se développe rapidement, et il y a une forte demande sur le marché pour étendre les possibilités de la plateforme.

Créer un produit, plutôt que de faire du développement sur mesure pour quelqu'un, était également excitant pour moi. Ainsi, ces deux choses — le e-commerce et le développement de produits — se sont naturellement combinées en l'idée d'une [application **Shopify**](https://apps.shopify.com/influencify).

### Comprendre la complexité de la création d'une application

Vous avez donc une idée pour votre application. Maintenant, vous devez décider si votre application interagira avec les vitrines des marchands en étendant les modèles ou en injectant des scripts. Ou peut-être devez-vous travailler avec une API tierce et l'intégrer dans votre application, ou étendre l'**Admin Shopify**.

Chaque partie peut être suffisamment complexe. Donc, si vous devez simplement faire quelque chose avec les données du magasin **Shopify** et afficher quelque chose dans la section Admin, vous traitez avec 1 type ou 1 point de complexité. Si vous devez travailler avec des API externes et avoir toujours une section dans Admin, vous avez 2 points de complexité. Et ainsi de suite.

### Commencer le développement avec un modèle de base

Eh bien, nous pouvons voir que notre application est assez complexe (bien que pour les clients, elle semble simple). Puisque nous nous sommes mis d'accord sur l'idée de l'application et le **MVP** initial, j'ai commencé à faire des recherches et j'ai découvert que **Shopify** dispose d'un excellent gem `shopify_app` **Ruby**.

C'est un outil assez cool qui vous fait gagner beaucoup de temps : il génère pour vous un framework d'application **Shopify** sans avoir besoin de configurer manuellement le flux **OAuth**. Autres points à noter :

* Modèle Shop généré
* Webhooks et ScriptTags simples à enregistrer
* Approches d'authentification
* Vérification de l'App Proxy (pour vos personnalisations de vitrine)

J'ai lancé une application vide en quelques minutes, pas en heures.

### Utiliser les outils recommandés

Ensuite, j'ai recherché comment aborder l'UI Admin dans votre application. J'ai découvert que **Shopify** simplifie également cette tâche grâce à la puissance de leur framework de design [**Shopify Polaris**](https://polaris.shopify.com/).

[**Polaris**](https://polaris.shopify.com/) est une bibliothèque de composants **React.js**, et c'est la méthode recommandée pour étendre la section Admin **Shopify**. Votre application ressemblera à une application native **Shopify** avec des sections d'administration comme « Produits » ou « Commandes » (**Shopify** l'utilise également, je suppose).

Vous devriez l'utiliser plutôt qu'un thème personnalisé, car il est bien documenté, supporté et dispose de directives.

### Étendre Shopify Admin

Après une installation réussie de **Shopify Polaris** dans le projet avec l'aide de **Webpacker** ou **Yarn**, vous pourrez étendre la section Admin **Shopify**.

Pour la page d'accueil (celle que les marchands verront après l'installation de l'application sans données configurées), vous ferez ces choses :

* Ajouter une route :

```
get 'welcome' => 'home#index'
```

* Créer un contrôleur **Rails** :

```
class HomeController < BaseAuthenticatedController
  def index
  end
end
```

* Ajouter un modèle de vue qui rend simplement un composant **React** avec l'aide du gem `react-rails` :

```
# home/index.html.erb
<%= react_component("Welcome", {  apiKey: ShopifyApp.configuration.api_key,  shopOrigin: "https://#{ @shop_session&.url }",  debug: Rails.env.development?,  forceRedirect: !Rails.env.development? && !Rails.env.test?}) %>
```

* Créer un composant **React** qui rend certains composants **Shopify Polaris** (comme `EmptyState`, par exemple).

La première étape est assez claire pour tous ceux qui ont déjà travaillé avec **Ruby on Rails**. La deuxième étape devrait l'être également, à l'exception du fait que vous devez faire hériter vos contrôleurs admin de `ShopifyApp::AuthenticatedController` pour que chaque requête soit autorisée. J'ai créé une sous-classe de cette classe pour toutes les futures classes de contrôleurs admin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2BYWJpAZHNIzSgtICBCQFA.png)

La troisième étape concerne le rendu. J'ai installé le gem `react-rails` qui vient avec un helper `react_component` pratique, et j'ai ajouté un rendu d'un composant de bienvenue en passant toutes les propriétés nécessaires. Pour les applications embarquées (celles qui étendent **Shopify** Admin), vous devez passer au moins les options `apiKey` et `shopOrigin` pour utiliser les [composants embarqués](https://polaris.shopify.com/components/get-started#using-embedded-components) fournis avec **Shopify Polaris**. Ces [composants embarqués](https://polaris.shopify.com/components/get-started#using-embedded-components) sont simplement des wrappers **React** autour du SDK d'application embarquée **Shopify**.

Et enfin, j'ai écrit un composant `Welcome` et je l'ai placé dans le dossier `app/javascript/components` selon `config/webpacker.yml`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HL9JrMwbbqMo_i81DxJmMw.png)

Notez que j'ai extrait une partie du code standard, comme la définition des propriétés `shopOrigin` et `apiKey`, dans le composant `BasePage` qui sera un composant parent pour chaque page de l'application. `InfluencifyApp` est un composant qui rend le composant `AppProvider` Polaris, `Page`, à l'intérieur, et tout enfant avec `{this.props.children}` à l'intérieur de `Page`.

Avec cette configuration, j'ai créé d'autres composants avec `InfluencifyApp` comme composant racine pour chaque page de l'application.

### Personnalisation de la vitrine

Il y a une bonne option dans **Shopify** qui vous permet de personnaliser les vitrines des marchands : les balises de script. Ce sont des fichiers JavaScript qui seront injectés dans le modèle de la vitrine.

Vous pouvez les enregistrer facilement en utilisant le gem `shopify_app`. Voici comment j'ai enregistré un script pour l'application [Influencify](https://apps.shopify.com/influencify) (dans `config/initializers/shopify_app.rb`) :

```
# pour inclure l'assistant asset_url
include ActionView::Helpers::AssetUrlHelper
...
config.scripttags = [
    {event: 'onload', src: -> (domain) { asset_url('influencify.js', host: ENV['APP_DOMAIN']) } }
]
```

Notez que vos scripts doivent être accessibles publiquement pour tous les marchands sur l'ensemble de vos déploiements. Je veux dire en termes de Rails, vous ne devriez pas avoir de digest dans le nom de fichier de votre script comme `influencify-dd432js....js`, mais plutôt, mettre la version compilée dans un dossier `public` ou la télécharger sur un CDN.

La deuxième option est que vous pouvez avoir des pages entières ou des parties de pages servies par votre application. C'est-à-dire, au cas où vous devez afficher quelque chose ou récupérer des données de votre script injecté, vous pouvez enregistrer quelles URLs pour les marchands seront servies par votre application. Cette fonctionnalité est connue sous le nom de [Application Proxies](https://help.shopify.com/en/api/guides/application-proxies). Encore une fois, pour implémenter cela dans votre application, c'est beaucoup plus facile avec l'aide du gem `shopify_app` — suivez simplement leurs [guides](https://github.com/Shopify/shopify_app#app-proxy-controller-generator).

### Test

Tester une application **Shopify** peut être un peu délicat, mais c'est familier pour quiconque a déjà travaillé avec des API tierces et testé via des outils comme `localtunnel` ou `ngrok`. Donc, chaque fois que vous allez tester votre application, lancez simplement votre outil de tunneling préféré et mettez à jour le champ « URL(s) de redirection autorisées » sur la page des paramètres de votre application avec une URL vers votre callback d'authentification qui ressemble à ceci : `[https://myapp.localtunnel.me/auth/shopify/callback](https://myapp.localtunnel.me/auth/shopify/callback)`.

Pour tester vos points de terminaison App Proxies pour les personnalisations de vitrine, vous devez également mettre à jour ce paramètre d'URL sous la section « Extensions ».

Bien sûr, pour tester une application, vous avez également besoin d'un magasin de développement de test.

### Déploiement

Il n'y a rien de spécial concernant le déploiement, puisque ce n'est qu'une application **Ruby on Rails** régulière. J'ai déployé mon application sur la plateforme **Heroku** avec les processus **Puma** et **Sidekiq** spécifiés via le Procfile.

De plus, vous devez définir les variables d'environnement que vous allez utiliser dans votre application via `ENV['SOMETHING']`.

Une autre chose à noter est que j'ai ajouté un **Node.js** buildpack, car j'avais des problèmes avec la construction via **Webpack** :

```
git:(master) heroku buildpacks     === influencify Buildpack URLs1. https://github.com/heroku/heroku-buildpack-ruby2. https://github.com/heroku/heroku-buildpack-nodejs
```

### Aller plus loin

Eh bien, comme vous pouvez le voir, construire une application de la manière recommandée par **Shopify** comprend de nombreuses étapes différentes, et cela peut s'avérer être une tâche complexe pour un développeur non expérimenté.

Bien sûr, construire une application n'est que la partie émergée de l'iceberg. Les prochaines étapes dans une aventure de création d'application **Shopify** sont la création de bons matériaux promotionnels, sa soumission à l'App Store, le marketing et le support client/développement après son approbation.

*Si vous avez aimé cet article, cliquez sur* 👋 *pour le partager.*