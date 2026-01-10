---
title: Comment créer votre propre site E-Commerce avec Medusa
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-02-27T15:36:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-own-e-commerce-site-with-medusa
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/medusa.png
tags:
- name: ecommerce
  slug: ecommerce
- name: node
  slug: node
seo_title: Comment créer votre propre site E-Commerce avec Medusa
seo_desc: "In today's digital age, having an online presence is crucial for businesses\
  \ of all sizes. \nWhether you're an established retailer or an aspiring entrepreneur,\
  \ an ecommerce site can provide you with a platform to reach a global audience and\
  \ sell your ..."
---

À l'ère numérique d'aujourd'hui, avoir une présence en ligne est crucial pour les entreprises de toutes tailles. 

Que vous soyez un détaillant établi ou un entrepreneur en herbe, un site ecommerce peut vous fournir une plateforme pour atteindre un public mondial et vendre vos produits ou services 24 heures sur 24.

Créer un site ecommerce peut sembler une tâche ardue, mais avec les bons outils et les bonnes directives, n'importe qui peut créer une boutique en ligne professionnelle et fonctionnelle. 

Dans ce tutoriel, vous apprendrez à créer votre propre site e-commerce avec Medusa.

## Qu'est-ce que Medusa ?

[Medusa](https://medusajs.com) est une plateforme de commerce _open source_ et _composable_, parfaite pour les développeurs qui souhaitent créer une solution ecommerce personnalisée. Avec son architecture flexible et ses fonctionnalités puissantes, Medusa offre une manière transparente et simple de créer un site ecommerce robuste et évolutif.

Medusa propose une variété de fonctionnalités, y compris la gestion des commandes avec des échanges, retours et réclamations automatisés. Il permet également la gestion des clients et leur affectation à des groupes de clients, ainsi que la personnalisation des produits et le tri des collections. 

Avec la capacité de gérer plusieurs régions et devises, les utilisateurs peuvent intégrer divers plugins et services tiers, créer des règles de prix et de réduction avancées, configurer les taxes et mettre en place plusieurs canaux de vente. 

De plus, Medusa offre des stratégies d'importation et d'exportation en masse, ainsi que des capacités de personnalisation complète pour créer des endpoints personnalisés, des services, des abonnés, des stratégies de tâches par lots, et plus encore.

En un peu plus d'un an depuis son lancement, cette plateforme est rapidement devenue la [solution ecommerce Node.js n°1](https://medusajs.com/blog/nodejs-ecommerce-backend/), accumulant plus de 17K+ étoiles sur [GitHub](https://github.com/medusajs/medusa) grâce à sa popularité immense.

## Architecture de Medusa

Avec une architecture composable, les composants frontend et backend de Medusa sont faiblement couplés. La plateforme se compose de trois composants différents : le **backend headless**, le **tableau de bord admin** et la **vitrine**.

Vous pouvez choisir d'utiliser la plateforme Medusa complète ou seulement les parties dont vous avez besoin pour votre boutique. 

De plus, avec le backend découplé du frontend, les développeurs peuvent se concentrer sur leurs domaines d'expertise respectifs. Les développeurs backend peuvent se concentrer sur le serveur Medusa, tandis que les développeurs frontend peuvent se concentrer sur la vitrine ou l'admin.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/medusa-arch.png)
_Architecture de Medusa_

Dans les sections à venir, vous verrez comment Medusa fournit la plupart des fonctionnalités des boutiques ecommerce directement, avec la possibilité de configurer ces fonctionnalités selon votre cas d'utilisation spécifique.

### **Serveur Medusa**

Le serveur Medusa, qui est un backend ecommerce Node.js, sert de composant central de la plateforme. Il contient toutes les données et la logique de la boutique, et les deux autres composants utilisent ses API REST pour créer, récupérer et modifier des données.

Le serveur fournit la plupart des fonctionnalités liées à un flux de travail ecommerce. Ces fonctionnalités incluent la gestion des produits, des paniers et des commandes, ainsi que l'intégration avec les fournisseurs de livraison et de paiement et la gestion des utilisateurs. 

En plus de cela, vous pouvez configurer votre boutique, y compris la région de votre boutique, les règles fiscales, les réductions, les cartes-cadeaux, et plus encore.

Puisque Medusa est hautement extensible, il permet aux développeurs de créer des fonctionnalités personnalisées telles que [l'automatisation des affectations de groupes de clients](https://medusajs.com/blog/customer-group-automation/) et [l'intégration de ChatGPT pour automatiser l'écriture des descriptions de produits](https://medusajs.com/blog/chatgpt-medusa/). 

En plus de cela, vous pouvez également intégrer des services tiers dans Medusa en utilisant des [Plugins](https://docs.medusajs.com/advanced/backend/plugins/overview). Vous pouvez trouver des plugins officiels et communautaires pour vous aider avec vos besoins courants. En savoir plus sur ces plugins [ici](https://docs.medusajs.com/advanced/backend/plugins/overview/).

Medusa vous permet également d'étendre ses fonctionnalités avec de nouveaux endpoints, une logique métier et des entités de base de données. De plus, vous pouvez créer des abonnés qui écoutent les événements et déclenchent des actions spécifiques.

### Vitrine Medusa

La vitrine sert de couche de présentation principale ou de frontend de votre boutique ecommerce où les clients peuvent voir et acheter vos produits. Ces vitrines peuvent prendre la forme d'applications web progressives ou d'applications mobiles.

Medusa propose deux modèles de vitrine construits avec [Next.js](https://docs.medusajs.com/starters/nextjs-medusa-starter) et [Gatsby](https://docs.medusajs.com/starters/gatsby-medusa-starter/), respectivement. La vitrine inclut plusieurs fonctionnalités telles que les pages de liste et de détails des produits, les fonctionnalités d'authentification et de profil client, et un flux de paiement complet prenant en charge les détails et méthodes de livraison. Elle est également équipée de capacités de recherche prêtes pour l'intégration avec des solutions de premier plan comme Algolia et MeiliSearch.

Ci-dessous une démonstration de l'apparence de la vitrine Next.js :

%[https://youtu.be/TmV2xNbNs4w]

En plus des modèles de vitrine fournis, vous avez la liberté de créer votre propre vitrine personnalisée en utilisant les [API REST de la vitrine](https://docs.medusajs.com/api/store/).

### **Admin Medusa**

Un composant essentiel d'une boutique ecommerce est le tableau de bord Admin, qui permet aux commerçants de visualiser, créer et modifier des données telles que les produits et les commandes.

Avec le tableau de bord Admin Medusa, Medusa fournit des fonctionnalités pour la gestion de la boutique, y compris la gestion des produits, des commandes et des utilisateurs. Vous pouvez gérer vos commandes de diverses régions et canaux en utilisant un seul tableau de bord.

Pour les commerçants migrant leurs boutiques depuis d'autres plateformes, le tableau de bord admin offre des fonctionnalités d'importation et d'exportation faciles pour de grands ensembles de données de produits, commandes et clients. Le tableau de bord offre également des fonctionnalités de groupe de clients pour créer des listes de prix personnalisées, des réductions et des cartes-cadeaux.

Voici à quoi ressemble le tableau de bord Admin Medusa :

%[https://youtu.be/Z6uoN7TR0Z0]

Cependant, si vous n'êtes pas satisfait du tableau de bord admin existant, vous pouvez utiliser les API REST Admin pour l'étendre davantage.

## Comment configurer une boutique Ecommerce avec Medusa

Dans cette section, vous allez configurer les trois composants de votre boutique ecommerce Medusa.

### Prérequis

Avant de commencer le tutoriel, vous devez avoir installé :

* [Node.js(V14 ou ultérieur)](https://docs.medusajs.com/tutorial/set-up-your-development-environment#nodejs)
* [Git](https://docs.medusajs.com/tutorial/set-up-your-development-environment/#git)
* [Medusa CLI](https://docs.medusajs.com/tutorial/set-up-your-development-environment#medusa-cli)

### Comment configurer le serveur Medusa

Créer un nouveau serveur Medusa est un processus simple en utilisant le CLI Medusa. Naviguez vers le répertoire où vous souhaitez créer votre serveur Medusa et exécutez la commande suivante pour créer un nouveau serveur Medusa avec le nom `my-medusa-store` :

```bash
medusa new my-medusa-store --seed
```

Cette commande créera un nouveau serveur Medusa avec le nom spécifié. L'option `--seed` indique au CLI Medusa de peupler les données après la création du serveur. Les données de peuplement incluent des données d'exemple telles que des produits, des catégories, et plus encore.

Une fois la commande terminée, naviguez vers le répertoire `my-medusa-store` et démarrez le serveur en exécutant la commande suivante :

```bash
cd my-medusa-store
medusa develop
```

En quelques minutes, le serveur démarrera sur le port par défaut `9000`. Vous pouvez le tester en envoyant une requête à l'aide d'un outil comme Postman ou via la ligne de commande :

```bash
curl localhost:9000/store/products
```

Si votre serveur est configuré avec succès, vous verrez une liste de produits et d'autres détails comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/curl-output.png)
_Sortie de la commande cURL_

### Comment configurer la vitrine Next.js

Maintenant que votre serveur Medusa est opérationnel, il est temps de configurer votre vitrine. Dans cette section, vous allez configurer la vitrine Next.js.

Créez un nouveau projet Next.js en utilisant le [modèle de démarrage Medusa Next.js](https://github.com/medusajs/nextjs-starter-medusa) :

```bash
npx create-next-app -e https://github.com/medusajs/nextjs-starter-medusa my-medusa-storefront
```

Naviguez vers le nouveau répertoire `my-medusa-storefront` et renommez le fichier de variables d'environnement de modèle pour utiliser les variables d'environnement en développement :

```bash
cd my-medusa-storefront
mv .env.template .env.local
```

Assurez-vous que le serveur Medusa est en cours d'exécution, puis exécutez le serveur Next.js local :

```bash
npm run dev
```

Votre vitrine Next.js sera maintenant en cours d'exécution sur son port par défaut `8000`.

Note : Medusa vous fournit également le [modèle de démarrage Gatsby](https://docs.medusajs.com/starters/gatsby-medusa-starter/) pour créer la vitrine.

### Comment configurer le tableau de bord Admin Medusa

Puisque le tableau de bord Admin Medusa utilise le serveur Medusa, assurez-vous que votre serveur est opérationnel.

Commencez par cloner le [dépôt GitHub Admin](https://github.com/medusajs/admin) :

```bash
git clone https://github.com/medusajs/admin my-medusa-admin
```

Naviguez vers le dossier cloné `my-medusa-admin` et installez toutes les dépendances :

```bash
cd my-medusa-admin
npm install
```

Exécutez le serveur de développement :

```bash
npm run start
```

En quelques minutes, l'admin démarrera sur le port par défaut `7000`. Donc, dans votre navigateur, allez à `localhost:7000` pour voir votre admin.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/medusa-admin.png)
_Connexion Admin Medusa_

Si vous aviez déjà peuplé les données dans votre serveur Medusa, vous pouvez utiliser l'email `admin@medusa-test.com` et le mot de passe `supersecret` pour vous connecter. Si vous ne l'aviez pas fait, vous pouvez [créer un nouvel utilisateur admin](https://docs.medusajs.com/admin/quickstart#create-a-new-admin-user).

## Comment configurer Medusa avec `create-medusa-app`

Jusqu'à présent, vous avez vu comment configurer les composants individuels d'un projet Medusa. Mais dans cette section, vous apprendrez à configurer un projet Medusa complet avec les trois composants en utilisant une seule commande.

Medusa vous fournit maintenant une commande `create-medusa-app` pour configurer un projet. Cette commande fournit une invite interactive qui vous guide tout au long du processus de configuration.

Pour utiliser `create-medusa-app`, exécutez simplement la commande suivante :

```bash
npx create-medusa-app
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/create-medusa-app.gif)
_Création d'un projet Medusa avec create-medusa-app_

Dans cette configuration interactive, vous serez invité à entrer le nom du répertoire où vous souhaitez installer le projet Medusa. Le nom par défaut est `my-medusa-store`, mais vous pouvez choisir de le nommer autrement.

Ensuite, vous serez invité à sélectionner un modèle de serveur Medusa parmi les options disponibles, qui incluent le modèle par défaut, le modèle Contentful, et l'option d'entrer une URL de modèle personnalisée. Le serveur sera installé dans le répertoire `backend` de votre projet, et une base de données SQLite de démonstration sera créée à l'intérieur.

Suite à la configuration du serveur Medusa, vous serez invité à choisir un modèle de vitrine parmi les options disponibles. Si vous choisissez d'installer une vitrine, elle sera installée dans le répertoire `storefront` de votre projet. Si vous choisissez "Aucun", aucune vitrine ne sera installée.

L'admin est configuré automatiquement dans le répertoire `admin` de votre projet.

Une fois la configuration terminée, vous recevrez des instructions sur la façon de démarrer chaque composant du projet Medusa.

```bash
Votre projet est prêt. Les commandes disponibles sont :

API Medusa
cd my-medusa-store/backend
yarn start

Admin
cd my-medusa-store/admin
yarn start

Vitrine
cd my-medusa-store/storefront
yarn develop # pour la vitrine Gatsby
yarn dev # pour la vitrine Next.js
```

Gardez simplement à l'esprit que les commandes peuvent différer en fonction de vos choix dans les invites précédentes.

### Structure du répertoire du projet

Dans le répertoire racine du projet (qui a été spécifié au début du processus d'installation - `my-medusa-store` dans ce cas), vous trouverez la structure de répertoire suivante :

```bash
my-medusa-store
  ├─ admin
  ├─ backend
  └─ storefront
```

## Conclusion

Dans ce tutoriel, nous avons exploré Medusa, une plateforme e-commerce open-source qui fournit un ensemble robuste de fonctionnalités pour créer des boutiques en ligne. Nous avons examiné l'architecture de Medusa, ses principales fonctionnalités et comment configurer le serveur, le tableau de bord admin et la vitrine.

L'un des points forts de Medusa est sa flexibilité et son extensibilité. Avec une variété de plugins et d'extensions, vous pouvez personnaliser votre site e-commerce pour répondre à vos besoins spécifiques. Vous pouvez également créer vos propres plugins ou thèmes, ce qui facilite la création d'un site qui reflète votre marque.

Si vous cherchez à créer un site e-commerce, Medusa est un choix solide qui offre beaucoup de fonctionnalités dès le départ. Avec son interface conviviale, la configuration d'une boutique en ligne est un processus simple. De plus, puisque c'est une plateforme open-source, vous avez la liberté de la modifier et de l'étendre selon vos besoins.

### Ressources supplémentaires

Voici quelques ressources que vous pouvez utiliser pour étendre les fonctionnalités :

* Intégrez [SendGrid](https://docs.medusajs.com/add-plugins/sendgrid) en tant que fournisseur de notifications.
* Intégrez [Stripe](https://docs.medusajs.com/add-plugins/stripe) en tant que fournisseur de paiement.
* [Créez un service](https://docs.medusajs.com/advanced/backend/services/create-service).