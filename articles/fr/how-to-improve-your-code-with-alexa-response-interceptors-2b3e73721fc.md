---
title: Comment améliorer votre code avec les interceptors de réponse Alexa
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-27T16:39:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-your-code-with-alexa-response-interceptors-2b3e73721fc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d0I7athFoo0jgOpGMLPCKg.jpeg
tags:
- name: Alexa
  slug: alexa
- name: Alexa Skills
  slug: alexa-skills
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment améliorer votre code avec les interceptors de réponse Alexa
seo_desc: 'By Garrett Vargas

  I’ve published over a dozen Alexa skills over the last few years. I have run across
  several patterns and best practices in that time.

  One of the more powerful but under-hyped features of the SDK that I’ve made extensive
  use of in my...'
---

Par Garrett Vargas

J'ai publié plus d'une douzaine de compétences Alexa au cours des dernières années. J'ai rencontré plusieurs modèles et meilleures pratiques pendant cette période.

L'une des fonctionnalités les plus puissantes mais sous-estimées du SDK que j'ai largement utilisée dans mon code est l'Interceptor de Réponse. Il fait partie du [Alexa Node SDK](https://www.npmjs.com/package/ask-sdk). Ce SDK simplifie le développement des compétences Alexa.

En l'utilisant, vous pourriez constater que votre code devient désordonné avec une gestion des erreurs redondante et des tâches de nettoyage. Les interceptors de réponse vous permettent d'insérer un hook dans le flux de gestion des intentions Alexa. Cela garde votre code propre en effectuant des actions de dernière minute en un seul endroit central avant de renvoyer la réponse à Alexa. Cela est extrêmement utile pour le **débogage**, la **résolution des tâches courantes**, et généralement pour **nettoyer les réponses** afin d'éviter certaines erreurs courantes rencontrées lors de l'utilisation de l'écosystème Alexa.

#### Débogage

Pour ajouter un interceptor de réponse avec le SDK Alexa, vous passez une classe qui implémente une fonction **process** à la fonction addResponseInterceptors sur votre objet SkillBuilder comme montré dans l'exemple de code ci-dessous. Nous aborderons les détails de l'implémentation de cette classe dans un instant.

Ce snippet montre également la définition d'une fonction d'interceptor de requête qui s'exécutera _avant_ qu'une requête ne soit passée à vos gestionnaires Alexa. Par exemple, je trouve que cela aide au débogage de journaliser chaque requête entrante et la réponse sortante. Vous pouvez faire cela avec l'interceptor de requête et l'interceptor de réponse comme démontré dans ce snippet de code. Le snippet montre également la syntaxe pour la fonction process retournant une Promise vide.

#### Résolution des tâches courantes

Beaucoup de mes compétences traitent AMAZON.RepeatIntent afin que l'utilisateur puisse réentendre la dernière réponse. Si vous avez une compétence complexe, surtout une qui maintient des moteurs d'état, vous devriez fournir des détails supplémentaires lorsque l'utilisateur demande à Alexa de se répéter afin que l'utilisateur sache exactement où il se trouve. Mais dans les compétences plus simples, il est acceptable de simplement rejouer la réponse précédente à l'utilisateur. Un interceptor de réponse vous permet de sauvegarder chaque discours sortant et les indices de réinvite afin que vous puissiez les rejouer facilement :

Une autre tâche courante est la gestion des attributs. Le SDK Alexa a plusieurs couches d'attributs.

* attributs de requête (valables uniquement pendant une seule requête)
* attributs de session (valables pour la durée d'une session)
* attributs persistants (sauvegardés dans un stockage comme DynamoDB pour être utilisés entre les sessions).

Je trouve que jongler avec tous ceux-ci peut être accablant. J'ai structuré mon code pour n'utiliser que les attributs de session, que je sauvegarde dans le stockage persistant à la fin de la session. Mais il y a deux problèmes avec cette approche générale — il y a des attributs que vous ne voulez peut-être pas sauvegarder et il y a des moments où vous voulez qu'une valeur passe entre les gestionnaires mais pas à travers la session (ce que les attributs de requête visent à résoudre).

Je contourne ces problèmes en utilisant un objet **session** et **request** hors de mes attributs. Vous pouvez voir un exemple du champ session dans le snippet de code ci-dessus sauvegardant lastResponse et lastReprompt. Je ne veux pas les sauvegarder de manière persistante, donc je nettoie cet objet entier avant de le persister dans le stockage à la fin de la session. De manière similaire, je nettoie l'objet request à chaque fois à la fin de mon interceptor de réponse, afin que ces attributs restent vraiment uniquement pour la requête.

#### Éviter les erreurs courantes

L'une des limitations qui tourmentent de nombreux développeurs est que les réponses ne peuvent pas contenir plus de 5 balises audio. Parfois, il peut être difficile d'éviter cela avec du contenu dynamique.

Par exemple, dans ma compétence Blackjack, je joue un son pour chaque carte qui est distribuée. Normalement, ce n'est pas un problème. Mais lorsque je lis la main du croupier, s'il finit par tirer plusieurs cartes, vous pouvez dépasser cette limite. Bien sûr, je pourrais essayer de rattraper cela lorsque je génère la réponse, mais cela complique le code. Qui peut dire si cela couvre tous les cas limites ?

Il est bien mieux de supprimer les effets sonores excédentaires dans le cadre du gestionnaire de réponse. Pour cette compétence, je supprime simplement les fichiers audio excédentaires de la fin de la réponse pour réduire le compte à 5.

Un autre problème que j'ai rencontré est que vous n'êtes pas autorisé à retourner des directives avec la directive Dialog.Delegate si vous sollicitez des slots de l'utilisateur. Cela peut être ennuyeux si vous gérez l'entrée des boutons ou utilisez des directives d'affichage. Vous pourriez devoir vérifier à plusieurs endroits avant d'ajouter des directives à votre réponse pour vous assurer de ne pas entrer en conflit avec le Dialog.Delegate. Gardez votre code propre et utilisez un responseInterceptor pour filtrer vos directives avant de les retourner :

J'espère que vous avez apprécié ces conseils et que vous voyez la puissance de l'utilisation des interceptors de réponse. Faites-moi part de vos propres meilleures pratiques et partagez vos propres conseils dans la section des commentaires !