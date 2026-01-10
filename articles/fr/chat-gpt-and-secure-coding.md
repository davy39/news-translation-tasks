---
title: ChatGPT peut-il garantir des pratiques de codage sécurisées ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-06T14:56:56.000Z'
originalURL: https://freecodecamp.org/news/chat-gpt-and-secure-coding
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/chatgpt-coding.jpg
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
seo_title: ChatGPT peut-il garantir des pratiques de codage sécurisées ?
seo_desc: "By Andrej Kovacevic\nChatGPT has been in the news a lot recently. The hype\
  \ around it continues, and many are concerned that this AI service might put many\
  \ out of work. \nDevelopers in particular feel threatened by this AI bot’s ability\
  \ to write code on..."
---

Par Andrej Kovacevic

ChatGPT a été beaucoup dans l'actualité récemment. L'engouement autour de celui-ci continue, et beaucoup s'inquiètent que ce service d'IA puisse mettre beaucoup de gens au chômage. 

Les développeurs se sentent particulièrement menacés par la capacité de ce bot IA à écrire du code à la volée. Le consensus général est cependant que les emplois de rédaction de code pour les humains sont sûrs pour l'instant. 

Le conseiller technologique Bernard Marr affirme que [ChatGPT et la technologie de traitement du langage naturel](https://www.forbes.com/sites/bernardmarr/2023/01/23/how-chatgpt-and-natural-language-technology-might-affect-your-job-if-you-are-a-computer-programmer/) ne rendront probablement pas les développeurs, programmeurs et ingénieurs logiciels superflus maintenant et dans un avenir proche. 

## Les limitations de ChatGPT

Tout d'abord, ChatGPT ne peut écrire que des applications relativement simples. Même s'il a les compétences pour faire du codage plus avancé avec des instructions appropriées, il ne donne pas instantanément aux non-développeurs un avantage concurrentiel sur les développeurs qui comprennent le codage et ont de l'expérience dans l'écriture réelle de code.

Une autre raison cruciale pour laquelle de nombreux emplois de développeurs sont sûrs est le besoin de codage sécurisé. ChatGPT lui-même concède qu'il ne peut pas garantir que le code qu'il produit est sécurisé.

Interrogé sur la capacité de ChatGPT à garantir la sécurité du code, voici la brève réponse du bot :

> « Non, ChatGPT ne garantit pas un codage sécurisé. ChatGPT est un modèle de langage IA qui peut aider à répondre aux questions et à générer du texte en fonction des entrées qu'il reçoit. Cependant, il n'a pas la capacité de garantir des pratiques de codage sécurisées ou de réaliser des évaluations de sécurité sur le code. Il est important de suivre les directives de sécurité établies et les meilleures pratiques lors du développement et du déploiement de code. »

ChatGPT apprend davantage à mesure qu'il est continuellement mis à jour. Mais sa capacité à incorporer des pratiques de codage sécurisées peut prendre un certain temps pour atteindre un niveau de maturité acceptable. Ou il peut ne jamais être capable de perfectionner le codage sécurisé, étant donné la nature évolutive du paysage des menaces.

## Qu'est-ce que le codage sécurisé ?

Le [codage sécurisé](https://www.checkpoint.com/cyber-hub/cloud-security/what-is-secure-coding/) est un nouveau paradigme dans le développement de code où la responsabilité de garantir la sécurité du code est déplacée vers la gauche ou revient au développeur. La sécurité n'est plus un processus séparé, mais fait partie du cycle de vie du développement logiciel (SDLC). Cela peut ne pas être obligatoire, mais c'est encouragé et préféré.

Les organisations qui adoptent le codage sécurisé gagnent l'avantage de pouvoir facilement se conformer aux normes de l'industrie. 

Au lieu de passer par une autre étape de numérisation et de test du code pour garantir la sécurité, le processus de production logicielle est considérablement raccourci car les bugs et autres défauts sont traités avant que le code ne soit déployé. 

Il est plus facile de corriger ces problèmes si vous pouvez les repérer et les résoudre pendant le processus d'écriture du code au lieu de les traiter dans une étape séparée.

Le codage sécurisé peut sembler être un fardeau supplémentaire pour les développeurs, mais c'est un changement qui vaut la peine d'être adopté étant donné ses avantages significatifs. Il intègre la sécurité avec le SDLC pour réduire le besoin de révisions de sécurité majeures. Et il en résulte une sécurité d'application significativement meilleure lors de la sortie.

## Pourquoi ChatGPT n'est pas encore capable de codage sécurisé

Le codage sécurisé implique des meilleures pratiques évolutives qui n'ont pas encore été apprises par ChatGPT. Comme révélé dans sa FAQ, [ses connaissances sont limitées](https://help.openai.com/en/articles/6783457-chatgpt-general-faq) aux choses qui ont été mises en ligne jusqu'en 2021. 

ChatGPT n'est pas mis à jour avec les dernières informations sur les nouvelles menaces, vulnérabilités et attaques. Il n'est pas spécifiquement lié à un cadre de cybersécurité. Il manque également dans les domaines suivants :

### Visibilité et surveillance de la sécurité

ChatGPT n'est pas conçu pour tenir compte des données qui sont enregistrées dans le dépôt de code qu'il génère. Il ne effectue pas non plus de scans de surveillance de détection de vulnérabilités automatisés, de triage et de mappage de tous les actifs informatiques qui seront impactés par l'application. 

En raison de cela, il n'y a aucune assurance que le code qu'il produit est sûr pour l'écosystème informatique spécifique où il sera déployé.

### Aucune conscience de la gestion des secrets

Il arrive que les développeurs incluent involontairement des secrets tels que des paires nom d'utilisateur-mot de passe, des clés API et des jetons dans les entrées de journal. C'est un non-non dans le codage sécurisé, et ChatGPT n'a pas la conscience de prendre cela en compte.

### Aucune garantie contre la mauvaise configuration

La mauvaise configuration est le plus grand défaut dans le codage humain. L'IA est censée aider à éviter cela, mais il est clair que ChatGPT n'offre aucune garantie qu'il n'y aura pas de problèmes de configuration dans les applications qu'il développe.

### Incapacité à appliquer l'obfuscation de code 

L'obfuscation de code fait référence à la modification du code source ou du code machine pour le rendre difficile à comprendre et à reverse engineer pour les hackers. C'est l'une des techniques utilisées dans le codage sécurisé, et ChatGPT dit qu'il est incapable de le faire.

### Manque de capacité à effectuer des révisions de sécurité de code 

ChatGPT concède également que la révision de code n'est pas dans sa gamme de compétences impressionnantes. Voici ce que le chatbot IA a à dire à ce sujet :

> « En tant que modèle de langage, je peux fournir des informations sur diverses pratiques de sécurité logicielle et suggérer les meilleures pratiques, mais je ne peux pas effectuer une révision de sécurité de code efficace par moi-même. »

### Aucune validation de source de données externe 

Il existe des projets de développement qui impliquent l'utilisation de code et de modules pré-écrits provenant de sources open-source ou tierces. 

L'intégration de ces composants avec du code écrit par ChatGPT peut ne pas être une bonne idée. ChatGPT n'a pas la capacité de garantir la légitimité, la sécurité et l'authenticité des sources de données externes.

### Aucun modèle de menace 

ChatGPT est un chatbot à usage général qui est capable d'écrire du code passable. Il n'est pas surprenant qu'il ne possède pas de capacités avancées de codage sécurisé comme un processus multistage pour l'évaluation des faiblesses et des vulnérabilités du code tout au long du SDLC.

## L'ironie de l'IA dans la cybersécurité

Malgré le fait qu'elle soit présentée comme l'une des technologies les plus importantes en cybersécurité, les chatbots IA comme ChatGPT ne dépassent pas réellement en cybersécurité. 

Ils sont des outils efficaces pour simplifier les tâches dans divers processus de cybersécurité tels que la détection des menaces, des attaques et des comportements anormaux. Mais ils ne peuvent pas être laissés à eux-mêmes pour appliquer une cybersécurité efficace.

Le codage de logiciels n'est pas aussi simple et direct que beaucoup ont tendance à le penser dans le contexte de l'engouement pour ChatGPT. Cela ne signifie pas que les outils d'IA comme ChatGPT ne sont pas remarquables. Mais ChatGPT ne possède pas les connaissances spécialisées et l'expertise pour traiter de manière fiable les menaces modernes.

## Conclusion

Des outils de codage sécurisé alimentés par l'IA existent pour aider ceux qui souhaitent traiter les potentielles failles de sécurité dans le code qu'ils construisent. Mais le code n'est bon que les intentions et la profondeur de compréhension du développeur. 

Les débutants en codage qui savent peu comment fonctionne le codage, et encore moins comment les sécuriser, devront améliorer leur compréhension du codage et de la cybersécurité pour tirer pleinement parti du codage IA et des solutions de codage sécurisé IA.

_Image via Unsplash (Jonathan Kemper)_