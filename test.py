with open("_ids.txt", "r") as f:
	ids = [row.strip() for row in f]
print(ids)