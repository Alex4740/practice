from multiprocessing import connection

from Entities.customer import Customer


class CustomerDAOInterface:
    pass


class CustomerDAOImp(CustomerDAOInterface):
    def insert_into_customer_table(self, customer_obj: Customer) -> Customer:
        # get
          # create curser
          # use curser to execute sql transaction
          # remember to commit transaction
          # get the returned generated id
          # assign it to my customer obj
          # return customer obj
    sql = "insert into customers values(default, %s, %s) returning customer_id"
    curser = connection.cu

    def delete_from_customer_table_by_id(self, customer_id: Customer) -> bool:
        pass
