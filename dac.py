KEY_TO_VERBOSE_MAPPING = {'r': 'Read', 'w': 'Write', 'wg': 'Write grant', 'rg': 'Read grant', 'no': 'no access', }
VERBOSE_TO_KEY_MAPPING = {'read': 'r', 'write': 'w', 'write grant': 'wg', 'read grant': 'rg', 'no access': 'no', }


def load_user_access_matrix(tsv_fname='access_matrix.tsv'):
    with open(tsv_fname, "r", encoding="utf-8") as tsv_file:
        user_access_matrix = {}
        for line in tsv_file:
            attrs = line.split()
            user_id = attrs[0]
            user_rights = {}
            for file_id in range(1, len(attrs)):
                rights_list = attrs[file_id].split(',')
                user_rights[str(file_id)] = rights_list
            user_access_matrix[user_id] = user_rights
        return user_access_matrix


def save_user_access_matrix(matrix, tsv_fname='access_matrix.tsv'):
    with open(tsv_fname, "w", encoding="utf-8") as tsv_file:
        for user_id, user_rights in matrix.keys():
            tsv_file.write(f"{user_id}")
            for file_rights in user_rights.values():
                s = ",".join(file_rights)
                tsv_file.write(f"\t{s}")
            tsv_file.write("\n")


def main():
    user_access_rights_matrix = load_user_access_matrix("access_matrix.tsv")
    user_id = input("Type username\n")
    if user_access_rights_matrix.get(user_id) is None:
        print('Invalid username')
    else:
        user_rights_map = user_access_rights_matrix[user_id]
        command = None
        while command != 'quit':
            command = input('Command\n')
            if command == 'write':
                obj = input('Object id\n')
                access_keys = user_rights_map[obj]
                if 'w' in access_keys or 'wg' in access_keys:
                    print('Succesful write.')
                else:
                    print('Access error')
            if command == 'relogin':
                user_id = input("Type username\n")
                if user_access_rights_matrix.get(user_id) is None:
                    print('Invalid username')
                else:
                    user_rights_map = user_access_rights_matrix[user_id]
            elif command == 'read':
                obj = input('Object id\n')
                access_keys = user_rights_map[obj]
                if 'r' in access_keys or 'rg' in access_keys:
                    print('Succesful read.')
                else:
                    print('Access error')
            elif command == 'grant':
                obj = input('Object id\n')
                command = input('Command\n')
                access_keys = user_rights_map[obj]
                if command == 'write':
                    if 'wg' in access_keys:
                        user_id = input('Username\n')
                        user_access_rights_matrix[user_id][obj].append("w")
                        print(f'Succesfully granted write to {user_id} on file {obj}!')
                    else:
                        print('Access error')
                elif command == 'read':
                    if 'rg' in access_keys:
                        user_id = input('Username\n')
                        user_access_rights_matrix[user_id][obj].append("r")
                        print(f'Succesfully granted read to {user_id} on file {obj}!')
                    else:
                        print('Access error')
                else:
                    print('Invalid command.')
    save_user_access_matrix(matrix=user_access_rights_matrix)


if __name__ == '__main__':
    main()
