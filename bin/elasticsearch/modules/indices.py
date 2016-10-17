def delete(args, conn):
    # To delete an index specified
    index_to_remove = args.delete_index

    try:
        conn.indices.delete(index=index_to_remove)
        print("The index '{remove}' has been removed").format(remove=index_to_remove)
    except:
        print("Unable to delete the '{remove}' index").format(remove=index_to_remove)


def list_all(conn):
    try:
        for index in conn.indices.get('*'):
            print(index)
    except:
        print("Unable to list all indices")
