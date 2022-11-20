from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import BarOr, BarorScore
from soldiers.models import Soldier


def list_of_barors(request):
    barors = BarOr.objects.all()
    return render(request, 'list_of_barors.html', {'barors':barors})


def create_baror(request):
    
    if request.method == 'POST':
        baror_round = request.POST.get('baror_round')
        new_baror = BarOr(baror_round=baror_round)
        new_baror.save()
        return redirect('baror:all-barors')
    return render(request, 'create_baror.html')


def add_baror_round(request):
    barors_counter = BarOr.objects.count()
    try:
        
        baror = BarOr(baror_round=f'BarOr {barors_counter+1}')
        baror.save()
        messages.success(request, "Round added successfully" )
    except Exception as ex:
        messages.error(request, f'ERROR! {str(ex)}')
    finally:
        return redirect('barors:all-barors')

    return HttpResponse(f"{ barors_counter} add baror")



def edit_baror(request, pk):
    print(pk)
    baror = BarOr.objects.get(id=pk)
    soldiers = Soldier.objects.filter(soldier_status='Waiting for Baror')
    return render(request, 'edit_baror.html', {'baror':baror,'soldiers':soldiers})



def add_soldier_to_round(request, pk, soldier_id):
    baror_id = request.GET.get('pk')
    print(baror_id)
    soldier_id = request.GET.get('soldier_id')
    print( soldier_id)
    soldier = Soldier.objects.get(id=soldier_id)
    print(soldier.name)
    print(pk)
    baror = BarOr.objects.get(id=pk)
    soldiers = Soldier.objects.filter(soldier_status='Waiting for Baror')

    return render(request, 'edit_baror.html', {'baror':baror,'soldiers':soldiers})






















# def delete_baror(request, pk):
#     # only admin
#     # if not request.user.is_staff:
#     #     return HttpResponse('YOU ARE Not allowed to delete books')
#     try:
#         baror = BarOr.objects.get(id=pk)
#         baror_name = baror.baror_round
#         messages.success(request, f'{baror_name} deleted!')
#         return redirect('baror:all-barors')
#     except Exception as ex:
#         messages.error(request, f'ERROR! {str(ex)}')

#     return HttpResponse(f'delete baror')






















#     # add a book
# @admin_bp.route('/addbook', methods=['GET','POST'])
# @login_required
# @admin_login_required
# def add_book():
#         if request.method == 'POST':
#             book = request.form.get('bookname')
#             price = request.form.get('price')
#             picture = request.files.get('picture')
#             upload_file()
#             print(f"{book},{price},{picture}")
#             add_book_to_data(book=book, price=price, picture=picture.filename)
#             return redirect('/admin/home')
#         return render_template("admin/add_book_form.html")