---
title: Comment configurer un registre dans shadcn
subtitle: ''
author: Abhijeet Dave
co_authors: []
series: null
date: '2025-10-27T14:27:20.419Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-registry-in-shadcn
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761575215365/54597001-a10f-4a3d-a082-3eb5ac8b9a7d.png
tags:
- name: shadcn
  slug: shadcn
- name: shadcn ui
  slug: shadcn-ui
seo_title: Comment configurer un registre dans shadcn
seo_desc: 'In this guide, you’ll learn how to set up a registry in shadcn. If you’re
  not familiar with this tool, shadcn is a collection of reusable and accessible components
  you can use in your projects.

  You’ll learn about essential concepts such as setting up...'
---

Dans ce guide, vous apprendrez comment configurer un registre dans shadcn. Si vous n'êtes pas familier avec cet outil, shadcn est une collection de composants réutilisables et accessibles que vous pouvez utiliser dans vos projets.

Vous découvrirez des concepts essentiels tels que la mise en place et la configuration du registre, l'ajout de l'authentification, les commandes CLI que vous pouvez utiliser, et bien plus encore.

## Table des matières :

* [Qu'est-ce qu'un registre dans shadcn ?](#heading-quest-ce-quun-registre-dans-shadcn)
    
* [Comment créer et configurer votre registre](#heading-comment-creer-et-configurer-votre-registre)
    
* [Système d'espaces de noms](#heading-systeme-despaces-de-noms)
    
* [Authentification pour les registres privés](#heading-authentification-pour-les-registres-prives)
    
* [Commandes CLI](#heading-commandes-cli)
    
* [Résolution des dépendances](#heading-resolution-des-dependances)
    
* [Gestion des erreurs](#heading-gestion-des-erreurs)
    
* [Conclusion](#heading-conclusion)
    

## **Qu'est-ce qu'un registre dans shadcn ?**

Un **registre** dans shadcn est un endroit central pour partager et gérer vos composants réutilisables, utilitaires et éléments d'interface utilisateur (ainsi que d'autres ressources) à travers différents projets. Il permet aux développeurs de numéroter et d'organiser les composants de manière standardisée. Cela facilite l'intégration et le partage des ressources au sein des équipes et entre elles.

Le système de registre aide à rendre ces composants facilement réutilisables. Il aide également les équipes à garder leur code propre et à gérer les dépendances plus efficacement.

Le système principal de shadcn utilise le fichier `registry.json`. Ce fichier fournit des informations clés sur le registre, telles que les noms des ressources et leurs emplacements, ainsi que les fichiers qui les accompagnent.

### Pourquoi utiliser un registre shadcn ?

L'utilisation de registres est utile car elle vous aide à standardiser les règles de vos composants. Chaque composant, élément d'interface utilisateur ou utilitaire suit un plan clair, ce qui facilite leur intégration et leur gestion.

De plus, les numéros de version vous permettent de gérer différentes versions d'un composant. Cela garantit que les diverses parties fonctionnent ensemble et vous permet de les mettre à jour sans problème.

Les registres vous donnent également la possibilité d'organiser les ressources en groupes tout en gérant les dépendances. Tout est flexible de cette manière.

Et si vous créez un registre, cela vous permet de partager vos composants avec d'autres développeurs (soit tout le monde, soit juste certaines personnes). Cela permet un travail interne ou en open source.

## Comment créer et configurer votre registre

La création d'un registre shadcn implique la mise en place d'un fichier de configuration (`registry.json`) à la racine de votre projet. Ce fichier contient les métadonnées et la structure de votre registre, aidant à définir les composants et leurs relations.

shadcn fournit ce [modèle de départ (starter template)](https://github.com/shadcn-ui/registry-template) pour vous aider à comprendre le fonctionnement des registres.

### Guide étape par étape pour créer un registre

#### 1\. Définir les métadonnées du registre

Vous devrez remplir les informations suivantes :

* `name` : Un nom unique pour le registre.
    
* `homepage` : Une URL pointant vers la page d'accueil du registre.
    
* `items` : Un tableau qui contient tous les composants, éléments d'interface utilisateur ou utilitaires disponibles dans le registre.
    

Voici un exemple d'un fichier `registry.json` simple :

```json
{
  "$schema": "<https://ui.shadcn.com/schema/registry.json>",
  "name": "acme",
  "homepage": "<https://acme.com>",
  "items": [
    // Les composants iront ici
  ]
}
```

#### 2\. Structure des composants

Chaque élément du registre peut être un composant, un thème, un hook ou un utilitaire. Ces éléments ont les propriétés suivantes :

* `name` : Nom unique du composant.
    
* `type` : Spécifie le type d'élément (par exemple, `registry:component`, `registry:block`).
    
* `files` : Un tableau de fichiers qui composent le composant.
    

Voici un exemple :

```json
{
  "name": "name",
  "type": "registry:block",
  "title": "title",
  "description": "Simple description",
  "files": [
    {
      "path": "registry/new-york/...",
      "type": "registry:component"
    }
  ]
}
```

Ce composant contient un bouton simple. Vous pouvez continuer à ajouter d'autres composants au tableau `items`.

#### 3\. Ajouter des composants

Après avoir créé le fichier `registry.json`, vous pouvez ajouter des composants au registre. Ces composants peuvent être des éléments d'interface utilisateur, des fonctions ou des utilitaires.

**Exemple 1 : Ajouter un composant bouton simple**

Tout d'abord, créez le fichier du composant. Vous pouvez définir votre composant dans un répertoire séparé. Par exemple, nous allons créer un composant `HelloWorld`.

```json
// registry/new-york/hello-world/hello-world.tsx
import { Button } from "@/components/ui/button"

export function HelloWorld() {
  return <Button>Hello World</Button>
}
```

Référencez le composant dans votre `registry.json` comme ceci :

```json
{
  "name": "hello-world",
  "type": "registry:block",
  "title": "Hello World",
  "description": "A simple hello world component.",
  "files": [
    {
      "path": "registry/new-york/hello-world/hello-world.tsx",
      "type": "registry:component"
    }
  ]
}
```

La clé `"files"` pointe vers le chemin où le composant est stocké, tandis que le `type` aide à catégoriser l'élément.

**Exemple 2 : Ajouter plusieurs composants**

Vous pouvez également ajouter plusieurs composants au registre. Par exemple, un bouton et un formulaire pourraient faire partie d'un package d'interface utilisateur :

```json
{
  "name": "ui-kit",
  "type": "registry:block",
  "title": "UI Kit",
  "description": "A collection of basic UI components.",
  "files": [
    {
      "path": "registry/ui-kit/button/button.tsx",
      "type": "registry:component"
    },
    {
      "path": "registry/ui-kit/form/form.tsx",
      "type": "registry:component"
    }
  ]
}
```

Cette approche modulaire permet un développement évolutif, facilitant les ajouts ou les mises à jour du registre sans affecter les autres parties de l'application.

> Vous pouvez en apprendre davantage sur les [bases du registre](https://ui.shadcn.com/docs/registry/getting-started) dans la documentation de shadcn UI.

## **Système d'espaces de noms**

Les espaces de noms (namespaces) dans shadcn aident à organiser les composants, utilitaires, thèmes ou autres ressources. L'objectif est d'éviter les conflits et de fournir une structure claire pour vos ressources.

### Qu'est-ce qu'un espace de noms ?

Un espace de noms regroupe des ressources sous un identifiant simple, généralement préfixé par un '@'. Grâce à cela, vous pouvez séparer différents types de ressources, des équipes, ou même des composants publics par rapport aux composants privés.

**Par exemple :**

* `@shadcn/button` pourrait représenter un composant bouton du registre de shadcn.
    
* `@acme/auth-utils` pourrait représenter des utilitaires d'authentification développés par l'entreprise Acme.
    

### Comment configurer plusieurs registres en utilisant des espaces de noms

Vous pouvez configurer plusieurs registres sous différents espaces de noms, ce qui aide à organiser les ressources par type ou par équipe :

```json
{
  "registries": {
    "@acme-ui": "<https://registry.acme.com/ui/{name}.json>",
    "@acme-docs": "<https://registry.acme.com/docs/{name}.json>",
    "@acme-ai": "<https://registry.acme.com/ai/{name}.json>",
    "@acme-internal": {
      "url": "<https://internal.acme.com/registry/{name}.json>",
      "headers": {
        "Authorization": "Bearer ${INTERNAL_TOKEN}"
      }
    }
  }
}
```

Cette configuration vous permet de :

* Séparer les composants d'interface utilisateur, la documentation, les ressources IA et les bibliothèques internes.
    
* Gérer facilement les ressources publiques et privées au sein de la même configuration de registre.
    

Vous pouvez en apprendre davantage sur les [**espaces de noms**](https://ui.shadcn.com/docs/registry/namespace#authentication--security) dans la documentation de shadcn UI.

## Authentification pour les registres privés

Si vous avez des registres privés, shadcn propose plusieurs méthodes d'authentification pour garantir que seuls les utilisateurs autorisés peuvent y accéder. Celles-ci incluent le jeton Bearer (OAuth 2.0), la clé API, l'authentification de base et l'authentification par paramètres de requête. Examinons chacune d'elles plus en détail.

### Jeton Bearer (OAuth 2.0)

Les jetons Bearer sont idéaux pour l'intégration avec des API externes comme GitHub ou des services internes prenant en charge OAuth 2.0.

Vous incluez le jeton dans l'en-tête `Authorization` de la requête. Vous obtenez généralement ce jeton via un flux OAuth 2.0, et il accorde l'accès aux ressources protégées.

Voici un exemple :

```json
{
  "@github": {
    "url": "<https://api.github.com/repos/org/registry/contents/{name}.json>",
    "headers": {
      "Authorization": "Bearer ${GITHUB_TOKEN}"
    }
  }
}
```

### Clé API

Les clés API sont couramment utilisées pour les registres NPM privés ou les API internes où une simple clé suffit pour le contrôle d'accès.

Une clé API est incluse dans les en-têtes de la requête, souvent sous `X-API-Key`. Cette clé est émise par le service et vous devez la garder confidentielle.

**Voici un exemple** :

```json
{
  "@private": {
    "url": "<https://api.company.com/registry/{name}>",
    "headers": {
      "X-API-Key": "${API_KEY}"
    }
  }
}
```

### Authentification de base (Basic Authentication)

Vous utiliserez généralement l'authentification de base dans les systèmes hérités qui nécessitent une authentification HTTP standard.

L'en-tête `Authorization` contient une chaîne encodée en base64 au format `utilisateur:motdepasse`. Bien qu'elle soit assez facile à mettre en œuvre, elle est moins sécurisée que les méthodes plus modernes comme OAuth 2.0.

**Voici un exemple** :

```json
{
  "@internal": {
    "url": "<https://registry.company.com/{name}.json>",
    "headers": {
      "Authorization": "Basic ${BASE64_CREDENTIALS}"
    }
  }
}
```

### Authentification par paramètres de requête

L'authentification par paramètres de requête est une forme plus simple d'authentification utilisant des paramètres dans l'URL pour les API.

Elle fonctionne en transmettant les détails d'authentification comme paramètres de requête dans l'URL. Bien que pratique, elle est moins sécurisée que d'autres méthodes car les paramètres de requête peuvent être exposés dans les journaux ou les URL.

**Voici un exemple :**

```json
{
  "@secure": {
    "url": "<https://registry.example.com/{name}.json>",
    "params": {
      "api_key": "${API_KEY}",
      "client_id": "${CLIENT_ID}",
      "signature": "${REQUEST_SIGNATURE}"
    }
  }
}
```

### Méthodes d'authentification multiples

Certains registres nécessitent plusieurs méthodes d'authentification simultanément – par exemple, une combinaison d'un jeton Bearer et d'une clé API.

La requête inclut plusieurs en-têtes et éventuellement des paramètres de requête pour satisfaire tous les mécanismes d'authentification requis. C'est courant dans les environnements d'entreprise où différentes couches de sécurité sont appliquées.

**Voici un exemple** :

```bash
{
  "@enterprise": {
    "url": "https://api.enterprise.com/v2/registry/{name}",
    "headers": {
      "Authorization": "Bearer ${ACCESS_TOKEN}",
      "X-API-Key": "${API_KEY}",
      "X-Workspace-Id": "${WORKSPACE_ID}"
    },
    "params": {
      "version": "latest"
    }
  }
}
```

Vous pouvez en apprendre davantage sur l' [**authentification et la sécurité**](https://ui.shadcn.com/docs/registry/namespace#authentication--security) dans la documentation de shadcn UI.

## Commandes CLI

La CLI de shadcn vous permet d'interagir avec le registre directement depuis la ligne de commande. Avec des commandes comme `add`, `view`, `search` et `list`, vous pouvez facilement installer et gérer les ressources. Examinons quelques exemples pour voir comment cela fonctionne.

### Installer des ressources depuis le registre

Utilisez les commandes suivantes pour ajouter des ressources à votre projet :

```bash
# Installer un composant spécifique
npx shadcn@latest add @acme/button

# Installer plusieurs composants à la fois
npx shadcn@latest add @acme/button @lib/utils @ai/prompt
```

Ces commandes récupèrent les composants spécifiés depuis le registre et les intègrent dans votre projet, en s'assurant que toutes les dépendances nécessaires sont également installées.

### Consulter les métadonnées

Avant d'intégrer un composant, il est crucial de comprendre sa structure et ses dépendances. La commande `view` vous permet d'inspecter les métadonnées d'un composant :

```bash
# Consulter un composant spécifique
npx shadcn@latest view @acme/button

# Consulter plusieurs composants
npx shadcn@latest view @acme/button @lib/utils @ai/prompt

# Consulter directement depuis une URL
npx shadcn@latest view https://registry.example.com/button.json

# Consulter depuis un fichier local
npx shadcn@latest view ./local-registry/button.json
```

Alors, qu'affiche la commande `view` ?

* Métadonnées de la ressource : Informations telles que le nom, le type et la description du composant.
    
* Dépendances : Liste les dépendances directes et de registre requises par le composant.
    
* Contenu des fichiers : Affiche le code réel qui sera installé.
    
* Variables CSS et configuration Tailwind : Montre toutes les configurations de style associées au composant.
    
* Variables d'environnement requises : Liste toutes les variables d'environnement nécessaires au bon fonctionnement du composant.
    

Cette commande est inestimable pour examiner les détails d'un composant avant l'installation, garantissant la compatibilité et la compréhension de ses exigences.

### **Rechercher des ressources**

Pour découvrir des composants au sein d'un registre, vous pouvez utiliser ces commandes :

```bash
# Rechercher dans un registre spécifique
npx shadcn@latest search @v0

# Rechercher avec une requête
npx shadcn@latest search @acme --query "auth"

# Rechercher dans plusieurs registres
npx shadcn@latest search @v0 @acme @lib

# Limiter les résultats
npx shadcn@latest search @v0 --limit 10 --offset 20

# Lister tous les éléments (alias pour search)
npx shadcn@latest list @acme
```

Elles vous aident à trouver des composants basés sur des critères tels que le registre, les termes de recherche et les limites de résultats.

En savoir plus sur les [**commandes CLI**](https://ui.shadcn.com/docs/registry/namespace#cli-commands) dans la documentation de shadcn UI.

## Résolution des dépendances

La CLI résout et installe automatiquement toutes les dépendances à partir de leurs registres respectifs.

Comprendre comment les dépendances sont résolues en interne est important si vous développez des registres ou si vous avez besoin de personnaliser des ressources tierces.

Dans shadcn, les composants dépendent souvent d'autres ressources provenant de divers registres. Lorsque vous installez un composant, shadcn s'assure que toutes ses dépendances sont également installées, même si elles résident dans des registres différents. Ce processus est connu sous le nom de **résolution des dépendances**.

### **Que signifie « résoudre les dépendances » ?**

Pour être clair, résoudre les dépendances implique l'identification, la récupération et l'installation des dépendances.

Tout d'abord, shadcn détermine quels composants une ressource nécessite pour fonctionner correctement. Ensuite, il récupère ces composants dépendants dans leurs registres respectifs. Enfin, il s'assure que toutes les dépendances sont installées avant le composant principal, en maintenant le bon ordre.

Ce processus garantit que lorsque vous installez un composant, tous ses prérequis sont également installés, assurant une fonctionnalité fluide.

### **Comprendre le tri topologique dans la résolution des dépendances**

Le **tri topologique** peut sembler compliqué, mais c'est essentiellement une méthode d'organisation des tâches (ou des composants) de manière à s'assurer que tout est fait dans le bon ordre.

Imaginez que vous ayez une liste de tâches, et que certaines tâches dépendent d'autres pour être terminées en premier. Par exemple, vous ne pouvez pas faire un gâteau sans d'abord mesurer puis mélanger les ingrédients. Ainsi, les tâches « mesurer les ingrédients » et « mélanger les ingrédients » doivent être terminées avant de « cuire le gâteau ».

Dans le contexte de shadcn, le tri topologique fonctionne de manière similaire pour organiser l'installation des composants :

* Chaque composant (comme `dashboard`) peut dépendre d'autres composants (comme `@shadcn/card` ou `@acme/data-table`).
    
* Le tri topologique organise les composants de sorte que chacun ne soit installé qu'après l'installation des composants dont il dépend.
    

#### Pourquoi le tri topologique est-il important ?

Le tri topologique s'occupe de plusieurs points clés. Premièrement, il s'assure que les composants sont installés dans le bon ordre. Par exemple, si le composant A dépend du composant B, alors le composant B sera installé en premier, suivi du composant A.

Il empêche également les dépendances circulaires. Si deux composants dépendent l'un de l'autre, le tri topologique détecte cela et empêche une boucle sans fin (également appelée dépendance circulaire).

#### Exemple de résolution de dépendances :

Considérez le composant suivant avec ses dépendances :

```json
{
  "name": "dashboard",
  "registryDependencies": [
    "@shadcn/card",
    "@v0/chart",
    "@acme/data-table"
  ]
}
```

Dans cet exemple, nous avons un **composant** : `dashboard` et ses **dépendances** : `@shadcn/card`, `@v0/chart` et `@acme/data-table`.

Dans ce cas, shadcn identifiera d'abord les dépendances en reconnaissant que `dashboard` dépend de `@shadcn/card`, `@v0/chart` et `@acme/data-table`. Ensuite, il récupérera ces composants dans leurs registres respectifs. Enfin, il installera `@shadcn/card`, `@v0/chart` et `@acme/data-table` en premier, avant d'installer `dashboard`, garantissant que tous les prérequis sont remplis.

Vous pouvez en apprendre davantage sur la [résolution des dépendances](https://ui.shadcn.com/docs/registry/namespace#authentication--security) dans la documentation de shadcn UI.

## **Gestion des erreurs**

La CLI de shadcn est équipée pour gérer plusieurs types d'erreurs. Voici quelques scénarios courants et comment les résoudre :

### **Erreurs courantes**

**1\. Registre inconnu (Unknown Registry)**

Cette erreur se produit lorsque le registre n'est pas défini dans la configuration.

Voici un exemple :

```json
Error: Unknown registry "@non-existent"
```

**Solution :** Pour corriger cela, ajoutez simplement le registre dans la section `registries` de votre configuration.

**2\. Variables d'environnement manquantes (Missing Environment Variables)**

Si votre registre nécessite certaines variables d'environnement qui ne sont pas définies, vous obtiendrez une erreur.

Voici un exemple :

```json
Registry "@private" requires REGISTRY_TOKEN
```

**Solution :** Pour corriger cela, ajoutez simplement les variables d'environnement requises à votre fichier `.env` ou `.env.local`.

**3\. 404 Non trouvé (404 Not Found)**

La ressource peut ne pas exister ou l'URL peut être incorrecte.

Voici un exemple :

```json
Error: The resource was not found at <https://api.company.com/button.json>
```

**4\. Échecs d'authentification (401/403)**

Si vous n'êtes pas autorisé à accéder à une ressource, vous verrez des erreurs 401 ou 403.

Pour corriger cela, assurez-vous que vos jetons, clés API ou identifiants sont valides.

Vous pouvez en apprendre davantage sur la [gestion des erreurs](https://ui.shadcn.com/docs/registry/namespace#authentication--security) dans la documentation de shadcn UI.

## Conclusion

Le système de registre shadcn fournit une solution modulaire efficace pour gérer et partager des composants ou des utilitaires entre projets. Si vous souhaitez explorer des mises en œuvre pratiques, des plateformes comme [shadcn/studio](https://shadcnstudio.com/) montrent comment vous pouvez exploiter les [composants shadcn](https://shadcnstudio.com/components) pour créer des solutions d'interface utilisateur élégantes et modernes avec une configuration minimale.

Grâce à son approche structurée des dépendances, ses espaces de noms flexibles, sa bonne authentification et ses commandes CLI, les registres permettent aux équipes de partager des ressources sécurisées et de les personnaliser au fur et à mesure.

J'ai préparé cet article avec l'aide de [Pruthvi Prajapati](https://github.com/PruthviPraj00), un développeur front-end avec 3 ans d'expérience.