---
title: Comment gérer la dette technique et préserver votre santé mentale
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-29T19:57:11.000Z'
originalURL: https://freecodecamp.org/news/tame-your-tech-debt-by-refactoring-more-often-fcc34dd24a33
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s7y24bN2-3GcYzPsm2kgtQ.jpeg
tags:
- name: agile
  slug: agile
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment gérer la dette technique et préserver votre santé mentale
seo_desc: 'By Gabriel Colombo

  When was the last time you found yourself working in a file containing 7,000+ lines
  of code?

  I’m doing exactly that at this very moment. Refactoring some functionality from
  a legacy project along with writing this article.

  Trust me...'
---

Par Gabriel Colombo

Quand était la dernière fois que vous vous êtes retrouvé à travailler sur un fichier contenant 7 000+ lignes de code ?

Je fais exactement cela à l'instant même. Je refactorise certaines fonctionnalités d'un projet hérité tout en écrivant cet article.

Croyez-moi, c'est pénible.

Malheureusement, c'est une réalité pour des tonnes de développeurs. Les projets deviennent incontrôlables pour diverses raisons. Un changement particulier peut ne pas correspondre au processus actuel ou devenir inefficace à long terme.

Ces situations conduisent souvent les développeurs à implémenter des solutions temporaires pour maintenir les choses en marche. Il n'y a rien de mal à cela.

Le problème commence à s'aggraver lorsque ces solutions sont réutilisées dans différentes fonctionnalités.

Réutiliser une solution sans comprendre les conditions dans lesquelles elle a été développée, et quel problème elle devait résoudre, ne fait qu'augmenter votre dette technique.

### Qu'est-ce que la dette technique

L'énoncé suivant reflète ma définition préférée de la dette technique :

> Un ensemble de compromis intentionnels faits lors des différentes étapes de développement d'une application.

Mais que signifie-t-il ?

Lors de la création d'un nouveau produit, des décisions importantes doivent être prises à chaque étape. Chaque décision a un poids particulier qui affecte le processus de développement. Des compromis doivent être faits.

« Devons-nous sacrifier les normes de codage pour pouvoir livrer plus rapidement ? »

« Comment créer cette fonctionnalité sans sur-ingénierie ? Elle n'a pas besoin d'une architecture complète pour l'instant, mais nous devrons l'améliorer plus tard. »

À mesure que nous prenons plus de décisions, ces compromis commencent à impacter le processus de développement. Des problèmes de maintenance surgissent et les nouvelles fonctionnalités ne sont pas livrées aussi rapidement qu'avant.

C'est le moment où la motivation s'en va.

J'ai travaillé sur des projets basés sur la prémisse suivante :

« Nous allons passer à une technologie différente et tout sera abandonné. Pour l'instant, tant que cela fonctionne, ne vous inquiétez pas trop des normes de codage. »

Si cela ne vous semble pas trop grave, regardons cela sous un autre angle :

« Nous allons tous mourir à un moment donné, alors tant que vous êtes en vie, faites ce que vous voulez et ne vous inquiétez pas des conséquences. »

Vous voyez ce que je veux dire ?

Chaque projet devrait avoir un ensemble de normes, afin que tout le monde sache comment ils doivent faire les choses. **Ces normes devraient toujours compter tant qu'il y a des gens qui travaillent sur le projet.**

### Pourquoi refactoriser ?

Lorsque j'étais développeur junior à mon premier emploi, nous étions une équipe de 5, donc tout le monde devait porter plusieurs casquettes à la fois.

J'ai commencé à développer à la fois le front et le back-end avec Laravel. Il a fallu du temps pour apprendre le framework et comprendre les [PSRs](http://www.php-fig.org/psr/) (PHP Standards Recommendations), puisque je n'avais jamais traité cela auparavant. Pendant cette période, une partie du code que j'ai écrit ne répondait pas aux normes.

Chaque lundi, je revenais en arrière et je regardais le code que j'avais écrit la semaine précédente et tout répondait aux normes. Mon patron refactorisait chaque semaine, et parfois quotidiennement si quelque chose semblait outrageant.

Cette refactorisation constante rendait la structure du projet quelque peu imprévisible. Les choses se cassaient de temps en temps, surtout lorsque nous travaillions sur différentes branches. Oh bien, vous savez ce qu'ils disent :

![Image](https://cdn-media-1.freecodecamp.org/images/0iU0eHDKl7NNOdmhioFGlayO3n7MeYXt7jk8)
_Assurez-vous simplement d'avoir une infrastructure stable. ([source](http://mashable.com/2014/04/30/facebooks-new-mantra-move-fast-with-stability/" rel="noopener" target="_blank" title="))_

Un jour, nous déjeunions ensemble et j'ai décidé de demander pourquoi il refactorisait notre code si souvent. Sa réponse était quelque chose comme ceci :

« Si je ne refactorise pas, personne ne le fera. »

« Nous avons une très petite équipe, mais elle finira par grandir. »

« Si vous allez dans notre base de code et que vous la trouvez désordonnée et hors normes, vous ne prendrez probablement pas le temps de faire les choses correctement, vous ajouterez simplement une autre instruction if et passerez à autre chose, mais si tout est propre et bien rangé, vous aurez l'impression de faire quelque chose de mal en ne suivant pas les normes. »

Cette conversation a changé ma façon de voir les choses, non seulement en tant que développeur, mais aussi en tant qu'individu. Pour cela, je suis reconnaissant.

James Q. Wilson et George L. Kelling ont exploré le concept général de son explication avec la Théorie des Vitres Brisées.

[**Théorie des vitres brisées — Wikipédia**](https://en.wikipedia.org/wiki/Broken_windows_theory)
[_La théorie des vitres brisées est une théorie criminologique de l'effet de normalisation et de signalisation du désordre urbain et..._en.wikipedia.org](https://en.wikipedia.org/wiki/Broken_windows_theory)

Leur théorie présente le concept suivant :

_Un environnement ordonné et propre, qui est maintenu, envoie le signal que la zone est surveillée et que le comportement criminel n'est pas toléré. Inversement, un environnement désordonné, qui n'est pas maintenu (vitres brisées, graffitis, déchets excessifs), envoie le signal que la zone n'est pas surveillée et que le comportement criminel a peu de risques d'être détecté._

Cela a tellement de sens lorsqu'il est lié à la programmation. Si personne ne s'en soucie, du code de mauvaise qualité est livré et le projet devient de plus en plus difficile à maintenir à long terme.

Connaissant cette petite histoire, examinons quand envisager de refactoriser votre code.

#### Quand refactoriser votre base de code

La refactorisation constante assure la cohérence, une productivité plus élevée et un meilleur contrôle sur la base de code.

Vous devriez envisager de refactoriser votre code si :

* Le projet continuera à fonctionner pendant longtemps.
* Vous avez des problèmes de maintenance. (Difficulté à trouver et résoudre des problèmes ou à apporter des modifications à une fonctionnalité particulière).
* Certaines fonctionnalités sont incohérentes (Le même composant se comporte différemment sur différentes pages).
* Il y a trop de duplication de code.
* Vos fonctions ont beaucoup trop de logique métier.

#### Quand résister à l'envie de refactoriser

* Le projet ne grandira pas et n'a pas besoin de beaucoup de maintenance.
* Vous manquez de tests automatisés et ne prévoyez pas de les implémenter.
* Vous voulez migrer vers une technologie différente parce que c'est à la mode.
* Lorsque la refactorisation consommera trop de temps.

### Conclusion

![Image](https://cdn-media-1.freecodecamp.org/images/EP0oxUGvbtOdroU3x2jMQjeLz6tm2GaF3ZE1)
_FAITES-LE !_

La dette technique est un énorme problème dans tout projet, surtout dans les projets hérités. Plus tôt nous agissons pour la garder sous contrôle, meilleure sera la qualité finale.

La refactorisation constante vous aide à réduire les dépendances et à augmenter la maintenabilité. La base de code devient plus facile à tester et à comprendre.

Pour commencer, essayez de repérer certaines des situations listées ci-dessus et réfléchissez à la manière de les améliorer. Voici un excellent [article](https://medium.com/web-engineering-vox/how-to-write-solid-code-that-doesnt-suck-2a3416623d48) pour vous aider à démarrer.

Merci d'avoir lu ! J'espère que vous avez apprécié cet article.

Si cela vous aide d'une manière ou d'une autre, aidez-moi à faire passer le mot en le partageant :)

Oh ! Dites-moi aussi bonjour sur Twitter — [@gcolombo](https://twitter.com/gcolombo_)