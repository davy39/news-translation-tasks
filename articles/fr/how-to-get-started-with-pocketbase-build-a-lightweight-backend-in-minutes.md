---
title: 'Comment débuter avec PocketBase : Créez un backend léger en quelques minutes'
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-11-14T18:11:55.251Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-pocketbase-build-a-lightweight-backend-in-minutes
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1763143867523/1a4c8cd4-629f-4dd7-8a82-5b6d0d34d90e.png
tags:
- name: backend
  slug: backend
- name: golang
  slug: golang
- name: Go Language
  slug: go
seo_title: 'Comment débuter avec PocketBase : Créez un backend léger en quelques minutes'
seo_desc: 'If you’re a developer looking for a simple, fast, and self-hosted backend,
  PocketBase might be exactly what you need.

  It’s an open-source backend written in Go that lets you set up a complete backend
  with database, authentication, file storage, and r...'
---


Si vous êtes un développeur à la recherche d'un backend simple, rapide et auto-hébergé, [PocketBase](https://github.com/pocketbase/pocketbase) pourrait être exactement ce qu'il vous faut.

Il s'agit d'un backend open-source écrit en Go qui vous permet de mettre en place un backend complet avec base de données, authentification, stockage de fichiers et mises à jour en temps réel, le tout dans un seul fichier exécutable.

Dans ce guide, nous explorerons ce qui rend PocketBase spécial, comment le configurer et comment vous pouvez le déployer dans le cloud.

## Au programme :

* [Qu'est-ce que PocketBase ?](#heading-quest-ce-que-pocketbase)
    
* [Pourquoi les développeurs aiment PocketBase](#heading-pourquoi-les-developpeurs-aiment-pocketbase)
    
* [Comment installer PocketBase](#heading-comment-installer-pocketbase)
    
* [Étendre PocketBase avec JavaScript](#heading-etendre-pocketbase-avec-javascript)
    
* [Utiliser les SDK pour interagir avec PocketBase](#heading-utiliser-les-sdk-pour-interagir-avec-pocketbase)
    
* [Auto-hébergement de PocketBase avec Sevalla](#heading-auto-hebergement-de-pocketbase-avec-sevalla)
    
* [Sécurité et nature Open Source](#heading-securite-et-nature-open-source)
    
* [Quand utiliser PocketBase](#heading-quand-utiliser-pocketbase)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que PocketBase ?

PocketBase est un backend tout-en-un qui fournit tout ce dont vous avez besoin pour alimenter une application web ou mobile moderne, éliminant ainsi le besoin d'une infrastructure complexe.

Il comprend une base de données [SQLite](https://sqlite.org/) intégrée, des abonnements en temps réel, une gestion des fichiers et des utilisateurs, un tableau de bord d'administration épuré et une API de style REST.

Puisqu'il s'exécute à partir d'un seul fichier, vous pouvez le déployer presque n'importe où, d'un VPS à votre machine locale ou même un Raspberry Pi.

Il est conçu pour les développeurs qui veulent à la fois contrôle et simplicité. Vous n'avez pas besoin de gérer des serveurs séparés pour l'authentification, le stockage et les points de terminaison d'API. PocketBase gère tout cela nativement. Vous pouvez l'utiliser comme un backend autonome ou l'intégrer dans votre application Go pour créer une solution personnalisée.

## Pourquoi les développeurs aiment PocketBase

[PocketBase](https://pocketbase.io/docs/how-to-use/) se concentre sur la rapidité et la simplicité. Vous n'avez pas besoin d'installer plusieurs packages ou services.

Une fois téléchargé, vous pouvez le lancer avec une seule commande. Il lancera ensuite un tableau de bord d'administration basé sur le web.

![PocketBase dashboard](https://cdn.hashnode.com/res/hashnode/image/upload/v1762853066915/e2f3af60-0a75-4b76-b55f-613b67b3e783.png align="center")

La base de données est construite avec SQLite, ce qui signifie que les données sont stockées localement par défaut, mais vous pouvez utiliser des extensions pour la connecter à vos flux de travail existants ou à un stockage cloud.

Un autre avantage majeur est ses capacités en temps réel. Chaque modification dans la base de données peut être diffusée instantanément aux clients connectés via des abonnements WebSocket. Cela le rend parfait pour créer des applications telles que des systèmes de chat, des tableaux de bord et des outils de collaboration nécessitant des mises à jour instantanées.

## Comment installer PocketBase

Lancer PocketBase prend moins d'une minute. Vous pouvez télécharger un [exécutable pré-construit](https://pocketbase.io/docs/) à partir de la page officielle des versions.

Il prend en charge toutes les plateformes majeures, y compris Windows, macOS et Linux.

Une fois téléchargé, extrayez l'archive et accédez au dossier dans votre terminal. Exécutez la commande suivante :

```python
./pocketbase serve
```

Cette commande démarre un serveur local et lance le tableau de bord d'administration à l'adresse `http://127.0.0.1:8090/_/`. De là, vous pouvez créer des collections, ajouter des utilisateurs, télécharger des fichiers et gérer les données. Il n'y a pas d'assistant de configuration ni d'installation de dépendances – tout est autonome à l'intérieur de ce binaire unique.

Si vous êtes un développeur Go, vous pouvez également installer PocketBase en tant que module Go et l'utiliser directement dans votre projet pour créer une logique personnalisée ou étendre l'API existante.

### Utiliser PocketBase comme un Framework Go

PocketBase peut agir comme un Framework Go, vous permettant de construire votre propre logique backend tout en gardant tout dans un seul fichier. Voici un exemple simple qui montre comment vous pouvez l'étendre avec une route personnalisée.

```python
package main

import (
    "log"
    "github.com/pocketbase/pocketbase"
    "github.com/pocketbase/pocketbase/core"
)
func main() {
    app := pocketbase.New()
    app.OnServe().BindFunc(func(se *core.ServeEvent) error {
        se.Router.GET("/hello", func(re *core.RequestEvent) error {
            return re.String(200, "Hello world!")
        })
        return se.Next()
    })
    if err := app.Start(); err != nil {
        log.Fatal(err)
    }
}
```

Une fois le fichier prêt, exécutez ces commandes :

```python
go mod init myapp && go mod tidy
go run main.go serve
```

Vous aurez maintenant un backend fonctionnel avec à la fois le tableau de bord PocketBase et votre point de terminaison personnalisé `/hello` disponibles en même temps.

Cela rend PocketBase flexible : vous pouvez l'utiliser comme un backend prêt à l'emploi ou comme partie d'un projet Go plus complexe.

## Étendre PocketBase avec JavaScript

PocketBase inclut un moteur JavaScript intégré qui vous permet d'étendre son comportement sans modifier ni recompiler le code Go. Cela facilite l'ajout de logique personnalisée, de validation, d'automatisation et de flux de travail pilotés par les événements directement dans votre backend.

Vous pouvez créer des fichiers JavaScript dans le dossier `pb_hooks`, et PocketBase les chargera et les exécutera automatiquement. Ces scripts peuvent écouter des événements tels que la création d'enregistrements, les mises à jour, l'authentification, et plus encore.

Voici un exemple simple qui envoie un e-mail de bienvenue chaque fois qu'un nouvel utilisateur s'inscrit.

Créez un fichier nommé `pb_hooks/user_email.js` dans votre répertoire PocketBase :

```javascript
/// <reference path="../pb_data/types.d.ts" />

onRecordAfterCreate("users", async (e) => {
    const user = e.record;

    console.log("New user registered:", user.email);

    // Exemple : envoyer un e-mail de bienvenue via une API tierce
    const emailResponse = await $http.send({
        url: "https://api.example.com/send-email",
        method: "POST",
        body: JSON.stringify({
            to: user.email,
            subject: "Welcome to our app!",
            message: `Hi ${user.username}, thanks for signing up!`
        }),
        headers: {
            "Content-Type": "application/json"
        }
    });

    console.log("Email status:", emailResponse.status);
});
```

Ce script s'exécute automatiquement chaque fois qu'un nouvel enregistrement est créé dans la collection `users`. Il récupère l'e-mail de l'utilisateur, le consigne dans les logs et utilise le client HTTP intégré de PocketBase (`$http`) pour appeler un service de messagerie externe.

Vous pouvez utiliser le même modèle pour valider les données avant de les enregistrer, déclencher des webhooks, bloquer des actions ou mettre à jour des enregistrements liés. Puisque tout s'exécute à l'intérieur de PocketBase, vous n'avez pas besoin de serveurs ou de fonctions supplémentaires pour automatiser la logique backend.

Cela le rend accessible aux équipes qui ne sont pas forcément à l'aise avec Go mais qui souhaitent tout de même ajouter une logique dynamique à leur backend. Vous trouverez plus de détails dans la documentation officielle sous la section « [Extend with JavaScript](https://pocketbase.io/docs/js-overview/) ».

## Utiliser les SDK pour interagir avec PocketBase

Pour faciliter la communication avec votre backend, PocketBase fournit des SDK officiels pour JavaScript et Dart.

Le SDK JavaScript fonctionne bien pour les projets basés sur le navigateur ou Node.js, tandis que le SDK Dart est idéal pour les applications mobiles construites avec Flutter. Les deux SDK offrent un moyen simple de se connecter, d'authentifier les utilisateurs et d'effectuer des opérations CRUD sans écrire manuellement des requêtes HTTP.

Par exemple, en JavaScript, vous pouvez vous connecter et récupérer des données comme ceci :

```python
import PocketBase from 'pocketbase'

const pb = new PocketBase('http://127.0.0.1:8090')
const records = await pb.collection('posts').getList(1, 20)
console.log(records)
```

Cette simplicité vous permet de vous concentrer sur la construction de votre frontend pendant que PocketBase gère l'authentification, les opérations de base de données et les mises à jour en temps réel.

## Auto-hébergement de PocketBase avec Sevalla

Lorsque vous êtes prêt à passer au-delà des tests, PocketBase vous offre deux options. Vous pouvez l'auto-héberger en utilisant votre propre infrastructure ou utiliser leur version cloud gérée sur [Pocketbase.io](https://pocketbase.io/).

L'auto-hébergement vous donne un contrôle total et est généralement préféré par les équipes techniques qui souhaitent conserver les données sensibles en interne.

Vous pouvez choisir n'importe quel fournisseur cloud, comme AWS, DigitalOcean ou d'autres pour configurer PocketBase. Mais je vais utiliser Sevalla.

[Sevalla](https://sevalla.com/) est un fournisseur PaaS conçu pour les développeurs et les équipes de développement qui déploient des fonctionnalités et des mises à jour en permanence de la manière la plus efficace possible. Il propose l'hébergement d'applications, de bases de données, de stockage d'objets et l'hébergement de sites statiques pour vos projets.

J'utilise Sevalla pour deux raisons :

* Chaque plateforme vous facturera la création d'une ressource cloud. Sevalla offre un crédit de 50 $ à utiliser, nous n'aurons donc aucun coût pour cet exemple.
    
* Sevalla dispose d'un [template pour PocketBase](https://docs.sevalla.com/templates/overview), ce qui simplifie l'installation manuelle et la configuration de chaque ressource nécessaire à l'installation.
    

[Connectez-vous](https://app.sevalla.com/login) à Sevalla et cliquez sur Templates. Vous pouvez voir PocketBase parmi les modèles.

![Sevalla Templates](https://cdn.hashnode.com/res/hashnode/image/upload/v1762853103062/870636bf-11df-4e3d-a73a-ebc0664818c2.png align="center")

Cliquez sur le modèle « PocketBase ». Vous verrez les ressources nécessaires pour provisionner l'application. Cliquez sur « Deploy Template » :

![Sevalla Deployment](https://cdn.hashnode.com/res/hashnode/image/upload/v1762853130642/f8ec7556-6544-4826-8c85-105e3893ca0c.png align="center")

Vous pouvez voir la ressource en cours de provisionnement. Une fois le déploiement terminé, allez dans l'application PocketBase et cliquez sur « Visit app ».

Vous verrez un message 404. Ajoutez `_` à l'URL et vous verrez le tableau de bord de connexion.

![Sevalla Deployment](https://cdn.hashnode.com/res/hashnode/image/upload/v1762853157824/6399c01d-7ae1-4c06-9f1d-9d7951bf04f7.png align="center")

Pour vous connecter pour la première fois, vous aurez besoin d'un compte super-utilisateur. Pour le créer, retournez à l'application et cliquez sur « Logs ». Vous verrez une URL commençant par [https://0.0.0.0.](http://0.0.0.0.)

![Pocketbase Deployment](https://cdn.hashnode.com/res/hashnode/image/upload/v1762853191932/d217e02f-91e8-4d28-ad4f-7eeb8d44b113.png align="center")

Remplacez le 0.0.0.0 par votre nouvelle URL cloud et copiez-collez le chemin complet dans le navigateur. Vous verrez l'option pour créer un super-utilisateur pour votre déploiement PocketBase.

![Pocketbase Create Super User](https://cdn.hashnode.com/res/hashnode/image/upload/v1762853227941/26c7086f-f95e-467a-a1db-97c34eadbcd4.png align="center")

Une fois que vous avez créé le super-utilisateur, vous pouvez à nouveau aller sur `/_` et vous connecter en utilisant le nom d'utilisateur et le mot de passe. Vous devriez maintenant voir le tableau de bord PocketBase.

![Pocketbase Dashboard](https://cdn.hashnode.com/res/hashnode/image/upload/v1762853283532/8cfc48e4-383a-4e11-820e-d64d22ed937d.png align="center")

Vous avez maintenant un serveur PocketBase de niveau production fonctionnant sur le cloud. Vous pouvez l'utiliser pour configurer des tables pour votre base de données et utiliser le SDK JavaScript ou d'autres SDK pour interagir avec PocketBase.

## Sécurité et nature Open Source

PocketBase est open source et sous licence MIT, ce qui signifie que vous êtes libre de l'utiliser dans des projets personnels ou commerciaux. Si vous trouvez un bug ou un problème de sécurité, vous pouvez le signaler aux mainteneurs, et ils le traiteront rapidement.

Le développement transparent du projet et sa communauté active en font un choix solide pour les startups, les développeurs indépendants et les passionnés qui préfèrent posséder leur infrastructure.

Comme il est encore en développement actif, la compatibilité ascendante n'est pas garantie avant la version 1.0. Mais il est déjà assez stable pour des applications de petite à moyenne envergure.

## Quand utiliser PocketBase

PocketBase est parfait pour les projets qui nécessitent un backend simple avec peu de maintenance. Il est idéal pour les prototypes, les petits produits SaaS, les applications indépendantes, les outils internes et les projets éducatifs.

Au lieu de configurer une stack complexe avec PostgreSQL, Node.js et nginx, vous pouvez lancer votre backend instantanément et vous concentrer sur votre produit.

Supposons que votre projet devienne plus important par la suite. Dans ce cas, vous pourrez migrer vers une configuration plus complexe ou continuer à utiliser PocketBase comme un service léger pour des fonctionnalités spécifiques comme l'authentification ou la synchronisation de données en temps réel.

## Conclusion

PocketBase redonne le plaisir d'un développement rapide sans configurations compliquées. Avec un seul exécutable, vous obtenez un backend qui prend en charge l'authentification, les mises à jour en temps réel, les téléchargements de fichiers et un tableau de bord d'administration. Il est open source, rapide et personnalisable, ce qui en fait un excellent choix pour les développeurs qui veulent avancer vite sans perdre le contrôle.

Que vous construisiez une application personnelle, un MVP de startup ou un tableau de bord interne, PocketBase vous donne le pouvoir de mettre en place un backend complet en quelques minutes. Vous pouvez commencer petit, l'étendre selon vos besoins et le déployer n'importe où – tout en gardant votre flux de travail simple et efficace.

*J'espère que vous avez apprécié cet article. Retrouvez-moi sur* [*Linkedin*](https://linkedin.com/in/manishmshiva) *ou* [*visitez mon site web*](https://manishshivanandhan.com/)*.*