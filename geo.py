import requests

def get_geo_info(ip: str):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        return {
            "country": data.get("country", "Unknown"),
            "region": data.get("regionName", "Unknown"),
            "city": data.get("city", "Unknown")
        }
    except:
        return {
            "country": "Unknown",
            "region": "Unknown",
            "city": "Unknown"
        }
