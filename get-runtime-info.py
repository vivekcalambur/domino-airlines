import os
import sys
import pprint

print(sys.version_info)

env_var = os.environ
print("\n")
print("All Runtime Environment Variables")
print("---------------------------------")
pprint.pprint(dict(env_var), width=1)
