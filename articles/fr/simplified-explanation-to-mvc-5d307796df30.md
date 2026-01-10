---
title: Qu'est-ce que le MVC, et en quoi est-ce comme un magasin de sandwichs ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-07T22:44:12.000Z'
originalURL: https://freecodecamp.org/news/simplified-explanation-to-mvc-5d307796df30
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f060_Azpyo--3fiHUjotmg.gif
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que le MVC, et en quoi est-ce comme un magasin de sandwichs ?
seo_desc: 'By Adam Wattis

  In today’s Internet, websites tend to be interactive, dynamic, and serve some sort
  of function. They can be more than a static HTML and CSS page. Here’s where the
  Model View Controller (MVC) architectural pattern comes in.

  User interac...'
---

Par Adam Wattis

Dans l'Internet d'aujourd'hui, les sites web tendent à être interactifs, dynamiques et servent une sorte de fonction. Ils peuvent être plus qu'une simple page HTML et CSS statique. C'est là que le modèle architectural **Modèle-Vue-Contrôleur** (MVC) entre en jeu.

L'interaction de l'utilisateur permet des cas d'utilisation qui seraient impossibles avec une page chargée de manière statique. C'est pourquoi, dans le développement web moderne, il est important de comprendre comment les pages dynamiques sont créées. Peut-être que la clé de cela est la familiarité avec le modèle architectural MVC.

Si vous êtes débutant en développement web, des termes tels que « modèle architectural » peuvent sembler intimidants et abstraits. Mais l'idée générale derrière le MVC est en fait très intuitive. Je vais faire de mon mieux pour l'expliquer de cette manière dans cet article.

### Est-il important de comprendre le MVC ?

À mon avis, la réponse à cette question est oui.

Le MVC est important à comprendre car c'est la structure de base sur laquelle la plupart des applications web sont construites. La même chose est également vraie pour les applications mobiles et les programmes de bureau.

Il existe de nombreuses variations autour de l'idée de base du MVC. Le [concept initial](http://heim.ifi.uio.no/~trygver/themes/mvc/mvc-index.html) a été créé vers 1978 chez Xerox PARC par [Trygve Reenskaug](https://en.wikipedia.org/wiki/Trygve_Reenskaug). Il était destiné à aider un utilisateur final à manipuler et contrôler un système informatique sous-jacent de manière plus visuelle et intuitive.

Le MVC atteint cet objectif en permettant à un utilisateur d'interagir avec une interface utilisateur. Cela permet la manipulation et le contrôle du système.

![Image](https://cdn-media-1.freecodecamp.org/images/p0m3rXF8jwWN1eREpdQ-j3UmDA6gbXf19vLY)
_Diagramme original du MVC_

### Le concept de haut niveau

Sans utiliser de mots compliqués, je vais maintenant expliquer l'idée de base derrière le MVC à travers un cas d'utilisation simple.

Imaginez que vous êtes dans un magasin de sandwichs. Vous vous approchez du comptoir et regardez le menu.

![Image](https://cdn-media-1.freecodecamp.org/images/DtIsu4ej81psfO0B6Wmo4Jb7rOH8aU-p99lo)
_Menu de sandwichs très simple_

Vous décidez que vous voulez le sandwich à la dinde (en fait, vous pouvez déjà imaginer le croquer). Alors vous dites au commis votre commande.

Le commis sait exactement ce que vous voulez lorsque vous commandez le sandwich à la dinde. Il se retourne vers le poste de préparation des sandwichs et dit aux personnes là-bas ce qu'elles doivent savoir pour remplir votre commande.

L'équipe de préparation des sandwichs dispose de nombreuses ressources. Le jambon, la dinde, le thon, la salade et le fromage peuvent tous aller dans les sandwichs. Ils prennent les ingrédients nécessaires pour votre commande et les assemblent pour faire le sandwich à la dinde que vous avez commandé.

Une fois le sandwich terminé, il vous est remis. Vous avez maintenant le sandwich à la dinde que vous vouliez.

### Une explication

Dans cet exemple précédent, il y avait trois objets distincts et séparés qui représentent chacun une partie de notre MVC :

* Le poste de préparation des sandwichs (Modèle)
* Le sandwich terminé que vous avez reçu à la fin (Vue)
* Le commis (Contrôleur)

![Image](https://cdn-media-1.freecodecamp.org/images/uHgRPiyifEHQjXI-hj2LgSYPChoj86JIlsHI)
_Flux d'activités assez simple_

Lorsque vous avez commandé votre sandwich, vous aviez une idée distincte de ce à quoi vous vous attendiez comme résultat final : un sandwich à la dinde (**vue**).

C'est la même chose lorsque vous êtes sur un site web. Par exemple, sur Facebook, vous pouvez appuyer sur le bouton 'Amis' pour voir une liste de vos amis. Vous vous attendez à ce que votre liste d'amis apparaisse, et vous pouvez déjà la visualiser dans votre esprit.

Lorsque vous appuyez sur le bouton 'Amis', vous faites une demande aux serveurs de Facebook. La demande est de vous servir votre liste d'amis, tout comme vous avez demandé votre sandwich au commis (**contrôleur**).

Votre demande arrive sur les serveurs de Facebook. Elle atteint leur contrôleur, qui tente de la résoudre. Il récupère ensuite tous vos amis dans une base de données, tout comme le préparateur de sandwichs (**modèle**) prend tous les ingrédients.

Ces ressources (les données de votre liste d'amis) sont assemblées en une réponse. Cela est similaire à la manière dont le préparateur de sandwichs a assemblé tous les ingrédients en un sandwich terminé (**vue**).

Cette liste d'amis vous est ensuite envoyée pour consommation, comme le sandwich l'a été à la fin de votre commande.

#### Résumé

Le commis est le contrôleur :

* Il connaît toutes les combinaisons possibles de sandwichs que vous pouvez commander
* Il recueille vos informations et envoie une commande à résoudre

Les préparateurs de sandwichs sont les modèles :

* Ils savent quels articles sont nécessaires pour assembler votre sandwich terminé

Le sandwich est la vue :

* C'est la « chose » que l'utilisateur final reçoit finalement

### Utilisation d'un framework web

**Contrôleur :**
Le contrôleur gère les requêtes entrantes. Dans un framework web, cela serait une déclaration d'URL spécifiques qui mappent à des fonctionnalités spécifiques qui composent votre demande.

```
Exemple d'URLswebsite.com/profile/ --> retourne votre profilwebsite.com/friends/ --> retourne la liste des amiswebsite.com/friend={userName}/ --> retourne un ami spécifique
```

**Modèle :**
Voici à quoi ressemblent vos données en back-end.

```
User:- userName- firstName- lastName- friends
```

**Vue :**
Il s'agit du modèle HTML qui est retourné après que votre demande soit résolue. Si la demande est réussie, vous devriez obtenir une page avec vos amis. Sinon, vous pourriez obtenir une page 404 'Non trouvé'.

```
<ul>  <li>Friend 1: {friendList[0].userName}</li>  <li>Friend 2: {friendList[1].userName}</li>  <li>Friend 3: {friendList[2].userName}</li>  ...</ul>
```

### Conclusion

Lors de l'interaction avec un système, vous êtes généralement en mesure de **C**réer, **R**écupérer, **M**ettre à jour et **S**upprimer des objets dans la base de données sous-jacente. Cela est souvent abrégé en « **CRUD** ». Ici, nous avons examiné la récupération de données.

Je n'ai pas expliqué ici comment un utilisateur peut modifier les données dans la base de données (le **C**, **U** et **D** dans **CRUD**). Habituellement, vous êtes en mesure d'ajouter, de mettre à jour et de supprimer des choses sur un site web.

La fonctionnalité pour cela est à peu près la même que celle expliquée ci-dessus. La différence est que vos données sont attachées à votre demande au contrôleur.

J'espère que vous avez maintenant une compréhension plus claire de ce qu'est l'architecture MVC et de son fonctionnement.

Si vous avez trouvé cette explication utile, ou si vous avez des questions ou des idées sur la façon d'améliorer cet article, n'hésitez pas à commenter !