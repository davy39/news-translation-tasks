---
title: Comment créer un tableau de bord d'administration avec shadcn/ui et TanStack
  Start
author: Ajay Patel
date: '2025-12-04T16:57:05.759Z'
originalURL: https://freecodecamp.org/news/build-an-admin-dashboard-with-shadcnui-and-tanstack-start
description: 'In this guide, we’ll build a feature-rich admin dashboard using shadcn/ui
  for beautiful, reusable components and TanStack Start for a powerful, type-safe
  full-stack framework.

  By the end, you’ll have:


  A fully functional /dashboard layout


  A statisti...'
subtitle: ''
seo_title: Comment créer un tableau de bord d'administration avec shadcn/ui et TanStack
  Start
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1764780775287/b8cb826d-ac42-497c-8bb9-b9ffe797df83.png
tags:
- name: shadcn
  slug: shadcn
- name: shadcnui
  slug: shadcnui
- name: shadcn ui
  slug: shadcn-ui
- name: tanstack-start
  slug: tanstack-start
- name: tanstack
  slug: tanstack
seo_desc: 'In this guide, we’ll build a feature-rich admin dashboard using shadcn/ui
  for beautiful, reusable components and TanStack Start for a powerful, type-safe
  full-stack framework.

  By the end, you’ll have:


  A fully functional /dashboard layout


  A statisti...'
---


Dans ce guide, nous allons construire un tableau de bord d'administration riche en fonctionnalités en utilisant shadcn/ui pour des composants magnifiques et réutilisables, et TanStack Start pour un framework full-stack puissant et type-safe.

À la fin, vous aurez :

* Une mise en page `/dashboard` entièrement fonctionnelle
    
* Une page d'accueil de tableau de bord riche en statistiques avec des graphiques et des tableaux
    
* Une page Produits utilisant TanStack Query et TanStack Table
    
* Une page de paramètres avec des contrôles de profil et de notifications
    

![Tableau de bord TanStack Start](https://cdn.hashnode.com/res/hashnode/image/upload/v1764155649571/eda17d57-3f13-4526-be89-be55ec27453c.png align="center")

## Table des matières

1. [Pourquoi TanStack Start ?](#heading-pourquoi-tanstack-start)
    
2. [Pourquoi shadcn/ui ?](#heading-pourquoi-shadcnui)
    
3. [Comment créer le tableau de bord d'administration en utilisant shadcn/ui et TanStack Start](#heading-comment-creer-le-tableau-de-bord-dadministration-en-utilisant-shadcnui-et-tanstack-start)
    
    * [1\. Créer une nouvelle application TanStack](#heading-1-creer-une-nouvelle-application-tanstack)
        
    * [2\. Nettoyage initial](#heading-2-nettoyage-initial)
        
    * [3\. Configuration des blocs shadcn/studio](#heading-3-configuration-des-blocs-shadcnstudio)
        
    * [4\. Structure de routage pour le tableau de bord](#heading-4-structure-de-routage-pour-le-tableau-de-bord)
        
    * [5\. Création de la mise en page /dashboard](#heading-5-creation-de-la-mise-en-page-dashboard)
        
    * [6\. Construction de la page d'accueil du tableau de bord](#heading-6-construction-de-la-page-daccueil-du-tableau-de-bord)
        
    * [7\. Configuration de la page Produits](#heading-7-configuration-de-la-page-produits)
        
    * [8\. Page de paramètres](#heading-8-page-de-parametres)
        
4. [Démo en direct et code source](#heading-demo-en-direct-et-code-source)
    
5. [Résumé](#heading-resume)
    
    * [Et ensuite ?](#heading-et-ensuite)
        
    * [Ressources :](#heading-ressources)
        

### Prérequis

Avant de commencer le guide, comprenons les exigences de base du projet :

* Node.js 18+ installé
    
* Connaissances de base de React et TypeScript
    
* Familiarité avec TailwindCSS
    

### Ce que nous allons construire

Dans cet article, nous allons construire un tableau de bord d'administration entièrement fonctionnel avec trois sections principales :

1. **Aperçu du tableau de bord** : Une page d'accueil qui affiche divers graphiques montrant les mesures de vente, des widgets d'aperçu des produits et un tableau d'historique des transactions.
    
2. **Produits :** Une page de produits qui démontre la récupération de données, la pagination côté serveur et des fonctionnalités de tableau avancées comme la recherche par colonne, le tri et le filtrage par colonne.
    
3. **Paramètres :** Une page de paramètres conviviale avec la gestion du profil et les préférences de notification.
    

Le tableau de bord comprendra une navigation par barre latérale responsive, des fils d'Ariane, un menu déroulant de profil utilisateur et un sélecteur de langue.

## Pourquoi TanStack Start ?

[TanStack Start](https://tanstack.com/start/latest) est un framework React full-stack moderne construit au-dessus de TanStack Router. Il vise à être une alternative flexible et type-safe aux méta-frameworks traditionnels comme Next.js.

Certains avantages clés de TanStack Start incluent :

* Routage et chargement de données type-safe
    
* Rendu côté serveur (SSR) prêt à l'emploi
    
* Construit sur TanStack Router, avec un routage basé sur les fichiers
    
* Excellente DX avec TypeScript et l'intégration de TanStack Query
    

Nous l'associerons à shadcn/ui pour construire rapidement un tableau de bord d'administration soigné.

## Pourquoi shadcn/ui ?

[shadcn/ui](https://ui.shadcn.com/) est une collection de composants React magnifiquement conçus et accessibles, construits au-dessus de Radix UI et stylisés avec Tailwind CSS.

Au lieu d'installer un package, vous pouvez copier et coller le code du composant directement dans votre projet ou utiliser une CLI pour le générer. Cela vous donne un contrôle total sur la structure du code et le style. Cette approche rend Shadcn hautement personnalisable pour des frameworks comme TanStack Start, Next.js, Astro, etc.

## Comment créer le tableau de bord d'administration en utilisant shadcn/ui et TanStack Start

### 1\. Créer une nouvelle application TanStack

Pour commencer, vous devrez créer une nouvelle application TanStack Start. Vous pouvez le faire avec la commande suivante :

```typescript
pnpm create @tanstack/start@latest
```

Lors de la configuration via la CLI, lorsqu'elle vous interroge sur les add-ons, assurez-vous de sélectionner :

* Shadcn
    
* Table
    
* Query
    

Cela vous donnera la configuration shadcn/ui et les intégrations TanStack Query + Table que nous utiliserons plus tard.

### 2\. Nettoyage initial

Le modèle de démarrage de TanStack Start est livré avec quelques routes de démonstration et un en-tête dont nous n'avons pas besoin.

Nettoyez le projet comme suit :

1. Supprimez le dossier demo à l'intérieur du répertoire `src/routes` (ou là où se trouve votre répertoire de routage).
    
2. Supprimez `Header.tsx` de `src/components`.
    
3. Supprimez l'importation et l'utilisation de `Header` dans `src/routes/__root.tsx`.
    
4. Nettoyez le fichier `src/routes/index.tsx` pour obtenir quelque chose de minimal (ou laissez une simple page d'atterrissage).
    

À ce stade, vous pouvez effectuer le premier Commit dans votre dépôt.

### 3\. Configuration des blocs shadcn/studio

Avant de configurer, assurons-vous que vous comprenez bien ce que sont les registres shadcn/studio et Shadcn.

#### Qu'est-ce que shadcn/studio ?

[shadcn/studio](https://shadcnstudio.com) est une collection open-source de composants, blocs et modèles shadcn/ui à copier-coller. Il est associé à un puissant générateur de thèmes shadcn pour vous aider à concevoir, personnaliser et livrer plus rapidement.

#### Qu'est-ce que le registre Shadcn ?

Un registre shadcn est un système de partage et de distribution d'actifs de code réutilisables tels que des composants UI, des hooks et des configurations de thèmes à travers différents projets. Gérer votre propre registre vous permet de publier vos composants personnalisés que d'autres peuvent ensuite utiliser. Le registre utilise un fichier `registry.json` pour définir et organiser les composants et leurs fichiers associés.

Si vous voulez en savoir plus sur les registres, vous pouvez consulter la [documentation officielle ici](https://ui.shadcn.com/docs/registry).

Pour une construction rapide, nous utiliserons le bloc shadcn gratuit de shadcn/studio – dashboard shell.

Tout d'abord, configurez les registres dans votre `components.json` :

```typescript
{
  // ...existing config
  "registries": {
    "@shadcn-studio": "https://shadcnstudio.com/r/{name}.json",
    "@ss-components": "https://shadcnstudio.com/r/components/{name}.json",
    "@ss-blocks": "https://shadcnstudio.com/r/blocks/{name}.json",
    "@ss-themes": "https://shadcnstudio.com/r/themes/{name}.json"
  }
}
```

Si vous rencontrez des problèmes lors de la configuration, vous pouvez consulter la [documentation](https://shadcnstudio.com/docs/getting-started/how-to-use-shadcn-cli).

#### Installer le bloc Dashboard Shell

Pour commencer, visitez les [blocs Shadcn](https://shadcnstudio.com/blocks) et naviguez vers la section Dashboard and App. Sélectionnez ensuite le bloc [Dashboard Shell 1](https://shadcnstudio.com/blocks/dashboard-and-application/dashboard-shell#dashboard-shell-1) (son utilisation est gratuite).

En haut à droite, vous verrez une commande pour installer le bloc dans votre projet :

![dashboard shell shadcn/studio ](https://cdn.hashnode.com/res/hashnode/image/upload/v1764155098742/23d1bee2-e082-4b19-860a-8112fe6bf41c.png align="center")

Copiez cette commande, collez-la dans votre terminal et exécutez-la. Cela installera tous les composants nécessaires à la mise en page du tableau de bord (barre latérale, en-tête, menus déroulants, etc.).

### 4\. Structure de routage pour le tableau de bord

Ensuite, nous allons configurer les routes du tableau de bord.

Tout d'abord, créez une nouvelle route de mise en page pour `/dashboard` en ajoutant un fichier à :

`src/routes/dashboard.tsx`

Ensuite, à l'intérieur d'un répertoire `dashboard`, créez les trois pages qui vivront sous cette mise en page :

* `src/routes/dashboard/index.tsx` – aperçu principal du tableau de bord
    
* `src/routes/dashboard/products.tsx` – page du tableau des produits
    
* `src/routes/dashboard/settings.tsx` – page des paramètres
    

Votre dossier `routes` devrait ressembler à ceci :

```typescript
src/routes/
├── __root.tsx
├── index.tsx
├── dashboard.tsx          // Layout for all /dashboard/* pages
└── dashboard/
    ├── index.tsx          // /dashboard
    ├── products.tsx       // /dashboard/products
    └── settings.tsx       // /dashboard/settings
```

### 5\. Création de la mise en page `/dashboard`

Cela configurera la mise en page du tableau de bord. Créez `src/routes/dashboard.tsx` et collez :

fichier : `src/routes/dashboard.tsx`

```typescript
import LanguageDropdown from '@/components/shadcn-studio/blocks/dropdown-language'
import ProfileDropdown from '@/components/shadcn-studio/blocks/dropdown-profile'
import { Avatar, AvatarImage } from '@/components/ui/avatar'
import {
    Breadcrumb,
    BreadcrumbItem,
    BreadcrumbLink,
    BreadcrumbList,
    BreadcrumbPage,
    BreadcrumbSeparator
} from '@/components/ui/breadcrumb'
import { Button } from '@/components/ui/button'
import { Separator } from '@/components/ui/separator'
import {
    Sidebar,
    SidebarContent,
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarHeader,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarProvider,
    SidebarTrigger
} from '@/components/ui/sidebar'
import { createFileRoute, Link, Outlet, useLocation } from '@tanstack/react-router'
import {
    FacebookIcon,
    InstagramIcon,
    LanguagesIcon,
    LayoutDashboard,
    LinkedinIcon,
    LogIn,
    Package,
    Settings,
    TwitterIcon,
    User2
} from 'lucide-react'
import React from 'react'

export const Route = createFileRoute('/dashboard')({
    component: DashboardLayout
})

function DashboardLayout() {
    const location = useLocation()
    const pathSegments = location.pathname.split('/').filter(Boolean)

    return (
        <div className='flex min-h-dvh w-full'>
            <SidebarProvider>
                <Sidebar>
                    <SidebarContent>
                        <SidebarHeader>
                            <SidebarMenu>
                                <SidebarMenuItem>
                                    <SidebarMenuButton size="lg" asChild>
                                        <Link to="/">
                                            <div className="flex aspect-square size-8 items-center justify-center rounded-lg bg-primary text-primary-foreground">
                                                <User2 className="size-4" />
                                            </div>
                                            <div className="grid flex-1 text-left text-sm leading-tight">
                                                <span className="truncate font-semibold">Your App</span>
                                                <span className="truncate text-xs">Dashboard</span>
                                            </div>
                                        </Link>
                                    </SidebarMenuButton>
                                </SidebarMenuItem>
                            </SidebarMenu>
                        </SidebarHeader>

                        <SidebarGroup>
                            <SidebarGroupLabel>General</SidebarGroupLabel>
                            <SidebarGroupContent>
                                <SidebarMenu>
                                    <SidebarMenuItem>
                                        <SidebarMenuButton asChild>
                                            <Link to='/dashboard'>
                                                <LayoutDashboard />
                                                <span>Dashboard</span>
                                            </Link>
                                        </SidebarMenuButton>
                                    </SidebarMenuItem>
                                    <SidebarMenuItem>
                                        <SidebarMenuButton asChild>
                                            <Link to='/dashboard/products'>
                                                <Package />
                                                <span>Products</span>
                                            </Link>
                                        </SidebarMenuButton>
                                    </SidebarMenuItem>
                                    <SidebarMenuItem>
                                        <SidebarMenuButton asChild>
                                            <Link to='/dashboard/settings'>
                                                <Settings />
                                                <span>Settings</span>
                                            </Link>
                                        </SidebarMenuButton>
                                    </SidebarMenuItem>
                                </SidebarMenu>
                            </SidebarGroupContent>
                        </SidebarGroup>
                    </SidebarContent>
                </Sidebar>
                <div className='flex flex-1 flex-col'>
                    <header className='bg-card sticky top-0 z-50 border-b'>
                        <div className='mx-auto flex max-w-7xl items-center justify-between gap-6 px-4 py-2 sm:px-6'>
                            <div className='flex items-center gap-4'>
                                <SidebarTrigger className='[&_svg]:h-5 [&_svg]:w-5' />
                                <Separator orientation='vertical' className='hidden h-4 sm:block' />
                                <Breadcrumb className='hidden sm:block'>
                                    <BreadcrumbList>
                                        <BreadcrumbItem>
                                            <BreadcrumbLink asChild>
                                                <Link to='/'>Home</Link>
                                            </BreadcrumbLink>
                                        </BreadcrumbItem>
                                        <BreadcrumbSeparator />
                                        {pathSegments.map((segment, index) => {
                                            const path = `/${pathSegments.slice(0, index + 1).join('/')}`
                                            const isLast = index === pathSegments.length - 1
                                            const title = segment.charAt(0).toUpperCase() + segment.slice(1)

                                            return (
                                                <React.Fragment key={path}>
                                                    <BreadcrumbItem>
                                                        {isLast ? (
                                                            <BreadcrumbPage>{title}</BreadcrumbPage>
                                                        ) : (
                                                            <BreadcrumbLink asChild>
                                                                <Link to={path as any}>{title}</Link>
                                                            </BreadcrumbLink>
                                                        )}
                                                    </BreadcrumbItem>
                                                    {!isLast && <BreadcrumbSeparator />}
                                                </React.Fragment>
                                            )
                                        })}
                                    </BreadcrumbList>
                                </Breadcrumb>
                            </div>
                            <div className='flex items-center gap-1.5'>
                                <LanguageDropdown
                                    trigger={
                                        <Button variant='ghost' size='icon'>
                                            <LanguagesIcon />
                                        </Button>
                                    }
                                />
                                <ProfileDropdown
                                    trigger={
                                        <Button variant='ghost' size='icon' className='h-10 w-10'>
                                            <Avatar className='h-10 w-10 rounded-md'>
                                                <AvatarImage src='https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-1.png' />
                                            </Avatar>
                                        </Button>
                                    }
                                />
                            </div>
                        </div>
                    </header>
                    <main className='mx-auto w-full max-w-7xl flex-1 px-4 py-6 sm:px-6'>
                        <Outlet />
                    </main>
                    <footer>
                        <div className='text-muted-foreground mx-auto flex w-full items-center justify-between gap-3 px-4 py-3 flex-col sm:flex-row sm:gap-6 sm:px-6'>
                            <p className='text-sm text-center sm:text-left'>
                                {`©${new Date().getFullYear()}`}{' '}
                                <a href='#' className='text-primary'>
                                    TanStack Start
                                </a>
                                , Made for better web design
                            </p>
                            <div className='flex items-center gap-5'>
                                <a href='#'>
                                    <FacebookIcon className='h-4 w-4' />
                                </a>
                                <a href='#'>
                                    <InstagramIcon className='h-4 w-4' />
                                </a>
                                <a href='#'>
                                    <LinkedinIcon className='h-4 w-4' />
                                </a>
                                <a href='#'>
                                    <TwitterIcon className='h-4 w-4' />
                                </a>
                            </div>
                        </div>
                    </footer>
                </div>
            </SidebarProvider>
        </div>
    )
}
```

Vous avez maintenant une mise en page complète pour toutes les routes `/dashboard/*`.

Analysons les parties clés de notre mise en page de tableau de bord :

* **Structure de la barre latérale :** Le composant `<Sidebar>` enveloppe notre menu de navigation. À l'intérieur, nous utilisons `<SidebarMenu>` et `<SidebarMenuItem>` pour créer des liens de navigation. Chaque élément de menu utilise le composant `<Link>` de TanStack Router pour une navigation type-safe. Nous avons également un en-tête configuré dans le `<SidebarProvider>`.
    
* **Fils d'Ariane dynamiques :** La section breadcrumb utilise `location.pathname` pour diviser l'URL actuelle en segments, puis itère sur ceux-ci pour créer des liens de fil d'Ariane. La vérification `isLast` garantit que le dernier fil d'Ariane s'affiche sous forme de texte brut plutôt que de lien.
    
* **Actions de l'en-tête** : L'en-tête comprend deux menus déroulants : `<LanguageDropdown>` pour l'internationalisation et `<ProfileDropdown>` pour les actions du compte utilisateur. Ceux-ci proviennent des blocs `shadcn/studio` que nous avons installés.
    
* **Composant Outlet :** Le composant `<Outlet />` est l'endroit où les routes enfants (comme `/dashboard`, `/dashboard/products`) seront rendues. Cela rend notre mise en page réutilisable sur toutes les pages du tableau de bord. La mise en page utilise les classes utilitaires de Tailwind pour l'espacement, les couleurs et le comportement responsive, ce qui facilite la personnalisation selon votre cas d'utilisation.
    

Pour plus de détails concernant le composant Sidebar, vous pouvez [consulter la documentation officielle ici](https://ui.shadcn.com/docs/components/sidebar).

### 6\. Construction de la page d'accueil du tableau de bord

Créez `src/routes/dashboard/index.tsx` :

```typescript
import { type Item } from '@/components/shadcn-studio/blocks/datatable-transaction'
import { createFileRoute } from '@tanstack/react-router'

import { Card } from '@/components/ui/card'

import SalesMetricsCard from '@/components/shadcn-studio/blocks/chart-sales-metrics'
import TransactionDatatable from '@/components/shadcn-studio/blocks/datatable-transaction'
import StatisticsCard from '@/components/shadcn-studio/blocks/statistics-card-01'
import ProductInsightsCard from '@/components/shadcn-studio/blocks/widget-product-insights'
import TotalEarningCard from '@/components/shadcn-studio/blocks/widget-total-earning'

import {
    CalendarX2Icon,
    TriangleAlertIcon,
    TruckIcon
} from 'lucide-react'

// Statistics card data
const StatisticsCardData = [
    {
        icon: <TruckIcon className='h-4 w-4' />,
        value: '42',
        title: 'Shipped Orders',
        changePercentage: '+18.2%'
    },
    {
        icon: <TriangleAlertIcon className='h-4 w-4' />,
        value: '8',
        title: 'Damaged Returns',
        changePercentage: '-8.7%'
    },
    {
        icon: <CalendarX2Icon className='h-4 w-4' />,
        value: '27',
        title: 'Missed Delivery Slots',
        changePercentage: '+4.3%'
    }
]

// Earning data for Total Earning card
const earningData = [
    {
        img: 'https://cdn.shadcnstudio.com/ss-assets/blocks/dashboard-application/widgets/zipcar.png',
        platform: 'Zipcar',
        technologies: 'Vuejs & HTML',
        earnings: '-$23,569.26',
        progressPercentage: 75
    },
    {
        img: 'https://cdn.shadcnstudio.com/ss-assets/blocks/dashboard-application/widgets/bitbank.png',
        platform: 'Bitbank',
        technologies: 'Figma & React',
        earnings: '-$12,650.31',
        progressPercentage: 25
    }
]

// Transaction table data
const transactionData: Item[] = [
    {
        id: '1',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-1.png',
        avatarFallback: 'JA',
        name: 'Jack Alfredo',
        amount: 315.0,
        status: 'paid',
        email: 'jack@shadcnstudio.com',
        paidBy: 'mastercard'
    },
    {
        id: '2',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-2.png',
        avatarFallback: 'MG',
        name: 'Maria Gonzalez',
        amount: 253.4,
        status: 'pending',
        email: 'maria.g@shadcnstudio.com',
        paidBy: 'visa'
    },
    {
        id: '3',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-3.png',
        avatarFallback: 'JD',
        name: 'John Doe',
        amount: 852.0,
        status: 'paid',
        email: 'john.doe@shadcnstudio.com',
        paidBy: 'mastercard'
    },
    {
        id: '4',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-4.png',
        avatarFallback: 'EC',
        name: 'Emily Carter',
        amount: 889.0,
        status: 'pending',
        email: 'emily.carter@shadcnstudio.com',
        paidBy: 'visa'
    },
    {
        id: '5',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-5.png',
        avatarFallback: 'DL',
        name: 'David Lee',
        amount: 723.16,
        status: 'paid',
        email: 'david.lee@shadcnstudio.com',
        paidBy: 'mastercard'
    },
    {
        id: '6',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-6.png',
        avatarFallback: 'SP',
        name: 'Sophia Patel',
        amount: 612.0,
        status: 'failed',
        email: 'sophia.patel@shadcnstudio.com',
        paidBy: 'mastercard'
    },
    {
        id: '7',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-7.png',
        avatarFallback: 'RW',
        name: 'Robert Wilson',
        amount: 445.25,
        status: 'paid',
        email: 'robert.wilson@shadcnstudio.com',
        paidBy: 'visa'
    },
    {
        id: '8',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-8.png',
        avatarFallback: 'LM',
        name: 'Lisa Martinez',
        amount: 297.8,
        status: 'processing',
        email: 'lisa.martinez@shadcnstudio.com',
        paidBy: 'mastercard'
    },
    {
        id: '9',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-9.png',
        avatarFallback: 'MT',
        name: 'Michael Thompson',
        amount: 756.9,
        status: 'paid',
        email: 'michael.thompson@shadcnstudio.com',
        paidBy: 'visa'
    },
    {
        id: '10',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-10.png',
        avatarFallback: 'AJ',
        name: 'Amanda Johnson',
        amount: 189.5,
        status: 'pending',
        email: 'amanda.johnson@shadcnstudio.com',
        paidBy: 'mastercard'
    },
    {
        id: '11',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-11.png',
        avatarFallback: 'KB',
        name: 'Kevin Brown',
        amount: 1024.75,
        status: 'paid',
        email: 'kevin.brown@shadcnstudio.com',
        paidBy: 'visa'
    },
    {
        id: '12',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-12.png',
        avatarFallback: 'SD',
        name: 'Sarah Davis',
        amount: 367.2,
        status: 'failed',
        email: 'sarah.davis@shadcnstudio.com',
        paidBy: 'mastercard'
    },
    {
        id: '13',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-13.png',
        avatarFallback: 'CG',
        name: 'Christopher Garcia',
        amount: 598.45,
        status: 'processing',
        email: 'christopher.garcia@shadcnstudio.com',
        paidBy: 'visa'
    },
    {
        id: '14',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-14.png',
        avatarFallback: 'JR',
        name: 'Jennifer Rodriguez',
        amount: 821.3,
        status: 'paid',
        email: 'jennifer.rodriguez@shadcnstudio.com',
        paidBy: 'mastercard'
    },
    {
        id: '15',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-15.png',
        avatarFallback: 'DM',
        name: 'Daniel Miller',
        amount: 156.75,
        status: 'pending',
        email: 'daniel.miller@shadcnstudio.com',
        paidBy: 'visa'
    },
    {
        id: '16',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-16.png',
        avatarFallback: 'NW',
        name: 'Nicole White',
        amount: 934.1,
        status: 'paid',
        email: 'nicole.white@shadcnstudio.com',
        paidBy: 'mastercard'
    },
    {
        id: '17',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-17.png',
        avatarFallback: 'AL',
        name: 'Anthony Lopez',
        amount: 412.85,
        status: 'failed',
        email: 'anthony.lopez@shadcnstudio.com',
        paidBy: 'visa'
    },
    {
        id: '18',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-18.png',
        avatarFallback: 'MH',
        name: 'Michelle Harris',
        amount: 675.5,
        status: 'processing',
        email: 'michelle.harris@shadcnstudio.com',
        paidBy: 'mastercard'
    },
    {
        id: '19',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-19.png',
        avatarFallback: 'JC',
        name: 'James Clark',
        amount: 289.95,
        status: 'paid',
        email: 'james.clark@shadcnstudio.com',
        paidBy: 'visa'
    },
    {
        id: '20',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-20.png',
        avatarFallback: 'RL',
        name: 'Rachel Lewis',
        amount: 1156.25,
        status: 'pending',
        email: 'rachel.lewis@shadcnstudio.com',
        paidBy: 'mastercard'
    },
    {
        id: '21',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-21.png',
        avatarFallback: 'TY',
        name: 'Thomas Young',
        amount: 543.6,
        status: 'paid',
        email: 'thomas.young@shadcnstudio.com',
        paidBy: 'visa'
    },
    {
        id: '22',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-22.png',
        avatarFallback: 'SB',
        name: 'Stephanie Brown',
        amount: 789.3,
        status: 'processing',
        email: 'stephanie.brown@shadcnstudio.com',
        paidBy: 'mastercard'
    },
    {
        id: '23',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-23.png',
        avatarFallback: 'BM',
        name: 'Brandon Moore',
        amount: 425.75,
        status: 'failed',
        email: 'brandon.moore@shadcnstudio.com',
        paidBy: 'visa'
    },
    {
        id: '24',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-24.png',
        avatarFallback: 'KT',
        name: 'Kelly Taylor',
        amount: 1203.5,
        status: 'paid',
        email: 'kelly.taylor@shadcnstudio.com',
        paidBy: 'mastercard'
    },
    {
        id: '25',
        avatar: 'https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-25.png',
        avatarFallback: 'MA',
        name: 'Mark Anderson',
        amount: 356.2,
        status: 'pending',
        email: 'mark.anderson@shadcnstudio.com',
        paidBy: 'visa'
    }
]

export const Route = createFileRoute('/dashboard/')({
    component: RouteComponent,
})

function RouteComponent() {
    return (
        <div className='grid grid-cols-2 gap-6 lg:grid-cols-3'>
            {/* Statistics Cards */}
            <div className='col-span-full grid gap-6 sm:grid-cols-3 md:max-lg:grid-cols-1'>
                {StatisticsCardData.map((card, index) => (
                    <StatisticsCard
                        key={index}
                        icon={card.icon}
                        title={card.title}
                        value={card.value}
                        changePercentage={card.changePercentage}
                    />
                ))}
            </div>

            <div className='grid gap-6 max-xl:col-span-full lg:max-xl:grid-cols-2'>
                {/* Product Insights Card */}
                <ProductInsightsCard className='justify-between gap-3 *:data-[slot=card-content]:space-y-5' />

                {/* Total Earning Card */}
                <TotalEarningCard
                    title='Total Earning'
                    earning={24650}
                    trend='up'
                    percentage={10}
                    comparisonText='Compare to last year ($84,325)'
                    earningData={earningData}
                    className='justify-between gap-5 sm:min-w-0 *:data-[slot=card-content]:space-y-7'
                />
            </div>

            <SalesMetricsCard className='col-span-full xl:col-span-2 *:data-[slot=card-content]:space-y-6' />
            <Card className='col-span-full w-full py-0'>
                <TransactionDatatable data={transactionData} />
            </Card>
        </div>
    )
}
```

Notre page d'accueil de tableau de bord utilise divers blocs shadcn-studio comme :

* **Les cartes de statistiques** affichent les KPI (Commandes expédiées, Retours endommagés, etc.) avec des indicateurs de tendance. Chaque carte reçoit des props pour l'icône, la valeur, le titre et le pourcentage de changement, ce qui les rend réutilisables pour n'importe quelle mesure.
    
* **Les composants de graphique** comme `<SalesMetricsCard>` utilisent `recharts` sous le capot pour visualiser les données. Le style provient du composant card de shadcn/ui et des utilitaires Tailwind.
    
* **Le tableau de données des transactions** démontre l'intégration de TanStack Table. Nous passons un tableau d'objets de transaction, et le composant `<TransactionDatatable>` gère le rendu, le tri et la pagination. Remarquez comment nous utilisons le type `Item[]` de TypeScript pour une sécurité totale des types.
    

Si vous naviguez maintenant vers `/dashboard`, vous devriez voir un tableau de bord d'administration avec des statistiques KPI, des graphiques et un tableau de transactions. Voici à quoi cela ressemblerait :

![démo du tableau de bord tanstack start](https://cdn.hashnode.com/res/hashnode/image/upload/v1764747793227/ca1c0e10-e295-45c4-8e3c-15702583c887.jpeg align="center")

Nous avons construit ce magnifique tableau de bord rapidement en utilisant les blocs pré-construits de shadcn/studio.

### 7\. Configuration de la page Produits

Avant de construire notre tableau de produits, nous devons installer **Zod**, une bibliothèque de validation de schéma TypeScript-first. Nous l'utiliserons pour valider la structure des données des requêtes vers notre fonction serveur.

#### Pourquoi Zod ?

Les fonctions serveur de TanStack Start utilisent Zod pour garantir un transfert de données type-safe entre le client et le serveur. Lorsque nous demandons à récupérer des produits, Zod valide que la requête inclut les types corrects pour `page`, `pageSize`, `sortBy` et `filters`. Cela permet de détecter les erreurs au runtime et offre une excellente inférence TypeScript.

Maintenant, configurons la page des produits avec un tableau de produits. Mais avant cela, installons la dépendance du package zod. Voici la commande pour cela :

```bash
pnpm add zod 
```

#### Création de données de produits fictives

Nous devrons stocker nos données de produits fictives quelque part. Pour cela, nous allons créer un nouveau fichier `data/products.ts` et coller le code ci-dessous. Cela nous aidera à simuler les données de produits pour notre tableau de produits.

```typescript
import { createServerFn } from "@tanstack/react-start";
import { z } from "zod";

export type Product = {
    id: string
    name: string
    category: string
    price: number
    stock: number
    status: 'active' | 'draft' | 'archived'
    image: string
}

// Define the type for the data parameter
type ProductQueryParams = {
    page: number;
    pageSize: number;
    sortBy?: string;
    sortOrder?: "asc" | "desc";
    filters?: {
        name?: string;
        category?: string;
        status?: string;
    };
};

const products: Product[] = [
    {
        id: 'PROD-001',
        name: 'Wireless Noise Cancelling Headphones',
        category: 'Electronics',
        price: 299.99,
        stock: 45,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=100&q=80',
    },
    {
        id: 'PROD-002',
        name: 'Ergonomic Office Chair',
        category: 'Furniture',
        price: 199.50,
        stock: 12,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1592078615290-033ee584e267?w=100&q=80',
    },
    {
        id: 'PROD-003',
        name: 'Mechanical Gaming Keyboard',
        category: 'Electronics',
        price: 129.99,
        stock: 0,
        status: 'archived',
        image: 'https://images.unsplash.com/photo-1587829741301-dc798b91add1?w=100&q=80',
    },
    {
        id: 'PROD-004',
        name: 'Smart Fitness Watch',
        category: 'Wearables',
        price: 149.00,
        stock: 89,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=100&q=80',
    },
    {
        id: 'PROD-005',
        name: 'Minimalist Desk Lamp',
        category: 'Lighting',
        price: 45.00,
        stock: 23,
        status: 'draft',
        image: 'https://images.unsplash.com/photo-1507473888900-52e1ad14723b?w=100&q=80',
    },
    {
        id: 'PROD-006',
        name: 'Portable Bluetooth Speaker',
        category: 'Electronics',
        price: 79.99,
        stock: 150,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=100&q=80',
    },
    {
        id: 'PROD-007',
        name: 'Ceramic Coffee Mug Set',
        category: 'Kitchen',
        price: 24.99,
        stock: 200,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?w=100&q=80',
    },
    {
        id: 'PROD-008',
        name: 'Leather Messenger Bag',
        category: 'Accessories',
        price: 129.50,
        stock: 15,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=100&q=80',
    },
    {
        id: 'PROD-009',
        name: 'Wireless Charging Pad',
        category: 'Electronics',
        price: 39.99,
        stock: 75,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1586816879360-004f5b0c51e3?w=100&q=80',
    },
    {
        id: 'PROD-010',
        name: 'Succulent Plant Set',
        category: 'Home & Garden',
        price: 29.99,
        stock: 30,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=100&q=80',
    },
    {
        id: 'PROD-011',
        name: 'Professional Chef Knife',
        category: 'Kitchen',
        price: 89.95,
        stock: 42,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1593618998160-e34014e67546?w=100&q=80',
    },
    {
        id: 'PROD-012',
        name: 'Yoga Mat',
        category: 'Fitness',
        price: 35.00,
        stock: 100,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=100&q=80',
    },
    {
        id: 'PROD-013',
        name: 'Smart Thermostat',
        category: 'Home Automation',
        price: 199.00,
        stock: 0,
        status: 'archived',
        image: 'https://images.unsplash.com/photo-1567789884554-0b844b597180?w=100&q=80',
    },
    {
        id: 'PROD-014',
        name: 'Vintage Film Camera',
        category: 'Photography',
        price: 450.00,
        stock: 3,
        status: 'draft',
        image: 'https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=100&q=80',
    },
    {
        id: 'PROD-015',
        name: 'Cotton T-Shirt Pack',
        category: 'Apparel',
        price: 49.99,
        stock: 150,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=100&q=80',
    },
    {
        id: 'PROD-016',
        name: 'Electric Toothbrush',
        category: 'Personal Care',
        price: 69.99,
        stock: 55,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1559656914-a30970c1affd?w=100&q=80',
    },
    {
        id: 'PROD-017',
        name: 'Gaming Mouse',
        category: 'Electronics',
        price: 59.99,
        stock: 88,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=100&q=80',
    },
    {
        id: 'PROD-018',
        name: 'Essential Oil Diffuser',
        category: 'Home & Garden',
        price: 34.50,
        stock: 25,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1602928321679-560bb453f190?w=100&q=80',
    },
    {
        id: 'PROD-019',
        name: 'Running Shoes',
        category: 'Footwear',
        price: 119.99,
        stock: 60,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=100&q=80',
    },
    {
        id: 'PROD-020',
        name: 'Digital Drawing Tablet',
        category: 'Electronics',
        price: 249.00,
        stock: 18,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1561525140-c2a4cc68e4bd?w=100&q=80',
    },
    {
        id: 'PROD-021',
        name: 'Bamboo Cutting Board',
        category: 'Kitchen',
        price: 22.99,
        stock: 95,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1594385208974-2e75f8d7bb48?w=100&q=80',
    },
    {
        id: 'PROD-022',
        name: 'Sunglasses',
        category: 'Accessories',
        price: 159.00,
        stock: 40,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=100&q=80',
    },
    {
        id: 'PROD-023',
        name: 'Water Bottle',
        category: 'Fitness',
        price: 19.99,
        stock: 300,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1602143407151-01114192003f?w=100&q=80',
    },
    {
        id: 'PROD-024',
        name: 'Throw Pillow Set',
        category: 'Home Decor',
        price: 45.99,
        stock: 28,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1584100936595-c0654b55a2e6?w=100&q=80',
    },
    {
        id: 'PROD-025',
        name: 'Wireless Earbuds',
        category: 'Electronics',
        price: 89.99,
        stock: 120,
        status: 'active',
        image: 'https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=100&q=80',
    }
]

export const getProducts = createServerFn({ method: "GET" })
    .inputValidator(
        z.object({
            page: z.number().default(0),
            pageSize: z.number().default(10),
            sortBy: z.string().optional(),
            sortOrder: z.enum(["asc", "desc"]).optional(),
            filters: z
                .object({
                    name: z.string().optional(),
                    category: z.string().optional(),
                    status: z.string().optional(),
                })
                .optional(),
        })
    )
    .handler(async ({ data }: { data: ProductQueryParams }) => {
        const { page, pageSize, sortBy, sortOrder, filters } = data;

        // Apply filters
        let filteredProducts = [...products];

        if (filters) {
            if (filters.name) {
                filteredProducts = filteredProducts.filter((product) =>
                    product.name.toLowerCase().includes(filters.name!.toLowerCase())
                );
            }

            if (filters.category) {
                filteredProducts = filteredProducts.filter(
                    (product) =>
                        product.category.toLowerCase() === filters.category!.toLowerCase()
                );
            }

            if (filters.status) {
                filteredProducts = filteredProducts.filter(
                    (product) => product.status === filters.status
                );
            }
        }

        // Apply sorting
        if (sortBy) {
            filteredProducts.sort((a, b) => {
                const aValue = a[sortBy as keyof Product];
                const bValue = b[sortBy as keyof Product];

                if (typeof aValue === "string" && typeof bValue === "string") {
                    return sortOrder === "desc"
                        ? bValue.localeCompare(aValue)
                        : aValue.localeCompare(bValue);
                }

                if (typeof aValue === "number" && typeof bValue === "number") {
                    return sortOrder === "desc" ? bValue - aValue : aValue - bValue;
                }

                return 0;
            });
        }

        // Calculate pagination
        const totalCount = filteredProducts.length;
        const totalPages = Math.ceil(totalCount / pageSize);
        const paginatedProducts = filteredProducts.slice(
            page * pageSize,
            (page + 1) * pageSize
        );

        // Simulate network delay
        await new Promise((resolve) => setTimeout(resolve, 500));

        return {
            products: paginatedProducts,
            pagination: {
                page,
                pageSize,
                totalCount,
                totalPages,
            },
        };
    });
```

Comprenons la fonction serveur et analysons ce qui se passe dans `getProducts` :

* **Validation des entrées** : La méthode `.inputValidator()` utilise un schéma Zod pour valider les requêtes entrantes. Elle garantit que `page` et `pageSize` sont des nombres, que `sortOrder` est soit "asc" soit "desc", et que les filtres sont des chaînes optionnelles.
    
* **Filtrage des produits** : La fonction filtre le tableau de produits en fonction des filtres fournis (nom, catégorie, statut). Cela simule ce qu'une véritable requête de base de données ferait.
    
* **Tri** : Les produits sont triés par la colonne spécifiée (`sortBy`) par ordre croissant ou décroissant (`sortOrder`).
    
* **Pagination** : Nous calculons quelle tranche de produits retourner en fonction de `page` et `pageSize`, ainsi que des métadonnées comme `totalCount` et `totalPages`.
    

#### Créer le tableau des produits :

Une fois les données prêtes, créons un tableau dans `/dashboard/products.tsx`. Ce tableau utilisera nos données de produits fictives et fournira plusieurs fonctions comme la recherche, le tri et le filtrage. Ce tableau démontre la puissante combinaison de TanStack Query pour la gestion des données et de TanStack Table pour le rendu.

Collez le code ci-dessous dans le fichier `products.tsx` :

```bash
import { useQuery } from '@tanstack/react-query'
import { createFileRoute } from '@tanstack/react-router'
import {
    ColumnDef,
    ColumnFiltersState,
    flexRender,
    getCoreRowModel,
    getFilteredRowModel,
    getPaginationRowModel,
    getSortedRowModel,
    SortingState,
    useReactTable,
    VisibilityState,
} from '@tanstack/react-table'
import {
    ArrowUpDown,
    ChevronDown,
    Filter,
    Loader2,
    MoreHorizontal,
    Plus,
    Search
} from 'lucide-react'
import { useState } from 'react'

import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import {
    DropdownMenu,
    DropdownMenuCheckboxItem,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import { Input } from '@/components/ui/input'
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from '@/components/ui/table'
import { getProducts, type Product } from '@/data/products'

export const Route = createFileRoute('/dashboard/products')({
    component: ProductsPage,
})

export const columns: ColumnDef<Product>[] = [
    {
        accessorKey: 'name',
        header: ({ column }) => {
            return (
                <Button
                    variant="ghost"
                    onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
                >
                    Product Name
                    <ArrowUpDown className="ml-2 h-4 w-4" />
                </Button>
            )
        },
        cell: ({ row }) => (
            <div className="flex items-center gap-3">
                <img
                    src={row.original.image}
                    alt={row.getValue('name')}
                    className="h-10 w-10 rounded-md object-cover"
                />
                <div className="flex flex-col">
                    <span className="font-medium">{row.getValue('name')}</span>
                    <span className="text-xs text-muted-foreground">{row.original.id}</span>
                </div>
            </div>
        ),
    },
    {
        accessorKey: 'category',
        header: 'Category',
        cell: ({ row }) => <div>{row.getValue('category')}</div>,
    },
    {
        accessorKey: 'status',
        header: 'Status',
        cell: ({ row }) => {
            const status = row.getValue('status') as string
            return (
                <Badge variant={status === 'active' ? 'default' : status === 'draft' ? 'secondary' : 'outline'}>
                    {status}
                </Badge>
            )
        },
    },
    {
        accessorKey: 'price',
        header: () => <div className="text-right">Price</div>,
        cell: ({ row }) => {
            const amount = parseFloat(row.getValue('price'))
            const formatted = new Intl.NumberFormat('en-US', {
                style: 'currency',
                currency: 'USD',
            }).format(amount)

            return <div className="text-right font-medium">{formatted}</div>
        },
    },
    {
        accessorKey: 'stock',
        header: () => <div className="text-right">Stock</div>,
        cell: ({ row }) => {
            const stock = parseFloat(row.getValue('stock'))
            return <div className={`text-right ${stock === 0 ? 'text-red-500 font-medium' : ''}`}>{stock}</div>
        },
    },
    {
        id: 'actions',
        enableHiding: false,
        cell: ({ row }) => {
            const product = row.original

            return (
                <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                        <Button variant="ghost" className="h-8 w-8 p-0">
                            <span className="sr-only">Open menu</span>
                            <MoreHorizontal className="h-4 w-4" />
                        </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent align="end">
                        <DropdownMenuLabel>Actions</DropdownMenuLabel>
                        <DropdownMenuItem
                            onClick={() => navigator.clipboard.writeText(product.id)}
                        >
                            Copy Product ID
                        </DropdownMenuItem>
                        <DropdownMenuSeparator />
                        <DropdownMenuItem>Edit Product</DropdownMenuItem>
                        <DropdownMenuItem>View Details</DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>
            )
        },
    },
]

function ProductsPage() {
    const [sorting, setSorting] = useState<SortingState>([])
    const [columnFilters, setColumnFilters] = useState<ColumnFiltersState>([])
    const [columnVisibility, setColumnVisibility] = useState<VisibilityState>({})
    const [rowSelection, setRowSelection] = useState({})
    const [pagination, setPagination] = useState({
        pageIndex: 0,
        pageSize: 10,
    })

    const { data, isLoading } = useQuery({
        queryKey: ['products', pagination, sorting, columnFilters],
        queryFn: () => getProducts({
            data: {
                page: pagination.pageIndex,
                pageSize: pagination.pageSize,
                sortBy: sorting[0]?.id,
                sortOrder: sorting[0]?.desc ? 'desc' : 'asc',
                filters: {
                    name: (columnFilters.find((f) => f.id === 'name')?.value as string) || undefined,
                    status: (columnFilters.find((f) => f.id === 'status')?.value as string) || undefined,
                }
            }
        }),
    })

    const products = data?.products || []
    const totalPages = data?.pagination.totalPages || 0
    const totalCount = data?.pagination.totalCount || 0

    const table = useReactTable({
        data: products,
        columns,
        pageCount: totalPages,
        manualPagination: true,
        manualSorting: true,
        manualFiltering: true,
        onSortingChange: setSorting,
        onColumnFiltersChange: setColumnFilters,
        getCoreRowModel: getCoreRowModel(),
        getPaginationRowModel: getPaginationRowModel(),
        getSortedRowModel: getSortedRowModel(),
        getFilteredRowModel: getFilteredRowModel(),
        onColumnVisibilityChange: setColumnVisibility,
        onRowSelectionChange: setRowSelection,
        onPaginationChange: setPagination,
        state: {
            sorting,
            columnFilters,
            columnVisibility,
            rowSelection,
            pagination,
        },
    })

    return (
        <div className="w-full space-y-4">
            <div className="flex items-center justify-between">
                <h2 className="text-2xl font-bold tracking-tight">Products</h2>
                <div className="flex items-center gap-2">
                    <Button variant="outline" size="sm">
                        <Filter className="mr-2 h-4 w-4" />
                        Filter
                    </Button>
                    <Button size="sm">
                        <Plus className="mr-2 h-4 w-4" />
                        Add Product
                    </Button>
                </div>
            </div>

            <Card>
                <CardHeader>
                    <CardTitle>Product Management</CardTitle>
                    <CardDescription>
                        Manage your product catalog, track inventory, and update prices.
                    </CardDescription>
                </CardHeader>
                <CardContent>
                    <div className="flex items-center py-4 gap-2">
                        <div className="relative flex-1">
                            <Search className="absolute left-2 top-2.5 h-4 w-4 text-muted-foreground" />
                            <Input
                                placeholder="Filter products..."
                                value={(table.getColumn("name")?.getFilterValue() as string) ?? ""}
                                onChange={(event) =>
                                    table.getColumn("name")?.setFilterValue(event.target.value)
                                }
                                className="pl-8 max-w-sm"
                            />
                        </div>
                        <DropdownMenu>
                            <DropdownMenuTrigger asChild>
                                <Button variant="outline" className="ml-auto">
                                    Columns <ChevronDown className="ml-2 h-4 w-4" />
                                </Button>
                            </DropdownMenuTrigger>
                            <DropdownMenuContent align="end">
                                {table
                                    .getAllColumns()
                                    .filter((column) => column.getCanHide())
                                    .map((column) => {
                                        return (
                                            <DropdownMenuCheckboxItem
                                                key={column.id}
                                                className="capitalize"
                                                checked={column.getIsVisible()}
                                                onCheckedChange={(value) =>
                                                    column.toggleVisibility(!!value)
                                                }
                                            >
                                                {column.id}
                                            </DropdownMenuCheckboxItem>
                                        )
                                    })}
                            </DropdownMenuContent>
                        </DropdownMenu>
                    </div>
                    <div className="rounded-md border">
                        <Table>
                            <TableHeader>
                                {table.getHeaderGroups().map((headerGroup) => (
                                    <TableRow key={headerGroup.id}>
                                        {headerGroup.headers.map((header) => {
                                            return (
                                                <TableHead key={header.id}>
                                                    {header.isPlaceholder
                                                        ? null
                                                        : flexRender(
                                                            header.column.columnDef.header,
                                                            header.getContext()
                                                        )}
                                                </TableHead>
                                            )
                                        })}
                                    </TableRow>
                                ))}
                            </TableHeader>
                            <TableBody>
                                {isLoading ? (
                                    <TableRow>
                                        <TableCell colSpan={columns.length} className="h-24 text-center">
                                            <div className="flex items-center justify-center gap-2">
                                                <Loader2 className="h-6 w-6 animate-spin" />
                                                <span>Loading products...</span>
                                            </div>
                                        </TableCell>
                                    </TableRow>
                                ) : table.getRowModel().rows?.length ? (
                                    table.getRowModel().rows.map((row) => (
                                        <TableRow
                                            key={row.id}
                                            data-state={row.getIsSelected() && "selected"}
                                        >
                                            {row.getVisibleCells().map((cell) => (
                                                <TableCell key={cell.id}>
                                                    {flexRender(
                                                        cell.column.columnDef.cell,
                                                        cell.getContext()
                                                    )}
                                                </TableCell>
                                            ))}
                                        </TableRow>
                                    ))
                                ) : (
                                    <TableRow>
                                        <TableCell
                                            colSpan={columns.length}
                                            className="h-24 text-center"
                                        >
                                            No results.
                                        </TableCell>
                                    </TableRow>
                                )}
                            </TableBody>
                        </Table>
                    </div>
                    <div className="flex items-center justify-end space-x-2 py-4">
                        <div className="flex-1 text-sm text-muted-foreground">
                            {table.getFilteredSelectedRowModel().rows.length} of{" "}
                            {totalCount} row(s) selected.
                        </div>
                        <div className="space-x-2">
                            <Button
                                variant="outline"
                                size="sm"
                                onClick={() => table.previousPage()}
                                disabled={!table.getCanPreviousPage()}
                            >
                                Previous
                            </Button>
                            <Button
                                variant="outline"
                                size="sm"
                                onClick={() => table.nextPage()}
                                disabled={!table.getCanNextPage()}
                            >
                                Next
                            </Button>
                        </div>
                    </div>
                </CardContent>
            </Card>
        </div>
    )
}
```

Vous pouvez maintenant voir la page des produits entièrement fonctionnelle en naviguant vers `/products` où vous pouvez rechercher et trier les produits.

![démo du tableau de bord tanstack start](https://cdn.hashnode.com/res/hashnode/image/upload/v1764748681745/6f73dc04-ac9a-4f75-a1ab-88ed1fc5c6f3.jpeg align="center")

#### Comment TanStack Query et TanStack Table fonctionnent-ils dans le tableau des produits ?

Notre page de produits utilise TanStack Query pour la récupération de données et TanStack Table pour le rendu.

`useQuery` est un hook fondamental dans TanStack Query pour gérer l'état du serveur dans les applications web. Il simplifie la récupération de données, la mise en cache et la synchronisation.

L'extrait de code ci-dessous montre comment nous avons utilisé `useQuery` dans notre tableau de produits :

```typescript
import { useQuery } from '@tanstack/react-query';

const { data, isLoading } = useQuery({
    queryKey: ['products', pagination, sorting, columnFilters],
    queryFn: () => getProducts({...})
}
```

Le hook `useQuery` gère la récupération de données dans notre application. Pour plus de détails, vous pouvez [consulter la documentation officielle ici](https://tanstack.com/query/latest).

**useReactTable :**

```typescript
import { useReactTable } from '@tanstack/react-table'

const table = useReactTable({
    data: products,
    columns,
    manualPagination: true,
    manualSorting: true,
    manualFiltering: true,
})
```

**TanStack Table** gère l'état de l'interface utilisateur et le rendu. En réglant `manualPagination`, `manualSorting` et `manualFiltering` sur `true`, nous indiquons au tableau que la logique côté serveur gère ces opérations.

Lorsque les utilisateurs trient, filtrent ou paginent, le tableau met à jour ses états et React Query détecte le changement d'état dans la `queryKey`. Il récupère à nouveau les données du serveur, et le tableau se rafraîchit avec les nouvelles données.

Cette architecture est prête pour la production et s'adapte à des milliers de lignes. Il vous suffit de remplacer le point de terminaison de l'API fictive par votre véritable point de terminaison API.

### 8\. Page de paramètres

Enfin, ajoutons une page de paramètres simple avec une section de profil et quelques préférences de notification de base.

Voici le code pour la page de paramètres. Vous pouvez le coller dans `/dashboard/settings.tsx` :

```bash
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
import { Button } from '@/components/ui/button'
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
import { Checkbox } from "@/components/ui/checkbox"
import { Input } from '@/components/ui/input'
import { Separator } from '@/components/ui/separator'
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/dashboard/settings')({
  component: SettingsPage,
})

function SettingsPage() {
  return (
    <div className="space-y-6">
      <div>
        <h3 className="text-lg font-medium">Settings</h3>
        <p className="text-sm text-muted-foreground">
          Manage your account settings and set e-mail preferences.
        </p>
      </div>
      <Separator />

      <div className="grid gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Profile</CardTitle>
            <CardDescription>
              This is how others will see you on the site.
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="flex items-center gap-4">
              <Avatar className="h-20 w-20">
                <AvatarImage src="https://cdn.shadcnstudio.com/ss-assets/avatar/avatar-1.png" />
                <AvatarFallback>JD</AvatarFallback>
              </Avatar>
              <Button variant="outline">Change Avatar</Button>
            </div>
            <div className="space-y-1">
              <label htmlFor="username" className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">Username</label>
              <Input id="username" defaultValue="jdoe" />
            </div>
            <div className="space-y-1">
              <label htmlFor="email" className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">Email</label>
              <Input id="email" defaultValue="john.doe@example.com" />
            </div>
            <div className="space-y-1">
              <label htmlFor="bio" className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">Bio</label>
              <Input id="bio" placeholder="Tell us a little bit about yourself" />
            </div>
          </CardContent>
          <CardFooter>
            <Button>Save Changes</Button>
          </CardFooter>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Notifications</CardTitle>
            <CardDescription>
              Configure how you receive notifications.
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="flex items-center justify-between rounded-lg border p-4">
              <div className="space-y-0.5">
                <label className="text-base font-medium">Communication emails</label>
                <p className="text-sm text-muted-foreground">
                  Receive emails about your account activity.
                </p>
              </div>
              {/* Toggle would go here, using a simple checkbox for now */}
              <Checkbox defaultChecked />
            </div>
            <div className="flex items-center justify-between rounded-lg border p-4">
              <div className="space-y-0.5">
                <label className="text-base font-medium">Marketing emails</label>
                <p className="text-sm text-muted-foreground">
                  Receive emails about new products, features, and more.
                </p>
              </div>
              <Checkbox />
            </div>
          </CardContent>
          <CardFooter>
            <Button variant="outline">Update Preferences</Button>
          </CardFooter>
        </Card>
      </div>
    </div>
  )
}
```

Dans cette page, nous avons créé deux sections :

1. Section Profil
    
2. Section Notification
    

Ces deux sections ont été construites en utilisant des composants shadcn/ui comme Card, Footer, Checkbox, Avatar, Input, etc.

À ce stade, nous avons :

* Une mise en page de tableau de bord avec barre latérale, en-tête, fils d'Ariane et pied de page
    
* Une page Dashboard avec des graphiques, des aperçus et un tableau de transactions
    
* Une page Produits propulsée par :
    
    * Les fonctions serveur de TanStack Start
        
    * TanStack Query
        
    * TanStack Table
        
* Une page de paramètres propre utilisant les composants shadcn/ui
    

## Démo en direct et code source

Vous pouvez consulter le code source complet sur GitHub ici :

* Dépôt GitHub : [https://github.com/themeselection/tanstack-dashboard-demo](https://github.com/themeselection/tanstack-dashboard-demo)
    
* Démo en direct : [https://tanstack-dashboard-demo.vercel.app/dashboard](https://tanstack-dashboard-demo.vercel.app/dashboard)
    

N'hésitez pas à cloner, expérimenter et l'étendre pour répondre aux besoins de votre propre application !

## Résumé

Félicitations ! Vous avez construit un tableau de bord d'administration complet et prêt pour la production en utilisant TanStack Start, TanStack Table, TanStack Query, shadcn/ui et shadcn/studio.

Tout au long de ce tutoriel, vous avez acquis une expérience pratique en :

* **Développement d'applications full-stack avec sécurité des types** : Nous avons développé une application full-stack avec les fonctions serveur de TanStack Start et la validation Zod pour créer des API type-safe.
    
* **Récupération de données avancée** : Nous avons implémenté TanStack Query pour la récupération de données avec mise en cache automatique et mises à jour en arrière-plan.
    
* **Interactions complexes avec les tableaux** : Nous avons construit des tableaux de données riches en fonctionnalités avec TanStack Table, incluant la pagination, le tri et le filtrage côté serveur.
    
* **Construction plus rapide de l'interface utilisateur** : Nous avons exploité shadcn/ui et les blocs shadcn/studio pour construire rapidement des interfaces soignées.
    
* **Mises en page responsives** : Et nous avons créé des designs adaptatifs qui fonctionnent de manière fluide du mobile au bureau.
    

### Et ensuite ?

Maintenant que vous avez une base solide, envisagez d'implémenter certaines ou toutes les fonctionnalités ci-dessous si vous souhaitez approfondir ce travail :

* **Authentification** : Ajoutez l'authentification des utilisateurs avec Clerk, NextAuth ou Auth.js
    
* **Base de données réelle** : Remplacez les données fictives par Prisma + PostgreSQL ou Drizzle + SQLite
    
* **Validation de formulaire** : Intégrez React Hook Form avec Zod pour une gestion robuste des formulaires
    
* **Thématisation** : Implémentez le mode sombre et des schémas de couleurs personnalisés en utilisant le système de thèmes de shadcn/ui
    
* **Routes API pour le CRUD** : Ajoutez des opérations CRUD pour les produits (créer, mettre à jour, supprimer)
    
* **Internationalisation :** Rendez le tableau de bord compatible avec plusieurs langues en intégrant l'internationalisation.
    

Nous avons livré un tableau de bord évolutif et prêt pour la production beaucoup plus rapidement qu'en partant de zéro. J'espère que vous avez apprécié le processus – et merci de m'avoir lu !

### Ressources :

* [Documentation TanStack Start](https://tanstack.com/start)
    
* [Documentation TanStack Table](https://tanstack.com/table)
    
* [Documentation TanStack Query](https://tanstack.com/query)
    
* [Composants Shadcn UI](https://shadcnstudio.com/components)