from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
def index(request):
    return render(request,'index.html')
def exchange(request):
    params={'Argentine Peso': '0.977480', 'Australian Dollar': '0.018750', 'Bahraini Dinar': '0.005035', 'Botswana Pula': '0.155378', 'Brazilian Real': '0.072466', 'British Pound': '0.010260', 'Bruneian Dollar': '0.018389', 'Bulgarian Lev': '0.022318', 'Canadian Dollar': '0.017811', 'Chilean Peso': '10.617068', 'Chinese Yuan Renminbi': '0.093008', 'Colombian Peso': '50.100132', 'Croatian Kuna': '0.085329', 'Czech Koruna': '0.298411', 'Danish Krone': '0.084991', 'Emirati Dirham': '0.049177', 'Euro': '0.011411', 'Hong Kong Dollar': '0.103781', 'Hungarian Forint': '3.935283', 'Icelandic Krona': '1.838266', 'Indonesian Rupiah': '196.866408', 'Iranian Rial': '564.060279', 'Israeli Shekel': '0.045649', 'Japanese Yen': '1.426645', 'Kazakhstani Tenge': '5.607301', 'Kuwaiti Dinar': '0.004094', 'Libyan Dinar': '0.018333', 'Malaysian Ringgit': '0.056177', 'Mauritian Rupee': '0.531949', 'Mexican Peso': '0.300127', 'Nepalese Rupee': '1.607500', 'New Zealand Dollar': '0.020355', 'Norwegian Krone': '0.120689', 'Omani Rial': '0.005149', 'Pakistani Rupee': '2.255569', 'Philippine Peso': '0.655238', 'Polish Zloty': '0.050261', 'Qatari Riyal': '0.048742', 'Romanian New Leu': '0.055170', 'Russian Ruble': '0.979305', 'Saudi Arabian Riyal': '0.050215', 'Singapore Dollar': '0.018389', 'South African Rand': '0.234258', 'South Korean Won': '15.871936', 'Sri Lankan Rupee': '2.467380', 'Swedish Krona': '0.117357', 'Swiss Franc': '0.012285', 'Taiwan New Dollar': '0.393934', 'Thai Baht': '0.417002', 'Trinidadian Dollar': '0.090598', 'Turkish Lira': '0.096683', 'US Dollar': '0.013391', 'Venezuelan Bolivar': '0.133739'}
    if  request.method=="POST":
        amount=int(request.POST.get("Amount",""))
        currency=request.POST.get("Currency","")
        d=amount*float(params[currency])

        messages.success(request,f"{amount} INR is equal to {d} {currency}")
    return redirect('/')
   
    