import csv

def defang_ioc(indicator):
    """Defangs malicious URLs and IP addresses so they cannot be clicked accidentally."""
    return indicator.replace("http://", "hxxp://").replace("https://", "hxxps://").replace(".", "[.]")

input_file = "../data/iocs.csv"

print("--- Defanged IoCs for Threat Report ---")
try:
    with open(input_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            safe_val = defang_ioc(row["indicator_value"])
            print(f"[{row['indicator_type']}] {safe_val} -> {row['threat_type']} ({row['malware_family']})")
except FileNotFoundError:
    print("Error: iocs.csv not found in ../data/ folder.")
