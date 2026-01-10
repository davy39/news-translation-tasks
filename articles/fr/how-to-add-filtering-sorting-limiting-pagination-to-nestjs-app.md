---
title: Comment ajouter le filtrage, le tri, la limitation et la pagination à votre
  application Nest.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-02-05T19:01:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-filtering-sorting-limiting-pagination-to-nestjs-app
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/nestjs-app-image.png
tags:
- name: api
  slug: api
- name: MongoDB
  slug: mongodb
- name: nestjs
  slug: nestjs
seo_title: Comment ajouter le filtrage, le tri, la limitation et la pagination à votre
  application Nest.js
seo_desc: "By Okure U. Edet\nIf you are reading this article, you are probably a developer\
  \ who has used an API to call data for your application. You may have also used\
  \ features such as filtering and pagination to limit the amount of data you want\
  \ to receive. \nT..."
---

Par Okure U. Edet

Si vous lisez cet article, vous êtes probablement un développeur qui a utilisé une API pour appeler des données pour votre application. Vous avez peut-être également utilisé des fonctionnalités telles que le filtrage et la pagination pour limiter la quantité de données que vous souhaitez recevoir. 

Ces fonctionnalités d'API sont importantes lors de la création de votre propre API. Elles aident à garantir que votre API est rapide, sécurisée et facilement compréhensible par les personnes qui l'utilisent.

Dans cet article, vous allez créer une API de dépenses simple avec Nest.js et MongoDB pour une base de données. Vous implémenterez ensuite le filtrage, le tri, la limitation et la pagination pour rendre votre API plus rapide et facile à utiliser. Commençons !

### Voici ce que nous allons couvrir :

* [Qu'est-ce qu'une API ?](#heading-quest-ce-quune-api)
* [Comment configurer une application Nest.js](#heading-comment-configurer-une-application-nestjs)
* [Comment configurer MongoDB](#heading-comment-configurer-mongodb)
* [Comment configurer les endpoints de dépenses](#heading-comment-configurer-les-endpoints-de-depenses)
* [Comment implémenter le filtrage et le tri](#heading-comment-implementer-le-filtrage-et-le-tri)
* [Comment implémenter la limitation et la pagination](#heading-comment-implementer-la-limitation-et-la-pagination)
* [Conclusion](#heading-conclusion)

## Qu'est-ce qu'une API ?

Les API sont la colonne vertébrale du développement logiciel moderne. API signifie Application Programming Interface, et elle permet à un logiciel de communiquer avec un autre logiciel. 

Les API web utilisent les protocoles de communication HTTP pour communiquer avec les ordinateurs. Il existe différents types d'API, mais nous n'entrerons pas dans les détails ici.

De nos jours, il est courant que les API web aient des fonctionnalités de conception telles que le filtrage, le tri, la limitation et la pagination pour rendre l'API plus rapide, plus facile à utiliser et plus sécurisée. Vous apprendrez comment implémenter ces fonctionnalités pour créer une meilleure API dans cet article.

## Comment configurer une application Nest.js

Tout d'abord, vous allez créer une API CRUD de dépenses simple dans Nestjs. Nestjs est un framework Node.js progressif pour construire des API modernes qui est assez facile à utiliser.

Pour commencer, ouvrez votre ligne de commande et tapez les commandes suivantes :

```
$ npm i -g @nestjs/cli
$ nest new expense-app
```

Suivez le guide d'installation. Cela générera quelques fichiers de base pour vous. Ensuite, vous pouvez ouvrir votre application Nest.js dans un IDE de votre choix.

## Comment configurer MongoDB

Puisque MongoDB est notre base de données préférée, il est important de la configurer pour pouvoir l'utiliser dans votre application. Tout d'abord, installez le package `@nestjs/mongoose` :

```
$ npm i @nestjs/mongoose mongoose
```

Une fois l'installation terminée, allez dans votre fichier de module d'application et importez le `MongooseModule` :

```
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { MongooseModule } from '@nestjs/mongoose';

@Module({
  imports: [MongooseModule.forRoot(`mongodb+srv://*******:*******@cluster0.30vt0jd.mongodb.net/expense-test-app`)],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

Si vous ne voulez pas exposer votre chaîne de cette manière, vous pouvez créer un fichier `.env` et y stocker votre chaîne de connexion à la base de données. Vous devrez ensuite installer le package `@nestjs/config` qui utilise dotenv en interne. 

À l'intérieur de votre fichier de module d'application, importez le `ConfigModule` :

```
@Module({
  imports: [
    ConfigModule.forRoot({ envFilePath: '.env', isGlobal: true }),
    MongooseModule.forRoot(process.env.DATABASE),
  ],
  controllers: [AppController],
  providers: [AppService],
})
```

`isGlobal: true` est pour rendre le module disponible partout dans votre application. `envFilePath` spécifie le chemin vers votre fichier `.env`.

## Comment configurer les endpoints de dépenses

Vous avez configuré MongoDB. Il est maintenant temps de configurer les endpoints de dépenses. 

Vous pouvez créer un module dans Nest.js en tapant ce qui suit dans le terminal : `nest generate module expenses`. Vous pouvez également générer le contrôleur comme ceci : `nest generate controller expenses` et le service comme ceci : `nest generate service expenses`. Vous devez faire tout cela dans le dossier src. 

Allez-y et générez un fichier expenses.schema.ts. À l'intérieur du fichier expenses.schema.ts, créez un schéma de dépenses avec une validation.

```
import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import mongoose, { HydratedDocument } from 'mongoose';

export type ExpenseDocument = HydratedDocument<Expense>;

@Schema()
export class Expense {
  @Prop({
    trim: true,
    required: [true, 'Le titre est requis'],
  })
  title: string;

  @Prop({
    min: 0,
    required: [true, 'Le montant est requis'],
  })
  amount: number;

  @Prop({
    type: String,
    trim: true,
    required: [true, 'La catégorie est requise'],
  })
  category: string;

  @Prop({
    type: Date,
    default: Date.now,
  })
  incurred: Date;

  @Prop({ type: String, trim: true })
  notes: string;

  @Prop()
  slug: string;

  @Prop()
  updated: Date;

  @Prop({
    type: Date,
    default: Date.now,
  })
  created: Date;
}

export const ExpenseSchema = SchemaFactory.createForClass(Expense);
```

Les propriétés de ce schéma incluent le titre, le montant, la catégorie, les notes et le slug.

Après avoir fait cela, vous voulez enregistrer le modèle de dépenses dans le fichier expenses.module.ts :

```
import { Module } from '@nestjs/common';
import { ExpensesController } from './expenses.controller';
import { ExpensesService } from './expenses.service';
import { MongooseModule } from '@nestjs/mongoose';
import { Expense, ExpenseSchema } from './expenses.schema';

@Module({
  imports: [
    MongooseModule.forFeature([{ name: Expense.name, schema: ExpenseSchema }]),
  ],
  controllers: [ExpensesController],
  providers: [ExpensesService],
})
export class ExpensesModule {}
```

Une fois que vous avez enregistré le schéma, vous pouvez alors injecter le modèle `Expense` dans le `ExpensesService` en utilisant un décorateur `@InjectModel()`.

```
import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Expense } from './expenses.schema';
import { Model } from 'mongoose';
import { ExpenseDto } from './dto/expense.dto';

@Injectable()
export class ExpensesService {
  constructor(
    @InjectModel(Expense.name) private expenseModel: Model<Expense>,
  ) {}

  async createExpense(data: ExpenseDto) {
    const expense = this.expenseModel.create(data);

    return expense;
  }

  async getExpenses() {
    const expenses = await this.expenseModel.find();

    return expenses;
  }
}
```

Dans le fichier `ExpensesService`, nous avons injecté le modèle `Expense` en tant que dépendance en utilisant le décorateur `@InjectModel()`. Une fois que vous avez fait cela, vous pouvez ensuite définir une fonction qui crée une dépense et une fonction qui obtient toutes les dépenses.

Dans votre contrôleur, ajoutez le code suivant :

```
import { Body, Controller, Get, Post, Res } from '@nestjs/common';
import { ExpensesService } from './expenses.service';
import { ExpenseDto } from './dto/expense.dto';

@Controller('expenses')
export class ExpensesController {
  constructor(private readonly expenseService: ExpensesService) {}

  @Post()
  async createExpense(@Body() data: ExpenseDto, @Res() response: any) {
    const expense = await this.expenseService.createExpense(data);
    console.log(expense);

    return response.status(201).json({
      message: 'succès',
      data: expense,
    });
  }

  @Get()
  async getExpenses(@Res() response: any) {
    const expenses = await this.expenseService.getExpenses();

    return response.status(200).json({
      message: 'succès',
      data: expenses,
    });
  }
}
```

Si vous obtenez une erreur de dépendance, naviguez vers votre fichier `app.module.ts` et retirez `ExpenseController` du tableau `controllers`.

Vous pouvez tester l'endpoint sur Postman.

## Comment implémenter le filtrage et le tri

Maintenant que vous avez configuré avec succès les endpoints de dépenses, il est temps d'implémenter les fonctionnalités de filtrage et de tri dans l'API.

### Filtrage

Le filtrage est essentiellement fait de la même manière que nous le faisons dans Node.js.

À l'intérieur de votre répertoire src, créez un nouveau dossier appelé `Utils` et à l'intérieur de ce dossier créez un nouveau fichier appelé `apiFeatures.ts`.

À l'intérieur de ce fichier, définissez une classe appelée `APIFeatures`. Cette classe contiendra des méthodes qui hébergeront les fonctionnalités de l'API que vous allez implémenter.

```
export class APIFeatures {
  mongooseQuery: any;
  queryString: any;

  constructor(mongooseQuery: any, queryString: any) {
    this.mongooseQuery = mongooseQuery;
    this.queryString = queryString;
  }

  filter() {
    // 1) Filtrage
    const queryObj = { ...this.queryString };
    const excludedFields = ['page', 'sort', 'limit', 'fields'];
    excludedFields.forEach((fields) => {
      delete queryObj[fields];
    });
    // console.log(queryObj);

    //2) Filtrage avancé
    let queryStr = JSON.stringify(queryObj);
    queryStr = queryStr.replace(/\b(gte|gt|lte|lt)\b/g, (match) => `$${match}`);
    //console.log(JSON.parse(queryStr));

    this.mongooseQuery = this.mongooseQuery.find(JSON.parse(queryStr));

    return this;
  }
}
```

Dans la méthode de filtrage, vous avez créé une copie exacte de `req.query`. Elle est passée en argument sous la forme de `queryString`. 

Avant de filtrer, vous voulez exclure certains champs spéciaux tels que `page`, `sort`, `limits` et `fields`. Ces champs sont supprimés de la copie exacte de l'objet qui est stockée dans la variable `queryObj`. Vous voulez également utiliser des opérateurs MongoDB tels que `gt` ou `gte`.

Par exemple, sur Postman, voici comment vous tapez la requête : `?amount[gt]=100`
Dans MongoDB, cela ressemblera à ceci : `{ amount: { $gt: 100 } }`. Dans la méthode de filtrage, nous avons ajouté un signe `$` aux opérateurs en utilisant une expression régulière.

Après cela, l'objet est analysé en utilisant la méthode `JSON.parse()` et il est ensuite passé dans la fonction de requête Mongoose. Assurez-vous de retourner la classe elle-même en tapant `return this`.

### Tri

Comme vous pouvez le voir, l'implémentation du filtrage est assez facile dans Nest.js comme dans Node.js.

Il est maintenant temps d'implémenter le tri. À l'intérieur de la classe `APIFeatures`, définissez une autre fonction appelée sorting.

```
  sorting() {
    if (this.queryString.sort) {
      const sortBy = this.queryString.sort.split(',').join(' ');
      // console.log(sortBy);
      this.mongooseQuery = this.mongooseQuery.sort(sortBy);
    } else {
      this.mongooseQuery = this.mongooseQuery.sort('-created');
    }

    return this;
  }
```

La méthode ci-dessus vérifie si une propriété de tri existe sur l'objet de requête. Si c'est le cas, vous divisez la chaîne par une `,` au cas où il y aurait plusieurs requêtes de tri. Ensuite, vous la joignez par un `' '`. 

Une fois que vous avez fait cela, vous l'enchaînez à la requête Mongoose avec une méthode de tri qui existe sur tous les documents. Le bloc else trie le document par la date à laquelle il a été créé au cas où l'utilisateur ne spécifie aucune requête de tri.


## Comment implémenter la limitation et la pagination

Félicitations ! Vous avez implémenté le filtrage et le tri. Il est maintenant temps d'implémenter la limitation et la pagination.

### Limitation

Pour limiter les champs, vous pouvez appeler la méthode `select()` sur la requête Mongoose.

Définissez une autre méthode dans la classe :

```
 limit() {
    if (this.queryString.fields) {
      const fields = this.queryString.fields.split(',').join(' ');

      this.mongooseQuery = this.mongooseQuery.select(fields);
    } else {
      this.mongooseQuery = this.mongooseQuery.select('-__v');
    }

    return this;
  }
```

Et voilà.

### Pagination

Pour implémenter la pagination, vous voulez obtenir la `page` et la `limite` de l'objet de requête. Vous voulez ensuite sauter un certain nombre de documents pour atteindre la page que vous voulez. Il existe une méthode `skip()` et une méthode `limit()` sur la requête Mongoose.

```
  pagination() {
    // obtenir la page et la convertir en nombre. Si aucune page n'est définie, la valeur par défaut est 1
    const page = this.queryString.page * 1 || 1;

    // obtenir la limite et si aucune limite n'est définie, définir la limite à 100
    const limit = this.queryString.limit * 1 || 100;

    // calculer la valeur de saut
    const skip = (page - 1) * limit;

    // l'enchaîner à la requête mongoose.
    this.mongooseQuery = this.mongooseQuery.skip(skip).limit(limit);

    // retourner l'objet
    return this;
  }
```

Une fois que vous avez fait cela, vous voulez appeler la classe `APIfeatures` dans votre classe `ExpensesService` dans votre fichier expenses.service.ts.

Remplacez votre fonction `getExpenses` par ce code :

```
 async getExpenses(query?: any) {
    const features = new APIFeatures(this.expenseModel.find(), query)
      .filter()
      .sort()
      .limit()
      .pagination();
    //Exécuter la requête
    const expenses = await features.mongooseQuery;

    return expenses;
  }
```

Dans la fonction, il est possible d'enchaîner toutes ces méthodes dans la classe `APIFeatures` car chaque méthode retourne l'objet.

Dans votre fichier expenses.controller.ts, votre fonction `getExpenses` devrait ressembler à ceci :

```
  @Get()
  async getExpenses(@Res() response: any, @Req() request: any) {
    const expenses = await this.expenseService.getExpenses(request.query);

    return response.status(200).json({
      message: 'succès',
      data: expenses,
    });
  }
```

Maintenant, exécutez l'application avec `npm start:dev` et testez les fonctionnalités de votre API dans Postman.


## Conclusion

Dans ce guide, vous avez appris comment implémenter le tri, le filtrage, la limitation et la pagination dans vos applications Nest.js. 

Avec cette connaissance, vous pouvez aller de l'avant et implémenter ces fonctionnalités dans vos projets personnels construits en utilisant Nest.js.