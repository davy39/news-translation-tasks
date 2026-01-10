---
title: Architecture Microservices – Expliquée en Anglais Simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-23T21:52:08.000Z'
originalURL: https://freecodecamp.org/news/microservices-architecture-for-humans
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/microservices-thumbnail.png
tags:
- name: distributed systems
  slug: distributed-systems
- name: Microservices
  slug: microservices
- name: software architecture
  slug: software-architecture
seo_title: Architecture Microservices – Expliquée en Anglais Simple
seo_desc: "By Charles M.\nOver the last few years, microservices have gone from an\
  \ overhyped buzzword to something you should understand as a software engineer.\
  \ \nAccording to an O'Reilly developer survey in 2020:\n\n61% of companies have\
  \ been using microservices i..."
---

Par Charles M.

Au cours des dernières années, les microservices sont passés d'un mot à la mode surhypé à quelque chose que vous devriez comprendre en tant qu'ingénieur logiciel. 

Selon une [enquête développeurs O'Reilly](https://www.oreilly.com/radar/microservices-adoption-in-2020) en 2020 :

* 61 % des entreprises ont utilisé des microservices au cours de l'année dernière
* 29 % disent qu'au moins la moitié de leurs systèmes d'entreprise sont construits en utilisant des microservices
* 74 % disent que leurs équipes possèdent les phases de construction/test/déploiement de leurs applications

Ces chiffres ne feront qu'augmenter avec le temps à mesure que l'écosystème autour des microservices mûrit et rend l'adoption encore plus facile. 

Cela ne signifie pas que vous devez être un expert en microservices pour obtenir un emploi, mais c'est définitivement un bonus de comprendre au moins les fondamentaux de base. 

La vérité est que les microservices ne sont pas si difficiles à comprendre lorsque vous les réduisez à l'essentiel. Le plus gros problème est que la plupart des ressources disponibles sont écrites pour impressionner les lecteurs plutôt que de les éduquer réellement. 

Une autre raison est qu'il n'existe même pas de définition concrète réelle de ce qu'est un microservice. Le résultat est qu'il existe des tonnes de définitions et de jargon qui se chevauchent, ce qui entraîne de la confusion pour les personnes qui essaient d'apprendre les microservices. 

Dans cet article, je vais éliminer tout le superflu et me concentrer sur les concepts de base de ce que sont réellement les microservices. J'utiliserai une variété d'exemples et de métaphores du monde réel pour rendre les concepts et idées abstraits plus faciles à comprendre.

Voici ce que nous allons couvrir :

* Brève histoire de la conception logicielle
* Avantages et inconvénients des monolithes
* Avantages et inconvénients des microservices

## Résumé des Microservices en 4 Minutes

Si vous préférez une introduction rapide aux microservices, vous pouvez regarder cette vidéo en premier :

%[https://www.youtube.com/watch?v=l4tQ66mDfxU]

## Comment Comprendre les Microservices avec une Analogie de Démarrage de Votre Propre Entreprise

Imaginons que vous êtes un ingénieur logiciel et que vous décidez de commencer à freelancer pour gagner de l'argent. Au début, vous avez quelques clients et tout se passe bien. Vous passez la plupart de votre temps à écrire du code et les clients sont heureux.

Mais avec le temps, vous commencez à ralentir à mesure que l'entreprise grandit. Vous passez de plus en plus de temps à faire du service client, à répondre aux emails, à apporter des modifications mineures pour les anciens clients, et à d'autres tâches qui ne vous font pas avancer en termes de revenus.

Vous réalisez que vous n'optimisez pas votre temps en tant qu'ingénieur logiciel, alors vous embauchez un employé dédié pour gérer le service client. 

À mesure que vous continuez à grandir, vous ajoutez plus d'employés avec des compétences spécialisées. Vous embauchez un marketeur pour vous concentrer sur l'attraction de nouveaux clients. Vous ajoutez des chefs de projet, plus d'ingénieurs logiciels, et finalement un département RH pour aider avec tous ces employés. 

Tout cela était nécessaire pour que votre entreprise grandisse au-delà de ce que vous pouviez faire seul, mais il y a bien sûr des douleurs de croissance. 

Parfois, il y a des incompréhensions entre les équipes ou les départements et les clients s'énervent lorsque des détails passent à travers les mailles du filet. Il y a le coût direct de devoir payer les salaires des employés, les rivalités internes entre les équipes, et de nombreux autres problèmes qui surviennent lorsque une entreprise grandit.

Cet exemple est quelque peu représentatif de la manière dont une entreprise logicielle pourrait passer d'un monolithe à une architecture de type microservice. Ce qui commence avec une seule personne faisant tout le travail devient progressivement une collection d'équipes spécialisées travaillant ensemble pour atteindre un objectif commun pour l'entreprise. 

Cela est très similaire à la manière dont les entreprises technologiques avec des monolithes ont migré vers des architectures de microservices. Bien que ces exemples ne soient pas une correspondance parfaite 1-1 pour les microservices, les problèmes généraux sont les mêmes :

1. **Mise à l'échelle** – Idéalement, vous voulez pouvoir embaucher rapidement de nouveaux employés et mettre à l'échelle linéairement la productivité de votre entreprise. 
2. **Communication** - Ajouter plus d'employés ajoute la charge de devoir coordonner et communiquer à travers l'organisation. Il existe de nombreuses stratégies que les entreprises essaient d'utiliser pour rendre cela efficace, surtout à cette ère du travail à distance. 
3. **Spécialisation** - Permettre à certains groupes de l'organisation d'avoir l'autonomie de résoudre les problèmes de la manière la plus efficace possible plutôt que d'essayer d'imposer un protocole standard pour toutes les situations. Certains clients peuvent avoir des besoins différents des autres, il est donc logique de permettre aux équipes d'avoir une certaine flexibilité dans la manière dont elles gèrent les choses.

## Comment Passer d'un Monolithe aux Microservices



![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-182.png)

Pour comprendre le présent, il est utile de comprendre le passé. Traditionnellement, les logiciels étaient conçus dans un style monolithique, et tout fonctionnait ensemble en tant qu'application unique. Comme tout le reste dans la vie, il y a des avantages et des inconvénients à ce style d'application.

Les monolithes ne sont pas intrinsèquement mauvais – et de nombreux défenseurs des microservices recommandent en fait de commencer par un monolithe et de s'y tenir jusqu'à ce que vous commenciez à rencontrer des problèmes. Vous pouvez ensuite diviser votre monolithe en microservices naturellement au fil du temps.

## Avantages d'une Architecture Monolithique

### Temps de développement plus rapide initialement

Avec une petite équipe, la vitesse de développement peut être extrêmement rapide lorsque vous commencez tout juste. 

Cela est dû au fait que le projet est petit, tout le monde comprend l'ensemble de l'application, et les choses avancent rapidement. Les membres de l'équipe savent exactement comment tout fonctionne ensemble et peuvent rapidement implémenter de nouvelles fonctionnalités.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-153.png)

### Déploiement simple

Parce que les monolithes fonctionnent comme une seule unité, des choses comme les tests et la journalisation sont relativement simples. Il est également plus facile de construire et de déployer un seul monolithe par rapport à un ensemble de microservices séparés. 

## Inconvénients d'une Architecture Monolithique

Malgré les avantages initiaux des monolithes, à mesure que les entreprises grandissent, elles rencontrent souvent plusieurs problèmes au niveau organisationnel et technique en raison de leur application monolithique.

### Couplage serré des modules

La plupart des entreprises avec des applications monolithiques essaient de diviser logiquement le monolithe en modules fonctionnels par cas d'utilisation pour garder les choses organisées. Pensez à des choses comme l'authentification, les commentaires, les utilisateurs et les articles de blog.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-183.png)

Le problème est que cela nécessite une discipline d'ingénierie extrême pour être maintenu à long terme. Les règles établies sont souvent jetées par la fenêtre lorsqu'une date limite approche. Cela entraîne des raccourcis pris pendant une période de rush et un code enchevêtré interconnecté qui s'accumule en tant que dette technique au fil du temps.

> Exemple du monde réel - Essayer de rester discipliné avec les monolithes est un peu comme s'en tenir à une routine d'exercice ou à un régime. Beaucoup de gens sont enthousiastes et peuvent rester disciplinés avec leur régime pendant quelques semaines, mais finalement la vie s'en mêle et vous revenez à votre routine normale.   
>   
> Essayer d'imposer un couplage lâche avec les monolithes est comme cela – il y a simplement trop de tentation de prendre des raccourcis lorsque vous êtes à court de temps.

### L'intégration des nouveaux employés devient difficile

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-154.png)

Pour les nouveaux employés, devenir productif prend souvent beaucoup plus de temps car ils doivent apprendre comment toutes les pièces interconnectées du monolithe fonctionnent ensemble avant de pouvoir risquer de modifier une partie quelconque de l'application. 

Il n'est pas rare que les nouveaux employés disent qu'il leur faut des mois pour se sentir vraiment à l'aise avec une base de code massive. Et il y a toujours la peur sous-jacente que chaque fois que vous poussez un nouveau code, cela pourrait faire planter toute l'application.

> Comparaison avec le monde réel - Former quelqu'un à faire une seule tâche comme enfoncer des clous vs former quelqu'un à faire chaque tâche possible sur un chantier de construction.   
>   
> Devoir enseigner à un nouveau employé absolument tout sur l'ensemble du travail augmente le coût de l'embauche de nouveaux employés.

### Exigences de ressources conflictuelles

Dans un monolithe, différents modules peuvent avoir des exigences matérielles différentes. Certaines tâches peuvent être des calculs intensifs en CPU, d'autres peuvent nécessiter beaucoup de RAM. 

Mais parce que l'ensemble de l'application doit fonctionner sur le même serveur, vous ne pouvez pas utiliser le type de matériel spécialisé pour une certaine tâche. 

> Exemple du monde réel - Certains types de véhicules sont mieux adaptés à certaines tâches.   
>   
> Si vous partez en voyage, une voiture avec une excellente économie de carburant serait le meilleur choix pour économiser de l'argent sur l'essence. Si vous emménagez dans un nouvel appartement, il serait bon d'avoir un véhicule avec plus d'espace de stockage pour ne pas avoir à faire autant de trajets. 

### Un seul bug peut faire tomber toute l'application 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-186.png)

Parce que l'application est déployée en tant qu'unité unique, cela signifie que n'importe quelle équipe peut accidentellement créer un bug qui fait tomber tout le monolithe.

> Exemple du monde réel - Pour empêcher une seule fuite de couler un navire entier, des cloisons sont utilisées pour sceller les sections si elles commencent à inonder.   
>   
> Les microservices fonctionnent de manière similaire – chaque service est déployé indépendamment des autres, ce qui peut réduire les chances qu'un bug fasse tomber toute l'application.

### Limite l'expérimentation

Lors de la construction d'un monolithe, vous êtes plus ou moins coincé avec l'écosystème du langage de programmation dans lequel le monolithe a été écrit. Un exemple simple serait les compromis des langages de programmation de bas niveau et des langages de programmation de haut niveau. 

Avec une architecture de microservices, si un certain service a du mal à évoluer, vous avez la possibilité de le réécrire dans un langage de haute performance comme C++ ou Go. 

Pour d'autres services où la performance n'est pas un facteur énorme, vous pouvez améliorer la vitesse de développement en utilisant des langages de haut niveau comme Python ou JavaScript.

Une architecture monolithique peut également aveugler une équipe en ne voyant pas d'autres façons de résoudre un problème. Lorsque vous n'avez qu'un marteau, tout ressemble à un clou.

> Comparaison avec le monde réel - La pizza est géniale, mais vous ne voudriez probablement pas manger de la pizza à chaque repas pour le reste de votre vie.   
>   
> De plus, dans certaines situations, ce serait également inconvénient de cuisiner et de manger de la pizza plutôt que quelque chose d'autre. Parfois, il serait agréable de simplement prendre une collation rapide ou de manger quelque chose d'un peu plus sain.

### Les déploiements peuvent devenir lents 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/slow-deployment-drawing.PNG)

L'un des points forts du monolithe listé ci-dessus peut éventuellement devenir une faiblesse. Le fait que l'ensemble de l'application soit déployé ensemble peut devenir un problème pour les monolithes massifs car cela peut entraîner un temps de déploiement long pour l'ensemble du service. Cela réduit la rapidité avec laquelle une équipe peut itérer et apporter des modifications à l'application. 

Chaque fois qu'ils apportent même une modification mineure, ils sont forcés d'attendre que l'application se construise et se déploie pour les tests.

> Exemple du monde réel - Votre rêve est de faire les meilleurs cookies du monde. La manière la plus rapide d'accomplir cet objectif serait de tester autant de lots de cookies que possible tout en modifiant et en améliorant progressivement la recette jusqu'à ce qu'elle soit parfaite.   
>   
> Maintenant, imaginez que vous n'avez qu'un seul four. Le rythme auquel vous pouvez tester différentes recettes de cookies est beaucoup plus lent par rapport à avoir 10 fours.

## Avantages des Microservices

Maintenant que vous connaissez les avantages et les inconvénients du style d'architecture monolithique, examinons les microservices.

### La vitesse de développement s'améliore

Parce que vous ne déployez plus un monolithe, les équipes sont capables de se déplacer plus rapidement lorsqu'il s'agit d'ajouter des fonctionnalités. Les équipes peuvent avoir des calendriers de publication indépendants et n'ont pas à se soucier de coordonner avec d'autres équipes autant. 

Tant que l'interface externe que les autres microservices utilisent pour interagir avec le service de l'équipe reste la même, une équipe de développement pourrait complètement réécrire le système dans un autre langage de programmation si elle le souhaitait.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-184.png)

Un autre avantage de chaque service étant déployé indépendamment est que les builds sont plus rapides en raison de chaque build étant plus petit. Cela signifie que le temps d'itération est également amélioré simplement parce que les builds sont plus rapides.

> Exemple du monde réel - Lorsque vous achetez de la nourriture dans un restaurant, vous ne vous souciez pas vraiment si quelque chose a changé en coulisses tant que la nourriture a bon goût.   
>   
> Peut-être qu'ils ont obtenu de nouveaux fours ou friteuses, mais tant que la nourriture a le même goût, vous ne vous en souciez pas. En tant que consommateur externe, la seule chose qui compte est le produit final.

### Intégration plus rapide pour les nouveaux employés

Les nouveaux employés peuvent apprendre un seul système pour commencer et commencer à contribuer. Avec le temps, ils peuvent continuer à apprendre davantage sur l'ensemble de l'application, mais ce n'est pas nécessaire tout de suite.

> Exemple du monde réel - La chaîne de montage a révolutionné la production en décomposant les choses. Au lieu que chaque employé doive savoir comment créer un produit entier à partir de zéro, il devait simplement apprendre la seule partie sur laquelle il travaillait. Cela a réduit le temps de formation pour les nouveaux employés et permis une meilleure mise à l'échelle.

### Tolérance aux pannes

Bien que les microservices dépendent souvent les uns des autres pour accomplir des tâches, une architecture de microservices bien conçue aura une redondance intégrée et des mécanismes de sécurité pour empêcher la défaillance de l'ensemble du système si un autre service tombe en panne. 

Souvent, cela implique de réessayer les requêtes avec une période d'attente croissante entre les requêtes ou une valeur de repli par défaut à retourner si le service n'est pas disponible.

> Exemple du monde réel - Si le service de recommandation de Netflix tombe en panne, il n'a pas de sens de retourner un message d'échec complet aux utilisateurs.   
>   
> Au lieu de cela, Netflix pourrait simplement retourner un ensemble par défaut de films populaires et en arrière-plan continuer à réessayer le service de recommandation jusqu'à ce qu'il soit en mesure de retourner les recommandations personnalisées de l'utilisateur.

### Évolutivité flexible

Parce que chaque service est déployé indépendamment, vous pouvez également répliquer et mettre à l'échelle chaque service individuellement. Avec un monolithe, l'entreprise serait obligée de mettre à l'échelle l'ensemble de l'application, malgré le fait qu'une seule fonctionnalité reçoit plus de trafic que d'habitude. 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-185.png)

Avec une architecture de microservices, une entreprise peut spécifiquement mettre à l'échelle uniquement le service qui doit gérer plus de trafic, ce qui est plus efficace et peut économiser de l'argent car cela réduit les ressources gaspillées. 

> Exemple du monde réel - Prenons quelque chose comme le Cyber Monday pour Amazon, beaucoup plus de commandes que d'habitude seront passées, mais la plupart des gens ont probablement déjà sélectionné ce qu'ils voulaient et l'ont mis dans leur panier.   
>   
> Donc, tandis que le service de commandes recevra beaucoup plus de trafic que d'habitude, des choses comme le service de recherche et d'autres fonctionnalités pourraient être autour des taux d'utilisation normaux. 

Cela est particulièrement utile si un service est particulièrement gourmand en une certaine ressource et peut utiliser du matériel spécialisé pour cette tâche. 

Si un service a besoin d'une tonne de ressources CPU mais pas beaucoup de RAM, l'entreprise peut économiser de l'argent en n'utilisant pas de serveurs polyvalents. Une entreprise utilisant un monolithe pur n'a pas d'autre choix que de mettre à l'échelle en utilisant des serveurs de type "touche-à-tout".

## Inconvénients des Microservices

Les microservices sont loin d'être parfaits. Le passage d'un monolithe aux microservices élimine certains problèmes tout en en créant de nouveaux.

### Complexité globale

Bien que chaque service individuel soit plus facile à comprendre, l'ensemble du système lui-même est compliqué. Cette complexité supplémentaire a conduit à l'émergence d'outils comme Docker et Kubernetes pour abstraire autant que possible. 

Le but de ces outils est de permettre aux ingénieurs logiciels de ne pas se soucier de quoi que ce soit d'autre que de la construction de fonctionnalités comme ils le feraient normalement, sans se soucier de la manière dont tout fonctionne en coulisses.

### Communication

L'un des plus grands problèmes avec les microservices est de déterminer comment ils communiquent entre eux. 

Une seule requête externe d'un utilisateur peut nécessiter plusieurs services travaillant ensemble pour satisfaire cette requête. Utilisons la passation d'une commande en ligne comme exemple de la manière dont cela pourrait fonctionner :

* L'utilisateur passe une commande dans l'application
* Le répartiteur de charge transfère la requête aux services disponibles pour traiter la requête
* Le service de panier d'achat donne la liste des articles dans la commande
* Le service d'inventaire confirme que les articles sont en stock
* Le service de livraison calcule le coût estimé et le temps de livraison
* Le service de paiement confirme que le paiement du client est valide
* Le service de recommandation utilise les articles commandés pour générer de nouvelles recommandations pour le client à l'avenir
* Le service de révision planifie un email pour demander au client de laisser un avis

À n'importe quelle étape ci-dessus, un seul service en échec pourrait entraîner l'échec de l'ensemble du processus de commande ou l'énervement de l'utilisateur, ce qui créerait rapidement des clients en colère. 

Gérer la manière dont tous ces services interagissent et traitent les échecs partiels est un énorme défi avec les architectures de microservices.

### Gestion des données

L'un des défis les plus difficiles avec les microservices est de savoir comment gérer les requêtes qui s'étendent sur plusieurs services et nécessitent de faire des mises à jour des données. 

Que se passe-t-il si une requête échoue en cours de route avec des données mises à jour dans un service mais pas dans les autres ? Vous ne voulez pas facturer un utilisateur mais qu'il ne reçoive pas ce pour quoi il a payé parce que le service était en panne.

Dans un monolithe, vous pouvez vous appuyer sur des transactions ACID pour annuler une modification de la base de données si quelque chose ne va pas. Avec les microservices, il y a beaucoup plus de complexité impliquée avec ce que l'on appelle les transactions distribuées à travers les services.

### Environnement de développement

La plupart des outils ont été conçus en pensant aux monolithes et le développement en général devient plus difficile avec une architecture de microservices. 

Les tests nécessitent de pouvoir simuler les interactions avec d'autres services, le débogage est plus difficile car les choses ne se passent plus dans un seul processus, et la journalisation doit être effectuée à travers plusieurs services.

Même quelque chose de simple comme essayer de suivre pourquoi un blog se charge lentement est plus difficile que vous ne le pensez. 

Disons que vous remarquez dans vos analyses que tout à coup il faut 5 secondes pour que les pages se chargent sur votre blog. Avec un monolithe, il serait assez facile de trouver le problème, mais avec une architecture de microservices, vous avez besoin d'outils spécialisés pour suivre les requêtes externes lorsqu'elles sont traitées par différents services.

## Conclusion

Espérons que cet article vous a donné une compréhension décente du quoi et du pourquoi des microservices et une compréhension intuitive de leur fonctionnement, même si vous ne comprenez pas tous les détails techniques sous le capot.

Si vous êtes intéressé à voir de futures vidéos et articles sur les microservices, assurez-vous de [vous abonner sur YouTube](https://www.youtube.com/channel/UCzYV9nBadlQdBMPP2ZuDvKA) ou [suivre sur Twitter](https://twitter.com/Ren_Engineer) pour ne rien manquer.