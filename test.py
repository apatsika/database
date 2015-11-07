import MySQLdb
from json import load


def main():
    config = load(open("config.json"))
    db_user = config["user"]
    pw = config["pw"]

    # Setup MySQL connection
    conn = MySQLdb.connect(host='health-db-internet.c6clocfz5zxy.us-east-1.rds.amazonaws.com',
                           port=3306,
                           user=db_user,
                           passwd=pw)
    cur = conn.cursor()

    # Execute query
    query = 'SELECT * FROM CMS_open_payments_2013.general_payment_data WHERE Recipient_State="WY"'
    print 'Running query:  {0};\n'.format(query)
    cur.execute(query)

    wyoming_data = cur.fetchall()
    print 'Columns:  {0}\n'.format([c[0] for c in cur.description])
    print 'Number of records: {0}'.format(len(wyoming_data))

    # Close MySQL connections
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
