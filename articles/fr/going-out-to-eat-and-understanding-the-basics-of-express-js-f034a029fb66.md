---
title: Sortir manger et comprendre les bases d'Express.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-03T17:27:55.000Z'
originalURL: https://freecodecamp.org/news/going-out-to-eat-and-understanding-the-basics-of-express-js-f034a029fb66
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iMkFu1T52fkSnlZDlCrvkQ.jpeg
tags:
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Sortir manger et comprendre les bases d'Express.js
seo_desc: 'By Kevin Kononenko

  If you have ever visited a sit-down restaurant, then you can understand the basics
  of Express. But if you are just starting to build your first Node.js back end…you
  might be in for a bumpy ride.

  Yes — it is certainly easier to lear...'
---

Par Kevin Kononenko

Si vous êtes déjà allé dans un restaurant avec service à table, alors vous pouvez comprendre les bases d'Express. Mais si vous commencez tout juste à construire votre premier back-end Node.js… vous pourriez avoir quelques difficultés.

Oui — il est certainement plus facile d'apprendre Node si vous avez déjà de l'expérience avec JavaScript. Mais les défis que vous rencontrerez en construisant un back-end sont complètement différents de ceux que vous rencontrez en utilisant JavaScript sur le front-end.

Quand j'ai appris Node, j'ai choisi la voie difficile. J'ai étudié des eBooks, des tutoriels écrits et des vidéos encore et encore jusqu'à ce que je comprenne enfin **pourquoi** je faisais ce que je faisais.

Il existe une méthode plus simple. Je vais utiliser une analogie avec un restaurant pour expliquer quatre parties clés de votre première application Express. [Express.js](https://expressjs.com/) est un framework populaire pour organiser votre code, et je le recommande pour tout débutant. Je vais expliquer plus en détail dans un instant.

Voici les quatre parties clés que nous allons couvrir :

1. Les instructions require
2. Le middleware
3. Le routage
4. App.listen()/ Démarrer le serveur

Dans cette analogie, vous êtes un propriétaire de restaurant cherchant à embaucher un directeur général — la personne qui crée tous les processus et gère l'établissement pour qu'il fonctionne sans accroc et que les clients repartent satisfaits.

Voici un aperçu de ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gWVqib20b1NNzB6vrM-U6w.png)

À la fin, vous comprendrez la fonctionnalité de chaque partie d'une application Express basique.

### Étape 1 : embaucher le directeur (instructions require)

Dans cet exemple, vous êtes le propriétaire du restaurant. Et vous devez embaucher un expert pour gérer les opérations quotidiennes de votre nouveau restaurant. Vous n'êtes certainement pas un expert, et vous ne pouvez pas laisser le personnel de salle et la cuisine se débrouiller seuls.

Si vous voulez gérer un restaurant efficace et sûr, vous avez besoin de quelqu'un pour maintenir votre personnel à une efficacité maximale. Express est le nouveau directeur.

La première partie est assez simple. Comme avec tout autre package NPM, vous devez installer le module express avec npm, puis utiliser une instruction **require** pour charger le module.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VjyG-yoVn9aUYJ_cdN6RYA.png)

Contrairement à de nombreux autres packages NPM, vous devez également utiliser cette ligne :

```
const app = express();
```

C'est parce que vous avez besoin d'une variable pour contenir votre nouvelle application Express. Express ne fait pas partie de Node par défaut.

### Étape 2 : prendre des décisions au restaurant (middleware)

Faisons un pas en arrière. Quelles sont les routines courantes dans les restaurants ? Trois me viennent immédiatement à l'esprit :

1. Installer de nouveaux clients
2. Prendre les commandes de nourriture
3. Présenter l'addition à la fin du repas

Pour chacune d'elles, il y a une série de vérifications à effectuer avant de pouvoir exécuter l'action. Par exemple, avant d'installer des clients, vous devez savoir :

1. Portent-ils une chemise et des chaussures (et un pantalon) ? Sinon, ils ne peuvent pas être installés.
2. S'ils veulent s'asseoir au bar, ont-ils 21 ans (si vous êtes aux États-Unis) ?

Ce n'est pas un bar de plage ! De même, dans votre code, vous devrez valider que les requêtes répondent à certains critères avant de pouvoir continuer. Par exemple, si une personne essaie de se connecter à votre site :

1. A-t-elle un compte ?
2. A-t-elle entré le mot de passe correct ?

C'est là qu'intervient le concept de **middleware**. Les fonctions middleware vous permettent d'agir sur toute requête entrante et de la modifier avant d'envoyer une réponse.

![Image](https://cdn-media-1.freecodecamp.org/images/0*8HIzvtX-DA3C26uv.png)

Dans votre restaurant, vous avez besoin d'une série de règles pour décider si vous devez installer les personnes qui arrivent ou non. Supposons qu'un couple entre par votre porte. Vous avez une règle avant de leur donner une table : portent-ils une chemise et des chaussures ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gqix0p7PBNJ5htTY3sT7OQ.png)

Tout d'abord, vous commencez avec [app.use()](http://expressjs.com/en/api.html#app.use). Cela signifie que ce sont simplement des règles qui doivent être appliquées pour les routes à venir. Elles ne sont pas une requête GET, POST, PUT ou DELETE.

À la ligne 4, vous avez une fonction anonyme avec les paramètres req, res et next. Pour les besoins de ce bloc de code, vous inspectez simplement la requête (req) pour voir si elle a une chemise et des chaussures.

Vous devez également utiliser la fonction next() à la fin parce que vous validez simplement les vêtements ici. Plus tard, dans les routes, vous permettrez aux invités d'obtenir une table réelle.

Aux lignes 5 et 6, vous vérifiez s'ils ont une chemise et des chaussures.

Et aux lignes 7–9, vous ne continuez que s'ils ont les deux.

Le bloc de code ci-dessus manque d'une chose importante : un **chemin**. Il s'agit de la chaîne spécifique incluse avec la requête. Et comme il manque un chemin, il s'exécutera sur chaque requête.

Pouvez-vous imaginer ? Lorsque les clients entraient dans le restaurant… commandaient de la nourriture… demandaient l'addition… les employés seraient obligés de les regarder de haut en bas pour s'assurer qu'ils étaient habillés ! C'est un moyen rapide de faire faillite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fjZKIJYmTIxQmVMURYTW9g.png)

Nous modifions donc la ligne 4 dans l'exemple ci-dessus. Maintenant, nous n'exécuterons ce code que lorsqu'un utilisateur demandera le long de la route '/table'.

L'explication complète :

![Image](https://cdn-media-1.freecodecamp.org/images/1*d1OPYjAlr6mUWtjtMRbk6g.png)

### Étape 3 : exécuter des routines courantes (routage)

Continuons avec l'exemple de l'installation. Jusqu'à présent, nous savons seulement comment valider si quelqu'un doit être installé ou non. Mais nous ne savons pas réellement comment les conduire à une table et les asseoir.

C'est là que les **routes** interviennent. Les routes nous permettent de scripter des actions spécifiques en fonction du **chemin**. Les options sont GET, POST, PUT et DELETE, mais nous nous concentrerons sur GET et POST pour l'instant.

Dans le contexte d'un restaurant, nous devons créer une requête GET afin de choisir une table spécifique et d'installer les invités. Les requêtes GET ne modifient pas ni n'ajoutent à votre base de données. Elles récupèrent simplement des informations en fonction de paramètres spécifiques.

Dans ce cas, supposons que vous devez créer une procédure pour installer un groupe de deux personnes. Le nombre 2 provient de la **requête** du client.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pGvgMABGA1xzrSL9EFGQmQ.png)

D'accord, avant d'expliquer : Oui, cela envoie simplement un message à la fin. Cela n'a pas encore trouvé de table spécifique pour installer le client. Je devrais rechercher dans un tableau une table libre, avoir plus d'histoire… cela dépasse le cadre de ce tutoriel.

À la ligne 12, nous définissons la procédure pour trouver une table lorsqu'un invité **demande** le long de la **route** '/table'. Tout comme l'exemple de middleware ci-dessus, nous avons les paramètres de requête et de réponse disponibles. Il a également un **paramètre**, amount. Dans cet exemple, il est de deux.

En fait, tout ce qui suit la déclaration de fonction à la ligne 12 est techniquement du **middleware** puisqu'il modifie une requête utilisateur. Vous le verrez dans le diagramme à la fin.

À la ligne 13, nous accédons au nombre de personnes dans le groupe à partir des **paramètres** de l'objet de requête. Cela n'est déclaré nulle part puisque la requête provient de l'utilisateur, et nous n'avons aucun code front-end. Voici à quoi pourrait ressembler la requête si cela était une vraie application :

```
req = {  params: {    amount: 2;  }}
```

À la ligne 13, notre variable party accède à la **propriété** amount de l'**objet** params dans la **requête**.

Enfin, à la ligne 14, nous envoyons une **réponse** au client : nous cherchons la table de taille appropriée.

C'est beaucoup à la fois. Voici un diagramme :

![Image](https://cdn-media-1.freecodecamp.org/images/1*k7DkIw1cheKYBwu_AC4SAA.png)

### Étape 3.5 : rendre votre restaurant efficace (routeur)

Maintenant, vous pouvez tracer le chemin complet de la requête à la réponse. Mais à mesure que votre application grandit, vous ne voudrez pas coder les règles pour chaque route individuellement. Vous constaterez que certaines routes partagent les mêmes règles, vous devez donc trouver un moyen d'appliquer un ensemble de règles à plusieurs routes.

En termes d'installation, vous pouvez soit installer vos clients au bar, soit à une table. Ces deux options ont des règles en commun comme chemise + chaussures, mais s'asseoir au bar nécessite que chaque membre du groupe ait 21 ans.

Et, en termes de service aux clients, vous devrez utiliser une procédure légèrement différente pour servir l'entrée, le plat principal et le dîner. Mais ces trois routes ont également beaucoup en commun.

C'est là qu'intervient le **routeur**. Le routeur vous permet de regrouper vos routes afin que vous puissiez créer des règles communes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6Irrxz4EmHaPgVm0JRgVLg.png)

Nous devons créer un middleware pour couvrir chacun de ces cas. Je vais simplement couvrir les cas d'installation pour l'instant, car cela écrasera le code ci-dessus.

Voici l'extrait de code complet :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Pih87WdfXU_PEXkcbsaAIw.png)

Je vais couvrir chaque partie individuellement.

À la ligne 4, nous déclarons notre routeur.

Aux lignes 6 et 14, nous avons maintenant seatingRouter.use() à la place de app.use() pour indiquer que ce **middleware** est uniquement lié aux routes de seatingRouter.

Enfin, à la ligne 21, nous ajoutons plus de middleware pour montrer que chaque route de seatingRouter commence par '/seating'. Ainsi, si quelqu'un demandait une place au bar, le chemin complet serait '/seating/bar'. Cela peut sembler un peu désordonné, car vous pourriez vous attendre à ce que le chemin soit défini lorsque vous créez le routeur à la ligne 4. C'est normal !

Voici cela sous forme de diagramme :

![Image](https://cdn-media-1.freecodecamp.org/images/1*-1x9T6VvBCQihyzwqgnGIA.png)

Et, lorsque vous ajoutez une route GET, elle se place au-dessus de la dernière instruction où vous attribuez des routes au routeur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EPEUF9z94mMlCYXMB6HENA.png)

### Étape 4 : ouvrir pour les affaires (ports)

D'accord, dernière partie. Jusqu'à présent, vous avez embauché un directeur, défini ce qu'il faut faire avant d'accepter les requêtes des clients, et déterminé quoi faire avec des requêtes spécifiques des clients une fois qu'elles arrivent. Maintenant, vous devez simplement déterminer l'adresse de l'emplacement où tout cela se passera.

Votre serveur a des **ports** qui sont un peu comme l'adresse du restaurant lui-même. Puisque votre serveur peut gérer de nombreux types de restaurants (ou scripts côté serveur) à la fois, vous devez lui dire où chaque script doit s'exécuter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xGoTkrNMLnwyh7zR2wbbVA.png)

Dans l'exemple ci-dessus, le port est 3000 et il est situé sur votre ordinateur. Donc si vous tapez :

```
https://localhost:3000/
```

dans votre navigateur, et que vous exécutez votre application Node, le serveur sait exécuter le script spécifique. Dans ce cas, dès que vous entrez l'URL, vous enregistrerez le message dans la console et pourrez utiliser n'importe laquelle de vos **routes**. Si le restaurant lui-même est votre application entière, alors il est maintenant ouvert pour les affaires à l'adresse 3000.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kl9doAbsvsaQNJdFWhc2-Q.png)

Avez-vous aimé cela ? Applaudissez pour que d'autres puissent le découvrir également. Et, si vous voulez être informé lorsque je publierai de futurs tutoriels utilisant des analogies, inscrivez-vous ici :