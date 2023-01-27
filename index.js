const core = require('@actions/core');
const github = require('@actions/github')

const context = github.context


// most @actions toolkit packages have async methods
async function run() {
  try {
    const myToken = core.getInput('github-token');
    const octokit = github.getOctokit(myToken);

    const label = core.getInput('label');
    const user = core.getInput('user');
    let message = core.getInput('message');

    const owner = context.repo.owner;
    const repo = context.repo.repo
    const issueNumber = context.issue.number

    if (!message.includes("{user}")) {
      message = "{user} - ".concat(message)
    }

    message = message.replaceAll("{user}", "@".concat(user));
    message = formattedMessage.replaceAll("{label}", label);
    
    if (context.payload.label.name == label) {
      await octokit.request('POST /repos/{owner}/{repo}/issues/{issue_number}/comments', {
        owner: owner,
        repo: repo,
        issue_number: issueNumber.toString(),
        body: message
      });
    }

  } catch (error) {
    core.setFailed(error.message);
  }
}

run();
