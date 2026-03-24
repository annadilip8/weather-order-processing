# weather-order-processing

## Overview

I built this project to check real-time weather conditions for delivery locations and identify whether an order might be delayed. It uses the OpenWeatherMap API to fetch weather data and updates the order status based on the conditions.

---

## Features

* Fetches weather data for multiple cities at the same time using asyncio
* Marks orders as delayed if weather conditions are bad (Rain, Snow, Extreme)
* Generates a simple apology message for delayed orders
* Handles invalid city inputs without stopping the program
* Keeps API key secure using a .env file

---

## Tech Stack

* Python
* asyncio, aiohttp
* OpenWeatherMap API
* python-dotenv

---

## Input

* orders.json file containing order details like order_id, customer name, city, and status

---

## Output

* updated_orders.json file:

  * Updates order status (Pending or Delayed)
  * Adds a message if the order is delayed

---

## How to Run

1. Install required libraries:
   pip install aiohttp python-dotenv

2. Create a .env file and add your API key:
   API_KEY=your_openweathermap_api_key

3. Run the script:
   python main.py

---

## Example Output

{
"order_id": "1003",
"customer": "Charlie Green",
"city": "London",
"status": "Delayed",
"message": "Hi Charlie Green, your order to London is delayed due to clouds. We appreciate your patience!"
}

---

## Example

If the weather is bad (like rain or clouds), the order will be marked as delayed and a message will be added.

---

## What I Learned

* How to use asyncio for parallel API calls
* How to work with real-time APIs
* Handling errors without breaking the program
* Reading and writing JSON files in Python

---

## AI Log

1. "Write Python code using asyncio and aiohttp to fetch multiple API requests concurrently using asyncio.gather."
2. "How to handle API errors in aiohttp without crashing the program and continue execution for other tasks?"
3. "Write Python logic to mark orders as delayed if weather conditions are Rain, Snow, or Extreme."
4. "Generate a Python function that creates a personalized apology message using customer name, city, and weather condition."

---

