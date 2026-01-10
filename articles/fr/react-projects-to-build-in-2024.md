---
title: 7 Projets React à Construire en 2024
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2024-01-16T12:07:51.000Z'
originalURL: https://freecodecamp.org/news/react-projects-to-build-in-2024
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/mugshotbot.com_customize_color-orange-mode-light-pattern-bubbles-theme-two_up-url-https___gifcoins.io--1-.png
tags:
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: 7 Projets React à Construire en 2024
seo_desc: 'To be confident with using React, you need to build real-world projects.
  But what projects are worth building in 2024?

  I have put together a list of seven projects that I think are ideal for becoming
  a confident React developer, from simple to comple...'
---

Pour être à l'aise avec l'utilisation de React, vous devez construire des projets concrets. Mais quels projets valent la peine d'être construits en 2024 ?

J'ai compilé une liste de sept projets que je pense idéaux pour devenir un développeur React confiant, allant des applications simples aux complexes. Cela vous donnera de l'inspiration pour les applications à construire.

Je vais également vous guider à travers l'ensemble de la stack technique que j'utiliserais pour construire chaque projet, ainsi qu'un résumé de la manière de construire chacun d'eux étape par étape.

Commençons !

## 👨🏻💻 Application IA ChatGPT

Alors que ChatGPT devient de plus en plus puissant, vous pouvez construire des applications impressionnantes en utilisant l'API ChatGPT.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/chatgpt.png)
_Application IA ChatGPT : Draw-a-UI_

C'est une excellente application de départ car, pour la plupart des applications, tout ce que vous avez à faire est d'envoyer du texte ou une image à l'API ChatGPT, de lui donner quelques instructions, et elle vous renverra une réponse.

Vous pourriez utiliser l'API ChatGPT pour construire un résumeur de texte, une application de traduction, une application qui explique ce que fait un extrait de code. Les possibilités sont vraiment infinies.

Une simple application IA alimentée par ChatGPT que j'ai construite est "Draw a UI", où vous pouvez dessiner une maquette rapide d'une interface utilisateur, l'envoyer à ChatGPT, et elle vous renverra le code HTML généré selon votre capture d'écran !

Je construirais cette application en utilisant Next.js ainsi que le package npm `tldraw`, qui vous permet de dessiner des images dans votre application React.

Ensuite, envoyez cette capture d'écran à un gestionnaire de route Next.js sur le backend qui utilise le package npm **openai** pour communiquer avec ChatGPT, puis renvoie le code HTML.

## 👨🏻💻 Site Web Personnel

Si vous n'êtes pas encore prêt à construire quelque chose de très complexe, un site web personnel est un excellent point de départ. Vous pouvez l'utiliser comme moyen de vous familiariser avec JSX et CSS dans React.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/portfolio.png)
_Un site web personnel fait avec Next.js et TailwindCSS_

Apprenez à créer des composants de base, à ajouter des images, des liens vers vos profils de réseaux sociaux, et ainsi de suite. Lorsque vous commencez à construire plus de projets, vous pouvez les montrer sur votre site web.

L'avantage d'un site web personnel est que vous pouvez l'étendre autant que vous le souhaitez. Vous pouvez ajouter votre propre blog intégré, ou vous pouvez parler des choses que vous avez apprises ou sur lesquelles vous travaillez actuellement.

Pour construire votre site web personnel, je recommande d'utiliser Next.js car il facilite la création de pages individuelles qui sont rendues statiquement, ce qui est bon pour le SEO.

Pour les images, vous pouvez utiliser la bibliothèque intégrée `next/image`. Et pour créer un blog, je recommande vivement d'utiliser le package ContentLayer, que vous pouvez utiliser pour écrire tous vos articles de blog en markdown ou MDX.

ContentLayer est génial car il rend votre contenu markdown typé de manière sécurisée afin que vous sachiez quelles données chaque article de blog inclut. C'est aussi une excellente façon de commencer avec TypeScript dans React, bien que cela puisse sembler intimidant au début.

## 💬 Application de Chat

Une application web vraiment dynamique serait une application de chat, quelque chose que vous utilisez probablement tous les jours. Il est bon de construire des applications que vous connaissez bien car cela vous donne une bonne idée des parties qui la composent.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/chat.png)
_Application de Chat faite avec React, similaire à WhatsApp_

Une application de chat est simple en termes de ses composants. Vous n'avez besoin que d'une zone de messages, d'une entrée pour taper de nouveaux messages, et d'une liste de personnes avec qui discuter.

C'est un excellent projet car il peut être aussi simple ou aussi complexe que vous le souhaitez. Pour construire quelque chose comme cela, j'utiliserais Vite pour créer le projet React et alimenter le backend avec Supabase.

Vous n'avez pas besoin de code côté serveur ici avec Supabase, et il offre également une fonctionnalité de chat en temps réel, entièrement gratuite. Vous pouvez ajouter une authentification pour identifier les utilisateurs (en utilisant Supabase Auth), et mettre tous les utilisateurs créés dans une barre latérale pour discuter.

Ensuite, vous pouvez créer une table pour les messages et les envoyer à Supabase chaque fois que quelqu'un tape du texte. Pour l'étendre davantage, vous pourriez permettre d'ajouter des images et des vidéos avec Supabase Storage.

Enfin, vous pouvez afficher les messages en temps réel en utilisant des abonnements en fonction de l'utilisateur avec qui vous discutez.

## 💳 Application E-Commerce

Le prochain type d'application dont nous allons parler est une application e-commerce.

Une application e-commerce peut être utilisée pour vendre des produits physiques ou numériques avec une fonctionnalité d'achat unique.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/ecommerce.png)
_Une application E-Commerce avec des biens physiques, faite avec Next.js_

Après l'achat, vous devez le livrer au client. L'application e-commerce pourrait être très complexe, mais elle n'a pas besoin de l'être au début. Vous devez simplement créer une vitrine de base avec vos produits.

Donnez-leur une image associée avec une description, ainsi qu'un bouton d'achat. Vous n'avez même pas besoin d'ajouter une authentification. Pour construire cela, j'utiliserais Next.js intégré avec Stripe pour gérer les achats.

Le système d'inventaire n'a pas besoin d'être très complexe si vous vendez un produit physique. Il pourrait être aussi simple que d'avoir un nombre dans une base de données qui peut être mis à jour lorsque le stock est ajouté et diminué lorsque quelqu'un fait un achat.

## 🛢🏻 Place de Marché en Ligne

La place de marché en ligne est une extension de l'application e-commerce. Elle est un peu plus complexe car vous ajoutez plus de produits. 

Vous pourriez également envisager d'ajouter des fonctionnalités supplémentaires telles que des avis, qui sont essentiels pour les achats en ligne.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/marketplace.png)
_Boutique Next.js avec un panier d'achat intégré et des avis_

Le défi dans ce cas est d'ajouter un panier d'achat. Pour offrir une bonne expérience utilisateur sur un site web avec de nombreux produits, vous voulez permettre aux clients d'ajouter plusieurs produits à leur panier.

Pour ajouter un panier d'achat, j'utiliserais la même stack que précédemment, Next.js et Stripe, pour gérer et acheter les produits. Heureusement, il existe un excellent package appelé use-shopping-cart, qui s'intègre parfaitement avec le checkout Stripe.

Vous pouvez l'utiliser pour créer un panier d'achat complet avec la possibilité d'ajouter et de supprimer des articles, ainsi que de vider le panier directement.

Pour les avis, vous pourriez ajouter une couche de base de données comme Supabase, ou vous pourriez externaliser les avis à un service tiers qui permet d'intégrer des avis, comme Trustpilot, par exemple.

## 🚚 Application SaaS (Logiciel en tant que Service)

L'évolution finale dans la vente en ligne avec React est une application SaaS.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/saas.png)
_Application SaaS inspirée de Gumroad faite avec Next.js_

Dans cette application, vous fournissez aux clients l'accès à un certain service logiciel que vous avez créé, généralement pour un abonnement mensuel ou annuel.

Vous pouvez créer une application SaaS comme version payante d'une application que vous avez déjà construite, telle que l'application IA ou l'application de chat.

En bref, si vous pouvez construire une application pour laquelle les utilisateurs paieraient, soit pour être plus productifs, pour se divertir, ou pour les éduquer, alors tout ce que vous avez à faire pour créer une application SaaS est de facturer à ces clients des frais pour son utilisation.

Une application SaaS pourrait facturer les utilisateurs en fonction de l'utilisation ou sur une période définie, telle qu'un mois ou une année.

Cela peut être fait avec l'aide de Stripe ou d'un marchand de records tel que Paddle, qui facilite les taxes. Les deux peuvent gérer les abonnements.

Je recommande d'utiliser Stripe Checkout pour permettre aux clients de gérer leur abonnement et de l'annuler si nécessaire.

## 📱 Clone d'Application du Monde Réel

Enfin, le projet le plus ambitieux serait de construire un clone d'une application que vous aimez vraiment ou que vous utilisez tous les jours.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/clone.png)
_Un clone de l'application web YouTube avec React_

Un clone d'application est très difficile car vous clonez généralement quelque chose sur lequel une grande entreprise est basée. Cependant, c'est une excellente approche pour améliorer vos compétences en tant que développeur React car vous devez réfléchir à la manière dont un service est conçu.

Si vous deviez cloner quelque chose comme YouTube, par exemple, vous ne construirez pas seulement l'interface utilisateur et la faire ressembler à celle de YouTube, mais vous aurez également besoin des fonctionnalités que YouTube possède, telles que les menus, les tiroirs, les notifications, et la capacité d'ajouter et de visualiser des vidéos, des commentaires, des likes, et ainsi de suite.

Si je devais construire un clone de YouTube, j'utiliserais soit Supabase soit une base de données MySQL comme PlanetScale, ainsi que Next.js, et l'authentification avec Supabase ou NextAuth.

Je construirais l'interface utilisateur avec TailwindCSS et Radix UI. Radix est une bibliothèque qui fournit des composants simples (primitifs) qui peuvent être facilement stylisés, mais qui sont entièrement fonctionnels, ce qui vous fait gagner beaucoup de temps.

Pour télécharger des vidéos et des médias, j'utiliserais une plateforme dédiée au streaming de vidéos telle que Mux, qui fournit une excellente API pour les développeurs.

Pour stocker les images et tous les autres médias et pièces jointes, j'utiliserais Supabase Storage.

Jusqu'où vous allez dépend vraiment de votre ambition et de votre volonté d'en faire une entreprise à part entière ou un excellent projet de portfolio à montrer à de potentiels employeurs.

## 🏠🏻 Vous voulez construire tous les projets ?

Vous pouvez apprendre exactement comment construire chaque projet dans cette liste à l'intérieur du tout nouveau React Bootcamp :

✨ **[Présentation : Le React Bootcamp](https://www.thereactbootcamp.com)**

Vous apprendrez comment construire chaque projet de cette liste à travers des heures de vidéos étape par étape, plus le code source complet pour les rendre vôtres.

Le bootcamp propose toutes les ressources pour vous aider à réussir avec React :

* 🎬 200+ vidéos approfondies
* 🕹🏻 100+ défis pratiques React
* 🏠🏻 5+ projets de portfolio impressionnants
* 📄 10+ fiches de révision essentielles React
* 🥾 Un bootcamp complet Next.js
* 🎼🏻 Une série complète de vidéos animées

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même.

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)