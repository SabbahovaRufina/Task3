from table import Table


class Category(Table):
    def __init__(self, name):
        super().__init__(name)

    async def create_table_sql(self):
        return f'''CREATE TABLE IF NOT EXISTS {self.schema}.{self.name} (
            id BIGINT PRIMARY KEY,
            name VARCHAR(40) NOT NULL
        );'''

    async def insert_sql(self, values):
        return f'''INSERT INTO {self.schema}.{self.name} (id, name)
        VALUES ({values[1]}, '{values[0]}');'''

