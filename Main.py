# Name: Keighley Manke
# Student ID: 001321515
# Class: WGU C950
from Loading import total_distance_both, truck1_total_distance, truck2_total_distance, package_hash_table


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

    while True:
        choice = input('Welcome to WGUPS. Please choose an option:\n'
                       '1) Print truck mileage\n'
                       '2) Print package status\n'
                       '3) Quit\n')

        if choice == '1':
            choice = input('Please choose an option:\n'
                           '1) Print total truck mileage\n'
                           '2) Print Truck 1 total mileage\n'
                           '3) Print Truck 2 total mileage\n'
                           '4) Quit\n')

            if choice == '1':
                print("Total distances both trucks:", total_distance_both)

            if choice == '2':
                print("Truck 1 total distance:", truck1_total_distance)

            if choice == '3':
                print("Truck 2 total distance:", truck2_total_distance)

            elif choice == '3':
                print('Exiting program...')
                break

        elif choice == '2':
            choice = input('Please choose an option:\n'
                           '1) Print package status by package ID\n'
                           '2) Print all package status\n'
                           '3) Quit\n')

            if choice == '1':
                user_id = input('Enter package ID: ')
                # ADD LOGIC FOR SEARCHING FOR PACKAGE ID

            if choice == '2':
                user_id = input('Enter package ID: ')
                # ADD LOGIC TO SEARCH FOR PACKAGE ID

            elif choice == '3':
                print('Exiting program...')
                break

        elif choice == '3':
            print('Exiting program...')
            break


# Call the ui function to start the program
ui()
