from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.responses import JSONResponse
from datetime import timedelta
from typing import Optional
import httpx
from fastapi_cache import caches, close_caches
from fastapi_cache.backends.redis import RedisCacheBackend

# Define your API key and OpenWeatherMap endpoint
API_KEY = "your_openweathermap_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Set up FastAPI
app = FastAPI()

# Set up caching with Redis (you can choose another backend)
cache_backend = RedisCacheBackend("redis://localhost:6379/0", prefix="weather_forecast_")
cache = caches.get("weather_forecast") or caches.set(
    "weather_forecast",
    cache_backend,
    expire=timedelta(minutes=30),
)


# Dependency to get the HTTP client
async def get_http_client():
    async with httpx.AsyncClient() as client:
        yield client


# API endpoint to get weather forecast
@app.get("/weather")
async def get_weather(
    city: Optional[str] = Query(None, title="City", description="Name of the city"),
    lat: Optional[float] = Query(None, title="Latitude", description="Latitude of the location"),
    lon: Optional[float] = Query(None, title="Longitude", description="Longitude of the location"),
    http_client: httpx.AsyncClient = Depends(get_http_client),
):
    if not city and not (lat and lon):
        raise HTTPException(status_code=400, detail="Provide either city or coordinates")

    # Check if data is in cache
    cache_key = city or f"{lat},{lon}"
    cached_data = await cache.get(cache_key)
    if cached_data:
        return JSONResponse(content=cached_data, status_code=200)

    # Prepare the request parameters
    params = {
        "q": city,
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",  # You can change units as per your preference
    }

    # Make the request to OpenWeatherMap
    response = await http_client.get(BASE_URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        # Cache the data for future use
        await cache.set(cache_key, weather_data)

        return weather_data
    else:
        raise HTTPException(status_code=response.status_code, detail="Error fetching weather data")


# Event handler to close the cache when the application shuts down
@app.on_event("shutdown")
async def shutdown_event():
    await close_caches()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
