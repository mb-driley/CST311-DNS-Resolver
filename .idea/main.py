import sys

check = False
validQueryTypes = "ANSMX"
domainName = input("Enter a domain: ")  # Prompts the user to enter a domain

while not check:
    queryType = input("Enter a query type (A, NS, MX): ").upper()  # Prompts the user to enter a query type
    if queryType == validQueryTypes[0]:
        check = True

    elif queryType == validQueryTypes[1:3]:
        check = True

    elif queryType == validQueryTypes[3:5]:
        check = True

    else:
        print("Invalid query type. Please try again and enter a valid query type.")


print("You entered the domain: " + domainName)  # Used for testing purposes
print("You entered the query type: " + queryType)  # Used for testing purposes
sys.exit(0)