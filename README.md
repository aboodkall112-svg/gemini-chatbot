# gemini-chatbot 


## شو هو ال api 

اوك هو انك تشارك الداتا تاعتك من السيرفر او موقع على الكود تاعك 

شو دخالها بال [[AI]] ؟ 

الموديلز زي شات جبت جيمني بتقدر تستخدمهم بالكود تاعك و تعطيهم اكسس على جهازك 

الشرح الي حهمله بسيط و هو كيف تعمل شات بوت بسيط يكون عنده ذاكرة بتقدر توصلها و بنفس الوقت تقدر تعطيه السبب او ليش بدك اياه 

لازم تجيب الapi بالاول 


بعدها بنحملهم ببايثون 
pip install google-genai



##  كيف اعرف الكلاينت ؟ 
```python
client = genai.Client(api_key="")

response = client.models.generate_content(model = "هون الموديل نفسه " , contents = هون السؤال  ,config={"system_instruction" :  هون بحط التعليمات تاعت المودل و شو وظيفته )
```

## كيف نخليه اقرب لشات بوت ؟


اول اشي لازم نخليه بللوب عشان يضل الشات دائم بين الكلاينت و اليوزر 

كيف ؟

نعمل while statement ونخليها True  هيك اللوب بضل شغالة 


عشان نخليه يتذكر الشات القبل لازم نعرف ملف 
```
data = (r'data.json')
```

بعدها بنعمل تجربة عشان بحال صار خطأ 
أول مرة اكيد حيصير خطأ ليش ؟ لانه مافي ملف ذاكرة فا بنعمل هيك
```
try :

    with open(data,"r") as abood :

            history = json.load(abood) 
```
هو هيك حيجرب يقرا متغير  الذاكرة لكن بحكم انه مافي متغير  ذاكرة فا راح يعطي ايرور فا عشان هيك بنحط try 

و بعدها بنعطي
```
except Exception :

    history = []
```
فا بحال ما قرء انه في متغير للذاكرة الي هو هيستوري راح يعرف واحد 

وهو اصلا جوا اللوب فا دايما حيخش ع تراي بس احنا بنستعمله ل اول مرة بس لانه ما حيكون متعرف من الاساس و اذا عرفناه قبل حيكون فاضي و يعطي ايرور 


طيب بعدها شو نعمل ؟
```
 user_input = input()

    if user_input.lower() == "exit":  

        break

    history.append(f"user {user_input}")
```
   طيب هون انا عرفت متغير الي هو الي سؤال المستخدم 
و حطيت اذا كتب exit يطلع من اللوب كاملة و يوقف البرنامج 


بحال ما تحقق الشرط نعمل append لل انبوت تاع اليوزر على متغير الذاكرة عشان يسيف الهاظ 


```
response = client.models.generate_content(model = "هون الموديل نفسه " , contents = هون السؤال  ,config={"system_instruction" :  هون بحط التعليمات تاعت المودل و شو وظيفته )
```
هسا هاي بنخليها باللوب هاي المرة ليش ؟ 

عشان ينعاد و يفوت الاوتبوت دايما على المودل 

بنحط مكان contents الهيستوري نفسه عشان يقدر يقرأه كامل 


## كيف اخزن كل هاظ الحكي بفايل لحال ؟ 

  
```
    with open(data, "w") as f:

        json.dump(history, f)
```

هاي بتخزن بفايل لحال اخر اشي 


## مصادر 

https://pypi.org/project/google-genai/

https://youtu.be/1IYrmTTKOoI?si=RrfY67WybsDz5XVP

https://youtu.be/V_NXT2-QIlE?si=sCyyfosI6zBtddJd

chatGPT

claude 



## full code 
```
from google import genai

import os , json

  

client = genai.Client(api_key="your api ")

  

data = (r'C:\Users\abood\OneDrive\Desktop\Projects\api test\data.json')

  

try :

    with open(data,"r") as abood :

            history = json.load(abood)

  

except Exception :

    history = []

  

while True :

  

    user_input = input()

    if user_input.lower() == "exit":  

        break

    history.append(f"user {user_input}")

  

    answer  = client.models.generate_content(model = "gemini-2.5-flash" ,

                                              contents = history ,

                                              config={"system_instruction":

                                                      """you are a palnets expirt your answrs are only about plants

                                                        // you cant talk about any thing other than plants

                                                      also you might be the lead agent for servel other agents so keep that in mind """})

  

    history.append(f"AI {answer}")

  

    with open(data, "w") as f:

        json.dump(history, f)

  

    print(answer.text)
```
