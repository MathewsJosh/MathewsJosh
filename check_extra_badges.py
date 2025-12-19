import requests

badges = [
    "https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white",
    "https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=elasticsearch&logoColor=white",
    "https://img.shields.io/badge/Kibana-005571?style=for-the-badge&logo=kibana&logoColor=white",
    "https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white",
    "https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white",
    "https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white"
]

for url in badges:
    try:
        r = requests.get(url)
        print(f"{url} -> {r.status_code}, len: {len(r.content)}")
    except Exception as e:
        print(f"Exception for {url}: {e}")
