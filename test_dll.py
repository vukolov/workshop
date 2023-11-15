from ctypes import *

dll_name = "./cmasterrace.so"
input_message = "Hello world!"
result = "f"
result_pointer = c_wchar_p(result)

#print(result_pointer)

libc = CDLL(dll_name)
encoded_message = libc.base64_encode(
    c_char_p(input_message),
    c_int(len(input_message)),
    result_pointer)
libc.base64_cleanup()

print(result_pointer.value)
