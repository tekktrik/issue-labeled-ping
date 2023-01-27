# issue-label-notifier

Notify a user when an issue gets a specific label applied.

## Usage

The default message is '{user} - {label} label was applied.'.  If the
message does include '{user}', the message will automatically start
with '{user} - ' and then include the provided message.

Note that a token with write permissions for issues is required.

```yaml
name: Notify users based on issue labels

on:
  issues:
      types: [labeled]

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - uses: tekktrik/issue-label-notifier@main
        with:
            github-token: ${{ secrets.ISSUES_TOKEN }}
            user: tekktrik
            label: wontfix
            message: Hey {user} - the {label} label was applied!
```
