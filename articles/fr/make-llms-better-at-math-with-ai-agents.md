---
title: Comment améliorer les LLMs en mathématiques à l'aide d'agents IA, MathJS et
  des appels d'outils BaseAI
subtitle: ''
author: Maham Codes
co_authors: []
series: null
date: '2024-12-19T14:53:46.717Z'
originalURL: https://freecodecamp.org/news/make-llms-better-at-math-with-ai-agents
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1734537732263/2ec966b6-d1d3-4d0f-ae37-982ef26ebc55.jpeg
tags:
- name: llm
  slug: llm
- name: AI
  slug: ai
- name: ai agents
  slug: ai-agents
- name: openai
  slug: openai
seo_title: Comment améliorer les LLMs en mathématiques à l'aide d'agents IA, MathJS
  et des appels d'outils BaseAI
seo_desc: Large Language Models (LLMs) like GPT often struggle to answer mathematical
  questions. In fact, if you ask a human a tough math question, like what is 185 cm
  in ft, they’ll struggle as well. They’d likely need a calculator to perform this
  conversion ...
---

Les grands modèles de langage (LLMs) comme GPT ont souvent du mal à répondre aux questions mathématiques. En fait, si vous posez une question de maths difficile à un humain, comme "Qu'est-ce que 185 cm en pieds", il aura aussi du mal. Il aurait probablement besoin d'une calculatrice pour effectuer cette conversion – et il en va de même pour les LLMs.

Les LLMs sont conçus pour gérer le langage naturel. Bien qu'ils soient généralement bons pour générer des mots et assembler le langage, lorsqu'il s'agit de mathématiques, ils ont souvent besoin d'aide.

Contrairement à une calculatrice ou à une bibliothèque mathématique, les LLMs ne peuvent parfois pas raisonner ou traiter la logique symbolique. Ainsi, bien qu'ils puissent gérer l'arithmétique de base, surtout si c'est quelque chose de familier de leurs données d'entraînement, ils ont généralement du mal avec des problèmes plus complexes, en particulier les problèmes écrits.

La question principale est de savoir comment corriger cette limitation des LLMs ?

Sans aucun doute, les LLMs ont évolué avec le lancement de modèles de raisonnement comme GPT-o1 ou Llama 3.3. Mais ils hallucinent toujours, manquent d'accès aux données en temps réel, ont du mal avec les mathématiques complexes et produisent des résultats non déterministes. Heureusement, nous pouvons résoudre ce problème en utilisant des agents IA.

## Qu'est-ce qu'un agent IA ?

Les agents IA sont des logiciels autonomes qui utilisent les LLMs pour effectuer des tâches au-delà de la simple génération de texte.

Ils prennent des décisions et exécutent des actions. Les agents IA s'appuient sur les LLMs pour la compréhension du langage mais ajoutent des capacités comme la mémoire, l'interaction en temps réel et la prise de décision.

## Comment les agents IA résolvent les limitations des LLMs

Les agents augmentent les capacités des LLMs de plusieurs manières :

* **Mémoire :** Les agents IA aident les LLMs à conserver le contexte des interactions passées, améliorant la cohérence des conversations à long terme.

* **Traitement asynchrone :** Les agents gèrent plusieurs tâches à la fois, améliorant l'efficacité.

* **Vérification des faits :** Ils se connectent à des sources de données en temps réel pour vérifier les informations.

* **Mathématiques améliorées :** Ils intègrent des outils pour gérer des calculs complexes.

* **Sortie cohérente :** Les agents standardisent les sorties des LLMs pour un formatage uniforme.

Pour aider à résoudre certaines des limitations mathématiques des LLMs, créons un agent IA qui construit une calculatrice en utilisant MathJS et les appels d'outils BaseAI.

## Prérequis

Dans ce tutoriel, j'utiliserai la pile technologique suivante :

* [MathJS](https://mathjs.org/) — une bibliothèque mathématique complète pour JavaScript et Node.js.

* [BaseAI](https://baseai.dev) — le framework web pour construire des agents IA localement.

* [Langbase](https://langbase.com) — la plateforme pour construire et déployer vos agents IA serverless.

* [OpenAI](https://openai.com) — pour obtenir la clé LLM pour le modèle préféré.

Vous devrez également :

* Vous inscrire sur Langbase pour obtenir accès à la clé API.

* Vous inscrire sur OpenAI pour générer la clé LLM pour le modèle que vous souhaitez utiliser (pour cette démonstration, j'utiliserai GPT-4o mini).

Commençons !

## Étape 1 : Créer un répertoire et initialiser npm

Pour commencer à créer un agent IA, vous devez créer un répertoire sur votre machine locale et installer toutes les dépendances de développement pertinentes. Vous pouvez le faire en naviguant vers celui-ci et en exécutant la commande suivante dans le terminal :

```bash
mkdir my-project

npm init -y

npm install dotenv mathjs
```

Cette commande créera un fichier `package.json` dans votre répertoire de projet avec des valeurs par défaut. Elle installera également le package `dotenv` pour lire les variables d'environnement à partir du fichier `.env`, et `mathjs` pour gérer les opérations mathématiques.

## Étape 2 : Créer un Pipe d'agent IA

Ensuite, nous allons créer un pipe d'agent IA. Les pipes sont différents des autres agents, car ils **sont des agents IA serverless avec des outils agentiques** qui peuvent fonctionner avec n'importe quel langage ou framework. Ils sont facilement déployables, et avec une seule API, ils vous permettent de connecter 100+ LLMs à n'importe quelle donnée pour construire n'importe quel workflow d'API de développeur.

Pour créer votre pipe d'agent IA, naviguez vers votre répertoire de projet. Exécutez la commande suivante :

```bash
npx baseai@latest pipe
```

En exécutant cette commande, vous verrez les invites suivantes :

```bash
BaseAI n'est pas installé mais est requis pour fonctionner. Souhaitez-vous l'installer ? Oui/Non

Nom du pipe ? pipe-with-tool

Description du pipe ? Un pipe d'agent IA qui peut appeler des outils

Statut du pipe ? Public/Privé

Prompt système ? Vous êtes un assistant IA utile
```

Une fois que vous avez terminé avec le nom, la description et le statut du pipe d'agent IA, tout sera configuré automatiquement pour vous. Votre pipe sera créé avec succès à `/baseai/pipes/pipe-with-tool.ts`.

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">Pipe est un agent IA serverless. Il a une mémoire agentique et des outils.</div>
</div>

## Étape 3 : Ajouter un fichier .env

Créez un fichier `.env` dans le répertoire racine de votre projet et ajoutez-y la clé API [OpenAI](https://platform.openai.com/api-keys) et Langbase. Vous pouvez accéder à votre clé API Langbase depuis [ici](https://langbase.com/docs/api-reference/api-keys).

## Étape 4 : Configurer le Pipe d'agent IA

Dans cette étape, nous allons configurer le pipe d'agent IA créé selon nos besoins.

Naviguez vers votre répertoire de projet et ouvrez le pipe d'agent IA que vous avez créé. Vous pouvez ajouter un prompt système au pipe si vous le souhaitez. Je vais utiliser `Vous êtes un assistant IA utile qui fonctionnera comme une calculatrice.` Voici à quoi cela ressemblera :

```typescript
import { PipeI } from '@baseai/core';

const pipePipeWithTool = (): PipeI => ({
   apiKey: process.env.LANGBASE_API_KEY!,
   name: 'pipe-with-tool',
   description: 'Un pipe d\'agent IA qui peut appeler des outils',
   status: 'private',
   model: 'openai:gpt-4o-mini',
   stream: true,
   json: false,
   store: true,
   moderate: true,
   top_p: 1,
   max_tokens: 1000,
   temperature: 0.7,
   presence_penalty: 1,
   frequency_penalty: 1,
   stop: [],
   tool_choice: 'auto',
   parallel_tool_calls: true,
   messages: [{ role: 'system', content: `Vous êtes un assistant IA utile qui fonctionnera comme une calculatrice.` }],
   variables: [],
   memory: [],
   tools: []
});

export default pipePipeWithTool;
```

## Étape 5 : Créer un outil Calculatrice

L'appel d'outil permet à un LLM d'utiliser des outils externes, tels que des fonctions, des APIs ou d'autres ressources, pour obtenir des informations ou effectuer des tâches au-delà de ses connaissances intégrées.

Dans cette étape, nous allons créer un **Outil Calculatrice** en utilisant les outils BaseAI. Cet outil gérera tous les calculs mathématiques dans votre projet, garantissant qu'ils sont sans erreur et fiables. L'outil est polyvalent et adapté à la fois aux calculs simples (par exemple, `5+7`) et aux calculs plus avancés (par exemple, `sin(pi/4) + log(10)`).

Il sera également particulièrement utile pour réduire les hallucinations, ce qu'il peut faire en déchargeant les calculs vers un outil externe. Cela évite les réponses incorrectes ou fabriquées que les LLMs pourraient autrement générer. Cela réduit également la probabilité d'obtenir des réponses incorrectes du LLM en revérifiant ou en recueillant des données supplémentaires pour garantir l'exactitude.

En utilisant les fonctionnalités d'appel d'outil intelligent et de mémoire de BaseAI, nous pouvons réduire les hallucinations de l'IA de **21%** tout en améliorant la capacité du modèle à auto-corriger ses sorties.

Ces améliorations sont utiles lorsqu'il s'agit d'expressions mathématiques complexes ou d'évaluations de formules et devraient vraiment améliorer la qualité et l'exactitude des réponses du LLM.

Pour créer un outil calculatrice dans votre projet qui sera responsable de l'exécution de tous les calculs sans erreur, exécutez cette commande dans votre terminal :

```bash
npx baseai@latest tool
```

Vous serez invité à fournir un nom et une description de l'outil dans votre terminal. Voici ce que je fournis :

```bash
Nom de l'outil ? Calculator

Description de l'outil ? Évaluer les expressions mathématiques
```

Votre outil sera créé à `/baseai/tools/calculator.ts`.

## Étape 6 : Configurer l'outil Calculatrice

Pour configurer l'outil, naviguez vers votre répertoire de projet et ouvrez l'outil que vous avez créé. Vous pouvez le trouver à `/baseai/tools/calculator.ts`.

Voici à quoi ressemblera le code :

```typescript
import { ToolI } from '@baseai/core';

export async function calculator() {
   // Ajoutez votre logique d'outil ici
   // Cette fonction sera appelée lorsque l'outil sera exécuté
}

const toolCalculator = (): ToolI => ({
   run: calculator,
   type: 'function' as const,
   function: {
       name: 'toolCalculator',
       description: 'Évaluer les expressions mathématiques',
       parameters: {}
   }
});

export default toolCalculator;
```

La clé `run` dans l'objet `toolCalculator` est la fonction qui sera exécutée lorsque l'outil sera appelé. Vous pouvez écrire votre logique pour obtenir les calculs mathématiques pour une fonction donnée.

Mettez à jour la description et le code de l'outil calculatrice en ajoutant des paramètres à la fonction calculatrice. Le LLM donnera des valeurs à ces paramètres lorsqu'il appellera l'outil. Et il importera même math depuis `mathjs`. Voici le code final :

```typescript
import * as math from 'mathjs';

export async function calculator({expression}: {expression: string}) {
   return math.evaluate(expression);
}

const toolCalculator = () => ({
   run: calculator,
   type: 'function' as const,
   function: {
       name: 'calculator',
       description:
           `Un outil qui peut évaluer des expressions mathématiques. ` +
           `Exemples d'expressions : ` +
           `'5.6 * (5 + 10.5)', '7.86 cm to inch', 'cos(80 deg) ^ 4'.`,
       parameters: {
           type: 'object',
           required: ['expression'],
           properties: {
               expression: {
                   type: 'string',
                   description: 'L\'expression mathématique à évaluer.',
               },
           },
       },
   },
});

export default toolCalculator;
```

## Étape 7 : Intégrer l'outil dans le Pipe d'agent IA

Dans cette étape, nous allons intégrer l'outil dans le pipe d'agent IA que nous avons créé. Pour cela, ouvrez le fichier pipe présent à `/baseai/pipes/pipe-with-tool.ts` et importez l'outil calculatrice en haut du fichier. Nous allons également appeler l'outil calculatrice dans le tableau des outils du pipe.

```typescript
import {PipeI} from '@baseai/core';
import toolCalculator from '../tools/calculator';

const pipeWithTools = (): PipeI => ({
   apiKey: process.env.LANGBASE_API_KEY!,
   name: 'pipe-with-tool',
   description: 'Un pipe d\'agent IA qui peut appeler des outils',
   status: 'public',
   model: 'openai:gpt-4o-mini',
   stream: false,
   json: false,
   store: true,
   moderate: true,
   top_p: 1,
   max_tokens: 1000,
   temperature: 0.7,
   presence_penalty: 1,
   frequency_penalty: 1,
   stop: [],
   tool_choice: 'auto',
   parallel_tool_calls: true,
   messages: [{role: 'system', content: `Vous êtes un assistant IA utile qui fonctionnera comme une calculatrice.`}],
   variables: [],
   memory: [],
   tools: [ toolCalculator()],
});

export default pipeWithTools;
```

## Étape 8 : Intégrer le Pipe d'agent IA dans Node.js

Maintenant, nous allons intégrer le pipe d'agent IA que vous avez créé dans le projet Node.js pour construire une interface de ligne de commande (CLI) interactive pour l'outil calculatrice. Ce projet Node.js servira de base pour tester et interagir avec le pipe d'agent IA (au début du tutoriel, nous avons configuré un projet Node.js en initialisant npm).

Maintenant, créez un fichier `index.ts` :

```bash
touch index.ts
```

Dans ce fichier TypeScript, importez le pipe d'agent IA que vous avez créé. Nous utiliserons le primitif pipe depuis `@baseai/core` pour exécuter le pipe.

Ajoutez le code suivant au fichier `index.ts` :

```typescript
import 'dotenv/config';
import { Pipe } from '@baseai/core';
import inquirer from 'inquirer';
import ora from 'ora';
import chalk from 'chalk';
import pipePipeWithTool from './baseai/pipes/pipe-with-tool';

const pipe = new Pipe(pipePipeWithTool());

async function main() {

   const initialSpinner = ora('Conversation avec l\'agent Math...').start();
   try {
       const { completion: calculatorTool} = await pipe.run({
           messages: [{ role: 'user', content: 'Bonjour' }],
       });
       initialSpinner.stop();
       console.log(chalk.cyan('Réponse de l\'agent générateur de rapports...'));
       console.log(calculatorTool);
   } catch (error) {
       initialSpinner.stop();
       console.error(chalk.red('Erreur lors du traitement de la demande initiale :'), error);
   }

   while (true) {
       const { userMsg } = await inquirer.prompt([
           {
               type: 'input',
               name: 'userMsg',
               message: chalk.blue('Entrez votre requête (ou tapez "exit" pour quitter) :'),
           },
       ]);

       if (userMsg.toLowerCase() === 'exit') {
           console.log(chalk.green('Au revoir !'));
           break;
       }

       const spinner = ora('Traitement de votre demande...').start();

       try {
           const { completion: reportAgentResponse } = await pipe.run({
               messages: [{ role: 'user', content: userMsg }],
           });

           spinner.stop();
           console.log(chalk.cyan('Agent :'));
           console.log(reportAgentResponse);
       } catch (error) {
           spinner.stop();
           console.error(chalk.red('Erreur lors du traitement de votre demande :'), error);
       }
   }
}

main();
```

Ce code crée une CLI interactive pour discuter avec un agent IA, en utilisant un pipe de la bibliothèque `@baseai/core` pour traiter les entrées de l'utilisateur. Voici ce qui se passe :

* Il importe les bibliothèques nécessaires telles que `dotenv` pour la configuration de l'environnement, `inquirer` pour les entrées de l'utilisateur, `ora` pour les spinners de chargement, et `chalk` pour les sorties colorées. Assurez-vous d'abord d'installer ces bibliothèques en utilisant cette commande dans votre terminal `npm install ora inquirer`.

* Un objet pipe est créé à partir de la bibliothèque BaseAI en utilisant un outil prédéfini appelé `pipe-with-tool`.

Dans la fonction `main()` :

* Un spinner démarre pendant qu'une conversation initiale avec l'agent IA est initiée avec le message 'Bonjour'.

* La réponse de l'IA est affichée.

* Une boucle s'exécute pour demander continuellement à l'utilisateur une entrée et envoyer des requêtes à l'agent IA.

* Les réponses de l'IA sont affichées, et le processus continue jusqu'à ce que l'utilisateur tape "exit".

## Étape 9 : Démarrer le serveur BaseAI

Pour exécuter le pipe d'agent IA localement, vous devez démarrer le serveur BaseAI. Exécutez la commande suivante dans votre terminal :

```bash
npx baseai@latest dev
```

## Étape 10 : Exécuter le Pipe d'agent IA

Exécutez le fichier `index.ts` en utilisant la commande suivante :

```bash
npx tsx index.ts
```

## Résultat

Dans votre terminal, vous serez invité à **"Entrez votre requête."** Par exemple, demandons : **"Qu'est-ce que 120 cm en pieds ?"** Les LLMs hallucinent généralement lors de la conversion en pieds. Mais grâce à l'auto-correction des appels d'outils du framework BaseAI, l'outil détecte et corrige ses propres erreurs.

Avec cette configuration, nous avons réussi à construire un agent IA qui utilise **MathJS** et les **appels d'outils BaseAI** pour éliminer les limitations mathématiques des LLMs.

Voici une démonstration du résultat final :

%[https://youtu.be/bBukL1Vte0g]

## Conclusion

Les grands modèles de langage (LLMs) ont souvent du mal avec le raisonnement mathématique en raison de leur concentration sur le langage, ce qui conduit à des erreurs fréquentes dans les calculs, en particulier avec les problèmes de mathématiques complexes.

Les agents IA étendent les capacités des LLMs en intégrant des appels d'outils. Ils gèrent les données en temps réel, assurent des sorties plus cohérentes et réduisent les hallucinations.

En incorporant MathJS et les appels d'outils via le framework BaseAI, les développeurs peuvent créer des agents IA serverless personnalisés appelés pipes qui servent de calculatrices fiables et répondent aux limitations inhérentes des LLMs.