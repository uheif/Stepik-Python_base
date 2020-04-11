def code_dict(keys: list, values: list):
    return {key: value for key, value in zip(keys, values)}


def encode(string: str, code: dict):
    return ''.join([code[char] for char in string])


def decode(string: str, code: dict):
    inv_code = {value: key for key, value in code.items()}
    return ''.join([inv_code[char] for char in string])


my_code_dict = code_dict(list(input("буквы: ")), list(input("шифр: ")))
print(my_code_dict)
print(encode(input("строка: "), my_code_dict))
print(decode(input("шифр: "), my_code_dict))
