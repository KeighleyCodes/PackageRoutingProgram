# Name: Keighley Manke
# Student ID: 001321515
# Class: WGU C950

import datetime

from Loading import total_distance_both, truck1_total_distance, truck2_total_distance, package_hash_table, \
    running_time_truck1, running_time_truck2, print_package_info


# Provides a user interface where options are presented to print truck mileage by individual truck, for both trucks, p
# package status for individual packages and all packages at a certain user-chosen time, and to print the final delivery
# times of each individual truck.
def ui():
    print('                                                               ')
    print('      ########  #####  #######   ##########   #######   ######')
    print('        ###    #####    ####   #############   ####       ###')
    print('        ###   ######   ####  #####      ####   ####       ###')
    print('        ###  ###  ##   ###   #####             ####       ###')
    print('        ###  ##   ##  ###    ####     ######   ####       ###')
    print('        ### ##    ## ###     ####       ####   ####       ###')
    print('        #####     #####       #############     ############')
    print('        ####      ####          #########         #######')
    print('                                                             ')
    print('    * ------  P A R C E L  ------  S E R V I C E  ----------* ')
    print('                                                                ')

    # Prompts user to choose between printing truck mileage, package status, delivery time, or close the program
    # The user's choice is used to continue to the next prompt
    while True:
        choice = input('Welcome to WGUPS. Please choose an option:\n'
                       '1) Print truck mileage\n'
                       '2) Print package status\n'
                       '3) Print truck delivery time\n'
                       '4) Quit\n')

        # If user chooses to print truck mileage another list of choices is presented to print the total truck mileage,
        # truck mileage for each individual truck or to quit the program
        # The user's choice is used to continue to the next prompt
        if choice == '1':
            choice = input('Please choose an option:\n'
                           '1) Print total truck mileage\n'
                           '2) Print Truck 1 total mileage\n'
                           '3) Print Truck 2 total mileage\n'
                           '4) Quit\n')

            # If the user chooses to print total mileage of both trucks it is printed
            if choice == '1':
                print("Total distances both trucks:", total_distance_both)

            # If the user chooses to print milage for Truck 1 it is printed
            if choice == '2':
                print("Truck 1 total distance:", truck1_total_distance)

            # If the user chooses to print milage for Truck 2 it is printed
            if choice == '3':
                print("Truck 2 total distance:", truck2_total_distance)

            # If the user chooses to exit the program a message is printed and the program exits
            elif choice == '4':
                print('Exiting program...')
                break

        # If the user chooses to print package status another prompt is presented to choose to print all package status,
        # package status by individual package, or quit the program
        # The user's choice is used to continue to the next prompt
        elif choice == '2':
            choice = input('Please choose an option:\n'
                           '1) Print package status by package ID\n'
                           '2) Print all package status\n'
                           '3) Quit\n')

            if choice == '1':
                selected_package_id = int(input('Enter package ID between 1 and 40: '))

                if selected_package_id not in range(1, 40):  # -------- FIX ME, range not working
                    print('Invalid package ID entered. Try again.')
                    break

                else:
                    hour_value = int(input("Please enter an hour value that's between 0 and 23:\n "))

                    if hour_value not in range(0, 23):
                        print('Invalid hour value entered. Try again.')
                        break

                    else:
                        minute_value = int(input("Please enter a minute value that's between 0 and 59:\n "))
                        if minute_value not in range(0, 59):
                            print('Invalid minute value. Try again.')
                            break

                        else:
                            specified_time = datetime.timedelta(hours=hour_value, minutes=minute_value)
                            print_package_info(selected_package_id, specified_time)

            if choice == '2':
                user_id = input('Input time: ')
                # ADD LOGIC TO SEARCH FOR TIME

            elif choice == '3':
                print('Exiting program...')
                break

        # If the user chooses to print truck delivery times another prompt is presented
        # The user's choice is used to continue to the next prompt
        if choice == '3':
            choice = input('Please choose an option:\n'
                           '1) Print Truck 1 last delivery time\n'
                           '2) Print Truck 2 last delivery time\n'
                           '3) Quit\n')

            # If the user chooses to print Truck 1 final running time it is printed
            if choice == '1':
                print("Truck 1 final running time:", running_time_truck1)

            # If the user chooses to print Truck 2 final running time it is printed
            if choice == '2':
                print("Truck 2 final running time:", running_time_truck2)

            # If the user chooses to exit the program a message is printed and the program exits
            elif choice == '3':
                print('Exiting program...')
                break

        # If the user chooses to exit the program a message is printed and the program exits
        elif choice == '4':
            print('Exiting program...')
            break


# Call the ui function to start the program
ui()
