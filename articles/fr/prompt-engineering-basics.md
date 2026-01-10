---
title: Bases de l'ingénierie des prompts – Comment rédiger des prompts efficaces pour
  l'IA
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2024-07-29T19:22:13.000Z'
originalURL: https://freecodecamp.org/news/prompt-engineering-basics
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-from-2024-07-27-11-25-56.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Prompt Engineering
  slug: prompt-engineering
seo_title: Bases de l'ingénierie des prompts – Comment rédiger des prompts efficaces
  pour l'IA
seo_desc: 'Thanks to the popularity of various Large-Language Models like ChatGPT,
  prompt engineering has become a key skill for developers (and non-developers) to
  have. It''s important if you want to be able to tap into the full potential of these
  models.

  Wheth...'
---

Grâce à la popularité de divers grands modèles de langage comme ChatGPT, l'ingénierie des prompts est devenue une compétence clé pour les développeurs (et les non-développeurs). Elle est importante si vous souhaitez pouvoir exploiter tout le potentiel de ces modèles.

Que vous soyez développeur, chercheur ou utilisateur général, savoir comment rédiger des prompts efficaces et clairs vous aidera grandement à améliorer la qualité et la pertinence du contenu IA que vous recevez.

Dans ce guide, je vais expliquer les bases de l'ingénierie des prompts, avec quelques exemples pratiques et des conseils utiles pour vous aider à tirer le meilleur parti des modèles de langage IA.

## Qu'est-ce que l'ingénierie des prompts ?

L'ingénierie des prompts est l'art de concevoir et d'affiner les prompts d'entrée qui guident les modèles IA et les aident à générer des sorties utiles. En gros, c'est ce que vous "dites" à un modèle IA et comment vous le dites.

Un bon prompt établit le contexte, le ton et la spécificité de la réponse dans la sortie. Il guide l'IA afin qu'elle puisse produire un contenu qui correspond aux besoins de l'utilisateur.

C'est un outil incroyablement puissant à votre disposition pour des tâches comme la création de campagnes publicitaires, la génération d'exemples de code pour des tutoriels techniques, la recherche pour un voyage, l'apprentissage de nouvelles compétences, et même la pratique de votre écriture créative.

## Éléments clés d'un bon prompt

**Clarté et spécificité** : Un prompt clair et spécifique aidera l'IA à comprendre ce que vous voulez.

Par exemple, alors que vous pourriez demander "Parlez-moi de l'IA", une question plus spécifique pourrait être : "Expliquez comment fonctionne l'apprentissage par renforcement, en particulier dans le contexte de l'intelligence artificielle de jeu, comme AlphaGo. Expliquez les principaux concepts—la récompense, les états, les actions et les politiques—avec une illustration de la manière dont ces éléments sont utilisés lors de l'entraînement de l'IA."

**Contexte** : Cela aidera l'IA à faire une prédiction pertinente et précise dans sa réponse.

Par exemple, si vous allez écrire un article, vous devez mentionner qui vous pensez le lira, le ton de la voix et la portée : "Rédigez un plan pour un article d'introduction sur le Machine Learning pour débutants axé sur les applications pratiques."

**Contraintes et directives** : L'ajout de contraintes, telles que des limites de mots ou des directives stylistiques, aidera à affiner la sortie.

Par exemple, "Résuméz les points clés de l'article suivant en 200 mots."

**Exemples et analogies** : Vous pouvez également utiliser des exemples ou des analogies dans vos questions pour simplifier des idées techniques hautement complexes.

Par exemple, "Expliquez la technologie blockchain en termes simples, comme si vous l'expliquiez à un enfant de 10 ans."

## Exemples pratiques d'ingénierie des prompts

### Développeurs

* **Pour l'apprentissage** : "Expliquez la différence entre les listes et les tuples Python avec des exemples pratiques."
* **Pour la génération de code** : "Écrivez une fonction Python pour calculer la factorielle d'un nombre en utilisant la récursivité."
* **Pour le dépannage** : "Comment corriger l'erreur 'TypeError: unsupported operand type(s)' en Python ?"
* **Pour comprendre les concepts** : "Qu'est-ce que les décorateurs Python et comment fonctionnent-ils avec les fonctions ?"

### Support client :

* Prompt : "Fournissez une réponse polie à un client s'enquérant de l'état de sa commande, passée il y a une semaine et actuellement retardée."
* Réponse : "Nous nous excusons pour le retard de votre commande. Notre équipe travaille dur pour vous la faire parvenir dès que possible. Merci pour votre patience."

### Génération de contenu :

* Prompt : "Générez un article de blog de 300 mots sur les bienfaits de la méditation pour la santé mentale."
* Réponse : "La méditation a montré des résultats pour réduire le stress, améliorer la concentration et promouvoir le bien-être émotionnel..."

### Écriture créative :

* Prompt : "Écrivez une courte histoire sur un détective résolvant un mystère dans une petite ville côtière."
* Réponse : "Le détective Harper arriva dans la charmante ville côtière de Seaview, où une série de disparitions mystérieuses avait intrigué les locaux..."

## Conseils pour une ingénierie efficace des prompts

1. **Expérimentez et itérez** : N'ayez pas peur d'expérimenter avec différentes formulations et structures. Itérez en fonction des réponses de l'IA pour affiner les prompts.
2. **Soyez concis mais complet** : Essayez de fournir suffisamment d'informations sans submerger le modèle. Trouvez un équilibre entre brièveté et détail.
3. **Utilisez l'apprentissage par quelques exemples** : Fournissez des exemples de la sortie souhaitée si le modèle le supporte. Cette technique, connue sous le nom d'apprentissage par quelques exemples, aide le modèle à comprendre le format et le contenu attendus.

## Comment utiliser l'IA pour le développement d'articles techniques

Lors de la rédaction d'un article technique, l'IA peut être un outil précieux pour soutenir votre processus créatif. Voici comment utiliser l'IA de manière responsable pour améliorer votre écriture :

### 1. Génération d'idées

**Remue-méninges sur les sujets** : L'IA peut aider à générer une liste de sujets et d'angles potentiels pour votre article. Par exemple, si vous écrivez sur l'informatique quantique et la cryptographie, vous pouvez demander à l'IA les tendances émergentes, les défis ou les domaines spécifiques d'intérêt dans ces domaines.

_Exemple de prompt_ : "Suggérez quelques angles uniques à explorer lors de la rédaction sur l'impact de l'informatique quantique sur la cryptographie moderne."

**Identification des lacunes** : En analysant la littérature actuelle ou les discussions en ligne, l'IA peut aider à identifier les lacunes ou les domaines moins couverts qui pourraient faire ressortir votre article.

_Exemple de prompt_ : "Quelles sont certaines des implications moins connues de l'informatique quantique sur la sécurité des données ?"

### 2. Génération d'exemples de code

**Fourniture d'exemples de code** : Si votre article implique du contenu technique nécessitant des exemples de code, l'IA peut vous aider à rédiger des versions initiales. Par exemple, lors de la discussion sur les algorithmes cryptographiques, vous pouvez demander des implémentations ou des démonstrations d'exemples.

_Exemple de prompt_ : "Fournissez un exemple de code Python de base illustrant comment l'algorithme de Shor pourrait factoriser un petit entier."

**Explication du code** : L'IA peut aider à décomposer des extraits de code complexes en explications compréhensibles, facilitant ainsi la communication des détails techniques à votre audience.

_Exemple de prompt_ : "Expliquez ce code Python pour la mise en œuvre du chiffrement RSA de base en termes simples."

### 3. Création de titres et de plans

**Structuration de l'article** : L'IA peut vous aider à esquisser votre article avec des titres et des sous-titres. Cela aide à rester concentré et à couvrir toutes les idées principales du sujet en question.

_Exemple de prompt_ : "Esquissez un article technique discutant des menaces et des avantages de l'informatique quantique en cryptographie."

**Affinement du plan** : Une fois que vous avez un plan de brouillon, l'IA peut suggérer des sections supplémentaires ou affiner celles existantes pour améliorer la fluidité et la cohérence.

_Exemple de prompt_ : "Quels sous-sujets doivent être inclus sous la section 'Menaces potentielles de l'informatique quantique pour la cryptographie' ?"

### 4. Formulation et phrasé spécifiques

**Clarification des concepts complexes** : Si vous avez du mal à expliquer un concept complexe, l'IA peut offrir des formulations alternatives plus claires ou plus concises.

_Exemple de prompt_ : "Comment puis-je expliquer le concept de 'superposition quantique' de manière simple et accessible ?"

**Polissage du langage** : L'IA peut également aider à affiner votre langage, garantissant que votre écriture est engageante et accessible à votre public cible.

_Exemple de prompt_ : "Suggérez une introduction plus engageante pour mon article sur l'impact de l'informatique quantique sur la cryptographie."

### 5. Considérations éthiques et meilleures pratiques

**Support, pas remplacement, du travail original** : Bien que l'IA puisse fournir une assistance précieuse, il est crucial de l'utiliser comme un outil de support plutôt que comme un remplacement pour vos propres recherches et écritures. S'engager profondément avec le matériel vous aide à développer une compréhension plus complète du sujet.

**Vérification et attribution** : Vérifiez toujours les informations et les exemples fournis par l'IA. Si vous utilisez des données ou des insights spécifiques, attribuez-les de manière appropriée pour maintenir la transparence et la crédibilité.

**Encourager l'apprentissage continu** : L'utilisation de l'IA devrait compléter vos efforts pour apprendre et grandir dans votre domaine. Le processus de recherche et d'écriture de manière indépendante est inestimable pour développer une expertise et des compétences de pensée critique.

## Conclusion

L'ingénierie des prompts est l'une des compétences les plus importantes que vous devriez connaître si vous travaillez avec des modèles de langage IA.

Des prompts bien réfléchis et précis libèrent tout le pouvoir de ces modèles afin qu'ils puissent vous aider à trouver des idées pour des articles utiles, répondre à des questions ou créer des interactions engageantes.

Plus les technologies IA deviendront sophistiquées, plus la maîtrise de l'ingénierie des prompts sera précieuse pour communiquer efficacement et efficacement avec de tels systèmes intelligents.