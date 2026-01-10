---
title: Que peut nous apprendre La Casa de Papel sur la cybersécurité ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-07T14:49:47.000Z'
originalURL: https://freecodecamp.org/news/cybersecurity-lessons-from-money-heist-show
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/money-heist-image.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: '#infosec'
  slug: infosec
- name: threat modeling
  slug: threat-modeling
seo_title: Que peut nous apprendre La Casa de Papel sur la cybersécurité ?
seo_desc: 'By Periklis Gkolias

  I was watching the TV series, La Casa De Papel (Money Heist), on Netflix a few weeks
  ago. I realized that the story of the gang can reveal some best practices we should
  use while dealing with the security of the products we build....'
---

Par Periklis Gkolias

Je regardais la série télévisée, La Casa De Papel (Money Heist), sur Netflix il y a quelques semaines. J'ai réalisé que l'histoire de la bande peut révéler certaines bonnes pratiques que nous devrions utiliser tout en traitant de la sécurité des produits que nous construisons.

Attention – ce texte contient des spoilers. Si vous n'avez pas regardé la série jusqu'à la fin et que vous prévoyez de le faire, veuillez visiter l'article un autre jour. Ou poursuivez à vos propres risques :)

## La modélisation des menaces peut vous protéger contre les événements inattendus

Tout d'abord, **qu'est-ce que la modélisation des menaces** ?

La modélisation des menaces, en termes profanes, est un processus analytique. Dans celui-ci, les ingénieurs qui construisent un produit coordonnent avec l'équipe de sécurité. Ils collaborent vers l'architecture de sécurité du produit.

Plus spécifiquement, c'est le modèle – comment quelqu'un peut attaquer le produit – et ce qui vaut la peine d'être protégé (actifs). Ils modélisent également ce qu'ils peuvent moins craindre. Moins craindre non pas parce qu'ils ne s'en soucient pas. Mais parce que le protéger peut être plus coûteux que l'actif lui-même.

La modélisation des menaces peut vous mener loin et vous protéger contre certains événements, contre toute attente.

Qu'est-ce que la modélisation des menaces dans notre cas "La Casa de Papel" ? C'est le plan du Professeur (alias Sergio Marquina) contre toutes les routes potentielles que le plan prendra. En ayant des alternatives, même pour les scénarios les plus extrêmes. Les actifs sont clairement l'argent volé ou ses complices dans le braquage.

## Un seul point de défaillance peut causer une chaîne de mauvaises réactions

La modélisation des menaces peut vous aider à vous remettre de nombreux problèmes de sécurité qui surgiront. Vous pouvez vous remettre d'une cyberattaque, mais les choses ne seront plus jamais les mêmes. Une faille dans le mur de sécurité peut avoir un effet domino.

Imaginez un barrage de lac, avec quelques fissures autour qui passent inaperçues et sont exploitées par la nature. Vous pouvez toujours le réparer, mais il faudra peut-être du temps pour que les visiteurs du lac rétablissent leur confiance.

De la même manière, les petites entreprises qui subissent un problème de sécurité peuvent fermer dans les mois suivants, selon une [enquête](https://cybersecurityventures.com/60-percent-of-small-companies-close-within-6-months-of-being-hacked/).

C'est comme le Professeur, qui a perdu le respect après que l'or a (temporairement) disparu. Même si ses grandes compétences en résolution de problèmes ont aidé à résoudre le problème, les choses se sont rapidement compliquées.

![Réactions en chaîne](https://i.imgur.com/3047AXD.jpg)

## La chance n'est pas une stratégie à long terme

Dans la série, il y a quelques cas provocants de chance. Par exemple :

* Raquel reniant l'organisation policière
* La police et l'armée échouant dans leurs plans pour envahir la banque
* Échec de tirer sur la cible à plusieurs reprises. Surtout par des troupes qui sont censées être des tireurs professionnels.

Après tout, dans le livre [pragmatic programmer](https://www.amazon.com/Pragmatic-Programmer-Journeyman-Master/dp/020161622X), il y a un chapitre entier sur la mauvaise pratique de programmer par coïncidence. Cela compare la chance-en-tant-que-stratégie avec le soldat qui avance sans plan dans un champ rempli de mines terrestres.

Les indicateurs et une défense pire que prévue peuvent vous donner un peu de temps supplémentaire pour avancer avec votre plan ou vous échapper. Mais vous devez en tirer parti. Soit pour avancer avec votre plan, soit pour vous échapper. Pensez toujours que votre chance peut disparaître, à tout moment.

## Ne lâchez jamais les armes

Cela ne s'applique pas spécifiquement à la cybersécurité, mais à la vie en général.

La douleur est temporaire, abandonner dure éternellement. Acceptez vos erreurs, remédiez-y et apprenez d'elles. Tant que votre cœur bat, vous n'êtes pas encore mort.

* Erreur architecturale ? Corrigée immédiatement et réarchitecturer le produit (oui, je sais... les contraintes de livraison et d'affaires)
* Surveillance en dessous des attentes ? Corrigée maintenant. Ajoutez plus de personnes et voyez comment elles peuvent être plus efficaces
* Défauts sérieux dans le code ? Formez votre équipe aux pratiques sécurisées et aux revues de code axées sur la sécurité. Achetez une licence pour un package comme Snyk ou Nessus. Prévoyez un pourcentage de votre capacité pour corriger les plus graves

![Contraintes budgétaires](https://i.imgur.com/BtMM0JS.jpg)

## Même dans les pires moments, gardez votre sang-froid

Imaginez une attaque par ransomware. Elle est là, elle se produit. Crier sur les têtes des gens ne résoudra pas le problème.

Lorsque vous ne pouvez pas gagner contre une attaque, vous devez toujours faire de votre mieux, pour au moins ne pas perdre. Surtout, ne paniquez pas. Comme le disent les Stoïciens, vous devez être la meilleure version de vous-même sur les choses que vous contrôlez. Et laissez le reste être. Acceptez-les.

Vous ne pouvez pas contrôler la prochaine étape d'une attaque. Mais vous pouvez faire de votre mieux pour l'empêcher, pour ne pas répéter les mêmes erreurs, et pour fermer les portes ouvertes qui existent maintenant.

Cela est vrai pour les problèmes non techniques également. Si un tuyau se casse à la maison, que feriez-vous ? D'abord, vous arrêtez les dégâts et peut-être fournissez une solution durable (étant donné le délai). Ensuite, vous essayez de voir comment cela ne se reproduira plus jamais.

Ne perdez pas votre sang-froid et votre esprit clair, comme Tamayo l'a perdu, lorsqu'il a réalisé que la bande le faisait chanter pour diverses raisons.

Il s'est mis en colère, il s'est fait chanter, il a même été ridiculisé aux yeux de la Banque centrale européenne. Et quel a été le résultat ? Il a perdu, sans discussion, même s'il a menti aux médias sur sa victoire.

## Conclusion

La cybersécurité de premier ordre n'est pas un repas gratuit. Et tout le monde ne peut pas le faire, car les pièges sont si nombreux. Mais avec un peu de discipline, de rétrospection et d'humilité, vous pouvez faire des merveilles. De plus, la série est géniale, si vous ne l'avez pas vue, veuillez la regarder.