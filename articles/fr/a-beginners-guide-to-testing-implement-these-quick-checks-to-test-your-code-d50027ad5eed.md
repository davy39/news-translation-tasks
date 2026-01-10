---
title: 'Un guide pour débutants sur les tests : les cas limites de gestion des erreurs'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-25T17:26:12.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-testing-implement-these-quick-checks-to-test-your-code-d50027ad5eed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ETy_5fhvpirGCwJgZXwuRw.jpeg
tags:
- name: coding
  slug: coding
- name: Computer Science
  slug: computer-science
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: 'Un guide pour débutants sur les tests : les cas limites de gestion des
  erreurs'
seo_desc: 'By JonLuca De Caro

  When building complex pieces of software, regardless of language, you start to notice
  a pattern in your testing habits. The same similar-looking issues will arise across
  different platforms or projects. Regardless of whether you’re...'
---

Par JonLuca De Caro

Lors de la construction de logiciels complexes, quel que soit le langage, vous commencez à remarquer un schéma dans vos habitudes de test. Les mêmes problèmes, semblables en apparence, surgiront sur différentes plateformes ou projets. Que vous construisiez une autre démonstration simple de liste de tâches pour une conférence ou que vous architecturiez un back-end complet pour une startup PaaS, les mêmes modèles génériques commencent à émerger.

Il existe six cas qui doivent être testés et qui mettront en lumière un nombre surprenant de problèmes. Ces cas ne sont pas destinés à être exhaustifs ou à constituer une suite de tests complète à eux seuls. Ils représentent plutôt un sous-ensemble facile à retenir de paradigmes de test courants qui peuvent s'appliquer à n'importe quel langage, framework ou environnement.

Ces cas sont immédiatement utiles dans deux aspects des routines quotidiennes de codage : le débogage de problèmes spécifiques lorsqu'ils surviennent, et la création de la suite de tests pour une base de code. Ils sont destinés à être des formes génériques et abstraites de test qui mettront en lumière certains des problèmes les plus courants auxquels les développeurs juniors sont confrontés.

Ces cas ne seront utiles que de manière détournée en programmation fonctionnelle. La programmation fonctionnelle contourne de nombreux types de bugs les plus simples décrits ci-dessous. Dans tous les cas, il est utile de garder à l'esprit ces cas limites abstraits, car ils fournissent une protection contre les mauvaises pratiques dans le code.

Les six tests sont les suivants :

* Zéro
* Un
* Deux
* Deux à max-1
* max
* max+1

Bien que ces cas soient des cas limites, leur valeur réside dans ce qu'ils représentent. Tout en veillant à ce que vos tests couvrent toutes les fonctionnalités de votre programme, vous devez garder vos tests simples avec aussi peu de fantaisie que possible.

### Zéro

Zéro est utilisé pour signifier toute forme d'entrée nulle, qu'il s'agisse de non défini, null, d'un tableau vide ou simplement du nombre 0. Arguablement la forme la plus courante et simple de bug est la référence à une valeur Zéro, et il est toujours utile de la tester. Testez simplement une fonction, un endpoint ou un upload avec une entrée Zéro, et vérifiez qu'il se comporte comme prévu.

### Un

Un, comme Zéro, est la forme la plus basique du test unique généralisé. La fonction est testée avec la première entrée valide et normale. Cela est particulièrement utile pour les tests de régression. Dans les itérations futures du code, ce test indiquera rapidement si le programme (ou le processus) fonctionne comme prévu.

Le test Un vous donne une base de référence pour le succès, qu'il s'agisse d'une authentification réussie sur un endpoint admin, d'un upload de fichier valide ou d'une modification correcte de tableau.

### Deux

Deux ne consiste pas simplement à tester l'index de tableau 2, ou à vérifier si votre algorithme fonctionne avec 2 entrées. Il englobe également ce qui se passe lorsque vous exécutez le même code deux fois.

Si quelqu'un devait faire une requête HTTP DELETE deux fois de suite sur la même ressource, que se passerait-il ? Si la fonction de tri avec un comparateur personnalisé est appelée deux fois de suite, se comporte-t-elle comme prévu ?

Deux est un nombre intéressant, car c'est la première fois où un code valide qui fonctionne lorsqu'il est appelé une fois peut montrer des effets secondaires lors d'exécutions répétées. Prenons un petit changement dans les fonctions que nous avons testées ci-dessus.

Cela revient aux modifications de l'état et à la compréhension du comportement d'une fonction. Si tout ce que nous avons est le nom de la fonction, alors ce code se comporte précisément comme prévu. Vous avez une variable appelée 0, vous appelez la fonction setVarToOne, puis vous affirmez qu'elle est égale à un.

À première vue, cela s'est comporté exactement comme prévu. Cependant, le tester avec l'idée de Deux à l'esprit mettrait en lumière des problèmes plus profonds avec le code. Vous le testeriez en l'appelant deux fois et en affirmant que dans les deux cas, mVar est égal à 1.

### Deux à max-1

Deux à max-1 est le test de cohérence. Il est très similaire au test Un, mais il y a une subtile différence. Cela devrait être un cas d'utilisation **moyen** — pas le plus simple ou le plus direct, ou le plus facile à lire. Juste un cas d'utilisation moyen qui n'est peut-être pas particulièrement simple, mais qui est assez **courant**.

### Max

Max est assez simple : il teste simplement les limites de votre application, en particulier autour des constantes max définies.

Si vous avez une implémentation simple de liste chaînée, vous pourriez imaginer que vous avez un nombre apparemment infini d'insertions autorisées. En réalité, il existe une limite supérieure — qu'il s'agisse de INT_MAX, du nombre de descripteurs de fichiers que votre système d'exploitation peut avoir ouverts, ou simplement de la quantité de mémoire ou d'espace disque alloué pour votre programme.

Dans certaines circonstances, Max peut sembler un test impossible car il n'y a pas de max connu pour ce que vous testez. Son objectif dans ces cas, cependant, est d'une autre nature : stresser votre application.

Par exemple, il est possible qu'une certaine donnée soumise par l'utilisateur soit réduite et passée à travers des fonctions jusqu'à ce qu'elle atteigne une boucle que vous avez définie. Si cette donnée est, par exemple, INT_MAX, cela pourrait prendre un temps non négligeable pour que votre code se termine. Pire encore, cela pourrait plonger votre code dans un état de non-arrêt. Ces problèmes peuvent être subtils et ne se manifester que lorsque votre code passe en production, il est donc important de les détecter pendant la phase de test.

### Max+1

Max+1 est un test principalement utilisé pour vérifier les normes ou règles mises en place par le programmeur. Cela implique de tester quoi que ce soit à sa limite théorique + epsilon.

Cela pourrait se manifester par un problème de dépassement de tableau, une erreur de décalage d'un, une erreur de dépassement d'entier, ou tout autre type de problème qui se produit lorsque vous atteignez les limites de votre fonction ou programme.

Si vous avez une taille maximale de téléchargement de fichier de 2 Mo, essayez de télécharger un fichier de 2 Mo + 1 octet. Si vous avez une limite sur le nombre d'entrées dans un catalogue utilisateur, assurez-vous que la vérification se fait à la fois côté client **et** côté serveur.

### Conclusion

Comme mentionné ci-dessus, cela ne représente pas une image complète de ce que vos routines de débogage ou de test devraient être. Cela fournit simplement une base solide et générique qui devrait transcender toute suite de tests ou framework spécifique.

Les tests sont communément considérés comme des cas limites ou des cas extrêmes, mais ils peuvent surgir dans des endroits qui ne sont pas immédiatement évidents.