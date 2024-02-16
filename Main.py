# Name: Keighley Manke
# Student ID: 001321515
# Class: WGU C950

import datetime

from Loading import total_distance_both, truck1_total_distance, truck2_total_distance, package_hash_table, \
    running_time_truck1, running_time_truck2, package_info


# Provides a user interface where options are presented to print truck mileage by individual truck, for both trucks, p
# package status for individual packages and all packages at a certain user-chosen time, and to print the final delivery
# times of each individual truck.
def ui():
    print('\n')
    print('      ########  #####  #######   ##########   #######   ######')
    print('        ###    #####    ####   #############   ####       ###')
    print('        ###   ######   ####  #####      ####   ####       ###')
    print('        ###  ###  ##   ###   #####             ####       ###')
    print('        ###  ##   ##  ###    ####     ######   ####       ###')
    print('        ### ##    ## ###     ####       ####   ####       ###')
    print('        #####     #####       #############     ############')
    print('        ####      ####          #########         #######\n')
    print('    * ------  P A R C E L  ------  S E R V I C E  ----------* \n')

    # Prompts user to choose between printing truck mileage, package status, delivery time, or close the program
    # The user's choice is used to continue to the next prompt
    while True:
        choice = input('Welcome to WGUPS. Please choose an option:\n'
                       '1) Print all package info\n'
                       '2) Print truck mileage\n'
                       '3) Print package status\n'
                       '4) Print truck delivery time\n'
                       '5) Quit\n')

        if choice == '1':
            print(package_hash_table)

        # If user chooses to print truck mileage another list of choices is presented to print the total truck mileage,
        # truck mileage for each individual truck or to quit the program
        # The user's choice is used to continue to the next prompt
        if choice == '2':
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
        elif choice == '3':
            choice = input('Please choose an option:\n'
                           '1) Print package status by package ID\n'
                           '2) Print all package status\n'
                           '3) Quit\n')

            if choice == '1':
                selected_package_id = int(input('Enter package ID between 1 and 40: \n'))

                if selected_package_id not in range(1, 41):
                    print('Invalid package ID entered. Try again.')
                    break

                else:

                    # Assuming specified_date is the same date as the truck loading times
                    specified_date = datetime.datetime(2024, 1, 31).date()

                    hour_value = int(input("Please enter an hour value that's between 0 and 23:\n "))

                    if not 0 <= hour_value <= 23:
                        print('Invalid hour value entered. Try again.')
                        break

                    else:
                        minute_value = int(input("Please enter a minute value that's between 0 and 59:\n "))
                        if not 0 <= minute_value <= 59:
                            print('Invalid minute value. Try again.')
                            break

                        else:
                            # Create specified_time as a datetime object
                            specified_time = datetime.datetime(2024, 1, 31, hour_value, minute_value)

                            # Print package info at specified time
                            print(package_info(selected_package_id, specified_time, specified_date))

            if choice == '2':
                print("Put something here")
                # ADD LOGIC TO PRINT ALL PACKAGES COMPARED TO TIME

            # If the user chooses to exit the program a message is printed and the program exits
            elif choice == '3':
                print('Exiting program...')
                break

        # If the user chooses to print truck delivery times another prompt is presented
        # The user's choice is used to continue to the next prompt
        if choice == '4':
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
        elif choice == '5':
            print('Exiting program...')
            break


# Call the ui function to start the program
ui()
