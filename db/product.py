from table import Table


class Product(Table):
    def __init__(self, name, target_table):
        super().__init__(name)
        self.target_table = target_table

    async def create_table_sql(self):
        return f'''CREATE TABLE IF NOT EXISTS {self.schema}.{self.name} (
            id BIGINT PRIMARY KEY,
            name TEXT NOT NULL,
            price BIGINT NOT NULL,
            category_id BIGINT NOT NULL,
            product_group TEXT NOT NULL,
            CONSTRAINT "FK_product_category" 
                FOREIGN KEY (category_id) REFERENCES {self.schema}.{self.target_table} (id) ON DELETE CASCADE
        );'''

    async def insert_sql(self, values):
        return f'''INSERT INTO {self.schema}.{self.name} (id, name, price, category_id, product_group)
        VALUES ({values[0]}, '{values[1].replace("'", "`")}', {values[2]}, {values[3]}, '{values[4]}');'''

