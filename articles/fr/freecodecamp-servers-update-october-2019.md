---
title: Que se passe-t-il avec les serveurs de freeCodeCamp ?
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2019-10-18T19:36:22.000Z'
originalURL: https://freecodecamp.org/news/freecodecamp-servers-update-october-2019
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/maxresdefault--5--1.jpg
tags:
- name: community
  slug: community
- name: freeCodeCamp.org
  slug: freecodecamp
- name: nonprofit
  slug: nonprofit
seo_title: Que se passe-t-il avec les serveurs de freeCodeCamp ?
seo_desc: 'Update at 17:00 California time: We have now fixed most of the problems.
  We''re still working on a few known issues, but /learn is now fully operational.

  Here was the culprit - a regular expression-based query that was running against
  millions of data...'
---

**Mise à jour à 17:00 heure de Californie** : Nous avons maintenant corrigé la plupart des problèmes. Nous travaillons encore sur quelques problèmes connus, mais /learn est maintenant pleinement opérationnel.

Voici le coupable - une requête basée sur une expression régulière qui s'exécutait contre des millions d'enregistrements de la base de données chaque fois qu'une personne essayait de s'authentifier.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/fix_api___revert_regex_based_email_query___37393__-_freeCodeCamp_freeCodeCamp_ebc49be.png)

Et voici l'utilisation du CPU de notre cluster avant et après avoir corrigé le problème :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-78.png)
_Eureka en effet._

Cela peut sembler évident, mais il a fallu [Mrugesh](https://twitter.com/raisedadead) 3 jours de travail de détective pour identifier le goulot d'étranglement.

Nous avons conclu que nous aurions pu repérer cela plus tôt avec un outil à 30 dollars par mois, alors nous avons craqué et l'avons acheté pour une utilisation future.

Ce qui suit est une explication plus détaillée de ce qui s'est passé.

## En bref :

* Mardi, nous avons déployé une tonne de nouveau code. Y compris du code qui nous permet de livrer en continu de nouvelles fonctionnalités et des corrections de bugs.
* Nous pensions avoir suffisamment testé notre nouveau code sous charge. Mais il n'était pas assez performant pour le poids soudain de 2 000 utilisateurs simultanés.
* /forum et /news fonctionnaient bien, mais la fonctionnalité de connexion sur /learn était peu fiable pendant 3 jours.

## OK. Maintenant, quelques détails supplémentaires.

Depuis environ 10 mois, nous accumulons de nouvelles fonctionnalités, des corrections de bugs et des améliorations de curriculum.

Nous avons continué à fusionner des améliorations dans notre branche Master et à les déployer sur notre serveur bêta à www.freecodecamp.dev.

Depuis 2 mois, de nombreux contributeurs utilisent cette version bêta de freeCodeCamp.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/screen-shot-3.png)

Et en célébration du 5e anniversaire de freeCodeCamp ce mois-ci, nous voulions pousser toutes ces améliorations en production sur www.freecodecamp.org.

Mardi, nous avons mis le site hors ligne pour ce que nous pensions être 3 minutes de maintenance planifiée. Nous avons effectué une dernière série de tests, fait une sauvegarde de la base de données, envoyé un tweet "nous serons de retour bientôt" et poussé 10 mois de code en direct d'un seul coup.

Mais la loi de Murphy attendait derrière le coin pour nous frapper aux genoux. Et à mesure que le trafic augmentait, nos serveurs ont fléchi.

Nous avons pu remettre /forum et /news en ligne presque immédiatement. Mais /learn nécessitait une authentification et touchait quelques points de terminaison et serveurs API supplémentaires. Donc pendant 3 jours, nous nous sommes déménés pour le faire fonctionner.

Il s'est avéré que notre nouveau code n'était pas aussi performant que nous le pensions, et nous frappions nos serveurs API beaucoup plus que nécessaire.

Nous avons donc identifié les parties du code qui faisaient des appels API inutiles et les avons refactorisées, tout en jonglant avec les défis DevOps.

## Pourquoi cela s'est-il produit, cependant ? Vraiment ?

À la fin de la journée, cette panne était de ma faute.

Voici pourquoi.

Notre budget total pour 2019 est d'environ 300 000 $ seulement. Et pourtant, nous aidons des millions de personnes à apprendre à coder chaque mois.

Nous recevons maintenant plus de trafic que d'autres sites d'apprentissage de la programmation comme Udacity et Codecademy. Nous recevons même plus de trafic que des sites d'actualités grand public comme TechCrunch.

```
+-------------------+------------+
|      Website      | Alexa Rank |
+-------------------+------------+
| stackoverflow.com |         40 |
| github.com        |         85 |
| theverge.com      |        615 |
| wired.com         |      1,435 |
| freeCodeCamp.org  |      1,596 |
| techcrunch.com    |      1,601 |
| codecademy.com    |      2,040 |
| udacity.com       |      2,348 |
| hackernoon.com    |      3,986 |
| dev.to            |      7,684 |
+-------------------+------------+
```

Lorsque vous opérez à une telle échelle extrême avec un budget aussi misérable, vous finissez par économiser sur tout.

Ces gros serveurs qui pourraient vous offrir une marge de manœuvre confortable pour les pics ? Trop chers.

Ces services DevOps sophistiqués qui identifient les points de blocage ? Trop chers.

Notre équipe de 5 ingénieurs finit par faire le travail de 10.

Mon point est - c'est de ma faute si freeCodeCamp n'a que 300 000 $ à dépenser cette année. Pour mettre ce chiffre en perspective, je connais des développeurs individuels à San Francisco dont le salaire est supérieur à 300 000 $.

Il n'y a rien de mal à avoir un gros salaire. San Francisco est une ville chère.

Mais il y a un problème lorsque freeCodeCamp - l'un des plus grands sites éducatifs sur internet - essaie de fonctionner avec un budget aussi ridiculement petit.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/c.jpg)
_Qu'est-ce que c'est ? Un budget pour les fourmis ?! (crédit image : Zoolander)_

Encore une fois, c'est de ma faute.

Je suis inexpérimenté en matière de collecte de fonds de base.

J'apprends encore à sensibiliser à tout le travail que nous faisons pour la communauté.

Je suis timide quand il s'agit de vous demander à tous de faire des dons pour financer ce travail.

Alors je vais faire un effort concerté pour m'améliorer et pour augmenter notre budget.

Je ne veux pas diffuser de publicités.

Je ne veux pas dire "freeCodeCamp, présenté par la société Acme".

Et bien sûr, je ne veux jamais faire payer les apprenants pour nos ressources d'apprentissage.

Jusqu'à présent, nous n'avons pas eu à faire aucune de ces choses.

Mais cela ne nous laisse vraiment qu'une seule source de financement. Nous, le peuple.

freeCodeCamp est une organisation à but non lucratif soutenue par des donateurs de base. Nous devons simplement nous améliorer pour demander de l'argent aux gens.

Nous entrons dans la saison des fêtes. C'est à ce moment que sont faits environ 80 % des dons caritatifs de l'année ici aux États-Unis.

Alors je vais rester concentré sur cela. Je documenterai ce que j'apprends au fur et à mesure de mes expériences. Et je créerai finalement un manuel de collecte de fonds pour d'autres organisations à but non lucratif soutenues par des donateurs de base, basé sur ce que j'apprends.

C'est un peu embarrassant, mais notre page de dons actuelle est hors ligne aujourd'hui parce que notre authentification est toujours défectueuse.

J'ai donc mis en place [une page PayPal où vous pouvez faire des dons ponctuels déductibles d'impôts à freeCodeCamp](https://paypal.me/freecodecamp).

Nous accueillons toujours votre soutien mensuel à freeCodeCamp. Vos dons de 5 $ chaque mois sont ce qui rend freeCodeCamp possible, et ce qui nous donne le budget stable pour planifier à l'avance.

Mais si vous avez un peu d'argent supplémentaire pour un don ponctuel, [ce serait une énorme aide](https://paypal.me/freecodecamp).

# Voici mon engagement envers vous :

freeCodeCamp restera gratuit.

freeCodeCamp ne diffusera pas de publicités.

Et lorsque nous vous demanderons de faire un don, nous le ferons avec tact et honnêteté. Nous n'utiliserons pas le pathos, ou ne ferons pas ces déclarations du type "nous allons faire faillite à moins que vous ne fassiez un don maintenant" auxquelles certaines autres organisations à but non lucratif recourent.

Parce que la réalité est celle-ci : Même si freeCodeCamp venait à manquer complètement d'argent, nous continuerions quand même.

Oui, nous devrions licencier tout le monde, y compris moi-même. Mais j'irais chercher un autre travail et paierais les serveurs moi-même.

Parce que freeCodeCamp est clairement quelque chose dont le monde a besoin.

J'ai investi 5 ans de ma vie dans cette communauté. J'ai investi 150 000 $ de mes économies personnelles de ma carrière d'enseignant dans freeCodeCamp.

freeCodeCamp ne mourra jamais.

Il s'agit simplement de savoir à quel point freeCodeCamp peut vivre de manière vibrante.

Encore une fois, si vous avez un peu d'argent à épargner, nous sommes une organisation à but non lucratif très efficace, et nous l'utiliserons de manière efficace. [Faites un don ici](https://paypal.me/freecodecamp).

Et merci encore pour votre patience avec la panne sur /learn.

Une fois que nous aurons tout corrigé, je vous informerai tous, et je publierai mon article du 5e anniversaire qui détaille toutes les grandes améliorations que nous avons pour notre 5e anniversaire.

Bon codage.