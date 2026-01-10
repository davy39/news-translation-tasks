---
title: What Are Solidity Modifiers? Explained with Examples
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
seo_title: null
seo_desc: "In this article, we will explore the various ways you can use modifiers\
  \ in Solidity to modify the behavior of functions. \nWe will cover topics such as\
  \ the syntax for defining and using modifiers, the _; symbol, using multiple modifiers\
  \ on a single fu..."
---

In this article, we will explore the various ways you can use modifiers in Solidity to modify the behavior of functions. 

We will cover topics such as the syntax for defining and using modifiers, the `_;` symbol, using multiple modifiers on a single function, modifiers with arguments, enum-based modifiers, inherited and overridden modifiers, and examples of how to use modifiers in real-world contracts. 

By the end of this article, you will have a deep understanding of how modifiers work and how to use them effectively in your Solidity code.

## What are Solidity Modifiers?

A modifier is a special type of function that you use to modify the behavior of other functions. Modifiers allow you to add extra conditions or functionality to a function without having to rewrite the entire function.

To define a modifier, you use the `modifier` keyword followed by the name of the modifier and any parameters it may have. 

Here is an example for a modifier:

```
modifier onlyOwner {
    require(msg.sender == owner);
    _;
}

```

In this example, the `onlyOwner` modifier has no parameters and includes a `require` statement that checks that the message sender is the contract owner. 

If the message sender is the contract owner, the function will be executed. If the message sender is not the contract owner, the function will not execute.

To use a modifier, attach it to a function by placing it in the function definition. For example:

```
function changeOwner(address newOwner) onlyOwner public {
    // function body
}

```

In this example, the `changeOwner` function has the `onlyOwner` modifier attached to it. This means that in order to execute the `changeOwner` function, the caller must be the contract owner. 

If the message sender is not the contract owner, the `require` statement in the `onlyOwner` modifier will fail and the function will not execute.

## How Does the `_;` Symbol Work?

The `_;` symbol is a special symbol that is used in Solidity modifiers to indicate the end of the modifier and the beginning of the function that the modifier is modifying.

The body of a modifier is made up of one or more statements that are used to modify the behavior of the function, and the `_;` symbol.

Here is the `onlyOwner` modifier with the `_;` symbol:

```
modifier onlyOwner {
    require(msg.sender == owner);
    _;
}

```

Without the `_;` symbol, the compiler would not know where to insert the code from the modifier into the function.

## How to Use Multiple Modifiers on a Function

You may want to use multiple modifiers on a single function. Solidity lets you use more than one modifier on a function as in the example below:

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

The order you place your modifiers in doesn’t matter. When you call the `changeOwner` function, the virtual machine executes both `onlyOwner` and `ownerChanges`.

## How to Use Modifiers with Arguments

Modifiers in Solidity can have arguments of any data type supported by Solidity. Modifiers with arguments are defined in the same way as regular modifiers, with the addition of one or more parameters in the function definition.

Here is an example syntax for a modifier with regular arguments:

```solidity
modifier onlyAllowedUser(address user) {
    require(msg.sender == user);
    _;
}

```

In this example, the `onlyAllowedUser` modifier has one parameter, `user`, which is of type `address`. The modifier includes a `require` statement that checks the value of the `user` parameter and only allows the function to execute if the message sender is equal to `user`.

To use a modifier with regular arguments, you can attach it to a function and pass the appropriate values as arguments. For example:

```solidity
function updateData(uint id, bytes32 newData, address user) onlyAllowedUser(user) public {
    // function body
}

```

In this example, the `updateData` function has the `onlyAllowedUser` modifier attached to it and takes an `address` parameter called `user`. When the `updateData` function is called, the value of the `user` parameter is passed to the `onlyAllowedUser` modifier.

## How to Create an Enum-based Modifier

Another way to use modifiers is to create an enum-based modifier. Enum-based modifiers allow you to specify a set of predefined values that can be used to determine whether or not a function should execute.

To create an enum-based modifier, you first need to define an enum type. An enum type is a special data type that consists of a set of named values called "members". Here is an example enum type:

```solidity
enum ActionType {
    CREATE,
    UPDATE,
    DELETE
}

```

Once you have defined the enum type, you can create an enum-based modifier by adding a parameter of the enum type to your modifier function. 

The modifier function should include a required statement that checks the value of the enum parameter and determines whether or not the function should execute. Here is an example of an enum-based modifier:

```solidity
modifier onlyAllowedAction(ActionType action) {
    require(action == ActionType.CREATE || action == ActionType.UPDATE);
    _;
}

```

The modifier, called `onlyAllowedAction`, will only allow the function to which it is attached to execute if the value of the action parameter is either `ActionType.CREATE` or `ActionType.UPDATE`. If the value of action is anything else, the `require` statement will fail and the function will not execute.

To use the enum-based modifier, you would attach it to a function and pass the appropriate enum value as an argument. For example:

```solidity
function updateData(uint id, bytes32 newData, ActionType action) onlyAllowedAction(action) public {
    // function body
}

```

In this example, the `updateData` function can only be executed if the action parameter is set to either `ActionType.CREATE` or `ActionType.UPDATE`.

## How to Inherit and Override Modifiers

In Solidity, it is possible to inherit and override modifiers in order to reuse code and customize the behavior of functions.

To inherit a modifier, use the `is` keyword in the contract that you want to inherit the modifier from. For example:

```
contract BaseContract {
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }
}

contract MyContract is BaseContract {
    // functions in MyContract can use the onlyOwner modifier
}

```

In this example, the `MyContract` contract inherits the `onlyOwner` modifier from the `BaseContract`. This means that any function in `MyContract` can use the `onlyOwner` modifier. The `onlyOwner` modifier ensures that only the contract owner can execute the function that it is attached to.

You can also override a modifier by defining a new version of the modifier in a contract that inherits from another contract. To do this, you can use the same name for the modifier and define a new implementation for it. For example:

```
contract BaseContract {
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }
}

contract MyContract is BaseContract {
    // override the onlyOwner modifier
    modifier onlyOwner {
        require(msg.sender == newOwner);
        _;
    }
}

```

In this example, the `MyContract` contract overrides the onlyOwner modifier from the `BaseContract`. This means that any function in `MyContract` that uses the `onlyOwner` modifier will now check that the message sender is equal to the `newOwner` variable, rather than the `owner` variable.

Inheriting and overriding modifiers can be a useful way to reuse code and customize the behavior of functions in your Solidity contracts.

## Conclusion

Modifiers in Solidity are special functions that modify the behavior of other functions. They allow developers to add extra conditions or functionality without having to rewrite the entire function. 

Modifiers can have arguments and can be inherited and overridden to customize their behavior, and they can be used in combination with other modifiers to further customize the behavior of functions.

Enum-based modifiers allow developers to specify a set of predefined values to determine whether or not a function should execute. State-based modifiers use the contract's current state to determine whether or not a function should execute. 

Modifiers can help developers write cleaner, more modular code and make it easier to maintain and update their contracts.

Thanks for reading!

