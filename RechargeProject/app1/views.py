from django.shortcuts import render
from app1.models import RechargeCardM
from app1.forms import CreditCardF
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

class RechargeCardV():
    code=''

    def index(request):
        return render(request,'index.html')

    def purchase(request):
         context={}
         context1={}
         nums=[1,2,3,4]
         n=0
         for num1 in nums:
            for num2 in nums:
                 context['model'+str(n)] = RechargeCardM.objects.filter(name=num1, price=num2)
                 n+=1
         try:
             if request.GET.get('0')=='100 Naira':
                 context1['sam']=context['model0'][0].code
                 RechargeCardM.code=context['model0'][0].code
                 context['model0'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('1')=='200 Naira':
                 context1['sam']=context['model1'][0].code
                 RechargeCardM.code=context['model1'][0].code
                 context['model1'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('2')=='500 Naira':
                 context1['sam']=context['model2'][0].code
                 RechargeCardM.code=context['model2'][0].code
                 context['model2'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('3')=='1000 Naira':
                 context1['sam']=context['model3'][0].code
                 RechargeCardM.code=context['model3'][0].code
                 context['model3'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('4')=='100 Naira':
                 context1['sam']=context['model4'][0].code
                 RechargeCardM.code=context['model4'][0].code
                 context['model4'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('5')=='200 Naira':
                 context1['sam']=context['model5'][0].code
                 RechargeCardM.code=context['model5'][0].code
                 context['model5'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('6')=='500 Naira':
                 context1['sam']=context['model6'][0].code
                 RechargeCardM.code=context['model6'][0].code
                 context['model6'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('7')=='1000 Naira':
                 context1['sam']=context['model7'][0].code
                 RechargeCardM.code=context['model7'][0].code
                 context['model7'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('8')=='100 Naira':
                 context1['sam']=context['model8'][0].code
                 RechargeCardM.code=context['model8'][0].code
                 context['model8'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('9')=='200 Naira':
                 context1['sam']=context['model9'][0].code
                 RechargeCardM.code=context['model9'][0].code
                 context['model9'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('10')=='500 Naira':
                 context1['sam']=context['model10'][0].code
                 RechargeCardM.code=context['model10'][0].code
                 context['model10'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('11')=='1000 Naira':
                 context1['sam']=context['model11'][0].code
                 RechargeCardM.code=context['model11'][0].code
                 context['model11'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('12')=='100 Naira':
                 context1['sam']=context['model12'][0].code
                 RechargeCardM.code=context['model12'][0].code
                 context['model12'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('13')=='200 Naira':
                 context1['sam']=context['model13'][0].code
                 RechargeCardM.code=context['model13'][0].code
                 context['model13'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('14')=='500 Naira':
                 context1['sam']=context['model14'][0].code
                 RechargeCardM.code=context['model14'][0].code
                 context['model14'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
             elif request.GET.get('15')=='1000 Naira':
                 context1['sam']=context['model15'][0].code
                 RechargeCardM.code=context['model15'][0].code
                 context['model15'][0].delete()
                 return HttpResponseRedirect(reverse("app1:payment"))
         except:
            RechargeCardM.code='Sorry there are no codes for now. You will not be charged'
            return HttpResponseRedirect(reverse("app1:payment"))

         return render(request,'purchase.html',context=context1)



    def payment(request):
         form=CreditCardF()

         if request.method=="POST":
             form=CreditCardF(request.POST)
             if form.is_valid():
                 form.save(commit=True)
                 return HttpResponseRedirect(reverse("app1:show"))
             else:
                 print('Error from invalid')
         return render(request,'payment.html',{'form':form})

    def show(request):
         dict={'code':RechargeCardM.code}
         return render(request,'about.html',context=dict)
    def about(request):
        return render(request,'about1.html')
