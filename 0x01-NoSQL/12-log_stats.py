from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['logs']
collection = db['nginx']

# Get total number of documents
total_logs = collection.count_documents({})

# Get count of each HTTP method
methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
method_counts = {method: collection.count_documents({'method': method}) for method in methods}

# Get count of logs with method=GET and path=/status
status_check_count = collection.count_documents({'method': 'GET', 'path': '/status'})

# Print results
print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_check_count} status check")
