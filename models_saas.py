import peewee


#db = connect('mysql://readonly_dev:QZy&h*YOc2%n6J||fLaN@external-read.cu98qr8jhy71.sa-east-1.rds.amazonaws.com/production')

db = peewee.MySQLDatabase("production",
                        host="external-read.cu98qr8jhy71.sa-east-1.rds.amazonaws.com",
                        port=3306,
                        user="readonly_dev",
                        passwd="QZy&h*YOc2%n6J||fLaN")


class BaseModel(peewee.Model):
    """Classe model base"""

    class Meta:
        # Indica em qual banco de dados a tabela
        # 'author' sera criada (obrigatorio). Neste caso,
        # utilizamos o banco 'codigo_avulso.db' criado anteriormente
        database = db

class Subscriptions_subscription(BaseModel):

    """
    Classe que representa a tabela Users
    """

    id = peewee.AutoField()
    subscription_date = peewee.DateField()
    exempt = peewee.SmallIntegerField()
    email = peewee.CharField()
    _deleted_at = peewee.DateTimeField()
    date_added = peewee.DateTimeField()
    is_subscriber = peewee.SmallIntegerField()
    canceled = peewee.SmallIntegerField
    charge_kind = peewee.CharField()


db.connect()

subscriptions = Subscriptions_subscription()


for row in subscriptions.select(Subscriptions_subscription.id,Subscriptions_subscription.charge_kind):
    print(row.id,row.charge_kind)

db.close()


