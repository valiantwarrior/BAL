
import subprocess
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from Modules import extraction as extractor

DEFAULT_ROUTINE_NAME = "Sample Schedules"
DEFUALT_AUTHOR_NAME = "Dmitry klokov"
SPLASH_ACTIVITY_XML = "Android/app/src/main/res/layout/activity_splash.xml"
VALUES_STRINGS_XML = "Android/app/src/main/res/values/strings.xml"

def copy_android_project() :
    
    subprocess.call('xcopy ..\\Android\\* Android\\* /e /h /k /y')


def xml_modification(target, old, new) :
  
    with open(target, 'r') as activity_xml :
        code = activity_xml.read()
    
    with open(target, 'w') as activity_xml :
        code = code.replace(old, new)
        activity_xml.write(code)
   

def main() :
    
    #copy_android_project()

    wp = extractor.init_workout_program()
    
    #xml_modification(SPLASH_ACTIVITY_XML, DEFAULT_ROUTINE_NAME, wp.program_name)
    #xml_modification(SPLASH_ACTIVITY_XML, DEFUALT_AUTHOR_NAME, wp.author)
    #xml_modification(VALUES_STRINGS_XML, DEFAULT_ROUTINE_NAME, wp.program_name)

    #subprocess.call('build.bat')
    

if __name__ == "__main__" :
    main()