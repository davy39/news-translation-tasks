---
title: Comment construire et déployer un agent IA avec LangChain, FastAPI et Sevalla
subtitle: ''
author: Manish Shivanandhan
date: '2026-01-08T23:43:55.189Z'
originalURL: https://freecodecamp.org/news/build-ai-agent-with-langchain-fastapi-and-sevalla
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1767915474046/728b3bd5-2dfe-45a3-a2a9-c682e4719d7d.png
tags:
- name: ai agents
  slug: ai-agents
- name: FastAPI
  slug: fastapi
- name: langchain
  slug: langchain
- name: AI
  slug: ai
seo_title: Comment construire et déployer un agent IA avec LangChain, FastAPI et Sevalla
seo_desc: 'Artificial intelligence is changing how we build software. Just a few years
  ago, writing code that could talk, decide, or use external data felt hard.

  Today, thanks to new tools, developers can build smart agents that read messages,
  reason about them...'
---

L'intelligence artificielle change la façon dont nous développons des logiciels. Il y a seulement quelques années, écrire du code capable de parler, de décider ou d'utiliser des données externes semblait difficile.

Aujourd'hui, grâce à de nouveaux outils, les développeurs peuvent construire des agents intelligents qui lisent des messages, raisonnent à leur sujet et appellent des fonctions par eux-mêmes.

L'une de ces plateformes qui facilite cela est [LangChain](https://github.com/langchain-ai/langchain). Avec LangChain, vous pouvez lier des modèles de langage, des outils et des applications ensemble. Vous pouvez également envelopper votre agent dans un serveur FastAPI, puis le pousser vers une plateforme cloud pour le déploiement.

Cet article vous guidera à travers la construction de votre premier agent IA. Vous apprendrez ce qu'est LangChain, comment construire un agent, comment le servir via FastAPI et comment le déployer sur Sevalla.

## Ce que nous allons couvrir

* [Qu'est-ce que LangChain ?](#heading-quest-ce-que-langchain)
  
* [Comment construire votre premier agent avec LangChain](#heading-comment-construire-votre-premier-agent-avec-langchain)
  
* [Envelopper votre agent avec FastAPI](#heading-envelopper-votre-agent-avec-fastapi)
  
* [Comment déployer votre agent IA sur Sevalla](#heading-comment-deployer-votre-agent-ia-sur-sevalla)
  
* [Conclusion](#heading-conclusion)
  

## Qu'est-ce que LangChain ?

LangChain est un framework pour travailler avec des grands modèles de langage. Il vous aide à construire des applications qui pensent, raisonnent et agissent.

![Langchain](https://cdn.hashnode.com/res/hashnode/image/upload/v1767629343581/a7f55a7e-f9fa-4d34-9ce5-666adf9cb93d.jpeg align="center")

Un modèle seul ne donne que des réponses textuelles, mais LangChain lui permet de faire plus. Il permet à un modèle d'appeler des fonctions, d'utiliser des outils, de se connecter avec des bases de données et de suivre des flux de travail.

Pensez à LangChain comme un pont. D'un côté se trouve le modèle de langage. De l'autre côté se trouvent vos outils, sources de données et logique métier. LangChain indique au modèle quels outils existent, quand les utiliser et comment répondre. Cela en fait un outil idéal pour construire des agents qui répondent à des questions, automatisent des tâches ou gèrent des flux complexes.

De nombreux développeurs utilisent LangChain en raison de sa flexibilité. Il supporte de nombreux modèles d'IA. Il s'intègre bien avec Python.

LangChain facilite également le passage du prototype à la production. Une fois que vous avez appris à créer un agent, vous pouvez réutiliser le modèle pour des cas d'utilisation plus avancés.

J'ai récemment publié un tutoriel détaillé sur [langchain](https://www.turingtalks.ai/p/langchain-tutorial) ici.

## Comment construire votre premier agent avec LangChain

Construisons notre premier agent. Il répondra aux questions des utilisateurs et [appellera un outil](https://www.freecodecamp.org/news/how-to-build-your-first-mcp-server-using-fastmcp/) lorsque nécessaire.

Nous lui donnerons un outil météo simple, puis lui demanderons la météo dans une ville. Avant cela, créez un fichier appelé `.env` et ajoutez votre clé API OpenAI. LangChain l'utilisera automatiquement lors des requêtes à OpenAI.

```python
OPENAI_API_KEY=<key>
```

Voici le code pour notre agent :

```python

from langchain.agents import create_agent
from dotenv import load_dotenv

# charger les variables d'environnement
load_dotenv()

# définir l'outil que le LLM peut appeler
def get_weather(city: str) -> str:
    """Obtenir la météo pour une ville donnée."""
    return f"Il fait toujours ensoleillé à {city} !"

# Créer un agent
agent = create_agent(
    model="gpt-4o",
    tools=[get_weather],
    system_prompt="Vous êtes un assistant utile",
)

result = agent.invoke({"messages":[{"role":"user","content":"Quel temps fait-il à San Francisco ?"}]})
```

Ce petit programme montre la puissance des agents LangChain.

Tout d'abord, nous importons `create_agent`, qui nous aide à construire l'agent. Ensuite, nous écrivons une fonction appelée `get_weather`. Elle prend un nom de ville et retourne une phrase amicale.

La fonction agit comme notre outil. Un outil est quelque chose que l'agent peut utiliser. Dans des projets réels, les outils peuvent récupérer des prix, stocker des notes ou appeler des API.

Ensuite, nous appelons `create_agent`. Nous lui donnons trois choses. Nous passons le modèle que nous voulons utiliser. Nous listons les outils que nous voulons qu'il appelle. Et nous donnons un prompt système. Le prompt système indique à l'agent qui il est et comment il doit se comporter.

Enfin, nous exécutons l'agent. Nous appelons `invoke` avec un message.

L'utilisateur demande la météo à San Francisco. L'agent lit ce message. Il voit que la question nécessite la fonction météo. Il appelle donc notre outil `get_weather`, passe la ville et retourne une réponse.

Même si cet exemple est minuscule, il capture l'idée principale. L'agent lit le langage naturel, détermine quel outil utiliser et envoie une réponse.

Plus tard, vous pouvez ajouter plus d'outils ou remplacer la fonction météo par une qui se connecte à une vraie API. Mais cela suffit pour que nous l'enveloppons et le déployions.

## Envelopper votre agent avec FastAPI

L'étape suivante consiste à servir notre agent. [FastAPI](https://fastapi.tiangolo.com/) nous aide à exposer notre agent via un endpoint HTTP. De cette façon, les utilisateurs et les systèmes peuvent l'appeler via une URL, envoyer des messages et obtenir des réponses.

Pour commencer, vous installez FastAPI et écrivez un fichier simple comme `main.py`. À l'intérieur, vous importez FastAPI, chargez l'agent et écrivez une route.

Lorsque quelqu'un poste une question, l'API la transmet à l'agent et retourne la réponse. Le flux est simple.

L'utilisateur parle à FastAPI. FastAPI parle à votre agent. L'agent pense et répond. Voici l'enveloppe FastAPI pour votre agent.

```python
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from langchain.agents import create_agent
from dotenv import load_dotenv
import os

load_dotenv()

# définir l'outil que le LLM peut appeler
def get_weather(city: str) -> str:
    """Obtenir la météo pour une ville donnée."""
    return f"Il fait toujours ensoleillé à {city} !"

# Créer un agent
agent = create_agent(
    model="gpt-4o",
    tools=[get_weather],
    system_prompt="Vous êtes un assistant utile",
)

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Bienvenue à votre premier agent"}

@app.post("/chat")
def chat(request: ChatRequest):
    result = agent.invoke({"messages":[{"role":"user","content":request.message}]})
    return {"reply": result["messages"][-1].content}

def main():
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
```

Ici, FastAPI définit un endpoint `/chat`. Lorsque quelqu'un envoie un message, le serveur appelle notre agent. L'agent le traite comme avant. Ensuite, FastAPI retourne une réponse JSON propre. La couche API cache la complexité derrière une interface simple.

À ce stade, vous avez un serveur d'agent fonctionnel. Vous pouvez l'exécuter sur votre machine, l'appeler avec Postman ou cURL, et vérifier les réponses. Lorsque cela fonctionne, vous êtes prêt à déployer.

![Résultat Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1767629386493/e5699447-d82e-4c73-87f8-87cec2d7dac2.png align="center")

## Comment déployer votre agent IA sur Sevalla

Vous pouvez choisir n'importe quel fournisseur de cloud, comme AWS, DigitalOcean, ou d'autres pour héberger votre agent. Je vais utiliser Sevalla pour cet exemple.

[Sevalla](https://sevalla.com/) est un fournisseur PaaS convivial pour les développeurs. Il offre l'hébergement d'applications, de bases de données, de stockage d'objets et de sites statiques pour vos projets.

Chaque plateforme vous facturera pour la création d'une ressource cloud. Sevalla offre un crédit de 50 $ à utiliser, donc nous n'aurons aucun coût pour cet exemple.

Poussons ce projet sur GitHub afin de pouvoir connecter notre dépôt à Sevalla. Nous pouvons également activer les déploiements automatiques afin que toute nouvelle modification du dépôt soit automatiquement déployée.

Vous pouvez également [forker mon dépôt](https://github.com/manishmshiva/first-agent-with-fastapi) depuis ici.

[Connectez-vous](https://app.sevalla.com/login) à Sevalla et cliquez sur Applications -> Créer une nouvelle application. Vous pouvez voir l'option pour lier votre dépôt GitHub afin de créer une nouvelle application.

![Créer une application](https://cdn.hashnode.com/res/hashnode/image/upload/v1767629443568/85e00d7f-c296-4bed-94ba-8e2e5bbdb0ba.png align="center")

Utilisez les paramètres par défaut. Cliquez sur "Créer une application". Maintenant, nous devons ajouter notre clé API OpenAI aux variables d'environnement. Cliquez sur la section "Variables d'environnement" une fois l'application créée, et enregistrez la valeur `OPENAI_API_KEY` comme variable d'environnement.

![Variables d'environnement Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1767629507196/0ae254e2-00f6-46a1-8535-c3af006022c6.png align="center")

Nous sommes maintenant prêts à déployer notre application. Cliquez sur "Déploiements" et cliquez sur "Déployer maintenant". Il faudra 2 à 3 minutes pour que le déploiement soit terminé.

![Déploiement Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1767629546289/cbdc2f5d-4902-4799-aed4-2177695748bc.png align="center")

Une fois terminé, cliquez sur "Visiter l'application". Vous verrez l'application servie via une URL se terminant par `sevalla.app`. C'est votre nouvelle URL racine. Vous pouvez remplacer `localhost:8000` par cette URL et tester dans Postman.

![Réponse Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1767629568646/e849222d-0cb5-433f-a399-0e8a63d891d1.png align="center")

Félicitations ! Votre premier agent IA avec appel d'outil est maintenant en ligne. Vous pouvez l'étendre en ajoutant plus d'outils et d'autres capacités, et en poussant votre code sur GitHub, et Sevalla déployera automatiquement votre application en production.

## Conclusion

Construire des agents IA n'est plus une tâche réservée aux experts. Avec LangChain, vous pouvez écrire quelques lignes et créer des outils de raisonnement qui répondent aux utilisateurs et appellent des fonctions par eux-mêmes.

En enveloppant l'agent avec FastAPI, vous lui donnez une porte d'entrée que les applications et les utilisateurs peuvent accéder. Enfin, Sevalla facilite la mise en ligne de votre agent, sa surveillance et son exécution en production.

Ce parcours, de l'idée d'agent au service déployé, montre à quoi ressemble le développement moderne de l'IA. Vous commencez petit. Vous explorez des outils. Vous les enveloppez et les déployez.

Ensuite, vous itérez, ajoutez plus de capacités, améliorez la logique et branchez des outils réels. Avant longtemps, vous avez un agent intelligent et vivant en ligne. C'est la puissance de cette nouvelle vague de technologie.

*J'espère que vous avez apprécié cet article. Inscrivez-vous à ma newsletter gratuite* [***TuringTalks.ai***](https://www.turingtalks.ai/) *pour plus de tutoriels pratiques sur l'IA. Vous pouvez également* [***visiter mon site web***](https://manishshivanandhan.com/)*.*