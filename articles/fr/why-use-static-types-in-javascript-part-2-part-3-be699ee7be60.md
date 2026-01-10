---
title: Pourquoi utiliser des types statiques en JavaScript ? Les avantages et les
  inconvénients
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-09T16:26:22.000Z'
originalURL: https://freecodecamp.org/news/why-use-static-types-in-javascript-part-2-part-3-be699ee7be60
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rvQDY9Lytjg7oUENPdzUyw.png
tags:
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Pourquoi utiliser des types statiques en JavaScript ? Les avantages et
  les inconvénients
seo_desc: 'By Preethi Kasireddy

  We covered a lot of ground in Part 1! With syntax out of the way, let’s finally
  get to the fun part: exploring the advantages and disadvantages of using static
  types.

  The Advantages of using static types

  Static types offer many b...'
---

Par Preethi Kasireddy

Nous avons couvert beaucoup de terrain dans [la partie 1](https://medium.com/@preethikasireddy/why-use-static-types-in-javascript-part-1-8382da1e0adb#.gqg3xut8w) ! Maintenant que la syntaxe est derrière nous, passons enfin à la partie amusante : explorer les avantages et les inconvénients de l'utilisation des types statiques.

### **Les avantages de l'utilisation des types statiques**

Les types statiques offrent de nombreux avantages lors de l'écriture de programmes. Explorons-en quelques-uns.

#### Avantage #1 : Vous pouvez détecter les bugs et les erreurs tôt

La vérification des types statiques nous permet de vérifier que les invariants que nous avons spécifiés sont vrais sans avoir à exécuter réellement le programme. Et si l'un de ces invariants est violé, cela sera découvert avant l'exécution plutôt que pendant.

Un exemple rapide : supposons que nous avons une fonction simple qui prend un rayon et calcule l'aire :

Maintenant, si nous devions passer un rayon qui n'est pas un nombre (par exemple, 'je suis méchant')...

...nous obtiendrions `NaN`. Si une partie de la fonctionnalité dépendait de cette fonction `calculateArea` pour toujours retourner un nombre, alors ce résultat pourrait conduire à un bug ou à un plantage. Ce n'est pas très agréable, n'est-ce pas ?

Si nous avions utilisé des types statiques, nous aurions pu spécifier les types exacts d'entrée(s) et de sortie pour la fonction :

Essayez de passer autre chose qu'un nombre dans notre fonction `calculateArea` maintenant, et Flow nous enverra un message pratique :

Maintenant, nous sommes assurés que la fonction n'acceptera que des nombres valides en entrée et retournera un nombre valide en sortie.

Parce que le vérificateur de types vous indique lorsqu'il y a des erreurs pendant que vous codez, c'est beaucoup plus pratique (et beaucoup moins coûteux) que de découvrir le bug une fois le code livré à vos clients.

#### Avantage #2 : Vous obtenez une documentation vivante

Les types servent de documentation vivante et respirante pour nous-mêmes et pour les autres utilisateurs de notre code.

Pour voir comment, regardons cette méthode que j'ai un jour trouvée dans une grande base de code sur laquelle je travaillais :

Au premier regard (et au deuxième et troisième), je n'avais aucune idée de comment utiliser cette fonction.

Est-ce que quote est un `number` ? Ou un `boolean` ? Est-ce que payment method est un `object` ? Ou peut-être est-ce une `string` représentant le type de méthode de paiement ? Est-ce que la fonction retourne la date sous forme de `string` ? Ou sous forme d'objet `Date` ?

Aucune idée.

Ma solution à l'époque était d'évaluer la logique métier et de fouiller dans la base de code jusqu'à ce que je comprenne. Mais c'est beaucoup de travail juste pour comprendre comment fonctionne une simple fonction.

D'un autre côté, si nous avions écrit quelque chose comme :

Il devient immédiatement clair quel type de données la fonction prend en entrée et quel type de données elle retourne en sortie. Cela démontre comment nous pouvons utiliser les types statiques pour communiquer l'_intention_ de la fonction. Nous pouvons dire aux autres développeurs ce que nous attendons d'eux, et voir ce qu'ils attendent de nous. La prochaine fois que quelqu'un utilisera cette fonction, il n'y aura aucune question posée.

Il y a un argument à faire que l'ajout de commentaires de code ou de documentation pourrait résoudre le même problème :

Cela fonctionne. Mais c'est beaucoup plus verbeux. Au-delà de la verbosité, les commentaires de code comme celui-ci sont difficiles à maintenir car ils sont peu fiables et manquent de structure — certains développeurs peuvent écrire de bons commentaires, d'autres peuvent écrire des commentaires obscurs, et certains peuvent oublier de les écrire du tout.

Il est particulièrement facile d'oublier de les mettre à jour lors d'un refactoring. Les annotations de type, en revanche, ont une syntaxe et une structure définies et ne peuvent jamais devenir obsolètes — elles sont encodées dans le code.

#### Avantage #3 : Cela réduit la gestion des erreurs compliquée

Les types aident à éliminer la gestion des erreurs compliquée. Revisitons notre fonction `calculateArea` pour voir comment.

Cette fois, je vais lui faire prendre un tableau de rayons et calculer l'aire pour chaque rayon :

Cette fonction fonctionne, mais ne gère pas correctement les arguments d'entrée invalides. Si nous voulions nous assurer de bien gérer les cas où l'entrée n'est pas un tableau valide de nombres, nous aboutirions à une fonction qui ressemble à :

Wow. C'est beaucoup de code pour une petite fonctionnalité.

Mais avec les types statiques, nous pourrions simplement faire :

Maintenant, la fonction ressemble à ce qu'elle était à l'origine sans tout le désordre visuel de la gestion des erreurs.

Facile à voir l'avantage, n'est-ce pas ? :)

#### Avantage #4 : Vous pouvez refactoriser avec une plus grande confiance

Je vais expliquer cela à travers une anecdote : je travaillais dans une très grande base de code une fois et il y avait une méthode définie sur la classe `User` que nous devions mettre à jour — spécifiquement, nous devions changer l'un des paramètres de la fonction d'une `string` à un `object`.

J'ai fait le changement, mais j'avais des pieds froids pour valider le changement — il y avait tant d'invocations de cette fonction éparpillées dans la base de code que je ne savais pas si j'avais mis à jour toutes les instances correctement. Et si j'en avais manqué une, profondément enfouie dans un fichier d'assistance non testé ?

La seule façon de le savoir était de livrer le code et de prier pour qu'il ne plante pas avec des erreurs.

L'utilisation de types statiques aurait évité cela. Cela m'aurait donné l'assurance et la tranquillité d'esprit que si j'avais mis à jour une fonction et, en retour, mis à jour les définitions de types, le vérificateur de types serait là pour moi pour attraper toutes les erreurs que j'aurais manquées. Tout ce que j'aurais à faire serait de passer en revue ces erreurs de type et de les corriger.

#### Avantage #5 : Cela sépare les données du comportement

Un avantage moins discuté des types statiques est qu'ils aident à séparer les données du comportement.

Revisitons notre fonction `calculateAreas` avec des types statiques :

Réfléchissons à la manière dont nous composerions cette fonction. Parce que nous annotons les types, nous sommes obligés de penser d'abord au type de données que nous avons l'intention d'utiliser afin de pouvoir définir correctement les types d'entrée et de sortie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iemrVKr16FMed25x6-bfBA.png)

Ce n'est qu'ensuite que nous implémentons la logique :

![Image](https://cdn-media-1.freecodecamp.org/images/1*PFxhb9gct7GYWBlBY0lofg.png)

Cette capacité à exprimer précisément les données séparément du comportement nous permet d'être explicites sur nos hypothèses et de communiquer plus précisément notre intention, ce qui soulage une partie de la charge mentale et apporte une certaine clarté mentale au programmeur. Sans cela, nous sommes laissés à suivre cela mentalement d'une manière ou d'une autre.

#### Avantage #6 : Cela élimine une catégorie entière de bugs

L'une des erreurs ou bugs les plus courants que nous rencontrons en tant que développeurs JavaScript sont les erreurs de type à l'exécution.

Par exemple, supposons que notre état initial de l'application est défini comme :

Et supposons que nous faisons ensuite un appel API pour récupérer les messages afin de remplir notre `appState`. Ensuite, notre application a un composant de vue excessivement simplifié qui prend les `messages` (définis dans notre état) en tant que prop et affiche le compteur de non lus et chaque message sous forme de liste :

Si l'appel API pour récupérer les messages échoue ou retourne `undefined`, nous aboutirons à une erreur de type en production :

`TypeError: Cannot read property 'length' of undefined`

... et votre programme plante. Vous perdez un client. Dommage.

Voyons comment les types peuvent nous aider. Nous allons commencer par ajouter des types Flow à notre état d'application. Je vais aliaser le type `AppState` puis utiliser cela pour définir l'état :

Puisque notre API pour récupérer les messages est connue pour être peu fiable, ici nous disons que `messages` est un type `maybe` d'un tableau de chaînes.

Même chose que la dernière fois — nous récupérons nos messages de l'API peu fiable et les utilisons dans notre composant de vue :

Sauf que maintenant, Flow attraperait notre erreur et se plaindrait :

Hé, mon ami !

Parce que nous avons défini `messages` comme un type `maybe`, nous disons qu'il est autorisé à être `null` ou `undefined`. Mais il ne nous permet toujours pas d'effectuer des opérations dessus (comme `.length` ou `.map`) sans faire une vérification `null` car si la valeur de `messages` était en fait `null` ou `undefined`, nous aboutirions à une erreur de type si nous effectuons une opération dessus.

Alors, retournons et mettons à jour notre fonction de vue pour qu'elle ressemble à :

Flow sait maintenant que nous avons géré le cas où les messages sont `null` ou `undefined`, et donc le code vérifie les types avec 0 erreur. Les erreurs de type à l'exécution sont enfin mortes :)

#### Avantage #7 : Cela réduit le nombre de tests unitaires

Nous avons vu précédemment comment les types statiques peuvent aider à éliminer la gestion des erreurs compliquée car ils garantissent les types d'entrée et de sortie. En conséquence, ils réduisent également le nombre de tests unitaires.

Par exemple, retournons à notre fonction `calculateAreas` typée dynamiquement avec gestion des erreurs :

Si nous étions des programmeurs diligents, nous aurions peut-être pensé à tester les entrées invalides pour nous assurer qu'elles sont gérées correctement dans notre programme :

... et ainsi de suite. Sauf qu'il est très probable que nous oubliions de tester certains cas limites — puis c'est notre client qui découvre le problème. :(

Puisque les tests sont uniquement basés sur les cas auxquels nous pensons tester, ils sont existentiels et faciles à contourner.

D'un autre côté, lorsque nous sommes obligés de définir des types :

... non seulement nous sommes assurés que notre intention correspond à la réalité, mais ils sont également simplement plus difficiles à échapper. Contrairement aux tests basés sur l'empirisme, les types sont universels et difficiles à contourner.

Le grand tableau ici est : les tests sont excellents pour tester la logique, et les types pour tester les types de données. Lorsqu'ils sont combinés, la somme des parties est supérieure au tout.

#### Avantage #8 : Cela fournit un outil de modélisation de domaine

L'un de mes cas d'utilisation préférés pour les types est la modélisation de domaine. Un modèle de domaine est un modèle conceptuel d'un domaine qui inclut à la fois les données et le comportement sur ces données. La meilleure façon de comprendre comment vous pouvez utiliser les types pour faire de la modélisation de domaine est de regarder un exemple.

Supposons que j'ai une application où un utilisateur a une ou plusieurs méthodes de paiement pour effectuer des achats sur la plateforme. Il existe trois types de méthodes de paiement qu'ils sont autorisés à avoir (Paypal, Carte de crédit, Compte bancaire).

Nous allons donc d'abord aliaser ces trois types de méthodes de paiement différents :

Maintenant, nous pouvons définir notre type `PaymentMethod` comme une union disjointe avec trois cas :

Ensuite, modélisons notre état d'application. Pour garder cela simple, supposons que les données de notre application ne consistent qu'en les méthodes de paiement de l'utilisateur.

Est-ce suffisant ? Eh bien, nous savons que pour obtenir les méthodes de paiement de l'utilisateur, nous devons faire une requête API, et selon où nous en sommes dans le processus de récupération, notre application aura différents états. Il y a donc en fait quatre états possibles :

1) Nous n'avons pas encore récupéré les méthodes de paiement  
2) Nous sommes en train de récupérer les méthodes de paiement  
3) Nous avons réussi à récupérer les méthodes de paiement  
4) Nous avons essayé de récupérer mais il y a eu une erreur lors de la récupération des méthodes de paiement

Mais notre simple type `Model` avec `paymentMethods` ne couvre pas tous ces cas. Au lieu de cela, il suppose que `paymentMethods` existe toujours.

Hmmm. Y a-t-il un moyen de modéliser notre état d'application pour qu'il soit l'un de ces quatre cas, et seulement ces quatre cas ? Jetons un coup d'œil :

Nous avons utilisé un type d'union disjointe pour définir notre état comme l'un des quatre scénarios décrits ci-dessus. Remarquez comment j'utilise une propriété `type` pour déterminer dans lequel des quatre états se trouve notre application. Cette propriété `type` est en fait ce qui fait de cela une union disjointe. En utilisant cela, nous pouvons faire une analyse de cas pour déterminer quand nous avons les méthodes de paiement et quand nous ne les avons pas.

Vous remarquerez également que je passe un type générique `E` et `D` dans l'état de l'application. Le type `D` représentera la méthode de paiement de l'utilisateur (`PaymentMethod` défini ci-dessus). Nous n'avons pas défini le type `E`, qui sera notre type d'erreur, alors faisons cela maintenant :

Maintenant, nous pouvons modéliser notre domaine d'application comme :

En résumé, la signature de notre état d'application est maintenant `AppState<E, D>` où E est de la forme `HttpError` et D est `PaymentMethod`. Et `AppState` a quatre (et seulement ces quatre) états possibles : `NotFetched`, `Fetching`, `Failure` et `Success`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IDG2HHn55BhiZk8KMADLsQ.png)

Je trouve ce type de modélisation de domaine utile pour réfléchir et construire des interfaces utilisateur contre certaines règles métier. Les règles métier nous disent que notre application ne peut être que dans l'un de ces états. Cela nous permet de représenter explicitement notre état d'application et garantit qu'il ne sera que dans l'un des états prédéfinis. Et lorsque nous construisons à partir de ce modèle (par exemple, pour créer un composant de vue), il devient évident que nous devons gérer les quatre états possibles.

De plus, le code devient auto-documenté — vous pouvez regarder les cas d'union et comprendre immédiatement comment l'état de l'application est structuré.

### Les inconvénients de l'utilisation des types statiques

Comme tout le reste dans la vie et en programmation, la vérification des types statiques comporte ses compromis.

Il est important que nous les comprenions et les reconnaissions afin de pouvoir prendre une décision éclairée sur le moment où les types statiques ont du sens et quand ils n'en valent simplement pas la peine.

Voici quelques-unes de ces considérations :

#### Inconvénient #1 : Les types statiques nécessitent un investissement initial pour apprendre

Une raison pour laquelle JavaScript est un langage si fantastique pour les débutants est qu'il ne nécessite pas que l'étudiant apprenne un système de types entier avant de pouvoir être productif dans le langage.

Lorsque j'ai initialement appris Elm (un langage fonctionnel à typage statique), les types m'ont souvent gêné. Je rencontrais constamment des erreurs de compilation liées à mes définitions de types.

Apprendre à utiliser le système de types efficacement a été la moitié de la bataille pour apprendre le langage lui-même. En conséquence, les types statiques ont rendu la courbe d'apprentissage d'Elm plus raide que celle de JavaScript.

Cela compte surtout pour les débutants où la charge cognitive de l'apprentissage de la syntaxe est à son apogée. Ajouter des types au mélange peut submerger un débutant.

#### Inconvénient #2 : La verbosité peut vous ralentir

Les types statiques rendent souvent les programmes plus verbeux et encombrés.

Par exemple, au lieu de :

Nous devrions écrire :

Et au lieu de :

Nous devrions écrire :

Évidemment, cela peut ajouter des lignes de code supplémentaires. Mais il y a quelques arguments contre le fait que cela soit un réel inconvénient.

Premièrement, comme nous l'avons mentionné précédemment, les types statiques aident à éliminer une catégorie entière de tests. Certains développeurs considéreraient cela comme un compromis parfaitement raisonnable.

Deuxièmement, comme nous l'avons vu précédemment, les types statiques peuvent parfois éliminer la gestion des erreurs compliquée et, à leur tour, réduire considérablement l'encombrement visuel du code.

Il est difficile de dire si la verbosité est un réel argument contre les types, mais c'est un point à garder à l'esprit.

#### Inconvénient #3 : Les types prennent du temps à maîtriser

Il faut du temps et beaucoup de pratique pour apprendre à spécifier au mieux les types dans un programme. De plus, développer un bon sens de ce qui vaut la peine d'être suivi statiquement et de ce qu'il faut garder dynamique nécessite également une réflexion, une pratique et une expérience minutieuses.

Par exemple, une approche que nous pourrions adopter est d'encoder la logique métier critique avec des types, tout en laissant les morceaux de logique éphémères ou non importants dynamiques pour éviter une complexité inutile.

Cette distinction peut être difficile à faire, surtout lorsque des développeurs moins expérimentés avec les types prennent des décisions à la volée.

#### Inconvénient #4 : Les types statiques peuvent entraver le développement rapide

Comme je l'ai mentionné précédemment, les types m'ont un peu gêné lorsque j'apprenais Elm — particulièrement lorsque j'ajoutais du code ou faisais des changements. Être constamment distrait par des erreurs de compilation rendait difficile le sentiment de faire des progrès.

L'argument ici est que la vérification des types statiques pourrait amener un programmeur à perdre le focus trop souvent — et comme nous le savons, le focus est clé pour écrire de bons programmes.

Non seulement cela, mais les vérificateurs de types statiques ne sont pas toujours parfaits. Parfois, vous rencontrez des situations où vous savez ce que vous devez faire et la vérification des types se met simplement en travers.

Je suis sûr qu'il y a d'autres compromis que je manque, mais ceux-ci étaient les plus importants pour moi.

### À venir, [la conclusion finale](https://medium.com/@preethikasireddy/why-use-static-types-in-javascript-part-4-b2e1e06a67c9#.cb2z6mty8)

Dans [la section finale](https://medium.com/@preethikasireddy/why-use-static-types-in-javascript-part-4-b2e1e06a67c9#.cb2z6mty8), nous conclurons en discutant s'il est judicieux d'utiliser des types statiques.

Je vous verrai [là-bas](https://medium.com/@preethikasireddy/why-use-static-types-in-javascript-part-4-b2e1e06a67c9#.cb2z6mty8).