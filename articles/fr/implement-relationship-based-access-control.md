---
title: Comment implémenter le contrôle d'accès basé sur les relations (ReBAC)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-03-08T14:08:21.000Z'
originalURL: https://freecodecamp.org/news/implement-relationship-based-access-control
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/RELATIONSHIP-BASED-ACCESS-CONTROL.png
tags:
- name: authorization
  slug: authorization
- name: database
  slug: database
seo_title: Comment implémenter le contrôle d'accès basé sur les relations (ReBAC)
seo_desc: 'By Imran

  In today''s digital age, managing who can access what resources is more critical
  than ever. That''s where ReBAC comes in. It''s a fresh take on authorization, focusing
  on the relationships between different entities rather than just assigning s...'
---

Par Imran

À l'ère numérique actuelle, gérer qui peut accéder à quelles ressources est plus crucial que jamais. C'est là que le ReBAC intervient. Il s'agit d'une nouvelle approche de l'autorisation, axée sur les relations entre différentes entités plutôt que sur l'attribution de rôles ou d'attributs statiques.

Les méthodes traditionnelles de contrôle d'accès, comme le contrôle d'accès basé sur les rôles (RBAC), attribuent des rôles spécifiques aux utilisateurs. Bien que cela fonctionne dans de nombreux cas, cela peut devenir difficile, surtout dans des environnements dynamiques où les rôles et les permissions doivent s'adapter rapidement. D'autre part, le contrôle d'accès basé sur les attributs (ABAC) offre une flexibilité basée sur les attributs des utilisateurs, mais il peut devenir complexe à gérer.

Maintenant, le ReBAC consiste à comprendre la toile complexe des relations entre les entités. Qu'il s'agisse d'une organisation, d'une plateforme de médias sociaux ou d'un outil de gestion de projet, le ReBAC garantit que le contrôle d'accès reste dynamique et conscient du contexte.

À la fin de ce tutoriel, vous aurez une compréhension claire du ReBAC et serez en mesure de modéliser un scénario ReBAC.

## Points clés

* **Principes du ReBAC** : Comprendre comment le ReBAC utilise les relations entre les entités pour le contrôle d'accès, différemment des modèles traditionnels.
* **Visualisation des politiques** : Apprendre à représenter les politiques sous forme de graphes pour une gestion plus claire.
* **Exemples concrets** : Explorer l'application du ReBAC dans des scénarios comme les plateformes de médias sociaux et les outils de gestion de projet.
* **Avantages du ReBAC** : Découvrir les avantages comme le contrôle granulaire et l'adaptation dynamique des politiques.
* **Modèles de permission** : Se familiariser avec les modèles courants du ReBAC tels que les modèles de propriété et hiérarchiques.
* **Implémentation avec Permify** : Guide étape par étape pour implémenter le ReBAC dans Permify, incluant la définition des entités, l'établissement des relations et la configuration des permissions.

## Qu'est-ce que le contrôle d'accès basé sur les relations (ReBAC) ?

Les méthodes traditionnelles de contrôle d'accès, comme le contrôle d'accès basé sur les rôles (RBAC), attribuent des rôles spécifiques aux utilisateurs, comme donner à quelqu'un un badge qui dit "manager" ou "employé". Mais que se passe-t-il si les rôles ne sont pas si clairement définis, et que les relations entre les personnes et les ressources comptent davantage ?

C'est là que le contrôle d'accès basé sur les relations (ReBAC) intervient. Au lieu de se fier uniquement à des rôles ou des attributs prédéfinis, le ReBAC prend en compte la toile complexe des connexions entre les utilisateurs, les ressources et d'autres entités. C'est comme dire : "Vous pouvez accéder à cela parce que vous êtes connecté à cela de cette manière spécifique", plutôt que de se baser uniquement sur une étiquette générique.

Mais comment le ReBAC fait-il cela ? Le ReBAC examine les relations entre les entités, telles que les utilisateurs et les ressources, et utilise ces connexions pour déterminer l'accès.

Décomposons cela davantage. Dans notre vie quotidienne, nous avons des relations qui comptent. Pensez aux réseaux sociaux - vous pouvez voir certaines publications parce que vous êtes ami avec quelqu'un ou parce que quelqu'un que vous suivez l'a aimé. Le ReBAC prend cette idée et l'applique au contrôle d'accès dans les systèmes.

## Politique sous forme de graphe

Au cœur du ReBAC se trouve le concept de "Politique sous forme de graphe". Cette idée montre l'importance de visualiser les politiques d'accès à travers les relations.

Imaginez que vous avez une carte détaillée d'une ville animée. Elle ne montre pas seulement les bâtiments mais aussi les connexions entre eux - les routes, les ponts et les chemins qui relient tout ensemble.

Maintenant, imaginez cette carte comme une représentation de votre organisation. Au lieu de bâtiments, elle représente les membres de l'équipe, les départements et leurs rôles. Les connexions entre eux symbolisent les relations qui dictent l'accès.

C'est ce que nous entendons par "Politique sous forme de graphe" dans le ReBAC.

En termes plus simples, les politiques d'accès sont comme des points interconnectés sur un graphe. Chaque point représente une entité, et les lignes entre eux signifient les relations influençant l'autorisation. C'est une représentation visuelle qui nous aide à comprendre la toile complexe des connexions qui régissent l'accès.

## En quoi le ReBAC est-il différent des autres modèles de contrôle ?

Maintenant, explorons comment le ReBAC se distingue des autres modèles de contrôle d'accès, tels que le contrôle d'accès basé sur les rôles (RBAC).

Contrairement aux modèles traditionnels, le ReBAC ne se fie pas uniquement à des rôles ou des attributs rigides. Au lieu de cela, il fonctionne en dérivant les permissions des relations existantes. Voici comment il se distingue :

* **Dérivation des rôles** : Le ReBAC permet la création de politiques d'autorisation basées sur des relations préexistantes. Cela signifie qu'attribuer un rôle à un utilisateur dans un contexte peut automatiquement étendre ce rôle aux entités liées, évitant ainsi le besoin d'une attribution manuelle.
* **Rôles de ressources** : Contrairement aux rôles globaux dans les modèles traditionnels, le ReBAC introduit le concept de rôles spécifiques aux ressources (par exemple : Folder#Owner). Ces rôles sont exclusifs au contexte d'une ressource particulière, garantissant que les permissions sont pertinentes et adaptées à cette entité spécifique.

## Exemples concrets

Pour mieux comprendre comment le contrôle d'accès basé sur les relations (ReBAC) fonctionne dans le monde réel, explorons deux scénarios qui imitent les complexités quotidiennes.

Ces exemples aideront à illustrer comment le ReBAC excelle dans la gestion des dynamiques d'accès complexes.

### Plateforme sociale de type Instagram

Considérons une plateforme inspirée d'Instagram où les utilisateurs possèdent des comptes individuels. Chaque compte comprend du contenu généré par les utilisateurs, à savoir des images (Pic 1 et Pic 2), des interactions de chat avec différents utilisateurs et une collaboration sur des projets.

Le compte utilisateur possède une liste d'utilisateurs bloqués qui sont restreints de voir les images. Voici une analyse détaillée des entités et des permissions :

#### 1. Entités de compte

* **Compte utilisateur** : Représente les comptes utilisateurs individuels sur la plateforme.
* **Images (Pic 1 et Pic 2)** : Représentent le contenu visuel généré par les utilisateurs.
* **Chats** : Capturent les historiques d'interaction avec différents utilisateurs.
* **Liste des utilisateurs bloqués** : Maintient une liste des utilisateurs bloqués de voir les images.

#### 2. Dynamique des permissions

##### Permissions d'accès au compte :

* "Account#Owner" accorde la propriété, permettant au titulaire du compte utilisateur de gérer tous les aspects.
* "Account#Viewer" permet aux autres de voir le compte de l'utilisateur.

##### Permissions de gestion des images :

* "Picture#Owner" désigne la propriété au niveau de l'image, permettant à l'utilisateur de modifier, supprimer et télécharger des images.
* "Picture#Viewer" permet aux spectateurs normaux de seulement voir les images.
* "BlockedUser#CannotView" garantit que les utilisateurs bloqués ne peuvent pas voir les images.

##### Permissions d'interaction de chat :

* "Chat#Participant" permet aux utilisateurs de participer aux interactions de chat.
* "Chat#BlockedUser" restreint certains utilisateurs de participer aux chats.

##### Permissions de modification de compte :

* "Account#Edit" accorde la capacité de mettre à jour les détails et préférences du compte.

![Instagram.png](https://www.freecodecamp.org/news/content/images/2024/03/Instagram.png)
_Entités de la plateforme sociale de type Instagram_

Dans ce scénario, le symbole "#" représente la relation entre les entités lors de la définition des permissions. Par exemple, "Account#Owner" signifie la propriété du compte utilisateur, permettant au titulaire du compte de gérer tous les aspects de son compte.

### Outil de gestion de projet

Imaginez un outil de gestion de projet où les équipes collaborent sur divers projets. Les entités comme "Teams", "Projects", et "Tasks" jouent des rôles centraux, montrant l'adaptabilité du ReBAC :

#### 1. Entités de l'équipe :

* **Teams** : Représentent des groupes collaboratifs au sein de l'outil de gestion de projet.
* **Projects** : Englobent diverses initiatives en cours.
* **Tasks** : Décomposent les activités de projet en tâches gérables.

#### 2. Dynamique des permissions :

##### Permissions de leadership d'équipe :

* "Team#Lead" désigne le leadership de l'équipe, permettant aux leaders de gérer les activités liées à l'équipe.

##### Permissions de propriété de projet :

* "Project#Owner" signifie la propriété au niveau du projet, accordant un contrôle complet sur les actions liées au projet.

**Permissions d'assignation de tâche :**

* "Task#Assignee" désigne les individus responsables de tâches spécifiques.



![project.png](https://www.freecodecamp.org/news/content/images/2024/03/project.png)
_Entités de l'outil de gestion de projet_

Ces scénarios concrets démontrent la polyvalence et l'efficacité du ReBAC dans la gestion du contrôle d'accès dans différents contextes.

## Avantages du ReBAC

Maintenant, comprenons pourquoi le contrôle d'accès basé sur les relations (ReBAC) se distingue des méthodes traditionnelles comme le contrôle d'accès basé sur les rôles (RBAC) et le contrôle d'accès basé sur les attributs (ABAC). Le ReBAC apporte une multitude d'avantages, améliorant la scalabilité, la flexibilité et l'adaptabilité dans des configurations organisationnelles complexes. Examinons de plus près ses principaux avantages :

### Contrôle granulaire et contextuel

Le ReBAC permet aux organisations de définir des contrôles d'accès granulaires adaptés aux relations spécifiques entre les utilisateurs, les ressources et les entités. Cela garantit que les permissions sont contextuellement pertinentes, offrant un niveau nuancé de contrôle.

### Gestion efficace des hiérarchies

Dans des scénarios avec des structures hiérarchiques, le ReBAC simplifie la gestion du contrôle d'accès. En permettant aux permissions d'être héritées en fonction des relations, il réduit le besoin d'attributions de rôles manuelles. 

Cela simplifie la création de connexions naturelles entre différentes unités commerciales, ressources et entités, facilitant la navigation dans des hiérarchies complexes.

### Scalabilité et adaptabilité

Le ReBAC est conçu pour évoluer avec la croissance organisationnelle et les changements dans les relations. Il s'adapte facilement à l'introduction de nouvelles entités ou connexions. Cependant, il est crucial de relever le défi de l'explosion des rôles, où le nombre de rôles croît de manière exponentielle parallèlement à la croissance des actifs. 

Sans une gestion appropriée, cela peut entraîner des risques de sécurité et une surcharge administrative. Pourtant, la scalabilité du ReBAC garantit que les contrôles d'accès restent efficaces, atténuant ces défis et évitant le besoin de modifications extensives.

Avec ces avantages à l'esprit, le ReBAC offre un cadre robuste pour le contrôle d'accès qui répond aux besoins évolutifs des organisations modernes. Maintenant, plongeons dans les modèles de permission de type de relation courants pour mieux comprendre comment le ReBAC fonctionne.

## Modèles de permission de type de relation courants

Examinons certains des modèles de permission :

### Modèle de **propriété**

Le modèle de propriété dans le ReBAC est un concept fondamental où les relations de propriété rationalisent l'autorisation au sein des structures hiérarchiques.

Dans ce modèle, le fait de posséder une entité de niveau supérieur étend automatiquement la propriété à ses entités subordonnées.

Imaginez un scénario dans une plateforme de stockage cloud où les utilisateurs créent des dossiers pour organiser leurs fichiers. Dans le modèle de propriété, l'utilisateur qui crée un dossier est désigné comme le propriétaire.

Par conséquent, cette relation de propriété accorde automatiquement à l'utilisateur des permissions de propriété pour tous les fichiers au sein de ce dossier.

Cette structure de propriété hiérarchique simplifie la gestion des permissions et reflète les dynamiques de propriété du monde réel.

### Modèle **parent-enfant et hiérarchique**

Le modèle parent-enfant et hiérarchique est un outil puissant pour gérer le contrôle d'accès dans des structures hiérarchiques telles que les cadres organisationnels ou les systèmes de fichiers.

Dans ce modèle, les permissions accordées au niveau parent sont transmises à ses entités enfants, assurant un système d'autorisation cohésif et efficace.

Considérons un environnement d'entreprise où les organisations ont plusieurs départements. En utilisant le modèle parent-enfant et hiérarchique du ReBAC, les permissions accordées au niveau de l'organisation, telles que les privilèges d'administrateur, s'étendent de manière transparente aux départements de l'organisation et à leurs membres respectifs.

Ce flux hiérarchique de permissions reflète la structure organisationnelle, facilitant la gestion du contrôle d'accès à différents niveaux.

### Modèle de **groupes d'utilisateurs et équipes**

Le modèle de groupes d'utilisateurs et équipes permet une gestion efficace des permissions en regroupant les utilisateurs en fonction d'attributs partagés ou d'affiliations de projet.

Dans ce modèle, les permissions assignées à un chef de groupe, par exemple, peuvent être appliquées sans effort à tous les membres de ce groupe.

Dans un outil collaboratif de gestion de projet, les équipes servent de groupes d'utilisateurs. En appliquant le modèle de groupes d'utilisateurs et équipes du ReBAC, les permissions du chef d'équipe, comme la modification ou la suppression des tâches de projet, peuvent être automatiquement héritées par tous les membres de l'équipe.

Cette approche rationalisée simplifie le contrôle d'accès dans les environnements collaboratifs, où les permissions basées sur les équipes sont cruciales pour l'efficacité du projet.

Ces trois modèles de contrôle d'accès basé sur les relations démontrent la flexibilité et l'adaptabilité du ReBAC dans la gestion de diverses structures organisationnelles et domaines d'application.

En alignant les permissions avec les relations inhérentes entre les entités, le ReBAC fournit un cadre de contrôle d'accès intuitif et puissant.

## Comment implémenter le ReBAC avec Permify

Maintenant, implémentons pratiquement le ReBAC en utilisant Permify.

[Permify](https://permify.co/) est une plateforme open-source d'autorisation en tant que service qui permet aux développeurs de modéliser, gérer et appliquer le contrôle d'accès dans les applications. Elle fournit des outils pour définir des règles d'autorisation complexes et des relations entre les entités, telles que les utilisateurs, les organisations et les ressources.

Permify utilise un langage spécifique de domaine pour créer des modèles d'autorisation et offre un environnement Playground pour tester ces modèles.

Il prend également en charge la création de tuples relationnels et d'attributs pour gérer des scénarios de contrôle d'accès dynamique, rationalisant le processus de mise en œuvre de systèmes d'autorisation robustes et flexibles dans les applications logicielles.

Nous allons créer un scénario couvrant à la fois les modèles de propriété et parent-enfant & hiérarchique.

Nous utiliserons le [Permify Playground](https://play.permify.co/) pour la modélisation.

### Modélisation

La modélisation dans Permify implique la création d'un schéma qui définit les relations et les permissions entre différentes entités dans votre système. 

Voici un processus simplifié :

1. **Définir les entités** : Commencez par créer des entités qui représentent les ressources dans votre système (par exemple : utilisateurs, organisations, équipes).
2. **Définir les relations** : Établissez des relations entre ces entités. Par exemple, une organisation peut avoir des membres et des administrateurs, ou une équipe peut faire partie d'une organisation.
3. **Définir les actions et les permissions** : Spécifiez les actions qui peuvent être effectuées sur chaque entité et les conditions dans lesquelles elles sont autorisées. Par exemple, seuls les administrateurs peuvent supprimer une organisation.

Permify utilise son propre langage pour modéliser la logique d'autorisation, permettant des structures complexes utilisant des opérateurs algébriques. Le processus de modélisation inclut la définition des entités, des relations, des actions, des permissions et, si nécessaire, des attributs pour des scénarios plus avancés comme l'ABAC (contrôle d'accès basé sur les attributs).

La modélisation dans Permify consiste à créer un plan clair de la structure de votre organisation et à définir qui peut faire quoi. 

Décomposons comment modéliser un schéma dans Permify.

### Étape 1 : Définir les entités

Les entités sont les objets principaux de votre modèle. Dans ce cas, nous avons `user`, `organization`, `department`, `project`, `file`, et `task`.

```jsx
entity user {}
entity organization {}
entity department {}
entity project {}
entity file {}
entity task {}


```

### Étape 2 : Établir les relations

Ensuite, nous spécifions les relations entre ces entités. Cela définit comment elles sont connectées.

**Organisation** :

* A des `admin` qui sont des utilisateurs.

```jsx
entity organization {
    relation admin @user
}


```

**Département** :

* Appartient à une `organization` (parent).
* A des rôles `head`, `manager`, et `employee`, tous étant des utilisateurs.

```jsx
entity department {
    relation parent @organization
    relation head @user
    relation manager @user
    relation employee @user
}


```

**Projet** :

* Appartient à un `department` (parent).

```jsx
entity project {
    relation parent @department
}


```

**Fichier** :

* Appartient à un `department` (parent).
* A un `owner` qui est un utilisateur.

```jsx
entity file {
    relation parent @department
    relation owner @user
}


```

**Tâche** :

* Appartient à un `project` (parent).
* A un `assignee` qui est un utilisateur.

```jsx
entity task {
    relation parent @project
    relation assignee @user
}


```

### Étape 3 : Définir les permissions

Les permissions déterminent quelles actions des rôles spécifiques peuvent effectuer sur chaque entité.

**Projet** :

* La permission `contribute_to_project` est accordée à `employee` ou `manager` du `department` parent.

```jsx
entity project {
    // ... (relations existantes)
    permission contribute_to_project = parent.employee or parent.manager
}


```

**Fichier** :

* Les permissions `read`, `edit`, et `delete` sont contrôlées en fonction du `manager` du `department` parent et du `owner`.

```jsx
entity file {
    // ... (relations existantes)
    permission read   = parent.manager or owner
    permission edit   = parent.manager or owner
    permission delete = owner
}


```

**Tâche** :

* La permission `view_task` est donnée à l'`assignee`.

```jsx
entity task {
    // ... (relations existantes)
    permission view_task = assignee
}


```

**Schéma complet** :

```
// Définir les entités
entity user {}

entity organization {
    // Rôles organisationnels
    relation admin @user
}

entity department {
    // Rôles de département
    relation parent @organization
    relation head @user
    relation manager @user
    relation employee @user
}

entity project {
    // Rôles de projet
    relation parent @department

    // Permissions
    permission contribute_to_project = parent.employee or parent.manager
}

entity file {
    // Représente l'entité parente des fichiers (département)
    relation parent @department

    // Représente le propriétaire du fichier
    relation owner @user

    // Permissions
    permission read   = parent.manager or owner
    permission edit   = parent.manager or owner
    permission delete = owner
}

entity task {
    // Représente l'entité parente des tâches (projet)
    relation parent @project

    // Représente l'assigné de la tâche
    relation assignee @user

    // Permissions
    permission view_task   = assignee
}

```

### Tuples de relation

La création de tuples de relation pour le schéma de l'organisation peut être accomplie via le Permify Playground et l'API. 

Voici comment les tuples de relation seraient structurés selon le schéma :

#### Relations utilisateur et organisation :

* Pour assigner un utilisateur comme administrateur dans une organisation, le tuple serait : `organization:ID#admin@user:ID`.
* Pour désigner un utilisateur comme membre d'une organisation : `organization:ID#member@user:ID`.

#### Relations utilisateur et département :

* Assigner un chef à un département : `department:ID#head@user:ID`.
* Assigner un manager à un département : `department:ID#manager@user:ID`.
* Associer un employé à un département : `department:ID#employee@user:ID`.
* Pour définir l'organisation parente d'un département : `department:ID#parent@organization:ID`.

#### Relations projet et département :

* Pour définir le département parent d'un projet : `project:ID#parent@department:ID`.

#### Gestion des fichiers :

* Associer un fichier à son département parent : `file:ID#parent@department:ID`.
* Définir le propriétaire d'un fichier : `file:ID#owner@user:ID`.

#### Gestion des tâches :

* Lier une tâche à son projet parent : `task:ID#parent@project:ID`.
* Assigner un utilisateur comme responsable d'une tâche : `task:ID#assignee@user:ID`.

Dans chacun de ces tuples, `ID` est un espace réservé qui doit être remplacé par l'identifiant réel de l'entité ou de l'utilisateur dans votre système. 

Par exemple, si vous avez une organisation avec un ID de 1 et un utilisateur avec un ID de 3, et que vous souhaitez assigner cet utilisateur comme administrateur de cette organisation, le tuple serait `organization:1#admin@user:3`.

![Untitled](https://www.freecodecamp.org/news/content/images/2024/03/Untitled-2.png)
_Tableau de bord des relations_

Ces tuples sont créés et gérés à l'aide de l'API Permify. L'API permet de créer, mettre à jour et supprimer ces tuples selon les besoins, reflétant la nature dynamique des relations et des permissions dans une organisation. Cette flexibilité garantit que vos données d'autorisation sont toujours à jour et cohérentes avec l'état actuel des entités de votre système et de leurs relations.

### Application

Pour appliquer le contrôle d'accès dans votre schéma en utilisant Permify, vous pouvez créer des scénarios dans la section Application du Permify Playground. Cela se fait en utilisant YAML pour définir divers scénarios de test. 

Voici un exemple basé sur votre schéma et les tuples de relation créés :

#### Vérifier si un utilisateur (par exemple : user:2) peut contribuer à un projet :

* Entité : `project:1`
* Sujet : `user:2`
* Assertion : `contribute_to_project: true or false` (selon que user:2 est un employé ou un manager dans le département parent de project:1).

```
- name: user_access_test
  checks:
    - entity: project:1
      subject: user:2
      context: null
      assertions:
        contribute_to_project: false
  entity_filters: []
  subject_filters: []

```

**Vérifier si un utilisateur (par exemple : user:4) peut voir une tâche** :

* Entité : `task:1`
* Sujet : `user:4`
* Assertion : `view_task: true or false` (vrai si user:4 est l'assigné de la tâche).

```
- name: user_access_test
  checks:
    - entity: task:1
      subject: user:4
      context: null
      assertions:
        view_task: false
  entity_filters: []
  subject_filters: []

```

Ces scénarios vous aideront à valider les permissions selon votre schéma dans un environnement contrôlé. 

Chaque assertion dans le scénario YAML définira le résultat attendu (vrai ou faux) pour une action ou une permission particulière basée sur votre schéma et vos tuples de données.

![Untitled](https://www.freecodecamp.org/news/content/images/2024/03/Untitled-1.png)
_Représentation YAML_

Pour des étapes détaillées et des exemples, consultez la [Documentation de modélisation de Permify](https://docs.permify.co/docs/getting-started/modeling/).

### Conclusion

En suivant ces étapes, vous pouvez implémenter efficacement un système sophistiqué de ReBAC en utilisant Permify. 

Cette implémentation fournira un cadre de contrôle d'accès robuste, flexible et sécurisé, adapté aux besoins et relations uniques au sein de votre organisation.