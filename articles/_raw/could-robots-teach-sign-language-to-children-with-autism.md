---
title: I helped build a robot that teaches sign language to children with Autism.
  This is what I learned.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-16T15:16:40.000Z'
originalURL: https://freecodecamp.org/news/could-robots-teach-sign-language-to-children-with-autism
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/back-1.png
tags:
- name: Autism
  slug: autism
- name: education
  slug: education
- name: educational technology
  slug: educational-technology
- name: robotics
  slug: robotics
seo_title: null
seo_desc: "By Minja Axelsson\nIn Spring 2018, I conducted a pilot study of a robot\
  \ teaching sign language to children with autism. This blog post reflects on the\
  \ results of the study, and our team’s process of designing the robot. \nRobotics,\
  \ Sign Language, and C..."
---

By Minja Axelsson

In Spring 2018, I conducted a pilot study of a robot teaching sign language to children with autism. This blog post reflects on the results of the study, and our team’s process of designing the robot. 

### Robotics, Sign Language, and Children with Autism

To start with, let’s answer the first big question: **Why use a robot in autism therapy?** [People with autism have an attention preference to objects over people](http://ekirjasto.kirjastot.fi/ekirjat/autismin-kirjo-ja-kuntoutus), and [children with autism have shown more interest toward therapy when it involves technological or robotic components](https://www.researchgate.net/profile/Janek_Dubowski/publication/228364332_Does_appearance_matter_in_the_interaction_of_children_with_autism_with_a_humanoid_robot_Interact_Stud/links/54b7a0970cf2bd04be33b122/Does-appearance-matter-in-the-interaction-of-children-with-autism-with-a-humanoid-robot-Interact-Stud.pdf). Additionally, a [robot’s operation can be strictly controlled, which can make therapy less overwhelming for autistic people](https://ri.cmu.edu/pub_files/2009/1/fulltext.pdf).

Then, the second big question: **Why teach sign language to children with autism?** People with Autism Spectrum Disorder (ASD) experience problems with communication: [40–50% of people with ASD are functionally mute in adulthood](https://books.google.fi/books?hl=en&lr=&id=0Smd-xouZjYC&oi=fnd&pg=PA3&dq=Bogdashina,+O.+(2004).+Communication+issues+in+autism+and+Asperger+syndrome:+Do+we+speak+the+same+language%3F.+Jessica+Kingsley+Publishers&ots=FBSfAPlA_z&sig=uyC0Dms-31cQRue-wilVK5SUQ-w&redir_esc=y#v=onepage&q=Bogdashina%2C%20O.%20(2004).%20Communication%20issues%20in%20autism%20and%20Asperger%20syndrome%3A%20Do%20we%20speak%20the%20same%20language%3F.%20Jessica%20Kingsley%20Publishers&f=false). To mitigate this, they use Augmentative and Alternative Communication (AAC) methods. [Assistive sign language — a simplified form of sign language — is the most common form of AAC](https://www.worldcat.org/title/introduction-to-augmentative-and-alternative-communication-sign-teaching-and-the-use-of-communication-aids-for-children-adolescents-and-adults-with-developmental-disorders/oclc/44603909). Other common AAC forms are symbolic pictures and photographs.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/symbolic.png)
_An example of a symbolic picture communication system used by children with autism: “We do assignments.”_

The idea to combine these two domains — robotics for children with ASD, and sign language for children with ASD — originally came from [Satakunta health care district](https://www.satasairaala.fi/). Satakunta is a small region in South-Western Finland, with a population of 225 000 people. The quality manager at the district had read about [a robot being used to teach sign language to neurotypical children](https://link.springer.com/article/10.1007/s12369-015-0307-x), and wanted to investigate the same method with autistic children.

Satakunta found out that the company I work for ([Futurice](https://www.futurice.com/)) had built a humanoid robot. They reached out, and we assembled a cross-disciplinary team that would re-design and modify Futurice’s humanoid robot to fit this purpose. Our team had three roboticists from Futurice, and three experts of autism treatment from Satakunta: a neuropsychologist, a speech therapist, and the quality manager.

### How Should We Design the Robot?

The humanoid robot Futurice had built was an InMoov robot. The [InMoov is designed by French sculptor Gaël Langevin](http://inmoov.fr/). He has made the schematics and software of the robot open source and available to anyone online. 

Using these, Futurice built its own InMoov. Satakunta wanted to use the InMoov due to its nimble hands that enable it to sign. Its human-like appearance was also an advantage: one of Satakunta’s neuropsychologists thought that a human-resembling robot would be best for this solution.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/inmoov.jpeg)
_The original form of the open source humanoid robot InMoov, designed by Gaël Langevin. Image Wikimedia Commons._

However, the InMoov was not ready as it was. To make the robot be suitable for children with autism, we needed to modify its form, behaviour, interactions and environment. 

My job was to design these four dimensions of the robot. I also needed to design the human-robot interaction study where children would meet and sign with the robot. Luckily, the open source nature of the robot’s software and hardware would make it relatively easy to make the necessary modifications.

We wanted to take the characteristics of ASD into account while designing the robot. ASD is characterized by problems with communication and language, problems with social behaviour, inflexibility of routines, and problems forming a holistic perception of surroundings. However, autism is a spectrum, so these characteristics present differently in different people. Due to different presentations, we knew we couldn’t design a robot that would benefit everyone. Nevertheless, we wanted to find the best solution that would serve the most children with ASD.

During the project, the team created five design guidelines for the robot, which would tailor its design for autistic children. For example, the concern that a child might get distracted during the experiment was brought up by the autism specialists. The team agreed that to avoid confusing the child, the robot’s behaviour should be consistent and structured. This was defined as the guideline: “consistent, structured, simple behaviour”. To follow the guideline, the speech therapist and I created strict script of the robot’s and child’s interaction. All five guidelines were formulated in a similar manner in co-design discussions.

#### Design guidelines for a robot to be used with autistic children:

1. Simple form
2. Consistent, structured, simple behaviour
3. Positive, supportive, rewarding experience and environment
4. Modular complexity
5. Modularity specific to child’s preferences

The design guidelines helped the team maintain a logical and uniform design for the robot, and formed a baseline for all decisions made during the design process.

### Embedded Ethics

While the team was discussing the design of the robot and the experiments, several ethical considerations were raised. These ethical considerations were embedded into the finalized robot.

**Physical safety** — Users can be potentially pinched or crushed by a robot. To mitigate this concern, we decided to stop the children from touching the robot during interactions. To accomplish this, we decided to have the speech therapist in the room with the child to stop them from approaching the robot, if need be.

**Data security** — It is paramount that the user’s data stay secure, especially in health care applications. Here, we decided to keep all data of the children attending the study encrypted. We also did not record any unnecessary data.

**Appropriate behaviour enforcement** — People can learn bad manners from robots. For example, [children have forgotten to use polite language such as “please” and “thank you” after interacting with the voice agent Alexa](https://thriveglobal.com/stories/artificial-intelligence-alexa-impact-children-expert-opinion-tips/). Alexa does not explicitly ask for polite language, causing people to behave badly toward it. In this case, we didn’t want children to learn to treat the robot badly, and potentially generalize that bad behaviour to people. We decided that the therapist would intervene in all bad behaviour toward the robot.

**Equality across users** — Artificial intelligence algorithms have been shown to be racist or sexist in the past (e.g. [COMPAS, a recidivism rate prediction algorithm used in USA, was biased toward African-Americans](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)). If a robot uses algorithms to function, designers of the algorithm need to be careful. Another thing to consider is the robot’s form. Robot designs have been shown to reinforce gender stereotypes, with “genius” robots often labeled as male, and “service” robots as female. In our case, we wanted to design a robot that was gender neutral, so that each child participating in the study could feel welcome. To do this, the robot was given no gender signifiers.

**Transparency** — If the user understands how the robot operates and makes decisions, they can calibrate their trust level in it. In our case, we decided to inform the children and their companions of the robot’s teleoperated nature at the end of the study. This way they could avoid forming false assumptions about the state of robotics today, and how it can be applied to autism therapy.

**Emotional consideration** — Research has shown that humans treat robots as is they were alive, even when they clearly aren’t. People form emotional bonds with robots. This should be taken into account in the design: how strong a bond is desirable for this use case? In this case, we didn’t want the child or their companions to think that the robot was replacing the bond between the child and the therapist. To ensure this, the speech therapist would stay in the room with the child the entire time.

### A Balancing Act

Building complex technology (robotics) for a complex domain (autism therapy) is difficult. The problem space was unintuitive to both sides of the team: the autism specialists weren’t familiar with technical limitations, and the roboticists had no knowledge of the user group. 

Designing was a balancing act: a seemingly small tweak in the design could result in a high amount of technical work. And vice versa, some changes that were significant design-wise could be easy to implement technically. 

This is where I spent most of my time — harmonizing the team’s different viewpoints into a good design that would be realistic to execute in our time frame of 6 months. Together we made a series of decisions balancing user experience and technical complexity.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/robo.png)
_The final InMoov with modifications: new Ada hands, lights attached to its right hand, and a screen on its chest._

When designing a social robot, there are a lot of moving parts (both literally and figuratively). The robot’s features all affect each other. The robot’s operation context affects how it behaves, which affects how it interacts with the user, which affects what its form is like. Prying these design considerations apart and crystallizing them into distinct and implementable technical tasks was challenging.

Modifying the robot from its original form took 4.5 months (the original build had been assembled in 9 months). All our modifications followed the design guidelines: for example, we changed the robot’s human-like voice to robotic, to give it a “simple form” (guideline 1).

To make the InMoov a better sign language teacher, we made a few big adjustments. We gave it new [Ada hands, designed by Open Bionics](https://openbionicslabs.com/obtutorials/ada-v1-assembly), and built by [Metropolia University of Applied Sciences](https://www.metropolia.fi/en/). We also embedded a screen into its chest, and lights onto its arms. The screen was added to provide another mode of communication (photographs are often used in AAC), and lights were added to capture the child’s attention.

### 10 Children and a Robot

10 children took part in the experiments. Some came with their parents, some came with other support people. Two roboticists (me included) were in the room adjacent to the experiment room, operating the robot and observing the experiment through a camera feed. A third roboticist was present to solve any problems that might emerge. The speech therapist was in the experiment room with each child, facilitating the interaction between the child and the robot, and intervening when needed.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/signs.png)
_The 9 words the robot signed, and the corresponding images on its screen._

The robot performed 9 signs. With ⅓ of the signs, it also flashed the lights on its arm. With another ⅓ of the signs, it displayed an image corresponding to the sign on its screen. These 3 different design conditions were examined to see which was most effective.

I was surprised by how differently each child interacted with the robot. A few of the children signed with near-perfect accuracy throughout the entire experiment, imitating all the robot’s signs in a mere 6 minutes. Some took as long as 28 minutes, struggling with each sign. One particular child — who was not too keen on signing — could not stop laughing at the robot. The child kept attempting to either hug or lunge at the robot throughout the experiment, with the speech therapist and neuropsychologist lunging after him to stop him in time.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/front.png)
_A child signs with the robot (picture with permission)._

![Image](https://www.freecodecamp.org/news/content/images/2019/08/back.png)
_The speech therapist signals to the robot operators that the child signed correctly (picture with permission)._

### Children Imitated and Paid Attention to the Robot

I measured the children’s signing accuracy and attention focus. Children and their companions also completed surveys where they gave their opinions on the robot.

#### What we learned:

**1. Children could imitate the robot, and paid attention to it**

7 out of 10 children successfully imitated the robot at least once. 70% of the time, they kept their gaze on the robot, indicating attention focus. 8 out of 8 companions who filled the survey also noted that the children had a connection with the robot.

**2. The image on the robot’s screen was good**

The robot displayed an image on its screen simultaneously to signing 1/3 of the time. Children’s companions found the images useful, and thought they could help the children learn.

**3. The robot was seen as good, but a bit scary**

Both children and their companions rated the children’s experiences with the robot as good. However, some children and their companions noted that the children felt the robot was scary. Factors that create scariness should be identified and reduced in future designs.

**4. Performance of the signs needs to be better**

Both the speech therapist and children’s companions noted that the robot did not sign all words well, which might affect the children’s understanding of them.

#### Things still to learn:

**1. Are children understanding the signs?**

For this experiment, I only measured whether children imitated the signs. Future experiments are needed to verify if children are understanding them.

**2. Who best benefits from the robot?**

Not all children responded similarly to the robot. It is unlikely that this type of robot-based sign language therapy is useful to all children with autism. Future experiments should examine who this therapy is suitable for. This varying benefit is supported by companions’ survey results: 6 out of 8 companions thought the robot could potentially be beneficial as a sign language tutor.

**3. How to input speech therapist’s commands?**

To use the robot in the future, the therapist needs to be able to independently control the robot. For future implementations, a remote control or UI for programming the robot’s behaviour and interactions may be useful.

**4. How will guidelines 4 and 5 affect the design?**

For this experiment, I used a static design of the robot. Only its interactions changed (using its screen and lights at different points). Future research is needed to examine the design guidelines “modularity of complexity” (guideline 4) and “modularity specific to children’s preferences” (guideline 5). These could help adapt the robot to different users.

### The Future of Robotic Sign Language Tutors

People interacting closely with robots can induce criticism. The most prominent concern is that of robots replacing humans. In this case, the robot is not intended to replace human care — rather augment and support human care.

Therapy sessions are demanding for therapists. They need to plan and conduct the session, while dealing with a potentially uncooperative participant. In the future, technological tools could be used to reduce the cognitive load of the therapist. The robot perform the signs, while the therapist could focus on encouraging, tutoring and managing the child. With reduced cognitive load, sessions could be longer and thus more in-depth. 

The same effect could potentially be achieved if the robot were situated in the child’s home: the child would get a consistent tool to practice signs with, and the robot would not be bored or frustrated by repetitive practice.

To my knowledge, this was the first instance of using a robot to teach sign language to children with autism. I hope this research is continued further. I hope our pilot can shed some light onto how to develop this application in the future.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/science.png)
_Science — especially pilot studies — sometimes requires improvisation: lights from the robot’s back were reflected on a window behind it, which might have distracted the children. We fashioned a light-reflection-blocker for the robot’s back, out of a towel stolen from our hotel (we did pay for it)._

---

%[https://www.youtube.com/watch?v=JKWnwpTl774]

The entire study is available as:

Axelsson, M., Racca, M., Weir, D., Kyrki, V. (2019). A Participatory Design Process of a Robotic Tutor of Assistive Sign Language for Children with Autism. In _2019 28th IEEE International Symposium on Robot and Human Interactive Communication (RO-MAN)_. IEEE. **Accepted.**

The study is based on my master’s thesis at Aalto University, [available here](https://aaltodoc.aalto.fi/handle/123456789/34183).

The project was funded by Prizztech’s Robocoast and ERDF-fund, and Futurice.

