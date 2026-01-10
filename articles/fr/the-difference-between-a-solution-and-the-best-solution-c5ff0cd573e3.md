---
title: Toute Solution Contre la Meilleure Solution
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-25T03:06:47.000Z'
originalURL: https://freecodecamp.org/news/the-difference-between-a-solution-and-the-best-solution-c5ff0cd573e3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wdzErOdqjTzh-ot9MTuEig.jpeg
tags:
- name: Design
  slug: design
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: teaching
  slug: teaching
- name: Web Development
  slug: web-development
seo_title: Toute Solution Contre la Meilleure Solution
seo_desc: 'By Sam Galizia

  A couple of months ago, I was searching for resources to help me improve my coding
  skills. It didn’t take long before I stumbled upon Free Code Camp.

  This open source community hosts a website dedicated to helping people learn how
  to c...'
---

Par Sam Galizia

Il y a quelques mois, je cherchais des ressources pour m'aider à améliorer mes compétences en codage. Cela n'a pas pris longtemps avant que je ne tombe sur [Free Code Camp](http://www.freecodecamp.com).

Cette communauté open source héberge un site web dédié à aider les gens à apprendre à coder, avec un accent sur le développement web. Les étudiants peuvent s'inscrire gratuitement et apprendre le HTML, le CSS, le JavaScript, la visualisation de données, et même des technologies back-end comme Node.js.

L'objectif ultime est de donner aux gens de la pratique en codage en construisant des projets, et finalement d'acquérir une expérience réelle en travaillant avec des organisations à but non lucratif.

Quand j'ai commencé leur programme, j'ai rapidement parcouru beaucoup des leçons de HTML et CSS, car j'avais déjà un peu d'expérience avec ces technologies.

Une fois arrivé aux sections sur JavaScript, cependant, j'ai ralenti et j'ai pris mon temps. Puis j'ai atteint la section Basic Algorithm Scripting.

Maintenant, je programme depuis un certain nombre d'années, en utilisant quelques langues différentes, et je pensais honnêtement que cela allait être une promenade de santé.

J'ai découvert à la dure que ces défis sont un peu plus difficiles qu'ils n'en ont l'air. Ils ne sollicitent pas seulement votre cerveau pour les solutions, mais encouragent également à utiliser différentes fonctionnalités du langage JavaScript.

J'ai passé un peu de temps à travailler sur quelques défis de base, mais inévitablement, je me suis retrouvé bloqué.

#### Une Lumière dans l'Obscurité

Quand nous sommes bloqués sur des problèmes, généralement notre première pensée est de chercher des ressources et d'essayer de comprendre ce que nous faisons de travers.

Heureusement, Free Code Camp a fourni une ressource incroyable pour vous aider lorsque vous êtes bloqué, comme le [Free Code Camp Wiki](https://github.com/FreeCodeCamp/freecodecamp/wiki). J'aime me référer à cette ressource comme une "lumière dans l'obscurité" car, juste au moment où vous pensez abandonner et jeter l'éponge, cette torche brillante éclaire soudainement l'obscurité autour de vous !

Le wiki de Free Code Camp est une ressource inestimable alors que vous travaillez sur les défis de projets front-end. Chaque article du wiki contient une explication du défi, et même des indices et plusieurs solutions possibles.

De nombreuses fois, lorsque je me suis retrouvé bloqué, je visitais le wiki et je lisais simplement un ou deux indices pour m'assurer que j'étais sur la bonne voie. Je n'ai jamais vraiment regardé les solutions avant d'avoir résolu les problèmes moi-même. Je voulais conquérir les défis par moi-même !

Au cours de ce parcours, j'ai également découvert le grand réseau de salons de discussion de Free Code Camp où vous pouvez traîner avec d'autres campeurs (étudiants de Free Code Camp) et discuter de ce qui ne va pas avec votre code.

Parmi les nombreuses personnes que j'ai rencontrées dans les salons, une personne s'est avérée être une ressource inestimable pour moi. [Justin Richardsson](http://gitter.im/hallaathrad) m'a aidé avec l'un des défis sur lesquels je luttais et, sans qu'il le sache, m'a mis sur la voie de la réalisation de l'étape manquante dans mon processus d'apprentissage.

#### Attention à Votre Marche ! Il Manque Quelque Chose !

Justin expliquait une erreur dans mon code, et il a commencé à parler d'une meilleure façon d'aborder le problème. Il m'a guidé à travers le processus en me posant des questions, me guidant vers la découverte des étapes par moi-même au fur et à mesure.

Finalement, j'ai compris ce qu'il disait, et j'ai eu une révélation. J'avais résolu les défis et trouvé une solution, mais était-ce la meilleure solution ?

Il s'est avéré que je ne tirais pas pleinement parti des meilleures pratiques et des concepts de base. Cette découverte m'a amené à croire que mes solutions n'étaient en fait pas la meilleure façon de résoudre les défis, et que quelque part en cours de route, j'avais manqué une étape.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vh0V9wTj7wMm9HMX40FAzQ.jpeg)
_L'étape manquante._

L'idée de cette étape manquante se résume à faire une chose :

> Une fois que vous avez trouvé une solution fonctionnelle au problème, vous devez réévaluer votre code et déterminer s'il peut être amélioré.

L'amélioration pourrait être aussi simple que d'utiliser moins de variables temporaires, ou moins de boucles. JavaScript a de nombreuses fonctionnalités utiles qui — lorsqu'elles sont vraiment comprises — peuvent être des outils puissants pour une résolution de problèmes plus efficace. Laissez-moi vous donner un exemple de ce que je veux dire.

Un défi implique une fonction prenant une chaîne de caractères, et vous devez inverser la chaîne et la retourner.

Cette première solution montre comment de nombreux débutants tentent de résoudre ce défi. La première solution n'est pas fausse, et il est acceptable de faire cela pendant que vous comprenez le flux de ce qui doit se passer. Regardons la première solution maintenant :

```
function reverseString(str) {  var splitString = str.split('');  var reversedString = splitString.reverse();  var finalString = reversedString.join('');   return finalString;}
```

Maintenant, en regardant le code ci-dessus, il n'y a rien de fondamentalement faux. Cette solution au défi est techniquement valide, car elle passe les vérifications requises, mais à ce stade, nous devons évaluer si c'est vraiment la meilleure façon de résoudre cela.

La première façon dont je remarque que je peux améliorer mon code est de supprimer toutes les variables inutiles.

Une chose que je pense que de nombreux étudiants oublient en apprenant JavaScript est que vous n'avez pas besoin de créer une nouvelle variable pour chaque modification d'une variable existante.

Lorsque vous écrivez une expression, le côté droit de l'expression est calculé avant son exécution. C'est un concept important à comprendre, car cela signifie que nous pouvons faire ceci à la place :

```
function reverseString(str) {  str = str.split('');  str = str.reverse();  str = str.join('');  return str;}
```

Regardez ça ! En exploitant les fonctionnalités intégrées du langage, nous avons déjà amélioré la lisibilité de notre code et supprimé toutes les variables inutiles.

Il y a encore plus que nous pouvons faire pour améliorer cette fonction. Nous avons utilisé des expressions et des affectations, mais prenons cela une étape plus loin. Je vais apporter une dernière modification à cette fonction :

```
function reverseString(str) {  return str.split('').reverse().join('');}
```

Dans cette troisième solution, nous avons supprimé les multiples affectations à _str_ et avons utilisé une fonctionnalité très importante, _l'enchaînement de fonctions_.

Il semble que de nombreux étudiants, en apprenant, oublient certaines de ces fonctionnalités importantes qui rendent honnêtement notre code beaucoup plus lisible et produisent des solutions plus correctes.

Les trois solutions ci-dessus sont techniquement correctes, mais la plupart des développeurs considéreraient probablement la troisième solution comme la meilleure pour ce problème. Cela est dû au fait que nous n'utilisons pas plus de ressources que nécessaire. Par conséquent, la fonction peut être exécutée rapidement, sans gaspiller de cycles CPU ou d'autres ressources. Certes, lorsque nous parlons de son exécution plus rapide, nous parlons relativement à d'autres fonctions en cours de traitement.

Je peux déjà entendre les critiques dire qu'une meilleure solution est subjective, et que d'autres personnes pourraient penser qu'une autre solution est la meilleure. Je ne prétends pas qu'il n'y a qu'une seule façon de résoudre ces défis.

Clairement, il existe de nombreuses façons différentes de résoudre les défis, mais une fois que nous avons trouvé une solution, nous devons nous assurer que nous le faisons _efficacement_. La différence entre la première solution et la troisième solution est très claire. En termes d'utilisation de cette stratégie particulière pour résoudre le défi, la troisième solution est clairement meilleure que la première.

#### Quelle est Notre Meilleure Solution ?

Justin m'a recommandé d'aider en contribuant mes nouvelles connaissances au wiki de Free Code Camp. J'étais très enthousiaste à l'idée d'aider à contribuer, et ce soir-là, j'ai travaillé sur ma première contribution.

J'avais réalisé que certains des articles du wiki montraient comment résoudre un défi, mais pas nécessairement la ou les meilleures façons de les résoudre. Je me suis fixé pour objectif d'essayer de contribuer du mieux que je pouvais, afin de pouvoir aider à enseigner aux autres cette étape manquante lorsqu'ils cherchaient de l'aide. Quelque part dans notre processus d'enseignement, nous avons oublié qu'il ne s'agit pas seulement de résoudre un problème, mais aussi d'enseigner les meilleures pratiques en cours de route.

Je pense sincèrement que lorsque nous aidons les gens avec les défis sur FreeCodeCamp, nous ne devrions pas seulement nous concentrer sur l'enseignement des concepts de base. Lorsque les gens viennent vers ceux d'entre nous qui ont plus d'expérience, nous devrions les aider à adopter les meilleures pratiques.

Il est important d'enseigner les concepts et pas seulement le code. En aidant les gens à comprendre les concepts, de nombreuses fois, ils découvriront par eux-mêmes qu'il existe une meilleure façon de résoudre un problème.

Une telle expérience que j'ai eue impliquait un gentleman cherchant de l'aide pour un défi. Après avoir examiné son code, je pouvais dire qu'il savait ce qu'il voulait faire, mais qu'il avait du mal à y parvenir efficacement.

Typiquement, plus nous avons de code dans une fonction, plus cela devient compliqué. Parfois, nous finissons par rendre les choses beaucoup trop compliquées, comme ce campeur l'avait fait.

J'ai procédé en offrant de l'aide sous la forme de deux indices. Je lui ai expliqué deux concepts qu'il avait probablement oubliés, en utilisant de très petits extraits de code qui n'étaient pas pertinents pour la solution réelle.

En lisant le deuxième indice que je lui avais donné, il m'a demandé avec excitation d'attendre une minute car il pensait savoir quoi faire. Après une minute ou deux, il a posté avec enthousiasme qu'il avait résolu le défi et a publié son code !

Ce campeur était si excité d'avoir enfin compris qu'il voulait revenir en arrière et retravailler ses autres solutions avant de continuer, car il savait maintenant une meilleure façon de les résoudre.

Cela montre exactement pourquoi il est si important d'enseigner les concepts et les meilleures pratiques. Je suis convaincu que le campeur se souviendra de ces concepts et, espérons-le, les transmettra à quelqu'un d'autre dans le besoin !

Alors, quelle est notre meilleure prochaine étape ? Enseigner aux gens apprenant à coder comment le faire correctement et efficacement en utilisant les meilleures pratiques et les concepts de base. Ce n'est que lorsque nous pourrons dire en toute confiance que nous enseignons les meilleures façons de coder et que nous inculquons les meilleures pratiques aux étudiants que nous pourrons dire que nous avons résolu le problème de l'étape manquante dans le processus d'apprentissage.