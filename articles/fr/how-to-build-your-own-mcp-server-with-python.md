---
title: Comment construire votre propre serveur MCP avec Python
subtitle: Apprenez à construire, déployer et étendre votre propre serveur Model Context
  Protocol (MCP) en utilisant Python pour permettre aux modèles d'IA d'accéder aux
  données du monde réel.
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-10-30T16:12:21.521Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-own-mcp-server-with-python
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761774966304/dace2a12-ea92-4c59-980a-5c16fb2d317d.png
tags:
- name: Python
  slug: python
- name: mcp
  slug: mcp
- name: Model Context Protocol
  slug: model-context-protocol
- name: AI
  slug: ai
seo_title: Comment construire votre propre serveur MCP avec Python
seo_desc: 'Artificial intelligence is evolving at a remarkable pace. Models today
  can reason, write, code, and analyze information in ways that once seemed impossible.

  But there’s one major limitation that still holds them back: context.

  Most AI models don’t ha...'
---

L'intelligence artificielle évolue à un rythme remarquable. Aujourd'hui, les modèles peuvent raisonner, écrire, coder et analyser des informations d'une manière qui semblait autrefois impossible.

Mais il reste une limitation majeure qui les freine : le contexte.

La plupart des modèles d'IA n'ont pas accès à votre système, à vos fichiers, à vos API ou à vos données en direct. Ils ne connaissent que ce que vous leur dites dans un prompt.

Le [Model Context Protocol](https://www.turingtalks.ai/p/how-model-context-protocol-works), également connu sous le nom de MCP, a été créé pour résoudre ce problème. Il permet aux modèles d'IA de se connecter en toute sécurité à vos propres outils, API et systèmes via de petits serveurs structurés appelés serveurs MCP.

Dans ce guide, vous apprendrez à construire votre propre serveur MCP en utilisant Python. Nous passerons en revue chaque partie du code et j'expliquerai son fonctionnement.

À la fin, vous aurez un serveur MCP opérationnel capable d'additionner des nombres, de retourner des mots aléatoires et de récupérer des données météo en direct sur Internet. Nous verrons également comment héberger ce serveur MCP sur le cloud.

### Ce que nous allons couvrir :

* [Qu'est-ce que le Model Context Protocol](#heading-comprendre-le-model-context-protocol) ?
    
* [Configuration de votre environnement](#heading-configuration-de-votre-environnement)
    
* [Création du projet](#heading-creation-du-projet)
    
* [Configuration de la journalisation](#heading-configuration-de-la-journalisation)
    
* [Création du serveur MCP](#heading-creation-du-serveur-mcp)
    
* [Définition des outils](#heading-definition-des-outils)
    
    * [Exemple 1 : Additionner deux nombres](#heading-exemple-1-additionner-deux-nombres)
        
    * [Exemple 2 : Retourner un mot secret aléatoire](#heading-exemple-2-retourner-un-mot-secret-aleatoire)
        
    * [Exemple 3 : Récupérer des données météo](#heading-exemple-3-recuperer-des-donnees-meteo)
        
* [Exécution du serveur](#heading-execution-du-serveur)
    
* [Tester les outils](#heading-tester-les-outils)
    
* [Déployer votre serveur MCP sur Sevalla](#heading-deployer-votre-serveur-mcp-sur-sevalla)
    
* [Pourquoi construire votre propre serveur MCP](#heading-pourquoi-construire-votre-propre-serveur-mcp)
    
* [Extension du serveur](#heading-extension-du-serveur)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que le Model Context Protocol ?

Avant de plonger dans le code, il est important de comprendre ce qu'est réellement le Model Context Protocol.

MCP est un standard ouvert qui définit comment les modèles d'IA et les systèmes externes communiquent. Vous pouvez le voir comme une API conçue spécifiquement pour les assistants d'IA.

Si une API permet à deux programmes informatiques d'échanger des données, le MCP permet à un modèle d'IA de parler à votre système. Cela ouvre des possibilités infinies.

Vous pourriez construire un serveur MCP qui permet à ChatGPT de lire des fichiers sur votre machine locale, ou un serveur qui appelle les API internes de votre entreprise pour récupérer des données. Vous pourriez même exposer vos propres fonctions Python afin qu'un modèle puisse les utiliser comme outils.

MCP rend cette communication structurée, sécurisée et extensible. Il repose sur des technologies web familières telles que les [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events), ou SSE, qui permettent au serveur d'envoyer des flux de données en temps réel au client.

## Configuration de votre environnement

Pour suivre ce tutoriel, vous aurez besoin de Python version 3.9 ou supérieure. Vous pouvez trouver le code de cet exemple [dans ce dépôt](https://github.com/sevalla-templates/python-demo-mcp-server).

Nous utiliserons une bibliothèque appelée [FastMCP](https://github.com/jlowin/fastmcp) qui simplifie le processus de construction de serveurs MCP. Vous pouvez l'installer via pip :

```powershell
pip install fastmcp requests
```

La bibliothèque `requests` sera utilisée pour effectuer des appels HTTP plus tard dans l'exemple. Une fois installée, vous êtes prêt à créer votre premier serveur MCP.

## Création du projet

Créez un nouveau fichier nommé `server.py` et commencez par importer les modules nécessaires :

```python
import logging
import os
import random
import sys
import requests
from mcp.server.fastmcp import FastMCP
```

Voici le rôle de chacun :

* Le module `logging` enregistre l'activité de votre serveur.
    
* `os` est utilisé pour accéder aux variables d'environnement comme les numéros de port.
    
* `random` nous aidera à générer des mots aléatoires.
    
* `sys` permet au script de s'arrêter proprement en cas d'erreur.
    
* `requests` nous permet de récupérer des données en direct via des API.
    
* Et enfin, `FastMCP` transforme nos fonctions Python en outils pouvant être appelés via le protocole MCP.
    

## Configuration de la journalisation

La journalisation (logging) vous donne de la visibilité sur ce que fait votre serveur. Elle est utile pendant le développement et vitale lorsque vous déployez votre serveur en production.

```python
name = "demo-mcp-server"
logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(name)
```

Cette configuration affiche les messages de log dans la console dans un format simple indiquant le nom du serveur, le niveau de log et le message. Chaque fois qu'un outil s'exécute, un message apparaîtra dans les logs, tel que :

```powershell
demo-mcp-server - INFO - Tool called: add(3, 5)
```

## Création du serveur MCP

Ensuite, nous allons créer l'instance du serveur qui hébergera nos outils.

```python
port = int(os.environ.get('PORT', 8080))
mcp = FastMCP(name, logger=logger, port=port)
```

Le serveur s'exécutera sur le port spécifié par la variable d'environnement `PORT`. Si cette variable n'est pas définie, il utilise par défaut le port 8080. L'objet `FastMCP` représente désormais votre serveur MCP en cours d'exécution.

## Définition des outils

Chaque fonction que vous décorez avec `@mcp.tool()` devient un outil accessible que les clients peuvent appeler. Commençons par un exemple simple : un outil d'addition.

### **Exemple 1 : Additionner deux nombres**

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    logger.info(f"Tool called: add({a}, {b})")
    return a + b
```

Cet outil prend deux nombres, journalise l'appel et retourne leur somme. Appeler `add(3, 5)` retournera 8.

Même s'il est simple, cela montre la structure de base de chaque outil MCP : des paramètres d'entrée, une instruction de journalisation et une valeur de retour.

### **Exemple 2 : Retourner un mot secret aléatoire**

Créons un autre outil qui retourne un mot aléatoire à partir d'une petite liste.

```python
@mcp.tool()
def get_secret_word() -> str:
    """Get a random secret word"""
    logger.info("Tool called: get_secret_word()")
    return random.choice(["apple", "banana", "cherry"])
```

Lorsque vous appelez cette fonction, elle choisit l'un des trois mots au hasard. Chaque fois que vous l'appelez, vous pourriez obtenir un résultat différent. Cette fonction démontre comment les outils MCP peuvent utiliser de la logique ou de l'aléatoire comme n'importe quelle fonction Python classique.

### Exemple 3 : Récupérer des données météo

Construisons maintenant quelque chose de plus pratique. Nous allons créer un outil qui récupère des données météo en direct sur le web en utilisant la bibliothèque `requests`.

```python
@mcp.tool()
def get_current_weather(city: str) -> str:
    """Get current weather for a city"""
    logger.info(f"Tool called: get_current_weather({city})")

try:
        endpoint = "https://wttr.in"
        response = requests.get(f"{endpoint}/{city}", timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logger.error(f"Error fetching weather data: {str(e)}")
        return f"Error fetching weather data: {str(e)}"
```

Cet outil accepte un nom de ville, envoie une requête au service météo public `wttr.in` et retourne le rapport météo au format texte. En cas de problème, comme un délai d'attente réseau ou un nom de ville invalide, la fonction journalise une erreur et retourne un message descriptif.

Appeler `get_current_weather("London")` affichera un court résumé météo pour cette ville.

## Exécution du serveur

Une fois tous vos outils définis, vous pouvez démarrer le serveur. Ajoutez le code suivant au bas de votre fichier :

```python
if __name__ == "__main__":
    logger.info(f"Starting MCP Server on port {port}...")
    try:
        mcp.run(transport="sse")
    except Exception as e:
        logger.error(f"Server error: {str(e)}")
        sys.exit(1)
    finally:
        logger.info("Server terminated")
```

Ce bloc démarre le serveur en utilisant la méthode de transport Server-Sent Events. Si quelque chose ne va pas, il journalise l'erreur et s'arrête proprement.

Vous pouvez maintenant lancer le serveur depuis votre terminal :

```powershell
python server.py
```

Si tout fonctionne, vous verrez :

```powershell
demo-mcp-server - INFO - Starting MCP Server on port 8080...
```

Votre serveur MCP est maintenant en ligne et prêt à accepter des requêtes.

## Tester les outils

Pour tester vos outils, vous avez besoin d'un client compatible MCP tel que ChatGPT avec les fonctionnalités développeur ou une autre application prenant en charge le protocole. Une fois connecté, le client listera vos outils disponibles.

Par exemple, vous pouvez envoyer une requête comme celle-ci :

```powershell
{
  "tool": "add",
  "args": [5, 7]
}
```

Le serveur répondra par :

```powershell
{
  "result": 12
}
```

Il en va de même pour les autres outils tels que `get_secret_word` ou `get_current_weather`.

Si vous souhaitez tester le serveur directement sans client MCP, vous pouvez toujours envoyer des requêtes HTTP manuellement (bien que cela contourne la logique complète du protocole).

Par exemple, pour tester votre outil météo, vous pouvez envoyer une simple requête GET :

```powershell
curl http://localhost:8080/tool/get_current_weather?city=London
```

ou en Python :

```python
import requests
response = requests.get("http://localhost:8080/tool/get_current_weather", params={"city": "London"})
print(response.text)
```

Cela n'utilisera pas la structure MCP (comme le streaming `sse`), mais c'est une vérification rapide pour s'assurer que votre serveur fonctionne.

## Déployer votre serveur MCP sur Sevalla

Vous pouvez exécuter ce serveur localement pour le développement. Mais si vous voulez l'utiliser dans des applications de production, vous devez le déployer sur un serveur.

Vous pouvez choisir n'importe quel fournisseur cloud, comme AWS, Heroku ou d'autres pour configurer ce projet. Mais je vais utiliser Sevalla.

[Sevalla](https://sevalla.com/) est un fournisseur moderne de Plateforme en tant que service (PaaS) basé sur l'utilisation. Il propose l'hébergement d'applications, de bases de données, de stockage d'objets et de sites statiques pour vos projets.

J'utilise Sevalla pour l'hébergement pour deux raisons :

* Chaque plateforme vous facturera la création d'une ressource cloud. Sevalla offre un crédit de 50 $ à utiliser, nous n'aurons donc aucun coût pour cet exemple.
    
* Sevalla dispose d'un [template pour serveur MCP Python](https://docs.sevalla.com/templates/overview), ce qui simplifie l'installation manuelle et la configuration de chaque ressource nécessaire.
    

[Connectez-vous](https://app.sevalla.com/login) à Sevalla et cliquez sur Templates. Vous verrez "Python MCP Server" parmi les modèles disponibles.

![Sevalla Templates](https://cdn.hashnode.com/res/hashnode/image/upload/v1761652364887/5003918a-f19a-42bf-94ad-306a3f6ab93c.png align="center")

Cliquez sur le modèle "Python MCP Server". Vous verrez les ressources nécessaires pour provisionner l'application. Cliquez sur "Deploy Template".

![Python MCP Server Resources](https://cdn.hashnode.com/res/hashnode/image/upload/v1761652387263/871bf43f-214a-49c4-9734-7f71d0e5ce32.png align="center")

Vous pouvez voir la ressource en cours de provisionnement. Si le déploiement ne démarre pas automatiquement, cliquez sur "Deploy now".

![Python MCP Server Resources Provisioning](https://cdn.hashnode.com/res/hashnode/image/upload/v1761652411264/3e5a71c0-71c1-4cf9-92c2-e01fa77b7f45.png align="center")

Attendez quelques minutes. Une fois le déploiement terminé, vous verrez une coche verte.

![Python MCP Server Deployment](https://cdn.hashnode.com/res/hashnode/image/upload/v1761652436109/68303890-91a4-4c8e-90d1-f6c142c571a6.png align="center")

Une fois le déploiement terminé, cliquez sur "Visit app". Vous obtiendrez une URL cloud, par exemple [https://python-mcp-server-rlfdk.sevalla.app](https://python-mcp-server-rlfdk.sevalla.app/). Utilisez-la comme URL de base au lieu de l'URL localhost:3000.

Vous avez maintenant un serveur MCP de qualité production fonctionnant sur le cloud. Vous pouvez le brancher sur n'importe quelle application pour récupérer des données pour nos applications LLM.

## Pourquoi construire votre propre serveur MCP ?

Construire un serveur MCP vous donne le contrôle et la flexibilité.

Vous pouvez connecter des modèles d'IA directement à vos bases de données ou systèmes internes, automatiser des actions répétitives et décider exactement à quelles données un modèle d'IA peut accéder.

Cela vous permet également d'expérimenter rapidement. Vous pouvez commencer petit avec quelques outils simples et étendre plus tard vers des workflows complexes.

En créant votre propre serveur MCP, vous n'écrivez pas seulement du code – vous définissez comment les systèmes intelligents interagissent avec le monde réel à travers votre logique et vos données.

## Extension du serveur

Une fois que vous maîtrisez les bases, il est facile d'étendre votre serveur. Vous pouvez ajouter des outils qui lisent et écrivent des fichiers, interrogent des bases de données, interagissent avec des API comme GitHub ou Slack, ou surveillent votre système. Chaque nouvelle fonction devient un autre outil que votre IA peut utiliser.

Cette approche modulaire vous permet de construire tout un écosystème d'outils conscients de l'IA, chacun effectuant une tâche spécifique mais travaillant ensemble via la même interface MCP.

## Conclusion

Dans ce tutoriel, vous avez appris à créer un serveur MCP en Python en utilisant la bibliothèque FastMCP. Vous avez configuré la journalisation, mis en place un serveur, défini plusieurs outils et appris à l'exécuter et à le tester. Vous avez également vu avec quelle facilité ces outils peuvent exposer des fonctionnalités réelles, comme la récupération de données météo en direct ou l'exécution de calculs de base.

Cette structure est simple mais puissante. Avec seulement quelques lignes de code Python, vous pouvez construire des ponts entre vos systèmes et des modèles intelligents. Le Model Context Protocol représente une étape vers des systèmes d'IA capables de véritablement comprendre et interagir avec les données et les actions du monde réel.

*J'espère que vous avez apprécié cet article. Inscrivez-vous à ma newsletter gratuite* [***TuringTalks.ai***](https://www.turingtalks.ai/) *pour plus de tutoriels pratiques sur l'IA. Vous pouvez également* [***visiter mon site web***](https://manishshivanandhan.com/)*.*