---
title: Comment transformer votre site web en une application mobile avec 7 lignes
  de JSON
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-22T02:42:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-turn-your-website-into-a-mobile-app-with-7-lines-of-json-631c9c9895f5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*x-5_XGJJhAgiBmLe54I3xg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment transformer votre site web en une application mobile avec 7 lignes
  de JSON
seo_desc: 'By Ethan

  A New Approach for Blending Web Engine into Native Apps

  What if I told you the 7 lines of JSON above, colored in orange is all you need
  to turn a website into a mobile app? No need to rewrite your website using some
  framework API just to mak...'
---

Par Ethan

#### Une nouvelle approche pour intégrer le moteur web dans les applications natives

Et si je vous disais que **les 7 lignes de JSON ci-dessus, colorées en orange** sont tout ce dont vous avez besoin pour transformer un site web en une application mobile ? Pas besoin de réécrire votre site web en utilisant une API de framework pour qu'il se comporte comme une application mobile. Il suffit d'apporter votre site web existant tel quel et de l'intégrer dans une application native avec une simple référence URL.

Et si, en modifiant légèrement le balisage JSON, vous pouviez accéder à toutes les API natives, aux composants d'interface utilisateur natifs, ainsi qu'aux transitions de vue natives dès la sortie de la boîte ?

Voici à quoi ressemble un exemple minimal en action :

![Image](https://cdn-media-1.freecodecamp.org/images/1kjzo4uXso3Yk08RYYUUYGK6HXrlCs42aXqG)

Remarquez comment j'ai intégré une [page web github.com](https://github.com/Jasonette), mais le reste de la mise en page est entièrement composé de composants d'interface utilisateur natifs, tels que [l'en-tête de navigation](https://docs.jasonette.com/document/#bodyheader) et la [barre d'onglets inférieure](https://docs.jasonette.com/document/#tabs). Et la transition est automatiquement native sans que vous ayez à réécrire le site web en utilisant des API.

Avant de vous expliquer comment, vous pourriez demander : « C'est cool, mais pouvez-vous faire autre chose de significatif que simplement afficher la page web dans un cadre d'application native ? »

Excellente question, car c'est le sujet principal de cet article. Tout ce que vous avez à faire est de créer un canal de communication **bidirectionnel entre la vue web et l'application**, afin que l'application parente puisse déclencher n'importe quelle fonction JavaScript à l'intérieur de la vue web et que la vue web puisse atteindre l'extérieur pour appeler des API natives.

Voici un exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/8AvgutqafADVJW2WYgH3o0kBVDZvVuUIoU6C)

Notez que cette vue contient :

1. Un en-tête de navigation natif, complet avec une fonctionnalité de transition intégrée
2. Une vue Web, qui intègre une application web de générateur de codes QR
3. Un composant de saisie de chat natif en bas

Tout cela peut être décrit en modifiant simplement certains des attributs de balisage JSON que nous avons vus ci-dessus.

Enfin, notez que le code QR change lorsque vous entrez quelque chose à partir de la saisie de chat. La saisie de chat déclenche une fonction JavaScript à l'intérieur de l'application web de code QR qui régénère l'image.

Aucun framework de développement d'applications n'a tenté de résoudre fondamentalement ce problème de **« intégration transparente de la vue web dans les applications natives »** car ils sont tous axés sur le choix entre 100 % natif ou 100 % HTML5.

Chaque fois que vous entendez quelqu'un parler de l'avenir des applications mobiles, vous entendrez probablement parler de **« Est-ce que l'approche HTML5 l'emportera ? Ou est-ce que ce sera le natif ? »**

Aucun d'entre eux ne voit `native` et `html` comme quelque chose qui pourrait coexister et, de plus, créer une synergie et réaliser des choses qui ne sont pas facilement possibles autrement.

Dans cet article, je vais expliquer :

* Pourquoi l'intégration du moteur web et des composants natifs est souvent une bonne idée.
* Pourquoi une intégration transparente de HTML et Natif n'est pas facile, et comment j'ai implémenté une solution.
* Plus important encore, comment VOUS pouvez l'utiliser pour construire votre propre application instantanément.

### Pourquoi utiliser HTML dans une application native ?

Avant d'aller plus loin, discutons d'abord si c'est une bonne idée, et quand vous pourriez vouloir adopter cette approche. Voici quelques cas d'utilisation potentiels :

#### 1. Utiliser les fonctionnalités Web natives

Certaines parties de votre application peuvent être mieux implémentées en utilisant le moteur web. Par exemple, [Websocket](https://en.wikipedia.org/wiki/WebSocket) est une fonctionnalité web-native conçue pour l'environnement web. Dans ce cas, il est logique d'utiliser le moteur web intégré (**WKWebView pour iOS** et **WebView pour Android**) au lieu d'installer une bibliothèque tierce qui **« émule »** essentiellement Websocket.

Pas besoin d'installer du code supplémentaire juste pour faire quelque chose que vous pouvez faire gratuitement, ce qui nous amène au point suivant.

#### 2. Éviter une taille binaire importante

Vous pourriez vouloir incorporer rapidement des fonctionnalités qui nécessiteraient autrement une énorme bibliothèque tierce.

Par exemple, pour incorporer un générateur d'images de codes QR de manière native, vous devrez installer une bibliothèque tierce qui augmentera la taille binaire. Mais si vous utilisez le moteur de vue web et une bibliothèque JavaScript via un simple `<script src>`, vous obtenez tout cela gratuitement, et vous n'avez pas besoin d'installer de bibliothèques natives tierces.

#### 3. Aucune bibliothèque mobile fiable n'existe

Pour certaines technologies de pointe, il n'existe pas encore d'implémentation mobile fiable et stable.

Heureusement, la plupart de ces technologies ont des implémentations web, donc le moyen le plus efficace de les intégrer est d'utiliser leur bibliothèque JavaScript.

#### 4. Construire des applications partiellement natives et partiellement basées sur le web

De nombreux nouveaux développeurs cherchant à porter leur site web dans une application mobile se découragent ou se sentent submergés lorsqu'ils découvrent que certaines fonctionnalités de leur site web existant sont trop complexes à réécrire rapidement à partir de zéro pour chaque plateforme mobile.

Par exemple, vous pourriez avoir une seule page web qui est trop complexe à convertir immédiatement en une application mobile, mais le reste de votre site web pourrait être facilement converti.

Dans ce cas, il serait bien s'il existait un moyen de construire la plupart de l'application de manière native, mais pour cette page web complexe particulière, de l'intégrer de manière transparente dans l'application sous forme de HTML.

### Comment cela fonctionne-t-il ?

#### A. Jasonette

Jasonette est une approche open source, basée sur le balisage, pour construire des applications natives multiplateformes.

C'est comme un navigateur web, mais au lieu d'interpréter le balisage HTML en pages web, il interprète le balisage JSON en applications natives sur iOS et Android.

Tout comme tous les navigateurs web ont exactement le même code mais peuvent vous fournir toutes sortes d'applications web différentes en interprétant divers balisages HTML à la demande, toutes les applications Jasonette ont exactement le même binaire, et il interprète divers balisages JSON à la demande pour créer votre application. Les développeurs n'ont jamais besoin de toucher au code. Au lieu de cela, vous construisez des applications en écrivant un balisage qui se traduit en application native en temps réel.

Vous pouvez en savoir plus sur Jasonette [ici](https://medium.freecodecamp.org/how-to-build-cross-platform-mobile-apps-using-nothing-more-than-a-json-markup-f493abec1873).

Bien que Jasonette, à sa base, soit entièrement dédié à la construction d'applications natives, cet article particulier traite de l'intégration de HTML dans le moteur natif de base, alors parlons-en.

#### B. Conteneur Web Jasonette

Les applications natives sont excellentes, mais parfois nous devons utiliser des fonctionnalités web.

Mais intégrer des vues web dans une application native est une tâche délicate. Une intégration transparente nécessite :

1. **La vue web doit être intégrée comme une partie de la mise en page native** : La vue web doit se fondre dans l'application comme une partie de la mise en page native et est traitée comme n'importe quel autre composant d'interface utilisateur natif. Sinon, cela semblera maladroit, et cela semblera exactement ce que c'est — un site web.
2. **L'application parente peut contrôler le conteneur web enfant** : L'application parente doit pouvoir contrôler librement la vue web enfant.
3. **Le conteneur web enfant peut déclencher des événements natifs sur l'application parente** : L'application enfant doit pouvoir déclencher les événements de l'application parente pour exécuter des API natives.

Cela représente beaucoup de travail, donc j'ai d'abord travaillé uniquement sur la première partie du puzzle — **simplement intégrer un conteneur web dans une mise en page native** — et je l'ai publié comme version 1 :

[**Conteneur Web JSON**](http://jasonette.com/webcontainer/)  
[_HTML à l'intérieur de JSON se transforme en composants d'application natifs_jasonette.com](http://jasonette.com/webcontainer/)

Cela était déjà assez utile, mais cela avait encore la limitation d'être non interactif.

L'application parente ne pouvait pas contrôler le conteneur web enfant, et l'enfant ne pouvait pas notifier le parent d'un événement quelconque, gardant le conteneur web complètement isolé du monde extérieur.

#### C. Jasonette Web Container 2.0 : Rendre le tout interactif

Après avoir publié la version 1, j'ai expérimenté avec la deuxième partie du puzzle — **ajouter de l'interactivité au conteneur web**.

La section suivante explique les solutions qui ont été ajoutées pour rendre les conteneurs web précédemment statiques interactifs, les rendant ainsi significativement plus puissants.

### Implémentation : Conteneur Web Interactif

#### **1. Chargement par URL**

#### Problème

Auparavant, dans la version 1, pour utiliser le conteneur web comme composant de vue d'arrière-plan, vous deviez d'abord [définir le type `$jason.body.background.type` sur `"html"` et ensuite coder en dur le texte HTML sous l'attribut `$jason.body.background.text`](https://jasonette.com/webcontainer/) comme ceci :

```
{  "$jason": {    "head": {      ...    },    "body": {      "background": {        "type": "html",        "text": "<html><body><h1>Hello World</h1></body></html>"      }    }  }}
```

Naturellement, les gens voulaient pouvoir instancier le conteneur en utilisant simplement une URL web au lieu de devoir coder en dur l'ensemble du texte HTML en une seule ligne.

#### Solution

Le conteneur web 2.0 a ajouté l'attribut `url`. Vous pouvez intégrer un fichier HTML local `file://` comme ceci (il charge à partir du fichier HTML local que vous livrez avec l'application) :

```
{  "$jason": {    "head": {      ...    },    "body": {      "background": {        "type": "html",        "url": "file://index.html"      }    }  }}
```

Ou intégrer une URL distante `http[s]://` comme ceci (il charge à partir d'un HTML distant) :

```
{  "$jason": {    "head": {      ...    },    "body": {      "background": {        "type": "html",        "url": "https://news.ycombinator.com"      }    }  }}
```

#### **2. Communication entre l'application parente et le conteneur web**

#### Problème

Auparavant, les conteneurs web n'étaient utilisés que pour afficher du contenu, et non pour interagir. Cela signifiait que **AUCUNE des actions suivantes n'était possible** :

1. **Jasonette => Conteneur Web** : Appeler des fonctions JavaScript à l'intérieur du conteneur web depuis Jasonette.
2. **Conteneur Web => Jasonette** : Appeler une API native depuis le code du conteneur web.

Tout ce que vous pouviez faire était d'afficher le conteneur web. Cela ressemblait à la manière dont vous intégreriez un iframe dans une page web, mais la page web principale n'avait aucun accès à ce qui se trouvait à l'intérieur de l'iframe.

#### Solution

Le but de Jasonette est de concevoir un langage de balisage standard pour décrire des applications mobiles multiplateformes. Dans ce cas, nous avions besoin d'un langage de balisage qui pourrait décrire de manière exhaustive les communications entre l'application parente et le conteneur web enfant.

Pour y parvenir, j'ai imaginé un canal de communication basé sur `[JSON-RPC](http://www.jsonrpc.org/specification)` entre l'application parente et le conteneur web enfant. Puisque tout dans Jasonette est exprimé en objets JSON, il était parfaitement logique d'utiliser le format standard JSON-RPC comme protocole de communication.

![Image](https://cdn-media-1.freecodecamp.org/images/dISqZspArHgei6hasHQ89nw7g1GrWSsyPG8s)

Pour effectuer un appel de fonction JavaScript dans le conteneur web, nous déclarons une action appelée `$agent.request` :

```
{  "type": "$agent.request",  "options": {    "id": "$webcontainer",    "method": "login",    "params": ["username", "password"]  }}
```

`[$agent.request](https://docs.jasonette.com/agents/#1-agentrequest)` est l'API native qui déclenche une requête JSON-RPC dans le conteneur web. Pour l'utiliser, nous devons passer un objet `options` comme paramètre.

L'objet `options` est la requête [JSON-RPC](http://www.jsonrpc.org/specification#conventions) réelle qui sera envoyée au conteneur web. Examinons ce que signifie chaque attribut :

* `id` : Le conteneur web est construit sur une architecture de niveau inférieur appelée [agent](https://jasonette.com/agent/). Normalement, vous pouvez avoir plusieurs agents pour une seule vue, et chaque agent peut avoir son identifiant unique. Mais [le conteneur web est un type spécial d'agent qui ne peut avoir que l'identifiant `$webcontainer`](https://docs.jasonette.com/web/#1-background-web-container-is-an-agent), c'est pourquoi nous utilisons cet identifiant ici.
* `method` : Le nom de la fonction JavaScript à appeler
* `params` : Le tableau des paramètres à passer à la fonction JavaScript.

Le balisage complet ressemblerait à ceci :

```
{  "$jason": {    "head": {      "actions": {        "$load": {          "type": "$agent.request",          "options": {            "id": "$webcontainer",            "method": "login",            "params": ["alice", "1234"]          }        }      }    },    "body": {      "header": {        "title": "Web Container 2.0"      },      "background": {        "type": "html",        "url": "file://index.html"      }    }  }}
```

Ce balisage dit :

Lorsque la vue se charge (`[$jason.head.actions.$load](https://docs.jasonette.com/actions/#1-load)`), faire une requête JSON-RPC dans l'agent du conteneur web (`[$agent.request](https://docs.jasonette.com/agents/#1-agentrequest)`) où la requête est spécifiée sous `options`.

Le conteneur web est défini sous `[$jason.body.background](https://docs.jasonette.com/web/#in-depth-on-background-web-container)`, qui dans ce cas charge un fichier local appelé `file://index.html`.

Il recherchera une fonction JavaScript appelée `login` et passera les deux arguments sous `params` (`"alice"` et `"1234"`)

```
login("alice", "1234")
```

Je n'ai expliqué que comment l'application parente peut déclencher les appels de fonctions JavaScript du conteneur web enfant, mais vous pouvez aussi faire l'inverse et [laisser le conteneur web déclencher l'API native de l'application parente](https://docs.jasonette.com/agents/#3-agenttrigger).

Pour en savoir plus, consultez la [documentation sur les agents](https://docs.jasonette.com/agents/).

#### Exemple

Revenons à l'exemple du code QR que j'ai brièvement partagé ci-dessus :

![Image](https://cdn-media-1.freecodecamp.org/images/q5-enhI0kpKTs6F33sgyI0mS9sLqOXnHFeHI)

1. Le [composant de saisie du pied de page est 100 % natif](https://docs.jasonette.com/document/#input).
2. Le code QR est généré par le conteneur web [en tant qu'application web](https://github.com/Jasonette/Jasonpedia/blob/gh-pages/webcontainer/agent/fn/agent.html).
3. Lorsque l'utilisateur entre quelque chose et appuie sur « Générer », il appelle l'action `$agent.request` dans l'agent du conteneur web, appelant la [fonction JavaScript « qr »](https://github.com/Jasonette/Jasonpedia/blob/gh-pages/webcontainer/agent/fn/agent.html#L22)

Vous pouvez consulter l'exemple [ici](https://github.com/Jasonette/Jasonpedia/blob/gh-pages/webcontainer/agent/fn/index.json).

#### **3. Injection de script**

#### Problème

Parfois, vous pourriez vouloir injecter dynamiquement du code JavaScript dans le conteneur web APRÈS qu'il ait terminé le chargement du HTML initial.

Imaginez que vous souhaitez construire une application de navigateur web personnalisée. Vous pourriez vouloir injecter votre propre JavaScript personnalisé dans chaque vue web pour personnaliser le comportement de la vue web, un peu comme le font les extensions de navigateur web.

Même si vous ne construisez pas un navigateur web, vous pourriez vouloir utiliser la méthode d'injection de script chaque fois que vous souhaitez un comportement personnalisé pour une URL dont vous ne pouvez pas contrôler le contenu. Le seul moyen de communiquer entre l'application native et le conteneur web est via l'API `$agent`. Mais si vous ne pouvez pas changer le contenu HTML, le seul moyen d'ajouter l'interface `$agent` dans le conteneur web est par injection dynamique.

#### Solution

Comme mentionné dans la section précédente, le conteneur web `$jason.body.background` est simplement un autre `agent`. Cela signifie que vous pouvez utiliser la même méthode `[$agent.inject](https://docs.jasonette.com/agents/#7-agentinject)` disponible pour les agents réguliers.

![Image](https://cdn-media-1.freecodecamp.org/images/kt6qG0I8AgcTy270pNSHCE2QfZpdRRMg8SZU)

#### **4. Gestion des clics sur les URL**

Par le passé, il n'y avait que deux façons pour un conteneur web de gérer les clics sur les liens :

1. **Lecture seule** : Traiter le conteneur web comme étant en lecture seule et ignorer tous les événements tels que le toucher ou le défilement. Tous les conteneurs web sont en lecture seule sauf si vous leur dites de se comporter comme un navigateur régulier, comme décrit ci-dessous.
2. **Comportement de navigateur régulier** : Laisser les utilisateurs interagir avec la page en se comportant comme un navigateur normal. Vous le déclarez en définissant `"type": "$default"` comme attribut d'`action`.

#### Problème

Les deux sont des solutions **« tout ou rien »**.

* Dans le cas « Lecture seule », toutes vos interactions sont complètement ignorées par le conteneur web.
* Dans le cas « Comportement de navigateur régulier », le conteneur web fonctionne littéralement comme un navigateur. Lorsque vous cliquez sur un lien, il vous envoie simplement à ce lien en actualisant la page comme une page web. Il n'y avait aucun moyen de détourner le clic et d'appeler une API native.

#### Solution

Avec le nouveau conteneur web, vous pouvez maintenant attacher n'importe quelle `action` au conteneur web `$jason.body.background` pour gérer les événements de clic sur les liens.

![Image](https://cdn-media-1.freecodecamp.org/images/FhoDSEv8qQ4ZISs6syta2eU80WYBeQmFRAAS)

Regardons un exemple :

```
{  "$jason": {    "head": {      "actions": {        "displayBanner": {          "type": "$util.banner",          "options": {            "title": "Cliqué",            "description": "Lien {{$jason.url}} cliqué !"          }        }      }    },    "body": {      "background": {        "type": "html",        "url": "file://index.html",        "action": {          "trigger": "displayBanner"        }      }    }  }}
```

Ici, nous avons attaché `"trigger": "displayBanner"` au conteneur web. Cela signifie que lorsque l'utilisateur clique sur un lien dans le conteneur web, il déclenchera l'action `displayBanner` au lieu de laisser la vue web le gérer.

De plus, si vous regardez l'action `displayBanner`, vous remarquerez la variable `$jason`. Dans ce cas, le lien cliqué sera passé via la variable `$jason`. Par exemple, si vous avez cliqué sur une URL nommée `"https://google.com"`, `$jason` aura la valeur suivante :

```
{  "url": "https://google.com"}
```

Cela signifie que vous pouvez déclencher sélectivement différentes actions en [vérifiant la valeur de `$jason.url`](https://docs.jasonette.com/web/#b-intercept-url-visits).

Prenons un autre exemple où nous implémentons un navigateur web personnalisé :

```
{  "$jason": {    "head": {      "actions": {        "handleLink": [{          "{{#if $jason.url.indexOf('signin') !== -1 }}": {            "type": "$href",            "options": {              "url": "file://key.html"            }          }        }, {          "{{#else}}": {            "type": "$default"          }        }]      }    },    "body": {      "background": {        "type": "html",        "url": "file://index.html",        "action": {          "trigger": "handleLink"        }      }    }  }}
```

Nous testons si l'URL contient la chaîne `signin` et exécutons ensuite deux actions différentes en fonction du résultat.

1. Si elle contient `signin`, elle ouvre une nouvelle vue pour gérer la connexion de manière native.
2. Si elle ne contient pas `signin`, elle exécute simplement l'action `"type": "$default"` pour qu'elle se comporte comme un navigateur régulier.

### Exemple d'utilisation

#### Construction d'un navigateur web personnalisé

Nous pouvons maintenant tirer parti du fait que le nouveau conteneur web peut :

1. Prendre un attribut `url` pour se charger lui-même, fonctionnant comme un navigateur complet
2. Gérer sélectivement les clics sur les liens en fonction de l'URL

Nous pouvons même construire une application de navigateur web personnalisée avec seulement une douzaine de lignes de JSON. Puisque nous pouvons maintenant détourner chaque clic sur un lien, nous pouvons examiner `$jason.url` et exécuter les actions que nous voulons en fonction de l'URL.

Par exemple, regardez l'exemple ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/iNRAFCyHHrGptiuenltF7rK902otq27ZMmTq)

![Image](https://cdn-media-1.freecodecamp.org/images/8vFiQuuuBm-KTt8LaNS-UEldKrWOCvJlI-0k)

Sur le côté gauche, nous voyons que cliquer sur un lien se comporte comme un navigateur régulier (`"type": "$default"`)

Sur le côté droit, nous voyons que cliquer sur un lien effectue une transition native vers une autre vue JASON.

Tout cela peut être réalisé en déclenchant sélectivement différentes actions basées sur `$jason.url`.

**Étape 1. Attacher une action nommée `visit` au conteneur web comme ceci :**

```
{  ...  "body": {    "background": {      "type": "html",      "url": "https://news.ycombinator.com",      "action": {        "trigger": "visit"      }    }  }}
```

**Étape 2. Exécuter des actions pertinentes à l'intérieur de `visit`, basées sur `$jason.url`**

Dans le code suivant, nous vérifions si `$jason.url` correspond à `newest`, `show`, `ask`, etc. (ce sont les liens des éléments du menu supérieur). Si elles correspondent, nous laissons le conteneur web se comporter comme un navigateur régulier en définissant `"type": "$default"`

Si elles ne correspondent pas au motif, nous effectuons une transition native `$href` vers une nouvelle vue et passons le lien cliqué comme paramètre.

```
..."actions": {  "visit": [    {      "{{#if /\\/(newest|show|ask)$/.test($jason.url) }}": {        "type": "$default"      }    },    {      "{{#else}}": {        "type": "$href",        "options": {          "url": "https://jasonette.github.io/Jasonpedia/webcontainer/agent/hijack.json",          "preload": {            "background": "#ffffff"          },          "options": {            "url": "{{$jason.url}}"          }        }      }    }  ]},
```

Consultez le balisage JSON complet pour le navigateur web [ici](https://github.com/Jasonette/Jasonpedia/blob/gh-pages/webcontainer/agent/hijack.json) (il ne fait que 48 lignes !).

#### Application "Hybride" Instantanée

Lorsque les gens parlent normalement d'applications "hybrides", ils signifient principalement des applications web HTML enveloppées dans un cadre d'application native.

Mais ce n'est pas ce que je veux dire ici. Lorsque je dis "Hybride", je veux dire une application vraiment hybride, où une application peut avoir plusieurs vues natives et plusieurs vues basées sur le web simultanément. De plus, où une vue peut avoir plusieurs composants d'interface utilisateur natifs et un conteneur web rendu dans la même mise en page native.

**Le croisement entre la vue basée sur le web et la vue native doit être si transparent qu'il est difficile de dire où l'une commence et où l'autre se termine.**

![Image](https://cdn-media-1.freecodecamp.org/images/KVknGIXFeBzMxUsY1pBCddiWdEub8Jl26i0g)

Dans cet exemple, j'ai créé une application qui affiche [jasonbase.com](https://www.jasonbase.com) dans un conteneur web comme vue d'accueil.

Jasonbase est un service d'hébergement JSON gratuit que j'ai construit pour héberger facilement le balisage JSON des applications Jasonette.

Naturellement, ce n'est qu'un site web, mais je l'ai intégré dans Jasonette de sorte que lorsque vous cliquez sur le lien, au lieu d'ouvrir une page web, il effectue une transition native `$href` vers une vue JASON native.

**Je n'ai pas eu à toucher au code de Jasonbase.com pour construire cette application.**

**J'ai simplement intégré le site web dans Jasonette en tant que conteneur web, et j'ai détourné les clics sur les liens pour les gérer de manière native, afin qu'il puisse faire toutes les choses natives comme déclencher des API natives et effectuer des transitions natives.**

Vous pouvez consulter le code [ici](https://github.com/Jasonette/Jasonpedia/blob/gh-pages/webcontainer/agent/hybrid.json).

### Conclusion

À mon avis, ce qui rend tout cela fabuleux, c'est que **tout est pris en charge au niveau du framework**. Tout le travail difficile est pris en charge en coulisses.

Au lieu de mettre le fardeau sur les développeurs d'applications pour implémenter tout ce qui suit à partir de zéro :

* Intégrer une webview dans une mise en page native
* Créer un pont JavaScript pour que l'application puisse effectuer des appels de fonctions dans la vue web
* Créer une architecture de gestion d'événements native pour que la vue web puisse déclencher des événements natifs sur l'application parente

La solution a été de créer une abstraction composée de :

1. **Langage de balisage déclaratif** : pour décrire comment intégrer une vue web dans une application native
2. **Protocole de communication (JSON-RPC)** : pour permettre des interactions extrêmement simples entre l'application et ses vues web enfants.

Je ne prétends pas que cette approche soit la solution ultime pour tout résoudre, mais je suis heureux de dire que cela a été une excellente solution pour mon propre cas d'utilisation.

J'essayais de construire une application qui repose sur une technologie de pointe qui n'a pas d'implémentations mobiles stables et fiables (et il n'est pas clair s'il y aura jamais une implémentation mobile en raison de la nature du protocole). Heureusement, elle avait des implémentations JavaScript, donc j'ai pu l'intégrer facilement dans l'application sans tracas.

Dans l'ensemble, cela a été formidable et je suis satisfait du résultat. [La documentation est à jour](https://docs.jasonette.com/web/) pour refléter toutes les nouvelles fonctionnalités, alors n'hésitez pas à vous plonger dedans et à jouer avec.

> Avertissement : Un grand pouvoir implique de grandes responsabilités

Je voudrais terminer par un avertissement : aussi formidable que soit ce nouveau pouvoir, je pense que vous devez garder un équilibre pour construire une application avec une excellente expérience utilisateur.

Certains pourraient prendre cela et construire une application entière en utilisant uniquement des vues web, mais alors vous vous retrouverez avec une application qui est essentiellement juste un site web, ce qui défait le but de construire une application dédiée.

Je souligne que je ne dis pas que vous devriez toujours construire des applications avec à la fois HTML et natif. Je dis que cela peut être très utile pour de nombreuses personnes dans différentes situations. Ne vous laissez simplement pas emporter.

> Suivez pour en savoir plus

Il existe de nombreuses configurations différentes dans lesquelles le noyau natif Jasonette et son conteneur web enfant peuvent communiquer pour accomplir des choses de manière créative et puissante, et cet article ne fait qu'effleurer la surface.

À l'avenir, je prévois de partager davantage de ces cas d'utilisation et tutoriels, alors si vous êtes intéressé, veuillez suivre sur [medium](https://medium.com/@gliechtenstein) ou [twitter](https://twitter.com/jasonclient).