---
title: Comment créer un agent IA Serverless pour générer des emails de prospection
  pour votre emploi de rêve
subtitle: ''
author: Maham Codes
co_authors: []
series: null
date: '2025-02-19T13:41:44.886Z'
originalURL: https://freecodecamp.org/news/build-a-serverless-ai-agent-for-generating-cold-emails
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1739971173263/869c0c1c-9b45-48af-a1d1-0982436b8630.png
tags:
- name: AI
  slug: ai
- name: llm
  slug: llm
- name: ai-agent
  slug: ai-agent
seo_title: Comment créer un agent IA Serverless pour générer des emails de prospection
  pour votre emploi de rêve
seo_desc: 'Cold emails can make a huge difference in your job search, but writing
  the perfect one takes time. You need to match your skills with the job description,
  find the right tone, and do it over and over again—it’s exhausting.

  This guide will walk you th...'
---

Les emails de prospection peuvent faire une énorme différence dans votre recherche d'emploi, mais écrire le parfait prend du temps. Vous devez faire correspondre vos compétences avec la description de poste, trouver le bon ton, et le faire encore et encore—c'est épuisant.

Ce guide vous expliquera comment créer un agent générateur d'emails de prospection en utilisant des agents de mémoire serverless de Langbase pour automatiser ce processus entier. Nous intégrerons l'agent de mémoire dans un projet Node.js, lui permettant de lire votre CV, d'analyser la description de poste, et de générer un email de prospection personnalisé et percutant en quelques secondes.

### Voici ce que je vais couvrir :

1. [Les grands modèles de langage (LLMs) sont sans état par nature](#heading-les-grands-modeles-de-langage-llms-sont-sans-etat-par-nature)

2. [Qu'est-ce que les agents de mémoire ?](#heading-quest-ce-que-les-agents-de-memoire)

3. [Prérequis](#heading-prerequis)

4. [Architecture de référence](#heading-architecture-de-reference)

5. [Étape 1 : Créer un répertoire et initialiser npm](#heading-etape-1-creer-un-repertoire-et-initialiser-npm)

6. [Étape 2 : Créer un agent Pipe serverless](#heading-etape-2-creer-un-agent-pipe-serverless)

7. [Étape 3 : Ajouter un fichier .env](#heading-etape-3-ajouter-un-fichier-env)

8. [Étape 4 : Créer un agent de mémoire serverless](#heading-etape-4-creer-un-agent-de-memoire-serverless)

9. [Étape 5 : Ajouter des documents à l'agent de mémoire](#heading-etape-5-ajouter-des-documents-a-lagent-de-memoire)

10. [Étape 6 : Générer des embeddings de mémoire](#heading-etape-6-generer-des-embeddings-de-memoire)

    * [Comprendre les embeddings de mémoire](#heading-comprendre-les-embeddings-de-memoire)

    * [Comment générer des embeddings ?](#heading-comment-generer-des-embeddings)

11. [Étape 7 : Intégrer la mémoire dans l'agent Pipe](#heading-etape-7-integrer-la-memoire-dans-lagent-pipe)

12. [Étape 8 : Intégrer l'agent de mémoire dans Node.js](#heading-etape-8-integrer-lagent-de-memoire-dans-nodejs)

13. [Étape 9 : Démarrer le serveur BaseAI](#heading-etape-9-demarrer-le-serveur-baseai)

14. [Étape 10 : Exécuter l'agent de mémoire](#heading-etape-10-executer-lagent-de-memoire)

15. [Le résultat](#heading-le-resultat)

## Les grands modèles de langage (LLMs) sont sans état par nature

Les LLMs (grands modèles de langage) sont sans état car ils ne conservent aucune mémoire des interactions précédentes ou du contexte des requêtes passées au-delà de l'entrée qui leur est donnée dans une session. Chaque fois qu'un LLM traite une invite, il fonctionne sur cette invite spécifique sans aucun historique des précédentes.

Cette nature sans état permet au modèle de traiter chaque demande de manière indépendante, ce qui simplifie son architecture et son processus de formation. Mais cela signifie également que, sans mécanismes comme le RAG (Retrieval-Augmented Generation) ou la mémoire (long terme), les LLMs ne peuvent pas transmettre d'informations d'une interaction à l'autre.

Pour introduire une continuité ou un contexte, les développeurs peuvent implémenter des systèmes externes pour gérer et injecter du contexte, mais le modèle lui-même ne "se souvient" de rien entre les requêtes.

### Comment résoudre ce problème ?

En intégrant les **agents de mémoire** de Langbase, nous pouvons donner aux LLMs une mémoire à long terme, leur permettant de stocker, récupérer et utiliser des informations de manière dynamique, les rendant ainsi beaucoup plus utiles pour des applications réelles.

## Qu'est-ce que les agents de mémoire ?

Les [agents de mémoire serverless de Langbase](https://langbase.com/docs/memory) (solution de mémoire à long terme) sont conçus pour acquérir, traiter, conserver et récupérer des informations de manière transparente. Ils attachent dynamiquement des données privées à n'importe quel LLM, permettant des réponses contextuelles en temps réel et réduisant les hallucinations.

Ces agents combinent le stockage vectoriel, la génération augmentée par récupération (RAG) et l'accès à Internet pour créer une API de recherche de contexte puissante et gérée. Les développeurs peuvent les utiliser pour construire des applications IA plus intelligentes et plus capables.

Dans une configuration RAG, la mémoire, lorsqu'elle est connectée directement à un agent Pipe de Langbase, devient un agent de mémoire. Ce couplage donne au LLM la capacité de récupérer des données pertinentes et de fournir des réponses précises et contextuellement exactes, répondant aux limitations des LLMs en matière de gestion de données privées.

Les agents de mémoire garantissent un stockage sécurisé de la mémoire locale. Les données utilisées pour créer des embeddings de mémoire restent protégées, traitées dans des environnements sécurisés et envoyées à l'extérieur uniquement si explicitement configurées. L'accès est strictement contrôlé via des clés API, garantissant que les informations sensibles restent en sécurité.

Notez que pipe est un agent IA serverless. Il dispose d'une mémoire agentique et d'outils.

## Prérequis

Avant de commencer à créer un agent générateur d'emails de prospection, vous devrez avoir la configuration et les outils suivants prêts à l'emploi.

Dans ce tutoriel, j'utiliserai cette stack technologique :

* [BaseAI](http://baseai.dev/) — le framework web pour construire des agents IA localement.

* [Langbase](http://langbase.com/) — la plateforme pour construire et déployer vos agents IA serverless.

* [OpenAI](https://openai.com/) — pour obtenir la clé LLM pour le modèle préféré.

Vous devrez également :

* Vous inscrire sur Langbase pour obtenir accès à la clé API.

* Vous inscrire sur OpenAI pour générer la clé LLM pour le modèle que vous souhaitez utiliser (pour cette démonstration, j'utiliserai GPT-4o mini). Vous pouvez générer la clé [ici](https://platform.openai.com/api-keys).

## Architecture de référence

Voici une représentation diagramme de l'ensemble du processus de construction d'un agent IA serverless pour générer des emails de prospection pour les candidatures à des emplois :

![Architecture de référence des agents de mémoire en fonctionnement](https://cdn.hashnode.com/res/hashnode/image/upload/v1739900463621/e2b6753e-287f-4d69-b453-36d50f316fb8.png align="center")

Commençons à construire l'agent !

## Étape 1 : Créer un répertoire et initialiser npm

Pour commencer à créer un agent IA serverless qui génère des emails de prospection pour une offre d'emploi, vous devez créer un répertoire dans votre machine locale et y installer toutes les dépendances de développement pertinentes. Vous pouvez le faire en naviguant vers celui-ci et en exécutant la commande suivante dans le terminal :

```bash
mkdir my-project
npm init -y
npm install dotenv
```

Cette commande créera un fichier package.json dans votre répertoire de projet avec des valeurs par défaut. Elle installera également le package `dotenv` pour lire les variables d'environnement depuis le fichier `.env`.

## Étape 2 : Créer un agent Pipe serverless

Ensuite, nous allons créer un [agent pipe](https://langbase.com/docs/pipe/quickstart). Les Pipes sont différents des autres agents, car ils sont des agents IA serverless avec des outils agentiques qui peuvent fonctionner avec n'importe quel langage ou framework. Ils sont facilement déployables, et avec une seule API, ils vous permettent de connecter plus de 250 LLMs à n'importe quelle donnée pour construire n'importe quel workflow d'API de développeur.

Pour créer votre pipe d'agent IA, naviguez vers votre répertoire de projet. Exécutez la commande suivante :

```bash
npx baseai@latest pipe
```

Lors de l'exécution, vous verrez les invites suivantes :

```bash
BaseAI n'est pas installé mais est requis pour fonctionner. Souhaitez-vous l'installer ? Oui/Non
Nom du pipe ? email-generator-agent
Description du pipe ? Génère des emails pour votre emploi de rêve en quelques secondes
Statut du pipe ? Public/Privé
Invite système ? Vous êtes un assistant IA utile
```

Une fois que vous avez terminé avec le nom, la description et le statut du pipe de l'agent IA, tout sera configuré automatiquement pour vous. Votre pipe sera créé avec succès à `/baseai/pipes/email-generator-agent.ts`.

## Étape 3 : Ajouter un fichier .env

Créez un fichier `.env` dans le répertoire racine de votre projet et ajoutez-y les clés API OpenAI et Langbase. Vous pouvez accéder à votre clé API Langbase depuis [ici](https://langbase.com/docs/api-reference/api-keys).

## Étape 4 : Créer un agent de mémoire serverless

Ensuite, nous allons créer une mémoire puis l'attacher au Pipe pour en faire un agent de mémoire. Pour ce faire, exécutez cette commande dans votre terminal :

```bash
npx baseai@latest memory
```

Lors de l'exécution de cette commande, vous verrez les invites suivantes :

```bash
Nom de la mémoire ? email-generator-memory
Description de la mémoire ? Contient mon CV
Souhaitez-vous créer une mémoire à partir du dépôt git du projet actuel ? Oui/Non
```

Après cela, tout sera configuré automatiquement pour vous et vous pourrez accéder à votre mémoire créée avec succès à `/baseai/memory/email-generator-memory.ts`.

## Étape 5 : Ajouter des documents à l'agent de mémoire

À l'intérieur de `/baseai/memory/email-generator-memory.ts`, vous verrez un autre dossier appelé documents. C'est là que vous stockerez les fichiers que vous souhaitez que votre agent IA accède. Enregistrons votre CV sous forme de fichier `.pdf` ou `.txt`. Ensuite, je vais le convertir en fichier markdown et le placer dans le répertoire `/baseai/memory/email-generator-memory/documents`.

Cette étape garantit que l'agent de mémoire peut traiter et récupérer des informations à partir de vos documents, rendant l'agent IA capable de générer des emails de prospection précis basés sur les expériences et compétences fournies dans le CV joint.

## Étape 6 : Générer des embeddings de mémoire

Avec vos documents ajoutés à la mémoire, l'étape suivante consiste à générer des embeddings de mémoire. Mais avant cela, laissez-moi expliquer rapidement ce que sont les embeddings et pourquoi ils sont importants.

### Comprendre les embeddings de mémoire

Les embeddings de mémoire sont des représentations numériques de vos documents qui permettent à une IA de saisir le contexte, les relations et le sens dans le texte. Ils agissent comme un pont, convertissant les données brutes en un format structuré que l'IA peut traiter pour la recherche sémantique et la récupération.

Sans embeddings, les agents IA ne pourraient pas connecter efficacement les requêtes des utilisateurs avec le contenu pertinent. La génération d'embeddings crée un index recherchable, permettant à l'agent de mémoire de fournir des réponses précises et contextuellement conscientes de manière efficace.

### Comment générer des embeddings

Pour générer des embeddings pour vos documents, exécutez la commande suivante dans votre terminal :

```bash
npx baseai@latest embed -m email-generator-memory
```

Votre mémoire est maintenant prête à être connectée à un Pipe (agent de mémoire), permettant à votre agent IA de récupérer des réponses précises et contextuellement conscientes à partir de vos documents.

## Étape 7 : Intégrer la mémoire dans l'agent Pipe

Ensuite, vous devez attacher la mémoire que vous avez créée à votre agent Pipe pour en faire un agent de mémoire. Pour cela, allez dans `/baseai/pipes/email-generator-agent.ts`. Voici à quoi cela ressemblera pour le moment :

```typescript
import { PipeI } from '@baseai/core';

const pipePipeWithMemory = (): PipeI => ({
  apiKey: process.env.LANGBASE_API_KEY!, // Remplacez par votre clé API https://langbase.com/docs/api-reference/api-keys
  name: 'email-generator-agent',
  description: 'Génère des emails pour votre emploi de rêve en quelques secondes',
  status: 'public',
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
  parallel_tool_calls: false,
  messages: [
    { role: 'system', content: Vous êtes un assistant IA utile. }],
  variables: [],
  memory: [],
  tools: []
});

export default pipePipeWithMemory;
```

Maintenant, intégrez la mémoire dans le pipe en l'important en haut et en l'appelant en tant que fonction dans le tableau `memory`. Ajoutez également ce qui suit dans le contenu des messages :

```bash
Sur la base de la description de poste et de mon CV joint, rédigez un email de prospection convaincant adapté au poste, mettant en avant mes compétences, réalisations et expériences les plus pertinentes. Assurez-vous que le ton est professionnel mais accessible, et incluez un appel à l'action fort pour un suivi ou un entretien.
```

Voici à quoi ressemblera le code après avoir fait tout cela :

```typescript
import { PipeI } from '@baseai/core';
import emailGeneratorMemoryMemory from '../memory/email-generator-memory';

const pipeEmailGeneratorAgent = (): PipeI => ({
  // Remplacez par votre clé API https://langbase.com/docs/api-reference/api-keys
  apiKey: process.env.LANGBASE_API_KEY!,
  name: 'email-generator-agent',
  description: 'Génère des emails pour votre emploi de rêve en quelques secondes',
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
  messages: [{ role: 'system', content: Sur la base de la description de poste et de mon CV joint, rédigez un email de prospection convaincant adapté au poste, mettant en avant mes compétences, réalisations et expériences les plus pertinentes. Assurez-vous que le ton est professionnel mais accessible, et incluez un appel à l'action fort pour un suivi ou un entretien. }],
  variables: [],
  memory: [emailGeneratorMemoryMemory()],
  tools: []
});

export default pipeEmailGeneratorAgent;
```

## Étape 8 : Intégrer l'agent de mémoire dans Node.js

Maintenant, nous allons intégrer l'agent de mémoire que vous avez créé dans le projet Node.js pour construire une interface de ligne de commande (CLI) interactive pour le document joint. Ce projet Node.js servira de base pour tester et interagir avec l'agent de mémoire (au début du tutoriel, nous avons configuré un projet Node.js en initialisant npm).

Maintenant, créez un fichier index.ts :

```bash
touch index.ts
```

Dans ce fichier TypeScript, importez l'agent pipe que vous avez créé. Nous utiliserons le primitif pipe de `@baseai/core` pour exécuter le pipe.

Ajoutez le code suivant au fichier `index.ts` :

```typescript
import 'dotenv/config';
import { Pipe } from '@baseai/core';
import inquirer from 'inquirer';
import ora from 'ora';
import chalk from 'chalk';
import pipeEmailGeneratorAgent from './baseai/pipes/email-generator-agent';

const pipe = new Pipe(pipeEmailGeneratorAgent());

async function main() {

  const initialSpinner = ora('Conversation avec l\'agent de mémoire...').start();
  try {
    const { completion: calculatorTool} = await pipe.run({
      messages: [{ role: 'user', content: 'Bonjour' }],
    });
    initialSpinner.stop();
    console.log(chalk.cyan('Réponse de l\'agent générateur de rapport...'));
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

Ce code crée une CLI interactive pour discuter avec un agent IA, en utilisant un pipe de la bibliothèque `@baseai/core` pour traiter l'entrée de l'utilisateur. Voici ce qui se passe :

* Il importe les bibliothèques nécessaires telles que `dotenv` pour la configuration de l'environnement, `inquirer` pour l'entrée de l'utilisateur, `ora` pour les spinners de chargement, et `chalk` pour la sortie colorée. Assurez-vous d'abord d'installer ces bibliothèques en utilisant cette commande dans votre terminal : `npm install ora inquirer`.

* Un objet pipe est créé à partir de la bibliothèque BaseAI en utilisant une mémoire prédéfinie appelée `email-generator-agent`.

Dans la fonction `main()` :

* Un spinner démarre pendant qu'une conversation initiale avec l'agent IA est initiée avec le message 'Bonjour'.

* La réponse de l'IA est affichée.

* Une boucle s'exécute pour demander continuellement à l'utilisateur une entrée et envoyer des requêtes à l'agent IA.

* Les réponses de l'IA sont affichées, et le processus continue jusqu'à ce que l'utilisateur tape "exit".

## Étape 9 : Démarrer le serveur BaseAI

Pour exécuter l'agent de mémoire localement, vous devez d'abord démarrer le serveur BaseAI. Exécutez la commande suivante dans votre terminal :

```bash
npx baseai@latest dev
```

## Étape 10 : Exécuter l'agent de mémoire

Exécutez le fichier `index.ts` en utilisant la commande suivante :

```bash
npx tsx index.ts
```

## Le résultat

Dans votre terminal, vous serez invité à "Entrez votre requête". Par exemple, collons une description de poste et demandons de générer un email de notre côté montrant de l'intérêt. Et il nous donnera la réponse avec les bonnes sources/citations également.

Avec cette configuration, nous avons construit un agent générateur d'emails de prospection qui utilise la puissance des LLMs et des agents de mémoire de Langbase pour surmonter les limitations des LLMs, garantissant des réponses précises sans hallucinations sur les données privées.

Voici une démonstration du résultat final :

%[https://youtu.be/ns7UqX6Ycs8]

Merci d'avoir lu !

Connectez-vous avec moi par 👌 :

* En vous abonnant à ma chaîne [YouTube](https://www.youtube.com/@AIwithMahamCodes). Si vous souhaitez apprendre sur l'IA et les agents.

* En vous abonnant à ma newsletter gratuite ["The Agentic Engineer"](https://mahamcodes.substack.com/) où je partage toutes les dernières nouvelles/tendances/emplois en IA et agents, et bien plus encore.

* Suivez-moi sur [X (Twitter)](https://x.com/MahamDev).