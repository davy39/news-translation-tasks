---
title: Comment construire des Micro Frontends en React avec Vite et Module Federation
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2025-08-26T20:48:20.948Z'
originalURL: https://freecodecamp.org/news/how-to-build-micro-frontends-in-react-with-vite-and-module-federation
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756231755011/283b9e67-9a09-4241-9d90-701cb075084d.jpeg
tags:
- name: React
  slug: reactjs
- name: module federation
  slug: module-federation
- name: vite
  slug: vite
- name: Microfrontend
  slug: microfrontend
seo_title: Comment construire des Micro Frontends en React avec Vite et Module Federation
seo_desc: 'Micro Frontend Architecture has become increasingly popular in recent years,
  as teams look to re-use parts of their existing applications in new projects rather
  than rebuilding everything from scratch.

  Micro frontends also allow large teams to share ...'
---

L'architecture Micro Frontend est devenue de plus en plus populaire ces dernières années, car les équipes cherchent à réutiliser des parties de leurs applications existantes dans de nouveaux projets plutôt que de tout reconstruire de zéro.

Les micro frontends permettent également aux grandes équipes de partager des composants communs – tels que les en-têtes (headers), les pieds de page (footers) et les modules de connexion – sur plusieurs applications, garantissant ainsi la cohérence et respectant le principe DRY (Don’t Repeat Yourself).

Dans cet article, vous apprendrez :

* Comment mettre en place un projet et une structure de dossiers implémentant une infrastructure Micro Frontend (MFE).
* Comment utiliser et configurer `@originjs/vite-plugin-federation` pour permettre l'usage de Module Federation (MF) avec des projets Vite.
* Comment partager et consommer des composants React entre plusieurs applications.
* Comment exécuter et tester localement votre application avec des composants partagés.

## Table des matières

* [Prérequis](#heading-prerequis)
* [Qu'est-ce que Module Federation ?](#heading-quest-ce-que-module-federation)
* [Avantages de Module Federation](#heading-avantages-de-module-federation)
* [Structure du projet](#heading-structure-du-projet)
* [Comment créer les projets](#heading-comment-creer-les-projets)
* [Comment installer les dépendances](#heading-comment-installer-les-dependances)
* [Comment configurer l'application distante (Remote)](#heading-comment-configurer-lapplication-distante)
* [Le plugin Vite Module Federation](#heading-le-plugin-vite-module-federation)
* [Contraintes clés sur les modules exportés](#heading-contraintes-cles-sur-les-modules-exportes)
* [Comment créer les composants distants](#heading-comment-creer-les-composants-distants)
* [Comment consommer les composants distants au sein de l'hôte](#heading-comment-consommer-les-composants-distants-au-sein-de-lhote)
* [Comment gérer les erreurs TypeScript](#heading-comment-gerer-les-erreurs-typescript)
* [Comment ajouter RemoteWrapperComponent à App.tsx](#heading-comment-ajouter-remotewrappercomponent-a-apptsx)
* [Comment servir l'application distante et exécuter votre hôte](#heading-comment-servir-lapplication-distante-et-executer-votre-hote)
* [La véritable puissance des Micro Frontends](#heading-la-veritable-puissance-des-micro-frontends)
* [Dernières réflexions](#heading-dernieres-reflexions)

## Prérequis

* Node installé sur votre machine – vous pouvez le télécharger [ici](https://nodejs.org/en/download).
* Familiarité avec JS / TS et React.
* Familiarité avec la ligne de commande / le terminal.

## Qu'est-ce que Module Federation ?

Avant d'aller plus loin, parlons de Module Federation (MF).

Module Federation est une technique de développement web qui permet à plusieurs builds séparés de fonctionner ensemble comme une seule application. Elle permet le partage de code entre différentes applications indépendantes au moment de l'exécution (runtime), plutôt qu'au moment du build. Cela signifie qu'une application hôte peut charger et exécuter dynamiquement du code provenant d'une application distante.

À la base, Module Federation utilise une architecture **"hôte" (host)** et **"distante" (remote)**. Une application **hôte** est l'application principale qui consomme le code / les composants partagés. Une application **distante** est celle qui expose le code à consommer.

L'application distante spécifie **quelles** parties de son code, ou "modules", sont disponibles pour les autres. L'hôte référence ensuite ces modules et les charge selon les besoins.

## Avantages de Module Federation

### Déploiement indépendant

Module Federation permet aux équipes de construire et de déployer leurs micro-frontends séparément. Cela élimine le besoin de redéploiements complets de l'application, accélérant ainsi le développement et réduisant les risques.

### Partage de code efficace

MF offre un moyen natif de partager du code et des dépendances entre micro-frontends. Cela évite la duplication de code, réduisant ainsi la taille des bundles et garantissant la cohérence.

### Gains de performance

En partageant les dépendances, Module Federation réduit la taille globale du bundle et améliore les temps de chargement initiaux, car chaque micro-frontend ne télécharge pas sa propre copie des bibliothèques communes.

### Évolutivité et maintenabilité

MF permet une architecture évolutive en décomposant les grandes applications en micro-frontends plus petits et gérables. Cela rend la base de code plus facile à maintenir et permet aux équipes de travailler de manière indépendante.

### Analogie

Imaginez la construction d'une boutique en ligne. Traditionnellement, vous créeriez l'ensemble du site – page d'accueil, pages produits, panier, profil utilisateur – comme une seule grande application. Un petit changement au niveau du panier nécessiterait de tout reconstruire et de tout redéployer.

Avec les Micro Frontends et Module Federation, le panier d'achat peut être sa propre application, construite et maintenue par une équipe dédiée. Le site principal l'importe simplement, permettant à l'équipe du panier de publier des mises à jour indépendamment, accélérant le développement et améliorant la concentration.

Cela fonctionne également pour les organisations possédant plusieurs sites nécessitant une apparence cohérente. Des composants partagés comme un en-tête, un pied de page ou une fiche produit peuvent être réutilisés sur des sites aux objectifs différents (ex: location de véhicules ou vente de meubles), garantissant la cohérence visuelle tout en gardant une fonctionnalité unique.

## Structure du projet

Vous devrez créer deux projets :

* **host** – celui-ci servira d'application hôte.
* **remote** – celui-ci exposera les composants que vous souhaitez partager.

## Comment créer les projets

Exécutez les commandes suivantes dans votre terminal pour créer votre dossier racine et vos deux projets Vite :

```bash
# créer le répertoire micro-frontends pour les deux projets vite, et naviguer dedans
mkdir micro-frontends; cd micro-frontends
```

### Créer un dépôt Git (Optionnel)

Avec la commande ci-dessous, vous pouvez créer un dépôt Git pour le contrôle de source.

```bash
# initialiser le dépôt git
git init
```

```bash
# créer l'application vite hôte
npm create vite@latest host-app

# une fois la commande soumise, sélectionnez React et appuyez sur Entrée, 
Select a framework:
│  ○ Vanilla
│  ○ Vue
│  ● React
│  ○ Preact
│  ○ Lit
│  ○ Svelte
│  ○ Solid
│  ○ Qwik
│  ○ Angular
│  ○ Marko
│  ○ Others

# sélectionnez Typescript + SWC et appuyez à nouveau sur Entrée
Select a variant:
│  ○ TypeScript
│  ● TypeScript + SWC
│  ○ JavaScript
│  ○ JavaScript + SWC
│  ○ React Router v7 
│  ○ TanStack Router
│  ○ RedwoodSDK 
│  ○ RSC 
```

Une fois cela fait, revenez au dossier racine du projet (`micro-frontends`) :

```bash
# revenir en arrière
cd ../

# créer remote-app 
npm create vite@latest remote-app

# suivez les instructions comme précédemment pour sélectionner React, Typescript + SWC
```

Vous avez maintenant vos deux projets, `host-app` et `remote-app`.

## Comment installer les dépendances

Ouvrez le dossier `micro-frontends` dans votre IDE / éditeur de code préféré. Dans ce tutoriel, j'utiliserai VS Code.

Astuce : Vous pouvez ouvrir le dossier actuel dans VS Code via votre terminal en utilisant la commande `code .` si vous avez déjà ajouté `code` à votre PATH.

Une fois VS Code ouvert, ouvrez le terminal et exécutez la commande suivante :

```bash
cd host-app && npm install -D @originjs/vite-plugin-federation
```

et ensuite exécutez :

```bash
cd ../remote-app && npm install -D @originjs/vite-plugin-federation
```

### Styling

Pour obtenir un rendu visuel similaire à mes exemples, vous devez ajouter Tailwind CSS à vos deux applications (remote et host). Vous trouverez les instructions sur la façon de procéder [ici](https://tailwindcss.com/docs/installation/using-vite).

## Comment configurer l'application distante

Pour pouvoir utiliser des modules et des composants de vos applications distantes, vous devez configurer votre application pour qu'elle expose ces modules, et votre application hôte pour qu'elle les consomme.

Utilisez les configurations suivantes dans vos applications pour permettre l'exposition et la consommation de vos composants – ne vous inquiétez pas pour les composants pour l'instant, vous les créerez bientôt.

### Application Hôte – `vite.config.ts`

Dans l'application `host`, ouvrez `vite.config.js` et ajoutez la configuration suivante :

```typescript
//host - vite.config.js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import federation from "@originjs/vite-plugin-federation";


export default defineConfig({
  plugins: [
    react(),
    federation({
      name: "host_app",
      remotes: {
        remote_app: "http://localhost:5001/assets/remoteEntry.js",
      },
      shared: ["react", "react-dom"],
    }),
  ],
  build: {
    modulePreload: false,
    target: "esnext",
    minify: false,
    cssCodeSplit: false,
  },
});
```

### Application Distante – `vite.config.ts`

Dans l'application `remote`, ouvrez `vite.config.js` et ajoutez la configuration suivante :

```typescript
// remote - vite.config.js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import federation from "@originjs/vite-plugin-federation";

export default defineConfig({
  plugins: [
    react(),
    federation({
      name: "remote_app",
      filename: "remoteEntry.js",
      exposes: {
        "./Button": "./src/components/Button",
        "./Header": "./src/components/Header",
      },
      shared: ["react", "react-dom"],
    }),
  ],
  build: {
    modulePreload: false,
    target: "esnext",
    minify: false,
    cssCodeSplit: false,
  },
  preview: {
    port: 5001,
    strictPort: true,
    cors: true,
  },
});
```

#### Explication de la configuration Vite :

1. `plugins` : tableau où vous indiquez à Vite quels **plugins** utiliser lorsqu'il :

* Exécute votre serveur de développement.
* Construit votre bundle de production.

Chaque plugin est essentiellement un petit (ou grand) morceau de code qui se branche sur le pipeline de build de Vite pour ajouter des fonctionnalités supplémentaires – par exemple :

* Ajout du support React JSX/TSX (`@vitejs/plugin-react`).
* Activation de Module Federation (`@originjs/vite-plugin-federation`).

2. `build` : Contrôle la manière dont Vite produit le build de production. Vous n'avez pas besoin de trop vous en soucier pour ce tutoriel.

3. `preview` : Contrôle la manière dont l'application est servie / prévisualisée :

* Utile dans les configurations microfrontend où un port fixe et l'activation de CORS sont nécessaires pour que les autres applications puissent récupérer vos modules distants.
* `strictPort: true` garantit une mise en réseau prévisible – évite les problèmes du type "ça marche sur ma machine" avec des ports aléatoires.

## Le plugin Vite Module Federation

Vous devez configurer votre plugin Vite Module Federation pour l'informer des composants à consommer et à exposer. Examinons les propriétés configurées :

* `name` : L'identifiant unique de votre application distante dans une configuration Module Federation. C'est le nom que les autres applications (hôtes) utiliseront lorsqu'elles déclareront votre application comme distante.
* `filename` : C'est le nom du fichier que votre hôte chargera lorsqu'il tentera de récupérer vos modules exposés.
* `exposes` : Un mappage des noms de modules publics → chemins de fichiers locaux. C'est ainsi que vous décidez quelles parties de votre code sont disponibles pour être consommées à distance.

```typescript
exposes: {
  "./Button": "./src/components/Button",
  "./Header": "./src/components/Header"
}
```

La **clé** (`"./Button"`) est le **nom du module public** – le nom que les autres applications (l'hôte) utiliseront lors de l'importation du module depuis votre application distante.

#### Comment ça fonctionne :

* La **Clé** (`"./Button"`) est l'identifiant exposé que les autres applications peuvent demander.
* La **Valeur** (`"./src/components/Button"`) est le chemin réel du fichier à l'intérieur de votre projet.

Par exemple, si le `name` de votre application distante est `"remote_app"`, l'hôte peut l'importer ainsi :

```typescript
import Button from "remote_app/Button";
```

Sous le capot, `"remote_app"` correspond au `name` de la **distante** dans sa configuration `federation()` et `Button` correspond à la clé `"./Button"` dans `exposes`.

* `shared` : dépendances qui doivent être **partagées** entre l'hôte et la distante. Cela évite d'envoyer des copies dupliquées de bibliothèques volumineuses (comme React), garantissant que l'hôte et la distante utilisent la même instance.
* `remotes` : Un mappage des noms d'applications distantes → l'URL de leur fichier `remoteEntry.js`. Cela indique à l'hôte où récupérer les modules exposés au moment de l'exécution.

```typescript
remotes: { remote_app: "http://localhost:5001/assets/remoteEntry.js" } 
```

La clé `remote_app` doit correspondre au `name` dans la configuration de l'application distante.

La valeur est l'URL complète vers le fichier d'entrée de la distante (servi en dev ou déployé en prod). Rappelez-vous que nous avons configuré `strictPort: true` plus tôt – c'est pour cette raison. Nous devons nous assurer de pointer vers le bon domaine et le bon port.

## Contraintes clés sur les modules exportés

### Contraintes et règles de nommage

**La clé dans** `exposes` (`"./Button"`) :

* Doit commencer par `./` (selon la spécification Module Federation).
* Doit être unique au sein de l'application distante.
* Est sensible à la casse.
* C'est le **chemin du module public** que l'hôte demandera.
* Ne doit pas nécessairement correspondre au nom du fichier, mais la correspondance est une bonne convention pour faciliter la lecture.

**Le fichier vers lequel vous pointez (**`"./src/components/Button"`) :

* Peut exporter par défaut (default), des exports nommés, ou les deux.
* L'hôte peut importer des exports par défaut ou nommés, comme n'importe quel module ES :

    ```typescript
    // Export par défaut
    import MyButton from 'remote_app/Button';
    
    // Export nommé
    import { SpecialButton } from 'remote_app/Button';
    ```

**Le nom d'importation :**

* Totalement libre pour le développeur de l'hôte lors de l'importation d'un export **par défaut**.
* Doit correspondre exactement pour les exports **nommés**.

## Comment créer les composants distants

Bien, vous avez créé votre structure de projet et configuré votre fichier `vite.config.ts` pour permettre l'exposition et la consommation de vos ressources partagées. Ensuite, vous allez créer les composants distants.

### Composant Button

Disons que vous voulez créer un composant bouton qui sera partagé entre toutes vos applications hôtes, car vous voulez maintenir une cohérence. Vous pouvez le faire comme suit :

Naviguez vers le dossier `remote-app` et créez un nouveau fichier nommé `Button.tsx` dans `src/components`. Cela garantira qu'il correspond au plugin de fédération configuré.

```typescript
// remote - ./src/components/Button.tsx
import React from "react";

interface ButtonProps {
  text: string;
  onClick?: () => void;
}

const Button: React.FC<ButtonProps> = ({ text, onClick }) => {
  return (
    <button
      onClick={onClick}
      className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600 hover:cursor-pointer"
    >
      {text}
    </button>
  );
};

export default Button;
```

Vous avez maintenant un composant `Button` réutilisable qui possède un style de base mais permet de configurer l'action du bouton en passant un argument `onClick()`.

### Composant Header

Toujours dans une optique de cohérence, vous voulez créer un composant `<header/>` utilisable sur tous les sites web de votre organisation, garantissant une apparence thématique sur toutes les applications.

Comme précédemment, créez un fichier `Header.tsx` dans `src/components/`, et collez le code suivant :

```typescript
// remote - .src/components/Header.tsx
import React from "react";

const Header: React.FC = () => {
  return (
    <header className="bg-gray-800 text-white p-4">
      <h1 className="text-2xl">Remote App Header</h1>
      <p className="text-white">Hi, Grant</p>
    </header>
  );
};

export default Header;
```

Je suis resté simple, car ce tutoriel est destiné à une preuve de concept plutôt qu'à des composants esthétiques ou réels.

## Comment consommer les composants distants au sein de l'hôte

Vos composants distants sont créés, il faut maintenant les intégrer dans votre application hôte et commencer à les utiliser. C'est assez simple maintenant que vous avez déjà configuré votre `vite.config.ts`.

Vous **pourriez** importer les composants directement dans votre `App.tsx`, mais ce n'est pas une bonne pratique car cela peut surcharger votre `App.tsx` (composant point d'entrée). J'ai choisi de créer un `RemoteWrapperComponent` qui récupère les composants distants et gère la logique métier.

`RemoteComponentWrapper` **:**

Créez un fichier nommé `RemoteComponentWrapper.tsx` dans `src/components`, en collant le code suivant :

```typescript
// host - ./src/components/RemoteComponentWrapper.tsx
import React, { Suspense } from "react";

const RemoteHeader = React.lazy(() => import("remote_app/Header"));
const RemoteButton = React.lazy(() => import("remote_app/Button"));

const LoadingSpinner = () => (
  <div className="flex justify-center p-4">
    <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900"></div>
  </div>
);

export const RemoteComponentWrapper = () => {
  return (
    <div className="p-4">
      <Suspense fallback={<LoadingSpinner />}>
        <RemoteHeader />
      </Suspense>

      <div className="mt-4">
        <Suspense fallback={<LoadingSpinner />}>
          <RemoteButton
            text="Remote Button"
            onClick={() =>
              alert(
                "Well done you've imported the MF remote component successfully"
              )
            }
          />
        </Suspense>
      </div>
    </div>
  );
};
```

Ce composant agit comme une enveloppe (wrapper), gérant une logique métier très simple telle que le chargement de vos composants distants, l'affichage d'un indicateur de chargement en attendant la réponse distante, et la transmission de votre événement `onClick` au bouton distant.

### Pourquoi utiliser `React.lazy()` ?

L'importation avec `React.lazy` n'est pas strictement obligatoire pour les composants Module Federation – c'est plutôt une bonne pratique pour les applications React quand le module distant est :

* Chargé de manière asynchrone au moment de l'exécution, ce qui est presque toujours le cas avec les remotes Module Federation.
* Vous voulez que React gère l'état de chargement et le fractionnement du code (code-splitting) avec élégance – illustré ici par l'utilisation du composant `Suspense`.

`React.lazy` + `<Suspense>` donne à React un moyen intégré de mettre en pause le rendu jusqu'à ce que le composant soit prêt. Sans cela, vous devriez gérer manuellement l'état de chargement.

Cela permet également à vos composants de garder une apparence "normale". Avec React.lazy, `<RemoteHeader/>` est juste un autre composant dans votre JSX.

Sans cela, vous auriez besoin de quelque chose comme :

```typescript
const [Header, setHeader] = useState(null);

useEffect(() => {
  import("remote_app/Header").then(m => setHeader(() => m.default));
}, []);

return Header ? <Header /> : <LoadingSpinner />;
```

…ce qui est plus brouillon et se répète pour chaque composant distant.

## Comment gérer les erreurs TypeScript

À l'intérieur de votre `RemoteWrapperComponent`, vous allez voir l'erreur suivante sur vos importations `Button` et `Header` :

> Cannot find module 'remote_app/Button' or its corresponding type declarations.ts (2307)

Vous obtenez cette erreur parce que les modules distants ne sont pas définis avec des types, donc votre application distante et votre hôte ne savent pas ce qu'est ce composant importé, ni quelle est sa structure (un élément clé du développement TypeScript).

Pour corriger cela, vous devrez fournir à votre application hôte des types personnalisés.

### Ajouter un fichier de déclaration de type

Un fichier de déclaration de type possède un suffixe `.d.ts`.

Au sein de votre application hôte, créez un fichier dans `src/types` nommé `remote-app.d.ts`. Nommer le fichier de cette manière nous permet de savoir que les déclarations à l'intérieur sont liées à l'*remote-app*. C'est particulièrement utile lors de la consommation de plusieurs remotes.

Copiez et collez les déclarations suivantes dans votre fichier `remote-app.d.ts` :

```typescript
// host - ./src/types/remote.d.ts
declare module "remote_app/Button" {
  const Button: React.FC<{
    text: string;
    onClick?: () => void;
  }>;
  export default Button;
}

declare module "remote_app/Header" {
  const Header: React.FC;
  export default Header;
}
```

Maintenant, si vous retournez dans votre `RemoteWrapperComponent`, vos erreurs devraient avoir disparu. Si ce n'est pas le cas, redémarrez votre IDE (dans VS Code, vous pouvez ouvrir votre palette de commandes et sélectionner `Restart Typescript Server`).

## Comment ajouter `RemoteWrapperComponent` à App.tsx

Importez le `RemoteWrapperComponent` dans App.tsx.

J'ai supprimé tout le code standard (boilerplate) et je l'ai remplacé par un style basique pour nous permettre de voir facilement ce qui appartient à l'hôte et ce qui provient des composants distants.

Copiez et collez le code suivant dans le fichier `App.tsx` de votre hôte :

```typescript
// host - ./src/App.tsx
import viteLogo from "/vite.svg";
import "./App.css";
import "./index.css";
import { RemoteComponentWrapper } from "./components/RemoteComponentWrapper";

function App() {
  return (
    <>
      <div className="px-6 border-2">
        <div className="flex justify-center items-center">
          <img src={viteLogo} alt="Example" />
        </div>
        <h1 className="text-2xl">Host Application</h1>
        <p>
          {" "}
          Welcome to the Host application, below are the components pulled from
          the remote application
        </p>
        <RemoteComponentWrapper />
      </div>
    </>
  );
}

export default App;
```

## Comment servir l'application distante et exécuter votre hôte

En raison du fonctionnement de Vite, vous devez construire (build) l'application avant de la prévisualiser ou de la servir.

Assurez-vous que le bloc scripts de votre fichier `package.json` ressemble à ceci :

```json
# remote-app
"scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview --port 5001 --strictPort",
    "serve": "npm run build && npm run preview"
  },

# host-app
"scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview --port 5000 --strictPort",
    "serve": "npm run build && npm run preview"
  },
```

Dans votre terminal, exécutez :

```bash
cd ./remote-app

# exécuter un build, et lancer l'application sur le port 5001
npm run serve
```

Vous devriez voir quelque chose comme ceci :

![capture d'écran montrant la sortie du terminal, port 5001 exécutant l'application distante](https://cdn.hashnode.com/res/hashnode/image/upload/v1755207471886/c64b29ef-3f95-44e5-903b-896f7a3a36fc.png align="center")

Maintenant, vous pouvez exécuter l'application hôte en faisant de même :

```bash
# passer à host-app dans un autre terminal 
cd ../host-app

# construire et exécuter l'application
npm run serve
```

![capture d'écran montrant l'application hôte s'exécutant sur le port 5000](https://cdn.hashnode.com/res/hashnode/image/upload/v1755207573717/77ab133f-ac2e-4f51-8152-3de7200c067c.png align="center")

Si vous ouvrez `localhost:5000`, vous devriez maintenant voir votre application hôte avec les composants distants :

![image : montre l'application hôte finale consommant les composants distants](https://cdn.hashnode.com/res/hashnode/image/upload/v1756078239732/775ab6ec-4566-44cd-ac85-66c37a9001ca.png align="center")

Ensuite, si vous cliquez sur le bouton, vous pouvez voir qu'il affiche le message que vous avez configuré depuis `RemoteWrapperComponent` :

![image : montre une fenêtre d'alerte avec le message fourni après avoir cliqué sur le bouton distant](https://cdn.hashnode.com/res/hashnode/image/upload/v1756078270491/65a72ab8-1cfa-4298-be02-68d0528fd50f.png align="center")

## La véritable puissance des Micro Frontends

La véritable puissance des micro frontends réside dans leur capacité à mettre à jour les composants distants sans avoir besoin de reconstruire l'hôte. Pour le démontrer pleinement, laissez l'hôte s'exécuter et mettez à jour le composant `Button` sur votre `remote-app`.

Mettons à jour les composants distants. Utilisez le code ci-dessous pour mettre à jour les composants `Button` et `Header` :

```typescript
// remote - ./src/components/Header.tsx
import React from "react";

const Header: React.FC = () => {
  return (
    <header className="bg-gray-800 text-white p-4">
      <h1 className="text-2xl">Updated Remote App Header</h1>
      <p className="text-white">Hi, Grant</p>
    </header>
  );
};

export default Header;

// remote - ./src/components/Button.tsx
import React from "react";

interface ButtonProps {
  text: string;
  onClick?: () => void;
}

const Button: React.FC<ButtonProps> = ({ text, onClick }) => {
  return (
    <button
      onClick={onClick}
      className="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600 hover:cursor-pointer"
    >
      {text}
    </button>
  );
};

export default Button;
```

Une fois les composants distants mis à jour, exécutez la commande suivante dans votre dossier `remote-app` :

```bash
npm run serve 
```

Ensuite, rafraîchissez votre application hôte dans le navigateur et vous verrez l'application mise à jour :

![image : montre l'application hôte avec les composants distants mis à jour](https://cdn.hashnode.com/res/hashnode/image/upload/v1756078980661/02ba0655-a18c-460c-939b-6fa95b4149b7.png align="center")

La mise à jour des composants distants est visible immédiatement, sans redémarrer ni reconstruire l'application hôte. Cela met en évidence un avantage clé des micro frontends : les composants partagés sont récupérés depuis leur propre serveur via le fichier `remoteEntry.js`, permettant des mises à jour indépendantes.

## Dernières réflexions

Vous avez réussi à construire et à déployer une architecture micro frontend – félicitations ! Cette implémentation de base démontre la véritable puissance de Module Federation et la capacité de mettre à jour des composants partagés sans avoir besoin de reconstruire et de redéployer l'intégralité de l'application hôte.

Cette indépendance peut accélérer considérablement les cycles de développement et permettre aux équipes de travailler de manière plus autonome.

J'espère que vous avez appris quelque chose de cet article, et comme toujours, pour plus de tutoriels et de discussions, retrouvez-moi sur [twitter/x](https://x.com/grantdotdev).