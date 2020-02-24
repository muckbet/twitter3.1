from docs import twitter_api


def get_twitter_acc():
    """
    (None) -> str

    Get twitter account
    """
    while True:
        user_name = input("Enter Twitter Account: ")
        if user_name:
            return user_name


def call_next_dict(json_dict, next_one, stack):
    """
    (dict, str, list) -> None

    Go through the directory
    """
    try:
        if next_one in json_dict:
            stack.append(json_dict)
            if type(json_dict[next_one]) == dict:
                go_through_json(json_dict[next_one], stack)
            elif type(json_dict[next_one]) == list:
                n = len(json_dict[next_one])
                d = {}
                for i in range(n):
                    d[str(i + 1)] = json_dict[next_one][i]
                go_through_json(d, stack)
            else:
                print(json_dict[next_one])
                back = input("Enter anything you will go back: ")
                if back == 'b':
                    go_through_json(stack.pop(-1), stack)
                else:
                    go_through_json(json_dict, stack)
        elif next_one == 'b':
            if stack == []:
                print("You cannot go back")
                go_through_json(json_dict, stack)
            go_through_json(stack.pop(-1), stack)
        else:
            go_through_json(json_dict, stack)
    except (KeyboardInterrupt, IndexError):
        print("\nClosed.")


def go_through_json(json_dict, stack):
    """
    (dict, list) -> None

    Print next possibles elements and call next element
    """
    for key in json_dict:
        print(key, end=" || ")
    next_one = input("\nEnter next element or \"b\" to go back: ")
    call_next_dict(json_dict, next_one, stack)


def main():
    """
    (None) -> None

    Run all functions
    """
    user_name = get_twitter_acc()
    json_friends = twitter_api.main(user_name)
    print("If you want to close this program press \"Ctrl + C\"")
    if json_friends:
        go_through_json(json_friends, [])


if __name__ == "__main__":
    main()
