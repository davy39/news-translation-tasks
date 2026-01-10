---
title: Comment obtenir les meilleures performances de vos applications Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-04T21:43:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-the-best-performance-out-of-your-angular-apps-d5132a6c3335
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ryh4WCX9tu1IdgFd
tags:
- name: Angular
  slug: angular
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: UI
  slug: ui
seo_title: Comment obtenir les meilleures performances de vos applications Angular
seo_desc: 'By Mark Grichanik

  Angular is a great framework and can be used for developing large scale applications,
  but can be tricky to fine tune and achieve good load time and run-time performance.
  In this post, I’ll detail some best practices I have learned a...'
---

Par Mark Grichanik

Angular est un excellent framework et peut être utilisé pour développer des applications à grande échelle, mais il peut être délicat à optimiser pour obtenir un bon temps de chargement et des performances d'exécution. Dans cet article, je vais détailler certaines bonnes pratiques que j'ai apprises en cours de route, afin que vous ne fassiez pas les mêmes erreurs que moi.

### Détection des changements

La détection des changements est le mécanisme d'Angular pour vérifier s'il y a des valeurs qui ont été modifiées et nécessitent une mise à jour de la vue. Par défaut, Angular exécute la détection des changements avec presque chaque interaction utilisateur. Pour savoir si la vue doit être rendue à nouveau, Angular accède à la nouvelle valeur mise à jour, la compare avec l'ancienne et prend une décision. À mesure que votre application grandit, elle inclura de nombreuses expressions, et avoir un cycle de détection des changements sur chacune d'entre elles causera un problème de performance.

Nous pouvons optimiser les choses si nous créons un composant 'dumb' avec un certain attribut pour gérer les cycles de détection des changements. Ce composant repose uniquement sur des données d'entrée non spécifiques et, de cette manière, nous pouvons dire à Angular de n'exécuter la détection des changements que lorsqu'une entrée change ou lorsque nous la déclenchons manuellement. Lorsqu'un type de référence est immutable, chaque fois que l'objet est mis à jour, la référence dans la mémoire stack devra changer. Maintenant, nous pouvons avoir une simple vérification de référence sur l'objet entre l'adresse mémoire et la stack. Si l'adresse mémoire a changé, alors nous vérifions toutes les valeurs. Cela permettra de sauter la détection des changements dans ce composant.

Nous devons garder à l'esprit que les types primitifs tels que les nombres, les booléens, les chaînes de caractères, etc., sont passés par valeur. Les objets, les tableaux et les fonctions sont également passés par valeur, mais la valeur est une copie d'une référence.

> Vous pouvez trouver plus de détails à ce sujet [ici](https://codeburst.io/explaining-value-vs-reference-in-javascript-647a975e12a0).

Et maintenant, nous allons voir deux exemples de la façon dont cela est implémenté.

#### Exemple : _ChangeDetectionStrategy.Default_

**Vous n'avez pas à spécifier le type de changeDetection, il sera 'ChangeDetectionStrategy.Default' par défaut.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*CmTLsaZ6lBFG2nLr23UEnw.gif)
_Détection des changements par défaut_

![Image](https://cdn-media-1.freecodecamp.org/images/0*M2e8BlgCZ2xEY51A)
_Photo par [Unsplash](https://unsplash.com/@timmossholder?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Tim Mossholder</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### ChangeDetectionStrategy.OnPush

Pour utiliser la détection des changements OnPush, nous devons modifier le composant enfant du premier exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2H5bcmDVupujYig-KKUNTQ.gif)
_Détection des changements OnPush_

### Minimiser les manipulations du DOM

Si vous avez une liste de données récupérées depuis un serveur et que vous devez les afficher, vous utilisez probablement la directive Angular, [**_ngFor_**](https://angular.io/api/common/NgForOf)**_._** Angular créera un nouveau template pour chaque élément de cette liste.

Si à un moment donné certaines des données ont été modifiées, Angular ne peut pas vraiment le savoir et remplacera toute la liste, au lieu de seulement les éléments qui ont été modifiés. Pour améliorer cela, Angular nous fournit la fonction `trackBy`. `trackBy` prend une fonction qui a deux arguments : `index` et `[item](https://angular.io/api/core/IterableChangeRecord#item)`. Si `trackBy` est donné, Angular suit les changements par la valeur de retour de la fonction.

Syntaxe :

L'utilisation la plus courante est de retourner simplement l'index lui-même ou item.id comme identifiant unique pour l'élément : `trackByFn(index, item){ return item.id; }`.

Avec cela, Angular peut suivre quels éléments ont été ajoutés ou supprimés selon l'identifiant unique et créer ou détruire uniquement les éléments qui ont été modifiés.

### Éviter d'utiliser des méthodes dans votre template

Bien qu'il soit très pratique d'utiliser des méthodes dans les templates Angular, Angular les recalculera à chaque détection de changement. Pour les grandes listes, cela affectera le temps de rendu et l'application peut même se bloquer en raison d'une consommation de mémoire énorme. Dans l'exemple suivant, Angular exécutera `getNumberOfCars` à chaque cycle de détection de changement (par exemple, lors de l'ajout d'une nouvelle ligne).

Comment pouvons-nous gérer cette situation ? Nous pouvons pré-calculer les résultats et ensuite accéder simplement aux données que nous avons calculées. Dans notre exemple, nous pouvons ajouter un nouvel attribut à l'objet person, vehiclesNumber, qui contient à l'avance le nombre de véhicules que chaque personne possède. Une autre façon de faire cela est d'implémenter la méthode getNumberOfCars comme un pipe pur.

Selon la [documentation des pipes Angular](https://angular.io/guide/pipes) :

> Angular exécute un _pipe pur_ uniquement lorsqu'il détecte un _changement pur_ de la valeur d'entrée. Un changement pur est soit un changement de valeur d'entrée primitive (`String`, `Number`, `Boolean`, `Symbol`) soit un changement de référence d'objet (`Date`, `Array`, `Function`, `Object`).

> Angular ignore les changements à l'intérieur des objets (composites).

> Cela peut sembler restrictif mais c'est aussi rapide. Une vérification de référence d'objet est rapide — beaucoup plus rapide qu'une vérification approfondie des différences — donc Angular peut rapidement déterminer s'il peut sauter à la fois l'exécution du pipe et une mise à jour de la vue.

Le pipe sera toujours exécuté à chaque cycle de détection de changement. Cependant, si un pipe est exécuté plus d'une fois avec les mêmes paramètres, les résultats de la première exécution sont retournés. Cela signifie qu'Angular mettra en cache les résultats pour de meilleures performances.

Voyons un exemple.

Sans un pipe :

![Image](https://cdn-media-1.freecodecamp.org/images/1*E10fN3t0GC2PvG6cvhkhRw.gif)

Alors qu'avec un pipe, nous obtiendrons :

Nous pouvons voir qu'il ne recalculera que sur les nouvelles données, au lieu de toute la liste.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1u5T_iGl9h5uM-TBF5uzYg.gif)

### Utiliser le flag Prod en production

Cela désactivera le mode de développement d'Angular, ce qui désactive les assertions et autres vérifications dans le framework. Cela augmentera également vos performances. Vous pouvez trouver plus de détails [ici](https://angular.io/api/core/enableProdMode).

### Ne pas utiliser console.log dans le code de production

Les impressions console.log peuvent vraiment ralentir votre application, car il faut un certain temps pour calculer ce que vous voulez imprimer. De plus, pour les informations longues, cela consommera également plus de temps pour le processus d'impression.

### Ne pas oublier de se désabonner de vos observables

Votre abonnement conserve une référence à votre instance de composant. Si vous ne vous désabonnez pas, l'instance ne sera pas effacée par le garbage collector, ce qui provoquera une fuite de mémoire. Vous pouvez vous désabonner facilement en utilisant `ngOnDestory(){this.subscription.unsubscribe();}`. Vous pouvez en lire plus à ce sujet [ici](https://angular.io/guide/observables).

### Mots de la fin

Si vous rencontrez des problèmes, n'hésitez pas à me contacter à : [_markgrichanik[at]gmail[dot]com_](mailto:markgrichanik@gmail.com).

J'adorerais également entendre vos retours/conseils lorsque vous travaillez sur des applications à grande échelle avec Angular.

> Si vous avez aimé cet article, ? pour que d'autres puissent le lire également