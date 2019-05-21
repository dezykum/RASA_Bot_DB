from __future__ import absolute_import,division,unicode_literals
# from rasa_core.actions.action import Action
# from rasa_core.events import SlotSet
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import sqlite3

class ActionDb(Action):
    def name(self):
        return 'action_db'
    
    def run(self, dispatcher, tracker, domain):
        db = sqlite3.connect('mydatabase.db')
        print("connected")
        cursor = db.cursor()
        PersonName = tracker.get_slot('empname')
        # q = "select * from employees WHERE name = '{}';".format(PersonName)
        q = "select name,salary,department,position,hireDate from employees WHERE name = '{}';".format(PersonName)

        try:
            cursor.execute(q)
            if cursor.execute(q)==0:
                print("Sorry, could not find any relevant data. Please contact 1234 for further assistance.")
            results = cursor.fetchall()
            # not all(results)
            for row in results:
                empname = row[0].capitalize()
                empsalary = row[1]
                department = row[2]
                position = row[3]
                hiredate = row[4]
                details = ("%s,%d,%s,%s,%s" % (empname,empsalary,department,position,hiredate))
                # details = ("empname=%s,empsalary=%d,department=%s" % (empname,empsalary,department))
                tup = details.split(',')
                print(tup)
        except:
            print ("Error: unable to fetch data")
        finally:
            db.close()
        # response = """The detail is as follows {}.""".format(results)
        # response = """The detail is as follows {}.""".format(details)
        response = """Hi, {0[0]} is a {0[3]} in {0[2]} department, His/Her monthly salary is {0[1]} INR. He/She was hired on {0[4]}. \n""".format(tup)
        dispatcher.utter_message(response)
        return [SlotSet('empname', PersonName)]



        








