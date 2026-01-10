---
title: Comment créer des agents IA serverless avec le serveur Langbase Docs MCP en
  quelques minutes
subtitle: ''
author: Maham Codes
co_authors: []
series: null
date: '2025-05-06T15:38:08.144Z'
originalURL: https://freecodecamp.org/news/how-to-create-serverless-ai-agents-with-langbase-docs-mcp-server-in-minutes
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746545857204/6df2b802-a7dc-4745-ac64-117c1c0f7ee1.png
tags:
- name: mcp
  slug: mcp
- name: AI
  slug: ai
- name: ai agents
  slug: ai-agents
- name: 'LLM''s '
  slug: llms
seo_title: Comment créer des agents IA serverless avec le serveur Langbase Docs MCP
  en quelques minutes
seo_desc: Building serverless AI agents has recently become a lot simpler. With the
  Langbase Docs MCP server, you can instantly connect AI models to Langbase documentation
  – making it easy to build composable, agentic AI systems with memory without complex
  inf...
---

La création d'agents IA serverless est récemment devenue beaucoup plus simple. Avec le serveur Langbase Docs MCP, vous pouvez connecter instantanément des modèles d'IA à la documentation Langbase, ce qui facilite la construction de systèmes IA agentiques et composables avec mémoire, sans infrastructure complexe.

Dans ce guide, vous apprendrez comment configurer le serveur Langbase Docs MCP dans Cursor (un éditeur de code IA), et construire un agent IA de synthèse qui utilise les documents Langbase comme contexte en direct et à la demande.

### Voici ce que nous allons couvrir :

* [Prérequis](#heading-prerequisites)

* [Qu'est-ce que le Model Context Protocol (MCP) ?](#heading-quest-ce-que-le-model-context-protocol-mcp)

* [Le rôle d'Anthropic dans le lancement du MCP](#heading-le-role-danthropic-dans-le-lancement-du-mcp)

* [L'éditeur de code IA Cursor](#heading-lediteur-de-code-ia-cursor)

* [Qu'est-ce que Langbase et pourquoi son serveur Docs MCP est-il utile ?](#heading-quest-ce-que-langbase-et-pourquoi-son-serveur-docs-mcp-est-il-utile)

* [Comment configurer le serveur Langbase Docs MCP dans Cursor](#heading-comment-configurer-le-serveur-langbase-docs-mcp-dans-cursor)

* [Comment utiliser le serveur Langbase Docs MCP dans Cursor AI](#heading-comment-utiliser-le-serveur-langbase-docs-mcp-dans-cursor-ai)

* [Cas d'usage : Construire un agent IA de synthèse avec le serveur Langbase Docs MCP](#heading-cas-dusage-construire-un-agent-ia-de-synthese-avec-le-serveur-langbase-docs-mcp)

## Prérequis

Avant de commencer à créer l'agent, vous devrez avoir certaines choses configurées et certains outils prêts à l'emploi.

Dans ce tutoriel, j'utiliserai la pile technologique suivante :

* [Langbase](http://langbase.com) – la plateforme pour construire et déployer vos agents IA serverless.

* [Langbase SDK](https://langbase.com/docs/sdk) – un SDK IA TypeScript, conçu pour fonctionner avec JavaScript, TypeScript, Node.js, Next.js, React, et autres.

* [Cursor](http://cursor.com) – Un éditeur de code IA similaire à VS Code.

Vous devrez également :

* [Vous inscrire](https://langbase.com/signup) sur Langbase pour obtenir accès à la clé API.

## **Qu'est-ce que le Model Context Protocol (MCP) ?**

[**Model Context Protocol (MCP)**](https://modelcontextprotocol.io/introduction) est un protocole ouvert qui standardise la manière dont les applications fournissent un contexte externe aux grands modèles de langage (LLM). Avec le MCP, les développeurs peuvent connecter des modèles d'IA à divers outils et sources de données comme la documentation, les API et les bases de données, de manière propre et cohérente.

Au lieu de dépendre uniquement des prompts, le MCP permet aux LLM d'appeler des outils personnalisés (comme des récupérateurs de documentation ou des explorateurs d'API) pendant une conversation.

### Architecture générale du MCP

À sa base, le MCP suit une architecture client-serveur où une application hôte peut se connecter à plusieurs serveurs.

Voici à quoi ressemble l'architecture générale :

[![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdjfGegMH-jHoYjgT3dRPhigOoIz8em0NyexLrfqwNEwdX7rvnbnCxfJG7nKqLk5fYcFu0_D5D8-DMb3vg0nLF4r-N8LlfH6IyFz18HjGZYlZ2J2_cq-jKq3Y6X_LPVxIz3rPs7?key=aHnkCxEY2NrPpuL4oNSIQJNY align="left")](https://modelcontextprotocol.io/introduction)

L'architecture du Model Context Protocol permet aux clients IA (comme Claude, les IDE et les outils de développement) de se connecter de manière sécurisée à plusieurs sources de données locales ou distantes en temps réel. Les clients MCP communiquent avec un ou plusieurs serveurs MCP, qui servent de ponts vers des données structurées, qu'elles proviennent de fichiers locaux, de bases de données ou d'API distantes.

Cette configuration permet aux modèles d'IA de récupérer un contexte frais et pertinent à partir de différentes sources de manière transparente, sans intégrer les données directement dans le modèle.

## **Le rôle d'Anthropic dans le lancement du MCP**

[Anthropic](https://www.anthropic.com/news/model-context-protocol) a introduit le MCP dans le cadre de leur vision de rendre les LLM augmentés par des outils par défaut. Le MCP a été initialement construit pour étendre les capacités de Claude, mais il est maintenant disponible plus largement et pris en charge dans des environnements conviviaux pour les développeurs comme Cursor et Claude Desktop.

En standardisant la manière dont les outils s'intègrent dans les flux de travail des LLM, le MCP facilite l'extension des systèmes IA par les développeurs sans avoir besoin de plugins personnalisés ou de hacks d'API.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1746454175998/50ed79a0-3728-4cca-92a1-0f48ded38049.png align="center")

## **L'éditeur de code IA Cursor**

[**Cursor**](https://www.cursor.com/) est un éditeur de code IA conçu pour les développeurs, qui intègre les LLM (comme Claude, GPT, et d'autres) directement dans votre IDE. Cursor prend en charge le MCP, ce qui signifie que vous pouvez rapidement attacher des serveurs d'outils personnalisés et les rendre accessibles en tant qu'outils augmentés par l'IA pendant que vous codez.

Imaginez Cursor comme VS Code rencontre les agents IA, avec un support intégré pour des outils intelligents comme les récupérateurs de documentation et les récupérateurs d'exemples de code.

## **Qu'est-ce que Langbase et pourquoi son serveur Docs MCP est-il utile ?**

**Langbase** est une plateforme IA serverless puissante pour construire des agents IA avec mémoire. Elle aide les développeurs à construire des applications et des assistants alimentés par l'IA en connectant directement les LLM à leurs données, API et documentation.

Le [serveur Langbase Docs MCP](https://langbase.com/docs/guides/docs-mcp-server) fournit un accès à la documentation Langbase et à la référence de l'API. Ce serveur vous permet d'utiliser la documentation Langbase comme contexte pour vos LLM.

En connectant ce serveur à Cursor (ou à tout IDE prenant en charge le MCP), vous pouvez rendre la documentation Langbase disponible pour vos agents IA à la demande. Cela signifie moins de changement de contexte, des flux de travail plus rapides et une assistance plus intelligente lors de la construction d'applications agentiques serverless.

## **Comment configurer le serveur Langbase Docs MCP dans Cursor**

Parcourons la configuration du serveur étape par étape.

### **1. Ouvrir les paramètres de Cursor**

Lancez Cursor et ouvrez les paramètres. Dans la barre latérale de gauche, sélectionnez MCP.

### **2. Ajouter un nouveau serveur MCP**

Cliquez sur le bouton jaune + Ajouter un nouveau serveur MCP global.

![Ajouter un nouveau serveur MCP global](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdpv9IyBcpFfY9iUo9xk_hfhwhXmyx7JG_4hCPy8WhYC2dMyxHyCniTB147YnQrjGjjqOyvRQsFpHq5-rPVOz637fAwhlfil9ZFhcoicgy3ggriV4_D9mAcdMMTXXCC3gfQiZE?key=aHnkCxEY2NrPpuL4oNSIQJNY align="left")

### **3. Configurer le serveur Langbase Docs MCP**

Collez la configuration suivante dans le fichier `mcp.json` :

```json
{
    "mcpServers": {
        "Langbase": {
        "command": "npx",
        "args": ["@langbase/cli","docs-mcp-server"]
        }
    }
}
```

### **4. Démarrer le serveur Langbase Docs MCP**

Dans votre terminal, exécutez :

```bash
pnpm add @langbase/cli
```

Puis exécutez cette commande :

```bash
pnpm dlx @langbase/cli docs-mcp-server
```

### **5. Activer le serveur MCP dans Cursor**

Dans les paramètres MCP, assurez-vous que le serveur Langbase est activé.

![Serveur Langbase activé dans Cursor](https://lh7-rt.googleusercontent.com/docsz/AD_4nXebJ0x4bjv6jDtvfrHnzHo76upu7JyUxasbsrWu0SVxg-ZyA6qir3_8tnCqAK1d1FixOkOcl0oLJN2FopMJGGNAyHLQfmJvkd4ittBaQyOIz26JHgW36PXdduyRt2qD82qrToJC?key=aHnkCxEY2NrPpuL4oNSIQJNY align="left")

## **Comment utiliser le serveur Langbase Docs MCP dans Cursor AI**

Une fois tout configuré, l'agent IA de Cursor peut maintenant appeler des outils de documentation Langbase comme :

* `docs_route_finder`

* `sdk_documentation_fetcher`

* `examples_tool`

* `guide_tool`

* `api_reference_tool`

Par exemple, vous pouvez demander à l'agent Cursor :

```bash
« Montrez-moi la référence API pour la mémoire Langbase »
 ou
 « Trouvez un exemple de code pour créer un pipe d'agent IA dans Langbase »
```

L'IA utilisera le serveur Docs MCP pour récupérer des extraits de documentation précis, directement dans Cursor.

## **Cas d'usage : Construire un agent IA de synthèse avec le serveur Langbase Docs MCP**

Construisons un agent de synthèse qui résume le contexte en utilisant le SDK Langbase, alimenté par le serveur Langbase Docs MCP dans l'éditeur de code IA Cursor.

1. Ouvrez un dossier vide dans Cursor et lancez le panneau de chat (`Cmd+Shift+I` sur Mac ou `Ctrl+Shift+I` sur Windows).

2. Passez en mode Agent à partir du sélecteur de mode et choisissez votre LLM préféré (nous utiliserons Claude 3.5 Sonnet pour cette démonstration).

3. Dans l'entrée de chat, saisissez l'invite suivante :
 « Dans ce répertoire, en utilisant le SDK Langbase, créez l'agent pipe de synthèse. Utilisez TypeScript et pnpm pour exécuter l'agent dans le terminal. »

4. Cursor invoquera automatiquement les appels MCP, générera les fichiers et le code requis en utilisant les documents Langbase comme contexte, et suggérera des modifications. Acceptez les modifications, et votre agent de synthèse sera prêt. Vous pouvez exécuter l'agent en utilisant les commandes fournies par Cursor et voir les résultats.

Voici une vidéo de démonstration de la création de cet agent de synthèse avec une seule invite et le serveur Langbase Docs MCP :

%[https://youtu.be/Pw6Su5hpWwU]

En combinant le serveur Docs MCP de Langbase avec Cursor AI, vous avez appris à construire des agents IA serverless en quelques minutes, le tout sans quitter votre IDE.

Si vous construisez des agents IA, des outils ou des applications avec Langbase, c'est l'une des façons les plus rapides de simplifier votre processus de développement.

Bonne construction ! 🚀

Connectez-vous avec moi par 👋 :

* En vous abonnant à ma chaîne [YouTube](https://www.youtube.com/@AIwithMahamCodes). Si vous souhaitez apprendre sur l'IA et les agents.

* En vous abonnant à ma newsletter gratuite [« The Agentic Engineer »](https://mahamcodes.substack.com/) où je partage toutes les dernières nouvelles, tendances, emplois et bien plus encore sur l'IA et les agents.

* Suivez-moi sur [X (Twitter)](https://x.com/MahamDev).