---
title: Signaux dans Angular – Comment écrire un code plus réactif
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-05T00:53:15.000Z'
originalURL: https://freecodecamp.org/news/angular-signals
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/thumbnail.png
tags:
- name: Angular
  slug: angular
seo_title: Signaux dans Angular – Comment écrire un code plus réactif
seo_desc: 'By Deborah Kurata

  An exciting new feature is coming to Angular: signals! Signals provide a new way
  for our code to tell our templates (and other code) that our data has changed. This
  improves Angular''s change detection, which also improves performanc...'
---

Par Deborah Kurata

Une nouvelle fonctionnalité passionnante arrive dans Angular : les signaux ! Les signaux offrent une nouvelle façon pour notre code d'indiquer à nos templates (et à d'autres codes) que nos données ont changé. Cela améliore la détection des changements dans Angular, ce qui améliore également les performances et rend notre code plus réactif.

Vous pouvez essayer cette nouvelle fonctionnalité puissante dès maintenant. Les signaux sont disponibles en préversion pour les développeurs dans Angular v16, dont la sortie est prévue en mai 2023. Vous pouvez obtenir des versions préliminaires d'Angular v16 pour l'essayer dès maintenant. Je vais vous expliquer comment faire plus tard dans ce tutoriel.

Regardez la vidéo associée ici pour les concepts et une démonstration :

%[https://youtu.be/oqYQG7QMdzw]

Trouvez le code exemple ici : https://stackblitz.com/edit/angular-signals-deborahk

Avant de plonger dans les détails du "quoi ?" et du "comment ?", commençons par le "pourquoi ?". Pourquoi voudriez-vous utiliser cette nouvelle fonctionnalité des signaux ?

## **Pourquoi avons-nous besoin des signaux ?**

Commençons par un exemple simple sans utiliser de signaux. Supposons que vous écrivez du code pour effectuer quelques opérations mathématiques de base.

```typescript
let x = 5;
let y = 3;
let z = x + y;
console.log(z);
```

Que fait ce code dans la console ? Oui, il affiche `8`.

Plus tard dans le code, nous changeons la valeur de `x`. Que fait `z` maintenant ?

```typescript
let x = 5;
let y = 3;
let z = x + y;
console.log(z);

x = 10;
console.log(z);
```

Il affiche toujours `8` ! C'est parce qu'une valeur est assignée à `z` lorsque l'expression est évaluée pour la première fois. La variable `z` ne réagit pas aux changements de `x` ou `y`.

Mais nous voulons que nos variables réagissent aux changements !

L'une des raisons pour lesquelles nous utilisons Angular est de construire des sites web réactifs, comme le montre la Figure 1. Lorsque l'utilisateur met à jour la quantité, les variables associées (comme le sous-total et la taxe) doivent réagir et ajuster les coûts. Si l'utilisateur choisit de supprimer un article du panier, nous voulons à nouveau que les variables associées réagissent et recalculent correctement les coûts.

![Image](https://lh5.googleusercontent.com/b3SbnD_bufoicCX2VGyQiA624LQEC7yIEAVeEj0aVHjxvwmNnTPs-qE565koSuPWUrjAj-UDSw9otj6fXRWHPtr9jce2fnLt8FFAiLP0KRijjpuUiN_cb9lFwe_IbmsSWSzWqV36zBa8Bsnh7ciX4zo)
_Figure 1. Le panier réagit et recalcule lorsque l'utilisateur change la quantité._

Avec les signaux, notre code peut être plus réactif. Notre exemple précédent implémenté avec des signaux ressemblerait à ceci :

```typescript
const x = signal(5);
const y = signal(3);
const z = computed(() => x() + y());
console.log(z()); // 8

x.set(10);
console.log(z()); // 13
```

Nous examinerons cette syntaxe en détail sous peu. Pour l'instant, le code ci-dessus définit deux signaux : `x` et `y` et leur donne des valeurs initiales de `5` et `3`. Nous définissons ensuite un signal calculé, `z`, qui est la somme de `x` et `y`. Comme les signaux fournissent des notifications de changement, lorsque les signaux `x` ou `y` changent, toute valeur calculée à partir de ces signaux sera automatiquement recalculée. Ce code est maintenant réactif ! Bien !

Les signaux calculés réagissent et recalculent lorsque l'un de leurs signaux dépendants change. Si un signal est lié dans un template, lorsque le signal change, la détection des changements d'Angular met automatiquement à jour toute vue qui lit le signal. Et l'utilisateur voit la valeur modifiée.

Donc la réponse à "pourquoi avons-nous besoin des signaux ?" est :

* Les signaux fournissent plus de réactivité
* L'utilisation de signaux nous donne un contrôle plus fin sur la détection des changements, ce qui peut améliorer les performances.

Plongeons un peu plus profondément dans ce qu'est un signal et comment il est utilisé.

## **Qu'est-ce qu'un signal ?**

Vous pouvez penser à un signal comme une valeur plus une notification de changement. Un signal est simplement un type spécial de variable qui contient une valeur. Mais contrairement aux autres variables, un signal fournit également une notification lorsque la valeur de la variable change.

Pensez à une variable normale comme une étagère, comme sur le côté gauche de la Figure 2. Lorsqu'une valeur est assignée à la variable, elle se trouve sur cette étagère. Tout code dans la portée peut simplement lire cette variable sur l'étagère.

![Image](https://lh6.googleusercontent.com/VNW2DY2fkiBRNox5DIGkh2qr_yRgurq7I3vLumHSqT2ACNKq6I3GiGcMpVvU6f2AImTNIJ3quMh7lzerxfRjD3WBiLPEKBWGRgxGfvsrWpwuvBpvbpllPKJ-lZWHzQLRBguqAHWnITJU3xajiV2BoZM)
_Figure 2. Métaphoriquement, une variable normale se trouve sur une étagère. Un signal est stocké dans une boîte qui brille lorsqu'il change._

Un signal est plus comme une boîte, comme le montre le côté droit de la Figure 2. Créer un signal, c'est métaphoriquement créer une boîte et mettre la valeur à l'intérieur de cette boîte. La boîte brille lorsque la valeur du signal change. Pour lire le signal, ouvrez d'abord la boîte en utilisant des parenthèses : `x()`. Techniquement parlant, nous appelons la fonction getter du signal pour lire le signal.

Nous avons maintenant la réponse à "qu'est-ce qu'un signal ?" :

* Un signal est une variable + une notification de changement
* Un signal est réactif, et est appelé une "primitive réactive"
* Un signal a toujours une valeur
* Un signal est synchrone
* Un signal n'est _pas_ un remplacement pour RxJS et les Observables pour les opérations asynchrones, comme `http.get`

Où pouvons-nous utiliser les signaux ?

* Utilisez-les dans les **composants** pour suivre l'état local du composant
* Utilisez-les dans les **directives**
* Utilisez-les dans un **service** pour partager l'état entre les composants
* Lisez-les dans un **template** pour afficher les valeurs des signaux
* Ou utilisez-les **ailleurs** dans votre code

Ensuite, voyons comment créer et utiliser des signaux.

## **Comment créer un signal**

Pour utiliser un signal, vous devez d'abord en créer un.

```typescript
quantity = signal<number>(1);
```

La syntaxe ci-dessus crée et initialise un signal en utilisant la fonction constructeur de signal.

Optionnellement, fournissez un paramètre de type générique pour définir le type de données du signal. Un signal peut être une chaîne, un nombre, un tableau, un objet ou tout type de données. Dans de nombreux cas, le type de données peut être inféré et le paramètre de type générique est inutile.

Passez au constructeur la valeur par défaut du signal. Un signal a toujours une valeur, commençant par cette valeur par défaut.

Voici quelques exemples supplémentaires :

```typescript
quantity = signal(1);

qtyAvailable = signal([1, 2, 3, 4, 5, 6]);

selectedVehicle = signal<Vehicle>({ 
  id: 1,
  name: 'AT-AT', 
  price: 19416.13
});

vehicles = signal<Vehicle[]>([]);
```

La première ligne de code ci-dessus crée un signal numérique avec une valeur par défaut de `1`. Parce que la valeur par défaut est un nombre, `quantity` est un signal qui contient un nombre. Le paramètre de type générique n'est pas nécessaire.

La deuxième ligne est un signal qui contient un tableau de nombres. La valeur par défaut fournit un tableau de valeurs de 1 à 6. Encore une fois, le paramètre de type générique n'est pas nécessaire dans ce cas car il peut être inféré à partir de la valeur par défaut.

Le signal `selectedVehicle` contient un objet `Vehicle`. Dans cet exemple, le type ne peut pas être inféré, donc nous spécifions un paramètre de type générique de `Vehicle`.

Le signal `vehicles` contient un tableau d'objets `Vehicle`. Sa valeur par défaut est un tableau vide. Pour typer fortement le tableau, nous ajoutons un paramètre de type générique de `<Vehicle[]>`.

Un signal créé avec la fonction constructeur de signal est modifiable, donc vous pouvez le définir à une nouvelle valeur, le mettre à jour en fonction de la valeur actuelle, ou modifier son contenu. Nous verrons des exemples de ces opérations sous peu.

Une fois que vous avez créé un signal, vous pouvez vouloir lire sa valeur.

## **Comment lire un signal**

Plus tôt, nous avons représenté un signal comme une boîte. Métaphoriquement parlant, pour lire la valeur d'un signal, vous devez d'abord ouvrir la boîte. Vous faites cela en ajoutant des parenthèses comme montré ci-dessous.

```typescript
quantity();
```

Commencez par le nom du signal et suivez-le avec des parenthèses ouvertes et fermantes. Techniquement parlant, cela appelle la fonction getter du signal. La fonction getter est créée en arrière-plan – vous ne la verrez pas dans votre code.

Lorsque vous travaillez avec Angular, un endroit courant pour lire les signaux est dans le template.

```html
<select
    [ngModel]="quantity()"
    (change)="onQuantitySelected($any($event.target).value)">
  <option *ngFor="let q of qtyAvailable()">{{ q }}</option>
</select>

<div>Véhicule : {{ selectedVehicle().name }}</div>
<div>Prix : {{ selectedVehicle().price }}</div>
<div [style.color]="color()">Total : {{ totalPrice() }}</div>
```

Le template ci-dessus affiche une boîte de sélection pour la sélection d'une quantité. Le `[ngModel]` lit la valeur du signal `quantity`, se liant à cette valeur.

Le binding de l'événement `change` appelle la méthode `onQuantitySelected()` dans le composant.

L'élément `option` utilise `ngFor` pour itérer à travers chaque élément de tableau dans le signal `qtyAvailable`. Il lit le signal et crée une option `select` pour chaque élément de tableau.

En dessous de l'élément `select` se trouvent trois éléments `div`. Le premier lit le signal `selectedVehicle`, puis accède à sa propriété `name`. Le deuxième élément `div` lit le signal `selectedVehicle`, puis affiche sa propriété `price`. Le dernier élément `div` lit le signal `totalPrice` (que nous n'avons pas encore défini). Et il définit la couleur du texte à la valeur du signal `color` (que nous n'avons pas non plus défini).

Il est important de noter que la lecture d'un signal lit toujours la valeur actuelle du signal. Le code n'a aucune connaissance des valeurs précédentes du signal.

Lorsque l'utilisateur choisit une quantité différente dans l'élément `select`, nous voulons changer la valeur du signal `quantity`. De cette façon, le signal `quantity` devient la "source de vérité" pour la quantité sélectionnée par l'utilisateur. Voyons comment faire cela ensuite.

## **Comment changer la valeur d'un signal**

La méthode `set` du signal remplace la valeur d'un signal par une nouvelle valeur. Elle ouvre essentiellement la boîte, retire l'élément actuel et met un nouvel élément à sa place.

```typescript
this.quantity.set(qty);
```

Un scénario courant est de changer la valeur du signal en fonction d'une action de l'utilisateur. Par exemple :

* L'utilisateur sélectionne une nouvelle quantité en utilisant l'élément `select`
* Le binding de l'événement de l'élément `select` appelle la méthode `onQuantitySelected()` et passe la quantité sélectionnée
* L'action de l'utilisateur est gérée dans ce gestionnaire d'événements dans le composant
* La nouvelle valeur est définie dans le signal `quantity`.

Voici un exemple de gestionnaire d'événements :

```typescript
onQuantitySelected(qty: number) {
  this.quantity.set(qty);
}
```

Chaque fois que le signal est défini, le code notifie tous les consommateurs que le signal a changé. Dans ce contexte, un _consommateur_ est tout code qui est intéressé à recevoir des notifications de changement.

Comment le consommateur indique-t-il qu'il est intéressé à recevoir des notifications sur un signal particulier ?

Si **le code lit un signal**, ce code est notifié lorsque le signal change.

Si un **template lit un signal**, ce template est notifié lorsque le signal change et la vue est programmée pour être réaffichée.

Ainsi, l'acte de lire un signal enregistre l'intérêt du consommateur à surveiller ce signal. L'équipe Angular appelle cela la **règle d'or** des composants de signal : "la détection des changements pour un composant sera programmée lorsque _et seulement lorsque_ un signal lu dans le template notifie Angular qu'il a changé."

Voici un exemple pour illustrer le processus. Supposons qu'il y a un certain travail en cours dans la méthode ci-dessous qui doit ajuster la quantité. Peut-être que si la quantité est de 5 ou plus, vous en obtenez un gratuit, par exemple. Le point est que le signal `quantity` pourrait changer plusieurs fois au cours de l'exécution de la méthode.

```typescript
onQuantitySelected(qty: number) {
  this.quantity.set(qty);
  
  this.quantity.set(5);
  this.quantity.set(42);
}
```

La quantité est affichée dans le template en utilisant le binding d'Angular comme montré ci-dessous. Puisque le binding _lit_ le signal `quantity`, le template enregistre son intérêt à recevoir des notifications de changement.

```html
{{ quantity() }}
```

Lorsque l'utilisateur sélectionne une quantité, la méthode `onQuantitySelected()` s'exécute. Le code dans la méthode définit d'abord le signal à la quantité sélectionnée par l'utilisateur. Lorsque le nouveau signal est défini, le signal génère une notification. À ce stade, la détection des changements d'Angular est programmée pour s'exécuter. Mais elle n'a pas l'occasion de s'exécuter jusqu'à _après_ l'exécution de la méthode `onQuantitySelected()`.

La méthode `onQuantitySelected()` continue, définissant le signal à `5`. Le signal génère une autre notification de changement. Encore une fois, la détection des changements d'Angular est rappelée qu'elle doit s'exécuter, mais elle ne peut toujours pas s'exécuter parce que la méthode `onQuantitySelected()` est toujours en cours d'exécution. La méthode définit ensuite le signal à `42` et le processus se répète.

Lorsque la méthode `onQuantitySelected()` a terminé son exécution, la détection des changements d'Angular peut enfin s'exécuter. Le template lit le signal et obtient la valeur actuelle de ce signal, qui est `42`. Le template n'est pas conscient des valeurs précédentes du signal. La vue est ensuite réaffichée, et la nouvelle valeur du signal `quantity` est affichée.

Si un signal est modifié, tout consommateur intéressé par la lecture de ce signal est notifié. Mais le consommateur ne reçoit pas la nouvelle valeur. La prochaine fois que c'est son tour de s'exécuter, le consommateur lit la valeur actuelle du signal.

Si vous êtes familier avec RxJS et les Observables, les signaux sont assez différents. Les signaux n'_émettent_ pas de valeurs comme le font les Observables. Et les signaux ne nécessitent pas d'abonnement.

En plus de `set()`, il existe deux autres façons de changer un signal : `update()` et `mutate()`.

La méthode `set()` remplace un signal par une nouvelle valeur, remplaçant métaphoriquement le contenu de la boîte du signal. Passez la nouvelle valeur dans la méthode set.

```typescript
// Remplacer la valeur
this.quantity.set(qty);
```

La méthode `update()` met à jour le signal en fonction de sa valeur actuelle. Passez à la méthode update une fonction fléchée. La fonction fléchée fournit la valeur actuelle du signal afin que vous puissiez la mettre à jour selon vos besoins. Dans le code ci-dessous, la quantité est doublée.

```typescript
// Mettre à jour la valeur en fonction de la valeur actuelle
this.quantity.update(qty => qty * 2);
```

La méthode `mutate()` modifie le contenu d'une valeur de signal, et non la valeur du signal elle-même. Utilisez-la avec des tableaux pour modifier les éléments du tableau, et des objets pour modifier les propriétés de l'objet. Dans le code ci-dessous, le prix d'un véhicule est augmenté de 20 %.

```typescript
this.selectedVehicle.mutate(v => v.price = v.price + (v.price * .20));
```

Quelle que soit la manière dont le signal est modifié, les consommateurs sont notifiés que le signal a changé. Les consommateurs peuvent ensuite lire la nouvelle valeur du signal lorsqu'il est leur tour de s'exécuter.

## **Comment définir un signal calculé**

Souvent, nous avons des variables dans notre code qui dépendent d'autres variables. Par exemple, le prix total d'un article est le prix de cet article multiplié par la quantité souhaitée de cet article. Si l'utilisateur change la quantité, nous voulons changer le prix total. Pour cela, nous utilisons des **signaux calculés**.

Définissez un signal calculé en appelant la fonction de création computed. La fonction `computed()` crée un nouveau signal qui dépend d'autres signaux.

Passez à la fonction computed une fonction de calcul qui effectue l'opération souhaitée. L'opération lit la valeur d'un ou plusieurs signaux pour effectuer son calcul.

```typescript
totalPrice = computed(() => this.selectedVehicle().price * this.quantity());

color = computed(() => this.totalPrice() > 50000 ? 'green' : 'blue');
```

La première ligne de code ci-dessus définit un signal calculé `totalPrice` en appelant la fonction de création `computed()`. La fonction de calcul passée dans cette fonction computed lit les signaux `selectedVehicle` et `quantity`. Si l'un ou l'autre signal change, ce signal calculé est notifié et sera mis à jour lorsqu'il sera son tour de s'exécuter.

La deuxième ligne de code définit un signal calculé `color`. Il définit la couleur sur `green` ou `blue` en fonction de la valeur du signal `totalPrice`. Le template peut se lier à ce signal pour afficher le style approprié.

Un signal calculé est en lecture seule. Il **ne peut pas** être modifié avec `set()`, `update()` ou `mutate()`.

La valeur d'un signal calculé est recalculée lorsque :

* Un ou plusieurs de ses signaux dépendants est changé.
* ET la valeur du signal calculé est lue.

La valeur du signal calculé est _mémoisée_, ce qui signifie qu'elle stocke le résultat calculé. Cette valeur calculée est réutilisée la prochaine fois que la valeur calculée est lue.

Supposons par exemple que nous avons ceci dans notre template :

```typescript
Prix étendu : {{ totalPrice() }}
Prix total : {{ totalPrice() }}
Montant dû : {{ totalPrice() }}
```

La première fois que le template lit le signal calculé `totalPrice`, la valeur est calculée et stockée en mémoire. Les deux autres fois que le signal `totalPrice` est lu, la valeur stockée est réutilisée. La valeur n'est pas recalculée sauf si l'un de ses signaux dépendants change.

## **Comment utiliser un effet**

Il peut y avoir des moments où vous devez exécuter du code lorsqu'un signal change, et que ce code a des effets secondaires. Par effets secondaires, je veux dire du code qui appelle une API ou effectue une autre opération non liée au signal. Dans ces cas, vous utiliserez un `effect()`.

Par exemple, vous voulez déboguer vos signaux et journaliser la valeur du signal chaque fois que le code réagit à un changement de ce signal. Appeler `console.log()` est un effet secondaire.

Pour définir un effet, appelez la fonction de création `effect()`. Passez à la fonction l'opération à effectuer. Cette opération est réexécutée chaque fois que le code réagit à un changement dans un signal dépendant.

```typescript
effect(() => console.log(this.selectedVehicle()));
```

La fonction `effect()` peut être appelée dans d'autres fonctions. Comme l'effet met en place un gestionnaire, il est souvent appelé dans le constructeur ou un autre code de démarrage.

Alternativement, un effet peut être défini de manière déclarative comme montré ci-dessous :

```typescript
e = effect(() => console.log(this.selectedVehicle()));
```

Un effet **ne doit pas** changer la valeur d'un signal. Si vous devez changer un signal en fonction d'un changement dans un signal dépendant, utilisez un signal calculé à la place.

Vous constaterez que vous n'utiliserez pas souvent les effets. Bien qu'ils soient utiles pour la journalisation ou l'appel d'autres API externes. (Mais ne les utilisez pas pour travailler avec RxJS et les Observables. Il y aura des fonctionnalités de signal pour convertir vers et depuis les Observables.)

## **Quand utiliser les signaux**

Voici quelques suggestions sur quand utiliser les signaux.

Tout d'abord, continuez à utiliser les gestionnaires d'événements dans un composant comme vous le faites maintenant pour les actions de l'utilisateur. Des actions telles qu'une sélection dans une liste déroulante, un clic sur un bouton ou une entrée dans une zone de texte.

Utilisez un signal ou un signal calculé dans un composant pour tout état qui pourrait changer. Dans ce contexte, l'état fait référence à toute donnée que le composant gère. Tout, d'un indicateur `isLoading` à la "page" de données actuellement affichée en passant par les critères de filtre sélectionnés par l'utilisateur, pourrait être des signaux. Les signaux sont particulièrement utiles lors de l'affichage de données dans le template lorsque ces données doivent réagir à d'autres actions.

Placez les signaux partagés dans les services. Le tableau des véhicules retourné dans un Observable pourrait être transformé en un signal. Tout total pourrait également être des signaux dans un service si ces signaux sont partagés entre les composants.

Continuez à utiliser les Observables pour les opérations asynchrones, comme `http.get()`. Il y a plus de fonctionnalités à venir pour les signaux afin de mapper un signal vers et depuis un Observable.

## **Conclusion**

Les signaux représentent une avancée majeure dans les capacités de programmation réactive d'Angular et les fonctionnalités de détection des changements.

Ce tutoriel a répondu aux questions : "Pourquoi ?", "Quoi ?" et "Comment ?". Et nous avons également abordé "Où ?" et "Quand ?".

Les signaux sont disponibles en préversion pour les développeurs dans Angular v16. Dans le cadre de cette préversion, les signaux sont intégrés dans le modèle de détection des changements existant. Les futures fonctionnalités des signaux devraient améliorer la détection des changements et marquer les composants pour vérification, quelque peu comme la détection des changements OnPush que nous avons aujourd'hui avec le pipe async.

Une façon facile d'essayer les signaux est d'utiliser stackblitz, qui est un éditeur en ligne qui fonctionne bien avec Angular et ne nécessite aucune installation. Pour utiliser stackblitz avec les signaux :

1. Accédez au site web de stackblitz : [www.stackblitz.com](http://www.stackblitz.com).
2. Cliquez sur l'icône Angular pour créer un projet Angular.
3. Modifiez le fichier `package.json` résultant et changez les versions des packages @angular à la dernière préversion d'Angular v16.
4. Enregistrez le projet pour rafraîchir les dépendances.
5. Essayez les signaux !

Pour voir ces étapes en action, consultez la démonstration fournie à la fin de cette vidéo :

%[https://youtu.be/oqYQG7QMdzw]

Ou commencez avec mon lien stackblitz : [https://stackblitz.com/edit/angular-signals-deborahk](https://stackblitz.com/edit/angular-signals-deborahk). Assurez-vous de fork mon projet pour essayer vos propres modifications.

Les signaux arrivent ! Ils amélioreront la réactivité de notre code et la détection des changements. Ils faciliteront la création et la lecture de notre code. Et ils sont très amusants !