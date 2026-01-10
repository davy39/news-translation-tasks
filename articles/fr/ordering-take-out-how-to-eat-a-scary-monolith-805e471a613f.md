---
title: 'Commander à emporter : Comment dévorer un monolithe effrayant'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-15T22:45:34.000Z'
originalURL: https://freecodecamp.org/news/ordering-take-out-how-to-eat-a-scary-monolith-805e471a613f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6fjILAnGqbbPAvkPfZOzvg.jpeg
tags:
- name: Microservices
  slug: microservices
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: 'Commander à emporter : Comment dévorer un monolithe effrayant'
seo_desc: 'By Alan Ridlehoover

  Martin Fowler said:


  Almost all the successful microservice stories have started with a monolith that
  got too big and was broken up.


  You can add our story to that list.

  My team and I just built a new messaging service. It replace...'
---

Par Alan Ridlehoover

Martin Fowler [a déclaré](https://www.martinfowler.com/bliki/MonolithFirst.html) :

> Presque toutes les histoires réussies de microservices ont commencé avec un monolithe qui est devenu trop grand et a été divisé.

Vous pouvez ajouter notre histoire à cette liste.

Mon équipe et moi venons de construire un nouveau service de messagerie. Il a remplacé un sous-système vieillissant dans notre application principale. Nous avons modélisé le nouveau service sur des concepts de la vie réelle. Cela a considérablement simplifié le modèle de données, débloquant de nouvelles fonctionnalités qui auraient été un défi à construire avec l'ancien modèle de données.

En cours de route, nous avons appris quelques choses que nous aimerions partager...

![Image](https://cdn-media-1.freecodecamp.org/images/MaXabuxVfnzuqOetILf5NhS1fmlts8AbyCLo)

### Notre estimation la plus pessimiste était follement optimiste

Notre estimation la plus conservatrice pour la durée du projet était de trois mois. Il en a pris dix.

Pour être juste, nous avions estimé que toute l'équipe prendrait trois mois pour compléter le travail. Mais en réalité, nous avons entrepris plusieurs projets à la fois. Nous avons continué la maintenance en cours du sous-système hérité, et même ajouté de nouvelles fonctionnalités. Ainsi, avec moins de la moitié des ressources, l'estimation initiale aurait dû être plus longue.

Cela dit, nous avons sous-estimé le travail. Nous avons sous-estimé le travail lié au désenchevêtrement du sous-système du monolithe. Nous avons commencé par rechercher des références aux classes appartenant au sous-système. Nous avons fini par examiner les requêtes SQL qui référenceaient les tables de la base de données sous-jacente. C'est à quel point le sous-système était étroitement couplé au reste de l'application.

**Leçon apprise :** Faites attention à _tous_ les points d'intégration. Il y en a probablement plus que vous ne le pensez.

![Image](https://cdn-media-1.freecodecamp.org/images/jcZnblemwjZBQ2trF9dpJWd5haPFYbphLrow)

### Construire un fossé autour du sous-système dans le monolithe

Dans _Domain Driven Design_, Eric Evans décrit un motif appelé la Couche Anti-Corruption. Cette couche est un mur entre deux sous-systèmes. Aucun sous-système ne parle directement à l'autre. Ils parlent tous les deux au mur. Suivre ce motif empêche les sous-systèmes de se mélanger.

Pour nous, d'autres sous-systèmes avaient métastasé dans le nôtre. Nous avions besoin d'un moyen de les déconnecter sans modifier leur fonctionnalité. Nous nous sommes tournés vers la Couche Anti-Corruption pour nous inspirer.

Notre solution : nous avons enveloppé une couche de façade autour de notre sous-système dans le monolithe. Cela a placé un fossé autour du sous-système, empêchant l'accès sauf par des interfaces définies. Cela nous a également permis de tester l'intégration des appels à la façade. Nous avons maintenu ces tests tout au long, même après avoir basculé vers le nouveau service.

Comme mentionné ci-dessus, cela a été de loin la partie la plus difficile de l'extraction du service. Tirer la moitié d'une requête SQL brute derrière une façade est un travail difficile :

D'abord, vous devez comprendre toute la requête, certaines faisant des centaines de lignes. Ensuite, vous extrayez les parties de la requête qui accèdent à l'ancien sous-système. Puis, vous les convertissez dans le nouveau modèle de données. Vous étendez le nouveau service pour supporter cette nouvelle requête. Enfin, vous intégrez les résultats avec le reste de la requête SQL originale. Si vous faites cela correctement, le code appelant ne remarque aucune différence.

**Leçon apprise :** Lors de la construction d'une application, il est important de maintenir des frontières. L'encapsulation est importante. Ce point est évident en dehors du monolithe. Mais il est encore plus important _à l'intérieur_ du monolithe. C'est la seule façon de garder le système flexible, afin que vous puissiez faire de la place pour de nouvelles fonctionnalités par le refactoring.

![Image](https://cdn-media-1.freecodecamp.org/images/rAlpgJ4-e13zDCzGJAFxfRsqwjneOWivEEuN)

### Exécuter les deux systèmes en parallèle

Nous avons exécuté les deux systèmes en parallèle pendant des mois tout en travaillant vers la parité des fonctionnalités. Nous avons pu faire cela parce que nous avons créé la façade mentionnée ci-dessus. Nous avons envoyé des requêtes à la façade à travers à la fois le sous-système hérité et le nouveau service. Comparer les résultats nous a permis de trouver (et de corriger) des incohérences de données. Cela nous a également donné un test de stress en conditions réelles contre des données de production en direct.

**Leçon apprise :** Nous avons trouvé la plupart de nos bugs de cette manière. Il n'y a pas de substitut aux charges de travail de production. Nous admettons que cela a augmenté les coûts de développement. Mais trouver les bugs avant de mettre le système en production en valait chaque centime.

![Image](https://cdn-media-1.freecodecamp.org/images/oBKskiY3Cni6yDQfCtAj50HcvrzKg7riCrdz)

### Utiliser des drapeaux de fonctionnalité pour le déploiement progressif

Un drapeau de fonctionnalité est une valeur booléenne qui active une fonctionnalité lorsqu'elle est activée et la désactive lorsqu'elle est désactivée. Les systèmes typiques de drapeaux de fonctionnalité vous permettent d'activer le drapeau pour des sous-ensembles de vos utilisateurs. Cela vous permet de déployer la fonctionnalité progressivement, plutôt que tout à la fois.

Notre implémentation a utilisé quatre drapeaux séparés :

* Un drapeau contrôlait s'il fallait écrire dans le nouveau système. Cela nous a permis d'exécuter les systèmes en parallèle. Nous avons activé ce drapeau très tôt dans le processus, nous donnant les avantages décrits ci-dessus.
* Un autre drapeau contrôlait s'il fallait lire les données du nouveau service. Ainsi, nous pouvions tester la fonctionnalité avant de l'activer globalement.
* Les deux derniers drapeaux contrôlaient quel système pouvait accéder à nos fournisseurs de messagerie tiers. Un drapeau désactivait le sous-système hérité. L'autre activait le nouveau service. Nous avons séparé ces drapeaux pour pouvoir désactiver les deux systèmes en même temps, en cas de problème majeur. (Nous n'avons pas eu à utiliser cette fonctionnalité. Mais nous sommes toujours contents de l'avoir construite.)

Enfin, l'utilisation de drapeaux de fonctionnalité nous a permis de déployer le nouveau service à un client à la fois. Cela a réduit les risques et empêché des perturbations excessives de l'entreprise.

**Leçon apprise :** Utilisez des drapeaux de fonctionnalité séparés pour l'écriture et la lecture d'un service. Cela vous permet de commencer à exécuter le service en parallèle avec le système hérité. Et, dans notre cas, l'ajout de drapeaux supplémentaires pour empêcher l'envoi de courriels en double était crucial.

![Image](https://cdn-media-1.freecodecamp.org/images/z5ciHTnv-lW9AORCgzx9pdiHcubvX9EAsiNV)

### Ajouter la journalisation, la gestion des exceptions et la surveillance tôt

L'une des premières choses que nous avons construites dans le nouveau service était un logger. Ensuite, nous avons ajouté la gestion des exceptions. Cela s'est avéré crucial lors du débogage du système. Nous l'avons trouvé particulièrement utile à travers la frontière du service.

Nous avons ajouté la surveillance plus tard pour nous donner une fenêtre sur notre processus d'importation de données. Son ajout a été facile grâce à notre logger centralisé.

**Leçon apprise :** Centralisez votre journalisation et votre gestion des exceptions, et construisez-les tôt. Vous vous remercierez plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/HZWJyhA6TsmtkdSHRcIoVRO6vnzzIxSLwG6V)

### Attendez-vous à des problèmes lors de la migration de vos données

Nous avons décidé de porter nos données dans le nouveau service, afin qu'il n'y ait qu'un seul système de référence. Nous l'avons fait en envoyant des messages au nouveau service, testant ainsi l'interface sous charge lourde.

La grande majorité des données a été migrée correctement. Mais il y avait de nombreux cas limites valides. Chaque fois que nous identifiions l'un des cas limites, nous ajustions la migration et la relancions.

En fin de compte, nous avions environ 700 enregistrements (sur 1,2 million) restants que nous ne pouvions pas expliquer. La grande majorité datait de plusieurs années. Ces données ne correspondaient à aucun des cas particuliers que nous avions identifiés et résolus. Après avoir passé quelques jours dessus, nous avons décidé de marquer les enregistrements comme "échoués" et de continuer.

**Leçon apprise :** Les données de production sont désordonnées. La plupart sembleront correctes. Certaines ne le seront pas. Plus les données sont anciennes, plus il est difficile de les migrer. Des enregistrements seront manquants. Les clés étrangères n'existeront pas. Il faut simplement s'adapter. Prenez les meilleures décisions, les plus conviviales pour l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/4etUQXX-ktD33z-PoW3dgJgYmjwibMCn2ZAP)

### Utiliser des UUID déterministes et des migrations idempotentes

Lorsque vous avez deux systèmes différents fonctionnant en parallèle, vous avez besoin d'un espace d'identification partagé. N'importe quel UUID fera l'affaire. Mais nous avons choisi d'utiliser des UUID déterministes pour supporter des migrations idempotentes. Pour générer un UUID déterministe, vous fournissez un espace de noms et un attribut unique. Étant donné les mêmes données, l'algorithme produit toujours le même UUID.

Dans notre cas, la façade dans l'application principale génère les UUID déterministes. Ensuite, elle envoie l'UUID au service pour stockage. À l'intérieur du service, nous avons indexé ce champ pour empêcher les doublons. Cela rend l'idempotence possible.

**Leçon apprise :** Vos données de production seront imprévisibles. Alors que vous résolvez les cas particuliers, vous devrez exécuter vos migrations encore et encore. L'utilisation d'UUID déterministes rend cela possible.

![Image](https://cdn-media-1.freecodecamp.org/images/RaN-4SHUcVD7X8ohmabLvlA933hVU6J6mBvB)

### Utiliser des files d'attente

Introduire un nouveau service signifie introduire un autre point de défaillance. Nous voulions nous protéger contre les petites pannes de service. Nous avons donc décidé de communiquer avec le service via une file d'attente. En utilisant une file d'attente robuste, nous avons obtenu une certaine tolérance aux pannes en cas d'indisponibilité du service. Nous avons également choisi une file d'attente FIFO pour garantir l'ordre des opérations. Cela empêche une mise à jour de précéder une création, ou de suivre une suppression. Cela nous a également permis d'accélérer notre processus d'importation de données en mettant à l'échelle horizontalement.

**Leçon apprise :** Il y a plusieurs avantages à utiliser une file d'attente robuste. La tolérance aux pannes apporte une tranquillité d'esprit. Et la mise à l'échelle horizontale vous permet de suivre la demande.

![Image](https://cdn-media-1.freecodecamp.org/images/3PnX0cTLctAh7DBHQoyxPycmOExnNxZga7zq)

### Utiliser des disjoncteurs

Lire des données de manière asynchrone via une file d'attente nécessite que l'appelant comprenne les rappels asynchrones. JavaScript est, bien sûr, très bon pour cela. Mais Ruby ne l'est pas. Et dans ce cas, c'est le monolithe qui appelle le service via une file d'attente.

Considérez une requête du front-end pour récupérer des données. Le monolithe recevrait cette requête et placerait un message dans une file d'attente avec un identifiant de corrélation. Le service répondrait ensuite (sur une file d'attente différente) avec les résultats et le même identifiant de corrélation. Mais le worker qui traite la réponse n'aurait pas de poignée sur la requête. Vous devriez donc pousser les données vers le front-end (probablement en utilisant des sockets).

En d'autres termes, nous aurions dû réécrire notre front-end pour recevoir des données via des sockets. Malheureusement, nous n'avions pas le temps de reconstruire le front-end de notre application pour qu'il fonctionne ainsi. Nous avons donc choisi d'utiliser HTTP pour les opérations de lecture. Cela a bien fonctionné, jusqu'à ce que cela ne fonctionne plus.

Lors des tests, un bug dans le processus de déploiement a mis le nouveau service hors ligne. Cela a empêché le monolithe de se charger dans notre environnement de staging. Pourquoi ? Parce que nous initialisions les données à partir du service lorsque nous chargions la première page. Comme le service était hors ligne, toutes les requêtes dépassaient le délai d'attente. La solution était d'utiliser le motif du disjoncteur.

Les disjoncteurs enveloppent les appels aux services externes. Si l'appel fonctionne, rien ne se passe. Mais si l'appel échoue avec certaines exceptions (comme un délai d'attente ou une erreur serveur), le disjoncteur se déclenche. Tant qu'il est déclenché, le disjoncteur n'appelle pas le service. Au lieu de cela, il retourne une valeur de retour codée en dur comme `nil` ou `[]` ou `{}` pendant une période de refroidissement. Une fois la période de refroidissement expirée, le disjoncteur commence à appeler le service à nouveau. S'il est de retour, c'est génial ! Sinon, le disjoncteur se déclenche à nouveau.

**Leçon apprise :** Si vous devez utiliser HTTP, protégez le système plus large des pannes de service. Les disjoncteurs sont un mécanisme pour le faire.

![Image](https://cdn-media-1.freecodecamp.org/images/mTAX0RC7RdFhjIeyJmJoAROtssQliybEWTll)

### Parrainage exécutif

Le succès des projets à long terme dépend souvent du parrainage exécutif. Nous avons eu la chance que notre VP Produit et notre VP Ingénierie soient tous deux en accord avec nos plans. Ils nous ont fait une grande confiance. Et lorsque le projet a commencé à sembler plus grand que prévu, ils nous ont soutenus. Nous n'aurions pas pu terminer notre travail sans leur soutien.

Pourquoi nos sponsors exécutifs étaient-ils prêts à se battre pour nous ? Plusieurs raisons. Mais l'une des plus importantes est que nous avons été ouverts et honnêtes dans nos communications avec eux. Ils savaient où en était le projet et ils savaient ce que nous devions faire.

**Leçon apprise :** Lorsque vous vous lancez dans un projet à long terme et à haut risque, assurez-vous d'avoir le soutien de votre direction. Assurez-vous qu'ils comprennent les avantages ainsi que les risques. Et communiquez en continu. Cela construit la confiance, dont vous aurez besoin si vous voulez réussir.

### Que ferions-nous différemment ?

Nous pensions avoir fait notre diligence raisonnable avant de proposer le projet. Nous avons trouvé chaque référence aux modèles utilisés dans le sous-système. Mais nous n'avons pas recherché de références directes aux noms des tables sous-jacentes dans les instructions SQL brutes. C'était une négligence. Nous le ferons définitivement la prochaine fois.

Si nous pouvions remonter le temps, nous isolerions l'ancien sous-système _à l'intérieur_ du monolithe. Encapsuler le sous-système simplifierait le processus d'extraction. En fait, cela aurait même pu le rendre inutile, puisque nous aurions pu refactoriser en place.

### Alors, le referions-nous ?

C'était un long voyage, c'est sûr. Extraire notre sous-système du monolithe était plus difficile que nous l'avions prédit en raison d'un couplage véritablement épique. Nous avons fait le travail de découplage par nécessité. Ce n'était pas agréable. Cela ressemblait à une corvée.

Mais travailler avec le nouveau service est un rêve. Le code est très bien factorisé. Nous avons une couverture de test très élevée. Et nous avons une logique de domaine bien définie qui correspond à des cas d'utilisation spécifiques. Ainsi, nous pouvons dire ce que fait l'application en regardant une seule classe. Cela signifie que l'extension du service est aussi simple que l'ajout d'une autre classe de domaine et de tests pour celle-ci.

Mais le referions-nous ?

En tant qu'ingénieurs ? Nous le referions définitivement. Le projet a conduit à des améliorations majeures de la productivité et de la satisfaction des développeurs. Le compromis en valait la peine pour nous en termes de satisfaction au travail. En fait, nous voyons déjà des opportunités pour extraire plusieurs petits services.

En tant qu'organisation ? Nous sommes très satisfaits des résultats obtenus. Les clients sont heureux que nous livrions des fonctionnalités longtemps demandées que nous n'avions pas pu livrer auparavant. La direction est heureuse qu'il n'y ait eu aucun problème de production. Et l'équipe est ravie d'être libérée du monolithe.

Cela dit, ce projet a été un investissement significatif pour nous à notre stade. Nous devrons voir un retour sur investissement solide avant de nous lancer dans un autre pari à grande échelle sur l'extraction de services.

Une version de cet article a été publiée pour la première fois sur [SourceCode](https://sourcecode.entelo.com/), notre blog sur l'ingénierie dans l'industrie du recrutement.

Je tiens à remercier [Fito von Zastrow](https://www.freecodecamp.org/news/ordering-take-out-how-to-eat-a-scary-monolith-805e471a613f/undefined), [Jason Rosendale](https://www.freecodecamp.org/news/ordering-take-out-how-to-eat-a-scary-monolith-805e471a613f/undefined), [Ryan A Booth](https://www.freecodecamp.org/news/ordering-take-out-how-to-eat-a-scary-monolith-805e471a613f/undefined) et [Cole Goeppinger](https://www.freecodecamp.org/news/ordering-take-out-how-to-eat-a-scary-monolith-805e471a613f/undefined), qui ont tous apporté des contributions inestimables à cet article.

Et merci à vous ! Vous gagnez un prix pour avoir lu jusqu'ici. Mentionnez cet article en ma présence pour un autocollant gratuit !