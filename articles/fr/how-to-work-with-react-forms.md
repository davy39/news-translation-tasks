---
title: Comment travailler avec les formulaires React sans se casser la tête
subtitle: ''
author: Oluwadamisi Samuel
co_authors: []
series: null
date: '2025-07-07T13:50:19.234Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-react-forms
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1751502730489/90e30388-3517-457a-8ca0-630f589da914.png
tags:
- name: React
  slug: reactjs
- name: Forms and input elements
  slug: forms-and-input-elements
- name: controlled and uncontrolled components
  slug: controlled-and-uncontrolled-components
- name: Programming Blogs
  slug: programming-blogs
seo_title: Comment travailler avec les formulaires React sans se casser la tête
seo_desc: If you’ve ever built a form in React and felt like the input fields had
  a mind of their own, you’re not alone. One minute your form is working fine, the
  next you’re staring at a blank input that won’t update. Or React throws a warning
  like “A compone...
---

Si vous avez déjà créé un formulaire dans React et que vous avez eu l'impression que les champs de saisie avaient une vie propre, vous n'êtes pas seul. Une minute, votre formulaire fonctionne bien, la suivante, vous regardez un champ de saisie vide qui ne se met pas à jour. Ou React affiche un avertissement comme « Un composant change une entrée non contrôlée de type texte pour la contrôler. » et vous n'êtes même pas sûr de ce que cela signifie.

Je ne l'ai pas vraiment compris non plus jusqu'à ce que je réalise que React ne se contente pas de lire les entrées de formulaire – il peut les « posséder ». Et que vous laissiez React contrôler vos entrées ou que vous laissiez le `DOM` les gérer fait une réelle différence dans le comportement de votre formulaire.

Dans cet article, je vais décomposer :

* Ce que sont les composants contrôlés et non contrôlés
  
* Pourquoi la différence est importante
  
* Quand utiliser chacun
  
* Et comment éviter les erreurs courantes des débutants
  

Vous obtiendrez du code réel, des exemples clairs et un guide sans détours pour faire en sorte que les formulaires React se comportent exactement comme vous le souhaitez.

### Voici ce que nous allons couvrir :

* [Qu'est-ce qu'un composant contrôlé ?](#heading-qu-est-ce-qu-un-composant-controle)
  
* [Qu'est-ce qu'un composant non contrôlé ?](#heading-qu-est-ce-qu-un-composant-non-controle)
  
* [Contrôlé vs non contrôlé : quelle est la différence ?](#heading-controle-vs-non-controle-quelle-est-la-difference)
  
* [Quand utiliser les composants contrôlés vs non contrôlés](#heading-quand-utiliser-les-composants-controles-vs-non-controles)
  
  * [Utiliser les composants contrôlés lorsque :](#heading-utiliser-les-composants-controles-lorsque)
      
  * [Utiliser les composants non contrôlés lorsque :](#heading-utiliser-les-composants-non-controles-lorsque)
      
* [Conclusion](#heading-conclusion)
  

## Qu'est-ce qu'un composant contrôlé ?

Un `composant contrôlé` dans React est une entrée (comme une zone de texte ou une liste déroulante) où React suit la valeur.

Au lieu de laisser le navigateur gérer l'entrée seul, vous utilisez l'état React pour indiquer à l'entrée ce qu'elle doit afficher, et vous mettez à jour cet état lorsque l'utilisateur tape. En gros, à chaque frappe, l'état est mis à jour et le composant est réaffiché.


Voici un exemple de base :

```javascript
import { useState } from "react";

function NameForm() {
  const [name, setName] = useState("");

  return (
    <input
      type="text"
      value={name} // Quelle que soit l'état, c'est ce que la valeur du champ de saisie sera
      onChange={(e) => setName(e.target.value)} // Lorsque vous tapez, cette fonction s'exécute et met à jour l'état
    />
  );
}
```

React réaffiche avec la nouvelle valeur, gardant l'interface utilisateur et les données synchronisées. Vous contrôlez toujours ce qu'il y a dans ce champ.

**Pourquoi utiliser cette approche ?**

* Vous connaissez toujours la valeur actuelle.
  
* Il est facile de valider, réinitialiser ou modifier l'entrée depuis le code.
  
* C'est l'approche standard dans la plupart des applications React.
  

## Qu'est-ce qu'un composant non contrôlé ?

Un `composant non contrôlé` est l'opposé de ce que nous venons de voir. Au lieu d'utiliser l'état React pour gérer l'entrée, vous laissez le navigateur le gérer seul, comme un formulaire HTML classique.

Pour obtenir la valeur, vous utilisez ce qu'on appelle une `ref` (abréviation de « référence ») pour accéder au DOM et la récupérer lorsque vous en avez besoin.

Dans React, les `refs` sont créées à l'aide d'un hook intégré appelé `useRef`. Ce hook vous permet de créer une référence à un élément DOM (comme un `<input>`), afin que vous puissiez accéder directement à sa valeur actuelle chaque fois que vous en avez besoin (par exemple, lorsqu'un formulaire est soumis).

Contrairement à `useState`, qui suit les changements et provoque des réaffichages, `useRef` vous donne simplement un moyen de « pointer vers » ou « accéder à » un élément dans le DOM sans déclencher de réaffichages. C'est utile lorsque vous ne voulez pas que React gère l'état de l'entrée, mais que vous devez toujours lire sa valeur plus tard.

Voici à quoi cela ressemble :

```javascript
import { useRef } from "react";

function NameForm() {
  const inputRef = useRef();

  const handleSubmit = () => {
    alert(inputRef.current.value); // affiche la valeur de l'élément d'entrée
  };

  return (
    <>
      <input type="text" ref={inputRef} />; // vous donne un accès direct à l'élément d'entrée
      <button onClick={handleSubmit}>Soumettre</button> //
    </>
  );
}
```

React n'est pas impliqué dans le suivi de chaque frappe. Il ne vérifie la valeur que lorsque vous la demandez et l'entrée suit sa valeur elle-même.

**Pourquoi utiliser cela ?**

* C'est plus simple pour les formulaires rapides où vous n'avez besoin de la valeur qu'à la fin (comme à la soumission).
  
* Cela évite les réaffichages pendant la frappe, ce qui peut être utile dans les applications sensibles aux performances.
  

Mais : il est plus difficile de faire des choses comme la validation, les mises à jour en temps réel ou la synchronisation avec d'autres parties de votre application.

## Contrôlé vs non contrôlé : quelle est la différence ?

Maintenant que vous avez vu les deux, rendons les différences cristallines.

| **Composants contrôlés** | **Composants non contrôlés** |
| --- | --- |
| React est responsable. | Le navigateur est responsable. |
| Vous utilisez useState pour stocker la valeur. | Vous utilisez useRef pour accéder à la valeur. |
| Vous mettez à jour la valeur avec onChange. | L'entrée conserve sa propre valeur. |
| React réaffiche l'entrée chaque fois que la valeur change. | Vous y accédez en utilisant une ref uniquement lorsque vous en avez besoin. |

Pensez à un composant contrôlé comme un parent qui suit attentivement ce que son enfant écrit dans un cahier, vérifiant chaque mot au fur et à mesure qu'il est écrit.

Un composant non contrôlé est plus comme laisser l'enfant écrire librement et ne lire ce qu'il a écrit qu'à la fin.

## Quand utiliser les composants contrôlés vs non contrôlés

Les composants contrôlés et non contrôlés ont leur place. La clé est de savoir quand chacun a du sens pour votre projet et ce que vous voulez accomplir.

### Utiliser les composants contrôlés lorsque :

* Vous devez valider l'entrée pendant que l'utilisateur tape.  
  **Exemple** : Afficher une erreur si l'utilisateur laisse un champ vide.
  
* Vous voulez activer/désactiver les boutons en fonction de l'entrée.  
  **Exemple** : Désactiver le bouton « Soumettre » jusqu'à ce que tous les champs soient remplis.
  
* Vous construisez des formulaires dynamiques.  
  **Exemple** : Afficher ou masquer des champs en fonction de ce que l'utilisateur sélectionne.
  
* Vous devez synchroniser les valeurs d'entrée avec un autre état.  
  **Exemple** : Mettre à jour un aperçu en direct lorsque l'utilisateur tape.
  

### Utiliser les composants non contrôlés lorsque :

* Vous avez juste besoin de la valeur lorsque le formulaire est soumis.  
  **Exemple** : Un formulaire de contact de base qui envoie des données une fois.
  
* Vous n'avez pas besoin de mettre à jour l'interface utilisateur en fonction de l'entrée.
  
* Vous voulez de meilleures performances dans les grands formulaires.  
  **Exemple** : Des dizaines d'entrées qui n'ont pas besoin de déclencher des réaffichages à chaque changement.
  

**En bref :**

* Si vous devez surveiller, valider ou réagir à ce que l'utilisateur tape (interagir avec l'état ou l'interface utilisateur de votre application), optez pour le contrôlé.
  
* Si vous avez juste besoin de récupérer la valeur plus tard, le non contrôlé peut fonctionner.
  

## Conclusion

Les composants contrôlés vs non contrôlés peuvent sembler une petite distinction technique au premier abord, mais comprendre la différence vous donne beaucoup plus de contrôle sur le comportement de vos formulaires dans React.

Les composants contrôlés vous mettent au volant. React gère l'état du formulaire pour vous, donc vous savez toujours ce qu'il y a dans vos entrées. Cela facilite la validation des entrées de l'utilisateur en temps réel, la synchronisation des données du formulaire avec d'autres parties de votre application, et la création d'expériences plus interactives et dynamiques.

Les composants non contrôlés, en revanche, gardent les choses minimales. Le navigateur gère l'état de l'entrée, et vous n'y accédez que pour obtenir la valeur lorsque vous en avez besoin, généralement en utilisant une ref.

Il n'y a pas de réponse universelle pour savoir lequel est le meilleur. Cela dépend entièrement de vos besoins. Si votre formulaire doit réagir à l'entrée de l'utilisateur au fur et à mesure qu'elle change ou se connecter étroitement avec la logique de l'application, optez pour le contrôlé. Si vous avez juste besoin de collecter quelques valeurs et de passer à autre chose, le non contrôlé peut être plus simple.