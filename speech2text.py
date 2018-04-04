#!/usr/bin/env python3

import speech_recognition as sr

def captureAudioToText():
    # obtain audio from the microphone
    r = sr.Recognizer()
    r.energy_threshold = 4000

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Cloud Speech
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
      "type": "service_account",
      "project_id": "braille-printer-1520455659433",
      "private_key_id": "a7d1bcfc0e3e067106ca34c69150bb78f6c049fa",
      "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCuDn/vCgpwBnaC\nrnP339nsVk3ozOrP83R5lCBYk0lYq7Vy30d9hlxWRxH7sD/9Yii2lFRGP/W+u+mL\nUld9GV0L0EYiGT0YEc7uDNWB1RG6YqHY7UbNez0eDPjfmtHqmBrCLuFWx7qQSdyV\nhHMyXwL59mT8yWZROy42mrdzIaQalnNmiDWQZSjtQFMw19bp2Vb+7Aj4UUGjj01x\nxP8W4i69mzgitBgIGvliXfj6uX+MGtazbgDHDvax56fBdAqUf/wCg9xFR0XXPe2m\nL2TKOe5fXxxMJ54MTjxo6gYa01qg/P3dh7jlmkcI9ca1NjbsCCOigd4+PlE+jcMF\n5fjp3EO1AgMBAAECggEAAdBB3KY7TJvXS+5FuWKaMoBbCHQWIDuLo6FQ+EtJ5i7H\n0bNqMHB1cYAFER0ZgD+FEr3skNzQEoAtDe1k3vdO2mAoUuj2E371Vn1IvjUPnbmz\nBlUWj0PbnlQJRcnRqm2SSHf/k2K6WrrXnbExwr0YWq1gCP2Pii92gE16tYGMuarX\njqNZ5GyAe/XJkKIlkSdOI5qIX7Sl1KGTJUbxop2ObGuAn4aMqedPjH1NJWhslA10\nT0l/kkxRfKGtgDUEtu/KAfmtWmoSYWTCEiD5Iuk1629GKNijGNKI2YyBjd5uMyXh\ntalPzMnS/OLlioftDlQXo5EIdocvQXz8WxR6jqMGAQKBgQDh33NcbwLDURDuKhsO\nFAzrmbRhsFDQ6LfMP7byZxi42h5QSr+M3TLyj/PWNupTgyFv/XBxPoojTBuDqSfs\nCfbWk+0HbZEBmSizTFKfjuxPIXmOPcqXwu9jaKDCsWFMO+qA7xOxQJoSqZS+Tn+4\nbaKMpLs3zHJzNue7i7rJpUZNAQKBgQDFRcG7aNgXFL3JuA1gj30UQ2lGVy1qcHU8\nxIxNNg6t0kUXMk5TYub7dk5HfWzTgL7HmMHQ1/pwsMenqyEYvzV//4wF+9s1olGp\n/b5NreUmB4Za9gIRbJAFZYDGDUlKWctfDDAfmeT7jrkp25JYaFi67Ec7kpulypKn\nqdgXSv3StQKBgAjX/OZTmmIXXHhWwbRtaIwY+o0QoDltwzSGEh2vl7I1KBawtotH\nZeVFaaCricU3TynZXHuynSoAotsm1l9RjI6eQBuYWKMdYhCTHnEM4Ye/ocjF9pa2\nlTTpNdIpq8uWVPozYiwAgYfVh/Njk3CfKkwjbwkiQiDst2oKcIfQps4BAoGBAIED\n/xC/H9vwf7LmQTFuhkHzWG1dZGFhTPtCG/P/L5h0lST3jIwyeZfppoZQvBSS9bJ5\n7//S0IJUyy6X19xkaOveSEg9j/7Cup/vSD9rRBsb/r2MeIvGsWYmHRLp643Jrhzq\nTqrMLhprHCQI6uwQyj7teiS23D6QfltS0/Vf4SKlAoGBANJ0/heXj5a2yqHanovN\nuYUQaQKHK8BFsk3hsNng5YLdJ3PjE+wAafHHMWMR4YXfsPpHQf8b9m4Typ0s1xYK\nSnTaUdC5+pUCwNf8abSggqKAgrjwoTpomebqly7XvE0dEGvw2ZAxY5XSMPAS4pvA\nEg+tRs4FVKhI36XFgNDM4MJH\n-----END PRIVATE KEY-----\n",
      "client_email": "brailler@braille-printer-1520455659433.iam.gserviceaccount.com",
      "client_id": "111663903160660268724",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://accounts.google.com/o/oauth2/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/brailler%40braille-printer-1520455659433.iam.gserviceaccount.com"
    }
    """
    recognizedText = ""
    try:
        recognizedText = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))

    return recognizedText
