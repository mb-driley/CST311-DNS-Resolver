import sys
import dns.resolver
from dns import rdata

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

    else:  # Else, the inputted query type isn't one of the program's valid types.
        print("Invalid query type. Please try again and enter a valid query type.")  # Tells the user, it is not valid

# print("You entered the domain: " + domainName)  # Used for testing purposes
# print("You entered the query type: " + queryType)  # Used for testing purposes

try:
    search = dns.resolver.resolve(domainName, queryType)
    print("Domain: " + f"{domainName}")
    print("Query Type: " + f"{queryType}")
    for rdata in search:
        print(f"{rdata}")

except Exception as e:
    print("An error has occurred: " + {e})

sys.exit(0)