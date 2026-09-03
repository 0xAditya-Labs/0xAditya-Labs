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

    stats_html = f"""
<ul>
  <li><b>Meta Hacker Cup:</b> Advanced to Round 2, securing Global Rank 3223 (AIR 875) out of thousands of competitors.</li>
  <li><b>Flipkart GRiD:</b> Semi-Finalist in 7.0 and 8.0 (consecutive years), placing in the top 0.5% among 3.2 lakh+ participants.</li>
  <li><b>CodeStorm:</b> Secured 2nd place in GDSC NIT Jalandhar's competitive programming contest.</li>
</ul>

<br>

<ul style="list-style-type: none; padding-left: 0;">
  <li><img src="https://skillicons.dev/icons?i=leetcode" width="20" align="center" /> &nbsp;<b>LeetCode:</b> Achieved {lc.get('title') or 'Knight'} status (Max Rating: {lc_max})</li>
  <li><img src="https://img.shields.io/badge/Codeforces-1F8ACB?style=flat-square&logo=codeforces&logoColor=white" align="center" /> &nbsp;<b>Codeforces:</b> {cf_title} (Max Rating: {cf_max})</li>
  <li><img src="https://img.shields.io/badge/CodeChef-5B4638?style=flat-square&logo=codechef&logoColor=white" align="center" /> &nbsp;<b>CodeChef:</b> {cc_stars} (Max Rating: {cc_max})</li>
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
