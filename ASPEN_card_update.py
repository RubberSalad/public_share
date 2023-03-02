# python 3 script for generating the ASPEN card update queries

# datetime object containing current date and time
from datetime import datetime
now = datetime.now()
# formatting date
t_string = now.strftime("%Y-%m-%d 00:00:00")

CHID = input("Please enter the Cardholder ID (the last 8 digits- exclude the 2000) \n")
NASS = input("Please enter the NASS ref \n")

#stripping accidentally entered whitespaces
CHID = CHID.strip()
NASS = NASS.strip()

#print("Use the below to update the payment instructions and card payments in the payments database")
print(f"\nUPDATE payment.nasspaymentinstruction SET cardreference = '{CHID}' WHERE nassreference = '{NASS}';")
print(f"UPDATE payment.paymentcards SET cardreference = '{CHID}' WHERE nassreference = '{NASS}';")

#print("\nIf the applicant never had a card, run the below also:")
print(f"INSERT INTO payment.paymentcards (nassreference,cardreference,datecreated,dateamended) VALUES ('{NASS}','{CHID}','{t_string}','{t_string}');")

#print("Once executed, the 'View Payments' page in Atlas should be updated with the correct ASPEN/MACP Card Reference. \nTo double check the database you can run the below select statements:")

print(f"SELECT * FROM payment.nasspaymentinstruction WHERE nassreference = '{NASS}';")
print(f"SELECT * FROM payment.paymentcards WHERE nassreference = '{NASS}';")

