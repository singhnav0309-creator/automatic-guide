import requests
import re
import os


user = input("Enter the image name: ")

user_agent = {
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}


url = f"https://www.google.com/search?sca_esv=e70e64ea00d48e9f&rlz=1C1GCEA_enIN1196IN1196&sxsrf=ANbL-n7GElvBIrpTs01KSxsNcMTomOVW3A:1779605883543&udm=2&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpaEWjvZ2Py1XXV8d8KvlI3p-ML-906rRL_m6h4jR-tdCeKIwp94h-QiJ4lJfObsqU79yRFgWBtc5FGpXu1cRl7St18L8nYrByvJY-8silHpqUEqUXiXZ02nRvNaACwtqNcImKCwsq28flpQyz0AUM3s1pfaxQS1GvKuxSwrBicdI76QtFk82TSXO2_bOPaupsfiziow&q={user}&sa=X&ved=2ahUKEwiRkZ3ErNGUAxU2RWwGHcwZDV8QtKgLegQIFBAB&biw=1397&bih=655&dpr=1.38"



response = requests.get(url=url, headers=user_agent).text
pattern = r"[https://.*\.jpg\",[0-9]+,[0-9]]"
image = re.findall(pattern, response)
print(f"Total Images: {len(image)}")
no_of_images = int(input("Enter the number of images to be downloaded: "))

for i in image[:no_of_images]:
       image_url = image[0]

       if image_url.startswith("http"):
           try:
              response = requests.get(image_url, headers=user_agent).text

              image_name = image_url.split("/")[-1]

              with open("{image_name}", "wb") as file:
                file.write(response)
              print("Download:", image_name)

           except Exception as e:
               print("Error:", e)



if image:
    if not os.path.exists(user):
        os.mkdir(user)
        os.chdir(user)

    else:
        os.chdir(user)

print(image_url)

