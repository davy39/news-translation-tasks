---
title: Comment construire des agents IA RAG avec TypeScript
subtitle: ''
author: Maham Codes
co_authors: []
series: null
date: '2025-04-16T14:45:59.795Z'
originalURL: https://freecodecamp.org/news/how-to-build-rag-ai-agents-with-typescript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744814746615/72626297-def9-466a-8c1a-2cdb1b411300.png
tags:
- name: 'RAG '
  slug: rag
- name: ai agents
  slug: ai-agents
- name: llm
  slug: llm
- name: TypeScript
  slug: typescript
seo_title: Comment construire des agents IA RAG avec TypeScript
seo_desc: The most powerful AI systems don’t just generate – they also retrieve, reason,
  and respond with context. Retrieval-Augmented Generation (RAG) is how we get there.
  It combines the strengths of search and generation to build more accurate, reliable,
  an...
---

Les systèmes IA les plus puissants ne se contentent pas de générer - ils récupèrent également, raisonnent et répondent avec contexte. La génération augmentée par récupération (RAG) est la méthode pour y parvenir. Elle combine les forces de la recherche et de la génération pour construire des systèmes IA plus précis, fiables et conscients du contexte.

Dans ce guide, vous allez construire un agent IA basé sur RAG en TypeScript en utilisant le SDK Langbase. Vous allez intégrer vos propres données comme mémoire, utiliser n'importe quel modèle d'embedding, récupérer le contexte pertinent et appeler un LLM pour générer une réponse précise.

À la fin de ce tutoriel, vous aurez un système RAG fonctionnel qui :

* Stocke et récupère des documents avec une mémoire sémantique

* Utilise des embeddings personnalisés pour la recherche vectorielle

* Gère les requêtes utilisateur avec un contexte pertinent

* Génère des réponses via OpenAI, Anthropic ou n'importe quel LLM

### Table des matières

* [Prérequis](#heading-prerequisites)

* [Qu'est-ce que le RAG agentique ?](#heading-quest-ce-que-le-rag-agentique)

* [SDK Langbase](#heading-langbase-sdk)

* [Étape 1 : Installation de votre projet](#heading-etape-1-installation-de-votre-projet)

* [Étape 2 : Obtenir la clé API Langbase](#heading-etape-2-obtenir-la-cle-api-langbase)

* [Étape 3 : Ajouter les clés API LLM](#heading-etape-3-ajouter-les-cles-api-llm)

* [Étape 4 : Créer une mémoire IA agentique](#heading-etape-4-creer-une-memoire-ia-agentique)

* [Étape 5 : Ajouter des documents à la mémoire IA](#heading-etape-5-ajouter-des-documents-a-la-memoire-ia)

* [Étape 6 : Effectuer une récupération RAG](#heading-etape-6-effectuer-une-recuperation-rag)

* [Étape 7 : Créer un agent pipe de support](#heading-etape-7-creer-un-agent-pipe-de-support)

* [Étape 8 : Générer des réponses RAG](#heading-etape-8-generer-des-reponses-rag)

* [Le résultat](#heading-le-resultat)

## Prérequis

Avant de commencer à créer un agent IA basé sur RAG, vous devrez avoir certains outils prêts à l'emploi.

Dans ce tutoriel, j'utiliserai la pile technologique suivante :

* [Langbase](http://langbase.com/) - la plateforme pour construire et déployer vos agents IA serverless.

* [SDK Langbase](https://langbase.com/docs/sdk) - un SDK IA TypeScript, conçu pour fonctionner avec JavaScript, TypeScript, Node.js, Next.js, React, et similaires.

* [OpenAI](https://openai.com/) - pour obtenir la clé LLM pour le modèle préféré.

Vous devrez également :

* Vous inscrire sur Langbase pour obtenir accès à la clé API.

* Vous inscrire sur OpenAI pour générer la clé LLM pour le modèle que vous souhaitez utiliser (pour cette démonstration, j'utiliserai le modèle `openai:text-embedding-3-large`). Vous pouvez générer la clé [ici](https://platform.openai.com/api-keys).

## Qu'est-ce que le RAG agentique ?

La génération augmentée par récupération (RAG) est une architecture pour optimiser les performances d'un modèle d'intelligence artificielle (IA) en le connectant avec des bases de connaissances externes. Le RAG aide les grands modèles de langage (LLM) à fournir des réponses plus pertinentes avec une qualité supérieure.

Lorsque nous utilisons des agents IA pour faciliter le RAG, cela devient le **RAG agentique**. Les systèmes RAG agentiques ajoutent des agents IA au pipeline RAG pour augmenter l'adaptabilité et la précision. Comparé aux systèmes RAG traditionnels, le RAG agentique permet aux LLM de conduire la récupération d'informations à partir de multiples sources et de gérer des flux de travail plus complexes.

Voici la comparaison tabulaire du RAG vs RAG agentique :

| **Fonctionnalité** | **RAG** | **RAG agentique** |
| --- | --- | --- |
| Complexité des tâches | Tâches de requête simples - pas de prise de décision complexe | Gère des tâches complexes et multi-étapes en utilisant plusieurs outils et agents |
| Prise de décision | Limitée - pas d'autonomie | Les agents décident quoi récupérer, comment noter, raisonner, réfléchir et générer |
| Raisonnement multi-étapes | Requêtes et réponses en une seule étape uniquement | Supporte le raisonnement multi-étapes avec récupération, notation, filtrage et évaluation |
| Rôle clé | LLM + données externes pour les réponses | Ajoute des agents intelligents pour la récupération, la génération, la critique et l'orchestration |
| Récupération de données en temps réel | Non supporté | Conçu pour la récupération en temps réel et l'intégration dynamique |
| Intégration de la récupération | Bases de données vectorielles statiques et prédéfinies | Les agents récupèrent dynamiquement à partir de sources diverses et flexibles |
| Conscience du contexte | Contexte statique - pas d'adaptabilité à l'exécution | Élevée - les agents s'adaptent aux requêtes, extraient le contexte pertinent et récupèrent des données en direct si nécessaire |

## SDK Langbase

Le SDK Langbase facilite la construction d'outils IA puissants en utilisant TypeScript. Il vous donne tout ce dont vous avez besoin pour travailler avec n'importe quel LLM, connecter vos propres modèles d'embedding, gérer la mémoire des documents et construire des agents IA capables de raisonner et de répondre.

Le SDK est conçu pour fonctionner avec Node.js, Next.js, React ou n'importe quelle pile JavaScript moderne. Vous pouvez l'utiliser pour télécharger des documents, créer une mémoire sémantique et exécuter des flux de travail IA (appelés agents Pipe) avec seulement quelques lignes de code.

Langbase est une plateforme IA API-first. Son SDK TypeScript simplifie l'expérience, rendant facile de commencer sans avoir à gérer l'infrastructure. Il suffit d'ajouter votre clé API, d'écrire votre logique, et vous êtes prêt à partir.

Maintenant que vous connaissez le SDK Langbase, commençons à construire l'agent RAG.

## Étape 1 : Installation de votre projet

Nous allons construire une application Node.js basique en TypeScript qui utilise le SDK Langbase pour créer un système RAG agentique. Pour cela, créez un nouveau répertoire pour votre projet et naviguez jusqu'à lui.

```bash
mkdir agentic-rag && cd agentic-rag
```

Ensuite, initialisez un projet Node.js et créez différents fichiers TypeScript en exécutant cette commande dans votre terminal :

```bash
npm init -y && touch index.ts agents.ts create-memory.ts upload-docs.ts create-pipe.ts
```

Voici une description de ce que chaque fichier fera dans le projet :

* **index.ts** : Il s'agit généralement du point d'entrée d'un projet TypeScript. Il orchestrera la création de l'agent, la configuration de la mémoire et le téléchargement des documents.

* **agents.ts** : Ce fichier gère la création et la configuration des agents IA.

* **create-memory.ts** : Ce fichier configure la mémoire Langbase (RAG) pour le stockage et la récupération du contexte.

* **upload-docs.ts** : Ce fichier téléchargera des documents vers la mémoire afin que les agents puissent y accéder et les utiliser.

* **create-pipe.ts** : Ce fichier configure un [agent Pipe Langbase](https://langbase.com/docs/pipe/quickstart) qui est un agent IA serverless avec des API unifiées pour chaque LLM.

Après cela, nous utiliserons le SDK Langbase pour créer des agents RAG et `dotenv` pour gérer les variables d'environnement. Alors, installons ces dépendances.

```bash
npm i langbase dotenv
```

## Étape 2 : Obtenir la clé API Langbase

Chaque requête que vous envoyez à Langbase nécessite une clé API. Vous pouvez générer des clés API à partir du [studio Langbase](https://studio.langbase.com/) en suivant ces étapes :

1. Passez à votre compte utilisateur ou organisation.

2. Dans la barre latérale, cliquez sur le menu `Paramètres`.

3. Dans la section des paramètres développeur, cliquez sur le lien `Clés API Langbase`.

4. À partir de là, vous pouvez créer une nouvelle clé API ou gérer celles existantes.

Pour plus de détails, consultez la documentation des clés API Langbase.

Après avoir généré la clé API, créez un fichier `.env` à la racine de votre projet et ajoutez votre clé API Langbase :

```bash
LANGBASE_API_KEY=xxxxxxxxx
```

Remplacez xxxxxxxxx par votre clé API Langbase.

## Étape 3 : Ajouter les clés API LLM

Une fois que vous avez la clé API Langbase, vous aurez également besoin de la clé LLM pour exécuter l'agent RAG. Si vous avez configuré des clés API LLM dans votre profil, la mémoire IA et l'agent pipe les utiliseront automatiquement. Sinon, naviguez vers la page des clés API LLM et ajoutez des clés pour différents fournisseurs comme OpenAI, Anthropic, etc.

Suivez ces étapes pour ajouter les clés LLM :

1. Ajoutez les clés API LLM dans votre compte en utilisant le studio Langbase

2. Passez à votre compte utilisateur ou organisation.

3. Dans la barre latérale, cliquez sur le menu `Paramètres`.

4. Dans la section des paramètres développeur, cliquez sur le lien `Clés API LLM`.

5. À partir de là, vous pouvez ajouter des clés API LLM pour différents fournisseurs comme OpenAI, TogetherAI, Anthropic, etc.

## Étape 4 : Créer une mémoire IA agentique

Utilisons maintenant le SDK Langbase pour créer une mémoire IA (agent de mémoire Langbase) où votre agent peut stocker et récupérer du contexte.

Les agents de mémoire serverless Langbase (solution de mémoire à long terme) sont conçus pour acquérir, traiter, retenir et récupérer des informations de manière transparente. Ils attachent dynamiquement des données privées à n'importe quel LLM, permettant des réponses conscientes du contexte en temps réel et réduisant les hallucinations.

Ces agents combinent le stockage vectoriel, le RAG et l'accès à Internet pour créer une API de recherche de contexte gérée puissante. Vous pouvez les utiliser pour construire des applications IA plus intelligentes et plus capables.

Dans une configuration RAG, la mémoire - lorsqu'elle est connectée directement à un agent Pipe Langbase - devient un agent de mémoire. Ce couplage donne au LLM la capacité de récupérer des données pertinentes et de fournir des réponses précises et contextuellement exactes - répondant aux limitations des LLM lorsqu'il s'agit de gérer des données privées.

Pour la créer, ajoutez le code suivant au fichier `create-memory.ts` que vous avez créé à l'étape 1 :

```typescript
import 'dotenv/config';
import {Langbase} from 'langbase';

const langbase = new Langbase({
	apiKey: process.env.LANGBASE_API_KEY!,
});

async function main() {
	const memory = await langbase.memories.create({
		name: 'knowledge-base',
		description: 'Une mémoire IA pour l\'atelier de mémoire agentique',
		embedding_model: 'openai:text-embedding-3-large'
	});

	console.log('Mémoire IA:', memory);
}

main();
```

Voici ce qui se passe dans le code ci-dessus :

* Importe le package `dotenv` pour charger les variables d'environnement.

* Importe la classe `Langbase` du package langbase.

* Crée une nouvelle instance de la classe Langbase avec votre clé API.

* Utilise la méthode `memories.create` pour créer une nouvelle mémoire IA.

* Définit le nom et la description de la mémoire.

* Utilise le modèle `openai:text-embedding-3-large` pour l'embedding.

* Affiche la mémoire créée dans la console.

Après cela, créons la mémoire agentique en exécutant le fichier `create-memory.ts`.

```bash
npx tsx create-memory.ts
```

Cela créera une mémoire IA et affichera les détails de la mémoire dans la console.

## Étape 5 : Ajouter des documents à la mémoire IA

Maintenant que vous avez créé un agent de mémoire IA, l'étape suivante consiste à ajouter des documents. Ces documents serviront de contexte que votre agent pourra référencer lors des interactions.

Tout d'abord, créez un répertoire docs à la racine de votre projet et ajoutez deux fichiers texte d'exemple :

* [agent-architectures.txt](https://langbase.com/docs/examples/agent-architectures)

* [langbase-faq.txt](http://langbase.com/docs)

Ensuite, ouvrez le fichier `upload-docs.ts` créé à l'étape 1 et collez le code suivant :

```typescript
import 'dotenv/config';
import { Langbase } from 'langbase';
import { readFile } from 'fs/promises';
import path from 'path';

const langbase = new Langbase({
	apiKey: process.env.LANGBASE_API_KEY!,
});

async function main() {
	const cwd = process.cwd();
	const memoryName = 'knowledge-base';

	// Télécharger le document d'architecture de l'agent
	const agentArchitecture = await readFile(path.join(cwd, 'docs', 'agent-architectures.txt'));
	const agentResult = await langbase.memories.documents.upload({
		memoryName,
		contentType: 'text/plain',
		documentName: 'agent-architectures.txt',
		document: agentArchitecture,
		meta: { category: 'Examples', topic: 'Agent architecture' },
	});

	console.log(agentResult.ok ? '✓ Document de l\'agent téléchargé' : '✗ Échec du téléchargement du document de l\'agent');

	// Télécharger le document FAQ
	const langbaseFaq = await readFile(path.join(cwd, 'docs', 'langbase-faq.txt'));
	const faqResult = await langbase.memories.documents.upload({
		memoryName,
		contentType: 'text/plain',
		documentName: 'langbase-faq.txt',
		document: langbaseFaq,
		meta: { category: 'Support', topic: 'FAQ Langbase' },
	});

	console.log(faqResult.ok ? '✓ Document FAQ téléchargé' : '✗ Échec du téléchargement du document FAQ');
}

main();
```

Décomposons ce qui se passe dans ce code :

* `dotenv/config` est utilisé pour charger les variables d'environnement à partir de votre fichier .env.

* Langbase est importé du SDK pour interagir avec l'API.

* `readFile` du module `fs/promises` lit chaque fichier de document de manière asynchrone.

* `path.join()` garantit que les chemins de fichiers fonctionnent sur différents systèmes d'exploitation.

* Une instance cliente Langbase est créée en utilisant votre clé API.

* `memories.documents.upload` est utilisé pour télécharger chaque fichier .txt vers la mémoire IA.

* Chaque téléchargement inclut des métadonnées comme `category` et `topic` pour aider à organiser le contenu.

* Le succès ou l'échec du téléchargement est enregistré dans la console.

Cette étape garantit que votre agent IA aura un contenu réel à extraire - FAQ, documents d'architecture ou tout autre contenu que vous téléchargez en mémoire.

Ensuite, exécutez le fichier `upload-docs.ts` pour télécharger les documents vers la mémoire IA en utilisant cette commande dans votre terminal. Cela téléchargera les documents vers la mémoire IA :

```bash
npx tsx upload-docs.ts
```

## Étape 6 : Effectuer une récupération RAG

Dans cette étape, nous allons effectuer une récupération RAG contre une requête en utilisant les documents que nous avons téléchargés vers la mémoire IA.

Ajoutez le code suivant à votre fichier `agents.ts` créé à l'étape 1 :

```typescript
import 'dotenv/config';
import { Langbase } from 'langbase';

const langbase = new Langbase({
	apiKey: process.env.LANGBASE_API_KEY!,
});

export async function runMemoryAgent(query: string) {
	const chunks = await langbase.memories.retrieve({
		query,
		topK: 4,
		memory: [
			{
				name: 'knowledge-base',
			},
		],
	});

	return chunks;
}
```

Décomposons ce que cela fait :

* Importe la classe `Langbase` du SDK Langbase.

* Initialise le client Langbase en utilisant votre clé API à partir des variables d'environnement.

* Définit une fonction asynchrone `runMemoryAgent` qui prend une chaîne de requête en entrée.

* Utilise `memories.retrieve` pour interroger la mémoire afin d'obtenir les chunks les plus pertinents, en récupérant les 4 meilleurs résultats (`topK: 4`) de la mémoire nommée "knowledge-base".

* Retourne les chunks de mémoire récupérés.

Maintenant, ajoutons le code suivant au fichier `index.ts` créé à l'étape 1 pour exécuter l'agent de mémoire :

```typescript
import { runMemoryAgent } from './agents';

async function main() {
	const chunks = await runMemoryAgent('Qu\'est-ce que la parallélisation des agents ?');
	console.log('Chunk de mémoire:', chunks);
}

main();
```

Ce code exécute une requête de mémoire Langbase pour « Qu'est-ce que la parallélisation des agents ? ». Il utilise `runMemoryAgent` pour récupérer les chunks correspondants de votre mémoire IA et enregistre les résultats. C'est ainsi que vous récupérez des connaissances pertinentes avec RAG.

Après cela, exécutez le fichier `index.ts` pour effectuer une récupération RAG contre la requête en utilisant cette commande dans le terminal :

```bash
npx tsx index.ts
```

Vous verrez la sortie de l'agent de mémoire sous forme de chunks de mémoire récupérés dans la console comme suit :

```bash
[
  {
    text: '---\n' +
      '\n' +
      '## Parallélisation des agents\n' +
      '\n' +
      'La parallélisation exécute plusieurs tâches LLM en même temps pour améliorer la vitesse ou la précision. Elle fonctionne en divisant une tâche en parties indépendantes (sectionnement) ou en générant plusieurs réponses pour comparaison (vote).\n' +
      '\n' +
      'Le vote est une méthode de parallélisation où plusieurs appels LLM génèrent différentes réponses pour la même tâche. Le meilleur résultat est sélectionné en fonction de l\'accord, de règles prédéfinies ou de l\'évaluation de la qualité, améliorant la précision et la fiabilité.\n' +
      '\n' +
      "`Ce code implémente un système d\'analyse d\'emails qui traite les emails entrants via plusieurs agents IA parallèles pour déterminer si et comment ils doivent être traités. Voici la décomposition :",
    similarity: 0.7146744132041931,
    meta: {
      docName: 'agent-architectures.txt',
      documentName: 'agent-architectures.txt',
      category: 'Examples',
      topic: 'Agent architecture'
    }
  },
  {
    text: 'async function main(inputText: string) {\n' +
      '\ttry {\n' +
      '\t\t// Créer les pipes d\'abord\n' +
      '\t\tawait createPipes();\n' +
      '\n' +
      '\t\t// Étape A : Déterminer vers quel agent router\n' +
      '\t\tconst route = await routerAgent(inputText);\n' +
      "\t\tconsole.log('Décision du routeur:', route);\n" +
      '\n' +
      '\t\t// Étape B : Appeler l\'agent approprié\n' +
      '\t\tconst agent = agentConfigs[route.agent];\n' +
      '\n' +
      '\t\tconst response = await langbase.pipes.run({\n' +
      '\t\t\tstream: false,\n' +
      '\t\t\tname: agent.name,\n' +
      '\t\t\tmessages: [\n' +
      "\t\t\t\t{ role: 'user', content: `${agent.prompt} ${inputText}` }\n" +
      '\t\t\t]\n' +
      '\t\t});\n' +
      '\n' +
      '\t\t// Sortie finale\n' +
      '\t\tconsole.log(\n' +
      '\t\t\t`Agent: ${agent.name} \\n\\n Réponse: ${response.completion}`\n' +
      '\t\t);\n' +
      '\t} catch (error) {\n' +
      "\t\tconsole.error('Erreur dans le flux de travail principal:', error);\n" +
      '\t}\n' +
      '}\n' +
      '\n' +
      '// Exemple d\'utilisation:\n' +
      "const inputText = 'Pourquoi les jours sont-ils plus courts en hiver ?';\n" +
      '\n' +
      'main(inputText);\n' +
      '```\n' +
      '\n' +
      '\n' +
      '---\n' +
      '\n' +
      '## Parallélisation des agents\n' +
      '\n' +
      'La parallélisation exécute plusieurs tâches LLM en même temps pour améliorer la vitesse ou la précision. Elle fonctionne en divisant une tâche en parties indépendantes (sectionnement) ou en générant plusieurs réponses pour comparaison (vote).',
    similarity: 0.5911030173301697,
    meta: {
      docName: 'agent-architectures.txt',
      documentName: 'agent-architectures.txt',
      category: 'Examples',
      topic: 'Agent architecture'
    }
  },
  {
    text: "`Ce code implémente un système d\'orchestration de tâches sophistiqué avec génération dynamique de sous-tâches et traitement parallèle. Voici comment cela fonctionne :\n" +
      '\n' +
      '1. Agent Orchestrateur (Phase de planification) :\n' +
      '   - Prend une tâche complexe en entrée\n' +
      '   - Analyse la tâche et la décompose en sous-tâches plus petites et gérables\n' +
      '   - Retourne à la fois une analyse et une liste de sous-tâches au format JSON\n' +
      '\n' +
      '2. Agents Travailleurs (Phase d\'exécution) :\n' +
      '   - Plusieurs travailleurs s\'exécutent en parallèle en utilisant Promise.all()\n' +
      '   - Chaque travailleur reçoit :\n' +
      '     - La tâche originale pour le contexte\n' +
      '     - Leur sous-tâche spécifique à accomplir\n' +
      '   - Tous les travailleurs utilisent le modèle Gemini 2.0 Flash\n' +
      '\n' +
      '3. Agent Synthétiseur (Phase d\'intégration) :\n' +
      '   - Prend toutes les sorties des travailleurs\n' +
      '   - Les combine en un résultat final cohésif\n' +
      '   - Assure que les morceaux s\'enchaînent naturellement',
    similarity: 0.5393730401992798,
    meta: {
      docName: 'agent-architectures.txt',
      documentName: 'agent-architectures.txt',
      category: 'Examples',
      topic: 'Agent architecture'
    }
  },
  {
    text: "`Ce code implémente un système d\'analyse d\'emails qui traite les emails entrants via plusieurs agents IA parallèles pour déterminer si et comment ils doivent être traités. Voici la décomposition :\n" +
      '\n' +
      '1. Trois agents spécialisés s\'exécutant en parallèle :\n' +
      '   - Agent d\'analyse de sentiment : Détermine si le ton de l\'email est positif, négatif ou neutre\n' +
      '   - Agent de résumé : Crée un résumé concis du contenu de l\'email\n' +
      '   - Agent décideur : Prend les sorties des autres agents et décide :\n' +
      '     - Si l\'email nécessite une réponse\n' +
      "     - S\'il s\'agit de spam\n" +
      '     - Niveau de priorité (faible, moyen, élevé, urgent)\n' +
      '\n' +
      '2. Le flux de travail :\n' +
      '   - Prend un email en entrée\n' +
      '   - Exécute l\'analyse de sentiment et la génération de résumé en parallèle en utilisant Promise.all()\n' +
      '   - Alimente ces résultats à l\'agent décideur\n' +
      '   - Produit un objet de décision final avec les exigences de réponse\n' +
      '\n' +
      '3. Tous les agents utilisent le modèle Gemini 2.0 Flash et sont structurés pour retourner des réponses JSON analysées',
    similarity: 0.49115753173828125,
    meta: {
      docName: 'agent-architectures.txt',
      documentName: 'agent-architectures.txt',
      category: 'Examples',
      topic: 'Agent architecture'
    }
  }
]
```

## Étape 7 : Créer un agent Pipe de support

Dans cette étape, nous allons créer un agent de support en utilisant le SDK Langbase. Ajoutez le code suivant au fichier `create-pipe.ts` créé à l'étape 1 :

```typescript
import 'dotenv/config';
import { Langbase } from 'langbase';

const langbase = new Langbase({
	apiKey: process.env.LANGBASE_API_KEY!,
});

async function main() {
	const supportAgent = await langbase.pipes.create({
		name: `ai-support-agent`,
		description: `Un agent IA pour aider les utilisateurs avec leurs requêtes.`,
		messages: [
			{
				role: `system`,
				content: `Vous êtes un assistant IA utile.
				Vous aiderez les utilisateurs avec leurs requêtes.
				Assurez-vous toujours de fournir des informations précises et pertinentes.`,
			},
		],
	});

	console.log('Agent de support:', supportAgent);
}

main();
```

Passons en revue le code ci-dessus :

* Initialise le SDK Langbase avec votre clé API.

* Utilise la méthode `pipes.create` pour créer un nouvel agent pipe.

* Affiche l'agent pipe créé dans la console.

Maintenant, exécutez le fichier `create-pipe.ts` pour créer l'agent pipe en utilisant cette commande dans votre terminal :

```bash
npx tsx create-pipe.ts
```

Cela créera un agent de support et affichera les détails de l'agent dans la console.

## Étape 8 : Générer des réponses RAG

Jusqu'à présent, nous avons créé un agent de mémoire Langbase, ajouté des documents, effectué une récupération RAG contre une requête et créé un agent de support en utilisant l'agent Pipe Langbase. La seule chose restante dans la création de cet agent RAG complet est la génération de réponses complètes en utilisant les LLM.

Pour ce faire, ajoutez le code suivant au fichier `agents.ts` créé à l'étape 1 :

```typescript
import 'dotenv/config';
import { Langbase, MemoryRetrieveResponse } from 'langbase';

const langbase = new Langbase({
	apiKey: process.env.LANGBASE_API_KEY!,
});

export async function runAiSupportAgent({
	chunks,
	query,
}: {
	chunks: MemoryRetrieveResponse[];
	query: string;
}) {
	const systemPrompt = await getSystemPrompt(chunks);

	const { completion } = await langbase.pipes.run({
		stream: false,
		name: 'ai-support-agent',
		messages: [
			{
				role: 'system',
				content: systemPrompt,
			},
			{
				role: 'user',
				content: query,
			},
		],
	});

	return completion;
}

async function getSystemPrompt(chunks: MemoryRetrieveResponse[]) {
	let chunksText = '';
	for (const chunk of chunks) {
		chunksText += chunk.text + '\n';
	}

	const systemPrompt = `
	Vous êtes un assistant IA utile.
	Vous aiderez les utilisateurs avec leurs requêtes.

	Assurez-vous toujours de fournir des informations précises et pertinentes.
	Ci-dessous se trouve un CONTEXTE pour vous aider à répondre aux questions. Répondez UNIQUEMENT à partir du CONTEXTE. Le CONTEXTE se compose de plusieurs chunks d'informations. Chaque chunk a une source mentionnée à la fin.

Pour chaque partie de réponse que vous fournissez, citez la source entre crochets comme ceci : [1].

À la fin de la réponse, listez toujours chaque source avec son numéro correspondant et fournissez le nom du document. Comme ceci [1] NomDuFichier.doc. S'il y a une URL, faites-en un hyperlien sur le nom.

Si vous ne connaissez pas la réponse, dites-le. Demandez plus de contexte si nécessaire.
	${chunksText}`;

	return systemPrompt;
}

export async function runMemoryAgent(query: string) {
	const chunks = await langbase.memories.retrieve({
		query,
		topK: 4,
		memory: [
			{
				name: 'knowledge-base',
			},
		],
	});

	return chunks;
}
```

Le code ci-dessus :

* Crée une fonction `runAiSupportAgent` qui prend des chunks et une requête en entrée.

* Utilise la méthode `pipes.run` pour générer des réponses en utilisant le LLM.

* Crée une fonction `getSystemPrompt` pour générer une invite système pour le LLM.

* Combine les chunks récupérés pour créer une invite système.

* Retourne la complétion générée.

Maintenant, exécutons l'agent de support avec les chunks de mémoire IA. Ajoutez le code suivant au fichier `index.ts` :

```typescript
import { runMemoryAgent, runAiSupportAgent } from './agents';

async function main() {
	const query = 'Qu\'est-ce que la parallélisation des agents ?';
	const chunks = await runMemoryAgent(query);

	const completion = await runAiSupportAgent({
		chunks,
		query,
	});

	console.log('Complétion:', completion);
}

main();
```

Ce code exécute deux agents : l'un pour récupérer les chunks de mémoire pertinents pour une requête (`runMemoryAgent`), et un autre (`runAiSupportAgent`) pour générer une réponse finale en utilisant ces chunks.

Ensuite, exécutez le fichier `index.ts` pour générer des réponses en utilisant le LLM.

```bash
npx tsx index.ts
```

### Le résultat

Après avoir exécuté l'agent de support, vous verrez la sortie suivante générée dans votre console :

```bash
Complétion : La parallélisation des agents est un processus qui exécute plusieurs tâches LLM (modèle de langage) simultanément pour améliorer la vitesse ou la précision. Cette technique peut être mise en œuvre de deux manières principales :

1. **Sectionnement** : Une tâche est divisée en parties indépendantes qui peuvent être traitées simultanément.
2. **Vote** : Plusieurs appels LLM génèrent différentes réponses pour la même tâche, et le meilleur résultat est sélectionné en fonction de l'accord, de règles prédéfinies ou de l'évaluation de la qualité. Cette approche améliore la précision et la fiabilité en comparant diverses sorties.

En pratique, la parallélisation des agents implique l'orchestration de plusieurs agents spécialisés pour gérer différents aspects d'une tâche, permettant un traitement efficace et des résultats améliorés.

Si vous avez besoin d'exemples plus détaillés ou d'éclaircissements supplémentaires, n'hésitez pas à demander !
```

C'est ainsi que vous pouvez construire un système RAG agentique avec TypeScript en utilisant le SDK Langbase.

Merci d'avoir lu !

Connectez-vous avec moi par 👋 :

* En vous abonnant à ma chaîne [YouTube](https://www.youtube.com/@AIwithMahamCodes) si vous voulez apprendre sur l'IA et les agents.

* En vous abonnant à ma newsletter gratuite [The Agentic Engineer](https://mahamcodes.substack.com/) où je partage toutes les dernières nouvelles/tendances/emplois sur l'IA et les agents et bien plus encore.

* Suivez-moi sur [X (Twitter)](https://x.com/MahamDev).