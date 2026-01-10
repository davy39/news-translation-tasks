---
title: Comment construire des applications React solides avec TDD et la React Testing
  Library
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-07T18:07:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-sturdy-react-apps-with-tdd-and-the-react-testing-library-47ad3c5c8e47
coverImage: https://cdn-media-1.freecodecamp.org/images/0*T8onsKEr4xcSyyQR.
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Comment construire des applications React solides avec TDD et la React
  Testing Library
seo_desc: 'By Ian Wilson

  One thing I struggled with when I started learning React was testing my web apps
  in a way that is both useful and intuitive. I used Enzyme with Jest to shallow render
  a component every time I wanted to test it.

  Of course, I was absolute...'
---

Par Ian Wilson

Une chose avec laquelle j'ai eu du mal lorsque j'ai commencé à apprendre React était de tester mes applications web de manière utile et intuitive. J'utilisais [Enzyme](http://airbnb.io/enzyme/docs/api/) avec [Jest](https://facebook.github.io/jest/) pour rendre un composant de manière superficielle chaque fois que je voulais le tester.

Bien sûr, j'abusais absolument de la fonctionnalité de test de snapshot.

Eh bien, au moins j'ai écrit un test, non ?

Vous avez peut-être entendu quelque part que l'écriture de tests unitaires et d'intégration améliore la qualité du logiciel que vous écrivez. Avoir de mauvais tests, en revanche, engendre une fausse confiance.

Récemment, j'ai assisté à un atelier via [workshop.me](https://workshop.me/) avec [Kent C. Dodds](https://www.freecodecamp.org/news/how-to-build-sturdy-react-apps-with-tdd-and-the-react-testing-library-47ad3c5c8e47/undefined) où il nous a appris à écrire de meilleurs tests d'intégration pour les applications React.

Il nous a également incités à utiliser sa [nouvelle bibliothèque de test](https://github.com/kentcdodds/react-testing-library), en faveur de son accent sur le test de l'application de la même manière qu'un utilisateur la rencontrerait.

Dans cet article, nous allons apprendre à exercer le TDD afin de construire des applications React solides en créant un fil de commentaires. Bien sûr, ce processus s'applique à presque tous les développements logiciels, pas seulement aux applications React ou JavaScript.

### **Installation**

Nous allons commencer par exécuter `create-react-app` et installer les dépendances. Mon hypothèse est que si vous lisez un article sur le test d'applications, vous êtes probablement déjà familier avec l'installation et le démarrage de projets JavaScript. J'utiliserai `yarn` plutôt que `npm` ici.

```
create-react-app comment-feed
```

```
cd comment-feed
```

```
yarn
```

Pour l'instant, nous pouvons supprimer tous les fichiers du répertoire `src` sauf index.js. Ensuite, à l'intérieur du dossier `src`, créez un nouveau dossier appelé `components` et un autre dossier appelé `containers`.

Pour les utilitaires de test, je vais construire cette application en utilisant la [React Testing Library](https://github.com/kentcdodds/react-testing-library) de Kent. Il s'agit d'un utilitaire de test léger qui encourage le développeur à tester son application de la même manière qu'elle sera utilisée.

Comme Enzyme, elle exporte une fonction de rendu, mais cette fonction de rendu fait toujours un montage complet de votre composant. Elle exporte des méthodes d'assistance permettant de localiser des éléments par libellé, texte ou même des identifiants de test. Enzyme le fait également avec son API `mount`, mais l'abstraction qu'elle crée offre en réalité plus d'options, dont beaucoup permettent de s'en tirer en testant les détails d'implémentation.

Nous ne voulons plus tester les détails d'implémentation. Nous voulons rendre un composant et voir si les bonnes choses se produisent lorsque nous cliquons ou changeons quelque chose sur l'interface utilisateur. C'est tout ! Plus de vérification directe des props, de l'état ou des noms de classe.

Installons-les et mettons-nous au travail.

```
yarn add react-testing-library
```

### **Construction du fil de commentaires avec TDD**

Faisons ce premier composant en style TDD. Lancez votre exécuteur de tests.

```
yarn test --watch
```

À l'intérieur du dossier `containers`, nous allons ajouter un fichier appelé CommentFeed.js. À côté, ajoutez un fichier appelé CommentFeed.test.js. Pour le tout premier test, vérifions que les utilisateurs peuvent créer des commentaires. Trop tôt ? D'accord, puisque nous n'avons encore aucun code, nous commencerons par un test plus petit. Vérifions que nous pouvons rendre le fil.

#### **Quelques notes sur react-testing-library**

Tout d'abord, notons la fonction de rendu ici. Elle est similaire à la manière dont `react-dom` rend un composant sur le DOM, mais elle retourne un objet que nous pouvons déstructurer pour obtenir quelques assistants de test sympas. Dans ce cas, nous obtenons `queryByText`, qui, étant donné un texte que nous nous attendons à voir sur le DOM, retournera cet élément HTML.

La [documentation de React Testing Library](https://github.com/kentcdodds/react-testing-library#faq) a une hiérarchie qui devrait vous aider à décider quelle méthode de requête ou d'obtention utiliser. Généralement, l'ordre est le suivant :

* `getByLabelText` (entrées de formulaire)
* `getByPlaceholderText` (uniquement si votre entrée n'a pas de libellé — moins accessible !)
* `getByText` (boutons et en-têtes)
* `getByAltText` (images)
* `getByTestId` (utilisez ceci pour des choses comme le texte dynamique ou d'autres éléments étranges que vous voulez tester)

Chacune de ces méthodes a une méthode associée `queryByFoo` qui fait la même chose, sauf qu'elle ne fera pas échouer votre test lorsqu'elle ne trouve pas un élément. Utilisez celles-ci si vous testez simplement l'**existence** d'un élément.

Si aucune de ces méthodes ne vous donne exactement ce que vous cherchez, la méthode `render` retourne également l'élément DOM mappé à la propriété `container`, vous pouvez donc l'utiliser comme `container.querySelector('body #root')`.

### **Le premier code d'implémentation**

Maintenant, l'implémentation sera assez simple. Nous devons simplement nous assurer que « Comment Feed » est dans le composant.

Cela pourrait être pire — je veux dire, j'étais sur le point d'écrire cet article entier en stylisant des composants. Heureusement, les tests ne se soucient pas trop des styles, donc nous pouvons nous concentrer sur la logique de notre application.

Ce prochain test vérifiera que nous pouvons rendre des commentaires. Mais nous n'avons même pas de commentaires, alors ajoutons également ce composant. Après le test cependant.

Je vais également créer un objet props pour stocker les données que nous pourrions réutiliser dans ces tests.

Dans ce cas, je vérifie que le nombre de commentaires est égal au nombre d'éléments passés dans le CommentFeed. C'est trivial, mais l'échec du test nous donne l'opportunité de créer le fichier Comment.js.

Cela fait passer notre suite de tests au vert afin que nous puissions continuer sans crainte. Tous les honneurs au TDD, le sauveur de notre espèce. Cela fonctionne lorsque nous lui donnons un tableau vide, bien sûr. Mais que se passe-t-il si nous lui donnons de vrais objets ?

Nous devons mettre à jour notre implémentation pour réellement rendre des choses. Assez simple maintenant que nous savons où nous allons, non ?

Ah, regardez cela, notre test passe à nouveau. Voici une belle capture de sa beauté.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vGkFKnUkA9ms5PbaOWoQ_A.png)

Remarquez comment je n'ai jamais dit que nous devrions lancer notre programme avec `yarn start` ? Nous allons garder cela ainsi pendant un moment. Le point est que vous devez sentir le code avec votre esprit.

Le style n'est que ce qu'il y a à l'extérieur — c'est ce qu'il y a à l'intérieur qui compte.

Au cas où vous voudriez démarrer l'application, mettez à jour index.js comme suit :

### **Ajouter un formulaire de commentaire**

C'est là que les choses commencent à devenir plus amusantes. C'est là que nous passons de la vérification somnolente de l'existence de nœuds DOM à faire réellement des choses avec cela et à **valider le comportement**. Tout le reste n'était qu'un échauffement.

Commençons par décrire ce que je veux pour ce formulaire. Il devrait :

* contenir une entrée de texte pour l'auteur
* contenir une entrée de texte pour le commentaire lui-même
* avoir un bouton de soumission
* éventuellement appeler l'API ou tout autre service qui gère la création et le stockage du commentaire.

Nous pouvons prendre cette liste dans un seul test d'intégration. Pour les cas de test précédents, nous avons pris cela plutôt lentement, mais maintenant nous allons accélérer le rythme et essayer de le clouer en un seul coup.

Remarquez comment notre suite de tests se développe ? Nous sommes passés de la codification en dur des props à l'intérieur de leurs propres cas de test à la création d'une usine pour eux.

#### **Arranger, Agir, Affirmer**

Ce test d'intégration suivant peut être divisé en trois parties : arranger, agir et affirmer.

* **Arranger** : créer des props et autres accessoires pour le cas de test
* **Agir** : simuler des changements aux éléments tels que des entrées de texte ou des clics sur des boutons
* **Affirmer** : affirmer que les fonctions souhaitées ont été invoquées le bon nombre de fois, et avec les arguments corrects

Il y a quelques hypothèses faites sur le code, comme le nom de nos libellés ou le fait que nous aurons une prop `createComment`.

Lors de la recherche d'entrées, nous voulons essayer de les trouver par leurs libellés. Cela priorise l'accessibilité lorsque nous construisons nos applications. La manière la plus simple de saisir le formulaire est d'utiliser `container.querySelector`.

Ensuite, nous devons assigner de nouvelles valeurs aux entrées et simuler le changement pour mettre à jour leur état. Cette étape peut sembler un peu étrange, puisque normalement nous tapons un caractère à la fois, mettant à jour l'état du composant pour chaque nouveau caractère.

Ce test se comporte plus comme le comportement de copier/coller, passant d'une chaîne vide à 'Socrates'. Pas de problèmes de rupture pour l'instant, mais nous pourrions vouloir en prendre note au cas où cela se produirait plus tard.

Après avoir soumis le formulaire, nous pouvons faire des assertions sur des choses comme quelles props ont été invoquées et avec quels arguments. Nous pourrions également utiliser ce moment pour vérifier que les entrées du formulaire ont été effacées.

Est-ce intimidant ? Pas besoin d'avoir peur, mon enfant, marche ainsi. Commencez par ajouter le formulaire à votre fonction de rendu.

Je pourrais diviser ce formulaire en son propre composant séparé, mais je vais m'abstenir pour l'instant. Au lieu de cela, je l'ajouterai à ma « Liste de souhaits de refactorisation » que je garde à côté de mon bureau.

C'est la voie du TDD. Lorsque quelque chose semble pouvoir être refactorisé, notez-le et continuez. Refactorisez uniquement lorsque la présence d'une abstraction vous bénéficie et ne semble pas inutile.

Vous vous souvenez lorsque nous avons refactorisé notre suite de tests en créant l'usine `createProps` ? Tout comme cela. Nous pouvons également refactoriser les tests.

Maintenant, ajoutons les méthodes de classe `handleChange` et `handleSubmit`. Celles-ci sont déclenchées lorsque nous changeons une entrée ou soumettons notre formulaire. Je vais également initialiser notre état.

Et c'est fait. Nos tests passent et nous avons quelque chose qui ressemble un peu à une vraie application. À quoi ressemble notre couverture ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q4coAIT2yaP120pDWGxoAQ.png)

Pas mal. Si nous ignorons toutes les configurations qui vont dans index.js, nous avons une application web entièrement couverte en termes de lignes exécutées.

Bien sûr, il y a probablement d'autres cas que nous voulons tester afin de vérifier que l'application fonctionne comme nous l'entendons. Ce nombre de couverture est juste quelque chose que votre patron peut vanter lorsqu'il parle aux autres cohortes.

### **Aimer les commentaires**

Et si nous vérifiions que nous pouvons aimer un commentaire ? Ce pourrait être un bon moment pour établir un certain concept d'authentification au sein de notre application. Mais nous n'irons pas trop loin pour l'instant. Mettons d'abord à jour notre usine de props pour ajouter un champ `auth` ainsi que des identifiants pour les commentaires que nous générons.

L'utilisateur qui est « authentifié » verra sa propriété `auth` transmise à travers l'application. Toutes les actions pertinentes quant à savoir s'ils sont authentifiés seront notées.

Dans de nombreuses applications, cette propriété peut contenir un type de jeton d'accès ou de cookie qui est envoyé lors de la réalisation de requêtes au serveur.

Sur le client, la présence de cette propriété permet à l'application de savoir qu'elle peut permettre à l'utilisateur de consulter son profil ou d'autres routes protégées.

Dans cet exemple de test, cependant, nous ne nous attarderons pas trop sur l'authentification. Imaginez un scénario comme celui-ci : lorsque vous entrez dans un salon de discussion, vous donnez votre pseudonyme. À partir de ce moment, vous êtes responsable de chaque commentaire qui utilise ce pseudonyme, malgré qui d'autre s'est connecté avec ce nom.

Bien que ce ne soit pas une solution idéale, même dans cet exemple artificiel, nous nous préoccupons uniquement de tester que le composant CommentFeed se comporte comme il se doit. Nous ne nous préoccupons pas de **comment** nos utilisateurs sont connectés.

En d'autres termes, nous pourrions avoir un composant de connexion totalement différent qui gère l'authentification d'un utilisateur particulier, le faisant ainsi passer par des cerceaux de feu et de fureur afin de dériver la propriété `auth` toute-puissante qui leur permet de semer le chaos dans notre application.

Aimons un commentaire. Ajoutez ce prochain cas de test puis mettez à jour l'usine de props pour inclure `likeComment`.

Et maintenant pour l'implémentation, nous allons commencer par mettre à jour le composant Comment pour avoir un bouton d'appréciation ainsi qu'un attribut `data-testid` afin que nous puissions le localiser.

J'ai mis l'identifiant de test directement sur le bouton afin que nous puissions immédiatement simuler un clic dessus sans avoir à imbriquer des sélecteurs de requête. J'ai également attaché un gestionnaire `onClick` au bouton afin qu'il appelle la fonction `onLike` qui lui est transmise.

Maintenant, nous ajoutons simplement cette méthode de classe à notre CommentFeed :

Vous vous demandez peut-être pourquoi nous ne transmettons pas simplement la prop `likeComment` directement au composant Comment. Pourquoi en faisons-nous une propriété de classe ?

Dans ce cas, parce que c'est assez simple, nous n'avons pas à construire cette abstraction. À l'avenir, nous pourrions décider d'ajouter d'autres gestionnaires `onClick` qui, par exemple, gèrent les événements d'analyse ou initient un abonnement aux futurs commentaires de ce post.

Pouvoir regrouper plusieurs appels de fonctions différents dans la méthode `handleLike` de ce composant conteneur a ses avantages. Nous pourrions également utiliser cette méthode pour mettre à jour l'état du composant après un « Like » réussi si nous le choisissons.

### **Ne pas aimer les commentaires**

À ce stade, nous avons des tests fonctionnels pour le rendu, la création et l'appréciation des commentaires. Bien sûr, nous n'avons pas implémenté la logique qui fait réellement cela — nous ne mettons pas à jour le magasin ou n'écrivons pas dans une base de données.

Vous avez peut-être également remarqué que la logique que nous testons est fragile et pas terribly applicable à un fil de commentaires réel. Par exemple, que se passe-t-il si nous essayons d'aimer un commentaire que nous avons déjà aimé ? Va-t-il incrémenter le compteur de likes indéfiniment, ou va-t-il le désaimer ? Puis-je aimer mes propres commentaires ?

Je vais laisser l'extension de la fonctionnalité des composants à votre imagination, mais un bon début serait d'écrire un nouveau cas de test. En voici un qui s'appuie sur l'hypothèse que nous aimerions implémenter le fait de ne pas aimer un commentaire que nous avons déjà aimé :

Remarquez que ce fil de commentaires que nous construisons me permet d'aimer mes propres commentaires. Qui fait cela ?

J'ai mis à jour le composant Comment avec une logique pour déterminer si l'utilisateur actuel a aimé le commentaire ou non.

Eh bien, j'ai un peu triché : là où nous passions `author` à la fonction `onLike` auparavant, je l'ai changé en `currentUser`, qui est la prop `auth` transmise au composant Comment.

Après tout, cela n'aurait pas de sens que l'auteur du commentaire apparaisse lorsque quelqu'un d'autre aime son commentaire.

Je me suis rendu compte de cela parce que j'écrivais vigoureusement des tests. Si je n'avais fait que coder par coïncidence, cela aurait pu m'échapper jusqu'à ce qu'un de mes collègues me rabrouent pour mon ignorance !

Mais il n'y a pas d'ignorance ici, juste des tests et le code qui suit. Assurez-vous de mettre à jour le CommentFeed afin qu'il s'attende à transmettre la propriété `auth`. Pour les gestionnaires `onClick`, nous pouvons omettre de transmettre la propriété `auth`, puisque nous pouvons la dériver de la propriété `auth` dans les méthodes `handleLike` et `handleDislike` du parent.

### **Conclusion**

Espérons que votre suite de tests ressemble à un sapin de Noël non éclairé.

Il y a tant de routes différentes que nous pouvons prendre à ce stade, cela peut devenir un peu accablant. Chaque fois que vous avez une idée pour quelque chose, notez-la simplement, soit sur papier, soit dans un nouveau bloc de test.

Par exemple, disons que vous voulez réellement implémenter `handleLike` et `handleDislike` dans une seule méthode de classe, mais vous avez d'autres priorités pour l'instant. Vous pouvez faire cela en documentant dans un cas de test comme suit :

Cela ne signifie pas que vous devez écrire un test entièrement nouveau. Vous pourriez également mettre à jour les deux cas précédents. Mais l'important est que vous pouvez utiliser votre exécuteur de tests comme une liste « À faire » plus impérative pour votre application.

#### **Liens utiles**

Il y a quelques excellents morceaux de contenu qui traitent des tests en général. En voici quelques-uns en particulier qui ont inspiré cet article ainsi que mes propres pratiques.

* « [Introducing the React Testing Library](https://blog.kentcdodds.com/introducing-the-react-testing-library-e3a274307e65) » par [Kent C. Dodds](https://www.freecodecamp.org/news/how-to-build-sturdy-react-apps-with-tdd-and-the-react-testing-library-47ad3c5c8e47/undefined). C'est une bonne idée de comprendre la philosophie derrière cette bibliothèque de tests.
* « [Software Testing Anti-patterns](http://blog.codepipes.com/testing/software-testing-antipatterns.html) » par Kostis Kapelonis. Un article extrêmement approfondi qui discute des tests unitaires et d'intégration. Ainsi que de la manière de ne pas les faire.
* « [Test Driven Development by Example](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530) » par Kent Beck. Il s'agit d'un livre physique qui discute des motifs de TDD. Il n'est pas trop long et il est écrit de manière conversationnelle, ce qui le rend facile à digérer.

J'espère que cela vous suffira pour un moment.

Curieux d'en savoir plus ou de remarques spirituelles ? Si vous avez aimé cet article, donnez-moi quelques applaudissements et suivez-moi sur [Medium](http://Medium](https://medium.com/@iwilsonq), [Github](https://github.com/iwilsonq), et [Twitter](https://twitter.com/iwilsonq) !