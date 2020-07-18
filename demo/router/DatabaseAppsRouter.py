from django.conf import settings

class DatabaseAppsRouter:
    """
    A router to control all database operations on models in the
    user application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read user models go to users_db.
        """
        print('db_for_read called');
        print('mode meta app label is ',model._meta.app_label)
        if model._meta.app_label == 'user_dbs':
            return 'post_dbs'
        elif model._meta.app_label == 'customer_dbs':
            return 'mysql_dbs'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to users_db.
        """
        print('db_for_write called');
        print('model meta app label is ', model._meta.app_label)
        if model._meta.app_label == 'postgres_db':
            return 'post_dbs'
        elif model._meta.app_label == 'mysql_db':
            return 'mysql_dbs'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        print('allow relation called')
        if obj1._meta.app_label == 'postgres_db' or \
                obj2._meta.app_label == 'postgres_db':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print('migration called')
        print('db name is ',db)
        print('app label is',app_label)
        if app_label == 'postgres_db':
            return db == 'post_dbs'
        elif app_label == 'mysql_db':
            return db == 'mysql_dbs'
        return None
