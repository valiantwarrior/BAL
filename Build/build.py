import pprint
import subprocess
import sys, os
import jsonpickle
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from Modules import extraction as extractor
from Modules.Classes import bal_workout_program

DEFAULT_ROUTINE_NAME = "Sample Schedules"
DEFUALT_AUTHOR_NAME = "Dmitry klokov"
SPLASH_ACTIVITY_XML = "Android/app/src/main/res/layout/activity_splash.xml"
VALUES_STRINGS_XML = "Android/app/src/main/res/values/strings.xml"

def copy_android_project() :
    
    subprocess.call('xcopy ..\\Android\\* Android\\* /e /h /k /y')

def copy_json() :
    subprocess.call('xcopy wp.json Android\\app\\src\\main\\python /h /k /y')


def xml_modification(target, old, new) :
  
    with open(target, 'r') as activity_xml :
        code = activity_xml.read()
    
    with open(target, 'w') as activity_xml :
        code = code.replace(old, new)
        activity_xml.write(code)
   

def main() :
    
    copy_android_project()


    wp = extractor.init_workout_program()
    encode = jsonpickle.encode(wp)
  
    with open('wp.json', mode='w', encoding='utf-8') as f :
        f.write(encode)
    
    copy_json()
    
    subprocess.call('build.bat')
    

if __name__ == "__main__" :
    main()