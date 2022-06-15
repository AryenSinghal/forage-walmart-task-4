def main():
    import sqlite3
    import csv

    # Connect to the database
    conn = sqlite3.connect('shipment_database.db')
    c = conn.cursor()

    # Create the table
    c.execute("""CREATE TABLE IF NOT EXISTS shipping_data (
        origin_warehouse TEXT,
        destination_store TEXT,
        product TEXT,
        on_time TEXT,
        product_quantity TEXT,
        driver_identifier TEXT)""")
    
    # Read the csv files
    with open('data/shipping_data_0.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            c.execute("INSERT INTO shipping_data VALUES (?,?,?,?,?,?)", row)
    
    with open('data/shipping_data_1.csv', 'r') as csvfile1:
        reader1 = csv.reader(csvfile1)
        shipment_identifier = ''
        count = 0
        for row1 in reader1:
            if shipment_identifier == row1[0]:
                count += 1
            else:
                if count > 1:
                    with open('data/shipping_data_2.csv', 'r') as csvfile2:
                        reader2 = csv.reader(csvfile2)
                        for row2 in reader2:
                            if row2[0] == shipment_identifier:
                                c.execute("INSERT INTO shipping_data VALUES (?,?,?,?,?,?)", (row2[1], row2[2], row1[1], row1[2], count, row2[3]))
                shipment_identifier = row1[0]
                count = 1
    
    conn.commit()
    conn.close()

main()