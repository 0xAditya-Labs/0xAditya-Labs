import json
import os
import re

README_FILE = os.path.join(os.getcwd(), 'README.md')
STATS_FILE = os.path.join(os.getcwd(), 'data', 'stats.json')

def update_readme():
    if not os.path.exists(STATS_FILE):
        print("Stats file not found.")
        return
        
    with open(STATS_FILE, 'r') as f:
        stats = json.load(f)
        
    lc = stats.get('leetcode', {})
    cf = stats.get('codeforces', {})
    cc = stats.get('codechef', {})
    
    lc_max = lc.get('maxRating') or 1965
    cf_max = cf.get('maxRating') or 1418
    cf_title = (cf.get('maxRank') or 'Specialist').title()
    cc_max = cc.get('maxRating') or 1661
    cc_stars = cc.get('maxStars') or '3-Star'

    # Map CodeChef stars to actual star emojis
    cc_stars_mapping = {
        '1-Star': '★',
        '2-Star': '★★',
        '3-Star': '★★★',
        '4-Star': '★★★★',
        '5-Star': '★★★★★',
        '6-Star': '★★★★★★',
        '7-Star': '★★★★★★★'
    }
    cc_stars_emoji = cc_stars_mapping.get(cc_stars, '★★★')

    stats_html = f"""
<ul style="list-style-type: none; padding-left: 0;">
  <li><img src="https://skillicons.dev/icons?i=leetcode" width="22" align="center" /> &nbsp;<b>LeetCode:</b> Achieved {lc.get('title') or 'Knight'} status (Max Rating: {lc_max})</li>
  <br>
  <li><img src="https://img.shields.io/badge/Codeforces-1F8ACB?style=flat-square&logo=codeforces&logoColor=white" align="center" /> &nbsp;<b>Codeforces:</b> {cf_title} (Max Rating: {cf_max})</li>
  <br>
  <li><img src="https://img.shields.io/badge/CodeChef-5B4638?style=flat-square&logo=codechef&logoColor=white" align="center" /> &nbsp;<b>CodeChef:</b> {cc_stars_emoji} (Max Rating: {cc_max})</li>
</ul>
"""

    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = r'(<!-- STATS:START -->)(.*?)(<!-- STATS:END -->)'
    replacement = r'\1\n' + stats_html.strip() + r'\n\3'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("README updated successfully.")

if __name__ == "__main__":
    update_readme()
