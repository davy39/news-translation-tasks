---
title: Comment créer des diagrammes d'architecture logicielle avec le modèle C4
subtitle: ''
author: Alex Pliutau
co_authors: []
series: null
date: '2024-08-21T18:50:04.506Z'
originalURL: https://freecodecamp.org/news/how-to-create-software-architecture-diagrams-using-the-c4-model
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724187048778/7d2821c6-c0c9-4d03-999f-37022388210c.jpeg
tags:
- name: Software Engineering
  slug: software-engineering
- name: software architecture
  slug: software-architecture
- name: design patterns
  slug: design-patterns
- name: C4 Model
  slug: c4-model
- name: diagrams
  slug: diagrams
seo_title: Comment créer des diagrammes d'architecture logicielle avec le modèle C4
seo_desc: 'As a developer, you''ll likely work on a complex project at some point
  where deciphering the codebase feels like reading a whole novel. Engineers are code
  wizards, but even the best get lost in sprawling code.

  The challenge is that architecture diagra...'
---

En tant que développeur, vous travaillerez probablement à un moment donné sur un projet complexe où déchiffrer la base de code ressemble à la lecture d'un roman complet. Les ingénieurs sont des magiciens du code, mais même les meilleurs se perdent dans un code tentaculaire.

Le défi est que les diagrammes d'architecture – s'ils existent – sont souvent des reliques obsolètes d'une époque révolue.

C'est pourquoi la création et la maintenance de diagrammes efficaces et clairs devraient se faire sans effort. Des visuels à jour garantissent que tout le monde reste sur la même longueur d'onde, éliminant la confusion et le temps perdu.

## Table des matières

* [Qu'est-ce que le modèle C4 ?](heading-questce-que-le-modele-c4)
    
* [Niveau 1 : Contexte](#heading-niveau-1-contexte)
    
* [Niveau 2 : Conteneurs](#heading-niveau-2-conteneurs)
    
* [Niveau 3 : Composants](#heading-niveau-3-composants)
    
* [Niveau 4 : Code](#heading-niveau-4-code)
    
* [Diagrammes supplémentaires](#heading-diagrammes-supplementaires)
    
* [Diagrammes en tant que code](#heading-diagrammes-en-tant-que-code)
    
* [Automatiser le rendu dans votre CI](#heading-automatiser-le-rendu-dans-votre-ci)
    
* [Ressources](#heading-ressources)
    

## Qu'est-ce que le modèle C4 ?

Le [modèle C4](https://c4model.com/) a été créé pour aider les équipes de développement logiciel à décrire et communiquer l'architecture logicielle.

C4 signifie « Contexte, Conteneurs, Composants et Code ». Ce sont les quatre niveaux qui devraient suffire pour décrire un système complexe.

La meilleure façon d'expliquer le concept est de penser à la façon dont nous utilisons Google Maps. Lorsque nous explorons une zone dans Google Maps, nous commençons souvent par un zoom arrière pour obtenir du contexte. Une fois que nous avons trouvé la zone approximative qui nous intéresse, nous pouvons zoomer pour obtenir un peu plus de détails.

### Niveau 1 : Contexte

Ce niveau est le plus éloigné. C'est une vue d'ensemble du système dans le contexte plus large du monde. Le diagramme se concentre sur les acteurs et les systèmes.

Pour les exemples ci-dessous, nous utiliserons un système logiciel simple de gestion de tâches pour démontrer ces 4 niveaux.

![Diagramme montrant le niveau Contexte](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d096cb9-3058-4bbd-9c69-6a41361e4d3b_1600x2000.png align="left")

Ce diagramme dépeint les interactions du système de gestion de tâches avec les systèmes externes et les différents groupes d'utilisateurs qui l'utilisent. Nous pouvons voir que le logiciel de gestion de tâches dépend de deux systèmes externes : l'E-mail et le Calendrier, et que deux types d'acteurs (utilisateurs) l'utilisent : le Client et l'Utilisateur Administrateur.

### Niveau 2 : Conteneurs

Le niveau des conteneurs est une vue plus détaillée de votre système (ne confondez pas les conteneurs C4 avec les conteneurs Docker).

Il révèle comment diverses unités fonctionnelles comme les applications et les bases de données travaillent ensemble et répartissent les responsabilités.

Ce diagramme met également en évidence les technologies clés employées et présente le flux de communication entre ces conteneurs. Il présente une vue simplifiée et centrée sur la technologie des composants de base du système et de leurs interactions.

Si vous avez une architecture Microservices, alors chaque Microservice serait un conteneur.

Exemples de conteneurs :

* Application monopage (SPA)
    
* Serveur web
    
* Fonction Serverless
    
* Base de données
    
* API
    
* Bus de messages
    

Et ainsi de suite.

![Diagramme montrant le niveau Conteneurs](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb614c4e5-4fbd-4e10-8682-c3e67ec72f2d_3028x2691.png align="left")

Ce niveau plonge dans la composition interne du système de gestion de tâches. Il montre que notre système se compose de conteneurs tels que l'Interface Web Utilisateur, l'Interface Web Admin, l'API et une Base de données. L'API est également le conteneur qui est connecté aux systèmes externes, par exemple pour envoyer des e-mails ou créer des événements dans le calendrier.

### Niveau 3 : Composants

Le niveau de zoom suivant est celui des composants. Cela montre les principaux blocs de construction structurels de votre application, et est souvent une vue conceptuelle de l'application. Le terme composant est ici assez large. Il pourrait représenter un contrôleur ou un service contenant la logique métier.

![Diagramme montrant le niveau Composants](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55564aaa-d404-4322-a6f3-9674326410d5_1995x1900.png align="left")

Ce diagramme se concentre sur la structure interne du conteneur API au sein du système de gestion de tâches. Il révèle que le conteneur API héberge des fonctionnalités cruciales telles que les opérations CRUD (Create, Read, Update, Delete) pour la manipulation des données et les mécanismes d'authentification des utilisateurs. Le composant CRUD est celui qui communique avec la base de données.

### Niveau 4 : Code

Le niveau de zoom le plus profond est le diagramme de code. Bien que ce diagramme existe, il n'est souvent pas utilisé car le code brosse un portrait très similaire. Cependant, dans des environnements hautement réglementés et pour des projets hérités (legacy) complexes, ce niveau peut aider à illustrer les subtilités internes du logiciel.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde6e40f0-d713-46b9-906e-618fb61eb622_602x339.png align="left")

### Diagrammes supplémentaires

Outre les 4 diagrammes ci-dessus, il en existe d'autres qui valent la peine d'être mentionnés :

* Diagramme de déploiement
    
* Diagramme dynamique : pour décrire un processus ou un flux
    

![Flux de connexion](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa13b10a-2093-4ab8-8302-dc75b09be96f_1570x1461.png align="left")

Sur ce diagramme, nous montrons un flux de connexion, qui n'est pas un conteneur ou un composant, mais plutôt un processus logiciel qui se produit dans notre système. Il montre que les interfaces Web/Admin utilisent une authentification basée sur JWT pour communiquer avec l'API et que le jeton JWT est stocké dans le stockage local du côté client.

## Diagrammes en tant que code

La puissance de C4 s'accompagne d'une approche de « diagramme en tant que code » (diagram-as-code). Cela signifie traiter vos diagrammes comme votre base de code :

* **Contrôle de version :** Stockez-les dans un système de contrôle de source (comme Git) pour un suivi et une collaboration facilités.
    
* **Collaboration :** Travaillez ensemble sur les diagrammes en utilisant des pull requests, à l'instar des revues de code.
    
* **Automatisation :** Intégrez-les dans vos pipelines de build pour un rendu automatique avec vos outils préférés.
    

### Outil utile : Structurizr

Il existe quelques outils pour aider à la modélisation et à la schématisation, mais le plus populaire de nos jours est [Structurizr](https://www.structurizr.com/) avec son DSL (Domain Specific Language) personnalisé.

Il vous suffit de vous familiariser avec la syntaxe du DSL, qui est assez simple. Dès que vous y serez habitué, vous pourrez créer ou mettre à jour des diagrammes en un rien de temps.

Ci-dessous, vous pouvez voir le DSL pour notre système de gestion de tâches.

```bash
workspace {
    model {
        # Acteurs
        customer = person "Client" "" "person"
        admin = person "Utilisateur Administrateur" "" "person"

        # Systèmes externes
        emailSystem = softwareSystem "Système d'e-mail" "Mailgun" "external"
        calendarSystem = softwareSystem "Système de calendrier" "Calendly" "external"

        # Système de gestion de tâches
        taskManagementSystem  = softwareSystem "Système de gestion de tâches"{
            webContainer = container "Interface Web Utilisateur" "" "" "frontend"
            adminContainer = container "Interface Web Admin" "" "" "frontend"
            dbContainer = container "Base de données" "PostgreSQL" "" "database"
            apiContainer = container "API" "Go" {
                authComp = component "Authentification"
                crudComp = component "CRUD"
            }
        }

        # Relations (Acteurs & Systèmes)
        customer -> webContainer "Gère les tâches"
        admin -> adminContainer "Gère les utilisateurs"
        apiContainer -> emailSystem "Envoie des e-mails"
        apiContainer -> calendarSystem "Crée des tâches dans le calendrier"

        # Relations (Conteneurs)
        webContainer -> apiContainer "Utilise"
        adminContainer -> apiContainer "Utilise"
        apiContainer -> dbContainer "Persiste les données"

        # Relations (Composants & Conteneurs)
        crudComp -> dbContainer "Lit et écrit dans"
        webContainer -> authComp "S'authentifie avec"
        adminContainer -> authComp "S'authentifie avec"
    }
}
```

Plongeons dans les parties les plus importantes :

```yaml
workspace [nom] [description] {
    model {
    }
}
```

Ici, nous définissons notre espace de travail (workspace) qui doit comporter au moins un modèle. Un nom et une description peuvent être donnés facultativement à l'espace de travail.

```yaml
customer = person "Client" "" "person"
admin = person "Utilisateur Administrateur" "" "person"
```

Dans cette section, nous définissons nos personnes (par exemple, un utilisateur, un acteur, un rôle ou un persona) au format suivant : `person <nom> [description] [étiquettes]`.

Vous pouvez utiliser un format similaire (nom, description, étiquettes) pour identifier les systèmes externes :

```yaml
        emailSystem = softwareSystem "Système d'e-mail" "Mailgun" "external"
        calendarSystem = softwareSystem "Système de calendrier" "Calendly" "external"
```

Pour décrire le système logiciel interne, nous devons écrire un bloc qui montre également ses conteneurs et composants :

```yaml
taskManagementSystem  = softwareSystem "Système de gestion de tâches"{
    webContainer = container "Interface Web Utilisateur" "" "" "frontend"
    adminContainer = container "Interface Web Admin" "" "" "frontend"
    dbContainer = container "Base de données" "PostgreSQL" "" "database"
    apiContainer = container "API" "Go" {
        authComp = component "Authentification"
        crudComp = component "CRUD"
    }
}
```

* Format du conteneur : `container <nom> [description] [technologie] [étiquettes]`
    
* Format du composant : `component <nom> [description] [technologie] [étiquettes]`
    

Le reste du modèle est la partie la plus intéressante où nous définissons les relations entre toutes les parties (systèmes, conteneurs, composants) :

```yaml
apiContainer -> emailSystem "Envoie des e-mails"
```

Le format suivant est utilisé : `<identifiant> -> <identifiant> [description] [technologie] [étiquettes]`.

Il existe d'autres fonctionnalités disponibles dans le DSL Structurizr, telles que le style, les thèmes, la visibilité, etc. Vous pouvez les trouver [ici](https://docs.structurizr.com/dsl/language).

## Automatiser le rendu dans votre CI

Puisque vous pouvez héberger vos modèles sur GitHub, il est très facile d'automatiser le pipeline pour le rendu des diagrammes dans les outils de votre choix.

Dans notre cas, Structurizr dispose d'une GitHub Action qui vous permet d'exécuter **structurizr-cli**, un utilitaire en ligne de commande pour Structurizr qui vous permet de créer des modèles d'architecture logicielle basés sur le modèle C4 en utilisant un langage spécifique au domaine textuel (DSL).

Ce dépôt d'exemple contient un [workflow](https://github.com/plutov/c4-diagram-example/blob/main/.github/workflows/pages.yaml) qui génère simplement une page statique et la publie sur GitHub Pages.

```yaml
name: Déployer le contenu statique sur GitHub Pages

on:
  push:
    branches: ["main"]

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/avisi-cloud/structurizr-site-generatr
      options: --user root
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Create site
        run: |
          /opt/structurizr-site-generatr/bin/structurizr-site-generatr generate-site -w diagram.dsl
      - uses: actions/upload-artifact@v3
        with:
          name: website
          path: build/site
  deploy:
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v3
        with:
          name: website
          path: build/site
      - name: Setup Pages
        uses: actions/configure-pages@v3
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v1
        with:
          path: "build/site"
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

Cette GitHub Action utilise l'action Structurizr CLI pour compiler notre fichier DSL en HTML et le publier sur GitHub Pages.

## Conclusion

Je suis convaincu que la création et la maintenance de diagrammes efficaces et clairs devraient se faire sans effort. Des visuels à jour garantissent que tout le monde reste sur la même longueur d'onde, éliminant la confusion et le temps perdu.

Le modèle C4 et un peu d'automatisation avec le DSL Structurizr peuvent aider à accélérer ce processus et à garder les diagrammes proches de la base de code. L'ensemble du processus peut désormais être automatisé également dans votre SDLC.

### Ressources

* [Dépôt GitHub](https://github.com/plutov/c4-diagram-example)
    
* [Modèle C4](https://c4model.com/)
    
* [Référence du langage DSL](https://docs.structurizr.com/dsl/language)
    
* [Extension Visual Studio Code pour C4 DSL](https://marketplace.visualstudio.com/items?itemName=systemticks.c4-dsl-extension)
    
* [structurizr-cli-action](https://github.com/marketplace/actions/structurizr-cli-action)
    
* [Découvrir plus d'articles de packagemain.tech](https://packagemain.tech)