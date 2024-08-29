from pop.CPM_DAY_DATA_mongo_models import DayDataModelCPM

import logging
logger = logging.getLogger(__name__)


def day_data_mongo_create(data, topic):
    # rt_data = {}

    # for dic in data:
    #     for key, value in dic.items():
    #         rt_data[key] = value

    today_rt_mongo_cpm = DayDataModelCPM.objects.create(
        device_code = data.get('id'),
        topic = topic,
        zydvsz = data.get('zydvsz', None),
        fydvsz = data.get('fydvsz', None),
        zy6sz = data.get('zy6sz', None),
        fy6sz = data.get('fy6sz', None),
    )

    logger.info(f"mongo_db = DayDataModelCPM, topic = {topic} created {today_rt_mongo_cpm._id} succesfully")
    print('<!---------------------------Data successfully inserted in DayDataModelCPM------------------------------!>')