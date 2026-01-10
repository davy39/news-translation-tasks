---
title: Comment construire une plateforme d'apprentissage social en utilisant Next.js,
  Stream et Supabase
subtitle: Apprenez à construire une plateforme d'apprentissage social qui connecte
  les étudiants avec des professionnels de divers domaines.
author: David Asaolu
co_authors: []
series: null
date: '2025-03-03T15:10:15.095Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-social-learning-platform-using-nextjs-stream-and-supabase
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1741009946459/dba65929-1b65-4278-9601-4d047042753a.png
tags:
- name: React
  slug: reactjs
- name: Next.js
  slug: nextjs
- name: Web Development
  slug: web-development
- name: Tutorial
  slug: tutorial
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Comment construire une plateforme d'apprentissage social en utilisant Next.js,
  Stream et Supabase
seo_desc: Social media and real-time communication have transformed how people interact,
  making it easier to share ideas, collaborate, and learn from others, regardless
  of location. From professional networks to online study groups, these platforms
  allow vario...
---

Les médias sociaux et la communication en temps réel ont transformé la manière dont les gens interagissent, rendant plus facile le partage d'idées, la collaboration et l'apprentissage des autres, indépendamment de la localisation. Des réseaux professionnels aux groupes d'étude en ligne, ces plateformes permettent diverses formes de communication telles que la messagerie instantanée, les appels vidéo et le partage de contenu.

Dans ce tutoriel, vous apprendrez à construire une plateforme d'apprentissage social qui connecte les étudiants avec des professionnels de divers domaines. La plateforme permet aux utilisateurs de :

* Planifier des sessions de visioconférence que les étudiants peuvent rejoindre,

* Partager des publications ou des annonces sur les outils tendance et les sessions à venir, et

* Créer des canaux communautaires où les étudiants peuvent interagir les uns avec les autres.

Le [Stream Video & Audio SDK](https://getstream.io/video/sdk/) et le [Stream Chat SDK](https://getstream.io/chat/sdk/) nous permettront d'intégrer facilement des appels vidéo et des canaux communautaires dans l'application.

![Personnage de dessin animé avec des cheveux roses et des lunettes vertes tenant un smartphone, qui affiche des emojis de cœur, de caca et de smiley sur l'écran.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740662075821/1a004f19-4889-4b57-921b-062cf1927261.gif align="center")

## Table des matières

* [Aperçu de l'application](#heading-apercu-de-lapplication)

* [Prérequis](#heading-prerequis)

* [Comment configurer l'authentification côté serveur avec Supabase](#heading-comment-configurer-lauthentification-cote-serveur-avec-supabase)

  * [Comment configurer l'authentification Supabase dans une application Next.js](#heading-comment-configurer-lauthentification-supabase-dans-une-application-nextjs)

  * [Authentification des étudiants avec Supabase](#heading-authentification-des-etudiants-avec-supabase)

  * [Authentification des instructeurs avec Supabase](#heading-authentification-des-instructeurs-avec-supabase)

* [Conception de la base de données de l'application](#heading-conception-de-la-base-de-donnees-de-lapplication)

  * [Politique d'accès pour la table des annonces](#heading-politique-dacces-pour-la-table-des-annonces)

  * [Politique d'accès pour la table des instructeurs](#heading-politique-dacces-pour-la-table-des-instructeurs)

  * [Politique d'accès pour la table des étudiants](#heading-politique-dacces-pour-la-table-des-etudiants)

* [Comment ajouter une fonctionnalité de visioconférence avec Stream](#heading-comment-ajouter-une-fonctionnalite-de-visioconference-avec-stream)

  * [Configuration du Stream Video & Audio SDK dans Next.js](#heading-configuration-du-stream-video-audio-sdk-dans-nextjs)

  * [Création et planification des appels avec Stream](#heading-creation-et-planification-des-appels-avec-stream)

  * [Rejoindre les appels vidéo Stream](#heading-rejoindre-les-appels-video-stream)

  * [Composants UI des appels Stream](#heading-composants-ui-des-appels-stream)

* [Comment intégrer une fonctionnalité de chat de groupe en utilisant Stream Chat Messaging](#heading-comment-integrer-une-fonctionnalite-de-chat-de-groupe-en-utilisant-stream-chat-messaging)

  * [Configuration du Stream Chat SDK dans Next.js](#heading-configuration-du-stream-chat-sdk-dans-nextjs)

  * [Composants UI de Stream Chat](#heading-composants-ui-de-stream-chat)

* [Prochaines étapes](#heading-prochaines-etapes)

## Aperçu de l'application

L'application se compose de deux types d'utilisateurs (étudiants et instructeurs), chacun ayant accès à des fonctionnalités spécifiques :

Les étudiants peuvent faire ce qui suit :

* Voir un fil d'actualité avec des publications d'instructeurs et y réagir.

* Suivre des instructeurs dans leur domaine d'intérêt.

* Rejoindre des sessions vidéo à venir et des canaux communautaires.

* Chaque étudiant a un attribut d'intérêt qui aide à les associer avec des instructeurs pertinents.

Les instructeurs peuvent également :

* Accéder à un tableau de bord montrant leur nombre d'abonnés et l'activité des publications.

* Planifier des visioconférences pour que les étudiants puissent rejoindre.

* Faire des annonces ou partager des publications.

* Créer des canaux communautaires (s'ils ne l'ont pas déjà fait).

* La plateforme suggère des instructeurs aux étudiants en fonction des intérêts de carrière partagés.

Voici une image montrant les différentes fonctions que les utilisateurs peuvent effectuer :

![Organigramme intitulé "Fonctions des utilisateurs" montrant une hiérarchie. "Utilisateurs" se divise en "Étudiants" et "Instructeurs". Les étudiants peuvent "Suivre les instructeurs", "Rejoindre les sessions vidéo", "Rejoindre les canaux communautaires" et "Lire et réagir aux publications". Les instructeurs peuvent "Voir le tableau de bord", "Créer des publications", "Planifier des sessions vidéo" et "Créer des canaux communautaires".](https://cdn.hashnode.com/res/hashnode/image/upload/v1740723106527/fd8af07a-1919-42f0-9e9a-ed380a0b77cc.png align="center")

## Prérequis

Pour comprendre pleinement ce tutoriel, vous devez avoir une compréhension de base de React ou Next.js.

Nous utiliserons les outils suivants :

* [Supabase](https://supabase.com/docs) : une plateforme Backend-as-a-service qui facilite l'intégration de l'authentification, de la base de données, de la communication en temps réel, du stockage de fichiers et des fonctions edge dans vos applications logicielles. Elle prend également en charge plusieurs langages de programmation.

* [Stream Chat](https://getstream.io/chat/docs/sdk/react/) et [Audio & Video SDK](https://getstream.io/video/docs/react/) : une plateforme de communication en temps réel qui vous permet d'ajouter de la vidéo, du chat et divers types de communication à votre application.

* [Shadcn UI](https://ui.shadcn.com/docs/installation/next) : une bibliothèque de composants UI qui fournit des composants UI personnalisables, magnifiquement conçus et accessibles pour vos applications.

Créez un projet Next.js en exécutant le code suivant :

```bash
npx create-next-app stream-lms
```

Installez les dépendances du package pour le projet :

```bash
npm install @supabase/supabase-js @supabase/ssr @stream-io/node-sdk @stream-io/video-react-sdk stream-chat stream-chat-react @emoji-mart/data @emoji-mart/react
```

Pour installer la bibliothèque Shadcn UI, suivez [le guide d'installation](https://ui.shadcn.com/docs/installation/next).

Une fois tout configuré, votre projet Next.js est prêt. Maintenant, commençons à construire ! 🚀

## Comment configurer l'authentification côté serveur avec Supabase

Ici, vous apprendrez à configurer Supabase, à ajouter une authentification côté serveur et à protéger les pages contre les utilisateurs non autorisés dans une application Next.js. Vous apprendrez également à gérer la logique d'authentification efficacement en utilisant [les actions serveur de Next.js](https://nextjs.org/docs/13/app/api-reference/functions/server-actions#with-client-components).

### Comment configurer l'authentification Supabase dans une application Next.js

Tout d'abord, créez un [compte Supabase](https://supabase.com/) et une organisation qui contiendra vos divers projets Supabase.

![Capture d'écran d'un formulaire sur le site web de Supabase pour créer une nouvelle organisation. Il comprend des champs pour le nom de l'organisation, le type et le plan, avec des options telles que "Personnel" et "Gratuit - 0 $/mois". Il y a des boutons pour "Annuler" et "Créer une organisation".](https://cdn.hashnode.com/res/hashnode/image/upload/v1740653729412/35339612-4688-489e-b9d2-2cc825962519.png align="center")

Ajoutez un nouveau projet Supabase à l'organisation et copiez les informations d'identification suivantes de votre tableau de bord dans un fichier `.env.local` à la racine de votre projet :

```bash
NEXT_PUBLIC_SUPABASE_ANON_KEY=<anon_key_from_Supabase_dashboard>
NEXT_PUBLIC_SUPABASE_URL=<supabase_project_url>
```

Créez un dossier `utils/supabase` à la racine du projet Next.js et ajoutez les fichiers suivants au dossier : `client.ts`, `middleware.ts` et `server.ts`.

```bash
mkdir utils && cd utils
mkdir supabase && cd supabase
touch client.ts middleware.ts server.ts
```

Copiez le code suivant dans `utils/supabase/client.ts`. Cela initialise un client Supabase pour le navigateur afin d'interagir avec Supabase sur les routes côté client :

```typescript
import { createBrowserClient } from "@supabase/ssr";

export function createClient() {
	return createBrowserClient(
		process.env.NEXT_PUBLIC_SUPABASE_URL!,
		process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
	);
}
```

Ensuite, copiez le code suivant dans `utils/supabase/server.ts`. Cela crée un client serveur Supabase pour gérer l'authentification et interagir avec Supabase dans les requêtes côté serveur :

```typescript
import { createServerClient } from "@supabase/ssr";
import { cookies } from "next/headers";

export async function createClient() {
	const cookieStore = await cookies();

	return createServerClient(
		process.env.NEXT_PUBLIC_SUPABASE_URL!,
		process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
		{
			cookies: {
				getAll() {
					return cookieStore.getAll();
				},
				setAll(cookiesToSet) {
					try {
						cookiesToSet.forEach(({ name, value, options }) =>
							cookieStore.set(name, value, options)
						);
					} catch {
						// La méthode `setAll` a été appelée depuis un composant serveur.
						// Cela peut être ignoré si vous avez un middleware actualisant
						// les sessions utilisateur.
					}
				},
			},
		}
	);
}
```

Maintenant, copiez le code suivant dans `utils/supabase/middleware.ts`. Ce middleware crée des cookies d'authentification et protège les pages contre les accès non autorisés :

```typescript
import { createServerClient } from "@supabase/ssr";
import { NextResponse, type NextRequest } from "next/server";

export async function updateSession(request: NextRequest) {
	let supabaseResponse = NextResponse.next({
		request,
	});
	//👋🏽 crée les fonctions de cookie Supabase
	const supabase = createServerClient(
		process.env.NEXT_PUBLIC_SUPABASE_URL!,
		process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
		{
			cookies: {
				getAll() {
					return request.cookies.getAll();
				},
				setAll(cookiesToSet) {
					cookiesToSet.forEach(({ name, value }) =>
						request.cookies.set(name, value)
					);
					supabaseResponse = NextResponse.next({
						request,
					});
					cookiesToSet.forEach(({ name, value, options }) =>
						supabaseResponse.cookies.set(name, value, options)
					);
				},
			},
		}
	);

	// 👉🏽 placeholder pour le contrôleur de route protégée
}
```

Pour appliquer l'authentification, ajoutez le code suivant à l'intérieur du placeholder dans `middleware.ts`. Cela vérifie si un utilisateur est connecté et redirige les utilisateurs non authentifiés vers la page de connexion :

```typescript
//👋🏽 obtient l'utilisateur actuel
const {
	data: { user },
} = await supabase.auth.getUser();

//👋🏽 déclare les routes protégées
if (
	!user &&
	request.nextUrl.pathname !== "/" &&
	!request.nextUrl.pathname.startsWith("/instructor/auth") &&
	!request.nextUrl.pathname.startsWith("/student/auth")
) {
	//👋🏽 Redirige les utilisateurs non authentifiés vers la page de connexion
	const url = request.nextUrl.clone();
	url.pathname = "/student/auth/login"; // 👉🏽 page de redirection
	return NextResponse.redirect(url);
}
//👋🏽 retourne la réponse Supabase
return supabaseResponse;
```

Ajoutez un autre fichier `middleware.ts` à la racine du projet Next.js et copiez le code suivant dans le fichier :

```typescript
import { type NextRequest } from "next/server";
import { updateSession } from "./utils/supabase/middleware";

export async function middleware(request: NextRequest) {
	return await updateSession(request);
}

export const config = {
	matcher: [
		/*
		 * Correspond à tous les chemins de requête sauf ceux commençant par :
		 * - _next/static (fichiers statiques)
		 * - _next/image (fichiers d'optimisation d'image)
		 * - favicon.ico (fichier favicon)
		 * N'hésitez pas à modifier ce motif pour inclure plus de chemins.
		 */
		"/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)",
	],
};
```

Enfin, créez une route [**auth/confirm**](https://github.com/dha-stix/stream-lms/blob/main/src/app/auth/confirm/route.ts) et une page [**error**](https://github.com/dha-stix/stream-lms/blob/main/src/app/error/page.tsx) dans le dossier de l'application Next.js.

Vous avez réussi à [configurer l'authentification dans votre projet Next.js](https://supabase.com/docs/guides/auth/server-side/nextjs) en utilisant Supabase.

### Authentification des étudiants avec Supabase

Dans cette section, vous apprendrez à créer les fonctions d'inscription et de connexion pour les étudiants au sein de l'application.

Tout d'abord, créez un dossier **actions** à la racine de votre projet Next.js et ajoutez un fichier `auth.ts` à l'intérieur. Ce fichier contiendra toutes les fonctions d'authentification Supabase.

Ajoutez les imports suivants en haut du fichier `auth.ts` :

```typescript
"use server";
import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { createClient } from "../utils/supabase/server";
```

Ensuite, vous devez créer les fonctions serveur qui acceptent les données de formulaire du client et inscrivent les utilisateurs ou les connectent en tant qu'étudiants.

Copiez le code suivant dans le fichier `actions/auth.ts` pour créer la fonction d'inscription de l'utilisateur :

```typescript
export async function studentSignUp(formData: FormData) {
	const supabase = await createClient();

	//👋🏽 Extraire les données du formulaire
	const credentials = {
		email: formData.get("email") as string,
		password: formData.get("password") as string,
		interest: formData.get("interest") as string,
		name: formData.get("name") as string,
	};

	//👋🏽 Fonction d'inscription Supabase (attribut options :- pour les métadonnées de l'utilisateur)
	const { data, error } = await supabase.auth.signUp({
		email: credentials.email,
		password: credentials.password,
		options: {
			data: {
				interest: credentials.interest,
				name: credentials.name,
			},
		},
	});

	//👉🏽 retourner l'objet utilisateur ou erreur
}
```

Le code ci-dessus accepte les informations d'identification du formulaire telles que l'email, le mot de passe, l'intérêt et le nom, et inscrit l'utilisateur en tant qu'utilisateur Supabase.

Modifiez la fonction pour retourner l'utilisateur ou l'objet erreur.

```typescript
export async function studentSignUp(formData: FormData) {
	//...form inputs and supabase functions

	if (error) {
		return { error: error.message, status: error.status, user: null };
	} else if (data.user?.identities?.length === 0) {
		return { error: "User already exists", status: 409, user: null };
	}

	revalidatePath("/", "layout");
	return { error: null, status: 200, user: data.user };
}
```

Créez la fonction de connexion de l'étudiant comme indiqué ci-dessous :

```typescript
export async function studentLogIn(formData: FormData) {
	const supabase = await createClient();

	const credentials = {
		email: formData.get("email") as string,
		password: formData.get("password") as string,
	};
	const { data, error } = await supabase.auth.signInWithPassword(credentials);

	if (error) {
		return { error: error.message, status: error.status, user: null };
	}
	//👋🏽 seuls les instructeurs ont un attribut image
	if (data && data.user.user_metadata.image) {
		return { error: "You are not a student", status: 400, user: null };
	}

	//👉🏽 créer une ligne d'étudiant et l'ajouter à la base de données

	revalidatePath("/", "layout");
	return { error: null, status: 200, user: data.user };
}
```

Le code ci-dessus prend l'email et le mot de passe de l'étudiant pour le connecter à l'application.

* Si une erreur se produit, il retourne un message d'erreur.

* Si l'objet utilisateur inclut un attribut image (indiquant qu'il s'agit d'un instructeur), il est empêché de se connecter.

Une fois l'étudiant connecté, vous devez stocker ses détails dans une table Supabase. Cela vous permet d'ajouter une colonne `following_list` qui suit les instructeurs qu'il suit. La liste sera mise à jour chaque fois que l'étudiant suit ou ne suit plus un instructeur.

```typescript
export async function studentLogIn(formData: FormData) {
	//...other functions

	const { data: existingUser } = await supabase
		.from("students")
		.select()
		.eq("email", credentials.email)
		.single();

	//👋🏽 si l'étudiant n'existe pas
	if (!existingUser) {
		const { error: insertError } = await supabase.from("students").insert({
			email: credentials.email,
			name: data.user.user_metadata.name,
			interest: data.user.user_metadata.interest,
			id: data.user.id,
			following_list: [] as string[],
		});

		if (insertError) {
			return { error: insertError.message, status: 500, user: null };
		}
	}

	revalidatePath("/", "layout");
	return { error: null, status: 200, user: data.user };
}
```

À chaque fois qu'un étudiant se connecte, le code vérifie s'il existe déjà dans la table `students`.

* Si l'étudiant est trouvé, aucune nouvelle entrée n'est créée.

* Si l'étudiant n'est pas trouvé, une nouvelle ligne avec ses détails est ajoutée.

Les données de chaque étudiant incluent deux clés primaires : `id` et `email` et des colonnes supplémentaires : `interest`, `name` et `following_list`.

![Formulaire d'inscription des étudiants avec des champs pour le nom complet, l'adresse email, l'intérêt et le mot de passe. Comprend un bouton "S'inscrire" et une option de connexion pour les comptes existants. L'onglet du navigateur montre l'URL "localhost:3000".](https://cdn.hashnode.com/res/hashnode/image/upload/v1740654932982/724fcf11-55e3-4163-9a6e-0b2771d0874c.gif align="center")

### Authentification des instructeurs avec Supabase

L'objet utilisateur de l'instructeur est assez différent de celui de l'étudiant. Il inclut des données telles que l'email, le mot de passe, le nom, l'intérêt, l'occupation, la bio, l'URL et l'image.

Ajoutez la fonction suivante à `actions/auth.ts` pour gérer les inscriptions des instructeurs :

```typescript
export async function instructorSignUp(formData: FormData) {
	const supabase = await createClient();

	//👋🏽 obtenir les informations d'identification de l'utilisateur à partir du formulaire
	const credentials = {
		email: formData.get("email") as string,
		password: formData.get("password") as string,
		interest: formData.get("interest") as string,
		name: formData.get("name") as string,
		occupation: formData.get("occupation") as string,
		bio: formData.get("bio") as string,
		url: formData.get("url") as string,
		image: formData.get("image") as File,
	};

	//👉🏽 extrait de code suivant ci-dessous
}
```

Ensuite, téléchargez l'image vers le stockage Supabase et récupérez son URL de téléchargement avant d'inscrire l'utilisateur en tant qu'instructeur. Mettez à jour la fonction `instructorSignUp` pour montrer cela :

```typescript
export async function instructorSignUp(formData: FormData) {
	//👋🏽 télécharger l'image de l'instructeur
	const { data: imageData, error: imageError } = await supabase.storage
		.from("headshots")
		.upload(`${crypto.randomUUID()}/image`, credentials.image);

	if (imageError) {
		return { error: imageError.message, status: 500, user: null };
	}
	//👋🏽 obtenir l'URL de l'image
	const imageURL = `${process.env.STORAGE_URL!}${imageData.fullPath}`;

	//👋🏽 authentifier l'utilisateur en tant qu'instructeur
	const { data, error } = await supabase.auth.signUp({
		email: credentials.email,
		password: credentials.password,
		options: {
			data: {
				interest: credentials.interest,
				name: credentials.name,
				occupation: credentials.occupation,
				bio: credentials.bio,
				url: credentials.url,
				image: imageURL,
			},
		},
	});

	//👋🏽 retourner l'objet utilisateur ou erreur
	if (error) {
		return { error: error.message, status: error.status, user: null };
	}

	revalidatePath("/", "layout");
	return { error: null, status: 200, user: data.user };
}
```

Enfin, une [fonction de connexion de l'instructeur](https://github.com/dha-stix/stream-lms/blob/main/actions/auth.ts) qui authentifie l'utilisateur, similaire à la fonction de connexion de l'étudiant, doit être créée. Elle doit vérifier si l'instructeur existe déjà dans la table `instructors`. Si l'instructeur n'existe pas, exécutez la fonction pour ajouter l'objet utilisateur de l'instructeur à la table de la base de données.

Voici la fonction Supabase pour ajouter un instructeur à la table :

```typescript
const { error: insertError } = await supabase.from("instructors").insert({
	email: credentials.email,
	name: data.user.user_metadata.name,
	occupation: data.user.user_metadata.occupation,
	bio: data.user.user_metadata.bio,
	url: data.user.user_metadata.url,
	image: data.user.user_metadata.image,
	id: data.user.id,
	interest: data.user.user_metadata.interest,
	followers: [],
});
```

La table `instructors` inclut un attribut supplémentaire `followers`, qui stocke un tableau d'IDs d'étudiants suivant l'instructeur. Vous pouvez trouver [le code complet sur GitHub](https://github.com/dha-stix/stream-lms/blob/main/actions/auth.ts).

De plus, des fonctions d'authentification comme [**getUserSession**](https://github.com/dha-stix/stream-lms/blob/main/actions/auth.ts) et [**logOut**](https://github.com/dha-stix/stream-lms/blob/main/actions/auth.ts) doivent être créées. Ces fonctions récupéreront l'objet utilisateur actuel et lui permettront de se déconnecter lorsque cela est nécessaire, comme lors du clic sur un bouton de déconnexion.

![Page de connexion de l'instructeur avec des champs pour l'email et le mot de passe, un bouton "Se connecter" et un lien pour créer un compte. Une barre latérale à gauche affiche "LinkedUp" avec un lien "Connexion étudiant".](https://cdn.hashnode.com/res/hashnode/image/upload/v1740655472825/4c038412-fe6d-4449-b2a9-d9d3649da2f8.gif align="center")

## Conception de la base de données de l'application

Dans la section précédente, nous avons créé deux tables de base de données : `instructors` et `students`, qui stockent les instructeurs et les étudiants séparément. Les instructeurs peuvent également télécharger des images de portrait vers [Supabase Storage](https://supabase.com/docs/guides/storage/quickstart).

Dans cette section, vous apprendrez à créer ces tables, à définir leurs politiques d'accès et à récupérer ou modifier les données dans les tables.

| **Announcements (type de données)** | **Instructors (type de données)** | **Students (type de données)** |
| --- | --- | --- |
| id (int8) | id (uuid) | id (uuid) |
| created\_at (timestamptz) | created\_at (timestamptz) | created\_at (timestamptz) |
| author\_name (text) | name (text) | email (text) |
| interest (text) | email (text) | name (text) |
| author\_title (text) | occupation (text) | interest (text) |
| author\_id (uuid) | bio (text) | following\_list (uuid\[\]) |
| content (text) | url (text) |  |
| likes (uuid \[\]) | interest (text) |  |
| author\_image (text) | image (text) |  |
|  | followers (uuid\[\]) |  |

**Note :** La table `instructors` inclut une colonne `image` qui stocke l'URL de la photo de l'instructeur. Vous pouvez obtenir cela en créant un bucket Supabase nommé `headshot` et en téléchargeant l'image lorsque l'instructeur s'inscrit.

Les tables `instructors` et `students` ont deux clés primaires : `id` et `email`.

Supabase vous permet de définir des politiques pour vos tables, contrôlant les opérations que différents utilisateurs peuvent effectuer au sein de l'application.

Ensuite, créons les politiques d'accès pour chaque table.

### Politique d'accès pour la table des annonces

La table `announcements` a quatre politiques d'accès :

* Activer l'opération de suppression pour les utilisateurs en fonction de leur ID utilisateur.

```sql
alter policy "Enable delete for users based on user_id"
on "public"."announcements"
to public
using (
  (( SELECT auth.uid() AS uid) = author_id)
);
```

* Activer l'opération d'insertion pour les utilisateurs authentifiés uniquement.

```sql
alter policy "Enable insert for authenticated users only"
on "public"."announcements"
to authenticated
with check (
  true
);
```

* Activer l'accès en lecture pour tous les utilisateurs.

```sql
alter policy "Enable read access for all users"
on "public"."announcements"
to public
using (
  true
);
```

* Activer l'opération de mise à jour pour les utilisateurs authentifiés uniquement.

```sql
alter policy "Enable update for authenticated users"
on "public"."announcements"
to authenticated
using (
  (auth.role() = 'authenticated'::text)
);
```

### Politique d'accès pour la table des instructeurs

La table `instructors` a trois politiques :

* Autoriser uniquement les utilisateurs authentifiés à mettre à jour la table `instructors`.

```sql
alter policy "Allow only authenticated users"
on "public"."instructors"
to authenticated
using (
  (auth.role() = 'authenticated'::text)
);
```

* Activer l'opération d'insertion pour les utilisateurs authentifiés uniquement.

```sql
alter policy "Enable insert for authenticated users only"
on "public"."instructors"
to authenticated
with check (
  true
);
```

* Activer l'accès en lecture pour tous les utilisateurs.

```sql
alter policy "Enable read access for all users"
on "public"."instructors"
to public
using (
  true
);
```

### Politique d'accès pour la table des étudiants

La table `students` a trois politiques :

* Activer l'opération d'insertion pour les utilisateurs authentifiés uniquement.

```sql
alter policy "Enable insert for authenticated users only"
on "public"."students"
to authenticated
with check (
  true
);
```

* Activer l'opération de mise à jour pour les utilisateurs authentifiés uniquement.

```sql
alter policy "Enable update for only authenticated users"
on "public"."students"
to authenticated
using ((auth.role() = 'authenticated'::text))
```

* Activer l'accès en lecture pour les utilisateurs authentifiés uniquement.

```sql
alter policy "Read access for only authenticated users"
on "public"."students"
to authenticated
using (
  true
);
```

## Comment ajouter une fonctionnalité de visioconférence avec Stream

Dans cette section, je vais vous guider à travers l'ajout d'une fonctionnalité de visioconférence à l'application en utilisant le [Stream Audio & Video SDK](https://getstream.io/video/docs/react/). Cela permettra aux instructeurs de planifier des sessions éducatives et aux étudiants de rejoindre les réunions.

### Configuration du Stream Video & Audio SDK dans Next.js

Créez un [compte Stream](https://getstream.io/) et une nouvelle organisation qui contient toutes vos applications.

![Formulaire pour créer une organisation, avec des champs pour le nom de l'organisation, l'adresse e-mail et l'URL du site web, et des boutons étiquetés "Annuler" et "Soumettre".](https://cdn.hashnode.com/res/hashnode/image/upload/v1740657831403/ba044353-b0f4-4380-82cf-5abeedd68ac9.png align="center")

Ajoutez une nouvelle application à l'organisation et copiez la clé API et la clé secrète de Stream dans le fichier `.env.local`.

```bash
NEXT_PUBLIC_STREAM_API_KEY=<paste_from_Stream_app_dashboard>
STREAM_SECRET_KEY=<paste_from_Stream_app_dashboard>
```

![Interface du tableau de bord affichant un aperçu du chat avec des métriques clés comme les utilisateurs actifs mensuels (4 MAUs), les connexions simultanées maximales (2) et le volume de messages (3). Inclut les clés d'accès à l'application créées le 17 février 2025.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740658025617/e8fb8a44-0a16-4730-875a-be3c2255276f.png align="center")

Créez un nouveau fichier nommé `stream.action.ts` à l'intérieur du dossier `actions` à la racine de votre projet Next.js. C'est le même dossier où sont stockées les actions serveur d'authentification pour Supabase. Ensuite, copiez le code suivant dans le fichier :

```typescript
"use server";

import { getUserSession } from "./auth";
import { StreamClient } from "@stream-io/node-sdk";

const STREAM_API_KEY = process.env.NEXT_PUBLIC_STREAM_API_KEY!;
const STREAM_API_SECRET = process.env.STREAM_SECRET_KEY!;

export const tokenProvider = async () => {
	const { user } = await getUserSession();

	if (!user) throw new Error("User is not authenticated");
	if (!STREAM_API_KEY) throw new Error("Stream API key secret is missing");
	if (!STREAM_API_SECRET) throw new Error("Stream API secret is missing");

	const streamClient = new StreamClient(STREAM_API_KEY, STREAM_API_SECRET);

	const expirationTime = Math.floor(Date.now() / 1000) + 3600;
	const issuedAt = Math.floor(Date.now() / 1000) - 60;

	const token = streamClient.generateUserToken({
		user_id: user.id,
		exp: expirationTime,
		validity_in_seconds: issuedAt,
	});

	return token;
};
```

* À partir de l'extrait de code ci-dessus,

  * La fonction **getUserSession** retourne l'objet utilisateur Supabase pour l'utilisateur actuel.

  * La fonction **tokenProvider** génère un jeton d'authentification pour l'utilisateur, permettant à Stream d'identifier et de gérer les utilisateurs pendant la communication en temps réel.

Créez un dossier `providers` contenant un composant `StreamVideoProvider` dans le dossier de l'application Next.js et copiez le code suivant dans le fichier :

```typescript
"use client";
import { createClient } from "../../../utils/supabase/client";
import { tokenProvider } from "../../../actions/stream.action";
import { StreamVideo, StreamVideoClient } from "@stream-io/video-react-sdk";
import { useState, ReactNode, useEffect, useCallback } from "react";
import { Loader2 } from "lucide-react";

const apiKey = process.env.NEXT_PUBLIC_STREAM_API_KEY!;

export const StreamVideoProvider = ({ children }: { children: ReactNode }) => {
	const [videoClient, setVideoClient] = useState<StreamVideoClient | null>(
		null
	);
	const supabase = createClient();

	const getUser = useCallback(async () => {
		//👉🏽 obtenir l'objet utilisateur de Supabase
		//👉🏽 définir les données utilisateur de Stream
		// 👉🏽 initialiser le client vidéo Stream en utilisant la clé API Stream, les données utilisateur Stream et le fournisseur de jetons
	}, [supabase.auth]);

	useEffect(() => {
		getUser();
	}, [getUser]);

	if (!videoClient)
		return (
			<div className='h-screen flex items-center justify-center'>
				<Loader2 size='32' className='mx-auto animate-spin' />
			</div>
		);

	return <StreamVideo client={videoClient}>{children}</StreamVideo>;
};
```

Le composant `StreamVideoProvider` est initialisé et gère les fonctionnalités vidéo de Stream dans l'application. Il enveloppe toutes les pages qui nécessitent un accès aux fonctionnalités vidéo en temps réel de Stream. Cela inclut :

* `instructor/[id]` – affiche les sessions à venir d'un instructeur.

* `instructor/dashboard` – permet aux instructeurs de planifier de nouveaux appels vidéo.

Mettez à jour la fonction `getUser` comme indiqué ci-dessous :

```typescript
const getUser = useCallback(async () => {
	const { data, error } = await supabase.auth.getUser();
	const { user } = data;
	if (error || !user || !apiKey) return;
	if (!tokenProvider) return;

	let streamUser;

	if (user.user_metadata?.image) {
		streamUser = {
			// 👋🏽 l'utilisateur est un instructeur
			id: user.id,
			name: user.user_metadata?.name,
			image: user.user_metadata?.image,
		};
	} else {
		// 👋🏽 l'utilisateur est un étudiant
		streamUser = {
			id: user.id,
			name: user.user_metadata?.name,
		};
	}

	//👋🏽 créer un client vidéo Stream
	const client = new StreamVideoClient({
		apiKey,
		user: streamUser,
		tokenProvider,
	});

	setVideoClient(client);
}, [supabase.auth]);
```

La fonction `getUser` récupère les données de l'utilisateur actuel à partir de Supabase Auth, configure l'utilisateur Stream et initialise un client vidéo Stream en utilisant la clé API Stream, l'objet utilisateur et le jeton.

### Création et planification des appels avec Stream

Ici, vous apprendrez à permettre aux instructeurs de planifier des appels en utilisant le Stream Video & Audio SDK.

Avant de continuer, créez un dossier `hooks` dans le dossier de l'application Next.js et ajoutez ces fichiers :

```bash
cd app && mkdir hooks
cd hooks
touch useGetCallById.ts useGetCalls.ts
```

Le fichier `useGetCallById` définit un hook React qui récupère les détails d'un appel Stream spécifique via son ID, tandis que le hook `useGetCalls` récupère tous les appels créés par un utilisateur Stream particulier.

Créons ces hooks React personnalisés.

Copiez le code suivant dans le fichier `useGetCallById.ts` :

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
				// https://getstream.io/video/docs/react/guides/querying-calls/#filters
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

Ajoutez ce qui suit au fichier `useGetCalls.ts` :

```typescript
import { useEffect, useState } from "react";
import { Call, useStreamVideoClient } from "@stream-io/video-react-sdk";
import { useParams } from "next/navigation";

export const useGetCalls = () => {
	const client = useStreamVideoClient();
	const [calls, setCalls] = useState<Call[]>();
	const [isLoading, setIsLoading] = useState(false);
	const { id } = useParams<{ id: string }>();

	useEffect(() => {
		const loadCalls = async () => {
			if (!client || !id) return;

			setIsLoading(true);

			try {
				const { calls } = await client.queryCalls({
					sort: [{ field: "starts_at", direction: 1 }],
					filter_conditions: {
						starts_at: { $exists: true },
						$or: [{ created_by_user_id: id }, { members: { $in: [id] } }],
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
	}, [client, id]);

	const now = new Date();
	//👋🏽 appels à venir
	const upcomingCalls = calls?.filter(({ state: { startsAt } }: Call) => {
		return startsAt && new Date(startsAt) > now;
	});
	//👋🏽 appels en cours
	const ongoingCalls = calls?.filter(
		({ state: { startsAt, endedAt } }: Call) => {
			return startsAt && new Date(startsAt) < now && !endedAt;
		}
	);

	return { upcomingCalls, isLoading, ongoingCalls };
};
```

Le hook **useGetCalls** récupère tous les appels où l'instructeur est soit le créateur, soit un participant, retournant à la fois les appels actuels et à venir. Il retourne également un état **isLoading** pour indiquer lorsque les données sont en cours de récupération, permettant un rendu conditionnel.

Ajoutez la fonction ci-dessous au tableau de bord de l'instructeur pour permettre aux instructeurs de créer ou de planifier des appels. Cette fonction accepte une description d'appel ainsi que la date et l'heure planifiées.

```typescript
//👋🏽 imports
import { useStreamVideoClient, Call } from "@stream-io/video-react-sdk";
const client = useStreamVideoClient();
//👋🏽 États du formulaire
const [description, setDescription] = useState<string>("");
const [dateTime, setDateTime] = useState<string>("");

const handleScheduleMeeting = async (e: React.FormEvent<HTMLFormElement>) => {
	e.preventDefault();
	if (!client || !user) return;

	try {
		const id = crypto.randomUUID();
		const call = client.call("default", id);
		if (!call) throw new Error("Failed to create meeting");
    //👋🏽 créer un appel Stream
		await call.getOrCreate({
			data: {
				starts_at: new Date(dateTime).toISOString(),
				custom: {
					description,
				},
			},
		});

		//👋🏽 Objet d'appel
		console.log({ call });
	} catch (error) {
		console.error(error);
	}
};
```

L'extrait de code ci-dessus initialise un appel vidéo Stream avec un type d'appel par défaut. Il attribue à l'appel un ID unique, définit la date et l'heure planifiées et inclut une description personnalisée.

**Note :** Assurez-vous que le composant `<StreamVideoProvider>` enveloppe le tableau de bord de l'instructeur où l'appel vidéo est créé. Vous pouvez y parvenir en ajoutant un fichier `layout.tsx` à la page du tableau de bord et en enveloppant tous les éléments enfants avec `<StreamVideoProvider>`.

![Interface du tableau de bord intitulée "LinkedUp" avec des sections pour les abonnés, les annonces et des options pour faire une annonce, planifier un appel ou accéder au canal communautaire. Le bouton de déconnexion est visible en haut à droite.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740658849436/109c53d7-c818-4d79-8bd7-19c3c0ae62a2.gif align="center")

### Rejoindre les appels vidéo Stream

La page `instructor/[id]` affiche des informations détaillées sur un instructeur spécifique de Supabase et liste ses appels actuels et à venir. Cela permet aux étudiants de voir les réunions planifiées et de les rejoindre lorsqu'elles commencent.

![Capture d'écran d'une page de profil pour Carl John, un UI Designer, sur une plateforme appelée LinkedUp. Elle inclut une photo de profil, un bouton pour rejoindre un canal communautaire, des annonces avec des options de suppression, et des réunions à venir avec des options pour rejoindre et copier le lien.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740659135003/0c53b3b6-fa91-4d28-81cf-89e8c90b7e02.gif align="center")

Pour implémenter cette fonctionnalité, nous utiliserons le composant `MeetingsBox` dans la page de profil de l'instructeur et créerons une route de page dédiée `calls/[id]` pour rejoindre les appels.

Tout d'abord, créez un dossier `(stream)` et ajoutez une route de page `calls/[id]`. Ensuite, créez un fichier `layout.tsx` dans le dossier `(stream)` et insérez le code suivant :

```typescript
import { StreamVideoProvider } from "../providers/StreamVideoProvider";
import type { Metadata } from "next";

export const metadata: Metadata = {
	title: "Calls & Chat | LinkedUp",
	description: "Generated by create next app",
};

export default function AuthLayout({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) {
	return <StreamVideoProvider>{children}</StreamVideoProvider>;
}
```

Le fichier `layout.tsx` garantit que le composant `StreamVideoProvider` enveloppe toutes les pages à l'intérieur du dossier `(stream)`, permettant l'accès aux fonctionnalités vidéo et audio de Stream sur ces pages.

Ensuite, rendez les appels dans le [composant MeetingsBox](https://github.com/dha-stix/stream-lms/blob/main/src/app/instructor/%5Bid%5D/\(components\)/MeetingsBox.tsx) et laissez les étudiants rejoindre les réunions.

```typescript
"use client";
import { formatDateTime } from "@/lib/utils";
import { Call } from "@stream-io/video-react-sdk";
import { useRouter } from "next/navigation";

export default function MeetingsBox({
	upcomingCalls,
	isLoading,
	ongoingCalls,
}: {
	upcomingCalls: Call[] | undefined;
	isLoading: boolean;
	ongoingCalls: Call[] | undefined;
}) {
	const router = useRouter();

	if (isLoading || !upcomingCalls || !ongoingCalls) {
		return <p className='text-xs opacity-60'>Fetching calls...</p>;
	}

	if (upcomingCalls.length === 0) {
		return <p className='text-xs  opacity-60'>No upcoming meetings</p>;
	}

	return {
		// --- éléments d'affichage des appels à venir et en cours ---
	};
}
```

Retournez les éléments UI suivants à partir du composant pour permettre à tous de voir les réunions actuelles et à venir de l'instructeur.

```typescript
return (
	<div className='space-y-4'>
		// --- appels en cours ---
		{ongoingCalls.map((call) => (
			<div className='bg-white p-2 rounded-md' key={call.id}>
				<h3 className='text-sm font-bold text-gray-500 mb-2'>
					{call.state.custom.description}
				</h3>
				<p className='text-xs'>
					Started: {formatDateTime(call.state?.startsAt?.toLocaleString())}
				</p>
				<div className='flex items-center space-x-4'>
					<button
						className='bg-blue-500 text-white px-4 py-2 text-xs rounded-md mt-2'
						onClick={() => handleJoinCall(call)}
					>
						Join In
					</button>

					<button
						className='bg-gray-500 text-white px-4 py-2 text-xs rounded-md mt-2'
						onClick={() => handleCopyLink(call)}
					>
						Copy Link
					</button>
				</div>
			</div>
		))}
		// --- appels à venir ---
		{upcomingCalls.map((call) => (
			<div className='bg-white p-2 rounded-md' key={call.id}>
				<h3 className='text-sm font-bold text-gray-500 mb-2'>
					{call.state.custom.description}
				</h3>

				<div className='flex items-center space-x-4'>
					<button
						className='bg-blue-500 text-white px-4 py-2 text-xs rounded-md mt-2'
						disabled={true}
					>
						{formatDateTime(call.state?.startsAt?.toLocaleString())}
					</button>

					<button
						className='bg-gray-500 text-white px-4 py-2 text-xs rounded-md mt-2'
						onClick={() => handleCopyLink(call)}
					>
						Copy Link
					</button>
				</div>
			</div>
		))}
	</div>
);
```

Le composant `MeetingsBox` rend les appels actuels et à venir de l'instructeur, permettant aux utilisateurs de copier le lien de l'appel et de rejoindre les réunions.

![Page de profil pour Carl John, un UI Designer, présentant des annonces et des réunions à venir. Les liens vers "Rejoindre mon canal communautaire" et les détails des réunions sont affichés.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740659373366/9150c744-7bb0-4e1f-99f5-b6b89d2bc488.png align="center")

Exécutez la fonction `handleJoinCall` pour rediriger l'utilisateur vers la page d'appel. Cela lui permet de confirmer l'action avant de rejoindre l'appel. La fonction `handleCopyLink` copie le lien de l'appel dans le presse-papiers.

```typescript
const handleJoinCall = (call: Call) => {
	router.push(`/call/${call.id}`);
};

const handleCopyLink = (call: Call) => {
	navigator.clipboard.writeText(
		`${process.env.NEXT_PUBLIC_PAGE_URL!}/call/${call.id}`
	);
	console.log({
		title: "Link copied to clipboard",
		description: "You can now share the link with interested participants",
	});
};
```

Maintenant, créez le composant `call/[id]/page.tsx` et copiez le code suivant dans le fichier :

```typescript
"use client";
import { useParams } from "next/navigation";
import { useEffect, useState, useCallback } from "react";
import { useRouter } from "next/navigation";
import { User } from "@supabase/supabase-js";
import { createClient } from "../../../../../utils/supabase/client";

export default function CallPage() {
	const { id } = useParams<{ id: string }>();
	const [user, setUser] = useState<User | null>(null);
	const router = useRouter();

	const authenticateUser = useCallback(async () => {
		const supabase = createClient();
		const { data } = await supabase.auth.getUser();
		const userData = data.user;
		if (!userData) {
			return router.push("/student/auth/login");
		}
		setUser(userData);
	}, [router, call, camMicEnabled]);

	useEffect(() => {
		authenticateUser();
	}, [authenticateUser]);

	return {
		// -- Rendre conditionnellement le composant Stream Call --
	};
}
```

L'extrait de code ci-dessus authentifie l'utilisateur pour s'assurer qu'il est connecté.

Ensuite, récupérez les détails de l'appel en utilisant l'ID de l'appel à partir de la route de la page via le hook `useParams`.

```typescript
"use client";
//..other imports
import { useGetCallById } from "@/app/hooks/useGetCallById";
import { StreamCall, StreamTheme } from "@stream-io/video-react-sdk";

export default function CallPage() {
	//..other states
	const { call, isCallLoading } = useGetCallById(id);
	const [confirmJoin, setConfirmJoin] = useState<boolean>(false);
	const [camMicEnabled, setCamMicEnabled] = useState<boolean>(false);

	const handleJoin = () => {
		//👋🏽 Fonction de jointure d'appel Stream
		call?.join();
		setConfirmJoin(true);
	};

	if (isCallLoading) return <p>Loading...</p>;

	if (!call) return <p>Call not found</p>;

	return (
		<main className='min-h-screen w-full items-center justify-center'>
			<StreamCall call={call}>
				<StreamTheme>
					{confirmJoin ? (
						<MeetingRoom call={call} />
					) : (
						<div className='flex flex-col items-center justify-center gap-5 h-screen w-full'>
							<h1 className='text-3xl font-bold'>Join Call</h1>
							<p className='text-lg'>
								Are you sure you want to join this call?
							</p>
							<div className='flex gap-5'>
								<button
									onClick={handleJoin}
									className='px-4 py-3 bg-blue-600 text-blue-50'
								>
									Join
								</button>
								<button
									onClick={() => router.back()}
									className='px-4 py-3 bg-red-600 text-red-50'
								>
									Cancel
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

Dans l'extrait de code ci-dessus,

* Le [composant **StreamCall**](https://getstream.io/video/docs/react/ui-components/core/stream-call/) enveloppe toute la page d'appel, permettant l'accès à diverses fonctionnalités d'appel audio et vidéo. Il accepte l'**objet call** comme prop.

* Le [composant **StreamTheme**](https://getstream.io/video/docs/react/ui-components/video-theme/) fournit un style UI pour l'appel, vous permettant d'utiliser différents thèmes.

* L'état `confirmJoin` est initialement défini sur `false`. Lorsque l'utilisateur clique sur le bouton **Join**, il déclenche la fonction `handleJoin`, qui rejoint l'appel et met à jour `confirmJoin` sur `true`.

* Lorsque `confirmJoin` est `true`, le composant rend le composant `MeetingRoom`, qui inclut tous les éléments UI préconstruits et personnalisables pour l'appel fournis par Stream.

Enfin, mettez à jour la fonction `authenticateUser` pour inviter l'utilisateur Stream à activer ou désactiver la caméra et le microphone immédiatement après avoir rejoint un appel.

```typescript
//👋🏽 état de désactivation/activation de l'appel et de la caméra
const [camMicEnabled, setCamMicEnabled] = useState<boolean>(false);

const authenticateUser = useCallback(async () => {
	const supabase = createClient();
	const { data } = await supabase.auth.getUser();
	const userData = data.user;
	if (!userData) {
		return router.push("/student/auth/login");
	}
	setUser(userData);
	//👋🏽 Activer la caméra et le microphone
	if (camMicEnabled) {
		call?.camera.enable();
		call?.microphone.enable();
	} else {
		call?.camera.disable();
		call?.microphone.disable();
	}
}, [router, call, camMicEnabled]);

useEffect(() => {
	authenticateUser();
}, [authenticateUser]);
```

### Composants UI des appels Stream

Stream facilite la configuration d'une page d'appel en utilisant des composants UI minimaux. Il fournit deux dispositions d'appel préconstruites ([PaginatedGridLayout](https://getstream.io/video/docs/react/ui-components/core/call-layout/) et [SpeakerLayout](https://getstream.io/video/docs/react/ui-components/core/call-layout/)) et un composant [CallControls](https://getstream.io/video/docs/react/ui-cookbook/replacing-call-controls/) personnalisable.

* PaginatedGridLayout et SpeakerLayout définissent comment les participants à l'appel sont affichés sur la page d'appel.

* CallControls fournit des fonctionnalités essentielles d'appel telles que l'activation/désactivation de la vidéo et de l'audio, le partage de l'écran, le fait de quitter l'appel, et plus encore.

![Interface d'appel vidéo avec une personne dans une petite fenêtre. Le microphone est désactivé, indiqué par une icône de microphone barrée. D'autres contrôles et un bouton rouge "End Call for Everyone" sont visibles en bas.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740659807590/b3e24561-60fc-4e0d-8054-a02d78a745a2.gif align="center")

Créez le composant **MeetingRoom** comme suit :

```typescript
const MeetingRoom = ({call} : {call: Call}) => {
	const [layout, setLayout] = useState<CallLayoutType>("grid");
	const router = useRouter();

//👋🏽 permet aux membres de quitter l'appel
	const handleLeave = () => {
        if (confirm("Are you sure you want to leave the call?")) {
            router.push("/");
        }
	};

//👋🏽 décrit la disposition de l'appel
	const CallLayout = () => {
		switch (layout) {
			case "grid":
				return <PaginatedGridLayout />;
			case "speaker-right":
				return <SpeakerLayout participantsBarPosition='left' />;
			default:
				return <SpeakerLayout participantsBarPosition='right' />;
		}
	};

  return (
    //  -- Composant UI de l'appel Stream --
  )
}
```

La fonction `handleLeave` permet aux participants de l'appel de quitter l'appel et le composant `CallLayout` détermine comment ils sont disposés à l'écran.

Retournez ce qui suit à partir du composant `MeetingRoom` :

```typescript
return (
	<section className='relative min-h-screen w-full overflow-hidden pt-4'>
		<div className='relative flex size-full items-center justify-center'>
			<div className='flex size-full max-w-[1000px] items-center'>
				<CallLayout />
			</div>
			<div className='fixed bottom-0 flex w-full items-center justify-center gap-5'>
				<CallControls onLeave={handleLeave} />
			</div>

			<div className='fixed bottom-0 right-0 flex items-center justify-center gap-5 p-5'>
				<EndCallButton call={call} />
			</div>
		</div>
	</section>
);
```

Les composants CallLayout et CallControls sont rendus sur la page, permettant aux utilisateurs de communiquer, de partager leur écran, d'activer ou de désactiver leur caméra et de s'engager dans des conversations à travers des réactions.

Enfin, créez le composant **EndCallButton** pour permettre à l'hôte (instructeur) de mettre fin à l'appel pour tout le monde.

```typescript
//👋🏽 hook d'appel Stream
import { useCallStateHooks } from "@stream-io/video-react-sdk";

const EndCallButton = ({ call }: { call: Call }) => {
	const { useLocalParticipant } = useCallStateHooks();
	const localParticipant = useLocalParticipant();
	const router = useRouter();

	const participantIsHost =
		localParticipant &&
		call.state.createdBy &&
		localParticipant.userId === call.state.createdBy.id;

	if (!participantIsHost) return null;

	const handleEndCall = () => {
		call.endCall();
		console.log({
			title: "Call Ended",
			description: "The call has been ended for everyone",
		});
		router.push("/");
	};

	return (
		<button
			className='bg-red-500 text-white px-4 py-2 rounded-md mt-2'
			onClick={handleEndCall}
		>
			End Call for Everyone
		</button>
	);
};
```

L'extrait de code ci-dessus garantit que seul l'hôte de l'appel peut mettre fin à l'appel pour tous les participants. Il vérifie d'abord si l'utilisateur actuel est l'hôte avant d'afficher le bouton ["End Call for Everyone"](https://getstream.io/video/docs/api/calls/#ending-calls).

![Page de profil d'un UI Designer nommé Carl John. La page inclut une section d'annonces avec des publications, une section de réunions à venir avec des options pour rejoindre et copier le lien, et un bouton de déconnexion. Un bouton pour rejoindre un canal communautaire est également présent.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740660039466/1851aba0-6961-4b54-87cf-54a3a98bb61a.gif align="center")

## Comment intégrer une fonctionnalité de chat de groupe en utilisant Stream Chat Messaging

Dans cette section, vous apprendrez à intégrer une fonctionnalité de chat communautaire dans l'application. Chaque instructeur créera un chat de groupe pour ses abonnés (étudiants). Le chat permettra aux étudiants d'interagir les uns avec les autres et de partager des documents, des liens vidéo, du texte, des images, etc., en utilisant le [Stream Chat Messaging SDK](https://getstream.io/chat/docs/sdk/react/).

### Configuration du Stream Chat SDK dans Next.js

Ajoutez le code suivant au fichier `stream.action.ts` :

```typescript
import { StreamChat } from "stream-chat";
import { getUserSession } from "./auth";

//👋🏽 crée une instance StreamChat
const serverClient = StreamChat.getInstance(STREAM_API_KEY, STREAM_API_SECRET);

//👋🏽 crée un jeton
export async function createToken(): Promise<string> {
	const { user } = await getUserSession();
	if (!user) throw new Error("User is not authenticated");
	return serverClient.createToken(user.id);
}
```

L'extrait de code ci-dessus initialise une instance Stream Chat en utilisant sa clé API et sa clé secrète. Il inclut également une fonction qui génère et retourne un jeton basé sur l'ID de l'utilisateur actuel.

Pour vous assurer que seuls les instructeurs peuvent créer un canal communautaire, suivez ces étapes :

1. Récupérez tous les canaux dont l'instructeur est membre.

2. Si aucun canal n'est trouvé (c'est-à-dire que le tableau retourné est vide), l'instructeur peut créer un nouveau canal.

3. Un message d'erreur est affiché si un canal existe déjà, informant l'instructeur qu'il ne peut avoir qu'un seul canal communautaire.

```typescript
export async function createChannel({
	userId,
	data,
}: {
	userId: string;
	data: { name: string; imageUrl: string };
}) {
	try {
		//👋🏽 récupérer la liste des canaux
		const channels = await serverClient.queryChannels(
			{
				members: { $in: [userId] },
				type: "messaging",
			},
			{ last_message_at: -1 }
		);
		//👋🏽 l'instructeur a déjà un canal
		if (channels.length > 0) {
			return {
				success: false,
				error: "You already have an existing channel",
				id: channels[0].id,
			};
		}
		//👋🏽 déclarer le type de canal
		const channel = serverClient.channel("messaging", `channel-${userId}`, {
			name: data.name,
			image: data.imageUrl,
			members: [userId],
			created_by_id: userId,
		});
		//👋🏽 créer un canal
		await channel.create();
		return { success: true, error: null, id: channel.id };
	} catch (err) {
		return { success: false, error: "Failed to create channel", id: null };
	}
}
```

L'extrait de code ci-dessus [crée un canal public](https://getstream.io/chat/docs/react/creating_channels/), ce qui signifie que n'importe qui peut rejoindre à tout moment. De plus, le nom du canal est lié à l'ID de l'instructeur, garantissant qu'il reste unique à cet instructeur.

Pour récupérer le lien du canal de l'instructeur, ajoutez une fonction dans le fichier `stream.action.ts`. Cette fonction doit retourner l'URL du canal (ID du canal), permettant aux membres d'accéder au canal chaque fois que nécessaire. Ensuite, vous pouvez afficher ce lien sur le profil de l'instructeur pour un accès facile.

```typescript
export async function getInstructorChannel(userId: string) {
	try {
		const channels = await serverClient.queryChannels(
			{
				members: { $in: [userId] },
				type: "messaging",
			},
			{ last_message_at: -1 }
		);
		return `/chat/${channels[0].id}`;
	} catch (err) {
		return null;
	}
}
```

Enfin, pour accorder aux utilisateurs l'accès à la page du canal, vérifiez si l'utilisateur est déjà membre. Si ce n'est pas le cas, ajoutez l'étudiant en tant que membre avant de rendre la page de chat. Cela garantit que seuls les utilisateurs autorisés peuvent participer à la conversation.

```typescript
export async function addUserToChannel(channelId: string, userId: string) {
	try {
		//👋🏽 vérifier si l'étudiant est déjà membre
		const channels = await serverClient.queryChannels(
			{
				members: { $in: [userId] },
				type: "messaging",
				id: channelId,
			},
			{ last_message_at: -1 }
		);
		//👋🏽 l'étudiant est déjà membre (succès - afficher la page de chat)
		if (channels.length > 0) {
			return {
				success: true,
				message: "Already a member",
				id: channels[0].id,
				error: null,
			};
		}
		//👋🏽 obtenir le canal par ID (l'étudiant n'est pas membre)
		const channel = serverClient.channel("messaging", channelId);
		//👋🏽 ajouter l'étudiant au canal en tant que membre
		await channel.addMembers([userId]);
		//👋🏽 l'étudiant est maintenant membre (succès - afficher la page de chat)
		return {
			success: true,
			error: null,
			id: channel.id,
			message: "Member just added",
		};
	} catch (error) {
		console.error("Error adding user to channel:", error);
		return {
			success: false,
			error: "Failed to add user to channel",
			id: null,
			message: null,
		};
	}
}
```

![La page de chat Stream utilisant les composants UI de l'appel Stream](https://cdn.hashnode.com/res/hashnode/image/upload/v1740660564180/474b342a-7d07-415e-b1d7-a213ed807b67.gif align="center")

### Composants UI de Stream Chat

À l'intérieur du dossier `(stream)`, créez un fichier `chat/[id]/page.tsx`. Cette page récupère l'ID du canal à partir de la route de la page et vérifie si l'utilisateur est déjà membre du canal. Si ce n'est pas le cas, l'utilisateur est automatiquement ajouté en tant que membre avant d'afficher l'interface de chat.

Copiez le code suivant dans le fichier `chat/[id]/page.tsx` :

```typescript
"use client";
import { useCallback, useEffect, useState } from "react";
import StreamChat from "./../(components)/StreamChat";
import { useParams } from "next/navigation";
import { useRouter } from "next/navigation";

export default function ChatPage() {
	const [userData, setUserData] = useState<UserData | null>(null);
	const [joinChannel, setJoinChannel] = useState<boolean>(false);
	const params = useParams<{ id: string }>();
	const router = useRouter();

	const fetchUserData = useCallback(async () => {
		// 👉🏽 obtenir l'objet utilisateur et l'ID du canal à partir de useParams
		// 👉🏽 exécuter la fonction addUserToChannel() déclarée dans la section précédente
		// 👉🏽 mettre à jour l'état React joinChannel
	}, [params.id, router]);

	useEffect(() => {
		fetchUserData();
	}, [fetchUserData]);

	if (!userData) {
		return null;
	}

	return (
		<>{joinChannel ? <StreamChat user={userData} /> : <ConfirmMember />}</>
	);
}

function ConfirmMember() {
	return (
		<div className='flex flex-col items-center justify-center h-screen'>
			<h1 className='text-2xl font-bold mb-4 text-blue-500'>
				You are not a member of this channel
			</h1>
			<p className='text-lg mb-4'>
				Please wait while we add you to the channel
			</p>

			<div className='loader'>
				<Loader2 size={48} className='animate-spin' />
			</div>
		</div>
	);
}
```

Ce code garantit qu'un utilisateur est soit déjà membre du canal, soit ajouté avant d'afficher l'interface de chat. Le composant **StreamChat** est un composant React personnalisé qui contient tous les éléments UI de Stream Chat. Le composant **ConfirmMember** affiche un message de chargement pendant que l'utilisateur est ajouté au canal.

Créez un composant StreamChat et ajoutez les imports suivants au fichier :

```typescript
"use client";
import { useCallback } from "react";
//👋🏽 -- Composants UI de Stream chat
import {
	Chat,
	Channel,
	ChannelList,
	Window,
	ChannelHeader,
	MessageList,
	MessageInput,
	useCreateChatClient,
} from "stream-chat-react";
// -- fin des composants UI de Stream chat

//👋🏽 -- permet aux membres d'envoyer des emojis dans le chat
import { EmojiPicker } from "stream-chat-react/emojis";
import { init, SearchIndex } from "emoji-mart";
import data from "@emoji-mart/data";
init({ data });
// -- fin des imports d'emojis
//👋🏽 -- créer un jeton d'action serveur
import { createToken } from "../../../../../actions/stream.action";
```

Déclarez le composant StreamChat comme suit :

```typescript
export default function StreamChat({ user }: { user: UserData }) {

	const tokenProvider = useCallback(async () => {
		return await createToken();
	}, []);

	const filters = { members: { $in: [user.id] }, type: "messaging" };
	const options = { presence: true, state: true };

	const client = useCreateChatClient({
		apiKey: process.env.NEXT_PUBLIC_STREAM_API_KEY!,
		tokenOrProvider: tokenProvider,
		userData: { id: user.id, name: user.name, image: user.image },
	});

	if (!client) return <div>Loading...</div>;

  return (
    // -- Composants UI de Stream Chat --
  )
```

Le hook **useCreateChatClient** crée un client de chat Stream en utilisant la clé API Stream, les données de l'utilisateur et le jeton créé à l'aide de la fonction `createToken()` déclarée précédemment dans cette section.

Enfin, retournez l'UI de chat à partir du composant StreamChat :

```typescript
return (
	<Chat client={client}>
		<div className='chat-container'>
			{/* -- Liste des canaux -- */}
			<div className='channel-list'>
				<ChannelList
					sort={{ last_message_at: -1 }}
					filters={filters}
					options={options}
				/>
			</div>

			{/* -- Panneau des messages -- */}
			<div className='chat-panel'>
				<Channel EmojiPicker={EmojiPicker} emojiSearchIndex={SearchIndex}>
					<Window>
						<ChannelHeader />
						<MessageList />
						<MessageInput />
					</Window>
				</Channel>
			</div>
		</div>
	</Chat>
);
```

* À partir de l'extrait de code ci-dessus :

  * Le composant [**Chat**](https://getstream.io/chat/docs/sdk/react/components/core-components/chat/) initialise le client Stream Chat et enveloppe toute la page de chat.

  * [**ChannelList**](https://getstream.io/chat/docs/sdk/react/components/core-components/channel_list/) montre les canaux de chat disponibles.

  * [**Channel**](https://getstream.io/chat/docs/sdk/react/components/core-components/channel/) configure une session de chat active.

  * **Window** contient les zones d'affichage et de saisie des messages.

  * **ChannelHeader**, [**MessageList**](https://getstream.io/chat/docs/sdk/react/components/core-components/message_list/), et **MessageInput** fournissent une interface de chat entièrement fonctionnelle.

![Une capture d'écran d'un chat de groupe nommé "UI Design Students" avec 2 membres, montrant une brève conversation avec les messages "Hello" et "Hi," horodatés à 11:33 AM.](https://cdn.hashnode.com/res/hashnode/image/upload/v1740660921805/65b237a8-584a-4d71-88ed-fe7edc68b737.png align="center")

Félicitations ! Vous avez terminé ce tutoriel. Le [code source de cet article est également disponible sur GitHub](https://github.com/dha-stix/stream-lms).

## Prochaines étapes

Jusqu'à présent, vous avez appris à construire une plateforme d'apprentissage social full-stack en utilisant Stream et Supabase. Cette plateforme permet aux utilisateurs d'interagir les uns avec les autres grâce à un chat en temps réel alimenté par Stream.

Stream vous aide à construire des applications engageantes qui évoluent jusqu'à des millions d'utilisateurs avec des API et SDK performants et flexibles pour le Chat, la Vidéo, la Voix, les Flux d'activité et la Modération, alimentés par un réseau edge mondial et une infrastructure de niveau entreprise.

Voici quelques ressources utiles pour vous aider à commencer :

* [Documentation de Stream Chat](https://getstream.io/chat/docs/)

* [Documentation de Stream Video et Audio](https://getstream.io/video/)

* [Stream Activity Feeds](https://getstream.io/activity-feeds/)

Merci d'avoir lu ! 🎉