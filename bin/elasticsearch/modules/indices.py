def delete(args, conn):
    # To delete an index specified
    index_to_remove = args.delete_index

    conn.indices.delete(index=index_to_remove)
    print("'" + index_to_remove + "'" + " has been removed")


def list_all(conn):
    for index in conn.indices.get('*'):
        print(index)
