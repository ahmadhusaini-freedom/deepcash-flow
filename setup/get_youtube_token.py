import os
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
CLIENT_SECRETS_FILE = "setup/client_secret.json"

def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES
    )
    credentials = flow.run_local_server(port=0)
    
    # Simpan token
    with open("setup/youtube_token.json", "w") as token_file:
        token_file.write(credentials.to_json())
    
    print("✅ Token berhasil disimpan di setup/youtube_token.json")

if __name__ == "__main__":
    main() 
