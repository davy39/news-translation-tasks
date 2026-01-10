---
title: Comment communiquer avec ChatGPT – Un guide sur l'ingénierie des prompts
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2023-04-20T20:54:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-communicate-with-ai-tools-prompt-engineering
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/ChatGPT--1-.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: chatgpt
  slug: chatgpt
- name: communication
  slug: communication
- name: Machine Learning
  slug: machine-learning
seo_title: Comment communiquer avec ChatGPT – Un guide sur l'ingénierie des prompts
seo_desc: "AI has become an integral part of our lives and businesses. Over the past\
  \ few years, we’ve seen the rapid rise of AI tools, and their impact on our day-to-day\
  \ activities can't be ignored. \nFrom virtual assistants to chatbots, AI just keeps\
  \ getting sm..."
---

L'IA est devenue une partie intégrante de nos vies et de nos entreprises. Au cours des dernières années, nous avons assisté à la montée rapide des outils d'IA, et leur impact sur nos activités quotidiennes ne peut être ignoré. 

Des assistants virtuels aux chatbots, l'IA ne cesse de devenir plus intelligente avec plus de fonctionnalités qu'auparavant. Cette technologie a changé la façon dont nous interagissons avec les humains et les machines.

Alors que cette évolution se poursuit, il y a un besoin constant d'améliorer la communication entre les humains et les machines. En comprenant pleinement comment communiquer efficacement avec l'IA, cela peut nous rapprocher de la réalisation de son plein potentiel. 

Cela nous permettra non seulement d'extraire des informations pertinentes, mais aussi de gagner de nouvelles perspectives, nous rendant plus informés dans différents domaines d'intérêt. Pour obtenir ces avantages, comprendre l'ingénierie des prompts est essentiel.

En tant que développeur en croissance, je passe la meilleure partie de mon temps à apprendre et à mettre en œuvre. Dans ce processus, je peux avoir besoin de faire des recherches, et cela peut prendre une éternité pour trouver ce dont j'ai besoin en naviguant sur le net. Mais avec de nouvelles technologies comme ChatGPT, je peux facilement obtenir ce dont j'ai besoin tant que je pose les bonnes questions. 

Comme beaucoup d'autres, comprendre la plateforme n'était pas facile. Il m'a fallu un certain temps avant de comprendre comment communiquer avec le modèle. Un aspect clé est de savoir comment structurer et formuler les prompts. Avec cela, vous pourrez améliorer la qualité et la précision des réponses que vous obtenez.

Dans ce guide, vous apprendrez ce qu'est l'ingénierie des prompts et comment vous pouvez l'utiliser pour améliorer votre communication avec les outils d'IA. En plus de cela, nous explorerons également différentes catégories de prompts et les principes de conception utilisés pour créer des prompts efficaces. 

À la fin de ce guide, vous devriez être capable d'écrire de bons prompts et de les adapter à vos besoins, facilitant ainsi une meilleure interaction entre vous et les modèles de langage. 

Commençons !

## Qu'est-ce que l'ingénierie des prompts ?
La communication avec l'IA est cruciale et comprendre comment communiquer efficacement avec elle est utile. L'ensemble du processus de communication tourne autour de l'écriture de commandes qui sont appelées prompts. 

Cela dit, nous pouvons facilement définir l'ingénierie des prompts comme le processus étape par étape de création d'entrées qui déterminent la sortie à générer par un modèle de langage IA.

Des entrées de haute qualité donneront de meilleurs résultats. De même, des prompts mal définis conduiront à des réponses inexactes ou à des réponses qui pourraient avoir un impact négatif sur l'utilisateur. Après tout, "Un grand pouvoir implique de grandes responsabilités".

L'ingénierie des prompts s'applique à différentes applications, y compris les chatbots, les outils de génération de contenu, les outils de traduction linguistique et les assistants virtuels. Mais vous vous demandez peut-être comment la technologie IA génère ses réponses. Découvrons-le dans la section suivante.

## Comment fonctionnent les modèles de langage ?
Les modèles de langage IA tels que GPT-4 s'appuient sur des algorithmes d'apprentissage profond et le traitement du langage naturel (NLP) pour comprendre pleinement le langage humain. 

Tout cela est rendu possible grâce à un entraînement qui consiste en de grands ensembles de données. Ces ensembles de données incluent des articles, des livres, des journaux, des rapports, et ainsi de suite. Cela aide les modèles de langage à développer leurs capacités de compréhension du langage. Avec les données, le modèle est affiné de manière à lui permettre de répondre à des tâches particulières qui lui sont assignées.

Selon le modèle de langage, il existe deux méthodes d'apprentissage principales – l'apprentissage supervisé ou non supervisé. 

L'apprentissage supervisé est celui où le modèle utilise un ensemble de données étiquetées où les données sont déjà marquées avec les bonnes réponses. Dans l'apprentissage non supervisé, le modèle utilise des ensembles de données non étiquetées, ce qui signifie que le modèle doit analyser les données pour des réponses possibles et précises. Des modèles comme GPT-4 utilisent la technique d'apprentissage non supervisé pour donner des réponses.

Le modèle a la capacité de générer du texte en fonction du prompt donné. Ce processus est appelé modélisation du langage, et c'est la base de nombreuses applications de langage IA. En savoir plus sur [l'apprentissage supervisé vs non supervisé par IBM](https://www.ibm.com/cloud/blog/supervised-vs-unsupervised-learning).

À ce stade, vous devriez comprendre que la performance d'un modèle de langage IA dépend principalement de la qualité et de la quantité des données d'entraînement. L'entraînement du modèle avec des tonnes de données provenant de différentes sources aidera le modèle à comprendre le langage humain, y compris la grammaire, la syntaxe et la sémantique.

Notez que, indépendamment de la quantité de données utilisées pour entraîner ces modèles, il y aura toujours des défis lorsqu'il s'agit de comprendre le langage naturel. Après tout, il s'agit d'un être artificiel et comprendre des choses comme le sarcasme, l'ironie ou les sentiments humains peut être difficile pour un modèle IA à interpréter.

Maintenant que nous avons une compréhension de la façon dont le modèle de langage IA fonctionne, regardons les différentes catégories de prompts qui sont disponibles pour nous aider à communiquer avec les modèles.  

## Quelles sont les catégories de prompts ?
Vous pouvez utiliser des prompts pour assurer une communication fluide avec les modèles de langage IA. La première étape pour écrire des prompts de qualité est de comprendre leurs différentes classifications afin de pouvoir facilement structurer les prompts avec une réponse cible donnée à l'esprit. 

Parmi les principales catégories de prompts, on trouve :

1. **Prompts de recherche d'informations** - Ces prompts sont spécifiquement conçus pour recueillir des informations. Les prompts répondent principalement aux questions **Quoi** et **Comment**. Exemples de tels prompts : "Quels sont les attractions touristiques les plus populaires au Kenya ?", "Comment me préparer pour un entretien d'embauche ?"
2. **Prompts basés sur des instructions** - Ceux-ci sont utilisés pour donner des instructions au modèle afin d'effectuer une tâche spécifique. Un bon exemple de tels prompts est l'utilisation de Siri, Alexa ou Google Assistant. Par exemple, un prompt d'instruction pourrait être "Appeler maman", ou "Jouer le dernier épisode de mon émission de télévision préférée." 
3. **Prompts fournissant un contexte** - Comme le suggère le nom, ces prompts fournissent des informations à l'IA pour l'aider à mieux comprendre ce dont l'utilisateur a besoin comme réponse. Par exemple, si vous planifiez une fête et avez besoin d'idées de décoration et d'activités pour les participants, vous pouvez structurer votre prompt comme suit : "Je planifie une fête pour mon enfant, quelles sont quelques idées de décoration et activités que les participants pourraient faire pour la rendre agréable et mémorable ?"
4. **Prompts comparatifs** - Ceux-ci sont utilisés pour comparer ou évaluer différentes options données au modèle pour aider l'utilisateur à prendre une décision appropriée. Par exemple : "Quels sont les points forts et les points faibles de l'option A par rapport à l'option B ?"
5. **Prompts de recherche d'opinion** - Ceux-ci sont conçus pour obtenir l'opinion de l'IA sur un sujet donné. Par exemple : "Que se passerait-il si nous pouvions voyager dans le temps ?"
6. **Prompts réflexifs** - Ces prompts sont conçus pour aider les individus à acquérir une compréhension plus profonde d'eux-mêmes, de leurs croyances et de leurs actions. Ils ressemblent davantage à des prompts d'encouragement/croissance personnelle basés sur un sujet ou une expérience personnelle. Vous pourriez être amené à donner au modèle un peu d'informations avant d'obtenir une réponse souhaitable.
7. **Prompts basés sur des rôles** - Ces prompts fournissent des réponses en encadrant la demande de l'utilisateur dans un rôle spécifique. C'est la catégorie de prompts la plus couramment utilisée. En donnant un rôle à l'IA, elle fournit des réponses basées sur le rôle donné. 
Un truc qui a fonctionné pour cette catégorie particulière est l'utilisation du **cadre des 5 W**, c'est-à-dire : 

* Qui - Assigne le rôle que vous souhaitez que le modèle joue. Un rôle comme enseignant, développeur, chef, etc.
* Quoi - Fait référence à l'action que vous souhaitez que le modèle effectue.
* Quand - Votre calendrier souhaité pour accomplir une tâche particulière.
* Où - Fait référence à l'emplacement ou au contexte d'un prompt particulier.
* Pourquoi - Fait référence aux raisons, motivations ou objectifs d'un prompt particulier.

Un exemple de prompt basé sur un rôle est :
```
En tant que tuteur en codage, votre rôle est de créer des plans d'étude personnalisés pour aider les individus à apprendre à coder. Vos responsabilités incluront la compréhension des objectifs, de l'engagement en temps et des ressources d'apprentissage préférées de chaque étudiant, et l'utilisation de ces informations pour développer un plan d'étude complet avec des calendriers clairs et des liens vers des ressources pertinentes. Vous devriez être capable d'adapter votre style d'enseignement pour répondre aux besoins individuels de chaque étudiant et fournir un soutien et des conseils continus tout au long du processus d'apprentissage. Votre objectif ultime sera d'aider chaque étudiant à développer les compétences et les connaissances dont il a besoin pour atteindre ses objectifs de codage.
``` 
Ce prompt devrait également inclure ce que vous avez l'intention d'apprendre, la période d'apprentissage prévue et votre objectif d'apprentissage. N'oubliez pas que plus vous donnez de détails, plus les résultats seront adaptés.

**NOTE :** Si vous manquez de connaissances préalables sur ce dont vous avez besoin d'aide, vous ne devriez pas vous fier entièrement à la réponse que vous obtenez du modèle. Assurez-vous de vérifier avec d'autres sources si vous doutez des réponses du modèle, car le modèle n'est pas toujours correct.

## Principes de l'ingénierie efficace des prompts
Maintenant que nous avons couvert les différentes catégories de prompts, regardons comment vous pouvez créer de bons prompts. Pour vous aider à mieux comprendre, nous passerons en revue différents cadres d'ingénierie des prompts qui optimisent les réponses que nous obtenons en fournissant des requêtes claires destinées au NLP. 

Vous devriez garder les points suivants à l'esprit lors de la création de prompts :

* **Clarté** – Dans tout contexte de communication, la clarté est très importante. Les mêmes principes s'appliquent à l'ingénierie des prompts. Si vous voulez créer un bon prompt, il est important d'être clair sur ce que vous voulez. Un bon prompt aide l'IA à fournir des réponses plus précises.

* **Fournir un contexte et des exemples** – Cela implique de fournir des informations supplémentaires qui peuvent aider l'IA à mieux comprendre ce que le prompt est censé accomplir. En faisant cela, vous augmentez les chances d'obtenir des réponses plus précises. 

* **Définir des limitations et des contraintes** – Cela implique de fixer des limites dans lesquelles l'IA doit opérer. Cela augmente les chances d'obtenir la réponse souhaitée et évite les informations indésirables/irrélevantes.

* **Décomposer les requêtes** – Décomposer les requêtes en blocs plus petits et plus faciles à gérer facilitera le traitement des informations par l'IA. Cela aidera le modèle à comprendre chaque requête et à produire de meilleures réponses.

* **Itérer et reformuler** – Dans certains cas, après avoir donné une requête à l'IA, vous pourriez ne pas être satisfait de la réponse obtenue. Dans de tels cas, vous pouvez reformuler votre prompt et également fournir plus de contexte pour de meilleurs résultats.

* **Prioriser les informations importantes** – C'est là que vous mettez en évidence les informations les plus importantes dans le prompt. En faisant cela, vous dites à l'IA de se concentrer sur la fourniture de réponses pertinentes par rapport aux informations mises en évidence.

* **Utiliser des questions à choix multiples** – Dans une situation où vous êtes bloqué avec le choix parmi plusieurs options, vous pouvez fournir à l'IA différentes options à utiliser pour gagner du temps.

* **Demander une explication étape par étape** – Supposons que vous ayez besoin d'informations détaillées ou d'une décomposition d'un sujet complexe. Vous pouvez structurer votre prompt de manière à ce qu'il instruise l'IA de donner des réponses de manière plus approfondie en décomposant chaque étape.

* **Encourager la pensée critique** – Cela peut être utile lorsque vous vous appuyez sur des informations comme un conseil de l'IA. En encourageant l'IA à penser de manière critique, vous augmentez les chances d'obtenir une réponse basée sur une logique réaliste.

* **Vérifier l'exactitude de la réponse générée** – Enfin, mais non des moindres, **il est toujours important de vérifier les réponses générées par l'IA**. Cela implique de s'assurer que les informations sont exactes et à jour. En faisant cela, vous êtes en mesure de vous assurer que vous prenez une décision éclairée basée sur la réponse générée.

## Exemple pratique d'un prompt
Ayant discuté des différentes catégories de prompts et des principes pour une écriture efficace de prompts, examinons de plus près comment appliquer ces concepts dans un cadre réel. 

Pour tirer pleinement parti de ce que nous avons couvert jusqu'à présent, nous examinerons quelques exemples pratiques, aborderons certains problèmes courants de réponse de l'IA et jetterons également un coup d'œil à la manière dont l'IA est utilisée dans différents secteurs.

Je sais que formuler une bonne question n'est pas facile, mais croyez-moi lorsque je dis que j'ai été là. Le processus devient plus facile lorsque vous apprenez à créer des prompts appropriés. 

Par exemple, supposons que vous souhaitez commencer à apprendre à coder avec des technologies front-end, et que vous êtes confus et ne savez pas par où commencer. Au lieu de poser une question ouverte comme : "Où puis-je apprendre le développement front-end ?", vous pouvez utiliser un prompt plus spécifique et ciblé comme : 

![crafting-prompts](https://www.freecodecamp.org/news/content/images/2023/04/crafting-prompts.png)

Comme vous pouvez le voir dans l'image ci-dessus, voici le prompt que j'ai donné :

> "En ce qui concerne l'apprentissage du développement web front-end en ligne, quelles sont les différences entre les diverses plateformes d'éducation au codage en termes de contenu de programme, de ressources d'apprentissage et de soutien communautaire ? Par exemple, quelle plateforme propose des cours plus complets et à jour en HTML, CSS et JavaScript, et lesquelles ont une communauté plus active et engagée pour soutenir les apprenants dans leur parcours de développement front-end ?"

L'IA a fourni une réponse raisonnablement détaillée et informative basée sur les informations que j'ai fournies.

Le bon côté de ce prompt est qu'il est applicable dans différents secteurs. Nous voyons de plus en plus différentes applications de l'IA dans des domaines comme le divertissement, la finance, le droit, la médecine, l'éducation, et ainsi de suite.

Parmi ces domaines, le domaine du divertissement est l'un des plus courants où l'IA a été utilisée. Nous avons vu des gens utiliser l'IA pour créer du contenu YouTube à partir de zéro. Cela implique une série d'étapes qui inclut la création d'une longue conversation entre vous et l'IA dans un scénario où l'IA se voit attribuer un rôle et vous suivez ses instructions. 

Autant nous pouvons nous appuyer sur l'IA pour accomplir une tâche spécifique, il est également important de considérer la tâche que nous assignons à l'IA et si elle est appropriée. Ces modèles de langage excellent principalement dans les tâches qui nécessitent le traitement de grandes quantités de données, ce qui les aide à identifier des motifs de réponse uniques. 

En plus de cela, il est également important de choisir un modèle approprié pour une tâche spécifique, car différents modèles sont formés pour gérer différentes tâches.

## Pièges et limitations de l'IA

Malgré toutes les avancées que l'IA a réalisées ces dernières années, nous pouvons convenir qu'elles ne sont pas non plus parfaites.

L'une des principales préoccupations soulignées par de multiples sources est que les modèles d'IA ont un potentiel de partialité. 

Comment cela est-il possible ? Eh bien, les algorithmes de machine learning s'appuient sur des données humaines pour faire des prédictions. Dans les cas où les données fournies au modèle sont biaisées, les réponses résultantes seraient également biaisées. Il est donc important d'évaluer soigneusement les données d'entraînement pour toute forme de partialité et de faire des ajustements à un stade précoce. 

De plus, bien que nous puissions faire confiance à l'IA pour automatiser certaines tâches, les résultats de leurs découvertes ne sont pas toujours exacts. Si l'IA n'est pas restreinte par des paramètres bien définis, elle peut aller au-delà des capacités de l'utilisateur. 

Pour éviter ces circonstances, il est toujours bon de prévoir une supervision humaine pour surveiller en continu le modèle et également aider à identifier les erreurs du modèle.

Un autre domaine courant où l'IA a du mal est la compréhension du langage complexe et la relation avec la façon dont un humain réel se sentirait dans différentes situations. Parce qu'elle ne peut pas "ressentir", beaucoup de ses décisions liées au comportement humain normal ne sont pas exactes et ne peuvent pas être entièrement fiables.

Et enfin, si les données d'entraînement sont incomplètes, le modèle peut ne pas être en mesure de donner les réponses les plus précises. Lorsque cela se produit, un modèle peut opter pour générer des idées basées sur ce qu'il pense que l'utilisateur pourrait demander. Cela signifie que le modèle a du mal car il ne dispose pas de suffisamment de données précises pour générer une bonne réponse.

### Problèmes actuels avec les réponses de l'IA

La vérité malheureuse à ce stade est que les réponses générées par l'IA ne sont pas toujours correctes. J'ai été victime de cela. Mais heureusement pour moi, j'étais conscient de l'erreur et j'ai pu la corriger. 

Une autre chose à noter est que si vous donnez à une IA des informations alternatives qui ne sont pas une réponse correcte, l'IA essaiera toujours d'être d'accord avec vous même si vous avez tort. C'est pourquoi il est bon de **s'assurer que vous avez une idée de ce que vous demandez à l'IA**. Dans un cas où l'IA vous donne une réponse incorrecte, vous pouvez toujours essayer de reformuler votre prompt en fournissant plus de contexte.

## Conclusion 
Il semble clair que la technologie de l'IA jouera un rôle très important dans nos vies à l'avenir. Cette technologie continuera à révolutionner la façon dont nous menons nos routines quotidiennes au travail, à la maison ou à l'école. 

Pour en tirer pleinement parti, nous devons nous assurer que nous sommes capables de communiquer efficacement avec ces systèmes. Et c'est là que l'ingénierie des prompts entre en jeu. En comprenant comment créer un bon prompt, nous pouvons améliorer l'interaction entre les humains et les machines.

Alors que nous essayons de nous appuyer sur les informations fournies par l'IA, il est essentiel de considérer les implications possibles qu'elles peuvent apporter à nos vies. Un problème majeur est que les systèmes d'IA sont souvent biaisés, ce qui pourrait conduire à des résultats discriminatoires. 

Mais quelle que soit la situation, il semble que l'IA soit là pour rester. Donc, plus tôt vous apprendrez à communiquer avec elle, mieux ce sera. Ne restez pas à l'écart de la fête 😊.