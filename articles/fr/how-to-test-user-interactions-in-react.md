---
title: Comment tester les interactions utilisateur avec la React Testing Library
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2023-02-20T19:12:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-test-user-interactions-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/0_cba5BsaMWpgBXzGK.jpeg
tags:
- name: React
  slug: react
- name: Software Testing
  slug: software-testing
- name: Testing
  slug: testing
seo_title: Comment tester les interactions utilisateur avec la React Testing Library
seo_desc: 'When you''re testing different components in React, you’ll need to simulate
  user interactions with various parts of each component.

  In this tutorial, I am going to show you some methods to simulate user interactions
  with different interactive elements...'
---

Lorsque vous testez différents composants dans React, vous devrez simuler des interactions utilisateur avec diverses parties de chaque composant.

Dans ce tutoriel, je vais vous montrer quelques méthodes pour simuler des interactions utilisateur avec différents éléments interactifs.

Avant de commencer, assurez-vous de savoir comment structurer un test dans React et comment écrire des tests simples. Vous pouvez rafraîchir vos connaissances en lisant mon [article précédent](https://www.freecodecamp.org/news/how-to-write-unit-tests-in-react/) sur la façon d'écrire des tests unitaires dans React.

J'ai également un défi pour vous, alors assurez-vous de lire l'article complet.

## Comment installer le projet

Créez votre application React en utilisant la commande `create-react-app testing-user-interactions`. Ensuite, installez la bibliothèque `user-event`.

```python
npm i user-event
```

Je suppose que vous savez comment utiliser cette bibliothèque. Si ce n'est pas le cas, j'ai expliqué son fonctionnement dans mon précédent [tutoriel](https://www.freecodecamp.org/news/how-to-write-unit-tests-in-react/).

En gros, cette bibliothèque dispose de quelques fonctions que vous pouvez utiliser pour simuler un utilisateur. Nous allons passer en revue toutes ces fonctions avec des exemples.

Avant d'écrire vos tests, vous devrez faire les importations suivantes au début de votre suite de tests (le fichier dans lequel vous écrivez tous vos tests).

```javascript
import {render, screen} from '@testing-library/react'
import userEvent from '@testing-library/user-event'
```

Vous devrez également importer le composant que vous allez tester.

Pour chaque test, nous allons simuler des interactions utilisateur et tester comment notre composant se comporte.

## Comment tester les interactions avec l'élément `select`

Dans votre application, vous pouvez avoir des éléments `select` qui permettent à un utilisateur de sélectionner quelque chose dans une liste d'options. Prenons un exemple :

```html
<select id='selectCity'>    
    <option> Mumbai</option>    
    <option> Bangalore</option>    
    <option> Chennai</option>
</select>
```

Normalement, lorsqu'un utilisateur voit un élément `select`, il clique dessus et sélectionne une option. Nous allons simuler exactement le même comportement et tester si notre composant réagit en conséquence. Par exemple, si un utilisateur sélectionne `Chennai`, la valeur affichée doit être la même.

Tout d'abord, voyons comment interroger l'élément. Utilisons `getByRole` pour interroger l'élément. Vous pouvez utiliser le rôle `combobox` pour l'élément ci-dessus.

```javascript
screen.getByRole('combobox')
```

Qu'est-ce qu'un rôle ? Comment savez-vous quel rôle utiliser pour un élément ? Dans React, à des fins de test, il existe un attribut appelé `role` défini pour chaque élément HTML. Cela facilite l'interrogation d'un élément lors des tests.

Maintenant, afin de connaître la valeur de l'attribut role pour chaque élément, vous pouvez vous référer à la liste des rôles [ici](https://www.w3.org/TR/html-aria/#docconformance).

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-18-at-12.37.44-PM.png align="left")

*Un aperçu de la liste des rôles*

Si vous souhaitez interroger un élément d'ancrage contenant un attribut `href`, vous pouvez utiliser le rôle `link`. Il en va de même pour les autres éléments de la liste.

Cependant, ne définissez pas d'attribut de rôle explicite pour votre élément HTML, car il est déjà défini pour vous.

Voyons une autre méthode d'interrogation de l'élément. S'il y a plus d'un élément `select`, vous pouvez utiliser `getByLabelText()`. Pour cela, ajoutez une étiquette, `<label htmlFor="selectCity">Select City</label>` pour l'élément et faites `screen.getByLabelText(/select city/i)`. Vous obtiendrez l'élément.

Maintenant, utilisez la méthode `[selectOptions()](https://testing-library.com/docs/ecosystem-user-event/#selectoptionselement-values-options)` de la bibliothèque pour simuler un utilisateur sélectionnant une option. Elle prend trois arguments : l'élément, la valeur et toute option.

```javascript
userEvent.selectOptions(    
    screen.getByRole('combobox'),    
    'Chennai'
)
```

Ensuite, ajoutez une assertion à la fin de votre test pour vérifier si l'élément a la même valeur que celle sélectionnée par l'utilisateur.

```javascript
expect(screen.getByRole('combobox')).toHaveValue('Chennai')
```

L'utilisateur a sélectionné `Chennai` et notre élément `select` a la même valeur, donc le test passe.

## Comment tester le changement d'état

Maintenant, je vais faire une mise à jour d'état en changeant la valeur de l'élément `select`. Tout d'abord, j'aurai un état appelé `cityName` pour afficher l'option sélectionnée.

```javascript
const [cityName, setCityName] = useState('Mumbai');
```

```html
<h2> Nom de la ville : {cityName} </h2>
```

Ensuite, j'ajouterai un attribut `onChange` avec une méthode qui met à jour l'état.

```javascript
onChange={(e) => { setCityName(e.target.value)}}
```

Pour écrire le test pour cela, suivez le même processus :

```javascript
test("En-tête du nom de la ville rendu", () => {    
    render(<SelectElement/>)    
    userEvent.selectOptions(        
        screen.getByRole('combobox'),        
        'Bangalore'    )    
    expect(screen.getByRole('heading',               
                     { name: /bangalore/i})).toBeInTheDocument();
})
```

Pour interroger l'élément `h2`, utilisez `[getByRole()](https://testing-library.com/docs/queries/byrole/)` avec l'option `name`. L'option `name` ajoute un autre filtre à la requête – au cas où il y aurait plusieurs éléments `h2`.

## Comment tester un événement de survol

Votre application peut avoir des fonctionnalités où un utilisateur peut survoler un élément pour voir certaines informations sous forme d'infobulle. Alors, pour apprendre à tester cela, implémentons une fonctionnalité d'infobulle de base.

```html
<div className="tooltip">    
    <p> Survolez-moi</p>    
    <span className="tooltiptext">Texte de l'infobulle</span>
</div>
```

Il y a aussi quelques styles CSS pour les classes définies ci-dessus, mais je ne les montrerai pas ici. En gros, lorsque l'utilisateur survole le texte *Survolez-moi*, le texte de l'infobulle devient visible.

Pour simuler un utilisateur survolant l'élément de texte, utilisez la méthode `hover()`. Ajoutez une assertion à la fin pour tester si l'infobulle est visible.

```javascript
test("Infobulle visible", () => {    
    render(<HoverEvent/>)
    userEvent.hover(screen.getByText(/survolez-moi/i))          
    expect(screen.getByText(/texte de l'infobulle/i)).toBeInTheDocument()
})
```

Le test passera si l'infobulle est visible au survol. Si ce n'est pas le cas, vous devrez refactoriser votre code.

## Comment tester un événement de téléchargement de fichier

Un autre événement important est celui où un utilisateur télécharge des fichiers sur votre site web. Il s'agit d'une fonctionnalité assez courante dans toute application UI.

Prenons un `input` de type `file`.

```html
<label htmlFor="singleFile">Télécharger un fichier</label>
<input type='file' id='singleFile' />
```

Dans le test, vous devrez simuler l'utilisateur téléchargeant un fichier. Utilisez la méthode `upload()` pour cela :

```javascript
test("Test de téléchargement d'un seul fichier", () => {    
    render(<FileUpload/>)    
    const file = new File(['hello'], 'hello.png', {type: 'image/png'})   
    userEvent.upload(screen.getByLabelText(/télécharger un fichier/i), file)  
    expect(screen.getByLabelText(/télécharger un fichier/i).files[0]).toEqual(file)
})
```

Tout d'abord, créez un fichier mock et téléchargez-le. Ensuite, faites une assertion que le fichier présent dans l'input correspond à notre fichier téléchargé. C'est le cas, donc le test passe.

Maintenant, prenons un exemple de téléchargement de plusieurs fichiers.

```html
<label htmlFor='multipleFiles'>Télécharger plusieurs fichiers</label>
<input type='file' id='multipleFiles' multiple />
```

Dans notre test, téléchargez plusieurs fichiers.

```javascript
test("Test de téléchargement de plusieurs fichiers", () => {    
    render(<FileUpload/>)    
    const files = [        
           new File(['file1'], 'file1.png', {type: 'image/png'}),       
           new File(['file2'], 'file2.png', {type: 'application/pdf'})   
    ]    
    userEvent.upload(screen.getByLabelText(/télécharger plusieurs fichiers/i), 
                        files)    
    const fileInput = screen.getByLabelText(/télécharger plusieurs fichiers/i)  
    
    expect(fileInput.files.length).toBe(2);   
    expect(fileInput.files[0]).toEqual(files[0]);   
    expect(fileInput.files[1]).toEqual(files[1]);
})
```

Dans les assertions, vérifiez le nombre de fichiers et si les deux fichiers correspondent à ceux téléchargés. Ainsi, tous nos tests passent avec une couverture de 100 %.

Maintenant, c'est le moment du défi. Parcourez mes articles sur [Téléchargements de plusieurs fichiers](https://medium.com/gitconnected/how-to-implement-multiple-file-uploads-in-react-4cdcaadd0f6e) et [Différents exemples du hook useState](https://medium.com/gitconnected/4-different-examples-of-the-usestate-hook-in-react-5504ce011a20) et écrivez des tests unitaires pour toutes les fonctionnalités. Téléchargez votre code sur GitHub et partagez-le avec moi.

## Comment tester le comportement des formulaires

Une fonctionnalité importante de la plupart des applications web est la gestion des formulaires. Lors de l'écriture de tests pour une application React, il est très probable que vous deviez tester le comportement de votre composant avec les formulaires.

Dans notre exemple, prenons un formulaire avec deux champs `input`, un champ `select` et un bouton de soumission.

Tout d'abord, définissons les états pour les champs respectifs et un état supplémentaire pour indiquer si le formulaire est soumis.

```javascript
const [name, setName] = useState('')
const [password, setPassword] = useState('')
const [country, setCountry] = useState('')
const [formSubmitted, setFormSubmitted] = useState(false)
```

```html
<form>    
    <input onChange={(e) => {setName(e.target.value)}}             
           placeholder='Entrez le nom'/>    
    <input onChange={(e) => {setPassword(e.target.value)}}                          placeholder='Entrez le mot de passe'/>    
    <label htmlFor='selectCountry'> Sélectionnez le pays </label>    
    <select id='selectCountry'             
            onChange={(e) => {setCountry(e.target.value)}}>       
        <option>Inde</option>        <option>Japon</option>       
        <option>Chine</option>        <option>USA</option>       
        <option>Angleterre</option>    
    </select>    
    <button onClick={handleSubmit}> Soumettre </button>
</form>
```

Dans l'attribut `onChange`, faites les mises à jour d'état. À la fin, affichez un texte lors de la soumission réussie du formulaire.

```html
{formSubmitted && 'Formulaire soumis'}
```

Ajoutons également une validation dans la méthode `handleSubmit`. Lorsqu'une validation échoue, une liste d'erreurs sera affichée. Créez un autre état pour contenir les erreurs.

```javascript
const [errors, setErrors] = useState([])
```

Maintenant, implémentez la méthode `handleSubmit`.

```javascript
const handleSubmit = (event) => {    
    event.preventDefault();    
    const errorList=[];    
    if(name == '' || password == '' || country == '') {        
        errorList.push('Veuillez remplir tous les détails')    
    }        
    const regex = /^[a-z]*$/i;    
    if(!name.match(regex)) {        
        errorList.push('Veuillez entrer un nom valide')    
    }    
    if(errorList.length != 0) {        
        setErrors(errorList);        
        setFormSubmitted(false);        
        return;      
    }     
    setErrors([]);    
    setFormSubmitted(true)
}
```

Tout d'abord, nous allons faire `event.preventDefault()` qui annule tout événement empêchant la soumission du formulaire. Ensuite, nous allons ajouter quelques vérifications d'erreurs et ajouter toute erreur à l'état `errors`. À la fin, s'il n'y a pas d'erreurs, définissez `errors` sur un tableau vide et définissez `formSubmitted` sur `true`.

Nous allons également afficher la liste de toutes les erreurs qui seront visibles en cliquant sur le bouton de soumission.

```javascript
errors.map(err => (    
    <p>        
    	{err}   
    </p>
))
```

Écrivons les tests pour cet exemple. Il y a quelques choses différentes que vous devriez tester. Tout d'abord, écrivez un test simulant un utilisateur interagissant avec le formulaire et le soumettant avec des valeurs correctes.

```javascript
test("Formulaire soumis avec des valeurs d'entrée correctes", () => {
    render(<FormBehaviour/>)

    userEvent.type(screen.getByPlaceholderText(/entrez le nom/i), 'kunal')
    userEvent.type(screen.getByPlaceholderText(/entrez le mot de passe/i),                                   'pass')
    userEvent.selectOptions(screen.getByLabelText(/sélectionnez le pays/i),                               'Inde')
    userEvent.click(screen.getByText(/soumettre/i))

    expect(screen.getByText(/formulaire soumis/i)).toBeInTheDocument();
})
```

Utilisez les méthodes `type` et `click` de la bibliothèque `userEvent` pour simuler les actions respectives. À la fin, ajoutez une assertion pour voir si le texte correspondant à l'expression régulière `/formulaire soumis/i` est visible dans le document, puisque notre logique affiche le texte dès que le formulaire est soumis.

![Image](https://miro.medium.com/max/1400/1*Tb0jZPtQRAJwlrlWpEhUiw.png align="left")

*Couverture de test pour le composant de comportement de formulaire*

Notre test passe, mais il reste encore quelques lignes non couvertes. Nous avons testé le comportement régulier du formulaire. Cependant, nous avons également des mécanismes de gestion des erreurs en place. Vous devez donc également écrire des tests qui couvrent différents scénarios d'erreurs.

Tout d'abord, simulez un utilisateur cliquant sur le bouton de soumission sans rien entrer.

```javascript
test("Erreur de champs vides affichée", () => {    
    render(<FormBehaviour/>)    
    userEvent.click(screen.getByText(/soumettre/i))    
    expect(screen.getByText(/veuillez remplir tous les détails/i))                         .toBeInTheDocument()
})
```

En cliquant sur le bouton de soumission, un message d'erreur doit être visible, invitant l'utilisateur à remplir tous les détails. Faites une assertion pour cela.

Toutes les lignes ne sont pas encore couvertes. Nous avons encore un autre scénario d'erreur. Et si l'utilisateur entre un nom invalide ?

```javascript
test("Erreur de nom invalide affichée", () => {    
    render(<FormBehaviour/>)    
    userEvent.type(screen.getByPlaceholderText(/entrez le nom/i), '@###')       userEvent.type(screen.getByPlaceholderText(/entrez le mot de passe/i),                                    'pass')    
    userEvent.selectOptions(screen.getByLabelText(/sélectionnez le pays/i),                                  'Inde')    
    userEvent.click(screen.getByText(/soumettre/i))    
    expect(screen.getByText(/Veuillez entrer un nom valide/i))
          .toBeInTheDocument();
})
```

Ce test est similaire au premier test, sauf qu'ici, l'utilisateur entre un nom invalide. Donc, vérifiez si l'erreur correspondante est affichée.

![Image](https://miro.medium.com/max/1400/1*QEBA48iEtB15EmuQrs-DTQ.png align="left")

*100 % de couverture pour le composant de comportement de formulaire*

Maintenant, tous nos tests passent avec une couverture de 100 %.

Vous pouvez trouver le code complet sur [GitHub](https://github.com/KunalN25/testing-user-interactions).

## Conclusion

Tester les interactions utilisateur vous aide à vous assurer que les utilisateurs peuvent interagir efficacement et efficacement avec votre application. Vous devez couvrir tous les scénarios possibles qu'un utilisateur peut rencontrer. Dans cet article, je vous ai montré comment vous pouvez simuler des interactions utilisateur avec différents éléments.

J'ai également démontré le test du comportement des formulaires couvrant de nombreux scénarios. J'espère que vous savez maintenant comment utiliser la bibliothèque `userEvent` pour tester le comportement de votre composant avec les événements utilisateur.

Si vous ne comprenez pas le contenu ou trouvez l'explication insatisfaisante, contactez-moi et faites-le-moi savoir. Les nouvelles idées sont toujours appréciées ! N'hésitez pas à me contacter sur Twitter. En attendant, au revoir !