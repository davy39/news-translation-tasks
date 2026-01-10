---
title: Architecture basée sur les composants dans Medusa – Comment construire des
  interfaces utilisateur robustes
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-05-18T18:22:11.000Z'
originalURL: https://freecodecamp.org/news/exploring-component-based-architecture-in-medusa-building-robust-user-interfaces
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-18-21-05-01.png
tags:
- name: components
  slug: components
- name: ecommerce
  slug: ecommerce
- name: User Interface
  slug: user-interface
seo_title: Architecture basée sur les composants dans Medusa – Comment construire
  des interfaces utilisateur robustes
seo_desc: "Medusa is a modern JavaScript framework that makes it easy to build robust\
  \ user interfaces. \nIt is built around a component-based architecture, which is\
  \ a design pattern that breaks down a UI into smaller, reusable components. This\
  \ makes it easier to..."
---

Medusa est un framework JavaScript moderne qui facilite la création d'interfaces utilisateur robustes.

Il est construit autour d'une architecture basée sur les composants, un modèle de conception qui décompose une interface utilisateur en composants plus petits et réutilisables. Cela facilite la maintenance et la mise à jour de l'interface utilisateur, ainsi que la création de nouvelles fonctionnalités.

Medusa est comme un ensemble LEGO pour construire des interfaces utilisateur. Tout comme les briques LEGO peuvent être assemblées et combinées pour créer diverses structures, Medusa vous permet de construire des interfaces utilisateur robustes en assemblant et en combinant des composants réutilisables.

Dans cet article, nous explorerons l'architecture basée sur les composants dans Medusa. Nous commencerons par discuter des avantages de l'utilisation de cette architecture, puis nous fournirons quelques exemples de code pour montrer comment vous pouvez l'utiliser pour construire des interfaces utilisateur.

## Avantages de l'architecture basée sur les composants

Il y a de nombreux avantages à utiliser l'architecture basée sur les composants dans Medusa. Certains des avantages les plus importants incluent :

* **Réutilisabilité** : Les composants peuvent être réutilisés à plusieurs endroits dans l'interface utilisateur, ce qui peut faire gagner du temps et des efforts.
* **Maintenabilité** : Les composants sont isolés les uns des autres, ce qui facilite la maintenance et la mise à jour de l'interface utilisateur.
* **Évolutivité** : Les composants peuvent être facilement ajoutés ou supprimés de l'interface utilisateur, ce qui facilite la mise à l'échelle de l'interface utilisateur selon les besoins.
* **Testabilité** : Les composants peuvent être facilement testés en isolation, ce qui facilite la vérification de leur bon fonctionnement.

## Comprendre le framework Medusa

Medusa est un framework et un ensemble d'outils complets pour construire des applications de commerce électronique. Il fournit les composants et l'infrastructure nécessaires pour développer, déployer et gérer des boutiques en ligne.

### Le backend de Medusa

Le backend de Medusa se concentre sur les opérations côté serveur et gère les fonctionnalités principales de l'application de commerce électronique. Il comprend des composants tels que :

* **Serveur** : Medusa fournit un serveur qui gère la logique et la gestion des données de l'application. Il facilite la communication entre le frontend et divers services, tels que les bases de données et les passerelles de paiement.
* **APIs** : Le backend expose un ensemble d'APIs (Interfaces de Programmation d'Applications) qui permettent au frontend et à d'autres applications d'interagir avec le serveur. Ces APIs définissent les points de terminaison et les structures de données pour effectuer des actions comme la récupération de produits, le traitement des commandes et la gestion des comptes utilisateurs.
* **Logique métier** : Le backend de Medusa implémente les règles et les flux de travail spécifiques au domaine du commerce électronique. Il gère des tâches telles que la gestion des stocks, le traitement des commandes, la gestion des paiements et l'application de réductions ou de promotions.
* **Intégrations de bases de données** : Le backend interagit avec une base de données pour stocker et récupérer des données liées aux produits, aux commandes, aux clients et à d'autres entités. Medusa prend en charge diverses bases de données, y compris PostgreSQL et MySQL, et fournit une couche d'abstraction pour simplifier les opérations de base de données.

Le backend de Medusa contient les répertoires et fichiers suivants :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-17-07-44-27.png)
_Backend de Medusa_

### Le frontend de Medusa

Le frontend de Medusa est responsable de la partie visible par l'utilisateur de l'application de commerce électronique. Il se concentre sur la fourniture d'une interface interactive et engageante pour que les clients puissent parcourir les produits, ajouter des articles à leur panier et finaliser l'achat. Le frontend comprend :

* **La vitrine** : Le composant de vitrine représente l'application où les utilisateurs interagissent avec la boutique de commerce électronique. Il comprend les listes de produits, la fonctionnalité de recherche, les détails des produits, le panier d'achat et le processus de paiement. Le frontend est responsable du rendu de ces composants et de la gestion des interactions utilisateur.
* **L'interface utilisateur (UI)** : Le frontend définit la disposition visuelle, le design et l'expérience utilisateur de l'application de commerce électronique. Il utilise HTML, CSS et JavaScript pour créer des interfaces réactives et conviviales. Medusa fournit des composants et des modèles d'interface utilisateur qui peuvent être personnalisés et étendus pour correspondre à la marque et aux exigences de la boutique en ligne.
* **Intégration avec les APIs backend** : Le frontend interagit avec les APIs backend fournies par le serveur Medusa. Il communique avec le serveur pour récupérer les données des produits, soumettre des commandes, mettre à jour les informations utilisateur et effectuer d'autres opérations. Le frontend utilise les données retournées par les APIs backend et les utilise pour rendre du contenu dynamique sur l'interface utilisateur.

Le frontend de Medusa contient les répertoires et fichiers suivants :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-17-07-45-21.png)
_Vitrine de Medusa_

Medusa est écrit en TypeScript et utilise React comme framework frontend. Medusa est divisé en trois parties principales : le `server`, la `storefront` et le panneau `admin`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-17-07-33-22.png)

Medusa est une solution de commerce électronique complète qui comprend divers outils et composants :

### Serveur

Medusa fournit un serveur qui gère les fonctionnalités principales d'une application de commerce électronique, telles que la gestion des catalogues de produits, le traitement des commandes et des paiements, et la gestion des comptes utilisateurs.

Voici comment accéder au backend :

```
cd my-medusa-store/backend
yarn start
```

Pour commencer avec Medusa, vous pouvez consulter [cet article](https://gatwirival.hashnode.dev/what-is-medusajs-and-why-use-it).

Lorsque nous exécutons `yarn start` dans le backend, par défaut, [localhost:9000](localhost:9000) est utilisé.

Naviguez vers [localhost:9000/store/products](localhost:9000/store/products) dans votre navigateur pour voir une collection JSON d'articles. Comme le seeder n'insère qu'un seul produit, il ne contiendra qu'un seul élément dans l'objet JSON.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-17-10-50-50-1.png)

### Vitrine

Medusa offre un composant de vitrine, qui est la partie visible par l'utilisateur de l'application. Il comprend le site web ou l'interface où les clients parcourent les produits, ajoutent des articles à leur panier et procèdent au processus d'achat.

```
cd my-medusa-store/storefront
yarn develop # pour la vitrine Gatsby
yarn dev # pour la vitrine Next.js
```

Comme j'utilise Next.js dans ma vitrine, j'utiliserai `yarn dev`. Lorsque nous exécutons `yarn dev` dans la vitrine, par défaut, [localhost:8000](localhost:8000) est utilisé.

Voici à quoi devrait ressembler la vitrine :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-17-11-58-02.png)

### Panneau d'administration

Medusa fournit un panneau d'administration qui permet aux propriétaires de boutiques ou aux administrateurs de gérer les opérations de commerce électronique. Il leur permet d'ajouter et de mettre à jour des produits, de traiter les commandes, de gérer les stocks, de configurer les options d'expédition et d'effectuer d'autres tâches administratives.

## Comment configurer le tableau de bord d'administration de Medusa

Pour configurer le tableau de bord d'administration de Medusa, suivez ces étapes :

Pour installer le package, vous devrez naviguer vers le répertoire de votre backend Medusa et exécuter la commande suivante pour installer le tableau de bord d'administration :

```
yarn add @medusajs/admin
```

Si vous utilisez npm, vous pouvez utiliser la commande suivante :

```
npm install @medusajs/admin
```

### Comment activer le plugin Admin dans le fichier de configuration de Medusa

Pour activer le plugin admin, ouvrez le fichier `medusa-config.js` dans votre projet et localisez le tableau `plugins`, puis ajoutez les lignes suivantes :

```
const plugins = [
  // ...
  {
    resolve: "@medusajs/admin",
    /** @type {import('@medusajs/admin').PluginOptions} */
    options: {
      // ...
    },
  },
]
```

Le plugin admin accepte diverses options de personnalisation :

* `serve` (par défaut : `true`) : Un booléen indiquant s'il faut servir le tableau de bord d'administration lorsque le backend Medusa démarre. Définissez-le sur `false` si vous préférez servir le tableau de bord d'administration séparément en utilisant la commande `yarn dev`.
* `path` (par défaut : `"app"`) : Une chaîne indiquant le chemin sur lequel le serveur admin doit s'exécuter. Il ne doit pas être préfixé ou suffixé avec une barre oblique ("/"), et il ne peut pas être l'un des chemins réservés : `"admin"` et `"store"`.
* `outDir` : Chemin facultatif spécifiant où sortir les fichiers de construction de l'admin.
* `autoRebuild` (par défaut : `false`) : Un booléen indiquant si l'interface utilisateur de l'admin doit être automatiquement reconstruite s'il y a des changements ou si une construction manquante est détectée lorsque le backend démarre. Si ce n'est pas défini, vous devez construire manuellement le tableau de bord d'administration.

Vous pouvez activer `autoRebuild` en le définissant sur `true` dans les options du plugin pour construire l'interface utilisateur de l'admin.

Exécutez le tableau de bord d'administration en utilisant la commande `yarn dev`.

Cette commande démarre à la fois le backend Medusa et le tableau de bord d'administration :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-17-13-23-52.png)

Par défaut, le tableau de bord d'administration sera accessible à l'adresse [localhost:9000/app](localhost:9000/app). Si vous avez défini une option de `path` personnalisée, l'admin sera disponible à l'adresse `localhost:9000/<PATH>`, où `<PATH>` est la valeur de l'option `path`. Vous pouvez en apprendre plus [ici](https://docs.medusajs.com/admin/quickstart).

Assurez-vous d'ajuster les configurations et les chemins selon votre configuration spécifique.

En suivant ces étapes, vous devriez être en mesure de configurer et d'accéder avec succès au tableau de bord d'administration de Medusa.

## Comprendre l'architecture basée sur les composants de Medusa

Medusa utilise une architecture basée sur les composants pour faciliter l'extension et la personnalisation. Chaque composant est autonome et peut être réutilisé dans d'autres parties de l'application. Cela facilite l'ajout de nouvelles fonctionnalités ou la modification de l'apparence de l'application sans affecter d'autres parties de la base de code.

Voici un exemple de composant de l'application de démarrage Medusa situé dans le dossier `storefront/src/modules/components/empty-cart-message` :

```js
import UnderlineLink from "@modules/common/components/underline-link"

const EmptyCartMessage = () => {
  return (
    <div className="bg-amber-100 px-8 py-24 flex flex-col justify-center items-center text-center">
      <h1 className="text-2xl-semi">Votre sac d'achat est vide</h1>
      <p className="text-base-regular mt-4 mb-6 max-w-[32rem]">
        Vous n'avez rien dans votre sac. Changeons cela, utilisez
        le lien ci-dessous pour commencer à parcourir nos produits.
      </p>
      <div>
        <UnderlineLink href="/store">Explorer les produits</UnderlineLink>
      </div>
    </div>
  )
}

export default EmptyCartMessage
```

Ce composant affiche un message lorsque le panier d'achat est vide. Le message inclut un lien vers la boutique afin que les utilisateurs puissent commencer à parcourir les produits.

Voici une analyse du code :

L'instruction `import UnderlineLink from "@modules/common/components/underline-link"` importe le composant `UnderlineLink` du module `@modules/common/components`. Ce composant sera utilisé pour rendre le lien vers la boutique.

L'instruction `const EmptyCartMessage = () => {` définit le composant `EmptyCartMessage`. Ce composant ne prend pas de props et retourne un élément `div` avec les attributs suivants : `className="bg-amber-100 px-8 py-24 flex flex-col justify-center items-center text-center"`.

L'instruction `return` retourne l'élément `div` avec le contenu suivant :

* Un élément `h1` avec le texte "Votre sac d'achat est vide".
* Un élément `p` avec le texte "Vous n'avez rien dans votre sac. Changeons cela, utilisez le lien ci-dessous pour commencer à parcourir nos produits.".
* Un élément `div` avec le composant `UnderlineLink` qui lie à la boutique.

## Medusa vs Shopify

Medusa est une alternative open-source à Shopify. Voici quelques comparaisons entre les deux produits :

### Personnalisation et flexibilité

Medusa offre un haut niveau de personnalisation et de flexibilité. Il permet aux développeurs de créer des applications de commerce électronique hautement personnalisées qui s'alignent sur des exigences commerciales spécifiques. Avec Medusa, les développeurs ont un contrôle total sur la base de code de l'application et peuvent personnaliser divers aspects, y compris les fonctionnalités frontend et backend.

Shopify offre un niveau de personnalisation moins granulaire par rapport à Medusa. Il fonctionne comme une plateforme hébergée, ce qui signifie que l'infrastructure principale et le backend sont gérés par Shopify. Bien que Shopify offre un système de personnalisation de thème et un écosystème d'applications pour étendre les fonctionnalités, il peut avoir des limitations lorsqu'il s'agit de mettre en œuvre des fonctionnalités hautement personnalisées.

### Hébergement et infrastructure

Medusa est un framework auto-hébergé, ce qui signifie que les développeurs doivent configurer leur propre environnement d'hébergement et gérer l'infrastructure eux-mêmes. Cela offre plus de contrôle et de scalabilité, mais nécessite également une expertise technique et des ressources supplémentaires.

Shopify est une plateforme entièrement hébergée, ce qui signifie que l'hébergement et la gestion de l'infrastructure sont gérés par Shopify. Cela élimine le besoin pour les développeurs de configurer et de maintenir des environnements d'hébergement, le rendant plus accessible aux utilisateurs non techniques.

### Tarification

En tant que framework open-source, Medusa est gratuit à utiliser et il n'y a pas de frais de licence. Cependant, comme il nécessite un hébergement auto-géré, il peut y avoir des coûts associés aux services d'hébergement et à la gestion de l'infrastructure.

Shopify fonctionne sur un modèle de tarification basé sur l'abonnement. Il offre différents plans tarifaires avec des fonctionnalités et des frais de transaction variables. Les frais d'abonnement couvrent l'hébergement, la sécurité et les services de support.

### Écosystème et intégrations d'applications

Medusa dispose d'un écosystème croissant d'extensions et d'intégrations, permettant aux développeurs de tirer parti d'outils et de services tiers pour améliorer leurs applications de commerce électronique. Bien que l'écosystème ne soit peut-être pas aussi étendu que celui de Shopify, la nature open-source de Medusa permet aux développeurs de créer des intégrations personnalisées selon les besoins.

Shopify dispose d'un vaste écosystème d'applications et d'intégrations disponibles via le Shopify App Store. Ces applications peuvent ajouter des fonctionnalités, étendre les fonctionnalités et s'intégrer à divers services tels que le marketing, l'analyse et les fournisseurs de services d'expédition. L'écosystème d'applications étendu de Shopify est l'une de ses principales forces.

### Public cible

Medusa convient aux entreprises qui nécessitent une personnalisation et une flexibilité avancées dans leurs applications de commerce électronique. C'est un choix adapté aux développeurs et aux entreprises disposant d'une expertise technique à la recherche d'un contrôle total sur leur infrastructure de commerce électronique.

Shopify est conçu pour répondre à un large éventail d'utilisateurs, y compris les petites et moyennes entreprises et les particuliers, qui souhaitent une solution de commerce électronique conviviale et sans tracas. Il convient aux utilisateurs ayant des connaissances techniques ou des ressources limitées qui privilégient la facilité d'utilisation et la commodité.

## Conclusion

L'architecture basée sur les composants est un modèle de conception puissant qui peut être utilisé pour construire des interfaces utilisateur robustes dans Medusa. En utilisant des composants, vous pouvez créer des interfaces utilisateur réutilisables, maintenables, évolutives et testables.

Medusa est un framework de commerce électronique complet qui comprend un serveur, un composant de vitrine et un panneau d'administration. Il fournit aux développeurs les outils nécessaires pour construire des applications de commerce électronique personnalisables et évolutives, adaptées à des besoins commerciaux spécifiques.

J'espère que cet article a été utile. N'hésitez pas à me faire savoir si vous avez des questions.