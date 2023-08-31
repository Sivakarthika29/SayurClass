######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number upto 12 rows.

for table in range(7,17):
    print(f"Table {table}")
    for count in range(1,13):
        print(f"{table} * {count} = {table*count}")
    print()