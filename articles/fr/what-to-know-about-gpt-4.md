---
title: Ce qu'il faut savoir sur GPT-4 pour les développeurs non-IA
subtitle: ''
author: Kaushal Joshi
co_authors: []
series: null
date: '2023-04-06T14:15:36.000Z'
originalURL: https://freecodecamp.org/news/what-to-know-about-gpt-4
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/gpt-4.gif
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: chatgpt
  slug: chatgpt
seo_title: Ce qu'il faut savoir sur GPT-4 pour les développeurs non-IA
seo_desc: 'We are living through an AI revolution. The AI industry is constantly evolving,
  with new tools, products, and technologies emerging every day.

  For those not familiar with the AI domain, keeping up with these developments can
  be challenging.

  The bigge...'
---

Nous vivons une révolution de l'IA. L'industrie de l'IA évolue constamment, avec de nouveaux outils, produits et technologies émergent chaque jour.

Pour ceux qui ne sont pas familiers avec le domaine de l'IA, suivre ces développements peut être un défi.

La plus grande nouvelle récemment est sans aucun doute GPT-4. Tout le monde, de mon coiffeur aux influenceurs de Twitter, veut en savoir plus. Mes collègues développeurs de logiciels ne font pas exception. On a l'impression d'avoir la FOMO parce que nous ne sommes pas à jour avec ce qui se passe dans le domaine de l'IA.

Dans cet article, nous allons couvrir tout ce que nous savons publiquement sur GPT-4. Donc, si vous n'êtes pas familier avec des termes comme ChatGPT, GPT-4, OpenAI et autres mots à la mode, ce guide est celui que vous devez lire.

## Histoire de GPT jusqu'à présent

OpenAI a annoncé GPT-3 en 2020. Il s'agit d'un modèle de langage formé sur un ensemble de données massif disponible sur Internet. Il peut être votre ami et répondre à vos questions, vous aider à déboguer ou à écrire du code, résoudre des questions logiques et d'aptitude, traduire du texte, et bien plus encore.

À la fin de 2022, l'entreprise a publié un aperçu gratuit de [ChatGPT](https://chat.openai.com/). Il s'agit d'un chatbot IA construit avec GPT-3.5, le successeur de GPT-3. ChatGPT est rapidement devenu le sujet de discussion de la ville (du monde !). Plus d'un million de personnes se sont inscrites pour l'aperçu en seulement cinq jours.

%[https://twitter.com/gdb/status/1599683104142430208?s=20] 

En janvier 2023, Microsoft a investi (selon les rapports) 10 milliards de dollars dans OpenAI. Nous discuterons plus tard de l'importance de cela.

Et enfin, OpenAI a [publié](https://openai.com/research/gpt-4) GPT-4 en mars 2023, ce qui a secoué le monde avec ses capacités.

## Qu'est-ce que GPT-4 ?

"Generative Pre-trained Transformer 4" ou GPT-4 est un modèle de langage multimodal de grande taille (LLM). Il est plus fiable, créatif et peut gérer des instructions plus complexes que GPT-3.5. Il surpasse tous les modèles d'IA connus dans tous les paramètres de mesure.

GPT-4 est le résultat des efforts d'OpenAI pour augmenter l'échelle de l'apprentissage profond. C'est le modèle d'IA le plus capable à ce jour. Bien qu'il soit moins capable que les humains dans de nombreux scénarios du monde réel, il excelle dans plusieurs benchmarks professionnels et académiques avec une précision de niveau humain.

## Disponibilité de GPT-4

GPT-4 n'est pas disponible pour tout le monde, contrairement à ChatGPT. Il existe plusieurs moyens d'y accéder :

1. [**Liste d'attente pour l'API**](https://openai.com/waitlist/gpt-4-api) : Vous pouvez vous inscrire sur la liste d'attente et obtenir un accès limité à l'API GPT-4
    
2. **Accès prioritaire** : Les développeurs peuvent contribuer à [OpenAI Evals](https://github.com/openai/evals) et obtenir un accès à l'API une fois la contribution fusionnée.
    
3. [**ChatGPT Plus**](https://openai.com/blog/chatgpt-plus) : Il est également disponible pour les abonnés ChatGPT Plus avec des frais mensuels de 20 $.
    
4. **Microsoft Bing** : Il alimente également le moteur de recherche Bing de Microsoft, récemment repensé. Il est actuellement disponible pour certains utilisateurs.
    
5. **Services tiers** : OpenAI a collaboré avec plusieurs organisations pour intégrer GPT-4, comme Duolingo, Morgan Stanley et Khan Academy, pour n'en nommer que quelques-unes.
    

## Capacités de GPT-4

GPT-4 surpasse la majorité des humains dans divers benchmarks professionnels et académiques. L'entreprise a testé le dernier modèle avec le précédent avec certains des examens les plus difficiles au monde. Et GPT-4 a excellé dans tout ce qui lui a été soumis, avec des résultats significatifs.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-259.png align="left")

*comparaison de GPT-4 avec GPT-3.5 dans divers examens compétitifs (source : OpenAI)*

OpenAI a publié un [article technique](https://arxiv.org/abs/2303.08774) qui analyse cela plus en détail.

L'équipe a passé 6 mois à rendre GPT-4 plus sûr et plus aligné. GPT-4 est 82 % moins susceptible de répondre aux demandes de contenu interdit et 40 % plus susceptible de produire des réponses factuelles que GPT-3.5 sur nos évaluations internes.

## Nouvelles méthodes d'entrée améliorées

GPT-4 sert les prompts des utilisateurs de manière intelligente. Il est meilleur pour gérer de grands textes et des entrées d'images. Il peut également changer sa personnalité pour vous parler !

### Fournir des prompts jusqu'à 25 000 mots

GPT-3.5 ne pouvait gérer que des entrées de texte allant jusqu'à 3 000 mots. GPT-4 va bien au-delà, acceptant des entrées allant jusqu'à 25 000 mots. Il peut également accepter des contributions graphiques.

Bien que GPT-4 ait du mal à traiter de grandes quantités de données, il reste supérieur à GPT-3.5. La longueur d'entrée accrue vous aidera à contextualiser vos prompts plus clairement. Vous pouvez fournir des documents entiers, des thèses et des pages web comme prompt en une seule fois.

### Télécharger une image comme prompt

Les entrées d'images sont encore en aperçu de recherche et ne sont pas encore disponibles publiquement. Pour l'instant, seul [be my eyes](https://www.bemyeyes.com/) supporte les dernières entrées d'images.

Néanmoins, les entrées d'images ont des capacités et des fonctionnalités identiques à celles des entrées de texte. Les utilisateurs peuvent spécifier la vision ou le langage pour obtenir le résultat souhaité. Il peut également être augmenté avec des techniques de temps de test développées pour les modèles de langage en texte uniquement, y compris le few-shot et le chain-of-thought prompting.

Une autre observation concernant les prompts d'entrée est que GPT-4 se souvient des conversations précédentes au sein d'une seule session de chat. Il peut faire référence à ce qu'il a dit dans le passé ou rappeler ce que vous avez demandé. Mais il ne peut pas encore se souvenir des conversations entre différentes sessions.

### Vous pouvez changer sa personnalité

Je dois dire que je suis fan de cette fonctionnalité. Les LLM peuvent changer leur personnalité et leur comportement selon les prompts des utilisateurs. Nous appelons cela la "dirigeabilité" en IA.

GPT-3.5 a une personnalité fixe avec un vocabulaire, un ton et un style prédéfinis. Tout ce qu'il répond semble être le même. Avec GPT-4, nous pouvons décrire des personnalités dans le message système. L'entreprise explique dans son blog qu'il est plus facile pour ChatGPT de rompre son caractère, donc la personnalité n'est changée que "dans certaines limites".

Cela est utile dans les scénarios où vous voulez que la réponse soit comme une personnalité spécifique. Vous pouvez lui dire d'être un auditeur compatissant, un guide, un mentor, un tuteur, etc.

Le blog explique la dirigeabilité en donnant un exemple de tuteur socratique. La [méthode socratique](https://en.wikipedia.org/wiki/Socratic_method) est une discussion entre un individu avec lui-même ou avec d'autres qui trouve des solutions en posant constamment des questions et en y répondant avec une pensée critique. En utilisant la méthode socratique, nous pouvons réfléchir de manière critique à un problème complexe et le comprendre mieux.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-22.png align="left")

## Plugins ChatGPT

Et quand nous pensions que tout se calmait, OpenAI a annoncé des plugins pour ChatGPT. Jusqu'à présent, GPT-4 reposait uniquement sur ses données d'entraînement, qui ont été mises à jour pour la dernière fois en septembre 2021. Il n'était pas connecté au monde extérieur.

Avec les plugins, il peut accéder à tout Internet. Les utilisateurs peuvent installer des plugins dans leur ChatGPT pour lui permettre d'accéder au monde extérieur. Maintenant, il peut interagir avec le monde réel et des données mises à jour pour effectuer diverses tâches pour vous.

Les plugins peuvent agir comme des "yeux et oreilles" pour les LLM. Cela permet aux LLM d'accéder à des informations indisponibles dans leurs données d'entraînement. Cela inclut les données trop récentes, personnelles ou spécifiques pour être incluses dans les données d'entraînement. Les plugins peuvent utiliser de telles informations pour produire des résultats meilleurs, plus précis et plus précis.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-20.png align="left")

*11 entreprises s'associant à OpenAI pour construire des plugins (Source : [Blog OpenAI](https://openai.com/blog/chatgpt-plugins))*

OpenAI s'est associé à 11 entreprises pour créer de tels plugins. Expedia, FiscalNote, Milo et Zapier sont quelques-unes des entreprises qui ont déjà créé leurs plugins. L'entreprise héberge également deux plugins : un navigateur web et un interpréteur de code. Elle a [open-sourcé](https://github.com/openai/chatgpt-retrieval-plugin) un plugin de récupération de base de connaissances.

Vous pouvez rejoindre la liste d'attente en soumettant votre intérêt sur son [site web](https://openai.com/waitlist/plugins). Si vous voulez en savoir plus, j'ai récemment écrit un [blog](https://www.showwcase.com/show/34206/chatgpt-has-a-game-changer-update) qui discute des plugins en détail.

## Ce qui est construit avec GPT-4 ?

Il existe plusieurs outils disponibles aujourd'hui qui sont construits sur GPT-4. OpenAI s'est associé à différentes entreprises en deux étapes. La première étape était pour le lancement de GPT-4 lui-même.

### Microsoft

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-28.png align="left")

*Source : Unsplash (Ed Hardie)*

Au début de l'article, j'ai mentionné que Microsoft a investi 10 milliards de dollars dans OpenAI. Microsoft intègre GPT-4 dans sa suite de services existants, principalement Office-365 et Microsoft Edge. Voici une brève description de chaque outil ou service Microsoft intégré avec les services OpenAI/GPT-4.

1. [**Copilot pour le Web**](https://blogs.microsoft.com/blog/2023/02/07/reinventing-search-with-a-new-ai-powered-microsoft-bing-and-edge-your-copilot-for-the-web/) : Microsoft Bing et Edge ont intégré GPT-4 pour une expérience meilleure, plus complète et créative.
    
2. [**OpenAI dans Azure**](https://azure.microsoft.com/en-us/blog/chatgpt-is-now-available-in-azure-openai-service/) : ChatGPT est disponible en aperçu dans Azure OpenAI Service.
    
3. [**Copilot X**](https://www.showwcase.com/show/34112/everything-you-need-to-know-about-github-copilot-x) : GitHub, un produit appartenant à Microsoft, a également introduit Copilot X qui utilise GPT-4 pour de nouvelles fonctionnalités.
    
4. [**Copilot pour le Travail**](https://blogs.microsoft.com/blog/2023/03/16/introducing-microsoft-365-copilot-your-copilot-for-work) : Microsoft a introduit Microsoft 365 Copilot, qui vise à transformer vos mots en l'outil de productivité le plus puissant de la planète.
    

### Duolingo

![Image](https://blog.duolingo.com/content/images/2023/02/DuoNews-622x296--1-.png align="left")

*Duolingo Max (Source : [Blog Duolingo](https://blog.duolingo.com/duolingo-max/))*

Duolingo a intégré GPT-4 et lancé [**Duolingo Max**](https://blog.duolingo.com/duolingo-max/). Il introduit deux nouvelles fonctionnalités : Expliquer ma réponse et Jeu de rôle. La première explique pourquoi les réponses de l'utilisateur étaient correctes ou incorrectes, et fournit des exemples supplémentaires pour une meilleure clarification. La seconde permet aux apprenants de pratiquer des compétences de conversation du monde réel avec des personnages du monde dans l'application.

### Be My Eyes

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-25.png align="left")

*source : Internet*

Be My Eyes est une plateforme pour les personnes malvoyantes pour les aider à mieux interpréter le monde. GPT-4 agit comme un bénévole virtuel et analyse les images grâce au générateur d'images en texte de GPT-4. Il n'analyse pas seulement le contenu de l'image, mais aussi le contexte de l'image.

### Khan Academy

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-26.png align="left")

*Source : [Khan Academy](https://www.khanacademy.org/khan-labs)*

Khan Academy est également l'un des premiers adopteurs de GPT-4. Il entend utiliser GPT-4 comme assistant d'étude et technique. Il peut aider les étudiants dans la préparation des examens, l'amélioration et la pratique du vocabulaire, et ainsi de suite. Il peut également aider les enseignants dans les tâches administratives, la rédaction de leçons et la création de crochets de leçons, la rédaction de tickets de sortie, et des tâches similaires.

### Stripe

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-27.png align="left")

*Source : [Stripe](https://stripe.com/en-in)*

Maintenant, Stripe intègre GPT-4 dans sa plateforme. L'entreprise utilisait déjà GPT-3 pour des tâches simples, mais l'intégration de GPT-4 signifie que l'IA jouera un rôle plus important dans les processus de l'entreprise. Il entend utiliser GPT-4 pour rationaliser l'expérience utilisateur et ajouter une autre couche de détection de fraude.

## Ce que font les concurrents

Les gens ont commencé à utiliser ChatGPT et Microsoft Sydney pour leurs recherches sur Internet. Google a reconnu la menace imminente pour leur entreprise et a agi rapidement. L'entreprise a annoncé "Bard", son propre chatbot IA qui concurrence GPT-4.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-19.png align="left")

*Source : [Google](https://bard.google.com/)*

Google Bard est un chatbot IA génératif qui peut produire des réponses textuelles basées sur les requêtes ou les prompts des utilisateurs. Bard utilise sa propre connaissance interne et sa créativité pour générer des réponses. Bard est alimenté par une nouvelle version de LaMDA, le modèle de langage de grande taille phare de Google qui a été affiné avec des retours humains.

Bard permet les entrées vocales ainsi que le texte brut. Il permet également de faire une recherche Google avec le même prompt pour vérifier les réponses de Bard.

Une chose à noter ici est que Bard nous rappelle constamment qu'il s'agit toujours d'un modèle expérimental et qu'il peut halluciner. Il n'oublie pas non plus de mentionner que Google ne soutient aucune des opinions que Bard peut exprimer.

Google Bard est actuellement disponible aux États-Unis et en Grande-Bretagne. Vous pouvez rejoindre la liste d'attente en visitant le [site officiel de Bard](https://bard.google.com/). J'ai écrit un [blog](https://www.showwcase.com/show/34094/everything-you-need-to-know-about-bard) discutant plus en détail de Bard. Assurez-vous de le lire également.

## L'IA va-t-elle prendre votre emploi ?

Après avoir lu l'article entier, vous pourriez vous sentir préoccupé par votre emploi. OpenAI, OpenResearch et l'Université de Pennsylvanie ont publié un article, "[**GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Model**](https://arxiv.org/abs/2303.10130)", pour analyser l'impact potentiel de tels outils sur le marché du travail.

Selon l'étude, 10 % des tâches de 80 % des travailleurs américains peuvent être effectuées par des LLM. Pour les ~19 % restants des travailleurs, les LLM pourraient influencer au moins 50 % des tâches. Les emplois à revenu élevé seront potentiellement plus exposés. Les emplois de programmation et d'écriture seront également impactés. D'un autre côté, les emplois qui nécessitent une pensée critique et des sciences sont sûrs. De même, les emplois avec une faible barrière à l'entrée sont moins susceptibles d'être impactés.

Ces emplois sont plus susceptibles d'être pris en charge par l'IA :

* mathématiciens
    
* préparateurs de taxes
    
* écrivains
    
* designers web, programmeurs
    
* comptables
    
* journalistes
    
* secrétaires juridiques
    

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-17.png align="left")

*L'IA sera plus susceptible de prendre ces emplois (Source : [Article de recherche](https://arxiv.org/abs/2303.10130))*

Les emplois qui sont moins susceptibles d'être impactés par GPT sont les suivants :

* designers graphiques
    
* stratégies de marketing de recherche
    
* gestionnaires financiers
    

Les chercheurs listent également l'impact des LLM sur diverses industries. Les industries avec l'impact le plus significatif sont les suivantes :

* services de traitement de données
    
* services d'information
    
* industries de l'édition
    
* transporteurs d'assurance
    

D'un autre côté, les industries avec l'impact le plus négligeable sont :

* fabrication alimentaire
    
* fabrication de produits en bois
    
* fabrication de soutien
    
* agriculture et sylviculture
    

![L'IA est très peu susceptible de prendre ces emplois (Source : Article de recherche)](https://www.freecodecamp.org/news/content/images/2023/04/image-18.png align="left")

*L'IA est très peu susceptible de prendre ces emplois (Source : [Article de recherche](https://arxiv.org/abs/2303.10130))*

## Épilogue

Si vous avez lu jusqu'au bout, donnez-vous une tape dans le dos ! Vous avez parcouru un long chemin et vous devriez maintenant connaître suffisamment ce mot à la mode pour partager vos connaissances lors de réunions et de retrouvailles.

J'espère que vous avez appris quelque chose dans cet aperçu de ChatGPT. Si c'est le cas, partagez-le dans vos réseaux afin que tout le monde puisse en bénéficier.

Presque toutes les informations ont été compilées à partir de blogs d'annonces existants, d'articles de recherche et de contenu publié par les comptes officiels des entreprises. Néanmoins, si vous trouvez une erreur ou une amélioration, faites-le moi savoir. Je serais ravi de corriger mes erreurs.

Restez en contact ! Je veux savoir ce que vous pensez de cet article. Pensez-vous que l'IA remplacera nos emplois ? Faites-le moi savoir. Voici comment vous pouvez me joindre :

* [Twitter](https://twitter.com/clumsy_coder)
    
* [Site web personnel](https://kaushaljoshi.dev/)
    
* [Showwcase](https://www.showwcase.com/clumsycoder)
    
* [Peerlist](https://peerlist.io/kaushal)
    

Enfin, consultez mon [blog personnel](https://blog.kaushaljoshi.dev/), où j'écris sur le développement front-end, l'open source, la technologie et la rédaction technique.

Restez curieux ! ✨