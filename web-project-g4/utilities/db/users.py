import db_manager

db_man = db_manager.DBManager()

user=db_man.fetch('SELECT * FROM customers')

print(user)


def get_user(user_name):
    query = "select * from customers where user_name='%s';" % user_name
    users_list = db_man.fetch(query)
    bool_ans=True
    if users_list==[]:
        bool_ans=False
    print(users_list)
    print(bool_ans)
    return (users_list, bool_ans)

get_user('Eden')

