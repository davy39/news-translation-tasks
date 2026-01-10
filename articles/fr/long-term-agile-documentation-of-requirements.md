---
title: Documentation à long terme et agile des exigences
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-25T18:47:01.000Z'
originalURL: https://freecodecamp.org/news/long-term-agile-documentation-of-requirements
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/art-book-pages-browse-256467.jpg
tags:
- name: agile
  slug: agile
- name: documentation
  slug: documentation
seo_title: Documentation à long terme et agile des exigences
seo_desc: 'By Bertil Muth

  In my training courses, we discuss many topics. Including: how do you document requirements
  in the long term, in an agile environment?

  Documentation is stored knowledge. As things are forgotten, its value increases
  over time. That’s wh...'
---

Par Bertil Muth

Dans mes formations, nous abordons de nombreux sujets. Y compris : comment documenter les exigences à long terme, dans un environnement agile ?

La documentation est une connaissance stockée. À mesure que les choses sont oubliées, sa valeur augmente avec le temps. C'est pourquoi je pense que la question de la documentation à long terme est intéressante.

Je voudrais commencer par deux options de documentation à long terme qui n'ont pas de sens dans un environnement agile. Ensuite, je souhaiterais souligner des options sensées. Chacune avec ses avantages et ses inconvénients.

#### Pas une option utile : Spécification détaillée préalable

Il n'a pas de sens de spécifier toutes les exigences en détail à l'avance. Dans un environnement complexe, il y a des changements fréquents. Les exigences sont re-priorisées. C'est l'un des avantages du développement agile. Certaines exigences sont envisagées, mais jamais mises en œuvre. Ou pas comme prévu, car vous acquérez de nouvelles connaissances pendant le développement.

La discussion et la documentation d'une exigence prennent du temps. Si l'exigence n'est pas mise en œuvre comme documentée, ce fut une perte de temps. Un temps qui est urgemment nécessaire dans le développement.

#### Pas une option utile non plus : Le backlog

Supposons que vous commenciez à travailler de manière agile. Peut-être pensez-vous : il n'y a pas de spécification détaillée. Mais un backlog. Utilisons-le pour documenter les exigences sur le long terme.

Mais un backlog sert l'avenir, pas le passé. C'est plus comme une liste de tâches. Que mettons-nous en œuvre ensuite ? Le backlog n'est pas une option sensée pour la documentation à long terme. Il ne documente pas ce qui a déjà été mis en œuvre.

#### Option 1 : Archiver les user stories après la mise en œuvre

Lors d'une formation, un participant m'a dit que son entreprise gère les user stories dans JIRA. Et les développeurs les archivent après la mise en œuvre. Bien sûr, vous pouvez rechercher dans cet archive. Le participant a rapporté que cela fonctionnait bien pour eux.

Un pragmatique agile peut difficilement être en désaccord. Ce qui fonctionne, fonctionne. Au moins dans un certain contexte. Je vois 2 risques à cette approche :

* **Trop de détails** : Pour pouvoir utiliser les stories à long terme, vous devez certainement documenter de nombreux détails. Que se passe-t-il si les détails ne peuvent pas être mis en œuvre comme prévu ? Les user stories seront-elles ajustées par la suite ? Les stories peuvent ne plus documenter correctement la mise en œuvre.
* **Documentation delta au lieu de documentation système** : Les user stories décrivent ce qui doit être fait. Le « delta » d'un état à un autre état. Pour connaître l'état actuel, il peut être nécessaire d'analyser plusieurs user stories passées. Les stories manquent d'informations contextuelles. Elles ne sont pas une documentation système, mais seulement de petits fragments.

#### Option 2 : Adaptation incrémentale de la documentation système

La documentation peut être maintenue en continu. Pendant un Sprint Scrum, vous documentez l'état actuel. Les exigences qui viennent d'être mises en œuvre. La documentation grandit avec le temps. Elle est complétée de manière incrémentale.

Si vous suivez cette approche de manière cohérente, elle présente un grand avantage. La documentation système est toujours à jour. Elle documente les exigences qui ont réellement été mises en œuvre.

Un défi avec cette option est la discipline. Seule une documentation cohérente permettra de maintenir la documentation à jour. Et cela prend du temps.

De plus, tous les développeurs ne sont pas des rédacteurs de documentation nés. Si, cependant, les développeurs ne documentent pas eux-mêmes, mais délèguent cela à d'autres employés, il y a un risque de perte d'informations.

Une façon de promouvoir cette discipline au sein d'une équipe est de l'inclure dans la Definition of Done. Quelque chose comme : « La documentation système a été mise à jour ». À vérifier lors de la Sprint Review.

#### Option 3 : Exigences dans le code

Un type de documentation à long terme complètement sous-estimé est le code du logiciel. Si vous structurez le code de manière appropriée et utilisez des conventions de nommage, vous pouvez générer de la documentation à partir du code.

Pour réaliser cela, j'ai [développé une bibliothèque](https://github.com/bertilmuth/requirementsascode). Avec elle, vous pouvez spécifier des modèles de cas d'utilisation exécutables dans le code. Ils agissent [de manière similaire à une machine à états](https://www.freecodecamp.org/news/kissing-the-state-machine-goodbye/). Voici un exemple de code pour un cas d'utilisation pour une carte de crédit :

```java
	Model model = Model.builder()
	  .useCase("Utiliser une carte de crédit")
	    .basicFlow()
	    	.step(ASSIGN).user(demandeAffecterLimite).system(affecteLimite)
	    	.step(WITHDRAW).user(demandeRetrait).system(retire).reactWhile(compteOuvert)
	    	.step(REPAY).user(demandeRemboursement).system(rembourse).reactWhile(compteOuvert)
	    	
	    .flow("Retirer à nouveau").after(REPAY)
	    	.step(WITHDRAW_AGAIN).user(demandeRetrait).system(retire)
	    	.step(REPEAT).continuesAt(WITHDRAW)
	    	
	    .flow("Cycle terminé").anytime()
	    	.step(CLOSE).on(demandeFermerCycle).system(fermeCycle)
	    	
	    .flow("Affecter la limite deux fois").condition(limiteDejaAffectee)
	    	.step(ASSIGN_TWICE).user(demandeAffecterLimite).system(lanceExceptionAffecterLimite)
	    	
	    .flow("Trop de retraits").condition(tropDeRetraitsDansCycle) 
	    	.step(WITHDRAW_TOO_OFTEN).user(demandeRetrait).system(lanceExceptionTropDeRetraits)
	.build();
```

La documentation [générée à partir de ce code](https://github.com/bertilmuth/requirementsascode/tree/master/requirementsascodeextract) suit.

DOCUMENTATION GÉNÉRÉE - DÉBUT

### **Utiliser une carte de crédit**

#### **Flux de base**

**Affecter la limite** : L'utilisateur demande à affecter la limite. Le système affecte la limite.  
**Retirer** : Tant que le compte est ouvert : L'utilisateur demande un retrait. Le système retire.  
**Rembourser** : Tant que le compte est ouvert : L'utilisateur demande un remboursement. Le système rembourse.

#### Retirer à nouveau

Après Rembourser :  
**Retirer à nouveau** : L'utilisateur demande un retrait. Le système retire.  
**Répéter** : Le système continue à Retirer.

#### Cycle terminé

À tout moment :  
**Fermer le cycle** : Gère DemandeFermerCycle : Le système ferme le cycle.

#### Affecter la limite deux fois

À tout moment, lorsque la limite est déjà affectée :  
**Affecter la limite deux fois** : L'utilisateur demande à affecter la limite. Le système lance une exception d'affectation de limite.

#### Trop de retraits

À tout moment, lorsqu'il y a trop de retraits dans le cycle :  
**Retirer trop souvent** : Le système lance une exception de trop de retraits.

DOCUMENTATION GÉNÉRÉE - FIN

Le même code contrôle le comportement de l'application et est la source de la documentation. L'avantage est évident : Vous pouvez générer de la documentation avec peu d'efforts. Et elle reflète le comportement réel du logiciel.

Bien sûr, cette approche nécessite également de la discipline. Surtout du côté des développeurs. Avant d'utiliser une approche, vous devriez l'essayer. Est-elle adaptée au type de logiciel développé ?

De plus, vous ne pouvez pas atteindre l'exhaustivité avec une telle approche. Par exemple, vous ne pouvez pas générer des exigences de qualité comme la robustesse à partir du code. Les compromis de conception ne font pas non plus partie du code.

J'attends avec impatience vos retours. Quelles options de documentation à long terme utilisez-_vous_ ?

_Cet article a été publié pour la première fois sur le_ [_HOOD Blog_](https://blog.hood-group.com/blog/2017/05/10/anforderungen-langfristig-dokumentieren-im-agilen-umfeld/) _en allemand. Si vous souhaitez suivre ce que je fais ou me laisser un mot, suivez-moi sur [dev.to](https://dev.to/bertilmuth), [LinkedIn](https://www.linkedin.com/in/bertilmuth/) ou [twitter](https://twitter.com/BertilMuth). Ou visitez mon [projet GitHub](https://github.com/bertilmuth/requirementsascode).