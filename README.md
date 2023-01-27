# issue-label-notifier

Notify a user when an issue gets a specific label applied.

## Usage

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
```
