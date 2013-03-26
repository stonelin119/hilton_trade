class AppRouter(object):
    dbs_for_write = {'master': 'master'}
    dbs_for_read = {'slave': 'slave'}

    def db_for_read(self, model, **hints):
        return self.__app_router(model, self.dbs_for_read)

    def db_for_write(self, model, **hints):
        return self.__app_router(model, self.dbs_for_write)

    def allow_relation(self, obj1, obj2, **hints):
        return obj1._meta.app_label == obj2._meta.app_label

    def allow_syncdb(self, db, model):
        return self.__app_router(model, self.dbs_for_write) == db

    def __app_router(self, model, dbs):
        return dbs.get(model._meta.app_label, 'default')
