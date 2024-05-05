from django.http import JsonResponse
from django.middleware.csrf import get_token
# Create your views here.

# Initialize Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, firestore, db
import json
cred = credentials.Certificate('/home/k213458/Documents/WebProjects/lookflock/lookflockbackend/drf/certificate.json')
firebase_admin.initialize_app(cred, {"databaseURL":"https://lookflock-asad-default-rtdb.asia-southeast1.firebasedatabase.app"})

db = firestore.client()

# Django view to retrieve CSRF token
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

def readAll(request):
    if request.method == "GET":
        count = request.GET.get('count')
        if count == None:
            count = 10
        else:
            count = int(count)
        print(count)
        docs = db.collection('lookflock').where('id', '<=', count).stream()
        # Convert documents to a list of dictionaries
        documents_data = [doc.to_dict() for doc in docs]
        # Print documents in pretty format
        print(json.dumps(documents_data, indent=2))
        return JsonResponse(documents_data, safe=False)
def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('name')
        print(name)
        imageURL = data.get('imageURL')
        currentPrice = data.get('currentPrice')
        oldPrice = data.get('oldPrice')
        discount = data.get('discount')
        temp = db.collection("lookflock").stream()
        num_documents = sum(1 for _ in temp) 
        try:
            abc = db.collection("lookflock").document(str(num_documents+1))
            abc.set({
                "id":num_documents+1,
                "name":name ,
                "imageURL":imageURL ,
                "currentPrice":currentPrice ,
                "oldPrice":oldPrice ,
                "discount":discount ,
            })
        except Exception as e:
            print("Error creating document:", e)
        return JsonResponse({"response":"Created successfully! "})
    else:
        # Return error response for unsupported HTTP methods
        return JsonResponse({'error': 'Only POST requests are supported'}, status=405)
def update(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        id = data.get('id')
        updated_name = data.get('name')
        updated_imageURL = data.get('imageURL')
        updated_currentPrice = data.get('currentPrice')
        updated_oldPrice = data.get('oldPrice')
        updated_discount = data.get('discount')
        try:
            doc_ref = db.collection('lookflock').document(str(id))
            # Update multiple fields
            doc_ref.update({
            "id": id,
            "name": updated_name,
            "imageURL": updated_imageURL,
            "currentPrice": updated_currentPrice,
            "oldPrice": updated_oldPrice,
            "discount": updated_discount
            })
        except Exception as e:
            print("Error updating document:", e)
        return JsonResponse({"response":"Updated successfully! "})
    else:
        # Return error response for unsupported HTTP methods
        return JsonResponse({'error': 'Only PUT requests are supported'}, status=405)
def delete(request):
    if request.method == "DELETE":
        data = json.loads(request.body)
        id = data.get('id')
        print(id)
        try:
            doc_ref = db.collection('lookflock').document(str(id))
            doc_ref.delete()
        except Exception as e:
            print("Error deleting document:", e)
        return JsonResponse({"response":"Deleted successfully! "})
    else:
        # Return error response for unsupported HTTP methods
        return JsonResponse({'error': 'Only DELETE requests are supported'}, status=405)
