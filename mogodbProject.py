import json
from bson import json_util 
from pymongo import MongoClient

# Making a Connection with MongoClient (using default host and port)
connection = MongoClient()

#//////////////////////////////////////
# Getting a Database                //
db = connection["city"]           #//
collection = db["inspections"]   #//
#//////////////////////////////////

# ============================================== Create Docs
def insert_document(document):
    status = True

    try:
        collection.insert_one(document)
    except Exception as e:
        print("\n\t -->", e)
        status = False
        
    return status

# ============================================== Read Docs
def read_document(document):
    result = ""

    try:
        result = collection.find_one(document)
    except Exception as e:
        print("\n\t -->", e)
    
    return result
  
# ============================================== Update Docs
def update_document(document, update):
    status = True

    try:
        collection.update_one(document, {"$set" : update})
    except Exception as e:
        print("\n\t -->", e)
        status = False
        
    return status
  
# ============================================== Delete Docs
def delete_document(document):
    status = True

    try:
        collection.delete_one(document)

    except Exception as e:
        print("\n\t -->", e)
        status = False
        
    return status
  
# ============================================== Main
def main():
  
    while True:
      print("==========================================================")
      print("1 - Create")
      print("2 - Read")
      print("3 - Update")
      print("4 - Delete")
      print("5 - Exit\n")
      userInput = int(input("Enter number choice: "))
      
      # Create
      if userInput == 1:
        userInputDoc = input("Enter document to create (i.e. {\"_id\" : 355, \"name\" : \"test\"}): \n")
        status = insert_document(json.loads(userInputDoc))
        print("\nDocument Created:", status)
        
      # Read
      elif userInput == 2:
        userInputDoc = input("Enter \"_id\" of document to be read (i.e {\"_id\" : 355}): \n")
        result = read_document(json.loads(userInputDoc))
        # Prints JSON of read document.
        print("\nRead Document:\n" + json.dumps(result, indent = 4))
        
      # Update
      elif userInput == 3:
        userInputDoc = input("Enter document \"_id\" to update (i.e {\"_id\" : 355}): \n")
        userInputDoc2 =  input("Enter update (i.e. {\"name\" : \"Updated Value UPDATED\"}): \n")
        status = update_document(json.loads(userInputDoc), json.loads(userInputDoc2))
        print("\nDocument Updated:", status)
        
      # Delete  
      elif userInput == 4: 
        userInputDoc = input("Enter \"_id\" of document to be deleted (i.e {\"_id\" : 355}): \n")
        status = delete_document(json.loads(userInputDoc))
        print("Document Deleted:", status)
        
      # Exit  
      elif userInput == 5:
        break;
      
      # Default
      else:
        print("Option not valid, enter a number from 1 to 5: ")      

      
#//////////////
main()     #//
#////////////
