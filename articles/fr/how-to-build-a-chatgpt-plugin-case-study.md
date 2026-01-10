---
title: Comment créer un plugin ChatGPT – Étude de cas utilisant PodcastAPI.com et
  Cloudflare Pages sans serveur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-22T23:01:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-chatgpt-plugin-case-study
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/56ae8d3bf6a04a8b85c96c695f29643f.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: chatgpt
  slug: chatgpt
- name: plugins
  slug: plugins
seo_title: Comment créer un plugin ChatGPT – Étude de cas utilisant PodcastAPI.com
  et Cloudflare Pages sans serveur
seo_desc: "By Wenbin Fang\nChatGPT is a highly intelligent auto-completion tool. It\
  \ takes instructions or questions in natural language and provides good enough text-based\
  \ outputs. \nBut there’s a catch — ChatGPT’s knowledge only goes up until September\
  \ 2021. So,..."
---

Par Wenbin Fang

[ChatGPT](https://chat.openai.com/) est un outil d'auto-complétion très intelligent. Il prend des instructions ou des questions en langage naturel et fournit des sorties textuelles suffisamment bonnes. 

Mais il y a un piège – les connaissances de ChatGPT ne vont que jusqu'en septembre 2021. Ainsi, au moment de la rédaction de cet article de blog (juin 2023), le modèle lui-même n'est pas au courant des événements ou des données après septembre 2021.

![Image](https://production.listennotes.com/web/image/5d9ab8edda604b2398d113fd45044b1d.png)

C'est là que les [plugins ChatGPT](https://openai.com/blog/chatgpt-plugins) viennent à la rescousse. Ces plugins permettent à ChatGPT d'interagir avec des API externes pour accéder à des informations à jour. Ils peuvent également aider ChatGPT à effectuer certaines actions comme déclencher une tâche Zapier ou envoyer un email.

Du point de vue d'un fournisseur d'API (comme [Listen Notes](https://www.listennotes.com/) fournissant [PodcastAPI.com](https://www.podcastapi.com/)), créer un plugin ChatGPT est similaire à fournir une interface conviviale, alimentée par l'IA, pour votre API. Pour les utilisateurs enthousiastes de ChatGPT, la création de plugins personnalisés peut étendre ses cas d'utilisation de manière significative.

Dans ce tutoriel, nous allons exploiter un exemple concret du [plugin ChatGPT Listen Notes](https://ai.listennotes.com/) (déjà disponible sur le Plugin store) comme étude de cas pour éclairer le processus de création d'un plugin ChatGPT. 

Le processus est plus simple que vous ne le pensez. À la fin de cet article, vous devriez avoir la compréhension nécessaire pour utiliser n'importe quelle API et créer votre propre plugin ChatGPT.

N'hésitez pas à essayer le [plugin ChatGPT Listen Notes](https://ai.listennotes.com/) et à explorer le code source [sur GitHub](https://github.com/ListenNotes/listennotes-chatgpt-plugin).

## **Comment fonctionnent les plugins ChatGPT ?**

Pour un utilisateur final, le processus d'utilisation d'un plugin ChatGPT est assez simple. Vous devez simplement activer le plugin sur l'interface utilisateur de ChatGPT, puis taper les invites.

![Image](https://production.listennotes.com/web/image/f8dcb56eeedb4b7bb810ddfc64a97028.png)
_Exemple d'un plugin ChatGPT en action_

Pour les développeurs, le processus nécessite un peu plus de travail. Vous devrez fournir un fichier **ai-plugin.json** hébergé en utilisant votre propre nom de domaine. Ce fichier inclut des métadonnées sur le plugin et une spécification OpenAPI détaillant les points de terminaison API disponibles avec lesquels ChatGPT peut interagir. 

Essentiellement, un plugin ChatGPT est un appelant d'API intelligent. L'utilisateur utilise le langage naturel pour appeler ces API externes au lieu d'écrire du code. Tous les points de terminaison API, ainsi que les fichiers **ai-plugin.json** et **openapi.json**, doivent être hébergés sous le même nom de domaine.

## **Étude de cas : Comment créer un plugin ChatGPT de découverte de podcasts utilisant PodcastAPI.com et Cloudflare Pages**

### **Exigences**

Notre plugin doit être capable de rechercher des podcasts ou des épisodes en fonction de mots-clés, de langues, de pays et de la durée audio, entre autres facteurs.

Nous utiliserons PodcastAPI.com et Cloudflare Pages pour créer ce plugin ChatGPT.

[PodcastAPI.com](https://www.podcastapi.com/) est une API Podcast largement utilisée dans le monde, et elle alimente [des milliers d'applications/sites web de podcasts](https://www.listennotes.com/api/apps/). C'est une API RESTful typique. 

Par exemple, pour trouver des podcasts liés à « startup » en anglais, vous envoyez une requête API comme **GET /search?q=startup&type=podcast&language=English**. Vous pouvez facilement essayer tous les points de terminaison de l'API Podcast avec le serveur mock et voir à quoi ressemblent les données JSON de réponse [sur la page de documentation de l'API](https://www.listennotes.com/api/docs/?test=1).

[Cloudflare Pages](https://pages.cloudflare.com/) est une plateforme sans serveur avec un quota gratuit généreux. Elle vous permet de créer une application web dynamique en JavaScript et d'envoyer des requêtes à des API externes de manière sécurisée sans exposer les identifiants de l'API. Et comme elle est sans serveur, vous n'avez pas à vous soucier de la provision de serveurs, de la scalabilité ou des problèmes opérationnels. 

Nous avons acquis une certaine expérience en utilisant Cloudflare Pages en construisant [microfeed](https://www.microfeed.org/)
— une alternative légère sans serveur à WordPress, que vous pouvez utiliser pour héberger des podcasts et des fichiers multimédias gratuitement.

### **Comment fonctionne exactement le plugin ?**

Vous pouvez trouver le code source du plugin ChatGPT Listen Notes sur GitHub : [github.com/ListenNotes/listennotes-chatgpt-plugin](http://github.com/ListenNotes/listennotes-chatgpt-plugin).

Le plugin, construit avec JavaScript, est déployé en tant qu'application web sur la plateforme sans serveur Cloudflare Pages. Ce déploiement sert trois ressources vitales sous le nom de domaine personnalisé ai.listennotes.com :

1. Le fichier **ai-plugin.json** : Celui-ci peut toujours être trouvé à [https://ai.listennotes.com/.well-known/ai-plugin.json](https://ai.listennotes.com/.well-known/ai-plugin.json). Le chemin de ce fichier est statique et ne doit pas être changé. [Voici](https://github.com/ListenNotes/listennotes-chatgpt-plugin/blob/main/functions/.well-known/ai-plugin.json/index.js) le code source pour référence.
2. Le fichier **openapi.json** : Cet emplacement est déterminé par le fichier **ai-plugin.json**. Dans notre cas, il est hébergé à [https://ai.listennotes.com/chatgpt-plugin/openapi.json](https://ai.listennotes.com/chatgpt-plugin/openapi.json). Vous pouvez consulter le code source [ici](https://github.com/ListenNotes/listennotes-chatgpt-plugin/blob/main/functions/chatgpt-plugin/openapi.json/index.js).
3. Points de terminaison de l'API proxy : Par exemple, https://ai.listennotes.com/api/v2/search_episodes. Ce sont essentiellement des enveloppes minces des points de terminaison réels de PodcastAPI.com. Le code source de ces points de terminaison peut être trouvé [ici](https://github.com/ListenNotes/listennotes-chatgpt-plugin/tree/main/functions/api/v2).

Alors, comment ces pièces fonctionnent-elles ensemble ? Approfondissons :

Tout d'abord, ChatGPT identifie le fichier **ai-plugin.json** à partir de son chemin fixe **/.well-known/ai-plugin.json**. Ce fichier contient des métadonnées essentielles sur le plugin et informe ChatGPT de l'emplacement du fichier **openapi.json**. Voici à quoi cela ressemble :

![Image](https://production.listennotes.com/web/image/439e931c7a7e460f834d3b2cdda20c19.png)

Deuxièmement, ChatGPT utilise le fichier **openapi.json** pour comprendre les points de terminaison API disponibles et leurs paramètres. Ce fichier aide essentiellement ChatGPT à comprendre comment interagir avec l'API.

![Image](https://production.listennotes.com/web/image/89307fbe9bb541cfab24f4a879f69856.png)

Enfin, en utilisant la description et d'autres métadonnées spécifiées dans le fichier **openapi.json**, ChatGPT peut traduire les invites en langage naturel en requêtes API spécifiques. 

Par exemple, une invite de l'utilisateur comme « rechercher des podcasts sur les startups en anglais » est traduite par ChatGPT en une requête GET à **GET /search_podcasts?q=startup&language=English**.

### Sécuriser les clés du royaume

Lors de l'utilisation d'API externes, comme PodcastAPI.com dans notre cas, une préoccupation importante est de maintenir la confidentialité des clés API. Vous pouvez le faire par des couches d'indirection – « Tous les problèmes en informatique peuvent être résolus par un autre niveau d'indirection. » :)

Tout d'abord, la vraie clé API (**LISTEN_API_KEY** dans notre cas) est fournie comme variable d'environnement sur Cloudflare Pages. Cela garantit que la clé API n'est jamais exposée dans le code source.

Ensuite, nous utilisons un secret (**CHATGPT_SECRET** dans notre cas) pour que ChatGPT appelle nos points de terminaison API proxy. Lors de la soumission du plugin à ChatGPT, vous serez invité à fournir ce secret.

Après avoir fourni le secret, ChatGPT émettra un jeton de vérification (**CHATGPT_VERIFICATION_TOKEN** dans notre cas), qui est placé dans le fichier ai-plugin.json. Il est parfaitement acceptable que ce jeton de vérification soit public.

Dans notre cas, **LISTEN_API_KEY**, **CHATGPT_SECRET** et **CHATGPT_VERIFICATION_TOKEN** sont tous stockés comme variables d'environnement chiffrées sur Cloudflare Pages, effectivement tenus à l'écart du public :

![Image](https://production.listennotes.com/web/image/5c9e02cdc2984f2993e033c1acda7b9c.png)

### Comment naviguer dans le processus de révision

Avant que votre plugin soit listé dans le magasin de plugins ChatGPT, vous pouvez le tester via votre domaine personnalisé (dans notre cas, ai.listennotes.com).

Lorsque vous êtes prêt à soumettre votre plugin pour révision, vous le ferez via un ticket Intercom. Vous devrez répondre à plusieurs questions et fournir des exemples d'invites. D'après notre expérience, il a fallu environ 2 jours à un membre de l'équipe ChatGPT pour examiner notre ticket.

Initialement, notre soumission a été rejetée parce que notre description ne se terminait pas par une ponctuation. Nous avons rapidement ajouté une période à la description de notre ai-plugin.json, resoumis et avons été approuvés dans les 2 heures. Ainsi, de la soumission à l'approbation, cela a été un processus d'environ 2 jours.

## **Comment adapter le processus pour d'autres API**

Si vous souhaitez adapter [le dépôt listennotes-chatgpt-plugin](https://github.com/ListenNotes/listennotes-chatgpt-plugin) pour qu'il fonctionne avec d'autres API, il y a trois domaines principaux que vous devrez modifier :

1. Mettre à jour **ai-plugin.json** ([code source](https://github.com/ListenNotes/listennotes-chatgpt-plugin/blob/main/functions/.well-known/ai-plugin.json/index.js)) : Vous trouverez plus de détails à ce sujet sur [openai.com](https://platform.openai.com/docs/plugins/getting-started/plugin-manifest).
2. Mettre à jour **openapi.json** ([code source](https://github.com/ListenNotes/listennotes-chatgpt-plugin/blob/main/functions/chatgpt-plugin/openapi.json/index.js)) : Cela est crucial car ChatGPT s'appuie sur cette spécification OpenAPI pour identifier les points de terminaison proxy disponibles. Pour plus d'informations, consultez [openai.com](https://platform.openai.com/docs/plugins/getting-started/openapi-definition).
3. Mettre à jour les points de terminaison de l'API proxy ([code source](https://github.com/ListenNotes/listennotes-chatgpt-plugin/tree/main/functions/api/v2)) pour les aligner avec d'autres API : Les points de terminaison proxy qui s'exécutent sur Cloudflare Pages doivent être mis à jour pour envoyer des requêtes API à vos API choisies. Vous pourriez vouloir vous familiariser avec [le fonctionnement des fonctions Cloudflare Pages](https://developers.cloudflare.com/pages/platform/functions/get-started/).

Après avoir apporté ces mises à jour, vous pouvez [déployer sur Cloudflare Pages](https://github.com/ListenNotes/listennotes-chatgpt-plugin#deploying-to-production) puis [soumettre votre plugin à ChatGPT pour révision](https://platform.openai.com/docs/plugins/review).

## Conclusion

Bien que cet aperçu vise à fournir des informations utiles, gardez à l'esprit que le plugin ChatGPT est encore en version bêta et sujet à des changements. 

Nous espérons maintenir cet article à jour au fur et à mesure des changements. Le monde de l'IA évolue rapidement, mais avec une solide compréhension de ces principes, vous serez bien équipé pour le naviguer.

Vous pouvez trouver cet article et bien d'autres sur [listennotes.com](https://www.listennotes.com/blog/how-to-build-a-chatgpt-plugin-a-case-study-using-78/).