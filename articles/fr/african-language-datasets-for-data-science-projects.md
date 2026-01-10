---
title: 10 Meilleurs Jeux de Données de Langues Africaines pour les Projets de Data
  Science
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-14T18:37:44.000Z'
originalURL: https://freecodecamp.org/news/african-language-datasets-for-data-science-projects
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/zVaxL0LohRUpfDQhznRQ9z3y5tj1-m6e31y3.jpeg
tags:
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
- name: nlp
  slug: nlp
seo_title: 10 Meilleurs Jeux de Données de Langues Africaines pour les Projets de
  Data Science
seo_desc: "By Davis David\nAfrica has over 2000 languages, but these languages are\
  \ not well-represented in the existing Natural Language Processing ecosystem. \n\
  One challenge is the lack of useful African language datasets that we can use to\
  \ solve different socia..."
---

Par Davis David

L'Afrique compte plus de **2000** langues, mais ces langues ne sont pas bien représentées dans l'écosystème existant de traitement automatique du langage naturel (NLP).

Un défi est le manque de jeux de données utiles en **langues africaines** que nous pouvons utiliser pour résoudre différents problèmes sociaux et économiques.

Dans cet article, j'ai compilé une liste de jeux de données en langues africaines provenant de différentes sources sur le web. Vous pouvez utiliser ces jeux de données dans diverses tâches de NLP telles que la classification de texte, la reconnaissance d'entités nommées, la traduction automatique, l'analyse de sentiment, la reconnaissance vocale et la modélisation de sujets.

J'ai rendu cette collection de jeux de données publique pour vous donner l'opportunité d'utiliser vos compétences et d'aider à résoudre différents défis.

## Jeux de Données de Classification de Texte

Les jeux de données de classification de texte sont catégorisés ou organisés en différents groupes en fonction de leur contenu.

Voici la liste des jeux de données en langues africaines pour la [classification de texte](https://hackernoon.com/14-open-datasets-for-text-classification-in-machine-learning-xd1u3wit?ref=hackernoon.com).

### [Jeu de Données de Nouvelles en Swahili](https://zenodo.org/record/4300294?ref=hackernoon.com#.YKvsdqiA59A)

Le jeu de données de nouvelles en swahili contient plus de **31 000 articles de nouvelles** provenant de différentes catégories de nouvelles telles que locales, internationales, économiques ou financières, santé, sports et divertissement. Le swahili est l'une des langues les plus parlées en Afrique, avec environ 100 à 150 millions de locuteurs en Afrique de l'Est.

J'ai collecté les données à partir de différentes plateformes de publication de nouvelles en Tanzanie et à l'étranger. Vous pouvez utiliser ce jeu de données pour développer un modèle de classification multiclasse afin de classer le contenu des nouvelles selon des catégories spécifiques.

Les plateformes de nouvelles en ligne en swahili peuvent utiliser le modèle pour regrouper automatiquement les nouvelles selon leurs catégories et aider les lecteurs à trouver les nouvelles spécifiques qu'ils souhaitent lire.

Vous pouvez également télécharger ce jeu de données à partir de la [bibliothèque Python datasets](https://pypi.org/project/datasets/?ref=hackernoon.com) :

```python
from datasets import load_dataset

dataset = load_dataset("swahili_news")
```

**Note :** Le jeu de données de nouvelles en swahili présente un déséquilibre dans la distribution des catégories. Il contient peu d'articles de nouvelles dans les catégories suivantes :

* Nouvelles internationales (6,2 %)
* Nouvelles sur la santé (4,9 %)
* Nouvelles économiques (4,3 %)

### [Jeu de Données de Nouvelles en Chichewa](https://zenodo.org/record/4315018?ref=hackernoon.com#.YKvs16iA59A)

Ce jeu de données se compose d'**articles de nouvelles** en chichewa. Le chichewa est une langue bantu parlée dans une grande partie de l'Afrique du Sud, du Sud-Est et de l'Est, notamment au Malawi et en Zambie, où c'est une langue officielle.

Le jeu de données contient une collection de **3 482 articles**, contenant plus de **930 000 mots** et plus de **48 000 phrases**. Les articles de nouvelles en chichewa ont été catégorisés en **19 catégories** telles que l'éducation, la loi/l'ordre, la politique, la culture, les arts et l'artisanat, l'agriculture, l'économie et la faune.

Vous pouvez également télécharger ce jeu de données ici : [AI4D Malawi News Classification Zindi Challenge](https://zindi.africa/competitions/ai4d-malawi-news-classification-challenge?ref=hackernoon.com).

## Jeux de Données de Reconnaissance d'Entités Nommées

Vous utilisez les jeux de données de reconnaissance d'entités nommées pour extraire des informations en localisant et en classant les entités nommées mentionnées dans du texte non structuré. Des exemples d'entités sont les noms de personnes, les organisations, les lieux, les heures et les dates.

La reconnaissance d'entités nommées est un composant essentiel de nombreuses applications, y compris les correcteurs orthographiques, les agents conversationnels et la localisation des systèmes vocaux et de dialogue.

Voici la liste des jeux de données en langues africaines pour la reconnaissance d'entités nommées.

### [Jeux de Données Masakhane-ner](https://github.com/masakhane-io/masakhane-ner?ref=hackernoon.com)

Masakhane est une communauté NLP de base pour l'Afrique, par des Africains, avec pour mission de renforcer et de stimuler la recherche en NLP dans les langues africaines. La communauté a créé le premier grand jeu de données de haute qualité disponible publiquement pour la reconnaissance d'entités nommées (NER) dans dix langues africaines.

* Amharique
* Haoussa
* Igbo
* Kinyarwanda
* Luganda
* Luo
* Pidgin du Nigeria
* Swahili
* Wolof
* Yoruba

![Image](https://www.freecodecamp.org/news/content/images/2021/06/zVaxL0LohRUpfDQhznRQ9z3y5tj1-4l2z31l1.jpeg)
_[Source de l'image](https://arxiv.org/abs/2103.11811?ref=hackernoon.com)_

Vous pouvez lire l'article de recherche ici : [MasakhaNER: Named Entity Recognition for African Languages](https://arxiv.org/abs/2103.11811?ref=hackernoon.com), et vous pouvez télécharger les dix jeux de données NER [ici](https://github.com/masakhane-io/masakhane-ner/tree/main/data?ref=hackernoon.com).

## Jeux de Données de Traduction Automatique

La traduction automatique (MT) est la tâche de traduire un texte ou un discours dans une langue source vers une langue cible différente. Vous pouvez utiliser la traduction automatique pour traduire de grands volumes de texte rapidement sans aucune intervention humaine.

Vous pouvez utiliser les jeux de données de traduction automatique pour créer des modèles de MT pour différents objectifs tels que :

* Les e-mails internes et autres communications écrites ou orales.
* La documentation et les instructions pour les produits ou services.

Voici la liste des jeux de données en langues africaines pour la traduction automatique.

### [Jeu de Données de Traduction Automatique du Français vers l'Éwé et du Français vers le Fon](https://zindi.africa/competitions/ai4d-takwimu-lab-machine-translation-challenge?ref=hackernoon.com)

Il s'agit d'un corpus parallèle pour la traduction automatique du **français vers l'éwé** et du **français vers le fon**.

Le fon et l'éwé sont des langues nigéro-congolaises. Le fon est parlé au Bénin avec environ 4,1 millions de locuteurs, tandis que l'éwé est parlé au Togo et dans le sud-est du Ghana avec environ 4,5 millions de locuteurs.

Ce jeu de données contient environ **23 000** phrases parallèles français-éwé et **53 000** phrases parallèles français-fon, collectées à partir de blogs, de contes, de journaux, de conversations quotidiennes et de pages web, et il a été annoté pour la traduction automatique neuronale.

### [Jeu de Données de Traduction Automatique du Yoruba vers l'Anglais](https://zindi.africa/competitions/ai4d-yoruba-machine-translation-challenge?ref=hackernoon.com)

Il s'agit d'un corpus de phrases parallèles pour la traduction automatique de la langue yoruba vers la langue anglaise.

Le yoruba est une langue nigéro-congolaise et elle est parlée en Afrique de l'Ouest (sud-ouest du Nigeria). Le nombre de locuteurs yoruba est estimé entre 45 et 55 millions.

Le jeu de données se compose de **10 054** phrases parallèles yoruba-anglais provenant de différents domaines comme les nouvelles, les proverbes yoruba, les transcriptions de films, les traductions de localisation et les livres.

### [Jeu de Données de Traduction Automatique de l'Anglais vers le Luganda](https://zenodo.org/record/4764039?ref=hackernoon.com#.YKzBkKiA59A)

Il s'agit d'un corpus de phrases parallèles pour la traduction automatique de la langue anglaise vers la langue luganda.

Le luganda est une langue bantu et c'est l'une des principales langues en Ouganda. Plus de 8,5 millions de Baganda la parlent ainsi que de nombreuses autres personnes à Kampala (la capitale de l'Ouganda).

Le jeu de données se compose de **15 022** phrases parallèles anglais-luganda. Une équipe de chercheurs du laboratoire de recherche en IA et en science des données de l'Université Makerere l'a créé avec une équipe d'enseignants, d'étudiants et de pigistes luganda.

## Jeux de Données d'Analyse de Sentiment

Les jeux de données d'analyse de sentiment sont utilisés pour l'interprétation et la classification des émotions (_positives, négatives et neutres_) dans les données textuelles en utilisant différentes méthodes d'analyse de texte.

L'analyse de sentiment a des applications dans divers domaines tels que la surveillance des médias sociaux, la surveillance de marque, le service client et la recherche marketing.

Voici la liste des jeux de données en langues africaines pour l'analyse de sentiment.

### [Jeu de Données Tunizi](https://zenodo.org/record/4275240?ref=hackernoon.com)

Tunizi est le premier jeu de données d'analyse de sentiment en arabizi tunisien. L'arabizi tunisien représente le dialecte tunisien qui est écrit en caractères latins et en chiffres plutôt qu'en lettres arabes.

[iCompass](https://www.icompass.tn/?ref=hackernoon.com) a recueilli des commentaires sur les plateformes de médias sociaux qui expriment des sentiments sur des sujets populaires. Ils ont extrait **100k commentaires** en utilisant des API de streaming publiques.

Les commentaires collectés ont été annotés manuellement en utilisant une polarité globale :

* Positif (1)
* Négatif (-1)
* Neutre (0)

Les annotateurs étaient diversifiés en genre, en âge et en milieu social.

Vous pouvez également télécharger ce jeu de données à partir de la [bibliothèque Python datasets](https://pypi.org/project/datasets/?ref=hackernoon.com) :

```python
from datasets import load_dataset

dataset = load_dataset("tunizi")
```

## Jeux de Données de Reconnaissance Vocale

La reconnaissance vocale, également connue sous le nom de reconnaissance automatique de la parole (ASR), est une technologie qui analyse la parole humaine et formule une sortie, souvent une transcription écrite, en temps réel. Cela est parfois appelé « parole en texte ».

Ne confondez pas cela avec la reconnaissance vocale, car la reconnaissance vocale cherche simplement à identifier la voix d'un utilisateur individuel.

Voici la liste des jeux de données en langues africaines pour la reconnaissance vocale.

### [Jeu de Données de Reconnaissance Vocale en Wolof](https://zindi.africa/competitions/ai4d-baamtu-datamation-automatic-speech-recognition-in-wolof/data?ref=hackernoon.com)

Le wolof est la langue du Sénégal, de la Gambie et de la Mauritanie. Il est parlé par plus de 10 millions de personnes et environ 40 pour cent (environ 5 millions de personnes) de la population du Sénégal parlent le wolof comme langue maternelle.

Le jeu de données ASR compte un total de **6 683** fichiers audio et transcriptions et il a été créé par une équipe de chercheurs de la société Baamtu Datamation au Sénégal.

### [Jeu de Données de Reconnaissance Vocale en Kinyarwanda](https://commonvoice.mozilla.org/rw/datasets?ref=hackernoon.com)

Le kinyarwanda est une langue bantu et une langue officielle du Rwanda. Au moins 12 millions de personnes la parlent au Rwanda, dans l'est de la République démocratique du Congo et dans le sud de l'Ouganda.

Le [jeu de données](https://commonvoice.mozilla.org/rw/speak?ref=hackernoon.com) a été créé par **895 locuteurs** de différents genres et âges sur une plateforme de voix commune. Le jeu de données compte un total de **1 183 heures** de parole validée. Le jeu de données actuel fait **40 Go**.

## Jeux de Données de Modélisation de Sujets

La modélisation de sujets utilise des techniques d'apprentissage non supervisé pour extraire le sujet principal ou l'ensemble des sujets qui apparaissent dans une collection de documents textuels.

Voici un jeu de données en langue africaine pour la modélisation de sujets.

### [Jeu de Données de Nouvelles Sud-Africaines](https://zenodo.org/record/3668495?ref=hackernoon.com)

Il s'agit du jeu de données de nouvelles d'Afrique du Sud. Les données de nouvelles ont été collectées à partir des pages Facebook de SABC4. La [SABC](https://www.sabc.co.za/sabc/?ref=hackernoon.com) est le diffuseur public en Afrique du Sud.

Le jeu de données contient des titres de nouvelles (c'est-à-dire du texte court) dans les langues **setswana** et **sepedi**. Le setswana est une langue bantu parlée en Afrique australe par environ 8,2 millions de personnes, tandis que le sepedi est principalement parlé dans les parties nord de l'Afrique du Sud par 4,7 millions de personnes.

Puisque le jeu de données n'est pas annoté, vous pouvez l'utiliser pour créer un modèle de sujet afin de regrouper les données de nouvelles en différents sujets de nouvelles tels que le sport, la politique, la culture et le divertissement.

## Réflexions Finales sur les Jeux de Données de Langues Africaines

J'espère que vous avez trouvé cette liste de différents jeux de données de langues africaines utile et que vous pouvez les utiliser dans vos prochains [projets de data science](https://hackernoon.com/top-datasets-on-climate-change-for-data-science-projects-rzz34p0?ref=hackernoon.com). Je suis impatient de voir quelles applications/solutions vous créerez à partir de ces jeux de données.

Si vous n'avez pas trouvé le jeu de données dont vous avez besoin, veuillez consulter les liens suivants :

* [Zenodo: Traitement Automatique du Langage Naturel Africain (AfricaNLP)](https://zenodo.org/communities/africanlp/search?page=1&size=20&ref=hackernoon.com)
* [Github: Masakhane](https://github.com/masakhane-io/?ref=hackernoon.com)

**Félicitations** 👏👏, vous êtes arrivé à la fin de cet article ! J'espère que vous avez appris quelque chose de nouveau qui vous aidera dans votre prochain projet de data science.

Si vous avez appris quelque chose de nouveau ou si vous avez apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine publication !

Vous pouvez également me trouver sur Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid?ref=hackernoon.com).

Vous pouvez lire [d'autres articles](https://hackernoon.com/u/davisdavid) ici.