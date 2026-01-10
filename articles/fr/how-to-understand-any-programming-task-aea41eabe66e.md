---
title: Comment comprendre n'importe quelle tâche de programmation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-18T21:35:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-understand-any-programming-task-aea41eabe66e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oCtk28IdNdpjnyMGiRsfLA.jpeg
tags:
- name: learning
  slug: learning
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment comprendre n'importe quelle tâche de programmation
seo_desc: 'By Justin Fuller

  The day has finally arrived. Is it your first day on your job, or have you been
  doing this for ten years? It doesn’t matter. We all eventually find ourselves with
  a task that we simply do not understand.

  So what should you do? Should...'
---

Par Justin Fuller

Le jour est enfin arrivé. Est-ce votre premier jour de travail, ou le faites-vous depuis dix ans ? Peu importe. Nous nous retrouvons tous, un jour ou l'autre, avec une tâche que nous ne comprenons tout simplement pas.

Alors, que faire ? Doit-on se lancer et espérer que cela fonctionne ? Doit-on immédiatement dire à son patron que l'on ne peut pas faire cela parce que l'on ne comprend pas ?

J'imagine que vous savez que la réponse n'est ni l'une ni l'autre !

En programmation, comme dans toute autre profession, j'ai constaté qu'il est presque impossible de passer une semaine (et parfois même une journée) sans rencontrer un problème que je ne comprends pas.

Mais ne vous inquiétez pas ! J'ai une excellente nouvelle. Non seulement vous pouvez résoudre ce problème, mais cela peut aussi être une bonne chose.

Cela signifie que, d'une certaine manière, vous élargissez vos compétences et vos connaissances au-delà de ce que vous avez fait et connu auparavant.

Dans les paragraphes suivants, je vais détailler comment vous pouvez combler l'écart entre les exigences qui vous ont été données et les connaissances dont vous avez besoin pour accomplir la tâche qui vous a été confiée.

## À propos des « exigences »

Vous avez peut-être remarqué que j'ai utilisé le mot « exigences ». Ce mot peut avoir certaines connotations selon l'endroit où vous travaillez.

D'après mon expérience, les grandes entreprises adorent les exigences et les petites entreprises parfois « ne font pas d'exigences ». Je pense que cela est parfaitement acceptable pour nos besoins ici.

C'est parce qu'en fin de compte, tout ce que nous faisons en tant qu'ingénieurs logiciels, c'est résoudre des problèmes.

Vous pourriez recevoir un rapport détaillé de cent pages sur la façon de résoudre ce problème (j'ai déjà eu une réunion d'une heure sur le texte d'un bouton). Ou peut-être que votre PDG viendra traîner à votre bureau et vous demandera décontracté si vous pouvez résoudre le problème d'ici vendredi.

Dans les deux cas, vous avez reçu une tâche et vous devez être sûr de bien comprendre ce problème pour le traiter correctement !

## À propos des étapes

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-57.png)

Toutes les étapes données ci-dessous ne sont pas nécessaires pour chaque problème. Seuls les problèmes les plus difficiles à comprendre peuvent nécessiter de procéder soigneusement à travers toutes les étapes qui seront discutées dans cet article.

Beaucoup des questions peuvent ne pas être répondables à travers les exigences qui vous ont été données, ou à travers votre expérience personnelle seule.

Vous devrez peut-être demander à d'autres développeurs, votre chef d'équipe, le propriétaire du produit, l'analyste commercial, ou même votre grand-mère. Peut-être devrez-vous tous les interroger avant d'avoir terminé !

Cela dit, ce n'est pas grave. Cela signifie que vous allez rassembler des connaissances dispersées et les condenser pour qu'elles résident en un seul endroit. Cet endroit est en vous et maintenant vous serez en mesure de produire le meilleur résultat possible !

**Un dernier avertissement avant d'apprendre les étapes :** ne formalisez pas trop ce processus. Le but ici est de vous aider à comprendre rapidement un problème. Cela ne devrait pas créer de barrières ou de bureaucratie ! Au lieu de cela, cela devrait vous fournir un plan systématique pour aborder un problème que vous ne comprenez pas.

# La première étape : Analyser la tâche

Dans cette étape, vous chercherez à comprendre ce que l'on vous a demandé de faire. Vous n'essayez pas encore de comprendre comment le faire !

La distinction ici est importante. Il peut être dangereux de se lancer directement dans l'implémentation sans réfléchir à toutes les conséquences, ou pire, sans identifier exactement ce que l'on vous a demandé de faire.

## Classer la tâche

Classer une tâche signifie déterminer quel type de travail vous allez faire pour résoudre ce problème. Voici quelques exemples de types de tâches :

* Correction de bug
* Nouvelle fonctionnalité
* Nouvelle application
* Mission de recherche
* Amélioration des performances

Rappelez-vous que ce ne sont pas toutes les options possibles.

Le but ici est de déterminer quel type de travail on attend de vous. Cela est important car cela a un effet direct sur le travail que vous allez faire.

Cette étape est particulièrement importante pour les exigences vagues. Un exemple d'exigence vague est : « Nous avons besoin d'un moyen de purger les caches de nos clients après une mise à jour du site web. »

Il peut y avoir quelques interprétations possibles.

1. Vous devez immédiatement implémenter un mécanisme de purge de cache afin que les clients voient toujours les dernières mises à jour.
2. Vous devez rechercher toutes les façons dont les caches des clients sont stockés et déterminer la ou les meilleures façons de vider ces caches après chaque mise à jour du site web.
3. Les caches des clients devraient déjà être vidés et vous devez trouver et corriger le bug qui les empêche de se vider.

À ce stade, si vous n'êtes pas absolument sûr de la signification utilisée, vous devriez demander des éclaircissements avant de continuer.

## Énoncer ce qu'est la tâche en une ou deux phrases simples.

Résumé des exigences compliquées comme si l'on vous avait demandé sur quoi vous travaillez aujourd'hui. Peut-être que ce ne sera pas si simple, mais vous devriez pouvoir le résumer en une ou deux phrases.

Si vous ne pouvez pas résumer la tâche, cela signifie probablement que vous allez devoir la diviser en plusieurs tâches. Ainsi, cette étape devient un test pour déterminer si vous avez organisé vos tâches en morceaux suffisamment petits.

Voici un bon exemple de résumé : « Lorsque nous mettons à jour le site, nous ajoutons un numéro unique aux fichiers afin que le navigateur sache qu'il doit utiliser le code le plus récent. »

Cette tâche passe le test de simplicité et vous n'avez probablement pas besoin de créer plusieurs tâches.

Un mauvais exemple pourrait ressembler à : « Lorsque nous mettons à jour le site, nous ajoutons un numéro unique aux fichiers afin que le navigateur sache qu'il doit utiliser le code le plus récent. Nous devons également envoyer un message à notre CDN pour lui indiquer qu'il doit mettre à jour les fichiers. De plus, les applications IOS et Android devront avoir une mise à jour envoyée à l'app store. De plus... »

Celui-ci échoue clairement le test. Il y a beaucoup de travail à faire et il peut être nécessaire de l'identifier et de le suivre séparément.

## Esquisser les grandes parties

Sous la forme qui vous est la plus pratique, vous devez maintenant dresser une liste des principales choses à faire.

Celles-ci doivent encore être des résumés très simples de chaque grande étape.

Celles-ci ne doivent pas être un guide étape par étape ou détaillé de la façon de corriger le problème.

Rappelez-vous que vous analysez toujours la tâche qui vous a été donnée. Je vous recommande de les noter d'une manière ou d'une autre. Personnellement, je les enregistre dans mon application Notes.

Notre tâche de mise en cache est très simple et peut ne pas nécessiter de plan. Pour cet exemple, nous considérerons un problème plus complexe.

Notre prochaine tâche est une nouvelle fonctionnalité : « Chaque utilisateur doit voir une publicité ciblée pour un produit interne. Cette publicité doit être adaptée à ses besoins individuels en fonction des données que nous avons collectées. »

Pour esquisser les grandes parties, vous devrez réfléchir clairement à ce que chaque partie de l'exigence vous fera faire.

* Nos publicités actuelles devront être décomposées de manière à pouvoir être corrélées à une métrique spécifique de l'utilisateur.
* Il devra y avoir un moyen pour notre équipe marketing de mapper de nouvelles publicités à une ou plusieurs données utilisateur (sans codage !)
* Le système devra agréger les métriques concernant un utilisateur qui sont pertinentes pour nos publicités.
* Enfin, vous devez créer un système qui reçoit un identifiant d'utilisateur et produit une publicité.

La beauté d'une liste comme celle-ci est qu'elle peut être utilisée pour vérifier rapidement avec votre équipe ou votre patron ! Donc dans cet exemple, peut-être que vous l'avez présenté à votre chef d'équipe et il a décidé qu'il devait y avoir une pièce majeure supplémentaire :

* Les utilisateurs doivent pouvoir nous dire quand ils ne veulent plus voir certaines publicités.

Car après tout, nous ne voulons pas ennuyer nos utilisateurs bien-aimés ! En prenant le temps de réfléchir à notre tâche pendant quelques minutes, nous avons économisé des heures ou des jours de douleur plus tard en identifiant et en planifiant une tâche importante avant de commencer à coder.

Avant de continuer, je veux aborder une critique possible que vous pourriez avoir.

Vous pourriez penser : « Dans une entreprise correcte, c'est le type de travail qui devrait être fait avant que les exigences n'atteignent le développeur », et je suis définitivement d'accord avec vous !

Cependant, nous ne vivons malheureusement pas dans un monde parfait. Parfois, les exigences ne sont pas toujours complètement élaborées avant d'atteindre un développeur. Cela signifie que nous devons tous faire de notre mieux pour évaluer correctement les exigences avant que le développement ne commence.

## Définir le ou les problèmes que vous essayez de résoudre.

Répondez à la question, « pourquoi quelqu'un utilisera-t-il cela ? », ou « quel problème réel ou perçu du monde réel essaie-je de résoudre ? »

Espérons que la réponse est évidente. Pour notre exemple de cache, vous pourriez dire, « les utilisateurs verront toujours les dernières mises à jour. » Pour l'exemple de publicité, « les utilisateurs verront des publicités pertinentes au lieu de publicités qui ne les intéressent pas. »

Si la réponse n'est pas évidente, il est probablement temps de demander à quelqu'un pourquoi vous faites cette tâche ! Poser cette question mènera soit à une compréhension plus claire de la tâche à accomplir, soit à une réévaluation de ce que l'on vous a demandé de faire.

Espérons que vous voyez les avantages de l'une ou l'autre de ces réponses ! Une compréhension plus profonde du problème et du but vous permettra de prendre des décisions dans votre implémentation qui servent réellement les objectifs de l'entreprise. Identifier les mauvaises solutions ou les problèmes qui n'ont pas de sens évitera les efforts gaspillés sur un travail qui ne résoudrait jamais un problème en fin de compte.

# La deuxième étape : Interpréter et évaluer les exigences

À ce stade, vous devriez avoir une compréhension de ce que vous allez faire et pourquoi vous le faites.

Votre prochaine étape sera de comprendre les détails de ce que vous faites, comment vous êtes censé le faire, et pourquoi vous le faites de cette manière.

## Clarifier tous les termes importants liés à votre tâche.

Vous pourriez constater que cette étape est plus importante si vous êtes un nouveau développeur dans une équipe ou si vous travaillez dans une grande entreprise. Ces deux situations rendent plus probable la présence de termes inconnus dans vos exigences.

Les termes peuvent être des termes commerciaux, comme les noms de produits, de clients ou de processus. Ils peuvent également être des termes de développement comme les noms d'outils, d'applications, de modèles, de services ou de bibliothèques.

Vous devez être sûr de comprendre tous les termes importants, sans aucune ambiguïté, afin de pouvoir être certain que vous implémentez votre tâche correctement.

Vous pourriez comprendre que vous devez créer un moyen d'accéder aux informations agrégées de l'utilisateur, mais comprenez-vous ce que cela signifie de l'ajouter au « dao » ?

Vous pourriez comprendre que vous devez formater les données de la publicité, mais comprenez-vous ce qu'est le « MADF » (Marking advertisement data feed) ?

Moi non plus.

C'est pourquoi vous devez identifier et définir tous les termes importants. Vous avez plus de chances d'implémenter incorrectement la tâche si vous vous trompez sur les définitions.

## Identifier comment la tâche doit être faite

À ce stade, vous devez maintenant commencer à examiner comment la tâche doit être faite. Cette étape peut varier largement en fonction de l'endroit où vous travaillez et de la tâche particulière qui vous a été confiée.

Dans certaines équipes, on ne vous dira pas comment implémenter les exigences, on vous dira simplement quelle fonctionnalité vous devriez obtenir.

D'autres détailleront chaque étape que vous devez suivre.

Le plus probablement, votre expérience se situe quelque part entre les deux.

Si votre équipe ne vous a pas donné d'instructions, vous ne pouvez pas faire grand-chose à cette étape. Si vous avez reçu des instructions, alors à ce stade, vous voudrez commencer à vous familiariser avec les étapes que vous devrez suivre.

Cette étape semble assez évidente, mais l'ordre dans lequel elle arrive est quelque chose à quoi vous devez prêter une attention particulière.

L'inclination naturelle peut être de plonger dans tous les détails de la tâche avant de s'assurer que le but de la tâche est compris.

Puisque vous avez pris le temps de comprendre votre tâche en premier, vous aurez maintenant un objectif plus clair en tête lorsque vous évaluerez les étapes que vous devez suivre.

## Déterminer si les problèmes ont été résolus

C'est là que la phase d'analyse et la phase d'interprétation se rejoignent. Dans la phase d'analyse, vous vous êtes concentré sur les grands objectifs et résultats, le « quoi » et le « pourquoi ».

Dans l'étape d'interprétation, vous vous êtes concentré sur les détails, le « comment ».

La raison pour laquelle cela s'appelle interprétation et évaluation est que vous allez maintenant comparer le « comment » au « quoi » et au « pourquoi ». Vous interprétez les détails en considérant le tableau d'ensemble. Vous évaluerez les détails et déterminerez si le problème original a été résolu.

Demandez-vous : Les étapes que l'on m'a données aboutiront-elles au résultat que votre tâche était censée créer ? Ce résultat résoudra-t-il réellement le problème original ?

Si vous êtes confiant que tous les problèmes sont résolus et que tous les détails ont du sens, vous êtes prêt à commencer votre travail ! Sinon, vous devez passer à la troisième étape pour résoudre tout conflit.

# La troisième étape : Penser de manière critique

À ce stade, vous devriez pouvoir affirmer en toute confiance que vous comprenez le problème et la solution. La toute dernière étape consiste à vous assurer que vous avez la bonne solution.

Afin de créer le meilleur produit possible, nous devrions tous avoir le sentiment d'avoir la responsabilité de parler lorsque quelque chose n'a tout simplement pas de sens.

D'un autre côté, nous ne voulons pas désapprouver à tort. Vous ne devriez pas dire que quelque chose ne va pas parce que « cela semble faux » ou parce que « je ne l'aime pas ». Vous devez avoir des raisons concrètes et bien réfléchies.

Alors, établissons quelques règles de base concernant les désaccords.

## Savoir quand désapprouver

* Ne désapprouvez pas tant que vous ne comprenez pas pleinement.

Ne dites jamais que quelque chose est faux tant que vous n'êtes pas absolument sûr de comprendre ce avec quoi vous n'êtes pas d'accord.

Si vous ne pouvez pas énoncer en toute confiance le problème et la solution prévue, vous ne devriez pas désapprouver. Si vous n'avez pas vérifié votre compréhension, vous ne devriez pas désapprouver. Seulement lorsque vous savez que vous avez la compréhension la plus complète possible devriez-vous commencer à désapprouver.

Si vous constatez que vous n'avez pas toutes les informations dont vous avez besoin, il est peut-être temps de vous arrêter et de revisiter l'une des étapes précédentes avant de dire à quelqu'un que les exigences sont fausses.

* Ne désapprouvez pas pour des questions subjectives. Concentrez-vous sur les problèmes potentiels réels.

« Je n'aime pas la façon dont cela est fait » est subjectif. « Cela causera des problèmes de performance en raison du nombre d'opérations impliquées. » est une raison objective. D'autres exemples de raisons subjectives pourraient inclure : « Ce n'est pas comme cela que je l'ai fait ailleurs » et « J'aurais conçu cette solution légèrement différemment, mais seulement à cause de préférences personnelles. »

* Ayez des explications bien raisonnées de vos désaccords prêtes à être présentées.

Si vous ne pouvez pas expliquer pourquoi quelque chose est faux, pouvez-vous vraiment dire que vous savez qu'il est faux ? Je vous suggère d'écrire les raisons pour lesquelles quelque chose est faux et ce qui peut être fait pour le corriger.

Alternativement, si vous n'avez pas de solution pour le corriger, indiquez clairement dès le début que vous ne savez pas.

Soyez prudent lorsque vous désapprouvez les autres. La majeure partie de votre temps devrait être consacrée à la compréhension et à l'écoute avant de désapprouver.

Si vous avez suivi toutes les étapes jusqu'à ce point, il est très probable que vous ayez une bonne compréhension. Mais prenez grand soin de garder l'esprit ouvert que vous avez peut-être manqué quelque chose !

J'aime commencer les conversations en disant : « Je ne suis pas en désaccord avec vous, je ne comprends tout simplement pas. » Plus tard vient le désaccord si nécessaire, mais espérons jamais avant la compréhension.

## Savoir comment désapprouver

Afin de nous assurer que nous désapprouvons de manière objective, voici quelques mesures qui vous aideront à déterminer si votre désaccord est valide.

Les désaccords objectifs font l'une ou plusieurs des choses suivantes :

* Montrer que la solution est mal informée.
* Montrer que la solution est mal informée.
* Montrer que le problème ou la solution est illogique.
* Montrer que la solution est incomplète.

Être mal informé n'est pas une insulte, mais cela signifie plutôt que des informations manquaient lors de la création d'une solution. Peut-être qu'ils ne savaient pas qu'un système existe actuellement et peut effectuer les actions nécessaires.

Être mal informé signifie que la solution est venue d'informations incorrectes.

Dans ce cas, ils pourraient penser qu'un système existant fait quelque chose qu'il ne fait pas réellement. Par exemple, peut-être que l'équipe SEO (optimisation pour les moteurs de recherche) vous a demandé d'avoir Google indexé une page connectée sur votre application. Google ne peut pas faire cela. Ils ont été mal informés sur ce que fait le crawler de Google.

Un problème ou une solution illogique est celui qui n'a tout simplement pas de sens. En tant que développeur, je pense qu'une demande illogique courante que vous pourriez voir est pour une fonctionnalité qui pourrait en casser une autre. Il pourrait être considéré comme illogique de faire cela car cela nuirait, plutôt que d'aider.

Une solution étant incomplète peut en fait être intentionnelle. En développement logiciel, nous essayons souvent de commencer par faire un MVP (produit minimum viable). Cela signifie que nous pouvons, au début, laisser intentionnellement de côté les fonctionnalités qui ne sont pas absolument nécessaires.

Au lieu de cela, vous ne devriez considérer une solution comme incomplète que si elle ne résout pas le problème immédiat que l'on vous a demandé de corriger, ou si les étapes fournies ne sont pas suffisantes pour créer un produit ou une fonctionnalité fonctionnelle.

# Résumé

Rappelez-vous, ne formalisez pas trop ce processus. Il devrait être rapide et probablement consister à noter quelques pensées dans votre application Notes. Ensuite, cela pourrait éventuellement mener à quelques conversations avec vos collègues pour clarifier ce que vous êtes censé faire. C'est tout !

Voici une liste simplifiée des étapes :

**Étape 1 — Analyser**

* Classer
* Résumé
* Plan
* Définir le problème

**Étape 2 — Interpréter et Évaluer**

* Clarifier les termes
* Identifier les tâches
* Déterminer si le problème sera résolu

**Étape 3 — Penser de manière critique**

* Savoir quand désapprouver
* Savoir comment désapprouver

---

Salut, je suis Justin Fuller. Je suis si heureux que vous ayez lu mon article ! Je dois vous faire savoir que tout ce que j'ai écrit ici est mon opinion personnelle et n'est pas destiné à représenter mon employeur de quelque manière que ce soit. Tous les exemples de code sont les miens et n'ont aucun rapport avec le code de Bank Of America.

J'adorerais aussi avoir de vos nouvelles, n'hésitez pas à me contacter sur [LinkedIn](https://www.linkedin.com/in/justin-fuller-8726b2b1/), [Github](https://github.com/justindfuller), ou [Medium](https://medium.com/@justindanielfuller). Merci encore d'avoir lu !