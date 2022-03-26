from django.shortcuts import render
from .models import UserData


# Create your views here.


def form(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone_num = request.POST.get("phone_num", "")
        city = request.POST.get("city", "")
        desc = request.POST.get("desc", "")
        tenthSchoolName = request.POST.get("tenthSchoolName", "")
        tenthPercentage = request.POST.get("tenthPercentage", "")
        twelveSchoolName = request.POST.get("twelveSchoolName", "")
        twelvePercentage = request.POST.get("twelvePercentage", "")
        collegeName = request.POST.get("collegeName", "")
        collegePercentage = request.POST.get("collegePercentage", "")
        projectName = request.POST.get("projectName", "")
        projectDesc = request.POST.get("projectDesc", "")
        firstSkill = request.POST.get("firstSkill", "")
        secondSkill = request.POST.get("secondSkill", "")
        thirdSkill = request.POST.get("thirdSkill", "")
        firstAchievement = request.POST.get("firstAchievement", "")
        secondAchievement = request.POST.get("secondAchievement", "")
        thirdAchievement = request.POST.get("thirdAchievement", "")
        hobby = request.POST.get("hobby", "")

        userData = UserData(name=name, email=email, phone_num=phone_num, city=city, desc=desc,
                            tenthSchoolName=tenthSchoolName, tenthPercentage=tenthPercentage,
                            twelveSchoolName=twelveSchoolName, twelvePercentage=twelvePercentage,
                            collegeName=collegeName, collegePercentage=collegePercentage,
                            projectName=projectName, projectDesc=projectDesc,
                            firstSkill=firstSkill, secondSkill=secondSkill, thirdSkill=thirdSkill,
                            firstAchievement=firstAchievement, secondAchievement=secondAchievement,
                            thirdAchievement=thirdAchievement, hobby=hobby
                            )
        userData.save()

    return render(request, 'index.html')
