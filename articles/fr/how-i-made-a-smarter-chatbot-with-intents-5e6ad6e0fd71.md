---
title: Comment j'ai rendu mon ChatBot plus intelligent en l'aidant à comprendre l'intention
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T17:37:18.000Z'
originalURL: https://freecodecamp.org/news/how-i-made-a-smarter-chatbot-with-intents-5e6ad6e0fd71
coverImage: https://cdn-media-1.freecodecamp.org/images/0*e-7HD__g3J0-Ix8h
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: '#chatbots'
  slug: chatbots
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment j'ai rendu mon ChatBot plus intelligent en l'aidant à comprendre
  l'intention
seo_desc: 'By P. Daniel Tyreus

  Using deep learning tools to better understand conversations about seasonal allergies

  I’ve been working on a chatbot to help understand seasonal allergies as a side project
  for quite a while. This time every year, my allergies fla...'
---

Par P. Daniel Tyreus

Utilisation d'outils d'apprentissage profond pour mieux comprendre les conversations sur les allergies saisonnières

Je travaille sur un chatbot pour aider à comprendre les allergies saisonnières en tant que projet parallèle depuis assez longtemps. À cette période chaque année, mes allergies s'aggravent et ma motivation pour améliorer [Hayfever](https://hayfever.io) connaît également un regain.

Au début de ce printemps, j'ai pris le temps de revoir à quel point mon chatbot communiquait bien avec les utilisateurs. Les résultats étaient humbles, pour le moins. J'ai donc étudié l'amélioration des performances de mon chatbot en intégrant un système moderne de compréhension du langage naturel basé sur l'apprentissage profond. Cet article discute de ce qui n'allait pas avec mes premières approches et de la manière dont je l'ai corrigé.

### Première tentative : Arbres de dialogue

J'ai construit l'« intelligence » derrière la première version du chatbot Hayfever en utilisant un mécanisme connu sous le nom d'[arbre de dialogue](https://en.wikipedia.org/wiki/Dialog_tree). Toute personne ayant déjà joué à un jeu vidéo de rôle a expérimenté un arbre de dialogue. Dans sa forme classique, un personnage du jeu prononce un dialogue et le joueur a le choix entre plusieurs réponses.

Un ancêtre encore plus primitif est le système de réponse vocale interactive ([IVR](https://en.wikipedia.org/wiki/Interactive_voice_response)). La plupart d'entre nous ont probablement eu le désagrément d'interagir avec un IVR en appelant la ligne de support client de notre banque. Ces mécanismes sont faciles à programmer et **fonctionnent de manière adéquate lorsque le domaine des réponses possibles est limité aux choix présentés**.

Dans le jeu vidéo, vous ne pouvez sélectionner que parmi les choix à l'écran, et avec l'IVR, vous ne pouvez appuyer que sur les numéros en fonction des choix donnés.

Avec les chatbots, les réponses possibles ne sont pas du tout limitées. Un utilisateur peut taper ce qu'il a en tête. Mais lorsque j'ai initialement implémenté le chatbot Hayfever dans Facebook Messenger, je n'avais pas accès à la technologie pour analyser l'entrée de manière sophistiquée. J'ai donc utilisé la fonctionnalité de « réponse rapide » pour essayer de forcer la conversation dans des directions spécifiques, un peu comme un arbre de dialogue.

![Image](https://cdn-media-1.freecodecamp.org/images/Cuz5hCGmyBUZOwpXSc-phjZiok6MAddfovv8)
_Tentative de forcer la direction de la conversation en utilisant des boutons de réponse rapide._

### Deuxième essai : Graphes de conversation

Après avoir observé le chatbot en action, j'ai compris presque immédiatement que cette approche ne fonctionnerait pas. Même si les utilisateurs se voyaient présenter quelques réponses rapides, rien ne les empêchait de taper quelque chose de totalement différent.

Dans la deuxième itération, j'ai décidé qu'une structure d'arbre était trop rigide et que je devais modéliser la conversation sous forme de graphe orienté. Je n'ai pas trouvé de framework qui répondait exactement à mes besoins. J'ai donc écrit mon propre moteur de dialogue basé sur des graphes appelé [conversation-kit](https://github.com/pdtyreus/conversation-kit).

Un **graphe orienté** présente certains avantages par rapport à une structure d'arbre, dans ce cas, car il **peut permettre à la conversation de se bifurquer et de s'écouler plus naturellement**. Sans entrer trop dans les détails, les sommets du graphe représentent des déclarations ou des questions du chatbot. Les arêtes représentent les réponses possibles de l'utilisateur. Ainsi, la conversation passe d'un sommet à l'autre le long des arêtes qui correspondent à la réponse de l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/JZ6PrSRMJM5JI5vwQQtZlFaFf4ShBNLxTCgS)
_La conversation du chatbot visualisée sous forme de graphe. Chaque sommet représente quelque chose que le bot peut dire, et chaque arête représente une déclaration possible suivante dans la conversation._

Tant que l'utilisateur ne s'éloignait pas trop de l'ensemble des réponses définies par les arêtes du graphe, cela fonctionnait assez bien. Par exemple, ci-dessous se trouve une discussion que j'ai eue avec Hayfever sur Facebook Messenger.

![Image](https://cdn-media-1.freecodecamp.org/images/pBYi8RR-PeMyB-iPPghx9SW76MQKrdaOji22)
_Une discussion réussie avec Hayfever sur Facebook Messenger en utilisant le modèle de conversation basé sur des graphes._

Puisque j'ai programmé le modèle, je savais essentiellement ce que je pouvais dire pour obtenir la réponse souhaitée. Les autres utilisateurs n'auraient pas cette connaissance. Donc, bien que cette version était meilleure, elle souffrait encore de sérieux inconvénients.

Premièrement, si la réponse d'un utilisateur ne correspondait à aucune arête, le bot se retrouvait coincé dans une boucle disant qu'il ne comprenait pas. Deuxièmement, l'algorithme que j'ai écrit pour faire correspondre les réponses aux arêtes était **vraiment primitif et comprenait souvent mal** ce que l'utilisateur disait. Enfin, si l'utilisateur voulait changer de sujet au milieu d'une conversation, il ou elle devrait essentiellement connaître une phrase déclenchante comme « help » pour réinitialiser la position dans le graphe.

Ci-dessous se trouvent quelques exemples des conversations non naturelles et frustrantes qui en résultent.

![Image](https://cdn-media-1.freecodecamp.org/images/sabbwOL8d-cdfsD--Yjy4qHUKIyuzC0HAPO2)
_Hayfever ne comprenant clairement pas un utilisateur, entraînant une conversation non naturelle et frustrante._

![Image](https://cdn-media-1.freecodecamp.org/images/WAKTt3UY73ysHlqIMlByydGxOBQSf-gabcxa)
_Un utilisateur faisant une demande naturelle que Hayfever ne pouvait pas comprendre car elle ne correspondait pas à une arête existante dans le graphe._

Dans les exemples ci-dessus, il est clair que mon chatbot ne comprenait pas du tout ce que l'utilisateur essayait de transmettre. En d'autres termes, **il ne comprenait pas l'intention de chaque déclaration**.

Les humains sont incroyablement doués pour comprendre les intentions subtiles dans une conversation orale. La plupart des gens combinent sans effort les indices des expressions faciales, du langage corporel et de l'intonation pour évaluer l'intention. En plus de cela, nous incorporons la connaissance de la personne à qui nous parlons, les détails contextuels des conversations précédentes et les références culturelles possibles pour affiner davantage le sens de ce qu'une personne nous dit.

Les technologies modernes d'intelligence artificielle sont loin d'être aussi bonnes que les humains dans ce domaine. Mais **les avancées en apprentissage profond** au cours des dernières années ont **considérablement amélioré la capacité d'un ordinateur à discerner l'intention** à partir de textes parlés ou écrits. À tout le moins, l'état de l'art est bien, bien meilleur que la technologie primitive que j'utilisais pour faire correspondre les réponses aux arêtes.

### Troisième essai : Comprendre l'intention

Après avoir étudié les interactions de mon chatbot avec les utilisateurs, j'ai réalisé que j'avais besoin d'une stratégie plus sophistiquée. J'avais vraiment besoin d'un moyen de mieux comprendre l'intention d'un utilisateur.

Ma première expérience avec l'intention était lorsque je programmais une compétence personnalisée pour le service Alexa d'Amazon. Le service Alexa convertit les mots que vous prononcez à un appareil comme un Echo en texte écrit. Il vérifie ensuite si les mots correspondent à l'une des intentions intégrées comme « help » ou « exit ».

En tant que développeur, vous pouvez également définir vos propres intentions en définissant des **énoncés** qui correspondent à la même **intention**. Par exemple, les énoncés « quelles sont les conditions aujourd'hui ? », « combien de pollen y a-t-il dans l'air ? » et « les conditions d'allergie sont-elles mauvaises ? » pourraient tous être l'expression par l'utilisateur de leur intention de demander un rapport sur les conditions. L'avantage de cela est que vous n'avez pas à définir chaque variation d'un **énoncé** pour une **intention** donnée. L'algorithme de traitement est souvent suffisamment bon pour faire correspondre des **énoncés** similaires à la même **intention**.

Pour un développeur de chatbot, c'est génial. Au lieu de gérer la génération de réponses pour des centaines ou des milliers d'entrées différentes, je peux me concentrer sur la génération de réponses pour une poignée d'intentions prédéfinies.

Ma correspondance primitive par expression régulière était facile à coder moi-même. Mais la technologie de pointe derrière la conversion d'un énoncé en une intention est assez sophistiquée. Heureusement, il existe plusieurs fournisseurs bien connus qui offrent la compréhension du langage naturel en tant que service.

* Microsoft Cognitive Services Language Understanding ([LUIS](https://www.luis.ai/home))
* Amazon Web Services [Lex](https://aws.amazon.com/lex/)
* Google [Dialogflow](https://dialogflow.com/)
* Facebooks [wit.ai](https://wit.ai/)

Tous ces services se présentent comme des technologies de « deep learning avancé » pour « construire des interfaces conversationnelles ». Tous sont basés sur des API, ce qui signifie qu'ils peuvent être intégrés dans presque toutes les applications ayant une connexion à Internet. Et tous offrent un niveau gratuit à l'usage dont j'avais actuellement besoin.

Pour ce projet, j'ai choisi Dialogflow. J'ai trouvé l'interface utilisateur agréable, les API compréhensibles, et cela nécessitait presque aucun verrouillage par le fournisseur. Il comprenait également un module complémentaire amusant appelé [Small Talk](https://dialogflow.com/docs/small-talk) qui permettait facilement à mon bot de répondre à des conversations informelles comme « comment ça va ? » et « quel est ton nom ? ». Étrangement, j'ai remarqué dans les journaux que de nombreux utilisateurs aimaient échanger des politesses informelles avec mon bot.

### Utilisation de Dialogflow

La boucle d'application lors de l'utilisation d'un service NLU est en fait plus simple que ce que j'avais avant. Le bot est entièrement piloté par événements. Il attend une entrée de l'utilisateur via un webhook Facebook Messenger, transmet le texte à Dialogflow pour analyser l'intention, génère la réponse appropriée pour l'intention et envoie la réponse formatée à l'API Facebook Messenger.

![Image](https://cdn-media-1.freecodecamp.org/images/JmPRkmoeD3mjXA43CSC8ZDVyv-tgw3SFlMhS)

La mise à jour de Hayfever pour utiliser Dialogflow s'est relativement bien passée, avec quelques exceptions.

Premièrement, il semble que j'ai attrapé Dialogflow au milieu d'une migration de leur API V1 vers V2 et que la documentation n'avait pas tout à fait suivi. En recherchant sur StackOverflow et d'autres blogs, il y avait beaucoup d'informations obsolètes qui faisaient référence à l'API V1.

Deuxièmement, Hayfever est un bot Facebook Messenger. Le format JSON pour intégrer les réponses de Facebook Messenger dans l'API DialogFlow est assez mal documenté. Si j'avais choisi wit.ai de Facebook, je suis sûr que cette partie aurait été plus facile. Mais je veux que Hayfever fonctionne sur **toute plateforme de messagerie ainsi que sur les plateformes vocales à l'avenir**.

J'ai donc complètement découplé le traitement des intentions Dialogflow du formatage des réponses Messenger. Ainsi, le code Dialogflow ne sait pas que l'entrée provient de Messenger, et Messenger ne sait pas que Dialogflow analyse les intentions. Ce n'était pas la manière la plus facile de construire cela, mais c'est assez futuriste.

Le passage à l'NLU Dialogflow a immédiatement amélioré la qualité des conversations de Hayfever. **Le bot n'était plus dérouté par des variations subtiles dans les entrées attendues, il pouvait discuter avec les utilisateurs et il pouvait même deviner les intentions à partir d'entrées qu'il n'avait jamais vues auparavant**. Il reste encore beaucoup de formation et d'optimisation à faire, mais c'est clairement un pas dans la bonne direction.

### Conclusion

[Hayfever](https://hayfever.io/) est un chatbot conçu pour aider les utilisateurs à suivre et à comprendre les symptômes d'allergie. Les premières versions utilisaient des mécanismes primitifs d'arbres de dialogue et étaient assez mauvaises pour comprendre les conversations naturelles. L'intégration d'un service de compréhension du langage naturel (NLU) basé sur l'apprentissage profond comme Dialogflow a considérablement amélioré la capacité de Hayfever à converser avec les utilisateurs.

En gardant le traitement NLU séparé de l'entrée et de la sortie spécifiques à la plateforme, il n'y a eu presque aucune augmentation de la complexité du code et aucun verrouillage de la plateforme.

À l'avenir, j'espère rendre Hayfever disponible sur des appareils vocaux comme Amazon Alexa et Google Home, ainsi que sur des plateformes de messagerie supplémentaires comme Telegram. J'aimerais également essayer de combiner le NLU avec certains des outils de conversation basés sur des graphes que j'ai utilisés précédemment pour peut-être donner au chatbot une meilleure mémoire de ce qui s'est déjà passé dans la conversation.