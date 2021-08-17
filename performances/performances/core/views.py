from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PredictModel
import pickle
from .models import performancePredict
from sklearn import preprocessing
# Create your views here.


def home(request):
    if request.method=="POST":
        form=PredictModel(request.POST)
        if form.is_valid():
            Pstatus=form.cleaned_data.get("Pstatus")
            print( Pstatus)

            reason=form.cleaned_data.get("reason")
            print( reason )

            studytime=form.cleaned_data.get("studytime")
            print(studytime)

            failures=form.cleaned_data.get("failures")
            print(failures)

            internet=form.cleaned_data.get("internet")
            print(internet)

            freetime=form.cleaned_data.get("freetime")
            print(freetime)

            G1=form.cleaned_data.get("G1")
            print(G1)

            G2=form.cleaned_data.get("G2")
            print(G2)

            internet_pkl=pickle.load(open("core/my_model/new_data.internet.pkl", "rb"))
            Pstatus_pkl=pickle.load(open("core/my_model/new_data.Pstatus.pkl", "rb"))
            reason_pkl=pickle.load(open("core/my_model/new_data.reason.pkl", "rb"))

            enc_int = internet_pkl.transform([internet])

            enc_Pst = Pstatus_pkl.transform([Pstatus])
            enc_rea = reason_pkl.transform([reason])
            
            #form.save()
            model_pkl = pickle.load(open("core/my_model/rfc_2.sav",'rb'))
            results= model_pkl.predict([[enc_Pst,enc_rea, studytime,failures,enc_int, freetime, G1, G2]])
            classification= results[0]
            p= performancePredict(Pstatus=Pstatus,reason=reason,studytime=studytime,failures=failures,internet=internet,freetime=freetime,G1=G1, G2=G2,classification=classification)
            p.save()
            return render(request, 'core/dashboard.html', {"classification":classification} )
    else:

        form= PredictModel()

    return render(request, 'core/home.html', {"form":form})


@login_required()
def predict(request):
    predicts= performancePredict.objects.all()
    return render(request, 'core/predict.html', {'predicts':predicts})

def dashboard(request):
    return render(request, 'core/dashboard.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')

    else:
        form = UserRegisterForm()

    return render(request, 'core/register.html', {'form': form})
