---
title: Pourquoi le Vibe Coding ne détruira pas l'ingénierie logicielle
date: '2025-05-21T15:46:37.887Z'
author: Ben
authorURL: https://www.freecodecamp.org/news/author/justanothertechlead/
originalURL: https://freecodecamp.org/news/why-vibe-coding-wont-destroy-software-engineering
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747835351675/3d178f26-c528-48b8-8ac2-32811a5672cf.png
tags:
- name: vibe coding
  slug: vibe-coding
- name: AI Coding Assistant
  slug: ai-coding-assistant
- name: AI
  slug: ai
- name: '#ai-tools'
  slug: ai-tools
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_desc: 'AI is disrupting all industries at a pace not seen at any time in history.

  Technologies and industries that were once dominated by one or two companies or
  were very much “human-focused” are coming under threat.

  Google is losing ground to AI search, t...'
---


L'IA bouleverse tous les secteurs à un rythme jamais vu dans l'histoire.

<!-- more -->

Des technologies et des industries autrefois dominées par une ou deux entreprises, ou très axées sur l'humain, sont aujourd'hui menacées.

[Google perd du terrain face à la recherche par IA][1], les [chauffeurs routiers][2] pourraient bientôt appartenir au passé, et des [emplois de bureau peu qualifiés sont supprimés chaque jour][3].

Cette perturbation détruira-t-elle l'industrie de l'ingénierie logicielle ? Je ne le pense pas, et je vais vous expliquer pourquoi.

### Voici ce que nous allons aborder :

1.  [Le phénomène du « Vibe Coding »][4]
    
2.  [Comment l'IA a changé le développement logiciel][5]
    
3.  [Le paradoxe de la productivité][6]
    
4.  [Pourquoi les ingénieurs humains restent essentiels][7]
    
5.  [L'IA comme « multiplicateur de capacités »][8]
    
6.  [Compétences critiques pour l'ère de l'IA][9]
    
7.  [La voie à suivre][10]
    

## **Le phénomène du « Vibe Coding »**

Si vous suivez les discussions tech sur X, vous avez probablement vu passer le terme « vibe coding » – la pratique consistant à construire des logiciels par essais et erreurs, intuition et extraits de code générés par l'IA, sans connaissances techniques approfondies.

Les assistants IA modernes tels que GitHub Copilot et ChatGPT peuvent générer des fonctions complètes, corriger des bugs et créer des composants à partir de simples descriptions. Les « Vibe Coders » affirment que les codeurs humains deviendront bientôt obsolètes.

De mon point de vue, ces outils d'IA fonctionnent davantage comme des multiplicateurs de compétences que comme des remplaçants.

Ils aident les développeurs talentueux à travailler plus vite tout en exposant les lacunes de connaissances des programmeurs moins qualifiés. Ceux qui manquent de bases techniques seront confrontés à des problèmes qu'ils ne pourront pas résoudre, mais les ingénieurs qui allient l'assistance de l'IA à une solide expertise pourront être incroyablement productifs.

## **Comment l'IA a changé le développement logiciel**

L'industrie du logiciel a connu une adoption rapide des outils de codage par IA basés sur des Grands Modèles de Langage (LLM) qui analysent les dépôts de code pour prédire et suggérer les étapes suivantes.

Ces outils ont transformé le travail quotidien de programmation en :

-   Suggérant des fonctions complètes au fur et à mesure de la frappe
    
-   Créant des points de terminaison d'API à partir de descriptions en langage naturel
    
-   Éliminant des heures passées sur des modèles de code standards
    
-   Automatisant les tâches de documentation
    
-   Gérant rapidement la logique répétitive
    

Ce passage vers le « vibe coding » accélère la livraison des fonctionnalités. Les programmeurs peuvent désormais construire sans maîtriser chaque détail technique – ils décrivent ce qu'ils veulent, obtiennent des suggestions de l'IA et ajustent jusqu'à ce que le code fonctionne.

Le risque ? Les développeurs déploient souvent du code qu'ils ne peuvent pas expliquer. Ils avancent vite pendant la phase de construction, mais peinent lorsque les systèmes tombent en panne ou doivent être modifiés.

Il existe également une tendance inquiétante de non-programmeurs vendant des applications construites par IA. Récemment, quelqu'un sans aucune base en programmation a lancé un service payant créé entièrement via des prompts IA, pour subir une violation de données quelques jours plus tard lorsque des hackers ont exploité des failles de sécurité basiques. C'est dangereux. Cela a gaspillé l'argent des gens et exposé leurs données. Imaginez si cela devenait courant à cause de la montée des « vibe coders » ?

Pour toute personne envisageant de construire un logiciel sans être ingénieur logiciel, voici quelques niveaux de sécurité de base à prendre en compte :

-   Ajouter l'authentification à vos points de terminaison d'API : des personnes peuvent scanner les ports ouverts et les endpoints sur Internet. S'ils peuvent appeler vos points de terminaison sans être authentifiés, cela peut causer toutes sortes de problèmes.
    
-   Ne stockez pas les mots de passe en texte clair. C'est une erreur majeure. Si vous faites cela et que votre base de données est exposée, ces mots de passe sont visibles par tous. Et soyons réalistes, les gens réutilisent leurs mots de passe, donc ce seront aussi leurs mots de passe pour d'autres sites.
    
-   SSL : assurez-vous que votre site Web est sécurisé et possède un certificat SSL à jour. Transmettre des données en texte clair est dangereux.
    
-   Verrouillez les ports inutilisés : si vous hébergez un service backend, assurez-vous que tous les ports que vous n'utilisez pas sont verrouillés et que personne ne peut s'y connecter.
    
-   Si vous avez des zones où les utilisateurs peuvent uploader des fichiers, limitez les téléchargements à des types de fichiers spécifiques.
    

Ce ne sont là que quelques considérations de sécurité pour votre site ou produit, mais il y en a bien d'autres.

## **Le paradoxe de la productivité**

L'assistance par IA augmente considérablement la production de code – mais le volume n'est pas synonyme de valeur en ingénierie logicielle.

Ces outils excellent dans la syntaxe mais n'ont aucune compréhension de l'architecture système, des enjeux de scalabilité et des exigences de maintenance. Tout comme la vitesse de frappe ne crée pas un meilleur roman, la vitesse de génération de code ne produit pas de meilleurs systèmes logiciels.

L'IA fonctionne pour des fonctions individuelles mais peine avec les décisions architecturales, la planification de la sécurité et les besoins de support à long terme. Sans une révision et une compréhension appropriées, le code généré par IA devient souvent la dette technique et le fardeau de maintenance de demain.

Considérez ce scénario : un développeur implémente un système d'authentification créé par IA qui fonctionne de manière isolée mais provoque des erreurs subtiles lors de l'inscription des utilisateurs au produit. Trouver et corriger ces problèmes d'intégration pourrait prendre plusieurs jours à un personnel expérimenté – annulant ainsi tout gain de temps initial. C'est un chemin rapide vers la perte d'argent et de confiance.

## **Pourquoi les ingénieurs humains restent essentiels**

Bien que les outils d'IA gèrent bien la syntaxe, ils ne peuvent pas :

1.  Planifier des systèmes qui évoluent avec la demande des utilisateurs
    
2.  Créer des pipelines de déploiement et de test fiables
    
3.  Anticiper des cas de défaillance inhabituels mais critiques
    
4.  Faire des compromis intelligents entre performance et coût
    
5.  Trouver des failles de sécurité non évidentes
    

Les excellents ingénieurs pensent au-delà du code. Ils développent des patterns qui aident des équipes entières, choisissent les bonnes technologies et planifient à la fois les scénarios de succès et d'échec.

La création de logiciels implique des compromis complexes : Priorisons-nous la vitesse ou la stabilité ? La flexibilité ou la simplicité ? Ces décisions nécessitent à la fois une expertise technique et une connaissance métier.

Les ingénieurs à plus haute valeur ajoutée avec lesquels je travaille passent plus de temps à réfléchir qu'à taper. Ils se demandent : Comment les exigences vont-elles évoluer ? Quels points de tension pourraient apparaître ? Comment le système se remettra-t-il d'une panne ?

À mesure que la génération de code de base devient largement accessible, votre valeur provient de la compréhension des interactions entre les systèmes. L'avantage concurrentiel appartiendra à ceux qui savent pourquoi certaines approches réussissent, où elles pourraient échouer, et comment construire des solutions résilientes.

Comme mentionné plus haut, il y a des choses que l'IA ne peut pas faire sans une surveillance appropriée.

L'IA peut, par exemple, être excellente pour répondre à des prompts simples afin de créer des solutions à des problèmes bien connus. Si vous utilisez ce prompt, par exemple :

![Prompt: "Create a Python module that will tell you if some input JSON is valid"](https://cdn.hashnode.com/res/hashnode/image/upload/v1747771377197/8aae1332-f852-435a-a724-a1770a4163bf.png)

Voici le code que vous pourriez obtenir :

```
import json

def is_valid_json(input_string: str) -> bool:
    """
    Checks if the input string is valid JSON.

    Args:
        input_string (str): The JSON string to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        json.loads(input_string)
        return True
    except json.JSONDecodeError:
        return False

def main():
    user_input = input("Enter a JSON string to validate: ")
    if is_valid_json(user_input):
        print("✅ The input is valid JSON.")
    else:
        print("❌ The input is NOT valid JSON.")

if __name__ == "__main__":
    main()
```

C'est assez basique.

Je ne demanderais pas, en revanche, à une IA de me construire une plateforme complexe de trading Forex.

![d212d814-7785-4391-8e01-79e80c05da44](https://cdn.hashnode.com/res/hashnode/image/upload/v1747771546630/d212d814-7785-4391-8e01-79e80c05da44.png)

Je vous épargne la lecture de toute la réponse, mais il suffit de dire qu'elle n'a pas été capable de le faire pour moi.

J'ai pensé décomposer cela en un sous-ensemble légèrement plus petit d'une plateforme de trading financier :

![Prompt: "Create me an endpoint for a FIX message for an FX Financial security. Make it in Python and I want to be able to accept J messages. Security is key here, so I need this to be as secure as possible."](https://cdn.hashnode.com/res/hashnode/image/upload/v1747771773603/b65e1a13-97aa-4276-81c7-55303e5a04c6.png)

Maintenant, je l'admets, cela s'en est rapproché. Voici le résultat :

```
from fastapi import FastAPI, Request, HTTPException, Header
from pydantic import BaseModel, Field
from typing import Optional
import hmac
import hashlib
import logging

app = FastAPI()

# === CONFIGURATION ===
SHARED_SECRET = b"super_secure_shared_secret"  # Keep this secure

# === LOGGING SETUP ===
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ems.fix")

# === Pydantic Model for Execution Report (simplified) ===
class ExecutionReport(BaseModel):
    msg_type: str = Field(default="J", const=True)
    cl_ord_id: str  # Tag 11
    order_id: str   # Tag 37
    exec_id: str    # Tag 17
    exec_type: str  # Tag 150
    ord_status: str # Tag 39
    symbol: str     # Tag 55 (e.g., EUR/USD)
    side: str       # Tag 54 (1=Buy, 2=Sell)
    leaves_qty: float  # Tag 151
    cum_qty: float     # Tag 14
    avg_px: float      # Tag 6
    transact_time: str # Tag 60 (ISO8601 string)

# === Helper: HMAC Validator ===
def verify_signature(payload: bytes, signature: str) -> bool:
    computed = hmac.new(SHARED_SECRET, payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed, signature)

# === Endpoint ===
@app.post("/fix/execution-report")
async def receive_execution_report(
    request: Request,
    x_signature: Optional[str] = Header(None)
):
    body = await request.body()

    if not x_signature or not verify_signature(body, x_signature):
        logger.warning("Invalid or missing signature.")
        raise HTTPException(status_code=403, detail="Unauthorized")

    try:
        report_data = ExecutionReport.parse_raw(body)
        logger.info(f"Execution Report received: {report_data.dict()}")
        # ✅ Here, you'd handle order updates, booking, etc.
        return {"status": "ok", "message": "Execution Report received"}
    except Exception as e:
        logger.exception("Invalid payload format.")
        raise HTTPException(status_code=400, detail=f"Invalid FIX message format: {str(e)}")
```

Mais cela est loin de la version finale. Même si vous pouviez utiliser ce code dans votre système de trading, à moins de savoir comment construire et architecturer un système logiciel complet, que faites-vous ensuite ? Vous pouvez dire à vos clients qu'ils peuvent vous envoyer un « ExecutionReport », mais après ?

J'ai lu et entendu les arguments selon lesquels il « suffit d'être meilleur en prompting pour construire des systèmes plus vastes ». Mais où est le bénéfice alors ? La complexité des systèmes de trading financier dépasse l'entendement. Prompter un système assez bien, avec assez d'informations pour le rendre complet, scalable, sécurisé et extensible (sans oublier capable d'être débogué) serait en soi une tâche titanesque. Alors, où gagne-t-on du temps ? Est-ce seulement possible ?

Je n'ai encore vu aucune preuve nulle part que quelqu'un a construit un système aussi complexe sans la supervision d'un humain, et je ne suis pas convaincu que nous en verrons de sitôt.

## **L'IA comme « multiplicateur de capacités »**

Ces outils d'IA aident à amplifier les capacités existantes plutôt qu'à les remplacer. Les développeurs qualifiés deviennent beaucoup plus productifs, tandis que les moins qualifiés génèrent des problèmes plus rapidement.

Les ingénieurs efficaces utilisent l'IA pour :

-   Gérer les tâches d'implémentation basiques
    
-   Créer des frameworks de projet initiaux
    
-   Comparer différentes approches de solution
    
-   Dépasser des problèmes bloquants
    

Pendant ce temps, les développeurs moins capables utilisent l'IA pour masquer leurs lacunes, implémentant des solutions qu'ils ne comprennent pas et ne peuvent pas modifier. Lorsque ces implémentations échouent, ils n'ont pas les connaissances nécessaires pour les corriger de manière indépendante.

Cela creuse l'écart de compétences. Les meilleurs ingénieurs exploitent l'IA pour les tâches mécaniques tout en se concentrant sur une réflexion à plus haute valeur ajoutée. Ceux qui utilisent l'IA comme substitut à l'apprentissage font face à des limites dès qu'ils travaillent au-delà des frontières de connaissances de l'IA.

Un bon exemple de ce pour quoi l'IA est parfaite est la logique de translation :

Disons que j'ai une Dataclass Python représentant un « InternalUser ». J'ai aussi une représentation ORM Django de la même entité. Si je voulais convertir l'une en l'autre, je peux simplement copier les deux représentations dans ChatGPT et lui demander de me créer une fonction de conversion. Notez que la fonction de conversion prend également en compte le fait que les noms de champs ne correspondent pas exactement :

```
@dataclass
class InternalUser:
    id: str
    email: str
    hashed_password: str
    full_name: str
    role: UserRole
    status: AccountStatus
    created_at: datetime
    updated_at: datetime
    address: Optional[Address] = None
    preferences: Preferences = field(default_factory=Preferences)
    login_activity: LoginActivity = field(default_factory=LoginActivity)
    tags: List[str] = field(default_factory=list)
    notes: Optional[str] = None
```

```
class InternalUser(models.Model):
    id = models.CharField(primary_key=True, max_length=100)  # Use UUIDField if preferred
    email = models.EmailField(unique=True)
    hashedPassword = models.CharField(max_length=256)
    fullName = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.USER)
    status = models.CharField(max_length=20, choices=AccountStatus.choices, default=AccountStatus.PENDING)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now=True)

    address = models.OneToOneField(Address, null=True, blank=True, on_delete=models.SET_NULL)
    preferences = models.OneToOneField(Preferences, on_delete=models.CASCADE)
    loginActivity = models.OneToOneField(LoginActivity, on_delete=models.CASCADE)

    tags = models.JSONField(default=list, blank=True)  # List of strings
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.fullName} ({self.email})"
```

```
from typing import Optional
from myapp.models import InternalUser as ORMInternalUser, Address as ORMAddress, Preferences as ORMPreferences, LoginActivity as ORMLoginActivity
from mydataclasses import InternalUser as DCInternalUser  # assuming your dataclass lives here


def convert_internal_user_to_model(dc_user: DCInternalUser) -> ORMInternalUser:
    # Create or update Address if provided
    orm_address: Optional[ORMAddress] = None
    if dc_user.address:
        orm_address = ORMAddress.objects.create(
            street=dc_user.address.street,
            city=dc_user.address.city,
            state=dc_user.address.state,
            postalCode=dc_user.address.postal_code,
            country=dc_user.address.country
        )

    # Create Preferences
    orm_preferences = ORMPreferences.objects.create(
        newsletterOptIn=dc_user.preferences.newsletter_opt_in,
        darkModeEnabled=dc_user.preferences.dark_mode_enabled,
        language=dc_user.preferences.language
    )

    # Create LoginActivity
    orm_login_activity = ORMLoginActivity.objects.create(
        lastLogin=dc_user.login_activity.last_login,
        loginAttempts=dc_user.login_activity.login_attempts,
        lastIpAddress=dc_user.login_activity.last_ip_address
    )

    # Create InternalUser
    orm_user = ORMInternalUser.objects.create(
        id=dc_user.id,
        email=dc_user.email,
        hashedPassword=dc_user.hashed_password,
        fullName=dc_user.full_name,
        role=dc_user.role.value,
        status=dc_user.status.value,
        createdAt=dc_user.created_at,
        updatedAt=dc_user.updated_at,
        address=orm_address,
        preferences=orm_preferences,
        loginActivity=orm_login_activity,
        tags=dc_user.tags,
        notes=dc_user.notes
    )

    return orm_user
```

C'est un exemple basique, mais extrapolez cela à un modèle de données interne complet et vous avez économisé des heures et des heures de code.

Vous pouvez même ensuite lui demander de vous créer les squelettes de fonctions pour les tests :

```
import pytest
from datetime import datetime
from yourmodule.dataclasses import InternalUser, Address, Preferences, LoginActivity, UserRole, AccountStatus
from yourmodule.conversion import dataclass_to_django_internal_user


@pytest.mark.django_db
def test_internal_user_conversion_basic_fields():
    # Test that basic fields (email, name, etc.) are correctly copied
    pass


@pytest.mark.django_db
def test_internal_user_conversion_with_address():
    # Test that address fields are properly mapped to the ORM model
    pass


@pytest.mark.django_db
def test_internal_user_conversion_with_preferences():
    # Test preferences like dark mode, newsletter opt-in, and language
    pass


@pytest.mark.django_db
def test_internal_user_conversion_with_login_activity():
    # Test login attempts, last IP, and last login datetime
    pass


@pytest.mark.django_db
def test_internal_user_conversion_with_tags_and_notes():
    # Test tags list and optional notes field
    pass


@pytest.mark.django_db
def test_internal_user_conversion_with_missing_optional_fields():
    # Ensure None fields like address or lastLogin don’t break conversion
    pass


@pytest.mark.django_db
def test_internal_user_conversion_saves_correctly():
    # Save all related models and main InternalUser model and check database
    pass
```

Maintenant, je ne suggère pas de les prendre tels quels sans ajouter votre propre réflexion à chaque scénario de test possible, mais c'est un excellent début.

Ces « tâches ingrates » n'ont jamais été la raison pour laquelle nous payions les meilleurs ingénieurs. C'étaient simplement des choses qu'ils devaient faire pour accomplir leur travail. Les gens n'appréciaient pas ces tâches. Elles n'étaient pas épanouissantes.

## **Compétences critiques pour l'ère de l'IA**

À mesure que l'IA gère davantage de tâches de codage, les ingénieurs qui réussissent doivent développer des forces dans des domaines où le jugement humain reste essentiel :

La pensée systémique devient la compétence principale – comprendre les interactions entre les composants, identifier les défaillances potentielles et concevoir pour la croissance future. Cette capacité vient de l'expérience, pas du prompting.

Vous devriez développer une expertise dans l'infrastructure et les processus de déploiement. Un logiciel qui fonctionne en développement mais échoue en production n'apporte aucune valeur. Apprenez donc l' [intégration continue][11], les systèmes de [monitoring][12] et les [capacités des plateformes cloud][13].

Vous devriez également maîtriser la [conception d'API][14] – les interfaces entre les systèmes. Des [APIs bien conçues][15] permettent l'indépendance des équipes. De mauvaises interfaces créent des goulots d'étranglement affectant tout le monde.

Une autre compétence clé est d'être capable d'intégrer la sécurité tout au long du processus de développement. Un seul oubli peut entraîner des violations, nuisant à la fois à la confiance des clients et à la réputation de l'entreprise.

Assurez-vous de développer vos compétences en communication pour des publics techniques et non techniques. Vous devrez expliquer clairement des décisions complexes à différents groupes de parties prenantes.

Et étudiez comment les outils d'IA fonctionnent pour comprendre leurs limites et leurs forces, vous permettant de les utiliser le plus efficacement possible.

Pour les développeurs seniors, le mentorat devient de plus en plus important. Les nouveaux ingénieurs ont besoin de conseils sur l'utilisation responsable de l'IA – savoir quand accepter les suggestions et quand les remettre en question.

## **La voie à suivre**

Le domaine du logiciel entre dans une transition majeure. L'IA générera plus de code plus rapidement, transformant les pratiques de développement. Ce changement présente à la fois des opportunités et des défis.

Les postes les plus précieux iront à ceux qui sont bons dans les tâches que les machines ne peuvent pas gérer. Ces ingénieurs détermineront quoi construire, comment le concevoir et comment équilibrer les contraintes techniques avec les objectifs commerciaux.

Le « vibe coding » est une technique utile pour des besoins spécifiques – comme construire rapidement des composants standards. Mais il échoue en tant que stratégie globale pour le développement de systèmes complexes.

Les ingénieurs qualifiés progresseront en déléguant le travail de routine à l'IA tout en s'attaquant à des problèmes plus difficiles. Les ingénieurs moins qualifiés auront du mal à mesure que les lacunes dans leurs connaissances fondamentales deviendront apparentes.

En ce qui concerne l'apprentissage de l'utilisation efficace de l'IA, faites également preuve de prudence et de jugement lorsque vous suivez les conseils de personnes en ligne. C'est encore un domaine assez nouveau qui change constamment.

Des gens en ligne partagent des « prompts gratuits » pour générer du code. Ces prompts peuvent être excellents ou problématiques. Ils ont peut-être fonctionné au moment où ils ont été utilisés, mais les modèles d'IA ont pu changer et produire des résultats différents aujourd'hui. Soyez prudent et utilisez votre meilleur jugement.

L'avenir appartient à ceux qui considèrent l'IA comme un outil collaboratif plutôt que comme un remplaçant. Le développement de logiciels reste fondamentalement dirigé par l'humain, désormais soutenu par une assistance de plus en plus puissante.

_Pendant son temps libre, Ben écrit sur son blog technique_ [_Just Another Tech Lead_][16] _et gère un site sur le SEO,_ [_SmoothSEO_][17]_._

[1]: https://www.smoothseo.co/blog/misc/what-the-numbers-say-about-ais-growing-role-in-search/
[2]: https://www.axios.com/2022/03/28/automation-long-haul-truckers-jobs
[3]: https://news.sky.com/story/ai-risks-up-to-eight-million-uk-job-losses-with-low-skilled-worst-hit-report-warns-13102214
[4]: #heading-le-phenomene-du-vibe-coding
[5]: #heading-comment-l-ia-a-change-le-developpement-logiciel
[6]: #heading-le-paradoxe-de-la-productivite
[7]: #heading-pourquoi-les-ingenieurs-humains-restent-essentiels
[8]: #heading-l-ia-comme-multiplicateur-de-capacites
[9]: #heading-competences-critiques-pour-l-ere-de-l-ia
[10]: #heading-la-voie-a-suivre
[11]: https://www.freecodecamp.org/news/learn-continuous-integration-delivery-and-deployment/
[12]: https://www.freecodecamp.org/news/how-to-set-up-monitoring-for-nodejs-applications-using-elastic/
[13]: https://www.freecodecamp.org/news/beginners-guide-to-cloud-computing-with-aws/
[14]: https://www.freecodecamp.org/news/rest-api-design-best-practices-build-a-rest-api/
[15]: https://www.freecodecamp.org/news/design-an-api-application-program-interface/
[16]: https://justanothertechlead.com/
[17]: https://www.smoothseo.co