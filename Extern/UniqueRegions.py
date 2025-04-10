PlaceComplete_DF = pd.read_csv('MergeAbsolute2_converted.csv')

unique_regions = PlaceComplete_DF["region"].unique()
sorted_unique_regions = sorted(unique_regions)
print("Unique Regions:")
for region in sorted_unique_regions:
    print(f"- {region}")