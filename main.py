import random  # adding libraries for later on
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
    # OPD doctor appoinment time
    opd_time_clock = ["5:00 PM", "4 PM", "6PM", "7PM"]
    doctors_opd_today_list = ["Dr Dina Sharma", "Dr Bisharath Thapaliya", "Dr Rajiv Pandey",
                              "Dr Sandip Raj Pandey", "Dr Manish Koirala", "Dr Sabal Bohora", "Dr Bikash Bhattrai", "Uma Shakya"]

    doctors_opd_tomorrow_list = [random.sample(doctors_opd_today_list, 2), "Dr Rajesh Singh Thakuri",
                                 "Dr Ram Thapa" "Dr Laju Basnet", "Dr Rahul Sharma", "Dr Sumit Chaulagain"]
    doctors_opd_this_weekend_list = [random.sample(doctors_opd_today_list, 2), random.sample(
        doctors_opd_tomorrow_list, 2), "Dr Aman Shrestha", "Dr Asif Sheikh", "Dr Alice Doe"]

    # OPD today
    if opd_time == "Today" or "today":
        print("Checking for the appoinments of today")
        print("Here are the doctors of OPD departments avalable today")

        doctors_opd_today_print = random.sample(doctors_opd_today_list, 5)
        print(doctors_opd_today_print)
        print("Now since you have got the doctors please choose any one doctor for the appoinment")
        doctor_opd_today_choose = input("")
        opd_time_print = random.choice(opd_time_clock)
        print(
            f"You have got an appoinment of {doctor_opd_today_choose} at {opd_time_print} Department: OPD")

    # OPD Tomorrow
    elif opd_time == "Tomorrow" or "tomorrow":
        print("Checking for the appoinment for tomorrow")
        print("Here are the doctors of OPD department who will be available tomorrow")

        doctors_opd_tomorrow_print = random.sample(
            doctors_opd_tomorrow_list, 5)
        print(doctors_opd_tomorrow_print)
        print("Now since you have got the doctors please choose a doctor and we will let you know the appoinment time")
        doctors_opd_tomorrow_choose = input("")
        opd_time_print = random.choice = (opd_time_clock)
        print(
            f"You have got an appoinment of {doctors_opd_tomorrow_choose} at {opd_time_print} Department : OPD")

    # OPD this weekend
    elif opd_time == "This weekend" or "this weekend":
        print("Checking for the appoinment for this weekend")
        print("Here are the doctors of OPD department who will be available this weekend")
        doctors_opd_this_weekend_print = random.sample(
            doctors_opd_this_weekend_list, 5)
        print(doctors_opd_this_weekend_print)
        print("Now since you have got the doctors please choose a doctor and we will let you know the appoinment time")
        doctors_opd_this_weekend_choose = input("")
        opd_time_print = random.choice(opd_time_clock)
        print(
            f"You have got an appoinment of {doctors_opd_this_weekend_choose} at {opd_time_print} Department : OPD")
    # If user chooses later on then lets ask a date
    elif opd_time == "Later on":
        print("Please give a specific date")
        date_input = input("")
        print("Doctors for the specific date are : ")
        doctor_opd_later_on_list = [random.sample(doctors_opd_today_list, 2), random.sample(
            doctors_opd_tomorrow_list, 3), random.sample(doctors_opd_this_weekend_list, 1),  "Dr Ashesh Basnet"]
        doctor_opd_later_on_print = random.sample(doctor_opd_later_on_list, 3)
        print(doctor_opd_later_on_print)
        print(
            "Choose a doctor for {date_input} appoinment and we will let you time")
        doctor_opd_later_on_choose = input("")
        opd_time_print = random.choice(opd_time_clock)

if user_input == "pediatrics":
    print("Welcome to pediatrics department of the VSS hospital please tell of when do you want an appoinment:")
    print("""
    Today
    Tomorrow
    This Weekend
    Later on 
    """)
    pediatrics_time = input("")
    # pediatrics doctor appoinment time
    pediatrics_time_clock = ["5:00 PM", "4 PM", "6PM", "7PM"]
    doctors_pediatrics_today_list = ["Dr Dina Sharma", "Dr Bisharath Thapaliya", "Dr Rajiv Pandey",
                              "Dr Sandip Raj Pandey", "Dr Manish Koirala", "Dr Sabal Bohora", "Dr Bikash Bhattrai", "Uma Shakya"]

    doctors_pediatrics_tomorrow_list = [random.sample(doctors_pediatrics_today_list, 2), "Dr Rajesh Singh Thakuri",
                                 "Dr Ram Thapa" "Dr Laju Basnet", "Dr Rahul Sharma", "Dr Sumit Chaulagain"]
    doctors_pediatrics_this_weekend_list = [random.sample(doctors_pediatrics_today_list, 2), random.sample(
        doctors_pediatrics_tomorrow_list, 2), "Dr Aman Shrestha", "Dr Asif Sheikh", "Dr Alice Doe"]
