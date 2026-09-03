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
  <li>
    <img src="https://cdn.simpleicons.org/leetcode/FFA116" width="20" align="center" />&nbsp;
    <b>LeetCode</b> -- {lc.get('title') or 'Knight'} (Max Rating: {lc_max})&nbsp;
    <a href="https://leetcode.com/u/Aditya_chauhan__/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Icon_External_Link.svg" width="14" align="center" /></a>
  </li>
  <br>
  <li>
    <img src="https://cdn.simpleicons.org/codeforces/1F8ACB" width="20" align="center" />&nbsp;
    <b>Codeforces</b> -- {cf_title} (Max Rating: {cf_max})&nbsp;
    <a href="https://codeforces.com/profile/Adree" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Icon_External_Link.svg" width="14" align="center" /></a>
  </li>
  <br>
  <li>
    <img src="https://cdn.simpleicons.org/codechef/5B4638" width="20" align="center" />&nbsp;
    <b>CodeChef</b> -- {cc_stars_emoji} (Max Rating: {cc_max})&nbsp;
    <a href="https://www.codechef.com/users/chauhanaditya5" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Icon_External_Link.svg" width="14" align="center" /></a>
  </li>
</ul>
"""

    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = r'(<!-- STATS:START -->)(.*?)(<!-- STATS:END -->)'
    
    new_content = re.sub(pattern, lambda m: f"{m.group(1)}\n{stats_html.strip()}\n{m.group(3)}", content, flags=re.DOTALL)

    
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("README updated successfully.")

if __name__ == "__main__":
    update_readme()
