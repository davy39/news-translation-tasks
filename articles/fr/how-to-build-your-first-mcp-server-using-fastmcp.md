---
title: Comment construire votre premier serveur MCP avec FastMCP
subtitle: Apprenez à construire votre premier serveur MCP en utilisant FastMCP et
  connectez-le à un grand modèle de langage pour effectuer des tâches concrètes via
  le code.
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-12-03T17:17:30.748Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-first-mcp-server-using-fastmcp
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1764782216715/fc1f7b09-d71d-4917-a249-f95686d23520.png
tags:
- name: llm
  slug: llm
- name: mcp
  slug: mcp
- name: AI
  slug: ai
- name: Python
  slug: python
seo_title: Comment construire votre premier serveur MCP avec FastMCP
seo_desc: "Model Context Protocol, or MCP, is changing how large language models connect\
  \ with data and tools. \nInstead of treating an AI model as a black box, MCP gives\
  \ it structured access to information and actions. \nIt is like the USB-C port for\
  \ AI, creating..."
---


Le Model Context Protocol, ou MCP, change la façon dont les grands modèles de langage se connectent aux données et aux outils.

Au lieu de traiter un modèle d'IA comme une boîte noire, le MCP lui donne un accès structuré aux informations et aux actions.

C'est comme le port USB-C pour l'IA, créant un moyen standard pour les modèles d'interagir avec des serveurs qui détiennent des données du monde réel ou effectuent des tâches utiles.

[FastMCP](https://gofastmcp.com/getting-started/welcome) est le Framework le plus simple et le plus rapide pour construire des serveurs MCP avec Python. Il masque tous les détails complexes du protocole et vous permet de vous concentrer sur votre logique.

Dans ce guide, vous apprendrez ce qu'est le MCP, comment fonctionne FastMCP, et comment construire et exécuter votre premier serveur MCP à partir de zéro.

## Table des matières

* [Qu'est-ce que le MCP](#heading-qu-est-ce-que-le-mcp) ?
    
* [Pourquoi utiliser FastMCP](#heading-pourquoi-utiliser-fastmcp) ?
    
* [Créer votre premier serveur MCP](#heading-creer-votre-premier-serveur-mcp)
    
* [Exécuter le serveur](#heading-executer-le-serveur)
    
* [Ajouter plus d'outils](#heading-ajouter-plus-d-outils)
    
* [Ajouter des ressources](#heading-ajouter-des-ressources)
    
* [Utiliser le contexte dans les outils](#heading-utiliser-le-contexte-dans-les-outils)
    
* [Se connecter avec un client MCP](#heading-se-connecter-avec-un-client-mcp)
    
* [Authentification et sécurité](#heading-authentification-et-securite)
    
* [Déployer votre serveur MCP](#heading-deployer-votre-serveur-mcp)
    
* [Utiliser le serveur MCP avec une application LLM](#heading-utiliser-le-serveur-mcp-avec-une-application-llm)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que le MCP ?

Le MCP est un protocole standard qui permet aux modèles de langage de communiquer avec des systèmes externes de manière sécurisée et cohérente. [Le MCP est similaire à une API](https://www.turingtalks.ai/p/difference-between-mcp-and-api), mais conçu pour les grands modèles de langage plutôt que pour les humains.

Un serveur MCP peut faire trois choses principales :

* Il peut exposer des données sous forme de ressources (similaires aux endpoints GET)
    
* Il peut fournir des actions via des outils (similaires aux requêtes POST)
    
* Et il peut définir des prompts qui guident la manière dont le modèle interagit avec les données ou les utilisateurs.
    

Par exemple, une ressource pourrait renvoyer une liste d'articles, un outil pourrait analyser ces articles, et un prompt pourrait définir comment le modèle les résume. En connectant un LLM à un tel serveur MCP, vous lui donnez le pouvoir d'utiliser vos propres données et votre logique en temps réel.

## Pourquoi utiliser FastMCP ?

Bien que vous puissiez construire un serveur MCP en utilisant le [SDK officiel](https://modelcontextprotocol.io/), FastMCP va beaucoup plus loin. C'est un Framework prêt pour la production avec une authentification d'entreprise, des bibliothèques clientes, des outils de test et une génération automatique d'API.

Vous pouvez utiliser FastMCP pour construire des applications MCP sécurisées et évolutives qui s'intègrent à des fournisseurs comme Google, GitHub et Azure. Il prend également en charge le déploiement sur le cloud ou sur votre propre infrastructure.

Plus important encore, le Framework est extrêmement convivial pour les développeurs. Vous pouvez créer un serveur MCP fonctionnel en seulement quelques lignes de code Python.

## Créer votre premier serveur MCP

Avant de commencer la construction, installez FastMCP dans votre environnement Python. Vous pouvez utiliser pip ou uv. L'outil uv est recommandé car il gère efficacement les environnements et les dépendances.

```powershell
uv pip install fastmcp
```

Une fois installé, vous êtes prêt à écrire votre premier serveur.

Chaque serveur MCP commence par la classe `FastMCP`. Cette classe représente votre application et gère vos outils, ressources et prompts. Commençons par créer un serveur simple qui additionne deux nombres.

Créez un fichier nommé `server.py` et ajoutez le code suivant :

```python
from fastmcp import FastMCP

mcp = FastMCP("Demo Server 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers and return the result"""
    return a + b
if __name__ == "__main__":
    mcp.run()
```

C'est tout ce dont vous avez besoin. Vous venez de créer un serveur MCP entièrement fonctionnel avec un outil appelé `add`. Lorsqu'un client appelle cet outil, le serveur additionne deux nombres et renvoie le résultat.

## Exécuter le serveur

Pour exécuter votre serveur localement, ouvrez votre terminal et tapez :

```powershell
fastmcp run server.py
```

Cette commande démarre le serveur MCP. Vous pouvez également utiliser les transports [HTTP ou SSE](https://www.pubnub.com/guides/server-sent-events/) pour des déploiements basés sur le Web. Par exemple, pour exécuter votre serveur via HTTP, utilisez :

```python
mcp.run(transport="http", host="127.0.0.1", port=8000, path="/mcp")
```

Une fois le serveur en cours d'exécution, les clients peuvent se connecter et appeler l'outil `add` à distance.

## Ajouter plus d'outils

Les outils FastMCP sont de simples fonctions Python que vous décorez avec `@mcp.tool`. Vous pouvez en ajouter autant que vous le souhaitez. Ajoutons ensuite un outil de multiplication :

```python
@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b
```

Vous pouvez maintenant relancer le serveur, et les clients auront accès aux outils `add` et `multiply`.

FastMCP génère automatiquement des schémas basés sur les signatures de vos fonctions et les docstrings, ce qui permet aux clients de comprendre facilement votre API.

## Ajouter des ressources

Les ressources dans MCP représentent des données en lecture seule auxquelles les clients peuvent accéder. Vous pouvez créer des ressources statiques ou des modèles dynamiques qui prennent des paramètres. Par exemple, vous pourriez exposer un numéro de version ou un profil utilisateur.

```python
@mcp.resource("config://version")
def get_version():
    return "1.0.0"

@mcp.resource("user://{user_id}/profile")
def get_profile(user_id: int):
    return {"name": f"User {user_id}", "status": "active"}
```

Dans cet exemple, la première ressource renvoie toujours le numéro de version, tandis que la deuxième ressource récupère dynamiquement un profil utilisateur en fonction de l'ID fourni.

## Utiliser le contexte dans les outils

FastMCP vous permet d'accéder au contexte de la session au sein de n'importe quel outil, ressource ou prompt en incluant un paramètre `ctx: Context`. Le contexte vous offre des capacités puissantes comme la journalisation, l'[échantillonnage LLM](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling), le suivi de la progression et l'accès aux ressources.

Voici un exemple qui montre comment utiliser le contexte :

```python
from fastmcp import Context

@mcp.tool
async def summarize(uri: str, ctx: Context):
    await ctx.info(f"Reading resource from {uri}")
    data = await ctx.read_resource(uri)
    summary = await ctx.sample(f"Summarize this: {data.content[:500]}")
    return summary.text
```

Cet outil enregistre un message, lit une ressource, puis demande au modèle de langage du client de la résumer. Le contexte rend vos outils MCP plus intelligents et plus interactifs.

## Se connecter avec un client MCP

Une fois votre serveur en cours d'exécution, vous pouvez vous y connecter en utilisant la classe `fastmcp.Client`. Le client peut communiquer via STDIO, HTTP ou SSE, et peut même s'exécuter en mémoire pour les tests.

Voici un exemple simple de connexion à votre serveur local et d'appel de l'outil `add` :

```python
from fastmcp import Client
import asyncio

async def main():
    async with Client("server.py") as client:
        tools = await client.list_tools()
        print("Available tools:", tools)
        result = await client.call_tool("add", {"a": 5, "b": 7})
        print("Result:", result.content[0].text)
asyncio.run(main())
```

Vous pouvez également vous connecter à plusieurs serveurs en utilisant un fichier de configuration MCP standard, ce qui facilite la construction de systèmes complexes qui interagissent avec plusieurs services simultanément.

## Authentification et sécurité

Lorsque vous passez du développement à la production, l'authentification devient importante.

FastMCP dispose d'un support intégré pour les fournisseurs d'authentification de classe entreprise tels que Google, GitHub, Microsoft Azure, Auth0 et WorkOS. Vous pouvez activer un accès sécurisé basé sur OAuth avec seulement quelques lignes de code :

```python
from fastmcp.server.auth.providers.google import GoogleProvider
from fastmcp import FastMCP

auth = GoogleProvider(client_id="...", client_secret="...", base_url="https://myserver.com")
mcp = FastMCP("Secure Server", auth=auth)
```

Désormais, seuls les utilisateurs authentifiés peuvent accéder à votre serveur. Du côté client, vous pouvez vous connecter en utilisant un flux OAuth comme ceci :

```python
async with Client("https://secure-server.com/mcp", auth="oauth") as client:
    result = await client.call_tool("protected_tool")
```

FastMCP gère automatiquement les tokens, les rafraîchissements et la gestion des erreurs.

## Déployer votre serveur MCP

Vous pouvez déployer des serveurs FastMCP n'importe où.

Pour les tests, la commande `fastmcp run` suffit. Pour la production, vous pouvez déployer sur [FastMCP Cloud](https://fastmcp.cloud/), qui fournit des endpoints HTTPS instantanés et une authentification intégrée.

Si vous préférez l'auto-hébergement, utilisez le transport HTTP ou SSE pour servir vos endpoints MCP depuis votre propre infrastructure. Une commande de déploiement simple pourrait ressembler à ceci :

```python
mcp.run(transport="http", host="0.0.0.0", port=8080)
```

Une fois déployé, votre serveur MCP est prêt à se connecter à des modèles de langage, des clients Web ou des workflows d'automatisation.

## Utiliser le serveur MCP avec une application LLM

Une fois votre serveur MCP opérationnel, l'étape suivante consiste à le connecter à un grand modèle de langage. Cela permet à un LLM d'appeler en toute sécurité les fonctions de votre serveur, de lire des ressources et d'effectuer des actions dans le cadre d'une conversation.

Pour connecter une application LLM, vous définissez d'abord votre fichier de configuration MCP. Ce fichier répertorie les serveurs disponibles, leurs méthodes de connexion et toutes les exigences d'authentification.

Une fois configuré, le LLM peut automatiquement découvrir vos outils MCP et les appeler en cas de besoin.

Par exemple, si votre serveur expose un outil `add` ou `summarize`, le modèle peut les utiliser directement comme s'il s'agissait de capacités intégrées. Dans un environnement de chat, lorsqu'un utilisateur demande au modèle d'effectuer une tâche telle que « Résumer le dernier article », le LLM appellera votre outil `summarize`, traitera le résultat et répondra avec la sortie.

Si vous construisez une application LLM personnalisée avec des frameworks comme l'Assistants API d'OpenAI ou LangChain, vous pouvez enregistrer votre serveur MCP en tant qu'outil externe. Le LLM interagit ensuite avec lui via la bibliothèque cliente MCP.

Voici un exemple simple :

```python
from fastmcp import Client
from openai import OpenAI
import asyncio

async def main():
    # Connect to your MCP server
    async with Client("http://localhost:8000/mcp") as client:
        # Call an MCP tool directly
        result = await client.call_tool("add", {"a": 10, "b": 5})
        print("MCP Result:", result.content[0].text)
        # Use the result inside an LLM prompt
        llm = OpenAI(api_key="YOUR_KEY")
        response = llm.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant using MCP tools."},
                {"role": "user", "content": f"The sum of 10 and 5 is {result.content[0].text}. Explain how MCP helps with this integration."}
            ]
        )
        print(response.choices[0].message.content)
        
asyncio.run(main())
```

Dans cette configuration, le LLM peut combiner de manière transparente son raisonnement avec la logique de votre serveur. Il utilise le client MCP pour récupérer des données ou effectuer des calculs, puis incorpore la sortie dans sa conversation ou son workflow.

Cette approche vous permet de construire des systèmes intelligents qui vont au-delà des prompts statiques. Vous pouvez connecter votre LLM à des bases de données réelles, des API ou des outils d'automatisation, le transformant en un agent actif capable de lire, d'écrire et d'exécuter avec un contexte du monde réel.

## Conclusion

FastMCP simplifie l'intégration de vos données, API et outils dans le monde de l'IA via le Model Context Protocol. Avec seulement quelques lignes de Python, vous pouvez créer de puissants serveurs MCP qui se connectent aux modèles de langage, automatisent les workflows et gèrent la logique du monde réel de manière sécurisée.

Que vous construisiez une démo rapide ou un système de classe entreprise, FastMCP vous offre le chemin le plus court de l'idée à la production. Installez-le aujourd'hui, lancez votre premier serveur et explorez comment le MCP peut débloquer le prochain niveau d'intégration de l'IA.

Si vous souhaitez en savoir plus sur les concepts généraux du MCP et sur la manière de construire un serveur MCP avec Python, j'ai écrit un autre article à ce sujet [que vous pouvez consulter ici](https://www.freecodecamp.org/news/how-to-build-your-own-mcp-server-with-python/).

*J'espère que vous avez apprécié cet article. Inscrivez-vous à ma newsletter gratuite* [***TuringTalks.ai***](https://www.turingtalks.ai/) *pour plus de tutoriels pratiques sur l'IA. Vous pouvez également* [***visiter mon site web***](https://manishshivanandhan.com/)*.*