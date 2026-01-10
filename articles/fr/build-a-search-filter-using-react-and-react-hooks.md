---
title: Comment créer un filtre de recherche avec React et React Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-17T17:56:15.000Z'
originalURL: https://freecodecamp.org/news/build-a-search-filter-using-react-and-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/How-to-Build-a-Weather-Application-using-React--23-.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: search
  slug: search
seo_title: Comment créer un filtre de recherche avec React et React Hooks
seo_desc: 'By Nishant Kumar

  When you send a GET request to an API, you get the response data back from the server.
  But sometimes managing this data can be a problem.

  In this blog post, I will show you how to create a search filter in React. It will
  search for a...'
---

Par Nishant Kumar

Lorsque vous envoyez une requête GET à une API, vous recevez les données de réponse du serveur. Mais parfois, la gestion de ces données peut poser problème.

Dans cet article, je vais vous montrer comment créer un filtre de recherche dans React. Il recherchera un terme particulier dans les données en utilisant des composants fonctionnels et des hooks React.

## Comment faire une requête GET à une API

Tout d'abord, faisons une requête GET à une API qui récupérera des données du serveur. Vous pouvez utiliser n'importe quel serveur pour obtenir les données, mais dans cet article, j'utiliserai {JSON} Placeholder pour récupérer la liste des utilisateurs.

Dans cet exemple, nous avons des cartes qui affichent les noms et les emails de différents utilisateurs. Nous avons également une boîte de recherche que nous utiliserons pour rechercher un utilisateur particulier.

```
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card, Input } from 'semantic-ui-react'
export default function Posts() {
    const [APIData, setAPIData] = useState([])
    useEffect(() => {
        axios.get(`https://jsonplaceholder.typicode.com/users`)
            .then((response) => {
                setAPIData(response.data);
            })
    }, [])

    return (
        <div style={{ padding: 20 }}>
            <Input icon='search'
                placeholder='Rechercher...'
            />
            <Card.Group itemsPerRow={3} style={{ marginTop: 20 }}>
                {APIData.map((item) => {
                    return (
                        <Card>
                            <Card.Content>
                                <Card.Header>{item.name}</Card.Header>
                                <Card.Description>
                                    {item.email}
                                </Card.Description>
                            </Card.Content>
                        </Card>
                    )
                })}
            </Card.Group>
        </div>
    )
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-14-202008.png)
_Obtenir la liste des utilisateurs et une entrée de recherche en haut_

Et si vous ne savez pas comment gérer les appels d'API GET dans React, suivez mon blog sur [les opérations CRUD avec React](https://www.freecodecamp.org/news/how-to-perform-crud-operations-using-react/) ou ma vidéo sur [les opérations CRUD avec React](https://youtu.be/-ZMP8ZladIQ) où je vous montre comment gérer les appels d'API dans React.

## Comment obtenir l'entrée de recherche depuis la boîte de recherche

Maintenant, obtenons notre requête de recherche depuis la boîte de recherche.

Créez un état pour l'entrée de recherche.

```
const [searchInput, setSearchInput] = useState('');
```

Ici, `searchInput` est une chaîne de caractères, et nous utiliserons `setSearchInput` pour définir l'entrée de recherche.

Maintenant, nous allons créer une fonction qui gérera notre fonctionnalité de recherche.

```
const searchItems = () => {
        
}
```

Et liez cette fonction à l'entrée de recherche via l'événement `onChange`.

```
<Input icon='search'
                placeholder='Rechercher...'
                onChange={() => searchItems()}
            />
```

Ainsi, chaque fois que nous tapons quelque chose dans le champ de saisie, `searchItems` s'exécutera.

Maintenant, nous devons passer la valeur de l'entrée à la fonction `searchItems`.

```
<Input icon='search'
                placeholder='Rechercher...'
                onChange={(e) => searchItems(e.target.value)}
            />
```

Ensuite, recevons la requête de recherche dans la fonction et définissons l'état `searchInput` à cette valeur en utilisant `setSearchInput` que nous avons créé précédemment.

```
const searchItems = (searchValue) => {
        setSearchInput(searchValue)
    }
```

Vous pouvez vérifier si cela fonctionne en affichant `searchValue` dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-14-203750.png)

Comme vous pouvez le voir, je tape mon nom ici et il s'affiche dans la console.

## Comment filtrer les éléments en fonction des résultats de recherche

Maintenant, nous allons filtrer nos données API en utilisant la méthode filter.

```
const searchItems = (searchValue) => {
        setSearchInput(searchValue)
        APIData.filter((item) => {
            return Object.values(item).join('').toLowerCase().includes(searchInput.toLowerCase())
        })
    }
```

Dans cette fonction `searchTerm`, vous pouvez voir que nous utilisons la méthode `filter` pour filtrer l'état APIData, qui contient les données provenant du serveur.

Nous utilisons également `Object.values` pour obtenir les valeurs de l'objet item.

Ensuite, nous convertissons les valeurs en une chaîne de caractères en utilisant la méthode `join(' ')`.

Puis, nous changeons ces valeurs de chaîne en minuscules en utilisant la méthode `toLowerCase`.

Et enfin, nous vérifions si cette chaîne inclut notre entrée de recherche que nous avons tapée dans la barre de recherche. Nous la convertissons également en minuscules pour nous assurer que si nous tapons notre terme en majuscules, il convertit la chaîne en minuscules pour rendre la recherche plus efficace.

Ensuite, nous retournons toute la requête.

Maintenant, nous devons définir ce tableau filtré dans une variable.

```
const filteredData = APIData.filter((item) => {
return Object.values(item).join('').toLowerCase().includes(searchInput.toLowerCase())
})
```

Vérifions la fonctionnalité ci-dessus en l'affichant dans la console. Recherchez un nom d'utilisateur et vous verrez que vous obtenez les données pour ce nom d'utilisateur en particulier.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-14-211709.png)
_Obtenir l'élément de recherche dans la console_

Maintenant, nous avons besoin d'un état où nous pouvons stocker les données filtrées. Alors, créons-en un.

```
const [filteredResults, setFilteredResults] = useState([]);
```

Créez un état qui contiendra nos données filtrées.

Ensuite, définissez cet état à `filteredData` dans la fonction `searchItems` en utilisant `setFilteredResults`.

```
const searchItems = (searchValue) => {
        setSearchInput(searchValue)
        const filteredData = APIData.filter((item) => {
            return Object.values(item).join('').toLowerCase().includes(searchInput.toLowerCase())
        })
        setFilteredResults(filteredData)
    }
```

## Comment afficher les résultats filtrés dans l'interface utilisateur

Maintenant, affichons ces résultats filtrés dans notre interface utilisateur principale.

Tout d'abord, nous devons écrire un peu de code qui vérifie si notre entrée de recherche est vide, et si c'est le cas, affiche toutes les données. Sinon, il les filtrera selon l'entrée de recherche.

```
const searchItems = (searchValue) => {
        setSearchInput(searchValue)
        if (searchInput !== '') {
            const filteredData = APIData.filter((item) => {
                return Object.values(item).join('').toLowerCase().includes(searchInput.toLowerCase())
            })
            setFilteredResults(filteredData)
        }
        else{
            setFilteredResults(APIData)
        }
    }
```

Nous avons également besoin de cette vérification dans la partie retour de l'application.

Ainsi, si la longueur du terme de recherche est supérieure à 1, nous afficherons les données filtrées. Sinon, nous afficherons toutes les données qui sont stockées dans l'état des données de l'API.

```
<Card.Group itemsPerRow={3} style={{ marginTop: 20 }}>
                {searchInput.length > 1 ? (
                    filteredResults.map((item) => {
                        return (
                            <Card>
                                <Card.Content>
                                    <Card.Header>{item.name}</Card.Header>
                                    <Card.Description>
                                        {item.email}
                                    </Card.Description>
                                </Card.Content>
                            </Card>
                        )
                    })
                ) : (
                    APIData.map((item) => {
                        return (
                            <Card>
                                <Card.Content>
                                    <Card.Header>{item.name}</Card.Header>
                                    <Card.Description>
                                        {item.email}
                                    </Card.Description>
                                </Card.Content>
                            </Card>
                        )
                    })
                )}
            </Card.Group>
```

Maintenant, si nous recherchons un nom d'utilisateur dans le champ de recherche, nous obtiendrons les données de cet utilisateur spécifique.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-14-212917.png)
_Obtenir les résultats de l'entrée de recherche dans l'interface utilisateur_

Et si nous supprimons le nom, nous obtiendrons toutes les données.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-14-213037.png)
_Obtenir toutes les données si l'entrée de recherche est vide_

Voici tout le code pour référence :

```
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card, Input } from 'semantic-ui-react'
export default function Posts() {
    const [APIData, setAPIData] = useState([])
    const [filteredResults, setFilteredResults] = useState([]);
    const [searchInput, setSearchInput] = useState('');
    useEffect(() => {
        axios.get(`https://jsonplaceholder.typicode.com/users`)
            .then((response) => {
                setAPIData(response.data);
            })
    }, [])

    const searchItems = (searchValue) => {
        setSearchInput(searchValue)
        if (searchInput !== '') {
            const filteredData = APIData.filter((item) => {
                return Object.values(item).join('').toLowerCase().includes(searchInput.toLowerCase())
            })
            setFilteredResults(filteredData)
        }
        else{
            setFilteredResults(APIData)
        }
    }

    return (
        <div style={{ padding: 20 }}>
            <Input icon='search'
                placeholder='Rechercher...'
                onChange={(e) => searchItems(e.target.value)}
            />
            <Card.Group itemsPerRow={3} style={{ marginTop: 20 }}>
                {searchInput.length > 1 ? (
                    filteredResults.map((item) => {
                        return (
                            <Card>
                                <Card.Content>
                                    <Card.Header>{item.name}</Card.Header>
                                    <Card.Description>
                                        {item.email}
                                    </Card.Description>
                                </Card.Content>
                            </Card>
                        )
                    })
                ) : (
                    APIData.map((item) => {
                        return (
                            <Card>
                                <Card.Content>
                                    <Card.Header>{item.name}</Card.Header>
                                    <Card.Description>
                                        {item.email}
                                    </Card.Description>
                                </Card.Content>
                            </Card>
                        )
                    })
                )}
            </Card.Group>
        </div>
    )
}

```

Et voilà, un filtre de recherche entièrement fonctionnel dans React en utilisant les hooks React.

Nous gérons souvent cette fonctionnalité côté serveur en passant des paramètres de requête de recherche dans le point de terminaison de l'API. Mais il est important de savoir comment le gérer également côté client.

Vous pouvez également consulter ma vidéo YouTube sur [la création d'un filtre de recherche en utilisant React et React Hooks](https://youtu.be/8YsQmvJ9UZE) si vous souhaitez compléter cet article.

> C'est tout pour aujourd'hui. Bon apprentissage.