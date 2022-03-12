from Entities.customer import Customer
from customer_class.customer_dao_imp import CustomerDAOImp

customer_dao = CustomerDAOImp():



def test_create_customer_record_success():
    test_customer = Customer(0, "Alex", "asha")
    returned_customer = customer_dao
def test_delete_customer_record_success():
    pass
