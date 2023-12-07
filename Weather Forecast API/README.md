
# Weather Forecast API

This is a simple API built with FastAPI that fetches weather forecasts from OpenWeatherMap and provides current weather information for a given city or coordinates. The API includes request validation using FastAPI and caching to reduce the number of requests to the external API.

## Getting Started

These instructions will help you set up and run the Weather Forecast API on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/manish-jsx/weather-forecast-api.git
   ```

2. Change into the project directory:

   ```bash
   cd weather-forecast-api
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and replace `"your_openweathermap_api_key"` in the `main.py` file with your actual API key.

2. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

3. Open your web browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the Swagger UI for testing the API endpoints.

### API Endpoints

- **GET /weather:** Retrieve current weather information for a city or coordinates.

   Example:
   - http://127.0.0.1:8000/weather?city=London
   - http://127.0.0.1:8000/weather?lat=51.5074&lon=-0.1278

### Configuration

You can configure the cache backend and other settings in the `main.py` file.

### Dependencies

- [FastAPI](https://fastapi.tiangolo.com/)
- [httpx](https://www.python-httpx.org/)
- [uvicorn](https://www.uvicorn.org/)
- [fastapi-cache](https://github.com/alysivji/fastapi-cache)

### Contributing

Feel free to contribute to this project. Open an issue or submit a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
