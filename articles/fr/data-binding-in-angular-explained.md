---
title: Liaison de données dans Angular expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-07T23:19:00.000Z'
originalURL: https://freecodecamp.org/news/data-binding-in-angular-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cb2740569d1a4ca33ab.jpg
tags:
- name: Angular
  slug: angular
- name: Binding Data
  slug: binding-data
- name: toothbrush
  slug: toothbrush
seo_title: Liaison de données dans Angular expliquée
seo_desc: 'Data Binding

  Motivation

  Data often defines the look of an application. Interpreting that data into the user
  interface involves class logic (.component.ts) and a template view (.component.html).
  Angular connects them through data binding. Think of dat...'
---

# **Liaison de données**

### Motivation

Les données définissent souvent l'apparence d'une application. L'interprétation de ces données dans l'interface utilisateur implique une logique de classe (`.component.ts`) et une vue de modèle (`.component.html`). Angular les connecte grâce à la liaison de données. Considérez la liaison de données comme un outil pour l'interaction des composants.

### Composant et Modèle

Le composant stocke la plupart de sa logique et de ses données à l'intérieur de sa classe décorée avec `@Component`. Ce décorateur définit la classe comme un composant avec un modèle HTML. Le modèle du composant représente la classe au sein de l'application. L'accent ici doit être mis entre la classe du composant et le modèle HTML.

C'est là que la liaison de données se produit. Les propriétés et les événements des éléments reçoivent des valeurs. Ces valeurs, définies par la classe du composant, servent l'un des deux rôles suivants. L'un est de produire des données que le modèle reçoit ensuite. L'autre gère les événements émis par l'élément du modèle.

![Exemple de Code](https://raw.githubusercontent.com/sosmaniac-FCC/designatedata/master/image4.png)

Essayez d'utiliser cette image comme modèle mental pour la section suivante.

### Directions de Liaison

Il existe deux façons de lier les données : unidirectionnelle et bidirectionnelle. Angular utilise techniquement uniquement un flux de données unidirectionnel. Le flux bidirectionnel est finalement unidirectionnel. Il se produit en deux applications de flux unidirectionnel, une pour chaque direction. Plus d'informations à ce sujet plus tard.

Le flux unidirectionnel définit une interaction à sens unique. Soit le composant envoie des données au modèle, soit le modèle émet un événement vers la logique du composant. Les changements de données dans le cadre du modèle ne remontent pas à la classe du composant. L'émission d'événements est une transaction à sens unique commençant à partir des éléments du modèle.

Le bidirectionnel constitue les deux directions. Cela signifie que les changements apportés aux données dans la logique de classe ou le modèle HTML persistent à travers chacun d'eux. La portée des changements est la vue du composant. La vue comprend la classe et le modèle du composant ensemble.

### Propriétés des Éléments

Pour reconnaître les propriétés des éléments liés aux données, Angular utilise une syntaxe de crochets spéciale.

```typescript
// my.component.ts
@Component({
  templateUrl: './my.component.html'
})

export class MyComponent {
  value:type = /* une valeur de type */;
}
```

```html
<!-- my.component.html -->
<any-element [property]="value">innerHTML</any-element>
```

Suivez-moi sur ce point.

`[property]` reflète la propriété dans le nœud objet de l'élément du Domain Object Model (DOM). Ne confondez pas les propriétés d'objet avec les attributs d'un élément DOM. Les propriétés et les attributs partagent souvent le même nom et font la même chose. Il y a cependant une distinction claire.

Rappelez-vous que `attr` (attributs) est une seule propriété de l'objet DOM sous-jacent. Il est déclaré à l'instantiation du DOM avec des valeurs d'attribut correspondant à la définition de l'élément. Il conserve la même valeur après cela. Les propriétés ont chacune leur propre champ clé-valeur dans un nœud d'objet DOM. Ces propriétés sont mutables après l'instantiation.

Connaître la différence entre les attributs et les propriétés. Cela conduira à une meilleure compréhension de la manière dont Angular lie les données aux propriétés (liaison de propriétés). Angular ne lie presque jamais les données aux attributs d'un élément. Les exceptions à cela sont très rares. Une dernière fois : Angular lie les données du composant aux propriétés, pas aux attributs !

En revenant à l'exemple, les `[ … ]` dans l'assignation de propriété de l'élément ont une signification spéciale. Les crochets montrent que `property` est lié à `"value"` à droite de l'assignation.

`value` a également une signification spéciale dans le contexte des crochets. `value` seul est une chaîne littérale. Angular la lit et fait correspondre sa valeur aux membres de la classe du composant. Angular substituera la valeur de l'attribut membre correspondant. Cela fait bien sûr référence à la même classe de composant qui héberge le modèle HTML.

Le flux unidirectionnel des données du composant vers le modèle est complet. Le membre correspondant à l'assignation droite de la propriété entre crochets fournit la `value`. Notez que les changements de la valeur du membre dans la classe du composant se répercutent jusqu'au modèle. C'est le mécanisme de détection des changements d'Angular en action. Les changements dans la portée du modèle n'ont aucun effet sur le membre de la classe du composant.

Point clé à retenir : la classe du composant fournit les données tandis que le modèle les affiche.

J'ai oublié de mentionner que les valeurs de données peuvent également apparaître dans le `innerHTML` d'un composant. Ce dernier exemple implémente des doubles accolades. Angular reconnaît ces accolades et interpole les données de la classe du composant correspondante dans le `innerHTML` de la `div`.

```html
<div>La valeur du membre de la classe du composant 'value' est {{value}}.</div>
```

### Gestion des Événements

Si le composant fournit des données, alors le modèle fournit des événements.

```typescript
// my.component.ts
@Component({
  templateUrl: './my.component.html'
})

export class MyComponent {
  handler(event):void {
      // la fonction fait des choses
  }
}
```

```html
// my.component.html
<any-element (event)="handler($event)">innerHTML</any-element>
```

Cela fonctionne de manière similaire à la liaison de propriétés.

Le `(event)` concerne tout type d'événement valide. Par exemple, l'un des types d'événements les plus courants est `click`. Il est émis lorsque vous cliquez avec votre souris. Peu importe le type, `event` est lié à `"handler"` dans l'exemple. Les gestionnaires d'événements sont généralement des fonctions membres de la classe du composant.

Les `( … )` sont spéciaux pour Angular. Les parenthèses indiquent à Angular qu'un événement est lié à l'assignation droite de `handler`. L'événement lui-même provient de l'élément hôte.

Lorsque l'événement est émis, il transmet l'objet Event sous la forme de `$event`. Le `handler` correspond à la fonction `handler` de la classe du composant. L'échange unidirectionnel de l'élément lié à l'événement vers la classe du composant est complet.

L'émission d'événements à partir du gestionnaire, bien que possible, n'a pas d'impact sur l'élément du modèle. La liaison est après tout unidirectionnelle.

### Liaison Bidirectionnelle

Les formulaires de saisie fournissent un excellent exemple de la nécessité de la liaison bidirectionnelle. Les liaisons de données bidirectionnelles sont plus coûteuses que les liaisons d'événements ou de propriétés.

La liaison de données bidirectionnelle a son propre module. Avant de regarder cela, considérons l'exemple suivant.

```typescript
// my.component.ts
@Component({
  templateUrl: './my.component.html'
})
export class MyComponent {
  inputValue:string = "";

  handler(event) {
      this.inputValue = event.target.value;
  }
}
```

```html
<!-- my.component.html -->
<input (input)="handler($event)" [value]="inputValue">
```

Il est temps de décomposer cela.

Cet exemple combine les deux précédents. Cela explique pourquoi il est plus coûteux. En suivant la logique, supposons que l'utilisateur tape quelque chose dans l'élément de saisie. L'élément émet un événement `input` vers le `handler` de la classe du composant du modèle. Le gestionnaire attribue le membre de classe `inputValue` à la valeur de l'événement émis. Cela conclut la gestion/liaison de l'événement.

Passons maintenant à la liaison de propriétés. La valeur `inputValue` a été attribuée à une nouvelle valeur. Puisque `inputValue` est lié à la `value` de l'élément de saisie, son changement de données se répercute dans la propriété `value` de l'élément de saisie. La `value` de l'élément de saisie correspond à `inputValue`. Cela conclut la liaison de propriétés.

Vous l'avez compris. La liaison de données bidirectionnelle se produit avec les deux applications de liaison unidirectionnelle appliquées consécutivement. La syntaxe est un peu désordonnée cependant.

Heureusement, Angular fournit `NgModel` pour simplifier la syntaxe. L'exemple ci-dessous est synonyme de celui ci-dessus.

```typescript
// my.component.ts
@Component({
  templateUrl: './my.component.html'
})

export class MyComponent {
  inputValue:string = "";
}
```

```html
<!-- my.component.html -->
<input [(ngModel)]="inputValue">
```

`ngModel` est une belle commodité. Vous devez importer le FormsModule dans la racine de votre application avant de l'utiliser. Avec cela réglé, la liaison de données bidirectionnelle devient beaucoup plus facile à utiliser.

Pour renforcer tout ce que vous avez appris, consultez cette image de la [Documentation officielle d'Angular<sup>1</sup>](https://angular.io/guide/architecture-components#data-binding).

![Diagramme de Flux de Données](https://raw.githubusercontent.com/sosmaniac-FCC/designatedata/master/image2.png)

Vous pouvez résumer visuellement tout ce qui précède avec cette image. La documentation d'Angular contient de nombreuses autres images qui valent la peine d'être vues. Celle-ci devrait suffire étant donné la portée de cet article.

### Composant à Composant

Pour lier des données et des événements entre différents composants, vous devez utiliser les décorateurs @Input et @Output. Les composants Angular sont privés. Aucun des membres d'un composant n'est accessible depuis l'extérieur de sa vue native.

Le décorateur @Input indique qu'une valeur de membre est sourcée à partir de la fonction parente. Cela nécessite une visualisation pour mieux comprendre.

![Exemple de Code](https://raw.githubusercontent.com/sosmaniac-FCC/designatedata/master/image3_.png)

Remarquez le passage du membre `value` du parent au membre `property` de l'enfant. Cela ne serait pas possible si `property` n'avait pas de décorateur @Input. Le compilateur Angular en dépend.

Un autre exemple pour @Output montre comment un événement voyage de l'enfant au parent. Gardez à l'esprit que @Output concerne presque toujours les liaisons d'événements personnalisés.

![Exemple de Code](https://raw.githubusercontent.com/sosmaniac-FCC/designatedata/master/image1.png)

Assurez-vous d'importer `EventEmitter`, `@Input`, et `@Output` depuis `@angular/common` si vous avez l'intention de reproduire l'un de ces exemples.

## Conclusion

C'est un bon endroit pour s'arrêter. La liaison de données couvre un large éventail de cas d'utilisation. Ce sujet mérite d'être exploré plus avant sur le [site web d'Angular](https://angular.io/). Ce ne sont pas les seules façons de manipuler des données dans Angular. Voir les liens sous Ressources pour plus d'informations.