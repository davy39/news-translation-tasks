---
title: How to Build a Digital Products Store with Medusa and Next.js
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
seo_title: null
seo_desc: 'In this tutorial, you will learn how to build an e-book online store using
  Medusa and Next.js.

  Throughout the course of the article, we will:


  Utilize the Medusa Next.js Starter Template along with the Digital Products Recipe
  build the store.

  Enhance...'
---

In this tutorial, you will learn how to build an e-book online store using Medusa and Next.js.

Throughout the course of the article, we will:

1. Utilize the Medusa [Next.js Starter Template](https://medusajs.com/nextjs-commerce/) along with the [Digital Products Recipe](https://docs.medusajs.com/recipes/digital-products) build the store.
2. Enhance the product pages to suit digital products. This involves adding a button for previewing media content and displaying essential product details.
3. Refine the checkout process to make it more efficient for delivering digital products.
4. Create Next.js API routes to validate and conceal file paths for product downloads.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/rmjjaunyells0it99c7a.gif)
_Demo of the final application_

## Table of Contents

1. [What is Medusa?](#heading-what-is-medusa)
2. [Prerequisites](#heading-prerequisites)
3. [Starting Out](#heading-starting-out)
4. [How to Set Up TypeScript Type Definitions](#heading-how-to-set-up-typescript-type-definitions)
5. [How to Incorporate e-Book Previews into the Product Details](#heading-how-to-incorporate-e-book-previews-into-the-product-details)
6. [How to Offer e-Book Previews](#heading-how-to-offer-e-book-previews)
7. [How to Adjust the Product and Shipping Details](#heading-how-to-adjust-the-product-and-shipping-details)
8. [How to Simplify the Checkout](#heading-how-to-simplify-the-checkout)
9. [How to Deliver Digital Products](#heading-how-to-deliver-digital-products)

Let's get started.

## What is Medusa?

Medusa is a suite of tools and modules specifically designed for e-Commerce products. 

Using Medusa, you can build modularized commerce logic like [carts](https://docs.medusajs.com/modules/carts-and-checkout/overview), [products](https://docs.medusajs.com/modules/products/overview), and [order management](https://docs.medusajs.com/modules/orders/overview). It also provide tools that help you orchestrate powerful ecommerce websites, POS applications, commerce-enabled products, and everything in between.

## Prerequisites

Before you get started with the tutorial, you should have installed:

* [Node.js(V14 or later)](https://docs.medusajs.com/tutorial/set-up-your-development-environment#nodejs)
* [Git](https://docs.medusajs.com/tutorial/set-up-your-development-environment/#git)
* [Medusa CLI](https://docs.medusajs.com/tutorial/set-up-your-development-environment#medusa-cli)

## Starting Out

Using the Next.js starter, you can create a new Medusa app by running the following command:

```bash
npx create-medusa-app@latest --with-nextjs-starter
```

After that, you can opt to create a user account for admin panel access. Then, set up the backend infrastructure following the Medusa Digital Products Recipe. 

Once the backend is set, create sample products through your Medusa admin interface. Make sure that these products include digital media files for previews and primary content. Also make sure to incorporate relevant product metadata values using key/value pairs linked to each product.

## How to Set Up TypeScript Type Definitions

If you’re using regular JavaScript, you can skip this step.

Before we continue, let's make sure to add in the necessary TypeScript type definitions for digital products in the Next.js storefront.

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

This code defines TypeScript types and interfaces for managing digital products and their associated media files in an e-commerce system. It introduces several crucial structures:

1. `ProductMedia`: This interface describes media files related to a product. These files can include images, documents, or any digital assets. It encompasses properties such as an `id` (a unique identifier for the media), `name` (an optional name for the media), `file` (representing the file path or URL), `mime_type` (the type of media, e.g., image/jpeg), `created_at` and `updated_at` timestamps, and `attachment_type` that categorizes the media as "preview" or "main." Additionally, a media item can have multiple variants, making it adaptable for various use cases.
2. `ProductMediaVariant`: This interface represents different variants or versions of a product's media. Each variant has its unique `id`, `variant_id` (relating it to a specific product variant), `product_media_id` (linking it to a particular media item), and timestamps for `created_at` and `updated_at`.
3. `DigitalProduct`: It extends the standard `Product` type by introducing an array called `product_medias`. This array enables the association of media files with a digital product, allowing the presentation of images or other media related to the product. The `variants` property is tailored for digital products, adapting the generic `ProductVariant` to digital product-specific requirements.
4. `DigitalProductVariant`: This type, an extension of `ProductVariant`, allows the linking of media files with a specific variant of a digital product. This is particularly valuable for showcasing different digital assets associated with each variant of the product.

## How to Incorporate e-Book Previews into the Product Details

Now, let's move forward by adding e-book previews to our product detail page. To do this, we'll get the media previews linked to the currently selected product variant. 

In the `src/lib/data/index.ts` file, we'll create a function to get these previews based on the chosen variant.

```javascript
// ... other imports
import { DigitalProduct, ProductMedia } from "types/product-media"

// ... rest of the functions

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

This function is responsible for fetching information related to a specific product variant. It does this by making an HTTP request to the `/product-media` endpoint. It takes one argument, `variant`, which is expected to be of type `Variant`. The request includes query parameters specifying the `variant_ids` and requests additional details about related "variants". 

The function awaits the response from the HTTP request and extracts the response body, which is assumed to be an array of product media objects. It then returns the first product media object from this array, presuming there is at least one such object. If an error occurs during the request, it catches the error and rethrows it.

## How to Offer e-Book Previews

To give customers a glimpse of the e-book's content, we'll provide a preview PDF with the first few pages. 

To do this, we'll set up a Next API route to manage file downloads while keeping the file's location private. We'll also create a component for a straightforward "download free preview" button. If a product variant has preview media, it will be shown in the product-actions component.

You can use the newly created `DigitalProduct` and `DigitalProductVariant` types to fix any TypeScript errors that you may encounter.

```javascript
import { NextRequest, NextResponse } from "next/server"

export async function GET(req: NextRequest) {
  // Get the file info from the URL
  const { filepath, filename } = Object.fromEntries(req.nextUrl.searchParams)

  // Fetch the PDF file
  const pdfResponse = await fetch(filepath)

  // Handle the case where the PDF could not be fetched
  if (!pdfResponse.ok) return new NextResponse("PDF not found", { status: 404 })

  // Get the PDF content as a buffer
  const pdfBuffer = await pdfResponse.arrayBuffer()

  // Define response headers
  const headers = {
    "Content-Type": "application/pdf",
    "Content-Disposition": `attachment; filename="${filename}"`, // This sets the file name for the download
  }

  // Create a NextResponse with the PDF content and headers
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
        Download free preview
      </Button>
    </div>
  )
}

export default ProductMediaPreview
```

The `GET` function is designed to handle incoming HTTP GET requests using the Next.js framework. It first extracts information from the request URL, specifically the `filepath` and `filename`, which are expected to be query parameters. It then attempts to fetch a PDF file from the specified `filepath`. If the PDF is successfully retrieved, it proceeds to convert the PDF content into a buffer.

In case the PDF retrieval fails, for instance, if the file is not found, it returns a response with a "PDF not found" message and a 404 status code, indicating a not found error.

If the PDF is successfully fetched, it defines response headers, specifying that the content type is "application/pdf" and setting the "Content-Disposition" header to control the behavior of file downloads. The `Content-Disposition` header is set to "attachment," and the `filename` parameter is used to suggest a filename for the downloaded PDF.

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
        Download free preview
      </Button>
    </div>
  )
}

export default ProductMediaPreview
```

 The above component displays a preview of a product's media along with a button to download a free preview of that media. The component receives a prop named `media`, which is expected to be of type `ProductMedia`.

Inside the component, there's a `downloadPreview` function that's called when a user clicks the "Download free preview" button. This function constructs a URL for downloading the preview using the `window.location.href` property. It combines the base URL from the environment variable `NEXT_PUBLIC_BASE_URL` with the "/api/download/preview" route and includes query parameters for the file path and file name, which are extracted from the `media` prop.

```javascript
// ...other imports
import ProductMediaPreview from "../product-media-preview"
import { getProductMediaPreviewByVariant } from "@lib/data"

const ProductActions: React.FC<ProductActionsProps> = ({ product }) => {
    // ...other code

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
            // ...other code

      {productMedia && <ProductMediaPreview media={productMedia} />}

      <Button onClick={addToCart}>
        {!inStock ? "Out of stock" : "Add to cart"}
      </Button>
    </div>
  )
}

export default ProductActions
```

This component is responsible for displaying product-related actions, such as adding a product to the cart, and showing product media preview if available. It leverages asynchronous operations to fetch the media data based on the provided `variant`, making it a dynamic and interactive component.

## How to Adjust the Product and Shipping Details

Because product and shipping information differs between digital and physical products, we'll make changes to these sections on the product page as needed.

### How to Add Product Details

I've added product details to the e-book using the product's metadata section in the Medusa admin. Since we're not using the standard attributes, we'll enhance the `ProductInfoTab` component to display any additional metadata we include.

By default, metadata is structured as an object. To make it simpler to create our list of attributes, we'll change it into an array. 

In this case, we'll feature four attributes from the metadata, splitting them into two columns. If you want to show a different number of attributes, you can easily adjust the values within the `slice()` function as needed.

```javascript
// ... other components

const ProductInfoTab = ({ product }: ProductTabsProps) => {
  // map the metadata object to an array
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
                {/* Map the metadata as product information */}
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

// ... other components

```

### How to Adjust the Shipping Details

Shipping information isn't relevant for digital products, so we'll change the content in this tab. You can make any necessary adjustments to the content within the `ShippingInfoTab` component in the same file to better match your store's requirements.

```jaavscript
// ... other components

const ProductTabs = ({ product }: ProductTabsProps) => {
  const tabs = useMemo(() => {
    return [
      {
        label: "Product Information",
        component: <ProductInfoTab product={product} />,
      },
      {
        label: "E-book delivery",
        component: <ShippingInfoTab />,
      },
    ]
  }, [product])
    // ... rest of code
}

// ... other components

const ShippingInfoTab = () => {
  return (
    <Tab.Panel className="text-small-regular py-8">
      <div className="grid grid-cols-1 gap-y-8">
        <div className="flex items-start gap-x-2">
          <FastDelivery />
          <div>
            <span className="font-semibold">Instant delivery</span>
            <p className="max-w-sm">
              Your e-book will be delivered instantly via email. You can also
              download it from your account anytime.
            </p>
          </div>
        </div>
        <div className="flex items-start gap-x-2">
          <Refresh />
          <div>
            <span className="font-semibold">Free previews</span>
            <p className="max-w-sm">
              Get a free preview of the e-book before you buy it. Just click the
              button above to download it.
            </p>
          </div>
        </div>
      </div>
    </Tab.Panel>
  )
}

// ... other components

```

The `ProductTabs` component is used for rendering a set of tabs. The component takes a `product` prop, and it uses the `useMemo` hook to create an array of tab objects. Each tab object consists of a label and a component to be displayed when that tab is active. 

In the above snippet, there are two tabs: "Product Information" and "E-book delivery." The "Product Information" tab displays information about the product using the `ProductInfoTab` component, which we defined earlier. 

The "E-book delivery" tab uses the `ShippingInfoTab` component to display information related to e-book delivery. Inside the `ShippingInfoTab` component, it provides details about the delivery process, mentioning instant delivery via email and the option to download from an account, as well as free e-book previews.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/10p0z2piqkpv60m4jgab.png)
_Product Page_

## How to Simplify the Checkout

Selling digital products doesn't require gathering customers' physical addresses. We only need their first name and email address to deliver the e-book, making the checkout process simpler by removing unnecessary input fields. 

In this example, we'll keep only the first name, last name, country, and email fields, completely removing the billing address section. Keep in mind that your specific requirements may require different input fields.

To start, we'll adjust the checkout types and context by removing any references to values that are no longer needed.

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

In the above snippet, you define TypeScript types for address values and the overall form structure. The `CheckoutContext` is also created to serve as a context for sharing checkout-related data and functions with other components.

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

The `CheckoutProvider` component manages cart data, customer information, form handling, and interactions with payment and shipping methods. It sets up various hooks and functions for these purposes.

You also define an idempotency key which will be used for preventing duplicate requests during payment session creation.

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

In this section of code, several variables and hooks are initialized to facilitate the management of a checkout process. 

We use the `methods` variable to manage the checkout form, with initial values populated by the `mapFormValues` function. The code also sets up mutation functions for updating the payment session and the cart (`setPaymentSessionMutation` and `updateCart`) and tracks their loading states. It retrieves available shipping options and regions using hooks, and it also handles cart resets and region selection. 

It also employs boolean states (`editAddresses` and `sameAsBilling`) to manage whether the user is currently editing addresses and whether the billing address matches the shipping address. 

These components collectively ensure smooth navigation and data management in the checkout process.

```javascript
/**
   * Boolean that indicates if a part of the checkout is loading.
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
   * Boolean that indicates if the checkout is ready to be completed. A checkout is ready to be completed if
   * the user has supplied a email, shipping address, billing address, shipping method, and a method of payment.
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

In the code above, first the `isLoading` boolean is computed using the `useMemo` hook. It reflects whether any part of the checkout is in a loading state. 

This is determined by observing four loading flags: `addingShippingMethod`, `settingPaymentSession`, `updatingCart`, and `completingCheckout`. If any of these flags is `true`, the `isLoading` flag will also be `true`. This indicates that some part of the checkout is currently in progress.

The `readyToComplete` boolean, also computed with `useMemo`, assesses whether the checkout is prepared for completion. 

To be deemed ready, several conditions must be met: there must be a valid `cart` object, an email address, a shipping address, a billing address, a payment session, and at least one shipping method selected. If all these conditions are satisfied, `readyToComplete` will be `true`, signaling that the checkout process is set to be finalized.

Finally, the `shippingMethods` variable is computed using `useMemo`. It is an array of available shipping methods with associated information. It maps the `shipping_options` (if they exist) to an array of objects, each containing a `value`, `label`, and `price`. 

These objects represent the shipping options, their names, and prices, formatted using the `formatAmount` function. This data is used to display and select shipping methods during the checkout process.

```javascript
/**
   * Resets the form when the cart changed.
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
   * Method to set the selected shipping method for the cart. This is called when the user selects a shipping method, such as UPS, FedEx, etc.
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
   * Method to create the payment sessions available for the cart. Uses a idempotency key to prevent duplicate requests.
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
   * Method that calls the createPaymentSession method and updates the cart with the payment session.
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
   * Method to set the selected payment session for the cart. This is called when the user selects a payment provider, such as Stripe, PayPal, etc.
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
   * Method that validates if the cart's region matches the shipping address's region. If not, it will update the cart region.
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
   * Method that sets the addresses and email on the cart.
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
   * Method to complete the checkout process. This is called when the user clicks the "Complete Checkout" button.
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

This code section orchestrates various aspects of an e-commerce checkout process. It manages form state, resets the form when the cart changes, and toggles address editing visibility. It handles the selection of shipping methods, the creation and initialization of payment sessions, and the choice of payment providers. And it ensures that shipping addresses, billing addresses, and email information are set appropriately, and validates the cart's region based on the shipping address. 

It also coordinates the completion of the checkout process, including payment processing and order confirmation. 

All of these functions and data are encapsulated within the `CheckoutProvider` component.

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
 * Method to map the fields of a potential customer and the cart to the checkout form values. Information is assigned with the following priority:
 * 1. Cart information
 * 2. Customer information
 * 3. Default values - null
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

The `useCheckout` hook is used to access the checkout context and form context, typically used in React components. It retrieves the `CheckoutContext` from the context of the application, and it also gets the form context of the checkout form, allowing components to access and utilize these contexts.

The `mapFormValues` function is responsible for mapping and prioritizing information for the checkout form. It takes customer and cart data, along with the current country, and generates values for the checkout form fields. 

It prioritizes data in this order: 1) Cart information, 2) Customer information, and 3) Default values set to null if no information is available. This function helps populate the checkout form with the most relevant data, ensuring a smoother user experience during the checkout process.

Now that the context is updated, we’ll remove the redundant input fields from the checkout form.

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
        <h2>Shipping address</h2>
      </div>
      {isEdit ? (
        <div className="px-8 pb-8">
          <ShippingAddress />
          <Button
            className="max-w-[200px] mt-6"
            onClick={handleSubmit(setAddresses)}
          >
            Continue to delivery
          </Button>
        </div>
      ) : (
        <div>
          <div className="bg-gray-50 px-8 py-6 text-small-regular">
            {cart && cart.shipping_address ? (
              <div className="flex items-start gap-x-8">
                <div className="bg-green-400 rounded-full min-w-[24px] h-6 flex items-center justify-center text-white text-small-regular">
                  ✓
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
                    <button onClick={setEdit}>Edit</button>
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
_Checkout Page_

In the last step, we'll modify the `shipping-details` component to show important information after the order is successfully placed. In this situation, we'll remove any extra details and add the buyer's email address for reference.

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
      <h2 className="text-base-semi">Delivery</h2>
      <div className="my-2">
        <h3 className="text-small-regular text-gray-700">Details</h3>
        <div className="flex flex-col">
          <span>{`${address.first_name} ${address.last_name}`}</span>
          <span>{email}</span>
        </div>
      </div>
      <div className="my-2">
        <h3 className="text-small-regular text-gray-700">Delivery method</h3>
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
_Order Confirmation Page_

## How to Deliver Digital Products

There are various ways to get digital products to customers, like sending a download link by email, adding a download button on the order confirmation page, or giving access through their account.

In all these situations, our main goal is to confirm that only those who've purchased the product can get it. 

To do this, I've set up the backend to create a special code (token) for each digital item in an order. We can use GET `/store/:token` to check the token and give the file to the user. But this method shows the file's web address to the user, which isn't great for preventing piracy. 

So we are going to make a Next API route at `src/app/api/download/main/[token]/route.ts`. This route will handle the token, acting as a middleman to provide the file to the user without revealing where it's stored.

```javascript
import { NextRequest, NextResponse } from "next/server"

export async function GET(
  req: NextRequest,
  { params }: { params: Record<string, any> }
) {
  // Get the token from the URL
  const { token } = params

  // Define the URL to fetch the PDF file data from
  const pdfUrl = `${process.env.NEXT_PUBLIC_MEDUSA_BACKEND_URL}/store/product-media/${token}`

  // Fetch the PDF file data
  const { file, filename } = await fetch(pdfUrl).then((res) => res.json())

  // Handle the case where the token is invalid
  if (!file) return new NextResponse("Invalid token", { status: 401 })

  // Fetch the PDF file
  const pdfResponse = await fetch(file)

  // Handle the case where the PDF could not be fetched
  if (!pdfResponse.ok) return new NextResponse("PDF not found", { status: 404 })

  // Get the PDF content as a buffer
  const pdfBuffer = await pdfResponse.arrayBuffer()

  // Define response headers
  const headers = {
    "Content-Type": "application/pdf",
    "Content-Disposition": `attachment; filename="${filename}"`, // This sets the file name for the download
  }

  // Create a NextResponse with the PDF content and headers
  const response = new NextResponse(pdfBuffer, {
    status: 200,
    headers,
  })

  return response
}

```

This code defines a serverless function for handling HTTP GET requests in a Next.js application. It retrieves a PDF file using a token provided in the URL parameters, fetching the file from an external source. The function ensures the token's validity and the availability of the PDF file. If the token is invalid, it returns a "401 Unauthorized" response. If the PDF is not found, it returns a "404 Not Found" response. 

When the PDF is successfully fetched, it constructs response headers, including the content type as "application/pdf" and a suggested filename for download, and returns the PDF file to the client as a downloadable attachment. This code is typically used to serve PDF files in response to specific GET requests.

We can now link to this API route from the delivery email like this: `{your_store_url}/api/download/main/{token}`.

You can add your own logic to invalidate tokens after a certain time or X number of downloads.

## **Mission Accomplished!**

Congratulations, you've made it! Don't forget to explore more [Recipes](https://docs.medusajs.com/recipes) for further ways to make the most of Medusa.




