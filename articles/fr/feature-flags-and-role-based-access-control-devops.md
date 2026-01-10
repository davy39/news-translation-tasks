---
title: Comment les Feature Flags et le Contrôle d'Accès Basé sur les Rôles peuvent
  aider à sécuriser votre processus DevOps
subtitle: ''
author: Kayode Adeniyi
co_authors: []
series: null
date: '2024-04-22T21:26:27.000Z'
originalURL: https://freecodecamp.org/news/feature-flags-and-role-based-access-control-devops
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/pete-alexopoulos-IssFEVzKV1w-unsplash.jpg
tags:
- name: Devops
  slug: devops
- name: Security
  slug: security
seo_title: Comment les Feature Flags et le Contrôle d'Accès Basé sur les Rôles peuvent
  aider à sécuriser votre processus DevOps
seo_desc: "These days, software is being developed and deployed at a very rapid pace.\
  \ It makes it easy to understand how the saying “move fast and break things” became\
  \ commonplace. \nIn an era where agile development is the go-to practice for quick\
  \ feature relea..."
---

De nos jours, les logiciels sont développés et déployés à un rythme très rapide. Cela permet de comprendre facilement comment le dicton "move fast and break things" est devenu courant.

À une époque où le développement agile est la pratique de référence pour des mises en production rapides de fonctionnalités et des retours, il est facile de négliger la sécurité et la conformité. Cela peut concerner la sécurisation des pipelines CI/CD, la protection des données utilisateur, ou la gestion de l'accès aux feature flags dans les environnements de production.

Bien que le secteur technologique sache que des mesures de sécurité solides et des pratiques de conformité sont essentielles dans le DevOps, parfois ces mesures passent au second plan derrière le besoin de livrer du code en production.

Pour cette raison, il est crucial que vous compreniez l'importance de la sécurité et de la conformité dans le DevOps. Vous devriez également apprendre comment votre équipe peut tirer parti de concepts de sécurité populaires comme le Contrôle d'Accès Basé sur les Rôles (RBAC), ce sur quoi nous allons nous concentrer ici.

Cela est utile non seulement pour les équipes DevOps (comme une pratique conforme pour assigner l'accès aux équipes), mais aussi comme une fonctionnalité complète que les plateformes SaaS telles que [Flagsmith](https://www.flagsmith.com) (une plateforme open source de feature flagging) offrent à leurs clients.

Mais vous pourriez demander – pourquoi le RBAC est-il important ? Eh bien, nous allons couvrir cela et plus encore dans ce tutoriel.

## Table des Matières :

1. [Pourquoi le RBAC est-il important ?](#heading-pourquoi-le-rbac-est-il-important)
2. [Feature Flagging et Flagsmith](#heading-feature-flagging-et-flagsmith)
3. [Comprendre les Utilisateurs, Groupes, Rôles et Permissions](#heading-comprendre-les-utilisateurs-groupes-roles-et-permissions)
   – [Créer le projet](#heading-creer-le-projet)
   – [Créer le groupe](#heading-creer-le-groupe)
   – [Créer un rôle Éditeur](#heading-creer-un-role-editeur)
   – [Assigner des permissions au rôle Éditeur](#heading-assigner-des-permissions-au-role-editeur)
   – [Assigner le rôle Éditeur à un groupe](#heading-assigner-le-role-editeur-a-un-groupe)
   – [Tester les permissions assignées](#heading-tester-les-permissions-assignees)
4. [Cas d'Usage : le Chaos chez "NetGlobal Solutions"](#heading-cas-dusage-le-chaos-chez-netglobal-solutions)
   – [Comment atténuer le problème](#heading-comment-attenuuer-le-probleme)
5. [Comment établir un processus DevOps standard](#heading-comment-etablir-un-processus-devops-standard)
6. [Conclusion](#heading-conclusion)

## Pourquoi le RBAC est-il important ?

Pour faire simple, le contrôle d'accès basé sur les rôles est une exigence fondamentale pour le DevOps. Si vous n'implémentez pas le RBAC, les données de vos utilisateurs sont beaucoup plus exposées à des risques de compromission. Cela peut entraîner des pertes financières et nuire à la réputation de votre site.

Ainsi, pour réduire la surface d'attaque et éviter les dommages, les équipes DevOps devraient utiliser tous les mécanismes de sécurité à leur disposition, [comme le RBAC](https://www.redhat.com/en/topics/security/what-is-role-based-access-control). Le RBAC est exactement ce à quoi il ressemble : donner aux membres d'une équipe des permissions basées sur le rôle qu'ils jouent au sein de l'organisation.

Cela aide à sécuriser non seulement le cycle de vie d'une fonctionnalité mise en production, mais aussi la manière dont elle est gérée après la mise en production – doit-elle être activée ou désactivée ? Quels utilisateurs devraient pouvoir l'utiliser ? Et qui sera responsable de cette opération ?

C'est là que le feature flagging et le besoin d'une plateforme qui gère ces préoccupations de sécurité entrent en jeu.

Qu'est-ce que le feature flagging et pourquoi le RBAC est-il important pour le gérer ?

## Feature Flagging et Flagsmith

Le feature flagging est un concept de développement logiciel qui consiste à activer ou désactiver une fonctionnalité indépendamment des redéploiements ou des modifications du code source.

Les [feature flags](https://www.martinfowler.com/articles/feature-toggles.html) sont des instructions conditionnelles dans le code de l'application qui déterminent quelle section de code exécuter à l'exécution en fonction d'une valeur booléenne. Ils aident à déployer de nouvelles fonctionnalités en production et offrent un contrôle granulaire sur leur visibilité pour une base d'utilisateurs ou un environnement de déploiement.

Vous pouvez configurer les valeurs des feature flags par diverses méthodes, telles que des fichiers de configuration, des en-têtes de requête, ou à partir de la base de données. Cela signifie qu'il y a une certaine intervention nécessaire des développeurs dans ce processus. Et toute personne ayant accès au code ou à la base de données peut activer ou désactiver une fonctionnalité en production.

Bien que les entreprises aient des pratiques de conformité pour gérer le feature flagging, il y a toujours un risque que quelqu'un fasse quelque chose qui pourrait nuire à la production (intentionnellement ou non).

Ainsi, pour vous et votre équipe, une meilleure visibilité et un contrôle fin sur le basculement des fonctionnalités, des outils de feature flagging tels que Flagsmith vous aident à résoudre ces problèmes de sécurité et de permission.

Mais vous pourriez vous demander – comment Flagsmith gère-t-il les permissions et les utilisateurs ? Voici le **[RBAC](https://www.flagsmith.com/role-based-access-change-control-security)**, qui est intégré à l'ensemble d'outils Flagsmith. Cela facilite la collaboration entre les grandes équipes sur des projets et des environnements, et permet aux entreprises de gérer l'accès. Approfondissons pour comprendre comment cela fonctionne.

## Comprendre les Utilisateurs, Groupes, Rôles et Permissions

Flagsmith a deux rôles principaux dans le système RBAC : administrateur d'organisation et utilisateurs simples.

Les administrateurs d'organisation bénéficient du privilège d'avoir des capacités de superutilisateur, tandis que les utilisateurs réguliers nécessitent une permission explicite pour accéder aux ressources nécessaires. Flagsmith vous permet également de contrôler les permissions pour de nombreux utilisateurs dans un groupe. Cela facilite la gestion de l'accès pour les grandes équipes qui sont divisées en fonction des responsabilités.

Il existe également certains rôles dans le RBAC de Flagsmith qui peuvent avoir un ensemble de permissions attaché. Cela permet aux personnes ayant ces rôles d'accéder à des fonctionnalités particulières de Flagsmith.

Les rôles sont particulièrement utiles lorsque vous devez assigner des permissions en masse à un groupe. Dans ce cas, vous pouvez créer un rôle, assigner des permissions, et l'attacher à un groupe.

Si nous examinons les permissions à un niveau macro, nous pouvons voir que Flagsmith a divisé l'ensemble des permissions en trois niveaux différents : Organisation, Projet et Environnement.

Par exemple, nous pouvons gérer les ensembles de permissions pour les utilisateurs afin de créer des projets au niveau organisationnel. Au niveau du projet, nous pouvons obtenir l'accès à la création d'environnements, aux journaux d'audit, et à la gestion des fonctionnalités et des segments. Enfin, nous pouvons gérer les feature flags, les segments, les identités, et plus encore au niveau de l'environnement.

Avant de passer à une étude de cas, créons un projet arbitraire sur Flagsmith et donnons des permissions à un utilisateur afin qu'il puisse commencer à créer des feature flags pour le projet. Nous allons effectuer les actions suivantes :

* Créer un projet au sein d'une organisation
* Créer un groupe "front_end_devs" et ajouter des utilisateurs à ce groupe
* Créer un rôle éditeur
* Assigner des permissions au niveau organisationnel, projet et environnement
* Assigner le rôle au groupe nouvellement créé
* Se connecter avec le compte utilisateur pour tester les permissions assignées

### Créer le Projet

Cliquez sur le bouton Créer un Projet après vous être connecté avec un compte propriétaire. Nous nommerons ce projet **Dev Test.**

![Image](https://lh7-us.googleusercontent.com/Gk4FaR8EecQ2vlUipL3KiIVENZnQuEkTX9n0FL9szgQJuHzXuZEfduIQ2oYnDst46yc0zVAubcgq0i0L32Q12jNEsbcIQep9X_5sVde_tXgJ8OcCbOCZOHDm3ThruWbEHZBXo2E9G7hiE0CpJgfiECM)
_Créer le projet_

### Créer le Groupe

Accédez à l'onglet **Membres**, cliquez sur Créer un Groupe, puis remplissez les détails requis.

![Image](https://lh7-us.googleusercontent.com/gGa6rP_qH9pyoOL0vh3T5euQfpDUq7gmoPGnEJfBzlynt8rc1vTmfErCfgidTZrLfVCMeMhor69wrJKzqdqZpOx_bC6T2Wp9hkCo93zZvXElCplrgpCT6k-n9N8jq6nd9Ov7cwK3bLPvVk3aPn7tpWs)
_Entrez les informations pour créer un groupe_

Nous avons créé un groupe "**front_end_devs**" et fait de John Smith l'administrateur du groupe. Considérez cela comme une permission en ligne lors de la création d'un groupe. John peut maintenant gérer les utilisateurs à l'intérieur de ce groupe.

### Créer un Rôle Éditeur

Cliquez sur **Rôles** à côté de **Groupes**, et créez un rôle appelé "**Éditeur**".

![Image](https://lh7-us.googleusercontent.com/5zlCc-KmGxUNu069Tv-WQeibL7P-gnAMnTO6JoswreHIAy-jZip4Ym5svznawtNQZIJS-Tkn6XiXyHi3hJehtGJN3QyOwzx82EMYF0WbpSo9kKawhcEroeKxoSkdNe9suxvIqmee9-JjPQFt1GCHbhw)
_Création d'un rôle éditeur_

Nous avons créé le rôle appelé Éditeur, alors assignons maintenant les permissions appropriées à ce rôle. L'Éditeur se verra attribuer des permissions à tous les trois niveaux – Organisation, Projet et Environnement.

### Assigner des Permissions au Rôle Éditeur

Pour assigner des permissions, cliquez sur le nom du rôle que vous venez de créer. Vous verrez une barre latérale sur le côté droit avec un onglet permissions. Nous allons assigner des permissions pour tous les niveaux, en commençant par le niveau Organisation.

![Image](https://lh7-us.googleusercontent.com/se3FjEfVwxJEAnOI2PZGFVcCUk9a1OhtUVWxnqOb2oPgwJV_m08fWZoHjanZkCUMqr_DFUHpIp4RTphmRBWAybeZpGX6asEKDIu8TD8LvQEnbSOkQhchMfygcdMwymQRV0DxSVjeS6y4YqUW7YmEJls)
_Assignation des permissions en commençant au niveau Organisation_

Ce rôle Éditeur peut maintenant créer des projets dans cette organisation et gérer les groupes et leurs membres dans cette organisation.

Ensuite, nous lui donnons des permissions au niveau Projet. Cliquez sur le nom du projet sous l'onglet Projet, et faites comme montré dans la capture d'écran ci-dessous :

![Image](https://lh7-us.googleusercontent.com/WKCBnmjb_r458FNPXVt-7Lp9lAAJpwnl8q5YLXLU709HDMDa81b047oe-FPElWOz41Z5MwVP8wrO4LPXZYALEO2gc0p46lPhp9cp8yDJWYGzqb1KCs63Aq_dT57fIPEzM4ZOLe2N9-XbAfH61-7dRGE)
_Assignation des permissions au niveau projet_

Comme vous pouvez le voir, nous avons assigné à ce rôle deux permissions au niveau projet : **Voir le Projet**, et **Créer une Fonctionnalité**. Ainsi, tout utilisateur ou ensemble d'utilisateurs avec ce rôle ne pourra que voir un projet et créer une fonctionnalité.

Maintenant, pour les permissions les plus granulaires, qui sont au niveau environnement. Cliquez sur l'onglet Environnement, choisissez le projet Dev Test dans le menu déroulant, et cliquez sur l'Environnement de Développement.

![Image](https://lh7-us.googleusercontent.com/bX6kJwrSeL4EB_rfgwtF3FQlRFE3nqysci5BTEqwSS-i4ypmXUk4g2Dib1MrkMEsIjTYM8ClNT0y8NGa2p3-Q-R1afP4zvLuTtnN0NAoG9HXW8Vs2sx5tde44DJ9GuoaQX5Ucs6qdPZ5IY9plWWWScA)
_Gestion des permissions au niveau environnement (les plus granulaires)_

Comme vous pouvez le voir, nous avons assigné à ce rôle deux permissions au niveau environnement : **Voir l'Environnement**, et **Mettre à jour l'État de la Fonctionnalité**. Tout utilisateur ou ensemble d'utilisateurs avec ce rôle ne pourra que voir un environnement et mettre à jour sa valeur d'état de fonctionnalité dans le projet.

### Assigner le Rôle Éditeur à un Groupe

Maintenant, nous allons assigner ce rôle au groupe "**front_end_devs**". Pour ce faire, sélectionnez le rôle éditeur, allez dans l'onglet Membres, puis cliquez sur le texte "**Groupes Assignés**". Entrez le nom de votre groupe dans la barre de recherche, et sélectionnez-le.

![Image](https://lh7-us.googleusercontent.com/7-j0MWNj30Y4GEplEcCDKkuzrE4xBkwlckPvev5lMCHHWTwvyL6J6ulUNIiGTtREnWdkJIyi8PPa4ZAXFsjrxMadysh9-nmcT5rwJNux-14LCU-BP7gHhzJKMz75kY0yrFHCVZDqk9eklEYCSu7a_G4)
_Recherche de groupes auxquels assigner le rôle Éditeur_

### Tester les Permissions Assignées

Après avoir suivi les étapes ci-dessus, les utilisateurs du groupe "**front_end_devs**" devraient uniquement être en mesure d'effectuer les opérations suivantes

* Créer un nouveau projet et gérer ses groupes (niveau Organisationnel). En tant que créateur d'un nouveau projet, les politiques assignées à cet utilisateur pour un autre projet ne seront pas applicables ici.
* Créer et Supprimer des Fonctionnalités dans le Projet Dev Test
* Mettre à jour les valeurs d'état des fonctionnalités dans le Projet Dev Test

Maintenant, nous nous connectons depuis le compte de John Smith, un utilisateur de test du groupe "**front_end_devs**", pour vérifier que les permissions assignées fonctionnent correctement.

Tout d'abord, nous vérifierons les permissions au niveau organisationnel qui nous permettent de créer un nouveau projet.

![Image](https://lh7-us.googleusercontent.com/97YU-J_iusUdPt_IR5KrKrxHqIMsATZ559sUykWlS2q1M_o2RAsUKWkeZaONNc606gsc4rTltj5bvGRaIcN_xAPQmo7IYxms5K2mxOoOE5lyrg1_WuvDZ6oLUysj26EqVzrulBUcAkMfjgvFXUvDS6o)
_Vérification des permissions au niveau organisationnel_

Vous pouvez voir que l'utilisateur a réussi à créer un nouveau projet. Et comme il est le créateur de ce projet, John est l'administrateur et a toute l'autorité pour le gérer.

Maintenant, nous pouvons tester les permissions pour le projet Dev Test. Il suffit de cliquer sur le nom du projet dans la liste déroulante de gauche et de basculer entre les projets. Vous remarquerez sûrement que dans la barre de menu de gauche, vous n'avez accès qu'à l'environnement de développement. Cela est dû aux permissions au niveau environnement que nous avons assignées au rôle Éditeur.

Pour créer la fonctionnalité, cliquez simplement sur le bouton Créer une fonctionnalité, donnez un nom à la fonctionnalité et entrez une valeur de votre choix.

![Image](https://lh7-us.googleusercontent.com/JgFC5AAlw_KJy6vnKARWlCkugkiy79k2mB4QxkpRfE37DOfozKYhuNpInPnG0c8tEm6Tum70_ImXIcOGEJsXPRdsbs_6sD9Y8U5U1PtAzVzWEemZf5XWU18i1U84DtLPUzV-Grlf0vrbOP_XfPudjGY)
_Création d'une fonctionnalité_

Vous verrez quelque chose comme ceci après la création de la fonctionnalité :

![Image](https://lh7-us.googleusercontent.com/-YVJ1FAeV5LUuBe6myfqcwFgE3FufIdU56-7RwE-wml4ZD4tVY9UrMUsVW-daXuiAfA7xsp7oDuM0fcboHLN-A9dGxan47wgbaNL5bb91Mk2cn80QIggoF3QWfUHPBzx7tD_KCkzYFaszjjfp3MrtnU)
_Après avoir créé la fonctionnalité appelée `johns_feature`_

Maintenant, vous devriez avoir une compréhension de base de la manière dont le RBAC de Flagsmith gère les assignations de permissions et manage les utilisateurs, groupes et rôles.

Pour vous aider à avoir une vue d'ensemble et comprendre comment l'implémentation de Flagsmith pour le feature flagging peut minimiser les incidents chaotiques en production, considérons un cas d'usage.

## Cas d'Usage : le Chaos chez "NetGlobal Solutions"

Supposons qu'il y a une entreprise appelée NetGlobal Solutions, un géant mondial dans le secteur des réseaux. Ils fournissent diverses solutions de réseau à leurs clients, telles que CDN, gestion DNS, géolocalisation, cybersécurité cloud et atténuation des DDoS.

Ils ont décidé d'introduire un nouveau service, NetGlobal load balancing (une solution pour gérer d'énormes quantités de trafic web) pour leurs clients.

La politique de NetGlobal stipule qu'une fonctionnalité doit être testée pendant au moins 3 mois avec seulement 10 % de leurs clients avant d'être pleinement exposée au reste des utilisateurs. Ils ont donc décidé d'utiliser le feature flagging pour la tester en production avec 10 % de leurs clients – disons 10 000 en considérant la grande taille de leur base de clients.

Les valeurs des feature flags sont transmises à leur base de code à partir d'une table de base de données centrale isolée de toute relation avec d'autres tables. La table a une valeur booléenne qui gère la visibilité de la nouvelle fonctionnalité, et Devin, le chef d'équipe pour le développement de cette fonctionnalité, est responsable de sa gestion et de sa stabilité.

Ainsi, le moment vient et Devin publie la fonctionnalité en production. Deux mois passent et des milliers de clients utilisent leur service de load balancing pour leurs projets.

Un développeur de l'équipe de Devin, en travaillant sur la base de données de production, modifie accidentellement la valeur du feature flag dans la table. En raison de cette erreur, le service de load balancing tombe instantanément et les utilisateurs commencent à subir des pertes de trafic sur leurs sites.

Le système de surveillance déclenche une alarme et les équipes de développement et DevOps se mettent en action. En environ 10-15 minutes, ils trouvent le problème et résolvent l'incident. Mais comme la base d'utilisateurs est énorme et que l'utilisation de la fonctionnalité par les utilisateurs était assez technique, une perte impactante s'est déjà produite.

### Comment atténuer le problème

Maintenant, voyons comment l'équipe de Devin aurait pu atténuer cet incident s'ils avaient utilisé Flagsmith pour créer le feature flagging. Nous allons également voir comment son RBAC aurait aidé à sécuriser l'accès aux valeurs des flags.

* **Gestion des valeurs des flags :** En utilisant le [SDK de Flagsmith](https://www.flagsmith.com/sdks) dans le code de l'application, les valeurs des flags auraient pu être gérées et transmises à l'application avec une visibilité claire.
* **Contrôle d'audit :** En utilisant le journal d'audit de Flagsmith, l'équipe aurait pu avoir une meilleure responsabilité et transparence concernant les changements apportés aux feature flags.
* **RBAC :** il aurait restreint l'accès aux développeurs non autorisés afin qu'ils ne puissent pas modifier les valeurs des feature flags et aurait fourni un contrôle granulaire au chef d'équipe, aux gestionnaires de publication ou aux ingénieurs DevOps.

Ce cas d'usage hypothétique nous aide à comprendre l'importance d'un outil de feature flagging pour les publications en production. Il nous montre également pourquoi le RBAC joue un rôle important dans la gestion des permissions et de la hiérarchie dans un écosystème pour aider votre équipe à éviter les incidents de temps d'arrêt.

Le point clé à retenir ici est qu'il est important d'établir un processus DevOps standard et de choisir des outils DevOps qui deviennent une partie conforme de la publication et de la gestion des fonctionnalités.

## Comment établir un processus DevOps standard

Un processus DevOps standard doit être mis en place pour le cycle de vie d'une fonctionnalité. Il doit aborder toutes les étapes, de la phase de construction à la publication en production.

Plus important encore, dans la quête de publications rapides, votre équipe ne doit pas ignorer l'importance de sécuriser ce processus, comme je l'ai mentionné au début de cet article.

Un exemple de base d'un processus DevOps standard commencerait par établir un workflow solide de **Continuous Integration** avec les étapes suivantes :

1. **Build et Scan :** Construction des artefacts et scan des vulnérabilités avant de pousser vers les hubs d'artefacts.
2. **Effectuer des tests unitaires, de bout en bout et d'intégration :** Écrire des tests unitaires, de bout en bout et d'intégration est primordial pour tester la fonctionnalité des builds d'application.

Ensuite, vous voudrez établir un workflow solide de **Continuous Deployment** avec les étapes suivantes :

1. **Séparation des environnements :** Séparer les environnements de développement, de staging et de production pour des tests spécifiques à l'environnement.
2. **Sélection de la méthode de déploiement :** Choisir des stratégies de déploiement en fonction de vos besoins, telles que les Rolling Updates, les tests A/B, les Canary Deployments et le Feature Flagging.

Ensuite, vous devriez implémenter un mécanisme de **monitoring** robuste pour les applications en utilisant des systèmes de monitoring tels que Prometheus pour le monitoring, Grafana pour la visualisation, et Grafana On Call pour l'outil de gestion des incidents/astreintes.

Et enfin, après avoir créé le mécanisme ci-dessus, la dernière étape consisterait à utiliser les systèmes **RBAC** en place. Vous commenceriez par les plateformes cloud et passeriez aux outils DevOps utilisés pour implémenter le concept de moindre privilège à tous les niveaux et les ajouter comme partie des pratiques de conformité DevOps.

## Conclusion

Dans cet article, nous avons discuté de l'importance du RBAC dans le monde du DevOps et de la manière dont les équipes peuvent l'utiliser dans l'industrie pour sécuriser les environnements de production.

Nous avons également discuté de ce qu'est le feature flagging, de son importance pour les publications de fonctionnalités, et de la manière dont il utilise le RBAC pour gérer les permissions des utilisateurs.

Pour une meilleure compréhension, nous avons discuté d'un cas d'usage dans lequel nous avons vu comment l'implémentation de Flagsmith aurait pu éviter un incident de temps d'arrêt, et comment un processus de conformité DevOps pourrait renforcer les publications de fonctionnalités en production.