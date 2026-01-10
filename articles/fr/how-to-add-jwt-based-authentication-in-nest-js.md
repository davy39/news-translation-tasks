---
title: Comment ajouter l'authentification basée sur JWT dans NestJS
subtitle: ''
author: Abimbola Adedotun Samuel
co_authors: []
series: null
date: '2024-07-31T14:33:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-jwt-based-authentication-in-nest-js
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/nest-auth-coverimage-1.png
tags:
- name: authentication
  slug: authentication
- name: JWT
  slug: jwt
- name: nestjs
  slug: nestjs
seo_title: Comment ajouter l'authentification basée sur JWT dans NestJS
seo_desc: 'Authentication is a very important aspect of software development. It is
  the process of verifying a user’s identity.

  Authentication ensures that only authorized individuals access specific resources
  or perform certain actions within a system. It prov...'
---

L'authentification est un aspect très important du développement logiciel. C'est le processus de vérification de l'identité d'un utilisateur.

L'authentification garantit que seules les personnes autorisées accèdent à des ressources spécifiques ou effectuent certaines actions au sein d'un système. Elle assure la responsabilité en permettant le suivi des actions des utilisateurs et en tenant les individus responsables de leurs activités.

Elle fournit également aux entreprises des données sur le nombre de personnes utilisant leurs produits. Sans une authentification appropriée de votre logiciel, vous pourriez rencontrer des risques de sécurité. Une mise en œuvre correcte empêche l'accès non autorisé et protège les données sensibles.

Ce tutoriel vous guidera à travers la création d'une authentification utilisateur basée sur JWT dans NestJS et MongoDb.

NestJS est un framework Node.js puissant pour construire des applications côté serveur. MongoDB est une base de données NoSQL populaire et nous l'utiliserons pour construire les endpoints d'authentification de base.

Dans ce tutoriel, nous aborderons les sujets suivants :

- Comment créer un nouveau projet NestJS et installer les dépendances nécessaires.
- Comment créer des modèles et des schémas d'utilisateurs.
- Comment implémenter la connexion et l'inscription avec un jeton JWT.
- Comment tester les endpoints avec Postman.

## **Prérequis**

Ce tutoriel est une démonstration pratique. Pour suivre, vous devez avoir les éléments suivants :

- [<u>Node.js</u>](https://nodejs.org/en/download/package-manager) v14 et supérieur

- Gestionnaire de paquets Node

- [<u>MongoDB Compass</u>](https://www.mongodb.com/docs/compass/current/install/)

- Compréhension de base de Node.js et de préférence ExpressJs

- Un éditeur de code (par exemple : VS Code)

## **Comment configurer le projet.**

Dans cette section, nous allons configurer le projet pour construire notre API REST avec NestJS et MongoDB. Nous commencerons par installer le CLI NestJS et l'utiliser pour générer de nouveaux projets.

Installez [<u>Nest CLI</u>](https://docs.nestjs.com/cli/overview) :

`$ npm i -g @nestjs/cli`

Ensuite, créez un nouveau projet NestJS avec cette commande :

`$ nest new project-name`

Appelons le projet authentication :

`$ nest new authentication`

Vous verrez des options concernant le gestionnaire de paquets que vous préférez installer. J'ai utilisé npm.

Après une installation réussie, déplacez-vous dans le répertoire créé et ouvrez le projet avec votre éditeur de code préféré.

Avant de créer des ressources et de configurer le projet, prenons un rapide aperçu du répertoire **src** et de ses fichiers :

- `src` : Le répertoire racine pour le code source.

- `src/app.module.ts` : Le module principal de l'application pour configurer et intégrer d'autres modules.

- `src/app.controller.ts` : Contient un contrôleur par défaut avec une seule route.

- `src/app.service.ts` : Cela inclut un service de base utilisant une seule méthode.

- `src/main.ts` : Le point d'entrée de l'application.

Ensuite, installez les dépendances pour configurer et connecter la base de données. Vous devrez installer le package `mongoose`, `bcrypt` :

`$ npm i -save @nestjs/mongoose @types/bcrypt mongoose bcrypt`

![dépendances installées avec succès](https://www.freecodecamp.org/news/content/images/2024/07/image3.png)

Ensuite, configurez votre base de données. Le `MongooseModule` de la dépendance `@nestjs/mongoose` sera utilisé pour configurer la base de données.

Allez dans le fichier `src/app.module.ts` :

```js
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { MongooseModule } from '@nestjs/mongoose';
import { UsersModule } from './users/users.module';
import { AuthModule } from './auth/auth.module';
import { ConfigModule } from '@nestjs/config';

@Module({
imports: [
MongooseModule.forRoot('mongodb://localhost:27017/auth-workshop'),
UsersModule,
AuthModule,
ConfigModule.forRoot({
envFilePath: '.env',
isGlobal: true,
}),
],
controllers: [AppController],
providers: [AppService],
})
export class AppModule {}
```

Analysons le code ci-dessus.
Le `app.module.ts` est le module racine de l'application nestjs et il est responsable de l'importation des dépendances et d'autres modules requis par l'application, de la configuration de l'application telle que les connexions de base de données et les variables d'environnement.

Nous avons d'abord spécifié le fichier `app.module.ts` comme un module en utilisant le décorateur `@Module({})` :

```js
@Module({})
```

Le tableau `imports` spécifie le module dont ce module dépend. Nous avons le `MongooseModule.forRoot('')` pour la connexion à la base de données en utilisant mongoose, l'import `ConfigModule.forRoot` configure le module de configuration pour lire à partir d'un fichier `.env` :

```js
import { MongooseModule } from '@nestjs/mongoose';
import { UsersModule } from './users/users.module';
import { AuthModule } from './auth/auth.module';
import { ConfigModule } from '@nestjs/config';

imports: [
MongooseModule.forRoot('mongodb://localhost:27017/auth-workshop'),
UsersModule,
AuthModule,
ConfigModule.forRoot({
envFilePath: '.env',
isGlobal: true,
}),
]
```
Vous pouvez remplacer la chaîne URI `MongooseModule.forRoot()` par votre propre chaîne de base de données.

Le tableau `controllers` spécifie le contrôleur qui appartient à ce module :
```js
controllers: [AppController]
```

Le tableau `providers` spécifie les services qui appartiennent à ce module :
```js
providers: [AppService]
```

Avec ces configurations, vous pouvez démarrer votre application en utilisant `npm run start:dev`.

## **Modèles et schémas d'utilisateurs**

Dans cette section, nous allons définir le modèle `User` et le schéma en utilisant `mongoose`. Le modèle `User` représentera les utilisateurs de l'application, et le schéma définira la structure des données stockées dans MongoDB.
Commençons par créer un module de ressource pour l'API des utilisateurs :

Tout d'abord, créez une ressource `users` avec le CLI nest :

`$ nest generate res users`

Cette commande créera une nouvelle ressource `users` dans le répertoire **src/users** avec une structure de base de contrôleurs et de services.

Ensuite, définissez le schéma pour les `Users` dans **src/users/entities/users.entity.ts** :

```js
import { Prop, Schema, SchemaFactory }
from '@nestjs/mongoose';
@Schema()
export class User {
@Prop()
name: string;
@Prop({ unique: true })
email: string;

@Prop()
password: string;
}
export const UserSchema = SchemaFactory.createForClass(User);
```

Le décorateur `@Schema` est ce qui fait de la classe un schéma. Ce schéma définit trois champs pour les utilisateurs : `name`, `email` et `password`. Ils sont tous de type chaîne.

Ensuite, enregistrez le schéma dans le fichier `users.module.ts` situé dans **src/users/users.module.ts** :

```js
import { Module } from '@nestjs/common';
import { UsersService } from './users.service';
import { UsersController } from './users.controller';
import { MongooseModule } from '@nestjs/mongoose';
import { UserSchema, User } from './entities/user.entity';

@Module({
imports: [MongooseModule.forFeature([{ name: User.name, schema:
UserSchema }])],
controllers: [UsersController],
providers: [UsersService],
})
export class UsersModule {}
```

En important le `MongooseModule.forFeature([{}])`, cela configure mongoose pour utiliser le `UserSchema` pour le modèle `User`.

En enregistrant le schéma avec Mongoose, nous avons créé un modèle prêt à être utilisé dans notre application. Cela prépare le terrain pour la construction de services et de contrôleurs qui peuvent interagir avec nos données et gérer les requêtes entrantes.

Enfin, définissez le DTO (objet de transfert de données). Cet objet transfère des données entre les systèmes. C'est un objet simple qui ne contient que des données et n'a pas de comportement.

Créez votre `CreateUserDto` dans le répertoire **src/users/dto/create-user.dto.ts** :

```js
export class CreateUserDto {
username: string;
email: string;
password: string;
}
```

## **Services et contrôleurs d'utilisateurs**

Nous nous sommes connectés à la base de données et avons créé le schéma et le modèle des `Users`. Écrivons les méthodes CRUD de base pour les utilisateurs.

Mettez à jour votre **users.service.ts** situé dans **src/users/users.service.ts** :

```js
import { Injectable, NotFoundException
} from '@nestjs/common';
import { CreateUserDto } from './dto/create-user.dto';
import { UpdateUserDto } from './dto/update-user.dto';
import { InjectModel } from '@nestjs/mongoose';
import { User } from './entities/user.entity';
import { Model } from 'mongoose';

@Injectable()
export class UsersService {
constructor(@InjectModel(User.name) private userModel:
Model<User>) {}
async createUsers(createUserDto: CreateUserDto) {
const user = await this.userModel.create(createUserDto);
return user.save();
}
async findAllUsers() {
const users = this.userModel.find();
return users;
}
async findUser(id: number) {
const user = await this.userModel.findById(id);
if (!user) throw new NotFoundException('could not find the user');
return user;
}
updateUser(id: number, updateUserDto: UpdateUserDto) {
return this.userModel.findByIdAndUpdate(id, updateUserDto, { new: true
});
}
removeUser(id: number) {
return this.userModel.findByIdAndDelete(id);
};
}

```

Mettez à jour votre **users.controller.ts** situé dans **src/users/users.controller.ts** :

```js
import { Controller, Get, Post, Body, Patch, Param, Delete, } from '@nestjs/common';
import { UsersService } from './users.service';
import { CreateUserDto } from './dto/create-user.dto';
import { UpdateUserDto } from './dto/update-user.dto';

@Controller('users')
export class UsersController {
constructor(private readonly usersService: UsersService) {}

@Post()
async create(@Body() createUserDto: CreateUserDto) {
return await this.usersService.createUsers(createUserDto);
}

@Get()
async findAll() {
return await this.usersService.findAllUsers();
}

@Get(':id')
async findOne(@Param('id') id: string) {
return await this.usersService.findOneUser(+id);
}

@Patch(':id')
async update(@Param('id') id: string, @Body() updateUserDto:
UpdateUserDto) {
return await this.usersService.updateUser(+id, updateUserDto);
}

@Delete(':id')
async remove(@Param('id') id: string) {
return await this.usersService.removeUser(+id);
}
}
```

Nous avons créé des API RESTful en utilisant `mongoose`. Les méthodes incluent :

- `findAllUsers` : Récupère tous les documents utilisateur de la collection.

- `getUserById` : Trouve un seul document utilisateur par ID.

- `createUsers` : Ajoute un nouveau document utilisateur à la collection.

- `updateUser` : Met à jour les détails de l'utilisateur existant dans la collection.

- `removeUser` : Supprime le document utilisateur par ID.

## **Comment implémenter l'inscription et la connexion**

Dans cette section, nous allons créer un service d'authentification qui génère des JSON Web Tokens (JWT).

Ce service aura deux méthodes : `signup` et `login`. La méthode `signup` prendra un objet de requête d'inscription contenant `name`, `email` et `password`, et la méthode `login` prendra un objet de requête de connexion contenant `email` et `password`. Les deux méthodes retourneront un JWT.

Commençons par créer un module de ressource pour les API d'authentification.

Créez une ressource `auth` avec Nest CLI :

`$ nest generate res auth`


Ensuite, définissez le DTO pour l'inscription et la connexion. Allez dans le dossier **dto** dans le dossier **src/auth/dto** :

**signup.dto.ts** :

```js
export class SignUpDto {
name: string;
email: string;
password: string;
}
```

**login.dto.ts** :

```js
export class Login {
email: string;
password: string;
}
```

Ensuite, créez un fichier **.env** dans le répertoire racine :

```env
JWT_SECRET=secret
JWT_EXPIRES=3d
```

Ensuite, ajoutez le `PassportModule`, `JwtModule` et `JwtStrategy` à `AuthModule`. Nous commencerons par installer ces packages :

`$ npm i @nestjs/passport @nestjs/jwt passport passport-jwt bcryptjs`

Allez dans **src/auth/auth.module.ts** et importez ces packages :

```js
import { Module } from '@nestjs/common';
import { AuthService } from './auth.service';
import { AuthController } from './auth.controller';
import { PassportModule } from '@nestjs/passport';
import { JwtModule } from '@nestjs/jwt';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { MongooseModule } from '@nestjs/mongoose';
import { UserSchema } from 'src/users/entities/user.entity';


@Module({
imports: [
PassportModule.register({ defaultStrategy: 'jwt' }),
JwtModule.registerAsync({
imports: [ConfigModule],
inject: [ConfigService],
useFactory: (config: ConfigService) => {
return {
secret: config.get<string>('JWT_SECRET'),
signOptions: {
expiresIn: config.get<string | number>('JWT_EXPIRES'),
},
};
},
}),
MongooseModule.forFeature([{ name: 'User', schema: UserSchema }]),
],
controllers: [AuthController],
providers: [AuthService],
})
export class AuthModule {}

```

Le `PassportModule.register` configure le module Passport pour utiliser la stratégie JWT comme mécanisme d'authentification.

Le `JwtModule.registerAsync` configure le module JWT en utilisant un processus d'enregistrement asynchrone, tel que le temps d'expiration du jeton.

Le `MongooseModule.forFeature()` configure mongoose pour utiliser le `UserSchema` pour le modèle `User`.

Ces imports permettent au module d'authentification de gérer l'authentification des utilisateurs, la génération de JWT et l'interaction avec la base de données.

Ensuite, créez les `AuthServices` pour l'inscription et la connexion dans le répertoire **src/auth/auth.service.ts** :

```js
import { Injectable, UnauthorizedException} from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { User } from 'src/users/entities/user.entity';
import { SignUpDto } from './dto/signup.dto';
import * as bcrypt from 'bcryptjs';
import { LoginDto } from './dto/login.dto';
import { ConfigService } from '@nestjs/config';

@Injectable()
export class AuthService {
constructor(
@InjectModel(User.name) private userModel: Model<User>,
private jwtService: JwtService,
private configService: ConfigService,
) {}

async signUp(signupDto: SignUpDto) {
const { name, email, password } = signupDto;

const hashedPassword = await bcrypt.hash(password, 10);
const user = await this.userModel.create({
name,
email,
password: hashedPassword,
});

await user.save();

const token = await this.jwtService.sign(
{ id: user.id },
{
secret: this.configService.get('JWT_SECRET'),
expiresIn: this.configService.get('JWT_EXPIRES'),
},
);
return { token };
}

async login(loginDto: LoginDto) {
const { email, password } = loginDto;
const user = await this.userModel.findOne({
email,
});

if (!user) throw new UnauthorizedException('invalid email or
password');
const passwordMatch = await bcrypt.compare(password,
user.password);
if (!passwordMatch)
throw new UnauthorizedException('invalid email or password');
const token = await this.jwtService.sign(
{ id: user.id },
{
secret: this.configService.get('JWT_SECRET'),
},
);
return { token };
}
}
```

Dans le `AuthService`, la méthode `signUp` facilite l'enregistrement des utilisateurs en :

- Déstructurant l'objet `SignupDto` pour extraire les informations d'identification de l'utilisateur.
- Hachant le mot de passe en utilisant `bcrypt` pour un stockage sécurisé.
- Créant un nouveau document utilisateur dans la base de données via le `userModel`.
- Enregistrant le document utilisateur dans la base de données.
- Générant un jeton JWT en utilisant `jwtService` lors de l'enregistrement réussi.
- Retournant le jeton JWT au client.

La méthode `login` authentifie les utilisateurs en :

- Déstructurant l'objet `LoginDto` pour vérifier les informations d'identification de l'utilisateur.
- Comparant le mot de passe saisi avec le hachage stocké pour garantir une correspondance.
- Lancant une erreur `UnauthorizedException` si les mots de passe ne correspondent pas.
- Utilisant le `jwtService` pour signer l'utilisateur et générer un jeton JWT lors de l'authentification réussie.
- Retournant le jeton JWT au client.


Mettez à jour le `AuthController` pour l'inscription et la connexion dans le répertoire **src/auth/auth.controller.ts** :

```js
import { Controller, Post, Body } from '@nestjs/common';
import { AuthService } from './auth.service';
import { SignUpDto } from './dto/signup.dto';
import { LoginDto } from './dto/login.dto';

@Controller('auth')
export class AuthController {
constructor(private readonly authService: AuthService) {}

@Post('signup')
signUp(@Body() signupDto: SignUpDto) {
return this.authService.signUp(signupDto);
}

@Post('login')
signin(@Body() loginDto: LoginDto) {
return this.authService.login(loginDto);
}
}

```

Avec ces étapes, vous avez implémenté une connexion et une inscription de base dans votre application. Dans les sections suivantes, nous testerons les routes `login` et `signup`.

## **Test dans Postman**

Maintenant que nous avons configuré nos endpoints, il est temps de les tester. Pour cet exemple, j'utiliserai Postman comme client API, mais n'hésitez pas à utiliser tout outil ou client qui convient à vos besoins. Voyons notre API en action !

### **Comment créer un utilisateur avec l'endpoint `/signup` :**

![test d'inscription postman](https://www.freecodecamp.org/news/content/images/2024/07/image4-1.png)

Après avoir envoyé une requête POST à l'endpoint /signup en utilisant Postman, nous avons reçu une réponse contenant l'accessToken. Vous pouvez vérifier qu'un nouvel utilisateur a été créé avec succès en vérifiant la base de données.

![vérification de l'inscription mongodb compass](https://www.freecodecamp.org/news/content/images/2024/07/image1.png)

### **Se connecter en tant qu'utilisateur existant avec l'endpoint `/login` :**

![test de connexion postman](https://www.freecodecamp.org/news/content/images/2024/07/image2-1.png)

## **Conclusion**

Félicitations, vous avez implémenté avec succès une authentification complète en utilisant NestJS, Mongoose et Passport. Nous avons conçu un processus d'inscription et de connexion sécurisé, et généré des JSON Web Tokens (JWT).

Pour améliorer et élargir vos connaissances sur l'authentification, explorez l'autorisation, la protection des routes avec un middleware d'authentification, et la mise en œuvre de la vérification par e-mail et de la fonctionnalité de réinitialisation du mot de passe.

Cette base fournit un point de départ solide pour construire un système d'authentification robuste et évolutif. Ce projet a été un plaisir à travailler, et j'espère que vous l'avez trouvé tout aussi agréable.

Pour votre commodité, le dépôt du projet est disponible sur Github [<u>repository is available on Github</u>](https://github.com/dotun2203/basic-nest-authentication).

N'hésitez pas à me contacter sur Twitter à [<u>@Adedot1Abimbola</u>](https://x.com/Adedot1Abimbola?t=2A7m7RbbIzJei3rrjxsVuA&s=09). J'aimerais avoir de vos nouvelles.