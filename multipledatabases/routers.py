class BasicRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'customers':
            return 'customers'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'customers':
            return 'customers'

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == 'customers':
            return (db == 'customers')
        else:
            return (db == 'default')
