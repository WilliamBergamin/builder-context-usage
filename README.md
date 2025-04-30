# Bolt for Python Custom Step with Builder Context

This is a Bolt for Python app used to build custom steps for use in
[Workflow Builder](https://api.slack.com/start#workflow-builder) with the user
context of the person building a workflow.

## Setup

Before getting started, first make sure you have a development workspace where
you have permission to install apps. **Please note that the features in this
project require that the workspace be part of
[a Slack paid plan](https://slack.com/pricing).**

### Developer Program

Join the [Slack Developer Program](https://api.slack.com/developer-program) for
exclusive access to sandbox environments for building and testing your apps,
tooling, and resources created to help developers build and grow.

## Installation

### Create a Slack App

1. Clone this repository
2. Choose the workspace you want to install the application to
3. Use the Slack CLI to create an instance to the app `slack init`
4. Install the dependencies
   1. python3 -m venv .venv
   2. source .venv/bin/activate
   3. pip install -r requirements.txt
5. Use `slack run` to start the application

### Linting

Run flake8 and black for linting and code formatting:

```zsh
# Run ruff from root directory for linting
ruff check

# Run ruff from root directory for code formatting
ruff format
ruff check --fix
```

## Using Steps in Workflow Builder

With your server running, the `Sample step` is now ready for use in
[Workflow Builder](https://api.slack.com/start#workflow-builder)! Add it as a
custom step in a new or existing workflow, then run the workflow while your app
is running.

For more information on creating workflows and adding custom steps, read more
[here](https://slack.com/help/articles/17542172840595-Create-a-new-workflow-in-Slack).

## Project Structure

### `app.py`

`app.py` is the entry point for the application and is the file you'll run to
start the server. This project aims to keep this file as thin as possible,
primarily using it as a way to route inbound requests.

### `manifest.json`

`manifest.json` is a configuration for Slack apps. With a manifest, you can
create an app with a pre-defined configuration, or adjust the configuration of
an existing app.

### `/listeners`

Every incoming request is routed to a "listener". Inside this directory, we
group each listener based on the Slack Platform feature used, so
`/listeners/actions.py` handles incoming
[Actions](https://api.slack.com/reference/interaction-payloads/block-actions)
requests, `/listeners/functions.py` handles
[Custom Steps](https://api.slack.com/automation/functions/custom-bolt) and so
on.
