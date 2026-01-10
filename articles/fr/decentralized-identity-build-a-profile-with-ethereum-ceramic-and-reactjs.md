---
title: Identité Décentralisée – Construire un Profil avec Next.js, Ethereum et le
  Réseau Ceramic
subtitle: ''
author: Idris Olubisi
co_authors: []
series: null
date: '2023-02-17T22:44:56.000Z'
originalURL: https://freecodecamp.org/news/decentralized-identity-build-a-profile-with-ethereum-ceramic-and-reactjs
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Decentralized-Identity--Build-a-Profile-with-NextJs--Ethereum
seo_title: Identité Décentralisée – Construire un Profil avec Next.js, Ethereum et
  le Réseau Ceramic
---

Ceramic-Network.png
étiquettes:
- nom: Blockchain
  slug: blockchain
- nom: décentralisation
  slug: decentralisation
- nom: Ethereum
  slug: ethereum
- nom: Web3
  slug: web3
seo_title: null
seo_desc: "Les intermédiaires centralisés de longue date, comme le gouvernement ou les grandes entreprises, sont ceux qui créent et conservent vos informations d'identification dans les systèmes traditionnels qui gèrent qui vous êtes. \nMais cela implique que vous n'avez aucun contrôle sur les informations\n  \ relatives à votre identification, qui a accès à [l'information personnellement identifiable (PII)](https://www.dol.gov/general/ppii#:~:text=Personal%20Identifiable%20Information%20(PII)%20is,either%20direct%20or%20indirect%20means.), et dans quelle mesure.\n\nEn conséquence, l'Identité Décentralisée fournit des informations liées à l'identité qui sont auto-contrôlées, privées et portables. Les identifiants décentralisés et les attestations servent de principales pièces de construction. \n\nGrâce aux bases de données d'applications décentralisées de Ceramic, les développeurs d'applications peuvent réutiliser des données entre les applications et les rendre automatiquement interopérables.\n\nDans cet article, vous apprendrez ce qu'est l'Identité Décentralisée, les Identifiants Décentralisés, le réseau Ceramic, et comment construire un profil d'identité décentralisée avec Ethereum sur les réseaux Ceramic."
---

Les intermédiaires centralisés de longue date, comme le gouvernement ou les grandes entreprises, sont ceux qui créent et conservent vos informations d'identification dans les systèmes traditionnels qui gèrent qui vous êtes. 

Mais cela implique que vous n'avez aucun contrôle sur les informations relatives à votre identification, qui a accès à [l'information personnellement identifiable (PII)](https://www.dol.gov/general/ppii#:~:text=Personal%20Identifiable%20Information%20(PII)%20is,either%20direct%20or%20indirect%20means.), et dans quelle mesure.

En conséquence, l'Identité Décentralisée fournit des informations liées à l'identité qui sont auto-contrôlées, privées et portables. Les identifiants décentralisés et les attestations servent de principales pièces de construction. 

Grâce aux bases de données d'applications décentralisées de Ceramic, les développeurs d'applications peuvent réutiliser des données entre les applications et les rendre automatiquement interopérables.

Dans cet article, vous apprendrez ce qu'est l'Identité Décentralisée, les Identifiants Décentralisés, le réseau Ceramic, et comment construire un profil d'identité décentralisée avec Ethereum sur les réseaux Ceramic.

### Voici ce que nous allons couvrir:

* Qu'est-ce qu'une Identité Décentralisée ?
* Qu'est-ce que les Identifiants Décentralisés ?
* Qu'est-ce que le Réseau de Données Ceramic ?
* Pourquoi le Réseau Ceramic ?
* Comment Construire un Profil d'Identité Décentralisée avec Next.js
* Prérequis
* Configuration et Installation du Projet
* Installer TailwindCSS dans Next.js
* Authentifier les Utilisateurs
* Créer/Mettre à Jour le Profil Utilisateur
* Comment Tester l'Application
* Conclusion
* Références

## Qu'est-ce qu'une Identité Décentralisée ?

[Identité Décentralisée](https://ethereum.org/en/decentralized-identity/) est un concept d'identification numérique où les personnes, les entreprises et les objets sont responsables de leurs données et peuvent les partager de manière sélective sans dépendre d'une autorité centralisée. 

Cela est rendu possible par l'utilisation de technologies décentralisées, telles que la blockchain. Celles-ci donnent aux personnes le contrôle et la propriété des informations associées à leurs identités plutôt que de les stocker sur un serveur central ou gérées par un tiers.

Une identité décentralisée est une identité auto-détenue et indépendante qui permet l'échange de données de confiance.

Les portefeuilles numériques basés sur la blockchain, tels que ceux utilisés pour stocker et gérer les cryptomonnaies, servent d'illustration pratique de l'identification décentralisée. Les utilisateurs de ces portefeuilles contrôlent les clés privées qui leur donnent accès à leur argent et peuvent distribuer leurs clés publiques à d'autres pour accepter des paiements de leur part.

Les utilisateurs qui gèrent leurs clés privées peuvent effectuer des transactions avec d'autres sans dépendre d'une autorité centrale, telle qu'une banque, et garder la garde de leur argent.

## Qu'est-ce que les Identifiants Décentralisés ?

Les identifiants décentralisés (DID) sont émis, détenus et contrôlés par des individus. Comme ils sont conservés sur des réseaux pair-à-pair ou des registres distribués (blockchains), ils sont globalement uniques, hautement disponibles et cryptographiquement vérifiables. 

Les identifiants décentralisés peuvent être associés à des individus, des groupes ou des entités gouvernementales.

Les DID sont un composant vital de l'écosystème d'identité décentralisée en développement. Ils sont conçus pour offrir un processus uniforme de développement, de maintenance et d'échange d'identités numériques non affiliées à une entreprise ou à une technologie particulière. 

Cela implique qu'un DID peut être maintenu et contrôlé par la personne ou l'entité à laquelle il appartient et utilisé dans divers systèmes et applications.

Ces dernières années, les plateformes de contrats intelligents comme Ethereum ont démontré l'utilité des applications décentralisées (dApps) qui peuvent être assemblées comme des blocs pour créer de nouvelles applications. Cela est particulièrement évident dans les jetons qui se construisent les uns sur les autres, dans les protocoles DeFi qui utilisent les uns les autres, et ainsi de suite.

Grâce à Ceramic, les données sur Internet peuvent désormais avoir le même type de composabilité. Tout type de données, y compris les profils, les connexions sociales, les publications de blog, les identités, les réputations, et ainsi de suite, peut être inclus. Vous en apprendrez plus sur le réseau Ceramic dans la section ci-dessous.

## Qu'est-ce que le Réseau Ceramic ?

[Ceramic](https://ceramic.network/) est un protocole public, sans permission, open-source qui offre du calcul, des transitions d'état et un consensus pour toutes les structures de données sur le web décentralisé. 

Avec l'aide du traitement de flux fourni par Ceramic, les développeurs peuvent construire des applications qui sont robustes, sûres, sans confiance et résistantes à la censure en utilisant des informations dynamiques – sans utiliser de serveurs de base de données peu fiables.

Ceramic stocke tout le contenu dans des documents intelligents, qui sont des journaux IPFS en ajout seulement. Avant d'être ancré dans une blockchain pour consensus, chaque commit est vérifié par une identification décentralisée (DID).

Tous les documents dans Ceramic sont ouvertement découvrables et peuvent être référencés par d'autres documents ou interrogés par tout autre utilisateur du réseau car le système est entièrement pair-à-pair.

## Pourquoi le Réseau Ceramic ?

L'interopérabilité des données est l'un des principaux avantages du Réseau Ceramic. Cette plateforme dispose d'un schéma de données flexible et modulaire qui permet le partage et la combinaison décentralisés et interopérables de divers types de données. 

Les développeurs ont désormais plus de facilité à créer des solutions d'identification décentralisées qui peuvent être intégrées à d'autres programmes et systèmes.

L'infrastructure du Réseau Ceramic est scalable, tolérante aux pannes, décentralisée et hautement disponible. Cela permet aux développeurs de créer des systèmes d'identité décentralisés robustes disponibles pour les utilisateurs partout.

Le Réseau Ceramic fournit également un ensemble d'outils et de bibliothèques pour les développeurs, rendant simple la création d'applications et de services d'identité décentralisés. Ces outils incluent des SDK, des API, des guides pour les développeurs et un écosystème croissant d'outils et de bibliothèques open-source.

Maintenant que vous avez appris les théories derrière l'identité décentralisée, plongeons dans la pratique et mettons les mains dans le cambouis.

## Comment Construire un Profil d'Identité Décentralisée avec Next.js

### Prérequis

Pour suivre ce tutoriel, vous aurez besoin d'une certaine expérience avec JavaScript et React.js. L'expérience avec Next.js n'est pas une exigence, mais c'est un plus.

Assurez-vous d'avoir Node.js ou npm installé sur votre ordinateur. Si ce n'est pas le cas, cliquez [**ici**](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

De plus, il sera très utile d'avoir une compréhension de base de la technologie blockchain et des concepts Web3.

### Configuration et Installation du Projet

Naviguez vers le terminal et utilisez `cd` pour accéder à n'importe quel répertoire de votre choix. Ensuite, exécutez les commandes suivantes :

```bash
mkdir projet-identite-decentralisee
cd projet-identite-decentralisee
npx create-next-app@latest .
```

Acceptez les options suivantes :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1676416198416/0b46fd0f-d47a-4533-9450-a79007205efe.png)

Installez les packages `@self.id/react` et `@self.id/web` en utilisant le snippet de code ci-dessous :

```bash
npm install @self.id/web @self.id/react
```

Ensuite, démarrez l'application en utilisant la commande suivante :

```bash
npm run dev
```

Vous devriez avoir quelque chose de similaire à ce qui est montré ci-dessous : la disposition de base par défaut pour Next.js 13.

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1676416289117/799cfc73-78b3-49f9-8b72-a407813f7d9c.png)

### Installer TailwindCSS dans Next.js

Dans cette section, vous allez configurer Tailwind CSS dans un projet Next.js. Installez `tailwindcss` et ses dépendances via npm, puis exécutez la commande init pour générer à la fois `tailwind.config.js` et `postcss.config.js`.

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Naviguez vers le fichier `tailwind.config.js`, et ajoutez les chemins vers vos fichiers de modèle avec le snippet de code suivant.

```javascript
/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
 
    // Ou si vous utilisez le répertoire `src` :
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Supprimez tous les styles CSS à l'intérieur de `globals.css`. Ajoutez les directives `@tailwind` pour chacune des couches de Tailwind à votre fichier `globals.css`.

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Configurer le Composant Provider

Le composant `Provider` doit être placé en haut de l'arborescence de l'application pour utiliser les hooks détaillés ci-dessous. Vous pouvez l'utiliser pour fournir un état initial ainsi qu'une configuration spécifique pour les clients et requêtes [Self.ID](http://Self.ID).

Mettez à jour le fichier `_app.js` sous le dossier pages avec le snippet de code suivant :

```javascript
// Importez le composant Provider de la bibliothèque "@self.id/react".
import { Provider } from "@self.id/react";

// Importez le fichier "globals.css" du répertoire "@/styles".
import "@/styles/globals.css";

// Définissez le composant App comme export par défaut.
export default function App({ Component, pageProps }) {
    
  // Rendre le composant Provider, qui fournit des fonctionnalités d'authentification et d'autorisation à l'application.
  // Passez une prop client au composant Provider, qui configure le testnet Ceramic avec la valeur "testnet-clay".
  // Rendre le Component avec ses props à l'intérieur du composant Provider, ce qui permet à l'application d'accéder au contexte d'authentification et d'autorisation.
    
  return (
    <Provider client={{ ceramic: "testnet-clay" }}>
      <Component {...pageProps} />
    </Provider>
  );
}

```

Dans le snippet de code ci-dessus, nous avons :

* Importé un composant fournisseur de contexte et des styles CSS globaux, puis défini un composant `App` qui enveloppe toute l'application avec le fournisseur de contexte.
* Configuré le fournisseur de contexte avec un client Ceramic testnet, ce qui permet à l'application d'accéder aux fonctionnalités d'authentification et d'autorisation.
* Enfin, le `Component` est rendu avec ses props à l'intérieur du fournisseur de contexte, permettant à l'application d'accéder au contexte d'authentification et d'autorisation.

### Construire la Mise en Page

Ensuite, naviguez vers le fichier `index.js` sous le dossier `pages` et mettez-le à jour avec le code suivant :

```javascript
// Importez le composant Head du module "next/head".
import Head from "next/head";

// Importez les hooks useViewerConnection et useViewerRecord de la bibliothèque "@self.id/react".
import { useViewerConnection, useViewerRecord } from "@self.id/react";

// Importez le composant EthereumAuthProvider de la bibliothèque "@self.id/web".
import { EthereumAuthProvider } from "@self.id/web";

// Importez le hook useState du module "react".
import { useEffect, useState } from "react";


export default function Home() {

  return (
    <>
      <Head>
        <title>
          Identité Décentralisée : Construire un Profil avec NextJs, Ethereum et le Réseau Ceramic
        </title>
        <meta name="description" content="Généré par create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="min-h-screen bg-gray-200">
        <div className="bg-gray-600 py-4 px-4 sm:px-6 lg:px-8 lg:py-6 shadow-lg text-white">
          <div className="container mx-auto px-6 md:px-0">
            <h1 className="text-2xl font-bold text-white text-center">
              Identité Décentralisée : Construire un Profil avec NextJs, Ethereum et le Réseau Ceramic
            </h1>
          </div>
        </div>

        <div className="flex items-center justify-center pt-20 font-sans overflow-hidden">
          <div className="max-w-md w-full mx-auto">
            <div className="bg-white p-10 rounded-lg shadow-lg">
              <form>
                <div className="mb-6">
                  <label
                    className="block text-gray-700 font-bold mb-2"
                    htmlFor="name"
                  >
                    Nom
                  </label>
                  <input
                    className="border border-gray-300 p-2 w-full rounded-lg"
                    type="text"
                    name="name"
                    id="name"
                    placeholder="Votre nom"
                  />
                </div>
                <div className="mb-6">
                  <label
                    className="block text-gray-700 font-bold mb-2"
                    htmlFor="bio"
                  >
                    Bio
                  </label>
                  <textarea
                    className="border border-gray-300 p-2 w-full rounded-lg"
                    name="bio"
                    id="bio"
                    rows="5"
                    placeholder="Écrivez quelque chose sur vous"
                  ></textarea>
                </div>
                <div className="mb-6">
                  <label
                    className="block text-gray-700 font-bold mb-2"
                    htmlFor="username"
                  >
                    Nom d'utilisateur
                  </label>
                  <input
                    className="border border-gray-300 p-2 w-full rounded-lg"
                    type="text"
                    name="username"
                    id="username"
                    placeholder="Votre nom d'utilisateur"
                  />
                </div>
                <div className="flex items-center justify-between">
                  <button
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                    type="submit"
                  >
                    Mettre à Jour le Profil
                  </button>
                  <button
                    className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
                    type="button"
                  >
                    Connecter le Portefeuille
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </main>
    </>
  );
}
```

Pour démarrer l'application, exécutez la commande suivante et naviguez vers localhost:3000 sur votre navigateur ; vous devriez avoir quelque chose de similaire à ce qui est montré ci-dessous :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1676418666618/bc0620d9-d7bb-4297-bdb1-6021d08d8d6c.png)

### Comment Authentifier les Utilisateurs

Dans cette section, vous allez implémenter l'authentification des utilisateurs pour permettre aux utilisateurs de connecter leurs portefeuilles et d'interagir avec l'application.

Mettez à jour le fichier `index.js` avec le code suivant :

```javascript
//..

export default function Home() {

  // Variables d'état pour la connexion, la fonction de connexion et la fonction de déconnexion
  const [connection, connect, disconnect] = useViewerConnection();
    
  
  const [isWindow, setIsWindow] = useState(null);
    

  // Variable d'état pour les données de profil de base du spectateur
  const record = useViewerRecord("basicProfile");

  // Fonction pour créer EthereumAuthProvider en utilisant le fournisseur window.ethereum
  async function createAuthProvider() {
    const addresses = await window.ethereum.request({
      method: "eth_requestAccounts",
    });
    return new EthereumAuthProvider(window.ethereum, addresses[0]);
  }

  // Fonction pour connecter au compte du spectateur en utilisant le authProvider créé
  async function connectAccount() {
    const authProvider = await createAuthProvider();
    await connect(authProvider);
  }

  // Code JSX rendu
  return (
    <>
      {/* ... */}
      <div className="flex items-center justify-between">
        {/* ... */}

        {/* Rendre conditionnellement un bouton pour connecter/déconnecter l'utilisateur */}
        {connection.status === "connected" ? (
          <button
            className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
            type="button"
            onClick={() => disconnect()}
          >
            Déconnecter
          </button>
        ) : isWindow && "ethereum" in window ? (
          <button
            className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
            type="button"
            disabled={connection.status === "connecting" || !record}
            onClick={() => {
              connectAccount();
            }}
          >
            Connecter le Portefeuille
          </button>
        ) : (
          <p className="text-red-500 text-sm italic mt-2 text-center w-full">
            Un fournisseur Ethereum injecté tel que{" "}
            <a href="https://metamask.io/">MetaMask</a> est nécessaire pour
            s'authentifier.
          </p>
        )}
      </div>
    </>
  )
}
```

Dans le snippet de code ci-dessus,

* Le hook `useViewerConnection` est utilisé pour configurer une variable d'état pour le statut de connexion de l'utilisateur, connecter et déconnecter.
* `isWindow` pour définir l'état initial de la fenêtre afin d'éviter [l'erreur d'hydratation React](https://nextjs.org/docs/messages/react-hydration-error)
* Le hook `useViewerRecord` est utilisé pour récupérer les données de profil de base de l'utilisateur.
* La fonction `createAuthProvider` crée un objet `EthereumAuthProvider` en utilisant le fournisseur `window.ethereum`.
* La fonction `connectAccount` appelle `createAuthProvider` et se connecte au compte de l'utilisateur en utilisant `connect(authProvider)`.
* Le code JSX rend conditionnellement un bouton en fonction du statut de connexion de l'utilisateur et de la disponibilité d'un fournisseur `ethereum` dans l'objet `window`.
* Si l'utilisateur est déjà connecté, le bouton lui permettra de se déconnecter. Si l'utilisateur n'est pas encore connecté et qu'un fournisseur `ethereum` est disponible, le bouton lui permettra de se connecter. Mais si l'utilisateur n'est pas connecté et qu'aucun fournisseur `ethereum` n'est disponible, un message sera affiché pour informer l'utilisateur qu'un fournisseur Ethereum injecté comme MetaMask est requis pour s'authentifier.

En testant la fonctionnalité d'authentification, vous devriez avoir quelque chose de similaire à ce qui est montré ci-dessous :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1676467487656/bc91509c-cd69-479a-80e5-7bc9b680150d.png)

### Comment Créer ou Mettre à Jour un Profil Utilisateur

Dans la section précédente, vous avez appris comment authentifier avec succès les utilisateurs. Ensuite, vous allez implémenter la fonctionnalité pour créer et mettre à jour un utilisateur authentifié avec le snippet de code suivant :

`pages/index.js`

```javascript
//...


export default function Home() {
// Utilisez le hook useState pour créer des variables d'état et des fonctions pour les mettre à jour
  const [name, setName] = useState("");
  const [bio, setBio] = useState("");
  const [username, setUsername] = useState("");

  //...

// Définissez une fonction asynchrone appelée updateProfile pour mettre à jour les informations de profil
  async function updateProfile() {
    // Si l'un des champs requis est vide, retournez tôt et ne mettez pas à jour
     if (!name || !bio || !username) {
       return;
     }
    
     // Utilisez la méthode merge pour mettre à jour l'enregistrement avec les nouvelles informations
     await record.merge({
       name,
       bio,
       username,
     });
   }

  // Rendre l'interface utilisateur du composant
  return (
    <>

    {/* ... */}

    <div className="flex items-center justify-center pt-20 font-sans overflow-hidden">
          <div className="max-w-md w-full mx-auto">
            <div className="bg-white p-10 rounded-lg shadow-lg">
              <form>
               {/* ... */}
              </form>
            </div>
			{connection.status === "connected" && record && record.content ? (
              <div className="flex flex-col items-center mt-8">
                <h2 className="text-3xl font-bold mb-6 text-gray-900">
                  Informations sur le Profil
                </h2>
                <div className="w-full max-w-md bg-white p-8 rounded-lg shadow-lg">
                  <p className="mb-4">
                    <span className="font-bold text-gray-700 mr-2 text-lg">
                      Nom :
                    </span>{" 