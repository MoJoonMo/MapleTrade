def insert_sql(table_name, column_name, value):
    ret = "INSERT INTO " + table_name 
    for index, fl in enumerate(column_name):
        if index == 0:
            ret = ret + "(`" + fl
        else:
            ret = ret + "`,`" + fl
    ret = ret + "`) VALUES "

    for index, fl in enumerate(value):
        if index == 0:
            ret = ret + "('" + fl
        else:
            ret = ret + "','" + fl
    ret = ret + "')"
    return ret

