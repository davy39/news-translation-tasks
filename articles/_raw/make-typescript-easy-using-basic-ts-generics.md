---
title: How TypeScript Generics Help You Write Less Code
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
seo_title: null
seo_desc: 'By Utkarsh Bhimte

  When developers discuss Typescript, one of their main complaints is that you have
  to write more code to achieve the same result. While I agree with that, I think
  Typescript Generics can reduce the code you need to write to a great e...'
---

By Utkarsh Bhimte

When developers discuss Typescript, one of their main complaints is that you have to write more code to achieve the same result. While I agree with that, I think Typescript Generics can reduce the code you need to write to a great extent.

## What are TypeScript Generics?

**TS Generics** can be used to bring abstraction into your TS interfaces. Using generics, you can pass an interface as a param to another interface.

Here is an example of a standard API response for both a happy path and an error case.

```js
// successful response ✅
{
	status: 'ok',
	responseCode: 200,
	data: {...}
}

// error response ❌
{
	responseCode: 500,
	errorMessage: "Something went wrong ?";
}

```

Instead of writing an interface for every response and adding these keys, you can simply use Generics to create something like this:

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

## Linking Generics with functions

Let's assume we have a function that we use to make an API request to our backend.

```ts
const getRequestTo = (endpoint: string) => {
	return fetch(process.env.BE_HOST + endpoint).then(res => res.json())
}

const userResponse = getRequestTo('/user-data')

```

The type of `userResponse` would be `any`. We can have a better TypeScript implementation here.

```ts
const getRequestTo = async <R>(endpoint: string): Promise<ApiResponse<R>> => {
	const request = await fetch(process.env.BE_HOST + endpoint);
	const response = await request.json();
	return response;
};

```

We can create a similar function for POST requests which also takes JSON as params of type `B` and the server will send back a JSON response of type `R`:

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

Similarly, there can be a PATCH request function as well, which handle‌s partial updates of any entity.

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

Here is how to implement something like that:

```ts
interface RequestBody {}
interface Response {}

const createPost = await postRequestTo<RequestBody, Response>('/post', postData);

const updatePost = await patchRequestTo<RequestBody, Response>('/post', {
	title: "new name"
});

```

Let's pull it all together with a simple JavaScript class:

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

and you can then create an entity service like this:

```ts
export const postService = new ApiService<Post>('/post');
```

and it's all linked and ready for you. 

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-70.png)
_VS Code auto-suggesting according to the typescript configuration that we have implemented_

Typescript has the potential to increase the developer experience tenfold if appropriately configured. These are some strategies to make that configuration process more comfortable. I hope this will help you use Typescript better in your current codebase. 

