---
title: Comment utiliser la récursion dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-09T18:55:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-recursion-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/How-to-Build-a-Weather-Application-using-React--39-.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Recursion
  slug: recursion
seo_title: Comment utiliser la récursion dans React
seo_desc: "By Nishant Kumar\nSometimes you'll need to print records from an array,\
  \ but the array is too big and nested. \nLet's say we have a family tree, or a folder\
  \ structure. We have multiple arrays nested inside arrays, and it goes on and on.\
  \ It's so big and ..."
---

Par Nishant Kumar

Parfois, vous devrez imprimer des enregistrements à partir d'un tableau, mais le tableau est trop grand et imbriqué. 

Disons que nous avons un arbre généalogique, ou une structure de dossiers. Nous avons plusieurs tableaux imbriqués à l'intérieur de tableaux, et cela continue ainsi. Il est si grand et profond qu'il n'est pas possible de mapper chaque tableau enfant à l'intérieur de son parent.

Cela ressemble à quelque chose comme ceci :

```
export const familyTree = {
  // Grand-père
  name: "John",
  age: 90,
  children: [
    {
      name: "Mary",
      age: 60,
    },
    {
      name: "Arthur",
      age: 60,
      children: [
        {
          name: "Lily",
          age: 35,
          children: [
            {
              name: "Hank",
              age: 60,
            },
            {
              name: "Henry",
              age: 57,
            },
          ],
        },
        {
          name: "Billy",
          age: 37,
        },
      ],
    },
    {
      name: "Dolores",
      age: 55,
    },
  ],
};

```

Dans l'exemple ci-dessus, nous avons un arbre généalogique. Si le parent a des enfants, ils seront à l'intérieur d'un tableau appelé **Children**. Si cet **Enfant** a des **Enfants**, ils seront à l'intérieur de leur tableau **Children**.

Cet exemple est un peu simple, mais disons que nous avons beaucoup, beaucoup de membres de la famille. Peut-être même tellement qu'il est difficile de les compter. 

Dans ce cas, pour représenter notre arbre généalogique efficacement, nous utiliserons quelque chose appelé **Récursion**. La récursion signifie simplement appeler la même fonction à l'intérieur d'elle-même, ou rendre un composant à l'intérieur du même composant.

Ce qui se passera, c'est que la fonction ou le composant sera appelé tant que nous avons les données. Alors, essayons d'implémenter la **Récursion** dans ce cas.

## Voici à quoi ressemble le code sans récursion

Donc, nous avons les données, comme vous pouvez le voir ci-dessus. Imprimons tous les noms des membres de la famille dans notre UI.

Créez un composant appelé **Family.** 

```
import "./App.css";
import { familyTree } from "./data";
import Family from "./Family";

function App() {
  return (
    <div>
      <Family familyTree={familyTree} />
    </div>
  );
}

export default App;

```

Nous importons également le tableau qui est **familyTree**. Ensuite, nous passons les données en tant que **familyTree** dans le composant **Family** en tant que props.

Maintenant, dans le composant Family, recevons les props et déstructurons-les.

```
import React from "react";

export default function Family({ familyTree }) {
  return <div style={{ paddingLeft: 10 }}></div>;
}

```

Maintenant, nous allons créer une fonction qui développera l'arbre généalogique en cliquant sur le nom du parent. Nous allons également créer un état qui basculera sa valeur lorsque la fonction s'exécutera.

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return <div style={{ paddingLeft: 10 }}></div>;
}

```

Maintenant, mappons le tableau familyTree et extrayons les données.

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div style={{ paddingLeft: 10 }}>
      <span>{familyTree.name}</span>
      {familyTree.children.map((child) => {
        return (
          <div style={{ paddingLeft: 10 }}>
            <span>{child.name}</span>
          </div>
        );
      })}
    </div>
  );
}

```

Nous mappons également le premier tableau (qui est à l'intérieur du tableau children) à l'intérieur du parent **John**. Cela signifie essentiellement que tous les enfants de **John** seront imprimés.

Maintenant, ajoutons le déclencheur de la fonction. Si nous cliquons sur le nom du parent, disons **John**, la fonction **expand** s'exécutera et basculera la valeur de l'état **isVisible**.

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div style={{ paddingLeft: 10 }}>
      <span onClick={expand}>{familyTree.name}</span>
      {familyTree.children.map((child) => {
        return (
          <div style={{ paddingLeft: 10 }}>
            <span>{child.name}</span>
          </div>
        );
      })}
    </div>
  );
}

```

Maintenant, cachons les valeurs du tableau mappé, et ne les affichons que lorsque **isVisible** est vrai.

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div style={{ paddingLeft: 10 }}>
      <span onClick={expand}>{familyTree.name}</span>
      {isVisible ? (
        familyTree.children.map((child) => {
          return (
            <div style={{ paddingLeft: 10 }}>
              <span>{child.name}</span>
            </div>
          );
        })
      ) : (
        <></>
      )}
    </div>
  );
}

```

Si vous cliquez sur le nom du parent, il basculera leurs enfants et affichera ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-06-223357.png)

Maintenant, disons que Mary a des enfants, ou Arthur a des enfants. Et leurs enfants ont des enfants, et ainsi de suite. Nous pouvons mapper chaque tableau à l'intérieur d'un tableau pour obtenir tout l'arbre généalogique dans la liste. Le code ressemblera à quelque chose comme ceci. 

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };

  return (
    <div style={{ paddingLeft: 10 }}>
      <span onClick={expand}>{familyTree.name}</span>

      {isVisible ? (
        familyTree?.children?.map((child) => {
          return (
            <div style={{ paddingLeft: 10 }}>
              <span onClick={expand}>{child.name}</span>
              {child?.children?.map((subChild) => {
                return (
                  <div style={{ paddingLeft: 10 }}>
                    <span onClick={expand}>{subChild?.name}</span>
                    {subChild.children?.map((subChildInner) => {
                      return (
                        <div style={{ paddingLeft: 10 }}>
                          <span onClick={expand}>{subChildInner?.name}</span>
                          {subChildInner.children?.map((subChildInner2) => {
                            return (
                              <div>
                                <span>{subChildInner2.name}</span>
                              </div>
                            );
                          })}
                        </div>
                      );
                    })}
                  </div>
                );
              })}
            </div>
          );
        })
      ) : (
        <></>
      )}
    </div>
  );
}

```

Et le résultat sera ceci.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-09-233108.png)

Mais nous ne pouvons pas simplement continuer à mapper chaque tableau enfant qui est à l'intérieur de leur tableau parent. L'ensemble du code peut sembler laid et le processus peut devenir chaotique. 

C'est si confus que j'ai été bloqué ici aussi pendant un certain temps. 

Dans ce cas, nous utiliserons la **Récursion**. Alors, implémentons-la.

## Comment utiliser la récursion à la place

Maintenant, faisons la même chose en utilisant la récursion. Notre code sera beaucoup plus propre maintenant.

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div style={{ paddingLeft: 10 }}>
      <span onClick={expand}>{familyTree.name}</span>
      {isVisible ? (
        familyTree.children.map((child) => {
          return (
            <div style={{ paddingLeft: 10 }}>
              <span>{child.name}</span> *
            </div>
          );
        })
      ) : (
        <></>
      )}
    </div>
  );
}

```

Donc, à la place de la balise **span** (à l'endroit où nous imprimons le nom de l'enfant à partir du tableau parent de premier niveau), nous appellerons à nouveau le composant **Family**. 

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div style={{ paddingLeft: 10 }}>
      <span onClick={expand}>{familyTree.name}</span>
      {isVisible ? (
        familyTree.children.map((child) => {
          return (
            <div style={{ paddingLeft: 10 }}>
              <Family />
            </div>
          );
        })
      ) : (
        <></>
      )}
    </div>
  );
}

```

Tout simplement comme ceci. Mais vous verrez que le composant **Family** reçoit une prop, qui est **familyTree.** Nous devons également la passer. 

Alors, que pouvons-nous passer qui satisfera la valeur de la prop **familyTree** ?

Ouvrez et regardez le tableau où nous obtenons nos données. Nous avons un niveau supérieur là, qui est **John**. Maintenant, nous mappons le tableau Children à l'intérieur de John, ce qui nous donne ses trois enfants, et nous les affichons dans notre UI.

Maintenant, si vous cliquez sur **Mary**, il affichera les enfants à l'intérieur de **Mary**, car Mary est maintenant le parent. 

Donc, pour aller plus loin dans le tableau, nous devons passer l'**enfant** du tableau lorsque nous l'avons mappé, en tant que prop familyTree.

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div style={{ paddingLeft: 10 }}>
      <span onClick={expand}>{familyTree.name}</span>
      {isVisible ? (
        familyTree.children.map((child) => {
          return (
            <div style={{ paddingLeft: 10 }}>
              <Family familyTree={child}/>
            </div>
          );
        })
      ) : (
        <></>
      )}
    </div>
  );
}

```

Tout simplement comme ceci. Assurez-vous que les noms des props sont les mêmes dans les deux endroits.

Mais nous rencontrerons un problème dès que nous cliquerons sur **Mary**. Parce que Mary n'a pas d'enfants et pas de tableau d'enfants à l'intérieur. Donc, nous ne pouvons pas mapper un tableau vide ou un tableau qui n'existe pas. Nous obtiendrons une erreur et la page deviendra blanche.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-06-224638.png)

Donc, nous devons sauter ceux qui n'ont pas de tableaux d'enfants à l'intérieur. 

Une façon simple de le faire est d'utiliser un point d'interrogation ('?'). Cela est connu sous le nom de Chaînage Optionnel. Si la valeur ou une propriété est indéfinie, elle la sautera. [Lisez plus sur le Chaînage Optionnel dans cet article](https://www.freecodecamp.org/news/how-the-question-mark-works-in-javascript/).

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div style={{ paddingLeft: 10 }}>
      <span onClick={expand}>{familyTree.name}</span>
      {isVisible ? (
        familyTree?.children?.map((child) => {
          return (
            <div style={{ paddingLeft: 10 }}>
              <Family familyTree={child} />
            </div>
          );
        })
      ) : (
        <></>
      )}
    </div>
  );
}

```

Donc, nous avons ajouté un point d'interrogation lorsque nous mappons le tableau. Si nous cliquons sur le parent sans enfants, nous n'aurons pas d'erreurs.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-06-225211.png)

Et nous pouvons afficher tout l'arbre généalogique comme ceci. Si le parent a un enfant, il se développera. Si le parent n'a pas d'enfants, il ne fera rien.

Et c'est ainsi que nous implémentons la **Récursion dans React.**

## Conclusion

Permettez-moi de répéter ce que nous faisons. Nous mappons simplement un tableau avec des enfants à l'intérieur, et certains de ces enfants ont des sous-enfants, et cela peut continuer.

Donc, nous avons utilisé la **récursion** pour automatiser le processus de mappage du tableau par lui-même. Nous appelons simplement le même composant Family à l'intérieur lorsqu nous mappons le tableau afin qu'il s'appelle lui-même et imprime tout à nouveau. Cela continuera jusqu'à ce qu'il ne reste plus rien, ou un tableau vide.

C'est la puissance de la récursion.

Si vous voulez voir la version vidéo de ceci, visitez ma vidéo sur [Recursion in React](https://youtu.be/1Qq_0rJUEos) sur ma chaîne [Cybernatico](https://www.youtube.com/c/CybernaticoByNishant).

Consultez également le code sur [Github](https://github.com/nishant-666/React-Interview-Questions/tree/master/recursion-in-react) si vous le souhaitez.

Merci d'avoir lu. Que Dieu vous bénisse.