---
title: Comment créer un système de design dans Next.js avec Tailwind CSS et Class
  Variance Authority
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-09-21T07:58:30.000Z'
originalURL: https://freecodecamp.org/news/how-a-design-system-in-next-js-with-tailwind-css-and-class-variance-authority
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/martin-adams-_OZCl4XcpRw-unsplash.jpg
tags:
- name: Design Systems
  slug: design-systems
- name: Next.js
  slug: nextjs
- name: tailwind
  slug: tailwind
seo_title: Comment créer un système de design dans Next.js avec Tailwind CSS et Class
  Variance Authority
seo_desc: 'By Olasunkanmi Balogun

  Building a web application and producing a smooth user experience in the always
  changing world of web development requires more than just good looks – you also
  need to make sure that your application''s design is efficient and c...'
---

Par Olasunkanmi Balogun

La création d'une application web et la production d'une expérience utilisateur fluide dans le monde en constante évolution du développement web nécessitent plus qu'un simple aspect attrayant - vous devez également vous assurer que le design de votre application est efficace et cohérent tout au long du projet.

Si vous disposez d'un système de design en place, vous pouvez facilement créer des composants UI cohérents et réutilisables dans de nombreux projets tout en conservant un aspect attrayant.

Un système de design est un ensemble de composants UI réutilisables et de tokens de design. Ces tokens sont comme des blocs de construction qui incluent des éléments tels que des boutons, des couleurs et des polices. Son objectif est de permettre aux développeurs et aux designers de créer des expériences produit engageantes en offrant une expérience utilisateur cohérente sur tous les produits.

Les designers utilisent souvent des outils comme Figma pour créer ces systèmes. Voici un exemple de système de design créé dans Figma :

![Design-System](https://www.freecodecamp.org/news/content/images/2023/09/Design-System.jpg)

Après que les designers aient créé ces éléments, les développeurs peuvent utiliser différents outils pour les utiliser et construire le site web. Il existe divers frameworks que les ingénieurs frontend peuvent choisir pour cela. Certains des plus populaires sont `MaterialUI` et `ChakraUI`. Ces bibliothèques peuvent faciliter les choses, mais elles ne couvrent peut-être pas tous les cas particuliers que vous souhaitez.

Si vous ou votre équipe de design avez des designs spécifiques en tête qui ne correspondent pas à ce que les bibliothèques existantes offrent, vous devrez vous plonger dans l'écriture d'une quantité substantielle de code. Cependant, ce processus peut rapidement devenir fastidieux et lourd, surtout lorsque le code que vous créez manque de cohérence ou lorsque vous vous retrouvez à construire répétitivement les mêmes éléments UI.

C'est là qu'un système de design devient incroyablement précieux. Armé de la connaissance de la manière d'implémenter un système de design, vous gagnez la capacité de créer un design sur mesure qui s'intègre parfaitement au système de design existant, offrant le niveau de flexibilité que vous désirez.

De plus, cette approche offre l'avantage de ne construire que les composants dont vous avez vraiment besoin. Contrairement à l'utilisation de bibliothèques, qui viennent souvent avec de nombreux composants pré-construits que vous n'utiliserez peut-être jamais, cette méthode garde votre base de code focalisée et efficace.

Créer votre propre design peut sembler attrayant, mais ce n'est pas aussi simple que cela peut paraître.

Néanmoins, avec l'assistance d'outils de stylisation tels que `Tailwind CSS` (qui est idéal grâce à son haut niveau de personnalisation), une bibliothèque connue sous le nom de [`cva`](#heading-installation) (qui est l'abréviation de `class-variance-authority`), et avec `TypeScript`, le processus d'établissement de votre système de design personnalisé dans `Next.js` devient notablement réalisable.

Maintenant que vous avez une compréhension claire de ce qu'est un système de design et de son importance, continuez à lire pour découvrir comment ces outils peuvent être combinés efficacement pour atteindre nos objectifs.

## Installation du projet : Installation de la bibliothèque CVA

Pour les besoins de cet article, il est supposé que vous avez déjà configuré votre projet `Next.js` et incorporé `TypeScript` et `Tailwind CSS`.

Si ce n'est pas le cas, l'intégration de ces deux éléments dans un nouveau projet `Next.js` est un processus simple.

Après cette configuration initiale, vous pouvez ajouter facilement la bibliothèque `CVA` à votre projet en utilisant la commande suivante :

```npm
npm i class-variance-authority
```

Avec l'inclusion de `CVA`, une interface conviviale est à votre disposition, simplifiant la définition des variantes.

Ces variantes permettent l'application conditionnelle de jeux de classes, tout en offrant les moyens d'exprimer des variations par défaut. Si cela semble un peu complexe pour le moment, ne vous inquiétez pas - nous plongerons dans des exemples pratiques au fur et à mesure que nous avancerons.

## Exemple pratique : Implémentation d'un système de design personnalisé

Imaginez une situation où vous construisez une application CRUD, équipée de `boutons` pour effectuer diverses actions telles que `créer`, `lire`, `mettre à jour` et `supprimer`.

Bien que ces `boutons` puissent partager des attributs communs comme `font-size` et `border-radius`, ils peuvent différer légèrement - par exemple, dans leurs couleurs. Peut-être préféreriez-vous un bouton `rouge` pour l'action de suppression, un bouton `bleu` pour la création, et un bouton `noir` pour la mise à jour.

Traditionnellement, vous pourriez envisager de créer des composants séparés pour chaque `bouton` et leur attribuer des couleurs distinctes. Par exemple, pour créer le bouton `noir`, vous incluriez la classe utilitaire `bg-black` de `Tailwind CSS` pour définir la couleur de fond :

```tsx
export default function Button() {
  return (
    <button
      className="bg-black rounded-3xl py-2 text-white w-80 font-sm"
      // autres attributs du bouton
    >
      // texte du bouton
    </button>
  );
}

```

Cependant, au lieu de créer des composants séparés pour chaque `bouton`, vous pouvez rationaliser le processus en concevant un seul composant `bouton` qui peut s'adapter aux différentes variantes de boutons dont vous avez besoin. Ce concept est au cœur d'un système de design.

Explorons comment nous pouvons transformer ce même composant de bouton que nous avons précédemment créé pour répondre à nos besoins.

Notre première étape consiste à importer la fonction `cva` et les `VariantProps` de la bibliothèque `class-variance-authority`. Au fur et à mesure que nous avançons, l'importance de ces imports deviendra évidente :

```tsx
import { cva, VariantProps } from 'class-variance-authority'
```

Par la suite, nous allons définir une variable nommée `buttonStyles`. Cette variable contiendra l'invocation de la fonction cva.

Au sein de cette fonction, nous fournirons d'abord les `styles` par défaut pour les boutons, suivis de l'objet `variants`. Cet objet contiendra les variations pour les différents types de boutons que nous désirons. Ce segment est crucial lors de l'implémentation du système de design.

Dans votre code, incluez le fragment de code suivant :

```tsx
const buttonStyles = cva("rounded-3xl py-2 text-white w-80 font-sm", {
  variants: {
    intent: {
      primary: "bg-blue-700",
      secondary: "bg-black",
      danger: "bg-red-600",
    },
    defaultVariants: {
      intent: "primary",
    },
  },
});
```

Au sein de l'objet `variants` intégré, il existe un autre objet nommé `intent`. C'est ici que vous attribuez des noms aux différentes variations de boutons que vous désirez - par exemple, `primary`, `secondary` et `danger`, correspondant respectivement aux boutons `créer`, `mettre à jour` et `supprimer`.

Le style défini pour l'`intent` spécifié lors du rendu du `bouton` sera appliqué à ce `bouton`, où qu'il apparaisse.

De plus, l'objet `variants` présente une autre propriété appelée `defaultVariants`. L'`intent` au sein de l'objet `defaultVariant` sera appliqué lorsqu'aucun `intent` explicite n'est fourni. Dans ce cas, nous avons défini l'`intent` par défaut sur `primary`.

Ensuite, nous allons définir une interface nommée `ButtonProps` qui étend le type `VariantProps` fourni par la bibliothèque `class-variance-authority` :

```tsx
interface ButtonProps extends VariantProps<typeof buttonStyles> {
  text: string;
}

```

Cette interface est utilisée pour définir les props que le composant `Button` acceptera. Le type `VariantProps` de `class-variance-authority` ajoute la propriété `intent`, qui sera utilisée pour déterminer la `variante` du `bouton`. L'interface inclut également une propriété supplémentaire appelée `text`, qui est de type `string`, il s'agit du texte réel qui apparaîtra sur le `bouton`.

Ayant fait cela, nous pouvons procéder à l'implémentation du composant `Button` conformément à cette `interface` définie :

```tsx
export default function Button({ intent, text, ...props }: ButtonProps) {
  return (
    <button className={buttonStyles({ intent })} {...props}>
      {text}
    </button>
  );
}
```

Dans la fonction du composant `Button`, nous avons utilisé la destructuration d'objet pour recevoir la propriété `intent` de `ButtonProps` passée au composant.

De plus, nous avons utilisé l'opérateur de propagation `(...props)` pour propager toute autre prop qui pourrait être passée au composant. Cela nous permet de transmettre facilement tout autre attribut ou gestionnaire d'événements à l'élément `<button>`.

Cela rend également nos `props` correctement typées, avec leurs types précisément alignés lorsque vous survolez chacune d'elles. Par exemple, la prop `intent` adhère strictement aux `intents` que nous avons définis dans la variable `buttonStyles`, assurant une correspondance de type robuste :

![Screenshot--166-](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot--166-.png)

Ensuite, la partie cruciale est l'attribut `className` sur l'élément `<button>`. Nous utilisons la fonction `buttonStyles` pour passer un objet avec la propriété `intent`, qui correspond à la variante de bouton souhaitée (`primary`, `secondary` ou `danger`).

Cela génère dynamiquement les `styles` appropriés en fonction de l'`intent` sélectionné, appliquant les `styles` associés au bouton.

Enfin, nous avons rationalisé le processus de création de `boutons` avec différents `styles`, nous permettant d'utiliser un seul composant `Button` tout en modifiant dynamiquement son apparence via la prop `intent`, démontrant l'implémentation efficace de notre système de design personnalisé.

Avec cela en place, vous êtes maintenant équipé pour rendre le composant `Button` selon vos besoins et préférences. À titre de démonstration visuelle, observons les résultats après avoir rendu chacune des variantes :

```tsx
<>
  <Button intent="primary" text="Créer" /> <br /> <br />
  <Button intent="secondary" text="Mettre à jour" /> <br /> <br />
  <Button intent="danger" text="Supprimer" /> <br /> <br />
</>
```

Résultat visuel :

![chrome-capture-2023-7-15--1-](https://www.freecodecamp.org/news/content/images/2023/09/chrome-capture-2023-7-15--1-.png)

Cette représentation visuelle souligne la polyvalence et l'adaptabilité de notre composant `Button` rationalisé, montrant le style distinct obtenu grâce à l'approche basée sur l'intention au sein de notre propre système de design.

## Conclusion

Tout au long de ce parcours, vous avez acquis des connaissances sur le potentiel d'un système de design pour produire un composant de bouton polyvalent qui change dynamiquement de couleurs en réponse à l'intention fournie.

Il est important de noter que cette adaptabilité n'est pas limitée uniquement aux couleurs - vous pouvez également expérimenter avec les tailles de police, les couleurs de texte et diverses autres propriétés CSS.

Fort des connaissances que vous avez acquises, vous êtes maintenant en mesure de tirer parti de cette nouvelle compréhension pour non seulement améliorer votre compréhension des systèmes de design, mais aussi pour implémenter des solutions créatives qui correspondent à vos exigences de projet uniques. Bon codage !