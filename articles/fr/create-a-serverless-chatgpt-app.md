---
title: Comment créer une application ChatGPT serverless en 10 minutes
subtitle: ''
author: Michael Yuan
co_authors: []
series: null
date: '2023-03-20T16:52:42.000Z'
originalURL: https://freecodecamp.org/news/create-a-serverless-chatgpt-app
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/c0fd422e-f234-49e2-85a6-24f91b0b9991-1.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: '#chatbots'
  slug: chatbots
- name: serverless
  slug: serverless
seo_title: Comment créer une application ChatGPT serverless en 10 minutes
seo_desc: 'Since OpenAI released an official API for ChatGPT in March 2023, many developers
  and entrepreneurs are interested in integrating it into their own business operations.

  But some significant barriers remain that make it difficult for them to do this:


  ...'
---

Depuis qu'OpenAI a [publié une API officielle pour ChatGPT](https://openai.com/blog/introducing-chatgpt-and-whisper-apis) en mars 2023, de nombreux développeurs et entrepreneurs souhaitent l'intégrer dans leurs propres opérations commerciales.

Mais certains obstacles importants subsistent et rendent cette tâche difficile :

* OpenAI fournit [une API stateless simple](https://platform.openai.com/docs/guides/chat) pour ChatGPT. Le développeur doit suivre l'historique et le contexte de chaque conversation dans un cache ou une base de données gérés par l'application. Le développeur doit également gérer et sécuriser les clés API. Il y a beaucoup de code boilerplate sans rapport avec la logique métier de l'application.
    
* L'interface utilisateur « naturelle » pour une application utilisant l'API ChatGPT est une discussion par fils (threaded chat). Mais il est difficile de créer une « interface de chat » dans un Framework web ou d'application traditionnel. En fait, l'interface de chat la plus couramment utilisée existe déjà dans des applications de messagerie comme Slack, Discord et même des forums (par exemple, GitHub Discussions). Nous avons besoin d'un moyen simple de connecter les réponses de l'API ChatGPT à un service de messagerie existant.
    

Dans cet article, je vais vous montrer comment créer un bot GitHub serverless. Le bot permet aux utilisateurs de GitHub de discuter avec ChatGPT et entre eux dans les GitHub Issues. Vous pouvez [l'essayer en posant une question](https://github.com/second-state/chat-with-chatgpt/issues/new), ou [rejoindre un autre fil de conversation](https://github.com/second-state/chat-with-chatgpt/issues) en laissant un commentaire. En d'autres termes, ce projet utilise l'interface de messages filés de GitHub Issues comme sa propre interface de chat.

![Image](https://i.imgur.com/7eWhQ8I.png align="left")

*Figure 1. Apprendre Rust avec ChatGPT. voir* [*https://github.com/second-state/chat-with-chatgpt/issues/31*](https://github.com/second-state/chat-with-chatgpt/issues/31)

Le bot est une fonction serverless écrite en Rust. Il suffit de forker l'exemple, de déployer votre fork sur [flows.network](https://www.freecodecamp.org/news/p/dfeeb7b1-d632-448e-97b3-9fcd7df30bce/flows.network) et de le configurer pour interagir avec vos propres dépôts GitHub et vos clés OpenAI. Vous disposerez d'un bot GitHub entièrement fonctionnel en 10 minutes. Il n'est pas nécessaire de configurer un serveur web, un webhook pour l'API GitHub ou un serveur de cache / base de données.

## Comment forker le dépôt modèle

Tout d'abord, [forkez ce dépôt modèle depuis GitHub](https://github.com/flows-network/chatgpt-github-app).

Le fichier [`src/lib.rs`](https://github.com/flows-network/chatgpt-github-app/blob/main/src/lib.rs) contient l'application du bot (également appelée fonction de flux). La fonction `run()` est appelée au démarrage. Elle écoute les événements `issue_comment` et `issues` du dépôt GitHub [`owner/repo`](https://github.com/second-state/chat-with-chatgpt). Ces événements sont émis lorsqu'un nouveau commentaire d'issue ou une nouvelle issue est créée dans le dépôt.

```rust
#[no_mangle]
#[tokio::main(flavor = "current_thread")]
pub async fn run() {
    // Configurer les variables pour
    //   owner : organisation GitHub pour installer le bot
    //   repo : dépôt GitHub pour installer le bot
    //   openai_key_name : Nom de votre clé API OpenAI
    // Toutes les valeurs peuvent être définies dans le code source ou en tant que variables d'environnement
    
    listen_to_event(&owner, &repo, vec!["issue_comment", "issues"], |payload| {
        handler(&owner, &repo, &openai_key_name, payload)
    })
    .await;
}
```

La fonction `handler()` traite les événements reçus par `listen_to_event()`. Si l'événement est un nouveau commentaire dans une issue, le bot appelle l'API ChatGPT d'OpenAI pour ajouter le texte du commentaire dans une conversation existante identifiée par `issue.number`. Il reçoit une réponse de ChatGPT et ajoute un commentaire dans l'issue.

La fonction de flux gère ici automatiquement et de manière transparente l'historique de la conversation avec l'API ChatGPT dans un stockage local. La clé API OpenAI est également stockée dans le stockage local de sorte qu'au lieu d'inclure le texte secret dans le code source, la clé peut être identifiée par un nom de chaîne dans `openai_key_name`.

```rust
EventPayload::IssueCommentEvent(e) => {
    if e.comment.user.r#type != "Bot" {
        if let Some(b) = e.comment.body {
            if let Some(r) = chat_completion (
                    openai_key_name,
                    &format!("issue#{}", e.issue.number),
                    &b,
                    &ChatOptions::default(),
            ) {
                if let Err(e) = issues.create_comment(e.issue.number, r.choice).await {
                    write_error_log!(e.to_string());
                }
            }
        }
    }
}
```

Si l'événement est une nouvelle issue, la fonction de flux crée une nouvelle conversation identifiée par `issue.number` et demande une réponse à ChatGPT.

```rust
EventPayload::IssuesEvent(e) => {
    if e.action == IssuesEventAction::Closed {
        return;
    }

    let title = e.issue.title;
    let body = e.issue.body.unwrap_or("".to_string());
    let q = title + "\n" + &body;
    if let Some(r) = chat_completion (
            openai_key_name,
            &format!("issue#{}", e.issue.number),
            &q,
            &ChatOptions::default(),
    ) {
        if let Err(e) = issues.create_comment(e.issue.number, r.choice).await {
            write_error_log!(e.to_string());
        }
    }
}
```

## Comment déployer la fonction de flux serverless

Comme nous pouvons le voir, le code de la fonction de flux appelle les API du SDK pour effectuer des opérations complexes. Par exemple,

* La fonction `listen_to_event()` enregistre une URL de webhook via l'API GitHub afin que la fonction `handler()` soit appelée lorsque certains événements se produisent dans GitHub.
    
* La fonction `chat_completion()` appelle l'API ChatGPT avec la clé API nommée et l'historique / contexte passé de la conversation spécifiée. La clé API et l'historique de la conversation sont stockés dans un cache Redis.
    

Le serveur de webhook et le cache Redis sont tous deux des services externes dont dépend le SDK. Cela signifie que la fonction de flux doit s'exécuter dans un environnement hôte géré qui fournit ces services externes. [Flows.network](https://flows.network/) est un hôte PaaS (Platform as a Service) pour les SDK de fonctions de flux.

Pour déployer la fonction de flux sur flows.network, il vous suffit d'importer son code source vers le PaaS.

Tout d'abord, connectez-vous à flows.network depuis votre compte GitHub. Importez votre dépôt GitHub forké qui contient le code source de la fonction de flux et choisissez « With Environment Variables ».

Notez qu'il ne s'agit PAS du dépôt GitHub où vous souhaitez déployer le bot. Il s'agit du dépôt de votre code source de fonction de flux forké.

![Image](https://i.imgur.com/CH1nUf8.png align="left")

*Figure 2. Importez le dépôt GitHub que vous avez forké depuis le modèle de fonction de flux dans flows.network.*

Définissez les variables d'environnement pour pointer la fonction de flux vers le nom de la clé API OpenAI (`open_ai_key`) et le dépôt GitHub (`owner` et `repo`).

Les variables GitHub `owner` et `repo` pointent ici vers le dépôt GitHub où vous souhaitez déployer le bot, PAS vers le dépôt du code source de la fonction de flux.

![Image](https://i.imgur.com/5gcTKMv.png align="left")

*Figure 3. Définissez les variables d'environnement pour le dépôt GitHub où vous souhaitez déployer le bot, ainsi que le nom de la clé API OpenAI.*

Flows.network récupérera le code source et compilera le code source Rust en bytecode Wasm à l'aide de la chaîne d'outils standard `cargo`. Il exécutera ensuite la fonction de flux Wasm dans le [WasmEdge Runtime](https://github.com/WasmEdge/WasmEdge).

## Comment connecter la fonction de flux à GitHub et OpenAI

Bien que la fonction de flux nécessite des connexions aux API OpenAI et GitHub, le code source ne contient aucune clé API, jeton d'accès ou logique OAUTH codé en dur. Les SDK de fonctions de flux ont permis aux développeurs d'interagir facilement et en toute sécurité avec les services API SaaS externes.

Flows.network découvre que la fonction de flux nécessite des connexions aux API OpenAI et GitHub. Il présente des flux de travail d'interface utilisateur pour que les développeurs puissent :

* Se connecter à GitHub, autoriser l'accès aux événements et enregistrer la fonction de flux en tant que webhook pour recevoir ces événements.
    
* Associer une clé API OpenAI au nom `openai_key_name`.
    

![Image](https://i.imgur.com/CpLDrub.png align="left")

*Figure 4. Les services externes requis par la fonction de flux sont connectés et passent au vert.*

Une fois que les API SaaS externes sont connectées et autorisées, elles deviennent vertes sur le tableau de bord de la fonction de flux. La fonction de flux recevra désormais les événements pour lesquels elle utilise `listen_to_event()`. Elle bénéficiera également d'un accès transparent à Redis pour la clé API OpenAI nommée et le contexte de conversation mis en cache pour prendre en charge la fonction SDK `chat_completion()`.

## Et ensuite ?

Le bot GitHub n'est qu'un des nombreux types de bots que flows.network peut prendre en charge. En connectant la fonction de flux à un canal Slack, vous pouvez faire participer ChatGPT à votre discussion de groupe. Voici un exemple de bot ChatGPT basé sur Slack.

%[https://github.com/flows-network/collaborative-chat] 

![Image](https://i.imgur.com/voB27bj.png align="left")

*Figure 5. Le bot ChatGPT Slack.*

Un autre exemple consiste à demander à ChatGPT de répondre à des questions juridiques dans un canal Slack. La fonction de flux fait précéder la question juridique d'un prompt.

%[https://github.com/flows-network/robo-lawyer] 

![Image](https://i.imgur.com/afDM5im.png align="left")

*Figure 6. Le bot avocat robot Slack.*

Outre GitHub et Slack, de nombreux produits SaaS peuvent être intégrés dans flows.network via leurs API.

Bien que les exemples de fonctions de flux soient écrits en Rust, nous visons à prendre en charge les SDK de fonctions de flux basés sur JavaScript. En d'autres termes, les fonctions du SDK de la plateforme telles que `listen_to_event()` et `chat_completion()` auront une version JavaScript. La fonction de flux JavaScript s'exécute dans le [WasmEdge Runtime](https://github.com/WasmEdge/WasmEdge) sur la plateforme flows.network via le module [WasmEdge-QuickJS](https://wasmedge.org/docs/develop/javascript/intro).