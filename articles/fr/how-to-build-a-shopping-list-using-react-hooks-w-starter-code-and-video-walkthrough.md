---
title: Comment créer une liste de courses avec React Hooks (avec code de départ et
  tutoriel vidéo)
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2020-10-12T20:16:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-shopping-list-using-react-hooks-w-starter-code-and-video-walkthrough
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/Copy-of-Build-a-Temperature-control-App--2-.png
tags:
- name: projects
  slug: projects
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: Web Development
  slug: web-development
seo_title: Comment créer une liste de courses avec React Hooks (avec code de départ
  et tutoriel vidéo)
seo_desc: "What we're building\nIn this beginner React tutorial, we're going to build\
  \ a shopping app. We'll work with complex state objects, update parts of the state,\
  \ and use existing state to calculate new state. \nCheck it out here:\n\nTry it\
  \ yourself\nIf you wan..."
---

## Ce que nous construisons

Dans ce tutoriel React pour débutants, nous allons créer une application de liste de courses. Nous travaillerons avec des objets d'état complexes, mettrons à jour des parties de l'état et utiliserons l'état existant pour calculer un nouvel état.

Découvrez-le ici :

![](https://jschris.com/41168097024a0b0e7b306a91023114b8/project.gif)

## Essayez par vous-même

Si vous souhaitez essayer par vous-même d'abord, voici les scénarios (vous pouvez également récupérer le code de départ ci-dessous) :

- L'utilisateur doit pouvoir ajouter de nouveaux éléments à la liste en tapant dans le champ de saisie et en cliquant sur le symbole "+"
- L'utilisateur doit pouvoir augmenter/diminuer les quantités d'un article particulier
- Le total doit afficher la quantité totale pour tous les articles de la liste

## Tutoriel vidéo

<iframe width="560" height="315" src="https://www.youtube.com/embed/_N6LQd6Y2UY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Code de départ

[Téléchargez-le sur GitHub ici](https://github.com/chrisblakely01/simple-shopping-list)

## Comment afficher une liste d'articles

La première chose que nous allons faire est d'afficher une liste d'articles. Si vous travaillez avec le code de départ, vous verrez que j'ai ajouté un objet d'état :

```jsx
const [items, setItems] = useState([]);
```

Nous allons l'initialiser avec un tableau d'objets. Nous utiliserons ensuite la fonction map pour parcourir cette liste et afficher les articles.

Remplacez la ligne ci-dessus par ce qui suit :

```jsx
const [items, setItems] = useState([
	{ itemName: 'article 1', quantity: 1, isSelected: false },
	{ itemName: 'article 2', quantity: 3, isSelected: true },
	{ itemName: 'article 3', quantity: 2, isSelected: false },
]);
```

Vous remarquerez que chaque article du tableau est un **objet**. Cet objet représente chaque article (ou ligne) et contient les éléments dont nous avons besoin pour l'affichage :

- Le nom de l'article
- La quantité
- Un indicateur que nous utiliserons pour afficher une "coche" ou un "cercle vide"

> La raison pour laquelle nous plaçons cette liste dans l'état sous forme de tableau est que la liste changera. Lorsque nous voulons modifier la liste, nous ajoutons simplement des éléments ou les supprimons du tableau et React mettra automatiquement à jour l'interface utilisateur pour nous.

D'accord, maintenant nous devons simplement ajouter une fonction map à notre JSX et parcourir ce tableau et afficher les propriétés sur l'interface utilisateur.

Remplacez la **div de la liste d'articles** par ce qui suit :

```jsx
<div className='item-list'>
	{items.map((item, index) => (
		<div className='item-container'>
			<div className='item-name'>
				{item.isSelected ? (
					<>
						<FontAwesomeIcon icon={faCheckCircle} />
						<span className='completed'>{item.itemName}</span>
					</>
				) : (
					<>
						<FontAwesomeIcon icon={faCircle} />
						<span>{item.itemName}</span>
					</>
				)}
			</div>
			<div className='quantity'>
				<button>
					<FontAwesomeIcon icon={faChevronLeft} />
				</button>
				<span> {item.quantity} </span>
				<button>
					<FontAwesomeIcon icon={faChevronRight} />
				</button>
			</div>
		</div>
	))}
</div>
```

Passons cela en revue.

- Nous avons introduit la fonction map. Elle parcourra les articles du tableau **items** et affichera un ensemble de JSX pour chaque **article**. N'oubliez pas que la fonction map nous donne **l'objet actuel sur lequel elle se trouve comme variable**, afin que nous puissions accéder à ses propriétés.

- Nous utilisons un ternaire pour vérifier la variable **item.isSelected**. Si la variable est vraie, nous affichons une "coche" avec un texte barré. Si la valeur est fausse, nous affichons un "cercle vide" ainsi que le nom de l'article.

- Nous affichons également la quantité pour cet article particulier.

## Comment stocker ce que l'utilisateur tape dans l'état

Maintenant que nous avons quelques articles affichés, nous allons permettre à l'utilisateur d'ajouter des articles à la liste. Ce ne serait pas une très bonne liste de courses s'ils ne pouvaient pas ajouter des choses !

Vous verrez dans le code de départ que j'ai inclus une entrée :

```jsx
<div className='add-item-box'>
	<input className='add-item-input' placeholder='Ajouter un article...' />
	<FontAwesomeIcon icon={faPlus} />
</div>
```

Pour l'instant, cela ne fait pas grand-chose. Nous devons donner le contrôle à React afin de pouvoir facilement travailler avec la valeur tapée par l'utilisateur.

Pour ce faire, nous allons créer une nouvelle valeur d'état pour contenir la valeur de ce que l'utilisateur a tapé, et nous allons ajouter un **événement onChange** pour changer cette valeur.

Ajoutez un nouvel objet d'état, et initialisez-le à une chaîne vide :

```jsx
const [inputValue, setInputValue] = useState('');
```

Maintenant, dans le champ de saisie, ajoutez une **valeur** et une fonction **onChange** comme suit :

```jsx
<input value={inputValue} onChange={(event) => setInputValue(event.target.value)} className='add-item-input' placeholder='Ajouter un article...' />
```

Chaque fois que l'utilisateur tape, l'événement **onChange** est appelé. React passe automatiquement l'**événement** pour nous, afin que nous puissions obtenir la valeur tapée par l'utilisateur à partir de celui-ci.

Nous prenons ensuite cette valeur et appelons **setInputValue** pour définir ce que l'utilisateur a tapé dans l'état.

Nous définissons ensuite la valeur du champ de saisie pour qu'elle soit égale à la valeur stockée dans la variable d'état **inputValue**.

## Comment ajouter un nouvel article à la liste

Maintenant, il est logique d'ajouter la valeur tapée par l'utilisateur à la liste. Puisque nous connaissons la liste actuelle et que nous connaissons ce que l'utilisateur a tapé (nous avons tout mis dans l'état !), tout ce que nous avons à faire est de rassembler ces éléments.

En d'autres termes, nous allons ajouter **inputValue** au tableau **items**.

Commencez par créer une nouvelle fonction, qui sera appelée lorsque l'utilisateur clique sur l'icône "+" :

```jsx
const handleAddButtonClick = () => {
	const newItem = {
		itemName: inputValue,
		quantity: 1,
		isSelected: false,
	};

	const newItems = [...items, newItem];

	setItems(newItems);
	setInputValue('');
};
```

Ce que cela fait :

- Crée un nouvel objet appelé **newItem** qui est ce qui est poussé dans le tableau. Nous définissons le **itemName** sur ce que **inputValue** est, nous définissons par défaut la **quantity** sur **1**, et le booléen **isSelected** sur **false**

- Copie le tableau existant (nous faisons cela pour éviter de muter l'état), et ajoute notre **objet newItem** à la fin

- Pousse le nouveau tableau dans l'état

- Enfin, réinitialise le **inputValue** à une chaîne vide afin que l'utilisateur puisse taper et ajouter plus de choses

Maintenant que nous avons une fonction, nous devons simplement la connecter à notre bouton :

```jsx
<FontAwesomeIcon icon={faPlus} onClick={() => handleAddButtonClick()} />
```

Si vous exécutez le code, tapez des choses dans le champ de saisie et cliquez sur l'icône "plus", cela devrait être ajouté à la liste. Hourra !

## Comment basculer un article

Maintenant, nous allons voir comment nous pouvons basculer un article pour indiquer qu'il a été sélectionné. Nous savons que chaque article du tableau/liste a une variable **_isSelected_**, donc tout ce que nous avons à faire est de mettre à jour cela lorsqu'un article est cliqué.

Créez une nouvelle fonction comme suit :

```jsx
const toggleComplete = (index) => {
	const newItems = [...items];

	newItems[index].isSelected = !newItems[index].isSelected;

	setItems(newItems);
};
```

Cela prend un **index** comme paramètre. L'index nous est donné par la fonction map et indique la _position_ dans le tableau où nous nous trouvons actuellement.

Nous utilisons ensuite cet index pour obtenir l'objet du tableau et définir la variable **isSelected** à l'opposé de ce qu'elle est actuellement.

Nous mettons ensuite les articles mis à jour dans l'état. Cela provoque le rerendu du composant par React et affiche soit un "cercle coché" soit un "cercle vide" pour chaque article en fonction de ce drapeau (rappelez-vous que nous avons écrit la logique ternaire pour cela plus tôt).

Pour que tout cela fonctionne, nous devons simplement appeler **toggleComplete** lorsque l'utilisateur clique sur le cercle :

Mettez à jour la **div itemName** comme suit :

```jsx
<div className='item-name' onClick={() => toggleComplete(index)}>
	// ...autre code
</div>
```

Notez que nous passons l'index que nous obtenons de la fonction map. Cela nous indique la position actuelle dans le tableau où nous nous trouvons.

Exécutez le code et vous devriez pouvoir "sélectionner" un article. Succès !

## Comment mettre à jour les quantités

Nous allons adopter une approche similaire pour mettre à jour les quantités. Nous commencerons par l'augmentation de la quantité. Ajoutez une fonction comme suit :

```jsx
const handleQuantityIncrease = (index) => {
	const newItems = [...items];

	newItems[index].quantity++;

	setItems(newItems);
};
```

Vous remarquerez que cela est similaire à la fonction **toggleComplete** :

- Nous utilisons l'index pour obtenir l'article/objet du tableau
- Nous augmentons la quantité
- Nous remettons tout dans l'état

Maintenant, nous devons simplement mettre à jour notre bouton pour appeler cette fonction :

```jsx
<button>
	<FontAwesomeIcon icon={faChevronRight} onClick={() => handleQuantityIncrease(index)} />
</button>
```

Essayez cela, et vous devriez pouvoir cliquer sur le "chevron droit" et la quantité devrait augmenter.

La gestion de la **diminution de la quantité** sera similaire. Créez une fonction comme suit :

```jsx
const handleQuantityDecrease = (index) => {
	const newItems = [...items];

	newItems[index].quantity--;

	setItems(newItems);
};
```

Ce que nous faisons :

- Nous utilisons l'index pour obtenir l'article/objet du tableau
- Nous diminuons la quantité
- Nous remettons tout dans l'état

## Comment calculer la quantité totale

D'accord, notre application a l'air bien. La dernière chose que nous devons faire est de mettre à jour la quantité totale en bas.

La première chose que nous allons faire est de créer une valeur d'état. Cela sera utilisé pour contenir/afficher les quantités totales :

```jsx
const [totalItemCount, setTotalItemCount] = useState(6);
```

Nous allons le définir par défaut sur **6** car c'est ce que les quantités de la liste initiale ajoutent.

Ensuite, nous allons le rendre dans notre JSX :

```jsx
<div className='total'>Total : {totalItemCount}</div>
```

Tout aura l'air identique jusqu'à présent. C'est parce que nous n'avons pas encore écrit de logique pour mettre à jour l'état. Nous allons créer une nouvelle fonction :

```jsx
const calculateTotal = () => {
	const totalItemCount = items.reduce((total, item) => {
		return total + item.quantity;
	}, 0);

	setTotalItemCount(totalItemCount);
};
```

Cela utilise la fonction **reduce** pour additionner toutes les quantités dans notre tableau d'articles.

Enfin, tout ce que nous avons à faire est d'appeler cette fonction chaque fois que l'utilisateur augmente/diminue la quantité ou ajoute un nouvel article. Mettez à jour les fonctions respectives comme suit :

```jsx
	const handleAddButtonClick = () => {
    // ...autre code
		calculateTotal();
	};

	const handleQuantityIncrease = (index) => {
    // ...autre code
		calculateTotal();
	};

	const handleQuantityDecrease = (index) => {
    // ...autre code
		calculateTotal();
	};
```

Allez-y et essayez d'augmenter/diminuer les quantités. Vous remarquerez que la quantité totale change également !

## Vous voulez plus d'idées de projets ?

Pourquoi ne pas essayer de construire des projets React pour booster votre apprentissage encore plus ?

Chaque semaine, j'envoie un nouveau projet pour que vous puissiez essayer un exemple de travail, un code de départ et des conseils. [Abonnez-vous pour recevoir cela directement dans votre boîte de réception !](https://subscribe.jschris.com)