# Commit and Push to Protected Branch

This action will simplify to commit and push something has updated in build time on Github action to a [protected branch](https://docs.github.com/en/github/administering-a-repository/defining-the-mergeability-of-pull-requests/about-protected-branches).

## Usage
### Pre-requisites
Create a workflow `.yml` file in your repositories `.github/workflows` directory, 
an [example workflow](#example-workflows) is available below. 
For more information, reference the GitHub Help Documentation for [Creating a workflow file](https://help.github.com/en/articles/configuring-a-workflow#creating-a-workflow-file).

### Supported authentications
To use this action we need a supported authentication accepted by the Git protocol. 
This action supports GitHub Apps and [personal access token (PAT)](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).

#### Required Variables

    - GIT_APP_TOKEN: ${{ secrets.GITHUB_API_TOKEN }} # Github App token
    - GITHUB_REPOSITORY: ${{ github.repository }} # github context data in environment variables.

##### Reference
- [Github Context](https://docs.github.com/en/actions/reference/context-and-expression-syntax-for-github-actions#github-context)
- [Github App generate token](https://docs.github.com/en/developers/apps/building-github-apps/creating-a-github-app)

## Example workflows
### GitHub app
```yaml
name: 'Example workflow'

on:
  push:
    branches:
      - master

jobs:
  example:
    runs-on: ubuntu-20.04
    env:
      GIT_APP_TOKEN: ${{ secrets.EXAMPLE }}
      GITHUB_REPOSITORY: ${{ github.repository }}

    steps:
    - uses: actions/checkout@v2

    - name: Protected branch commit
      uses: augustonascimentos/commit_and_push_to_protected_branch@v1
```


## Contributions
Contributions are welcome!
This action is inspired by [CasperWA/push-protected](https://github.com/CasperWA/push-protected) and to ease its use.
