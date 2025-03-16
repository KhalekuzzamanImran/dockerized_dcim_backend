class NonRelRouter:
    """
    A router to control if database should use
    primary database or non-relational one.
    """
    nonrel_models = {
        'yearlytuyaenergymetermongo', 
        'dailytuyaenergymetermongo', 
        'hourlytuyaenergymetermongo', 
        'tuyaenergymetermongo', 
        'temptuyaenergymetermongo', 
        'todaytuyaenergymetermongo', 
        'tempairqualitymongo', 
        'airqualitymongo', 
        'todayairqualitymongo', 
        'thisweekairqualitymongo', 
        'thismonthairqualitymongo', 
        'thisyearairqualitymongo',

        'rtmodelcpm',
        'temporaryrtmodelcpm',
        'todayrtmodelcpm',
        'last7daysrtmodelcpm',
        'last30daysrtmodelcpm',
        'thisyearrtmodelcpm',

        'enynowdatamodelcpm',
        'temporaryenynowdatamodelcpm',
        'todayenynowdatamodelcpm',
        'last7daysenynowdatamodelcpm',
        'last30daysenynowdatamodelcpm',
        'thisyearenynowdatamodelcpm',

        'daydatamodelcpm',
        'enyfrzdatamodelcpm', 

        'thermohygrometermongomodel',
        'tempthermohygrometermongomodel',
        'todaythermohygrometermongomodel',
        'last7daysthermohygrometermongomodel',
        'last30daysthermohygrometermongomodel',
        'thisyearthermohygrometermongomodel',

        'ccclgenerator', 'temporaryccclgenerator', 'todayccclgenerator', 'last7daysccclgenerator', 'last30daysccclgenerator', 'thisyearccclgenerator',
        'ccclenvironment', 'temporaryccclenvironment', 'todayccclenvironment', 'last7daysccclenvironment', 'last30daysccclenvironment', 'thisyearccclenvironment', 
        'upsmodel',
    }

    def db_for_read(self, model, **_hints):
        if model._meta.model_name in self.nonrel_models:
            return 'nonrel'
        return 'default'

    def db_for_write(self, model, **_hints):
        if model._meta.model_name in self.nonrel_models:
            return 'nonrel'
        return 'default'

    def allow_migrate(self, _db, _app_label, model_name=None, **_hints):
        if _db == 'nonrel' or model_name in self.nonrel_models:
            return False
        return True
