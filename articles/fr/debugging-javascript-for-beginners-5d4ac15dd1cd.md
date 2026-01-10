---
title: Conseils et astuces de débogage pour les débutants en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-06T03:12:15.000Z'
originalURL: https://freecodecamp.org/news/debugging-javascript-for-beginners-5d4ac15dd1cd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Tmt5zAQNLHt3GIELqHmFWw.jpeg
tags:
- name: beginner
  slug: beginner
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Conseils et astuces de débogage pour les débutants en JavaScript
seo_desc: 'By Priyanka Garg

  My intended audience for this tutorial is beginner programmers. You’ll learn about
  frustration-free debugging with chrome dev tools.

  Dear Beginner, a while ago, I was where you are! After a lot of struggles, I feel
  like I have come f...'
---

Par Priyanka Garg

Mon public cible pour ce tutoriel est les programmeurs débutants. Vous apprendrez à déboguer sans frustration avec les outils de développement de Chrome.

Cher Débutant, il y a quelque temps, j'étais à votre place ! Après beaucoup de luttes, j'ai l'impression d'avoir parcouru un long chemin dans mon parcours d'apprentissage. Je suis actuellement dans la phase avancée d'un bootcamp immersif où je développe des applications full stack.

Chaque jour, j'apprends et je tombe sur tant de choses que j'aurais aimé connaître avant. Cet article est une tentative de partager une de ces idées qui vous facilitera la vie.

Comme vous l'avez probablement appris, la meilleure façon d'apprendre la programmation est de pratiquer. Maintenant, lorsque vous commencez à pratiquer le codage, parfois (ou la plupart du temps), votre code ne fonctionnera pas ; en d'autres termes, il y aura un BUG dans votre code. Et vous avez peut-être déjà essayé et appris certaines approches de débogage. Cet article ne traite pas d'une approche spécifique de débogage, mais plutôt d'une configuration pour déboguer votre code lors de la pratique de la programmation.

Si vous pratiquez sur un environnement de développement en ligne, vous avez probablement une configuration où vous avez un éditeur, un problème et une suite de tests qui teste votre programme.

Vous avez écrit du code, et il y a quelques bugs, et à un moment donné, les erreurs renvoyées par la suite de tests ne sont pas vraiment utiles.

Je ne vais pas m'étendre sur la façon dont le débogage peut devenir fastidieux ici — passons plutôt directement à quelques conseils pour les débutants.

### Le problème

Par exemple, j'écris un vérificateur de palindromes dans l'éditeur de FreeCodeCamp. Ma solution échoue. Dans ce cas, nous pourrions utiliser les résultats de la suite de tests pour déboguer.

Mais supposons que cette suite de tests ne me donne pas de bons indices sur l'erreur exacte. (Ce n'est peut-être pas l'exemple idéal en termes d'erreur logique. Le point est que vous rencontrerez des problèmes où la suite de tests ne pointera pas directement vers une erreur logique.)

![Image](https://cdn-media-1.freecodecamp.org/images/dwhQsMHv5CPslBuNUg-zP0k5hLajefSpkYjA)

#### **Astuce : Utilisez la console des outils de développement.**

J'exécute le même code dans la console avec le cas de test échoué, et je vois qu'il retourne 'undefined'. Cela signifie que le code n'a renvoyé aucune valeur. Je peux rapidement voir que j'ai oublié de retourner 'true' si la chaîne était un palindrome.

![Image](https://cdn-media-1.freecodecamp.org/images/m1vALMoCZfmqBhdCbcr9RsLavcnrlCQBeCf2)

C'était une erreur très simple. La plupart du temps, vous aurez des bugs qui nécessiteront d'examiner vos variables. Une approche pour vérifier les variables consiste à utiliser **_console.log(<variable_**s>) dans le programme.

Cependant, je vous suggère d'utiliser plutôt le **_débogueur des outils de développement_**. Dans votre programme, vous pouvez spécifier le point où vous souhaitez commencer à obtenir de l'aide du débogueur.

![Image](https://cdn-media-1.freecodecamp.org/images/-PRHwB8hzqcCh2WhQmQSubwCXsMucMPhmlgn)

Le débogueur vous montrera toutes les variables dans la pile d'appels et vous permettra de parcourir les appels de fonctions, ce que vous trouverez très utile.

![Image](https://cdn-media-1.freecodecamp.org/images/7IKv-WVp8ztTZyyC-zlAnOmOxN5gpi9FGmD4)

Vous vous habituerez à utiliser le débogueur après l'avoir utilisé quelques fois. Remarquez les flèches dans la boîte en bas à gauche ? Elles vous permettront de contrôler le flux du programme et de montrer les variables à mesure qu'elles changent.

Passons maintenant à une astuce.

#### **Astuce : Créez une configuration de débogage personnelle**

Comme vu précédemment, avec le débogueur et la console, nous pouvons identifier les problèmes facilement. Cependant, si je veux exécuter le programme corrigé à nouveau sur la console avec une seule ligne de changement, je devrais le retaper.

Même après cela, j'obtiens une erreur :

![Image](https://cdn-media-1.freecodecamp.org/images/XKcVHUYzfB150kJNfqHACYaqmfWtxBYTsZi7)

Cette erreur est due au fait que j'ai utilisé une fonction fléchée et que je ne peux pas redéclarer une _const_. Cela signifie que je devrais ouvrir un nouvel onglet et une nouvelle console chaque fois que je change mon code. Un surcroît de travail, n'est-ce pas ?

Trouvons une solution de contournement. Sur votre système, créez un répertoire et accédez à ce répertoire.

Créez maintenant deux fichiers : index.js et index.html. Tapez le HTML suivant dans index.html :

![Image](https://cdn-media-1.freecodecamp.org/images/Pyy9bL6vTdq4wxYW-DKHxEAHHUny7pdod0Yi)

Maintenant, déplacez votre code de la console vers index.js. Remarquez que j'ai démarré le débogueur à la ligne 2 dans le code.

![Image](https://cdn-media-1.freecodecamp.org/images/NbliUjnLiOhn5w9NTgL61cnY1qUdxf8QkIZ8)

Maintenant, exécutez le fichier index.html dans le navigateur. Ouvrez les outils de développement ou la console (vous devrez peut-être actualiser pour voir le débogueur). Vous pouvez déboguer votre code ici.

![Image](https://cdn-media-1.freecodecamp.org/images/aF-D9XXD3MF2bPnufdhclS2Ht9TiVDyd0XRT)

Maintenant, chaque fois que vous apportez une modification à index.js, il vous suffit d'actualiser cet onglet et le code s'exécute à nouveau. Pas besoin de fermer et d'ouvrir des onglets, pas besoin de retaper tout le programme.

Gardez le dossier que vous venez de créer à portée de main. Chaque fois que vous devez essayer ou déboguer un morceau de code, placez-le dans index.js et expérimentez !!

#### Réflexions finales

Si vous saviez déjà cela, félicitations, vous avez perdu 4 minutes précieuses ;)

Enfin, rappelez-vous que _l'erreur est humaine !_ Ne vous inquiétez pas des bugs — ils vous enseigneront les leçons les plus précieuses de la programmation... et puis... _Oh ! les endroits où vous irez..._