import pandas as pd

df = pd.read_csv("sample_satellites.csv")

regions = {}

for _, row in df.iterrows():

    inclination = row["INCLINATION"]

    region = int(inclination // 10)

    regions[region] = regions.get(region, 0) + 1

print("\nSPACE TRAFFIC REPORT\n")

for region, count in sorted(regions.items()):

    if count > 5:
        status = "🔴 DANGEROUS"

    elif count > 2:
        status = "🟡 CROWDED"

    else:
        status = "🟢 SAFE"

    print(
        f"Region {region}: {count} satellites | {status}"
    )