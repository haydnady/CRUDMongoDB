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
    result = ""
    status = True

    try:
        result = collection.insert_one(document)
    except Exception as e:
        print("\nERROR insert_document:", e)
        status = False
        
    return result, status

# ============================================== Read Docs
def read_document(document):
    result = ""

    try:
        result = collection.find_one(document)
    except Exception as e:
        print("\nERROR read_document:", e)
        result = "Failed to retrieve data"
    
    return result
  
# ============================================== Update Docs
def update_document(document, update):
    result = ""

    try:
        collection.update_one(document, {"$set" : update})
        result = collection.find_one(document)
    except Exception as e:
        print("\nERROR update_document:", e)
        result = "Failed to update data"
        
    return result
  
# ============================================== Delete Docs
def delete_document(document):
    result = ""

    try:
        collection.delete_many(document)
        result = collection.find_one(document)
    except Exception as e:
        print("\nERROR delete_document:", e)
        result = "Failed to delete data"
        
    return result
  
# ============================================== Main
def main():
  
    while True:
      print("==========================================================")
      print("1 - Create")
      print("2 - Read")
      print("3 - Update")
      print("4 - Delete")
      print("5 - Exit")
      userInput = int(input("Enter number choice: "))
      
      # Create
      if userInput == 1:
        userInputDoc = input("Enter document to create: \n")
        result, status = insert_document(myDocument)
        print("\n1. Document Created:", status) # Prints status of inserted data (True/False)
        print("--------------------------------------")
        
      # Read
      elif userInput == 2:
        userInputDoc = input("Enter \"_id\" of document to be read: \n")
        # Prints JSON of read document
        print("2. Read Document:\n", json.dumps(result, indent = 4))
        print("--------------------------------------")
        
      # Update
      elif userInput == 3:
        userInputDoc = input("Enter document to update: \n")
        result= update_document({"_id" : 35445565655}, {"name" : "Updated Value UPDATED"})
        # Prints JSON of updated document
        print("3. Updated Document:\n", json.dumps(result, indent = 4))
        print("--------------------------------------")
        
      # Delete  
      elif userInput == 4: 
        userInputDoc = input("Enter \"_id\" of document to be deleted: \n")
        result = delete_document({"_id" : 35445565655})
        # Prints "JSON" (null, none) of deleted document
        print("4. Delete Document:\n", json.dumps(result, indent = 4))
        print("--------------------------------------")
        
      # Exit  
      elif userInput == 5:
        break;
      
      # Default
      else:
        print("Option not valid, enter a number from 1 to 4: ")      

      
#//////////////
main()     #//
#////////////
