def launch_retroko_server():
    # Preparation et execution du serveur app Retroko 
    from fastapi import FastAPI, HTTPException
    from fastapi.responses import RedirectResponse
    app = FastAPI()

    @App.get("/login/wordpress")
    def login_with_wp():
        return RedirectRespons(
            url="https://public-api.wordpress.com/oauth2/authorize?client_id=4402&response_type=code&redirect_uri=http://localhost:8000/callback"
        )
    

    @App.get("/callback")
    def callback(code: str):
        # Faire la demande du code par activation
        return {"status": "recupered"}

    if __name__ == "__main__":
        launch_retroko_server()