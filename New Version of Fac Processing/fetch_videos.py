import psycopg2
from psycopg2 import OperationalError


def get_sections_for_course(course_section_id: list, server_type: str) -> list[tuple[int, int]]:
    """
    Get (section_id, content_id) for a given course content ID and type=2.
    """
    if not course_section_id:
        return [], []
    
    # Convert list to comma-separated string for SQL IN clause
    ids_str = ','.join(map(str, course_section_id))

    query = f"""select id, content_id from "Lms_coursesections" where id IN ({ids_str})"""

    try:
        if server_type == 'dev':
            # Attempt to connect to the dev database
            with psycopg2.connect(dbname="piruby_db_v2", user="postgres", host="3.108.6.18",
                                  password="prjeev@275", port="5432") as prod_db:
                with prod_db.cursor() as prod_cursor:
                    prod_cursor.execute(query)
                    data = prod_cursor.fetchall()
        else:
            # Attempt to connect to the prod database
            with psycopg2.connect(dbname="piruby_db_v2", user="postgres", host="216.48.176.169",
                                  password="prjeev@275", port="6432") as prod_db:
                with prod_db.cursor() as prod_cursor:
                    prod_cursor.execute(query)
                    data = prod_cursor.fetchall()

        # Print the retrieved data
        # print("Data fetched from the database:", data)

        if data is None:
            return [], []

        return [item[0] for item in data], [item[1] for item in data]

    except OperationalError as e:
        print(f"Error: Unable to connect to the database. {e}")
        return [], []
    

def get_videos_for_section(content_ids: list[int], server_type: str) -> tuple:
    """
    Get video_ids from Lms_videomaster for a specific section ID.
    """
    if not content_ids:
        return []

    # Convert list to comma-separated string for SQL IN clause
    ids_str = ','.join(map(str, content_ids))
    query = f"""SELECT DISTINCT video_id FROM "Lms_videomaster" WHERE id IN ({ids_str})"""

    try:
        if server_type == 'dev':
            # Attempt to connect to the dev database
            with psycopg2.connect(dbname="piruby_db_v2", user="postgres", host="3.108.6.18",
                                  password="prjeev@275", port="5432") as prod_db:
                with prod_db.cursor() as prod_cursor:
                    prod_cursor.execute(query)
                    data = prod_cursor.fetchall()
        else:
            # Attempt to connect to the prod database
            with psycopg2.connect(dbname="piruby_db_v2", user="postgres", host="216.48.176.169",
                                  password="prjeev@275", port="6432") as prod_db:
                with prod_db.cursor() as prod_cursor:
                    prod_cursor.execute(query)
                    data = prod_cursor.fetchall()

        # Print the retrieved data
        # print("Data fetched from the database:", data)

        if data is None:
            return []

        return [item[0] for item in data]

    except OperationalError as e:
        print(f"Error: Unable to connect to the database. {e}")
        return []
    

def get_course_vids_secs(course_id: int, server_type: str, video_type: int) -> tuple:
    """
    Function to get video_ids and sections_ids belonging to a particular course
    """
    # query = """select distinct video_id, course_section_id from "Lms_videomaster" where course_section_id in
    # (select distinct id from "Lms_coursesections" where course_content_id = {}) and type = {}""".format(course_id,
    #                                                                                                     video_type)
    query = """select distinct video_id, course_section_id from "Lms_videomaster" where course_section_id in
    (select id from "Lms_coursesections" where course_content_id = {} order by sno) and type = {}""".format(course_id,
                                                                                                               video_type)

    try:
        if server_type == 'dev':
            # Attempt to connect to the dev database
            with psycopg2.connect(dbname="piruby_db_v2", user="postgres", host="3.108.6.18",
                                  password="prjeev@275", port="5432") as prod_db:
                with prod_db.cursor() as prod_cursor:
                    prod_cursor.execute(query)
                    data = prod_cursor.fetchall()
        else:
            # Attempt to connect to the prod database
            with psycopg2.connect(dbname="piruby_db_v2", user="postgres", host="216.48.176.169",
                                  password="prjeev@275", port="6432") as prod_db:
                with prod_db.cursor() as prod_cursor:
                    prod_cursor.execute(query)
                    data = prod_cursor.fetchall()

        # Print the retrieved data
        # print("Data fetched from the database:", data)

        if data is None:
            return [], []

        return [item[0] for item in data], [item[1] for item in data]

    except OperationalError as e:
        print(f"Error: Unable to connect to the database. {e}")
        return [], []
    
    
# result = get_course_vids_secs(212, 'dev', 2)  
# print(result)