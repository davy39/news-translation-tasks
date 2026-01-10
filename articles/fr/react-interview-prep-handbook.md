---
title: Le guide de préparation aux entretiens React – Sujets essentiels et exemples
  de code
date: '2024-10-11T10:50:19.771Z'
author: Kunal Nalawade
authorURL: https://www.freecodecamp.org/news/author/KunalN25/
originalURL: https://freecodecamp.org/news/react-interview-prep-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1728643567956/00c98d19-4694-4942-9ad2-d2f25bcf05c0.png
tags:
- name: React
  slug: reactjs
- name: interview questions
  slug: interview-questions
- name: handbook
  slug: handbook
seo_desc: 'Hi everyone! In the ever-changing landscape of web development, React is
  in very high demand. Companies are often seeking skilled React developers to build
  dynamic and engaging web applications.

  If you are a web developer or aspiring to be one, it''s ...'
---


Salut à tous ! Dans le paysage en constante évolution du développement web, React est très demandé. Les entreprises recherchent souvent des développeurs React qualifiés pour créer des applications web dynamiques et attrayantes.

<!-- more -->

Si vous êtes un développeur web ou si vous aspirez à le devenir, il est important de comprendre ce que ces entreprises recherchent chez les candidats. Se préparer aux entretiens dans ces entreprises peut être une tâche intimidante.

C'est pourquoi, dans cet article, je vais lister certains sujets pour vous aider à préparer votre prochain entretien React. Nous discuterons de chaque sujet en détail, avec des exemples, afin que vous puissiez y jeter un coup d'œil avant les entretiens et éventuellement gagner un avantage sur les autres candidats. Plongeons dans le vif du sujet !

## Table des matières

-   [Fondamentaux de JavaScript][1]
    
-   [Les essentiels de React][2]
    
-   [Les Hooks React][3]
    
-   [Concepts additionnels][4]
    
-   [React Redux][5]
    
-   [Notes complémentaires][6]
    

## Fondamentaux de JavaScript

Pour préparer n'importe quel entretien de développement web, vous devez vous familiariser avec les fondamentaux de JavaScript, quel que soit le framework listé dans la description du poste. Les questions basées sur les frameworks sont toujours secondaires par rapport aux fondamentaux de JavaScript, attendez-vous donc à être testé sur JavaScript en premier.

Si vous êtes débutant, vous devez maîtriser les bases de JavaScript avant de vous lancer dans React. Beaucoup de gens (moi y compris) font l'erreur de sauter directement dans React après avoir appris un peu de JavaScript.

J'ai écrit un article détaillé sur les [concepts JavaScript importants pour les entretiens][7]. Vous pouvez l'inclure dans votre préparation à l'entretien React. Si vous maîtrisez tous les fondamentaux de JavaScript, vous pouvez passer à la section suivante.

## Les essentiels de React

Passons en revue quelques sujets essentiels avec lesquels vous devez vous familiariser :

### Qu'est-ce que le Virtual DOM dans React ?

Comme nous le savons tous, le DOM (Document Object Model) du navigateur est une structure en arbre de différents éléments HTML. Le Virtual DOM est une représentation en mémoire ou une version légère du DOM réel. C'est une abstraction créée par React qui est similaire au DOM réel.

Pourquoi React utilise-t-il le DOM virtuel ? La mise à jour et le rendu du DOM réel sont lents et inefficaces, surtout s'ils sont mis à jour fréquemment. Ainsi, au lieu de mettre à jour directement le DOM réel, React met à jour le DOM virtuel.

Le DOM virtuel est ensuite comparé au DOM réel et, une fois les différences identifiées, il ne met à jour que cette partie du DOM, plutôt que de restituer l'intégralité du DOM. Ce processus est connu sous le nom de [diffing et réconciliation][8].

### Qu'est-ce que le JSX ?

JSX (JavaScript XML) est une extension de syntaxe pour JavaScript qui vous permet d'écrire du code de type HTML dans le même fichier que le code JavaScript. Cela facilite grandement l'interaction de votre HTML avec JavaScript.

Vous pouvez écrire du code JSX dans un fichier `.js` ou `.jsx`. Considérez le fichier **MyComponent.jsx** suivant :

```
const MyComponent = () => {
    const name = "Kunal"
    return (
        <div>
            {name}
        </div>
    )
}
```

### Qu'est-ce que le State ?

Le State (état) est un objet React qui contient des informations sur le composant et détermine son comportement. Le State peut changer à tout moment en fonction du comportement de l'utilisateur. Tout changement d'état provoque le nouveau rendu (re-render) de l'ensemble du composant.

Le State est utilisé pour afficher des informations dynamiques dans le composant et rendre l'interface utilisateur interactive. Le State détermine comment un composant réagit aux événements tels que la saisie de l'utilisateur et la manipulation des données, et contrôle ce qu'il affiche à l'écran.

Quelques points à garder à l'esprit lors de l'utilisation du State :

-   Les States sont immuables. Mettez toujours à jour l'état à l'aide d'une fonction `setState`. Pour les objets/tableaux, créez-en de nouveaux et définissez l'état avec le nouveau tableau/objet. Cela garantit un comportement correct du composant.
    
-   N'utilisez le State que lorsque cela est nécessaire, évitez de stocker des informations redondantes car cela peut provoquer des re-renders inutiles.
    
-   Utilisez le State localement dans le même composant, évitez de faire descendre le State dans l'arbre DOM, sauf si cela est absolument nécessaire. Pour un état global, utilisez Context ou Redux.
    

Consultez la [documentation héritée][9] pour le State dans les composants de classe. Pour les composants fonctionnels, reportez-vous à la section [`useState`][10].

### Que sont les props ?

Les props (abréviation de properties) sont un moyen de passer des données d'un composant à un autre. Elles peuvent être considérées comme des arguments passés aux composants. Les props sont transmises à un composant enfant de la même manière que les attributs HTML.

Prenons un exemple :

```
function ParentComponent() {
  const name = "John Doe";
  const age = 30;

  const handleClick = () => {
    console.log("Button clicked")
  };

  return (
    <div>
      <ChildComponent name={name} age={age} handleClick={handleClick} />
    </div>
  );
}

function ChildComponent({ name, age, handleClick }) {
  return (
    <div>
      <p>Name: {name}</p>
      <p>Age: {age}</p>
      <button onClick={handleClick}>Click Me</button>
    </div>
  );
}
```

-   Ici, le composant parent transmet le nom, l'âge et la méthode handleClick en tant que props au composant enfant.
    
-   Ces props forment un objet `props` qui contient les valeurs transmises. Chaque composant fonctionnel prend un objet `props` comme argument.
    
-   Nous avons accédé aux props par déstructuration de l'objet dans le composant enfant.
    

Les props ne peuvent être transmises que dans un seul sens dans l'arbre des composants. C'est-à-dire du composant parent vers le composant enfant. Les props sont en lecture seule, vous ne pouvez pas changer leur valeur directement. Les valeurs d'état transmises en tant que props peuvent être mises à jour à l'aide de la fonction de mise à jour de l'état.

### Différence entre les composants de classe et fonctionnels

Les composants React sont de deux types : les composants de classe et les composants fonctionnels. Comprenons la différence entre les deux :

**Composants de classe :**

-   Les composants de classe sont écrits à l'aide de classes ES6. Leurs propriétés et fonctions sont accessibles via le mot-clé `this`. Ils ont besoin d'une méthode `render` pour renvoyer du JSX.
    
-   Les composants de classe sont des composants avec état (stateful) qui contiennent des fonctionnalités intégrées comme le State et le Context.
    
-   Ils ont des méthodes pour les différentes étapes du cycle de vie du composant : `componentDidMount()`, `componentDidUpdate()`, `componentWillUnmount()`, etc.
    
-   Les composants de classe sont verbeux, difficiles à lire et nécessitent toujours le mot-clé `this` pour accéder aux propriétés.
    

**Composants fonctionnels :**

-   Les composants fonctionnels sont de simples fonctions JavaScript qui prennent un objet `props` comme argument. Ils n'ont pas besoin de méthode `render`, ils renvoient directement du JSX.
    
-   Les composants fonctionnels sont sans état (stateless) et n'ont pas d'état propre à l'origine. Au lieu de cela, ils utilisent des Hooks pour utiliser les fonctionnalités des composants de classe comme le State ou le Context.
    
-   Il n'y a pas de méthodes de cycle de vie, le cycle de vie est géré avec le hook `useEffect`.
    
-   Les composants fonctionnels nécessitent moins de code que les composants de classe, ils sont donc plus faciles à lire et à écrire.
    

De nos jours, les développeurs préfèrent et recommandent les composants fonctionnels, en particulier avec les Hooks. Les composants de classe se trouvent généralement dans des bases de code plus anciennes.

Cependant, connaître les composants de classe est utile car de nombreuses entreprises ont d'anciennes bases de code écrites avec des composants de classe.

### Qu'est-ce que le cycle de vie des composants ?

Chaque composant React a un cycle de vie qui passe par trois phases : Montage (Mounting), Mise à jour (Updating) et Démontage (Unmounting).

**Montage (Mounting)**

Dans cette phase, un composant est créé et ajouté au DOM. Lorsqu'un composant est monté, les méthodes suivantes sont appelées :

-   [`constructor()`][11]

-   [`static getDerivedStateFromProps(props, state)`][12] (rarement utilisé)
    
-   [`render()`][13]
    
-   `componentDidMount()`
    

`componentDidMount()` n'est appelée qu'une seule fois ; c'est-à-dire lorsque le composant est monté. C'est la méthode préférée pour exécuter des effets de bord (side effects) lorsqu'un composant se charge pour la première fois. Dans les composants fonctionnels, son équivalent est le Hook `useEffect`.

**Mise à jour (Updating)**

Dans la phase de mise à jour, l'état ou les props du composant changent, ce qui provoque un re-render du composant. Les méthodes suivantes sont appelées lors de la mise à jour du composant :

-   [`shouldComponentUpdate(nextProps, nextState)`][14]
    
-   `render()` (appelée à nouveau)
    
-   [`getSnapshotBeforeUpdate()`][15]
    
-   `componentDidUpdate()`
    

La méthode `componentDidUpdate` est appelée aux moments suivants :

-   La première fois que le composant est monté, après la méthode `componentDidMount`.
    
-   Tout changement d'état ou de props déclenchant un re-render du composant.
    

Il est utile d'exécuter des effets de bord lorsqu'un état est mis à jour. Dans un composant fonctionnel, l'équivalent est `useEffect` avec des dépendances.

**Démontage (Unmounting)**

Dans cette phase, le composant est supprimé du DOM. La méthode `componentWillUnmount` est appelée pendant le démontage.

Elle est principalement utilisée pour les tâches de nettoyage avant que le composant ne soit démonté. Reportez-vous à la section [`useEffect`][16] pour son équivalent.

### Composants contrôlés et non contrôlés

Dans les composants contrôlés, les éléments de formulaire sont gérés par l'état React. Cela signifie que les valeurs des champs de formulaire sont définies et mises à jour ("contrôlées" par l'état React). Toutes les données du formulaire sont stockées dans l'état avant de soumettre le formulaire.

Exemple de composant contrôlé :

```
function ControlledComponent() {
  const [value, setValue] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Value: ${value}`);
  };

  return (
    <form onSubmit={handleSubmit}>
        <input type="text" value={value} onChange={(e) => setValue(e.target.value)} />
        <button type="submit">Submit</button>
    </form>
  );
}
```

-   La valeur du champ `input` est contrôlée par la variable d'état React `value`.
    
-   Lorsque vous mettez à jour le champ de saisie, l'état est mis à jour et la valeur de la saisie est définie en conséquence.
    

Les composants non contrôlés, en revanche, ne dépendent pas de l'état pour gérer les formulaires. Au lieu de cela, les valeurs des champs de formulaire sont gérées en interne, généralement avec des refs. Les refs sont utilisées pour interagir directement avec les éléments du DOM et mettre à jour les valeurs sans mettre à jour l'état ni provoquer de re-renders.

Exemple de composant non contrôlé :

```
function UncontrolledComponent() {
  const inputRef = useRef(null);

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Input Value: ${inputRef.current.value}`);
  };

  return (
    <form onSubmit={handleSubmit}>
        <input type="text" ref={inputRef} />
        <button type="submit">Submit</button>
    </form>
  );
}
```

Ici, nous avons utilisé une ref pour accéder directement au nœud DOM de l'élément d'entrée et utilisé sa valeur pour accéder aux données du formulaire. Cela simplifie considérablement la gestion des formulaires par rapport à l'utilisation de l'état.

Quand utiliser l'un ou l'autre :

-   Utilisez des composants contrôlés si vous voulez plus de contrôle sur les données que l'utilisateur saisit. Ceci est particulièrement utile lorsque deux champs de formulaire dépendent l'un de l'autre.
    
-   Si vous avez plusieurs états dépendants des données du formulaire, l'utilisation de l'état est une bonne pratique.
    
-   Utilisez des composants non contrôlés si votre formulaire est très simple et qu'il n'est pas nécessaire de manipuler les données du formulaire.
    

### Que sont les composants purs ?

Un composant pur est similaire à un composant normal, sauf qu'il ne s'affiche que si son état ou ses props ont changé.

Prenons un exemple :

```
const PureExample = React.memo(() => {
  return <h1> Hello {this.props.name} </h1>;
});

function App() {
  const [name, setName] = useState("");
  const [toggle, setToggle] = useState(false);
  return (
    <div className="App">
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <button onClick={() => setToggle(!toggle)}> Toggle </button>
      <PureExample name={name} />
    </div>
  );
}
```

-   `PureExample` est un composant pur qui est un enfant du composant `App`. Les composants purs peuvent être créés en entourant la fonction avec `React.memo()`.
    
-   Dans l'exemple, nous avons un champ `input` qui met à jour `name`, et un bouton qui bascule l'état, `toggle`.
    
-   `name` est transmis en tant que props à `PureExample`, il se re-render donc si `name` est mis à jour. Si vous mettez à jour `toggle` ou tout autre état, `PureExample` ne se re-render pas.
    

Dans le cas des composants de classe, les composants purs peuvent être créés en étendant la classe `PureComponent`. Cependant, les composants fonctionnels sont recommandés.

```
class PureExample extends React.PureComponent {
  render() {
    return <h1> Hello {this.props.name} </h1>;
  }
}
```

Habituellement, lorsque le composant parent se re-render, React restitue à nouveau tous ses composants enfants, même si aucun des composants enfants n'a été mis à jour.

Les composants purs sont utilisés pour les composants enfants qui n'ont besoin de se re-render que si l'une de leurs props change. Cela évite les re-renders inutiles et améliore les performances.

## Les Hooks React

Les Hooks React sont une fonctionnalité révolutionnaire introduite dans React en 2016. Les Hooks offrent un moyen d'implémenter les fonctionnalités des composants de classe dans les composants fonctionnels. Grâce aux hooks, les développeurs préfèrent aujourd'hui les composants fonctionnels aux composants de classe.

### Hook useState

Nous avons déjà vu ce qu'est le state. Comprenons comment implémenter l'état dans les composants fonctionnels avec un exemple simple :

```
const [count, setCount] = useState(0);
const increment = () => {
    setCount(count + 1);
};
const decrement = () => {
    setCount(count - 1);
};
return (
    <div>
        <h1>Count: {count}</h1>
        <button onClick={increment}>Increment</button>
        <button onClick={decrement}>Decrement</button>
    </div>
);
```

-   La fonction `useState` prend une valeur initiale comme argument et renvoie un tableau contenant deux éléments : l'état actuel et une fonction de mise à jour de l'état.
    
-   Dans cet exemple, nous avons deux boutons qui incrémentent et décrémentent le compteur. Au clic sur le bouton, les opérations d'incrémentation/décrémentation sont effectuées en mettant à jour l'état `count`.
    
-   Le composant se re-render et affiche le `count` mis à jour.
    

Pour plus d'exemples de ses utilisations, consultez mon article ci-dessous :

[https://levelup.gitconnected.com/4-different-examples-of-the-usestate-hook-in-react-5504ce011a20][17]

### Hook useEffect

Le hook `useEffect` est utilisé pour implémenter des effets de bord dans un composant. Les effets de bord incluent les appels d'API, l'abonnement à un service et la manipulation du DOM. `useEffect` peut également être utilisé pour mettre à jour conditionnellement un état en fonction d'un autre changement d'état.

Comprenons comment l'utiliser, avec un exemple :

```
function App() {
  const [data, setData] = useState([]);
  const [page, setPage] = useState(1);
  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`https://api.example.com/data?page=${page}`);
      const result = await response.json();
      setData(result);
    };

    fetchData();
  }, [page]);

  return (
    <div>
      <div> {JSON.stringify(data)} </div>
      <button onClick={() => setPage(page - 1)} disabled={page <= 1}>
        Previous
      </button>
      <button onClick={() => setPage(page + 1)}>Next</button>
    </div>
  );
}
```

-   `useEffect` prend deux arguments : une fonction qui effectue des effets de bord et un tableau de dépendances.
    
-   Dans cet exemple, nous affichons des données paginées en incluant la logique de récupération à l'intérieur d'un `useEffect` et en incluant la page actuelle dans la dépendance.
    
-   `useEffect` effectue l'appel API lors du premier rendu, chargeant la première page de données. Après cela, il charge des données supplémentaires chaque fois que l'utilisateur change de page.
    

Comment implémenter les méthodes de cycle de vie dans `useEffect` :

-   Pour implémenter `componentDidMount()`, passez un tableau de dépendances vide.
    
-   Pour implémenter `componentDidUpdate()`, passez des dépendances pour exécuter le `useEffect` si l'une de ces dépendances change.
    
-   Pour `componentWillUnmount()`, renvoyez une fonction de rappel (callback) de `useEffect` contenant le code de nettoyage.
    

`useEffect` peut être utilisé de nombreuses façons. La [documentation][18] de React contient plusieurs exemples d'utilisations.

### Hook useContext

Les states sont utilisés pour stocker des informations sur un composant et contrôlent son comportement. Dans certains cas, les composants enfants ont besoin d'accéder à l'état du composant parent.

Pour y parvenir, nous transmettons les données d'état sous forme de props. Cependant, le passage de données via les props peut entraîner des problèmes. Comprenons le problème majeur :

**Qu'est-ce que le Prop Drilling ?**

Pour passer des données du composant parent au composant enfant, nous utilisons des props. Mais que se passe-t-il si un composant situé profondément dans l'arbre des composants a besoin d'accéder à une prop ? Vous devriez la faire passer par plusieurs composants qui n'en ont même pas besoin.

Le même problème se pose lorsque plusieurs composants dans différentes branches de l'arbre ont besoin d'accéder à la même prop.

Le passage de props à travers de nombreux composants conduit à une situation connue sous le nom de prop drilling.

**Comment le contexte React résout-il le problème ?**

Le Context permet aux composants parents de passer des données à tous les composants de l'arbre sans passer par les props. Cela élimine le besoin de faire descendre les props à travers plusieurs composants de l'arbre.

Le Context a d'abord été introduit comme une [fonctionnalité des composants de classe][19], mais il peut désormais être utilisé dans les composants fonctionnels avec le hook `useContext`.

Voyons comment utiliser le hook :

```
import React, {useContext} from "react";

const DataContext = React.createContext(null);

export default function App() {
  return (
    <DataContext.Provider value="Some value">
      <MainComponent />
    </DataContext.Provider>
  );
}

function MainComponent() {
  const data = useContext(DataContext);
  return <div> Data: {data} </div>;
}
```

-   Nous avons utilisé la méthode `React.createContext` pour créer un contexte, puis nous avons créé une fonction fournisseur (provider) qui enveloppe le composant principal.
    
-   La prop `value` de `DataContext.Provider` est utilisée pour passer des données à l'ensemble de l'arbre des composants sous `MainComponent`.
    
-   Le Hook `useContext` consomme ces données à l'intérieur des composants. Il renvoie les données qui ont été passées à la prop `value` du fournisseur.
    

`useContext` ne peut être utilisé que si le composant ou l'un de ses parents possède un fournisseur de contexte enveloppé autour de lui. Des exemples de cas d'utilisation sont les thèmes, les informations utilisateur, les préférences linguistiques et la localisation, etc.

Consultez les utilisations supplémentaires de `useContext` dans la [documentation][20].

### Hook useRef

Les refs (abréviation de références) sont un moyen d'interagir directement avec les éléments du DOM. Elles vous donnent un accès direct à l'objet DOM JavaScript et à ses [méthodes][21].

Consultez la [documentation héritée][22] pour l'utilisation des refs dans les composants de classe. Dans les composants fonctionnels, nous avons le Hook `useRef`. Prenons un exemple :

```
export function App(props) {
  const myRef = useRef(null);

  useEffect(() => {
    myRef.current.focus();
  }, []);

  return <input type="text" ref={myRef} />;
}
```

-   `useRef` prend une valeur initiale comme argument et renvoie un objet `ref`.
    
-   Lorsque cet objet `ref` est passé à la prop `ref` d'un élément, nous obtenons une référence directe au nœud DOM de l'élément.
    
-   La valeur d'une `ref` est stockée à l'intérieur de sa propriété `current`.
    
-   Puisque `ref` est un objet DOM JavaScript, nous pouvons appeler la méthode [focus()][23] pour mettre le focus sur l'élément `input` lorsque le composant est monté.
    

Contrairement au state, les refs ne provoquent pas de re-renders du composant et, contrairement aux variables locales, les refs conservent leurs valeurs entre les rendus.

Quelques points à retenir sur les refs :

-   Les composants peuvent exposer leurs nœuds DOM aux composants parents en utilisant [forwardRef][24].
    
-   N'utilisez les refs que lorsque vous avez absolument besoin d'accéder aux éléments du DOM. Des exemples de cas d'utilisation pourraient être des tâches telles que la mise au point sur des éléments d'entrée, la sélection de tests, le déclenchement d'animations, la détermination de la position des éléments, etc.
    
-   Évitez de trop les utiliser, préférez le state et les props aux refs. Évitez de modifier explicitement les éléments du DOM pour contrôler le comportement des composants, utilisez plutôt le state.
    

### Hook useMemo

Si votre composant doit effectuer un calcul intensif lors du rendu de quelque chose, cela ralentit les performances du site Web puisque le composant exécute le calcul à chaque rendu.

Cela peut être acceptable pour une valeur d'état qui en dépend, mais c'est inefficace si la fonction coûteuse s'exécute à nouveau lors d'autres mises à jour d'état non liées. Pour y remédier, nous mémoïsons le résultat du calcul et ne le recalculons que lorsque l'état concerné change.

Le Hook `useMemo` est utilisé pour mémoïser le résultat de ce calcul, afin qu'il ne s'exécute pas à chaque rendu. Prenons un exemple :

```
const MemoExample = () => {
  const [computedValue, setComputedValue] = useState(value);
  const [otherState, setOtherState] = useState('Initial State');

  const expensiveFunction = () => {
      let result = 0;
      for (let i = 0; i < 10000000; i++) {
          result += i * 2;
      }
      return result;
  }

  const value = useMemo(expensiveFunction, [computedValue]);

  return  (
    <div>
      <button onClick={() => setComputedValue(computedValue + 1)}>
            Re-calculate
      </button>
      <button onClick={() => setOtherState('State Changed')}>
        Change Other State
      </button>
    </div>
  );
};
```

-   `useMemo` prend en entrée la fonction et un tableau de dépendances comme arguments, et renvoie le résultat de cette fonction. Il mémoïse le résultat pour le prochain rendu et renvoie la valeur mémoïsée à moins qu'une dépendance ne change.
    
-   Nous avons passé l'état `computedValue` à l'intérieur du tableau, donc, après s'être exécutée au premier rendu, la fonction ne s'exécutera que lorsque `computedValue` changera.
    
-   Si vous mettez à jour n'importe quel autre état, le composant se re-render, mais la fonction ne s'exécute pas à nouveau.
    

Quand l'utiliser :

-   Si vous ne voulez pas exécuter une fonction à chaque rendu, sauf pour l'état qui en dépend.
    
-   Pour maintenir l'égalité référentielle des tableaux et des objets à travers les rendus. Les références de tableaux/objets changent à chaque fois qu'ils sont déclarés.
    
-   Lors du rendu de listes avec [`Array.map`][25] qui n'ont pas besoin de changer sauf pour les mises à jour d'état pertinentes.
    

### Hook useCallback

`useCallback` est similaire à `useMemo`, la seule différence est que `useCallback` met en cache la définition de la fonction elle-même, plutôt que de mémoïser sa valeur de retour.

Semblable aux tableaux ou aux objets, une référence de fonction change à chaque fois qu'elle est déclarée. Ainsi, l'envelopper dans un `useCallback` maintient l'égalité référentielle de la fonction à travers les rendus.

Comprenons cela avec un exemple :

```
function ParentComponent() {
  const [toggle, setToggle] = useState(false);

  const handleSubmit = useCallback(() => {
    console.log('Child component form submitted');
  }, []); // Ajoutez les props ou l'état dont dépend cette fonction
  return (
    <div className={toggle ? 'dark' : ''}>
      <button onClick={() => setToggle(!toggle)}> Toggle Theme </button>
      <Child handleSubmit={handleSubmit} />
    </div>
  );
}

const Child = React.memo(({ handleSubmit }) => {

  for (let i = 0; i < 1000000000; i++) {
    // Supposons que le composant est lent
  }
  return (
    <div>
      <h2> Child component </h2>
      <button onClick={handleSubmit}> Click Me </button>
    </div>
  );
});
```

-   Ici, nous ralentissons délibérément le composant enfant pour simuler des rendus lents. Comme il est enveloppé dans `React.memo()`, il ne se re-render que si sa seule prop `handleSubmit` change.
    
-   Mais lorsque l'état `toggle` change, cela déclenche également un re-render pour le composant enfant, même s'il n'est pas transmis au composant enfant.
    
-   C'est parce que, chaque fois que le composant parent s'affiche, la fonction `handleSubmit` est créée avec une nouvelle référence. Donc, techniquement, `handleSubmit` a changé et ainsi, le composant enfant se re-render.
    
-   Pour éviter ce comportement, nous enveloppons la déclaration de la fonction `handleSubmit` dans un `useCallback`. Cela garantit que la référence de la fonction reste la même entre les rendus.
    
-   Dans notre exemple, la fonction n'est créée qu'une seule fois, puisqu'il n'y a pas de dépendances. Si vous ajoutez des dépendances, la fonction n'est recréée que si l'une d'entre elles change.
    

Quand l'utiliser :

-   Lorsque vous avez des gestionnaires d'événements (event handlers) définis pour un élément à l'intérieur de votre composant, enveloppez-les dans un `useCallback` pour éviter les recréations inutiles de gestionnaires d'événements.
    
-   Lorsque vous appelez une fonction à l'intérieur d'un `useEffect`, vous passez généralement la fonction comme dépendance. Pour éviter d'exécuter `useEffect` inutilement à chaque rendu, enveloppez la définition de la fonction dans un `useCallback`.
    
-   Si votre Hook personnalisé renvoie une fonction, il est recommandé de l'envelopper dans un `useCallback`. Ainsi, les utilisateurs n'ont pas à optimiser le Hook – ils peuvent plutôt se concentrer sur leur propre code.
    

Si vous voulez en savoir plus sur les hooks `useMemo` et `useCallback`, consultez mon article ci-dessous :

[https://www.freecodecamp.org/news/difference-between-usememo-and-usecallback-hooks/][26]

[https://www.freecodecamp.org/news/difference-between-usememo-and-usecallback-hooks/][27]

### Hook useReducer

Le Hook `useReducer` est un autre moyen de gérer l'état dans les applications React. À mesure que votre application grandit, son état devient de plus en plus complexe. Avec le temps, il devient difficile de gérer une logique d'état complexe avec le Hook `useState`.

useReducer offre un moyen plus structuré de gérer un état complexe en gérant toutes les mises à jour d'état dans une fonction réductrice (reducer). Cela facilite la gestion de l'état puisque toute la logique de mise à jour de l'état se trouve au même endroit.

Voyons comment utiliser ce hook avec un exemple :

```
const reducer = (state, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    case 'DECREMENT':
      return { count: state.count - 1 };
    case 'RESET':
      return { count: 0 };
    default:
      throw new Error(`Unknown action type: ${action.type}`);
  }
};

export function App(props) {
  const initialState = { count: 0 };
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <div className='App'>
      State: {state.count}
      <div>

        <button onClick={() => dispatch({ type: 'INCREMENT' })}>Increment</button>
        <button onClick={() => dispatch({ type: 'DECREMENT' })}>Decrement</button>
        <button onClick={() => dispatch({ type: 'RESET' })}>Reset</button>
      </div>
    </div>
  );
}
```

-   Cet exemple contient un état de compteur simple avec trois actions : incrémenter, décrémenter et réinitialiser.
    
-   Nous définissons une fonction reducer qui accepte l'état actuel et un objet action comme arguments. L'objet action contient le type d'action (une chaîne de caractères) et le payload (données transmises à l'action).
    
-   Le Hook `useReducer` accepte la fonction reducer et un état initial, et renvoie un tableau contenant l'état actuel et une méthode `dispatch`.
    
-   Pour mettre à jour l'état, nous appelons la méthode `dispatch` et passons le type d'action et le payload dans un objet. Nous appelons ce processus "dispatcher une action".
    

Quand utiliser `useReducer` :

-   N'utilisez ce hook que lorsque votre composant possède une logique de mise à jour d'état complexe. Comme cela implique d'écrire plus de code, préférez `useState` pour des mises à jour d'état plus simples. L'exemple simple fourni n'est qu'à des fins de démonstration.
    
-   Lorsqu'il y a beaucoup d'actions de mise à jour d'état avec des logiques différentes, il est logique de les avoir toutes dans une fonction séparée. Avec cela, vous passez simplement le type d'action et le payload à une fonction `dispatch` et le reducer gère la mise à jour de l'état.
    

Si vous voulez en savoir plus sur le hook `useReducer`, consultez mon article :

[https://www.freecodecamp.org/news/usereducer-hook-react/][28]

Jusqu'à présent, nous avons couvert les hooks les plus courants fournis par React. En plus de ceux-ci, React propose également des hooks supplémentaires, moins couramment utilisés. Donc, si vous êtes intéressé, lisez à leur sujet dans la [documentation][29]. Cependant, l'apprentissage des hooks ci-dessus devrait suffire pour vos entretiens.

### Hooks personnalisés (Custom Hooks)

Il existe des situations où vous pouvez avoir besoin de créer vos propres hooks en plus de ceux existants. Les hooks personnalisés offrent des fonctionnalités réutilisables à travers plusieurs composants et contribuent à un code plus propre et maintenable.

Pour créer un Hook personnalisé, identifiez d'abord une fonctionnalité que vous souhaitez réutiliser. Ensuite, vous pouvez l'exporter en tant que fonction dont le nom commence par le préfixe 'use'.

Supposons que vous ayez plusieurs composants qui doivent récupérer des données à partir d'API. Vous pouvez exporter la logique de récupération en tant que Hook pour éviter de dupliquer le code.

```
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const result = await response.json();
        setData(result);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [url]);

  return { data, loading, error };
}

export default useFetch;
```

-   Dans le hook personnalisé `useFetch`, nous avons récupéré les données à l'intérieur d'un Hook `useEffect`, tout comme nous le ferions à l'intérieur d'un composant. Nous avons également géré les états de chargement et d'erreur dans le Hook.
    
-   Enfin, nous renvoyons les données, avec les états de chargement et d'erreur, permettant au composant de les utiliser pour gérer la logique de rendu.
    

Utilisons cela dans un composant :

```
const UserList = () => {
  const { data, loading, error } = useFetch('https://jsonplaceholder.typicode.com/users');

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <ul>
      {data.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
};
```

Le composant `UsersList` affiche une liste d'utilisateurs récupérés à partir d'une API, et affiche également le texte "Chargement..." et une erreur le cas échéant. Pour utiliser le Hook personnalisé, nous avons appelé `useFetch` comme n'importe quel autre hook, et passé un point de terminaison d'API. Nous pouvons encore modifier le hook personnalisé `useFetch` pour inclure des en-têtes de requête, un corps de requête, etc.

De cette façon, les Hooks personnalisés vous aident à abstraire la logique d'un composant et à la rendre réutilisable dans toute l'application. Il existe plusieurs autres cas d'utilisation :

-   Écouteurs d'événements pour des événements tels que le redimensionnement de la fenêtre, les mouvements de la souris ou les pressions sur le clavier.
    
-   Gestion des formulaires, y compris la validation et la soumission des formulaires.
    
-   Thèmes, caches, transitions, etc.
    

Consultez la [documentation][30] pour en savoir plus sur les hooks personnalisés.

## Concepts additionnels

Voici quelques concepts supplémentaires qui peuvent être utiles :

### Pourquoi ne pas utiliser l'index comme clés lors du rendu de listes ?

Lorsque vous affichez des listes dans React à l'aide de la méthode [`Array.map`][31], on vous demande de fournir une prop `key` unique à chaque élément rendu. Cette clé est utilisée pour distinguer les éléments les uns des autres.

Les indices sont uniques, il est donc tentant de les utiliser comme clés par simplicité. Cependant, les indices des éléments ne sont pas stables.

Des éléments sont souvent ajoutés ou supprimés dans un tableau. L'ordre des éléments peut également être modifié. Dans ces cas, la valeur de la prop `key` change et peut entraîner un comportement imprévisible.

Considérons la liste suivante :

```
const items = [
  {
    id: 1,
    name: 'Item A'
  },
  {
    id: 2,
    name: 'Item B'
  },
  {
    id: 3,
    name: 'Item C'
  }
]
export const App = () => (
  <ul>
    {items.map((item, index) => (
      <li key={index}>
        {item.name}
      </li>
    ))}
  </ul>
);
```

Chaque élément rendu dans la liste a son index comme clé. Si nous supprimons `Item B` de la liste, les références des autres éléments sont modifiées.

React utilise des clés pour identifier de manière unique les éléments de la liste, afin que leur rendu devienne plus facile. React réutilise souvent ces éléments pour des rendus rapides. Cependant, si un élément est supprimé, les clés de tous les éléments suivants sont mises à jour.

React peut réutiliser la clé supprimée ou restituer à nouveau la liste entière, ce qui pourrait entraîner des problèmes de performances. Au lieu des indices, choisissez quelque chose d'unique, de préférence un nom d'utilisateur, un e-mail ou un identifiant généré par la base de données.

### Composants d'ordre supérieur (Higher Order Components)

Un composant d'ordre supérieur (HOC) est une fonction qui prend un composant comme argument et renvoie un nouveau composant qui enveloppe l'original. Les HOC vous permettent de fournir des fonctionnalités supplémentaires à un composant ainsi que de les réutiliser sur plusieurs composants.

Plutôt que de fournir une brève explication ici, je recommanderais l'article suivant qui explique les HOC avec divers exemples :

[https://www.freecodecamp.org/news/higher-order-components-in-react/][32]

### Chargement différé (Lazy Loading)

Le chargement différé (Lazy Loading) est un modèle de développement web qui retarde le chargement de ressources telles que des images, des vidéos ou des composants non essentiels. Il aide les pages Web à se charger plus rapidement en chargeant d'abord le contenu nécessaire à l'interaction, puis en chargeant le reste du contenu.

Un exemple de chargement différé est une page de catalogue de produits e-commerce. La page charge d'abord les noms et les prix des produits et les éléments cliquables. Ensuite, elle charge les images et les autres éléments de l'interface utilisateur.

Dans React, le chargement différé peut être implémenté en utilisant `React.lazy()` et `Suspense` :

```
const LazyComponent = React.lazy(() => import('./LazyComponent'));

export const App = () => {
  return (
    <div>
      <h1>Showing lazy component below</h1>
      <Suspense fallback={<div>Loading...</div>}>
        <LazyComponent />
      </Suspense>
    </div>
  );
};
```

-   Une fois que vous avez identifié un composant à charger de manière différée, utilisez la fonction `React.lazy()` pour importer dynamiquement le composant.
    
-   Enveloppez le composant chargé de manière différée à l'intérieur de `Suspense`. Il affiche un composant de secours (fallback) par défaut jusqu'à ce que le composant différé se charge.
    

De cette façon, vous pouvez charger un composant React à la demande. C'est ce qu'on appelle aussi le **code splitting**. Le code est divisé et une partie du code React est chargée dynamiquement en cas de besoin.

Le code splitting optimise les performances des applications React qui ont de grands composants complexes. En utilisant `Suspense`, vous pouvez afficher une interface utilisateur temporaire à l'utilisateur, afin qu'il n'ait pas à regarder un écran vide pendant le chargement d'un composant.

Le code splitting divise votre application en plusieurs morceaux (chunks), chaque morceau étant chargé indépendamment. Ce processus est donc également connu sous le nom de **chunking**.

### Différence entre le rendu côté client et le rendu côté serveur

Il existe deux façons de restituer des pages Web dans React. Jetons-y un coup d'œil :

**Rendu côté serveur (SSR - Server Side Rendering) :**

-   La page Web est générée et rendue sur le serveur avant d'être envoyée au client. Le client reçoit la page Web complète du serveur et l'affiche directement à l'utilisateur.
    
-   Le chargement du HTML préparé permet des temps de chargement plus rapides, améliorant ainsi l'expérience utilisateur. Ceci est particulièrement bénéfique pour les utilisateurs ayant des connexions Internet plus lentes.
    
-   Comme la page Web est déjà préparée, cela aide les moteurs de recherche à mieux indexer votre site Web, ce qui le rend plus convivial pour le SEO.
    
-   Le SSR peut augmenter la charge du serveur si la page est mise à jour fréquemment. Les pages avec un contenu dynamique peuvent prendre plus de temps à se mettre à jour car elles doivent être re-rendues souvent.
    
-   Le SSR est utilisé pour les sites Web de marketing, de blogging et d'actualités où les temps de chargement initiaux et le SEO sont importants.
    

**Rendu côté client (CSR - Client Side Rendering) :**

-   Un fichier HTML de base est envoyé au client, puis il rend le contenu dynamique à l'aide de JavaScript.
    
-   Les temps de chargement initiaux sont plus lents car la préparation et le rendu du contenu se font principalement du côté client.
    
-   Comme il rend initialement du HTML de base et ajoute du contenu JavaScript plus tard, les moteurs de recherche peuvent ne pas être en mesure d'indexer votre contenu, ce qui le rend moins convivial pour le SEO.
    
-   Pour les pages Web avec un contenu dynamique, les temps de rendu sont plus rapides puisque tout le rendu se fait du côté client.
    
-   Le CSR est utilisé pour les sites Web avec un contenu dynamique et des interactions utilisateur fréquentes comme les plateformes de réseaux sociaux ou les tableaux de bord.
    

## React Redux

Redux est une bibliothèque de gestion d'état qui aide à gérer l'état complexe d'une application. C'est une bibliothèque puissante pour gérer l'état dans les grandes applications React.

Dans le contexte de React, examinons les Hooks fournis par Redux :

### useSelector

Une fonction sélectrice (selector) accepte un objet d'état Redux comme argument et renvoie une partie de cet état. Le Hook `useSelector` est utilisé pour appeler la fonction sélectrice. Prenons l'exemple suivant :

```
// exemple d'état pour une application e-commerce
const initialState = {
    users: { 
        ...
    },
    products: {
        ...
    },
    cart: {
        ...
    }
    orders: {
        ordersList: [
            {
                id: 101,
                status: "Shipped"
            },
            {
                id: 102,
                status: "Processing"
            },

            ...
        ]
    }
}
```

Disons que vous voulez afficher la liste des commandes sur une page. Nous ne pouvons pas accéder à cet état directement depuis le composant car il fait partie du store Redux. Nous utilisons donc des fonctions sélectrices.

```
const selectAllOrders = (state) => state.orders.ordersList
```

Pour appeler cette fonction sélectrice, nous utilisons le Hook `useSelector` :

```
const OrdersList = () => {
  const orders = useSelector(selectAllOrders);
  return (
    // afficher les commandes
  );
};
```

Le principal avantage de l'utilisation des sélecteurs est que vous accédez à l'objet d'état Redux, ce qui vous permet d'accéder à n'importe quelle tranche (slice) de l'état.

### useDispatch

Le Hook `useDispatch` renvoie une fonction que vous pouvez utiliser pour dispatcher des actions, telles que la mise à jour de l'état et l'appel d'API. Cette fonction prend un objet action comme argument et effectue l'action correspondante. Cette fonction est connue sous le nom de fonction de dispatch.

Prenons un exemple. Nous allons travailler avec le même état et mettre à jour le statut de l'une des commandes :

```
function App() {
  const dispatch = useDispatch();

  const handleUpdateStatus = () => {
    dispatch({type: 'ORDER_UPDATE_STATUS', payload: {
      id: 102,
      status: "Shipped"
    }});
  };

  return (
    <div>
      <h2>Update Order Status</h2>
      <button onClick={handleUpdateStatus}>Mark as Delivered</button>
    </div>
  );
}
```

Ici, l'action `ORDER_UPDATE_STATUS` sera dispatchée avec le payload correspondant. Cette action sera mappée à un reducer qui effectuera la mise à jour de l'état.

L'avantage d'utiliser dispatch est que vous pouvez simplement spécifier le type d'action et passer le payload, et la logique de mise à jour de l'état sera gérée par le reducer, au lieu du composant lui-même.

### Autres

Je n'ai listé que deux Hooks fournis par React pour travailler avec Redux. Cependant, si vous n'êtes pas familier avec Redux, vous devriez consulter la [documentation][33] pour commencer.

Redux est bien plus que ces deux Hooks. Assurez-vous d'être au clair sur les concepts de base : store, slices, reducers, actions, selectors, dispatch. [Redux Sagas][34] est un autre concept majeur que vous devriez apprendre. Ils sont principalement utilisés pour les opérations asynchrones.

## Notes complémentaires

Il y a quelques autres domaines que je n'ai pas mentionnés jusqu'à présent, mais qui peuvent être un bon complément :

-   [React Router][35]
    
-   [Tests unitaires dans React][36]
    

De plus, on peut vous demander d'implémenter une petite fonctionnalité en utilisant les concepts que j'ai expliqués dans cet article. Cela vous donne l'occasion de démontrer votre compréhension de React.

Il est également utile d'avoir quelques projets React sur votre CV. Consultez [Maîtriser React en construisant 25 projets][37].

Gardez à l'esprit que React ne se limite pas à ces sujets, il existe des ressources supplémentaires dans la section Références. Cependant, ce guide devrait servir de guide utile avant les entretiens. N'hésitez pas à le consulter régulièrement pendant votre préparation aux entretiens.

## Conclusion

Dans ce guide, nous avons souligné plusieurs sujets importants pour préparer votre prochain entretien React. Nous avons commencé par quelques concepts de base dans React, puis nous sommes passés aux Hooks. Ensuite, nous avons vu quelques concepts supplémentaires qu'il est bon de connaître avant de discuter de React Redux.

J'ai écrit des explications claires et concises pour chaque sujet, avec des exemples. Cela devrait vous aider à articuler ces concepts devant les recruteurs. Là où je n'ai pas pu expliquer en détail, j'ai pointé vers d'autres ressources utiles qui expliquent mieux. Cela fait de cet article votre lieu de référence à tout moment pendant votre préparation aux entretiens.

Pendant les entretiens, restez calme et démontrez vos connaissances avec confiance. Une bonne communication fait une bonne impression lors de l'entretien. Enfin, n'oubliez pas que chaque entretien est une opportunité d'apprentissage, que vous réussissiez ou non. Restez positif et continuez à affiner vos compétences. Bonne chance pour vos entretiens !

### Références

-   [Questions d'entretien React – Préparation à l'entretien avec réponses et exemples][38]
    
-   [Questions d'entretien React][39] - InterviewBit
    
-   [Apprendre React – Un guide des concepts clés par Ankur Tyagi][40]
    

[1]: #heading-fondamentaux-de-javascript
[2]: #heading-les-essentiels-de-react
[3]: #heading-les-hooks-react
[4]: #heading-concepts-additionnels
[5]: #heading-react-redux
[6]: #heading-notes-complementaires
[7]: https://www.freecodecamp.org/news/js-interview-prep-handbook/
[8]: https://legacy.reactjs.org/docs/reconciliation.html
[9]: https://legacy.reactjs.org/docs/state-and-lifecycle.html
[10]: #heading-hook-usestate
[11]: https://www.geeksforgeeks.org/react-js-constructor-method/
[12]: https://www.geeksforgeeks.org/react-js-static-getderivedstatefromprops/
[13]: https://www.geeksforgeeks.org/react-js-render-method/
[14]: https://www.geeksforgeeks.org/reactjs-shouldcomponentupdate-method/
[15]: https://www.geeksforgeeks.org/reactjs-getsnapshotbeforeupdate-method/
[16]: #heading-hook-useeffect
[17]: https://levelup.gitconnected.com/4-different-examples-of-the-usestate-hook-in-react-5504ce011a20
[18]: https://react.dev/reference/react/useEffect#usage
[19]: https://legacy.reactjs.org/docs/context.html
[20]: https://react.dev/reference/react/useContext#usage
[21]: https://www.tutorialspoint.com/javascript/javascript_dom_methods.htm
[22]: https://legacy.reactjs.org/docs/refs-and-the-dom.html
[23]: https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus
[24]: https://react.dev/reference/react/forwardRef
[25]: http://Array.map
[26]: https://www.freecodecamp.org/news/difference-between-usememo-and-usecallback-hooks/
[27]: https://www.freecodecamp.org/news/difference-between-usememo-and-usecallback-hooks/
[28]: https://www.freecodecamp.org/news/usereducer-hook-react/
[29]: https://react.dev/reference/react/hooks
[30]: https://react.dev/learn/reusing-logic-with-custom-hooks
[31]: http://Array.map
[32]: https://www.freecodecamp.org/news/higher-order-components-in-react/
[33]: https://redux.js.org/introduction/getting-started
[34]: https://redux-saga.js.org/docs/introduction/GettingStarted
[35]: https://www.freecodecamp.org/news/react-router-cheatsheet/
[36]: https://www.freecodecamp.org/news/how-to-write-unit-tests-in-react/
[37]: https://www.freecodecamp.org/news/master-react-by-building-25-projects/
[38]: https://www.freecodecamp.org/news/react-interview-questions-and-answers/
[39]: https://www.interviewbit.com/react-interview-questions/
[40]: https://www.freecodecamp.org/news/learn-react-key-concepts/#how-much-javascript-do-you-need-to-know-before-learning-react