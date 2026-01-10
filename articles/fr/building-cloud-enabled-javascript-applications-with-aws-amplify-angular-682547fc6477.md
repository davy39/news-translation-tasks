---
title: Comment utiliser AWS Amplify et Angular pour créer des applications JavaScript
  compatibles avec le cloud
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-24T21:01:47.000Z'
originalURL: https://freecodecamp.org/news/building-cloud-enabled-javascript-applications-with-aws-amplify-angular-682547fc6477
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EB-8t3dR5qMQYNXyqgM2wQ.png
tags:
- name: Angular
  slug: angular
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: serverless
  slug: serverless
- name: Web Development
  slug: web-development
seo_title: Comment utiliser AWS Amplify et Angular pour créer des applications JavaScript
  compatibles avec le cloud
seo_desc: 'By Nader Dabit

  AWS Amplify helps you add functionality like storage, GraphQL, authentication, analytics,
  pub-sub, and internationalization to your JavaScript applications.

  While you can integrate AWS Amplify into any JavaScript framework, Angular com...'
---

Par Nader Dabit

[AWS Amplify](https://aws.github.io/aws-amplify/?utm_source=blog&utm_campaign=amplify_angular_medium_nader) vous aide à ajouter des fonctionnalités telles que le stockage, GraphQL, l'authentification, l'analyse, pub-sub et l'internationalisation à vos applications JavaScript.

Bien que vous puissiez intégrer AWS Amplify dans _n'importe quel_ framework JavaScript, des composants Angular ont récemment été ajoutés, ce qui facilite plus que jamais l'utilisation des services cloud dans une application Angular.

Dans cet article, nous allons voir comment démarrer avec AWS Amplify dans une application Angular.

### Installation

#### Installation des dépendances

Pour commencer, nous devons installer quelques dépendances : AWS Amplify et AWS Amplify Angular :

```bash
$ npm install --save aws-amplify
$ npm install --save aws-amplify-angular
```

#### Création d'un nouveau projet AWS Mobile

Si vous avez déjà un projet AWS que vous souhaitez utiliser, vous pouvez ignorer cette étape. Sinon, vous apprendrez comment utiliser AWS Mobile Hub pour rapidement démarrer avec des services AWS comme Amazon Cognito pour l'authentification, Amazon Pinpoint pour l'analyse, AWS AppSync pour GraphQL géré, et Amazon S3 pour le stockage.

La prochaine chose à faire ici est d'installer l'AWS Mobile CLI :

```bash
npm i -g awsmobile-cli
```

Ensuite, nous devons configurer l'AWS Mobile CLI pour utiliser vos identifiants IAM préférés.

> Si vous êtes nouveau sur AWS et souhaitez voir comment configurer cela pour la première fois, consultez [cette](https://www.youtube.com/watch?v=MpugaNKtw3k) vidéo.

```bash
awsmobile configure
```

Maintenant, notre AWS Mobile CLI est prêt à l'emploi et nous pouvons créer un nouveau projet.

Créons un nouveau projet avec l'analyse, le stockage et l'authentification activés :

```bash
awsmobile init

awsmobile user-signin enable
awsmobile user-files enable
awsmobile push
```

Après avoir créé votre backend, le fichier de configuration est copié dans `/awsmobilejs/#current-backend`

#### Visualisation de votre projet dans la console AWS

Maintenant que vous avez créé votre projet à partir de la CLI, vous pouvez visualiser votre projet dans AWS Mobile Hub en visitant [https://console.aws.amazon.com/mobilehub/home](https://console.aws.amazon.com/mobilehub/home?region=us-east-1) et en cliquant sur le nom de votre projet.

### Travailler avec Angular

Pour importer le fichier de configuration dans votre application Angular, vous devez renommer `aws_exports.js` en `aws_exports.ts`.

Pour importer le fichier de configuration dans votre application Angular, vous devez renommer `aws_exports.js` en `aws_exports.ts`.

```js
import Amplify from 'aws-amplify'
import awsmobile from './aws-exports'
Amplify.configure(aws_exports)
```

Lorsque vous travaillez avec le `aws-js-sdk` sous-jacent, le package « node » doit être inclus dans l'option de compilation _types_. Assurez-vous de modifier le fichier `tsconfig.app.json` dans votre dossier de fichiers source, par exemple `_src/tsconfig.app.json_`.

```json
"compilerOptions": {
  "types" : ["node"]
}
```

#### Importation d'Amplify

Dans votre [module racine](https://angular.io/guide/bootstrapping) `src/app/app.module.ts`, vous pouvez importer les modules AWS Amplify comme suit :

```ts
import { AmplifyAngularModule, AmplifyService } from 'aws-amplify-angular'

@NgModule({
  ...
  imports: [
    ...
    AmplifyAngularModule
  ],
  ...
  providers: [
    ...
    AmplifyService
  ]
  ...
})
```

> Le fournisseur de service est facultatif. Vous pouvez importer les catégories principales normalement, par exemple `import { Analytics } from 'aws-amplify'` ou créer votre propre fournisseur. Le fournisseur de service effectue certaines tâches pour vous et expose les catégories en tant que méthodes. Le fournisseur gère également et distribue les changements d'état d'authentification en utilisant des observables auxquels vous pouvez vous abonner dans vos composants (voir ci-dessous).

#### Utilisation du service AWS Amplify

AmplifyService est un fournisseur dans votre application Angular, et il fournit les catégories principales d'AWS Amplify via l'injection de dépendances.

Pour utiliser _AmplifyService_ avec [l'injection de dépendances](https://angular.io/guide/dependency-injection-in-action), injectez-le dans le constructeur de n'importe quel composant ou service, n'importe où dans votre application.

```ts
import { AmplifyService } from 'aws-amplify-angular';

...
constructor(
    public navCtrl:NavController,
    public amplifyService: AmplifyService,
    public modalCtrl: ModalController
) {
    this.amplifyService = amplifyService;
}
...
```

#### Utilisation des catégories AWS Amplify

Vous pouvez accéder et travailler directement avec les catégories AWS Amplify via le fournisseur de service intégré :

```ts
import { Component } from '@angular/core';
import { AmplifyService }  from 'aws-amplify-angular';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  
  constructor( public amplify:AmplifyService ) {
      
      this.amplifyService = amplify;

      /** maintenant vous pouvez accéder aux API de catégorie :
       * this.amplifyService.auth();          // Authentification AWS Amplify
       * this.amplifyService.analytics();     // Analyse AWS Amplify
       * this.amplifyService.storage();       // Stockage AWS Amplify
       * this.amplifyService.api();           // API AWS Amplify
       * this.amplifyService.cache();         // Cache AWS Amplify
       * this.amplifyService.pubsub();        // PubSub AWS Amplify
     **/
  }
  
}
```

#### Exemple d'utilisation : S'abonner aux changements d'état d'authentification

Importez AmplifyService dans votre composant et écoutez les changements d'état d'authentification :

```ts
import { AmplifyService }  from 'aws-amplify-angular';

  // ...
constructor( public amplifyService: AmplifyService ) {

    this.amplifyService = amplifyService;

    this.amplifyService.authStateChange$
        .subscribe(authState => {
        this.signedIn = authState.state === 'signedIn';
        if (!authState.user) {
            this.user = null;
        } else {
            this.user = authState.user;
            this.greeting = "Bonjour " + this.user.username;
        }
        });

}
```

#### Composants de vue

AWS Amplify fournit également des composants que vous pouvez utiliser dans vos modèles de vue Angular, y compris un composant d'authentification, un composant de sélection de photo et un composant d'album Amazon S3.

**Authentificateur**

Le composant Authentificateur crée une expérience de connexion/inscription clé en main pour votre application Angular. Pour utiliser Authentificateur, ajoutez simplement la directive `amplify-authenticator` dans votre vue .html :

```ts
<amplify-authenticator></amplify-authenticator>
```

**Sélecteur de photo**

Le composant Sélecteur de photo affichera un contrôle de téléchargement de fichier qui permettra de choisir une image locale et de la télécharger sur Amazon S3. Une fois qu'une image est sélectionnée, un aperçu de l'image encodé en base64 sera affiché automatiquement.

Pour afficher le sélecteur de photo dans une vue Angular, utilisez le composant _`amplify-photo-picker`_ :

```ts
<amplify-photo-picker 
    (picked)="onImagePicked($event)"
    (loaded)="onImageLoaded($event)">
</amplify-photo-picker>
```

Le composant émettra deux événements :

* `(picked)` - Émis lorsqu'une image est sélectionnée. L'événement contiendra l'objet `File` qui peut être utilisé pour le téléchargement.
* `(loaded)` - Émis lorsqu'un aperçu de l'image a été rendu et affiché.

**Téléchargement d'une image**

Utilisez `onImagePicked(event)` pour télécharger votre photo sur Amazon S3 en utilisant la catégorie Stockage AWS Amplify :

```ts
onImagePicked( file ) {

    let key = `pics/${file.name}`;
    
    this.amplify.storage().put( key, file, {
      'level': 'private',
      'contentType': file.type
    })
    .then (result => console.log('téléchargé : ', result))
    .catch(err => console.log('erreur de téléchargement : ', err));
  
}
```

#### Album S3

Le composant Album Amazon S3 affiche une liste d'images du bucket S3 connecté.

Pour afficher l'album, utilisez le composant `_amplify-s3-album_` dans votre vue Angular :

```ts
<amplify-s3-album
  path="pics" (selected)="onAlbumImageSelected($event)"
>
</amplify-s3-album>
```

L'événement `(selected)` peut être utilisé pour récupérer l'URL de l'image cliquée dans la liste :

```ts
onAlbumImageSelected( event ) {
      window.open( event, '_blank' );
}
```

**Styles personnalisés**

Vous pouvez utiliser des styles personnalisés pour les composants AWS Amplify. Il suffit d'importer votre fichier _styles.css_ personnalisé qui remplace les styles par défaut que vous pouvez trouver dans `/node_modules/aws-amplify-angular/theme.css`.

### Conclusion

AWS Amplify est open source et en développement actif, et nous aimerions recevoir des retours et/ou des problèmes de la part des clients ou des utilisateurs pour nous aider dans notre feuille de route future.

N'hésitez pas à consulter la documentation [ici](https://aws.github.io/aws-amplify/), ou le dépôt GitHub [ici](https://github.com/aws/aws-amplify).

Je m'appelle [Nader Dabit](https://twitter.com/dabit3). Je suis un Developer Advocate chez [AWS Mobile](https://aws.amazon.com/mobile/) travaillant sur des projets comme [AWS AppSync](https://aws.amazon.com/appsync/) et [AWS Amplify](https://aws.github.io/aws-amplify/?utm_source=blog&utm_campaign=amplify_angular_medium_nader), et le fondateur de [React Native Training](http://reactnative.training/).