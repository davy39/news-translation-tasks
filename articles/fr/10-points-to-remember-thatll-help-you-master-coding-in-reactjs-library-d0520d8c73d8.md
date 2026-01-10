---
title: Comment écrire du code React hautement lisible — 10 conseils de style de codage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-03T16:00:49.000Z'
originalURL: https://freecodecamp.org/news/10-points-to-remember-thatll-help-you-master-coding-in-reactjs-library-d0520d8c73d8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NlqpTTAM8DbGl4paBmjE_g.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment écrire du code React hautement lisible — 10 conseils de style de
  codage
seo_desc: 'By Nirmalya Ghosh

  When doing code reviews, developers rarely get enough time to truly understand each
  line of code we’re reviewing. Instead, we have to quickly ponder the different situations
  where that code might fail.

  So every time I review code, I...'
---

Par Nirmalya Ghosh

Lors des revues de code, les développeurs ont rarement assez de temps pour vraiment comprendre chaque ligne de code que nous examinons. Au lieu de cela, nous devons rapidement réfléchir aux différentes situations où ce code pourrait échouer.

Donc, chaque fois que je révise du code, je cherche certains points pour m'aider à comprendre rapidement le code.

Cet article vous aidera à comprendre comment vous pouvez écrire un meilleur code, afin que d'autres développeurs puissent mieux le comprendre. Cet article vous donnera une brève introduction à certaines techniques que j'utilise lors de la conception de mes composants, et vous montrera comment vous pouvez faire de même.

Notez que nous nous en tiendrons principalement à ReactJS ici, mais que certains de ces points peuvent également s'appliquer à l'utilisation d'autres bibliothèques JavaScript.

### Conseil #1 : Utilisez toujours prop-types pour définir toutes les props dans vos composants

[prop-types](https://github.com/facebook/prop-types) est une vérification de type à l'exécution pour les props React et les objets similaires.

prop-types vous aidera à vérifier si le type de prop souhaité est passé à votre composant ou non.

Si le type approprié d'une prop spécifique n'est pas passé à votre composant, alors le package lancera un avertissement dans la console de votre navigateur.

Dans le pen ci-dessus, vous pouvez vérifier la console et elle lancera l'avertissement suivant :

```
"Warning: Failed prop type: Invalid prop `message` of type `string` supplied to `Hello`, expected `array`.    in Hello"
```

D'après le message d'avertissement ci-dessus, il est assez clair que nous passons une chaîne au composant Hello, mais que le composant attend que la prop message soit de type array.

### Conseil #2 : Utilisez displayName pour définir un nom particulier à votre composant

La chaîne [displayName](https://reactjs.org/docs/react-component.html#displayname) est utilisée dans les messages de débogage.

Si vous n'utilisez pas displayName dans vos composants, vous devriez l'utiliser à partir de maintenant.

Normalement, si vous déboguez votre composant à l'aide des [React developer tools](https://github.com/facebook/react-devtools), vous verrez les composants car il est déduit du nom de la fonction ou de la classe qui définit le composant.

Cependant, si vous avez une situation où vous avez deux composants avec le même nom (bouton, dropdown, etc.), alors vous devrez peut-être renommer vos composants. Sinon, vous ne pourrez pas les distinguer.

Vous pouvez résoudre le problème ci-dessus en utilisant displayName.

Vous renommez simplement l'un des composants en utilisant displayName.

Dans l'exemple ci-dessus, vous pouvez voir que même si le nom de la classe est Component, vous verrez le nom « Hello » dans l'outil de développement React car il a Hello comme displayName.

Cela est très utile pour le débogage et est souvent négligé.

### Conseil #3 : Utilisez un linter pour rendre votre code plus facile à réviser

Si vous vous souciez de votre santé mentale, alors vous devriez utiliser un linter sur votre base de code.

Les linters vous aideront à rendre votre code similaire à celui des autres développeurs de votre entreprise. En suivant un ensemble strict de règles, vous pouvez être certain que toute la base de code sera cohérente.

Par exemple, vous pouvez forcer les autres développeurs à utiliser des points-virgules à la fin d'une ligne. S'ils ne le font pas, alors le linter lancera une erreur ou un avertissement en fonction de vos paramètres.

Le linter que je suis principalement est [ESLint](https://eslint.org/) mais vous pouvez en choisir un autre qui convient à vos besoins.

### Conseil #4 : Révisez votre propre code avant de créer une pull request

Que vous corrigiez un bug ou développiez une nouvelle fonctionnalité, il est probable que vous poussiez vos changements et créiez une pull request rapidement lorsque vous êtes pressé.

Le problème avec cela est que vous n'avez même pas le temps de réviser vos propres changements. En conséquence, vous pourriez manquer certains endroits que vous pourriez refactoriser et améliorer.

D'après mon expérience, après avoir révisé mes propres changements, parfois, je pouvais les rendre plus performants, diviser les fonctions plus grandes en plusieurs fonctions plus petites et rendre le code plus modulaire.

Auparavant, je ne révisais jamais mon propre code. Mais en pratiquant cette habitude, je sens que cela améliore mon codage et cela pourrait vous aider aussi.

### Conseil #5 : Votre premier brouillon n'est pas toujours le meilleur

Beaucoup d'entre vous le savent déjà. La première itération n'est pas toujours la meilleure.

Vous devriez regarder votre première itération de codage et penser aux fonctionnalités que vous auriez pu manquer.

Une façon de corriger cela pourrait être de faire un développement piloté par les tests (TDD), qui est une excellente pratique mais rarement suivie. Si vous suivez une approche TDD, votre première itération peut être la meilleure. Mais vous devriez chercher une meilleure approche.

Prenez votre temps pour réfléchir à la manière dont vous souhaitez procéder avant même d'écrire une seule ligne de code et lorsque vous avez terminé d'implémenter une fonctionnalité ou de corriger un bug, regardez vos changements et pensez à la manière dont vous pouvez les améliorer.

### Conseil #6 : Divisez votre code en plusieurs fonctions plus petites

Diviser vos fonctions plus grandes en plusieurs fonctions plus petites rendra les fonctions plus petites plus réutilisables. Elles deviendront également beaucoup plus faciles à tester.

Vous pouvez également créer de nombreux fichiers utilitaires qui peuvent vous aider à supprimer le code dupliqué de plusieurs fichiers.

Après avoir créé plusieurs fichiers, regardez-les et vous verrez qu'il y a de nombreuses lignes de code dupliquées. Vous pouvez prendre ces lignes et créer un fichier utilitaire. Vous pouvez ensuite réutiliser le même fichier utilitaire dans plusieurs fichiers.

### Conseil #7 : Créez plusieurs fichiers au lieu d'écrire un gros fichier

Réviser un gros fichier est toujours plus difficile que de réviser plusieurs petits fichiers.

Si vous divisez votre code en plusieurs petits fichiers et que chaque fichier ne contient qu'une seule logique, alors il devient très facile pour le réviseur de réviser ce fichier.

### Conseil #8 : Soyez très prudent lors du nommage de vos fichiers

Une autre chose à retenir ici est que si vous nommez vos fichiers en fonction du travail qu'ils effectuent, cela vous aidera également à l'avenir ainsi que les autres développeurs à comprendre ce que le fichier fait réellement.

Après avoir regardé le nom du fichier, les autres développeurs devraient comprendre ce que le fichier est censé faire.

Par exemple, dropdown.js est un bon nom mais il est très générique et si vous l'utilisez à plusieurs endroits dans le même répertoire, vous pourriez le nommer comme topDropdown.js, bottomDropdown.js, ce qui est mauvais.

Une meilleure façon sera de les préfixer avec le travail qu'ils sont censés effectuer. Par exemple, userDropdown.js, fileDropdown.js, etc.

### Conseil #9 : Écrivez toujours des tests pour votre code

Je ne peux pas assez insister sur l'importance de ce point. Les tests complètent votre code.

Après avoir développé une fonctionnalité, vous pourriez penser qu'elle fonctionne et qu'elle fonctionne effectivement. Mais il peut y avoir (et il y aura probablement) des cas limites où elle pourrait ne pas fonctionner. Les tests vous aideront à identifier ces cas.

Il est évident que l'écriture de cas de test augmentera le temps dont vous avez besoin pour écrire votre code. Mais cela vous aidera toujours à éliminer les bugs potentiels qui pourraient surgir à l'avenir.

Vous devriez prendre le temps d'écrire des tests si vous vous souciez de votre application.

### Conseil #10 : Ne surutilisez pas le hook de cycle de vie de gestion des erreurs

React 16 a introduit une meilleure façon de [gérer les erreurs](https://reactjs.org/blog/2017/07/26/error-handling-in-react-16.html) en utilisant une fonctionnalité appelée Error Boundaries.

Essentiellement, les error boundaries sont des composants React qui attrapent les erreurs JavaScript n'importe où dans leur arbre de composants enfants, enregistrent ces erreurs et affichent une UI de repli au lieu de l'arbre de composants qui a planté.

Si la logique pour l'UI de repli est présente dans votre composant ErrorBoundary, alors vous pouvez encapsuler votre composant à l'intérieur de ce composant ErrorBoundary.

```
<ErrorBoundary>  <YourComponent /></ErrorBoundary>
```

C'est une belle façon dont vous pouvez montrer une UI de repli pour vos erreurs. Mais vous n'avez pas besoin d'envelopper tous vos composants avec un composant ErrorBoundary.

Vous pouvez placer votre composant ErrorBoundary [uniquement dans quelques endroits stratégiques](https://reactjs.org/blog/2017/07/26/error-handling-in-react-16.html#where-to-place-error-boundaries) où vous en avez besoin.

### Conclusion

J'espère que ces points vous aideront à écrire un meilleur code ReactJS et un meilleur code JavaScript en général. Faites-moi savoir si vous utilisez d'autres approches que j'ai manquées ici.