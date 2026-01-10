---
title: Comment concevoir des API qui ne sont pas nulles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-23T13:27:45.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-anupcowkur-how-to-design-apis-that-dont-suck-922d864365c9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wSKrrW74dUcgu42OqwA1BQ.png
tags:
- name: api
  slug: api
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment concevoir des API qui ne sont pas nulles
seo_desc: 'By Anup Cowkur

  Other developers actually have to use the APIs you design. So don’t let those APIs
  suck. If you don’t want hordes of angry programmers to descend on your home in the
  middle the night with torches and pitchforks, you need to design them...'
---

Par Anup Cowkur

D'autres développeurs doivent effectivement utiliser les API que vous concevez. Alors ne les laissez pas être nulles. Si vous ne voulez pas que des hordes de programmeurs en colère débarquent chez vous au milieu de la nuit avec des torches et des fourches, vous devez les concevoir correctement.

Voici quelques conseils de conception que j'ai glanés auprès de collègues au fil des ans. Ils s'appliquent à tous les types d'API : bibliothèques open source, SDK internes, modules ou même une seule classe.

### Soyez explicite

![Image](https://cdn-media-1.freecodecamp.org/images/DSOySAAyesVKzC6ELKzkEp91o6a88RmSBYRl)

Ceci est peut-être le conseil le plus important. Si vous avez une méthode appelée `getUser` et qu'elle provoque un effet secondaire sans être explicite à ce sujet, cela peut entraîner beaucoup de problèmes.

Ne modifiez pas l'état mutable partagé sans être explicite à ce sujet. Si j'appelle `getUser`, je m'attends à ce qu'elle retourne simplement un utilisateur, pas à ce qu'elle incrémente le `user_id` de `1` en cours de route. Vous pourriez envisager d'utiliser des [structures de données immuables](https://speakerdeck.com/anupcowkur/the-mutable-state-monster-and-how-to-defeat-it) également.

Encodez autant de comportement que possible dans le nom de la méthode/classe/module dans des limites raisonnables. N'attendez pas des utilisateurs qu'ils plongent dans le code source pour découvrir un comportement caché que le nom ne révèle pas. Vous vous épargnerez beaucoup de peine à long terme.

### Gardez la surface de votre API petite

![Image](https://cdn-media-1.freecodecamp.org/images/4KXGTI1YlSKWcRgDnZxKPbSL7ujqj9smEqYG)

Personne n'aime les programmes gonflés. Moins vous exposez d'API pour accomplir le travail, meilleure est l'expérience pour tout le monde.

Quelqu'un demande-t-il vraiment cette nouvelle API que vous voulez écrire ? Vous pouvez probablement la reporter jusqu'à ce que ce soit réellement un problème que quelqu'un veut résoudre.

Dans certains environnements de programmation comme Android, il existe des limites strictes sur le nombre total de méthodes que les applications peuvent avoir, donc c'est peut-être quelque chose que vous devez garder à l'esprit si vous ciblez ces plateformes.

L'implémentation anticipative est responsable de quantités honteuses d'heures de programmation gaspillées. Pratiquez le [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it).

### Réduisez le code passe-partout

![Image](https://cdn-media-1.freecodecamp.org/images/9yJ0ghRN0COLWY7IbyQMJsgtpeWKhWhxNdl4)

Gérez autant de détails d'implémentation que possible en interne pour réduire la charge sur les clients. Moins le consommateur a à faire, moins le nombre de bugs que vous aurez à gérer sera élevé.

Il y a aussi la question de l'esthétique. Devoir écrire du code passe-partout peut ruiner une API par ailleurs parfaitement bonne et rendre le code du consommateur laid. Nous aimons tous le code propre, n'est-ce pas ? Facilitez la tâche à vos consommateurs pour garder le code concis et propre lors de l'utilisation de votre API.

### Réduisez les dépendances

![Image](https://cdn-media-1.freecodecamp.org/images/rSBUK82V1tiyfrJa6UslDdJKsUdbGV8IqMv7)

Essayez de garder votre code aussi autonome que possible. Plus vous avez de dépendances, plus cela peut causer de problèmes potentiels dans le code consommateur en aval.

Si vous voulez vraiment cette belle fonctionnalité d'un autre module, essayez de l'extraire et n'incluez que ce dont vous avez besoin.

C'est toujours un acte d'équilibriste entre la réutilisation du code et le couplage serré. Vous devrez faire ce choix. Si cette fonctionnalité est petite, il peut être utile de la réimplémenter vous-même.

### Retournez des états d'erreur significatifs

![Image](https://cdn-media-1.freecodecamp.org/images/-RVX-RiOcYT95tqhRYJMnmKwyyYb-QfL830G)

Je pourrais râler toute la journée sur la façon dont `null` est une construction inutile dans de nombreux cas. Cela signifie littéralement _rien_.

« Hé module, donne-moi un utilisateur »

« Non. Voici _rien_ à la place »

Cela ne me donne aucune information sur ce qui a mal tourné et ce que je peux faire pour améliorer la situation. Si nous avons plutôt une manière documentée d'exprimer les états d'erreur attendus dans notre domaine de problème, comme `Error.USER_NOT_CREATED` ou `Error.USER_DELETED`, cela me donne beaucoup plus de données exploitables et m'aide à déboguer le problème.

Les messages d'erreur doivent également suivre les mêmes directives. _Vous devez vous connecter avant de continuer_ est beaucoup mieux que _LOL ! Quelque chose a mal tourné._

### Réservez les exceptions pour les cas vraiment exceptionnels

![Image](https://cdn-media-1.freecodecamp.org/images/UMLr3G0JKXjEM6ulyGiXurHZu4SL0ojg7YsO)

Si votre langage ne dispose pas d'exceptions, réjouissez-vous ! Les types `Either` et leurs cohortes trouvés dans les langages fonctionnels sont bien meilleurs pour fournir des états d'erreur significatifs de toute façon.

Les exceptions tendent à être fortement abusées dans le monde Java. Les exceptions sont destinées à gérer des cas _vraiment exceptionnels_. Ne vous attendez-vous vraiment pas à ce que `getUser` ne trouve pas un utilisateur ? Ne lancez pas de `UserNotFoundException`. Retournez plutôt un état d'erreur approprié.

Si cependant il y a un échec réel, il est toujours préférable d'échouer rapidement.

Comme le dit [Jake Wharton](https://www.freecodecamp.org/news/https-medium-com-anupcowkur-how-to-design-apis-that-dont-suck-922d864365c9/undefined) :

> _« La seule chose pire qu'un programme qui plante est celui qui ne plante pas et continue dans un état indéterminé. »_

### Documentez tout

![Image](https://cdn-media-1.freecodecamp.org/images/r7Hic26NyTbMq9ARW2ysPhyJXu8cua-loJvR)

La documentation est ennuyeuse. Et comme beaucoup de choses ennuyeuses, elle est essentielle. Une bonne documentation vous sauvera la santé mentale. Vous éviterez les questions constantes des consommateurs de votre API, et cela seul vaut son poids en or.

Une bonne documentation doit comprendre :

1. Un aperçu de haut niveau de l'ensemble du module et de son fonctionnement
2. Javadocs, Heredocs, Rdocs ou autres de ses méthodes et protocoles publics
3. Du code exemple montrant comment l'utiliser

Toutes les abstractions ne nécessitent pas le même niveau de documentation. Une petite classe n'a pas besoin de code exemple par exemple.

La documentation doit également être évolutive. Si vous recevez beaucoup de questions posant la même chose, vous pouvez l'ajouter à la documentation pour les futurs consommateurs.

Trop de documentation est également une perte de temps, car c'est un autre actif que vous devez maintenir à jour. Elle n'a aucune valeur si personne ne l'utilise.

Une documentation ciblée et adéquate, cependant, est toujours utile.

### Écrivez des tests

![Image](https://cdn-media-1.freecodecamp.org/images/v5fWTuryjAfWKGSzs9ocX6vY2WTRiEgDtSqz)

Les tests sont la preuve de la correction, de la documentation et du code exemple, le tout en un. Ils fournissent une immense valeur lors du refactoring et vous permettent de vous déplacer rapidement avec confiance lorsque vous changez des choses.

Les consommateurs qui veulent creuser plus profondément dans votre implémentation peuvent toujours lire les tests pour comprendre davantage l'intention et le comportement interne de votre code. La documentation ne peut pas capturer tout, et c'est là que les tests aident.

« Pourquoi écrire de la documentation du tout alors si j'ai des tests ? » pourriez-vous demander. Au risque d'utiliser une analogie ténue, si la documentation est le _manuel de l'utilisateur_ de votre API, alors les tests sont la _référence des instructions opcode x86_.

### Rendez-le testable

![Image](https://cdn-media-1.freecodecamp.org/images/YP5cCfvl-1LjWNiFJwKICv286lVV9Xa86rk-)

Tester votre propre code est une chose. Écrire des API qui permettent à ceux qui les utilisent de tester leur code facilement en est une autre. Les développeurs qui se soucient des tests seront rebutés par les API qui rendent difficile le mock/stub dans les cas de test.

Vous pouvez utiliser des options de configuration pour les versions de debug et de production lorsque cela est applicable. Les choses ont souvent besoin de se comporter un peu différemment dans les environnements d'Intégration Continue/Déploiement Continu que dans la production. Tenez compte de cela.

### Permettez le choix de l'utilisateur

![Image](https://cdn-media-1.freecodecamp.org/images/kl9YBnKLsBLCe97pV4YC5buUS7USGSrsRhHJ)

Tous les consommateurs ne voudront pas utiliser vos API de la même manière. Certains peuvent la vouloir synchrone. D'autres peuvent préférer des callbacks asynchrones, des futures, des promesses ou des observables Rx.

Permettez aux consommateurs la capacité de choisir ce qu'ils veulent autant que possible. Plus votre API peut s'intégrer facilement dans leur environnement de programmation et système existant, plus il est probable que les gens l'utiliseront.

### Ne permettez pas trop de choix à l'utilisateur

![Image](https://cdn-media-1.freecodecamp.org/images/Sozy1eQKs8QRsMuvW0Q6H4Dh65qLLbNSktyz)

Ne donnez pas aux consommateurs tant de choix qu'ils finissent par être paralysés par l'analyse. Efforcez-vous toujours de fournir des valeurs par défaut sensées. La plupart du temps, votre API sera utilisée d'une certaine manière. Faites en sorte que les valeurs par défaut se comportent de cette manière.

Les API doivent encourager un comportement canonique. Ne laissez pas les consommateurs modifier un état aléatoire dans votre module si cela ne fait pas partie du contrat de l'API. Si vous exposez un comportement étrange non intentionnel, vous pouvez être sûr qu'il sera utilisé un jour, engendrant des conséquences imprévues.

Soyez opiniâtre. Ne perdez pas de vue en donnant trop d'options. Équilibrer la bonne quantité d'opinion contre la bonne quantité de flexibilité prend de la pratique et de l'expérience. En cas de doute, privilégiez moins de choix.

### Conclusion

Concevoir des API est un art. Espérons que les conseils décrits ici vous aideront à écrire un meilleur code. J'ai probablement oublié beaucoup d'autres choses, mais celles-ci m'ont bien servi. Vivez et apprenez.

_Si vous avez aimé cela, cliquez sur le ? ci-dessous. Je remarque chacun d'eux et je suis reconnaissant pour chacun d'eux._

_Pour plus de réflexions sur la programmation, suivez-moi afin d'être informé lorsque j'écrirai de nouveaux articles._