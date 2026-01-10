---
title: Comment valider des formulaires avec Zod et React-Hook-Form
subtitle: ''
author: Gift Uhiene
co_authors: []
series: null
date: '2024-01-17T21:58:56.000Z'
originalURL: https://freecodecamp.org/news/react-form-validation-zod-react-hook-form
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Frame-7.png
tags:
- name: forms
  slug: forms
- name: React
  slug: react
- name: zod
  slug: zod
seo_title: Comment valider des formulaires avec Zod et React-Hook-Form
seo_desc: "Forms allow you to collect user data on your websites and apps. And validation\
  \ is essential to guarantee type safety and the proper format for collected data.\
  \ You can perform validation on both the client and server side of the application.\
  \ \nThis is ..."
---

Les formulaires permettent de collecter des données utilisateur sur vos sites web et applications. Et la validation est essentielle pour garantir la sécurité des types et le bon format des données collectées. Vous pouvez effectuer la validation à la fois sur le côté client et serveur de l'application.

C'est là que Zod et React-Hook-Form entrent en jeu en tant que duo dynamique, prêts à faire passer vos formulaires au niveau supérieur.

[Zod](https://zod.dev/) est une bibliothèque de validation qui fournit une syntaxe concise et expressive pour définir des schémas de données, ce qui en fait un excellent choix pour valider les données de formulaire.

D'autre part, [React-Hook-Form](https://react-hook-form.com/) est une bibliothèque de formulaires légère pour React qui adopte des composants non contrôlés et simplifie la construction de formulaires avec son API intuitive basée sur les hooks.

Dans ce tutoriel, vous apprendrez à construire un formulaire sécurisé en utilisant React-Hook-Form pour la gestion des formulaires et Zod pour la validation côté client et côté serveur.

### Voici ce que nous allons couvrir :

1. [Prise en main](#heading-installation)
2. [Comment définir les types de formulaire](#heading-comment-definir-les-types-de-formulaire)
3. [Comment créer un formulaire avec react-hook-form](#heading-comment-creer-un-formulaire-avec-react-hook-form)
4. [Comment intégrer Zod pour la validation de schéma](#heading-comment-integrer-zod-pour-la-validation-de-schema)
5. [Comment gérer les erreurs côté serveur](#heading-comment-gerer-les-erreurs-cote-serveur)
6. [Conclusion](#heading-conclusion)

## Prise en main

Pour commencer, clonez le modèle de départ pour le projet. Ouvrez votre terminal et exécutez cette commande :

```bash
git clone --branch starter https://github.com/Giftea/zod-rhf-fcc.git
```

Vous pouvez trouver la version finale sur GitHub [ici](https://github.com/Giftea/zod-rhf-fcc).

Une fois que vous avez le modèle sur votre machine locale, exécutez les commandes suivantes pour installer les dépendances et démarrer le projet :

```bash
npm install
npm run dev

```

Pointez votre navigateur vers [http://localhost:3000](http://localhost:3000), et vous serez accueilli par la page de départ de notre projet.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-16-at-15.21.10.png)
_localhost_

## Comment définir les types de formulaire

Le fichier `/types.ts` contiendra les types et schémas liés à nos champs de formulaire et à leur validation. Mettez à jour le fichier `/types.ts` avec le code ci-dessous :

```typescript
import { FieldError, UseFormRegister } from "react-hook-form";

export type FormData = {
    email: string;
    githubUrl: string;
    yearsOfExperience: number;
    password: string;
    confirmPassword: string;
  };

  export type FormFieldProps = {
    type: string;
    placeholder: string;
    name: ValidFieldNames;
    register: UseFormRegister<FormData>;
    error: FieldError | undefined;
    valueAsNumber?: boolean;
  };
  

  export type ValidFieldNames =
  | "email"
  | "githubUrl"
  | "yearsOfExperience"
  | "password"
  | "confirmPassword";
```

`FormData` représente la structure des données attendues dans le formulaire.

`FormFieldProps` définit les propriétés attendues par le composant de champ de formulaire (que nous construirons plus tard). Il inclut :

* `type` : Le type du champ de saisie (par exemple, texte, mot de passe).
* `placeholder` : Texte de l'espace réservé pour le champ de saisie.
* `name` : Le nom du champ, qui correspond à l'un des noms de champ valides définis dans le type `ValidFieldNames`.
* `register` : Une fonction de `react-hook-form` (`UseFormRegister<FormData>`) utilisée pour enregistrer le champ de saisie avec le formulaire.
* `error` : Représente toute erreur de validation associée au champ. Il peut être `undefined` s'il n'y a pas d'erreurs.
* `valueAsNumber` (optionnel) : Un indicateur booléen indiquant si la valeur du champ doit être traitée comme un nombre. Par défaut, `undefined`.

`ValidFieldNames` est un type d'union qui énumère les noms de champ valides pour le formulaire. Ceux-ci correspondent aux champs définis dans le type `FormData`.

## Comment créer un formulaire avec React-Hook-Form

Maintenant que nous avons défini les types pour le formulaire, créons un composant de champ de formulaire réutilisable et le composant de formulaire.

### Créer un composant de champ de formulaire réutilisable

Créons un composant `FormField` réutilisable qui gère le rendu d'un élément d'entrée, l'enregistre avec le formulaire en utilisant `react-hook-form`, et affiche un message d'erreur de validation lorsque cela est nécessaire.

Rendez-vous dans le fichier `/app/components/FormField.tsx` et mettez à jour le composant :

```tsx
import { FormFieldProps } from "@/types";

const FormField: React.FC<FormFieldProps> = ({
  type,
  placeholder,
  name,
  register,
  error,
  valueAsNumber,
}) => (
  <>
    <input
      type={type}
      placeholder={placeholder}
      {...register(name, { valueAsNumber })}
    />
    {error && <span className="error-message">{error.message}</span>}
  </>
);
export default FormField;

```

#### Imports :

* Le composant importe le type `FormFieldProps` du module `@/types`. Ce type contient les propriétés attendues pour un champ de formulaire, telles que `type`, `placeholder`, `name`, `register`, `error`, et `valueAsNumber`.

#### Élément d'entrée :

* Le composant rend un élément `<input>` avec des attributs définis en fonction des props fournies (`type`, `placeholder`, `name`).
* La syntaxe `...register(name, { valueAsNumber })` est utilisée pour enregistrer le champ de saisie avec le formulaire, permettant la gestion de l'état du formulaire.

#### Gestion des erreurs :

* Si une erreur de validation est présente, un élément `<span>` est rendu, affichant le message d'erreur.

### Créer le composant de formulaire

Le composant `Form` utilisera la bibliothèque `react-hook-form` pour gérer l'état du formulaire. Il modularise les champs de formulaire en utilisant notre composant `FormField` réutilisable.

Accédez à `app/components/Form.tsx` et mettez-le à jour avec le code ci-dessous :

```tsx
import { useForm } from "react-hook-form";
import { FormData } from "@/types";
import FormField from "./FormField";

function Form() {
  const {
    register,
    handleSubmit,
    formState: { errors },
    setError,
  } = useForm<FormData>();
  
  const onSubmit = async (data: FormData) => {
  	console.log("SUCCESS", data);
  }

  return (
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="grid col-auto">
          <h1 className="text-3xl font-bold mb-4">
            Zod & React-Hook-Form
          </h1>
          <FormField
            type="email"
            placeholder="Email"
            name="email"
            register={register}
            error={errors.email}
          />

          <FormField
            type="text"
            placeholder="GitHub URL"
            name="githubUrl"
            register={register}
            error={errors.githubUrl}
          />

          <FormField
            type="number"
            placeholder="Années d'expérience (1 - 10)"
            name="yearsOfExperience"
            register={register}
            error={errors.yearsOfExperience}
            valueAsNumber
          />

          <FormField
            type="password"
            placeholder="Mot de passe"
            name="password"
            register={register}
            error={errors.password}
          />

          <FormField
            type="password"
            placeholder="Confirmer le mot de passe"
            name="confirmPassword"
            register={register}
            error={errors.confirmPassword}
          />
          <button type="submit" className="submit-button">
            Soumettre
          </button>
        </div>
      </form>
  );
}

export default Form;
```

#### Imports :

* Le hook `useForm` fournit des fonctionnalités pour gérer l'état et la validation du formulaire.
* `FormData` représente la structure des données du formulaire.
* `FormField` est notre composant de champ de formulaire réutilisable.

#### Composant de formulaire :

* Les fonctions et variables d'état liées au formulaire sont déstructurées à partir du hook `useForm`, qui est explicitement typé avec `FormData` pour définir la forme des données du formulaire.
* Dans le formulaire, les composants `FormField` sont rendus pour différents champs de saisie tels que l'email, l'URL GitHub, les années d'expérience, le mot de passe et la confirmation du mot de passe.

#### Exécuter le code :

Importez le composant `Form` dans le fichier `/app/page.tsx` :

```tsx
"use client";
import Form from "./components/Form";

function Home() {
 
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
     <Form />
    </main>
  );
}

export default Home;
```

Visitez [http://localhost:3000/](http://localhost:3000/) pour voir le formulaire :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-11-at-11.40.22.png)
_[http://localhost:3000/](http://localhost:3000/)_

En résumé, notre composant `Form` est une structure de formulaire basique qui utilise la bibliothèque `react-hook-form` pour la gestion de l'état et emploie un composant `FormField` réutilisable pour gérer le rendu et la validation des champs de formulaire individuels.

## Comment intégrer Zod pour la validation de schéma

Zod se distingue comme une bibliothèque de déclaration et de validation de schéma, avec TypeScript comme principal focus. Le terme "schéma" englobe divers types de données, allant des chaînes de caractères, des nombres et des booléens à des objets plus complexes.

### Définir un schéma de formulaire avec Zod

Créons un schéma de formulaire soutenu par TypeScript en utilisant Zod pour notre structure de formulaire.

Rendez-vous dans votre fichier `/types.ts`, ajoutez les nouvelles imports et créez un schéma utilisateur avec le code ci-dessous :

```ts
 import { z, ZodType } from "zod"; // Ajouter une nouvelle import
 
 export const UserSchema: ZodType<FormData> = z
  .object({
    email: z.string().email(),
    githubUrl: z
      .string()
      .url()
      .includes("github.com", { message: "URL GitHub invalide" }),
    yearsOfExperience: z
      .number({
        required_error: "champ requis",
        invalid_type_error: "Les années d'expérience sont requises",
      })
      .min(1)
      .max(10),
    password: z
      .string()
      .min(8, { message: "Le mot de passe est trop court" })
      .max(20, { message: "Le mot de passe est trop long" }),
    confirmPassword: z.string(),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: "Les mots de passe ne correspondent pas",
    path: ["confirmPassword"], // chemin de l'erreur
  });
```

#### Imports :

* `z` est une instance de l'objet Zod.
* `ZodType` est un type générique qui représente un type de schéma Zod pour une structure de données spécifique.

#### Schéma utilisateur :

* `export const UserSchema: ZodType<FormData> = ...` : Le `UserSchema` représente un type Zod qui correspond à la structure définie par le type `FormData`.
* `z.object({...})` : Cette partie définit un schéma d'objet en utilisant Zod. L'objet a plusieurs champs, chacun avec ses propres règles de validation.
* À l'intérieur de l'objet, chaque champ est défini avec ses propres règles de validation en utilisant des méthodes Zod comme `z.string()`, `z.url()`, `z.number()`, et `z.min()`. Des messages d'erreur personnalisés optionnels sont fournis pour certains des champs.
* `z.refine((data) => data.password === data.confirmPassword, { /* ... */ });` : Ajoute un raffinement au schéma pour vérifier si les champs `password` et `confirmPassword` correspondent. Si ce n'est pas le cas, un message d'erreur personnalisé est fourni, et l'erreur est associée au champ `confirmPassword`.

### Comment intégrer Zod avec React-Hook-Form pour la validation

Maintenant que nous avons configuré le schéma Zod pour le formulaire, intégrons-le avec notre composant Form existant. Pour ce faire, nous utiliserons `zodResolver` de la bibliothèque `[@hookform](https://www.npmjs.com/package/@hookform/resolvers)`.

`zodResolver` est une fonction de résolution qui intègre la validation du schéma Zod avec le processus de validation du formulaire.

Rendez-vous dans le fichier `app/components/Form.tsx` et mettez-le à jour avec le code ci-dessous :

```tsx
// Mettre à jour les imports
import { FormData, UserSchema } from "@/types";
import { zodResolver } from "@hookform/resolvers/zod";

function Form() {
  const {
    register,
    handleSubmit,
    formState: { errors },
    setError,
  } = useForm<FormData>({
    resolver: zodResolver(UserSchema), // Appliquer le zodResolver
  });

{/* Code existant... */}

}
```

Si vous essayez de soumettre le formulaire avec des champs de saisie vides, vous verrez des messages d'erreur dans le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-11-at-20.38.03.png)
_Messages d'erreur - http://localhost:3000/_

De plus, nos messages d'erreur personnalisés, tels que demander aux utilisateurs de fournir une URL GitHub valide et vérifier si les mots de passe correspondent, sont démontrés dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-11-at-20.59.18.png)
_Messages d'erreur personnalisés - http://localhost:3000/_

## Comment gérer les erreurs côté serveur

Lors de la création de formulaires, l'intégrité des données et la sécurité des types sont très importantes, étant donné que les données soumises vont au serveur du site web. Cela nous amène à l'importance de la gestion des erreurs côté serveur, une mesure de sécurité supplémentaire pour s'assurer que les données du client sont exactes et non malveillantes.

### Comment implémenter la validation côté serveur

Pour implémenter la validation côté serveur, nous allons exploiter les capacités backend de Next.js pour construire un serveur simple. Ce serveur recevra et validera les données soumises via notre formulaire.

Accédez à `app/api/form/route.ts` et incluez le code ci-dessous :

```ts
import { UserSchema } from "@/types";
import { NextResponse } from "next/server";

export async function POST(request: Request) {
  // Récupérer les données JSON du corps de la requête
  const body = await request.json();

  // Utiliser Zod pour valider les données reçues contre le UserSchema
  const result = UserSchema.safeParse(body);

  // Vérifier si la validation est réussie
  if (result.success) {
    return NextResponse.json({ success: true });
  }

  // Si des erreurs de validation, les mapper dans un objet
  const serverErrors = Object.fromEntries(
    result.error?.issues?.map((issue) => [issue.path[0], issue.message]) || []
  );

  // Répondre avec un objet JSON contenant les erreurs de validation
  return NextResponse.json({ errors: serverErrors });
}
```

#### Imports :

* Le `UserSchema` que nous avons défini précédemment est importé.
* `NextResponse` du module `next/server`, qui nous permet de créer des réponses serveur dans un environnement Next.js.

#### Fonction POST :

* `const body = await request.json()` : Récupère les données JSON du corps de la requête et les stocke dans la variable `body`.
* `const result = UserSchema.safeParse(body)` : Utilise la méthode `safeParse` fournie par Zod pour valider les données reçues contre le `UserSchema`. Le résultat contient des informations sur le fait que la validation a réussi et, si ce n'est pas le cas, des détails sur les problèmes de validation.
* `if (result.success) { return NextResponse.json({ success: true }); }` : Si la validation est réussie, une réponse JSON avec `{ success: true }` est envoyée.
* `const serverErrors = Object.fromEntries(/* ... */)` : Si des erreurs de validation sont présentes, le code les mappe dans un objet avec les noms de champs et les messages d'erreur correspondants.
* `return NextResponse.json({ errors: serverErrors })` : Répond avec un objet JSON contenant les erreurs de validation.

Dans votre terminal, arrêtez l'exécution du projet et exécutez `npm run dev` à nouveau pour redémarrer le serveur.

### Comment intégrer la validation côté serveur

Pour intégrer la validation côté serveur, nous devons mettre à jour la fonction `onSubmit` dans le composant Form.

Rendez-vous dans le fichier `/app/components/Form.tsx` et mettez à jour les imports et la fonction `onSubmit` :

```tsx
// Mettre à jour l'import
import { FormData, UserSchema, ValidFieldNames } from "@/types";  
import axios from "axios";

function Form() {
{/* Code existant... */}

  const onSubmit = async (data: FormData) => {
    try {
      const response = await axios.post("/api/form", data); // Faire une requête POST
      const { errors = {} } = response.data; // Déstructurer la propriété 'errors' des données de réponse

      // Définir une correspondance entre les noms de champs côté serveur et leurs noms correspondants côté client
      const fieldErrorMapping: Record<string, ValidFieldNames> = {
        email: "email",
        githubUrl: "githubUrl",
        yearsOfExperience: "yearsOfExperience",
        password: "password",
        confirmPassword: "confirmPassword",
      };

      // Trouver le premier champ avec une erreur dans les données de réponse
      const fieldWithError = Object.keys(fieldErrorMapping).find(
        (field) => errors[field]
      );

      // Si un champ avec une erreur est trouvé, mettre à jour l'état d'erreur du formulaire en utilisant setError
      if (fieldWithError) {
        // Utiliser le type ValidFieldNames pour s'assurer des noms de champs corrects
        setError(fieldErrorMapping[fieldWithError], {
          type: "server",
          message: errors[fieldWithError],
        });
      }
    } catch (error) {
      alert("La soumission du formulaire a échoué !");
    }
  };
{/* Code existant... */}
}
```

* `axios` est utilisé pour faire une requête POST à l'endpoint du serveur `/api/form` avec les données du formulaire.
* L'objet `errors` est extrait des données de réponse.
* Une correspondance (`fieldErrorMapping`) entre les noms de champs et leurs `ValidFieldNames` correspondants est définie.
* Il vérifie ensuite s'il y a des erreurs liées aux champs de formulaire en itérant sur `fieldErrorMapping` et en trouvant le premier champ avec une erreur.
* Si un champ avec une erreur est trouvé, la fonction `setError` de `react-hook-form` est utilisée pour définir une erreur pour le champ correspondant. Le type d'erreur est marqué comme "server", et le message d'erreur provient de la réponse du serveur.
* Si une erreur survient dans l'ensemble du bloc try, elle est capturée et une alerte est affichée : "La soumission du formulaire a échoué !"

Maintenant, pour tester si nous pouvons recevoir des erreurs du serveur, nous allons délibérément envoyer des données mal formatées au serveur. Dans votre fonction `onSubmit`, remplacez l'objet `data` par les données incorrectes dans le bloc de code ci-dessous :

```tsx

{/* Code existant... */}
  const onSubmit = async (data: FormData) => {
 
    try {
      // Mettre à jour les données envoyées dans axios avec des données incorrectes
      const response = await axios.post("/api/form", {
        email: "Not an email",
        githubUrl: "Not a URL",
        yearsOfExperience: "Hello",
        password: 1234,
        confirmPassword: 1234,
      }); // Faire une requête POST
      
{/* Code existant... */}
}
```

Remplissez le formulaire dans le navigateur normalement et soumettez le formulaire.

Inspectez l'onglet "Network" dans les outils de développement du navigateur. Vous trouverez des messages d'erreur provenant directement du serveur, comme démontré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-10.21.47.png)
_Erreurs serveur - http://localhost:3000/_

Si vous ne recevez aucune réponse de votre serveur, n'oubliez pas d'arrêter l'exécution de votre projet dans votre terminal et d'exécuter `npm run dev` à nouveau pour redémarrer le serveur.

## Conclusion

Dans ce tutoriel, nous avons construit un formulaire avec React-Hook-Form et l'avons validé avec Zod. Avec Zod, nous avons exploré la validation de schéma, les messages d'erreur personnalisés et les erreurs côté serveur. L'intégration de React-Hook-Form et Zod présente une solution puissante et conviviale pour créer des formulaires résilients.

Vous pouvez me contacter sur [Twitter](https://twitter.com/dev_giftea) si vous avez des questions.

Vous pouvez consulter le [code source](https://github.com/Giftea/zod-rhf-fcc) et l'application déployée [ici](https://zod-rhf-fcc.vercel.app/).

### Ressources :

* [Documentation Zod](https://zod.dev/)
* [Gestion des erreurs Zod](https://zod.dev/ERROR_HANDLING?id=error-handling-in-zod)
* [Documentation React-Hook-Form](https://react-hook-form.com/get-started)
* [Hookform Resolvers](https://www.npmjs.com/package/@hookform/resolvers)