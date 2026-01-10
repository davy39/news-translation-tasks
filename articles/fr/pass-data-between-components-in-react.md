---
title: Comment transmettre des données et des événements entre les composants dans
  React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-08T16:17:32.000Z'
originalURL: https://freecodecamp.org/news/pass-data-between-components-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/Colorful-Animal-Crossing-Icons-Icon-Set-2.png
tags:
- name: components
  slug: components
- name: crud
  slug: crud
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment transmettre des données et des événements entre les composants
  dans React
seo_desc: "By Nishant Kumar\nIf you're trying to implement CRUD operations using API\
  \ endpoints, you might find that it's hard to manage data across multiple components.\n\
  Or maybe you have a modal, but you want to trigger it from a different component.\
  \ \nWrapping y..."
---

Par Nishant Kumar

Si vous essayez de mettre en œuvre des opérations CRUD en utilisant des points de terminaison d'API, vous pourriez constater qu'il est difficile de gérer les données entre plusieurs composants.

Ou peut-être avez-vous une modale, mais vous voulez la déclencher depuis un composant différent.

Comprendre comment aborder ces scénarios peut être difficile.

Dans ce tutoriel, je vais vous montrer comment vous pouvez le faire.

## Comment transmettre des données entre un composant parent et un composant enfant

Tout d'abord, transmettons des données entre un composant parent et un composant enfant.

Tout d'abord, vous devrez créer deux composants, un parent et un enfant.

```
import React from 'react'

export default function Parent() {
  return (
    <div>
      
    </div>
  )
}

```

```
import React from 'react'

export default function Child() {
    return (
        <div>
            
        </div>
    )
}

```

Ensuite, vous importerez le composant enfant dans le composant parent et le retournerez.

```
import React from 'react'
import Child from './Child';

export default function Parent() {
  return (
    <div>
      <Child/>
    </div>
  )
}
```

Ensuite, vous créerez une fonction et un bouton pour déclencher cette fonction. De plus, vous créerez un état en utilisant le Hook _useState_ pour gérer les données.

```
import React from 'react'
import Child from './Child';
import { Button } from 'semantic-ui-react';
import { useState } from 'react';
import './App.css';

export default function Parent() {
  const [data, setData] = useState('');
  
  const parentToChild = () => {
    setData("Ce sont des données du composant parent vers le composant enfant.");
  }
  return (
    <div className="App">
      <Child/>
      
      <div>
        <Button primary onClick={() => parentToChild()}>Cliquer Parent</Button>
      </div>
    </div>
  )
}

```

Comme vous pouvez le voir ici, nous appelons la fonction _parentToChild_ lors du clic sur le bouton _Cliquer Parent_. Lorsque le bouton Cliquer Parent est cliqué, il stockera "Ce sont des données du composant parent vers le composant enfant" dans la variable _data_.

Maintenant, transmettons cet état de données à nos composants enfants. Vous pouvez le faire en utilisant des props.

Transmettez les données en tant que props lorsque vous appelez le composant enfant comme ceci :

```
<Child parentToChild={data}/>
```

Ici, nous transmettons les données dans le composant enfant en tant que _data_.

`data` est la donnée que nous devons transmettre, et `parentToChild` est le nom de la prop.

Ensuite, il est temps de capturer les données dans le composant enfant. Et c'est très simple.

Ici, il peut y avoir deux cas.

Cas 1 : Si vous utilisez un composant fonctionnel, capturez simplement parentToChild dans les paramètres.

```
import React from 'react'

export default function Child({parentToChild}) {
    return (
        <div>
            {parentToChild}
        </div>
    )
}
```

Cas 2 : Si vous avez un composant de classe, utilisez simplement `this.props.parentToChild`.

```
import React, { Component } from 'react'

export default class Child extends Component {
    render() {
        return (
            <div>
                {this.props.parentToChild}
            </div>
        )
    }
}
```

Dans les deux cas, vous obtiendrez les mêmes résultats :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-06-132836.png)

Lorsque nous cliquons sur le bouton `Cliquer Parent`, nous verrons les données s'afficher à l'écran.

```
import React from 'react'
import Child from './Child';
import { Button } from 'semantic-ui-react';
import { useState } from 'react';
import './App.css';

export default function Parent() {
  const [data, setData] = useState('');
  
  const parentToChild = () => {
    setData("Ce sont des données du composant parent vers le composant enfant.");
  }
  return (
    <div className="App">
      <Child parentToChild={data}/>
      
      <div className="child">
        <Button primary onClick={() => parentToChild()}>Cliquer Parent</Button>
      </div>
    </div>
  )
}
```

Ci-dessus, vous verrez le code complet pour le `Composant Parent`.

## Comment transmettre des données entre un composant enfant et un composant parent

Celui-ci est un peu plus délicat.

Tout d'abord, vous devez créer une fonction dans le composant parent appelée `childToParent` et un état vide nommé `data`.

```
const [data, setData] = useState('');

const childToParent = () => {
   
}
```

Ensuite, transmettez la fonction `childToParent` en tant que prop au composant enfant.

```
<Child childToParent={childToParent}/>
```

Maintenant, dans notre composant enfant, acceptez cet appel de fonction en tant que props et attribuez-le à un événement onClick.

De plus, déclarez un état qui contient certaines données sous forme de chaîne ou de nombre.

Transmettez les données dans la fonction `parentToChild` en tant que paramètres.

```
import React from 'react'
import { Button } from 'semantic-ui-react';

export default function Child({childToParent}) {
    const data = "Ce sont des données du composant enfant vers le composant parent."
    return (
        <div>
            <Button primary onClick={() => childToParent(data)}>Cliquer Enfant</Button>
        </div>
    )
}
```

Ensuite, dans le composant parent, acceptez ces données dans la fonction `childToParent` en tant que paramètre. Ensuite, définissez les données en utilisant le hook useState.

```
import './App.css';
import { useState } from 'react';
import Child from './Child';

function Parent() {
  const [data, setData] = useState('');
  
  const childToParent = (childdata) => {
    setData(childdata);
  }

  return (
    <div className="App">
      <div>
        <Child/>
      </div>
    </div>
  );
}

export default Parent;

```

Ensuite, affichez cette variable de données dans la fonction return.

```
import './App.css';
import { useState } from 'react';
import Child from './Child';

function Parent() {
  const [data, setData] = useState('');
  
  const childToParent = (childdata) => {
    setData(childdata);
  }

  return (
    <div className="App">
     {data}
      <div>
        <Child childToParent={childToParent}/>
      </div>
    </div>
  );
}

export default Parent;
```

Les données de l'enfant écraseront les données du parent lorsque le bouton `Cliquer Enfant` sera cliqué.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-06-134803.png)

Maintenant, vous pouvez transmettre des données de **l'Enfant vers le Parent** et du **Parent vers l'Enfant** comme un pro.

### Vous pouvez également transmettre des événements comme onClick ou OnChange

Il suffit d'appeler une méthode d'alerte dans la fonction `childToParent` et de transmettre cette fonction en tant que prop au composant enfant.

```
import './App.css';
import Child from './Child';

function Parent() {
  const childToParent = () => {
    alert("Ceci est une alerte du composant enfant")
  }

  return (
    <div className="App">
      <div className="child">
        <Child childToParent={childToParent}/>
      </div>
    </div>
  );
}

export default Parent;
```

Et dans le composant enfant, acceptez la fonction `childToParent` en tant que prop. Ensuite, attribuez-la à un événement onClick sur un bouton.

```
import React from 'react'
import { Button } from 'semantic-ui-react';

export default function Child({childToParent}) {
    return (
        <div>
            <Button primary onClick={() => childToParent()}>Cliquer Enfant</Button>
        </div>
    )
}
```

Votre fonction dans le composant parent sera appelée lorsque vous cliquerez sur le bouton dans le composant enfant et vous verrez cette alerte :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-06-140405.png)

C'est tout !

Vous pouvez [trouver le code sur Github](https://github.com/nishant-666/Passing-data-in-React) si vous souhaitez expérimenter davantage.

> Eh bien, c'est tout pour aujourd'hui. Bon apprentissage.