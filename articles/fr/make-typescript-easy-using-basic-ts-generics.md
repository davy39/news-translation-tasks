---
title: Comment les génériques TypeScript vous aident à écrire moins de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-03T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/make-typescript-easy-using-basic-ts-generics
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9971740569d1a4ca1fbf.jpg
tags:
- name: Productivity
  slug: productivity
- name: TypeScript
  slug: typescript
seo_title: Comment les génériques TypeScript vous aident à écrire moins de code
seo_desc: 'By Utkarsh Bhimte

  When developers discuss Typescript, one of their main complaints is that you have
  to write more code to achieve the same result. While I agree with that, I think
  Typescript Generics can reduce the code you need to write to a great e...'
---

Par Utkarsh Bhimte

Lorsque les développeurs discutent de Typescript, l'une de leurs principales plaintes est qu'il faut écrire plus de code pour obtenir le même résultat. Bien que je sois d'accord avec cela, je pense que les génériques Typescript peuvent réduire considérablement la quantité de code que vous devez écrire.

## Qu'est-ce que les génériques TypeScript ?

Les **génériques TS** peuvent être utilisés pour apporter de l'abstraction dans vos interfaces TS. En utilisant les génériques, vous pouvez passer une interface en tant que paramètre à une autre interface.

Voici un exemple de réponse d'API standard pour un cas de succès et un cas d'erreur.

```js
// réponse réussie ✅
{
	status: 'ok',
	responseCode: 200,
	data: {...}
}

// réponse d'erreur ❌
{
	responseCode: 500,
	errorMessage: "Something went wrong ?";
}

```

Au lieu d'écrire une interface pour chaque réponse et d'ajouter ces clés, vous pouvez simplement utiliser les génériques pour créer quelque chose comme ceci :

```ts
interface ApiResponse<T>{
	errorMessage?: string;
	responseCode?: string;
	data?: T;
}

```

```ts
interface UserData {
	name: string;
	email: string;
}
const response: ApiResponse<UserData> = {}

```

## Lier les génériques avec les fonctions

Supposons que nous avons une fonction que nous utilisons pour faire une requête API à notre backend.

```ts
const getRequestTo = (endpoint: string) => {
	return fetch(process.env.BE_HOST + endpoint).then(res => res.json())
}

const userResponse = getRequestTo('/user-data')

```

Le type de `userResponse` serait `any`. Nous pouvons avoir une meilleure implémentation TypeScript ici.

```ts
const getRequestTo = async <R>(endpoint: string): Promise<ApiResponse<R>> => {
	const request = await fetch(process.env.BE_HOST + endpoint);
	const response = await request.json();
	return response;
};

```

Nous pouvons créer une fonction similaire pour les requêtes POST qui prend également du JSON en tant que paramètres de type `B` et le serveur renverra une réponse JSON de type `R` :

```ts
const postRequestTo = async <B, R>(
	endpoint: string,
	body: B
): Promise<ApiResponse<R>> => {
	const request = await fetch(process.env.BE_HOST + endpoint, {
		method: "POST",
		body: JSON.stringify(body),
	});

	const response = await request.json();

	return response;
};

```

De même, il peut y avoir une fonction de requête PATCH qui gère les mises à jour partielles de n'importe quelle entité.

```ts
const patchRequestTo = async <B, R>(endpoint: string,body: Partial<B>): Promise<ApiResponse> => {
	const request = await fetch(process.env.BE_HOST + endpoint, {
    	method: "PATCH",
	    body: JSON.stringify(body)
    });
	const response = await request.json();
	return response;
};

```

Voici comment implémenter quelque chose comme cela :

```ts
interface RequestBody {}
interface Response {}

const createPost = await postRequestTo<RequestBody, Response>('/post', postData);

const updatePost = await patchRequestTo<RequestBody, Response>('/post', {
	title: "new name"
});

```

Regroupons le tout avec une simple classe JavaScript :

```ts
class ApiService<T> {
	constructor(entitySlug: string) {
		this.entitySlug = entitySlug;
	}

	private entitySlug: string;

	getOne = async (id: string): Promise<APIResponse<T>> => {
		const request = await fetch(process.env.BE_HOST + this.entitySlug + '/' + id);
		const response = await request.json();
		return response;
	};
    
	getList = async (): Promise<APIResponse<T[]>> => {
		const request = await fetch(process.env.BE_HOST + this.entitySlug);
		const response = await request.json();
		return response;
	};

	create = async (body: Omit<T, 'id' | 'created' | 'updated'>): Promise<APIResponse<T>> => {
		const request = await fetch(process.env.BE_HOST + this.entitySlug, {
			method: 'POST',
			body: JSON.stringify(body)
		});

		const response = await request.json();
		return response;
	};
    
	update = async (
		body: Omit<Partial<T>, 'id' | 'created' | 'updated'>
	): Promise<APIResponse<T>> => {
		const request = await fetch(process.env.BE_HOST + this.entitySlug + '/' + body.id, {
			method: 'PATCH',
			body: JSON.stringify(body)
		});
		const response = await request.json();
		return response;
	};
    
	delete = async (id: string): Promise<void> => {
		const request = await fetch(process.env.BE_HOST + this.entitySlug + '/' + id, {
			method: 'DELETE'
		});
		const response = await request.json();
		return response;
	};
};


```

et vous pouvez ensuite créer un service d'entité comme ceci :

```ts
export const postService = new ApiService<Post>('/post');
```

et tout est lié et prêt pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-70.png)
_VS Code suggérant automatiquement selon la configuration typescript que nous avons implémentée_

Typescript a le potentiel d'améliorer l'expérience des développeurs de manière exponentielle s'il est correctement configuré. Ce sont quelques stratégies pour rendre ce processus de configuration plus confortable. J'espère que cela vous aidera à utiliser Typescript de manière plus efficace dans votre base de code actuelle.