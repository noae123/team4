from db_manager import dbManager

def get_user(user_name):
    query = "select * from customers where user_name='%s';" % user_name
    users_list = dbManager.fetch(query)
    bool_ans=True
    if users_list==[]:
        bool_ans=False
    return (users_list, bool_ans)

