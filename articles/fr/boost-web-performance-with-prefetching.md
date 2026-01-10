---
title: Comment booster les performances web avec le prefetching – Améliorer l'expérience
  utilisateur en réduisant le temps de chargement
subtitle: ''
author: Keyur Paralkar
co_authors: []
series: null
date: '2024-09-23T15:48:11.596Z'
originalURL: https://freecodecamp.org/news/boost-web-performance-with-prefetching
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/-Vqn2WrfxTQ/upload/0657c02758973f4ea5701f2bd98469a7.jpeg
tags:
- name: web performance
  slug: web-performance
- name: React
  slug: reactjs
seo_title: Comment booster les performances web avec le prefetching – Améliorer l'expérience
  utilisateur en réduisant le temps de chargement
seo_desc: 'We''ve all encountered the frustration of waiting through long loading
  screens, only to find ourselves stuck with unresponsive pages. You see loading spinners
  everywhere, but nothing seems to move forward. Let me paint a clearer picture for
  you:


  This...'
---

Nous avons tous déjà connu la frustration d'attendre devant de longs écrans de chargement, pour finalement nous retrouver face à des pages qui ne répondent pas. Vous voyez des indicateurs de chargement partout, mais rien ne semble avancer. Laissez-moi vous brosser un tableau plus précis :

[![Plusieurs loaders squelettes sur une page de tableau de bord](https://cdn.hashnode.com/res/hashnode/image/upload/v1726397417280/bc56c517-c63f-433e-93c6-939c3b82c556.gif align="center")](https://dribbble.com/shots/3358709-Skeleton-Loader#)

Cela se produit généralement parce que le site web essaie de récupérer toutes les données nécessaires dès que vous arrivez sur la page. Il se peut qu'une requête API soit en cours de traitement, ou que plusieurs API récupèrent des données de manière séquentielle, ce qui retarde le chargement de la page.

Le résultat ? Une mauvaise expérience utilisateur. Vous pourriez vous dire : « Comment une si grande entreprise peut-elle ne pas prioriser l'expérience utilisateur ? C'est décevant. » En conséquence, les utilisateurs quittent souvent le site, ce qui affecte les indicateurs clés et potentiellement les revenus.

Mais que se passerait-il si vous pouviez récupérer les données de ces pages lourdes à l'avance, de sorte qu'au moment où l'utilisateur arrive sur la page, il puisse interagir avec elle instantanément ?

C'est ici qu'intervient le concept de prefetching, et c'est exactement ce que nous allons explorer dans cet article de blog. Alors, sans plus attendre, commençons !

## Table des matières

* [Le prefetching comme solution](#heading-le-prefetching-comme-solution)
    
* [Comment le prefetching améliore l'expérience utilisateur](#heading-comment-le-prefetching-ameliore-lexperience-utilisateur)
    
* [Comprendre le problème](#heading-comprendre-le-probleme)
    
* [Solution n°1 : Prefetching des données dans le composant parent](#heading-solution-n1-prefetching-des-donnees-dans-le-composant-parent)
    
* [Solution n°2 : Prefetching des données au chargement de la page](#heading-solution-n2-prefetching-des-donnees-au-chargement-de-la-page)
    
* [Comment implémenter le prefetching avec React](#heading-comment-implementer-le-prefetching-avec-react)
    
* [Trop de prefetching peut également causer des](#heading-comment-implementer-le-prefetching-avec-react) [l](#heading-trop-de-prefetching-peut-egalement-causer-des-lenteurs)[enteurs](#heading-comment-implementer-le-prefetching-avec-react)
    
* [Résumé](#heading-resume)
    

## Le prefetching comme solution

Voici la version révisée avec la grammaire et l'orthographe corrigées :

Pour le problème mentionné ci-dessus, ce que nous voulons, c'est récupérer les données d'une page donnée avant qu'elle ne soit chargée sur le site web, afin que l'utilisateur n'ait pas besoin de récupérer les données au moment du chargement de la page. C'est ce qu'on appelle le prefetching. D'un point de vue technique, sa définition est la suivante :

> *C'est un moyen de récupérer les données requises à l'avance afin que le composant principal n'ait pas à attendre les données, améliorant ainsi l'expérience.*

Cela peut améliorer l'expérience utilisateur, renforçant ainsi la confiance du client dans votre site web.

Le prefetching est une solution simple mais élégante, plus centrée sur l'utilisateur qu'un processus standard. Pour implémenter le prefetching, nous devons comprendre le comportement de l'utilisateur sur le site web. C'est-à-dire les pages les plus visitées, ou les composants qui récupèrent des données lors de petites interactions (comme le survol).

Après avoir analysé de tels scénarios, il est logique de leur appliquer le prefetching. Cependant, en tant que développeurs, nous devons être prudents avec ce concept. Trop de prefetching peut également ralentir votre site web puisque vous essayez de récupérer beaucoup de données pour des scénarios futurs, ce qui pourrait bloquer la récupération des données pour la page principale.

## Comment le prefetching améliore l'expérience utilisateur

Examinons quelques scénarios où le prefetching est bénéfique :

1. Charger les données/la page plus tôt pour le lien le plus visité de votre page d'accueil. Par exemple, imaginez que vous ayez un lien « contactez-nous ». Supposons que ce soit le lien que les utilisateurs consultent le plus et qu'il contienne beaucoup de données lors de son chargement. Plutôt que de charger les données au moment du chargement de la page de contact, vous pouvez simplement récupérer les données sur la page d'accueil afin de ne pas avoir à attendre sur la page de contact. Vous pouvez en savoir plus sur le prefetching de pages [ici](https://web.dev/articles/link-prefetch).
    
2. Prefetching des données de tableau pour les pages suivantes.
    
3. Récupération des données depuis un composant parent et chargement dans le composant enfant.
    
4. Prefetching des données qui doivent être affichées dans un popover.
    

Ce sont quelques-unes des façons de réaliser le prefetching dans votre application et comment cela aide à améliorer l'expérience utilisateur.

Dans cet article de blog, nous allons discuter du dernier scénario : « prefetching des données qui doivent être affichées dans le popover ». C'est un exemple classique où le prefetching peut être bénéfique et offre une expérience plus fluide à l'utilisateur.

## Comprendre le problème

Laissez-moi définir le problème ici. Imaginez le scénario suivant :

1. Vous avez un composant qui affiche des informations spécifiques.
    
2. Il y a un élément à l'intérieur de ce composant qui affiche un autre popover/tooltip lorsque vous le survolez.
    
3. Le popover récupère des données lors de son chargement.
    

Imaginez maintenant que l'utilisateur survole l'élément et doive attendre que les données soient récupérées et affichées dans le popover. Pendant cette attente, il voit le loader squelette.

Le scénario ressemblera à ceci :

![Exemple de récupération de données lors du montage du composant popover](https://cdn.hashnode.com/res/hashnode/image/upload/v1726395720567/6ec88fab-ffe2-4f20-b934-94342f9cf3c0.gif align="center")

C'est tout simplement frustrant de voir combien de temps l'utilisateur doit attendre chaque fois qu'il survole l'image :

![Utilisateur survolant les images pour charger le composant popover qui récupère les données](https://cdn.hashnode.com/res/hashnode/image/upload/v1726395733461/3598da70-e8af-4a1a-b3cf-5c3ed62fe9cc.gif align="center")

Pour résoudre ce problème, il existe deux solutions qui peuvent vous aider à démarrer et à optimiser la solution selon vos besoins.

## Solution n°1 : Prefetching des données dans le composant parent

Cette solution est inspirée de [l'article de blog de Martin Fowler](https://martinfowler.com/articles/data-fetch-spa.html?utm_source=cassidoo&utm_medium=email&utm_campaign=until-youre-ready-to-look-foolish-youll-never#prefetching). Elle permet de récupérer les données avant que la popup n'apparaisse, au lieu de les récupérer lors du chargement du composant.

La popup apparaît lorsque vous la survolez. Nous pouvons récupérer les données lorsque la souris entre dans le composant parent. Avant même que le composant réel — l'image — ne soit survolé, nous aurons les données pour le popover et nous les transmettrons au composant popover.

Cette solution ne supprime pas totalement l'état de chargement, mais elle aide à réduire considérablement les chances de voir cet état de chargement.

![Amélioration de l'UX en récupérant les données depuis le composant parent](https://cdn.hashnode.com/res/hashnode/image/upload/v1726395771616/69b6c536-8b62-4124-837a-f26746f6f305.gif align="center")

## Solution n°2 : Prefetching des données au chargement de la page

Cette solution est inspirée de [x.com](http://x.com) où, pour le composant popover, ils récupèrent les données partiellement lors du chargement de la page principale et récupèrent le reste des données lors du montage du composant.

![Publicité Twitter par XDevelopers. Le texte indique : "Appel à tous les #développeurs ! Innovez avec nos données en temps réel et historiques sur l'API X. Commencez avec Pro👇". L'image montre une personne en chemise blanche avec le texte "Construisez la suite avec notre API @XDevelopers" et "Abonnez-vous maintenant !" Utilisé avec permission. De twitter.com.](https://cdn.hashnode.com/res/hashnode/image/upload/v1726395833198/c7f1fa64-986d-4bfc-83cb-f052cd560f3a.gif align="center")

Comme vous pouvez le voir dans la vidéo ci-dessus, les détails du profil de l'utilisateur sont affichés dans le popover. Si vous regardez de plus près, les détails relatifs aux followers sont récupérés plus tard.

Cette technique est très efficace lorsque vous avez beaucoup de données à afficher dans le popover, mais que leur récupération peut être coûteuse au moment du montage du popover ou lors du chargement de la page principale.

Une meilleure solution serait de charger partiellement les données requises sur la page principale et de charger le reste des données lorsque le composant est monté.

Dans notre exemple, nous avons récupéré les données pour le popover lorsque le curseur est entré dans l'élément parent de l'image. Imaginez maintenant que vous deviez récupérer des détails supplémentaires une fois que les données du popover sont chargées. Ainsi, en nous basant sur la méthode de x.com ci-dessus, nous pouvons récupérer des données supplémentaires au chargement du popover. Voici le résultat :

![GIF expliquant comment nous effectuons le prefetch des données depuis le parent et chargeons des données supplémentaires au montage du composant pour le popover](https://cdn.hashnode.com/res/hashnode/image/upload/v1726395913909/b5f6f231-5a1e-4c44-a4eb-bd5ed863ce3b.gif align="center")

Ici, nous faisons les choses suivantes :

* Nous récupérons les données principales qui sont juste nécessaires pour afficher le popover lorsque la souris entre dans le composant parent de l'image.
    
* Cela nous donne assez de temps pour récupérer les données principales.
    
* Lors du chargement du popover, nous récupérons d'autres données, comme le nombre d'albums. Pendant que l'utilisateur lit des données comme le nom et l'e-mail, nous aurons les données suivantes prêtes à être consultées.
    

De cette façon, nous pouvons apporter de petites modifications intelligentes pour minimiser l'affichage de loaders vides à l'écran 😊.

## Comment implémenter le prefetching avec React

Dans cette section, nous allons passer brièvement en revue la manière d'implémenter l'application d'exemple de prefetching ci-dessus.

### Configuration du projet

Pour commencer la création de l'application de prefetching, suivez le processus ci-dessous :

Vous pouvez utiliser [vitejs](https://vitejs.dev/) (c'est ce que j'ai utilisé) ou [create-react-app](https://create-react-app.dev/) pour créer votre application. Collez la commande ci-dessous dans votre terminal :

```bash
yarn create vite prefetch-example --template react-ts
```

Une fois l'application créée, vous devriez avoir la structure de dossiers suivante lorsque vous ouvrez le dossier **prefetch-example** avec VS Code.

* ![Image de la structure des dossiers une fois l'application vitejs créée](https://cdn.hashnode.com/res/hashnode/image/upload/v1726764168271/2dc9bfa1-07d9-491e-96fd-e780c3623eeb.png align="center")
    

Plongeons maintenant dans les composants que nous allons construire pour cette application.

### Composants

Dans cet exemple, nous allons utiliser 3 composants :

* `PopoverExample`
    
* `UserProfile`
    
* `UserProfileWithFetching`
    

### Composant `PopoverExample`

Commençons par le premier composant qui est `PopoverExample`. Ce composant affiche un avatar image et du texte sur sa droite. Il devrait ressembler à ceci :

![Image du composant PopoverExample qui contient une image à gauche et du texte lorem ipsum à droite](https://cdn.hashnode.com/res/hashnode/image/upload/v1727002319443/bcc28972-fce0-42ba-899c-274513c4a7c6.png align="center")

Le but de ce composant est de servir d'exemple similaire à des scénarios réels. L'image de ce composant charge un composant popover lorsqu'elle est survolée.

![Image de l'élément popover qui contient les informations utilisateur lorsque l'image est survolée](https://cdn.hashnode.com/res/hashnode/image/upload/v1727002429245/9af8f26e-f149-41f7-b124-3ec2a0f5c80a.png align="center")

Voici le code du composant :

```typescript
import { useState } from "react";
import { useFloating, useHover, useInteractions } from "@floating-ui/react";
import ContentLoader from "react-content-loader";
import UserProfile from "./UserProfile";
import UserProfileWithFetching from "./UserProfileWithFetching";

export const MyLoader = () => (
	<ContentLoader
		speed={2}
		width={340}
		height={84}
		viewBox="0 0 340 84"
		backgroundColor="#d1d1d1"
		foregroundColor="#fafafa"
	>
		<rect x="0" y="0" rx="3" ry="3" width="67" height="11" />
		<rect x="76" y="0" rx="3" ry="3" width="140" height="11" />
		<rect x="127" y="48" rx="3" ry="3" width="53" height="11" />
		<rect x="187" y="48" rx="3" ry="3" width="72" height="11" />
		<rect x="18" y="48" rx="3" ry="3" width="100" height="11" />
		<rect x="0" y="71" rx="3" ry="3" width="37" height="11" />
		<rect x="18" y="23" rx="3" ry="3" width="140" height="11" />
		<rect x="166" y="23" rx="3" ry="3" width="173" height="11" />
	</ContentLoader>
);
export default function PopoverExample() {
	const [isOpen, setIsOpen] = useState(false);
	const [isLoading, setIsLoading] = useState(false);
	const [data, setData] = useState({});

	const { refs, floatingStyles, context } = useFloating({
		open: isOpen,
		onOpenChange: setIsOpen,
		placement: "top",
	});

	const hover = useHover(context);

	const { getReferenceProps, getFloatingProps } = useInteractions([hover]);

	const handleMouseEnter = () => {
		if (Object.keys(data).length === 0) {
			setIsLoading(true);
			fetch("https://jsonplaceholder.typicode.com/users/1")
				.then((resp) => resp.json())
				.then((data) => {
					setData(data);
					setIsLoading(false);
				});
		}
	};

	return (
		<div
			id="hover-example"
			style={{
				display: "flex",
				flexDirection: "row",
				alignItems: "center",
				textAlign: "left",
			}}
			onMouseEnter={handleMouseEnter}
		>
			<span
				style={{
					padding: "1rem",
				}}
			>
				<img
					ref={refs.setReference}
					{...getReferenceProps()}
					style={{
						borderRadius: "50%",
					}}
					src="https://cdn.jsdelivr.net/gh/alohe/avatars/png/vibrent_5.png"
				/>
			</span>
			<p>
				Lorem Ipsum is simply dummy text of the printing and typesetting
				industry. Lorem Ipsum has been the industry's standard dummy text ever
				since the 1500s, when an unknown printer took a galley of type and
				scrambled it to make a type specimen book. It has survived not only five
				centuries, but also the leap into electronic typesetting, remaining
				essentially unchanged. It was popularised in the 1960s with the release
				of Letraset sheets containing Lorem Ipsum passages, and more recently
				with desktop publishing software like Aldus PageMaker including versions
				of Lorem Ipsum.
			</p>
			{isOpen && (
				<div
					className="floating"
					ref={refs.setFloating}
					style={{
						...floatingStyles,
						backgroundColor: "white",
						color: "black",
						padding: "1rem",
						fontSize: "1rem",
					}}
					{...getFloatingProps()}
				>
					{isLoading ? (
						<MyLoader />
					) : (
						<UserProfile hasAdditionalDetails {...data} />
					)}
					{/* <UserProfileWithFetching /> */}
				</div>
			)}
		</div>
	);
}
```

Il se passe plusieurs choses ici, laissez-moi vous les expliquer étape par étape :

* Nous avons un `div` parent nommé `hover-example` qui contient une image et du texte.
    
* Ensuite, nous avons rendu conditionnellement un `div` avec le nom de classe `floating`. Il s'agit du composant popover réel qui s'ouvre lorsque vous survolez l'image.
    
    * Nous avons utilisé la [bibliothèque `floating-ui`](https://floating-ui.com/) et son [exemple de survol de base](https://floating-ui.com/docs/useHover) pour réaliser l'effet de survol du popover.
        
* À l'intérieur du popover, nous avons chargé conditionnellement `UserProfile` et le loader squelette. Ce loader apparaît lorsque nous récupérons les données du profil de l'utilisateur. Plus d'informations à ce sujet plus tard.
    
* Nous avons utilisé la bibliothèque [react-content-loader](https://github.com/danilowoz/react-content-loader) dans le composant `MyLoader`. Cette bibliothèque possède également un site web qui vous aide à créer des loaders, vous pouvez le consulter [ici](https://skeletonreact.com/).
    

### Composant `UserProfile`

Maintenant que nous avons défini notre exemple de `Popover`, il est temps d'entrer dans les détails du composant `UserProfile`.

Ce composant apparaît à l'intérieur du composant popover. Le but de ce composant est de charger les détails `name`, `email`, `phone`, `website` qui sont récupérés depuis [l'API JSON placeholder](https://jsonplaceholder.typicode.com/users/1).

Pour illustrer l'exemple de prefetching, nous devons nous assurer que le composant `UserProfile` agit uniquement comme un composant de présentation ; c'est-à-dire qu'aucune logique de récupération explicite n'est présente à l'intérieur.

Le point clé à noter à propos de ce composant est que la récupération des données se fait depuis le composant parent, qui est le composant `PopoverExample`. Dans ce composant, nous commençons à récupérer les données lorsque la souris entre dans ce composant (l'événement `mouseenter`). C'est la solution n°1 dont nous avons discuté précédemment.

Cela vous donne suffisamment de temps pour récupérer les données jusqu'à ce que l'utilisateur survole l'image. Voici le code :

```typescript
import { useEffect, useState } from "react";
import ContentLoader from "react-content-loader";

const MyLoader = () => (
	<ContentLoader
		speed={2}
		viewBox="0 0 476 124"
		backgroundColor="#d1d1d1"
		foregroundColor="#fafafa"
	>
		<rect x="4" y="43" rx="0" ry="0" width="98" height="30" />
	</ContentLoader>
);

export default function UserProfile(props: Record<string, string | boolean>) {
	const { name, email, phone, website, hasAdditionalDetails } = props;
	const [isLoading, setIsLoading] = useState(false);
	const [additionalData, setAdditionalData] = useState(0);

	useEffect(() => {
		if (hasAdditionalDetails) {
			setIsLoading(true);
			fetch("https://jsonplaceholder.typicode.com/albums")
				.then((resp) => resp.json())
				.then((data: Array<unknown>) => {
					const albumCount = data.reduce((acc, curr) => {
						if (curr.userId === 1) acc += 1;

						return acc;
					}, 0);
					setAdditionalData(albumCount);
				})
				.finally(() => {
					setIsLoading(false);
				});
		}
	}, [hasAdditionalDetails]);

	return (
		<div id="user-profile">
			<div id="user-name">nom : {name}</div>
			<div id="user-email">e-mail : {email}</div>
			<div id="user-phone">téléphone : {phone}</div>
			<div id="user-website">site web : {website}</div>
			{hasAdditionalDetails && (
				<>
					{isLoading ? (
						<MyLoader />
					) : (
						<div id="user-albums">Nombre d'albums : {additionalData}</div>
					)}
				</>
			)}
		</div>
	);
}
 
```

Ce composant utilise la prop `hasAdditionalDetails`. Le but de cette `prop` est de charger des données supplémentaires lors du montage du composant. Cela illustre la solution n°2 mentionnée ci-dessus.

### Composant `UserProfileWithFetching`

Ce composant est assez similaire à celui de `UserProfile`. Il contient simplement la logique de récupération des données lors du chargement du composant. Le but de ce composant est de montrer à quoi ressemblerait la solution générale sans la technique de prefetching.

Ce composant chargera donc toujours les données lors du montage du composant, ce qui affichera le loader squelette.

Voici le code :

```typescript
import { useEffect, useState } from "react";
import { MyLoader } from "./PopoverExample";

export default function UserProfileWithFetching() {
	const [isLoading, setIsLoading] = useState(false);
	const [data, setData] = useState<Record<string, string>>({});

	useEffect(() => {
		setIsLoading(true);
		fetch("https://jsonplaceholder.typicode.com/users/1")
			.then((resp) => resp.json())
			.then((data) => {
				setData(data);
				setIsLoading(false);
			});
	}, []);

	if (isLoading) return <MyLoader />;

	return (
		<div id="user-profile">
			<div id="user-name">nom : {data.name}</div>
			<div id="user-email">e-mail : {data.email}</div>
			<div id="user-phone">téléphone : {data.phone}</div>
			<div id="user-website">site web : {data.website}</div>
		</div>
	);
}
```

Le code complet de cette application peut être trouvé [ici](https://github.com/keyurparalkar/prefetch-examples).

## Trop de prefetching peut également causer des lenteurs

Un petit conseil : trop de prefetching n'est pas bon car :

* Cela pourrait ralentir votre application.
    
* Cela peut dégrader l'expérience utilisateur si le prefetching n'est pas appliqué de manière stratégique.
    

Le prefetching doit être appliqué lorsque vous connaissez le comportement de l'utilisateur. C'est-à-dire que vous êtes en mesure de prédire le mouvement de l'utilisateur grâce à des métriques et de dire s'il visite souvent une page. Dans ce cas, le prefetching est une bonne idée.

N'oubliez donc pas de toujours appliquer le prefetching de manière stratégique.

## Résumé

C'est tout pour le moment ! J'espère que vous avez apprécié cet article de blog. Dans cet article, vous avez appris que l'implémentation du prefetching peut considérablement améliorer la vitesse et la réactivité de votre application web, améliorant ainsi la satisfaction des utilisateurs.

Pour aller plus loin, veuillez vous référer aux articles ci-dessous :

* [Prefetching de pages](https://www.patterns.dev/vanilla/prefetch/)
    
* [Preload, Prefetch et Priorités dans Chrome](https://medium.com/reloading/preload-prefetch-and-priorities-in-chrome-776165961bbf)
    
* [Ce qu'il ne faut pas prefetcher](https://addyosmani.com/blog/what-not-to-prefetch-prerender/)
    

Pour plus de contenu, vous pouvez me suivre sur [Twitter](https://twitter.com/keurplkar), [GitHub](http://github.com/keyurparalkar) et [LinkedIn](https://www.linkedin.com/in/keyur-paralkar-494415107/).