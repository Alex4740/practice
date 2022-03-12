from Entities.customer import Customer
from customer_class.customer_dao_imp import CustomerDAOImp

customer_dao = CustomerDAOImp()


def test_create_customer_record_success():
    test_customer = Customer(0, "Brain", "Kun")
    return_customer = customer_dao.insert_into_customer_table(test_customer)
    assert return_customer.customer_id != test_customer.customer_id

    # pass a customer object in to create method
    # check return customer object has new id


def test_delete_customer_record_success():
    result = customer_dao.delete_from_customer_table_by_id(-1)
    assert result


    # I need the id of customer to delete
    # pass that id in to delete method
    # check if t get true boolean back.