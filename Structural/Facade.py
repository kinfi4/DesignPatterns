#  Такс, ну это вообще похоже не много ко инкапсуляцию, только прячем мы не только детали реализации конкретного класса
#  но и целой системы классов.

from Creational.MetaclassSingleton import Singleton


#  Этот класс и есть наш фасад
class DataBase(metaclass=Singleton):
    def __init__(self):
        self._migration_controller = MigrationController()
        self._query_controller = QueryController()

    def make_query(self, sql):
        self._query_controller.build_connection()
        self._query_controller.make_query(sql)

    def migrate(self):
        self._migration_controller.prepare_database()
        self._migration_controller.migrate()
        self._migration_controller.post_migrate_actions()


class MigrationController:
    def prepare_database(self):
        print('Database for migration prepared')

    def migrate(self):
        print('Making migration')

    def post_migrate_actions(self):
        print('Closing database')


class QueryController:
    def build_connection(self):
        print('building connection for querying')

    def make_query(self, sql):
        print(f'Querying with {sql}')


db = DataBase()

db.migrate()
db.make_query('SELECT * FROM db.people')
