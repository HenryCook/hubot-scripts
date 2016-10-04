def delete(args, conn):
    # To delete an index specified
    index_to_remove = args.delete_index

    try:
        conn.indices.delete(index=index_to_remove)
        print("'" + index_to_remove + "'" + " has been removed")
    except:
        print("Unable to delete the " + "'" + index_to_remove + "'" + " index")


def list_all(conn):
    try:
        for index in conn.indices.get('*'):
            print(index)
    except:
        print("Unable to list al indices")
