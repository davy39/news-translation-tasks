---
title: 'Outils d''apprentissage automatique AWS : Le guide complet'
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-10-06T12:10:00.000Z'
originalURL: https://freecodecamp.org/news/aws-machine-learning-tools-the-complete-guide
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/wall-7.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: framework
  slug: framework
- name: Machine Learning
  slug: machine-learning
- name: tools
  slug: tools
seo_title: 'Outils d''apprentissage automatique AWS : Le guide complet'
seo_desc: 'In this article, we will take a look the machine learning tools offered
  by AWS. We''ll also understand the type of problems they try to solve for their
  customers.

  AWS Machine Learning comprises a rich set of tools that Amazon offers to help developers...'
---

Dans cet article, nous allons examiner les outils d'apprentissage automatique proposés par AWS. Nous comprendrons également le type de problèmes qu'ils tentent de résoudre pour leurs clients.

[AWS Machine Learning](https://aws.amazon.com/machine-learning/) comprend un ensemble riche d'outils qu'Amazon offre pour aider les développeurs à intégrer des modèles d'apprentissage automatique dans leurs applications. 

AWS propose également des modèles pré-entraînés pour des cas d'utilisation incluant la vision par ordinateur, les moteurs de recommandation et la traduction linguistique.

Amazon propose actuellement 15 services d'apprentissage automatique sur sa plateforme. Dans cet article, nous allons examiner chacun d'eux afin de comprendre le type de problème qu'ils tentent de résoudre pour leurs clients.

## SageMaker

[Amazon SageMaker](https://aws.amazon.com/sagemaker/) vous aide à passer de la conception à la production de vos modèles d'apprentissage automatique en une fraction de temps par rapport aux approches traditionnelles basées sur le code. 

Sagemaker est un service géré et dispose de l'ensemble complet d'outils dont vous avez besoin pour construire, entraîner et déployer vos modèles d'apprentissage automatique. Ils vous aident à étiqueter vos données, optimiser vos algorithmes, et plus encore. C'est une solution complète pour créer et déployer des modèles d'apprentissage automatique.

SageMaker dispose également d'une option autopilot qui traitera automatiquement les données et les fera passer par plusieurs algorithmes. Cela aide les développeurs à trouver le meilleur algorithme pour leur modèle sans entraîner et tester manuellement ces modèles. 

Sagemaker est également livré avec un IDE intégré et un notebook Jupyter partageable que vous pouvez utiliser pour collaborer avec votre équipe.

## CodeGuru

[Amazon CodeGuru](https://aws.amazon.com/codeguru/) vous permet d'automatiser vos revues de code et les optimisations de performance pour votre application. 

Il peut trouver des problèmes comme les [conditions de course](https://searchstorage.techtarget.com/definition/race-condition), les fuites de ressources et les cycles CPU gaspillés. Cela vous aide à produire un code de meilleure qualité en fournissant des recommandations spécifiques basées sur le contexte du code.

Les algorithmes de CodeGuru sont entraînés avec des bases de code provenant des projets d'Amazon. Pour l'instant, CodeGuru ne prend en charge que les applications Java, mais vous pouvez vous attendre à ce que la fonctionnalité s'étende à d'autres langages dans un avenir proche.

## Comprehend

[Amazon Comprehend](https://aws.amazon.com/comprehend/) est un service de traitement du langage naturel d'Amazon qui utilise l'apprentissage automatique pour trouver des informations précieuses à partir de données textuelles. 

Comprehend peut travailler avec des données non structurées comme des avis de produits, des e-mails de clients, des tweets Twitter, etc., pour vous aider à tirer des conclusions (comme le sentiment général du public).

C'est également un service entièrement géré, ce qui signifie que vous pouvez utiliser des modèles pré-entraînés pour travailler avec vos données. Comprehend dispose également d'un service supplémentaire appelé Amazon Comprehend Medical qui vous permet de travailler avec des documents médicaux pour analyser des conditions médicales et des dosages.

## Forecast

[Amazon Forecast](https://aws.amazon.com/forecast/) est utilisé pour construire des modèles de prédiction de séries temporelles en utilisant vos ensembles de données existants. 

Forecast fonctionne très bien pour des cas d'utilisation comme la prédiction des futures dépenses commerciales, la prédiction des prix des actions et la planification des ressources pour les organisations en fonction de la demande des clients.

Ce service est également personnalisable et vous permet de construire des modèles personnalisés sur la base des modèles d'apprentissage profond existants d'Amazon. Comme la plupart des outils d'apprentissage automatique dans AWS, Forecast est également entièrement géré et peut s'adapter selon vos besoins commerciaux.

## Fraud Detector

[Amazon Fraud Detector](https://aws.amazon.com/fraud-detector/) est un autre service entièrement géré qui vous aide à détecter les inscriptions frauduleuses et les transactions frauduleuses. 

Le détecteur de fraude peut identifier les comptes potentiellement frauduleux et vous aide ensuite à mettre en place une vérification supplémentaire pour ces comptes signalés.

Un détecteur de fraude a besoin d'un ensemble de données existant de transactions frauduleuses étiquetées afin de s'entraîner et de comprendre le schéma de comportement de vos clients. Il utilise ensuite ces données pour prévenir d'autres transactions frauduleuses. 

Vous pouvez également configurer des règles d'authentification personnalisées pour les connexions d'invités et les essais de produits.

## Kendra

[Amazon Kendra](https://aws.amazon.com/kendra/) est un moteur de recherche d'entreprise alimenté par l'IA qui vous aidera à fournir des résultats de recherche très précis basés sur les requêtes des clients. 

Vous pouvez utiliser Kendra pour alimenter les moteurs de recherche dans vos produits qui aident vos utilisateurs à trouver exactement ce qu'ils recherchent.

Kendra peut également être utilisé pour aider les clients à trouver des réponses à des problèmes spécifiques tout en utilisant votre produit sans avoir besoin d'un support client supplémentaire. 

Kendra prend également en charge les questions en langage naturel, offrant une expérience encore plus fluide pour vos clients.

## Lex

[Amazon Lex](https://aws.amazon.com/lex/) vous permet de construire des interfaces conversationnelles dans vos produits. Lex offre des modèles de [compréhension du langage naturel (NLU)](https://en.wikipedia.org/wiki/Natural-language_understanding) qui peuvent comprendre les entrées conversationnelles des utilisateurs et effectuer les bonnes actions.

Lex peut être utilisé comme un remplacement pour le support client manuel afin d'aider à filtrer les requêtes courantes et y répondre automatiquement. C'est également un service entièrement géré qui s'adapte automatiquement et utilise un modèle de paiement à l'usage.

## Personalize

[Amazon Personalize](https://aws.amazon.com/personalize/) vous permet de créer des recommandations personnalisées pour vos clients en fonction de leurs habitudes d'utilisation. 

Alors que les moteurs de recommandation traditionnels ne peuvent être utilisés que pour recommander des produits, Personalize vous permet littéralement de personnaliser chaque étape de l'expérience utilisateur de vos clients.

Personalize est un excellent outil pour construire des recommandations de produits, des résultats de recherche personnalisés basés sur des requêtes et employer des promotions marketing ciblées.

## Polly

[Amazon Polly](https://aws.amazon.com/polly/) vous aide à construire des produits activés par la voix pour vos clients. Polly fournit des sorties vocales réalistes dans une variété de langues, y compris le chinois, le coréen et le japonais.

Polly est alimenté par des algorithmes d'apprentissage profond qui imitent une interface de style conversationnel qui peut être utilisée dans des narrations, des applications de téléphonie et d'autres applications.

## Rekognition

[Amazon Rekognition](https://aws.amazon.com/rekognition/) est une solution de vision par ordinateur d'AWS qui aide les développeurs à construire des applications capables de reconnaître des objets à partir d'images et de vidéos. 

En plus de la reconnaissance automatique d'objets, vous pouvez personnaliser Rekognition pour détecter des objets et des scènes spécifiques en fonction de vos propres exigences.

Rekognition peut être utilisé dans des cas d'utilisation comme l'identification des défauts de fabrication dans les produits, la détection de personnel non autorisé dans une organisation, la recherche de contenu inapproprié dans les films, etc. Il peut également être utilisé pour analyser les mouvements des joueurs dans les jeux pour une analyse post-jeu.

## Textract

[Amazon Textract](https://aws.amazon.com/textract/) vous permet de lire des données à partir de documents scannés. L'approche habituelle pour numériser des documents papier consiste à utiliser la saisie manuelle de données ou des [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition) avec des configurations personnalisées. 

Textract simplifie cela en appliquant automatiquement des règles aux documents et en extrayant des données précieuses ainsi que des composants comme des formulaires et des images dans le document.

Textract est utile pour le traitement des demandes de prêt, des réclamations médicales, et plus encore. En plus d'extraire des données, celles-ci peuvent être optimisées pour la recherche en utilisant Textract. Les documents qui prennent généralement des mois à être traités avec des méthodes manuelles peuvent être traités en quelques heures avec AWS Textract.

## Transcribe

[Amazon Transcribe](https://aws.amazon.com/transcribe/) vous permet de construire des services de reconnaissance vocale dans votre application. Transcribe est utile pour construire des services de transcription médicale, du streaming audio, générer des sous-titres pour des enregistrements vidéo, et plus encore.

Transcribe peut également être utilisé pour convertir les appels clients en texte et les analyser pour améliorer le service client. La catalogation des archives audio est un autre cas d'utilisation pour AWS Transcribe.

## Translate

[Amazon Translate](https://aws.amazon.com/translate/) est un service d'apprentissage automatique similaire à Google Translate. Translate peut travailler avec une variété de langues avec une grande précision, ce qui permet aux entreprises de personnaliser leurs langues en fonction de la démographie de leur public.

Translate est également conçu pour être plus naturel pour les clients, car le contexte de la phrase est également pris en compte. 

Translate est également hautement personnalisable, ce qui peut aider à améliorer la précision de la traduction lors de l'utilisation de vos noms de marque et de mots uniques liés à votre entreprise.

## DeepLens

[Amazon DeepLens](https://aws.amazon.com/deeplens/) est une caméra vidéo avec des capacités d'apprentissage profond intégrées qui vous aide à construire et tester des modèles de vision par ordinateur en temps réel. 

DeepLens est entièrement programmable et peut être utilisé pour tester des modèles comme la reconnaissance d'objets en direct, la classification d'oiseaux/animaux, la détection de visages, etc.

Le produit est conçu pour les développeurs qui commencent dans l'apprentissage automatique. Il les aide à comprendre comment leurs modèles fonctionneront dans le monde réel. 

DeepLens est également intégré à l'écosystème AWS et peut être utilisé avec d'autres services AWS comme Lambda et Rekognition pour étendre ses capacités.

## DeepRacer

Si vous êtes un fan de voitures autonomes, [AWS DeepRacer](https://aws.amazon.com/deepracer/) est une petite voiture de course autonome conçue par AWS qui fonctionne en utilisant l'apprentissage automatique. DeepRacer vous aide à tester vos modèles d'apprentissage par renforcement en utilisant une piste physique.

Vous pouvez construire des modèles d'apprentissage par renforcement en utilisant AWS SageMaker et les tester instantanément avec DeepRacer. Amazon vous donne également l'opportunité de vous connecter et de rivaliser avec d'autres passionnés de course en construisant des pistes de course privées virtuelles.

## Résumé

Avec une solution à presque tous les problèmes d'apprentissage automatique, Amazon Machine Learning offre un ensemble riche d'outils pour les ingénieurs en apprentissage automatique. 

Amazon ajoute également de nouveaux services tous les quelques mois en fonction de nouveaux cas d'utilisation, ce qui en fait l'une des plateformes les plus fiables où les ingénieurs peuvent construire des solutions d'IA pour leurs clients.

_Aimez cet article ?_ [**_Rejoignez ma Newsletter_**](http://tinyletter.com/manishmshiva) _et obtenez un résumé de mes articles et vidéos chaque lundi._