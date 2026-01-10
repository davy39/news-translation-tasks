---
title: Comment étendre les opérations CRUD pour les aligner sur les flux de travail
  métier
subtitle: ''
author: Tim Kleier
co_authors: []
series: null
date: '2025-09-10T15:39:44.823Z'
originalURL: https://freecodecamp.org/news/extend-crud-operations-to-align-with-business-workflows
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757518255485/8e727e36-d22a-42d9-b1a7-98d3ca5eae35.png
tags:
- name: crud
  slug: crud
- name: API
  slug: api
- name: Backend Development
  slug: backend-development
seo_title: Comment étendre les opérations CRUD pour les aligner sur les flux de travail
  métier
seo_desc: 'Most developers are introduced to databases and APIs through a simple pattern:
  CRUD—Create, Read, Update, Delete. It seems like the perfect abstraction. With just
  four operations, you can model almost anything. Tutorials use it. Frameworks generate
  i...'
---

La plupart des développeurs découvrent les bases de données et les API via un modèle simple : le CRUD — Create, Read, Update, Delete (Créer, Lire, Mettre à jour, Supprimer). Cela semble être l'abstraction parfaite. Avec seulement quatre opérations, vous pouvez modéliser presque n'importe quoi. Les tutoriels l'utilisent. Les Frameworks le génèrent. Nous l'enseignons aux débutants comme la base du travail avec les données.

Mais dès que vous dépassez les applications basiques, le CRUD commence à montrer ses limites.

Les systèmes du monde réel ne se contentent pas de « mettre à jour » ou de « supprimer » des choses. Dans un système de demande de prêt, par exemple, les emprunteurs « soumettent » des demandes, les agents de crédit les « approuvent » ou les « rejettent », et les demandes sont finalement « archivées ». Ce ne sont pas des opérations CRUD génériques : ce sont des **actions spécifiques au domaine** qui portent un sens.

Et c'est là le problème : le CRUD masque la signification de nos systèmes derrière des verbes vagues. Les API REST héritent du même problème, mappant les verbes HTTP sur le CRUD tout en échouant à exprimer clairement les flux de travail réels.

Dans cet article, nous explorerons :

* Pourquoi le CRUD fonctionne bien pour les applications simples mais devient un anti-pattern à grande échelle
    
* Comment des concepts comme l'**upsert**, l'**archivage** et les **opérations en masse (bulk)** révèlent ses failles
    
* Pourquoi REST ne résout pas ces problèmes
    
* Comment concevoir des API autour des actions de domaine et des flux de travail à la place.
    

À la fin, vous verrez le CRUD pour ce qu'il est réellement : un outil pédagogique, pas une philosophie de conception.

## Table des matières

* [Qu'est-ce que le CRUD ?](#heading-qu-est-ce-que-le-crud)
    
* [Étendre le CRUD : Upsert, Archive, Bulk](#heading-etendre-le-crud-upsert-archive-bulk)
    
* [Rompre avec le CRUD : Actions de domaine](#heading-rompre-avec-le-crud-actions-de-domaine)
    
* [Rompre avec le CRUD : Autorisation de domaine](#heading-rompre-avec-le-crud-autorisation-de-domaine)
    
* [Alternative au CRUD : S'aligner sur les flux de travail](#heading-alternative-au-crud-s-aligner-sur-les-flux-de-travail)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que le CRUD ?

**Create, Read, Update, Delete** — ce sont les quatre opérations de base que nous effectuons sur les données dans une base de données.

* **Create** – ajoute un nouvel enregistrement.
    
* **Read** – récupère un enregistrement existant (ou une liste d'enregistrements).
    
* **Update** – modifie un ou plusieurs champs dans un enregistrement.
    
* **Delete** – supprime un enregistrement.
    

Par exemple, dans une application Node.js + Express typique gérant des utilisateurs :

```javascript
// Create a user
app.post('/users', createUser);

// Read a user
app.get('/users/:id', getUser);

// Update a user
app.put('/users/:id', updateUser);

// Delete a user
app.delete('/users/:id', deleteUser);
```

Cela correspond directement au SQL sous-jacent :

```sql
INSERT INTO users (...);
SELECT * FROM users WHERE id = ...;
UPDATE users SET ... WHERE id = ...;
DELETE FROM users WHERE id = ...;
```

Et c'est le CRUD dans sa forme la plus pure — quatre opérations qui peuvent décrire presque n'importe quelle interaction avec une base de données.

## Étendre le CRUD : Upsert, Archive, Bulk

Les développeurs réalisent rapidement que le CRUD ne suffit pas, ils inventent donc des extensions :

* **Upsert** : un mélange de « update » et « insert ». Si l'enregistrement existe, on le met à jour ; sinon, on le crée.
    
* **Archive** : au lieu de supprimer un enregistrement, nous effectuons une « suppression logique » (soft delete) ou nous le marquons comme inactif pour que l'historique reste intact.
    
* **Opérations en masse (Bulk operations)** : exécuter create, update ou delete sur de nombreux enregistrements à la fois pour plus d'efficacité.
    

Ces extensions résolvent des problèmes réels, mais elles étirent le modèle simple du CRUD. Nous devons maintenant faire la distinction entre les actions sur une ressource unique et les actions en masse. Et nous devons également prendre en compte les préoccupations techniques des upserts et des suppressions logiques.

## Rompre avec le CRUD : Actions de domaine

Le domaine technique lui-même étire considérablement le CRUD, mais les préoccupations du domaine métier le brisent entièrement. Prenons un système de demande de prêt :

* Un emprunteur ne « crée » pas et ne « met pas à jour » une demande — il la commence, la soumet ou la retire.
    
* Un agent de crédit ne « met pas à jour » une demande — il l'examine, l'approuve ou la rejette.
    
* Les demandes ne sont pas « supprimées » — elles sont généralement archivées pour qu'il y ait une trace pour la conformité.
    

Si nous essayons de modéliser cela comme du simple CRUD, le sens se perd :

```http
PATCH /applications/123 { "status": "approved" }
```

Techniquement, cela fonctionne. Mais que signifie réellement « update » ici ? La demande a-t-elle été soumise, rejetée ou archivée ? On ne peut pas le dire à partir de l'appel API.

Le problème central : le CRUD masque l'intention derrière un langage technique générique. Les processus métier réels sont exprimés sous forme d'actions spécifiques au domaine, et non de mises à jour ou de suppressions génériques.

## Rompre avec le CRUD : Autorisation de domaine

Le CRUD n'obscurcit pas seulement l'intention — il crée également des failles d'autorisation. En reprenant l'exemple de la demande de prêt :

* Seuls les agents de crédit devraient approuver les demandes.
    
* Les emprunteurs ne devraient pouvoir modifier que leurs propres informations ou retirer leurs demandes.
    

Si l'action « approuver » est simplement modélisée comme une mise à jour générique, le système ne peut pas distinguer les rôles sans vérifications supplémentaires. Une règle d'autorisation naïve comme « cet utilisateur peut-il mettre à jour ? » permet soudainement aux emprunteurs d'effectuer des actions réservées aux agents.

Ce décalage entre les verbes techniques et les règles métier peut entraîner :

* Des problèmes de sécurité — actions non autorisées effectuées par le mauvais utilisateur.
    
* Des problèmes d'audit — il n'est pas clair qui a fait quoi, et quand.
    
* Une confusion dans le flux de travail — les transitions d'état se perdent dans des mises à jour génériques.
    

La solution : traiter chaque action de domaine comme son propre appel API avec des règles d'autorisation explicites :

```http
POST /applications/123/approve   # Accessible uniquement aux agents de crédit
POST /applications/123/withdraw  # Accessible uniquement à l'emprunteur
```

En modélisant les actions au lieu des opérations CRUD, l'intention et les permissions sont claires, réduisant ainsi les bugs et les risques de sécurité.

## Alternative au CRUD : S'aligner sur les flux de travail

Les applications du monde réel suivent des flux de travail — des séquences d'états par lesquels une ressource passe. Reprenons notre exemple de demande de prêt :

![Loan Application Workflow Diagram](https://cdn.hashnode.com/res/hashnode/image/upload/v1757257665063/f26ce4c4-afee-4b03-8ddc-bdb724aa9850.png align="center")

Voici à quoi pourraient ressembler les points de terminaison (endpoints) de l'API correspondants :

```http
# Actions de l'emprunteur
POST /applications/123/submit       # Draft → Submitted
POST /applications/123/withdraw     # Draft/Submitted → Closed

# Actions de l'agent de crédit
POST /applications/123/approve      # Submitted → Approved
POST /applications/123/reject       # Submitted → Rejected

# Actions système/administrateur
POST /applications/123/close        # Approved/Rejected → Closed

# Effet secondaire : génération d'un prêt (après Approved)
POST /loans
{
  "applicationId": "123",
  "amount": 50000,
  "borrowerId": "456",
  "terms": { ... }
}
```

À ce stade, nos appels API sont presque entièrement en dehors du modèle CRUD — le seul qui ressemble à une action CRUD est la génération d'un prêt, qui ressemble à un « create ». Dans les coulisses, nous utiliserons toujours des instructions `INSERT`, `SELECT` et `UPDATE` en SQL, mais au niveau de l'API, nous nous alignons sur le flux de travail métier réel. Grâce à cela, nous sommes en mesure de prendre facilement en charge les points suivants :

1. **Les actions reflètent l'intention métier** — chaque appel API correspond à une tâche du monde réel comme soumettre, approuver ou retirer.
    
2. **Autorisation intégrée** — les points de terminaison séparent clairement les responsabilités de l'emprunteur, de l'agent de crédit et de l'administrateur.
    
3. **Auditabilité et application du flux de travail** — les transitions d'état sont explicites et les transitions invalides sont empêchées.
    
4. **Effets secondaires contrôlés** — la génération de prêts, les notifications et les processus en aval sont gérés de manière délibérée.
    

## Conclusion

En s'éloignant du CRUD pour modéliser les actions de domaine à la place, notre API s'aligne sur les flux de travail métier réels, communique clairement l'intention et applique naturellement les règles et l'autorisation. Les transitions d'état, les effets secondaires et l'audit deviennent explicites, réduisant les erreurs et les risques de sécurité. Bien que le CRUD alimente toujours les opérations de base de données sous-jacentes, penser en termes d'actions et de flux de travail garantit que le système se comporte comme l'entreprise l'attend.