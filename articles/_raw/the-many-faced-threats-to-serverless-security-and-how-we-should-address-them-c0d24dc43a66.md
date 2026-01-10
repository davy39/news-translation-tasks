---
title: The many-faced threats to Serverless security, and how we should address them
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-14T09:30:21.000Z'
originalURL: https://freecodecamp.org/news/the-many-faced-threats-to-serverless-security-and-how-we-should-address-them-c0d24dc43a66
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lz4OEP6QW6duz3-mxrByWg.png
tags:
- name: aws lambda
  slug: aws-lambda
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Yan Cui

  Threats to the security of our server­less appli­ca­tions take many forms. Some
  are old foes we have faced before. Some are new. And some have taken on new forms
  in the server­less world.

  As we adopt the server­less par­a­digm, we del­e­ga...'
---

By Yan Cui

Threats to the security of our server­less appli­ca­tions take many forms. Some are old foes we have faced before. Some are new. And some have taken on new forms in the server­less world.

As we adopt the server­less par­a­digm, we del­e­gate even more operational respon­si­bil­i­ties to our cloud providers. With AWS Lambda, you no longer have to con­fig­ure AMIs, patch the OS, and install monitoring dae­mons. AWS takes care all that for you.

What does this mean for the [**Shared Respon­si­bil­i­ty Mod­el**](https://aws.amazon.com/compliance/shared-responsibility-model/) that has long been the cor­ner­stone of secu­ri­ty in the AWS cloud?

![Image](https://cdn-media-1.freecodecamp.org/images/1*6kr67q2FRqMCmJH83DSZpA.png)

### Protection from attacks against the OS

AWS takes over the respon­si­bil­i­ty for main­tain­ing the host OS as part of their core com­pe­ten­cy. This alleviates you of the rig­or­ous task of apply­ing all the latest secu­ri­ty patch­es. This is something most of us don’t do a good enough job of, as it’s not our pri­ma­ry focus.

In doing so, it pro­tects us from attacks against known vul­ner­a­bil­i­ties in the OS and pre­vents attacks such as [Wan­naCry](https://en.wikipedia.org/wiki/WannaCry_ransomware_attack).

By remov­ing long-lived servers from the pic­ture, we are also removing the threats posed by com­pro­mised servers that live in our envi­ron­ment for a long time.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yxyS9qbLUBOs_28hl5Zj6g.png)
_Wan­naCry hap­pened because the MS17–017 secu­ri­ty patch was not applied to the affect­ed hosts._

How­ev­er, it is still our respon­si­bil­i­ty to patch our appli­ca­tion and address vul­ner­a­bil­i­ties that exist in our code and our depen­den­cies.

### OWASP top 10 is still as relevant as ever

![Image](https://cdn-media-1.freecodecamp.org/images/1*A-fSGp4uquJNZce9n4-lQg.png)
_Aside from a few reclas­si­fi­ca­tions, the OWASP top 10 list has large­ly stayed the same in 7 years._

A glance at the [OWASP top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project) for 2017 shows us famil­iar threats. Injec­tion attacks, Broken Authentication, and Cross-Site Script­ing (XSS) still occupy the top spots seven years on.

#### A9 — Components with Known Vulnerabilities

When the folks at [Snyk](https://snyk.io/) looked at a dataset of 1792 data breach­es in 2016, they found that [**12 of the top 50** **data breach­es**](https://snyk.io/blog/owasp-top-10-breaches) were caused by appli­ca­tions using com­po­nents with known vul­ner­a­bil­i­ties.

Fur­ther­more, [77% of the top 5000 URLs from Alexa include at least one vul­ner­a­ble library](https://snyk.io/blog/77-percent-of-sites-use-vulnerable-js-libraries). This is less sur­pris­ing than it first sounds when you con­sid­er that some of the most pop­u­lar front-end js frame­works — eg. [jQuery](https://snyk.io/vuln/npm:jquery), [Angu­lar](https://snyk.io/vuln/npm:angular) and [React](https://snyk.io/vuln/npm:react) — all had known vul­ner­a­bil­i­ties. It high­lights the need to con­tin­u­ous­ly update and patch your depen­den­cies.

Unlike OS patch­es, which are stand­alone, trust­ed and easy to apply. S**ecu­ri­ty updates to 3rd par­ty depen­den­cies are often bun­dled with fea­ture and API changes that need to be inte­grat­ed and test­ed**. It makes our life as devel­op­ers dif­fi­cult. It’s yet anoth­er thing we have to do when we’re work­ing over­time to ship new fea­tures.

And then there’s the mat­ter of tran­sient depen­den­cies. If these tran­sient depen­den­cies have vul­ner­a­bil­i­ties, then you too are vul­ner­a­ble through your direct depen­den­cies.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bB9XkUioCbd7TUtM8vQdVQ.png)
_[https://david-dm.org/request/request?view=tree](https://david-dm.org/request/request?view=tree" rel="noopener" target="_blank" title=")_

Find­ing vul­ner­a­bil­i­ties in our depen­den­cies is hard work and requires constant dili­gence. Which is why ser­vices such as [Snyk](https://snyk.io/) is so use­ful. It even comes with a built-in [inte­gra­tion with Lamb­da](https://snyk.io/docs/aws-lambda), too!

#### Attacks against NPM publishers

![Image](https://cdn-media-1.freecodecamp.org/images/0*fyWZzYs7lD1pODKQ.gif)
_What if the author/publisher of your 3rd party dependency is not who you think they are?_

Last year, a secu­ri­ty boun­ty hunter [man­aged to gain direct push rights to **14% of NPM pack­ages**](https://github.com/ChALkeR/notes/blob/master/Gathering-weak-npm-credentials.md). The list of affect­ed pack­ages include some big names too: `debug`, `request`, `react`, `co`, `express`, `moment`, `gulp`, `mongoose`, `mysql`, `bower`, `browserify`, `electron`, `jasmine`, `cheerio`, `modernizr`, `redux` and many more. In total, these pack­ages account for **20% of the total num­ber of month­ly down­loads from NPM**.

_Let that sink in for a moment._

Did he use sophis­ti­cat­ed meth­ods to cir­cum­vent NPM’s secu­ri­ty?

Nope, it was a com­bi­na­tion of **brute force** and using **known** account and credential leaks from a num­ber of sources includ­ing Github. In oth­er words, any­one could have pulled these off with very lit­tle research.

It’s hard not to feel let down by these pack­age authors when so many dis­play such a cav­a­lier atti­tude towards secur­ing access to their NPM accounts.

> 662 users had pass­word «`123456`», 174 — «`123`», 124 — «`password`».

> 1409 users (1%) used their user­name as their pass­word, in its orig­i­nal form, with­out any mod­i­fi­ca­tions.

> 11% of users reused their leaked pass­words: 10.6% — direct­ly, and 0.7% — with minor mod­i­fi­ca­tions.

As I [demon­strat­ed in my talk on Server­less secu­ri­ty](https://youtu.be/jUhiPj6h_L8?t=794), you can steal tem­po­rary AWS cre­den­tials by adding a few lines of code.

Imag­ine, then, a sce­nario where an attack­er had man­aged to gain push rights to 14% of all NPM pack­ages. He could pub­lish a patch update to all these pack­ages and steal AWS cre­den­tials at a mas­sive scale.

The stakes are high and it’s pos­si­bly the biggest secu­ri­ty threat we face in the server­less world. And, it also impacts applications running inside EC2 or containers.

The prob­lems and risks with pack­age man­age­ment are not spe­cif­ic to the Node.js ecosys­tem. I have spent most of my career work­ing with .Net and now Scala, and pack­age man­age­ment has been a chal­lenge every­where. **We need package authors to exer­cise due diligence towards the security of their accounts**.

#### A1 — Injection & A3 — XSS

SQL injec­tion and oth­er forms of injec­tion attacks are still pos­si­ble in the server­less world. As are Cross-Site Script­ing (XSS) attacks.

Even if you’re using NoSQL data­bas­es you might not be safe from injec­tion attacks either. Mon­goDB, for instance, expos­es a num­ber of [attack vec­tors](https://zanon.io/posts/nosql-injection-in-mongodb) through its query APIs.

DynamoDB’s more rigid API makes an injection attack harder. But you’re still open to oth­er forms of exploits. For example, XSS and leaked cre­den­tials which grant attack­er access to DynamoDB tables.

Nonethe­less, you should always san­i­tize user inputs, as well as the out­put from your Lamb­da func­tions.

#### A6 — Sensitive Data Exposure

Along with servers, web frame­works are also redundant when you move to the server­less par­a­digm. These web frame­works have served us well for many years. But they also hand­ed us a loaded gun we can shot our­selves in the foot with.

_Troy Hunt_ [demon­strat­ed](https://skillsmatter.com/skillscasts/9954-london-dot-net-june-meetup) how we can acci­den­tal­ly expose all kinds of sen­si­tive data by leav­ing direc­to­ry list­ing options ON. From web.config con­tain­ing cre­den­tials (at 35:28) to SQL back­ups files (at 1:17:28)!

With _API Gate­way_ and _Lamb­da_, acci­den­tal expo­sures like this are very unlike­ly. Because direc­to­ry list­ing becomes a “fea­ture” you’d have to imple­ment your­self. It forces you to make a con­scious decision about when to sup­port direc­to­ry list­ing, and the answer is likely _nev­er_.

### IAM

If your func­tions are com­pro­mised, the next line of defense is to restrict what the com­pro­mised func­tions can do.

This is why you need to apply the **Least Priv­i­lege Prin­ci­ple** when con­fig­ur­ing Lamb­da per­mis­sions.

In the [Serverless](https://serverless.com/framework/) frame­work, the default behav­iour is to use the same IAM role for all func­tions in the ser­vice.

How­ev­er, the `serverless.yml` spec allows you to spec­i­fy a [dif­fer­ent IAM role per func­tion](https://serverless.com/framework/docs/providers/aws/guide/iam/#custom-iam-roles-for-each-function). But it involves a lot more devel­op­ment effort and adds enough fric­tion that almost no one does this.

Thankfully, _Guy Lichtman_ created a plugin for the _Serverless_ framework called [serverless-iam-role-per-function](https://github.com/functionalone/serverless-iam-roles-per-function). This plugin makes applying per function IAM roles much easier. Follow the instructions on the Github page and give it a try yourself.

![Image](https://cdn-media-1.freecodecamp.org/images/1*T78Ys1ipg_dEFe2_K63R5A.png)
_You should apply per-func­tion IAM poli­cies._

#### IAM policy not versioned with Lambda

A short­com­ing with Lamb­da and IAM con­fig­u­ra­tion is that IAM poli­cies are not ver­sioned with the Lamb­da func­tion.

If you have mul­ti­ple ver­sions of the same func­tion in active use (per­haps with dif­fer­ent alias­es), then it becomes prob­lem­at­ic to add or remove per­mis­sions:

* Adding per­mis­sions to a new ver­sion allows older ver­sions more access than they need
* Remov­ing per­mis­sions from a new ver­sion can break older versions that still need those per­mis­sions

Before 1.0, this was a common problem with the _Serverless_ framework because it used aliases to implement stages. Since 1.0, this is no longer a problem, because each stage is deployed as a sep­a­rate function. For example:

* `service-function-dev`
* `service-function-staging`
* `service-function-prod`

This means only one version of each function is active at any moment in time. Except when you use aliases during a [canary deployment](https://aws.amazon.com/blogs/compute/implementing-canary-deployments-of-aws-lambda-functions-with-alias-traffic-shifting/).

**Account** **lev­el iso­la­tion** can also help mit­i­gate the prob­lems of adding/removing per­mis­sions. This iso­la­tion also helps **compartmentalize secu­ri­ty breach­es**. For example, a compromised func­tion in a non-pro­duc­tion account can­not be used to gain access to pro­duc­tion data.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2lyB5B4OydPapmdqbozTSQ.png)
_We can apply the same idea of bulk­heads (which has been pop­u­larised in the microser­vices world by Michael Nygard’s “Release It”) and com­part­men­talize secu­ri­ty breach­es at an account lev­el._

#### Delete unused functions

One of the ben­e­fits of the server­less par­a­digm is that you don’t pay for func­tions when they’re not used.

The flip side is that you have less incentive to remove unused functions since they don’t cost you anything. How­ev­er, these func­tions still exist as attack sur­faces. They are also more dangerous than active­ func­tions because they’re less like­ly to be updat­ed and patched. Over time, these unused func­tions can become a hotbed for known vul­ner­a­bil­i­ties that attack­ers can exploit.

Lambda’s doc­u­men­ta­tion also cites this as one of the [best prac­tices](http://docs.aws.amazon.com/lambda/latest/dg/best-practices.html).

> Delete old Lamb­da func­tions that you are no longer using.

### The changing face of DoS attacks

With AWS Lamb­da, you are far more like­ly to scale your way out of a Denial-of-Service (DoS) attack. How­ev­er, scal­ing your server­less archi­tec­ture aggressively to fight a DoS attack with brute force has a sig­nif­i­cant cost implication.

No won­der peo­ple start­ed call­ing DoS attacks against server­less appli­ca­tions **Denial of Wal­let (DoW)** attacks!

> “But you can just throt­tle the no. of con­cur­rent invo­ca­tions, right?”

Sure, and you end up with a DoS prob­lem instead… it’s a lose-lose sit­u­a­tion.

Of course, there is [AWS Shield](https://aws.amazon.com/shield/). For a flat fee, AWS Shield Advanced gives you payment pro­tec­tion in the event of a DoS attack. But at the time of writ­ing, this pro­tec­tion does not cov­er Lamb­da costs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XcX3b03mcFcmyVfENHbYPg.png)
_For a month­ly flat fee, AWS Shield Advanced gives you cost pro­tec­tion in the event of a DoS attack, but that pro­tec­tion does not cov­er Lamb­da yet._

Also, Lamb­da has an [**at-least-once** invo­ca­tion pol­i­cy](http://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html). [Accord­ing to the folks at Sun­Gard](https://blog.sungardas.com/CTOLabs/2017/06/run-lambda-run/), this can result in up to three (suc­cess­ful) invo­ca­tions. From the arti­cle, the report­ed rate of mul­ti­ple invo­ca­tions is extreme­ly low, at 0.02%. But one won­ders if the rate is tied to the load and might man­i­fest itself at a much high­er rate dur­ing a DoS attack.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HUDZHb1Ky4S-kQuThh1-Lg.png)
_Tak­en from the “Run, Lamb­da, Run” arti­cle men­tioned above._

Fur­ther­more, you need to con­sid­er how Lamb­da [retries failed invo­ca­tions](http://docs.aws.amazon.com/lambda/latest/dg/retries-on-errors.html) by an [asyn­chro­nous source](http://docs.aws.amazon.com/lambda/latest/dg/invoking-lambda-function.html). For example, S3, SNS, SES, and Cloud­Watch Events.

Offi­cial­ly, these invo­ca­tions are retried twice before they’re sent to the assigned Dead Letter Queue (DLQ) if one is configured. How­ev­er, an [analy­sis](https://engineering.opsgenie.com/aws-lambda-performance-series-part-2-an-analysis-on-async-lambda-fail-retry-behaviour-and-dead-b84620af406) by Ops­Ge­nie showed that the number of retries can go up to as many as 6 before the invo­ca­tion is sent to the DLQ.

If the DoS attacker is able to trigger failed async invocations then they can **magnify the impact of their attack**.

For example, if your application allows the client to update a file to S3 for processing. Then the attacker can DoS you by uploading large numbers of invalid files that will cause your functions to error and retry.

All these add up to the poten­tial for the actu­al number of Lamb­da invocations to explode dur­ing a DoS attack. As we dis­cussed ear­li­er, while your infra­struc­ture might be able to han­dle the attack, **can your wal­let stretch to the same extent**? Should you allow it to?

### Securing external data

![Image](https://cdn-media-1.freecodecamp.org/images/1*PlSruVB-6fWW2XyO9z-q0w.png)
_Just a hand­ful of the places you could be stor­ing state out­side of your state­less Lamb­da func­tion._

Due to the ephemer­al nature of Lamb­da func­tions, chances are all your functions are state­less. More than ever, states are stored in exter­nal sys­tems and we need to secure them both **at rest** and **in-tran­sit**.

Com­mu­ni­ca­tion to all AWS ser­vices happens via HTTPS and every request is signed and authen­ti­cat­ed. A hand­ful of AWS ser­vices also offer serv­er-side encryp­tion for your data at rest. For example, [S3](http://amzn.to/1N3Twb8), [RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html) and [Kine­sis streams](http://amzn.to/2tgvFR2) spring to mind. Lamb­da also has built-in inte­gra­tion with KMS to encrypt envi­ron­ment vari­ables.

Recently DynamoDB has also announced [support for encryption at-rest](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EncryptionAtRest.html).

The same dili­gence needs to be applied when stor­ing sen­si­tive data in services/databases that do not offer built-in encryp­tion. In the case of a data breach, it pro­vides anoth­er lay­er of pro­tec­tion for your users’ data.

_We owe our users that much_.

Use secure trans­port when trans­mit­ting data to and from ser­vices (both exter­nal and inter­nal ones). If you’re build­ing APIs with API Gate­way and Lamb­da then you’re forced to use HTTPS by default, which is a good thing. How­ev­er, API Gate­way endpoints are always public, you need to take the nec­es­sary pre­cau­tions to secure access to inter­nal APIs.

You should use [IAM roles](http://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html) to protect internal APIs. It gives you [fine-grained con­trol](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-iam-policy-examples-for-api-execution.html) over who can invoke which actions on which resources. Using IAM roles also spares you from awk­ward con­ver­sa­tions like this:

_“It’s X’s last day, he prob­a­bly has our API keys on his lap­top some­where, should we rotate the API keys just in case?”_

_“Hmm.. that’d be a lot of work, X is trust­wor­thy, he’s not gonna do any­thing.”_

_“Ok… if you say so… (secret­ly prays that X doesn’t lose his lap­top or devel­op a belat­ed grudge against the com­pa­ny)”_

For­tu­nate­ly, this can be [eas­i­ly con­fig­ured](https://serverless.com/framework/docs/providers/aws/events/apigateway#http-endpoints-with-aws_iam-authorizers) using the `Serverless` frame­work.

### Leaked credentials

![Image](https://cdn-media-1.freecodecamp.org/images/1*8wH4JqfvBQmdcQpaROJCog.png)
_Don’t become an unwill­ing bit­coin min­er._

The inter­net is full of hor­ror sto­ries of devel­op­ers rack­ing up a mas­sive AWS bill after their leaked cre­den­tials are used to mine bit­coins. For every such sto­ry, many more have been affect­ed but chose to stay silent. For the same reason, many secu­ri­ty breach­es are not disclosed pub­licly as com­pa­nies do not want to lose face.

Even with­in my small social cir­cle, I know of two such inci­dents. Nei­ther were made pub­lic and both result­ed in over $100k worth of dam­ages. For­tu­nate­ly, in both cas­es AWS agreed to cov­er the cost.

AWS scans pub­lic Github repos for active AWS cre­den­tials and tries to alert you as soon as pos­si­ble. But even if your cre­den­tials were public for a brief moment, it might not escape the watch­ful gaze of attack­ers. Plus, they still exist in Git com­mit his­to­ry unless you rewrite the his­to­ry, too. If your credentials came into the public domain then it’s best to deac­ti­vate the cre­den­tials as soon as possible.

A good approach to pre­vent AWS cre­den­tial leaks is to use Git pre-com­mit hooks as out­lined by [this post](https://www.unixdaemon.net/cloud/preventing-aws-creds-in-git-with-pre-commit/).

From what I hear, attackers are most likely to launch EC2 instances in the Sao Paulo and Tokyo regions. You can use CloudWatch event patterns and Lambda to alert you when there are EC2 API calls in regions you’re not using. That way, you can at least react more quickly when your credentials are leaked.

### Conclusions

We looked at a num­ber of secu­ri­ty threats to our server­less appli­ca­tions in this post. Many of them are the same threats that have plight­ed the soft­ware indus­try for years. All the OWASP top 10 still apply to us, includ­ing SQL, NoSQL, and oth­er forms of injec­tion attacks.

Leaked AWS cre­den­tials remain a major issue and can impact any organ­i­sa­tion that uses AWS. Whilst there are quite a few pub­licly report­ed inci­dents, I have a strong feel­ing that the actu­al number of inci­dents are much much high­er.

We are still respon­si­ble for secur­ing our users’ data both at rest as well as in-tran­sit. API Gate­way is always pub­licly acces­si­ble, so we need to take the nec­es­sary pre­cau­tions to secure access to our inter­nal APIs, prefer­ably with IAM roles. IAM offers fine-grained con­trol over who can invoke which actions on your API resources, and make it easy to man­age access when employ­ees come and go.

On a pos­i­tive note, hav­ing AWS take over the respon­si­bil­i­ty for the secu­ri­ty of the host OS gives us a number of secu­ri­ty ben­e­fits:

* Pro­tec­tion against OS attacks, because AWS can do a much bet­ter job of patch­ing known vul­ner­a­bil­i­ties in the OS
* Host OSs are ephemer­al which means no long-lived com­pro­mised servers

With API Gateway and Lambda, you don’t need web frameworks to create an API anymore. Without web frameworks, there is no easy way to support directory listing. But, that’s a good thing, because it makes a directory listing a concise design decision. No more accidental exposure of sensitive data through misconfiguration.

DoS attacks have tak­en a new form in the server­less world. While you’re able to scale your way out of an attack, it’ll still hurt you in the wal­let instead. Lamb­da costs incurred dur­ing a DoS attack is **not** **cov­ered** by _AWS Shield Advanced_ at the time of writ­ing.

Mean­while, some new attack sur­faces have emerged with AWS Lamb­da:

* Func­tions are often over-per­mis­sioned. A com­pro­mised func­tion can do more harm than it might oth­er­wise.
* Unused func­tions are often left around for a long time, because there is no cost penalty. But attack­ers can exploit them. They’re also more like­ly to con­tain known vul­ner­a­bil­i­ties since they’re not actively maintained.

Above all, the most wor­ri­some threat for me are attacks against the pack­age authors them­selves. Many authors do not take the secu­ri­ty of their accounts seri­ous­ly. This endan­gers them­selves as well as the rest of the com­mu­ni­ty that depends on them. It’s difficult to guard against such attacks and erodes one of the strongest aspect of any soft­ware ecosys­tem — the com­mu­ni­ty behind it.

Once again, peo­ple have proven to be the weak­est link in the secu­ri­ty chain.

