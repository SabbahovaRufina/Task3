import pandas
import asyncio


async def get_df_from_excel(path, sheet):
    return pandas.read_excel(path, sheet_name=sheet)


async def print_df_from_excel(path, sheet):
    print(await get_df_from_excel(path, sheet))


async def main():
    # df = await get_df_from_excel("Исходник.xlsx", "Категории")
    df = await get_df_from_excel("Исходник.xlsx", "Товары")
    # await print_df_from_excel("Исходник.xlsx", "Товары")
    for index, row in df.iterrows():
        print(row)


if __name__ == '__main__':
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        exit(0)

