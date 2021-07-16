import os
import json
import logging
import requests
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO)

REQUEST_TIMEOUT = 10  # in seconds
API_V3_BASE = "https://api.github.com"


def api_request(url: str, http_request: str = 'get', check_response: bool = True, **kwargs):
    url = urljoin(API_V3_BASE, url)

    try:
        requests_action = getattr(requests, http_request)
        response = requests_action(
            url,
            headers={
                "Authorization": f"Bearer {os.getenv('GIT_APP_TOKEN')}",
                "Accept": "application/vnd.github.luke-cage-preview+json",
            },
            timeout=REQUEST_TIMEOUT,
            **kwargs
        )

        if check_response:
            try:
                response = response.json()

            except json.JSONDecodeError as exc:
                raise RuntimeError(f'Failed to jsonify response.\n{exc!r}')

        return response

    except Exception as err:
        raise err


def remove_branch_protection():
    url = f'/repos/{os.getenv("GITHUB_REPOSITORY", "")}/branches/master/protection/required_pull_request_reviews'
    logging.info('Looking for current branch protection rules.')
    response = api_request(url)

    data = {
        "dismiss_stale_reviews": response.get("dismiss_stale_reviews", False),
        "require_code_owner_reviews": response.get("require_code_owner_reviews", False),
        "required_approving_review_count": response.get("required_approving_review_count", 1)
    }

    if 'organization' in api_request(f'/repos/{os.getenv("GITHUB_REPOSITORY", "")}'):
        data["dismissal_restrictions"] = {
            "users": [
                _.get("login")
                for _ in response.get("dismissal_restrictions", {}).get("users", [])
            ],
            "teams": [
                _.get("slug")
                for _ in response.get("dismissal_restrictions", {}).get("teams", [])
            ]
        }

    logging.info('Saving protection rules file.')
    with open("tmp_protection_rules.json", "w") as handle:
        json.dump(data, handle)

    logging.info('Removing branch protection.')
    api_request(url, http_request='delete', check_response=False)


def re_add_branch_protection():
    logging.info('Reading protection rules file.')
    with open('tmp_protection_rules.json', 'r') as handle:
        data = json.load(handle)

    url = f'/repos/{os.getenv("GITHUB_REPOSITORY", "")}/branches/master/protection/required_pull_request_reviews'
    logging.info('Re-adding protection branch rules.')
    api_request(url, http_request='put', json=data, check_response=False)


def git_add_and_commit():
    logging.info('Pushing to remote Github.')
    os.system('git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"')
    os.system('git config --global user.name "github-actions[bot]"')
    os.system('git stash clear')
    os.system('git stash')
    os.system('git pull origin master')
    os.system('git stash apply')
    os.system('git add -A')
    os.system('git commit -m "Updated by Github Actions :)"')
    os.system('git push origin master')


def main():
    logging.info('Initializing...')
    remove_branch_protection()
    git_add_and_commit()
    re_add_branch_protection()
    logging.info('Finished...')


if __name__ == "__main__":
    main()
