---
title: Construire une application multi-tenant est facile… si vous avez un appartement
  !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T16:17:55.000Z'
originalURL: https://freecodecamp.org/news/building-a-multi-tenant-app-is-easy-if-you-have-an-apartment-3465f6eda85b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WXq8WqcR24xYG9PlOdwktw.jpeg
tags:
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: SaaS
  slug: saas
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Construire une application multi-tenant est facile… si vous avez un appartement
  !
seo_desc: 'By Igor Petrov

  These days, more and more startups are appearing on the SaaS market. For their apps,
  they have several development approaches to choose from. And one of the technical
  models is the multi-tenancy or multi-tenant app. If you’re going to ...'
---

Par Igor Petrov

De nos jours, de plus en plus de startups apparaissent sur le marché du _SaaS_. Pour leurs applications, elles ont le choix entre plusieurs approches de développement. L'un des modèles techniques est l'application _multi-tenancy_ ou _multi-tenant_. Si vous prévoyez de partager l'ensemble de votre logiciel avec vos clients de startup — que ce soit avec la possibilité d'avoir des données/contenus et des URL séparés (disons, le _SaaS_), ou juste une partie — vous avez besoin d'une application _multi-tenant_.

Ce n'est pas le seul choix : je devrais mentionner d'autres approches, mais contentons-nous de les citer — une comparaison des différentes approches pourrait être un bon sujet pour le prochain article.

Voici ma liste (ordonnée par complexité d'implémentation) :

* _SaaS_ basé sur le chemin d'URL. Le plus simple. Domaine unique, base de données unique, etc. Restrictions des données au niveau de l'application.
* _SaaS_ multi-tenant. Complexité moyenne. Basé sur des sous-domaines ou des domaines. Plusieurs bases de données ou schémas. Restrictions des données au niveau de la base de données.
* _SaaS_ basé sur la virtualisation (merci à _Docker_ et ses amis !). Haut niveau de complexité. Basé sur des sous-domaines/domaines. Plusieurs copies d'applications et de bases de données. Restrictions des données au niveau de la virtualisation.

### Multi-tenancy

Alors, qu'est-ce que la _multi-tenancy_ ? La _multi-tenancy_ est une approche d'architecture de développement logiciel dans laquelle chaque client obtient sa propre configuration d'application et ses propres données (isolées de manière stricte ou souple des autres clients). Chaque « instance » est appelée un « _tenant_ ».

Au cours des dernières années, j'ai travaillé sur plusieurs applications multi-tenant (j'ai principalement fait de la _multi-tenancy_ à partir de zéro). Et même maintenant, je travaille sur deux applications _multi-tenant_.

Passons de l'introduction et de la théorie à la pratique, et regardons ce qui pourrait être utilisé pour les applications _multi-tenant_ dans le monde de _Ruby on Rails_.

### Apartment

C'est le numéro un pour les applications _Ruby on Rails_. Ajoutons-le au _Gemfile_ :

```
gem ‘apartment’
```

Après `bundle install`, vous devez exécuter un générateur afin d'obtenir des modèles de configuration de base :

```
bundle exec rails generate apartment:install
```

Vous avez maintenant `config/initializers/apartment.rb` où vous pouvez ajuster la façon dont vous souhaitez utiliser _Apartment_. Les points les plus importants à configurer sont : comment « _apartment_ » saura identifier vos tenants pour le stockage des données (nous supposerons qu'il s'agit d'une base de données _PostgreSQL_ où chaque schéma _PostgreSQL_ est un tenant distinct), et comment afficher les données en fonction des requêtes _HTTP_.

Ok, dans une application que je développe, j'ai un modèle _ActiveRecord_ `Website` avec un champ `slug`. Par conséquent, le premier paramètre ressemble à ceci, et chaque site web est un _tenant_ :

```
config.tenant_names = lambda { Website.pluck(:slug) }
```

Disons que j'ai décidé de traiter n'importe quel sous-domaine comme le slug du site web. Donc, si j'ai un `Website` avec le slug `mon-super-site`, alors `mon-super-site.example.com` servira les données du schéma de base de données `mon-super-schema`. Pour avoir ce comportement, nous avons besoin de :

```
# require 'apartment/elevators/subdomain'
```

```
...Rails.application.config.middleware.use Apartment::Elevators::Subdomain
```

Le troisième paramètre dont vous pourriez avoir besoin est l'exclusion de certains modèles qui devraient être partagés entre tous les _tenants_. Comme `Website` lui-même dans mon exemple :

```
config.excluded_models = %w{ Customer Website Plan Feature PlanFeature }
```

### **Conseils avancés**

#### Classe Elevator personnalisée

Ok, nous avons construit une application _multi-tenant_ basée sur les sous-domaines, mais que se passe-t-il si nous avons besoin d'une fonctionnalité de domaines personnalisés pour nos clients ? Mais cela devrait toujours être accessible depuis le sous-domaine également. Nous avons alors besoin d'une classe elevator personnalisée — similaire à celle que nous avons utilisée ci-dessus — `Apartment::Elevators::Subdomain`.

La classe Elevator doit décider, sur la base de la requête actuelle, quel _tenant_ (base de données/schéma) doit être utilisé. Dans le cas où nous avons un champ `domain` sur le modèle `Website` :

![Image](https://cdn-media-1.freecodecamp.org/images/V8XTwU6cnTD4964hPCl0IOI0t1ANiMOx152I)

Ici, nous avons créé une classe elevator personnalisée (dans `lib/apartment/elevators/active_website.rb`) héritée de l'elevator `Subdomain` et surchargée par `parse_tenant_name` qui doit renvoyer le nom du tenant en fonction d'une requête. Nous appelons donc d'abord `super` et enregistrons le résultat dans la variable `tenant`. Si nous avons un site web avec le domaine configuré comme domaine demandé, nous renverrons ce slug (_tenant_). Sinon, nous nous rabattons sur le sous-domaine.

#### Page Non Trouvé pour les tenants incorrects

Tâche n°2 : que se passe-t-il si un tenant inexistant est demandé ? Quelqu'un fait une requête vers `aucun-tenant.example.com`, mais nous n'avons pas un tel schéma de base de données. La meilleure chose à faire est de répondre avec une page 404. Cette tâche ne concerne pas directement `apartment`, mais y est étroitement liée.

Nous allons améliorer notre classe elevator comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/zq3Kl4ZPYlbhj0SVRjyHgoPTsTx6ptXYNL8v)

Qu'est-ce que `::NotFound`, me demanderez-vous ? C'est un simple middleware que j'utilise à cet effet. Placé dans `app/middlewares`, il est écrit comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/3mHqiBZYHRzFTZWBcUbX02vDi0f-i9wNbBrK)

Tâche résolue — le client est content !

#### Sous-domaines exclus

Si vous avez besoin qu'un ou plusieurs sous-domaines soient traités comme un _tenant_ public (pas celui d'un client) et de ne pas changer lors des requêtes pour celui-ci, vous utiliseriez l'option `excluded_subdomains`. Cette option est disponible pour l'elevator `Subdomain` et ses sous-classes bien sûr :

```
Apartment::Elevators::ActiveWebsite.excluded_subdomains = ['app']
```

#### Peupler les données (Seeding)

Si vos _tenants_ sont déjà créés, vous pourriez les initialiser avec des données en utilisant `db/seeds.rb`. Avec `rails db:seed`, cela sera appliqué à chaque tenant.

Mais que se passe-t-il si vous devez initialiser un _tenant_ tout juste créé (via `Apartment::Tenant.create`) avec des données par programmation ? Eh bien, vous pourriez toujours le faire en basculant vers le tenant et en créant certains modèles (ou en exécutant la tâche _Rake_ par programmation).

Regardez comment la gem `spree_shared` fait cela pour la gem populaire `spree` (le code ci-dessous est une version mise à jour car `spree_shared` ne fonctionne pas avec la version actuelle de _Spree_) :

![Image](https://cdn-media-1.freecodecamp.org/images/MQ895qx1DCMfsbdtQD5JGI14gmnQZCCozCWe)

Si vous avez besoin que les seeds soient appliqués à chaque _tenant_, vous pourriez l'écrire de cette façon (encore une fois, un exemple modifié de `spree_shared`) :

![Image](https://cdn-media-1.freecodecamp.org/images/8iKqTff27RWVTIQqIQGZbq-blm0ItibiulKL)

#### Envelopper la création de tenant dans une transaction

L'étape suivante consiste à envelopper la création du _tenant_ dans un bloc de transaction, car nous savons que chaque _tenant_ a un modèle de base de données correspondant (`Website` ou `Customer`), et nous voulons nous assurer que l'instance du modèle et le _tenant_ ont tous deux été créés. Cela rendra notre application plus transactionnelle, et nous n'aurons pas de _tenant_ de base de données sans l'instance de modèle correspondante ou vice versa.

Les _Service Objects_ viennent à la rescousse ! Pour notre application de sites web hébergés, nous pourrions écrire quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/XYHmkWvcrpBMdkIT-6rZ8a0wpnKUK-TPLU51)

Nous devons gérer les exceptions possibles : si un enregistrement ou un _tenant_ n'a pas été créé pour une raison quelconque.

### Conclusion

Eh bien, comme vous pouvez le voir, développer des applications _multi-tenant_ est assez facile si vous avez de bons outils comme la gem `apartment`. Faites-moi part dans les commentaires de vos cas d'utilisation d' `apartment`. Surtout les cas non standard.