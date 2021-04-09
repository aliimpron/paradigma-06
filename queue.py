def bank_queue():
    queue = []
    
    while true:
        if a_new_customer_arrived:
            new_customer = get_customer()
            queue.append(new_customer)
            customer_to_be_served = queue.pop(0)
            serve_customer (customer_to_be_served)
         