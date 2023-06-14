from django.shortcuts import render


def halaman(request):
    judul = "Fashion Pria", "Sepatu", "Sandal", "Jam Tangan", "Tas Pria"
    pembeli = "Sofi"

    konteks = {
        'title': judul,
        'pembeli': pembeli,
    }
    return render(request, 'halaman.html', konteks)



