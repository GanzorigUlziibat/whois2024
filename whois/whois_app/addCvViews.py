from django.shortcuts import render
from django.http import JsonResponse
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from whois.settings import sendResponse, connectDB, disconnectDB


def index(request):
    return render(request, 'index.html', {'aichitsu': 'Hello world'})
# hamaaralgui


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
            if action == 'addCv':
                address = jsons['personal_details']['address']
                lastname = jsons['personal_details']['lastname']

                con = connectDB()
                cur = con.cursor()
                query = f'''
                            INSERT INTO whois.t_person_details(address, lastname)
                            VALUES ('{address}', '{lastname}')
                            RETURNING pid'''

                cur.execute(query)
                con.commit()

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
                                                VALUES({pid}, '{company}')
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
                cur.close()
                disconnectDB(con)

                res = sendResponse(200, [], action)
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
