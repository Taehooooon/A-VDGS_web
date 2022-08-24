import pyodbc


# 서버 주소(DB 접속ip)
server = "localhost"

# 접속 유저
user = "2VDGSIF"

# 패스워드
password = "2VI"

# 데이터베이스명
db = "VDGS"

cnxn = pyodbc.connect( "DRIVER={SQL Server};SERVER=" + server + ";uid=" + user + ";pwd=" + password + ";DATABASE=" + db)
cursor = cnxn.cursor()


# cnxn =  pymssql.connect(server , user, password, db)
# cursor = cnxn.cursor()

res =  cursor.execute('select top 5 * from [dbo].[EAI_DISPINFOAFL_RCV]')

row = cursor.fetchone()

while row:
    print(row[0], row[1], row[2])
    row = cursor.fetchone()

cnxn.close()