from djongo import models as mongo_models
from pop.CCCL_generator_mongo_model import CCCLGenerator, TemporaryCCCLGenerator, TodayCCCLGenerator, Last7DaysCCCLGenerator, Last30DaysCCCLGenerator, ThisYearCCCLGenerator

import logging
logger = logging.getLogger(__name__)

def cccl_enm_mongo_create(data, topic):
    rt_data = {}
    temp_list = data.get('data')[0].get('point')

    for dic in temp_list:
        if dic.get('id') == 1:
            rt_data['ua'] = dic.get('val')
        elif dic.get('id') == 2:
            rt_data['ub'] = dic.get('val')
        elif dic.get('id') == 3:
            rt_data['uc'] = dic.get('val')
        elif dic.get('id') == 7:
            rt_data['ia'] = dic.get('val')
        elif dic.get('id') == 8:
            rt_data['ib'] = dic.get('val')
        elif dic.get('id') == 9:
            rt_data['ic'] = dic.get('val')
        elif dic.get('id') == 10:
            rt_data['pa'] = dic.get('val')
        elif dic.get('id') == 11:
            rt_data['pb'] = dic.get('val')
        elif dic.get('id') == 12:
            rt_data['pc'] = dic.get('val')
        elif dic.get('id') == 13:
            rt_data['zyggl'] = dic.get('val')
        elif dic.get('id') == 22:
            rt_data['pfa'] = dic.get('val')
        elif dic.get('id') == 23:
            rt_data['pfb'] = dic.get('val')
        elif dic.get('id') == 24:
            rt_data['pfc'] = dic.get('val')
        elif dic.get('id') == 25:
            rt_data['zglys'] = dic.get('val')
        elif dic.get('id') == 26:
            rt_data['f'] = dic.get('val')

    # print(rt_data)
    cccl_mongo = CCCLGenerator.objects.create(

        device_code = rt_data.get('id', '3071523B00003'),
        topic = topic,
        ua = rt_data.get('ua', None),
        ub = rt_data.get('ub', None),
        uc = rt_data.get('uc', None),
        ia = rt_data.get('ia', None),
        ib = rt_data.get('ib', None),
        ic = rt_data.get('ic', None),
        pa = rt_data.get('pa', None),
        pb = rt_data.get('pb', None),
        pc = rt_data.get('pc', None),
        zyggl = rt_data.get('zyggl', None),
        pfa = rt_data.get('pfa', None),
        pfb = rt_data.get('pfb', None),
        pfc = rt_data.get('pfc', None),
        zglys = rt_data.get('zglys', None),
        f = rt_data.get('f', None),
    ) 

    logger.info(f"mongo_db = CCCLGenerator, topic = {topic} created {cccl_mongo._id} succesfully")
    print('<!---------------------------Data successfully inserted in CCCLGenerator------------------------------!>')

    temporary_cccl_mongo = TemporaryCCCLGenerator.objects.create(

        device_code = rt_data.get('id', '3071523B00003'),
        topic = topic,
        ua = rt_data.get('ua', None),
        ub = rt_data.get('ub', None),
        uc = rt_data.get('uc', None),
        ia = rt_data.get('ia', None),
        ib = rt_data.get('ib', None),
        ic = rt_data.get('ic', None),
        pa = rt_data.get('pa', None),
        pb = rt_data.get('pb', None),
        pc = rt_data.get('pc', None),
        zyggl = rt_data.get('zyggl', None),
        pfa = rt_data.get('pfa', None),
        pfb = rt_data.get('pfb', None),
        pfc = rt_data.get('pfc', None),
        zglys = rt_data.get('zglys', None),
        f = rt_data.get('f', None),
    ) 

    logger.info(f"mongo_db = TemporaryCCCLGenerator, topic = {topic} created {temporary_cccl_mongo._id} succesfully")
    print('<!---------------------------Data successfully inserted in TemporaryCCCLGenerator------------------------------!>')

    today_cccl_mongo = TodayCCCLGenerator.objects.create(

        device_code = rt_data.get('id', '3071523B00003'),
        topic = topic,
        ua = rt_data.get('ua', None),
        ub = rt_data.get('ub', None),
        uc = rt_data.get('uc', None),
        ia = rt_data.get('ia', None),
        ib = rt_data.get('ib', None),
        ic = rt_data.get('ic', None),
        pa = rt_data.get('pa', None),
        pb = rt_data.get('pb', None),
        pc = rt_data.get('pc', None),
        zyggl = rt_data.get('zyggl', None),
        pfa = rt_data.get('pfa', None),
        pfb = rt_data.get('pfb', None),
        pfc = rt_data.get('pfc', None),
        zglys = rt_data.get('zglys', None),
        f = rt_data.get('f', None),
    ) 

    logger.info(f"mongo_db = TodayCCCLGenerator, topic = {topic} created {today_cccl_mongo._id} succesfully")
    print('<!---------------------------Data successfully inserted in TodayCCCLGenerator------------------------------!>')


def date_wise_cccl_generator_mongo_create(data, device_code, topic, flag):
    if 'LAST_7_DAYS' in flag:
        last7days_cccl_mongo = Last7DaysCCCLGenerator.objects.create(
            device_code = device_code,
            topic = topic,
            ua = data.get('ua', None),
            ub = data.get('ub', None),
            uc = data.get('uc', None),
            ia = data.get('ia', None),
            ib = data.get('ib', None),
            ic = data.get('ic', None),
            pa = data.get('pa', None),
            pb = data.get('pb', None),
            pc = data.get('pc', None),
            zyggl = data.get('zyggl', None),
            pfa = data.get('pfa', None),
            pfb = data.get('pfb', None),
            pfc = data.get('pfc', None),
            zglys = data.get('zglys', None),
            f = data.get('f', None),
        )

        logger.info(f"mongo_db = Last7DaysCCCLGenerator, topic = {topic} created {last7days_cccl_mongo._id} succesfully")
        print('<!---------------------------Data successfully inserted in Last7DaysCCCLGenerator------------------------------!>')
    
    if 'LAST_30_DAYS' in flag:
        last30days_cccl_mongo = Last30DaysCCCLGenerator.objects.create(
            device_code = device_code,
            topic = topic,
            ua = data.get('ua', None),
            ub = data.get('ub', None),
            uc = data.get('uc', None),
            ia = data.get('ia', None),
            ib = data.get('ib', None),
            ic = data.get('ic', None),
            pa = data.get('pa', None),
            pb = data.get('pb', None),
            pc = data.get('pc', None),
            zyggl = data.get('zyggl', None),
            pfa = data.get('pfa', None),
            pfb = data.get('pfb', None),
            pfc = data.get('pfc', None),
            zglys = data.get('zglys', None),
            f = data.get('f', None),
        )

        logger.info(f"mongo_db = Last30DaysCCCLGenerator, topic = {topic} created {last30days_cccl_mongo._id} succesfully")
        print('<!---------------------------Data successfully inserted in Last30DaysCCCLGenerator------------------------------!>')

    if "THIS_YEAR" in flag:
        thisyear_cccl_mongo = ThisYearCCCLGenerator.objects.create(
            device_code = device_code,
            topic = topic,
            ua = data.get('ua', None),
            ub = data.get('ub', None),
            uc = data.get('uc', None),
            ia = data.get('ia', None),
            ib = data.get('ib', None),
            ic = data.get('ic', None),
            pa = data.get('pa', None),
            pb = data.get('pb', None),
            pc = data.get('pc', None),
            zyggl = data.get('zyggl', None),
            pfa = data.get('pfa', None),
            pfb = data.get('pfb', None),
            pfc = data.get('pfc', None),
            zglys = data.get('zglys', None),
            f = data.get('f', None),
        )

        logger.info(f"mongo_db = ThisYearCCCLGenerator, topic = {topic} created {thisyear_cccl_mongo._id} succesfully")
        print('<!---------------------------Data successfully inserted in ThisYearCCCLGenerator------------------------------!>')


