---
title: Comment Google effectue les revues de code – Conseils d'assurance qualité tirés
  de la documentation de Google
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-01-14T18:09:46.000Z'
originalURL: https://freecodecamp.org/news/what-google-taught-me-about-code-reviews
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Google.png
tags:
- name: code review
  slug: code-review
- name: Google
  slug: google
- name: QA
  slug: qa
- name: Quality Assurance
  slug: quality-assurance
seo_title: Comment Google effectue les revues de code – Conseils d'assurance qualité
  tirés de la documentation de Google
seo_desc: "A code review, sometimes called code Quality Assurance, is the practice\
  \ of having other people check your code after you write it. \nCode reviews bring\
  \ many benefits to the process of writing and delivering software:\n\nEnsures consistency\
  \ through your ..."
---

Une revue de code, parfois appelée assurance qualité du code, est la pratique consistant à faire vérifier votre code par d'autres personnes après l'avoir écrit. 

Les revues de code apportent de nombreux avantages au processus d'écriture et de livraison de logiciels :

* Assure la cohérence dans votre base de code.
* Enseigne à tous les membres de la revue (aide au transfert de connaissances).
* Crée une sensibilisation contextuelle concernant ce qui pourrait affecter d'autres parties de l'équipe.
* Aide à éviter les ruptures de builds.
* Apporte un regard neuf sur une modification de code pour rechercher des optimisations et des simplifications dans la modification.
* Favorise la qualité et aide à s'assurer que personne n'a oublié ou manqué quoi que ce soit.

Google possède 1 918 dépôts sur [leur GitHub](https://github.com/google) dans plusieurs langues, et encore plus qui ne sont pas open source.

L'un de leurs codebases est partagé par plus de 25 000 Googlers, et a généralement [40 000 commits](https://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext) par jour (16 000 changements humains, et 24 000 par des systèmes automatisés). Chaque jour, il doit servir environ 800 000 requêtes par seconde pendant les heures de pointe.

Google a publié ses pratiques d'ingénierie, alors voyons comment ils effectuent les revues de code à leur échelle, avec autant de commits par jour.

Google fait référence aux changements dans leurs codebases sous le nom de **CLs** (change lists). C'est simplement une unité de travail / un morceau de code passant en revue. 

# Comment se préparer aux revues de code

Tout d'abord, avant même de penser au processus de revue de code, essayez de vous concentrer sur **qui** effectuera la revue. Essayez de choisir un expert en la matière. Choisissez quelqu'un qui est familier avec cette base de code ou cette partie de la base de code. 

Parfois, cela peut même signifier avoir différentes personnes examiner différentes parties du code. Mais moins [de 25 % des revues de code chez Google ont plus d'un relecteur.](https://sback.it/publications/icse2018seip.pdf)

Obtenir une réponse rapide de quelqu'un est également important. Pour éviter les goulots d'étranglement et la surcharge des individus, il suffit de mettre les relecteurs en copie du changement pour qu'ils le révise à leur convenance s'ils le souhaitent.

# Comment effectuer des revues de code rapides

Les revues de code doivent être effectuées rapidement. La durée **maximale** pour une revue doit être d'un jour ouvré.

Pourquoi cette urgence ? J'ai personnellement eu des QA qui ont parfois pris des semaines ou plus.

* **Cela devient un blocage.** Bien que l'auteur du code passe à un nouveau travail, de nouveaux changements commencent à former un arriéré, et les retards peuvent s'accumuler sur des semaines ou des mois.
* **Les développeurs se sentent frustrés.** Si le relecteur demande des changements majeurs mais ne répond que tous les 3 jours, c'est frustrant pour le développeur qui travaille sur ce changement. Mais avec des réponses rapides, chaque fois que vous avez besoin d'une explication précise de ce que vous devez faire, la frustration s'estompe.
* **La qualité du code peut se dégrader.** Si vos revues sont toujours lentes, les développeurs sont moins susceptibles de faire des nettoyages de code, des travaux de refactorisation ou des améliorations générales du code ("Si mon relecteur ne répondra pas avant 4 jours, quel est même l'intérêt ?"), et la qualité du code soumis dans les revues est plus susceptible de baisser.

La principale raison pour laquelle les revues de code peuvent être rapides est qu'elles sont petites. Plutôt que d'envoyer un CL de 1 000 lignes, elles sont séparées en plusieurs CL – en poussant 10 changements plus petits de 100 lignes par exemple.

Google a également des urgences où des changements de code doivent être faits rapidement pour résoudre des problèmes majeurs en production. Dans ces cas, la qualité du code est relâchée. Cette revue devrait immédiatement devenir la première priorité du relecteur. Il y a quelques exemples d'urgences auxquelles Google a été confronté [ici](https://www.freecodecamp.org/news/what-is-a-software-post-mortem/) si vous êtes curieux.

## Normes de revue de code de Google

La règle clé que Google met en avant est :

**Les relecteurs devraient généralement approuver un changement une fois qu'il améliore définitivement la santé globale du code, même s'il n'est pas parfait.**

Le point clé que Google semble souligner est que le code parfait n'existe pas. Si cela l'améliore, c'est suffisant. 

C'est définitivement un acte d'équilibriste entre quelque chose étant meilleur, et **combien** mieux cela pourrait être. Si vous pourriez ajouter plus de feedback pour faire des améliorations significatives, il peut être nécessaire de faire plus de travail sur le code.

## Ce que les Googlers recherchent dans les revues de code

Lors des revues de code, Google se concentre sur ces éléments selon leur [documentation des pratiques d'ingénierie](https://google.github.io/eng-practices/review/reviewer/looking-for.html) :

> **Conception** : Le code est-il bien conçu et approprié pour votre système ? Ce changement appartient-il à votre base de code, ou à une bibliothèque ? S'intègre-t-il bien avec le reste de votre système ?  
>   
> **Fonctionnalité** : Le code se comporte-t-il comme l'auteur l'a probablement prévu ? La manière dont le code se comporte est-elle bonne pour ses utilisateurs ? Principalement, nous nous attendons à ce que les développeurs testent bien les CL pour qu'ils fonctionnent correctement au moment où ils arrivent à la revue de code.   
>   
> **Complexité** : Le code pourrait-il être simplifié ? Un autre développeur serait-il capable de comprendre et d'utiliser facilement ce code lorsqu'il le rencontrera à l'avenir ? Est-il sur-ingénierisé pour son cas d'utilisation actuel ?  
>   
> **Tests** : Le code a-t-il des tests automatisés corrects et bien conçus ? Les tests échoueront-ils réellement lorsque le code est cassé ? Commenceront-ils à produire des faux positifs ? Chaque test fait-il des assertions simples et utiles ?  
>   
> **Nommage** : Le développeur a-t-il choisi des noms clairs pour les variables, les classes, les méthodes, etc. ?  
>   
> **Commentaires** : Les commentaires sont-ils clairs et utiles ? Assurez-vous que les commentaires expliquent **pourquoi** quelque chose est fait, plutôt que comment.  
>   
> **Style et cohérence** : Le code suit-il nos [guides de style](http://google.github.io/styleguide/) ?  
>   
> **Documentation** : Le développeur a-t-il également mis à jour la documentation pertinente ?

Google a des guides de style pour plusieurs langues comme [C++](https://google.github.io/styleguide/cppguide.html), [Swift](https://google.github.io/swift/), [HTML/CSS](https://google.github.io/styleguide/htmlcssguide.html), [Lisp](https://google.github.io/styleguide/lispguide.xml), [JavaScript](https://google.github.io/styleguide/jsguide.html) et [plus encore.](https://google.github.io/styleguide/)

Avoir un document auquel tout le monde peut se référer aide à standardiser le code. Cela aide également à clarifier les attentes dans le processus de revue.

## Comment les Googlers effectuent les revues de code

Il existe un processus en trois étapes pour la revue de code dans les pratiques d'ingénierie de Google. Voici une liste des choses que vous devriez couvrir si vous deviez effectuer une revue :

1. Obtenir un aperçu de haut niveau du changement
2. Examiner les principales parties du changement
3. Parcourir le reste du code, dans un ordre sensé

Examinons chaque étape plus en détail.

## 1. Obtenir un aperçu de haut niveau du changement de code

Regardez la description/le résumé du changement de code. Tout cela a-t-il du sens ? Par exemple, si quelqu'un modifie une base de code qui sera supprimée la semaine prochaine, remettez en question le changement _courtoisement_, et expliquez pourquoi le changement ne semble plus nécessaire. 

C'est inefficace si les gens passent du temps sur un travail qui n'est pas réellement nécessaire, alors jetez un coup d'œil à votre cycle de développement et voyez pourquoi cela pourrait se produire. Plus vous pouvez détecter ces problèmes tôt, mieux c'est.

Pour obtenir un aperçu de haut niveau du code, vous pouvez vouloir scanner brièvement les composants du code pour voir comment tout cela fonctionne ensemble. 

Si vous voyez un problème architectural sérieux ou quelque chose de gravement incorrect, vous devriez partager vos observations immédiatement à ce stade. Même si vous n'avez pas le temps de revoir chaque autre élément de la revue. Revoir le reste pourrait bien finir par être une perte de temps si les problèmes architecturaux sont suffisamment graves. 

Outre cela, il y a 2 raisons majeures pour lesquelles vous devriez envoyer vos commentaires de revue immédiatement : 

* Les Googlers envoient souvent un changement par e-mail, puis commencent immédiatement un nouveau travail basé sur ce changement. Si le changement en revue a besoin d'ajustements sérieux, ils pourraient construire quelque chose qui doit être significativement modifié.
* Les grands changements apportés au CL peuvent prendre un certain temps à terminer. Les développeurs ont tous des délais et il est courtois d'essayer de les aider à les respecter en leur permettant de commencer le retravail dès que possible.

## 2. Examiner les principales parties du changement de code

Une fois que vous avez eu un aperçu, passez en revue les parties "principales" du changement.

Trouvez le ou les fichiers qui sont centraux pour le CL. Souvent, il y a un fichier qui a le plus grand nombre de changements, et c'est la pièce majeure du CL.

Consacrez la plupart de votre attention à l'examen de ces pièces. Cela fournit un contexte à toutes les petites pièces, et rend généralement l'examen plus rapide. 

Si le CL est trop grand pour que vous puissiez avoir un bon aperçu et comprendre le flux, c'est un bon signe que le développeur devrait diviser son CL en changements plus petits.

## 3. Parcourir le reste du code, dans un ordre sensé

Une fois que vous avez un bon aperçu du changement, il est temps de creuser dans les détails et d'aller fichier par fichier. 

Chaque relecteur fait généralement cela différemment. Certains suivent l'ordre que le contrôle de version leur présente et d'autres choisissent un ordre particulier. Choisissez ce qui a du sens pour vous. Il est important de simplement tout passer en revue, et de ne rien manquer.

### Passer en revue chaque ligne de code

Ne manquez pas ou ne survolez pas les détails importants. Parfois, il peut y avoir des fichiers de configuration, ou du code généré que vous pouvez scanner brièvement à la recherche d'irrégularités. Mais votre travail ici est d'être très minutieux et de scruter soigneusement le code. 

Assurez-vous de penser aux bugs, aux conditions de course, aux approches alternatives, à la concision, à la lisibilité, et ainsi de suite.

Si vous ne pouvez pas comprendre le code, il est très probable que d'autres développeurs ne puissent pas non plus, et vous devriez demander au développeur de le clarifier.

### Comprendre le contexte

Souvent, le logiciel de contrôle de version ne montre que les lignes modifiées. Mais il est important de lire les lignes avant et après, ou le fichier entier, pour vous assurer de comprendre exactement ce que le changement fait.  

Vous ne verrez peut-être que quelqu'un ajouter 2 blocs `if` de plus dans un changement. Mais si vous regardez le contexte, vous verrez peut-être que le bloc `if` `else` contient maintenant 15 `if` différents à l'intérieur. Vous pouvez alors rejeter le changement de code et améliorer correctement la qualité du code dans ce domaine, plutôt que de l'aggraver.

Rappelez-vous que la dégradation du code se produit lentement, avec chaque changement qui est apporté. Notre objectif principal est de nous assurer que la qualité évolue constamment vers le haut, et que nous ne reculons jamais.

## **Comment les Googlers écrivent les commentaires sur le code** 

Google a des sections spécifiques couvrant comment faire des [revues de code courtoises et respectueuses](https://chromium.googlesource.com/chromium/src/+/master/docs/cr_respect.md). Cela n'est pas en opposition avec le fait d'être clair et aussi utile que possible pour le développeur. La règle d'or ici est de faire des commentaires sur le _code_ et non sur le développeur. 

## Ce qu'il faut faire :

#### 

> **Demandez pourquoi** : Si ce n'est pas clair pourquoi l'auteur fait les choses d'une certaine manière, n'hésitez pas à demander pourquoi il a fait un changement particulier. Ne pas savoir est acceptable, et demander "Pourquoi" laisse une trace écrite qui aidera à répondre à cette question à l'avenir. (Et parfois, "Je suis curieux, pourquoi avez-vous décidé de le faire de cette manière ?" peut aider l'auteur à reconsidérer sa décision.)  
>   
> **Trouvez une fin** : Si vous aimez que les choses soient bien ordonnées, il est tentant de passer en revue un code encore et encore jusqu'à ce qu'il soit parfait, le prolongeant plus longtemps que nécessaire. C'est décourageant pour le destinataire, cependant. Gardez à l'esprit que "LGTM" ne signifie pas "Je garantis de mon âme immortelle que cela ne échouera jamais", mais "cela me semble bien". Si cela semble bien, passez à autre chose. (Cela ne signifie pas que vous ne devriez pas être minutieux. C'est une question de jugement.) Et s'il y a des refactorisations plus importantes à faire, déplacez-les vers un nouveau CL. ([Source](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/cr_respect.md))

## Ce qu'il ne faut pas faire

> **N'utilisez pas de langage extrême ou très négatif** : Veuillez ne pas dire des choses comme "aucune personne sensée ne ferait jamais cela" ou "cet algorithme est terrible", que ce soit à propos du changement que vous passez en revue ou du code environnant. Bien que cela puisse intimider le relecteur pour qu'il fasse ce que vous voulez, ce n'est pas utile à long terme - ils se sentiront incapables, et il n'y a pas beaucoup d'informations pour les aider à s'améliorer. "C'est un bon début, mais cela pourrait nécessiter quelques travaux" ou "Cela nécessite quelques nettoyages" sont des manières plus gentilles de le dire. Discutez du code, pas de la personne.  
>   
> **Ne faites pas de bikeshedding** : Demandez-vous toujours si cette décision compte _vraiment_ à long terme, ou si vous imposez une préférence subjective. Cela fait du bien d'avoir raison, mais seulement l'un des deux participants peut gagner à ce jeu. Si ce n'est pas important, acceptez de ne pas être d'accord, et passez à autre chose. ([Source](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/cr_respect.md))

Rappelez-vous que les revues de code peuvent parfois tendre vers la recherche de problèmes ou de discussions avec le code et non des éloges.

Si votre relecteur a répondu à vos commentaires, ou s'il a fait une optimisation ou un code intelligent que vous aimez, remerciez-le. Dites que vous aimez l'approche / la manière dont il a résolu un problème. 

Inversement, remerciez le relecteur s'il explique clairement ce qu'il veut et répond rapidement à vos questions.

J'ai eu des revues où les relecteurs ont laissé de gros commentaires expliquant quelque chose que j'avais mal compris et je me souviens encore de qui c'était et de ce qu'ils ont dit.

## Comment gérer les résistances dans les revues de code

Parfois, le développeur qui reçoit la revue peut ne pas être d'accord avec les changements que vous proposez. Voici comment gérer cela.

### Considérez qu'ils pourraient avoir raison

Parfois, le développeur est plus proche du code et de son fonctionnement, et il pourrait avoir raison. S'ils ont raison, passez à autre chose de ce point de discussion et laissez ce code tel quel.

Mais s'ils n'ont pas raison, ou s'ils ont mal compris quelque chose, vous devriez insister sur le changement. Répondez à ce que le développeur vous a initialement contesté, et expliquez votre raisonnement courtoisement. 

Les améliorations de la qualité du code tendent à se faire par petites étapes incrémentielles, et la revue est l'un des moyens par lesquels cela se produit. Insistez sur l'amélioration du code, même si cela signifie un travail supplémentaire pour le développeur.

### Essayez d'éviter "Je corrigerai cela plus tard..."

L'un des problèmes les plus courants dans les revues n'est pas que les gens ne sont pas d'accord sur la nécessité du changement de code, mais plutôt qu'ils veulent le faire sous un autre ticket ou le faire plus tard. Donc, si vous passez cette revue, ils vous assurent qu'ils suivront plus tard et corrigeront les problèmes.

En général, _suivre plus tard_ arrive rarement. Cela ne signifie pas qu'il y a quelque chose qui ne va pas avec le développeur ou son éthique de travail. Mais il est facile d'oublier, de voir les priorités changer, ou même de se perdre dans leur file d'attente de travail. 

Insistez pour que le travail soit fait maintenant. Il n'y a pas de gain fantastique réel à fusionner des changements dans la base de code que vous devez immédiatement corriger. Vous ajoutez simplement une dette technique qui _pourrait_ être suivie plus tard, ou pourrait être oubliée. Corriger de nombreux tickets plus tard est un moyen facile pour que la qualité baisse.

La seule exception à cela est les [urgences](https://google.github.io/eng-practices/review/emergencies.html), qui impliquent les bugs de la plus haute priorité que Google traite où il y a quelque chose de gravement incorrect. Cela pourrait être des services qui tombent en panne, ou des erreurs qui font planter les pages des gens en production.

Il y a naturellement une volonté de fusionner les changements dès que possible, et la revue pourrait accepter une qualité légèrement inférieure, avec une correction de suivi étant immédiatement écrite. Le point principal est que le premier changement supprime l'urgence, et le second changement la corrige _correctement._

# **Conclusion**

J'espère que cela a expliqué quelques concepts utiles que Google utilise dans son processus de revue de code. J'ai écrit cela pour mieux l'ancrer dans mon propre esprit, et j'étais curieux de savoir comment d'autres entreprises gèrent le processus de QA. 

J'ai trouvé qu'il y a plusieurs points que je peux retenir et appliquer aux revues que je conduis.

Le document auquel je me suis référé tout au long de cet article peut être trouvé [ici](https://google.github.io/eng-practices/review/reviewer/).

Je partage mes écrits sur [Twitter](https://twitter.com/kealanparr) si vous avez aimé cet article et souhaitez en voir plus.