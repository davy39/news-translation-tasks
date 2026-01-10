---
title: Comment j'ai construit une bibliothèque de validation de formulaire asynchrone
  en ~100 lignes de code avec React Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T17:40:04.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-an-async-form-validation-library-in-100-lines-of-code-with-react-hooks-81dbff6c4a04
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EGRMyNT8x7gb0LdLmj4xMQ.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment j'ai construit une bibliothèque de validation de formulaire asynchrone
  en ~100 lignes de code avec React Hooks
seo_desc: 'By Austin Malerba

  Form validation can be a tricky thing. There are a surprising number of edge cases
  as you get into the guts of a form implementation. Thankfully, there are many form
  validation libraries out there which provide the necessary flags a...'
---

Par Austin Malerba

La validation de formulaire peut être une chose délicate. Il y a un nombre surprenant de cas particuliers lorsque l'on entre dans les détails d'une implémentation de formulaire. Heureusement, il existe de nombreuses bibliothèques de validation de formulaire qui fournissent les indicateurs et gestionnaires nécessaires pour implémenter un formulaire robuste, mais je me suis lancé le défi d'en construire une en moins de 100 lignes de code en utilisant l'[API React Hooks](https://reactjs.org/docs/hooks-reference.html) (actuellement en alpha). Comme les React Hooks sont encore une proposition expérimentale, ceci est une preuve de concept pour l'application des React Hooks à l'implémentation de la validation de formulaire.

Aussi, attention, la _bibliothèque_ que je construis fait 100 lignes de code, mais ce tutoriel a ~200 lignes de code car je dois montrer comment la bibliothèque est utilisée.

De nombreux tutoriels sur les formulaires que j'ai vus ne traitent pas trois grands sujets : la **validation asynchrone**, les validations de champs qui doivent être déclenchées lorsque **d'autres champs changent**, et l'optimisation de la **fréquence de validation**. Je suis gêné par les tutoriels qui se concentrent sur un seul cas d'utilisation et maintiennent toutes les autres variables constantes car ce n'est pas ainsi que fonctionne le monde réel, donc je vais essayer de couvrir une variété de cas d'utilisation.

Efforçons-nous de satisfaire les points suivants :

* Valider de manière synchrone un champ et tous les champs dépendants lorsque la valeur du champ change
* Valider de manière asynchrone un champ et tous les champs dépendants lorsque la valeur du champ change
* Valider de manière synchrone tous les champs avant la soumission
* Valider de manière asynchrone tous les champs avant la soumission
* Tentative de soumission asynchrone et si le formulaire échoue à se soumettre, afficher les erreurs de la réponse
* Exposer les méthodes de validation au développeur afin que le développeur puisse valider onBlur ou à d'autres moments qui ont du sens
* Permettre plusieurs validations par champ
* Désactiver la soumission si le formulaire contient des erreurs
* Ne pas afficher les erreurs d'un champ tant qu'il n'a pas été modifié ou tant qu'une soumission de formulaire n'a pas été tentée

Nous allons couvrir ces cas d'utilisation en implémentant un formulaire d'inscription de compte avec un nom d'utilisateur, un mot de passe et une confirmation de mot de passe. Ci-dessous, j'ai décrit le type d'interface que nous recherchons, nous allons construire une bibliothèque pour satisfaire ce contrat.

Il s'agit d'une API relativement simple, mais qui devrait nous donner beaucoup de flexibilité. Vous avez peut-être remarqué que cette interface inclut deux fonctions de noms similaires, validation et validate. Nous allons définir une validation comme une fonction qui prend les données du formulaire et un nom de champ et retourne un message d'erreur si un problème est trouvé, sinon elle retournera une valeur fausse. D'autre part, une fonction validate exécutera toutes les fonctions de validation pour un champ et mettra à jour la liste des erreurs du champ.

Premièrement, nous avons besoin d'un squelette pour gérer les changements de valeur et la soumission du formulaire. Notre première itération n'inclura aucune validation, elle gérera simplement l'état du formulaire.

Il ne se passe rien de trop fou dans ce code. Le seul état que nous suivons est les valeurs des champs. Nous faisons en sorte que chaque champ s'enregistre lui-même avec le formulaire à la fin de son initialisation. Nos gestionnaires onChange sont simples. La fonction la plus intimidante ici est getFormData, mais même celle-ci est assez triviale derrière la syntaxe peu attrayante de reduce. getFormData itère sur les champs du formulaire et nous donne une représentation en objet simple des valeurs du formulaire. La dernière chose que je pense devoir expliquer est que nous devons appeler preventDefault sur submit pour empêcher la page de se recharger.

C'est bien et joli, mais ajoutons maintenant la prise en charge des validations. Nous ne spécifierons pas encore quels champs doivent être validés lorsque la valeur d'un champ change. Au lieu de cela, nous validerons tous les champs chaque fois qu'une valeur change et chaque fois que le formulaire est soumis.

Le code ci-dessus est une amélioration et, à première vue, il semble pouvoir bien fonctionner, mais il est en réalité assez [peu soigné pour l'utilisateur final](https://codesandbox.io/s/wy074qmk98?module=%2Fsrc%2FformHooks.js). Il manque beaucoup d'indicateurs nécessaires qui aident à prévenir l'affichage d'erreurs à des moments inappropriés. Il valide immédiatement les champs avant que l'utilisateur n'ait eu la chance de les modifier et affiche les erreurs correspondantes.

Au minimum, nous avons besoin d'un indicateur pristine pour dire à l'UI de ne pas afficher les erreurs si l'utilisateur n'a pas changé un champ. Mais allons plus loin. En plus d'un indicateur pristine, nous voudrons quelques indicateurs supplémentaires.

Nous voudrons un indicateur pour indiquer que l'utilisateur a tenté de soumettre le formulaire et nous voudrons des indicateurs pour indiquer lorsque le formulaire est en cours de soumission et lorsque chaque champ est en cours de validation de manière asynchrone. Vous vous demandez peut-être aussi pourquoi nous invoquons validateFields à l'intérieur de useEffect plutôt qu'à l'intérieur du gestionnaire onChange. Nous avons besoin de useEffect car setValue se produit de manière asynchrone et ne retourne pas de promesse ni n'offre de rappel. Par conséquent, la seule façon dont nous pouvons être sûrs que setValue est terminé est en écoutant un changement de valeur via useEffect.

Implémentons les indicateurs que j'ai mentionnés pour aider à nettoyer l'UI et à gérer certains cas particuliers.

Notre dernière itération ajoute beaucoup de choses. Elle ajoute quatre indicateurs : pristine, validating, submitted et submitting. Elle ajoute également le paramètre fieldsToValidateOnChange, qui est passé à validateFields pour indiquer quels champs doivent être validés lorsque la valeur d'un champ change. Nous utilisons ces indicateurs dans l'UI pour contrôler quand les spinners et les erreurs sont affichés ainsi que pour désactiver le bouton de soumission.

Une chose particulière que vous avez peut-être remarqué est le validateCounter. Nous devons suivre le nombre de fois que la fonction validate a été appelée car au moment où notre fonction validate a atteint son achèvement, il est possible que validate ait été appelée à nouveau. Si c'est le cas, nous devons ignorer les résultats de cette invocation et n'utiliser que les résultats de l'invocation la plus récente pour mettre à jour l'état d'erreur d'un champ.

Lorsque tout est dit et fait, voici le résultat fonctionnel.

Les React Hooks fournissent une solution élégante à la validation de formulaire. C'est ma première expérimentation avec l'API proposée et je l'ai trouvée puissante, mais un peu maladroite. L'interface est particulière, avec un peu trop de magie à mon goût. Cependant, une fois que j'ai accepté ses défauts, elle s'est avérée assez capable.

J'ai senti qu'il lui manquait quelques fonctionnalités, notamment un mécanisme de rappel pour indiquer lorsqu'un setter useState a terminé la mise à jour de l'état et également un moyen d'inspecter les deltas de props dans le hook useEffect.

#### Note finale

J'ai intentionnellement omis certaines validations d'arguments et gestion d'erreurs afin de garder ce tutoriel bref et simple à suivre. Prenez, par exemple, la façon dont je ne vérifie pas si le formulaire passé à un champ est effectivement un formulaire. Il serait beaucoup plus agréable de vérifier cela explicitement et de lancer une erreur verbeuse. Cependant, tel que je l'ai écrit, le code planterait avec quelque chose comme

```
Cannot read property 'addField' of undefined
```

Ce code a besoin d'une validation d'argument et d'une gestion d'erreur appropriées avant de pouvoir être publié en tant que bibliothèque npm. Cela dit, j'ai implémenté une [version plus robuste](https://codesandbox.io/s/1417995kx4) qui inclut la validation d'argument via [superstruct](https://github.com/ianstormtaylor/superstruct) si vous souhaitez la vérifier.