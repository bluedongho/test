from django.shortcuts import render
from .models import ResMenu 

# 1번
def home(request):
    res_menu = ResMenu.objects.order_by('?')[:1]
    return render(request, "index.html", {"res_menu":res_menu})

# 2번
# def home(request):
#     conn, cur=None, None
#     row=""

#     conn=pymysql.connect(host='192.168.3.22',user='root',password='1q2w3e4r5t',db='launch_menu',charset='utf8')
#     cur=conn.cursor()

#     cur.execute("select * from res_menu")
#     # cur.execute("select emp_no from res_menu")

#     row=cur.fetchall()
#     random_menu=random.choice(row)

#     conn.close()
#     return HttpResponse(random_menu)

# 3번
# def home(request):
#     random_num=random.randint(1, 3)
#     res_menu = ResMenu.objects.filter(menu_no = random_num)
#     return render(request, "index.html", {"res_menu":res_menu})