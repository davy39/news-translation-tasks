---
title: Comment créer votre propre liste d'abonnés sans serveur avec Go et AWS
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-11-16T19:37:12.000Z'
originalURL: https://freecodecamp.org/news/build-your-own-serverless-subscriber-list-with-go-and-aws
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/envelope.png
tags:
- name: AWS
  slug: aws
- name: email
  slug: email
- name: golang
  slug: golang
- name: serverless
  slug: serverless
seo_title: Comment créer votre propre liste d'abonnés sans serveur avec Go et AWS
seo_desc: "In this article, I'll share how I lovingly built a subscription sign up\
  \ flow with email confirmation that doesn’t suck. You can do it, too. \nIf you want\
  \ to see it in action, you can now subscribe to my email list on victoria.dev.\n\
  Now, I'll show you h..."
---

Dans cet article, je vais partager comment j'ai construit avec amour un flux d'inscription avec confirmation par email qui ne déçoit pas. Vous pouvez le faire aussi. 

Si vous voulez le voir en action, vous pouvez maintenant vous abonner à ma liste d'emails sur [victoria.dev](https://victoria.dev/).

Maintenant, je vais vous montrer comment je l'ai construit.

## **Présentation de Simple Subscribe**

Si vous êtes intéressé par la gestion de votre propre liste de diffusion ou newsletter, vous pouvez configurer Simple Subscribe sur vos propres ressources AWS pour collecter des adresses email. 

Cette API open source est écrite en Go et fonctionne sur AWS Lambda. Les visiteurs de votre site peuvent s'inscrire à votre liste, qui est stockée dans une table DynamoDB, prête à être interrogée ou exportée à votre convenance.

Lorsqu'une personne s'inscrit, elle reçoit un email lui demandant de confirmer son abonnement. Cela s'appelle parfois "double opt-in", bien que je préfère le terme "vérifié". 

Simple Subscribe fonctionne sur une infrastructure sans serveur et utilise une AWS Lambda pour gérer les demandes d'abonnement, de confirmation et de désabonnement.

Vous pouvez trouver le [projet Simple Subscribe, avec son code entièrement open source, sur GitHub](https://github.com/victoriadrake/simple-subscribe). Je vous encourage à consulter le code et à suivre ! 

Dans cet article, je vais partager chaque étape de construction, le processus de réflexion derrière les fonctions à responsabilité unique de l'API, et les considérations de sécurité pour un projet AWS comme celui-ci.

## **Comment construire un flux d'abonnement vérifié**

Un processus d'inscription par email non vérifié est simple. Quelqu'un met son email dans une boîte sur votre site web, puis cet email va dans votre base de données. 

Cependant, si je vous ai appris quelque chose sur [la méfiance envers les entrées utilisateur](https://victoria.dev/blog/sql-injection-and-xss-what-white-hat-hackers-know-about-trusting-user-input/), l'idée même d'un processus d'inscription non vérifié devrait vous mettre mal à l'aise. Le spam peut être délicieux lorsqu'il est frit dans un sandwich, mais ce n'est pas amusant lorsqu'il fait grimper votre facture AWS.

Bien que vous puissiez utiliser une stratégie comme un CAPTCHA ou un puzzle pour la vérification humaine, ceux-ci peuvent créer suffisamment de friction pour éloigner vos potentiels abonnés. 

Au lieu de cela, un email de confirmation peut aider à garantir à la fois l'exactitude de l'adresse et la sentience de l'utilisateur.

Pour construire un flux d'abonnement avec confirmation par email, créez des fonctions à responsabilité unique qui satisfont chaque étape logique. Ce sont :

1. Accepter une adresse email et l'enregistrer.
2. Générer un jeton associé à cette adresse email et l'enregistrer.
3. Envoyer un email de confirmation à cette adresse email avec le jeton.
4. Accepter une demande de vérification qui contient à la fois l'adresse email et le jeton.

Pour atteindre chacun de ces objectifs, Simple Subscribe utilise le [SDK AWS officiel pour Go](https://docs.aws.amazon.com/sdk-for-go/api/) pour interagir avec DynamoDB et SES.

À chaque étape, considérez à quoi ressemblent les données et comment vous les stockez. Cela peut aider à gérer des dilemmes comme, "Que se passe-t-il si quelqu'un essaie de s'abonner deux fois ?" ou même [la modélisation des menaces](https://victoria.dev/blog/if-you-want-to-build-a-treehouse-start-at-the-bottom/) comme, "Que se passe-t-il si quelqu'un s'abonne avec une adresse email qui ne lui appartient pas ?"

Prêt ? Décomposons chaque étape et voyons comment la magie opère.

### **S'abonner**

Le processus d'abonnement commence avec un humble formulaire web, comme celui sur la page principale de mon site. Une entrée de formulaire avec les attributs `type="email" required` aide à la validation, [grâce au navigateur](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email#Validation). Lorsqu'il est soumis, le formulaire envoie une requête GET à l'endpoint d'abonnement de Simple Subscribe.

Simple Subscribe reçoit une requête GET à cet endpoint avec une chaîne de requête contenant l'email de l'abonné potentiel. Il génère ensuite une valeur `id` et ajoute à la fois `email` et `id` à votre table DynamoDB.

L'élément de la table ressemble maintenant à :

<table style="margin: 1em auto; padding: 0px; box-sizing: border-box; width: auto; min-width: 100%; border-collapse: collapse; overflow-x: auto; font-size: 17.1px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-style: initial; text-decoration-color: initial;"><thead style="margin: 0px; padding: 0px; box-sizing: border-box;"><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><th style="margin: 0px; padding: 5px; box-sizing: border-box; font-size: 0.9em; text-align: left; ">email</th><th style="margin: 0px; padding: 5px; box-sizing: border-box; font-size: 0.9em; text-align: left;  ">confirm</th><th style="margin: 0px; padding: 5px; box-sizing: border-box; font-size: 0.9em;  text-align: left; ">id</th><th style="margin: 0px; padding: 5px; box-sizing: border-box; font-size: 0.9em; text-align: left;">timestamp</th></tr></thead><tbody style="margin: 0px; padding: 0px; box-sizing: border-box;"><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 5px; box-sizing: border-box; text-align: left; "><code style="margin: 0px; padding: 0.1em 0.3em; box-sizing: border-box; font-size: 0.86em; border-radius: 8px;">subscriber@example.com</code></td><td style="margin: 0px; padding: 5px; box-sizing: border-box; text-align: left; "><em style="margin: 0px; padding: 0px; box-sizing: border-box;">false</em></td><td style="margin: 0px; padding: 5px; box-sizing: border-box; text-align: left; "><code style="margin: 0px; padding: 0.1em 0.3em; box-sizing: border-box; font-size: 0.86em; border-radius: 8px;">uuid-xxxxx</code></td><td style="margin: 0px; padding: 5px; box-sizing: border-box; text-align: left;">2020-11-01 00:27:39</td></tr></tbody></table>

La colonne `confirm`, qui contient un booléen, indique que l'élément est une demande d'abonnement qui n'a pas encore été confirmée. Pour vérifier une adresse email dans la base de données, vous devrez trouver l'élément correct et changer `confirm` en `true`.

Lorsque vous travaillez avec vos données, considérez l'objectif de chaque manipulation et comment vous pourriez comparer une requête entrante aux données existantes.

Par exemple, si quelqu'un fait une demande d'abonnement ultérieure pour la même adresse email, comment la gérer ? 

Vous pourriez dire, "Créer un nouvel élément avec un nouvel `id`." Cependant, cela pourrait ne pas être la meilleure stratégie lorsque votre base de données d'application sans serveur est payée par volume de requêtes.

Étant donné que la [tarification de DynamoDB](https://aws.amazon.com/dynamodb/pricing/) dépend de la quantité de données que vous lisez et écrivez dans vos tables, il est avantageux d'éviter d'accumuler des données excédentaires.

Dans cette optique, il serait prudent de gérer les demandes d'abonnement pour la même adresse email en effectuant une mise à jour plutôt qu'en ajoutant une nouvelle ligne. 

Simple Subscribe utilise en fait la même fonction pour ajouter ou mettre à jour un élément de la base de données. Cela est généralement appelé "update or insert".

Dans une base de données comme SQLite, cela est accompli avec la [syntaxe UPSERT](https://www.sqlite.org/lang_UPSERT.html). Dans le cas de DynamoDB, vous utilisez une opération de mise à jour. Pour le [SDK Go](https://docs.aws.amazon.com/sdk-for-go/api/service/dynamodb/), sa syntaxe est `UpdateItem`.

Lorsqu'une demande d'abonnement en double est reçue, l'élément de la base de données est apparié uniquement sur l'`email`. Si un élément de ligne existant est trouvé, son `id` et son `timestamp` sont écrasés, ce qui met à jour l'enregistrement de la base de données existant et évite d'inonder votre table avec des demandes en double.

### **Comment vérifier les adresses email**

Après avoir soumis le formulaire, l'abonné potentiel reçoit un email de SES contenant un lien. Ce lien est construit en utilisant l'`email` et l'`id` de la table, et prend le format :

```url
<BASE_URL><VERIFY_PATH>/?email=subscriber@example.com&id=uuid-xxxxx

```

Dans cette configuration, l'`id` est un UUID qui agit comme un jeton secret. Il fournit un identifiant que vous pouvez apparier qui est suffisamment complexe et difficile à deviner. Cette approche dissuade les personnes de s'abonner avec des adresses email qu'elles ne contrôlent pas.

Visiter le lien envoie une requête à votre endpoint de vérification avec l'`email` et l'`id` dans la chaîne de requête. 

Cette fois, il est important de comparer à la fois les valeurs `email` et `id` entrantes avec l'enregistrement de la base de données. Cela vérifie que le destinataire de l'email de confirmation initie la requête.

L'endpoint de vérification s'assure que ces valeurs correspondent à un élément de votre base de données, puis effectue une autre opération de mise à jour pour définir `confirm` sur `true`, et met à jour le timestamp. L'élément ressemble maintenant à :

<table style="margin: 1em auto; padding: 0px; box-sizing: border-box; width: auto; min-width: 100%; border-collapse: collapse; overflow-x: auto; font-size: 17.1px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-style: initial; text-decoration-color: initial;"><thead style="margin: 0px; padding: 0px; box-sizing: border-box;"><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><th style="margin: 0px; padding: 5px; box-sizing: border-box; font-size: 0.9em; text-align: left; ">email</th><th style="margin: 0px; padding: 5px; box-sizing: border-box; font-size: 0.9em; text-align: left;  ">confirm</th><th style="margin: 0px; padding: 5px; box-sizing: border-box; font-size: 0.9em;  text-align: left; ">id</th><th style="margin: 0px; padding: 5px; box-sizing: border-box; font-size: 0.9em; text-align: left;">timestamp</th></tr></thead><tbody style="margin: 0px; padding: 0px; box-sizing: border-box;"><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 5px; box-sizing: border-box; text-align: left; "><code style="margin: 0px; padding: 0.1em 0.3em; box-sizing: border-box; font-size: 0.86em; border-radius: 8px;">subscriber@example.com</code></td><td style="margin: 0px; padding: 5px; box-sizing: border-box; text-align: left; "><em style="margin: 0px; padding: 0px; box-sizing: border-box;">true</em></td><td style="margin: 0px; padding: 5px; box-sizing: border-box; text-align: left; "><code style="margin: 0px; padding: 0.1em 0.3em; box-sizing: border-box; font-size: 0.86em; border-radius: 8px;">uuid-xxxxx</code></td><td style="margin: 0px; padding: 5px; box-sizing: border-box; text-align: left;">2020-11-01 00:37:39</td></tr></tbody></table>

### **Comment interroger les emails**

Vous pouvez maintenant interroger votre table pour construire votre liste d'emails. Selon votre solution d'envoi d'emails, vous pouvez le faire manuellement, avec une autre Lambda, ou même depuis la ligne de commande.

Étant donné que les données des abonnements demandés (où `confirm` est `false`) sont stockées dans la table aux côtés des abonnements confirmés, il est important de différencier ces données lors de l'interrogation des adresses email à envoyer. Vous voudrez vous assurer de ne retourner que les emails où `confirm` est `true`.

## **Comment fournir des liens de désabonnement**

De manière similaire à la vérification d'une adresse email, Simple Subscribe utilise `email` et `id` comme arguments de la fonction qui supprime un élément de votre table DynamoDB afin de désabonner une adresse email. 

Pour permettre aux personnes de se retirer de votre liste, vous devrez fournir une URL dans chaque email que vous envoyez qui inclut leur `email` et `id` en tant que chaîne de requête à l'endpoint de désabonnement. Cela ressemblerait à quelque chose comme :

```url
<BASE_URL><UNSUBSCRIBE_PATH>/?email=subscriber@example.com&id=uuid-xxxxx

```

Lorsque le lien est cliqué, la chaîne de requête est transmise à l'endpoint de désabonnement. Si l'`email` et l'`id` fournis correspondent à un élément de la base de données, cet élément sera supprimé.

Fournir une méthode à vos abonnés pour se retirer automatiquement de votre liste, sans aucune intervention humaine nécessaire, fait partie d'une philosophie éthique et respectueuse envers la gestion des données qui vous ont été confiées.

## Comment prendre soin de vos données

Une fois que vous décidez d'accepter les données d'autres personnes, cela devient votre responsabilité de les gérer. Cela s'applique à tout ce que vous construisez. Pour Simple Subscribe, cela signifie maintenir la sécurité de votre base de données et nettoyer périodiquement votre table.

Afin d'éviter de conserver les adresses email où `confirm` est `false` au-delà d'un certain délai, il serait judicieux de configurer une fonction de nettoyage qui s'exécute selon un calendrier régulier. Cela peut être réalisé manuellement, avec une fonction AWS Lambda, ou en utilisant la ligne de commande.

Pour nettoyer, trouvez les éléments de la base de données où `confirm` est `false` et `timestamp` est plus ancien qu'un point particulier dans le temps. Selon votre cas d'utilisation et les volumes de requêtes, la fréquence à laquelle vous choisissez de nettoyer variera.

Selon votre cas d'utilisation, vous pouvez également souhaiter conserver des sauvegardes de vos données. Si vous êtes particulièrement préoccupé par l'intégrité des données, vous pouvez explorer la [Sauvegarde à la demande](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_HowItWorks.html) ou la [Récupération à un instant donné](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html) pour DynamoDB.

## Construisez votre base d'abonnés indépendante

Construire votre propre liste d'abonnés peut être une entreprise enrichissante ! Que vous ayez l'intention de lancer une newsletter, d'envoyer des notifications pour du nouveau contenu, ou de créer une communauté autour de votre travail, il n'y a rien de plus personnel ou direct qu'un email de moi à vous.

Je vous encourage à commencer à construire votre base d'abonnés avec Simple Subscribe dès aujourd'hui. Comme la plupart de mes travaux, il est open source et gratuit pour un usage personnel. Plongez dans le code sur [le dépôt GitHub](https://github.com/victoriadrake/simple-subscribe) ou découvrez-en plus sur [SimpleSubscribe.org](https://simplesubscribe.org/).

Si vous avez aimé cet article, j'adorerais le savoir. Rejoignez les milliers de personnes qui apprennent avec moi sur [victoria.dev](https://victoria.dev/). Visitez ou [abonnez-vous via RSS](https://victoria.dev/index.xml) pour plus de projets comme celui-ci.