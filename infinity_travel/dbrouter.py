class AuthRouter(object):
    def __init__(self):
        self.model_list = ["admin", "accounts", "auth", "contenttypes", "sessions"]

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.model_list:
            return "user_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.model_list:
            return "user_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.model_list
            or obj2._meta.app_label in self.model_list
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.model_list:
            return db == "user_db"
        return None


class ChatRouter(object):
    def __init__(self):
        self.model_list = ["chat"]

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.model_list:
            return "chat_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.model_list:
            return "chat_db"
        return None

    # def allow_relation(self, obj1, obj2, **hints):
    #     if (
    #         obj1._meta.app_label in self.model_list
    #         or obj2._meta.app_label in self.model_list
    #     ):
    #         return True
    #     return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.model_list:
            return db == "chat_db"
        return None
