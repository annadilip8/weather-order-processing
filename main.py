import json
import asyncio
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

DELAY_CONDITIONS = ["Rain", "Snow", "Extreme", "Clouds"]


def generate_apology(customer, city, weather):
    return f"Hi {customer}, your order to {city} is delayed due to {weather.lower()}. We appreciate your patience!"


async def fetch_weather(session, order):
    city = order["city"]

    params = {
        "q": city,
        "appid": API_KEY
    }

    try:
        async with session.get(BASE_URL, params=params) as response:
            data = await response.json()

            
            if response.status != 200:
                print(f"Error fetching weather for {city}: {data.get('message')}")
                return order

            weather_main = data["weather"][0]["main"]

            print(f"{city}: {weather_main}")

            
            if weather_main in DELAY_CONDITIONS:
                order["status"] = "Delayed"
                order["message"] = generate_apology(
                    order["customer"],
                    city,
                    weather_main
                )

            return order

    except Exception as e:
        print(f"Exception for {city}: {str(e)}")
        return order



async def main():
    
    with open("orders.json", "r") as f:
        orders = json.load(f)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, order) for order in orders]

        updated_orders = await asyncio.gather(*tasks)

   
    with open("updated_orders.json", "w") as f:
        json.dump(updated_orders, f, indent=4)

    print("\nProcessing completed. Check updated_orders.json")


if __name__ == "__main__":
    asyncio.run(main())