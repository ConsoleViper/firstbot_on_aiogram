import psycopg
from create_bot import bot


async def sql_start():
    async with await psycopg.AsyncConnection.connect("dbname=blue_dog_helper user=postgres password=People211") as d_base:

        async with d_base.cursor() as cur:

            await cur.execute("""
                CREATE TABLE IF NOT EXISTS employees(
                    img text,
                    first_name text,
                    last_name text,
                    age smallint,
                    phone_number text,
                    emploee_email text,
                    specialization text,
                    department text,
                    job_title text
                    )
                """)
            await d_base.commit()

async def add_employee_in_table(state):
    
    async with await psycopg.AsyncConnection.connect("dbname=blue_dog_helper user=postgres password=People211") as d_base:

        async with d_base.cursor() as cur:

            async with state.proxy() as data:
                
                await cur.execute(
                    "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    tuple(data.values()))
                
                await d_base.commit()

async def sql_read(message):
    async with await psycopg.AsyncConnection.connect("dbname=blue_dog_helper user=postgres password=People211") as d_base:
        async with d_base.cursor() as cur:
            await cur.execute('SELECT * FROM employees')
            #await cur.fetchall() смысла его испльзовать не было, так как fetchall возвращает список значений
            async for employees in cur:
                await bot.send_photo(message.from_user.id, employees[0], f"Name: {employees[1]}\nLast name: {employees[2]}\nAge: {employees[3]}\nPhone: {employees[4]}\nEmail: {employees[5]}\nSpecializations: {employees[6]}\nDepartment: {employees[7]}\nJob title: {employees[8]}")
                