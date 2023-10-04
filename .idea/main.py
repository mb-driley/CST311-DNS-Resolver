import sys

# Variables
check = False  # Boolean variable
validQueryTypes = "ANSMX"  # String variable

domainName = input("Enter a domain: ")  # Prompts the user to enter a domain
while not check:  # While loop to continue, if check isn't updated (No valid query types are inputted)
    queryType = input("Enter a query type (A, NS, MX): ").upper()  # Prompts the user to enter a query type
    if queryType == validQueryTypes[0]:  # If the query type is Type.A
        check = True  # Updates the boolean variable to leave the while loop

    elif queryType == validQueryTypes[1:3]:  # If the query type is Type.NS
        check = True  # Updates the boolean variable to leave the while loop

    elif queryType == validQueryTypes[3:5]:  # If the query type is Type.MX
        check = True  # Updates the boolean variable to leave the while loop

    else:
        print("Invalid query type. Please try again and enter a valid query type.")


print("You entered the domain: " + domainName)  # Used for testing purposes
print("You entered the query type: " + queryType)  # Used for testing purposes
sys.exit(0)