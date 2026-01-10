---
title: Comment exécuter des migrations de base de données dans Kubernetes – Différentes
  approches avec exemples
subtitle: ''
author: Alex Pliutau
co_authors: []
series: null
date: '2024-10-02T15:09:50.933Z'
originalURL: https://freecodecamp.org/news/how-to-run-database-migrations-in-kubernetes
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727685813983/f4672022-9a38-49c9-a252-96f40181fac1.jpeg
tags:
- name: Kubernetes
  slug: kubernetes
- name: Go Language
  slug: go
- name: Databases
  slug: databases
- name: Helm
  slug: helm
seo_title: Comment exécuter des migrations de base de données dans Kubernetes – Différentes
  approches avec exemples
seo_desc: 'In the era of Microservices and Kubernetes, managing database migrations
  has become more complex than ever. Traditional methods of running migrations during
  application startup are no longer sufficient.

  This article explores various approaches to han...'
---

À l'ère des microservices et de Kubernetes, la gestion des migrations de base de données est devenue plus complexe que jamais. Les méthodes traditionnelles d'exécution des migrations lors du démarrage de l'application ne sont plus suffisantes.

Cet article explore diverses approches pour gérer les migrations de base de données dans un environnement Kubernetes, en mettant l'accent sur l'outillage Go. Vous tirerez le meilleur parti de cet article si vous avez déjà une certaine expérience avec Go, Kubernetes et les bases de données relationnelles.

## Table des matières

* [Le défi des migrations dans Kubernetes](#heading-le-defi-des-migrations-dans-kubernetes)
    
* [Outils de migration populaires pour Golang](#heading-outils-de-migration-populaires-pour-golang)
    
* [Exécuter les migrations à l'intérieur de l'application](#heading-executer-les-migrations-a-linterieur-de-lapplication)
    
* [Exécuter les migrations dans initContainers](#heading-executer-les-migrations-dans-initcontainers)
    
* [Exécuter les migrations en tant que Kubernetes Job](#heading-executer-les-migrations-en-tant-que-kubernetes-job)
    
* [Hooks Helm](#heading-hooks-helm)
    
* [Bonnes pratiques pour les migrations Kubernetes](#heading-bonnes-pratiques-pour-les-migrations-kubernetes)
    
* [Conclusion](#heading-conclusion)
    
* [Ressources](#heading-ressources)
    

## Le défi des migrations dans Kubernetes

Kubernetes introduit de nouveaux défis pour les migrations de base de données :

* Plusieurs réplicas démarrant simultanément. Ceux-ci peuvent déclencher la même migration deux fois, ce qui peut introduire des verrous de base de données.
    
* Séparation des préoccupations entre la logique de l'application et celle de la migration. Cela signifie qu'il est préférable de pouvoir exécuter ou annuler des migrations sans redéployer votre application.
    

## Outils de migration populaires pour Golang

Comme je l'ai mentionné dans un autre [post](https://packagemain.tech/i/149097592/database-migrations), il existe plusieurs outils différents que vous pouvez utiliser pour gérer vos migrations. Ils sont assez similaires, donc je n'ai personnellement pas de préférence marquée pour l'un ou l'autre. Je voulais simplement proposer quelques options pour que vous sachiez quels sont les outils populaires.

1. [**golang-migrate**](https://github.com/golang-migrate/migrate)
    

* Largement utilisé et supporte de nombreuses bases de données.
    
* CLI et API simples.
    
* Supporte diverses sources de migration (fichiers locaux, S3, Google Storage).
    

2. [**goose**](https://github.com/pressly/goose)
    

* Supporte les principales bases de données SQL.
    
* Permet des migrations écrites en Go pour des scénarios complexes.
    
* Schémas de versionnage flexibles.
    

3. [**atlas**](https://atlasgo.io/)
    

* Puissant outil de gestion de schéma de base de données.
    
* Supporte les migrations déclaratives et versionnées.
    
* Offre des vérifications d'intégrité et du linting de migration.
    
* Fournit des GitHub Actions et un fournisseur Terraform.
    

## Exécuter les migrations à l'intérieur de l'application

Une implémentation naïve consisterait à exécuter le code de la migration directement à l'intérieur de votre fonction principale avant de démarrer votre serveur.

**Exemple utilisant golang-migrate :**

```go
package main

import (
    "database/sql"
    "fmt"
    "log"
    "net/http"

    "github.com/golang-migrate/migrate/v4"
    "github.com/golang-migrate/migrate/v4/database/postgres"
    _ "github.com/golang-migrate/migrate/v4/source/file"
    _ "github.com/lib/pq"
)

func main() {
    // Paramètres de connexion à la base de données
    url := "postgres://user:pass@localhost:5432/dbname"

    // Connexion à la base de données
    db, err := sql.Open("postgres", url)
    if err != nil {
        log.Fatalf("could not connect to database: %v", err)
    }
    defer db.Close()

    // Exécution des migrations
    if err := runMigrations(db); err != nil {
        log.Fatalf("could not run migrations: %v", err)
    }

    // Lancer l'application, par exemple démarrer le serveur
    if err := http.ListenAndServe(":8080", nil); err != nil {
        log.Fatalf("server failed to start: %v", err)
    }
}

func runMigrations(db *sql.DB) error {
    driver, err := postgres.WithInstance(db, &postgres.Config{})
    if err != nil {
        return fmt.Errorf("could not create database driver: %w", err)
    }

    m, err := migrate.NewWithDatabaseInstance(
        "file://migrations", // Chemin vers vos fichiers de migration
        "postgres",          // Type de base de données
        driver,
    )
    if err != nil {
        return fmt.Errorf("could not create migrate instance: %w", err)
    }

    if err := m.Up(); err != nil && err != migrate.ErrNoChange {
        return fmt.Errorf("could not run migrations: %w", err)
    }

    log.Println("migrations completed successfully")
    return nil
}
```

Cependant, cela pourrait causer différents problèmes, comme des migrations lentes et le fait que Kubernetes considère que le pod n'a pas démarré avec succès et l'arrête donc. Vous pourriez exécuter ces migrations dans une routine Go, mais comment gérez-vous les échecs dans ce cas ?

Dans les cas où plusieurs pods sont créés en même temps, vous auriez un problème potentiel de concurrence.

Cela signifie également que vos migrations doivent se trouver à l'intérieur de votre image Docker.

Malgré ses inconvénients, cette approche peut bien fonctionner pour des changements de base de données rapides et stables ainsi que pour de petits projets.

## **Exécuter les migrations dans initContainers**

En utilisant des [initContainers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) dans votre déploiement Kubernetes, la migration s'exécutera avant le démarrage du conteneur de l'application principale. C'est une bonne première solution lorsque la mise à l'échelle n'est pas encore un problème.

Si l'initContainer échoue, le déploiement blue/green de Kubernetes n'ira pas plus loin et vos pods précédents resteront en place. Cela évite d'avoir une version plus récente du code sans la migration prévue.

**Exemple :**

```yaml
initContainers:
  - name: migrations
    image: migrate/migrate:latest
    command: ['/migrate']
    args: ['-source', 'file:///migrations', '-database','postgres://user:pass@db:5432/dbname', 'up']
```

Cette approche peut bien fonctionner pour des changements de base de données rapides et stables pour des déploiements avec un seul Pod. Et elle sépare déjà les couches d'application et de migration.

## **Exécuter les migrations en tant que Kubernetes Job**

Vous pourriez créer un [Kubernetes Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) qui exécute vos migrations, et déclencher ce job pendant le processus de déploiement avant de déployer l'application.

**Exemple :**

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: db-migrate
spec:
  template:
    spec:
      containers:
      - name: migrate
        image: your-migration-image:latest
        command: ['/app/migrate']
```

You can also combine it with initContainers, making sure that the pod starts only when the job is successful.

```yaml
initContainers:
  - name: migrations-wait
    image: ghcr.io/groundnuty/k8s-wait-for:v2.0
    args:
      - "job"
      - "my-migration-job"
```

Cette approche peut résoudre les problèmes liés aux réplicas multiples mentionnés ci-dessus.

## Hooks Helm

Si vous utilisez Helm, il possède des [hooks](https://helm.sh/docs/topics/charts_hooks/) que vous pouvez utiliser pour exécuter des migrations lors de l'installation ou de la mise à jour d'un chart. Il vous suffit de définir un hook pre-install ou pre-upgrade dans votre chart Helm.

**pre-install-hook.yaml :**

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: {{ include "mychart.fullname" . }}-migrations
  annotations:
    "helm.sh/hook": pre-install,pre-upgrade
    "helm.sh/hook-weight": "-5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  template:
    spec:
      containers:
        - name: migrations
          image: your-migrations-image:tag
          command: ["./run-migrations.sh"]
```

Dans cet exemple, le hook pre-install s'exécute après le rendu des templates, mais avant que toute ressource ne soit créée dans Kubernetes.

Ceci ne fonctionne bien sûr que si vous utilisez Helm, ce qui signifie que vous devrez trouver une autre solution si vous décidez de ne pas l'utiliser.

## **Bonnes pratiques pour les migrations Kubernetes**

Découpler les migrations du code de l'application :

1. Créez une image Docker séparée pour les migrations. Cela garantit que la logique de migration est encapsulée et n'interfère pas avec la base de code de l'application.
    
2. Utilisez des outils comme Atlas pour gérer les migrations de manière indépendante. Des outils comme Atlas offrent des fonctionnalités pour automatiser les processus de migration, la planification et l'annulation (rollback).
    

Utiliser le contrôle de version pour les migrations :

1. Stockez les fichiers de migration dans votre dépôt Git. Cela garantit un historique complet des modifications de migration, ce qui facilite le suivi et l'annulation des changements.
    
2. Utilisez un versionnage séquentiel ou basé sur l'horodatage. Le versionnage séquentiel garantit l'ordre correct des migrations, ce qui est très important pour les bases de données relationnelles.
    

Assurer l'idempotence des migrations :

1. Assurez-vous que les migrations peuvent être exécutées plusieurs fois sans effets secondaires. Des migrations idempotentes empêchent la corruption accidentelle des données ou les incohérences si une migration est exécutée plusieurs fois.
    

Avoir une stratégie d'annulation (rollback)

1. Implémentez et testez des procédures d'annulation pour chaque migration. Avoir une stratégie d'annulation garantit que vous pouvez revenir en arrière si une migration échoue ou cause des problèmes inattendus.
    

Effectuer une surveillance et une journalisation

1. Utilisez des outils comme Atlas Cloud pour avoir une visibilité sur l'historique des migrations. Atlas Cloud fournit des journaux détaillés et l'historique des migrations, facilitant le suivi des modifications et le dépannage.
    

## **Conclusion**

La gestion des migrations de base de données dans un environnement Kubernetes nécessite une planification et une exécution minutieuses.

En tirant parti d'outils comme golang-migrate, goose ou atlas, et en suivant les bonnes pratiques, vous pouvez créer des stratégies de migration robustes, évolutives et maintenables.

N'oubliez pas de découpler les migrations du code de l'application, d'utiliser le contrôle de version et de mettre en œuvre une surveillance appropriée pour assurer une évolution fluide de la base de données dans votre architecture basée sur Kubernetes.

### **Ressources**

* [Découvrez plus d'articles de packagemain.tech](https://packagemain.tech/p/database-migrations-in-kubernetes)
    
* [Hooks Helm](https://helm.sh/docs/topics/charts_hooks/)