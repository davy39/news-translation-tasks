---
title: Comment créer une application mobile de quiz avec React Native, ChatGPT et
  Supabase
subtitle: ''
author: David Asaolu
co_authors: []
series: null
date: '2024-02-29T17:30:26.000Z'
originalURL: https://freecodecamp.org/news/build-a-mobile-quiz-app
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Building-a-mobile-quiz-app-with-React-Native--ChatGPT-and-Supabase--1--1.png
tags:
- name: chatgpt
  slug: chatgpt
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
- name: supabase
  slug: supabase
seo_title: Comment créer une application mobile de quiz avec React Native, ChatGPT
  et Supabase
seo_desc: "In this tutorial, you'll learn how to build a mobile quiz application that\
  \ authenticates users, allows them to take tests, and ranks them based on their\
  \ scores. \nThe application leverages some of Supabase's features, such as authentication\
  \ and databa..."
---

Dans ce tutoriel, vous apprendrez à créer une application mobile de quiz qui authentifie les utilisateurs, leur permet de passer des tests et les classe en fonction de leurs scores. 

L'application tire parti de certaines fonctionnalités de Supabase, telles que l'authentification et le stockage de base de données, pour construire une application mobile full-stack sécurisée.

De plus, vous apprendrez à créer des applications React Native avec Expo, à générer un ensemble de questions et de réponses à partir de ChatGPT, et à effectuer des opérations CRUD et l'authentification des utilisateurs avec Supabase.

Pour comprendre pleinement ce tutoriel, vous devrez avoir une connaissance de base de React Native et de la récupération de données dans les applications React.

## Table des matières

* [Démonstration de l'application mobile](#heading-demo-de-lapplication-mobile)
* [Comment configurer une application React Native avec Expo](#heading-comment-configurer-une-application-react-native-avec-expo)
* [Comment styliser l'application React Native avec Tailwind CSS](#heading-comment-styliser-lapplication-react-native-avec-tailwind-css)
* [Comment construire les écrans de l'application](#heading-comment-construire-les-ecrans-de-lapplication)
* [Comment construire les écrans d'authentification](#heading-comment-construire-les-ecrans-dauthentification)
* [Comment construire les écrans d'onglets](#heading-comment-construire-les-ecrans-donglets)
* [Comment construire les écrans de pile](#heading-comment-construire-les-ecrans-de-pile)
* [Comment générer des questions et réponses de quiz à partir de ChatGPT](#heading-comment-generer-des-questions-et-reponses-de-quiz-a-partir-de-chatgpt)
* [Comment ajouter Supabase à React Native](#heading-comment-ajouter-supabase-a-react-native)
* [Comment ajouter l'authentification Supabase aux applications React Native](#heading-comment-ajouter-lauthentification-supabase-aux-applications-react-native)
* [Comment inscrire de nouveaux utilisateurs](#heading-comment-inscrire-de-nouveaux-utilisateurs)
* [Comment connecter les utilisateurs existants](#heading-comment-connecter-les-utilisateurs-existants)
* [Comment déconnecter les utilisateurs de l'application](#heading-comment-deconnecter-les-utilisateurs-de-lapplication)
* [Comment protéger les écrans des utilisateurs non authentifiés](#heading-comment-proteger-les-ecrans-des-utilisateurs-non-authentifies)
* [Comment interagir avec la base de données Supabase](#heading-comment-interagir-avec-la-base-de-donnees-supabase)
* [Comment sauvegarder le score de l'utilisateur dans la base de données](#heading-comment-sauvegarder-le-score-de-lutilisateur-dans-la-base-de-donnees)
* [Comment récupérer les données de Supabase](#heading-comment-recuperer-les-donnees-de-supabase)
* [Conclusion](#heading-conclusion)

## Démonstration de l'application mobile

Pour prévisualiser l'application, téléchargez [Expo Go](https://expo.dev/client) et collez les liens ci-dessous dans le champ URL de l'application :

**Android :** `exp://u.expo.dev/update/a4774250-e156-4d34-bcfc-a4f2549c2e1d`  
**iOS :** `exp://u.expo.dev/update/7e5f8ba5-89c4-4c1d-b219-a613ace642df`

![Image](https://www.freecodecamp.org/news/content/images/2024/02/app-demo.png)
_Scannez le code QR pour prévisualiser l'application mobile de quiz dans l'application Expo Go_

## Comment configurer une application React Native avec Expo

Expo est une plateforme open-source qui vous permet de créer facilement des applications multiplateformes avec JavaScript. Elle nous évite les configurations complexes nécessaires pour créer une application native avec le CLI React Native, ce qui en fait le moyen le plus simple et le plus rapide de construire et de publier des applications React Native.

Exécutez l'extrait de code ci-dessous pour créer un nouveau projet [Expo](https://expo.dev/) qui utilise [Expo Router](https://docs.expo.dev/router/introduction/) pour naviguer entre les écrans.

```bash
npx create-expo-app@latest --template tabs@50
```

[Expo Router](https://docs.expo.dev/router/introduction/) est un système de routage basé sur des fichiers open-source qui permet aux utilisateurs de naviguer facilement entre les écrans. Il est similaire à Next.js, où chaque nom de fichier représente son nom de route.

Démarrez le serveur de développement pour vous assurer que l'application fonctionne comme prévu.

```bash
npx expo start
```

### Comment styliser l'application React Native avec Tailwind CSS

Tailwind CSS est un framework CSS qui vous permet de créer facilement des applications modernes et époustouflantes. 

Cependant, pour styliser les applications Expo en utilisant Tailwind CSS, vous devez installer [NativeWind](https://www.nativewind.dev/v4/getting-started/expo-router) – une bibliothèque qui utilise Tailwind CSS comme langage de script.

Exécutez l'extrait de code ci-dessous pour installer NativeWind et ses dépendances :

```bash
npx expo install nativewind@^4.0.1 react-native-reanimated tailwindcss

```

Exécutez `npx tailwindcss init` dans votre terminal pour créer un fichier `tailwind.config.js`. Mettez à jour le fichier avec l'extrait de code ci-dessous :

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./app/**/*.{js,jsx,ts,tsx}"],
    presets: [require("nativewind/preset")],
    theme: {
        extend: {},
    },
    plugins: [],
};
```

Créez un fichier `globals.css` à la racine de votre projet et ajoutez les directives Tailwind ci-dessous :

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Mettez à jour le fichier `babel.config.js` avec le code ci-dessous :

```javascript
module.exports = function (api) {
  api.cache(true);
  return {
    presets: [
      ["babel-preset-expo", { jsxImportSource: "nativewind" }],
      "nativewind/babel",
    ],
  };
};
```

Créez un fichier `metro.config.js` à la racine de votre projet et collez l'extrait de code ci-dessous dans le fichier :

```javascript
const { getDefaultConfig } = require("expo/metro-config");
const { withNativeWind } = require('nativewind/metro');

const config = getDefaultConfig(__dirname)

module.exports = withNativeWind(config, { input: './globals.css' })
```

Enfin, importez le fichier `./globals.css` dans le fichier `app/_layout.tsx` pour vous permettre de styliser votre application avec Tailwind CSS :

```typescript
//👉🏻 Dans ./app/_layout.tsx

import "../globals.css";
```

Bon travail pour la création du projet React Native avec Expo ! Maintenant, vous êtes prêt à ajouter du style en utilisant Tailwind CSS. Si vous rencontrez des problèmes lors de l'installation de NativeWind, consultez la [documentation](https://www.nativewind.dev/v4/getting-started/expo-router) pour un guide étape par étape.

## Comment construire les écrans de l'application

Ici, je vais vous guider à travers la construction des écrans de l'application. Ils sont divisés en trois catégories :

* Les écrans d'authentification – les écrans d'enregistrement et de connexion.
* Les écrans de disposition d'onglets – les écrans de tableau de bord, de classement et de profil.
* Les écrans de pile – les écrans de test et de fin de test.

L'application invite les nouveaux utilisateurs à créer un compte et à se connecter avant d'autoriser l'accès aux écrans de disposition d'onglets. 

Sur l'écran du tableau de bord, les utilisateurs peuvent passer des tests sur divers sujets. L'écran de classement présente les dix meilleurs utilisateurs. Les utilisateurs peuvent se déconnecter ou prévisualiser leurs tentatives précédentes sur la page de profil.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/application-demo.gif)
_Démonstration de l'application_

### Comment construire les écrans d'authentification

Les écrans d'authentification acceptent l'email et le mot de passe de l'utilisateur et s'assurent que les identifiants sont valides avant de créer un compte ou d'accorder l'accès à l'application.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/auth-screens.png)
_Les écrans d'authentification_

Créez un fichier `index.tsx` et un fichier `register.tsx` dans le dossier `app` et un composant qui accepte l'email et le mot de passe de l'utilisateur en utilisant le composant [React Native TextInput](https://reactnative.dev/docs/textinput).

```typescript
import { Text, View, TextInput, Pressable, Alert } from "react-native";
import { Link, useRouter } from "expo-router";
import { useState } from "react";

export default function LoginScreen() {
	const [email, setEmail] = useState<string>("");
	const [password, setPassword] = useState<string>("");
	const [loading, setLoading] = useState<boolean>(false);
	const router = useRouter();

	//👇🏻 déclenché lorsque l'utilisateur soumet l'email et le mot de passe
	const handleLogin = () => {
		if (!email.trim() || !password.trim())
			return Alert.alert("Erreur", "Veuillez remplir tous les champs");
		setLoading(true);
		console.log({
			email,
			password,
		});
		router.replace("/(tabs)/");
	};

	return (
    	<View>
		{/** -- interface utilisateur--*/}
        </View>
	);
}
```

L'extrait de code stocke l'email et le mot de passe de l'utilisateur dans des états en utilisant le hook useState de React. La fonction `handleLogin` accepte l'email et le mot de passe de l'utilisateur lorsque le formulaire est soumis et s'assure qu'ils ne sont pas vides avant de les enregistrer dans la console et de rediriger l'utilisateur vers la page du tableau de bord.

Vous pouvez créer l'interface utilisateur en utilisant l'extrait de code ci-dessous. Il affiche les champs de saisie pour les identifiants de l'utilisateur et un bouton de connexion interactif qui exécute la fonction `handleLogin`. De plus, l'état `loading` garantit que le bouton n'est pressé qu'une seule fois.

```typescript
<View className=' flex-1'>
	<View className='w-full px-4'>
		<Text className='text-3xl mb-4 font-bold text-white text-center'>
			Se connecter
		</Text>

		<Text className='text-lg text-gray-200'>Adresse e-mail</Text>
		<TextInput
			className='w-full border-b-[1px] py-4 rounded-md mb-3 text-white font-bold'
			value={email}
			onChangeText={setEmail}
		/>
		<Text className='text-lg text-gray-200'>Mot de passe</Text>
		<TextInput
			className='w-full border-b-[1px] py-4 rounded-md mb-3 text-white font-bold'
			secureTextEntry
			value={password}
			onChangeText={setPassword}
		/>
		<Pressable
			className={`w-full ${
				loading ? "bg-orange-200" : "bg-orange-600"
			} rounded-xl p-4 border-[1px] border-orange-200`}
			disabled={loading}
			onPress={() => handleLogin()}
		>
			<Text className='text-white text-center font-bold text-xl'>
				{loading ? "Authentification..." : "Se connecter"}
			</Text>
		</Pressable>
		<Text className='text-center mt-2 text-orange-200'>
			Vous n'avez pas de compte ?{" "}
			<Link href='/register'>
				<Text className='text-white'>S'inscrire</Text>
			</Link>
		</Text>
	</View>
</View>
```

Par exemple, l'état `loading` devient vrai lorsque l'utilisateur clique sur le bouton de connexion. Le composant Pressable (bouton) a un attribut `disabled` défini sur l'état `loading` pour s'assurer que l'utilisateur ne presse pas le bouton plusieurs fois. De plus, vous pouvez utiliser l'état de chargement pour notifier l'utilisateur que la demande est en cours de traitement.

Le fichier `register.tsx` est également similaire au fichier `login.tsx`. Vous devez simplement changer les mots de Login à Register.

### Comment construire les écrans d'onglets

Les écrans d'onglets se composent des écrans Tableau de bord, Classement et Profil.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/tab-screens.png)
_Les écrans d'onglets_

Créez un dossier `(tabs)` contenant les fichiers `index.tsx`, `leaderboard.tsx`, `profile.tsx` et `_layout.tsx` dans le dossier `app`.

```bash
cd app
mkdir (tabs)
cd (tabs)
touch index.tsx leaderboard.tsx profile.tsx _layout.tsx

```

Après avoir créé le fichier `_layout.tsx` dans le dossier (tabs), mettez à jour le `_layout.tsx` pour spécifier la navigation des écrans d'onglets pour les écrans nouvellement créés. Les écrans utilisent des icônes de la [bibliothèque Expo Vector Icons](https://icons.expo.fyi/Index).

```typescript
import { Tabs } from "expo-router";
import { Ionicons, MaterialIcons, FontAwesome5 } from "@expo/vector-icons";
import { ActivityIndicator } from "react-native";

export default function TabScreen() {
	return (
		<Tabs
			screenOptions={{
				tabBarActiveTintColor: "#f97316",
				tabBarInactiveTintColor: "gray",
				tabBarShowLabel: false,
				headerShown: false,
				tabBarStyle: {
					backgroundColor: "#ffedd5",
					borderTopColor: "#ffedd5",
				},
			}}
		>
			<Tabs.Screen
				name='index'
				options={{
					tabBarIcon: ({ color }) => (
						<Ionicons name='home' size={24} color={color} />
					),
				}}
			/>
			<Tabs.Screen
				name='leaderboard'
				options={{
					tabBarIcon: ({ color }) => (
						<MaterialIcons name='leaderboard' size={24} color={color} />
					),
				}}
			/>
			<Tabs.Screen
				name='profile'
				options={{
					tabBarIcon: ({ color }) => (
						<FontAwesome5 name='user-alt' size={24} color={color} />
					),
				}}
			/>
		</Tabs>
	);
}
```

Ensuite, mettez à jour le composant `RootLayoutNav` dans le fichier `_app/layout.tsx` pour rendre tous les écrans de l'application.

```typescript
function RootLayoutNav() {
	return (
		<Stack screenOptions={{ headerShown: false }}>
			<Stack.Screen name='(tabs)' />
			<Stack.Screen name='(stack)' />
			<Stack.Screen name='index' />
			<Stack.Screen name='register' />
		</Stack>
	);
}
```

#### L'écran du tableau de bord

Mettez à jour le composant pour permettre aux utilisateurs de sélectionner quatre catégories parmi une liste de catégories.

```typescript
export default function HomeScreen() {
	const greet = getGreeting();
	const router = useRouter();
	const { session } = useAuth();
	const [loading, setLoading] = useState<boolean>(false);
	const [userCategories, setUserCategories] = useState<string[]>([]);

	const fetchQuestions = async () => {};

	const handleStartTest = async () => {
		Alert.alert("Démarrer le test", "Êtes-vous sûr de vouloir commencer le test ?", [
			{
				text: "Annuler",
				style: "destructive",
			},
			{
				text: "Oui",
				onPress: () => fetchQuestions(),
			},
		]);
	};

	return (
		<SafeAreaView className='flex-1 bg-orange-100 px-4 py-2'>
			<View className='flex flex-row items-center justify-between mb-2'>
				<View>
					<Text className='font-bold text-2xl mb-[1px]'>
						Bonjour
						<Ionicons name='partly-sunny-sharp' size={24} color='orange' />
					</Text>

					<Text className='text-lg'>Bienvenue Utilisateur</Text>
				</View>
			</View>
			{userCategories.length === 4 && (
				<Pressable
					className={`w-full h-[70px] flex items-center justify-center ${
						loading ? "bg-orange-300" : "bg-orange-500"
					} rounded-xl mb-2`}
					disabled={loading}
					onPress={() => handleStartTest()}
				>
					<Text className='text-xl font-bold text-orange-50'>
						{loading ? "Chargement des questions..." : "COMMENCER LE TEST"}
					</Text>
				</Pressable>
			)}

			<View className='w-full flex-1'>
				<Text className='text-xl font-bold text-orange-500 mb-4'>
					Catégories disponibles
				</Text>
				<FlatList
					data={categories}
					numColumns={2}
					contentContainerStyle={{ width: "100%", gap: 10 }}
					columnWrapperStyle={{ gap: 10 }}
					renderItem={({ item }) => (
						<Categories
							item={item}
							userCategories={userCategories}
							setUserCategories={setUserCategories}
						/>
					)}
					showsVerticalScrollIndicator={false}
					keyExtractor={(item) => item.id}
				/>
			</View>
		</SafeAreaView>
	);
}
```

L'extrait de code ci-dessus rend une liste de catégories où les utilisateurs peuvent sélectionner seulement quatre catégories pour répondre aux questions et commencer le quiz.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/dashboard-screen.gif)
_L'écran du tableau de bord_

#### L'écran du classement

L'écran du classement affiche les dix meilleurs utilisateurs classés par ordre décroissant.

```typescript
import { Text, FlatList, SafeAreaView } from "react-native";
import Board from "../../components/Board";

interface Props {
	total_score: number;
	user_id: string;
}

export default function LeaderboardScreen() {
	const [leaderboard, setLeaderboard] = useState<Props[]>([]);

	return (
		<SafeAreaView className='flex-1 bg-orange-100 p-4'>
			<Text className='text-2xl font-bold text-gray-500 text-center mb-6'>
				Classement
			</Text>

			<FlatList
				data={leaderboard}
				renderItem={({ item }) => <Board item={item} />}
				keyExtractor={(item) => item.user_id}
				showsVerticalScrollIndicator={false}
			/>
		</SafeAreaView>
	);
}
```

L'extrait de code ci-dessus rend une FlatList avec dix éléments. Vous pouvez créer un tableau contenant dix utilisateurs et le passer dans la FlatList pour l'instant.

#### L'écran du profil

L'écran du profil affiche l'image de l'utilisateur, ses tentatives récentes et un bouton de déconnexion qui permet à l'utilisateur de se déconnecter de l'application.

```typescript
export default function ProfileScreen() {
	const [loading, setLoading] = useState<boolean>(false);
	const [total_score, setTotalScore] = useState<number>(0);
	const [attempts, setAttempts] = useState<string[]>([]);

	const handleSignOut = async () => {
		setLoading(true);
	};

	return (
		<SafeAreaView className='flex-1 bg-orange-100 p-4'>
			<View className='flex items-center justify-center mb-6'>
				<Text className='text-gray-600 mb-[1px]'>
					<FontAwesome name='star' size={20} color='red' />
					<Text>45</Text>
				</Text>
				<Text className='text-gray-600 mb-2'>@dhastix</Text>

				<Pressable onPress={() => handleSignOut()} disabled={loading}>
					<Text className='text-red-500'>
						{loading ? "Déconnexion..." : "Se déconnecter"}
					</Text>
				</Pressable>
			</View>

			<Text className='font-bold text-xl text-gray-700 mb-3 px-4'>
				Tentatives récentes
			</Text>

			<FlatList
				data={attempts}
				contentContainerStyle={{ padding: 15 }}
				renderItem={({ item }) => <Attempts item={item} />}
				keyExtractor={(item, index) => index.toString()}
				showsVerticalScrollIndicator={false}
			/>
		</SafeAreaView>
	);
}
```

L'extrait de code ci-dessus affiche l'image de l'utilisateur, le bouton de déconnexion et toutes les tentatives de l'utilisateur. Vous pouvez créer un tableau d'éléments à des fins de test.

### Comment construire les écrans de pile

Les écrans de pile comprennent deux écrans – l'écran de quiz et l'écran qui affiche le score de l'utilisateur après avoir terminé une session de quiz.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/test-screens-1.png)
_Les écrans de pile_

#### L'écran de quiz

L'écran de quiz affiche un minuteur qui compte à rebours à partir de 15 secondes avant de passer à la question suivante. Il montre la question, sa catégorie, les options disponibles, les boutons Passer et Suivant, et une icône d'annulation.

Créez un écran similaire à celui montré ci-dessous. Vous pouvez utiliser [ceci](https://github.com/dha-stix/techtest-app/blob/main/app/(stack)/test.tsx) comme guide.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/test-screen.gif)
_L'écran de quiz_

#### L'écran de fin de quiz

Il affiche le score de l'utilisateur après avoir terminé un test.

```typescript
import {
	SafeAreaView,
	Text,
	Pressable,
	View,
	ImageBackground,
} from "react-native";
import { MaterialIcons } from "@expo/vector-icons";
import { useLocalSearchParams } from "expo-router";

export default function CompletedScreen() {
	const { score } = useLocalSearchParams();

	return (
		<View className='flex flex-1 bg-orange-400'>
			<ImageBackground
				source={{ uri: "https://source.unsplash.com/NAP14GEjvh8" }}
				className='flex-1 p-4'
			>
				<SafeAreaView />
				<Pressable onPress={() => router.replace("/(tabs)/")}>
					<MaterialIcons name='cancel' size={60} color='white' />
				</Pressable>

				<View className='flex-1 flex items-center justify-center'>
					<View className='bg-orange-50 w-full py-[50px] rounded-xl p-4 flex items-center justify-center shadow-lg shadow-orange-500'>
						<Text className='text-3xl text-orange-600 font-bold mb-4'>
							{Number(score) > 20 ? "Félicitations\ud83e\udd73" : "Désolé ! Vous avez perdu \ud83e\udd72"}
						</Text>
						<Text className='font-bold text-xl'>Vous avez obtenu {score} !</Text>
					</View>
				</View>
			</ImageBackground>
		</View>
	);
}
```

L'extrait de code ci-dessus accepte le score de l'utilisateur comme paramètre après avoir terminé le quiz et affiche le score à l'utilisateur.

## Comment générer des questions et réponses de quiz à partir de ChatGPT

Lors de la création d'une application de quiz, la première question est : comment obtenir les questions et les options pour l'application ? Vous pouvez soit créer une liste de questions, soit rechercher une API publique appropriée.

Cependant, je vais vous guider à travers la création d'une liste de questions et d'options au format JSON en utilisant ChatGPT. Utilisez cette invite pour générer des questions et des réponses à partir de ChatGPT :

> _Générez 25 questions distinctes sur <SUJET> et assurez-vous qu'elles sont au format JSON contenant un id, une catégorie qui est <SUJET>, un attribut question contenant la question, un tableau d'options de 3 options, et une propriété de réponse._

L'invite retourne un résultat JSON contenant les questions et les réponses. Vous pouvez les héberger sur GitHub ou les sauvegarder dans une base de données.

Les questions et réponses que j'utilise dans cette application mobile sont disponibles sur [GitHub](https://github.com/dha-stix/trivia-app/tree/main/questions). N'hésitez pas à cloner ou copier les fichiers.

Une fois vos questions et réponses prêtes, vous pouvez connecter l'application à Supabase.

## Comment ajouter Supabase à React Native

Supabase est une alternative open-source à Firebase qui vous permet de créer des applications logicielles sécurisées et évolutives en quelques minutes.

Il fournit une base de données Postgres sécurisée, un système complet de gestion des utilisateurs qui gère diverses formes d'authentification (y compris l'email et le mot de passe, la connexion par email et l'authentification sociale), un système de stockage de fichiers qui vous permet de stocker et de servir des fichiers de toute taille, une communication en temps réel et de nombreuses autres fonctionnalités.

Dans ce tutoriel, je vais vous guider à travers les étapes suivantes :

* Comment authentifier les utilisateurs et contrôler l'accès à certains écrans de l'application avec Supabase.
* Comment sauvegarder les scores des utilisateurs dans la base de données pour vous permettre de les classer en fonction de leurs scores.

Tout d'abord, vous devez installer Supabase et ses dépendances requises. Vous pouvez le faire avec les commandes suivantes :

```bash
npm install @supabase/supabase-js 
npm install react-native-elements @react-native-async-storage/async-storage react-native-url-polyfill
npx expo install expo-secure-store
```

Créez un fichier `supabase.ts` dans votre projet et copiez l'extrait de code ci-dessous dans le fichier pour initier Supabase :

```typescript
import "react-native-url-polyfill/auto";
import * as SecureStore from "expo-secure-store";
import { createClient } from "@supabase/supabase-js";

const ExpoSecureStoreAdapter = {
	getItem: (key: string) => {
		return SecureStore.getItemAsync(key);
	},
	setItem: (key: string, value: string) => {
		SecureStore.setItemAsync(key, value);
	},
	removeItem: (key: string) => {
		SecureStore.deleteItemAsync(key);
	},
};

const supabaseUrl = "YOUR_REACT_NATIVE_SUPABASE_URL";
const supabaseAnonKey = "YOUR_REACT_NATIVE_SUPABASE_ANON_KEY";

export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
	auth: {
		storage: ExpoSecureStoreAdapter as any,
		autoRefreshToken: true,
		persistSession: true,
		detectSessionInUrl: false,
	},
});
```

Ensuite, visitez la [page d'accueil de Supabase](https://supabase.com), connectez-vous et créez une nouvelle organisation et un nouveau projet.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/project.png)
_Créer un nouveau projet Supabase_

Cliquez sur l'icône des paramètres dans la barre latérale et sélectionnez API pour copier l'URL du projet et la clé API publique.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-24-at-17.50.34.png)
_Paramètres de l'API Supabase contenant les identifiants du projet_

Créez un fichier `.env.local` et copiez les identifiants dans les variables. Mettez à jour le fichier `supabase.ts` pour utiliser l'URL et la clé API de Supabase.

```txt
EXPO_PUBLIC_API_URL=<YOUR_SUPABASE_URL>
EXPO_PUBLIC_API_KEY=<YOUR_SUPABASE_API_KEY>
```

Félicitations ! Vous pouvez maintenant interagir avec Supabase depuis votre application et accéder à diverses fonctionnalités telles que l'authentification, la base de données, le stockage de fichiers, etc.

## Comment ajouter l'authentification Supabase aux applications React Native

Supabase offre diverses formes d'authentification. Mais nous n'avons besoin que de la méthode d'authentification par email et mot de passe pour cette application.

### Comment inscrire de nouveaux utilisateurs

L'extrait de code ci-dessous accepte un email et un mot de passe et crée un compte pour l'utilisateur. Sinon, il retourne une erreur si l'un des identifiants est invalide.

```typescript
//👇🏻 importer supabase depuis le fichier supabase
import { supabase } from "../lib/supabase";

//👇🏻 fonction d'inscription
const handleRegister = async () => {
	if (!email.trim() || !password.trim())
		return Alert.alert("Erreur", "Veuillez remplir tous les champs");
	const { error } = await supabase.auth.signUp({ email, password });
	if (error) return Alert.alert("Erreur", error.message);
	router.replace("/");
};
```

Avec la fonction `supabase.auth.signUp()`, Supabase gère le processus d'authentification. Si cela réussit, l'utilisateur est redirigé vers la page de connexion. Sinon, il affiche un message d'erreur.

### Comment connecter les utilisateurs existants

Cette fonction permet aux utilisateurs existants d'accéder à l'application. Elle accepte l'email et le mot de passe de l'utilisateur et connecte l'utilisateur à l'application.

```typescript
//👇🏻 importer supabase depuis le fichier supabase
import { supabase } from "../lib/supabase";

//👇🏻 fonction de connexion
const handleLogin = async () => {
	if (!email.trim() || !password.trim())
		return Alert.alert("Erreur", "Veuillez remplir tous les champs");
	const { error } = await supabase.auth.signInWithPassword({ email, password });
	if (error) return Alert.alert("Erreur", error.message);
	router.replace("/(tabs)/");
};
```

La fonction `supabase.auth.signInWithPassword()` valide l'email et le mot de passe de l'utilisateur et redirige l'utilisateur vers l'écran du tableau de bord. Sinon, elle retourne l'erreur d'authentification nécessaire.

### Comment déconnecter les utilisateurs de l'application

Supabase permet également aux utilisateurs de se déconnecter de l'application. Vous pouvez exécuter cette fonction lorsque l'utilisateur clique sur un bouton dans la page de profil.

```typescript
//👇🏻 importer supabase depuis le fichier supabase
import { supabase } from "../lib/supabase";

//👇🏻 fonction de déconnexion
const handleSignOut = async () => {
	try {
		const { error } = await supabase.auth.signOut();
		if (error) throw error;
	} catch (error) {
		console.log(error);
	}
};
```

### Comment protéger les écrans des utilisateurs non authentifiés

Vous avez pu ajouter les fonctionnalités d'inscription, de connexion et de déconnexion à l'application React Native. Mais le tableau de bord et les autres écrans contenant des données sensibles sont toujours accessibles aux utilisateurs non authentifiés.

Comment corriger cela ?

Dans cette section, je vais vous guider à travers la protection des écrans contre les utilisateurs non autorisés en utilisant l'[API de contexte React](https://react.dev/reference/react/createContext).

L'API de contexte React nous permet de passer des données à travers l'arbre des composants sans avoir besoin de passer des props manuellement à chaque niveau.

Créez un fichier `AuthProvider.tsx`. C'est ici que les données à passer aux écrans de l'application sont stockées. Copiez l'extrait de code ci-dessous dans le fichier :

```typescript
import { supabase } from "./supabase";
import { Session } from "@supabase/supabase-js";
import {
	PropsWithChildren,
	createContext,
	useContext,
	useEffect,
	useState,
} from "react";

type AuthData = {
	session: Session | null;
	loading: boolean;
};

//👇🏻 données à passer aux composants
const AuthContext = createContext<AuthData>({
	session: null,
	loading: true,
});

export default function AuthProvider({ children }: PropsWithChildren) {
	const [session, setSession] = useState<Session | null>(null);
	const [loading, setLoading] = useState(true);

	//👇🏻 récupère la session actuelle de l'utilisateur
	useEffect(() => {
		const fetchSession = async () => {
			const {
				data: { session },
			} = await supabase.auth.getSession();
			setSession(session);
			setLoading(false);
		};

		fetchSession();
		supabase.auth.onAuthStateChange((_event, session) => {
			setSession(session);
			setLoading(false);
		});
	}, []);

	return (
		<AuthContext.Provider value={{ session, loading }}>
			{children}
		</AuthContext.Provider>
	);
}
//👇🏻 hook personnalisé pour utiliser le contexte (données)
export const useAuth = () => useContext(AuthContext);
```

L'extrait de code récupère la session actuelle de l'utilisateur. Si l'utilisateur est connecté, les variables d'état de session et de chargement sont mises à jour pour montrer que l'utilisateur est actif, et elles sont passées à d'autres composants au sein de l'application.

Le hook personnalisé `useAuth` vous permet d'accéder aux variables d'état (session et loading) au sein des écrans de l'application.

Pour accéder au contexte (données) disponible au sein des écrans de l'application, enveloppez toute l'application avec le `AuthProvider`. Donc maintenant, mettez à jour le composant `RootLayoutNav` dans le fichier `app/_layout.tsx` comme montré ci-dessous :

```typescript
import AuthProvider from "../lib/AuthProvider";

function RootLayoutNav() {
	return (
		<AuthProvider>
			<Stack screenOptions={{ headerShown: false }}>
				<Stack.Screen name='(tabs)' />
				<Stack.Screen name='(stack)' />
				<Stack.Screen name='index' />
				<Stack.Screen name='register' />
			</Stack>
		</AuthProvider>
	);
}
```

Félicitations ! Vous avez réussi à configurer le contexte. Ensuite, comment lire le contexte et s'assurer que seuls les utilisateurs authentifiés peuvent voir certains des écrans de l'application ?

Vous pouvez le faire en utilisant le hook personnalisé `useAuth`. Par exemple, vous pouvez protéger les écrans d'onglets via le fichier `(tabs)/_layout.tsx`.

```typescript
import { Tabs, Redirect } from "expo-router";
import { useAuth } from "../../lib/AuthProvider";
import { ActivityIndicator } from "react-native";

export default function TabScreen() {
	const { session, loading } = useAuth();

	if (!session) {
		return <Redirect href='/' />;
	}

	if (loading) {
		return <ActivityIndicator size='large' color='#f97316' />;
	} else {
		return (
			<Tabs
				screenOptions={{
					tabBarActiveTintColor: "#f97316",
					tabBarInactiveTintColor: "gray",
					tabBarShowLabel: false,
					headerShown: false,
					tabBarStyle: {
						backgroundColor: "#ffedd5",
						borderTopColor: "#ffedd5",
					},
				}}
			>
				{/**-- écrans--*/}
			</Tabs>
		);
	}
}
```

L'extrait de code ci-dessus vérifie s'il y a une session pour l'utilisateur actuel. Si null, l'application redirige l'utilisateur vers l'écran de connexion. Si l'application n'a pas encore déterminé le statut de l'utilisateur, elle affiche une icône de chargement.

## Comment interagir avec la base de données Supabase

Dans cette section, je vais vous guider à travers la création de la base de données pour l'application mobile. Vous apprendrez à stocker et récupérer les scores des utilisateurs et à les classer en fonction de leur score total.

Avant de continuer, notez que l'application calcule le score de l'utilisateur après avoir répondu à chaque question sur l'écran de test. À la fin, le score de l'utilisateur est récupéré et affiché sur l'écran de fin de test.

```typescript
const handleSave = () => {
	//👇🏻 vérifie si l'utilisateur n'a pas terminé le test
	if (count < questions.length - 1) {
		//👇🏻 met à jour le score de l'utilisateur si la réponse sélectionnée est correcte
		if (questions[count].answer === userAnswer) {
			setUserScore((userScore) => userScore + 1);
		}
		//👇🏻 change la question, rafraîchit la réponse sélectionnée et le temps
		setCount((count) => count + 1);
		setSelectedBox(null);
		setTime(15);
	} else {
		//👇🏻 test terminé
		router.push({
			pathname: "/(stack)/completed",
			params: { score: userScore },
		});
	}
};
```

Dans votre projet Supabase, sélectionnez Table Editor dans le menu de la barre latérale et créez une nouvelle table contenant les colonnes suivantes :

* `id` – contient un identifiant unique pour chaque ligne de données.
* `created_at` – représente l'heure à laquelle les données ont été créées.
* `attempts` – un tableau de texte contenant les attributs de score et de date.
* `total_score` – représente le score cumulatif d'un utilisateur. Nous classerons les utilisateurs en utilisant ce score
* `user_id` – un identifiant unique utilisé pour identifier les données de chaque utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-24-at-10.05.55.png)
_Les colonnes de la table_

Enfin, vous pouvez ajouter une sécurité au niveau des lignes qui permet uniquement aux utilisateurs authentifiés d'interagir avec la base de données.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-24-at-10.20.51.png)
_La politique de sécurité au niveau des lignes de la table_

### Comment sauvegarder le score de l'utilisateur dans la base de données

Avant de pouvoir sauvegarder le score d'un utilisateur dans la base de données, vous devez vérifier si les données de l'utilisateur existent déjà – ce qui signifie que l'utilisateur a déjà passé un test. Si c'est vrai, vous devez mettre à jour le score de l'utilisateur avec le dernier score de test. Sinon, ajoutez les données à la base de données.

L'extrait de code ci-dessous accepte le score de l'utilisateur et l'identifiant de l'utilisateur (à partir des données de session) et sauvegarde le score de l'utilisateur dans Supabase.

```typescript
export const saveScore = async (userScore: number, userID: string) => {
	try {
		//👇🏻 vérifie si les données de l'utilisateur existent
		const { data, error } = await supabase
			.from("scores")
			.select()
			.eq("user_id", userID);
		if (error) throw error;

		//👇🏻 si les données de l'utilisateur n'existent pas, insère une nouvelle
		if (error || !data.length) {
			const { data, error } = await supabase
				.from("scores")
				.insert({
					attempts: [{ score: userScore, date: getCurrentDate() }],
					total_score: userScore,
					user_id: userID,
				})
				.single();
			if (error) throw error;
		} else {
			//👇🏻 si les données de l'utilisateur existent, met à jour les tentatives et le total_score
			const { data: updateData, error } = await supabase
				.from("scores")
				.update({
					attempts: [
						...data[0].attempts,
						{ score: userScore, date: getCurrentDate() },
					],
					total_score: data[0].total_score + userScore,
				})
				.eq("user_id", userID);
			if (error) throw error;
		}
	} catch (err) {
		console.log(err);
	}
};
```

### Comment récupérer les données de Supabase

Rappelez-vous que vous devez classer les utilisateurs en fonction de leurs scores sur l'écran de classement et récupérer les tentatives de l'utilisateur sur l'écran de profil.

L'extrait de code ci-dessous accepte l'identifiant d'un utilisateur et récupère les tentatives et le score total de la base de données.

```typescript
export const getUserAttempts = async (userID: string) => {
	try {
		const { data, error } = await supabase
			.from("scores")
			.select("attempts, total_score")
			.eq("user_id", userID);
		if (error) throw error;
		return { attempts: data[0].attempts, total_score: data[0].total_score };
	} catch (err) {
		return { attempts: "", total_score: 0 };
	}
};
```

L'extrait de code ci-dessous récupère les dix meilleurs utilisateurs de la base de données en fonction de leur score.

```typescript
export const getLeaderBoard = async () => {
	try {
		const { data, error } = await supabase
			.from("scores")
			.select("total_score, user_id")
			.order("total_score", { ascending: false })
			.limit(10);
		if (error) throw error;
		return data;
	} catch (err) {
		return null;
	}
};
```

Félicitations ! Vous avez réussi à compléter le projet pour ce tutoriel.

## Conclusion

Dans ce tutoriel, vous avez appris à :

* construire des applications mobiles React Native avec Expo,
* styliser vos applications mobiles avec [Tailwind CSS](https://www.nativewind.dev/),
* créer des navigations d'écrans de pile et d'onglets en utilisant [Expo Router](https://docs.expo.dev/router/introduction/),
* utiliser Supabase et tirer parti de ses fonctionnalités d'authentification et de base de données pour construire des applications full-stack.

Supabase est un outil incroyable qui vous permet de construire une application logicielle full-stack sans tracas. Si vous envisagez de livrer rapidement des produits logiciels ou des projets secondaires, envisagez d'utiliser Supabase.

Expo nous évite également les complexités de la configuration et du développement d'applications mobiles en utilisant le [CLI React Native](https://reactnative.dev/docs/environment-setup). Il vous permet de vous concentrer davantage sur la construction de vos applications tout en gérant les configurations nécessaires, y compris le déploiement.

N'hésitez pas à personnaliser l'application en utilisant [ChatGPT](https://chat.openai.com/) pour générer des questions et des réponses adaptées à n'importe quelle niche ou sujet.

Le code source de ce tutoriel est disponible dans ce [dépôt GitHub](https://github.com/dha-stix/techtest-app).

Merci d'avoir lu !