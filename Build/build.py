import subprocess

SPLASH_ACTIVITY_XML = "Android/app/src/main/res/layout/activity_splash.xml"
VALUES_STRINGS_XML = "Android/app/src/main/res/values/strings.xml"

def copy_android_project() :
    
    subprocess.call('xcopy ..\\Android\\* Android\\* /e /h /k /y')


def xml_modification(target, old, new) :
  
    with open(target, 'r') as splash_activity_xml :
        code = splash_activity_xml.read()
    
    with open(target, 'w') as splash_activity_xml :
        code = code.replace(old, new)
        splash_activity_xml.write(code)
   

def main() :
    
    copy_android_project()

    xml_modification(SPLASH_ACTIVITY_XML, 'Sample Schedules', 'Stronglift 5x5')
    xml_modification(VALUES_STRINGS_XML, 'Sample Schedules', 'Stronglift 5x5')

    subprocess.call('build.bat')
    

if __name__ == "__main__" :
    main()