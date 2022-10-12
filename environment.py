from generate_token import Generate_token

token_object = Generate_token()
token = token_object.authorization()
token_object.close()
