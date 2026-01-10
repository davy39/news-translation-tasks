---
title: Comment créer un générateur de descriptions de poste avec NextJS et ChatGPT
subtitle: ''
author: Ashutosh K Singh
co_authors: []
series: null
date: '2023-01-18T23:50:19.000Z'
originalURL: https://freecodecamp.org/news/build-a-job-description-generator-with-nextjs-and-chatgpt
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/m1ieud6fgxhqsgnec96n-1.gif
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Next.js
  slug: nextjs
- name: projects
  slug: projects
- name: tailwind
  slug: tailwind
seo_title: Comment créer un générateur de descriptions de poste avec NextJS et ChatGPT
seo_desc: 'In this tutorial, we will discuss how to build a Job Description Generator
  with Next.js, and ChatGPT, a powerful language generation model developed by OpenAI.

  We will also use TailwindCSS, a utility-first CSS framework, to style our Next.js
  app.

  Che...'
---

Dans ce tutoriel, nous allons discuter de la manière de créer un générateur de descriptions de poste avec [Next.js](https://nextjs.org/), et [ChatGPT](https://openai.com/blog/chatgpt/), un puissant modèle de génération de langage développé par OpenAI.

Nous allons également utiliser [TailwindCSS](https://tailwindcss.com/), un framework CSS basé sur les utilitaires, pour styliser notre application Next.js.

Consultez le dépôt GitHub [ici](https://github.com/lelouchB/ai-job-description) si vous souhaitez plonger directement dans le code.

Et voici un lien vers la version déployée : [https://ai-job-description.vercel.app/](https://ai-job-description.vercel.app/).

Maintenant, commençons.

## Prérequis

Avant de commencer, vous devez avoir :

1. Des connaissances en [HTML, CSS et JavaScript](https://www.freecodecamp.org/learn/responsive-web-design/).
2. Une compréhension de base de [React](https://www.freecodecamp.org/learn/front-end-libraries/react/) et [Next.js](https://nextjs.org/).
3. [Node](https://nodejs.org/en/) et NPM installés sur votre machine de développement locale.
4. Un éditeur de code de votre choix. (exemple [VSCode](https://code.visualstudio.com/))

Si vous pensez que vos progrès pourraient être améliorés parce que vous devez en apprendre davantage sur ces sujets, consultez [https://www.freecodecamp.org/learn](https://www.freecodecamp.org/learn). Les modules géniaux là-bas vous mettront en route en un rien de temps.

## **Comment installer et configurer Next.js**

Nous allons utiliser [Create Next App](https://nextjs.org/docs/api-reference/create-next-app) pour initialiser rapidement un projet Next.js. Dans le répertoire racine de votre projet, exécutez les commandes suivantes dans le terminal :

```bash
npx create-next-app@latest ai-job-description --src-dir
cd ai-job-description
npm run dev

```

Sélectionnez `Non` lorsque vous êtes invité à ajouter des configurations supplémentaires.

```bash
✓ Would you like to use TypeScript with this project? … No / Yes
✓ Would you like to use ESLint with this project? … No / Yes
? Would you like to use experimental `app/` directory with this project? ‣ No / ✓ Would you like to use experimental `app/` directory with this project? … No
```

Vous pouvez exécuter la commande suivante si vous souhaitez créer un projet TypeScript :

```bash
npx create-next-app@latest ai-job-description --typescript --src-dir
cd ai-job-description
npm run dev

```

La dernière commande, `npm run dev`, démarrera le serveur de développement sur le port 3000 de votre système.

Accédez à [http://localhost:3000](http://localhost:3000) dans le navigateur. Voici à quoi ressemblera votre application :

![Next.js 13](https://www.freecodecamp.org/news/content/images/2023/01/Untitled.png)
_Next.js 13_

Vous pouvez maintenant fermer le serveur de développement. L'étape suivante consiste à nettoyer le code d'exemple généré par Create Next App et à configurer le projet pour utiliser TailwindCSS.

Exécutez les commandes suivantes pour installer TailwindCSS dans le projet.

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

```

La dernière commande créera un fichier `tailwind.config.js` dans le répertoire racine de votre projet.

Mettez à jour le fichier `tailwind.config.js` comme suit pour inclure les chemins vers nos fichiers :

```js

module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};

```

1. Supprimez le fichier `src/styles/Home.module.css`.
2. Mettez à jour le fichier `src/styles/globals.css` comme suit.

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

```

3.   Modifiez `src/pages/index.js` comme suit :

```js
// src/pages/index.js
import Head from "next/head";
import { Inter } from "@next/font/google";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
    <>
      <Head>
        <title>Générateur de descriptions de poste avec IA</title>
        <meta name="description" content="Générateur de descriptions de poste avec IA" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={"bg-white min-h-screen "}>
        <div className="flex flex-col items-center justify-center px-4 py-2">
          <h1 className="text-4xl md:text-6xl font-bold">
            Générateur de descriptions de poste avec IA
            <span className="text-4xl md:text-6xl font-bold text-blue-600">
              .
            </span>
          </h1>
          <p className="mt-3 text-2xl">
            Créez de belles
            <span className="text-2xl font-bold text-blue-600">
              {" "}
              descriptions de poste{" "}
            </span>
            en quelques secondes
          </p>
        </div>
      </main>
    </>
  );
}

```

Nous avons ajouté un titre et un sous-titre simples à notre application dans le code ci-dessus. Redémarrez le serveur de développement en exécutant la commande `npm run dev` et accédez à nouveau à [http://localhost:3000/](http://localhost:3000/) dans le navigateur. Votre application ressemblera à ceci :

![Générateur de descriptions de poste avec IA](https://www.freecodecamp.org/news/content/images/2023/01/Untitled-1-.png)
_Générateur de descriptions de poste avec IA_



## Comment générer une clé API OpenAI

Dans cette section, nous allons discuter de la manière dont vous pouvez générer une clé API OpenAI. Accédez à [https://beta.openai.com/signup](https://beta.openai.com/signup) dans le navigateur et créez un compte sur OpenAI si vous ne l'avez pas encore fait.

![https://beta.openai.com/signup](https://www.freecodecamp.org/news/content/images/2023/01/Untitled-2-.png)
_https://beta.openai.com/signup_

Après avoir créé un compte, accédez à [https://beta.openai.com/account/api-keys](https://beta.openai.com/account/api-keys) et cliquez sur `+ Create new secret key`.

![Créer une nouvelle clé secrète](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-18-at-12-06-06-OpenAI-API.png)

Cela générera une nouvelle clé API – copiez cette clé. Exécutez la commande suivante pour créer un fichier `.env` :

```bash
touch .env

```

Dans ce fichier `.env`, créez une nouvelle variable d'environnement nommée `OPENAI_API_KEY` et collez la clé API là.

```
OPENAI_API_KEY = <REMPLACER_PAR_VOTRE_CLE>

```

Next.js a un support intégré pour charger les variables d'environnement depuis `.env` dans `process.env`. Vous pouvez en lire plus à ce sujet [ici](https://nextjs.org/docs/basic-features/environment-variables).

## Comment construire l'interface utilisateur de l'application

Pour générer les descriptions de poste, nous avons besoin de quelques détails de base sur le poste lui-même. Dans cette section, nous allons créer le formulaire pour prendre les entrées de l'utilisateur. 

Nous allons demander à l'utilisateur le titre du poste, le secteur d'activité, le ton et les mots-clés à inclure dans la description de poste. Vous pouvez modifier les champs pour créer un générateur de descriptions de poste personnalisé. 

Par exemple, si vous souhaitez construire cela pour le secteur **Tech**, vous pouvez coder en dur cette information et supprimer les champs correspondants.

Nous allons afficher le résultat de la requête API ChatGPT dans une zone de texte et donner à l'utilisateur la possibilité de copier la sortie dans son presse-papiers.

Exécutez les commandes suivantes dans le répertoire racine pour créer un fichier nommé `Dashboard.js` dans le dossier `components`.

```js
cd src
mkdir components
cd components
touch Dashboard.js

```

Ajoutez le code suivant au fichier `Dashboard.js` :

```js
import React, { useState } from "react";

export default function Dashboard() {
  const [jobDescription, setJobDescription] = useState("");

  const [jobTitle, setJobTitle] = useState("");
  const [industry, setIndustry] = useState("");
  const [keyWords, setKeyWords] = useState("");
  const [tone, setTone] = useState("");
  const [numWords, setNumWords] = useState("");

  const [isGenerating, setIsGenerating] = useState(false);
  const [isCopied, setIsCopied] = useState(false);

  return (
    <div className="max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="grid gap-y-12 md:grid-cols-2 md:gap-x-12 ">
        <div className="">
          <form>
            <div className="flex flex-col">
              <label className="sr-only" htmlFor="jobTitle">
                Titre du poste
              </label>
              <input
                type="text"
                className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
                name="jobTitle"
                placeholder="Titre du poste"
                id="jobTitle"
                value={jobTitle}
                onChange={(e) => setJobTitle(e.target.value)}
                required
              />
            </div>
            <div className="flex flex-col">
              <label htmlFor="industry" className="sr-only">
                Secteur d'activité
              </label>
              <input
                value={industry}
                onChange={(e) => setIndustry(e.target.value)}
                className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
                placeholder="Secteur d'activité (Optionnel)"
                type="text"
                name="industry"
                id="industry"
              />
            </div>
            <div className="flex flex-col">
              <label htmlFor="keywords" className="sr-only">
                Mots-clés pour l'IA (Optionnel)
              </label>
              <textarea
                rows={7}
                value={keyWords}
                onChange={(e) => setKeyWords(e.target.value)}
                name="keyWords"
                id="keyWords"
                placeholder="Mots-clés pour l'IA (Optionnel)"
                className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
              />
            </div>
            <div className="flex flex-col">
              <label className="sr-only" htmlFor="tone">
                Ton
              </label>

              <select
                value={tone}
                onChange={(e) => setTone(e.target.value)}
                className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
                name="tone"
                id="tone"
              >
                <option value="default">Sélectionner le ton (Optionnel)</option>
                <option value="casual">Décontracté</option>
                <option value="friendly">Amical</option>
                <option value="professional">Professionnel</option>
                <option value="formal">Formel</option>
              </select>
            </div>
            <div className="flex flex-col">
              <label htmlFor="words" className="sr-only">
                Mots (Optionnel)
              </label>
              <input
                value={numWords}
                onChange={(e) => setNumWords(e.target.value)}
                type="number"
                className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
                placeholder="Nombre de mots - Par défaut 200 (Optionnel)"
                name="words"
                id="words"
              />
            </div>

            <button
              className={`bg-blue-600 w-full hover:bg-blue-700 text-white font-bold mt-6 py-2 px-4 rounded
                ${
                  isGenerating || jobTitle === ""
                    ? "cursor-not-allowed opacity-50"
                    : ""
                }`}
              type="submit"
              disabled={isGenerating || jobTitle === ""}
            >
              {isGenerating ? "Génération en cours..." : "Générer la description de poste"}
            </button>
          </form>
        </div>
        <div className="">
          <div className="flex flex-col">
            <label htmlFor="output" className="sr-only">
              Sortie
            </label>
            <textarea
              rows={
                jobDescription === ""
                  ? 7
                  : jobDescription.split("\\n").length + 12
              }
              name="output"
              onChange={(e) => setJobDescription(e.target.value)}
              value={jobDescription}
              disabled={jobDescription === ""}
              id="output"
              placeholder="Description de poste générée par l'IA"
              className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
            />
            <button
              onClick={() => {}}
              className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
              type="submit"
              disabled={jobDescription === ""}
            >
              {isCopied ? "Copié" : "Copier dans le presse-papiers"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

```

Voici ce que nous faisons :

Tout d'abord, nous commençons par importer le hook `useState` de `react`. Les hooks sont des fonctions qui vous permettent d'utiliser des fonctionnalités React, telles que la définition de l'état, sans avoir à écrire une classe. 

Le `useState` vous permet de suivre l'état, c'est-à-dire les données ou propriétés, dans un composant fonctionnel. Ici, nous utilisons le hook `useState` pour suivre la valeur de tous les champs de saisie.

Nous avons défini les états suivants :

```js
  const [jobDescription, setJobDescription] = useState("");

  const [jobTitle, setJobTitle] = useState("");
  const [industry, setIndustry] = useState("");
  const [keyWords, setKeyWords] = useState("");
  const [tone, setTone] = useState("");
  const [numWords, setNumWords] = useState("");

  const [isGenerating, setIsGenerating] = useState(false);
  const [isCopied, setIsCopied] = useState(false);


```

L'état `jobDescription` est pour la description de poste envoyée par l'API ChatGPT. Les états `jobTitle`, `industry`, `keyWords`, `tone` et `numWords` sont les états pour tous les champs du formulaire. L'état `isGenerating` est utilisé pour suivre si la requête est en cours de traitement après que l'utilisateur a cliqué sur le bouton `Générer`. L'état `isCopied` suit si l'utilisateur a copié avec succès la description de poste générée.

Nous utilisons [TailwindCSS](https://tailwindcss.com/docs/grid-template-columns) pour créer une grille de deux colonnes. La première colonne contiendra le formulaire de saisie, et l'autre colonne affichera la description de poste générée.

```js
<div className="grid gap-y-12 md:grid-cols-2 md:gap-x-12">
...
</div>

```

Nous créons un élément `form` dans la première colonne et définissons ses champs de saisie.

```js
<form>
  <div className="flex flex-col">
    <label className="sr-only" htmlFor="jobTitle">
      Titre du poste
    </label>
    <input
      type="text"
      className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
      name="jobTitle"
      placeholder="Titre du poste"
      id="jobTitle"
      value={jobTitle}
      onChange={(e) => setJobTitle(e.target.value)}
      required
    />
  </div>
...
</form>

```

Le champ `jobTitle` est le seul champ obligatoire du formulaire et est nécessaire pour générer la description de poste. Nous définissons la valeur de ce champ de saisie sur l'état `jobTitle` et passons la fonction `setJobTitle()` à l'événement `onChange()` qui mettra à jour `jobTitle` chaque fois que l'utilisateur tape dans le champ de saisie. Maintenant, l'état `jobTitle` et le champ de saisie sont interconnectés.

![Champ Titre du poste](https://www.freecodecamp.org/news/content/images/2023/01/Untitled-1.png)

Nous utilisons le même format pour créer d'autres champs de saisie pour le secteur d'activité et le nombre de mots.

Pour les mots-clés, nous utilisons une `textarea` pour que l'utilisateur puisse entrer des informations ou des mots-clés pertinents pour la description de poste.

```js
<div className="flex flex-col">
  <label htmlFor="keywords" className="sr-only">
    Mots-clés pour l'IA (Optionnel)
  </label>
  <textarea
    rows={7}
    value={keyWords}
    onChange={(e) => setKeyWords(e.target.value)}
    name="keyWords"
    id="keyWords"
    placeholder="Mots-clés pour l'IA (Optionnel)"
    className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
  />
</div>

```

Voici à quoi ressemble ce champ `textarea` :

![Champ Mots-clés](https://www.freecodecamp.org/news/content/images/2023/01/Untitled-1--1.png)

Nous créons également un champ `select` pour le ton de la description de poste. Vous pouvez personnaliser les options selon vos besoins. 

Cette application propose quatre tons – **Décontracté**, **Amical**, **Professionnel** et **Formel**. Comme le champ de saisie ci-dessus pour `jobTitle`, nous utilisons les propriétés `value` et `onChange` pour interconnecter le champ `select` avec l'état `tone`.

```js
<div className="flex flex-col">
  <label className="sr-only" htmlFor="tone">
    Ton
  </label>

  <select
    value={tone}
    onChange={(e) => setTone(e.target.value)}
    className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
    name="tone"
    id="tone"
  >
    <option value="default">Sélectionner le ton (Optionnel)</option>
    <option value="casual">Décontracté</option>
    <option value="friendly">Amical</option>
    <option value="professional">Professionnel</option>
    <option value="formal">Formel</option>
  </select>
</div>

```

![Ton](https://www.freecodecamp.org/news/content/images/2023/01/Untitled-2--1.png)

Le dernier champ du formulaire est un `button` pour déclencher la génération de la description de poste.

```js
<button
  className={`bg-blue-600 w-full hover:bg-blue-700 text-white font-bold mt-6 py-2 px-4 rounded
                ${
                  isGenerating || jobTitle === ""
                    ? "cursor-not-allowed opacity-50"
                    : ""
                }`}
  type="submit"
  disabled={isGenerating || jobTitle === ""}
>
  {isGenerating ? "Génération en cours..." : "Générer la description de poste"}
</button>

```

Nous ne voulons pas que les utilisateurs cliquent sur le bouton `Générer` sans aucun titre de poste et créent des requêtes vides. Donc, dans le bouton ci-dessus, nous utilisons les états `isGenerating` et `jobTitle` pour désactiver le bouton lorsque `jobTitle` est vide. Nous changeons également le texte du bouton en `Génération en cours` lorsque la requête API est en cours de traitement.

![Bouton Générer la description de poste](https://www.freecodecamp.org/news/content/images/2023/01/Untitled-3-.png)

Nous ajoutons un champ `textarea` pour afficher la description de poste générée dans la deuxième colonne. Ce `textarea` est désactivé tant que l'état `jobDescription` est vide.

```js
<div className="flex flex-col">
  <label htmlFor="output" className="sr-only">
    Sortie
  </label>
  <textarea
    rows={jobDescription === "" ? 7 : jobDescription.split("\\n").length + 12}
    name="output"
    onChange={(e) => setJobDescription(e.target.value)}
    value={jobDescription}
    disabled={jobDescription === ""}
    id="output"
    placeholder="Description de poste générée par l'IA"
    className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
  />
  ...
</div>

```

Nous ajoutons également un bouton de copie à la deuxième colonne afin que les utilisateurs puissent facilement copier la description de poste générée. Ce bouton est également désactivé tant que l'état `jobDescription` est vide.

```js
<button
  onClick={() => {}}
  className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
  type="submit"
  disabled={jobDescription === ""}
>
  {isCopied ? "Copié" : "Copier dans le presse-papiers"}
</button>

```

Voici à quoi ressemble la deuxième colonne :

![Colonne de sortie](https://www.freecodecamp.org/news/content/images/2023/01/Untitled-4-.png)

Ensuite, nous mettons à jour le fichier `index.js` comme suit pour importer et ajouter le composant `Dashboard` :

```js
import Head from "next/head";
import { Inter } from "@next/font/google";
import Dashboard from "@/components/Dashboard";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
    <>
      <Head>
        <title>Générateur de descriptions de poste avec IA</title>
        <meta name="description" content="Générateur de descriptions de poste avec IA" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={"bg-white min-h-screen "}>
        <div className="flex flex-col items-center justify-center px-4 py-2">
          <h1 className="text-4xl md:text-6xl font-bold">
            Générateur de descriptions de poste avec IA
            <span className="text-4xl md:text-6xl font-bold text-blue-600">
              .
            </span>
          </h1>
          <p className="mt-3 text-2xl">
            Créez de belles
            <span className="text-2xl font-bold text-blue-600">
              {" "}
              descriptions de poste{" "}
            </span>
            en quelques secondes
          </p>
        </div>
        <Dashboard />
      </main>
    </>
  );
}

```

Votre application ressemblera à ceci :

![Générateur de descriptions de poste avec IA](https://www.freecodecamp.org/news/content/images/2023/01/Untitled-5-.png)

Vous pouvez ajouter des valeurs aux champs vides, mais ce n'est pas encore fonctionnel. Nous ajouterons la logique pour récupérer et afficher la description de poste dans la section suivante.

## Comment récupérer des données de ChatGPT

Dans cette section, nous allons discuter de la manière dont vous pouvez créer une route API Next.js qui envoie une requête à ChatGPT pour générer la description de poste à partir des données d'entrée de l'utilisateur.

Next.js fournit une solution facile pour construire votre API sans avoir besoin d'un autre projet, par exemple, un projet Node-Express.

D'après la [documentation NextJS](https://nextjs.org/docs/api-routes/introduction) :

> _Les fichiers dans le dossier pages/api sont mappés à la route /api/ et traités comme des points de terminaison API plutôt que comme des pages. Ces fichiers sont uniquement côté serveur et n'ajoutent pas à la taille du bundle côté client._

Tout d'abord, exécutez la commande suivante à la racine du projet pour créer une route API.

```bash
cd src/pages/api
touch returnJobDescription.js

```

Ensuite, ajoutez le code suivant au fichier `returnJobDescription.js` :

```js
const generateDescription = async ({
  jobTitle,
  industry,
  keyWords,
  tone,
  numWords,
}) => {
  try {
    const response = await fetch(
      "https://api.openai.com/v1/engines/text-davinci-003/completions",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
        },
        body: JSON.stringify({
          prompt: `Écrivez une description de poste pour un rôle de ${jobTitle} 
          ${industry ? `dans le secteur ${industry}` : ""} qui fait environ ${
            numWords || 200
          } mots dans un ton ${tone || "neutre"}. ${
            keyWords ? `Incorporez les mots-clés suivants : ${keyWords}.` : ""
          }. Le poste doit être décrit de manière SEO friendly, en mettant en avant ses caractéristiques et avantages uniques.`,
          max_tokens: 100,
          temperature: 0.5,
        }),
      }
    );
    const data = await response.json();

    return data.choices[0].text;
  } catch (err) {
    console.error(err);
  }
};

export default async function handler(req, res) {
  const { jobTitle, industry, keyWords, tone, numWords } = req.body;

  const jobDescription = await generateDescription({
    jobTitle,
    industry,
    keyWords,
    tone,
    numWords,
  });

  res.status(200).json({
    jobDescription,
  });
}

```

Voici ce que nous faisons :

Tout d'abord, nous créons une fonction asynchrone nommée `generateJobDescription` qui prend `jobTitle`, `industry`, `tone`, `numWords` et `keywords` comme arguments.

```js
const generateDescription = async ({
  jobTitle,
  industry,
  keyWords,
  tone,
  numWords,
}) => {
...
}

```

Ensuite, nous utilisons l'API `fetch` à l'intérieur d'un bloc try/catch pour créer une requête `POST` vers le point de terminaison OpenAI ChatGPT. Vous pouvez en lire plus sur l'API `fetch` [ici](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch). Vous pouvez également utiliser le [package OpenAI NodeJS](https://www.npmjs.com/package/openai) au lieu de l'API `fetch`.

Les requêtes sont envoyées au point de terminaison suivant : `https://api.openai.com/v1/engines/text-davinci-003/completions`

Ici, `text-davinci-003` est le modèle pour ChatGPT, et `completions` est la tâche que nous voulons effectuer. Vous pouvez lire sur les autres modèles OpenAI [ici](https://beta.openai.com/docs/models/gpt-3).

```js
  try {
    const response = await fetch(
      "https://api.openai.com/v1/engines/text-davinci-003/completions",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
        },
        body: JSON.stringify({
          prompt: `Écrivez une description de poste pour un rôle de ${jobTitle} 
          ${industry ? `dans le secteur ${industry}` : ""} qui fait environ ${
            numWords || 200
          } mots dans un ton ${tone || "neutre"}. ${
            keyWords ? `Incorporez les mots-clés suivants : ${keyWords}.` : ""
          }. Le poste doit être décrit de manière SEO friendly, en mettant en avant ses caractéristiques et avantages uniques.`,
          max_tokens: 100,
          temperature: 0.5,
        }),
      }
    );

...
}
catch (err) {
    console.error(err);
  }


```

L'API OpenAI utilise la clé API que nous avons générée précédemment pour authentifier les requêtes. Nous l'ajoutons à l'en-tête HTTP `Authorization` comme suit :

```js
headers: {
 Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
},

```

Dans le `body` de la requête `POST`, nous ajoutons les valeurs d'entrée de l'utilisateur à une invite préconfigurée pour la description de poste. Cette invite peut être une chaîne, un tableau de chaînes, un tableau de jetons ou un tableau de tableaux de jetons. Vous pouvez personnaliser cette invite en conséquence. 

Nous avons ajouté une valeur par défaut pour `numWords` et `tone` dans l'invite, c'est-à-dire `200` et `neutre`, respectivement. Vous pouvez en lire plus à ce sujet [ici](https://beta.openai.com/docs/api-reference/completions/create).

```js
body: JSON.stringify({
	prompt: `Écrivez une description de poste pour un rôle de ${jobTitle} 
          ${industry ? `dans le secteur ${industry}` : ""} qui fait environ ${
		numWords || 200
	} mots dans un ton ${tone || "neutre"}. ${
		keyWords ? `Incorporez les mots-clés suivants : ${keyWords}.` : ""
	}. Le poste doit être décrit de manière SEO friendly, en mettant en avant ses caractéristiques et avantages uniques.`,
	max_tokens: 100,
	temperature: 0.5,
})

```

Les jetons sont des séquences courantes de caractères trouvées dans le texte. Le `max_tokens` est le nombre maximum de jetons utilisés pour générer la description de poste. Vous pouvez en lire plus sur les jetons [ici](https://beta.openai.com/tokenizer).

La `temperature` spécifie la [température d'échantillonnage](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277) à utiliser. Des valeurs plus élevées signifient que le modèle prendra plus de risques. Par exemple, 0,9 sera le meilleur pour des applications plus créatives, et 0 (échantillonnage argmax) pour celles avec une réponse bien définie.

Enfin, nous analysons le flux de réponse de l'API OpenAI au format JSON et le retournons depuis la fonction. Vous pouvez en lire plus sur la méthode `json()` [ici](https://developer.mozilla.org/en-US/docs/Web/API/Response/json).

```js
const data = await response.json();
return data.choices[0].text;


```

Cette fonction `generateDescription` est utilisée à l'intérieur du gestionnaire de route API NextJS, et la sortie de l'API OpenAI est retournée depuis la route API.

```js
export default async function handler(req, res) {
  const { jobTitle, industry, keyWords, tone, numWords } = req.body;

  const jobDescription = await generateDescription({
    jobTitle,
    industry,
    keyWords,
    tone,
    numWords,
  });

  res.status(200).json({
    jobDescription,
  });
}

```

## Comment intégrer la route API NextJS

Nous avons créé l'interface utilisateur et la route API. Il est maintenant temps de les rassembler et de compléter notre application. Dans cette section, nous allons intégrer notre frontend et notre backend ensemble.

Tout d'abord, créez une fonction nommée `handleSubmit` dans le fichier `Dashboard.js` juste en dessous de l'endroit où vous avez défini les états.

```js
const handleSubmit = async (e) => {
    e.preventDefault();
    setIsGenerating(true);
    const res = await fetch("/api/returnJobDescription", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        jobTitle,
        industry,
        keyWords,
        tone,
        numWords,
      }),
    });
    setIsGenerating(false);
    const data = await res.json();
    setJobDescription(data.jobDescription.trim());
  };

```

Dans la fonction ci-dessus, nous empêchons d'abord la page de se recharger en utilisant `e.preventDefault()` lorsque le `form` est soumis. Nous mettons ensuite à jour l'état `isGenerating` à `true` en utilisant `setIsGenerating(true)`.

Nous utilisons à nouveau l'API `fetch` pour envoyer une requête POST à notre route API NextJS `/api/returnJobDescription` avec les valeurs d'entrée de l'utilisateur dans le `body` de la requête.

```js
body: JSON.stringify({
	jobTitle,
	industry,
	keyWords,
	tone,
	numWords,
})

```

Après la requête, nous définissons l'état `isGenerating` à `false`. Ensuite, nous convertissons la réponse au format JSON et la définissons dans l'état `jobDescription`.

```js
setIsGenerating(false);
const data = await res.json();
setJobDescription(data.jobDescription.trim());

```

Ensuite, mettez à jour le `form` avec l'événement `onSubmit` et passez-lui la fonction `handleSubmit()`

```js
<form onSubmit={(e) => handleSubmit(e)}>
...
</form>

```

Enfin, nous créons la fonction `handleCopy` pour copier l'état `jobDescription` dans le presse-papiers.

```js
const handleCopy = () => {
    navigator.clipboard.writeText(jobDescription);
    setIsCopied(true);
  };

```

Mettez à jour le bouton `Copier dans le presse-papiers` comme suit :

```js
<button
	onClick={handleCopy}
	className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
	type="submit"
	disabled={jobDescription === ""}
>
	{isCopied ? "Copié" : "Copier dans le presse-papiers"}
</button>

```

Voici le code complet pour le fichier `Dashboard.js` :

```js
import React, { useState } from "react";

export default function Dashboard() {
  const [jobDescription, setJobDescription] = useState("");

  const [jobTitle, setJobTitle] = useState("");
  const [industry, setIndustry] = useState("");
  const [keyWords, setKeyWords] = useState("");
  const [tone, setTone] = useState("");
  const [numWords, setNumWords] = useState("");

  const [isGenerating, setIsGenerating] = useState(false);
  const [isCopied, setIsCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(jobDescription);
    setIsCopied(true);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsGenerating(true);
    const res = await fetch("/api/returnJobDescription", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        jobTitle,
        industry,
        keyWords,
        tone,
        numWords,
      }),
    });
    setIsGenerating(false);
    const data = await res.json();
    setJobDescription(data.jobDescription.trim());
  };

  return (
    <div className="max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="grid gap-y-12 md:grid-cols-2 md:gap-x-12 ">
        <div className="">
          <form onSubmit={(e) => handleSubmit(e)}>
            <div className="flex flex-col">
              <label className="sr-only" htmlFor="jobTitle">
                Titre du poste
              </label>
              <input
                type="text"
                className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
                name="jobTitle"
                placeholder="Titre du poste"
                id="jobTitle"
                value={jobTitle}
                onChange={(e) => setJobTitle(e.target.value)}
                required
              />
            </div>
            <div className="flex flex-col">
              <label htmlFor="industry" className="sr-only">
                Secteur d'activité
              </label>
              <input
                value={industry}
                onChange={(e) => setIndustry(e.target.value)}
                className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
                placeholder="Secteur d'activité (Optionnel)"
                type="text"
                name="industry"
                id="industry"
              />
            </div>
            <div className="flex flex-col">
              <label htmlFor="keywords" className="sr-only">
                Mots-clés pour l'IA (Optionnel)
              </label>
              <textarea
                rows={7}
                value={keyWords}
                onChange={(e) => setKeyWords(e.target.value)}
                name="keyWords"
                id="keyWords"
                placeholder="Mots-clés pour l'IA (Optionnel)"
                className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
              />
            </div>
            <div className="flex flex-col">
              <label className="sr-only" htmlFor="tone">
                Ton
              </label>

              <select
                value={tone}
                onChange={(e) => setTone(e.target.value)}
                className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
                name="tone"
                id="tone"
              >
                <option value="default">Sélectionner le ton (Optionnel)</option>
                <option value="casual">Décontracté</option>
                <option value="friendly">Amical</option>
                <option value="professional">Professionnel</option>
                <option value="formal">Formel</option>
              </select>
            </div>
            <div className="flex flex-col">
              <label htmlFor="words" className="sr-only">
                Mots (Optionnel)
              </label>
              <input
                value={numWords}
                onChange={(e) => setNumWords(e.target.value)}
                type="number"
                className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
                placeholder="Nombre de mots - Par défaut 200 (Optionnel)"
                name="words"
                id="words"
              />
            </div>

            <button
              className={`bg-blue-600 w-full hover:bg-blue-700 text-white font-bold mt-6 py-2 px-4 rounded
                ${
                  isGenerating || jobTitle === ""
                    ? "cursor-not-allowed opacity-50"
                    : ""
                }`}
              type="submit"
              disabled={isGenerating || jobTitle === ""}
            >
              {isGenerating ? "Génération en cours..." : "Générer la description de poste"}
            </button>
          </form>
        </div>
        <div className="">
          <div className="flex flex-col">
            <label htmlFor="output" className="sr-only">
              Sortie
            </label>
            <textarea
              rows={
                jobDescription === ""
                  ? 7
                  : jobDescription.split("\n").length + 12
              }
              name="output"
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              disabled={jobDescription === ""}
              id="output"
              placeholder="Description de poste générée par l'IA"
              className="block w-full rounded-md bg-white border border-gray-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-4 py-2 placeholder-gray-500 my-2 text-gray-900"
            />
            <button
              onClick={handleCopy}
              className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
              type="submit"
              disabled={jobDescription === ""}
            >
              {isCopied ? "Copié" : "Copier dans le presse-papiers"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

```

Voici le code ci-dessus en action :

![m1ieud6fgxhqsgnec96n.gif](https://www.freecodecamp.org/news/content/images/2023/01/m1ieud6fgxhqsgnec96n-2.gif)

## Vous l'avez fait ! 🎉

Félicitations 👏 pour avoir construit ce projet **Générateur de descriptions de poste avec IA**.

## Conclusion

Dans ce tutoriel, nous avons appris comment construire un générateur de descriptions de poste avec Next.js en utilisant OpenAI ChatGPT.

Nous avons également discuté de la manière d'installer TailwindCSS dans un projet NextJS et de la manière de créer des routes API Next.js.

Voici quelques ressources supplémentaires qui peuvent être utiles :

* [Documentation Next.js](https://nextjs.org/docs/getting-started)
* [Documentation OpenAI](https://beta.openai.com/docs/introduction/overview)
* [Documentation TailwindCSS](https://tailwindcss.com/docs/installation)

_Ce tutoriel est un aperçu de l'un des projets de l'ebook gratuit 8 Projets IA. Vous pouvez obtenir un accès anticipé aux 8 tutoriels de projets complets [8AIProjects](http://8aiprojects.com/)._

Si vous êtes inspiré pour ajouter des fonctionnalités vous-même, n'hésitez pas à partager et à [me taguer](https://twitter.com/noharashutosh) – J'adorerais en entendre parler :)