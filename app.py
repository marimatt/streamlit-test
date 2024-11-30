import streamlit as st
import threading
from fastapi import FastAPI
from starlette.responses import JSONResponse
import uvicorn

# Create a FastAPI app
api_app = FastAPI()

@api_app.get("/api/hello")
async def read_hello():
    return JSONResponse(content={"message": "Hello from FastAPI!"})

# Function to run Uvicorn server in a separate thread
def run_api():
    uvicorn.run(api_app, host="0.0.0.0", port=8000)

# Start the FastAPI server
threading.Thread(target=run_api, daemon=True).start()

# Streamlit UI
st.title("Streamlit with FastAPI")
st.write("Go to [localhost:8000/api/hello](http://localhost:8000/api/hello) to test the FastAPI endpoint.")


# from tornado.web import Application, RequestHandler
# from tornado.routing import Rule, PathMatches
# import gc
# import streamlit as st
# from tornado.ioloop import IOLoop

# def main():
#     app = Application()
#     app.listen(8080)
#     IOLoop.current().start()


# @st.cache_resource()
# def setup_api_handler(uri, handler):
#     print("Setup Tornado. Should be called only once")

#     # Get instance of Tornado
#     tornado_app = next(o for o in gc.get_referrers(Application) if o.__class__ is Application)

#     # Setup custom handler
#     tornado_app.wildcard_router.rules.insert(0, Rule(PathMatches(uri), handler))

#     # Start Tornado
#     main()


# class HelloHandler(RequestHandler):
#   def get(self):
#     self.write({'message': 'hello world'})


# if __name__ == '__main__':

#     setup_api_handler('/api/hello', HelloHandler)




# import streamlit as st

# import uvicorn
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# @app.get('/')
# def root():
#     print('Hello World!')
#     return {'Hello': 'World'}


# @app.get('/ciao')
# def say_ciao():
#     print('ciaooo')
#     return {'ciao': 'ciao'}


# if __name__ == '__main__':

#     uvicorn.run(app, host='0.0.0.0', port=8000)
