from django.shortcuts import render
from django.http import JsonResponse
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from whois.settings import sendResponse, connectDB, disconnectDB


def index(request):
    return render(request, 'index.html', {'aichitsu': 'Hello world'})
# hamaaralgui


def login_cv(request):
    data = json.loads(request.body)
    action = data['action']
    username = data['personal_details']['username']
    password = data['personal_details']['password']

    with connectDB() as con:
        with con.cursor() as cur:
            query = f'''select COUNT(*) from whois.t_person_details p
                        where p.username ='{username}' and p.password='{password}'
                    '''

            cur.execute(query)
            userCount = cur.fetchone()[0]
            if userCount == 0:
                res = sendResponse(
                    301, [{'error': 'Таны нэвтрэх нэр эсвэл нууц үг буруу байна'}], action)
                return res
            # userCount
            query = f'''select p.pid from whois.t_person_details p
                    where p.username ='{username}'
            '''

            cur.execute(query)
            pid = cur.fetchone()[0]
            res = sendResponse(
                200, [{'success': 'Та амжилттай нэвтэрлээ', "pid": pid}], action)
            return res


def logout_cv(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    request.session.flush()
    res = sendResponse(200, [{'success': 'Та амжилттай гарлаа'}], action)
    return res


@ csrf_exempt
def addCv(request):
    if request.method == "POST":
        try:
            jsons = json.loads(request.body)
        except:
            result = sendResponse(4001)
            return JsonResponse(result)
        if 'action' in jsons:
            action = jsons['action']
            if action == 'login_cv':
                res = login_cv(request)
                return JsonResponse(res)
            elif action == 'logout_cv':
                res = logout_cv(request)
                return JsonResponse(res)
            elif action == 'addCv':
                firstname = jsons['personal_details']['firstname']
                lastname = jsons['personal_details']['lastname']
                headline = jsons['personal_details']['headline']
                address = jsons['personal_details']['address']
                phone = jsons['personal_details']['phone']
                email = jsons['personal_details']['email']
                linkedin = jsons['personal_details']['linkedin']
                github = jsons['personal_details']['github']
                facebook = jsons['personal_details']['facebook']
                summary = jsons['personal_details']['summary']
                city = jsons['personal_details']['city']
                username = jsons['personal_details']['username']
                password = jsons['personal_details']['password']

                with connectDB() as con:
                    with con.cursor() as cur:
                        query = f'''select COUNT(*) from whois.t_person_details
                                    where username='{username}'
                                    '''
                        cur.execute(query)
                        userCount = cur.fetchone()[0]

                        if userCount != 0:
                            res = sendResponse(
                                301, [{'error': 'username давхцаж байна'}], action)
                            return JsonResponse(res)
                        # userCount

                        query = f'''
                            INSERT INTO whois.t_person_details(
                                firstname, lastname, headline, address, phone, email,
                                linkedin, github, facebook, summary, username, password, city)
                            VALUES (
                                '{firstname}', '{lastname}', '{headline}', '{address}', '{phone}', '{email}',
                                '{linkedin}', '{github}', '{facebook}', '{summary}', '{username}', '{password}', '{city}')
                            RETURNING pid, username
                                '''


                        cur.execute(query)
                        con.commit()
                        pid = cur.fetchone()[0]
                        # t_person_details

                        eduCount = len(jsons['education'])
                        if eduCount > 0:
                            for i in jsons['education']:
                                query = f'''
                                            INSERT INTO whois.t_education(pid, institution, start_year)
                                            VALUES (
                                                {pid},'{i["institution"]}', '{i["start_year"]}')
                                            '''
                                cur.execute(query)
                        # t_education

                        expCount = len(jsons['experience'])

                        if expCount > 0:
                            for i in jsons['experience']:
                                company = i['company']
                                query = f'''
                                            INSERT INTO whois.t_experience(pid, company)
                                                        VALUES(
                                                            {pid}, '{company}')
                                                        returning expid
                                        '''

                                cur.execute(query)
                        # t_experience

                                expid = cur.fetchone()[0]
                                resCount = len(i['responsibilities'])
                                if resCount > 0:
                                    for j in i['responsibilities']:
                                        query = f'''
                                            INSERT INTO whois.t_exp_respons(expid,responsibilities)
                                            VALUES (
                                                {expid},'{j}')
                                            '''
                                        cur.execute(query)
                                        con.commit()
                        # t_exp_respons

                        skills = jsons['skills']
                        if 0 < len(skills):
                            for i in skills:
                                skill = i['skill']
                                profid = i['proficiency']
                                query = f'''
                                        INSERT INTO whois.t_skills(skill,pid,profid)
                                                            VALUES('{skill}', {pid},{profid}) '''
                                cur.execute(query)
                                con.commit()
                            # skills

                        res = sendResponse(
                            200, [{'success': 'amjilttai burtgegdlee ta login hiij orno uu'}], action)
                        return JsonResponse(res)

            else:
                action = "action not found"
                data = []
                result = sendResponse(404, data, action)
                return JsonResponse(result)

        else:
            action = "no action"
            data = []
            result = sendResponse(404, data, action)
            return JsonResponse(result)
    else:
        action = "method buruu"
        data = []
        result = sendResponse(405, data, action)
        return JsonResponse(result)
