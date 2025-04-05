import requests

username = input("Enter GitHub username: ")
res = requests.get(f"https://api.github.com/users/{username}/repos")
repos = res.json()
for repo in repos:
    print("📦", repo["name"], "- ⭐", repo["stargazers_count"])