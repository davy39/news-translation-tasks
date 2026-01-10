---
title: Comment construire le chatbot IA ultime en suivant ces étapes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-26T12:58:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-the-ultimate-ai-chatbot-by-following-these-steps-e0abe77a2b20
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mDFiewb7C0vXSWvbZ6VodQ.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: bots
  slug: bots
- name: '#chatbots'
  slug: chatbots
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment construire le chatbot IA ultime en suivant ces étapes
seo_desc: 'By Paul Pinard

  A quick guide that helps you avoid common pitfalls


  Building a bot is a rewarding experience: creating your own artificial intelligence
  is amazing!

  However, it can be a challenge, and there are mistakes to avoid. In this piece,
  we’re g...'
---

Par Paul Pinard

#### Un guide rapide pour éviter les pièges courants

![Image](https://cdn-media-1.freecodecamp.org/images/Na8oklNT0d3X7Nix1l0-mfV3mGJUv6BjNiKx)

Construire un bot est une expérience enrichissante : créer votre propre intelligence artificielle est incroyable !

Cependant, cela peut être un défi, et il y a des erreurs à éviter. Dans cet article, nous allons vous guider à travers les erreurs les plus courantes ou dommageables que commettent les nouveaux constructeurs de bots à chaque phase de la construction : conception, formation, construction, connexion, expérience utilisateur et maintenance. C'est parti !

### **Conception**

Construire un bot ne commence pas à la première ligne de code. Cela commence bien plus tôt, lors de la conception.

Lors de cette première étape, il est important de définir le cas d'utilisation de votre chatbot. Quel est le problème que vous voulez résoudre ? Quels sont vos besoins commerciaux ?

Nous voyons souvent des gens dire « Je veux un bot qui fait ceci », mais lorsque nous creusons plus profondément, nous réalisons qu'un bot différent résoudrait en fait le problème beaucoup plus efficacement. Si vous voulez construire un chatbot qui gère les questions des clients sur les politiques de retour, mais que vous réalisez plus tard que ces requêtes représentent moins de 2 % de votre volume global, vous pourriez vouloir passer à un autre sujet. Commencez donc par le problème commercial et construisez à partir de là.

Maintenant que vous avez établi le besoin commercial réel, comment le flux de conversation du bot doit-il se dérouler pour le résoudre ? Ce que nous faisons habituellement, c'est prendre un tableau de dessin et dessiner tous les flux de conversation, du début à la fin. Modéliser toutes les possibilités vous permet de vous assurer que chaque sujet est couvert et donne au développeur un bon aperçu de ce qui doit être fait. C'est aussi la première étape de la création de votre expérience utilisateur, dont nous parlerons plus tard. Pour l'instant, gardez simplement à l'esprit que chaque conversation doit comporter environ 3 ou 4 échanges, pas plus.

Lors de cette étape, n'oubliez pas votre public : qui sont les utilisateurs finaux qui parleront à votre bot ? Vous devez créer quelque chose qui fonctionne pour eux.

N'oubliez pas d'inclure les conversations informelles dans votre conception. Tous les chatbots sont censés comprendre et répondre à un certain nombre de sujets sans rapport avec leur mission : blagues, questions sur la météo, « comment ça va », et même des remarques comme « veux-tu m'épouser » ou d'autres sujets hors-sujet. Assurez-vous de prévoir ceux-ci si vous voulez que l'utilisateur soit satisfait de l'expérience. Mais ne vous inquiétez pas, nous fournissons des compétences de conversation pré-entraînées sur [SAP Conversational AI](https://cai.tools.sap/?utm_source=medium&utm_medium=article&utm_campaign=UA2019).

**Ce qu'il ne faut pas faire lors de la construction d'un bot :**

> **1. Le considérer comme une étape non importante**

> **2. Partir de ce que vous voulez et non de ce dont vous avez besoin**

> **3. Comprendre incorrectement qui seront les utilisateurs finaux du bot et concevoir une expérience qu'ils n'apprécieront pas**

> **4. Ne pas inclure les conversations informelles et autres questions couramment posées**

### **Formation**

La formation du bot est le facteur le plus important pour déterminer ses performances. Une mauvaise formation conduira inévitablement à un chatbot peu performant et à des utilisateurs frustrés.

Sur la base du flux que vous avez créé lors de la conception, la formation consiste à créer des intentions et à les remplir avec des expressions. Si vous n'êtes pas à l'aise avec le concept d'intentions et d'expressions, [cet article](https://cai.tools.sap/docs/concepts/intent) devrait vous aider. Mais voici quelques éléments qui font une bonne formation.

Le nombre d'expressions dans chaque intention est crucial. Cinq ne suffisent pas, vous devriez en avoir 50+. SAP Conversational AI fonctionne très bien avec de petits ensembles de données, mais nous avons encore besoin d'un peu d'information. Ces phrases doivent être variées et doivent provenir des utilisateurs finaux. N'entraînez jamais votre bot uniquement avec l'équipe de développement et de projet : ils connaissent trop bien le jargon technique pour représenter avec précision les personnes qui utiliseront réellement le bot.

![Image](https://cdn-media-1.freecodecamp.org/images/-Yycb-a6fPKt0xLNWMfceZVVoZYgLeJ33k2a)

L'étiquetage des entités a également quelques règles. Les entités sont des mots-clés que vous devez détecter dans une phrase pour extraire des informations (le point clé ici étant « extraire des informations »). Vous n'avez pas besoin d'étiqueter chaque nom, adjectif ou mot par phrase juste parce que vous pouvez le faire ! Le but des entités est d'extraire des informations pertinentes que vous pouvez utiliser dans votre code. N'étiquetez que celles-ci.

Cependant, évitez d'avoir des phrases qui ne sont composées que d'un seul mot qui est une entité (par exemple, « Paris » comme phrase complète). Cette entité peut être détectée par n'importe quelle intention, ce qui peut conduire à des problèmes de détection.

![Image](https://cdn-media-1.freecodecamp.org/images/MZHlf-J9SBKS9FC3zq8JzZGTgbxvBgpdBSRw)

Une bonne pratique courante pour les grands bots est d'utiliser les intentions et les entités de pair. Il est préférable de créer une intention globale et d'utiliser des entités pour spécifier la demande de l'utilisateur, plutôt que de créer des intentions très spécifiques que le classificateur confondra car elles se chevauchent.

![Image](https://cdn-media-1.freecodecamp.org/images/EQsnPzNr1wkFVldSUSEuYeXKpbaAXO5840Ek)
_Ici, l'intention globale est la résolution de problèmes, mais les entités détectent quel produit ne fonctionne pas._

**Ce qu'il ne faut pas faire lors de la construction d'un bot :**

> **5. Avoir moins de 50 expressions par intention**

> **6. Entraîner votre bot avec des personnes qui ne sont pas les utilisateurs finaux**

> **7. Étiqueter chaque mot dans une phrase comme une entité**

> **8. Étiqueter des mots comme des entités lorsque vous n'utilisez pas les informations extraites**

> **9. Avoir des expressions qui ne sont que des entités (c'est-à-dire « Paris »)**

> **10. Créer des intentions très spécifiques au lieu d'utiliser des entités pour comprendre le sujet**

### **Construction**

Construire un bot est souvent supposé ne consister qu'à construire le flux de conversation. C'est la partie amusante ! C'est lorsque tout prend vie. Cependant, cela peut être un processus effrayant.

La première chose à comprendre est qu'il est acceptable d'utiliser plusieurs compétences pour accomplir une tâche. Une compétence n'a pas à égaler un processus complet. Cela peut être une bonne solution de créer une « méga-compétence » dont le travail est de dispatcher l'entrée de l'utilisateur à la compétence correcte.

![Image](https://cdn-media-1.freecodecamp.org/images/AziHdCyg92iqRr0HQ8RtCK0DrlIpJs-Nd9vB)
_Dans notre exemple de résolution de problèmes (ts), une méga-compétence redirige vers les différentes compétences qui gèrent les procédures spécifiques_

C'est aussi une solution si vous avez des compétences avec des déclencheurs qui se chevauchent. Et si quelque chose ne fonctionne pas, assurez-vous d'utiliser les logs dans la console de débogage pour comprendre d'où vient le problème.

![Image](https://cdn-media-1.freecodecamp.org/images/ZjjNiSVhAlfy9E7Oq30-EFZsQdQyXhFLNJ07)

**Ce qu'il ne faut pas faire lors de la construction d'un bot :**

> **11. Insister sur la philosophie « une compétence = une tâche »**

> **12. Ne pas utiliser les outils de débogage de la plateforme**

### **Connexion et Expérience Utilisateur**

Lors de la connexion de votre bot, vous devez décider où il sera disponible pour vos utilisateurs, et donc travailler sur une expérience utilisateur. Il y a quelques choses à savoir pour fournir une UX agréable, la première étant : votre bot doit être beau. Un bot attrayant avec beaucoup de boutons, d'éléments graphiques, de photos HD, de couleurs et une bonne personnalité fait toute la différence.

Mais comment obtenir cela ?

Tout d'abord, pensez à votre public lorsque vous choisissez votre canal. Si vous ciblez les 50 à 65 ans, vous ne allez probablement pas mettre votre bot sur Kik ! N'essayez pas d'attirer votre public sur un canal qu'ils n'utilisent pas, même si c'est mieux. Au lieu de cela, intégrez le bot là où vos utilisateurs se trouvent déjà.

Ensuite, gardez à l'esprit qu'un chatbot est une interface conversationnelle. Les conversations sont des échanges interactifs ; par conséquent, votre bot ne doit jamais répondre avec de longs blocs de texte (plus de 60 caractères est déjà long).

Séparez les réponses en différents messages, utilisez des images, des boutons, des listes et d'autres composants UX en fonction du canal que vous utilisez pour le rendre vivant. Il est également important de créer une conversation gratifiante : votre bot n'est pas un agent du FBI. Personne ne veut répondre à 20 questions avant d'obtenir une réponse. Au lieu de cela, créez votre flux et votre UX pour fournir une réponse tous les 3 ou 4 échanges afin de garder l'utilisateur engagé.

Puisque nous fournissons une puissante API de traitement du langage naturel avec notre outil de construction de bots, nos utilisateurs tendent à vouloir tout faire par le langage. Bien que ce soit admirable, nous conseillons toujours de diversifier : offrez des cartes, des boutons et d'autres éléments graphiques pour l'interactivité et la facilité d'utilisation, mais assurez-vous que tout le flux peut être fait en utilisant le langage naturel. C'est alors que les utilisateurs savent que votre bot est le vrai.

![Image](https://cdn-media-1.freecodecamp.org/images/rl5eyf2CDstgMMB-NdSjzDt5tjYWSRNiDUlO)

Donner une personnalité à votre chatbot est essentiel, cependant, vous devez trouver le bon équilibre. Nous conseillons toujours de laisser vos utilisateurs savoir qu'ils parlent à un bot. C'est simplement de la gestion des attentes !

Un humain qui parle à un autre humain va s'attendre au plus haut niveau d'interaction, alors qu'un humain qui parle à un bot va savoir qu'il ne peut pas demander n'importe quoi. Cependant, ne le rendez pas trop robotique : donnez-lui un nom, une image, et utilisez des smileys et un ton de voix pour le rendre mémorable.

**Ce qu'il ne faut pas faire lors de la construction d'un bot :**

> **13. Identifier incorrectement le canal que votre public utilise**

> **14. Créer des conversations où l'utilisateur doit répondre à 4+ questions pour obtenir une première réponse**

> **15. Envoyer des blocs de texte comme réponses (plus de 60 caractères est trop)**

> **16. Écarter tous les éléments UX (boutons, cartes, listes, etc.) juste pour se concentrer sur le texte**

> **17. Faire passer votre bot pour une personne humaine**

> **18. Ne pas donner à votre bot une personnalité qui attire votre public**

### **Maintenance**

Une fois votre bot en production, votre travail n'est pas terminé ! Maintenir votre bot est une partie essentielle de son succès à long terme. Cela consiste principalement à affiner votre formation et à surveiller ce que vos utilisateurs disent pour adapter votre flux ou créer de nouveaux cas d'utilisation.

Lors de la formation, procédez avec prudence. Bien qu'il soit important d'ajouter de nouvelles phrases d'utilisateurs via le flux de logs, vous ne voulez pas déséquilibrer la formation que vous avez créée et qui fonctionne déjà. Ne submergez pas vos intentions en ajoutant toutes les nouvelles expressions, ajoutez seulement ce qui est nécessaire. Gardez à l'esprit que toutes les intentions doivent être formées de la même manière ! Si une intention a 100 expressions et l'autre en a 10, ce n'est pas bon. Par conséquent, vérifiez régulièrement lors de l'assignation de nouvelles expressions. Nos analyses de formation sont vos meilleures amies lorsqu'il s'agit d'améliorer vos données de formation !

Enfin, votre flux de logs est l'endroit où vous pouvez voir ce dont parlent les utilisateurs. Voyez-vous un sujet que vos utilisateurs soulèvent fréquemment et que votre bot ne gère pas encore ? Pourquoi ne pas l'intégrer dans votre flux ? C'est la meilleure façon de montrer à votre communauté que le bot qu'ils utilisent s'efforce toujours de fournir une grande expérience.

**Ce qu'il ne faut pas faire lors de la construction d'un bot :**

> **19. Penser que une fois le bot en production, votre travail est terminé**

> **20. Surcharger les intentions avec de nouvelles expressions d'utilisateurs et gâcher votre formation existante**

> **21. Créer des inégalités dans la taille de vos intentions**

> **22. Ne pas prêter attention à la manière dont les gens utilisent votre bot**

Avec tout cela en tête, vous êtes parfaitement prêt à construire un premier bot génial ! Si vous êtes prêt à aller plus loin, ce [tutoriel pas à pas](https://medium.freecodecamp.org/how-to-build-your-first-chatbot-with-the-sap-conversational-ai-9a1a2bd44e3c) peut vous guider à travers le processus réel pour construire un chatbot génial qui raconte des blagues !

Bonne construction !

_Publié à l'origine sur [SAP Conversational AI Blog](https://cai.tools.sap/blog/building-a-bot-22-rules/)._