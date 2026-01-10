---
title: 'Petits Projets Heureux : Elixir, Phoenix, Twilio et l''API Spotify'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-15T18:32:55.000Z'
originalURL: https://freecodecamp.org/news/happy-little-projects-ef8cd157287
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9RWesRs9XuAaOeObRW81SQ.jpeg
tags:
- name: Elixir
  slug: elixir
- name: learning
  slug: learning
- name: Phoenix framework
  slug: phoenix
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: 'Petits Projets Heureux : Elixir, Phoenix, Twilio et l''API Spotify'
seo_desc: 'By Nathan

  One of the most difficult aspects of starting a programming project is coming up
  with a project idea in the first place. No inspiration means no programming!

  Luckily, I recently discovered a project idea with a nice pacing to it: a basic
  No...'
---

Par Nathan

L'un des aspects les plus difficiles pour commencer un projet de programmation est de trouver une idée de projet en premier lieu. Pas d'inspiration signifie pas de programmation !

Heureusement, j'ai récemment découvert une idée de projet avec un bon rythme : une application basique Node.js et Express.js utilisant l'API de Spotify et Twilio.

Si vous souhaitez suivre la version JavaScript, consultez cette [vidéo](https://youtu.be/EKb8XD_V32o). Si vous voulez la construire avec Gradle et Spark, voici le [post original](https://www.twilio.com/blog/2015/09/getting-started-with-gradle-and-the-spark-framework-3.html) de Twilio.

Pour cet article, nous allons construire cette application en utilisant Elixir et Phoenix. Commençons.

Voici le flux général de l'application :

* Vous envoyez par SMS le titre d'une chanson à un numéro Twilio
* Twilio envoie une requête HTTP POST à une URL préconfigurée avec certaines informations, y compris le titre de la chanson et des informations sur le demandeur
* L'application recherche la chanson dans l'API Spotify et extrait une URL de prévisualisation
* L'application envoie un message à l'API Twilio. Cela inclut le numéro à appeler et une URL pour récupérer du TwiML (Twilio Markup Language)
* Twilio récupère le TwiML depuis notre application, appelle le destinataire et lui joue la prévisualisation de la chanson.

J'ai suivi la majorité du programme de [Free Code Camp](http://www.freecodecamp.com). J'ai aidé à concevoir et à construire une grande partie des systèmes principaux derrière Free Code Camp, donc je suis très à l'aise avec JavaScript. Suivre la présentation était facile, et j'ai rapidement pu la recréer. La question était, pouvais-je le faire avec un langage et un framework que je ne maîtrisais pas solidement ?

Si vous souhaitez savoir à quoi ressemble le produit final, envoyez par SMS le titre d'une chanson au +1 (334) 721-2652. Ne vous inquiétez pas, nous n'enregistrerons pas votre numéro de téléphone ou votre chanson. Demandez autant d'ABBA que vous voulez !

NOTE : J'ai chargé des fonds pour que cela continue un moment. Je l'héberge sur Heroku, donc cela peut prendre un moment pour se réveiller et répondre. Si cela ne répond pas du tout, les fonds que j'ai ajoutés ont été épuisés.

Voici une courte vidéo de moi interagissant avec mon application en utilisant Google Voice.

Je voulais me challenger et jouer avec un langage qui me fascine depuis que j'en ai entendu parler. [Elixir](http://elixir-lang.org/) est un langage magnifique avec une syntaxe inspirée de Ruby. Elixir s'exécute sur la BEAM (machine virtuelle Erlang) et est interopérable avec Erlang. Oui, Erlang de la renommée de [WhatsApp](http://www.wired.com/2015/09/whatsapp-serves-900-million-users-50-engineers/). J'adore l'idée de pouvoir exploiter ce genre de puissance et de fiabilité. J'**adore** aussi la programmation fonctionnelle.

En plus d'Elixir, je suis également fan du [framework web Phoenix](http://www.phoenixframework.org/). Il est facile de commencer et de faire des choses. Les messages d'erreur sont excellents et tendent à vous dire exactement comment les corriger. Croyez-moi sur ce point, j'en ai vu assez.

La première tâche est de générer une nouvelle application Phoenix. J'ai appelé la mienne Philter, donc j'ai tapé :

```
mix phoenix.new philter --no-ecto --no-brunch
```

Avec cela, nous créons une nouvelle application Phoenix appelée Philter, sans couche de base de données et sans système de construction JavaScript. Nous n'utiliserons aucun JavaScript dans ce projet !

Suivez les instructions à l'écran pour terminer la configuration de l'application. Nous sommes maintenant prêts à travailler sur notre liste de tâches.

#### **Twilio**

Twilio facilite la création d'un compte. En passant, leur documentation et leur console sont de premier ordre. C'est l'un de mes services web préférés à utiliser.

Inscrivez-vous à Twilio [ici](https://www.twilio.com/try-twilio). Si vous souhaitez suivre ce tutoriel, vous devrez ajouter des fonds. 5 $ seraient plus que suffisants pour vous donner des jours de jeu. Si vous décidez de suivre, achetez un numéro de téléphone et gardez votre onglet de navigateur ouvert.

#### Ngrok

Le service suivant que vous voudrez utiliser est [ngrok](https://ngrok.com/). Ce petit service pratique crée un tunnel vers un port spécifié sur votre ordinateur et vous donne une URL publique à utiliser. Le service est complètement gratuit, mais je me suis inscrit au plan de 5 $/mois pour avoir un sous-domaine réservé. Ce sont les petites choses, je vous le dis.

Ouvrez un nouvel onglet de terminal et installez ngrok via npm. Utilisez ensuite ngrok pour spécifier que vous souhaitez créer un tunnel http vers le port 4000 de votre ordinateur.

```
# est un commentaire pour votre information
# ~ représente votre prompt de terminal
~ npm i -g ngrok
```

```
...
~ ngrok http 4000
ngrok by @inconshreveable                           (Ctrl+C to quit)
```

```
Tunnel Status             online
Version                   2.1.1
Region                    United States (us)
Web Interface             http://127.0.0.1:4040
Forwarding                http://someurl.ngrok.io -> localhost:4000
Forwarding                https://someurl.ngrok.io -> localhost:4000
```

Maintenant, revenez à votre onglet de terminal d'origine et démarrez votre application Phoenix.

```
~ iex -S mix phoenix.server      # <ou>
~ mix phoenix.server
```

La première option démarre le serveur dans un shell interactif qui vous permettra d'interagir avec lui. Quelle que soit la méthode que vous utilisez pour le démarrer, vous verrez qu'il se connecte et écoute sur votre machine locale sur le port 4000.

![Image](https://cdn-media-1.freecodecamp.org/images/zIq2uSM4GlYePld0AMckR7YAYtGlrYH3F5kk)

Ouvrez maintenant un nouvel onglet de navigateur et visitez _localhost:4000_ pour confirmer que cela fonctionne. Ensuite, collez l'URL de la ligne _Forwarding_ http dans le terminal ngrok que j'ai mise en gras ci-dessus. Vous verrez également votre application là-bas. Magie !

Retournez à l'onglet où vous avez votre console Twilio ouverte, et trouvez votre numéro de téléphone. Cliquez dessus, et vous devriez voir certaines informations de configuration. Dans la section de messagerie, « When a message comes in », entrez l'URL de ngrok suivie de « api/sms ». Assurez-vous que la méthode HTTP est définie sur POST. Pour référence, lors de la construction de cette application, la mienne était définie sur _http://tkb.ngrok.com/api/sms_

![Image](https://cdn-media-1.freecodecamp.org/images/ISv5k57nBcVTQJp-xVCfpvLE33K-FDkxJ5Vb)

Pendant que nous avons la console Twilio ouverte, obtenez vos identifiants ACCOUNT SID et AUTH TOKEN. Vous pouvez les trouver en cliquant sur votre nom de compte dans le coin supérieur droit de la fenêtre et en regardant la section « API Credentials ». Créez deux variables d'environnement, TWILIO_ACCOUNT_SID et TWILIO_AUTH_TOKEN. J'utilise une extension du panneau de préférences sur mon Mac appelée [EnvPane](https://github.com/hschmidt/EnvPane). Vous pouvez également rechercher sur Google et obtenir une tonne de résultats si vous avez besoin d'aide pour configurer les vôtres.

Avec toutes ces informations en main, nous sommes presque prêts à tout rassembler. Nous avons une dernière chose à configurer. Nous allons utiliser [ExTwilio](https://github.com/danielberkompas/ex_twilio), une bibliothèque pour aider notre application Phoenix à communiquer avec Twilio.

Ouvrez _config/config.exs_ et ajoutez ce qui suit au-dessus de la dernière instruction _import_ :

```
config :ex_twilio,
  account_sid: System.get_env("TWILIO_ACCOUNT_SID"),
  auth_token: System.get_env("TWILIO_AUTH_TOKEN")
```

C'est ici que nous disons à notre application de lire ces deux variables d'environnement afin que nous puissions envoyer des messages et passer des appels téléphoniques via l'API de Twilio.

Dans votre éditeur préféré (le mien est [Spacemacs](http://spacemacs.org)), ouvrez votre répertoire d'application Phoenix. Mettons-nous au travail.

Ouvrez _web/router.ex_ et supprimez tout ce qui concerne **scope** que vous voyez. Remplacez-le par :

```
scope "/", Philter do
  pipe_through :browser
```

```
  post "/twiml", TwimlController, :index
end
```

```
scope "/api", Philter do
  pipe_through :api
```

```
  post "/sms", SmsController, :index
end
```

Remplacez toute mention de Philter par le nom que vous avez donné à votre application.

Le code ci-dessus a fait quelques choses. Nous avons créé une route qui correspondra aux POSTs vers _http://votreurlngrok/twiml_ et les dirigera vers la fonction index de _TwimlController_. Nous avons également fait de même pour la route _http://votreurlngrok/api/sms_, en passant à la fonction index de _SmsController_. Pour en savoir plus sur le routage dans Phoenix, consultez la excellente [documentation](http://www.phoenixframework.org/docs/routing).

Maintenant, créez deux fichiers dans le répertoire _web/controllers/_, _sms_controller.ex_ et _twiml_controller.ex_. Faites en sorte que votre _sms_controller.ex_ ressemble à ceci :

```
defmodule Philter.SmsController do
  use Philter.Web, :controller
```

```
  alias Philter.Sms
```

```
  def index(conn, %{"Body" => song, "From" => from, "To" => to}) do
```

```
    Task.start_link(fn -> search_spotify(song, %{from: from, to: to}) end)
    send_resp(conn, 200, "")
  end
```

```
  defp search_spotify(song, twilio_data) do
    Philter.Spotify.search(song, twilio_data)
  end
end
```

Pour les Elixiristes qui lisent ceci, veuillez garder à l'esprit que je suis encore en train d'apprendre. Avec cet avertissement, passons à une brève explication.

Twilio enverra le numéro de téléphone du demandeur dans un champ _From_, notre numéro Twilio dans le champ _To_, et le corps de leur texte dans le champ _Body_. Nous extrayons ces informations, puis nous lançons une tâche pour rechercher dans l'API Spotify.

![Image](https://cdn-media-1.freecodecamp.org/images/-pfgkBdJYkKY--vlTT9D32JaH9mjrnyqP8PP)

Lancer une tâche exécute une fonction longue durée dans un processus BEAM super léger. Si quelque chose arrive au processus, comme un plantage ou un incendie ou une frappe par des rayons cosmiques, notre application continuera joyeusement à accepter des connexions et à prévenir les moments de panique du développeur.

Une discussion complète sur les tâches et OTP en général est bien au-delà de la portée de cet article. Veuillez vous référer aux liens Elixir dans cet article si vous souhaitez en savoir plus sur cette bête amazing.

Maintenant, consultez le [dépôt GitHub](https://github.com/terakilobyte/Philter) pour ce projet. Les fichiers que vous voudrez copier sont _lib/philter/spotify.ex_ et le répertoire entier _lib/philter/spotify/_. Assurez-vous de parcourir les fichiers, en changeant toute mention de Philter par le nom de votre propre application. Dans _spotify.ex_, [à la ligne 55](https://github.com/terakilobyte/Philter/blob/master/lib/philter/spotify.ex#L55), remplacez « tkb » dans l'URL par votre URL ngrok.

Maintenant, faites en sorte que votre _twiml_controller.ex_ ressemble à ceci :

```
defmodule Philter.TwimlController do
  use Philter.Web, :controller
```

```
  alias Philter.Twiml
```

```
  def index(conn, %{"song" => song}) do
    render(conn, "index.html", song: song)
  end
end
```

Tout ce que nous faisons ici est d'extraire la chanson et de la passer comme variable à notre template.

Ouvrez le fichier _app.html.eex_ dans le répertoire _web/templates/_ et supprimez tout sauf :

```
<%= render @view_module, @view_template, assigns %>
```

Nous n'avons pas besoin de tout ce autre balisage !

Ensuite, créez un fichier sous le répertoire _web/views/_ appelé _twiml_view.ex_. Nous pourrions mettre des fonctions d'aide ici, mais nous n'en avons pas besoin, donc il va simplement vivre comme un fichier shell. Le contenu doit être :

```
defmodule Philter.TwimlView do
  use Philter.Web, :view
end
```

Maintenant, créez un nouveau répertoire sous _web/templates/_ appelé _twiml/_ et à l'intérieur créez un fichier appelé _index.html.eex_. Le contenu est simple :

```
<?xml version="1.0" encoding="UTF-8" ?>
<Response>
  <Say>Please enjoy the clip!</Say>
  <Play><%= @song %></Play>
  <Say>I hope you enjoyed your song clip</Say>
</Response>
```

C'est la réponse que nous enverrons à Twilio lorsqu'ils nous demanderont du TwiML en réponse à notre interaction avec l'API dans la tâche que j'ai à peine abordée. N'hésitez pas à jouer, et consultez la grande [documentation TwiML](https://www.twilio.com/docs/api/twiml).

Avec un redémarrage de Phoenix, vous devriez pouvoir envoyer un SMS à votre numéro Twilio et recevoir un appel téléphonique avec la prévisualisation de la chanson !

#### Dénouement

J'ai eu beaucoup de plaisir à implémenter cette petite application avec Elixir. Tout comme lorsque j'apprenais JavaScript, j'ai dû comprendre comment faire les choses, utiliser correctement les fonctions (même trouver les bonnes fonctions à utiliser !), et m'assurer que la logique de l'application était correcte.

Il y a eu beaucoup de sourcils froncés et beaucoup de documentation et de tutoriels en ligne ont été consultés alors que je plongeais plus profondément dans Elixir. J'ai été très agréablement surpris de la quantité de code spécifique à Phoenix nécessaire. C'est un excellent framework à mon avis.

En fin de compte, le produit final a rendu les frustrations temporaires dignes. Obtenir des réactions de ma femme et de mes amis comme « C'est trop cool ! » ou « Tu as fait ça ? » valent définitivement l'effort. Cela a également aidé à cimenter des modèles et des notions que j'avais sur le fonctionnement des choses plus clairement. Peut-être qu'après avoir quitté l'armée, je pourrai effectivement faire la transition vers une carrière dans la programmation.

Je dois rendre hommage à Twilio. Ils ont créé un excellent projet. Chaque interaction que je devais effectuer était bien documentée, et leur console de gestion elle-même a facilité la recherche de ce dont j'avais besoin et la configuration des actions de ce côté.

Si vous êtes intéressé à en savoir plus sur Elixir et Phoenix, je vous recommande vivement [Programming Elixir](https://pragprog.com/book/elixir12/programming-elixir-1-2), [Elixir In Action](https://www.manning.com/books/elixir-in-action), et [Programming Phoenix](https://pragprog.com/book/phoenix/programming-phoenix). J'ai les trois et ils sont excellents ! La documentation en ligne est bien au-dessus de la moyenne, et de plus en plus de tutoriels et d'articles apparaissent. En général, la communauté Elixir est l'une des meilleures.

Nous sommes définitivement enthousiastes à l'idée d'ajouter Elixir à nos langages backend chez FreeCodeCamp.

Apprendre à coder est difficile. Je vous recommande vivement de vous inscrire à [FreeCodeCamp](http://www.freecodecamp.com) et de suivre la voie d'apprentissage très structurée et auto-rythmée que nous avons établie. Des milliers et des milliers de personnes trouvent du succès, et nous avons une **énorme** communauté de personnes serviables - des débutants aux professionnels - dans notre salle Gitter.

Rappelez-vous, ne laissez pas quelque chose d'éphémère comme la frustration face à une tâche aujourd'hui vous empêcher d'atteindre vos objectifs demain. Bon codage !