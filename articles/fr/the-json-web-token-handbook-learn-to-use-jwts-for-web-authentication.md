---
title: 'Le guide du JSON Web Token : Apprenez à utiliser les JWT pour l''authentification
  web'
subtitle: ''
author: Sumit Saha
co_authors: []
series: null
date: '2025-10-08T18:18:43.201Z'
originalURL: https://freecodecamp.org/news/the-json-web-token-handbook-learn-to-use-jwts-for-web-authentication
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759947512495/9c8aee78-1a83-4958-8c01-110e2247286d.png
tags:
- name: JSON Web Tokens (JWT)
  slug: json-web-tokens-jwt
- name: JWT
  slug: jwt
- name: authentication
  slug: authentication
- name: token
  slug: token
seo_title: 'Le guide du JSON Web Token : Apprenez à utiliser les JWT pour l''authentification
  web'
seo_desc: 'JWT stands for JSON Web Token, and it’s one of those terms you’ll constantly
  come across in modern web development.

  At its core, a JWT is a JSON-based open standard format that allows you to represent
  specific claims securely between two parties. The...'
---

JWT signifie JSON Web Token, et c’est l’un de ces termes que vous rencontrerez constamment dans le développement web moderne.

À la base, un JWT est un format standard ouvert basé sur JSON qui vous permet de représenter des revendications (claims) spécifiques de manière sécurisée entre deux parties. Ce qui est passionnant, c’est la fréquence à laquelle le JWT est utilisé, en particulier dans les architectures de microservices et les systèmes d’authentification modernes.

Dans cet article, nous allons décomposer ce que sont réellement les JWT, explorer leur structure et voir exactement comment ils aident à sécuriser les applications web. À la fin, vous comprendrez pourquoi les développeurs s’appuient sur les JWT chaque jour.

## Voici ce que nous allons aborder

1. [Prérequis](#heading-prerequis)
    
2. [Qu'est-ce qu'un JWT ?](#heading-qu-est-ce-qu-un-jwt)
    
3. [Pourquoi avons-nous besoin de tokens ?](#heading-pourquoi-avons-nous-besoin-de-tokens)
    
    * [Tokens de session : l'approche classique](#heading-tokens-de-session-l-approche-classique)
        
    * [JWT : la solution moderne](#heading-jwt-la-solution-moderne)
        
4. [Structure d'un JWT : En-tête, Payload et Signature](#heading-structure-d-un-jwt-en-tete-payload-et-signature)
    
5. [Exemple : décoder un JWT](#heading-exemple-decoder-un-jwt)
    
6. [Comment les JWT assurent la sécurité : la signature](#heading-comment-les-jwt-assurent-la-securite-la-signature)
    
7. [Considérations de sécurité et gestion des tokens](#heading-considerations-de-securite-et-gestion-des-tokens)
    
8. [Comment créer des JWT dans différents langages](#heading-comment-creer-des-jwt-dans-differents-langages)
    
9. [Mise en œuvre pratique : Authentification JWT avec Express + MongoDB](#heading-mise-en-oeuvre-pratique-authentification-jwt-avec-express-mongodb)
    
    * [1\. Configuration du projet et dépendances](#heading-1-configuration-du-projet-et-dependances)
        
    * [2\. Structure des dossiers du projet](#heading-2-structure-des-dossiers-du-projet)
        
    * [3\. Implémentation étape par étape](#heading-3-implementation-etape-par-etape)
        
    * [4\. Comment tester votre API](#heading-4-comment-tester-votre-api)
        
10. [Résumé](#heading-resume)
    
11. [Mot de la fin](#heading-mot-de-la-fin)
    

## **Prérequis**

Pour suivre ce guide et en tirer le meilleur parti, vous devriez avoir :

1. Une connaissance de base de JavaScript / Node.js
    
2. Node.js et npm installés sur votre machine locale
    
3. Une compréhension de base de HTTP et des API REST
    
4. Une compréhension de JSON et de la manière de le parser/sérialiser
    
5. Des connaissances de base d'Express (ou la capacité de suivre les étapes)
    
6. Une instance de MongoDB en cours d'exécution (locale ou distante)
    
7. Une expérience avec le code asynchrone / Promises / async-await
    
8. Une familiarité avec les variables d'environnement / configuration .env
    

J’ai également créé une vidéo pour accompagner cet article. Si vous êtes du genre à aimer apprendre par la vidéo autant que par le texte, vous pouvez la consulter ici :

%[https://youtu.be/6drpx_QcMdg] 

## Qu'est-ce qu'un JWT ?

Les JWT sont aujourd'hui couramment utilisés pour l'authentification, mais ce n'était pas leur but initial. Ils ont été créés pour fournir un moyen standard à deux parties d'échanger des informations de manière sécurisée. En fait, il existe même une spécification standard de l'industrie ([RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519)) qui définit exactement comment les JWT doivent être structurés et comment ils sont censés être utilisés pour l'échange de données. Pensez-y comme à [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript#:~:text=ECMAScript%20\(%2F%CB%88%C9%9Bkm,pages%20across%20different%20web%20browsers.), ou ES, qui définit le standard pour JavaScript.

![Communication sécurisée Client-Serveur](https://cdn.hashnode.com/res/hashnode/image/upload/v1759525281325/62565bc2-dc09-4565-8e5b-12b6333e6ff6.jpeg align="center")

Dans les applications réelles, les JWT sont principalement utilisés pour l'authentification, et c'est l'angle sur lequel nous nous concentrerons dans cet article.

Mais n'oubliez pas que les JWT n'ont pas été conçus uniquement pour l'authentification. Il existe d'autres moyens de gérer l'authentification, et l'une des alternatives les plus populaires est le token de session.

## Pourquoi avons-nous besoin de tokens ?

Quelle que soit la stratégie d'authentification que nous utilisons, qu'il s'agisse d'un token de session ou d'un JWT, la raison sous-jacente est la même : la nature sans état (stateless) du protocole HTTP.

Lorsque nous échangeons des requêtes et des réponses d'un navigateur vers un serveur ou entre serveurs via HTTP, le protocole lui-même ne conserve aucune information.

*Sans état* signifie que lors des interactions entre le client et le serveur, HTTP ne se souvient d'aucune requête ou donnée précédente. En d'autres termes, chaque requête doit transporter séparément toutes les informations nécessaires. HTTP ne stocke aucune donnée par lui-même. Une fois qu'il reçoit une information, il l'oublie. C'est pourquoi nous disons que HTTP est sans état, car il n'a pas d'état inhérent ou d'information persistante.

Voyez les choses ainsi : lorsque nous accédons à une page web à partir d'un serveur, quelles informations envoyons-nous réellement au serveur ? S'il s'agit d'un simple site web statique, nous n'avons pas besoin d'envoyer grand-chose. Nous envoyons simplement l'URL de la page au serveur, et le serveur répond en livrant la page HTML correspondante. Cela signifie que le serveur n'a pas besoin de se souvenir d'informations ou de maintenir un état, ce qui est exactement la façon dont HTTP est conçu pour fonctionner, car HTTP lui-même est sans état.

![Réponse HTML simple d'un site statique](https://cdn.hashnode.com/res/hashnode/image/upload/v1759525352836/7e6081f5-7d34-462a-9a7d-bcffd0242e00.jpeg align="center")

Mais si l'application web fournit des réponses différentes pour chaque utilisateur – en d'autres termes, si le site web est dynamique – alors l'envoi de l'URL seule ne suffit pas. L'utilisateur doit également envoyer son identité avec l'URL au serveur.

Par exemple, si un utilisateur veut accéder à `page-1`, il doit dire au serveur : « *Je suis l'utilisateur A, donnez-moi la page-1.* » Le serveur répondra alors avec la `page-1` en conséquence. Mais la fois suivante, si l'utilisateur demande : « *Maintenant, donnez-moi la page-2* », que fera le serveur ? Comme HTTP est sans état, si la requête n'inclut pas l'identité de l'utilisateur, le serveur ne saura pas quelle réponse fournir. Cela signifie qu'à chaque requête, l'utilisateur doit fournir son identité, n'est-ce pas ?

Mais si nous regardons les sites web qui nous entourent, devons-nous vraiment fournir notre identité à chaque fois ? Prenez Facebook comme exemple. Une fois que nous nous sommes authentifiés et connectés, le serveur nous montre la page d'accueil lorsque nous la demandons, ou notre page de profil lorsque nous la demandons, sans nous obliger à nous authentifier à chaque requête.

La question est donc : si HTTP est sans état, comment est-ce possible ? Comment l'application web se souvient-elle de notre session de navigation ? La réponse est que les applications web peuvent maintenir des sessions de différentes manières, et l'une des méthodes les plus courantes consiste à utiliser des **tokens**.

![Comment le serveur se souvient-il de notre session ?](https://cdn.hashnode.com/res/hashnode/image/upload/v1759525399836/7b7cdeab-4baa-4cda-bbeb-aaf4e4d4170c.jpeg align="center")

### Tokens de session : l'approche classique

Il existe deux options populaires pour cela. L'une est le **Token de Session**, et l'autre est le **JSON Web Token (JWT)**. Comprenons les deux afin de clarifier ce que sont les JWT et pourquoi ils sont utilisés.

Imaginez un scénario dans le service client d'une entreprise. Un client appelle pour une plainte. Le représentant du support écoute le problème et essaie diverses étapes de dépannage mais ne parvient pas à résoudre le problème.

À ce stade, il transmet le dossier à son équipe de direction et crée un dossier client. Ce fichier contient toutes les conversations avec le client et les détails des tentatives de dépannage. Le client reçoit alors un ID de dossier ou un ID de ticket, de sorte que la prochaine fois qu'il appelle, il n'ait pas à repasser par les mêmes étapes.

![Scénario Service Client 1 - Analogie du Token de Session](https://cdn.hashnode.com/res/hashnode/image/upload/v1759525453002/c56bb7da-f6dd-4afe-b16b-966149bc7f91.jpeg align="center")

Le lendemain, lorsque le client appelle à nouveau, il donne son ID de ticket au représentant du service client. Le représentant effectue une recherche dans le système à l'aide de cet ID de ticket, récupère les détails et est en mesure de répondre avec précision au client.

![Scénario Service Client 2 - Analogie du Token de Session](https://cdn.hashnode.com/res/hashnode/image/upload/v1759525515798/426af5fa-ff38-4ce2-ae1b-48ca1a8f1e6c.jpeg align="center")

Ce scénario illustre le fonctionnement de l'authentification dans une application web à l'aide d'un token de session. Lorsqu'un utilisateur s'authentifie, le serveur crée une session et en assure le suivi. Un ID de session est généré pour cette session et renvoyé à l'utilisateur, comme le ticket de support dans l'exemple précédent. Dès lors, chaque fois que l'utilisateur envoie une requête au serveur, il inclut cet ID de session ou token. Le serveur recherche la session à l'aide de cet ID et identifie le client. Comme le serveur doit gérer plusieurs clients, cette méthode de token de session est devenue une stratégie efficace et largement utilisée pour l'authentification.

Et la manière dont le client envoie l'ID de session au serveur peut varier selon l'implémentation. La méthode la plus courante consiste à stocker l'ID de session dans les cookies du navigateur. L'avantage de cette approche est que chaque fois que le navigateur envoie une requête au même serveur, il ajoute automatiquement les informations du cookie à l'en-tête de la requête. Il s'agit d'un comportement intégré des navigateurs, aucune étape supplémentaire n'est donc nécessaire.

![Exemple de Token de Session](https://cdn.hashnode.com/res/hashnode/image/upload/v1759525561275/5881de41-571d-40ca-a0f7-4022d8c41754.jpeg align="center")

Lorsque l'utilisateur s'authentifie, le serveur enregistre les données dans le cookie du navigateur et, à partir de là, ces informations de cookie sont envoyées automatiquement avec chaque requête, permettant au serveur de reconnaître l'utilisateur. C'était une méthode très populaire, bien que dans les applications modernes, elle soit devenue un peu dépassée.

Mais ce mécanisme présente certains problèmes. Le plus gros problème est qu'il suppose qu'il n'y a qu'un seul serveur. Dans les applications web modernes, il y a généralement plusieurs serveurs. Dans de tels cas, un équilibreur de charge (load balancer) se place devant et décide quel serveur traitera la requête de l'utilisateur.

Disons que la méthode du token de session est utilisée. Lorsque l'utilisateur envoie la première requête, l'équilibreur de charge la transmet au `Serveur-1`. Le `Serveur-1` crée un ID de session et le renvoie au client. Plus tard, lorsque l'utilisateur envoie une autre requête, l'équilibreur de charge la dirige vers le `Serveur-2`. Mais le `Serveur-2` n'a pas cet ID de session stocké, alors comment saura-t-il à quel utilisateur appartient la requête ?

La solution courante consiste à stocker les ID de session non pas sur un serveur spécifique mais dans une base de données [Redis](https://redis.io/) partagée, afin que n'importe quel serveur puisse y vérifier l'ID de session. C'est ce qu'on appelle un **cache Redis**. Mais dans une architecture de microservices, cette approche a une faiblesse. Si, pour une raison quelconque, le cache Redis tombe en panne, les serveurs peuvent toujours fonctionner, mais le mécanisme d'authentification échouera. C'est précisément là qu'interviennent les JSON Web Tokens, offrant une approche légèrement différente.

![Gestion de plusieurs serveurs avec Token de Session et Cache Redis](https://cdn.hashnode.com/res/hashnode/image/upload/v1759525611999/a970e2d9-6663-4a4e-9c63-37ea13470b90.jpeg align="center")

### JWT : la solution moderne

Revenons à l'exemple du service client. Cette fois, imaginez qu'il n'y ait ni téléphone ni système. Le client vient directement au bureau et rencontre l'agent de support en personne. Comme l'agent n'a pas de système cette fois-ci, il ne peut pas stocker toutes les informations comme avant. Au lieu de cela, il écrit tout sur un morceau de papier et dit au client : « *La prochaine fois que vous viendrez, apportez ceci avec vous.* »

Cela signifie que la méthode est un peu différente du concept précédent, n'est-ce pas ? Mais il y a toujours un problème : la « **validité** ». Si le client n'est pas légitime et agit de manière malveillante, comment le représentant du support peut-il lui faire confiance ? Le lendemain, si le client arrive avec les mêmes informations écrites sur une feuille de papier vierge, comment l'agent peut-il vérifier la validité de son identité ?

Dans ce cas, une solution possible est que le responsable du service client signe le papier en le remettant au client. Ensuite, lorsque le client rapporte le papier, le représentant du support peut vérifier la signature et fournir le service en toute confiance.

Les JSON Web Tokens fonctionnent de manière similaire. Ici, lorsque le client s'authentifie, au lieu que le serveur enregistre toutes les informations, il envoie toutes les informations de l'utilisateur sous forme de token JSON accompagné d'une signature. Plus tard, à chaque requête suivante, le client envoie l'intégralité du token avec la requête, lequel contient des informations telles que l'identité de l'utilisateur, son nom et d'autres détails nécessaires.

Dans ce cas, le serveur n'enregistre rien, et toutes les informations restent chez le client. Chaque fois que le client envoie une requête avec ce token, le serveur peut le lire, identifier quel utilisateur a fait la requête et fournir les données nécessaires.

Ce token n'est pas seulement un simple ID. C'est un objet JSON contenant toutes les informations, et c'est ce que nous appelons un JSON Web Token. La manière dont le client stocke ce JWT dépend entièrement du client. Les méthodes les plus courantes consistent à le stocker dans les cookies du navigateur ou dans le stockage local (local storage).

![Analogie du JSON Web Token](https://cdn.hashnode.com/res/hashnode/image/upload/v1759525648690/691848c9-e4c2-4b3f-b3f5-06623627e38f.jpeg align="center")

### Structure d'un JWT : En-tête, Payload et Signature

Comme mentionné, le serveur reçoit un objet JSON, mais un JWT ne ressemble pas à un JSON classique.

![Structure JWT](https://cdn.hashnode.com/res/hashnode/image/upload/v1759525702339/f74219b8-4a01-4ac4-920b-449faf103520.png align="center")

Dans l'image ci-dessus, cela peut sembler un peu inhabituel. En fait, il s'agit d'une version encodée de l'objet JSON, une sorte de représentation brouillée ou compacte. Si vous regardez de plus près, vous verrez qu'un JWT est divisé en trois parties, séparées par des points. La première partie est l'**en-tête (header)**, la deuxième partie est le **payload JSON**, qui contient essentiellement nos données, et la troisième partie est la **signature**.

Si nous examinons chaque partie individuellement :

* L'**en-tête** est un objet JSON distinct.
    
* Le **payload** est également un objet JSON distinct contenant nos données.
    
* La troisième partie est la **signature**.
    

Mais que signifie la signature ici ? En termes simples, la signature est une valeur de hachage. Nos données sont hachées à l'aide d'une clé secrète pour créer la signature. Cette clé secrète est conservée sur le serveur. Ainsi, lorsque ce JSON Web Token est envoyé au serveur, le serveur peut utiliser cette clé secrète pour vérifier la signature. Cela garantit que le token est valide et n'a pas été falsifié.

## Exemple : décoder un JWT

Regardons un exemple. Le meilleur site web pour travailler avec les JWT et comprendre leur structure est [jwt.io](http://jwt.io)[.](https://jwt.io/) Si vous collez un JWT sur le site, trois sections apparaissent : l'en-tête, le payload et la signature. Le payload est affiché dans la section « Decoded Payload », qui contient le contenu et les données. Vous verrez qu'il y a un ID, un objet JSON avec un nom et un délai d'expiration.

![Décodage d'un JWT](https://cdn.hashnode.com/res/hashnode/image/upload/v1759525738886/84c2532f-dc09-4a96-83de-ecd4a24d958f.jpeg align="center")

L'en-tête est également un objet JSON tout à fait valide, qui spécifie un algorithme et indique le type – indiquant essentiellement quel algorithme sera utilisé pour créer ou vérifier ce JWT.

Ainsi, les données principales se trouvent dans la section « Decoded Payload », et la troisième partie est la signature. Maintenant, il y a un point important à noter : vous pourriez vous demander d'où vient ce token à l'aspect brouillé. C'est en fait très simple. Les données du « Decoded Payload » sont **encodées en Base64**, et c'est ce qui donne l'apparence de ce token brouillé.

Si vous copiez cette partie du JWT et la collez dans n'importe quel décodeur Base64 en ligne, vous verrez immédiatement les données.

![Encodage Décodage Base64](https://cdn.hashnode.com/res/hashnode/image/upload/v1759525794705/4ee950a2-2ad0-40b4-8287-fdfea9543a6f.png align="center")

Qu'est-ce que cela signifie ? Cela signifie que si ces données sont à nouveau encodées en Base64, le même token sera généré. L'en-tête fonctionne également de la même manière.

Et le point final : la partie brouillée ou encodée. Est-ce fait pour la sécurité ? Non, ce n'est pas pour la sécurité. C'est fait purement par commodité. Les objets JSON peuvent être assez volumineux, et tous les langages de programmation ne les gèrent pas de la même manière. En JavaScript, c'est facile, mais dans d'autres langages, cela peut parfois poser problème. Donc, pour faciliter la manipulation, les données sont encodées en Base64. Ce n'est pas pour la sécurité, car l'encoder ainsi ne rend pas les données sûres, puisque les informations peuvent toujours être consultées publiquement.

Comme vous pouvez le voir dans le diagramme ci-dessus, dès que vous les saisissez sur ce site, vos données sont immédiatement visibles. Cela signifie qu'aucune information sensible ne doit être stockée ici, seulement des détails d'identification de l'utilisateur, comme un ID utilisateur ou d'autres informations publiques. **Les mots de passe ou les clés secrètes ne doivent jamais être stockés dans le token, car ils peuvent être facilement lus.** Même s'il semble brouillé ou encodé, il est en réalité public.

## Comment les JWT assurent la sécurité : la signature

Passons maintenant à la partie sécurité, qui est assurée par la signature. Dans notre exemple de papier précédent, une personne pouvait simplement ajouter une signature à la main.

Mais pour les données, le processus de création d'une signature est différent. Pour les données, la signature est créée de manière cryptographique à l'aide d'une clé secrète, qui constitue la signature réelle. Le processus de création de la signature est le suivant :

1. Les données sont encodées en Base64.
    
2. Elles sont concaténées avec la clé secrète.
    
3. Le tout est à nouveau encodé en Base64.
    

La configuration spécifie un algorithme. Cet algorithme peut être modifié, mais le même algorithme utilisé pour créer le token doit être utilisé pour le vérifier. En d'autres termes, l'algorithme de génération et de vérification du token doit toujours être le même.

Enfin, les données sont hachées à l'aide d'une clé secrète. Cette clé secrète n'est pas accessible au public. Au lieu de cela, elle est conservée uniquement sur le serveur, généralement stockée de manière sécurisée dans un coffre-fort serveur. Lorsque ce JWT atteint le serveur, le serveur utilise la clé secrète pour vérifier si le token est valide. S'il ne correspond pas correctement, il affichera « signature invalide ». Cela garantit que le serveur peut confirmer si le token a été falsifié et que son intégrité est intacte.

![La Grande Formule](https://cdn.hashnode.com/res/hashnode/image/upload/v1759525829955/bf017016-d9fd-43cb-836a-eafe4f35540b.jpeg align="center")

Par exemple, si vous utilisez `love-you-all-from-logicbaselabs` comme signature et que le serveur la vérifie, il affichera « *signature vérifiée* ». Cela démontre que la clé secrète n'existe que sur le serveur. Cela garantit que même si des informations publiques sont affichées, la validité du token peut être confirmée.

Les JSON Web Tokens ne sont pas comme un mot de passe, cependant. Ils servent principalement à identifier l'utilisateur. Le serveur peut vérifier le JWT pour déterminer s'il appartient à un utilisateur valide. En d'autres termes, le JWT représente l'identité de l'utilisateur. C'est un token très important, contenant un contenu sécurisé ainsi que la signature.

![Vérification de la signature](https://cdn.hashnode.com/res/hashnode/image/upload/v1759525873387/a434b453-0a38-41a5-93f3-bd12b46806f3.jpeg align="center")

## Considérations de sécurité et gestion des tokens

Une chose importante à retenir : si quelqu'un s'empare de votre JWT, c'est-à-dire s'il possède exactement le même token, il peut facilement se connecter en tant qu'utilisateur. Il lui suffit d'envoyer des requêtes avec ce token pour obtenir l'accès nécessaire.

Vous pourriez y penser ainsi : si quelqu'un obtient votre mot de passe Facebook, il peut se connecter à votre compte Facebook. De même, si quelqu'un obtient le code PIN de votre compte PayPal, il peut facilement accéder à votre compte. En d'autres termes, si quelqu'un s'empare de vos informations les plus sécurisées, il n'y a aucun moyen de les protéger.

Il en va de même pour les JWT : conserver le token en toute sécurité du côté client est absolument crucial. À cet égard, nous sommes quelque peu vulnérables.

Il existe cependant une différence clé. Dans le cas des tokens de session, si nous supposons qu'un compte a été compromis, le serveur peut invalider cette session. En d'autres termes, plus personne ne peut se connecter en utilisant cet ID de session.

Mais avec un JWT, le token reste valide jusqu'à son expiration. Il n'y a donc pas de moyen direct de l'invalider. Comme le token est cryptographiquement autonome et signé avec la clé secrète du serveur, une fois créé, il ne peut pas être directement révoqué par le serveur.

La seule façon de gérer cela est ce qui se fait sur le web : mettre le token sur une liste de blocage (denylisting). En d'autres termes, le serveur maintient une base de données distincte répertoriant tous les tokens JWT qui sont sur liste noire. Chaque fois qu'une requête arrive, le serveur vérifie d'abord si le token est valide. Ensuite, via un middleware, il vérifie si le token est sur la liste de blocage. L'accès n'est autorisé à l'utilisateur que s'il n'est pas sur cette liste.

Voici donc les règles d'utilisation des JSON Web Tokens. Les JWT peuvent être utilisés dans n'importe quel langage de programmation, en particulier dans le contexte des API REST. Ils sont extrêmement populaires et largement utilisés dans les architectures de microservices.

## Comment créer des JWT dans différents langages

La façon dont vous créez un JWT dépend du langage de programmation que vous utilisez. Par exemple, dans Node.js, il existe des bibliothèques spécialisées, comme [jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken), c'est donc simple. Et en PHP, il existe également des options faciles à utiliser pour créer des JWT. Ainsi, les JWT sont un outil universel, non limité à un langage de programmation spécifique. Beaucoup de gens pensent qu'ils ne sont que pour JavaScript, mais ce n'est pas vrai.

Et n'oubliez pas que les JWT ne sont pas seulement utilisés à des fins d'authentification. Vous pouvez les utiliser pour représenter n'importe quel type d'identité. Par exemple, si vous allez à un concert, l'accès pourrait être accordé à l'aide d'un JWT au lieu d'un ticket ordinaire. Lorsque votre client utilise ce JWT, la passerelle ou le serveur peut lire le token, fournir l'accès aux informations et le vérifier à l'aide de la signature.

## Mise en œuvre pratique : Authentification JWT avec Express + MongoDB

Dans cette section, nous allons mettre en pratique tous les concepts que nous avons appris jusqu'à présent. En utilisant [**Express.js**](https://www.freecodecamp.org/news/the-express-handbook/) et [**MongoDB**](https://www.freecodecamp.org/news/how-to-start-using-mongodb/), nous allons construire un système d'authentification JWT complet étape par étape.

Ne vous inquiétez pas si cela semble impressionnant au début. Nous irons prudemment, une étape à la fois, et à la fin, vous aurez un projet fonctionnel. Pensez-y comme à l'entrée dans un bâtiment étage par étage : nous explorerons chaque section en profondeur et en ressortirons avec une solide compréhension.

### 1\. Configuration du projet et dépendances

Avant d'écrire du code, nous devons configurer notre projet Node.js et installer les dépendances requises.

#### Initialiser le projet Node.js

Ouvrez votre terminal et exécutez :

```javascript
mkdir jwt-auth-demo
cd jwt-auth-demo
npm init -y
```

Cela créera un fichier `package.json` avec les paramètres par défaut.

#### Installer les dépendances

Nous avons besoin de quelques packages pour construire notre système d'authentification JWT :

```javascript
npm install express mongoose bcryptjs jsonwebtoken dotenv
```

* `express` : Framework web Node.js rapide et minimaliste pour créer des routes d'API.
    
* `mongoose` : Bibliothèque ODM (Object Data Modeling) pour interagir facilement avec MongoDB.
    
* `bcryptjs` : Bibliothèque pour hacher et comparer les mots de passe de manière sécurisée.
    
* `jsonwebtoken` : Bibliothèque pour générer et vérifier les tokens JWT.
    
* `dotenv` : Charge les variables d'environnement à partir d'un fichier `.env` pour garder les secrets en sécurité.
    

#### Installer les dépendances de développement (Optionnel)

Pour plus de commodité lors du développement, installez **nodemon** pour redémarrer automatiquement le serveur lors des modifications de fichiers :

```javascript
npm install --save-dev nodemon
```

Mettez à jour les scripts du `package.json` :

```javascript
"scripts": {
  "start": "node server.js",
  "dev": "nodemon server.js"
}
```

* `npm start` lance le serveur normalement.
    
* `npm run dev` lance le serveur avec redémarrage automatique via **nodemon**.
    

### 2\. Structure des dossiers du projet

```javascript
jwt-auth-demo/
│
├── config/
│   └── db.js
│
├── controllers/
│   └── authController.js
│
├── middlewares/
│   └── authMiddleware.js
│
├── models/
│   └── User.js
│
├── routes/
│   └── auth.js
│
├── services/
│   ├── hashService.js
│   └── jwtService.js
│
├── .env
├── server.js
├── package.json
```

**Qu'est-ce qui va où ?**

* `config/` : Connexion à la base de données et configuration de l'environnement.
    
* `controllers/` : Logique principale pour chaque point de terminaison (endpoint).
    
* `middlewares/` : Fonctions qui s'exécutent avant les contrôleurs (par exemple, vérifications d'authentification).
    
* `models/` : Schémas Mongoose.
    
* `routes/` : Définitions des points de terminaison de l'API.
    
* `services/` : Logique réutilisable (hachage, JWT).
    
* `.env` : Secrets et variables de configuration.
    
* `server.js` : Point d'entrée de l'application.
    

### 3\. Implémentation étape par étape

#### Initialiser le serveur Express

Avant de faire quoi que ce soit de complexe, nous devons configurer un serveur simple à l'aide d'Express. Considérez cela comme le cœur de notre application. Ce serveur sera chargé d'écouter les requêtes entrantes (comme la connexion ou l'inscription d'un utilisateur) et de renvoyer des réponses.

**Fichier : server.js**

```javascript
// server.js

// Importer la bibliothèque express pour construire notre serveur
const express = require("express");

// Créer une instance d'express
const app = express();

// Middleware pour parser les corps de requête JSON (important pour les API)
app.use(express.json());

// Route par défaut pour tester le serveur
app.get("/", (req, res) => {
  res.send("Hello World! Votre serveur fonctionne 🚀");
});

// Démarrer le serveur sur le port 5000
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Serveur en cours d'exécution sur http://localhost:${PORT}`);
});
```

* Nous importons Express et créons une instance d'application.
    
* Nous utilisons un middleware pour parser les requêtes JSON (important pour les API).
    
* Nous définissons une route simple `/` pour tester si notre serveur fonctionne.
    
* Nous démarrons le serveur sur le port 5000 et affichons un message lorsqu'il est opérationnel.
    

Maintenant, testons-le :

* Exécutez `node server.js` ou `npm run dev`.
    
* Ouvrez votre navigateur sur `http://localhost:5000`.
    
* Vous devriez voir : `Hello World! Votre serveur fonctionne 🚀`
    

#### Connecter MongoDB avec Mongoose

Dans cette étape, nous voulons stocker les utilisateurs dans une base de données. Pour cela, nous utiliserons MongoDB. Pour interagir facilement avec MongoDB dans Node.js, nous utilisons Mongoose, qui est une bibliothèque ODM.

**Fichier : config/db.js**

```javascript
// config/db.js

// Importer mongoose
const mongoose = require("mongoose");

// Se connecter à MongoDB en utilisant une variable d'environnement
const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGO_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log("✅ MongoDB Connecté");
  } catch (err) {
    console.error("❌ Erreur de connexion MongoDB :", err.message);
    process.exit(1); // Arrêter le serveur si la DB échoue
  }
};

module.exports = connectDB;
```

Maintenant, notre serveur est connecté à MongoDB. Chaque fois que nous insérerons, mettrons à jour ou interrogerons des données, elles iront dans cette base de données.

**Fichier : .env**

```javascript
PORT=5000
MONGO_URI=mongodb://127.0.0.1:27017/jwt-auth-demo
JWT_SECRET=votre_cle_super_secrete
```

Le fichier .env stocke des informations sensibles telles que l'URI de votre base de données, le secret JWT et le port du serveur. En utilisant des variables d'environnement, vous pouvez garder les secrets hors de votre code et modifier facilement la configuration sans modifier vos fichiers sources. Ne committez jamais le fichier .env dans des dépôts publics pour protéger vos identifiants.

#### Créer le modèle utilisateur

Dans cette étape, nous devons définir à quoi ressemble un utilisateur dans notre base de données. Chaque utilisateur aura un **nom, un e-mail et un mot de passe**.

**Fichier : models/User.js**

```javascript
// models/User.js
const mongoose = require("mongoose");

// Définir un schéma (plan des données utilisateur)
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
});

// Créer et exporter le modèle
module.exports = mongoose.model("User", userSchema);
```

Comme vous pouvez le voir, chaque utilisateur a maintenant un nom, un e-mail et un mot de passe haché. Cela garantit que chaque utilisateur que nous enregistrons possède ces trois champs.

#### Services de hachage et JWT

Dans cette étape, nous allons gérer le hachage des mots de passe et la gestion des JWT à l'aide de services distincts. Cela permet de garder notre code organisé et réutilisable.

**Fichier : services/hashService.js**

```javascript
//services/hashService.js

const bcrypt = require("bcryptjs");

// Fonction pour hacher un mot de passe en clair
exports.hashPassword = async (plainPassword) => {
  // bcrypt.hash génère une version hachée du mot de passe
  // Le nombre 10 correspond aux tours de salage (salt rounds), ce qui affecte la complexité du hachage
  return await bcrypt.hash(plainPassword, 10);
};

// Fonction pour comparer un mot de passe en clair avec un mot de passe haché
exports.comparePassword = async (plainPassword, hashedPassword) => {
  // bcrypt.compare vérifie si le mot de passe en clair correspond au mot de passe haché
  return await bcrypt.compare(plainPassword, hashedPassword);
};
```

* `hashPassword(plainPassword)` : Prend un mot de passe en texte clair et renvoie une version hachée à l'aide de bcrypt. Ne stockez jamais de mots de passe en clair directement.
    
* `comparePassword(plainPassword, hashedPassword)` : Compare un mot de passe saisi par l'utilisateur avec le mot de passe haché stocké dans la base de données. Renvoie `true` s'ils correspondent.
    

**Fichier : services/jwtService.js**

```javascript
// services/jwtService.js

const jwt = require("jsonwebtoken");

// Fonction pour générer un JWT
exports.generateToken = (payload) => {
  // jwt.sign crée un token signé en utilisant notre clé secrète des variables d'environnement
  // expiresIn définit la durée de validité du token (ici 1 heure)
  return jwt.sign(payload, process.env.JWT_SECRET, { expiresIn: "1h" });
};

// Fonction pour vérifier un JWT
exports.verifyToken = (token) => {
  // jwt.verify vérifie si le token est valide et non expiré
  return jwt.verify(token, process.env.JWT_SECRET);
};
```

* `generateToken(payload)` : Génère un JWT pour un utilisateur. Le `payload` contient généralement l'ID de l'utilisateur et son e-mail.
    
* `verifyToken(token)` : Vérifie que le JWT est valide et renvoie le payload décodé en cas de succès.
    
* L'utilisation d'un service JWT distinct permet de centraliser la logique des tokens et de la gérer facilement.
    

#### Contrôleur d'authentification (Auth Controller)

Dans cette étape, nous allons gérer toute la logique liée à l'authentification dans un contrôleur séparé. Cela permet de garder les routes propres et de séparer la logique métier des définitions de points de terminaison.

**Fichier : controllers/authController.js**

```javascript
// controllers/authController.js

const User = require("../models/User");
const { hashPassword, comparePassword } = require("../services/hashService");
const { generateToken } = require("../services/jwtService");

// Inscrire un nouvel utilisateur
exports.register = async (req, res) => {
  try {
    const { name, email, password } = req.body; // Récupérer l'entrée utilisateur

    // Étape 1 : Vérifier si l'utilisateur existe déjà
    const existingUser = await User.findOne({ email });
    if (existingUser)
      return res.status(400).json({ message: "L'utilisateur existe déjà !" });

    // Étape 2 : Hacher le mot de passe en utilisant hashService
    const hashedPassword = await hashPassword(password);

    // Étape 3 : Enregistrer l'utilisateur dans la base de données
    const user = new User({ name, email, password: hashedPassword });
    await user.save();

    // Étape 4 : Envoyer une réponse de succès
    res.status(201).json({ message: "Utilisateur inscrit avec succès !" });
  } catch (err) {
    // Gérer les erreurs avec élégance
    res.status(500).json({ error: err.message });
  }
};

// Connecter l'utilisateur
exports.login = async (req, res) => {
  try {
    const { email, password } = req.body; // Récupérer l'entrée utilisateur

    // Étape 1 : Trouver l'utilisateur par e-mail
    const user = await User.findOne({ email });
    if (!user)
      return res.status(400).json({ message: "E-mail ou mot de passe invalide" });

    // Étape 2 : Comparer le mot de passe fourni avec le mot de passe haché
    const isMatch = await comparePassword(password, user.password);
    if (!isMatch)
      return res.status(400).json({ message: "E-mail ou mot de passe invalide" });

    // Étape 3 : Générer un JWT en utilisant jwtService
    const token = generateToken({ id: user._id, email: user.email });

    // Étape 4 : Envoyer une réponse de succès avec le token
    res.json({ message: "Connexion réussie !", token });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Route de profil protégée
exports.profile = (req, res) => {
  // req.user est défini par le middleware d'authentification après vérification du token
  res.json({
    message: "Bienvenue sur votre profil !",
    user: req.user,
  });
};
```

* **Fichier :** `controllers/authController.js` – Contient toute la logique liée à l'authentification.
    
* `exports.register` gère l'inscription des utilisateurs :
    
    * Vérifie si l'utilisateur existe.
        
    * Hache le mot de passe à l'aide de `hashService`.
        
    * Enregistre le nouvel utilisateur dans MongoDB.
        
    * Renvoie un message de succès.
        
* `exports.login` gère la connexion des utilisateurs :
    
    * Trouve l'utilisateur par e-mail.
        
    * Compare les mots de passe à l'aide de `hashService.comparePassword`.
        
    * Génère un token JWT s'il est valide.
        
    * Renvoie le token dans la réponse.
        
* `exports.profile` gère la route de profil protégée :
    
    * Renvoie les informations de l'utilisateur à partir de `req.user`, qui est défini par le middleware d'authentification.
        
* L'utilisation d'un contrôleur permet de garder les définitions de routes propres et de séparer la logique métier de la gestion des points de terminaison.
    

#### Middleware d'authentification (Auth Middleware)

Dans cette étape, nous créons un middleware pour protéger les routes en vérifiant les JWT. Seuls les utilisateurs authentifiés peuvent accéder aux points de terminaison protégés.

**Fichier : middlewares/authMiddleware.js**

```javascript
// middlewares/authMiddleware.js

const { verifyToken } = require("../services/jwtService");

// Middleware pour protéger les routes
module.exports = (req, res, next) => {
  // Étape 1 : Récupérer l'en-tête Authorization
  const authHeader = req.headers["authorization"];
  if (!authHeader)
    return res.status(401).json({ message: "Aucun token fourni" });

  // Étape 2 : Extraire le token du format 'Bearer <token>'
  const token = authHeader.split(" ")[1];
  if (!token) return res.status(401).json({ message: "Token malformé" });

  try {
    // Étape 3 : Vérifier le token en utilisant jwtService
    const decoded = verifyToken(token);

    // Étape 4 : Attacher les infos utilisateur décodées à l'objet de requête
    req.user = decoded;

    // Passer au middleware suivant ou au gestionnaire de route
    next();
  } catch (err) {
    // Si le token est invalide ou expiré
    res.status(401).json({ message: "Token invalide ou expiré" });
  }
};
```

* **Fichier :** `middlewares/authMiddleware.js` – Middleware pour protéger les routes.
    
* Étape 1 : Vérifie si l'en-tête `Authorization` est présent.
    
* Étape 2 : Extrait le token du format `Bearer <token>`.
    
* Étape 3 : Vérifie le token à l'aide de `jwtService.verifyToken`.
    
* Étape 4 : Attache les informations utilisateur décodées à `req.user` pour une utilisation dans les gestionnaires de routes suivants.
    
* Si le token est manquant, malformé, invalide ou expiré, le middleware répond par **401 Unauthorized**. Cela garantit que seuls les utilisateurs authentifiés peuvent accéder aux routes protégées.
    

#### Routes d'authentification (Auth Routes)

Dans cette étape, nous allons définir les routes liées à l'authentification et les connecter au contrôleur et au middleware.

**Fichier : routes/auth.js**

```javascript
// routes/auth.js

const express = require("express");
const router = express.Router();
const authController = require("../controllers/authController");
const authMiddleware = require("../middlewares/authMiddleware");

// Étape 1 : Route d'inscription
// Les utilisateurs envoient leur nom, e-mail et mot de passe à ce point de terminaison
router.post("/register", authController.register);

// Étape 2 : Route de connexion
// Les utilisateurs envoient leur e-mail et mot de passe pour recevoir un JWT
router.post("/login", authController.login);

// Étape 3 : Route de profil protégée
// Accessible uniquement aux utilisateurs authentifiés avec un JWT valide
router.get("/profile", authMiddleware, authController.profile);

module.exports = router;
```

* **Fichier :** `routes/auth.js` – Fichier central pour définir les points de terminaison d'authentification.
    
* `router.post("/register", authController.register)` : Gère l'inscription des utilisateurs.
    
* `router.post("/login", authController.login)` : Gère la connexion des utilisateurs et la génération de tokens.
    
* `router.get("/profile", authMiddleware, authController.profile)` : Route protégée, nécessite un JWT. Le `authMiddleware` garantit que seuls les utilisateurs authentifiés peuvent y accéder.
    
* L'utilisation de routes avec des contrôleurs et des middlewares permet de garder l'application organisée et professionnelle.
    

#### Fichier serveur principal

C'est le point d'entrée principal de notre application. Il configure le serveur, se connecte à la base de données et monte toutes les routes.

**Fichier : server.js**

```javascript
// server.js

require("dotenv").config(); // Étape 1 : Charger les variables d'environnement depuis .env
const express = require("express");
const connectDB = require("./config/db");

const app = express();

// Étape 2 : Se connecter à MongoDB
connectDB();

// Étape 3 : Middleware pour parser les corps de requête JSON
app.use(express.json());

// Étape 4 : Monter les routes d'authentification
// Toutes les routes liées à l'authentification commenceront par /api/auth
app.use("/api/auth", require("./routes/auth"));

// Étape 5 : Route par défaut pour tester le serveur
app.get("/", (req, res) => {
  res.send("Hello World! Votre serveur fonctionne 🚀");
});

// Étape 6 : Démarrer le serveur sur le PORT du .env ou par défaut 5000
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Serveur en cours d'exécution sur http://localhost:${PORT}`);
});
```

* **Charger les variables d'environnement :** Utilisation de `dotenv` pour séparer les secrets et la configuration du code.
    
* **Se connecter à MongoDB :** Appelle `connectDB()` depuis `config/db.js`.
    
* **Middleware :** `express.json()` permet à Express de parser les corps de requête JSON.
    
* **Monter les routes :** `app.use("/api/auth", ...)` enregistre toutes les routes d'authentification.
    
* **Route par défaut :** Un simple point de terminaison GET pour vérifier que le serveur fonctionne.
    
* **Démarrer le serveur :** `app.listen` commence à écouter sur le port configuré.
    

### 4\. Comment tester votre API

Dans cette section, vous apprendrez à tester votre API d'authentification JWT à l'aide d'outils comme Postman ou n'importe quel client HTTP.

Avant de tester, assurez-vous que votre serveur est en cours d'exécution. S'il ne l'est pas, ouvrez un terminal et exécutez :

```javascript
npm run dev
```

ou

```javascript
node server.js
```

Cela démarrera votre serveur sur le port défini dans le fichier `.env` (par défaut `5000`).

Assurez-vous que votre MongoDB est en cours d'exécution. Si vous utilisez MongoDB en local, démarrez-le avec :

```javascript
mongod
```

ou assurez-vous que votre service MongoDB est actif.

Vérifiez toujours le terminal pour d'éventuelles erreurs. Si le serveur ou la base de données ne démarre pas, vos requêtes API ne fonctionneront pas.

#### Inscrire un utilisateur

Requête :

```javascript
POST http://localhost:5000/api/auth/register
Content-Type: application/json

{
  "name": "sumit",
  "email": "sumit@example.com",
  "password": "mypassword"
}
```

Réponse :

```javascript
{
  "message": "Utilisateur inscrit avec succès !"
}
```

Cela envoie une requête POST à `http://localhost:5000/api/auth/register` avec les détails de l'utilisateur. En cas de succès, vous recevez un message de confirmation.

#### Connexion

Requête :

```javascript
POST http://localhost:5000/api/auth/login
Content-Type: application/json

{
  "email": "sumit@example.com",
  "password": "mypassword"
}
```

Réponse :

```javascript
{
  "message": "Connexion réussie !",
  "token": "<JWT_TOKEN>"
}
```

Cela envoie une requête POST à `http://localhost:5000/api/auth/login` avec l'e-mail et le mot de passe. Si les identifiants sont corrects, vous recevez un JWT pour accéder aux routes protégées.

#### Accéder à une route protégée

Requête :

```javascript
GET http://localhost:5000/api/auth/profile
Authorization: Bearer <JWT_TOKEN>
```

Réponse :

```javascript
{
  "message": "Bienvenue sur votre profil !",
  "user": {
    "id": "...",
    "email": "sumit@example.com",
    "iat": ...,
    "exp": ...
  }
}
```

Cela envoie le JWT dans l'en-tête `Authorization` en utilisant le schéma `Bearer`.

* Seuls les tokens valides permettront d'accéder à cette route protégée.
    
* `iat` et `exp` indiquent l'heure d'émission et l'heure d'expiration du token.
    

**Note :** Incluez toujours `Authorization: Bearer <token>` pour les routes protégées.

## Résumé

Cet article vous a donné un aperçu complet des JSON Web Tokens (JWT) et de leur rôle dans l'authentification web. Il a expliqué la nature sans état de HTTP, le besoin de tokens, et a comparé les tokens de session classiques avec les JWT.

Nous avons couvert la structure des JWT, les mécanismes de sécurité et la mise en œuvre pratique à l'aide de Node.js, Express et MongoDB. Nous avons également discuté des considérations de sécurité, de la gestion des tokens et de la manière de tester une API d'authentification JWT.

### Voici un résumé des points clés :

1. **Qu'est-ce que le JWT ?**
    
    * Le JWT est un standard ouvert basé sur JSON pour représenter de manière sécurisée des revendications entre deux parties, défini par la RFC 7519.
        
    * Largement utilisé pour l'autorisation dans les applications web modernes et les architectures de microservices.
        
    * Alternative aux tokens de session pour maintenir l'état de l'utilisateur.
        
2. **Nature sans état de HTTP**
    
    * HTTP ne conserve pas d'informations entre les requêtes, ce qui oblige chaque requête à transporter les données nécessaires.
        
    * Les tokens (session ou JWT) sont utilisés pour maintenir les sessions utilisateur dans les applications web dynamiques.
        
3. **Tokens de session**
    
    * Approche classique où le serveur crée et stocke un ID de session, généralement dans des cookies.
        
    * Fonctionne bien pour les configurations à serveur unique mais nécessite un stockage partagé (par exemple, Redis) dans les environnements multi-serveurs.
        
    * Vulnérable si le cache partagé tombe en panne.
        
4. **JWT : la solution moderne**
    
    * Le serveur envoie un token JSON signé au client, qui le stocke et l'envoie avec chaque requête.
        
    * Aucun stockage côté serveur requis – toutes les informations utilisateur sont dans le token.
        
    * La signature garantit la validité et l'intégrité.
        
5. **Structure du JWT**
    
    * Trois parties : En-tête, Payload, Signature (séparées par des points).
        
    * L'en-tête et le payload sont des objets JSON encodés en Base64. La signature est un hachage utilisant une clé secrète.
        
    * L'encodage Base64 est une question de commodité, pas de sécurité.
        
6. **Décodage des JWT**
    
    * Des outils comme [jwt.io](https://jwt.io/) peuvent décoder les JWT pour afficher l'en-tête, le payload et la signature.
        
    * Les données sensibles ne doivent pas être stockées dans les JWT, car le payload est lisible publiquement.
        
7. **Sécurité du JWT**
    
    * La signature est créée à l'aide d'une clé secrète et d'un algorithme cryptographique.
        
    * Le serveur vérifie l'intégrité du token à l'aide de la clé secrète.
        
    * Les JWT identifient les utilisateurs mais ne font pas office de mots de passe.
        
8. **Considérations de sécurité et gestion des tokens**
    
    * Si un JWT est compromis, l'attaquant peut usurper l'identité de l'utilisateur jusqu'à l'expiration du token.
        
    * Les JWT ne peuvent pas être directement révoqués ; la mise sur liste noire est utilisée pour invalider les tokens compromis.
        
    * Les tokens de session peuvent être invalidés par le serveur.
        
9. **Les JWT dans différents langages**
    
    * Les JWT sont indépendants du langage et peuvent être implémentés en Node.js, PHP et d'autres langages.
        
    * Utiles pour l'authentification et la représentation de tout type d'identité.
        
10. **Mise en œuvre pratique : Authentification JWT avec Express + MongoDB**
    
    * Guide étape par étape pour construire un système d'authentification JWT :
        
        * Configuration du projet et dépendances
            
        * Structure des dossiers
            
        * Initialisation du serveur Express
            
        * Connexion MongoDB
            
        * Création du modèle utilisateur
            
        * Hachage de mot de passe et services JWT
            
        * Contrôleur d'authentification et middleware
            
        * Routes d'authentification
            
        * Fichier serveur principal
            
        * Instructions de test de l'API
            
11. **Tester l'API**
    
    * Instructions pour inscrire des utilisateurs, se connecter et accéder aux routes protégées à l'aide d'outils comme Postman.
        
    * Exemples de requêtes et de réponses fournis.
        
12. **Résumé et mot de la fin**
    
    * Les JWT sont sécurisés, sans état et largement utilisés pour l'autorisation.
        
    * La sécurité dépend du stockage sûr des tokens et d'une gestion appropriée.
        

## Mot de la fin

Vous pouvez trouver tout le code source de ce tutoriel dans [ce dépôt GitHub](https://github.com/logicbaselabs/jwt-auth-demo). S'il vous a aidé d'une manière ou d'une autre, n'hésitez pas à lui donner une étoile pour montrer votre soutien !

De plus, si vous avez trouvé les informations ici précieuses, n'hésitez pas à les partager avec d'autres personnes qui pourraient en bénéficier. J'apprécierais vraiment vos retours – mentionnez-moi sur X [@sumit\_analyzen](https://x.com/sumit_analyzen) ou sur Facebook [@sumit.analyzen](https://facebook.com/sumit.analyzen), [regardez mes tutoriels de programmation](https://youtube.com/@logicBaseLabs), ou [connectez-vous simplement avec moi](https://www.linkedin.com/in/sumitanalyzen/) sur LinkedIn.