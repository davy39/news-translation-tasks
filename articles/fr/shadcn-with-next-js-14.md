---
title: Comment utiliser Shadcn avec Next.js 14
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-01T15:21:36.000Z'
originalURL: https://freecodecamp.org/news/shadcn-with-next-js-14
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-3-.png
tags:
- name: Next.js
  slug: nextjs
- name: UI Design
  slug: ui-design
- name: User Interface
  slug: user-interface
seo_title: Comment utiliser Shadcn avec Next.js 14
seo_desc: Shadcn is a collection of beautifully designed, accessible, and customizable
  React components that you can use to build modern web applications with Next.js.
  With Shadcn, you can quickly and easily create user interfaces that are both stylish
  and fun...
---

Shadcn est une collection de composants React magnifiquement conçus, accessibles et personnalisables que vous pouvez utiliser pour construire des applications web modernes avec Next.js. Avec Shadcn, vous pouvez créer rapidement et facilement des interfaces utilisateur à la fois stylées et fonctionnelles.

Si vous cherchez un moyen de construire des applications web modernes, stylées et accessibles avec Next.js, alors Shadcn est une excellente option.

Dans ce guide, vous apprendrez comment installer et utiliser Shadcn dans vos projets Next.js, comment styliser des éléments et comment personnaliser les composants Shadcn.

## Table des matières

* [Qu'est-ce que Shadcn ?](#heading-questce-que-shadcn)
* [Comment installer Next.js et Shadcn](#heading-comment-installer-nextjs-et-shadcn)
* [Comment installer Next.js](#heading-comment-installer-nextjs)
* [Comment installer Shadcn](#heading-comment-installer-shadcn)
* [Comment utiliser Shadcn dans Next.js](#heading-comment-utiliser-shadcn-dans-nextjs)
* [Comment styliser un bouton à la manière difficile et à la manière Shadcn](#heading-comment-styliser-un-bouton-a-la-maniere-difficile-et-a-la-maniere-shadcn)
* [Comment ajouter un composant de Shadcn](#heading-comment-ajouter-un-composant-de-shadcn)
* [Styliser un bouton à la manière difficile](#heading-styliser-un-bouton-a-la-maniere-difficile-en-utilisant-tailwind)
* [Styliser un bouton à la manière Shadcn](#heading-styliser-un-bouton-a-la-maniere-shadcn)
* [Comment personnaliser les composants Shadcn](#heading-comment-personnaliser-les-composants-shadcn)
* [Conclusion](#heading-conclusion)

## Qu'est-ce que Shadcn ?

Shadcn UI n'est pas spécifiquement une bibliothèque de composants ou un framework UI. Comme indiqué dans la documentation, il est décrit comme "une compilation de composants réutilisables qui peuvent être facilement copiés et collés dans nos applications".

Shadcn utilise Tailwind CSS et Radix UI comme base. Il offre actuellement une compatibilité avec Next.js, Gatsby, Remix, Astro, Laravel et Vite. Il existe un [guide d'intégration manuelle](https://ui.shadcn.com/docs/installation/manual) qui peut vous aider à l'incorporer avec d'autres technologies.

Vous pouvez obtenir le code source complet de ce tutoriel [ici](https://github.com/dotslashbit/fcc-article-resources/tree/main/nextjs-shadcn/my-app).

## Comment installer Next.js et Shadcn

Je vais suivre les instructions dans la [documentation Shadcn](https://ui.shadcn.com/docs/installation), donc vous pouvez suivre si vous le souhaitez.

Tout d'abord, vous devez choisir le framework que vous utilisez actuellement. Cet article et le code dans mon dépôt ci-dessus ont été écrits en pensant à Next.js, donc sélectionnez l'option Next.js.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-30-at-5.23.21-PM.png)
_Choisissez un framework pour configurer Shadcn_

Maintenant, vous devez installer et configurer un nouveau projet Next.js.

### Comment installer Next.js

J'utilise généralement npm, mais si vous utilisez un autre gestionnaire de paquets, n'hésitez pas à copier une commande pour votre gestionnaire de paquets respectif ci-dessous.

Pour installer Next.js avec npm :

```bash
npx create-next-app@latest my-app --typescript --tailwind --eslint
```

Pour installer Next.js avec yarn :

```bash
yarn create next-app@latest my-app --typescript --tailwind --eslint
```

Pour installer Next.js avec pnpm :

```bash
pnpm create next-app@latest my-app --typescript --tailwind --eslint

```

Pour installer Next.js avec bun :

```bash
bunx --bun create-next-app@latest my-app --typescript --tailwind --eslint

```

Après avoir exécuté l'une de ces commandes, vous verrez les questions de configuration suivantes :

```bash
Need to install the following packages:
create-next-app@14.1.0
Ok to proceed? (y) y
[32m✓[39m Would you like to use `src/` directory? … No / Yes
[32m✓[39m Would you like to use App Router? (recommended) … No / Yes
[32m✓[39m Would you like to customize the default import alias (@/*)? … No / Yes
```

J'ai sélectionné "No" pour la première question car je ne veux pas avoir un répertoire `src` à l'intérieur de mon répertoire `app`.

J'ai sélectionné "Yes" pour la deuxième question car je veux utiliser l'app router, qui est la manière recommandée pour Next.js 14.

Enfin, j'ai sélectionné "No" pour la troisième question car j'aime la manière dont les imports fonctionnent avec `@` dans Next.js 14.

### Comment installer Shadcn

Avant de continuer, n'oubliez pas d'aller dans le répertoire `my-app` dans votre terminal :

```bash
cd my-app
```

Pour initialiser Shadcn avec npm :

```bash
npx shadcn-ui@latest init

```

Pour initialiser Shadcn avec yarn :

```bash
npx shadcn-ui@latest init

```

Pour initialiser Shadcn avec pnpm :

```bash
pnpm dlx shadcn-ui@latest init

```

Pour initialiser Shadcn avec bun :

```bash
bunx --bun shadcn-ui@latest init

```

Après avoir exécuté l'une de ces commandes, vous verrez à nouveau des questions de configuration, mais cette fois-ci, elles concernent Shadcn :

```bash
[32m✓[39m Which style would you like to use? ● New York
[32m✓[39m Which color would you like to use as base color? ● Slate
[32m✓[39m Would you like to use CSS variables for colors? … yes
```

Vous pouvez voir les questions et mes réponses dans le code ci-dessus.

Pour la première question, il y a deux options, `default` et `New York`. J'ai choisi le style "New York".

Pour la deuxième question, il y a cinq options : `Slate`, `Gray`, `Zinc`, `Neutral`, `Stone`. J'ai choisi `Slate` car j'aime un style minimaliste en noir et blanc.

Pour la troisième question, il y a deux options : `Yes` et `No`. J'ai choisi oui, car je préfère avoir les variables CSS activées pour le style (bien que nous ne les utiliserons pas dans cet article).

Vous pouvez en savoir plus sur les options de `style`, les options de `base` et cette configuration [ici](https://ui.shadcn.com/docs/components-json).

Et avec cela, vous avez configuré un nouveau projet Next.js 14 avec Shadcn.

Maintenant, vous pouvez voir deux nouveaux répertoires qui ont été ajoutés à votre répertoire de projet, `components` et `lib`.

Remarquez que le répertoire `components` est actuellement vide, ce qui signifie que Shadcn ne charge pas votre projet avec des composants que vous pourriez ne pas utiliser. Cela vous donne beaucoup de flexibilité et garde votre projet léger (vous pouvez simplement ajouter les composants dont vous avez besoin).

## Comment utiliser Shadcn dans Next.js

Tout d'abord, supprimons tout le code de base du fichier `page.tsx` du projet `my-app`. (Vous n'avez besoin de supprimer le code de base que de `my-app/page.tsx`.)

Après avoir supprimé tout le code de base du fichier `page.tsx` à l'intérieur du répertoire `app`, j'ajouterai un simple texte "hello world".

Voici le code mis à jour de `page.tsx` :

```typescript
export default function Home() {
  return (
    <>
      <h1>Hello World</h1>
    </>
  );
}

```

Et voici à quoi votre projet devrait ressembler dans le navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-30-at-5.49.27-PM.png)
_Configuration Hello World pour le projet Next.js_

### Comment styliser un bouton à la manière difficile et à la manière Shadcn

Maintenant, ajoutons deux boutons à la page. Un bouton sera simple sans style, et l'autre sera un composant de Shadcn.

#### Comment ajouter un composant de Shadcn

Avant d'ajouter nos boutons, nous devons apprendre comment ajouter un composant de Shadcn à notre projet. Voici comment faire :

1. Allez sur la [documentation Shadcn](https://ui.shadcn.com/docs).
2. Cliquez sur le composant que vous souhaitez utiliser.
3. Vous verrez alors la commande à exécuter pour ajouter ce composant à votre projet.
4. Enfin, importez ce composant dans votre projet et commencez à l'utiliser.

Pour ajouter le composant `Button` de Shadcn, suivez ces étapes :

1. Allez sur la [page du composant Button](https://ui.shadcn.com/docs/components/button).
2. Exécutez ensuite cette commande dans votre terminal : `npx shadcn-ui@latest add button`. Note : Cette commande est pour npm – si vous utilisez un autre gestionnaire de paquets, vous devrez modifier légèrement la commande.
3. Enfin, importez le composant bouton dans le fichier où vous souhaitez l'utiliser.

Maintenant, nous verrons des exemples d'ajout d'un bouton de deux manières différentes : en utilisant Tailwind CSS et en utilisant Shadcn.

### Styliser un bouton à la manière difficile (en utilisant Tailwind)

```typescript
export default function Home() {
  return (
    <>
      <button className="p-2 bg-orange-400">Click me</button>
    </>
  );
}

```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-31-at-9.11.58-AM.png)
_Bouton personnalisé avec fond orange_

J'ai créé un bouton avec un fond orange ayant un padding de 2 unités. Vous pouvez voir qu'il a l'air laid et n'a également aucun effet de survol par défaut.

### Styliser un bouton à la manière Shadcn

```typescript
import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <>
      <Button variant="outline">Button</Button>
    </>
  );
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-31-at-9.16.22-AM.png)
_Bouton par défaut de Shadcn_

Pour utiliser le bouton Shadcn, importez d'abord le composant `Button` dans le fichier où vous souhaitez l'utiliser – vous n'avez pas besoin d'ajouter de style (vous pouvez le personnaliser, ce que vous apprendrez à faire dans la section suivante). Par défaut, il a l'air bien et il a des effets de survol. Donc, importez simplement le composant et vous pouvez l'utiliser.

Vous pouvez également jouer avec les différentes options que les composants Shadcn vous offrent. Allez sur la page de documentation de ce composant et jetez un œil aux options ou ouvrez le code source du composant qui se trouve dans le répertoire `components/ui`.

Examinons le code source de `button.tsx` pour voir combien de variantes de boutons vous pouvez créer.

```typescript
import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const buttonVariants = cva(
  "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default:
          "bg-primary text-primary-foreground shadow hover:bg-primary/90",
        destructive:
          "bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90",
        outline:
          "border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground",
        secondary:
          "bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2",
        sm: "h-8 rounded-md px-3 text-xs",
        lg: "h-10 rounded-md px-8",
        icon: "h-9 w-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
);

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean;
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button";
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    );
  }
);
Button.displayName = "Button";

export { Button, buttonVariants };

```

Vous pouvez voir qu'il y a un objet `variants`, et à l'intérieur, il y a plusieurs variantes parmi lesquelles choisir. Remarquez qu'il y a un objet `size` qui vous permet de choisir différentes tailles pour le bouton également.

Vous pouvez également voir qu'il y a un objet `defaultVariants` qui stocke la variante par défaut et la taille par défaut du bouton.

## Comment personnaliser les composants Shadcn

Rappelez-vous qu'après l'installation de Shadcn, le répertoire `components` était vide. Mais après avoir ajouté le composant `Button`, vous pouvez voir qu'il y a un répertoire `ui` à l'intérieur du répertoire `components`. Et à l'intérieur du répertoire `ui`, vous aurez le fichier `Button.tsx`, qui est le code pour le composant `Button`.

Si vous ouvrez le fichier `Button.tsx`, vous verrez qu'il y a plusieurs variantes du composant `Button` comme `default`, `destructive`, `outline`, `secondary`, `ghost`, et `link`. Il y a aussi une taille par défaut, et d'autres tailles parmi lesquelles choisir :

```typescript
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default:
          "bg-primary text-primary-foreground shadow hover:bg-primary/90",
        destructive:
          "bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90",
        outline:
          "border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground",
        secondary:
          "bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2",
        sm: "h-8 rounded-md px-3 text-xs",
        lg: "h-10 rounded-md px-8",
        icon: "h-9 w-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }

```

L'une des meilleures choses à propos des composants Shadcn est que vous pouvez les personnaliser et supprimer les variantes que vous n'utiliserez pas. Vous pouvez également ajouter vos propres variantes au composant.

Par exemple, disons que vous voulez ajouter le bouton personnalisé que nous avons codé en premier comme une variante du composant `Button` de Shadcn. Vous pouvez faire cela comme ceci :

```typescript
import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const buttonVariants = cva(
  "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default:
          "bg-primary text-primary-foreground shadow hover:bg-primary/90",
        destructive:
          "bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90",
        outline:
          "border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground",
        secondary:
          "bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
        myButton: "p-2 bg-orange-400",
      },
      size: {
        default: "h-9 px-4 py-2",
        sm: "h-8 rounded-md px-3 text-xs",
        lg: "h-10 rounded-md px-8",
        icon: "h-9 w-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
);

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean;
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button";
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    );
  }
);
Button.displayName = "Button";

export { Button, buttonVariants };

```

Remarquez que j'ai ajouté une nouvelle variante `myButton` et que j'ai simplement collé le style que nous avons utilisé pour le bouton personnalisé. C'est tout, et maintenant vous avez votre propre bouton personnalisé à l'intérieur du composant `Button` de Shadcn.

Remarquez que le code inclut maintenant une nouvelle variante nommée `myButton`, et j'ai simplement collé le style du bouton personnalisé de notre exemple précédent. Et c'est tout ! Maintenant, vous avez votre propre variante de composant `Button` Shadcn personnalisée.

Voici comment vous pouvez utiliser la variante personnalisée `myButton` dans votre projet :

```typescript
import { Button } from "@/components/ui/button";
export default function Home() {
  return (
    <div className="flex justify-center items-center flex-col gap-10">
      <Button variant="outline" size="sm">
        sm button
      </Button>
      <Button variant="destructive" size="lg">
        large button
      </Button>
      <Button variant="ghost" size="lg">
        ghost button
      </Button>
      <Button variant="link" size="lg">
        link button
      </Button>
      <Button variant="myButton">My Button</Button>
    </div>
  );
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-31-at-9.33.59-AM.png)
_Boutons avec plusieurs variantes de Shadcn_

Notez que j'ai ajouté plus de variantes du composant `Button`, juste pour vous montrer que vous pouvez créer plusieurs types de boutons avec différentes tailles très facilement.

Le dernier bouton dans l'exemple ci-dessus a la variante `myButton`, qui est la variante personnalisée que vous avez ajoutée au fichier `Button.tsx`. Mais cela n'affecte que le style, et vous pouvez ajouter votre propre taille personnalisée si vous le souhaitez.

## Conclusion

Dans ce guide, vous avez appris comment intégrer Shadcn dans vos projets Next.js. Vous pouvez explorer davantage la vaste bibliothèque de composants de Shadcn et les utiliser tels quels, ou vous pouvez les personnaliser à votre guise. Le pouvoir de créer votre prochaine application vous attend – allez la construire !

Si vous avez des commentaires sur cet article, veuillez me contacter sur [Twitter](https://twitter.com/introvertedbot).