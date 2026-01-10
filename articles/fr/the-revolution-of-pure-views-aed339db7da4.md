---
title: La programmation fonctionnelle prend le contrôle des interfaces utilisateur
  avec des vues pures.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-12-29T18:05:47.000Z'
originalURL: https://freecodecamp.org/news/the-revolution-of-pure-views-aed339db7da4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iqyzwSonyQR8eBQRduP3cg.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: La programmation fonctionnelle prend le contrôle des interfaces utilisateur
  avec des vues pures.
seo_desc: 'By Bobby Schultz

  The last couple years have seen a huge improvement in how UIs are developed by using
  Purely Functional Views. In functional programming a “pure function” is one that
  when run, returns a value but does not change anything outside its ...'
---

Par Bobby Schultz

Les dernières années ont vu une énorme amélioration dans la façon dont les interfaces utilisateur sont développées en utilisant des vues purement fonctionnelles. En programmation fonctionnelle, une « fonction pure » est une fonction qui, lorsqu'elle est exécutée, retourne une valeur mais ne modifie rien en dehors de sa portée (également connue sous le nom de fonction sans effet de bord). Cela réduit considérablement la charge cognitive et les permutations dans les applications, de sorte qu'elles ont une réduction massive des bugs ([voir l'étude de cas](https://medium.com/@puppybits/react-without-flux-a76236d1e1d)), sont faciles à comprendre, à composer ensemble et incroyablement stables.

David Nolen a l'une des meilleures explications pour ce type de modèle de développement d'interface utilisateur **Œ(d)=V**. C'est une fonction qui reçoit des données en entrée et retourne une vue. Pas de portée, de liaison, de sous-classement, d'accès externe aux variables ou d'effets de bord. Cela la rend très prévisible avec beaucoup moins de considération pour le contexte dans lequel une vue pure est exécutée. Dans le monde JavaScript, on pourrait dire : étant donné n'importe quel JSON, cela créera TOUJOURS le même HTML, CSS et les mêmes écouteurs d'événements.

#### Pourquoi les vues pures sont-elles différentes des autres modèles d'interface utilisateur ?

Pour bien comprendre cela, nous devons comprendre ce que nous avons implicitement fait pendant des années dans notre code. Le code est écrit comme une série de permutations complexes. Chaque fonction que nous appelons modifie quelque chose en dehors de sa portée privée. Nous appelons ensuite une autre fonction qui modifie autre chose. Si les données ou l'ordre de ces appels de fonctions dévie de quelque manière que ce soit, des bugs se produisent de manière inattendue. Pensez aux fois où vous avez corrigé un bug qui était causé par quelque chose de apparemment sans rapport dans une autre classe ou sur un serveur quelque part. Ce sont de grands problèmes de permutation.

Jetez un coup d'œil au graphique ci-dessous. C'est ainsi que nous pensons intérieurement à nos applications.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_HGWb7cZuJs72uPFT19PzA.png)
_Comment nous « pensons » que notre application fonctionne._

Super clair, n'est-ce pas ? Appelez `login()`, puis `getUser()`, puis `getCart()`. En réalité, le flux de notre application inclut des chemins d'erreur, des valeurs inattendues, des opérations réseau et de thread. S'ils reviennent dans un ordre légèrement différent ou si les données sont légèrement différentes ou si les données sont mutées par plusieurs classes dans nos applications, cela provoquera des bugs. Voici un modèle plus précis des branches possibles :

![Image](https://cdn-media-1.freecodecamp.org/images/1*LaWtFnAP8QAMu7mYFzE2-g.png)
_Comment nos applications fonctionnent vraiment._

Si quelque chose ne suit pas un chemin attendu au moment attendu, nous obtenons des bugs. Les classes OOP sont censées encapsuler les données, les événements et les transformations à l'intérieur de leurs limites pour faire fonctionner cela sans bugs. Évidemment, nous avons tous des bugs. Les systèmes sont difficiles parce qu'ils sont complexes et ces complexités causent des bugs.

#### Simple Made Easy

Pour quiconque a appris les Gang of Four et les modèles orientés objet mais n'a pas vu la conférence de Rich Hickey « Simple Made Easy » [allez la regarder maintenant](https://www.infoq.com/presentations/Simple-Made-Easy). Le concept central dont parle Hickey est comment trop d'externalités est une raison majeure pour laquelle nous ne comprenons pas pleinement ce que notre code fait lorsque nous le lisons. Ce n'est pas facile parce que trop de plaques tournent en même temps. Les langages orientés objet ont des modèles qui tentent de réduire cette complexité en étant fortement axés sur l'utilisation de l'encapsulation. Les langages fonctionnels, à l'inverse, sont fortement axés sur la composabilité comme caractéristique clé pour réduire la complexité. Un meilleur mélange des deux est nécessaire pour obtenir un meilleur contrôle sur nos interfaces utilisateur.

Les vues pures apportent certains des avantages des langages fonctionnels au monde OO dans lequel vivent la plupart des développeurs. Dans les langages fonctionnels, une fonction pure ne fait qu'une seule chose et n'a pas d'effets de bord (effet de bord signifiant qu'elle ne peut pas affecter quoi que ce soit, seulement retourner une nouvelle valeur). Plusieurs fonctions simples peuvent être composées de différentes manières pour produire de nombreux types de sorties. Pour paraphraser Rich Hickey ; Simple signifie faire une seule chose. Facile signifie quelque chose que nous sommes capables de comprendre l'étendue. Dans le cas des vues pures, en regardant la fonction de rendu, nous devrions être capables de comprendre toutes les sorties potentielles. Cela réduit le besoin de comprendre l'ensemble de la base de code pour savoir comment elle peut affecter une seule fonction.

Voici comment fonctionnerait un processus de vue pure fonctionnel :

![Image](https://cdn-media-1.freecodecamp.org/images/1*bf7BFe_mAaJaYNoxUTnEmw.png)
_Les vues pures sont des transformations simples sans effets de bord._

C'est un concept incroyablement puissant. Au lieu de devoir propager à travers les fonctions, les événements et les piles réseau et les mutations partout, il suffit de prendre un instantané des données et de les rendre dans une vue. La vue aura toute la mise en page, les gestionnaires d'événements et les points d'accès pour que l'utilisateur interagisse avec les données sous-jacentes. Cela signifie que pour atteindre n'importe quel emplacement dans l'application, la seule dépendance est un modèle de données statique. Généralement, ces vues pures sont couplées avec des méthodes de cycle de vie pour mieux comprendre quand, pourquoi et comment les données changent. Par exemple, voici un exemple de code réel d'une vue pure :

```
createView({  getDefaultProps(){    return {      selectedIds: [1, 10],      banks: [/* données de banque ici */]    };  }   render(){     let selectedBanks = this.props.banks.filter(function(bank){      return this.props.selectedIds.indexOf(bank.id) > -1;    });    let bankItems = [];    for (let i=0; i < selectedBanks.length; i++){      bankItems.push(        el("BankItem", {key:i, bank:selectedBanks[i]})      );    }    return el("div", null,             el("h1", null, "Banques sélectionnées"),             bankItems,             el("a", {href:"/installation", "Suivant"})           );  }})
```

Cette vue encapsule les propriétés qui lui sont passées par son parent. Lorsque la fonction de rendu est appelée, elle ne nécessite rien en dehors de la portée de la vue elle-même. Tout ce qui peut affecter la sortie est dans une seule fonction. Jusqu'à ce que la fonction de rendu soit terminée, les props et l'état ne peuvent pas être modifiés non plus. Cela facilite le raisonnement sur ce qui se passera à chaque exécution. Chaque fois que le parent lui envoie de nouvelles données, cela déclenchera la fonction de rendu pour s'exécuter à nouveau.

#### Étendre les capacités sans ajouter de complexité

Parce que les vues pures ne font qu'une seule chose et n'affectent rien en dehors de leur propre portée, cela les rend extrêmement flexibles sans introduire de complexités supplémentaires. Il y a quelques cas qui montrent vraiment la puissance des vues pures.

Le premier s'appelle **Hot Module Replacement**. Si vous pensez que cela ressemble à Live Reloading dans le navigateur, vous vous trompez. Dès que vous enregistrez un fichier dans votre éditeur, seul le code mis à jour peut être envoyé à votre application, remplace l'ancien code, la fonction de rendu pour cette vue est exécutée et seul le HTML qui diffère est modifié. La couche de données entière de l'application n'est pas affectée. Cela fonctionne avec les mises en page, les hiérarchies de vues et les gestionnaires d'événements. Les données dans l'application ne changent pas, donc votre vue est mise à jour en temps réel. Il existe des bibliothèques pour supporter cela dans les navigateurs, iOS, Android, Windows et les applications Mac. Lorsque le temps d'itération entre la réalisation d'un changement dans le code et la visualisation de la sortie est proche de 0, cela change complètement votre flux de travail de codage.

Le suivant est **Time Travel Debugging**. C'est vraiment incroyable comme cela en a l'air. Sans les vues pures, stocker chaque propagation d'événement et ses effets sur la vue est une charge impossible pour la plupart des systèmes. Avec les vues pures, tout ce dont vous avez besoin est un tableau et pousser une nouvelle copie des données chaque fois qu'elles sont modifiées. Si vous comprenez comment fonctionnent les structures de données persistantes, c'est encore moins de travail pour sauvegarder chaque changement dans votre application. Lors du débogage, il suffit de faire défiler en avant et en arrière comme avec un magnétoscope. (Oui, la technologie UI des années 80 et la plupart des frameworks UI ne l'ont pas dans leur boîte à outils de débogage aujourd'hui). L'état de l'application peut même être sérialisé et sauvegardé sur le serveur en production pour obtenir des étapes de reproduction complètes de presque tous les bugs dans votre application.

La dernière capacité majeure est **Résilience plutôt que rigidité**. Les données ne sont pas liées à l'interface utilisateur. C'est une séparation claire des préoccupations. La couche de données de votre application peut se concentrer en termes de fonctions, de transformations de données et de mise en cache sans avoir à penser à toutes les préoccupations qu'un utilisateur pourrait avoir. Dans la grande majorité des projets, la logique métier change à peine ; le code pour un panier d'achat en ligne a à peu près les mêmes exigences. Mais au niveau de la vue, les designers trouvent toujours de nouvelles façons d'expliquer ou de clarifier l'interface ou d'augmenter les ventes. Les tests unitaires et d'intégration peuvent se concentrer sur le test du flux d'application en données pures et simples. Puisque la vue n'est qu'une simple transformation et un reflet des données à un état donné, elle est beaucoup moins susceptible d'avoir des complexités ou des bugs. Cela signifie également que lorsque le designer ou le directeur commercial demande des changements à la vue, cela peut être fait sans affecter la fonctionnalité du flux de données.

#### Retour au monde réel

Le mouvement des vues pures est en croissance. Il y a peu, voire aucun avantage que les couches de vue traditionnelles ont sur les vues pures. Les frameworks plus ouverts comme Backbone permettent d'échanger des systèmes de templating de chaînes de caractères contre des vues pures. De plus en plus d'auteurs de frameworks voient les avantages et passent aux vues pures. Quelques frameworks notables qui défendent vraiment cette approche sont Elm, Ember 2, Om Next, ReactJS.

Pour tirer parti de certaines des capacités étendues offertes par les vues pures, il existe des outils prêts à l'emploi qui facilitent l'intégration. Pour le Hot Module Replacement, Webpack et React ont une excellente configuration. Je maintiens un kit de démarrage appelé [Megatome](https://bit.ly/megatome) qui devrait vous permettre de démarrer un nouveau projet en 2 minutes. Pour le Time Travel Debugging, [regardez Redux](https://github.com/rackt/redux), qui est une couche de données conçue pour fonctionner avec React.

Une dernière note pour tous ceux qui se retrouvent à scruter la syntaxe (comme Lisps ou JSX) : ne jugez pas un livre à sa couverture. Si vous ne regardez pas plus profondément, vous pouvez complètement ignorer les possibilités et la puissance qui peuvent venir de quelque chose de différent. Regardez à nouveau le code ci-dessus pour une vue pure réelle. C'est tout du code valide sans besoin de transpilation, de gestionnaires de paquets ou d'étapes de construction supplémentaires. La seule chose qui manque est les trois premières lignes :

```
let el = React.createElement;let createView = React.createClass;
```

_Mon dernier projet est plus difficile que le codage. Nous faisons en sorte que la finance personnelle ne soit pas une corvée. Voyez comment votre rythme de dépenses mène à la maîtrise de votre budget sur [getfiskal.com](https://www.getfiskal.com)._