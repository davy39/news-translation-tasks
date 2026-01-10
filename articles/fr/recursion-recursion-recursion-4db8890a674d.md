---
title: Récursivité, Récursivité, Récursivité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-27T07:51:06.000Z'
originalURL: https://freecodecamp.org/news/recursion-recursion-recursion-4db8890a674d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3E0JXxCCMTTKYtlmwONWbA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Récursivité, Récursivité, Récursivité
seo_desc: 'By Michael Olorunnisola

  Before I tell you what recursion is, you should read this article:

  Recursion, Recursion, Recursion_Before I tell you what recursion is, you should
  read this article:_medium.freecodecamp.com

  Give yourself a pat on the back if y...'
---

Par Michael Olorunnisola

Avant de vous dire ce qu'est la récursivité, vous devriez lire cet article :

[**Récursivité, Récursivité, Récursivité**](https://medium.freecodecamp.com/recursion-recursion-recursion-4db8890a674d)  
[_Avant de vous dire ce qu'est la récursivité, vous devriez lire cet article : medium.freecodecamp.com](https://medium.freecodecamp.com/recursion-recursion-recursion-4db8890a674d)

Félicitez-vous si vous n'êtes pas tombé dans le panneau. Si c'est le cas, pas de souci — vous savez maintenant ce qu'est la récursivité !

> Les gens plaisantent souvent en disant que pour comprendre la récursivité, vous devez d'abord comprendre la récursivité. — John D. Cook

Quand j'ai commencé à coder, je pensais tout le temps à la récursivité. Je la considérais comme une sorte de sortilège magique, ou une technique de haut niveau que seuls les meilleurs développeurs utilisaient pour résoudre les problèmes les plus difficiles.

En réalité, ce n'est pas du tout magique. Mais les bons développeurs la comprennent. Et les excellents développeurs savent quand il est préférable de l'utiliser.

Alors, qu'est-ce que la récursivité exactement ?

Avez-vous déjà pratiqué quelque chose encore et encore jusqu'à ce que vous le "maîtrisiez" ? Alors vous avez effectué un acte récursif.

En termes simples, vous avez exécuté une tâche ou une série d'étapes de manière répétée jusqu'à atteindre un objectif souhaité. Cela, mes amis, est l'essence de la récursivité.

En langage de code, une fonction récursive est une fonction qui s'appelle elle-même.

Avant de plonger dans le code, examinons un exemple de base pour comprendre la structure des fonctions récursives. Comme le piano me tient à cœur, nous allons créer une fonction appelée practicePiano.

Chaque fois que cette fonction est appelée avec une personne, cette personne pratiquera le piano. Comme je ne passe pas assez de temps à m'entraîner en ce moment, je devrais m'entraîner un peu.

```
practicePiano(person){  practiceScales(person);    practiceChords(person);}
```

```
practicePiano('Michael');
```

J'ai appelé la fonction ci-dessus une fois, donc j'ai pu faire une session, mais j'ai définitivement besoin de plus d'une session pour vraiment m'améliorer.

```
practicePiano('Michael');practicePiano('Michael');practicePiano('Michael');practicePiano('Michael');practicePiano('Michael');practicePiano('Michael');practicePiano('Michael');practicePiano('Michael');...
```

C'est bien et tout, mais cela viole l'un des grands principes de la programmation : Ne vous répétez pas (DRY).

J'ai pu faire plus de sessions de pratique, mais chaque fois que je veux m'entraîner davantage, je dois ajouter un autre appel à practicePiano.

Une façon de résoudre ce problème est d'appeler la fonction à l'intérieur d'elle-même, afin que chaque fois que je pratiquePiano, je m'entraîne davantage :

```
practicePiano(person){  practiceScales(person);    practiceChords(person);
```

```
//Magie récursive ici !
```

```
  practicePiano(person);}
```

```
//Maintenant, nous n'avons besoin que d'un seul de ceux-ci !
```

```
practicePiano('Michael');
```

C'est génial ! Je n'ai qu'à l'appeler une fois. Le seul problème est que, une fois que j'appelle cette fonction… je ne m'arrête jamais de m'entraîner. Je ne m'arrête jamais jusqu'à ce qu'il soit littéralement impossible pour moi de m'entraîner davantage.

```
//Notre code ci-dessus se comporterait comme suit :
```

```
  practiceScales('Michael');    practiceChords('Michael');
```

```
//Appel récursif
```

```
  practiceScales('Michael');    practiceChords('Michael');
```

```
//Appel récursif
```

```
  practiceScales('Michael');    practiceChords('Michael');
```

```
//Appel récursif
```

```
//..jusqu'à ce que je ne puisse plus physiquement m'entraîner
```

Lorsque votre ordinateur atteint un point similaire où il est incapable de continuer, il retourne généralement cette erreur :

```
RangeError: Maximum call stack size exceeded
```

C'est l'équivalent de votre ordinateur disant : « J'ai épuisé l'espace et j'ai dû fermer boutique. » Il a enregistré chaque appel de fonction en mémoire dans une pile. Mais comme les appels ne s'arrêtent jamais, la pile se remplit complètement et l'ordinateur est forcé de s'arrêter. (C'est de là que vient le nom du site populaire, Stack Overflow.)

Alors, en revenant à ma pratique infinie du piano, comment pouvons-nous empêcher mes mains de tomber ?

C'est là que nous voyons l'importance d'un terme que vous avez peut-être déjà entendu : **le cas de base**.

Dans les fonctions récursives, le cas de base est l'objectif que vous essayez d'atteindre ou la tâche que vous cherchez à accomplir. Le rôle du cas de base est de dire à votre fonction quand elle doit s'arrêter.

Dans notre analogie, cet objectif peut être de s'entraîner jusqu'à ce que je sois fatigué.

```
practicePiano(person){   if (tired(person)){ //Quand je suis enfin fatigué    console.log("Devinez que vous pouvez faire une pause maintenant...");    return ;  //Cela sortira de la fonction et arrêtera l'appel récursif  }
```

```
  practiceScales(person);    practiceChords(person);
```

```
//Magie récursive ici !
```

```
  practicePiano(person);}
```

```
//Maintenant, quand nous appelons cela ici... je ne m'entraînerai encore et encore que jusqu'à ce que je sois fatigué
```

```
practicePiano('Michael');
```

C'est là que la plupart des développeurs rencontrent des problèmes. Bien que notre analogie actuelle de la pratique du piano soit une simplification, elle souligne un point extrêmement important : et si je ne me fatiguais jamais de m'entraîner ? Alors le cas de base que nous avons écrit ne résoudrait pas notre erreur « Maximum call stack size exceeded ».

Avant de plonger directement dans le codage, il est important de prendre le temps de réfléchir à toutes les situations possibles qui peuvent — et devraient — arrêter nos appels récursifs.

En tant que développeur, vous écrivrez des algorithmes complexes, qui peuvent prendre des entrées variables et utiliser la récursivité pour atteindre un objectif.

Vous pouvez développer un cas de base ou plusieurs cas de base que vous croyez être atteints par votre appel récursif. Mais ce ne sera peut-être pas toujours le cas.

Considérez le cas de mon homologue cyborg :

```
practicePiano(person){   if (tired(person)){    console.log("Devinez que vous pouvez faire une pause maintenant...");    return ;    }
```

```
 if (handsFallOff(person)){   console.log("Allez voir un médecin pour cela");    return ; }
```

```
  practiceScales(person);    practiceChords(person);
```

```
  practicePiano(person);}
```

```
practicePiano('Cyborg-Michael'); 
```

```
//Cyborg-Michael ne se fatigue jamais//Ses mains ne tombent jamais//Retour à la pratique éternelle...
```

Étant donné cela, il est important de toujours s'assurer que vous êtes minutieux dans le développement de vos cas de base et que votre fonction se comporte de manière à ce qu'un cas de base soit toujours atteint.

Dans notre exemple, un cas de base logique serait de pouvoir jouer un morceau comme la 5ème de Beethoven.

En refactorisant notre code, nous avons maintenant :

```
practicePiano(person, song){   if (tired(person)){    console.log("Devinez que vous pouvez faire une pause maintenant...");    return ;    }
```

```
 if (handsFallOff(person)){   console.log("Allez voir un médecin pour cela");    return ; }
```

```
 if (song(person)){   console.log("Excellent travail ! Il est temps d'apprendre cela à la guitare !");    return ; }
```

```
  practiceScales(person);    practiceChords(person);
```

```
  practicePiano(person, song);}
```

```
practicePiano('Cyborg Michael', BeethovenFifth); 
```

```
//La version cyborg de moi ne se fatigue jamais//Mes mains ne tombent jamais//Mais, étant un cyborg... je peux apprendre la 5ème de Beethoven assez rapidement
```

C'est la puissance des solutions récursives. Avec quelques lignes de code, je peux accomplir une tâche pour laquelle je ne sais peut-être pas combien d'étapes cela prendra. J'ai peut-être besoin de 100 sessions de pratique, alors que mon moi cyborg n'aura besoin que de 5, mais cette solution fonctionnera toujours pour nous deux.

Alors, pour résumer, rappelez-vous simplement ce qui suit :

1. La récursivité vous permet de répéter facilement une tâche pour accomplir un objectif.
2. Le ou les cas de base doivent être suffisamment complets pour permettre à votre fonction récursive d'atteindre une conclusion (et de ne pas fonctionner indéfiniment).
3. La récursivité vous aide à garder votre code DRY (encore une fois, vous entendrez souvent cet acronyme, alors rappelez-vous qu'il signifie « Ne vous répétez pas » — oops, je viens de le faire !)

### Plus de récursivité à venir

Nous approfondirons la récursivité dans ma prochaine série sur les structures de données. Lors de cette plongée en profondeur, nous verrons comment vous pouvez commencer à utiliser l'[analyse de la complexité temporelle](https://medium.freecodecamp.com/time-is-complex-but-priceless-f0abd015063c#.huo7yk6wy) et la récursivité dans votre code quotidien. Nous travaillerons également sur diverses méthodes de boucles pour comprendre pourquoi il peut être préférable d'utiliser l'une plutôt que l'autre.

À titre de remarque, l'un des sujets que nous n'avons pas eu l'occasion d'aborder ici sont les problèmes de [factorielle](https://en.wikipedia.org/wiki/Factorial). Les problèmes de factorielle sont ceux où l'on trouve des solutions récursives appliquées le plus souvent, car ils nécessitent une itération récursive un certain nombre de fois défini. Vous pouvez trouver plus de détails sur la résolution des problèmes de factorielle dans cet [article génial](https://www.sitepoint.com/recursion-functional-javascript/) de SitePoint.

Voici quelques ressources supplémentaires pour vous aider :

[**Khan Academy sur la Récursivité**](https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursion)   
[_Apprenez gratuitement les maths, l'art, la programmation informatique, l'économie, la physique, la chimie, la biologie, la médecine, la finance… www.khanacademy.org](https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursion)[**SparkNotes : Qu'est-ce que la Récursivité ? : Qu'est-ce que la Récursivité ?**](http://www.sparknotes.com/cs/recursion/whatisrecursion/section1.rhtml)  
[_Un résumé de Qu'est-ce que la Récursivité ? dans 's Qu'est-ce que la Récursivité ?. Apprenez exactement ce qui s'est passé dans ce chapitre, scène, ou… www.sparknotes.com](http://www.sparknotes.com/cs/recursion/whatisrecursion/section1.rhtml)[**mybrainishuge/recursion-prompts**](https://github.com/mybrainishuge/recursion-prompts)  
[_recursion-prompts - Dépôt de prompts à résoudre en utilisant la récursivité github.com](https://github.com/mybrainishuge/recursion-prompts)

De plus, merci à [Yara Tercero](https://yctercero.github.io/) pour avoir aidé à éditer cela.