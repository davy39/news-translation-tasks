---
title: Comment créer un bot Discord alimenté par LangGraph et Composio
subtitle: ''
author: Shrijal Acharya
co_authors: []
series: null
date: '2025-06-24T21:03:03.788Z'
originalURL: https://freecodecamp.org/news/build-a-langgraph-composio-powered-discord-bot
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1750798930964/65dd7078-e4e7-42d0-a797-1e7d72690513.png
tags:
- name: AI
  slug: ai
- name: agentic AI
  slug: agentic-ai
- name: langgraph
  slug: langgraph
- name: bot
  slug: bot
seo_title: Comment créer un bot Discord alimenté par LangGraph et Composio
seo_desc: 'With the rise of AI tools over the past couple years, most of us are learning
  how to use them in our projects. And in this article, I’ll teach you how to build
  a quick Discord bot with LangGraph and Composio.

  You’ll use LangGraph nodes to build a bra...'
---

Avec l'essor des outils d'IA au cours des dernières années, la plupart d'entre nous apprenons à les utiliser dans nos projets. Et dans cet article, je vais vous apprendre à créer rapidement un bot Discord avec LangGraph et Composio.

Vous utiliserez les nœuds LangGraph pour créer un flux de branchement qui traite les messages entrants et détecte l'intention comme le chat, le support ou l'utilisation d'outils. Il les acheminera ensuite vers la logique appropriée en fonction de ce que dit l'utilisateur.

Je sais que cela peut sembler un peu étrange d'utiliser LangGraph pour un bot Discord, mais vous verrez bientôt que ce projet est une manière assez amusante de visualiser comment les flux de travail d'IA basés sur des nœuds fonctionnent réellement.

Pour l'instant, le flux de travail est simple : vous déterminerez si l'utilisateur discute simplement, pose une question de support ou demande au bot d'effectuer une action, et vous répondrez en conséquence.

**Ce que vous allez apprendre :** 👀

* Comment utiliser LangGraph pour créer un flux de travail piloté par l'IA qui alimente la logique de votre bot.

* Comment vous pouvez intégrer Composio pour permettre à votre bot d'effectuer des actions réelles en utilisant des outils externes.

* Comment vous pouvez utiliser Discord.js et gérer différents types de messages comme les réponses, les fils de discussion et les embeds.

* Comment vous pouvez maintenir un contexte par canal en utilisant l'historique des messages et le transmettre à l'IA.

À la fin de cet article, vous aurez un bot Discord assez décent et fonctionnel que vous pourrez ajouter à votre serveur. Il répond aux utilisateurs en fonction du contexte des messages et dispose même d'une assistance pour les appels d'outils ! (Et il y a un petit défi pour vous afin d'implémenter quelque chose vous-même.) 😉

## Prérequis

Assurez-vous d'avoir Discord installé sur votre machine afin de pouvoir tester facilement le bot.

Ce projet est conçu pour démontrer comment vous pouvez créer un bot alimenté par LangGraph et Composio. Avant de continuer, il est utile d'avoir une compréhension de base de :

* Comment travailler avec Node.js

* Une idée approximative de ce qu'est LangGraph et de son fonctionnement

* Comment travailler avec Discord.js

* Ce que sont les agents IA

Si vous n'êtes pas sûr de l'un de ces points, essayez de suivre quand même. Vous pourriez très bien comprendre les choses. Et si cela devient confus, vous pouvez toujours consulter le code source complet [ici](https://github.com/shricodev/discord-bot-langgraph-composio).

## Table des matières

* [Comment configurer l'environnement](#heading-installation)

  * [Initialiser le projet](#heading-initialiser-le-projet)

  * [Installer les dépendances](#heading-installer-les-dependances)

  * [Configurer Composio](#heading-configurer-composio)

  * [Configurer l'intégration Discord](#heading-configurer-lintegration-discord)

  * [Ajouter les variables d'environnement](#heading-ajouter-les-variables-denvironnement)

* [Construire la logique de l'application](#heading-construire-la-logique-de-lapplication)

  * [Définir les types et les helpers utilitaires](#heading-definir-les-types-et-les-helpers-utilitaires)

  * [Implémenter le flux de travail LangGraph](#heading-implementer-le-flux-de-travail-langgraph)

  * [Configurer le client Discord.js](#heading-configurer-le-client-discordjs)

* [Conclusion](#heading-conclusion)

## Comment configurer l'environnement

Dans cette section, nous allons tout configurer pour construire le projet.

### Initialiser le projet

Initialisez une application Node.js avec la commande suivante :

💁 Ici, j'utilise Bun, mais vous pouvez choisir n'importe quel gestionnaire de paquets de votre choix.

```bash
mkdir discord-bot-langgraph && cd discord-bot-langgraph \
&& bun init -y
```

Maintenant que notre application Node.js est prête, installons quelques dépendances.

### Installer les dépendances

Nous allons utiliser les principaux packages suivants et quelques autres packages d'assistance :

* [discord.js](https://discord.js.org) : Interagit avec l'API Discord

* [composio](https://composio.dev) : Ajoute la prise en charge de l'intégration des outils au bot

* [openai](https://platform.openai.com) : Permet des réponses alimentées par l'IA

* [langchain](https://www.langchain.com) : Gère les flux de travail LLM

* [zod](https://zod.dev) : Valide et analyse les données en toute sécurité

```bash
bun add discord.js openai @langchain/core @langchain/langgraph \
langchain composio-core dotenv zod uuid
```

### Configurer Composio

💁 Vous utiliserez Composio pour ajouter des intégrations à votre application. Vous pouvez choisir l'intégration de votre choix, mais ici j'utilise Google Sheets.

Tout d'abord, avant de continuer, vous devez obtenir un accès à une clé API Composio.

Allez-y et créez un compte sur Composio, obtenez votre clé API et collez-la dans le fichier `.env` à la racine du projet :

![Tableau de bord Composio](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lkr1pys0txedp9vam4tt.png align="left")

```ini
COMPOSIO_API_KEY=<votre_clé_api_composio>
```

Authentifiez-vous avec la commande suivante :

```bash
composio login
```

Une fois cela fait, exécutez la commande `composio whoami`, et si vous voyez quelque chose comme ci-dessous, vous êtes connecté avec succès.

![Résultat de la commande `composio whoami`](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ifzbkw6u6bwnj68lwqxt.png align="left")

Vous y êtes presque : maintenant, vous devez simplement configurer les intégrations. Ici, j'utiliserai Google Sheets, mais encore une fois, vous pouvez configurer n'importe quelle intégration que vous souhaitez.

Exécutez la commande suivante pour configurer l'intégration Google Sheets :

```bash
composio add googlesheets
```

Vous devriez voir un résultat similaire à ceci :

![Ajouter l'intégration Google Sheets de Composio](https://cdn.hashnode.com/res/hashnode/image/upload/v1750336813743/9079ef2b-dc2a-4b10-b001-50e4cf98f3c5.png align="center")

Rendez-vous à l'URL qui est affichée, et vous devriez être authentifié comme suit :

![Succès de l'authentification Composio](https://cdn.hashnode.com/res/hashnode/image/upload/v1750325571006/b0864445-7471-471f-88eb-f2ec8d832b39.png align="center")

C'est tout. Vous avez ajouté avec succès l'intégration Google Sheets et pouvez accéder à tous ses outils dans votre application.

Une fois terminé, exécutez la commande `composio integrations` pour vérifier si cela a fonctionné. Vous devriez voir une liste de toutes vos intégrations :

![Liste des intégrations Composio](https://cdn.hashnode.com/res/hashnode/image/upload/v1750325653419/4585b63a-5581-4102-92e4-a55dca018063.png align="center")

### Configurer l'intégration Discord

Cela est un peu hors sujet pour ce tutoriel, mais en gros, vous allez créer une application/bot sur Discord et l'ajouter à votre serveur.

Vous pouvez trouver un guide sur la façon de créer et d'ajouter un bot à votre serveur dans la [documentation Discord.js](https://discordjs.guide/preparations/adding-your-bot-to-servers.html#bot-invite-links).

Et oui, c'est gratuit si vous vous demandez si une étape ici nécessite un compte pro ou autre chose. 😉

Assurez-vous de remplir ces trois variables d'environnement :

```ini
DISCORD_BOT_TOKEN=<VOTRE_TOKEN_DISCORD_BOT>
DISCORD_BOT_GUILD_ID=<VOTRE_ID_GUILD_DISCORD_BOT>
DISCORD_BOT_CHANNEL_ID=<VOTRE_ID_CHAINE_DISCORD_BOT>
```

### Ajouter les variables d'environnement

Vous aurez besoin de quelques autres variables d'environnement, y compris la clé API OpenAI, pour que le bot fonctionne.

Votre fichier `.env` final devrait ressembler à ceci :

```ini
OPENAI_API_KEY=<VOTRE_CLÉ_API_OPENAI>

COMPOSIO_API_KEY=<VOTRE_CLÉ_API_COMPOSIO>

DISCORD_BOT_TOKEN=<VOTRE_TOKEN_DISCORD_BOT>
DISCORD_BOT_GUILD_ID=<VOTRE_ID_GUILD_DISCORD_BOT>
DISCORD_BOT_CHANNEL_ID=<VOTRE_ID_CHAINE_DISCORD_BOT>
```

## Construire la logique de l'application

Maintenant que vous avez posé toutes les bases, vous pouvez enfin commencer à coder le projet.

### Définir les types et les helpers utilitaires

Commençons par écrire quelques fonctions d'assistance et définir les types de données avec lesquels vous allez travailler.

Il est important dans toute application, surtout dans celles comme celle que nous construisons - qui est sujette aux erreurs en raison de multiples appels API - que nous configurions une journalisation décente afin de savoir quand et comment les choses tournent mal.

Créez un nouveau fichier nommé `logger.ts` à l'intérieur du répertoire `utils` et ajoutez les lignes de code suivantes :

```typescript
// 👇 discord-bot-langgraph/utils/logger.ts

export const DEBUG = "DEBUG";
export const INFO = "INFO";
export const WARN = "WARN";
export const ERROR = "ERROR";

export type LogLevel = typeof DEBUG | typeof INFO | typeof WARN | typeof ERROR;

// eslint-disable-next-line  @typescript-eslint/no-explicit-any
export function log(level: LogLevel, message: string, ...data: any[]) {
  const timestamp = new Date().toLocaleString();
  const prefix = `[${timestamp}] [${level}]`;

  switch (level) {
    case ERROR:
      console.error(prefix, message, ...data);
      break;
    case WARN:
      console.warn(prefix, message, ...data);
      break;
    default:
      console.log(prefix, message, ...data);
  }
}
```

Cela commence déjà à bien se présenter. Pourquoi ne pas écrire un petit validateur de variables d'environnement ? Exécutez cela lors du démarrage initial du programme, et si quelque chose ne va pas, l'application quittera avec des logs clairs afin que les utilisateurs sachent si des variables d'environnement sont manquantes.

Créez un nouveau fichier nommé `env-validator.ts` dans le répertoire `utils` et ajoutez les lignes de code suivantes :

```typescript
// 👇 discord-bot-langgraph/utils/env-validator.ts

import { log, ERROR } from "./logger.js";

export const OPENAI_API_KEY = "OPENAI_API_KEY";

export const DISCORD_BOT_TOKEN = "DISCORD_BOT_TOKEN";
export const DISCORD_BOT_GUILD_ID = "DISCORD_BOT_GUILD_ID";
export const DISCORD_BOT_CLIENT_ID = "DISCORD_BOT_CLIENT_ID";

export const COMPOSIO_API_KEY = "COMPOSIO_API_KEY";

export const validateEnvVars = (requiredEnvVars: string[]): void => {
  const missingVars: string[] = [];

  for (const envVar of requiredEnvVars) {
    if (!process.env[envVar]) {
      missingVars.push(envVar);
    }
  }

  if (missingVars.length > 0) {
    log(
      ERROR,
      "variables d'environnement requises manquantes. veuillez créer un fichier .env et ajouter les éléments suivants :",
    );
    missingVars.forEach((envVar) => console.error(`- ${envVar}`));
    process.exit(1);
  }
};
```

Maintenant, définissons également le type de données avec lesquelles vous allez travailler :

Créez un nouveau fichier nommé `types.ts` à l'intérieur du répertoire `types` et ajoutez les lignes de code suivantes :

```typescript
// 👇 discord-bot-langgraph/types/types.ts

export const QUESTION = "QUESTION";
export const HELP = "HELP";
export const SUPPORT = "SUPPORT";
export const OTHER = "OTHER";
export const TOOL_CALL_REQUEST = "TOOL_CALL_REQUEST";

export type FinalAction =
  | { type: "REPLY"; content: string }
  | { type: "REPLY_IN_THREAD"; content: string }
  | {
      type: "CREATE_EMBED";
      title: string;
      description: string;
      roleToPing?: string;
    };

export type MessageChoice =
  | typeof SUPPORT
  | typeof OTHER
  | typeof TOOL_CALL_REQUEST;

export type SupportTicketType = typeof QUESTION | typeof HELP;

export type Message = {
  author: string;
  content: string;
};

export type SupportTicketQuestion = {
  description: string;
  answer: string;
};

export type SupportTicket = {
  type?: SupportTicketType;
  question?: SupportTicketQuestion;
};

export type ToolCallRequestAction = {
  // actionLog n'est pas destiné à être montré à l'utilisateur final.
  // Ceci est uniquement à des fins de journalisation.
  actionLog: string;
  status: "success" | "failed" | "acknowledged";
};
```

Les types sont assez explicites, mais voici un bref aperçu.

`Message` contient l'entrée de l'utilisateur et l'auteur. Chaque message peut être marqué comme support, une demande d'appel d'outil, ou simplement autre, comme du spam ou une conversation anodine.

Les messages de support sont également étiquetés comme aide ou question en utilisant `SupportTicketType`.

Le graphique retourne une `FinalAction`, qui peut être une réponse directe, une réponse dans un fil de discussion, ou un embed. Si c'est `CREATE_EMBED` et que `roleToPing` est défini, cela indique une aide de support, donc nous pouvons mentionner le modérateur.

Pour les réponses basées sur des outils, `ToolCallRequestAction` stocke le statut et un journal interne utilisé pour le débogage.

Maintenant, vous avez besoin d'une dernière fonction d'assistance à utiliser dans vos nœuds pour extraire la réponse du LLM. Créez un nouveau fichier nommé `helpers.ts` et ajoutez le code suivant :

```typescript
// 👇 discord-bot-langgraph/utils/helpers.ts

import type { AIMessage } from "@langchain/core/messages";

export function extractStringFromAIMessage(
  message: AIMessage,
  fallback: string = "Aucune réponse valide générée par le LLM.",
): string {
  if (typeof message.content === "string") {
    return message.content;
  }

  if (Array.isArray(message.content)) {
    const textContent = message.content
      .map((item) => (typeof item === "string" ? item : ""))
      .join(" ");
    return textContent.trim() || fallback;
  }

  return fallback;
}
```

Vous êtes prêt pour l'instant avec ces fonctions d'assistance en place. Maintenant, vous pouvez commencer à coder la logique.

### Implémenter le flux de travail LangGraph

Maintenant que vous avez défini les types, structurez votre graphique et connectez-le avec quelques arêtes.

Créez un nouveau fichier nommé `graph.ts` à l'intérieur du répertoire `src` et ajoutez les lignes de code suivantes :

```typescript
// 👇 discord-bot-langgraph/src/graph.ts

import { Annotation, END, START, StateGraph } from "@langchain/langgraph";
import {
  type FinalAction,
  type ToolCallRequestAction,
  type Message,
  type MessageChoice,
  type SupportTicket,
} from "../types/types.js";
import {
  processToolCall,
  processMessage,
  processOther,
  processSupport,
  processSupportHelp,
  processSupportQuestion,
} from "./nodes.js";
import { processMessageEdges, processSupportEdges } from "./edges.js";

const state = Annotation.Root({
  message: Annotation<Message>(),
  previousMessages: Annotation<Message[]>(),
  messageChoice: Annotation<MessageChoice>(),
  supportTicket: Annotation<SupportTicket>(),
  toolCallRequest: Annotation<ToolCallRequestAction>(),
  finalAction: Annotation<FinalAction>(),
});

export type State = typeof state.State;
export type Update = typeof state.Update;

export function initializeGraph() {
  const workflow = new StateGraph(state);

  workflow
    .addNode("process-message", processMessage)
    .addNode("process-support", processSupport)
    .addNode("process-other", processOther)

    .addNode("process-support-question", processSupportQuestion)
    .addNode("process-support-help", processSupportHelp)
    .addNode("process-tool-call", processToolCall)

    // Configuration des arêtes commence ici....
    .addEdge(START, "process-message")

    .addConditionalEdges("process-message", processMessageEdges)
    .addConditionalEdges("process-support", processSupportEdges)

    .addEdge("process-other", END)
    .addEdge("process-support-question", END)
    .addEdge("process-support-help", END)
    .addEdge("process-tool-call", END);

  const graph = workflow.compile();

  // Pour obtenir le graphique en png
  // getGraph() est déprécié cependant
  // Bun.write("graph/graph.png", await graph.getGraph().drawMermaidPng());

  return graph;
}
```

La fonction `initializeGraph`, comme son nom l'indique, retourne le graphique que vous pouvez utiliser pour exécuter le flux de travail.

Le nœud `process-message` est le point de départ du graphique. Il prend le message de l'utilisateur, le traite et le route vers le nœud suivant approprié : `process-support`, `process-tool-call` ou `process-other`.

Le nœud `process-support` classe davantage le message de support et décide s'il doit aller à `process-support-help` ou `process-support-question`.

Le nœud `process-tool-call` gère les messages lorsque l'utilisateur essaie de déclencher un outil ou une action.

Le nœud `process-other` gère tout ce qui ne relève pas des catégories de support ou d'appel d'outil. Ce sont des réponses générales ou de secours.

Pour vous aider à visualiser comment les choses vont se structurer, voici à quoi ressemble le graphique avec tous les différents nœuds (à travailler !) :

![Nœuds LangGraph pour le flux de travail du bot Discord](https://cdn.hashnode.com/res/hashnode/image/upload/v1750327093884/fa8e6b4e-ca61-4900-9b3b-7b3a2863c296.png align="center")

Pour tout connecter, vous devez définir des arêtes entre les nœuds, y compris des arêtes conditionnelles qui décident dynamiquement de l'étape suivante en fonction de l'état.

Créez un nouveau fichier nommé `edges.ts` à l'intérieur du répertoire `src` et ajoutez les lignes de code suivantes :

```typescript
// 👇 discord-bot-langgraph/src/edges.ts

import { END } from "@langchain/langgraph";
import { type State } from "./graph.js";
import { QUESTION, OTHER, SUPPORT, TOOL_CALL_REQUEST } from "../types/types.js";
import { log, WARN } from "../utils/logger.js";

export const processMessageEdges = (
  state: State,
): "process-support" | "process-other" | "process-tool-call" | "__end__" => {
  if (!state.messageChoice) {
    log(WARN, "state.messageChoice est indéfini. Retour...");
    return END;
  }

  switch (state.messageChoice) {
    case SUPPORT:
      return "process-support";
    case TOOL_CALL_REQUEST:
      return "process-tool-call";
    case OTHER:
      return "process-other";
    default:
      log(WARN, "choix de message inconnu. Retour...");
      return END;
  }
};

export const processSupportEdges = (
  state: State,
): "process-support-question" | "process-support-help" | "__end__" => {
  if (!state.supportTicket?.type) {
    log(WARN, "state.supportTicket.type est indéfini. Retour...");
    return END;
  }

  return state.supportTicket.type === QUESTION
    ? "process-support-question"
    : "process-support-help";
};
```

Ce sont les arêtes qui connectent différents nœuds dans votre application. Elles dirigent le flux dans votre graphique.

Les choses se mettent vraiment en place - alors terminons la logique principale en implémentant tous les nœuds pour votre application.

Créez un nouveau fichier nommé `nodes.ts` à l'intérieur du répertoire `src` et ajoutez les lignes de code suivantes :

```typescript
// 👇 discord-bot-langgraph/src/nodes.ts

import { type State, type Update } from "./graph.js";
import { ChatOpenAI } from "@langchain/openai";
import { z } from "zod";
import {
  HELP,
  TOOL_CALL_REQUEST,
  OTHER,
  QUESTION,
  SUPPORT,
} from "../types/types.js";
import { extractStringFromAIMessage } from "../utils/helpers.js";
import { OpenAIToolSet } from "composio-core";
import type { ChatCompletionMessageToolCall } from "openai/resources/chat/completions.mjs";
import { v4 as uuidv4 } from "uuid";
import { DEBUG, ERROR, INFO, log, WARN } from "../utils/logger.js";
import {
  SystemMessage,
  HumanMessage,
  ToolMessage,
  BaseMessage,
} from "@langchain/core/messages";

// n'hésitez pas à utiliser n'importe quel modèle. Ici, j'utilise gpt-4o-mini
const model = "gpt-4o-mini";

const toolset = new OpenAIToolSet();
const llm = new ChatOpenAI({
  model,
  apiKey: process.env.OPENAI_API_KEY,
  temperature: 0,
});

export const processMessage = async (state: State): Promise<Update> => {
  log(DEBUG, "message dans le traitement du message :", state.message);

  const llm = new ChatOpenAI({
    model,
    apiKey: process.env.OPENAI_API_KEY,
    temperature: 0,
  });

  const structuredLlm = llm.withStructuredOutput(
    z.object({
      type: z.enum([SUPPORT, OTHER, TOOL_CALL_REQUEST]).describe(`
Catégoriser le message de l'utilisateur :
- ${SUPPORT} : Support technique, aide pour les problèmes ou questions sur l'IA.
- ${TOOL_CALL_REQUEST} : L'utilisateur demande au bot d'effectuer une action d'outil (par exemple, "envoyer un email", "résumer le chat", "résumer les feuilles Google").
- ${OTHER} : Conversation générale, spam ou messages hors sujet.
`),
    }),
  );

  const res = await structuredLlm.invoke([
    [
      "system",
      `Vous êtes un expert en analyse de messages IA. Vous devez catégoriser le message dans
l'une de ces catégories :

- ${SUPPORT} : Si le message demande un support technique, de l'aide pour un problème ou des questions sur les IA et les LLM.
- ${TOOL_CALL_REQUEST} : Si le message est une commande directe ou une demande pour que le bot effectue une action en utilisant des outils/services externes. Exemples : "Résumé d'un document ou d'une feuille Google", "Résumé de la dernière heure de chat", "Envoyer un email à l'équipe de développement concernant ce bug", "Créer une carte Trello pour cette demande de fonctionnalité". Priorisez cela si l'utilisateur demande au bot de *faire* quelque chose au-delà de simplement répondre.
- ${OTHER} : Pour les discussions générales, le spam, les messages hors sujet ou tout ce qui ne correspond pas à ${SUPPORT} ou ${TOOL_CALL_REQUEST}.
`,
    ],
    ["human", state.message.content],
  ]);

  return {
    messageChoice: res.type,
  };
};

export const processSupport = async (state: State): Promise<Update> => {
  log(DEBUG, "message dans le support :", state.message);

  const llm = new ChatOpenAI({
    model,
    apiKey: process.env.OPENAI_API_KEY,
    temperature: 0,
  });

  const structuredLlm = llm.withStructuredOutput(
    z.object({
      type: z.enum([QUESTION, HELP]).describe(`
Type de support nécessaire :
- ${QUESTION} : L'utilisateur pose une question spécifique en quête d'informations ou d'une réponse.
- ${HELP} : L'utilisateur a besoin d'une assistance plus large, de conseils ou signale un problème nécessitant une intervention/dépannage.
`),
    }),
  );

  const res = await structuredLlm.invoke([
    [
      "system",
      `
Vous êtes un analyseur de tickets de support. Étant donné un message de support, catégorisez-le comme ${QUESTION} ou ${HELP}.
- ${QUESTION} : Pour les questions spécifiques.
- ${HELP} : Pour les demandes d'assistance, de dépannage ou de rapports de problèmes.
`,
    ],
    ["human", state.message.content],
  ]);

  return {
    supportTicket: {
      ...state.supportTicket,
      type: res.type,
    },
  };
};

export const processSupportHelp = async (state: State): Promise<Update> => {
  log(DEBUG, "message dans l'aide de support :", state.message);

  return {
    supportTicket: {
      ...state.supportTicket,
    },
    finalAction: {
      type: "CREATE_EMBED",
      title: "🚨 Aide nécessaire !",
      description: `Une nouvelle demande d'aide a été soulevée par **@${state.message.author}**.\n\n**Requête :**\n> ${state.message.content}`,
      roleToPing: process.env.DISCORD_SUPPORT_MOD_ID,
    },
  };
};

export const processSupportQuestion = async (state: State): Promise<Update> => {
  log(DEBUG, "message dans la catégorie de question de support :", state.message);

  const llm = new ChatOpenAI({
    model,
    apiKey: process.env.OPENAI_API_KEY,
    temperature: 0,
  });

  const systemPrompt = `
Vous êtes un assistant IA utile spécialisé dans l'IA et les LLM. Répondez
à la question de l'utilisateur de manière concise et précise en fonction des connaissances générales dans
ces domaines. Si la question est en dehors de ce cadre (par exemple, des conseils personnels,
sujets non techniques), indiquez poliment que vous ne pouvez pas répondre. Question de l'utilisateur :
`;

  const res = await llm.invoke([
    ["system", systemPrompt],
    ["human", state.message.content],
  ]);

  const llmResponse = extractStringFromAIMessage(res);
  return {
    supportTicket: {
      ...state.supportTicket,
      question: {
        description: state.message.content,
        answer: llmResponse,
      },
    },
    finalAction: {
      type: "REPLY",
      content: llmResponse,
    },
  };
};

export const processOther = async (state: State): Promise<Update> => {
  log(DEBUG, "message dans la catégorie autre :", state.message);

  const response =
    "Cela semble être un message général. Je suis là pour aider avec le support technique ou effectuer des actions spécifiques si vous le demandez. Comment puis-je vous aider avec cela ?";

  return {
    finalAction: {
      type: "REPLY_IN_THREAD",
      content: response,
    },
  };
};
```

Il n'y a pas grand-chose à expliquer pour ces nœuds. Chaque nœud dans le flux fonctionne comme un classificateur de messages. Il lance une instance de Chat LLM et utilise une sortie structurée pour s'assurer que le modèle retourne une étiquette spécifique parmi un ensemble prédéfini comme `QUESTION` ou `HELP` pour les messages de support. L'invite système définit clairement ce que signifie chaque étiquette, et votre message utilisateur est transmis pour classification.

Vous y êtes presque. Mais il manque une pièce. Pouvez-vous la repérer ?

Le nœud `process-tool-call` qui est censé gérer le flux de travail lorsque l'utilisateur demande à utiliser un outil. C'est une grande partie du flux de travail.

C'est un peu plus long, alors je vais l'expliquer séparément.

Modifiez le fichier `nodes.ts` ci-dessus pour ajouter le nœud manquant :

```typescript
// 👇 discord-bot-langgraph/src/nodes.ts

// Reste du code...
export const processToolCall = async (state: State): Promise<Update> => {
  log(DEBUG, "message dans la catégorie de demande d'appel d'outil :", state.message);

  const structuredOutputType = z.object({
    service: z
      .string()
      .describe("Le service cible (par exemple, 'email', 'discord')."),
    task: z
      .string()
      .describe(
        "Une description concise de la tâche (par exemple, 'envoyer un email à X', 'résumer le chat récent', 'créer la tâche Y').",
      ),
    details: z
      .string()
      .optional()
      .describe(
        "Tous les détails ou paramètres spécifiques extraits du message pertinents pour la tâche.",
      ),
  });

  const structuredLlm = llm.withStructuredOutput(structuredOutputType);

  let parsedActionDetails: z.infer<typeof structuredOutputType> = {
    service: "unknown",
    task: "perform a requested action",
  };

  try {
    const res = await structuredLlm.invoke([
      [
        "system",
        `Analyser la demande de l'utilisateur pour identifier une action. Extraire le service cible, une description de la tâche et tous les détails ou paramètres pertinents.
      Exemples :
      - "Rappelle-moi de vérifier les emails à 17h" : service : calendrier/rappel, tâche : définir un rappel, détails : vérifier les emails à 17h
      - "Envoyer un résumé de cette conversation au canal #general" : service : discord, tâche : envoyer un résumé au canal, détails : canal #general
      - "Créer un rapport de bug pour 'l'échec de la connexion sur mobile'" : service : gestionnaire de projet, tâche : créer un rapport de bug, détails : titre 'l'échec de la connexion sur mobile'`,
      ],
      ["human", state.message.content],
    ]);

    parsedActionDetails = res;
    log(INFO, "détails de l'action d'analyse initiale :", parsedActionDetails);
  } catch (error) {
    log(ERROR, "erreur d'analyse initiale :", error);
    return {
      toolCallRequest: {
        actionLog: `Échec de l'analyse de la demande de l'utilisateur : ${state.message.content}`,
        status: "failed",
      },
      finalAction: {
        type: "REPLY_IN_THREAD",
        content:
          "Je suis désolé, j'ai eu du mal à comprendre cette action. Pourriez-vous la reformuler, s'il vous plaît ?",
      },
    };
  }

  try {
    log(INFO, "récupération des outils composio");
    const tools = await toolset.getTools({
      apps: ["GOOGLESHEETS"],
    });

    log(INFO, `récupéré ${tools.length} outils. Erreurs si > 128 pour OpenAI :`);

    if (tools.length === 0) {
      log(WARN, "aucun outil récupéré depuis Composio. passage...");
      return {
        toolCallRequest: {
          actionLog: `Service : ${parsedActionDetails.service}, Tâche : ${parsedActionDetails.task}. Aucun outil composio trouvé`,
          status: "failed",
        },
        finalAction: {
          type: "REPLY_IN_THREAD",
          content: "Je n'ai pas trouvé d'outils pour effectuer votre action.",
        },
      };
    }

    log(DEBUG, "début de la boucle d'exécution d'outil itérative");

    const conversationHistory: BaseMessage[] = [
      new SystemMessage(
        "Vous êtes un assistant utile qui effectue des appels d'outils. Votre tâche est de comprendre la demande de l'utilisateur et d'utiliser les outils disponibles pour répondre complètement à la demande. Vous pouvez utiliser plusieurs outils en séquence pour accomplir des tâches complexes. Fournissez toujours un résumé bref et conversationnel de ce que vous avez accompli après avoir utilisé les outils.",
      ),
      new HumanMessage(state.message.content),
    ];

    let totalToolsUsed = 0;
    let finalResponse: string | null = null;

    const maxIterations = 5;
    let iteration = 0;

    while (iteration < maxIterations) {
      iteration++;
      log(
        DEBUG,
        `Itération ${iteration} : appel du LLM avec ${tools.length} outils`,
      );

      const llmResponse = await llm.invoke(conversationHistory, {
        tools: tools,
      });

      log(DEBUG, `Réponse du LLM à l'itération ${iteration} :`, llmResponse);

      const toolCalls = llmResponse.tool_calls;

      if ((!toolCalls || toolCalls.length === 0) && llmResponse.content) {
        finalResponse =
          typeof llmResponse.content === "string"
            ? llmResponse.content
            : JSON.stringify(llmResponse.content);
        log(
          INFO,
          `Réponse finale reçue après ${iteration} itérations :`,
          finalResponse,
        );
        break;
      }

      if (toolCalls && toolCalls.length > 0) {
        log(
          INFO,
          `Itération ${iteration} : exécution de ${toolCalls.length} outil(s)`,
        );
        totalToolsUsed += toolCalls.length;

        conversationHistory.push(llmResponse);

        for (const toolCall of toolCalls) {
          log(
            INFO,
            `Exécution de l'outil : ${toolCall.name} avec les arguments :`,
            toolCall.args,
          );

          const composioCompatibleToolCall: ChatCompletionMessageToolCall = {
            id: toolCall.id || uuidv4(),
            type: "function",
            function: {
              name: toolCall.name,
              arguments: JSON.stringify(toolCall.args),
            },
          };

          let toolOutputContent: string;
          try {
            const executionResult = await toolset.executeToolCall(
              composioCompatibleToolCall,
            );
            log(
              INFO,
              `Résultat de l'exécution de l'outil ${toolCall.name} :`,
              executionResult,
            );
            toolOutputContent = JSON.stringify(executionResult);
          } catch (toolError) {
            log(ERROR, `Erreur d'exécution de l'outil ${toolCall.name} :`, toolError);
            const errorMessage =
              toolError instanceof Error
                ? toolError.message
                : String(toolError);

            toolOutputContent = `Erreur : ${errorMessage}`;
          }

          conversationHistory.push(
            new ToolMessage({
              content: toolOutputContent,
              tool_call_id: toolCall.id || uuidv4(),
            }),
          );
        }

        continue;
      }

      log(
        WARN,
        `Itération ${iteration} : le LLM n'a fourni aucun appel d'outil ou contenu`,
      );
      break;
    }

    let userFriendlyResponse: string;

    if (totalToolsUsed > 0) {
      log(DEBUG, "Génération d'un résumé convivial pour l'utilisateur à l'aide du LLM");

      try {
        const summaryResponse = await llm.invoke([
          new SystemMessage(
            "Vous êtes chargé de créer un résumé bref et convivial pour un utilisateur Discord concernant les actions qui viennent d'être effectuées. Gardez-le conversationnel, en moins de 2-3 phrases, et concentrez-vous sur ce qui a été accompli plutôt que sur les détails techniques. Commencez par des phrases comme 'Terminé !', 'Réussi', 'Tout est prêt !', etc.",
          ),
          new HumanMessage(
            `L'utilisateur a demandé : "${state.message.content}"

J'ai utilisé ${totalToolsUsed} outils sur ${iteration} itérations pour compléter sa demande. ${finalResponse ? `Ma réponse finale était : ${finalResponse}` : "La tâche a été complétée avec succès."}

Générez un résumé bref et convivial de ce qui a été accompli.`,
          ),
        ]);

        userFriendlyResponse =
          typeof summaryResponse.content === "string"
            ? summaryResponse.content
            : `Terminé ! J'ai complété votre demande en utilisant ${totalToolsUsed} action${totalToolsUsed > 1 ? "s" : ""}.`;

        log(INFO, "Résumé convivial généré :", userFriendlyResponse);
      } catch (summaryError) {
        log(ERROR, "Échec de la génération du résumé :", summaryError);
        userFriendlyResponse = `Tout est prêt ! J'ai complété votre demande en utilisant ${totalToolsUsed} action${totalToolsUsed > 1 ? "s" : ""}.`;
      }
    } else {
      userFriendlyResponse =
        finalResponse ||
        `J'ai compris votre demande concernant '${parsedActionDetails.task}' mais je n'ai pas trouvé les bons outils pour la compléter.`;
    }

    const actionLog = `Service : ${parsedActionDetails.service}, Tâche : ${parsedActionDetails.task}. Utilisé ${totalToolsUsed} outils sur ${iteration} itérations.`;

    return {
      toolCallRequest: {
        actionLog,
        status: totalToolsUsed > 0 ? "success" : "acknowledged",
      },
      finalAction: {
        type: "REPLY_IN_THREAD",
        content: userFriendlyResponse,
      },
    };
  } catch (error) {
    log(ERROR, "traitement de l'appel d'outil avec Composio :", error);
    const errorMessage = error instanceof Error ? error.message : String(error);

    return {
      toolCallRequest: {
        actionLog: `Erreur lors de l'appel d'outil (Service : ${parsedActionDetails.service}, Tâche : ${parsedActionDetails.task}). Erreur : ${errorMessage}`,
        status: "failed",
      },
      finalAction: {
        type: "REPLY_IN_THREAD",
        content: "Désolé, j'ai rencontré une erreur lors du traitement de votre demande.",
      },
    };
  }
};
```

La partie jusqu'au premier bloc try-catch est la même. Jusqu'à ce point, vous essayez de déterminer l'outil que l'utilisateur essaie d'appeler. Voici la partie intéressante : gérer réellement les appels d'outils.

À ce stade, vous devez récupérer les outils de Composio. Ici, je passe simplement Google Sheets comme option à des fins de démonstration, mais vous pourriez utiliser littéralement n'importe quoi une fois que vous vous êtes authentifié comme montré ci-dessus.

Après avoir récupéré les outils, vous entrez dans une boucle où le LLM peut les utiliser. Il examine l'historique de la conversation et décide quels outils appeler. Vous exécutez ces appels, vous alimentez les résultats et vous répétez jusqu'à 5 itérations ou jusqu'à ce que le LLM donne une réponse finale.

Cette boucle s'exécute jusqu'à 5 fois comme mesure de sécurité pour que le LLM ne se retrouve pas dans un échange sans fin.

Si des outils ont été utilisés, vous demandez au LLM d'écrire un résumé convivial pour l'utilisateur au lieu de déverser la réponse JSON brute. Si aucun outil n'a fonctionné ou n'a correspondu, informez simplement l'utilisateur que vous n'avez pas pu effectuer l'action.

Maintenant, avec cela, vous avez terminé la partie difficile (je veux dire, c'était assez facile, non ?). À partir de là, vous devez simplement configurer et travailler avec l'API Discord en utilisant Discord.js.

### Configurer le client Discord.js

Dans cette application, vous utilisez des commandes slash. Pour utiliser des commandes slash dans Discord, vous devez d'abord les enregistrer. Vous pouvez le faire manuellement, mais pourquoi ne pas l'automatiser également ? 😉

Créez un nouveau fichier nommé `slash-deploy.ts` à l'intérieur du répertoire `utils` et ajoutez les lignes de code suivantes :

```typescript
// 👇 discord-bot-langgraph/utils/slash-deploy.ts

import { REST, Routes } from "discord.js";
import dotenv from "dotenv";
import { log, INFO, ERROR } from "./logger.js";
import {
  DISCORD_BOT_TOKEN,
  DISCORD_BOT_GUILD_ID,
  OPENAI_API_KEY,
  DISCORD_BOT_CLIENT_ID,
  validateEnvVars,
} from "./env-validator.js";

dotenv.config();

const requiredEnvVars = [
  DISCORD_BOT_TOKEN,
  DISCORD_BOT_GUILD_ID,
  DISCORD_BOT_CLIENT_ID,
  OPENAI_API_KEY,
];
validateEnvVars(requiredEnvVars);

const commands = [
  {
    name: "ask",
    description: "Posez une question à l'assistant IA ou donnez-lui une commande.",
    options: [
      {
        name: "prompt",
        type: 3,
        description: "Votre question ou commande pour le bot",
        required: true,
      },
    ],
  },
];

const rest = new REST({ version: "10" }).setToken(
  process.env.DISCORD_BOT_TOKEN!,
);

(async () => {
  try {
    log(INFO, "déploiement des commandes slash(/)");
    await rest.put(
      Routes.applicationGuildCommands(
        process.env.DISCORD_BOT_CLIENT_ID!,
        process.env.DISCORD_BOT_GUILD_ID!,
      ),
      {
        body: commands,
      },
    );

    log(INFO, "commandes slash(/) déployées");
  } catch (error) {
    log(ERROR, "déploiement des commandes slash(/) :", error);
  }
})();
```

Voyez votre fonction `validateEnvVars` en action ? Ici, vous spécifiez les variables d'environnement qui doivent être définies avant d'exécuter le programme. Si certaines sont manquantes et que vous essayez d'exécuter le programme, vous obtiendrez une erreur.

![Sortie de la commande échouée pour le déploiement de la commande slash vers Discord](https://cdn.hashnode.com/res/hashnode/image/upload/v1750340614800/ce0b37bc-647c-4b94-9099-2e396b0ffa93.png align="center")

La manière dont vous déployez les commandes slash vers Discord est en utilisant l'API `REST` fournie par `discord.js`, spécifiquement en appelant `rest.put` avec vos données de commande et la guilde cible.

Maintenant, exécutez simplement le script bun `commands:deploy` et vous devriez avoir `/ask` enregistré comme une commande slash dans votre Discord.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1750340646555/2d5b22df-cd43-4e54-b985-b64576831316.png align="center")

À ce stade, vous devriez voir la commande slash `/ask` disponible dans votre serveur. Il ne reste plus qu'à créer le fichier `index.ts`, qui sera le point d'entrée de votre bot Discord.

Créez un nouveau fichier nommé `index.ts` à l'intérieur du répertoire `src` et ajoutez les lignes de code suivantes :

```typescript
// 👇 discord-bot-langgraph/src/index.ts

import dotenv from "dotenv";
import {
  Client,
  Events,
  GatewayIntentBits,
  EmbedBuilder,
  type Interaction,
} from "discord.js";
import { initializeGraph } from "./graph.js";
import { type Message as ChatMessage } from "../types/types.js";
import { ERROR, INFO, log } from "../utils/logger.js";
import {
  DISCORD_BOT_TOKEN,
  DISCORD_BOT_GUILD_ID,
  OPENAI_API_KEY,
  validateEnvVars,
  DISCORD_BOT_CLIENT_ID,
  COMPOSIO_API_KEY,
} from "../utils/env-validator.js";

dotenv.config();

const requiredEnvVars = [
  DISCORD_BOT_CLIENT_ID,
  DISCORD_BOT_TOKEN,
  DISCORD_BOT_GUILD_ID,

  OPENAI_API_KEY,

  COMPOSIO_API_KEY,
];
validateEnvVars(requiredEnvVars);

const graph = initializeGraph();

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
  ],
});

// utilisez une map pour stocker l'historique par canal afin que cela fonctionne correctement avec tous les
// canaux et non pour un canal spécifique.
const channelHistories = new Map<string, ChatMessage[]>();

client.on(Events.ClientReady, async (readyClient) => {
  log(INFO, `connecté en tant que ${readyClient.user.tag}. prêt à traiter les commandes !`);
});

client.on(Events.InteractionCreate, async (interaction: Interaction) => {
  if (!interaction.isChatInputCommand()) return;
  if (interaction.commandName !== "ask") return;

  const userPrompt = interaction.options.getString("prompt", true);
  const user = interaction.user;
  const channelId = interaction.channelId;

  if (!channelHistories.has(channelId)) channelHistories.set(channelId, []);

  const messageHistory = channelHistories.get(channelId)!;

  const currentUserMessage: ChatMessage = {
    author: user.username,
    content: userPrompt,
  };

  const graphInput = {
    message: currentUserMessage,
    previousMessages: [...messageHistory],
  };

  messageHistory.push(currentUserMessage);
  if (messageHistory.length > 20) messageHistory.shift();

  try {
    await interaction.reply({
      content: "Hmm... traitement de votre demande ! 🐀",
    });

    const finalState = await graph.invoke(graphInput);

    if (!finalState.finalAction) {
      log(ERROR, "aucune action finale trouvée");
      await interaction.editReply({
        content: "Je suis désolé, je n'ai pas pu traiter votre demande.",
      });
      return;
    }

    const userPing = `<@${user.id}>`;
    const action = finalState.finalAction;

    const quotedPrompt = `🗣😀 "${userPrompt}"`;

    switch (action.type) {
      case "REPLY":
        await interaction.editReply({
          content: `${userPing}\n\n${quotedPrompt}\n\n${action.content}`,
        });
        break;

      case "REPLY_IN_THREAD":
        if (!interaction.channel || !("threads" in interaction.channel)) {
          await interaction.editReply({
            content: "Impossible de créer un fil dans ce canal",
          });
          return;
        }

        try {
          const thread = await interaction.channel.threads.create({
            name: `Action : ${userPrompt.substring(0, 50)}...`,
            autoArchiveDuration: 60,
          });

          await thread.send(
            `${userPing}\n\n${quotedPrompt}\n\n${action.content}`,
          );
          await interaction.editReply({
            content: `J'ai créé un fil pour vous : ${thread.url}`,
          });
        } catch (threadError) {
          log(ERROR, "échec de la création ou de la réponse dans le fil :", threadError);
          await interaction.editReply({
            content: `${userPing}\n\n${quotedPrompt}\n\nJ'ai essayé de créer un fil mais j'ai échoué. Voici votre réponse :\n\n${action.content}`,
          });
        }
        break;

      case "CREATE_EMBED": {
        const embed = new EmbedBuilder()
          .setColor(0xffa500)
          .setTitle(action.title)
          .setDescription(action.description)
          .setTimestamp()
          .setFooter({ text: "Système de support" });

        const rolePing = action.roleToPing ? `<@${action.roleToPing}>` : "";

        await interaction.editReply({
          content: `${userPing} ${rolePing}`,
          embeds: [embed],
        });
        break;
      }
    }
  } catch (error) {
    log(ERROR, "génération de la réponse IA ou traitement du graphique :", error);
    const errorMessage =
      "désolé, j'ai rencontré une erreur lors du traitement de votre demande.";
    if (interaction.replied || interaction.deferred) {
      await interaction.followUp({ content: errorMessage, ephemeral: true });
    } else {
      await interaction.reply({ content: errorMessage, ephemeral: true });
    }
  }
});

const token = process.env.DISCORD_BOT_TOKEN!;
client.login(token);
```

Au cœur de notre bot se trouve l'objet `Client` de `discord.js`. Cela représente votre bot et gère tout, de la connexion à l'API de Discord à l'écoute d'événements comme les messages des utilisateurs ou les interactions.

Qu'en est-il de cette intention ? Discord utilise les intentions comme un moyen pour les bots de déclarer à quel type de données ils veulent accéder. Dans notre cas :

* `Guilds` permet au bot de se connecter aux serveurs

* `GuildMessages` lui permet de voir les messages

* `MessageContent` donne accès au contenu réel des messages

Ce sont des intentions assez standard, et il en existe beaucoup d'autres en fonction des différents cas d'utilisation. Vous pouvez toujours les consulter tous [ici](https://discordjs.guide/popular-topics/intents.html#privileged-intents).

Vous conservez également une `Map` pour stocker l'historique des messages par canal afin que le bot puisse répondre avec un contexte sur plusieurs canaux :

```ts
const channelHistories = new Map<string, ChatMessage[]>();
```

Discord.js fournit l'accès à quelques événements auxquels vous pouvez écouter. Lorsque vous travaillez avec des commandes slash, il enregistre un `Events.InteractionCreate`, que vous écoutez.

Avec chaque commande `/ask`, vous prenez l'invite de l'utilisateur et les messages précédents. Si `channelHistories` n'a pas de clé avec cet `channelId` spécifique, ce qui signifie qu'il est utilisé pour la première fois, vous l'initialisez avec un tableau vide et vous les alimentez dans l'état de l'IA.

```ts
const finalState = await graph.invoke({
  message: currentUserMessage,
  previousMessages: [...messageHistory],
});
```

Selon ce que le graphique `finalAction.type` retourne, vous :

* répondez directement,

* créez un fil et répondez là-bas,

* ou envoyez un embed (pour les réponses de type support).

Si un fil ne peut pas être créé, vous revenez à répondre dans le canal principal. L'historique des messages est limité à 20 pour garder les choses légères.

Notez que nous n'utilisons pas vraiment `previousMessages` pour l'instant dans l'application, mais j'ai préparé tout ce dont vous avez besoin pour gérer l'interrogation des conversations précédentes. Vous pourriez facilement créer un nouveau nœud LangGraph qui interroge ou raisonne sur l'historique si le bot doit se référer aux conversations passées. (Prenez cela comme votre défi !)

Ce projet devrait vous donner une idée de base de la manière dont vous pouvez utiliser LangGraph + Composio pour construire un bot quelque peu utile qui peut déjà gérer des choses décentes. Il y a beaucoup plus que vous pourriez améliorer. Je vous laisse le soin de le faire. 👌😀

Voici une rapide démonstration de ce que nous avons construit jusqu'à présent :

%[https://youtu.be/aeQKN0nMGRg] 

---

## Conclusion

À ce stade, vous devriez avoir une bonne idée de la manière dont LangGraph fonctionne et aussi comment alimenter le bot avec des intégrations en utilisant Composio.

Ce n'est qu'une fraction de ce que vous pouvez faire. Essayez d'ajouter plus de fonctionnalités et de support d'intégration au bot pour l'adapter à votre flux de travail. Cela peut vraiment être utile.

Si vous vous êtes perdu quelque part en codant, vous pouvez trouver le code source [ici](https://github.com/shricodev/discord-bot-langgraph-composio).

Alors, c'est tout pour cet article. Merci beaucoup d'avoir lu ! À la prochaine. 🧡

Aimez construire des choses cool comme ça ? Je construis régulièrement ce genre de choses toutes les quelques semaines. N'hésitez pas à me contacter ici :

* GitHub : [github.com/shricodev](http://github.com/shricodev)

* Portfolio : [techwithshrijal.com](http://techwithshrijal.com)

* LinkedIn : [linkedin.com/in/iamshrijal](http://linkedin.com/in/iamshrijal)