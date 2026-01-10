---
title: Créez un environnement de bureau sain avec ces directives efficaces de révision
  de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-10T19:49:05.000Z'
originalURL: https://freecodecamp.org/news/create-a-sane-office-environment-with-these-effective-code-review-guidelines-1d99ae2bdd47
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tmWNK9yElTaVKFqq_5C6qQ.png
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Créez un environnement de bureau sain avec ces directives efficaces de
  révision de code
seo_desc: 'By Sandor Dargo

  In my new team, we are working on several guidelines, rules and process improvements.
  Why do we think these are so important? If things are well-documented, it’s easier
  for a newcomer to start delivering value. It reduces the possibil...'
---

Par Sandor Dargo

Dans ma nouvelle équipe, nous travaillons sur plusieurs directives, règles et améliorations de processus. Pourquoi pensons-nous qu'elles sont si importantes ? Si les choses sont bien documentées, il est plus facile pour un nouveau venu de commencer à apporter de la valeur. Cela réduit les possibilités d'erreurs pour tout le monde. Cela élimine de nombreuses possibilités de conflits. Et nous savons tous que [l'on ne peut pas gagner une dispute](http://lesswrong.com/lw/j6o/according_to_dale_carnegie_you_cant_win_an), donc nous devrions les éviter à tout prix.

Pour une vision plus détaillée de l'importance des directives, veuillez consulter [cet article](https://medium.com/@SandorDargo/zuckerbergs-gray-t-shirt-and-coding-guidelines-caef9079ba7e). Je le revisiterai bientôt, d'ailleurs.

Cette fois, je vais me concentrer sur les revues de code et sur les directives correspondantes.

### L'objectif de la révision de code

Examiner une pull request est une tâche importante et délicate. À mon avis, elle est au moins aussi importante que l'écriture du code. De plus, examiner le code de quelqu'un d'autre n'est pas seulement une tâche technique, c'est aussi une tâche humaine. Cela donne la plupart de sa délicatesse.

Alors, laissez-moi commencer par la règle la plus importante que vous devriez toujours avoir à l'esprit lorsque vous commencez à examiner une pull request ou lorsque vous ouvrez une révision que vous avez reçue :

**Aucun commentaire ne doit être personnel. Aucun commentaire ne doit être fait sur l'auteur ou le réviseur. Une révision doit toujours porter sur le code !**

L'objectif d'une révision de code est d'améliorer le code, de détecter les bugs avant la fusion et la livraison, et d'améliorer la maintenabilité d'une base de code donnée.

![Image](https://cdn-media-1.freecodecamp.org/images/iwBJmQjVw5bLuAarwiexTTHpdZWktPyW-WEx)
_Le code doit être rigoureusement vérifié_

### Éléments à vérifier dans une révision de code

Examiner le code est difficile, et c'est une tâche très large. Selon mes patrons, je suis considéré comme un bon réviseur de code. Pourtant, je pense que mon efficacité pourrait être grandement améliorée. Je pense que suivre des listes de contrôle, dans la plupart des cas, peut être d'une grande aide.

Maintenant, évidemment, certaines de ces listes de contrôle et/ou tâches seront spécifiques à un langage. Cependant, les revues sont aidées par les mêmes concepts existant dans plusieurs langages de code.

Ces listes sont principalement là pour vous donner quelques idées, car elles sont loin d'être complètes. N'hésitez pas à les utiliser, à les mettre à jour, à les personnaliser, ou simplement à les laisser vous inspirer pour créer de nouvelles listes.

Je pense qu'un réviseur ne devrait pas toutes les utiliser, mais peut-être seulement quelques-unes. Mais si vous avez des listes de contrôle séparées, il est facile de partager les tâches.

Toutes les listes de contrôle ne sont pas là pour être utilisées pour toutes les revues de code. Si la pull request est une correction de bug vraiment petite, corrigeant simplement un décalage d'un dans une condition, elle ne nécessitera pas de vérifier la conception de tout le domaine.

### Types de listes de contrôle

#### Liste de contrôle du processus complet

Celle-ci se concentre sur certaines caractéristiques fondamentales d'une pull request. Assurez-vous que les nouveaux commits ne cassent pas la compilation ou les tests. Votre pipeline d'intégration continue devrait s'en occuper, mais au cas où ce ne serait pas le cas, n'oubliez pas de le vérifier. Sinon, vérifiez ce qui suit :

* Des nouveaux tests unitaires/de non-régression sont-ils ajoutés ?
* Y a-t-il de nouveaux avertissements du compilateur ?
* Le changement a-t-il un sens fonctionnellement ?
* Y a-t-il beaucoup de dépendances ?
* Les messages de commit sont-ils clairs ?

#### Liste de contrôle des principes SOLID (conception orientée objet)

Afin de vérifier la santé de la conception, il vaut la peine de passer en revue les principes SOLID. Il est utile de développer ces éléments en sous-listes, ce qui aide à vérifier chaque principe :

* Principe de responsabilité unique
* Principe ouvert/fermé
* Principe de substitution de Liskov
* Principe de ségrégation des interfaces
* Principe d'inversion des dépendances

#### Liste de contrôle de sécurité

Votre application peut être critique en termes de sécurité ou non. Dès qu'elle est piratée une fois ou qu'elle échoue à cause d'une entrée désordonnée, elle deviendra critique. Cette liste de contrôle devrait être fortement dépendante du langage (je vous donne une pour le C++). La liste est principalement extraite de cette [conférence sur les pratiques de programmation sécurisée à la NDC Security Conference en 2018](https://www.youtube.com/watch?v=Jh0G_A7iRac)

* Les entrées externes sont-elles gérées correctement ?
* Les interfaces de style C sont-elles utilisées ?
* L'opérateur `new` est-il utilisé de manière superflue au lieu de l'allocation sur la pile ?
* Y a-t-il beaucoup de calculs de taille (sujets aux erreurs) ?
* Les pointeurs sont-ils beaucoup utilisés ?
* Les shared_ptrs sont-ils beaucoup utilisés ?
* Y a-t-il des threads ?

#### Liste de contrôle des meilleures pratiques de test

J'espère que nous sommes tous d'accord pour dire que les tests font partie du travail d'un développeur. Si nous avions une discussion sur les tests, elle porterait sur les différentes façons de les faire, et non sur le fait de les faire ou non.

La mauvaise nouvelle est qu'il n'y a pas une seule méthode qui convienne à tous. Pourtant, je vous conseillerais de suivre le cycle du développement piloté par les tests. La bonne nouvelle est que, sur un projet, il y a au moins une compréhension commune de ce qui doit être fait.

S'il n'y en a pas, intervenez et plaidez pour les tests, rassemblez des articles et des études, et convainquez l'équipe. Vous serez beaucoup plus respecté.

Voici quelques points à clarifier concernant la partie test :

* Y a-t-il assez de tests unitaires ?
* Y a-t-il assez de tests de non-régression ?
* Les tests testent-ils une seule chose ?
* Ont-ils des assertions ? (Un test peut avoir plusieurs assertions, mais logiquement, ils affirment une seule chose)
* Sont-ils lisibles ?
* Comment les dates sont-elles utilisées ? (Fixes vs. générées)

#### Liste de contrôle de la lisibilité du code

Nous — développeurs — sommes tous des auteurs. Si nous faisons un travail impeccable, [notre code se lira comme une prose](https://www.goodreads.com/quotes/7029841-clean-code-is-simple-and-direct-clean-code-reads-like). Je ne dis pas que vous devriez toujours atteindre cet objectif pour toute la base de code, mais vous devriez viser cela.

Le réviseur de code a une grande responsabilité ici. Si vous lisez une pull request, veuillez réfléchir aux questions suivantes :

* Les noms sont-ils significatifs ?
* Les classes/fonctions sont-elles assez petites ?
* Le code "se lit-il comme une prose" ?
* Le code est-il bien formaté ?
* Y a-t-il du code dupliqué ?

#### Liste de contrôle de la gestion des ressources, alias [RAII](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization)

Celle-ci est plutôt spécifique au langage. Ce n'est pas seulement pour le C++, mais principalement. Si vous êtes un développeur C++ et que vous avez déjà lutté contre des pointeurs pendants, des fuites de mémoire et des vidages de mémoire désagréables, alors vous savez ce que je veux dire.

Il peut être vraiment difficile pour un non-expert de repérer ces problèmes. Mais suivre une liste de contrôle utile peut vous aider à la fois à pointer les lignes problématiques et à développer l'expertise RAII.

* La propriété des objets est-elle clarifiée ?
* Les objets sont-ils correctement détruits/la mémoire est-elle correctement désallouée ?
* Les nouveaux champs sont-ils correctement gérés ?
* Les champs sont-ils correctement initialisés dans les constructeurs ?
* Les opérateurs de comparaison sont-ils mis à jour ?

![Image](https://cdn-media-1.freecodecamp.org/images/g5hd9nbvxcs2wVXZN-AmvzcLiYZeqQ9xUq2Q)
_La révision est pour améliorer la qualité et s'éduquer mutuellement_

### Le code de conduite pour les réviseurs de code

Comme indiqué précédemment, commenter le code de quelqu'un d'autre est aussi une tâche humaine, alors soyez gentil avec vos collègues développeurs. Voici quelques conseils. Les suivre diminuera considérablement les chances que les développeurs pleurent ou se lancent des chaises dans le bureau. (Mais je n'ai jamais vu ce dernier cas — jusqu'à présent…)

#### À ne pas faire

* Ne faites pas référence à des traits personnels et ne jugez pas (par exemple, abstenez-vous de dire que vous/votre code est stupide…)
* Ne faites pas de demandes (au moins mettez un "s'il vous plaît" et expliquez pourquoi vous demandez un changement)
* Ne soyez pas sarcastique, même si vous êtes copains. D'autres réviseurs/lecteurs pourraient trouver certains commentaires inappropriés
* Ne dites jamais jamais, ni toujours. Il y aura toujours des exceptions. Alors traitez cette règle avec soin…
* Évitez la propriété sélective du code (c'est-à-dire, n'utilisez pas "mon", "pas mon", "vôtre"…)

#### À faire

* Posez des questions.
* Demandez des clarifications.
* Soyez explicite. Rappelez-vous que les gens ne comprennent pas toujours vos intentions en ligne.
* Cherchez à comprendre la perspective de l'auteur.
* Si les discussions deviennent trop philosophiques ou académiques, déplacez la discussion hors ligne
* Identifiez des moyens de simplifier le code tout en résolvant toujours le problème.
* Communiquez quelles idées vous ressentent fortement et lesquelles vous ne ressentent pas. Si vous exprimez simplement votre préférence, dites que c'est seulement votre préférence.
* Éduquez. Si vous suggérez quelque chose, partagez des preuves de pourquoi c'est mieux (comme des articles, des études, des livres, etc.).

![Image](https://cdn-media-1.freecodecamp.org/images/f1wn8KRB4zrj1SyBz3iMmvkGrv66l7hjr3Bb)
_Nous, les développeurs, sommes tous des auteurs_

### Règles pour les auteurs

* Soyez humble et honnête à propos du code soumis. Les erreurs arrivent tous les jours, et le processus est là pour vous soutenir.
* Rappelez-vous que vous ne devriez pas le prendre personnellement. La révision porte sur le code, pas sur vous.
* Expliquez pourquoi le code existe.
* Suivez les directives.
* Cherchez à comprendre la perspective du réviseur.
* Soyez reconnaissant pour les suggestions alternatives et gardez la discussion technique. Essayez d'apprendre de différentes perspectives.

### Appel à l'action

* Faites des revues de code approfondies. Vous apprendrez beaucoup, tout comme vos collègues développeurs.
* Soulignez l'importance des revues de code appropriées dans vos équipes, et si nécessaire, éduquez vos collègues sur la façon de réviser le code.
* Consultez et étoilez [ce dépôt](https://github.com/sandordargo/code-review-guidelines) où j'ai rassemblé quelques listes de contrôle et idées. N'hésitez pas à contribuer et à ajouter ce que vous avez trouvé important !

_Cet article a été initialement publié sur [mon blog](http://sandordargo.com/blog/2018/03/28/codereview-guidelines)._