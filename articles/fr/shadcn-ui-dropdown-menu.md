---
title: Comment créer un menu déroulant avec shadcn/ui
subtitle: ''
author: Ajay Kalal
co_authors: []
series: null
date: '2025-07-17T21:02:46.587Z'
originalURL: https://freecodecamp.org/news/shadcn-ui-dropdown-menu
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1752786132476/fef60fd2-ad5e-4f9d-9dcf-de4b99adac99.png
tags:
- name: shadcn
  slug: shadcn
- name: Tailwind CSS
  slug: tailwind-css
- name: Next.js
  slug: nextjs
- name: UI
  slug: ui
seo_title: Comment créer un menu déroulant avec shadcn/ui
seo_desc: 'Dropdown menus are little pop-up menus that help you show more options
  without cluttering your screen. They’re super helpful in websites and apps.

  In this guide, you’ll learn how to build a dropdown menu using shadcn/ui. It’s a
  tool that works well w...'
---

Les menus déroulants sont de petits menus contextuels qui vous aident à afficher plus d'options sans encombrer votre écran. Ils sont très utiles dans les sites web et les applications.

Dans ce guide, vous apprendrez à créer un menu déroulant en utilisant shadcn/ui. C'est un outil qui fonctionne bien avec Tailwind CSS et Radix UI pour vous aider à créer des menus esthétiques et faciles à utiliser.

## Table des matières

* [Qu'est-ce que shadcn/ui ?](#heading-qu-est-ce-que-shadcnui)
    
* [Pourquoi utiliser shadcn/ui pour les menus déroulants ?](#heading-pourquoi-utiliser-shadcnui-pour-les-menus-déroulants)
    
* [Créons un menu déroulant étape par étape](#heading-créons-un-menu-déroulant-étape-par-étape)
    
    * [Étape 1 : Démarrer un nouveau projet](#heading-étape-1-démarrer-un-nouveau-projet)
        
    * [Étape 2 : Ajouter le composant de menu déroulant](#heading-étape-2-ajouter-le-composant-de-menu-déroulant)
        
    * [Étape 3 : Importer ce dont vous avez besoin](#heading-étape-3-importer-ce-dont-vous-avez-besoin)
        
    * [Étape 4 : Construire un menu déroulant simple](#heading-étape-4-construire-un-menu-déroulant-simple)
        
    * [Étape 5 : Améliorer son apparence](#heading-étape-5-améliorer-son-apparenance)
        
    * [Étape 6 : Le rendre compatible avec tous les écrans](#heading-étape-6-le-rendre-compatible-avec-tous-les-écrans)
        
    * [Étape 7 : Ajouter des icônes sympas](#heading-étape-7-ajouter-des-icônes-sympas)
        
    * [Étape 8 : Il est déjà accessible !](#heading-étape-8-il-est-déjà-accessible)
        
* [Cas d'utilisation réel : Menu déroulant de pays avec drapeaux](#heading-cas-d-utilisation-réel-menu-déroulant-de-pays-avec-drapeaux)
    
* [Réflexions finales](#heading-réflexions-finales)
    

### 4E1 Prérequis

Avant de commencer, assurez-vous d'avoir :

* Des connaissances de base en React et JavaScript
    
* Node.js et un gestionnaire de paquets comme npm, pnpm ou yarn installés
    
* Une familiarité avec Tailwind CSS est un plus, mais pas obligatoire
    

Nous allons tout passer en revue étape par étape, donc ne vous inquiétez pas si vous n'êtes pas encore un expert.

## Qu'est-ce que shadcn/ui ?

[shadcn/ui](https://ui.shadcn.com/docs/installation) est un ensemble d'outils (appelés composants) qui vous aident à construire des parties d'un site web, comme des boutons, des modales et des menus déroulants. Il est construit avec Radix UI et stylisé avec Tailwind CSS. Il est parfait si vous utilisez React ou Next.js.

Avec shadcn/ui, vous n'obtenez pas seulement des composants stylisés, vous avez un contrôle total sur le fonctionnement et l'apparence de tout. Cela le rend parfait pour les équipes qui veulent une cohérence dans la conception sans sacrifier la flexibilité.

### Pourquoi utiliser shadcn/ui pour les menus déroulants ?

Les menus déroulants sont un excellent cas d'utilisation pour shadcn/ui car :

* Il est facile à utiliser avec le clavier et les lecteurs d'écran
    
* Vous pouvez créer des apparences personnalisées en utilisant Tailwind CSS
    
* Vous contrôlez son fonctionnement et son apparence
    
* Il fonctionne parfaitement dans les sites web et les applications réels
    
* Il s'intègre bien avec les workflows React modernes
    

## Créons un menu déroulant étape par étape

### Étape 1 : Démarrer un nouveau projet avec shadcn/ui

Vous n'avez pas besoin de configurer React, Next.js ou Tailwind manuellement. Exécutez simplement cette commande :

```bash
pnpm dlx shadcn@latest init
```

Cela créera automatiquement une nouvelle application Next.js avec Tailwind CSS et shadcn/ui préconfigurés.

Astuce : Vous pouvez également utiliser `npx` au lieu de `pnpm dlx` si vous préférez :

```bash
npx shadcn@latest init
```

### Étape 2 : Ajouter le composant de menu déroulant

Après que votre projet soit prêt, ajoutez le composant de menu déroulant en utilisant :

```bash
npx shadcn@latest add dropdown-menu
```

Cela importera tous les composants nécessaires pour créer un menu déroulant.

### Étape 3 : Importer ce dont vous avez besoin

Dans votre fichier React, importez le module complet de menu déroulant pour pouvoir accéder à toutes ses fonctionnalités :

```tsx
import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuGroup,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuPortal,
} from "@/components/ui/dropdown-menu"
```

### Étape 4 : Construire un menu déroulant simple

![Capture d'écran du menu déroulant de base que nous construisons](https://cdn.hashnode.com/res/hashnode/image/upload/v1752690572839/4cb2bd61-b843-4fe3-8530-4b341d38a633.jpeg align="center")

Voici un exemple de menu déroulant de base :

```tsx
export function ProfileMenu() {
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <button className="px-4 py-2 bg-primary text-white rounded">
          Ouvrir le menu
        </button>
      </DropdownMenuTrigger>
      <DropdownMenuContent className="w-56">
        <DropdownMenuLabel>Mon compte</DropdownMenuLabel>
        <DropdownMenuSeparator />
        <DropdownMenuItem>Profil</DropdownMenuItem>
        <DropdownMenuItem>Paramètres</DropdownMenuItem>
        <DropdownMenuItem>Déconnexion</DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
```

Ce n'est qu'un début. Vous pouvez ajouter des groupes, des sous-menus et des raccourcis clavier pour les utilisateurs avancés.

### Étape 5 : Améliorer son apparence

![Capture d'écran montrant le menu déroulant avec le style appliqué](https://cdn.hashnode.com/res/hashnode/image/upload/v1752690441156/0c2b8e39-72ca-4823-8dd2-6af305f02275.jpeg align="center")

Utilisez Tailwind CSS pour styliser votre menu déroulant et ajouter des effets de survol comme ceci :

```tsx
<DropdownMenu>
        <DropdownMenuTrigger asChild>
          <button className="px-3 py-1.5 bg-primary text-white text-sm font-medium rounded-md hover:bg-primary/90 transition-colors">
            Ouvrir le menu
          </button>
        </DropdownMenuTrigger>
        <DropdownMenuContent className="w-52 border-gray-200 shadow-lg rounded-md space-y-0.5">
          <DropdownMenuLabel className="text-xs text-gray-500">
            Mon compte
          </DropdownMenuLabel>
          <DropdownMenuSeparator className="border-t border-gray-100" />
          <DropdownMenuItem className="px-3 py-1.5 text-sm text-gray-700 hover:bg-gray-100 rounded-md cursor-pointer transition-colors">
            Profil
          </DropdownMenuItem>
          <DropdownMenuItem className="px-3 py-1.5 text-sm text-gray-700 hover:bg-gray-100 rounded-md cursor-pointer transition-colors">
            Paramètres
          </DropdownMenuItem>
          <DropdownMenuItem className="px-3 py-1.5 text-sm text-red-600 hover:bg-red-50 rounded-md cursor-pointer transition-colors">
```

### Étape 6 : Le rendre compatible avec tous les écrans

Vous voulez que votre menu déroulant soit réactif ? Utilisez les classes réactives de Tailwind :

```tsx
<DropdownMenuContent className="w-full md:w-64">
```

Vous pouvez également positionner dynamiquement le menu déroulant en utilisant le support de portail intégré de Radix.

### Étape 7 : Ajouter des icônes sympas

![Capture d'écran du menu déroulant avec des icônes ajoutées](https://cdn.hashnode.com/res/hashnode/image/upload/v1752691587711/0a96c5ca-0fa2-4916-92d2-087f2071d40e.jpeg align="center")

Installez les icônes Lucide :

```bash
npm install lucide-react
```

Puis utilisez-les dans votre menu :

```tsx
import { User, Settings, LogOut } from "lucide-react"

<DropdownMenuItem>
  <User className="mr-2 h-4 w-4" /> Profil
</DropdownMenuItem>
```

Les icônes aident les utilisateurs à parcourir rapidement les options, ce qui est une excellente touche pour l'UX.

### Étape 8 : Il est déjà accessible !

shadcn/ui (grâce à Radix UI) rend votre menu déroulant :

* Compatible avec le clavier
    
* Prêt pour les lecteurs d'écran
    
* Conforme aux meilleures pratiques du web
    

Vous n'avez pas besoin de configurer l'accessibilité, cela fonctionne simplement :)

## Cas d'utilisation réel : Menu déroulant de pays avec drapeaux

Vous cherchez un menu déroulant plus avancé ? Voici un exemple incroyable qui inclut la recherche, les icônes de drapeaux et le regroupement :

![Exemple de menu déroulant shadcn](https://cdn.hashnode.com/res/hashnode/image/upload/v1752598285627/6cb8b27e-7cba-4d92-95c5-3bea44e0c01c.png align="center")

449 [shadcn-country-dropdown.vercel.app](https://shadcn-country-dropdown.vercel.app/)

C'est open-source et un excellent endroit pour voir ce qui est possible avec shadcn/ui.

## Réflexions finales

Utiliser shadcn/ui pour créer un menu déroulant est rapide, simple et puissant. Vous obtenez un excellent style, une accessibilité et un contrôle total sur l'apparence et le fonctionnement des choses. Que vous débutiez ou que vous construisiez pour la production, c'est un outil solide à utiliser.

Les menus déroulants ne sont qu'un début. shadcn/ui offre une bibliothèque complète de composants headless pour construire des interfaces utilisateur modernes.

J'espère que vous avez trouvé cet article utile ! Si vous construisez un produit SaaS ou une application web qui implique une interaction utilisateur ou une conversion, envisagez d'améliorer la confiance des utilisateurs avec des notifications en temps réel comme des pop-ups modales, [sales pop up](http://toastie.saasindie.com), etc.