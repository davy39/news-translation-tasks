---
title: Comment créer un contrôle d'accès basé sur les rôles (RBAC) avec des Custom
  Claims en utilisant les règles Firebase
subtitle: ''
author: Ayodele Aransiola
co_authors: []
series: null
date: '2025-10-15T19:52:01.007Z'
originalURL: https://freecodecamp.org/news/firebase-rbac-custom-claims-rules
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1760557889448/ac51a7a3-cdd8-46c9-964d-a7e281e1affc.png
tags:
- name: Firebase
  slug: firebase
- name: Security
  slug: security
- name: rbac
  slug: rbac
- name: Web Development
  slug: web-development
- name: JavaScript
  slug: javascript
seo_title: Comment créer un contrôle d'accès basé sur les rôles (RBAC) avec des Custom
  Claims en utilisant les règles Firebase
seo_desc: When you’re building an application, not all users should have the same
  level of access. For example, an admin might be able to update or delete some data
  (logs excluded), while a regular user should only be able to read it. This is where
  Role-Based ...
---

Lorsque vous construisez une application, tous les utilisateurs ne devraient pas avoir le même niveau d'accès. Par exemple, un administrateur peut être capable de mettre à jour ou de supprimer certaines données (hors journaux), tandis qu'un utilisateur standard ne devrait pouvoir que les lire. C'est là qu'intervient le **contrôle d'accès basé sur les rôles (RBAC)**.

[Firebase](https://firebase.google.com/) rend cela possible grâce aux [custom claims](https://firebase.google.com/docs/auth/admin/custom-claims) (revendications personnalisées) et aux règles de sécurité. Dans cet article, vous apprendrez comment :

* Ajouter des custom claims aux utilisateurs avec le SDK Firebase Admin.
    
* Utiliser les règles de sécurité Firebase pour appliquer le RBAC.
    
* Tester vos règles avec différents rôles.
    

À la fin, vous disposerez d'une configuration fonctionnelle où les rôles comme `admin` et `user` sont appliqués directement dans Firestore.

## Table des matières

* [Étape 1 : Comprendre les Custom Claims Firebase](#heading-etape-1-comprendre-les-custom-claims-firebase)
    
* [Étape 2 : Attribuer un rôle avec le SDK Firebase Admin](#heading-etape-2-attribuer-un-role-avec-le-sdk-firebase-admin)
    
* [Étape 3 : Écrire et appliquer des règles de sécurité Firestore](#heading-etape-3-ecrire-et-appliquer-des-regles-de-securite-firestore)
    
* [Étape 4 : Construire le Frontend avec Next.js et Firebase](#heading-etape-4-construire-le-frontend-avec-nextjs-et-firebase)
    
* [Étape 5 : Tester le flux de travail RBAC](#heading-etape-5-tester-le-flux-de-travail-rbac)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Pour suivre ce tutoriel, vous devez :

* Avoir un projet Firebase configuré avec Authentication et Firestore activés.
    
* Être à l'aise avec JavaScript/Node.js.
    
* Avoir installé le SDK Firebase et le SDK Admin.
    

Si vous débutez avec Firebase, consultez le [guide d'installation officiel](https://firebase.google.com/docs/web/setup) avant de continuer.

## Étape 1 : Comprendre les Custom Claims Firebase

Les custom claims de Firebase vous permettent d'attacher des informations supplémentaires (comme un rôle) au jeton d'authentification d'un utilisateur. Vous définissez ces informations **côté serveur** à l'aide du SDK Admin. Elles sont incluses dans le `request.auth.token` de l'utilisateur, et vous ne pouvez pas les définir directement depuis le client (pour des raisons de sécurité).

Voici un exemple : le jeton d'ID d'un utilisateur pourrait ressembler à ceci après l'ajout d'une claim :

```json
{
  "user_id": "abc123",
  "email": "jane@example.com",
  "role": "admin"
}
```

Dans cet exemple, le champ `role` détermine les privilèges d'accès dans votre application. Firebase inclut automatiquement cette claim dans le jeton d'ID de l'utilisateur, afin qu'elle puisse être validée de manière sécurisée tant sur le serveur que dans les règles Firestore.

## Étape 2 : Attribuer un rôle avec le SDK Firebase Admin

Le SDK Firebase Admin vous permet de gérer les utilisateurs et d'attribuer des rôles de manière sécurisée depuis votre backend (ou via un script).

Tout d'abord, installez le SDK Admin dans un environnement Node (pas dans votre application frontend) :

```bash
npm install firebase-admin
```

Ensuite, initialisez-le avec les informations d'identification de votre compte de service Firebase :

```js
const admin = require("firebase-admin");
const serviceAccount = require("./service-account.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});
```

Pour obtenir votre fichier service-account.json, accédez aux paramètres de votre projet Firebase > paramètres du projet > comptes de service.

![une image montrant l'interface du compte de service sur la console firebase](https://cdn.hashnode.com/res/hashnode/image/upload/v1760235082674/8f542b00-2246-4585-b267-f8cb663797ea.png align="center")

Cliquez sur "Générer une nouvelle clé privée", et le fichier JSON sera automatiquement téléchargé. Vous pouvez renommer le fichier ou l'utiliser tel quel.

Vous pouvez maintenant définir une fonction simple pour définir le rôle d'un utilisateur :

```js
async function setUserRole(uid, role) {
  await admin.auth().setCustomUserClaims(uid, { role });
  console.log(`Rôle ${role} attribué à l'utilisateur ${uid}`);
}
```

Le paramètre `role` peut être tout ce que vous définissez, par exemple :

* `"admin"` : Accès complet en lecture/écriture.
    
* `"editor"` : Peut créer ou modifier du contenu limité.
    
* `"user"` : Accès en lecture seule.
    

Le rôle que vous attribuez à un utilisateur dépend des besoins de votre application. Dans la plupart des applications, vous commencerez simplement, peut-être juste avec `admin` et `user`, et évoluerez avec le temps.

### Exemple d'utilisation :

Une fois la fonction définie, appelez-la avec l'UID d'un utilisateur :

```js
setUserRole("USER_UID_HERE", "admin");
```

Cela attache de manière sécurisée une custom claim à l'utilisateur.

**Note :** L'utilisateur doit se déconnecter et se reconnecter (ou rafraîchir son jeton) pour que la nouvelle claim soit prise en compte.

## Étape 3 : Écrire des règles de sécurité Firestore pour le RBAC

Les `Security Rules` de Firestore contrôlent la manière dont vos données peuvent être lues ou écrites. Elles sont exécutées **avant** que toute requête client n'atteigne votre base de données, garantissant que votre logique de sécurité ne soit pas contournée.

Ouvrez vos règles Firestore (`firestore.rules`) et définissez l'accès basé sur les rôles comme ceci :

![image montrant la section des règles firebase](https://cdn.hashnode.com/res/hashnode/image/upload/v1760234391658/9e9cf217-6291-4189-a135-8310c8905587.png align="center")

```js
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    
    match /posts/{postId} {
      // Toute personne connectée peut lire
      allow read: if request.auth != null;

      // Seuls les admins peuvent écrire
      allow write: if request.auth.token.role == "admin";
    }
  }
}
```

Voici ce qui se passe :

* `request.auth != null` : garantit que l'utilisateur est connecté.
    
* `request.auth.token.role == "admin"` : accorde l'accès en écriture uniquement aux utilisateurs ayant le rôle admin.
    

Vous pouvez étendre cela pour plusieurs rôles :

```js
allow write: if request.auth.token.role in ["admin", "editor"];
```

## Référence rapide

Gardez ces points à l'esprit lors de la gestion du RBAC Firebase :

* **Gardez vos rôles simples** (par exemple, `admin`, `editor`, `user`). Ne compliquez pas trop.
    
* **Ne stockez pas les rôles dans les documents Firestore**. Appliquez-les via des custom claims à la place.
    
* **Testez toujours les règles** localement avant de les déployer.
    
* N'oubliez pas que les utilisateurs doivent **rafraîchir leurs jetons** après la mise à jour des claims.
    

## Étape 4 : Construire le Frontend avec Next.js et Firebase

Donnons vie à cela avec une [démo fonctionnelle](https://github.com/CodeLeom/firebase-rbac) utilisant Next.js et Firebase.

```bash
firebase-rbac/
├── firebase-admin-scripts/       # Scripts côté serveur pour définir les rôles
│   ├── assignRole.js             # Utilise le SDK Firebase Admin pour attribuer des claims
│   ├── .env                      # Contient le chemin du compte de service et l'UID de test
│   └── fir-rbac-...json          # Fichier JSON du compte de service SDK Firebase Admin
│
├── src/
│   ├── app/
│   │   ├── page.js               # Page principale Next.js pour login + affichage des posts
│   │   ├── layout.js             # Mise en page globale
│   │   └── globals.css           # Styles globaux Tailwind
│   └── lib/
│       └── firebase.js           # Initialisation du client Firebase
│
├── .env.local                    # Configuration web Firebase (variables NEXT_PUBLIC_)
├── package.json
└── README.md
```

Dans votre fichier `.env.local`, complétez ces variables avec les informations de configuration de votre projet Firebase :

```bash
NEXT_PUBLIC_FIREBASE_API_KEY=votre-cle-api
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=votre-id-projet.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=votre-id-projet
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=votre-id-projet.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=votre-id-expediteur
NEXT_PUBLIC_FIREBASE_APP_ID=votre-id-app
```

Initialisation de Firebase (src/lib/firebase.js) :

```javascript
import { initializeApp, getApps, getApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
```

Composant de démo (src/app/page.js) :

Ce composant vous permet de vous connecter, de voir les posts et, si vous êtes admin, d'en créer de nouveaux.

```javascript
"use client";

import { useState, useEffect } from "react";
import { auth, db } from "@/lib/firebase";
import {
  signInWithEmailAndPassword,
  onAuthStateChanged,
  signOut,
} from "firebase/auth";
import { collection, getDocs, addDoc } from "firebase/firestore";

export default function Page() {
  const [user, setUser] = useState(null);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [posts, setPosts] = useState([]);
  const [newPost, setNewPost] = useState("");

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (u) => {
      setUser(u);
      if (u) await loadPosts();
      else setPosts([]);
    });
    return () => unsubscribe();
  }, []);

  const loadPosts = async () => {
    const snapshot = await getDocs(collection(db, "posts"));
    setPosts(snapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() })));
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      await signInWithEmailAndPassword(auth, email, password);
      alert("Connecté !");
      setEmail("");
      setPassword("");
    } catch (error) {
      console.error("Échec de la connexion :", error.message);
      alert("Échec de la connexion : " + error.message);
    }
  };

  const handleLogout = async () => {
    await signOut(auth);
    setUser(null);
  };

  const handleAddPost = async () => {
    try {
      await addDoc(collection(db, "posts"), { text: newPost });
      setNewPost("");
      await loadPosts();
      alert("Nouveau post ajouté !");
    } catch (e) {
      alert("Oups !! Seuls les admins peuvent ajouter des posts.");
      console.error(e.message);
    }
  };

  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-gray-900 text-gray-100 px-4">
      <div className="w-full max-w-md bg-gray-800 rounded-2xl shadow-lg p-8 space-y-6">
        <h1 className="text-2xl font-bold text-center text-indigo-400">
          Démo Firebase RBAC (Next.js)
        </h1>

        {/* Formulaire de connexion */}
        {!user ? (
          <form onSubmit={handleLogin} className="space-y-4">
            <div>
              <label className="block text-gray-300 text-sm mb-1">Email</label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="vous@exemple.com"
                required
                className="w-full px-3 py-2 rounded-md bg-gray-700 border border-gray-600 text-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-400"
              />
            </div>

            <div>
              <label className="block text-gray-300 text-sm mb-1">
                Mot de passe
              </label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••"
                required
                className="w-full px-3 py-2 rounded-md bg-gray-700 border border-gray-600 text-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-400"
              />
            </div>

            <button
              type="submit"
              className="w-full px-6 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 transition font-medium text-white"
            >
              Se connecter
            </button>
          </form>
        ) : (
          <div className="space-y-6">
            <div className="flex flex-col items-center">
              <p className="text-gray-300 mb-2">
                Connecté en tant que{" "}
                <span className="font-semibold text-indigo-400">
                  {user.email}
                </span>
              </p>
              <button
                onClick={handleLogout}
                className="text-sm text-red-400 hover:text-red-300 underline"
              >
                Se déconnecter
              </button>
            </div>

            <section className="border-t border-gray-700 pt-4">
              <h2 className="text-lg font-semibold text-indigo-300 mb-3">
                Posts
              </h2>

              {posts.length > 0 ? (
                <ul className="space-y-2">
                  {posts.map((p) => (
                    <li
                      key={p.id}
                      className="bg-gray-700 rounded-md px-3 py-2 text-gray-200"
                    >
                      {p.text}
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="text-gray-400 italic">Aucun post pour le moment.</p>
              )}

              <div className="mt-4 flex items-center gap-2">
                <input
                  value={newPost}
                  onChange={(e) => setNewPost(e.target.value)}
                  placeholder="Nouveau post"
                  className="flex-1 px-3 py-2 rounded-md bg-gray-700 border border-gray-600 text-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-400"
                />
                <button
                  onClick={handleAddPost}
                  className="px-4 py-2 rounded-md bg-indigo-600 hover:bg-indigo-500 transition font-medium text-white"
                >
                  Ajouter
                </button>
              </div>
            </section>
          </div>
        )}
      </div>

      <footer className="mt-8 text-gray-500 text-sm">
        Propulsé par Next.js + Firebase | &copy; FreeCodeCamp 2025
      </footer>
    </main>
  );
}
```

## Étape 5 : Tester le flux de travail RBAC

Maintenant que tout est configuré, il est temps de tester l'ensemble du flux de contrôle d'accès basé sur les rôles pour s'assurer que vos règles et vos rôles fonctionnent correctement.

### Activer l'Authentification

Rendez-vous sur votre console Firebase, sélectionnez votre projet et accédez à Authentication puis à l'onglet "Sign-in method". Sélectionnez "Ajouter un nouveau fournisseur". Activez ensuite l'authentification par Email/Mot de passe. Cela vous permettra de créer et de vous connecter avec des utilisateurs de test directement depuis votre application.

![une image de la section authentification sur firebase](https://cdn.hashnode.com/res/hashnode/image/upload/v1760441502551/7ce05b9b-51f2-4704-83ed-1b62bf22ef2c.png align="center")

### Configurer les règles Firestore

Ensuite, vous devrez mettre à jour les règles Firestore. Accédez à Firestore Database, situé dans le menu déroulant "Build". Une fois sur place, cliquez sur l'onglet "Règles" où vous pourrez mettre à jour les règles.

Remplacez les règles par défaut par les règles RBAC que vous avez définies précédemment. Ces règles garantissent que seuls les utilisateurs authentifiés peuvent lire les données, et que seuls les administrateurs peuvent créer ou modifier des posts.

Publiez ensuite la version mise à jour et vous êtes prêt à partir.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1760441655143/9a34a908-0692-4f84-92c4-7526aafdbd51.png align="center")

### Attribuer un rôle à un utilisateur

Pour tester les permissions d'administrateur, attribuez un rôle admin à l'un de vos utilisateurs de test. Ouvrez votre terminal, placez-vous dans le répertoire `firebase-admin-scripts` et exécutez :

```bash
cd firebase-admin-scripts
node assignRole.js
```

Ceci exécute le script du SDK Admin qui ajoute une custom claim à votre utilisateur de test. Une fois le rôle défini, vous recevrez un message confirmant que le rôle `admin` a été attribué à l'ID utilisateur spécifié.

Si l'utilisateur est déjà connecté, il doit se déconnecter et se reconnecter pour que le nouveau rôle soit effectif.

### Lancer l'application

Vous pouvez maintenant démarrer votre serveur de développement Next.js :

```bash
npm run dev
```

Visitez [http://localhost:3000](http://localhost:3000) dans votre navigateur. Vous devriez voir l'application de démo Firebase RBAC.

### Vérifier l'accès basé sur les rôles

Essayez de vous connecter avec l'utilisateur auquel le rôle **admin** a été attribué. Une fois connecté, vous devriez pouvoir créer de nouveaux posts avec succès. Ensuite, connectez-vous en tant qu'utilisateur standard. Vous remarquerez que vous pouvez voir les posts existants, mais toute tentative d'ajout d'un nouveau post échouera avec une alerte "Permission denied".

Si vous observez ces comportements, alors votre système RBAC fonctionne comme prévu !

En appliquant les permissions au niveau de la couche Firestore, vous garantissez que la sécurité est gérée de manière centralisée et ne peut pas être contournée en manipulant le code côté client. Cette approche maintient votre application sécurisée et évolutive, même si vos rôles et vos données deviennent plus complexes.

Étapes suivantes :

* Ajouter plus de rôles (comme éditeur, et d'autres selon vos souhaits).
    
* Combiner le RBAC avec une validation au niveau du document pour un contrôle plus fin.
    
* Explorer les [règles de sécurité](https://firebase.google.com/docs/rules/) de Firebase.
    

## Conclusion

Vous venez d'apprendre une fonctionnalité simple mais cruciale de **contrôle d'accès basé sur les rôles (RBAC)** dans Firebase. Dans ce guide, nous avons couvert les custom claims et comment définir des rôles à l'aide du SDK Admin. Vous avez également appris comment appliquer ces rôles dans les règles de sécurité Firestore.