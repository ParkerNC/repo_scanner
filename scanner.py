import sys
import requests
import argparse

class repo_info():
    def __init__(self, owner, repo, token) -> None:
        self.owner = owner
        self.repo = repo
        self.token = token

    def get_commits(self):
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/commits"
        response = requests.get(url, params = {"per_page": 100})
        print(response.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Repo Security Scanner",
        description="Scanns the indicated repository for inconsitencies in commit signatures",
    )
    parser.add_argument("-r", "--repository", required=True, help="name of repository to scan")
    parser.add_argument("-o",  "--repository_owner", required=True, help="user name of the repositories owner")
    parser.add_argument("-t", "--api_token", help="api token to allow for more scans")

    args = parser.parse_args()
    print(args.repository, args.repository_owner, args.api_token)

    repo = repo_info(args.repository_owner, args.repository, args.api_token)
    repo.get_commits()