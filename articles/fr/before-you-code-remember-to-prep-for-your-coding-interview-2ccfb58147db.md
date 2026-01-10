---
title: Quand il s'agit d'entretiens de codage sur tableau blanc, n'oubliez pas de
  vous PRÉPARER
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-21T19:33:05.000Z'
originalURL: https://freecodecamp.org/news/before-you-code-remember-to-prep-for-your-coding-interview-2ccfb58147db
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vLadxMniF0KW0HWeGkipJw.jpeg
tags:
- name: Coding Bootcamps
  slug: coding-bootcamps
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Quand il s'agit d'entretiens de codage sur tableau blanc, n'oubliez pas
  de vous PRÉPARER
seo_desc: 'By Andy Tiffany

  PREP is a mnemonic I created to help you remember the steps involved in solving
  whiteboard coding problems. It stands for Parameters, Return, Example, Pseudocode.


  The mnemonic is new, but the underlying technique is battle tested. Th...'
---

Par Andy Tiffany

PREP est un moyen mnémotechnique que j'ai créé pour vous aider à vous souvenir des étapes impliquées dans la résolution de problèmes de codage sur tableau blanc. Il signifie **P**aramètres, **R**etour, **E**xemple, **P**seudocode.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vbQ8FGNAlEC4jnxg8Z7Ceg.png)

Le moyen mnémotechnique est nouveau, mais la technique sous-jacente est éprouvée. Il s'agit essentiellement d'une version conviviale pour débutants du [développement piloté par les tests](https://en.wikipedia.org/wiki/Test-driven_development) qui se prête bien aux défis de codage.

Commençons tout de suite et apprenons PREP à travers un exemple de problème. Nous utiliserons JavaScript, mais cette technique fonctionne pour presque tous les langages de programmation.

### Votre interviewer vous demande d'écrire une fonction qui accepte une phrase et retourne le mot le plus long. Que faites-vous ?

#### « P » pour Paramètres

La plupart des problèmes impliquent d'écrire une fonction. Dans cette étape, vous devez déterminer quels paramètres votre fonction doit accepter. Ensuite, vous devez leur donner des noms significatifs.

Des mots-clés comme « prend en entrée » ou « accepte » dans l'énoncé du problème vous guideront ici. Si ce n'est pas clair, vous pouvez également demander à l'interviewer de clarifier. Dans votre cas, l'énoncé « accepte une phrase » vous indique que la fonction doit accepter un seul paramètre de type chaîne de caractères.

Vous avez donc déterminé le _type_ de votre paramètre. Mais comment devez-vous le nommer ? Cela peut sembler simple, mais bien nommer est une compétence de programmation cruciale, et cela prend de la pratique.

Vous pourriez l'appeler « sentenceString », mais l'appeler « sentence » est plus concis et il est toujours clair que nous traitons une chaîne de caractères.

Puisque c'est votre première étape, vous devez également penser à un nom significatif pour votre fonction elle-même. Dans votre cas, « longestWord » est à la fois concis et descriptif. Maintenant que vous avez décidé cela, vous pouvez écrire la structure de votre fonction comme ceci :

#### « R » pour Retour

Que retourne cette fonction ? Est-ce un nombre ? Un booléen ? Une chaîne de caractères ?

Rappelez-vous : la valeur qu'une fonction retourne n'est pas la même que ce qu'elle pourrait afficher dans une instruction print/log.

Une fois de plus, vous pouvez regarder l'énoncé du problème pour clarification. « Retourne le mot le plus long » vous indique que vous retournez un _mot_, et vous savez que les mots sont des chaînes de caractères. Rendons cela très clair en créant une variable pour représenter cette valeur de retour et en configurant votre fonction pour la retourner. Même si vous ne retournez pas encore la bonne réponse, vous êtes prêt à retourner le bon type. Vous avez créé un espace réservé qui rendra les étapes suivantes plus faciles.

#### « E » pour Exemple

Même pour les développeurs experts, le code statique est plus difficile à comprendre que le code en cours d'exécution. Vous voulez rendre votre code exécutable et « vivant » dès que possible. Vous pouvez donner vie à votre fonction avec un exemple d'invocation de test.

Vous savez que si votre fonction accepte la phrase « I saw a hippopotamus », elle _devrait_ retourner la chaîne « hippopotamus » une fois qu'elle fonctionne correctement. Mais pour l'instant, vous voulez simplement voir votre valeur de espace réservé de l'étape précédente pour confirmer que votre code est exécutable et configuré correctement.

#### Le dernier « P » est pour Pseudocode

Bien qu'il soit tentant de plonger directement et de commencer à coder maintenant, il serait trop facile de se laisser entraîner dans un détail qui pourrait vous distraire de la vue d'ensemble. Vous devez d'abord élaborer une stratégie, et le _pseudocode_ est juste la tactique pour cela.

Le pseudocode est une série d'instructions précises écrites en commentaires en langage parlé qui décrivent ce que vous devez faire.

### Vous avez terminé PREP. Maintenant vous pouvez coder !

Les quatre étapes de PREP vous ont aidé à bien cadrer le problème et à réfléchir à la manière de le résoudre. En vérité, un cadrage précis est la moitié de la bataille. La plupart des interviewers seront déjà impressionnés de voir votre approche méthodique. À ce stade, votre objectif est simplement d'écrire du code qui fera passer vos exemples et tests. Vous le ferez en encodant chacune de vos étapes de pseudocode.

Vous savez que vous avez une solution fonctionnelle lorsque vous pouvez exécuter votre code et voir la sortie correcte.

Vous avez passé la partie la plus difficile maintenant. Vous pouvez soupirer de soulagement car vous êtes au moins arrivé à une solution fonctionnelle. À ce stade, il ne reste plus que deux questions à considérer :

* Y a-t-il des cas limites qui pourraient casser le code ? Par exemple, devez-vous prendre en compte les phrases qui ont une période à la fin ? Vous écrirez plus de cas de test pour ces cas limites, puis corrigerez le code si nécessaire.
* Pouvez-vous rendre le code plus propre ou plus efficace maintenant ? Vous devriez discuter des idées avec l'interviewer afin qu'ils connaissent vos pensées avant de risquer de casser la solution.

C'est tout ! Ce processus peut sembler trop mécanique au début, mais faites-moi confiance, il deviendra une seconde nature — un peu comme les étapes pour apprendre à conduire. Même après plus de 12 ans de programmation, c'est toujours à peu près la séquence que je suis lorsque je résous des problèmes. Je serais plus susceptible d'utiliser un cadre de test formel au lieu d'instructions de journalisation comme nous l'avons fait ici, mais les étapes sont les mêmes dans les deux cas.

Maintenant, c'est à vous d'essayer ! Voici quelques problèmes de niveau débutant avec lesquels vous pouvez vous entraîner, dans un ordre de difficulté approximativement croissant :

1. Supposons que vous avez un tableau de chaînes comme [ "adios", "bye", "ciao" ]. Votre tâche est d'écrire une fonction appelée total_characters qui accepte un tel tableau comme paramètre et retourne le nombre total de caractères dans toutes les chaînes du tableau.
2. Écrivez une fonction pour lancer une pièce n fois qui retourne le nombre de fois où un « pile » a été obtenu.
3. _(De [Free Code Camp](https://www.freecodecamp.com/challenges/sum-all-numbers-in-a-range))_ Nous vous passerons un tableau de deux nombres. Retournez la somme de ces deux nombres et de tous les nombres entre eux. Le nombre le plus bas ne viendra _pas_ toujours en premier. Essayez d'utiliser PREP pour configurer cela vous-même d'abord, mais ensuite n'hésitez pas à confirmer votre configuration et à terminer la résolution [ici](https://www.freecodecamp.com/challenges/sum-all-numbers-in-a-range).

PREP a déjà aidé plusieurs apprenants de [First Step Coding](https://firststepcoding.com) à réussir leurs entretiens de codage, et j'espère qu'il pourra vous aider aussi. Bon codage !

_Si vous avez aimé cela, cliquez sur le ? ci-dessous pour que d'autres personnes voient cela ici sur Medium._