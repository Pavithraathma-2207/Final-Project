import requests

# Base URL for EC2 instance metadata service
base_url = "http://169.254.169.254/latest/meta-data/"

# Metadata fields you want to retrieve
keys = [
    "instance-id",
    "ami-id",
    "hostname",
    "public-ipv4",
    "local-ipv4",
    "security-groups"
]

print("✅ EC2 Instance Metadata:")

# Loop through each metadata key and request its value
for key in keys:
    try:
        response = requests.get(base_url + key, timeout=2)
        if response.status_code == 200 and response.text.strip():
            print(f"{key}: {response.text}")
        else:
            print(f"{key}: Not available")
    except requests.exceptions.RequestException as e:
        print(f"{key}: Failed to retrieve ({e})")
