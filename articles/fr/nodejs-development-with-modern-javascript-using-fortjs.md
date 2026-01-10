---
title: Développement Node.js avec JavaScript moderne en utilisant FortJs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-23T02:37:44.000Z'
originalURL: https://freecodecamp.org/news/nodejs-development-with-modern-javascript-using-fortjs
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-from-2019-10-20-20-36-31-1.png
tags:
- name: dependency injection
  slug: dependency-injection
- name: ES6
  slug: es6
- name: Node.js
  slug: nodejs
- name: REST
  slug: rest
- name: TypeScript
  slug: typescript
seo_title: Développement Node.js avec JavaScript moderne en utilisant FortJs
seo_desc: 'By Ujjwal Gupta

  Introduction

  Nodejs gives you the power to write server side code using JavaScript. In fact,
  it is very easy and fast to create a web server using Nodejs. There are several
  frameworks available on Node package manager which makes the ...'
---

Par Ujjwal Gupta

## Introduction

Node.js vous donne le pouvoir d'écrire du code côté serveur en utilisant JavaScript. En fait, il est très facile et rapide de créer un serveur web en utilisant Node.js. Il existe plusieurs frameworks disponibles sur le gestionnaire de paquets Node qui rendent le développement encore plus facile et rapide.

Mais il y a quelques défis dans le développement Node.js :

* Node.js est tout au sujet des callbacks, et avec de plus en plus de callbacks, vous vous retrouvez dans une situation appelée l'enfer des callbacks.
* Écrire du code lisible.
* Écrire du code maintenable.
* Vous n'obtenez pas beaucoup de support d'intellisense, ce qui rend le développement lent.

Si vous êtes assez expérimenté et avez une bonne connaissance de Node.js, vous pouvez utiliser différentes techniques et essayer de minimiser ces défis.

La meilleure façon de résoudre ces problèmes est d'utiliser JavaScript moderne ES6, ES7 ou TypeScript, selon ce avec quoi vous êtes à l'aise. Je recommande TypeScript, car il fournit un support d'intellisense pour chaque mot de code, ce qui rend votre développement plus rapide.

J'ai donc créé un framework appelé [FortJs](http://fortjs.info/) qui est très facile à apprendre et à utiliser. FortJs vous permet d'écrire du code côté serveur en utilisant ES6 ou TypeScript qui est modulaire, sécurisé, et assez joli et lisible.

## Fonctionnalités

Quelques-unes des fonctionnalités importantes de FortJs sont :

* Basé sur l'architecture [Fort](https://github.com/ujjwalguptaofficial/fort).
* Framework MVC et suit l'approche OOPS, donc tout est classe et objet.
* Fournit des composants - Wall, Shield et Guard. Les composants aident à modulariser l'application.
* Utilise ES6 async/await ou promise pour exécuter du code asynchrone.
* Tout est configurable - vous pouvez configurer votre stockage de session, moteur de vue, websocket, etc.
* Injection de dépendances.
* Tout peut être testé unitairement, donc vous pouvez utiliser une approche [TDD](https://guide.freecodecamp.org/agile/test-driven-development/).

## Codons

Dans cet article, je vais créer une API REST en utilisant FortJs et ES6. Mais vous pouvez utiliser le même code et les mêmes étapes pour implémenter en utilisant TypeScript également.

### Installation du projet

FortJs fournit un CLI - fort-creator. Cela vous aide à configurer le projet et à développer plus rapidement. Utilisons le CLI pour développer.

Effectuez les étapes suivantes séquentiellement :

* Ouvrez votre terminal ou invite de commande.
* Installez **fort-creator** globalement - exécutez la commande "npm i fort-creator -g". Note : Assurez-vous que Node.js est installé dans votre système.
* Créez un nouveau projet - exécutez la commande "fort-creator new my-app". Ici, "my-app" est le nom de l'application, donc vous pouvez choisir n'importe quel nom. Le CLI vous demandera de choisir la langue avec deux options : TypeScript et JavaScript. Choisissez votre langue en utilisant les touches fléchées et appuyez sur entrée - j'ai choisi JavaScript. Cela prendra un certain temps pour créer le projet, donc veuillez attendre jusqu'à ce que vous voyiez "new project my-app created".
* Entrez dans le répertoire du projet - "cd my-app".
* Démarrez le serveur de développement avec rechargement en direct - exécutez la commande "fort-creator start".
* Ouvrez le navigateur et tapez l'URL - [http://localhost:4000/](http://localhost:4000/).

Vous devriez voir quelque chose comme ceci dans le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-from-2019-10-20-20-36-31.png)
_Page de démarrage de FortJs_

Comprenons comment cette page est rendue :

* Ouvrez le dossier du projet dans votre éditeur de code préféré. Je vais utiliser VS Code. Vous verrez de nombreux dossiers à la racine du projet tels que controllers, views, etc. Chaque dossier est regroupé par leur utilisation - par exemple, le dossier controllers contient tous les contrôleurs et le dossier views contient toutes les vues.
* Ouvrez le dossier controllers -> À l'intérieur des contrôleurs, vous verrez un fichier nommé - default_controller. Ouvrons-le et observons le code. Le fichier contient une classe DefaultController - il s'agit d'une classe [controller](http://fortjs.info/tutorial/controller/) et elle contient des méthodes qui retournent une réponse http.
* À l'intérieur de la classe DefaultController, vous verrez une méthode 'index' - c'est celle qui rend le résultat actuel dans le navigateur. La méthode est connue sous le nom de [worker](http://fortjs.info/tutorial/worker/) dans FortJs car elles effectuent un certain type de travail et retournent le résultat sous forme de réponse http. Observons le code de la méthode index :

```
const data = {
    title: title
}
const result = await viewResult('default/index.html', data);
return result;
```

Il crée un objet de données et passe cet objet dans la méthode **viewResult**. La méthode **viewResult** prend deux paramètres - l'emplacement de la vue et les données de la vue. Le travail de **viewResult** est de rendre la vue et de retourner une réponse, que nous voyons dans le navigateur.

* Trouvons le code de la vue et comprenons-le. Ouvrez le dossier views -> ouvrez le dossier default -> ouvrez index.html. Il s'agit de notre code de vue. Il s'agit d'un code HTML simple avec une syntaxe mustache. Le moteur de vue par défaut pour FortJs est mustache.

J'espère que vous avez compris l'architecture du projet. Si vous avez des difficultés ou des doutes, n'hésitez pas à demander dans la section des commentaires.

Maintenant, nous allons passer à la partie suivante de cet article où nous apprendrons comment créer une simple API REST.

## REST

Nous allons créer un endpoint REST pour l'entité user - qui effectuera des opérations CRUD pour l'utilisateur telles que l'ajout d'un utilisateur, la suppression d'un utilisateur, l'obtention d'un utilisateur et la mise à jour d'un utilisateur.

Selon REST :

1. Ajouter un utilisateur - doit être fait en utilisant la méthode http "`POST`"
2. Supprimer un utilisateur - doit être fait en utilisant la méthode http "`REMOVE`"
3. Obtenir un utilisateur - doit être fait en utilisant la méthode http "`GET`"
4. Mettre à jour un utilisateur - doit être fait en utilisant la méthode http "`PUT`"

Pour créer un endpoint, nous devons créer un Controller similaire au contrôleur par défaut expliqué précédemment.

Exécutez la commande "`fort-creator add`". Il vous demandera "Choose the component to add ?" Choisissez Controller & appuyez sur **enter**. Entrez le nom du contrôleur "User" et appuyez sur **enter**. 

Maintenant que nous avons créé le contrôleur utilisateur, nous devons informer FortJs en l'ajoutant aux routes. La route est utilisée pour mapper notre contrôleur à un chemin.

Puisque notre entité est user, "`/user`" sera une bonne route. Ajoutons-la. Ouvrez routes.js à l'intérieur du répertoire racine du projet et ajoutez `UserController` aux routes.

Après avoir ajouté UserController, routes.js ressemblera à ceci :

```javascript
import { DefaultController } from "./controllers/default_controller";
import { UserController } from "./controllers/user_controller";

export const routes = [{
    path: "/*",
    controller: DefaultController
},
{
    path: "/user",
    controller: UserController
}]
```

Donc, lorsqu'une requête http a le chemin "/user", alors UserController sera appelé.

Ouvrons l'URL - [http://localhost:4000/user](http://localhost:4000/user).

Note : Si vous avez arrêté FortJs lors de l'ajout du contrôleur, veuillez le redémarrer en exécutant la commande - `fort-creator start`

Et vous voyez une page blanche, n'est-ce pas ?

C'est parce que nous ne retournons rien depuis la méthode index et ainsi nous obtenons une réponse vide. Retourons un texte "Hello World" depuis la méthode index. Ajoutez le code ci-dessous à l'intérieur de la méthode index et sauvegardez :

```javascript
return textResult('Hello World');
```

Actualisez l'URL - [http://localhost:4000/user](http://localhost:4000/user)

Et vous voyez "Hello World", n'est-ce pas ?

Maintenant, convertissons "UserController" en une API REST. Mais avant d'écrire le code pour l'API REST, créons un service factice qui effectuera des opérations CRUD pour les utilisateurs.

### Service

Créez un dossier appelé "services" et ensuite un fichier "user_service.js" à l'intérieur du dossier. Collez le code ci-dessous à l'intérieur du fichier :

```javascript
const store = {
    users: [{
        id: 1,
        name: "ujjwal",
        address: "Bangalore India",
        emailId: "ujjwal@mg.com",
        gender: "male",
        password: "admin"
    }]
}

export class UserService {
    getUsers() {
        return store.users;
    }

    addUser(user) {
        const lastUser = store.users[store.users.length - 1];
        user.id = lastUser == null ? 1 : lastUser.id + 1;
        store.users.push(user);
        return user;
    }

    updateUser(user) {
        const existingUser = store.users.find(qry => qry.id === user.id);
        if (existingUser != null) {
            existingUser.name = user.name;
            existingUser.address = user.address;
            existingUser.gender = user.gender;
            existingUser.emailId = user.emailId;
            return true;
        }
        return false;
    }

    getUser(id) {
        return store.users.find(user => user.id === id);
    }

    removeUser(id) {
        const index = store.users.findIndex(user => user.id === id);
        store.users.splice(index, 1);
    }
}
```

Le code ci-dessus contient une variable store qui contient une collection d'utilisateurs. La méthode à l'intérieur du service effectue des opérations comme ajouter, mettre à jour, supprimer et obtenir sur ce store.

Nous utiliserons ce service dans l'implémentation de l'API REST.

### GET

Pour la route "/user" avec la méthode http "GET", l'API doit retourner une liste de tous les utilisateurs.

Afin de l'implémenter, renommons la méthode "index" à l'intérieur de user_controller.js en "getUsers" pour la rendre sémantiquement correcte. Ensuite, collez le code ci-dessous à l'intérieur de la méthode :

```javascript
const service = new UserService();
return jsonResult(service.getUsers());
```

Maintenant, user_controller.js ressemble à ceci :

```javascript

import { Controller, DefaultWorker, Worker, textResult, jsonResult } from "fortjs";
import { UserService } from "../services/user_service";

export class UserController extends Controller {

    @DefaultWorker()
    async getUsers() {
        const service = new UserService();
        return jsonResult(service.getUsers());
    }
}
```

Ici, nous utilisons le décorateur DefaultWorker. Le DefaultWorker fait deux choses : il ajoute la route "/" & la méthode http "GET". C'est un raccourci pour ce scénario. Dans la partie suivante, nous utiliserons d'autres décorateurs pour personnaliser la route.

Testons cela en appelant l'URL [http://localhost:4000/user](http://localhost:4000/user). Vous pouvez l'ouvrir dans le navigateur ou utiliser des outils clients http comme postman ou curl.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-from-2019-10-20-21-53-59.png)

Ok, nous avons donc créé avec succès un endpoint :) .

Regardons à nouveau notre code et voyons si nous pouvons l'améliorer :

1. Le service "UserService" est étroitement couplé avec le Controller "UserController", ce qui devient un problème pour les tests unitaires "UserController". Nous allons donc utiliser [l'injection de dépendances](http://fortjs.info/tutorial/dependency-injection/) de FortJs pour injecter UserService.
2. Nous créons une instance de "UserService" chaque fois que la méthode getUsers est appelée. Mais ce dont nous avons besoin de "UserService" est un seul objet, puis nous appelons la méthode "UserService" à partir de l'objet.

Donc, si nous pouvons stocker un objet de "UserService", nous pouvons rendre notre code plus rapide (car l'appel de new fait un certain travail en arrière-plan). Pour cela, nous allons utiliser la fonctionnalité singleton de FortJs.

Changeons le code de user_controller.js par le code ci-dessous :

```javascript

import { Controller, DefaultWorker, Worker, textResult, jsonResult, Singleton } from "fortjs";
import { UserService } from "../services/user_service";

export class UserController extends Controller {

    @DefaultWorker()
    async getUsers(@Singleton(UserService) service) {
        return jsonResult(service.getUsers());
    }
}
```

Comme vous pouvez le voir, le seul changement est que nous utilisons le décorateur "Singleton" dans la méthode getUsers. Cela créera un singleton et l'injectera lorsque getUsers est appelé. Ce singleton sera disponible dans toute l'application.

Puisque service est maintenant un paramètre, nous pouvons passer manuellement le paramètre lors de l'appel. Cela rend getUsers testable unitairement.

Pour effectuer des tests unitaires ou des tests E2E, veuillez lire cette documentation de test - [http://fortjs.info/tutorial/test/](http://fortjs.info/tutorial/test/)

### POST

Ajoutons une méthode "addUser" qui extraira les données du corps de la requête et appellera le service pour ajouter un utilisateur.

```javascript
async addUser(@Singleton(UserService) service) {
        const user = {
            name: this.body.name,
            gender: this.body.gender,
            address: this.body.address,
            emailId: this.body.emailId,
            password: this.body.password
        };
        const newUser = service.addUser(user);
        return jsonResult(newUser, HTTP_STATUS_CODE.Created);
}
```

> Dans le code ci-dessus, nous créons à nouveau le Singleton de UserService. Donc la question est : va-t-il créer un autre objet ?

Non, ce sera le même objet que dans getUser. FortJs fournit l'objet en tant que paramètre lorsqu'il appelle la méthode.

Les méthodes créées ne sont pas visibles par défaut pour une requête http. Donc, pour rendre cette méthode visible pour la requête http, nous devons la marquer comme un worker.

Une méthode est marquée comme un worker en ajoutant le décorateur "Worker". Le décorateur Worker prend une liste de méthodes http et rend cette méthode disponible uniquement pour ces méthodes http. Ajoutons donc le décorateur :

```javascript
@Worker([HTTP_METHOD.Post])
async addUser(@Singleton(UserService) service) {
    const user = {
        name: this.body.name,
        gender: this.body.gender,
        address: this.body.address,
        emailId: this.body.emailId,
        password: this.body.password
    };
    const newUser = service.addUser(user);
    return jsonResult(newUser, HTTP_STATUS_CODE.Created);
}
```

Maintenant, la route de cette méthode est la même que le nom de la méthode, c'est-à-dire "addUser". Vous pouvez vérifier cela en envoyant une requête POST à [http://localhost:4000/user/addUser](http://localhost:4000/user/addUser) avec les données de l'utilisateur dans le corps.

Mais nous voulons que la route soit "/", afin qu'elle soit une API REST. La route du worker est configurée en utilisant le décorateur "Route". Changeons la route maintenant.

```
@Worker([HTTP_METHOD.Post])
@Route("/")
async addUser(@Singleton(UserService) service) {
    const user = {
        name: this.body.name,
        gender: this.body.gender,
        address: this.body.address,
        emailId: this.body.emailId,
        password: this.body.password
    };
    const newUser = service.addUser(user);
    return jsonResult(newUser, HTTP_STATUS_CODE.Created);
}
```

Maintenant, notre endpoint est configuré pour une requête POST. Testons cela en envoyant une requête POST à [http://localhost:4000/user/](http://localhost:4000/user/) avec les données de l'utilisateur dans le corps.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-from-2019-10-20-22-43-19.png)

Il retourne l'utilisateur créé avec un identifiant qui est notre logique. Nous avons donc créé l'endpoint pour la requête POST, mais une chose importante à faire est de valider les données. La validation est une partie essentielle de toute application et est très importante pour une application backend.

Jusqu'à présent, notre code est propre et lisible. Mais si nous ajoutons du code de validation, il deviendra un peu sale.

Ne vous inquiétez pas, FortJs fournit le composant [Guard](http://fortjs.info/tutorial/guard/) pour ce type de travail. Selon la documentation de FortJs :

> Guard est une couche de sécurité au-dessus de Worker. Il contrôle si une requête doit être autorisée à appeler le Worker.

Nous allons donc utiliser guard pour la validation des données. Créons le guard en utilisant fort-creator. Exécutez la commande `fort-creator add` et choisissez Guard. Entrez le nom de fichier "UserValidator". Un fichier "user_validator_guard.js" sera créé dans le dossier guards. Ouvrez ce fichier.

Un guard a accès au corps, vous pouvez donc valider les données à l'intérieur. Retourner null à l'intérieur de la méthode `check` signifie que nous permettons d'appeler le worker. Retourner autre chose signifie bloquer l'appel.

Rendons cela plus clair en écrivant du code pour la validation. Collez le code ci-dessous à l'intérieur du fichier "user_validator_guard.js" :

```javascript

import { Guard, textResult, HTTP_STATUS_CODE } from "fortjs";

export class UserValidatorGuard extends Guard {

    async check() {
        const user = {
            name: this.body.name,
            gender: this.body.gender,
            address: this.body.address,
            emailId: this.body.emailId,
            password: this.body.password
        };
        const errMsg = this.validate(user);
        if (errMsg == null) {
            // passer l'utilisateur à la méthode worker, afin qu'ils n'aient pas besoin de parser à nouveau
            this.data.user = user;
            // retourner null signifie - guard permet à la requête de passer
            return null;
        } else {
            return textResult(errMsg, HTTP_STATUS_CODE.BadRequest);
        }
    }
    
    validate(user) {
        let errMessage;
        if (user.name == null || user.name.length < 5) {
            errMessage = "le nom doit comporter au moins 5 caractères"
        } else if (user.password == null || user.password.length < 5) {
            errMessage = "le mot de passe doit comporter au moins 5 caractères";
        } else if (user.gender == null || ["male", "female"].indexOf(user.gender) < 0) {
            errMessage = "le genre doit être soit masculin soit féminin";
        } else if (user.emailId == null || !this.isValidEmail(user.emailId)) {
            errMessage = "email non valide";
        } else if (user.address == null || user.address.length < 10) {
            errMessage = "la longueur de l'adresse doit être supérieure à 10";
        }
        return errMessage;
    }
    
    isValidEmail(email) {
        var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }


}
```

Dans le code ci-dessus :

* Nous avons créé une méthode validate qui prend le paramètre user. Elle valide l'utilisateur & retourne le message d'erreur s'il y a une erreur de validation, sinon null.
* Nous validons les données à l'intérieur de la méthode check, qui fait partie du cycle de vie de guard. Nous validons l'utilisateur à l'intérieur en appelant la méthode validate.
Si l'utilisateur est valide, alors nous passons la valeur de l'utilisateur en utilisant la propriété "data" et retournons null. Retourner null signifie que guard a autorisé cette requête et que le worker doit être appelé.
* Si un utilisateur n'est pas valide, nous retournons un message d'erreur en tant que réponse texte avec le code HTTP "Bad Request". Dans ce cas, l'exécution s'arrêtera ici et le worker ne sera pas appelé.

Afin d'activer ce guard pour la méthode addUser, nous devons l'ajouter en haut de addUser. Le guard est ajouté en utilisant le décorateur "Guards". Ajoutons donc le guard :

```javascript
@Worker([HTTP_METHOD.Post])
@Route("/")
@Guards([UserValidatorGuard])
async addUser(@Singleton(UserService) service) {
    const newUser = service.addUser(this.data.user);
    return jsonResult(newUser, HTTP_STATUS_CODE.Created);
}
```

Dans le code ci-dessus :

* J'ai ajouté le guard, "UserValidatorGuard" en utilisant le décorateur Guards.
* Avec le guard dans le processus, nous n'avons plus besoin de parser les données du corps à l'intérieur du worker. Plutôt, nous les lisons à partir de this.data que nous passons depuis "UserValidatorGuard".
* La méthode "addUser" ne sera appelée que lorsque Guard l'autorise, ce qui signifie que toutes les données sont valides.

Une chose à noter est que la méthode "addUser" semble très légère après avoir utilisé un composant, et elle fait aussi de la validation. Vous pouvez ajouter plusieurs guards à un worker, ce qui vous donne la possibilité de modulariser votre code en plusieurs guards et d'utiliser ce guard à plusieurs endroits.

> N'est-ce pas cool :D ?

Essayons d'ajouter un utilisateur avec des données invalides :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-from-2019-10-20-23-21-37.png)

Comme vous pouvez le voir dans la capture d'écran, j'ai essayé d'envoyer une requête sans mot de passe. Le résultat est - "le mot de passe doit comporter au moins 5 caractères". Cela signifie donc que le guard est activé et fonctionne parfaitement.

### PUT

Ajoutons une autre méthode - "updateUser" avec la route "" , le guard "UserValidatorGuard" (pour la validation de l'utilisateur) et surtout - le worker avec la méthode http "PUT".

```javascript
@Worker([HTTP_METHOD.Put])
@Guards([UserValidatorGuard])
@Route("/")
async updateUser(@Singleton(UserService) service) {
    const user = this.data.user;
    const userUpdated = service.updateUser(user);
    if (userUpdated === true) {
        return textResult("utilisateur mis à jour");
    } else {
        return textResult("utilisateur invalide");
    }
}
```

Le code mis à jour est similaire au code addUser sauf en termes de fonctionnalité, il met à jour les données. Ici, nous avons réutilisé UserValidatorGuard pour valider les données.

### DELETE

Afin de supprimer des données, l'utilisateur doit passer l'identifiant de l'utilisateur. Cela peut être fait par :

* Envoyer des données dans le corps comme nous l'avons fait pour ajouter & mettre à jour - {id:1}
* Envoyer des données dans la chaîne de requête - ?id=1
* Envoyer des données dans la route - pour cela, nous devons personnaliser notre route - "/user/1"

Nous avons déjà implémenté l'obtention de données à partir du corps. Voyons donc les deux autres façons :

**Envoyer des données dans la chaîne de requête**

Créons une méthode "removeByQueryString" et collons le code ci-dessous :

```javascript
@Worker([HTTP_METHOD.Delete])
@Route("/")
async removeByQueryString(@Singleton(UserService) service) {
    // prendre l'id de la chaîne de requête
    const userId = Number(this.query.id);
    const user = service.getUser(userId);
    if (user != null) {
        service.removeUser(userId);
        return textResult("utilisateur supprimé");
    } else {
        return textResult("utilisateur invalide", 404);
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-from-2019-10-20-23-40-34.png)

**Envoyer des données dans la route**

Vous pouvez paramétrer la route en utilisant "{var}" dans une route. Voyons comment.

Créons une autre méthode "removeByRoute" et collons le code ci-dessous :

```javascript
@Worker([HTTP_METHOD.Delete])
@Route("/{id}")
async removeByRoute(@Singleton(UserService) service) {
    
    // prendre l'id de la route
    const userId = Number(this.param.id);

    const user = service.getUser(userId);
    if (user != null) {
        service.removeUser(userId);
        return textResult("utilisateur supprimé");
    } else {
        return textResult("utilisateur invalide");
    }
}
```

Le code ci-dessus est exactement le même que removeByQueryString sauf qu'il extrait l'identifiant de la route et utilise le paramètre dans la route, c'est-à-dire "/{id}" où id est le paramètre.

Testons cela :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-from-2019-10-20-23-46-42.png)

Nous avons donc enfin créé une API REST pour toutes les fonctionnalités sauf l'obtention d'un utilisateur particulier par identifiant. Je vous laisse cela pour la pratique.

## POINTS D'INTÉRÊT

Q : Comment ajouter une authentification à "UserController", afin qu'aucune requête non authentifiée ne puisse appeler l'endpoint "/user".

R : Il existe plusieurs approches pour cela :

* Nous pouvons vérifier dans chaque worker pour l'authentification. (MAUVAIS - beaucoup de travail supplémentaire et répétition de code)
* Créer un composant Guard et l'assigner à chaque worker. (BON)
* Créer un composant [Shield](http://fortjs.info/tutorial/shield/) et l'assigner au contrôleur. Shield est une couche de sécurité similaire à guard mais fonctionne au-dessus du contrôleur, donc si shield rejette alors le contrôleur n'est pas initié. (MEILLEUR)

Jetez un œil à la documentation d'authentification de FortJs - [http://fortjs.info/tutorial/authentication/](http://fortjs.info/tutorial/authentication/)

## RÉFÉRENCES

* [http://fortjs.info/](http://fortjs.info/)
* [https://medium.com/fortjs](https://medium.com/fortjs)