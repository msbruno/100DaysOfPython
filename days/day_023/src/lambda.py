#lambda expressions

def filter_even(arr:list):
   for element in arr:
      if element % 2 == 0:
         yield element

def filter_even_with_list_comprehension(arr:list):
   return [ element for element in arr if element % 2 == 0]


filter_even_lambda = lambda arr: [element for element in arr if element % 2 == 0]

test_data = [1,2,3,4,5,6]
expect_result = [2,4,6]
unexpected_result_text = lambda result: "result was:{}".format(result)

result = list(filter_even(test_data))
assert expect_result == result, unexpected_result_text(result)

result = filter_even_with_list_comprehension(test_data)
assert expect_result == result, unexpected_result_text(result)

result = filter_even_lambda(test_data)
assert expect_result == result, unexpected_result_text(result)
