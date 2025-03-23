from rest_framework import viewsets
from rest_framework.response import Response
from bson import ObjectId
from pymongo import MongoClient
from rest_framework import status
from .solar_serializers import SolarReadingSerializer
import math  # For handling float validation
from datetime import datetime, timedelta
from django.utils import timezone
import pytz

# MongoDB URI
MONGO_URI = "mongodb://root:root@165.22.221.252:27017/"

# Create MongoDB Client
client = MongoClient(MONGO_URI)
db = client["dcim"]  # Replace with your actual database name
collection = db["pop_solar_readings"]

class SolarReadingViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            # Get the 'time_range' query parameter
            time_range = request.query_params.get('time_range', 'TODAY').upper()

            # Define timezone for UTC
            utc_tz = pytz.utc

            # Get current time in UTC
            now = datetime.now(utc_tz)

            # Prepare filter
            filter_query = {}

            if time_range == 'TODAY':
                start_time = now.astimezone(utc_tz).replace(hour=0, minute=0, second=0, microsecond=0)
            elif time_range == "LAST_7_DAYS":
                start_time = (now - timedelta(days=7)).astimezone(utc_tz)
            elif time_range == "LAST_30_DAYS":
                start_time = (now - timedelta(days=30)).astimezone(utc_tz)
            elif time_range == "THIS_YEAR":
                start_time = datetime(now.year, 1, 1, tzinfo=utc_tz)
            else:
                start_time = None  # Handle unexpected values

            if start_time:
                filter_query["timestamp"] = {"$gte": start_time}

            print(f"✅ Corrected Filter Query: {filter_query}")  # Debugging output

            # Fetch data
            readings = list(collection.find({}))
            readings = [sanitize_data(reading) for reading in readings]

            # Convert ObjectId to string
            for reading in readings:
                reading["_id"] = str(reading["_id"])

            return Response(SolarReadingSerializer(readings, many=True).data)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# Helper function to sanitize invalid float values
def sanitize_data(data):
    """Sanitize data to remove or replace invalid float values like NaN, Infinity, or -Infinity."""
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = sanitize_data(value)  # Recurse for nested dictionaries
    elif isinstance(data, list):
        for i in range(len(data)):
            data[i] = sanitize_data(data[i])  # Recurse for list items
    elif isinstance(data, float):
        if math.isnan(data) or math.isinf(data):
            return None  # or replace with 0, depending on your use case
    return data
