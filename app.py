from services.common import *
# from services.email import *

for i in range(1, count_column()):
    encrypted_data = get_data(i)
    # print('id: ', i, ', encrypt: ', encrypted_data)
    decrypted_data = decrypt_data(encrypted_data)
    # print('id: ', i, ', decrypt: ', decrypted_data)
    # check_email(decrypted_data)
    update_data(decrypted_data, i)