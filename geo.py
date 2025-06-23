import requests
import logging

# Loglarni yozib borish (xato aniqlash oson bo‘ladi)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_geo_info(ip: str) -> dict:
    """
    IP manzil asosida geolokatsiya ma'lumotlarini ipinfo.io orqali olish.
    """
    try:
        # IP manzilni tekshirish (localhost yoki ichki tarmoq IP bo‘lishi mumkin)
        if ip.startswith("127.") or ip.startswith("192.168.") or ip == "0.0.0.0":
            logger.warning(f"Local or invalid IP: {ip}")
            return {
                "country": "Local",
                "region": "Local",
                "city": "Local",
                "loc": "",
                "timezone": "Local",
                "org": "Local",
                "postal": "00000"
            }

        url = f"https://ipinfo.io/{ip}/json"
        headers = {
            "Accept": "application/json",
            "User-Agent": "GeoInfoFetcher/1.0"
        }

        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # xatoliklarni ko‘taradi

        data = response.json()
        logger.info(f"Geo data fetched for IP {ip}: {data}")

        return {
            "country": data.get("country", "Unknown"),
            "region": data.get("region", "Unknown"),
            "city": data.get("city", "Unknown"),
            "loc": data.get("loc", ""),
            "timezone": data.get("timezone", "Unknown"),
            "org": data.get("org", "Unknown"),
            "postal": data.get("postal", "Unknown")
        }

    except requests.exceptions.Timeout:
        logger.error(f"Geo info request timed out for IP: {ip}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Geo info error for IP {ip}: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error in get_geo_info: {e}")

    return {
        "country": "Unknown",
        "region": "Unknown",
        "city": "Unknown",
        "loc": "",
        "timezone": "Unknown",
        "org": "Unknown",
        "postal": "Unknown"
    }
