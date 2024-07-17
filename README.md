# gameConversationAI

All commands run in local repository folder

Docker:

Run Docker Desktop

Open terminal in repository

Build image (approx. 2-3mins):
docker buildx build --tag test . 

How to run (approx. 30s-1min):
docker run --name test --rm -p 7860:7860 test:latest 

http://localhost:7860/generate?text="your text"

Swagger:
http://localhost:7860/docs

Ctrl+c on terminal - terminate container
