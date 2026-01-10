---
title: Comment sécuriser une application Next.js IA déployée sur Vercel
subtitle: ''
author: Gideon Akinsanmi
co_authors: []
series: null
date: '2024-08-19T21:06:52.685Z'
originalURL: https://freecodecamp.org/news/how-to-secure-a-nextjs-ai-application-deployed-on-vercel
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724061409083/f9df1023-0bf0-4dc4-b97b-041738bfe5f8.png
tags:
- name: Next.js
  slug: nextjs
- name: Security
  slug: security
seo_title: Comment sécuriser une application Next.js IA déployée sur Vercel
seo_desc: In this in-depth guide, I’ll be showing how to secure a Next.js AI app deployed
  on Vercel. We’ll be taking a hands-on approach by starting with a simple AI app
  riddled with vulnerabilities. This article will guide you through how you can detect
  vulne...
---

Dans ce guide approfondi, je vais montrer comment sécuriser une application Next.js IA déployée sur Vercel. Nous allons adopter une approche pratique en commençant par une application IA simple truffée de vulnérabilités. Cet article vous guidera à travers la détection des vulnérabilités et l'application de correctifs dans une application Next.js IA existante.

Ce tutoriel couvre différents domaines du développement logiciel comme le full-stack, le développement cloud et l'intégration de tiers. Vous apprendrez à utiliser des outils comme Git/GitHub, Next.js et Vercel pour améliorer la sécurité d'une application IA.

De plus, si vous préférez regarder des implémentations réelles, il y a des vidéos YouTube à la fin de la plupart des sections pour vous montrer comment cela se fait.

## Table des matières

* [Prérequis](#heading-prealables)
    
* [Getting started](#heading-demarrer)
    
* [Exploration des fichiers du projet](#heading-exploration-des-fichiers-du-projet)
    
    * [Le fichier layout.tsx](#heading-le-fichier-layouttsx)
        
    * [Le fichier page.tsx](#heading-le-fichier-pagetsx)
        
    * [Le fichier hooks/useOpenAI.ts](#heading-le-fichier-hooksuseopenaits)
        
    * [Le fichier package.json](#heading-le-fichier-packagejson)
        
* [Comment obtenir vos clés API OpenAI](#heading-comment-obtenir-vos-cles-api-openai)
    
* [Comment déployer le projet sur Vercel](#heading-comment-deployer-le-projet-sur-vercel)
    
* [Vulnérabilité un : Exposition de données sensibles dans le frontend](#heading-vulnerabilite-un-exposition-de-donnees-sensibles-dans-le-frontend)
    
* [Vulnérabilité deux : Attaques DOS ou DDOS](#heading-vulnerabilite-deux-attaques-dos-et-ddos)
    
    * [Limitation de débit](#heading-limitation-de-debit)
        
    * [Protection DDOS de Vercel et Cloudflare](#heading-protection-ddos-de-vercel-et-cloudflare)
        
    * [Fonctionnalités de sécurité de Vercel](#heading-fonctionnalites-de-securite-de-vercel)
        
* [Vulnérabilité 3 : Pas d'authentification et d'autorisation](#heading-vulnerabilite-3-pas-dauthentification-et-dautorisation)
    
* [Optimisation du code](#heading-optimisation-du-code)
    
* [Conclusion](#heading-conclusion)
    

## **Prérequis**

Avant de commencer ce tutoriel, voici quelques-unes des choses dont vous avez besoin :

* Une connaissance de base de l'écriture de code [Next.js](https://nextjs.org)
    
* Un éditeur de code (comme VSCode) pour écrire et éditer le code source du projet.
    
* [Git](https://git-scm.com) et un compte [GitHub](https://github.com) pour le contrôle de version, l'intégration continue et l'authentification.
    
* Un compte [Vercel](https://vercel.com) pour héberger le projet.
    
* Un compte [OpenAI Developer](https://platform.openai.com) pour obtenir votre clé API.
    

## Getting Started

Tout d'abord, vous devez cloner ce [dépôt GitHub](https://github.com/Gidthecoder/nextjs-ai).

J'ai créé le dépôt spécifiquement pour ce tutoriel afin de vous montrer certaines des vulnérabilités que vous pourriez négliger lors de la création d'une application Next.js IA.

Pour cloner le projet, ouvrez votre interface de ligne de commande et naviguez jusqu'au dossier dans lequel vous souhaitez que le dépôt soit.

Ensuite, utilisez la commande `git clone` pour cloner le projet.

```plaintext
git clone https://github.com/Gidthecoder/nextjs-ai.git
```

N'oubliez pas que vous devez avoir déjà configuré Git dans votre système, sinon la commande ne fonctionnera pas.

Une fois cela fait, naviguez jusqu'au dossier en utilisant la commande ci-dessous :

```plaintext
cd nextjs-ai
```

Ensuite, tapez la commande ci-dessous pour installer les dépendances du projet :

```plaintext
npm install
```

Une fois cela fait, vous pouvez ouvrir le dossier dans votre éditeur de texte et explorer les fichiers.

Le code est bien commenté, donc vous ne devriez pas avoir beaucoup de problèmes à le comprendre.

Pour exécuter le projet, assurez-vous d'abord d'être dans le répertoire du projet dans votre CLI. Ensuite, exécutez la commande ci-dessous :

```plaintext
npm run dev
```

Si tout fonctionne bien, ouvrez votre navigateur et tapez `http://localhost:3000/` dans la barre de recherche.

Le résultat du navigateur devrait ressembler à ceci :

![Image montrant le projet affiché dans le navigateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1724021933164/2abbc405-c90b-44d1-bd8c-d2c233f42062.png align="center")

Si vous avez obtenu le même résultat, félicitez-vous. Bon travail.

Si vous essayez d'envoyer un message depuis le formulaire, vous remarquerez qu'un message d'erreur s'affiche. Cela est dû au fait que vous n'avez pas ajouté de clé API OpenAI au projet.

Mais ne vous inquiétez pas pour cela pour l'instant. Examinons les fichiers du projet.

Voici la vidéo pour cette section :

%[https://youtu.be/ataC9zP6aL0] 

## **Exploration des fichiers du projet**

Le projet que nous avons cloné est essentiellement un wrapper ChatGPT. Vous lui posez une question et il vous donne une réponse.

Sous le capot, le projet utilise Next.js pour envoyer une requête API au serveur OpenAI et affiche la réponse à l'utilisateur.

Si vous avez ouvert le dossier via VSCode, la structure du projet devrait ressembler à ceci :

![Image montrant la structure des dossiers du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1724054546731/203d0875-1694-48ed-9ed4-a92f37b887fb.png align="center")

Le projet a 4 dossiers de premier niveau : `.next`, `node_modules`, `public` et `src`.

Les fichiers dans le dossier racine incluent `.gitignore`, `package.json`, `tailwind.config.js`, `tsconfig.json`, et autres.

La plupart de votre travail se fera dans le dossier `src/app` car il contient tout le code dont vous avez besoin pour le projet.

Le dossier app représente le routeur d'application. Il contient `layout.tsx`, `page.tsx`, `global.css`, le dossier `hooks`, et ainsi de suite.

### **Le fichier layout.tsx**

`layout.tsx` est un fichier TypeScript qui contient le code pour la mise en page racine.

Des lignes 1 à 3, vous importerez le type `Metadata`, la police `Inter` et un fichier `globals.css` qui vous permet d'utiliser les classes utilitaires TailwindCSS.

```javascript
import type { Metadata } from "next";

import { Inter } from "next/font/google";

import "./globals.css";
```

Des lignes 5 à 10, vous créerez les variables `inter` et `metadata`. `inter` initialise la police `Inter`, et `metadata` stocke un objet qui contient le titre et la description du site, similaire aux éléments de titre et de méta HTML.

```javascript
const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "WriterAI",
  description: "Un wrapper ChatGPT qui répond à vos questions",
};
```

Ensuite, vous créerez le composant `RootLayout` qui enveloppera toutes les pages du projet.

```javascript
export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {children}
      </body>
    </html>
);
}
```

### **Le fichier page.tsx**

`app/page.tsx` est un fichier TypeScript qui représente le code qui sera rendu dans le navigateur lorsque l'URL racine (/) est appelée.

La ligne 1 contient une directive `use client` qui déclare le fichier comme un composant client. De cette manière, nous pouvons utiliser pleinement les fonctionnalités de React.js dans le composant.

```javascript
"use client";
```

Des lignes 3 à 6, vous importerez un hook personnalisé `useOpenAI` et les hooks intégrés de React (`useState`, `useRef`, `useEffect`, ...).

```javascript
//import the custom hook for getting the response from the OpenAI API
import useOpenAI from './hooks/useOpenAI';

import {useState, useRef, useEffect, FormEvent} from 'react';
```

Ensuite, vous créerez un type personnalisé `Message` qui sera utilisé avec l'état qui stocke les messages entre l'utilisateur et l'API OpenAI.

```javascript
type Message = {
  role: string;
  content: string;
};
```

Les lignes 13 à 120 contiennent le code pour le composant `Home` qui sera rendu dans le navigateur lorsque l'URL racine est appelée.

Dans le composant `Home`, la ligne 15 initialise le hook `useOpenAI`.

```javascript
//initialize the custom hook
const getCompletion = useOpenAI();
```

La ligne 17 initialise un hook `useRef` qui sera utilisé pour référencer l'élément DOM conteneur qui enveloppe les messages entre l'utilisateur et le serveur.

```javascript
const chatContainerRef = useRef<HTMLDivElement>(null);
```

Des lignes 19 à 23, vous créez une variable `content` qui représente un tableau qui sera utilisé comme valeurs initiales pour l'état qui stocke le chat/messages.

```javascript
//initial chats for the site
 let content: Message[] = [
   {role: "user", content: "Are you ready to write about any topic for me"},
   {role: "assistant", content: "Always ready bruv. what is your topic?"}
]
```

Les lignes 25 à 30 représentent les variables d'état du composant. `Input` suit le texte saisi dans l'élément d'entrée par l'utilisateur. `chats` stocke les messages de l'utilisateur et de l'API OpenAI. Il est initialisé avec la variable `content`. `isTyping` suit lorsque l'utilisateur tape. Sa valeur initiale est `false`.

```javascript
 //this state stores the input value
 let [input, setInput] = useState<string>('');
 //this state stores the chats
 let [chats, setChats] = useState<Message[]>(content);
 //this state keeps track of when the AI is typing
 let [isTyping, setIsTyping] = useState<boolean>(false);
```

Le code des lignes 31 à 72 représente la fonction `handlerChat` qui est le gestionnaire d'événements appelé chaque fois qu'un utilisateur appuie sur la touche Entrée ou le bouton de demande dans le formulaire.

En résumé, son travail est de recevoir l'invite du formulaire, de mettre à jour les états `input`, `isTyping` et `chats`, de transmettre l'invite à la fonction `getCompletion` du hook `useOpenAI`, d'attendre la réponse et de l'afficher à l'utilisateur.

```javascript
//handleChat event handler for the submit event
let handleChat = async (prompt: string, e: FormEvent) => {
  //prevent the form from reloading the entire page when submitting
  e.preventDefault();

  //if there is no value in the input or it is clicked when the isTyping is true, do nothing
  if (!prompt || isTyping) return;

  //set isTyping state to true. 'true' adds an element displaying 'AI typing'
  setIsTyping(true);
  
  //clear the content of the input state. This also clears the input element which displays the value.
  setInput('');
   
  //updates the chats state with the prompt sent from the input
  setChats(prevChats => {
    const updatedChats = [...prevChats, { role: 'user', content: prompt}];
    return updatedChats;
  });

  try {
    //send the prompt through the openai api and wait for the response
    const result = await getCompletion(prompt);

    //update the chat prompt with response gotten from the openai api
    setChats(prevChats => {
      const updatedChats = [...prevChats, Object(result)];
      return updatedChats;
     });

    //set isTyping state to false. 'false' removes the element displaying 'AI typing'
     setIsTyping(false)

  } catch (error) {
    //catch any possible error from the request
    console.error("Error fetching completion:", error);

    //set isTyping state to false. 'false' removes the element displaying 'AI typing'
    setIsTyping(false)
  }
}
```

Les lignes 73 à 78 contiennent le code dans le hook `useEffect`. Chaque fois que l'état `chats` est mis à jour, le document sera défilé vers le bas afin que les messages les plus récents soient affichés.

```javascript
useEffect(() => {
  if (chatContainerRef.current) {
    //whenever the chats state is updated, scroll to the bottom of the container element to display the recent messages
    chatContainerRef.current.scrollTo({ top: chatContainerRef.current.scrollHeight, behavior: 'smooth' });
  }
}, [chats]);
```

Le code des lignes 81 à 120 contient le balisage qui sera rendu dans le navigateur.

Des lignes 91 à 99, le contenu de l'état `chats` est ajouté au balisage en utilisant la fonction `map`. Les messages de l'IA sont alignés à gauche tandis que ceux de l'utilisateur sont alignés à droite.

```javascript
{
  //the content of chats state is looped to display the content. if the content is from the user, it will be aligned to the right. if it's from the AI, it'll be aligned to the left
  chats.map((data, index) =>
    <div key={index} className={`${data.role == 'user'? 'text-right': 'text-left'} my-[30px]`}>
      <p className="text-[15px] bg-[#4d4d4dff] max-w-[60%] p-[10px] lg:p-[20px] rounded-xl text-left text-[#f2f2f2ff] inline-block">
        {data.content}
      </p>
    </div>
  ))
}
```

Des lignes 101 à 107, il y a un bloc de code qui est toujours rendu chaque fois que l'état `isTyping` (qui est déclenché chaque fois qu'un utilisateur envoie un message et attend une réponse) est `true`.

```javascript
{/*if the isTyping state is true, display the element. if not, hide it.*/}
<div className={isTyping? 'block': 'hidden'}>
  <div className='text-left my-[30px]'>
    <p className="text-[15px] bg-[#4d4d4dff] max-w-[60%] p-[10px] lg:p-[20px] rounded-xl text-center text-[#f2f2f2ff] inline-block">
      AI Typing...
    </p>
  </div>
</div>
```

Les lignes 113 à 116 contiennent le code qui représente le formulaire. Chaque fois que l'élément d'entrée est modifié, l'état `input` sera mis à jour. Et chaque fois que le formulaire est soumis (lorsque le bouton est cliqué ou que l'entrée est saisie), la fonction `handleChat` est appelée, envoyant la valeur de l'état `input` et l'événement du formulaire comme arguments.

```javascript
{/*when the form is submitted, activate a submit event that sends the value of the input and the event to the handleChat function */}
<form action='' onSubmit={(e) => handleChat(input, e)}>
  <input className=" lg:w-[50%] w-[70%] ml-[5%] lg:ml-[20%] p-[10px] outline-none bg-[#4d4d4dff] text-[15px] text-[#f2f2f2ff]" type='text' value={input} placeholder='Ask your questions' onChange={ (e) => setInput(e.target.value)}/>
  <button className='py-[10px] px-[20px] bg-black text-[15px] text-[#f2f2f2ff]'>Ask</button>
</form>
```

### **Le fichier hooks/useOpenAI.ts**

Dans le fichier `hooks/useOpenAi.ts`, vous importerez la bibliothèque OpenAI et stockerez la clé API dans une variable.

```javascript
import OpenAI from 'openai';

const API_KEY = 'YOUR-API-KEY';
```

Une fonction `useOpenAI` représentant le hook a été créée.

Dans la fonction, une instance de l'objet OpenAI a été créée. Il y a également une fonction `getCompletion` asynchrone qui reçoit l'invite de l'argument et envoie la requête à l'API OpenAI. Si une erreur survient en cours de route, un message d'erreur est retourné.

```javascript
function useOpenAI() {
  const client = new OpenAI({ apiKey: API_KEY, dangerouslyAllowBrowser: true });

  const getCompletion = async (prompt: string) => {
    try {
      let completion = await client.chat.completions.create({
        messages: [
            { "role": "system", "content": "Your job is to write about any topic asked by the user" },
            { "role": "user", "content": prompt }
        ],
        model: "gpt-3.5-turbo",
        });

      return completion.choices[0].message;

    } catch(e){
      return {"role": "assistant", "content": "Something went wrong"}
    }
  };

  return getCompletion;

}
```

N'oubliez pas que vous obtenez un message d'erreur chaque fois que vous envoyez un message depuis le site.

Cela est dû au fait que vous n'avez pas ajouté les clés API OpenAI au projet. Nous aborderons cette partie plus tard.

### **Le fichier package.json**

Le fichier `Package.json` contient des informations sur les bibliothèques et les scripts nécessaires pour exécuter votre projet.

Le fichier doit ressembler à ceci :

```javascript
{
  "name": "nextjs-ai",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@upstash/ratelimit": "^2.0.1",
    "@vercel/kv": "^2.0.0",
    "next": "14.2.5",
    "next-auth": "^4.24.7",
    "openai": "^4.52.7",
    "react": "^18",
    "react-dom": "^18"
  },
  "devDependencies": {
    "@types/node": "^20",
    "@types/react": "18",
    "@types/react-dom": "^18",
    "eslint": "^8",
    "eslint-config-next": "14.2.5",
    "postcss": "^8",
    "tailwindcss": "^3.4.1",
    "typescript": "^5"
  }
}
```

Dans le code ci-dessus, le script 'dev' sera utilisé pour exécuter le projet en mode développement. C'est pourquoi vous utilisez `npm run dev` dans le CLI.

Les deux scripts suivants, `build` et `start`, seront utilisés pour optimiser les fichiers et démarrer le projet dans un environnement de production. Vous n'avez pas besoin de vous en soucier car Vercel s'occupera de tout.

`next`, `react` et `react-dom` sont les bibliothèques principales du projet.

La bibliothèque `openai` sera utilisée pour communiquer avec l'API OpenAI.

`@upstash/ratelimit`, `@vercel/kv` et `next-auth` seront utilisés pour implémenter certaines fonctionnalités de sécurité dans les prochaines sections.

Les dépendances de développement ne seront utilisées que pendant le développement du projet. Elles incluent `typescript`, `tailwindcss`, etc.

## **Comment obtenir vos clés API OpenAI**

Pour que le projet fonctionne comme prévu, vous devez ajouter la clé secrète OpenAI au projet. Cette clé permettra à l'application de s'intégrer avec succès à l'API OpenAI, permettant aux utilisateurs d'envoyer des requêtes de prompt depuis le côté client et de recevoir des réponses IA.

Pour obtenir vos clés secrètes OpenAI, vous devez d'abord vous inscrire (ou vous connecter) sur le site [platforms.openai.com](https://platforms.openai.com). Ensuite, vous devez configurer les détails de votre carte de paiement si vous ne l'avez pas déjà fait. Sans eux, l'API ne fonctionnera pas.

Après cela, allez dans la section des clés API pour créer votre clé API. Assurez-vous de la copier immédiatement.

Ensuite, vous devez stocker la clé API en tant que variable d'environnement en créant un fichier `.env.local` à la racine de votre projet et en collant la valeur là.

```javascript
NEXT_PUBLIC_API_KEY='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'
```

Le nom de la propriété commence par `NEXT_PUBLIC` afin qu'elle puisse être utilisée côté client.

Ensuite, à la ligne 4 du fichier `useOpenAI.ts`, changez le code en ceci :

```javascript
const API_KEY = process.env.NEXT_PUBLIC_API_KEY;
```

Une fois cela fait, vous pouvez enregistrer les fichiers, attendre que le serveur Next.js recompile et tester le site.

Si vous avez éteint le serveur, naviguez jusqu'au répertoire de votre projet dans votre CLI et entrez `npm run dev`. Une fois que le serveur a compilé, ouvrez votre navigateur et tapez `http://localhost:3000/` dans la barre de recherche. Assurez-vous également que votre wifi est connecté afin que votre requête puisse être envoyée à l'API OpenAI.

Une fois le site chargé, essayez d'interagir avec lui, posez quelques questions et attendez votre réponse des serveurs OpenAI.

Si vous avez suivi toutes les étapes correctement, voici à quoi devrait ressembler votre interaction :

%[https://youtu.be/5cQWdwxeZpc] 

Le style peut ne pas être beau, mais cela fonctionne. Vous pouvez travailler sur le style plus tard.

Voici la vidéo pour cette section :

%[https://youtu.be/kv-oS77w394] 

## **Comment déployer le projet sur Vercel**

Maintenant, il est temps de déployer le projet sur Vercel. Nous utiliserons Vercel pour le déploiement dans ce tutoriel, car les créateurs de Vercel ont également créé Next.js, donc le déploiement ne sera pas stressant.

Mais avant cela, vous devrez pousser vos modifications sur GitHub afin de pouvoir déployer facilement le projet sur Vercel.

Pour cela, vous devez taper les commandes suivantes :

```javascript
git init

git add .

git commit -m "first commit"

git branch -m master main
```

Une fois que vous avez fait cela, vous devriez aller sur votre compte GitHub pour créer un nouveau dépôt. Assurez-vous de ne pas ajouter de fichiers, y compris un README ou une licence, pour éviter des erreurs Git lors du déploiement.

Après avoir créé le dépôt, copiez le lien du dépôt et collez-le dans la commande ci-dessous :

```javascript
git remote add origin <link-of-your-repo>
```

Maintenant, poussez le code vers la branche principale :

```javascript
git push -u origin main
```

Une fois que vous avez fait cela, consultez le dépôt dans votre compte GitHub pour vous assurer qu'il a été validé dans la branche principale.

Une fois cela fait, vous devez vous inscrire à Vercel avec votre compte GitHub.

Ensuite, importez le dépôt nextjs-ai depuis GitHub et déployez-le.

Avant de le déployer, collez le contenu de votre fichier `.env.local` dans la section des variables d'environnement. Après cela, cliquez sur **Deploy** et attendez que le projet soit déployé.

Après quelques secondes, votre application sera déployée et vous verrez l'URL publique de votre projet.

Lorsque vous visitez le lien déployé, le site devrait se comporter comme ceci :

%[https://youtu.be/xDsBqgBTsB0] 

Bien que l'application fasse ce qu'elle est censée faire, elle est remplie de vulnérabilités de sécurité qui peuvent vous coûter beaucoup d'argent en raison de cyberattaques. Nous allons donc faire une pause avant d'obtenir un nom de domaine afin de corriger ces problèmes.

%[https://youtu.be/eVai4j47rmM] 

## **Vulnérabilité un : Exposition de données sensibles dans le frontend**

Exposer des données sensibles comme les clés API dans le frontend est dangereux car les données peuvent être volées et utilisées de manière malveillante par un attaquant.

Bien que vous ayez stocké la clé API en tant que variable d'environnement, elle peut toujours être vue dans le navigateur. Cela est dû au fait que vous avez utilisé la variable d'environnement dans un hook React qui sera exécuté côté client.

Cela signifie que toute personne ayant suffisamment de compétences peut vérifier vos clés API dans le navigateur.

Bien que l'API OpenAI applique strictement l'utilisation de son API côté serveur, en fournissant une prop `dangerouslyAllowBrowser` pour rappeler aux utilisateurs les dangers de l'utiliser côté client, la plupart des API n'ont pas ce type d'application.

Si j'étais un attaquant, voici comment je pourrais obtenir vos clés API OpenAI :

Tout d'abord, j'ouvrirais les outils de développement du navigateur et je cliquerais sur l'onglet réseau. Ensuite, j'entrerais une invite dans l'entrée et je cliquerais sur entrer. Alors que la requête était envoyée, l'onglet réseau capturerait les requêtes sortantes et afficherait toutes les informations.

Ensuite, lorsque je cliquerais sur l'onglet des en-têtes et que je naviguerais vers les en-têtes de la requête, je pourrais voir l'en-tête d'autorisation et la clé API.

La vidéo ci-dessous montre une démonstration :

%[https://youtu.be/ul5kmGYvgDw] 

### Comment corriger la vulnérabilité 1 :

Alors, comment corriger cela ? Ne vous inquiétez pas, c'est simple.

Pour éviter d'exposer des données côté client, vous devez déplacer le code sensible vers le backend et accéder à vos variables d'environnement depuis le côté serveur. De cette manière, toute requête du navigateur est abstraite et le serveur sert de proxy pour communiquer avec l'API OpenAI.

Dans Next.js, vous pouvez faire cela en utilisant des gestionnaires de route. Nous utiliserons des gestionnaires de route pour recevoir les requêtes entrantes vers la route `api/ai`, envoyer l'invite à l'API OpenAI et retourner les réponses côté client.

Les gestionnaires de route sont des fonctions côté serveur, donc leur code ne sera pas visible dans le navigateur et votre variable d'environnement sera sécurisée.

Maintenant que vous savez ce qu'il faut faire, mettons à jour le code.

Tout d'abord, retirez le préfixe `NEXT_PUBLIC` de `NEXT_PUBLIC_API_KEY` pour qu'il devienne `API_KEY`. Cela garantit que la clé ne sera pas disponible côté client.

```javascript
API_KEY='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'
```

Ensuite, créez un dossier `api` dans `app`. Ce dossier stockera tous les gestionnaires de route pour votre projet.

Ensuite, créez un dossier `ai` et un fichier `route.ts` à l'intérieur. Le dossier `ai` doit être dans `app/api`.

Le fichier `api/ai/route.ts` gérera les requêtes vers la route `api/ai`.

Ensuite, ajoutez ce code à votre fichier `api/ai/route.ts` :

```javascript
import {NextRequest, NextResponse} from 'next/server';

import OpenAI from 'openai';

const API_KEY = process.env.API_KEY;

const client = new OpenAI({ apiKey: API_KEY });

export async function POST (req: NextRequest) {
  let {prompt} = await req.json();

  if (!prompt) {
    return NextResponse.json({ content: 'Prompt is required' }, {status: 400});
  }

  try {
    let completion = await client.chat.completions.create({
      messages: [
          { role: 'system', content: 'Your job is to write about any topic asked by the user' },
          { role: 'user', content: prompt }
      ],
      model: 'gpt-3.5-turbo',
    });

    return NextResponse.json(completion.choices[0].message, {status: 200});

  } catch (error) {
    console.error(error)
    return NextResponse.json({ content: 'Internal Server Error' }, {status: 500});
  } 
};
```

Dans le code ci-dessus, vous avez importé les fonctions `NextRequest` et `NextResponse` représentant des extensions de l'API Web Request et de l'API Web Response. Vous avez également importé la fonction `OpenAI` de la bibliothèque `openai`.

Ensuite, vous avez créé une variable (`API_KEY`) qui stocke la variable d'environnement API_KEY. Vous avez également créé une autre variable qui stocke une nouvelle instance de l'objet OpenAI.

Enfin, vous avez créé une fonction POST pour gérer les requêtes POST vers la route `api/ai`. La fonction reçoit l'invite et la transmet à l'API OpenAI, attend une réponse et la retourne à l'utilisateur. Si la requête n'a pas de propriété prompt dans le corps ou s'il y a une erreur en cours de route, un message d'erreur sera retourné à l'utilisateur.

Ensuite, allez dans votre fichier `hooks/useOpenAI.ts` et remplacez-le par ceci :

```javascript
const useOpenAI = () => {
  const getCompletion = async (prompt: string) => {
    try {
      const response = await fetch('/api/ai', {
        method: 'POST',
        body: JSON.stringify({ prompt }),
        headers: {
          'Content-Type': 'application/json',
        }
      });

      const result = await response.json()

      if (!response.ok) {
        return { role: 'assistant', content: result.content};
      }

      return result;

    } catch (error) {
      return { role: 'assistant', content: 'Something went wrong' };
    }

  };

  return getCompletion;
};

export default useOpenAI;
```

Dans le code ci-dessus, vous avez modifié le hook `useOpenAI` de sorte que si `getCompletion` est appelé, il enverra une requête fetch à la route `api/ai` et retournera la réponse à l'utilisateur. Si la requête n'est pas réussie, un message d'erreur sera retourné à l'utilisateur.

Si vous avez fait cela, il est temps de tester votre endpoint.

Dans votre système, naviguez jusqu'au CLI du projet et exécutez la commande ci-dessous :

```javascript
npm run dev
```

Si vous testez le site et que tout se passe bien, cela signifie que tout est correct.

Maintenant, vérifions si vous pouvez obtenir les clés API dans les outils de développement :

%[https://youtu.be/psjSXJnkJLY] 

Dans la vidéo ci-dessus, vous pouvez voir qu'aucune clé API n'a été exposée dans les en-têtes de requête.

Maintenant que cela est résolu, vous devriez pousser les modifications vers votre dépôt GitHub.

Toute modification apportée dans la branche principale de votre dépôt GitHub sera automatiquement déployée sur Vercel.

Exécutez ces commandes pour mettre à jour votre dépôt GitHub :

```javascript
git add .

git commit -m "moved sensitive code to backend"

git push -u origin main
```

Après avoir mis à jour les modifications, allez sur la page de déploiement de votre projet sur Vercel pour confirmer que le déploiement a réussi.

Malheureusement, le déploiement est susceptible d'échouer car vous n'avez pas mis à jour les variables d'environnement que vous avez ajoutées à Vercel (de `NEXT_PUBLIC_API_KEY` à `API_KEY`).

Vous devez donc aller dans **paramètres** > **variables d'environnement**, et importer le fichier `.env.local` de votre projet.

Une fois que vous avez fait cela, allez sur la page de déploiement et redéployez la dernière modification.

Après le déploiement réussi, visitez le site et vérifiez l'onglet réseau pour confirmer que les clés API ne sont pas exposées lorsque vous envoyez des messages depuis l'invite.

Si aucune clé API n'est visible dans l'en-tête de la requête, cela signifie que votre code sensible a été déplacé avec succès vers le backend et que vos dernières modifications ont été déployées.

Félicitations ! Maintenant, passons à la partie suivante...

Mais d'abord, voici la vidéo pour cette section :

%[https://youtu.be/V7Cm6kTyCQE] 

## **Vulnérabilité deux : Attaques DOS et DDOS**

Bien que notre clé API soit sécurisée dans le backend, l'application est toujours vulnérable aux attaques par déni de service (DOS) et aux attaques par déni de service distribué (DDOS).

Une attaque DOS est lorsque votre site est inondé de requêtes excessives provenant d'un seul appareil qui submerge votre serveur et empêche vos utilisateurs réels de profiter des services de votre application.

Une attaque plus avancée est une attaque par déni de service distribué (DDOS) qui implique l'envoi d'une quantité écrasante de requêtes provenant de plusieurs appareils simultanément vers votre site.

Différentes zones d'un site peuvent être vulnérables aux attaques DOS ou DDOS. L'attaque peut cibler votre infrastructure DNS, votre base de données, vos points de terminaison API et même vos fichiers statiques.

Sans des stratégies d'atténuation efficaces, les attaques DoS ou DDoS peuvent entraîner des pertes financières importantes en raison de l'augmentation des coûts des services cloud et des dépenses impliquées dans la restauration et la sécurisation de votre site.

Pour comprendre comment fonctionne cette attaque, essayons de simuler une simple attaque DOS sur notre application IA.

Si vous étiez un attaquant, vous pourriez exécuter le script ci-dessous dans la console de votre navigateur pour envoyer 50 requêtes à votre route `api/ai`.

```javascript
//fonction pour envoyer la requête
const getCompletion = async (prompt) => {
  try {
    const response = await fetch('/api/ai', {
      method: 'POST',
      body: JSON.stringify({ prompt }),
      headers: {
        'Content-Type': 'application/json',
      },
   });

    const result = await response.json();
    if (!response.ok) {
      return { role: 'assistant', content: result.content};
   }
   
   return result;

  } catch (error) {
    return { role: 'assistant', content: 'Something went wrong' };
  }
};

//fonction pour envoyer la requête 50 fois
const attackServer = async () => {
  const prompt = ['Write about a lion', 'write about a tiger', 'write about america', 'write about ice cream', 'write about pizza'];

  const numRequests = 50;

  const results = [];

  for (let i = 0; i < numRequests; i++) {
    const startTime = performance.now();
    const result = await getCompletion( prompt[Math.floor(Math.random()*4)] );
    const endTime = performance.now();
    const responseTime = endTime - startTime;

    results.push({
      index: i,
      result,
      responseTime,
    });

    console.log(`Request ${i + 1}: Response time = ${responseTime}ms`);
  }

  return results;

};

// commande pour activer l'attaque et afficher le résultat
attackServer().then((results) => {
  console.log('All requests completed');
  console.table(results);
});
```

Dans le code ci-dessus, vous avez collé deux fonctions asynchrones (`getCompletion` et `attackServer`) dans la console.

`getCompletion` contient la requête fetch qui sera envoyée à la route `api/ai`. `attackServer` contient le code qui sera utilisé pour appeler la fonction `getCompletion` 50 fois.

Après cela, vous avez collé les dernières commandes qui exécuteront la fonction `attackServer` et afficheront le résultat contenant les informations sur toutes les requêtes envoyées, y compris les données reçues du serveur et le temps de réponse.

Voici comment cela s'est passé pour moi :

%[https://youtu.be/qh0WgB6Ovy8] 

Bien que cette simple attaque ait impliqué l'envoi de 50 requêtes à la route API tierce, elle m'a en fait coûté près de 0,02 $ dans mon utilisation de l'API OpenAI. Si l'attaque avait impliqué 50 000 requêtes, elle m'aurait coûté 20 dollars. Si l'attaque avait impliqué 50 000 000 requêtes, elle m'aurait coûté près de 20 000 $.

Différentes stratégies peuvent être mises en œuvre dans Next.js et Vercel pour protéger votre site contre ces attaques. Elles incluent la limitation de débit, les pare-feu, la protection DDOS de Vercel/Cloudflare, le mode défi d'attaque, la gestion des dépenses et la surveillance du site web.

### **Limitation de débit**

La limitation de débit est une méthode utilisée pour bloquer les requêtes répétitives provenant d'un appareil qui dépasse un certain nombre dans un laps de temps donné. Si les requêtes dépassent un seuil, l'utilisateur peut être temporairement restreint d'accéder à un service.

Il existe différents algorithmes de limitation de débit, mais nous utiliserons un algorithme simple qui restreint l'accès au point de terminaison api/ai chaque fois qu'un utilisateur envoie trop de requêtes.

Nous utiliserons la base de données Vercel KV et la bibliothèque `@upstash/ratelimit` pour implémenter cet algorithme de limitation de débit.

`@upstash/ratelimit` est une puissante bibliothèque de limitation de débit conçue pour être utilisée dans un environnement serverless comme les fonctions Next.js. Vercel KV est un service de base de données Redis que nous utiliserons pour suivre les requêtes des utilisateurs.

Tout d'abord, nous devons configurer Vercel KV. Pour cela, créez une base de données KV en cliquant sur **Stockage** > **Créer une base de données Vercel KV**. Une fois qu'une boîte de dialogue apparaît, remplissez les informations nécessaires. Donnez au champ de nom n'importe quelle valeur, sélectionnez une région, sélectionnez votre environnement (soit développement, prévisualisation ou production), et enfin cliquez sur connecter. Ensuite, connectez-vous au projet.

Ensuite, vérifiez vos variables d'environnement dans l'onglet des paramètres pour confirmer que vos clés et jetons KV ont été ajoutés.

Ensuite, créez un fichier `middleware.ts` dans le dossier `src` et ajoutez ce code :

```javascript
import { NextRequest, NextResponse } from 'next/server';

import { Ratelimit } from '@upstash/ratelimit';

import { kv } from '@vercel/kv';

const ratelimit = new Ratelimit({
  redis: kv,
  // 1 requête de la même IP toutes les 30 secondes
  limiter: Ratelimit.slidingWindow(1, '30 s'),
});

export const config = {
  matcher: '/api/ai'
}

export default async function middleware(request: NextRequest) {
  const ip = request.ip || '127.0.0.1';
  const { success, pending, limit, reset, remaining } = await ratelimit.limit(
    ip
  );
  console.log(success)
  return success
    ? NextResponse.next()
    : NextResponse.json({ role: 'assistant', content: 'too many requests' }, {status: 429});
}
```

Dans le code ci-dessus, vous avez importé `NextRequest` et `NextResponse` de `next/server`, `Ratelimit` de `@upstash/ratelimit`, et `kv` de `@Vercel/kv`. Ensuite, vous avez configuré la fonction `Ratelimit` pour utiliser la base de données KV et permettre seulement 1 requête toutes les 30 secondes.

Ensuite, vous avez créé une variable de configuration pour vous assurer que seules les requêtes vers la route `api/ai` sont limitées en débit. Enfin, vous avez créé une fonction middleware qui examine les requêtes vers api/ai. Si l'adresse IP de la requête n'a pas dépassé le seuil de limitation de débit, elle sera transmise à `api/ai`. Si elle a dépassé le seuil, un message d'erreur sera retourné à l'utilisateur.

Pour confirmer que l'algorithme de limitation de débit a été implémenté avec succès, vous devrez mettre à jour le dépôt GitHub et tester le dernier déploiement Vercel.

Vous ne pouvez pas tester l'algorithme sur le serveur local car `request.ip` n'est disponible que sur Vercel.

Comme d'habitude, suivez les commandes ci-dessous pour pousser les modifications locales vers GitHub :

```javascript
git add .

git commit -m "rate limiting algorithm done"

git push -u origin main
```

Après la mise à jour réussie, visitez la page de déploiement de votre projet sur Vercel pour confirmer que les modifications GitHub ont été déployées avec succès.

Maintenant, visitez le lien du site déployé et collez le script ci-dessous pour confirmer que votre algorithme de limitation de débit a été implémenté avec succès.

```javascript
//fonction pour envoyer la requête
const getCompletion = async (prompt) => {
  try {
    const response = await fetch('/api/ai', {
      method: 'POST',
      body: JSON.stringify({ prompt }),
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      return { role: 'assistant', content: 'Internal server error' };
    }

    const result = await response.json();
    return result;

  } catch (error) {
    return { role: 'assistant', content: 'Something went wrong' };
  }
};

//fonction pour envoyer la requête 50 fois
const attackServer = async () => {
  const prompt = ['Write about a lion', 'How are you', 'write about america', 'write about ice cream', 'what is your name'];

  const numRequests = 50;

  const results = [];

  for (let i = 0; i < numRequests; i++) {
    const startTime = performance.now();
    const result = await getCompletion( prompt[Math.floor(Math.random()*4)] );
    const endTime = performance.now();
    const responseTime = endTime - startTime;

    results.push({
      index: i,
      result,
      responseTime,
    });

    console.log(`Request ${i + 1}: Response time = ${responseTime}ms`);
  }

  return results;
};

// commande pour activer l'attaque et afficher le résultat
attackServer().then((results) => {
  console.log('All requests completed');
  console.table(results);
});
```

Voici comment cela s'est passé pour moi :

%[https://youtu.be/pBkJiNsR7A0] 

Dans la vidéo ci-dessus, vous pouvez voir que la plupart des réponses étaient des messages d'erreur. Cela signifie que l'algorithme de limitation de débit fonctionne. Si un utilisateur essaie d'envoyer plus d'une requête toutes les 30 secondes, il recevra un message d'erreur.

Voici la vidéo pour cette section :

%[https://youtu.be/iDhAxDEoqHo] 

### **Protection DDOS de Vercel et Cloudflare**

En plus de la limitation de débit, vous pouvez utiliser la mitigation automatique DDOS de Vercel. Selon le site web de Vercel, il n'y a pas de frais pour la protection DDOS. Donc tout ce que vous pouvez faire est de faire confiance à leur service.

De plus, si vous avez (ou souhaitez acheter) un nom de domaine, vous pouvez utiliser Cloudflare et obtenir une protection DDOS gratuite et illimitée et une sécurité pour votre application. Vous pouvez consulter le site [Cloudflare](https://www.cloudflare.com/en-gb/ddos) pour plus d'informations.

### **Fonctionnalités de sécurité de Vercel**

En plus des mesures ci-dessus, vous pouvez également utiliser une combinaison de gestion des dépenses, de mode défi d'attaque, de règles Vercel WAF et de surveillance du site web pour améliorer la sécurité de votre application.

Tout d'abord, vous configurez la gestion des dépenses pour vous notifier lorsque vos factures atteignent certains seuils et pour suspendre vos projets lorsqu'ils atteignent un montant. Une fois que vous savez combien vous allez dépenser, vous pouvez définir le montant dans votre paramètre de gestion des dépenses.

Une autre fonctionnalité de sécurité de Vercel est le mode défi d'attaque. Vous pouvez utiliser le mode défi d'attaque pour faire passer à vos utilisateurs certaines vérifications avant qu'ils puissent continuer à utiliser votre site. Cela doit être fait temporairement lorsque vous recevez une notification concernant vos factures ou que vous remarquez un trafic inhabituel sur votre site.

Il y a aussi les règles WAF personnalisées. Il existe différentes règles dans les paramètres que vous pouvez utiliser. Vous pouvez définir des règles qui restreignent l'accès à des points de terminaison spécifiques et à des méthodes de requête. Vous pouvez également restreindre les utilisateurs avec un en-tête de requête spécifique, une adresse IP, un protocole, un continent et un pays.

Il est toujours important de surveiller le trafic de votre site et l'utilisation de vos ressources. Si vous remarquez une augmentation dirigée vers une route spécifique sans le flux d'utilisation approprié, vous pouvez configurer le mode défi d'attaque et des règles WAF personnalisées pour réduire la possibilité d'une attaque.

En résumé, pour protéger votre application IA contre une attaque DOS/DDOS, vous pouvez configurer la limitation de débit, la gestion des dépenses, les pare-feu personnalisés, le mode défi d'attaque et la surveillance du site web.

Je pense qu'il est sûr de dire que cette vulnérabilité a été corrigée.

## **Vulnérabilité 3 : Pas d'authentification et d'autorisation**

Bien que vous ayez mis en œuvre certaines mesures qui protègent votre site contre différentes formes d'attaque, une autre vulnérabilité peut compromettre le travail que vous avez fait jusqu'à présent.

Savez-vous ce que c'est ?

C'est l'absence de mécanismes d'authentification et d'autorisation.

Pour une application qui se connecte à une API externe, l'absence de mécanismes d'authentification et d'autorisation peut rendre votre site web extrêmement vulnérable aux attaques comme le DDOS et le CSRF. Cela est dû au fait que n'importe qui peut visiter le site web et l'utiliser sans passer par des vérifications de sécurité.

Votre limitation de débit et votre sécurité DDOS ne peuvent pas faire grand-chose si les requêtes semblent légitimes et proviennent de milliers (ou de millions) d'utilisateurs. Et si toutes les requêtes sont répondus, cela peut vous coûter beaucoup d'argent.

Tout comme je suis capable d'envoyer des invites à l'endpoint, des millions d'utilisateurs potentiels peuvent également le faire.

Et c'est pourquoi vous devez implémenter l'authentification et l'autorisation.

L'authentification est lorsque les utilisateurs sont vérifiés avant de pouvoir accéder à un site. L'autorisation vérifie si un utilisateur est autorisé à accéder ou à utiliser une fonctionnalité.

Pour ce travail, vous utiliserez la bibliothèque `next-auth`. Next-auth est une bibliothèque qui vous permet d'implémenter différentes formes d'authentification dans votre site Next.js.

Vous utiliserez cette bibliothèque pour configurer l'authentification OAuth GitHub. De cette manière, seuls ceux qui sont authentifiés via GitHub seront autorisés à envoyer des requêtes à votre route `api/ai`.

Tout d'abord, vous devez obtenir votre Client ID et Client Secret depuis votre tableau de bord GitHub. Sans cela, votre site ne pourra pas utiliser l'authentification GitHub.

Pour obtenir cela, vous devez créer une application OAuth GitHub (**Paramètres** > **Paramètres du développeur**), puis générer et copier l'ID client et le secret dans votre fichier `.env.local`.

Vous pouvez regarder la vidéo ci-dessous pour apprendre comment faire cela :

%[https://youtu.be/_TZUYH6hDNI] 

Dans votre fichier `.env.local`, les clés doivent être `GITHUB_CLIENT_SECRET` et `GITHUB_SECRET_ID`.

```javascript
GITHUB_CLIENT_ID=Ov23liRYdIehpA61t3Js
GITHUB_SECRET_ID=547vfbsjgfsk4859030
```

Ensuite, vous devez également créer une clé secrète qui sera utilisée par `next-auth` pour chiffrer vos jetons JWT. La valeur ne doit pas être facilement devinable. Vous pouvez utiliser la commande `openssl` (si vous l'avez installée sur votre PC) dans votre ligne de commande afin d'obtenir une valeur complexe qui ne peut pas être devinée.

```javascript
openssl rand -base64 32
```

Une fois cela fait, vous devez copier la valeur et la coller dans votre fichier `.env.local`.

Si vous n'avez pas `openssl`, vous pouvez créer une valeur aléatoire complexe et l'utiliser à la place.

```javascript
NEXTAUTH_SECRET=OtPuemlSrP8At2uZFIMrc47WBT14pifeKhziIW8
```

Ensuite, vous devez spécifier le chemin de base pour l'authentification. Il s'agit généralement de l'URL de la page d'accueil du site. Cela signifie que l'authentification et l'autorisation engloberont toutes vos routes. Puisque vous allez tester le site dans l'environnement local, vous allez utiliser `http://localhost:3000/`.

Cela signifie que vous devez avoir une autre clé (`NEXTAUTH_URL`) dans votre fichier `.env.local`.

```javascript
NEXTAUTH_URL=http://localhost:3000/
```

Une fois cela fait, vous devez créer une fonction d'assistance qui stockera les configurations pour `next-auth`.

Dans le dossier app, créez un dossier `helper` et ajoutez un fichier `authOption.ts`.

Ensuite, ajoutez ce code au fichier `app/helper/authOptions.ts` :

```javascript
import { NextAuthOptions } from "next-auth";

import GithubProvider from "next-auth/providers/github";

export const authOptions: NextAuthOptions = {
  // Configure one or more authentication providers
  providers: [
    GithubProvider({
      clientId: process.env.GITHUB_CLIENT_ID as string,
      clientSecret: process.env.GITHUB_SECRET as string,
    })
  ],
  secret: process.env.NEXTAUTH_SECRET as string,
  session: {
    strategy: 'jwt',
    maxAge: 60 * 2 //expires 2 minutes after the last request
  },
};
```

Dans le code ci-dessus, vous avez créé la configuration qui sera utilisée par `next-auth`. La configuration spécifie que l'application utilisera le fournisseur GitHub pour l'authentification. Le secret a également été ajouté à la configuration. Et enfin, vous utiliserez un jeton JWT configuré pour expirer 2 minutes après la dernière requête.

Ensuite, créez un fichier `api/auth/[nextauth]/route.ts` dans votre dossier app.

La structure du dossier devrait ressembler à ceci :

![Image montrant la structure de dossier mise à jour après la création de plus de dossiers et de fichiers](https://cdn.hashnode.com/res/hashnode/image/upload/v1724056167587/f2ab8235-2eca-4d7b-ac92-52ab9574015e.png align="center")

Ensuite, ajoutez le code ci-dessous au fichier :

```javascript
import NextAuth from "next-auth";

import {authOptions} from "@/app/helper/authOption";

const handler = NextAuth(authOptions);

export { handler as GET, handler as POST };
```

Dans le code ci-dessus, vous avez importé `NextAuth` et la fonction `authOptions` (de `app/helper/authOption`). Ensuite, vous avez utilisé cette `authOption` pour initialiser `next-auth`. Enfin, vous avez exporté le gestionnaire afin de pouvoir l'utiliser côté serveur.

Ensuite, créez un composant client qui rend la session accessible côté client. Le composant sera utilisé pour envelopper le contenu du fichier de mise en page racine (`app/layout.tsx`).

Dans votre dossier helper, créez un fichier `provider.tsx` et ajoutez ce code :

```javascript
"use client";

import {SessionProvider} from "next-auth/react";

export function Provider({children}: {children: React.ReactNode}) {
  return <SessionProvider>{children}</SessionProvider>;
}
```

Ensuite, dans votre mise en page racine (`app/layout.tsx`), importez le fournisseur de session et enveloppez-le autour de la prop children du composant `RootLayout` :

```javascript
//layout.tsx

import {Provider} from "@/app/helper/provider";

//...other code

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Provider>{children}</Provider>
      </body>
    </html>
);
}
```

Une fois que le fournisseur de session a été enveloppé autour du projet, cela signifie que vous pouvez utiliser la session côté client pour appliquer l'authentification et l'autorisation.

Dans votre fichier `app/page.tsx`, vous devez importer les fonctions `signIn`, `signOut` et `useSession` de `next-auth/react`. Cela permettra aux utilisateurs de pouvoir se connecter, se déconnecter et voir leurs informations de profil.

```javascript
import {signIn, signOut, useSession} from 'next-auth/react';
```

Ensuite, dans le composant `Home`, ajoutez ce code :

```javascript
const {data: session, status} = useSession();
console.log("status", status);
console.log("session", session);
```

Le code ci-dessus obtient la session et le statut (authentifié ou non authentifié) de l'utilisateur à partir du hook `useSession`. Ensuite, le statut et la session seront affichés dans la console du navigateur afin que le comportement puisse être observé. Lorsque vous déployez les modifications, vous pouvez supprimer le console.log.

Ensuite, remplacez le code dans l'élément d'en-tête (des lignes 92 à 94) par ceci :

```javascript
<header className="flex flex-row fixed w-[100%] top-0 left-0 p-[10px] px-[20px] text-white text-center bg-[#242424]">
    <a className='text-[15px]'>WriterAI</a>
   <div className="ml-auto flex flex-row gap-[10px]">
       { session
           ? <a>{session.user.name}</a>
           : <a onClick={() => { signIn('github') }} className="cursor-pointer">Sign in</a>
       }
       { session && <a onClick={() => { signOut() }} className="cursor-pointer">Sign out</a>}
   </div>
</header>
```

Dans le code ci-dessus, lorsque l'utilisateur clique sur le lien de connexion, il est redirigé vers GitHub pour autoriser le transfert d'informations. Et lorsque le lien de déconnexion est cliqué, la session est détruite.

De plus, si la page est chargée alors que la session est encore active, les informations de l'utilisateur et un lien de déconnexion seront affichés. Mais s'il n'y a pas de session, seul un lien de connexion sera affiché.

De plus, remplacez le code dans le conteneur de formulaire (lignes 129 à 135) afin que le formulaire soit masqué pour les utilisateurs non authentifiés et que seuls ceux qui sont authentifiés puissent envoyer des invites au serveur.

```javascript
<div className='fixed w-[100%] p-[10px] bottom-0 bg-[#242424]'>
   {/*when the form is submitted, activate a submit event that sends the value of the input and the event to the handleChat function */}
   {session 
     ? <form action='' onSubmit={(e) => handleChat(input, e)}>
        <input className=" lg:w-[50%] w-[70%] ml-[5%] lg:ml-[20%] p-[10px] outline-none bg-[#4d4d4dff] text-[15px] text-[#f2f2f2ff]" type='text' value={input} placeholder='Ask your questions' onChange={ (e) => setInput(e.target.value)}/>
        <button className='py-[10px] px-[20px] bg-black text-[15px] text-[#f2f2f2ff]'>Ask</button>
      </form>
     : <a className="block text-white text-[20px] text-center cursor-pointer" onClick={() => { signIn('github') }}>Sign in to send messages</a>
   }
</div>
```

Maintenant, si vous enregistrez les modifications et rechargez votre site, voici à quoi devrait ressembler votre site :

![Image montrant comment le projet devrait apparaître pour les utilisateurs non authentifiés](https://cdn.hashnode.com/res/hashnode/image/upload/v1724056553338/6bad6ba5-b16d-4d96-8202-2b6e71f6648f.png align="center")

Lorsque vous cliquez sur le lien de connexion, vous serez redirigé vers GitHub pour l'autorisation et redirigé vers le site après cela. Une fois l'autorisation réussie, les informations de l'utilisateur seront visibles sur le site.

Voici le mien :

![Image montrant comment le projet devrait apparaître pour les utilisateurs authentifiés](https://cdn.hashnode.com/res/hashnode/image/upload/v1724056571863/01440fb8-b2d7-4d8a-9c93-d220886361e6.png align="center")

Si vous vérifiez la console du navigateur, vous verrez les informations de la session, y compris le nom, l'e-mail et l'heure/date d'expiration. N'oubliez pas que nous avons configuré la session pour expirer 2 minutes après la dernière requête envoyée au serveur. Si vous n'envoyez aucune requête au serveur dans les 2 minutes, la session sera détruite et vous serez invité à vous connecter à nouveau.

N'oubliez pas que c'est le paramètre que j'ai ajouté dans mon fichier `helper/authOption.ts`. Vous pouvez configurer la session pour qu'elle soit active pendant des jours, des semaines ou des mois.

Il n'y a pas lieu de s'inquiéter lorsque vous envoyez une invite et recevez des messages d'erreur. Cela est dû au fait que vous avez certaines variables d'environnement dans Vercel qui n'ont pas été ajoutées au fichier `.env.local`. Lorsque vous mettrez enfin à jour les modifications, vous pourrez envoyer vos invites au site déployé comme d'habitude.

Lorsque vous cliquez également sur le lien de déconnexion, la session sera détruite, l'application sera rechargée et le formulaire sera masqué.

Si cela fonctionne comme je viens de l'expliquer, cela signifie que tout s'est bien passé.

De plus, vous devez ajouter une autorisation dans la route api/ai afin que les utilisateurs non autorisés ne puissent pas envoyer de requêtes directement à l'endpoint.

Dans votre fichier `api/ai/route.ts`, vous devez importer `getServerSession` et `authOptions`.

```javascript
import {authOptions} from "@/app/helper/authOption";

import { getServerSession} from "next-auth";
```

Ensuite, dans la fonction POST, ajoutez ce code :

```javascript
let session = await getServerSession(authOptions);

if (!session) {
  return NextResponse.json({content: 'Unauthorized access. Authentication required'}, {status: 401})
}
```

Le code ci-dessus empêche également les utilisateurs non autorisés d'obtenir des réponses de la route `api/ai` en envoyant un code de statut 401 et un message d'erreur.

Une fois cela fait, il est temps de pousser les modifications vers le dépôt GitHub.

Mais avant cela, vous devez copier les variables d'environnement (`GITHUB_CLIENT_ID`, `GITHUB_SECRET`, `NEXTAUTH_SECRET`, `NEXTAUTH_URL`) dans votre fichier `.env.local` et les coller dans la section des variables d'environnement de la page des paramètres de votre projet sur Vercel.

Après cela, exécutez le code ci-dessous pour pousser les modifications vers GitHub :

```javascript
git add .

git commit -m "added GitHub authentication and authorization"

git push -u origin main
```

Après la mise à jour réussie, visitez la page de déploiement de votre projet sur Vercel pour confirmer que les modifications GitHub ont été déployées avec succès.

Mais malheureusement, une erreur que nous n'avons pas remarquée fera échouer le déploiement.

Voici le message d'erreur :

![Image montrant l'erreur de déploiement qui sera visible sur Vercel](https://cdn.hashnode.com/res/hashnode/image/upload/v1724056626098/46178ff9-1f7a-41e6-a056-41fc04e91cc0.png align="center")

Puisque je ne savais pas non plus ce qui n'allait pas, j'ai demandé de l'aide à ChatGPT. Et j'ai pu trouver le problème.

Le déploiement a échoué parce que nous n'avons pas vérifié que `session.user` était défini avant d'y accéder.

![Image montrant les messages de ChatGPT](https://cdn.hashnode.com/res/hashnode/image/upload/v1724056744333/e512a378-a3d9-4a00-bf21-c425bd1f5848.png align="center")

Donc dans votre fichier `page.tsx`, assurez-vous de corriger le code comme indiqué ci-dessous :

```javascript
{ session && session.user
    ? <a>{session.user.name}</a>
     : <a onClick={() => { signIn('github') }} className="cursor-pointer">Sign in</a>
}
```

Après cela, poussez les modifications vers GitHub et attendez que le projet soit déployé avec succès sur Vercel.

Maintenant, vous pouvez visiter le lien déployé pour commencer à tester l'authentification.

Mais lorsque vous cliquez sur le lien de connexion, la page ne se charge pas. Cela est dû au fait que vous n'avez pas changé l'URL dans votre variable d'environnement et GitHub de `http://localhost:3000` au domaine de votre projet déployé.

Vous devez donc vérifier les informations de déploiement de votre projet sur Vercel et copier le nom de domaine.

Ensuite, allez dans les paramètres de vos variables d'environnement et mettez à jour l'`NEXTAUTH_URL` avec le nom de domaine du projet. Le mien est `https://nextjs-ai-pro.vercel.app`.

Ensuite, allez dans l'application OAuth que vous avez créée, remplacez le nom de domaine dans l'URL de la page d'accueil et l'URL de rappel de `http://localhost:3000`/ par le nom de domaine Vercel.

N'oubliez pas que si vous avez votre propre nom de domaine (par exemple, domain.com), il sera utilisé à la place du nom de domaine Vercel.

Si vous rechargez le site et cliquez sur le lien de connexion, vous serez redirigé vers GitHub et votre session sera créée. Lorsque vous vous déconnectez, la session sera également détruite.

Lorsque vous essayez également d'exécuter le script ci-dessous dans la console de votre navigateur, vous obtiendrez un message d'erreur car vous ne vous êtes pas connecté.

```javascript
//fonction pour envoyer la requête
const getCompletion = async (prompt) => {

  try {
    const response = await fetch('/api/ai', {
      method: 'POST',
      body: JSON.stringify({ prompt }),
      headers: {
        'Content-Type': 'application/json',
      },
  });

  const result = await response.json();

  if (!response.ok) {
    return { role: 'assistant', content: result.content };
  }

  return result;

  } catch (error) {
    return { role: 'assistant', content: 'Something went wrong' };
  }
};

getCompletion().then( (result) => {
    console.log(result)
})
```

Cela signifie que les utilisateurs non autorisés ne pourront pas exécuter de script dans vos outils de développement pour obtenir une réponse IA.

Vous pouvez également tester le site et envoyer quelques invites.

Si tout fonctionne comme expliqué, cela signifie que l'authentification et l'autorisation ont été implémentées avec succès. Félicitations !

Vous pouvez regarder la vidéo pour cette section ci-dessous :

%[https://youtu.be/YhXuTtHkY3A] 

## **Optimisation du code**

Maintenant, la plupart du travail est terminé. Mais vous pouvez faire d'autres choses pour optimiser davantage votre code. Cela dépend entièrement de la manière dont vous souhaitez qu'il soit.

Par exemple, vous pouvez refactoriser le code, améliorer le style, augmenter le délai d'expiration des fonctions pour les invites plus longues, optimiser les journaux, gérer les erreurs dans le middleware, configurer des tests unitaires et d'intégration, configurer un pipeline CI/CD, mettre à jour les métadonnées de votre projet (titre, description, logo), créer un environnement de prévisualisation pour vos déploiements, rediriger les connexions infructueuses vers une page de destination et ajouter de nombreuses autres fonctionnalités à votre application.

## **Conclusion**

Dans ce tutoriel, nous avons exploré beaucoup de choses. Vous avez appris à intégrer votre application Next.js avec des API tierces. Vous avez également appris à sécuriser votre application contre les cyberattaques les plus courantes en mettant en œuvre des stratégies comme la limitation de débit, la configuration de pare-feu et la mise en œuvre de l'authentification et de l'autorisation sur votre application IA déployée sur Vercel.

En appliquant la même logique dans votre application Next.js IA, je suis convaincu que vous serez en mesure de déployer votre application en toute sécurité sans craindre de vous réveiller avec une facture astronomique ou des plantages de serveur.

Pour être du bon côté, assurez-vous de surveiller votre déploiement Vercel quotidiennement. Vous pouvez également engager un ingénieur logiciel professionnel pour vérifier la sécurité de votre application si vous ne vous sentez pas confiant dans vos compétences dans ce domaine.