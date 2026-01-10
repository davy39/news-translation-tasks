---
title: Comment créer une boutique de produits numériques avec Medusa et Next.js
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-10-17T22:59:34.000Z'
originalURL: https://freecodecamp.org/news/build-a-digital-products-store-with-medusa-and-next-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/digital-products.png
tags:
- name: ecommerce
  slug: ecommerce
- name: Next.js
  slug: nextjs
seo_title: Comment créer une boutique de produits numériques avec Medusa et Next.js
seo_desc: 'In this tutorial, you will learn how to build an e-book online store using
  Medusa and Next.js.

  Throughout the course of the article, we will:


  Utilize the Medusa Next.js Starter Template along with the Digital Products Recipe
  build the store.

  Enhance...'
---

Dans ce tutoriel, vous apprendrez à créer une boutique en ligne de livres électroniques en utilisant Medusa et Next.js.

Au cours de cet article, nous allons :

1. Utiliser le modèle de démarrage Medusa [Next.js Starter Template](https://medusajs.com/nextjs-commerce/) ainsi que la [Recette de Produits Numériques](https://docs.medusajs.com/recipes/digital-products) pour construire la boutique.
2. Améliorer les pages produits pour les adapter aux produits numériques. Cela implique l'ajout d'un bouton pour prévisualiser le contenu multimédia et l'affichage des détails essentiels du produit.
3. Affiner le processus de paiement pour le rendre plus efficace pour la livraison de produits numériques.
4. Créer des routes API Next.js pour valider et masquer les chemins de fichiers pour les téléchargements de produits.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/rmjjaunyells0it99c7a.gif)
_Démonstration de l'application finale_

## Table des matières

1. [Qu'est-ce que Medusa ?](#heading-quest-ce-que-medusa)
2. [Prérequis](#heading-prerequis)
3. [Démarrage](#heading-demarrage)
4. [Comment configurer les définitions de types TypeScript](#heading-comment-configurer-les-definitions-de-types-typescript)
5. [Comment incorporer les aperçus de livres électroniques dans les détails du produit](#heading-comment-incorporer-les-aperçus-de-livres-electroniques-dans-les-details-du-produit)
6. [Comment offrir des aperçus de livres électroniques](#heading-comment-offrir-des-aperçus-de-livres-electroniques)
7. [Comment ajuster les détails du produit et de la livraison](#heading-comment-ajuster-les-details-du-produit-et-de-la-livraison)
8. [Comment simplifier le paiement](#heading-comment-simplifier-le-paiement)
9. [Comment livrer des produits numériques](#heading-comment-livrer-des-produits-numeriques)

Commençons.

## Qu'est-ce que Medusa ?

Medusa est une suite d'outils et de modules spécialement conçus pour les produits e-Commerce.

En utilisant Medusa, vous pouvez construire une logique de commerce modulaire comme les [paniers](https://docs.medusajs.com/modules/carts-and-checkout/overview), les [produits](https://docs.medusajs.com/modules/products/overview) et la [gestion des commandes](https://docs.medusajs.com/modules/orders/overview). Il fournit également des outils qui vous aident à orchestrer des sites web ecommerce puissants, des applications POS, des produits compatibles avec le commerce, et tout ce qui se trouve entre les deux.

## Prérequis

Avant de commencer le tutoriel, vous devez avoir installé :

* [Node.js (V14 ou ultérieur)](https://docs.medusajs.com/tutorial/set-up-your-development-environment#nodejs)
* [Git](https://docs.medusajs.com/tutorial/set-up-your-development-environment/#git)
* [Medusa CLI](https://docs.medusajs.com/tutorial/set-up-your-development-environment#medusa-cli)

## Démarrage

En utilisant le modèle de démarrage Next.js, vous pouvez créer une nouvelle application Medusa en exécutant la commande suivante :

```bash
npx create-medusa-app@latest --with-nextjs-starter
```

Après cela, vous pouvez choisir de créer un compte utilisateur pour accéder au panneau d'administration. Ensuite, configurez l'infrastructure backend en suivant la recette des produits numériques de Medusa.

Une fois le backend configuré, créez des produits d'exemple via votre interface d'administration Medusa. Assurez-vous que ces produits incluent des fichiers multimédias numériques pour les aperçus et le contenu principal. Assurez-vous également d'incorporer des valeurs de métadonnées de produit pertinentes en utilisant des paires clé/valeur liées à chaque produit.

## Comment configurer les définitions de types TypeScript

Si vous utilisez JavaScript standard, vous pouvez sauter cette étape.

Avant de continuer, assurons-nous d'ajouter les définitions de types TypeScript nécessaires pour les produits numériques dans la vitrine Next.js.

```javascript
import { Product } from "@medusajs/medusa"
import { ProductVariant } from "@medusajs/product"

export enum ProductMediaVariantType {
  PREVIEW = "preview",
  MAIN = "main",
}

export type ProductMedia = {
  id: string
  name?: string
  file?: string
  mime_type?: string
  created_at?: Date
  updated_at?: Date
  attachment_type?: ProductMediaVariantType
  variant_id?: string
  variants?: ProductMediaVariant[]
}

export type ProductMediaVariant = {
  id: string
  variant_id: string
  product_media_id: string
  type: string
  created_at: Date
  updated_at: Date
}

export type DigitalProduct = Omit<Product, "variants"> & {
  product_medias?: ProductMedia[]
  variants?: DigitalProductVariant[]
}

export type DigitalProductVariant = ProductVariant & {
  product_medias?: ProductMedia
}

      throw err
    })

  return product_medias[0]
}

```

Ce code définit les types et interfaces TypeScript pour gérer les produits numériques et leurs fichiers multimédias associés dans un système de commerce électronique. Il introduit plusieurs structures cruciales :

1. `ProductMedia` : Cette interface décrit les fichiers multimédias liés à un produit. Ces fichiers peuvent inclure des images, des documents ou tout autre actif numérique. Elle comprend des propriétés telles qu'un `id` (un identifiant unique pour le média), `name` (un nom optionnel pour le média), `file` (représentant le chemin de fichier ou l'URL), `mime_type` (le type de média, par exemple image/jpeg), `created_at` et `updated_at` timestamps, et `attachment_type` qui catégorise le média comme "preview" ou "main". De plus, un élément multimédia peut avoir plusieurs variantes, le rendant adaptable pour divers cas d'utilisation.
2. `ProductMediaVariant` : Cette interface représente différentes variantes ou versions d'un média de produit. Chaque variante a son `id` unique, `variant_id` (le reliant à une variante de produit spécifique), `product_media_id` (le liant à un élément multimédia particulier), et des timestamps pour `created_at` et `updated_at`.
3. `DigitalProduct` : Il étend le type `Product` standard en introduisant un tableau appelé `product_medias`. Ce tableau permet l'association de fichiers multimédias avec un produit numérique, permettant la présentation d'images ou d'autres médias liés au produit. La propriété `variants` est adaptée pour les produits numériques, adaptant le `ProductVariant` générique aux exigences spécifiques des produits numériques.
4. `DigitalProductVariant` : Ce type, une extension de `ProductVariant`, permet la liaison de fichiers multimédias avec une variante spécifique d'un produit numérique. Cela est particulièrement précieux pour présenter différents actifs numériques associés à chaque variante du produit.

## Comment incorporer les aperçus de livres électroniques dans les détails du produit

Maintenant, ajoutons des aperçus de livres électroniques à notre page de détails de produit. Pour ce faire, nous allons obtenir les aperçus multimédias liés à la variante de produit actuellement sélectionnée.

Dans le fichier `src/lib/data/index.ts`, nous allons créer une fonction pour obtenir ces aperçus en fonction de la variante choisie.

```javascript
// ... autres imports
import { DigitalProduct, ProductMedia } from "types/product-media"

// ... reste des fonctions

export async function getProductMediaPreviewByVariant(
  variant: Variant
): Promise<ProductMedia> {
  const { product_medias } = await medusaRequest("GET", `/product-media`, {
    query: {
      variant_ids: variant.id,
      expand: ["variants"],
    },
  })
    .then((res) => res.body)
    .catch((err) => {
      throw err
    })

  return product_medias[0]
}

```

Cette fonction est responsable de la récupération d'informations liées à une variante de produit spécifique. Elle le fait en effectuant une requête HTTP vers le point de terminaison `/product-media`. Elle prend un argument, `variant`, qui est attendu d'être de type `Variant`. La requête inclut des paramètres de requête spécifiant les `variant_ids` et demande des détails supplémentaires sur les "variants" associés.

La fonction attend la réponse de la requête HTTP et extrait le corps de la réponse, qui est supposé être un tableau d'objets de médias de produit. Elle retourne ensuite le premier objet de média de produit de ce tableau, en supposant qu'il y a au moins un tel objet. Si une erreur se produit pendant la requête, elle capture l'erreur et la relance.

## Comment offrir des aperçus de livres électroniques

Pour donner aux clients un aperçu du contenu du livre électronique, nous fournirons un PDF d'aperçu avec les premières pages.

Pour ce faire, nous allons configurer une route API Next pour gérer les téléchargements de fichiers tout en gardant l'emplacement du fichier privé. Nous allons également créer un composant pour un bouton "télécharger l'aperçu gratuit" simple. Si une variante de produit a un média d'aperçu, il sera affiché dans le composant product-actions.

Vous pouvez utiliser les nouveaux types `DigitalProduct` et `DigitalProductVariant` pour corriger toute erreur TypeScript que vous pourriez rencontrer.

```javascript
import { NextRequest, NextResponse } from "next/server"

export async function GET(req: NextRequest) {
  // Obtenir les informations sur le fichier à partir de l'URL
  const { filepath, filename } = Object.fromEntries(req.nextUrl.searchParams)

  // Récupérer le fichier PDF
  const pdfResponse = await fetch(filepath)

  // Gérer le cas où le PDF n'a pas pu être récupéré
  if (!pdfResponse.ok) return new NextResponse("PDF non trouvé", { status: 404 })

  // Obtenir le contenu du PDF sous forme de buffer
  const pdfBuffer = await pdfResponse.arrayBuffer()

  // Définir les en-têtes de réponse
  const headers = {
    "Content-Type": "application/pdf",
    "Content-Disposition": `attachment; filename="${filename}"`, // Cela définit le nom du fichier pour le téléchargement
  }

  // Créer une NextResponse avec le contenu du PDF et les en-têtes
  const response = new NextResponse(pdfBuffer, {
    status: 200,
    headers,
  })

  return response
}
```

```javascript
import Button from "@modules/common/components/button"
import { ProductMedia } from "types/product-media"

type Props = {
  media: ProductMedia
}

const ProductMediaPreview: React.FC<Props> = ({ media }) => {
  const downloadPreview = () => {
    window.location.href = `${process.env.NEXT_PUBLIC_BASE_URL}/api/download/preview?filepath=${media.file}&filename=${media.name}`
  }

  return (
    <div>
      <Button variant="secondary" onClick={downloadPreview}>
        Télécharger l'aperçu gratuit
      </Button>
    </div>
  )
}

export default ProductMediaPreview
```

La fonction `GET` est conçue pour gérer les requêtes HTTP GET entrantes en utilisant le framework Next.js. Elle extrait d'abord les informations de l'URL de la requête, spécifiquement le `filepath` et le `filename`, qui sont attendus comme paramètres de requête. Elle tente ensuite de récupérer un fichier PDF à partir du `filepath` spécifié. Si le PDF est récupéré avec succès, il procède à la conversion du contenu du PDF en un buffer.

En cas d'échec de la récupération du PDF, par exemple si le fichier est introuvable, il retourne une réponse avec un message "PDF non trouvé" et un code de statut 404, indiquant une erreur de non-trouvé.

Si le PDF est récupéré avec succès, il définit les en-têtes de réponse, spécifiant que le type de contenu est "application/pdf" et définissant l'en-tête "Content-Disposition" pour contrôler le comportement des téléchargements de fichiers. L'en-tête `Content-Disposition` est défini sur "attachment", et le paramètre `filename` est utilisé pour suggérer un nom de fichier pour le PDF téléchargé.

```javascript
import Button from "@modules/common/components/button"
import { ProductMedia } from "types/product-media"

type Props = {
  media: ProductMedia
}

const ProductMediaPreview: React.FC<Props> = ({ media }) => {
  const downloadPreview = () => {
    window.location.href = `${process.env.NEXT_PUBLIC_BASE_URL}/api/download/preview?filepath=${media.file}&filename=${media.name}`
  }

  return (
    <div>
      <Button variant="secondary" onClick={downloadPreview}>
        Télécharger l'aperçu gratuit
      </Button>
    </div>
  )
}

export default ProductMediaPreview
```

Le composant ci-dessus affiche un aperçu du média d'un produit ainsi qu'un bouton pour télécharger un aperçu gratuit de ce média. Le composant reçoit une prop nommée `media`, qui est attendue d'être de type `ProductMedia`.

À l'intérieur du composant, il y a une fonction `downloadPreview` qui est appelée lorsque l'utilisateur clique sur le bouton "Télécharger l'aperçu gratuit". Cette fonction construit une URL pour télécharger l'aperçu en utilisant la propriété `window.location.href`. Elle combine l'URL de base de la variable d'environnement `NEXT_PUBLIC_BASE_URL` avec la route "/api/download/preview" et inclut des paramètres de requête pour le chemin de fichier et le nom de fichier, qui sont extraits de la prop `media`.

```javascript
// ... autres imports
import ProductMediaPreview from "../product-media-preview"
import { getProductMediaPreviewByVariant } from "@lib/data"

const ProductActions: React.FC<ProductActionsProps> = ({ product }) => {
    // ... autre code

  const [productMedia, setProductMedia] = useState({} as ProductMedia)

  useEffect(() => {
    const getProductMedia = async () => {
      if (!variant) return
      await getProductMediaPreviewByVariant(variant).then((res) => {
        setProductMedia(res)
      })
    }
    getProductMedia()
  }, [variant])

  return (
            // ... autre code

      {productMedia && <ProductMediaPreview media={productMedia} />}

      <Button onClick={addToCart}>
        {!inStock ? "En rupture de stock" : "Ajouter au panier"}
      </Button>
    </div>
  )
}

export default ProductActions
```

Ce composant est responsable de l'affichage des actions liées au produit, telles que l'ajout d'un produit au panier, et de l'affichage de l'aperçu du média du produit si disponible. Il utilise des opérations asynchrones pour récupérer les données du média en fonction de la `variant` fournie, ce qui en fait un composant dynamique et interactif.

## Comment ajuster les détails du produit et de la livraison

Étant donné que les informations sur le produit et la livraison diffèrent entre les produits numériques et physiques, nous apporterons les modifications nécessaires à ces sections sur la page du produit.

### Comment ajouter les détails du produit

J'ai ajouté des détails sur le produit au livre électronique en utilisant la section des métadonnées du produit dans l'administration Medusa. Puisque nous n'utilisons pas les attributs standard, nous allons améliorer le composant `ProductInfoTab` pour afficher toutes les métadonnées supplémentaires que nous incluons.

Par défaut, les métadonnées sont structurées sous forme d'objet. Pour simplifier la création de notre liste d'attributs, nous allons les transformer en tableau.

Dans ce cas, nous mettrons en avant quatre attributs des métadonnées, en les divisant en deux colonnes. Si vous souhaitez afficher un nombre différent d'attributs, vous pouvez facilement ajuster les valeurs dans la fonction `slice()` selon vos besoins.

```javascript
// ... autres composants

const ProductInfoTab = ({ product }: ProductTabsProps) => {
  // mapper l'objet metadata en un tableau
  const metadata = useMemo(() => {
    if (!product.metadata) return []
    return Object.keys(product.metadata).map((key) => {
      return [key, product.metadata?.[key]]
    })
  }, [product])

  return (
    <Tab.Panel className="text-small-regular py-8">
      <div className="grid grid-cols-2 gap-x-8">
        <div className="flex flex-col gap-y-4">
                {/* Mapper les métadonnées en tant qu'informations sur le produit */}
          {metadata &&
            metadata.slice(0, 2).map(([key, value], i) => (
              <div key={i}>
                <span className="font-semibold">{key}</span>
                <p>{value}</p>
              </div>
            ))}
        </div>
        <div className="flex flex-col gap-y-4">
          {metadata.length > 2 &&
            metadata.slice(2, 4).map(([key, value], i) => {
              return (
                <div key={i}>
                  <span className="font-semibold">{key}</span>
                  <p>{value}</p>
                </div>
              )
            })}
        </div>
      </div>
      {product.tags?.length ? (
        <div>
          <span className="font-semibold">Tags</span>
        </div>
      ) : null}
    </Tab.Panel>
  )
}

// ... autres composants

```

### Comment ajuster les détails de livraison

Les informations de livraison ne sont pas pertinentes pour les produits numériques, nous allons donc modifier le contenu de cet onglet. Vous pouvez apporter les ajustements nécessaires au contenu du composant `ShippingInfoTab` dans le même fichier pour mieux correspondre aux exigences de votre boutique.

```javascript
// ... autres composants

const ProductTabs = ({ product }: ProductTabsProps) => {
  const tabs = useMemo(() => {
    return [
      {
        label: "Informations sur le produit",
        component: <ProductInfoTab product={product} />,
      },
      {
        label: "Livraison du livre électronique",
        component: <ShippingInfoTab />,
      },
    ]
  }, [product])
    // ... reste du code
}

// ... autres composants

const ShippingInfoTab = () => {
  return (
    <Tab.Panel className="text-small-regular py-8">
      <div className="grid grid-cols-1 gap-y-8">
        <div className="flex items-start gap-x-2">
          <FastDelivery />
          <div>
            <span className="font-semibold">Livraison instantanée</span>
            <p className="max-w-sm">
              Votre livre électronique sera livré instantanément par email. Vous pouvez également
              le télécharger depuis votre compte à tout moment.
            </p>
          </div>
        </div>
        <div className="flex items-start gap-x-2">
          <Refresh />
          <div>
            <span className="font-semibold">Aperçus gratuits</span>
            <p className="max-w-sm">
              Obtenez un aperçu gratuit du livre électronique avant de l'acheter. Il suffit de cliquer sur
              le bouton ci-dessus pour le télécharger.
            </p>
          </div>
        </div>
      </div>
    </Tab.Panel>
  )
}

// ... autres composants

```

Le composant `ProductTabs` est utilisé pour rendre un ensemble d'onglets. Le composant prend une prop `product`, et il utilise le hook `useMemo` pour créer un tableau d'objets d'onglets. Chaque objet d'onglet se compose d'une étiquette et d'un composant à afficher lorsque cet onglet est actif.

Dans l'extrait ci-dessus, il y a deux onglets : "Informations sur le produit" et "Livraison du livre électronique". L'onglet "Informations sur le produit" affiche des informations sur le produit en utilisant le composant `ProductInfoTab`, que nous avons défini précédemment.

L'onglet "Livraison du livre électronique" utilise le composant `ShippingInfoTab` pour afficher des informations liées à la livraison du livre électronique. À l'intérieur du composant `ShippingInfoTab`, il fournit des détails sur le processus de livraison, mentionnant la livraison instantanée par email et l'option de télécharger depuis un compte, ainsi que des aperçus gratuits de livres électroniques.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/10p0z2piqkpv60m4jgab.png)
_Page du Produit_

## Comment simplifier le paiement

La vente de produits numériques ne nécessite pas de recueillir les adresses physiques des clients. Nous avons seulement besoin de leur prénom et de leur adresse email pour livrer le livre électronique, ce qui simplifie le processus de paiement en supprimant les champs de saisie inutiles.

Dans cet exemple, nous allons conserver uniquement les champs de prénom, nom, pays et email, en supprimant complètement la section d'adresse de facturation. Gardez à l'esprit que vos besoins spécifiques peuvent nécessiter des champs de saisie différents.

Pour commencer, nous allons ajuster les types de paiement et le contexte en supprimant toute référence aux valeurs qui ne sont plus nécessaires.

```javascript
"use client"

import { medusaClient } from "@lib/config"
import useToggleState, { StateType } from "@lib/hooks/use-toggle-state"
import { Cart, Customer, StorePostCartsCartReq } from "@medusajs/medusa"
import Wrapper from "@modules/checkout/components/payment-wrapper"
import { isEqual } from "lodash"
import {
  formatAmount,
  useCart,
  useCartShippingOptions,
  useMeCustomer,
  useRegions,
  useSetPaymentSession,
  useUpdateCart,
} from "medusa-react"
import { useRouter } from "next/navigation"
import React, { createContext, useContext, useEffect, useMemo } from "react"
import { FormProvider, useForm, useFormContext } from "react-hook-form"
import { useStore } from "./store-context"

type AddressValues = {
  first_name: string
  last_name: string
  country_code: string
}

export type CheckoutFormValues = {
  shipping_address: AddressValues
  billing_address?: AddressValues
  email: string
}

interface CheckoutContext {
  cart?: Omit<Cart, "refundable_amount" | "refunded_total">
  shippingMethods: { label?: string; value?: string; price: string }[]
  isLoading: boolean
  readyToComplete: boolean
  sameAsBilling: StateType
  editAddresses: StateType
  initPayment: () => Promise<void>
  setAddresses: (addresses: CheckoutFormValues) => void
  setSavedAddress: (address: AddressValues) => void
  setShippingOption: (soId: string) => void
  setPaymentSession: (providerId: string) => void
  onPaymentCompleted: () => void
}

const CheckoutContext = createContext<CheckoutContext | null>(null)
```

Dans l'extrait ci-dessus, vous définissez des types TypeScript pour les valeurs d'adresse et la structure globale du formulaire. Le `CheckoutContext` est également créé pour servir de contexte de partage de données et de fonctions liées au paiement avec d'autres composants.

```javascript
interface CheckoutProviderProps {
  children?: React.ReactNode
}

const IDEMPOTENCY_KEY = "create_payment_session_key"

export const CheckoutProvider = ({ children }: CheckoutProviderProps) => {
  const {
    cart,
    setCart,
    addShippingMethod: {
      mutate: setShippingMethod,
      isLoading: addingShippingMethod,
    },
    completeCheckout: { mutate: complete, isLoading: completingCheckout },
  } = useCart()

  const { customer } = useMeCustomer()
  const { countryCode } = useStore()

  const methods = useForm<CheckoutFormValues>({
    defaultValues: mapFormValues(customer, cart, countryCode),
    reValidateMode: "onChange",
  })
```

Le composant `CheckoutProvider` gère les données du panier, les informations du client, la gestion des formulaires et les interactions avec les méthodes de paiement et de livraison. Il configure divers hooks et fonctions à ces fins.

Vous définissez également une clé d'idempotence qui sera utilisée pour prévenir les requêtes en double lors de la création de la session de paiement.

```javascript
 const methods = useForm<CheckoutFormValues>({
    defaultValues: mapFormValues(customer, cart, countryCode),
    reValidateMode: "onChange",
  })

  const {
    mutate: setPaymentSessionMutation,
    isLoading: settingPaymentSession,
  } = useSetPaymentSession(cart?.id!)

  const { mutate: updateCart, isLoading: updatingCart } = useUpdateCart(
    cart?.id!
  )

  const { shipping_options } = useCartShippingOptions(cart?.id!, {
    enabled: !!cart?.id,
  })

  const { regions } = useRegions()

  const { resetCart, setRegion } = useStore()
  const { push } = useRouter()

  const editAddresses = useToggleState()
  const sameAsBilling = useToggleState(
    cart?.billing_address && cart?.shipping_address
      ? isEqual(cart.billing_address, cart.shipping_address)
      : true
  )
```

Dans cette section de code, plusieurs variables et hooks sont initialisés pour faciliter la gestion d'un processus de paiement.

Nous utilisons la variable `methods` pour gérer le formulaire de paiement, avec des valeurs initiales peuplées par la fonction `mapFormValues`. Le code configure également des fonctions de mutation pour mettre à jour la session de paiement et le panier (`setPaymentSessionMutation` et `updateCart`) et suit leurs états de chargement. Il récupère les options de livraison et les régions disponibles en utilisant des hooks, et il gère également les réinitialisations de panier et la sélection de région.

Il emploie également des états booléens (`editAddresses` et `sameAsBilling`) pour gérer si l'utilisateur est en train de modifier les adresses et si l'adresse de facturation correspond à l'adresse de livraison.

Ces composants assurent collectivement une navigation fluide et une gestion des données dans le processus de paiement.

```javascript
/**
   * Booléen qui indique si une partie du paiement est en cours de chargement.
   */
  const isLoading = useMemo(() => {
    return (
      addingShippingMethod ||
      settingPaymentSession ||
      updatingCart ||
      completingCheckout
    )
  }, [
    addingShippingMethod,
    completingCheckout,
    settingPaymentSession,
    updatingCart,
  ])

  /**
   * Booléen qui indique si le paiement est prêt à être complété. Un paiement est prêt à être complété si
   * l'utilisateur a fourni un email, une adresse de livraison, une adresse de facturation, une méthode de livraison et un moyen de paiement.
   */
  const readyToComplete = useMemo(() => {
    return (
      !!cart &&
      !!cart.email &&
      !!cart.shipping_address &&
      !!cart.billing_address &&
      !!cart.payment_session &&
      cart.shipping_methods?.length > 0
    )
  }, [cart])

  const shippingMethods = useMemo(() => {
    if (shipping_options && cart?.region) {
      return shipping_options?.map((option) => ({
        value: option.id,
        label: option.name,
        price: formatAmount({
          amount: option.amount || 0,
          region: cart.region,
        }),
      }))
    }

    return []
  }, [shipping_options, cart])
```

Dans le code ci-dessus, le booléen `isLoading` est calculé en utilisant le hook `useMemo`. Il reflète si une partie du paiement est en cours de chargement.

Cela est déterminé en observant quatre indicateurs de chargement : `addingShippingMethod`, `settingPaymentSession`, `updatingCart` et `completingCheckout`. Si l'un de ces indicateurs est `true`, l'indicateur `isLoading` sera également `true`. Cela indique qu'une partie du paiement est actuellement en cours.

Le booléen `readyToComplete`, également calculé avec `useMemo`, évalue si le paiement est prêt à être finalisé.

Pour être considéré comme prêt, plusieurs conditions doivent être remplies : il doit y avoir un objet `cart` valide, une adresse email, une adresse de livraison, une adresse de facturation, une session de paiement et au moins une méthode de livraison sélectionnée. Si toutes ces conditions sont satisfaites, `readyToComplete` sera `true`, signalant que le processus de paiement est prêt à être finalisé.

Enfin, la variable `shippingMethods` est calculée en utilisant `useMemo`. Il s'agit d'un tableau des méthodes de livraison disponibles avec les informations associées. Il mappe les `shipping_options` (si elles existent) à un tableau d'objets, chacun contenant une `value`, un `label` et un `price`.

Ces objets représentent les options de livraison, leurs noms et leurs prix, formatés en utilisant la fonction `formatAmount`. Ces données sont utilisées pour afficher et sélectionner les méthodes de livraison pendant le processus de paiement.

```javascript
/**
   * Réinitialise le formulaire lorsque le panier a changé.
   */
  useEffect(() => {
    if (cart?.id) {
      methods.reset(mapFormValues(customer, cart, countryCode))
    }
  }, [customer, cart, methods, countryCode])

  useEffect(() => {
    if (!cart) {
      editAddresses.open()
      return
    }

    if (cart?.shipping_address && cart?.billing_address) {
      editAddresses.close()
      return
    }

    editAddresses.open()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [cart])

  /**
   * Méthode pour définir la méthode de livraison sélectionnée pour le panier. Cela est appelé lorsque l'utilisateur sélectionne une méthode de livraison, comme UPS, FedEx, etc.
   */
  const setShippingOption = (soId: string) => {
    if (cart) {
      setShippingMethod(
        { option_id: soId },
        {
          onSuccess: ({ cart }) => setCart(cart),
        }
      )
    }
  }

  /**
   * Méthode pour créer les sessions de paiement disponibles pour le panier. Utilise une clé d'idempotence pour prévenir les requêtes en double.
   */
  const createPaymentSession = async (cartId: string) => {
    return medusaClient.carts
      .createPaymentSessions(cartId, {
        "Idempotency-Key": IDEMPOTENCY_KEY,
      })
      .then(({ cart }) => cart)
      .catch(() => null)
  }

  /**
   * Méthode qui appelle la méthode createPaymentSession et met à jour le panier avec la session de paiement.
   */
  const initPayment = async () => {
    if (cart?.id && !cart.payment_sessions?.length && cart?.items?.length) {
      const paymentSession = await createPaymentSession(cart.id)

      if (!paymentSession) {
        setTimeout(initPayment, 500)
      } else {
        setCart(paymentSession)
        return
      }
    }
  }

  /**
   * Méthode pour définir la session de paiement sélectionnée pour le panier. Cela est appelé lorsque l'utilisateur sélectionne un fournisseur de paiement, comme Stripe, PayPal, etc.
   */
  const setPaymentSession = (providerId: string) => {
    if (cart) {
      setPaymentSessionMutation(
        {
          provider_id: providerId,
        },
        {
          onSuccess: ({ cart }) => {
            setCart(cart)
          },
        }
      )
    }
  }

  const prepareFinalSteps = () => {
    initPayment()

    if (shippingMethods?.length && shippingMethods?.[0]?.value) {
      setShippingOption(shippingMethods[0].value)
    }
  }

  const setSavedAddress = (address: AddressValues) => {
    const setValue = methods.setValue

    setValue("shipping_address", {
      country_code: address.country_code || "",
      first_name: address.first_name || "",
      last_name: address.last_name || "",
    })
  }

  /**
   * Méthode qui valide si la région du panier correspond à la région de l'adresse de livraison. Si ce n'est pas le cas, elle mettra à jour la région du panier.
   */
  const validateRegion = (countryCode: string) => {
    if (regions && cart) {
      const region = regions.find((r) =>
        r.countries.map((c) => c.iso_2).includes(countryCode)
      )

      if (region && region.id !== cart.region.id) {
        setRegion(region.id, countryCode)
      }
    }
  }

  /**
   * Méthode qui définit les adresses et l'email sur le panier.
   */
  const setAddresses = (data: CheckoutFormValues) => {
    const { shipping_address, billing_address, email } = data

    const payload: StorePostCartsCartReq = {
      shipping_address,
      email,
    }

    if (isEqual(shipping_address, billing_address)) {
      sameAsBilling.open()
    }

    if (sameAsBilling.state) {
      payload.billing_address = shipping_address
    } else {
      payload.billing_address = billing_address
    }

    updateCart(payload, {
      onSuccess: ({ cart }) => {
        setCart(cart)
        prepareFinalSteps()
      },
    })
  }

  /**
   * Méthode pour compléter le processus de paiement. Cela est appelé lorsque l'utilisateur clique sur le bouton "Compléter le paiement".
   */
  const onPaymentCompleted = () => {
    complete(undefined, {
      onSuccess: ({ data }) => {
        resetCart()
        push(`/order/confirmed/${data.id}`)
      },
    })
  }

  return (
    <FormProvider {...methods}>
      <CheckoutContext.Provider
        value={{
          cart,
          shippingMethods,
          isLoading,
          readyToComplete,
          sameAsBilling,
          editAddresses,
          initPayment,
          setAddresses,
          setSavedAddress,
          setShippingOption,
          setPaymentSession,
          onPaymentCompleted,
        }}
      >
        <Wrapper paymentSession={cart?.payment_session}>{children}</Wrapper>
      </CheckoutContext.Provider>
    </FormProvider>
  )
}
```

Cette section de code orchestres divers aspects d'un processus de paiement e-commerce. Elle gère l'état du formulaire, réinitialise le formulaire lorsque le panier change, et bascule la visibilité de l'édition des adresses. Elle gère la sélection des méthodes de livraison, la création et l'initialisation des sessions de paiement, et le choix des fournisseurs de paiement. Et elle garantit que les adresses de livraison, les adresses de facturation et les informations d'email sont définies de manière appropriée, et valide la région du panier en fonction de l'adresse de livraison.

Elle coordonne également l'achèvement du processus de paiement, y compris le traitement du paiement et la confirmation de la commande.

Toutes ces fonctions et données sont encapsulées dans le composant `CheckoutProvider`.

```javascript
export const useCheckout = () => {
  const context = useContext(CheckoutContext)
  const form = useFormContext<CheckoutFormValues>()
  if (context === null) {
    throw new Error(
      "useProductActionContext must be used within a ProductActionProvider"
    )
  }
  return { ...context, ...form }
}

/**
 * Méthode pour mapper les champs d'un client potentiel et le panier aux valeurs du formulaire de paiement. Les informations sont assignées avec la priorité suivante :
 * 1. Informations du panier
 * 2. Informations du client
 * 3. Valeurs par défaut - null
 */
const mapFormValues = (
  customer?: Omit<Customer, "password_hash">,
  cart?: Omit<Cart, "refundable_amount" | "refunded_total">,
  currentCountry?: string
): CheckoutFormValues => {
  const customerShippingAddress = customer?.shipping_addresses?.[0]
  const customerBillingAddress = customer?.billing_address

  return {
    shipping_address: {
      first_name:
        cart?.shipping_address?.first_name ||
        customerShippingAddress?.first_name ||
        "",
      last_name:
        cart?.shipping_address?.last_name ||
        customerShippingAddress?.last_name ||
        "",
      country_code:
        currentCountry ||
        cart?.shipping_address?.country_code ||
        customerShippingAddress?.country_code ||
        "",
    },
    billing_address: {
      first_name:
        cart?.billing_address?.first_name ||
        customerBillingAddress?.first_name ||
        "",
      last_name:
        cart?.billing_address?.last_name ||
        customerBillingAddress?.last_name ||
        "",
      country_code:
        cart?.shipping_address?.country_code ||
        customerBillingAddress?.country_code ||
        "",
    },
    email: cart?.email || customer?.email || "",
  }
}

```

Le hook `useCheckout` est utilisé pour accéder au contexte de paiement et au contexte du formulaire, généralement utilisé dans les composants React. Il récupère le `CheckoutContext` à partir du contexte de l'application, et il obtient également le contexte du formulaire de paiement, permettant aux composants d'accéder et d'utiliser ces contextes.

La fonction `mapFormValues` est responsable de la cartographie et de la priorisation des informations pour le formulaire de paiement. Elle prend les données du client et du panier, ainsi que le pays actuel, et génère des valeurs pour les champs du formulaire de paiement.

Elle priorise les données dans cet ordre : 1) Informations du panier, 2) Informations du client, et 3) Valeurs par défaut définies à null si aucune information n'est disponible. Cette fonction aide à remplir le formulaire de paiement avec les données les plus pertinentes, assurant une expérience utilisateur plus fluide lors du processus de paiement.

Maintenant que le contexte est mis à jour, nous allons supprimer les champs de saisie redondants du formulaire de paiement.

```javascript
import { useCheckout } from "@lib/context/checkout-context"
import Button from "@modules/common/components/button"
import Spinner from "@modules/common/icons/spinner"
import ShippingAddress from "../shipping-address"

const Addresses = () => {
  const {
    editAddresses: { state: isEdit, toggle: setEdit },
    setAddresses,
    handleSubmit,
    cart,
  } = useCheckout()
  return (
    <div className="bg-white">
      <div className="text-xl-semi flex items-center gap-x-4 px-8 pb-6 pt-8">
        <div className="bg-gray-900 w-8 h-8 rounded-full text-white flex justify-center items-center text-sm">
          1
        </div>
        <h2>Adresse de livraison</h2>
      </div>
      {isEdit ? (
        <div className="px-8 pb-8">
          <ShippingAddress />
          <Button
            className="max-w-[200px] mt-6"
            onClick={handleSubmit(setAddresses)}
          >
            Continuer vers la livraison
          </Button>
        </div>
      ) : (
        <div>
          <div className="bg-gray-50 px-8 py-6 text-small-regular">
            {cart && cart.shipping_address ? (
              <div className="flex items-start gap-x-8">
                <div className="bg-green-400 rounded-full min-w-[24px] h-6 flex items-center justify-center text-white text-small-regular">
                  
                </div>
                <div className="flex items-start justify-between w-full">
                  <div className="flex flex-col">
                    <span>
                      {cart.shipping_address.first_name}{" "}
                      {cart.shipping_address.last_name}
                      {cart.shipping_address.country}
                    </span>
                    <div className="mt-4 flex flex-col">
                      <span>{cart.email}</span>
                    </div>
                  </div>
                  <div>
                    <button onClick={setEdit}>Modifier</button>
                  </div>
                </div>
              </div>
            ) : (
              <div className="">
                <Spinner />
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  )
}

export default Addresses
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/t1osg7g86bmd4s8qugdf.png)
_Page de Paiement_

Dans la dernière étape, nous allons modifier le composant `shipping-details` pour afficher des informations importantes après que la commande a été passée avec succès. Dans cette situation, nous allons supprimer tous les détails supplémentaires et ajouter l'adresse email de l'acheteur pour référence.

```javascript
import { Address, ShippingMethod } from "@medusajs/medusa"

type ShippingDetailsProps = {
  address: Address
  shippingMethods: ShippingMethod[]
  email: string
}

const ShippingDetails = ({
  address,
  shippingMethods,
  email,
}: ShippingDetailsProps) => {
  return (
    <div className="text-base-regular">
      <h2 className="text-base-semi">Livraison</h2>
      <div className="my-2">
        <h3 className="text-small-regular text-gray-700">Détails</h3>
        <div className="flex flex-col">
          <span>{`${address.first_name} ${address.last_name}`}</span>
          <span>{email}</span>
        </div>
      </div>
      <div className="my-2">
        <h3 className="text-small-regular text-gray-700">Méthode de livraison</h3>
        <div>
          {shippingMethods.map((sm) => {
            return <div key={sm.id}>{sm.shipping_option.name}</div>
          })}
        </div>
      </div>
    </div>
  )
}

export default ShippingDetails
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/io66rfgqkr88i1wcojj9.png)
_Page de Confirmation de Commande_

## Comment livrer des produits numériques

Il existe diverses façons de livrer des produits numériques aux clients, comme l'envoi d'un lien de téléchargement par email, l'ajout d'un bouton de téléchargement sur la page de confirmation de commande, ou l'octroi d'un accès via leur compte.

Dans toutes ces situations, notre objectif principal est de confirmer que seuls ceux qui ont acheté le produit peuvent l'obtenir.

Pour ce faire, j'ai configuré le backend pour créer un code spécial (jeton) pour chaque article numérique dans une commande. Nous pouvons utiliser GET `/store/:token` pour vérifier le jeton et fournir le fichier à l'utilisateur. Mais cette méthode expose l'adresse web du fichier à l'utilisateur, ce qui n'est pas idéal pour prévenir le piratage.

Nous allons donc créer une route API Next à `src/app/api/download/main/[token]/route.ts`. Cette route gérera le jeton, agissant comme un intermédiaire pour fournir le fichier à l'utilisateur sans révéler où il est stocké.

```javascript
import { NextRequest, NextResponse } from "next/server"

export async function GET(
  req: NextRequest,
  { params }: { params: Record<string, any> }
) {
  // Obtenir le token de l'URL
  const { token } = params

  // Définir l'URL pour récupérer les données du fichier PDF
  const pdfUrl = `${process.env.NEXT_PUBLIC_MEDUSA_BACKEND_URL}/store/product-media/${token}`

  // Récupérer les données du fichier PDF
  const { file, filename } = await fetch(pdfUrl).then((res) => res.json())

  // Gérer le cas où le token est invalide
  if (!file) return new NextResponse("Token invalide", { status: 401 })

  // Récupérer le fichier PDF
  const pdfResponse = await fetch(file)

  // Gérer le cas où le PDF n'a pas pu être récupéré
  if (!pdfResponse.ok) return new NextResponse("PDF non trouvé", { status: 404 })

  // Obtenir le contenu du PDF sous forme de buffer
  const pdfBuffer = await pdfResponse.arrayBuffer()

  // Définir les en-têtes de réponse
  const headers = {
    "Content-Type": "application/pdf",
    "Content-Disposition": `attachment; filename="${filename}"`, // Cela définit le nom du fichier pour le téléchargement
  }

  // Créer une NextResponse avec le contenu du PDF et les en-têtes
  const response = new NextResponse(pdfBuffer, {
    status: 200,
    headers,
  })

  return response
}

```

Ce code définit une fonction serverless pour gérer les requêtes HTTP GET dans une application Next.js. Il récupère un fichier PDF en utilisant un token fourni dans les paramètres de l'URL, en récupérant le fichier à partir d'une source externe. La fonction garantit la validité du token et la disponibilité du fichier PDF. Si le token est invalide, elle retourne une réponse "401 Non autorisé". Si le PDF n'est pas trouvé, elle retourne une réponse "404 Non trouvé".

Lorsque le PDF est récupéré avec succès, il construit des en-têtes de réponse, y compris le type de contenu comme "application/pdf" et un nom de fichier suggéré pour le téléchargement, et retourne le fichier PDF au client comme une pièce jointe téléchargeable. Ce code est généralement utilisé pour servir des fichiers PDF en réponse à des requêtes GET spécifiques.

Nous pouvons maintenant lier cette route API à partir de l'email de livraison comme ceci : `{your_store_url}/api/download/main/{token}`.

Vous pouvez ajouter votre propre logique pour invalider les tokens après un certain temps ou X nombre de téléchargements.

## **Mission accomplie !**

Félicitations, vous avez réussi ! N'oubliez pas d'explorer plus de [Recettes](https://docs.medusajs.com/recipes) pour d'autres façons de tirer le meilleur parti de Medusa.