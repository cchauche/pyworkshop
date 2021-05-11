import requests
import pprint

API_URL = "https://api.github.com/search/repositories"

PARAMS = {
    "q": "stars:>50000"
}


def repos_with_most_stars(languages):
    params = {
        'q': create_query(languages),
        'sort': 'stars',
        'order': 'desc',
    }
    print("params:", params)
    response = requests.get(API_URL, params=params)
    return response.json()["items"]


def create_query(languages):
    query = 'stars:>50000'
    for lang in languages:
        query += f" language:{lang}"
    return query


def main():
    top_repos = repos_with_most_stars(['python', 'go'])
    for i, repo in enumerate(top_repos):
        "Top starred repos on GitHub:"
        print(
            f"  {i+1}: {repo['name']} - {str(repo['stargazers_count'])} stars")


if __name__ == "__main__":
    main()
