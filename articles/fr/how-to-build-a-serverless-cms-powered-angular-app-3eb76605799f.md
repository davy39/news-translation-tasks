---
title: Comment créer une application Angular alimentée par un CMS serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T22:44:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-serverless-cms-powered-angular-app-3eb76605799f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*5P2Krzh734kVxaQJ.
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment créer une application Angular alimentée par un CMS serverless
seo_desc: 'By Jake Lumetta

  This tutorial is a follow-up to my previous tutorial on how to build a serverless
  CMS-powered Vue.js application, and shows you how to build a serverless CMS-powered
  Angular app.


  _[Unsplash](https://unsplash.com/@helloquence?utm_sour...'
---

Par Jake Lumetta

Ce tutoriel est une suite de mon [précédent tutoriel](https://medium.freecodecamp.org/how-to-build-a-serverless-cms-powered-vue-js-application-ee17f5957538) sur la création d'une application Vue.js alimentée par un CMS serverless, et vous montre comment créer une application Angular alimentée par un CMS serverless.

![Image](https://cdn-media-1.freecodecamp.org/images/H1ERkty7MoNY-zkHQ7ayRNAJjLhC06rnqtM6)
_[Unsplash](https://unsplash.com/@helloquence?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Helloquence</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Angular, développé et maintenu par des ingénieurs de Google, a trouvé sa place dans les applications web dynamiques et est un langage de plus en plus demandé. C'est un langage robuste et complet pour le développement front-end qui est prêt pour les tests unitaires, ce qui en fait le langage de choix pour de nombreux développeurs. Angular simplifie l'expérience de développement front-end en étendant la syntaxe HTML pour vous permettre de créer rapidement des capacités de gestion de contenu.

Grâce à la simplicité d'Angular, les développeurs l'utilisent de plus en plus pour ajouter des capacités de CMS aux sites web.

Pour les utilisateurs de WordPress, une façon populaire d'intégrer des capacités de gestion de contenu est de travailler avec la bibliothèque wp-api-angular qui vous permet d'interagir avec l'API WordPress et les applications Angular. Si vous utilisez WordPress comme plateforme CMS, l'utilisation d'Angular et de l'API WordPress peut réduire les temps de chargement du contenu sur votre page.

Pour ceux qui n'utilisent pas WordPress, il existe une nouvelle génération de CMS basés sur API qui simplifient grandement les choses. Nous allons en discuter un exemple ici.

Dans cet article, nous allons utiliser [ButterCMS](https://buttercms.com/) comme alternative à WordPress et comme exemple de CMS headless basé sur SaaS qui fournit un tableau de bord CMS hébergé et une API de contenu que vous interrogez depuis votre application Angular. Cela signifie que vous n'avez pas besoin de mettre en place une nouvelle infrastructure pour ajouter un CMS à votre application Angular.

Ce tutoriel démontrera comment créer une application Angular alimentée par un CMS qui comprend des pages marketing (études de cas clients), un blog et une FAQ, le tout alimenté par API. Aucun serveur nécessaire !

### Installation

Tout d'abord, vous allez commencer par installer l'interface de ligne de commande Angular.

```
npm install -g @angular/cli
```

Configurez un nouveau projet Angular en utilisant l'interface de ligne de commande Angular. Par défaut, angular-cli utilise le style CSS, donc l'ajout du drapeau `--style=scss` indique à Angular CLI d'utiliser SCSS à la place.

```
ng new hello-buttercms-project --style=scss
cd hello-buttercms-project
```

Installez Angular Material et les packages associés à Angular Material.

```
npm install --save @angular/material @angular/cdk
npm install --save @angular/animations
```

Installez ButterCMS. Exécutez cette commande dans votre ligne de commande :

```
npm install buttercms --save
```

Butter peut également être chargé en utilisant un CDN :

```
<script src="https://cdnjs.buttercms.com/buttercms-1.1.1.min.js"></script>
```

### Démarrage rapide

Ouvrez le projet dans l'éditeur de code de votre choix. Sous src/app, créez un répertoire appelé `_services`.

Nous allons créer un fichier appelé `butterCMS.service.js`. Cela vous permet d'avoir votre jeton API à un seul endroit et de ne pas le modifier accidentellement.

```
import * as Butter from 'buttercms';
```

```
export const butterService = Butter('b60a008584313ed21803780bc9208557b3b49fbb');
```

Vous allez importer ce fichier dans tout composant où vous souhaitez utiliser ButterCMS.

Pour un démarrage rapide, allez dans `src/app/hello-you/hello-you.component.ts` et importez `butterService`.

```
import {butterService} from '../_services';
```

À l'intérieur du `HelloYouComponent`, créez des méthodes :

```
fetchPosts() {
  butter.post.list({
    page: 1,
    page_size: 10
  })
  .then((res) => {
    console.log('Contenu de ButterCMS')
    console.log(res)
  })
}
```

Maintenant, appelez cette méthode lorsque le composant est chargé en l'ajoutant au hook de cycle de vie `OnInit` :

```
ngOnInit() {
  this.fetchPosts();
}
```

Cette requête API récupère un exemple d'article de blog. Votre compte est livré avec un exemple de publication que vous verrez dans la réponse. Si vous obtenez une réponse, cela signifie que vous êtes maintenant en mesure de vous connecter à l'API.

### Ajouter des pages marketing

La configuration de pages alimentées par CMS est un processus en trois étapes :

1. Définir le type de page
2. Créer une page
3. Intégrer dans votre application

#### **Définir la page**

Tout d'abord, créez un type de page pour représenter vos pages d'études de cas clients. Ensuite, définissez les champs que vous souhaitez pour vos études de cas clients. Avec votre type de page défini, vous pouvez maintenant créer la première page d'étude de cas. Spécifiez le nom et l'URL de la page, puis remplissez le contenu de la page.

![Image](https://cdn-media-1.freecodecamp.org/images/fxruBTuJEAibmwUHLClhhR1g02XRq73waSsS)

Avec votre page définie, l'API ButterCMS la retournera au format JSON comme ceci :

```
{
    "data": {
      "slug": "acme-co",
      "fields": {
        "facebook_open_graph_title": "Acme Co loves ButterCMS",
        "seo_title": "Acme Co Customer Case Study",
        "headline": "Acme Co saved 200% on Anvil costs with ButterCMS",
        "testimonial": "<p>We’ve been able to make anvils faster than ever before! — <em>Chief Anvil Maker</em></p>\r\n<p><img src=\"https://cdn.buttercms.com/NiA3IIP3Ssurz5eNJ15a\" alt=\"\" caption=\"false\" width=\"249\" height=\"249\" /></p>",
        "customer_logo": "https://cdn.buttercms.com/c8oSTGcwQDC5I58km5WV",
        }
     }
  }
```

Ce guide utilise le framework Angular et Angular CLI pour générer tous les composants et packager notre application.

Passons au code.

#### Créer un nouveau projet

```
ng new buttercms-project --style=scss
cd buttercms-project
npm install --save @angular/material @angular/cdk
npm install --save @angular/animations
npm install -S buttercms
ng serve
```

Votre localhost:4200 devrait être prêt à servir votre page Angular.

#### Créer un fichier TypeScript pour exporter le service ButterCMS

Sous `src/app`, créez un répertoire appelé `_services`. Créez un fichier appelé `butterCMS.service.js`.

```
import * as Butter from 'buttercms';
export const butterService = Butter('your_api_token');
```

#### Mettre à jour les routes des composants

Ces composants sont générés par Angular CLI en utilisant :

`ng g component <my-new-component>`

Sous `src/app`, créez un fichier appelé `app-routing.module.ts`.

```
import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {CustomerComponent} from './customer/listing/customer.listing.component';
import {FaqComponent} from './faq/faq.component';
import {BlogPostComponent} from './blog-post/listing/blog-post.component';
import {HomeComponent} from './home/home.component';
import {CustomerDetailsComponent} from './customer/details/customer.details.component';
import {BlogPostDetailsComponent} from './blog-post/details/blog-post.details.component';
import {FeedComponent} from './feed/feed.component';
import {HelloYouComponent} from './hello-you/hello-you.component';
```

```
const appRoutes: Routes = [
    {path: 'customer', component: CustomerComponent},
    {path: 'customer/:slug', component: CustomerDetailsComponent},
    {path: 'faq', component: FaqComponent},
    {path: 'blog', component: BlogPostComponent},
    {path: 'blog/:slug', component: BlogPostDetailsComponent},
    {path: 'rss', component: FeedComponent},
    {path: 'hello-you', component: HelloYouComponent},
    {path: 'home', component: HomeComponent},
    {path: '**', redirectTo: 'home'}];
```

```
@NgModule({
    imports: [RouterModule.forRoot(appRoutes)],
    exports: [RouterModule]})
export class AppRoutingModule {}
```

### Configurer la page de liste des clients

Sous `apps/customer`, tapez : `ng g component`.

Dans le fichier `apps/customer/listing/customer.listing.component.ts` :

1. Importez `butterService`
2. Dans le hook `OnInit`, utilisez `butterService` pour obtenir la liste des clients
3. Stockez les résultats dans la variable pages et le balisage (HTML) sera mis à jour avec les données

```
import {Component, OnInit} from '@angular/core';
import {butterService} from '../../_services';
```

```
@Component({
    selector: 'app-customer',
    templateUrl: './customer.listing.component.html',
    styleUrls: ['./customer.listing.component.scss']})
```

```
export class CustomerComponent implements OnInit {
  public pages: any[];
  constructor() { }
```

```
ngOnInit() {
  butterService.page.list('customer_case_study')
    .then((res) => {
      this.pages = res.data.data;
  });
}
```

Affichez les résultats dans `customer.listing.component.html`.

```
<mat-card>
  <mat-card-title class="page-title">Clients</mat-card-title>
  <mat-divider></mat-divider>
  <mat-card-content class="page-body">
    <mat-card *ngFor="let page of pages">
      <mat-card-title>
        <div class="container">
          <a [routerLink]="[page.slug]">
            <div fxLayout="row" fxLayout.xs="column"
                 fxFlex class="content">
            <div class="blocks">
              <img src="{{page.fields.customer_logo}}" alt="{{page.fields.seotitle}}" height="64" width="64"/>
            </div>
            <div class="blocks">
              {{page.fields.headline}}
            </div>
          </div>
        </a>
      </div>
    </mat-card-title>
  </mat-card>
</mat-card-content>
<mat-divider></mat-divider>
<mat-card-footer>
  <div class="page-footer">
    <mat-icon>whatshot</mat-icon>
  </div>
</mat-card-footer>
</mat-card>
```

### Configurer la page de détails du client

Sous `apps/customer`, tapez `ng g component details`.

```
apps/customer/details/customer.details.component.ts
```

#### Créer une page client

1. Importez `butterService`
2. Dans le hook `OnInit`, utilisez `butterService` pour obtenir la page client donnée le slug dans le chemin de l'URL
3. Stockez les résultats dans la variable page et le balisage (HTML) sera mis à jour avec les données du client

```
import {Component, OnInit} from '@angular/core';
import {Observable} from 'rxjs/Observable';
import {ActivatedRoute} from '@angular/router';
import {butterService} from '../../_services';
import {map, take} from 'rxjs/operators';
```

```
@Component({
  selector: 'app-customer-details',
  templateUrl: './customer.details.component.html',
  styleUrls: ['./customer.details.component.scss']})
```

```
export class CustomerDetailsComponent implements OnInit {
  constructor(protected route: ActivatedRoute) { }
```

```
  protected slug$: Observable<string>;
  public page: any;
```

```
  ngOnInit() {
    this.slug$ = this.route.paramMap
    .pipe(
      map(params => (params.get('slug')))
   );
```

```
    this.slug$.pipe(
      take(1))
        .subscribe(slug => {
          butterService.page.retrieve('customer_case_study', slug)
            .then((res) => {
              this.page = res.data.data;
            }).catch((res) => {
            console.log(res);
          });
        });
      }
    }
```

Affichez les résultats dans `customer.details.component.html`.

```
<mat-card>
  <div class="container">
    <div fxLayout="column" class="details">
      <div class="blocks">
        <img src="{{page.fields.customer_logo}}" alt="" height="124" width="124"/>
      </div>
```

```
      <h1 class="blocks">
        {{page.fields.headline}}
      </h1>
      <h3 class="is-size-3">Témoignages</h3>
      <div [innerHTML]="page.fields.testimonial"></div>
      <div [innerHTML]="page.fields.body"></div>
    </div>
  </div>
</mat-card>
```

Vous pouvez maintenant naviguer vers la page client via la liste de toutes les pages clients ou directement via l'URL.

### Ajouter une base de connaissances

#### Configurer les champs de contenu

Supposons que vous souhaitiez ajouter un CMS à une page FAQ statique avec un titre et une liste de questions avec réponses.

Rendre votre contenu dynamique avec Butter est un processus en deux étapes :

1. Configurer des champs de contenu personnalisés dans Butter
2. Intégrer les champs dans votre application

Pour configurer des champs de contenu personnalisés, connectez-vous d'abord au tableau de bord Butter.

Créez un nouvel espace de travail ou cliquez sur un espace de travail existant. Les espaces de travail vous permettent d'organiser les champs de contenu de manière conviviale pour les éditeurs de contenu et n'ont aucun effet sur le développement ou l'API. Par exemple, un site immobilier pourrait avoir un espace de travail appelé « Properties » et un autre appelé « About Page ».

![Image](https://cdn-media-1.freecodecamp.org/images/qeOtvQ6EyV2Ch2ydKxz-jZD0oudTrWPm3fIt)

Une fois dans un espace de travail, cliquez sur le bouton pour créer un nouveau champ de contenu. Choisissez le type « Object » et nommez le champ « FAQ Headline ».

![Image](https://cdn-media-1.freecodecamp.org/images/fCjTN2LyszZoEbvJEFXJke4YmD0TGn6V9fZ7)

Après avoir enregistré, ajoutez un autre champ, mais cette fois choisissez le type « Collection » et nommez le champ `FAQ Items`.

Sur l'écran suivant, configurez deux propriétés pour les éléments de la collection.

Retournez à votre espace de travail et mettez à jour votre titre et vos éléments FAQ.

### Intégrer votre application

#### Créer un composant FAQ

Sous `apps`, tapez : `ng g component faq`.

```
apps/faq/faq.component.ts
```

#### Configurer le hook onInit pour charger la FAQ

```
import {Component, OnInit} from '@angular/core';
import {butterService} from '../_services';
```

```
@Component({
  selector: 'app-faq',
  templateUrl: './faq.component.html',
  styleUrls: ['./faq.component.scss']})
```

```
export class FaqComponent implements OnInit {
  constructor() {}
```

```
  public faq: any = {
      items: [],
      title: 'FAQ'
  };
```

```
ngOnInit() {
  butterService.content.retrieve(['faq_headline', 'faq_items'])
    .then((res) => {
      console.log(res.data.data);
      this.faq.title = res.data.data.faq_headline;
      this.faq.items = res.data.data.faq_items;
    });
  }
}
```

#### Afficher le résultat

```
<mat-card>
  <mat-card-title class="page-title"></mat-card-title>
  <mat-divider></mat-divider>
  <mat-card-content class="page-body">
    <mat-card *ngFor="let item of faq.items">
      <mat-card-content>
        <h3>
          {{item.question}}
        </h3>
        <div>
          {{item.answer}}
        </div>
      </mat-card-content>
    </mat-card>
  </mat-card-content>
  <mat-divider></mat-divider>
  <mat-card-footer>
    <div class="page-footer">
      <mat-icon>whatshot</mat-icon>
    </div>
  </mat-card-footer>
</mat-card>
```

Les valeurs saisies dans le tableau de bord Butter mettront immédiatement à jour le contenu dans notre application.

### Blogging

Pour afficher les articles, vous devez créer une route `/blog` dans votre application et récupérer les articles de blog depuis l'API Butter, ainsi qu'une route `/blog/:slug` pour gérer les articles individuels.

Voir la référence de l'API pour des options supplémentaires telles que le filtrage par catégorie ou auteur. La réponse inclut également des métadonnées que nous utiliserons pour la pagination.

#### Configurer la page d'accueil du blog

Sous `apps/blog-post`, tapez : `ng g component listing`.

```
apps/blog-post/listing/blog-post.listing.component.ts
```

Mettez à jour le composant pour obtenir tous les articles :

1. Importez `butterService`
2. Obtenez tous les articles `onInit`

```
import {Component, OnInit} from '@angular/core';
import {butterService} from '../../_services';
```

```
@Component({
  selector: 'app-blog-post',
  templateUrl: './blog-post.component.html',
  styleUrls: ['./blog-post.component.scss']})
export class BlogPostComponent implements OnInit {
  public posts: any[];
```

```
 constructor() { }
```

```
ngOnInit() {
  butterService.post.list({
  page: 1,
  page_size: 10}).then((res) => {
  console.log(res.data)
  this.posts = res.data.data;
  });
}
```

Affichez le résultat :

```
<mat-card>
  <mat-card-title class="page-title">Articles de blog</mat-card-title>
  <mat-divider></mat-divider>
  <mat-card-content class="page-body">
    <mat-card *ngFor="let post of posts">
      <mat-card-title>
```

```
      <a [routerLink]="[post.slug]">
        <div class="container">
          <div fxLayout="row" fxLayout.xs="column"
            fxFlex class="content">
            <div class="blocks">
              <img *ngIf="post.featured_image" src="{{post.featured_image}}" height="64" width="64"/>
            </div>
            <div class="blocks">
              {{post.title}}
            </div>
          </div>
        </div>
        <div class="container">
          <div fxLayout="column" class="summary">
            <div [innerHTML]="post.summary"></div>
          </div>
        </div>
      </a>
    </mat-card-title>
  </mat-card>
</mat-card-content>
<mat-divider></mat-divider>
```

```
<mat-card-footer>
  <div class="page-footer">
    <mat-icon>whatshot</mat-icon>
  </div>
</mat-card-footer>
</mat-card>
```

#### Configurer la page de l'article de blog

Sous `apps/blog-post`, tapez : `ng g component details`.

```
apps/blog-post/details/blog-post.details.component.ts
```

Pour afficher un seul article :

1. Importez `butterService`
2. Dans le hook `OnInit`, utilisez `butterService` pour obtenir l'article de blog donné le slug dans le chemin de l'URL
3. Stockez les résultats dans la variable post et le balisage (HTML) sera mis à jour avec les données du client

```
import {Component, OnInit, ViewEncapsulation} from '@angular/core';
import {Observable} from 'rxjs/Observable';
import {ActivatedRoute} from '@angular/router';
import {butterService} from '../../_services';
import {map, take} from 'rxjs/operators';
```

```
@Component({
  selector: 'app-blog-post-details',
  templateUrl: './blog-post.details.component.html',
  styleUrls: ['./blog-post.details.component.scss'],
  encapsulation: ViewEncapsulation.None})
```

```
export class BlogPostDetailsComponent implements OnInit {
```

```
    constructor(protected route: ActivatedRoute) {    }
```

```
    protected slug$: Observable<string>;
    public post = {
      meta: null,
      data: null};
```

```
ngOnInit() {
  this.slug$ = this.route.paramMap
      .pipe(
        map(params => (params.get('slug')))
      );
```

```
  this.slug$.pipe(
      take(1))
      .subscribe(slug => {
        butterService.post.retrieve(slug)
          .then((res) => {
            this.post = res.data;
          }).catch((res) => {
          console.log(res);
       });
   });
}
```

Affichez le résultat :

```
<mat-card>
  <div class="container">
    <div fxLayout="column" class="blog-details">
      <div class="container">
        <div fxLayout="row">
          <h1 class="blocks">
            {{post.data.title}}
          </h1>
          <div *ngIf="post.meta.previous_post"><a [routerLink]="post.meta.previous_post"><</a></div>
          <div *ngIf="post.meta.next_post"><a [routerLink]="post.meta.next_post">></a></div>
        </div>
        <h4>
          {{post.data.author.first_name}}
          {{post.data.author.last_name}}
        </h4>
        <div class="post-body" [innerHTML]="post.data.body"></div>
      </div>
    </div>
  </div>
</mat-card>
```

Votre application dispose maintenant d'un blog fonctionnel qui peut être facilement mis à jour dans le tableau de bord ButterCMS.

### Catégories, tags et auteurs

Utilisez les API de Butter pour les catégories, les tags et les auteurs pour mettre en avant et filtrer le contenu de votre blog.

#### Lister toutes les catégories et obtenir les articles par catégorie

Appelez ces méthodes dans le hook de cycle de vie `onInit()` :

```
methods: { ... getCategories() {   butter.category.list()     .then((res) => {       console.log('Liste des catégories :')       console.log(res.data.data)     }) }, getPostsByCategory() {   butter.category.retrieve('example-category', {       include: 'recent_posts'     })     .then((res) => {       console.log('Articles avec une catégorie spécifique :')       console.log(res)     })   } }, created() { ... this.getCategories() this.getPostsByCategory()}
```

```
 getCategories() {
  butter.category.list()
  .then((res) => {
   console.log('Liste des catégories :')
   console.log(res.data.data)
  })
 }, getPostsByCategory() {
  butter.category.retrieve('example-category', {
   include: 'recent_posts'
  })
  .then((res) => {
   console.log('Articles avec une catégorie spécifique :')
   console.log(res)
  })
 }},
created() { 
  ...
  this.getCategories()
  this.getPostsByCategory()
}
```

### Conclusion

Félicitations, vous avez réussi à transformer votre application Angular statique en une application alimentée par un CMS en utilisant des API de contenu et en maintenant ainsi une architecture serverless. Votre équipe de développement peut tirer parti des aspects économiseurs de temps d'Angular, et vous avez économisé encore plus de temps en utilisant un CMS serverless.

*Si vous avez apprécié cet article, aidez-le à se diffuser en applaudissant ci-dessous ! Pour plus de contenu comme celui-ci, suivez-nous sur [Twitter](https://twitter.com/ButterCMS) et [abonnez-vous](https://buttercms.com/blog/) à notre blog.*

*Et si vous souhaitez ajouter un blog ou un [CMS Angular](https://buttercms.com/angular-cms/) à votre site web sans vous soucier de WordPress, [vous devriez essayer Butter CMS](https://buttercms.com/).*