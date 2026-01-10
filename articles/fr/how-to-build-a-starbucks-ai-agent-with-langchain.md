---
title: 'Comment créer un agent IA avec LangChain et LangGraph : Construire un agent
  Starbucks autonome'
author: Djibril-M🍀
date: '2025-12-19T00:21:01.530Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-starbucks-ai-agent-with-langchain
description: En 2023, quand j'ai commencé à utiliser ChatGPT, ce n'était qu'un chatbot
  de plus auquel je pouvais poser des questions complexes et qui identifiait les erreurs
  dans mes extraits de code. Tout allait bien. L'application n'avait aucune mémoire
  des états précédents ou de ce qui avait été dit la veille...
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1765630477745/8dffec85-c3c4-4d83-9aa4-f332439d4663.png
tags:
- name: ai agents
  slug: ai-agents
- name: langchain
  slug: langchain
- name: nestjs
  slug: nestjs
- name: handbook
  slug: handbook
seo_desc: Back in 2023, when I started using ChatGPT, it was just another chatbot
  that I could ask complex questions to and it would identify errors in my code snippets.
  Everything was fine. The application had no memory of previous states or what was
  said the...
---


En 2023, quand j'ai commencé à utiliser ChatGPT, ce n'était qu'un chatbot de plus auquel je pouvais poser des questions complexes et qui identifiait les erreurs dans mes extraits de code. Tout allait bien. L'application n'avait aucune mémoire des états précédents ou de ce qui avait été dit la veille.

Puis, en 2024, tout a commencé à changer. Nous sommes passés d'un chatbot sans état à un agent IA capable d'appeler des outils, de faire des recherches sur Internet et de générer des liens de téléchargement.

À ce moment-là, j'ai commencé à devenir curieux. Comment un LLM peut-il faire des recherches sur Internet ? Une infinité de questions me traversaient l'esprit. Peut-il créer ses propres outils, programmes, ou exécuter son propre code ? J'avais l'impression que nous nous dirigions vers la révolution Skynet (Terminator).

J'étais simplement ignorant 😅. Mais c'est alors que j'ai commencé mes recherches et découvert LangChain, un outil qui promet tous ces miracles sans un budget d'un milliard de dollars.

Dans cet article, vous allez construire un agent IA entièrement fonctionnel en utilisant LangChain et LangGraph. Vous commencerez par définir des données structurées à l'aide de schémas Zod, puis vous les analyserez pour qu'elles soient compréhensibles par l'IA. Ensuite, vous apprendrez à résumer des données en texte, à créer des outils que l'agent peut appeler et à configurer des nœuds LangGraph pour orchestrer les workflows.

Vous verrez comment compiler le graphe de workflow, gérer l'état et persister l'historique des conversations à l'aide de MongoDB. À la fin, vous aurez un barista Starbucks fonctionnel sous forme d'IA qui démontre comment combiner le raisonnement, l'exécution d'outils et la mémoire dans un seul agent.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Qu'est-ce qu'un agent LLM ?](#heading-qu-est-ce-qu-un-agent-llm)
    
* [Configuration du projet](#heading-configuration-du-projet)
    
* [Schématisation des données avec Zod](#heading-schematisation-des-donnees-avec-zod)
    
* [Comment analyser le schéma](#heading-comment-analyser-le-schema)
    
* [Résumé de données en texte](#heading-resume-de-donnees-en-texte)
    
* [Comment persister les commandes avec MongoDB dans NestJS](#heading-comment-persister-les-commandes-avec-mongodb-dans-nestjs)
    
* [Termes d'état et d'annotation LangGraph](#heading-termes-d-etat-et-d-annotation-langgraph)
    
* [Comment créer des outils pour l'agent](#heading-comment-creer-des-outils-pour-l-agent)
    
* [Nœuds LangGraph (Composants de workflow)](#heading-noeuds-langgraph-composants-de-workflow)
    
* [Déclaration du graphe](#heading-declaration-du-graphe)
    
* [Compilation du workflow et persistance de l'état (Partie finale)](#heading-compilation-du-workflow-et-persistance-de-l-etat-partie-finale)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Pour profiter pleinement de cet article, vous devez avoir une compréhension de base de TypeScript, Node.js, et un peu de NestJS vous aidera, car c'est le framework backend que nous utiliserons.

## **Qu'est-ce qu'un agent LLM ?**

Par définition, un agent LLM est un programme logiciel capable de percevoir son environnement, de prendre des décisions et d'entreprendre des actions autonomes pour atteindre des objectifs spécifiques. Il le fait souvent en interagissant avec des outils et des systèmes.

De nombreux frameworks et conventions ont été créés pour y parvenir, et l'un des plus célèbres et des plus utilisés est le framework ReAct (Reason & Act).

Avec ce framework, le LLM reçoit un prompt, réfléchit, décide de l'action suivante (cela peut être l'appel d'un outil spécifique) et reçoit les données de l'outil. Une fois la réponse de l'outil reçue, le modèle d'IA observe la réponse, génère sa propre réponse et planifie ses actions suivantes en fonction de la réponse de l'outil.

Vous pouvez en savoir plus sur ce concept dans le [livre blanc officiel](https://arxiv.org/abs/2210.03629). Et voici un diagramme qui résume l'ensemble du processus :

![Diagramme illustrant le workflow d'un agent LLM : l'agent reçoit un prompt, raisonne, décide d'une action (comme l'appel d'un outil), observe la réponse de l'outil, génère sa propre réponse et planifie de manière itérative ses actions suivantes à l'aide du framework ReAct](https://cdn.hashnode.com/res/hashnode/image/upload/v1765064426716/b1e6d7b2-4e4b-43c4-af5c-9cd49b27a864.png align="center")

Notez que le workflow n'est pas limité à une seule invocation d'outil – il peut passer par plusieurs cycles avant de répondre à l'utilisateur.

Mais pour qu'un agent LLM soit vraiment proche de l'humain et agisse avec la connaissance du passé, il nécessite une mémoire. Cela lui permet de se souvenir des prompts et des réponses précédents, maintenant ainsi la cohérence au sein d'un thread donné.

Il n'y a pas de source unique de vérité sur la façon d'aborder cela. La plupart des agents implémentent une mémoire à court terme. Cela signifie que l'agent ajoutera chaque nouveau chat à l'historique de la conversation, et lorsqu'un nouveau prompt est soumis, l'agent ajoutera les messages précédents au nouveau prompt.

Cette méthode est très efficace et donne au LLM une solide connaissance des états précédents. Mais elle peut aussi introduire des problèmes, car plus la conversation s'allonge, plus le LLM devra parcourir tous les messages précédents afin de comprendre quelle action entreprendre ensuite.

Et cela peut introduire une certaine dérive contextuelle, tout comme les humains en font l'expérience. Vous ne pouvez pas regarder un podcast de deux heures et vous souvenir de tous les mots prononcés, n'est-ce pas ? Dans ce scénario, le LLM se concentrera sur les informations les plus pertinentes, finissant par perdre une partie du contexte.

![Illustration montrant le workflow d'un agent LLM avec mémoire : l'agent traite plusieurs cycles de prompts et d'interactions avec les outils, maintient une mémoire à court terme des conversations précédentes et utilise ce contexte pour décider des actions, tandis que le contexte plus ancien peut s'estomper avec le temps, causant une dérive contextuelle potentielle.](https://cdn.hashnode.com/res/hashnode/image/upload/v1765064542431/18b8d0a7-b9f1-4f7d-993d-76b3c4058ccf.png align="center")

Vous n'avez pas besoin d'implémenter cela de zéro. De nombreux outils et frameworks ont été développés pour rendre l'implémentation aussi facile que possible. Vous pouvez le construire de zéro si vous le souhaitez, bien sûr, mais nous ne ferons pas cela ici.

Dans cet article, nous allons construire un barista Starbucks qui collecte les informations de commande et appelle un outil `create_order` une fois que la commande répond à tous les critères. C'est un outil que nous allons créer et exposer à l'IA.

## Configuration du projet

Commençons par initialiser notre projet. Nous utiliserons Nest.js pour son efficacité et son support natif de TypeScript. Notez que rien ici n'est lié à Nest.js – c'est juste une préférence de framework, et tout ce que nous ferons ici peut être fait avec Node.js et Express.js.

Voici une liste de tous les outils que nous utiliserons :

1. `langchain/core` - **Toujours requis**
    
    C'est le moteur principal de Langchain qui définit tous les outils de base et les fonctions fondamentales, contenant :
    
    * les templates de prompt
        
    * les types de messages
        
    * les runnables
        
    * les interfaces d'outils
        
    * les utilitaires de composition de chaînes, et plus encore.
        
    
    La plupart des projets LangChain en ont besoin.
    
2. `langchain/google-genai` - Ce package est utilisé pour interagir avec les modèles d'IA générative de Google, les modèles d'embeddings vectoriels et d'autres outils connexes.
    
3. `langchain/langgraph` - **Important pour construire un agent IA avec un contrôle total**
    
    Langgraph est un framework d'orchestration de bas niveau pour construire des agents contrôlables. Il peut être utilisé pour construire :
    
    * Des agents conversationnels.
        
    * Des automatisations de tâches complexes.
        
    * La gestion du contexte de l'agent.
        
4. `langchain/langgraph-checkpoint-mongodb` - Ce package fournit un checkpointer basé sur MongoDB pour LangGraph, permettant la persistance de l'état de l'agent et de la mémoire à court terme à l'aide de MongoDB.
    
5. `@langchain/mongodb` - Ce package fournit des intégrations MongoDB pour LangChain, vous permettant de :
    
    * Stocker et récupérer des embeddings vectoriels.
        
    * Persister des documents LangChain, des agents ou des états de mémoire.
        
    * Intégrer facilement MongoDB comme backend de base de données pour vos workflows d'IA.
        
6. `@nestjs/mongoose` - Un wrapper NestJS autour de Mongoose pour MongoDB. Fournit :
    
    * Le support de l'injection de dépendances pour les modèles Mongoose.
        
    * Une définition de schéma et une gestion de modèle simplifiées.
        
    * Une intégration transparente de MongoDB dans les applications NestJS, permettant la persistance des données structurées pour les applications d'IA ou tout backend.
        
7. `langchain` - C'est le package npm principal qui agrège les fonctionnalités de LangChain. Il fournit :
    
    * L'accès aux connecteurs, utilitaires et modules de base.
        
    * L'importation facile de différents composants LangChain en un seul endroit.
        
    * Couramment utilisé aux côtés de `@langchain/core` pour construire des applications avec une configuration minimale.
        
8. `mongodb` - Le driver officiel MongoDB pour Node.js. Il fournit :
    
    * Un accès flexible et de bas niveau aux bases de données MongoDB.
        
    * Le support des opérations CRUD, des transactions et de l'indexation.
        
    * Une dépendance requise si vous prévoyez de connecter des composants LangChain ou votre backend directement à MongoDB.
        
9. `mongoose` - Une bibliothèque ODM (Object Data Modeling) pour MongoDB. Offre :
    
    * Une modélisation des données basée sur des schémas pour les documents MongoDB.
        
    * Des middlewares, de la validation et des hooks pour les opérations MongoDB.
        
    * Idéal pour la gestion des données structurées dans NestJS ou d'autres applications Node.js.
        
10. `zod` - Une bibliothèque de validation de schéma orientée TypeScript. Utilisée pour :
    
    * Définir des schémas de données stricts et valider les entrées/sorties.
        
    * Assurer la sécurité des types au moment de l'exécution.
        
    * Utile dans les applications d'IA pour valider les réponses des modèles ou imposer la cohérence des données.
        

Commencez par initialiser votre projet Nest.js et installez toutes les dépendances requises :

```dart
$ npm i -g @nestjs/cli // Si vous n'avez pas Nest.js installé sur votre machine
$ nest new project-name

"dependencies" : {
    "@langchain/core": "^0.3.75",
    "@langchain/google-genai": "^0.2.16",
    "@langchain/langgraph": "^0.4.8",
    "@langchain/langgraph-checkpoint-mongodb": "^0.1.1",
    "@langchain/mongodb": "^0.1.0",
    "@nestjs/mongoose": "^11.0.3",
    "langchain": "^0.3.33",
    "mongodb": "^6.19.0",
    "mongoose": "^8.18.1",
    "zod": "^4.1.8"
}

// Les versions peuvent ne pas être les mêmes au moment où vous lisez ceci, je recommande donc de vérifier
// la documentation officielle pour chaque package.
```

Maintenant que notre projet est créé et que tous les packages sont installés, voyons ce que nous devons faire pour transformer notre vision en projet. Pensez à ce dont vous aurez besoin pour créer un barista Starbucks :

* Tout d'abord, nous devons définir la structure de nos données (création de schémas)
    
* Ensuite, nous devons créer une liste de menu à laquelle notre agent se référera.
    
* Après cela, nous ajouterons l'interaction avec le LLM
    
* Et enfin, nous ajouterons la possibilité de sauvegarder les conversations précédentes pour le contexte conversationnel.
    

### Structure des dossiers

Vous pouvez modifier cette structure de dossiers et l'adapter en fonction de votre framework de choix. Mais l'implémentation de base est la même pour tous les frameworks.

```plaintext
├── .env
├── .eslintrc.js
├── .gitignore
├── .prettierrc
├── nest-cli.json
├── package.json
├── README.md
├── tsconfig.build.json
├── tsconfig.json
├── src/
│   ├── app.controller.ts
│   ├── app.module.ts
│   ├── app.service.ts
│   ├── main.ts
│   ├── chat/
│   │   ├── chat.controller.ts
│   │   ├── chat.module.ts
│   │   ├── chat.service.ts
│   │   └── dtos/
│   │       └── chat.dto.ts
│   ├── data/
│   │   └── schema/
│   │       └── order.schema.ts
│   └── util/
│       ├── constants/
│       │   └── drinks_data.ts
│       ├── schemas/
│       │   ├── drinks/
│       │   │   └── Drink.schema.ts
│       │   └── orders/
│       │       └── Order.schema.ts
│       ├── summeries/
│       │   └── drink.ts
│       └── types/
```

## Schématisation des données avec Zod

Ce fichier contient toutes nos définitions de schémas concernant les boissons et toutes les modifications qu'elles peuvent recevoir. Cette partie est utile pour définir la structure des données qui seront utilisées par l'agent IA.

### **Importation de Zod**

Dans le fichier `lib/util/schemas/drinks.ts`, avant de définir tout schéma, importez la bibliothèque Zod, qui fournit des outils pour construire des schémas orientés TypeScript.

```typescript
// Importe l'objet 'z' de la bibliothèque 'zod'.
// Zod est une bibliothèque de déclaration et de validation de schéma orientée TypeScript.
// 'z' est l'objet principal utilisé pour définir des schémas (ex: z.object, z.string, z.boolean, z.array).
import z from "zod";
```

Zod vous offre un moyen simple et expressif de définir et de valider la structure des données avec lesquelles notre agent interagira.

### **Schéma de boisson (Drink Schema)**

Ce schéma représente la structure d'une boisson dans le menu de style Starbucks. J'ai divisé et expliqué chaque champ afin que le lecteur comprenne clairement ce que chaque propriété contrôle.

```typescript
export const DrinkSchema = z.object({
  name: z.string(),            // Nom requis de la boisson
  description: z.string(),     // Explication requise de ce qu'est la boisson
  supportMilk: z.boolean(),    // Si les options de lait sont disponibles
  supportSweeteners: z.boolean(), // Si des édulcorants peuvent être ajoutés
  supportSyrup: z.boolean(),   // Si les sirops aromatisés sont autorisés
  supportTopping: z.boolean(), // Si les garnitures sont supportées
  supportSize: z.boolean(),    // Si la boisson peut être commandée en différentes tailles
  image: z.string().url().optional(), // URL d'image optionnelle
});
```

### **Ce que ce schéma représente**

* Il garantit que chaque boisson a un nom et une description appropriés.
    
* Il définit quelles personnalisations s'appliquent à la boisson.
    
* Il prépare l'agent à raisonner sur les options de boissons dans un format structuré et validé.
    

### **Schéma d'édulcorant (Sweetener Schema)**

Chaque option d'édulcorant dans le menu est représentée par son propre schéma.

```typescript
export const SweetenerSchema = z.object({
  name: z.string(),                // Nom de l'édulcorant
  description: z.string(),         // Ce que c'est / description du goût
  image: z.string().url().optional(), // URL d'image optionnelle
});
```

Cela garantit la cohérence entre toutes les entrées d'édulcorants et évite les données malformées.

### **Schéma de sirop (Syrup Schema)**

Similaire aux édulcorants, mais pour les saveurs de sirop :

```typescript

export const SyrupSchema = z.object({
  name: z.string(),
  description: z.string(),
  image: z.string().url().optional(),
});
```

Cela peut représenter des saveurs comme Vanille, Caramel ou Noisette.

### **Schéma de garniture (Topping Schema)**

Les garnitures telles que la crème fouettée ou la cannelle sont définies ici.

```typescript
export const ToppingSchema = z.object({
  name: z.string(),
  description: z.string(),
  image: z.string().url().optional(),
});
```

### **Schéma de taille (Size Schema)**

Les tailles de boissons sont également modélisées comme des objets :

```typescript
export const SizeSchema = z.object({
  name: z.string(),               // ex: Petit, Moyen
  description: z.string(),        // Une courte explication
  image: z.string().url().optional(),
});
```

### **Schéma de lait (Milk Schema)**

Représente les types de lait tels que Entier, Écrémé, Amande ou Avoine.

```typescript
export const MilkSchema = z.object({
  name: z.string(),
  description: z.string(),
  image: z.string().url().optional(),
});
```

### **Collections d'éléments**

Maintenant que les schémas d'éléments individuels existent, nous pouvons en créer des **collections**. Celles-ci représentent toutes les garnitures, tailles, types de lait, sirops, édulcorants disponibles, ainsi que l'intégralité du menu des boissons.

```typescript
export const ToppingsSchema = z.array(ToppingSchema);
export const SizesSchema = z.array(SizeSchema);
export const MilksSchema = z.array(MilkSchema);
export const SyrupsSchema = z.array(SyrupSchema);
export const SweetenersSchema = z.array(SweetenerSchema);
export const DrinksSchema = z.array(DrinkSchema);
```

Pourquoi des tableaux ? Parce que dans le monde réel, votre agent recevra des **listes** provenant d'une base de données ou d'une API — pas des éléments uniques.

### **Types inférés**

Zod permet également à TypeScript d'inférer automatiquement les types à partir des schémas.

Cela garantit que :

* Les types TypeScript correspondent toujours aux schémas.
    
* Vous évitez les définitions dupliquées.
    
* Le code de l'agent reste cohérent et sûr.
    

```typescript
export type Drink = z.infer<typeof DrinkSchema>;
export type SupportSweetener = z.infer<typeof SweetenerSchema>;
export type Syrup = z.infer<typeof SyrupSchema>;
export type Topping = z.infer<typeof ToppingSchema>;
export type Size = z.infer<typeof SizeSchema>;
export type Milk = z.infer<typeof MilkSchema>;

export type Toppings = z.infer<typeof ToppingsSchema>;
export type Sizes = z.infer<typeof SizesSchema>;
export type Milks = z.infer<typeof MilksSchema>;
export type Syrups = z.infer<typeof SyrupsSchema>;
export type Sweeteners = z.infer<typeof SweetenersSchema>;
export type Drinks = z.infer<typeof DrinksSchema>;
```

Ceux-ci fournissent au reste de votre code LangChain/LangGraph un typage fort basé sur vos définitions de schémas.

Ce fichier complet :

* Encode toutes les structures de données liées aux boissons.
    
* Fournit une validation pour garantir des données propres et prévisibles.
    
* Génère automatiquement des types TypeScript.
    
* Aide l'agent IA à raisonner de manière fiable sur les boissons et les options de personnalisation.
    

Vous utiliserez ces schémas plus tard et les convertirez en représentations textuelles pour les prompts du LLM.

*Vous pouvez trouver le fichier contenant tout le code* [*ici*](https://github.com/DjibrilM/langgraph-starbucks-agent/blob/main/src/lib/schemas/drinks.ts)*.*

## Comment analyser le schéma

Comme mentionné précédemment, les LLM sont des **machines à entrées-sorties textuelles**. Ils ne comprennent pas directement les types TypeScript ou les schémas Zod. Si vous incluez un schéma à l'intérieur d'un prompt, le modèle le verra simplement comme du texte brut sans comprendre sa structure ou ses contraintes.

Pour cette raison, nous avons besoin d'un moyen de convertir les schémas dans un format de chaîne lisible qui peut être intégré à l'intérieur d'un prompt, tel que :

> "La sortie doit être un objet JSON avec les champs suivants..."

C'est exactement le problème résolu par `StructuredOutputParser` de `langchain/output_parsers`. Il prend un schéma Zod et le transforme en :

* Une description lisible par l'homme qui peut être envoyée à un LLM.
    
* Un validateur qui vérifie si la sortie du modèle correspond au schéma.
    

En résumé, il agit comme un pont entre la logique d'application typée et la sortie d'IA basée sur le texte.

### Définition du schéma de commande (Order Schema)

Nous allons commencer par un schéma Zod simple qui représente la commande de boisson d'un client. Ce schéma définit la forme exacte et les contraintes des données que nous attendons du modèle.

```typescript
export const OrderSchema = z.object({
  drink: z.string(),
  size: z.string(),
  mil: z.string(),
  syrup: z.string(),
  sweeteners: z.string(),
  toppings: z.string(),
  quantity: z.number().min(1).max(10),
});

export type OrderType = z.infer<typeof OrderSchema>;
```

À ce stade, le schéma n'est utile qu'à l'intérieur de notre application TypeScript. Le LLM n'a toujours aucune idée de ce que signifie cette structure.

### Analyse du schéma en texte lisible par l'homme

C'est là qu'intervient l'analyse de schéma. En utilisant `StructuredOutputParser.fromZodSchema`, nous pouvons transformer le schéma Zod en :

* Des instructions que le LLM peut comprendre.
    
* Un validateur d'exécution qui garantit que la réponse est correcte.
    

```typescript
export const OrderParser =
  StructuredOutputParser.fromZodSchema(OrderSchema as any);
```

L'analyseur permet deux workflows critiques :

#### Génération d'instructions de prompt

L'analyseur peut générer une description textuelle du schéma qui ressemble approximativement à : "Renvoyez un objet JSON avec les champs `drink`, `size`, `mil`, `syrup`, `sweeteners` et `toppings` sous forme de chaînes, et `quantity` sous forme de nombre entre 1 et 10." Cette chaîne peut être injectée directement dans votre prompt afin que le LLM sache exactement comment formater sa réponse.

#### Validation de la sortie du modèle

Une fois que le LLM a répondu, sa sortie n'est toujours que du texte. L'analyseur :

* Convertit ce texte en un objet JavaScript.
    
* Le valide par rapport au schéma Zod original.
    
* Lance une erreur si quelque chose manque, est malformé ou hors limites.
    

Cela empêche les données invalides générées par l'IA (par exemple, `quantity: 0`) d'entrer dans votre système.

### Réutilisation de la même approche pour d'autres schémas

Une fois que vous avez compris ce modèle, l'appliquer à d'autres schémas est simple.

Par exemple, vous pouvez faire la même chose pour un `DrinkSchema` :

```typescript
export const DrinkParser =
  StructuredOutputParser.fromZodSchema(DrinkSchema as any);
```

Maintenant, vous pouvez dire en toute confiance quelque chose comme : "Hé Gemini, voici à quoi ressemble un objet boisson — s'il te plaît, réponds en utilisant cette structure."

### Pourquoi c'est important

L'analyse de schéma vous permet de :

* Conserver un typage fort dans votre application.
    
* Donner des instructions de formatage claires au LLM.
    
* Convertir en toute sécurité une sortie d'IA non structurée en données validées et prêtes pour la production.
    

Sans cette étape, travailler avec des LLM à grande échelle devient peu fiable et sujet aux erreurs.

## Résumé de données en texte

Dans le contexte des agents LLM, le **résumé de données en texte** consiste à convertir des données structurées — telles que des objets renvoyés par une base de données ou une API backend — en **chaînes de caractères claires et lisibles par l'homme** qui peuvent être intégrées directement dans les prompts.

Même les LLM les plus avancés fonctionnent uniquement sur du texte. Ils ne raisonnent pas sur des objets JavaScript, des lignes de base de données ou des structures JSON de la même manière que les humains ou les programmes. Plus votre entrée textuelle est claire et descriptive, plus la sortie du modèle sera précise et fiable.

Pour cette raison, un modèle courant et recommandé lors de la construction de systèmes alimentés par LLM est :

**Récupérer les données structurées → les résumer en langage naturel → passer le résumé dans le prompt**

Pour garder cet article focalisé, nous stockerons nos données dans des constantes au lieu d'interroger une base de données réelle. La technique est exactement la même, que les données proviennent de MongoDB, PostgreSQL ou d'une API.

### L'idée centrale

L'objectif du résumé de données en texte est simple :

* Prendre un objet avec des champs et des drapeaux booléens
    
* Le convertir en un court paragraphe qui explique ce que l'objet représente
    
* Éliminer l'ambiguïté et les suppositions pour le LLM
    

Au lieu de forcer le modèle à inférer le sens à partir de données brutes, nous l'*énonçons explicitement*.

### Résumer un objet boisson

Considérez l'objet boisson suivant :

```typescript
{
  name: 'Espresso',
  description: 'Shot de café concentré et fort.',
  supportMilk: false,
  supportSweeteners: true,
  supportSyrup: true,
  supportTopping: false,
  supportSize: false,
}
```

Bien que cette structure soit facile à comprendre pour les développeurs, elle n'est pas idéale pour un prompt de LLM. Les drapeaux booléens comme `supportMilk: false` nécessitent une interprétation, ce qui augmente le risque de suppositions incorrectes.

Au lieu de cela, nous convertissons cet objet en un paragraphe descriptif :

"Une boisson nommée Espresso. Elle est décrite comme un shot de café fort et concentré. Elle ne peut pas être préparée avec du lait. Elle peut être préparée avec des édulcorants. Elle peut être préparée avec du sirop. Elle ne peut pas être préparée avec des garnitures. Elle ne peut pas être préparée en différentes tailles."

Cette transformation est exactement ce que fournit le résumé de données en texte.

### Un modèle de résumé standard

Voici un exemple simplifié de la façon dont nous convertissons un objet `Drink` en une description lisible.

```typescript
export const createDrinkItemSummary = (drink: Drink): string => {
  const name = `Une boisson nommée ${drink.name}.`;
  const description = `Elle est décrite comme ${drink.description}.`;

  const milk = drink.supportMilk
    ? 'Elle peut être préparée avec du lait.'
    : 'Elle ne peut pas être préparée avec du lait.';

  const sweeteners = drink.supportSweeteners
    ? 'Elle peut être préparée avec des édulcorants.'
    : 'Elle ne peut pas contenir d\'édulcorants.';

  const syrup = drink.supportSyrup
    ? 'Elle peut être préparée avec du sirop.'
    : 'Elle ne peut pas être préparée avec du sirop.';

  const toppings = drink.supportTopping
    ? 'Elle peut être préparée avec des garnitures.'
    : 'Elle ne peut pas être préparée avec des garnitures.';

  const size = drink.supportSize
    ? 'Elle peut être préparée en différentes tailles.'
    : 'Elle ne peut pas être préparée en différentes tailles.';

  return `${name} ${description} ${milk} ${sweeteners} ${syrup} ${toppings} ${size}`;
};
```

### Pourquoi cela fonctionne bien pour les LLM

* La logique booléenne est convertie en **phrases explicites**
    
* Chaque capacité et limitation est clairement énoncée
    
* La sortie peut être intégrée directement dans un prompt système ou utilisateur
    

### Résumer des collections de données

Cette même approche s'applique aux listes de données telles que les laits, les sirops, les garnitures ou les tailles. Au lieu de passer un tableau d'objets au modèle, nous les convertissons en résumés textuels sous forme de puces :

```typescript
export const createSweetenersSummary = (): string => {
  return `Les édulcorants disponibles sont :
${SWEETENERS.map(
  (s) => `- ${s.name} : ${s.description}`
).join('\n')}`;
};
```

Cela donne au modèle une **vue d'ensemble complète et lisible** des options disponibles sans lui demander d'interpréter des tableaux bruts.

### Appliquer la même idée à d'autres domaines

Ce modèle n'est pas limité aux boissons ou aux menus. Il fonctionne pour *n'importe quel* domaine. Par exemple, voici la même technique de résumé appliquée à un objet représentant une chaussure dans un assistant de commande en ligne :

```typescript
export const createShoeItemSummary = (shoe: {
  name: string;
  description: string;
  genderCategory: string;
  styleType: string;
  material: string;
  availableInMultipleColors: boolean;
  limitedEdition: boolean;
  supportsCustomization: boolean;
}): string => {
  return `
Une chaussure nommée ${shoe.name}.
Elle est décrite comme ${shoe.description}.
Elle est classée comme une chaussure ${shoe.genderCategory.toLowerCase()}.
Elle appartient au style de mode ${shoe.styleType.toLowerCase()}.
Elle est faite de ${shoe.material.toLowerCase()}.
${shoe.availableInMultipleColors ? 'Elle est disponible en plusieurs couleurs.' : 'Elle est disponible en une seule couleur.'}
${shoe.limitedEdition ? 'C\'est une édition limitée.' : 'Ce n\'est pas une édition limitée.'}
${shoe.supportsCustomization ? 'Elle supporte des options de personnalisation.' : 'Elle ne supporte pas d\'options de personnalisation.'}
`.trim();
};
```

Ce qui produit une sortie comme :

"Une chaussure nommée Veloria Canvas Sneaker. Elle est décrite comme une basket minimaliste de tous les jours conçue pour une tenue décontractée. Elle est classée comme une chaussure unisexe. Elle appartient au style de mode décontracté. Elle est faite de toile respirante. Elle est disponible en plusieurs couleurs. Ce n'est pas une édition limitée. Elle supporte des options de personnalisation légère."

## Comment persister les commandes avec MongoDB dans NestJS

Maintenant que nous avons établi les bases de notre application — schémas, analyseurs et résumés de données en texte — il est temps de **persister les données**. Dans un assistant réel, les commandes et les conversations ne devraient pas disparaître au redémarrage du serveur. Elles doivent être stockées de manière fiable afin de pouvoir être récupérées, analysées ou poursuivies plus tard.

Pour y parvenir, nous utiliserons MongoDB comme base de données et l'intégration NestJS Mongoose pour gérer les modèles de données et les collections.

### Connexion de MongoDB à une application NestJS

Dans NestJS, le `AppModule` est le module racine de l'application. C'est là que les dépendances globales — telles que les connexions aux bases de données — sont configurées.

```typescript
@Module({
  imports: [
    MongooseModule.forRoot(process.env.MONGO_URI),
    ChatsModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

Que se passe-t-il ici ?

* `MongooseModule.forRoot(...)` établit une connexion MongoDB globale.
    
* La chaîne de connexion est lue à partir d'une variable d'environnement (`MONGO_URI`), ce qui est la pratique recommandée pour la sécurité.
    
* Une fois configurée, cette connexion devient disponible dans toute l'application.
    
* `ChatsModule` est importé afin qu'il puisse accéder à la connexion à la base de données et enregistrer ses propres schémas.
    

Cette configuration garantit que chaque module de fonctionnalité peut interagir en toute sécurité avec MongoDB sans créer de multiples connexions.

### Définition d'un schéma de commande avec Mongoose

NestJS utilise des décorateurs pour définir les schémas MongoDB de manière propre et basée sur des classes. Chaque classe représente un document MongoDB, et chaque propriété devient un champ dans la collection.

```typescript
@Schema()
export class Order {
  @Prop({ required: true })
  drink: string;

  @Prop({ default: null })
  size: string;

  @Prop({ default: null })
  milk: string;

  @Prop({ default: null })
  syrup: string;

  @Prop({ default: null })
  sweeter: string;

  @Prop({ default: null })
  toppings: string;

  @Prop({ default: 1 })
  quantity: number;
}
```

Pourquoi cette approche ?

* Chaque décorateur `@Prop()` correspond directement à un champ MongoDB.
    
* Les valeurs par défaut permettent de sauvegarder des commandes partielles de manière incrémentielle.
    
* Les champs obligatoires (comme `drink`) imposent une intégrité de base des données.
    
* Le schéma reflète étroitement la sortie structurée produite par le LLM.
    

Une fois la classe définie, elle est convertie en un schéma Mongoose :

```typescript
export const OrderSchema = SchemaFactory.createForClass(Order);
```

Cette seule ligne crée :

* Une collection MongoDB
    
* Une couche de validation
    
* Un schéma que Mongoose peut utiliser pour créer, lire et mettre à jour des commandes
    

### Comment cela s'intègre dans l'architecture de l'agent LLM

À ce stade, nous avons :

* **Des schémas Zod** → pour valider la sortie de l'IA
    
* **Des fonctions de résumé** → pour convertir les données en prompts lisibles
    
* **Des schémas MongoDB** → pour persister les commandes finalisées
    

Cette séparation est intentionnelle :

* Zod gère la *validation côté IA*
    
* Mongoose gère la *persistance en base de données*
    
* NestJS agit comme le liant qui unit le tout
    

### Préparation de la logique de l'agent

Avec la base de données en place, nous sommes maintenant prêts à implémenter l'agent lui-même.

Les responsabilités de l'agent incluront :

* L'interprétation des messages des utilisateurs
    
* L'appel d'outils
    
* La génération de commandes structurées
    
* Leur validation
    
* Leur persistance dans MongoDB
    
* Le maintien de l'état conversationnel
    

Toute cette logique vivra à l'intérieur du fichier `src/chats/chats.service.ts`. La section suivante présente la **logique centrale de l'agent**, et nous la parcourrons étape par étape pour que chaque partie soit facile à suivre.

Commencez par importer les dépendances requises :

```tsx

import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { MongoClient } from 'mongodb';
import { Model } from 'mongoose';

import { tool } from '@langchain/core/tools';
import {
  ChatPromptTemplate,
  MessagesPlaceholder,
} from '@langchain/core/prompts';
import { AIMessage, BaseMessage, HumanMessage } from '@langchain/core/messages';

import { ChatGoogleGenerativeAI } from '@langchain/google-genai';
import { StateGraph } from '@langchain/langgraph';
import { ToolNode } from '@langchain/langgraph/prebuilt';
import { Annotation } from '@langchain/langgraph';
import { START, END } from '@langchain/langgraph';

import { MongoDBSaver } from '@langchain/langgraph-checkpoint-mongodb';

import z from 'zod';

import { Order } from './schemas/order.schema';
import { OrderParser, OrderSchema, OrderType } from 'src/lib/schemas/orders';
import { DrinkParser } from 'src/lib/schemas/drinks';
import { DRINKS } from 'src/lib/utils/constants/menu_data';

import {
  createSweetenersSummary,
  availableToppingsSummary,
  createAvailableMilksSummary,
  createSyrupsSummary,
  createSizesSummary,
  createDrinkItemSummary,
} from 'src/lib/summaries';

const GOOGLE_API_KEY = process.env.GOOGLE_API_KEY || '';
const client: MongoClient = new MongoClient(process.env.MONGO_URI || '');
const database_name = 'drinks_db';
```

## Termes d'état et d'annotation LangGraph

Dans LangGraph, l'**état** (state) peut être considéré comme un espace de travail temporaire qui existe pendant que l'agent s'exécute. Il stocke toutes les informations auxquelles les nœuds (nous verrons les nœuds en détail plus tard) pourraient avoir besoin d'accéder, comme le dernier message, l'historique de la conversation ou toute donnée intermédiaire générée pendant l'exécution.

Cet état permet aux nœuds de **le lire, de le mettre à jour et de transmettre des informations** au fur et à mesure que l'agent traite un workflow, ce qui en fait la mémoire à court terme de l'agent pour la durée de l'exécution.

```tsx
@Injectable()
export class ChatService {

  chatWithAgent = async ({
    thread_id,
    query,
  }: {
    thread_id: string;
    query: string;
  }) => {

    const graphState = Annotation.Root({
      messages: Annotation<BaseMessage[]>({
        reducer: (x, y) => [...x, ...y],
      }),
    });

  }

}
```

Ce code définit l'**état LangGraph** pour l'agent de chat. L'objet `graphState` agit comme une mémoire centrale que chaque nœud du workflow peut lire et mettre à jour.

Le champ `messages` stocke spécifiquement tous les messages de la conversation, y compris les messages de l'utilisateur, les réponses de l'IA et les sorties des outils. La fonction réductrice (reducer) `[...x, ...y]` ajoute les nouveaux messages au tableau existant, préservant l'historique de la conversation à travers plusieurs étapes.

Le mécanisme de réducteur de LangGraph permet aux développeurs de contrôler comment le nouvel état fusionne avec l'ancien. Dans ce système de chat, l'approche est similaire à la mise à jour d'un état React avec `setMessages(prev => [...prev, ...newMessages])` : elle conserve les anciens messages tout en ajoutant les nouveaux.

Ensemble, cet état permet à l'agent, aux outils et au système de checkpointing de maintenir une conversation cohérente, permettant à chaque nœud du workflow LangGraph d'accéder au contexte complet et de contribuer de manière incrémentielle.

## Comment créer des outils pour l'agent

Les chatbots modernes peuvent faire plus que simplement générer du texte - ils peuvent également effectuer des recherches sur Internet, lire des fichiers ou effectuer des calculs. Bien que les LLM soient puissants, ils ne peuvent pas exécuter de code ou compiler des programmes par eux-mêmes.

Dans le contexte des agents LLM, un outil est un morceau de code écrit par le développeur de l'agent qu'un LLM peut invoquer sur la machine hôte. La machine hôte exécute le code, et le LLM ne reçoit que la sortie finale du calcul.

Voici comment créer un outil qui stocke les commandes dans la base de données. Toujours dans la fonction `chatWithAgent` au sein de la classe `ChatService`. Sous la définition du store d'état :

```tsx
const orderTool = tool(
  async ({ order }: { order: OrderType }) => {
    try {
      await this.orderModel.create(order);
      return 'Order created successfully';
    } catch (error) {
      console.log(error);
      return 'Failed to create the order';
    }
  },
  {
    schema: z.object({
      order: OrderSchema.describe('The order that will be stored in the DB'),
    }),
    name: 'create_order',
    description: 'This tool creates a new order in the database',
  }
);

const tools = [orderTool];
```

## Nœuds LangGraph (Composants de workflow)

D'un point de vue définition, un nœud LangGraph est un composant fondamental d'un workflow LangGraph, représentant une unité unique de calcul ou une étape individuelle dans le processus d'un agent IA.

Chaque nœud peut effectuer une tâche spécifique, telle que la génération d'un message, l'invocation d'un outil ou la transformation de données, et il interagit avec l'état pour lire les entrées et écrire les sorties. Ensemble, les nœuds sont connectés pour former le workflow de l'agent ou le graphe d'exécution, permettant un raisonnement complexe et des opérations en plusieurs étapes.

Dans notre projet, nous aurons quatre nœuds.

1. **Nœud Agent :** Ce nœud est chargé d'interagir avec le LLM - il construit le template de message principal de l'agent et empile les anciens messages sur le nouveau prompt pour créer du contexte.
    
2. **Nœud Tools :** Le nœud d'outils introduit des capacités externes, qui permettent au workflow d'interagir avec des API externes.
    
3. **Nœud** `START` **:** Ce nœud indique le point d'entrée de notre workflow, ou pour être précis, quel nœud appeler lorsqu'un utilisateur initie une conversation avec l'agent. Il est assez simple à définir.
    
4. `addConditionalEdges` - `addConditionalEdges('agent', shouldContinue)` : Dans LangGraph, `.addConditionalEdges('agent', shouldContinue)` permet au workflow de bifurquer dynamiquement après l'exécution du nœud `'agent'`, en fonction d'une condition définie dans `shouldContinue`. Contrairement à une arête fixe, qui va toujours d'un nœud au suivant, une arête conditionnelle évalue la sortie de l'agent et dirige le workflow vers différents nœuds selon le résultat, permettant à l'agent IA de prendre des décisions et d'adapter ses prochaines étapes.
    

## Déclaration du graphe

Dans LangGraph, un graphe est la structure centrale qui modélise le workflow d'un agent IA sous forme de nœuds interconnectés, où chaque nœud représente une étape de calcul, un outil ou une décision. Il orchestre le flux de données et de contrôle entre les nœuds, gère les branchements conditionnels et maintient la boucle récursive d'exécution.

Essentiellement, le graphe est la colonne vertébrale qui garantit que les interactions complexes et avec état se produisent de manière coordonnée et modulaire, connectant des nœuds comme `agent`, `tools` et des arêtes conditionnelles en un workflow cohérent.

Avec ces connaissances en place, nous pouvons maintenant créer le graphe de l'agent avec tous ses nœuds.

```tsx
  const callModal = async (states: typeof graphState.State) => {
    const prompt = ChatPromptTemplate.fromMessages([
      {
        role: 'system',
        content: `
            You are a helpful assistant that helps users order drinks from Starbucks.
            Your job is to take the user's request and fill in any missing details based on how a complete order should look.
            A complete order follows this structure: ${OrderParser}.

            **TOOLS**
            You have access to a "create_order" tool.
            Use this tool when the user confirms the final order.
            After calling the tool, you should inform the user whether the order was successfully created or if it failed.

            **DRINK DETAILS**
            Each drink has its own set of properties such as size, milk, syrup, sweetener, and toppings.
            Here is the drink schema: ${DrinkParser}.

            You must ask for any missing details before creating the order.

            If the user requests a modification that is not supported for the selected drink, tell them that it is not possible.

            If the user asks for something unrelated to drink orders, politely tell them that you can only assist with drink orders.

            **AVAILABLE OPTIONS**
            List of available drinks and their allowed modifications:
            ${DRINKS.map((drink) => `- ${createDrinkItemSummary(drink)}`)}

            Sweeteners: ${createSweetenersSummary()}
            Toppings: ${availableToppingsSummary()}
            Milks: ${createAvailableMilksSummary()}
            Syrups: ${createSyrupsSummary()}
            Sizes: ${createSizesSummary()}

            Order schema: ${OrderParser}

            If the user's query is unclear, tell them that the request is not clear.

            **ORDER CONFIRMATION**
            Once the order is ready, you must ask the user to confirm it.
            If they confirm, immediately call the "create_order" tool.
            Only respond after the tool completes, indicating success or failure.

            **FRONTEND RESPONSE FORMAT**
            Every response must include:

            "message": "Your message to the user",
            "current_order": "The order currently being constructed",
            "suggestions": "Options the user can choose from",
            "progress": "Order status ('completed' after creation)"

            **IMPORTANT RULES**
            - Be friendly, use emojis, and add humor.
            - Use null for unfilled fields.
            - Never omit the JSON tracking object.
        `,
      },
      new MessagesPlaceholder('messages'),
    ]);

  const formattedPrompt = await prompt.formatMessages({
    time: new Date().toISOString(),
    messages: states.messages,
  });

  const chat = new ChatGoogleGenerativeAI({
    model: 'gemini-2.0-flash',
    temperature: 0,
    apiKey: GOOGLE_API_KEY,
  }).bindTools(tools);

  const result = await chat.invoke(formattedPrompt);
  return { messages: [result] };
  };     
    const shouldContinue = (state: typeof graphState.State) => {
      const lastMessage = state.messages[
        state.messages.length - 1
      ] as AIMessage;
      return lastMessage.tool_calls?.length ? 'tools' : END;
    };

    const toolsNode = new ToolNode<typeof graphState.State>(tools);

    /**
     * Build the conversation graph.
     */
    const graph = new StateGraph(graphState)
      .addNode('agent', callModal)
      .addNode('tools', toolsNode)
      .addEdge(START, 'agent')
      .addConditionalEdges('agent', shouldContinue)
      .addEdge('tools', 'agent');
```

### Explication

* **État du graphe (**`graphState`)  
    L'objet `graphState` est la mémoire partagée entre tous les nœuds. Il stocke les `messages`, qui suivent l'historique de la conversation, y compris les entrées utilisateur, les réponses de l'IA et les interactions avec les outils. Le réducteur `[...x, ...y]` ajoute les nouveaux messages, préservant le contexte passé. C'est similaire aux mises à jour d'état React : les anciens messages restent tandis que les nouveaux sont ajoutés.
    
* **Nœud Agent (**`callModal`)  
    Ce nœud gère l'**appel au LLM**. Il formate un prompt contenant les instructions système, les schémas de boissons, les outils disponibles et les règles de réponse pour le frontend. En incluant `states.messages`, l'IA voit l'historique complet de la conversation, permettant un dialogue multi-tours.
    
* **Exécution du LLM**  
    `ChatGoogleGenerativeAI` génère la réponse de l'IA. `.bindTools(tools)` permet à l'IA d'appeler directement des outils comme `create_order` si nécessaire.
    
* **Flux conditionnel (**`shouldContinue`)  
    Après la réponse de l'IA, la fonction `shouldContinue` vérifie si le message inclut des appels d'outils. Si c'est le cas, l'exécution passe au nœud `tools` ; sinon, le workflow se termine. Cela permet un branchement dynamique en fonction de la sortie de l'IA.
    
* **Nœud d'outil (**`ToolNode`)  
    Le nœud `tools` exécute l'outil demandé, comme la sauvegarde de la commande dans la base de données. Une fois terminé, le contrôle revient au nœud agent, permettant à l'IA de répondre à l'utilisateur avec les résultats.
    
* **Construction du graphe (**`StateGraph`)  
    Les nœuds sont connectés dans un workflow cohérent :
    
    * `START → agent` commence la conversation
        
    * Les arêtes conditionnelles gèrent l'exécution des outils
        
    * `tools → agent` garantit que l'agent peut répondre après l'exécution des outils
        
* **Flux global**  
    Ensemble, le graphe et l'état partagé garantissent une **conversation multi-tours avec état**. L'IA peut demander des détails manquants, appeler des outils quand c'est nécessaire et maintenir le contexte à travers les interactions. Chaque nœud lit et écrit dans le même état.
    

## **Compilation du workflow et persistance de l'état (Partie finale)**

Jusqu'à présent, tous nos états sont temporaires, ce qui signifie qu'ils n'existent que pendant la durée de la requête d'un utilisateur. Cependant, nous voulons que notre agent **se souvienne et rappelle le contexte de la conversation** même lorsqu'une nouvelle requête est envoyée avec le même `thread_id` ou ID de conversation.

Pour y parvenir, nous utiliserons MongoDB en combinaison avec la bibliothèque `langchain/langgraph-checkpoint-mongo`. Cette bibliothèque simplifie la persistance de l'état en associant chaque conversation à un ID unique assigné manuellement. Toutes les opérations — de la récupération des messages précédents à la sauvegarde des nouveaux — sont gérées en interne, vous n'avez qu'à fournir l'ID de conversation avec lequel vous souhaitez travailler.

```tsx
const graph = new StateGraph(graphState)
  .addNode('agent', callModal)
  .addNode('tools', toolsNode)
  .addEdge(START, 'agent')
  .addConditionalEdges('agent', shouldContinue)
  .addEdge('tools', 'agent');

  const checkpointer = new MongoDBSaver({ client, dbName: database_name });

  const app = graph.compile({ checkpointer });

  /**
     * Run the graph using the user's message.
     */
    const finalState = await app.invoke(
      { messages: [new HumanMessage(query)] },
      { recursionLimit: 15, configurable: { thread_id } },
    );

  /**
   * Extract JSON payload from AI response.
   */
  function extractJsonResponse(response: any) {
    const match = response.match(/```json\\s*([\\s\\S]*?)\\s*```/i);
    if (match && match[1] && typeof response === 'string') {
      return JSON.parse(match[1].trim());
    }
    throw response;
  }

  const lastMessage = finalState.messages.at(-1) as AIMessage; // Extrait le dernier message de la conversation
  return extractJsonResponse(lastMessage.content); // Réponse
```

Le code ci-dessus démontre comment initialiser un checkpoint, compiler un graphe et invoquer l'agent avec un prompt entrant.

La méthode `extractJsonResponse` est utilisée pour récupérer la réponse formatée que nous avons demandé au LLM de générer chaque fois qu'il renvoie quelque chose à l'utilisateur.

Sur la base de cette instruction donnée dans le template principal, chaque réponse doit inclure : "message" : "Votre message à l'utilisateur", "current\_order" : "La commande en cours de construction", "suggestions" : "Options que l'utilisateur peut choisir", "progress" : "Statut de la commande ('completed' après création)"

Chaque réponse du LLM devrait ressembler à ceci :

```tsx
'```json\\n' +
  '{\\n' +
  '"message": "Got it! To make sure I get your order just right, can you clarify which coffee drink you\\'d like? We have Latte, Cappuccino, Cold Brew, and Frappuccino. 😊",\\n' +
  '"current_order": {\\n' +
  '"drink": null,\\n' +
  '"size": null,\\n' +
  '"mil": null,\\n' +
  '"syrup": null,\\n' +
  '"sweeteners": null,\\n' +
  '"toppings": null,\\n' +
  '"quantity": null\\n' +
  '},\\n' +
  '"suggestions": [\\n' +
  '"Latte",\\n' +
  '"Cappuccino",\\n' +
  '"Cold Brew",\\n' +
  '"Frappuccino"\\n' +
  '],\\n' +
  '"progress": "incomplete"\\n' +
  '}\\n' +
  '```';
```

Cette structure permet au frontend de rendre facilement la réponse du LLM et de suivre l'état de la commande actuelle. C'est plus un choix de conception qu'une convention.

## **Conclusion**

Construire un agent IA autonome avec LangChain et LangGraph vous permet de combiner la puissance de raisonnement des LLM avec l'exécution d'outils pratiques et une mémoire persistante. En définissant des schémas, en analysant les données dans des formats lisibles par l'homme et en orchestrant les workflows via des nœuds, vous pouvez créer des agents intelligents capables de gérer des tâches du monde réel — comme notre barista Starbucks.

Avec l'intégration de MongoDB pour la persistance de l'état, votre agent peut maintenir le contexte à travers les conversations, rendant les interactions plus naturelles et humaines. Cette approche ouvre la porte à la construction d'assistants IA plus sophistiqués et spécifiques à un domaine sans repartir de zéro.

En résumé : **définissez vos données, apprenez à votre agent comment raisonner et laissez LangGraph orchestrer la magie.** ☕🤖

Code source ici : [https://github.com/DjibrilM/langgraph-starbucks-agent](https://github.com/DjibrilM/langgraph-starbucks-agent)

### **Ressources**

* Documentation LangGraph : [https://docs.langchain.com/oss/javascript/langgraph/quickstart](https://docs.langchain.com/oss/javascript/langgraph/quickstart)
    
* Synergizing Reasoning and Acting in Language Models : [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)