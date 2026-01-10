---
title: Comment transformer des sites web en données prêtes pour les LLM avec Firecrawl
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-10-22T16:02:51.202Z'
originalURL: https://freecodecamp.org/news/how-to-turn-websites-into-llm-ready-data-using-firecrawl
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761148818578/a9572dc3-cc79-4ba9-ab47-4270e465df70.png
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
- name: APIs
  slug: apis
- name: llm
  slug: llm
seo_title: Comment transformer des sites web en données prêtes pour les LLM avec Firecrawl
seo_desc: 'If you’ve ever tried feeding web pages into an AI model, you know the pain.

  Websites come with ads, navigation bars, and messy HTML. Before your Large Language
  Model (LLM) can understand the content, you must clean and format it.

  That’s where Firecra...'
---

Si vous avez déjà essayé d'alimenter un modèle d'IA avec des pages web, vous connaissez la difficulté.

Les sites web contiennent des publicités, des barres de navigation et du code HTML désordonné. Avant que votre Modèle de langage étendu (LLM) puisse comprendre le contenu, vous devez le nettoyer et le formater.

C'est là que [Firecrawl](https://github.com/firecrawl/firecrawl) vous facilite la vie. Il s'agit d'un outil d'API open-source qui transforme n'importe quel site web en données propres et structurées, prêtes pour les LLM en quelques secondes.

Dans ce tutoriel, nous examinerons deux façons d'utiliser Firecrawl. L'une via l'API de Firecrawl (une API payante avec un niveau gratuit) et l'autre via une version auto-hébergée.

## Table des matières

* [Qu'est-ce que Firecrawl ?](#heading-quest-ce-que-firecrawl)
    
* [Pourquoi les LLM ont besoin de données propres](#heading-pourquoi-les-llm-ont-besoin-de-donnees-propres)
    
* [Configuration de Firecrawl](#heading-configuration-de-firecrawl)
    
* [Scraping d'une seule page](#heading-scraping-dune-seule-page)
    
* [Crawling d'un site web entier](#heading-crawling-dun-site-web-entier)
    
* [Extraction de données structurées avec l'IA](#heading-extraction-de-donnees-structurees-avec-lia)
    
* [Auto-hébergement de Firecrawl avec Sevalla](#heading-auto-hebergement-de-firecrawl-avec-sevalla)
    
* [Cas d'utilisation](#heading-cas-dutilisation)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que Firecrawl ?

[Firecrawl](https://www.firecrawl.dev/) est un service de crawling et de scraping web qui aide les développeurs à collecter des données propres à partir de sites web. Vous lui donnez une URL, et il renvoie le contenu dans des formats tels que Markdown, HTML, JSON ou même des captures d'écran.

![Illustration de Firecrawl - version open source et cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1760534000207/93e57884-c611-40cc-b7be-4fe7d3c1ac5c.png align="center")

Contrairement aux scrapers basiques, Firecrawl comprend les sites web complexes qui chargent du contenu avec JavaScript. Il peut crawler à travers les liens, suivre les pages et gérer les tâches lourdes comme les proxies et les systèmes anti-bots automatiquement.

En résumé, il s'occupe de la partie difficile de la collecte de données web, afin que vous puissiez vous concentrer sur l'utilisation de ces données pour vos projets d'IA ou d'automatisation.

## Pourquoi les LLM ont besoin de données propres

Les LLM apprennent et répondent en fonction du texte que vous leur donnez. Si ce texte inclut des éléments encombrants comme des balises HTML, des scripts ou des sections non pertinentes, l'IA s'embrouille.

Des données propres et bien structurées aident le modèle à rester concentré sur le contenu réel, comme le corps de l'article, les détails du produit ou la documentation.

Firecrawl simplifie ce processus. Au lieu de passer des heures à construire des scrapers ou à nettoyer du texte, vous pouvez obtenir du contenu prêt à l'emploi en un seul appel d'API.

## Configuration de Firecrawl

Pour commencer, créez un compte sur [firecrawl.dev](https://firecrawl.dev/) et récupérez votre clé API. L'exécution de Firecrawl sur votre machine implique la configuration d'un serveur, d'un cache Redis, etc. Nous utiliserons donc la clé API de firecrawl.dev pour tester l'API.

Nous pouvons également tester rapidement ses capacités dans l'interface utilisateur du site web.

Utilisons [https://freecodecamp.org](https://freecodecamp.org/) comme domaine pour voir si Firecrawl peut renvoyer des résultats.

![Crawling de freeCodeCamp](https://cdn.hashnode.com/res/hashnode/image/upload/v1760534104974/eb7ebdb4-d91f-4c49-92d9-b1c56c86ebb1.png align="center")

Et oui, nous pouvons voir plusieurs URL scrapées par Firecrawl.

![Résultats de Firecrawl](https://cdn.hashnode.com/res/hashnode/image/upload/v1760534508920/5f6423e6-aef2-4935-a821-0246fd96c12e.png align="center")

Maintenant, accédons à Firecrawl par le code. Le plan gratuit vous permet de scraper 500 pages, ce qui est suffisant pour comprendre son fonctionnement.

Vous pouvez utiliser soit le [Python SDK](https://docs.firecrawl.dev/sdks/python), le [Node.js SDK](https://docs.firecrawl.dev/sdks/node), ou des requêtes API directes avec curl.

Voici comment installer les SDK :

Python :

```plaintext
pip install firecrawl-py
```

Node.js :

```plaintext
npm install @mendable/firecrawl-js
```

Une fois installé, il vous suffit de configurer votre clé API et vous êtes prêt à crawler.

## Scraping d'une seule page

Supposons que vous souhaitiez extraire le contenu principal de la page d'accueil de Firecrawl. Vous pouvez le faire en quelques lignes seulement.

**Exemple Python :**

```python
from firecrawl import Firecrawl
```

```python
firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")
```

```python
doc = firecrawl.scrape(
    "https://firecrawl.dev",
    formats=["markdown", "html"]
)
```

```python
print(doc.markdown)
```

Ce script renvoie la version nettoyée de la page au format Markdown, parfait pour être lu ou analysé par un LLM.

Avec cette seule commande, vous obtenez le texte essentiel, débarrassé de l'encombrement HTML.

## Crawling d'un site web entier

Si vous avez besoin de données provenant de plusieurs pages, comme un site de documentation complet, vous pouvez crawler l'ensemble du domaine. Firecrawl trouve tous les liens et les scrape automatiquement.

Exemple d'appel API :

```plaintext
curl -X POST https://api.firecrawl.dev/v2/crawl \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://docs.firecrawl.dev",
    "limit": 10,
    "scrapeOptions": {
      "formats": ["markdown", "html"]
    }
  }'
```

Cela lance une tâche de crawl et renvoie un ID de tâche. Une fois terminé, vous pouvez télécharger toutes les pages scrapées dans des formats propres et prêts pour les LLM.

## Extraction de données structurées avec l'IA

L'une des meilleures fonctionnalités de Firecrawl est l'extraction alimentée par l'IA. Vous pouvez demander à Firecrawl de lire une page et de renvoyer des données structurées, comme le prix d'un produit, sa description ou des avis, au format JSON.

Exemple :

```plaintext
curl -X POST https://api.firecrawl.dev/v2/extract \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "urls": ["https://firecrawl.dev/*"],
    "prompt": "Extract the company mission and whether it is open source.",
    "schema": {
      "type": "object",
      "properties": {
        "company_mission": { "type": "string" },
        "is_open_source": { "type": "boolean" }
      }
    }
  }'
```

Firecrawl utilise un LLM intégré pour lire le contenu et remplir la structure automatiquement. Vous pouvez même ignorer le schéma et simplement fournir un prompt en langage naturel, tel que :

> *« Extrayez tous les détails de tarification et les noms des fonctionnalités de cette page. »*

C'est idéal pour les pipelines d'IA, les systèmes RAG (Génération augmentée par récupération) ou les tableaux de bord qui reposent sur des données propres et structurées.

## Auto-hébergement de Firecrawl avec Sevalla

Firecrawl est open source, ce qui signifie que vous n'avez pas à payer pour l'API si vous préférez un contrôle total. Vous pouvez le déployer sur votre propre serveur et le personnaliser comme bon vous semble.

Vous pouvez installer Firecrawl sur votre machine locale en configurant une base de données, un cache et d'autres composants requis. Mais cette configuration ne fonctionnera que pour des projets locaux et ne vous permettra pas de construire ou de déployer des applications utilisant Firecrawl.

Pour installer Firecrawl, vous pouvez choisir n'importe quel fournisseur cloud comme [AWS](https://aws.amazon.com/), [Heroku](https://www.heroku.com/) ou d'autres pour configurer ce projet. Mais j'utiliserai Sevalla.

[Sevalla](https://sevalla.com/) est un fournisseur moderne de Platform-as-a-service basé sur l'utilisation. Il propose l'hébergement d'applications, de bases de données, de stockage d'objets et l'hébergement de sites statiques pour vos projets.

J'utilise Sevalla pour l'hébergement pour deux raisons :

* Chaque plateforme vous facturera la création d'une ressource cloud. Sevalla offre un crédit de 50 $ à utiliser, nous n'aurons donc aucun coût pour cet exemple.
    
* Sevalla dispose d'un [template pour Firecrawl](https://docs.sevalla.com/templates/overview), ce qui simplifie l'installation manuelle et la configuration de chaque ressource dont vous aurez besoin pour Firecrawl.
    

Connectez-vous à Sevalla et cliquez sur Templates. Vous pouvez voir Firecrawl parmi les modèles.

![Templates Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1760534530797/6d327148-5c6f-40cc-863a-2ad9d82763bd.png align="center")

Cliquez sur « Deploy now », choisissez un serveur dans la fenêtre contextuelle et cliquez sur « Deploy ». Sevalla commencera à provisionner les ressources nécessaires au fonctionnement de notre instance Firecrawl.

![Ressources Firecrawl](https://cdn.hashnode.com/res/hashnode/image/upload/v1760534550817/38525217-89cb-41b3-8128-85164734b764.png align="center")

Une fois le déploiement terminé, vous verrez trois instances provisionnées :

* un [cache Redis](https://redis.io/)
    
* un serveur pour exécuter [Playwright](https://playwright.dev/)
    
* L'application API
    

Allez dans l'application Firecrawl-API. Dans la section des déploiements, cliquez sur « Visit app » une fois le déploiement terminé.

![Déploiement Firecrawl](https://cdn.hashnode.com/res/hashnode/image/upload/v1760534571061/3f4db002-c775-445f-a1fc-af1aefff2d86.png align="center")

Vous pouvez maintenant utiliser votre point de terminaison (endpoint) privé dans vos applications. Mon URL d'API est [https://firecrawl-api-56t8x.sevalla.app](https://firecrawl-api-56t8x.sevalla.app/) (il s'agit d'une URL temporaire – ne l'utilisez pas), je peux donc remplacer api.firecrawl.dev par cette URL.

```plaintext
curl -X POST https://firecrawl-api-56t8x.sevalla.app/v2/extract \
  -H 'Content-Type: application/json' \
  -d '{
    "urls": ["https://firecrawl.dev/*"],
    "prompt": "Extract the company mission and whether it is open source.",
    "schema": {
      "type": "object",
      "properties": {
        "company_mission": { "type": "string" },
        "is_open_source": { "type": "boolean" }
      }
    }
  }'
```

Si vous souhaitez exécuter le projet localement en installant des applications comme Redis, Postgresql et Playwright, [voici un guide détaillé](https://github.com/firecrawl/firecrawl/blob/main/CONTRIBUTING.md).

## Cas d'utilisation

Les développeurs et les data scientists utilisent Firecrawl pour un large éventail de tâches. Ils s'appuient souvent sur lui pour transformer des sites de documentation en données d'entraînement pour les modèles de langage étendus, garantissant ainsi que leurs modèles peuvent apprendre à partir de sources précises et bien organisées.

D'autres l'utilisent pour collecter des articles de blog ou des articles d'actualité pour l'[analyse de sentiment](https://www.turingtalks.ai/p/how-to-build-a-simple-sentiment-analyzer-using-hugging-face-transformer), les aidant à comprendre les tendances, les opinions ou les réactions du public sur le web.

Firecrawl est également précieux pour surveiller les changements de contenu web, ce qui est essentiel pour les projets de recherche ou le suivi de conformité où des informations à jour sont critiques.

Les équipes peuvent également l'utiliser pour créer des assistants IA de type « chattez avec votre site web » capables de répondre aux questions basées sur le contenu le plus récent du site.

Dans chacun de ces cas, Firecrawl garantit que votre modèle reçoit des données propres, structurées et cohérentes, ce qui facilite la création de systèmes d'IA fiables et intelligents.

## Conclusion

Transformer des sites web désordonnés en texte lisible était autrefois l'une des parties les plus difficiles de la création de systèmes d'IA. Firecrawl change la donne. Avec un seul appel d'API, vous pouvez scraper, crawler et extraire des données de haute qualité que votre LLM peut immédiatement comprendre.

Si vous construisez quoi que ce soit lié à l'IA, au RAG ou aux pipelines de données, Firecrawl est l'un de ces outils que vous regretterez de ne pas avoir découvert plus tôt.