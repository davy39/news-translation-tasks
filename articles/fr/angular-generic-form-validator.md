---
title: Comment créer un validateur de formulaire générique dans Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-03T17:22:23.000Z'
originalURL: https://freecodecamp.org/news/angular-generic-form-validator
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/461803-angular-JavaScript-HTML-1.jpg
tags:
- name: Angular
  slug: angular
- name: Form validations
  slug: form-validations
seo_title: Comment créer un validateur de formulaire générique dans Angular
seo_desc: "By Victor Onwuzor\nBuilding an Angular application that involves many forms\
  \ can be stressful. Especially so when you have to handle the validation messages\
  \ on each component. \nOne way to reduce your stress is to write a generic validation\
  \ class that h..."
---

Par Victor Onwuzor

Créer une application Angular qui implique de nombreux formulaires peut être stressant. Surtout lorsque vous devez gérer les messages de validation sur chaque composant. 

Une façon de réduire votre stress est d'écrire une classe de validation générique qui gère tous vos messages de validation.

D'une part, cela réduira considérablement le code sur votre modèle HTML. Cela vous donnera également une source unique de messages d'erreur avec la flexibilité de remplacer le message d'erreur sur chaque composant.

D'autre part, cela implique d'écrire un peu plus de code sur le composant et des fichiers supplémentaires.

Mais je pense que les avantages l'emportent sur les inconvénients lorsque vous traitez avec plusieurs formulaires dans différents composants.

### Prérequis

* Connaissance de base d'Angular
* Connaissance de base des formulaires réactifs

## Ce que nous construisons

Angular a deux types de formulaires : les formulaires pilotés par modèle et les formulaires réactifs. Dans cet article, nous nous concentrerons sur les formulaires réactifs.

Nous allons apprendre à valider un simple formulaire de connexion et d'inscription avec une validation générique en utilisant un formulaire réactif. J'ai utilisé le framework CSS Bulma pour le design. 

Les valeurs des entrées du formulaire sont simplement enregistrées dans la console lorsque vous cliquez sur soumettre. J'ai fait cela pour que nous puissions nous concentrer principalement sur la validation du formulaire, mais vous pouvez faire ce que vous voulez avec les valeurs des entrées du formulaire. 

Voici le lien de démonstration sur [Stackblitz](https://stackblitz.com/github/onwuvic/generic-reactive-form-validation).

## Étape 1 : Installation

J'ai créé un fichier de démarrage pour ce projet avec tout le HTML, CSS et Bulma déjà fait. Cela nous permet de nous concentrer davantage sur la validation générique des formulaires. Clonez ce dépôt sur [GitHub ici](https://github.com/onwuvic/generic-reactive-form-validation).

Ensuite, dans votre terminal, exécutez cette commande :

```
git clone git@github.com:onwuvic/generic-reactive-form-validation.git
```

Ou vous pouvez faire ceci :

```
git clone https://github.com/onwuvic/generic-reactive-form-validation.git
```

```
cd generic-reactive-form-validation
```

```
git checkout starter
```

```cmd
npm install
```

```
ng serve
```

Ensuite, visitez [http://localhost:4200/](http://localhost:4200/) dans votre navigateur.

Ouvrez le dossier generic-reactive-form-validation dans l'un de vos éditeurs. La structure des fichiers devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-02-at-09.22.45.png)
_structure des fichiers_

## Étape 2 : Importer ReactiveFormsModule

Maintenant, importons `ReactiveFormsModule` dans notre module d'application et ajoutons-le au tableau `imports`.

```typescript
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './modules/login/login.component';
import { SignUpComponent } from './modules/sign-up/sign-up.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignUpComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

## Étape 3 : Créer une classe de validation générique et un validateur de confirmation de mot de passe

### Classe de validation générique

Créons un dossier partagé à l'intérieur du dossier racine de l'application. Ensuite, à l'intérieur du dossier partagé, créez un fichier generic-validator.ts. Écrivez le code suivant :

```typescript
import { FormGroup } from '@angular/forms';

// Fournir tous les ensembles de messages de validation ici
const VALIDATION_MESSAGES = {
  email: {
    required: 'Requis',
    email: 'Cet email est invalide'
  },
  password: {
    required: 'Requis',
    minlength: 'La longueur du mot de passe doit être supérieure ou égale à 8'
  },
  confirmPassword: {
    required: 'Requis',
    match: 'Le mot de passe ne correspond pas'
  },
  firstName: {
    required: 'Requis'
  },
  lastName: {
    required: 'Requis'
  }
};

export class GenericValidator {
  // Par défaut, l'ensemble défini de messages de validation est transmis, mais un message personnalisé peut également être transmis lorsque la classe est appelée
  constructor(private validationMessages: { [key: string]: { [key: string]: string } } = VALIDATION_MESSAGES) {}

  // Cela traitera chaque formcontrol dans le groupe de formulaires
  // puis retournera le message d'erreur à afficher
  // la valeur de retour sera dans ce format `formControlName: 'message d'erreur'`;
  processMessages(container: FormGroup): { [key: string]: string } {
    const messages = {};
    // parcourir tous les formControls
    for (const controlKey in container.controls) {
      if (container.controls.hasOwnProperty(controlKey)) {
        // obtenir les propriétés de chaque formControl
        const controlProperty = container.controls[controlKey];
        // Si c'est un FormGroup, traiter ses contrôles enfants.
        if (controlProperty instanceof FormGroup) {
          const childMessages = this.processMessages(controlProperty);
          Object.assign(messages, childMessages);
        } else {
          // Valider uniquement s'il y a des messages de validation pour le contrôle
          if (this.validationMessages[controlKey]) {
            messages[controlKey] = '';
            if ((controlProperty.dirty || controlProperty.touched) && controlProperty.errors) {
              // parcourir l'objet des erreurs
              Object.keys(controlProperty.errors).map(messageKey => {
                if (this.validationMessages[controlKey][messageKey]) {
                  messages[controlKey] += this.validationMessages[controlKey][messageKey] + ' ';
                }
              });
            }
          }
        }
      }
    }
    return messages;
  }
}
```

Tout d'abord, nous importons `FormGroup`. Nous pouvons écrire tous nos messages de validation dans ce fichier ou transmettre chaque message de validation de formulaire depuis leurs composants. 

Chaque propriété de l'objet `VALIDATION_MESSAGES` correspond à chaque nom de champ de saisie ou `formControlName`. De plus, chaque propriété du champ de saisie correspond au nom de validation sur celui-ci. Sa valeur est ce que vous voulez afficher comme message d'erreur. 

Par exemple, le nom du champ de saisie `formControlName` "email" a des validations de "required" et "email" sur celui-ci.

Dans la méthode du constructeur, nous pouvons remplacer les messages d'erreur par défaut depuis le composant où notre validation générique est utilisée en transmettant le message de validation lorsque nous instancions notre classe de validation générique.

La méthode processMessages traite chaque champ de saisie du formulaire et retourne le message d'erreur à afficher.

### Validation de confirmation de mot de passe

Maintenant, créons un validateur de confirmation de mot de passe pour vérifier si notre mot de passe et la confirmation du mot de passe correspondent.

À l'intérieur du dossier partagé, créez un fichier `password-matcher.ts`. Écrivez le code suivant :

```typescript
import { AbstractControl } from '@angular/forms';

export class PasswordMatcher {
  static match(control: AbstractControl): void | null {
    const passwordControl = control.get('password');
    const confirmPasswordControl = control.get('confirmPassword');

    if (passwordControl.pristine || confirmPasswordControl.pristine) {
      return null;
    }

    if (passwordControl.value === confirmPasswordControl.value) {
      return null;
    }

    confirmPasswordControl.setErrors({ match: true });
  }
}
```

## Étape 4 : Ajouter FormGroup et FormBuilder à chaque composant et modèle

### Composant de formulaire d'inscription

À l'intérieur de app/modules/sign-up, ajoutez le code suivant au composant d'inscription :

```typescript
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

import { PasswordMatcher } from '../../shared/password-matcher';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.scss']
})
export class SignUpComponent implements OnInit {
  signupForm: FormGroup;

  // Utiliser avec la classe de message de validation générique
  displayMessage: { [key: string]: string } = {};

  constructor(private fb: FormBuilder) {}

  ngOnInit() {
    this.signupForm = this.fb.group({
      firstName: ['', [Validators.required]],
      lastName: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]],
      confirmPassword: ['', Validators.required]
    }, { validator: PasswordMatcher.match });
  }

  signup() {
    console.log('---form', this.signupForm.value);
  }

}
```

Nous avons des validations intégrées d'Angular pour chaque champ de saisie ainsi que notre validation personnalisée `PasswordMatcher` pour garantir que le mot de passe et le mot de passe confirmé correspondent.

### Modèle de formulaire d'inscription

Maintenant, examinons le modèle de formulaire d'inscription :

```html
<h1 class="title is-4">Inscription</h1>
<p class="description">Commençons !</p>
<form (ngSubmit)="signup()" [formGroup]="signupForm" novalidate autocomplete="false">
  <div class="field">
    <div class="control">
      <input [ngClass]="{'is-danger': displayMessage.firstName}" formControlName="firstName" class="input is-medium" type="text" placeholder="Prénom">
      <p *ngIf="displayMessage.firstName" class="help is-danger">
        {{ displayMessage.firstName }}
      </p>
    </div>
  </div>
  <div class="field">
    <div class="control">
      <input [ngClass]="{'is-danger': displayMessage.lastName}" formControlName="lastName" class="input is-medium" type="text" placeholder="Nom">
      <p *ngIf="displayMessage.lastName" class="help is-danger">
        {{ displayMessage.lastName }}
      </p>
    </div>
  </div>
  <div class="field">
    <div class="control">
      <input [ngClass]="{'is-danger': displayMessage.email}" formControlName="email" class="input is-medium" type="email" placeholder="Email">
      <p *ngIf="displayMessage.email" class="help is-danger">
        {{ displayMessage.email }}
      </p>
    </div>
  </div>
  <div class="field">
    <div class="control">
      <input [ngClass]="{'is-danger': displayMessage.password || displayMessage.confirmPassword }" formControlName="password" class="input is-medium" type="password" placeholder="Mot de passe">
      <p *ngIf="displayMessage.password" class="help is-danger">
        {{ displayMessage.password }}
      </p>
    </div>
  </div>
  <div class="field">
    <div class="control">
      <input [ngClass]="{'is-danger': displayMessage.confirmPassword}" formControlName="confirmPassword" class="input is-medium" type="password" placeholder="Confirmer le mot de passe">
      <p *ngIf="displayMessage.confirmPassword" class="help is-danger">
        {{ displayMessage.confirmPassword }}
      </p>
    </div>
  </div>
  <br>
  <button type="submit" class="button is-block is-primary is-fullwidth is-medium" [disabled]="signupForm.invalid">Soumettre</button>
  <br>
  <small class="has-text-centered">
    <em>
      Vous avez déjà un compte
      <a [routerLink]="['']" class="primary-color">Connexion</a>
    </em>
  </small>

</form>
```

```html
<form (ngSubmit)="signup()" [formGroup]="signupForm" novalidate autocomplete="false">
```

Nous avons ajouté notre `ngSubmit` et `formGroup` à la balise form.

```html
<input [ngClass]="{'is-danger': displayMessage.firstName}" formControlName="firstName" class="input is-medium" type="text" placeholder="Prénom">
```

Nous avons également ajouté `formControlName` à chaque champ de saisie. Si le message d'affichage contient un message d'erreur firstName, il appliquera la classe ngClass is-danger au champ de saisie.

```html
<p *ngIf="displayMessage.firstName" class="help is-danger">
  {{ displayMessage.firstName }}
</p>
```

Cela affiche notre message d'erreur.

```html
<button type="submit" class="button is-block is-primary is-fullwidth is-medium" [disabled]="signupForm.invalid">Soumettre</button>
```

Nous désactivons le bouton de soumission si le formulaire n'est pas valide.

### Composant de formulaire de connexion

À l'intérieur de app/modules/login, ajoutez le code suivant au composant de connexion :

```typescript

import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit, AfterViewInit {
  loginForm: FormGroup;

  // Utiliser avec la classe de message de validation générique
  displayMessage: { [key: string]: string } = {};
  private validationMessages: { [key: string]: { [key: string]: string } };

  constructor(private fb: FormBuilder) {
    // Définit tous les messages de validation pour le formulaire.
    this.validationMessages = {
      email: {
        required: 'Requis',
        email: 'Cet email est invalide'
      },
      password: {
        required: 'Requis',
        minlength: 'La longueur du mot de passe doit être supérieure ou égale à 8'
      }
    };
  }

  ngOnInit() {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]],
    });
  }

  login() {
    console.log('---form', this.loginForm.value);
  }

}
```

La seule différence ici avec le composant d'inscription est que nous allons remplacer le message d'erreur par défaut dans notre classe de validation générique par le message de validation.

### Modèle de formulaire de connexion

Écrivez le code suivant dans le modèle de connexion :

```html
<h1 class="title is-4">Connexion</h1>
<p class="description">Bienvenue !</p>
<form (ngSubmit)="login()" [formGroup]="loginForm" novalidate autocomplete="false">
  <div class="field">
    <div class="control">
      <input [ngClass]="{'is-danger': displayMessage.email}" class="input is-medium" type="email" placeholder="Email" formControlName="email">
      <p *ngIf="displayMessage.email" class="help is-danger">
        {{ displayMessage.email }}
      </p>
    </div>
  </div>
  <div class="field">
    <div class="control">
      <input [ngClass]="{'is-danger': displayMessage.password}" class="input is-medium" type="password" placeholder="Mot de passe" formControlName="password">
      <p *ngIf="displayMessage.password" class="help is-danger">
        {{ displayMessage.password }}
      </p>
    </div>
  </div>
  <button type="submit" class="button is-block is-primary is-fullwidth is-medium" [disabled]="loginForm.invalid">Connexion</button>
  <br>
  <small class="has-text-centered">
    <em>
      Vous n'avez pas de compte
      <a [routerLink]="['signup']" class="primary-color">Inscription</a>
    </em>
  </small>
</form>
```

## Étape 5 : Utiliser la validation générique dans chaque composant

### Validation générique sur l'inscription

Ajoutez le code suivant au fichier `sign-up.component.ts` :

```typescript
import { Component, OnInit, ViewChildren, ElementRef, AfterViewInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators, FormControlName, AbstractControl } from '@angular/forms';
import { Observable, fromEvent, merge } from 'rxjs';
import { debounceTime } from 'rxjs/operators';
import { GenericValidator } from '../../shared/generic-validator';
import { PasswordMatcher } from '../../shared/password-matcher';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.scss']
})
export class SignUpComponent implements OnInit, AfterViewInit {
  // Accéder à tous les champs de saisie du formulaire dans notre fichier HTML d'inscription
  @ViewChildren(FormControlName, { read: ElementRef }) formInputElements: ElementRef[];
  signupForm: FormGroup;

  // Utiliser avec la classe de message de validation générique
  displayMessage: { [key: string]: string } = {};
  private genericValidator: GenericValidator;

  constructor(private fb: FormBuilder) {
    // Définir une instance du validateur pour une utilisation avec ce formulaire,
    this.genericValidator = new GenericValidator();
  }

  ngOnInit() {
    this.signupForm = this.fb.group({
      firstName: ['', [Validators.required]],
      lastName: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]],
      confirmPassword: ['', Validators.required]
    }, { validator: PasswordMatcher.match });
  }

  ngAfterViewInit(): void {
    // Surveiller l'événement de perte de focus de n'importe quel élément de saisie du formulaire.
    const controlBlurs: Observable<any>[] = this.formInputElements
      .map((formControl: ElementRef) => fromEvent(formControl.nativeElement, 'blur'));

    // Fusionner l'observable de l'événement de perte de focus avec l'observable des changements de valeur
    merge(this.signupForm.valueChanges, ...controlBlurs).pipe(
      debounceTime(800)
    ).subscribe(value => {
      this.displayMessage = this.genericValidator.processMessages(this.signupForm);
    });
  }

  signup() {
    console.log('---form', this.signupForm.value);
  }

}
```

Ici, nous avons importé la classe de validation générique.

```
@ViewChildren(FormControlName, { read: ElementRef }) formInputElements: ElementRef[];
```

Nous avons ajouté `@ViewChildren` pour accéder à chaque champ de saisie du formulaire dans notre fichier HTML d'inscription. Cela nous aide à écouter un événement sur eux.

```
private genericValidator: GenericValidator;

constructor(private fb: FormBuilder) {
   // Définir une instance du validateur pour une utilisation avec ce formulaire
   this.genericValidator = new GenericValidator();
}
```

Nous instancions la validation générique à l'intérieur du constructeur.

Ensuite, nous implémentons l'interface ngAfterViewInit.

```
ngAfterViewInit(): void {
   // Surveiller l'événement de perte de focus de n'importe quel 
   // élément de saisie du formulaire.
   const controlBlurs: Observable<any>[] = this.formInputElements
      .map((formControl: ElementRef) =>
         fromEvent(formControl.nativeElement, 'blur')
      );
   // Fusionner l'observable de l'événement de perte de focus 
   // avec l'observable des changements de valeur
   merge(this.signupForm.valueChanges, ...controlBlurs)
    .pipe(debounceTime(800))
    .subscribe(value => {
      this.displayMessage = this.genericValidator
        .processMessages(this.signupForm);
   });
}
```

Ici, nous surveillons l'événement de perte de focus de n'importe quel élément de saisie du formulaire. 

```typescript
const controlBlurs: Observable<any>[] = this.formInputElements
      .map((formControl: ElementRef) =>
         fromEvent(formControl.nativeElement, 'blur')
      );
```

```typescript
merge(this.signupForm.valueChanges, ...controlBlurs)
    .pipe(debounceTime(800))
    .subscribe(value => {
      this.displayMessage = this.genericValidator
        .processMessages(this.signupForm);
   });
```

Maintenant, nous avons combiné l'observable des changements de valeur du formulaire (qui est déclenché lorsque l'une des valeurs de saisie change) et les événements de perte de focus de n'importe quel champ de saisie en un seul observable. 

Ainsi, lorsqu'un utilisateur modifie une valeur de saisie ou appuie sur n'importe quel champ de saisie, cette méthode de fusion est déclenchée. 

Ensuite, nous ajoutons un délai de 800 millisecondes avec `debounceTime(800)`. Cela donne à l'utilisateur le temps de faire des modifications avant de déclencher la validation. 

Enfin, nous obtenons les messages d'erreur à afficher en appelant la méthode du validateur générique.

### Validation générique sur la connexion

Écrivez le code suivant dans le fichier `login.component.ts` :

```typescript
import { Component, OnInit, ViewChildren, ElementRef, AfterViewInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators, FormControlName } from '@angular/forms';
import { Observable, fromEvent, merge } from 'rxjs';
import { debounceTime } from 'rxjs/operators';
import { GenericValidator } from '../../shared/generic-validator';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit, AfterViewInit {
  // Accéder à tous les champs de saisie du formulaire dans notre fichier HTML de connexion
  @ViewChildren(FormControlName, { read: ElementRef }) formInputElements: ElementRef[];
  loginForm: FormGroup;

  // Utiliser avec la classe de message de validation générique
  displayMessage: { [key: string]: string } = {};
  private validationMessages: { [key: string]: { [key: string]: string } };
  private genericValidator: GenericValidator;

  constructor(private fb: FormBuilder) {
    // Définit tous les messages de validation pour le formulaire.
    this.validationMessages = {
      email: {
        required: 'Requis',
        email: 'Cet email est invalide'
      },
      password: {
        required: 'Requis',
        minlength: 'La longueur du mot de passe doit être supérieure ou égale à 8'
      }
    };
    // Définir une instance du validateur pour une utilisation avec ce formulaire,
    // en passant l'ensemble des messages de validation de ce formulaire.
    this.genericValidator = new GenericValidator(this.validationMessages);
  }

  ngOnInit() {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]],
    });
  }

  ngAfterViewInit(): void {
    // Surveiller l'événement de perte de focus de n'importe quel élément de saisie du formulaire.
    const controlBlurs: Observable<any>[] = this.formInputElements
      .map((formControl: ElementRef) => fromEvent(formControl.nativeElement, 'blur'));

    // Fusionner l'observable de l'événement de perte de focus avec l'observable des changements de valeur
    merge(this.loginForm.valueChanges, ...controlBlurs).pipe(
      debounceTime(800)
    ).subscribe(value => {
      this.displayMessage = this.genericValidator.processMessages(this.loginForm);
    });
  }

  login() {
    console.log('---form', this.loginForm.value);
  }

}
```

La seule différence ici par rapport au code d'inscription est que nous remplaçons nos messages de validation par défaut par nos nouveaux messages de validation spécifiés dans ce composant. Ensuite, nous les transmettons à la classe de validation générique lorsque nous l'instancions.

```
  constructor(private fb: FormBuilder) {
    // Définit tous les messages de validation pour le formulaire.
    this.validationMessages = {
      email: {
        required: 'Requis',
        email: 'Cet email est invalide'
      },
      password: {
        required: 'Requis',
        minlength: 'La longueur du mot de passe doit être supérieure ou égale à 8'
      }
    };
    // Définir une instance du validateur pour une utilisation avec ce formulaire,
    // en passant l'ensemble des messages de validation de ce formulaire.
    this.genericValidator = new GenericValidator(this.validationMessages);
  }
```

Nous pouvons nous attendre à ce que cela fonctionne de la même manière que la validation générique d'inscription.

Et c'est tout ce dont vous avez besoin pour créer un validateur générique dans Angular.

## Conclusion

Créer un validateur générique facilite la gestion de plusieurs validations de formulaires sans utiliser une tonne de code redondant dans votre application Angular. 

J'espère que cet article vous a été utile !

Vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/victoronwuzor/) et [Twitter](https://twitter.com/victoronwuzor).