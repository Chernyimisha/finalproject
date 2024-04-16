# import requests
# import json
#
#
# def fetch(url, params):
#     headers = params['headers']
#     body = params['body']
#     if params['method'] == 'GET':
#         return requests.get(url, headers=headers)
#     if params['method'] == 'POST':
#         return requests.post(url, headers=headers, data=body)
#     if params['method'] == 'PUT':
#         return requests.put(url, headers=headers, data=body)
#     if params['method'] == 'DELETE':
#         return requests.delete(url, headers=headers, data=body)
#     if params['method'] == 'PATCH':
#         return requests.patch(url, headers=headers, json=body)
#
#
# def create_params(*args, **kwargs):
#     api_key = kwargs['api_key']
#     method = kwargs['method']
#     body = kwargs['body']
#
#     result = {
#         "headers": {
#             "Authorization": api_key
#         },
#         "body": body,
#         "method": method
#     }
#     return result


# result = {
#         "headers": {
#             "Authorization": api_key
#         },
#         "body": {
#             "id": id_feedback,
#             "text": title
#         },
#         "method": "PATCH"
#     }