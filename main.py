from sort import SortResult
from logs import Logs


def find_repositories():
    """Function that provides to find github repositories by inputted repository name"""

    repo_name: str = input("\nInput Repository Name: ").strip()

    if repo_name == '':  # Repository cannot be empty string
        print('\nRepository name must include characters!')
    else:
        log = Logs()
        log.log_search(search_request=repo_name)
        sort_result = SortResult(repo_name=repo_name)

        if sort_result.check_repo_quantity():
            sort_order = input("Do you want to sort order in [A]scending or in [D]escending?: ")

            if sort_order.lower() == 'a' or sort_order.lower() == 'ascending':
                sort_result.ascending()
            elif sort_order.lower() == 'd' or sort_order.lower() == 'descending':
                sort_result.descending()
            else:
                print("Input is incorrect!")
                userInput = input("Do you want to try again? \n[Y]es/[N]o: ").strip()

                if userInput.lower() == 'y' or userInput.lower() == 'yes':
                    find_repositories()
                elif userInput.lower().strip() == 'n' or userInput.lower().strip() == 'no':
                    print("\n<-Back")
        else:
            print("\nNo repos found. Try another repository name!")


def main():
    """Main function which runs first"""

    print("\n<<<Hello this is app which can give you list of github repositories>>>\n")
    user_input = input("Do You Want To Find Github Repositories?\n[Y]es or [N]o: ")
    log = Logs()

    if user_input.lower() == 'yes' or user_input.lower() == 'y':
        while True:
            print("\n1) Input Repository Name\n2) Searched Repositories\n3) Exit\n")
            user_input = input("Which action do you want?: ")

            if user_input.strip() == '1':
                find_repositories()

            elif user_input.strip() == '2':
                print('\nList of searched repositories:\n')
                log.print_searched_repos('search.log')

            elif user_input.strip() == '3':
                print('\nBye, Have A Good Time!')
                break
    else:
        print('\nBye, Bye. Wish You All The Best!')


if __name__ == "__main__":
    main()
