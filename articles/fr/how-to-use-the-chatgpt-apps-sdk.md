---
title: 'Comment utiliser le ChatGPT Apps SDK : Créer une application de pizza avec
  l''Apps SDK'
subtitle: ''
author: Shola Jegede
co_authors: []
series: null
date: '2025-10-15T18:32:52.088Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-chatgpt-apps-sdk
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1760552846436/808fcd59-4dbc-4874-bd62-2e13965f956c.png
tags:
- name: AI
  slug: ai
- name: openai
  slug: openai
- name: chatgpt
  slug: chatgpt
seo_title: 'Comment utiliser le ChatGPT Apps SDK : Créer une application de pizza
  avec l''Apps SDK'
seo_desc: 'OpenAI recently introduced ChatGPT Apps, powered by the new Apps SDK and
  the Model Context Protocol (MCP).

  Think of these apps as plugins for ChatGPT:


  You can invoke them naturally in a conversation.


  They can render custom interactive UIs inside Ch...'
---

OpenAI a récemment introduit les ChatGPT Apps, propulsées par le nouveau [Apps SDK](https://developers.openai.com/apps-sdk) et le Model Context Protocol (MCP).

Considérez ces applications comme des plugins pour ChatGPT :

* Vous pouvez les invoquer naturellement dans une conversation.
    
* Elles peuvent afficher des interfaces utilisateur (UI) interactives personnalisées à l'intérieur de ChatGPT (cartes, carrousels, vidéos, et plus encore).
    
* Elles s'exécutent sur un serveur MCP que vous contrôlez, lequel définit les outils, les ressources et les widgets fournis par l'application.
    

Dans ce guide étape par étape, vous allez construire une ChatGPT App en utilisant l'exemple officiel [Pizza App](https://github.com/openai/openai-apps-sdk-examples/tree/main/pizzaz_server_node). Cette application montre comment ChatGPT peut afficher des widgets UI comme une carte de pizzas ou un carrousel, alimentés par votre serveur local.

## Ce que vous allez apprendre

En suivant ce tutoriel, vous apprendrez comment :

* Configurer et exécuter une ChatGPT App avec le OpenAI Apps SDK.
    
* Comprendre les blocs de construction de base : outils, ressources et widgets.
    
* Connecter votre serveur d'application local à ChatGPT en utilisant le Developer Mode.
    
* Afficher une UI personnalisée directement dans une conversation ChatGPT.
    

## Table des matières

* [Ce que vous allez apprendre](#heading-ce-que-vous-allez-apprendre)
    
* [Table des matières](#heading-table-des-matieres)
    
* [Comment fonctionnent les ChatGPT Apps (vue d'ensemble)](#heading-comment-fonctionnent-les-chatgpt-apps-vue-densemble)
    
* [Étape 1. Cloner le dépôt d'exemples](#heading-etape-1-cloner-le-depot-dexemples)
    
* [Étape 2. Lancer le serveur de l'application Pizza](#heading-etape-2-lancer-le-serveur-de-lapplication-pizza)
    
* [Étape 3. Exposer votre serveur local](#heading-etape-3-exposer-votre-serveur-local)
    
    * [3.1 Obtenir ngrok](#heading-31-obtenir-ngrok)
        
    * [3.2 Installer ngrok](#heading-32-installer-ngrok)
        
    * [3.3 Connecter votre compte](#heading-33-connecter-votre-compte)
        
    * [3.4 Démarrer un tunnel](#heading-34-demarrer-un-tunnel)
        
* [Étape 4. Parcourir le code de l'application Pizza](#heading-etape-4-parcourir-le-code-de-lapplication-pizza)
    
    * [4.1 Importations et configuration](#heading-41-importations-et-configuration)
        
    * [4.2 Définition des widgets Pizza](#heading-42-definition-des-widgets-pizza)
        
    * [4.3 Mise en correspondance des widgets avec les outils et les ressources](#heading-43-mise-en-correspondance-des-widgets-avec-les-outils-et-les-ressources)
        
    * [4.4 Gestion des requêtes](#heading-44-gestion-des-requetes)
        
    * [4.5 Création du serveur](#heading-45-creation-du-serveur)
        
* [Étape 5. Activer le mode développeur dans ChatGPT](#heading-etape-5-activer-le-mode-developpeur-dans-chatgpt)
    
    * [5.1 Activer le mode développeur](#heading-51-activer-le-mode-developpeur)
        
    * [5.2 Créer l'application](#heading-52-creer-lapplication)
        
    * [5.3 Utiliser votre application](#heading-53-utiliser-votre-application)
        
* [Défis (à essayer vous-même)](#heading-defis-a-essayer-vous-meme)
    
    * [Défi A : Ajouter un widget « Pizza Specials » (texte uniquement)](#heading-defi-a-ajouter-un-widget-pizza-specials-texte-uniquement)
        
    * [Défi B : Prendre en charge plusieurs garnitures](#heading-defi-b-prendre-en-charge-plusieurs-garnitures)
        
    * [Défi C : Récupérer des données de pizza réelles depuis une API externe](#heading-defi-c-recuperer-des-donnees-de-pizza-reelles-depuis-une-api-externe)
        
* [Conclusion](#heading-conclusion)
    

## Comment fonctionnent les ChatGPT Apps (vue d'ensemble)

Voici l'architecture en termes simples :

```markdown
ChatGPT (frontend)
   |
   v
Serveur MCP (votre backend)
   |
   v
Widgets (balisage HTML/JS affiché dans ChatGPT)
```

* **ChatGPT** envoie des requêtes comme : *« Montre-moi un carrousel de pizzas. »*
    
* **Le serveur MCP** répond avec des ressources (balisage HTML) et la logique des outils.
    
* **Les widgets** sont rendus en ligne dans ChatGPT.
    

## Étape 1. Cloner le dépôt d'exemples

OpenAI fournit un dépôt d'exemples officiel qui inclut la Pizza App. Clonez-le et installez les dépendances à l'aide de ces commandes :

```powershell
git clone https://github.com/openai/openai-apps-sdk-examples.git
cd openai-apps-sdk-examples
pnpm install
```

Après l'installation, construisez les composants et démarrez le serveur de développement :

```powershell
pnpm run build  
pnpm run dev
```

## Étape 2. Lancer le serveur de l'application Pizza

Naviguez vers le serveur de la Pizza App et démarrez-le :

```powershell
cd pizzaz_server_node
pnpm start
```

Si cela fonctionne, vous devriez voir :

```powershell
Pizzaz MCP server listening on http://localhost:8000
  SSE stream: GET http://localhost:8000/mcp
  Message post endpoint: POST http://localhost:8000/mcp/messages
```

Cela signifie que votre serveur fonctionne localement.

## Étape 3. Exposer votre serveur local

Pour permettre à ChatGPT de communiquer avec votre application, votre serveur local a besoin d'une URL publique. ngrok offre un moyen rapide de l'exposer pendant le développement.

### 3.1 Obtenir ngrok

Inscrivez-vous sur [ngrok.com](https://ngrok.com) et copiez votre **authtoken**.

### 3.2 Installer ngrok

**macOS :**

```powershell
brew install ngrok
```

**Windows :**

* Téléchargez et décompressez ngrok.
    
* Optionnellement, ajoutez le dossier à votre PATH.
    

### 3.3 Connecter votre compte

```powershell
ngrok config add-authtoken <votre_authtoken>
```

### 3.4 Démarrer un tunnel

```powershell
ngrok http 8000
```

Cela vous donne une URL HTTPS publique (comme [`https://xyz.ngrok.app/mcp`](https://xyz.ngrok.app/mcp)).

## Étape 4. Parcourir le code de l'application Pizza

Le code complet du serveur de la Pizza App est long, alors décomposons-le en parties digestes.

### 4.1 Importations et configuration

```typescript
import { createServer } from "node:http";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { SSEServerTransport } from "@modelcontextprotocol/sdk/server/sse.js";
import { z } from "zod";
```

* `Server` et `SSEServerTransport` proviennent de l'Apps SDK.
    
* `zod` valide les entrées pour s'assurer que ChatGPT envoie les bons arguments.
    

### 4.2 Définition des widgets Pizza

Les widgets sont le cœur de l'application. Chacun représente un élément d'UI que ChatGPT peut afficher.

Voici le widget Pizza Map :

```typescript
{
  id: "pizza-map",
  title: "Show Pizza Map",
  templateUri: "ui://widget/pizza-map.html",
  html: `
    <div id="pizzaz-root"></div>
    <link rel="stylesheet" href=".../pizzaz-0038.css">
    <script type="module" src=".../pizzaz-0038.js"></script>
  `,
  responseText: "Rendered a pizza map!"
}
```

* `id` → nom unique du widget.
    
* `templateUri` → comment ChatGPT récupère l'UI.
    
* `html` → balisage réel et assets.
    
* `responseText` → message qui s'affiche dans le chat.
    

L'application définit cinq widgets :

* Pizza Map
    
* Pizza Carousel
    
* Pizza Album
    
* Pizza List
    
* Pizza Video
    

### 4.3 Mise en correspondance des widgets avec les outils et les ressources

Ensuite, les widgets sont convertis en **outils** (choses que ChatGPT peut appeler) et en **ressources** (balisage UI que ChatGPT peut afficher).

```typescript
const tools = widgets.map((widget) => ({
  name: widget.id,
  description: widget.title,
  inputSchema: toolInputSchema,
  title: widget.title,
  _meta: widgetMeta(widget)
}));

const resources = widgets.map((widget) => ({
  uri: widget.templateUri,
  name: widget.title,
  description: `${widget.title} widget markup`,
  mimeType: "text/html+skybridge",
  _meta: widgetMeta(widget)
}));
```

Cela rend chaque widget appelable et affichable.

### 4.4 Gestion des requêtes

Le serveur MCP répond aux requêtes de ChatGPT. Par exemple, quand ChatGPT appelle un outil de widget :

```typescript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const widget = widgetsById.get(request.params.name);
  const args = toolInputParser.parse(request.params.arguments ?? {});
  return {
    content: [{ type: "text", text: widget.responseText }],
    structuredContent: { pizzaTopping: args.pizzaTopping },
    _meta: widgetMeta(widget)
  };
});
```

Ceci :

* Trouve le widget demandé.
    
* Valide l'entrée (`pizzaTopping`).
    
* Répond avec du texte + des métadonnées pour que ChatGPT puisse afficher le widget.
    

### 4.5 Création du serveur

Enfin, le serveur est lié aux points de terminaison HTTP (`/mcp` et `/mcp/messages`) afin que ChatGPT puisse diffuser des messages vers et depuis celui-ci.

```typescript
const httpServer = createServer(async (req, res) => {
  // gérer les requêtes vers /mcp et /mcp/messages
});

httpServer.listen(8000, () => {
  console.log("Pizzaz MCP server running on port 8000");
});
```

## Étape 5. Activer le mode développeur dans ChatGPT

### 5.1 Activer le mode développeur

* Ouvrez ChatGPT
    
* Allez dans **Settings → Apps & Connectors → Advanced Settings**
    
* Activez **Developer Mode**
    

![Activer le mode développeur](https://cdn.hashnode.com/res/hashnode/image/upload/v1760313826734/7cf96d44-ae03-48d1-92b9-7fee42d895ad.png align="center")

Lorsque le **Developer Mode** est activé, ChatGPT devrait ressembler à ceci :

![Mode développeur activé](https://cdn.hashnode.com/res/hashnode/image/upload/v1760313206155/f2677b50-8bc0-4c10-b971-b0a60d66181f.png align="center")

### 5.2 Créer l'application

* Retournez dans **Settings → Apps & Connectors**
    
* Cliquez sur **Create**
    
* Ensuite :
    
    * **Name** : Entrez un nom pour votre application (par exemple, *Pizza App*)
        
    * **Description** : Entrez une description pour votre application (ou laissez vide)
        
    * **MCP Server URL** : Collez l'URL HTTPS publique de votre point de terminaison MCP. Assurez-vous qu'elle pointe directement vers `/mcp`, et pas seulement vers la racine du serveur
        
    * **Authentication** : Choisissez **No authentication**
        
    * Cochez **I trust this application**
        
    * Cliquez sur **Create** pour terminer
        

![Créez votre application dans ChatGPT](https://cdn.hashnode.com/res/hashnode/image/upload/v1760313317398/93d30263-59db-4606-8066-467b7949efb9.png align="center")

Une fois votre application connectée à ChatGPT, elle devrait ressembler à ceci :

![L'application est connectée à ChatGPT](https://cdn.hashnode.com/res/hashnode/image/upload/v1760313733914/944b363a-7004-4737-a102-bd1e328f717d.png align="center")

Lorsque vous cliquez sur l'icône **Retour**, vous devriez voir votre application et d'autres applications auxquelles vous pouvez vous connecter et utiliser avec ChatGPT :

![Voir toutes les applications connectables à ChatGPT](https://cdn.hashnode.com/res/hashnode/image/upload/v1760313649918/627594a8-a89b-4cd5-90a6-1fa2d804063e.png align="center")

### 5.3 Utiliser votre application

Pour utiliser votre application,

* Ouvrez une nouvelle discussion dans ChatGPT
    
* Cliquez sur l'icône **+**
    
* Faites défiler vers le bas jusqu'à **more**
    
* Vous devriez voir votre application
    
* Choisissez **Pizza App** pour commencer à l'utiliser
    

![Comment utiliser votre application dans ChatGPT](https://cdn.hashnode.com/res/hashnode/image/upload/v1760313495700/e978f689-622b-4ceb-aa73-6459302e8b3b.png align="center")

Voici quelques commandes que vous pouvez essayer avec votre application de pizza dans ChatGPT :

* *Montre-moi une carte de pizzas avec une garniture pepperoni*
    
* *Montre-moi un carrousel de pizzas avec une garniture champignons*
    
* *Montre-moi un album de pizzas avec une garniture végétarienne*
    
* *Montre-moi une liste de pizzas avec une garniture fromage*
    
* *Montre-moi une vidéo de pizza avec une garniture poulet*
    

Chaque commande indique à ChatGPT quel widget afficher, et vous pouvez changer la garniture comme vous le souhaitez.

![Saisissez une commande dans ChatGPT pour appeler les outils de votre application](https://cdn.hashnode.com/res/hashnode/image/upload/v1760313589161/07b69ab7-fd36-4a14-84de-883a0f634b82.png align="center")

Voici quelques exemples :

* Carte avec garniture pepperoni :
    

![Exemple de réponse : Carte avec garniture pepperoni](https://cdn.hashnode.com/res/hashnode/image/upload/v1760314642952/6527fe96-061b-433c-94b9-86b8152fd082.png align="center")

* Carrousel extra fromage :
    

![Exemple de réponse : Carrousel extra fromage](https://cdn.hashnode.com/res/hashnode/image/upload/v1760314675799/8b65e9b3-4547-40a2-9269-cec56aa8705f.png align="center")

* Album avec garniture champignons :
    

![Exemple de réponse : Album avec garniture champignons](https://cdn.hashnode.com/res/hashnode/image/upload/v1760314714658/ae6edf57-44c9-421b-a140-364cc8873db4.png align="center")

## Défis (à essayer vous-même)

Voici trois façons pratiques d'étendre votre Pizza App. Chacune est directement liée au code que vous avez déjà.

### Défi A : Ajouter un widget « Pizza Specials » (texte uniquement)

**Objectif :** Créer un widget qui affiche simplement un court message comme *« Spécial du jour : Margherita au basilic. »*

**Où modifier :**

* `resources.widgets` → dupliquez une entrée et donnez-lui un nouvel `id`/`title`.
    
* `tools` → enregistrez-le comme un nouvel outil.
    
* Gestionnaire `CallTool` → détectez quand il est appelé (`if (request.params.name === "pizza-special")`) et renvoyez votre spécialité.
    

**Astuce :**  
Ce widget n'a pas besoin de fichiers CSS/JS supplémentaires. Gardez simplement son `html` comme `<div>🍕 Spécial du jour : Margherita</div>`. L'idée est de montrer que les widgets peuvent être aussi simples que du HTML pur.

### Défi B : Prendre en charge plusieurs garnitures

**Objectif :** Permettre aux utilisateurs de commander une pizza avec plus d'une garniture, comme `["pepperoni", "mushroom"]`.

**Où modifier :**

* `toolInputSchema` → passez de `z.string()` à `z.array(z.string())`.
    
* Gestionnaire `CallTool` → après l'analyse, `args.pizzaTopping` sera un tableau. Joignez-le en une chaîne de caractères avant de l'insérer dans le HTML/la réponse.
    
* Widget HTML → mettez à jour l'affichage pour qu'il liste toutes les garnitures choisies.
    

**Astuce :**  
Faites un `console.log` des `args` analysés d'abord pour confirmer que vous recevez bien un tableau. Ensuite, essayez quelque chose comme :

```typescript
const toppings = args.pizzaTopping.join(", ");
return { responseText: `Pizza commandée avec : ${toppings}` };
```

### Défi C : Récupérer des données de pizza réelles depuis une API externe

**Objectif :** Au lieu de coder le contenu en dur, récupérez de vraies informations sur les pizzas. Par exemple, vous pourriez appeler l'API de Yelp pour lister les pizzerias d'un lieu, ou utiliser une API de test gratuite pour simuler des données.

**Où modifier :**

* À l'intérieur du gestionnaire `CallTool` pour votre widget.
    
* Remplacez le HTML statique par un appel `fetch(...)` qui construit un HTML dynamique à partir de la réponse.
    

**Astuce :**  
Commencez petit avec une API gratuite comme [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts). Par exemple :

```typescript
const res = await fetch("https://jsonplaceholder.typicode.com/posts?_limit=3");
const data = await res.json();

const html = `
  <ul>
    ${data.map((p: any) => `<li>${p.title}</li>`).join("")}
  </ul>
`;

return { responseText: "Pizzerias récupérées !", content: [{ type: "text/html", text: html }] };
```

Une fois que cela fonctionne, remplacez par une véritable API telle que Yelp ou Google Maps Places pour afficher de vraies pizzerias.

## Conclusion

Vous venez de construire votre première ChatGPT App en utilisant le **OpenAI Apps SDK**. Avec un peu de JavaScript et de HTML, vous avez créé un serveur avec lequel ChatGPT peut communiquer, et affiché des widgets interactifs directement dans la fenêtre de chat.

Cet exemple s'est concentré sur l'échantillon d'application de pizza fourni par OpenAI, mais vous pourriez construire :

* Un tableau de bord météo,
    
* Un moteur de recherche de films,
    
* Un visualiseur de données financières,
    
* Ou même un mini-jeu.
    

Le SDK permet de mélanger **conversation + UI interactive** de manières inédites et puissantes.

Explorez la [documentation du OpenAI Apps SDK](https://developers.openai.com/apps-sdk) pour aller plus loin et commencer à construire vos propres applications.