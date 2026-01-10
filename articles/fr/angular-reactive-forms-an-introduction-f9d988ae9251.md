---
title: Une introduction aux formulaires réactifs Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-04T11:40:11.000Z'
originalURL: https://freecodecamp.org/news/angular-reactive-forms-an-introduction-f9d988ae9251
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NwUCxqLzu4PfMDwsfA8Bvw.jpeg
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
seo_title: Une introduction aux formulaires réactifs Angular
seo_desc: 'By Gulfam Ansari

  Angular uses two different approaches to handle forms. The first one is the Template
  Driven Approach and the other one is the Reactive Approach. Both approaches use
  different techniques to handle your form data. In the Template Drive...'
---

Par Gulfam Ansari

Angular utilise deux approches différentes pour gérer les formulaires. La première est l'approche pilotée par les templates et l'autre est l'approche réactive. Les deux approches utilisent différentes techniques pour gérer les données de votre formulaire. Dans l'approche pilotée par les templates, nous définissons la structure du formulaire dans notre code HTML. En revanche, dans l'approche réactive, la structure du formulaire est définie dans la classe du composant.

L'approche réactive est plus complexe par rapport à l'approche pilotée par les templates, car elle peut offrir de nombreuses autres fonctionnalités. Dans cet article, nous allons créer un formulaire de contact en utilisant l'approche réactive Angular. Alors, qu'attendons-nous ? Plongeons-nous dedans.

### **Comment utiliser les formulaires réactifs dans Angular ?**

Pour implémenter les formulaires réactifs dans Angular, nous suivons les étapes ci-dessous.

1. Importer le module Reactive Form dans le fichier `app.module.ts`.
2. Créer une instance de la classe `FormGroup` dans le fichier du composant et initialiser les valeurs par défaut de tous les `FormControls`.
3. Lier le `FormGroup` et le `FormControl` dans le code HTML.

### 1. Importer le ReactiveFormsModule

Pour utiliser les formulaires réactifs dans votre application, vous devez importer `ReactiveFormsModule` dans votre fichier `module.ts` parent. C'est comme lorsque nous importons `FormsModule` dans notre fichier `app.module.ts` pour utiliser les formulaires pilotés par les templates.

```
import { AppComponent } from './app.component';
```

```
import { BrowserModule } from '@angular/platform-browser';
```

```
import { NgModule } from '@angular/core';
```

```
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
```

```
import { ReactiveFormsModule } from '@angular/forms';
```

```
@NgModule({
```

```
declarations: [AppComponent],
```

```
imports: [
```

```
  BrowserModule,
```

```
  BrowserAnimationsModule,
```

```
  ReactiveFormsModule
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

### 2. Définir FormGroup dans le composant

Comme nous le savons, dans l'approche des formulaires réactifs, la structure du formulaire est définie dans le fichier du composant, et cette structure est synchronisée avec le code HTML en utilisant la directive `formGroup`. Donc, pour créer notre formulaire de contact, nous devons d'abord définir notre modèle de formulaire dans la classe du composant.

**Form Control** est le plus petit bloc de construction d'un formulaire réactif qui suit toutes les valeurs d'entrée HTML et leurs validations.

**Form Group** est une collection de FormControls qui combine toutes les valeurs d'entrée HTML en un seul objet.

Il est maintenant temps de créer notre fichier de composant de formulaire de contact.

```
import { Component, OnInit } from '@angular/core';
```

```
import { FormGroup, FormControl } from '@angular/forms';
```

```
@Component({
```

```
  selector: 'app-contact',
```

```
  templateUrl: './contact.component.html',
```

```
  styleUrls: ['./contact.component.scss']
```

```
})
```

```
export class ContactFormComponent implements OnInit {
```

```
  public contactForm: FormGroup;
```

```
  constructor() { } 
```

```
  ngOnInit() {
```

```
    this.contactForm = new FormGroup({
```

```
      'name': new FormControl(null),
```

```
      'email': new FormControl(null),
```

```
      'subject': new FormControl(null),
```

```
      'message': new FormControl(null)
```

```
    });
```

```
  }
```

```
}
```

Dans le code ci-dessus, nous importons la classe FormGroup depuis `@angular/forms` et déclarons la propriété `FormGroup` nommée `contactform`.

Définissez tous les `FormControl` et regroupez-les en utilisant `FormGroup` et attribuez-les à `contactForm`.

### 3. Lier les FormControls dans le fichier HTML

Liez notre propriété FormGroup dans le Template en utilisant la directive `formGroup`.

Connectez tous les FormControls dans le Template en utilisant la directive `formControlName` pour mapper chaque élément d'entrée du HTML.

Nous utilisons également la directive `ngSubmit` pour poster les données du formulaire en cliquant sur le bouton de soumission.

```
<form [formGroup]="contactForm" (ngSubmit)="onSubmit()">
```

```
<input type="text" name="name" placeholder="Votre nom" formControlName="name">
```

```
<input type="text" name="email" placeholder="Votre email" formControlName="email">
```

```
<input type="text" name="subject" placeholder="Sujet" formControlName="subject">
```

```
<textarea name="message" placeholder="Votre message" formControlName="message"></textarea>
```

```
<button type="submit" class="btn btn-large">Envoyer le message</button>
```

```
</form>
```

### Validation

Vous avez implémenté la version de base d'un formulaire réactif. Maintenant, faites un pas en avant et validez vos valeurs d'entrée avant de les envoyer à la base de données.

En fait, nous faisons beaucoup de validation dans la couche backend avant d'envoyer les données à la base de données, mais pour rendre notre application plus rapide, nous introduisons également une validation côté client. Le module Angular ReactiveForm effectue cette validation de manière très efficace. Alors, validons nos entrées avant de les envoyer à la base de données.

Pour ajouter des validateurs dans votre formulaire, nous devons importer la classe `Validators` depuis `@angular/form` et ajouter des validateurs lors de la création d'un nouvel objet FormControl.

Le constructeur de la classe FormControl prend 3 arguments.

1. La valeur par défaut d'une entrée
2. Validateur ou tableau de validateurs
3. Validateurs asynchrones

Pour la validation du formulaire, nous utilisons le 2ème argument du constructeur de la classe FormControl.

```
this.contactForm = new FormGroup({
```

```
  'name': new FormControl(Enter Name, Validators.required),
```

```
  'email': new FormControl(null, [Validators.email, Validators.pattern('[a-z0-9.@]*')]),
```

```
  'subject': new FormControl(null, Validators.minLength(10)),
```

```
  'message': new FormControl(null, Validators.required)
```

```
});
```

Vous pouvez ajouter plus de validateurs en les ajoutant au tableau des validateurs.

### Validateurs personnalisés

La classe FormControl vous offre de nombreuses fonctions de validation intégrées qui couvrent de nombreux cas d'utilisation. Mais si vous souhaitez ajouter des vérifications personnalisées pour vos valeurs d'entrée, vous pouvez facilement le faire en utilisant vos propres fonctions de validation.

Vous pouvez passer des fonctions de validation personnalisées ainsi que des validateurs intégrés lors de la création de l'objet FormControl.

```
export class ContactFormComponent implements OnInit {
```

```
  public contactForm: FormGroup;  public forbiddenUserNames = ['Mack', 'John'];
```

```
  constructor() { }
```

```
  ngOnInit() {
```

```
    this.contactForm = new FormGroup({
```

```
      'name': new FormControl(Enter Name, [Validators.required, this.forbiddenNames.bind(this)]),
```

```
      'email': new FormControl(null, [Validators.email, Validators.pattern('[a-z0-9.@]*')]),
```

```
      'subject': new FormControl(null, Validators.minLength(10)),
```

```
      'message': new FormControl(null, Validators.required)
```

```
   });
```

```
 }
```

```
public forbiddenNames(formControl: FormControl): any {   if ( this.forbiddenUserNames.indexOf(formControl.value)){     return { 'nameForbidden': true };    }   }}
```

Dans le code ci-dessus, nous créons notre fonction de validation personnalisée qui vérifie si le nom de l'utilisateur est valide ou non. La fonction `forbiddenNames` prend un argument de type FormControl et vérifie si le nom saisi est présent dans le tableau `forbiddenUserNames`.

### Validateurs asynchrones

Comme le nom l'indique, la validation est effectuée de manière asynchrone. Lorsque le résultat des validateurs d'entrée prend un certain temps pour valider les valeurs d'entrée, nous utilisons des validateurs asynchrones.

Créons une fonction de validation qui répond après 1 seconde et retourne l'état de l'entrée, indiquant si l'entrée est valide ou non. Pour les validateurs asynchrones, nous devons retourner une promesse ou un observable au lieu de retourner un objet.

```
export class ContactFormComponent implements OnInit {
```

```
  public contactForm: FormGroup;  public forbiddenUserNames = ['Mack', 'John'];
```

```
  constructor() { }
```

```
  ngOnInit() {
```

```
    this.contactForm = new FormGroup({
```

```
      'name': new FormControl(Enter Name, [Validators.required, this.forbiddenNames.bind(this)]),
```

```
      'email': new FormControl(null, [Validators.email, Validators.pattern('[a-z0-9.@]*')], this.forbiddenEmail),
```

```
      'subject': new FormControl(null, Validators.minLength(10)),
```

```
      'message': new FormControl(null, Validators.required)
```

```
   });
```

```
}
```

```
public forbiddenNames(formControl: FormControl): any {   if ( this.forbiddenUserNames.indexOf(formControl.value)){       return { 'nameForbidden': true };    } else {      retunr null;    }
```

```
  }
```

```
public forbiddenEmail(formControl: FormControl): Promise<any> {   return new Promise((resolve, reject)=>{     setTimeout(()=>{       if (formControl.value === 'abc@gmail.com'){         resolve({ 'emailForbidden': true });       } else {        resolve(null);       }
```

```
     }, 1000);
```

```
   });  }}
```

Nous devons passer notre fonction de validation asynchrone nouvellement créée dans le troisième argument de l'objet `FormControl`. Nous pouvons passer un seul validateur asynchrone ou un tableau de validateurs asynchrones comme nous le faisons pour les validateurs normaux.

### FormArray

Jusqu'à présent, nous avons créé un `FormControl` pour chaque entrée. Mais que se passe-t-il si l'utilisateur a la possibilité d'ajouter ses propres FormControls ? `FormArray` est une classe importée depuis `@angular/core` qui est utilisée pour créer des FormControls dynamiques.

Mettons à jour notre formulaire de contact avec une entrée supplémentaire pour les hobbies, et cette entrée sera créée par l'utilisateur.

```
ngOnInit() {  this.contactForm = new FormGroup({
```

```
    'name': new FormControl(Enter Name, [Validators.required, this.forbiddenNames.bind(this)]),
```

```
    'email': new FormControl(null, [Validators.email, Validators.pattern('[a-z0-9.@]*')], this.forbiddenEmail),
```

```
    'subject': new FormControl(null, Validators.minLength(10)),
```

```
    'message': new FormControl(null, Validators.required),    'hobbies': new FormArray([])
```

```
  });}
```

```
public addHobby() {  (<FormArray>this.contactForm.get('hobbies')).push(new FormControl(null));}
```

Dans le code ci-dessus, la fonction `addHobby` sera exécutée chaque fois que l'utilisateur clique sur le bouton `Ajouter un hobby`. Cette fonction ajoutera un nouveau FormControl au FormArray. Maintenant, liez le FormArray des hobbies avec notre Template.

```
<div formArrayName="hobbies">  <button type="button">Ajouter un hobby</button>  <div *ngFor="let hobbyControl of this.contactForm.get('hobbies');  let i=index">    <input type="text" [formControlName"]="i">  </div></div>
```

Dans le code ci-dessus, nous utilisons la directive `formArrayName` pour lier le FormArray comme `formControlName` pour lier les FormControls.

J'espère que cet article a répondu à la plupart de vos questions concernant les formulaires réactifs Angular. Si vous avez des questions ou des doutes, n'hésitez pas à me contacter dans la boîte de commentaires.