---
title: Comment implémenter une compétence Alexa avec Spring Boot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T13:06:28.000Z'
originalURL: https://freecodecamp.org/news/implementing-an-alexa-skill-with-spring-boot-also-why-would-you-do-such-a-thing-9992c0797646
coverImage: https://cdn-media-1.freecodecamp.org/images/1*agCi2IBtbBlRZsDfy6KRxA.jpeg
tags:
- name: amazon echo
  slug: amazon-echo
- name: Java
  slug: java
- name: software development
  slug: software-development
- name: spring-boot
  slug: spring-boot
- name: technology
  slug: technology
seo_title: Comment implémenter une compétence Alexa avec Spring Boot
seo_desc: 'By Rafael Fiol

  And why you would do such a thing


  There are two ways to implement custom skills for Alexa.

  The first is the most common and is the Amazon-recommended way. Use AWS Lambda,
  a server-less computer service. There is no shortage of article...'
---

Par Rafael Fiol

#### Et pourquoi vous feriez une telle chose

![Image](https://cdn-media-1.freecodecamp.org/images/1*agCi2IBtbBlRZsDfy6KRxA.jpeg)

Il existe deux façons d'implémenter des compétences personnalisées pour Alexa.

La première est la plus courante et est la méthode recommandée par Amazon. Utilisez [AWS Lambda](https://aws.amazon.com/lambda/), un service informatique sans serveur. Il ne manque pas d'articles et de tutoriels sur le sujet. Ce n'en est pas un.

La deuxième façon est beaucoup moins courante. Il s'agit d'héberger un point de terminaison en utilisant un service web HTTPS que vous gérez. Il est un peu plus difficile de trouver de bons exemples de cette approche. Cet article tentera de faire exactement cela, et utilisera [Spring Boot](https://spring.io/projects/spring-boot) comme base pour l'implémentation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CBS-TT_JYEOWhYsdyr0OWQ.jpeg)
_Configuration du point de terminaison dans la console de développement des compétences Alexa_

Mais avant de plonger dans le **comment**, parlons du **pourquoi** :

* Pourquoi ne pas utiliser AWS Lambda ?
* Pourquoi ignorer une recommandation d'Amazon ?

Ces questions sont importantes. Vous trouverez des tonnes d'exemples et de documentation sur la création de compétences avec Lambda, mais moins pour l'alternative. Il est également important si vous adhérez au principe — ce que je fais — que le monde va vers le [sans serveur](https://en.wikipedia.org/wiki/Serverless_computing). Voici un [excellent article](https://read.acloud.guru/six-months-of-serverless-lessons-learned-f6da86a73526) sur ce sujet par James Beswick. Opter pour la voie HTTPS vous mènera sur un chemin solitaire, mais parfois c'est acceptable.

Voici quelques raisons pour lesquelles vous pourriez vouloir ou devoir emprunter ce chemin solitaire.

* Vous pouvez écrire vos services web Alexa en utilisant n'importe quel langage de programmation.
* Si vous avez déjà des services RESTful déployés et que vous souhaitez tirer parti de cette infrastructure/investissement.
* Si votre [CISO](https://en.wikipedia.org/wiki/Chief_information_security_officer) n'autorise pas les infrastructures hors site ou basées sur le cloud.
* Si vous aimez les chemins solitaires.

Dans mon cas, j'ai décidé d'explorer la voie non-Lambda principalement parce que j'avais déjà une couche de services existante, que je voulais utiliser. Il y a des [POJOs](https://en.wikipedia.org/wiki/Plain_old_Java_object) et des méthodes que je voulais réutiliser, sans avoir à exposer de nouveaux points de terminaison. Bien sûr, j'aurais pu créer des Lambdas qui se contentent de frontaler ces services, et c'est un modèle valide. Mais je ne voulais pas ajouter une autre couche de scripts de déploiement, de tests et de surveillance.

Vous avez probablement vos propres raisons. Si je construisais une nouvelle application [greenfield](https://en.wikipedia.org/wiki/Greenfield_project), je prendrais probablement la voie Lambda.

### Prérequis

Vous utiliserez la [Console de développement Alexa](https://developer.amazon.com/alexa) pour enregistrer votre compétence, définir les intentions et les énoncés, et la tester. J'ai supposé que vous avez déjà créé un compte développeur et que vous pouvez configurer une nouvelle compétence personnalisée dans la console.

### Une compétence Alexa avec Spring Boot

Le reste de cet article vous montrera à quel point il est facile d'ajouter une compétence Alexa à vos applications Spring Boot existantes. Pour démontrer cela, nous créerons une compétence qui recherchera des faits amusants sur une année spécifique ou une année aléatoire. Vous pourrez interagir avec notre compétence en disant des choses comme :

```
Alexa, demande à mon application de démonstration de me dire des anecdotes sur une année aléatoire.Alexa, demande à mon application de démonstration, qu'est-il arrivé en 1984 ? 
```

D'accord, oui, c'est une compétence assez inutile. Mais elle démontrera tous les aspects importants d'une application Alexa, y compris :

* la gestion des intentions personnalisées
* l'utilisation de slots, la gestion des sessions
* la gestion des intentions intégrées

Pour y parvenir, notre exemple de compétence appellera une API tierce gratuite pour rechercher les informations d'anecdotes, en utilisant le merveilleux [NumbersAPI](http://numbersapi.com/#42). Un grand merci à [David](https://twitter.com/divad12) et [Mack](https://github.com/mduan) pour avoir créé ce service amusant.

### Pour commencer

Premières choses d'abord. Ajoutez le [SDK Alexa Skills Kit](https://mvnrepository.com/artifact/com.amazon.alexa/alexa-skills-kit) à votre fichier "pom.xml". Au moment de la rédaction, la dernière version du SDK est la 1.8.1.

```
<dependency>    <groupId>com.amazon.alexa</groupId>    <artifactId>alexa-skills-kit</artifactId>    <version>1.8.1</version></dependency>
```

Le SDK inclut un servlet spécial, nommé `SpeechletServlet`, que vous devrez charger dans le cadre de l'amorçage de l'application. Cela est en fait très facile à faire.

Le servlet est un cheval de bataille. Il gère toutes les [exigences compliquées pour héberger une compétence](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-a-web-service.html), telles que la vérification que la demande a été envoyée par Alexa, la validation de la signature et la vérification du timestamp. Heureusement pour nous, nous n'avons pas à nous occuper de ces maux de tête. Nous devons simplement charger le servlet. Voici comment nous faisons cela :

Simple. Vous pouvez voir ci-dessus que nous avons créé une classe de configuration qui charge notre servlet. À la ligne 10, vous pouvez voir que `SpeechletServlet` est instancié, puis à la ligne 13, il est enregistré avec Spring.

C'est à peu près tout ce que vous devez faire pour charger le servlet.

Comme je l'ai noté, le servlet s'occupe de toutes les communications de handshake compliquées avec Alexa. Et après cela, le servlet délègue la logique métier de l'interaction réelle à un **Speechlet**, que vous devez implémenter. Vous pouvez voir à la ligne 11 que le Speechlet, que j'ai nommé `HandlerSpeechlet`, est assigné au servlet. Ce Speechlet sera invoqué avec chaque interaction Alexa.

Un Speechlet est simplement un POJO qui se conforme à l'interface SpeechletV2 définie dans le SDK Alexa Skills. Voici à quoi ressemble l'interface.

C'est à vous de mettre en œuvre ces quatre méthodes.

Elles sont toutes importantes, mais la plupart du travail se fait dans `OnIntent()`, qui est invoqué lorsque l'utilisateur dit quelque chose de significatif. Si vous êtes nouveau dans le vocabulaire de la programmation Alexa, vous devriez lire [Intents, Utterances, and Slots: The New Vocabulary Needed To Develop For Voice](https://medium.com/screenmedia-lab/utterances-slots-and-skills-the-new-vocabulary-needed-to-develop-for-voice-7428bff4ed79).

### Définition des intentions

Plongez dans la [Console de développement Alexa](https://developer.amazon.com/alexa). Configurez une nouvelle compétence personnalisée dans la console — cette partie est très facile. J'ai nommé ma compétence "MyDemoApp", et sous le menu Invocation, j'ai défini le nom d'invocation de la compétence comme "my demo app".

Rappelons plus tôt dans cet article que j'ai dit que vous pouvez interagir avec notre compétence en disant des choses comme :

```
Alexa, demande à mon application de démonstration de me dire des anecdotes sur une année aléatoire.Alexa, demande à mon application de démonstration, qu'est-il arrivé en 1984 ?
```

Vous pouvez voir que chacune des phrases ci-dessus commence par le mot de réveil ("Alexa") et le nom d'invocation de la compétence ("my demo app").

```
Alexa, demande à mon application de démonstration ...
```

Tout ce qui suit le nom d'invocation de la compétence est connu sous le nom d'**énoncé**. C'est à vous de lister les énoncés dans la console de développement et de mapper ces énoncés à une intention. Une seule intention a normalement de nombreux énoncés, représentant les variations qu'un utilisateur pourrait dire. Par exemple, tous les énoncés suivants sont essentiellement les mêmes :

```
dis-moi des anecdotes sur une année aléatoire.dis quelque chose sur une année quelconque.choisis une année aléatoire.dis-moi quelques anecdotes.dis n'importe quoi sur une année quelconque.
```

Tous ces énoncés signifient la même chose et peuvent donc être mappés à une seule intention. Dans mon application, je l'ai appelée "RandomYearIntent". Voici à quoi cela ressemble dans la console de développement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-jAvV7iIAAnBDazM_TGgTA.png)

### Retour à l'écriture de code

Avec notre première intention définie, il est maintenant temps de revenir à notre application Spring et d'écrire du code. Modifions notre "HandlerSpeechlet". Pour l'instant, sautons les méthodes `onSessionStarted` et `onLaunch` du Speechlet, et plongeons directement dans la méthode `onIntent`.

Parce que notre application gérera éventuellement plusieurs intentions, nous devrons d'abord déterminer quelle intention est invoquée.

À la ligne 10, nous avons maintenant le nom de l'intention. Dans notre exemple jusqu'à présent, cela devrait être `RandomYearIntent`. À ce stade, vous pourriez être tenté d'écrire un tas d'instructions `if-else` contre le nom de l'intention, mais essayons quelque chose d'un peu plus intelligent.

En veillant à ce que nos intentions suivent une convention de nommage spécifique, nous pouvons utiliser un peu de magie Spring pour charger et invoquer des gestionnaires spécialisés pour chaque intention. Ce qui suit n'est pas quelque chose de spécifique au SDK Alexa Skills. C'est juste ma propre façon de gérer plusieurs intentions. Il existe de nombreuses façons de mettre en œuvre cette logique. Voici la mienne.

Commençons par définir une interface que nous utiliserons pour tous nos gestionnaires. Créons `IntentHandler` comme suit :

Ensuite, pour chaque intention, nous créerons une classe qui implémente cette interface. Nous veillerons également à nommer nos classes de la même manière que le nom de l'intention, avec le mot "Handler" ajouté. Par exemple, pour l'intention "RandomYearIntent", nous créerons une classe nommée `RandomYearIntentHandler`_._

D'accord, laissons cela non implémenté pour l'instant. Nous reviendrons à notre "HandlerSpeechlet" pour ajouter du code qui passera le contrôle à notre nouveau "RandomYearIntentHandler". La stratégie de base consiste à s'appuyer sur notre convention de nommage "IntentName" + "Handler".

J'ai supprimé certains détails et la gestion des erreurs du code ci-dessous afin que nous puissions nous concentrer sur les parties importantes. À la fin de cet article, vous trouverez un lien vers mon dépôt GitHub avec le code complet.

Consultez les lignes 12 et 13 ci-dessous, qui construisent le nom de la classe, puis demandent à Spring de trouver un bean enregistré avec ce nom. Ensuite, enfin, à la ligne 17, nous passons le contrôle à ce gestionnaire.

### RandomYearIntentHandler

Nous avons maintenant la plomberie en place pour appeler nos gestionnaires d'intentions spécialisés. Revenons à l'implémentation de notre "RandomYearIntentHandler". Cette intention particulière est simple. Voici l'implémentation complète.

Simple ! Avez-vous remarqué l'annotation à la ligne 1 ? Cette annotation `@Component` est un petit truc sympa qui indiquera à Spring de créer une instance de cette classe en tant que Bean. C'est ainsi que nous pouvons accéder au gestionnaire dans notre Speechlet, en utilisant `beanFactory.getBean(handlerBeanName)`.

À la ligne 11, nous créons un nombre aléatoire entre 1900 et l'année en cours. Ensuite, nous appelons l'API [Numbers API](http://numbersapi.com/#42) pour obtenir des anecdotes sur cette année.

Aux lignes 14 et 15, nous créons une `Card` et un `Speech`. La `Card` est ce qui est affiché dans votre application mobile Alexa — ou à l'écran dans l'Echo Show. Le Speech est ce qui est dit à l'utilisateur.

`AlexaUtils` est une classe simple que j'ai créée. Je n'entrerai pas dans les détails ici, mais vous pouvez la consulter sur [GitHub](https://github.com/raf66/AlexSpringBootWeb/blob/master/src/main/java/net/fiol/demo/alexa/utils/AlexaUtils.java).

### C'était facile — qu'en est-il des slots ?

Les slots sont essentiellement des **variables dans les énoncés**. Revenez aux deux intentions de notre application. La deuxième intention, que j'appellerai "SpecificYearIntent", permet à l'utilisateur de dire n'importe quelle année. Par exemple :

```
Alexa, demande à mon application de démonstration, qu'est-il arrivé en 1984 ?
```

Dans l'énoncé ci-dessus, l'année est très variable. Nous ne voulons pas définir un énoncé pour chaque année possible. Au lieu de cela, nous définirons cet énoncé en utilisant un slot, comme suit :

```
Alexa, demande à mon application de démonstration, qu'est-il arrivé en {Year} ?
```

{Year} représente un nombre. En revenant à notre console de développement, nous configurerons une nouvelle intention "SpecificYearIntent" avec ses énoncés associés comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CDFfMDV8z_cQQeoSeMaisw.jpeg)
_Énoncés de SpecificYearIntent_

J'ai défini un Slot nommé "Year", qui est de type "AMAZON.NUMBER". Maintenant, dans mon gestionnaire, je peux récupérer facilement la valeur du slot par son nom.

La ligne 13 est celle où nous résolvons le slot de l'année. Le reste est du code Java standard, qui suit le même modèle que la première intention — appeler le service NumbersAPI pour l'année et gérer la réponse.

### Sessions et état

Je ne suis pas entré dans les méthodes `OnSessionStarted` ou `OnLaunch` du Speechlet dans cet article, mais j'ai inclus une implémentation pour `OnLaunch` dans le [projet d'exemple sur GitHub](https://github.com/raf66/AlexSpringBootWeb).

Vous pouvez utiliser l'objet `Session` pour stocker des variables qui seront conservées entre les invocations en mode conversation. Le mode conversation se produit lorsque l'utilisateur invoque votre compétence mais ne prononce pas un énoncé reconnu. Par exemple :

```
Alex, ouvre mon application de démonstration.
```

```
>> Bonjour. Voici quelques choses que vous pouvez dire : Dites-moi quelque chose sur une année aléatoire. Ou, qu'est-il arrivé en mille neuf cent quatre-vingt-neuf ?
```

```
Qu'est-il arrivé en 1984 ?
```

```
>> 1984 est l'année où la Communauté économique européenne met 1,8 million de livres à disposition pour aider à combattre la famine en Éthiopie le 25 octobre. 
```

```
>> Que puis-je vous dire d'autre ? Dites "Aide" pour quelques suggestions.
```

```
Annuler.
```

```
>> D'accord. Au revoir.
```

Vous remarquerez dans mon code source que j'ai une méthode nommée `setConversationMode`. Elle définit simplement une variable dans la Session, me permettant de savoir que nous sommes en mode conversation.

### Résumé

Écrire des compétences Alexa avec Spring Boot est assez facile et peut être un moyen puissant de réutiliser votre infrastructure existante. [Téléchargez l'application complète depuis GitHub](https://github.com/raf66/AlexSpringBootWeb) pour plus de détails.

Et si vous êtes dans la région du sud de la Floride, vous pouvez utiliser ma [compétence Cutler Stew](https://www.amazon.com/Rafael-Fiol-Cutler-Stew/dp/B0793FRYJG) (construite avec Spring Boot) pour savoir quand et où mon groupe Cutler Stew se produira prochainement.