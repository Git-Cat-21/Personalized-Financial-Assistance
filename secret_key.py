import os
import binascii

# Generate a random 24-byte key and convert it to a hexadecimal string
secret_key = binascii.hexlify(os.urandom(24)).decode()
print("Your secret key:", secret_key)


#This key is used to securely sign session cookies and must be set to enable session-based features, 
# like flashing messages.