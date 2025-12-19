import requests

badges = [
    "https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white",
    "https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white",
    "https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white",
    "https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white",
    "https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white",
    "https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white",
    "https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white",
    "https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white",
    "https://img.shields.io/badge/Kotlin-0095D5?style=for-the-badge&logo=kotlin&logoColor=white",
    "https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black",
    "https://img.shields.io/badge/MATLAB-ED8B00?style=for-the-badge&logo=mathworks&logoColor=white",
    "https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white",
    "https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white",
    "https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white",
    "https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white",
    "https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white",
    "https://img.shields.io/badge/Matplotlib-013243?style=for-the-badge&logo=anaconda&logoColor=white",
    "https://img.shields.io/badge/Seaborn-2C2D72?style=for-the-badge&logo=python&logoColor=white",
    "https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB",
    "https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white",
    "https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white",
    "https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB",
    "https://img.shields.io/badge/Unity-100000?style=for-the-badge&logo=unity&logoColor=white",
    "https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=three.js&logoColor=white",
    "https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white",
    "https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white",
    "https://img.shields.io/badge/Materialize-FF4081?style=for-the-badge&logo=materialize&logoColor=white",
    "https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white",
    "https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white",
    "https://img.shields.io/badge/Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white",
    "https://img.shields.io/badge/Salesforce-00A1E0?style=for-the-badge&logo=salesforce&logoColor=white",
    "https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white",
    "https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white",
    "https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white",
    "https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black",
    "https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white",
    "https://img.shields.io/badge/Adobe_Photoshop-31A8FF?style=for-the-badge&logo=adobe%20photoshop&logoColor=white",
    "https://img.shields.io/badge/Adobe_Premiere-9999FF?style=for-the-badge&logo=adobe%20premiere%20pro&logoColor=white",
    "https://img.shields.io/badge/Vegas_Pro-000000?style=for-the-badge&logo=sony&logoColor=white"
]

for url in badges:
    try:
        r = requests.get(url)
        if r.status_code != 200:
            print(f"Error {r.status_code}: {url}")
        else:
            # Check content length to see if it's too small (potential error SVG)
            if len(r.content) < 500:
                print(f"Small content ({len(r.content)} bytes): {url}")
    except Exception as e:
        print(f"Exception for {url}: {e}")
