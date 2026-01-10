---
title: Construisez votre propre bascule de fonctionnalité avec Next.js et React en
  moins de 30 minutes
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2021-07-08T17:13:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-feature-toggles-in-next-js-and-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/thumb.jpg
tags:
- name: Next.js
  slug: nextjs
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: Construisez votre propre bascule de fonctionnalité avec Next.js et React
  en moins de 30 minutes
seo_desc: "This post will show you how to build the Feature Toggle mechanism in your\
  \ Next.JS application. \nWe are going to use Next.JS, React, and TypeScript. We\
  \ will deploy our application to Vercel to demonstrate the real-life example.\n\
  You can find the code a..."
---

Cet article vous montrera comment construire le mécanisme de bascule de fonctionnalité dans votre application Next.JS.

Nous allons utiliser Next.JS, React et TypeScript. Nous allons déployer notre application sur Vercel pour démontrer un exemple réel.

Vous pouvez trouver le **code** et la **vidéo** dans le résumé à la fin.

## **Ce que vous apprendrez dans cet article**

Dans cet article, nous allons approfondir plusieurs sujets tels que :

* Qu'est-ce que les bascules de fonctionnalité ?
* Comment utiliser l'API Context de React
* Qu'est-ce que les variables d'environnement et comment les utiliser dans nos applications ?
* Comment construire des hooks personnalisés dans React.

## **Qu'est-ce que les bascules de fonctionnalité ?**

Les bascules de fonctionnalité (aka Feature Flags) sont une technique qui permet de changer l'état de votre application sans modifier son code.

Au début, cela peut sembler un peu confus, mais considérons le scénario suivant : chaque décembre, de nombreuses entreprises changent leur logo pour ajouter un peu d'esprit de fête. Peut-être veulent-elles ajouter un chapeau de Père Noël dans leurs logos ou une sorte de bonhomme de neige.

Vous êtes-vous déjà demandé si elles changent leur site web chaque année juste pour mettre à jour le logo ? Non, dans la plupart des cas, elles ne le font qu'une seule fois et le connectent simplement à leur bascule de fonctionnalité. Ainsi, elles peuvent activer le logo spécial chaque fois qu'elles en ont besoin.

Voici un autre exemple : imaginez une équipe de développement qui suit l'intégration continue (CI). Ils utilisent ce mécanisme pour commiter du code non terminé, puis le fusionner sur la branche principale. Le code non terminé est désactivé sur l'environnement de production afin que les utilisateurs ne voient pas les fonctionnalités incomplètes.

Gardez à l'esprit que cela n'est une bonne idée que pour les équipes de développement matures qui ont des développeurs expérimentés à bord ainsi que des vérifications automatisées pour leurs pipelines CI (comme des tests automatisés, l'analyse statique de code, la compilation/bundling, etc.).

## **Avant de commencer**

Ce tutoriel nécessite quelques bases de Node et React. Vous devriez également savoir comment utiliser Git et GitHub avant de suivre les instructions de cet article.

J'ai sauté la partie sur l'initialisation de l'application exemple puisque j'ai montré un processus très similaire dans l'un de mes précédents articles. Si vous ne savez pas comment faire cela, ce n'est pas grave – consultez simplement les tutoriels ci-dessous sur freeCodeCamp (ils sont gratuits !) avant de commencer à suivre les instructions de cet article :

* [Git et Github pour débutants](https://www.youtube.com/watch?v=RGOj5yH7evk).
* [Apprendre Node.js - Tutoriel complet pour débutants](https://www.youtube.com/watch?v=RLtyhwFtXQA).
* [Apprendre React - Cours complet pour débutants](https://www.freecodecamp.org/news/learn-react-course/).
* [Comment construire une application serverless entièrement fonctionnelle en moins de deux heures](https://www.freecodecamp.org/news/how-to-build-a-serverless-app/) (optionnel).

J'ai créé deux dépôts GitHub pour cet article. Le premier contient l'échafaudage de l'application, afin que vous puissiez suivre toutes les étapes du tutoriel par vous-même. Le second est l'application terminée que vous pouvez déployer sur Vercel sans écrire de code si vous souhaitez simplement voir le résultat final.

* [Échafaudage de l'application (GitHub)](https://github.com/mateuszsokola/next-feature-toggle-scaffolder).
* [Application finale, prête à être déployée (GitHub)](https://github.com/mateuszsokola/next-feature-toggle-example).

Nous allons construire l'application exemple en utilisant Next.JS, React et Typescript. Le but principal de l'application est d'afficher deux graphiques financiers.

Le premier représente le PIB des États-Unis, et le second montre la maturité constante du Trésor sur les 10 dernières années.

Le second n'est pas terminé. Notre objectif est de le cacher derrière la bascule de fonctionnalité, afin que nous puissions l'activer chaque fois que nous en avons besoin.

L'application finale devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/article-1.png)

Vous pouvez [la trouver ici](https://next-feature-toggle-example.vercel.app/).

## **Commençons !**

Nous devons cloner le dépôt d'échafaudage depuis GitHub, et nous pouvons le faire en tapant la commande suivante dans le terminal :

```bash
$ git clone git@github.com:mateuszsokola/next-feature-toggle-scaffolder.git
```

Maintenant, nous devons installer les dépendances requises et démarrer le serveur.

```bash
$ cd next-feature-toggle-scaffolder
$ npm install
$ npm run dev

# SORTIE DE LA COMMANDE :
> next-feature-toggle-example@0.1.0 dev /Users/msokola/code/next-feature-toggle-scaffolder
> next dev

ready - server started on 0.0.0.0:3000, url: http://localhost:3000
info  - Using webpack 5. Reason: no next.config.js https://nextjs.org/docs/messages/webpack5
event - compiled successfully
event - build page: /
wait  - compiling...
event - compiled successfully
```

Maintenant, vous pouvez ouvrir [http://localhost:3000/](http://localhost:3000/) dans votre navigateur et voir le site web suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-08-at-14.17.03.png)

> Si vous vous demandez comment construire une application Next.JS à partir de zéro, vous pouvez apprendre à le faire à partir de [mon autre tutoriel ici](https://www.freecodecamp.org/news/how-to-build-a-serverless-app/).

Maintenant, comment pouvons-nous implémenter le mécanisme de bascule de fonctionnalité ici ? L'API Context de React semble être le moyen le plus facile et le plus approprié.

## Qu'est-ce que l'API Context de React ?

L'API Context de React offre un moyen propre et ordonné de transmettre des données à travers plusieurs niveaux de composants sans le faire manuellement. Regardons l'exemple suivant :

```jsx
<Page enabledFeatures={features} />
<PageLayout enabledFeatures={features} />
<NavigationBar enabledFeatures={features} />
<Link href="https://freecodecamp.org/news/">
  <Avatar enabledFeatures={features} />
</Link>
```

Si vous ne voulez pas utiliser Context, vous devrez transmettre les données en tant que propriétés à chaque composant. Cela est sujet aux erreurs et fastidieux. Si vous décidez d'utiliser le contexte, vous pouvez injecter des données directement dans le composant qui en a réellement besoin.

Maintenant, nous pouvons créer un contexte pour notre bascule de fonctionnalité. Nous devons créer un répertoire appelé `context/`, et un nouveau fichier dans ce répertoire. Nous pouvons l'appeler `FeatureToggleContext.ts`.

```bash
mkdir context
cd context
touch FeatureToggleContext.ts
```

Créer un contexte dans React est assez facile. Vous devez importer React dans votre fichier et appeler la méthode `React.createContext` avec la valeur de contexte par défaut. Voir l'exemple ci-dessous :

```typescript
// fichier : context/FeatureToggleContext.ts
import React from "react";

export const FeatureToggleContext = React.createContext({
    // TypeScript aura du mal à déterminer son type,
    // si nous ne castons pas ce tableau en un tableau de chaînes.
    // Probablement, nous allons finir avec un tableau de never ou any.
    enabledFeatures: [] as string[],
})
```

Gardez à l'esprit que la valeur par défaut n'est utilisée que lorsque le composant n'est pas enveloppé dans le fournisseur de contexte. Ce n'est qu'un secours, et il ne devrait pas être utilisé sans le fournisseur.

## Le composant fournisseur de contexte

Le contexte est livré avec un composant Provider qui permet aux composants consommateurs d'écouter les changements de contexte. Le composant Provider prend une propriété `value` que vous transmettez aux composants qui sont les enfants de ce fournisseur.

En termes simples, si nous voulons tirer parti du contexte, nous devrons faire du Provider un parent de tous nos composants. J'ai décidé d'envelopper le Provider dans un composant autonome afin de ne pas encombrer d'autres parties de l'application.

Créons un nouveau fichier dans le répertoire `components/` appelé `FeatureToggle.tsx` :

```bash
cd components
touch FeatureToggle.tsx
```

Maintenant, nous pouvons créer un composant qui accepte deux propriétés : `children` et `enabledFeatures`.

`children` est le composant principal de l'application. Si vous avez créé une application React en utilisant `create-react-app`, vous avez peut-être remarqué que le composant principal est appelé `App`. Next.JS l'appelle `MyApp`, et vous pouvez le trouver dans le fichier `pages/_app.tsx`.

`enabledFeatures` est le tableau des fonctionnalités activées. Nous allons l'utiliser plus tard.

```typescript
# fichier : components/FeatureToggle.tsx

import React from "react";
import { FeatureToggleContext } from "../context/FeatureToggleContext";

type Props = {
    children: any;
    enabledFeatures: string[];
}

export const FeatureToggle = ({ children, enabledFeatures }: Props) => {
    return (
        <FeatureToggleContext.Provider value={{ enabledFeatures }}>
            {children}
        </FeatureToggleContext.Provider>
    )
}
```

Le composant enveloppé est prêt. Maintenant, nous devons le connecter au composant principal. Ouvrons le fichier `pages/_app.tsx`.

Nous n'avons qu'une seule fonctionnalité basculable – `treasury_chart`. Nous devons l'ajouter à la liste des fonctionnalités activées. Pour l'instant, nous allons coder en dur cette liste et la transmettre directement au fournisseur pour confirmer que nous avons accès au contexte. Plus tard, nous allons créer une API appropriée pour la bascule de fonctionnalité.

Nous devons modifier le fichier pour qu'il ressemble à ceci :

```typescript
import { FeatureToggle } from "../components/FeatureToggle";
import "../styles/globals.css";

function MyApp({ Component, pageProps }) {
  const enabledFeatures = ["treasury_chart"];

  return ( 
    <FeatureToggle enabledFeatures={enabledFeatures}>
      <Component {...pageProps} />
    </FeatureToggle>
  );
}

export default MyApp;
```

Techniquement, la liste des fonctionnalités activées est maintenant disponible dans toute l'application. Mais nous n'avons pas d'interface pour consommer sa valeur. Tirer parti des hooks React est le meilleur moyen de l'exposer.

## Comment créer des hooks personnalisés dans React

Nous avons créé ce mécanisme basé sur l'API Context de React, et la manière la plus React de consommer le Context de React est d'utiliser des hooks. Nous devons donc créer un hook qui offre un accès facile aux bonnes données dans le contexte.

Créons un nouveau répertoire appelé `hooks/`, et un nouveau fichier appelé `useFeatureToggle.ts`.

```bash
mkdir hooks
touch useFeatureToggle.ts
```

Réfléchissons un instant au hook. Nous voulons vérifier le statut d'une fonctionnalité donnée. Si la fonctionnalité est activée, nous allons la rendre, sinon nous ne le ferons pas. Donc le hook devrait retourner un helper qui vérifie si la fonctionnalité demandée est dans la liste des fonctionnalités activées, n'est-ce pas ? Codons-le.

```typescript
# fichier : hooks/useFeatureToggle.ts

import React, { useContext } from "react";
import { FeatureToggleContext } from "../context/FeatureToggleContext";

export const useFeatureToggle = () => {
	// nous devons lire les valeurs définies dans le FeatureToggleContext.
    // Dans ce cas, nous ne prendrons que le tableau des fonctionnalités activées.
    const { enabledFeatures } = useContext(FeatureToggleContext);

    const isEnabled = (featureName: string) => {
        return enabledFeatures.includes(featureName);
    }

	// Pour la cohérence, nous retournons un tableau de helpers,
    // afin de suivre le modèle défini par le hook useState.
    // Cela rend le code ouvert aux extensions,
    // donc pas besoin de refactoriser l'application lorsqu'un nouveau helper est ajouté ici.
    return [
        isEnabled,
    ];
}
```

Le hook est prêt. Nous pouvons ouvrir la page principale et connecter le graphique du Trésor à la bascule de fonctionnalité.

Ouvrons `pages/index.tsx`.

Nous allons utiliser notre hook personnalisé pour obtenir un accès au helper `isEnabled`, et l'utiliser pour vérifier si la fonctionnalité est activée.

```typescript
const [isEnabled] = useFeatureToggle();

// ... 

return (
	/* ... */
    {isEnabled("treasury_chart") && (<TreasuryChart />)}
    /* ... */
);
```

L'implémentation complète ressemble à ceci :

```typescript
# fichier : pages/index.tsx

import React from "react";
import Head from "next/head";
import { Layout } from "antd";

import { GdpChart, TreasuryChart } from "../components/Charts";
import { useFeatureToggle } from "../hooks/useFeatureToggle";

const { Header, Content } = Layout;

export default function Home() {
  const [isEnabled] = useFeatureToggle();
  return (
    <Layout className="layout">
      <Head>
        <title>🚦 Feature Toggle in Next.js</title>
      </Head>
      <Header>
        <div className="logo" />
      </Header>
      <Content className="content">
        <GdpChart />
        {isEnabled("treasury_chart") && (<TreasuryChart />)}
      </Content>
    </Layout>
  );
}

```

Maintenant, vous pouvez essayer l'application dans votre navigateur. Gardez à l'esprit que vous verrez toujours le second graphique.

Vous pouvez jouer avec le nom de la fonctionnalité donné au helper `isEnabled`. Par exemple, vous pouvez faire une faute de frappe, et le graphique devrait disparaître ensuite.

Malheureusement, cette solution ne nous donne pas la flexibilité de basculer les fonctionnalités sans modifier la base de code. Chaque fois que nous voulons changer le statut de la fonctionnalité, nous devrons modifier la liste des fonctionnalités activées. Comment pouvons-nous corriger cela ?

Le moyen le plus simple de le rendre basculable sans changer le code serait d'implémenter une API qui lit les statuts des fonctionnalités à partir des variables d'environnement et retourne un tableau des fonctionnalités actives.

## Comment utiliser les variables d'environnement dans Node

Une variable d'environnement est une variable dont la valeur est définie en dehors de l'application, généralement par des fonctionnalités intégrées au système d'exploitation. Dans notre cas, c'est Node.JS.

Créons un fichier `.env` dans notre projet.

```bash
touch .env
```

Maintenant, nous pouvons ouvrir ce fichier et ajouter une nouvelle variable. Nous pouvons l'appeler `FEATURE_TREASURY_CHART`. Nous devons définir sa valeur à `false`.

```
# fichier : .env
FEATURE_TREASURY_CHART=false
```

Si nous utilisons des variables `.env`, nous devrons utiliser certaines fonctionnalités serveur de Next.JS et définir une nouvelle API. Cela signifie que nous devrons écrire plus de code.

Nous devons donc créer un nouveau fichier dans le répertoire `pages/api/`. Appelons-le `features.ts`.

L'API retournera un tableau des fonctionnalités activées.

```typescript
// fichier : pages/api/features.ts

export default (req, res) => {
    res.status(200).json([
    	// Vos variables d'environnement sont disponibles dans l'objet `process.env`.
    	// IMPORTANT ! Toutes les valeurs des variables d'environnement sont des chaînes.
        // Nous ne pouvons donc pas les comparer avec des booléens, des nombres, etc.
        process.env.FEATURE_TREASURY_CHART === "true" ? "treasury_chart" : "",
    ])
}
```

Maintenant, vous pouvez essayer d'ouvrir [http://localhost:3000/api/features](http://localhost:3000/api/features) dans votre navigateur, et vous devriez recevoir la sortie suivante :

```
[""]
```

Le `treasury_chart` n'a pas été ajouté à la liste des fonctionnalités activées, car il est désactivé. Vous pouvez changer la variable `FEATURE_TREASURY_CHART` à `true`, et redémarrer votre serveur pour l'essayer.

## Comment utiliser l'API des fonctionnalités

Nous sommes prêts à connecter la partie React de l'application à notre toute nouvelle API. Avant de le faire, nous devrons installer `axios`.

Axios nous aidera à faire des requêtes HTTP de manière plus pratique que `fetch`. Il supporte la gestion des erreurs et les types dès la sortie de la boîte. Nous n'avons pas besoin de l'implémenter nous-mêmes, donc nous pouvons passer directement aux affaires. Vous devrez peut-être tuer votre serveur en appuyant sur `Control + C`. Deux fois.

```
$ npm install --save axios
```

Créons un nouveau répertoire appelé `services/`, et un nouveau fichier appelé `FeatureToggle.ts`.

Maintenant, nous devons utiliser une fonction asynchrone standard pour faire une requête GET à notre API.

```typescript
// Fichier : services/FeatureToggle.ts

import axios from "axios";

export const fetchFeatures = async () => {
    try {
        const { data } = await axios.get<string[]>("/api/features");

        return data;
    }
    catch(e) {
        console.log("Something went wrong");
    }

    return [] as string[];
}
```

OK. La requête de l'API des fonctionnalités est prête. Nous pouvons en fait déclencher cette fonction au niveau du composant principal.

Ouvrez le fichier `pages/_app.tsx`.

Nous devons faire une requête API comme toutes les autres dans React en utilisant les hooks `useEffect` et `useState`. Nous devons ajouter le snippet suivant au composant `MyApp` :

```typescript
  const [enabledFeatures, setFeatures] = useState<string[]>([]);

  const processFeatures = async () => {
    const features = await fetchFeatures();

    setFeatures(features);
  }

  useEffect(() => {
    processFeatures();
  }, []);
```

La solution complète est ici :

```typescript
// fichier : pages/_app.tsx

import { useEffect, useState } from "react";
import { FeatureToggle } from "../components/FeatureToggleProvider";
import { fetchFeatures } from "../services/FeatureToggle";
import "../styles/globals.css";

function MyApp({ Component, pageProps }) {
  const [enabledFeatures, setFeatures] = useState<string[]>([]);

  const processFeatures = async () => {
    const features = await fetchFeatures();

    setFeatures(features);
  }

  useEffect(() => {
    processFeatures();
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  return (
    <FeatureToggle enabledFeatures={enabledFeatures}>
      <Component {...pageProps} />
    </FeatureToggle>
  )
}

export default MyApp;

```

Hourra ! Nous avons terminé avec le codage. La dernière étape est de déployer notre application.

## Comment publier l'application sur Vercel

Nous allons [déployer l'application sur Vercel](https://vercel.com/), car ils offrent un hébergement gratuit pour les applications et ils nous permettent de définir des variables d'environnement personnalisées, ce qui est crucial pour nous.

Comme d'habitude, je vais sauter le processus de création d'un nouveau compte. Vous pouvez en créer un en un clic en utilisant votre compte GitHub ou Google.

Une fois inscrit, vous devriez voir cet écran. Cliquez sur le bouton "_Nouveau Projet_" :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-08-at-18.12.06.png)

Maintenant, vous devez sélectionner le dépôt GitHub que vous souhaitez importer. Dans mon cas, c'est "_next-ft-demo_", mais vous avez peut-être appelé cela autrement. Si vous ne voyez pas votre dépôt, vous devez cliquer sur "_Ajuster les permissions de l'application GitHub_" (le lien ci-dessous marqué avec l'ellipse rouge) :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-08-at-18.14.51.png)

Nous devons configurer le projet. Ouvrons "_Variables d'environnement_", ajoutons une nouvelle variable appelée `FEATURE_TREASURY_CHART`, et définissons sa valeur à `false`. Ensuite, cliquez sur le bouton "_Ajouter_", et appuyez sur "_Déployer_" :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-08-at-18.18.47.png)

L'application est en cours de déploiement. Vous devriez voir l'écran suivant une fois terminé. Cliquez simplement sur le bouton "_Aller au tableau de bord_" :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-08-at-18.26.20.png)

Vous pouvez ouvrir votre application en cliquant sur le bouton "_Visiter_" :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-08-at-18.29.44.png)

L'application n'affiche qu'un seul graphique :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-08-at-18.32.53.png)

Si vous souhaitez activer le graphique du Trésor, vous devez sélectionner l'onglet "_Paramètres_", choisir la section "_Variables d'environnement_" et définir la variable `FEATURE_TREASURY_CHART` à `true` :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-08-at-18.35.37.png)

Maintenant, nous devons redéployer l'application pour charger les nouvelles variables.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-08-at-18.39.25.png)

Une fois le déploiement terminé, vous verrez le graphique du Trésor sur votre site web :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-08-at-18.42.06.png)

## **Résumé**

Il s'agit d'une implémentation simple des bascules de fonctionnalité. Vous devrez probablement l'ajuster pour qu'elle réponde à vos besoins. Mais je pense que c'est un bon point de départ sur lequel vous pouvez construire.

Si vous avez une idée pour améliorer ma solution ou si vous souhaitez nous montrer une autre façon de le faire, veuillez la partager sur le forum freeCodeCamp ou dans la section des commentaires de la vidéo YouTube ci-dessous (je réponds à chaque commentaire).

%[https://youtu.be/H9Tx5SqWX9o]

Si vous trouvez la vidéo utile, cela signifierait beaucoup pour moi si vous cliquez sur le bouton j'aime et vous abonnez.

**Vous pouvez trouver tout le code** sur **GitHub** :

* [Échafaudage de l'application avec Next.JS](https://github.com/mateuszsokola/next-feature-toggle-scaffolder).
* [Application finale avec Next.JS, prête à être déployée sur Vercel](https://github.com/mateuszsokola/next-feature-toggle-example).

Si vous avez des questions, vous pouvez m'envoyer un message direct sur Twitter : [@msokola](https://twitter.com/msokola)

J'espère que vous avez aimé et que vous passez une excellente journée 😊