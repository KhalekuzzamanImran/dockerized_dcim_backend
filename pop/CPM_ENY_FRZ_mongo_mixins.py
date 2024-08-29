from pop.CPM_ENY_FRZ_mongo_models import EnyFrzDataModelCPM

import logging
logger = logging.getLogger(__name__)

def eny_frz_mongo_create(data, topic):
    # rt_data = {}

    # for dic in data:
    #     for key, value in dic.items():
    #         rt_data[key] = value

    eny_frz_mongo_cpm = EnyFrzDataModelCPM.objects.create(
        device_code = data.setdefault('id', 'None'),
        topic = topic,
        zydvdd = data.setdefault('zydvdd', 0.0),
        fydvdd = data.setdefault('fydvdd', 0.0),
        zy6dd = data.setdefault('zy6dd', 0.0),
        fy6dd = data.setdefault('fy6dd', 0.0),
        mfhl = data.setdefault('mfhl', 0.0),
    )

    logger.info(f"mongo_db = EnyFrzDataModelCPM, topic = {topic} created {eny_frz_mongo_cpm._id} succesfully")
    print('<!---------------------------Data successfully inserted in EnyFrzDataModelCPM------------------------------!>')