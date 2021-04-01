import sys
import argparse
from howfairis import Repo, Checker

parser = argparse.ArgumentParser(description='Citation checker using howfairis')
parser.add_argument('--url', action='store', type=str, help='Repository url.')

args = parser.parse_args()

url = args.url
repo = Repo(url)
checker = Checker(repo, is_quiet=True)

compliance = checker.check_five_recommendations()

if compliance.citation:
    sys.exit(0)
else:
    sys.exit(1)
