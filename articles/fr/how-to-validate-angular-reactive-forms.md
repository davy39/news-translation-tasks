---
title: Comment valider les formulaires réactifs Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-20T09:24:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-validate-angular-reactive-forms
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e95740569d1a4ca3de6.jpg
tags:
- name: Angular
  slug: angular
- name: Form validations
  slug: form-validations
- name: forms
  slug: forms
- name: TypeScript
  slug: typescript
seo_title: Comment valider les formulaires réactifs Angular
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will learn about validations in reactive forms in Angular. We
  will create a simple user registration form and implement some inbuilt validations
  on it. Along with the inbuilt validations, we will also ...'
---

Par Ankit Sharma

## Introduction

Dans cet article, nous allons apprendre à propos des validations dans les formulaires réactifs dans Angular. Nous allons créer un simple formulaire d'inscription d'utilisateur et implémenter quelques validations intégrées. En plus des validations intégrées, nous allons également implémenter quelques validations personnalisées pour le formulaire réactif.

Nous allons considérer les validations personnalisées suivantes pour cette démonstration :

* Vérifier la disponibilité du nom d'utilisateur
* Validation du motif du mot de passe
* Faire correspondre le mot de passe saisi dans deux champs différents

Jetez un coup d'œil à l'application en action.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/reactiveFormValidation.gif)

## Prérequis

* Installer Visual Studio Code depuis [ici](https://code.visualstudio.com/)
* Installer la dernière version d'Angular CLI depuis [ici](https://cli.angular.io/)

## Code source

Obtenez le code source depuis [GitHub](https://github.com/AnkitSharma-007/angular-forms-validation).

## Créer l'application Angular

Naviguez vers le dossier où vous souhaitez créer votre fichier de projet. Ouvrez une fenêtre de commande et exécutez la commande suivante :

```
ng new angular-forms-validation --routing=false --style=scss
```

Nous spécifions la commande pour créer une nouvelle application Angular. L'option pour créer le module de routage est définie sur false et l'extension des fichiers de style est définie sur `scss`. Cette commande créera le projet Angular avec le nom `angular-forms-validation`.

Changez de répertoire pour le nouveau projet et ouvrez le projet dans VS Code en utilisant l'ensemble de commandes suivant :

```
cd angular-forms-validation 
code .
```

## Installer Bootstrap

Exécutez la commande suivante pour installer la bibliothèque Bootstrap :

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

Cette commande créera un dossier nommé services qui contient deux fichiers : `customvalidation.service.ts` et `customvalidation.service.spec.ts`. Ouvrez le fichier `customvalidation.service.ts` et placez le code suivant dedans :

```js
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

Nous allons utiliser une expression régulière pour valider le mot de passe. Nous allons valider les quatre conditions suivantes en utilisant l'expression régulière :

* Le mot de passe doit avoir une longueur minimale de huit caractères.
* Il contient au moins une lettre minuscule.
* Il contient au moins une lettre majuscule.
* Il contient au moins un chiffre.

Si le mot de passe échoue à la vérification regex, nous allons définir la propriété `invalidPassword` à vrai.

La méthode `MatchPassword` est utilisée pour comparer les mots de passe dans deux champs. Cette méthode acceptera deux paramètres de type string. Ces paramètres représentent le nom des champs à faire correspondre. Nous allons obtenir le `FormControl` pour ces deux champs et ensuite faire correspondre les valeurs qu'ils contiennent. Si les valeurs ne correspondent pas, nous allons définir la propriété `passwordMismatch` à vrai.

La méthode `userNameValidator` est utilisée pour vérifier si le nom d'utilisateur est déjà pris ou non. Cette méthode acceptera un paramètre de type `AbstractControl`. Nous allons vérifier si la valeur de ce champ est présente dans un tableau statique, `UserList`. Si la valeur saisie par l'utilisateur est déjà présente, nous allons définir la propriété `userNameNotAvailable` à vrai.

Nous utilisons la fonction `setTimeout` pour invoquer cette vérification toutes les deux secondes. Cela garantira que l'erreur sera levée deux secondes après que l'utilisateur ait arrêté de taper dans le champ.

> Pour la simplicité de cet article, nous utilisons un tableau statique pour rechercher la disponibilité des noms d'utilisateur. Idéalement, cela devrait être un appel de service au serveur pour rechercher la valeur dans une base de données.

## Créer le composant de formulaire réactif

Exécutez la commande suivante pour créer le composant reactive-form :

```
ng g c reactive-form
```

Ouvrez `reactive-form.component.ts` et placez le code suivant dedans :

```js
import { Component, OnInit } from '@angular/core';
import { Validators, FormGroup, FormBuilder } from '@angular/forms';
import { CustomvalidationService } from '../services/customvalidation.service';

@Component({
  selector: 'app-reactive-form',
  templateUrl: './reactive-form.component.html',
  styleUrls: ['./reactive-form.component.scss']
})
export class ReactiveFormComponent implements OnInit {

  registerForm: FormGroup;
  submitted = false;

  constructor(
    private fb: FormBuilder,
    private customValidator: CustomvalidationService
  ) { }

  ngOnInit() {
    this.registerForm = this.fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      username: ['', [Validators.required], this.customValidator.userNameValidator.bind(this.customValidator)],
      password: ['', Validators.compose([Validators.required, this.customValidator.patternValidator()])],
      confirmPassword: ['', [Validators.required]],
    },
      {
        validator: this.customValidator.MatchPassword('password', 'confirmPassword'),
      }
    );
  }

  get registerFormControl() {
    return this.registerForm.controls;
  }

  onSubmit() {
    this.submitted = true;
    if (this.registerForm.valid) {
      alert('Formulaire soumis avec succès!!!\n Vérifiez les valeurs dans la console du navigateur.');
      console.table(this.registerForm.value);
    }
  }
}
```

Nous allons créer une variable `registerForm` de type `FormGroup`. Dans la méthode `ngOnInit`, nous allons définir les contrôles pour le formulaire en utilisant la classe `FormBuilder`. Tous les champs sont définis comme champs obligatoires pour ce formulaire. Nous allons invoquer la méthode `userNameValidator` du service en utilisant la fonction bind.

Pour le champ mot de passe, nous allons utiliser la méthode compose pour fusionner plusieurs validateurs en une seule fonction. Nous allons également invoquer la méthode `MatchPassword` et passer le nom des contrôles de formulaire `password` et `confirmPassword` en tant que paramètres.

La propriété `registerFormControl` retournera les contrôles de formulaire du formulaire. La méthode `onSubmit` imprimera le contenu du formulaire sur la console si le formulaire est valide et soumis avec succès.

Ouvrez `reactive-form.component.html` et placez le code suivant dedans :

```html
<div class="container">
    <div class="row">
        <div class="col-md-8 mx-auto">
            <div class="card">
                <div class="card-header">
                    <h3>Formulaire Réactif Angular</h3>
                </div>
                <div class="card-body">
                    <form class="form" [formGroup]="registerForm" (ngSubmit)="onSubmit()">
                        <div class="form-group">
                            <label>Nom</label>
                            <input type="text" class="form-control" formControlName="name">
                            <span class="text-danger"
                                *ngIf="(registerFormControl.name.touched || submitted) && registerFormControl.name.errors?.required">
                                Le nom est requis
                            </span>
                        </div>
                        <div class="form-group">
                            <label>Email</label>
                            <input type="text" class="form-control" formControlName="email">
                            <span class="text-danger"
                                *ngIf="(registerFormControl.email.touched || submitted) && registerFormControl.email.errors?.required">
                                L'email est requis
                            </span>
                            <span class="text-danger"
                                *ngIf="registerFormControl.email.touched && registerFormControl.email.errors?.email">
                                Entrez une adresse email valide
                            </span>
                        </div>
                        <div class="form-group">
                            <label>Nom d'utilisateur</label>
                            <input type="text" class="form-control" formControlName="username">
                            <span class="text-danger"
                                *ngIf="(registerFormControl.username.touched || submitted) && registerFormControl.username.errors?.required">
                                Le nom d'utilisateur est requis
                            </span>
                            <span class="text-danger"
                                *ngIf="registerFormControl.username.touched && registerFormControl.username.errors?.userNameNotAvailable">
                                Le nom d'utilisateur n'est pas disponible
                            </span>
                        </div>
                        <div class="form-group">
                            <label>Mot de passe</label>
                            <input type="password" class="form-control" formControlName="password">
                            <span class="text-danger"
                                *ngIf="(registerFormControl.password.touched || submitted) && registerFormControl.password.errors?.required">
                                Le mot de passe est requis
                            </span>
                            <span class="text-danger"
                                *ngIf="registerFormControl.password.touched && registerFormControl.password.errors?.invalidPassword">
                                Le mot de passe doit avoir un minimum de 8 caractères, au moins 1 lettre majuscule, 1 lettre minuscule et 1 chiffre
                            </span>
                        </div>
                        <div class="form-group">
                            <label>Confirmer le mot de passe</label>
                            <input type="password" class="form-control" formControlName="confirmPassword">
                            <span class="text-danger"
                                *ngIf="(registerFormControl.confirmPassword.touched || submitted)&& registerFormControl.confirmPassword.errors?.required">
                                La confirmation du mot de passe est requise
                            </span>
                            <span class="text-danger"
                                *ngIf="registerFormControl.confirmPassword.touched && registerFormControl.confirmPassword.errors?.passwordMismatch">
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

Nous allons créer un formulaire réactif et utiliser la carte Bootstrap pour le style. L'en-tête de la carte contiendra un titre tandis que le corps de la carte contiendra les champs du formulaire. Nous allons lier la propriété `formGroup` de la balise `<form>` au nom de notre formulaire qui est `registerForm`. La méthode `onSubmit` sera invoquée lors de la soumission du formulaire. Nous allons également lier la propriété `formControlName` de chaque champ d'entrée au nom du contrôle de notre `FormGroup`. Nous allons vérifier les erreurs dans les contrôles de formulaire et ensuite afficher le message d'erreur de validation approprié à l'écran.

## Créer le composant nav-bar

Exécutez la commande suivante pour créer le composant nav-bar :

```
ng g c nav-bar
```

Ouvrez `nav-bar.component.html` et placez le code suivant dedans :

```html
<nav class="navbar navbar-expand-sm navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" [routerLink]='[""]'>Démonstration de Validation de Formulaire</a>
    <div class="collapse navbar-collapse">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item">
                <a class="nav-link" [routerLink]='["reactive-form"]'>Formulaire Réactif</a>
            </li>
        </ul>
    </div>
</nav>
```

Nous ajoutons le lien de navigation vers le composant de formulaire réactif dans la barre de navigation.

## Mettre à jour le composant app

Ouvrez le fichier `app.component.html` et placez le code suivant dedans :

```html
<app-nav-bar></app-nav-bar>
<div class="container">
  <router-outlet></router-outlet>
</div>
```

## Mettre à jour le module App

Ajoutez le code suivant dans le fichier `app.module.ts`. Nous allons importer le module de formulaires et définir le routage pour notre application. Vous pouvez vous référer à [GitHub](https://github.com/AnkitSharma-007/angular-forms-validation/blob/master/src/app/app.module.ts) pour le code source complet de ce fichier.

```js
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from  '@angular/forms';

@NgModule({
  ...    
  imports: [
    ...
    ReactiveFormsModule,
    RouterModule.forRoot([
      { path: '', component: ReactiveFormComponent },
      { path: 'reactive-form', component: ReactiveFormComponent }
    ]),
  ],
})
```

## Démonstration d'exécution

Nous allons utiliser la commande suivante pour démarrer le serveur web :

```
ng serve -o
```

Cette commande lancera l'application dans votre navigateur par défaut à l'adresse `http://localhost:4200/`. Vous pouvez effectuer toutes les validations de formulaire que nous avons discutées ici.

Cette application est également hébergée à l'adresse [https://ng-forms-validation.herokuapp.com/](https://ng-forms-validation.herokuapp.com/). Naviguez vers le lien et jouez avec pour une meilleure compréhension.

## Résumé

Nous avons créé un exemple de formulaire d'inscription d'utilisateur en utilisant l'approche de formulaire réactif dans Angular. Nous avons implémenté les validations intégrées ainsi que les validations personnalisées pour le formulaire. La bibliothèque Bootstrap est utilisée pour styliser le formulaire.

Obtenez le code source depuis [GitHub](https://github.com/AnkitSharma-007/angular-forms-validation) et jouez avec pour une meilleure compréhension.

## Voir aussi

* [Localisation dans Angular en utilisant les outils i18n](https://ankitsharmablogs.com/localization-in-angular-using-i18n-tools/)
* [Validation de formulaire pilotée par modèle dans Angular](https://ankitsharmablogs.com/template-driven-form-validation-in-angular/)
* [Comprendre l'animation Angular](https://ankitsharmablogs.com/understanding-angular-animation/)
* [Autorisation basée sur les politiques dans Angular en utilisant JWT](https://ankitsharmablogs.com/policy-based-authorization-in-angular-using-jwt/)
* [Authentification et autorisation Facebook dans une application Blazor côté serveur](https://ankitsharmablogs.com/facebook-authentication-and-authorization-in-server-side-blazor-app/)

Vous pouvez trouver d'autres articles comme [Validation de formulaire réactif dans Angular](https://ankitsharmablogs.com/reactive-form-validation-in-angular/) sur [le blog d'Ankit Sharma](https://ankitsharmablogs.com/).