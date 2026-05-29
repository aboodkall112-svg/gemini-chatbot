from google import genai

qr = input("Please ask any question: ")
qr = qr.lower()
while qr != "exit" :

    client = genai.Client(api_key="AIzaSyCEsZQmcgiAXvLeRFhGWZzIqE0umDhQ6hM")

    response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=qr
)

    print(response.text)

