import requests

badges = [
    "https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white",
    "https://img.shields.io/badge/Materialize-FF4081?style=for-the-badge&logo=materializecss&logoColor=white",
    "https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white",
    "https://img.shields.io/badge/Azure-0089D6?style=for-the-badge&logo=microsoftazure&logoColor=white",
    "https://img.shields.io/badge/Salesforce-00A1E0?style=for-the-badge&logo=salesforce&logoColor=white",
    "https://img.shields.io/badge/Photoshop-31A8FF?style=for-the-badge&logo=adobephotoshop&logoColor=white",
    "https://img.shields.io/badge/Premiere-9999FF?style=for-the-badge&logo=adobepremierepro&logoColor=white",
    "https://img.shields.io/badge/Matlab-ED8B00?style=for-the-badge&logo=mathworks&logoColor=white",
    "https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"
]

for url in badges:
    try:
        r = requests.get(url)
        print(f"{url} -> {r.status_code}, len: {len(r.content)}")
    except Exception as e:
        print(f"Exception for {url}: {e}")
