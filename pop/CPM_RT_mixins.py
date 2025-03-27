from pop.CPM_RT_mongo_models import RTModelCPM, TodayRTModelCPM, Last7DaysRTModelCPM, Last30DaysRTModelCPM, ThisYearRTModelCPM

import logging
logger = logging.getLogger(__name__)

def rt_mongo_create(data, topic):
    rt_data = {}

    for dic in data:
        for key, value in dic.items():
            rt_data[key] = value


    rt_mongo_cpm = RTModelCPM.objects.create(

        # _id = mongo_models.ObjectIdField()
        # created_date = mongo_models.DateField(auto_now_add=True)
        # created_time = mongo_models.TimeField(auto_now_add=True)
        
        device_code = rt_data.get('id', None),
        topic = topic,
        ua = rt_data.get('ua', None),
        ub = rt_data.get('ub', None),
        uc = rt_data.get('uc', None),
        ia = rt_data.get('ia', None),
        ib = rt_data.get('ib', None),
        ic = rt_data.get('ic', None),
        uab = rt_data.get('uab', None),
        ubc = rt_data.get('ubc', None),
        uca = rt_data.get('uca', None),
        pa = rt_data.get('pa', None),
        pb = rt_data.get('pb', None),
        pc = rt_data.get('pc', None),
        zyggl = rt_data.get('zyggl', None),
        qa = rt_data.get('qa', None),
        qb = rt_data.get('qb', None),
        qc = rt_data.get('qc', None),
        zwggl = rt_data.get('zwggl', None),
        sa = rt_data.get('sa', None),
        sb = rt_data.get('sb', None),
        sc = rt_data.get('sc', None),
        zszgl = rt_data.get('zszgl', None),
        pfa = rt_data.get('pfa', None),
        pfb = rt_data.get('pfb', None),
        pfc = rt_data.get('pfc', None),
        zglys = rt_data.get('zglys', None),
        f = rt_data.get('f', None),
        u0 = rt_data.get('u0', None),
        u_plus = rt_data.get('u_plus', None),
        u_minus = rt_data.get('u_minus', None),
        i0 = rt_data.get('i0', None),
        i_plus = rt_data.get('i_plus', None),
        i_minus = rt_data.get('i_minus', None),
        uxja = rt_data.get('uxja', None),
        uxjb = rt_data.get('uxjb', None),
        uxjc = rt_data.get('uxjc', None),
        ixja = rt_data.get('ixja', None),
        ixjb = rt_data.get('ixjb', None),
        ixjc = rt_data.get('ixjc', None),
        unb = rt_data.get('unb', None),
        inb = rt_data.get('inb', None),
        pdm = rt_data.get('pdm', None),
        qdm = rt_data.get('qdm', None),
        sdm = rt_data.get('sdm', None),
    )

    logger.info(f"mongo_db = RTModelCPM, topic = {topic} created {rt_mongo_cpm._id} succesfully")
    print('<!---------------------------Data successfully inserted in RTModelCPM------------------------------!>')
    

    today_rt_mongo_cpm = TodayRTModelCPM.objects.create(

        # _id = mongo_models.ObjectIdField()
        # created_date = mongo_models.DateField(auto_now_add=True)
        # created_time = mongo_models.TimeField(auto_now_add=True)
        
        device_code = rt_data.get('id', None),
        topic = topic,
        ua = rt_data.get('ua', None),
        ub = rt_data.get('ub', None),
        uc = rt_data.get('uc', None),
        ia = rt_data.get('ia', None),
        ib = rt_data.get('ib', None),
        ic = rt_data.get('ic', None),
        # uab = rt_data.get('uab', None),
        # ubc = rt_data.get('ubc', None),
        # uca = rt_data.get('uca', None),
        pa = rt_data.get('pa', None),
        pb = rt_data.get('pb', None),
        pc = rt_data.get('pc', None),
        zyggl = rt_data.get('zyggl', None),
        # qa = rt_data.get('qa', None),
        # qb = rt_data.get('qb', None),
        # qc = rt_data.get('qc', None),
        # zwggl = rt_data.get('zwggl', None),
        # sa = rt_data.get('sa', None),
        # sb = rt_data.get('sb', None),
        # sc = rt_data.get('sc', None),
        # zszgl = rt_data.get('zszgl', None),
        pfa = rt_data.get('pfa', None),
        pfb = rt_data.get('pfb', None),
        pfc = rt_data.get('pfc', None),
        zglys = rt_data.get('zglys', None),
        f = rt_data.get('f', None),
        # u0 = rt_data.get('u0', None),
        # u_plus = rt_data.get('u_plus', None),
        # u_minus = rt_data.get('u_minus', None),
        # i0 = rt_data.get('i0', None),
        # i_plus = rt_data.get('i_plus', None),
        # i_minus = rt_data.get('i_minus', None),
        # uxja = rt_data.get('uxja', None),
        # uxjb = rt_data.get('uxjb', None),
        # uxjc = rt_data.get('uxjc', None),
        # ixja = rt_data.get('ixja', None),
        # ixjb = rt_data.get('ixjb', None),
        # ixjc = rt_data.get('ixjc', None),
        # unb = rt_data.get('unb', None),
        # inb = rt_data.get('inb', None),
        pdm = rt_data.get('pdm', None),
        qdm = rt_data.get('qdm', None),
        sdm = rt_data.get('sdm', None),
    )

    logger.info(f"mongo_db = TodayRTModelCPM, topic = {topic} created {today_rt_mongo_cpm._id} succesfully")
    print('<!---------------------------Data successfully inserted in TodayRTModelCPM------------------------------!>')


    last7days_rt_mongo_cpm = Last7DaysRTModelCPM.objects.create(
        device_code = rt_data.get('id', None),
        topic = topic,
        ua = rt_data.get('ua', None),
        ub = rt_data.get('ub', None),
        uc = rt_data.get('uc', None),
        ia = rt_data.get('ia', None),
        ib = rt_data.get('ib', None),
        ic = rt_data.get('ic', None),
        # uab = rt_data.get('uab', None),
        # ubc = rt_data.get('ubc', None),
        # uca = rt_data.get('uca', None),
        pa = rt_data.get('pa', None),
        pb = rt_data.get('pb', None),
        pc = rt_data.get('pc', None),
        zyggl = rt_data.get('zyggl', None),
        # qa = rt_data.get('qa', None),
        # qb = rt_data.get('qb', None),
        # qc = rt_data.get('qc', None),
        # zwggl = rt_data.get('zwggl', None),
        # sa = rt_data.get('sa', None),
        # sb = rt_data.get('sb', None),
        # sc = rt_data.get('sc', None),
        # zszgl = rt_data.get('zszgl', None),
        pfa = rt_data.get('pfa', None),
        pfb = rt_data.get('pfb', None),
        pfc = rt_data.get('pfc', None),
        zglys = rt_data.get('zglys', None),
        f = rt_data.get('f', None),
        # u0 = rt_data.get('u0', None),
        # u_plus = rt_data.get('u_plus', None),
        # u_minus = rt_data.get('u_minus', None),
        # i0 = rt_data.get('i0', None),
        # i_plus = rt_data.get('i_plus', None),
        # i_minus = rt_data.get('i_minus', None),
        # uxja = rt_data.get('uxja', None),
        # uxjb = rt_data.get('uxjb', None),
        # uxjc = rt_data.get('uxjc', None),
        # ixja = rt_data.get('ixja', None),
        # ixjb = rt_data.get('ixjb', None),
        # ixjc = rt_data.get('ixjc', None),
        # unb = rt_data.get('unb', None),
        # inb = rt_data.get('inb', None),
        pdm = rt_data.get('pdm', None),
        qdm = rt_data.get('qdm', None),
        sdm = rt_data.get('sdm', None),
    )

    logger.info(f"mongo_db = Last7DaysRTModelCPM, topic = {topic} created {last7days_rt_mongo_cpm._id} succesfully")
    print('<!---------------------------Data successfully inserted in Last7DaysRTModelCPM------------------------------!>')

    last30days_rt_mongo_cpm = Last30DaysRTModelCPM.objects.create(
        device_code = rt_data.get('id', None),
        topic = topic,
        ua = rt_data.get('ua', None),
        ub = rt_data.get('ub', None),
        uc = rt_data.get('uc', None),
        ia = rt_data.get('ia', None),
        ib = rt_data.get('ib', None),
        ic = rt_data.get('ic', None),
        # uab = rt_data.get('uab', None),
        # ubc = rt_data.get('ubc', None),
        # uca = rt_data.get('uca', None),
        pa = rt_data.get('pa', None),
        pb = rt_data.get('pb', None),
        pc = rt_data.get('pc', None),
        zyggl = rt_data.get('zyggl', None),
        # qa = rt_data.get('qa', None),
        # qb = rt_data.get('qb', None),
        # qc = rt_data.get('qc', None),
        # zwggl = rt_data.get('zwggl', None),
        # sa = rt_data.get('sa', None),
        # sb = rt_data.get('sb', None),
        # sc = rt_data.get('sc', None),
        # zszgl = rt_data.get('zszgl', None),
        pfa = rt_data.get('pfa', None),
        pfb = rt_data.get('pfb', None),
        pfc = rt_data.get('pfc', None),
        zglys = rt_data.get('zglys', None),
        f = rt_data.get('f', None),
        # u0 = rt_data.get('u0', None),
        # u_plus = rt_data.get('u_plus', None),
        # u_minus = rt_data.get('u_minus', None),
        # i0 = rt_data.get('i0', None),
        # i_plus = rt_data.get('i_plus', None),
        # i_minus = rt_data.get('i_minus', None),
        # uxja = rt_data.get('uxja', None),
        # uxjb = rt_data.get('uxjb', None),
        # uxjc = rt_data.get('uxjc', None),
        # ixja = rt_data.get('ixja', None),
        # ixjb = rt_data.get('ixjb', None),
        # ixjc = rt_data.get('ixjc', None),
        # unb = rt_data.get('unb', None),
        # inb = rt_data.get('inb', None),
        pdm = rt_data.get('pdm', None),
        qdm = rt_data.get('qdm', None),
        sdm = rt_data.get('sdm', None),
    )

    logger.info(f"mongo_db = Last30DaysRTModelCPM, topic = {topic} created {last30days_rt_mongo_cpm._id} succesfully")
    print('<!---------------------------Data successfully inserted in Last30DaysRTModelCPM------------------------------!>')


    this_year_rt_mongo_cpm = ThisYearRTModelCPM.objects.create(
        device_code = rt_data.get('id', None),
        topic = topic,
        ua = rt_data.get('ua', None),
        ub = rt_data.get('ub', None),
        uc = rt_data.get('uc', None),
        ia = rt_data.get('ia', None),
        ib = rt_data.get('ib', None),
        ic = rt_data.get('ic', None),
        # uab = rt_data.get('uab', None),
        # ubc = rt_data.get('ubc', None),
        # uca = rt_data.get('uca', None),
        pa = rt_data.get('pa', None),
        pb = rt_data.get('pb', None),
        pc = rt_data.get('pc', None),
        zyggl = rt_data.get('zyggl', None),
        # qa = rt_data.get('qa', None),
        # qb = rt_data.get('qb', None),
        # qc = rt_data.get('qc', None),
        # zwggl = rt_data.get('zwggl', None),
        # sa = rt_data.get('sa', None),
        # sb = rt_data.get('sb', None),
        # sc = rt_data.get('sc', None),
        # zszgl = rt_data.get('zszgl', None),
        pfa = rt_data.get('pfa', None),
        pfb = rt_data.get('pfb', None),
        pfc = rt_data.get('pfc', None),
        zglys = rt_data.get('zglys', None),
        f = rt_data.get('f', None),
        # u0 = rt_data.get('u0', None),
        # u_plus = rt_data.get('u_plus', None),
        # u_minus = rt_data.get('u_minus', None),
        # i0 = rt_data.get('i0', None),
        # i_plus = rt_data.get('i_plus', None),
        # i_minus = rt_data.get('i_minus', None),
        # uxja = rt_data.get('uxja', None),
        # uxjb = rt_data.get('uxjb', None),
        # uxjc = rt_data.get('uxjc', None),
        # ixja = rt_data.get('ixja', None),
        # ixjb = rt_data.get('ixjb', None),
        # ixjc = rt_data.get('ixjc', None),
        # unb = rt_data.get('unb', None),
        # inb = rt_data.get('inb', None),
        pdm = rt_data.get('pdm', None),
        qdm = rt_data.get('qdm', None),
        sdm = rt_data.get('sdm', None),
    )
    
    logger.info(f"mongo_db = ThisYearRTModelCPM, topic = {topic} created {this_year_rt_mongo_cpm._id} succesfully")
    print('<!---------------------------Data successfully inserted in ThisYearRTModelCPM------------------------------!>')    





