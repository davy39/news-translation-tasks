---
title: Comment créer un contrôle d'accès évolutif pour votre application web [Guide
  complet]
date: '2025-02-04T19:26:37.559Z'
author: Samhitha Rama Prasad
authorURL: https://www.freecodecamp.org/news/author/samhitharamaprasad/
originalURL: https://freecodecamp.org/news/how-to-build-scalable-access-control-for-your-web-app
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738695897990/7a5962ce-9c4a-4e7c-bdeb-520dccc5d240.png
tags:
- name: React
  slug: reactjs
- name: permissions
  slug: permissions
- name: Security
  slug: security
- name: access control
  slug: access-control
- name: ABAC
  slug: abac
- name: casl
  slug: casl
seo_desc: Access control is crucial for preventing unauthorized access and ensuring
  that only the right people can access sensitive data in your application. As your
  app grows in complexity, so does the challenge of enforcing permissions in a clean
  and efficie...
---


Le contrôle d'accès est crucial pour empêcher les accès non autorisés et garantir que seules les bonnes personnes peuvent accéder aux données sensibles de votre application. À mesure que votre application gagne en complexité, le défi consistant à appliquer les autorisations de manière propre et efficace augmente également.

<!-- more -->

Dans ce guide, nous explorerons divers mécanismes de contrôle d'accès et détaillerons deux approches pour créer une solution de contrôle d'accès à base d'attributs (ABAC) évolutive dans React.

Tout d'abord, nous examinerons CASL, une bibliothèque d'autorisation open-source populaire. Ensuite, nous construirons une solution personnalisée à partir de zéro pour approfondir votre compréhension de la conception d'un système de validation d'autorisations flexible.

Ce guide comprend des démonstrations de code détaillées pour les deux approches, couvrant des concepts clés tels que la gestion d'état, les hooks personnalisés et la mise en cache/requêtes conditionnelles à l'aide de Redux Toolkit.

Si vous prévoyez d'implémenter le code, vous devriez avoir une compréhension de base du fonctionnement d'une application web utilisant la gestion d'état. Mais même si vous ne codez pas en même temps, vous obtiendrez des informations précieuses sur les design patterns et les meilleures pratiques derrière la création d'un système de validation d'autorisations robuste.

Plongeons dans le vif du sujet !

## Table des matières

-   [Qu'est-ce que le contrôle d'accès ? En quoi est-il différent de l'AuthZ, l'AuthN et des autorisations ?][1]
    
-   [Contrôle d'accès multicouche][2]
    
    -   [Poudlard en harmonie : une défense unifiée][3]
-   [Modèles de contrôle d'accès][4]
    
-   [Pourquoi l'ABAC ?][5]
    
-   [Le contrôle d'accès à base d'attributs en profondeur][6]
    
    -   [Composants de base][7]
        
    -   [Comment fonctionne l'ABAC ?][8]
        
    -   [Qui définit les politiques ABAC ?][9]
        
    -   [Où l'appliquer — back-end ou front-end ?][10]
        
    -   [Où sont définies les politiques ?][11]
        
-   [1 : Implémentation des autorisations avec CASL][12]
    
-   [2 : Construisez votre propre framework de validation d'autorisations personnalisé][13]
    
    -   [Définition de politique via la Politique en tant que Code][14]
        
    -   [Aperçu du flux de travail][15]
        
    -   [Validation de politique][16]
        
    -   [Application de la politique][17]
        
-   [Résumé][18]
    
    -   [Considérations supplémentaires sur l'évolutivité][19]
-   [Conclusion][20]
    

## Qu'est-ce que le contrôle d'accès ? En quoi est-il différent de l'AuthZ, l'AuthN et des autorisations ?

Laissez-moi décomposer ces termes en utilisant l'exemple d'un aéroport.

Lorsque vous arrivez au comptoir d'enregistrement, vous présentez votre passeport pour vérifier votre identité. L'**Authentification** (Qui êtes-vous ?) est le processus consistant à confirmer que vous êtes bien celui que vous prétendez être.

Une fois votre identité confirmée, la compagnie aérienne vérifie si vous êtes autorisé à monter à bord du vol en vérifiant votre billet, ou si vous êtes autorisé à accéder au salon en examinant votre statut de membre, votre classe de voyage ou votre niveau de programme de fidélité. L'**Autorisation** (Qu'êtes-vous autorisé à faire ?) consiste à déterminer les ressources spécifiques auxquelles vous êtes autorisé à accéder.

Les **Autorisations** (Quelles actions spécifiques pouvez-vous entreprendre ?) sont les détails granulaires de ce que vous êtes autorisé à faire dans le cadre de votre autorisation. Si vous êtes autorisé à monter à bord du vol et à accéder au salon, vos autorisations peuvent inclure : s'asseoir à la porte d'embarquement, se détendre dans le salon, faire des achats en duty-free ou, si vous êtes membre du personnel, accéder aux zones restreintes.

Le **Contrôle d'accès** fait référence aux mesures en place pour appliquer les politiques d'autorisation. Ce sont les règles que l'aéroport suit pour valider les cartes d'embarquement ou l'accès au salon, et pour vous guider vers la bonne porte.

## Contrôle d'accès multicouche

Pour garantir une protection complète, le contrôle d'accès doit être appliqué à plusieurs couches, en fonction de l'architecture de votre application.

Pour comprendre cela, voici une petite analogie pour mes collègues fans de Harry Potter :

### Poudlard en harmonie : une défense unifiée

À la limite même de Poudlard, vous avez votre Périmètre — les défenses extérieures qui tiennent les forces obscures à distance. Pensez-y comme aux hauts _murs de pierre enchantés_ qui entourent le château — agissant comme un pare-feu, avec des statues de sangliers ailés perchées sur les parapets, montant la garde. Seuls ceux qui ont l'autorisation appropriée sont autorisés à franchir les portes, garantissant qu'aucun invité indésirable, comme des mages noirs, ne puisse entrer.

Lorsque les étudiants arrivent à Poudlard, ils viennent par _bateaux ou par diligences tirées par des Sombrals_, qui sont les seuls moyens de transport de confiance. C'est comme l'**Endpoint Detection and Response (EDR)**, garantissant que seuls les bons appareils (ou diligences) sont autorisés à entrer.

Si un étudiant essaie d'utiliser un appareil non conforme (comme un _balai maudit ou la Transplanage_), il ne sera pas autorisé à entrer. La **Gestion des appareils mobiles (MDM)** agit comme le processus d'inspection magique — seuls les appareils qui répondent aux normes de Poudlard peuvent franchir la porte et se connecter aux systèmes de l'école.

À Poudlard, les _hiboux_ sont les messagers de confiance qui transportent les messages entre l'école et le monde extérieur. Ces hiboux, comme les clés API et les JWT, portent le sceau d'approbation et ne livrent des messages qu'aux bons destinataires. Les créatures sombres comme les _Détraqueurs_ ont l'interdiction de livrer des messages, garantissant que seules les bonnes communications passent.

La _lettre d'acceptation de Poudlard_ est comme un **token OAuth**. Elle prouve que vous appartenez au monde magique et vous donne accès à l'école sans avoir besoin de montrer votre visage ou de révéler votre statut de sang.

À l'intérieur du château, l'accès aux différentes zones est contrôlé par qui vous êtes et votre rôle à Poudlard. Par exemple, le **Contrôle d'accès basé sur les rôles (RBAC)** garantit que seuls les _Gryffondor_ peuvent accéder à leur salle commune, tandis que les _Serpentard_ ont la leur. Les _Préfets_ bénéficient de privilèges supplémentaires, comme l'accès à la salle de bain des préfets ou à d'autres pièces spéciales. Ces rôles définissent où vous pouvez aller et ce que vous pouvez faire dans le château.

Mais les choses deviennent plus nuancées avec le **Contrôle d'accès à base d'attributs (ABAC)**. Par exemple, seuls les étudiants inscrits au cours de _Soins aux créatures magiques_ ont accès à la Forêt Interdite, mais ils ne sont autorisés à y entrer que pendant la journée, quand c'est plus sûr. La forêt est trop dangereuse la nuit, et seuls ceux qui ont les bons attributs (comme un emploi du temps spécifique) peuvent y entrer au bon moment.

À l'intérieur de Poudlard se trouve la _Pierre Philosophale_, cachée dans un coffre-fort gardé par de puissants enchantements. C'est votre couche de données – les ressources les plus précieuses, sécurisées par de puissantes protections. Tout comme les autorisations de base de données, le coffre est protégé par Touffu, le chien à trois têtes, une série d'enchantements et de pièges. De même, la sécurité au niveau des lignes et des colonnes garantit que seul Harry Potter peut récupérer la Pierre parce qu'il est le seul digne (vous ne pouvez accéder qu'à ce qui vous est destiné).

En résumé,

1.  **Couche réseau (niveau infrastructure) :** Pare-feux et réseaux privés virtuels (VPN) pour contrôler le trafic réseau entrant et sortant.
    
2.  **Couche endpoint (niveau appareil) :** Endpoint Detection and Response (EDR) et Mobile Device Management (MDM) pour garantir que seul un appareil conforme peut accéder à votre application.
    
3.  **Couche API (niveau service) :** Clés API, JSON Web Tokens (JWT) et passerelles API pour authentifier et autoriser l'appelant et appliquer des politiques telles que la limitation de débit, la liste blanche d'IP, etc.
    
4.  **Couche application :** Là où réside généralement la logique métier principale pour l'autorisation (ce sur quoi porte ce guide).
    
5.  **Couche de données (niveau base de données) :** Autorisations de base de données, sécurité au niveau des lignes/colonnes.
    

## Modèles de contrôle d'accès

Au niveau de la couche application, trois modèles principaux de contrôle d'accès sont couramment utilisés en génie logiciel : le contrôle d'accès basé sur les rôles (RBAC), le contrôle d'accès à base d'attributs (ABAC) et le plus récent contrôle d'accès basé sur les relations (ReBAC).

Le **RBAC** **(Role-Based Access Control)** est un modèle où l'accès est accordé ou refusé en fonction des rôles attribués à un utilisateur.

Un rôle est une collection d'autorisations ou de privilèges qui définissent les actions qu'un utilisateur peut effectuer dans un système. Les rôles simplifient le contrôle d'accès en affectant les utilisateurs à des rôles prédéfinis, plutôt qu'en gérant les autorisations individuelles pour chaque utilisateur.

Lorsqu'un utilisateur se voit attribuer un rôle, il hérite automatiquement de toutes les autorisations associées à ce rôle. Chaque autorisation a également une portée (scope), qui définit les limites ou les contextes dans lesquels les autorisations du rôle s'appliquent. Les portées sont généralement utilisées pour restreindre l'accès à des ressources ou des données spécifiques.

Laissez-moi illustrer cela (et tous les concepts de ce guide) en utilisant une application de blog comme exemple. Cette application permet aux utilisateurs de créer, gérer et publier des articles de blog dans plusieurs catégories. Elle prend en charge divers rôles d'utilisateurs, chacun ayant différents niveaux d'accès au contenu et aux fonctionnalités de la plateforme.

-   **Admin** : Peut voir, modifier, supprimer et gérer tous les articles de blog et les rôles d'utilisateurs. (Portée : Tous les articles et utilisateurs)
    
-   **Éditeur** : Peut modifier et approuver des articles dans ses catégories assignées (par exemple, Tech, Lifestyle). (Portée : Catégories assignées)
    
-   **Auteur** : Peut créer et modifier uniquement ses propres articles de blog. (Portée : Propres articles)
    
-   **Utilisateur invité** : Peut voir les articles de blog publics et publiés mais ne peut pas accéder aux articles privés. (Portée : Articles publics publiés uniquement)
    

La relation entre les utilisateurs et les rôles est souvent de type plusieurs-à-plusieurs, et les rôles peuvent également être hiérarchiques, permettant des structures d'autorisation complexes.

![Schéma du contrôle d'accès basé sur les rôles](https://cdn.hashnode.com/res/hashnode/image/upload/v1737780482515/e30316f8-58a9-4595-81ba-8eb08b2d5a3d.jpeg)

L'**ABAC** **(Attribute-Based Access Control)** est un modèle où les décisions d'accès sont prises en fonction des attributs du sujet (utilisateur), de l'objet (ressource) et de l'environnement. Il évalue dynamiquement si un sujet peut effectuer une action sur un objet en fonction de ces attributs et des politiques qui les régissent.

Le **ReBAC** **(Relationship-Based Access Control)** est un modèle émergent qui accorde l'accès en fonction des relations entre les utilisateurs et les ressources. Par exemple, il pourrait permettre uniquement à l'utilisateur qui a créé un article de le modifier. Ce modèle est particulièrement utile dans les applications de réseaux sociaux, où l'accès dépend des relations entre utilisateurs (comme les amis, les abonnés ou la propriété du contenu).

## Pourquoi l'ABAC ?

Le RBAC offre plusieurs avantages, notamment la facilité d'implémentation, la réduction de la charge administrative en permettant l'intégration rapide de nouveaux utilisateurs et un audit simplifié, car il est facile de vérifier quels rôles ont accès aux données sensibles.

Mais, à mesure que la plateforme se développe, vous introduisez des exigences plus nuancées pour le contrôle d'accès. Ces nouvelles exigences mènent à la création de nouveaux rôles pour répondre à des besoins d'accès spécifiques :

1.  **Éditeur de publication** : Peut voir, modifier, approuver, publier et supprimer des articles dans toutes les catégories, mais ne peut pas gérer les rôles d'utilisateurs ou les paramètres.
    
2.  **Auteur junior** : Peut créer et modifier ses propres articles dans les catégories assignées.
    
3.  **Auteur senior** : Peut créer et modifier ses propres articles dans n'importe quelle catégorie.
    
4.  **Utilisateur (Abonné)** : Peut voir et commenter les articles privés en plus des articles publics.
    
5.  **Abonné Premium** : Possède toutes les autorisations d'un abonné régulier et l'accès aux articles exclusifs.
    

Rapidement, vous pourriez vous retrouver à gérer une liste sans cesse croissante de rôles tels que Éditeur Senior, Superviseur de Publication, Utilisateur Invité, Abonné, Abonné Premium, Graphiste, Designer UX, Photographe, Gestionnaire de Médias Sociaux, Spécialiste Marketing US, Spécialiste Marketing UK, Développeur Web, Analyste de Données, Gestionnaire d'Adhésion, Gestionnaire de Publicité, Conseiller Juridique et Gestionnaire de Sponsoring.

L'introduction d'exigences supplémentaires — telles que la catégorie du blog, l'ancienneté et la juridiction — peut rapidement conduire à une explosion des rôles. Imaginez comment cela évoluerait dans des applications d'entreprise gourmandes en données comme la finance ou la santé.

Bien que les portées fonctionnent bien lorsque les limites sont claires et statiques (par exemple, département, types de blog), elles nécessitent des vérifications personnalisées pour des attributs plus granulaires tels que l'ancienneté, la durée de service, l'heure de création du blog ou le statut de publication. Les portées ont également du mal à prendre en compte les attributs qui changent au fil du temps, comme le lieu ou l'heure de l'accès.

Parce que le RBAC repose sur des rôles et des portées fixes pour prendre des décisions d'accès, il devient limité dans la gestion de besoins d'accès complexes et dynamiques. C'est pourquoi l'[**OWASP** (Open Worldwide Application Security Project) recommande d'utiliser l'**ABAC** ou le **ReBAC** plutôt que le RBAC][21], car ils sont plus efficaces pour implémenter le principe du moindre privilège.

## Le contrôle d'accès à base d'attributs en profondeur

### Composants de base

Les composants de base de l'ABAC sont :

**Attributs** : Les attributs sont des paires clé-valeur utilisées pour définir le contexte d'accès. Les exemples incluent :

-   **Attributs utilisateur** : Ceux-ci décrivent les caractéristiques de la personne demandant l'accès, comme le rôle, le département, l'âge, le niveau d'habilitation, etc. 💡 Comme vous pouvez le voir, le rôle peut être l'un des attributs sur lesquels repose la décision de contrôle d'accès. Ainsi, l'ABAC est essentiellement une extension du RBAC.
    
-   **Attributs de ressource** : Ceux-ci décrivent les caractéristiques des ressources (telles que les fichiers, les bases de données ou les services) auxquelles on accède. Par exemple, le propriétaire, la catégorie, le statut, etc.
    
-   **Attributs d'action** : Ceux-ci définissent quelles actions sont demandées par l'utilisateur sur la ressource. Par exemple, l'accès `read` comme voir/ouvrir, l'accès `write` comme créer/modifier/supprimer, l'accès `execute` comme traiter/exécuter, etc.
    
-   **Attributs d'environnement** : Ceux-ci incluent des éléments contextuels tels que l'`heure` ou le `lieu` qui influencent le processus de prise de décision.
    

**Politiques** : Les politiques sont des règles logiques ou des déclarations qui définissent quelles combinaisons d'attributs autorisent ou refusent l'accès. Par exemple, un éditeur de publication peut _publier_ des articles approuvés dans les catégories assignées pendant les heures de bureau.

### Comment fonctionne l'ABAC ?

Prenons Sam, une éditrice de publication pour notre blog, comme exemple. Sam est autorisée à publier des articles qui ont été approuvés par l'éditeur, mais seulement dans les catégories qui lui ont été assignées, telles que « Tech », « Lifestyle » et « Santé ». Elle n'est autorisée à publier ces articles que pendant des heures spécifiques, par exemple de 9h à 18h.

Le rôle de Sam en tant qu'éditrice de publication et ses catégories assignées ont été définis lorsqu'elle a rejoint l'équipe. La ressource ici est l'Article (Post), auquel on attribue une catégorie lors de sa création. L'action qu'elle peut effectuer est de publier, et la condition environnementale est que cela doit être pendant les heures de bureau.

Puisque la règle de contrôle d'accès est basée sur les attributs de Sam — son rôle d'éditrice de publication et les catégories qui lui sont assignées — elle peut publier des articles dans ces catégories. Si l'un de ses attributs change, par exemple si elle passe à un autre département, comme la Gestion des Adhésions, ou si ses catégories assignées changent pour « Mode » ou « Voyage », son accès est automatiquement révoqué.

> _L'ABAC permet aux administrateurs de définir des contrôles d'accès sans avoir besoin de savoir spécifiquement qui aura besoin d'accès. À mesure que de nouveaux membres rejoignent une organisation, il n'est pas nécessaire de modifier les règles existantes ou les attributs d'objet ; tant qu'ils possèdent les attributs nécessaires, ils peuvent accéder aux ressources requises. Cette capacité à s'adapter automatiquement à des utilisateurs nouveaux et imprévus sans ajustements supplémentaires est un avantage clé de l'utilisation de l'ABAC_. ([Source][22])

### Qui définit les politiques ABAC ?

1.  **Administrateurs de gestion des identités et des accès** :
    
    Dans de nombreuses organisations, les administrateurs de sécurité ou les administrateurs de contrôle d'accès définissent les politiques ABAC. Leurs responsabilités incluent l'analyse des besoins de l'entreprise, la gestion des risques, la conformité réglementaire et la garantie que les utilisateurs disposent du bon niveau d'accès aux ressources. Ils traduisent les exigences de sécurité en politiques basées sur les différents attributs et conditions spécifiques à l'organisation.
    
2.  **Gestionnaires d'entreprise et de ressources** :
    
    Dans certains cas, les unités commerciales ou les chefs de département peuvent également contribuer à la définition des politiques. Ils comprennent les besoins opérationnels et sont les mieux placés pour indiquer comment les données doivent être consultées par leurs équipes.
    
    Par exemple, un gestionnaire d'adhésion pourrait définir des politiques régissant qui peut accéder aux articles de blog premium en fonction du statut d'abonnement, du rôle de l'utilisateur ou du niveau d'adhésion (par exemple, Abonné, Abonné Premium).
    

### **Où l'appliquer — back-end ou front-end ?**

Les politiques de contrôle d'accès doivent être appliquées à la fois sur le **front-end** et le **back-end**. Voici pourquoi :

**1.** **Application côté front-end**

-   **Retour instantané** : Lorsque vous appliquez des politiques ABAC sur le front-end, vous pouvez immédiatement afficher ou masquer des éléments (comme des boutons, des liens ou des menus) en fonction des attributs de l'utilisateur. Cela rend l'interface plus propre et aide les utilisateurs à comprendre immédiatement ce qu'ils peuvent ou ne peuvent pas faire.
    
-   **Interface utilisateur plus intelligente** : Vous pouvez éviter de montrer aux utilisateurs des options qu'ils ne devraient pas voir. Par exemple, masquer des fonctionnalités si l'utilisateur n'a pas le bon rôle ou les bonnes autorisations. Cela rend l'interface utilisateur plus intuitive et réactive.
    
-   **Charge serveur réduite** : En appliquant certaines restrictions d'accès dans le front-end, vous réduisez les requêtes inutiles vers le back-end, améliorant ainsi les performances de l'application et réduisant la charge sur vos serveurs.
    
-   **Couche de sécurité** : Bien que le front-end ne soit pas l'endroit où les données sensibles doivent résider, vous pouvez toujours ajouter une couche de sécurité supplémentaire en l'utilisant pour filtrer les actions ou contenus invalides **avant** qu'une requête ne soit faite au back-end. Par exemple, vous pouvez masquer des éléments d'interface sensibles (comme les contrôles d'administration) ou désactiver des boutons en fonction des attributs de l'utilisateur, ce qui rend plus difficile pour les utilisateurs non autorisés de tenter de déclencher certaines actions.
    

**2.** **Application côté back-end**

-   **Risque de contournement** : L'inconvénient de se fier uniquement au front-end est que les utilisateurs peuvent facilement le **contourner**. Avec les bons outils, ils peuvent manipuler le code front-end ou les requêtes réseau (en utilisant les outils de développement du navigateur ou des proxys API). C'est pourquoi l'application côté back-end est essentielle — elle garantit que les règles d'accès sont appliquées **côté serveur**, là où elles ne peuvent pas être altérées.
    
-   **Protection des données sensibles** : Le back-end est l'endroit où vos données sensibles sont stockées et traitées. En appliquant les politiques ABAC sur le serveur, vous garantissez que les utilisateurs non autorisés ne peuvent pas accéder, modifier ou même voir des informations sensibles. Pour éviter les fuites de données, vous devriez toujours filtrer le contenu sensible en fonction des autorisations de l'utilisateur et n'envoyer que le contenu pertinent au client.
    

Maintenant que vous savez que les politiques ABAC doivent être appliquées à la fois dans le front-end et le back-end, la question suivante est : **Où définissez-vous ces politiques ?**

En tant que développeur, vous pourriez penser : « _Si je connais les politiques définies par l'équipe de sécurité, je peux simplement les traduire en code pour le front-end et le back-end._ »

Par exemple, si la politique est que seuls les auteurs seniors peuvent approuver des blogs dans des catégories spécifiques, vous pourriez écrire quelque chose comme ceci :

**Exemple front-end (simplifié) :**

```
if (user.role === 'author' && user.seniority === 'senior' && user.categories.includes('Tech')) {
  showApprovalDashboard();
} else {
  hideApprovalDashboard();
}
```

**Exemple back-end (simplifié) :**

```
if (user.role === 'author' && user.seniority === 'senior' && user.categories.includes('Tech')) {
  return res.send(approvalDashboardData);
} else {
  return res.status(403).send('Forbidden: You do not have approval access for this category.');
}
```

Mais comment garantir la cohérence des politiques entre les deux couches de votre application sans dupliquer la logique ?

Que se passe-t-il lorsque vous devez introduire des conditions supplémentaires à cette politique, comme la prise en compte d'autres attributs utilisateur ou la combinaison d'autorisations avec des feature flags pour activer conditionnellement certaines fonctionnalités pour des utilisateurs spécifiques ?

Et si vos exigences varient pour chaque utilisateur, comme :

-   Afficher certains éléments d'interface uniquement pour les utilisateurs ayant un abonnement premium,
    
-   Bloquer un appel API pour un gestionnaire de médias sociaux en fonction d'attributs spécifiques,
    
-   Ou masquer une route entière pour les utilisateurs qui ne sont pas administrateurs ?
    

Sans une approche structurée, votre application devient un fouillis de déclarations if-else éparpillées dans tout le code source.

Lisez la suite pour trouver les réponses à ces questions !

### Où sont définies les politiques ?

Avant de plonger dans les détails de l'implémentation, laissez-moi revenir brièvement sur la question de la section précédente : où devriez-vous _définir_ les politiques ?

Lorsqu'il existe plusieurs façons d'accéder à un service – que ce soit via une application mobile, une application web ou d'autres plateformes – le back-end doit servir de source de vérité pour les définitions de politiques. Définir les politiques ABAC dans le back-end maintient la cohérence et la sécurité sur toutes les plateformes. Cela signifie que tous les clients interagissent avec le même ensemble de règles, réduisant ainsi les risques de divergences de politiques.

Ainsi, le back-end est l'endroit où vivent toutes les définitions de politiques, et il les met à disposition du front-end en cas de besoin. Le front-end applique ensuite ces décisions sur l'interface utilisateur. Mais n'oubliez pas, le back-end doit toujours appliquer ces politiques également.

Dans les sections suivantes, vous apprendrez deux approches pour implémenter le modèle de contrôle d'accès ABAC.

## 1 : Implémentation des autorisations avec CASL

[CASL][23] est une bibliothèque JavaScript isomorphe open-source qui facilite grandement la gestion des autorisations dans votre application grâce à son API simple et déclarative.

Cela signifie que vous pouvez utiliser CASL à la fois côté client (front-end) et côté serveur (back-end). C'est particulièrement intéressant pour les applications full-stack, car cela garantit la cohérence du contrôle d'accès. La même logique d'autorisation peut être appliquée dans toute votre application, peu importe d'où vient la requête.

Avec CASL, vous bénéficiez d'un **contrôle d'accès déclaratif**, ce qui signifie que vous définissez _ce qui_ est autorisé, plutôt que de vous soucier de _comment_ vérifier les autorisations. Cela rend votre code plus propre, plus lisible et plus facile à maintenir. Que vous masquiez des éléments d'interface dans le front-end ou que vous vous assuriez qu'un appel API est autorisé dans le back-end, CASL vous aide à appliquer les autorisations de manière cohérente dans toute votre application.

La meilleure partie ? Vous pouvez définir des autorisations à l'aide d'une syntaxe claire et expressive. Cela facilite la gestion de règles d'autorisation même complexes. Par exemple, vous pouvez contrôler ce qu'un utilisateur peut (ou ne peut pas) faire en fonction de son rôle, des ressources qu'il possède et d'autres facteurs.

Et ce n'est pas seulement pour React/React Native – ils fournissent également des packages de support pour [Angular][24], [Vue][25] et [Aurelia][26].

### Étape 1 : Installer CASL

Tout d'abord, installez CASL à l'aide d'un gestionnaire de paquets. J'ai utilisé la v6 pour les exemples de code.

```
npm install @casl/react @casl/ability
# ou
yarn add @casl/react @casl/ability
# ou
pnpm add @casl/react @casl/ability
```

### Étape 2 : Définir les capacités (abilities)

Dans CASL, considérez les « capacités » comme un ensemble de règles qui définissent les actions qu'un utilisateur peut ou ne peut pas effectuer sur des sujets spécifiques (comme « Posts » ou « Users »). Utilisons nos exemples précédents de l'application de blog. Pour simplifier, nous considérerons deux types d'utilisateurs : les **Admins** et les **Auteurs**.

-   Un Admin peut tout gérer.
    
-   Un Auteur peut créer et modifier ses propres articles dans les catégories assignées, mais il ne peut pas supprimer les articles publiés.
    

Maintenant, créez un fichier `defineAbilities.ts` pour définir les capacités de manière déclarative et de haut niveau en utilisant un DSL.

Commencez par définir les `Actions` qu'un utilisateur peut effectuer (par exemple, `create`, `read`, `update`, `delete`, `manage`) et les `Subjects` (les entités sur lesquelles les actions sont effectuées, telles que `‘User’`, `‘Post‘`, ou des objets comme `User` ou `Post`).

```
//defineAbilities.ts

type Actions = 'create' | 'read' | 'update' | 'delete' | 'manage';
type Subjects = 'User' | 'Post' | 'all' | User | Post
```

Ensuite, créez un type représentant la structure de vos capacités. Il combine les `Actions` et les `Subjects` pour créer un système de capacités clair et typé.

Le `PureAbility<[Actions, Subjects]>` signifie que le système de capacités saura quelles actions sont autorisées sur quels sujets. La fonction `createAppAbility` est utilisée pour créer une instance de capacité basée sur vos actions et sujets définis. Vous pouvez utiliser cette fonction pour créer des capacités spécifiques au rôle ou aux autorisations d'un utilisateur.

```
//defineAbilities.ts

import { CreateAbility, PureAbility, AbilityBuilder, createMongoAbility } from '@casl/ability';
// autres imports

type Actions = 'create' | 'read' | 'update' | 'delete' | 'manage';
type Subjects = 'User' | 'Post' | 'all' | Post | User

export type AppAbility = PureAbility<[Actions, Subjects]>
export const createAppAbility = createMongoAbility as CreateAbility<AppAbility>
```

Notez que `createMongoAbility` est uniquement utilisé pour prendre en charge des opérateurs simples du [langage de requête MongoDB][27], comme $in, $lte, $eq qui sont utilisés pour spécifier des conditions pour vos règles. Ne vous inquiétez pas – cela ne signifie pas que votre application doit utiliser MongoDB, ni que vous devez être familier avec le langage de requête. Vous pouvez également les ignorer entièrement et créer des opérateurs personnalisés.

Ensuite, définissez une fonction appelée `defineAbilityFor`, qui prend un objet `user` comme argument et renvoie une instance de capacité. L'objet `user` est censé avoir une propriété `role` (telle que 'admin' ou 'author') qui détermine les autorisations de l'utilisateur.

L'objet `userPermissions` associe chaque utilisateur à une fonction qui définit ses autorisations à l'aide des méthodes `can` et `cannot` fournies par `AbilityBuilder`. Cette approche passe mieux à l'échelle qu'un switch case à mesure que vous ajoutez des rôles.

```
//defineAbilities.ts

export default function defineAbilityFor(user: User) {
  const { can, cannot, build } = new AbilityBuilder(createAppAbility);
   const userPermissions = {
    admin: () => {
      // L'utilisateur Admin peut tout gérer
      can('manage', 'all');
    },
    author: () => {
      // L'Auteur peut créer des Posts mais ne peut pas les supprimer
      can('create', 'Post');
      cannot('delete', 'Post');
    },
    // Ajouter plus de rôles
  };

  // Appeler les autorisations associées à l'utilisateur, ou par défaut aucune autorisation.
  const permissions = userPermissions[user.role] || (() => {});
  permissions(); 

  return build();
}
```

Note : `manage` et `all` sont des mots-clés dans CASL où manage signifie n'importe quelle action et all signifie n'importe quel sujet.

Pour spécifier des conditions qui empêchent les utilisateurs de mettre à jour des articles qu'ils n'ont pas créés, de supprimer des articles publiés, et pour restreindre l'accès à certains champs, vous pouvez utiliser des **conditions** et des **champs**. CASL vous permet de définir des conditions spécifiques sur les autorisations via la propriété `subject`, qui représente l'objet, et la propriété `fields`, qui représente les propriétés de l'objet avec lesquelles l'utilisateur interagit.

Ajoutez des règles conditionnelles au fichier ci-dessus.

```

   author: () => {
      // L'Auteur peut créer des articles dans les catégories 'Tech' et 'Lifestyle'
      can('create', 'Post', { category: { $in: ['Tech', 'Lifestyle'] } });

      // L'Auteur peut mettre à jour le titre et la description des articles dont il est l'auteur
      can('update', 'Post', ['title', 'description'], { ownerId: user.id, status: 'draft' });

      // L'Auteur ne peut pas supprimer les articles qui ont un statut 'Published'
      cannot('delete', 'Post', { status: 'published' });
    },
```

Dans CASL, les règles directes (comme `can`) sont combinées à l'aide de `OR` et les règles inversées (comme `cannot`) et les conditions sont combinées à l'aide de `AND`. L'auteur :

-   peut créer des Posts dans ses catégories assignées `OR`
    
-   peut mettre à jour le titre/description des Posts qu'il possède `AND` qui sont à l'état Draft
    
-   `AND` ne peut pas supprimer les Posts publiés
    

Rappelez-vous, pour la même paire action/sujet, vous devez définir les règles `cannot` _après_ les règles `can`, sinon elles seront écrasées.

Lorsque vous traitez un objet `Post` qui possède un champ imbriqué `details` (par exemple, `details.author.name`, `details.metadata.tags`), vous pouvez utiliser les jokers `*` et `**` pour contrôler l'accès en fonction du niveau d'imbrication.

-   Le joker `*` correspond uniquement aux **champs de premier niveau** au sein d'un objet donné.
    
    Cela signifie qu'il accordera l'accès aux champs qui sont directement à l'intérieur de l'objet `details`, mais pas aux **champs imbriqués**.
    
-   Le joker `**` permet l'accès à **tous les champs**, y compris ceux profondément imbriqués, au sein de l'objet.
    
    Cela signifie qu'il accordera l'accès à chaque champ à l'intérieur de `details`, quelle que soit la profondeur de l'imbrication.
    

```
// donne accès à tous les champs imbriqués sous Post.details, peu importe leur profondeur
can('read', 'Post', ['details.**']) 

// donne accès uniquement aux champs de premier niveau (tels que details.body, details.author)
can('read', 'Post', ['details.*'])
```

Notez que `*` correspond à tous les symboles sauf le point (.)

L'instance de capacité dans `defineAbilities.ts` peut être utilisée pour appliquer les autorisations dans toute votre application. Ce fichier peut agir comme une bibliothèque partagée, de sorte que le front-end (par exemple : React) et le back-end (par exemple : Node.js) puissent accéder et utiliser la même logique d'autorisation.

Bien que l'`AbilityBuilder` fonctionne pour les autorisations définies à l'intérieur du système, si votre application reçoit des autorisations définies de l'extérieur sous forme d'objet JSON, comme :

```
[
  {
    action: 'read',
    subject: 'Post'
  },
  {
    inverted: true, // indique des règles cannot
    action: 'delete',
    subject: 'Post',
    conditions: { published: true }
  }
]
```

vous pouvez le passer directement au constructeur `Ability` comme suit :

```
  const defineAbilityFor = (permissions: (SubjectRawRule<any, any, MongoQuery<AnyObject>>)[]) => {
    return createMongoAbility<[Actions, Subjects]>(permissions);
  }

  export default defineAbilityFor;
```

L'utilisation du JSON pour définir les règles a également l'avantage supplémentaire de **réduire la taille du bundle de votre application** puisque vous n'avez pas besoin d'inclure des dépendances lourdes comme `AbilityBuilder` !

### **Étape 3 : Créer une instance de capacité pour l'utilisateur**

Après une authentification réussie par votre service de Login ou d'Authentification, vous récupérerez les données utilisateur ou les autorisations associées (selon l'approche choisie à l'étape 2) vers votre application et créerez une instance de capacité dans votre composant de connexion (ou similaire) comme suit :

```
// login.tsx

import defineAbiltyFor from './config/defineAbilities.js'

const LoginComponent = () => {
    // Récupérer les données utilisateur depuis l'API. Ensuite,
    const ability = defineAbilityFor(user)
}
```

### **Étape 4 : Fournir l'instance de capacité à toute l'application**

Les [Contextes][28] sont utilisés dans React pour partager des données entre les composants sans avoir à passer des props à travers l'arbre des composants. Ajoutez le code ci-dessous dans un fichier `can.ts` :

```
// can.ts

import {createContext} from 'react'
import {createContextualCan} from '@casl/react'

export const AbilityContext = createContext()
export const Can = createContextualCan(AbilityContext.Consumer)
```

Ceci crée un composant `Can`, que vous utiliserez à l'étape suivante pour déterminer si un utilisateur a les autorisations pour effectuer une action, sur la base des capacités passées via `AbilityContext`.

Ensuite, utilisez l'`AbilityContext` ci-dessus pour envelopper votre composant `App` et définissez l'instance `ability` créée à l'étape 3 comme `value`, afin que les capacités soient disponibles pour tous les composants de l'application.

```
ReactDOM.render(
<AbilityContext.Provider value={ability}>
  <App />
</AbilityContext.Provider>,
  document.getElementById('root')
)
```

### **Étape 5 : Vérifier les autorisations utilisateur à l'aide des capacités**

Il existe deux façons de déterminer si un utilisateur a l'autorisation d'effectuer une action : utiliser `ability.can` pour les vérifications programmatiques et utiliser le composant `Can` pour le rendu conditionnel.

Supposons que ceci soit votre objet post :

```
// post.ts

export interface Post {
    ownerId: string;
    category: string;
    title: string;
    description: string;
    status: string;
}
const post: Post = {
    ownerId: 'votreNomUtilisateur',
    category: 'Lifestyle',
    title: 'Mon premier article',
    description: 'Ceci est la description du premier article.',
    status: 'published'
};
```

`ability.can` et le composant `Can` prennent tous deux l'action, le sujet et un champ optionnel, et vérifient ces paramètres par rapport aux capacités définies.

```
// user-profile.tsx

import { useAbility } from '@casl/react';
import { subject } from '@casl/ability';
import { AbilityContext, Can } from '../config/can';
// autres imports

export default const UserProfile = () => {
  const ability = useAbility(AbilityContext);

  const canCreatePost = ability.can('create', 'Post'); //==== Exemple (1) ====
  const canDeletePost = ability.can('delete', post); //==== Exemple (2) ====

  return (
    <div>
      <h1>Profil Utilisateur</h1>

      {/* ==== Exemple (3) ==== */}
      <Can I="delete" a="Post">
        <p>Vous pouvez supprimer un Post.</p>
      </Can>

      {/* ==== Exemple (4) ==== */}
      <Can I="delete" this={subject('Post', post)}>
        {(allowed) =>
          allowed ? <button disabled={!allowed}>Supprimer le Post</button> 
          : <p>Impossible de supprimer l'article.</p>
        }
      </Can>
    </div>
  );
}
```

Voyez-vous à quel point la vérification d'autorisation est lisible ?

Regardons maintenant les quatre exemples.

L'exemple `(1)` renvoie true car l'utilisateur peut créer des articles.

L'exemple `(2)` devrait renvoyer true car vous pouvez supprimer vos articles publiés, **mais il renvoie** **false**. Pourquoi ? Parce que même si `post` est une instance de `Post`, CASL ne peut pas détecter son type de sujet (le type de l'objet `post`) car CASL utilise `object.constructor.modelName` ou `object.constructor.name` pour la détection du type de sujet.

Vous avez deux façons de corriger cela.

-   Utiliser un helper `subject` pour spécifier le type de l'instance `post` comme montré dans l'exemple `(4)` (il renvoie true)
    
-   Utiliser un algorithme de détection de type de sujet personnalisé pour indiquer quelle propriété CASL doit utiliser pour discerner le type. Cela peut être fait en utilisant `detectSubjectType` comme ceci :
    
    ```
      // defineAbilities.ts
    
      export default function defineAbilityFor(user: User) {
        const { can, cannot, build } = new AbilityBuilder(createAppAbility);
        // règles définies comme expliqué ci-dessus
    
        return build({
          detectSubjectType: object => object.__typename
        });
      }
    
       // post.ts
    
       const post: Post = {
          ownerId: 'votreNomUtilisateur',
          category: 'Lifestyle',
          title: 'Mon premier article',
          description: 'Ceci est la description du premier article.',
          status: 'published',
          __typename: 'Post'
      };
    ```
    

Désormais, l'exemple `(2)` devrait renvoyer true.

Ensuite, regardez l'exemple `(3)`. Il renvoie également true car la vérification porte sur le _type_ de sujet et non sur le sujet lui-même. Rappelez-vous, lorsque vous vérifiez sur un

> -   sujet, vous demandez « puis-je supprimer CE post ? »
>     
> -   type de sujet, vous demandez « puis-je supprimer UN article ? » (c'est-à-dire, au moins un post) ([Source][29])
>     

Bien que CASL offre une approche puissante pour le contrôle d'accès granulaire, il ne répond pas directement à notre besoin d'appliquer des conditions basées sur les attributs de l'utilisateur.

Bien que les bibliothèques tierces puissent offrir de la commodité, leur documentation est parfois peu claire, obsolète ou inexacte, et il peut y avoir des vulnérabilités au sein des composants eux-mêmes. Pour un contrôle total sur vos processus de sécurité, l'implémentation d'une logique d'autorisation personnalisée peut être nécessaire.

## 2 : Construisez votre propre framework de validation d'autorisations personnalisé

Pour construire un framework de validation personnalisé, examinons comment les politiques sont définies, validées et appliquées, et voyons comment toutes ces pièces s'assemblent.

### **Définition de politique via la Politique en tant que Code**

Vous avez déjà appris que vos politiques de contrôle d'accès devraient résider dans le back-end. Pour l'implémentation personnalisée, vous utiliserez la **Politique en tant que Code** (Policy as Code ou PaC). Cela fait référence à la pratique consistant à définir et à gérer les politiques à l'aide de code ou de fichiers de configuration (comme YAML, JSON ou DSL) plutôt que par des processus manuels ou de la documentation. Cela permet aux politiques d'être versionnées, appliquées automatiquement et plus fiables dans des environnements dynamiques. Ces politiques sont rédigées par l'administrateur de sécurité et sont gérées par un Service de Politique.

En YAML, votre politique peut ressembler à ceci, où la liste `policies` est représentée par une séquence (`-`).

```
policies:
  - policyId: P001
    resource: Post
    action: view
    effect: allow
    conditions: '(resource.tag != "exclusive") || (resource.tag == "exclusive" && user.role == "premium user")'
  - policyId: P002
    resource: Post
    action: edit
    effect: allow
    conditions: 'resource.ownerId == user.id'
  # autres politiques
```

Le **policyId** est un identifiant unique pour la politique. La **resource** spécifie le type de ressource auquel la politique s'applique, comme « Post ». L'**action** définit quelle opération est autorisée ou refusée sur la ressource, comme « edit ». L'**effect** détermine si l'action est autorisée ou refusée, avec des valeurs comme « allow » ou « deny ». Les **conditions** représentent l'expression logique qui doit être satisfaite pour que la politique s'applique, comme vérifier si l'ID du propriétaire de la ressource correspond à l'ID de l'utilisateur.

Comme vous pouvez le voir, les conditions dans les politiques sont dans un format lisible par l'homme, proche du TypeScript. C'est parce qu'elles sont écrites en utilisant le **Common Expression Language (CEL)** de Google.

CEL est un langage open-source, indépendant de la plateforme, rapide et sûr pour exécuter des expressions définies par l'utilisateur ([contrairement à `eval()`][30], surtout côté serveur). Ses performances sont accrues car CEL est compilé une fois en un arbre de syntaxe abstraite, qui est ensuite utilisé pour évaluer plusieurs entrées en nanosecondes ou microsecondes.

Redéfinissons la structure comme suit :

```
policies:
  Post:
    view:
      policyId: P001
      resource: Post
      action: view
      effect: allow
      conditions: '(resource.tag != "exclusive") || (resource.tag == "exclusive" && user.role == "premium user")'
    edit:
      policyId: P002
      resource: Post
      action: edit
      effect: allow
      conditions: 'resource.ownerId == user.id'
    publish:
      policyId: P003
      resource: Post
      action: publish
      effect: allow
      conditions: 'user.role == "publisher" && resource.category in ["Tech", "Lifestyle"] && resource.status == "approved" && system.time >= "09:00:00" && system.time <= "18:00:00"'

  Comment:
    create:
      policyId: C001
      resource: Comment
      action: create
      effect: deny
      conditions: 'user.role == "guest"'
    edit:
      policyId: C002
      resource: Comment
      action: edit
      effect: allow
      conditions: 'resource.authorId == user.id'
    delete:
      policyId: C003
      resource: Comment
      action: delete
      effect: allow
      conditions: 'resource.authorId == user.id || user.role in ["moderator", "admin"]'
  # autres politiques
```

Voici pourquoi :

1.  **Structure améliorée** : En regroupant les politiques par ressource et par action, vous facilitez grandement la navigation. L'ajout de nouvelles politiques ou actions devient un jeu d'enfant, sans perturber la configuration globale. Par exemple, si vous devez ajouter une action `archive` pour la ressource `Post`, vous l'ajoutez simplement sous l'objet `Post`. Cette approche modulaire rend la maintenance et l'extension des politiques beaucoup plus simples.
    
2.  **Recherche efficace** : Lorsque ces politiques sont accédées dans votre application sous forme d'objets JavaScript, les recherches sont efficaces et en temps constant (O(1)). C'est parce que les politiques sont stockées à l'aide de recherches par clé directe, où chaque politique peut être consultée instantanément par sa clé unique. Cela booste considérablement les performances par rapport à une recherche dans une liste (qui prendrait un temps O(n)). À mesure que le nombre de politiques augmente, votre temps de recherche reste le même, donc les performances ne ralentissent pas.
    
3.  **Audit et contrôle de version facilités** : Cette structure rend également l'audit et le contrôle de version beaucoup plus fluides. Vous pouvez facilement suivre les modifications apportées aux politiques et gérer les mises à jour sans risquer de perturber accidentellement d'autres politiques.
    

💡

Pour comprendre comment fonctionnent les littéraux de chaîne dans CEL pour les conditions ci-dessus, consultez quelques exemples [ici][31].

### Aperçu du flux de travail

Au démarrage de l'application, vous récupérez les politiques auprès du Service de Politique à l'aide de RTK Queries, qui les met automatiquement en cache dans votre cache RTK. Une fois l'utilisateur authentifié, ses données — comme son rôle et son département — seront également stockées dans le cache.

Pour faire persister ces données pendant la durée de la session, vous devrez les stocker dans le session storage, mais veillez à éviter de stocker des informations sensibles. Pour les besoins de notre validateur d'autorisations, nous lirons les données utilisateur directement depuis le cache.

Aux points où l'application de la politique est nécessaire, comme dans les composants ou les routes (appelons-les _points d'application de politique_), l'application appellera notre hook d'autorisation personnalisé. Ce hook valide ensuite les autorisations en fonction des politiques, de l'utilisateur, de la ressource et des attributs d'environnement pour accorder ou refuser l'accès à l'action demandée.

![Flux de travail du contrôle d'accès à base d'attributs](https://cdn.hashnode.com/res/hashnode/image/upload/v1737780571125/1dba1568-ee54-4bea-8d25-5c058fa6da68.jpeg)

### Validation de politique

#### Étape 1 : Créer un validateur d'autorisations

Commencez par définir les types pour `Action`, `Resource` et `Policy` dans votre code :

```
// validator.type.ts

export type Action = "view" | "edit" | "create" | "approve" | "publish" | "delete";
export type Resource = Partial<Post> | Partial<User> | Partial<Comment>;

export type PolicyEffect = "allow" | "deny"

export interface Policy {
  policyId: string;
  resource: string;
  action: string;
  effect: PolicyEffect;
  conditions: string;
}
```

Vous vous demandez peut-être pourquoi vous devez utiliser `Partial` ici. En utilisant `Partial`, nous disons que chaque champ de `Post`, `User` ou `Comment` n'est pas obligatoire lors de l'exécution de certaines actions. C'est particulièrement utile lorsque vous validez des actions de création, où l'objet peut ne pas être encore complètement formé – certains champs pourraient encore manquer. Par exemple, lors de la création d'un nouveau `Post`, vous pourriez n'avoir qu'un titre et un contenu, mais pas encore la liste complète des commentaires ou des tags.

Ensuite, installez `cel-js`, un évaluateur CEL pour JavaScript à utiliser dans votre validateur.

```
npm i cel-js
```

Créez une fonction `validatePermission` pour extraire les règles d'action pour la ressource donnée à partir de l'objet `policies` fourni et construire un contexte qui inclut les informations `user`, `resource` et `system`. Notez que vous devrez peut-être utiliser `__typename` (ou similaire) pour la détection du type de ressource, comme vous l'avez fait dans CASL.

En utilisant la bibliothèque `cel-js`, évaluez les `conditions` spécifiées dans les règles d'action, ce qui vérifiera si l'utilisateur répond aux critères requis pour l'action. Si les conditions sont satisfaites, la politique « prend effet », ce qui signifie que l'action spécifiée est appliquée selon l'effet défini – qu'il s'agisse d'autoriser ou de refuser l'action. Si aucune règle n'est définie ou si une erreur survient lors de l'évaluation, refusez par défaut.

```
// validator.ts

import * as cel from 'cel-js';
// autres imports

export const validatePermission = (
  action: Action,  
  resource: Resource,  
  system: System, 
  user: User,
  policies: { [resourceKey: string]: { [actionKey: string]: Policy } }
): boolean => {

  const actionRules = policies[resource.__typename]?.[action];
  if (!actionRules) return false; 

  try {
    const context = {
      user: user,  
      resource: resource,  
      system: system,  
    };

    return cel.evaluate(actionRules.conditions, context) && actionRules.effect === "allow";

  } catch (error) {
    console.error('Erreur lors de l\'évaluation de la condition d\'autorisation :', error);
    return false;
  }
};
```

Tout composant devant valider l'autorisation d'un utilisateur pour une action nécessite de récupérer les politiques dans le cache et de récupérer l'utilisateur dans l'état global, tout en gérant les états de chargement et d'erreur.

Pour éviter cette duplication de code et encapsuler la logique de ces opérations, vous pouvez créer un hook personnalisé qui fournit une interface cohérente pour la validation des autorisations entre les composants.

#### Étape 2 : Créer un hook personnalisé pour encapsuler la logique réutilisable

Puisque les politiques ont déjà été récupérées auprès du service de gestion des politiques lors du démarrage de l'application, la même RTK Query les récupérera désormais directement depuis le cache. Suivez la référence ci-dessous pour créer un hook personnalisé `usePermission`.

Remarquez comment la condition `skip: !userId` est utilisée pour garantir que les politiques ne sont récupérées que si un `userId` valide est présent, évitant ainsi des requêtes réseau inutiles.

```
// usePermission.ts

import { useSelector } from 'react-redux';
import { useGetPoliciesQuery } from './services/api'; 
import { validatePermission } from './validator';
// autres imports

export const usePermission = (action: Action, resource: Resource, system: System): boolean => {

  const user = useSelector((state: any) => state.user); 

  const { data: policies, isLoading: isPoliciesLoading, isError: isPoliciesError } = useGetPoliciesQuery({
    skip: !userId,
  });

  if (isPoliciesError || !policies) {
    console.error('Échec de la récupération des politiques');
    return false;
  }

  const hasPermission = validatePermission(action, resource, system, user, policies);

  return hasPermission;
};
```

#### Étape 3 : Ajouter une validation d'action contextuelle

Le plus souvent, même si un utilisateur dispose de l'autorisation requise pour effectuer une action, il peut toujours ne pas être autorisé à le faire en raison d'une logique métier contextuelle. Par exemple :

-   **Approbation d'article** : Un éditeur peut avoir l'autorisation d'approuver un article, mais s'il est en train de le modifier et qu'il y a des modifications non enregistrées, le bouton d'approbation doit être masqué.
    
-   **Commentaires** : Le bouton de commentaire doit être désactivé si un utilisateur n'a rien tapé, même s'il a l'autorisation de commenter.
    
-   **Création de catégorie** : Un utilisateur disposant de l'autorisation pourrait toujours être empêché de créer une catégorie si le nom est vide ou existe déjà.
    

Ces règles dépendent de l'état actuel de l'application et doivent être gérées dynamiquement. Pour gérer ces actions contextuelles, les règles de validation doivent être définies en fonction de l'état actuel de l'application (par exemple, l'article en cours de modification, le contenu en cours de saisie, la disponibilité du nom de la catégorie).

Avant d'approfondir la manière dont les hooks personnalisés peuvent gérer ces validations, définissons d'abord les règles pour ces actions contextuelles :

```
// contextualRules.ts

import _ from 'lodash';
// autres imports

const contextualActionRules = {
  Post: {
    approve: (state: PostState, resource: Resource) => {
      // Empêcher l'approbation si l'article est en cours de modification
      const postId = resource?.id;
      return postId && !state[postId]?.isEditing;
    },
  },
  Comment: {
    create: (state: CommentState, resource: Resource) => {
      // Empêcher la création d'un commentaire si le contenu du commentaire est vide
      return !_.isEmpty(resource?.content);
    },
  },
  Category: {
    create: (state: CategoryState[], resource: Resource) => {
      // Empêcher la création d'une catégorie si le nom est vide ou existe déjà
      const categoryName = resource.name?.trim();
      return (
        !_.isEmpty(categoryName) &&
        !state.some(category => category.name === categoryName)
      );
    },
  },
};
```

Maintenant, mettez à jour le hook `usePermission` pour incorporer les vérifications des `contextualActionRules`. Si une règle contextuelle est définie pour la `resource` et l'`action` spécifiées, elle sera évaluée parallèlement à l'autorisation basée sur la politique en utilisant l'`state` actuel de l'application. Si aucune règle contextuelle n'est trouvée, le hook renverra le résultat basé uniquement sur l'autorisation de la politique.

```
// usePermission.ts

export const usePermission = (action: Action, resource: Resource, system: System): boolean => {

  const state = useSelector((state: RootState) => state);

  /**
    Cette partie du code est la même que ci-dessus
  **/ 

  const hasPermission = validatePermission(action, resource, system, user, policies);
  const validateContextualRule = contextualActionRules[resource?.__typename]?.[action];

  if (validateContextualRule) {
    const contextualActionAllowed = validateContextualRule(state, resource);
    return hasPermission && contextualActionAllowed;
  }

  return hasPermission;
};
```

Il y a une chose qui doit **absolument** être modifiée dans le code ci-dessus. Devinez quoi ?

**En quoi** `usePermission` **est-il bénéfique pour les validations contextuelles basées sur l'état de l'application ?** Parce que le hook est abonné à l'état de l'application ! Ainsi, lorsque quelque chose change – comme la saisie dans une zone de commentaire – le hook se re-render. Puisque le composant Commentaire s'appuie sur ce hook pour contrôler l'état du bouton de commentaire, toute mise à jour dans le hook déclenche également un re-render du composant. Cela signifie qu'à mesure que vous tapez, le bouton devient visible, et si le contenu est effacé, le bouton est désactivé.

Mais nous ne voulons pas que le hook `usePermission` se re-render _chaque_ fois que l'état de l'application change. Corrigeons cela.

Définissez `resourceToStateMap` en dehors du hook `usePermission` pour éviter une recréation redondante à chaque appel. `useSelector` s'abonne uniquement à la tranche d'état pertinente en fonction du type de ressource et de l'ID.

```
// Mauvaise pratique : Au lieu de cela,
const state = useSelector((state: RootState) => state);

// Bonne pratique : Faites ceci
const resourceToStateMap: Record<string, (state: RootState, id: string | number) => any> = {
  Post:     (state, id) => state.posts[id],
  Comment:  (state, id) => state.comments[id],
  User:     (state, id) => state.user,
  // Ajoutez-en plus 
};

const resourceType = resource?.__typename;
const resourceId = resource?.id;
const stateSlice = useSelector((state: RootState) => {
  if (resourceType && resourceId && resourceToStateMap[resourceType]) {
    return resourceToStateMap[resourceType](state, resourceId);
  }

  return null;
});
```

C'est pourquoi il est important de rendre les sélecteurs aussi granulaires que possible.

-   **Éviter le sur-fetching** : Vous ne sélectionnez plus l'état entier, juste la partie nécessaire pour évaluer l'autorisation et les règles contextuelles. C'est beaucoup plus efficace, surtout dans les grandes applications.
    
-   **Re-renders optimisés** : Avec une sélection d'état granulaire, seule la tranche d'état pertinente déclenchera un re-render, améliorant les performances de l'application, surtout lorsque de nombreux composants utilisent le hook `usePermission`.
    

Maintenant que vous avez terminé l'essentiel de la logique de validation des autorisations, rendons son utilisation plus élégante.

#### Étape 4 : Créer un wrapper pour le rendu conditionnel

Créez un composant `Can` qui vérifie si l'utilisateur a l'autorisation d'effectuer une action spécifique sur une ressource à l'aide du hook `usePermission`. Si l'autorisation est accordée, il rend les `children` ou les appelle en tant que fonction avec le statut d'autorisation (cela sera utilisé pour désactiver les boutons). Sinon, il affiche un élément de secours (fallback).

```
// Can.tsx

import { usePermission } from '../hooks/usePermission';

export interface CanProps {
  I: Action;
  a: Resource;
  context: System;
  fallback?: React.ReactNode; 
  children: React.ReactNode | ((allowed: boolean) => React.ReactNode); 
}

const Can: React.FC<CanProps> = ({
  I,
  a,
  context,
  fallback = null,
  children,
}) => {
  const hasPermission = usePermission(I, a, context);

  // Si `children` est une fonction, l'appeler avec `hasPermission`
  if (typeof children === 'function') {
    return <>{children(hasPermission)}</>;
  }

  // Sinon, rendre les enfants ou le fallback
  if (hasPermission) {
    return <>{children}</>;
  }

  return <>{fallback}</>;
};

export default Can;
```

### Application de la politique

Vous pouvez utiliser le hook `usePermission` pour les vérifications programmatiques et le composant `Can` pour le rendu conditionnel.

**1\. Utiliser** `Can` **pour masquer/afficher des composants**

```
<Can
  I="approve"
  a={post}
  context={system}
  fallback={<p>Vous n'avez pas accès pour supprimer un commentaire.</p>}
>
  <YourComponent />
</Can>
```

**2\. Utiliser** `Can` **pour désactiver des composants**

```
<Can
  I="delete"
  a={comment}
  context={system}
>
  {(allowed) => (
     <button onClick={deleteComment} disabled={!allowed}>
       Supprimer le commentaire
     </button>
   )}
</Can>
```

**3\. Utiliser** `usePermission` **pour créer des routes protégées**

```
// ProtectedRoute.tsx

import { Navigate, Outlet } from 'react-router-dom'

export function ProtectedRoute() {
  const hasPermission = usePermission("view", user, context);

  return hasPermission ? <Outlet /> : <Navigate to='/login' />
}

// Configuration des routes
<Route element={<ProtectedRoute />}>
  <Route path='/' element={<Admin />} />
</Route>
```

**4\. Utiliser** `usePermission` **pour ignorer des appels API**

```
const hasPermission = usePermission("view", user, context);

const { data: user, isLoading: isUserLoading, isError: isUserError } = useUserQuery({
    skip: !hasPermission,
});
```

C'est tout ! Concluons par un bref résumé.

## Résumé

Dans ce guide, vous avez appris à implémenter un contrôle d'accès évolutif en utilisant à la fois CASL et une solution personnalisée. Nous avons commencé par explorer différents modèles de contrôle d'accès, en nous concentrant sur l'ABAC, et nous avons examiné deux façons d'appliquer des règles basées sur l'ABAC.

Avec CASL, vous avez vu à quel point il est facile de définir les capacités des utilisateurs, que vous utilisiez une bibliothèque partagée ou des autorisations externes. Nous avons détaillé comment configurer le contrôle d'accès pour diverses actions utilisateur, le tout avec un code propre et lisible. Vous avez également appris à ajouter des fonctionnalités avancées telles que des conditions dynamiques et un accès au niveau des champs pour un contrôle encore plus granulaire.

D'un autre côté, vous avez également appris à construire un framework d'autorisation personnalisé adapté aux besoins spécifiques de votre application. Vous avez combiné des vérifications contextuelles basées sur l'état avec des règles basées sur les politiques, créant ainsi un système de contrôle d'accès flexible et évolutif. En chemin, vous avez exploré des concepts tels que la Politique en tant que Code, CEL (Common Expression Language), les hooks personnalisés, la mise en cache et la récupération conditionnelle à l'aide des requêtes RTK. Vous avez également vu comment appliquer le contrôle d'accès sur les composants, les routes protégées, et plus encore.

Les deux approches partagent des avantages clés :

-   **Dynamique et évolutif** : L'ajout de nouvelles actions ou entités est aussi simple que la mise à jour d'un seul fichier – aucune réécriture de code n'est requise.
    
-   **Séparation des préoccupations** : Maintient la logique de validation séparée des composants de l'interface utilisateur, ce qui rend votre code plus facile à maintenir.
    
-   **Lisible** : Vous pouvez définir des autorisations en utilisant un langage simple et conversationnel comme « _Puis-je lire cet article ?_ » ou « _Puis-je créer un commentaire ?_ »
    
-   **Composants réutilisables** : Vous pouvez réutiliser les composants wrappers et les hooks dans toute votre application pour réduire la duplication.
    
-   **Réactivité de l'état** : Fonctionne de manière transparente avec l'état de React, garantissant que vos règles de contrôle d'accès sont reflétées dynamiquement dans votre interface utilisateur.
    

### **Considérations supplémentaires sur l'évolutivité**

 Si votre charge utile de politique est lourde ou si la logique de validation est coûteuse en calcul, envisagez les optimisations suivantes :

-   **Mémoïser la sortie** : Utilisez `useMemo` pour mettre en cache le résultat de calculs coûteux, mais gardez à l'esprit que `useMemo` lui-même peut être coûteux s'il est surutilisé.
    
-   **Modulariser les politiques** : Décomposez vos politiques en fichiers séparés en fonction de leur domaine. Ne récupérez que les politiques essentielles au démarrage et chargez les politiques non essentielles à la demande (lazy loading).
    
-   **Déporter la validation vers le backend** : Déplacez la logique de validation des politiques vers le backend et envisagez le rendu côté serveur (SSR). Mais n'oubliez pas que certaines vérifications dynamiques doivent toujours avoir lieu sur le frontend.
    

N'oubliez pas d'implémenter également le contrôle d'accès sur le back-end et assurez-vous de filtrer les données sensibles avant de les envoyer au client !

## Conclusion

Que vous choisissiez CASL pour sa simplicité et sa puissance ou que vous implémentiez votre propre solution personnalisée pour plus de flexibilité, vous disposez désormais des outils et des connaissances nécessaires pour intégrer le contrôle d'accès dans vos applications React, garantissant ainsi que vos utilisateurs ne peuvent accéder qu'à ce qu'ils sont autorisés à voir.

Si vous avez aimé lire ceci (ou même si ce n'est pas le cas ;)), envoyez-moi un message sur [LinkedIn][32] avec vos commentaires.

Bon codage, et que les autorisations de votre application soient aussi évolutives que votre base d'utilisateurs !

[1]: #heading-qu-est-ce-que-le-controle-d-acces-en-quoi-est-il-different-de-l-authz-l-authn-et-des-autorisations
[2]: #heading-controle-d-acces-multicouche
[3]: #heading-poudlard-en-harmonie-une-defense-unifiee
[4]: #heading-modeles-de-controle-d-acces
[5]: #heading-pourquoi-l-abac
[6]: #heading-le-controle-d-acces-a-base-d-attributs-en-profondeur
[7]: #heading-composants-de-base
[8]: #heading-comment-fonctionne-l-abac
[9]: #heading-qui-definit-les-politiques-abac
[10]: #heading-ou-l-appliquer-back-end-ou-front-end
[11]: #heading-ou-sont-definies-les-politiques
[12]: #heading-1-implementation-des-autorisations-avec-casl
[13]: #heading-2-construisez-votre-propre-framework-de-validation-d-autorisations-personnalise
[14]: #heading-definition-de-politique-via-la-politique-en-tant-que-code
[15]: #heading-apercu-du-flux-de-travail
[16]: #heading-validation-de-politique
[17]: #heading-application-de-la-politique
[18]: #heading-resume
[19]: #heading-considerations-supplementaires-sur-l-evolutivite
[20]: #heading-conclusion
[21]: https://en.wikipedia.org/wiki/OWASP
[22]: https://www.optiq.ai/blog-post/what-is-attribute-based-access-control-explained
[23]: https://casl.js.org/v6/en
[24]: https://casl.js.org/v6/en/package/casl-angular
[25]: https://casl.js.org/v6/en/package/casl-vue
[26]: https://casl.js.org/v6/en/package/casl-aurelia
[27]: https://www.mongodb.com/docs/manual/reference/operator/query/
[28]: https://react.dev/reference/react/createContext
[29]: https://casl.js.org/v6/en/guide/intro
[30]: https://owasp.org/www-community/attacks/Direct_Dynamic_Code_Evaluation_Eval%20Injection
[31]: https://stackblitz.com/edit/github-b9k23yjf-kbho9jtj?file=demo.ts
[32]: https://www.linkedin.com/in/samhitharamaprasad/