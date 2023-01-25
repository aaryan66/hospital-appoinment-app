import random #adding libraries for later on
print("Welcome to the VSS hospital please choose any one department")
print("""
1.)OPD
2.)Pediatrics
3.)Gynaecology
4.)Radiology
5.)ENT
6.)Dental
7.)Cardiology""")
user_input = input("")
print(f'>{user_input}')
if user_input == "OPD":
    print("Welcome to OPD department of the VSS hospital please tell of when do you want an appoinment:")
    print("""
    Today
    Tomorrow
    This Weekend
    Later on 
    """)
    opd_time = input("")
    if opd_time == "Today" or "today":
        print("Checking for the appoinments of today")
        print("Here are the doctors of OPD departments avalable today")
        doctors_opd_list= ["Dr Dina Sharma", "Dr Bisharath Thapaliya", "Dr Rajiv Pandey","Dr Sandip Raj Pandey","Dr Manish Koirala","Dr Sabal Bohora","Dr Bikash Bhattrai", "Uma Shakya"]
        doctors_opd_print = random.sample(doctors_opd_list, 5)
        print(doctors_opd_print)
        print("Now since you have got the doctors please choose any one doctor for the appoinment")
        doctor_opd_choose = input()
        opd_time = ["5:00 PM", "4 PM","6PM","7PM"]
        opd_time_print= random.choice(opd_time)
        print(f"You have got an appoinment of {doctor_opd_choose} at {opd_time_print}")