import sqlite3
conn = sqlite3.connect(r'C:\Users\yosse\PycharmProjects\pythonProject1\hospital\hospital.db')
c = conn.cursor()
f = open('patient.txt', 'r')
lines = f.readlines()
c.execute("delete from Patients")
for line in lines:
    line=line.split(',')
    print(line)

    sql = f"""
    insert into Patients(name, age, gender, address, phone_number) values ('{line[0]}','{line[1]}','{line[2]}','{line[3]}','{line[4].strip()}')
    """
    print(sql)

    c.execute(sql)
    conn.commit()
c.close()
conn.close()