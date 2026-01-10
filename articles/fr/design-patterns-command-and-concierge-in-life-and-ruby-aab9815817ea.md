---
title: 'Design Patterns : Command et Concierge dans la vie et en Ruby'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-13T16:45:26.000Z'
originalURL: https://freecodecamp.org/news/design-patterns-command-and-concierge-in-life-and-ruby-aab9815817ea
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oHisJCqpKvA2G-t2st7PZw.png
tags:
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: Web Development
  slug: web-development
seo_title: 'Design Patterns : Command et Concierge dans la vie et en Ruby'
seo_desc: 'By Sihui Huang

  The Command Pattern’s definition is a stressful one to look at. The formal definition
  is that it:


  encapsulates a request as an object

  thereby letting you parameterize other objects with different requests, queue or
  log requests, and s...'
---

Par Sihui Huang

La définition du Design Pattern Command est stressante à regarder. La définition formelle est qu'il :

* encapsule une requête en tant qu'objet
* vous permettant ainsi de paramétrer d'autres objets avec différentes requêtes, de mettre en file d'attente ou de journaliser les requêtes, et de supporter des opérations annulables.

Oublions cela pour une seconde et partons à Hawaï.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gaUs2oV-Mv6K5yTfY9GTfA.png)

Et vivons dans un hôtel de luxe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SEPz2ulxuXpSC62G958ZQw.png)

Nous avons passé la journée à la plage, fait de la plongée sous-marine et du tourisme. Il est temps de retourner à l'hôtel pour se détendre, manger et planifier la journée suivante.

Après être retournés à l'hôtel, nous voulons :

1. Obtenir le service en chambre pour le dîner
2. Obtenir le service de blanchisserie car nous n'avons pas apporté de vêtements supplémentaires
3. Obtenir un guide de voyage pour Kauai, l'île où nous allons demain

Nous consultons le menu des services de l'hôtel et trouvons trois articles de service correspondant à nos besoins.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-zYwuRdFHA3oTs-076CAoQ.png)

Nous appelons ensuite la réception pour passer ces trois commandes. Un concierge répond à notre appel, note notre liste de demandes et agit sur chaque demande de service comme indiqué par le menu des services.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7PbUyLZWcULve0IB2gnjkw.png)

Ensuite, chaque membre du personnel exécute selon chaque demande spécifique :

1. Le chef dans la cuisine commence à cuisiner
2. Le département de nettoyage envoie un membre du personnel dans notre chambre pour récupérer nos vêtements
3. Le personnel dans le hall prend un guide de voyage et le livre dans notre chambre

Récapitulons ce qui vient de se passer.

a. Nous avons sélectionné les services que nous voulions dans le menu et les avons soumis à un concierge.

b. Le concierge a noté ces demandes de service sous forme de liste.

c. Après avoir raccroché, instruit par le menu des services, le concierge a envoyé nos demandes aux départements correspondants.

d. Chaque département a exécuté la demande donnée.

### Voyons les actions en Ruby.

1. Nous avons soumis ces trois demandes au concierge :

2. Ces demandes sont entrées dans une liste que le concierge suit :

Voyons cela en action (console) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gef7_F3B3AlSNPR8n-ESLw.png)

Comme nous pouvons le voir, après que `nous` avons soumis trois demandes, ces demandes étaient dans une `liste_de_demandes` prise en charge par `concierge`.

3. Instruits par le menu des services, le concierge a envoyé nos demandes aux départements correspondants.

Le code ci-dessus devrait fonctionner correctement.

Sauf pour une chose...

Cela sent mauvais.

Plus précisément, la partie où nous avons les cas de commutation :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZURBU8cccrssu44O_cq64g.png)

Pourquoi cette partie sent-elle mauvais ?

1. Si l'hôtel offre vingt services, au lieu de trois, la méthode sera vraiment longue.
2. Nous voulons offrir de nouveaux services ou supprimer un service existant. Cependant, chaque fois que nous devons ouvrir la classe `Concierge` et redéfinir la méthode `act_on_requests`.

**La méthode en sait trop et nécessite des changements fréquents**. **Avoir ces deux combinaisons ensemble est presque toujours une mauvaise chose.**

Pourquoi ?

Une méthode qui nécessite des changements fréquents est une méthode que vous devez mettre à jour souvent. Chaque fois que vous mettez à jour un morceau de code est une opportunité d'introduire de nouveaux bugs dans le système.

Lorsque la méthode sait aussi beaucoup de choses — et qu'elle est longue — les chances de la perturber lors de la mise à jour augmentent considérablement. C'est la raison derrière [un principe de conception dont nous avons parlé plus tôt](http://www.sihui.io/design-pattern-factory/) — **encapsuler ce qui varie.**

### Il est temps de refactoriser !

Il doit y avoir une meilleure façon que celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZOZwUbQ4qOP118ZuichbMw.png)

Regardons de plus près et réfléchissons.

Reformulons ce que fait le code en anglais. Nous parcourons les demandes de la liste des demandes. Pour chaque demande, selon son type de service, nous donnons au département correspondant les données liées et exécutons la demande. Essentiellement, nous parcourons les demandes et exécutons chacune d'elles en conséquence.

Mais que se passerait-il si chaque demande savait comment s'exécuter elle-même ?

Alors la méthode pourrait être aussi simple que :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qjmwlq83eoCo144JeexHzQ.png)

Au lieu de laisser la méthode `act_on_requests` décider comment chaque demande doit être traitée, nous distribuons cette responsabilité et cette connaissance à chaque demande et la laissons décider comment elle doit être traitée.

Cela dit, nos demandes pourraient ressembler à ceci :

Et le `Concierge` mis à jour ressemblera à ceci :

Avec les codes mis à jour, voici comment nous, clients de l'hôtel, envoyons des demandes au concierge.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xNsFb62V7sOPCR5bvZJR5g.png)

Il est assez facile de créer un autre service.

Par exemple, l'hôtel nous permet également de réserver un SPA :

Le service supporte non seulement `execute` (faire une réservation de spa) mais aussi `undo` (annuler la réservation).

Disons que l'hôtel propose également une autre façon de demander des services sans avoir à appeler le concierge — un panneau de demande de service :

![Image](https://cdn-media-1.freecodecamp.org/images/1*khdqlv3l_ETG3JW92J9nPw.png)

Nous pouvons simplement appuyer sur le bouton et le service avec un paramètre par défaut sera livré dans notre chambre.

Voici le code pour le `ServicePanel` :

Et voici comment nous pouvons créer un panneau de service :

![Image](https://cdn-media-1.freecodecamp.org/images/1*t3qn7WWidvn44W51A5sNlw.png)

### ??Nous utilisons maintenant le Design Pattern Command ?! ??

Revisitons la définition du Design Pattern Command. Il :

* encapsule une requête en tant qu'objet
* vous permettant ainsi de paramétrer d'autres objets avec différentes requêtes, de mettre en file d'attente ou de journaliser les requêtes, et de supporter des opérations annulables.

> 1. « encapsule une requête en tant qu'objet »

Chacune des classes de services que nous avons créées, `RoomService`, `LaundryService`, `TripPlanningService`, et `SpaReservationService`, est un exemple d'encapsulation d'une requête en tant qu'objet.

Récapitulatif :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KN9SLCFu_m0cjse4CcnuGQ.png)

> 2. « vous permettant ainsi de paramétrer d'autres objets avec différentes requêtes, »

Le `ServicePanel` est un exemple de paramétrage d'un objet avec différentes requêtes.

Récapitulatif :

![Image](https://cdn-media-1.freecodecamp.org/images/1*56FeG3eKTst6X73DgFFj0A.png)

> 3. « mettre en file d'attente ou journaliser les requêtes, »

Nos demandes ont été mises en file d'attente pendant que le concierge les prenait par téléphone.

Récapitulatif :

![Image](https://cdn-media-1.freecodecamp.org/images/1*wCjFrqn2HZiShOzRr70giQ.png)

> 4. et supporter des opérations annulables.

`SpaReservationService` supporte `undo`.

Récapitulatif :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8bQzLGARIgIMCze913npDA.png)

Merci d'avoir lu !

N'oubliez pas de vous abonner. :D

Ceci a été publié à l'origine sur mon blog, [Design patterns in life and Ruby](http://www.sihui.io/design-patterns/).