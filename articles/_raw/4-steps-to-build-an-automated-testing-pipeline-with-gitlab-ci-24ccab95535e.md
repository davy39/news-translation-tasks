---
title: 'Catch bugs systematically: how to build a GitLab CI testing pipeline in 4
  steps'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-14T20:05:02.000Z'
originalURL: https://freecodecamp.org/news/4-steps-to-build-an-automated-testing-pipeline-with-gitlab-ci-24ccab95535e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3HCwOHLXPebHuA-2oe_FMA.jpeg
tags:
- name: Continuou
  slug: continuou
- name: Docker
  slug: docker
- name: GitLab
  slug: gitlab
- name: Testing
  slug: testing
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Joyz

  Your first app is a hit the day it’s launched. But one week later, you realize that
  it has no retention. You discover that this is because whenever a user clicks the
  “send” button, their comments get posted twice.

  The bug was so minor, but it...'
---

By Joyz

Your first app is a hit the day it’s launched. But one week later, you realize that it has no retention. You discover that this is because whenever a user clicks the “send” button, their comments get posted twice.

The bug was so minor, but it killed your momentum. But that’s okay. For your second app, you and your partner check more carefully. You both click, click, click your app all day and night to prevent minor bugs like that from happening again.

For one app, that’s okay. But after a year, you have a company building 7 apps on different platforms, including web, iOS, and Android. Your team now does code review before any app launch. You test through the apps and do your clicking before they’re shipped. But your nightmare from app #1 returns: users drop the app and this time it’s because their posts showing strange characters when they type an emoji. You end up with 1-star ratings after launch.

There are 3 types of product-making companies: those who do not test, those who test, and those who test fast, accurately and frequently.

Is an automated testing system with continuous integration (CI) just a dream? CI seems like a “nice-to-have”, especially since services that run tests and generate reports like [Sauce Labs](https://saucelabs.com/), [BrowserStack](https://www.browserstack.com/), [Test Complete](https://support.smartbear.com/testcomplete/) are expensive. The good news is, there are many free and popular tools out there that you can mix and match to set up a free automated testing system. As a QA tester, I figured out a free testing pipeline setup, so I’m sharing it to save you time and money.

Why did my company want to set up an automated system? Here are some reasons below:

* We hate manual repetitive jobs that are prone to human error.
* We want a smoother process (test it when there is a code update), and reduce the waiting time.
* We want to schedule the tests and make them under control.

### Setting up your UI tests

This post introduces a practical pipeline setup that can run **web-based** UI (User Interface) tests automatically and continuously. The later part maybe a bit technical but it’s quite fun to build!

I have set up the whole system with these free and open-source tools:

* [Selenium](http://www.seleniumhq.org/) — to script and automate browsers to perform tests
* [Docker](https://www.docker.com/) — to build an image for test environment and ship it fast
* [Gitlab CI](https://about.gitlab.com/gitlab-ci/) — to trigger, build and run the test upon code updates
* [Skygear](https://skygear.io/) — to save test result for report on demand

![Image](https://cdn-media-1.freecodecamp.org/images/1*3HCwOHLXPebHuA-2oe_FMA.jpeg)
_Setting up takes 4 steps. Here we go!_

### Step #1: Write the script and run it locally

First of all, we write the test script, to let our original manual test run automatically. [Selenium](http://www.seleniumhq.org/) is a well-known tool for web automation. It supports different client languages including Java, Ruby, Python, etc.

Here’s an example on perform a button click on a website in Python.

> Update: Added usage of Chrome official headless mode (details [here](https://medium.com/@joyzoursky/recent-updates-6264d1e5d42f)).

With the idea of a basic unit test model, we could easily identify these three major components in the script:

* Set up
* Run test case
* Tear down

In this script, it will run `test_case_1` and `test_case_2` respectively, both with `setUp` before the test and `tearDown` after the test. We use [unittest](https://docs.python.org/3/library/unittest.html) as our testing framework in this example. Feel free to use what you like, such as [pytest](http://doc.pytest.org/en/latest/) or [nose](http://nose.readthedocs.io/en/latest/) in Python.

You can add more test cases, such as filling in forms and clicking on elements, depending on your website's interface.

### Step #2: Build an image with your testing environment

Test running requires a clean environment. To create a clean environment, we definitely do not want to set up a real machine every time and wait for hours to install all the software needed. The container concept helps.

[Docker](https://www.docker.com/) helps you build your testing environment into an image. The image includes all the software that needs to be pre-installed and run on that container like a virtual machine. With Docker, you can just create a new container and pull the same image every time you want to start over from your default environment.

To perform our test with the Selenium Python client, we want our image to pre-install the following:

* Python
* Google Chrome
* Chrome driver
* [Xvfb](https://en.wikipedia.org/wiki/Xvfb)

Xvfb is a virtual display server that helps you to launch a browser in [a headless mode](http://elementalselenium.com/tips/38-headless) (without display). It is necessary to run the UI tests in a container. It cannot connect to a display output to show the browser visually.

Then, we will also install the Selenium package inside the container. Not all projects need the same list of packages.

We create a [Dockerfile](https://docs.docker.com/engine/reference/builder/), build the image and upload to our [Docker Cloud](https://cloud.docker.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*6O2QhCEpjoALjK1nzo0N7g.png)

You could find this image through this [link](https://hub.docker.com/r/joyzoursky/python-chromedriver/), or directly pull this image with this command:

```
docker pull joyzoursky/python-chromedriver:3.6-xvfb
```

Then you will have an environment ready for performing the UI tests.

> Update: Added new Docker image built with Xvfb deprecated (details [here](https://medium.com/@joyzoursky/recent-updates-6264d1e5d42f)).

### Step #3: Set up GitLab CI

[GitLab](https://about.gitlab.com/) provides a CI/CD Pipelines feature, to continuously build and run your projects. The setup is like other CI tools such as [Travis CI](https://travis-ci.org/) or [Jenkins.](https://jenkins.io/) This requires a `.gitlab-ci.yml`file to configure your build process.

Take a look at this example:

> Update: Added example with Xvfb deprecated (details [here](https://medium.com/@joyzoursky/recent-updates-6264d1e5d42f)).

When new codes are pushed to the repository, GitLab will look for `.gitlab-ci.yml` from the root directory, and trigger a build according to your settings.

In this script, it pulls the environment image from `joyzoursky/python-chromedriver:3.6-xvfb` in the first line. Then it installs the required packages like Selenium, sets variables needed, and then it starts the process.

Note that there are 2 stages of the build process in this example: `test` and `report`. In each stage, the jobs in that stage will be run **concurrently.** You can define tests in the same stage if they could run in sync.

Go to the Pipelines page to see the flow and completion here:

![Image](https://cdn-media-1.freecodecamp.org/images/1*yEi8rtmbGz0JYottZ188oA.png)

So where do we run our tests actually?

GitLab hosts some shared runners which are free. By looking into the build log, we can find the container information in the first few lines:

```
Running with gitlab-ci-multi-runner 1.10.4 (b32125f)Using Docker executor with image joyzoursky/python-chromedriver:3.5 ...Pulling docker image joyzoursky/python-chromedriver:3.5 ...Running on runner-4e4528ca-project-2749300-concurrent-0 via runner-4e4528ca-machine-1489737516-5e0de836-digital-ocean-4gb...
```

It shows the container name running on [Digital Ocean](https://www.digitalocean.com/).

Of course, you can also create your specific runners to run the test on your self-hosted machines. GitLab supports runners on different platforms including [Docker](https://www.docker.com/) and [Kubernetes](https://kubernetes.io/). But, as GitLab is a new platform, it goes through many updates. So the specific runners may sometimes break when they are out-of-date. You should always refer to the [official repository](https://gitlab.com/gitlab-org/gitlab-ci-multi-runner/tree/master) when configuring the setup.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JZJwNUSlvVrA-mF2noJiLQ.png)

### Step #4: Run and report periodically

You may want to have your tests run periodically. You can achieve this by setting up [cron jobs](https://en.wikipedia.org/wiki/Cron), but you may not want to set up a server just to run a one-line cron job. My company’s open source serverless back-end is [Skygear](http://skygear.io). We can use it to write a simple cloud code function with the [@every](https://docs.skygear.io/guides/cloud-function/scheduled-tasks/python/) decorator and trigger the test pipeline on an interval of time.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yuASEuatDfLkSD3sfmKaqA.png)
_[Skygear](https://skygear.io/" rel="noopener" target="_blank" title=")’s developer portal. Look for your Cloud Code Git URL._

* Login to your [Skygear portal](https://portal.skygear.io)
* Find your Cloud Code Git URL
* Clone the quick start codes
* Edit to add the little piece of code below
* Push the codes and the cron job will trigger the test every hour

> Update: Used GitLab 10.0 pipeline scheduler instead of cron job (details [here](https://medium.com/@joyzoursky/recent-updates-6264d1e5d42f)).

Assume that you have already written some code to generate test reports. Would you like to receive and read the test reports every hour? Of course not. So, we also link [Skygear’s free Cloud DB](https://docs.skygear.io/guides/cloud-db/basics/js/) service to store the test result. The system only sends alerts when a test case changes from PASS to FAIL, or FAIL to PASS. This notification approach may vary according to the project need.

To save and retrieve data from the Skygear database, we could use the existing SDK. Or if you are a Python user, you may use this little [Python DB Client](https://github.com/skygear-demo/python-db-client) to help write your data handler . We use it to save test results after each test case, and retrieve the reports after running all test suites.

Finally, we can have the test result alerts sent on demand.

P.S. We use [Slack](https://slack.com/) [real time messaging API](https://api.slack.com/rtm) to do the reporting, so we can receive notifications in the corresponding project channels.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xHr_ezmVEBYRVZ4oOLJq3Q.png)

### Conclusion

Now, whenever there is a code update on the production branch, this automated UI test is triggered and tests are done automatically. Failure results will be pushed back to our Slack channel to notify our developers.

The biggest barrier to setting up a free automated UI test is probably researching the tools if you are not already a professional QA tester. Since QA is my full-time job, I hope that sharing our upgraded UI Test stack will help free up your time as well!

If you found this useful, please click the ? below so other people can see it too. Thank you!

