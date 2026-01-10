---
title: Comment créer un chatbot RAG propulsé par l'IA avec Amazon Lex, Bedrock et
  S3
subtitle: ''
author: Chisom Uma
co_authors: []
series: null
date: '2025-12-03T22:34:26.277Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-ai-powered-rag-chatbot
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1764801036311/e1bb9ed8-f64e-433f-916f-fd3079aac4d3.png
tags:
- name: chatbot
  slug: chatbot
- name: AI
  slug: ai
- name: AWS
  slug: aws
seo_title: Comment créer un chatbot RAG propulsé par l'IA avec Amazon Lex, Bedrock
  et S3
seo_desc: Chatbots are widely adopted among software companies, especially those that
  interact heavily with customers. It is typically used for tasks such as customer
  support, answering questions, and providing information on websites, apps, and messaging
  plat...
---


Les chatbots sont largement adoptés par les entreprises de logiciels, en particulier celles qui interagissent intensivement avec les clients. Ils sont généralement utilisés pour des tâches telles que le support client, la réponse aux questions et la fourniture d'informations sur des sites web, des applications et des plateformes de messagerie.

De nos jours, comme on pouvait s'y attendre, certains chatbots sont propulsés par l'IA et peuvent générer des réponses aux requêtes grâce à la Génération Augmentée par Récupération (RAG). J'étais curieux de savoir comment cela fonctionnait, je l'ai construit moi-même, et maintenant, nous allons voir comment créer un chatbot RAG propulsé par l'IA.

Pour ce tutoriel, vous allez construire un chatbot RAG qui répond aux questions sur les politiques de voyage vers Mars. Le chatbot récupère ses réponses à partir de notre propre source de données (documents de politique de voyage) stockée dans un bucket S3. Le document sert de source de données interne que le chatbot peut consulter lors de la génération des prompts.

Au lieu de réponses scénarisées provenant de données pré-entraînées, le chatbot extraira des réponses contextuelles directement de la base de connaissances.

C'est parti :)

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Qu'est-ce que la Génération Augmentée par Récupération (RAG) ?](#heading-quest-ce-que-la-generation-augmentee-par-recuperation-rag)
    
* [Qu'est-ce qu'Amazon Bedrock ?](#heading-quest-ce-quamazon-bedrock)
    
* [Premiers pas : Accéder aux modèles sur Bedrock](#heading-premiers-pas-acceder-aux-modeles-sur-bedrock)
    
* [Étape 1 : Télécharger les documents de politique de voyage vers le bucket S3](#heading-etape-1-telecharger-les-documents-de-politique-de-voyage-vers-le-bucket-s3)
    
* [Étape 2 : Créer une base de connaissances dans Amazon Bedrock](#heading-etape-2-creer-une-base-de-connaissances-dans-amazon-bedrock)
    
* [Étape 3 : Créer un chatbot Amazon Lex](#heading-etape-3-creer-un-chatbot-amazon-lex)
    
* [Étape 4 : Ajouter une intention de bienvenue à votre chatbot](#heading-etape-4-ajouter-une-intention-de-bienvenue-a-votre-chatbot)
    
* [Étape 5 : Construire le chatbot](#heading-etape-5-construire-le-chatbot)
    
* [Étape 6 : Ajouter Amazon QnAIntent](#heading-etape-6-ajouter-amazon-qnaintent)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

* Un compte AWS, connecté en tant qu'utilisateur IAM avec des privilèges d'administrateur
    
* Accès au modèle Amazon Titan Embeddings G1 - text sur Amazon Bedrock
    
* Accès à Anthropic Claude 3.5 Sonnet sur Amazon Bedrock.
    
* Accès aux documents de politique de voyage. Vous pouvez les télécharger depuis Google Drive [ici](https://drive.google.com/file/d/1kyewU4eCFnaYS3wQ7Fyv22G3ycthbfJb/view).
    
* Expérience de l'utilisation de la console AWS.
    
* Aucun codage requis.
    

## Qu'est-ce que la Génération Augmentée par Récupération (RAG) ?

Les grands modèles de langage (LLM) comme GPT-4 et Claude sont pratiquement partout. Ils réussissent certaines choses de manière incroyable et se trompent sur d'autres de façon très intéressante, comme les hallucinations, où le modèle génère des informations factuellement incorrectes ou fabriquées. Cela nous amène à l'idée du RAG.

*Marina Danilevsky*, *Chercheuse principale chez IBM*, dans une [conférence](https://youtu.be/T-D1OfcDW1M?si=YFYcEeulZpXf9AXN), a décrit le RAG comme un « Framework » pour aider les LLM à être plus précis et à jour.

Avant d'entrer dans le vif du sujet du RAG, parlons brièvement de la partie « génération ». La génération, dans le contexte du RAG, fait référence aux LLM qui génèrent des textes en réponse à une requête d'utilisateur, appelée prompt.

Ces LLM peuvent parfois donner des réponses incorrectes, en raison d'un contexte limité ou d'informations obsolètes. Surtout parce qu'ils ne récupèrent des informations qu'à partir de données pré-entraînées. Imaginez qu'on vous demande combien de Grammy Awards votre artiste préféré a remportés, et que vous donniez une réponse lue dans un magazine il y a quatre ans. Vous pourriez avoir raison, mais il y a deux problèmes avec cette réponse : d'abord, vous n'avez pas cité de source, et ensuite, elle est obsolète.

C'est le problème que les LLM ont traditionnellement rencontré. Les réponses étaient obsolètes et aucune source crédible n'était citée.

Maintenant, imaginez si vous aviez d'abord cherché la réponse auprès d'une source réputée sur Google. Votre réponse serait plus précise et factuelle, et s'il y avait le moindre doute de la part de la personne qui a posé la question, vous pourriez facilement partager le lien vers la source réputée sur Google, et il n'y aurait plus de doutes ou de questions.

Quel est le rapport avec les LLM et le RAG ? Eh bien, maintenant, au lieu que le LLM obtienne uniquement des réponses de ses données pré-entraînées, au risque de fournir des réponses obsolètes, lorsque le RAG intervient, il récupère les réponses aux requêtes directement à partir d'un magasin de contenu, qui peut comprendre des sources externes, comme Internet, ou des sources internes, comme des documents (ce qui sera utilisé dans ce tutoriel). De cette façon, les réponses générées sont plus précises.

Le RAG aide le LLM à rester à jour en récupérant des informations supplémentaires auprès d'autres sources plutôt qu'uniquement à partir de ses données pré-entraînées.

## Qu'est-ce qu'Amazon Bedrock ?

[Amazon Bedrock](https://aws.amazon.com/bedrock/) est le service géré d'AWS qui vous donne accès à des modèles de fondation, essentiellement les moteurs d'IA de base qui alimentent les applications d'IA générative. La beauté de Bedrock est qu'il gère tout le travail lourd pour vous. Pas besoin de provisionner des GPU, de mettre en place des pipelines de modèles ou de gérer des problèmes d'infrastructure.

C'est une plateforme unique où vous pouvez expérimenter, personnaliser et déployer des modèles d'IA de premier plan provenant de fournisseurs tels qu'*Anthropic*, *Stability AI*, et les propres modèles *Titan* d'Amazon (utilisés dans ce tutoriel).

Voici un exemple pratique : supposons que vous construisiez un chatbot de support client. Avec Bedrock, vous choisissez simplement un modèle de langage qui correspond à vos besoins, vous l'affinez pour votre cas d'utilisation spécifique et vous l'intégrez dans votre application, le tout sans toucher à la configuration du serveur ou au code d'infrastructure.

## Premiers pas : Accéder aux modèles sur Bedrock

Pour accéder aux modèles sur AWS via Bedrock :

* Connectez-vous à votre compte AWS IAM avec des privilèges root.
    
* Naviguez vers **Amazon Bedrock > Model catalog.**
    

![Image de la page du catalogue de modèles Amazon Bedrock](https://cdn.hashnode.com/res/hashnode/image/upload/v1764493545469/839771fb-c3aa-47d4-b1b9-60cd67ba26c5.png align="center")

* Localisez le modèle « Titan Embeddings G1 - Text » et les modèles « Claude 3.5 Sonnet ».
    

Lorsque vous cliquez sur ces modèles, vous êtes dirigé vers une page avec plus de détails. Vous n'avez rien à faire sur cette page. Nous utiliserons ces modèles plus tard dans ce tutoriel. Dans les sections suivantes, nous passerons en revue les étapes pour construire le chatbot.

## Étape 1 : Télécharger les documents de politique de voyage vers le bucket S3

Pour télécharger des documents, naviguez vers la page Amazon S3 dans votre console AWS, puis créez un bucket. Pour plus de détails sur la création d'un bucket, reportez-vous à la [documentation AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html). Ensuite, téléchargez le document téléchargé dans le bucket S3.

Notez que le document est compressé (zip) ; vous devrez le décompresser avant de le télécharger.

## Étape 2 : Créer une base de connaissances dans Amazon Bedrock

Maintenant que nous avons créé nos buckets S3 et téléchargé nos documents, nous ne pouvons pas simplement connecter notre chatbot construit avec Lex directement aux buckets S3. S3 n'est pas vraiment « intelligent » d'un point de vue IA. Pour obtenir les capacités d'IA nécessaires pour faire fonctionner cela, nous avons besoin d'Amazon Bedrock.

Tout d'abord, nous devons créer une base de connaissances dans Amazon Bedrock.

Pour commencer, retournez sur la page Bedrock ouverte précédemment et naviguez vers **Build** > **Knowledge Bases**. Cliquez sur **Create**. Dans le menu déroulant, choisissez « Knowledge base with vector store ». Laissez les permissions IAM sur « Create and use a new service role ». C'est ce qui permet à Bedrock d'accéder à d'autres services. Choisissez « Amazon S3 » comme type de source de données. Cliquez sur **Next**.

Ensuite, cliquez sur **Browse S3** et sélectionnez le bucket créé avec les documents téléchargés. Cliquez sur **Next**. Sur la page suivante, cliquez sur **Select model** pour choisir un modèle d'embedding. Sélectionnez le « Titan Embeddings G1 - Text », puis sélectionnez « Amazon OpenSearch Serverless » et cliquez sur **Apply**.

Laissez tout le reste tel quel et cliquez sur **Next**. Sur la page suivante, cliquez sur **Create Knowledge Base**. Notez que cela prend un certain temps (quelques minutes), vous devez donc être patient pour cette étape. Une fois votre base de connaissances créée, vous serez dirigé vers une nouvelle page avec un message comme celui de l'image ci-dessous :

![image de la création réussie de la base de connaissances Bedrock](https://cdn.hashnode.com/res/hashnode/image/upload/v1764493716382/fd92d1d9-51ef-470f-bae9-b1cb636a260e.png align="center")

Le deuxième message vous indique que vous devez synchroniser la base de connaissances avec les sources de données. Pour ce faire, faites défiler vers le bas jusqu'à la section *Data source*, sélectionnez la source de données, puis cliquez sur **Sync**. Attendez quelques secondes et tout se synchronise.

**Note :** Si vous avez plus de données que ce que nous avons dans ce tutoriel (seulement quatre PDF), la synchronisation peut prendre plus de temps.

Maintenant, notre base de connaissances Bedrock est configurée. La base de connaissances se connecte au bucket S3 contenant les documents de voyage.

Il est maintenant temps de créer le chatbot. Pour cela, nous utiliserons [Amazon Lex](https://aws.amazon.com/lex/).

## Étape 3 : Créer un chatbot Amazon Lex

Dans votre console AWS, naviguez vers Amazon Lex, puis cliquez sur **Create bot**. Sélectionnez **Create a blank bot** sous la méthode de création *Traditional*. Pour le nom du bot, vous pouvez l'appeler « Mars travel bot » ou tout autre nom de votre choix.

Sous la section « *IAM permissions* », sélectionnez **Create a role with basic Amazon Lex permissions**. Sous la section « *Children’s Online Privacy Protection Act (COPPA)* », sélectionnez **No**, car notre bot n'est pas soumis à la COPPA, et cliquez sur **Next**.

Sur la page suivante, entrez une courte description dans le champ de texte *Description*. Sélectionnez votre option d'interaction vocale préférée disponible pour la synthèse vocale. C'est la voix que vos utilisateurs entendront lorsqu'ils utiliseront le chatbot.

![Image des voix du bot Amazon Lex](https://cdn.hashnode.com/res/hashnode/image/upload/v1764493888022/29ad9758-c0b7-42f4-8308-8255137c4649.png align="center")

Ce qui est cool avec Lex, c'est que vous pouvez écouter un échantillon de voix pour chaque voix. Cela peut vous aider à prendre la meilleure décision pour votre entreprise. Ensuite, cliquez sur **Done**.

## Étape 4 : Ajouter une intention de bienvenue à votre chatbot

Après avoir cliqué sur le bouton **Done**, vous devriez voir une page pour créer une intention (intent). Une intention est essentiellement une action qui répond à la demande d'un utilisateur.

Commençons par créer une intention de bienvenue. Pour commencer, changez le nom de l'intention en « WelcomeIntent ». Ensuite, faites défiler vers le bas jusqu'à la section « *Sample utterances* » et ajoutez des énoncés. Ce sont des exemples de textes que vous attendez d'un utilisateur lorsqu'il commence à utiliser votre chatbot. Ainsi, si l'utilisateur dit « Salut », le chatbot répond par un message de bienvenue. Pour ce tutoriel, j'ai ajouté les énoncés attendus suivants :

* « Salut »
    
* « Hey »
    
* « Bonjour »
    

Vous pouvez en ajouter autant que vous le souhaitez.

Dans la section « *Initial response* », vous pouvez fournir une réponse à l'énoncé de l'utilisateur. Sous le menu déroulant **Message group**, vous pouvez taper quelque chose comme « Salut ! Bienvenue ! Comment puis-je vous aider aujourd'hui ? ». Ensuite, cliquez sur le bouton *Advanced options*. Cela fait apparaître une boîte de dialogue. Sous *Set values*, sélectionnez l'option « Wait for users input ». Vous pouvez sélectionner d'autres options, mais pour ce tutoriel, nous choisissons celle-ci. Cliquez sur **Update options**.

Lorsque vous revenez à la page *Intents*, vous remarquerez une intention « Fallbackintent » générée automatiquement pour vous. Cette intention est censée être invoquée lorsqu'un utilisateur lance votre bot avec un énoncé qui diffère de celui créé pour l'intention de bienvenue.

## Étape 5 : Construire le chatbot

À l'étape précédente, nous avons construit une intention pour le bot. Il est maintenant temps de construire le chatbot proprement dit qui regroupe toute cette configuration en quelque chose d'utilisable.

Pour commencer, cliquez sur **Build** en haut à droite de votre écran.

![Image de la construction du bot](https://cdn.hashnode.com/res/hashnode/image/upload/v1764494047899/cac4a609-f551-4b3e-9714-1330da3e7908.png align="center")

Une fois la construction terminée, vous recevrez un message en haut de la page. Maintenant, il est temps de tester le bot. Cliquez sur **Test** en haut à droite de votre écran.

Vous obtenez un chatbot pré-construit pour tester votre implémentation. Entrez un texte ou un énoncé, dans ce cas, par exemple, « Salut », et vous obtenez une réponse initiale. Rappelez-vous, l'énoncé et la réponse initiale ont été définis dans la section précédente.

![Image de l'interaction avec le bot](https://cdn.hashnode.com/res/hashnode/image/upload/v1764494109571/391fbcc9-b3b0-498c-85f9-43e28d12b58d.png align="center")

Lorsque vous cliquez sur Inspect, vous verrez l'intention actuelle. Dans ce cas, la WelcomeIntent.

À ce stade, nous n'avons pas encore pleinement intégré les capacités d'IA requises pour obtenir des réponses sur les politiques de voyage vers Mars.

## Étape 6 : Ajouter Amazon QnAIntent

L'Amazon QnAIntent introduit des capacités de GenAI dans notre bot. Il s'agit d'une intention intégrée qui utilise l'IA générative pour répondre aux demandes de questions fréquemment posées (FAQ) en interrogeant le contenu de la base de connaissances autorisée.

Pour commencer, naviguez vers **Add intent > Use built-in intent** sur la page Intents. Sélectionnez l'option QnAIntent, comme le montre l'image ci-dessous :

![Image de l'intention intégrée](https://cdn.hashnode.com/res/hashnode/image/upload/v1764494196339/d28020cb-c3a2-4595-aae0-f02463d422a7.png align="center")

Donnez-lui le nom de votre choix. Cliquez sur **Add**. Vous serez dirigé vers la page de l'intention. Dans la section « *QnA configuration* », sélectionnez **Claude3.5 Sonnet** comme modèle souhaité.

![Image de la configuration du modèle et de la base de connaissances dans Lex](https://cdn.hashnode.com/res/hashnode/image/upload/v1764494285444/9d49daed-02ed-44a6-a7e6-763611f3a214.png align="center")

Pour l'ID, puisque nous avions déjà créé une base de connaissances plus tôt, retournez dans **Amazon Bedrock** > **Knowledge Bases** et copiez votre *Knowledge Base ID* et collez-le dans le champ « Knowledge base for Amazon Bedrock Id ». Cliquez sur **Save intent**. Avant de tester vos modifications, cliquez sur **Build** pour construire à nouveau le bot.

Maintenant, faisons un petit test avec le chatbot. Je vais l'interroger sur les articles que je peux passer en note de frais pour mon voyage.

![Image de l'implémentation de l'IA et de l'interaction avec le chatbot, récupérant les réponses aux requêtes depuis S3 via la base de connaissances Bedrock](https://cdn.hashnode.com/res/hashnode/image/upload/v1764494425584/65ec0a99-e438-44d3-ad62-965d82200142.png align="center")

L'image ci-dessus me montre en train d'avoir une conversation avec le chatbot. J'ai envoyé un énoncé pour l'intention de bienvenue, et il a répondu par un message de bienvenue. Lorsque j'ai interrogé le chatbot sur les articles que je peux passer en frais pour le voyage, il a extrait les informations de la base de connaissances Bedrock, qui est connectée au bucket S3 hébergeant les documents de politique de voyage.

Essayez d'expérimenter avec d'autres questions comme « Combien coûte mon voyage ? » ou « Puis-je emmener mes animaux de compagnie ? ».

Vous voulez ajouter une véritable interface utilisateur web à votre bot ? Suivez les instructions étape par étape dans ce [dépôt GitHub](https://github.com/aws-samples/aws-lex-web-ui).

Pour information - vous devriez supprimer les ressources telles que votre base de connaissances, votre bucket S3 et votre magasin de vecteurs (naviguez vers **Amazon OpenSearch Service** > **Serverless** > **Dashboard** et supprimez la collection de vecteurs de la base de connaissances) pour éviter d'encourir des frais indésirables de la part d'AWS.

## Conclusion

Vous venez de construire un chatbot propulsé par l'IA qui extrait des réponses de vos propres sources de données. Plus de réponses génériques ou d'informations obsolètes. En combinant Amazon Lex, Bedrock, S3 et le RAG, vous avez créé un système qui comprend réellement votre documentation/base de connaissances et fournit des réponses précises et contextuelles.

Le véritable pouvoir ici ne réside pas seulement dans la pile technologique, mais dans ce que vous pouvez en faire. Étendez cette approche pour gérer les requêtes de support client, les questions RH internes, la documentation produit ou tout scénario où vous avez besoin de réponses instantanées et précises à partir de votre propre base de connaissances.

Ce n'est que le début. Expérimentez avec différents modèles de fondation dans Bedrock, enrichissez votre base de connaissances avec plus de documents ou affinez vos intentions pour gérer des conversations plus complexes. L'infrastructure est construite, il est maintenant temps de la personnaliser pour votre cas d'utilisation spécifique.

Si vous avez trouvé ce tutoriel utile, n'hésitez pas à le partager avec votre équipe ou vos collègues développeurs.