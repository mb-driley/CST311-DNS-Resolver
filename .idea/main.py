import sys

domainName = input("Enter a domain: ")  # Prompts the user to enter a domain
queryType = input("Enter a query type (A, NS, MX): ").upper()  # Prompts the user to enter a query type
print("You entered the domain: " + domainName)  # Used for testing purposes
print("You entered the query type: " + queryType)  # Used for testing purposes
sys.exit(0)