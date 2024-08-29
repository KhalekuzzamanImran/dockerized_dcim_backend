from pop.CPM_ENY_NOW_mongo_models import EnyNowDataModelCPM, TemporaryEnyNowDataModelCPM, TodayEnyNowDataModelCPM, Last7DaysEnyNowDataModelCPM, Last30DaysEnyNowDataModelCPM, ThisYearEnyNowDataModelCPM

import logging
logger = logging.getLogger(__name__)

def eny_now_mongo_create(data, topic):
    eny_data = {}

    for dic in data:
        for key, value in dic.items():
            eny_data[key] = value


    eny_now_mongo_cpm = EnyNowDataModelCPM.objects.create(
        device_code = eny_data.get('id'),
        topic = topic,
        zygsz = eny_data.get('zygsz'),
        fygsz = eny_data.get('fygsz'),
        zwgsz = eny_data.get('zwgsz'),
        fwgsz = eny_data.get('fwgsz'),
        zyjsz = eny_data.get('zyjsz'),
        fyjsz = eny_data.get('fyjsz'),
        zyfsz = eny_data.get('zyfsz'),
        fyfsz = eny_data.get('fyfsz'),
        zypsz = eny_data.get('zypsz'),
        fypsz = eny_data.get('fypsz'),
        zyvsz = eny_data.get('zyvsz'),
        fyvsz = eny_data.get('fyvsz'),
        zydvsz = eny_data.get('zydvsz'),
        fydvsz = eny_data.get('fydvsz'),
        zy6sz = eny_data.get('zy6sz'),
        fy6sz = eny_data.get('fy6sz'),
        dmpmax = eny_data.get('dmpmax'),
        dmpmaxoct = eny_data.get('dmpmaxoct'),
        dmsmax = eny_data.get('dmsmax'),
        dmsmaxoct = eny_data.get('dmsmaxoct'),
        uathd = eny_data.get('uathd'),
        ubthd = eny_data.get('ubthd'),
        ucthd = eny_data.get('ucthd'),
        iathd = eny_data.get('iathd'),
        ibthd = eny_data.get('ibthd'),
        icthd = eny_data.get('icthd'),
        uaxbl3 = eny_data.get('uaxbl3'),
        ubxbl3 = eny_data.get('ubxbl3'),
        ucxbl3 = eny_data.get('ucxbl3'),
        iaxbl3 = eny_data.get('iaxbl3'),
        ibxbl3 = eny_data.get('ibxbl3'),
        icxbl3 = eny_data.get('icxbl3'),
        uaxbl5 = eny_data.get('uaxbl5'),
        ubxbl5 = eny_data.get('ubxbl5'),
        ucxbl5 = eny_data.get('ucxbl5'),
        iaxbl5 = eny_data.get('iaxbl5'),
        ibxbl5 = eny_data.get('ibxbl5'),
        icxbl5 = eny_data.get('icxbl5'),
        uaxbl7 = eny_data.get('uaxbl7'),
        ubxbl7 = eny_data.get('ubxbl7'),
        ucxbl7 = eny_data.get('ucxbl7'),
        iaxbl7 = eny_data.get('iaxbl7'),
        ibxbl7 = eny_data.get('ibxbl7'),
        icxbl7 = eny_data.get('icxbl7'),
        iaxb3 = eny_data.get('iaxb3'),
        ibxb3 = eny_data.get('ibxb3'),
        icxb3 = eny_data.get('icxb3'),
        iaxb5 = eny_data.get('iaxb5'),
        ibxb5 = eny_data.get('ibxb5'),
        icxb5 = eny_data.get('icxb5'),
        iaxb7 = eny_data.get('iaxb7'),
        ibxb7 = eny_data.get('ibxb7'),
        icxb7 = eny_data.get('icxb7'),
    )

    logger.info(f"mongo_db = EnyNowDataModelCPM, topic = {eny_now_mongo_cpm.topic} created {eny_now_mongo_cpm._id} succesfully")
    print('<!---------------------------Data successfully inserted in EnyNowDataModelCPM------------------------------!>')

    temp_eny_now_mongo_cpm = TemporaryEnyNowDataModelCPM.objects.create(
        device_code = eny_data.get('id'),
        topic = topic,
        zygsz = eny_data.get('zygsz'),
    )

    logger.info(f"mongo_db = TemporaryEnyNowDataModelCPM, topic = {temp_eny_now_mongo_cpm.topic} created {temp_eny_now_mongo_cpm._id} succesfully")
    print('<!---------------------------Data successfully inserted in TemporaryEnyNowDataModelCPM------------------------------!>')

    today_eny_now_mongo_cpm = TodayEnyNowDataModelCPM.objects.create(
        device_code = eny_data.get('id'),
        topic = topic,
        zygsz = eny_data.get('zygsz'),
    )

    logger.info(f"mongo_db = TodayEnyNowDataModelCPM, topic = {today_eny_now_mongo_cpm.topic} created {today_eny_now_mongo_cpm._id} succesfully")
    print('<!---------------------------Data successfully inserted in TodayEnyNowDataModelCPM------------------------------!>')

    last7days_eny_now_mongo_cpm = Last7DaysEnyNowDataModelCPM.objects.create(
        device_code = eny_data.get('id'),
        topic = topic,
        zygsz = eny_data.get('zygsz'),
    )

    logger.info(f"mongo_db = Last7DaysEnyNowDataModelCPM, topic = {last7days_eny_now_mongo_cpm.topic} created {last7days_eny_now_mongo_cpm._id} succesfully")
    print('<!---------------------------Data successfully inserted in Last7DaysEnyNowDataModelCPM------------------------------!>')

    

def date_wise_cpm_enynow_mongo_create(data, device_code, topic, flag):
    if 'LAST_30_DAYS' in flag:
        last30days_eny_now_mongo_cpm = Last30DaysEnyNowDataModelCPM.objects.create(
        device_code = device_code,
        topic = topic,
        zygsz = data.get('zygsz'),
        )
        
        logger.info(f"mongo_db = Last30DaysEnyNowDataModelCPM, topic = {last30days_eny_now_mongo_cpm.topic} created {last30days_eny_now_mongo_cpm._id} succesfully")
        print('<!---------------------------Data successfully inserted in Last30DaysEnyNowDataModelCPM------------------------------!>')

    if 'THIS_YEAR' in flag:
        thisyear_eny_now_mongo_cpm = ThisYearEnyNowDataModelCPM.objects.create(
        device_code = device_code,
        topic = topic,
        zygsz = data.get('zygsz'),
        )
        
        logger.info(f"mongo_db = ThisYearEnyNowDataModelCPM, topic = {thisyear_eny_now_mongo_cpm.topic} created {thisyear_eny_now_mongo_cpm._id} succesfully")
        print('<!---------------------------Data successfully inserted in ThisYearEnyNowDataModelCPM------------------------------!>')