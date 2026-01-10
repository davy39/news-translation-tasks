---
title: Comment créer une application web progressive avec Angular et un CMS headless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-17T16:47:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-progressive-web-app-featuring-angular-and-headless-cms-b8ee4f7a5ea3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZBkMjm06K3zeKAuXCL0mkg.png
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: progressive web app
  slug: progressive-web-app
- name: 'tech '
  slug: tech
seo_title: Comment créer une application web progressive avec Angular et un CMS headless
seo_desc: 'By Ondrej Chrastina

  Have you ever wondered how a headless Content Management System fits in with Progressive
  Web Apps?

  I recently read my colleague Bryan’s story about Progressive Web Apps. The article
  talks about the implementation of a Progressive ...'
---

Par Ondrej Chrastina

Vous êtes-vous déjà demandé comment un système de gestion de contenu headless s'intègre avec les applications web progressives ?

J'ai récemment lu l'article de mon collègue [Bryan](https://www.freecodecamp.org/news/how-to-create-a-progressive-web-app-featuring-angular-and-headless-cms-b8ee4f7a5ea3/undefined) sur les applications web progressives. L'article parle de la mise en œuvre d'une [application web progressive](https://developers.google.com/web/progressive-web-apps) (PWA) qui liste des lieux intéressants stockés dans le CMS headless.

Vous pourriez installer cette application sur votre appareil. Elle utilise un service worker pour mettre en cache l'application et les données sur les points d'intérêt. L'application a été écrite en JavaScript simple.

Ayant écrit une bonne partie de code JavaScript, j'ai voulu approfondir le concept en utilisant des frameworks plus complexes.

J'ai réduit mes choix à trois grands acteurs — React, Vue et Angular. J'ai choisi d'utiliser Angular, car il prend déjà en charge les service workers, et je voulais utiliser [TypeScript](https://www.typescriptlang.org/).

Chaque étape de ce tutoriel sera accompagnée d'un lien vers un commit GitHub. Ainsi, vous pourrez toujours voir à quoi ressemble le code.

Pour exécuter l'application, téléchargez ou clonez simplement le commit et exécutez `npm install` et `ng serve -o`. L'ensemble du code est stocké dans [l'une des branches](https://github.com/Kentico/cloud-sample-angular-pwa-app/commits/v1-introduction).

Commençons !

#### Prérequis

* [node.js](https://nodejs.org/en/download) v8+
* [Angular CLI](https://www.npmjs.com/package/@angular/cli) v.1.7.4 installé en tant que dépendance globale via le gestionnaire de paquets npm : `npm install -g @angular/cli`

#### Mise en route

Tout d'abord, générez un nouveau projet. Vous pouvez facilement générer tout le code de base à l'aide des outils Angular CLI. Naviguez simplement vers un dossier et générez un code prêt à être exécuté :

```bash
ng new cloud-sample-angular-pwa-aps
```

#### Configuration du code de base

![Image](https://cdn-media-1.freecodecamp.org/images/4Hjiz65hb-1T-nUK-LjuICXRKbymmoBvyx88)
_[Commit de configuration du code de base](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/1857f253955e4abf0685222fa958d199648dd6ba" rel="noopener" target="_blank" title=")_

Il y a quelques étapes pour configurer le code de base.

Le code généré utilise CSS simple par défaut. Mais vous pourriez vouloir vous faciliter la vie avec SCSS. Pour ce faire, suivez ces étapes :

1. Définissez la valeur `defaults.styleExt` de `css` à `scss` dans le fichier de configuration `/.angular-cli.json`
2. Renommez `styles.css` en `styles.scss`
3. Renommez `/src/app.component.css` en `/src/app.component.scss` et reflétez ce renommage dans `app.component.ts` dans la valeur de la propriété `styleUrls` de l'attribut de déclaration du composant.

#### **Créer un contenu initial pour l'application**

* Styles globaux : [/src/styles.scss](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/1857f253955e4abf0685222fa958d199648dd6ba#diff-6a2256f44598ec970b4bd034962e011e)
* Composant : [/src/app/app.component.html](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/1857f253955e4abf0685222fa958d199648dd6ba#diff-465e9f13ce23ec4a1e366935273fdbb6) et [/src/app/app.component.scss](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/1857f253955e4abf0685222fa958d199648dd6ba#diff-f4c58ad626d121a4d36442d6696213eb)

Regardons ça !

![Image](https://cdn-media-1.freecodecamp.org/images/Al8CUwqAdD24f1o-Wuw5u4xrLM8HYpSmFaM7)
_Voilà, premier lancement de l'application._

Exécutez simplement cette commande :

```bash
ng serve -o
```

#### Charger les données

![Image](https://cdn-media-1.freecodecamp.org/images/4LCfjsHaWVGURtUehLSGhtx2095mR96ExNEr)
_[Commit de chargement des données.](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/00072d54eda9023f6f9176fc6de3ed49b339b602" rel="noopener" target="_blank" title=")_

Utilisons enfin la puissance d'Angular. Dans cette section, nous allons définir un client [injectable](https://angular.io/guide/dependency-injection) qui permet à l'application d'obtenir les données de [Kentico Cloud](https://kenticocloud.com/). J'utiliserai la même source de données que Bryan a utilisée dans son article.

Tout d'abord, installez le [SDK de livraison Kentico Cloud](https://github.com/Enngage/KenticoCloudDeliveryTypeScriptSDK) via la commande suivante :

```bash
npm install -P kentico-cloud-delivery-typescript-sdk
```

Ensuite, créez un fournisseur de client qui sera utilisé dans l'injection de dépendances.

Créez un nouveau fichier dans le dossier `/src/app` et nommez-le `delivery-client.provider.ts`. Ce module [fournisseur](https://angular.io/guide/dependency-injection#factory-providers) doit exporter un objet définissant la factory utilisée pour créer notre client. Dans le code ci-dessous, vous pouvez voir l'ID du projet dans Kentico Cloud où les données sont stockées.

```ts
import { DeliveryClient, DeliveryClientConfig } from 'kentico-cloud-delivery-typescript-sdk';

export const DeliveryClientFactory = (): DeliveryClient => {
    const projectId = '975bf280-fd91-488c-994c-2f04416e5ee3';
    
    return new DeliveryClient(
        new DeliveryClientConfig(projectId, [])
    );
};

export const DeliveryClientProvider = {
    provide: DeliveryClient,
    useFactory: DeliveryClientFactory,
    deps: []
};
```

Ensuite, modifiez `app.module.ts`. C'est ici que vous indiquez quels modules sont chargés.

```ts
... 
import { DeliveryClientProvider } from './delivery-client.provider';
...

@NgModule({
...
providers: [DeliveryClientProvider]
...
})
```

Maintenant, nous sommes prêts à utiliser le client dans le composant de l'application.

Nous allons configurer `app.component.ts` pour utiliser le `DeliveryClient` qui est automatiquement injecté en tant que paramètre du constructeur. Nous allons également abonner le composant à l'observable du client et nous allons définir une action d'observateur correspondante.

```ts
import { Component, OnInit, OnDestroy } from '@angular/core';
import { DeliveryClient, ContentItem } from 'kentico-cloud-delivery-typescript-sdk';
import { Subscription } from 'rxjs/Subscription';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit, OnDestroy {
  dataSubscription: Subscription;
  pointsOfInterest: ContentItem[];
  
constructor(private deliveryClient: DeliveryClient) { }

ngOnInit() {
    this.dataSubscription = this.deliveryClient
      .items<ContentItem>()
      .type('point_of_interest')
      .get()
      .subscribe(response => {
        this.pointsOfInterest = response.items;
      });
  }
  
ngOnDestroy(): void {
    this.dataSubscription.unsubscribe();
  }
}
```

La dernière étape consiste à afficher les données du CMS en utilisant la directive Angular `ngFor` pour parcourir les éléments et les rendre.

```html
<header>
    <h2>Pack and Go</h2>
</header>
<main class="main">
    <div class="card" *ngFor="let poi of pointsOfInterest">
        <h2 class="title">{{poi.title.value}}</h2>
        <div class="content" innerHTML="{{poi.description.value}}"></div>
        <a class="map-link" target="_blank" href="http://maps.google.com/?ie=UTF8&amp;hq=&amp;ll={{poi.latitude__decimal_degrees_.value}},{{poi.longitude__decimal_degrees_.value}}&amp;z=16">
           Open the map
        </a>
    </div>
</main>
```

#### Permettre l'ajout d'une icône de raccourci

Maintenant, nous allons rendre l'application capable d'ajouter son icône sur le bureau ou l'écran d'accueil de l'appareil.

![Image](https://cdn-media-1.freecodecamp.org/images/hDtH-KcbAIVk8hyusfrbGV8JaHEd--pLYSbk)

Cette étape est assez simple. Elle nécessite de créer un fichier JSON contenant des métadonnées sur l'application et de le lier à partir de la balise `head`. Le fichier manifest doit pointer vers plusieurs URL d'icônes de différentes tailles.

Nous devons également lister le fichier `manifest.json` dans une déclaration d'assets dans le fichier de configuration `.angular-cli.json`.

```json
{
    ...
    apps: {
        assets : [
            ...,
            "manifest.json"
        ],
        ...
    },
    ...
}
```

Mais, plus important encore, liez le fichier `manifest.json` à partir de `index.html`.

```html
<link rel="manifest" href="manifest.json" />
```

Enfin, nous allons créer le manifest lui-même, ainsi que toutes les versions des icônes. Jetez un œil au lien ci-dessous pour voir le résultat.

![Image](https://cdn-media-1.freecodecamp.org/images/jmtJk-647gvGgq-bdjB3ssca-qbgo2QbmR8p)
_[Lien vers le commit avec les données.](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/abb80401d8775c608b5e554e17da2f7ef1437a42" rel="noopener" target="_blank" title=")_

#### Configurer le service worker

Le concept du service worker est ce qui rend les applications PWA révolutionnaires.

Les service workers fonctionnent comme un proxy entre le client et Internet. Selon la configuration réelle, le service worker peut pré-mettre en cache le squelette de l'application (appelé « app shell ») lors du premier chargement. Cela signifie que les requêtes suivantes sont ultra-rapides. Le service worker peut également mettre en cache silencieusement toutes les autres données de l'application.

Tout d'abord, il est nécessaire d'installer le module de service worker dans l'application.

```bash
npm install -P @angular/service-worker
```

Maintenant, activez le service worker dans Angular dans le fichier de configuration `.angular-cli.json`.

```json
{
    ...
    apps: {
        "serviceWorker": true,
        ...
    },
    ...
}
```

Maintenant, importons le module de service worker dans notre application en utilisant le fichier `app.module.ts`.

```ts
...
import { ServiceWorkerModule } from '@angular/service-worker';
...
@NgModule({
  ...
  imports: [
    ...
    ServiceWorkerModule.register('/ngsw-worker.js', { enabled: environment.production })
  ],
  ...
})
...
```

La dernière chose est de configurer les stratégies de mise en cache pour l'app shell et les données. Tout d'abord, nous devons créer le fichier de configuration `ngsw-config.json` sous le dossier `/src`.

Pour l'app shell, nous utiliserons la configuration par défaut décrite dans la [documentation](https://angular.io/guide/service-worker-getting-started#step-4-create-the-configuration-file-ngsw-configjson). Cette configuration pré-chargera `index.html`, le `favicon.ico`, et l'app shell, y compris les bundles CSS et JavaScript liés. Les fichiers dans le dossier `/assets` sont chargés de manière paresseuse.

Les requêtes de données de Kentico Cloud utiliseront une autre stratégie de mise en cache. Nous définirons un point de terminaison API comme un nouveau [groupe de données](https://angular.io/guide/service-worker-config#datagroups) et configurerons la mise en cache pour utiliser la stratégie de [fraîcheur](https://angular.io/guide/service-worker-config#strategy). Dans le lien de commit ci-dessous, vous pouvez voir le contenu complet du fichier de configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/-fdiGKoHlYE2tkUjOZiS7V89pT0d1jjedLkc)
_[Lien vers le commit](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/6a5f2b3230f04901c51573124bafce4bd31672e4" rel="noopener" target="_blank" title=")_

Maintenant, nous sommes prêts à installer l'application sur l'appareil. Par exemple, dans Chrome sur Android, vous pouvez le faire en appuyant sur le glyphe ellipsis et en choisissant « Ajouter à l'écran d'accueil ».

![Image](https://cdn-media-1.freecodecamp.org/images/NLmY5ZkuUm8267AT-VfDutcekoSzFp6uhGuO)

Très bien, nous avons terminé. Malgré une mise en œuvre rapide et simple, l'application est assez puissante et rapide. Et nous sommes libres de l'étendre de diverses manières, comme importer le design matériel ou les icônes de police.

Les API PWA nous permettent également d'utiliser des fonctionnalités natives intéressantes telles que :

* lire les capteurs de l'appareil
* afficher des notifications push
* et utiliser les caméras de l'appareil.

Notre application pourrait également détecter lorsque l'appareil passe de en ligne à hors ligne, et vice versa. Nous pourrions également utiliser les [modèles de contenu générés automatiquement et fortement typés](https://www.npmjs.com/package/kentico-cloud-model-generator-utility) du CMS.

Comme vous pouvez le voir, créer une PWA dans Angular est facile, mais permet d'étendre l'application beaucoup plus loin.