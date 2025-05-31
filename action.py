# SPDX-FileCopyrightText: 2025 Alec Delaney
# SPDX-License-Identifier: MIT

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pygithub",
# ]
# ///

"""Script for commenting on an issue if a matching label is added to it."""

import json
import os
import sys

import github

try:
    token = os.environ["INPUT_GITHUB_TOKEN"]

    user = os.environ["INPUT_USER"]
    label = os.environ["INPUT_LABEL"]
    message = os.environ["INPUT_MESSAGE"]

    repo = os.environ["ACTION_REPO"]
    event_path = os.environ["ACTION_EVENT_PATH"]

    with open(event_path) as jsonfile:
        event = json.load(jsonfile)

    issue_number = event["issue"]["number"]
    label_used = event["label"]["name"]

    if "{user}" not in message:
        message = "{user} - " + message

    message = message.replace("{user}", f"@{user}")
    message = message.replace("{label}", label)

    if label_used != label:
        print("No users were notified.")
        sys.exit(0)

    g = github.Github(token)
    g_repo = g.get_repo(repo)
    g_issue = g_repo.get_issue(issue_number)
    g_issue.create_comment(message)

except:

    print("Something went wrong and the ping action failed.")
    sys.exit(1)
