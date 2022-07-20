import db_manager

db_man = db_manager.DBManager()

user=db_man.fetch('SELECT * FROM customers')

print(user)


def get_user(user_name):
    query = "select * from customers where user_name='%s';" % user_name
    users_list = db_man.fetch(query)
    bool_ans=True
    if users_list==[]:
        bool_ans = False
    # print(users_list)
    # print(bool_ans)
    return (users_list, bool_ans)

#get_user('Eden')

def create_user(name,user_nickname,user_password,user_email):
    bool_ans=True
    if get_user(name)[1] == True:
       #print('user exist')
        bool_ans = False
    else:
        query = "Insert into customers (user_name,nickname,password,email) VALUES ( '%s', '%s', '%s', '%s')" % (name, user_nickname, user_password, user_email)
        db_man.commit(query)
    return(bool_ans)


#create_user('Gil','gili2202','Don12345','don@gmail.com')