---
title: Comment authentifier vos APIs Elixir/Phoenix en utilisant Guardian
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-19T19:13:09.000Z'
originalURL: https://freecodecamp.org/news/authentication-using-elixir-phoenix-f9c162b2c398
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kK_wSy_F4xp77Uj8aSFkeQ.jpeg
tags:
- name: api
  slug: api
- name: Elixir
  slug: elixir
- name: Phoenix framework
  slug: phoenix
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment authentifier vos APIs Elixir/Phoenix en utilisant Guardian
seo_desc: 'By Nirmalya Ghosh

  Authentication is always a tricky subject. People tend to use so many types of authentication
  in their apps. Authentication using an email address and a password with an option
  confirm password field is the most common. But every ti...'
---

Par Nirmalya Ghosh

L'authentification est toujours un sujet délicat. Les gens ont tendance à utiliser tant de types d'authentification dans leurs applications. L'authentification utilisant une adresse e-mail et un mot de passe avec une option de confirmation du mot de passe est la plus courante. Mais chaque fois que vous voyez un formulaire d'inscription, vous vous ennuyez en pensant que vous devrez taper autant de choses juste pour vous inscrire ! Où est le plaisir dans tout ça !

Donc, pour cette application, je vais faire l'authentification en utilisant votre compte Google. C'est assez simple. Vous devez simplement cliquer sur un bouton, donner à l'application les autorisations nécessaires pour accéder à votre profil Google de base et vous êtes prêt ! Cool, non ?

Nous allons utiliser [Ueberauth](https://github.com/ueberauth/ueberauth), [Ueberauth Google](https://github.com/ueberauth/ueberauth_google) et [Guardian](https://github.com/ueberauth/guardian) pour authentifier notre utilisateur. Ueberauth et Ueberauth Google aideront à authentifier l'utilisateur avec leurs identifiants Google. Guardian nous aidera à générer un JSON Web Token pour les utilisateurs connectés. Ce token est nécessaire et doit être dans l'en-tête de chaque requête pour toute route nécessitant une authentification.

Guardian vérifiera ce token dans l'en-tête des requêtes et si le token est valide, les routes authentifiées seront disponibles pour l'utilisateur. Je vais expliquer ces choses en détail.

Si vous n'avez pas déjà installé [Phoenix](http://www.phoenixframework.org) et ses dépendances nécessaires, vous pouvez vous rendre sur les [Guides Phoenix](http://www.phoenixframework.org/docs/installation) pour installer et démarrer.

Pour commencer, ajoutez les dépendances à notre `mix.exs`.

```
defp deps do  [   ...      {:ueberauth, "~> 0.4"},   {:ueberauth_google, "~> 0.2"},   {:ja_serializer, "~> 0.11.2"},   {:guardian, "~> 0.14.2"}]end
```

Après cela, exécutez `mix deps.get` pour récupérer les dépendances.

Vous devez également ajouter `ueberauth` et `ueberauth_google` à notre application dans `mix.exs`.

```
def application do  [mod: {SocialAppApi, []},   applications: [   ...      :ueberauth, :ueberauth_google]]end
```

Maintenant, vous devrez ajouter votre configuration `ueberauth`, `ueberauth_google` et `guardian` à votre fichier `config/config.exs`.

```
# Config Ueberauth pour oauthconfig :ueberauth, Ueberauth,  base_path: "/api/v1/auth",  providers: [    google: { Ueberauth.Strategy.Google, [] },    identity: { Ueberauth.Strategy.Identity, [        callback_methods: ["POST"],        uid_field: :username,        nickname_field: :username,      ] },  ]
```

```
# Config Ueberauth Strategy pour Google oauthconfig :ueberauth, Ueberauth.Strategy.Google.OAuth,  client_id: System.get_env("GOOGLE_CLIENT_ID"),  client_secret: System.get_env("GOOGLE_CLIENT_SECRET"),  redirect_uri: System.get_env("GOOGLE_REDIRECT_URI")
```

```
# Configuration Guardianconfig :guardian, Guardian,  allowed_algos: ["HS512"], # optionnel  verify_module: Guardian.JWT,  # optionnel  issuer: "SocialAppApi",  ttl: { 30, :days },  allowed_drift: 2000,  verify_issuer: true, # optionnel  secret_key: System.get_env("GUARDIAN_SECRET") || "rFtDNsugNi8jNJLOfvcN4jVyS/V7Sh+9pBtc/J30W8h4MYTcbiLYf/8CEVfdgU6/",  serializer: SocialAppApi.GuardianSerializer
```

Comme vous pouvez le voir ici, j'ai utilisé `System.get_env()`. C'est une façon de stocker les identifiants dans votre application que vous ne voulez pas faire partie de votre base de code. Vous pouvez créer un fichier `.env` et stocker tous ces identifiants comme suit :

```
export DB_NAME_PROD="social_app_api_db"export DB_PASSWORD_PROD="password"export DB_USERNAME_PROD="password"
```

Après cela, vous devez faire `source .env` et ensuite, vous pouvez les utiliser dans votre application.

Maintenant, nous devons faire un tas de choses avec nos contrôleurs qui permettront à l'utilisateur de s'inscrire ou de se connecter.

Tout d'abord, créez un nouveau fichier `web/controllers/auth_controller.ex`.

```
defmodule SocialAppApi.AuthController do  use SocialAppApi.Web, :controller  plug Ueberauth
```

```
  alias SocialAppApi.User  alias MyApp.UserQuery
```

```
  plug :scrub_params, "user" when action in [:sign_in_user]
```

```
  def request(_params) do  end
```

```
  def delete(conn, _params) do    # Déconnecter l'utilisateur    conn    |> put_status(200)    |> Guardian.Plug.sign_out(conn)  end
```

```
  def callback(%{assigns: %{ueberauth_failure: _fails}} = conn, _params) do    # Ce callback est appelé lorsque l'utilisateur refuse que l'application obtienne les données du fournisseur oauth    conn    |> put_status(401)    |> render(SocialAppApi.ErrorView, "401.json-api")  end
```

```
  def callback(%{assigns: %{ueberauth_auth: auth}} = conn, _params) do    case AuthUser.basic_info(auth) do      {:ok, user} ->        sign_in_user(conn, %{"user" => user})    end
```

```
  case AuthUser.basic_info(auth) do      {:ok, user} ->        conn        |> render(SocialAppApi.UserView, "show.json-api", %{data: user})      {:error} ->        conn        |> put_status(401)        |> render(SocialAppApi.ErrorView, "401.json-api")    end  end
```

```
  def sign_in_user(conn, %{"user" => user}) do    try do      # Tentative de récupérer exactement un utilisateur de la base de données, dont      # l'email correspond à celui fourni avec la requête de connexion      user = User      |> where(email: ^user.email)      |> Repo.one!
```

```
      cond do        true ->          # Connexion réussie          # Encoder un JWT          { :ok, jwt, _ } = Guardian.encode_and_sign(user, :token)
```

```
          auth_conn = Guardian.Plug.api_sign_in(conn, user)          jwt = Guardian.Plug.current_token(auth_conn)          {:ok, claims} = Guardian.Plug.claims(auth_conn)
```

```
          auth_conn          |> put_resp_header("authorization", "Bearer #{jwt}")          |> json(%{access_token: jwt}) # Retourner le token au client
```

```
        false ->          # Connexion échouée          conn          |> put_status(401)          |> render(SocialAppApi.ErrorView, "401.json-api")      end    rescue      e ->        IO.inspect e # Afficher l'erreur dans la console pour le débogage
```

```
        # Inscription réussie        sign_up_user(conn, %{"user" => user})    end  end
```

```
  def sign_up_user(conn, %{"user" => user}) do    changeset = User.changeset %User{}, %{email: user.email,      avatar: user.avatar,      first_name: user.first_name,      last_name: user.last_name,      auth_provider: "google"}
```

```
    case Repo.insert changeset do      {:ok, user} ->        # Encoder un JWT        { :ok, jwt, _ } = Guardian.encode_and_sign(user, :token)
```

```
        conn        |> put_resp_header("authorization", "Bearer #{jwt}")        |> json(%{access_token: jwt}) # Retourner le token au client      {:error, changeset} ->        conn        |> put_status(422)        |> render(SocialAppApi.ErrorView, "422.json-api")    end  end
```

```
  def unauthenticated(conn, params) do    conn    |> put_status(401)    |> render(SocialAppApi.ErrorView, "401.json-api")  end
```

```
  def unauthorized(conn, params) do    conn    |> put_status(403)    |> render(SocialAppApi.ErrorView, "403.json-api")  end
```

```
  def already_authenticated(conn, params) do    conn    |> put_status(200)    |> render(SocialAppApi.ErrorView, "200.json-api")  end
```

```
  def no_resource(conn, params) do    conn    |> put_status(404)    |> render(SocialAppApi.ErrorView, "404.json-api")  endend
```

Ici, `sign_in_user` connectera l'utilisateur et renverra un `access_token` en réponse. Le `sign_up_user` inscrira l'utilisateur en utilisant leurs identifiants Google et renverra ensuite un `access_token` en réponse. Ce token est essentiel car Guardian vérifiera ce `access_token` dans l'en-tête de toutes les requêtes. Il vérifiera si l'utilisateur est actuellement en session ou non. Si oui, toutes les routes authentifiées seront disponibles pour l'utilisateur. Sinon, il recevra une réponse `401` pour les routes authentifiées.

Ajoutons quelques routes à notre application. Notre fichier `router.ex` ressemble à ceci :

```
defmodule SocialAppApi.Router do  use SocialAppApi.Web, :router
```

```
  pipeline :api do    plug :accepts, ["json", "json-api"]    plug JaSerializer.Deserializer  end
```

```
  pipeline :api_auth do    plug :accepts, ["json", "json-api"]    plug Guardian.Plug.VerifyHeader, realm: "Bearer"    plug Guardian.Plug.LoadResource    plug JaSerializer.Deserializer  end
```

```
  scope "/api/v1", SocialAppApi do    pipe_through :api_auth
```

```
  resources "/users", UserController, except: [:new, :edit]    get "/user/current", UserController, :current, as: :current_user    delete "/logout", AuthController, :delete  end
```

```
  scope "/api/v1/auth", SocialAppApi do    pipe_through :api
```

```
    get "/:provider", AuthController, :request    get "/:provider/callback", AuthController, :callback    post "/:provider/callback", AuthController, :callback  endend
```

Ici, le pipeline `api_auth` est celui qui est authentifié. Le pipeline `api` ne l'est pas. Donc, nous pouvons visiter `get "/:provider", AuthController, :request` sans nous connecter.

Créez un autre fichier appelé `web/models/auth_user.ex` avec le code suivant :

```
defmodule AuthUser do  alias Ueberauth.Auth
```

```
  def basic_info(%Auth{} = auth) do    {:ok,      %{        avatar: auth.info.image,        email: auth.info.email,        first_name: auth.info.first_name,        last_name: auth.info.last_name      }    }  endend
```

Vous devrez également créer un modèle `User`.

```
mix phoenix.gen.json User users email:string auth_provider:string first_name:string last_name:string avatar:string
```

Cela générera votre modèle et migration nécessaires.

Votre modèle ressemblera à quelque chose comme ceci :

```
defmodule SocialAppApi.User do  use SocialAppApi.Web, :model
```

```
  schema "users" do    field :email, :string    field :auth_provider, :string    field :first_name, :string    field :last_name, :string    field :avatar, :string
```

```
    timestamps()  end
```

```
  def changeset(struct, params \\ %{}) do    struct    |> cast(params, [:email, :auth_provider, :first_name, :last_name, :avatar])    |> validate_required([:email, :auth_provider, :first_name, :last_name, :avatar])    |> unique_constraint(:email)  endend
```

Votre fichier de migration ressemblera à quelque chose comme ceci :

```
defmodule SocialAppApi.Repo.Migrations.CreateUser do  use Ecto.Migration
```

```
  def change do    create table(:users) do      add :email, :string      add :auth_provider, :string      add :first_name, :string      add :last_name, :string      add :avatar, :string
```

```
      timestamps()    end
```

```
    # Contrainte d'adresse e-mail unique, via l'index DB    create index(:users, [:email], unique: true)  endend
```

Maintenant, exécutez la migration.

```
mix ecto.migrate
```

Créez également un `UserController` pour notre modèle `user`. Il contiendra le code suivant :

```
defmodule SocialAppApi.UserController do  use SocialAppApi.Web, :controller
```

```
  alias SocialAppApi.User
```

```
  plug Guardian.Plug.EnsureAuthenticated, handler:     SocialAppApi.AuthController
```

```
  def index(conn, _params) do    users = Repo.all(User)    render(conn, "index.json-api", data: users)  end
```

```
  def current(conn, _) do    user = conn    |> Guardian.Plug.current_resource
```

```
    conn    |> render(SocialAppApi.UserView, "show.json-api", data: user)  endend
```

Cela est utile si vous voulez vérifier si les routes authentifiées fonctionnent ou non après tout votre travail acharné.

Créez deux autres vues dans `web/views/error_view.ex` avec le code suivant :

```
defmodule SocialAppApi.ErrorView do  use SocialAppApi.Web, :view  use JaSerializer.PhoenixView
```

```
  def render("401.json-api", _assigns) do    %{title: "Non autorisé", code: 401}    |> JaSerializer.ErrorSerializer.format  end
```

```
  def render("403.json-api", _assigns) do    %{title: "Interdit", code: 403}    |> JaSerializer.ErrorSerializer.format  end
```

```
  def render("404.json-api", _assigns) do    %{title: "Page non trouvée", code: 404}    |> JaSerializer.ErrorSerializer.format  end
```

```
  def render("422.json-api", _assigns) do    %{title: "Entité non traitée", code: 422}    |> JaSerializer.ErrorSerializer.format  end
```

```
  def render("500.json-api", _assigns) do    %{title: "Erreur interne du serveur", code: 500}    |> JaSerializer.ErrorSerializer.format  end
```

```
  # Au cas où aucune clause de rendu ne correspond ou aucun  # modèle n'est trouvé, rendons-le comme 500  def template_not_found(_template, assigns) do    render "500.json-api", assigns  endend
```

Créez également une autre vue `web/views/user_view.ex` avec le code suivant :

```
defmodule SocialAppApi.UserView do  use SocialAppApi.Web, :view  use JaSerializer.PhoenixView
```

```
  attributes [:avatar, :email, :first_name, :last_name, :auth_provider]end
```

Et vous êtes prêt. Lancez votre serveur :

```
mix phoenix.server
```

Maintenant, allez sur [http://localhost:4000/api/v1/auth/google](http://localhost:4000/api/v1/auth/google) et vous serez redirigé vers la page de connexion de Google. Une fois que vous avez donné à l'application les autorisations nécessaires, vous recevrez un `access_token` dans la réponse :

```
{  access_token: "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJVc2VyOjIiLCJleHAiOjE0ODk4NjM4MzUsImlhdCI6MTQ4NzI3MTgzNSwiaXNzIjoiU29jaWFsQXBwQXBpIiwianRpIjoiODU0NzJhODAtN2Q4Ny00MjM0LWIxNmUtODgyMTBmYWZkZDJmIiwicGVtIjp7fSwic3ViIjoiVXNlcjoyIiwidHlwIjoiYWNjZXNzIn0.L2LjpsyJAjF1r99hR11WVGcQ"}
```

Maintenant, vous pouvez installer l'extension [Modheader](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj?hl=en) pour Chrome et toute autre extension grâce à laquelle vous pouvez définir les en-têtes de réponse. Ajoutez `Authorization` comme `Request Header` et le `access_token` avec `Bearer <access_token>`.

![Image](https://cdn-media-1.freecodecamp.org/images/8s46wKgYRFAp7mdlDFIYgtInAUZzUpw3-INz)
_Modheader_

Allez sur [http://localhost:4000/api/v1/users](http://localhost:4000/api/v1/users) et vous pourrez voir un tableau d'utilisateurs que vous avez déjà inscrits. Vous pouvez également aller sur [http://localhost:4000/api/v1/user/current](http://localhost:4000/api/v1/user/current) pour voir l'utilisateur actuel dans la session.

Si vous supprimez cette valeur de Modheader et allez sur [http://localhost:4000/api/v1/users](http://localhost:4000/api/v1/users), vous recevrez la réponse suivante :

```
{  jsonapi: {    version: "1.0"  },  errors: [{    title: "Non autorisé",    code: 401  }]}
```

Comme je l'ai mentionné précédemment, vous devez envoyer le `access_token` reçu pour voir les routes authentifiées. Maintenant, vous savez comment faire l'authentification des API en Elixir. Vous pouvez comparer votre code avec mon code sur [Github](https://github.com/ghoshnirmalya/social_app_api/tree/5f16f6432796f3fe372e971522dd588b5db3a421).

Si vous avez des commentaires, faites-le moi savoir dans les commentaires ci-dessous.