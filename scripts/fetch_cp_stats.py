import json
import urllib.request
import urllib.parse
import os
import time

OUTPUT_FILE = os.path.join(os.getcwd(), 'data', 'stats.json')

CF_HANDLE = 'Adree'
LC_USERNAME = 'Aditya_chauhan__'
CC_USERNAME = 'chauhanaditya5'

def lc_graphql(query, variables):
    url = 'https://leetcode.com/graphql/'
    data = json.dumps({'query': query, 'variables': variables}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as res:
            response = json.loads(res.read().decode())
            return response.get('data', {})
    except Exception as e:
        print(f"LeetCode error: {e}")
        return {}

def get_leetcode_stats():
    contest_query = '''
    query userContestInfo($username: String!) {
      userContestRanking(username: $username) { rating }
      userContestRankingHistory(username: $username) { attended rating }
    }
    '''
    data = lc_graphql(contest_query, {'username': LC_USERNAME})
    ranking = data.get('userContestRanking') or {}
    history = [e for e in (data.get('userContestRankingHistory') or []) if e.get('attended')]
    max_rating = max([e.get('rating', 0) for e in history]) if history else None
    
    return {
        'currentRating': round(ranking.get('rating', 0)) if ranking.get('rating') else None,
        'maxRating': round(max_rating) if max_rating else None
    }

def get_codeforces_stats():
    url = f"https://codeforces.com/api/user.info?handles={CF_HANDLE}"
    try:
        with urllib.request.urlopen(url) as res:
            data = json.loads(res.read().decode())
            user = data.get('result', [{}])[0]
            return {
                'currentRating': user.get('rating'),
                'maxRating': user.get('maxRating'),
                'currentRank': user.get('rank'),
                'maxRank': user.get('maxRank')
            }
    except Exception as e:
        print(f"Codeforces error: {e}")
        return {}

def get_codechef_stats():
    url = f"https://www.codechef.com/users/{CC_USERNAME}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as res:
            html = res.read().decode()
            marker = "all_rating = "
            start_idx = html.find(marker)
            if start_idx == -1: return {}
            arr_start = html.find("[", start_idx)
            depth = 0
            arr_end = -1
            for i in range(arr_start, len(html)):
                if html[i] == '[': depth += 1
                if html[i] == ']':
                    depth -= 1
                    if depth == 0:
                        arr_end = i + 1
                        break
            if arr_end == -1: return {}
            raw = html[arr_start:arr_end]
            contests = json.loads(raw)
            ratings = [int(c['rating']) for c in contests if 'rating' in c]
            current_rating = ratings[-1] if ratings else None
            max_rating = max(ratings) if ratings else None
            
            def get_stars(r):
                if r is None: return None
                if r < 1400: return "1-Star"
                if r < 1600: return "2-Star"
                if r < 1800: return "3-Star"
                if r < 2000: return "4-Star"
                if r < 2200: return "5-Star"
                if r < 2500: return "6-Star"
                return "7-Star"

            return {
                'currentRating': current_rating,
                'maxRating': max_rating,
                'stars': get_stars(current_rating),
                'maxStars': get_stars(max_rating)
            }
    except Exception as e:
        print(f"CodeChef error: {e}")
        return {}

def main():
    print("Fetching LeetCode...")
    lc = get_leetcode_stats()
    time.sleep(1)
    
    print("Fetching Codeforces...")
    cf = get_codeforces_stats()
    time.sleep(1)
    
    print("Fetching CodeChef...")
    cc = get_codechef_stats()
    
    result = {
        'leetcode': lc,
        'codeforces': cf,
        'codechef': cc
    }
    
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(result, f, indent=2)
    print(f"Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
