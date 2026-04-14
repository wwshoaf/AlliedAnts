# Build main.py top-level CLI menu
# Imports all modules · loops until exit · routes to submenus
import time


# Greetings
print("Welcome to YOGA Studio Management System.")
print("  a product of Allied Ants @2026\n")


state_flag = 'root'

while 1:
    # Give user time to read any error message
    time.sleep(0.5)

    match state_flag:
        # Default menu
        case 'root':
            print("Main Menu\nPlease enter an option:\n\t(1) Find / Look up\n\t(2) New / Update")
            print("\t(3) Generate reports\n\t(4) Exit")
            line = input().strip()
            print()
            match line:
                case '1':
                    state_flag = 'query'
                    continue
                case '2':
                    state_flag = 'update'
                    continue
                case '3':
                    state_flag = 'reports'
                    continue
                case '4':
                    print("closing... Have a good day ：）")
                    break
                case _: 
                    print('Invalid input. Please try again.')
                    continue
        # Primary
        case 'query':
            print("Please choose what you want to look up for:")
            print("(0) Go back\n\t(1) Person\n\t(2) Class\n\t(3) Transaction")
            line = input().strip()
            print()
            match line:
                case '1':
                    state_flag = 'query_person'
                    continue
                case '2':
                    state_flag = 'query_Class'
                    continue
                case '3':
                    state_flag = 'query_Transaction'
                    continue
                case '0':
                    state_flag = 'root'
                    continue
                case _: 
                    print('Invalid input. Please try again.')
                    continue
        case 'query_person':
            print('')
        case 'query_Class':
            print('')
        case 'query_Transaction':
            print('')
            
        # Primary
        case 'update':
            print("Please choose what you want to add or update:")
            print("(0) Go back\n\t(1) Person\n\t(2) Class\n\t(3) Transaction")
            line = input().strip()
            print()
            match line:
                case '1':
                    state_flag = 'update_person'
                    continue
                case '2':
                    state_flag = 'update_class'
                    continue
                case '3':
                    state_flag = 'update_trans'
                    continue
                case '0':
                    state_flag = 'root'
                    continue
                case _: 
                    print('Invalid input. Please try again.')
                    continue
        case 'update_person':
            print('')
        case 'update_class':
            print('')
        case 'update_trans':
            print('')

        # Primary
        case 'reports':
            print("Please choose which report to generate:")
            print("(0) Go back\n\t(1) Revenue\n\t(2) Classes per teacher\n\t(3) Attendance")
            line = input().strip()
            print()
            match line:
                case '1':
                    state_flag = 'reports_rev'
                    continue
                case '2':
                    state_flag = 'reports_teach'
                    continue
                case '3':
                    state_flag = 'reports_attn'
                    continue
                case '0':
                    state_flag = 'root'
                    continue
                case _: 
                    print('Invalid input. Please try again.')
                    continue
        case 'reports_rev':
            print('')
        case 'reports_teach':
            print('')
        case 'reports_attn':
            print('')


        # catch fall through
        case _:
            print("Unsupported function. Returning to main menu...")
            state_flag='root'
            continue