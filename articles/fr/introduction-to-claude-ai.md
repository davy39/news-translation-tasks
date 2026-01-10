---
title: Comment utiliser Claude AI – Introduction à Claude AI + Exemple de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-03-15T00:54:58.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-claude-ai
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/claude-2.png
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: '#chatbots'
  slug: chatbots
- name: 'LLM''s '
  slug: llms
seo_title: Comment utiliser Claude AI – Introduction à Claude AI + Exemple de code
seo_desc: 'By Firas Ahmed

  Claude is one of the leading Large Language Models (LLMs) in the market, developed
  by Anthropic — an AI startup that was co-founded by ex OpenAI employees. The company
  is known for its stringent set of AI ethics and is currently backed...'
---

Par Firas Ahmed

Claude est l'un des principaux modèles de langage de grande taille (LLM) sur le marché, développé par _Anthropic_ — une startup en IA cofondée par d'anciens employés d'OpenAI. L'entreprise est connue pour son ensemble strict d'éthique de l'IA et est actuellement soutenue par des géants technologiques tels que Google et Amazon.

Dans cet article, nous allons explorer Claude AI, le comparer à ChatGPT et fournir un exemple rapide de la façon de travailler avec lui via l'API.

## Qu'est-ce que Claude ?

Similaire aux chatbots d'IA tels que ChatGPT et Gemini, Claude est un chatbot alimenté par Claude 3 — le dernier modèle de langage de grande taille d'Anthropic. Il est capable de prendre des entrées utilisateur et de générer des sorties semblables à celles d'un humain. En plus des conversations, vous pouvez télécharger des images et des documents vers Claude et lui demander de les résumer ou de répondre à des questions sur des points spécifiques.

Ce qui distingue Claude des autres concurrents est l'affirmation d'Anthropic selon laquelle il est plus sûr et moins susceptible de produire des sorties nuisibles et offensantes grâce à l'"IA Constitutionnelle" — une approche unique de formation pionnière d'Anthropic visant à développer des systèmes d'IA qui adhèrent à un ensemble de principes éthiques.

Le premier modèle a été publié en mars 2023, suivi plus tard par des versions mises à jour avec des capacités améliorées, des techniques de formation plus avancées et un accent plus marqué sur la sécurité.

En mars 2024, Anthropic a lancé Claude 3, sa suite de modèles la plus avancée et à la pointe de la technologie : _Haiku_, _Sonnet_ et _Opus_. Chacun ayant ses propres capacités uniques, avec Opus étant le plus puissant.

Claude 3 offre le traitement d'images, des taux de hallucination plus faibles et une fenêtre de contexte significativement plus grande. Le chatbot Claude, actuellement alimenté par Claude 3, a démontré des performances supérieures à celles de ChatGPT dans des benchmarks standardisés.

En plus du chatbot, Claude est également disponible via une API où les développeurs peuvent construire des applications sur celle-ci.

## Capacités de Claude AI

Voici les domaines clés où Claude excelle :

* **Conversation** : Claude est hautement capable de s'engager dans des conversations naturelles, de comprendre le contexte de l'utilisateur et de fournir des réponses réfléchies.
* **Création de contenu** : Claude peut générer du contenu de haute qualité adapté aux exigences définies par l'utilisateur.
* **Traduction linguistique** : À l'ère actuelle, la communication globale est cruciale. Claude possède des capacités multilingues, permettant la traduction entre différentes langues en temps réel et la création de contenu multilingue.
* **Traitement visuel** : Claude peut analyser et transcrire des images, y compris des photographies et des notes manuscrites.
* **Génération de code** : La génération de code est devenue une fonctionnalité attrayante et un avantage concurrentiel clé avec chaque nouvelle sortie de modèle d'IA. Claude peut générer des extraits de code, comprendre différents langages de programmation, expliquer la fonctionnalité du code et aider au débogage.

## Claude vs ChatGPT

Comparons les différences entre ChatGPT et Claude :

### LLM

* Claude 3 est la dernière gamme de modèles publiée en mars 2024.
* GPT-4 est le modèle actuel depuis mars 2023.

### Performance

Au moment de la rédaction, Claude excelle en termes de précision factuelle et peut maintenir le contexte sur des conversations plus longues. Claude Opus est montré pour surpasser GPT-4 dans tous les benchmarks d'évaluation des systèmes d'IA, en particulier en termes de connaissance et de compréhension du langage.

### Fenêtre de contexte

La fenêtre de contexte représente le nombre maximum de tokens qu'un système d'IA peut traiter dans une seule entrée ou sortie. Une fenêtre de contexte plus grande signifie que le LLM peut gérer des textes plus longs et maintenir le contexte lors du traitement de ce texte.

* GPT-4 a **8 192 tokens**, tandis qu'une version plus récente (GPT-4-32k) a **32 768 tokens**.
* Les trois versions de Claude 3 ont une fenêtre de contexte de **200 000 tokens**, ce qui est significativement plus grand que GPT-4.

### Sécurité

**GPT-4** :

* Bien que la sécurité soit un aspect critique de ChatGPT et que des efforts aient été faits pour atténuer la désinformation, le chatbot tend à générer certaines sorties incorrectes.
* ChatGPT sauvegarde les conversations avec l'utilisateur pour améliorer et entraîner davantage le modèle.

**Claude 3** :

* Claude a été développé en gardant la sécurité à l'esprit. Anthropic met l'accent sur l'utilisation éthique de l'IA tant dans la formation que dans la manière dont le chatbot traite les entrées et génère les sorties. Le modèle suit strictement l'IA Constitutionnelle.
* Claude ne conserve pas les données des utilisateurs.

### Accessibilité

Les modèles Claude 3 et GPT-4 sont disponibles directement via les chatbots ainsi que via l'API. De plus, ils sont accessibles sur d'autres plateformes :

* **GPT-4** : Microsoft a fortement investi dans OpenAI pour intégrer leurs derniers LLM dans les plateformes Microsoft. À ce jour, GPT-4 est disponible via Microsoft's Copilot gratuitement.
* **Claude 3** : Anthropic s'est associé à des entreprises comme Notion, Amazon et DuckDuckGo pour intégrer Claude 3 dans leurs produits.

## Comment interagir avec Claude AI

Si vous êtes familier avec ChatGPT (ce qui est probablement le cas maintenant), vous devriez avoir une expérience similaire avec le chatbot Claude. Une fois que vous avez créé un compte [ici](https://claude.ai/chats), il sera aussi simple que de taper vos requêtes.

Dans cette section, nous allons nous concentrer sur l'interaction avec le modèle d'IA via l'API fournie en utilisant Python pour lui demander d'expliquer le concept des réseaux de neurones.

Pour commencer, inscrivez-vous [ici](https://console.anthropic.com/login), puis naviguez [ici](https://console.anthropic.com/settings/keys) pour créer votre première clé API. Assurez-vous de copier et de stocker la clé API dans un fichier sécurisé.

Voici un exemple de script Python qui demande à Claude d'expliquer le concept des réseaux de neurones :

```python
  # importer la bibliothèque anthropic
  import anthropic
  
  # créer une instance client
  client = anthropic.Anthropic(
      api_key="votre_cle_api",
  )

  # créer le prompt et appeler l'API
  message = client.messages.create(
      model="claude-3-opus-20240229",
      max_tokens=1000,
      temperature=0.0,
      system="Répondez en phrases courtes et claires.",
      messages=[
          {
            "role": "user",
            "content": "Pouvez-vous expliquer le concept des réseaux de neurones ?"
          }
      ]
  )

  print(message.content)
```

Assurez-vous de remplacer `votre_cle_api` par la clé API réelle que vous avez créée.

Discutons rapidement des paramètres définis ci-dessus :

* `model="claude-3-opus-20240229"` spécifie le modèle à utiliser.
* `max_tokens=1000` définit le nombre maximum de tokens que la réponse générée peut avoir.
* `temperature=0.0` contrôle le niveau d'aléatoire de la réponse générée. `0.0` signifie que la réponse sera plus cohérente et moins variée.
* `system="Fournir des réponses courtes et claires."` spécifie comment le système doit générer la réponse.
* `messages=[{"role": "user", "content": "Pouvez-vous expliquer le concept des réseaux de neurones ?"}]` définit le rôle et le message d'entrée en fonction desquels la sortie sera générée.

Voici un exemple de réponse en JSON :

```json
{
    "id": "msg_01H4xwvAZnb6XTz8cHPoerBS",
    "type": "message",
    "role": "assistant",
    "content": [
        {
            "type": "text",
            "text": "Les réseaux de neurones sont un type d'algorithme d'apprentissage automatique inspiré par la structure et la fonction du cerveau humain. Ils consistent en des nœuds interconnectés, ou \"neurones\", organisés en couches. Chaque neurone reçoit une entrée, la traite et transmet la sortie aux neurones de la couche suivante. Grâce à l'entraînement sur de grands ensembles de données, les réseaux de neurones apprennent à reconnaître des motifs et à faire des prédictions ou des décisions.\n\nPoints clés sur les réseaux de neurones :\n\n1. Structure : Couche d'entrée, couche(s) cachée(s) et couche de sortie de neurones\n2. Poids et biais : Chaque connexion a un poids qui détermine l'importance de l'entrée\n3. Fonctions d'activation : Déterminent la sortie d'un neurone en fonction de son entrée\n4. Entraînement : Les réseaux apprennent en ajustant les poids par rétropropagation et des algorithmes d'optimisation\n5. Applications : Utilisés pour des tâches comme la reconnaissance d'images, le traitement du langage naturel et la prédiction\n\nLes réseaux de neurones excellent dans l'apprentissage de relations complexes et non linéaires dans les données et ont révolutionné des domaines comme la vision par ordinateur et la reconnaissance vocale. Cependant, ils nécessitent de grandes quantités de données d'entraînement et de ressources computationnelles."
        }
    ],
    "model": "claude-3-opus-20240229",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "usage": {
        "input_tokens": 23,
        "output_tokens": 219
    }
}
```

## Conclusion

Claude représente un bond significatif dans le domaine de l'intelligence artificielle qui surpasse divers concurrents sur le marché.

Claude offre une vision unique, un ensemble de normes concernant la sécurité et la sûreté, et propose une gamme diversifiée d'applications, de la création de contenu à la génération de code.