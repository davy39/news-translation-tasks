---
title: Comment créer un agent de planification d'études par IA avec Gemini en Python
subtitle: ''
author: Tarun Singh
co_authors: []
series: null
date: '2025-09-05T15:19:14.262Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-ai-study-planner-agent-using-gemini-in-python
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757085526077/66391609-bf27-4206-aa29-382508d15ee8.png
tags:
- name: Python
  slug: python
- name: AI
  slug: ai
- name: agentic AI
  slug: agentic-ai
- name: Machine Learning
  slug: machine-learning
- name: llm
  slug: llm
seo_title: Comment créer un agent de planification d'études par IA avec Gemini en
  Python
seo_desc: The world is shifting from simple AI chatbots answering our queries to full-fledged
  systems that are capable of so much more. AI Agents can not only answer our queries
  but can also perform tasks we give them independently, making them much more power...
---

Le monde évolue, passant de simples chatbots IA répondant à nos questions à des systèmes complets capables de bien plus. Les agents IA peuvent non seulement répondre à nos requêtes, mais aussi accomplir les tâches que nous leur confions de manière indépendante, ce qui les rend beaucoup plus puissants et utiles.

Dans ce tutoriel, vous allez construire un agent avancé basé sur le web qui servira de planificateur d'études virtuel. Cet agent IA sera capable de comprendre vos objectifs, de prendre des décisions et d'agir pour les atteindre.

Ce projet va au-delà de la simple conversation de base. Vous apprendrez à construire un agent basé sur des objectifs avec deux capacités clés :

1. **Mémoire :** L'agent se souviendra de l'historique complet de votre conversation, ce qui lui permettra de fournir des conseils de suivi et d'adapter ses plans en fonction de vos retours.
    
2. **Utilisation d'outils (Tool Use) :** L'agent sera capable d'utiliser un outil de recherche pour trouver des ressources en ligne pertinentes, ce qui en fait un assistant plus puissant qu'un outil s'appuyant uniquement sur ses connaissances internes.
    

Vous apprendrez à créer un système complet avec une interface utilisateur web simple construite avec Flask et Tailwind CSS, offrant une base solide pour construire des agents encore plus complexes à l'avenir. Alors, commençons.

## Table des matières :

* [Prérequis](#heading-pre-requis)
    
* [Outils que vous utiliserez pour créer cet agent](#heading-outils-que-vous-utiliserez-pour-creer-cet-agent)
    
* [Comprendre les agents IA](#heading-comprendre-les-agents-ia)
    
    * [Que sont les agents IA ? Combien de types existe-t-il ?](#heading-que-sont-les-agents-ia-combien-de-types-existe-t-il)
        
    * [En quoi les agents IA sont-ils uniques par rapport aux autres outils d'IA ?](#heading-en-quoi-les-agents-ia-sont-ils-uniques-par-rapport-aux-autres-outils-dia)
        
* [Comment configurer votre environnement](#heading-comment-configurer-votre-environnement)
    
    * [1\. Créer un répertoire de projet](#heading-1-creer-un-repertoire-de-projet)
        
    * [2\. Créer un environnement virtuel](#heading-2-creer-un-environnement-virtuel)
        
    * [3\. Installer les dépendances](#heading-3-installer-les-dependances)
        
    * [4\. Obtenir votre clé API Gemini](#heading-4-obtenir-votre-cle-api-gemini)
        
    * [5\. Ajouter votre clé au fichier .env](#heading-5-ajouter-votre-cle-au-fichier-env)
        
* [Comment créer la logique de l'agent en temps réel](#heading-comment-creer-la-logique-de-lagent-en-temps-reel)
    
    * [Créer le client Gemini (avec recherche web)](#heading-creer-le-client-gemini-avec-recherche-web)
        
    * [Créer le backend et le frontend Flask](#heading-creer-le-backend-et-le-frontend-flask)
        
* [Comment tester l'agent IA](#heading-comment-tester-lagent-ia)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de suivre ce tutoriel, vous devriez avoir :

* Des connaissances de base en Python
    
* Les bases du développement web
    
* Python 3+ installé sur votre machine
    
* VS Code ou un autre IDE de votre choix installé
    

## Outils que vous utiliserez pour créer cet agent

Pour construire cet agent de planification d'études, vous aurez besoin de quelques composants :

* **Google Gemini API :** C'est le service d'IA central qui fournit le modèle génératif. Il permet à notre agent de comprendre le langage naturel, de raisonner et de générer des réponses de type humain.
    
* **Flask :** Il s'agit d'un Framework web léger pour Python. Nous l'utiliserons pour créer notre serveur web (c'est-à-dire le backend). Son objectif principal ici est de gérer les requêtes web du navigateur de l'utilisateur, de les traiter et de renvoyer une réponse.
    
* **Tailwind CSS :** C'est un Framework CSS pour construire l'interface utilisateur (c'est-à-dire le frontend). Au lieu d'écrire du CSS personnalisé, vous utilisez des classes prédéfinies comme `bg-blue-300`, `m-4`, etc., pour styliser la page directement dans votre HTML.
    
* **Python-dotenv :** Cette bibliothèque nous aide à gérer les variables d'environnement.
    
* **DuckDuckGo Search :** Cette bibliothèque offre un moyen simple d'effectuer des recherches web en temps réel. Elle agit comme l'\"outil\" pour notre agent IA. Lorsqu'un utilisateur pose une question qui nécessite des informations externes, notre agent peut utiliser cet outil pour trouver des ressources pertinentes sur le web et utiliser ces informations pour formuler une réponse.
    

## Comprendre les agents IA

Avant de plonger dans le code, couvrons les bases pour que vous compreniez ce qu'est un agent IA et de quoi il est capable.

### Que sont les agents IA ? Combien de types existe-t-il ?

Un agent IA est un logiciel capable d'effectuer des tâches de manière autonome pour le compte d'un utilisateur. Les agents IA perçoivent leur environnement, traitent les informations et agissent pour atteindre les objectifs de l'utilisateur. Contrairement aux programmes fixes, un agent peut raisonner et s'adapter.

Il existe différents types d'agents, notamment :

* **Réflexe simple** (agit sur l'entrée actuelle, comme un thermostat)
    
* **Basé sur des modèles** (utilise une carte interne, comme les aspirateurs robots)
    
* **Basé sur des objectifs** (planifie pour atteindre des buts, comme un planificateur d'études)
    
* **Basé sur l'utilité** (choisit les meilleurs résultats, comme les bots de trading)
    
* **Agents apprenants** (s'améliorent avec le temps, comme les systèmes de recommandation).
    

### En quoi les agents IA sont-ils uniques par rapport aux autres outils d'IA ?

Les agents IA utilisent des technologies comme les LLM, mais ils s'en distinguent par leur autonomie et leur capacité d'action. Comprenons ces différents types d'outils d'IA plus en détail :

1. **Grands Modèles de Langage (LLM) :** Les LLM sont le cerveau de l'opération. Ils sont entraînés sur un très grand ensemble de données pour comprendre et traiter les requêtes des utilisateurs en langage naturel afin de générer une sortie humaine. GPT d'OpenAI, Gemini de Google et Claude d'Anthropic sont tous des exemples de LLM.
    
2. **Génération Augmentée par Récupération (RAG) :** Le RAG est un processus ou une technique qui permet aux LLM de récupérer des informations non seulement à partir de leurs données d'entraînement, mais aussi de sources externes, comme une base de données ou une bibliothèque de documents, pour répondre aux requêtes. Bien que le RAG récupère des informations, il ne décide pas de manière indépendante d'effectuer une action ou de planifier une séquence d'étapes pour atteindre un objectif.
    
3. **Agents IA :** Comme expliqué plus haut, les agents sont les systèmes capables d'exécuter des tâches utilisateur en utilisant les LLM comme moteur de raisonnement principal. L'architecture complète d'un agent lui permet de percevoir son environnement, de planifier, d'agir et d'apprendre (mémoire, basée sur les interactions passées).
    

Dans ce tutoriel, vous allez utiliser un LLM (Gemini) pour le raisonnement, ainsi qu'un moteur de recherche web, DuckDuckGo search, pour construire l'agent. Passons maintenant à l'étape suivante.

## Comment configurer votre environnement

Avant de pouvoir construire votre agent IA de planification d'études virtuel, vous devrez configurer votre environnement de développement. Voici les étapes à suivre :

### 1\. Créer un répertoire de projet

Tout d'abord, créez un nouveau dossier avec le nom de votre choix et déplacez-vous dans ce répertoire :

```bash
mkdir study-planner
cd study-planner
```

### 2\. Créer un environnement virtuel

En Python, il est toujours recommandé de travailler dans un environnement virtuel. Créez-en un et activez-le comme ceci :

```bash
python -m venv venv
```

Maintenant, activez l'environnement virtuel :

```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3\. Installer les dépendances

Nous aurons besoin de quelques packages ou dépendances pour construire l'agent planificateur d'études, notamment :

* `flask` : serveur web
    
* `google-generativeai` : client Gemini
    
* `python-dotenv` : charger GEMINI_API_KEY depuis .env
    
* `requests` : utilitaire HTTP (toujours utile)
    
* `duckduckgo-search` : recherche web réelle
    

Vous pouvez les installer avec une seule commande :

```bash
pip install flask google-generativeai python-dotenv requests duckduckgo-search
```

### 4\. Obtenir votre clé API Gemini

Allez sur [Google AI Studio](https://aistudio.google.com/) et créez un nouveau compte (si vous n'en avez pas déjà un).

![Page d'accueil de Google AI Studio](https://cdn.hashnode.com/res/hashnode/image/upload/v1756829119333/fd2f68f8-2d15-491e-9b9d-a5563f3d926b.png align="center")

Ensuite, obtenez une nouvelle clé API en cliquant sur **Create API Key** dans la section [API Keys](https://platform.openai.com/api-keys).

![Tableau de bord des clés API Google AI Studio](https://cdn.hashnode.com/res/hashnode/image/upload/v1756829166748/a79ec404-2267-42f3-8185-a88903f5bcaf.png align="center")

**NOTE :** Une fois la clé API générée, SAUVEGARDEZ-LA quelque part. Vous ne pourrez peut-être plus récupérer la même clé.

### 5\. Ajouter votre clé au fichier `.env`

Créez un fichier `.env` à l'intérieur de `backend/` et ajoutez votre clé API.

```bash
GEMINI_API_KEY=votre_cle_api_ici
```

Vous devriez maintenant avoir configuré votre environnement de développement avec succès. Vous êtes prêt à construire l'agent IA Virtual Study Planner. Commençons !

## Comment créer la logique de l'agent en temps réel

Le cœur de ce projet est une boucle continue qui accepte l'entrée de l'utilisateur, maintient un historique de conversation et envoie cet historique à l'API Gemini pour générer une réponse. C'est ainsi que nous donnons de la mémoire à l'agent.

### Créer le client Gemini (avec recherche web)

Créez un nouveau fichier dans `backend/gemini_client.py` :

```python
# backend/gemini_client.py
import os
from typing import List, Dict
import google.generativeai as genai
from dotenv import load_dotenv
from duckduckgo_search import DDGS

# Charger les variables d'environnement
load_dotenv()

# La fonction utilise une requête et la bibliothèque duckduckgo_search pour effectuer une recherche web
def perform_web_search(query: str, max_results: int = 6) -> List[Dict[str, str]]:
    """Effectue une recherche DuckDuckGo et retourne une liste de résultats.

    Chaque résultat contient : title, href, body.
    """
    results: List[Dict[str, str]] = []
    try:
        with DDGS() as ddgs:
            for result in ddgs.text(query, max_results=max_results):
                if not isinstance(result, dict):
                    continue
                title = result.get('title') or ''
                href = result.get('href') or ''
                body = result.get('body') or ''
                if title and href:
                    results.append({
                        'title': title,
                        'href': href,
                        'body': body,
                    })
        return results
    except Exception as e:
        print(f"DuckDuckGo search error: {e}")
        return []

# Une classe qui gère l'interaction avec l'API Gemini et la logique de l'agent
class GeminiClient:
    def __init__(self):
        try:
            genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
            self.model = genai.GenerativeModel('gemini-1.5-flash')
            self.chat = self.model.start_chat(history=[])
        except Exception as e:
            print(f"Error configuring Gemini API: {e}")
            self.chat = None

    def generate_response(self, user_input: str) -> str:
        """Génère une réponse IA avec recherche web optionnelle par préfixe.

        Pour déclencher la recherche web, commencez votre message par :
        - "search: <requête>"
        - "/search <requête>"
        Sinon, le modèle répond directement en utilisant l'historique.
        """
        if not self.chat:
            return "Le service d'IA n'est pas configuré correctement."

        try:
            text = user_input or ""
            lower = text.strip().lower()

            # Déclencheur de recherche
            search_query = None
            if lower.startswith("search:"):
                search_query = text.split(":", 1)[1].strip()
            elif lower.startswith("/search "):
                search_query = text.split(" ", 1)[1].strip()

            if search_query:
                web_results = perform_web_search(search_query, max_results=6)
                if not web_results:
                    return "Je n'ai pas pu récupérer de résultats web pour le moment. Veuillez réessayer."

                # Construire le contexte avec des références numérotées
                refs_lines = []
                for idx, item in enumerate(web_results, start=1):
                    refs_lines.append(f"[{idx}] {item['title']} — {item['href']}\n{item['body']}")
                refs_block = "\n\n".join(refs_lines)

                system_prompt = (
                    "Vous êtes un assistant de recherche IA. Utilisez les résultats de recherche fournis pour répondre à la requête. "
                    "Synthétisez de manière concise, citez les sources comme [1], [2] et incluez un bref résumé."
                )
                composed = (
                    f"<system>\n{system_prompt}\n</system>\n"
                    f"<user_query>\n{search_query}\n</user_query>\n"
                    f"<web_results>\n{refs_block}\n</web_results>"
                )
                response = self.chat.send_message(composed)
                return response.text

            # Par défaut : chat normal
            response = self.chat.send_message(text)
            return response.text
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Désolé, j'ai rencontré une erreur lors du traitement de votre demande."
```

Comprenons ce qui se passe dans le code ci-dessus :

* La fonction `perform_web_search()` :
    
    * Nous gardons une session de chat ouverte afin que le modèle se souvienne de la conversation.
        
    * Si un message commence par `search:` ou `/search`, le service DuckDuckGo est appelé, rassemble quelques résultats et les transmet à Gemini avec une courte instruction pour citer les sources.
        
    * Sinon, nous envoyons simplement le message normalement.
        
* La classe `GeminiClient` :
    
    * La classe `GeminiClient` est conçue pour se connecter et communiquer avec l'IA Gemini de Google. Dans la méthode `__init__`, elle appelle d'abord `genai.configure()` avec la clé API des variables d'environnement, ce qui déverrouille l'accès aux services de Gemini.
        
    * Ensuite, `self.model = genai.GenerativeModel('gemini-1.5-flash')` charge le modèle Gemini spécifique, et `self.chat = self.model.start_chat(history=[])` démarre une nouvelle conversation sans historique préalable. Ainsi, la classe est prête à envoyer et recevoir des réponses.
        
    * L'action réelle se produit dans `generate_response()`. Si le message d'un utilisateur commence par `search:` ou `/search`, cela déclenche une recherche DuckDuckGo via `perform_web_search()`.
        
    * Les résultats sont formatés avec titres, liens et extraits, puis transmis à Gemini pour créer une réponse claire et citée.
        
    * Si aucune commande de recherche n'est utilisée, elle discute simplement avec Gemini en utilisant l'entrée donnée. La gestion des erreurs est intégrée, donc au lieu de planter, elle renvoie un message de sécurité général.
        

### Créer le backend et le frontend Flask

Ensuite, nous allons configurer le serveur web Flask pour connecter la logique de notre agent à une interface web simple.

#### Le Backend Flask

Créez un nouveau dossier `backend` à l'intérieur du répertoire `study-planner`, et ajoutez un nouveau fichier `app.py` :

```python
# backend/app.py
import os
from flask import Flask, render_template, request, jsonify
from gemini_client import GeminiClient

app = Flask(__name__, template_folder='../templates')
client = GeminiClient()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    payload = request.get_json(silent=True) or {}
    user_message = payload.get('message', '').strip()
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        response_text = client.generate_response(user_message)
        return jsonify({'response': response_text})
    except Exception as e:
        return jsonify({'error': 'Error generating response'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

Ce qu'il fait :

* `@app.route('/')` : C'est la page d'accueil. Lorsqu'un utilisateur navigue vers l'URL principale (ex: `http://localhost:5000`), Flask exécute la fonction `index()`, qui affiche simplement le fichier `index.html`. Cela sert l'interface utilisateur au navigateur.
    
* Ensuite, nous avons créé `@app.route('/api/chat', methods=['POST'])`, le point de terminaison de l'API. Lorsque l'utilisateur clique sur \"Envoyer\" sur le frontend, le JavaScript envoie une requête `POST` à cette URL. La fonction `chat()` reçoit alors le message de l'utilisateur, le transmet au `GeminiClient` pour obtenir une réponse, puis renvoie cette réponse au frontend sous forme d'objet JSON.
    

#### Le Frontend Flask

Créer un nouveau dossier nommé `templates` dans le répertoire racine de votre projet. À l'intérieur, créez un fichier `index.html`.

```xml
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>IA Planificateur d'Études</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
      body {
        background-color: #f3f4f6;
      }
      .chat-container {
        max-width: 768px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        height: 100vh;
      }
      .message-bubble {
        padding: 1rem;
        border-radius: 1.5rem;
        max-width: 80%;
        margin-bottom: 1rem;
      }
      .user-message {
        background-color: #3b82f6;
        color: white;
        align-self: flex-end;
      }
      .agent-message {
        background-color: #e5e7eb;
        color: #374151;
        align-self: flex-start;
      }
    </style>
  </head>
  <body class="bg-gray-100">
    <div class="chat-container">
      <header
        class="bg-white shadow-sm p-4 text-center font-bold text-xl text-gray-800"
      >
        IA Planificateur d'Études
      </header>

      <main id="chat-history" class="flex-1 overflow-y-auto p-4 space-y-4">
        <div class="message-bubble agent-message">
          Bonjour ! Je suis votre IA de planification d'études. Quel sujet aimeriez-vous étudier aujourd'hui ?
        </div>
      </main>

      <footer class="bg-white p-4">
        <div class="flex items-center">
          <input
            type="text"
            id="user-input"
            class="flex-1 p-3 border-2 border-gray-300 rounded-full focus:outline-none focus:border-blue-500"
            placeholder="Tapez votre message..."
          />
          <button
            id="send-btn"
            class="ml-4 px-6 py-3 bg-blue-500 text-white rounded-full font-semibold hover:bg-blue-600 transition-colors"
          >
            Envoyer
          </button>
        </div>
      </footer>
    </div>

    <script>
      const chatHistory = document.getElementById("chat-history");
      const userInput = document.getElementById("user-input");
      const sendBtn = document.getElementById("send-btn");

      function addMessage(sender, text) {
        const messageElement = document.createElement("div");
        messageElement.classList.add(
          "message-bubble",
          sender === "user" ? "user-message" : "agent-message"
        );
        messageElement.textContent = text;
        chatHistory.appendChild(messageElement);
        chatHistory.scrollTop = chatHistory.scrollHeight;
      }

      async function sendMessage() {
        const message = userInput.value.trim();
        if (message === "") return;

        addMessage("user", message);
        userInput.value = "";

        try {
          const response = await fetch("/api/chat", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ message: message }),
          });

          const data = await response.json();
          if (data.response) {
            addMessage("agent", data.response);
          } else if (data.error) {
            addMessage("agent", `Erreur: ${data.error}`);
          } else {
            addMessage("agent", "Réponse inattendue du serveur.");
          }
        } catch (error) {
          console.error("Erreur:", error);
          addMessage("agent", "Désolé, un problème est survenu. Veuillez réessayer.");
        }
      }

      sendBtn.addEventListener("click", sendMessage);
      userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
          sendMessage();
        }
      });
    </script>
  </body>
</html>
```

C'est toute l'interface. C'est juste une page avec une zone de texte et un bouton d'envoi. Elle contient une fonction JavaScript simple pour gérer l'interaction du chat :

* Lorsque l'utilisateur tape un message et clique sur \"Envoyer\", elle :
    
    * Récupère le message du champ de saisie.
        
    * Crée une nouvelle bulle `user-message` et l'affiche.
        
    * Utilise l'API `fetch()` pour envoyer le message au point de terminaison `/api/chat` du backend.
        
    * Attend la réponse du backend.
        
    * Une fois la réponse reçue, elle crée une nouvelle bulle `agent-message` et affiche la réponse de l'IA.
        

## Comment tester l'agent IA

À ce stade, la structure de votre projet devrait ressembler à ceci :

```bash
study-planner/
├── backend/
│   ├── .env
│   ├── app.py
│   └── gemini_client.py
└── templates/
    └── index.html
```

Maintenant, naviguez vers le répertoire `backend` et exécutez :

```bash
cd backend
python app.py
```

Si tout est configuré, vous verrez l'application Flask démarrer sur [`http://127.0.0.1:5000`](http://127.0.0.1:5000) ou [`http://localhost:5000`](http://localhost:5000).

Ouvrez cette URL dans votre navigateur. Ça y est, vous avez enfin créé votre propre agent IA !

Essayez de poser des questions normales comme :

* \"Crée-moi un plan de 3 semaines pour apprendre la programmation Java pour débutants.\"
    
* \"Donne-moi un quiz sur le développement d'agents IA ?\"
    

Ou vous pouvez également déclencher une recherche web comme :

* `search: ressources pour java`
    
* `/search comment préparer les entretiens de codage frontend`
    

Lorsque vous utilisez le préfixe de recherche comme ci-dessus, l'agent récupère une poignée de liens et demande à **Gemini** de les synthétiser avec de courtes citations intégrées comme [1], [2]. C'est idéal pour des résumés de recherche rapides.

## Conclusion

Félicitations ! Vous disposez maintenant d'un agent de planification d'études fonctionnel qui se souvient de vos conversations et peut même effectuer des recherches en ligne.

À partir de là, vous pouvez encore améliorer cet agent en :

* Enregistrant les historiques des utilisateurs dans une base de données.
    
* Ajoutant l'authentification pour gérer plusieurs utilisateurs.
    
* Connectant des calendriers ou des gestionnaires de tâches, et bien plus encore.
    

Cette base constitue un point de départ solide pour construire des agents IA encore plus sophistiqués, adaptés à vos besoins spécifiques.

Si vous avez trouvé ce tutoriel utile et souhaitez discuter de développement d'IA ou de logiciels, n'hésitez pas à me contacter sur [X/Twitter](https://x.com/itsTarun24), [LinkedIn](https://www.linkedin.com/in/tarunsingh24), ou à consulter mon portfolio sur mon [Blog](http://tarunportfolio.vercel.app/blog). Je partage régulièrement des réflexions sur l'IA, le développement, la rédaction technique, etc., et j'aimerais beaucoup voir ce que vous construirez avec cette base.

Bon codage !