import base64
from google.cloud import kms
def hello_pubsub(event, context):


     # Create the client.
     client = kms.KeyManagementServiceClient()


     plaintext = " some text "
     import base64

     # Build the key name.
     #k
     key_name = client.crypto_key_path("<Project-Name>", "<KEY REGION, e.g: us-central1>", "<CMEK_KEY_RING_NAME>", "<CMEK_KEY_NAME>")
     print (key_name)

     # Convert the plaintext to bytes.
     try:
          plaintext_bytes = plaintext.encode('utf-8')
          encrypt_response = client.encrypt(request={'name': key_name, 'plaintext': plaintext_bytes})
          print('Ciphertext: {}'.format(base64.b64encode(encrypt_response.ciphertext)))
          print (encrypt_response)
          # Take actions here if access to CMEK works
     except:
          print ("Take action, there is no access to CMEK !!!")
          # Take actions here if access to CMEK does not work
