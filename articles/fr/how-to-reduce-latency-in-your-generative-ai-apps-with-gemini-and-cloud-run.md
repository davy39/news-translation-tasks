---
title: Comment réduire la latence de vos applications d'IA générative avec Gemini
  et Cloud Run
author: Amina Lawal
date: '2025-12-10T14:35:12.162Z'
originalURL: https://freecodecamp.org/news/how-to-reduce-latency-in-your-generative-ai-apps-with-gemini-and-cloud-run
description: Vous avez créé votre première fonctionnalité d'IA générative. Et maintenant
  ? Lors du déploiement de l'IA, le défi n'est plus de savoir si le modèle peut répondre,
  mais à quelle vitesse il peut le faire pour un utilisateur situé à l'autre bout
  du monde. Une faible latence n'est pas un luxe, c'est une nécessité pour une bonne
  expérience utilisateur...
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1765370930321/e4256d2f-cab3-4ae3-9486-c6651e363366.png
tags:
- name: optimization
  slug: optimization
- name: AI
  slug: ai
- name: Load Balancing
  slug: load-balancing
seo_desc: You've built your first Generative AI feature. Now what? When deploying
  AI, the challenge is no longer if the model can answer, but how fast it can answer
  for a user halfway across the globe. Low latency is not a luxury, it's a requirement
  for good u...
---


Vous avez créé votre première fonctionnalité d'IA générative. Et maintenant ? Lors du déploiement de l'IA, le défi n'est plus de savoir *si* le modèle peut répondre, mais *à quelle vitesse* il peut répondre pour un utilisateur situé à l'autre bout du monde. Une faible latence n'est pas un luxe, c'est une exigence pour une bonne expérience utilisateur.

Aujourd'hui, nous avons dépassé les simples déploiements de conteneurs pour construire des **Architectures d'IA mondiales**. Cette configuration exploite l'infrastructure de Google pour fournir des réponses d'IA générative instantanées et sensibles au contexte, partout dans le monde. Si vous êtes prêt à mettre la main à la pâte, construisons ensemble l'avenir des fonctionnalités intelligentes mondiales.

Dans cet article, vous ne allez pas seulement déployer un conteneur, vous allez construire une architecture d'IA mondiale.

Une architecture d'IA mondiale est un modèle de conception qui s'appuie sur un réseau mondial pour déployer et gérer des services d'IA, garantissant le temps de réponse le plus rapide possible (faible latence) pour les utilisateurs, quel que soit leur emplacement. Au lieu de déployer une fonctionnalité dans une seule région, cette architecture distribue le service sur plusieurs continents.

La plupart des gens déploient un service dans une seule région. C'est acceptable pour un utilisateur local, mais la distance physique et la vitesse de la lumière créent une latence terrible pour tous les autres. Nous allons éliminer ce problème en utilisant le réseau mondial de Google pour déployer le service dans un « triangle » de localisations.

Le service d'IA générative que vous allez construire est un « Guide Local ». Cette application sera conçue pour être profondément **hyper-personnalisée**, changeant sa personnalité et fournissant des recommandations basées sur le contexte géographique détecté de l'utilisateur. Par exemple, si un utilisateur est à Paris, le guide l'accueillera chaleureusement en mentionnant sa ville et en suggérant une activité locale.

Vous allez construire ce service pour atteindre trois objectifs critiques :

*   **Présent presque partout :** Déployé sur trois continents simultanément (États-Unis, Europe et Asie).
    
*   **Sensation d'instantanéité :** Utilise le réseau de fibre optique mondial de Google et l'IP Anycast pour router les utilisateurs vers le serveur le plus proche, garantissant la latence la plus faible possible.
    
*   **Sait où vous vous trouvez :** Détecte automatiquement l'emplacement de l'utilisateur (sans dépendre des autorisations GPS côté client) pour fournir des suggestions personnalisées et sensibles à la localisation.
    

## Table des matières

*   [Prérequis](#heading-prerequis)
    
*   [Phase 1 : Le code « sensible à la localisation »](#heading-phase-1-le-code-sensible-a-la-localisation)
    
*   [Phase 2 : Build & Push](#heading-phase-2-build-amp-push)
    
*   [Phase 3 : Le déploiement en « triangle »](#heading-phase-3-le-deploiement-en-triangle)
    
*   [Phase 4 : Le réseau mondial (le liant)](#heading-phase-4-le-reseau-mondial-le-liant)
    
*   [Phase 5 : Tests (l'heure de la téléportation)](#heading-phase-5-tests-l-heure-de-la-teleportation)
    
*   [Conclusion : L'Edge AI mondial](#heading-conclusion-l-edge-ai-mondial)
    

## **Prérequis**

Pour suivre ce tutoriel, vous avez besoin de :

1.  **Un projet Google Cloud** (avec la facturation activée).
    
2.  **Google Cloud Shell** (Recommandé ! Aucune installation locale requise). Cliquez sur l'icône en haut à droite de la console GCP qui ressemble à une invite de terminal `>_`.
    

**Note** : Le projet utilise divers services Google Cloud (Cloud Run, Artifact Registry, Load Balancer, Vertex AI), qui nécessitent tous un projet Google Cloud avec facturation activée pour fonctionner. Bien que beaucoup de ces services offrent un niveau gratuit, vous devez lier un compte de facturation à votre projet. Bien qu'un compte de facturation soit requis, les nouveaux utilisateurs de Google Cloud peuvent être éligibles à un [**crédit d'essai gratuit**](https://console.cloud.google.com/freetrial?hl=fr) qui devrait couvrir le coût de ce lab. [Voir l'éligibilité et la couverture du programme de crédit](https://cloud.google.com/free/docs/free-cloud-features#free-trial)

## **Phase 1 : Le code « sensible à la localisation »**

Nous ne voulons pas construire un chatbot générique, nous allons donc créer un « Guide Local » qui change sa personnalité en fonction de l'origine de la requête.

### **Activer les API**

Pour activer les services, exécutez ceci dans votre terminal :

```bash
gcloud services enable \
  run.googleapis.com \
  artifactregistry.googleapis.com \
  compute.googleapis.com \
  aiplatform.googleapis.com \
  cloudbuild.googleapis.com
```

Cette commande active les API Google Cloud nécessaires pour le projet :

*   Cloud Run ([run.googleapis.com](http://run.googleapis.com))
    
*   Artifact Registry ([artifactregistry.googleapis.com](http://artifactregistry.googleapis.com))
    
*   Compute Engine ([compute.googleapis.com](http://compute.googleapis.com))
    
*   Vertex AI ([aiplatform.googleapis.com](http://aiplatform.googleapis.com))
    
*   Cloud Build ([cloudbuild.googleapis.com](http://cloudbuild.googleapis.com)).
    

Leur activation garantit que les services dont nous avons besoin sont prêts à être utilisés.

![Capture d'écran montrant l'activation réussie des API Google Cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1764156603095/fb2ffd56-12e4-4b9f-ac2d-8fbb30fc0a2d.png align="center")

### Créer et remplir [`main.py`](http://main.py)

C'est le cerveau de notre service. Dans votre terminal Cloud Shell, créez un fichier nommé [`main.py`](http://main.py) et collez-y le code suivant :

```python
import os
import logging
from flask import Flask, request, jsonify
import vertexai
from vertexai.generative_models import GenerativeModel

app = Flask(__name__)

# Initialize Vertex AI
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
vertexai.init(project=PROJECT_ID)

@app.route("/", methods=["GET", "POST"])
def generate():
    # 1. Identify where the code is physically running (We set this ENV var later)
    service_region = os.environ.get("SERVICE_REGION", "unknown-region")
    
    # 2. Identify where the user is (Header comes from Global Load Balancer)
    # Format typically: "City,State,Country"
    user_location = request.headers.get("X-Client-Geo-Location", "Unknown Location")
    
    model = GenerativeModel("gemini-2.5-flash")
    
    # 3. Construct a location-aware prompt
    prompt = (
        f"You are a helpful local guide. The user is currently in {user_location}. "
        "Greet them warmly mentioning their city, and suggest one "
        "hidden gem activity to do nearby right now. Keep it under 50 words."
    )

    try:
        response = model.generate_content(prompt)
        return jsonify({
            "ai_response": response.text,
            "meta": {
                "served_from_region": service_region,
                "user_detected_location": user_location
            }
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
```

Il s'agit d'une application web Flask simple qui repose entièrement sur un en-tête HTTP spécifique (`X-Client-Geo-Location`) que le Load Balancer mondial injectera plus tard dans le processus. Ce choix de conception permet de garder le code Python propre, rapide et concentré sur l'utilisation du contexte fourni par la puissante infrastructure Google Cloud. Le script utilise Vertex AI et le modèle génératif haute performance Gemini 2.5 Flash.

Cette logique centrale de l'application est un service web Flask simple. Il effectue les opérations suivantes :

*   **Initialisation :** Configure l'application Flask, la journalisation et initialise le client Vertex AI à l'aide de l'ID du projet.
    
*   **Contexte :** Il extrait deux informations critiques : la `SERVICE_REGION` (où le code s'exécute physiquement) à partir de la variable d'environnement, et `X-Client-Geo-Location` (la localisation détectée de l'utilisateur) à partir de l'en-tête de la requête, qui sera injecté par le Load Balancer mondial.
    
*   **Génération par l'IA :** Il utilise le modèle haute performance `gemini-2.5-flash`.
    
*   **Construction du Prompt :** Un prompt dynamique et sensible à la localisation est construit en utilisant la ville détectée pour demander à Gemini d'agir comme un guide local utile et de fournir une suggestion personnalisée.
    
*   **Réponse :** La réponse inclut le texte généré par l'IA et une section `meta` contenant à la fois la région de service et la localisation détectée de l'utilisateur, ce qui facilite la vérification.
    

### **Créer le** `Dockerfile`

Ce Dockerfile indique à Cloud Run comment transformer l'application Python en une image de conteneur. Créez un fichier nommé `Dockerfile` dans le même répertoire que `main.py` et collez-y le contenu suivant :

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY main.py .

# Install Flask and Vertex AI SDK
RUN pip install flask google-cloud-aiplatform

CMD ["python", "main.py"]
```

Voici ce que fait le code :

*   Commence par une image de base Python légère `python:3.9