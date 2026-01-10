---
title: Comment utiliser les agents de mémoire Langbase pour transformer n'importe
  quel LLM en IA conversationnelle pour vos documents
subtitle: ''
author: Maham Codes
co_authors: []
series: null
date: '2025-01-17T21:17:39.296Z'
originalURL: https://freecodecamp.org/news/how-to-use-langbase-memory-agents
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1737148633610/45e0af50-6026-4953-8e1a-953a7d5b6df6.png
tags:
- name: llm
  slug: llm
- name: ai agents
  slug: ai-agents
seo_title: Comment utiliser les agents de mémoire Langbase pour transformer n'importe
  quel LLM en IA conversationnelle pour vos documents
seo_desc: It’s 2025, and Large Language Models (LLMs) still can’t access your private
  data. Ask them something personal, and they’ll either guess or give you the wrong
  answer. That’s the limitation—they’re trained on public information and don’t have
  access to...
---

Nous sommes en 2025, et les grands modèles de langage (LLM) ne peuvent toujours pas accéder à vos données privées. Posez-leur une question personnelle, et ils devineront ou vous donneront la mauvaise réponse. C'est la limitation : ils sont formés sur des informations publiques et n'ont pas accès à votre contexte privé.

Les agents de mémoire résolvent ce problème en reliant de manière sécurisée vos données privées à n'importe quel LLM en temps réel. Dans ce tutoriel, je vais vous montrer comment transformer un LLM en une IA conversationnelle qui discute avec vos documents personnels en utilisant les agents de mémoire Langbase.

### Voici ce que nous allons couvrir :

1. [Qu'est-ce que les agents de mémoire ?](#heading-quest-ce-que-les-agents-de-memoire)
    
2. [Sécuriser vos données avec les agents de mémoire](#heading-securiser-vos-donnees-avec-les-agents-de-memoire)
    
3. [Cas d'utilisation des agents de mémoire](#heading-cas-dutilisation-des-agents-de-memoire)
    
4. [Prérequis](#heading-prerequis)
    
5. [Étape 1 : Créer un répertoire et initialiser npm](#heading-etape-1-creer-un-repertoire-et-initialiser-npm)
    
6. [Étape 2 : Créer un agent Pipe](#heading-etape-2-creer-un-agent-pipe)
    
7. [Étape 3 : Ajouter un fichier .env](#heading-etape-3-ajouter-un-fichier-env)
    
8. [Étape 4 : Créer un agent de mémoire](#heading-etape-4-creer-un-agent-de-memoire)
    
9. [Étape 5 : Ajouter des documents à l'agent de mémoire](#heading-etape-5-ajouter-des-documents-a-lagent-de-memoire)
    
10. [Étape 6 : Générer des embeddings de mémoire](#heading-etape-6-generer-des-embeddings-de-memoire)
    
    * [Qu'est-ce que les embeddings de mémoire ?](#heading-quest-ce-que-les-embeddings-de-memoire)
        
    * [Pourquoi avez-vous besoin d'embeddings de mémoire ?](#heading-pourquoi-avez-vous-besoin-dembeddings-de-memoire)
        
    * [Comment générer des embeddings](#heading-comment-generer-des-embeddings)
        
11. [Étape 7 : Intégrer la mémoire dans l'agent Pipe](#heading-etape-7-integrer-la-memoire-dans-lagent-pipe)
    
12. [Étape 8 : Intégrer l'agent de mémoire dans Node.js](#heading-etape-8-integrer-lagent-de-memoire-dans-nodejs)
    
13. [Étape 9 : Démarrer le serveur BaseAI](#heading-etape-9-demarrer-le-serveur-baseai)
    
14. [Étape 10 : Exécuter l'agent de mémoire](#heading-etape-10-executer-lagent-de-memoire)
    
15. [Le résultat](#heading-le-resultat)
    

## Qu'est-ce que les agents de mémoire ?

La mémoire est ce qui rend les interactions significatives. C'est ainsi que les systèmes peuvent se souvenir de ce qui s'est passé auparavant, un aspect clé pour construire des agents IA véritablement intelligents.

Voici le problème : les LLM peuvent sembler humains, mais ils n'ont pas de mémoire intégrée. Ils sont **stateless par conception**. Pour les rendre utiles pour des tâches réelles, vous devez ajouter de la mémoire. C'est là que les agents de mémoire interviennent.

Les [agents de mémoire Langbase](https://langbase.com/docs/memory) (solution de mémoire à long terme) sont conçus pour **acquérir, traiter, retenir et récupérer** des informations de manière transparente. Ils attachent dynamiquement des données privées à n'importe quel LLM, permettant des réponses contextuelles en temps réel et réduisant les hallucinations.

Ces agents combinent le stockage vectoriel, la génération augmentée par récupération (RAG), et l'accès à Internet pour créer une API de recherche de contexte puissante et gérée. Les développeurs peuvent les utiliser pour construire des applications IA plus intelligentes et plus capables.

Dans une configuration RAG, la mémoire - lorsqu'elle est connectée directement à un [agent Pipe Langbase](https://langbase.com/docs/pipe) - devient un **agent de mémoire**. Ce couplage donne au LLM la capacité de récupérer des données pertinentes et de fournir des réponses précises et contextuellement exactes, répondant aux limitations des LLM lorsqu'il s'agit de gérer des données privées.

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">Pipe est un agent IA serverless. Il dispose d'une mémoire agentique et d'outils.</div>
</div>

Voici une représentation diagramme de l'ensemble du processus :

![Diagramme architectural du flux de travail des agents de mémoire](https://cdn.hashnode.com/res/hashnode/image/upload/v1736776247313/6d66a33b-bf82-4a8e-96d7-1d8a6382b863.png align="center")

## Sécuriser vos données avec les agents de mémoire

Les agents de mémoire priorisent la sécurité des données en gardant les informations privées isolées et traitées localement ou dans des environnements sécurisés. Les données utilisées pour créer des embeddings de mémoire ne sont pas envoyées à des serveurs externes sauf si explicitement configuré, garantissant que les informations sensibles restent protégées.

De plus, l'accès au système de mémoire est strictement contrôlé par des clés API et des permissions, empêchant tout accès non autorisé. Cette configuration améliore non seulement les capacités de l'IA, mais maintient également la confiance des utilisateurs en protégeant leurs données.

## Cas d'utilisation des agents de mémoire

Voici quelques applications pratiques de ces agents :

* **Support client** : Fournir une assistance personnalisée et contextuelle en rappelant l'historique des interactions.
    
* **Recherche de documents** : Permettre une recherche sémantique rapide dans de grandes bases de données, manuels ou FAQ.
    
* **Assistance de code** : Fournir une documentation spécifique au projet et des conseils de débogage pour les développeurs.
    
* **Gestion des connaissances** : Centraliser et récupérer des informations internes pour les équipes de manière efficace.
    
* **Éducation et formation** : Fournir aux étudiants ou employés des matériaux de formation personnalisés, suivre les progrès et répondre aux questions basées sur les ressources stockées.
    
* **Santé** : Récupérer de manière sécurisée les dossiers des patients ou l'historique médical pour un support précis.
    
* **Flux de travail collaboratifs** : Suivre l'historique des projets et s'intégrer avec des outils pour l'alignement des équipes.
    
* **Conformité légale** : Référencer des directives pour garantir des décisions précises et conformes aux réglementations.
    

Les nombreux cas d'utilisation rendus possibles par les agents de mémoire ouvrent de nouvelles possibilités et changent ce que l'**Intelligence Générale Artificielle (AGI)** peut faire.

## Prérequis

Avant de commencer à créer un agent de mémoire qui discute avec vos documents, vous devrez avoir la configuration et les outils suivants prêts à l'emploi.

Dans ce tutoriel, j'utiliserai la pile technologique suivante :

* [BaseAI](http://baseai.dev) — le framework web pour construire des agents IA localement.
    
* [Langbase](http://langbase.com) — la plateforme pour construire et déployer vos agents IA serverless.
    
* [OpenAI](https://openai.com/) — pour obtenir la clé LLM pour le modèle préféré.
    

Vous devrez également :

* Vous inscrire sur Langbase pour obtenir accès à la clé API.
    
* Vous inscrire sur OpenAI pour générer la clé LLM pour le modèle que vous souhaitez utiliser (pour cette démonstration, j'utiliserai GPT-4o mini).
    

Commençons !

## Étape 1 : Créer un répertoire et initialiser npm

Pour commencer à créer un agent de mémoire qui discute avec vos documents, vous devez créer un répertoire dans votre machine locale et installer toutes les dépendances de développement pertinentes. Vous pouvez faire cela en naviguant vers celui-ci et en exécutant la commande suivante dans le terminal :

```bash
mkdir my-project
npm init -y
npm install dotenv
```

Cette commande créera un fichier `package.json` dans votre répertoire de projet avec des valeurs par défaut. Elle installera également le package `dotenv` pour lire les variables d'environnement depuis le fichier `.env`.

## Étape 2 : Créer un agent Pipe

Ensuite, nous allons créer un agent pipe. Les pipes sont différents des autres agents, car ils sont des agents IA serverless avec des outils agentiques qui peuvent fonctionner avec n'importe quel langage ou framework. Ils sont facilement déployables, et avec une seule API, ils vous permettent de connecter 100+ LLM à n'importe quelle donnée pour construire n'importe quel flux de travail d'API de développeur.

Pour créer votre pipe d'agent IA, naviguez vers votre répertoire de projet. Exécutez la commande suivante :

```bash
npx baseai@latest pipe
```

Lors de l'exécution, vous verrez les invites suivantes :

```bash
BaseAI n'est pas installé mais est requis pour fonctionner. Souhaitez-vous l'installer ? Oui/Non
Nom du pipe ?  pipe-with-memory
Description du pipe ? Pipe attaché à une mémoire
Statut du pipe ? Public/Privé
Prompt système ? Vous êtes un assistant IA utile
```

Une fois que vous avez terminé avec le nom, la description et le statut du pipe de l'agent IA, tout sera configuré automatiquement pour vous. Votre pipe sera créé avec succès à `/baseai/pipes/pipe-with-memory.ts`.

## Étape 3 : Ajouter un fichier .env

Créez un fichier `.env` dans le répertoire racine de votre projet et ajoutez-y la clé API [OpenAI](https://platform.openai.com/api-keys) et Langbase. Vous pouvez accéder à votre clé API Langbase depuis [ici](https://langbase.com/docs/api-reference/api-keys).

## Étape 4 : Créer un agent de mémoire

Ensuite, nous allons créer une mémoire puis l'attacher au Pipe pour en faire un agent de mémoire. Pour cela, exécutez cette commande dans votre terminal :

```bash
npx baseai@latest memory
```

Lors de l'exécution de cette commande, vous verrez les invites suivantes :

```bash
Nom de la mémoire ?  chat-with-docs-agent
Description de la mémoire ? FAQs docs
Souhaitez-vous créer une mémoire à partir du dépôt git actuel du projet ? Oui/Non
```

Après cela, tout sera configuré automatiquement pour vous et vous pourrez accéder à votre mémoire créée avec succès à `/baseai/memory/chat-with-docs-agent.ts`.

## Étape 5 : Ajouter des documents à l'agent de mémoire

À l'intérieur de `/baseai/memory/chat-with-docs-agent.ts`, vous verrez un autre dossier appelé documents. C'est là que vous stockerez les fichiers que vous souhaitez que votre agent IA accède. Pour cette démonstration, j'enregistrerai la page FAQs de Pipe sous forme de fichier `.pdf` ou `.txt`. Ensuite, je le convertirai en fichier markdown et le placerai dans le répertoire `baseai/memory/chat-with-docs/documents`.

Cette étape garantit que l'agent de mémoire peut **traiter et récupérer** des informations à partir de vos documents, rendant l'agent IA capable de répondre aux requêtes en fonction du contenu que vous fournissez.

## Étape 6 : Générer des embeddings de mémoire

Maintenant que vous avez ajouté des documents à la mémoire, l'étape suivante consiste à générer des embeddings de mémoire. Mais d'abord, que sont exactement les embeddings et pourquoi sont-ils essentiels ?

### Qu'est-ce que les embeddings de mémoire ?

Les embeddings sont des représentations numériques de vos documents qui permettent à l'IA de comprendre le contexte et les relations entre les mots, les phrases et les sentences. Pensez aux embeddings comme un moyen de traduire vos documents dans une langue que l'IA peut traiter pour la recherche sémantique et la récupération.

### Pourquoi avez-vous besoin d'embeddings de mémoire ?

Sans embeddings, l'agent IA ne pourrait pas faire correspondre les requêtes des utilisateurs avec le contenu pertinent de vos documents. En générant des embeddings, vous créez essentiellement un index recherchable qui permet des réponses précises et efficaces de l'agent de mémoire.

### Comment générer des embeddings

Pour générer des embeddings pour vos documents, exécutez la commande suivante dans votre terminal :

```bash
npx baseai@latest embed -m chat-with-docs-agent
```

Votre mémoire est maintenant prête à être connectée à un Pipe (agent de mémoire), permettant à votre agent IA de récupérer des réponses précises et contextuelles à partir de vos documents.

## Étape 7 : Intégrer la mémoire dans l'agent Pipe

Ensuite, vous devez attacher la mémoire que vous avez créée à votre agent Pipe pour en faire un agent de mémoire. Pour cela, allez dans `/baseai/pipes/pipe-with-memory.ts`. Voici à quoi cela ressemblera pour le moment :

```typescript
import { PipeI } from '@baseai/core';

const pipePipeWithMemory = (): PipeI => ({
	apiKey: process.env.LANGBASE_API_KEY!, // Remplacez par votre clé API https://langbase.com/docs/api-reference/api-keys
	name: 'pipe-with-memory',
	description: 'Pipe attaché à une mémoire',
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
		{ role: 'system', content: `Vous êtes un assistant IA utile.` }],
	variables: [],
    memory: [],
    tools: []
});

export default pipePipeWithMemory;
```

Maintenant, intégrez la mémoire dans le pipe en l'important en haut et en l'appelant en tant que fonction dans le tableau `memory`. Voici à quoi ressemblera le code après avoir fait tout cela :

```typescript
import { PipeI } from '@baseai/core';
import chatWithDocsAgentMemory from '../memory/chat-with-docs-agent';

const pipePipeWithMemory = (): PipeI => ({
	apiKey: process.env.LANGBASE_API_KEY!, // Remplacez par votre clé API https://langbase.com/docs/api-reference/api-keys
	name: 'pipe-with-memory',
	description: 'Pipe attaché à une mémoire',
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
		{ role: 'system', content: `Vous êtes un assistant IA utile.` }],
	variables: [],
    memory: [chatWithDocsAgentMemory()],
    tools: []
});

export default pipePipeWithMemory;
```

## Étape 8 : Intégrer l'agent de mémoire dans Node.js

Maintenant, nous allons intégrer l'agent de mémoire que vous avez créé dans le projet Node.js pour construire une interface de ligne de commande (CLI) interactive pour le document attaché. Ce projet Node.js servira de base pour tester et interagir avec l'agent de mémoire (au début du tutoriel, nous avons configuré un projet Node.js en initialisant npm).

Maintenant, créez un fichier `index.ts` :

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
import pipePipeWithMemory from './baseai/pipes/pipe-with-memory';

const pipe = new Pipe(pipePipeWithMemory());

async function main() {

   const initialSpinner = ora('Conversation avec l\'agent de mémoire...').start();
   try {
       const { completion: calculatorTool} = await pipe.run({
           messages: [{ role: 'user', content: 'Bonjour' }],
       });
       initialSpinner.stop();
       console.log(chalk.cyan('Réponse de l\'agent générateur de rapports...'));
       console.log(calculatorTool);
   } catch (error) {
       initialSpinner.stop();
       console.error(chalk.red('Erreur lors du traitement de la requête initiale :'), error);
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


       const spinner = ora('Traitement de votre requête...').start();


       try {
           const { completion: reportAgentResponse } = await pipe.run({
               messages: [{ role: 'user', content: userMsg }],
           });


           spinner.stop();
           console.log(chalk.cyan('Agent :'));
           console.log(reportAgentResponse);
       } catch (error) {
           spinner.stop();
           console.error(chalk.red('Erreur lors du traitement de votre requête :'), error);
       }
   }
}

main();
```

Ce code crée une CLI interactive pour discuter avec un agent IA, en utilisant un pipe de la bibliothèque `@baseai/core` pour traiter les entrées de l'utilisateur. Voici ce qui se passe :

* Il importe les bibliothèques nécessaires telles que `dotenv` pour la configuration de l'environnement, `inquirer` pour les entrées de l'utilisateur, `ora` pour les spinners de chargement, et `chalk` pour les sorties colorées. Assurez-vous d'installer d'abord ces bibliothèques en utilisant cette commande dans votre terminal : `npm install ora inquirer`.
    
* Un objet pipe est créé à partir de la bibliothèque BaseAI en utilisant une mémoire prédéfinie appelée `pipe-with-memory`.
    

Dans la fonction `main()` :

* Un spinner commence pendant qu'une conversation initiale avec l'agent IA est initiée avec le message 'Bonjour'.
    
* La réponse de l'IA est affichée.
    
* Une boucle s'exécute pour demander continuellement à l'utilisateur une entrée et envoyer des requêtes à l'agent IA.
    
* Les réponses de l'IA sont affichées, et le processus continue jusqu'à ce que l'utilisateur tape "exit".
    

## Étape 9 : Démarrer le serveur BaseAI

Pour exécuter l'agent de mémoire localement, vous devez d'abord démarrer le serveur BaseAI. Exécutez la commande suivante dans votre terminal :

```bash
npx baseai@latest dev
```

## Étape 10 : Exécuter l'agent de mémoire

Exécutez le fichier index.ts en utilisant la commande suivante :

```bash
npx tsx index.ts
```

## Le résultat

Dans votre terminal, vous serez invité à "Entrez votre requête". Par exemple, demandons : "Qu'est-ce qu'un pipe sur Langbase ?" Et il nous donnera la réponse avec les sources/citations correctes également.

Avec cette configuration, nous avons construit un agent "Discuter avec votre document" qui utilise la puissance des LLM et des agents de mémoire Langbase pour surmonter les limitations des LLM, garantissant des réponses précises sans hallucinations sur les données privées.

Voici une démonstration du résultat final :

%[https://youtu.be/v2Iev-q3kuc] 

Merci d'avoir lu !