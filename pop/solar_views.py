from rest_framework import viewsets, status
from rest_framework.response import Response
from pymongo import MongoClient
from .solar_serializers import SolarReadingSerializer
import math
from bson import ObjectId

# MongoDB Connection
MONGO_URI = "mongodb://root:root@165.22.221.252:27017/"
client = MongoClient(MONGO_URI)
db = client["dcim"]  # Replace with actual database name

class SolarEnergyConsumptionViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            # Map time_range to collections
            collection_map = {
                "TODAY": "pop_today_solar_readings",
                "LAST_30_DAYS": "pop_thismonth_solar_readings",
                "THIS_YEAR": "pop_solar_readings"
            }
            time_range = request.query_params.get("time_range", "TODAY").upper()
            collection_name = collection_map.get(time_range, "pop_solar_readings")
            collection = db[collection_name]

            first_entry = collection.find_one(sort=[('_id', 1)])
            last_entry = collection.find_one(sort=[('_id', -1)])

            if not first_entry or not last_entry:
                return Response({
                    "energy_consumption": 0,
                    "time_range": time_range,
                    "first_timestamp": None,
                    "last_timestamp": None,
                    "message": "No data found for selected time range"
                })

            first_value = first_entry.get('energy_consumption', [0])[0]
            last_value = last_entry.get('energy_consumption', [0])[0]

            energy_consumption = last_value - first_value

            return Response({
                "energy_consumption": energy_consumption,
                "time_range": time_range,
                "first_timestamp": first_entry.get('timestamp'),
                "last_timestamp": last_entry.get('timestamp')
            })

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class SolarReadingViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            # Map time_range to collections
            collection_map = {
                "TODAY": "pop_today_solar_readings",
                "LAST_30_DAYS": "pop_thismonth_solar_readings",
                "THIS_YEAR": "pop_solar_readings"
            }
            time_range = request.query_params.get("time_range", "TODAY").upper()
            collection_name = collection_map.get(time_range, "pop_solar_readings")
            collection = db[collection_name]

            print(time_range)

            # Fetch and sanitize data
            readings = [sanitize_data(reading) for reading in collection.find({})]

            return Response(SolarReadingSerializer(readings, many=True).data)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def sanitize_data(data):
    """Recursively sanitize data, converting ObjectId and handling invalid floats."""
    if isinstance(data, dict):
        return {k: sanitize_data(v) for k, v in data.items()}
    if isinstance(data, list):
        return [sanitize_data(item) for item in data]
    if isinstance(data, ObjectId):
        return str(data)
    if isinstance(data, float) and (math.isnan(data) or math.isinf(data)):
        return None  # Replace with 0 if required
    return data





# class SolarReadingViewSet(viewsets.ViewSet):
#     def list(self, request):
#         try:
#             # Get the 'time_range' query parameter
#             time_range = request.query_params.get('time_range', 'TODAY').upper()

#             # Define timezone for UTC
#             utc_tz = pytz.utc

#             # Get current time in UTC
#             now = datetime.now(utc_tz)

#             # Prepare filter
#             filter_query = {}

#             if time_range == 'TODAY':
#                 start_time = now.astimezone(utc_tz).replace(hour=0, minute=0, second=0, microsecond=0)
#             elif time_range == "LAST_7_DAYS":
#                 start_time = (now - timedelta(days=7)).astimezone(utc_tz)
#             elif time_range == "LAST_30_DAYS":
#                 start_time = (now - timedelta(days=30)).astimezone(utc_tz)
#             elif time_range == "THIS_YEAR":
#                 start_time = datetime(now.year, 1, 1, tzinfo=utc_tz)
#             else:
#                 start_time = None  # Handle unexpected values

#             if start_time:
#                 filter_query["timestamp"] = {"$gte": start_time}

#             print(f"✅ Corrected Filter Query: {filter_query}")  # Debugging output

#             # Fetch data
#             readings = list(collection.find({}))
#             readings = [sanitize_data(reading) for reading in readings]

#             # Convert ObjectId to string
#             for reading in readings:
#                 reading["_id"] = str(reading["_id"])

#             return Response(SolarReadingSerializer(readings, many=True).data)

#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


