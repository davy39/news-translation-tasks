---
title: Que sont les modificateurs Solidity ? Explication avec des exemples
subtitle: ''
author: Oduah Chigozie
co_authors: []
series: null
date: '2023-01-06T18:18:52.000Z'
originalURL: https://freecodecamp.org/news/what-are-solidity-modifiers
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/shubham-dhage-UxDU0Gg5pqQ-unsplash.jpg
tags:
- name: clean code
  slug: clean-code
- name: Smart Contracts
  slug: smart-contracts
- name: Solidity
  slug: solidity
seo_title: Que sont les modificateurs Solidity ? Explication avec des exemples
seo_desc: "In this article, we will explore the various ways you can use modifiers\
  \ in Solidity to modify the behavior of functions. \nWe will cover topics such as\
  \ the syntax for defining and using modifiers, the _; symbol, using multiple modifiers\
  \ on a single fu..."
---

Dans cet article, nous allons explorer les différentes façons d'utiliser les modificateurs en Solidity pour modifier le comportement des fonctions. 

Nous aborderons des sujets tels que la syntaxe pour définir et utiliser les modificateurs, le symbole `_;`, l'utilisation de plusieurs modificateurs sur une seule fonction, les modificateurs avec arguments, les modificateurs basés sur des énumérations, les modificateurs hérités et remplacés, ainsi que des exemples de l'utilisation des modificateurs dans des contrats réels. 

À la fin de cet article, vous aurez une compréhension approfondie du fonctionnement des modificateurs et de la manière de les utiliser efficacement dans votre code Solidity.

## Que sont les modificateurs Solidity ?

Un modificateur est un type spécial de fonction que vous utilisez pour modifier le comportement d'autres fonctions. Les modificateurs vous permettent d'ajouter des conditions ou des fonctionnalités supplémentaires à une fonction sans avoir à réécrire toute la fonction.

Pour définir un modificateur, vous utilisez le mot-clé `modifier` suivi du nom du modificateur et de ses paramètres éventuels. 

Voici un exemple de modificateur :

```
modifier onlyOwner {
    require(msg.sender == owner);
    _;
}

```

Dans cet exemple, le modificateur `onlyOwner` n'a pas de paramètres et inclut une instruction `require` qui vérifie que l'expéditeur du message est le propriétaire du contrat. 

Si l'expéditeur du message est le propriétaire du contrat, la fonction sera exécutée. Si l'expéditeur du message n'est pas le propriétaire du contrat, la fonction ne sera pas exécutée.

Pour utiliser un modificateur, attachez-le à une fonction en le plaçant dans la définition de la fonction. Par exemple :

```
function changeOwner(address newOwner) onlyOwner public {
    // corps de la fonction
}

```

Dans cet exemple, la fonction `changeOwner` a le modificateur `onlyOwner` attaché. Cela signifie que pour exécuter la fonction `changeOwner`, l'appelant doit être le propriétaire du contrat. 

Si l'expéditeur du message n'est pas le propriétaire du contrat, l'instruction `require` dans le modificateur `onlyOwner` échouera et la fonction ne sera pas exécutée.

## Comment fonctionne le symbole `_;` ?

Le symbole `_;` est un symbole spécial utilisé dans les modificateurs Solidity pour indiquer la fin du modificateur et le début de la fonction que le modificateur modifie.

Le corps d'un modificateur est composé d'une ou plusieurs instructions utilisées pour modifier le comportement de la fonction, et du symbole `_;`.

Voici le modificateur `onlyOwner` avec le symbole `_;` :

```
modifier onlyOwner {
    require(msg.sender == owner);
    _;
}

```

Sans le symbole `_;`, le compilateur ne saurait pas où insérer le code du modificateur dans la fonction.

## Comment utiliser plusieurs modificateurs sur une fonction

Vous pouvez souhaiter utiliser plusieurs modificateurs sur une seule fonction. Solidity vous permet d'utiliser plus d'un modificateur sur une fonction comme dans l'exemple ci-dessous :

```solidity
contract MyContract{
   address owner;

   modifier ownerChanges {
       _;
       require(msg.sender == owner);
   }

   modifier onlyOwner {
       require(msg.sender == owner);
       _;
   }

   function changeOwner(address newOwner) onlyOwner ownerChanges public {
       owner = newOwner;
   }
}

```

L'ordre dans lequel vous placez vos modificateurs n'a pas d'importance. Lorsque vous appelez la fonction `changeOwner`, la machine virtuelle exécute à la fois `onlyOwner` et `ownerChanges`.

## Comment utiliser des modificateurs avec des arguments

Les modificateurs en Solidity peuvent avoir des arguments de n'importe quel type de données supporté par Solidity. Les modificateurs avec arguments sont définis de la même manière que les modificateurs réguliers, avec l'ajout d'un ou plusieurs paramètres dans la définition de la fonction.

Voici un exemple de syntaxe pour un modificateur avec des arguments réguliers :

```solidity
modifier onlyAllowedUser(address user) {
    require(msg.sender == user);
    _;
}

```

Dans cet exemple, le modificateur `onlyAllowedUser` a un paramètre, `user`, qui est de type `address`. Le modificateur inclut une instruction `require` qui vérifie la valeur du paramètre `user` et ne permet l'exécution de la fonction que si l'expéditeur du message est égal à `user`.

Pour utiliser un modificateur avec des arguments réguliers, vous pouvez l'attacher à une fonction et passer les valeurs appropriées en tant qu'arguments. Par exemple :

```solidity
function updateData(uint id, bytes32 newData, address user) onlyAllowedUser(user) public {
    // corps de la fonction
}

```

Dans cet exemple, la fonction `updateData` a le modificateur `onlyAllowedUser` attaché et prend un paramètre `address` appelé `user`. Lorsque la fonction `updateData` est appelée, la valeur du paramètre `user` est passée au modificateur `onlyAllowedUser`.

## Comment créer un modificateur basé sur une énumération

Une autre façon d'utiliser les modificateurs est de créer un modificateur basé sur une énumération. Les modificateurs basés sur des énumérations permettent de spécifier un ensemble de valeurs prédéfinies qui peuvent être utilisées pour déterminer si une fonction doit être exécutée ou non.

Pour créer un modificateur basé sur une énumération, vous devez d'abord définir un type d'énumération. Un type d'énumération est un type de données spécial qui se compose d'un ensemble de valeurs nommées appelées "membres". Voici un exemple de type d'énumération :

```solidity
enum ActionType {
    CREATE,
    UPDATE,
    DELETE
}

```

Une fois que vous avez défini le type d'énumération, vous pouvez créer un modificateur basé sur une énumération en ajoutant un paramètre du type d'énumération à votre fonction de modificateur. 

La fonction de modificateur doit inclure une instruction requise qui vérifie la valeur du paramètre d'énumération et détermine si la fonction doit être exécutée ou non. Voici un exemple de modificateur basé sur une énumération :

```solidity
modifier onlyAllowedAction(ActionType action) {
    require(action == ActionType.CREATE || action == ActionType.UPDATE);
    _;
}

```

Le modificateur, appelé `onlyAllowedAction`, ne permettra l'exécution de la fonction à laquelle il est attaché que si la valeur du paramètre d'action est soit `ActionType.CREATE` soit `ActionType.UPDATE`. Si la valeur de l'action est autre chose, l'instruction `require` échouera et la fonction ne sera pas exécutée.

Pour utiliser le modificateur basé sur une énumération, vous l'attacheriez à une fonction et passeriez la valeur d'énumération appropriée en tant qu'argument. Par exemple :

```solidity
function updateData(uint id, bytes32 newData, ActionType action) onlyAllowedAction(action) public {
    // corps de la fonction
}

```

Dans cet exemple, la fonction `updateData` ne peut être exécutée que si le paramètre d'action est défini sur `ActionType.CREATE` ou `ActionType.UPDATE`.

## Comment hériter et remplacer des modificateurs

En Solidity, il est possible d'hériter et de remplacer des modificateurs afin de réutiliser du code et de personnaliser le comportement des fonctions.

Pour hériter d'un modificateur, utilisez le mot-clé `is` dans le contrat à partir duquel vous souhaitez hériter le modificateur. Par exemple :

```
contract BaseContract {
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }
}

contract MyContract is BaseContract {
    // les fonctions dans MyContract peuvent utiliser le modificateur onlyOwner
}

```

Dans cet exemple, le contrat `MyContract` hérite du modificateur `onlyOwner` du `BaseContract`. Cela signifie que toute fonction dans `MyContract` peut utiliser le modificateur `onlyOwner`. Le modificateur `onlyOwner` garantit que seul le propriétaire du contrat peut exécuter la fonction à laquelle il est attaché.

Vous pouvez également remplacer un modificateur en définissant une nouvelle version du modificateur dans un contrat qui hérite d'un autre contrat. Pour ce faire, vous pouvez utiliser le même nom pour le modificateur et définir une nouvelle implémentation pour celui-ci. Par exemple :

```
contract BaseContract {
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }
}

contract MyContract is BaseContract {
    // remplacer le modificateur onlyOwner
    modifier onlyOwner {
        require(msg.sender == newOwner);
        _;
    }
}

```

Dans cet exemple, le contrat `MyContract` remplace le modificateur `onlyOwner` du `BaseContract`. Cela signifie que toute fonction dans `MyContract` qui utilise le modificateur `onlyOwner` vérifiera désormais que l'expéditeur du message est égal à la variable `newOwner`, plutôt qu'à la variable `owner`.

Hériter et remplacer des modificateurs peut être un moyen utile de réutiliser du code et de personnaliser le comportement des fonctions dans vos contrats Solidity.

## Conclusion

Les modificateurs en Solidity sont des fonctions spéciales qui modifient le comportement d'autres fonctions. Ils permettent aux développeurs d'ajouter des conditions ou des fonctionnalités supplémentaires sans avoir à réécrire toute la fonction. 

Les modificateurs peuvent avoir des arguments et peuvent être hérités et remplacés pour personnaliser leur comportement, et ils peuvent être utilisés en combinaison avec d'autres modificateurs pour personnaliser davantage le comportement des fonctions.

Les modificateurs basés sur des énumérations permettent aux développeurs de spécifier un ensemble de valeurs prédéfinies pour déterminer si une fonction doit être exécutée ou non. Les modificateurs basés sur l'état utilisent l'état actuel du contrat pour déterminer si une fonction doit être exécutée ou non. 

Les modificateurs peuvent aider les développeurs à écrire un code plus propre et plus modulaire, et faciliter la maintenance et la mise à jour de leurs contrats.

Merci d'avoir lu !