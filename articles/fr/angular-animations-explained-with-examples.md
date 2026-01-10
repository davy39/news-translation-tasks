---
title: Les animations Angular expliquées avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T01:50:00.000Z'
originalURL: https://freecodecamp.org/news/angular-animations-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ce2740569d1a4ca34b8.jpg
tags:
- name: Angular
  slug: angular
- name: animations
  slug: animations
- name: toothbrush
  slug: toothbrush
seo_title: Les animations Angular expliquées avec des exemples
seo_desc: 'Why use Animations?

  Modern web components frequently use animations. Cascading Style-sheets (CSS) arms
  developers with the tools to create impressive animations. Property transitions,
  uniquely named animations, multi-part keyframes are possible with ...'
---

# **Pourquoi utiliser les animations ?**

Les composants web modernes utilisent fréquemment des animations. Les feuilles de style en cascade (CSS) fournissent aux développeurs les outils pour créer des animations impressionnantes. Les transitions de propriétés, les animations nommées de manière unique, les keyframes en plusieurs parties sont possibles avec CSS. Les possibilités d'animation sont infinies grâce à CSS.

Dans une application web moderne, l'animation concentre l'attention de l'utilisateur. Les bonnes animations cherchent à guider l'attention de l'utilisateur de manière satisfaisante et productive. Les animations ne doivent pas être ennuyeuses pour l'utilisateur.

Les animations offrent un retour sous forme de mouvement. Elles montrent à l'utilisateur que l'application traite activement ses demandes. Quelque chose d'aussi simple qu'un appui visible sur un bouton ou un chargeur lorsque l'application doit charger capte l'attention de l'utilisateur.

Les animations continuent de devenir de plus en plus pertinentes dans le cas d'Angular. Google développe Angular tout en promouvant la philosophie Material Design. Elle encourage des interfaces utilisateur (UI) concises, complétées par des retours animés pour l'utilisateur. Cela rend les applications web quelque peu vivantes et amusantes à utiliser.

La communauté Angular développe une bibliothèque de widgets de base appelée [Material2](https://github.com/angular/material2). Ce projet ajoute une variété de modules de widgets à Angular. La plupart d'entre eux comportent des animations. Pour comprendre comment ils fonctionnent, cet article recommande d'étudier les animations CSS avant de continuer.

Les animations Angular sont la version rationalisée par le framework de ce que CSS fournit nativement. CSS est la technologie de base pour les animations Angular se produisant dans le navigateur web. CSS est hors du cadre de cet article. Il est temps de s'attaquer de front aux animations Angular.

## Installation des animations

Avant d'animer, le `BrowserAnimationsModule` doit être inclus dans le tableau des imports du module racine. Il est disponible depuis `@angular/platform-browser/animations`. Ce NgModule garantit que les animations fonctionnent pour la plateforme donnée. Cet article suppose le navigateur web standard pour chaque exemple.

Les animations Angular sont déclarées dans les métadonnées `@Component`. `@Component` décore une classe pour la distinguer comme un composant à Angular. Ses métadonnées contiennent des configurations de composant, y compris le champ `animations: []`. Chaque élément de tableau de ce champ représente un déclencheur d'animation (`AnimationTriggerMetadata`).

Les animations sont exclusives à leur composant hôte via les métadonnées du décorateur. Les animations ne peuvent être utilisées que dans le template du composant hôte. Les animations ne s'héritent pas aux enfants du composant. Il existe une solution simple pour cela.

Vous pouvez toujours créer un fichier séparé qui exporte un tableau. Toute classe de composant peut importer ce tableau depuis le haut de son fichier hôte. Le jeton de tableau importé va ensuite dans les métadonnées des animations du composant. Répétez ce processus pour tout autre composant nécessitant le même tableau dans leurs métadonnées d'animations.

La projection de contenu vous permet d'appliquer des animations au DOM de contenu du composant A. Le composant B enveloppant ce DOM de contenu peut projeter le contenu dans son propre template. Une fois cela fait, les animations du composant A ne sont pas annulées. Le composant B incorpore les animations de A par projection de contenu.

OK. Vous savez comment configurer les animations et où les déclarer. La mise en œuvre est l'étape suivante.

## Méthodes d'animation

Les animations Angular utilisent une série d'appels de méthodes importables depuis `@angular/animations`. Chaque élément du tableau des animations `@Component` commence par une seule méthode. Ses arguments se déroulent comme une séquence d'appels de méthodes de haut niveau. La liste suivante montre certaines des méthodes utilisées pour construire des animations Angular.

* `trigger(selector: string, AnimationMetadata[])`

retourne `AnimationTriggerMetadata`

* `state(data: string, AnimationStyleMetadata, options?: object)`

retourne `AnimationStateMetadata`

* `style(CSSKeyValues: object)`

retourne `AnimationStyleMetadata`

* `animate(timing: string|number, AnimationStyleMetadata|KeyframesMetadata)`

retourne `AnimationAnimateMetadata`

* `transition(stateChange: string, AnimationMetadata|AnimationMetadata[], options?: object)`

retourne `AnimationTransitionMetadata`

Bien qu'il existe certainement [plus de méthodes](https://angular.io/api/animations) parmi lesquelles choisir, ces cinq méthodes gèrent les bases. Essayer de comprendre ces méthodes principales sous forme de liste n'aide pas beaucoup. Des explications point par point suivies d'un exemple donneront un meilleur sens.

### trigger(selector: string, AnimationMetadata[])

La méthode `trigger(...)` encapsule un seul élément d'animation à l'intérieur du tableau des animations.

Le premier argument de la méthode `selector: string` correspond à l'attribut membre `[@selector]`. Il agit comme une directive d'attribut dans le template du composant. Il connecte essentiellement l'élément d'animation au template via un sélecteur d'attribut.

Le deuxième argument est un tableau contenant une liste de méthodes d'animation applicables. Le `trigger(...)` les regroupe toutes dans un seul tableau.

### state(data: string, AnimationStyleMetadata, options?: object)

La méthode `state(...)` définit l'état final de l'animation. Elle applique une liste de propriétés CSS à l'élément cible après la conclusion d'une animation. Cela permet de faire correspondre le CSS de l'élément animé à la résolution de l'animation.

Le premier argument correspond à la valeur des données liées à la liaison d'animation. C'est-à-dire que la valeur liée à `[@selector]` dans le template correspond au premier argument d'un `state(...)`. La valeur des données détermine l'état final. Le changement de la valeur détermine les moyens de l'animation (voir `transition(...)`).

Le deuxième argument contient les styles CSS qui s'appliquent à un élément après l'animation. Les styles sont passés en invoquant `style(...)` et en passant dans son argument les styles souhaités sous forme d'objet.

Une liste d'options occupe éventuellement le troisième argument. Les options par défaut de `state(...)` doivent rester inchangées sauf si une raison justifie le contraire.

### style(CSSKeyValues: object)

Vous avez peut-être remarqué `AnimationStyleMetadata` plusieurs fois dans la liste précédente. Le composant `style(...)` retourne exactement ce type de métadonnées. Partout où les styles CSS s'appliquent, la méthode `style(...)` doit être invoquée. Un objet contenant des styles CSS se substitue à son argument.

Bien sûr, les styles animables en CSS se reportent dans la méthode `style(...)` d'Angular. Certes, rien d'impossible pour CSS ne devient soudainement possible avec les animations Angular.

### animate(timing: string|number, AnimationStyleMetadata|AnimationKeyframesMetadata)

La fonction `animate(...)` accepte une expression de timing comme premier argument. Cet argument temporise, rythme et/ou retarde l'animation de la méthode. Cet argument accepte soit une expression numérique, soit une chaîne. Le formatage est expliqué [ici](https://angular.io/api/animations/animate#usage).

Le deuxième argument de `animate(...)` est la propriété CSS justifiant l'animation. Cela prend la forme de la méthode `style(...)` qui retourne `AnimationStyleMetadata`. Considérez `animate(...)` comme la méthode qui initie l'animation.

Une série de keyframes peut également s'appliquer au deuxième argument. Les keyframes sont une option plus avancée que cet article explique plus loin. Les keyframes distinguent diverses sections de l'animation.

`animate(...)` peut ne pas recevoir de deuxième argument. Dans ce cas, le timing de l'animation de la méthode ne s'applique qu'au CSS reflété dans les méthodes `state(...)`. Les changements de propriété dans les méthodes `state(...)` du déclencheur s'animeront.

### transition(changExpr: string, AnimationMetadata|AnimationMetadata[], options?: object)

`animate(...)` initie une animation tandis que `transition(...)` détermine quelle animation est initiée.

Le premier argument se compose d'une forme unique de micro-syntaxe. Il désigne un changement d'état (ou changement de données) en cours. Les données liées à la liaison d'animation du template (`[selector]="value"`) déterminent cette expression. La section à venir intitulée « État de l'animation » explique ce concept un peu plus loin.

Le deuxième argument de `transition(...)` comprend `AnimationMetadata` (retourné par `animate(...)`). L'argument accepte soit un tableau de `AnimationMetadata`, soit une seule instance.

La valeur du premier argument correspond à la valeur des données liées dans le template (`[selector]="value"`). Si une correspondance parfaite se produit, l'argument est évalué avec succès. Le deuxième argument initie alors une animation en réponse au succès du premier.

Une liste d'options occupe éventuellement le troisième argument. Les options par défaut de `transition(...)` doivent rester inchangées sauf si une raison justifie le contraire.

## Exemple d'animation

```typescript
import { Component, OnInit } from '@angular/core';
import { trigger, state, style, animate, transition } from '@angular/animations';

@Component({
  selector: 'app-example',
  template: `
  <h3>Cliquez sur le bouton pour changer sa couleur !</h3>
  <button (click)="toggleIsCorrect()"     // liaison d'événement
    [@toggleClick]="isGreen">Basculer !</button>  // liaison d'animation
    `,
    animations: [       // tableau de métadonnées
      trigger('toggleClick', [     // bloc de déclencheur
      state('true', style({      // CSS final suivant l'animation
        backgroundColor: 'green'
      })),
      state('false', style({
        backgroundColor: 'red'
      })),
      transition('true => false', animate('1000ms linear')),  // timing de l'animation
      transition('false => true', animate('1000ms linear'))
    ])
  ]        // fin du bloc de déclencheur
})
export class ExampleComponent {
  isGreen: string = 'true';

  toggleIsCorrect() {
    this.isGreen = this.isGreen === 'true' ? 'false' : 'true'; // changement de la valeur liée aux données
  }
}
```

L'exemple ci-dessus effectue un échange de couleur très simple à chaque clic sur le bouton. Bien sûr, les transitions de couleur se font rapidement avec un fondu linéaire selon `animate('1000ms linear')`. L'animation se lie au bouton en faisant correspondre le premier argument de `trigger(...)` à la liaison d'animation `[@toggleClick]`.

La liaison se lie à la valeur de `isGreen` de la classe du composant. Cette valeur détermine la couleur résultante telle que définie par les deux méthodes `style(...)` à l'intérieur du bloc `trigger(...)`. La liaison d'animation est unidirectionnelle de sorte que les changements apportés à `isGreen` dans la classe du composant notifient la liaison du template. C'est-à-dire, la liaison d'animation `[@toggleClick]`.

L'élément bouton dans le template a également un événement `click` qui lui est lié. Cliquer sur le bouton fait basculer les valeurs de `isGreen`. Cela change les données de la classe du composant. La liaison d'animation détecte cela et invoque sa méthode `trigger(...)` correspondante. Le `trigger(...)` se trouve dans le tableau des animations des métadonnées du composant. Deux choses se produisent lors de l'invocation du déclencheur.

La première occurrence concerne les deux méthodes `state(...)`. La nouvelle valeur de `isGreen` correspond au premier argument d'une méthode `state(...)`. Une fois qu'elle correspond, les styles CSS de `style(...)` s'appliquent à l'état final de l'élément hôte de la liaison d'animation. L'état final prend effet après toutes les animations.

Maintenant pour la deuxième occurrence. Le changement de données qui a invoqué la liaison d'animation est comparé aux deux méthodes `transition(...)`. L'une d'elles correspond au changement de données de leur premier argument. Le premier clic sur le bouton a fait passer `isGreen` de 'true' à 'false' ('true => false'). Cela signifie que la première méthode `transition(...)` active son deuxième argument.

La fonction `animate(...)` correspondant à la méthode `transition(...)` évaluée avec succès s'initie. Cette méthode définit la durée du fondu de couleur animé ainsi que le rythme du fondu. L'animation s'exécute et le bouton passe au rouge.

Ce processus peut se produire un nombre quelconque de fois après un clic sur le bouton. La `backgroundColor` du bouton cyclera entre le vert et le rouge avec un fondu linéaire.

## État de l'animation

La micro-syntaxe `transition(...)` mérite d'être abordée en détail. Angular détermine les animations et leur timing en évaluant cette syntaxe. Il existe les transitions d'état suivantes. Elles modélisent un changement de données lié à une liaison d'animation.

* `'someValue' => 'anotherValue'`

Un déclencheur d'animation où les données liées changent de 'someValue' à 'anotherValue'.

* `'anotherValue' => 'someValue'`

Un déclencheur d'animation où les données liées changent de 'anotherValue' à 'someValue'.

* `'someValue' <=> 'anotherValue'`

Les données changent de 'someValue' à 'anotherValue' ou vice versa.

Il existe également les états `void` et `*`. `void` indique que le composant entre ou sort du DOM. Cela est parfait pour les animations d'entrée et de sortie.

* `'someValue' => void` : le composant hôte des données liées quitte le DOM
* `void => 'someValue'` : le composant hôte des données liées entre dans le DOM

`*` désigne un état générique. Les états génériques peuvent être interprétés comme « n'importe quel état ». Cela inclut `void` plus tout autre changement des données liées.

## Keyframes

Cet article a abordé les bases de l'animation des applications Angular. Des techniques d'animation avancées existent aux côtés de ces bases. Le regroupement des keyframes est une telle technique. Elle est inspirée de la règle CSS `@keyframes`. Si vous avez travaillé avec les `@keyframes` CSS, vous comprenez déjà comment fonctionnent les keyframes dans Angular. Il s'agit simplement d'une question de syntaxe.

La méthode `keyframes(...)` est importée depuis `@angular/animations`. Elle passe dans le deuxième argument de `animate(...)` au lieu du `AnimationStyleMetadata` typique. La méthode `keyframes(...)` accepte un argument sous forme de tableau de `AnimationStyleMetadata`. Cela peut également être appelé un tableau de méthodes `style(...)`.

Chaque keyframe de l'animation va à l'intérieur du tableau `keyframes(...)`. Ces éléments de keyframe sont des méthodes `style(...)` prenant en charge la propriété `offset`. `offset` indique un point dans la durée de l'animation où ses propriétés de style accompagnantes doivent s'appliquer. Sa valeur s'étend de 0 (début de l'animation) à 1 (fin de l'animation).

```typescript
import { Component } from '@angular/core';
import { trigger, state, style, animate, transition, keyframes } from '@angular/animations';

@Component({
  selector: 'app-example',
  styles: [
    `.ball {
      position: relative;
      background-color: black;
      border-radius: 50%;
      top: 200px;
      height: 25px;
      width: 25px;
    }`
  ],
  template: `
  <h3>Animation de balle en arc</h3>
  <button (click)="toggleBounce()">Animer la balle !</button>
  <div [@animateArc]="arc" class="ball"></div>
  `,
  animations: [
    trigger('animateArc', [
      state('true', style({
        left: '400px',
        top: '200px'
      })),
      state('false', style({
        left: '0',
        top: '200px'
      })),
      transition('false => true', animate('1000ms linear', keyframes([
        style({ left: '0',     top: '200px', offset: 0 }),
        style({ left: '200px', top: '100px', offset: 0.50 }),
        style({ left: '400px', top: '200px', offset: 1 })
      ]))),
      transition('true => false', animate('1000ms linear', keyframes([
        style({ left: '400px', top: '200px', offset: 0 }),
        style({ left: '200px', top: '100px', offset: 0.50 }),
        style({ left: '0',     top: '200px', offset: 1 })
      ])))
    ])
  ]
})
export class ExampleComponent {
  arc: string = 'false';

  toggleBounce(){
    this.arc = this.arc === 'false' ? 'true' : 'false';
  }
}
```

La principale différence de l'exemple ci-dessus par rapport à l'autre exemple est le deuxième argument de `animate(...)`. Il contient maintenant une méthode `keyframes(...)` hébergeant un tableau de keyframes d'animation. Bien que l'animation elle-même soit également différente, la technique d'animation est similaire.

Cliquer sur le bouton fait traverser l'écran à la balle en arc. La balle se déplace selon les éléments du tableau de la méthode `keyframes(...)` (keyframes). Au point médian de l'animation (`offset: 0.50`), la balle change de trajectoire. Elle descend à sa hauteur d'origine tout en continuant à traverser l'écran. Cliquer à nouveau sur le bouton inverse l'animation.

`left` et `top` sont des propriétés animables après avoir défini `position: relative;` pour l'élément. La propriété `transform` peut effectuer des animations similaires basées sur le mouvement. `transform` est une propriété expansive mais entièrement animable.

Un nombre quelconque de keyframes peut exister entre les offsets 0 et 1. Des séquences d'animation complexes prennent la forme de keyframes. Elles sont l'une des nombreuses techniques avancées dans les animations Angular.

## Animations avec liaison d'hôte

Vous rencontrerez sans doute la situation où vous souhaitez attacher une animation à l'élément HTML d'un composant lui-même, au lieu d'un élément dans le template du composant. Cela nécessite un peu plus d'effort puisque vous ne pouvez pas simplement aller dans le HTML du template et attacher l'animation là. Au lieu de cela, vous devrez importer `HostBinding` et l'utiliser.

Le code minimal pour ce scénario est montré ci-dessous. Je vais réutiliser la même condition d'animation pour le code ci-dessus pour la cohérence et je ne montre aucun du code d'animation réel puisque vous pouvez facilement le trouver ci-dessus.

```typescript
import { Component, HostBinding } from '@angular/core';

@Component({
...
})
export class ExampleComponent {
  @HostBinding('@animateArc') get arcAnimation() {
    return this.arc;
  }
}
```

L'idée derrière l'animation du composant hôte est pratiquement la même que l'animation d'un élément du template, la seule différence étant votre manque d'accès à l'élément que vous animez. Vous devez toujours passer le nom de l'animation (`@animateArc`) lors de la déclaration du `HostBinding` et vous devez toujours retourner l'état actuel de l'animation (`this.arc`). Le nom de la fonction n'a pas vraiment d'importance, donc `arcAnimation` aurait pu être changé en n'importe quoi, tant qu'il n'entre pas en conflit avec les noms de propriétés existants sur le composant, et cela fonctionnerait parfaitement bien.

## Conclusion

Cela couvre les bases de l'animation avec Angular. Angular rend la configuration des animations très facile en utilisant l'Angular CLI. Commencer avec votre première animation ne nécessite qu'une seule classe de composant. N'oubliez pas que les animations sont limitées au template du composant. Exportez votre tableau de transitions depuis un fichier séparé si vous prévoyez de l'utiliser dans plusieurs composants.

Chaque utilitaire/méthode d'animation est exporté depuis `@angular/animations`. Ils travaillent tous ensemble pour fournir un système d'animation robuste inspiré de CSS. Il existe plus de méthodes que ce que cet article pourrait couvrir.

Maintenant que vous connaissez les bases, n'hésitez pas à explorer les liens ci-dessous pour plus d'informations sur les animations Angular.

## Plus d'informations sur les animations Angular :

* [Documentation Angular](https://angular.io/guide)
* [Comment utiliser l'animation avec Angular 6](https://www.freecodecamp.org/news/how-to-use-animation-with-angular-6-675b19bc3496/)