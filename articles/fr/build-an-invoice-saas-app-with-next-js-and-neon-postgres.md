---
title: Comment construire une application SaaS de facturation avec Next.js, Resend,
  Clerk et Neon Postgres
subtitle: ''
author: Ankur Tyagi
co_authors: []
series: null
date: '2024-08-01T20:58:01.000Z'
originalURL: https://freecodecamp.org/news/build-an-invoice-saas-app-with-next-js-and-neon-postgres
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/Orange
seo_title: Comment construire une application SaaS de facturation avec Next.js, Resend,
  Clerk et Neon Postgres
---

Yellow-Gradient-Make-Design-Blog-Banner--79-.png
balises:
- nom: full stack
  slug: full-stack
- nom: Next.js
  slug: nextjs
seo_title: null
seo_desc: Dans ce tutoriel, vous apprendrez à construire une application web de facturation qui permet aux utilisateurs d'ajouter leurs informations bancaires, de gérer une liste de clients et de créer et envoyer des factures aux clients. Vous apprendrez également à imprimer et envoyer des composants React en tant que factures et modèles d'e-mails directement depuis l'application vers l'e-mail du client.
---

Dans ce tutoriel, vous apprendrez à construire une application web de facturation qui permet aux utilisateurs d'ajouter leurs informations bancaires, de gérer une liste de clients et de créer et envoyer des factures aux clients. Vous apprendrez également à imprimer et envoyer des composants React en tant que factures et modèles d'e-mails directement depuis l'application vers l'e-mail du client.

Ce sera un excellent projet pour vous aider à apprendre comment assembler des applications full stack et comment créer une application où le backend peut communiquer avec le frontend en temps réel.

Lors de la construction de l'application, vous acquerrez une expérience pratique en travaillant avec les outils de développement suivants :

* [**Neon**](https://neon.tech/docs/introduction) : une base de données Postgres qui nous permet de stocker et de récupérer des données facilement au sein de l'application.
* [**Clerk**](https://clerk.com/) : un système d'authentification complet qui garantit que seules les utilisateurs authentifiés peuvent effectuer des actions spécifiques au sein de l'application.
* [**React-to-print**](https://www.npmjs.com/package/react-to-print) : un package qui nous permet de convertir et d'imprimer des composants React en fichiers PDF.
* [**Resend**](https://resend.com/) **et** [**React Email**](https://react.email/docs/integrations/resend) : pour envoyer des factures numériques magnifiquement conçues directement à l'e-mail des clients.

[Voici le code source](https://github.com/tyaga001/invoice-saas-app-nextjs-neon-postgres) (n'oubliez pas de lui donner une étoile ⭐).

## **Table des matières**

1. [Qu'est-ce que](#heading-questce-que-neon) Neon ?
2. [Construction de l'application de facturation avec Next.js](#heading-construction-de-lapplication-de-facturation-avec-nextjs)
3. [Comment authentifier les utilisateurs avec Clerk](#heading-comment-authentifier-les-utilisateurs-avec-clerk)
4. [Comment ajouter Neon à une application Next.js](#heading-comment-ajouter-neon-a-une-application-nextjs)
5. [Comment configurer le pilote serverless de Neon avec Drizzle ORM dans Next.js](#heading-comment-configurer-le-pilote-serverless-de-neon-avec-drizzle-orm-dans-nextjs)
6. [Création des points de terminaison API pour l'application](#heading-creation-des-points-de-terminaison-api-pour-lapplication)
7. [Comment imprimer et télécharger des factures dans Next.js](#heading-comment-imprimer-et-telecharger-des-factures-dans-nextjs)
8. [Comment envoyer des factures numériques avec Resend et React Email](#id="comment-envoyer-des-factures-numeriques-avec-resend-et-react-email")
9. [Prochaines étapes](#heading-prochaines-etapes)

## **Qu'est-ce que Neon ?**

[Neon](https://github.com/neondatabase/neon) est une base de données Postgres open-source, évolutive et efficace qui sépare le calcul du stockage. Cela signifie que les processus de calcul de la base de données (requêtes, transactions, etc.) sont gérés par un ensemble de ressources (calcul), tandis que les données elles-mêmes sont stockées sur un ensemble de ressources séparé (stockage).

Cette architecture permet une plus grande évolutivité et performance, faisant de Neon un choix solide pour les applications web modernes.

![Neon - une base de données Postgres serverless](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcnJDCduaAEwKDQL2fc2lHsMj6g68thVN_txmoGMyD1ep-x1sWa5d-eiZ3AWjq4xkmGlF7JWxuEvrO9Os5qcEXbzBLep6tCpv-RSuCJjbLwe3hzP9870mfL6LcsH0HvV1x-ymzJ-PU1YjTFuQcihvwEUgeB?key=QrOqhkDtPIneanOaExEDaA)
_[Neon - une base de données Postgres serverless](https://github.com/neondatabase/neon?tab=readme-ov-file)_

## **Construction de l'application de facturation avec Next.js**

Dans cette section, je vais vous guider à travers la construction des différentes pages de l'application de facturation en utilisant Next.js. L'application est divisée en six pages clés, chacune servant un objectif spécifique :

* **Page d'accueil** : Il s'agit de la page de destination. Elle fournit un aperçu de l'application et connecte les utilisateurs à l'application.
* **Page des paramètres** : Ici, les utilisateurs peuvent mettre à jour leurs informations bancaires telles qu'elles seront affichées sur les factures.
* **Page des clients** : Cette page permet aux utilisateurs de gérer leur base de clients, et d'ajouter ou de supprimer des clients si nécessaire.
* **Tableau de bord** : Le cœur de l'application où les utilisateurs peuvent créer de nouvelles factures. Les utilisateurs peuvent sélectionner un client, entrer le titre et la description de la facture, et générer des factures.
* **Page d'historique** : Cette page affiche les factures récemment créées. Elle inclut des liens qui permettent aux utilisateurs de prévisualiser chaque facture, offrant un moyen rapide de revoir les transactions passées.
* **Page d'impression et d'envoi de facture** : Cette page permet aux utilisateurs d'imprimer et d'envoyer des factures aux clients.

Avant de continuer, créez un projet Next.js TypeScript en exécutant le code suivant dans votre terminal :

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Raleway,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">npx create-next-app invoice-app-</span><span style="font-size:11pt;font-family:Raleway,sans-serif;color:#fcc28c;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">avec</span><span style="font-size:11pt;font-family:Raleway,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">-neon</span></p></td></tr></tbody></table>

Ajoutez un fichier **types.d.ts** dans le dossier du projet. Il contiendra les déclarations de types pour les variables au sein de l'application.

```javascript
interface Item {
    id: string;
    name: string;
    cost: number;
    quantity: number;
    price: number;
}

interface Invoice {
    id?: string,
    created_at?: string,
    user_id:  string,
    customer_id: number,
    title: string,
    items: string,
    total_amount: number,
}

interface Customer {
    user_id: string,
    name: string,
    email: string,
    address: string
}

interface BankInfo {
    user_id: string,
    account_name: string,
    account_number: number,
    bank_name: string,
    currency: string
}
```

### **Page d'accueil**

Copiez le code suivant dans le fichier **app/page.tsx**. Il affiche des informations brèves sur l'application et un bouton qui redirige les utilisateurs vers le tableau de bord ou la page de connexion, selon leur statut d'authentification.

```javascript
import Link from "next/link";

export default function Home() {
  return (
    <main className='w-full'>
      <section className='p-8 h-[90vh] md:w-2/3 mx-auto text-center w-full flex flex-col items-center justify-center'>
        <h2 className='text-3xl font-bold mb-4 md:text-4xl'>
          Créer des factures pour vos clients
        </h2>
        <p className='opacity-70 mb-4 text-sm md:text-base leading-loose'>
          Invoicer est un logiciel de facturation en ligne qui vous aide à créer et
          à imprimer des factures professionnelles pour vos clients gratuitement ! Gardez votre
          entreprise et vos clients avec un seul logiciel de facturation.
        </p>
        <Link
          href='/dashboard'
          className='rounded w-[200px] px-2 py-3 bg-blue-500 text-gray-50'
        >
          SE CONNECTER
        </Link>
      </section>
    </main>
  );
}

```

![Invoice-app-home-page](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfxl_8niZbdRmGGgjCG66VCVO3dIZHO-oQ4TtSDjBRFqrU7qb6yGrVOBK4xqPYeFpYgddmDPA3hcw8X5bE1eqtdUP2Un9BHn_IM2CsjII17qap-VnDD8Qyo6ZW0TwFkTgWWNxXmxST6xcvr-KxIRYjK_2xg?key=QrOqhkDtPIneanOaExEDaA)
_Invoice-app-home-page_

### **Page des paramètres**

Ajoutez un dossier **settings** contenant un fichier **page.tsx** dans le répertoire de l'application Next.js et copiez le code suivant dans le fichier :

```javascript
"use client";
import { ChangeEvent, useEffect, useState, useCallback } from "react";
import SideNav from "@/app/components/SideNav";

export default function Settings() {
    //👇🏻 informations bancaires par défaut
    const [bankInfo, setBankInfo] = useState({
        account_name: "",
        account_number: 1234567890,
        bank_name: "",
        currency: "",
 });

    //👇🏻 informations bancaires provenant des entrées du formulaire
    const [inputBankInfo, setInputBankInfo] = useState({
        accountName: "",
        accountNumber: 1234567890,
        bankName: "",
        currency: "",
 });

    //👇🏻 met à jour l'état des entrées du formulaire
    const handleUpdateBankInfo = (
        e: ChangeEvent<HTMLInputElement | HTMLSelectElement>
 ) => {
        const { name, value } = e.target;
        setInputBankInfo((prevState) => ({
 ...prevState,
 [name]: value,
 }));
 };

    //👇🏻 met à jour les informations bancaires
    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        console.log("Tente de mettre à jour les informations bancaires...");
 };
return ()
}
```

Le code ci-dessus montre que la page affiche les informations bancaires de l'utilisateur et permet également à l'utilisateur de les mettre à jour si nécessaire.

Retournez les éléments UI suivants depuis le composant :

```javascript
export default function Settings() {
  //👇🏻 états et fonctions React

  return (
    <div className='w-full'>
      <main className='min-h-[90vh] flex items-start'>
        <SideNav />

        <div className='md:w-5/6 w-full h-full p-6'>
          <h2 className='text-2xl font-bold'>Informations bancaires</h2>
          <p className='opacity-70 mb-4'>
            Mettez à jour les informations de votre compte bancaire
          </p>

          <div className='flex md:flex-row flex-col items-start justify-between w-full md:space-x-4'>
            <section className='md:w-1/3 w-full bg-blue-50 h-full p-3 rounded-md space-y-3'>
              <p className='text-sm opacity-75'>
                Nom du compte : {bankInfo.account_name}
              </p>
              <p className='text-sm opacity-75'>
                Numéro de compte : {bankInfo.account_number}
              </p>
              <p className='text-sm opacity-75'>
                Nom de la banque : {bankInfo.bank_name}
              </p>
              <p className='text-sm opacity-75'>
                Devise : {bankInfo.currency}
              </p>
            </section>
            
            <form
              className='md:w-2/3 w-full p-3 flex flex-col'
              method='POST'
              onSubmit={handleSubmit}
            >
              <label htmlFor='accountName' className='text-sm'>
                Nom du compte
              </label>
              <input
                type='text'
                name='accountName'
                id='accountName'
                className='border-[1px] p-2 rounded mb-3'
                required
                value={inputBankInfo.accountName}
                onChange={handleUpdateBankInfo}
              />

              <label htmlFor='accountNumber' className='text-sm'>
                Numéro de compte
              </label>
              <input
                type='number'
                name='accountNumber'
                id='accountNumber'
                className='border-[1px] p-2 rounded mb-3'
                required
                value={inputBankInfo.accountNumber}
                onChange={handleUpdateBankInfo}
              />

              <label htmlFor='bankName' className='text-sm'>
                Nom de la banque
              </label>
              <input
                type='text'
                name='bankName'
                id='bankName'
                className='border-[1px] p-2 rounded mb-3'
                required
                value={inputBankInfo.bankName}
                onChange={handleUpdateBankInfo}
              />

              <label htmlFor='currency' className='text-sm'>
                Devise
              </label>
              <select
                name='currency'
                id='currency'
                className='border-[1px] p-2 rounded mb-3'
                required
                value={inputBankInfo.currency}
                onChange={handleUpdateBankInfo}
              >
                <option value=''>Sélectionner</option>
                <option value='$'>USD</option>
                <option value='€'>EUR</option>
                <option value='£'>GBP</option>
              </select>
              <div className='flex items-center justify-end'>
                <button
                  type='submit'
                  className='bg-blue-500 text-white p-2 w-[200px] rounded'
                >
                  Mettre à jour les informations bancaires
                </button>
              </div>
            </form>
          </div>
        </div>
      </main>
    </div>
  );
}

```

![Invoice-app-settings-page](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfjj47wp06nbinvyDFg1Zl8udWgJWenfeu3wQ_b8_6KWP9bJAH69wCMsX5v0_XVm5-PF2K9mR_zyP7tJHLvmp2L2aLopuRQ8NiAVUVEa6WcSKV3gQOjGb2Va0227mk5OTCxQrro1uIQdwE7vyWI-rnqUkC6?key=QrOqhkDtPIneanOaExEDaA)
_Invoice-app-settings-page_

### **Page des clients**

Ajoutez un dossier **customers** contenant un fichier **page.tsx** dans le répertoire Next.js et copiez le code suivant dans le fichier :

```javascript
import CustomersTable from "../components/CustomersTable";
import { useCallback, useEffect, useState } from "react";
import SideNav from "@/app/components/SideNav";

export default function Customers() {
  const [customerName, setCustomerName] = useState<string>("");
  const [customerEmail, setCustomerEmail] = useState<string>("");
  const [customerAddress, setCustomerAddress] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [customers, setCustomers] = useState([]);

  const handleAddCustomer = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // 👉🏻 createCustomer();
  };

  return (
    <div className='w-full'>
      <main className='min-h-[90vh] flex items-start'>
        <SideNav />
        <div className='md:w-5/6 w-full h-full p-6'>
          <h2 className='text-2xl font-bold'>Clients</h2>
          <p className='opacity-70 mb-4'>Créer et voir tous vos clients</p>

          <form className='w-full' onSubmit={handleAddCustomer} method='POST'>
            <div className='w-full flex items-center space-x-4 mb-3'>
              <section className='w-1/2'>
                <label>Nom du client</label>
                <input
                  type='text'
                  className='w-full p-2 border border-gray-200 rounded-sm'
                  value={customerName}
                  required
                  onChange={(e) => setCustomerName(e.target.value)}
                />
              </section>

              <section className='w-1/2'>
                <label>Adresse e-mail</label>
                <input
                  type='email'
                  className='w-full p-2 border border-gray-200 rounded-sm'
                  value={customerEmail}
                  onChange={(e) => setCustomerEmail(e.target.value)}
                  required
                />
              </section>
            </div>
            <label htmlFor='address'>Adresse de facturation</label>
            <textarea
              name='address'
              id='address'
              rows={3}
              className='w-full p-2 border border-gray-200 rounded-sm'
              value={customerAddress}
              onChange={(e) => setCustomerAddress(e.target.value)}
              required
            />
            <button
              className='bg-blue-500 text-white p-2 rounded-md mb-6'
              disabled={loading}
            >
              {loading ? "Ajout..." : "Ajouter le client"}
            </button>
          </form>

          <CustomersTable customers={customers} />
        </div>
      </main>
    </div>
  );
}

```

Le code ci-dessus permet aux utilisateurs de voir, créer et supprimer des clients de l'application.

![Invoice-app-customer-page](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdd4_PjRZlb7a65BP3PJIItYL0b7GuwMqwiMstNFqPsOl7n5lNIehqAZFK33YPMSHBtbPeRg-LwRmMwv0ASz1PBfC9Bo8YWaNGJcO_heST76rrsB7R6c0PDeXeC5B9AH2TfWriGj4SNC7FGO1BcEm8cEwol?key=QrOqhkDtPIneanOaExEDaA)
_Invoice-app-customer-page_

### **Page du tableau de bord**

Créez un dossier **dashboard** contenant un fichier **page.tsx** dans le répertoire de l'application Next.js et copiez le code suivant dans le fichier :

```javascript
"use client";
import InvoiceTable from "@/app/components/InvoiceTable";
import React, { useState, useEffect, useCallback } from "react";
import { useRouter } from "next/navigation";
import SideNav from "@/app/components/SideNav";

export default function Dashboard() {
  const { isLoaded, isSignedIn, user } = useUser();
  const [itemList, setItemList] = useState<Item[]>([]);
  const [customer, setCustomer] = useState<string>("");
  const [invoiceTitle, setInvoiceTitle] = useState<string>("");
  const [itemCost, setItemCost] = useState<number>(1);
  const [itemQuantity, setItemQuantity] = useState<number>(1);
  const [itemName, setItemName] = useState<string>("");
  const [customers, setCustomers] = useState([]);
  const router = useRouter();

  const handleAddItem = (e: React.FormEvent) => {
    e.preventDefault();
    if (itemName.trim() && itemCost > 0 && itemQuantity >= 1) {
      setItemList([
        ...itemList,
        {
          id: Math.random().toString(36).substring(2, 9),
          name: itemName,
          cost: itemCost,
          quantity: itemQuantity,
          price: itemCost * itemQuantity,
        },
      ]);
    }

    setItemName("");
    setItemCost(0);
    setItemQuantity(0);
  };

  const getTotalAmount = () => {
    let total = 0;
    itemList.forEach((item) => {
      total += item.price;
    });
    return total;
  };

  const handleFormSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    //👉🏻 createInvoice();
  };

  return (
    <div className='w-full'>
      <main className='min-h-[90vh] flex items-start'>
        <SideNav />
        <div className='md:w-5/6 w-full h-full p-6'>
          <h2 className='font-bold text-2xl mb-3'>Ajouter une nouvelle facture</h2>

          <form className='w-full flex flex-col' onSubmit={handleFormSubmit}>
            <label htmlFor='customer'>Client</label>
            <select
              className='border-[1px] p-2 rounded-sm mb-3'
              required
              value={customer}
              onChange={(e) => setCustomer(e.target.value)}
            >
              {customers.map((customer: any) => (
                <option key={customer.id} value={customer.name}>
                  {customer.name}
                </option>
              ))}
            </select>

            <label htmlFor='title'>Titre</label>
            <input
              className='border-[1px] rounded-sm mb-3 py-2 px-3'
              required
              value={invoiceTitle}
              onChange={(e) => setInvoiceTitle(e.target.value)}
            />

            <div className='w-full flex justify-between flex-col'>
              <h3 className='my-4 font-bold'>Liste des articles</h3>

              <div className='flex space-x-3'>
                <div className='flex flex-col w-1/4'>
                  <label htmlFor='itemName' className='text-sm'>
                    Nom
                  </label>
                  <input
                    type='text'
                    name='itemName'
                    placeholder='Nom'
                    className='py-2 px-4 mb-6 bg-gray-100'
                    value={itemName}
                    onChange={(e) => setItemName(e.target.value)}
                  />
                </div>

                <div className='flex flex-col w-1/4'>
                  <label htmlFor='itemCost' className='text-sm'>
                    Coût
                  </label>
                  <input
                    type='number'
                    name='itemCost'
                    placeholder='Coût'
                    className='py-2 px-4 mb-6 bg-gray-100'
                    value={itemCost}
                    onChange={(e) => setItemCost(Number(e.target.value))}
                  />
                </div>

                <div className='flex flex-col justify-center w-1/4'>
                  <label htmlFor='itemQuantity' className='text-sm'>
                    Quantité
                  </label>
                  <input
                    type='number'
                    name='itemQuantity'
                    placeholder='Quantité'
                    className='py-2 px-4 mb-6 bg-gray-100'
                    value={itemQuantity}
                    onChange={(e) => setItemQuantity(Number(e.target.value))}
                  />
                </div>

                <div className='flex flex-col justify-center w-1/4'>
                  <p className='text-sm'>Prix</p>
                  <p className='py-2 px-4 mb-6 bg-gray-100'>
                    {Number(itemCost * itemQuantity).toLocaleString("en-US")}
                  </p>
                </div>
              </div>
              <button
                className='bg-blue-500 text-gray-100 w-[100px] p-2 rounded'
                onClick={handleAddItem}
              >
                Ajouter un article
              </button>
            </div>

            <InvoiceTable itemList={itemList} />
            <button
              className='bg-blue-800 text-gray-100 w-full p-4 rounded my-6'
              type='submit'
            >
              ENREGISTRER ET PRÉVISUALISER LA FACTURE
            </button>
          </form>
        </div>
      </main>
    </div>
  );
}

```

Le code ci-dessus affiche un formulaire qui accepte les détails de la facture, tels que le nom du client, le titre de la facture et la liste des articles nécessaires pour créer une facture.

![Invoice-app-dashboard](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcUHH9gL0R6IRq-WSuKxwiTyNLM0Hae4uqYjIPXBswcEDG_zNfk7-QBLGj1Ht-RC5zbPkp6JddjSgIEwvkNeID6756C7i_uA-_vq8kgTDU-tuA6FqORWxtaJ8Jc53XdOULfmGOmEHSsiGRbTuXuth957Hkt?key=QrOqhkDtPIneanOaExEDaA)
_Invoice-app-dashboard_

### **Page d'historique**

Créez un dossier **history** contenant un fichier **page.tsx** dans le répertoire de l'application Next.js et copiez le code suivant dans le fichier :

```javascript
"use client";
import { useState, useEffect, useCallback } from "react";
import Link from "next/link";
import SideNav from "@/app/components/SideNav";

export default function History() {
  const { isLoaded, isSignedIn, user } = useUser();
  const [invoices, setInvoices] = useState<Invoice[]>([]);

  return (
    <div className='w-full'>
      <main className='min-h-[90vh] flex items-start'>
        <SideNav />
        <div className='md:w-5/6 w-full h-full p-6'>
          <h2 className='text-2xl font-bold'>Historique</h2>
          <p className='opacity-70 mb-4'>Voir toutes vos factures et leur statut</p>

          {invoices.map((invoice) => (
            <div
              className='bg-blue-50 w-full mb-3 rounded-md p-3 flex items-center justify-between'
              key={invoice.id}
            >
              <div>
                <p className='text-sm text-gray-500 mb-2'>
                  Facture - #0{invoice.id} émise à{" "}
                  <span className='font-bold'>{invoice.customer_id}</span>
                </p>
                <h3 className='text-lg font-bold mb-[1px]'>
                  {Number(invoice.total_amount).toLocaleString()}
                </h3>
              </div>
              <Link
                href={{
                  pathname: `/invoices/${invoice.id}`,
                  query: { customer: invoice.customer_id },
                }}
                className='bg-blue-500 text-blue-50 rounded p-3'
              >
                Aperçu
              </Link>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}

```

Le code ci-dessus affiche les factures récemment créées et permet aux utilisateurs de les prévisualiser si nécessaire.

![Invoice-app-history-page](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfn94sQF287nrzVJb3FB3rO3zkfidF87Amtx4xliIM93iK_I30dAEZEZaDrt7YMX2e_Zi2o0lMJYHvqudFrlQA880nL8NbO0Rsii_n_sdMVV1Lp6DHbOT7eo-RLhAM7VUfxekxVyXjlpzqSn5LaX28_vZOz?key=QrOqhkDtPIneanOaExEDaA)
_Invoice-app-history-page_

## **Comment authentifier les utilisateurs avec Clerk**

[Clerk](https://github.com/clerkinc) est une plateforme complète de gestion des utilisateurs qui vous permet d'ajouter diverses formes d'authentification à vos applications logicielles. Elle fournit des composants UI et des API faciles à utiliser et flexibles qui peuvent être intégrés de manière transparente dans votre application.

Installez le [Clerk Next.js SDK](https://clerk.com/docs/quickstarts/nextjs) en exécutant le code suivant dans votre terminal :

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Raleway,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">npm install @clerk/nextjs</span></p></td></tr></tbody></table>

Créez un fichier `middleware.ts` dans le dossier src de Next.js et copiez le code suivant dans le fichier :

```javascript
import { clerkMiddleware, createRouteMatcher } from "@clerk/nextjs/server";

// la fonction createRouteMatcher accepte un tableau de routes à protéger
const protectedRoutes = createRouteMatcher([
    "/customers",
    "/settings",
    "/dashboard",
    "/history",
    "/invoices(.*)",
]);

// protège la route
export default clerkMiddleware((auth, req) => {
    if (protectedRoutes(req)) {
        auth().protect();
 }
});

export const config = {
    matcher: ["/((?!.*\\..*|_next).*)", "/", "/(api|trpc)(.*)"],
};
```

La fonction **`createRouteMatcher()`** accepte un tableau contenant des routes à protéger des utilisateurs non authentifiés, et la fonction **`clerkMiddleware()`** garantit que les routes sont protégées.

Ensuite, importez les composants Clerk suivants dans le fichier **app/layout.tsx** et mettez à jour la fonction **`RootLayout`** comme indiqué ci-dessous :

```javascript
import {
    ClerkProvider,
    SignInButton,
    SignedIn,
    SignedOut,
    UserButton,
} from "@clerk/nextjs";
import Link from "next/link";

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
 <ClerkProvider>
 <html lang='en'>
 <body className={inter.className}>
 <nav className='flex justify-between items-center h-[10vh] px-8 border-b-[1px]'>
 <Link href='/' className='text-xl font-extrabold text-blue-700'>
 Invoicer
 </Link>
 <div className='flex items-center gap-5'>
                            {/*-- si l'utilisateur est déconnecté --*/}
 <SignedOut>
 <SignInButton mode='modal' />
 </SignedOut>
                            {/*-- si l'utilisateur est connecté --*/}
 <SignedIn>
 <Link href='/dashboard' className=''>
 Tableau de bord
 </Link>
 <UserButton showName />
 </SignedIn>
 </div>
 </nav>

                    {children}
 </body>
 </html>
 </ClerkProvider>
 );
}
```

Lorsque l'utilisateur n'est pas connecté, le composant [Sign in button](https://clerk.com/docs/components/unstyled/sign-in-button) est rendu.

![Clerk-Auth-Signup-Page](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe7-OxFwVNEjJ_vvM9zo7j-d1jVKcYj1EXoV-Kk5_WR3k3Ie3h1wXnr2VB_Df5rbc4OJ_uK3wtJ4g1iTfYNrsOqTDu4oMrljRNxhh0xQCVMkSyO_zrrUxmBaT-iBgAkiAKk4Tkoj17stTyY-Y3VP72BbjFL?key=QrOqhkDtPIneanOaExEDaA)
_Clerk-Auth-Signup-Page_

Ensuite, après s'être connecté à l'application, le [User Button component](https://clerk.com/docs/components/user/user-button) de Clerk et un lien vers le tableau de bord sont affichés.

Ensuite, créez un [compte Clerk](https://clerk.com/) et ajoutez un nouveau projet d'application.

![Clerk-Auth-Project-Page](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcu_CxSCF4Gy9AxT0QGVt8Ia1xcU3XrqLsOMxi9v1mqs7qMIHXQGPVHabyfIUkJ9YfyzkXcy-7Q85fSUz9_r1FPxY_9R8RtFuMxiR0CeNZjLqlgkNLXLG43L_EIdeyK1Dwl5tJd7PvBrG7LeHb-NJ8-I0o?key=QrOqhkDtPIneanOaExEDaA)
_Clerk-Auth-Project-Page_

Sélectionnez **email** comme méthode d'authentification et créez le projet Clerk.

Enfin, ajoutez vos clés publiques et secrètes Clerk dans le fichier **.env.local**.

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=&lt;votre_clé_publique&gt;</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">CLERK_SECRET_KEY=&lt;votre_clé_secrète&gt;</span></p></td></tr></tbody></table>

Clerk offre diverses façons de [lire les données de l'utilisateur](https://clerk.com/docs/references/nextjs/read-session-data) sur le client et le serveur, ce qui est essentiel pour identifier les utilisateurs au sein de l'application.

## **Comment ajouter Neon à une application Next.js**

[Neon](https://github.com/tyaga001/awesome-neon) prend en charge plusieurs frameworks et bibliothèques et fournit une documentation claire et détaillée sur l'ajout de Neon à ceux-ci. Le pilote serverless de Neon vous permet de vous connecter à Neon et d'interagir avec lui dans une application Next.js.

Avant de continuer, créons un [compte Neon et un projet](https://neon.tech/docs/guides/nextjs).

![Neon-postgres-all-project-dashboard](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdbDT3O2Kdn_GAbeMGyegKJB6dDkFnXRC9YyW_YTkGTyZuC3GYpb9ohemo3iatRjq7Cpx0jnwCnY5MXy0xkK6Nu7hf18rvZZOIsRXJi3zZUsTTAaOwDpN61WtnFVpIclISdBDZquVFtEFG8ZB9tg6bVg2wD?key=QrOqhkDtPIneanOaExEDaA)
_Neon-postgres-all-project-dashboard_

Dans votre tableau de bord de projet, vous trouverez une chaîne de connexion à la base de données. Vous l'utiliserez pour interagir avec votre base de données Neon.

![Neon-project-dashboard](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf62euRKYINnsRnREwseLaCeBpGc9kKGTk1sIC4xO36QGpwCaYUhLva-71rrhJ_Z7sb9v1dN0Tz-3DtCCrKPy62duD2afc5MDVMpLi9wgvtw-rKg3o4huDZIbbxxSiwuftKwmtq6iVNAeQwkx1OohSKAA4b?key=QrOqhkDtPIneanOaExEDaA)
_Neon-project-dashboard_

Ensuite, installez le package Neon Serverless dans le projet Next.js :

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">npm install </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#fc9b9b;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">@neondatabase</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">/serverless</span></p></td></tr></tbody></table>

Copiez votre chaîne de connexion à la base de données dans le fichier **.env.local**.

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">NEON_DATABASE_URL=</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#a2fca2;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">"postgres://&lt;user&gt;:&lt;password&gt;@&lt;endpoint_hostname&gt;.neon.tech:&lt;port&gt;/&lt;dbname&gt;?sslmode=require"</span></p></td></tr></tbody></table>

Créez un dossier **db** contenant un fichier **index.ts** dans le répertoire de l'application Next.js et copiez le code suivant dans le fichier :

```javascript
import { neon } from '@neondatabase/serverless';

if (!process.env.NEON_DATABASE_URL) {
  throw new Error('NEON_DATABASE_URL doit être une chaîne de connexion Neon postgres')
}

export const getDBVersion = async() => {
    const sql = neon(process.env.NEON_DATABASE_URL!);
    const response = await sql`SELECT version()`;
    return { version: response[0].version }
}
```

Convertissez le fichier **app/page.tsx** en un composant serveur et exécutez la fonction **`getDBVersion()`** :

```javascript
import { getDBVersion } from "./db";

export default async function Home() {
    const { version } = await getDBVersion();
    console.log({version})
    
   return (<div>{/** -- Éléments UI -- */}</div>)

}
```

La fonction **`getDBVersion()`** établit une connexion avec la base de données Neon et nous permet d'exécuter des requêtes SQL en utilisant le client Postgres. Cette fonction retourne la version de la base de données, qui est ensuite enregistrée dans la console.

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">{</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">version: </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#a2fca2;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">'PostgreSQL 16.3 on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit'</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">}</span></p></td></tr></tbody></table>

Félicitations, vous avez ajouté Neon à votre application Next.js avec succès.

Cependant, interagir avec la base de données Neon en écrivant directement des requêtes SQL peut nécessiter un apprentissage supplémentaire ou introduire des complexités pour les développeurs qui ne sont pas familiers avec SQL. Cela peut également entraîner des erreurs ou des problèmes de performance lors de l'exécution de requêtes complexes.

C'est pourquoi Neon prend en charge les ORM de base de données tels que Drizzle ORM, qui fournissent une interface de niveau supérieur pour interagir avec la base de données. [Drizzle ORM](https://orm.drizzle.team/docs/overview) vous permet d'écrire des fonctions de requête complexes et d'interagir facilement avec la base de données en utilisant TypeScript.

## **Comment configurer le pilote serverless de Neon avec Drizzle ORM dans Next.js**

Drizzle ORM vous permet de requêter des données et d'effectuer diverses opérations sur la base de données en utilisant des commandes de requête TypeScript simples. Il est léger, sécurisé et facile à utiliser.

Tout d'abord, vous devrez installer le [Drizzle Kit](https://orm.drizzle.team/kit-docs/overview) et le package [Drizzle ORM](https://orm.drizzle.team/docs/overview).

Drizzle Kit vous permet de gérer le schéma de la base de données et les migrations.

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">npm i drizzle-orm</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">npm i -D drizzle-kit</span></p></td></tr></tbody></table>

À l'intérieur du dossier **db**, ajoutez un fichier **actions.ts** et **schema.ts** :

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">cd db</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">touch actions.ts schema.ts</span></p></td></tr></tbody></table>

Le fichier actions.ts contiendra les requêtes et opérations de base de données nécessaires, tandis que le fichier schema.ts définira le schéma de la base de données pour l'application de facturation.

### **Conception de la base de données pour l'application de facturation**

Rappelons que les utilisateurs peuvent ajouter des clients, mettre à jour leurs informations bancaires et créer des factures au sein de l'application. Vous devez donc créer des tables de base de données pour les données dans Neon.

L'ID de l'utilisateur sera utilisé comme clé étrangère pour identifier chaque ligne de données appartenant à un utilisateur spécifique.

Copiez le code suivant dans le fichier **db/schema.ts** :

```javascript
import {  text, serial, pgTable, timestamp, numeric } from "drizzle-orm/pg-core";

//👇🏻 table des factures avec ses types de colonnes
export const invoicesTable = pgTable("invoices", {
    id: serial("id").primaryKey().notNull(),
    owner_id: text("owner_id").notNull(),
    customer_id: text("customer_id").notNull(),
    title: text("title").notNull(),
    items: text("items").notNull(),
    created_at: timestamp("created_at").defaultNow(),
    total_amount: numeric("total_amount").notNull(),
});

//👇🏻 table des clients avec ses types de colonnes
export const customersTable = pgTable("customers", {
    id: serial("id").primaryKey().notNull(),
    created_at: timestamp("created_at").defaultNow(),
    owner_id: text("owner_id").notNull(),
    name: text("name").notNull(),
    email: text("email").notNull(),
    address: text("address").notNull(),
})

//👇🏻 table des informations bancaires avec ses types de colonnes
export const bankInfoTable = pgTable("bank_info", {
    id: serial("id").primaryKey().notNull(),
    owner_id: text("owner_id").notNull().unique(),
    bank_name: text("bank_name").notNull(),
    account_number: numeric("account_number").notNull(),
    account_name: text("account_name").notNull(),
    created_at: timestamp("created_at").defaultNow(),
    currency: text("currency").notNull(),
})
```

Le fichier actions.ts contiendra les différentes opérations de base de données nécessaires au sein de l'application. Tout d'abord, ajoutez le code suivant au fichier :

```javascript
import { invoicesDB, customersDB, bankInfoDB } from ".";
import { invoicesTable, customersTable, bankInfoTable } from './schema';
import { desc, eq } from "drizzle-orm";

//👇🏻 ajoute une nouvelle ligne à la table des factures
export const createInvoice = async (invoice: any) => {
    await invoicesDB.insert(invoicesTable).values({
    owner_id: invoice.user_id,
    customer_id: invoice.customer_id,
    title: invoice.title,
    items: invoice.items,
    total_amount: invoice.total_amount,
 });
};

//👇🏻 obtient toutes les factures de l'utilisateur
export const getUserInvoices = async (user_id: string) => {
    return await invoicesDB.select().from(invoicesTable).where(eq(invoicesTable.owner_id, user_id)).orderBy(desc(invoicesTable.created_at));
};

//👇🏻 obtient une seule facture
export const getSingleInvoice = async (id: number) => {
    return await invoicesDB.select().from(invoicesTable).where(eq(invoicesTable.id, id));
};
```

La fonction **`createInvoice`** accepte les détails de la facture en tant que paramètre et ajoute une nouvelle ligne de données à sa table de factures. La fonction **`getUserInvoices`** filtre la table et retourne un tableau de factures créées par l'utilisateur. La fonction **`getSingleInvoice`** accepte un ID de facture, filtre la table et retourne la facture avec un ID correspondant.

Ajoutez les fonctions suivantes au fichier db/actions :

```javascript
//👇🏻 obtient la liste des clients
export const getCustomers = async (user_id: string) => {
    return await customersDB.select().from(customersTable).where(eq(customersTable.owner_id, user_id)).orderBy(desc(customersTable.created_at));
};

//👇🏻 obtient un seul client
export const getSingleCustomer = async (name: string) => {
    return await customersDB.select().from(customersTable).where(eq(customersTable.name, name));
};

//👇🏻 ajoute une nouvelle ligne à la table des clients
export const addCustomer = async (customer: Customer) => {
    await customersDB.insert(customersTable).values({
        owner_id: customer.user_id,
        name: customer.name,
        email: customer.email,
        address: customer.address,
 });
};

//👇🏻 supprime un client
export const deleteCustomer = async (id: number) => {
  await customersDB.delete(customersTable).where(eq(customersTable.id, id));
};
```

Ce code permet aux utilisateurs de récupérer tous leurs clients de la base de données, d'obtenir un seul client via son ID, d'ajouter de nouveaux clients et de supprimer des clients de la table **customers**.

Enfin, ajoutez ceci également au fichier **db/actions.ts** :

```javascript
//👇🏻 obtient les informations bancaires de l'utilisateur
export const getUserBankInfo = async (user_id: string) => {
    return await bankInfoDB.select().from(bankInfoTable).where(eq(bankInfoTable.owner_id, user_id));
};

//👇🏻 met à jour la table des informations bancaires
export const updateBankInfo = async (info: any) => {
await bankInfoDB.insert(bankInfoTable)
 .values({
        owner_id: info.user_id,
        bank_name: info.bank_name,
        account_number: info.account_number,
        account_name: info.account_name,
        currency: info.currency,
 })
 .onConflictDoUpdate({
            target: bankInfoTable.owner_id,
            set: {
                bank_name: info.bank_name,
                account_number: info.account_number,
                account_name: info.account_name,
                currency: info.currency,
 },
 });
};
```

La fonction **`getUserBankInfo`** récupère les informations bancaires de l'utilisateur depuis la base de données, tandis que la fonction **`updateBankInfo`** les met à jour. Si l'utilisateur en a déjà, la fonction les met à jour avec les nouveaux détails, sinon elle crée une nouvelle entrée.

Ensuite, mettez à jour le fichier **db/index.ts** pour vous connecter à la base de données Neon et exporter l'instance Drizzle pour chaque table. Cela sera utilisé pour exécuter des requêtes SQL sécurisées contre votre base de données Postgres hébergée sur Neon.

```javascript
import { neon } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-http';
import { invoicesTable, customersTable, bankInfoTable } from './schema';

if (!process.env.NEON_DATABASE_URL) {
  throw new Error('DATABASE_URL doit être une chaîne de connexion Neon postgres')
}
const sql = neon(process.env.NEON_DATABASE_URL!);


export const invoicesDB = drizzle(sql, {
  schema: { invoicesTable }
});

export const customersDB = drizzle(sql, {
  schema: { customersTable }
});

export const bankInfoDB = drizzle(sql, {
  schema: { bankInfoTable }
});
```

Créez un fichier **drizzle.config.ts** à la racine du dossier Next.js et ajoutez la configuration suivante. Assurez-vous d'installer le package [Dotenv](https://www.npmjs.com/package/dotenv).

```javascript
import type { Config } from "drizzle-kit";
import * as dotenv from "dotenv";

dotenv.config();

if (!process.env.NEON_DATABASE_URL)
    throw new Error("NEON DATABASE_URL non trouvé dans l'environnement");

export default {
    schema: "./src/app/db/schema.ts",
    out: "./src/app/db/migrations",
    dialect: "postgresql",
    dbCredentials: {
        url: process.env.NEON_DATABASE_URL,
 },
    strict: true,
} satisfies Config;
```

Le fichier **drizzle.config.ts** contient toutes les informations sur votre connexion à la base de données, le dossier de migration et les fichiers de schéma.

Enfin, mettez à jour le fichier **package.json** pour inclure les commandes Drizzle Kit pour générer les migrations de la base de données et créer les tables.

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">{</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#a2fca2;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">"scripts"</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> : {</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#a2fca2;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">"migrate"</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">: </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#a2fca2;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">"npx drizzle-kit generate -- dotenv_config_path='.env.local'"</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">,</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#a2fca2;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">"db-create"</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">: </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#a2fca2;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">"npx drizzle-kit push -- dotenv_config_path='.env.local'"</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"> }</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">}</span></p></td></tr></tbody></table>

Vous pouvez maintenant exécuter **`npm run db-create`** pour pousser les tables de la base de données vers la console Neon.

![Neon-tables-dashboard](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdK9dJHITFXRrqOiK6pFL7hUZtvinCaymedYlOuWu9QUOOEEmKuweQ1z0MflHyhdsffeNJ7HGnFLlm9QQ10rH8q6gwGWB7nr-S6GDyCiHmkNAZCfJNhiwPuBY193H0W9nFLDUeLt8zaethyZ2bU9pMOKO5g?key=QrOqhkDtPIneanOaExEDaA)
_Neon-tables-dashboard_

## **Création des points de terminaison API pour l'application**

Dans la section précédente, vous avez créé les fonctions nécessaires pour interagir avec la base de données. Dans cette section, vous apprendrez à créer les points de terminaison API pour chaque opération de base de données.

Tout d'abord, créez un dossier `api` dans le répertoire de l'application Next.js. Il contiendra toutes les routes API de l'application.

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">cd app</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">mkdir api</span></p></td></tr></tbody></table>

Ajoutez un dossier **`bank-info`** contenant un **route.ts** dans le dossier `api`. Cela signifie que la route API (**/api/bank-info**) gérera la mise à jour et la récupération des informations bancaires de l'utilisateur.

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">cd api</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">mkdir bank-info && cd bank-info</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">touch route.ts</span></p></td></tr></tbody></table>

Copiez le code suivant dans le fichier /bank-info/route.ts. La méthode de requête POST met à jour les informations bancaires de l'utilisateur et retourne une réponse, et la méthode de requête GET récupère les informations bancaires de la base de données en utilisant l'ID de l'utilisateur.

```javascript
import { updateBankInfo, getUserBankInfo } from "@/app/db/actions";
import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
    const { accountName, userID, accountNumber, bankName, currency } = await req.json();
    try {
        await updateBankInfo({
            user_id: userID,
            bank_name: bankName,
            account_number: Number(accountNumber),
            account_name: accountName,
            currency: currency,
 });
        return NextResponse.json({ message: "Détails bancaires mis à jour !" }, { status: 201 });
 } catch (err) {
        return NextResponse.json(
 { message: "Une erreur s'est produite", err },
 { status: 400 }
 );
 }
}

export async function GET(req: NextRequest) {
   const userID  = req.nextUrl.searchParams.get("userID");
    
    try {
        const bankInfo = await getUserBankInfo(userID!);
        return NextResponse.json({ message: "Détails bancaires récupérés", bankInfo }, { status: 200 });
 } catch (err) {
        return NextResponse.json(
 { message: "Une erreur s'est produite", err },
 { status: 400 }
 );
 }
}
```

Ensuite, ajoutez un dossier **invoice** contenant un fichier **route.ts** au répertoire **`api`**. Copiez le code suivant dans le fichier /api/invoice/route.ts :

```javascript
import { createInvoice, getUserInvoices } from "@/app/db/actions";
import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
    const { customer, title, items, total, ownerID } = await req.json();
    
    try {
        await createInvoice({
            user_id: ownerID,
            customer_id: customer,
            title,
            total_amount: total,
            items: JSON.stringify(items),
 })
        return NextResponse.json(
 { message: "Nouvelle facture créée !" },
 { status: 201 }
 );
 } catch (err) {
        return NextResponse.json(
 { message: "Une erreur s'est produite", err },
 { status: 400 }
 );
 }
}

export async function GET(req: NextRequest) {
    const userID = req.nextUrl.searchParams.get("userID");
    
    try {
        const invoices = await getUserInvoices(userID!);
        return NextResponse.json({message: "Factures récupérées avec succès !", invoices}, { status: 200 });
 } catch (err) {
        return NextResponse.json(
 { message: "Une erreur s'est produite", err },
 { status: 400 }
 );
 }
}
```

La méthode de requête POST crée une nouvelle facture et la méthode de requête GET retourne toutes les factures de l'utilisateur depuis la base de données.

Vous pouvez également créer un sous-dossier nommé **`single`** dans le dossier **/api/invoices**, et ajouter un fichier **route.ts** à l'intérieur.

```javascript
import { NextRequest, NextResponse } from "next/server";
import { getSingleInvoice } from "@/app/db/actions";

export async function GET(req: NextRequest) {
   const invoiceID = req.nextUrl.searchParams.get("id");
    
    try {
        const invoice = await getSingleInvoice(invoiceID);
        return NextResponse.json({ message: "Facture récupérée avec succès !", invoice }, { status: 200 });
 } catch (err) {
        return NextResponse.json(
 { message: "Une erreur s'est produite", err },
 { status: 400 }
 );
 }
}
```

Le code ci-dessus accepte un ID de facture et récupère toutes ses données disponibles dans la table de la base de données. Vous pouvez faire de même avec la table **customers** également.

Félicitations ! Vous avez appris à _créer_, _stocker_ et _récupérer_ des données de la base de données Postgres Neon. Dans les sections à venir, vous découvrirez comment imprimer et envoyer des factures aux clients.

## **Comment imprimer et télécharger des factures dans Next.js**

Le package [React-to-print](https://www.npmjs.com/package/react-to-print) est une bibliothèque JavaScript simple qui vous permet d'imprimer le contenu d'un composant React facilement sans altérer les styles CSS du composant. Il convertit les composants React exactement tels qu'ils sont en fichiers PDF téléchargeables.

Tout d'abord, exécutez le code suivant dans votre terminal pour installer le package :

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">npm install -save react-to-print</span></p></td></tr></tbody></table>

Créez une page client (**/invoice/[id].tsx**).

Pour ce faire, ajoutez un dossier **invoice** contenant un sous-dossier **[id]** au répertoire de l'application Next.js. À l'intérieur du dossier **[id]**, ajoutez un fichier **page.tsx**. Cette page affiche toutes les informations sur une facture et permet aux utilisateurs d'imprimer, de télécharger et d'envoyer des factures aux clients.

![Invoice-app-download-page-ui](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcnG8Yav_Xnqpmk5lO4PXkKjrWqMzEkOat42mTkGR-bvAEA5VTiZ1nasFEc05H_JR6pwlyars_oWMRuBNg4CCLCNpghvnZUQ8eBen-I0OvdPGYfItoUkcXC-Abz87MjBQdacIFUotw2WGYp7YyJFq6NeOrr?key=QrOqhkDtPIneanOaExEDaA)
_Invoice-app-download-page-ui_

Créez un design de facture similaire à l'image ci-dessus en copiant le code suivant dans le fichier page.tsx :

```javascript
const ComponentToPrint = forwardRef<HTMLDivElement, Props>((props, ref) => {
  const { id, customer, invoice, bankInfo } = props as Props;

  return (
    <div className='w-full px-2 py-8' ref={ref}>
      <div className='lg:w-2/3 w-full mx-auto shadow-md border-[1px] rounded min-h-[75vh] p-5'>
        <header className='w-full flex items-center space-x-4 justify-between'>
          <div className='w-4/5'>
            <h2 className='text-lg font-semibold mb-3'>FACTURE #0{id}</h2>
            <section className='mb-6'>
              <p className='opacity-60'>Nom de l'émetteur : {bankInfo?.account_name}</p>
              <p className='opacity-60'>Date : {formatDateString(invoice?.created_at!)}</p>
            </section>
            <h2 className='text-lg font-semibold mb-2'>À :</h2>
            <section className='mb-6'>
              <p className='opacity-60'>Nom : {invoice?.customer_id}</p>
              <p className='opacity-60'>Adresse : {customer?.address}</p>
              <p className='opacity-60'>Email : {customer?.email}</p>
            </section>
          </div>

          <div className='w-1/5 flex flex-col'>
            <p className='font-extrabold text-2xl'>
              {`${bankInfo?.currency}${Number(invoice?.total_amount).toLocaleString()}`}
            </p>
            <p className='text-sm opacity-60'>Montant total</p>
          </div>
        </header>
        <div>
          <p className='opacity-60'>Objet :</p>
          <h2 className='text-lg font-semibold'>{invoice?.title}</h2>
        </div>

        <InvoiceTable itemList={invoice?.items ? JSON.parse(invoice.items) : []} />
      </div>
    </div>
  );
});

ComponentToPrint.displayName = "ComponentToPrint";

```

Le code ci-dessus accepte les détails de la facture, y compris le client et les informations bancaires de l'utilisateur, et les affiche dans le composant.

Enfin, vous devez envelopper ce composant avec un autre composant parent et instruire **React-to-print** d'imprimer le sous-composant. Ajoutez le code suivant sous le composant **`ComponentToPrint`**.

```javascript
import { useReactToPrint } from "react-to-print";

export default function Invoices() {
  const { id } = useParams<{ id: string }>();
  // Référence au composant à imprimer
  const componentRef = useRef<any>();

  // États pour les données
  const [customer, setCustomer] = useState<Customer>();
  const [bankInfo, setBankInfo] = useState<BankInfo>();
  const [invoice, setInvoice] = useState<Invoice>();

  // Fonction qui envoie la facture par email
  const handleSendInvoice = async () => {};

  // Fonction qui imprime la facture
  const handlePrint = useReactToPrint({
    documentTitle: "Facture",
    content: () => componentRef.current,
  });

  return (
    <main className='w-full min-h-screen'>
      <section className='w-full flex p-4 items-center justify-center space-x-5 mb-3'>
        <button
          className='p-3 text-blue-50 bg-blue-500 rounded-md'
          onClick={handlePrint}
        >
          Télécharger
        </button>
        <button
          className='p-3 text-blue-50 bg-green-500 rounded-md'
          onClick={() => {
            handleSendInvoice();
          }}
        >
          Envoyer la facture
        </button>
      </section>

      <ComponentToPrint
        ref={componentRef}
        id={id}
        customer={customer}
        bankInfo={bankInfo}
        invoice={invoice}
      />
    </main>
  );
}

```

Le composant affiche le composant **`ComponentToPrint`**, crée une référence à celui-ci et l'imprime en utilisant le hook [**useReactToPrint**](https://github.com/MatthewHerbst/react-to-print?tab=readme-ov-file#usage).

![Invoice-app-print-ui](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeMjZeFBZ_-Y-mP7tH9rmlBYUwSsGIJfOiCQ7VvYOtLhZBJhgZn60bWpFBNlqOWFIGtwMDizCTooXoWtSX6soKbiGr2xKU3PGMC-5YG9wA-9er21DORGzX4IsdtaxoipsQqQVKlGCu7Ix2igPgLEBaWB_I?key=QrOqhkDtPIneanOaExEDaA)
_Invoice-app-print-ui_

## **Comment envoyer des factures numériques avec Resend et React Email**

[Resend](https://resend.com/) est un service API qui nous permet d'envoyer et de gérer des emails de manière programmatique, facilitant l'intégration de la fonctionnalité email dans les applications logicielles. 

[React Email](https://react.email/) est une bibliothèque qui nous permet de créer des modèles d'email réutilisables et magnifiquement conçus en utilisant des composants React. Les deux packages sont créés par la même personne, permettant une intégration fluide entre les deux services.

Installez les deux packages en exécutant le code suivant :

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">npm install resend </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">npm install react-email </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#fc9b9b;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">@react</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">-email/components -E</span></p></td></tr></tbody></table>

Configurez React Email en incluant le script suivant dans votre fichier **package.json**.

Le drapeau **`--dir`** donne à React Email accès aux modèles d'email situés dans le projet. Dans ce cas, les modèles d'email sont situés dans le dossier **src/app/emails**.

<table style="border:none;border-collapse:collapse;"><colgroup></colgroup><tbody><tr style="height:0pt"><td style="vertical-align:top;background-color:#333333;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">{</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp; &nbsp; </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#a2fca2;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">"scripts"</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">: {</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp; &nbsp; &nbsp; &nbsp; </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#a2fca2;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">"email"</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">: </span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#a2fca2;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">"email dev --dir src/app/emails"</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp; &nbsp; }</span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;"><br></span><span style="font-size:11pt;font-family:Consolas,sans-serif;color:#ffffff;background-color:#333333;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">}</span></p></td></tr></tbody></table>

Ensuite, créez le dossier emails contenant le modèle d'email à envoyer à l'email des clients :

```javascript
import { Heading, Hr, Text } from "@react-email/components";

export default function EmailTemplate({
    invoiceID,
    items,
    amount,
    issuerName,
    accountNumber,
    currency,
}: Props) {
    return (
 <div>
 <Heading as='h2' style={{ color: "#0ea5e9" }}>
 Facture d'achat de {issuerName}
 </Heading>
 <Text style={{ marginBottom: 5 }}>Numéro de facture : INV0{invoiceID}</Text>
 <Heading as='h3'> Détails de paiement :</Heading>
 <Text>Détails du compte : {issuerName}</Text>
 <Text>Numéro de compte : {accountNumber}</Text>
 <Text>Montant total : {`${currency}${amount}`}</Text>
 <Hr />
 <Heading as='h3'> Articles : </Heading>
            {items &&
                items.map((item, index) => (
 <div key={index}>
 <Text>
                            {item.cost} x {item.quantity} = {item.price}
 </Text>
 </div>
 ))}
 </div>
 );
}
```

Le modèle d'email accepte tous les détails de la facture en tant que props et envoie un modèle d'email dynamique à l'utilisateur. Vous pouvez également prévisualiser la mise en page de la facture en exécutant **`npm run email`** dans votre terminal.

Ensuite, créez un [compte Resend](https://resend.com/docs/introduction), et sélectionnez **API Keys** dans le menu latéral de votre tableau de bord pour en créer une.

![resend-api-keys-dashboard](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdTkbkk-f3JIvcGLXoFdeQGpFNF6gDgqZWVL5NnJjcbu17I4dRp3rF8GYNUHXkvF2Gs59OQgjuknTVXWzOjknrJVeZ7xv90LhLZLPeqGgYI-il5PyKEcL3g-E3_VAem-sX13pkRlz-AhqPdgXgVQo884Uce?key=QrOqhkDtPIneanOaExEDaA)
_resend-api-keys-dashboard_

Copiez la clé API dans le fichier .env.local.

Enfin, créez un point de terminaison API qui accepte les détails de la facture depuis le frontend et envoie une facture contenant les données à un client.

```javascript
import { NextRequest, NextResponse } from "next/server";
import EmailTemplate from "@/app/emails/email";
import { Resend } from "resend";
const resend = new Resend(process.env.RESEND_API_KEY!);

export async function POST(req: NextRequest) {
    const {
        invoiceID,
        items,
        title,
        amount,
        customerEmail,
        issuerName,
        accountNumber,
        currency,
 } = await req.json();

    try {
        const { data, error } = await resend.emails.send({
            from: "Acme <onboarding@resend.dev>",
            to: [customerEmail],
            subject: title,
            react: EmailTemplate({
                invoiceID,
                items: JSON.parse(items),
                amount: Number(amount),
                issuerName,
                accountNumber,
                currency,
 }) as React.ReactElement,
 });

        if (error) {
            return Response.json(
 { message: "Email non envoyé !", error },
 { status: 500 }
 );
 }

        return NextResponse.json({ message: "Email livré !" }, { status: 200 });
 } catch (error) {
        return NextResponse.json(
 { message: "Email non envoyé !", error },
 { status: 500 }
 );
 }
}
```

Le code ci-dessus accepte les détails de la facture depuis le frontend, transmet les données requises au modèle d'email et envoie un email à l'utilisateur.

## **Prochaines étapes**

Félicitations. À ce stade, vous devriez avoir une bonne compréhension de la manière de construire des applications full-stack avec Clerk, Resend, Neon Postgres et Next.js.

Si vous souhaitez en savoir plus sur la manière dont vous pouvez utiliser Neon Postgres pour construire des applications avancées et évolutives, vous pouvez consulter les ressources suivantes :

* [Documentation de Neon](https://neon.tech/docs/introduction)
* [Awesome Neon](https://github.com/tyaga001/awesome-neon)
* [Projets d'exemple de Neon](https://github.com/neondatabase/examples)
* [Comment intégrer Neon avec Vercel](https://neon.tech/docs/guides/vercel)
* [Comment importer vos données d'une base de données Postgres vers Neon](https://neon.tech/docs/import/import-from-postgres)

## Merci d'avoir lu

Si vous avez trouvé cet article utile, vous pouvez :

* [Vous abonner à ma newsletter.](https://bytesizedbets.com/)
* [Me suivre sur Twitter](https://x.com/TheAnkurTyagi) où je poste sur mon parcours entrepreneurial et d'écriture, mes projets secondaires et mes apprentissages actuels.
* Consulter [mon blog](https://theankurtyagi.com/) pour plus de tutoriels comme celui-ci sur les outils de développement.