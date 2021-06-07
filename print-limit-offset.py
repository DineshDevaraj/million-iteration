
import sys
limit = int(sys.argv[1])
offset = 1_000_000_000 - limit
print(f"LIMIT {limit} OFFSET {offset}")
