---
title: Comment construire un outil de paraphrase avec ReactJs et ChatGPT Turbo
subtitle: ''
author: Idris Olubisi
co_authors: []
series: null
date: '2023-03-31T17:51:04.000Z'
originalURL: https://freecodecamp.org/news/build-a-paraphrasing-tool-with-reactjs-chatgpt-turbo
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/paraphrase.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: React
  slug: react
seo_title: Comment construire un outil de paraphrase avec ReactJs et ChatGPT Turbo
seo_desc: "In a world where online content is growing exponentially, it's more important\
  \ than ever to produce unique content that stands out.\nParaphrasing tools can offer\
  \ a quick solution to help you develop unique ideas and create original content.\
  \ \nWith the h..."
---

Dans un monde où le contenu en ligne croît de manière exponentielle, il est plus important que jamais de produire un contenu unique qui se démarque.

Les outils de paraphrase peuvent offrir une solution rapide pour vous aider à développer des idées uniques et à créer du contenu original.

Avec l'aide de ReactJs et de ChatGPT Turbo, les développeurs peuvent construire un outil de paraphrase puissant et efficace qui fournit des résultats précis et efficaces.

Avec l'IA, vous pouvez automatiser les tâches répétitives, tester le code plus efficacement et améliorer la qualité globale de votre logiciel. Récemment, nous avons vu un grand nombre de développeurs poser des questions comme "Comment créer un chatbot dans Reactjs ?", "Comment utiliser l'API ChatGPT dans React ?", et "ChatGPT peut-il écrire du code JavaScript ?".

Cet article nous apprendra à construire un outil de paraphrase en utilisant ReactJs, ChatGPT Turbo et TailwindCSS pour le style.

## Introduction à ChatGPT Turbo

[ChatGPT Turbo](https://openai.com/blog/introducing-chatgpt-and-whisper-apis) est une fonctionnalité récemment introduite par [OpenAI](https://openai.com/) pour les abonnés ChatGPT Plus, qui vise à fournir des réponses supérieures à un rythme accéléré.

Le mode Turbo est actuellement en phase alpha, mais nous utiliserons le mode `gpt-3.5-turbo` dans ce tutoriel. Le mode Turbo est conçu pour fournir des réponses de haute qualité. Il s'agit d'une version avancée du mode par défaut de ChatGPT, nécessitant des ressources computationnelles minimales pour les applications en temps réel.

## Prérequis

* Assurez-vous d'avoir Node.js et npm installés sur votre ordinateur. Si ce n'est pas le cas, vous pouvez aller [**ici**](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

Vous pouvez vérifier que vous avez Node.js installé en utilisant la commande suivante dans le terminal :

```bash
node -v && npm -v
```

* Installez et configurez Git sur votre PC. Si vous ne l'avez pas, allez [ici](https://git-scm.com/) pour l'installer.

* Vous devriez avoir une compréhension de base de JavaScript/TypeScript

## Installation et configuration du projet

Pour commencer rapidement avec la configuration et l'installation du projet, clonez ce [**projet sur GitHub**](https://github.com/Olanetsoft/ai-paraphrasing-tool-with-nextjs/tree/starter). Assurez-vous d'être sur la branche `starter` en utilisant la commande suivante :

```bash
git clone https://github.com/Olanetsoft/ai-paraphrasing-tool-with-nextjs.git
```

Ensuite, lancez le projet localement après l'avoir cloné en utilisant la commande suivante dans votre terminal.

Voici comment vous pouvez installer le projet en utilisant `npm` :

```solidity
cd ai-paraphrasing-tool-with-nextjs && npm i && npm start
```

## Comment concevoir la mise en page pour l'outil de paraphrase

À l'étape précédente, vous avez cloné et installé le projet de démarrage que nous utiliserons dans cet article. Il contient la mise en page par défaut pour le projet que nous construirons dans ce tutoriel.

Accédez à [http://localhost:3000/](http://localhost:3000/) dans le navigateur. Voici ce que vous devriez avoir après avoir cloné et installé le projet :

![Outil de paraphrase avec ReactJs et ChatGPT Turbo](https://cdn.hashnode.com/res/hashnode/image/upload/v1679840553951/b45632bc-0bd5-4e6c-a59b-229a88e5da9d.png)

Accédez au répertoire du projet et renommez le `.env.example` en `env`. Ou vous pouvez créer un nouveau fichier `.env` avec la commande suivante dans le répertoire racine du projet.

```bash
touch .env
```

Mettez à jour le `.env` avec ce qui suit :

```bash
NEXT_PUBLIC_ENV_VARIABLE_OPEN_AI_API_KEY=<Votre-Clé-API>
```

Remplacez `<Votre-Clé-API>` par votre clé `API` d'OpenAI. Visitez le [site web d'OpenAI](https://platform.openai.com/), créez un compte gratuitement et générez une clé API.

Vous devriez avoir quelque chose de similaire à ce qui est montré ci-dessous pour implémenter la fonctionnalité de paraphrase dans votre application avec ChapGPT Turbo.

![Répertoire du projet Outil de paraphrase avec ReactJs et ChatGPT Turbo](https://cdn.hashnode.com/res/hashnode/image/upload/v1679841350457/3e0ee4ad-64d7-4503-84a9-6a90fe9c02c3.png)

## Comment intégrer ChatGPT Turbo

Dans cette section, vous allez intégrer ChatGPT Turbo et implémenter la fonctionnalité de paraphrase.

Pour commencer, naviguez vers le fichier `paraphrase.ts` sous le répertoire `api` et ajoutez le snippet suivant :

```typescript
// Importer les types nécessaires de Next.js
import type { NextApiRequest, NextApiResponse } from "next";

// Vérifier si la variable d'environnement requise est définie
if (!process.env.NEXT_PUBLIC_ENV_VARIABLE_OPEN_AI_API_KEY) {
  throw new Error("Variable d'environnement manquante d'OpenAI");
}

// Définir le type ChatGPTAgent comme une union de user et system
export type ChatGPTAgent = "user" | "system";

// Définir l'interface ChatGPTMessage
interface ChatGPTMessage {
  role: ChatGPTAgent;
  content: string;
}

// Définir l'interface promptPayload
interface promptPayload {
  model: string;
  messages: ChatGPTMessage[];
  temperature: number;
  max_tokens: number;
}

// Définir la fonction de gestionnaire asynchrone
const handler = async (req: NextApiRequest, res: NextApiResponse) => {
  try {
    // Obtenir le prompt du corps de la requête
    const prompt = req.body.prompt;

    // Valider le prompt
    if (!prompt) {
      return new Response("Aucun prompt dans la requête", { status: 400 });
    }

    // Définir l'objet payload à envoyer à l'API OpenAI
    const payload: promptPayload = {
      model: "gpt-3.5-turbo",
      messages: [{ role: "user", content: prompt }],
      temperature: 1,
      max_tokens: 500,
    };

    // Envoyer la requête à l'API OpenAI et attendre la réponse
    const response = await fetch("https://api.openai.com/v1/chat/completions", {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${
          process.env.NEXT_PUBLIC_ENV_VARIABLE_OPEN_AI_API_KEY ?? ""
        }`,
      },
      method: "POST",
      body: JSON.stringify(payload),
    });

    // Analyser la réponse JSON et la renvoyer dans la réponse
    const data = await response.json();
    return res.json(data);
  } catch (error) {
    // Journaliser les erreurs qui se produisent pendant la requête
    console.log("L'erreur : ", error);
  }
};

// Exporter la fonction de gestionnaire comme exportation par défaut
export default handler;
```

Passons en revue ce qui se passe dans l'extrait de code ci-dessus :

* Importer les types `NextApiRequest` et `NextApiResponse` de Next.js.

* Vérifier si `NEXT_PUBLIC_ENV_VARIABLE_OPEN_AI_API_KEY`, une variable d'environnement, est définie et lancer une erreur si ce n'est pas le cas.

* Définir un type et deux interfaces pour les agents et messages ChatGPT - `ChatGPTAgent` et `ChatGPTMessage`, respectivement.

* Définir une interface pour le payload de la requête à l'API OpenAI et une fonction de gestionnaire asynchrone qui prend une requête et une réponse Next.js comme arguments.

* Obtenir un prompt du corps de la requête et le valider.

* Envoyer une requête à l'`API OpenAI` avec le prompt et d'autres paramètres dans le payload de la requête.

* Analyser et retourner la réponse JSON de l'API OpenAI.

Ensuite, nous allons consommer le nouveau endpoint que nous venons d'implémenter. Naviguez vers le fichier `index.vue` dans le répertoire des pages, et mettez-le à jour avec le snippet de code suivant :

```typescript
//...

// Définir une fonction de composant par défaut appelée Home
export default function Home() {

  // Définir trois variables d'état pour le texte original, le texte paraphrasé et le mode de paraphrase
  const [originalText, setOriginalText] = useState<string>("");
  const [paraphrasedText, setParaphrasedText] = useState<string>("");
  const [paraphraseMode, setParaphraseMode] = useState<string>("Standard");

  // Définir une référence pour l'élément de zone de texte
  const textAreaRef = useRef(null);

  // Définir une variable d'état pour l'état de chargement de l'opération de paraphrase
  const [loading, setLoading] = useState<boolean>(false);

  // Construire une chaîne de prompt basée sur le texte original et le mode de paraphrase
  const prompt = `Paraphrase "${originalText}" en utilisant le mode ${paraphraseMode}. Ne pas ajouter de mot supplémentaire.`;

  // Définir une fonction asynchrone pour gérer l'opération de paraphrase
  const handleParaphrase = async (e: React.FormEvent) => {
    // Empêcher la soumission du formulaire si le texte original est vide
    if (!originalText) {
      toast.error("Entrez le texte à paraphraser !");
      return;
    }

    // Définir l'état de chargement et réinitialiser le texte paraphrasé
    setLoading(true);

    // Envoyer une requête POST à l'endpoint API "/api/paraphrase" avec le prompt dans le corps de la requête
    const response = await fetch("/api/paraphrase", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        prompt,
      }),
    });

    // Analyser la réponse en JSON
    const data = await response.json();

    // Définir le texte paraphrasé sur le contenu du message du premier choix dans la réponse
    setParaphrasedText(data.choices[0].message.content);

    // Réinitialiser l'état de chargement
    setLoading(false);
  };

  // Retourner le JSX pour le composant Home
  return (
    <>
    {/* //... */}
    </>
  );
}
```

Dans l'extrait de code ci-dessus :

* Initialiser trois variables d'état en utilisant le hook `useState` : `originalText`, `paraphrasedText`, et `paraphraseMode`.

* Initialiser une référence à un élément `textarea` en utilisant le hook `useRef` et une variable d'état de chargement.

* Définir `handleParaphrase`, une fonction qui envoie une requête `POST` à `/api/paraphrase` avec un prompt pour paraphraser le texte dans la variable d'état `originalText` en utilisant le `paraphraseMode` sélectionné.

Le composant retourne une UI avec un élément `textarea` pour saisir le texte à paraphraser, un élément `select` pour choisir le mode de paraphrase, un bouton `button` pour initier le processus de paraphrase, et un élément `div` pour afficher le texte paraphrasé.

Mettez à jour le bouton `Paraphrase` avec le snippet de code suivant pour ajouter l'événement `onClick` :

```typescript
  <button
     onClick={handleParaphrase}
     //...
     >
       Paraphrase
 </button>
```

Testons notre application. Vous devriez avoir quelque chose de similaire à ce que vous voyez ci-dessous :

![praraphrase](https://www.freecodecamp.org/news/content/images/2023/03/praraphrase.gif)

Vous pouvez trouver le code complet dans ce dépôt GitHub [**ici**](https://github.com/Olanetsoft/ai-paraphrasing-tool-with-nextjs).

## Conclusion

Cet article fournit un guide étape par étape sur la façon de construire un outil de paraphrase en utilisant ReactJs, ChatGPT Turbo et TailwindCSS pour styliser l'application.

J'adorerais me connecter avec vous via [**Twitter**](https://twitter.com/olanetsoft) | [**LinkedIn**](https://www.linkedin.com/in/olubisi-idris-ayinde-05727b17a/) | [**GitHub**](https://github.com/Olanetsoft) | [**Portfolio**](https://idrisolubisi.com/)

À bientôt dans mon prochain article de blog. Prenez soin de vous !