---
title: Comment extraire des informations à partir de texte en utilisant la reconnaissance
  d'entités nommées (NER)
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-07-31T23:34:00.376Z'
originalURL: https://freecodecamp.org/news/extract-insights-from-text-using-named-entity-recognition
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747753280612/991828ce-0554-4c20-bfcc-bb278c9f2954.png
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
seo_title: Comment extraire des informations à partir de texte en utilisant la reconnaissance
  d'entités nommées (NER)
seo_desc: 'Many of us enjoy reading the news and staying up-to-date on current events.
  But the number of new stories each day can be overwhelming.

  You probably want to know who’s involved in world events, where things are happening
  globally, and which organizat...'
---

Beaucoup d'entre nous aiment lire les nouvelles et rester informés des événements actuels. Mais le nombre de nouveaux articles chaque jour peut être écrasant.

Vous voulez probablement savoir qui est impliqué dans les événements mondiaux, où les choses se passent à l'échelle mondiale et quelles organisations sont mentionnées. Mais lire intégralement chaque article prend beaucoup de temps – et vous êtes probablement occupé. C'est là que la reconnaissance d'entités nommées (NER) peut aider.

Dans cet article, je vais vous montrer comment construire un analyseur de nouvelles qui utilise un modèle NER basé sur des transformateurs pour extraire des données utiles à partir d'un flux RSS en direct.

Parcourons comment tout cela fonctionne.

## Table des matières

* [Qu'est-ce que la reconnaissance d'entités nommées ?](#heading-qu-est-ce-que-la-reconnaissance-d-entités-nommées)
  
* [Qu'est-ce que Hugging Face Transformers ?](#heading-qu-est-ce-que-hugging-face-transformers)
  
* [Comment construire l'analyseur de nouvelles](#heading-comment-construire-l-analyseur-de-nouvelles)
  
* [Précision dans la NER](#heading-précision-dans-la-ner)
  
* [Autres cas d'utilisation](#heading-autres-cas-d-utilisation)
  
* [Conclusion](#heading-conclusion)
  

## **Qu'est-ce que la reconnaissance d'entités nommées ?**

La reconnaissance d'entités nommées est un outil qui vous aide à repérer les termes importants dans un texte.

Elle étiquette les parties d'une phrase comme des types d'entités spécifiques – comme des noms, des lieux ou des dates. Voici à quoi cela ressemble en pratique. Prenons cette phrase :

> « **Le PDG d'Apple, Tim Cook, a tenu une réunion avec des dirigeants de Goldman Sachs à New York.** »

Un bon modèle NER identifiera :

* **« Tim Cook »** — une *personne*
  
* **« Apple »** — une *organisation*
  
* **« Goldman Sachs »** — une *organisation*
  
* **« New York »** — un *lieu*
  

Ce type d'extraction transforme du texte non structuré en données structurées. Cela facilite la recherche, le comptage et l'analyse de ce qui se passe dans les nouvelles.

## **Qu'est-ce que Hugging Face Transformers ?**

[**Hugging Face Transformers**](https://huggingface.co/docs/transformers/fr/index) est une bibliothèque Python qui vous donne accès à certains des modèles NLP les plus avancés.

Ces modèles sont entraînés sur des quantités massives de données. Au lieu de partir de zéro, vous pouvez utiliser des modèles qui comprennent déjà la grammaire, la structure des phrases et la reconnaissance d'entités.

La bibliothèque fournit une fonction simple `pipeline()` qui vous permet d'exécuter des tâches complexes comme la NER en quelques lignes de code. Vous pouvez trouver de nombreux modèles pré-entraînés sur [**huggingface.co/models**](http://huggingface.co/models).

Pour ce projet, nous utiliserons un modèle qui a été affiné pour la NER en anglais.

## **Comment construire l'analyseur de nouvelles**

Construisons l'analyseur de nouvelles. [**Voici un notebook Google Colab**](https://colab.research.google.com/drive/1Bd3mMGCv5izBwEyfI8VrOVtVtMRy-1yt?usp=sharing) si vous voulez essayer cela vous-même.

Vous aurez besoin de quelques packages Python. Ouvrez votre terminal ou invite de commande et exécutez :

```plaintext
pip install feedparser transformers
```

Ces bibliothèques vous permettront de récupérer des flux RSS et d'analyser du texte en utilisant des modèles de transformateurs pré-entraînés.

Nous utiliserons feedparser pour obtenir des articles de nouvelles. Voici comment vous pouvez récupérer et imprimer des résumés à partir du [**flux RSS de CNN**](http://rss.cnn.com/rss/money_topstories.rss) :

```plaintext
import feedparser
rss_url = "https://rss.cnn.com/rss/edition.rss"
feed = feedparser.parse(rss_url)

for entry in feed.entries[:5]:  # limiter aux 5 premiers articles
    print(f"Titre : {entry.title}")
    print(f"Résumé : {entry.summary}\n")
```

Ce code extrait le titre et le résumé des derniers articles.

![Articles RSS](https://cdn.hashnode.com/res/hashnode/image/upload/v1746721895350/6af303c4-a0f4-429b-b09c-07d3d989c8d8.png align="center")

Maintenant, chargeons un modèle de transformateur pour la NER.

Le modèle dslim/bert-base-NER fonctionne bien pour les textes d'actualité en anglais :

```plaintext
from transformers import pipeline

ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
```

L'argument `aggregation_strategy="simple"` indique au pipeline de fusionner les tokens consécutifs qui forment une seule entité nommée (comme « Tim Cook »).

Ce modèle classe chaque mot/token dans l'une des catégories d'entités : PER (personne), LOC (lieu), ORG (organisation), MISC (divers), ou O (hors de toute entité).

Laissez un peu de temps pour que le modèle se télécharge dans votre notebook Colab ou votre machine locale.

Relions le modèle NER à votre flux. Le script ci-dessous extrait le titre de chaque article et exécute la NER dessus.

Pour simplifier, nous sautons les résumés, mais si vous voulez les inclure, mettez à jour `ner_pipeline(title)` en `ner_pipeline(title+entry.summary)`.

```plaintext
for entry in feed.entries[:5]:
    title = entry.title
    print(f"\nAnalyse : {title}")
    entities = ner_pipeline(title)
    for ent in entities:
        print(f"{ent['word']} ({ent['entity_group']})")
```

Cela imprime les entités trouvées dans chaque résumé d'article, classées par type.

![Réponse NER](https://cdn.hashnode.com/res/hashnode/image/upload/v1746721942832/05a4dbf1-dcd6-4d99-a6dc-96dcca170b5c.png align="center")

Par exemple, le premier morceau de texte est :

> **Le Mexique prêt à riposter en nuisant aux agriculteurs américains**

La réponse est :

```plaintext
Mexique (LOC)
États-Unis (LOC)
```

Les deux sont des lieux. Si nous regardons les autres exemples, nous pouvons voir les classifications faites par le modèle NER comme :

```plaintext
iPhone (MISC)
America First (ORG)
India First (ORG)
Suisse (MISC)
Trump (PER)
```

Une fois que vous avez extrait les entités, vous pouvez :

* Compter la fréquence d'apparition des personnes ou des organisations.
  
* Suivre les tendances au fil du temps (par exemple, la fréquence d'apparition d'une personne particulière chaque semaine).
  
* Filtrer les articles mentionnant certains lieux ou entreprises.
  

## Précision dans la NER

Obtenir des données structurées à partir de la NER est puissant, mais ce n'est pas parfait. Les modèles peuvent manquer des entités, mal étiqueter des termes ou confondre des noms similaires.

Par exemple, « Amazon » pourrait être étiqueté comme un lieu dans une phrase et comme une organisation dans une autre, selon le contexte. Cela est normal car les modèles NER recherchent des motifs, ils ne « comprennent » pas vraiment le sens derrière le texte.

Pour tirer le meilleur parti de la NER, considérez-la comme un premier filtre plutôt que comme une réponse finale. Voici quelques façons pratiques de travailler avec ses résultats :

* **Recherchez des motifs :** Les erreurs occasionnelles n'auront pas autant d'importance lorsque vous analysez des tendances sur une période. Par exemple, suivre les entreprises qui apparaissent le plus souvent dans les titres vous donne des informations utiles même si quelques mentions sont mal classées.
  
* **Vérifiez avec des listes ou des bases de données connues :** Si vous surveillez des noms de sociétés ou de produits, comparez les résultats de la NER avec une liste de référence pour détecter les fautes de frappe ou les mauvaises classifications.
  
* **Combinez la NER avec d'autres techniques :** Associez-la à l'[analyse de sentiment](https://www.freecodecamp.org/news/what-is-sentiment-analysis-a-complete-guide-to-for-beginners/), à la correspondance de mots-clés ou aux comptages de fréquence pour rendre les données plus fiables et exploitables.
  
* **Vérifiez manuellement les résultats à enjeux élevés :** Si votre flux de travail implique des décisions ayant un impact juridique, financier ou réputationnel, échantillonnez et révisez la sortie de la NER pour confirmer son exactitude.
  

En traitant la NER comme un outil pour structurer et filtrer le texte plutôt que comme une source absolue de vérité, vous pouvez découvrir des tendances, construire des tableaux de bord et mettre en évidence des informations rapidement, tout en gardant les erreurs sous contrôle.

## Autres cas d'utilisation

La NER va bien au-delà de l'analyse des titres de nouvelles. C'est un outil fondamental pour extraire du sens à partir de grandes quantités de texte non structuré.

Les entreprises l'utilisent pour mettre automatiquement en évidence les détails critiques dans les interactions avec les clients. Par exemple, les équipes de support peuvent instantanément signaler les noms de clients, les produits, les numéros de série ou les lieux dans les tickets de support et les e-mails. Cela facilite la priorisation des demandes urgentes, l'acheminement des problèmes vers la bonne équipe et la détection des problèmes récurrents sans avoir à lire manuellement chaque message.

Les cabinets d'avocats et les chercheurs s'appuient fortement sur la NER pour traiter de grands volumes de documents. Les équipes juridiques peuvent extraire les noms de personnes, d'entreprises et de lieux à partir de contrats, de dépôts judiciaires et de mises à jour réglementaires pour construire des bases de données consultables ou cartographier les connexions entre les entités.

Les chercheurs académiques peuvent faire de même avec des articles scientifiques, accélérant les revues de littérature et découvrant des motifs à travers des milliers de publications.

Dans le domaine de la finance, la NER est un outil puissant pour l'intelligence de marché. Les analystes l'utilisent pour suivre les mentions d'entreprises, de codes boursiers, de devises et de matières premières à travers les nouvelles, les rapports de résultats et les briefings d'analystes. En agrégeant ces données, ils peuvent détecter des tendances, évaluer l'exposition aux risques ou repérer des événements majeurs du marché plus rapidement qu'une revue manuelle ne le pourrait.

Les équipes des médias sociaux et du marketing dépendent également de la NER. En identifiant automatiquement les marques, les concurrents ou les influenceurs dans les tweets et les publications, ils peuvent surveiller le sentiment de la marque, détecter les tendances émergentes et réagir rapidement aux risques de relations publiques.

En bref, partout où vous êtes submergé par du texte, qu'il s'agisse de retours clients, de contrats, de rapports de marché ou de flux sociaux, la NER peut transformer ce désordre non structuré en informations structurées et exploitables.

## **Conclusion**

Ce que nous avons construit ici est un petit mais puissant analyseur de nouvelles. En combinant une source de données en direct (flux RSS) avec un modèle NER pré-entraîné de Hugging Face Transformers, vous pouvez automatiquement extraire qui, quoi et où des articles de nouvelles.

Gardez à l'esprit que les modèles NER ne sont pas parfaits. Ils font des prédictions basées sur des motifs, pas sur la compréhension. C'est à vous de décider comment interpréter leurs résultats et gérer les inexactitudes.

Si vous aimez les jeux en ligne, consultez [GameBoost](https://gameboost.com/), le marché ultime pour les joueurs. Vous pouvez y trouver des objets de jeu qui vous aident à monter de niveau plus rapidement, comme [Grow a Garden](https://gameboost.com/grow-a-garden/items), Fortnite, Clash of Clans et bien d'autres.