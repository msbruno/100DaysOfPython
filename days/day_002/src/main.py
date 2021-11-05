def upper_case(msg:str)->str:
    return msg.upper()

def lower_case(msg:str)->str:
    return msg.lower()

def order_str(msg:str, treatment_func:function):
    treated_msg = treatment_func(msg) 
    sorted_msg = sorted(treated_msg)
    return "".join(sorted_msg)
    

assert order_str("BCA", upper_case) == "ABC"





