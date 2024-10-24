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
        except json.JSONDecodeError:

            action = "wrong json"
            data = []
            result = sendResponse(404, data, action)

            return JsonResponse(json.loads(result))
        if 'action' in jsons:
            action = jsons['action']
            if action == 'login_cv':
                res = login_cv(request)
                return JsonResponse(json.loads(res))
            elif action == 'logout_cv':
                res = logout_cv(request)
                return JsonResponse(json.loads(res))
            elif action == 'addCv':
                address = jsons['personal_details']['address']
                lastname = jsons['personal_details']['lastname']
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
                            return JsonResponse(json.loads(res))
                        # userCount

                        query = f'''
                                    INSERT INTO whois.t_person_details(address, lastname,username,password)
                                    VALUES ('{address}', '{lastname}',
                                            '{username}','{password}')
                                    RETURNING pid'''

                        cur.execute(query)
                        con.commit()
                        # t_person_details

                        pid = cur.fetchone()[0]

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
                        # t_exp_respons

                        con.commit()

                        res = sendResponse(
                            200, [{'success': 'amjilttai burtgegdlee'}], action)
                        return JsonResponse(json.loads(res))

            else:
                action = "action not found"
                data = []
                result = sendResponse(404, data, action)
                return JsonResponse(json.loads(result))

        else:
            action = "no action"
            data = []
            result = sendResponse(404, data, action)
            return JsonResponse(json.loads(result))
    else:
        action = "method buruu"
        data = []
        result = sendResponse(405, data, action)
        return JsonResponse(json.loads(result))
