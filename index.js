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

    const owner = context.repo.owner;
    const repo = context.repo.repo
    const issueNumber = context.issue.number

    const bodyStart = "Heads up @"
    const body = bodyStart.concat(user, ' - the "', label, '" label was applied to this issue.')
    
    if (context.payload.label.name == label) {
      await octokit.request('POST /repos/{owner}/{repo}/issues/{issue_number}/comments', {
        owner: owner,
        repo: repo,
        issue_number: issueNumber.toString(),
        body: body
      })
    }

  } catch (error) {
    core.setFailed(error.message);
  }
}

run();
