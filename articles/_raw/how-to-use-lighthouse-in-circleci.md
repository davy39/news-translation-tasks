---
title: How to use Lighthouse in CircleCI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-lighthouse-in-circleci
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/nyc-building-in-midtown-east.jpg
tags:
- name: Accessibility
  slug: accessibility
- name: CircleCI
  slug: circleci
- name: Lighthouse
  slug: lighthouse
- name: SEO
  slug: seo
- name: technology
  slug: technology
- name: Website performance
  slug: website-performance
seo_title: null
seo_desc: 'By Adam Henson

  CircleCI is a popular tool for orchestrating CI/CD pipelines. Lighthouse is an open-source
  project from Google for improving the quality of web pages. It provides user-centric
  metrics to audit SEO, performance, accessibility, best prac...'
---

By Adam Henson

[CircleCI](https://circleci.com/) is a popular tool for orchestrating CI/CD pipelines. Lighthouse is an open-source project from Google for improving the quality of web pages. It provides user-centric metrics to audit SEO, performance, accessibility, best practices, and progressive web apps. 

For a deeper dive about Lighthouse you can read “[How to analyze website performance with Lighthouse](https://www.freecodecamp.org/news/three-ways-to-analyze-website-performance-with-lighthouse-8d100966c04b/)”. 

By combining these forces, we can establish website quality automation. This post will demonstrate the following:

* Basic implementation of Lighthouse in a CircleCI workflow.
* Advanced setup to display Lighthouse results in pull request comments.
* S3 Lighthouse report uploads.
* Slack notifications.

# Lighthouse Check CircleCI Orb

[CircleCI Orbs](https://circleci.com/docs/2.0/orb-intro/#section=configuration) are shareable packages of configuration elements, including jobs, commands, and executors you use in your workflows. This post will provide a guide for using the [Lighthouse Check CircleCI Orb](https://circleci.com/orbs/registry/orb/foo-software/lighthouse-check) for automating Lighthouse audits.

### Basic Example

Below is a minimal example and all we need to run Lighthouse automatically on any code change ? In this example both [`https://www.foo.software`](https://www.foo.software) and [`https://www.foo.software/contact`](https://www.foo.software/contact) will be audited.

```yaml
version: 2.1

orbs:
  lighthouse-check: foo-software/lighthouse-check@0.0.8

jobs:
  test: 
    executor: lighthouse-check/default
    steps:
      - lighthouse-check/audit:
          urls: https://www.foo.software,https://www.foo.software/contact

workflows:
  test:
    jobs:
      - test
```

With this minimal setup we have a summary provided in the output of our job. We also have full HTML reports saved as [CircleCI "artifacts"](https://circleci.com/docs/2.0/artifacts/).

![Image](https://www.freecodecamp.org/news/content/images/2020/01/circleci-orb-lighthouse-check-output.png)
_Lighthouse Check Orb output_

![Image](https://www.freecodecamp.org/news/content/images/2020/01/circleci-orb-lighthouse-check-artifacts.png)
_Lighthouse Check Orb save artifacts_

### Advanced Example

Lighthouse Check CircleCI Orb offers a complete set of bells and whistles by utilizing `[lighthouse-check](https://github.com/foo-software/lighthouse-check)` [NPM module](https://github.com/foo-software/lighthouse-check) under the hood. There’s so much more we can do with this. Let’s proceed!

## Pull Request Comments

By utilizing this feature, comments are posted with Lighthouse results on every commit. We can do so by following the steps below.

1. Create a new user or find an existing one to act as a “bot”.
2. [Create a personal access token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) from this user account.
3. [Create a CircleCI environment variable in your project](https://circleci.com/docs/2.0/env-vars/#setting-an-environment-variable-in-a-project) to hold the encrypted value from above. In our example we name it `LIGHTHOUSE_CHECK_GITHUB_ACCESS_TOKEN`.
4. Update our config file with the diff shown below.

```diff
+ prCommentAccessToken: $LIGHTHOUSE_CHECK_GITHUB_ACCESS_TOKEN
+ prCommentUrl: https://api.github.com/repos/foo-software/lighthouse-check-orb/pulls/${CIRCLE_PULL_REQUEST##*/}/reviews
urls: https://www.foo.software,https://www.foo.software/contact
```

The updates above provides a token to authorize comments on a corresponding pull request. `prCommentUrl` should be an endpoint in the [format specified by the GitHub API](https://developer.github.com/v3/pulls/reviews/#create-a-pull-request-review). Your endpoint will be similar but with `owner` and `repo` params replaced ( `foo-software/lighthouse-check-orb` ). With this, we’ve created a bot to post Lighthouse results on pull requests ?

![Image](https://www.freecodecamp.org/news/content/images/2020/01/lighthouse-check-pr-comment.png)
_Lighthouse Check PR comments_

## S3 Report Uploads

In our example we persist results by uploading reports as artifacts in our job. This solution could be sufficient in some cases, but artifacts aren’t stored permanently. In order to view reports, we need to navigate into the workflow and manually download reports from the artifact view. 

But what if we want a more dependable way of storing and referencing reports? This is where the S3 feature comes into play. We can configure AWS S3 storage by following the below steps.

1. [Create an AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) if you don’t already have one.
2. [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/SigningUpforS3.html) if you don’t already have one.
3. [Acquire an AWS access key id and secret access key](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html).
4. [Create a CircleCI environment variables](https://circleci.com/docs/2.0/env-vars/#setting-an-environment-variable-in-a-project) for these two values. In our example we’ll use `LIGHTHOUSE_CHECK_AWS_ACCESS_KEY_ID` and `LIGHTHOUSE_CHECK_AWS_SECRET_ACCESS_KEY`, respectively.
5. Add the bucket name and [region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) (example: `us-east-1`) as CircleCI environment variables: `LIGHTHOUSE_CHECK_AWS_BUCKET` and `LIGHTHOUSE_CHECK_AWS_REGION`.

Next, we’ll update our configuration with the following diff.

```diff
+ awsAccessKeyId: $LIGHTHOUSE_CHECK_AWS_ACCESS_KEY_ID
+ awsBucket: $LIGHTHOUSE_CHECK_AWS_BUCKET
+ awsRegion: $LIGHTHOUSE_CHECK_AWS_REGION
+ awsSecretAccessKey: $LIGHTHOUSE_CHECK_AWS_SECRET_ACCESS_KEY
prCommentUrl: https://api.github.com/repos/foo-software/lighthouse-check-orb/pulls/${CIRCLE_PULL_REQUEST##*/}/reviews
```

In our next commit and push, reports are automatically uploaded to S3 ✅! We also have a them linked in our PR comments.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/pr-comment-lighthouse.png)
_Lighthouse result PR comment with S3 report linked_

## Slack Notifications

What’s a new feature in a DevOps workflow without Slack notifications? A sad one indeed. Let’s ramp things up by adding notifications to a Slack channel for our whole team to see. We can accomplish this in the below steps.

1. [Create an “Incoming Webhook” in your Slack workspace and authorize a channel](https://api.slack.com/messaging/webhooks).
2. Add the Webhook URL as a CircleCI environment variable — `LIGHTHOUSE_CHECK_SLACK_WEBHOOK_URL`.

```diff
+ slackWebhookUrl: $LIGHTHOUSE_CHECK_SLACK_WEBHOOK_URL
urls: https://www.foo.software,https://www.foo.software/contact
```

Our next commit and push introduces Slack notifications! The “Lighthouse audit” link in the below screenshot navigates to the S3 report as configured ✨

![Image](https://www.freecodecamp.org/news/content/images/2020/01/circleci-orb-lighthouse-check-slack.png)
_Lighthouse Slack notification_

At this point our complete "advanced example" configuration looks like the below.

```yaml
usage:
  version: 2.1

  orbs:
    lighthouse-check: foo-software/lighthouse-check@0.0.8

  jobs:
    test: 
      executor: lighthouse-check/default
      steps:
        - lighthouse-check/audit:
            awsAccessKeyId: $LIGHTHOUSE_CHECK_AWS_ACCESS_KEY_ID
            awsBucket: $LIGHTHOUSE_CHECK_AWS_BUCKET
            awsRegion: $LIGHTHOUSE_CHECK_AWS_REGION
            awsSecretAccessKey: $LIGHTHOUSE_CHECK_AWS_SECRET_ACCESS_KEY
            prCommentAccessToken: $LIGHTHOUSE_CHECK_GITHUB_ACCESS_TOKEN
            prCommentUrl: https://api.github.com/repos/foo-software/lighthouse-check-orb/pulls/${CIRCLE_PULL_REQUEST##*/}/reviews
            slackWebhookUrl: $LIGHTHOUSE_CHECK_SLACK_WEBHOOK_URL
            urls: https://www.foo.software,https://www.foo.software/contact

  workflows:
    test:
      jobs:
        - test
```

## Maintaining a Historical Record

[Foo’s Automated Lighthouse Check](https://www.foo.software/lighthouse) is tool we can use to manage a historical record of Lighthouse audits. We can connect to it with the Lighthouse Check Orb! By doing so you can run Lighthouse remotely versus in a local, dockerized CircleCI environment. With this we can be assured our Lighthouse results aren't flaky from CircleCI infrastructure change. Follow the [documented steps to connect with Automated Lighthouse Check](https://github.com/foo-software/lighthouse-check-orb#usage-automated-lighthouse-check-api).

![Image](https://www.freecodecamp.org/news/content/images/2020/01/automated-lighthouse-check.png)
_A historical record of Lighthouse audits with "Automated Lighthouse Check"_

# What Now?

You can find other of examples of [Lighthouse Check Orb usage on GitHub](https://github.com/foo-software/lighthouse-check-orb/tree/master/src/examples). I hope this article has provided a helpful addition to your DevOps workflow! With Lighthouse integrated in a CI/CD pipeline, we can stay fully equipped to ensure high quality in website SEO, performance, accessibility, best practice, and progressive web apps.

