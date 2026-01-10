---
title: Comment utiliser TypeSpec pour documenter et modéliser des APIs
subtitle: ''
author: Adalbert Pungu
co_authors: []
series: null
date: '2025-04-11T19:25:13.959Z'
originalURL: https://freecodecamp.org/news/use-typespec-for-documenting-and-modeling-apis
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744399481891/de5db16a-2eea-46d8-820d-50c1e66d5019.png
tags:
- name: TypeSpec
  slug: typespec
- name: openai
  slug: openai
- name: APIs
  slug: apis
- name: Developer
  slug: developer
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: TypeScript
  slug: typescript
seo_title: Comment utiliser TypeSpec pour documenter et modéliser des APIs
seo_desc: 'If you''re curious and passionate about technology like I am, and you’re
  looking for clarity in your code, you''ve likely already experienced the limitations
  of conventional tools for documenting and modeling APIs.

  Tools such as Swagger, JSON Schema, o...'
---

Si vous êtes curieux et passionné par la technologie comme je le suis, et que vous cherchez de la clarté dans votre code, vous avez probablement déjà rencontré les limitations des outils conventionnels pour documenter et modéliser les APIs.

Des outils tels que Swagger, JSON Schema ou OpenAPI sont puissants, mais ils peuvent être verbeux, inflexibles ou peu propices à la réutilisation.

Eh bien, j'ai récemment découvert TypeSpec. Dans ce guide, je vais vous montrer comment tirer parti de TypeSpec pour créer des APIs REST modernes, maintenables et bien documentées.

![Capture d'écran du site web de TypeSpec. Il présente un fond sombre avec "Design APIs" en gros texte et une description sur la conception de données pour générer des schémas, des spécifications, du code, et plus. Il inclut les boutons "Install" et "Playground" en haut.](https://cdn.hashnode.com/res/hashnode/image/upload/v1744242129685/403f9a32-8d06-47e2-b551-2ec1de1f6c0a.png align="center")

Nous allons examiner :

* [Prérequis](#heading-prerequis)
    
* [Qu'est-ce que TypeSpec ?](#heading-quest-ce-que-typespec)
    
* [Pourquoi utiliser TypeSpec ?](#heading-pourquoi-utiliser-typespec)
    
* [Comment installer et configurer TypeSpec](#heading-comment-installer-et-configurer-typespec)
    
* [Syntaxe de base de TypeSpec](#heading-syntaxe-de-base-de-typespec)
    
* [Comment créer un modèle d'API REST](#heading-comment-creer-un-modele-dapi-rest)
    
* [Comment construire l'API dans Express et](#heading-comment-construire-lapi-dans-express-et) [ASP.NET](http://ASP.NET) [Core](#heading-comment-construire-lapi-dans-express-et-aspnet-core)
    
* [Bonnes pratiques pour structurer les projets et composants TypeSpec](#heading-bonnes-pratiques-pour-structurer-les-projets-et-composants-typespec)
    
* [Conclusion](#heading-conclusion)
    

## **Prérequis**

Avant de plonger dans l'utilisation de TypeSpec pour documenter et modéliser des APIs, voici quelques éléments que vous devrez connaître et/ou avoir :

* **Node.js** (version 18 ou supérieure)
    
* **npm** pour la gestion des dépendances
    
* **Visual Studio Code** (recommandé pour tirer parti de l'extension officielle TypeSpec). Pour une expérience optimale, pour créer votre projet facilement, il fournit la coloration syntaxique, la validation, l'autocomplétion, la navigation, et plus encore.
    
* **Extension TypeSpec** dans VS Code (Vous pouvez installer l'extension via [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=typespec.typespec-vscode))
    
* Une compréhension de l'utilisation et de la création d'APIs
    

## Qu'est-ce que TypeSpec ?

TypeSpec est un langage déclaratif open-source, développé par Microsoft, conçu pour décrire les APIs de manière explicite, réutilisable, évolutive et basée sur des standards. Il est conçu pour modéliser les APIs REST, gRPC, GraphQL et d'autres types d'APIs, et offre une syntaxe moderne proche de TypeScript.

Il peut générer automatiquement :

* Des spécifications OpenAPI, JSON Schema ou Protobuf
    
* Du code serveur et client
    
* De la documentation d'API
    
* Et d'autres artefacts liés à l'interface
    

TypeSpec n'est pas seulement un langage, c'est une plateforme de conception d'API qui favorise l'abstraction, encourage la réutilisation du code et s'intègre avec des outils modernes comme Visual Studio Code via une extension dédiée. Vous pouvez installer l'extension via le [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=typespec.typespec-vscode).

## Pourquoi utiliser TypeSpec ?

Avant de plonger dans le code, prenons une minute pour comprendre la philosophie de TypeSpec. Microsoft utilise TypeSpec en interne pour fournir des services d'API de haute qualité à des millions de clients, sur des dizaines de milliers de points de terminaison, tout en assurant la qualité du code, la gouvernance et l'évolutivité.

![Capture d'écran avec le texte sur un fond sombre qui dit : "Why TypeSpec - API-First for developers. With TypeSpec, remove the handwritten files that slow you down, and generate standards-compliant API schemas in seconds."](https://cdn.hashnode.com/res/hashnode/image/upload/v1744242196525/a1947dfb-e46d-4083-95c5-218615ab75e6.png align="center")

Contrairement aux générateurs tels que Swagger, Codegen ou Postman, qui partent d'un fichier OpenAPI pour générer du code, TypeSpec fait l'inverse : vous écrivez d'abord votre conception d'API dans un DSL (Domain Specific Language), puis vous générez tout ce dont vous avez besoin.

TypeSpec a été conçu pour répondre aux principaux défis de la conception et de la gouvernance des APIs à grande échelle :

* **Simplification** : syntaxe claire et concise pour se concentrer sur la logique métier.
    
* **Réutilisabilité** : encapsule les types, les modèles de requête/réponse et les directives dans des composants modulaires.
    
* **Productivité** : génère automatiquement les ressources nécessaires à partir d'une définition source unique.
    
* **Cohérence** : maintient la conformité avec les standards internes grâce à des bibliothèques partagées.
    
* **Interopérabilité** : s'intègre avec l'écosystème OpenAPI et supporte la génération multi-format.
    
* **Évolutivité** : conçu pour gérer des milliers de points de terminaison comme ceux utilisés par Microsoft Azure.
    

Regardons comment installer et configurer l'environnement de développement.

## Comment installer et configurer TypeSpec

Avant de pouvoir commencer à écrire votre première API avec TypeSpec, vous devez configurer votre environnement de développement. Voici comment installer TypeSpec sur votre machine.

#### Prérequis :

* **Node.js** (version 18 ou supérieure)
    
* **npm** pour la gestion des dépendances
    
* **Visual Studio Code** (recommandé pour tirer parti de l'extension officielle TypeSpec). Pour une expérience optimale, il fournit la coloration syntaxique, la validation, l'autocomplétion, la navigation, et plus encore.
    

Installation globale de TypeSpec CLI :

```bash
npm install -g @typespec/compiler
```

### Comment créer un projet TypeSpec

La manière la plus simple de créer un projet est d'utiliser Visual Studio Code via l'extension TypeSpec que vous avez installée (si vous n'êtes pas à l'aise avec la ligne de commande (CMD)).

Créez un dossier contenant le projet et ouvrez-le avec Visual Studio Code. Ensuite, cliquez sur l'onglet `View`, puis sur `Comment Palette`.

Dans la barre de recherche qui apparaît, entrez `TypeSpec: Create TypeSpec Project`.

Suivez les sélections rapides pour sélectionner le dossier racine du projet que vous venez de créer. Ensuite, choisissez le modèle - pour notre cas, ce sera `Generic REST API` - et entrez le nom du projet. Laissez l'émetteur `OpenAPI 3.1 document` (3.1 est la version actuelle au moment de l'écriture) sélectionné par défaut. Cela nous mettra `@typespec/http@typespec/openapi3`. Enfin, attendez que la configuration du projet se termine.

Vous devriez avoir une configuration de projet TypeSpec de base avec une structure qui ressemble à ceci :

![Une capture d'écran d'un explorateur de fichiers montrant un dossier nommé "node_modules" et des fichiers : .gitignore, main.tsp, package-lock.json, package.json, et tspconfig.yaml.](https://cdn.hashnode.com/res/hashnode/image/upload/v1744242632713/69485276-b885-450c-870a-56af5e6d8122.png align="center")

* **node\_modules/** : Répertoire où npm installe les dépendances du projet.
    
* **main.tsp** : le point d'entrée pour votre build TypeSpec. Ce fichier contient généralement les définitions principales de vos modèles, services et opérations.
    
* **package.json** : Contient les métadonnées du projet, y compris les dépendances, les scripts et d'autres informations liées au projet.
    
* **tspconfig.yaml** : Fichier de configuration du compilateur TypeSpec, spécifiant les options et paramètres pour le processus de génération.
    

Vous pouvez également exécuter `tsp compile .` pour compiler le projet, mais il est préférable d'exécuter `tsp compile . --watch` pour compiler automatiquement les changements pendant le développement à chaque sauvegarde.

![Une interface de ligne de commande montrant la compilation réussie d'un projet en utilisant le compilateur TypeSpec v1.0.0-rc.0, avec une sortie vers "tsp-output/schema/".](https://cdn.hashnode.com/res/hashnode/image/upload/v1744242865089/dea4c75e-80e3-454d-a1ab-af4186423271.png align="center")

Une fois le projet compilé, vous verrez les dossiers `tsp-output` et `schema` générés et un fichier ajouté `openai.yaml`.

![Structure de répertoire de fichiers avec des dossiers "node_modules" et "tsp-output", contenant des fichiers comme "openapi.yaml", ".gitignore", "main.tsp", "package-lock.json", "package.json", et "tsconfig.yaml".](https://cdn.hashnode.com/res/hashnode/image/upload/v1744242771607/ad948a7c-ea56-44df-861d-7fa04cad1a6d.png align="center")

* **tsp-output/** : Répertoire où le compilateur TypeSpec génère les fichiers.
    
* **openapi.yaml** : Fichier de spécification OpenAPI généré pour votre API, détaillant les points de terminaison de l'API, les modèles et les opérations. La sortie peut varier en fonction du format cible spécifié dans le fichier `tspconfig.yaml`.
    

```yaml
emit:
  - "@typespec/openapi3"
options:
  "@typespec/openapi3":
    emitter-output-dir: "{output-dir}/schema"
    openapi-versions:
      - 3.1.0
```

Grâce à cette configuration du fichier `tspconfig.yaml`, l'un des principaux atouts de TypeSpec est sa capacité à générer automatiquement des spécifications OpenAPI à partir d'un code source clair, typé et modulaire. Cela signifie que vous pouvez écrire votre API comme vous le feriez en TypeScript (ou dans un DSL bien structuré), et obtenir une sortie dans des fichiers `.yaml` compatibles avec tout l'écosystème OpenAPI : Swagger UI, Postman, Redoc, et ainsi de suite.

Dans la section suivante, nous examinerons la syntaxe de base de TypeSpec.

## Syntaxe de base de TypeSpec

Maintenant que vous avez une idée claire de ce qu'est TypeSpec et de ses avantages dans le monde de la conception d'API, il est temps d'aborder le cœur du sujet : la syntaxe de base.

TypeSpec est un langage déclaratif, inspiré de TypeScript, qui vous permet de modéliser les ressources, les routes, les structures de données et les comportements d'une API de manière explicite, lisible et modulaire. Sa syntaxe est basée sur des mots-clés simples et une organisation claire des fichiers, ce qui le rend facile à apprendre tout en étant puissant.

### Bases du langage

Voici un exemple très simple de définition d'un modèle avec TypeSpec :

```typescript
model Book {
  id: string;
  title: string;
  author: string;
}
```

Ce bloc définit une ressource `Book` avec trois champs typés. Le mot-clé `model` est utilisé pour décrire les objets JSON manipulés par l'API. Il est équivalent aux schémas dans JSON Schema ou aux définitions de type dans OpenAPI.

#### Définir une opération HTTP

TypeSpec vous permet de lier des opérations aux modèles en utilisant le mot-clé `@route`. Voici un exemple minimal d'un point de terminaison :

```typescript
@route("/books")
op listBooks(): Book[];
```

Cette syntaxe déclare une opération REST qui retourne une liste de livres. `@route` indique le chemin de l'URL, `op` introduit une opération, et `Book[]` est le type de retour.

Vous pouvez également définir des paramètres de chemin, de requête ou de corps très facilement.

```typescript
@route("/books/{id}")
op getBook(@path id: string): Book;
```

Dans cet exemple, nous déclarons que `id` est un paramètre d'URL (paramètre de chemin).

### **Concepts fondamentaux**

#### `model` Définir des structures de données

Un `model` représente une entité d'API, comme un objet JSON. Les modèles sont la base de vos échanges d'informations.

```typescript
model User {
  id: string;
  email: string;
  age?: int32;
}
```

#### `interface` **Grouper les opérations**

Une `interface` regroupe un ensemble d'opérations logiquement liées. Cela est utile pour structurer de grands ensembles d'API.

```typescript
interface BookOperations {
  @get op listBooks(): Book[];
  @get op getBook(@path id: string): Book;
}
```

#### `service` **Point d'entrée de l'API**

Un `service` définit les interfaces exposées publiquement, leur version et le chemin de base.

```typescript
@service({ title: "Book API", version: "1.0.0" })
namespace BookApi {
  interface BookOperations;
}
```

### **Importer et organiser votre code avec des espaces de noms**

TypeSpec fournit une organisation claire grâce aux espaces de noms, similaires aux modules ou packages.

```typescript
namespace CommonModels {
  model Error {
    message: string;
  }
}
```

Ensuite, vous pouvez les importer dans un autre fichier comme ceci :

```typescript
import CommonModels from "./common.tsp";
```

### **Exemple complet d'un service REST**

Prenons un exemple complet d'un service REST dans TypeSpec.

```typescript
@service({ title: "Book Service", version: "1.0.0" })

@route("/books")

namespace BookService {

  model Book {
    id: string;
    title: string;
    author: string;
    publishedYear?: int32;
  }

  @get()
  op listBooks(): Book[];

  @post()
  op createBook(@body book: Book): Book;

  @get("/{id}")
  op getBook(@path id: string): Book;

  @put("/{id}")
  op updateBook(@path id: string, @body book: Book): Book;

  @delete("/{id}")
  op deleteBook(@path id: string): void;
}
```

**Voici ce qui se passe** :

* `@service({ title, version })` : Définit les métadonnées du service (nom, version), utiles pour la documentation générée (par exemple, Swagger UI).
    
* `@route("/books")` : Définit le chemin de base pour toutes les opérations de cette API.
    
* `namespace BookService {
... }` : Encapsule tous les modèles et opérations liés à ce service sous un seul nom logique.
    

**Viennent ensuite les opérations** :

* `@get() op listBooks()` : Point de terminaison `GET /books` qui retourne un tableau de livres.
    
* `@post() op createBook()` : Point de terminaison `POST /books` qui accepte un objet `Book` dans le corps de la requête (`@body`) et retourne le livre créé.
    
* `@get("/{id}")` : Point de terminaison `GET /books/{id}` qui récupère un livre via son identifiant (`@path`).
    
* `@put("/{id}")` : Point de terminaison `PUT /books/{id}` qui met à jour les données d'un livre.
    
* `@delete("/{id}")` : Supprime un livre via son `id`. Le type `void` signifie qu'aucune donnée n'est retournée.
    

Avec seulement quelques lignes, vous obtenez un service REST complet, bien organisé, facilement lisible, prêt à être automatiquement converti en documentation OpenAPI, un SDK client ou du code backend.

### **Ajouter des annotations de validation**

TypeSpec facilite l'ajout d'annotations de validation à vos modèles en utilisant :

```typescript
model Book {
  id: string;
  title: string @minLength(3);
  author: string @minLength(3);
  publishedYear?: int32 @minValue(1800);
}
```

Cela ajoute des règles de validation directement au schéma, qui seront prises en compte lors de la génération OpenAPI.

### Comparaison avec d'autres outils (OpenAPI / Swagger)

Vous pourriez vous demander - pourquoi utiliser TypeSpec plutôt que d'écrire directement en OpenAPI ?

Prenons l'exemple d'OpenAPI 3 (YAML) :

```yaml
paths:
  /books:
    get:
      summary: Get list of books
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Book'
    post:
      summary: Create a new book
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Book'
      responses:
        '201':
          description: Created
  /books/{id}:
    get:
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
    put:
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Book'
    delete:
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
components:
  schemas:
    Book:
      type: object
      properties:
        id:
          type: string
        title:
          type: string
        author:
          type: string
        publishedYear:
          type: integer
```

Comme vous pouvez le voir, la définition OpenAPI est beaucoup plus verbeuse. Les relations entre les chemins, les méthodes, les schémas et les paramètres sont dispersées, ce qui complique la lecture et la maintenance. De plus, elle est moins typée, étant donné qu'OpenAPI reste en YAML (ou JSON), sans la sécurité de typage ou la modularité d'un vrai langage.

#### Pourquoi TypeSpec est utile ici

Avec TypeSpec, tout est centralisé dans un format déclaratif, modulaire, typé et intuitif.

* **Meilleure lisibilité** : moins de bruit, plus d'intention.
    
* **Réutilisabilité** : vous pouvez créer des composants modulaires et les partager entre les projets.
    
* **Productivité** : vous écrivez moins de code et générez plus (OpenAPI, client, serveur, doc).
    
* **Cohérence** : les erreurs sont détectées tôt grâce au typage fort.
    

| **Critère** | **OpenAPI / Swagger** | **TypeSpec** |
| --- | --- | --- |
|  |  |  |
| **Syntaxe** | Verbeuse (YAML/JSON) | Déclarative, typée, concise |
| **Organisation** | Fragmentée | Modulaire (namespace, import) |
| **Modulaire** | Limitée | Élevée (modèles, services) |
| **Validation intégrée** | Séparée ou manuelle | Décorateurs (@minLength, etc.) |
| **Génération automatique** | Manuelle | Intégrée (OpenAPI, SDK, etc.) |

Note : TypeSpec ne remplace pas OpenAPI, mais le complète : vous écrivez en TypeSpec, puis générez automatiquement des fichiers OpenAPI, des SDK, des spécifications, etc. Il vous donne un langage source pour décrire précisément votre API.

Dans la section suivante, nous examinerons comment créer un modèle d'API REST.

## Comment créer un modèle d'API REST

Pour approfondir notre compréhension de la création d'API REST avec TypeSpec, continuons avec l'exemple de gestion de livres. Dans cet exemple, nous allons créer un modèle `Book`, définir un service pour gérer les livres, et ajouter des validations pour garantir que les données respectent les bonnes contraintes.

### Définir un modèle de données pour `Book`

Tout d'abord, nous allons définir un modèle de données pour la ressource Book. Un livre peut avoir les propriétés suivantes :

* `id` : Un identifiant unique pour le livre.
    
* `title` : Le titre du livre.
    
* `author` : L'auteur du livre.
    
* `publicationYear` : L'année de publication du livre.
    
* `isbn` : Le numéro ISBN du livre.
    

**Modèle `Book` dans TypeSpec**

```typescript
model Book {
  id: integer;
  @minLength(1)
  title: string;
  @minLength(1)
  author: string;
  publicationYear: integer;
  @pattern("^\\d{3}-\\d{1,5}-\\d{1,7}-\\d{1,7}-\\d{1}$")
  isbn: string;
}
```

* `id` : Identifiant unique du livre (type `integer`).
    
* `title` et `author` : Chaînes de caractères représentant le titre et l'auteur du livre, validées par `@minLength(1)` pour s'assurer qu'elles ne sont pas vides.
    
* `publicationYear` : L'année de publication du livre (type `integer`).
    
* `isbn` : Le numéro ISBN du livre, validé avec une expression régulière qui correspond au format standard d'un ISBN.
    

### Définir un service REST pour gérer les livres

Maintenant que nous avons un modèle `Book`, nous allons créer un service pour gérer les opérations CRUD sur cette ressource. Ce service contiendra des méthodes pour récupérer un livre par son identifiant, créer un nouveau livre, mettre à jour un livre existant et supprimer un livre.

**Service `BooksService` dans TypeSpec**

```typescript
service BooksService {

  @get("/books/{id}")
  getBook(id: integer): Book;

  @post("/books")
  createBook(book: Book): Book;

  @put("/books/{id}")
  updateBook(id: integer, book: Book): Book;

  @delete("/books/{id}")
  deleteBook(id: integer): void;
}
```

Le `BooksService` contient quatre méthodes pour effectuer des actions sur les livres :

* `@get("/books/{id}")` : Méthode pour récupérer un livre par son `id`.
    
* `@post("/books")` : Méthode pour créer un nouveau livre.
    
* `@put("/books/{id}")` : Méthode pour mettre à jour un livre existant par son `id`.
    
* `@delete("/books/{id}")` : Méthode pour supprimer un livre en fonction de son `id`.
    

Ces méthodes utilisent des annotations HTTP pour indiquer le type d'opération qu'elles effectuent (GET, POST, PUT, DELETE).

### **Ajouter des validations supplémentaires pour le modèle `Book`**

Comme dans l'exemple précédent pour les utilisateurs, nous pouvons ajouter des validations supplémentaires sur les propriétés du modèle **Book**.

**Exemple de validation sur `publicationYear` et `isbn`**

```typescript
model Book {
  id: integer;
  @minLength(1)
  title: string;
  @minLength(1)
  author: string;
  @minValue(1000)
  publicationYear: integer;
  @pattern("^\\d{3}-\\d{1,5}-\\d{1,7}-\\d{1,7}-\\d{1}$")
  isbn: string;
}
```

* `@minValue(1000)` garantit que l'année de publication est supérieure ou égale à 1000.
    
* La validation de l'`isbn` reste la même, utilisant une expression régulière pour valider un format ISBN standard.
    

### **Un service complet pour gérer les livres**

Maintenant que nous avons le modèle `Book` et les validations nécessaires, voici un service complet pour gérer les livres, avec toutes les opérations essentielles.

**Service `BooksService` complet dans TypeSpec**

```typescript
model Book {
  id: integer;
  @minLength(1)
  title: string;
  @minLength(1)
  author: string;
  @minValue(1000)
  publicationYear: integer;
  @pattern("^\\d{3}-\\d{1,5}-\\d{1,7}-\\d{1,7}-\\d{1}$")
  isbn: string;
}

service BooksService {
  @get("/books/{id}")
  getBook(id: integer): Book;

  @post("/books")
  createBook(book: Book): Book;

  @put("/books/{id}")
  updateBook(id: integer, book: Book): Book;

  @delete("/books/{id}")
  deleteBook(id: integer): void;
}
```

* Le modèle `Book` définit les propriétés et les validations pour un livre.
    
* Le `BooksService` fournit des points de terminaison pour récupérer, créer, mettre à jour et supprimer un livre.
    
* Chaque méthode de service est correctement annotée avec les verbes HTTP correspondants (`GET`, `POST`, `PUT`, `DELETE`).
    

Et voici un résumé de tout ce que nous avons fait :

* Nous avons créé un modèle `Book` avec des propriétés telles que le titre, l'auteur, l'année de publication et le numéro ISBN.
    
* Nous avons défini un `BooksService` pour fournir des opérations CRUD sur les livres.
    
* Nous avons ajouté des validations pour garantir que les données respectent les contraintes spécifiées (par exemple, ISBN et année de publication).
    
* Nous avons conçu une API REST complète pour gérer les livres avec TypeSpec, en utilisant un minimum de code et en restant fidèle aux standards.
    

Cet exemple montre à quel point TypeSpec peut être utilisé rapidement et efficacement pour modéliser une API REST, tout en assurant une structure claire et des validations robustes.

## Comment construire l'API dans Express et ASP.NET Core

Maintenant que nous avons défini un service REST de gestion de livres avec TypeSpec, voyons comment nous implémenterions cette même API en utilisant deux frameworks populaires :

* **ExpressJS (Node.js / TypeScript)**
    
* **ASP.NET Core (C#)**
    

Cela nous permettra de mieux comparer la concision et la lisibilité de TypeSpec avec les implémentations traditionnelles.

**Implémentation manuelle avec ExpressJS (Node.js / TypeScript) :**

```typescript
//server.ts
import express from 'express';

const app = express();
app.use(express.json());

interface Book {
  id: number;
  title: string;
  author: string;
  publicationYear: number;
  isbn: string;
}

const books: Book[] = [];

// GET /books/:id
app.get('/books/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const book = books.find(b => b.id === id);
  if (!book) return res.status(404).send({ message: 'Book not found' });
  res.send(book);
});

// POST /books
app.post('/books', (req, res) => {
  const newBook: Book = req.body;
  books.push(newBook);
  res.status(201).send(newBook);
});

// PUT /books/:id
app.put('/books/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = books.findIndex(b => b.id === id);
  if (index === -1) return res.status(404).send({ message: 'Book not found' });

  books[index] = req.body;
  res.send(books[index]);
});

// DELETE /books/:id
app.delete('/books/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = books.findIndex(b => b.id === id);
  if (index === -1) return res.status(404).send({ message: 'Book not found' });

  books.splice(index, 1);
  res.status(204).send();
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

**Observations :**

* Beaucoup de logique répétitive.
    
* Aucune validation automatique.
    
* Les routes doivent être maintenues manuellement.
    
* Aucune documentation d'API générée automatiquement.
    

**Implémentation manuelle avec** [**ASP.NET**](http://ASP.NET) **Core (C#) :**

```csharp
// Book.cs
public class Book
{
    public int Id { get; set; }
    
    [Required]
    public string Title { get; set; } = string.Empty;
    
    [Required]
    public string Author { get; set; } = string.Empty;
    
    [Range(1000, int.MaxValue)]
    public int PublicationYear { get; set; }
    
    [RegularExpression(@"^\d{3}-\d{1,5}-\d{1,7}-\d{1,7}-\d{1}$")]
    public string Isbn { get; set; } = string.Empty;
}
```

```csharp
// BooksController.cs
[ApiController]
[Route("books")]
public class BooksController : ControllerBase
{
    private static readonly List<Book> books = new();

    [HttpGet("{id}")]
    public IActionResult GetBook(int id)
    {
        var book = books.FirstOrDefault(b => b.Id == id);
        if (book == null) return NotFound("Book not found");
        return Ok(book);
    }

    [HttpPost]
    public IActionResult CreateBook([FromBody] Book book)
    {
        books.Add(book);
        return CreatedAtAction(nameof(GetBook), new { id = book.Id }, book);
    }

    [HttpPut("{id}")]
    public IActionResult UpdateBook(int id, [FromBody] Book updatedBook)
    {
        var index = books.FindIndex(b => b.Id == id);
        if (index == -1) return NotFound("Book not found");

        books[index] = updatedBook;
        return Ok(updatedBook);
    }

    [HttpDelete("{id}")]
    public IActionResult DeleteBook(int id)
    {
        var book = books.FirstOrDefault(b => b.Id == id);
        if (book == null) return NotFound("Book not found");

        books.Remove(book);
        return NoContent();
    }
}
```

**Observations :**

* Plus formel et structuré qu'Express, grâce aux annotations C# (`[HttpPost]`, `[Required]`, etc.).
    
* La validation est gérée automatiquement via les annotations de données.
    
* Une fois de plus, aucune génération automatique OpenAPI ou SDK client sans configuration supplémentaire.
    

**Comparaison avec TypeSpec :**

| **Aspect** | **TypeSpec** | **ExpressJS** | [**ASP.NET**](http://ASP.NET) **Core** |
| --- | --- | --- | --- |
|  |  |  |  |
| **Syntaxe** | Déclarative | Impérative | Structurée |
| **Validation** | Automatique | Manuelle | Annotations de données |
| **Documentation** | Automatique | Manuelle | Générée (Swashbuckle) |
| **Réutilisabilité** | Élevée | Faible | Moyenne |
| **Génération** | OpenAPI/SDK | Non native | Possible |

## Bonnes pratiques pour structurer les projets et composants TypeSpec

Lorsque vous commencez à écrire des définitions d'API dans TypeSpec, il est facile de tout mettre dans un seul fichier. Mais comme pour tout projet logiciel, à mesure que l'application grandit, une bonne structure devient essentielle pour garantir la lisibilité, la réutilisabilité et la maintenabilité du code.

Voici un ensemble de bonnes pratiques que je recommande fortement :

### **Organiser par domaine fonctionnel**

Utilisez des espaces de noms pour regrouper les modèles, interfaces et opérations par domaine métier : **book**, **user**, **auth**, **payment**, etc.

```typescript
namespace MyApi.Books;
```

Créez un dossier `/books` avec les fichiers suivants :

```yaml
src/
├── books/
│   ├── models.tsp
│   ├── routes.tsp
│   └── service.tsp
```

Cela assure une séparation claire des responsabilités, tout comme dans un projet Node.js bien structuré.

### **Un seul point d'entrée `main.tsp`**

C'est le fichier principal qui orchestrer :

```typescript
// main.tsp
import "./books/service.tsp";
import "./users/service.tsp";
import "./auth/service.tsp";
```

Cela vous permet de compiler l'ensemble du projet à partir d'un seul point.

### Créer des composants réutilisables

Définissez les modèles et types communs dans un fichier partagé. Exemple :

```typescript
// common/models.tsp
model ErrorResponse {
  code: string;
  message: string;
}

@defaultResponse
op Error(): ErrorResponse;
```

Ensuite, importez-les dans vos autres fichiers :

```typescript
import "../common/models.tsp";
```

Cela est pratique pour centraliser les erreurs, les réponses standard, les types de pagination, etc.

### Utiliser des décorateurs pour enrichir vos composants

Les décorateurs tels que `@doc`, `@minLength`, `@server`, `@route` ou `@tag` peuvent être utilisés pour générer des APIs valides et documentées sans effort supplémentaire :

```typescript
@route("/books")
@doc("Get all books")
op listBooks(): Book[];
```

Une API bien annotée est une API prête pour la génération automatique de documentation ou de clients.

### Définir les serveurs au bon endroit

Ajoutez votre directive @server à un fichier `service.tsp` ou global `api.tsp` :

```typescript
@server("Production", "https://api.mysite.com")
@server("Staging", "https://staging.mysite.com")
```

Cela vous permet de cibler différents environnements sans dupliquer les définitions.

### Valider régulièrement

Intégrez `tsp compile` dans votre CI/CD pour vous assurer que vos définitions sont toujours valides. Exemple avec un script npm :

```bash
npm run tsp compile src/main.tsp --emit=./dist
```

Cela évite les erreurs de dernière minute et garantit la cohérence de votre API au fil du temps.

**Exemple de structure complète recommandée :**

```yaml
project-root/
├── src/
│   ├── books/
│   │   ├── models.tsp
│   │   ├── routes.tsp
│   │   └── service.tsp
│   ├── users/
│   │   ├── models.tsp
│   │   └── service.tsp
│   ├── common/
│   │   └── models.tsp
│   └── main.tsp
├── tspconfig.yaml
├── package.json
└── README.md
```

En résumé :

| **Bonne pratique** | **Pourquoi c'est important** |
| --- | --- |
|  |  |
| Utiliser `namespaces` | Organisation claire, lisibilité |
| Diviser les fichiers par domaine | Réutilisabilité, modularité |
| Centraliser les composants partagés | DRY (Don't Repeat Yourself) |
| Utiliser des décorateurs | Enrichir la documentation et la validation |
| Intégrer avec CI/CD | Qualité continue, pas de surprises |
| Avoir un fichier d'entrée clair (`main.tsp`) | Compilation simple et centralisée |

## Conclusion

TypeSpec représente une véritable évolution dans la manière dont nous concevons, documentons et maintenons les APIs. En adoptant une approche déclarative, modulaire et typée, il simplifie la définition des APIs tout en améliorant leur qualité, leur lisibilité et leur cohérence à grande échelle.

Que vous soyez un développeur front-end consommant des APIs, un architecte logiciel cherchant à standardiser les pratiques de votre équipe, ou un passionné de documentation technique, TypeSpec vous offre une solution robuste, moderne et extensible.

L'écosystème TypeSpec est encore jeune mais très prometteur, soutenu par Microsoft et utilisé en interne à grande échelle. Il est donc temps de commencer à l'explorer et à l'adopter pour vos projets.

#### Ressources

1. **Site officiel de TypeSpec**  
    [https://typespec.io](https://typespec.io/)  
    Documentation complète, guides, références de syntaxe et APIs.
    
2. **Dépôt GitHub de TypeSpec (Microsoft)**  
    [https://github.com/microsoft/typespec](https://github.com/microsoft/typespec/)  
    Code source, exemples et discussions communautaires.
    
3. **Playground TypeSpec (essayer dans le navigateur)**  
    [https://typespec.io/playground](https://typespec.io/playground/)  
    Testez rapidement vos modèles sans rien installer.
    
4. **Documentation TypeSpec — Microsoft Learn**  
    [https://learn.microsoft.com/en-us/azure/developer/typespec/overview](https://learn.microsoft.com/en-us/azure/developer/typespec/overview/)  
    Apprenez à utiliser TypeSpec pour créer des APIs cohérentes et de haute qualité de manière efficace et les intégrer de manière transparente avec les chaînes d'outils existantes.
    
5. **Spécification OpenAPI**  
    [https://swagger.io/specification](https://swagger.io/specification/)  
    Pour comparer avec les standards actuels de description d'API.
    
6. **TypeSpec 101 par Mario Guerra Product Manager pour TypeSpec chez Microsoft**  
    [https://www.youtube.com/playlist?list=PLYWCCsom5Txglkl\_I1XvwzrzM5G3SuVsR](https://www.youtube.com/playlist?list=PLYWCCsom5Txglkl_I1XvwzrzM5G3SuVsR/)  
    Une série de tutoriels, animée par Mario Guerra, responsable produit pour TypeSpec chez Microsoft, vous guidera à travers le processus de création d'une API REST en utilisant TypeSpec, et la génération d'une spécification OpenAPI à partir de notre code.
    
7. **APIs à grande échelle avec TypeSpec**  
    [https://youtu.be/yfCYrKaojDo](https://youtu.be/yfCYrKaojDo/)  
    Une conférence donnée par Mandy Whaley de Microsoft lors du sommet API 2024 à Austin, Texas.
    

Merci pour la lecture. Vous pouvez me trouver sur [LinkedIn](https://www.linkedin.com/in/AdalbertPungu/), et me suivre sur tous les réseaux sociaux @AdalbertPungu.