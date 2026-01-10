---
title: Comment construire une authentification SSR sécurisée avec Supabase, Astro
  et Cloudflare Turnstile
subtitle: ''
author: Fatuma Abdullahi
co_authors: []
series: null
date: '2025-06-20T17:02:12.690Z'
originalURL: https://freecodecamp.org/news/build-secure-ssr-authentication-with-supabase-astro-and-cloudflare-turnstile
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1750438909287/d36c0c01-e779-4eea-aa41-b797fcbb05f6.png
tags:
- name: supabase ss
  slug: supabase-ss
- name: Astro
  slug: astro
- name: authentication
  slug: authentication
- name: supabase
  slug: supabase
- name: supabase auth
  slug: supabase-auth
- name: magic links
  slug: magic-links
- name: cloudflare
  slug: cloudflare
- name: Cloudflare Turnstile
  slug: cloudflare-turnstile
- name: SSR
  slug: ssr
seo_title: Comment construire une authentification SSR sécurisée avec Supabase, Astro
  et Cloudflare Turnstile
seo_desc: 'In this guide, you''ll build a full server-side rendered (SSR) authentication
  system using Astro, Supabase, and Cloudflare Turnstile to protect against bots.

  By the end, you''ll have a fully functional authentication system with Astro actions,
  magic li...'
---

Dans ce guide, vous allez construire un système d'authentification entièrement rendu côté serveur (SSR) en utilisant Astro, Supabase et Cloudflare Turnstile pour vous protéger contre les bots.

À la fin, vous aurez un système d'authentification entièrement fonctionnel avec des actions Astro, une authentification par lien magique utilisant Supabase, une protection contre les bots via Cloudflare Turnstile, des routes protégées et un middleware, ainsi qu'une gestion sécurisée des sessions.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Comprendre les technologies](#heading-comprendre-les-technologies)
    
    * [Qu'est-ce qu'Astro ?](#heading-quest-ce-quastro)
        
    * [Qu'est-ce que les actions Astro ?](#heading-quest-ce-que-les-actions-astro)
        
    * [Qu'est-ce que Supabase ?](#heading-quest-ce-que-supabase)
        
    * [Qu'est-ce que Cloudflare Turnstile ?](#heading-quest-ce-que-cloudflare-turnstile)
        
* [Comprendre l'authentification SSR](#heading-comprendre-lauthentification-ssr)
    
    * [Authentification SSR vs. SPA](#heading-authentification-ssr-vs-spa)
        
* [Pourquoi protéger les formulaires d'authentification ?](#heading-pourquoi-proteger-les-formulaires-dauthentification)
    
* [Partie 1 : Comment configurer le backend](#heading-partie-1-comment-configurer-le-backend)
    
    * [Configurer le backend Supabase](#heading-configurer-le-backend-supabase)
        
    * [Configurer Cloudflare Turnstile](#heading-configurer-cloudflare-turnstile)
        
* [Partie 2 : Comment configurer le frontend](#heading-partie-2-comment-configurer-le-frontend)
    
    * [Créer le projet Astro](#heading-creer-le-projet-astro)
        
    * [Configurer Astro pour SSR](#heading-configurer-astro-pour-ssr)
        
    * [Installer les dépendances Supabase](#heading-installer-les-dependances-supabase)
        
    * [Configurer les variables d'environnement](#heading-configurer-les-variables-environnement)
        
* [Partie 3 : Comment configurer Supabase SSR](#heading-partie-3-comment-configurer-supabase-ssr)
    
    * [Créer le client Supabase](#heading-creer-le-client-supabase)
        
    * [Créer un middleware pour la protection des routes](#heading-creer-un-middleware-pour-la-protection-des-routes)
        
* [Partie 4 : Comment construire l'interface utilisateur](#heading-partie-4-comment-construire-linterface-utilisateur)
    
    * [Mettre à jour la mise en page](#heading-mettre-a-jour-la-mise-en-page)
        
    * [Créer la page de connexion](#heading-creer-la-page-de-connexion)
        
    * [Créer la page protégée](#heading-creer-la-page-protegee)
        
* [Partie 5 : Comment configurer les actions Astro](#heading-partie-5-comment-configurer-les-actions-astro)
    
    * [Créer les actions d'authentification](#heading-creer-les-actions-dauthentification)
        
    * [Créer la route API d'échange de code](#heading-creer-la-route-api-dechange-de-code)
        
* [Partie 6 : Comment tester votre application](#heading-partie-6-comment-tester-votre-application)
    
* [Notes et ressources supplémentaires](#heading-notes-et-ressources-supplementaires)
    
    * [Documentation utile](#heading-documentation-utile)
        
    * [Dépôt de code complet](#heading-depot-de-code-complet)
        

## Prérequis

Ce tutoriel suppose que vous êtes familier avec :

* Les frameworks de développement web
    
* [Les flux d'authentification de base](https://www.freecodecamp.org/news/set-up-authentication-in-apps-with-supabase/)
    
* Les concepts de base du Backend-as-a-Service (BaaS)
    

## Comprendre les technologies

### Qu'est-ce qu'Astro ?

[Astro](https://docs.astro.build/en/getting-started/) est un framework web agnostique en termes d'UI qui rend par défaut [server-first](https://docs.astro.build/en/concepts/why-astro/#server-first). Il [peut être utilisé avec n'importe quel framework UI](https://docs.astro.build/en/guides/integrations-guide/#official-integrations), y compris [les composants clients Astro](https://docs.astro.build/en/guides/client-side-scripts/).

### Qu'est-ce que les actions Astro ?

[Les actions Astro](https://docs.astro.build/en/guides/actions/) vous permettent d'écrire des fonctions côté serveur qui peuvent être appelées sans configurer explicitement des routes API. Elles fournissent de nombreuses utilités qui simplifient le processus d'exécution de la logique serveur et peuvent être appelées à partir des environnements client et serveur.

### Qu'est-ce que Supabase ?

[Supabase](https://supabase.com/docs) est un Backend-as-a-Service open-source qui s'appuie sur [Postgres](https://www.postgresql.org/docs/). Il fournit des fonctionnalités clés telles que l'authentification, des capacités en temps réel, des fonctions edge, du stockage, et plus encore. Supabase offre à la fois une version hébergée pour un scaling facile et une version auto-hébergeable pour un contrôle total.

### Qu'est-ce que Cloudflare Turnstile ?

Turnstile est [le remplacement de Cloudflare pour les CAPTCHAs](https://www.cloudflare.com/en-gb/application-services/products/turnstile/), qui sont des puzzles visuels utilisés pour différencier les utilisateurs légitimes des bots. Contrairement aux CAPTCHAs traditionnels, qui sont visuellement encombrants, ennuyeux et [parfois difficiles à résoudre](https://blog.cloudflare.com/turnstile-ga/), Turnstile détecte l'activité malveillante sans nécessiter que les utilisateurs résolvent des puzzles, tout en offrant une meilleure expérience utilisateur.

## Comprendre l'authentification SSR

L'authentification SSR (Server-Side Rendered) fait référence à la gestion de l'authentification sur le serveur en utilisant une [méthode d'authentification basée sur les cookies](https://www.freecodecamp.org/news/set-up-authentication-in-apps-with-supabase/#how-does-authentication-work).

Le flux fonctionne comme suit :

1. Le serveur crée une session et stocke un identifiant de session dans un cookie envoyé au client
    
2. Le navigateur reçoit le cookie et l'inclut automatiquement dans les requêtes futures
    
3. Le serveur utilise le cookie pour déterminer si l'utilisateur est authentifié
    

Puisque les navigateurs ne peuvent pas modifier les cookies HTTP-only et que les serveurs ne peuvent pas accéder au stockage local, l'authentification SSR nécessite une gestion minutieuse pour prévenir les risques de sécurité tels que le détournement de session et les sessions obsolètes.

### Authentification SSR vs. SPA

Les applications monopages (SPA), comme les applications React traditionnelles, gèrent l'authentification côté client car elles n'ont pas d'accès direct à un serveur. Les SPA utilisent généralement des JWT stockés dans le stockage local, les cookies ou le stockage de session, envoyant ces jetons dans les en-têtes HTTP lors de la communication avec les serveurs.

%[https://youtu.be/HdE3dk8VkRU?si=dunB-asKXUt-OMYQ] 

## Pourquoi protéger les formulaires d'authentification ?

L'authentification protège les ressources sensibles contre les accès non autorisés, faisant des formulaires d'authentification des cibles principales pour les bots et les acteurs malveillants. Prendre des précautions supplémentaires est important pour maintenir la sécurité.

## Partie 1 : Comment configurer le backend

### Configurer le backend Supabase

Tout d'abord, vous aurez besoin [d'un compte Supabase](https://supabase.com/dashboard/). Créez un projet, puis :

1. Allez dans l'onglet Authentication dans la barre latérale
    
2. Cliquez sur l'onglet Sign In / Up sous Configuration
    
3. Activez les inscriptions des utilisateurs
    
4. Faites défiler vers le bas jusqu'à Auth Providers et activez l'email (désactivez la confirmation par email pour ce tutoriel)
    

![Interface de configuration de l'authentification Supabase montrant les options d'inscription des utilisateurs et le fournisseur d'email activé](https://cdn.hashnode.com/res/hashnode/image/upload/v1742054137964/a379192b-4eaf-491f-bcf4-a0e1e0deef94.png align="left")

### Configurer Cloudflare Turnstile

1. [Connectez-vous ou inscrivez-vous pour un compte Cloudflare](https://dash.cloudflare.com/login)
    
2. Cliquez sur l'onglet Turnstile dans la barre latérale
    
3. Cliquez sur le bouton "Add widget"
    
4. Nommez votre widget et ajoutez "localhost" comme nom d'hôte
    
5. Laissez tous les autres paramètres par défaut, et créez le widget
    

![Interface de création de widget Cloudflare Turnstile](https://cdn.hashnode.com/res/hashnode/image/upload/v1750260766060/95ec02e5-8ee7-4438-a66c-76866ec068c1.png align="left")

Après avoir créé le widget, copiez la clé secrète et ajoutez-la à votre tableau de bord Supabase :

1. Retournez aux paramètres d'authentification Supabase
    
2. Allez dans l'onglet Auth Protection sous Configuration
    
3. Activez la protection Captcha
    
4. Choisissez Cloudflare comme fournisseur
    
5. Collez votre clé secrète
    

![Paramètres de protection des attaques Supabase avec la configuration Turnstile](https://cdn.hashnode.com/res/hashnode/image/upload/v1750260776990/56ef5fc1-3321-45f0-ab9a-878679a08e88.png align="left")

## Partie 2 : Comment configurer le frontend

### Créer le projet Astro

Ensuite, vous devrez créer un projet Astro. Ouvrez le terminal intégré de votre IDE ou éditeur de texte préféré et exécutez la commande suivante pour échafauder un projet Astro dans un dossier nommé "ssr-auth". N'hésitez pas à utiliser le nom que vous souhaitez.

```bash
npm create astro@latest ssr-auth
```

Suivez les invites fournies et choisissez un modèle de base pour commencer. Une fois terminé, accédez au dossier, puis exécutez `npm install` pour installer les dépendances, suivi de `npm run dev` pour démarrer le serveur, et votre site sera disponible à l'adresse [`localhost:4321`](http://localhost:4321).

### Configurer Astro pour SSR

Configurez Astro pour qu'il s'exécute en mode SSR en ajoutant `output: "server",` à la fonction `defineConfig` trouvée dans le fichier `astro.config.mjs` à la racine du dossier.

Ensuite, [ajoutez un adaptateur](https://docs.astro.build/en/guides/integrations-guide/node/) pour créer un runtime serveur. Pour cela, utilisez l'adaptateur Node.js en exécutant cette commande dans un terminal : `npx astro add node`. Cela l'ajoutera et effectuera automatiquement toutes les modifications pertinentes.

Enfin, ajoutez Tailwind pour le style. Exécutez cette commande dans une fenêtre de terminal : `npx astro add tailwind`. Suivez les invites, et il effectuera toutes les modifications nécessaires.

À ce stade, votre fichier `astro.config.mjs` devrait ressembler à ceci :

```typescript
// @ts-check
import { defineConfig } from "astro/config";
import node from "@astrojs/node";
import tailwindcss from "@tailwindcss/vite";

// https://astro.build/config
export default defineConfig({
  output: "server",
  adapter: node({
    mode: "standalone",
  }),
  vite: {
    plugins: [tailwindcss()],
  },
});
```

### Installer les dépendances Supabase

Vous pouvez le faire en exécutant la commande suivante :

```bash
npm install @supabase/supabase-js @supabase/ssr
```

### Configurer les variables d'environnement

Créez un fichier `.env` à la racine du projet et ajoutez ce qui suit. N'oubliez pas de remplacer par vos identifiants réels :

```bash
SUPABASE_URL=<YOUR_URL>
SUPABASE_ANON_KEY=<YOUR_ANON_KEY>
TURNSTILE_SITE_KEY=<YOUR_TURNSTILE_SITE_KEY>
```

Vous pouvez obtenir les valeurs Supabase à partir du tableau de bord :

![Interface de connexion du projet Supabase montrant les variables d'environnement](https://cdn.hashnode.com/res/hashnode/image/upload/v1742054292788/8aeec326-259c-49bd-a6f8-b885e9a9e6ea.png align="left")

**💡Note :** Dans Astro, les variables d'environnement accessibles côté client doivent être préfixées par 'PUBLIC'. Mais comme nous utilisons des actions Astro qui s'exécutent sur le serveur, le préfixe n'est pas requis.

## Partie 3 : Comment configurer Supabase SSR

### Créer le client Supabase

Créez `src/lib/supabase.ts` :

```typescript

import { createServerClient, parseCookieHeader } from "@supabase/ssr";
import type { AstroCookies } from "astro";

export function createClient({
	request,
	cookies,
}: {
	request: Request;
	cookies: AstroCookies;
}) {
	const cookieHeader = request.headers.get("Cookie") || "";

	return createServerClient(
		import.meta.env.SUPABASE_URL,
		import.meta.env.SUPABASE_ANON_KEY,
		{
			cookies: {
				getAll() {
					const cookies = parseCookieHeader(cookieHeader);
					return cookies.map(({ name, value }) => ({
						name,
						value: value ?? "",
					}));
				},
				setAll(cookiesToSet) {
					cookiesToSet.forEach(({ name, value, options }) =>
						cookies.set(name, value, options)
					);
				},
			},
		}
	);
}
```

Cela configure Supabase pour gérer [les cookies dans une application rendue côté serveur](https://supabase.com/docs/guides/auth/server-side/creating-a-client?queryGroups=framework&framework=astro&queryGroups=environment&environment=astro-browser) et exporte une fonction qui prend l'objet request et cookies en entrée. La fonction est configurée de cette manière car Astro a trois façons d'accéder aux informations de requête et de cookie :

* Via l'objet global d'Astro, qui n'est disponible que sur les pages Astro.
    
* Via l'objet `AstroAPIContext`, qui n'est disponible que dans les actions Astro.
    
* Via `APIContext` qui est un sous-ensemble de l'objet global et est disponible via les routes API et le middleware.
    

Ainsi, la fonction `createClient` accepte les objets `request` et `cookies` séparément pour la rendre flexible et applicable dans les divers contextes dans lesquels elle peut être utilisée.

### Créer un middleware pour la protection des routes

Ensuite, créez un fichier `middleware.ts` dans le dossier `src` et collez ceci dedans :

```typescript
import { defineMiddleware } from "astro:middleware";
import { createClient } from "./lib/supabase";

export const onRequest = defineMiddleware(async (context, next) => {
	const { pathname } = context.url;

	console.log("Middleware executing for path:", pathname);

	const supabase = createClient({
		request: context.request,
		cookies: context.cookies,
	});

	if (pathname === "/protected") {
		console.log("Checking auth for protected route");

		const { data } = await supabase.auth.getUser();

		// If no user, redirect to index
		if (!data.user) {
			return context.redirect("/");
		}
	}

	return next();
});
```

Ce middleware vérifie la présence d'un utilisateur actif lors de l'accès à la route protégée et redirige les utilisateurs non authentifiés vers la page d'accueil.

## Partie 4 : Comment construire l'interface utilisateur

### Mettre à jour la mise en page

Tout d'abord, mettez à jour `src/layouts/Layout.astro` pour inclure le script Turnstile. Ajoutez ceci juste au-dessus de la balise de fermeture `</head>` :

```typescript
<script
	src="https://challenges.cloudflare.com/turnstile/v0/api.js"
	async
	defer>
</script>
```

### Créer la page de connexion

Remplacez le contenu de `src/pages/index.astro` :

```typescript
---
import Layout from "../layouts/Layout.astro";
import { createClient } from "../lib/supabase";
import "../styles/global.css";

const supabase = createClient({
	request: Astro.request,
	cookies: Astro.cookies,
});

const { data } = await supabase.auth.getUser();

if (data.user) {
	return Astro.redirect("/protected");
}

const apiKey = import.meta.env.TURNSTILE_SITE_KEY;
---

<Layout>
	<section class="flex flex-col items-center justify-center m-30">
		<h1 class="text-4xl text-left font-bold mb-12">Connectez-vous à votre compte</h1>
		<form id="signin-form" class="flex flex-col gap-2 w-1/2">
			<label for="email" class="">Entrez votre email</label>
			<input
				type="email"
				name="email"
				id="email"
				placeholder="votreemail@example.com"
				class="border border-gray-500 rounded-md p-2"
				required
			/>
			<div class="cf-turnstile" data-sitekey={apiKey}></div>
			<button
				type="submit"
				id="sign-in"
				class="bg-gray-600 hover:bg-gray-700 p-2 rounded-md text-white font-bold w-full cursor-pointer disabled:bg-gray-500 disabled:hover:bg-gray-500 disabled:cursor-not-allowed"
				>Se connecter</button
			>
		</form>
	</section>
</Layout>
```

Ici, le frontmatter crée un client serveur Supabase puis l'utilise pour vérifier si nous avons un utilisateur actif. Il redirige en fonction de ces informations. Cela fonctionne car le frontmatter s'exécute côté serveur, et le projet est configuré pour une sortie serveur.

Le modèle affiche un formulaire simple avec une entrée d'email. Pour le compléter, ajoutez ceci sous la balise de fermeture `</Layout>` :

```typescript

<script>
	import { actions } from "astro:actions";

	declare global {
		interface Window {
			turnstile?: {
				reset: () => void;
			};
		}
	}

	const signInForm = document.querySelector("#signin-form") as HTMLFormElement;
	const formSubmitBtn = document.getElementById("sign-in") as HTMLButtonElement;

	signInForm?.addEventListener("submit", async (e) => {
		e.preventDefault();
		formSubmitBtn.disabled = true;
		formSubmitBtn.textContent = "Connexion en cours...";

		try {
			const turnstileToken = (
				document.querySelector(
					"[name='cf-turnstile-response']"
				) as HTMLInputElement
			)?.value;

			if (!turnstileToken) {
				throw new Error("verification_missing");
			}

			const formData = new FormData(signInForm);
			formData.append("captchaToken", turnstileToken);

			const results = await actions.signIn(formData);

			if (!results.data?.success) {
				if (results.data?.message?.includes("captcha protection")) {
					alert("La vérification a échoué. Veuillez réessayer.");
					if (window.turnstile) {
						window.turnstile.reset();
					}
					formSubmitBtn.disabled = false;
					formSubmitBtn.textContent = "Se connecter";
					return;
				} else {
					alert("Oups ! Impossible de se connecter. Veuillez réessayer");
					formSubmitBtn.disabled = false;
					formSubmitBtn.textContent = "Se connecter";
					return;
				}
			}

			formSubmitBtn.textContent = "Se connecter";
			alert("Veuillez vérifier votre email pour vous connecter");
		} catch (error) {
			if (window.turnstile) {
				window.turnstile.reset();
			}
			formSubmitBtn.disabled = false;
			formSubmitBtn.textContent = "Se connecter";
			console.log(error);
			alert("Quelque chose s'est mal passé. Veuillez réessayer");
		}
	});
</script>
```

Cela ajoute un peu de JavaScript vanilla qui appelle l'action `SignIn` lors de la soumission du formulaire. Cette action fournit un retour utilisateur via des alertes et gère le texte et l'état désactivé du bouton. Cela ajoute effectivement une interactivité côté client à la page.

### Créer la page protégée

Créez `src/pages/protected.astro` :

```typescript
---
import Layout from "../layouts/Layout.astro";
import { createClient } from "../lib/supabase";
import "../styles/global.css";

const supabase = createClient({
	request: Astro.request,
	cookies: Astro.cookies,
});

const { data } = await supabase.auth.getUser();
---

<Layout>
	<section class="flex flex-col items-center justify-center m-30">
		<h1 class="text-4xl text-left font-bold mb-12">Vous êtes connecté !</h1>
		<p class="mb-6">Votre identifiant utilisateur : {data.user?.id}</p>
		<button
			id="sign-out"
			class="bg-gray-600 hover:bg-gray-700 px-4 py-2 rounded-md text-white font-bold cursor-pointer disabled:bg-gray-500 disabled:hover:bg-gray-500 disabled:cursor-not-allowed"
			>Se déconnecter</button
		>
	</section>
</Layout>

<script>
	import { actions } from "astro:actions";
	const signOutBtn = document.getElementById("sign-out") as HTMLButtonElement;

	signOutBtn?.addEventListener("click", async (e) => {
		e.preventDefault();
		signOutBtn!.disabled = true;
		signOutBtn!.textContent = "Déconnexion en cours...";

		try {
			const results = await actions.signOut();

			if (!results.data?.success) {
				signOutBtn!.disabled = false;
				signOutBtn!.textContent = "Se déconnecter";
				return alert("Oups ! Impossible de se déconnecter. Veuillez réessayer");
			}
			return window.location.reload();
		} catch (error) {
			signOutBtn.disabled = false;
			signOutBtn.textContent = "Se déconnecter";
			console.log(error);
			return alert("Quelque chose s'est mal passé. Veuillez réessayer");
		}
	});
</script>
```

Cette page récupère les données utilisateur côté serveur dans le frontmatter et les affiche dans le modèle, ainsi qu'un bouton de déconnexion.

Le JavaScript dans les balises `script` gère l'appel à l'action de déconnexion, le retour utilisateur et l'état du bouton, comme dans la page `index.astro`.

## Partie 5 : Comment configurer les actions Astro

### Créer les actions d'authentification

Enfin, ajoutez un dossier `actions` dans le dossier `src` et créez un fichier `index.ts` pour contenir notre logique. Collez ce qui suit dedans :

```typescript
import { defineAction, type ActionAPIContext } from "astro:actions";
import { z } from "astro:schema";
import { createClient } from "../lib/supabase";

const emailSignUp = async (
	{
		email,
		captchaToken,
	}: {
		email: string;
		captchaToken: string;
	},
	context: ActionAPIContext
) => {
	console.log("Sign up action");
	try {
		const supabase = createClient({
			request: context.request,
			cookies: context.cookies,
		});

		const { data, error } = await supabase.auth.signInWithOtp({
			email,
			options: {
				captchaToken,
				emailRedirectTo: "http://localhost:4321/api/exchange",
			},
		});

		if (error) {
			console.error("Sign up error", error);
			return {
				success: false,
				message: error.message,
			};
		} else {
			console.log("Sign up success", data);
			return {
				success: true,
				message: "Successfully logged in",
			};
		}
	} catch (err) {
		console.error("SignUp action other error", err);
		return {
			success: false,
			message: "Unexpected error",
		};
	}
};

export const server = {
	signIn: defineAction({
		accept: "form",
		input: z.object({
			email: z.string().email(),
			captchaToken: z.string(),
		}),
		handler: async (input, context) => {
			return emailSignUp(input, context);
		},
	}),
	signOut: defineAction({
		handler: async (_, context) => {
			const supabase = createClient({
				request: context.request,
				cookies: context.cookies,
			});
			const { error } = await supabase.auth.signOut();
			if (error) {
				console.error("Sign out error", error);
				return {
					success: false,
					message: error.message,
				};
			}
			return {
				success: true,
				message: "Successfully signed out",
			};
		},
	}),
};
```

Cette action gère à la fois les méthodes de connexion et de déconnexion. Une instance serveur Supabase est créée pendant la méthode de connexion, et la méthode de lien magique est utilisée pour la connexion. Elle passe une URL de redirection, que nous n'avons pas encore créée, et gère les erreurs qui peuvent survenir.

Elle passe également la vérification du jeton, permettant à Supabase d'effectuer la vérification en notre nom, éliminant ainsi le besoin d'appeler directement [les API de vérification de Cloudflare](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/).

La méthode de déconnexion appelle la méthode de déconnexion de Supabase et gère les erreurs potentielles.

L'URL de redirection fait référence à une route API qui échange le code de l'email envoyé par Supabase contre une session que Supabase gère.

### Créer la route API d'échange de code

Créez `src/pages/api/exchange.ts` :

```typescript
import type { APIRoute } from "astro";
import { createClient } from "../../lib/supabase";

export const GET: APIRoute = async ({ request, cookies, redirect }) => {
	const url = new URL(request.url);
	const code = url.searchParams.get("code");

	if (!code) {
		return redirect("/");
	}

	const supabase = createClient({ request, cookies });
	const { error } = await supabase.auth.exchangeCodeForSession(code);

	if (error) {
		console.error("Error exchanging code for session:", error);
		return redirect("/404");
	}

	return redirect("/protected");
};
```

Cela récupère le code de l'URL dans le lien magique envoyé, crée un client serveur, et appelle la méthode `exchangeCodeForSession` avec le code. Il gère toute erreur en redirigeant vers la page non trouvée intégrée d'Astro.

Sinon, il redirigera vers la page protégée car Supabase gère les détails de mise en œuvre de la session.

## Partie 6 : Comment tester votre application

Démarrez votre serveur de développement : `npm run dev`

Visitez l'URL localhost fournie. Vous devriez voir la page de connexion avec le widget Turnstile :

![Page de connexion avec vérification Turnstile et champ de saisie d'email](https://cdn.hashnode.com/res/hashnode/image/upload/v1750267075336/66ad5f39-67c6-458a-96ea-4dfe1123b015.png align="left")

Si vous essayez d'accéder à la page `/protected`, elle vous redirigera vers cette vue jusqu'à ce que vous vous connectiez. Maintenant, connectez-vous, et vous devriez recevoir un email avec un lien qui vous redirigera vers la page `/protected`. Voici ce que vous devriez voir :

![Texte indiquant : "Vous êtes connecté !" avec un champ intitulé "Votre identifiant utilisateur" et un bouton "Se déconnecter" en dessous.](https://cdn.hashnode.com/res/hashnode/image/upload/v1750335131827/f85cde2f-f9bb-46b0-a09e-6ae6456cd49f.png align="left")

Et avec cela, vous avez réussi à construire un système d'authentification complet qui utilise les actions Astro, l'authentification Supabase et la protection contre les bots de Cloudflare Turnstile. Cette configuration offre une expérience d'authentification sécurisée et conviviale tout en protégeant votre application contre les acteurs malveillants.

## Notes et ressources supplémentaires

### Documentation utile

* [Guide avancé de Supabase pour SSR](https://supabase.com/docs/guides/auth/server-side/advanced-guide)
    
* [Package SSR de Supabase](https://github.com/supabase/ssr)
    
* [Documentation sur les cookies Astro](https://docs.astro.build/en/reference/api-reference/#cookies)
    
* [Documentation sur le flux PKCE de Supabase](https://supabase.com/docs/guides/auth/sessions/pkce-flow)
    
* [Documentation sur les actions Astro](https://docs.astro.build/en/guides/actions/)
    
* [Commencer avec Turnstile](https://developers.cloudflare.com/turnstile/get-started/)
    

### Dépôt de code complet

Le code complet de ce projet est disponible sur GitHub :

* [Configuration d'authentification de base](https://github.com/FatumaA/supa-ssr)
    
* [Avec Cloudflare Turnstile](https://github.com/FatumaA/supa-ssr/tree/add-cloudflare)