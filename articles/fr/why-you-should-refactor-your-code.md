---
title: Pourquoi vous devriez refactoriser votre code
subtitle: ''
author: Oleh Romanyuk
co_authors: []
series: null
date: '2020-04-03T20:00:25.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-refactor-your-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/refactor-your-react-code.png
tags:
- name: clean code
  slug: clean-code
- name: refactoring
  slug: refactoring
seo_title: Pourquoi vous devriez refactoriser votre code
seo_desc: 'Raise your hand if any of the following sounds familiar: Think about code
  formatting. Get rid of unnecessary <div>''s and <span>''s. Use functional React
  components. Try to avoid arrow function in render. And do not repeat yourself!

  Before I go straigh...'
---

Levez la main si l'une des situations suivantes vous semble familière : Pensez à la mise en forme du code. Supprimez les `<div>` et `<span>` inutiles. Utilisez des composants React fonctionnels. Essayez d'éviter les fonctions fléchées dans le rendu. Et ne vous répétez pas !

Avant de passer directement à la refactorisation, je dois vous demander de répondre à une question simple : Que signifie développer une application ? Généralement, cela signifie produire un logiciel qui répond aux exigences en implémentant certaines fonctionnalités. 

Et comment faisons-nous cela ? Nous recueillons les exigences des clients, nous les estimons et nous développons les fonctionnalités une par une, n'est-ce pas ? Presque.

## **Ne pas oublier les bugs**

Oui, des erreurs se produisent. Selon le processus de développement, la complexité du logiciel, la stack technique et de nombreux autres paramètres, le nombre de bugs peut varier. 

Une entreprise ne peut pas se permettre d'avoir des problèmes critiques en production. Pour minimiser les problèmes, vous devez accorder une attention particulière au [<ins>processus d'assurance qualité</ins>](https://keenethics.com/blog/qa-documentation). Mais la théorie de l'assurance qualité affirme qu'il est généralement impossible d'exécuter une couverture de test à 100 % de vos applications et de se préparer à tous les scénarios possibles. 

Néanmoins, pour obtenir des résultats optimaux, les équipes passent beaucoup de temps à tester le logiciel et à corriger les problèmes. C'est une partie nécessaire du processus que chaque client doit comprendre et prioriser.

## **Pensez à la dette technique**

Cependant, cette pièce a un revers. Plus le processus de développement et de test prend du temps, plus vous accumulez de dette technique. 

Alors, que signifie "dette technique" ? La dette technique fait référence à tous les problèmes liés à la qualité que vous avez dans votre code. Des problèmes qui nécessiteront de dépenser des ressources supplémentaires à l'avenir. 

Vous accumulez de la dette technique pour diverses raisons, telles que :

1. L'entreprise pousse à la sortie de nouvelles fonctionnalités plus rapidement.
2. Les tests sont insuffisants.
3. Les exigences changent rapidement.
4. Les développeurs sont inexpérimentés.

La dette technique doit être documentée. Si vous ne laissez pas de tâches à faire dans le code, vous oublierez probablement le problème. Et même si vous avez le temps de vous en occuper à l'avenir, vous ne vous souviendrez pas de le corriger.

## **Comprenez l'importance de la refactorisation**

Généralement, vous devez passer du temps à refactoriser le code existant afin de résoudre les problèmes de qualité du code et ainsi réduire la dette technique. 

Mais qu'est-ce que la refactorisation ? C'est le processus de restructuration du code existant sans changer son comportement externe. Et c'est en fait quelque chose qui peut être difficile à comprendre pour les personnes d'affaires gérant le projet.

> – Aurons-nous de nouvelles fonctionnalités ?   
>   
> – Non.   
>   
> – Corrigerons-nous au moins quelques bugs ?   
>   
> – Non plus.    
>   
> – Que recevrons-nous alors ?   
>   
> – …

Travailler avec la dette technique aide à éviter les bugs. Et pour ajouter des corrections ou des changements au projet, nous devons toujours lire l'ancien code. 

Par conséquent, la refactorisation et le maintien d'une bonne qualité de code nous aideront à garder le développement à un bon rythme. 

Parfois, une entreprise peut ne pas en avoir besoin. Par exemple, si vous travaillez sur un prototype ou une [<ins>preuve de concept</ins>](https://keenethics.com/services-proof), ou s'il y a des priorités commerciales qui ne peuvent pas être ajustées, vous pouvez vous passer de refactorisation. 

Mais dans la plupart des cas, supprimer la refactorisation n'est pas une sage décision. Vous pourriez passer un énorme amount de temps sur la refactorisation si vos développeurs sont perfectionnistes, mais cela n'a pas de sens non plus. 

Par conséquent, vous devez trouver un équilibre. Vous ne devez pas passer plus de temps à refactoriser que vous n'en économiserez à l'avenir.

## **Comment commencer à refactoriser votre code React**

### **Pensez à la mise en forme du code**

Certaines personnes ajoutent des virgules finales, et d'autres non. Certains utilisent des guillemets simples, tandis que d'autres utilisent des guillemets doubles pour une chaîne. 

Si vous travaillez en équipe, maintenir un style de code commun peut être vraiment difficile. Et l'incohérence dans le style de code peut rendre votre code désordonné et difficile à lire. 

Donc, si vous n'avez pas encore pensé à utiliser des outils de mise en forme de code, il est grand temps de le faire. L'un des outils de refactorisation React les plus populaires et faciles à utiliser est [<ins>Prettier</ins>](https://prettier.io/). Vous pouvez simplement l'ajouter au projet et il s'occupera de la mise en forme pour vous. 

Prettier a quelques paramètres de style par défaut, mais vous pouvez les changer selon vos préférences en ajoutant un fichier `.prettierrc` avec vos règles de mise en forme. 

Une bonne configuration de `.prettierrc` peut ressembler à ceci :

```js
{ "printWidth": 120,  "singleQuote": true, "trailingComma": "none" }
```

Vous pouvez également reformater automatiquement le code avant de commiter avec [<ins>pre-commit hooks</ins>](https://prettier.io/docs/en/precommit.html).

### **Supprimez les <div> et <span> inutiles**

Lorsque React 16.2 a été publié en novembre 2017, de nombreux développeurs React ont soupiré de soulagement. Auparavant, pour qu'un composant retourne une liste d'enfants, il était nécessaire d'envelopper les enfants dans un élément supplémentaire, tel que `<div>` ou `<span>`. 

Mais avec React 16.2, nous avons reçu un meilleur support pour retourner les enfants des composants. Maintenant, les développeurs peuvent utiliser ce que l'on appelle des fragments. Ils ressemblent à des balises JSX vides (`<> … </>`). Avec l'aide des fragments, vous pouvez passer une liste d'enfants au composant sans ajouter de nœuds supplémentaires au DOM.

### **Pensez aux noms**

Ne soyez pas paresseux lorsque vous pensez à des noms pour les composants et les variables. Chaque nom doit être auto-explicatif.

Avez-vous déjà vu des extraits de code comme ceci ?

```js
const modifyData = data.map(x => [x.a, x.b]))
```

Que fait-il ? Si vous ne pouvez pas comprendre le but d'une variable à partir de son nom, il est temps de la renommer ! 

Cela vous aidera, vous et votre équipe, à comprendre la logique plus facilement. Cela éliminera également le temps passé à apporter des modifications aux composants existants à l'avenir.

### **Ne vous répétez pas**

Le principe DRY a été formulé pour la première fois dans le livre _The Pragmatic Programmer_. Il stipule que "chaque morceau de connaissance doit avoir une représentation unique, non ambiguë et autoritaire au sein d'un système". En d'autres termes, vous devez mettre les blocs de code répétitifs dans des composants réutilisables séparés. 

Rendre votre code DRY a de nombreux avantages. Cela peut vous faire économiser beaucoup de temps. Si vous devez changer ce code à l'avenir, vous ne le ferez qu'à un seul endroit. De plus, vous n'aurez jamais à vous soucier d'avoir oublié de faire des changements à certains endroits. De plus, vous garderez les composants plus propres et augmenterez la lisibilité du code. 

Pour garder vos composants DRY et petits, vous pouvez suivre deux règles simples :

1. Si vous utilisez un bloc de code plus de deux fois, il est temps de l'extraire.
2. Si vous dépassez un nombre prédéterminé de lignes dans un composant (par exemple, 100 lignes), il y a probablement une logique qui peut être extraite. Divisez-le en composants plus petits par fonctionnalité.

### **Utilisez des composants fonctionnels plutôt que des composants de classe**

Avec l'introduction des Hooks dans React 16.8, nous avons obtenu l'accès aux fonctionnalités des composants de classe React dans les composants fonctionnels. Les Hooks résolvent un ensemble de problèmes fréquemment rencontrés par les développeurs au cours des dernières années. 

Par exemple, le hook `useEffect`, comme le suggèrent les docs React, nous permet de regrouper la logique du composant en petites fonctions basées sur les morceaux qui sont liés (au lieu de regrouper la logique basée sur les méthodes de cycle de vie). Cela nous aide à mieux restructurer notre logique. 

En fin de compte, la refactorisation des composants React à l'aide des hooks rend le code plus propre et réduit la quantité de code que vous devez écrire. 

Voici un exemple très basique : récupérer les données après que le composant a été monté et les récupérer à nouveau en fonction des props mises à jour. 

Dans un composant de classe, nous écririons quelque chose comme ceci :

```js
class BookList extends React.Component {
  componentDidMount() {
    this.props.fetchBooks(this.props.bookGenre);
  }
  componentDidUpdate(prevProps) {
    if (prevProps.bookGenre !== this.props.booksGenre) {
      this.props.fetchBooks(this.props.bookGenre);
    }
  } 
// ... }
```

Avec les hooks React, cela ressemblera à ceci :

```js
const BookList = ({ bookGenre, fetchBooks }) => {
  useEffect(() => {
    fetchBooks(bookGenre);
  }, [bookGenre]);
// ... }
```

La logique de récupération des livres est maintenant rassemblée en un seul endroit. Le hook `useEffect` s'exécutera après le montage chaque fois que les props `[bookGenre]` entre crochets changent. Beaucoup plus propre, n'est-ce pas ? 

De plus, vous pouvez extraire une logique similaire avec état et la réutiliser dans différents composants en créant vos propres hooks. Vous pouvez en savoir plus sur les hooks personnalisés dans la documentation officielle <ins>[React](https://reactjs.org/docs/hooks-custom.html)</ins>.

### **Essayez d'éviter les fonctions fléchées dans le rendu**

Avez-vous déjà vu du code comme ceci ?

```js
render() {    
  return (
    <div>
      <button onClick={() => this.setState({ flag: true })} />
      ...      
    </div>    
  );  
}
```

Bien sûr que oui. Quel est le problème avec cela ? Chaque fois qu'un composant est rendu, une nouvelle instance d'une telle fonction est créée. 

Ce n'est pas un gros problème si le composant est rendu une ou deux fois. Mais dans d'autres cas, cela peut vraiment affecter les performances. Donc, si vous vous souciez des performances, déclarez la fonction avant de l'utiliser dans le rendu :

```js
changeFlag = () => this.setState({ flag: true })
render() {    
  return (      
    <div> 
      <button onClick={this.changeFlag} />        
      ...      
    </div>    
  );  
}
```

### **Rendez le bundle plus petit**

Si vous utilisez une bibliothèque tierce, vous ne devez pas charger toute la bibliothèque si ce n'est pas nécessaire. Parfois, vous pouvez tomber sur une importation qui utilise uniquement une méthode de la bibliothèque, comme :

```js
import lodash form 'lodash'  
...  
const certainProps = lodash.pick(userObject, ['name', 'email']);  ...
```

Au lieu de cela, il est préférable d'utiliser ce qui suit :

```js
import pick from 'lodash/pick' 
... 
const certainProps = pick(userObject, ['name', 'email']); ...
```

Maintenant, vous ne chargez pas toute la bibliothèque, juste la méthode dont vous avez besoin.

## **Pour conclure**

Passons en revue les étapes que vous devez suivre pour refactoriser votre code React :

* Pensez à la mise en forme du code
* Supprimez les `<div>` et `<span>` inutiles
* Pensez aux noms
* Ne vous répétez pas
* Utilisez des composants fonctionnels plutôt que des composants de classe
* Essayez d'éviter les fonctions fléchées dans le rendu
* Rendez le bundle plus petit

Cependant, la refactorisation idéale est celle qui ne se produit pas. En tant que développeur et surtout en tant que responsable technique, vous devez penser à plusieurs étapes à l'avance et essayer de produire un code de haute qualité. Vous devez également effectuer des revues de code régulières, non seulement au sein d'une équipe, mais aussi entre les équipes.

## Avez-vous une idée pour un projet React ?

Mon entreprise KeenEthics est une entreprise expérimentée en développement React [development company](https://keenethics.com/services-web-development). Si vous êtes prêt à changer la donne avec votre projet logiciel, n'hésitez pas à [demander une estimation](https://keenethics.com/services-web-development).

Vous pouvez lire d'autres articles similaires sur mon blog Keen. Permettez-moi de vous suggérer [The Value of User Testing](https://keenethics.com/blog/the-value-of-user-testing) ou [Angular vs React: What to Choose for Your App?](https://keenethics.com/blog/angular-vs-react-what-to-choose-for-your-app)

Surtout, je voudrais dire "merci" à Yaryna Korduba et Max Fedas, deux développeurs React exceptionnels, pour avoir coécrit cet article ainsi qu'aux lecteurs pour l'avoir lu jusqu'à la fin !