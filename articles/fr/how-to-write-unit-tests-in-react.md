---
title: Comment écrire des tests unitaires dans React
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2023-01-23T15:35:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-unit-tests-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/unit-testing-in-react-image.jpeg
tags:
- name: React
  slug: react
- name: Software Testing
  slug: software-testing
- name: unit testing
  slug: unit-testing
seo_title: Comment écrire des tests unitaires dans React
seo_desc: 'When you''re building a website and coding all the cool features you had
  planned, you''ll want to test if everything works as expected.

  Now, you can’t do that just by going through the website yourself – you need to
  check if each unit of your code is w...'
---

Lorsque vous construisez un site web et codez toutes les fonctionnalités cool que vous aviez prévues, vous voudrez tester si tout fonctionne comme prévu.

Maintenant, vous ne pouvez pas faire cela simplement en parcourant le site web vous-même – vous devez vérifier si chaque unité de votre code fonctionne comme vous le souhaitez. Pour cela, vous devez écrire des tests unitaires. Et ils peuvent être assez fastidieux lorsque vous vous mettez réellement à les écrire.

Alors, dans cet article, je vais vous montrer comment vous pouvez commencer à écrire des tests unitaires dans React. Je vais expliquer le processus à travers plusieurs exemples pour vous aider à mieux comprendre.

Pour cet article, je suppose que vous avez une connaissance de base de React. Si ce n'est pas le cas, alors dirigez-vous vers les [docs](https://reactjs.org/docs/getting-started.html) pour commencer.

## Comment un test est-il structuré ?

Les tests impliquent de vérifier si votre code fonctionne comme il est censé le faire en comparant la sortie attendue avec la sortie réelle.

### Que tester

En général, vos tests doivent couvrir les aspects suivants de votre code :

1. Si un composant se rend avec ou sans props

2. Comment un composant se rend avec les changements d'état

3. Comment un composant réagit aux interactions utilisateur

### Que ne pas tester

Tester la plupart de votre code est important, mais voici quelques choses que vous n'avez pas besoin de tester :

1. **Implémentation réelle :** Vous n'avez pas besoin de tester l'implémentation réelle d'une fonctionnalité. Testez simplement si le composant se comporte correctement.
   Supposons que vous souhaitiez trier un tableau au clic d'un bouton. Il n'est pas nécessaire de tester la logique de tri réelle. Vous testez uniquement si la fonction a été appelée et si les changements d'état sont rendus correctement.

2. **Bibliothèques tierces :** Si vous utilisez des bibliothèques tierces comme Material UI, pas besoin de les tester – elles devraient déjà être testées et éprouvées.

Cela peut sembler un peu compliqué pour le moment, mais vous devriez mieux comprendre à travers des exemples.

Tout test dans React, peu importe sa complexité, suit cette structure :

1. Rendre le composant

2. Obtenir un élément du composant et simuler des interactions utilisateur

3. Écrire une assertion.

## Comment configurer notre projet

Tout d'abord, créez l'application avec `create-react-app`. Nous utiliserons [Jest](https://jestjs.io/docs/getting-started) et [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/). Les deux viennent préinstallés avec `create-react-app`. Vous pouvez voir à quoi cela ressemble ici :

```javascript
"dependencies": {
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.4.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
},
```

Comme vous pouvez le voir, Jest n'est pas visible ici. Mais, si vous allez dans le dossier `node_modules`, vous verrez Jest là. Donc, pas besoin de l'installer séparément.

Assurez-vous également d'avoir les lignes suivantes dans votre fichier `setupTests.js` :

```javascript
import '@testing-library/jest-dom';
import '@testing-library/jest-dom/extend-expect';
```

De plus, dans votre fichier `package.json`, modifiez vos scripts comme ceci :

```javascript
"scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test --watchAll --coverage",
    "eject": "react-scripts eject"
},
```

Cela exécutera vos tests en mode surveillance et vous montrera également la couverture (c'est-à-dire la portion du code couverte par vos tests). Vous pouvez également définir le seuil de couverture en ajoutant une autre propriété `jest`. Pour l'instant, gardez le seuil à 80 %.

```javascript
"jest": {
    "coverageThreshold": {
        "global": {
            "lines": 80
        }
    }
}
```

C'est tout, vous êtes maintenant prêt à commencer les tests. Commençons d'abord par un test de base.

## Comment écrire votre premier test pour une application React

Écrivons un test pour le composant suivant :

```javascript
const FirstTest = () => {
  return (
    <div>
        <h2> First test </h2>
    </div>
  )
}
```

Ici, nous devons simplement tester si l'élément `h2` se rend. Maintenant, où devons-nous écrire les tests ? Nous pouvons les écrire dans un dossier `__tests__` n'importe où dans le dossier `src`. Le fichier de test doit simplement avoir une extension `.test.js/jsx` et le runner de test le prendra.

Voici à quoi ressemble le test dans notre fichier `FirstTest.test.jsx` :

```javascript
import { render, screen } from '@testing-library/react'
import FirstTest from '../components/FirstTest';

test("Example 1 renders successfully", () => {
    render(<FirstTest/>);

    const element = screen.getByText(/first test/i);

    expect(element).toBeInTheDocument();
})
```

Tout d'abord, importez les méthodes requises. La méthode `test()` contient un test individuel. Elle prend le nom du test et une fonction de rappel comme les deux arguments.

Maintenant, en suivant la structure mentionnée ci-dessus, rendez le composant que vous testez en utilisant la méthode [render](https://testing-library.com/docs/react-testing-library/api/#render). Ensuite, utilisez l'objet `screen` pour faire une requête pour un élément. Dans ce cas, c'est l'élément `h2`. Notre requête obtient un élément contenant du texte qui correspond à l'expression régulière `/first test/i` (*i* signifie ignorer la casse).

Enfin, faites l'assertion en utilisant la méthode `expect`. Nous nous attendons à ce que l'élément soit dans le document et il y est, donc le test passe.

Il existe de nombreuses autres assertions que vous pouvez faire dans vos tests. Vous pouvez en lire plus à leur sujet [ici](https://jestjs.io/docs/using-matchers). De plus, vous pouvez trouver une liste de façons de requêter un élément [ici](https://testing-library.com/docs/queries/about). Nous en utiliserons certaines dans nos exemples suivants.

## Comment tester avec des données mockées dans React

Ici, nous avons un composant avec une prop `data` qui affiche une liste d'éléments. Supposons que ces données proviennent du backend et que votre composant affiche ces données.

```javascript
import React from 'react'

const TestWithMockData = ({data}) => {
  return (
    <div>
        <ul>
            {data.map(item => (
                <li key={item.id}>
                    {item.id}
                    {item.first_name},
                    {item.last_name},
                    {item.email}

                </li>
            ))}
        </ul>
    </div>
  )
}

export default TestWithMockData
```

Lors de l'écriture de tests pour un composant avec des props, vous devez passer des données mockées lors du rendu de ce composant qui concerne votre fonctionnalité. Ici, un objet dans nos données contient quatre champs, donc nous passons des données mockées ici.

```javascript
const mockData = [
    {
        "id": 1,
        "first_name": "Fletcher",
        "last_name": "McVanamy",
        "email": "mmcvanamy0@e-recht24.de",
        "age": 30
      }, {
        "id": 2,
        "first_name": "Clarice",
        "last_name": "Harrild",
        "email": "charrild1@dion.ne.jp",
        "age": 35
      }, 
]
```

Notez que les données réelles pourraient contenir des milliers d'enregistrements, mais les données mockées n'ont besoin d'être pertinentes que pour ce que vous voulez tester. Maintenant, écrivons le test et vérifions si la liste se rend.

```javascript
test("List renders successfully", () => {
    render(<TestWithMockData data={mockData} />)
    expect(screen.getByText(/fletcher/i)).toBeInTheDocument();
})
```

## Comment tester avec des données mockées couvrant toutes les branches dans React

Introduisons un peu de branchement dans le composant ci-dessus. Nous aurons une autre prop, `displayUnorderedList`, qui détermine si une liste ordonnée ou non ordonnée doit être affichée. Nous afficherons également `Senior` pour `age > 50` et `Not Senior` sinon.

```javascript
import React from 'react'

const TestWithMockData = ({data, displayUnorderedList, handleClick}) => {
  return (
    <div>
        {displayUnorderedList ? 
            <ul>
                {data.map(item => (
                    <li key={item.id}>
                        {item.id}
                        {item.first_name},
                        {item.last_name},
                        <a onClick={() => {
                            console.log("email link clicked")
                            handleClick()
                        }}>{item.email}</a>

                        {item.age > 50 ? 'Senior' : 'Not senior'}

                    </li>
                ))}
            </ul>
        : 
            <ol>
                {data.map(item => (
                    <li key={item.id}>
                        Last name: {item.last_name}
                    </li>
                ))}
            </ol>
        }
    </div>
  )
}

export default TestWithMockData
```

Voici le rapport de couverture jusqu'à présent :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-141.png align="left")

*Test échoué : Impossible de trouver l'élément*

Vous pouvez voir que la ligne 9 (c'est-à-dire la partie liste non ordonnée) n'est pas couverte par nos tests existants. Et notre test précédent a également échoué car il est incapable de trouver `fletcher` dans le composant.

Pourquoi en est-il ainsi ? Dans notre test précédent, nous n'avons pas passé la prop `displayUnorderedList` au composant, donc elle est `null`. Ainsi, le composant rend la liste ordonnée et elle ne contient pas le `first_name`.

Alors, écrivons un autre test couvrant la partie liste ordonnée.

```javascript
test("Ordered list renders", () => {
    render(<TestWithMockData data={mockData} displayUnorderedList={false} />)

    expect(screen.getByText(/McVanamy/i)).toBeInTheDocument()
})
```

Ici, passez la valeur de la prop à `false` pour rendre la liste ordonnée. Ajoutez également la prop `displayUnorderedList` au test échoué et passez la valeur `true`.

Maintenant, tous nos tests passent avec une couverture de 100 %.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-142.png align="left")

*Branche non couverte*

Une ligne n'est toujours pas couverte par les cas de test, qui est la logique de branchement pour `age`. Donc, ajoutez un autre enregistrement aux données mockées qui a un âge supérieur à 50.

```javascript
{
    "id": 3,
    "first_name": "Amby",
    "last_name": "Emmer",
    "email": "aemmer2@buzzfeed.com",
    "age": 67
}
```

Maintenant, tous nos tests devraient passer avec une couverture de 100 %.

## Comment tester les interactions utilisateur dans React

La partie la plus importante du test de toute application UI est de tester son comportement avec diverses interactions utilisateur. Presque toutes les fonctionnalités d'une application UI impliquent des interactions utilisateur.

Vous pouvez utiliser la bibliothèque `user-event` pour simuler des interactions utilisateur. Elle dispose de méthodes pour simuler divers événements utilisateur tels que *click*, *type*, *hover*, et ainsi de suite.

Tout d'abord, nous devons installer la bibliothèque :

```python
npm install --save-dev @testing-library/user-event
```

Nous pouvons utiliser cette bibliothèque pour simuler des événements utilisateur. Dans nos exemples, nous interagirons avec différents éléments, principalement des éléments `input` et `button`.

### Comment tester un appel de fonction au clic d'un élément

Dans notre composant ci-dessus, nous devons rendre le champ `email` cliquable et appeler une fonction `handleClick` dessus. Cela sera passé en tant que props au composant. Là, remplacez `{item.email}` par :

```javascript
<a onClick={() => {
    console.log("email link clicked")
    handleClick()
}}>{item.email}</a>
```

Maintenant, notre couverture de test prend un coup. Pour couvrir ce scénario, écrivez le test suivant :

```javascript
test("Email link click handler called", async () => {
    const mockHandleClick = jest.fn();
    render(<TestWithMockData 
                data={mockData} 
                displayUnorderedList={true}
                handleClick = {mockHandleClick}
          />)
    await userEvent.click(screen.getByText(/mmcvanamy0@e-recht24.de/i));
    expect(mockHandleClick).toHaveBeenCalled();
})
```

Tout d'abord, créez le mock de la fonction `handleClick` en utilisant `jest.fn()`. Nous n'avons pas besoin de l'implémentation réelle de la méthode, car nous voulons seulement tester le comportement du composant. Donc, nous créons un mock vide et passons le même en tant que props. Lisez plus sur le mocking des fonctions [ici](https://jestjs.io/docs/mock-functions).

Maintenant, requêtez l'élément `<a>` par texte (n'importe quel `email` des données mockées). Utilisez la méthode `click()` pour simuler un événement de clic. Utilisez `await` car la simulation d'un événement utilisateur est une opération asynchrone.

Écrivez une assertion à la fin pour vérifier si la méthode a été appelée. La méthode a été appelée, donc notre test passe avec une couverture de 100 %.

### Comment requêter les champs de saisie et les boutons

Jusqu'à présent, nous avons utilisé une seule méthode de requête d'éléments – `getByText()`. Maintenant, voyons comment vous pouvez requêter les champs de saisie et les boutons.

```html
<input placeholder='Enter name'/>
<button> Submit </button>
```

Pour requêter ces éléments, vous pouvez faire ce qui suit :

```javascript
const inputElement = screen.getByRole('textbox')
```

`getByRole` trouve un élément par le rôle donné. Dans ce cas, le rôle `textbox` signifie l'élément `input`.

Comment le rôle est-il déterminé ? Chaque élément a un rôle défini, donc vous n'avez pas besoin de spécifier un attribut de rôle explicite. Vous pouvez voir une liste des rôles pour différents éléments [ici](https://www.w3.org/TR/html-aria/#docconformance). Quel que soit l'élément que vous voulez, faites simplement `getByRole` et référez-vous à la liste.

Pour `button`, le rôle par défaut est 'button' comme vous pouvez le voir ici :

```javascript
const button = screen.getByRole('button')
```

Que se passe-t-il si nous ajoutons un autre élément `input`, `<input placeholder='Enter description'/>` ? Le runner de test lancera maintenant une erreur disant qu'il y a deux éléments avec le même rôle. Que devons-nous faire dans un tel scénario ? Utilisez une autre requête `getByPlaceholderText()`.

```javascript
const nameInput = screen.getByPlaceholderText(/enter name/i);
const descrInput = screen.getByPlaceholderText(/enter description/i);
```

Vous pouvez également utiliser `getByLabelText()` si votre `input` a une `label`.

```javascript
<label htmlFor='password'> Enter password</label>
<input type='password' id='password'/>
```

```javascript
const passwordInput = screen.getByLabelText(/enter password/i);
```

Pour requêter les boutons, nous pouvons faire `screen.getByRole('button')`.

```html
<button> Submit </button>
<button> Apply</button>
```

Puisque nous avons deux boutons ici, faire simplement `getByRole` lancera une erreur. Donc, nous utilisons une option `name`.

```javascript
const submitButton = screen.getByRole('button', { name: /submit/i });
const applyButton = screen.getByRole('button', { name: /apply/i });
```

L'option `name` peut contenir le libellé d'un élément de formulaire, le texte d'un bouton ou la valeur de l'attribut `aria-label` de n'importe quel élément. Nous pouvons également faire `getByText()` pour un bouton.

```javascript
const submitButton = screen.getByText(/submit/i);
```

## Comment tester les mises à jour d'état dans React

Nous avons vu comment requêter des éléments de formulaire comme `input` et `button`. Maintenant, simulons quelques interactions utilisateur et testons les mises à jour d'état. Que veux-je dire par tester les mises à jour d'état ?

Les mises à jour d'état provoquent un nouveau rendu d'un composant. Donc, lorsque votre fonctionnalité effectue une mise à jour d'état, vous devez tester comment le composant se comporte en raison du changement d'état.

Tout d'abord, prenons un exemple simple où nous définissons l'état dès que le composant est chargé – c'est-à-dire dans le bloc `useEffect`.

```javascript
const TestingStateChange = () => {
    const [loaded, setLoaded] = useState(false)
    useEffect(() => {
        setLoaded(true)
    }, [])
  return (
    <div>
        {loaded && <h3> Page Loaded </h3>}
    </div>
  )
}
```

Ici, tout votre composant, à partir de l'instruction `useEffect` jusqu'à la fin, n'est pas couvert. Lorsque vous écrivez le test suivant, non seulement la partie HTML est couverte, mais aussi la partie `useEffect` où vous définissez l'état.

```javascript
test("Testing page load", () => {
    render(<TestingStateChange/>)
    expect(screen.getByText(/page loaded/i)).toBeInTheDocument();
})
```

C'est ainsi que vous testez les mises à jour d'état. Vous testez si le composant se comporte comme vous l'attendez avec un changement d'état.

### Comment tester un changement d'état au clic d'un bouton

Ayons un bouton et un texte qui bascule au clic du bouton.

```javascript
const [toggleTextVisible, setToggleTextVisible] = useState(false)`
```

```html
{toggleTextVisible && <p> Text visible </p> }

<button onClick={() => { setToggleTextVisible(!toggleTextVisible) }}> 
    Toggle text 
</button>
```

Nous allons écrire le test pour cela :

```javascript
test("Toggle text visible", async () => {
    render(<TestingStateChange/>);
    await userEvent.click(screen.getByText(/toggle text/i));
    expect(screen.getByText(/text visible/i)).toBeInTheDocument();
})
```

Avec `userEvent`, nous avons simulé le clic d'un bouton et asserté si le texte est visible.

Maintenant, testons un autre scénario où nous vérifions si le bouton ci-dessus est désactivé au clic d'un autre bouton.

```javascript
const [btnDisabled, setBtnDisabled] = useState(false);
```

Ajoutez un attribut `disabled={btnDisabled}` au bouton ci-dessus et créez un autre bouton qui contrôle sa valeur.

```html
<button onClick={() => { setBtnDisabled(!btnDisabled) }}> 
      Toggle button disabled 
</button>
```

Utilisez la méthode `toBeDisabled()` pour tester si le bouton est désactivé.

```javascript
test("Button disabled on click", async () => {
    render(<TestingStateChange/>)
    await userEvent.click(screen.getByText(/toggle button disabled/i));
    expect(screen.getByText(/toggle text/i)).toBeDisabled();
})
```

### Comment tester si un élément a été ajouté à une liste

Effectuons une autre assertion. Ici, nous vérifierons si un élément a été ajouté à une liste. Nous aurons des données et créerons un état avec les données comme valeur initiale. Nous l'afficherons tout en ayant un bouton pour ajouter un élément.

```javascript
const [elements, setElements] = useState(data);
```

```html
<h3> List </h3>
{elements.map(item => (
    <div key= {item.id}>
       {item.id}: { item.name }
    </div>
))}
<button onClick={() => {
    setElements([...elements, {
        id: 4,
        name: 'abhinav'
    }])
}}> Add to list </button>
```

Ajoutez un attribut `data-testid='record'` à chaque enregistrement pour aider à requêter l'élément. Écrivons le test pour cela :

```javascript
test("Element added to the list", async () => {
    render(<TestingStateChange/>)
    expect(screen.getAllByTestId('record').length).toBe(3);

    await userEvent.click(screen.getByText(/add to list/i));
    expect(screen.getAllByTestId('record').length).toBe(4);
})
```

Pour obtenir plusieurs éléments avec la même requête, utilisez la méthode `getAllBy`. Dans ce cas, il y a plusieurs éléments avec le test-id `record`, donc l'utilisation de la méthode `getAllByTestId()` obtient une liste de tous ces éléments.

Ici, nous avons vérifié la longueur de la liste. Nous pouvons ajouter une autre assertion pour vérifier si le nouvel élément est visible.

```javascript
expect(screen.getByText(/abhinav/i)).toBeInTheDocument();
```

### Comment tester si un élément a été supprimé d'une liste

Maintenant, ajoutons un autre bouton qui supprime un élément de la liste.

```html
<button onClick={() => {
    setElements(elements.filter(item => item.id != 2))
}}> Remove from list </button>
```

Le test pour cela :

```javascript
test("Element removed from list", async () => {
    render(<TestingStateChange/>)
    await userEvent.click(screen.getByText(/remove from list/i));
    expect(screen.getAllByTestId('record').length).toBe(2);
})
```

Ici, nous testons si la longueur de la liste a été réduite. Tous nos tests passent avec une couverture de 100 %.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-143.png align="left")

*Rapport de couverture pour le test de changement d'état : Tests réussis*

## Comment tester les appels API dans React

Les appels API sont une partie importante de toute application UI. Comprenons comment tester un appel API.

Dans cet exemple, nous avons un fichier `data.json` qui contient des données. Nous allons faire un appel API pour récupérer ces données.

Pour la démonstration, nous allons sauvegarder ce fichier sur le serveur local uniquement (dans le dossier `public`), mais la procédure reste la même lorsque l'on récupère un fichier depuis un serveur distant.

Nous allons utiliser `fetch` pour faire l'appel API.

```javascript
fetch("http://localhost:3000/data.json")
  .then(res => {
      return res.json();
  })
  .then(data => {
      // Stocker les données dans l'état
  })
```

Maintenant, ayons un état pour stocker les données et les rendre.

```javascript
const [data, setData] = useState([])
```

```html
<div>
    {data.map(item => (
        <div>
            {item.name}
        </div>
    ))}
</div>
```

Comment écrivons-nous le test pour cela ? Une façon est de mock la méthode `fetch` et de fournir notre propre implémentation mock. Mais que se passe-t-il s'il y a plusieurs appels API Fetch dans le composant ? Vous ne pouvez pas avoir la même implémentation mock pour tout le monde.

Donc, nous mettons l'appel `fetch` dans une fonction séparée et avons une implémentation mock de cette fonction. Nous mettons notre appel API dans une méthode `FetchData` qui retourne la promesse retournée par `fetch`.

Nous mettons la méthode dans un fichier `Services.js` séparé et l'exportons depuis là.

```javascript
export const FetchData = () => {
    return fetch("http://localhost:3000/data.json")
        .then(res => {
            return res.json();
        }) 
}
```

Maintenant, lorsque nous appelons cette méthode à l'intérieur de notre composant, cela ressemble à ceci :

```javascript
const [data, setData] = useState([])

useEffect(() => {
    FetchData().then(data => {
        setData(data);
    })
})

return (
  <div>
      {data.map(item => (
          <div>
              {item.name}
          </div>
      ))}
  </div>
)
```

Maintenant, écrivons le test pour cela. La chose principale est de mock la méthode FetchData. Tout d'abord, importez toutes les méthodes de `Services.js` en tant que module.

```python
import * as services from '../utils/Services'
```

Mockons notre fonction en utilisant `jest.spyOn()`. La méthode prend deux arguments, l'objet et le nom de la méthode sous forme de chaîne.

```python
const mockFetchData = jest.spyOn(services, 'FetchData')
        .mockImplementation(async () => {
            return [{
                name: 'kunal'
            }];
        })
```

`spyOn` crée un mock vide de la méthode. Maintenant, nous fournissons notre implémentation mock où nous retournons des données mock. Cela sera appelé lorsque notre composant se rendra.

```python
render(<TestingAPICalls/>)
expect(mockFetchData).toHaveBeenCalled();
```

Nous utilisons `toHaveBeenCalled()` pour tester si la méthode a été appelée. Elle l'a été – donc le test passe. Maintenant, pour tester le comportement de notre composant, testons si le nom a été rendu.

```javascript
expect(screen.getByText(/kunal/i)).toBeInTheDocument();
```

Dans ce cas, le test échoue car il est incapable de trouver l'élément. Pourquoi en est-il ainsi ?

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-144.png align="left")

*Test échoué : Impossible de trouver l'élément*

Puisque les appels API et les mises à jour d'état sont asynchrones, le texte n'a pas encore été rendu. Pour tester le comportement asynchrone, enveloppez la requête dans un bloc `waitFor()`.

```javascript
await waitFor(() => {
    expect(screen.getByText(/kunal/i)).toBeInTheDocument();
})
```

`waitFor` fait exactement ce que le nom suggère. Il attend que le comportement asynchrone se termine avant de faire la requête. Maintenant, notre test passe avec une couverture de 100 %.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-145.png align="left")

*100 % de couverture pour les tests d'appels API*

Vous pouvez trouver le code complet sur [GitHub](https://github.com/KunalN25/react-testing-basics).

## Conclusion

Ouf ! C'était long. Mais il fallait l'être. J'ai expliqué, à travers des exemples de base, comment vous pouvez commencer à écrire des tests dans React.

Cet article a commencé par un test de base avec une assertion simple et a expliqué comment utiliser des données mock pour servir le but de votre test.

J'ai également expliqué comment simuler des interactions utilisateur, comment tester le comportement d'un composant lors des mises à jour d'état, et enfin comment tester les appels API. Espérons que tous ces exemples vous aident à écrire des tests pour votre prochain projet.

Si vous n'êtes pas en mesure de comprendre le contenu ou trouvez l'explication insatisfaisante, veuillez me le faire savoir. Les nouvelles idées sont toujours appréciées ! N'hésitez pas à me DM sur [LinkedIn](https://www.linkedin.com/in/kunalnk25/) si vous voulez discuter de quoi que ce soit. En attendant, au revoir !