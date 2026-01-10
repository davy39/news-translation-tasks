---
title: Comment construire des agents autonomes en utilisant le chaînage de prompts
  avec des primitives d'IA (sans frameworks)
subtitle: ''
author: Maham Codes
co_authors: []
series: null
date: '2025-04-21T15:22:42.999Z'
originalURL: https://freecodecamp.org/news/build-autonomous-agents-using-prompt-chaining-with-ai-primitives
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745248868960/12efd5ab-3d9b-4c93-979f-45bde796639b.png
tags:
- name: llm
  slug: llm
- name: ai-agent
  slug: ai-agent
- name: AI
  slug: ai
seo_title: Comment construire des agents autonomes en utilisant le chaînage de prompts
  avec des primitives d'IA (sans frameworks)
seo_desc: 'Autonomous agents might sound complex, but they don’t have to be. These
  are AI systems that can make decisions and take actions on their own to achieve
  a goal – usually by using LLMs, various tools, and memory to reason through a task.

  You can build ...'
---

Les agents autonomes peuvent sembler complexes, mais ils ne le sont pas nécessairement. Ce sont des systèmes d'IA capables de prendre des décisions et d'agir de manière autonome pour atteindre un objectif, généralement en utilisant des LLMs, divers outils et une mémoire pour raisonner à travers une tâche.

Vous pouvez construire des systèmes agentiques puissants sans frameworks lourds ni moteurs d'orchestration. L'une des méthodes les plus simples et efficaces consiste à utiliser les architectures agentiques de Langbase (construites avec des primitives d'IA qui ne nécessitent pas de framework pour déployer des systèmes agentiques d'IA scalables).

Dans cet article, nous allons explorer l'une des architectures agentiques de Langbase : le chaînage de prompts. Nous verrons pourquoi c'est utile et comment l'implémenter en construisant un agent de chaînage de prompts.

### Table des matières

1. [Prérequis](#heading-prerequisites)

2. [Primitives d'IA (architecture agentique)](#heading-ai-primitives-agentic-architecture)

3. [Qu'est-ce que le chaînage de prompts ?](#heading-quest-ce-que-le-chainage-de-prompts)

4. [Architecture de chaînage de prompts](#heading-architecture-de-chainage-de-prompts)

5. [SDK Langbase](#heading-langbase-sdk)

6. [Construction d'un agent de chaînage de prompts en utilisant Langbase Pipes](#heading-construction-dun-agent-de-chainage-de-prompts-en-utilisant-httpslangbasecomlangbase-pipes)

   * [Étape 1 : Installation de votre projet](#heading-etape-1-installation-de-votre-projet)

   * [Étape 2 : Obtenir la clé API Langbase](#heading-etape-2-obtenir-la-cle-api-langbase)

   * [Étape 3 : Ajouter les clés API LLM](#heading-etape-3-ajouter-les-cles-api-llm)

   * [Étape 4 : Ajouter la logique dans le fichier prompt-chaining.ts](#heading-etape-4-ajouter-la-logique-dans-le-fichier-prompt-chainingts)

   * [Étape 5 : Exécuter le fichier](#heading-etape-5-executer-le-fichier)

7. [Le résultat](#heading-le-resultat)

## Prérequis

Avant de commencer à créer un agent de chaînage de prompts, vous devez avoir les éléments suivants prêts.

Dans ce tutoriel, j'utiliserai la pile technologique suivante :

* [Langbase](http://langbase.com/) – la plateforme pour construire et déployer vos agents IA serverless.

* [SDK Langbase](https://langbase.com/docs/sdk) – un SDK IA TypeScript, conçu pour fonctionner avec JavaScript, TypeScript, Node.js, Next.js, React, et autres.

* [OpenAI](https://openai.com/) – pour obtenir la clé LLM pour le modèle préféré.

Vous devrez également :

* Vous inscrire sur Langbase pour obtenir accès à la clé API.

* Vous inscrire sur OpenAI pour générer la clé LLM pour le modèle que vous souhaitez utiliser (pour cette démonstration, j'utiliserai le modèle `openai:gpt-4o-mini`). Vous pouvez générer la clé [ici](https://platform.openai.com/api-keys).

## Primitives d'IA (Architecture Agentique)

Une approche au niveau des primitives d'IA signifie construire des systèmes d'IA en utilisant les blocs de construction les plus basiques, sans dépendre d'abstractions lourdes, de moteurs d'orchestration ou de frameworks complets.

Les agents Pipe et Memory de Langbase servent de blocs de construction.

Les [agents Pipe](https://langbase.com/docs/pipe) sur Langbase sont différents des autres agents. Ce sont des agents IA serverless avec des outils agentiques qui peuvent fonctionner avec n'importe quel langage ou framework. Les agents Pipe sont facilement déployables, et avec une seule API, ils vous permettent de connecter 250+ LLMs à n'importe quelle donnée pour construire n'importe quel workflow d'API de développeur.

Les [agents mémoire de Langbase](https://langbase.com/docs/memory) (solution de mémoire à long terme) sont conçus pour acquérir, traiter, conserver et récupérer des informations de manière transparente. Ils attachent dynamiquement des données privées à n'importe quel LLM, permettant des réponses contextuelles en temps réel et réduisant les hallucinations. La mémoire, lorsqu'elle est connectée à un agent pipe, devient un agent mémoire.

Avec ces blocs de construction (primitives d'IA), vous pouvez construire des workflows agentiques complets. Pour cela, les architectures agentiques de Langbase servent de modèle pour construire, déployer et mettre à l'échelle des agents autonomes.

Examinons l'une des architectures agentiques : le chaînage de prompts.

## Qu'est-ce que le chaînage de prompts ?

Le chaînage de prompts est une architecture d'agent où une tâche est décomposée en une séquence de prompts. Chaque étape transmet sa sortie à la suivante, permettant au LLM de gérer des workflows plus complexes avec une plus grande précision.

Cela est particulièrement utile pour des tâches structurées comme :

* La synthèse et l'analyse de documents

* La génération de contenu en plusieurs étapes

* La transformation et le nettoyage de données

* La validation et l'affinage de contenu

Plutôt que de compter sur un seul prompt pour tout faire, vous divisez le travail en étapes ciblées. Cela facilite le débogage, améliore la qualité de la sortie et introduit des "points de contrôle" naturels dans votre workflow IA.

## Architecture de chaînage de prompts

Voici une architecture de référence expliquant le workflow :

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXchmBDXvU8DXnQu7EjqKoSUTdxQ__KsTZemZ9yaTGpeCAMUc1RX_Swby9NOtxXwONFdKGPrjFcjVZhQmQoKe1eu2nceFWGLaPA8bpu-JYB7rh4ChJmExLRRWJzjB4686HjUsP_t?key=l4b_IFG3ufUXGX7WLcs4Dknq align="left")

Ce diagramme est une référence visuelle pour montrer comment le chaînage de prompts peut être utilisé pour construire un système agentique léger en utilisant simplement des appels LLM et une logique conditionnelle, sans aucun framework lourd.

Voici une décomposition de ce qui se passe dans le flux :

1. **Entrée → Appel LLM**

   * Prend l'entrée initiale et exécute le premier appel LLM.

   * Produit la Sortie 1.

2. **Porte**

   * Évalue la Sortie 1 pour décider de l'étape suivante.

   * Agit comme un point de contrôle conditionnel (par exemple, succès/échec, validation d'intention, seuil de confiance).

3. **Si la Porte passe :**

   * Passe à l'Appel LLM 2 avec la Sortie 1 comme entrée.

   * L'Appel LLM 2 produit la Sortie 2.

   * La Sortie 2 va dans l'Appel LLM 3, qui génère le résultat final.

   * La sortie finale s'écoule vers la Sortie.

4. **Si la Porte échoue :**

   * Le flux se termine prématurément à la Sortie.

   * Évite les appels LLM supplémentaires, économisant du calcul et évitant les sorties invalides.

## SDK Langbase

Le SDK Langbase facilite la construction d'agents IA puissants en utilisant TypeScript. Il vous donne tout ce dont vous avez besoin pour travailler avec n'importe quel LLM, connecter vos propres modèles d'embedding, gérer la mémoire des documents et construire des agents IA capables de raisonner et de répondre.

Le SDK est conçu pour fonctionner avec Node.js, Next.js, React ou toute pile JavaScript moderne. Vous pouvez l'utiliser pour télécharger des documents, créer une mémoire sémantique et exécuter des workflows IA (appelés agents Pipes) avec seulement quelques lignes de code.

Langbase est une plateforme IA API-first, et son SDK TypeScript simplifie l'expérience, rendant facile de commencer sans avoir à gérer l'infrastructure. Il suffit d'ajouter votre clé API, d'écrire votre logique, et vous êtes prêt à partir.

Maintenant que vous connaissez le SDK Langbase, commençons à construire l'agent de chaînage de prompts.

## Construction d'un agent de chaînage de prompts en utilisant Langbase Pipes

Parcourons un système agentique réel de chaînage de prompts construit en utilisant les agents Pipe de Langbase (agents IA serverless avec des APIs unifiées pour chaque LLM). Pour cela, nous allons configurer un projet Node.js de base.

Nous allons implémenter un pipeline de contenu marketing de produit séquentiel qui transforme une description brute de produit en une copie marketing polie à travers trois étapes (c'est-à-dire la création de trois agents Pipe) :

### Première étape (Agent de synthèse) :

* Prend une description brute de produit

* La condense en deux phrases concises

* A une porte de qualité qui vérifie si le résumé est suffisamment détaillé (au moins 10 mots)

### Deuxième étape (Agent de fonctionnalités) :

* Prend le résumé de l'étape 1

* Extrait et formate les fonctionnalités clés du produit sous forme de puces

### Étape finale (Agent de copie marketing) :

* Prend les puces de l'étape 2

* Génère une copie marketing raffinée pour le produit

Toutes les étapes utiliseront le modèle OpenAI 4o-mini via le SDK Langbase. Le meilleur, c'est que vous pouvez utiliser différents modèles LLM pour chaque étape/création d'agent Pipe également.

Ce qui rend cela intéressant, c'est son approche par pipeline. Chaque étape s'appuie sur la sortie de l'étape précédente, avec une vérification de qualité après l'étape de synthèse pour garantir que le pipeline maintient des normes élevées.

Commençons par la création de ce système agentique de chaînage de prompts.

### Étape 1 : Installation de votre projet

Je vais construire une application Node.js de base en TypeScript qui utilise le SDK Langbase pour créer un système agentique de chaînage de prompts scalable. Il fonctionnera sans aucun framework, suivant une approche au niveau des primitives d'IA.

Pour commencer, créez un nouveau répertoire pour votre projet et naviguez jusqu'à lui :

```bash
mkdir agentic-architecture && cd agentic-architecture
```

Ensuite, initialisez un projet Node.js et créez un fichier TypeScript en exécutant cette commande dans votre terminal :

```bash
npm init -y && touch prompt-chaining.ts
```

Le fichier `prompt-chaining.ts` contiendra le code de toutes les créations d'agents.

Après cela, nous utiliserons le SDK Langbase pour créer les agents et `dotenv` pour gérer les variables d'environnement. Installons donc ces dépendances.

```bash
npm i langbase dotenv
```

### Étape 2 : Obtenir la clé API Langbase

Chaque requête que vous envoyez à Langbase nécessite une clé API. Vous pouvez générer des clés API depuis le [Langbase studio](https://studio.langbase.com/) en suivant ces étapes :

1. Passez à votre compte utilisateur ou organisation.

2. Dans la barre latérale, cliquez sur le menu `Paramètres`.

3. Dans la section des paramètres développeur, cliquez sur le lien `Clés API Langbase`.

4. À partir de là, vous pouvez créer une nouvelle clé API ou gérer celles existantes.

Pour plus de détails, vous pouvez consulter la documentation des clés API Langbase.

Après avoir généré la clé API, créez un fichier `.env` à la racine de votre projet et ajoutez votre clé API Langbase :

```bash
LANGBASE_API_KEY=xxxxxxxxx
```

Remplacez xxxxxxxxx par votre clé API Langbase.

### Étape 3 : Ajouter les clés API LLM

Une fois que vous avez la clé API Langbase, vous aurez également besoin de la clé LLM pour exécuter l'agent RAG. Si vous avez configuré des clés API LLM dans votre profil, la mémoire IA et le pipe de l'agent les utiliseront automatiquement. Sinon, naviguez vers la page des clés API LLM et ajoutez des clés pour différents fournisseurs comme OpenAI, Anthropic, etc.

Suivez ces étapes pour ajouter les clés LLM :

1. Ajoutez les clés API LLM dans votre compte en utilisant le studio Langbase

2. Passez à votre compte utilisateur ou organisation.

3. Dans la barre latérale, cliquez sur le menu `Paramètres`.

4. Dans la section des paramètres développeur, cliquez sur le lien `Clés API LLM`.

5. À partir de là, vous pouvez ajouter des clés API LLM pour différents fournisseurs comme OpenAI, TogetherAI, Anthropic, etc.

### Étape 4 : Ajouter la logique dans le fichier `prompt-chaining.ts`

Dans le fichier `prompt-chaining.ts` que vous avez créé à l'étape 1, ajoutez le code suivant :

```typescript
import dotenv from 'dotenv';
import { Langbase } from 'langbase';


dotenv.config();


const langbase = new Langbase({
   apiKey: process.env.LANGBASE_API_KEY!
});


async function main(inputText: string) {
   // Étapes de chaînage de prompts
   const steps = [
       {
           name: `summary-agent-${Date.now()}`,
           model: 'openai:gpt-4o-mini',
           description:
               'résumer la description du produit en deux phrases concises',
           prompt: `Veuillez résumer la description de produit suivante en deux phrases
           concises :\n`
       },
       {
           name: `features-agent-${Date.now()}`,
           model: 'openai:gpt-4o-mini',
           description: 'extraire les caractéristiques clés du produit sous forme de puces',
           prompt: `Sur la base du résumé suivant, listez les caractéristiques clés du produit sous
           forme de puces :\n`
       },
       {
           name: `marketing-copy-agent-${Date.now()}`,
           model: 'openai:gpt-4o-mini',
           description:
               'générer une copie marketing polie en utilisant les puces',
           prompt: `En utilisant les puces suivantes des caractéristiques du produit, générez une
           copie marketing convaincante et raffinée pour le produit, soyez précis :\n`
       }
   ];


   //  Créer les agents pipe
   await Promise.all(
       steps.map(step =>
           langbase.pipes.create({
               name: step.name,
               model: step.model,
               messages: [
                   {
                       role: 'system',
                       content: `Vous êtes un assistant utile qui peut ${step.description}.`
                   }
               ]
           })
       )
   );


   // Initialiser les données avec l'entrée brute.
   let data = inputText;


   try {
       // Traiter chaque étape du workflow de manière séquentielle.
       for (const step of steps) {
           // Appeler le LLM pour l'étape actuelle.
           const response = await langbase.pipes.run({
               stream: false,
               name: step.name,
               messages: [{ role: 'user', content: `${step.prompt} ${data}` }]
           });


           data = response.completion;


           console.log(`Étape : ${step.name} \n\n Réponse : ${data}`);


           // Porte sur la sortie de l'agent de synthèse pour s'assurer qu'elle n'est pas trop brève.
           // Si le résumé fait moins de 10 mots, lever une erreur pour arrêter le workflow.
           if (step.name === 'summary-agent' && data.split(' ').length < 10) {
               throw new Error(
                   'Porte déclenchée pour l\'agent de synthèse. Le résumé est trop bref. Sortie du workflow.'
               );
               return;
           }
       }
   } catch (error) {
       console.error('Erreur dans le workflow principal :', error);
   }


   // La copie marketing finale raffinée
   console.log('Copie Marketing de Produit Finale Raffinée :', data);
}


const inputText = `Notre nouvelle montre intelligente est un appareil polyvalent doté d'un écran haute résolution,
une longue durée de vie de la batterie, un suivi de la condition physique et une connectivité smartphone. Elle est conçue pour
un usage quotidien et est résistante à l'eau. Avec des capteurs de pointe et un design élégant, elle est
parfaite pour les individus passionnés de technologie.`;


main(inputText);
```

Voici une décomposition du code ci-dessus :

Configuration et initialisation :

* `dotenv` charge les variables `env` depuis le fichier `.env` pour un accès sécurisé à la clé API.

* Langbase est importé depuis le SDK pour interagir avec l'API.

* Une instance cliente Langbase est créée en utilisant votre clé API.

Définir les étapes IA (chaîne de prompts) :

* Trois agents IA (étapes) sont définis pour un pipeline :

   1. **Agent de Synthèse** : Résume l'entrée de la description du produit en 2 phrases.

   2. **Agent d'Extraction de Fonctionnalités** : Extrait les fonctionnalités clés du résumé sous forme de puces.

   3. **Agent de Copie Marketing** : Transforme les puces en une copie marketing polie.

* Chaque agent utilise `openai:gpt-4o-mini` comme LLM.

Créer les Pipes Langbase (agents) :

* Les pipes Langbase sont créés pour chaque étape en utilisant `langbase.pipes.create(...)`.

* Chaque pipe a un nom unique (horodaté) et un message système guidant son but.

Exécuter le workflow (traitement séquentiel) :

* Le texte d'entrée circule à travers chaque étape une par une :

   * La sortie d'une étape devient l'entrée pour la suivante.

   * Les pipes sont exécutés en utilisant `langbase.pipes.run(...)`.

* Les sorties intermédiaires sont journalisées après chaque étape.

Vérification de validation (contrôle) :

* Si la sortie du résumé est trop courte (moins de 10 mots), le workflow s'arrête avec une erreur.

Sortie finale :

* Après toutes les étapes, le résultat final est une copie marketing raffinée imprimée sur la console.

Pour cet article, nous utilisons une description de produit de montre intelligente de démonstration pour voir le résultat dans le champ `inputText`.

### Étape 5 : Exécuter le fichier

Pour exécuter le fichier `prompt-chaining.ts` afin de voir les résultats, vous devez :

* Ajouter TypeScript comme dépendance

* Ajouter un script pour exécuter les fichiers TypeScript

* Ajouter un fichier de configuration TypeScript

Pour cela, installons d'abord `pnpm` en exécutant cette commande dans votre terminal :

```bash
pnpm install
```

Ensuite, dans votre terminal, exécutez cette commande pour ajouter les dépendances et fichiers de configuration pertinents :

```bash
pnpm add -D typescript ts-node @types/node
```

Après cela, créez un fichier de configuration TypeScript `tsconfig.json` :

```bash
pnpm exec tsc --init
```

Et mettez à jour le `package.json` pour ajouter le script pertinent. Voici à quoi votre `package.json` devrait ressembler après la mise à jour :

```json
{
 "name": "agentic-architectures",
 "version": "1.0.0",
 "main": "index.js",
 "scripts": {
   "test": "echo \"Error: no test specified\" && exit 1",
   "prompt-chaining": "ts-node prompt-chaining.ts"
 },
 "keywords": [],
 "author": "",
 "license": "ISC",
 "description": "",
 "dependencies": {
   "dotenv": "^16.5.0",
   "langbase": "^1.1.55"
 },
 "devDependencies": {
   "@types/node": "^22.14.1",
   "ts-node": "^10.9.2",
   "typescript": "^5.8.3"
 }
}
```

Maintenant, exécutons le projet avec pnpm run prompt-chaining

## Le résultat

Après avoir exécuté le projet, vous verrez le résultat de l'exemple de description de produit de montre intelligente dans votre console comme suit :

```bash
Étape : summarize-description
Réponse : Cette montre intelligente combine le suivi de la condition physique et la connectivité smartphone avec un écran haute résolution et une batterie longue durée. Conçue pour un usage quotidien avec une construction élégante et résistante à l'eau, elle est idéale pour les passionnés de technologie.

Étape : extract-features
Réponse : Voici les caractéristiques clés du produit extraites du résumé :

Suivi de la condition physique
Connectivité smartphone
Écran haute résolution
Batterie longue durée
Design élégant
Construction résistante à l'eau
Conçue pour un usage quotidien
Étape : refine-marketing-copy
Réponse : ## Élevez votre quotidien avec une connectivité transparente et des performances inégalées.

Découvrez la fusion parfaite du style et de la fonctionnalité avec notre appareil révolutionnaire, conçu pour s'intégrer de manière transparente dans votre mode de vie actif. Restez motivé et informé avec le suivi complet de la condition physique, tout en restant facilement connecté via la connectivité smartphone.

Plongez dans une clarté vibrante avec l'écran haute résolution époustouflant, et traversez votre journée sans interruption grâce à la batterie longue durée. Encadré dans un design élégant, cet appareil est aussi stylé que pratique.

Conçu pour résister aux rigueurs de la vie quotidienne, la construction résistante à l'eau garantit un port sans souci, qu'il pleuve ou qu'il fasse beau. Conçu pour le confort et la performance, cet appareil est conçu pour un usage quotidien, vous permettant de vivre votre meilleure vie, sans effort.
```

C'est ainsi que vous pouvez construire un système agentique de chaînage de prompts avec des primitives d'IA (sans framework) en utilisant le SDK Langbase et les architectures agentiques de Langbase.

Merci d'avoir lu !

Connectez-vous avec moi par 👌 :

* En vous abonnant à ma chaîne [YouTube](https://www.youtube.com/@AIwithMahamCodes). Si vous souhaitez apprendre sur l'IA et les agents.

* En vous abonnant à ma newsletter gratuite ["The Agentic Engineer"](https://mahamcodes.substack.com/) où je partage toutes les dernières nouvelles/tendances/emplois en IA et agents, et bien plus encore.

* Suivez-moi sur [X (Twitter)](https://x.com/MahamDev).