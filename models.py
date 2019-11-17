import peewee
db = peewee.MySQLDatabase('superset', user='root', passwd='snerknow12')
#db = connect('mysql://root:snerknow12@localhost:3306/superset')


class BaseModel(peewee.Model):
    """Classe model base"""

    class Meta:
        # Indica em qual banco de dados a tabela
        # 'author' sera criada (obrigatorio). Neste caso,
        # utilizamos o banco 'codigo_avulso.db' criado anteriormente
        database = db


class Users(BaseModel):

    """
    Classe que representa a tabela Users
    """

    user_id = peewee.BigAutoField()
    name = peewee.CharField()


if __name__ == '__main__':

 
    #for user in Users.select():
    #    print('ID: ' + str(user.user_id) + ' Name: ' + user.name)


    #users = Users.get_by_id(1)
    users = Users.get(Users.user_id == 2)


    print(users.name)