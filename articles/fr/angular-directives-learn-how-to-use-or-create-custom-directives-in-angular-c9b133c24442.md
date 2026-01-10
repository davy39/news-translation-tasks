---
title: Comment utiliser et créer des directives personnalisées dans Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-30T12:28:26.000Z'
originalURL: https://freecodecamp.org/news/angular-directives-learn-how-to-use-or-create-custom-directives-in-angular-c9b133c24442
coverImage: https://cdn-media-1.freecodecamp.org/images/1*A4-tgMN9OZ6gIoRVFDJj_g.jpeg
tags:
- name: Angular
  slug: angular
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment utiliser et créer des directives personnalisées dans Angular
seo_desc: 'By Gulfam Ansari

  After playing with Angular for a long time, I finally came up with an understandable
  explanation of Angular directives. In this article, we will first understand what
  a directive exactly is and how to use it in Angular. We will creat...'
---

Par Gulfam Ansari

Après avoir travaillé avec Angular pendant longtemps, j'ai enfin trouvé une explication compréhensible des directives Angular. Dans cet article, nous allons d'abord comprendre ce qu'est exactement une directive et comment l'utiliser dans Angular. Nous créerons également nos propres directives personnalisées. Alors, qu'attendons-nous ? Plongeons-nous dans le sujet.

### Qu'est-ce qu'une directive Angular ?

Les directives sont des fonctions qui s'exécutent chaque fois que le compilateur Angular les trouve. Les directives Angular améliorent les capacités des éléments HTML en attachant des comportements personnalisés au DOM.

Conceptuellement, les directives Angular sont catégorisées en trois catégories.

1. **Directives d'attribut**
2. **Directives structurelles**
3. **Composants**

#### Directives d'attribut

Les directives d'attribut sont responsables de la manipulation de l'apparence et du comportement des éléments du DOM. Nous pouvons utiliser des directives d'attribut pour changer le style des éléments du DOM. Ces directives sont également utilisées pour masquer ou afficher des éléments DOM particuliers de manière conditionnelle. Angular fournit de nombreuses directives d'attribut intégrées comme **NgStyle**, **NgClass**, etc. Nous pouvons également créer nos propres directives d'attribut personnalisées pour la fonctionnalité souhaitée.

#### **Directives structurelles**

Les directives structurelles sont responsables de la modification de la structure du DOM. Elles fonctionnent en ajoutant ou en supprimant des éléments du DOM, contrairement aux directives d'attribut qui ne changent que l'apparence et le comportement de l'élément.

Vous pouvez facilement différencier une directive structurelle d'une directive d'attribut en regardant la syntaxe. Le nom de la directive structurelle commence toujours par un préfixe astérisque (*), tandis que la directive d'attribut ne contient aucun préfixe. Les trois directives structurelles intégrées les plus populaires qu'Angular fournit sont **NgIf**, **NgFor** et **NgSwitch**.

#### **Composants**

Les composants sont des directives avec des templates. La seule différence entre les composants et les deux autres types de directives est le template. Les directives d'attribut et structurelles n'ont pas de templates. Ainsi, nous pouvons dire que le composant est une version plus propre de la directive avec un template, ce qui est plus facile à utiliser.

### **Utilisation des directives intégrées d'Angular**

Il existe de nombreuses directives intégrées disponibles dans Angular que vous pouvez facilement utiliser. Dans cette section, nous allons utiliser deux directives intégrées très simples.

La directive **NgStyle** est une directive d'attribut utilisée pour changer le style de n'importe quel élément DOM en fonction de certaines conditions.

```
<p [ngStyle]="{'background': isBlue ? 'blue' : 'red'}"> Je suis une directive d'attribut</p>
```

> Dans l'extrait de code ci-dessus, nous ajoutons un fond bleu si la valeur de la variable `isBlue` est vraie. Si la valeur de la variable `isBlue` est fausse, alors le fond de l'élément ci-dessus sera rouge.

La directive **NgIf** est une directive structurelle utilisée pour ajouter des éléments dans le DOM selon certaines conditions.

```
<p *ngIf="show">Je suis une directive structurelle</p>
```

> Dans l'extrait de code ci-dessus, le paragraphe entier restera dans le DOM si la valeur de la variable `show` est vraie, sinon il sera supprimé du DOM.

### **Création d'une directive d'attribut personnalisée**

Créer une directive personnalisée est similaire à la création d'un composant Angular. Pour créer une directive personnalisée, nous devons remplacer le décorateur `@Component` par le décorateur `@Directive`.

Alors, commençons par créer notre première directive d'attribut personnalisée. Dans cette directive, nous allons mettre en surbrillance l'élément DOM sélectionné en définissant la couleur de fond de l'élément.

Créez un fichier `app-highlight.directive.ts` dans le dossier `src/app` et ajoutez l'extrait de code ci-dessous.

```
import { Directive, ElementRef } from '@angular/core';
```

```
@Directive({
```

```
    selector: '[appHighlight]'
```

```
})
```

```
export class HighlightDirective {
```

```
    constructor(private eleRef: ElementRef) {
```

```
        eleRef.nativeElement.style.background = 'red';
```

```
    }
```

```
}
```

Ici, nous importons `Directive` et `ElementRef` depuis le cœur d'Angular. `Directive` fournit la fonctionnalité du décorateur `@Directive` dans lequel nous fournissons sa propriété de sélecteur à `appHighLight` afin que nous puissions utiliser ce sélecteur n'importe où dans l'application. Nous importons également `ElementRef` qui est responsable de l'accès à l'élément DOM.

Maintenant, pour que la directive `appHighlight` fonctionne, nous devons ajouter notre directive au tableau des déclarations dans le fichier `app.module.ts`.

```
import ...;
```

```
import { ChangeThemeDirective } from './app-highlight.directive';
```

```
@NgModule({
```

```
declarations: [
```

```
AppComponent,
```

```
ChangeThemeDirective
```

```
],
```

```
imports: [
```

```
...
```

```
],
```

```
providers: [],
```

```
bootstrap: [AppComponent]
```

```
})
```

```
export class AppModule { }
```

Maintenant, nous allons utiliser notre nouvelle directive personnalisée. J'ajoute la directive `appHightlight` dans le fichier `app.component.html`, mais vous pouvez l'utiliser n'importe où dans l'application.

```
<h1 appHightlight>Mettez-moi en surbrillance !</h1>
```

Le résultat de l'extrait de code ci-dessus ressemblera à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/2gCU64J6c149TzNBHuP-QROInU7IA09OyDwA)

### Création d'une directive structurelle personnalisée

Dans la section précédente, nous avons créé notre première directive d'attribut. La même approche est utilisée pour créer la directive structurelle également.

Alors, commençons par créer notre directive structurelle. Dans cette directive, nous allons implémenter la directive `*appNot` qui fonctionnera à l'opposé de `*ngIf`.

Maintenant, créez un fichier `app-not.directive.ts` dans le dossier `src/app` et ajoutez le code ci-dessous.

```
import { Directive, Input, TemplateRef, ViewContainerRef } from '@angular/core';
```

```
@Directive({
```

```
    selector: '[appNot]'
```

```
})
```

```
export class AppNotDirective {
```

```
constructor(
```

```
    private templateRef: TemplateRef<any>,
```

```
    private viewContainer: ViewContainerRef) { }
```

```
    @Input() set appNot(condition: boolean) {
```

```
        if (!condition) {
```

```
            this.viewContainer.createEmbeddedView(this.templateRef);
```

```
        } else {
```

```
            this.viewContainer.clear();        }
```

```
    }
```

```
}
```

Comme vous l'avez vu dans l'extrait de code ci-dessus, nous importons `Directive, Input, TemplateRef et ViewContainerRef` depuis `@angular/core`.

`Directive` fournit la même fonctionnalité pour le décorateur `@Directive`. Le décorateur `Input` est utilisé pour communiquer entre les deux composants. Il envoie des données d'un composant à l'autre en utilisant la liaison de propriétés.

`TemplateRef` représente le template intégré qui est utilisé pour instancier les vues intégrées. Ces vues intégrées sont liées au template qui doit être rendu.

`ViewContainerRef` est un conteneur où une ou plusieurs vues peuvent être attachées. Nous pouvons utiliser la fonction `createEmbeddedView()` pour attacher les templates intégrés dans le conteneur.

Maintenant, pour que la directive `appNot` fonctionne, nous devons ajouter notre directive au tableau des déclarations dans le fichier `app.module.ts`.

```
import ...;
```

```
import { AppNotDirective } from './app-not.directive';
```

```
@NgModule({
```

```
declarations: [
```

```
AppComponent,
```

```
AppNotDirective
```

```
],
```

```
imports: [
```

```
...
```

```
],
```

```
providers: [],
```

```
bootstrap: [AppComponent]
```

```
})
```

```
export class AppModule { }
```

Maintenant, il est temps d'utiliser notre nouvelle directive structurelle.

J'ajoute la directive `appNot` dans le fichier `app.component.html`, mais vous pouvez l'utiliser n'importe où dans l'application.

```
<h1 *appNot="true">Vrai</h1><h1 *appNot="false">Faux</h1>
```

La directive `*appNot` est conçue de manière à ce qu'elle ajoute l'élément de template dans le DOM si la valeur de `*appNot` est `false`, à l'opposé de la directive `*ngIf`.

Le résultat de l'extrait de code ci-dessus ressemblera à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/Gq-nb90cSoMpnte266GnWRQb3RuUqVESuRAe)

J'espère que cet article a répondu à la plupart de vos questions concernant les directives Angular. Si vous avez des questions ou des doutes, n'hésitez pas à me contacter dans la boîte de commentaires.