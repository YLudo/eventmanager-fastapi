import httpx

async def get_coordinates_from_location(location: str) -> str | None:
    async with httpx.AsyncClient() as client:
        response = await client.get("https://nominatim.openstreetmap.org/search", params={
            "q": location,
            "format": "json",
            "limit": 1
        }, headers={"User-Agent": "eventmanager/1.0"})
        
        data = response.json()
        if data:
            lat = data[0]["lat"]
            lon = data[0]["lon"]
            return f"{lat},{lon}"
    return None
