import asyncio
from sys import exit
from data_base import DataBase
from category import Category
from product import Product
from read_excel import get_df_from_excel


async def df_to_db(table, path, sheet):
    data = await get_df_from_excel(path, sheet)
    for index, row in data.iterrows():
        await table.insert_table(row)


async def main():
    bd = DataBase()
    category = Category('category')
    product = Product('product', 'category')

    try:
        await bd.drop_schema()
        await bd.create_schema()

        await category.drop_table()
        await product.drop_table()

        await category.create_table()
        await product.create_table()

        await df_to_db(category, "Исходник.xlsx", "Категории")
        await df_to_db(product, "Исходник.xlsx", "Товары")

    finally:
        bd.conn.close()


if __name__ == '__main__':
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        exit(0)

