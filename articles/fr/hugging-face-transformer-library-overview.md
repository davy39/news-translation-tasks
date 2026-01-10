---
title: Comment utiliser la bibliothèque Transformer de Hugging Face
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-01-31T00:36:42.000Z'
originalURL: https://freecodecamp.org/news/hugging-face-transformer-library-overview
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/hugging-face.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
seo_title: Comment utiliser la bibliothèque Transformer de Hugging Face
seo_desc: 'In this article, I''ll talk about why I think the Hugging Face’s Transformer
  Library is a game-changer in NLP for developers and researchers alike.

  Have you ever wondered how modern AI achieves such remarkable feats, like understanding
  human language ...'
---

Dans cet article, je vais parler de pourquoi je pense que la bibliothèque Transformer de Hugging Face est un changement de jeu dans le NLP pour les développeurs et les chercheurs.

Vous êtes-vous déjà demandé comment l'IA moderne réalise des exploits remarquables, comme comprendre le langage humain ou générer du texte qui semble écrit par une personne ?

Une partie significative de cette magie provient d'un modèle révolutionnaire appelé [le Transformer](https://blogs.nvidia.com/blog/what-is-a-transformer-model/). De nombreux frameworks publiés dans le domaine du traitement du langage naturel (NLP) sont basés sur le modèle Transformer, et l'un des plus importants est la [bibliothèque Transformer de Hugging Face](https://huggingface.co/docs/transformers/index).

Dans cet article, je vais vous expliquer pourquoi cette bibliothèque n'est pas seulement un autre logiciel, mais un outil puissant pour les ingénieurs et les chercheurs. Ensuite, vous verrez un exemple pratique de son utilisation.

## Qu'est-ce que la bibliothèque Transformer de Hugging Face ?

La bibliothèque Transformer de Hugging Face est une bibliothèque open-source qui fournit une vaste gamme de modèles pré-entraînés principalement axés sur le NLP. Elle est construite sur PyTorch et TensorFlow, ce qui la rend incroyablement polyvalente et puissante.

L'une des premières raisons pour lesquelles la bibliothèque Hugging Face se distingue est sa remarquable convivialité. Même si vous n'êtes pas un expert en apprentissage profond, vous pouvez utiliser cette bibliothèque avec une relative facilité.

Elle offre des interfaces simples qui vous permettent d'implémenter des modèles complexes avec seulement quelques lignes de code. Cette simplicité ouvre les portes de l'IA avancée à un plus large éventail de développeurs et de chercheurs.

## Prêts à l'emploi et prêts à être utilisés

La beauté des modèles d'apprentissage profond d'aujourd'hui est que vous n'avez pas à entraîner un modèle à partir de zéro. La plupart des modèles sont pré-entraînés et votre travail en tant qu'ingénieur IA consistera à entraîner un modèle en utilisant des données personnalisées.

Imaginez donc avoir accès à une boîte à outils où chaque outil est conçu pour un travail spécifique. C'est ce que Hugging Face offre avec sa large gamme de modèles pré-entraînés.

Que vous travailliez sur la classification de texte, la réponse aux questions ou la génération de langage, il y a un modèle prêt à être utilisé. Cela permet d'économiser une énorme quantité de temps et de ressources, car vous n'avez pas à commencer à partir de zéro.

Bien que les modèles pré-entraînés soient fantastiques, ils ne conviennent peut-être pas à tous les besoins spécifiques. C'est là que Hugging Face brille vraiment. La bibliothèque vous permet d'affiner les modèles sur votre ensemble de données, ce qui rend possible la personnalisation des modèles selon vos exigences spécifiques.

## Soutien de la communauté

Ce qui distingue Hugging Face, ce n'est pas seulement ses capacités techniques, mais aussi sa communauté dynamique. En interagissant avec cette communauté, vous accédez à une richesse de connaissances et de soutien.

Les utilisateurs contribuent continuellement à la bibliothèque, ajoutant de nouveaux modèles et fonctionnalités, ce qui en fait un écosystème vivant et évolutif. Cet esprit collaboratif garantit que la bibliothèque reste à la pointe de la recherche et de l'application en IA.

## Performance et évolutivité

Dans le monde de l'IA, la performance est essentielle, et la bibliothèque Hugging Face ne déçoit pas. Elle est conçue pour gérer efficacement des modèles à grande échelle, ce qui signifie que vous pouvez travailler avec certains des modèles d'IA les plus avancés sans avoir besoin d'un supercalculateur à votre disposition.

Hugging Face ne se limite pas non plus à l'anglais. Il prend en charge plusieurs langues, ce qui est essentiel pour les organisations et les développeurs visant à créer des applications d'IA pour une base d'utilisateurs diversifiée.

## Modèles populaires de Hugging Face

1. [**BERT (Bidirectional Encoder Representations from Transformers)**](https://huggingface.co/docs/transformers/model_doc/bert) : BERT excelle dans la compréhension du contexte d'un mot dans une phrase, ce qui le rend efficace pour des tâches comme l'analyse de sentiment, la réponse aux questions et la compréhension du langage. Il est largement utilisé dans les chatbots, les moteurs de recherche et pour améliorer l'interaction des utilisateurs avec les systèmes d'IA.
2. [**GPT (Generative Pretrained Transformer)**](https://huggingface.co/gpt2) : Connu pour sa capacité à générer du texte semblable à celui d'un humain, GPT est utilisé pour l'écriture créative, la génération de réponses conversationnelles et même l'écriture de code. Il est particulièrement populaire dans les chatbots, les outils de création de contenu automatisé et les applications de service client.
3. [**DistilBERT**](https://huggingface.co/docs/transformers/model_doc/distilbert) : Une version simplifiée de BERT, DistilBERT offre des capacités similaires mais est plus rapide et nécessite moins de puissance de calcul. Il est idéal pour les environnements où les ressources sont limitées, comme les applications mobiles, et est utilisé dans des tâches comme la classification de texte et l'extraction d'informations.
4. [**RoBERTa (Robustly Optimized BERT Approach)**](https://huggingface.co/docs/transformers/model_doc/roberta) : Une version optimisée de BERT, RoBERTa est entraînée sur un ensemble de données plus grand et pendant une période plus longue, ce qui conduit à une amélioration des performances. Il est utilisé dans des tâches NLP plus complexes comme l'analyse de sentiment, l'inférence de langage et la classification de texte.
5. [**T5 (Text-To-Text Transfer Transformer)**](https://huggingface.co/docs/transformers/model_doc/t5) : T5 convertit tous les problèmes de NLP en un format texte-à-texte, offrant une approche polyvalente pour des tâches comme la traduction, la synthèse et la réponse aux questions. Son adaptabilité en fait un outil précieux dans diverses applications, des services de traduction automatisée aux outils de synthèse d'informations.

Chacun de ces modèles a ses propres forces, et vous devez les choisir en fonction des exigences spécifiques de vos tâches. Assurez-vous d'équilibrer des facteurs comme les ressources de calcul, la complexité de la tâche et le niveau de performance souhaité.

## Comment utiliser la bibliothèque Transformers de Hugging Face

Permettez-moi de vous montrer à quel point il est facile de travailler avec la bibliothèque Transformers de Hugging Face. Nous allons implémenter un script de synthèse simple qui prend un texte long et retourne un résumé court.

Nous allons d'abord importer `pipeline` depuis la bibliothèque transformers. Dans Hugging Face, un "pipeline" est comme un outil qui vous aide à effectuer une série d'étapes pour transformer les données dans le format que vous souhaitez.

```
from transformers import pipeline
```

Le pipeline simplifie l'utilisation de ces outils pour différentes tâches, sans avoir besoin de connaître tous les détails complexes sur le fonctionnement interne de ces outils. Pour cet exemple, nous allons utiliser le pipeline "summarization".

```
summarizer = pipeline("summarization")
```

Et nous sommes maintenant prêts à commencer à utiliser le pipeline de synthèse. Passons un long morceau de texte et voyons quelle est la réponse.

```
text = """
Le développement de l'internet a été l'un des événements les plus transformateurs de l'histoire humaine, modifiant pratiquement tous les aspects de la vie moderne. Initialement conçu comme un réseau militaire et académique à la fin des années 1960, l'internet a rapidement évolué au cours des années 1970 et 1980, élargissant sa portée et ses capacités avec chaque année qui passait. L'introduction du World Wide Web au début des années 1990 a été un moment critique, rendant l'internet beaucoup plus accessible et convivial, déclenchant une révolution mondiale dans la communication, les affaires et les divertissements. En tant qu'outil de diffusion de l'information, l'internet a été sans précédent, permettant un accès instantané à d'énormes quantités de données du monde entier. Il a démocratisé l'information, brisant les barrières qui existaient autrefois en raison de la géographie ou du statut social. L'internet a également eu un impact profond sur le commerce, donnant naissance au commerce électronique et transformant les modèles commerciaux traditionnels. La facilité des achats en ligne et l'essor des places de marché numériques ont remodelé les habitudes et les attentes des consommateurs. Socialement et culturellement, l'internet a connecté les gens à travers le globe, facilitant l'échange d'idées et de cultures d'une manière qui était auparavant inimaginable. Cependant, il a également soulevé des préoccupations concernant la vie privée, la sécurité des données et la fracture numérique. La diffusion rapide de l'information a parfois conduit à la propagation de la désinformation, posant des défis pour les sociétés dans la distinction de la vérité et du mensonge. Alors que l'internet continue d'évoluer, il pose de nouveaux défis et opportunités, façonnant l'avenir de l'interaction humaine, de la gouvernance et de la technologie.
"""

summary = summarizer(text)
print(summary[0]['summary_text'])
```

Voici un exemple de réponse :

```
L'introduction de l'internet dans les années 1970 et 1980 a été un événement majeur pour la première fois dans le monde. En conséquence, l'internet a pu connecter les gens à travers le globe. L'internet a également soulevé des préoccupations concernant la vie privée et la sécurité à l'ère numérique du 21e siècle.
```

C'est à quel point il est facile de travailler avec la bibliothèque Transformers de Hugging Face.

## IA éthique et transparence : une étape vers une IA responsable

Puisque l'éthique de l'IA est de plus en plus sous les projecteurs, Hugging Face s'engage en faveur de la transparence et du développement responsable de l'IA. La nature open-source de la bibliothèque promeut un niveau de transparence essentiel pour le développement éthique de l'IA. Les utilisateurs peuvent voir exactement comment les modèles sont construits et prendre des décisions éclairées sur leur utilisation.

L'IA est un domaine qui n'est jamais statique, et il en va de même pour la bibliothèque Transformer de Hugging Face. Elle est continuellement mise à jour avec les dernières avancées en recherche sur l'IA. Cela signifie que lorsque vous utilisez Hugging Face, vous êtes toujours à la pointe de la technologie de l'IA.

Enfin, le vrai test de tout outil est ses applications dans le monde réel, et ici, Hugging Face excelle. Elle est utilisée par les universitaires pour des recherches de pointe et par les entreprises pour des applications pratiques comme l'analyse de sentiment, la génération de contenu et la traduction de langage.

## Conclusion

En résumé, la bibliothèque Transformer de Hugging Face est bien plus qu'une simple collection de modèles d'IA. C'est une porte d'entrée vers l'IA avancée pour les personnes de tous niveaux de compétence. Sa facilité d'utilisation et la disponibilité d'une gamme complète de modèles en font une bibliothèque exceptionnelle dans le monde de l'IA.

Que vous soyez un expert en IA chevronné ou que vous débutiez, la bibliothèque Hugging Face est une ressource utile qui peut vous aider à atteindre vos objectifs en matière d'IA.

J'espère que vous avez apprécié cet article. Trouvez plus de tutoriels pour débutants sur l'IA sur **[turingtalks.ai](https://www.turingtalks.ai/)**.