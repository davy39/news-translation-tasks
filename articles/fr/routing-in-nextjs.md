---
title: Le routage dans Next.js – Comment utiliser l'App Router dans vos applications
  Next
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2023-08-24T15:13:32.000Z'
originalURL: https://freecodecamp.org/news/routing-in-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Article-Cover.png
tags:
- name: JavaScript
  slug: javascript
- name: Next.js
  slug: nextjs
- name: routing
  slug: routing
seo_title: Le routage dans Next.js – Comment utiliser l'App Router dans vos applications
  Next
seo_desc: "In the ever-evolving world of web development, Next.js has consistently\
  \ been a beacon of hope for developers seeking a balance between performance and\
  \ ease of use. \nWith the introduction of the App Router in 2023, the framework\
  \ has once again stirred..."
---

Dans le monde en constante évolution du développement web, Next.js a toujours été un phare d'espoir pour les développeurs cherchant un équilibre entre performance et facilité d'utilisation. 

Avec l'introduction de l'App Router en 2023, le framework a une fois de plus bouleversé les habitudes, laissant beaucoup d'entre nous se gratter la tête et se demander : "Devons-nous rester fidèles au répertoire Pages éprouvé ou adopter le tout nouveau App Router ?". 

Dans cette exploration, nous allons plonger dans les aspects uniques de l'App Router, offrant des conseils précieux pour naviguer dans ces nouvelles fonctionnalités.

## Prérequis

* Une bonne compréhension de JavaScript.
* Une bonne compréhension de React.js et Next.js.

## Un bref aperçu du routage

Le routage est un aspect critique des applications web qui permet aux utilisateurs de se déplacer entre diverses pages. Il garantit que les utilisateurs peuvent accéder à différentes parties d'une application, qu'ils passent d'une page d'accueil à une liste de produits ou qu'ils naviguent dans des applications monopages. 

Le répertoire Pages et l'App Router sont deux composants cruciaux qui déterminent comment les utilisateurs naviguent dans une application Next.js.

## Comment fonctionne le répertoire Pages dans Next.js

Alors que les projecteurs sont braqués sur le nouvel App Router, n'oublions pas la solide fondation fournie par le répertoire Pages. Une différence clé entre les deux réside dans la génération des routes.

Le répertoire Pages crée automatiquement des routes dans le dossier `pages`, tandis que l'App Router organise les routes dans le dossier `app`. Ce système de routage par dossier maintient la familiarité des développeurs avec le fonctionnement du routage tout en introduisant un changement dans l'organisation des routes.

Cette distinction permet une gestion efficace des routes et facilite une transition transparente entre les deux mécanismes de routage.

### Comment configurer le répertoire Pages

Pour configurer le répertoire Pages pour le routage, vous devez d'abord créer une application Next. Vous pouvez le faire en exécutant la commande suivante dans le terminal de votre machine locale ou de votre éditeur de code :

```bash
npx-create-next-app votre-nom-d-app
```

Une liste d'options de configuration apparaît sous votre commande. Sélectionnez "Non" pour `App Router` lors de la configuration de l'application. Cela crée un dossier pages à partir duquel vous pouvez créer des routes.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Folder-Directory-Setup-2.png)
_Installation et configuration du répertoire de dossiers_

### Comment créer une route avec le répertoire Pages

Pour créer une route, créez un dossier dans le dossier pages et appelez-le comme vous voulez que la route soit nommée (**about**, par exemple).

Ensuite, placez un fichier **index.js** dans le dossier **about** et remplissez-le avec le contenu que vous souhaitez.

Pour naviguer entre les pages, vous pouvez utiliser le composant `link` de Next.js et passer l'URL correspondante à laquelle vous souhaitez accéder.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Folder-Directory-Example---3.png)
_Exemple de répertoire de dossiers_

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Implementing-folder-routing.gif)
_Mise en œuvre du routage en utilisant le répertoire de dossiers_

### Limites du répertoire Pages

Le répertoire Pages offre une excellente façon de structurer les routes dans une application Next.js, mais il présente certaines limites. Voici quelques points à garder à l'esprit :

* Exportations statiques : La configuration du répertoire Pages repose sur des routes dynamiques générées à l'aide de `getStaticProps` et `getStaticPaths`. Cela signifie que toutes les pages du répertoire ne peuvent pas être exportées statiquement.
* Configuration de l'Edge Runtime : Si vous utilisez l'Edge Runtime, vous devrez peut-être effectuer une configuration supplémentaire au-delà de ce qui est possible dans le répertoire Pages.
* Routage d'internationalisation : Bien que Next.js supporte le routage d'internationalisation, vous devez configurer les locales, les locales par défaut et les locales spécifiques au domaine dans le fichier **next.config.js** plutôt que dans le répertoire Pages.
* Fonctions serverless : Les routes API définies dans le répertoire Pages peuvent gérer les fonctionnalités de base de l'API, mais des fonctions serverless plus complexes peuvent nécessiter une configuration supplémentaire et un placement alternatif des fichiers.
* Distribution des pages générées statiquement : Les pages générées statiquement peuvent ne pas être optimisées pour les visiteurs sans configuration supplémentaire de CDN ou "vendoring". Cela peut impacter les performances et la distribution des pages générées statiquement. 

## Comment fonctionne l'App Router dans Next.js

L'App Router est la nouvelle venue sur la scène Next.js, conçue pour répondre à certaines des limites de l'approche du répertoire Pages. Bien que l'App Router utilise toujours le répertoire de dossiers pour le routage, il le fait avec une convention légèrement différente.

### Comment configurer l'App Router

Pour configurer l'App Router, suivez le même processus d'installation que mentionné pour le répertoire Pages, mais choisissez "Oui" lorsque vous êtes invité à utiliser l'`App Router` lors de la configuration. Cela crée un répertoire **app**.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/App-router-Setup-2.png)
_Installation et configuration de l'App Router_

### Comment créer une route avec l'App Router

Le routage avec l'App Router implique également la création de dossiers, mais dans le répertoire **app**. Placez un fichier **page.js** dans le dossier approprié pour définir votre route.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/App-router-Example-2.png)
_Exemple de répertoire de dossiers_

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Implementing-app-routing.gif)
_Mise en œuvre du routage en utilisant l'App Router_

## Fonctionnalités de l'App Router dans Next.js

Outre le routage, l'App Router offre une gamme d'autres fonctionnalités, notamment :

### Composant de mise en page

Un composant de mise en page est un élément d'interface utilisateur polyvalent qui façonne la structure d'une page. Il peut inclure des composants comme des en-têtes, des pieds de page et des barres latérales, et même offrir des fonctions partagées comme la navigation.

Les composants de mise en page fonctionnent avec le routage, permettant des transitions fluides entre les pages de l'application. Comme le composant de mise en page reste actif lorsque les routes changent, son état est conservé, assurant des mises en page cohérentes et réutilisables avec un minimum d'effort. 

Ce composant est conçu pour recevoir une prop `children` et envelopper tous les fichiers de page dans le même répertoire avec celui-ci :

```js
export default function layout({ children }) {
  return <div className="layout">{children}</div>;
}

```

Voici un exemple qui utilise un composant de mise en page (une boîte grise) comme celui dans le code ci-dessus entre la page utilisateur et la page des paramètres :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Layout-example-2.png)
_Création d'un composant de mise en page qui partage des styles avec ses pages sœurs_

Dans l'image ci-dessus, le composant **layout.js** est partagé par les pages utilisateur et paramètres. Ainsi, les deux pages auront les styles et la logique du composant de mise en page.

Et le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Implementing-layouts.gif)
_Mise en œuvre du composant de mise en page sur la page utilisateur et la page des paramètres_

### Mises en page imbriquées

Ce sont des mises en page définies à l'intérieur de dossiers et qui s'appliquent à des segments de route spécifiques et se rendent lorsque ces segments sont actifs. Cela permet de définir plusieurs niveaux de composants de mise en page, chacun enveloppant le contenu de ses composants enfants. 

Cette fonctionnalité offre une manière flexible et modulaire de structurer l'interface utilisateur de votre application.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/nested-layouts.png)
_Démonstration du fonctionnement des mises en page avec les pages sœurs et enfants_

Dans le diagramme ci-dessus, les styles et la logique du premier fichier de mise en page s'appliquent à toutes les pages à l'intérieur du répertoire **dashboard**, tandis que le deuxième fichier de mise en page s'applique aux pages du répertoire **developer**.

### Composants de modèle

Les composants de modèle sont similaires aux mises en page, mais ils créent une nouvelle instance pour chaque enfant lors de la navigation. Cela signifie recréer des éléments DOM, perdre l'état et réinitialiser les effets à chaque changement de route. 

Vous pouvez les utiliser pour des choses comme le suivi des vues de page ou des widgets interactifs. Vous pouvez créer un modèle en exportant un composant React par défaut depuis un fichier `template.js`. Ce composant doit être conçu pour recevoir une prop children.

```js
export default function Template({ children }) {
  return <div>{children}</div>
}
```

### Composant de chargement

Ce composant peut être créé dans n'importe quel répertoire de dossier d'application. Il enveloppe automatiquement les pages avec une frontière de suspense React (c'est-à-dire un composant qui aide à gérer les moments de chargement lorsque les composants doivent récupérer des données ou des ressources de manière asynchrone). Il s'affiche au premier chargement et pendant la navigation entre les routes sœurs.

Cela ressemble à quelque chose comme ceci sous le capot :

```js
<Suspense fallback={<Loading />}>
   <YourComponent />
</Suspense>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/loading-component.png)
_Présentation du composant de chargement en utilisation_

### Streaming

Cela implique l'envoi de parties d'une page web progressivement du serveur vers l'appareil de l'utilisateur. Contrairement au rendu côté serveur (SSR) traditionnel, où toutes les données doivent être récupérées avant le rendu, le streaming envoie de plus petits morceaux de HTML dès qu'ils sont prêts. 

**Avant le streaming**

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Before-streaming.png)
_Affichage du fonctionnement du SSR avant l'introduction du streaming_

Dans l'image ci-dessus, aucun contenu n'est affiché pendant que la page est en cours de rendu. Le composant attend que tous les contenus soient prêts.

**Utilisation du streaming**

![Image](https://www.freecodecamp.org/news/content/images/2023/08/using-streaming.png)
_Comment le SSR fonctionne maintenant avec le streaming_

Dans l'image ci-dessus, le composant n'attend pas tout le contenu de la page, il rend chaque élément dès qu'il est prêt. 

Cela accélère l'affichage initial de la page, en donnant la priorité aux composants de haute priorité pour une interactivité précoce. Le streaming réduit le [Time To First Byte](https://en.wikipedia.org/wiki/Time_to_first_byte#:~:text=Time%20to%20first%20byte%20(TTFB,received%20by%20the%20client's%20browser.) (TTFB), améliore l'interactivité et fonctionne bien avec le modèle de composant de React.

Il fonctionne en utilisant le composant `<Suspense>`, améliorant le chargement et l'expérience utilisateur, surtout sur les appareils plus lents.

### Composant d'erreur

Ce composant confine les erreurs à la plus petite section de l'application. La création d'un fichier d'erreur enveloppe automatiquement la page avec une frontière d'erreur React. Toute erreur dans le dossier de ce fichier remplace le composant par son contenu.

Le composant d'erreur est rendu comme ceci en arrière-plan :

```js
<Layout>
  <ErrorBoundary fallback={<Error />}>
    <Page/>
  </ErrorBoundary>
</Layout>
```

Et affiche quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/error-layout.png)
_Présentation du composant d'erreur en cas d'erreur_

### Groupes de routes

Les groupes de routes organisent les routes dans le répertoire de l'application sans modifier les chemins d'URL. En enfermant un nom de dossier entre parenthèses, vous créez un groupe de routes qui maintient les routes connexes ensemble. 

Cela permet un regroupement logique, des mises en page imbriquées et une structure d'URL propre. C'est-à-dire :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/route-groups.png)
_Comment utiliser les groupes de routes pour organiser les routes_

Dans l'exemple ci-dessus, les pages d'authentification sont regroupées pour une meilleure organisation, sans modifier la structure de l'URL.

### Composants serveur 

Les composants serveur, une ajout majeur à l'App Router, sont rendus sur le serveur et diffusés vers le client. Cela accélère le chargement des pages et améliore les performances. Ils accélèrent les temps de chargement des pages car différents contenus de page sont chargés en petits morceaux et indépendamment.

Notez qu'ils ne supportent pas les actions côté client comme les événements de clic et les hooks React (`useState`, `useRef`). Pour convertir un composant serveur en composant client, marquez-le avec `use client` au début du fichier. 

Voici un exemple :

```js
'use client'
 
import { useState } from 'react'
 
export default function Counter() {
  const [count, setCount] = useState(0)
 
  return (
    <div>
      <p>Vous avez cliqué {count} fois</p>
      <button onClick={() => setCount(count + 1)}>Cliquez-moi</button>
    </div>
  )
}
```

### Récupération de données

Les composants serveur apportent un nouveau modèle de récupération de données, permettant aux composants `async` de récupérer des données à l'intérieur d'eux. Cela réduit la dépendance aux API comme `getServerSideProps`. 

Pour récupérer des données, marquez un composant comme `async` et utilisez la fonction fetch à l'intérieur :

```js
export default async function Home() {
  const response = await fetch("https://api.adviceslip.com/advice");
  const data = await response.json();
  return (
    <main>
      <h1>Page d'accueil</h1>
      <p>{data.slip.advice}</p>
    </main>
  );
}
```

Et obtenez votre résultat sur la page comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/fetch.png)
_Utilisation de la fonction fetch dans un composant serveur_

  
L'App Router met également en cache les données récupérées sur le serveur, éliminant le besoin de récupérer à nouveau ces données à chaque requête, sauf si un paramètre de révalidation est passé dans la fonction fetch :  


```js
export default async function Home() {
  const response = await fetch("https://api.adviceslip.com/advice", {
    next: { revalidate: 5 },
  });
```

Le code ci-dessus provoque une nouvelle récupération de données toutes les 5 secondes.

### SEO intégré

Une autre fonctionnalité de l'App Router de Next.js est l'API Metadata intégrée, utilisée comme outil SEO pour optimiser les sites web pour les moteurs de recherche. Cette API fournit une gamme de paramètres SEO, y compris le [protocole Open Graph](https://ogp.me/), pour améliorer la visibilité des sites web pour les moteurs de recherche.

Il existe deux méthodes pour implémenter cela — les méthodes statique et dynamique.

Voici l'approche statique :

```js
import { Metadata } from "next";

export const Metadata = {
  title: "Titre de la page de blog",
  description: "Description de la page de blog",
};

export default function page() {
  return (
    <main>
      <h1>Page de blog</h1>
    </main>
  );
}
```

Voici l'approche dynamique utilisant la fonction `getMetadata` :

```js
export async function generateMetadata({ params, searchParams}) {

const id= params.id

   const blog= await fetch(`https://blog/${id}`).then((res) =>res.json()

  return { 
        title: blog.title,
        Description: blog.description,
   };

}

export default function Page({ params, searchParams }) {}

```

## Fonctionnalités avancées de l'App Router dans Next.js

Bien que nous ayons couvert des aspects notables, les capacités de l'App Router s'étendent au-delà de ce que nous avons discuté. Des fonctionnalités comme les actions serveur, la révalidation des données, les routes parallèles et l'interception des routes offrent une utilité supplémentaire.

Comme toujours, vous pouvez vous tourner vers la [documentation Next.js](https://nextjs.org/docs) pour une gamme plus large d'informations afin d'élever votre compréhension et votre maîtrise de ces ajouts à l'écosystème Next.js.

## Répertoire Pages vs App Router - Lequel utiliser ?

Dans le monde en rapide évolution du développement web, il est facile de se laisser emporter par l'engouement entourant les nouvelles technologies et outils. Cependant, lorsqu'il s'agit de choisir entre le répertoire Pages et l'App Router, il est important de trouver un équilibre entre excitation et prudence.

Les deux options ont leurs propres forces et considérations, et comprendre vos besoins et objectifs vous aidera à déterminer lequel utiliser dans un contexte donné.

### Sélection de l'outil approprié pour vos besoins

Lors du choix entre le répertoire Pages et l'App Router, il est crucial de prendre en compte vos besoins et objectifs individuels. Voici quelques facteurs à garder à l'esprit :

1. Stabilité vs Flexibilité : Si vos principales préoccupations sont la stabilité et la convivialité, le répertoire Pages est une option fiable. Il fournit une base solide pour les tâches de routage simples. Cependant, si vous avez besoin de plus de flexibilité et de la capacité à personnaliser, l'App Router pourrait être un choix plus approprié.

2. Vitesse de développement : Le répertoire Pages offre une approche rapide et efficace pour créer et gérer des pages, ce qui le rend idéal pour un développement rapide. En revanche, en raison de ses capacités avancées, l'App Router peut nécessiter plus de configuration et d'efforts de développement initiaux.

3. Scénarios de routage complexes : Si votre application nécessite des scénarios de routage complexes comme des routes imbriquées ou un routage dynamique basé sur des données externes, la programmabilité de l'App Router peut être un avantage significatif.

En fin de compte, la clé pour prendre des décisions éclairées réside dans le fait de rester informé sur les capacités et les compromis des deux, le répertoire Pages et l'App Router.

## Conclusion

En résumé, vous avez maintenant une bonne compréhension de l'App Router de Next.js et de ses fonctionnalités.

Vous avez appris comment structurer les routes en utilisant à la fois le répertoire Pages et l'App Router, ainsi que des fonctionnalités avancées telles que les composants de mise en page, les composants serveur et la récupération de données.

En explorant ces sujets, vous avez non seulement acquis des informations sur les capacités de ces outils, mais vous avez également appris comment choisir entre la nouvelle approche (App Router) et l'ancienne approche utilisant le répertoire Pages.

Avec cette connaissance, vous êtes bien préparé pour prendre des décisions éclairées et créer des expériences web exceptionnelles dans le paysage en constante évolution du développement web. 

## Informations de contact

Vous souhaitez me contacter ? N'hésitez pas à me contacter via les liens suivants :

* Twitter, désolé (X) 😂 : [@jajadavid8](https://twitter.com/JajaDavid8)
* LinkedIn : [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
* Email : Jajadavidjid@gmail.com