import json
import logging
import os
import string
from typing import List, TypedDict

from slack_bolt import Ack, App, Complete
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
logging.basicConfig(level=logging.DEBUG)


class Text(TypedDict):
    type: str
    text: str


class OptionSelect(TypedDict):
    text: Text
    value: str


def build_option_select(value: str) -> OptionSelect:
    return {
        "text": {
            "type": "plain_text",
            "text": value,
        },
        "value": value,
    }


def get_authorized_actions(name: str) -> List[OptionSelect]:
    midpoint = len(string.ascii_lowercase) // 2
    if name[0] in string.ascii_lowercase[:midpoint]:
        return [
            build_option_select("run"),
            build_option_select("jump"),
            build_option_select("faint"),
        ]
    return [
        build_option_select("cry"),
        build_option_select("fly"),
        build_option_select("smile"),
    ]


@app.function("authorized_actions", auto_acknowledge=False)
def handle_authorized_actions(
    inputs: dict,
    complete: Complete,
    ack: Ack,
    client: WebClient,
    logger: logging.Logger,
):
    logger.info(json.dumps(inputs, indent=1))
    builder_id = inputs["builder"]["id"]
    try:
        response = client.users_info(user=builder_id)
        builder_name = response["user"]["profile"]["real_name"]
        logger.info(f"Builder name: {builder_name}")
        complete(outputs={"options": get_authorized_actions(builder_name)})
    except SlackApiError as e:
        logger.exception(e)
    finally:
        ack()


@app.function("select_authorized_action")
def handle_select_authorized_action(inputs: dict, complete: Complete):
    complete(outputs={"selected_action": inputs["action"]})


if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
