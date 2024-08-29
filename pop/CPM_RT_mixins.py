from pop.CPM_RT_mongo_models import RTModelCPM, TemporaryRTModelCPM, TodayRTModelCPM, Last7DaysRTModelCPM, Last30DaysRTModelCPM, ThisYearRTModelCPM

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
    
    temp_rt_mongo_cpm = TemporaryRTModelCPM.objects.create(

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

    logger.info(f"mongo_db = TemporaryRTModelCPM, topic = {topic} created {temp_rt_mongo_cpm._id} succesfully")
    print('<!---------------------------Data successfully inserted in TemporaryRTModelCPM------------------------------!>')

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


def date_wise_cpm_rt_mongo_create(data, device_code, topic, flag):

    # if not data.get('ua', 0.0) and \
    # not data.get('ub', 0.0) and \
    # not data.get('uc', 0.0) and \
    # not data.get('ia', 0.0) and \
    # not data.get('ib', 0.0) and \
    # not data.get('ic', 0.0) and \
    # not data.get('uab', 0.0) and \
    # not data.get('ubc', 0.0) and \
    # not data.get('uca', 0.0) and \
    # not data.get('pa', 0.0) and \
    # not data.get('pb', 0.0) and \
    # not data.get('pc', 0.0) and \
    # not data.get('zyggl', 0.0) and \
    # not data.get('qa', 0.0) and \
    # not data.get('qb', 0.0) and \
    # not data.get('qc', 0.0) and \
    # not data.get('zwggl', 0.0) and \
    # not data.get('sa', 0.0) and \
    # not data.get('sb', 0.0) and \
    # not data.get('sc', 0.0) and \
    # not data.get('zszgl', 0.0) and \
    # not data.get('pfa', 0.0) and \
    # not data.get('pfb', 0.0) and \
    # not data.get('pfc', 0.0) and \
    # not data.get('zglys', 0.0) and \
    # not data.get('f', 0.0) and \
    # not data.get('u0', 0.0) and \
    # not data.get('u_plus', 0.0) and \
    # not data.get('u_minus', 0.0) and \
    # not data.get('i0', 0.0) and \
    # not data.get('i_plus', 0.0) and \
    # not data.get('i_minus', 0.0) and \
    # not data.get('uxja', 0.0) and \
    # not data.get('uxjb', 0.0) and \
    # not data.get('uxjc', 0.0) and \
    # not data.get('ixja', 0.0) and \
    # not data.get('ixjb', 0.0) and \
    # not data.get('ixjc', 0.0) and \
    # not data.get('unb', 0.0) and \
    # not data.get('inb', 0.0) and \
    # not data.get('pdm', 0.0) and \
    # not data.get('qdm', 0.0) and \
    # not data.get('sdm', 0.0): 
    #     return ''
         
    if 'LAST_7_DAYS' in flag:
        last7days_rt_mongo_cpm = Last7DaysRTModelCPM.objects.create(
            device_code = device_code,
            topic = topic,
            ua = data.get('ua', None),
            ub = data.get('ub', None),
            uc = data.get('uc', None),
            ia = data.get('ia', None),
            ib = data.get('ib', None),
            ic = data.get('ic', None),
            # uab = data.get('uab', None),
            # ubc = data.get('ubc', None),
            # uca = data.get('uca', None),
            pa = data.get('pa', None),
            pb = data.get('pb', None),
            pc = data.get('pc', None),
            zyggl = data.get('zyggl', None),
            # qa = data.get('qa', None),
            # qb = data.get('qb', None),
            # qc = data.get('qc', None),
            # zwggl = data.get('zwggl', None),
            # sa = data.get('sa', None),
            # sb = data.get('sb', None),
            # sc = data.get('sc', None),
            # zszgl = data.get('zszgl', None),
            pfa = data.get('pfa', None),
            pfb = data.get('pfb', None),
            pfc = data.get('pfc', None),
            zglys = data.get('zglys', None),
            f = data.get('f', None),
            # u0 = data.get('u0', None),
            # u_plus = data.get('u_plus', None),
            # u_minus = data.get('u_minus', None),
            # i0 = data.get('i0', None),
            # i_plus = data.get('i_plus', None),
            # i_minus = data.get('i_minus', None),
            # uxja = data.get('uxja', None),
            # uxjb = data.get('uxjb', None),
            # uxjc = data.get('uxjc', None),
            # ixja = data.get('ixja', None),
            # ixjb = data.get('ixjb', None),
            # ixjc = data.get('ixjc', None),
            # unb = data.get('unb', None),
            # inb = data.get('inb', None),
            pdm = data.get('pdm', None),
            qdm = data.get('qdm', None),
            sdm = data.get('sdm', None),
        )

        logger.info(f"mongo_db = Last7DaysRTModelCPM, topic = {topic} created {last7days_rt_mongo_cpm._id} succesfully")
        print('<!---------------------------Data successfully inserted in Last7DaysRTModelCPM------------------------------!>')
    
    if 'LAST_30_DAYS' in flag:
        last30days_rt_mongo_cpm = Last30DaysRTModelCPM.objects.create(
            device_code = device_code,
            topic = topic,
            ua = data.get('ua', None),
            ub = data.get('ub', None),
            uc = data.get('uc', None),
            ia = data.get('ia', None),
            ib = data.get('ib', None),
            ic = data.get('ic', None),
            # uab = data.get('uab', None),
            # ubc = data.get('ubc', None),
            # uca = data.get('uca', None),
            pa = data.get('pa', None),
            pb = data.get('pb', None),
            pc = data.get('pc', None),
            zyggl = data.get('zyggl', None),
            # qa = data.get('qa', None),
            # qb = data.get('qb', None),
            # qc = data.get('qc', None),
            # zwggl = data.get('zwggl', None),
            # sa = data.get('sa', None),
            # sb = data.get('sb', None),
            # sc = data.get('sc', None),
            # zszgl = data.get('zszgl', None),
            pfa = data.get('pfa', None),
            pfb = data.get('pfb', None),
            pfc = data.get('pfc', None),
            zglys = data.get('zglys', None),
            f = data.get('f', None),
            # u0 = data.get('u0', None),
            # u_plus = data.get('u_plus', None),
            # u_minus = data.get('u_minus', None),
            # i0 = data.get('i0', None),
            # i_plus = data.get('i_plus', None),
            # i_minus = data.get('i_minus', None),
            # uxja = data.get('uxja', None),
            # uxjb = data.get('uxjb', None),
            # uxjc = data.get('uxjc', None),
            # ixja = data.get('ixja', None),
            # ixjb = data.get('ixjb', None),
            # ixjc = data.get('ixjc', None),
            # unb = data.get('unb', None),
            # inb = data.get('inb', None),
            pdm = data.get('pdm', None),
            qdm = data.get('qdm', None),
            sdm = data.get('sdm', None),
        )

        logger.info(f"mongo_db = Last30DaysRTModelCPM, topic = {topic} created {last30days_rt_mongo_cpm._id} succesfully")
        print('<!---------------------------Data successfully inserted in Last30DaysRTModelCPM------------------------------!>')
    
    if 'THIS_YEAR' in flag:
        this_year_rt_mongo_cpm = ThisYearRTModelCPM.objects.create(
            device_code = device_code,
            topic = topic,
            ua = data.get('ua', None),
            ub = data.get('ub', None),
            uc = data.get('uc', None),
            ia = data.get('ia', None),
            ib = data.get('ib', None),
            ic = data.get('ic', None),
            # uab = data.get('uab', None),
            # ubc = data.get('ubc', None),
            # uca = data.get('uca', None),
            pa = data.get('pa', None),
            pb = data.get('pb', None),
            pc = data.get('pc', None),
            zyggl = data.get('zyggl', None),
            # qa = data.get('qa', None),
            # qb = data.get('qb', None),
            # qc = data.get('qc', None),
            # zwggl = data.get('zwggl', None),
            # sa = data.get('sa', None),
            # sb = data.get('sb', None),
            # sc = data.get('sc', None),
            # zszgl = data.get('zszgl', None),
            pfa = data.get('pfa', None),
            pfb = data.get('pfb', None),
            pfc = data.get('pfc', None),
            zglys = data.get('zglys', None),
            f = data.get('f', None),
            # u0 = data.get('u0', None),
            # u_plus = data.get('u_plus', None),
            # u_minus = data.get('u_minus', None),
            # i0 = data.get('i0', None),
            # i_plus = data.get('i_plus', None),
            # i_minus = data.get('i_minus', None),
            # uxja = data.get('uxja', None),
            # uxjb = data.get('uxjb', None),
            # uxjc = data.get('uxjc', None),
            # ixja = data.get('ixja', None),
            # ixjb = data.get('ixjb', None),
            # ixjc = data.get('ixjc', None),
            # unb = data.get('unb', None),
            # inb = data.get('inb', None),
            pdm = data.get('pdm', None),
            qdm = data.get('qdm', None),
            sdm = data.get('sdm', None),
        )
        
        logger.info(f"mongo_db = ThisYearRTModelCPM, topic = {topic} created {this_year_rt_mongo_cpm._id} succesfully")
        print('<!---------------------------Data successfully inserted in ThisYearRTModelCPM------------------------------!>')



