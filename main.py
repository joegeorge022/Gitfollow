import requests

username = "XXXXXXXXX" # Replace with your username
token = "XXXXXXXXXXXXXXXXXXXXX" # Replace with your PAT

headers = {
    "Authorization": f"token {token}"
}

def get_all_pages(url):
    """Fetch all paginated results from GitHub API."""
    results = []
    while url:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        results.extend(response.json())
        url = response.links.get('next', {}).get('url')
    return results

# Get followers 
followers_url = f"https://api.github.com/users/{username}/followers?per_page=100"
followers_data = get_all_pages(followers_url)
followers = {user['login'] for user in followers_data}

# Get following 
following_url = f"https://api.github.com/users/{username}/following?per_page=100"
following_data = get_all_pages(following_url)
following = {user['login'] for user in following_data}

# Print summary
print(f"\n👥 Total Followers: {len(followers)} \n")
print(f"➡️ Total Following: {len(following)}  \n")

print("\n Followers:", followers)
print("\n Following:", following)

# Compare sets
not_following_back = following - followers
not_followed_by_you = followers - following

print("\n❌ People who don't follow you back:")
for user in sorted(not_following_back):
    print("-", user)

print("\n")

print("\n🔁 People you don't follow back:")
for user in sorted(not_followed_by_you):
    print("-", user)
