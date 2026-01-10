---
title: Comment valider les formulaires pilotés par template dans Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-22T08:18:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-validate-angular-template-driven-forms
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e88740569d1a4ca3da3.jpg
tags:
- name: Angular
  slug: angular
- name: Form validations
  slug: form-validations
- name: template-driven-forms
  slug: template-driven-forms
- name: TypeScript
  slug: typescript
seo_title: Comment valider les formulaires pilotés par template dans Angular
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will learn about validations in Angular template-driven forms.
  We will create a simple user registration form and implement some inbuilt validations
  on it. Along with the inbuilt validations, we will a...'
---

Par Ankit Sharma

## **Introduction**

Dans cet article, nous allons apprendre à valider les formulaires pilotés par template dans Angular. Nous allons créer un simple formulaire d'inscription utilisateur et implémenter quelques validations intégrées. En plus des validations intégrées, nous allons également implémenter quelques validations personnalisées pour le formulaire piloté par template.

Nous allons considérer les validations personnalisées suivantes pour cette démonstration :

* Vérification de la disponibilité du nom d'utilisateur
* Validation du motif du mot de passe
* Correspondance du mot de passe saisi dans deux champs différents

Regardez l'application en action.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/TemplateFormValidation.gif)

## **Prérequis**

* Installer Visual Studio Code depuis [ici](https://code.visualstudio.com/)
* Installer la dernière version d'Angular CLI depuis [ici](https://cli.angular.io/)
* Installer la dernière version LTS de Node.js depuis [ici](https://nodejs.org/en/)

## **Code source**

Vous pouvez obtenir le code source depuis [GitHub](https://github.com/AnkitSharma-007/angular-forms-validation).

## **Créer l'application Angular**

Naviguez vers le dossier où vous souhaitez créer votre fichier de projet. Ouvrez une fenêtre de commande et exécutez la commande suivante :

```
ng new angular-forms-validation --routing=false --style=scss
```

Nous spécifions la commande pour créer une nouvelle application Angular. L'option de création du module de routage est définie sur false et l'extension des fichiers de style est définie sur SCSS. Cette commande créera le projet Angular avec le nom angular-forms-validation.

Changez de répertoire vers le nouveau projet et ouvrez le projet dans VS Code en utilisant la série de commandes ci-dessous :

```
cd angular-forms-validation
code .
```

## Installer Bootstrap

Exécutez la commande suivante pour installer Bootstrap :

```
npm install bootstrap --save
```

Ajoutez la définition d'importation suivante dans le fichier `styles.scss` :

```
@import "~bootstrap/dist/css/bootstrap.css";
```

## Créer le service de validation

Exécutez la commande suivante pour créer un nouveau service :

```
ng g s services\customvalidation
```

Cette commande créera un dossier nommé services qui contient deux fichiers à l'intérieur - `customvalidation.service.ts` et `customvalidation.service.spec.ts`. Ouvrez `customvalidation.service.ts` et mettez le code suivant à l'intérieur :

```
import { Injectable } from '@angular/core';
import { ValidatorFn, AbstractControl } from '@angular/forms';
import { FormGroup } from '@angular/forms';

@Injectable({
  providedIn: 'root'
})
export class CustomvalidationService {

  patternValidator(): ValidatorFn {
    return (control: AbstractControl): { [key: string]: any } => {
      if (!control.value) {
        return null;
      }
      const regex = new RegExp('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$');
      const valid = regex.test(control.value);
      return valid ? null : { invalidPassword: true };
    };
  }

  MatchPassword(password: string, confirmPassword: string) {
    return (formGroup: FormGroup) => {
      const passwordControl = formGroup.controls[password];
      const confirmPasswordControl = formGroup.controls[confirmPassword];

      if (!passwordControl || !confirmPasswordControl) {
        return null;
      }

      if (confirmPasswordControl.errors && !confirmPasswordControl.errors.passwordMismatch) {
        return null;
      }

      if (passwordControl.value !== confirmPasswordControl.value) {
        confirmPasswordControl.setErrors({ passwordMismatch: true });
      } else {
        confirmPasswordControl.setErrors(null);
      }
    }
  }

  userNameValidator(userControl: AbstractControl) {
    return new Promise(resolve => {
      setTimeout(() => {
        if (this.validateUserName(userControl.value)) {
          resolve({ userNameNotAvailable: true });
        } else {
          resolve(null);
        }
      }, 1000);
    });
  }

  validateUserName(userName: string) {
    const UserList = ['ankit', 'admin', 'user', 'superuser'];
    return (UserList.indexOf(userName) > -1);
  }
}
```

La méthode `patternValidator` est utilisée pour valider le motif du mot de passe dans notre formulaire. Le paramètre de cette méthode est de type `AbstractControl` qui est une classe de base pour `FormControl`.

Nous allons utiliser une expression régulière pour valider le mot de passe. Cette expression régulière vérifiera les quatre conditions suivantes dans le mot de passe :

* Le mot de passe doit comporter au moins huit caractères
* Il doit contenir au moins une lettre minuscule
* Il doit contenir au moins une lettre majuscule
* Il doit contenir au moins un chiffre

Si le mot de passe ne passe pas la vérification regex, nous définirons la propriété `invalidPassword` sur true.

La méthode `MatchPassword` est utilisée pour comparer les mots de passe dans deux champs. Cette méthode acceptera deux paramètres de type string. Ces paramètres représentent le nom des champs à faire correspondre. Nous obtiendrons le `FormControl` pour ces deux champs puis nous ferons correspondre les valeurs qu'ils contiennent. Si les valeurs ne correspondent pas, nous définirons la propriété `passwordMismatch` sur true.

La méthode `userNameValidator` est utilisée pour vérifier si le nom d'utilisateur est déjà pris ou non. Cette méthode acceptera un paramètre de type `AbstractControl`.

Nous vérifierons si la valeur de ce champ est présente dans un tableau statique, UserList. Si la valeur saisie par l'utilisateur est déjà présente, nous définirons la propriété `userNameNotAvailable` sur true.

Nous utilisons la fonction setTimeout pour invoquer cette vérification toutes les deux secondes. Cela garantira que l'erreur sera lancée deux secondes après que l'utilisateur ait arrêté de taper dans le champ.

Pour la simplicité de cet article, nous utilisons un tableau statique pour rechercher la disponibilité des noms d'utilisateur. Idéalement, cela devrait être un appel de service au serveur pour rechercher la valeur dans une base de données.

## Créer le modèle utilisateur

Créez un nouveau dossier appelé models à l'intérieur du dossier `src/app`. Ajoutez un nouveau fichier appelé `user.ts` à l'intérieur du dossier models. Mettez le code suivant dans le fichier `user.ts`.

```
export class User {
    public name: string;
    public email: string;
    public username: string;
    public password: string;
    public confirmPassword: string;
}
```

## Créer des directives personnalisées

Nous allons créer des directives personnalisées pour implémenter des validateurs personnalisés pour les formulaires pilotés par template.

Exécutez la commande suivante pour créer la directive `passwordPattern` :

```
ng g d directives\passwordPattern
```

Cette commande créera un dossier nommé directives qui contient deux fichiers à l'intérieur - `passwordPattern.directive.ts` et `passwordPattern.directive.spec.ts`. Ouvrez `passwordPattern.directive.ts` et mettez le code suivant à l'intérieur.

```
import { Directive } from '@angular/core';
import { NG_VALIDATORS, Validator, AbstractControl } from '@angular/forms';
import { CustomvalidationService } from '../services/customvalidation.service';

@Directive({
  selector: '[appPasswordPattern]',
  providers: [{ provide: NG_VALIDATORS, useExisting: PasswordPatternDirective, multi: true }]
})
export class PasswordPatternDirective implements Validator {

  constructor(private customValidator: CustomvalidationService) { }

  validate(control: AbstractControl): { [key: string]: any } | null {
    return this.customValidator.patternValidator()(control);
  }
}
```

Cette directive est utilisée pour valider le motif du mot de passe. Nous allons implémenter l'interface Validator sur la classe `PasswordPatternDirective`. Nous allons remplacer la méthode validate qui accepte un paramètre de type `AbstractControl`, qui est le contrôle que nous voulons valider. Nous allons ensuite invoquer la méthode `patternValidator` du service.

Exécutez la commande suivante pour créer la directive `matchPassword` :

```
ng g d directives\matchPassword
```

Ouvrez `matchPassword.directive.ts` et mettez le code suivant à l'intérieur :

```
import { Directive, Input } from '@angular/core';
import { NG_VALIDATORS, Validator, ValidationErrors, FormGroup } from '@angular/forms';
import { CustomvalidationService } from '../services/customvalidation.service';

@Directive({
  selector: '[appMatchPassword]',
  providers: [{ provide: NG_VALIDATORS, useExisting: MatchPasswordDirective, multi: true }]
})
export class MatchPasswordDirective implements Validator {
  @Input('appMatchPassword') MatchPassword: string[] = [];

  constructor(private customValidator: CustomvalidationService) { }

  validate(formGroup: FormGroup): ValidationErrors {
    return this.customValidator.MatchPassword(this.MatchPassword[0], this.MatchPassword[1])(formGroup);
  }
}
```

Cette directive est utilisée pour valider si les mots de passe saisis dans deux champs correspondent ou non. Cette directive acceptera une entrée de type tableau de chaînes, qui contient les champs à faire correspondre. Nous allons remplacer la méthode validate et passer le paramètre de type `FormGroup`. Nous allons ensuite invoquer la méthode `MatchPassword` du service.

Exécutez la commande suivante pour créer la directive `validateUserName` :

```
ng g d directives\validateUserName
```

Ouvrez `validateUserName.directive.ts` et mettez le code suivant à l'intérieur :

```
import { Directive, forwardRef } from '@angular/core';
import { Validator, AbstractControl, NG_ASYNC_VALIDATORS } from '@angular/forms';
import { CustomvalidationService } from '../services/customvalidation.service';
import { Observable } from 'rxjs';

@Directive({
  selector: '[appValidateUserName]',
  providers: [{ provide: NG_ASYNC_VALIDATORS, useExisting: forwardRef(() => ValidateUserNameDirective), multi: true }]

})
export class ValidateUserNameDirective implements Validator {

  constructor(private customValidator: CustomvalidationService) { }

  validate(control: AbstractControl): Promise<{ [key: string]: any }> | Observable<{ [key: string]: any }> {
    return this.customValidator.userNameValidator(control);
  }
}
```

Cette directive est utilisée pour valider la disponibilité du nom d'utilisateur. Nous allons remplacer la méthode validate et passer le paramètre de type `AbstractControl`. Nous allons ensuite invoquer la méthode `userNameValidator` du service. Cette méthode retournera une promesse.

## Créer le composant de formulaire piloté par template

Exécutez la commande suivante pour créer le composant template-driven-form :

```
ng g c template-driven-form
```

Ouvrez `template-driven-form.component.ts` et mettez le code suivant à l'intérieur :

```
import { Component } from '@angular/core';
import { User } from '../models/user';

@Component({
  selector: 'app-template-driven-form',
  templateUrl: './template-driven-form.component.html',
  styleUrls: ['./template-driven-form.component.scss']
})
export class TemplateDrivenFormComponent {

  userModal = new User();

  constructor() { }

  onSubmit() {
    alert('Formulaire soumis avec succès!!!\n Vérifiez les valeurs dans la console du navigateur.');
    console.table(this.userModal);
  }
}
```

Nous avons créé un objet `userModal` de type User. Nous allons lier les champs du formulaire aux propriétés de cet objet. La méthode `onSubmit` affichera le message de succès à l'écran et imprimera le contenu du formulaire dans la console.

Ouvrez `template-driven-form.component.html` et mettez le code suivant à l'intérieur :

```
<div class="container">
    <div class="row">
        <div class="col-md-8 mx-auto">
            <div class="card">
                <div class="card-header">
                    <h3>Formulaire piloté par template dans Angular</h3>
                </div>
                <div class="card-body">
                    <form class="form" #registerForm="ngForm" [appMatchPassword]="['password', 'confirmPassword']"
                        (ngSubmit)="registerForm.form.valid && onSubmit()" novalidate>
                        <div class=" form-group">
                            <label>Nom</label>
                            <input type="text" class="form-control" [(ngModel)]="userModal.name" name="name"
                                #name="ngModel" required>
                            <span class="text-danger"
                                *ngIf="(name.touched || registerForm.submitted) && name.errors?.required">
                                Le nom est requis
                            </span>
                        </div>
                        <div class="form-group">
                            <label>Email</label>
                            <input type="text" class="form-control" [(ngModel)]="userModal.email" name="email"
                                #email="ngModel" required email>
                            <span class="text-danger"
                                *ngIf="(email.touched || registerForm.submitted) && email.errors?.required">
                                L'email est requis
                            </span>
                            <span class="text-danger" *ngIf="email.touched && email.errors?.email">
                                Entrez une adresse email valide
                            </span>
                        </div>
                        <div class="form-group">
                            <label>Nom d'utilisateur</label>
                            <input type="text" class="form-control" [(ngModel)]="userModal.username" name="username"
                                #username="ngModel" appValidateUserName required>
                            <span class="text-danger"
                                *ngIf="(username.touched || registerForm.submitted) && username.errors?.required">
                                Le nom d'utilisateur est requis
                            </span>
                            <span class="text-danger" *ngIf="username.touched && username.errors?.userNameNotAvailable">
                                Nom d'utilisateur non disponible
                            </span>
                        </div>
                        <div class="form-group">
                            <label>Mot de passe</label>
                            <input type="password" class="form-control" [(ngModel)]="userModal.password" name="password"
                                #password="ngModel" appPasswordPattern required>
                            <span class="text-danger"
                                *ngIf="(password.touched || registerForm.submitted) && password.errors?.required">
                                Le mot de passe est requis
                            </span>
                            <span class="text-danger" *ngIf="password.touched && password.errors?.invalidPassword">
                                Le mot de passe doit contenir au moins 8 caractères, dont au moins 1 lettre majuscule, 1 lettre minuscule et 1 chiffre
                            </span>
                        </div>
                        <div class="form-group">
                            <label>Confirmer le mot de passe</label>
                            <input type="password" class="form-control" [(ngModel)]="userModal.confirmPassword"
                                name="confirmPassword" #confirmPassword="ngModel" required>
                            <span class="text-danger"
                                *ngIf="(confirmPassword.touched || registerForm.submitted) && confirmPassword.errors?.required">
                                La confirmation du mot de passe est requise
                            </span>
                            <span class="text-danger"
                                *ngIf="confirmPassword.touched && confirmPassword.errors?.passwordMismatch">
                                Les mots de passe ne correspondent pas
                            </span>
                        </div>
                        <div class="form-group">
                            <button type="submit" class="btn btn-success">S'inscrire</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
```

Nous allons créer un formulaire piloté par template et utiliser la carte Bootstrap pour le style. L'en-tête de la carte contiendra un titre tandis que le corps de la carte contiendra les champs du formulaire.

Nous allons utiliser la directive `appMatchPassword` sur notre formulaire et passer les champs password et `confirmPassword` pour la validation. La propriété `ngModel` est utilisée pour lier le contrôle de formulaire au modèle.

Pour valider la disponibilité du nom d'utilisateur, nous utiliserons la directive `appValidateUserName` sur le champ username. De même, nous utiliserons la directive `appPasswordPattern` sur le champ password pour valider le motif du mot de passe.

Nous vérifierons les erreurs dans les contrôles de formulaire puis afficherons le message d'erreur de validation approprié à l'écran.

## Créer le composant nav-bar

Exécutez la commande suivante pour créer le composant nav-bar :

```
ng g c nav-bar
```

Ouvrez `nav-bar.component.html` et mettez le code suivant à l'intérieur :

```
<nav class="navbar navbar-expand-sm navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" [routerLink]='["/"]'>Démonstration de validation de formulaire</a>
    <div class="collapse navbar-collapse">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item">
                <a class="nav-link" [routerLink]='["/template-form"]'>Formulaire Template</a>
            </li>
        </ul>
    </div>
</nav>
```

Ici, nous ajoutons le lien de navigation vers le composant de formulaire piloté par template.

## Mettre à jour le composant app

Ouvrez le fichier `app.component.html` et mettez le code suivant à l'intérieur :

```
<app-nav-bar></app-nav-bar>
<div class="container">
  <router-outlet></router-outlet>
</div>
```

## Mettre à jour le module App

Nous allons importer le module de formulaires et également configurer le routage pour notre application dans le module app. Ajoutez le code suivant dans le fichier `app.module.ts`. Vous pouvez vous référer à [GitHub](https://github.com/AnkitSharma-007/angular-forms-validation/blob/master/src/app/app.module.ts) pour le code source complet de ce fichier :

```
import { RouterModule } from '@angular/router';
import { FormsModule } from  '@angular/forms';

@NgModule({
  ...    
  imports: [
    ...
    FormsModule,
    RouterModule.forRoot([
      { path: '', component: TemplateDrivenFormComponent },
      { path: 'template-form', component: TemplateDrivenFormComponent }
    ]),
  ],
})
```

## Démonstration d'exécution

Utilisez la commande suivante pour démarrer le serveur web :

```
ng serve -o
```

Cette commande lancera l'application dans votre navigateur par défaut à l'adresse `http://localhost:4200/`. Vous pouvez effectuer toutes les validations de formulaire que nous avons discutées ici.

Cette application est également hébergée à l'adresse [https://ng-forms-validation.herokuapp.com/](https://ng-forms-validation.herokuapp.com/). Naviguez vers le lien et jouez avec pour une meilleure compréhension.

## Résumé

Nous avons créé un exemple de formulaire d'inscription utilisateur en utilisant l'approche de formulaire piloté par template dans Angular. Nous avons implémenté les validations intégrées ainsi que les validations personnalisées pour le formulaire. La bibliothèque Bootstrap est utilisée pour styliser le formulaire.

Obtenez le code source depuis [GitHub](https://github.com/AnkitSharma-007/angular-forms-validation) et jouez avec pour une meilleure compréhension.

## Voir aussi

* [Validation de formulaire réactif dans Angular](https://ankitsharmablogs.com/reactive-form-validation-in-angular/)
* [Localisation dans Angular en utilisant les outils i18n](https://ankitsharmablogs.com/localization-in-angular-using-i18n-tools/)
* [Autorisation basée sur les politiques dans Angular en utilisant JWT](https://ankitsharmablogs.com/policy-based-authorization-in-angular-using-jwt/)
* [ASP.NET Core – Utilisation de Highcharts avec Angular 5](https://ankitsharmablogs.com/asp-net-core-using-highcharts-with-angular-5/)
* [ASP.NET Core – CRUD utilisant Angular et Entity Framework Core](https://ankitsharmablogs.com/asp-net-core-crud-using-angular-and-entity-framework-core/)

Vous pouvez trouver cet article [Validation de formulaire piloté par template dans Angular](https://ankitsharmablogs.com/template-driven-form-validation-in-angular/) et d'autres similaires sur [Le blog d'Ankit Sharma](https://ankitsharmablogs.com/).