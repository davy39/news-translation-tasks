---
title: Comment implémenter le RBAC dans un tableau de bord communautaire avec Nuxt
subtitle: ''
author: Obum
co_authors: []
series: null
date: '2024-11-22T17:28:44.668Z'
originalURL: https://freecodecamp.org/news/rbac-community-dashboard-with-nuxt
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1732043730534/d88680d7-2590-4541-9120-40a43c3724ef.png
tags:
- name: authorization
  slug: authorization
- name: authentication
  slug: authentication
- name: Nuxt.js
  slug: nuxtjs
seo_title: Comment implémenter le RBAC dans un tableau de bord communautaire avec
  Nuxt
seo_desc: 'Role Based Access Control (RBAC) is a useful authorization model for users
  with different access levels, such as those in a community dashboard.

  In this article, you’ll learn how to integrate this type of authorization with Permit.io
  in Nuxt.

  Table o...'
---

Le contrôle d'accès basé sur les rôles (RBAC) est un modèle d'autorisation utile pour les utilisateurs avec différents niveaux d'accès, comme ceux d'un tableau de bord communautaire.

Dans cet article, vous apprendrez comment intégrer ce type d'autorisation avec Permit.io dans Nuxt.

## Table des matières

* [Table des matières](#heading-table-des-matieres)
    
* [Quelle est la différence entre l'authentification et l'autorisation ?](#heading-quelle-est-la-difference-entre-lauthentification-et-lautorisation)
    
* [Qu'est-ce que le contrôle d'accès basé sur les rôles (RBAC) ?](#heading-quest-ce-que-le-controle-dacces-base-sur-les-roles-rbac)
    
* [Quels sont les avantages de l'utilisation de l'autorisation en tant que service ?](#heading-quels-sont-les-avantages-de-lutilisation-de-lautorisation-en-tant-que-service)
    
* [Ce que nous allons construire](#heading-ce-que-nous-allons-construire)
    
* [Comment planifier le RBAC avec](#heading-comment-planifier-le-rbac-avec-permitio) [Permit.io](http://Permit.io)
    
* [Comment configurer](#heading-comment-configurer-permitio-dans-nuxt) [Permit.io](http://Permit.io) [dans Nuxt](#heading-comment-configurer-permitio-dans-nuxt)
    
* [Comment contrôler l'accès à l'API avec le middleware Nuxt](#heading-comment-controler-lacces-a-lapi-avec-le-middleware-nuxt)
    
* [Comment tester le RBAC dans le tableau de bord communautaire](#heading-comment-tester-le-rbac-dans-le-tableau-de-bord-communautaire)
    
* [Résumé](#heading-resume)
    

## Quelle est la différence entre l'authentification et l'autorisation ?

Lors de la construction d'applications, nous effectuons souvent l'authentification ainsi que l'autorisation. Cependant, ces deux concepts sont essentiellement différents.

L'authentification consiste à vérifier qui est un utilisateur. Pendant le processus d'authentification, l'utilisateur doit généralement se connecter avec un identifiant tel qu'un email, un téléphone, un nom d'utilisateur, *avec* Google, *avec* Microsoft, etc.

L'autorisation spécifie les ressources qu'un utilisateur authentifié peut consulter et ce qu'il peut faire dans l'application. L'autorisation indique les droits d'accès d'un utilisateur après que cet utilisateur a été authentifié avec succès.

Par exemple, l'authentification est un utilisateur se connectant avec un email et un mot de passe ou vérifiant son numéro de téléphone avec un SMS. D'autre part, l'autorisation est un rédacteur créant et modifiant des publications tandis que seuls les administrateurs peuvent approuver et publier ces publications.

Le but principal de l'authentification est d'établir l'identité d'un utilisateur avant de lui accorder l'accès au système. L'objectif principal de l'autorisation est de contrôler les actions des utilisateurs et de protéger les données ou ressources sensibles.

## Qu'est-ce que le contrôle d'accès basé sur les rôles (RBAC) ?

Le contrôle d'accès basé sur les rôles (RBAC) est un modèle d'autorisation que vous pouvez utiliser pour gérer et restreindre l'accès aux ressources du système. Il est basé sur les responsabilités, les devoirs ou les rôles des utilisateurs.

Dans le RBAC, les rôles représentent des ensembles prédéfinis de permissions qui indiquent quelles actions un utilisateur peut exécuter dans une application. Ces rôles sont ensuite attribués aux utilisateurs en fonction de leurs fonctions ou responsabilités.

Dans les systèmes courants, n'importe qui peut attribuer des permissions à des utilisateurs individuels. Dans le RBAC, nous regroupons les permissions en rôles. À notre tour, nous attribuons ces rôles aux utilisateurs. Par exemple, dans un tableau de bord communautaire, les utilisateurs peuvent avoir des rôles comme « Admin », « Mentor » ou « Membre ».

Outre le contrôle d'accès basé sur les rôles, d'autres modèles d'autorisation populaires existent tels que le contrôle d'accès basé sur les attributs (ABAC) et le contrôle d'accès basé sur les relations (ReBAC). Le contrôle d'accès basé sur les attributs utilise une large gamme d'attributs et convient aux systèmes en constante évolution. Vous pourriez également le combiner avec le contrôle d'accès basé sur les rôles. Pour plus d'informations, consultez l'article [Permit.io sur RBAC vs. ABAC](https://www.permit.io/blog/rbac-vs-abac).

## Quels sont les avantages de l'utilisation de l'autorisation en tant que service ?

Vous pouvez construire des modèles d'autorisation vous-même dans votre application. Mais cela peut être chronophage et coûteux à long terme.

L'utilisation d'un fournisseur externe pour l'autorisation vous permet de vous concentrer sur la logique métier dans vos applications. Les avantages de l'externalisation de l'autorisation sont similaires à l'utilisation d'un tiers comme Auth0 ou Firebase pour l'authentification.

[L'autorisation en tant que service](https://www.permit.io/blog/authorization-as-a-service) fournit une solution pour gérer l'accès des utilisateurs et les permissions dans les applications. Lorsque vous utilisez une telle solution d'autorisation, vous bénéficiez d'une sécurité renforcée, d'un contrôle granulaire des politiques d'accès, de politiques d'auto-scaling, d'une réduction de la charge de maintenance, de mises à jour plus rapides, d'une journalisation robuste, etc.

Permit.io est gratuit à utiliser pour [jusqu'à 1000 utilisateurs actifs mensuels](https://docs.permit.io/manage-your-account/workspace-usage/#maus--tenants-usage), et dispose d'une interface utilisateur et d'une API pour RBAC, ABAC et ReBAC.

Pour commencer avec Permit.io :

* Allez sur [app.permit.io](https://app.permit.io)
    
* Créez un compte
    
* Créez un espace de travail (dans votre compte)
    

![Démo de la prise en main de Permit.io](https://cdn.hashnode.com/res/hashnode/image/upload/v1732037452876/4604ad72-c5cc-4e07-8f04-70ff4f3dbb8c.gif align="center")

## Ce que nous allons construire

Un tableau de bord communautaire connecte les membres au sein d'une communauté ou d'un forum. C'est une plateforme où ils peuvent interagir et accéder aux ressources.

À des fins de démonstration du RBAC, nous allons construire un simple tableau de bord communautaire qui inclura 3 types de contenu (entités) : publications, matériaux et annonces.

Le code que nous allons utiliser se trouve à l'adresse [https://github.com/obumnwabude/rbac-community-dashboard](https://github.com/obumnwabude/rbac-community-dashboard). Il consiste en un dépôt Nuxt avec son serveur configuré pour les appels API et son front-end construit avec Vue. Clonez-le avec git et explorez le code dans un éditeur/IDE.

Dans le serveur, nous allons exposer des endpoints *GET, POST* et *DELETE* pour chaque entité (publications, matériaux et annonces). Dans Nuxt, vous pouvez utiliser le verbe HTTP dans le nom de fichier pour le gestionnaire d'endpoint. Nous pouvons donc avoir **posts.get.ts**, **posts.delete.ts**, **materials.post.ts**, etc., chaque fichier contenant le gestionnaire respectif pour l'endpoint API concerné.

De plus, les fichiers du serveur stockent et récupèrent les entités à partir de fichiers JSON. Vous devriez avoir une configuration de base de données robuste dans votre produit. Pour ce projet, nous utiliserons des fichiers JSON locaux pour construire un exemple minimal reproductible en nous concentrant sur les rôles et l'autorisation.

Dans le front-end, nous avons quatre pages : trois pour les entités et une page de paramètres. Il y a aussi une navigation simple : une barre inférieure sur les petits écrans et une barre latérale sur les plus grands. Chaque page d'entité affiche une liste de ses éléments et un petit formulaire pour en créer de nouveaux.

De plus, le code de démonstration utilise [tailwindcss](https://tailwindcss.com/) pour styliser rapidement tout. La page des paramètres contient des exemples d'utilisateurs et de rôles codés en dur pour la démonstration. Lors des tests, basculez l'utilisateur actuel et voyez les rôles en action.

![Démo de l'exploration du tableau de bord communautaire](https://cdn.hashnode.com/res/hashnode/image/upload/v1732031161755/36a4981c-bc1c-4156-afb8-05fab7d45ee7.gif align="center")

Cet article se concentre sur les parties du code qui traitent de l'autorisation. Pour le backend et les spécificités de l'interface utilisateur du tableau de bord communautaire, nous ne donnerons qu'un aperçu. Après cela, nous plongerons en profondeur dans les points de contact du RBAC.

## Comment planifier le RBAC avec Permit.io

Dans l'ensemble, la planification de l'autorisation signifie cartographier « qui » peut effectuer une action sur « quoi ». Dans le RBAC, nous définissons des rôles puis nous les attribuons aux utilisateurs. La combinaison des rôles et des utilisateurs est la partie « qui » de l'autorisation.

Le côté « quoi » fait référence aux entités ou ressources que votre application fournit ou gère. Pour l'exemple de cet article, nous avons choisi nos ressources comme Publications, Matériaux et Annonces.

Les actions sont des activités utilisateur. Les actions les plus courantes sont « créer », « lire », « mettre à jour » et « supprimer ». Par ressource dans votre application, vous pouvez utiliser ces quatre actions, en ajouter plus ou en omettre certaines. Dans cet article, nos ressources auront chacune les quatre actions.

Lors de la planification de l'autorisation, définissez les ressources ainsi que les « actions » que les utilisateurs peuvent exécuter sur chaque ressource. Après cela, définissez les rôles. Pour chaque rôle, spécifiez quelles actions un utilisateur détenant ce rôle peut effectuer sur chaque ressource. La cartographie des ressources, des actions et des rôles vous permet de définir les politiques d'autorisation de votre application.

Permit.io facilite la modification des politiques. Dans Permit.io, vous disposez d'un tableau de bord intuitif où vous pouvez créer des ressources et leurs actions, créer des rôles et fusionner les deux avec des tables de politiques.

![Démo de la création de ressources et d'actions dans Permit.io](https://cdn.hashnode.com/res/hashnode/image/upload/v1732037510499/2c0acabb-e0b4-4002-8b7b-e2fd4dbb4777.gif align="center")

Pour notre exemple de tableau de bord communautaire, nous allons créer trois rôles avec un accès incrémental : membre, mentor et administrateur. Pour chaque rôle, nous permettrons l'accès en lecture à toutes les ressources. Cependant, chaque rôle a différents niveaux d'accès de gestion aux ressources comme suit :

* Les **membres** peuvent consulter toutes les entités mais ne peuvent créer ou supprimer que des publications.
    
* Les **mentors** peuvent consulter toutes les entités et peuvent créer ou supprimer des publications et des matériaux.
    
* Les **administrateurs** peuvent créer, consulter et supprimer toutes les entités.
    

L'attribution de rôles aux actions dans les ressources est la même que la modification des politiques.

![Démo de la création de rôles et de la modification des politiques dans Permit.io](https://cdn.hashnode.com/res/hashnode/image/upload/v1732037619254/e8900675-18c0-429c-9840-3ba8c1c38a6c.gif align="center")

## Comment configurer Permit.io dans Nuxt

Pour notre projet de démonstration, vous devez exécuter `npm install`, créer un fichier `.env` et exporter votre jeton Permit.

Cependant, si vous construisez un nouveau projet, pour configurer Permit dans Nuxt, installez-le d'abord avec npm.

```bash
npm install permitio
```

Après cela, créez un fichier `.env` et ajoutez votre PERMIT\_TOKEN. Obtenez le jeton depuis le tableau de bord.

```bash
PERMIT_TOKEN=permit_key_XXXXXXXXXXXXXXXXXXXXX
```

Pour rendre ce jeton disponible pour la configuration `runtimeConfig` de Nuxt, ajoutez-le au fichier `nuxt.config.ts`. Ajoutez également `permitio` (ainsi que d'autres dépendances) dans le tableau `transpile` de la propriété build du fichier de configuration Nuxt.

Cette addition est pour tenir compte des optimisations spécifiques de Nuxt. Votre fichier `nuxt.config.ts` devrait ressembler à ce qui suit :

```typescript
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  // ... autres propriétés

  build: {
    transpile: ['axios', 'permitio', 'pino']
  },
  runtimeConfig: {
    permitToken: process.env.PERMIT_TOKEN
  }
});
```

Après cela, Permit.io devrait être disponible pour votre code serveur dans Nuxt. Vous pouvez maintenant l'utiliser dans le code middleware pour vérifier les permissions.

## Comment contrôler l'accès à l'API avec le middleware Nuxt

En termes simples, le middleware est un code qui s'exécute avant un gestionnaire cible. Dans Nuxt, vous pouvez ajouter un middleware pour les endpoints API en créant les fichiers nécessaires dans un répertoire `middleware` contenu dans le répertoire `server` de niveau supérieur.

Puisque nous traitons des permissions, nous nommerons notre fichier middleware `permissions.ts`. Ici, vous vérifierez si un utilisateur est autorisé à effectuer une action sur une ressource donnée.

Permit.io facilite cela avec une simple méthode `.check` qui retourne un booléen indiquant si l'utilisateur est autorisé.

```typescript
await permit.check(user, action, resource);
```

Pour ce simple exemple de tableau de bord communautaire, notre code middleware essaiera d'abord de déterminer l'utilisateur et l'action à partir des propriétés de la requête. Le code exemple réalise cela de manière rudimentaire. Ils sont suffisants pour expliquer le concept et vous devriez utiliser des méthodes plus robustes conformes aux normes de l'industrie pour cela.

Après cela, dans le code exemple ci-dessous, nous construisons l'objet Permit en utilisant notre jeton permit et l'endpoint PDP (Policy-Decision-Point microservice) public par défaut. Le [Permit PDP est open-source.](https://github.com/permitio/PDP) Si vous le souhaitez, vous pouvez configurer votre PDP local/personnel en suivant les étapes [ici](https://docs.permit.io/how-to/deploy/deploy-to-production).

```typescript
import { Permit } from 'permitio';

export default defineEventHandler(async (event) => {
  // Ne vérifier les permissions que si la requête est une requête POST ou DELETE
  const { method, path } = event;
  if (method !== 'POST' && method !== 'DELETE') return;

  // Assurez-vous que l'en-tête d'autorisation est présent
  let authorization = event.node.req.headers['authorization'];
  if (!authorization) throw new Error('Non autorisé');

  // Extrait l'utilisateur de l'en-tête d'autorisation. Ceci est à des fins d'exemple
  // uniquement. Dans une application réelle, vous utiliseriez une bibliothèque JWT ou
  // de meilleures méthodes d'authentification dans votre API.
  const user = authorization.split(' ')[1];
  if (!user) throw new Error('Non autorisé');

  // Extrait la ressource du chemin. Ceci est à des fins d'exemple uniquement.
  let resource = path.split('/').reverse()[0]; // obtenir la dernière partie du chemin
  resource = resource.slice(0, -1); // supprime le 's' final
  // Met en majuscule la première lettre
  resource = resource.charAt(0).toUpperCase() + resource.slice(1);

  // Définit l'action sur la ressource à partir de la méthode de requête.
  // Ceci est à des fins d'exemple uniquement. Dans une application réelle, vous auriez
  // une méthode plus robuste pour déterminer l'action.
  const action = method === 'POST' ? 'create' : 'delete';

  // Construit l'objet Permit. Utilise le jeton de la configuration runtime.
  const config = useRuntimeConfig(event);
  const permit = new Permit({
    pdp: 'https://cloudpdp.api.permit.io',
    token: config.permitToken
  });

  // Vérifie si l'utilisateur est autorisé à créer la ressource.
  // Si ce n'est pas le cas, lance une erreur.
  const isPermitted = await permit.check(user, action, resource);
  if (!isPermitted) throw new Error('Non autorisé');
});
```

Comme vous pouvez le voir, si le vérificateur Permit échoue, une erreur sera lancée. Cela empêchera Nuxt de gérer les ressources non autorisées dans votre système. Une telle séparation des préoccupations est efficace, surtout en matière d'autorisation.

## Comment tester le RBAC dans le tableau de bord communautaire

La page des paramètres fonctionne avec le fichier `stores/permissions.ts` pour compléter le flux dans le front-end. Nous avons codé en dur les rôles et les « identifiants utilisateur » pour faciliter le basculement et les tests. Vous n'aurez certainement pas cela dans une application de production. Vous pouvez [intégrer CASL pour les vérifications de permissions dans un frontend](https://docs.permit.io/integrations/feature-flagging/casl/).

Dans ce tableau de bord communautaire de démonstration, les points de contact de l'interface utilisateur ne permettent les modifications des entités que si l'utilisateur agissant a les bons rôles. En d'autres termes, vous ne pouvez ajouter ou supprimer une entité que si le rôle actuel dans la page des paramètres le permet. Voyons cela en action.

Dans le tableau de bord Permit.io, créez trois utilisateurs de test : « example-member », « example-mentor » et « example-admin ». Attribuez les rôles respectifs à chaque utilisateur.

![Démo de la création d'utilisateurs de test et de l'attribution de rôles dans Permit.io](https://cdn.hashnode.com/res/hashnode/image/upload/v1732037709104/0cb7b666-8597-4839-802b-e79e0434572a.gif align="center")

Démarrez l'application Nuxt en exécutant `npm run dev`. Visitez `localhost:3000` dans votre navigateur et explorez l'autorisation basée sur les rôles dans le tableau de bord communautaire de démonstration.

Vous pouvez voir que lorsque vous définissez l'utilisateur actuel sur admin, vous pouvez créer et supprimer des annonces, mais lorsque vous le définissez sur invité, vous ne pouvez que consulter les entités et non les gérer. Avec cela, nous avons pleinement implémenté l'autorisation.

![Démo de test des rôles dans le tableau de bord communautaire](https://cdn.hashnode.com/res/hashnode/image/upload/v1732031066634/54310991-3ce9-4736-8735-c2776e4f6d82.gif align="center")

## Résumé

Vous pouvez être plus efficace dans la construction de votre application en vous concentrant sur la logique métier et en externalisant des parties cruciales comme l'autorisation.

Dans cet article, vous avez appris comment utiliser une solution d'autorisation (Permit.io) pour implémenter le contrôle d'accès basé sur les rôles dans un tableau de bord communautaire de démonstration avec Nuxt. Vous pouvez également utiliser Permit dans tout autre type d'application (pas seulement les tableaux de bord communautaires).

Lors de la planification de l'autorisation, définissez les ressources ainsi que les « actions » que les utilisateurs peuvent exécuter sur chaque ressource. Après cela, définissez les rôles comme les permissions que les utilisateurs peuvent avoir.

Santé !