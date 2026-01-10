---
title: Comment utiliser GitHub Copilot pour devenir un développeur plus heureux et
  plus productif
subtitle: ''
author: Tim Kleier
co_authors: []
series: null
date: '2023-06-16T17:02:17.000Z'
originalURL: https://freecodecamp.org/news/developer-productivity-with-github-copilot
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-14-at-12.42.04-PM.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: GitHub
  slug: github
- name: Happiness
  slug: happiness
- name: Productivity
  slug: productivity
seo_title: Comment utiliser GitHub Copilot pour devenir un développeur plus heureux
  et plus productif
seo_desc: 'There are a number of AI tools for developers emerging on the market. But
  in my mind GitHub Copilot stands above the rest because of its usability, seamless
  IDE integration, and remarkable enhancements to developer productivity.

  Copilot offers a vari...'
---

Il existe de nombreux outils d'IA pour les développeurs émergents sur le marché. Mais à mon avis, GitHub Copilot se distingue des autres grâce à son utilité, son intégration transparente avec les IDE et ses améliorations remarquables de la productivité des développeurs.

Copilot offre une variété d'outils d'IA qui ont radicalement rationalisé mon expérience en tant que développeur de logiciels. Je l'ai utilisé pour générer du code, des tests et même des applications simples. Il est également excellent pour le débogage, le refactoring et la documentation du code existant. 

Étrangement, l'utilisation de Copilot m'a permis de développer des fonctionnalités plus rapidement que les parties prenantes de l'entreprise ne peuvent les examiner.

Il est important de noter que les outils d'IA, y compris Copilot, peuvent être clairement erronés, s'excuser (ou non) lorsqu'ils sont corrigés, puis produire la même erreur avec confiance. Mais tant que vous êtes conscient des inconvénients des outils d'IA et que vous avez suffisamment de connaissances en codage pour reconnaître lorsqu'ils sont incorrects, vous pouvez les atténuer sur le chemin vers une [productivité considérablement améliorée](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/).

## Comment installer GitHub Copilot

Pour l'installation et l'utilisation de base de Copilot, consultez la [documentation](https://docs.github.com/fr/copilot). Vous pouvez ajouter Copilot à un compte individuel ou professionnel, et il y a un essai gratuit et un [prix raisonnable](https://github.com/features/copilot#pricing) après l'essai. 

Après avoir ajouté Copilot à votre compte GitHub, vous voudrez installer les [plugins pour votre IDE](https://docs.github.com/fr/copilot/getting-started-with-github-copilot) et vous connecter à GitHub pour accéder à Copilot.

Dans cet article, nous utiliserons ces [extensions Visual Studio Code](https://marketplace.visualstudio.com/search?term=copilot&target=VSCode&category=All%20categories&sortBy=Relevance):

| Extension GitHub      | Description | Aperçu |
| ----------- | ----------- | ----------- |
| [Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)      | Programmeur pair IA avec des suggestions de code dans l'IDE       | Non |
| [Copilot Nightly](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-nightly)   | Version nocturne de Copilot, inclut les dernières modifications        | Non |
| [Copilot Labs](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-labs) | Fonctionnalités expérimentales dans la barre latérale | [Oui](https://githubnext.com/projects/copilot-labs/) |
| [Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) | Chat interactif dans la barre latérale, partie de Copilot X | [Oui](https://github.com/features/preview/copilot-x) |
| [Copilot Voice](https://marketplace.visualstudio.com/items?itemName=GitHub.heygithub) | Assistant vocal | [Oui](https://githubnext.com/projects/copilot-voice/) |

Notes:

1. Ces informations sont à jour au moment de la rédaction de cet article, mais elles changeront probablement à mesure que GitHub fera évoluer ces produits.
2. Je n'ai pas encore reçu l'accès à Copilot Voice ou Copilot (X) pour les Pull Requests, donc mon point de vue sur ces sujets est limité et basé sur les documents de prévisualisation de GitHub.

### Vie privée

Avant de plonger dans quelques cas d'utilisation clés pour Copilot, une rapide note sur la vie privée : Basiquement, si vous faites confiance à GitHub pour héberger votre code source, vous pouvez probablement faire confiance à ce qu'ils font avec vos prompts Copilot et vos extraits de code. [Voir leur [FAQ](https://github.com/features/copilot#faq) et [Déclaration de confidentialité](https://docs.github.com/fr/site-policy/privacy-policies/github-privacy-statement).]

## Cas d'utilisation pour GitHub Copilot

Les cas d'utilisation pour GitHub Copilot sont nombreux, surtout lorsque vous ajoutez les fonctionnalités de prévisualisation de Labs, Chat et Voice. L'utilisation des fonctionnalités de Copilot peut vraiment rationaliser le processus de développement. 

Voici quelques excellentes façons de tirer parti des extensions Copilot:

| Catégorie      | Extension(s) |
| ----------- | ----------- |
| Génération de code      | Copilot, Copilot Nightly, Copilot Voice  |
| Explication de code   | Copilot Labs, Copilot Chat, Copilot Voice        | 
| Traduction de langage | Copilot Labs, Copilot Chat |
| Débogage | Copilot Labs, Copilot Chat |
| Refactoring | Copilot Labs, Copilot Chat |
| Génération de tests | Copilot, Copilot Nightly, Copilot Labs, Copilot Chat |
| Revues de code | Copilot Chat |
| Développement piloté par la voix | Copilot Voice |

### Génération de code

Copilot est connu pour ses fonctionnalités de complétion de code. Si un commentaire est donné dans le code ou si vous tapez le début d'une ligne de code, Copilot suggérera une solution que vous pouvez accepter, ignorer ou explorer des alternatives. Cela est appelé "texte fantôme".

Une fois que vous avez installé l'extension Copilot et que vous êtes connecté, la complétion de code est aussi simple que de taper des instructions et d'appuyer sur la touche Tab une fois que la suggestion apparaît.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screen-Recording-2023-06-09-at-8--1-.gif)
_Un prompt de commentaire en Ruby que Copilot utilise pour créer une méthode et une invocation_

Allant plus loin que la complétion de code, Copilot Chat peut prendre un seul prompt et générer des instructions pour construire une application entière. 

Je lui ai demandé de créer une API REST en Node avec des fonctions CRUD pour "produits", et il a généré du code fonctionnel. Globalement impressionnant. Étant donné le même prompt, ChatGPT m'a également donné des instructions sur la façon d'exécuter le code, ce qui était bien.

Copilot Voice peut également écrire ou modifier du code en fonction des commandes vocales. La plupart du temps, l'utilisation du clavier avec la complétion de code Copilot est plus rapide que la dictée de lignes de code avec Voice. Mais il est convaincant de penser à utiliser Copilot Voice pour créer et exécuter du code sans avoir à taper ou à regarder un écran.

### Explication de code

Je dois souvent fixer un écran pour comprendre ce qu'un bloc de code fait. Parfois, c'est du code hérité où je ne comprends pas le contexte métier. Parfois, il utilise une bibliothèque particulière à laquelle je ne suis pas habitué. Parfois, je maudis la personne qui l'a écrit, même si c'est moi.

Voici un exemple de code généré par Copilot Chat à partir de mon prompt "API REST en Node..." ci-dessus:

```javascript
app.get('/products/:id', (req, res) => {
  const id = req.params.id;
  const product = products.find((p) => p.id === id);
  if (product) {
    res.json(product);
  } else {
    res.status(404).json({ error: 'Product not found' });
  }
});
```

J'ai pris ce code et je l'ai alimenté dans la fonction "Explain" de Copilot Labs. Voici la réponse...

_Voici l'explication pour le code ci-dessus:_  

1. _Nous définissons une route avec le chemin de route /products/:id. Les deux-points : dans le chemin indiquent qu'il s'agit d'un paramètre de route. La valeur du paramètre de route sera disponible dans req.params. Par exemple, si le chemin de route est /products/:id et que nous faisons une requête à /products/5, alors la valeur de req.params sera { id: 5 }._
2. _Nous obtenons l'id de req.params et trouvons le produit avec l'id donné à partir du tableau des produits. Si un produit avec l'id donné existe, nous le retournons. Sinon, nous envoyons une réponse d'erreur 404 avec le message d'erreur Product not found._

Il s'agit d'un segment de code assez simple, et la réponse est claire et directe. Il serait facile d'ajouter cela comme documentation dans un commentaire de code au-dessus de la fonction.

Un autre bon exemple est les expressions régulières. Je comprends comment fonctionnent les expressions régulières, mais je n'ai souvent pas la patience de comprendre ce qu'une regex particulière fait. J'ai alimenté Copilot Chat avec cette énorme instruction regex pour la validation des emails:

```
(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])
```

Il a expliqué la regex à un niveau élevé, indiquant qu'elle était divisée en parties locales et de domaine, représentant avant et après le signe "@" dans une adresse email. Ensuite, il a décrit les caractères autorisés dans chaque partie. Très utile.  

### Traduction de langage

Les développeurs doivent souvent apprendre rapidement de nouveaux langages et frameworks. Copilot Labs et Chat rendent cela assez facile. Voici un tableau de produits en JavaScript et Ruby qui a été converti par Copilot:

```javascript
let products = [
  { id: '1', name: 'Product 1', price: 10.99 },
  { id: '2', name: 'Product 2', price: 19.99 },
  { id: '3', name: 'Product 3', price: 7.99 }
];
```

```ruby
products = [
  { id: '1', name: 'Product 1', price: 10.99 },
  { id: '2', name: 'Product 2', price: 19.99 },
  { id: '3', name: 'Product 3', price: 7.99 }
]
```

Il s'agit d'un exemple très simple, alors essayons de transformer cela en une classe et d'aller dans l'autre sens (de Ruby à JavaScript):

```ruby
class Product
  attr_reader :name, :price

  def initialize(name, price)
    @name = name
    @price = price
  end
end
```

```javascript
class Product {
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }
}
```

Cela semble correct. Pour faire bonne mesure, j'ai également testé TypeScript, et cela a également fonctionné parfaitement.

### Débogage

Il s'agit d'une fonctionnalité très pratique. Vous pouvez donner à Copilot Chat ou Labs du code problématique ou des messages d'erreur et il indiquera ce qu'il pense être le problème. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screen-Recording-2023-06-14-at-1.gif)
_Fonctionnalité "Fix Bug" de Copilot Labs_

Je ne peux pas vous dire combien de cheveux je me suis arrachés parce que je ne trouvais pas ce qui s'avérait être une erreur de syntaxe. La capacité de Copilot à corriger les bugs me rend simplement plus heureux et plus chevelu. 

Vous pouvez également donner à Copilot Chat un message d'erreur sans autre prompt et il peut vous dire le problème. J'ai arbitrairement supprimé un point du code de l'API REST Node:

```javascript
products[productIndex] = { id, ..req.body };
```

J'ai copié/collé le message d'erreur dans Chat, et il a répondu avec...

> En regardant l'extrait de code que vous avez fourni, il semble que le problème soit à la ligne 49 où il y a une erreur de syntaxe dans le littéral d'objet. Les ".." avant `req.body` causent l'erreur. Il devrait y avoir un seul point au lieu de deux.

Cela est à la fois correct (la ligne et la source de l'erreur) et incorrect (qu'il devrait y avoir un seul point). Il m'a ensuite donné un extrait de code avec trois points, ce qui est également correct. 

Comme je l'ai mentionné au début, vous devez double-vérifier le travail de l'IA. Néanmoins, je suis impressionné par la capacité de Copilot à analyser un message d'erreur, décrire ce qu'il pense être incorrect et suggérer une correction.

### Refactoring

Un autre excellent cas d'utilisation est le refactoring. Considérez le code ci-dessous:

```ruby
def price_with_discount
  price - (price * discount_rate)
end
```

Ce simple calcul de prix ne tient pas compte des valeurs `nil`, des chaînes de caractères qui devraient être des nombres, ou des valeurs raisonnables pour `price` ou `discount_rate`. Nous avons besoin que le code fasse ce qui suit:

1. Assurer que `price` est un entier ou un flottant (non nil)
2. Assurer que `price` n'est pas négatif
3. Assurer que `discount_rate` est un flottant (non nil)
4. Assurer que `discount_rate` n'est pas négatif et inférieur ou égal à 1

Copilot Chat gère cela avec facilité...

```ruby
def price_with_discount(price, discount_rate)
  raise ArgumentError, "Price must be a positive number" unless price.is_a?(Numeric) && price >= 0
  raise ArgumentError, "Discount rate must be a float between 0 and 1" unless discount_rate.is_a?(Float) && discount_rate >= 0 && discount_rate <= 1

  price - (price * discount_rate)
end
```

### Génération de tests

Utiliser Copilot pour générer des tests est techniquement un sous-ensemble de la "Génération de code" ci-dessus, mais je pensais que c'était si utile que cela méritait sa propre mention.

Générer des tests unitaires pour du code peut être fastidieux si vous essayez de couvrir les chemins heureux et tristes, les cas d'utilisation principaux et les cas limites. Notre code `price_with_discount` ci-dessus a besoin de cas de test pour s'assurer qu'une erreur est levée si `price` ou `discount_rate` ne répondent pas aux exigences. En outre, nous pourrions vouloir tester ce qui suit:

1. Un `price` sans `discount_rate`
2. Un `price` avec un `discount_rate` raisonnable (par exemple, une réduction de 10%)
3. Un `price` avec un `discount_rate` de 100% (par exemple, si nous voulons donner le produit)

Avec ceux-ci et nos cas d'erreur précédents, voici ce que Copilot Chat a généré, après un peu de réglage fin (re-prompting) et en passant de Minitest à Rspec.

```ruby
RSpec.describe Product do
  describe "#price_with_discount" do
    context "when given a valid price and discount rate" do
      it "returns the price with the discount applied" do
        product = Product.new("Test Product", 100, 0.2)
        expect(product.price_with_discount(product.price, product.discount_rate)).to eq(80)
      end
    end

    context "when given a nil price" do
      it "raises an ArgumentError with an appropriate message" do
        product = Product.new("Test Product", nil, 0.2)
        expect { product.price_with_discount(product.price, product.discount_rate) }.to raise_error(ArgumentError, "Price must be a positive number")
      end
    end

    context "when given a price less than 0" do
      it "raises an ArgumentError with an appropriate message" do
        product = Product.new("Test Product", -100, 0.2)
        expect { product.price_with_discount(product.price, product.discount_rate) }.to raise_error(ArgumentError, "Price must be a positive number")
      end
    end

    context "when given a nil discount rate" do
      it "raises an ArgumentError with an appropriate message" do
        product = Product.new("Test Product", 100, nil)
        expect { product.price_with_discount(product.price, product.discount_rate) }.to raise_error(ArgumentError, "Discount rate must be a float between 0 and 1")
      end
    end

    context "when given a discount rate less than 0" do
      it "raises an ArgumentError with an appropriate message" do
        product = Product.new("Test Product", 100, -0.2)
        expect { product.price_with_discount(product.price, product.discount_rate) }.to raise_error(ArgumentError, "Discount rate must be a float between 0 and 1")
      end
    end

    context "when given a discount rate greater than 1" do
      it "raises an ArgumentError with an appropriate message" do
        product = Product.new("Test Product", 100, 1.5)
        expect { product.price_with_discount(product.price, product.discount_rate) }.to raise_error(ArgumentError, "Discount rate must be a float between 0 and 1")
      end
    end
  end
end
```

Un test pour une entrée valide, cinq pour des entrées invalides. Les six fonctionnent, et je n'ai pas eu à les écrire!

### Revues de code

Une fonctionnalité de Copilot X est [Copilot pour les Pull Requests](https://githubnext.com/projects/copilot-for-pull-requests#technical-preview-available-now). Voici quelques-unes des fonctionnalités clés:

* **Expansion de modèle** – Utilisez Copilot pour remplir votre modèle de PR et expliquer le code
* **Gentest** – Générez des tests pour votre code basé sur l'analyse de Copilot
* **Texte fantôme** – Recevez des suggestions pendant que vous tapez dans la PR

### Développement piloté par la voix

Anciennement connu sous le nom de "Hey, Github!", Copilot Voice vous permet d'utiliser des prompts en langage naturel pour interagir avec votre code. Cela semble impressionnant, avec ces capacités:

* **Écrire/Modifier du code** – Utilisez des commandes vocales pour déclencher des suggestions de code Copilot
* **Navigation dans le code** – Naviguez dans un fichier sans clavier ni souris
* **Contrôle de l'IDE** – Déclenchez n'importe quelle commande VS Code
* **Résumé de code** – Obtenez des résumés de blocs de code

## Résumé

GitHub produit rapidement des outils de productivité révolutionnaire pour les développeurs avec sa suite d'extensions Copilot. Cela augmente ma joie de programmer et diminue le temps que je passe sur des tâches fastidieuses. Je vous encourage à suivre les améliorations de Copilot car elles se produisent rapidement.

Ignorez les promesses de "gain de productivité 10x" qui ne sont que du click-bait, mais ne négligez pas les recherches sur [l'impact de Copilot sur la productivité et le bonheur des développeurs](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/). 

Passez du temps avec les outils Copilot en essayant les cas d'utilisation ci-dessus, et je pense que vous serez surpris par son effet sur votre productivité et votre bonheur.