print("--- Type Conversion Demonstration ---")

int_num = 10
float_num = 5.5
result = int_num + float_num  # int_num is promoted to float
print(f"Implicit Conversion: {int_num} (int) + {float_num} (float) = {result} ({type(result).__name__})")

str_val = "123"
converted_int = int(str_val)
converted_float = float(str_val)

print(f"\nString '{str_val}' converted to int: {converted_int} ({type(converted_int).__name__})")
print(f"String '{str_val}' converted to float: {converted_float} ({type(converted_float).__name__})")

num_val = 456
converted_str = str(num_val)
print(f"Number {num_val} converted to string: '{converted_str}' ({type(converted_str).__name__})")
