---
title: Apprendre à contrôler GPT dans l'OpenAI Playground
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-12-08T17:15:34.000Z'
originalURL: https://freecodecamp.org/news/learn-to-control-gpt-in-openai-playground
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/pexels-levi-damasceno-571249.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: chatgpt
  slug: chatgpt
- name: 'LLM''s '
  slug: llms
- name: openai
  slug: openai
seo_title: Apprendre à contrôler GPT dans l'OpenAI Playground
seo_desc: "ChatGPT is the interface most people use to work with OpenAI's large language\
  \ model. But for someone who needs the versatility and power of programmatic access,\
  \ there's no replacement for OpenAI's API. \nThe API is the interface you can use\
  \ to connect..."
---

ChatGPT est l'interface que la plupart des gens utilisent pour travailler avec le grand modèle de langage d'OpenAI. Mais pour quelqu'un qui a besoin de la polyvalence et de la puissance de l'accès programmatique, rien ne remplace l'API d'OpenAI. 

L'API est l'interface que vous pouvez utiliser pour connecter le code de programmation s'exécutant sur votre propre PC avec les serveurs GPT d'OpenAI. 

Bien sûr, lors de l'utilisation de l'API, vous pouvez inclure des prompts en langage simple où vous demandez à GPT des réponses et du contenu généré. Mais vous pouvez également appliquer toute la puissance intégrée de ce code de programmation pour créer des opérations sophistiquées et automatisées qui impliquent GPT. 

Vous pourriez, par exemple, demander à ChatGPT d'écrire un article sur un sujet spécifique. Mais en utilisant l'API, vous pouvez lui demander d'écrire 100 articles sur les sujets listés dans un document texte et puis vous asseoir pendant que votre code fait tout le travail pour vous. 

Tout ce qui tire parti du code plutôt que d'effectuer des opérations manuelles est mille fois plus efficace lorsque vous ajoutez GPT à l'équation.

Le problème est que, comme toutes les API, comprendre la syntaxe et autres détails peut prendre du temps. Pour vous aider à surmonter cet obstacle, OpenAI a créé les outils visuels dans leur [Playground](https://platform.openai.com/playground). Voyons comment cela peut aider. 

Cet article est extrait de [mon livre Manning, The Complete Obsolete Guide to Generative AI](https://www.manning.com/books/the-complete-obsolete-guide-to-generative-ai?a_aid=bootstrap-it&a_bid=8c39744&a_bid=8c397448&chan=fcc_ai). 

## Qu'est-ce que le Playground ?

Le Playground, montré dans la figure ci-dessous, existait même avant ChatGPT, et c'est là que j'ai eu mes premières interactions avec GPT. Bien que gardez à l'esprit que, comme tout le reste dans le monde de l'IA, l'interface aura probablement changé au moins deux fois d'ici à ce que vous y accédiez. 

Nous allons utiliser le Playground tout au long de ce tutoriel pour apprendre à interagir avec GPT.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/gai-2-2.png)
_Interface du Playground d'OpenAI_

Vous accédez au [Playground](https://platform.openai.com/playground) depuis votre compte de connexion OpenAI. Plutôt que de profiter d'une conversation soutenue où les échanges ultérieurs sont informés par les prompts et les complétions précédents, lorsque l'option Chat est sélectionnée dans le menu déroulant en haut à gauche de l'écran, le champ de texte dans le Playground n'offre qu'un seul échange à la fois. Les modèles sur lesquels il est basé peuvent également être un peu plus anciens et moins raffinés que la version ChatGPT.

Mais il y a deux choses qui distinguent le Playground de ChatGPT. L'une est les contrôles de configuration affichés sur le côté droit de l'écran dans l'image ci-dessus. La seconde est la fonctionnalité _View code_ en haut à droite. Ce sont ces fonctionnalités qui font du Playground principalement un outil éducatif plutôt qu'une simple autre interface GPT.

## Comment accéder aux exemples de code Python

L'image ci-dessous montre une session typique du Playground où j'ai tapé un prompt puis cliqué sur le bouton "View code" avec l'option "Python" sélectionnée. On me montre un code fonctionnel qui, en supposant que vous ajouterez une clé API OpenAI valide à la ligne 4, peut être copié et exécuté depuis n'importe quel ordinateur connecté à Internet.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/gai-2-3-1.png)
_Outil View code du Playground avec du code Python_

Ne vous inquiétez pas des détails pour l'instant, mais prenez un moment pour parcourir les arguments qui sont inclus dans la méthode `openai.Completion.create()`. 

Le modèle actuellement sélectionné dans le champ Model sur le côté droit du Playground est là (`text-davinci-003`), tout comme mon prompt réel (`Explain the purpose of...`). En fait, chaque option de configuration que j'ai sélectionnée est là. 

En d'autres termes, je peux expérimenter avec n'importe quelle combinaison de configurations ici dans le Playground, puis copier le code et l'exécuter – ou des variations de celui-ci – n'importe où.

En fait, c'est là que vous apprenez à utiliser l'API. En d'autres termes, c'est ici que vous voyez des exemples de code qui peuvent former la base de beaucoup de ce que vous voudrez éventuellement exécuter dans votre propre environnement.

## Comment accéder aux exemples de code CURL

L'image suivante nous montre comment ce même prompt fonctionnerait si je décidais d'utiliser l'outil de ligne de commande, curl, au lieu de Python. 

![Image](https://www.freecodecamp.org/news/content/images/2023/12/gai-2-4.png)
_Outil View code du Playground avec du code curl_

`curl` est un outil de ligne de commande open source vénérable qui est souvent disponible par défaut. Vous utiliserez généralement `curl` lorsque vous souhaitez accéder à un serveur distant directement depuis votre ligne de commande. Ceux-ci seront généralement pour des requêtes relativement plus simples. 

Python, en revanche, sera l'outil de choix pour des applications plus compliquées qui impliquent une logique de programmation.

Pour confirmer qu'il est disponible sur votre système, tapez simplement `curl` à n'importe quel prompt de ligne de commande. Vous devriez voir un message d'aide avec des suggestions pour une utilisation correcte.

Outre Python et curl, vous pouvez également afficher du code en Node.js (pour lorsque vous construisez des applications basées sur un serveur) et en JSON (pour permettre des intégrations programmatiques). 

Avec cela, vous êtes prêt à plonger plus profondément que de simples sessions de chat : vous êtes maintenant capable de contrôler finement et d'automatiser de manière programmatique vos interactions avec GPT depuis le confort de votre propre ligne de commande (ou IDE).

Cet article est extrait de [mon livre Manning, The Complete Obsolete Guide to Generative AI](https://www.manning.com/books/the-complete-obsolete-guide-to-generative-ai?a_aid=bootstrap-it&a_bid=8c39744&a_bid=8c397448&chan=fcc_ai). Il y a beaucoup plus de bonnes choses technologiques disponibles via [mon site web](https://bootstrap-it.com).