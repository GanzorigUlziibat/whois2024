from django.shortcuts import render
from django.http import JsonResponse
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from whois.settings import sendResponse, connectDB, disconnectDB


def index(request):
    return render(request, 'index.html', {'aichitsu': 'Hello world'})
# hamaaralgui


def gettime(request):
    ognoo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    res = {"date": ognoo}
    return res
# gettime


def get_personal_details(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    try:
        asuulttoo = jsons["asuulttoo"]
    except Exception as e:
        action = action
        data = [{"error": str(e) + " key error"}]
        result = sendResponse(404, data, action)
        return result
    try:

        myCon = connectDB()
        cursor = myCon.cursor()
        query = F"""SELECT  pid, fname, lname, headline, address, phone, email, linkedin, github, facebook, summary
                    FROM whois.t_person
                    ORDER BY random() LIMIT {asuulttoo}"""
        cursor.execute(query)
        columns = cursor.description
        respRow = [{columns[index][0]: column
                    for index, column in enumerate(value)} for value in cursor.fetchall()]

        cursor.close()
        disconnectDB(myCon)

        data = respRow
        result = sendResponse(200, data, action)
        return result
    except Exception as e:
        pass
# get_personal_details


def education(request):
    con = connectDB()
    cur = con.cursor()
    query = f'''SELECT eduid, degid, "institution ", location, s_year, d_year, description, bid
        FROM whois.t_education;'''
    cur.execute(query)
    columns = cur.description
    jsons = json.loads(request.body)
    action = jsons['action']
    respRow = [{columns[index][0]: column
                for index, column in enumerate(value)} for value in cur.fetchall()]
    cur.close()
    disconnectDB(con)
    return sendResponse(200, respRow, action)
# education


def experience(request):
    con = connectDB()
    cur = con.cursor()
    query = f'''SELECT expid, pid, jobid, company, location, start_date, end_date, respons
        FROM whois.t_experience;'''
    cur.execute(query)
    columns = cur.description
    jsons = json.loads(request.body)
    action = jsons['action']
    respRow = [{columns[index][0]: column
                for index, column in enumerate(value)} for value in cur.fetchall()]
    cur.close()
    disconnectDB(con)
    return sendResponse(200, respRow, action)
# experience


def skills(request):
    con = connectDB()
    cur = con.cursor()
    query = f'''SELECT skid, profid, skill, pid
        FROM whois.t_skills;'''
    cur.execute(query)
    columns = cur.description
    jsons = json.loads(request.body)
    action = jsons['action']
    respRow = [{columns[index][0]: column
                for index, column in enumerate(value)} for value in cur.fetchall()]
    cur.close()
    disconnectDB(con)
    return sendResponse(200, respRow, action)
# skills


def certifications(request):
    con = connectDB()
    cur = con.cursor()
    query = f'''SELECT cerid, pid, name, institution, year
        FROM whois.t_certifications;'''
    cur.execute(query)
    columns = cur.description
    jsons = json.loads(request.body)
    action = jsons['action']
    respRow = [{columns[index][0]: column
                for index, column in enumerate(value)} for value in cur.fetchall()]
    cur.close()
    disconnectDB(con)
    return sendResponse(200, respRow, action)
# certifications


def projects(request):
    con = connectDB()
    cur = con.cursor()
    query = f'''SELECT projid, pid, project_name, description, url
        FROM whois.t_projects;'''
    cur.execute(query)
    columns = cur.description
    jsons = json.loads(request.body)
    action = jsons['action']
    respRow = [{columns[index][0]: column
                for index, column in enumerate(value)} for value in cur.fetchall()]
    cur.close()
    disconnectDB(con)
    return sendResponse(200, respRow, action)
# projects


def languages(request):
    con = connectDB()
    cur = con.cursor()
    query = f'''SELECT lanid, pid, language, lprofid
        FROM whois.t_languages;'''
    cur.execute(query)
    columns = cur.description
    jsons = json.loads(request.body)
    action = jsons['action']
    respRow = [{columns[index][0]: column
                for index, column in enumerate(value)} for value in cur.fetchall()]
    cur.close()
    disconnectDB(con)
    return sendResponse(200, respRow, action)
# languages

def example(request):
    jsons = json.loads(request.body)
    action = jsons['action']
    respRow = [{
  "personal_details": {
    "firstname": "John",
    "lastname": "Boldoo",
    "headline": "uuriin tuhai",
    "address": "1234 Elm Street, Apt 567, Springfield, IL 62704, USA",
    "phone": "+1-234-567-8901",
    "email": "john.doe@example.com",
    "linkedin": "https://www.linkedin.com/in/johndoe",
    "github": "https://github.com/johndoe",
    "facebook": "https://fb.com/johndoe",
    "city": "Ulaanbaatar"
  },

  "summary": "Experienced software engineer with over 5 years of experience in full stack development, specializing in Python, JavaScript, and cloud technologies. Proven track record of building scalable applications and leading cross-functional teams.",

  "education": [
    {
      "degree": "Master of Science in Computer Science",
      "institution": "Stanford University",
      "location": "Stanford, CA",
      "start_year": 2016,
      "graduation_year": 2020,
      "description": "Focused on artificial intelligence and machine learning. Completed a thesis on deep learning algorithms for natural language processing. Participated in various research projects and collaborated with leading experts in the field."
    },
    {
      "degree": "Bachelor of Science in Computer Science",
      "institution": "University of Illinois at Urbana-Champaign",
      "location": "Champaign, IL",
      "start_year": 2016,
      "graduation_year": 2018,
      "description": "Specialized in software engineering and data structures. Graduated with honors and received the Dean's List award for academic excellence. Engaged in extracurricular activities such as coding competitions and hackathons."
    }
  ],

  "experience": [
    {
      "job_title": "Senior Software Engineer",
      "company": "Tech Solutions Inc.",
      "location": "Chicago, IL",
      "start_date": "2021-06",
      "end_date": "Present",
      "responsibilities": [
        "Lead a team of 5 engineers to develop and maintain a cloud-based SaaS platform.",
        "Implement microservices architecture to improve scalability and reduce latency.",
        "Conduct code reviews and mentor junior developers."
      ]
    },

    {
      "job_title": "Software Engineer",
      "company": "Innovative Apps LLC",
      "location": "Springfield, IL",
      "start_date": "2018-07",
      "end_date": "2021-05",
      "responsibilities": [
        "Developed front-end and back-end components for various web applications.",
        "Collaborated with UX/UI designers to create user-friendly interfaces.",

        "Optimized application performance, reducing load times by 30%."
      ]
    }
  ],

  "skills": [
    {
      "skill": "Python",
      "proficiency": "Expert"
    },
    {
      "skill": "JavaScript",
      "proficiency": "Advanced"
    },
    {
      "skill": "React",
      "proficiency": "Advanced"
    },
    {
      "skill": "Node.js",
      "proficiency": "Advanced"
    },
    {
      "skill": "Django",
      "proficiency": "Expert"
    },
    {
      "skill": "AWS",
      "proficiency": "Advanced"
    },
    {
      "skill": "Docker",
      "proficiency": "Intermediate"
    },
    {
      "skill": "Kubernetes",
      "proficiency": "Intermediate"
    },
    {
      "skill": "SQL",
      "proficiency": "Advanced"
    },
    {
      "skill": "NoSQL",
      "proficiency": "Advanced"
    }
  ],

  "certifications": [
    {
      "name": "AWS Certified Solutions Architect",
      "institution": "Amazon Web Services",
      "year": 2020
    },
    {
      "name": "Certified Kubernetes Administrator",
      "institution": "Cloud Native Computing Foundation",
      "year": 2019
    }
  ],

  "projects": [
    {
      "name": "E-commerce Platform",
      "description": "Developed a full-stack e-commerce platform using React, Node.js, and MongoDB. Implemented features such as product listings, shopping cart, and payment processing.",
      "url": "https://github.com/johndoe/ecommerce-platform"
    },
    {
      "name": "Chat Application",
      "description": "Built a real-time chat application using Django Channels and WebSockets. Integrated with a PostgreSQL database for persistent storage.",
      "url": "https://github.com/johndoe/chat-application"
    }
  ],

  "languages": [
    {
      "language": "English",
      "proficiency": "Native"
    },
    {
      "language": "Spanish",
      "proficiency": "Intermediate"
    }
  ],
  "hobbies": ["Hiking", "Photography", "Traveling"]
}
]
    return sendResponse(200, respRow, action)


@csrf_exempt
def home(request):
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
            if action == 'gettime':
                result = gettime(request)
                return JsonResponse(json.loads(result))
            elif action == "get_personal_details":
                result = get_personal_details(request)
                return JsonResponse(json.loads(result))
            elif action == 'education':
                res = education(request)
                return JsonResponse(json.loads(res))
            elif action == 'experience':
                res = experience(request)
                return JsonResponse(json.loads(res))
            elif action == 'skills':
                res = skills(request)
                return JsonResponse(json.loads(res))
            elif action == 'certifications':
                res = certifications(request)
                return JsonResponse(json.loads(res))
            elif action == 'projects':
                res = projects(request)
                return JsonResponse(json.loads(res))
            elif action == 'languages':
                res = languages(request)
                return JsonResponse(json.loads(res))
            elif action == 'example':
                res = example(request)
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
