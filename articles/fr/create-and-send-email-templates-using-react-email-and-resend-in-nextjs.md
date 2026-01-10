---
title: Comment créer et envoyer des modèles d'e-mails avec React Email et Resend dans
  Next.js
subtitle: ''
author: David Asaolu
co_authors: []
series: null
date: '2024-12-12T17:12:33.532Z'
originalURL: https://freecodecamp.org/news/create-and-send-email-templates-using-react-email-and-resend-in-nextjs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1733995060570/3450a9b3-e740-4362-b0ab-0269646e725c.png
tags:
- name: React
  slug: reactjs
- name: Next.js
  slug: nextjs
- name: Tutorial
  slug: tutorial
- name: Programming Blogs
  slug: programming-blogs
seo_title: Comment créer et envoyer des modèles d'e-mails avec React Email et Resend
  dans Next.js
seo_desc: Modern software applications often rely on email communication to engage
  with users. They may send authentication codes during sign in attempts, marketing
  emails, or newsletters, for example. This means that email notifications are typically
  the most...
---

Les applications logicielles modernes s'appuient souvent sur la communication par e-mail pour interagir avec les utilisateurs. Elles peuvent envoyer des codes d'authentification lors des tentatives de connexion, des e-mails marketing ou des newsletters, par exemple. Cela signifie que les notifications par e-mail sont généralement le moyen de communication le plus courant avec les utilisateurs.

Dans ce tutoriel, vous apprendrez à concevoir des modèles d'e-mails magnifiques avec [React Email](https://react.email/docs/introduction) et à les envoyer en utilisant [Resend](https://resend.com/docs/send-with-nextjs) – une plateforme d'API d'e-mails simple et puissante.

## Prérequis

Pour tirer le meilleur parti de ce tutoriel, vous devez avoir une compréhension de base de React ou Next.js.

Nous utiliserons également les outils suivants :

* React Email : Une bibliothèque qui vous permet de créer des modèles d'e-mails magnifiquement conçus en utilisant des composants React.

* Resend : Une plateforme d'API simple et puissante pour envoyer des e-mails depuis vos applications.

## Comment construire l'application avec Next.js

Dans cette section, vous allez créer une application simple de support client. L'application inclura un formulaire pour que les utilisateurs soumettent leurs questions, ce qui déclenchera une notification par e-mail confirmant qu'un ticket de support a été créé.

Pour commencer, nous allons d'abord configurer l'interface utilisateur et un point de terminaison API.

Exécutez la commande suivante pour créer un nouveau projet Next.js TypeScript :

```bash
npx create-next-app react-email-resend
```

Mettez à jour le fichier `app/page.tsx` pour afficher un formulaire qui collecte les détails du client, y compris son nom complet, son adresse e-mail, l'objet du ticket et un message détaillé décrivant le problème. Lorsque le formulaire est soumis, les données d'entrée sont enregistrées dans la console à l'aide de la fonction `handleSubmit`.

```typescript
"use client";
import support from "@/app/images/support.jpg";
import { useState } from "react";
import Image from "next/image";

export default function Page() {
    //👇🏻 états d'entrée
	const [name, setName] = useState<string>("");
	const [email, setEmail] = useState<string>("");
	const [subject, setSubject] = useState<string>("");
	const [content, setContent] = useState<string>("");

	const handleSubmit = async (e: React.FormEvent) => {
		e.preventDefault();
		//👇🏻 enregistrer l'entrée de l'utilisateur
		console.log({ name, email, subject, content });
	};
return ({/** -- Éléments UI -- */})
}
```

Retournez les éléments UI du formulaire qui acceptent le nom complet de l'utilisateur, l'adresse e-mail, l'objet du ticket et un message détaillé décrivant le problème.

```typescript
	return (
		<main className='w-full min-h-screen flex items-center justify-between'>
				<form className='w-full' onSubmit={handleSubmit}>
					<label htmlFor='name' className='opacity-60'>
						Nom complet
					</label>
					<input
						type='text'
						className='w-full px-4 py-3 border-[1px] mb-3 border-gray-300 rounded-sm'
						id='name'
						required
						value={name}
						onChange={(e) => setName(e.target.value)}
					/>

					<label htmlFor='email' className='opacity-60'>
						Adresse e-mail
					</label>
					<input
						type='email'
						className='w-full px-4 py-3 border-[1px] mb-3 border-gray-300 rounded-sm'
						id='email'
						value={email}
						onChange={(e) => setEmail(e.target.value)}
						required
					/>

					<label htmlFor='subject' className='opacity-60'>
						Objet
					</label>
					<input
						type='text'
						className='w-full px-4 py-3 border-[1px] mb-3 border-gray-300 rounded-sm'
						id='subject'
						value={subject}
						onChange={(e) => setSubject(e.target.value)}
						required
					/>

					<label htmlFor='message' className='opacity-60'>
						Message
					</label>
					<textarea
						rows={7}
						className='w-full px-4 py-3 border-[1px] mb-3 border-gray-300 rounded-sm'
						id='message'
						required
						value={content}
						onChange={(e) => setContent(e.target.value)}
					/>

					<button className='w-full bg-blue-500 py-4 px-3 rounded-md font-bold text-blue-50'>
						ENVOYER LE MESSAGE
					</button>
				</form>
			</div>
		</main>
	);
```

Voici la page résultante du composant :

![Le composant Page affiche un formulaire qui accepte l'entrée de l'utilisateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1733748196715/703e7e5b-f868-45e6-b62f-64a2d6dd279e.png align="center")

Ensuite, créez un point de terminaison API (`/api/route.ts`) qui accepte l'entrée du client.

```bash
cd app
mkdir api && cd api
touch route.ts 
```

Copiez le code suivant dans le fichier `api/route.ts`. Le point de terminaison API enregistre l'entrée du client dans la console lors de sa réception.

```typescript
import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
    const { name, email, subject, content } = await req.json();
    //👇🏻 enregistrer le contenu
    console.log({ name, email, subject, content });
    return NextResponse.json({
        message: "Email envoyé avec succès",
        data,
 });
}
```

Mettez à jour la fonction `handleSubmit` pour envoyer les données du client au point de terminaison API et retourner la réponse JSON :

```typescript
const handleSubmit = async (e: React.FormEvent) => {
	e.preventDefault();

	try {
		const response = await fetch("/api", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ name, email, subject, content }),
		});
		const data = await response.json();
		alert(data.message);
	} catch (error) {
		console.error(error);
		alert("Une erreur s'est produite, veuillez réessayer plus tard");
	}
	setName("");
	setEmail("");
	setSubject("");
	setContent("");
};
```

Félicitations ! Vous avez configuré la collecte et la soumission des données. Dans les sections suivantes, je vous guiderai à travers la création et l'envoi de modèles d'e-mails avec React Email et Resend.

## Comment créer des modèles d'e-mails avec React Email

React Email vous permet de créer et d'envoyer des composants d'e-mails en utilisant React et TypeScript. Il prend en charge plusieurs clients de messagerie, y compris Gmail, Yahoo Mail, Outlook et Apple Mail.

React Email fournit également plusieurs [composants UI](https://react.email/components) qui vous permettent de personnaliser les modèles d'e-mails selon votre mise en page préférée en utilisant des composants React JSX/TSX.

Installez le package React Email et ses composants en exécutant le snippet de code ci-dessous :

```bash
npm install react-email -D -E
npm install @react-email/components -E
```

Incluez ce script dans votre fichier `package.json`. Il dirige React Email vers l'emplacement des modèles d'e-mails dans votre projet.

```json
  "scripts": {
    "email": "email dev --dir src/emails"
  },
```

L'une des fonctionnalités de React Email est la possibilité de prévisualiser votre modèle d'e-mail dans votre navigateur pendant le développement, ce qui vous permet de voir comment il apparaîtra dans l'e-mail du destinataire.

Alors, créez un dossier `emails` contenant un fichier `TicketCreated.tsx` dans le dossier `src` de Next.js et copiez le snippet de code suivant dans le fichier :

```typescript
import * as React from "react";
import {
	Body,
	Container,
	Head,
	Heading,
	Hr,
	Html,
	Link,
	Preview,
	Text,
	Tailwind,
} from "@react-email/components";

interface TicketCreatedProps {
	username: string;
	ticketID: string;
}

const baseUrl = process.env.VERCEL_URL || "http://localhost:3000";
```

Dans le snippet de code ci-dessus, nous avons importé les composants nécessaires pour construire le modèle d'e-mail.

Ensuite, ajoutez le composant `TicketCreated` au fichier pour afficher le modèle d'e-mail en utilisant les [composants React Email](https://react.email/components).

```typescript
export const TicketCreated = ({ username, ticketID }: TicketCreatedProps) => {
	return (
		<Html>
			<Head />
			<Preview>E-mail de confirmation de ticket de support 🎉</Preview>
			<Tailwind>
				<Body className='bg-white my-auto mx-auto font-sans px-2'>
					<Container className='border border-solid border-[#eaeaea] rounded my-[40px] mx-auto p-[20px] max-w-[465px]'>
						<Heading className='text-black text-[24px] font-normal text-center p-0 my-[30px] mx-0'>
							Votre ticket a été créé
						</Heading>
						<Text className='text-black text-[14px] leading-[24px]'>
							Bonjour {username},
						</Text>
						<Text className='text-black text-[14px] leading-[24px]'>
							<strong>Ticket de support</strong> (
							<Link
								href={`${baseUrl}/ticket/${ticketID}`}
								className='text-blue-600 no-underline'
							>
								{`#${ticketID}`}
							</Link>
							) a été créé avec succès.
						</Text>

						<Text className='text-black text-[14px] leading-[24px]'>
							L'équipe de support examinera votre ticket et vous répondra
							bientôt.
						</Text>

						<Hr className='border border-solid border-[#eaeaea] my-[26px] mx-0 w-full' />
						<Text className='text-[#666666] text-[12px] leading-[24px]'>
							Ce message était destiné à{" 