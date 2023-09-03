import win32com.client
import speech_recognition as sr
import webbrowser
import datetime
import pygame
import os
import requests
from retrying import retry

# Set your Bard API key as an environment variable
os.environ['BARD_API_KEY'] = "aQiQPBEsQGWIHvC41IvFQa9tta_HgLQ5CpnBhpyhe-IBTlarSnMvv3oJf5v8uzy4cd02Tg."

# Define a retry decorator to handle retries with a backoff strategy


@retry(
    stop_max_attempt_number=3,  # Maximum number of retry attempts
    wait_exponential_multiplier=1000,  # Initial backoff delay in milliseconds
    wait_exponential_max=10000  # Maximum backoff delay in milliseconds
)
def get_answer_to_question(question):
    url = "https://api.bard.ai/v2/answer"  # Specify the full URL with https://
    headers = {"Authorization": f"Bearer {os.getenv('BARD_API_KEY')}"}
    data = {"question": question}

    # Disable SSL certificate verification by setting verify=False
    response = requests.post(url, headers=headers, data=data, verify=False)

    if response.status_code == 200:
        answer = response.json()["answer"]
        return answer
    else:
        print(f"Error getting answer: {response.status_code}")
        response.raise_for_status()


class Bard:
    @staticmethod
    def get_answer_to_question(question):
        url = "https://api.bard.ai/v2/answer"
        headers = {"Authorization": f"Bearer {os.getenv('BARD_API_KEY')}"}
        data = {"question": question}

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            answer = response.json()["answer"]
            return answer
        else:
            print(f"Error getting answer: {response.status_code}")
            return None


def play_music(music_path):
    music_paths = {
        "Malang Sajna": "C:\\Users\\shrey\\PycharmProjects\\pythonProject\\Malang Sajna(PagalWorld.com.se).mp3",
        "Maan Meri Jaan": "C:\\Users\\shrey\\PycharmProjects\\pythonProject\\Maan Meri Jaan(PagalWorld.com.se).mp3",
        "Tu Hai To Mujhe Phir Aur Kya Chahiye": "C:\\Users\\shrey\\PycharmProjects\\pythonProject\\Tu Hai To Mujhe Phir Aur Kya Chahiye(PagalWorld.com.se).mp3",
        "Raatan Lambiyan": "C:\\Users\\shrey\\PycharmProjects\\pythonProject\\Raatan Lambiyan(PagalWorld.com.se).mp3",
        "Kesariya": "C:\\Users\\shrey\\PycharmProjects\\pythonProject\\Kesariya(PagalWorld.com.se).mp3"
    }

    try:
        if music_path not in music_paths:
            print("The song is not present in the list.")
            return
        pygame.mixer.init()
        pygame.mixer.music.load(music_paths[music_path])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
    except Exception as e:
        print(f"Error playing music: {str(e)}")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(f"Some Error Occurred. Sorry for the inconvenience: {str(e)}")
            return None


def main():
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak("Hello, I am NerdBot AI")

    music_paths = {
        "Malang Sajna": "C:\\Users\\shrey\\PycharmProjects\\pythonProject\\Malang Sajna(PagalWorld.com.se).mp3",
        "Maan Meri Jaan": "C:\\Users\\shrey\\PycharmProjects\\pythonProject\\Maan Meri Jaan(PagalWorld.com.se).mp3",
        "Tu Hai To Mujhe Phir Aur Kya Chahiye": "C:\\Users\\shrey\\PycharmProjects\\pythonProject\\Tu Hai To Mujhe Phir Aur Kya Chahiye(PagalWorld.com.se).mp3",
        "Raatan Lambiyan": "C:\\Users\\shrey\\PycharmProjects\\pythonProject\\Raatan Lambiyan(PagalWorld.com.se).mp3",
        "Kesariya": "C:\\Users\\shrey\\PycharmProjects\\pythonProject\\Kesariya(PagalWorld.com.se).mp3"
    }

    while True:
        print("Listening....")
        user_query = take_command()

        if user_query:
            user_query = user_query.lower()

            if user_query == "more information":
                speaker.Speak("Please ask your question for more information.")
                user_question = take_command()
                if user_question:
                    answer = Bard.get_answer_to_question(user_question)
                    if answer:
                        speaker.Speak(answer)
                    else:
                        speaker.Speak("I couldn't find an answer to your question.")

            elif "open music" in user_query:
                for song in music_paths.keys():
                    if song.lower() in user_query:
                        play_music(song)
                        break
                else:
                    print("Song not found in the list.")

            elif "open" in user_query and "website" in user_query:
                sites = {
                    "Google": "https://www.google.co.in",
                    "Youtube": "https://www.youtube.com",
                    "Whatsapp": "https://web.whatsapp.com",
                    "Instagram": "https://www.instagram.com"
                }
                for site_name, site_url in sites.items():
                    if site_name.lower() in user_query:
                        webbrowser.open(site_url)
                        speaker.Speak(f"Opening {site_name} Ma'am....")

            elif "the time" in user_query:
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M")
                speaker.Speak(f"Ma'am, the time is {current_time}")

            elif "open" in user_query:
                apps = {
                    "Spotify": "C:\\Users\\shrey\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe",
                    "Notepad": "C:\\Users\\shrey\\AppData\\Local\\Microsoft\\WindowsApps\\notepad.exe",
                    "Calculator": "C:\\Windows\\System32\\calc.exe"
                }
                for app_name, app_path in apps.items():
                    if app_name.lower() in user_query:
                        os.startfile(app_path)
                        speaker.Speak(f"Opening {app_name} Ma'am....")


if __name__ == '__main__':
    main()
