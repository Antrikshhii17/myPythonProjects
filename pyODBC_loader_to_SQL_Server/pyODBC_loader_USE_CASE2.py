import pyodbc
import pandas as pd


# Read the file into a variable
filename = r'C:\Users\antriksh.chourasia\PycharmProjects\pyODBC_loader\View IT Bid Floors.csv'


# Read the file into a pandas dataframe | Some special characters were causing problem, so I used 'unicode_escape'
df = pd.read_csv(filename,encoding='unicode_escape')


# Define column headers
df1 = pd.DataFrame(df,columns=['Receipt_Location','Delivery_Location','Cycle','Start_Gas_Day','End_Gas_Day','Daily_Equivalent_FT','Load_Factor','Bid_Floor'])


# Verify the content of the dataframe
df


# Create a pyodbc connection
# If using SQL Server authentication, replace the argument 'trusted_connection' with 'UID' and 'PWD'
conn = pyodbc.connect(
    """Driver={SQL Server Native Client 11.0};
    Server=BLR-ANTRIX;
    Database=NORTHWND;
    trusted_connection=yes;"""
)


# USE CASE(2): Using 'cursor.execute' for small files
# Lets initiate the cursor
cursor = conn.cursor()


# SQL Insert statement
sql = """INSERT INTO Stage1(
Receipt_Location,Delivery_Location,Cycle,Start_Gas_Day,End_Gas_Day,Daily_Equivalent_FT,Load_Factor,Bid_Floor)
VALUES(?,?,?,?,?,?,?,?)"""


# Writing data to database with try-catch block
# Please note that we can explicitly supply the rows as arguments here which cannot \
# be done by 'cursor.executemany()' since it accepts exactly two arguments.
try:
    for row in df1.itertuples():    
        cursor.execute(sql,row.Receipt_Location,
                           row.Delivery_Location,
                           row.Cycle,
                           row.Start_Gas_Day,
                           row.End_Gas_Day,
                           row.Daily_Equivalent_FT,
                           row.Load_Factor,
                           row.Bid_Floor)
    conn.commit()
    print('****************Data successfully loaded to the database!***************')
except:
    conn.rollback()
    print('Error! please check your code.')
conn.close()
