from ctypes import *

dll_name = "./cmasterrace.so"
input_message = "Hello world!"
result = 1
result_pointer = c_void_p(result)

# print(result_pointer)

libc = CDLL(dll_name)
libs.base64_encode.restype = c_wchar_p
encoded_message = libc.base64_encode(
    c_wchar_p(input_message),
    c_int(len(input_message)),
    result_pointer)
libc.base64_cleanup()

print(result_pointer.value)
