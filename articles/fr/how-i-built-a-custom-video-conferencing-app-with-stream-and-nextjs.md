---
title: Comment j'ai construit une application de visioconférence personnalisée avec
  Stream et Next.js
subtitle: ''
author: Ankur Tyagi
co_authors: []
series: null
date: '2024-10-02T17:46:39.006Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-custom-video-conferencing-app-with-stream-and-nextjs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727433361539/498f0742-2ff1-4762-b268-2c25eb22017e.png
tags:
- name: Next.js
  slug: nextjs
- name: Web Development
  slug: web-development
- name: Startups
  slug: startups
- name: software development
  slug: software-development
- name: AI
  slug: ai
- name: webdev
  slug: webdev
- name: Developer Tools
  slug: developer-tools
- name: General Programming
  slug: programming
seo_title: Comment j'ai construit une application de visioconférence personnalisée
  avec Stream et Next.js
seo_desc: 'Building full-stack apps can be tough. You have to think about frontend,
  APIs, databases, auth – plus you have to know how all of these things work together.

  And building a project like a video conferencing app from scratch can feel even
  more overwhe...'
---

Construire des applications full-stack peut être difficile. Vous devez penser au frontend, aux API, aux bases de données, à l'authentification – et vous devez savoir comment tous ces éléments fonctionnent ensemble.

Et construire un projet comme une application de visioconférence à partir de zéro peut sembler encore plus accablant, surtout avec les complexités de la gestion des flux vidéo, de l'authentification des utilisateurs et des interactions en temps réel.

Mais et si je vous disais qu'il existe un moyen plus simple de le faire – un moyen qui vous permet de construire votre application de visioconférence en une fraction du temps ?

Dans cet article, je vais vous montrer comment j'ai construit une application de visioconférence en utilisant [Stream](https://getstream.io/) et Clerk dans Next.js.

Voici le [code source](https://github.com/tyaga001/facetime-on-stream) (n'oubliez pas de lui donner une étoile ⭐).

Avant de commencer, laissez-moi vous dire pourquoi j'ai écrit ce tutoriel.

Je suis un ingénieur logiciel qui se soucie de l'écriture et j'**adore** **coder**, **concevoir**, **développer**, puis **enseigner** aux gens.

J'utilise des projets, des produits et des services open-source depuis un certain temps maintenant, et je contribue à beaucoup d'entre eux pour les améliorer comme je le peux. Le mois dernier, j'ai construit un blog open-source pour les « outils de développement géniaux » appelé - [devtoolsacademy](https://www.devtoolsacademy.com/)

[![devtoolsacademy](https://cdn.hashnode.com/res/hashnode/image/upload/v1727430858395/70ffbec4-69ab-4f31-a9cb-02b44066ac6b.png align="center")](https://www.devtoolsacademy.com/)

Cet article traite du partage de l'expérience que j'ai eue en utilisant un autre outil de développement génial.

## **Table des matières :**

* [Qu'est-ce que Stream ?](#heading-questce-que-stream)
    
* [Prérequis](#heading-prerequis)
    
* [Comment construire l'interface de l'application avec Next.js](#heading-comment-construire-linterface-de-lapplication-avec-nextjs)
    
    * [Le modal de création de lien](#heading-le-modal-de-creation-de-lien)
        
    * [Le modal de réunion instantanée](#heading-le-modal-de-reunion-instantanee)
        
    * [Le modal pour rejoindre une réunion](#heading-le-modal-pour-rejoindre-une-reunion)
        
* [Comment authentifier les utilisateurs avec Clerk](#heading-comment-authentifier-les-utilisateurs-avec-clerk)
    
* [Comment configurer Stream dans une application Next.js](#heading-comment-configurer-stream-dans-une-application-nextjs)
    
* [Comment créer et rejoindre des appels avec Stream](#heading-comment-creer-et-rejoindre-des-appels-avec-stream)
    
    * [Création et planification d'appels](#heading-creation-et-planification-dappels)
        
    * [Rejoindre des appels et la page de réunion](#heading-rejoindre-des-appels-et-la-page-de-reunion)
        
    * [Récupération des appels à venir](#heading-recuperation-des-appels-a-venir)
        
* [Prochaines étapes](#heading-prochaines-etapes)
    

## Qu'est-ce que Stream ?

[Stream](https://getstream.io/) est une plateforme cloud open-source qui fournit des API et des SDK pour créer des applications en temps réel évolutives et riches en fonctionnalités. Elle propose des composants UI pré-construits pour créer des logiciels de qualité entreprise avec des fonctionnalités telles que le chat, la vidéo, l'audio et les flux d'activité.

[![Qu'est-ce que Stream](https://cdn.hashnode.com/res/hashnode/image/upload/v1726475007023/be45aa40-7794-434a-8f5d-f4b637d97fd8.png align="center")](https://getstream.io)

Voici comment j'utiliserai `Stream` lors de la construction de l'application :

* Configurer des appels vidéo et audio en temps réel
    
* Utiliser les composants UI de Stream pour construire rapidement l'interface
    
* Implémenter des fonctionnalités clés telles que les appels `vidéo` et `audio`
    
* `Types d'appels` – j'implémenterai des réunions instantanées et des appels pré-planifiés en utilisant Stream
    
* Exploiter les objets d'appel et de participant de Stream pour gérer l' `état de l'appel`
    

## **Prérequis**

Pour bien comprendre le tutoriel, vous devez avoir une compréhension de base de [React](https://www.freecodecamp.org/news/learn-react-key-concepts/) et [Next.js](https://theankurtyagi.com/next-js/). Vous aurez également besoin des éléments suivants :

* [Stream React SDK](https://getstream.io/chat/docs/sdk/react/) - fournit des composants UI pré-construits pour ajouter rapidement des fonctionnalités d'appel vidéo.
    
* [Stream Node.js SDK](https://github.com/GetStream/stream-node) - pour gérer les interactions côté serveur et maintenir la synchronisation de l'état de Stream.
    
* [Clerk](https://clerk.com/) - une plateforme complète de gestion des utilisateurs pour gérer l'authentification sans effort.
    
* [Headless UI](https://headlessui.com/) - fournit des composants UI accessibles pour construire des applications conviviales.
    
* [React Copy-to-Clipboard](https://www.npmjs.com/package/react-copy-to-clipboard) - permet aux utilisateurs de copier facilement les liens de réunion dans l'application.
    
* [React Icons](https://react-icons.github.io/react-icons/) - propose une bibliothèque d'icônes facilement intégrables.
    

## Comment construire l'interface de l'application avec Next.js

Dans cette section, je vais vous guider à travers la création de l'interface utilisateur pour l'application de visioconférence. L'interface permettra aux utilisateurs de créer, rejoindre et planifier facilement des réunions, ainsi que de visualiser leurs réunions à venir.

Tout d'abord, créons un projet Next.js TypeScript en exécutant l'extrait de code ci-dessous :

```bash
npx create-next-app facetime-app
```

Ensuite, installez les paquets suivants :

* [React icons](https://react-icons.github.io/react-icons/) - un paquet d'icônes React populaire
    
* [Headless UI](https://headlessui.com/) - fournit un ensemble de composants UI accessibles
    
* [React-copy-to-clipboard](https://www.npmjs.com/package/react-copy-to-clipboard) - un paquet léger qui nous permet de copier les liens de réunion.
    

```bash
npm install react-icons @headlessui/react react-copy-to-clipboard
```

Copiez l'extrait de code ci-dessous dans le fichier `app/page.tsx` :

```typescript
"use client";
import { useState } from "react";
import { FaLink, FaVideo } from "react-icons/fa";
import InstantMeeting from "@/app/modals/InstantMeeting";
import UpcomingMeeting from "@/app/modals/UpcomingMeeting";
import CreateLink from "@/app/modals/CreateLink";
import JoinMeeting from "@/app/modals/JoinMeeting";

export default function Dashboard() {
	const [startInstantMeeting, setStartInstantMeeting] =
		useState<boolean>(false);
	const [joinMeeting, setJoinMeeting] = useState<boolean>(false);
	const [showUpcomingMeetings, setShowUpcomingMeetings] =
		useState<boolean>(false);
	const [showCreateLink, setShowCreateLink] = useState<boolean>(false);

	return (
		<>
			<button
				className=' top-5 right-5 text-sm fixed bg-green-500 px-2 w-[150px] hover:bg-green-600 py-3 flex flex-col items-center text-white rounded-md shadow-sm cursor-pointer z-10'
				onClick={() => setJoinMeeting(true)}
			>
				<FaVideo className='mb-[3px] text-white' />
				Rejoindre FaceTime
			</button>

			<main className='w-full h-screen flex flex-col items-center justify-center'>
				<h1 className='font-bold text-2xl text-center'>FaceTime</h1>
				<div className='flex flex-col'>
					<button
						className='text-green-500 underline text-sm text-center cursor-pointer'
						onClick={() => setShowUpcomingMeetings(true)}
					>
						FaceTime à venir
					</button>
				</div>

				<div className='flex items-center justify-center space-x-4 mt-6'>
					<button
						className='bg-gray-500 px-4 w-[200px] py-3 flex flex-col items-center hover:bg-gray-600 text-white rounded-md shadow-sm'
						onClick={() => setShowCreateLink(true)}
					>
						<FaLink className='mb-[3px] text-gray-300' />
						Créer un lien
					</button>
					<button
						className='bg-green-500 px-4 w-[200px] hover:bg-green-600 py-3 flex flex-col items-center text-white rounded-md shadow-sm'
						onClick={() => setStartInstantMeeting(true)}
					>
						<FaVideo className='mb-[3px] text-white' />
						Nouveau FaceTime
					</button>
				</div>
			</main>

			{startInstantMeeting && (
				<InstantMeeting
					enable={startInstantMeeting}
					setEnable={setStartInstantMeeting}
				/>
			)}
			{showUpcomingMeetings && (
				<UpcomingMeeting
					enable={showUpcomingMeetings}
					setEnable={setShowUpcomingMeetings}
				/>
			)}
			{showCreateLink && (
				<CreateLink enable={showCreateLink} setEnable={setShowCreateLink} />
			)}
			{joinMeeting && (
				<JoinMeeting enable={joinMeeting} setEnable={setJoinMeeting} />
			)}
		</>
	);
}
```

L'extrait de code ci-dessus rend plusieurs boutons qui permettent aux utilisateurs d'effectuer des actions telles que rejoindre, créer et planifier un appel. Chaque bouton ouvre un modal qui invite l'utilisateur à fournir des détails supplémentaires spécifiques à l'action qu'il effectue.

![facetime-app-home-page](https://cdn.hashnode.com/res/hashnode/image/upload/v1726481911712/286f7349-0d95-419d-97e5-193371307e13.png align="center")

Ensuite, créons un dossier `modals` dans le répertoire de l'application Next.js et ajoutons les composants suivants au dossier `modals` :

```bash
cd app
mkdir modals && cd modals
touch CreateLink.tsx InstantMeeting.tsx JoinMeeting.tsx UpcomingMeeting.tsx
```

Le modal `CreateLink` permet aux utilisateurs de fournir une description et de planifier une heure pour l'appel. Le modal `InstantMeeting` permet aux utilisateurs de démarrer une réunion instantanée en fournissant une description de l'appel. Le modal `JoinMeeting` permet aux utilisateurs de saisir un lien d'appel et de rejoindre une réunion. Et le modal `UpcomingMeeting` affiche tous les appels planifiés à venir.

### Le modal de création de lien

Copiez l'extrait de code ci-dessous dans le modal `CreateLink` :

```typescript
"use client";
import {
	Dialog,
	DialogTitle,
	DialogPanel,
	Transition,
	Description,
	TransitionChild,
} from "@headlessui/react";
import { Fragment, SetStateAction, useState, Dispatch } from "react";
import CopyToClipboard from "react-copy-to-clipboard";
import { FaCopy } from "react-icons/fa";

export default function CreateLink({ enable, setEnable }: Props) {
	const [showMeetingLink, setShowMeetingLink] = useState(false);
	const [facetimeLink, setFacetimeLink] = useState<string>("");
	const closeModal = () => setEnable(false);

	return (
		<>
			<Transition appear show={enable} as={Fragment}>
				<Dialog as='div' className='relative z-10' onClose={closeModal}>
					<TransitionChild
						as={Fragment}
						enter='ease-out duration-300'
						enterFrom='opacity-0'
						enterTo='opacity-100'
						leave='ease-in duration-200'
						leaveFrom='opacity-100'
						leaveTo='opacity-0'
					>
						<div className='fixed inset-0 bg-black/75' />
					</TransitionChild>

					<div className='fixed inset-0 overflow-y-auto'>
						<div className='flex min-h-full items-center justify-center p-4 text-center'>
							<TransitionChild
								as={Fragment}
								enter='ease-out duration-300'
								enterFrom='opacity-0 scale-95'
								enterTo='opacity-100 scale-100'
								leave='ease-in duration-200'
								leaveFrom='opacity-100 scale-100'
								leaveTo='opacity-0 scale-95'
							>
								<DialogPanel className='w-full max-w-2xl transform overflow-hidden rounded-2xl bg-white p-6 align-middle shadow-xl transition-all text-center'>
									{showMeetingLink ? (
										<MeetingLink facetimeLink={facetimeLink} />
									) : (
										<MeetingForm
											setShowMeetingLink={setShowMeetingLink}
											setFacetimeLink={setFacetimeLink}
										/>
									)}
								</DialogPanel>
							</TransitionChild>
						</div>
					</div>
				</Dialog>
			</Transition>
		</>
	);
}
```

L'extrait de code ci-dessus rend un formulaire qui permet aux utilisateurs de saisir une description et de sélectionner une heure pour planifier un appel. Une fois l'appel créé, le lien généré est affiché et peut être copié.

Enfin, ajoutez les composants `MeetingForm` et `MeetingLink` sous le composant `CreateLink` :

```typescript
const MeetingForm = ({
	setShowMeetingLink,
	setFacetimeLink,
}: {
	setShowMeetingLink: React.Dispatch<SetStateAction<boolean>>;
	setFacetimeLink: Dispatch<SetStateAction<string>>;
}) => {
	const [description, setDescription] = useState<string>("");
	const [dateTime, setDateTime] = useState<string>("");

	const handleStartMeeting = async (e: React.FormEvent<HTMLFormElement>) => {
		e.preventDefault();
		console.log({ description, dateTime });
	};

	return (
		<>
			<DialogTitle
				as='h3'
				className='text-lg font-bold leading-6 text-green-600'
			>
				Planifier un FaceTime
			</DialogTitle>

			<Description className='text-xs opacity-40 mb-4'>
				Planifiez une réunion FaceTime avec votre groupe
			</Description>

			<form className='w-full' onSubmit={handleStartMeeting}>
				<label
					className='block text-left text-sm font-medium text-gray-700'
					htmlFor='description'
				>
					Description de la réunion
				</label>
				<input
					type='text'
					name='description'
					id='description'
					value={description}
					onChange={(e) => setDescription(e.target.value)}
					className='mt-1 block w-full text-sm py-3 px-4 border-gray-200 border-[1px] rounded mb-3'
					required
					placeholder='Entrez une description pour la réunion'
				/>

				<label
					className='block text-left text-sm font-medium text-gray-700'
					htmlFor='date'
				>
					Date et heure
				</label>

				<input
					type='datetime-local'
					id='date'
					name='date'
					required
					className='mt-1 block w-full text-sm py-3 px-4 border-gray-200 border-[1px] rounded mb-3'
					value={dateTime}
					onChange={(e) => setDateTime(e.target.value)}
				/>

				<button className='w-full bg-green-600 text-white py-3 rounded mt-4'>
					Créer FaceTime
				</button>
			</form>
		</>
	);
};
```

Le composant `MeetingForm` accepte la description de l'appel et l'heure planifiée, tandis que le composant `MeetingLink` affiche le lien d'appel généré et permet aux utilisateurs de le copier.

```typescript
const MeetingLink = ({ facetimeLink }: { facetimeLink: string }) => {
	const [copied, setCopied] = useState<boolean>(false);
	const handleCopy = () => setCopied(true);

	return (
		<>
			<DialogTitle
				as='h3'
				className='text-lg font-bold leading-6 text-green-600'
			>
				Copier le lien FaceTime
			</DialogTitle>

			<Description className='text-xs opacity-40 mb-4'>
				Vous pouvez partager le lien facetime avec vos participants
			</Description>

			<div className='bg-gray-100 p-4 rounded flex items-center justify-between'>
				<p className='text-xs text-gray-500'>
					{`${process.env.NEXT_PUBLIC_FACETIME_HOST}/${facetimeLink}`}
				</p>

				<CopyToClipboard
					onCopy={handleCopy}
					text={`${process.env.NEXT_PUBLIC_FACETIME_HOST}/${facetimeLink}`}
				>
					<FaCopy className='text-green-600 text-lg cursor-pointer' />
				</CopyToClipboard>
			</div>

			{copied && (
				<p className='text-red-600 text-xs mt-2'>Lien copié dans le presse-papiers</p>
			)}
		</>
	);
};
```

![facetime-app-schedule-popup](https://cdn.hashnode.com/res/hashnode/image/upload/v1726482044698/0cb22caa-3e5a-4f01-9fa2-25c7ce77b08a.png align="center")

### Le modal de réunion instantanée

Copiez l'extrait de code suivant dans le modal `InstantMeeting` :

```typescript
"use client";
import {
	Dialog,
	DialogTitle,
	DialogPanel,
	Transition,
	Description,
	TransitionChild,
} from "@headlessui/react";
import { FaCopy } from "react-icons/fa";
import CopyToClipboard from "react-copy-to-clipboard";
import { Fragment, useState, Dispatch, SetStateAction } from "react";
import { useStreamVideoClient } from "@stream-io/video-react-sdk";
import { useUser } from "@clerk/nextjs";
import Link from "next/link";

export default function InstantMeeting({ enable, setEnable }: Props) {
	const [showMeetingLink, setShowMeetingLink] = useState(false);
	const [facetimeLink, setFacetimeLink] = useState<string>("");

	const closeModal = () => setEnable(false);

	return (
		<>
			<Transition appear show={enable} as={Fragment}>
				<Dialog as='div' className='relative z-10' onClose={closeModal}>
					<TransitionChild
						as={Fragment}
						enter='ease-out duration-300'
						enterFrom='opacity-0'
						enterTo='opacity-100'
						leave='ease-in duration-200'
						leaveFrom='opacity-100'
						leaveTo='opacity-0'
					>
						<div className='fixed inset-0 bg-black/75' />
					</TransitionChild>

					<div className='fixed inset-0 overflow-y-auto'>
						<div className='flex min-h-full items-center justify-center p-4 text-center'>
							<TransitionChild
								as={Fragment}
								enter='ease-out duration-300'
								enterFrom='opacity-0 scale-95'
								enterTo='opacity-100 scale-100'
								leave='ease-in duration-200'
								leaveFrom='opacity-100 scale-100'
								leaveTo='opacity-0 scale-95'
							>
								<DialogPanel className='w-full max-w-2xl transform overflow-hidden rounded-2xl bg-white p-6 align-middle shadow-xl transition-all text-center'>
									{showMeetingLink ? (
										<MeetingLink facetimeLink={facetimeLink} />
									) : (
										<MeetingForm
											setShowMeetingLink={setShowMeetingLink}
											setFacetimeLink={setFacetimeLink}
										/>
									)}
								</DialogPanel>
							</TransitionChild>
						</div>
					</div>
				</Dialog>
			</Transition>
		</>
	);
}
```

L'extrait de code ci-dessus rend un formulaire qui permet aux utilisateurs de fournir une description d'appel. Une fois l'appel créé, le lien est généré et disponible pour être copié avant de démarrer l'appel.

Enfin, ajoutez les composants `MeetingForm` et `MeetingLink` sous le composant `CreateLink` :

```typescript
const MeetingForm = ({
	setShowMeetingLink,
	setFacetimeLink,
}: {
	setShowMeetingLink: Dispatch<SetStateAction<boolean>>;
	setFacetimeLink: Dispatch<SetStateAction<string>>;
}) => {
	const [description, setDescription] = useState<string>("");

	const handleStartMeeting = async (e: React.FormEvent<HTMLFormElement>) => {
		e.preventDefault();
		console.log({ description });
	};

	return (
		<>
			<DialogTitle
				as='h3'
				className='text-lg font-bold leading-6 text-green-600'
			>
				Créer un FaceTime instantané
			</DialogTitle>

			<Description className='text-xs opacity-40 mb-4'>
				Vous pouvez démarrer un nouveau FaceTime instantanément.
			</Description>

			<form className='w-full' onSubmit={handleStartMeeting}>
				<label
					className='block text-left text-sm font-medium text-gray-700'
					htmlFor='description'
				>
					Description de la réunion
				</label>
				<input
					type='text'
					name='description'
					id='description'
					value={description}
					required
					onChange={(e) => setDescription(e.target.value)}
					className='mt-1 block w-full text-sm py-3 px-4 border-gray-200 border-[1px] rounded mb-3'
					placeholder='Entrez une description pour la réunion'
				/>

				<button className='w-full bg-green-600 text-white py-3 rounded mt-4'>
					Continuer
				</button>
			</form>
		</>
	);
};
```

Le composant `MeetingForm` accepte la description de l'appel, tandis que le composant `MeetingLink` affiche le lien d'appel généré et permet aux utilisateurs de le copier avant de démarrer l'appel.

![facetime-app-create-instant-facetime](https://cdn.hashnode.com/res/hashnode/image/upload/v1726482110082/638609aa-e0ae-4cc4-b520-2050966180b4.png align="center")

### Le modal pour rejoindre une réunion

Copiez l'extrait de code ci-dessous dans le fichier `JoinMeeting.tsx`. Il rend un formulaire qui accepte le lien de l'appel et redirige les utilisateurs vers la page de l'appel.

```typescript
"use client";
import {
	Dialog,
	DialogTitle,
	DialogPanel,
	Transition,
	TransitionChild,
} from "@headlessui/react";
import { useRouter } from "next/navigation";
import { Fragment, useState } from "react";

export default function JoinMeeting({ enable, setEnable }: Props) {
	const closeModal = () => setEnable(false);

	return (
		<>
			<Transition appear show={enable} as={Fragment}>
				<Dialog as='div' className='relative z-10' onClose={closeModal}>
					<TransitionChild
						as={Fragment}
						enter='ease-out duration-300'
						enterFrom='opacity-0'
						enterTo='opacity-100'
						leave='ease-in duration-200'
						leaveFrom='opacity-100'
						leaveTo='opacity-0'
					>
						<div className='fixed inset-0 bg-black/75' />
					</TransitionChild>

					<div className='fixed inset-0 overflow-y-auto'>
						<div className='flex min-h-full items-center justify-center p-4 text-center'>
							<TransitionChild
								as={Fragment}
								enter='ease-out duration-300'
								enterFrom='opacity-0 scale-95'
								enterTo='opacity-100 scale-100'
								leave='ease-in duration-200'
								leaveFrom='opacity-100 scale-100'
								leaveTo='opacity-0 scale-95'
							>
								<DialogPanel className='w-full max-w-2xl transform overflow-hidden rounded-2xl bg-white p-6 align-middle shadow-xl transition-all text-center'>
									<CallLinkForm />
								</DialogPanel>
							</TransitionChild>
						</div>
					</div>
				</Dialog>
			</Transition>
		</>
	);
}
```

Ajoutez le `CallLinkForm` sous le composant `JoinMeeting` :

```typescript
const CallLinkForm = () => {
	const [link, setLink] = useState<string>("");
	const router = useRouter();

	const handleJoinMeeting = (e: React.FormEvent<HTMLFormElement>) => {
		e.preventDefault();
		router.push(`${link}`);
	};

	return (
		<>
			<DialogTitle
				as='h3'
				className='text-lg font-bold leading-6 text-green-600'
			>
				Rejoindre FaceTime
			</DialogTitle>

			<form className='w-full' onSubmit={handleJoinMeeting}>
				<label
					className='block text-left text-sm font-medium text-gray-700'
					htmlFor='link'
				>
					Entrez le lien FaceTime
				</label>
				<input
					type='url'
					name='link'
					id='link'
					value={link}
					onChange={(e) => setLink(e.target.value)}
					className='mt-1 block w-full text-sm py-3 px-4 border-gray-200 border-[1px] rounded mb-3'
					placeholder='Entrez le lien FaceTime'
				/>

				<button className='w-full bg-green-600 text-white py-3 rounded mt-4'>
					Rejoindre maintenant
				</button>
			</form>
		</>
	);
};
```

![facetime-app-join-popup](https://cdn.hashnode.com/res/hashnode/image/upload/v1726482173301/09881faa-54f8-4293-a186-b608ef5a0e05.png align="center")

Félicitations ! Vous avez terminé l'interface de l'application.

## Comment authentifier les utilisateurs avec Clerk

[Clerk](https://clerk.com/) est une plateforme de gestion des utilisateurs qui vous permet d'ajouter une authentification aux applications web.

Vous pouvez installer le [Clerk Next.js SDK](https://clerk.com/docs/quickstarts/nextjs) en exécutant l'extrait de code suivant dans votre terminal :

```bash
npm install @clerk/nextjs
```

Créez un fichier `middleware.ts` dans le dossier `src` de Next.js et copiez l'extrait de code ci-dessous dans le fichier :

```typescript
import { clerkMiddleware, createRouteMatcher } from "@clerk/nextjs/server";

const protectedRoutes = createRouteMatcher([
	"/facetime(.*)",
	"/dashboard",
	"/",
]);

//👇🏻 protège la route
export default clerkMiddleware((auth, req) => {
	if (protectedRoutes(req)) {
		auth().protect();
	}
});

export const config = {
	matcher: ["/((?!.*\\\\..*|_next).*)", "/", "/(api|trpc)(.*)"],
};
```

La fonction `createRouteMatcher` accepte un tableau contenant les routes à protéger des utilisateurs non authentifiés et la fonction `clerkMiddleware()` garantit que les routes sont protégées.

Ensuite, importez les composants Clerk suivants dans le fichier `app/layout.tsx` et mettez à jour la fonction `RootLayout` comme indiqué ci-dessous :

```typescript
import {
	ClerkProvider,
	SignInButton,
	SignedIn,
	SignedOut,
	UserButton,
} from "@clerk/nextjs";
import "./globals.css";

export default function RootLayout({
	children,
}: {
	children: React.ReactNode;
}) {
	return (
		<ClerkProvider>
			<html lang='en'>
				<body className={inter.className}>
					<nav className='w-full py-4 md:px-8 px-4 text-center flex items-center justify-between sticky top-0 bg-white '>
						<div className='flex items-center justify-end gap-5'>
							{/*-- si l'utilisateur est déconnecté --*/}
							<SignedOut>
								<SignInButton mode='modal' />
							</SignedOut>
							{/*-- si l'utilisateur est connecté --*/}
							<SignedIn>
								<UserButton />
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

Une fois cela fait, les utilisateurs seront invités à créer un compte ou à se connecter avant de pouvoir accéder aux pages de l'application.

Enfin, créez un [compte Clerk](https://clerk.com) et configurez une nouvelle application Clerk. Ajoutez vos clés Clerk (publique et secrète) au fichier `.env.local` de votre projet.

```bash
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=<publishable_key>
CLERK_SECRET_KEY=<secret_key>
```

## Comment configurer Stream dans une application Next.js

Tout d'abord, créez un [compte Stream](https://getstream.io/) et configurez une organisation pour héberger votre application. Ensuite, copiez les identifiants suivants dans votre fichier `.env.local` :

```bash
STREAM_APP_ID=<votre_id_app>
NEXT_PUBLIC_STREAM_API_KEY=<votre_cle_api_stream>
STREAM_SECRET_KEY=<votre_cle_secrete_stream>
NEXT_PUBLIC_FACETIME_HOST=http://localhost:3000/facetime
```

Ensuite, installez le [Stream React Video SDK](https://www.npmjs.com/package/@stream-io/video-react-sdk) et le [Stream Node.js SDK](https://getstream.io/video/docs/api/#installation).

```bash
npm install @stream-io/video-react-sdk @stream-io/node-sdk
```

Créez un dossier `providers` contenant un fichier `StreamVideoProvider.tsx` et copiez l'extrait de code suivant dans le fichier :

```typescript
"use client";
import { tokenProvider } from "@/actions/stream.actions";
import { StreamVideo, StreamVideoClient } from "@stream-io/video-react-sdk";
import { useState, ReactNode, useEffect } from "react";
import { useUser } from "@clerk/nextjs";

const apiKey = process.env.NEXT_PUBLIC_STREAM_API_KEY!;

export const StreamVideoProvider = ({ children }: { children: ReactNode }) => {
	const [videoClient, setVideoClient] = useState<StreamVideoClient>();

	const { user, isLoaded } = useUser();

	useEffect(() => {
		if (!isLoaded || !user || !apiKey) return;
		if (!tokenProvider) return;
		const client = new StreamVideoClient({
			apiKey,
			user: {
				id: user?.id,
				name: user?.primaryEmailAddress?.emailAddress,
				image: user?.imageUrl,
			},
			tokenProvider, //👉🏻 en attente de création
		});

		setVideoClient(client);
	}, [user, isLoaded]);

	if (!videoClient) return null;

	return <StreamVideo client={videoClient}>{children}</StreamVideo>;
};
```

Enveloppons toute l'application avec le composant `StreamVideoProvider`, qui initialise un client Stream pour identifier chaque utilisateur.

La fonction `StreamVideoClient` prend un objet contenant la clé API, l'objet utilisateur avec les détails de Clerk, et un `tokenProvider`.

Ensuite, créons une [action serveur Next.js](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations) (`tokenProvider`) qui génère le jeton.

Créez un dossier `actions`, ajoutez un fichier `stream.actions.ts`, et copiez l'extrait de code suivant dans le fichier :

```typescript
//👇🏻 fonction tokenProvider
"use server";

import { currentUser } from "@clerk/nextjs/server";
import { StreamClient } from "@stream-io/node-sdk";

const STREAM_API_KEY = process.env.NEXT_PUBLIC_STREAM_API_KEY!;
const STREAM_API_SECRET = process.env.STREAM_SECRET_KEY!;

export const tokenProvider = async () => {
	const user = await currentUser();

	if (!user) throw new Error("L'utilisateur n'est pas authentifié");
	if (!STREAM_API_KEY) throw new Error("La clé API Stream est manquante");
	if (!STREAM_API_SECRET) throw new Error("Le secret API Stream est manquant");

	const streamClient = new StreamClient(STREAM_API_KEY, STREAM_API_SECRET);

	const expirationTime = Math.floor(Date.now() / 1000) + 3600;
	const issuedAt = Math.floor(Date.now() / 1000) - 60;

	//👇🏻 génère un jeton utilisateur Stream
	const token = streamClient.generateUserToken({
		user_id: user.id,
		exp: expirationTime,
		validity_in_seconds: issuedAt,
	});
	//👇🏻 retourne le jeton utilisateur
	return token;
};
```

Enfin, mettez à jour la fonction `RootLayout` dans le fichier `app/layout.tsx` en enveloppant toute l'application avec le composant `StreamVideoProvider` :

```typescript
import "@stream-io/video-react-sdk/dist/css/styles.css";
import { StreamVideoProvider } from "./providers/StreamVideoProvider";

export default function RootLayout({
	children,
}: {
	children: React.ReactNode;
}) {
	return (
		<ClerkProvider>
			<html lang='en'>
				<body className={inter.className}>
					<StreamVideoProvider>
						<nav className='w-full py-4 md:px-8 px-4 text-center flex items-center justify-between sticky top-0 bg-white '>
							<div className='flex items-center justify-end gap-5'>
								{/*-- si l'utilisateur est déconnecté --*/}
								<SignedOut>
									<SignInButton mode='modal' />
								</SignedOut>
								{/*-- si l'utilisateur est connecté --*/}
								<SignedIn>
									<UserButton />
								</SignedIn>
							</div>
						</nav>

						{children}
					</StreamVideoProvider>
				</body>
			</html>
		</ClerkProvider>
	);
}
```

Félicitations ! Vous avez intégré avec succès Stream dans l'application Next.js.

## Comment créer et rejoindre des appels avec Stream

Dans cette section, vous apprendrez à créer, planifier et rejoindre des appels à l'aide du SDK Stream. Vous apprendrez également à configurer la salle de réunion avec les composants nécessaires et à récupérer les appels à venir depuis Stream.

### Création et planification d'appels

Pour créer une réunion instantanée, exécutez la fonction `handleStartMeeting`. Elle génère un ID aléatoire pour l'appel et crée la réunion en utilisant la date actuelle et la description fournie.

```typescript
import { useStreamVideoClient } from "@stream-io/video-react-sdk";
import { useUser } from "@clerk/nextjs";
const client = useStreamVideoClient();
const { user } = useUser();

const handleStartMeeting = async (e: React.FormEvent<HTMLFormElement>) => {
	e.preventDefault();
	if (!client || !user) return;
	try {
		const id = crypto.randomUUID();
		const call = client.call("default", id);
		if (!call) throw new Error("Échec de la création de la réunion");

		await call.getOrCreate({
			data: {
				starts_at: new Date(Date.now()).toISOString(),
				custom: {
					description,
				},
			},
		});

		setFacetimeLink(`${call.id}`);
		setShowMeetingLink(true);
	} catch (error) {
		console.error(error);
		alert("Échec de la création de la réunion");
	}
};
```

La fonction `call.getOrCreate()` accepte une description d'appel facultative ainsi que la date et l'heure actuelles pour initier l'appel.

Elle vous permet également de planifier des appels pour une heure spécifique dans le futur. Dans ce cas, vous pouvez spécifier la date et l'heure souhaitées, et Stream planifiera automatiquement l'appel pour cette période.

```typescript
import { useStreamVideoClient } from "@stream-io/video-react-sdk";
import { useUser } from "@clerk/nextjs";
const client = useStreamVideoClient();
const { user } = useUser();

const handleScheduleMeeting = async (e: React.FormEvent<HTMLFormElement>) => {
	e.preventDefault();
	if (!client || !user) return;
	try {
		const id = crypto.randomUUID();
		const call = client.call("default", id);
		if (!call) throw new Error("Échec de la création de la réunion");

		await call.getOrCreate({
			data: {
				//👇🏻 seules les modifications nécessaires
				starts_at: new Date(dateTime).toISOString(),
				custom: {
					description,
				},
			},
		});
		setFacetimeLink(`${call.id}`);
		setShowMeetingLink(true);
	} catch (error) {
		console.error(error);
		console.error("Échec de la création de la réunion");
	}
};
```

### Rejoindre des appels et la page de réunion

Rappelez-vous que le lien de réunion dans l'application est déclaré comme suit :

```jsx
`${process.env.NEXT_PUBLIC_FACETIME_HOST}/${facetimeLink}`
// 👉🏻 format: <http://localhost:3000/facetime/><call.id>
```

Par conséquent, nous devons créer la route `/facetime/<callID>` pour permettre aux utilisateurs de rejoindre un appel. Pour ce faire, créez un dossier `facetime` avec un répertoire `[id]` à l'intérieur, et dans ce répertoire, ajoutez un fichier `page.tsx`. Ensuite, copiez l'extrait de code suivant dans le fichier :

```typescript
"use client";
import { useGetCallById } from "@/app/hooks/useGetCallById";
import { useUser } from "@clerk/nextjs";
import {
	StreamCall,
	StreamTheme,
	PaginatedGridLayout,
	CallControls,
} from "@stream-io/video-react-sdk";
import { useParams, useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export default function FaceTimePage() {
	const { id } = useParams<{ id: string }>();
	const [confirmJoin, setConfirmJoin] = useState<boolean>(false);
	const [camMicEnabled, setCamMicEnabled] = useState<boolean>(false);
	const router = useRouter();
	//👇🏻 obtient les détails de l'appel par ID
	const { call, isCallLoading } = useGetCallById(id);

	useEffect(() => {
		if (camMicEnabled) {
			call?.camera.enable();
			call?.microphone.enable();
		} else {
			call?.camera.disable();
			call?.microphone.disable();
		}
	}, [call, camMicEnabled]);

	//👇🏻 permet aux utilisateurs de rejoindre des appels
	const handleJoin = () => {
		call?.join();
		setConfirmJoin(true);
	};

	if (isCallLoading) return <p>Chargement...</p>;

	if (!call) return <p>Appel non trouvé</p>;

	return (
		<main className='min-h-screen w-full items-center justify-center'>
			<StreamCall call={call}>
				<StreamTheme>
					{confirmJoin ? (
						<MeetingRoom />
					) : (
						<div className='flex flex-col items-center justify-center gap-5'>
							<h1 className='text-3xl font-bold'>Rejoindre l'appel</h1>
							<p className='text-lg'>
								Êtes-vous sûr de vouloir rejoindre cet appel ?
							</p>
							<div className='flex gap-5'>
								<button
									onClick={handleJoin}
									className='px-4 py-3 bg-green-600 text-green-50'
								>
									Rejoindre
								</button>
								<button
									onClick={() => router.push("/")}
									className='px-4 py-3 bg-red-600 text-red-50'
								>
									Annuler
								</button>
							</div>
						</div>
					)}
				</StreamTheme>
			</StreamCall>
		</main>
	);
}
```

Lorsque les utilisateurs visitent la page de réunion, un message de confirmation s'affiche, leur permettant de confirmer qu'ils souhaitent rejoindre l'appel.

![facetime-app-live](https://cdn.hashnode.com/res/hashnode/image/upload/v1726483083226/26ccb1d9-dc33-4a31-81a9-c4b0a3d00b91.png align="center")

Dans l'extrait de code ci-dessus :

* Le hook `useGetCallById` est une fonction personnalisée qui récupère les détails de l'appel en fonction de l'ID de l'appel.
    
* La fonction `handleJoin` permet aux utilisateurs de rejoindre l'appel puis affiche le composant `<MeetingRoom />`.
    

Ajoutez le composant `MeetingRoom` sous le composant `FaceTimePage` :

```typescript
const MeetingRoom = () => {
	const router = useRouter();

	const handleLeave = () => {
		confirm("Êtes-vous sûr de vouloir quitter l'appel ?") && router.push("/");
	};

	return (
		<section className='relative min-h-screen w-full overflow-hidden pt-4'>
			<div className='relative flex size-full items-center justify-center'>
				<div className='flex size-full max-w-[1000px] items-center'>
					<PaginatedGridLayout />
				</div>
				<div className='fixed bottom-0 flex w-full items-center justify-center gap-5'>
					<CallControls onLeave={handleLeave} />
				</div>
			</div>
		</section>
	);
};
```

Le [`PaginatedGridLayout`](https://getstream.io/video/docs/react/ui-components/core/call-layout/#paginatedgridlayout) organise les participants dans une disposition en grille avec pagination, vous permettant de gérer des appels vidéo plus importants en affichant un nombre défini de participants par page.

Le composant `CallControls` fournit des actions intégrées, telles que la coupure du son, l'activation/désactivation de la vidéo et le partage d'écran, qui peuvent être effectuées pendant un appel. Les deux composants font partie du SDK Stream, ce qui rend l'intégration transparente.

De plus, vous pouvez passer au [`SpeakerLayout`](https://getstream.io/video/docs/react/ui-components/core/call-layout/#speakerlayout), qui met en avant l'orateur principal ou l'écran partagé tout en affichant les autres participants dans une vue plus petite.

Enfin, créez un dossier `hooks` contenant le fichier `useGetCallById.ts` et copiez l'extrait de code ci-dessous dans le fichier :

```typescript
import { useEffect, useState } from "react";
import { Call, useStreamVideoClient } from "@stream-io/video-react-sdk";

export const useGetCallById = (id: string | string[]) => {
	const [call, setCall] = useState<Call>();
	const [isCallLoading, setIsCallLoading] = useState(true);

	const client = useStreamVideoClient();

	useEffect(() => {
		if (!client) return;

		const loadCall = async () => {
			try {
				const { calls } = await client.queryCalls({
					filter_conditions: { id },
				});

				if (calls.length > 0) setCall(calls[0]);

				setIsCallLoading(false);
			} catch (error) {
				console.error(error);
				setIsCallLoading(false);
			}
		};

		loadCall();
	}, [client, id]);

	return { call, isCallLoading };
};
```

L'extrait de code ci-dessus filtre la liste des appels et [renvoie l'appel avec un ID correspondant](https://getstream.io/video/docs/react/guides/querying-calls/#filters), permettant aux utilisateurs de rejoindre l'appel spécifié.

### Récupération des appels à venir

Pour récupérer les appels à venir depuis Stream, vous pouvez créer un hook personnalisé qui [récupère tous les appels créés par l'utilisateur](https://getstream.io/video/docs/react/guides/querying-calls/#calls-the-user-has-created-or-is-a-member-of), ainsi que les appels dont il est membre.

```typescript
import { useEffect, useState } from "react";
import { useUser } from "@clerk/nextjs";
import { Call, useStreamVideoClient } from "@stream-io/video-react-sdk";

export const useGetCalls = () => {
	const { user } = useUser();
	const client = useStreamVideoClient();
	const [calls, setCalls] = useState<Call[]>();
	const [isLoading, setIsLoading] = useState(false);

	useEffect(() => {
		const loadCalls = async () => {
			if (!client || !user?.id) return;
			setIsLoading(true);
			try {
				//👇🏻 obtient tous les appels dans lesquels l'utilisateur figure
				const { calls } = await client.queryCalls({
					sort: [{ field: "starts_at", direction: -1 }],
					filter_conditions: {
						starts_at: { $exists: true },
						$or: [
							{ created_by_user_id: user.id },
							{ members: { $in: [user.id] } },
						],
					},
				});

				setCalls(calls);
			} catch (error) {
				console.error(error);
			} finally {
				setIsLoading(false);
			}
		};

		loadCalls();
	}, [client, user?.id]);

	const now = new Date();

	//👇🏻 obtient uniquement les appels qui n'ont pas encore commencé
	const upcomingCalls = calls?.filter(({ state: { startsAt } }: Call) => {
		return startsAt && new Date(startsAt) > now;
	});

	return { upcomingCalls, isLoading };
};
```

Le hook `useGetCalls` [récupère la liste des appels à venir](https://getstream.io/video/docs/react/guides/querying-calls/#calls-the-user-has-created-or-is-a-member-of), qui peut ensuite être affichée dans le modal `UpcomingMeeting`.

Félicitations ! Vous avez terminé le projet de ce tutoriel.

Découvrez l'application en direct [ici.](https://facetime-on-stream.vercel.app/)

## Prochaines étapes

Jusqu'à présent, vous avez appris à construire une application de visioconférence. Si vous souhaitez en savoir plus sur la manière dont vous pouvez exploiter Stream pour construire des applications évolutives, consultez ces ressources :

* [Comment intégrer Stream Chat Messaging](https://getstream.io/chat/)
    
* [Comment intégrer les appels audio et vidéo Stream](https://getstream.io/video/)
    
* [Comment intégrer les flux d'activité Stream](https://getstream.io/activity-feeds/)
    

## **Avant de terminer...**

J'espère que vous l'avez trouvé instructif et que cela vous a donné suffisamment de motivation sur la façon de construire des applications en utilisant des outils de développement géniaux.

Voici quelques-uns de mes autres articles de blog les plus récents.

* [État des bases de données pour le Serverless en 2024](https://www.devtoolsacademy.com/blog/state-of-databases-2024)
    
* [**Neon Postgres vs Supabase**](https://www.devtoolsacademy.com/blog/neon-vs-supabase)
    
* [**MongoDB vs. PostgreSQL**](https://www.devtoolsacademy.com/blog/mongoDB-vs-postgreSQL)
    

Consultez [mon blog](https://theankurtyagi.com/) pour plus de tutoriels comme celui-ci sur des outils de développement géniaux.

Suivez-moi sur [Twitter](https://x.com/theankurtyagi) pour rester informé de mes projets secondaires et de mon apprentissage continu.

Bon codage.