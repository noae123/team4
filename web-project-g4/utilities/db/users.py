from utilities.db import db_manager

db_man = db_manager.DBManager()
users=db_man.fetch('SELECT * FROM customers')
print(users)


def get_user_by_name(user_name):
    query = "select * from customers where user_name='%s';" % user_name
    user_list = db_man.fetch(query)
    bool_ans=True
    if user_list==[]:
        bool_ans = False
    return (user_list, bool_ans)


def get_user_by_id(id):
    query = "select * from customers where id='%s';" % id
    user_row = db_man.fetch(query)
    bool_ans = True
    if user_row == []:
        bool_ans = False
    # user_name=db_man.fetch("select user_name from customers where id='%s';"%id)
    # user_nickname=db_man.fetch("select nickname from customers where id='%s';"%id)
    # user_email=db_man.fetch("select email from customers where id='%s';"%id)
    # user_password=db_man.fetch("select password from customers where id='%s';"%id)
    user=db_man.fetch("select user_name, nickname, email, password  from customers where id='%s';"%id)[0]
    return (user[0],user[1],user[2], user[3], bool_ans)


def create_user(name,user_nickname,user_password,user_email):
    bool_ans=True
    if get_user_by_name(name)[1] == True:
        bool_ans = False
    else:
        query = "Insert into customers (user_name,nickname,password,email) VALUES ( '%s', '%s', '%s', '%s')" % (name, user_nickname, user_password, user_email)
        last_row_effected=db_man.commit(query)
    return(last_row_effected,bool_ans)


def update_user(id,user_name,user_nickname,user_email,user_password):
    if get_user_by_id(id)[4] == True:
        query = "UPDATE customers SET user_name = '%s', nickname= '%s',email= '%s',password='%s' WHERE id='%s';" % (user_name,user_nickname,user_email,user_password, id)
        db_man.commit(query)
        bool_ans=True
    else:
        bool_ans=False
    updated_user=db_man.fetch("select * from customers where id='%s';" % id)
    return(updated_user,bool_ans)



def delete_user(id):
    query="DELETE  FROM customers WHERE id='%s';" % id
    db_man.commit(query)
    check_if_user_exist="select * from customers where id='%s';"% id
    if check_if_user_exist == []:
        bool_ans= True
    else:
        bool_ans = False
    return(bool_ans)

def get_user_id_by_name_password(user_name,password):
    query=("SELECT id FROM customers WHERE user_name='%s'and password='%s';"%(user_name,password))
    user_id = db_man.fetch(query)[0]
    if user_id == False or user_id == []:
        print('dont found')
        bool_ans= False
    else:
        bool_ans=True
    return(user_id[0],bool_ans)

def get_user_id_by_name(user_name):
    query="SELECT id FROM customers WHERE user_name='%s';" %user_name
    user_id=db_man.fetch(query)
    if user_id == False or user_id==[]:
        bool_ans=False
    else:
        bool_ans=True
    return (user_id,bool_ans)


