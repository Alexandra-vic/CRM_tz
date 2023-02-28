# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponseNotFound
# from .models import Location, Product


# def index(request):
#     location = Location.objects.all()
#     return render(request, "index.html", {"location": location})

# def create(request):
#     if request.method == "POST":
#         location = Location()
#         location.city = request.POST.get("city")
#         location.save()
#     return HttpResponseRedirect("/")

# def edit(request, id):
#     try:
#         location = Location.objects.get(id=id)

#         if request.method == "POST":
#             location.city = request.POST.get("city")
#             location.save()
#             return HttpResponseRedirect("/")
#         else:
#             return render(request, "edit.html", {"location": location})
#     except Location.DoesNotExist:
#         return HttpResponseNotFound("<h2>Location not found</h2>")   


# def delete(request, id):
#     try:
#         location = Location.objects.get(id=id)
#         location.delete()
#         return HttpResponseRedirect("/")
#     except Location.DoesNotExist:
#         return HttpResponseNotFound("<h2>Location not found</h2>")     
    


# def index(request):
#     product = Product.objects.all()
#     return render(request, "index.html", {"product": product})

# def create(request):
#     if request.method == "POST":
#         product = Product()
#         product.name = request.POST.get("name")
#         product.description = request.POST.get("description")
#         product.price = request.POST.get("price")
#         product.location = request.POST.get("location")
#         product.save()
#     return HttpResponseRedirect("/")

# def edit(request, id):
#     try:
#         product = Product.objects.get(id=id)

#         if request.method == "POST":
#             product.name = request.POST.get("name")
#             product.description = request.POST.get("description")
#             product.price = request.POST.get("price")
#             product.location = request.POST.get("location")
#             product.save()
#             return HttpResponseRedirect("/")
#         else:
#             return render(request, "edit.html", {"product": product})
#     except Product.DoesNotExist:
#         return HttpResponseNotFound("<h2>Product not found</h2>")   


# def delete(request, id):
#     try:
#         product = Product.objects.get(id=id)
#         product.delete()
#         return HttpResponseRedirect("/")
#     except Product.DoesNotExist:
#         return HttpResponseNotFound("<h2>Product not found</h2>")     