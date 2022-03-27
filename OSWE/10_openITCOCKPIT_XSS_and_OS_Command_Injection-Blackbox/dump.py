import os
from db import create_connection, get_content, get_locations

database = r"sqlite.db" 
contentDir = os.getcwd() + "/content"

def write_to_file(url, content): 
    fileName = url.replace('https://','') 
    if not fileName.endswith(".html"): 
        fileName = fileName + ".html" 
        fullname = os.path.join(contentDir, fileName) 
        path, basename = os.path.split(fullname)
        
        if not os.path.exists(path): 
            os.makedirs(path) with open(fullname, 'w') as f:
                f.write(content) 

if __name__ == '__main__': 
    conn = create_connection(database)
    locations = get_locations(conn)
    for l in locations:
        content = get_content(conn, l)
        write_to_file(l[0], content)
