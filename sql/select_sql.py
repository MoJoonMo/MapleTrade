def search_item_list(use_yn):
    return "select * from search_item_list where ifnull(use_yn,'Y') = '" + use_yn + "'"
    
def search_nextval(table_name):
    print("SELECT nextval2('"+ table_name+"')")
    return "SELECT nextval2('"+ table_name+"')"