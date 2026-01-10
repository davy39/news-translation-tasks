---
title: Comment créer une application Electron avec Angular et SQLite3.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-15T03:44:08.000Z'
originalURL: https://freecodecamp.org/news/creating-an-electron-app-using-angular-and-sqlite3-24ca7d892810
coverImage: https://cdn-media-1.freecodecamp.org/images/0*fYvEL90t63nfj3Nb
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: Comment créer une application Electron avec Angular et SQLite3.
seo_desc: 'By William Boxx

  I was recently experimenting with converting one of my Angular web apps into a desktop
  application using Electron. I encountered a few hurdles along the way, and decided
  to put my experience in writing so that it may help others. If y...'
---

Par William Boxx

J'ai récemment expérimenté la conversion de l'une de mes applications web Angular en une application de bureau en utilisant Electron. J'ai rencontré quelques obstacles en cours de route et j'ai décidé de mettre mon expérience par écrit afin qu'elle puisse aider les autres. Si vous avez des plans similaires pour votre projet, j'espère que cela pourra être utile. Le code source de ce guide peut être trouvé [ici](https://github.com/wboxx1/typescript-electron-angular6-sqlite3).

### Partie I : Angular

#### Créer le Boilerplate.

Pour les besoins de ce guide, nous allons créer une nouvelle application Angular à partir de zéro. J'utiliserai [Electron-Forge](https://electronforge.io/) pour créer le boilerplate. Electron-Forge offre plusieurs [modèles](https://electronforge.io/templates) pour créer du code boilerplate, y compris un pour Angular 2. Installez d'abord le CLI Electron-Forge.

```
$ npm i -g electron-forge
```

Utilisez maintenant le CLI pour créer le boilerplate de l'application Angular.

```
$ electron-forge init electron-angular-sqlite3 --template=angular2
$ cd electron-angular-sqlite3
```

Le CLI forge ajoutera les éléments essentiels dont nous avons besoin pour exécuter notre application. Ajoutons quelques répertoires supplémentaires pour héberger nos fichiers de base de données. Ajoutez un répertoire assets sous src, et mettez les répertoires data et model sous celui-ci.

```
$ mkdir ./src/assets/data ./src/assets/model
```

L'arborescence des répertoires devrait maintenant ressembler à ceci :

```
.
+-node_modules
+-src
|  |
|  +-assets
|  |  |
|  |  +-data
|  |  +-model
|  |
|  +-app.component.ts
|  +-bootstrap.ts
|  +-index.html
|  +-index.ts
|
+-.compilerc
+-.gitignore
+-package-lock.json
+-package.json
+-tsconfig.json
+-tslint.json
```

#### Écrire du Code.

En tant que première étape, ajoutons un fichier de modèle que nous allons faire correspondre à notre schéma de base de données. Pour cet exemple simple, créons une classe appelée Item. Chaque élément contiendra un id et une propriété name. Enregistrez le fichier dans votre projet à `src/assets/model/item.schema.ts`.

Nous allons utiliser T[ypeORM](http://typeorm.io/#/) pour notre mapping relationnel objet. Installez d'abord TypeORM.

```
$ npm install typeorm --save
```

Nous allons suivre le [guide](http://typeorm.io/#/undefined/step-by-step-guide) de TypeORM pour créer un schéma ici. Une fois terminé, le fichier devrait ressembler à ceci :

```ts
import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity()
export class Item
{
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	name: string;
}
```

TypeORM utilise les [décorateurs](https://www.typescriptlang.org/docs/handbook/decorators.html) de TypeScript. Nous utilisons le décorateur Entity pour déclarer notre classe Item comme une table. Le décorateur `@PrimaryGeneratedColumn()` déclare `id` comme notre identification unique et indique à la base de données de le générer automatiquement. Nous nous préoccuperons de la liaison à une base de données plus tard.

#### Créer le Service.

Notre prochaine action probable serait de créer un service d'application qui gère la communication entre le front-end et le back-end. Electron met à disposition la classe `IpcRenderer` pour cela. `IpcRenderer` est la [classe de communication inter-processus](https://electronjs.org/docs/api/ipc-main) d'Electron qui est utilisée dans le processus de rendu. Basiquement, nous voulons utiliser `IpcRenderer` pour envoyer des messages au processus principal d'Electron. Ces messages transmettront des informations au processus principal afin qu'il puisse gérer les interactions avec la base de données.

L'implémentation de `IpcRenderer` est là où nous rencontrons notre premier obstacle. Electron repose sur la méthode window.require(), qui n'est disponible qu'à l'intérieur du processus de rendu d'Electron. C'est un problème bien documenté [ici](https://github.com/electron/electron/issues/7300). Pour contourner cela, nous pouvons utiliser le package [ngx-electron de ThornstonHans](https://github.com/ThorstenHans/ngx-electron), qui enveloppe toutes les API d'Electron exposées au processus de rendu dans un seul service Electron. Vous pouvez en lire plus à ce sujet [ici](https://thorsten-hans.com/integrating-angular-and-electron-using-ngx-electron-9c36affca25e).

Avant de pouvoir utiliser `ngx-electron`, nous devons l'installer.

```
$ npm install ngx-electron --save
```

Maintenant, créons un service pour gérer notre communication `IpcRenderer`. Créez `src/app.service.ts`.

```ts
import { Injectable } from '@angular/core';

import { Item } from './assets/model/item.schema';

import { ElectronService } from 'ngx-electron';
import { Observable } from 'rxjs/observable';
import { of } from 'rxjs/observable/of';
import { catchError } from 'rxjs/operators';

@Injectable()
export class AppService {
  constructor(private _electronService: ElectronService) {}

  getItems(): Observable<Item[]> {
    return of(this._electronService.ipcRenderer.sendSync('get-items')).pipe(
      catchError((error: any) => Observable.throw(error.json))
    );
  }

  addItem(item: Item): Observable<Item[]> {
    return of(
      this._electronService.ipcRenderer.sendSync('add-item', item)
    ).pipe(catchError((error: any) => Observable.throw(error.json)));
  }

  deleteItem(item: Item): Observable<Item[]> {
    return of(
      this._electronService.ipcRenderer.sendSync('delete-item', item)
    ).pipe(catchError((error: any) => Observable.throw(error.json)));
  }
}
```

Dans `app.service.ts`, nous créons une classe appelée `AppService` et ajoutons le décorateur `@Injectable()`. Cela nous permet d'utiliser l'injection de dépendances (DI) intégrée d'Angular. Dans notre constructeur, nous créons une variable locale `_electronService` de type `ElectronService`. La classe `ElectronService` nous est fournie par `ngrx-electron`. Elle nous permet d'utiliser la classe `IpcRender` d'Electron sans aucun des problèmes mentionnés précédemment.

Nous créons trois fonctions : une qui obtient tous les Items dans la base de données, une pour ajouter un Item à la base de données, et une pour supprimer un Item. Chaque fonction retournera un Observable.

Les Observables font partie de la [bibliothèque RxJs](https://angular.io/guide/rx-library) et fournissent un bon moyen de gérer nos interactions avec la base de données de manière asynchrone. Vous pouvez en lire plus sur les Observables [ici](https://angular.io/guide/observables). Notez l'utilisation de l'opérateur Observable `of` pour indiquer que nous enveloppons notre réponse de `this._electronService.ipcRenderer.sendSync()` comme une valeur Observable.

#### Enregistrement des Services et Écriture du Composant.

Avec notre service terminé, allons dans `src/app.component.ts` et enregistrons-le pour DI. Pendant que nous y sommes, nous ajouterons un simple modèle html et des fonctions pour gérer nos événements de bouton.

```ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { Component, OnInit } from '@angular/core';

import { Item } from './assets/model/item.schema';
import { AppService } from './app.service';
import { ElectronService } from 'ngx-electron';

@Component({
  selector: 'App',
  template: `<div style="text-align:center">
    <h1>
        Bienvenue dans {{ title }}!
    </h1>
    <button (click)="addItem()" mat-raised-button>Ajouter un Item</button>
    <button (click)="deleteItem()" mat-raised-button>Supprimer un Item</button>
    <h2>Voici le contenu de la base de données : </h2>
    <div>
        <ul style="list-style: none">
            <li *ngFor="let item of itemList">
                {{ item.name }}
            </li>
        </ul>
    </div>
</div>`,
})
export class AppComponent implements OnInit {
  public readonly title = 'mon application';
  itemList: Item[];

  constructor(private appservice: AppService) {}

  ngOnInit(): void {
    console.log('composant initialisé');
    this.appservice.getItems().subscribe((items) => (this.itemList = items));
  }

  addItem(): void {
    let item = new Item();
    item.name = 'Item ' + this.itemList.length;
    this.appservice.addItem(item).subscribe((items) => (this.itemList = items));
  }

  deleteItem(): void {
    const item = this.itemList[this.itemList.length - 1];
    this.appservice
      .deleteItem(item)
      .subscribe((items) => (this.itemList = items));
  }
}

@NgModule({
  imports: [ BrowserModule ],
  declarations: [ AppComponent ],
  bootstrap: [ AppComponent ],
  providers: [ AppService, ElectronService ],
})
export class AppModule {}
```

Assurez-vous d'ajouter `AppService` en tant que fournisseur dans les arguments du décorateur `@NgModule` et également en tant que variable privée dans le constructeur `AppComponent`. Nous devons également ajouter `ElectronService` en tant que fournisseur.

Lors de l'initialisation de notre composant, nous voulons charger tout le contenu de notre base de données et l'afficher. Pour ce faire, nous nous abonnons à la fonction `addItem()` du service que nous avons créé. Si vous vous souvenez, toutes nos fonctions de service retournent des Observables. Pour obtenir des données de notre observable, nous nous y abonnons, en passant une fonction de rappel qui s'exécute lorsque les données sont reçues. Dans l'exemple ci-dessus, `(items) => (this.itemList = items)` remplira notre variable de classe `itemList` avec le contenu de la base de données une fois qu'il est récupéré.

Nous suivons des tactiques similaires pour ajouter et supprimer des éléments de la base de données. Chaque fois, nous repeuplons `itemList` avec le contenu mis à jour de la base de données.

### Partie II : Electron

#### Installation de SQLite3.

Maintenant que nous avons terminé notre front-end, nous devons créer le back-end Electron. Le back-end Electron gérera et traitera les messages envoyés depuis le front-end et gérera la base de données sqlite3.

Nous allons utiliser sqlite3 pour notre base de données et nous devons l'installer.

```
$ npm install sqlite3 --save
```

Un obstacle que j'ai rencontré en travaillant avec sqlite3 et Electron initialement, était que les binaires natifs de sqlite devaient être recompilés pour une utilisation avec Electron. Electron-Forge devrait s'en charger pour vous. Une chose à noter, Electron-Forge utilisera [node-gyp](https://www.npmjs.com/package/node-gyp) pour compiler les binaires. Vous devrez peut-être l'avoir correctement installé et configuré avant de l'utiliser, ce qui inclut l'installation de Python. À ce jour, node-gyp utilise python 2. Si vous avez plusieurs versions sur votre machine, vous devez vous assurer que la version actuelle utilise la bonne.

#### Connexion à la Base de Données.

Maintenant, ouvrons notre fichier `src/index.ts` et ajoutons du code pour nous connecter à la base de données. Les deux choses que nous devons faire sont : nous connecter à la base de données et ajouter des fonctions pour gérer nos requêtes depuis le processus de rendu. Le fichier terminé ressemble à ceci :

```ts
import { app, BrowserWindow, ipcMain } from 'electron';
import { enableLiveReload } from 'electron-compile';

import { createConnection } from 'typeorm';

import { Item } from './assets/model/item.schema';

// Gardez une référence globale de l'objet window, si vous ne le faites pas, la fenêtre sera
// fermée automatiquement lorsque l'objet JavaScript sera garbage collecté.
let mainWindow: Electron.BrowserWindow | null;

const isDevMode = process.execPath.match(/[\\/]electron/);

if (isDevMode) enableLiveReload();

const createWindow = async () => {
  const connection = await createConnection({
    type: 'sqlite',
    synchronize: true,
    logging: true,
    logger: 'simple-console',
    database: './src/assets/data/database.sqlite',
    entities: [ Item ],
  });

  const itemRepo = connection.getRepository(Item);

  // Créez la fenêtre du navigateur.
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
  });

  // et chargez le index.html de l'application.
  mainWindow.loadURL(`file://${__dirname}/index.html`);

  // Ouvrez les DevTools.
  if (isDevMode) {
    mainWindow.webContents.openDevTools();
  }

  // Émis lorsque la fenêtre est fermée.
  mainWindow.on('closed', () => {
    // Déréférencez l'objet window, généralement vous stockeriez les fenêtres
    // dans un tableau si votre application supporte plusieurs fenêtres, c'est le moment
    // où vous devriez supprimer l'élément correspondant.
    mainWindow = null;
  });

  ipcMain.on('get-items', async (event: any, ...args: any[]) => {
    try {
      event.returnValue = await itemRepo.find();
    } catch (err) {
      throw err;
    }
  });

  ipcMain.on('add-item', async (event: any, _item: Item) => {
    try {
      const item = await itemRepo.create(_item);
      await itemRepo.save(item);
      event.returnValue = await itemRepo.find();
    } catch (err) {
      throw err;
    }
  });

  ipcMain.on('delete-item', async (event: any, _item: Item) => {
    try {
      const item = await itemRepo.create(_item);
      await itemRepo.remove(item);
      event.returnValue = await itemRepo.find();
    } catch (err) {
      throw err;
    }
  });
};

// Cette méthode sera appelée lorsque Electron aura terminé
// l'initialisation et sera prêt à créer des fenêtres de navigateur.
// Certaines API ne peuvent être utilisées qu'après cet événement.
app.on('ready', createWindow);

// Quittez lorsque toutes les fenêtres sont fermées.
app.on('window-all-closed', () => {
  // Sur OS X, il est courant pour les applications et leur barre de menu
  // de rester actives jusqu'à ce que l'utilisateur quitte explicitement avec Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  // Sur OS X, il est courant de recréer une fenêtre dans l'application lorsque
  // l'icône du dock est cliquée et qu'il n'y a pas d'autres fenêtres ouvertes.
  if (mainWindow === null) {
    createWindow();
  }
});

// Dans ce fichier, vous pouvez inclure le reste du code spécifique du processus principal de votre application
// Vous pouvez également les mettre dans des fichiers séparés et les importer ici.
```

Une explication approfondie de TypeORM et Electron dépasse le cadre de ce guide, donc je ne discuterai que brièvement du fichier ci-dessus. Tout d'abord, nous devons importer la classe `createConnection` de la bibliothèque TypeORM. Nous devons également importer notre schéma Item.

Comme prévu, la classe `createConnection` créera une connexion à notre base de données. Nous lui passons un constructeur avec des paramètres tels que type, database et entities. Type est une chaîne qui décrit le type de base de données que nous utilisons. Database est une chaîne qui pointe vers l'emplacement de la base de données. Entities est l'endroit où nous disons à TypeORM quels schémas attendre. Pour notre usage : type est 'sqlite', Database est './src/assets/data/database.sqlite', et Entities est notre classe Item importée.

TypeORM vous offre deux options lors de la gestion des transactions de base de données : [EntityManager](http://typeorm.io/#/working-with-entity-manager) et [Repository](http://typeorm.io/#/working-with-repository). Les deux vous donneront accès à des fonctions pour interroger la base de données, sans écrire le SQL. Nous créons un objet Repository avec la ligne `itemRepo = connection.getRepository(Item)`. Cela nous donne accès aux méthodes de transaction pour notre table Item.

La dernière étape consiste à créer des fonctions pour gérer les messages envoyés depuis le `IpcRenderer`. Chaque fonction utilisera l'objet `itemRepo` que nous avons créé pour accéder à la base de données. Après l'achèvement réussi de chaque transaction, les fonctions passeront le nouvel état de la base de données au processus de rendu.

### Partie III : Exécutez-le !

Avec tout terminé, nous pouvons maintenant exécuter l'application. Electron-Forge gère ce processus pour nous. Tout ce que nous avons à faire est d'exécuter la commande :

```
$ npm run start
```

Si tout est correct, Electron ouvrira votre application et vous pourrez la tester.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rZLZdXtOGnUANw3jByRz6g.gif)

Merci d'avoir lu !