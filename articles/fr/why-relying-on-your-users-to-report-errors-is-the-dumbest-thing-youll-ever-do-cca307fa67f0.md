---
title: Pourquoi compter sur vos utilisateurs pour signaler les erreurs est la pire
  idée que vous puissiez avoir
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-02T03:41:04.000Z'
originalURL: https://freecodecamp.org/news/why-relying-on-your-users-to-report-errors-is-the-dumbest-thing-youll-ever-do-cca307fa67f0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BwpQjOGjV2HhN-s3EGfhUA.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pourquoi compter sur vos utilisateurs pour signaler les erreurs est la
  pire idée que vous puissiez avoir
seo_desc: 'By Nick Harley

  We all love to code.

  When we think about coding, we are usually picturing ourselves building.

  Building features, new innovations, new functionality, and exciting updates that
  users will love. It’s that mental picture that gets us excit...'
---

Par Nick Harley

Nous aimons tous coder.

Quand nous pensons au codage, nous nous imaginons généralement en train de **construire**.

Construire des fonctionnalités, des innovations, de nouvelles fonctionnalités et des mises à jour passionnantes que les utilisateurs aimeront. C'est cette image mentale qui nous enthousiasme pour les choses que nous pouvons construire ensuite.

Mais les images romantiques dans nos têtes ne se traduisent souvent pas par la réalité.

![Image](https://cdn-media-1.freecodecamp.org/images/6Ro4thCsMpOPcurgBnCHWtsAPGnbCCf4FaVA)

Les développeurs de logiciels passent la plupart de leur temps sur des tâches autres que la construction. Ils assistent à des réunions, discutent des spécifications, planifient et nettoient le code existant. Et bien sûr, leur activité préférée est la correction de bugs.

Je n'ai pas encore rencontré de développeur qui aime trouver des problèmes dans son code. Mais cette frustration provient probablement du fait que la recherche et la reproduction des erreurs prennent beaucoup de temps.

Historiquement, les développeurs de logiciels ont dû chercher une aiguille dans une botte de foin. Ils ont dû trouver les réponses eux-mêmes, plutôt que de compter sur ces captures d'écran des utilisateurs postées dans un document Microsoft Word.

![Image](https://cdn-media-1.freecodecamp.org/images/dHAAlT2dswHdmCgiyFbYRVGNP6JHBgGWyWvr)
_Nous avons tous été là !_

Quel navigateur et quelle version utilisez-vous ? Quel système d'exploitation ? Pouvez-vous me dire exactement où vous avez cliqué ? Ensuite, qu'est-il arrivé ? Sur quelle page étiez-vous avant ? Comment êtes-vous arrivé à cet écran ?

Tant de questions, si peu de réponses (utiles).

Le débogage d'un problème peut prendre **une éternité !**

### Compter sur les utilisateurs pour signaler les problèmes

De nombreuses équipes de développement logiciel comptent encore sur les utilisateurs pour signaler les problèmes avec leurs applications.

**Ce qui est un peu fou de nos jours.**

C'est un peu comme les chaînes de restaurants fast-food. Elles mettent la responsabilité sur les clients de débarrasser leurs propres tables en fournissant des plateaux et des stations de collecte des déchets. La nourriture du restaurant a peut-être été terrible. Mais le client aurait pu calmement débarrasser sa table, jeter ses déchets et partir. À moins qu'ils ne prennent le temps de se plaindre, le personnel suppose qu'un autre client satisfait vient de quitter le restaurant.

Mais ils ne reviendront jamais.

Certains développeurs s'attendent à ce que les utilisateurs se débrouillent seuls lorsqu'ils utilisent leurs applications. Après tout, si personne ne signale de problèmes, nous n'en avons pas — n'est-ce pas ? Mettre la responsabilité sur vos utilisateurs pour signaler les problèmes qu'ils rencontrent est limitant. Vous verrez environ un pour cent des instances totales affectant votre base d'utilisateurs entière, et les détails techniques seront minces et incohérents.

Les développeurs passeront plus de temps à essayer de déboguer le problème — en utilisant de petits morceaux d'informations — qu'à le corriger. C'est s'ils peuvent trouver le problème du tout.

### Votre logiciel n'est pas aussi bon que vous le pensez

Je parlais à un ami qui travaille pour un grand détaillant en ligne. Il m'a expliqué comment ils avaient trouvé un gros problème dans leur système de commande en ligne que personne ne connaissait.

Après plusieurs jours d'enquête, ils n'ont pas pu identifier le problème. À ce moment-là, ils ont décidé d'essayer un outil dédié pour détecter et diagnostiquer les erreurs dans leur application.

Ce qu'ils ont trouvé était alarmant.

L'outil a identifié que l'un des huit serveurs manquait de mémoire et générait des erreurs. Cela a provoqué l'arrêt complet du processus de paiement de l'utilisateur.

**Une session de paiement sur huit était interrompue.**

La découverte et la correction de ce problème ont entraîné une augmentation immédiate des ventes de 20 000 $ par mois ! Les gens ne rencontraient plus de problèmes lors du processus d'achat.

Ils ont estimé que cela avait affecté plus de 5 000 utilisateurs — pourtant, ils n'avaient reçu que deux tickets de support à ce sujet.

Bien que l'équipe ait été heureuse de trouver le problème, il y avait aussi une déception écrasante. Une erreur non identifiée avait probablement entraîné plus de 100 000 $ de revenus manqués.

### S'envoyer un email lorsque des erreurs se produisent est une mauvaise idée

Vous pouvez vous asseoir et regarder un flux en direct des problèmes qui se produisent dans votre code en suivant les logs. Et vous pouvez engager quelqu'un pour le faire pendant que vous dormez. Ou, vous pouvez vous envoyer un email lorsqu'une exception non gérée se produit — semble être une bonne idée !

Jusqu'à ce que vous le fassiez.

Si vous configurez cela, cela pourrait ressembler à ceci :

```
public void TryProcessLineNumber(int lineNumber){    try    {        ProcessLineNumber(lineNumber);    }    catch (Exception ex)    {        LetMyselfKnowViaEmail("Something went wrong: " + ex.Message);    }}
```

Mais méfiez-vous des problèmes que cela peut créer.

Envoyer des erreurs par email peut être adapté pour des projets secondaires plus petits et des projets personnels. Mais une fois que vous vous étendez au-delà de cela, les choses commencent à devenir désordonnées. Très, très désordonnées :

* Les détails de diagnostic sont limités
* Il est difficile de configurer des règles de notification et les choses commencent à devenir bruyantes
* Une exception capturée dans une boucle infinie peut envoyer 50 000 emails à votre boîte de réception pendant la nuit
* Les erreurs n'ont aucun niveau de priorité ou visibilité d'impact et apparaissent toutes égales
* Après avoir reçu plus de cent emails, vous abandonnez leur lecture

![Image](https://cdn-media-1.freecodecamp.org/images/CivTmgQUVSD9X1YuzuZCTPv6QhIbvrkwNlgK)

Peu de temps après avoir commencé à vous envoyer des erreurs par email, vous commencez à les ignorer. Ou vous les filtrez dans un dossier parce qu'il y a juste trop de bruit et aucun signal.

Vous êtes laissé à fouiller à travers des milliers d'emails à la recherche de la bonne instance d'erreur.

Nous avons besoin de quelque chose de plus intelligent.

### ELMAH — journalisation de vos exceptions

ELMAH (Error Logging Modules and Handlers) est une installation de journalisation des erreurs à l'échelle de l'application qui est complètement pluggable. Il peut être ajouté dynamiquement à une application web [ASP.NET](http://www.asp.net/) en cours d'exécution, ou même à toutes les applications web ASP.NET sur une machine, sans avoir besoin de recompilation ou de redéploiement.

ELMAH ne prend pas en charge tous les langages de programmation et plates-formes. Puisque sa fonctionnalité est assez limitée lorsqu'il s'agit d'approfondir la cause racine d'un problème, il est généralement utilisé pour des projets plus petits. Il n'est également plus vraiment en développement actif ces jours-ci, mais au moins c'est _quelque chose_, et c'est gratuit.

![Image](https://cdn-media-1.freecodecamp.org/images/0MNhVYYCmI5dUqwRbvqGFXELL6qAnI3joFaw)
_Journalisation des erreurs Elmah_

ELMAH est essentiellement un package NuGet pour les applications web .NET. Il journalise chaque exception qui se produit sur un ou plusieurs sites web vers le stockage que vous choisissez. Contrairement à d'autres frameworks de journalisation, ELMAH journalise chaque exception automatiquement lorsqu'il est configuré dans sa forme la plus simple. Bien sûr, il y a une API que vous pouvez utiliser pour journaliser des erreurs personnalisées. Mais la plupart des gens n'utilisent que la partie automatique. Dans ce tutoriel, nous nous concentrerons uniquement sur les parties de base.

Voici [un excellent tutoriel](https://blog.elmah.io/elmah-tutorial/) sur la façon de commencer.

### Outils dédiés de signalement des erreurs et des plantages

Si vous êtes sérieux concernant la gestion des erreurs et des plantages dans vos applications, utilisez un outil dédié de [surveillance des erreurs](https://raygun.com/). Il détecte et diagnostique automatiquement les problèmes affectant vos utilisateurs en ajoutant un fournisseur à votre code d'application.

C'est quelques lignes de code — c'est tout ce qu'il faut.

**Utiliser un outil comme celui-ci vous permet de :**

* Éliminer les exceptions bruyantes et vous concentrer sur les choses qui comptent, comme l'impact sur les utilisateurs
* Configurer des notifications personnalisables via email, Slack ou HipChat
* Utiliser un seul outil pour suivre plusieurs langages et plates-formes
* Profiter du regroupement des erreurs pour les erreurs similaires
* Garder toute votre équipe au courant des erreurs et de leur résolution

![Image](https://cdn-media-1.freecodecamp.org/images/ZuGj-GY6XUa-TjLZG1uk374kGWzDf4dsTffp)
_Utilisez un système logiciel dédié de surveillance des erreurs comme [Raygun](https://raygun.com" rel="noopener" target="_blank" title=")_

Ces outils ne sont pas bon marché ou gratuits comme les autres programmes dont nous avons parlé, mais quel prix mettez-vous sur votre temps ? Supposons que vous utilisiez une solution gratuite. Ensuite, vous devez arrêter de coder pendant trois heures pendant que vous essayez de reproduire un bug. Cela représente en fait un très mauvais retour sur investissement.

Les équipes qui cherchent à avancer rapidement et à livrer de nouvelles fonctionnalités aux utilisateurs diraient que de telles solutions professionnelles valent chaque centime. Elles peuvent réduire le temps que les développeurs passent à corriger les bugs et les ramener au codage et à la construction d'améliorations.

Même si vous pensez que votre code est parfait et que les utilisateurs ne rencontrent aucun problème, branchez un outil comme [Raygun](https://raygun.com/). Vous serez surpris de ce que vous trouverez.

### Adoptez une approche proactive et récoltez les récompenses

Nous aimerions tous que la technologie corrige automatiquement nos problèmes logiciels. Malheureusement, je pense que nous sommes encore loin des logiciels auto-réparants et auto-consciencieux.

Vous pouvez également intégrer des solutions de surveillance des erreurs dans les flux de travail des développeurs pour faciliter la résolution des erreurs et des plantages. Mais les données sont souvent souillées et séparées du contexte dans d'autres systèmes.

L'avenir de la surveillance des erreurs réside dans le fait de s'assurer que toutes les équipes — front-end, back-end, gestion ou support — ont une visibilité complète sur chaque problème que rencontrent leurs utilisateurs. Et ensuite avoir la capacité de le résoudre immédiatement.

Cela s'étend également aux tendances à venir dans l'espace de livraison et de déploiement continus. Vous pouvez appliquer des correctifs et livrer en production en quelques minutes après avoir identifié le problème. Vous n'avez pas à attendre des semaines avant le prochain déploiement majeur.

Mettez l'accent sur votre équipe lors de la gestion des erreurs et des plantages dans vos propres applications. Découvrez les problèmes avant vos utilisateurs et ne comptez pas sur eux pour signaler les erreurs.

**_Car ils ne le feront pas._**