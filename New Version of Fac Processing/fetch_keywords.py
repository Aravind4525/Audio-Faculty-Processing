import psycopg2

def fetch_keywords(video_ids: list[str]):
    """Fetch critical keywords for the given video IDs.
    """
    if not video_ids:
        return []
    
    # Convert video IDs into a comma-separated string with quotes
    video_id_str = ', '.join(f"'{vid}'" for vid in video_ids)

    query = f"""
        SELECT critical_keywords 
        FROM public.cs_ee_5m_test 
        WHERE video_id IN ({video_id_str}) order by _offset;
    """
    
    adhoc_db = psycopg2.connect(dbname="piruby_automation", user="postgres", host="164.52.194.25",
                                password="piruby@157", port="5432")
    adhoc_cursor = adhoc_db.cursor()
    
    adhoc_cursor.execute(query)
    result = adhoc_cursor.fetchall()

    # Flatten the list of tuples into a list of keywords
    keywords = [row[0] for row in result]

    # print("Critical keywords:", keywords)
    
    adhoc_cursor.close()
    adhoc_db.close()
    return keywords


def fetch_all_keywords(video_ids: list[str]):
    """
    Fetch all critical keywords for the given list of video IDs using IN (...) syntax.
    """
    if not video_ids:
        return []

    # Convert video IDs into a comma-separated string with quotes
    video_id_str = ', '.join(f"'{vid}'" for vid in video_ids)

    query = f"""
        SELECT critical_all_keywords 
        FROM public.cs_ee_5m_test 
        WHERE video_id IN ({video_id_str});
    """

    # Connect to the database
    adhoc_db = psycopg2.connect(
        dbname="piruby_automation",
        user="postgres",
        host="164.52.194.25",
        password="piruby@157",
        port="5432"
    )
    adhoc_cursor = adhoc_db.cursor()

    adhoc_cursor.execute(query)
    result = adhoc_cursor.fetchall()

    all_keywords = [row[0] for row in result if row[0]]

    adhoc_cursor.close()
    adhoc_db.close()

    return all_keywords

# Example usage
# keywords = fetch_all_keywords(['g1Zbuk1gAfk', '4b5d3muPQmA'])
# print("All keywords:", keywords)
