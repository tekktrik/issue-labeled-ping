# SPDX-FileCopyrightText: 2025 Alec Delaney
# SPDX-License-Identifier: MIT

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pygithub",
# ]
# ///

"""Script for commenting on an issue if a matching label is added to it."""

import os
import sys

import github

try:
    token = os.environ["INPUT_GITHUB_TOKEN"]

    user = os.environ["INPUT_USER"]
    label = os.environ["INPUT_LABEL"]
    message = os.environ["INPUT_MESSAGE"]

    repo = os.environ["ACTION_REPO"]

    label_used = os.environ["ACTION_LABEL_USED"]
    issue_number = int(os.environ["ACTION_ISSUE_NUMBER"])

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
