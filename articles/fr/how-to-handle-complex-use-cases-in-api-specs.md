---
title: Comment gérer les cas d'utilisation complexes dans vos spécifications OpenAPI
  – Guide de documentation d'API
subtitle: ''
author: Onyeanuna Prince
co_authors: []
series: null
date: '2024-11-04T16:44:16.429Z'
originalURL: https://freecodecamp.org/news/how-to-handle-complex-use-cases-in-api-specs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730415311732/58afe01c-0ac4-4351-a4b4-a15729b5bcb1.png
tags:
- name: 'Technical writing '
  slug: technical-writing-1
- name: OpenApi
  slug: openapi
- name: APIs
  slug: apis
- name: documentation
  slug: documentation
seo_title: Comment gérer les cas d'utilisation complexes dans vos spécifications OpenAPI
  – Guide de documentation d'API
seo_desc: When you’re documenting an API reference, there are two main approaches
  you can follow. You can either use the manual approach of filling in the endpoints
  via a user interface, or organize a structured document containing all the necessary
  informatio...
---

Lorsque vous documentez une référence d'API, il existe deux approches principales que vous pouvez suivre. Vous pouvez soit utiliser l'approche manuelle consistant à remplir les endpoints via une interface utilisateur, soit organiser un document structuré contenant toutes les informations nécessaires sur votre API.

Ce document structuré est appelé une [spécification OpenAPI](https://www.openapis.org/) (OpenAPI Spec ou OAS).

Une spécification OpenAPI est un format pour décrire les API. C'est un plan qui décrit tout le fonctionnement d'une API – quels endpoints sont disponibles, quelles données vous pouvez envoyer ou recevoir, et quelles réponses attendre.

Cela signifie qu'un fichier OAS bien rédigé équivaut à une documentation de référence d'API bien rédigée.

Lors de la rédaction de ce fichier, certaines parties peuvent devenir un peu compliquées. Par exemple, vous devrez peut-être documenter un seul endpoint avec différentes méthodes ou parfois des endpoints dupliqués.

J'ai rencontré et documenté ces deux cas d'utilisation. Ainsi, dans cet article, je vais vous montrer comment faire de même. Nous passerons en revue chaque cas d'utilisation avec des exemples de spécifications OpenAPI, et à la fin, je vous laisserai quelques conseils utiles pour documenter vos fichiers de spécifications OpenAPI.

## **Table des matières**

* [Prérequis](#heading-prerequisites)
  
* [Poser les bases](#heading-installation)
  
* [Cas d'utilisation 1 : Endpoints dupliqués](#heading-use-case-1-duplicate-endpoints)
  
* [Cas d'utilisation 2 : Comment documenter plusieurs méthodes HTTP](#heading-use-case-2-how-to-document-multiple-http-methods)
  
* [Conseils pour la documentation d'API](#heading-api-documentation-tips)
  
  * [Utiliser Markdown dans OpenAPI](#heading-use-markdown-in-openapi)
      
  * [Utiliser le champ operationId](#heading-use-the-operationid-field)
      
  * [Utiliser $ref pour les composants réutilisables](#heading-use-ref-for-reusable-components)
      
* [Conclusion](#heading-conclusion)
  

## Prérequis

Il y a quelques choses que vous devez savoir pour suivre les cas d'utilisation ci-dessous. Cela inclut :

1. [**Une connaissance de base des API et de la documentation d'API**](https://www.freecodecamp.org/news/how-apis-work/) : La familiarité avec la terminologie et la structure des API (par exemple, endpoints, méthodes, structure des requêtes/réponses) est essentielle pour comprendre comment un document de spécification OpenAPI (OAS) fonctionne.
  
2. [**Familiarité avec la spécification OpenAPI**](https://spec.openapis.org/oas/latest.html) : Compréhension de base de l'OAS, y compris son objectif, sa structure, etc.
  
3. **Accès à Swagger ou à d'autres outils de documentation OpenAPI** : Vous avez besoin d'outils comme l'[éditeur Swagger](https://editor-next.swagger.io/) ou [RapiDoc](https://rapidocweb.com/), qui vous permettront de tester et de visualiser les fichiers OpenAPI.
  

## **Poser les bases**

En programmation comme dans la vie, si vous pouvez déterminer que quelque chose est "complexe", cela signifie qu'il existe aussi une manière simpliste et régulière de le faire. Et c'est la même chose pour un fichier OAS.

Lors de la création de votre fichier de spécification, vous ne rencontrerez pas toujours les cas d'utilisation que nous aborderons bientôt. C'est pourquoi il est utile de savoir à quoi ressemble un fichier de spécification conventionnel.

Une spécification OpenAPI est un fichier lisible par l'homme et la machine, écrit en JSON ou YAML. Ci-dessous, un exemple de structure de fichier OAS au format YAML :

```yaml
paths:
  /users:
    get:
      summary: Obtenir une liste d'utilisateurs
      responses:
        '200':
          description: Une liste d'utilisateurs.
  /users/{userId}:
    get:
      summary: Obtenir les détails d'un seul utilisateur
      parameters:
 - name: userId
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Détails d'un seul utilisateur.
  /orders:
    get:
      summary: Obtenir une liste de commandes
      responses:
        '200':
          description: Une liste de commandes.
```

Voici une brève description de cette structure de fichier OAS :

1. **Paths** : La section `paths` vous permet de lister chaque endpoint ou URL avec lequel vous pouvez interagir dans cette API. Chaque chemin, tel que `/users` ou `/orders`, montre quel type de données vous pouvez obtenir ou envoyer à cette URL.
  
2. **Operations** : Sous chaque chemin, il y a une méthode ou opération, comme `GET`, qui nous indique ce que nous pouvons faire avec cet endpoint. Dans cet exemple, chaque chemin utilise `GET`, ce qui signifie que vous demandez des informations.
  
3. **Summary** : Chaque opération a un `summary` – une courte description expliquant ce que fait l'endpoint, comme "Obtenir une liste d'utilisateurs" ou "Obtenir les détails d'un seul utilisateur".
  
4. **Parameters** : Pour les chemins qui incluent des espaces réservés, comme `/users/{userId}`, vous verrez une section `parameters` expliquant quels détails sont requis.
  
5. **Responses** : Chaque opération inclut une section `responses`, qui liste les réponses possibles de l'API.
  

**NOTE** : Ceci n'est pas un fichier OAS complet. J'ai omis certaines informations précédentes à des fins d'explication.

Maintenant, plongeons dans les scénarios plus complexes.

## **Cas d'utilisation 1 : Endpoints dupliqués**

Lors du développement d'une API, vous pouvez créer un seul endpoint avec plusieurs variations. Selon le cas d'utilisation, vous pouvez vouloir que cet endpoint accepte plusieurs formats de données ou des paramètres spécifiques.

Lorsque vous rencontrez de tels scénarios et que vous souhaitez documenter la référence de l'API en utilisant une spécification OpenAPI, vous ne pourrez pas la répliquer exactement comme elle est dans la collection [Postman](https://postman.com/) (ou tout autre environnement de développement).

Si vous essayiez, vous obtiendriez cette erreur :

![Failed OpenAPI Spec](https://cdn.hashnode.com/res/hashnode/image/upload/v1730414590959/017c94c1-7e33-46c7-b572-b9ea03763e1f.png align="left")

La solution à ce problème est de consolider ces multiples variations sous une seule définition de chemin en regroupant les différentes requêtes et réponses en tant qu'**exemples**.

Dans l'exemple ci-dessous, vous avez une API qui possède un endpoint pour gérer l'enregistrement des sessions lors d'une conférence. Cet endpoint a diverses requêtes et réponses basées sur le type d'enregistrement (par exemple, Speaker, Attendee, ou VIP).

Dans une collection Postman, vous pouvez avoir chacun de ces endpoints dans un dossier séparé pour une identification et un test faciles.

![Postman collection](https://cdn.hashnode.com/res/hashnode/image/upload/v1730414608239/be94b45d-fb16-438f-9e7e-07cdc38c179d.png align="left")

Mais lors de la documentation de votre fichier de spécification, il devrait ressembler à ceci :

```yaml
openapi: 3.0.0
info:
  title: Conference Events API
  description: API pour gérer les inscriptions aux événements de conférences
  version: 1.0.0
paths:
  /register-session:
    post:
      tags:
        - Registration
      summary: S'inscrire à une session de conférence
      description: Inscrire un utilisateur pour une session spécifique en fonction de son rôle, avec des détails fournis pour chaque type d'enregistrement.
      operationId: registerSession
      requestBody:
        description: Inscrire un utilisateur pour une session à la conférence. Il accepte différents formats pour les inscriptions des participants, des intervenants ou des VIP.
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SessionRegistration'
            examples:
              Attendee:
                summary: S'inscrire en tant que participant
                value:
                  userType: Attendee
                  userId: 789
                  sessionId: 1234
                  preferences:
                    seating: General
                    accessLevel: Basic
              Speaker:
                summary: S'inscrire en tant qu'intervenant
                value:
                  userType: Speaker
                  userId: 456
                  sessionId: 1234
                  preferences:
                    seating: VIP
                    accessLevel: Full
                    presentationEquipment: Projector
              VIP:
                summary: S'inscrire en tant que VIP
                value:
                  userType: VIP
                  userId: 123
                  sessionId: 1234
                  preferences:
                    seating: Front Row
                    accessLevel: Full
                    exclusiveAccess: true
      responses:
        '200':
          description: Inscription réussie pour le participant, l'intervenant ou le VIP
          content:
            application/json:
              schema:
                type: object
                properties:
                  registrationId:
                    type: string
                  success:
                    type: boolean
              examples:
                Attendee:
                  summary: Réponse pour l'inscription d'un participant
                  value:
                    registrationId: att-456def
                    success: true
                Speaker:
                  summary: Réponse pour l'inscription d'un intervenant
                  value:
                    registrationId: spk-123abc
                    success: true
                VIP:
                  summary: Réponse pour l'inscription d'un VIP
                  value:
                    registrationId: vip-789ghi
                    success: true
components:
  schemas:
    SessionRegistration:
      type: object
      properties:
        userType:
          type: string
          description: Type d'utilisateur s'inscrivant (par exemple, participant, intervenant, VIP)
        userId:
          type: integer
          description: ID unique de l'utilisateur
        sessionId:
          type: integer
          description: ID unique de la session à laquelle s'inscrire
        preferences:
          type: object
          properties:
            seating:
              type: string
              description: Préférence de siège (par exemple, général, VIP, première rangée)
            accessLevel:
              type: string
              description: Niveau d'accès accordé (par exemple, basique, complet)
            presentationEquipment:
              type: string
              description: Équipement requis pour les intervenants (uniquement applicable aux intervenants)
            exclusiveAccess:
              type: boolean
              description: Accès exclusif pour les utilisateurs VIP
```

Dans ce fichier, vous avez un seul chemin `POST /register-session` qui capture tous les types d'enregistrement sans dupliquer les endpoints.

Voici une représentation visuelle de ce fichier OAS en utilisant l'[éditeur Swagger](https://editor-next.swagger.io/) :

![OpenAPI Spec Multiple Request Examples](https://cdn.hashnode.com/res/hashnode/image/upload/v1730414627353/eed5843b-f5f4-4e61-9126-51fd10e417c6.png align="left")

## **Cas d'utilisation 2 : Comment documenter plusieurs méthodes HTTP**

Un autre cas d'utilisation que vous pouvez rencontrer se produit lorsque vous avez le même endpoint mais avec différentes méthodes HTTP.

Cela arrive généralement parce que chaque méthode sert un objectif différent, même si elles partagent le même chemin.

Par exemple, une méthode **GET** récupère des informations sur une ressource, comme afficher les détails d'enregistrement d'un utilisateur pour une session de conférence.

D'autre part, une méthode **PATCH** met à jour des champs spécifiques pour cet enregistrement d'utilisateur, comme mettre à jour sa préférence de siège.

Puisque les méthodes `GET` et `PATCH` concernent la même ressource (`/register-session` dans notre exemple), la solution consiste à les regrouper sous le même chemin. Ainsi, vous documenterez deux méthodes distinctes pour un seul chemin.

Dans OpenAPI, chaque combinaison d'un chemin et d'une méthode est appelée une "opération". Regrouper les opérations qui partagent le même chemin aide à maintenir des documents plus clairs et mieux structurés.

En utilisant l'exemple de l'API des événements de conférence, voici à quoi devrait ressembler votre fichier OAS :

```yaml
openapi: 3.0.0
info:
  title: Conference Events API
  description: API pour gérer les inscriptions aux événements de conférences
  version: 1.0.0
paths:
  /register-session:
    get:
      tags:
        - Registration
      summary: Récupérer un enregistrement pour une session de conférence
      description: Récupérer les détails d'enregistrement pour un utilisateur spécifique, comme l'assignation de siège et le niveau d'accès.
      operationId: getSessionRegistration
      parameters:
        - in: query
          name: userId
          schema:
            type: integer
          required: true
          description: L'ID de l'utilisateur dont vous souhaitez récupérer l'enregistrement.
      responses:
        '200':
          description: Détails de l'enregistrement récupérés avec succès
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SessionRegistration'
              example:
                userId: 789
                sessionId: 1234
                preferences:
                  seating: General
                  accessLevel: Basic
                  exclusiveAccess: false

    patch:
      tags:
        - Registration
      summary: Mettre à jour un enregistrement pour une session de conférence
      description: Mettre à jour des champs spécifiques pour l'enregistrement de session d'un utilisateur, tels que le siège ou le niveau d'accès.
      operationId: updateSessionRegistration
      requestBody:
        description: Permet de mettre à jour des champs pour un enregistrement de session spécifique.
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateSessionPreferences'
            example:
              userId: 789
              preferences:
                seating: VIP
                accessLevel: Full
                exclusiveAccess: true
      responses:
        '200':
          description: Enregistrement mis à jour avec succès
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  message:
                    type: string
              example:
                success: true
                message: "Enregistrement mis à jour avec succès."
components:
  schemas:
    SessionRegistration:
      type: object
      properties:
        userId:
          type: integer
          description: ID unique de l'utilisateur
        sessionId:
          type: integer
          description: ID unique de la session
        preferences:
          type: object
          properties:
            seating:
              type: string
              description: Préférence de siège (par exemple, général, VIP, première rangée)
            accessLevel:
              type: string
              description: Niveau d'accès accordé (par exemple, basique, complet)
            exclusiveAccess:
              type: boolean
              description: Accès exclusif accordé à certains utilisateurs

    UpdateSessionPreferences:
      type: object
      properties:
        userId:
          type: integer
          description: ID unique de l'utilisateur
        preferences:
          type: object
          properties:
            seating:
              type: string
              description: Nouvelle préférence de siège (par exemple, VIP)
            accessLevel:
              type: string
              description: Niveau d'accès mis à jour (par exemple, complet)
            exclusiveAccess:
              type: boolean
              description: Préférence d'accès mise à jour (par exemple, vrai ou faux)
```

Dans ce fichier, vous avez un seul chemin `/register-session` avec plusieurs méthodes. Nous définissons un seul chemin, `/register-session`, et listons les méthodes `GET` et `PATCH` sous celui-ci. Cela garde la spécification propre, réduit la duplication et montre que ces méthodes concernent la même ressource.

Voici une représentation visuelle de ce fichier OAS en utilisant l'éditeur Swagger :

![Multiple methods in one operation in an OpenAPI spec](https://cdn.hashnode.com/res/hashnode/image/upload/v1730414663261/680dd222-8d36-41be-a73a-10a55771d906.png align="left")

## **Conseils pour la documentation d'API**

Lors de la création de spécifications OpenAPI, il existe quelques astuces et conseils utiles qui peuvent rendre votre fichier OAS plus lisible et plus facile à maintenir.

### **Utiliser Markdown dans OpenAPI**

Les spécifications OpenAPI permettent l'utilisation de Markdown dans le champ `description`. La version de Markdown utilisée dans OAS est appelée CommonMark, la même version utilisée dans GitHub.

Le formatage Markdown vous permet de rendre le texte plus visuellement attrayant et organisé. Vous pouvez ajouter des formats tels que des en-têtes, des listes, des blocs de code, du texte en gras, en italique, etc., ce qui peut rendre votre documentation plus facile à parcourir et plus accessible pour les lecteurs.

Par exemple, si vous devez mettre en évidence certaines parties du but d'un endpoint ou souligner des détails importants, Markdown vous permet de le faire naturellement.

Vous pouvez ajouter Markdown directement dans n'importe quel champ `description` du fichier OpenAPI, comme ceci :

```yaml
paths:
  /register-session:
    get:
      description: |
        ## Récupérer l'enregistrement de session
       Récupère les détails d'enregistrement pour un utilisateur spécifique.  
       - **Note :** Ces données incluent l'assignation de siège et le niveau d'accès.  
       - Exemple de réponse JSON : `{"userId": 789, "sessionId": 1234, "seating": "General"}`
      responses:
        '200':
          description: Détails de l'enregistrement récupérés avec succès
```

Lorsque cela est déployé sur des plateformes de documentation prises en charge comme [RapiDoc](https://rapidocweb.com/) ou [ReadMe](https://readme.com/), cela sera rendu magnifiquement avec tous vos styles Markdown intacts.

Voici une version déployée de cet exemple dans Readme :

![Markdown in description field on Readme](https://cdn.hashnode.com/res/hashnode/image/upload/v1730414669217/100bcde8-a25e-4eab-9102-5113476a334b.png align="left")

### **Utiliser le champ** `operationId`

Le champ `operationId` est un champ facultatif dans les spécifications OpenAPI qui attribue un nom unique à chaque opération d'API.

C'est un identifiant que vous pouvez utiliser pour appeler des méthodes spécifiques lors de l'intégration avec des SDK ou lors de la liaison entre les parties de votre documentation.

En utilisant efficacement `operationId`, vous facilitez grandement la référence des développeurs à des actions spécifiques dans l'API, ce qui est particulièrement utile lorsque l'API est complexe ou possède plusieurs endpoints.

Placez `operationId` à l'intérieur de chaque bloc de méthode HTTP pour lui donner un identifiant unique. Par exemple :

```yaml
paths:
  /register-session:
    get:
      operationId: getSessionRegistration
      description: Récupérer un enregistrement pour une session de conférence
      responses:
        '200':
          description: Enregistrement récupéré avec succès
    patch:
      operationId: updateSessionRegistration
      description: Mettre à jour un enregistrement pour une session de conférence
      responses:
        '200':
          description: Enregistrement mis à jour avec succès
```

Avec `operationId`, les développeurs peuvent se référer directement à `getSessionRegistration` ou `updateSessionRegistration` en tant qu'appels de fonction dans le code ou les clients API.

### **Utiliser** `$ref` pour les composants réutilisables

Le mot-clé `$ref` dans OpenAPI vous permet de créer et de réutiliser des composants dans votre fichier de spécification. Cette technique est particulièrement utile lorsque vous avez des corps de requête, des réponses ou des paramètres similaires répétés dans plusieurs endpoints.

En définissant des composants en un seul endroit et en les référençant selon les besoins, vous évitez la redondance, réduisez les erreurs et facilitez les mises à jour.

Ainsi, au lieu de mettre à jour le même paramètre à plusieurs endroits, vous le mettez à jour une fois dans le composant réutilisable, et chaque endpoint l'utilisant reçoit la mise à jour.

Pour l'utiliser, définissez d'abord le composant réutilisable dans la section des composants de votre fichier OpenAPI, puis référencez-le ailleurs en utilisant `$ref` :

```yaml
components:
  schemas:
    RegistrationDetails:
      type: object
      properties:
        userId:
          type: integer
        sessionId:
          type: integer
        seating:
          type: string
paths:
  /register-session:
    post:
      summary: S'inscrire pour une session
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RegistrationDetails'
      responses:
        '201':
          description: Inscription réussie pour la session
```

Dans ce fichier, `RegistrationDetails` est défini une fois et est référencé en utilisant le mot-clé `$ref` dans l'opération `/register-session`.

## **Conclusion**

Dans cet article, vous avez appris comment résoudre certains cas d'utilisation complexes que vous pourriez rencontrer lors de la documentation de votre référence d'API en utilisant une spécification OpenAPI. Nous avons passé en revue ce qu'il faut faire lorsque vous avez un seul endpoint avec plusieurs méthodes ou des endpoints dupliqués.

Créer votre référence d'API sans un fichier de spécification OpenAPI est une approche manuelle qui peut devenir redondante si vous devez la répliquer sur diverses plateformes. Mais en vous appuyant sur les conseils de l'article, vous êtes sûr de créer de meilleures spécifications OpenAPI, plus efficaces et plus réutilisables. Et celles-ci, à leur tour, mèneront à une meilleure documentation d'API.