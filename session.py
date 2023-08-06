from session14 import Customer
from session14b import DBhelper
def main():

    db = DBhelper()
    print("Welcome to VetsApp")
    meassage = """
      1: Add customer
      0: Quit
      """
    print(meassage)
    choice = int(input("Enter Your Choices:"))

    customer= Customer()
    while True:
      if choice == 1:


             customer = Customer()
             customer.read_customer_data()
             print(vars(customer))
             sql = customer.get_insert_sql_query()
             db.excute_sql(sql)

      elif choice == 2:
               pass
      phone=input("enter the phone number")
      sql=customer.get_customer_sql_query()
      rows=db.excute_select_sql(sql)
      customer_fetched=row[0]
      customer.cid=customer_fetched[0]

      customer.name=input("enter the name")
      if len(customer.name) ==0:
          customer.name= customer_fetched[1]

      elif choice == 3:
               pass

      elif choice == 4:
              pass
              sql=customer.get_customer_sql_query()
              rows=db.excute_select_sql(sql)
              for row in rows:
                  print(row)

      elif choice==5:
                  phone=input("enter customer phone:")
                  sql= customer.get_customer_sql_query(phone)
                  row=db.excute_selct_sql(sql)
                  for row in rows:
                      print(row)



      elif choice==0:
                  print("Thank you for using VetsApp")
                  break

      else:
                print("Invalid choice...")
                print(meassage)
                choice = int(input("Enter your choice:"))

      choice=int(input("Enter your choice:"))

if __name__=="__main__":
    main()
