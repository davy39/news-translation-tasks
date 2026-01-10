---
title: Guide du débutant sur les LLM – Qu'est-ce qu'un grand modèle de langage et
  comment fonctionne-t-il ?
date: '2024-08-15T19:41:19.413Z'
author: Bhavishya Pandit
authorURL: https://www.freecodecamp.org/news/author/bhav09/
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-large-language-models
translator: ''
reviewer: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1723750839199/0dc3a4ff-3e4e-4055-b3c1-955474946b0f.jpeg
tags:
- name: llm
  slug: llm
- name: Beginner Developers
  slug: beginners
- name: beginner
  slug: beginner
- name: Open Source
  slug: opensource
- name: Machine Learning
  slug: machine-learning
- name: Data Science
  slug: data-science
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
seo_desc: 'ChatGPT was released in November 2022. Since then, we’ve witnessed rapid
  advancements in the field of AI and technology.

  But did you know that the journey of AI chatbots began way back in 1966 with ELIZA?
  ELIZA was not as sophisticated as today’s mod...'
---


ChatGPT est sorti en novembre 2022. Depuis, nous avons été témoins d'avancées rapides dans le domaine de l'IA et de la technologie.

<!-- more -->

Mais saviez-vous que le voyage des chatbots d'IA a commencé dès 1966 avec ELIZA ? ELIZA n'était pas aussi sophistiquée que les modèles actuels comme GPT, mais elle a marqué le début du chemin passionnant qui nous a menés là où nous en sommes aujourd'hui.

Le langage est l'essence même de l'interaction humaine et, à l'ère du numérique, apprendre aux machines à comprendre et à générer du langage est devenu une pierre angulaire de l'intelligence artificielle.

Les modèles avec lesquels nous interagissons aujourd'hui — tels que GPT, Llama3, Gemini et Claude — sont connus sous le nom de Grands Modèles de Langage (LLM pour *Large Language Models*). On les appelle ainsi car ils sont entraînés sur de vastes jeux de données textuelles, ce qui leur permet d'accomplir un large éventail de tâches liées au langage.

Mais que sont exactement les LLM, et pourquoi suscitent-ils un tel engouement ?

Dans cet article, vous apprendrez ce que sont les LLM et les raisons de cet engouement.

## **Qu'est-ce que les LLM ?**

Les Grands Modèles de Langage sont des modèles d'IA entraînés sur d'immenses quantités de données textuelles pour comprendre, générer et manipuler le langage humain. Ils reposent sur des architectures de deep learning comme les transformers, qui leur permettent de traiter et de prédire du texte d'une manière qui imite la compréhension humaine.

En termes plus simples, un LLM est un programme informatique qui a été entraîné sur de nombreux exemples pour différencier une pomme d'un Boeing 787 – et pour être capable de décrire chacun d'eux.

Avant d'être prêts à l'emploi et de pouvoir répondre à vos questions, les LLM sont entraînés sur des jeux de données massifs. De manière réaliste, un programme ne peut rien conclure d'une seule phrase. Mais après avoir analysé, disons, des billions de phrases, il est capable de construire une logique pour compléter des phrases ou même générer les siennes.

### Comment entraîner un LLM

Voici comment se déroule le processus d'entraînement :

1.  **Collecte de données :** La première étape consiste à rassembler des millions (voire des milliards) de documents textuels provenant de sources diverses, notamment des livres, des sites web, des articles de recherche et des réseaux sociaux. Ce jeu de données étendu sert de base au processus d'apprentissage du modèle.
    
2.  **Apprentissage des patterns :** Le modèle analyse les données collectées pour identifier et apprendre des schémas (*patterns*) dans le texte. Ces schémas incluent les règles de grammaire, les associations de mots, les relations contextuelles et même un certain niveau de sens commun. En traitant ces données, le modèle commence à comprendre comment le langage fonctionne.
    
3.  **Fine-tuning :** Après l'entraînement initial, le modèle est affiné (processus de *fine-tuning*) pour des tâches spécifiques. Cela implique d'ajuster les paramètres du modèle pour optimiser ses performances pour des tâches telles que la traduction, le résumé automatique, l'analyse de sentiment ou la réponse aux questions.
    
4.  **Évaluation et tests :** Une fois entraîné, le modèle est rigoureusement testé par rapport à une série de benchmarks pour évaluer sa précision, son efficacité et sa fiabilité. Cette étape garantit que le modèle fonctionne bien dans des applications réelles.
    

Une fois le processus d'entraînement terminé, les modèles sont lourdement testés sur une série de benchmarks pour la précision, l'efficacité, la sécurité, etc.

## **Applications des LLM**

Les LLM ont un large éventail d'applications, de la génération de contenu à la prédiction, et bien plus encore.

![Applications des LLM dans différents domaines comme la santé, l'éducation, le support client, etc.](https://cdn.hashnode.com/res/hashnode/image/upload/v1723742816242/6e40d678-96ed-4f51-aa35-61c565548a32.png)

### **Création de contenu :**

-   **Assistance à la rédaction :** Des outils comme Grammarly utilisent des LLM pour fournir des suggestions en temps réel afin d'améliorer la grammaire, le style et la clarté de l'écriture. Que vous rédigiez un e-mail ou un roman, les LLM peuvent vous aider à polir votre texte.
    
-   **Narration automatisée :** Les modèles d'IA peuvent désormais générer du contenu créatif, des nouvelles aux romans complets. Ces modèles peuvent imiter le style d'auteurs célèbres ou même créer des styles littéraires entièrement nouveaux.
    

### **Service client :**

-   **Chatbots :** De nombreuses entreprises déploient des chatbots alimentés par l'IA capables de comprendre et de répondre aux demandes des clients en temps réel. Ces chatbots peuvent gérer un large éventail de tâches, de la réponse aux questions fréquemment posées au traitement des commandes.
    
-   **Assistants personnels :** Les assistants virtuels comme Siri et Alexa utilisent des LLM pour interpréter et répondre aux commandes vocales, fournissant aux utilisateurs des informations, des rappels et du divertissement à la demande.
    

### **Santé :**

-   **Résumé de dossiers médicaux :** Les LLM peuvent assister les professionnels de santé en résumant les dossiers des patients, facilitant ainsi l'examen des informations critiques et la prise de décisions éclairées.
    
-   **Aide au diagnostic :** Les modèles d'IA peuvent analyser les données des patients et la littérature médicale pour aider les médecins à diagnostiquer des maladies et à recommander des traitements.
    

### **Recherche et éducation :**

-   **Revue de littérature :** Les LLM peuvent passer au crible de vastes quantités d'articles de recherche pour fournir des résumés concis, identifier des tendances et suggérer de nouvelles directions de recherche.
    
-   **Outils éducatifs :** Les tuteurs alimentés par l'IA peuvent offrir des expériences d'apprentissage personnalisées en s'adaptant aux progrès et aux besoins de l'élève. Ces outils peuvent fournir un feedback instantané et des plans d'étude sur mesure.
    

### **Divertissement :**

-   **Développement de jeux vidéo :** Les LLM sont utilisés pour créer des personnages plus dynamiques et réactifs dans les jeux vidéo. Ces personnages pilotés par l'IA peuvent interagir avec les joueurs de manière plus réaliste et interactive.
    
-   **Génération de musique et d'art :** Les modèles d'IA sont désormais capables de composer de la musique, de générer des œuvres d'art et même d'écrire des scénarios de films, repoussant les limites de l'expression créative.
    

## **Défis liés aux LLM**

Bien que les LLM soient puissants, ils ne sont pas sans défis. ChatGPT compte plus de 150 millions d'utilisateurs mensuels, ce qui nous donne une idée de l'ampleur de l'impact de l'IA. Mais les nouvelles technologies posent aussi certains problèmes.

### **Biais et équité :**

-   Les LLM apprennent à partir des données sur lesquelles ils sont entraînés, lesquelles peuvent inclure des biais présents dans la société. Cela peut conduire à des résultats biaisés ou injustes dans leurs prédictions ou réponses. Résoudre ce problème nécessite une sélection minutieuse des jeux de données et des ajustements algorithmiques pour minimiser les biais.

### **Confidentialité des données :**

-   Les LLM peuvent involontairement apprendre et retenir des informations sensibles provenant des données d'entraînement, ce qui soulève des préoccupations en matière de confidentialité. Des recherches sont en cours sur la manière de rendre les LLM plus respectueux de la vie privée.

### **Consommation de ressources :**

-   L'entraînement des LLM nécessite une puissance de calcul immense et de grands jeux de données, ce qui peut être coûteux et peser sur l'environnement. Des efforts sont faits pour créer des modèles plus efficaces nécessitant moins d'énergie et de données.

### **Interprétabilité :**

-   Les LLM sont souvent perçus comme des "boîtes noires", ce qui signifie qu'il est difficile de comprendre exactement comment ils arrivent à certaines conclusions. Le développement de méthodes pour rendre l'IA plus interprétable et explicable est un domaine de recherche actif.

## **Coder avec les LLM : un exemple avec Replicate**

Pour ceux d'entre vous qui aiment mettre la main à la pâte avec du code, voici un exemple rapide de l'utilisation d'un LLM avec la bibliothèque Replicate.

**Replicate** est un package Python qui simplifie le processus d'exécution de modèles de machine learning dans le cloud. Il fournit une interface conviviale pour accéder et utiliser une vaste collection de modèles pré-entraînés depuis la plateforme Replicate.

Avec Replicate, vous pouvez facilement :

-   Exécuter des modèles directement depuis votre code Python ou vos notebooks Jupyter.
    
-   Accéder à divers types de modèles, y compris la génération d'images, la génération de texte, et plus encore.
    
-   Profiter d'une infrastructure cloud puissante pour une exécution efficace des modèles.
    
-   Intégrer des capacités d'IA dans vos applications sans la complexité de l'entraînement et du déploiement de modèles.
    

Voici un simple extrait de code pour générer du texte en utilisant le modèle llama3-70b-instruct de Meta. **Llama 3** est l'un des derniers modèles de langage open-source développés par Meta. Il est conçu pour être performant, polyvalent et accessible, permettant aux utilisateurs d'expérimenter, d'innover et de mettre à l'échelle leurs applications d'IA.

```
import os
import replicate # pip install replicate

# Get your token from -> https://replicate.com/account/api-tokens
os.environ["REPLICATE_API_TOKEN"] = "TOKEN"
api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

# Running llama3 model using replicate
output = api.run(
    "meta/meta-llama-3-70b-instruct",
        input={"prompt": 'Hey how are you?'}
    )

# Printing llama3's response
for item in output:
    print(item, end="")
```

Explication :

-   Nous enregistrons d'abord le token Replicate en utilisant le package `os` comme variable d'environnement.
    
-   Ensuite, nous utilisons le modèle Llama3 70b-instruct pour obtenir une réponse basée sur notre prompt. Vous pouvez personnaliser la sortie en modifiant le prompt.
    

Et qu'est-ce qu'un prompt ? **Un prompt est essentiellement une instruction textuelle ou une requête donnée à un modèle d'IA.** C'est comme fournir un point de départ ou une direction pour que l'IA génère du texte, traduise des langues, rédige différents types de contenu créatif et réponde à vos questions de manière informative.

Par exemple :

-   **"Écris un poème sur un robot explorant l'océan."**
    
-   **"Traduis 'Bonjour, comment vas-tu ?' en espagnol."**
    
-   **"Explique l'informatique quantique en termes simples."**
    

Ce sont tous des prompts qui guident l'IA pour produire une sortie spécifique.

En utilisant le modèle **llama-3-70b-instruct** de Meta, vous pouvez construire divers outils autour des applications mentionnées dans cet article. Ajustez les prompts en fonction de votre cas d'utilisation et vous serez prêt à vous lancer ! ⚡️

## **Conclusion**

Dans cet article, nous avons exploré le monde des Grands Modèles de Langage, en fournissant une compréhension de haut niveau de leur fonctionnement et de leur processus d'entraînement. Nous avons approfondi les concepts de base des LLM, notamment la collecte de données, l'apprentissage de patterns et le fine-tuning, et nous avons discuté des nombreuses applications des LLM dans divers secteurs.

Bien que les LLM offrent un potentiel immense, ils s'accompagnent également de défis tels que les biais, les préoccupations liées à la confidentialité, la demande en ressources et l'interprétabilité. Relever ces défis est crucial à mesure que l'IA continue d'évoluer et de s'intégrer plus profondément dans nos vies.

Nous avons également donné un aperçu de la manière dont vous pouvez commencer à travailler avec les LLM en utilisant la bibliothèque Replicate, montrant que même des modèles complexes comme Llama3 70b-instruct peuvent être accessibles aux développeurs disposant des bons outils.

---

![Bhavishya Pandit](https://cdn.hashnode.com/res/hashnode/image/upload/v1723527142033/f9488cce-0499-4dab-996f-d678eaae2d05.jpeg)

Lire [plus d'articles][1].

---

Si cet article vous a été utile, partagez-le.

Apprenez à coder gratuitement. Le curriculum open-source de freeCodeCamp a aidé plus de 40 000 personnes à obtenir un emploi de développeur. [Commencer][2]

[1]: /news/author/bhav09/
[2]: https://www.freecodecamp.org/learn/