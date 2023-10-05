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
        #  print("You query type was: " + validQueryTypes[0] + " to prove it, the user input was: " + queryType)
        #  Line Above Used for testing

    elif queryType == validQueryTypes[1:3]:  # If the query type is Type.NS
        check = True  # Updates the boolean variable to leave the while loop
        #  print("You query type was: " + validQueryTypes[1:3] + " to prove it, the user input was: " + queryType)
        #  Line Above Used for testing

    elif queryType == validQueryTypes[3:5]:  # If the query type is Type.MX
        check = True  # Updates the boolean variable to leave the while loop
        #  print("You query type was: " + validQueryTypes[3:5] + " to prove it, the user input was: " + queryType)
        #  Line Above Used for testing

    else:  # Else, the inputted query type isn't one of the program's valid types.
        print("Invalid query type. Please try again and enter a valid query type.")  # Tells the user, it is not valid

# print("You entered the domain: " + domainName)  # Used for testing purposes
# print("You entered the query type: " + queryType)  # Used for testing purposes

try:
    search = dns.resolver.resolve(domainName, queryType)  # Performs the dns.resolver search
    print("Domain: " + f"{domainName}")  # Prints the User Inputted Domain Name
    print("Query Type: " + f"{queryType}")  # Prints the User Inputted Query Type
    for rdata in search:  # For each loop to assure all data is printed
        print(f"{rdata}")  # Prints the data found from the dns.resolver search

except Exception as NXDomain:  # Exception added if the domain isn't found/doesn't exist
    print(domainName + " is an invalid domain")

except Exception as e:  # Standard Error Exception
    print("An error has occurred: " + {e})

sys.exit(0)