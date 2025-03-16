# time_range = self.request.query_params.get('time_range', None)
        # print(time_range)

        # if time_range:
        #     now = timezone.now()

        #     if time_range == 'TODAY':
        #         start_time = timezone.make_aware(timezone.datetime(now.year, now.month, now.day, 0, 0, 0))
        #     elif time_range == "LAST_7_DAYS":
        #         start_time = now - timedelta(days=7)
        #     elif time_range == "LAST_30_DAYS":
        #         start_time = now - timedelta(days=30)
        #     elif time_range == "THIS_YEAR":
        #         start_time = timezone.make_aware(timezone.datetime(now.year, 1, 1))
        #     else:
        #         return queryset 
            
        #     queryset = queryset.filter(timestamp__gte=start_time)



# Debugging raw pymongo query
        from pymongo import MongoClient
        from django.conf import settings

        mongo_config = settings.DATABASES['nonrel']['CLIENT']
        client = MongoClient(
            host=mongo_config["host"],
            port=int(mongo_config["port"]),
            username=mongo_config["username"],
            password=mongo_config["password"]
        )

        db = client[settings.DATABASES["nonrel"]["NAME"]]
        raw_count = db["pop_upsdata"].count_documents({})
        print("Raw Count from MongoDB:", raw_count)  # Should match Django ORM count