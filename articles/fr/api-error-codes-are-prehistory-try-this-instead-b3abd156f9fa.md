---
title: Les codes d'erreur d'API sont préhistoriques — essayez ceci à la place
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T09:36:18.000Z'
originalURL: https://freecodecamp.org/news/api-error-codes-are-prehistory-try-this-instead-b3abd156f9fa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*29vCdubMr2uQk5laP7Lmiw.jpeg
tags:
- name: api
  slug: api
- name: Computer Science
  slug: computer-science
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Les codes d'erreur d'API sont préhistoriques — essayez ceci à la place
seo_desc: 'By Pakal de Bonchamp

  A cautionary tale

  Once upon a time, a young girl observed her mother, who was unwrapping a freshly
  bought piece of beef for roasting. The mother cut the extremities of the meat out.

  “Mommy, why do you do that?” the young girl ask...'
---

Par Pakal de Bonchamp

### Une histoire édifiante

Il était une fois, une jeune fille qui observait sa mère, qui déballait un morceau de bœuf fraîchement acheté pour le rôtir. La mère coupait les extrémités de la viande.

« Maman, pourquoi fais-tu cela ? » demanda la jeune fille.

« Cela donne un meilleur goût », répondit la mère, en mettant le repas au four.

« Comment cela ? »

« Je ne me souviens pas, va demander à ta grand-mère, elle m'a appris tous ces types de trucs et astuces. »

L'enfant était curieuse et courut à la maison voisine de sa grand-mère.

« Grand-maman, sais-tu pourquoi couper les côtés du rôti de bœuf le rend meilleur ? »

« Cela doit être lié à la circulation du jus », répondit la grand-mère.

« Ne peut-on pas simplement percer des trous avec une fourchette à la place ? »

« Ma mère les a toujours préparés ainsi, et elle était certainement une grande cuisinière. »

L'enfant n'était pas seulement curieuse mais aussi persévérante, et courut à la maison où vivait son aïeule. Elle raconta ce que sa mère et sa grand-mère lui avaient dit, et répéta sa question.

L'aïeule éclata de rire.

« J'ai toujours coupé les extrémités de mon rôti de bœuf, mais seulement parce que mon four était bien trop petit pour un morceau entier. »

Cette petite histoire, qui existe en [d'innombrables variations](https://www.snopes.com/fact-check/grandmas-cooking-secret/), fait un point important sur la vie humaine. Les vieilles habitudes ont la vie dure, même lorsqu'elles n'ont plus de sens depuis des décennies (si tant est qu'elles en aient jamais eu). Et l'informatique, bien qu'évoluant à un rythme rapide, est assez sujette à ce type de tradition nuisible.

![Image](https://cdn-media-1.freecodecamp.org/images/ISagFl1mcQBDqHbbHGrgUZDMmwy9E7FQOtjV)

### Gestion des erreurs

Prenons la gestion des erreurs, par exemple. Nous sommes profondément habitués aux codes de statut HTTP, aux petits "errnos" Unix, aux longs codes d'erreur Windows... et nos API sont remplies de nombres personnalisés, indiquant des problèmes avec les entrées, ou avec des erreurs opérationnelles SQL, ou avec des permissions d'accès...

Les premiers langages de programmation de bas niveau — incluant C et Fortran — avaient des types de données très rudimentaires. C'est pourquoi ils géraient les erreurs comme de simples entiers, qu'ils pouvaient comparer, utiliser dans des switch-case, rechercher comme indices de tableau, et transmettre sans douleur. Et c'est pourquoi ils ont fini par utiliser 0 (booléen False) pour indiquer tous les succès, et des entiers non nuls (booléen True) pour indiquer des erreurs — quelque chose de peu intuitif pour les mortels ordinaires.

Mais que attendons-nous des erreurs dans nos langages modernes, de haut niveau, au quotidien ? Qu'elles soient :

* **explicites**, afin que nous sachions ce qu'elles signifient sans demander à tout le web à chaque fois
* **deeply hierarchical**, afin que nous puissions affiner les cas d'erreur sans casser le logiciel actuel, et revenir à des traitements génériques lorsque des erreurs trop spécifiques sont rencontrées
* **contextualisées**, afin que des données supplémentaires puissent accompagner l'erreur, et détailler ce qui s'est exactement mal passé et pourquoi

C'est ainsi que les exceptions sont implémentées dans de nombreux langages modernes. Il existe des hiérarchies de classes avec (espérons-le) des significations claires. Chacune a différents attributs d'instance dans différentes branches de ces hiérarchies, par exemple des noms de fichiers, des noms de champs, et des erreurs du système d'exploitation d'origine. Et ces instances traînent avec elles des tonnes d'informations, y compris des tracebacks et leurs variables locales par cadre.

Mais lorsque l'erreur doit traverser les frontières de ce processus spécifique, de ce langage spécifique ? Les codes d'erreur sont parmi les pires supports pour cela.

Que signifie "Erreur 0x29273363833" ? Vous n'en avez aucune idée. Vous ne pouvez pas subdiviser cette erreur en cas plus précis. Si vous voulez plus d'informations contextuelles, vous devrez les chercher ailleurs.

Et vous avez peu d'indices sur ce que pourrait être le code d'erreur parent le plus proche. Il est vrai que certains systèmes préconisent des comportements de repli rudimentaires — par exemple, si vous rencontrez une erreur HTTP 478 inconnue, vous êtes censé la traiter comme une erreur HTTP 400. Mais c'est encore un peu trop grossier pour de nombreux cas, et une fois que vous avez utilisé tous les nombres d'une classe d'erreur, vous êtes malchanceux.

### **Alors, que propose-je ?**

Il suffit de mapper les types d'exceptions à leurs représentations compatibles JSON les plus proches.   
Ce qui se trouve être... des séquences d'identifiants.

Mesdames et messieurs, je vous présente, un ensemble de **slugs de statut** :

* ["Exception", "LookupError", "KeyError"]
* "error|functional|invalid_input|missing_value"
* "error|technical|connectivity|mysql.database_unreachable"
* ["success"]
* ["success", "instance_found_in_cache"]

Comme vous pouvez le voir, que nous utilisions des listes ou des chaînes n'a pas beaucoup d'importance ; même le terme "slug" ne doit pas être pris trop rigidement, avoir des traits de soulignement ou des lettres majuscules n'est pas nocif.

Les **messages importants à retenir** sont que ces slugs sont :

* assez explicites
* assez faciles à mapper aux exceptions spécifiques au langage
* assez faciles à faire correspondre dans le dispatcher de gestion des erreurs.

Les points doivent être réservés pour qualifier, et ainsi différencier, les exceptions de même nom fournies par différents packages. Un exemple ici est "cuteforms.Invalid" vs "validator.Invalid".

La cerise sur le gâteau est que les slugs de statut peuvent être utilisés pour distinguer les cas de succès également, comme la famille "HTTP 2XX" l'a préconisé pour le web.

Voici donc le premier point que je voulais faire : **utilisez des slugs de statut pour annoncer les résultats des opérations**.

**La gestion des erreurs est au cœur même de la robustesse du logiciel et d'une expérience utilisateur agréable, elle mérite donc plus que des types de données de niveau assembleur**. Arrêtons simplement d'utiliser une mauvaise distribution d'erreurs basée sur des entiers, sur des slugs uniques, ou — pire encore — sur des booléens.

![Image](https://cdn-media-1.freecodecamp.org/images/swBxJBfvHeKOw87J-k1doVYZAi0FYdJGPl6N)
_Toujours une meilleure gestion des erreurs que "Une erreur s'est produite, veuillez vérifier les logs"...

Le deuxième point que je voulais faire concernant la gestion des erreurs est : **soyez ambitieux**.

De nombreux protocoles définissent des structures d'erreur tronquées — "si c'est suffisant pour moi, c'est suffisant pour les autres". Et les développeurs finissent par ajouter leur propre système de gestion des erreurs. Parfois, les réponses SUCCESS du protocole initial sont remplies de leurs propres structures d'erreur, lorsque les réponses ERROR ne laissent aucune place à la personnalisation (je vous regarde, XML-RPC).

Donc, si vous finissez, un jour, par avoir à spécifier votre propre format d'erreur — ce qui est toujours dommage, mais parfois inévitable — **pensez grand**.

Que attendons-nous d'un format de réponse ?

* Bien sûr, nous avons besoin de slugs de statut, pour voir précisément quel type de succès ou d'erreur s'est produit.
* Nous pouvons également avoir besoin de messages traduits pour l'affichage de l'interface utilisateur.
* Très probablement, nous avons également besoin de messages non traduits, car ils sont beaucoup plus pratiques à rechercher dans les codes sources, ou à traduire côté frontend.
* Nous avons besoin de place pour des arbres de données spécifiques au statut, afin que toutes les informations pertinentes puissent être fournies de manière traitables par machine.
* Nous avons probablement également besoin de support pour des structures de données multiples — ou plutôt récursives —, comme lorsque plusieurs champs d'un formulaire web ont chacun leur propre raison d'être rejetés.
* Nous devons peut-être transmettre des succès partiels, par exemple lorsque toutes les données du compte utilisateur n'ont pas pu être récupérées depuis les répertoires. Nous devons peut-être transmettre des échecs partiels, par exemple lorsque une réponse faisant autorité n'a pas pu être récupérée, mais que certaines données en cache sont retournées au cas où elles vous aideraient.

Voici un exemple de structure StatusPack (presque) universelle :

> {  
>  status_slugs : liste de slugs pour la distribution des succès/erreurs, champ obligatoire  
>  data: arbre de données avec des informations contextuelles (résultats, champs d'entrée invalides...)  
>  traceback : uniquement pour le mode dev, peut inclure des cadres avec des variables locales  
>  nested_statuses: liste optionnelle de structures StatusPack  
>  message_translated: chaîne affichable  
>  message_untranslated: chaîne ou paire [modèle de chaîne, paramètres]  
> }

Cette structure devrait couvrir les cas d'utilisation mentionnés ci-dessus, grâce à la malléabilité fournie par le champ "nested_statuses".

Si vous traitez avec des **microservices**, l'enchaînement de ces packs de statut, et leur affichage correct côté utilisateur — **surtout le traceback** — pourrait vous faire économiser des jours d'investigation de logs.

Et si vous voulez obfusquer vos erreurs, alors très bien. Mais il n'est pas nécessaire de spécifier vous-même les codes d'erreur. Créez simplement des **hachages** de vos "status_slugs" et générez automatiquement la liste complète des erreurs disponibles en introspectant votre base de code.

![Image](https://cdn-media-1.freecodecamp.org/images/IjhQTfo7JkC9BOqM1fDtlEfpWs9nNIv0ipHk)
_Ce sentiment lorsque votre code gère tous les types d'erreurs utilisateur et réseau sans faille_

Le dernier point que je souligne est : **soyez gentil avec les consommateurs d'API.**

Assurez-vous que vos consommateurs **sachent** lorsqu'une erreur se produit. Assurez-vous que vos consommateurs **sachent** également quoi faire, surtout de manière programmatique, dans ce cas.

* Les erreurs silencieuses sont l'antichambre de l'Enfer. Supprimer un compte inexistant **doit** retourner une erreur. Mais fournissez un paramètre "strict=False" doux à de telles opérations, afin que les utilisateurs puissent effectuer des appels sans importance sans s'embarrasser d'erreurs.
* Avoir une "ValueError" sur un champ de formulaire que les utilisateurs ont soumis (erreur d'entrée), ou sur une variable dont ils ne savent rien (erreur serveur), sont des cas totalement différents. Ceux-ci devraient aboutir à des slugs de statut différents. Lorsque votre API agit comme un relais entre les utilisateurs et d'autres API, cette analyse peut être très difficile à réaliser, surtout si les API distantes ont un mauvais rapport d'erreur. Mais essayez, quand même.
* Soyez clair, dans votre documentation, sur la signification des classes d'erreur, et sur les actions attendues des consommateurs. Typiquement, les erreurs techniques signifient "si vous réessayez plus tard, cela pourrait fonctionner." D'autre part, les erreurs fonctionnelles signifient "vos workflows ou entrées sont incorrects, réessayer aveuglément n'aidera pas." Votre hiérarchie de slugs de statut pourrait avoir besoin d'être affinée, avec amour et attention, sur plusieurs années.

Ces deux idées — **slugs de statut et structures StatusPack** — ne sont certainement pas l'apogée de la gestion des erreurs, mais elles représentent une étape sûre vers l'avant en termes de précision et d'évolutivité.

J'aimerais entendre les autres champs d'erreur, ou autres stratégies de gestion, que les développeurs d'API ici présents pourraient avoir imaginés. **Veuillez partager vos innovations et leçons difficiles !**

_**Édité le 2018/09/07** : Correction des fautes de frappe, et précision de l'idée derrière le terme "slug"._

_**Édité le 2019/06/22** : Précision du champ "data" de StatusPack_